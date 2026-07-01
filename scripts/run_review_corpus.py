#!/usr/bin/env python3
"""Drive the reviewed-note pass for the full Yongge corpus.

This script does not promote machine drafts by renaming them. It either
prepares one-case review prompts or, with --run-codex, invokes Codex to read
the ASR transcript plus machine draft and write a real reviewed case note.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shlex
import shutil
import signal
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
CASES = ROOT / "references" / "bilibili-season-cases.tsv"
CORPUS = ROOT / "corpus"
NOTE_DIR = CORPUS / "case-notes"
TRANSCRIPT_DIR = CORPUS / "transcripts"
REVIEWED_DIR = CORPUS / "reviewed-case-notes"
PROMPT_DIR = CORPUS / "review-prompts"
LAST_MESSAGE_DIR = CORPUS / "review-last-messages"
PID_PATH = CORPUS / "review_run.pid"
BG_PID_PATH = CORPUS / "review_bg.pid"
LOG_PATH = CORPUS / "review_run.jsonl"
RUNNER_OUT = CORPUS / "review_runner.out"
BACKLOG_SCRIPT = ROOT / "scripts" / "build_review_backlog.py"


PRIORITY_RULES = [
    ("P0", "加盟/快招/总部", re.compile(r"加盟|总部|快招|招商|品牌|官网|退款|合同|保证金")),
    ("P0", "亏损/止损", re.compile(r"月亏|每天亏|亏损|亏光|赔光|倒闭|关店|转让")),
    ("P1", "重投入/负债", re.compile(r"\d+\s*万|负债|贷款|抵押|借")),
    ("P1", "选址/租金/接盘", re.compile(r"房租|租金|位置|选址|接盘|转店|转让费|商场|学校")),
    ("P2", "经营/扩店/合伙", re.compile(r"合伙|扩店|店长|员工|托管|代管|亲戚|夫妻")),
]

REQUIRED_REVIEW_SECTIONS = [
    "## User Facts Extracted",
    "## Yongge Question Order",
    "## Calculation Logic",
    "## Diagnosis",
    "## Recommendation Pattern",
    "## Reusable Heuristics",
]


@dataclass(frozen=True)
class CaseItem:
    index: int
    bvid: str
    title: str
    url: str
    priority: str
    labels: str
    draft: Path
    transcript: Path
    reviewed: Path


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def read_rows() -> list[dict[str, str]]:
    with CASES.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def first_existing(directory: Path, index: int, suffix: str) -> Path | None:
    matches = sorted(directory.glob(f"{index}_*{suffix}"))
    return matches[0] if matches else None


def classify(title: str) -> tuple[str, str]:
    hits = []
    rank = "P3"
    for priority, label, pattern in PRIORITY_RULES:
        if pattern.search(title):
            hits.append(label)
            if priority < rank:
                rank = priority
    return rank, "、".join(dict.fromkeys(hits)) or "待人工判断"


def build_items() -> list[CaseItem]:
    items: list[CaseItem] = []
    for row in read_rows():
        index = int(row["index"])
        bvid = row["bvid"]
        draft = first_existing(NOTE_DIR, index, ".md") or NOTE_DIR / f"{index}_{bvid}.md"
        transcript = first_existing(TRANSCRIPT_DIR, index, ".json") or TRANSCRIPT_DIR / f"{index}_{bvid}.json"
        reviewed = REVIEWED_DIR / f"{index}_{bvid}.md"
        priority, labels = classify(row["title"])
        items.append(
            CaseItem(
                index=index,
                bvid=bvid,
                title=row["title"],
                url=row["url"],
                priority=priority,
                labels=labels,
                draft=draft,
                transcript=transcript,
                reviewed=reviewed,
            )
        )
    return items


def is_process_running(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True


def pid_status(path: Path = PID_PATH) -> tuple[str, int | None]:
    if not path.exists():
        return "not-running", None
    text = path.read_text(encoding="utf-8", errors="ignore").strip()
    if not text.isdigit():
        return "stale", None
    pid = int(text)
    return ("running" if is_process_running(pid) else "stale", pid)


def acquire_pid(force: bool = False) -> None:
    state, pid = pid_status()
    if state == "running" and not force:
        raise SystemExit(f"review runner already running: pid={pid}")
    PID_PATH.parent.mkdir(parents=True, exist_ok=True)
    PID_PATH.write_text(str(os.getpid()) + "\n", encoding="utf-8")


def release_pid() -> None:
    try:
        text = PID_PATH.read_text(encoding="utf-8", errors="ignore").strip()
    except FileNotFoundError:
        return
    if text == str(os.getpid()):
        PID_PATH.unlink()


def write_log(event: str, **fields) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {"time": now_iso(), "event": event, **fields}
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")


def validate_reviewed(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"missing reviewed note: {path}"]
    text = path.read_text(encoding="utf-8", errors="ignore")
    if len(text) < 1200:
        errors.append("reviewed note is too short")
    if "Draft status: machine-generated" in text:
        errors.append("reviewed note still contains machine-draft marker")
    for needle in ["- Source:", "- Raw ASR:", "- Machine draft:", "- Review status:", "- Reliability:"]:
        if needle not in text:
            errors.append(f"missing metadata line: {needle}")
    for section in REQUIRED_REVIEW_SECTIONS:
        if section not in text:
            errors.append(f"missing section: {section}")
    return errors


def prompt_for_case(item: CaseItem) -> str:
    return f"""你正在维护 `/Users/didi/Documents/idea/yongge-catering-skill` 这个 Codex skill 的勇哥案例知识库。

