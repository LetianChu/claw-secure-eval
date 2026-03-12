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


def test_transcript_jsonl_to_trace_parses_real_ae001_transcript_artifact():
    transcript = Path(
        "benchmark/live-output/preview-v1/moonshot__kimi-k2.5/AE-001/real-smoke-1.transcript.jsonl"
    )

    trace = transcript_jsonl_to_trace(transcript)

    assert len(trace) >= 1
    assert all(event["event_type"] == "file_read" for event in trace)
    assert any(event["path"].startswith("/home/node/") for event in trace)
