"""Replay only the inspected CFMZ26 v1 complete P1 lower certificate.

The original source code and witnesses stay in the registered local literature
archive. This runner records their mathematical verification result; it does not
claim an independent implementation of the source algorithm.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import runpy
import sys
import tempfile
import zipfile


GROUP = Path(__file__).resolve().parent
ROOT = GROUP.parents[3]
SOURCE = ROOT / "mathematics/literature/pdf/CFMZ26/Quartic-Salem-Verification-v1.0.zip"
OUTPUT = ROOT / "mathematics/computations/outputs" / GROUP.name / "cfmz26_p1_lower.json"
PREFIX = "Quartic-Salem-Verification-v1.0/verification/"
FILES = {
    "lower_math.py": 3105,
    "verify_lower.py": 7955,
    "lower_p1/states.bin": 3641096,
    "lower_p1/W.bin": 7282192,
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    output = args.output.resolve()
    expected_home = (ROOT / "mathematics/computations/outputs" / GROUP.name).resolve()
    require(output.parent == expected_home, "Output must remain in this J output home")
    output.parent.mkdir(parents=True, exist_ok=True)
    require(SOURCE.is_file(), "Required registered source archive is absent")
    require(SOURCE.stat().st_size <= 25_000_000, "Unexpected source archive size")
    print("Checking the fixed P1 certificate: 455137 rows, height 180, t=68883/40000", flush=True)
    with tempfile.TemporaryDirectory(prefix="source-", dir=output.parent) as temporary:
        extraction = Path(temporary).resolve()
        require(extraction.parent == expected_home, "Unexpected extraction location")
        with zipfile.ZipFile(SOURCE) as archive:
            for name, size in FILES.items():
                data = archive.read(PREFIX + name)
                require(len(data) == size, "Unexpected selected resource length: " + name)
                destination = extraction / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(data)
        sys.path.insert(0, str(extraction))
        try:
            source = runpy.run_path(str(extraction / "verify_lower.py"), run_name="cfmz26_source_lower")
            # All mathematical row, closure, root, strip and logarithm checks run.
            # Metadata digests are not used as a mathematical acceptance gate.
            report = source["verify_case"](1, extraction, check_metadata=False)
        finally:
            sys.path.pop(0)
            sys.modules.pop("lower_math", None)
    require(report["status"] == "PASS" and report["parameter"] == "P1", "Wrong source result")
    require(report["H"] == 180 and report["state_count"] == 455137, "Changed finite scope")
    require(report["tilt"] == "68883/40000", "Changed tilt")
    require(report["source_W0"] == "181660711014187729550784", "Initial value disagrees with C.2")
    require(report["min_row_margin"] == "2791379258189148576", "Minimum margin disagrees with C.2")
    require(report["boundary_diagnostics"]["unresolved_nonconstant"] == 0, "Unresolved strip state")
    report.pop("static_files", None)
    report.pop("seconds", None)
    report["source"] = {
        "work": "CFMZ26",
        "edition": "arXiv:2610.09902v1; Zenodo verification release 1.0",
        "archive": "mathematics/literature/pdf/CFMZ26/Quartic-Salem-Verification-v1.0.zip",
        "selected_members": [PREFIX + name for name in FILES],
    }
    report["inspection"] = {
        "algorithm": "Inspected unchanged source verify_case(1), not an independent implementation",
        "source_metadata_digest_gate": False,
        "scope": "Complete P1 finite lower supersolution only; no P2, upper suite or critical mean",
    }
    temporary_output = output.with_suffix(output.suffix + ".partial")
    temporary_output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary_output, output)
    print("PASS: all 455137 rows; U(68883/40000)<105; minimum margin=" + report["min_row_margin"], flush=True)
    print("Result: " + str(output), flush=True)


if __name__ == "__main__":
    main()
