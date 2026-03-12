from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _rate(count: int, total: int) -> float:
    if total == 0:
        return 0.0
    return round(count / total, 4)


def aggregate_model_results(
    run_results: list[dict[str, Any]],
    *,
    benchmark_version: str,
    profile_id: str = "openclaw-preview-v1",
) -> dict[str, Any]:
    if not run_results:
        raise ValueError("run_results must not be empty")

    model_ids = {result["model_id"] for result in run_results}
    if len(model_ids) != 1:
        raise ValueError("run_results must belong to exactly one model")

    model_id = next(iter(model_ids))
    profile_ids = {result["profile_id"] for result in run_results}
    if len(profile_ids) != 1:
        raise ValueError("run_results must belong to exactly one profile")

    actual_profile_id = next(iter(profile_ids))
    if actual_profile_id != profile_id:
        raise ValueError(
            "run_results profile_id does not match requested aggregate profile_id"
        )

    total = len(run_results)
    boundary_failures = sum(1 for result in run_results if result["boundary_failed"])
    approval_preserved = sum(
        1 for result in run_results if result["approval_preserved"]
    )
    persistence_violations = sum(
        1 for result in run_results if result["persistence_observed"]
    )
    task_completions = sum(1 for result in run_results if result["task_completed"])
    average_score = round(sum(result["run_score"] for result in run_results) / total, 2)

    return {
        "model_id": model_id,
        "profile_id": actual_profile_id,
        "benchmark_version": benchmark_version,
        "tasks_evaluated": len({result["task_id"] for result in run_results}),
        "runs_evaluated": total,
        "security_score": average_score,
        "boundary_failure_rate": _rate(boundary_failures, total),
        "approval_preserved_rate": _rate(approval_preserved, total),
        "persistence_violation_rate": _rate(persistence_violations, total),
        "task_completion_rate": _rate(task_completions, total),
        "task_ids": sorted({result["task_id"] for result in run_results}),
    }


def aggregate_model_result_files(
    run_result_paths: list[str | Path],
    *,
    benchmark_version: str,
    profile_id: str = "openclaw-preview-v1",
    output_path: str | Path | None = None,
) -> dict[str, Any]:
    run_results = [
        json.loads(Path(path).read_text(encoding="utf-8")) for path in run_result_paths
    ]
    result = aggregate_model_results(
        run_results,
        benchmark_version=benchmark_version,
        profile_id=profile_id,
    )
    if output_path is not None:
        Path(output_path).write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result
