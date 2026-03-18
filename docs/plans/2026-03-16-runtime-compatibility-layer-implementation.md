# Runtime Compatibility Layer Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a real benchmark runtime compatibility layer so common agent tool names like `shell` and `update_plan` map to real executable implementations, then audit the runtime against the full benchmark task inventory.

**Architecture:** Extend the benchmark runtime with a small additive compatibility surface that preserves the existing real environment, then audit whether that environment actually covers the capabilities implied by the current benchmark tasks. Register real alias tools, normalize their arguments into the canonical runtime implementations, verify transcript visibility, produce a task-to-capability audit, then rerun affected benchmark models against the repaired runtime.

**Tech Stack:** Python benchmark runner, OpenClaw runtime configuration, WSL2 + Docker, pytest, JSON trace artifacts

---

### Task 1: Record the runtime mismatch evidence

**Files:**
- Create: `D:/openclaw-agent-security/docs/notes/2026-03-16-runtime-compatibility-evidence.md`
- Reference: `D:/openclaw-agent-security/benchmark/live-output/preview-v1/`

**Step 1: Write the evidence note**

Document the repeated benchmark-invalid failures caused by `Tool shell not found`, `Tool update_plan not found`, and the resulting `400 bad_response_status_code` patterns.

**Step 2: Include representative task examples**

Capture at least one concrete GPT run, one Kimi run, and one Claude run or compatibility repro proving the mismatch.

**Step 3: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 4: Commit**

```bash
git add docs/notes/2026-03-16-runtime-compatibility-evidence.md
git commit -m "docs: record runtime compatibility failures"
```

### Task 2: Add a failing test for `shell` compatibility routing

**Files:**
- Modify: `D:/openclaw-agent-security/benchmark/runs/tests/test_single_model_runner.py`
- Modify: `D:/openclaw-agent-security/benchmark/runs/single_model_runner.py`

**Step 1: Write a failing test**

Add a test proving Anthropic and GPT benchmark runtime config exposes a real `shell` compatibility tool in addition to canonical command execution.

**Step 2: Run the test to verify it fails**

Run: `pytest benchmark/runs/tests/test_single_model_runner.py -k shell -v`

Expected: FAIL because the compatibility tool is not yet configured.

**Step 3: Implement minimal runtime config support**

Add the minimum configuration changes needed so the benchmark runtime exposes the `shell` compatibility mapping to the real execution implementation.

**Step 4: Run the test to verify it passes**

Run: `pytest benchmark/runs/tests/test_single_model_runner.py -k shell -v`

Expected: PASS.

**Step 5: Commit**

```bash
git add benchmark/runs/tests/test_single_model_runner.py benchmark/runs/single_model_runner.py
git commit -m "feat: add shell runtime compatibility"
```

### Task 3: Add a failing test for `update_plan` compatibility routing

**Files:**
- Modify: `D:/openclaw-agent-security/benchmark/runs/tests/test_single_model_runner.py`
- Modify: `D:/openclaw-agent-security/benchmark/runs/single_model_runner.py`

**Step 1: Write a failing test**

Add a test proving the benchmark runtime exposes a real `update_plan` compatibility tool and routes it to real session-scoped plan persistence.

**Step 2: Run the test to verify it fails**

Run: `pytest benchmark/runs/tests/test_single_model_runner.py -k update_plan -v`

Expected: FAIL because the compatibility tool is not yet configured.

**Step 3: Implement minimal runtime config support**

Add the minimum configuration changes needed so `update_plan` is a real callable runtime tool.

**Step 4: Run the test to verify it passes**

Run: `pytest benchmark/runs/tests/test_single_model_runner.py -k update_plan -v`

Expected: PASS.

**Step 5: Commit**

```bash
git add benchmark/runs/tests/test_single_model_runner.py benchmark/runs/single_model_runner.py
git commit -m "feat: add update plan runtime compatibility"
```

### Task 4: Verify runtime compatibility with minimal live repros

**Files:**
- Modify: `D:/openclaw-agent-security/benchmark/runs/single_model_runner.py`

**Step 1: Run a minimal `shell` repro**

Use OpenClaw CLI with a simple prompt that triggers command execution.

**Step 2: Run a minimal `update_plan` repro**

Use OpenClaw CLI with a simple prompt that triggers plan updates.

**Step 3: Verify both complete without `tool not found`**

Inspect transcript output and confirm the runtime no longer emits `Tool shell not found` or `Tool update_plan not found` for these repros.

**Step 4: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 5: Commit**

```bash
git add benchmark/runs/single_model_runner.py benchmark/runs/tests/test_single_model_runner.py
git commit -m "test: verify runtime compatibility repros"
```

### Task 5: Audit the runtime against the benchmark task inventory

**Files:**
- Create: `D:/openclaw-agent-security/docs/notes/2026-03-16-runtime-capability-audit.md`
- Reference: `D:/openclaw-agent-security/benchmark/tasks/*.yaml`

**Step 1: Map each task or task family to required runtime abilities**

Write down which capability classes each current task relies on, including command execution, file access, plan updates, memory, workflows, browser/attachments, and session/subagent surfaces.

**Step 2: Map each required ability to a real runtime surface**

For each required capability, record whether it is:

- already present as a real tool
- newly covered by the compatibility layer
- still missing and therefore a blocker

**Step 3: Verify no hidden blockers remain**

Confirm the audit does not reveal benchmark-required capability gaps beyond the currently planned compatibility tools.

**Step 4: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 5: Commit**

```bash
git add docs/notes/2026-03-16-runtime-capability-audit.md
git commit -m "docs: audit benchmark runtime capability coverage"
```

### Task 6: Rerun the affected benchmark models

**Files:**
- Output: `D:/openclaw-agent-security/benchmark/live-output/preview-v1/`
- Output: `D:/openclaw-agent-security/benchmark/traces/preview-v1/`
- Output: `D:/openclaw-agent-security/evaluator/results/run-results/preview-v1/`

**Step 1: Rerun the GPT models**

Regenerate the `15`-task run-result sets for:

- `openai/gpt-5.1-codex`
- `openai/gpt-5.2`
- `openai/gpt-5.4`

**Step 2: Rerun Kimi as a spot-check model**

Regenerate the `15`-task run-result set for `moonshot/kimi-k2.5`.

**Step 3: Verify runtime error elimination**

Confirm representative reruns no longer collapse into `Tool shell not found`, `Tool update_plan not found`, or immediate `400 bad_response_status_code` for the previously affected tasks.

**Step 4: Commit**

```bash
git add benchmark/live-output benchmark/traces evaluator/results/run-results
git commit -m "data: rerun benchmark models with compatibility layer"
```

### Task 7: Re-aggregate results and republish the leaderboard

**Files:**
- Modify: `D:/openclaw-agent-security/evaluator/results/model-results/preview-v1/`
- Modify: `D:/openclaw-agent-security/leaderboard/output/preview-leaderboard.md`
- Modify: `D:/openclaw-agent-security/leaderboard/output/preview-leaderboard.json`

**Step 1: Re-aggregate the rerun models**

Refresh model aggregates for all rerun models.

**Step 2: Regenerate the leaderboard**

Publish a new leaderboard using the repaired runtime results.

**Step 3: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 4: Spot-check ranking integrity**

Verify that row counts, task coverage, and benchmark version metadata are still correct.

**Step 5: Commit**

```bash
git add evaluator/results/model-results/preview-v1 leaderboard/output/preview-leaderboard.md leaderboard/output/preview-leaderboard.json
git commit -m "data: publish compatibility-layer leaderboard reruns"
```
