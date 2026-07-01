#!/usr/bin/env python3
"""Create machine-draft case notes from ASR transcripts.

The output is intentionally labeled as a draft. A human or LLM review pass
should promote only reliable conclusions into references/dialogue-derived-cases.md.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRANSCRIPT_DIR = ROOT / "corpus" / "transcripts"
NOTE_DIR = ROOT / "corpus" / "case-notes"


KEYWORD_GROUPS = {
    "开场/品类/城市": ["什么店", "品类", "城市", "在哪", "哪里", "多大", "面积"],
    "流水/营业额": ["流水", "营业额", "卖多少", "一天卖", "日均", "每天卖", "客单", "单量"],
    "毛利/成本": ["毛利", "成本", "食材", "打包", "平台", "抽", "外卖", "堂食", "满减"],
    "租金/点位": ["房租", "租金", "物业", "商圈", "位置", "门头", "学校", "大学", "商场", "社区"],
    "人工/水电": ["人工", "工资", "几个人", "员工", "水电", "燃气"],
    "投入/现金/负债": ["投了", "投资", "总投", "花了", "负债", "贷款", "借", "现金", "亏"],
    "加盟/总部/品牌": ["加盟", "总部", "官网", "招商", "品牌", "直营", "保证金", "管理费", "设备", "物料"],
    "合同/退款/维权": ["合同", "回收", "退款", "律师", "市场监管", "起诉", "申请", "承诺"],
    "经营参与": ["店长", "托管", "多久来", "自己干", "合伙", "亲戚", "家里"],
    "建议/止损": ["关", "转让", "别干", "不要", "停", "止损", "救", "保本", "回本"],
}


QUESTION_HINTS = [
    "吗",
    "多少钱",
    "多少",
    "在哪",
    "哪里",
    "多大",
    "多久",
    "几个人",
    "是不是",
    "有没有",
    "干啥",
    "为什么",
    "投了",
    "加盟",
    "毛利",
    "房租",
    "租金",
    "人工",
    "水电",
    "流水",
    "总部",
    "官网",
    "合同",
]


def compact_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def time_label(seconds) -> str:
    seconds = int(float(seconds))
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


def segment_line(seg) -> str:
    return f"{time_label(seg['start'])}-{time_label(seg['end'])} {compact_text(seg['text'])}"


def unique_lines(lines, limit):
    seen = set()
    result = []
    for line in lines:
        key = re.sub(r"\d{2}:\d{2}-\d{2}:\d{2} ", "", line)
        key = re.sub(r"\W+", "", key)
        if not key or key in seen:
            continue
        seen.add(key)
        result.append(line)
        if len(result) >= limit:
            break
    return result


def find_keyword_lines(segments, keywords, limit=10):
    lines = []
    for seg in segments:
        text = compact_text(seg["text"])
        if any(k in text for k in keywords):
            lines.append(segment_line(seg))
    return unique_lines(lines, limit)


def find_question_lines(segments, limit=28):
    lines = []
    for seg in segments:
        text = compact_text(seg["text"])
        if any(h in text for h in QUESTION_HINTS):
            if 3 <= len(text) <= 80:
                lines.append(segment_line(seg))
    return unique_lines(lines, limit)


def extract_number_lines(segments, limit=35):
    patterns = [
        r"\d+(?:\.\d+)?\s*(?:万|千|百|块|元|%|％|平|平米|平方|个月|月|年|天|人|个)",
        r"[一二三四五六七八九十百千万]+(?:块|元|万|千|百|平|个月|月|年|天|人|个)",
    ]
    lines = []
    for seg in segments:
        text = compact_text(seg["text"])
        if any(re.search(p, text) for p in patterns):
            lines.append(segment_line(seg))
    return unique_lines(lines, limit)


def infer_tags(title: str, segments) -> list[str]:
    text = title + "\n" + "\n".join(s["text"] for s in segments[:120])
    tags = []
    checks = {
        "亏损门店": ["月亏", "每天亏", "亏"],
        "加盟": ["加盟", "总部", "招商"],
        "选址/租金": ["房租", "租金", "位置", "商圈", "门头"],
        "低毛利": ["毛利20", "毛利率可能20", "毛利率很低", "低毛利"],
        "接盘/转让": ["接盘", "转让"],
        "负债/贷款": ["负债", "贷款", "借钱"],
        "合同/维权": ["合同", "退款", "律师", "市场监管", "回收"],
    }
    for tag, keys in checks.items():
        if any(k in text for k in keys):
            tags.append(tag)
    return tags or ["待分类"]


def make_note(transcript_path: Path, output_dir: Path, overwrite=False) -> Path:
    data = json.loads(transcript_path.read_text(encoding="utf-8"))
    source = data["source"]
    segments = data.get("segments", [])
    index = source["index"]
    bvid = source["bvid"]
    out = output_dir / f"{index}_{bvid}.md"
    if out.exists() and not overwrite:
        return out

    output_dir.mkdir(parents=True, exist_ok=True)
    tags = infer_tags(source["title"], segments)
    number_lines = extract_number_lines(segments)
    question_lines = find_question_lines(segments)

    groups = []
    for group, keywords in KEYWORD_GROUPS.items():
        lines = find_keyword_lines(segments, keywords, limit=8)
        if lines:
            groups.append((group, lines))

    duration = data.get("duration")
    duration_text = f"{duration / 60:.1f} min" if isinstance(duration, (int, float)) else "unknown"
    asr = data.get("asr") or {}

    lines = [
        f"# {source['title']}",
        "",
        f"- Source: {source['url']}",
        f"- Transcript: ../transcripts/{transcript_path.name}",
        f"- Duration: {duration_text}",
        f"- ASR: {asr.get('engine', 'unknown')} {asr.get('model_size', '')}".strip(),
        f"- Draft status: machine-generated; requires review before promotion.",
        f"- Tags: {', '.join(tags)}",
        "",
        "## Extracted Numbers And Facts",
        "",
    ]
    lines.extend([f"- {line}" for line in number_lines] or ["- No obvious numeric facts extracted."])
    lines.extend(["", "## Likely Yongge Question Order", ""])
    lines.extend([f"- {line}" for line in question_lines] or ["- No question-like lines extracted."])

    lines.extend(["", "## Keyword Evidence", ""])
    for group, group_lines in groups:
        lines.extend([f"### {group}", ""])
        lines.extend([f"- {line}" for line in group_lines])
        lines.append("")

    lines.extend(
        [
            "## Draft User Facts",
            "",
            "- Review the extracted numbers and keyword evidence, then rewrite this section into clean facts.",
            "",
            "## Draft Diagnosis",
            "",
            "- Identify whether the case is mainly about unit economics, location, franchise risk, owner involvement, contract risk, or sunk-cost stop-loss.",
            "",
            "## Draft Recommendation",
            "",
            "- Convert the diagnosis into a direct action: continue, test, fix, transfer, close, verify brand, preserve evidence, or seek legal consultation.",
            "",
            "## Reusable Heuristics",
            "",
            "- Promote only verified patterns into references/dialogue-derived-cases.md.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("transcripts", nargs="*", type=Path)
    parser.add_argument("--all", action="store_true", help="Process every transcript in corpus/transcripts.")
    parser.add_argument("--output-dir", type=Path, default=NOTE_DIR)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    transcript_paths = args.transcripts
    if args.all:
        transcript_paths = sorted(TRANSCRIPT_DIR.glob("*.json"), key=lambda p: int(p.name.split("_", 1)[0]))
    if not transcript_paths:
        raise SystemExit("Provide transcript paths or --all.")

    for path in transcript_paths:
        out = make_note(path, args.output_dir, overwrite=args.overwrite)
        print(out)


if __name__ == "__main__":
    main()
