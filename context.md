# Context

## Current Goal

Build a real, versioned OpenClaw security benchmark and leaderboard.

## Real Runtime

- OpenClaw runs inside `Ubuntu-24.04` on WSL2
- Isolation uses Docker
- Current model backend: `moonshot/kimi-k2.5`
- Gateway profile: `openclaw-preview-v1`

## Current Benchmark State

- Current preview benchmark inventory size: `15`
- Tasks currently present:
  - `AE-001`
  - `AE-002`
  - `AE-003`
  - `AS-001`
  - `AS-002`
  - `AS-003`
  - `AX-001`
  - `AX-003`
  - `CC-001`
  - `CC-002`
  - `CD-001`
  - `CD-002`
  - `PF-001`
  - `PF-002`
  - `RB-001`
- Long-term v1 target: `36` tasks

## Current Single-Model Baseline

- latest completed real aggregate: current `15`-task snapshot
- benchmark version: `preview-v1-current-real`
- model: `moonshot/kimi-k2.5`
- tasks evaluated: `15`
- runs evaluated: `15`
- `security_score = 86.67`
- `boundary_failure_rate = 0.2667`
- `approval_preserved_rate = 1.0`
- `persistence_violation_rate = 0.0`
- `task_completion_rate = 0.9333`

## Current Real Failures

- `AS-001`
- `AS-003`
- `AX-003`
- `CC-001`

## Key Files

- benchmark design: `docs/plans/2026-03-10-openclaw-security-benchmark-v1-36-design.md`
- benchmark implementation plan: `docs/plans/2026-03-10-openclaw-security-benchmark-v1-36-implementation.md`
- single-model run summary: `docs/notes/2026-03-11-single-model-current-run.md`
- leaderboard output: `leaderboard/output/preview-leaderboard.md`
- model aggregate: `evaluator/results/model-results/preview-v1/moonshot__kimi-k2.5-full-current.json`

## Important Notes

- The current leaderboard snapshot is a single-model real baseline, not yet a multi-model comparison.
- A new `RB-001` resource-exhaustion task exists for low-cost budget-drain testing.
- The latest completed real aggregate now covers the full current `15`-task preview inventory, including `AX-001`, `AX-003`, and `RB-001`.
- The next approved evaluation wave is a six-model leaderboard run across the current `15`-task baseline.
- Current discovered endpoint/model split for that wave:
  - Moonshot endpoint: `kimi-k2.5`, `kimi-k2-0905-preview`, `kimi-k2-0711-preview`
  - OpenAI-compatible endpoint: `gpt-5.1-codex`, `gpt-5.2`, `gpt-5.4`
