from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from evaluator.evaluate_model import aggregate_model_result_files
from evaluator.evaluate_run import evaluate_trace_file
from leaderboard.generate_leaderboard import generate_leaderboard


def _slugify_model_id(model_id: str) -> str:
    return model_id.replace("/", "__")


def load_run_matrix(matrix_path: str | Path) -> dict[str, Any]:
    return yaml.safe_load(Path(matrix_path).read_text(encoding="utf-8"))


def expected_runs_per_model(matrix: dict[str, Any]) -> int:
    return len(matrix["tasks"]) * int(matrix["runs_per_task"])


def evaluate_matrix_artifacts(
    matrix_path: str | Path,
    *,
    traces_root: str | Path,
    results_root: str | Path,
    leaderboard_markdown: str | Path,
    leaderboard_json: str | Path,
) -> dict[str, Any]:
    matrix = load_run_matrix(matrix_path)
    traces_root = Path(traces_root)
    results_root = Path(results_root)
    benchmark_version = matrix["benchmark_version"]
    profile_id = matrix["profile_id"]
    tasks = matrix["tasks"]

    model_result_paths: list[Path] = []
    completed_models: list[str] = []
    incomplete_models: list[str] = []

    for model in matrix["models"]:
        model_id = model["model_id"]
        model_slug = _slugify_model_id(model_id)
        run_result_paths: list[Path] = []

        for task_id in tasks:
            task_trace_dir = traces_root / benchmark_version / model_slug / task_id
            if not task_trace_dir.exists():
                continue

            for trace_path in sorted(task_trace_dir.glob("*.json")):
                run_output_dir = (
                    results_root
                    / "run-results"
                    / benchmark_version
                    / model_slug
                    / task_id
                )
                run_output_dir.mkdir(parents=True, exist_ok=True)
                run_result_path = run_output_dir / f"{trace_path.stem}.json"
                evaluate_trace_file(
                    trace_path,
                    task_id=task_id,
                    model_id=model_id,
                    profile_id=profile_id,
                    output_path=run_result_path,
                )
                run_result_paths.append(run_result_path)

        expected = expected_runs_per_model(matrix)
        if len(run_result_paths) < expected:
            incomplete_models.append(model_id)
            continue

        model_output_dir = results_root / "model-results" / benchmark_version
        model_output_dir.mkdir(parents=True, exist_ok=True)
        model_result_path = model_output_dir / f"{model_slug}.json"
        aggregate_model_result_files(
            run_result_paths,
            benchmark_version=benchmark_version,
            profile_id=profile_id,
            output_path=model_result_path,
        )
        model_result_paths.append(model_result_path)
        completed_models.append(model_id)

    leaderboard_entries: list[dict[str, Any]] = []
    if model_result_paths:
        leaderboard_entries = generate_leaderboard(
            model_result_paths,
            benchmark_version=benchmark_version,
            profile_id=profile_id,
            expected_runs=expected_runs_per_model(matrix),
            markdown_output=leaderboard_markdown,
            json_output=leaderboard_json,
        )
    else:
        Path(leaderboard_markdown).parent.mkdir(parents=True, exist_ok=True)
        Path(leaderboard_markdown).write_text(
            "# OpenClaw Safety Leaderboard\n\nNo complete model results are available yet.\n",
            encoding="utf-8",
        )
        Path(leaderboard_json).write_text("[]", encoding="utf-8")

    summary = {
        "benchmark_version": benchmark_version,
        "profile_id": profile_id,
        "completed_models": completed_models,
        "incomplete_models": incomplete_models,
        "leaderboard_entries": leaderboard_entries,
    }
    summary_path = results_root / "summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary
