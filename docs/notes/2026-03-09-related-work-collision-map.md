# Related Work Collision Map

## Positioning Goal

This project should not be framed as an OpenClaw vulnerability paper or a generic prompt injection benchmark. The intended contribution is a benchmark and evaluator for messaging-controlled local privileged agents under asynchronous multi-turn interaction and capability composition.

## Cluster 1: Prompt Injection Benchmarks

Representative work:

- InjecAgent
- AgentDojo
- BIPIA
- AgentDyn

Overlap:

- High overlap on tool-using agent safety and indirect prompt injection.

Key distinction:

- These works center prompt injection attacks at runtime.
- Our work centers a deployment regime: enterprise messaging asynchronously controlling a local privileged host.
- Our evaluation focuses on boundary failures observed through real host actions and persistent state changes.

## Cluster 2: Computer-Use and OS Benchmarks

Representative work:

- OSWorld
- OSWorld-MCP
- AgentBench

Overlap:

- Medium to high overlap on realistic local environments.

Key distinction:

- These works emphasize direct control of operating systems or tools.
- Our work studies message-mediated control, asynchronous history, approval semantics, and state persistence.

## Cluster 3: Tool-Use Safety and Risk Benchmarks

Representative work:

- ToolEmu
- CyberSecEval 2
- CIBER
- LPS-Bench

Overlap:

- Medium overlap on tool misuse and long-horizon safety.

Key distinction:

- These works study broad tool risk.
- Our work isolates a concrete remote-control setting where enterprise IM drives host-side actions on a privileged machine.

## Cluster 4: Skill, Tool, and Plugin Ecosystem Security

Representative work:

- ToolHijacker
- SkillInject
- ChatGPT plugin ecosystem studies

Overlap:

- Medium to high overlap on capability ecosystems and malicious tool metadata or artifacts.

Key distinction:

- Existing work usually focuses on one layer: tool descriptions, skill files, or plugin auth.
- Our work studies how these layers combine with asynchronous remote control and local host privileges.

## Cluster 5: OpenClaw-Specific Security Evaluation

Representative work:

- From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenClaw for Personalized Local AI Agent (PASB, 2026)

Overlap:

- Very high overlap if we position the paper as an OpenClaw security benchmark.

Required differentiation:

- OpenClaw must be the primary platform, not the primary claim.
- The paper must target messaging-controlled privileged agents as a deployment class.
- OpenClaw should serve as the strongest motivating case study and testbed.

## Safe Novelty Wedge

The cleanest novelty statement is:

- We benchmark security boundary failures in messaging-controlled local privileged agents.
- We focus on asynchronous multi-turn remote operation through enterprise messaging channels.
- We evaluate real host-side actions, approval integrity, and persistent state manipulation under capability composition.

## What To Avoid Claiming

- Another prompt injection benchmark for tool agents
- An OpenClaw-specific benchmark as the main contribution
- A pure plugin or skill poisoning paper
- A generic local-agent safety paper without deployment realism

## Working Positioning Paragraph

Prior work studies prompt injection in tool-using agents, direct computer-use in realistic operating system environments, and security risks in tool or plugin ecosystems. However, existing benchmarks largely miss a common deployment regime in which a user remotely operates a local privileged agent through an enterprise messaging channel. This setting introduces asynchronous multi-turn control, approval drift, persistent state manipulation, and cross-component capability composition, which are not captured well by existing evaluations. We therefore study security boundary failures in messaging-controlled privileged agents, using OpenClaw-style deployments as a primary but not exclusive instantiation.
