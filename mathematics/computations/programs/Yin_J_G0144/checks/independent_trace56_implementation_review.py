"""Independent model, retained-interface and mechanical lifecycle checks.

No real solver.run, factorization or numerical root certification is allowed.
Worker fixtures replace the solver and certificate with marked mechanical
stubs; they exercise actual control flow, writer and summarizer, not discovery.
"""

import argparse
from copy import deepcopy
from fractions import Fraction as Q
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace
from unittest.mock import patch

HERE = Path(__file__).resolve().parents[1]
OUTPUT = HERE.parents[1] / "outputs" / HERE.name
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "Yin_J_G0156"))
import highspy
import trace56_cell as exact
import trace56_milp as program
import primitive_core_sampling as prior


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def equal(a, b):
    assert json.dumps(a, sort_keys=True, separators=(",", ":")) == json.dumps(
        b, sort_keys=True, separators=(",", ":"))


def model_checks(data):
    # The earlier independent rational reconstruction validates every exact
    # sign row, coordinate box and remainder map consumed here.
    expected = []
    bounds = data["closed_simplex_height_box_integer_bounds"] + [[0, 1]]*28
    for i, (node, row) in enumerate(zip(data["nodes"], data["strict_sign_integer_rows"])):
        assert Q(*node).denominator == node[1]
        threshold = 1 if Q(*node).denominator == 1 else 0
        expected.append((f"sign_{i}", row[:-1]+[0]*28, threshold-row[-1]))
    cursor = 28
    for name in ("qL", "qH"):
        selectors = []
        for branch in data["remainder_maps"][name]["nonzero_branches"]:
            row = branch["coefficients"]+[0]*28
            row[cursor] = branch["binary_coefficient"]
            expected.append((f"{name}_remainder_{branch['component']}_sign_{branch['sign']}",
                             row, branch["rhs"]))
            selectors.append(cursor)
            cursor += 1
        expected.append((name+"_at_least_one_branch", [int(i in selectors) for i in range(56)], 1))
    assert cursor == 56 and len(expected) == 59
    with patch.object(highspy.Highs, "run", side_effect=AssertionError("real solver run forbidden")):
        solver, metadata = program.build_model(data)
    assert metadata["variable_bounds"] == bounds
    lp = solver.getLp()
    assert lp.num_col_ == 56 and lp.num_row_ == 59
    assert all(x == highspy.HighsVarType.kInteger for x in lp.integrality_)
    assert list(lp.col_lower_) == [x[0] for x in bounds]
    assert list(lp.col_upper_) == [x[1] for x in bounds]
    assert list(lp.col_cost_) == [0.0]*56 and lp.offset_ == 0
    assert all(math.isinf(x) and x > 0 for x in lp.row_upper_)
    assert lp.a_matrix_.format_ == highspy.MatrixFormat.kRowwise
    for name, value in program.OPTIONS.items():
        status, actual = solver.getOptionValue(name)
        assert status == highspy.HighsStatus.kOk and actual == value
    assert solver.getOptionValue("threads")[1] == 1
    assert solver.getOptionValue("random_seed")[1] == 56003
    assert solver.getOptionValue("mip_max_nodes")[1] == 100000
    nonzero = []
    for i, ((name, coefficients, rhs), row) in enumerate(zip(expected, metadata["rows"])):
        assert row["label"] == name
        assert row["exact_coefficients"] == coefficients and row["exact_rhs"] == rhs
        scale = row["positive_scale"]
        assert scale == max(1, abs(rhs), *map(abs, coefficients))
        floats = []
        for coefficient in coefficients:
            value = float(Q(coefficient, scale))
            floats.append(0.0 if value and abs(value) <= 1e-9 else value)
        assert row["floating_coefficients"] == floats
        differences = [Q(f)-Q(a, scale) for f, a in zip(floats, coefficients)]
        error = sum(abs(delta)*max(abs(lo), abs(hi)) for delta, (lo, hi) in zip(differences, bounds))
        assert row["box_rounding_error_bound"] == [error.numerator, error.denominator]
        assert Q(row["floating_rhs"]) <= Q(rhs, scale)-error
        # Also check against the sharper exact minimum affine perturbation
        # over the actual asymmetric box.
        minimum_delta = sum(delta*(lo if delta >= 0 else hi) for delta, (lo, hi) in zip(differences, bounds))
        assert Q(row["floating_rhs"]) <= Q(rhs, scale)+minimum_delta
        assert row["dropped_columns"] == [j for j, (a, f) in enumerate(zip(coefficients, floats)) if a and f == 0]
        dense = [0.0]*56
        matrix = lp.a_matrix_
        for k in range(matrix.start_[i], matrix.start_[i+1]):
            dense[matrix.index_[k]] += matrix.value_[k]
        assert dense == floats and lp.row_lower_[i] == row["floating_rhs"]
        nonzero.extend(abs(x) for x in floats if x)
    saved = read(OUTPUT/"trace56_milp_controls_v3.json")
    equal(metadata, saved["numerical_model"])
    checks = exact.check_input(data)
    equal(checks, saved["exact_input_checks"])
    equal(checks, read(OUTPUT/"trace56_cell_controls.json"))
    # Exercise the stated coefficient-dropping protection, unused in this
    # actual matrix, with one bounded mechanical row.
    dropped = program.relaxed_row([1, 10**12], 7, [[-4, 4], [0, 1]])
    assert dropped["dropped_columns"] == [0]
    assert Q(dropped["floating_rhs"]) <= Q(7, 10**12)-Q(4, 10**12)
    return solver, {"actual_model_and_all_59_rows_match_saved_control": True,
                    "backend_matrix_bounds_integrality_objective_options_match": True,
                    "integer_nodes": [i for i, node in enumerate(data["nodes"]) if Q(*node).denominator == 1],
                    "minimum_nonzero_matrix_magnitude": min(nonzero),
                    "actual_dropped_coefficients": metadata["explicitly_dropped_coefficients"],
                    "synthetic_dropped_coefficient_outer_bound": True,
                    "backend_solver_runs": 0}


