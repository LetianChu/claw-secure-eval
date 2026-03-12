# OpenClaw Leaderboard Scope v1

## Objective

Publish a preview leaderboard that compares model security behavior inside a fixed OpenClaw environment.

The public question for `preview-v1` is simple: under the same OpenClaw setup and the same benchmark tasks, which models are less likely to violate core security boundaries?

## Fixed Comparison Unit

For `preview-v1`, the comparison unit is:

- one model
- one fixed OpenClaw configuration
- one fixed pilot benchmark
- one fixed scoring policy

Only the model changes.

## Pilot Benchmark

`preview-v1` uses these six pilot tasks:

- `AE-001`
- `AE-002`
- `AS-002`
- `CD-001`
- `PF-001`
- `CC-001`

These tasks were selected because each one focuses on a primary boundary failure and has a rule-based oracle over observable traces.

## Public Outputs

The preview leaderboard publishes:

- `Security Score`
- `Boundary Failure Rate`
- `Approval Preserved Rate`
- `Persistence Violation Rate`
- `Task Completion Rate`
- benchmark version
- OpenClaw profile version
- update timestamp

## Non-Goals

`preview-v1` does not claim:

- universal model safety rankings
- cross-platform safety comparisons
- production-grade completeness
- exhaustive OpenClaw coverage
- stable scores across future benchmark versions

## Preview Publish Criteria

Before release, the project must have:

- pilot benchmark frozen
- fixed OpenClaw profile frozen
- evaluator v0 for pilot tasks
- trace and result schemas documented
- launch model matrix defined
- leaderboard output generated
- methodology and limitation notes published

## Disclaimer Rules

All public leaderboard views must say:

- results are measured in OpenClaw only
- this is a preview release with a 6-task pilot benchmark
- scores may change as tasks, evaluator logic, and run counts evolve

## Expansion Path

Future versions can expand by:

- adding more models
- increasing repeated runs
- promoting the full benchmark beyond the pilot six
- versioning benchmark and scoring updates
- publishing archived snapshots for comparability
