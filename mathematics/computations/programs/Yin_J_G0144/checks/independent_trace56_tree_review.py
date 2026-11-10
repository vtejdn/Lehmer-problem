"""Independent exact replay of the fixed D56 tree, with no LP or roots.

The mathematical traversal below uses reviewer-owned polynomial arithmetic.
Author replay functions are invoked only afterwards as interface comparisons.
"""

import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction as Q
from functools import reduce
import gzip
import hashlib
import itertools
import json
from math import gcd, isfinite, lcm, prod
from pathlib import Path
import sys

from independent_trace56_review import BASIS, multiply, to_free, evaluate, divide, trace
from independent_trace56_result_review import decode, exact_equal, scalar_statistics

HERE = Path(__file__).resolve().parents[1]
OUTPUT = HERE.parents[1] / "outputs" / HERE.name
PROTOCOL = "fixed-D56-height4-exact-separation-tree"
OPTIONS = {"output_flag": False, "threads": 1, "parallel": "off", "solver": "simplex",
           "presolve": "off", "random_seed": 56003, "simplex_strategy": 1,
           "simplex_scale_strategy": 2, "primal_feasibility_tolerance": 1e-9,
           "dual_feasibility_tolerance": 1e-9}
PARAMETERS = {"internal_prefix_cap": 50000, "wall_seconds_from_prelaunch": 120,
              "integer_hint_scale": 2**36, "coordinate_order": "a1 through a28",
              "traversal": "depth-first; ascending integer children", "LP_options": OPTIONS}


def read(path):
    return decode(Path(path).read_text(encoding="utf-8"))


