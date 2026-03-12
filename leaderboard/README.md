# Leaderboard Output Generator

This directory generates preview leaderboard artifacts from aggregated model result files.

## Inputs

- one JSON file per model aggregate
- fixed `benchmark_version`
- fixed `profile_id`

## Outputs

- markdown leaderboard for human reading
- json leaderboard for downstream use

## Ordering

Rows are ranked by:

1. higher `security_score`
2. lower `boundary_failure_rate`
3. higher `approval_preserved_rate`
4. lower `persistence_violation_rate`
5. higher `task_completion_rate`
6. `model_id` ascending
