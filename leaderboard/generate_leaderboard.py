from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DISCLAIMER = (
    "Preview leaderboard measured in OpenClaw only; "
    "results do not imply universal model safety rankings."
)
INTRO = (
    "OpenClaw Safety Leaderboard compares model security behavior under a fixed "
    "OpenClaw setup and a versioned benchmark set."
)
LIMITATIONS = (
    "This is a preview release with platform-specific scope; scores may change as "
    "tasks, evaluator logic, and run counts evolve."
)


def _load_entries(paths: list[str | Path]) -> list[dict[str, Any]]:
    return [json.loads(Path(path).read_text(encoding="utf-8")) for path in paths]


def _validate_entries(
    entries: list[dict[str, Any]],
    *,
    benchmark_version: str,
    profile_id: str,
    expected_runs: int | None = None,
) -> None:
    for entry in entries:
        if entry.get("benchmark_version") != benchmark_version:
            raise ValueError("Input model result benchmark_version does not match")
        if entry.get("profile_id") != profile_id:
            raise ValueError("Input model result profile_id does not match")
        if expected_runs is not None and entry.get("runs_evaluated", 0) < expected_runs:
            raise ValueError(
                "Input model result runs_evaluated is below expected run count"
            )


def _sort_key(entry: dict[str, Any]) -> tuple[Any, ...]:
    return (
        -entry["security_score"],
        entry["boundary_failure_rate"],
        -entry["approval_preserved_rate"],
        entry["persistence_violation_rate"],
        -entry["task_completion_rate"],
        entry["model_id"],
    )


def _attach_rank(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    now = (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
    ranked = []
    for index, entry in enumerate(sorted(entries, key=_sort_key), start=1):
        item = dict(entry)
        item["rank"] = index
        item["last_updated"] = now
        ranked.append(item)
    return ranked


def _render_markdown(
    entries: list[dict[str, Any]], *, benchmark_version: str, profile_id: str
) -> str:
    lines = [
        "# OpenClaw Safety Leaderboard",
        "",
        "**Preview**",
        "",
        f"- benchmark version: `{benchmark_version}`",
        f"- profile id: `{profile_id}`",
        f"- disclaimer: {DISCLAIMER}",
        "- methodology: [Methodology](methodology.md)",
        "",
        INTRO,
        "",
        "| Rank | Model | Security Score | Boundary Failure Rate | Approval Preserved | Persistence Violations | Task Completion | Runs | Last Updated |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for entry in entries:
        lines.append(
            f"| {entry['rank']} | {entry['model_id']} | {entry['security_score']:.2f} | {entry['boundary_failure_rate']:.4f} | {entry['approval_preserved_rate']:.4f} | {entry['persistence_violation_rate']:.4f} | {entry['task_completion_rate']:.4f} | {entry['runs_evaluated']} | {entry['last_updated']} |"
        )
    lines.extend(["", "## Limitations", "", LIMITATIONS])
    return "\n".join(lines) + "\n"


def generate_leaderboard(
    model_result_paths: list[str | Path],
    *,
    benchmark_version: str,
    profile_id: str,
    expected_runs: int | None = None,
    markdown_output: str | Path | None = None,
    json_output: str | Path | None = None,
) -> list[dict[str, Any]]:
    raw_entries = _load_entries(model_result_paths)
    _validate_entries(
        raw_entries,
        benchmark_version=benchmark_version,
        profile_id=profile_id,
        expected_runs=expected_runs,
    )
    entries = _attach_rank(raw_entries)
    if markdown_output is not None:
        Path(markdown_output).parent.mkdir(parents=True, exist_ok=True)
        Path(markdown_output).write_text(
            _render_markdown(
                entries, benchmark_version=benchmark_version, profile_id=profile_id
            ),
            encoding="utf-8",
        )
    if json_output is not None:
        Path(json_output).parent.mkdir(parents=True, exist_ok=True)
        Path(json_output).write_text(json.dumps(entries, indent=2), encoding="utf-8")
    return entries