def reconstruction(data):
    assert data["protocol"] == "S10-fixed-D56-all-real-trace-cell"
    assert (data["degree"], data["trace_degree"], data["height"]) == (56, 28, 4)
    assert data["qL_ascending"] == [3, 4, -5, -5, 1, 1]
    assert data["qH_ascending"] == [-1, 4, 8, -17, -14, 20, 7, -8, -1, 1]
    nodes = [Q(*pair) for pair in data["nodes"]]
    rational_vertices = []
    for omitted in range(29):
        polynomial = [Q(1)]
        for i, node in enumerate(nodes):
            if i != omitted:
                polynomial = multiply(polynomial, [-node, 1])
        rational_vertices.append(to_free(polynomial))
    encoded = [[[x.numerator, x.denominator] for x in v] for v in rational_vertices]
    exact_equal(encoded, data["vertices_free_descending"])
    denominator = lcm(*(x.denominator for v in rational_vertices for x in v))
    assert denominator == 70835497243044678205440
    vertices = []
    for rational in rational_vertices:
        assert all((x*denominator).denominator == 1 for x in rational)
        vertices.append([int(x*denominator) for x in rational])
    ceiling = lambda x: -((-x.numerator)//x.denominator)
    box = [[max(-4, ceiling(min(v[j] for v in rational_vertices))),
            min(4, max(v[j] for v in rational_vertices).__floor__())] for j in range(28)]
    exact_equal(box, data["closed_simplex_height_box_integer_bounds"])
    sign_rows = []
    for i, node in enumerate(nodes):
        values = [(-1)**i*evaluate(p, node) for p in [*reversed(BASIS[:28]), BASIS[28]]]
        scale = lcm(*(x.denominator for x in values))
        integers = [int(x*scale) for x in values]
        common = reduce(gcd, integers, 0)
        sign_rows.append([x//common for x in integers])
    exact_equal(sign_rows, data["strict_sign_integer_rows"])
    maps = {}
    for name in ("qL", "qH"):
        core = data[name+"_ascending"]
        degree = len(core)-1
        columns = []
        for polynomial in [BASIS[28], *reversed(BASIS[:28])]:
            _, remainder = divide(polynomial, core)
            assert all(x.denominator == 1 for x in remainder)
            columns.append([int(remainder[j]) if j < len(remainder) else 0 for j in range(degree)])
        maps[name] = {"constants": columns[0], "rows": [list(row) for row in zip(*columns[1:])]}
        for key in ("constants", "rows"):
            exact_equal(maps[name][key], data["remainder_maps"][name][key])
    return {"n": 28, "vertices": vertices, "denominator": denominator, "box": box,
            "sign_rows": sign_rows, "remainder_maps": maps,
            "rational_vertices": rational_vertices, "nodes": nodes, "data": data}


def inner(a, b):
    return sum(x*y for x, y in zip(a, b))


def maximum_box(normal, prefix, box):
    return sum(value*(prefix[j] if j < len(prefix) else box[j][1] if value >= 0 else box[j][0])
               for j, value in enumerate(normal))


def bound(sign, normal, scale, prefix, problem):
    assert type(scale) is int and scale > 0
    assert len(normal) == problem["n"] and all(type(x) is int for x in normal)
    d = problem["denominator"]
    k = len(prefix)
    support = max(sign*scale*v[k]-inner(normal, v) for v in problem["vertices"])
    numerator = d*maximum_box(normal, prefix, problem["box"])+support
    denominator = d*scale
    answer, remainder = divmod(numerator, denominator)
    assert 0 <= remainder < denominator
    return answer


def choices_for(hint, prefix, problem):
    assert len(prefix) < problem["n"] and isinstance(hint, list)
    if hint[0] == "separate":
        assert len(hint) == 2
        normal = hint[1]
        assert len(normal) == problem["n"] and all(type(x) is int for x in normal)
        assert min(inner(normal, v) for v in problem["vertices"]) > problem["denominator"]*maximum_box(normal, prefix, problem["box"])
        return []
    assert len(hint) == 3 and hint[0] == "bounds"
    for vector in hint[1:]:
        assert isinstance(vector, list) and len(vector) == problem["n"]+1
        assert all(type(x) is int for x in vector) and vector[0] > 0
    low = max(problem["box"][len(prefix)][0], -bound(-1, hint[1][1:], hint[1][0], prefix, problem))
    high = min(problem["box"][len(prefix)][1], bound(1, hint[2][1:], hint[2][0], prefix, problem))
    return list(range(low, high+1))


def leaf_data(prefix, problem):
    assert len(prefix) == 28 and all(type(x) is int for x in prefix)
    whole = [1, *prefix, *reversed(prefix[:-1]), 1]
    polynomial = trace(whole)
    values = [inner(row, [*prefix, 1]) for row in problem["sign_rows"]]
    failed = [i for i, value in enumerate(values) if value <= 0]
    remainders = {}
    for name in ("qL", "qH"):
        core = problem["data"][name+"_ascending"]
        _, rem = divide(polynomial, core)
        assert all(x.denominator == 1 for x in rem)
        remainders[name] = [int(rem[j]) if j < len(rem) else 0 for j in range(len(core)-1)]
    fibers = [name for name, value in remainders.items() if not any(value)]
    reason = "failed_strict_signs" if failed else "known_core_fiber" if fibers else "survivor"
    result = {"reason": reason, "failed_sign_indices": failed, "remainders": remainders, "divisible_by": fibers}
    if reason == "survivor":
        result["coefficients_ascending"] = whole
        result["strict_integer_sign_values"] = values
    return result, whole, polynomial, values


def complete_replay(events, problem):
    assert [e["kind"] for e in events[:3]] == ["configuration", "prepared", "LP_model"]
    exact_equal(events[0]["parameters"], PARAMETERS)
    assert events[0]["protocol"] == PROTOCOL and events[0]["input"] == "trace56_cell.json"
    exact_equal({k: v for k, v in events[1].items() if k not in {"kind", "elapsed"}},
                {"denominator": problem["denominator"], "box": problem["box"], "vertices": 29})
    exact_equal({k: v for k, v in events[2].items() if k not in {"kind", "elapsed"}},
                {"highspy_version": "1.15.1", "numpy_version": "2.5.4", "vertices": 29,
                 "coordinate_rows": 28, "options": OPTIONS})
    assert all(type(e["elapsed"]) is float and isfinite(e["elapsed"]) and 0 <= e["elapsed"] < 120 for e in events)
    assert all(a["elapsed"] <= b["elapsed"] for a, b in zip(events, events[1:]))
    widths = [hi-lo+1 for lo, hi in problem["box"]]
    suffix = [prod(widths[j:]) for j in range(29)]
    assert suffix[0] == 35294189134260626586455040
    stack, cursor, sequence, calls = [()], 3, 0, 0
    internal, excluded, empty_intervals = 0, 0, 0
    depths, seen, leaves, entries = Counter(), set(), [], Counter()
    while stack:
        prefix = stack.pop()
        assert prefix not in seen
        seen.add(prefix)
        depth = len(prefix)
        beginning = events[cursor]
        assert beginning["kind"] == "prefix_begin" and beginning["sequence"] == sequence
        exact_equal(beginning["prefix"], list(prefix))
        assert beginning["node_type"] == ("leaf" if depth == 28 else "internal")
        cursor += 1
        if depth < 28:
            for sign in (-1, 1):
                start, returned = events[cursor:cursor+2]
                calls += 1
                assert (start["kind"], returned["kind"]) == ("LP_start", "LP_return")
                for event in (start, returned):
                    assert (event["sequence"], event["sign"], event["call"]) == (sequence, sign, calls)
                sample = Q(120)-Q(start["remaining_seconds"])
                assert Q(events[cursor-1]["elapsed"]) <= sample <= Q(start["elapsed"])
                assert returned["status"] == "Optimal"
                cursor += 2
            event = events[cursor]
            assert event["kind"] == "node" and event["sequence"] == sequence
            exact_equal(event["prefix"], list(prefix))
            options = choices_for(event["hint"], prefix, problem)
            entries[event["hint"][0]] += 1
            excluded += (widths[depth]-len(options))*suffix[depth+1]
            assert all(problem["box"][depth][0] <= x <= problem["box"][depth][1] for x in options)
            stack.extend(prefix+(x,) for x in reversed(options))
            internal += 1
            empty_intervals += not options
        else:
            event = events[cursor]
            assert event["kind"] == "leaf" and event["sequence"] == sequence
            exact_equal(event["prefix"], list(prefix))
            result, whole, polynomial, values = leaf_data(prefix, problem)
            exact_equal(result, event["result"])
            leaves.append({"sequence": sequence, "prefix": list(prefix), "result": result,
                           "whole": whole, "trace": polynomial, "strict_integer_sign_values": values})
        depths[depth] += 1
        sequence += 1
        cursor += 1
    assert cursor == len(events)-1
    finish = events[cursor]
    assert finish["kind"] == "finish" and finish["reason"] == "complete"
    assert finish["internal_prefixes"] == internal == 1504 < 50000
    assert finish["leaves"] == len(leaves) == 1
    assert finish["LP_run_calls"] == calls == 3008
    assert finish["frontier"] == []
    assert excluded+len(leaves) == suffix[0]
    leaf = leaves[0]
    data = problem["data"]
    exact_equal(leaf["prefix"], data["parent_free_descending"])
    exact_equal(leaf["whole"], data["parent_ascending"])
    exact_equal(leaf["trace"], data["parent_trace_ascending"])
    assert min(leaf["strict_integer_sign_values"]) > 0
    assert leaf["result"]["divisible_by"] == ["qL"]
    assert leaf["result"]["remainders"]["qH"] == [2, -8, -14, 29, 8, -15, -1, 2, 0]
    weights = []
    for i, node in enumerate(problem["nodes"]):
        denominator = prod(node-other for j, other in enumerate(problem["nodes"]) if i != j)
        weights.append(evaluate(leaf["trace"], node)/denominator)
    assert all(x > 0 for x in weights) and sum(weights) == 1
    assert [sum(w*v[j] for w, v in zip(weights, problem["rational_vertices"])) for j in range(28)] == leaf["prefix"]
    return {"internal_prefixes": internal, "coordinate_bound_checks": 2*internal,
            "mathematical_entries": sequence, "complete_events": len(events), "LP_run_calls_observed": calls,
            "hint_kinds": dict(entries), "empty_child_intervals": empty_intervals,
            "processed_counts_by_depth": [depths[j] for j in range(29)],
            "initial_clipped_box_integer_vectors": suffix[0], "integer_vectors_in_disjoint_excluded_subboxes": excluded,
            "remaining_full_leaves": len(leaves), "final_frontier": [],
            "unique_leaf": leaf, "parent_positive_convex_weights_verified": True,
            "closed_simplex_height_four_integer_intersection": "Exactly the original parent vector"}


def mechanical_interfaces(problem, proof, original_verification):
    sys.path.insert(0, str(HERE))
    import trace56_tree as author
    actual_replay = author.verify(HERE/"trace56_tree_proof.json.gz")
    exact_equal(actual_replay, original_verification)
    assert not any(name in sys.modules for name in ("highspy", "numpy", "flint"))
    # Independent small checks use a nonunit common denominator and negative
    # rational vertex coordinates, unlike the original integer triangle.
    triangle = {"n": 2, "vertices": [[-3, -2], [15, -2], [-3, 16]],
                "denominator": 6, "box": [[-1, 3], [-1, 3]]}
    points = [(x, y) for x in range(-1, 4) for y in range(-1, 4)
              if Q(x) >= Q(-1, 2) and Q(y) >= Q(-1, 3) and Q(x+y) <= Q(13, 6)]
    cases = 0
    for prefix in [(), *[(x,) for x in range(-1, 4)]]:
        extensions = [p for p in points if p[:len(prefix)] == prefix]
        for normal in itertools.product((-2, 0, 3), repeat=2):
            for scale in (1, 3, 5):
                for sign in (-1, 1):
                    value = bound(sign, normal, scale, prefix, triangle)
                    assert value == author.coordinate_bound(sign, normal, scale, prefix, triangle)
                    assert all(sign*p[len(prefix)] <= value for p in extensions)
                    cases += 1
    assert author.separated([-1, -1], (2,), {**triangle, "box": [[-1, 3], [1, 3]]})
    rejected = []
    def rejects(name, action):
        try:
            action()
        except (ValueError, json.JSONDecodeError):
            rejected.append(name)
        else:
            raise AssertionError("invalid fixture accepted: "+name)
    rejects("false zero-normal separation", lambda: author.verify_step(["separate", [0]*28], (), problem))
    for scale in (0, -1, True):
        rejects("invalid scale "+repr(scale), lambda scale=scale: author.verify_step(
            ["bounds", [scale]+[0]*28, [1]+[0]*28], (), problem))
    parent = problem["data"]["parent_free_descending"]
    result = leaf_data(parent, problem)[0]
    singleton = {**problem, "box": [[x, x] for x in parent]}
    records = [{"kind": "node", "sequence": i, "prefix": parent[:i],
                "hint": ["bounds", [1]+[0]*28, [1]+[0]*28], "elapsed": i/100} for i in range(28)]
    records += [{"kind": "leaf", "sequence": 28, "prefix": parent, "result": result, "elapsed": .28},
                {"kind": "finish", "reason": "complete", "internal_prefixes": 28, "leaves": 1,
                 "frontier": [], "elapsed": .29}]
    assert author.replay(records, singleton)["complete_within_generation_budget"]
    partial = author.replay(records[:5], singleton)
    assert partial["frontier"] == [parent[:5]] and not partial["complete_within_generation_budget"]
    rejects("missing internal entry", lambda: author.replay(records[:4]+records[5:], singleton))
    rejects("missing leaf", lambda: author.replay(records[:-2]+records[-1:], singleton))
    altered = deepcopy(records)
    altered[-2]["result"]["reason"] = "survivor"
    rejects("changed leaf classification", lambda: author.replay(altered, singleton))
    rejects("record after termination", lambda: author.replay(records+[records[0]], singleton))
    late = deepcopy(records)
    late[-1]["elapsed"] = 120.0
    assert not author.replay(late, singleton)["complete_within_generation_budget"]
    late = deepcopy(records)
    late[0]["elapsed"] = 120.0
    assert not author.replay(late, singleton)["complete_within_generation_budget"]
    first_node = next(i for i, event in enumerate(proof["events"]) if event["kind"] == "node")
    prefix_events = proof["events"][:first_node]
    text = "".join(json.dumps(e)+"\n" for e in prefix_events)+'{"kind":"node"'
    recovered, tail = author.parse_journal(text)
    exact_equal(recovered, prefix_events)
    assert tail == '{"kind":"node"'
    pending = author.replay(recovered, problem)
    assert pending["frontier"] == [[]] and pending["pending_started_prefix"]["prefix"] == []
    rejects("malformed newline-terminated JSON", lambda: author.parse_journal('{"kind":}\n'))
    controls = read(OUTPUT/"trace56_tree_controls_v2.json")
    assert controls["small_exact_bound_cases"] == 600 and controls["tiny_LP_total_run_calls"] == 3
    original_triangle = {"n": 2, "vertices": [[0, 0], [2, 0], [0, 2]],
                         "denominator": 1, "box": [[0, 2], [0, 2]]}
    assert choices_for(controls["tiny_LP_hints"][0], (2,), original_triangle) == [0]
    assert choices_for(controls["tiny_LP_hints"][1], (2,), {**original_triangle, "box": [[0, 2], [1, 2]]}) == []
    return {"author_existing_certificate_replay_matches_saved_output": True,
            "nonunit_denominator_negative_vertex_exact_cases": cases,
            "invalid_mechanical_inputs_rejected": rejected,
            "complete_singleton_and_partial_frontier": True,
            "at_deadline_record_or_finish_loses_generation_credit": True,
            "incomplete_node_line_preserves_pending_root_prefix": True,
            "saved_two_tiny_LP_hints_checked_without_LP": True,
            "new_LP_or_roots": 0}


def review():
    proof_path = HERE/"trace56_tree_proof.json.gz"
    journal_path = OUTPUT/"trace56_exact_tree_attempt.jsonl"
    supervision_path = OUTPUT/"trace56_exact_tree_attempt.json"
    proof_bytes = proof_path.read_bytes()
    proof_text = gzip.decompress(proof_bytes).decode("utf-8")
    proof = decode(proof_text)
    original_text = journal_path.read_text(encoding="utf-8")
    assert original_text.endswith("\n")
    lines = original_text.splitlines()
    assert len(lines) == 9030 and all(line.strip() for line in lines)
    original = [decode(line) for line in lines]
    exact_equal(proof["events"], original)
    exact_equal(proof["supervision"], read(supervision_path))
    decimal_proof = decode(proof_text, True)
    exact_equal(decimal_proof["events"], [decode(line, True) for line in lines])
    exact_equal(decimal_proof["supervision"], decode(supervision_path.read_text(encoding="utf-8"), True))
    assert set(proof) == {"protocol", "input", "parameters", "supervision", "events",
                          "unfinished_last_line", "retention_scope"}
    assert proof["protocol"] == PROTOCOL and proof["input"] == "trace56_cell.json"
    exact_equal(proof["parameters"], PARAMETERS)
    assert proof["unfinished_last_line"] == ""
    assert proof["retention_scope"] == "lossless event retention after generation; no new hints, LP or leaf evaluations"
    assert len(proof_bytes) == 384470 and journal_path.stat().st_size == 1619760
    problem = reconstruction(read(HERE/"trace56_cell.json"))
    traversal = complete_replay(original, problem)
    supervision = proof["supervision"]
    assert supervision["killed_at_cap"] is False and type(supervision["returncode"]) is int and supervision["returncode"] == 0
    assert supervision["stderr"] == ""
    assert original[-1]["elapsed"] <= supervision["elapsed_seconds"] < 120
    verification = read(OUTPUT/"trace56_tree_verification.json")
    for key in ("internal_prefixes", "processed_counts_by_depth", "frontier"):
        expected = traversal["final_frontier"] if key == "frontier" else traversal[key]
        exact_equal(verification[key], expected)
    assert verification["leaves"] == 1 and verification["closed_tree_without_survivor"]
    assert verification["complete_within_generation_budget"] and verification["exact_replay"] == "pass"
    interfaces = mechanical_interfaces(problem, proof, verification)
    return {"scope": "Independent fixed tree, exact closed-hull conclusion, program interfaces and actual retained attempt.",
            "common_positive_denominator": problem["denominator"], "clipped_height_four_box": problem["box"],
            "all_29_vertices_29_sign_rows_and_two_remainder_maps_reconstructed": True,
            "native_all_original_fields_types_binary_and_decimal_values_preserved": True,
            "native_statistics": scalar_statistics(proof), "native_gzip_bytes": len(proof_bytes),
            "original_journal_bytes": journal_path.stat().st_size,
            "native_sha256": hashlib.sha256(proof_bytes).hexdigest(),
            "event_kind_counts": dict(Counter(e["kind"] for e in original)),
            "traversal": traversal, "generation_finish_elapsed": original[-1]["elapsed"],
            "generation_supervision": supervision, "interfaces": interfaces,
            "new_generation_LP_or_root_calls": 0,
            "finite_conclusion": "The closed fixed simplex intersected with the height-four integer box consists exactly of the original parent; the strict cell has no point outside the two known-value fibers.",
            "original_MIP_status_changed": False, "G0001_completion": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT/"independent_trace56_tree_review.json")
    destination = parser.parse_args().output
    if destination.exists():
        raise FileExistsError(destination)
    result = review()
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps({key: value for key, value in result.items() if key not in {"traversal", "clipped_height_four_box"}}, indent=2))
    print(json.dumps({key: value for key, value in result["traversal"].items() if key != "unique_leaf"}, indent=2))


if __name__ == "__main__":
    main()
