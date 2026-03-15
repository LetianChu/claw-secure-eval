# Preview 15-Task Aggregate Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Regenerate the official single-model preview baseline so it reflects the current 15-task run-result set instead of the older 11-task snapshot.

**Architecture:** Reuse the existing per-task run-result JSON files as the aggregation source, then regenerate the model aggregate and leaderboard outputs with the current utility scripts. After artifact regeneration, update summary docs so they reflect the new 15-task baseline consistently.

**Tech Stack:** Python aggregation utilities, existing JSON run results, Markdown docs, pytest

---

### Task 1: Rebuild the model aggregate from 15 run-result files

**Files:**
- Modify: `D:/openclaw-agent-security/evaluator/results/model-results/preview-v1/moonshot__kimi-k2.5-full-current.json`
- Reference: `D:/openclaw-agent-security/evaluator/results/run-results/preview-v1/moonshot__kimi-k2.5/`

**Step 1: Verify the source run-result set**

Confirm there are 15 per-task `real-smoke-1.json` files under the current preview run-results directory.

**Step 2: Run the aggregate command**

Use `aggregate_model_result_files()` to write the updated model aggregate.

**Step 3: Inspect the output**

Check that:

- `tasks_evaluated = 15`
- `runs_evaluated = 15`
- all 15 task ids are included

**Step 4: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 5: Commit**

```bash
git add evaluator/results/model-results/preview-v1/moonshot__kimi-k2.5-full-current.json
git commit -m "update: regenerate 15-task model aggregate"
```

### Task 2: Regenerate leaderboard outputs for the 15-task baseline

**Files:**
- Modify: `D:/openclaw-agent-security/leaderboard/output/preview-leaderboard.md`
- Modify: `D:/openclaw-agent-security/leaderboard/output/preview-leaderboard.json`

**Step 1: Run leaderboard generation**

Generate leaderboard outputs from the updated model aggregate with `expected_runs=15`.

**Step 2: Inspect the rendered leaderboard**

Confirm the leaderboard row now reports 15 runs.

**Step 3: Check consistency with aggregate metrics**

Make sure the markdown and JSON outputs match the regenerated model aggregate.

**Step 4: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 5: Commit**

```bash
git add leaderboard/output/preview-leaderboard.md leaderboard/output/preview-leaderboard.json
git commit -m "update: regenerate 15-task leaderboard"
```

### Task 3: Update baseline documentation to the new 15-task aggregate

**Files:**
- Modify: `D:/openclaw-agent-security/docs/notes/2026-03-11-single-model-current-run.md`
- Modify: `D:/openclaw-agent-security/context.md`
- Modify: `D:/openclaw-agent-security/README.md`

**Step 1: Update the run summary note**

Replace language that still says the latest completed aggregate is the older 11-task snapshot.

**Step 2: Update `context.md`**

Make the current single-model baseline section reflect the new 15-task aggregate metrics.

**Step 3: Update `README.md` current snapshot**

Align the top-level README snapshot with the new 15-task aggregate.

**Step 4: Verify consistency manually**

Check that all three docs agree on:

- task count
- runs evaluated
- security metrics
- failing tasks if they changed

**Step 5: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 6: Commit**

```bash
git add docs/notes/2026-03-11-single-model-current-run.md context.md README.md
git commit -m "docs: update 15-task preview baseline"
```
