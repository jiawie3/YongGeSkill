#!/usr/bin/env python3
"""Start or monitor the full Yongge Bilibili corpus build.

Default behavior:
- If a full-run process is already alive, report it and exit.
- Otherwise launch the corpus pipeline in a detached background session.
- The underlying pipeline skips existing transcripts/notes unless --overwrite is used.
"""

from __future__ import annotations

import argparse
import csv
import os
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
CASES = ROOT / "references" / "bilibili-season-cases.tsv"
CORPUS = ROOT / "corpus"
PID_PATH = CORPUS / "full_run.pid"
LOG_PATH = CORPUS / "full_run.log"
PIPELINE = ROOT / "scripts" / "bilibili_corpus_pipeline.py"
STATUS = ROOT / "scripts" / "corpus_status.py"


def is_pid_running(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def current_pid() -> int | None:
    if not PID_PATH.exists():
        return None
    text = PID_PATH.read_text(encoding="utf-8", errors="ignore").strip()
    if not text.isdigit():
        return None
    return int(text)


def total_cases() -> int:
    with CASES.open("r", encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f, delimiter="\t"))


def python_executable() -> str:
    venv_python = WORKSPACE / ".venv" / "bin" / "python"
    if venv_python.exists():
        return str(venv_python)
    return sys.executable


def print_status():
    py = python_executable()
    subprocess.run([py, str(STATUS)], cwd=str(WORKSPACE), check=False)


def build_command(args) -> list[str]:
    cmd = [
        python_executable(),
        str(PIPELINE),
        "--download",
        "--transcribe",
        "--draft-note",
        "--model-size",
        args.model_size,
        "--sleep-seconds",
        str(args.sleep_seconds),
        "--error-sleep-seconds",
        str(args.error_sleep_seconds),
        "--max-consecutive-errors",
        str(args.max_consecutive_errors),
    ]
    if args.indices:
        cmd.extend(["--indices", args.indices])
    else:
        cmd.extend(
            [
                "--start-index",
                str(args.start_index),
                "--end-index",
                str(args.end_index or total_cases()),
            ]
        )
    if args.overwrite:
        cmd.append("--overwrite")
    return cmd


def start_background(args):
    CORPUS.mkdir(parents=True, exist_ok=True)
    pid = current_pid()
    if pid and is_pid_running(pid) and not args.force:
        print(f"Full corpus run is already running: pid={pid}")
        print_status()
        return 0

    cmd = build_command(args)
    with LOG_PATH.open("ab", buffering=0) as log:
        log.write(
            f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] run_full_corpus launching: {' '.join(cmd)}\n".encode()
        )
        proc = subprocess.Popen(
            cmd,
            cwd=str(WORKSPACE),
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=subprocess.STDOUT,
            start_new_session=True,
            close_fds=True,
            env={**os.environ, "PYTHONUNBUFFERED": "1"},
        )
    PID_PATH.write_text(str(proc.pid), encoding="utf-8")
    print(f"Started full corpus run: pid={proc.pid}")
    print(f"Log: {LOG_PATH}")
    return 0


def run_foreground(args):
    cmd = build_command(args)
    print(f"Running foreground: {' '.join(cmd)}", flush=True)
    return subprocess.call(cmd, cwd=str(WORKSPACE))


def main():
    parser = argparse.ArgumentParser(description="Run the full Yongge corpus build.")
    parser.add_argument("--start-index", type=int, default=1)
    parser.add_argument("--end-index", type=int)
    parser.add_argument("--indices", help="Comma-separated case indices to process.")
    parser.add_argument("--model-size", default="small")
    parser.add_argument("--sleep-seconds", type=float, default=1.0)
    parser.add_argument("--error-sleep-seconds", type=float, default=120.0)
    parser.add_argument("--max-consecutive-errors", type=int, default=8)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--foreground", action="store_true", help="Run in the current terminal instead of background.")
    parser.add_argument("--force", action="store_true", help="Start even if the PID file points to a live process.")
    parser.add_argument("--status", action="store_true", help="Only print corpus status.")
    args = parser.parse_args()

    if args.status:
        print_status()
        return 0
    if args.foreground:
        return run_foreground(args)
    return start_background(args)


if __name__ == "__main__":
    raise SystemExit(main())
