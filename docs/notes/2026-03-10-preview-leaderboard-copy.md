# Preview Leaderboard Copy

## Intro

OpenClaw Safety Leaderboard is a preview benchmark that compares how models behave under security-sensitive tasks inside a fixed OpenClaw environment.

## Methodology Summary

`preview-v1` uses a fixed OpenClaw profile, a 6-task pilot benchmark, and a rule-based evaluator that scores boundary failures, approval preservation, persistence violations, and safe task completion.

The launch matrix uses 3 runs per task with a 180 second timeout and no automatic retry in preview mode.

## Limitations

- this is an OpenClaw-only measurement
- this is a preview benchmark with six pilot tasks
- results do not imply universal model safety rankings

## Update Note

Future versions will expand the task set, add more models, and publish versioned leaderboard snapshots.

Incomplete runs are recorded explicitly instead of being silently converted into successful scores.
