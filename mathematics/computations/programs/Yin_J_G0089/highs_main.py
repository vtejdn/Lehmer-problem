"""Run the declared fixed scope with a live 180-second subprocess limit."""
from pathlib import Path
import subprocess
import sys

PROGRAM = Path(__file__).resolve().parent


def main():
    if len(sys.argv) != 1:
        raise SystemExit("No scope overrides are supported")
    try:
        process = subprocess.run([sys.executable, "-B", "-X", "utf8", str(PROGRAM / 'highs_worker.py')], timeout=180)
    except subprocess.TimeoutExpired:
        print("The declared computation timed out; no complete result is claimed.", file=sys.stderr)
        return 124
    return process.returncode


if __name__ == "__main__":
    raise SystemExit(main())
