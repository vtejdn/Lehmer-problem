"""One bounded numerical suggestion for the fixed D56 integer trace cell.

The controls command builds the model but never calls a solver.  Only run
launches the single formal search.  A hard supervisor charges child imports,
model construction, exact checking, full roots and journal writes to 120s.
"""

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parents[1] / "outputs" / HERE.name
INPUT = HERE / "trace56_cell.json"
LABEL = "trace56_fixed_cell_s56003"
SECONDS, SEED, NODES = 120, 56003, 100000
SMALL_MATRIX = 1e-9
OPTIONS = {"output_flag": False, "threads": 1, "random_seed": SEED, "mip_max_nodes": NODES,
           "presolve": "on", "parallel": "off", "mip_rel_gap": 0.0, "mip_abs_gap": 0.0,
           "mip_feasibility_tolerance": 1e-9, "primal_feasibility_tolerance": 1e-9,
           "small_matrix_value": SMALL_MATRIX}


class Journal:
    def __init__(self, stream, started):
        self.stream, self.started = stream, started

    def emit(self, kind, **values):
        self.stream.write(json.dumps({"kind": kind, "elapsed": time.perf_counter() - self.started, **values},
                                    separators=(",", ":"), allow_nan=False) + "\n")
        self.stream.flush()


def encode_fraction(value):
    return [value.numerator, value.denominator]


def relaxed_row(coefficients, rhs, bounds):
    """An outward floating relaxation on the complete bounded variable box."""
    scale = max(1, abs(rhs), *(abs(value) for value in coefficients))
    exact = [Fraction(value, scale) for value in coefficients]
    floating = [float(value) for value in exact]
    dropped = []
    for i, value in enumerate(floating):
        if value and abs(value) <= SMALL_MATRIX:
            dropped.append(i)
            floating[i] = 0.0
    error = sum(abs(Fraction(value) - target) * max(abs(lo), abs(hi))
                for value, target, (lo, hi) in zip(floating, exact, bounds))
    lower = Fraction(rhs, scale) - error
    rounded_lower = math.nextafter(float(lower), -math.inf)
    assert Fraction(rounded_lower) <= lower
    assert all(value == 0 or abs(value) > SMALL_MATRIX for value in floating)
    return {"exact_coefficients": coefficients, "exact_rhs": rhs, "positive_scale": scale,
            "floating_coefficients": floating, "floating_rhs": rounded_lower,
            "box_rounding_error_bound": encode_fraction(error), "dropped_columns": dropped}


def build_model(data):
    import highspy
    import numpy

    solver = highspy.Highs()
    for name, value in OPTIONS.items():
        if solver.setOptionValue(name, value) != highspy.HighsStatus.kOk:
            raise RuntimeError(f"unsupported HiGHS option: {name}")
    bounds = [list(pair) for pair in data["closed_simplex_height_box_integer_bounds"]]
    branch_counts = {name: len(mapping["nonzero_branches"]) for name, mapping in data["remainder_maps"].items()}
    bounds += [[0, 1] for _ in range(sum(branch_counts.values()))]
    variables = [solver.addVariable(lb=lo, ub=hi, type=highspy.HighsVarType.kInteger) for lo, hi in bounds]
    rows = []

    def add(coefficients, rhs, label):
        row = relaxed_row(coefficients, rhs, bounds)
        solver.addConstr(solver.qsum(value * variables[i] for i, value in enumerate(row["floating_coefficients"]) if value) >= row["floating_rhs"])
        rows.append({"label": label, **row})

    for i, (node, row) in enumerate(zip(data["nodes"], data["strict_sign_integer_rows"])):
        # Monic integer polynomials have no noninteger rational root.  At
        # those nodes >=0 is equivalent to >0 for exact integer candidates.
        threshold = 1 if node[1] == 1 else 0
        add(row[:-1] + [0] * sum(branch_counts.values()), threshold - row[-1], f"sign_{i}")
    cursor = 28
    for name, mapping in data["remainder_maps"].items():
        selectors = []
        for branch in mapping["nonzero_branches"]:
            row = branch["coefficients"] + [0] * sum(branch_counts.values())
            row[cursor] = branch["binary_coefficient"]
            add(row, branch["rhs"], f"{name}_remainder_{branch['component']}_sign_{branch['sign']}")
            selectors.append(cursor)
            cursor += 1
        row = [int(j in selectors) for j in range(len(variables))]
        add(row, 1, name + "_at_least_one_branch")
    assert cursor == len(variables) == 56 and len(rows) == 59
    assert solver.getNumCol() == 56 and solver.getNumRow() == 59
    metadata = {"highspy_version": solver.version(), "numpy_version": numpy.__version__,
                "variables": 56, "integer_free_variables": 28, "binary_selectors": 28,
                "constraints": 59, "options": OPTIONS, "objective": "constant zero feasibility",
                "variable_bounds": bounds, "rows": rows,
                "row_scope": "outward numerical relaxation of the exact integer formulation; no solver status is a proof",
                "minimum_nonzero_matrix_magnitude": min(abs(value) for row in rows for value in row["floating_coefficients"] if value),
                "explicitly_dropped_coefficients": sum(len(row["dropped_columns"]) for row in rows)}
    return solver, metadata


