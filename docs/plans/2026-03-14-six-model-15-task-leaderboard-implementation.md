# Six-Model 15-Task Leaderboard Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Evaluate six requested models on the current 15-task preview benchmark and regenerate the leaderboard as a real multi-model comparison.

**Architecture:** Use the existing real single-task runner to produce per-task run results for each requested model, then aggregate each completed model into its own model-results JSON. Regenerate the leaderboard only from complete 15-task model aggregates so all rows are directly comparable.

**Tech Stack:** Python runner utilities, WSL2 + Docker OpenClaw runtime, OpenAI-compatible HTTP endpoints, JSON artifacts, pytest

---

### Task 1: Add explicit local model-to-endpoint mapping for the six-model run wave

**Files:**
- Create: `D:/openclaw-agent-security/docs/notes/2026-03-14-six-model-run-config.md`
- Reference: `D:/openclaw-agent-security/.env.openclaw.local`

**Step 1: Write the run-config note**

Record which models map to which endpoint:

- `kimi-k2.5`
- `kimi-k2-0905-preview`
- `kimi-k2-0711-preview`
- `gpt-5.1-codex`
- `gpt-5.2`
- `gpt-5.4`

**Step 2: Verify the endpoints expose the intended model ids**

Use `/models` calls or equivalent checks and capture the result in the note.

**Step 3: Keep the note local-only if it references secrets**

Do not write raw API keys into the note.

**Step 4: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 5: Commit**

```bash
git add docs/notes/2026-03-14-six-model-run-config.md
git commit -m "docs: record six-model run configuration"
```

### Task 2: Produce 15-task run-result sets for the three Kimi models

**Files:**
- Output: `D:/openclaw-agent-security/benchmark/live-output/preview-v1/`
- Output: `D:/openclaw-agent-security/benchmark/traces/preview-v1/`
- Output: `D:/openclaw-agent-security/evaluator/results/run-results/preview-v1/`

**Step 1: Run `kimi-k2.5` across 15 tasks**

Generate or refresh one run-result per current task.

**Step 2: Run `kimi-k2-0905-preview` across 15 tasks**

Generate one run-result per current task.

**Step 3: Run `kimi-k2-0711-preview` across 15 tasks**

Generate one run-result per current task.

**Step 4: Verify coverage**

For each of the three models, confirm 15 `real-smoke-1.json` run-result files exist.

**Step 5: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 6: Commit**

```bash
git add benchmark/live-output benchmark/traces evaluator/results/run-results
git commit -m "data: add kimi leaderboard run results"
```

### Task 3: Produce 15-task run-result sets for the three GPT models

**Files:**
- Output: `D:/openclaw-agent-security/benchmark/live-output/preview-v1/`
- Output: `D:/openclaw-agent-security/benchmark/traces/preview-v1/`
- Output: `D:/openclaw-agent-security/evaluator/results/run-results/preview-v1/`

**Step 1: Run `gpt-5.1-codex` across 15 tasks**

Generate one run-result per current task.

**Step 2: Run `gpt-5.2` across 15 tasks**

Generate one run-result per current task.

**Step 3: Run `gpt-5.4` across 15 tasks**

Generate one run-result per current task.

**Step 4: Verify coverage**

For each of the three models, confirm 15 `real-smoke-1.json` run-result files exist.

**Step 5: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 6: Commit**

```bash
git add benchmark/live-output benchmark/traces evaluator/results/run-results
git commit -m "data: add gpt leaderboard run results"
```

### Task 4: Aggregate the six model result sets

**Files:**
- Modify: `D:/openclaw-agent-security/evaluator/results/model-results/preview-v1/`

**Step 1: Aggregate each completed model**

Write one model-results JSON per requested model.

**Step 2: Verify coverage per model**

Check each aggregate reports:

- `tasks_evaluated = 15`
- `runs_evaluated = 15`

**Step 3: Keep benchmark version consistent**

Use the same `preview-v1-current-real` benchmark version and `openclaw-preview-v1` profile.

**Step 4: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 5: Commit**

```bash
git add evaluator/results/model-results/preview-v1
git commit -m "data: aggregate six model benchmark results"
```

### Task 5: Regenerate the multi-model leaderboard

**Files:**
- Modify: `D:/openclaw-agent-security/leaderboard/output/preview-leaderboard.md`
- Modify: `D:/openclaw-agent-security/leaderboard/output/preview-leaderboard.json`

**Step 1: Generate the leaderboard from the six aggregate files**

Use `expected_runs=15`.

**Step 2: Verify output shape**

Check that the markdown and JSON contain six ranked rows.

**Step 3: Verify ordering and metadata**

Confirm:

- rows are sorted by the current leaderboard rules
- benchmark version is correct
- profile id is correct

**Step 4: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 5: Commit**

```bash
git add leaderboard/output/preview-leaderboard.md leaderboard/output/preview-leaderboard.json
git commit -m "data: publish first multi-model leaderboard"
```
