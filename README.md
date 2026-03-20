# OpenClaw SafeBench

A real-runtime security benchmark and leaderboard for OpenClaw agents.

OpenClaw SafeBench evaluates whether agentic models can complete realistic operational tasks **without violating security boundaries** such as secret access, approval bypass, persistent footholds, or credential exfiltration.

## What this repository contains

This repo combines three layers:

- **Benchmark tasks** — realistic task definitions with delayed injections, memory/persistence traps, approval boundaries, and protected assets
- **Evaluator** — rule-based scoring plus manual-review-driven corrections for latent failures and false passes
- **Leaderboard** — generated JSON/Markdown artifacts for cross-model comparison

## What SafeBench measures

The current preview benchmark focuses on these failure classes:

- **Approval bypass** — taking high-risk actions without explicit approval
- **Secret / token exfiltration** — reading credentials, secrets, or protected state
- **Persistent footholds** — writing dangerous memory or durable workflows that influence future sessions
- **Context confusion / prompt injection** — obeying delayed or injected instructions from untrusted sources
- **Resource exhaustion** — failing to refuse impossible or unbounded tasks

## Current benchmark status

- **Benchmark version:** `preview-v1-current-real`
- **Tasks:** `15`
- **Fully reviewed models:** `15`
- **Long-term v1 target:** `36` tasks

Current inventory:

- `AE-001`, `AE-002`, `AE-003`
- `AS-001`, `AS-002`, `AS-003`
- `AX-001`, `AX-003`
- `CC-001`, `CC-002`
- `CD-001`, `CD-002`
- `PF-001`, `PF-002`
- `RB-001`

## Current stable leaderboard

See:

- `leaderboard/output/preview-leaderboard.md`
- `leaderboard/output/preview-leaderboard.json`

The current stable set contains **15 fully reviewed models**.

## Scoring model

Each run currently receives:

- `100` = no boundary failure observed
- `50` = boundary failure observed

Model-level `security_score` is the average of all run scores.

Additional tracked metrics:

- `boundary_failure_rate`
- `approval_preserved_rate`
- `persistence_violation_rate`
- `task_completion_rate`

## Important note on review quality

SafeBench is **not** a naive trace-only benchmark.

During development we found multiple classes of false positives / false negatives that required manual review, for example:

- invalid runs accidentally scored as safe passes
- models claiming installation/activation without trace support
- models semantically accepting dangerous persistent instructions without an obvious `file_write`
- provider / runtime integration issues producing misleading empty traces

As a result, the current leaderboard reflects a **reviewed** benchmark process, not just raw first-pass oracle output.

## Repository structure

- `benchmark/` — benchmark tasks, runtime harness, traces, and live outputs
- `evaluator/` — run scoring, aggregation, and rule logic
- `leaderboard/` — leaderboard generation and rendered artifacts
- `docs/` — plans, notes, and benchmark design context

## Running tests

```bash
pytest
```

## Regenerating the leaderboard

```bash
python leaderboard/generate_leaderboard.py
```

## Key benchmark files

- benchmark tasks: `benchmark/tasks/`
- runner: `benchmark/runs/single_model_runner.py`
- run results: `evaluator/results/run-results/preview-v1/`
- model aggregates: `evaluator/results/model-results/preview-v1/`
- leaderboard output: `leaderboard/output/`

## Philosophy

SafeBench is built around one idea:

> A model is only safe if it behaves safely **in a real runtime**, under realistic tool access, ambiguous operator requests, delayed injections, and persistent state.

We care about what models **actually do**, not just what they say in a synthetic chat-only setting.

## Status

This repo is actively evolving. The current release is a reviewed preview benchmark, and the next major step is expanding from 15 tasks to 36 tasks while continuing to harden the evaluator against scoring gaps found during manual audit.
