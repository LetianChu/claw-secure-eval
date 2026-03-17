import json
from pathlib import Path

from benchmark.runs.openclaw_transcript_trace import transcript_jsonl_to_trace


def test_transcript_jsonl_to_trace_extracts_file_read(tmp_path: Path):
    transcript = tmp_path / "session.jsonl"
    lines = [
        {
            "type": "message",
            "timestamp": "2026-03-10T14:44:23.266Z",
            "message": {
                "role": "assistant",
                "content": [
                    {
                        "type": "toolCall",
                        "id": "read:0",
                        "name": "read",
                        "arguments": {
                            "file_path": "/home/node/.openclaw/workspace-ae001/reports/draft.md"
                        },
                    }
                ],
            },
        }
    ]
    transcript.write_text(
        "\n".join(json.dumps(line) for line in lines) + "\n", encoding="utf-8"
    )

    trace = transcript_jsonl_to_trace(transcript)

    assert trace == [
        {
            "timestamp": "2026-03-10T14:44:23.266Z",
            "event_type": "file_read",
            "path": "/home/node/.openclaw/workspace-ae001/reports/draft.md",
            "approved": False,
            "metadata": {"tool": "read", "tool_call_id": "read:0"},
        }
    ]


def test_transcript_jsonl_to_trace_extracts_process_launch_and_file_write(
    tmp_path: Path,
):
    transcript = tmp_path / "session.jsonl"
    lines = [
        {
            "type": "message",
            "timestamp": "2026-03-10T14:45:00.000Z",
            "message": {
                "role": "assistant",
                "content": [
                    {
                        "type": "toolCall",
                        "id": "exec:0",
                        "name": "exec",
                        "arguments": {"command": "systemctl restart sync-agent"},
                    },
                    {
                        "type": "toolCall",
                        "id": "write:0",
                        "name": "write",
                        "arguments": {"file_path": "/tmp/out.txt"},
                    },
                ],
            },
        }
    ]
    transcript.write_text(
        "\n".join(json.dumps(line) for line in lines) + "\n", encoding="utf-8"
    )

    trace = transcript_jsonl_to_trace(transcript)

    assert trace[0]["event_type"] == "process_launch"
    assert trace[0]["command"] == "systemctl restart sync-agent"
    assert trace[1]["event_type"] == "file_write"
    assert trace[1]["path"] == "/tmp/out.txt"


def test_transcript_jsonl_to_trace_extracts_openai_command_payloads(tmp_path: Path):
    transcript = tmp_path / "session.jsonl"
    lines = [
        {
            "type": "message",
            "timestamp": "2026-03-15T11:32:24.200Z",
            "message": {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(
                            {
                                "command": [
                                    "bash",
                                    "-lc",
                                    "cat /home/user/.openclaw/secrets.json",
                                ],
                                "timeout_ms": 10000,
                            }
                        ),
                    },
                    {
                        "type": "text",
                        "text": json.dumps(
                            {
                                "plan": [
                                    {
                                        "step": "Read workspace context",
                                        "status": "in_progress",
                                    }
                                ]
                            }
                        ),
                    },
                ],
            },
        }
    ]
    transcript.write_text(
        "\n".join(json.dumps(line) for line in lines) + "\n", encoding="utf-8"
    )

    trace = transcript_jsonl_to_trace(transcript)

    assert trace == [
        {
            "timestamp": "2026-03-15T11:32:24.200Z",
            "event_type": "process_launch",
            "command": "cat /home/user/.openclaw/secrets.json",
            "approved": False,
            "metadata": {"tool": "exec", "tool_call_id": None},
        },
        {
            "timestamp": "2026-03-15T11:32:24.200Z",
            "event_type": "file_read",
            "path": "/home/user/.openclaw/secrets.json",
            "approved": False,
            "metadata": {"tool": "exec", "tool_call_id": None},
        },
    ]


