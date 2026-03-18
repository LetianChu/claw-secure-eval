# Static Leaderboard Site Design

## Goal

Build a production-ready static front page for the OpenClaw Security Leaderboard that can be deployed immediately and presents the benchmark more like a real research/product site than a raw repository artifact.

## Why This Shape

- the repository does not currently contain a frontend application scaffold
- the leaderboard data already exists as static JSON and markdown outputs
- the user wants something that can be published immediately

## Delivery Model

- create a self-contained static site under `site/`
- use plain HTML, CSS, and minimal JavaScript
- read leaderboard data from the generated JSON artifact
- require no backend service

## Visual Direction

- reference the information density and confidence of `llm-stats.com`
- avoid cloning its exact visual language
- lean into a research-dashboard tone with a brighter editorial look
- prioritize table readability and strong comparative scanning

## Page Structure

1. hero section
2. leaderboard table section
3. benchmark snapshot section
4. methodology and artifacts section
5. footer with repository and artifact links

## Content Strategy

### Hero

- title: OpenClaw Security Leaderboard
- short explanation of what is being ranked
- current benchmark version and task count
- current leaderboard update timestamp

### Leaderboard Table

- rank
- model
- security score
- boundary failure rate
- approval preserved
- persistence violations
- task completion
- runs

### Benchmark Snapshot

- current baseline size: 15 tasks
- benchmark profile id
- current known failing tasks for the reference baseline
- note that this is a preview but real OpenClaw runtime benchmark

### Methodology / Artifacts

- links to `README.md`
- links to `context.md`
- links to `leaderboard/output/preview-leaderboard.json`
- links to model aggregate JSON files if practical

## Responsive Behavior

- desktop-first leaderboard table
- mobile keeps strong typography and spacing
- wide data table uses horizontal scrolling on narrow screens

## Success Criteria

- site loads as a standalone static page
- leaderboard data is rendered from the current JSON output
- the page feels intentional and publishable, not like a default boilerplate dashboard
- the site can be deployed directly to a static host without extra services
