# Root README Design

## Goal

Create a root `README.md` that works as the repository front door for first-time visitors while still giving research collaborators a clear snapshot of the benchmark's current status.

## Audience

- first-time visitors who need to understand what this repository is
- research or evaluation collaborators who need the current benchmark state quickly

## Recommended Structure

1. project overview
2. why this repository exists
3. current snapshot
4. repository map
5. quick start
6. key artifacts
7. roadmap

## Content Decisions

- Lead with a plain-language description of the repository as a real, versioned OpenClaw security benchmark and leaderboard.
- Include the current benchmark state from `context.md`, including the 11-task real library, the long-term 36-task target, the current single-model baseline, and known failure cases.
- Keep setup instructions lightweight and practical rather than exhaustive.
- Link readers to the design docs, implementation plan, run summary, and generated leaderboard.
- Avoid over-claiming maturity; make clear that the current leaderboard is a single-model real baseline snapshot.

## Success Criteria

- A new visitor can understand the project in under a minute.
- A collaborator can find the current results and key planning documents immediately.
- The README reflects the repository's current state without duplicating too much internal documentation.
