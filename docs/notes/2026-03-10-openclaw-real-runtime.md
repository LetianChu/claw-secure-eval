# OpenClaw Real Runtime Notes

## What Is Running

OpenClaw is now running inside `Ubuntu-24.04` on WSL2, with the gateway hosted in Docker.

Runtime layout:

- WSL distro: `Ubuntu-24.04`
- repo root in WSL: `~/openclaw`
- config dir in WSL: `/root/.openclaw`
- gateway health: `http://127.0.0.1:18789/healthz`

## How To Talk To OpenClaw

For benchmark work, the cleanest entrypoint is direct CLI invocation through the gateway.

Reference shape:

```bash
wsl -d Ubuntu-24.04 -- bash -lc 'cd ~/openclaw && docker compose run -T --rm openclaw-cli agent --agent "main" --message "Reply READY" --json'
```

This does not require an external IM channel. It uses the same gateway-backed agent runtime, but drives it from a deterministic CLI entrypoint that is easier to automate for benchmarking.

## Why This Is Enough For Benchmarking

For the first real benchmark runs, we do not need WhatsApp, Telegram, or Slack.

We need:

- a real OpenClaw gateway
- a real model backend
- a deterministic session entrypoint
- captured runtime outputs and traces

The direct `openclaw agent` path satisfies the first three once model credentials are configured.

## Current Blocker

The gateway is healthy, but no working provider credential has been configured yet.

OpenClaw currently reports the default model as:

- `anthropic/claude-opus-4-6`

Before a real agent turn can succeed, the runtime needs a valid provider credential for the selected model, or a different reachable model backend must be configured.

## Next Benchmark Step

Once credentials are present, the first smoke flow is:

1. run one direct `openclaw agent --agent main --message ... --json`
2. save the raw output and gateway logs
3. normalize the run into a trace artifact
4. feed the trace into the evaluator and leaderboard pipeline

## Helper Code

The repo now contains a small helper module for building these runtime commands:

- `benchmark/runs/real_openclaw_runtime.py`

Its tests are in:

- `benchmark/runs/tests/test_real_openclaw_runtime.py`
