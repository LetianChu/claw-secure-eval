from __future__ import annotations

import json
from pathlib import Path

from benchmark.runs.run_preview_matrix import evaluate_matrix_artifacts


def test_evaluate_matrix_artifacts_builds_leaderboard_from_complete_traces(
    tmp_path: Path,
):
    matrix_path = tmp_path / "matrix.yaml"
    matrix_path.write_text(
        """
benchmark_version: preview-v1
profile_id: openclaw-preview-v1
tasks:
  - AE-001
runs_per_task: 1
models:
  - model_id: provider/model-a
    provider: provider
    version_pin: model-a
    status: stable
""".strip(),
        encoding="utf-8",
    )

    trace_dir = tmp_path / "traces" / "preview-v1" / "provider__model-a" / "AE-001"
    trace_dir.mkdir(parents=True)
    (trace_dir / "run-1.json").write_text(
        json.dumps([]),
        encoding="utf-8",
    )

    results_root = tmp_path / "results"
    leaderboard_md = tmp_path / "leaderboard" / "preview-leaderboard.md"
    leaderboard_json = tmp_path / "leaderboard" / "preview-leaderboard.json"

    summary = evaluate_matrix_artifacts(
        matrix_path,
        traces_root=tmp_path / "traces",
        results_root=results_root,
        leaderboard_markdown=leaderboard_md,
        leaderboard_json=leaderboard_json,
    )

    assert summary["completed_models"] == ["provider/model-a"]
    assert summary["incomplete_models"] == []
    assert leaderboard_md.exists()
    assert leaderboard_json.exists()


def test_evaluate_matrix_artifacts_marks_incomplete_models(tmp_path: Path):
    matrix_path = tmp_path / "matrix.yaml"
    matrix_path.write_text(
        """
benchmark_version: preview-v1
profile_id: openclaw-preview-v1
tasks:
  - AE-001
  - AE-002
runs_per_task: 1
models:
  - model_id: provider/model-a
    provider: provider
    version_pin: model-a
    status: stable
""".strip(),
        encoding="utf-8",
    )

    trace_dir = tmp_path / "traces" / "preview-v1" / "provider__model-a" / "AE-001"
    trace_dir.mkdir(parents=True)
    (trace_dir / "run-1.json").write_text(json.dumps([]), encoding="utf-8")

    summary = evaluate_matrix_artifacts(
        matrix_path,
        traces_root=tmp_path / "traces",
        results_root=tmp_path / "results",
        leaderboard_markdown=tmp_path / "leaderboard" / "preview-leaderboard.md",
        leaderboard_json=tmp_path / "leaderboard" / "preview-leaderboard.json",
    )

    assert summary["completed_models"] == []
    assert summary["incomplete_models"] == ["provider/model-a"]
