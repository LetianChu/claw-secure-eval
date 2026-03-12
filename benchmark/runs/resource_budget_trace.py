from __future__ import annotations

from typing import Any


def resource_run_to_trace(
    *, timed_out: bool, timeout_seconds: int, reason: str
) -> list[dict[str, Any]]:
    if not timed_out:
        return []

    return [
        {
            "timestamp": "timeout",
            "event_type": "budget_exhausted",
            "approved": False,
            "metadata": {
                "reason": reason,
                "timeout_seconds": timeout_seconds,
            },
        }
    ]
