from benchmark.runs.real_openclaw_runtime import (
    build_agent_command,
    build_health_command,
    expected_trace_path,
)


def test_build_health_command_targets_wsl_openclaw_gateway():
    command = build_health_command(distro="Ubuntu-24.04")
    assert "wsl -d Ubuntu-24.04 -- bash -lc" in command
    assert (
        "docker compose exec -T openclaw-gateway curl -fsS http://127.0.0.1:18789/healthz"
        in command
    )


def test_build_agent_command_targets_main_agent_and_json_output():
    command = build_agent_command(
        distro="Ubuntu-24.04",
        message="Reply READY",
        agent_id="main",
    )
    assert "docker compose run -T --rm openclaw-cli agent" in command
    assert '--agent "main"' in command
    assert '--message "Reply READY"' in command
    assert "--json" in command


def test_expected_trace_path_uses_model_and_task_structure():
    path = expected_trace_path(
        traces_root="/tmp/traces",
        benchmark_version="preview-v1",
        model_id="anthropic/claude-sonnet-4.5",
        task_id="AE-001",
        run_id="run-1",
    )
    assert (
        str(path)
        == "/tmp/traces/preview-v1/anthropic__claude-sonnet-4.5/AE-001/run-1.json"
    )
