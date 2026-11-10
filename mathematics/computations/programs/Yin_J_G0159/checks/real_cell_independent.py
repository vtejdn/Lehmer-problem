"""Independent finite evidence checks for J159's fixed real p2003 witness.

Run with Python 3.14 from the repository root:
    python -B mathematics/computations/programs/Yin_J_G0159/checks/real_cell_independent.py
The only external package is python-flint, defaulting to the explicitly named J156 output package directory.
An alternative existing installation may be selected with --flint-path.
All selected author inputs and outputs are read, but no author module, optimizer or J156 evaluator is imported or executed.

The full reciprocal polynomial is assembled from shifted geometric blocks, not by the author's cumulative-division routine.
The two trace jets use the value and derivative recurrence for E and B at zero.
At every grid point, 2048-bit Arb Clenshaw recurrence evaluates the rational E-basis polynomial directly.
Multiplication by a separately enclosed positive sine allows comparison with the author's sine-sum balls.
These enclosures certify the fixed rational witness and the conductor-nine control, not an integer completion or nonneutrality.

Separate floating checks compare every stored model coefficient with its defining sine, and reconstruct the recorded objective observations.
These comparisons do not validate LP optima or prove MIP infeasibility.
The two recorded integer searches are not rerun.
Default output: outputs/Yin_J_G0159/real_cell_independent.json.
"""

import argparse
from fractions import Fraction
import json
import math
from math import gcd, lcm
from pathlib import Path
import re
import sys


J_HOME = Path(__file__).resolve().parents[1]
OUT_HOME = J_HOME.parent.parent / "outputs" / J_HOME.name
INPUT = J_HOME / "inputs" / "real_p2003_coefficients.json"
DEFAULT_FLINT = J_HOME.parent.parent / "outputs" / "Yin_J_G0156" / "packages"
L = 140
FIXED = [2 if i == 0 else 4 if i % 2 == 0 else 0 for i in range(L - 1)]
RUN_FILES = [
    "prefix_cell_lp.json", "prefix_cell_lp_p2003.json",
    "prefix_cell_integer_p2003.json", "prefix_cell_integer_p2003_Q0_0_Qp_neg1.json",
    "prefix_cell_lp_p2003_q0-min.json", "prefix_cell_lp_p2003_q0-max.json",
    "prefix_cell_lp_p2003_qprime-min.json", "prefix_cell_lp_p2003_qprime-max.json",
]


def load(name):
    return json.loads((OUT_HOME / name).read_text(encoding="utf-8"))


def zero_jets(n):
    # E_(j+1)(0)=-E_(j-1)(0), E'_(j+1)(0)=E_j(0)-E'_(j-1)(0).
    previous, current, d_previous, d_current = 0, 1, 0, 0
    b, derivative = [], []
    for j in range(n + 1):
        b.append(current + previous)
        derivative.append(d_current + d_previous)
        previous, current, d_previous, d_current = current, -previous, d_current, current - d_previous
    return b, derivative


def exact_polynomial(coefficients, prefix=False):
    n = len(coefficients)
    p = 2 * n + 1
    denominator = lcm(*(value.denominator for value in coefficients))
    scaled = [int(value * denominator) for value in coefficients]
    # z^m B_m(z+z^-1) = 1+...+z^(2m).
    full = [0] * (2 * n + 3)
    for j in range(p):
        full[j] += denominator
        full[j + 2] += denominator
    for i, value in enumerate(scaled):
        for j in range(i + 2, p - i):
            full[j] += value
    assert full == full[::-1]
    assert full[0] == full[-1] == denominator
    endpoint = Fraction(sum((-1) ** j * value for j, value in enumerate(full)), denominator)
    assert endpoint == 2 + sum((-1) ** i * value for i, value in enumerate(coefficients))
    if prefix:
        expected = []
        numerator = {0: 1, 2: 2, 4: 1}
        for degree in range(L + 1):
            value = numerator.get(degree, 0)
            for shift, sign in [(1, 1), (2, 1), (3, -1)]:
                if degree >= shift:
                    value += sign * expected[degree - shift]
            expected.append(value)
        assert full[:L + 1] == [value * denominator for value in expected]
    b, derivative = zero_jets(n)
    q0 = sum(value * b[n - 1 - i] for i, value in enumerate(coefficients))
    qp = b[n] + sum(value * derivative[n - 1 - i] for i, value in enumerate(coefficients))
    polynomial_denominator = denominator // gcd(denominator, *full)
    return {"degree": 2 * n + 2, "common_denominator": denominator,
            "polynomial_minimum_common_denominator": polynomial_denominator,
            "polynomial_scaled_coefficients": full, "endpoint": endpoint,
            "Q0": q0, "Qprime0": qp,
            "all_coefficients_integer": all(value.denominator == 1 for value in coefficients),
            "noninteger_parameter_count": sum(value.denominator != 1 for value in coefficients),
            "polynomial_is_integer": polynomial_denominator == 1}


