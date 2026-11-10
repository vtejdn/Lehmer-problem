"""Read-only exact comparison of the one retained D56 formal observation.

No author program, solver, polynomial library or root evaluator is imported.
"""

import argparse
from collections import Counter
from decimal import Decimal
from fractions import Fraction
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
OUTPUT = HERE.parents[1] / "outputs" / HERE.name
STEM = "trace56_fixed_cell_s56003"
PROTOCOL = "S10-fixed-D56-all-real-trace-cell"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON member: "+key)
        result[key] = value
    return result


def invalid_constant(value):
    raise ValueError("nonfinite JSON constant: "+value)


def decode(text, decimal=False):
    return json.loads(text, object_pairs_hook=unique_object,
                      parse_float=Decimal if decimal else float, parse_constant=invalid_constant)


def read(path, decimal=False):
    return decode(Path(path).read_text(encoding="utf-8"), decimal)


def exact_equal(left, right, path="$"):
    assert type(left) is type(right), (path, type(left), type(right))
    if isinstance(left, dict):
        assert left.keys() == right.keys(), path
        for key in left:
            exact_equal(left[key], right[key], path+"."+key)
    elif isinstance(left, list):
        assert len(left) == len(right), path
        for index, (a, b) in enumerate(zip(left, right)):
            exact_equal(a, b, path+f"[{index}]")
    elif isinstance(left, float):
        assert math.isfinite(left) and math.isfinite(right) and left.hex() == right.hex(), path
    else:
        assert left == right, (path, left, right)


def scalar_statistics(value):
    counts = Counter()
    maximum_digits = 0
    def visit(x):
        nonlocal maximum_digits
        counts[type(x).__name__] += 1
        if type(x) is int:
            maximum_digits = max(maximum_digits, len(str(abs(x))))
        elif isinstance(x, dict):
            for child in x.values():
                visit(child)
        elif isinstance(x, list):
            for child in x:
                visit(child)
    visit(value)
    return {"value_type_counts": dict(sorted(counts.items())), "maximum_integer_decimal_digits": maximum_digits}


