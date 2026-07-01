#!/usr/bin/env python3
"""Build a review backlog for machine-draft Yongge case notes."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "references" / "bilibili-season-cases.tsv"
NOTE_DIR = ROOT / "corpus" / "case-notes"
TRANSCRIPT_DIR = ROOT / "corpus" / "transcripts"
REVIEWED_DIR = ROOT / "corpus" / "reviewed-case-notes"
OUT_PATH = ROOT / "references" / "corpus-review-backlog.md"


PRIORITY_RULES = [
    ("P0", "加盟/快招/总部", re.compile(r"加盟|总部|快招|招商|品牌|官网|退款|合同|保证金")),
    ("P0", "亏损/止损", re.compile(r"月亏|每天亏|亏损|亏光|赔光|倒闭|关店|转让")),
    ("P1", "重投入/负债", re.compile(r"\d+\s*万|负债|贷款|抵押|借")),
    ("P1", "选址/租金/接盘", re.compile(r"房租|租金|位置|选址|接盘|转店|转让费|商场|学校")),
    ("P2", "经营/扩店/合伙", re.compile(r"合伙|扩店|店长|员工|托管|代管|亲戚|夫妻")),
]


def read_rows() -> list[dict[str, str]]:
    with CASES.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def first_existing(directory: Path, index: str, suffix: str) -> Path | None:
    matches = sorted(directory.glob(f"{index}_*{suffix}"))
    return matches[0] if matches else None


def note_status(note: Path | None, reviewed: Path | None) -> str:
    if reviewed:
        return "reviewed"
    if not note:
        return "missing-note"
    text = note.read_text(encoding="utf-8", errors="ignore")
    if "Draft status: machine-generated" in text:
        return "machine-draft"
    return "legacy-reviewed"


def classify(title: str) -> tuple[str, str]:
    hits = []
    rank = "P3"
    for priority, label, pattern in PRIORITY_RULES:
        if pattern.search(title):
            hits.append(label)
            if priority < rank:
                rank = priority
    return rank, "、".join(dict.fromkeys(hits)) or "待人工判断"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT_PATH)
    args = parser.parse_args()

    REVIEWED_DIR.mkdir(parents=True, exist_ok=True)
    rows = read_rows()
    counts: dict[str, int] = {}
    backlog = []
    for row in rows:
        index = row["index"]
        transcript = first_existing(TRANSCRIPT_DIR, index, ".json")
        note = first_existing(NOTE_DIR, index, ".md")
        reviewed = first_existing(REVIEWED_DIR, index, ".md")
        status = note_status(note, reviewed)
        priority, labels = classify(row["title"])
        counts[status] = counts.get(status, 0) + 1
        backlog.append((priority, int(index), row, transcript, note, reviewed, status, labels))

    backlog.sort(key=lambda item: (item[0], item[1]))

    lines = [
        "# Corpus Review Backlog",
        "",
        "This is the working queue for turning machine-draft notes into reviewed case notes.",
        "Do not treat `machine-draft` rows as human-refined knowledge.",
        "",
        "## Status Summary",
        "",
    ]
    for key in ["reviewed", "legacy-reviewed", "machine-draft", "missing-note"]:
        lines.append(f"- {key}: {counts.get(key, 0)}")

    lines.extend(
        [
            "",
            "## Queue",
            "",
            "| Priority | Index | Status | Labels | Title | Draft | Reviewed | Transcript |",
            "| --- | ---: | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for priority, index, row, transcript, note, reviewed, status, labels in backlog:
        title = row["title"].replace("|", "\\|")
        draft_link = f"../corpus/case-notes/{note.name}" if note else ""
        reviewed_link = f"../corpus/reviewed-case-notes/{reviewed.name}" if reviewed else ""
        transcript_link = f"../corpus/transcripts/{transcript.name}" if transcript else ""
        lines.append(
            f"| {priority} | {index} | {status} | {labels} | {title} | "
            f"{draft_link} | {reviewed_link} | {transcript_link} |"
        )

    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
