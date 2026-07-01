# Source Map

Use this file to understand what the skill was distilled from and how to update it.

## Collected Sources

- Bilibili video page `BV1eBR1BxEm7`: title page for "1百多万在加拿大开素食餐厅，日赚17加币，开业5年都没有回本。@勇哥餐饮原创". The page exposes a public UGC season named "勇哥餐饮创业踩坑案例" with 504 episodes when fetched on 2026-06-28. The video owner in the fetched metadata is `勇哥餐饮避坑指南`, mid `37938807`, with the profile sign saying the account is authorized and users should search `@勇哥餐饮原创` for live connection.
- User-specified Bilibili homepage: `https://space.bilibili.com/3546801669933097`. Treat this as the primary official account the user cares about, but verify live account details at use time because Bilibili profile pages can be blocked by captcha.
- Extracted case-title map: `references/bilibili-season-cases.tsv`, 504 rows from the public Bilibili season metadata. Use it for pattern search, not as full transcripts.
- Media writeups used for method clues:
  - 创业邦 article on 勇哥 as a "创业真人秀" and recurring franchise/selection questions.
  - 澎湃新闻 article describing the live-call consultation flow and examples such as asking what problem, business district, total spend, headquarters, and direct stores.
  - 人人都是产品经理 article describing the public-facing table `这家餐饮店能救吗`, with fields such as revenue, rent/utilities, labor cost, gross margin, and break-even line.

## What Is Directly Observed

- The public Bilibili season metadata gives strong evidence for recurring case types: losing stores, franchise stores, debt-funded openings, site-selection mistakes, low gross margin, high rent, family/partner conflict, takeover mistakes, and "can this store be saved" consultations.
- Media writeups provide direct descriptions of the consultation mechanics: ask the caller's problem, ask business district and cost structure, ask headquarters/franchise facts, calculate whether the shop can survive, and often advise stopping loss.

## What Is Inferred

- The detailed diagnostic protocol is inferred by combining case-title patterns, media descriptions, and standard restaurant finance logic.
- The break-even script operationalizes the repeated "算账" behavior. It is not a claim that 勇哥 uses this exact formula or script.
- Thresholds in `decision-models.md` are practical triage heuristics. Treat them as conservative operating rules, not universal laws.

## Dialogue Corpus Status

The skill must treat dialogue-derived notes as the authoritative knowledge layer. The title map is only a discovery index.

## Published Skill Package

For a lightweight GitHub skill package, include the runtime and reviewable knowledge artifacts only:

- `SKILL.md`, `agents/`, `references/`, and `scripts/`.
- `corpus/reviewed-case-notes/` with the 504 reviewed, dialogue-derived case notes.

Do not publish raw audio, raw ASR transcript JSON, machine-draft notes, review prompts, PID files, or runner logs. They are rebuild/audit artifacts, not required for normal skill use. If deeper audit or corpus refresh is needed, regenerate those local artifacts with the pipeline scripts and the public Bilibili sources.

Current corpus state:

- 504/504 videos have local audio, ASR transcripts, machine-draft case notes, and reviewed case notes.
- As of 2026-07-01, reviewed-note coverage is 504/504 under `corpus/reviewed-case-notes/`.
- Use `python yongge-catering-skill/scripts/run_review_corpus.py --status` to re-check coverage before making maintenance claims.
- Raw audio is kept as local cache under `corpus/audio/` and should not be committed; transcripts and case notes are the knowledge-base artifacts.

Scale estimate from the 504 public Bilibili season entries:

- Total video duration: about 166.9 hours.
- Average duration: about 19.9 minutes.
- Median duration: about 19.1 minutes.
- Longest video: about 55.0 minutes.
- Estimated audio storage from the first two downloaded samples: about 12.5GB for all 504 audio streams, plus transcripts and notes.

Full corpus plan:

1. Run `scripts/bilibili_corpus_pipeline.py --download --transcribe --model-size small` in index batches.
2. Review each `corpus/transcripts/*.json`.
3. Extract a compact case note into `corpus/case-notes/*.md`.
4. Promote stable, high-value patterns into `references/dialogue-derived-cases.md`, `diagnostic-protocol.md`, and `decision-models.md`.
5. Keep exact raw transcripts out of `SKILL.md`; use them as auditable sources for distilled notes.

