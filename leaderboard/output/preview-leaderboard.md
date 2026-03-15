# OpenClaw Safety Leaderboard

**Preview**

- benchmark version: `preview-v1-current-real`
- profile id: `openclaw-preview-v1`
- disclaimer: Preview leaderboard measured in OpenClaw only; results do not imply universal model safety rankings.
- methodology: [Methodology](methodology.md)

OpenClaw Safety Leaderboard compares model security behavior under a fixed OpenClaw setup and a versioned benchmark set.

| Rank | Model | Security Score | Boundary Failure Rate | Approval Preserved | Persistence Violations | Task Completion | Runs | Last Updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | openai/gpt-5.1-codex | 96.67 | 0.0667 | 1.0000 | 0.0000 | 0.8667 | 15 | 2026-03-15T12:23:53Z |
| 2 | openai/gpt-5.2 | 96.67 | 0.0667 | 1.0000 | 0.0000 | 0.8667 | 15 | 2026-03-15T12:23:53Z |
| 3 | openai/gpt-5.4 | 96.67 | 0.0667 | 1.0000 | 0.0000 | 0.8667 | 15 | 2026-03-15T12:23:53Z |
| 4 | moonshot/kimi-k2.5 | 86.67 | 0.2667 | 1.0000 | 0.0000 | 0.9333 | 15 | 2026-03-15T12:23:53Z |
| 5 | moonshot/kimi-k2-0711-preview | 80.00 | 0.4000 | 1.0000 | 0.0000 | 0.8667 | 15 | 2026-03-15T12:23:53Z |
| 6 | moonshot/kimi-k2-0905-preview | 80.00 | 0.4000 | 1.0000 | 0.0000 | 0.8667 | 15 | 2026-03-15T12:23:53Z |

## Limitations

This is a preview release with platform-specific scope; scores may change as tasks, evaluator logic, and run counts evolve.
