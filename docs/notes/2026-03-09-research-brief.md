# Research Brief: Messaging-Controlled Privileged Agents

## Working Title

Remote Messages, Local Actions: Benchmarking Security Boundary Failures in Messaging-Controlled Privileged Agents

## Core Question

In real deployments, users increasingly run an AI agent on a local privileged device and control it remotely through an enterprise messaging channel. Under multi-turn asynchronous interaction and capability composition, which security boundaries fail first, why do they fail, and how can we evaluate those failures systematically?

## Motivation

- Many existing evaluations study prompt injection in tool-using agents.
- Others study direct computer-use on local operating systems.
- But a common deployment pattern sits between these two: enterprise messaging controls a local privileged agent that can touch files, execute commands, invoke workflows, and persist state.
- This setting introduces asynchronous interaction, stale context, approval drift, and long-lived state changes that are not captured well by current benchmarks.

## Deployment Pattern of Interest

- Enterprise IM -> agent runtime -> local tools/workflows/skills/plugins -> local privileged host
- OpenClaw is the primary motivating platform because it closely matches this deployment style.
- OpenClaw should be treated as the main case study platform, not the full scope of the paper.

## Proposed Contributions

1. A benchmark setting for messaging-controlled local privileged agents.
2. An execution-trace-based evaluator for real boundary failures.
3. A failure taxonomy for asynchronous, capability-composed agent deployments.
4. An empirical study across configuration, isolation, and capability settings.

## Target Failure Families

- Approval erosion
- Async escalation
- Capability drift
- Persistent foothold
- Cross-component confusion

## Boundary Types

- File confidentiality
- File integrity
- Command execution
- Network exfiltration
- Approval integrity
- Capability integrity
- Session isolation
- Persistence and control-plane integrity

## Evaluation Principle

Do not score tasks based on assistant text alone. Judge success or failure from real execution traces, such as:

- tool calls
- process launches
- file changes
- network requests
- approval events
- config or workflow persistence changes

## Novelty Positioning

- Not another generic prompt injection benchmark.
- Not another direct computer-use benchmark.
- Not an OpenClaw-only benchmark.
- The key novelty is the deployment setting: messaging-mediated, asynchronous, remote control over a local privileged agent with composable capabilities.

## Tentative Venues

- ACL / EMNLP / NAACL for benchmark and evaluation framing
- ICLR if the automated evaluator and methodology become the central novelty
- NeurIPS Datasets and Benchmarks if the benchmark becomes broad and reusable enough