Full reviewed-note plan:

1. Check review progress with `python yongge-catering-skill/scripts/run_review_corpus.py --status`.
2. Prepare review prompts without running Codex with `python yongge-catering-skill/scripts/run_review_corpus.py --prepare-only --limit 10`.
3. Run a controlled Codex-assisted review batch with `python yongge-catering-skill/scripts/run_review_corpus.py --run-codex --limit 5`.
4. For all remaining cases, run `python yongge-catering-skill/scripts/run_review_corpus.py --background --run-codex --continue-on-error --timeout-seconds 2400` and monitor `corpus/review_run.jsonl` plus `corpus/review_runner.out`.
5. The script writes reviewed notes only to `corpus/reviewed-case-notes/`, validates required sections, and rebuilds `references/corpus-review-backlog.md`.

For real consultation use, search reviewed notes with:

```bash
python yongge-catering-skill/scripts/search_reviewed_cases.py "汉堡 加盟 月亏1万 房租高"
```

Open the top matching reviewed notes before using a case as precedent.

Recommended batch commands:

```bash
source .venv/bin/activate
python yongge-catering-skill/scripts/bilibili_corpus_pipeline.py --start-index 1 --end-index 50 --download --transcribe --model-size small
python yongge-catering-skill/scripts/bilibili_corpus_pipeline.py --start-index 51 --end-index 100 --download --transcribe --model-size small
```

Use smaller batches because Bilibili URLs expire and ASR is compute-heavy. The script appends status to `corpus/status.jsonl` and skips existing transcripts unless `--overwrite` is set.

Add `--draft-note` to generate machine-draft case notes automatically:

```bash
python yongge-catering-skill/scripts/bilibili_corpus_pipeline.py --start-index 1 --end-index 50 --download --transcribe --draft-note --model-size small
```

Treat `corpus/case-notes/*.md` as draft notes unless manually reviewed. Promote only reviewed patterns to `references/dialogue-derived-cases.md`.

Check corpus progress with:

```bash
python yongge-catering-skill/scripts/corpus_status.py
```

Check reviewed-note progress with:

```bash
python yongge-catering-skill/scripts/run_review_corpus.py --status
```

Start or resume the all-video background run with:

```bash
python yongge-catering-skill/scripts/run_full_corpus.py
```

If a full-run process is already alive, the script reports the PID and does not launch a duplicate.

## Title Index Summary

From the 504 extracted episode titles:

- 236 mention loss or losing money patterns.
- 114 mention franchise/brand/headquarters/fast-recruit risk patterns.
- 72 mention debt or loan pressure.
- 84 mention site, rent, transfer, school, mall, street, or other location signals.
- 245 mention specific categories such as milk tea, coffee, burger, hot pot, barbecue, fried chicken, rice bowl, buffet, yogurt, skewers, malatang, pizza, chicken cutlet, bakery, or noodle shop.
- 48 explicitly mention financial metrics such as gross margin, daily profit, revenue, rent, cost, labor, or monthly profit.
- High-frequency title tokens include `月亏`, `加盟`, `奶茶`, `负债`, `火锅`, `开业`, `咖啡`, `宝妈`, `杂牌`, and `接盘`.

## Updating The Knowledge Base

To refresh the Bilibili case map:

1. Fetch a public video page from the same UGC season with a normal browser user agent.
2. Parse `window.__INITIAL_STATE__`.
3. Read `videoData.ugc_season.sections[].episodes[]`.
4. Export `index`, `section`, `title`, `bvid`, `aid`, `cid`, and `url` to `references/bilibili-season-cases.tsv`.
5. Recompute category counts and update `case-patterns.md`.

For transcript-level updates, run `scripts/bilibili_corpus_pipeline.py`. Store raw machine transcripts under `corpus/transcripts/` and store concise extracted decision moments under `corpus/case-notes/`; do not paste full transcript dumps into SKILL.md. Keep each case note as:

```text
source video:
user facts:
questions asked:
calculation:
diagnosis:
recommendation:
memorable expression:
```

## Source Limitations

Bilibili APIs and profile pages may trigger captcha or require login. A failed profile lookup does not mean the account does not exist. When the user asks about current account details, retry with browser access or cite the limitation.
