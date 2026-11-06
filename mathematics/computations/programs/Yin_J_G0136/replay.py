"""Replay retained exploratory bodies; this is not an independent verifier."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import platform
import runpy

import numpy


def main():
    group = Path(__file__).resolve().parent
    output = group.parent.parent / "outputs" / group.name
    results = {}
    for name in ("original_p4_pairs.py", "original_small_scan.py"):
        captured = StringIO()
        with redirect_stdout(captured):
            runpy.run_path(str(group / name), run_name="__main__")
        results[name] = captured.getvalue()
    payload = {
        "status": "completed exploratory replay",
        "python": platform.python_version(),
        "numpy": numpy.__version__,
        "arithmetic": {
            "autocorrelations_and_dynamic_program": "exact Python integers",
            "positivity_screen": "NumPy floating Chebyshev roots; uncertified",
            "imaginary_tolerance": 1e-8,
            "positive_minimum_threshold": 1e-8,
        },
        "outputs": results,
        "limits": "No universal SOS theorem, rigorous positivity classification, or independent verification.",
    }
    output.mkdir(parents=True, exist_ok=True)
    path = output / "results.json"
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    for value in results.values():
        print(value, end="")
    print(f"Saved {path}")


if __name__ == "__main__":
    main()
