# Preview 15-Task Aggregate Design

## Goal

Promote the current 15-task preview inventory from a set of individually verified run results into a formal aggregated baseline by regenerating the model aggregate, leaderboard outputs, and summary documents.

## Why This Now

- the repository already contains real run-result artifacts for all 15 current preview tasks
- the official aggregate and leaderboard still reflect the older 11-task snapshot
- this mismatch makes it hard to reason about benchmark progress or compare future expansions cleanly

## Scope

This wave does three things:

- aggregate the current 15 per-task run results into a new model baseline
- regenerate leaderboard outputs from that aggregate
- update key docs so they describe the 15-task baseline honestly and consistently

## Design Principles

- reuse existing run-result artifacts rather than forcing a needless rerun first
- keep the benchmark version stable unless a schema or methodology change requires otherwise
- update documentation only after the aggregate artifacts are written and verified
- keep the distinction between inventory size and aggregate size only if they still differ after regeneration

## Aggregation Strategy

- use `evaluator/results/run-results/preview-v1/moonshot__kimi-k2.5/*/real-smoke-1.json` as the source of truth
- write the new model aggregate to `evaluator/results/model-results/preview-v1/moonshot__kimi-k2.5-full-current.json`
- regenerate leaderboard markdown and JSON from that updated aggregate

## Documentation Strategy

Update these files after the aggregate is regenerated:

- `docs/notes/2026-03-11-single-model-current-run.md`
- `context.md`
- `README.md` if the current snapshot section needs metric updates

The docs should no longer describe the current baseline as an 11-task snapshot if the new aggregate successfully covers all 15 tasks.

## Verification Strategy

- run `pytest -q`
- verify aggregate output shows `tasks_evaluated = 15`
- verify aggregate output shows `runs_evaluated = 15`
- verify leaderboard row updates to `15` runs
- verify task list in the aggregate contains all 15 current task ids

## Success Criteria

- the official model aggregate reflects all 15 current preview tasks
- leaderboard outputs reflect the new 15-task baseline
- summary docs are aligned with the regenerated aggregate
- repository tests remain green
