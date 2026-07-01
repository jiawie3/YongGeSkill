#!/usr/bin/env python3
"""Build a dialogue-level corpus from public Bilibili video metadata.

This script intentionally stores raw transcripts under corpus/ instead of
loading them into SKILL.md. The skill should use distilled case notes, while
raw transcripts remain auditable source material.
"""

from __future__ import annotations

import argparse
import csv
import json
import http.client
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "references" / "bilibili-season-cases.tsv"
CORPUS = ROOT / "corpus"
AUDIO_DIR = CORPUS / "audio"
TRANSCRIPT_DIR = CORPUS / "transcripts"
NOTE_DIR = CORPUS / "case-notes"
STATUS_PATH = CORPUS / "status.jsonl"


UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36"


def load_cases(limit: int | None = None):
    with CASES.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    return rows[:limit] if limit else rows


def request_json(url: str, referer: str, retries=3):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Referer": referer,
            "Origin": "https://www.bilibili.com",
        },
    )
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8", "ignore"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(2 * attempt)
    raise last_error


def get_subtitles(row):
    url = f"https://api.bilibili.com/x/player/v2?aid={row['aid']}&cid={row['cid']}"
    data = request_json(url, row["url"])
    return (data.get("data") or {}).get("subtitle", {}).get("subtitles", []) or []


def get_audio_url(row):
    url = (
        "https://api.bilibili.com/x/player/playurl"
        f"?bvid={row['bvid']}&cid={row['cid']}&fnval=16&fnver=0&fourk=1"
    )
    data = request_json(url, row["url"])
    if data.get("code") != 0:
        raise RuntimeError(f"playurl failed: {data.get('code')} {data.get('message')}")
    dash = (data.get("data") or {}).get("dash") or {}
    audio = dash.get("audio") or []
    if not audio:
        raise RuntimeError("no audio stream in playurl response")
    best = sorted(audio, key=lambda x: x.get("bandwidth") or 0, reverse=True)[0]
    return best.get("baseUrl") or best.get("base_url")


def download_audio(row, overwrite=False, retries=3):
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    path = AUDIO_DIR / f"{row['index']}_{row['bvid']}.m4s"
    part_path = AUDIO_DIR / f"{row['index']}_{row['bvid']}.m4s.part"
    if path.exists() and path.stat().st_size > 1024 and not overwrite:
        return path
    if part_path.exists():
        part_path.unlink()
    audio_url = get_audio_url(row)
    req = urllib.request.Request(
        audio_url,
        headers={
            "User-Agent": UA,
            "Referer": row["url"],
            "Origin": "https://www.bilibili.com",
            "Range": "bytes=0-",
        },
    )
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp, part_path.open("wb") as out:
                out.write(resp.read())
            part_path.replace(path)
            return path
        except (urllib.error.URLError, TimeoutError, http.client.IncompleteRead) as exc:
            last_error = exc
            for incomplete in (path, part_path):
                if incomplete.exists():
                    incomplete.unlink()
            if attempt < retries:
                time.sleep(3 * attempt)
    raise last_error
    return path


def transcribe_audio(row, audio_path, model_size="base", overwrite=False):
    TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = TRANSCRIPT_DIR / f"{row['index']}_{row['bvid']}.json"
    if out_path.exists() and not overwrite:
        return out_path
    model = get_model(model_size)
    segments, info = model.transcribe(
        str(audio_path),
        language="zh",
        vad_filter=True,
        beam_size=5,
        condition_on_previous_text=False,
    )
    result = {
        "source": {
            "index": row["index"],
            "bvid": row["bvid"],
            "aid": row["aid"],
            "cid": row["cid"],
            "title": row["title"],
            "url": row["url"],
        },
        "language": info.language,
        "language_probability": info.language_probability,
        "duration": info.duration,
        "asr": {
            "engine": "faster-whisper",
            "model_size": model_size,
            "language": "zh",
            "vad_filter": True,
            "compute_type": "int8",
        },
        "segments": [
            {"start": s.start, "end": s.end, "text": s.text.strip()} for s in segments
        ],
    }
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path


_MODEL_CACHE = {}


def get_model(model_size):
    if model_size in _MODEL_CACHE:
        return _MODEL_CACHE[model_size]
    try:
        from faster_whisper import WhisperModel
    except Exception as exc:  # pragma: no cover - dependency guard
        raise RuntimeError(
            "Install faster-whisper in the active Python environment first."
        ) from exc
    model = WhisperModel(model_size, device="auto", compute_type="int8")
    _MODEL_CACHE[model_size] = model
    return model