def ball_bounds(text):
    match = re.fullmatch(r"\[([+\-0-9.eE]+) \+/- ([+\-0-9.eE]+)\]", text)
    assert match is not None, text
    midpoint, radius = map(Fraction, match.groups())
    assert radius > 0
    return midpoint - radius, midpoint + radius


def interval_signs(coefficients, recorded_checks, arb, strong_margin=False):
    n, p = len(coefficients), 2 * len(coefficients) + 1
    values = [arb(value.numerator) / value.denominator for value in coefficients]
    for check in recorded_checks:
        assert list(map(Fraction, check["coefficients_rational"])) == coefficients
        assert len(check["sign_rows"]) == n
    signs = []
    containment_count = 0
    for j in range(1, n + 1):
        theta = 2 * arb.pi() * j / p
        node, sine = 2 * theta.cos(), theta.sin()
        assert sine > 0
        next_value = after_next = arb(0)
        for coefficient in reversed(values):
            current = coefficient + node * next_value - after_next
            after_next, next_value = next_value, current
        h_value = next_value
        required = 1 if j < n else -1
        if required * h_value > 0:
            sign = True
        else:
            assert required * h_value < 0
            sign = False
        signs.append(sign)
        sine_value = sine * h_value
        if strong_margin:
            assert required * h_value > arb(1) / 2000
            assert required * sine_value > arb(9) / 10000
        for check in recorded_checks:
            row = check["sign_rows"][j - 1]
            assert (row["node"], row["required_sign"]) == (j, required)
            assert row["strict_sign_certified"] is sign
            lo, hi = ball_bounds(row["sine_value_ball"])
            assert sine_value > arb(lo.numerator) / lo.denominator
            assert sine_value < arb(hi.numerator) / hi.denominator
            containment_count += 1
    for check in recorded_checks:
        assert check["all_strict_signs_certified"] is all(signs)
    return {"nodes_checked": n, "correct_strict_signs": sum(signs),
            "opposite_strict_signs": n - sum(signs),
            "all_required_signs": all(signs),
            "recorded_sine_balls_containing_independent_enclosures": containment_count,
            "signed_h_lower_bound": "1/2000" if strong_margin else None,
            "signed_sine_lower_bound": "9/10000" if strong_margin else None}


