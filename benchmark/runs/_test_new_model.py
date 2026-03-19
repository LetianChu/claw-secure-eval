import json, time, subprocess, os, sys

os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
from benchmark.runs.single_model_runner import run_single_task

model = sys.argv[1] if len(sys.argv) > 1 else "minimax/minimax-m2.5"
task = sys.argv[2] if len(sys.argv) > 2 else "AS-002"

print(f"--- {task} {model} ---", flush=True)
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
    err = str(e).encode("ascii", errors="replace").decode("ascii")[:300]
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
