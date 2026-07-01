#!/usr/bin/env python3
"""Report corpus build progress for yongge-catering-skill."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "references" / "bilibili-season-cases.tsv"
CORPUS = ROOT / "corpus"
AUDIO_DIR = CORPUS / "audio"
TRANSCRIPT_DIR = CORPUS / "transcripts"
NOTE_DIR = CORPUS / "case-notes"
REVIEWED_DIR = CORPUS / "reviewed-case-notes"
PID_PATH = CORPUS / "full_run.pid"
LOG_PATH = CORPUS / "full_run.log"


def read_cases():
    with CASES.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def index_from_name(path):
    try:
        return int(path.name.split("_", 1)[0])
    except Exception:
        return None


def size_mb(paths):
    return sum(p.stat().st_size for p in paths if p.exists()) / 1024 / 1024


def compress_ranges(numbers):
    nums = sorted(set(numbers))
    if not nums:
        return ""
    ranges = []
    start = prev = nums[0]
    for n in nums[1:]:
        if n == prev + 1:
            prev = n
            continue
        ranges.append((start, prev))
        start = prev = n
    ranges.append((start, prev))
    return ", ".join(str(a) if a == b else f"{a}-{b}" for a, b in ranges)


def transcript_duration_hours(paths):
    total = 0.0
    for path in paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        duration = data.get("duration")
        if isinstance(duration, (int, float)):
            total += duration
    return total / 3600


def main():
    cases = read_cases()
    total = len(cases)
    expected = set(range(1, total + 1))

    audio = sorted(AUDIO_DIR.glob("*.m4s"))
    transcripts = sorted(TRANSCRIPT_DIR.glob("*.json"))
    notes = sorted(NOTE_DIR.glob("*.md"))
    reviewed_case_notes = sorted(REVIEWED_DIR.glob("*.md"))

    audio_idx = {index_from_name(p) for p in audio}
    transcript_idx = {index_from_name(p) for p in transcripts}
    note_idx = {index_from_name(p) for p in notes}
    audio_idx.discard(None)
    transcript_idx.discard(None)
    note_idx.discard(None)

    legacy_refined_notes = []
    draft_notes = []
    for note in notes:
        text = note.read_text(encoding="utf-8", errors="ignore")
        if "Draft status: machine-generated" in text:
            draft_notes.append(note)
        else:
            legacy_refined_notes.append(note)

    print("Yongge corpus status")
    print(f"- Total indexed videos: {total}")
    print(f"- Audio downloaded: {len(audio_idx)}/{total}")
    print(f"- Transcripts: {len(transcript_idx)}/{total}")
    print(f"- Case notes: {len(note_idx)}/{total}")
    print(f"- Machine draft notes: {len(draft_notes)}")
    print(f"- Legacy refined notes in case-notes: {len(legacy_refined_notes)}")
    print(f"- Reviewed case notes: {len(reviewed_case_notes)}")
    print(f"- Audio storage: {size_mb(audio):.1f} MB")
    print(f"- Transcript storage: {size_mb(transcripts):.1f} MB")
    print(f"- Transcript duration completed: {transcript_duration_hours(transcripts):.1f} hours")
    if PID_PATH.exists():
        pid_text = PID_PATH.read_text(encoding="utf-8", errors="ignore").strip()
        running = False
        if pid_text.isdigit():
            try:
                os.kill(int(pid_text), 0)
                running = True
            except OSError:
                running = False
        print(f"- Full-run PID: {pid_text or 'unknown'} ({'running' if running else 'not running'})")
    if LOG_PATH.exists():
        print(f"- Full-run log: {LOG_PATH}")

    missing_transcripts = sorted(expected - transcript_idx)
    missing_notes = sorted(expected - note_idx)
    print(f"- Missing transcript ranges: {compress_ranges(missing_transcripts[:80])}")
    if len(missing_transcripts) > 80:
        print(f"  ... plus {len(missing_transcripts) - 80} more indices")
    print(f"- Missing note ranges: {compress_ranges(missing_notes[:80])}")
    if len(missing_notes) > 80:
        print(f"  ... plus {len(missing_notes) - 80} more indices")


if __name__ == "__main__":
    main()
