"""The one declared J87 invocation: fixed scope, 180-second aggregate cap, no retry."""

import json
import os
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
    if len(sys.argv) != 1:
        raise SystemExit("No scope or tuning arguments are supported")
    started = perf_counter()
    try:
        # The worker checks this same starting clock; the subprocess timeout also
        # bounds a blocked worker. There is exactly one child and no retry loop.
        result = subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str((_J_PROGRAM / 'worker.py')),
             repr(started)], timeout=max(0.001, 180 - (perf_counter() - started)),
            check=False)
        returncode = result.returncode
    except subprocess.TimeoutExpired:
        returncode = 124
    raise SystemExit(returncode)


if __name__ == "__main__":
    main()