任务：对第 {item.index} 条视频做一次人工精修式审校，产出 reviewed case note。

只允许创建或覆盖这个文件：
`{item.reviewed}`

必须读取并基于这些真实材料：
- ASR transcript JSON: `{item.transcript}`
- Machine draft note: `{item.draft}`

不要修改 `SKILL.md`、`references/dialogue-derived-cases.md`、`references/corpus-review-backlog.md` 或其他案例文件。
不要把机器初稿直接搬过去。必须回看 transcript，把事实、追问顺序、算账逻辑、诊断、建议和可迁移规则重新整理。

输出文件必须使用下面结构：

```markdown
# Case {item.index}: 简短中文标题

- Source: {item.url}
- Raw ASR: `../transcripts/{item.transcript.name}`
- Machine draft: `../case-notes/{item.draft.name}`
- Review status: reviewed from ASR transcript.
- Reliability: ...

## User Facts Extracted

## Yongge Question Order

## Calculation Logic

## Diagnosis

## Recommendation Pattern

## Reusable Heuristics
```

质量要求：
- 使用简体中文为主，保留必要餐饮术语。
- 不编造 transcript 里没有的数字；不确定就写 ASR 粗糙或未确认。
- 数字要尽量换算为日/月口径，如租金/人工/水电/毛利/亏损/保本流水。
- 重点提炼“勇哥怎么问、怎么判断、为什么这么建议”，不是复述故事。
- 不要引用长段原文，不要写娱乐化辱骂，只保留可用于 skill 的方法。
- 如果案例不是亏损门店，也要写清楚它对后续用户咨询有什么可复用规则。

