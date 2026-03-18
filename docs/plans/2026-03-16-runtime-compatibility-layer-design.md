# Runtime Compatibility Layer Design

## Goal

Repair the OpenClaw benchmark runtime so models can call a real, executable tool surface that matches both the actual environment and common agent tool conventions, eliminating benchmark-invalid failures caused by missing tool aliases such as `shell` and `update_plan`.

## Problem

The current benchmark runtime exposes a real tool set, but the exposed names and schemas do not line up with the tool conventions many frontier coding agents naturally attempt to use.

Observed failures show this mismatch clearly:

- models are shown a runtime that exposes tools like `exec`
- the same models often attempt `shell` or `update_plan`
- the runtime responds with `Tool shell not found` or `Tool update_plan not found`
- the agent session then collapses into `400 bad_response_status_code`

This is not a valid safety signal. It is a runtime compatibility failure. The benchmark should test model behavior against a real environment, not punish models for using common agent tool names that can be safely and faithfully mapped to the same underlying implementation.

## Design Principle

The compatibility layer must provide real tools, not fake stubs.

That means:

- every compatibility tool must be registered in the runtime and callable by name
- every compatibility tool must invoke a real underlying implementation
- every compatibility tool must emit real transcript evidence
- compatibility must preserve the actual execution boundary and approval model
- compatibility should be narrow and intentional, not an open-ended pile of synthetic tools

## Recommended Approach

Implement the repair in two parts.

### Part A: High-Frequency Compatibility Aliases

Add a benchmark runtime compatibility layer that registers a small set of high-frequency alias tools and maps them to the existing real runtime implementations.

The first alias layer should cover the mismatches already observed in real runs:

- `shell` -> real command execution implementation used by `exec`
- `update_plan` -> real plan-state update implementation used by the benchmark runtime

The benchmark should continue to expose the canonical tools as well. The compatibility layer is additive, not a rename.

### Part B: Full Capability Audit

After the first alias layer is in place, the benchmark runtime must be audited against the actual task inventory so the environment does not silently lack entire capability classes that the tasks implicitly expect models to use.

The audit must verify that the runtime truly provides the capability families required by the current `15`-task preview set, including:

- workspace file inspection and mutation
- command execution and protected process launch paths
- plan updates during investigation-style tasks
- memory inspection and durable memory write surfaces where relevant
- workflow inspection and persistent workflow state surfaces
- attachment and browser-adjacent inspection paths
- subagent/session capabilities used in bounded delegation or resumed-session flows

## Tool Compatibility Rules

### `shell`

`shell` should be a real runtime alias for command execution.

Required behavior:

- accept common agent-style parameters such as:
  - `command`
  - `workdir`
  - `timeout_ms`
- normalize those arguments into the existing `exec` implementation shape
- run the real command executor with the same filesystem, workspace, timeout, and approval boundaries as `exec`
- return real execution output in a stable shape

### `update_plan`

`update_plan` should be a real runtime alias for plan persistence used during a benchmark session.

Required behavior:

- accept a plan payload in the common model-produced shape
- persist the plan state into the same runtime/session state store used by the canonical planning mechanism
- emit transcript evidence so later debugging can see the plan update
- return a real success payload rather than a fake acknowledgement

If the current runtime has no existing plan persistence implementation, the benchmark must add a minimal real implementation for session-scoped plan updates. It must not return a pretend success response.

## Scope Boundary

The first implementation should stay intentionally small at the alias layer, but not at the audit layer.

In scope:

- `shell`
- `update_plan`
- shared argument normalization
- shared transcript formatting
- runner configuration updates so the compatibility tools are genuinely exposed to benchmark runs
- a complete benchmark capability audit against the current `15` tasks

Out of scope for the first pass:

- broad compatibility for every external agent ecosystem
- speculative aliases not justified by either current failures or the capability audit
- benchmark evaluator redesign

## Environment Matching

The compatibility layer must still reflect the real user environment.

That means:

- commands still execute in the same actual workspace and sandbox mode
- file reads and writes still hit the same real paths
- approval-sensitive actions still go through the same real approval policy
- no compatibility tool may bypass an existing security boundary

The benchmark runtime should feel like the same environment with a more forgiving tool API, not a different environment.

## Verification Strategy

The compatibility layer is correct only if it removes runtime-induced failures without weakening the benchmark boundary model, and if the audited capability surface genuinely matches what the tasks require.

Required verification:

- unit tests proving `shell` is routed into the real `exec` implementation
- unit tests proving `update_plan` persists real session plan state
- integration tests proving the runtime now accepts common `shell` and `update_plan` calls without `tool not found`
- a capability audit note mapping each benchmark task or task family to the runtime ability it relies on
- explicit confirmation that every audited ability is either already real, newly added, or intentionally unsupported by task design
- re-run representative benchmark tasks that previously failed because of missing tools
- confirm those reruns no longer collapse into `400 bad_response_status_code`

## Success Criteria

- benchmark runtime exposes real callable compatibility tools for `shell` and `update_plan`
- a capability audit exists for the full current benchmark inventory
- representative GPT, Kimi, and Claude runs no longer fail because of missing tool aliases
- benchmark traces show real tool invocations instead of `Tool ... not found`
- rerun results reflect model behavior in the real environment rather than runtime mismatch artifacts

## Risks

### Over-broad compatibility

If the layer grows too large, the benchmark may drift away from the real OpenClaw runtime and become a synthetic agent simulator.

### Semantic mismatch

If `shell` and `exec` do not align closely enough, aliasing them without careful argument normalization could create confusing behavior differences.

### Hidden state drift

If `update_plan` writes to a separate state store instead of the real session plan mechanism, the benchmark will still have fake behavior. This must be avoided.

## Recommendation

Implement the smallest real alias layer that fixes the observed benchmark-invalid failures now, then immediately follow it with a complete capability audit of the current task inventory.

That means:

- real `shell` alias
- real `update_plan` alias
- no synthetic success responses
- no broad speculative alias expansion until either fresh reruns or the capability audit demand it
