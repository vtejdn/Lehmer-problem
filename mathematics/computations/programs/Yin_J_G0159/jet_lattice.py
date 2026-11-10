"""A bounded integer-coordinate repair on the fixed conductor-2003 jet branch.

The affine lattice is exact; LP and coordinate repair only propose candidates.
Every integer success is checked against the original grid and complete J156
factor/root evaluator. No solver status is an infeasibility certificate.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import random
import sys
import time

from prefix_cell import FIXED, b_zero, b_derivative_zero, endpoint, interval_check, lift

HERE = Path(__file__).resolve().parent
OUT = HERE.parent.parent / "outputs" / HERE.name
P, N, L, DIM = 2003, 1001, 140, 860


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_suffix(path.suffix + ".part")
    pending.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    pending.replace(path)


def tail_from_u(u):
    """Ascending B coordinates for C_free = 2 - 862t + t^2 sum u_j B_j."""
    assert len(u) == DIM
    tail = [0] * (DIM + 2)
    tail[0], tail[1] = 864, -862
    tail[0] += 2 * u[0] - u[1]
    tail[1] += -u[0] + 2 * u[1]
    tail[2] += u[0]
    tail[3] += u[1]
    for j in range(2, DIM):
        tail[j - 2] += u[j]
        tail[j] += 2 * u[j]
        tail[j + 2] += u[j]
    return tail


def coefficients_from_u(u):
    return FIXED + tail_from_u(u)[::-1]


def jets(coefficients):
    return (sum(value * b_zero(N - 1 - i) for i, value in enumerate(coefficients)),
            b_zero(N) + sum(value * b_derivative_zero(N - 1 - i)
                            for i, value in enumerate(coefficients)))


def controls():
    # Independent monomial recurrences test both exceptional boundary columns.
    bs = [[1], [1, 1]]
    for j in range(1, 10):
        next_b = [0] + bs[-1]
        for k, value in enumerate(bs[-2]):
            next_b[k] -= value
        bs.append(next_b)
    for j in range(9):
        if j == 0:
            terms = [(2, 1), (1, -1), (0, 2)]
        elif j == 1:
            terms = [(3, 1), (1, 2), (0, -1)]
        else:
            terms = [(j + 2, 1), (j, 2), (j - 2, 1)]
        right = [0] * (j + 3)
        for k, multiplier in terms:
            for index, value in enumerate(bs[k]):
                right[index] += multiplier * value
        assert right == [0, 0] + bs[j]
    fixed_q0 = sum(value * b_zero(N - 1 - i) for i, value in enumerate(FIXED))
    fixed_qp = b_zero(N) + sum(value * b_derivative_zero(N - 1 - i)
                             for i, value in enumerate(FIXED))
    assert (fixed_q0, fixed_qp) == (-2, 861)
    rng = random.Random(20261110)
    u = [rng.randrange(-3, 4) for _ in range(DIM)]
    a = coefficients_from_u(u)
    assert len(a) == N and a[:139] == FIXED and jets(a) == (0, -1)
    assert endpoint(a) == 2006 + 4 * sum((-1) ** j * v for j, v in enumerate(u))
    polynomial = lift(a)
    assert len(polynomial) == P + 2
    # Recover u by monic triangular back-substitution in the B columns.
    residue = tail_from_u(u)
    residue[0] -= 864
    residue[1] += 862
    recovered = [0] * DIM
    for j in range(DIM - 1, -1, -1):
        recovered[j] = residue[j + 2]
        if j == 0:
            entries = [(2, 1), (1, -1), (0, 2)]
        elif j == 1:
            entries = [(3, 1), (1, 2), (0, -1)]
        else:
            entries = [(j + 2, 1), (j, 2), (j - 2, 1)]
        for index, weight in entries:
            residue[index] -= weight * recovered[j]
    assert recovered == u and residue == [0] * (DIM + 2)
    return {"boundary_columns_monomial_checked": True,
            "fixed_Q0": fixed_q0, "fixed_Qprime0": fixed_qp,
            "integer_roundtrip_and_jets_checked": True,
            "endpoint_congruence_checked": True, "full_lift_checked": True}


def matrices(np):
    theta = 2 * math.pi * np.arange(1, N + 1, dtype=float) / P
    b = 2 * np.cos(theta)
    signs = np.ones(N)
    signs[-1] = -1
    sine = np.sin(theta[:, None] * np.arange(1, N + 1, dtype=float)[None, :])
    base = np.array(coefficients_from_u([0] * DIM), dtype=float)
    fixed_rows = signs * (sine @ base)
    # Exact grid identity: sin(theta) E_(n-1-j)(b) = (-1)^(node+1)
    # times sin((j+1/2) theta), so the t^2 columns have this closed form.
    node_sign = (-1.0) ** np.arange(2, N + 2)
    rows = signs[:, None] * node_sign[:, None] * b[:, None] ** 2 * np.sin(
        theta[:, None] * (np.arange(DIM, dtype=float)[None, :] + 0.5))
    transform = np.zeros((DIM + 2, DIM))
    transform[0, 0], transform[1, 0], transform[2, 0] = 2, -1, 1
    transform[0, 1], transform[1, 1], transform[3, 1] = -1, 2, 1
    for j in range(2, DIM):
        transform[j - 2, j], transform[j, j], transform[j + 2, j] = 1, 2, 1
    direct = signs[:, None] * sine[:, 139:] @ transform[::-1]
    difference = float(np.max(np.abs(rows - direct)))
    assert difference < 1e-9
    return rows, fixed_rows, b, difference


def lp_proposal(np, highspy, rows, fixed_rows, seconds):
    solver = highspy.Highs()
    options = {"output_flag": False, "threads": 1, "random_seed": 0,
               "time_limit": seconds, "primal_feasibility_tolerance": 1e-9,
               "dual_feasibility_tolerance": 1e-9, "small_matrix_value": 1e-12}
    for name, value in options.items():
        assert solver.setOptionValue(name, value) == highspy.HighsStatus.kOk
    variables = [solver.addVariable(lb=-highspy.kHighsInf, ub=highspy.kHighsInf)
                 for _ in range(DIM)]
    margin = solver.addVariable(lb=-highspy.kHighsInf, ub=highspy.kHighsInf, obj=-1)
    for row, base in zip(rows, fixed_rows):
        solver.addConstr(solver.qsum(float(v) * variables[j] for j, v in enumerate(row))
                         - margin >= -float(base))
    # For an integer point, the endpoint is 2 mod 4. This real branch uses >=2.
    solver.addConstr(solver.qsum(4 * (-1) ** j * variables[j] for j in range(DIM)) >= -2004)
    started = time.perf_counter()
    solver.run()
    solution = solver.getSolution()
    result = {"options": options, "status": str(solver.getModelStatus()),
              "value_valid": bool(solution.value_valid),
              "solver_seconds": time.perf_counter() - started}
    if solution.value_valid:
        u = np.array(solution.col_value[:DIM], dtype=float)
        result.update({"u_float": u.tolist(), "margin": float(solution.col_value[-1]),
                       "direct_minimum": float(np.min(rows @ u + fixed_rows)),
                       "u_abs_max": float(np.max(np.abs(u)))})
    return result


def metrics(np, u, rows, fixed_rows):
    a = coefficients_from_u([int(v) for v in u])
    values = rows @ u + fixed_rows
    return {"minimum_signed_sine": float(np.min(values)),
            "nonpositive_sign_rows": int(np.sum(values <= 0)),
            "endpoint": int(endpoint(a)), "Q0": int(jets(a)[0]),
            "Qprime0": int(jets(a)[1]), "max_abs_a": max(map(abs, a)),
            "max_abs_u": int(np.max(np.abs(u)))}


def repair(np, rows, fixed_rows, b, raw, cfg):
    """Monotone exact-integer coordinate moves for a floating hinge objective.

    When the tested coordinate moves cease improving, reproducible integer kicks
    start another descent. This is not a proof of coordinatewise optimality,
    enumeration, or an infeasibility procedure.
    """
    started = time.perf_counter()
    deadline = started + cfg["repair_seconds"]
    rng = np.random.default_rng(cfg["seed"])
    starts = []
    best_score = math.inf
    best_u = None
    total_steps = 0
    for attempt in range(cfg["restarts"]):
        if time.perf_counter() >= deadline:
            break
        scale = np.ones(N) if attempt % 2 == 0 else 1 / (b * b)
        matrix = np.vstack((rows * scale[:, None], (-1.0) ** np.arange(DIM)))
        constant = np.r_[scale * (fixed_rows - cfg["sine_margin"]), 501.0]
        if attempt < 2:
            u = np.rint(raw).astype(np.int64)
        else:
            u = np.floor(raw).astype(np.int64) + (rng.random(DIM) < raw - np.floor(raw))
        residual = matrix @ u + constant
        initial = metrics(np, u, rows, fixed_rows)
        initial_negative = np.minimum(residual, 0.0)
        local_best, local_u = float(initial_negative @ initial_negative), u.copy()
        kicks, steps = 0, 0
        for step in range(cfg["steps_per_restart"]):
            if time.perf_counter() >= deadline:
                break
            negative = np.minimum(residual, 0.0)
            loss = float(negative @ negative)
            if loss < local_best:
                local_best, local_u = loss, u.copy()
            if loss == 0:
                break
            active = residual < 0
            curvature = np.sum(matrix[active] ** 2, axis=0)
            gradient = matrix.T @ negative
            proposed = np.rint(-gradient / np.maximum(curvature, 1e-15))
            proposed = np.clip(proposed, -cfg["max_step"], cfg["max_step"]).astype(np.int64)
            proposed[proposed == 0] = np.where(gradient[proposed == 0] > 0, -1, 1)
            # Direct floating-point objective evaluations for the proposed moves.
            trial = np.minimum(residual[:, None] + matrix * proposed[None, :], 0.0)
            losses = np.sum(trial * trial, axis=0)
            index = int(np.argmin(losses))
            if float(losses[index]) < loss - 1e-10 * max(1.0, loss):
                delta = int(proposed[index])
                u[index] += delta
                residual += delta * matrix[:, index]
                steps += 1
                total_steps += 1
            elif kicks < cfg["kicks_per_restart"]:
                chosen = rng.choice(DIM, size=cfg["kick_coordinates"], replace=False)
                shifts = rng.choice([-1, 1], size=len(chosen))
                u[chosen] += shifts
                residual = matrix @ u + constant
                kicks += 1
            else:
                break
        # Refresh every reported score from exact integer u and original rows.
        final = metrics(np, local_u, rows, fixed_rows)
        # Compare starts in a common, unscaled squared violation objective.
        original = np.r_[rows @ local_u + fixed_rows - cfg["sine_margin"],
                         (final["endpoint"] - 2) / 4]
        common_loss = float(np.minimum(original, 0) @ np.minimum(original, 0))
        starts.append({"attempt": attempt, "loss_scaling": "raw" if attempt % 2 == 0 else "divide_by_trace_squared",
                       "initial": initial, "final": final, "descent_moves": steps,
                       "kicks": kicks, "common_loss": common_loss,
                       "local_scaled_loss": local_best, "u_integer": local_u.tolist()})
        if common_loss < best_score:
            best_score, best_u = common_loss, local_u.copy()
        print(json.dumps({"repair_attempt": attempt, "moves": steps, "kicks": kicks,
                          "final": final}), flush=True)
        if final["minimum_signed_sine"] > 0 and final["endpoint"] >= 2:
            best_u = local_u
            break
    return {"attempts": starts, "total_descent_moves": total_steps,
            "elapsed_seconds": time.perf_counter() - started,
            "soft_deadline_reached": time.perf_counter() >= deadline,
            "best_u_integer": None if best_u is None else best_u.tolist()}


def run(config_path):
    import numpy as np
    import highspy
    import flint

    cfg = json.loads(config_path.read_text(encoding="utf-8"))
    assert (cfg["p"], cfg["prefix_L"], cfg["Q0"], cfg["Qprime0"]) == (P, L, 0, -1)
    results = {"scope": "bounded exact-lattice proposal; no integer infeasibility claim",
               "configuration": cfg, "controls": controls(),
               "versions": {"numpy": np.__version__, "highspy": highspy.Highs().version(),
                            "python_flint": flint.__version__}}
    rows, fixed_rows, b, error = matrices(np)
    results["floating_grid_column_crosscheck_max_error"] = error
    lp = lp_proposal(np, highspy, rows, fixed_rows, cfg["lp_seconds"])
    results["branch_lp"] = lp
    print(json.dumps({"branch_lp": {k: v for k, v in lp.items() if k != "u_float"}}), flush=True)
    output = OUT / "jet_lattice.json"
    write_json(output, results)
    if not lp["value_valid"] or lp["direct_minimum"] <= 0:
        return
    rational_u = [Fraction(str(v)) for v in lp["u_float"]]
    rational_a = coefficients_from_u(rational_u)
    assert jets(rational_a) == (0, -1)
    real_check = interval_check(rational_a)
    results["real_branch_check"] = real_check
    if real_check["all_strict_signs_certified"] and real_check["endpoint_positive"]:
        write_json(HERE / "inputs" / "jet_lattice_real.json",
                   {"p": P, "prefix_L": L, "Q0": 0, "Qprime0": -1,
                    "u_rational": [str(v) for v in rational_u]})
    write_json(output, results)
    print(json.dumps({"rational_branch_strict": real_check["all_strict_signs_certified"],
                      "endpoint": real_check["endpoint"]}), flush=True)
    results["integer_repair"] = repair(np, rows, fixed_rows, b, np.array(lp["u_float"]), cfg)
    best = results["integer_repair"]["best_u_integer"]
    if best is not None:
        a = coefficients_from_u(best)
        assert all(type(v) is int for v in a) and jets(a) == (0, -1)
        results["best_integer_coefficients"] = a
        results["best_integer_metrics"] = metrics(np, np.array(best), rows, fixed_rows)
        check = interval_check(a)
        results["best_integer_check"] = check
        # Save the exact integer proposal before potentially expensive full evaluation.
        write_json(output, results)
        if check["all_strict_signs_certified"] and check["endpoint_positive"]:
            polynomial = lift(a)
            write_json(HERE / "inputs" / "jet_lattice_integer.json",
                       {"p": P, "prefix_L": L, "Q0": 0, "Qprime0": -1,
                        "u_integer": best, "coefficients_integer": a,
                        "polynomial_ascending": polynomial})
            sys.path.insert(0, str(HERE.parent / "Yin_J_G0156"))
            import sampler
            results["complete_measure_certificate"] = sampler.certify_polynomial(polynomial)
    write_json(output, results)
    print(json.dumps({"output": str(output), "integer_strict": bool(
        results.get("best_integer_check", {}).get("all_strict_signs_certified", False)),
        "integer_metrics": results.get("best_integer_metrics")}), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=HERE / "inputs" / "jet_lattice.json")
    parser.add_argument("--verify-real", type=Path)
    args = parser.parse_args()
    if args.verify_real:
        source = json.loads(args.verify_real.read_text(encoding="utf-8"))
        assert (source["p"], source["prefix_L"], source["Q0"], source["Qprime0"]) == (P, L, 0, -1)
        a = coefficients_from_u([Fraction(v) for v in source["u_rational"]])
        assert jets(a) == (0, -1)
        check = interval_check(a)
        assert check["endpoint_positive"] and check["all_strict_signs_certified"]
        write_json(OUT / "jet_lattice_real_verification.json", check)
        print(json.dumps({"exact_rational_branch_verified": True, "endpoint": check["endpoint"]}))
    else:
        run(args.config)


if __name__ == "__main__":
    main()
