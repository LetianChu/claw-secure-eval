from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _map_tool_call(timestamp: str, item: dict[str, Any]) -> dict[str, Any] | None:
    name = item.get("name")
    arguments = item.get("arguments") or {}
    base = {
        "timestamp": timestamp,
        "approved": False,
        "metadata": {"tool": name, "tool_call_id": item.get("id")},
    }

    if name == "read":
        return {
            **base,
            "event_type": "file_read",
            "path": arguments.get("file_path") or arguments.get("path"),
        }
    if name in {"write", "edit"}:
        return {
            **base,
            "event_type": "file_write",
            "path": arguments.get("file_path") or arguments.get("path"),
        }
    if name in {"exec", "process"}:
        return {
            **base,
            "event_type": "process_launch",
            "command": arguments.get("command"),
        }
    return None


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
            if item.get("type") != "toolCall":
                continue
            mapped = _map_tool_call(timestamp, item)
            if mapped is not None:
                trace.append(mapped)
    return trace