def write_note_skeleton(row, transcript_path=None):
    NOTE_DIR.mkdir(parents=True, exist_ok=True)
    out_path = NOTE_DIR / f"{row['index']}_{row['bvid']}.md"
    if out_path.exists():
        return out_path
    transcript_ref = transcript_path.name if transcript_path else ""
    out_path.write_text(
        f"""# {row['title']}

- Source: {row['url']}
- Transcript: ../transcripts/{transcript_ref}

## User Facts

- TODO

## Yongge Questions

- TODO

## Calculations Or Business Logic

- TODO

## Diagnosis

- TODO

## Recommendation

- TODO

## Reusable Heuristics

- TODO
""",
        encoding="utf-8",
    )
    return out_path


def write_draft_note(transcript_path, overwrite=False):
    script = ROOT / "scripts" / "draft_case_notes.py"
    cmd = [sys.executable, str(script), str(transcript_path)]
    if overwrite:
        cmd.append("--overwrite")
    completed = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return completed.stdout.strip().splitlines()[-1]


def record_status(row, status, detail):
    CORPUS.mkdir(parents=True, exist_ok=True)
    with STATUS_PATH.open("a", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {
                    "time": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "index": row["index"],
                    "bvid": row["bvid"],
                    "status": status,
                    "detail": str(detail),
                },
                ensure_ascii=False,
            )
            + "\n"
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, help="Process only the first N cases.")
    parser.add_argument("--start-index", type=int, default=1)
    parser.add_argument("--end-index", type=int, help="Process up to this inclusive case index.")
    parser.add_argument("--indices", help="Comma-separated 1-based case indices to process, e.g. 260,283,287.")
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--transcribe", action="store_true")
    parser.add_argument("--draft-note", action="store_true", help="Generate a machine-draft case note from each transcript.")
    parser.add_argument("--model-size", default="small")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--sleep-seconds", type=float, default=1.0, help="Pause between videos to reduce request pressure.")
    parser.add_argument("--error-sleep-seconds", type=float, default=60.0, help="Pause after a video-level error.")
    parser.add_argument("--max-consecutive-errors", type=int, default=8, help="Stop the batch after this many consecutive video-level errors.")
    args = parser.parse_args()

    rows = load_cases(args.limit)
    if args.indices:
        wanted = {int(x.strip()) for x in args.indices.split(",") if x.strip()}
        rows = [r for r in rows if int(r["index"]) in wanted]
    else:
        rows = [r for r in rows if int(r["index"]) >= args.start_index]
        if args.end_index:
            rows = [r for r in rows if int(r["index"]) <= args.end_index]
    total = len(rows)
    consecutive_errors = 0
    for offset, row in enumerate(rows, 1):
        started = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{started}] {offset}/{total} index={row['index']} bvid={row['bvid']} start: {row['title']}", flush=True)
        try:
            subtitles = get_subtitles(row)
            if subtitles:
                record_status(row, "subtitle_available", subtitles)
            audio_path = None
            transcript_path = None
            if args.download or args.transcribe:
                audio_path = download_audio(row, overwrite=args.overwrite)
                record_status(row, "audio_downloaded", audio_path)
            if args.transcribe:
                transcript_path = transcribe_audio(
                    row, audio_path, model_size=args.model_size, overwrite=args.overwrite
                )
                record_status(row, "transcribed", transcript_path)
            if args.draft_note and transcript_path:
                note_path = write_draft_note(transcript_path, overwrite=args.overwrite)
                record_status(row, "draft_note", note_path)
            else:
                note_path = write_note_skeleton(row, transcript_path)
                record_status(row, "note_skeleton", note_path)
            consecutive_errors = 0
            finished = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{finished}] {offset}/{total} index={row['index']} done", flush=True)
        except Exception as exc:
            consecutive_errors += 1
            record_status(row, "error", repr(exc))
            print(
                f"[ERROR] {row['index']} {row['bvid']}: {exc} "
                f"(consecutive_errors={consecutive_errors})",
                file=sys.stderr,
                flush=True,
            )
            if args.error_sleep_seconds > 0:
                time.sleep(args.error_sleep_seconds)
            if args.max_consecutive_errors and consecutive_errors >= args.max_consecutive_errors:
                print(
                    f"[STOP] reached max consecutive errors ({args.max_consecutive_errors}); "
                    "stop this batch and resume later.",
                    file=sys.stderr,
                    flush=True,
                )
                break
        if args.sleep_seconds > 0 and offset < total:
            time.sleep(args.sleep_seconds)


if __name__ == "__main__":
    main()
