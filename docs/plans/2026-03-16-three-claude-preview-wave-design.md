# Three-Claude Preview Wave Design

## Goal

Extend the current real `15`-task preview leaderboard with three Claude models from the existing OpenAI-compatible endpoint so the benchmark becomes a richer cross-provider comparison without re-running the already completed six-model baseline.

## Scope

- add `claude-haiku-4-5-20251001`
- add `claude-sonnet-4-6`
- add `claude-opus-4-6`
- keep the current benchmark version at `preview-v1-current-real`
- keep the current profile id at `openclaw-preview-v1`
- preserve the existing six published model aggregates unless new evidence requires replacement

## Why This Approach

- the current benchmark and evaluator are already stable enough to compare additional models on the same `15`-task baseline
- the configured `API_BASE_URL_2` endpoint now exposes both GPT and Claude ids, so the next comparison wave can broaden provider coverage without new infrastructure
- reusing the existing six-model artifacts avoids unnecessary cost and time while keeping the comparison directly tied to the same benchmark version and evaluator logic

## Candidate Models

Use the currently confirmed Claude ids from `API_BASE_URL_2`:

- `claude-haiku-4-5-20251001`
- `claude-sonnet-4-6`
- `claude-opus-4-6`

These three provide a lightweight, mid-tier, and top-tier Claude slice, which is enough to reveal whether the current benchmark can separate Claude variants better than it separates the current GPT set.

## Delivery Model

- verify the endpoint still exposes the three chosen Claude ids before running anything expensive
- produce one full `15`-task real run-result set per Claude model using the existing `run_single_task()` path
- aggregate each Claude model into its own model-result JSON under `evaluator/results/model-results/preview-v1/`
- regenerate the leaderboard from the existing six aggregates plus the three new Claude aggregates

## Execution Strategy

- use `benchmark/runs/single_model_runner.py` as the only runtime entrypoint for each task/model pair
- route all three Claude models through the existing `API_BASE_URL_2` endpoint, the same way the GPT models were routed
- generate or refresh these artifact families for each Claude model:
  - `benchmark/live-output/preview-v1/`
  - `benchmark/traces/preview-v1/`
  - `evaluator/results/run-results/preview-v1/`
- aggregate only after all `15` run-result files exist for a given Claude model
- publish a new leaderboard only after all three Claude aggregates are complete

## Data And Artifact Rules

- do not modify the current six-model aggregate files unless a verification issue forces regeneration
- do not include partial Claude coverage in the published leaderboard
- keep output naming consistent with the existing provider-prefixed convention used by GPT and Kimi models
- keep all generated artifacts versioned under the existing `preview-v1` folder structure

## Validation Strategy

- re-check `/models` for the three Claude ids before the run wave begins
- verify repository tests before and after the run wave
- verify each Claude model has exactly `15` run-result JSON files at `real-smoke-1.json`
- verify each Claude aggregate reports:
  - `tasks_evaluated = 15`
  - `runs_evaluated = 15`
- verify the regenerated leaderboard contains `9` ranked rows
- verify ordering still follows the current leaderboard sort rules

## Risks

### Runtime Compatibility

Claude models may expose different tool-calling behavior than the current GPT runs. That may produce new failure shapes, especially on tasks where the current OpenAI-compatible path already showed tool-name mismatch issues.

### Benchmark Resolution

The current evaluator remains fairly coarse. Even after adding Claude models, some variants may still tie if they land in the same boundary-failure and task-completion buckets.

### Publishability Risk

If one Claude model fails to complete all `15` tasks, including it in the leaderboard would reduce comparability. The publish rule should remain strict: complete models only.

## Success Criteria

- three new Claude model run-result sets exist with full `15`-task coverage
- three new Claude aggregate JSON files exist under `evaluator/results/model-results/preview-v1/`
- `leaderboard/output/preview-leaderboard.json` and `leaderboard/output/preview-leaderboard.md` expand from `6` rows to `9` rows
- the leaderboard still uses a single benchmark version and a single profile id across every row
- the published result gives a meaningful first cross-provider comparison between GPT, Claude, and Kimi on the same OpenClaw preview baseline
