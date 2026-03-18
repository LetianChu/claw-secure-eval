# Three-Claude Preview Wave Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add three Claude models to the current `15`-task preview benchmark and regenerate the leaderboard as a nine-model comparison.

**Architecture:** Reuse the existing real single-task runner and artifact layout without changing benchmark semantics. Treat the three Claude models as an incremental extension of the current six-model baseline: verify model availability, run full task coverage, aggregate each Claude model, then regenerate the leaderboard from the combined complete aggregate set.

**Tech Stack:** Python runner utilities, WSL2 + Docker OpenClaw runtime, OpenAI-compatible HTTP endpoint, JSON artifacts, pytest

---

### Task 1: Record the Claude run configuration

**Files:**
- Create: `D:/openclaw-agent-security/docs/notes/2026-03-16-three-claude-run-config.md`
- Reference: `D:/openclaw-agent-security/.env.openclaw.local`

**Step 1: Write the run-config note**

Record the selected Claude model ids and route them to `API_BASE_URL_2`.

**Step 2: Verify endpoint exposure**

Use a `/models` call with the local env-backed endpoint and capture confirmation that these ids are present:

- `claude-haiku-4-5-20251001`
- `claude-sonnet-4-6`
- `claude-opus-4-6`

**Step 3: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 4: Commit**

```bash
git add docs/notes/2026-03-16-three-claude-run-config.md
git commit -m "docs: record three-claude run configuration"
```

### Task 2: Produce a full 15-task run-result set for Claude Haiku

**Files:**
- Output: `D:/openclaw-agent-security/benchmark/live-output/preview-v1/`
- Output: `D:/openclaw-agent-security/benchmark/traces/preview-v1/`
- Output: `D:/openclaw-agent-security/evaluator/results/run-results/preview-v1/`

**Step 1: Run `claude-haiku-4-5-20251001` across 15 tasks**

Generate one `real-smoke-1` run-result per current task.

**Step 2: Verify coverage**

Confirm `15` run-result JSON files exist for `claude-haiku-4-5-20251001`.

**Step 3: Inspect obvious runtime failures**

Spot-check any missing, aborted, or malformed run artifacts before moving on.

**Step 4: Commit**

```bash
git add benchmark/live-output benchmark/traces evaluator/results/run-results
git commit -m "data: add claude haiku benchmark run results"
```

### Task 3: Produce a full 15-task run-result set for Claude Sonnet

**Files:**
- Output: `D:/openclaw-agent-security/benchmark/live-output/preview-v1/`
- Output: `D:/openclaw-agent-security/benchmark/traces/preview-v1/`
- Output: `D:/openclaw-agent-security/evaluator/results/run-results/preview-v1/`

**Step 1: Run `claude-sonnet-4-6` across 15 tasks**

Generate one `real-smoke-1` run-result per current task.

**Step 2: Verify coverage**

Confirm `15` run-result JSON files exist for `claude-sonnet-4-6`.

**Step 3: Inspect obvious runtime failures**

Spot-check any missing, aborted, or malformed run artifacts before moving on.

**Step 4: Commit**

```bash
git add benchmark/live-output benchmark/traces evaluator/results/run-results
git commit -m "data: add claude sonnet benchmark run results"
```

### Task 4: Produce a full 15-task run-result set for Claude Opus

**Files:**
- Output: `D:/openclaw-agent-security/benchmark/live-output/preview-v1/`
- Output: `D:/openclaw-agent-security/benchmark/traces/preview-v1/`
- Output: `D:/openclaw-agent-security/evaluator/results/run-results/preview-v1/`

**Step 1: Run `claude-opus-4-6` across 15 tasks**

Generate one `real-smoke-1` run-result per current task.

**Step 2: Verify coverage**

Confirm `15` run-result JSON files exist for `claude-opus-4-6`.

**Step 3: Inspect obvious runtime failures**

Spot-check any missing, aborted, or malformed run artifacts before moving on.

**Step 4: Commit**

```bash
git add benchmark/live-output benchmark/traces evaluator/results/run-results
git commit -m "data: add claude opus benchmark run results"
```

### Task 5: Aggregate the three Claude model result sets

**Files:**
- Modify: `D:/openclaw-agent-security/evaluator/results/model-results/preview-v1/`

**Step 1: Aggregate Claude Haiku**

Write `D:/openclaw-agent-security/evaluator/results/model-results/preview-v1/anthropic__claude-haiku-4-5-20251001.json`.

**Step 2: Aggregate Claude Sonnet**

Write `D:/openclaw-agent-security/evaluator/results/model-results/preview-v1/anthropic__claude-sonnet-4-6.json`.

**Step 3: Aggregate Claude Opus**

Write `D:/openclaw-agent-security/evaluator/results/model-results/preview-v1/anthropic__claude-opus-4-6.json`.

**Step 4: Verify aggregate coverage**

Check each aggregate reports `tasks_evaluated = 15` and `runs_evaluated = 15`.

**Step 5: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 6: Commit**

```bash
git add evaluator/results/model-results/preview-v1
git commit -m "data: aggregate three claude benchmark results"
```

### Task 6: Publish the nine-model leaderboard

**Files:**
- Modify: `D:/openclaw-agent-security/leaderboard/output/preview-leaderboard.md`
- Modify: `D:/openclaw-agent-security/leaderboard/output/preview-leaderboard.json`

**Step 1: Regenerate the leaderboard from the nine complete aggregate files**

Use the current benchmark version and `expected_runs=15`.

**Step 2: Verify output shape**

Check that the markdown and JSON both contain `9` ranked rows.

**Step 3: Verify metadata and ordering**

Confirm:

- benchmark version remains `preview-v1-current-real`
- profile id remains `openclaw-preview-v1`
- rows remain sorted by the current leaderboard rules

**Step 4: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 5: Commit**

```bash
git add leaderboard/output/preview-leaderboard.md leaderboard/output/preview-leaderboard.json
git commit -m "data: publish nine-model preview leaderboard"
```
