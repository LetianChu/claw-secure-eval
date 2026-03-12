from benchmark.runs.resource_budget_trace import resource_run_to_trace


def test_resource_run_to_trace_marks_budget_exhausted_on_timeout():
    trace = resource_run_to_trace(
        timed_out=True,
        timeout_seconds=8,
        reason="rb001-proof-loop",
    )

    assert trace == [
        {
            "timestamp": "timeout",
            "event_type": "budget_exhausted",
            "approved": False,
            "metadata": {
                "reason": "rb001-proof-loop",
                "timeout_seconds": 8,
            },
        }
    ]


def test_resource_run_to_trace_returns_empty_trace_when_run_completes():
    trace = resource_run_to_trace(
        timed_out=False, timeout_seconds=8, reason="rb001-proof-loop"
    )
    assert trace == []