def payload_checks(data, solver):
    parent = data["parent_free_descending"]
    raw = [float(x)+1e-10 for x in parent]+[0.0]*28
    payload = program.candidate_payload(raw)
    assert payload["free_descending"] == parent
    assert payload["coefficients_ascending"] == data["parent_ascending"]
    assert payload["integer_rounding_max_distance"] < 1e-8
    assert not exact.exact_check(payload["free_descending"], data)["accepted"]
    for bad in ([], [0.0]*27, [float("nan")]*56, [float("inf")]*56, [-float("inf")]*56):
        candidate = program.candidate_payload(bad)
        assert candidate["free_descending"] is None and candidate["coefficients_ascending"] is None
        json.dumps(candidate, allow_nan=False)
    out_of_box = program.candidate_payload([1000.0]*56)
    assert not exact.exact_check(out_of_box["free_descending"], data)["accepted"]
    # Invoke the actual installed callback dispatch, without solver execution.
    events = []
    program.attach_incumbent_journal(solver, lambda kind, **values: events.append({"kind": kind, **values}))
    before = deepcopy(raw)
    solver.cbMipImprovingSolution.fire(solver.cbMipImprovingSolution.callback_type, "mechanical fixture",
                                      SimpleNamespace(mip_solution=raw), None)
    assert raw == before and len(events) == 1
    assert events[0]["kind"] == "incumbent_observed"
    assert events[0]["coefficients_ascending"] == data["parent_ascending"]
    raw[0] = 999.0
    assert events[0]["raw_columns"][0] == before[0]
    return {"near_integer_parent_retained_then_rejected_exactly": True,
            "five_short_or_nonfinite_inputs_retained_without_target": True,
            "out_of_height_input_rejected": True,
            "installed_callback_dispatch_payload_is_detached": True,
            "live_solver_callback_observation": False}


