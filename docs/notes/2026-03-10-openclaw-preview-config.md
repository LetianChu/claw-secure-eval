# OpenClaw Preview Config v1

## Goal

Freeze one OpenClaw evaluation profile for the preview leaderboard so models are compared under the same environment.

## Fixed Configuration

- profile id: `openclaw-preview-v1`
- host type: `local_vm`
- message channel: `synthetic_enterprise_im`
- tool profile: `full`
- sandbox level: `partial`
- approval policy: `ask_high_risk`

## State Assumptions

- memory resets per run
- workflow state resets per run
- session state resets per run
- workspace resets per run

These resets avoid hidden carry-over advantages between models or runs.

## Trace Contract

Each run trace should include ordered events with these fields:

- `timestamp`
- `event_type`
- `approved`
- `metadata`

For approval-gated actions, `approval_event` metadata should identify the authorized target, such as a protected command or protected path prefix.

And, when relevant:

- `path`
- `command`

## Runtime Rules

- one attempt per task in the preview release
- no automatic retries in preview mode
- fixed runtime budget per task

## Fairness Rules

All models must use:

- the same OpenClaw profile
- the same task set
- the same evaluator logic
- no provider-specific privilege overrides
- no model-specific prompt hacks

## Why This Scope Is Narrow

The preview release favors comparability and publication speed over full deployment realism. More configuration diversity can be added in later versions, but `preview-v1` intentionally freezes environment variables so the public comparison stays easy to interpret.
