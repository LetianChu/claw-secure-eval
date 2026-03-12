# Methodology

## Scope

This leaderboard measures model security behavior in OpenClaw, not general model safety across all platforms.

## Benchmark

- benchmark version: `preview-v1`
- profile id: `openclaw-preview-v1`
- tasks: `AE-001`, `AE-002`, `AS-002`, `CD-001`, `PF-001`, `CC-001`
- runs per task: `3`
- task timeout: `180` seconds
- retry policy: `no_retry_in_preview`

## Current Real Snapshot

The current published real-execution snapshot is a single-model full pass over the current task library, not yet a multi-model matrix.

- snapshot benchmark version: `preview-v1-current-real`
- real tasks currently aggregated: `AE-001`, `AE-002`, `AS-001`, `AS-002`, `CC-001`, `CC-002`, `CD-001`, `CD-002`, `PF-001`, `PF-002`, `RB-001`
- model rows should be interpreted as single-model baseline coverage until the broader multi-model matrix is executed

## Incomplete Runs

- missing trace: mark run incomplete
- invalid trace: keep artifact, exclude from aggregate if no valid run result can be produced
- provider failure: record in run notes and rerun only in a later snapshot

## Metrics

- `Security Score`
- `Boundary Failure Rate`
- `Approval Preserved Rate`
- `Persistence Violation Rate`
- `Task Completion Rate`

## Limitation

This is a preview release and scores may change as tasks, evaluator logic, and run counts evolve.
