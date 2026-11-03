"""Run one fixed J86 scope in a subprocess with a 30-second hard timeout."""

import argparse
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import subprocess
import sys
from time import perf_counter

GROUP = (_J_PROGRAM / 'main.py').parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("compare", "lehmer1024"), required=True)
    mode = parser.parse_args().mode
    started = perf_counter()
    try:
        result = subprocess.run([sys.executable, "-B", "-X", "utf8", str((_J_PROGRAM / 'worker.py')),
                                 "--mode", mode], cwd=GROUP, timeout=30, check=True,
                                capture_output=True, text=True)
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as failure:
        payload = {'complete': False, 'mode': mode, 'hard_timeout_seconds': 30, 'failure_type': type(failure).__name__, 'detail': str(failure), 'stderr': str(getattr(failure, 'stderr', ''))[-4000:]}
        ((_J_OUTPUT / 'failure.json')).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        raise
    print(result.stdout.strip())
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    print(json.dumps({"supervisor_seconds": perf_counter() - started,
                      "hard_timeout_seconds": 30}))


if __name__ == "__main__":
    main()
