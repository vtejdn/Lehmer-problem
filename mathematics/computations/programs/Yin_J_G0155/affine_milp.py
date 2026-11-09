"""One fixed affine p=81, k=3, x=0 MILP proposal and exact incumbent checks.

The proposal uses all 40 integral E_i coefficients and the full L462v9 box.
Only one scipy.optimize.milp call is made by propose.  The verify command
checks a retained integer incumbent without running a solver.
"""

import argparse
from fractions import Fraction
from math import isfinite
from pathlib import Path
from time import monotonic
import json
import platform
import warnings

import flint
from flint import arb, ctx, fmpq, fmpz_poly
import numpy as np
import scipy
from scipy.optimize import Bounds, LinearConstraint, milp


P = 81
N = 40
CUT = 3
SIGN_MARGIN = 1e-6
ROW_ERROR_DENOMINATOR = 2**46
MODEL_PRECISION = 512
ROUNDING_TOLERANCE = 1e-6
COEFFICIENT_BOUNDS = [2, 0] + [(1550*(i+1)+2)//3 - 1 for i in range(2, N)]
OPTIONS = {
    "disp": True, "presolve": True, "time_limit": 60.0, "node_limit": 100000,
    "mip_rel_gap": 0.0, "mip_abs_gap": 0.0,
    "mip_feasibility_tolerance": 1e-8,
    "primal_feasibility_tolerance": 1e-9,
    "dual_feasibility_tolerance": 1e-9,
    "random_seed": 0, "threads": 1,
}


def basis():
    t = fmpz_poly([0, 1])
    elements = [fmpz_poly([1]), t]
    for _ in range(2, N + 1):
        elements.append(t * elements[-1] - elements[-2])
    return elements, elements[40] + elements[39], elements[39] + elements[38]


def sturm_count(numerator, denominator):
    minors = [1, numerator]
    for _ in range(2, 40):
        minors.append(numerator * minors[-1] - denominator**2 * minors[-2])
    minors.append((numerator + denominator) * minors[-1] - denominator**2 * minors[-2])
    assert len(minors) == 41 and all(minors)
    variations = sum(a*b < 0 for a, b in zip(minors, minors[1:]))
    return {"rational": [numerator, denominator], "scaled_minors": minors,
            "variations": variations}


def build_model():
    ctx.prec = MODEL_PRECISION
    elements, _, _ = basis()
    bound_proof = [sturm_count(a, b) for a, b in ((-193, 100), (-49, 25), (-31, 16))]
    assert all(record["variations"] == 37 for record in bound_proof)
    assert COEFFICIENT_BOUNDS[-1] == 20666
    error = arb(fmpq(1, ROW_ERROR_DENOMINATOR))
    evaluation_error = Fraction(sum(COEFFICIENT_BOUNDS[2:]), ROW_ERROR_DENOMINATOR)
    assert float(evaluation_error) + OPTIONS["mip_feasibility_tolerance"] < SIGN_MARGIN

    rows, lower, upper, labels = [], [], [], []
    midpoint_ratios = []
    for j in range(1, N + 1):
        node = 2 * arb.cos_pi_fmpq(fmpq(2*j, P))
        midpoints, ratios = [], []
        for i in range(N):
            value = elements[i](node)
            midpoint = float(value.mid())
            numerator, denominator = midpoint.as_integer_ratio()
            assert abs(value - arb(fmpq(numerator, denominator))) < error
            midpoints.append(midpoint)
            ratios.append([numerator, denominator])
        assert midpoints[0] == 1.0
        sigma = 1 if j <= N - CUT else -1
        rows.append([sigma * value for value in midpoints] + [0.0] * N)
        lower.append(SIGN_MARGIN)
        upper.append(np.inf)
        labels.append(f"sign_node_{j}")
        midpoint_ratios.append(ratios)
    for i in range(N):
        for sign in (1, -1):
            row = [0.0] * (2*N)
            row[i], row[N+i] = sign, -1
            rows.append(row)
            lower.append(-np.inf)
            upper.append(0.0)
            labels.append(f"absolute_{i}_{sign}")
    rows.append([(-1)**i for i in range(N)] + [0.0]*N)
    lower.append(-1.0)
    upper.append(np.inf)
    labels.append("endpoint_U_at_least_minus_one")
    a_lower = [-bound for bound in COEFFICIENT_BOUNDS]
    a_upper = COEFFICIENT_BOUNDS.copy()
    a_lower[0] = a_upper[0] = 2
    a_lower[1] = a_upper[1] = 0
    variable_lower = a_lower + [0]*N
    variable_upper = a_upper + COEFFICIENT_BOUNDS
    objective = [0.0]*N + [1.0]*N
    integrality = [1]*N + [0]*N
    assert len(rows) == 121 and all(len(row) == 80 for row in rows)
    serial = {
        "p": P, "n": N, "cut": CUT, "profile_x": 0,
        "coefficient_basis": "E0=1,E1=t,E(i+1)=t*Ei-E(i-1)",
        "coefficient_absolute_bounds": COEFFICIENT_BOUNDS,
        "variable_lower": variable_lower, "variable_upper": variable_upper,
        "integrality": integrality, "objective": objective,
        "row_labels": labels, "constraint_matrix_binary64": rows,
        "constraint_lower": [value if isfinite(value) else None for value in lower],
        "constraint_upper": [value if isfinite(value) else None for value in upper],
        "null_bound_convention": "lower null means -infinity; upper null means +infinity",
        "node_basis_midpoint_rational_pairs": midpoint_ratios,
        "model_precision_bits": MODEL_PRECISION,
        "basis_midpoint_error_strict_bound": [1, ROW_ERROR_DENOMINATOR],
        "sign_row_evaluation_error_upper": [evaluation_error.numerator, evaluation_error.denominator],
        "fixed_coordinate_errors": "a0=2 multiplies exact E0=1; a1=0",
        "sign_margin_binary64": SIGN_MARGIN,
        "sign_margin_exact_binary64_ratio": list(SIGN_MARGIN.as_integer_ratio()),
        "sturm_separator_checks": bound_proof,
        "solver_options": OPTIONS, "rounding_tolerance": ROUNDING_TOLERANCE,
        "mathematical_exclusion_claimed": False,
    }
    return (
        np.asarray(objective), np.asarray(integrality),
        Bounds(variable_lower, variable_upper),
        LinearConstraint(np.asarray(rows), np.asarray(lower), np.asarray(upper)),
        serial,
    )


def all_signs(h):
    attempts = []
    for precision in (256, 512, 1024, 2048, 4096):
        ctx.prec = precision
        values, certified, wrong, unresolved = [], [], [], []
        for j in range(1, N + 1):
            node = 2 * arb.cos_pi_fmpq(fmpq(2*j, P))
            value = h(node)
            signed = value if j <= N-CUT else -value
            values.append({"node": j, "value_ball": str(value), "signed_value_ball": str(signed)})
            if signed > 0:
                certified.append(j)
            elif signed < 0:
                wrong.append(j)
            else:
                unresolved.append(j)
        attempts.append({"precision_bits": precision, "values": values,
                         "certified_nodes": certified, "wrong_nodes": wrong,
                         "unresolved_nodes": unresolved})
        if not unresolved:
            break
    return {"attempts": attempts, "all_strict_signs": len(certified) == N,
            "wrong_nodes": wrong, "unresolved_nodes": unresolved}


def whole_measure(polynomial):
    content, factors = polynomial.factor()
    reconstruction = fmpz_poly([content])
    for factor, exponent in factors:
        reconstruction *= factor**exponent
    assert reconstruction == polynomial and int(content) == 1
    attempts = []
    for precision in (256, 512, 1024, 2048, 4096):
        ctx.prec = precision
        total, total_roots, records = arb(1), 0, []
        all_cyclotomic = True
        for factor, exponent in factors:
            cyclotomic = bool(factor.is_cyclotomic())
            all_cyclotomic = all_cyclotomic and cyclotomic
            factor_product = arb(abs(int(factor[factor.degree()])))
            roots, count = [], 0
            for root, multiplicity in factor.complex_roots():
                modulus = abs(root)
                if modulus < 1:
                    contribution, region = arb(1), "inside"
                elif modulus > 1:
                    contribution, region = modulus, "outside"
                else:
                    contribution, region = arb(1).union(modulus), "meets_one"
                factor_product *= contribution**multiplicity
                count += multiplicity
                roots.append({"ball": str(root), "modulus_ball": str(modulus),
                              "contribution_ball": str(contribution),
                              "multiplicity": multiplicity, "region": region})
            assert count == factor.degree()
            if cyclotomic:
                assert not (factor_product > 1 or factor_product < 1)
                factor_product = arb(1)
            total *= factor_product**exponent
            total_roots += count * exponent
            records.append({"coefficients_ascending": list(map(int, factor)),
                            "degree": factor.degree(), "exponent": int(exponent),
                            "cyclotomic": cyclotomic, "root_count": count,
                            "roots": roots, "measure_ball": str(factor_product)})
        assert total_roots == polynomial.degree()
        attempts.append({"precision_bits": precision, "measure_ball": str(total),
                         "radius_below_1e_minus_25": bool(total.rad() < arb("1e-25")),
                         "separated_above_one": bool(total > 1)})
        if total.rad() < arb("1e-25") and (all_cyclotomic or total > 1):
            break
    assert total.rad() < arb("1e-25")
    assert all_cyclotomic or total > 1
    return {
        "factor_content": int(content), "factorization_product_verified": True,
        "factors": records, "root_count_with_multiplicity": total_roots,
        "measure_ball": str(total), "log_measure_ball": str(total.log()),
        "all_cyclotomic": all_cyclotomic, "strictly_above_one": bool(total > 1),
        "precision_attempts": attempts, "whole_measure_certified": True,
    }


def verify_coefficients(coefficients):
    assert len(coefficients) == N and all(type(value) is int for value in coefficients)
    coefficient_checks = {
        "fixed_coordinates": coefficients[:2] == [2, 0],
        "all_coefficient_bounds": all(abs(value) <= bound
                                      for value, bound in zip(coefficients, COEFFICIENT_BOUNDS)),
    }
    elements, B, D = basis()
    t = elements[1]
    h = sum((value*element for value, element in zip(coefficients, elements)), fmpz_poly())
    C = (D*h) % B
    K, L = int(C[39]), int(C[38] - B[39]*C[39])
    assert (K, L) == (coefficients[0], coefficients[1])
    coefficient_checks["moment_target"] = (K, L) == (2, 0)
    signs = all_signs(h)
    common_factor = B.gcd(h)
    U = sum((-1)**i * value for i, value in enumerate(coefficients))
    Q = t*B + C
    z = fmpz_poly([0, 1])
    lift = sum((Q[i]*z**(41-i)*(1+z*z)**i for i in range(42)), fmpz_poly())
    lift_coefficients = list(map(int, lift))
    assert lift.degree() == 82 and lift[0] == lift[82] == 1
    assert lift_coefficients == lift_coefficients[::-1]
    endpoint = int(lift(-1))
    assert endpoint == -int(Q(-2)) == 2 + U
    resultant_h, resultant_Q = int(B.resultant(h)), int(B.resultant(Q))
    assert resultant_h == resultant_Q
    endpoint_pass = U >= -1
    assert endpoint_pass == (endpoint > 0)
    valid = all(coefficient_checks.values()) and signs["all_strict_signs"] and endpoint_pass
    print("Exact incumbent", coefficients, "K,L,U,P(-1)", K, L, U, endpoint,
          "resultant", resultant_h, "valid_strict_chamber", valid, flush=True)
    measure = whole_measure(lift)
    print("Full measure", measure["measure_ball"], flush=True)
    return {
        "p": P, "cut": CUT, "x": 0, "coefficients_E_basis": coefficients,
        "coefficient_checks": coefficient_checks, "L1": sum(map(abs, coefficients)),
        "K": K, "L": L, "third_moment": coefficients[0] + coefficients[2],
        "U": U, "P_minus_one": endpoint, "strict_endpoint": endpoint_pass,
        "sign_checks": signs, "exact_zero_component": common_factor.degree() > 0,
        "gcd_B_h_coefficients_ascending": list(map(int, common_factor)),
        "signed_resultant_B_h": resultant_h, "signed_resultant_B_Q": resultant_Q,
        "absolute_resultant": abs(resultant_h),
        "h_coefficients_ascending": list(map(int, h)),
        "C_coefficients_ascending": list(map(int, C)),
        "Q_coefficients_ascending": list(map(int, Q)),
        "P_coefficients_ascending": lift_coefficients,
        "valid_strict_chamber": valid, "whole_measure": measure,
    }


def output_home():
    source = Path(__file__).resolve()
    output = source.parents[2] / "outputs" / source.parent.name
    output.mkdir(parents=True, exist_ok=True)
    return output


def write_json(name, record):
    (output_home() / name).write_text(json.dumps(record, indent=2, allow_nan=False) + "\n",
                                    encoding="utf-8")


def scalar_metric(value):
    if value is None:
        return None
    result = float(value)
    return result if isfinite(result) else str(result)


def propose():
    objective, integrality, bounds, constraints, model = build_model()
    write_json("model_81_k3.json", model)
    started = monotonic()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        result = milp(objective, integrality=integrality, bounds=bounds,
                      constraints=constraints, options=OPTIONS.copy())
    solver_seconds = monotonic() - started
    record = {
        "solver_calls": 1, "status": int(result.status), "message": str(result.message),
        "success_reported_by_solver": bool(result.success),
        "solver_seconds": solver_seconds, "solver_options": OPTIONS,
        "warnings": [str(warning.message) for warning in caught],
        "versions": {"python": platform.python_version(), "scipy": scipy.__version__,
                     "numpy": np.__version__, "python_flint": flint.__version__},
        "objective_reported": scalar_metric(getattr(result, "fun", None)),
        "mip_node_count": int(result.mip_node_count) if getattr(result, "mip_node_count", None) is not None else None,
        "mip_gap": scalar_metric(getattr(result, "mip_gap", None)),
        "mip_dual_bound": scalar_metric(getattr(result, "mip_dual_bound", None)),
        "raw_solution": result.x.tolist() if result.x is not None else None,
        "candidate_validation": None, "mathematical_exclusion_claimed": False,
        "mathematical_optimality_claimed": False,
    }
    print("Solver return", {key: record[key] for key in (
        "status", "message", "solver_seconds", "objective_reported",
        "mip_node_count", "mip_gap", "mip_dual_bound")}, flush=True)
    write_json("proposal_81_k3.json", record)
    if result.x is not None:
        rounded = [int(round(value)) for value in result.x[:N]]
        distance = max(abs(value - integer) for value, integer in zip(result.x[:N], rounded))
        record["coefficient_rounding_max_error"] = float(distance)
        record["rounding_tolerance"] = ROUNDING_TOLERANCE
        record["rounded_coefficients"] = rounded
        if distance <= ROUNDING_TOLERANCE:
            record["candidate_validation"] = verify_coefficients(rounded)
        else:
            record["rounding_rejected"] = True
    write_json("proposal_81_k3.json", record)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("propose")
    verify = subparsers.add_parser("verify")
    verify.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    if args.command == "propose":
        propose()
    else:
        native = json.loads(args.input.read_text(encoding="utf-8"))
        assert (native["p"], native["cut"], native["x"]) == (81, 3, 0)
        record = verify_coefficients(native["coefficients_E_basis"])
        write_json("incumbent_verification_81_k3.json", record)


if __name__ == "__main__":
    main()