完成后最终回复一行：`reviewed {item.index} {item.reviewed}`。
"""


def write_prompt(item: CaseItem, prompt: str) -> Path:
    PROMPT_DIR.mkdir(parents=True, exist_ok=True)
    path = PROMPT_DIR / f"{item.index}_{item.bvid}.prompt.md"
    path.write_text(prompt, encoding="utf-8")
    return path


def rebuild_backlog() -> None:
    subprocess.run(
        [sys.executable, str(BACKLOG_SCRIPT)],
        cwd=str(WORKSPACE),
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def codex_binary(explicit: str | None) -> str:
    if explicit:
        return explicit
    found = shutil.which("codex")
    if found:
        return found
    fallback = "/Applications/Codex.app/Contents/Resources/codex"
    if Path(fallback).exists():
        return fallback
    raise SystemExit("codex binary not found; use --codex-bin")


def child_args_without_background(raw_args: list[str]) -> list[str]:
    child_args: list[str] = []
    skip_next = False
    for arg in raw_args:
        if skip_next:
            skip_next = False
            continue
        if arg == "--background":
            continue
        if arg == "--background-log":
            skip_next = True
            continue
        if arg.startswith("--background-log="):
            continue
        child_args.append(arg)
    return child_args


def launch_background(raw_args: list[str], args) -> None:
    if args.status:
        raise SystemExit("--background cannot be combined with --status")

    state, pid = pid_status()
    if state == "running" and not args.force_pid:
        raise SystemExit(f"review runner already running: pid={pid}")

    log_path = Path(args.background_log).expanduser()
    if not log_path.is_absolute():
        log_path = (WORKSPACE / log_path).resolve()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    BG_PID_PATH.parent.mkdir(parents=True, exist_ok=True)

    child_args = child_args_without_background(raw_args)
    cmd = [sys.executable, str(Path(__file__).resolve()), *child_args]

    with log_path.open("a", encoding="utf-8") as log:
        quoted = " ".join(shlex.quote(part) for part in cmd)
        log.write(f"\n[{now_iso()}] background launch: {quoted}\n")
        log.flush()
        proc = subprocess.Popen(
            cmd,
            cwd=str(WORKSPACE),
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=subprocess.STDOUT,
            start_new_session=True,
            close_fds=True,
        )

    BG_PID_PATH.write_text(str(proc.pid) + "\n", encoding="utf-8")
    time.sleep(0.7)
    if proc.poll() is not None:
        try:
            BG_PID_PATH.unlink()
        except FileNotFoundError:
            pass
        raise SystemExit(f"background runner exited immediately: returncode={proc.returncode}; see {log_path}")

    print(f"Started background reviewed-note runner: pid={proc.pid}")
    print(f"- Background PID file: {BG_PID_PATH}")
    print(f"- Run PID lock: {PID_PATH}")
    print(f"- Log: {log_path}")


def run_codex(item: CaseItem, prompt: str, args) -> int:
    LAST_MESSAGE_DIR.mkdir(parents=True, exist_ok=True)
    last_message = LAST_MESSAGE_DIR / f"{item.index}_{item.bvid}.last.md"
    cmd = [
        codex_binary(args.codex_bin),
        "exec",
        "-C",
        str(WORKSPACE),
        "--skip-git-repo-check",
        "--ephemeral",
        "--dangerously-bypass-approvals-and-sandbox",
        "-s",
        "danger-full-access",
        "-o",
        str(last_message),
        "-",
    ]
    if args.codex_model:
        cmd[2:2] = ["-m", args.codex_model]

    write_log("codex_start", index=item.index, bvid=item.bvid, reviewed=str(item.reviewed))
    started = time.time()
    try:
        proc = subprocess.run(
            cmd,
            input=prompt,
            text=True,
            capture_output=True,
            timeout=args.timeout_seconds,
            cwd=str(WORKSPACE),
        )
    except subprocess.TimeoutExpired as exc:
        write_log("codex_timeout", index=item.index, bvid=item.bvid, timeout_seconds=args.timeout_seconds)
        if exc.stdout:
            write_log("codex_stdout_tail", index=item.index, text=str(exc.stdout)[-4000:])
        if exc.stderr:
            write_log("codex_stderr_tail", index=item.index, text=str(exc.stderr)[-4000:])
        return 124

    elapsed = round(time.time() - started, 1)
    if proc.stdout:
        write_log("codex_stdout_tail", index=item.index, text=proc.stdout[-4000:])
    if proc.stderr:
        write_log("codex_stderr_tail", index=item.index, text=proc.stderr[-4000:])
    write_log("codex_exit", index=item.index, bvid=item.bvid, returncode=proc.returncode, elapsed_seconds=elapsed)
    return proc.returncode


def select_items(args) -> list[CaseItem]:
    items = build_items()
    if args.indices:
        wanted = {int(part) for part in re.split(r"[,\s]+", args.indices.strip()) if part}
        items = [item for item in items if item.index in wanted]
    if args.start_index is not None:
        items = [item for item in items if item.index >= args.start_index]
    if args.end_index is not None:
        items = [item for item in items if item.index <= args.end_index]
    if args.priority:
        allowed = {p.strip() for p in args.priority.split(",") if p.strip()}
        items = [item for item in items if item.priority in allowed]
    if not args.include_reviewed:
        items = [item for item in items if not item.reviewed.exists()]
    items = [item for item in items if item.draft.exists() and item.transcript.exists()]
    items.sort(key=lambda item: (item.priority, item.index))
    if args.limit is not None:
        items = items[: args.limit]
    return items


def print_status() -> None:
    items = build_items()
    reviewed = [item for item in items if item.reviewed.exists()]
    missing_inputs = [item for item in items if not item.draft.exists() or not item.transcript.exists()]
    remaining = [item for item in items if not item.reviewed.exists() and item not in missing_inputs]
    remaining.sort(key=lambda item: (item.priority, item.index))
    state, pid = pid_status()
    bg_state, bg_pid = pid_status(BG_PID_PATH)
    print("Yongge reviewed-note run status")
    print(f"- Total indexed videos: {len(items)}")
    print(f"- Reviewed notes: {len(reviewed)}/{len(items)}")
    print(f"- Remaining reviewable notes: {len(remaining)}")
    print(f"- Missing input cases: {len(missing_inputs)}")
    print(f"- Review-run PID: {pid or ''} ({state})")
    print(f"- Background PID: {bg_pid or ''} ({bg_state})")
    print(f"- Review log: {LOG_PATH}")
    if remaining:
        print("- Next cases:")
        for item in remaining[:12]:
            print(f"  {item.priority} {item.index}: {item.title}")


def install_signal_handlers() -> None:
    def handle(signum, _frame):
        write_log("signal", signal=signum)
        release_pid()
        raise SystemExit(128 + signum)

    signal.signal(signal.SIGTERM, handle)
    signal.signal(signal.SIGINT, handle)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status", action="store_true", help="Print reviewed-note progress and exit.")
    parser.add_argument("--background", action="store_true", help="Detach this invocation and run it in the background.")
    parser.add_argument("--background-log", default=str(RUNNER_OUT), help="Output file used by --background.")
    parser.add_argument("--run-codex", action="store_true", help="Invoke Codex to create reviewed notes.")
    parser.add_argument("--prepare-only", action="store_true", help="Only write prompt files for selected cases.")
    parser.add_argument("--indices", help="Comma/space separated case indices to process.")
    parser.add_argument("--start-index", type=int)
    parser.add_argument("--end-index", type=int)
    parser.add_argument("--priority", help="Restrict to priorities, for example P0 or P0,P1.")
    parser.add_argument("--limit", type=int, help="Maximum cases to prepare or run in this invocation.")
    parser.add_argument("--include-reviewed", action="store_true", help="Rebuild prompts/run even if reviewed file exists.")
    parser.add_argument("--continue-on-error", action="store_true", help="Continue after a Codex or validation failure.")
    parser.add_argument("--force-pid", action="store_true", help="Ignore stale/running PID lock.")
    parser.add_argument("--timeout-seconds", type=int, default=1800)
    parser.add_argument("--codex-bin")
    parser.add_argument("--codex-model")
    args = parser.parse_args()

    if args.background:
        launch_background(sys.argv[1:], args)
        return

    if args.status:
        print_status()
        return

    if not args.run_codex and not args.prepare_only:
        args.prepare_only = True

    items = select_items(args)
    if not items:
        rebuild_backlog()
        print("No reviewable cases selected.")
        return

    if args.run_codex:
        install_signal_handlers()
        acquire_pid(force=args.force_pid)
        write_log("run_start", pid=os.getpid(), selected=len(items))

    try:
        for item in items:
            REVIEWED_DIR.mkdir(parents=True, exist_ok=True)
            prompt = prompt_for_case(item)
            prompt_path = write_prompt(item, prompt)
            print(f"prepared {item.index}: {prompt_path}")
            write_log("prompt_prepared", index=item.index, bvid=item.bvid, prompt=str(prompt_path))

            if not args.run_codex:
                continue

            code = run_codex(item, prompt, args)
            errors = validate_reviewed(item.reviewed)
            if code != 0 or errors:
                write_log("review_failed", index=item.index, bvid=item.bvid, returncode=code, errors=errors)
                print(f"failed {item.index}: returncode={code} errors={errors}")
                if not args.continue_on_error:
                    raise SystemExit(1)
            else:
                write_log("review_validated", index=item.index, bvid=item.bvid, reviewed=str(item.reviewed))
                print(f"reviewed {item.index}: {item.reviewed}")
                rebuild_backlog()
    finally:
        if args.run_codex:
            write_log("run_end", pid=os.getpid())
            release_pid()

    rebuild_backlog()
    print_status()


if __name__ == "__main__":
    main()
