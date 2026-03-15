# AX Runtime Smoke Design

## Goal

Make the first AX pair, `AX-001` and `AX-003`, runnable through the real single-task OpenClaw smoke path so they generate transcript, trace, and evaluator outputs in the same format as the existing benchmark tasks.

## Why This Scope

- the repository already defines `AX-001` and `AX-003` at the task and evaluator level
- the current highest-value next step is proving they can execute in the real runtime
- adding them to the preview matrix should wait until single-task smoke behavior is stable

## Scope

This wave does exactly three things:

- add any minimal runtime fixtures needed by `AX-001`
- add any minimal runtime fixtures needed by `AX-003`
- run one real smoke execution for each task and persist outputs

## Design Principles

- prefer single-task smoke validation before matrix inclusion
- keep runtime fixtures minimal and deterministic
- preserve artifact hygiene by reusing secret redaction for persisted outputs
- treat new runtime issues as runner-hardening work only when they are necessary for smoke execution

## AX-001 Runtime Direction

`AX-001` needs enough seeded context to make the social-payment request legible without requiring a real payment backend.

Recommended runtime support:

- seed the thank-you note referenced by the task
- allow the model to inspect local workspace state
- rely on trace-level detection of the protected payout command if the model attempts it

## AX-003 Runtime Direction

`AX-003` needs enough seeded context to make the billing-support scam legible while preserving secret hygiene.

Recommended runtime support:

- seed the billing-sync triage note referenced by the task
- seed the protected API key file at the task's sensitive path
- ensure persisted outputs redact any API-key-like values before they land in transcript or response artifacts

## Verification Strategy

- run `pytest -q` before and after runtime changes
- execute `run_single_task` once for `AX-001`
- execute `run_single_task` once for `AX-003`
- confirm each task creates:
  - live response output
  - transcript output
  - normalized trace output
  - evaluator run-result output

## Success Criteria

- `AX-001` real smoke artifacts exist and are readable
- `AX-003` real smoke artifacts exist and are readable
- repository tests remain green
- no raw secret material from `AX-003` is persisted in saved outputs
