"""Complete-measure tests of fixed Gaussian one-kick cyclic norms."""

import argparse
import importlib.util
import json
from pathlib import Path
import platform
import time

import flint
from flint import fmpz_poly


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
SOURCE = HERE.parent / "Yin_J_G0156" / "sampler.py"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boundary", action="store_true",
                        help="m=1,...,4 and b=0,...,m+2, the exact small-degree range")
    args = parser.parse_args()
    started = time.monotonic()
    specification = importlib.util.spec_from_file_location("j156_measure", SOURCE)
    evaluator = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(evaluator)
    z = fmpz_poly([0, 1])
    records = []
    parameters = ([(m, b) for m in range(1, 5) for b in range(m + 3)]
                  if args.boundary else [(m, 1) for m in range(1, 13)])
    for m, b in parameters:
        real = (z ** m - 1) * (z ** 2 + z - 1) + 2 * z
        imaginary = -b * z * (z ** m - 1)
        polynomial = real ** 2 + imaginary ** 2
        coefficients = [int(c) for c in polynomial.coeffs()]
        assert polynomial.degree() == 2 * m + 4
        assert coefficients[0] == coefficients[-1] == 1
        assert coefficients == coefficients[::-1]
        if m == 1 and b == 1:
            assert polynomial == (z ** 2 + 1) * (z ** 4 + 1)
        certificate = evaluator.certify_polynomial(coefficients)
        records.append({
            "m": m,
            "b": b,
            "gaussian_real_coefficients_ascending": [int(c) for c in real.coeffs()],
            "gaussian_imaginary_coefficients_ascending": [int(c) for c in imaginary.coeffs()],
            "certificate": certificate,
        })
    assert len(records) == (22 if args.boundary else 12)
    summary = [{
        "m": row["m"],
        "b": row["b"],
        "degree": len(row["certificate"]["coefficients_ascending"]) - 1,
        "neutral": row["certificate"]["neutral"],
        "whole_measure_ball": row["certificate"]["measure_ball"],
        "target_6_5": row["certificate"]["thresholds"]["6/5"],
        "factor_degrees": [[factor["degree"], factor["exponent"]]
                           for factor in row["certificate"]["factors"]],
    } for row in records]
    result = {
        "python_version": platform.python_version(),
        "python_flint_version": flint.__version__,
        "parameters": parameters,
        "arithmetic": "exact integer norm and factorization, 128-bit Arb complete measure",
        "records": records,
        "summary": summary,
        "elapsed_seconds": time.monotonic() - started,
        "scope": ("Twenty-two exact small-degree inputs" if args.boundary
                  else "Twelve complete norm polynomials; no asymptotic conclusion"),
    }
    destination = OUTPUT / ("boundary.json" if args.boundary else "one_kick.json")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    temporary.replace(destination)
    print(json.dumps(summary, indent=2))
    print(json.dumps({"elapsed_seconds": result["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
