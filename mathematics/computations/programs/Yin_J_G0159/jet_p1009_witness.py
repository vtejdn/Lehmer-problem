"""Exact last-two-coordinate correction and optimizer-free witness verification.

This checks one rational conductor-1009 jet-branch input, not integer supply.
The LP proposal is optional preparation input; verification uses only the saved
exact rational coefficients and the original prefix-cell interval evaluator.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

from prefix_cell import FIXED, b_zero, b_derivative_zero, endpoint, interval_check

HERE = Path(__file__).resolve().parent
OUT = HERE.parent.parent / "outputs" / HERE.name
INPUT = HERE / "inputs" / "jet_p1009_witness.json"
P, N, L = 1009, 504, 140


def jets(a):
    return (sum(value * b_zero(N - 1 - i) for i, value in enumerate(a)),
            b_zero(N) + sum(value * b_derivative_zero(N - 1 - i)
                            for i, value in enumerate(a)))


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_suffix(path.suffix + ".part")
    pending.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    pending.replace(path)


def verify(data):
    assert (data["p"], data["n"], data["prefix_L"], data["x"], data["kappa"]) == (P, N, L, 0, 1)
    assert (data["Q0"], data["Qprime0"]) == (0, -1)
    a = [Fraction(v) for v in data["coefficients_rational"]]
    assert len(a) == N and a[:139] == FIXED
    assert jets(a) == (0, -1)
    fixed_q0 = sum(value * b_zero(N - 1 - i) for i, value in enumerate(FIXED))
    fixed_qp = b_zero(N) + sum(value * b_derivative_zero(N - 1 - i)
                             for i, value in enumerate(FIXED))
    assert (fixed_q0, fixed_qp) == (2, 365)
    result = interval_check(a, 1)
    assert result["endpoint_positive"] and result["all_strict_signs_certified"]
    result.update({"scope": "one exact rational witness; no integer construction or independent review",
                   "p": P, "n": N, "prefix_L": L, "free_tail_dimension": 365,
                   "jet_branch_dimension": 363, "Q0": "0", "Qprime0": "-1",
                   "fixed_Q0": fixed_q0, "fixed_Qprime0": fixed_qp,
                   "all_coefficients_integer": all(v.denominator == 1 for v in a)})
    return result


def prepare(source):
    if INPUT.exists():
        raise FileExistsError("The selected witness is already retained; use verification instead.")
    lp = json.loads(source.read_text(encoding="utf-8"))
    assert (lp["p"], lp["n"], lp["prefix_L"], lp["x"], lp["kappa"]) == (P, N, L, 0, 1)
    assert lp["requested_Q0"] == 0 and lp["requested_Qprime0"] == -1
    assert lp["solution_value_valid"] and lp["observed_signed_sine_minimum"] > 0
    a = list(map(Fraction, FIXED)) + [Fraction(str(v)) for v in lp["raw_tail"]]
    assert len(a) == N
    q0, qp = jets(a)
    # Index 502 multiplies B1 = t+1; index 503 multiplies B0 = 1.
    delta_b1 = -1 - qp
    delta_b0 = -q0 - delta_b1
    before_endpoint = endpoint(a)
    a[-2] += delta_b1
    a[-1] += delta_b0
    assert jets(a) == (0, -1)
    assert endpoint(a) == before_endpoint + delta_b1 - delta_b0
    data = {"p": P, "n": N, "x": 0, "kappa": 1, "prefix_L": L,
            "Q0": 0, "Qprime0": -1, "free_tail_dimension": 365,
            "jet_branch_dimension": 363,
            "coefficients_rational": [str(v) for v in a],
            "correction": {"original_Q0": str(q0), "original_Qprime0": str(qp),
                           "index_502_B1_increment": str(delta_b1),
                           "index_503_B0_increment": str(delta_b0),
                           "original_endpoint": str(before_endpoint),
                           "corrected_endpoint": str(endpoint(a))}}
    result = verify(data)
    write(INPUT, data)
    write(OUT / "jet_p1009_preparation.json", result)
    print(json.dumps({"saved_witness": str(INPUT), "correction": data["correction"],
                      "strict_signs_certified": result["all_strict_signs_certified"],
                      "all_coefficients_integer": result["all_coefficients_integer"]}))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare-from", type=Path)
    parser.add_argument("--input", type=Path, default=INPUT)
    args = parser.parse_args()
    if args.prepare_from:
        prepare(args.prepare_from)
    else:
        result = verify(json.loads(args.input.read_text(encoding="utf-8")))
        write(OUT / "jet_p1009_verification.json", result)
        print(json.dumps({"p": P, "strict_signs_certified": result["all_strict_signs_certified"],
                          "sign_rows": len(result["sign_rows"]), "Q0": result["Q0"],
                          "Qprime0": result["Qprime0"], "endpoint": result["endpoint"],
                          "all_coefficients_integer": result["all_coefficients_integer"]}))


if __name__ == "__main__":
    main()