def rounding(raw):
    if len(raw) < 28 or not all(math.isfinite(value) for value in raw[:28]):
        return None, None
    free = [int(round(value)) for value in raw[:28]]
    return free, max(abs(value - integer) for value, integer in zip(raw[:28], free))


def candidate_payload(raw):
    raw = [float(value) for value in raw]
    free, distance = rounding(raw)
    polynomial = [1, *free, *reversed(free[:-1]), 1] if free is not None else None
    return {"raw_columns": [value if math.isfinite(value) else repr(value) for value in raw],
            "free_descending": free, "integer_rounding_max_distance": distance,
            "coefficients_ascending": polynomial}


def attach_incumbent_journal(solver, emit):
    """Preserve observed incumbents even if the supervisor kills before return."""
    def observe(event):
        emit("incumbent_observed", **candidate_payload(event.data_out.mip_solution),
             scope="observational improving-incumbent callback; exact checks and certificate pending")
    solver.cbMipImprovingSolution.subscribe(observe)
    return observe


def certificate_for(free):
    # This is the declared cross-J complete evaluator, with unchanged precision,
    # factorization, all-root contribution rules and structural interpretation.
    sys.path.insert(0, str(HERE.parent / "Yin_J_G0156"))
    import primitive_core_sampling as prior
    polynomial = prior.frozen.reciprocal_polynomial(free)
    certificate = prior.frozen.certify_polynomial(polynomial)
    structure = prior.structural_diagnostics(certificate, 56)
    verified = (not certificate["neutral"] and certificate["thresholds"]["6/5"] == "below"
                and prior.frozen.interval_fraction(certificate["measure_interval"][0]) > 1)
    return {"certificate": certificate, "structure": structure, "verified_target": verified}


