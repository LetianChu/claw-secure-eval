# OpenClaw Security Benchmark

This repository builds a real, versioned OpenClaw security benchmark and leaderboard for evaluating agent behavior under realistic runtime constraints.

## Why this repository exists

OpenClaw agents operate in a real runtime, not a toy sandbox. This project tracks whether models can complete tasks while preserving security boundaries such as approval requirements, protected resources, and persistence restrictions.

The current repository combines three pieces:

- a benchmark task library with real task definitions and run outputs
- a rule-based evaluator that scores normalized traces and run results
- a leaderboard generator that turns model aggregates into comparable benchmark artifacts

## Current snapshot

The current benchmark state is a real preview baseline rather than a synthetic demo, and the latest completed aggregate now covers the full current task inventory.

- benchmark version: `preview-v1-current-real`
- current preview benchmark inventory: `15` tasks
- latest completed real aggregate: `15` tasks evaluated
- long-term v1 target: `36` tasks
- current model baseline: `moonshot/kimi-k2.5`
- tasks evaluated: `15`
- runs evaluated: `15`
- `security_score = 86.67`
- `boundary_failure_rate = 0.2667`
- `approval_preserved_rate = 1.0`
- `persistence_violation_rate = 0.0`
- `task_completion_rate = 0.9333`
- current real failures: `AS-001`, `CC-001`

Current inventory tasks:

- `AE-001`, `AE-002`, `AE-003`
- `AS-001`, `AS-002`, `AS-003`
- `AX-001`, `AX-003`
- `CC-001`, `CC-002`
- `CD-001`, `CD-002`
- `PF-001`, `PF-002`
- `RB-001`

Important context:

- the current leaderboard snapshot is a single-model real baseline from the full current 15-task run
- `RB-001` adds low-cost resource-exhaustion coverage
- the `AX` abuse-and-exfiltration family now has an initial pair in inventory and both tasks are reflected in the completed aggregate metrics

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

- expand from the current 15-task inventory toward the 36-task v1 benchmark and rerun real aggregates as coverage grows
- add more models so the leaderboard becomes a real comparison rather than a single-model snapshot
- grow the `AX` abuse-and-exfiltration task family
- keep the benchmark grounded in real runtime behavior on OpenClaw + WSL2 + Docker
