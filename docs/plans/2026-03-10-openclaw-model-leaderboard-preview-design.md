# OpenClaw Model Leaderboard Preview Design

**Goal:** Design a preview leaderboard that compares model security behavior inside a fixed OpenClaw environment and can evolve into a continuously updated public benchmark product.

## Product Positioning

This is not a generic model capability leaderboard. It is a security-behavior leaderboard for models operating inside OpenClaw.

The product claim for the preview release is intentionally narrow:

- fixed OpenClaw platform
- fixed pilot task set
- fixed scoring rules
- model-only comparison

The leaderboard must avoid implying universal model safety rankings across all agents, tools, or deployment environments.

## Release Strategy

The first release is a `Preview` leaderboard.

Preview means:

- only the pilot benchmark is used
- only one OpenClaw configuration is used
- only a limited model set is evaluated
- methodology is visible and versioned
- future updates are expected and explicitly announced

The preview release is followed by rolling updates:

- add more models
- add more benchmark tasks
- add repeated runs
- add versioned methodology changes

## Fixed Comparison Unit

The leaderboard compares different models under the same OpenClaw setup.

For preview `v1`, keep these fixed:

- OpenClaw profile
- tool surface
- sandbox level
- approval policy
- persistent state assumptions
- task set
- score formula

Only the model changes.

## Benchmark Layers

### Layer 1: Preview Benchmark

The preview benchmark is the public launch benchmark.

Use these 6 pilot tasks:

- `AE-001`
- `AE-002`
- `AS-002`
- `CD-001`
- `PF-001`
- `CC-001`

Preview benchmark design rules:

- each task has one primary failure condition
- each task uses a rule-based oracle
- each task is trace-checkable
- each task is short enough for public explanation

### Layer 2: Full Benchmark

The full benchmark is the long-term expansion path.

The current seed set contains 10 tasks, and later versions can expand to 20 plus tasks with:

- more task variants
- more failure families
- harder async and persistence cases
- repeated-run stability analysis

## Scoring Philosophy

The leaderboard should reward safe behavior before successful task completion.

Preview scoring principles:

- severe boundary failures dominate score
- approval violations are strongly penalized
- persistence violations are strongly penalized
- task completion matters, but cannot cancel out serious safety failures

The public page should show both a single summary score and decomposed metrics.

## Public Metrics

Each model entry should expose:

- `Security Score`
- `Boundary Failure Rate`
- `Approval Preserved Rate`
- `Persistence Violation Rate`
- `Task Completion Rate`
- `Runs`
- `Last Updated`

## Frontend Direction

The frontend should borrow the strong leaderboard-first information architecture from the reference site while staying clearly security-focused.

### Core UI structure

- hero section with title, subtitle, preview tag, and update timestamp
- benchmark switcher area reserved for future versions
- filter bar for model provider, openness, version status, and benchmark version
- sortable leaderboard table as the main element
- linked detail pages or sections for methodology, tasks, models, and changelog

### Main table columns

- `Rank`
- `Model`
- `Security Score`
- `Boundary Failure Rate`
- `Approval Preserved`
- `Persistence Violations`
- `Task Completion`
- `Runs`
- `Last Updated`

### Detail page expectations

Each model detail view should include:

- model metadata
- evaluated benchmark version
- per-task outcomes
- failure-family breakdown
- representative failure summary
- methodology and limitations links

## Content and Trust Signals

The leaderboard must visibly include:

- methodology summary
- exact benchmark version
- exact OpenClaw profile version
- clear preview disclaimer
- changelog for score-impacting updates

## Required Disclaimer Language

The preview release must state:

- this leaderboard measures security behavior in OpenClaw only
- this is a preview benchmark with a 6-task pilot set
- results do not imply universal model safety rankings
- scores may change as tasks, evaluator logic, and run counts evolve

## Launch Criteria for Preview v1

Before publishing, the project should have:

- 6 pilot tasks frozen
- one fixed OpenClaw preview profile frozen
- evaluator v0 implemented for pilot tasks
- trace and result schema documented
- 4 to 6 launch models selected
- one generated leaderboard output
- methodology and disclaimer page written

## Long-Term Update Policy Direction

Every future public update should version:

- benchmark set
- evaluator logic
- score formula
- OpenClaw profile
- model version identifiers

This avoids silent score drift and makes the leaderboard a credible benchmark product rather than a one-off chart.
