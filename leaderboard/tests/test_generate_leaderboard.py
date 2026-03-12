import json
from pathlib import Path

from leaderboard.generate_leaderboard import generate_leaderboard


def test_generate_leaderboard_sorts_rows_and_writes_outputs(tmp_path: Path):
    input_dir = tmp_path / "model-results"
    input_dir.mkdir()

    rows = [
        {
            "model_id": "model-b",
            "profile_id": "openclaw-preview-v1",
            "benchmark_version": "preview-v1",
            "tasks_evaluated": 6,
            "runs_evaluated": 18,
            "security_score": 72.0,
            "boundary_failure_rate": 0.3,
            "approval_preserved_rate": 0.8,
            "persistence_violation_rate": 0.2,
            "task_completion_rate": 0.5,
            "task_ids": ["AE-001"],
        },
        {
            "model_id": "model-a",
            "profile_id": "openclaw-preview-v1",
            "benchmark_version": "preview-v1",
            "tasks_evaluated": 6,
            "runs_evaluated": 18,
            "security_score": 88.0,
            "boundary_failure_rate": 0.1,
            "approval_preserved_rate": 0.9,
            "persistence_violation_rate": 0.0,
            "task_completion_rate": 0.7,
            "task_ids": ["AE-001"],
        },
    ]

    paths = []
    for idx, row in enumerate(rows, start=1):
        path = input_dir / f"model-{idx}.json"
        path.write_text(json.dumps(row), encoding="utf-8")
        paths.append(path)

    markdown_output = tmp_path / "leaderboard.md"
    json_output = tmp_path / "leaderboard.json"

    result = generate_leaderboard(
        paths,
        benchmark_version="preview-v1",
        profile_id="openclaw-preview-v1",
        markdown_output=markdown_output,
        json_output=json_output,
    )

    assert result[0]["rank"] == 1
    assert result[0]["model_id"] == "model-a"
    assert result[1]["rank"] == 2
    assert markdown_output.exists()
    assert json_output.exists()


def test_generate_leaderboard_uses_deterministic_tiebreaks(tmp_path: Path):
    rows = [
        {
            "model_id": "z-model",
            "profile_id": "openclaw-preview-v1",
            "benchmark_version": "preview-v1",
            "tasks_evaluated": 6,
            "runs_evaluated": 18,
            "security_score": 80.0,
            "boundary_failure_rate": 0.2,
            "approval_preserved_rate": 0.9,
            "persistence_violation_rate": 0.1,
            "task_completion_rate": 0.6,
            "task_ids": ["AE-001"],
        },
        {
            "model_id": "a-model",
            "profile_id": "openclaw-preview-v1",
            "benchmark_version": "preview-v1",
            "tasks_evaluated": 6,
            "runs_evaluated": 18,
            "security_score": 80.0,
            "boundary_failure_rate": 0.2,
            "approval_preserved_rate": 0.9,
            "persistence_violation_rate": 0.1,
            "task_completion_rate": 0.6,
            "task_ids": ["AE-001"],
        },
    ]

    paths = []
    for idx, row in enumerate(rows, start=1):
        path = tmp_path / f"model-{idx}.json"
        path.write_text(json.dumps(row), encoding="utf-8")
        paths.append(path)

    result = generate_leaderboard(
        paths, benchmark_version="preview-v1", profile_id="openclaw-preview-v1"
    )
    assert result[0]["model_id"] == "a-model"
    assert result[1]["model_id"] == "z-model"


def test_generate_leaderboard_includes_disclaimer_and_config(tmp_path: Path):
    row = {
        "model_id": "model-a",
        "profile_id": "openclaw-preview-v1",
        "benchmark_version": "preview-v1",
        "tasks_evaluated": 6,
        "runs_evaluated": 18,
        "security_score": 88.0,
        "boundary_failure_rate": 0.1,
        "approval_preserved_rate": 0.9,
        "persistence_violation_rate": 0.0,
        "task_completion_rate": 0.7,
        "task_ids": ["AE-001"],
    }
    input_path = tmp_path / "model.json"
    input_path.write_text(json.dumps(row), encoding="utf-8")
    markdown_output = tmp_path / "leaderboard.md"

    generate_leaderboard(
        [input_path],
        benchmark_version="preview-v1",
        profile_id="openclaw-preview-v1",
        markdown_output=markdown_output,
    )

    content = markdown_output.read_text(encoding="utf-8")
    assert "Preview" in content
    assert "openclaw-preview-v1" in content
    assert "results do not imply universal model safety rankings" in content
    assert "methodology.md" in content


def test_generate_leaderboard_rejects_mixed_benchmark_metadata(tmp_path: Path):
    row = {
        "model_id": "model-a",
        "profile_id": "wrong-profile",
        "benchmark_version": "preview-v1",
        "tasks_evaluated": 6,
        "runs_evaluated": 18,
        "security_score": 88.0,
        "boundary_failure_rate": 0.1,
        "approval_preserved_rate": 0.9,
        "persistence_violation_rate": 0.0,
        "task_completion_rate": 0.7,
        "task_ids": ["AE-001"],
    }
    input_path = tmp_path / "model.json"
    input_path.write_text(json.dumps(row), encoding="utf-8")

    import pytest

    with pytest.raises(ValueError, match="profile_id"):
        generate_leaderboard(
            [input_path],
            benchmark_version="preview-v1",
            profile_id="openclaw-preview-v1",
        )


def test_generate_leaderboard_rejects_incomplete_run_counts(tmp_path: Path):
    row = {
        "model_id": "model-a",
        "profile_id": "openclaw-preview-v1",
        "benchmark_version": "preview-v1",
        "tasks_evaluated": 6,
        "runs_evaluated": 6,
        "security_score": 88.0,
        "boundary_failure_rate": 0.1,
        "approval_preserved_rate": 0.9,
        "persistence_violation_rate": 0.0,
        "task_completion_rate": 0.7,
        "task_ids": ["AE-001"],
    }
    input_path = tmp_path / "model.json"
    input_path.write_text(json.dumps(row), encoding="utf-8")

    import pytest

    with pytest.raises(ValueError, match="runs_evaluated"):
        generate_leaderboard(
            [input_path],
            benchmark_version="preview-v1",
            profile_id="openclaw-preview-v1",
            expected_runs=18,
        )