def floating_records():
    geometry = {}
    reports = []
    for filename in RUN_FILES:
        record = load(filename)
        p, n = record["p"], record["n"]
        assert p == 2 * n + 1 and p in (401, 2003)
        assert (record["x"], record["kappa"], record["prefix_L"]) == (0, 1, L)
        assert record["fixed_coefficients"] == FIXED
        assert record["free_indices"] == list(range(L - 1, n))
        end_row = [(-1) ** i for i in range(L - 1, n)]
        assert record["endpoint_row"] == end_row and record["endpoint_rhs"] == -279
        objective = record.get("objective", "margin")
        b, derivative = zero_jets(n)
        q0_rows = [b[n - 1 - i] for i in range(n)]
        qp_rows = [derivative[n - 1 - i] for i in range(n)]
        q0_fixed = sum(a * v for a, v in zip(FIXED, q0_rows))
        qp_fixed = b[n] + sum(a * v for a, v in zip(FIXED, qp_rows))
        if "q0_row" in record:
            assert record["q0_row"] == q0_rows[L - 1:]
            assert record["qprime_row"] == qp_rows[L - 1:]
            assert record["q0_fixed"] == q0_fixed and record["qprime_fixed"] == qp_fixed
            assert record["conditional_q0_zero"] is objective.startswith("qprime")
        matrix = record.get("floating_signed_sine_rows")
        if p not in geometry:
            assert matrix is not None and len(matrix) == n
            largest = 0.0
            for j, row in enumerate(matrix, 1):
                assert len(row) == n - L + 1
                sign = 1 if j < n else -1
                for index, value in enumerate(row, L - 1):
                    reference = sign * math.sin(2 * math.pi * j * (index + 1) / p)
                    largest = max(largest, abs(reference - value))
            assert largest < 3e-12
            geometry[p] = (matrix, record["floating_fixed_signed_sine"], largest)
        reference_matrix, fixed_rows, largest = geometry[p]
        if matrix is not None:
            assert matrix == reference_matrix
        assert record["floating_fixed_signed_sine"] == fixed_rows
        fixed_error = max(abs(fixed_rows[j - 1] - (1 if j < n else -1) * math.fsum(
            a * math.sin(2 * math.pi * j * (i + 1) / p) for i, a in enumerate(FIXED)))
                          for j in range(1, n + 1))
        assert fixed_error < 1e-9
        report = {"file": filename, "mode": record["mode"], "objective": objective,
                  "model_status": record["model_status"], "solution_value_valid": record["solution_value_valid"],
                  "matrix_shape": [n, n - L + 1], "maximum_float_coefficient_difference": largest,
                  "maximum_float_fixed_row_difference": fixed_error,
                  "record_contains_jet_rows": "q0_row" in record,
                  "requested_Q0": record.get("requested_Q0"),
                  "requested_Qprime0": record.get("requested_Qprime0")}
        if record["mode"] == "integer":
            assert record["integer_coefficient_bound"] == 16
            assert record["integer_search_sine_margin"] == 1e-7
            assert record["options"]["time_limit"] == 60.0
            assert record["model_status"] == "HighsModelStatus.kTimeLimit"
            assert record["solution_value_valid"] is False and record["candidate"] is None
            report["conclusion"] = "recorded timeout with no valid solution; no infeasibility conclusion"
        else:
            assert record["model_status"] == "HighsModelStatus.kOptimal" and record["solution_value_valid"]
            raw = record["raw_tail"]
            assert len(raw) == n - L + 1
            signed_min = min(math.fsum(v * x for v, x in zip(row, raw)) + fixed
                             for row, fixed in zip(reference_matrix, fixed_rows))
            assert abs(signed_min - record["observed_signed_sine_minimum"]) < 1e-7
            proposed = list(map(Fraction, FIXED)) + [Fraction(str(value)) for value in raw]
            exact_end = 2 + sum((-1) ** i * value for i, value in enumerate(proposed))
            exact_q0 = sum(value * weight for value, weight in zip(proposed, q0_rows))
            exact_qp = b[n] + sum(value * weight for value, weight in zip(proposed, qp_rows))
            if objective == "margin":
                assert list(map(Fraction, record["candidate"]["coefficients_rational"])) == proposed
                assert Fraction(record["candidate"]["endpoint"]) == exact_end
            assert abs(float(exact_end) - record["observed_endpoint"]) < 1e-7
            for key, exact in [("observed_Q0", exact_q0), ("observed_Qprime0", exact_qp)]:
                if key in record:
                    assert abs(float(exact) - record[key]) < 1e-7
            report.update({"observed_signed_sine_minimum": record["observed_signed_sine_minimum"],
                           "observed_endpoint": record["observed_endpoint"],
                           "observed_Q0": record.get("observed_Q0"),
                           "observed_Qprime0": record.get("observed_Qprime0"),
                           "optimized_margin": record.get("optimized_margin"),
                           "conditional_Q0_zero": objective.startswith("qprime"),
                           "raw_decimal_Q0": str(exact_q0), "raw_decimal_Qprime0": str(exact_qp),
                           "conclusion": "numerical recorded optimum only; no exact global bound"})
        reports.append(report)
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--flint-path", type=Path, default=DEFAULT_FLINT)
    args = parser.parse_args()
    sys.path.insert(0, str(args.flint_path))
    import flint
    from flint import arb, ctx
    ctx.prec = 2048
    ctx.threads = 1

    data = json.loads(INPUT.read_text(encoding="utf-8"))
    assert tuple(data[k] for k in ("p", "n", "x", "kappa", "prefix_L")) == (2003, 1001, 0, 1, 140)
    coefficients = list(map(Fraction, data["coefficients_rational"]))
    assert len(coefficients) == 1001 and coefficients[:L - 1] == FIXED
    exact = exact_polynomial(coefficients, prefix=True)
    assert exact["endpoint"] == Fraction(3027458616443292296351, 10**19)
    assert exact["endpoint"] > 0
    assert exact["noninteger_parameter_count"] == 862
    assert exact["polynomial_minimum_common_denominator"] == 10**19
    real_check = load("real_p2003_verification.json")
    proposal_check = load("prefix_cell_lp_p2003.json")["candidate"]
    for check in (real_check, proposal_check):
        assert Fraction(check["endpoint"]) == exact["endpoint"] and check["endpoint_positive"]
    signs = interval_signs(coefficients, [real_check, proposal_check], arb, strong_margin=True)

    control = load("control.json")
    control_coefficients = list(map(Fraction, control["coefficients"]))
    control_exact = exact_polynomial(control_coefficients)
    assert control_exact["polynomial_scaled_coefficients"] == control["polynomial_ascending"]
    assert (control_exact["endpoint"], control_exact["Q0"], control_exact["Qprime0"]) == (2, 0, -3)
    control_signs = interval_signs(control_coefficients, [control["check"]], arb)
    rejected = load("prefix_cell_lp.json")["candidate"]
    rejected_coefficients = list(map(Fraction, rejected["coefficients_rational"]))
    rejected_signs = interval_signs(rejected_coefficients, [rejected], arb)
    assert not rejected_signs["all_required_signs"]

    result = {"scope": "fixed finite J159 evidence; no new theorem, solver run, integer completion or nonneutrality",
              "python": sys.version.split()[0], "python_flint": flint.__version__, "precision_bits": 2048,
              "independent_method": "geometric-block full lift, zero-jet recurrences and direct E-basis Clenshaw signs",
              "real_witness": {key: str(value) if isinstance(value, Fraction) else value
                               for key, value in exact.items()},
              "real_witness_signs": signs,
              "control_exact_endpoint": str(control_exact["endpoint"]),
              "control_Q0": str(control_exact["Q0"]), "control_Qprime0": str(control_exact["Qprime0"]),
              "control_signs": control_signs,
              "conductor401_proposal_signs": rejected_signs,
              "numerical_record_checks": floating_records(),
              "numerical_check_limits": "floating consistency only; no dual or exact optimum certificate",
              "excluded_material": "jet_lattice.py and D22 were not read or executed"}
    output = OUT_HOME / "real_cell_independent.json"
    pending = output.with_suffix(".json.part")
    pending.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    pending.replace(output)
    print(json.dumps({"degree": exact["degree"], "endpoint": str(exact["endpoint"]),
                      "Q0": str(exact["Q0"]), "Qprime0": str(exact["Qprime0"]),
                      "polynomial_minimum_common_denominator": exact["polynomial_minimum_common_denominator"],
                      "real_signs": signs, "control_signs": control_signs,
                      "conductor401_proposal_signs": rejected_signs,
                      "numerical_records_checked": len(result["numerical_record_checks"])}, indent=2))


if __name__ == "__main__":
    main()
