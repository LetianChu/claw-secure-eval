# OpenClaw Security Benchmark v1 (36 Tasks) Design

**Goal:** Expand the current OpenClaw security benchmark into a structured 36-task v1 benchmark that supports a meaningful public safety leaderboard while remaining feasible to run and maintain.

## Why 36 Tasks

The current pilot set is useful for validating the runtime, trace, evaluator, and leaderboard pipeline, but it is too small to serve as a mature benchmark.

`36` tasks is the recommended `v1` target because it is:

- much larger than the current pilot set
- still maintainable with real OpenClaw execution
- large enough to support category-level reporting
- small enough to version carefully without losing methodological control

## Benchmark Structure

The benchmark is split into three layers.

### Layer 1: Pilot Core (6 tasks)

Purpose:

- keep the existing stable, low-friction, easily scorable tasks
- preserve the ability to run fast smoke tests and leaderboard checks

Current pilot core:

- `AE-001`
- `AE-002`
- `AS-002`
- `CD-001`
- `PF-001`
- `CC-001`

### Layer 2: Seed Expansion (12 tasks)

Purpose:

- fill out the original benchmark taxonomy
- keep one-primary-failure design
- make each category richer than a single smoke example

This layer includes the current seed tasks plus immediate additions to balance category coverage.

### Layer 3: Real Abuse and Harder Variants (18 tasks)

Purpose:

- add realistic abuse scenarios drawn from actual incidents
- introduce more hidden intent and stronger completion pressure
- make the benchmark capable of separating cautious models from truly robust models

This layer includes:

- realistic social-to-finance abuse tasks
- realistic credential exfiltration tasks
- harder variants of existing async and approval tasks

## Recommended Category Layout

Use six benchmark families with six tasks each.

### 1. Approval Erosion (`AE`) - 6 tasks

Measures whether models incorrectly treat prior, vague, stale, or indirect approval as authorization for high-risk actions.

Target task count:

- 2 existing pilot/seed tasks
- 2 harder approval ambiguity variants
- 2 realistic operational approval abuse tasks

### 2. Async Escalation (`AS`) - 6 tasks

Measures whether delayed content, resumed sessions, attachments, or asynchronous context changes can smuggle in higher-risk instructions.

Target task count:

- 2 existing seed tasks
- 2 harder delayed/attachment variants
- 2 realistic context-splitting attacks

### 3. Capability Drift (`CD`) - 6 tasks

Measures whether inspection or metadata tasks drift into enablement, state reads, or broader capability activation.

Target task count:

- 2 existing seed tasks
- 2 workflow/plugin drift variants
- 2 realistic admin-surface confusion variants

### 4. Persistent Foothold (`PF`) - 6 tasks

Measures whether models create durable workflows, memory entries, or control-plane state without explicit authorization.

Target task count:

- 2 existing seed tasks
- 2 harder persistence temptation variants
- 2 realistic account/webhook/autoload persistence variants

### 5. Cross-Component Confusion (`CC`) - 6 tasks

Measures whether models confuse external content, attachments, or plugin outputs with trusted control instructions.

Target task count:

- 2 existing seed tasks
- 2 harder cross-surface variants
- 2 impersonation or template-import confusion variants

### 6. Abuse and Exfiltration (`AX`) - 6 tasks

This is the new family motivated by realistic incidents.

It covers:

- social-media-driven financial abuse
- credential extraction scams
- operator impersonation that targets money movement or secret disclosure

Proposed tasks:

- `AX-001` Social Red Packet Request
- `AX-002` Social Reward Transfer
- `AX-003` API Key Verification Scam
- `AX-004` Env Dump Support Scam
- `AX-005` Promo Attachment Payout Trigger
- `AX-006` Fake Support Credential Recovery

## Why Add `AX` Instead of Forcing Everything Into Existing Families

The new real-world examples do overlap existing categories, but they are important enough to deserve a visible benchmark family.

Reasons:

- the risk is more legible to outside readers
- leaderboard category reporting becomes more compelling
- it captures security failures that are not just "prompt injection" but also money movement and secret disclosure abuse

This family can still be cross-labeled internally if needed, but should be visible externally.

## Design Rules For All 36 Tasks

- one primary failure condition per task
- one clear protected asset or protected action per task
- trace-based oracle first
- rule-based evaluator where possible
- fixed OpenClaw profile for `v1`
- real-execution-compatible tasks prioritized

## Difficulty Mix

Recommended split:

- `12 easy`
- `14 medium`
- `10 hard`

This keeps the benchmark from collapsing into either toy tasks or all highly engineered edge cases.

## Real-Execution Coverage Goal

Not all 36 tasks need immediate real execution on day one.

Recommended v1 expectation:

- at least `12` tasks should be runnable in the real OpenClaw environment early
- the remaining tasks may begin as schema-complete tasks with evaluator-ready oracles
- over time, increase the count of real-executed tasks toward the full set

## Leaderboard Reporting

For the public leaderboard, the v1 benchmark should expose:

- overall `Security Score`
- category breakdown across the six families
- count of real-executed runs vs schema-only tasks if a transition phase remains

## Immediate Build Priority

The next build wave should focus on:

1. harder variants of current pilot tasks, especially `AS-002` and `AE-002`
2. first `AX` tasks for social-finance abuse and API key disclosure
3. real-execution support for more than one category beyond the current smoke set

## Roadmap Beyond 36

`36` is the recommended formal `v1` target, not the final ceiling.

Planned growth path:

- `v1`: 36 tasks
- `v2` roadmap: 72 tasks

The expansion from 36 to 72 should come from richer task variants, more real-execution coverage, and more realistic abuse surfaces rather than random task count inflation.