def worker(started, events_path):
    deadline = started + SECONDS
    with events_path.open("x", encoding="utf-8") as stream:
        emit = Journal(stream, started).emit
        emit("configuration", protocol="S10-fixed-D56-all-real-trace-cell", seed=SEED,
             threads=1, node_cap=NODES, seconds=SECONDS, input=INPUT.name)
        try:
            import trace56_cell as exact
            data = json.loads(INPUT.read_text(encoding="utf-8"))
            checks = exact.check_input(data)
            emit("exact_input_checked", checks=checks)
            solver, model = build_model(data)
            emit("model", **model)
            attach_incumbent_journal(solver, emit)
            remaining = deadline - time.perf_counter()
            if remaining <= 0:
                emit("finish", reason="deadline_before_solver")
                return
            import highspy
            assert solver.setOptionValue("time_limit", remaining) == highspy.HighsStatus.kOk
            emit("solver_start", remaining_wall_seconds=remaining)
            # Exactly one run call; neither invalid suggestions nor timeouts
            # cause a restart, moved separator, different objective or no-good.
            solver.run()
            information = solver.getInfo()
            status = solver.modelStatusToString(solver.getModelStatus())
            solution = solver.getSolution()
            emit("solver_return", status=status, mip_node_count=information.mip_node_count,
                 value_valid=solution.value_valid, solver_run_seconds=solver.getRunTime())
            if not solution.value_valid:
                emit("finish", reason="numerical_status_without_candidate_unresolved", solver_status=status)
                return
            payload = candidate_payload(solution.col_value)
            free = payload["free_descending"]
            emit("candidate", **payload,
                 scope="numerical suggestion retained before exact verification")
            if free is None or time.perf_counter() >= deadline:
                emit("finish", reason="candidate_unverified_nonfinite_or_deadline")
                return
            checked = exact.exact_check(free, data)
            emit("exact_candidate_check", result=checked)
            if not checked["accepted"]:
                emit("finish", reason="numerical_candidate_rejected_exactly")
                return
            if time.perf_counter() >= deadline:
                emit("finish", reason="exact_candidate_root_certificate_pending_deadline")
                return
            certified = certificate_for(free)
            emit("whole_certificate", **certified)
            finished = time.perf_counter()
            if certified["verified_target"] and finished < deadline:
                emit("verified_commit", elapsed=finished - started,
                     scope="exact signs and both nonzero remainders plus complete whole target certificate")
                emit("finish", reason="verified_target")
            else:
                emit("finish", reason="root_certificate_unresolved_or_over_budget")
        except Exception as error:
            emit("worker_failure", error=repr(error))
            raise


def read_events(path):
    if not path.is_file():
        return []
    result = []
    with path.open(encoding="utf-8") as stream:
        for line in stream:
            try:
                result.append(json.loads(line))
            except json.JSONDecodeError:
                break
    return result


def describe(events, supervision):
    by_kind = {event["kind"]: event for event in events}
    candidate = by_kind.get("candidate")
    incumbents = [event for event in events if event["kind"] == "incumbent_observed"]
    exact = by_kind.get("exact_candidate_check")
    certificate = by_kind.get("whole_certificate")
    commit = by_kind.get("verified_commit")
    on_time = bool(commit and commit["elapsed"] < SECONDS and candidate and exact and exact["result"]["accepted"]
                   and certificate and certificate["verified_target"])
    failed = bool("worker_failure" in by_kind or (not supervision["killed_at_cap"] and supervision["returncode"] != 0))
    if "configuration" not in by_kind:
        failed = True
    reason = "verified_target" if on_time else "worker_failure" if failed else "deadline_incomplete" if supervision["killed_at_cap"] else by_kind.get("finish", {}).get("reason", "early_exit_unresolved")
    return {"protocol": "S10-fixed-D56-all-real-trace-cell", "formal_parameters": {"seed": SEED, "node_cap": NODES, "threads": 1, "seconds": SECONDS},
            "supervision": supervision, "termination_reason": reason, "on_time_verified_target": on_time,
            "observed_elapsed_seconds": min(SECONDS, supervision["elapsed_seconds"]),
            "solver_return": by_kind.get("solver_return"), "candidate": candidate,
            "solver_incumbent_observations": incumbents,
            "retained_candidate_for_later_check": candidate or (incumbents[-1] if incumbents else None),
            "exact_candidate_check": exact, "whole_certificate": certificate,
            "verification_scope": "Later checking cannot add historical on-time credit; numerical infeasibility and timeout are not exact exclusions",
            "original_event_count": len(events), "worker_failure": by_kind.get("worker_failure"),
            "no_configuration_observed": "configuration" not in by_kind}


def supervise_child(command, started, seconds):
    """Shared by the one formal child and the separate nonmathematical control."""
    killed, returncode, stderr = False, None, b""
    try:
        process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                                   creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    except OSError as error:
        returncode, stderr = -1, repr(error).encode()
    else:
        try:
            _, stderr = process.communicate(timeout=max(0, seconds - (time.perf_counter() - started)))
        except subprocess.TimeoutExpired:
            killed = True
            process.kill()
            _, stderr = process.communicate()
        returncode = process.returncode
    return {"killed_at_cap": killed, "returncode": returncode, "elapsed_seconds": time.perf_counter() - started,
            "stderr": stderr.decode(errors="replace"), "postrun_summary": "bookkeeping only; no solving or certification"}


