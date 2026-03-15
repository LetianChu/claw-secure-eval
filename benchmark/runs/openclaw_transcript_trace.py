from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def _normalize_command(command: Any) -> str | None:
    if isinstance(command, str):
        return command
    if not isinstance(command, list) or not command:
        return None

    parts = [str(part) for part in command]
    if (
        len(parts) >= 3
        and parts[0] in {"bash", "sh", "/bin/sh"}
        and parts[1]
        in {
            "-c",
            "-lc",
        }
    ):
        return parts[2]
    return " ".join(parts)


_EXPLICIT_READ_PATTERNS = (
    re.compile(r"(?<!\S)cat\s+(?P<path>(?:~|/)[^\s;&|]+)"),
    re.compile(
        r"(?<!\S)sed\s+-n\s+(?:'[^']+'|\"[^\"]+\")\s+(?P<path>(?:~|/)[^\s;&|]+)"
    ),
)


def _extract_file_reads(command: str) -> list[str]:
    matches: list[tuple[int, str]] = []
    for pattern in _EXPLICIT_READ_PATTERNS:
        for match in pattern.finditer(command):
            matches.append((match.start(), match.group("path")))

    reads: list[str] = []
    for _, path in sorted(matches):
        if path not in reads:
            reads.append(path)
    return reads


def _process_events(
    timestamp: str, base: dict[str, Any], command: str | None
) -> list[dict[str, Any]]:
    if command is None:
        return []

    events = [{**base, "event_type": "process_launch", "command": command}]
    for path in _extract_file_reads(command):
        events.append({**base, "event_type": "file_read", "path": path})
    return events


def _map_tool_call(timestamp: str, item: dict[str, Any]) -> list[dict[str, Any]]:
    name = item.get("name")
    arguments = item.get("arguments") or {}
    base = {
        "timestamp": timestamp,
        "approved": False,
        "metadata": {"tool": name, "tool_call_id": item.get("id")},
    }

    if name == "read":
        return [
            {
                **base,
                "event_type": "file_read",
                "path": arguments.get("file_path") or arguments.get("path"),
            }
        ]
    if name in {"write", "edit"}:
        return [
            {
                **base,
                "event_type": "file_write",
                "path": arguments.get("file_path") or arguments.get("path"),
            }
        ]
    if name in {"exec", "process"}:
        return _process_events(
            timestamp, base, _normalize_command(arguments.get("command"))
        )
    return []


def _map_openai_text_payload(timestamp: str, text: Any) -> list[dict[str, Any]]:
    if not isinstance(text, str):
        return []

    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return []

    command = _normalize_command(payload.get("command"))
    if command is None:
        return []

    return _process_events(
        timestamp,
        {
            "timestamp": timestamp,
            "approved": False,
            "metadata": {"tool": "exec", "tool_call_id": None},
        },
        command,
    )


def transcript_jsonl_to_trace(transcript_path: str | Path) -> list[dict[str, Any]]:
    trace: list[dict[str, Any]] = []
    for raw in Path(transcript_path).read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        event = json.loads(raw)
        if event.get("type") != "message":
            continue
        message = event.get("message") or {}
        if message.get("role") != "assistant":
            continue
        timestamp = event.get("timestamp")
        for item in message.get("content", []):
            if item.get("type") == "toolCall":
                trace.extend(_map_tool_call(timestamp, item))
            elif item.get("type") == "text":
                trace.extend(_map_openai_text_payload(timestamp, item.get("text")))
    return trace
