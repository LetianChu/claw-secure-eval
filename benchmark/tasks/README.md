# Seed Benchmark Tasks

This directory contains the first 10 experiment-first task manifests for messaging-controlled privileged agents.

## Naming

- `AE-*`: approval erosion
- `AS-*`: async escalation
- `CD-*`: capability drift
- `PF-*`: persistent foothold
- `CC-*`: cross-component confusion
- `RB-*`: resource exhaustion

## Common Assumptions

- `host_type: local_vm`
- `message_channel: synthetic_enterprise_im`
- 2-4 messages per task
- one primary protected asset per task
- one primary boundary failure per task

## Validation

All YAML files should conform to `benchmark/schema/task-schema.json` and include:

- a concrete protected asset
- explicit allowed and disallowed actions
- rule-based failure conditions over observable traces
- safe completion conditions that do not depend on assistant wording alone

## Pilot First

Prioritize these six tasks for the first pilot run:

- `AE-001`
- `AE-002`
- `AS-002`
- `CD-001`
- `PF-001`
- `CC-001`

## Evaluator v0 Expectations

The first evaluator version should focus on simple trace matching over:

- `file_read`
- `file_write`
- `process_launch`
- `approval_event`
- `network_event`
- optional extensions: `workflow_enable`, `config_change`
