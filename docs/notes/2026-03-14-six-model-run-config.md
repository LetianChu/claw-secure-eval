# Six-Model Run Config

## Goal

Freeze the local model-to-endpoint mapping for the current six-model leaderboard wave without copying secrets from `D:/openclaw-agent-security/.env.openclaw.local`.

## Local Endpoint Mapping

`D:/openclaw-agent-security/.env.openclaw.local` currently defines two local OpenAI-compatible endpoints:

- `API_BASE_URL_1`: `https://api.moonshot.cn/v1`
- `API_BASE_URL_2`: `https://api-s.zwenooo.link/v1`

Use this mapping for the six-model run wave:

| Model id | Endpoint var | Base URL | Notes |
| --- | --- | --- | --- |
| `moonshot/kimi-k2.5` | `API_BASE_URL_1` | `https://api.moonshot.cn/v1` | Moonshot endpoint |
| `moonshot/kimi-k2-0905-preview` | `API_BASE_URL_1` | `https://api.moonshot.cn/v1` | Moonshot endpoint |
| `moonshot/kimi-k2-0711-preview` | `API_BASE_URL_1` | `https://api.moonshot.cn/v1` | Moonshot endpoint |
| `openai/gpt-5.1-codex` | `API_BASE_URL_2` | `https://api-s.zwenooo.link/v1` | OpenAI-compatible endpoint |
| `openai/gpt-5.2` | `API_BASE_URL_2` | `https://api-s.zwenooo.link/v1` | OpenAI-compatible endpoint |
| `openai/gpt-5.4` | `API_BASE_URL_2` | `https://api-s.zwenooo.link/v1` | OpenAI-compatible endpoint |

## Endpoint Verification

Verification checked each configured `/models` endpoint using the local env file and confirmed that every requested model id is exposed.

### `API_BASE_URL_1`

- endpoint: `https://api.moonshot.cn/v1`
- requested ids found: `kimi-k2.5`, `kimi-k2-0905-preview`, `kimi-k2-0711-preview`
- additional ids observed during verification included `kimi-k2-thinking`, `kimi-k2-thinking-turbo`, `kimi-k2-turbo-preview`, and multiple `moonshot-v1-*` variants

### `API_BASE_URL_2`

- endpoint: `https://api-s.zwenooo.link/v1`
- requested ids found: `gpt-5.1-codex`, `gpt-5.2`, `gpt-5.4`
- additional ids observed during verification included `gpt-5`, `gpt-5.1`, `gpt-5.1-codex-max`, `gpt-5.1-codex-mini`, `gpt-5.2-codex`, and `gpt-5.3-codex`

## Local Config Notes

- Do not copy raw `API_KEY_*` values into versioned notes or committed config.
- The root local env file currently keeps provider-specific `OPENCLAW_MODEL_*` variables blank, so this note is the explicit source of truth for the six-model wave routing.
