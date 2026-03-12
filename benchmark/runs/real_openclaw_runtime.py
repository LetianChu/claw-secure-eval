from __future__ import annotations

import shlex
from pathlib import Path, PurePosixPath


def _wsl_bash(distro: str, inner_command: str) -> str:
    return f"wsl -d {distro} -- bash -lc {shlex.quote(inner_command)}"


def _model_slug(model_id: str) -> str:
    return model_id.replace("/", "__")


def build_health_command(*, distro: str, repo_dir: str = "~/openclaw") -> str:
    inner = (
        f"cd {repo_dir} && "
        "docker compose exec -T openclaw-gateway "
        "curl -fsS http://127.0.0.1:18789/healthz"
    )
    return _wsl_bash(distro, inner)


def build_agent_command(
    *,
    distro: str,
    message: str,
    agent_id: str = "main",
    repo_dir: str = "~/openclaw",
) -> str:
    escaped_message = message.replace('"', '\\"')
    inner = (
        f"cd {repo_dir} && "
        "docker compose run -T --rm openclaw-cli agent "
        f'--agent "{agent_id}" --message "{escaped_message}" --json'
    )
    return _wsl_bash(distro, inner)


def expected_trace_path(
    *,
    traces_root: str | Path,
    benchmark_version: str,
    model_id: str,
    task_id: str,
    run_id: str,
) -> PurePosixPath:
    return (
        PurePosixPath(str(traces_root))
        / benchmark_version
        / _model_slug(model_id)
        / task_id
        / f"{run_id}.json"
    )
