"""Bounded exact factorization of the whole N=1155 central-minus-one quotient.

This is a separate follow-up to the root-shape calculation.  It asks whether
individual rational factors require a separate small-measure investigation.
The child process is bounded; a timeout supplies no factorization conclusion.
"""

import argparse
import importlib.util
import json
from pathlib import Path
import platform
import subprocess
import sys
import time


def factor(measure=False):
    import flint
    from flint import fmpz_poly

    started = time.monotonic()
    x = fmpz_poly([0, 1])
    numerator = fmpz_poly.cyclotomic(1155) - x ** 240
    block = fmpz_poly([1])
    for order, power in [(1, 2), (2, 2), (3, 1), (4, 1), (5, 1),
                         (6, 1), (8, 1), (10, 1), (12, 1), (24, 1)]:
        block *= fmpz_poly.cyclotomic(order) ** power
    quotient, remainder = divmod(numerator, block)
    assert not remainder and block * quotient == numerator
    assert quotient.degree() == 446
    content, factors = quotient.factor()
    rebuilt = fmpz_poly([content])
    records = []
    for polynomial, multiplicity in factors:
        rebuilt *= polynomial ** multiplicity
        records.append({
            "degree": int(polynomial.degree()),
            "multiplicity": int(multiplicity),
            "coefficients_ascending": [int(c) for c in polynomial.coeffs()],
        })
    assert rebuilt == quotient
    result = {
        "status": "completed",
        "python_version": platform.python_version(),
        "python_flint_version": flint.__version__,
        "N": 1155,
        "content": int(content),
        "factors": records,
        "elapsed_seconds": time.monotonic() - started,
        "scope": "Exact FLINT factorization; multiplication verified, no Mahler evaluation",
    }
    if measure:
        source = Path(__file__).resolve().parent.parent / "Yin_J_G0156" / "sampler.py"
        specification = importlib.util.spec_from_file_location("j156_measure", source)
        module = importlib.util.module_from_spec(specification)
        specification.loader.exec_module(module)
        result["measure_certificate"] = module.certify_polynomial(
            [int(c) for c in quotient.coeffs()])
        result["elapsed_seconds"] = time.monotonic() - started
        result["scope"] = "Complete factorization and all-root J156 Mahler enclosure"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--measure", action="store_true")
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output is None:
        args.output = (Path(__file__).resolve().parents[2] / "outputs" /
                       "Yin_J_G0138" /
                       ("core_measure.json" if args.measure else "core_factors.json"))
    if args.worker:
        print(json.dumps(factor(args.measure)))
        return
    assert args.timeout > 0
    try:
        command = [sys.executable, "-B", str(Path(__file__).resolve()), "--worker"]
        if args.measure:
            command.append("--measure")
        completed = subprocess.run(
            command,
            capture_output=True, text=True, check=True, timeout=args.timeout,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        output = json.loads(completed.stdout)
    except subprocess.TimeoutExpired:
        output = {"status": "timeout", "timeout_seconds": args.timeout,
                  "N": 1155, "scope": "No factorization conclusion"}
    output["timeout_seconds"] = args.timeout
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    temporary.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    temporary.replace(args.output)
    print(json.dumps({k: v for k, v in output.items()
                      if k not in ("factors", "measure_certificate")}))
    if "factors" in output:
        print(json.dumps([{k: v for k, v in row.items()
                           if k != "coefficients_ascending"}
                          for row in output["factors"]]))
    if "measure_certificate" in output:
        certificate = output["measure_certificate"]
        print(json.dumps({key: certificate[key] for key in (
            "measure_ball", "measure_interval", "root_count_with_multiplicity",
            "thresholds")}))


if __name__ == "__main__":
    main()
