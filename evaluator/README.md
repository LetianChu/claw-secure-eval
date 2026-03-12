# Evaluator v0

This directory contains the first rule-based evaluator for the OpenClaw preview leaderboard.

## Scope

Evaluator v0 supports the six pilot tasks:

- `AE-001`
- `AE-002`
- `AS-002`
- `CD-001`
- `PF-001`
- `CC-001`

## Run Result Fields

- `task_completed`
- `boundary_failed`
- `approval_preserved`
- `persistence_observed`

For `preview-v1`, `persistence_observed` is interpreted as a persistence violation observed in the trace.

## Aggregate Fields

- `security_score`
- `boundary_failure_rate`
- `approval_preserved_rate`
- `persistence_violation_rate`
- `task_completion_rate`
- `tasks_evaluated`
- `runs_evaluated`

## Current Approach

The evaluator is rule-based. It reads task ids plus normalized traces and applies explicit checks for protected file reads, protected command launches, approval ordering, and persistence writes.

This version is intentionally simple so the preview leaderboard is transparent and easy to audit.
