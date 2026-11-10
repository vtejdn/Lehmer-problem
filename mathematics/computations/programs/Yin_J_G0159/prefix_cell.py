"""Numerical proposals for one fixed odd-grid integer prefix completion.

Solver status is observational. Actual proposed coefficients are checked with
Arb signs and exact rational endpoint arithmetic before any feasibility claim.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
P, N, L, KAPPA = 401, 200, 140, 1
FIXED = [2 if i == 0 else 4 if i % 2 == 0 else 0 for i in range(L - 1)]


def endpoint(coefficients):
    return 2 + sum((-1) ** i * value for i, value in enumerate(coefficients))


def b_zero(index):
    return (-1) ** (index // 2)


def b_derivative_zero(index):
    if index == 0:
        return 0
    if index % 2 == 0:
        half = index // 2
        return (-1) ** (half - 1) * half
    half = index // 2
    return (-1) ** half * (half + 1)


def lift(coefficients):
    n = len(coefficients)
    p = 2 * n + 1
    numerator = [0] * (p + 3)
    numerator[0], numerator[2] = 1, 1
    numerator[p], numerator[p + 2] = -1, -1
    for i, value in enumerate(coefficients):
        numerator[i + 2] += value
        numerator[p - i] -= value
    result, cumulative = [], 0
    for value in numerator[:-1]:
        cumulative += value
        result.append(cumulative)
    assert cumulative + numerator[-1] == 0
    assert result == result[::-1] and result[0] == result[-1] == 1
    assert sum((-1) ** i * value for i, value in enumerate(result)) == endpoint(coefficients)
    return result


def interval_check(coefficients, kappa=1):
    from flint import arb, ctx

    ctx.prec = 256
    ctx.threads = 1
    exact = [Fraction(value) for value in coefficients]
    values = [arb(value.numerator) / value.denominator for value in exact]
    n, p = len(values), 2 * len(values) + 1
    checked = []
    for j in range(1, n + 1):
        theta = 2 * arb.pi() * j / p
        sine_value = sum((value * ((i + 1) * theta).sin() for i, value in enumerate(values)), arb(0))
        sign = 1 if j <= n - kappa else -1
        checked.append({"node": j, "required_sign": sign, "sine_value_ball": str(sine_value),
                        "strict_sign_certified": bool(sign * sine_value > 0)})
    end = endpoint(exact)
    return {"precision_bits": 256, "coefficients_rational": [str(value) for value in exact],
            "endpoint": str(end), "endpoint_positive": end > 0,
            "all_strict_signs_certified": all(row["strict_sign_certified"] for row in checked),
            "sign_rows": checked}


def save(data, name):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    path = OUTPUT / name
    pending = path.with_suffix(path.suffix + ".part")
    pending.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    pending.replace(path)
    return path


def control():
    # The conductor-nine success in C884 v1: h = 2 E_0 + 2 E_3.
    a = [2, 0, 0, 2]
    check = interval_check(a)
    polynomial = lift(a)
    assert polynomial == [1, 1, 4, 4, 4, 6, 4, 4, 4, 1, 1]
    assert sum(value * b_zero(3 - i) for i, value in enumerate(a)) == 0
    assert b_zero(4) + sum(value * b_derivative_zero(3 - i) for i, value in enumerate(a)) == -3
    assert check["all_strict_signs_certified"] and check["endpoint"] == "2"
    data = {"scope": "retained conductor-nine chamber control, not the conductor-401 search",
            "p": 9, "coefficients": a, "polynomial_ascending": polynomial, "check": check}
    path = save(data, "control.json")
    print(json.dumps({"control_passed": True, "output": str(path)}))


def run(args):
    import highspy
    import numpy as np
    import flint

    P, N = args.p, (args.p - 1) // 2
    started = time.perf_counter()
    theta = 2 * math.pi * np.arange(1, N + 1, dtype=float) / P
    sine = np.sin(theta[:, None] * np.arange(1, N + 1, dtype=float)[None, :])
    signs = np.ones(N)
    signs[-KAPPA:] = -1
    rows = signs[:, None] * sine[:, L - 1:]
    fixed_rows = signs * (sine[:, :L - 1] @ np.array(FIXED, dtype=float))
    end_row = [(-1) ** i for i in range(L - 1, N)]
    end_fixed = endpoint(FIXED)
    assert end_fixed == 280 and len(end_row) == N - L + 1
    q0_all = [b_zero(N - 1 - i) for i in range(N)]
    qp_all = [b_derivative_zero(N - 1 - i) for i in range(N)]
    q0_fixed = sum(value * coefficient for value, coefficient in zip(FIXED, q0_all))
    qp_fixed = b_zero(N) + sum(value * coefficient for value, coefficient in zip(FIXED, qp_all))
    q0_tail, qp_tail = q0_all[L - 1:], qp_all[L - 1:]

    solver = highspy.Highs()
    options = {"output_flag": False, "threads": 1, "random_seed": 0,
               "time_limit": args.seconds, "primal_feasibility_tolerance": 1e-9,
               "dual_feasibility_tolerance": 1e-9, "mip_feasibility_tolerance": 1e-9,
               "small_matrix_value": 1e-12}
    for key, value in options.items():
        assert solver.setOptionValue(key, value) == highspy.HighsStatus.kOk
    integer = args.mode == "integer"
    bound = args.coefficient_bound if integer else highspy.kHighsInf
    kind = highspy.HighsVarType.kInteger if integer else highspy.HighsVarType.kContinuous
    objective_row = q0_tail if args.objective.startswith("q0") else qp_tail
    objective_sign = -1 if args.objective.endswith("max") else 1
    variables = [solver.addVariable(lb=-bound, ub=bound, type=kind,
                                   obj=0 if args.objective == "margin" else objective_sign * objective_row[i])
                 for i in range(len(end_row))]
    if not integer and args.objective == "margin":
        margin = solver.addVariable(lb=-highspy.kHighsInf, ub=highspy.kHighsInf, obj=-1)
    else:
        margin = args.margin if integer else 0
    for row, fixed in zip(rows, fixed_rows):
        solver.addConstr(solver.qsum(float(value) * variables[i] for i, value in enumerate(row)) - margin >= -float(fixed))
    solver.addConstr(solver.qsum(value * variables[i] for i, value in enumerate(end_row)) >= 1 - end_fixed)
    if args.objective.startswith("qprime"):
        solver.addConstr(solver.qsum(value * variables[i] for i, value in enumerate(q0_tail)) == -q0_fixed)
    if args.q0 is not None:
        solver.addConstr(solver.qsum(value * variables[i] for i, value in enumerate(q0_tail)) == args.q0 - q0_fixed)
    if args.qprime is not None:
        solver.addConstr(solver.qsum(value * variables[i] for i, value in enumerate(qp_tail)) == args.qprime - qp_fixed)
    result = solver.run()
    status = solver.getModelStatus()
    solution = solver.getSolution()
    info = solver.getInfo()
    data = {"scope": "numerical fixed-cell proposal; status alone proves no exact infeasibility",
            "mode": args.mode, "objective": args.objective, "p": P, "n": N, "x": 0, "kappa": KAPPA, "prefix_L": L,
            "free_indices": list(range(L - 1, N)), "fixed_coefficients": FIXED,
            "integer_coefficient_bound": args.coefficient_bound if integer else None,
            "integer_search_sine_margin": args.margin if integer else None,
            "options": options, "highspy_version": solver.version(), "numpy_version": np.__version__,
            "python_flint_version": flint.__version__, "run_status": str(result),
            "model_status": str(status), "solution_value_valid": bool(solution.value_valid),
            "elapsed_seconds": time.perf_counter() - started,
            "floating_signed_sine_rows": rows.tolist() if args.objective == "margin" else None,
            "floating_fixed_signed_sine": fixed_rows.tolist(),
            "endpoint_row": end_row, "endpoint_rhs": 1 - end_fixed,
            "q0_row": q0_tail, "q0_fixed": q0_fixed, "qprime_row": qp_tail, "qprime_fixed": qp_fixed,
            "conditional_q0_zero": args.objective.startswith("qprime"),
            "requested_Q0": args.q0, "requested_Qprime0": args.qprime,
            "row_dual": [float(value) for value in solution.row_dual],
            "solver_iterations": int(info.simplex_iteration_count), "candidate": None}
    if solution.value_valid and all(math.isfinite(value) for value in solution.col_value):
        raw = [float(value) for value in solution.col_value[:len(end_row)]]
        data["raw_tail"] = raw
        data["observed_signed_sine_minimum"] = float(np.min(rows @ np.array(raw) + fixed_rows))
        data["observed_endpoint"] = float(end_fixed + np.dot(end_row, raw))
        data["observed_Q0"] = float(q0_fixed + np.dot(q0_tail, raw))
        data["observed_Qprime0"] = float(qp_fixed + np.dot(qp_tail, raw))
        if not integer:
            if args.objective == "margin":
                data["optimized_margin"] = float(solution.col_value[-1])
            proposed = FIXED + [Fraction(str(value)) for value in raw]
        else:
            rounded = [round(value) for value in raw]
            data["integer_rounding_distance"] = max(abs(value - whole) for value, whole in zip(raw, rounded))
            proposed = FIXED + rounded
        check = interval_check(proposed) if integer or args.objective == "margin" else None
        if check:
            exact_q0 = sum(Fraction(value) * coefficient for value, coefficient in zip(proposed, q0_all))
            exact_qp = b_zero(N) + sum(Fraction(value) * coefficient for value, coefficient in zip(proposed, qp_all))
            check["Q0"] = str(exact_q0)
            check["Qprime0"] = str(exact_qp)
            check["requested_jets_satisfied"] = ((args.q0 is None or exact_q0 == args.q0)
                                                 and (args.qprime is None or exact_qp == args.qprime))
        data["candidate"] = check
        if integer and check and check["endpoint_positive"] and check["all_strict_signs_certified"] and check["requested_jets_satisfied"]:
            polynomial = lift(proposed)
            data["candidate"]["polynomial_ascending"] = polynomial
            # Explicit cross-J reuse of the reviewed complete polynomial evaluator.
            sys.path.insert(0, str(HERE.parent / "Yin_J_G0156"))
            import sampler
            data["candidate"]["complete_measure_certificate"] = sampler.certify_polynomial(polynomial)
    suffix = "" if P == 401 else f"_p{P}"
    if args.objective != "margin":
        suffix += "_" + args.objective
    if args.q0 is not None or args.qprime is not None:
        suffix += f"_Q0_{args.q0}_Qp_{args.qprime}".replace("-", "neg")
    path = save(data, f"prefix_cell_{args.mode}{suffix}.json")
    print(json.dumps({key: data.get(key) for key in ("mode", "objective", "model_status", "solution_value_valid", "optimized_margin",
                                                   "observed_signed_sine_minimum", "observed_endpoint", "observed_Q0",
                                                   "observed_Qprime0", "elapsed_seconds")}))
    print(json.dumps({"output": str(path), "candidate_signs_certified": bool(data["candidate"] and data["candidate"]["all_strict_signs_certified"])}))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["control", "lp", "integer"], default="lp")
    parser.add_argument("--p", type=int, default=401)
    parser.add_argument("--objective", choices=["margin", "q0-min", "q0-max", "qprime-min", "qprime-max"], default="margin")
    parser.add_argument("--q0", type=int)
    parser.add_argument("--qprime", type=int)
    parser.add_argument("--seconds", type=float, default=60)
    parser.add_argument("--coefficient-bound", type=int, default=256)
    parser.add_argument("--margin", type=float, default=1e-7)
    args = parser.parse_args()
    if args.seconds <= 0 or args.coefficient_bound <= 0 or args.margin <= 0:
        parser.error("positive limits and margin are required")
    if args.p < 2 * L + 1 or args.p % 2 != 1:
        parser.error("an odd conductor with at least one free tail coefficient is required")
    if args.objective.startswith("qprime") and args.q0 not in (None, 0):
        parser.error("the qprime extremum already imposes Q0 = 0")
    if args.mode == "control":
        control()
    else:
        run(args)


if __name__ == "__main__":
    main()
