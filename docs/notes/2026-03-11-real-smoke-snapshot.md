# Real Smoke Snapshot

## Scope

This snapshot is not the full preview leaderboard matrix. It is the first real-execution snapshot produced from actual OpenClaw runs in the WSL2 Docker environment.

## Model

- `moonshot/kimi-k2.5`

## Profile

- `openclaw-preview-v1`

## Benchmark Version

- `preview-v1-real-smoke`

## Included Real Tasks

- `AE-001`
- `AE-002`
- `AS-002`
- `RB-001`

## Aggregate Result

- `security_score = 100.0`
- `boundary_failure_rate = 0.0`
- `approval_preserved_rate = 1.0`
- `persistence_violation_rate = 0.0`
- `task_completion_rate = 1.0`
- `runs_evaluated = 4`

## Why This Snapshot Matters

This is the first leaderboard row derived from real OpenClaw executions rather than synthetic traces only. It proves that the current runtime, transcript extraction, evaluator, and leaderboard generator can be connected end to end.

## Limitation

This is a partial real snapshot, not a complete multi-model benchmark comparison.
