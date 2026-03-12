# OpenClaw Security Benchmark

This repository builds a real, versioned OpenClaw security benchmark and leaderboard for evaluating agent behavior under realistic runtime constraints.

## Why this repository exists

OpenClaw agents operate in a real runtime, not a toy sandbox. This project tracks whether models can complete tasks while preserving security boundaries such as approval requirements, protected resources, and persistence restrictions.

The current repository combines three pieces:

- a benchmark task library with real task definitions and run outputs
- a rule-based evaluator that scores normalized traces and run results
- a leaderboard generator that turns model aggregates into comparable benchmark artifacts

## Current snapshot

The current benchmark state is a real preview baseline rather than a synthetic demo.

- benchmark version: `preview-v1-current-real`
- current real task library: `11` tasks
- long-term v1 target: `36` tasks
- current model baseline: `moonshot/kimi-k2.5`
- tasks evaluated: `11`
- runs evaluated: `11`
- `security_score = 90.91`
- `boundary_failure_rate = 0.1818`
- `approval_preserved_rate = 1.0`
- `persistence_violation_rate = 0.0`
- `task_completion_rate = 1.0`
- current real failures: `AS-001`, `CC-001`

Important context:

- the current leaderboard snapshot is still a single-model real baseline
- `RB-001` adds low-cost resource-exhaustion coverage
- the next major expansion area is the `AX` abuse-and-exfiltration family

## Repository map

- `benchmark/` - task definitions, benchmark profiles, real run harnesses, traces, and live outputs
- `evaluator/` - rule-based scoring logic, schemas, examples, and aggregated result generation
- `leaderboard/` - leaderboard generation code plus rendered markdown and JSON outputs
- `docs/` - design notes, implementation plans, and run summaries

## Quick start

Run the test suite:

```bash
pytest
```

Regenerate the leaderboard artifact:

```bash
python leaderboard/generate_leaderboard.py
```

Useful places to inspect first:

- current leaderboard: `leaderboard/output/preview-leaderboard.md`
- current model aggregate: `evaluator/results/model-results/preview-v1/moonshot__kimi-k2.5-full-current.json`
- current run summary: `docs/notes/2026-03-11-single-model-current-run.md`

## Key artifacts

- benchmark design: `docs/plans/2026-03-10-openclaw-security-benchmark-v1-36-design.md`
- benchmark implementation plan: `docs/plans/2026-03-10-openclaw-security-benchmark-v1-36-implementation.md`
- single-model real run summary: `docs/notes/2026-03-11-single-model-current-run.md`
- leaderboard output: `leaderboard/output/preview-leaderboard.md`

## Roadmap

- expand from the current 11 real tasks toward the 36-task v1 benchmark
- add more models so the leaderboard becomes a real comparison rather than a single-model snapshot
- grow the `AX` abuse-and-exfiltration task family
- keep the benchmark grounded in real runtime behavior on OpenClaw + WSL2 + Docker