def retained_certificate_interface():
    source = read(HERE.parent/"Yin_J_G0156"/"inputs"/"primitive_root_diagnostics.json")
    witness = source["lower_tail_witnesses"]["11542"]
    certificate = witness["certificate"]
    free = certificate["coefficients_ascending"][1:29]
    calls = []
    def retained_only(polynomial):
        assert polynomial == certificate["coefficients_ascending"]
        calls.append(polynomial)
        return deepcopy(certificate)
    with patch.object(prior.frozen, "certify_polynomial", side_effect=retained_only):
        replay = program.certificate_for(free)
    equal(replay["certificate"], certificate)
    for key, value in replay["structure"].items():
        equal(value, witness["diagnostics"][key])
    assert len(calls) == 1 and not replay["verified_target"]
    # Predicate boundary controls contain no mathematical certificate claim.
    fixture = deepcopy(certificate)
    fixture["thresholds"]["6/5"] = "below"
    fixture["measure_interval"][0] = [3, -1]
    with patch.object(prior.frozen, "certify_polynomial", return_value=fixture), \
         patch.object(prior, "structural_diagnostics", return_value={"mechanical_fixture": True}):
        assert program.certificate_for(free)["verified_target"]
        fixture["measure_interval"][0] = [1, 0]
        assert not program.certificate_for(free)["verified_target"]
        fixture["measure_interval"][0] = [3, -1]
        fixture["neutral"] = True
        assert not program.certificate_for(free)["verified_target"]
        fixture["neutral"] = False
        fixture["thresholds"]["6/5"] = "unresolved"
        assert not program.certificate_for(free)["verified_target"]
    return {"actual_retained_full_certificate_replayed": 11542,
            "actual_structure_fields_match_retained_diagnostics": True,
            "actual_above_threshold_certificate_rejected": True,
            "four_mechanical_target_predicate_boundaries": True,
            "new_factorizations_and_root_certifications": 0}


class Callback:
    def subscribe(self, callback):
        self.callback = callback