def run():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    journal, destination = OUTPUT / (LABEL + ".jsonl"), OUTPUT / (LABEL + ".json")
    if journal.exists() or destination.exists():
        raise FileExistsError("the fixed formal identity already exists; no automatic repeat")
    started = time.perf_counter()
    command = [sys.executable, "-B", str(Path(__file__).resolve()), "_worker", "--started", str(started), "--events", str(journal)]
    supervision = supervise_child(command, started, SECONDS)
    record = describe(read_events(journal), supervision)
    record["events_file"] = journal.name
    write_new(destination, record)
    print(json.dumps({key: record[key] for key in ("termination_reason", "on_time_verified_target", "observed_elapsed_seconds")}))


def lifecycle_child(started, path):
    with path.open("x", encoding="utf-8") as stream:
        writer = Journal(stream, started)
        writer.emit("configuration", protocol="control_only_trace56_supervisor", formal_identity=False)
        writer.emit("candidate", **candidate_payload([0.0] * 56),
                    scope="synthetic bookkeeping input, no solver or mathematical evaluation")
        time.sleep(2)
        writer.emit("control_after_deadline", scope="must be absent under the 0.75s control supervisor")


def lifecycle_control(destination):
    journal = destination.with_suffix(".jsonl")
    if destination.exists() or journal.exists():
        raise FileExistsError("preserve existing lifecycle control")
    destination.parent.mkdir(parents=True, exist_ok=True)
    seconds, started = 0.75, time.perf_counter()
    command = [sys.executable, "-B", str(Path(__file__).resolve()), "_lifecycle_child", "--started", str(started), "--events", str(journal)]
    supervision = supervise_child(command, started, seconds)
    events = read_events(journal)
    assert supervision["killed_at_cap"] and supervision["returncode"] != 0
    assert supervision["elapsed_seconds"] >= seconds
    assert [event["kind"] for event in events] == ["configuration", "candidate"]
    assert all(event["elapsed"] < seconds for event in events)
    record = describe(events, supervision)
    assert record["retained_candidate_for_later_check"]["coefficients_ascending"] == [1] + [0] * 55 + [1]
    assert not record["on_time_verified_target"]
    missing = OUTPUT / "trace56_control_nonexistent_interpreter.exe"
    assert not missing.exists()
    failed = supervise_child([str(missing)], time.perf_counter(), seconds)
    assert not failed["killed_at_cap"] and failed["returncode"] == -1 and failed["stderr"]
    assert describe([], failed)["termination_reason"] == "worker_failure"
    result = {"protocol": "control_only_trace56_supervisor", "formal_identity": False,
              "real_child_budget_seconds": seconds, "real_subprocesses_started": 1,
              "supervision": supervision, "retained_events": events, "startup_failure": failed,
              "checks": {"same_Popen_timeout_kill_path": "pass", "same_writer_flush": "pass",
                         "before_cap_candidate_retained": "pass", "after_cap_marker_absent": "pass",
                         "on_time_target_credit": False, "actual_Popen_startup_failure": "pass"},
              "solver_run_calls": 0, "root_certifications": 0}
    write_new(destination, result)
    print(json.dumps(result, indent=2))


