#!/usr/bin/env python3
"""Search reviewed Yongge case notes by user-case keywords."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "references" / "bilibili-season-cases.tsv"
REVIEWED_DIR = ROOT / "corpus" / "reviewed-case-notes"

DOMAIN_TERMS = [
    "加盟",
    "快招",
    "总部",
    "官网",
    "直营",
    "品牌",
    "合同",
    "退款",
    "奶茶",
    "咖啡",
    "汉堡",
    "炸鸡",
    "火锅",
    "烧烤",
    "烤肉",
    "烤鱼",
    "自助",
    "披萨",
    "米线",
    "面馆",
    "面包",
    "甜品",
    "亏",
    "月亏",
    "每天亏",
    "负债",
    "贷款",
    "借钱",
    "房租",
    "租金",
    "人工",
    "水电",
    "毛利",
    "外卖",
    "平台",
    "接盘",
    "转让",
    "商场",
    "学校",
    "大学",
    "社区",
    "县城",
    "合伙",
    "扩店",
]

FOOD_TERMS = {
    "奶茶",
    "咖啡",
    "汉堡",
    "炸鸡",
    "火锅",
    "烧烤",
    "烤肉",
    "烤鱼",
    "自助",
    "披萨",
    "米线",
    "面馆",
    "面包",
    "甜品",
}

STRUCTURAL_TERMS = {
    "加盟",
    "快招",
    "总部",
    "官网",
    "直营",
    "品牌",
    "月亏",
    "每天亏",
    "负债",
    "贷款",
    "借钱",
    "房租",
    "租金",
    "毛利",
    "接盘",
    "转让",
    "商场",
    "学校",
    "社区",
    "县城",
}


def load_titles() -> dict[int, dict[str, str]]:
    with CASES.open("r", encoding="utf-8", newline="") as f:
        return {int(row["index"]): row for row in csv.DictReader(f, delimiter="\t")}


def tokens_for(query: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z0-9]+|[\u4e00-\u9fff]{2,}|[0-9.]+万|[0-9.]+%", query)
    tokens.extend(term for term in DOMAIN_TERMS if term in query)
    cleaned = []
    for token in tokens:
        token = token.lower().strip()
        if not token:
            continue
        if re.fullmatch(r"\d+", token) and len(token) < 2:
            continue
        cleaned.append(token)
    return list(dict.fromkeys(cleaned))


def case_index(path: Path) -> int:
    return int(path.name.split("_", 1)[0])


def score_case(query_tokens: list[str], title: str, text: str) -> int:
    hay_title = title.lower()
    hay_text = text.lower()
    score = 0
    for token in query_tokens:
        title_hits = hay_title.count(token)
        text_hits = hay_text.count(token)
        if token in FOOD_TERMS:
            score += title_hits * 40
            score += min(text_hits, 10) * 4
        elif token in STRUCTURAL_TERMS:
            score += title_hits * 25
            score += min(text_hits, 12) * 2
        else:
            score += title_hits * 15
            score += min(text_hits, 8)
        if token in hay_text[:2000]:
            score += 5
    return score


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="User case keywords, e.g. '汉堡 加盟 月亏1万 房租高'")
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()

    titles = load_titles()
    tokens = tokens_for(args.query)
    if not tokens:
        raise SystemExit("No searchable tokens found.")

    matches = []
    for path in sorted(REVIEWED_DIR.glob("*.md"), key=case_index):
        idx = case_index(path)
        row = titles.get(idx, {})
        title = row.get("title", path.stem)
        text = path.read_text(encoding="utf-8", errors="ignore")
        score = score_case(tokens, title, text)
        if score > 0:
            matches.append((score, idx, title, row.get("url", ""), path))

    matches.sort(key=lambda item: (-item[0], item[1]))
    print(f"Query tokens: {', '.join(tokens)}")
    print(f"Reviewed cases searched: {len(list(REVIEWED_DIR.glob('*.md')))}")
    print()
    for score, idx, title, url, path in matches[: args.limit]:
        print(f"- score {score:>3} | Case {idx}: {title}")
        print(f"  note: {path}")
        if url:
            print(f"  source: {url}")


if __name__ == "__main__":
    main()
