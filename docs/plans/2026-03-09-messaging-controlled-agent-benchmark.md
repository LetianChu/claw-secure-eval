# Messaging-Controlled Agent Benchmark Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build the first pilot benchmark and evaluator for security boundary failures in messaging-controlled privileged agents.

**Architecture:** Start with a VM-based testbed that simulates an enterprise messaging channel controlling a local privileged agent runtime. Define a small seed benchmark, capture execution traces, and implement task oracles that score real boundary failures instead of assistant text.

**Tech Stack:** Virtual machines, Python or TypeScript orchestration, OpenClaw test deployment, structured execution logs, benchmark task manifests in YAML or JSON.

---

### Task 1: Lock Problem Statement

**Files:**
- Review: `D:/openclaw-agent-security/docs/notes/2026-03-09-research-brief.md`
- Review: `D:/openclaw-agent-security/docs/notes/2026-03-09-related-work-collision-map.md`
- Create: `D:/openclaw-agent-security/docs/notes/2026-03-09-problem-statement-v1.md`

**Step 1: Write the short paper problem statement**

Include:

- setting
- threat model
- novelty wedge
- non-goals

**Step 2: Review against related work**

Check that the statement does not collapse into:

- generic prompt injection
- OpenClaw-only evaluation
- generic local-agent safety

**Step 3: Freeze one sentence of contribution framing**

Expected output:

- one title line
- one contribution paragraph
- one sentence on why existing benchmarks are insufficient

### Task 2: Define Benchmark Schema

**Files:**
- Create: `D:/openclaw-agent-security/docs/notes/2026-03-09-task-schema-v1.md`
- Create: `D:/openclaw-agent-security/benchmark/schema/task-schema.json`

**Step 1: Define benchmark fields**

Required fields:

- task id
- deployment profile
- message history
- protected asset
- allowed actions
- disallowed actions
- oracle definition
- severity weight

**Step 2: Write three example tasks**

Include one task each for:

- approval erosion
- async escalation
- persistent foothold

**Step 3: Review for automatic scoring**

Ensure every task can be judged by traces rather than natural-language interpretation.

### Task 3: Build VM Testbed Prototype

**Files:**
- Create: `D:/openclaw-agent-security/testbed/README.md`
- Create: `D:/openclaw-agent-security/testbed/docker-compose.yml` or VM setup notes
- Create: `D:/openclaw-agent-security/testbed/message-adapter/README.md`

**Step 1: Choose the first reproducible environment**

Recommended default:

- one Linux VM
- one OpenClaw deployment
- one synthetic enterprise-messaging adapter

**Step 2: Define trace capture points**

Capture at least:

- incoming message events
- tool calls
- host command execution
- file writes
- approval events

**Step 3: Run one end-to-end smoke test**

Expected result:

- a single remote message triggers a controlled agent action and emits a complete trace

### Task 4: Create Seed Benchmark v0

**Files:**
- Create: `D:/openclaw-agent-security/benchmark/tasks/`
- Create: `D:/openclaw-agent-security/benchmark/tasks/README.md`

**Step 1: Write 10 seed tasks**

Distribution:

- 2 approval erosion
- 2 async escalation
- 2 capability drift
- 2 persistent foothold
- 2 cross-component confusion

**Step 2: Validate task completeness**

Each task must specify:

- initial state
- message sequence
- expected safe behavior
- failure oracle

**Step 3: Pilot-run the easiest 3 tasks**

Expected result:

- at least one task differentiates two configuration settings

### Task 5: Implement Evaluator v0

**Files:**
- Create: `D:/openclaw-agent-security/evaluator/README.md`
- Create: `D:/openclaw-agent-security/evaluator/oracles/`
- Create: `D:/openclaw-agent-security/evaluator/results/`

**Step 1: Define scoring outputs**

Minimum outputs:

- task success
- boundary failure
- approval preserved or not
- persistence observed or not

**Step 2: Implement rule-based oracles first**

Do not start with an LLM judge.

Use:

- trace events
- state diffs
- network and file logs

**Step 3: Run a pilot evaluation table**

Compare:

- minimal tools vs broader tools
- sandbox on vs sandbox off

### Task 6: Write Pilot Study Summary

**Files:**
- Create: `D:/openclaw-agent-security/docs/notes/2026-03-09-pilot-study-template.md`

**Step 1: Record setup and limitations**

Include:

- VM environment
- synthetic messaging assumptions
- OpenClaw configuration

**Step 2: Record first results**

Include:

- number of tasks run
- number of failures found
- which settings most affect boundary robustness

**Step 3: Decide next expansion axis**

Pick one:

- real enterprise messaging integration
- more tasks
- stronger evaluator automation
- second platform baseline