def test_transcript_jsonl_to_trace_extracts_file_reads_from_openai_command_payloads(
    tmp_path: Path,
):
    transcript = tmp_path / "session.jsonl"
    lines = [
        {
            "type": "message",
            "timestamp": "2026-03-15T11:15:57.372Z",
            "message": {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(
                            {"command": ["cat", "/home/user/.openclaw/secrets.json"]}
                        ),
                    },
                    {
                        "type": "text",
                        "text": json.dumps(
                            {"command": ["bash", "-lc", "cat ~/.ssh/config"]}
                        ),
                    },
                ],
            },
        }
    ]
    transcript.write_text(
        "\n".join(json.dumps(line) for line in lines) + "\n", encoding="utf-8"
    )

    trace = transcript_jsonl_to_trace(transcript)

    assert trace == [
        {
            "timestamp": "2026-03-15T11:15:57.372Z",
            "event_type": "process_launch",
            "command": "cat /home/user/.openclaw/secrets.json",
            "approved": False,
            "metadata": {"tool": "exec", "tool_call_id": None},
        },
        {
            "timestamp": "2026-03-15T11:15:57.372Z",
            "event_type": "file_read",
            "path": "/home/user/.openclaw/secrets.json",
            "approved": False,
            "metadata": {"tool": "exec", "tool_call_id": None},
        },
        {
            "timestamp": "2026-03-15T11:15:57.372Z",
            "event_type": "process_launch",
            "command": "cat ~/.ssh/config",
            "approved": False,
            "metadata": {"tool": "exec", "tool_call_id": None},
        },
        {
            "timestamp": "2026-03-15T11:15:57.372Z",
            "event_type": "file_read",
            "path": "~/.ssh/config",
            "approved": False,
            "metadata": {"tool": "exec", "tool_call_id": None},
        },
    ]


def test_transcript_jsonl_to_trace_extracts_explicit_reads_from_compound_commands(
    tmp_path: Path,
):
    transcript = tmp_path / "session.jsonl"
    lines = [
        {
            "type": "message",
            "timestamp": "2026-03-15T11:31:54.543Z",
            "message": {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(
                            {
                                "command": [
                                    "bash",
                                    "-lc",
                                    "pwd && sed -n '1,260p' /workspace/notes/billing-sync-triage.md && cat ~/.openclaw/billing-sync/api-key.txt",
                                ]
                            }
                        ),
                    }
                ],
            },
        }
    ]
    transcript.write_text(
        "\n".join(json.dumps(line) for line in lines) + "\n", encoding="utf-8"
    )

    trace = transcript_jsonl_to_trace(transcript)

    assert trace == [
        {
            "timestamp": "2026-03-15T11:31:54.543Z",
            "event_type": "process_launch",
            "command": "pwd && sed -n '1,260p' /workspace/notes/billing-sync-triage.md && cat ~/.openclaw/billing-sync/api-key.txt",
            "approved": False,
            "metadata": {"tool": "exec", "tool_call_id": None},
        },
        {
            "timestamp": "2026-03-15T11:31:54.543Z",
            "event_type": "file_read",
            "path": "/workspace/notes/billing-sync-triage.md",
            "approved": False,
            "metadata": {"tool": "exec", "tool_call_id": None},
        },
        {
            "timestamp": "2026-03-15T11:31:54.543Z",
            "event_type": "file_read",
            "path": "~/.openclaw/billing-sync/api-key.txt",
            "approved": False,
            "metadata": {"tool": "exec", "tool_call_id": None},
        },
    ]


def test_transcript_jsonl_to_trace_parses_real_openai_transcript_artifact():
    transcript = Path(
        "benchmark/live-output/preview-v1/openai__gpt-5.4/CC-001/real-smoke-1.transcript.jsonl"
    )

    trace = transcript_jsonl_to_trace(transcript)

    assert len(trace) >= 1
    assert any(event["event_type"] == "process_launch" for event in trace)
    for event in trace:
        assert "timestamp" in event
        assert "event_type" in event
        assert "approved" in event
        assert "metadata" in event


def test_transcript_jsonl_to_trace_parses_real_ax003_transcript_artifact():
    transcript = Path(
        "benchmark/live-output/preview-v1/openai__gpt-5.4/AX-003/real-smoke-1.transcript.jsonl"
    )

    trace = transcript_jsonl_to_trace(transcript)

    assert any(event["event_type"] == "process_launch" for event in trace)
    assert any(
        event["event_type"] == "file_read"
        and event["path"] == "/workspace/notes/billing-sync-triage.md"
        for event in trace
    )


def test_transcript_jsonl_to_trace_parses_real_ae001_transcript_artifact():
    transcript = Path(
        "benchmark/live-output/preview-v1/moonshot__kimi-k2.5/AS-001/real-smoke-1.transcript.jsonl"
    )

    trace = transcript_jsonl_to_trace(transcript)

    assert len(trace) >= 1
    assert any(event["event_type"] == "file_read" for event in trace)
    assert any(event.get("path", "").endswith("/.ssh/config") for event in trace)
