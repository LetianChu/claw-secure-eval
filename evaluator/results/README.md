# Evaluator Result Artifacts

This directory stores normalized outputs produced by evaluator v0.

## Artifact Types

- raw traces from OpenClaw runs
- normalized run results
- aggregated model results
- leaderboard export rows

Example export artifacts are stored in `evaluator/examples/`, including one safe trace and one unsafe trace.

## Required Trace Fields

- `timestamp`
- `event_type`
- `approved`
- `metadata`

Optional task-specific fields:

- `path`
- `command`

For approval-gated tasks, `approval_event.metadata.target` should name the approved command or protected path prefix.

## Preview Result Flow

1. collect a trace for one model-task run
2. evaluate it into one run result
3. aggregate all run results for one model
4. export model-level leaderboard rows
