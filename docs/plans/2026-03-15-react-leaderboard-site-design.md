# React Leaderboard Site Design

## Goal

Build a production-ready leaderboard frontend as a small `Vite + React` application so the site can launch quickly now and still grow into a richer benchmark product later.

## Why Switch From Pure Static HTML

- the user wants immediate publishability and future extensibility
- the repository now has enough moving data to justify components and typed state flow
- React gives an easier path to later add model detail pages, task drilldowns, filters, charts, and multiple leaderboard views

## Delivery Model

- create a standalone frontend app under `site/`
- use `Vite + React`
- read leaderboard data from generated JSON artifacts in the repository
- keep it static-host friendly with no server requirement

## Visual Direction

- inspired by the information density and confidence of `llm-stats.com`
- not a clone; the tone should feel more security-research oriented
- bright editorial layout with strong table readability and benchmark framing
- no generic purple dashboard aesthetic

## App Structure

- `site/index.html`
- `site/src/main.*`
- `site/src/App.*`
- `site/src/components/`
- `site/src/styles/`
- `site/public/` only if static assets are needed

## Initial Page Scope

### Hero

- product title
- one-sentence explanation of OpenClaw security benchmarking
- current benchmark version and profile
- leaderboard update timestamp

### Leaderboard Section

- sortable-feeling but initially static rank table
- model, score, boundary failure rate, approval preserved, persistence violations, task completion, runs

### Benchmark Snapshot Section

- current inventory size
- reference baseline context
- key failure tasks
- note that this is a preview but uses a real OpenClaw runtime

### Methodology / Artifacts Section

- links to README, context, leaderboard JSON, and methodology docs

## Data Strategy

- load `leaderboard/output/preview-leaderboard.json` at runtime
- keep data fetching logic isolated so future API migration is easy
- fail gracefully with a visible error state if data cannot be loaded

## Engineering Principles

- minimal dependency footprint
- componentize only the pieces that are likely to evolve
- preserve static deployability
- make styling deliberate and publishable from the first version

## Success Criteria

- the app builds and runs locally with `Vite`
- the leaderboard page renders from the real JSON artifact
- the UI feels launch-ready rather than like scaffold output
- the codebase is structured cleanly enough for future expansion