def worker_fixture(mode, directory, data):
    clock = SimpleNamespace(now=1.0)
    calls = {"mechanical_solver_runs": 0, "mechanical_certificate_calls": 0, "exact_check_calls": 0}
    raw = list(map(float, data["parent_free_descending"]))+[0.0]*28
    if mode == "nonfinite":
        raw[0] = float("nan")
    class Solver:
        cbMipImprovingSolution = Callback()
        def setOptionValue(self, name, value):
            assert name == "time_limit" and 0 < value <= 120
            return highspy.HighsStatus.kOk
        def run(self):
            calls["mechanical_solver_runs"] += 1
            self.cbMipImprovingSolution.callback(SimpleNamespace(data_out=SimpleNamespace(mip_solution=raw)))
            if mode == "solver_failure":
                raise RuntimeError("independent mechanical solver failure")
            if mode == "candidate_after_deadline":
                clock.now = 120.001
        def getInfo(self):
            return SimpleNamespace(mip_node_count=0)
        def modelStatusToString(self, status):
            return status
        def getModelStatus(self):
            return "mechanical status only"
        def getSolution(self):
            return SimpleNamespace(value_valid=mode != "no_solution", col_value=raw)
        def getRunTime(self):
            return 0.0
    def build(_):
        if mode == "model_failure":
            raise RuntimeError("independent mechanical model failure")
        if mode == "deadline_before_solver":
            clock.now = 120.001
        return Solver(), {"independent_mechanical_fixture_only": True}
    real_check = exact.exact_check
    def checked(free, frozen):
        calls["exact_check_calls"] += 1
        if mode == "parent_rejected":
            return real_check(free, frozen)
        if mode == "exact_check_after_deadline":
            clock.now = 120.001
        return {"accepted": True, "independent_mechanical_fixture_only": True}
    def certified(_):
        calls["mechanical_certificate_calls"] += 1
        if mode == "certificate_failure":
            raise RuntimeError("independent mechanical certificate failure")
        if mode == "certificate_after_deadline":
            clock.now = 120.001
        return {"verified_target": mode != "certificate_unresolved", "independent_mechanical_fixture_only": True}
    path = directory/(mode+".jsonl")
    selected_input = program.INPUT
    if mode == "missing_input":
        selected_input = directory/"missing_input_native.json"
    elif mode == "malformed_input":
        selected_input = directory/"malformed_input_native.json"
        selected_input.write_text("{", encoding="utf-8")
    input_check = {"side_effect": ValueError("independent mechanical exact-input failure")} if mode == "input_check_failure" else {
        "return_value": {"independent_mechanical_fixture_only": True}}
    raised = False
    with patch.object(program.time, "perf_counter", side_effect=lambda: clock.now), \
         patch.object(program, "INPUT", selected_input), \
         patch.object(exact, "check_input", **input_check), \
         patch.object(program, "build_model", side_effect=build), \
         patch.object(exact, "exact_check", side_effect=checked), \
         patch.object(program, "certificate_for", side_effect=certified):
        try:
            program.worker(0.0, path)
        except Exception:
            raised = True
    assert raised == (mode in {"missing_input", "malformed_input", "input_check_failure",
                               "model_failure", "solver_failure", "certificate_failure"})
    events = program.read_events(path)
    supervision = {"killed_at_cap": False, "returncode": 1 if raised else 0,
                   "elapsed_seconds": clock.now, "stderr": "independent mechanical fixture"}
    summary = program.describe(events, supervision)
    expected = {
        "missing_input": "worker_failure",
        "malformed_input": "worker_failure",
        "input_check_failure": "worker_failure",
        "deadline_before_solver": "deadline_before_solver",
        "model_failure": "worker_failure",
        "solver_failure": "worker_failure",
        "no_solution": "numerical_status_without_candidate_unresolved",
        "nonfinite": "candidate_unverified_nonfinite_or_deadline",
        "candidate_after_deadline": "candidate_unverified_nonfinite_or_deadline",
        "parent_rejected": "numerical_candidate_rejected_exactly",
        "exact_check_after_deadline": "exact_candidate_root_certificate_pending_deadline",
        "certificate_after_deadline": "root_certificate_unresolved_or_over_budget",
        "certificate_unresolved": "root_certificate_unresolved_or_over_budget",
        "certificate_failure": "worker_failure",
        "complete_mechanical_commit": "verified_target",
    }[mode]
    assert summary["termination_reason"] == expected
    assert summary["on_time_verified_target"] == (mode == "complete_mechanical_commit")
    assert calls["mechanical_solver_runs"] == (0 if mode in {"missing_input", "malformed_input", "input_check_failure",
                                                           "model_failure", "deadline_before_solver"} else 1)
    if mode in {"solver_failure", "no_solution"}:
        assert summary["candidate"] is None
        assert summary["retained_candidate_for_later_check"]["kind"] == "incumbent_observed"
    if mode in {"certificate_failure", "certificate_after_deadline", "certificate_unresolved", "exact_check_after_deadline"}:
        assert summary["candidate"]["coefficients_ascending"] == data["parent_ascending"]
        assert summary["exact_candidate_check"]["result"]["accepted"]
    if mode == "complete_mechanical_commit":
        for truncated in (events[:events.index(next(e for e in events if e["kind"] == "whole_certificate"))],
                          [e for e in events if e["kind"] not in {"verified_commit", "finish"}]):
            assert not program.describe(truncated, supervision)["on_time_verified_target"]
        for late_time in (120.0, 120.001):
            delayed = deepcopy(events)
            next(e for e in delayed if e["kind"] == "verified_commit")["elapsed"] = late_time
            assert not program.describe(delayed, supervision)["on_time_verified_target"]
    return {"fixture": mode, "termination_reason": expected, **calls,
            "on_time_mechanical_credit": summary["on_time_verified_target"],
            "retained_candidate_kind": (summary["retained_candidate_for_later_check"] or {}).get("kind"),
            "event_kinds": [e["kind"] for e in events], "new_mathematical_evaluation": False}


