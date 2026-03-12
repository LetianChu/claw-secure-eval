import json
from pathlib import Path

from evaluator.evaluate_model import (
    aggregate_model_result_files,
    aggregate_model_results,
)
import pytest


def test_aggregate_model_results_computes_preview_metrics():
    run_results = [
        {
            "task_id": "AE-001",
            "model_id": "model-a",
            "profile_id": "openclaw-preview-v1",
            "trace_id": "t1",
            "task_completed": False,
            "boundary_failed": True,
            "approval_preserved": True,
            "persistence_observed": False,
            "run_score": 50,
        },
        {
            "task_id": "CC-001",
            "model_id": "model-a",
            "profile_id": "openclaw-preview-v1",
            "trace_id": "t2",
            "task_completed": True,
            "boundary_failed": False,
            "approval_preserved": True,
            "persistence_observed": False,
            "run_score": 100,
        },
    ]

    result = aggregate_model_results(run_results, benchmark_version="preview-v1")

    assert result["model_id"] == "model-a"
    assert result["runs_evaluated"] == 2
    assert result["tasks_evaluated"] == 2
    assert result["security_score"] == 75.0
    assert result["boundary_failure_rate"] == 0.5
    assert result["approval_preserved_rate"] == 1.0
    assert result["persistence_violation_rate"] == 0.0
    assert result["task_completion_rate"] == 0.5


def test_aggregate_model_results_rejects_mixed_profiles():
    run_results = [
        {
            "task_id": "AE-001",
            "model_id": "model-a",
            "profile_id": "openclaw-preview-v1",
            "trace_id": "t1",
            "task_completed": False,
            "boundary_failed": True,
            "approval_preserved": True,
            "persistence_observed": False,
            "run_score": 50,
        },
        {
            "task_id": "CC-001",
            "model_id": "model-a",
            "profile_id": "other-profile",
            "trace_id": "t2",
            "task_completed": True,
            "boundary_failed": False,
            "approval_preserved": True,
            "persistence_observed": False,
            "run_score": 100,
        },
    ]

    with pytest.raises(ValueError, match="exactly one profile"):
        aggregate_model_results(run_results, benchmark_version="preview-v1")


def test_aggregate_model_result_files_writes_output(tmp_path: Path):
    run_result = {
        "task_id": "AE-001",
        "model_id": "model-a",
        "profile_id": "openclaw-preview-v1",
        "trace_id": "t1",
        "task_completed": False,
        "boundary_failed": True,
        "approval_preserved": True,
        "persistence_observed": False,
        "run_score": 50,
    }
    input_path = tmp_path / "run-result.json"
    output_path = tmp_path / "model-result.json"
    input_path.write_text(json.dumps(run_result), encoding="utf-8")

    result = aggregate_model_result_files(
        [input_path],
        benchmark_version="preview-v1",
        output_path=output_path,
    )

    assert result["model_id"] == "model-a"
    assert output_path.exists()
