# Three-Claude Run Config

## Goal

Freeze the local model-to-endpoint mapping for the incremental three-Claude evaluation wave without copying secret values from the local env file.

## Selected Models

- `anthropic/claude-haiku-4-5-20251001`
- `anthropic/claude-sonnet-4-6`
- `anthropic/claude-opus-4-6`

## Endpoint Mapping

Use the existing OpenAI-compatible local endpoint:

- env var: `API_BASE_URL_2`
- base URL: `https://api-s.zwenooo.link/v1`

## Endpoint Verification

A fresh `/models` check against `API_BASE_URL_2` confirmed the selected Claude ids are currently exposed.

Observed selected ids:

- `claude-haiku-4-5-20251001`
- `claude-sonnet-4-6`
- `claude-opus-4-6`

Other observed ids on the same endpoint during the same check included:

- `claude-opus-4-5-20251101`
- `claude-opus-4-5-20251101-thinking`
- `claude-opus-4-6`
- `claude-sonnet-4-5-20250929`
- `claude-sonnet-4-6`
- `gpt-5`
- `gpt-5.1`
- `gpt-5.1-codex`
- `gpt-5.1-codex-max`
- `gpt-5.1-codex-mini`
- `gpt-5.2`
- `gpt-5.2-codex`
- `gpt-5.3-codex`
- `gpt-5.4`

## Runtime Notes

- the benchmark runner now accepts the selected Claude ids using the `anthropic/` prefix while still routing them through the same OpenAI-compatible provider config behind `API_BASE_URL_2`
- do not copy or commit raw `API_KEY_2` values
- publish only complete `15`-task Claude aggregates to keep the leaderboard directly comparable