def controls():
    from types import SimpleNamespace
    import trace56_cell as exact
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    checks = exact.check_input(data)
    solver, model = build_model(data)
    # No call to solver.run occurs in these controls.
    for row in model["rows"]:
        scale = row["positive_scale"]
        error = sum(abs(Fraction(f) - Fraction(a, scale)) * max(abs(lo), abs(hi))
                    for f, a, (lo, hi) in zip(row["floating_coefficients"], row["exact_coefficients"], model["variable_bounds"]))
        assert encode_fraction(error) == row["box_rounding_error_bound"]
        assert Fraction(row["floating_rhs"]) <= Fraction(row["exact_rhs"], scale) - error
    assert [i for i, node in enumerate(data["nodes"]) if node[1] == 1] == [0, 9, 27]
    for name, mapping in data["remainder_maps"].items():
        for branch in mapping["nonzero_branches"]:
            j, sign, big_m = branch["component"], branch["sign"], branch["big_M"]
            lower, upper = mapping["component_bounds"][j]
            assert (lower if sign == 1 else -upper) >= 1 - big_m
    free, distance = rounding([float(x) + 1e-10 for x in data["parent_free_descending"]] + [0.0] * 28)
    assert free == data["parent_free_descending"] and distance < 1e-8
    assert not exact.exact_check(free, data)["accepted"]
    assert rounding([float("nan")] * 56) == (None, None)
    recorded = []
    callback = attach_incumbent_journal(solver, lambda kind, **values: recorded.append({"kind": kind, "elapsed": 119.9, **values}))
    callback(SimpleNamespace(data_out=SimpleNamespace(mip_solution=[float(x) for x in free] + [0.0] * 28)))
    assert len(recorded) == 1 and recorded[0]["free_descending"] == free
    assert recorded[0]["coefficients_ascending"] == exact.whole_polynomial(free)
    supervision = {"killed_at_cap": True, "returncode": -9, "elapsed_seconds": 120.01, "stderr": "mechanical fixture"}
    config = {"kind": "configuration", "elapsed": .1}
    candidate = {"kind": "candidate", "elapsed": 119.9, "free_descending": free}
    missing = describe([], {**supervision, "killed_at_cap": False, "returncode": -1})
    assert missing["termination_reason"] == "worker_failure" and missing["candidate"] is None
    pending = describe([config, candidate], supervision)
    assert pending["candidate"] == candidate and not pending["on_time_verified_target"]
    inside_solver = describe([config, *recorded], supervision)
    assert inside_solver["candidate"] is None and inside_solver["retained_candidate_for_later_check"] == recorded[0]
    assert not inside_solver["on_time_verified_target"]
    # Synthetic statuses only test bookkeeping, not a certificate assertion.
    accepted = {"kind": "exact_candidate_check", "elapsed": 119.91, "result": {"accepted": True}}
    certified = {"kind": "whole_certificate", "elapsed": 119.95, "verified_target": True, "mechanical_fixture_only": True}
    assert not describe([config, candidate, accepted, certified], supervision)["on_time_verified_target"]
    assert not describe([config, candidate, accepted, certified, {"kind": "verified_commit", "elapsed": 120.001}], supervision)["on_time_verified_target"]
    assert describe([config, candidate, accepted, certified, {"kind": "verified_commit", "elapsed": 119.99}], supervision)["on_time_verified_target"]
    return {"exact_input_checks": checks, "numerical_model": model,
            "controls": {"outward_float_rows_over_complete_box": "pass", "exact_big_M_deactivation": "pass",
                         "parent_candidate_old_core_rejection": "pass", "nonfinite_candidate": "retained as unverified",
                         "startup_failure_and_pending_candidate": "pass", "missing_or_after_deadline_commit_no_yield": "pass"},
            "complete_predeadline_mechanical_commit_has_credit": True,
            "observational_incumbent_callback_registered_and_mechanically_checked": True,
            "solver_run_calls": 0, "real_subprocess_controls": 0, "new_root_certifications": 0,
            "formal_search": "not run"}


def write_new(path, value):
    if path.exists():
        raise FileExistsError("preserve existing observation or check output")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("run")
    commands.add_parser("controls").add_argument("--output", type=Path, required=True)
    commands.add_parser("lifecycle-control").add_argument("--output", type=Path, required=True)
    internal = commands.add_parser("_worker")
    internal.add_argument("--started", type=float, required=True)
    internal.add_argument("--events", type=Path, required=True)
    internal_control = commands.add_parser("_lifecycle_child")
    internal_control.add_argument("--started", type=float, required=True)
    internal_control.add_argument("--events", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "run":
        run()
    elif args.command == "_worker":
        worker(args.started, args.events)
    elif args.command == "_lifecycle_child":
        lifecycle_child(args.started, args.events)
    elif args.command == "lifecycle-control":
        lifecycle_control(args.output)
    else:
        if args.output.exists():
            raise FileExistsError("preserve previous controls")
        result = controls()
        write_new(args.output, result)
        print(json.dumps({key: value for key, value in result.items() if key != "numerical_model"}, indent=2))
