# Launch Model Matrix v1

## Goal

Define a realistic launch set for `preview-v1` that is small enough to execute quickly and large enough to make the leaderboard interesting.

## Selection Rules

- 4 to 6 models maximum
- all models run under `openclaw-preview-v1`
- all models use the same 6 pilot tasks
- each model version must be pinned by provider-visible identifier
- incomplete runs must be recorded, not silently dropped

## Recommended Launch Set

- `openai/gpt-5`
- `anthropic/claude-sonnet-4.5`
- `google/gemini-2.5-pro`
- `qwen/qwen3-32b`
- `deepseek/deepseek-v3.1`

This set gives one preview leaderboard row for major closed-model families plus two strong open-model baselines.

## Run Policy

- benchmark version: `preview-v1`
- profile id: `openclaw-preview-v1`
- pilot tasks: `AE-001`, `AE-002`, `AS-002`, `CD-001`, `PF-001`, `CC-001`
- initial runs per task: `3`
- task timeout: `180` seconds
- retry rule: no automatic retry during preview collection

## Incomplete Run Handling

- missing trace: mark run incomplete
- invalid trace: keep artifact, exclude from aggregate if no valid run result can be produced
- provider failure: record in run notes and rerun only in a later snapshot

## Why This Is Publishable

- small enough to finish quickly
- broad enough to attract attention
- easy to explain on a public leaderboard page
- stable enough to extend into `preview-v2`
