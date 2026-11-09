"""A separate p=81, k=3, x=0 proposal with third moment N=6.

The old two-moment experiment is unchanged. This wrapper fixes a2=4 in its
complete coefficient box and makes one bounded MILP call. A missing proposal
or numerical infeasibility is not an integer exclusion.
"""

import argparse
import json
from pathlib import Path
from time import monotonic
import warnings

import affine_milp as base
from flint import fmpz_poly
from scipy.optimize import Bounds


THIRD_MOMENT = 6
FIXED_A2 = 4


def model():
    objective, integrality, old_bounds, constraints, record = base.build_model()
    lower, upper = old_bounds.lb.copy(), old_bounds.ub.copy()
    lower[2] = upper[2] = FIXED_A2
    assert lower[0] == upper[0] == 2 and lower[1] == upper[1] == 0
    for i in range(80):
        if i != 2:
            assert lower[i] == old_bounds.lb[i] and upper[i] == old_bounds.ub[i]
    record["variable_lower"][2] = record["variable_upper"][2] = FIXED_A2
    record["third_moment_target"] = THIRD_MOMENT
    record["additional_fixed_coordinate"] = {"index": 2, "value": FIXED_A2}
    record["base_experiment_preserved"] = "affine_milp.py, two-moment domain"
    return objective, integrality, Bounds(lower, upper), constraints, record


def precheck(coefficients):
    if len(coefficients) != base.N or any(type(a) is not int for a in coefficients):
        return {"valid": False, "reason": "not forty native integer coefficients"}
    elements, B, D = base.basis()
    h = sum((a * E for a, E in zip(coefficients, elements)), fmpz_poly())
    C = (D * h) % B
    K = int(C[39])
    L = int(C[38] - B[39] * K)
    third = int(C[37] - B[39] * L - B[38] * K)
    assert (K, L, third) == (coefficients[0], coefficients[1],
                             coefficients[0] + coefficients[2])
    U = sum((-1)**i * a for i, a in enumerate(coefficients))
    Q = elements[1] * B + C
    endpoint = -int(Q(-2))
    assert endpoint == 2 + U
    checks = {
        "moment_target": (K, L, third) == (2, 0, THIRD_MOMENT),
        "all_coefficient_bounds": all(abs(a) <= b for a, b in
                                       zip(coefficients, base.COEFFICIENT_BOUNDS)),
        "strict_endpoint": endpoint > 0,
        "no_zero_component": B.gcd(h).degree() == 0,
    }
    signs = base.all_signs(h)
    checks["strict_node_signs"] = signs["all_strict_signs"]
    return {
        "valid": all(checks.values()), "checks": checks,
        "K": K, "L": L, "third_moment": third, "U": U,
        "P_minus_one": endpoint, "sign_checks": signs,
    }


def validate(coefficients):
    screening = precheck(coefficients)
    record = {"precheck": screening, "complete_candidate": None}
    if screening["valid"]:
        candidate = base.verify_coefficients(coefficients)
        assert candidate["valid_strict_chamber"]
        assert candidate["third_moment"] == THIRD_MOMENT
        record["complete_candidate"] = candidate
    return record


def propose():
    objective, integrality, bounds, constraints, specification = model()
    base.write_json("model_81_k3_N6.json", specification)
    started = monotonic()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        result = base.milp(objective, integrality=integrality, bounds=bounds,
                           constraints=constraints, options=base.OPTIONS.copy())
    record = {
        "third_moment_target": THIRD_MOMENT, "solver_calls": 1,
        "solver_seconds": monotonic() - started, "solver_options": base.OPTIONS,
        "status": int(result.status), "message": str(result.message),
        "success_reported_by_solver": bool(result.success),
        "warnings": [str(item.message) for item in caught],
        "versions": {
            "python": base.platform.python_version(), "scipy": base.scipy.__version__,
            "numpy": base.np.__version__, "python_flint": base.flint.__version__,
        },
        "objective_reported": base.scalar_metric(getattr(result, "fun", None)),
        "mip_node_count": (int(result.mip_node_count)
                           if getattr(result, "mip_node_count", None) is not None else None),
        "mip_gap": base.scalar_metric(getattr(result, "mip_gap", None)),
        "mip_dual_bound": base.scalar_metric(getattr(result, "mip_dual_bound", None)),
        "raw_solution": result.x.tolist() if result.x is not None else None,
        "validation": None, "mathematical_exclusion_claimed": False,
        "mathematical_optimality_claimed": False,
    }
    base.write_json("proposal_81_k3_N6.json", record)
    print("N6 solver return", {key: record[key] for key in (
        "status", "message", "solver_seconds", "objective_reported",
        "mip_node_count", "mip_gap", "mip_dual_bound")}, flush=True)
    if result.x is not None:
        rounded = [int(round(a)) for a in result.x[:base.N]]
        distance = max(abs(a-b) for a, b in zip(result.x[:base.N], rounded))
        record["coefficient_rounding_max_error"] = float(distance)
        record["rounding_tolerance"] = base.ROUNDING_TOLERANCE
        record["rounded_coefficients"] = rounded
        if distance <= base.ROUNDING_TOLERANCE:
            record["validation"] = validate(rounded)
        else:
            record["rounding_rejected"] = True
    base.write_json("proposal_81_k3_N6.json", record)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("propose")
    verification = commands.add_parser("verify")
    verification.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    if args.command == "propose":
        propose()
    else:
        native = json.loads(args.input.read_text(encoding="utf-8"))
        assert (native["p"], native["cut"], native["x"],
                native["third_moment_target"]) == (81, 3, 0, THIRD_MOMENT)
        result = validate(native["coefficients_E_basis"])
        base.write_json("incumbent_verification_81_k3_N6.json", result)
        assert result["precheck"]["valid"], result["precheck"]["checks"]


if __name__ == "__main__":
    main()
