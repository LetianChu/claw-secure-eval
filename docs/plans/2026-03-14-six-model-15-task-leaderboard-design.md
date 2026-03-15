# Six-Model 15-Task Leaderboard Design

## Goal

Run six requested models against the current formal 15-task preview baseline and publish the first genuinely comparative multi-model OpenClaw leaderboard.

## Requested Model Set

- `gpt-5.1-codex`
- `gpt-5.2`
- `gpt-5.4`
- `kimi-k2.5`
- `kimi-k2-0905-preview`
- `kimi-k2-0711-preview`

## Why This Scope

- the 15-task baseline is now formally aggregated and documented
- the user explicitly wants a multi-model leaderboard, not just more task expansion
- these six models are actually reachable through the currently available API endpoints

## Design Principles

- keep all model comparisons on the same 15-task benchmark version and profile
- treat each model run as independent and reproducible
- do not mix smoke-only outputs into the leaderboard; use complete 15-task result sets only
- prefer a small amount of configuration glue over one-off manual command variance

## Execution Strategy

- use the existing single-task real runner as the execution path for every task/model combination
- generate one run-result per task for each model
- aggregate each model into its own model-results JSON
- regenerate the leaderboard from all completed model aggregates together

## API Strategy

- `moonshot` endpoint for the three Kimi models
- OpenAI-compatible third-party endpoint for the three GPT models
- configure model-to-endpoint mapping explicitly so runs do not depend on ambiguous global state

## Verification Strategy

- confirm the two API endpoints expose the expected model ids before running
- run repository tests before the long evaluation wave
- verify each completed model has 15 run results before aggregating it
- regenerate leaderboard only from models with complete 15-task result sets

## Success Criteria

- all six requested models have complete 15-task run-result sets
- six model aggregate JSON files exist under `evaluator/results/model-results/preview-v1/`
- leaderboard markdown and JSON contain six ranked rows
- the resulting leaderboard is fully comparable on the same 15-task baseline
