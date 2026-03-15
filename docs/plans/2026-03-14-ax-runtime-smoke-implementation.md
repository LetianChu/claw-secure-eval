# AX Runtime Smoke Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make `AX-001` and `AX-003` runnable through the real single-task OpenClaw smoke path, with persisted response, transcript, trace, and evaluator outputs.

**Architecture:** Reuse the existing `run_single_task` flow and extend only the task-fixture and persistence paths needed for the new AX tasks. Keep runtime support minimal and deterministic, then verify by running one smoke execution per AX task and checking the generated artifacts.

**Tech Stack:** Python runner utilities, YAML task manifests, pytest, WSL2 + Docker OpenClaw runtime, persisted JSON/JSONL artifacts

---

### Task 1: Add runtime fixtures for `AX-001`

**Files:**
- Modify: `D:/openclaw-agent-security/benchmark/runs/single_model_runner.py`
- Test: `D:/openclaw-agent-security/benchmark/runs/tests/test_single_model_runner.py`

**Step 1: Write the failing test**

Add a test asserting `_task_fixtures()` seeds the note file referenced by `AX-001`.

Example:

```python
def test_task_fixtures_seed_ax001_note():
    fixtures = _task_fixtures()
    assert "/workspace/notes/community-thanks-draft.md" in fixtures["AX-001"]
```

**Step 2: Run test to verify it fails**

Run: `pytest benchmark/runs/tests/test_single_model_runner.py -k ax001 -v`

Expected: FAIL if `AX-001` runtime fixture is missing.

**Step 3: Implement minimal fixture support**

Seed only the note file needed for the task’s visible context.

**Step 4: Run test to verify it passes**

Run: `pytest benchmark/runs/tests/test_single_model_runner.py -k ax001 -v`

Expected: PASS.

**Step 5: Commit**

```bash
git add benchmark/runs/single_model_runner.py benchmark/runs/tests/test_single_model_runner.py
git commit -m "test: seed AX-001 runtime fixture"
```

### Task 2: Add runtime fixtures and persistence hygiene for `AX-003`

**Files:**
- Modify: `D:/openclaw-agent-security/benchmark/runs/single_model_runner.py`
- Test: `D:/openclaw-agent-security/benchmark/runs/tests/test_single_model_runner.py`

**Step 1: Write the failing tests**

Add tests asserting:

- `_task_fixtures()` seeds the triage note for `AX-003`
- `_task_fixtures()` seeds the protected API key file for `AX-003`
- persisted sanitization redacts the seeded API key value

**Step 2: Run tests to verify they fail**

Run: `pytest benchmark/runs/tests/test_single_model_runner.py -k ax003 -v`

Expected: FAIL while runtime support is incomplete.

**Step 3: Implement minimal support**

Seed the note and protected API key file, and extend persistence redaction only as needed to keep the saved artifacts clean.

**Step 4: Run tests to verify they pass**

Run: `pytest benchmark/runs/tests/test_single_model_runner.py -k ax003 -v`

Expected: PASS.

**Step 5: Commit**

```bash
git add benchmark/runs/single_model_runner.py benchmark/runs/tests/test_single_model_runner.py
git commit -m "test: seed AX-003 runtime fixture"
```

### Task 3: Run real smoke for `AX-001`

**Files:**
- Verify: `D:/openclaw-agent-security/benchmark/tasks/AX-001.yaml`
- Output: `D:/openclaw-agent-security/benchmark/live-output/preview-v1/moonshot__kimi-k2.5/AX-001/`
- Output: `D:/openclaw-agent-security/benchmark/traces/preview-v1/moonshot__kimi-k2.5/AX-001/`
- Output: `D:/openclaw-agent-security/evaluator/results/run-results/preview-v1/moonshot__kimi-k2.5/AX-001/`

**Step 1: Execute one real smoke run**

Run `run_single_task()` for `AX-001`.

**Step 2: Verify artifacts exist**

Check for:

- `real-smoke-1.response.json`
- `real-smoke-1.transcript.jsonl`
- `real-smoke-1.json` trace
- `real-smoke-1.json` run result

**Step 3: Inspect the run result**

Record whether the task completed and whether a boundary failure occurred.

**Step 4: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 5: Commit**

```bash
git add benchmark/live-output/preview-v1/moonshot__kimi-k2.5/AX-001 benchmark/traces/preview-v1/moonshot__kimi-k2.5/AX-001 evaluator/results/run-results/preview-v1/moonshot__kimi-k2.5/AX-001
git commit -m "data: add AX-001 real smoke artifacts"
```

### Task 4: Run real smoke for `AX-003`

**Files:**
- Verify: `D:/openclaw-agent-security/benchmark/tasks/AX-003.yaml`
- Output: `D:/openclaw-agent-security/benchmark/live-output/preview-v1/moonshot__kimi-k2.5/AX-003/`
- Output: `D:/openclaw-agent-security/benchmark/traces/preview-v1/moonshot__kimi-k2.5/AX-003/`
- Output: `D:/openclaw-agent-security/evaluator/results/run-results/preview-v1/moonshot__kimi-k2.5/AX-003/`

**Step 1: Execute one real smoke run**

Run `run_single_task()` for `AX-003`.

**Step 2: Verify artifacts exist**

Check for:

- `real-smoke-1.response.json`
- `real-smoke-1.transcript.jsonl`
- `real-smoke-1.json` trace
- `real-smoke-1.json` run result

**Step 3: Verify persisted secret hygiene**

Confirm the saved response/transcript do not expose raw API key material.

**Step 4: Run repository tests**

Run: `pytest -q`

Expected: PASS.

**Step 5: Commit**

```bash
git add benchmark/live-output/preview-v1/moonshot__kimi-k2.5/AX-003 benchmark/traces/preview-v1/moonshot__kimi-k2.5/AX-003 evaluator/results/run-results/preview-v1/moonshot__kimi-k2.5/AX-003
git commit -m "data: add AX-003 real smoke artifacts"
```
