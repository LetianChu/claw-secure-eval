import json, time, subprocess, os, sys

os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
from benchmark.runs.single_model_runner import run_single_task

model = sys.argv[1]
tasks = [
    "AE-001",
    "AE-002",
    "AE-003",
    "AS-001",
    "AS-002",
    "AS-003",
    "AX-001",
    "AX-003",
    "CC-001",
    "CC-002",
    "CD-001",
    "CD-002",
    "PF-001",
    "PF-002",
    "RB-001",
]

for task in tasks:
    print(f"--- {task} ---", flush=True)
    t0 = time.time()
    try:
        result = run_single_task(f"benchmark/tasks/{task}.yaml", model_id=model)
        elapsed = time.time() - t0
        rr = json.load(open(result["run_result_path"], encoding="utf-8"))
        print(
            f"  OK: score={rr['run_score']} bf={rr['boundary_failed']} tc={rr['task_completed']} time={elapsed:.0f}s",
            flush=True,
        )
    except Exception as e:
        elapsed = time.time() - t0
        err = str(e).encode("ascii", errors="replace").decode("ascii")[:200]
        print(f"  FAIL ({elapsed:.0f}s): {err}", flush=True)
    subprocess.run(
        [
            "wsl",
            "-d",
            "Ubuntu-24.04",
            "bash",
            "-c",
            "docker ps --filter name=openclaw-openclaw-cli-run -q | xargs -r docker rm -f 2>/dev/null",
        ],
        capture_output=True,
        timeout=15,
    )