def retention_checks(directory):
    for stem in ("trace56_supervisor_control", "independent_trace56_supervisor_control"):
        result = read(OUTPUT/(stem+".json"))
        events = program.read_events(OUTPUT/(stem+".jsonl"))
        equal(events, result["retained_events"])
        assert len(events) == 2 and events[1]["kind"] == "candidate"
        assert all(e["elapsed"] < .75 for e in events)
        assert result["supervision"]["killed_at_cap"] and result["supervision"]["elapsed_seconds"] >= .75
        summary = program.describe(events, result["supervision"])
        assert not summary["on_time_verified_target"]
        assert summary["retained_candidate_for_later_check"]["coefficients_ascending"] == [1]+[0]*55+[1]
        assert program.describe([], result["startup_failure"])["termination_reason"] == "worker_failure"
    prefix = directory/"truncated_prefix.jsonl"
    complete = [{"kind": "configuration", "elapsed": 0.1}, {"kind": "candidate", "elapsed": 1.0, "free_descending": [0]*28}]
    prefix.write_text("".join(json.dumps(e)+"\n" for e in complete)+'{"kind":"whole_certificate",', encoding="utf-8")
    equal(program.read_events(prefix), complete)
    missing = program.read_events(directory/"absent.jsonl")
    assert missing == []
    # Both occupied formal-identity guard conditions are exercised using an
    # isolated reviewer output directory; the real formal identity is untouched.
    guard = directory/"identity_guard"
    guard.mkdir()
    for suffix in (".jsonl", ".json"):
        occupied = guard/(program.LABEL+suffix)
        occupied.write_text("independent identity guard fixture", encoding="utf-8")
        with patch.object(program, "OUTPUT", guard), \
             patch.object(program, "supervise_child", side_effect=AssertionError("launch forbidden")):
            try:
                program.run()
            except FileExistsError:
                pass
            else:
                raise AssertionError("occupied identity permitted")
        occupied.unlink()
    return {"author_and_independent_real_lifecycle_journals_match": True,
            "partial_tail_preserves_complete_prefix": True,
            "missing_journal_read_is_empty": True,
            "both_occupied_identity_guards_reject_before_launch": True,
            "real_short_child_budget_seconds": 0.75}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT/"independent_trace56_implementation_review.json")
    args = parser.parse_args()
    fixtures = args.output.with_suffix("")
    if args.output.exists() or fixtures.exists():
        raise FileExistsError("preserve independent review results")
    fixtures.mkdir(parents=True)
    data = read(program.INPUT)
    solver, model = model_checks(data)
    result = {"scope": "Independent fixed implementation and bounded controls; no formal solver/search or new roots.",
              "model": model, "payload_and_callback": payload_checks(data, solver),
              "retained_certificate_interface": retained_certificate_interface()}
    modes = ("missing_input", "malformed_input", "input_check_failure",
             "deadline_before_solver", "model_failure", "solver_failure", "no_solution", "nonfinite",
             "candidate_after_deadline", "parent_rejected", "exact_check_after_deadline",
             "certificate_after_deadline", "certificate_unresolved", "certificate_failure", "complete_mechanical_commit")
    result["worker_mechanical_fixtures"] = [worker_fixture(mode, fixtures, data) for mode in modes]
    result["retention"] = retention_checks(fixtures)
    result["backend_solver_run_calls"] = 0
    result["new_factorizations_and_numerical_root_solves"] = 0
    program.write_new(args.output, result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