def review():
    summary_path = OUTPUT/(STEM+".json")
    journal_path = OUTPUT/(STEM+".jsonl")
    native_path = HERE/"trace56_observation.json"
    summary = read(summary_path)
    native = read(native_path)
    raw = journal_path.read_text(encoding="utf-8")
    assert raw.endswith("\n")
    lines = raw.splitlines()
    assert len(lines) == 6 and all(line.strip() for line in lines)
    events = [decode(line) for line in lines]
    assert set(native) == {"protocol", "fixed_input", "original_output_stem", "summary", "events"}
    assert native["protocol"] == PROTOCOL
    assert native["fixed_input"] == "trace56_cell.json"
    assert native["original_output_stem"] == STEM
    exact_equal(native["summary"], summary)
    exact_equal(native["events"], events)
    # Repeat preservation comparisons before binary conversion, so coincident
    # double rounding cannot hide a changed decimal value in the native copy.
    decimal_native = read(native_path, True)
    exact_equal(decimal_native["summary"], read(summary_path, True))
    exact_equal(decimal_native["events"], [decode(line, True) for line in lines])
    kinds = [e["kind"] for e in events]
    assert kinds == ["configuration", "exact_input_checked", "model", "solver_start", "solver_return", "finish"]
    config, checked, model, started, returned, finished = events
    cell = read(HERE/"trace56_cell.json")
    parameters = {"seed": 56003, "threads": 1, "node_cap": 100000, "seconds": 120}
    assert cell["formal_parameters"] == {"seed": 56003, "threads": 1, "node_cap": 100000,
                                         "wall_seconds_from_prelaunch": 120}
    expected_config = {"kind": "configuration", "elapsed": config["elapsed"], "protocol": PROTOCOL,
                       **parameters, "input": "trace56_cell.json"}
    exact_equal(config, expected_config)
    assert cell["protocol"] == PROTOCOL and (cell["degree"], cell["trace_degree"], cell["height"]) == (56, 28, 4)
    controls = read(OUTPUT/"trace56_milp_controls_v3.json")
    exact_equal(checked["checks"], controls["exact_input_checks"])
    actual_model = {key: value for key, value in model.items() if key not in {"kind", "elapsed"}}
    exact_equal(actual_model, controls["numerical_model"])
    exact_equal({key: value for key, value in read(native_path, True)["events"][2].items()
                 if key not in {"kind", "elapsed"}},
                read(OUTPUT/"trace56_milp_controls_v3.json", True)["numerical_model"])
    assert len(model["rows"]) == 59 and len(model["variable_bounds"]) == 56
    assert model["options"]["random_seed"] == parameters["seed"]
    assert model["options"]["threads"] == parameters["threads"]
    assert model["options"]["mip_max_nodes"] == parameters["node_cap"]
    assert model["highspy_version"] == "1.15.1" and model["numpy_version"] == "2.5.4"
    clock = [e["elapsed"] for e in events]
    assert all(type(value) is float and math.isfinite(value) for value in clock)
    assert 0 <= clock[0] and all(a < b for a, b in zip(clock, clock[1:]))
    assert clock[-1] < 120
    supervision = summary["supervision"]
    assert type(supervision["killed_at_cap"]) is bool and not supervision["killed_at_cap"]
    assert type(supervision["returncode"]) is int and supervision["returncode"] == 0
    assert type(supervision["elapsed_seconds"]) is float and clock[-1] <= supervision["elapsed_seconds"] < 120
    assert supervision["stderr"] == ""
    assert supervision["postrun_summary"] == "bookkeeping only; no solving or certification"
    # The remaining-time sample precedes solver_start emission.  The source
    # budget is 120 seconds; compare represented doubles exactly as rationals.
    remaining = Fraction(started["remaining_wall_seconds"])
    remaining_sample_elapsed = Fraction(120)-remaining
    assert Fraction(model["elapsed"]) <= remaining_sample_elapsed <= Fraction(started["elapsed"])
    assert 0 < returned["solver_run_seconds"] <= returned["elapsed"]-started["elapsed"]
    assert type(returned["mip_node_count"]) is int and 0 <= returned["mip_node_count"] < 100000
    assert returned["status"] == "Infeasible" and returned["value_valid"] is False
    assert finished["reason"] == "numerical_status_without_candidate_unresolved"
    assert finished["solver_status"] == returned["status"]
    expected_summary = {
        "protocol": PROTOCOL, "formal_parameters": parameters, "supervision": supervision,
        "termination_reason": finished["reason"], "on_time_verified_target": False,
        "observed_elapsed_seconds": supervision["elapsed_seconds"], "solver_return": returned,
        "candidate": None, "solver_incumbent_observations": [], "retained_candidate_for_later_check": None,
        "exact_candidate_check": None, "whole_certificate": None,
        "verification_scope": "Later checking cannot add historical on-time credit; numerical infeasibility and timeout are not exact exclusions",
        "original_event_count": 6, "worker_failure": None, "no_configuration_observed": False,
        "events_file": STEM+".jsonl"}
    exact_equal(summary, expected_summary)
    absent = ["incumbent_observed", "candidate", "exact_candidate_check", "whole_certificate", "verified_commit", "worker_failure"]
    assert all(kind not in kinds for kind in absent)
    return {
        "scope": "Independent retained formal-result review only; no implementation controls or mathematical solver rerun.",
        "original_json_and_complete_six_line_journal_parsed": True,
        "native_all_fields_types_double_bits_and_decimal_values_preserved": True,
        "native_statistics": scalar_statistics(native),
        "protocol": PROTOCOL, "formal_parameters": parameters,
        "all_model_fields_and_59_rows_identical_to_R14_reviewed_v3_control": True,
        "event_kinds": kinds, "event_elapsed_seconds": clock,
        "remaining_time_sample_elapsed": float(remaining_sample_elapsed),
        "solver_remaining_wall_seconds": started["remaining_wall_seconds"],
        "solver_run_seconds": returned["solver_run_seconds"], "mip_node_count": returned["mip_node_count"],
        "reported_solver_status": returned["status"], "returned_value_valid": returned["value_valid"],
        "supervision": supervision,
        "raw_summary_independently_reconstructed": True,
        "absent_event_kinds": absent, "on_time_verified_target": False,
        "interpretation": "Normal numerical infeasible return without an observed candidate; finite mathematical feasibility remains unresolved.",
        "not_timeout_or_node_cap_termination": True,
        "exact_empty_set_certificate": False, "new_solver_runs_or_roots": 0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT/"independent_trace56_result_review.json")
    destination = parser.parse_args().output
    if destination.exists():
        raise FileExistsError(destination)
    result = review()
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
