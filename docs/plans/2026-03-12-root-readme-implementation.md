# Root README Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a root `README.md` that introduces the repository, shows the current benchmark snapshot, and gives new contributors a short path to understanding and running the project.

**Architecture:** The README will be a concise top-level markdown document that synthesizes existing project context from `context.md` and links to deeper documents already present in the repository. It should avoid duplicating subsystem READMEs while making the main repository understandable as a whole.

**Tech Stack:** Markdown, existing repository docs, pytest command references

---

### Task 1: Draft the root README content

**Files:**
- Create: `README.md`
- Reference: `context.md`
- Reference: `leaderboard/README.md`
- Reference: `evaluator/README.md`

**Step 1: Write the README structure**

Include these sections:

```md
# OpenClaw Security Benchmark

## What this repository is
## Why it exists
## Current snapshot
## Repository map
## Quick start
## Key artifacts
## Roadmap
```

**Step 2: Fill in the current snapshot**

Use the current repository facts:

```text
- 11 real tasks today
- 36-task long-term v1 target
- single-model baseline on moonshot/kimi-k2.5
- security_score 90.91
- boundary_failure_rate 0.1818
- approval_preserved_rate 1.0
- persistence_violation_rate 0.0
- task_completion_rate 1.0
- current failures: AS-001, CC-001
```

**Step 3: Add a short repository map**

Describe these directories briefly:

```text
benchmark/
evaluator/
leaderboard/
docs/
```

### Task 2: Add lightweight usage instructions

**Files:**
- Modify: `README.md`

**Step 1: Add verification and usage commands**

Include short commands such as:

```bash
pytest
python leaderboard/generate_leaderboard.py
```

**Step 2: Add links to key artifacts**

Link to:

```text
docs/plans/2026-03-10-openclaw-security-benchmark-v1-36-design.md
docs/plans/2026-03-10-openclaw-security-benchmark-v1-36-implementation.md
docs/notes/2026-03-11-single-model-current-run.md
leaderboard/output/preview-leaderboard.md
```

### Task 3: Verify and prepare follow-up

**Files:**
- Verify: `README.md`

**Step 1: Read the README for clarity**

Check that the first screen explains the project to a new visitor without requiring other docs.

**Step 2: Run tests to confirm no accidental breakage**

Run: `pytest`

Expected: all tests pass

**Step 3: Prepare commit if requested**

```bash
git add README.md docs/plans/2026-03-12-root-readme-design.md docs/plans/2026-03-12-root-readme-implementation.md
git commit -m "docs: add root repository README"
```
