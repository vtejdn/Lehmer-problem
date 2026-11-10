"""One bounded rational separation-tree attempt for the fixed D56 trace cell.

Only generate makes the selected proof-generation attempt.  Verification uses
the standard library and exact integer/rational arithmetic, without an LP solver.
"""

import argparse
from collections import Counter
from fractions import Fraction
import gzip
import itertools
import json
from math import gcd, isfinite, lcm
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parents[1] / "outputs" / HERE.name
INPUT = HERE / "trace56_cell.json"
PROOF = HERE / "trace56_tree_proof.json.gz"
LABEL = "trace56_exact_tree_attempt"
PROTOCOL = "fixed-D56-height4-exact-separation-tree"
N, HEIGHT, INTERNAL_CAP, WALL_SECONDS, SCALE = 28, 4, 50000, 120, 2**36
OPTIONS = {"output_flag": False, "threads": 1, "parallel": "off", "solver": "simplex",
           "presolve": "off", "random_seed": 56003, "simplex_strategy": 1,
           "simplex_scale_strategy": 2, "primal_feasibility_tolerance": 1e-9,
           "dual_feasibility_tolerance": 1e-9}
PARAMETERS = {"internal_prefix_cap": INTERNAL_CAP, "wall_seconds_from_prelaunch": WALL_SECONDS,
              "integer_hint_scale": SCALE, "coordinate_order": "a1 through a28",
              "traversal": "depth-first; ascending integer children", "LP_options": OPTIONS}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def basis_up_to(n):
    basis = [[2], [0, 1]]
    for k in range(2, n + 1):
        row = [0] + basis[k - 1]
        for j, value in enumerate(basis[k - 2]):
            row[j] -= value
        basis.append(row)
    basis[0] = [1]
    return basis[:n + 1]


def monic_remainder(polynomial, divisor):
    require(divisor[-1] == 1, "nonmonic remainder divisor")
    work = list(polynomial)
    degree = len(divisor) - 1
    for k in range(len(work) - 1, degree - 1, -1):
        leading = work[k]
        for j, value in enumerate(divisor):
            work[k - degree + j] -= leading * value
    return (work + [0] * degree)[:degree]


def prepare(data):
    """Reconstruct every vertex, sign row and remainder map without FLINT/LP."""
    require(data["protocol"] == "S10-fixed-D56-all-real-trace-cell", "wrong fixed input")
    require((data["degree"], data["trace_degree"], data["height"]) == (56, N, HEIGHT), "wrong scope")
    require(data["qL_ascending"] == [3, 4, -5, -5, 1, 1], "wrong qL")
    require(data["qH_ascending"] == [-1, 4, 8, -17, -14, 20, 7, -8, -1, 1], "wrong qH")
    nodes = [Fraction(*pair) for pair in data["nodes"]]
    require(len(nodes) == N + 1 and all(a < b for a, b in zip(nodes, nodes[1:])), "invalid nodes")
    require((nodes[0], nodes[-2], nodes[-1]) == (-2, 2, Fraction(61, 30)), "wrong endpoint nodes")
    basis = basis_up_to(N)
    vertices = []
    for omitted in range(N + 1):
        polynomial = [Fraction(1)]
        for j, node in enumerate(nodes):
            if j != omitted:
                expanded = [Fraction(0)] * (len(polynomial) + 1)
                for k, coefficient in enumerate(polynomial):
                    expanded[k] -= node * coefficient
                    expanded[k + 1] += coefficient
                polynomial = expanded
        require(polynomial[-1] == 1, "nonmonic vertex")
        for j, value in enumerate(basis[N]):
            polynomial[j] -= value
        free = []
        for k in range(N - 1, -1, -1):
            value = polynomial[k]
            free.append(value)
            for j, coefficient in enumerate(basis[k]):
                polynomial[j] -= value * coefficient
        require(not any(polynomial), "vertex coordinate conversion failed")
        vertices.append(free)
    encoded = [[[x.numerator, x.denominator] for x in row] for row in vertices]
    require(encoded == data["vertices_free_descending"], "vertex/input mismatch")
    denominator = lcm(*(x.denominator for row in vertices for x in row))
    integers = [[int(x * denominator) for x in row] for row in vertices]
    box = [[max(-HEIGHT, -((-min(v[j] for v in integers)) // denominator)),
            min(HEIGHT, max(v[j] for v in integers) // denominator)] for j in range(N)]
    require(box == data["closed_simplex_height_box_integer_bounds"], "box mismatch")
    rows = []
    for i, node in enumerate(nodes):
        values = [sum(coefficient * node**j for j, coefficient in enumerate(poly))
                  for poly in [*reversed(basis[:N]), basis[N]]]
        scale = lcm(*(value.denominator for value in values))
        raw = [int((-1)**i * value * scale) for value in values]
        divisor = gcd(*raw)
        rows.append([value // divisor for value in raw])
    require(rows == data["strict_sign_integer_rows"], "exact sign row mismatch")
    maps = {}
    for name in ("qL", "qH"):
        core = data[name + "_ascending"]
        constants = monic_remainder(basis[N], core)
        remainders = [monic_remainder(poly, core) for poly in reversed(basis[:N])]
        linear = [list(row) for row in zip(*remainders)]
        require(constants == data["remainder_maps"][name]["constants"] and
                linear == data["remainder_maps"][name]["rows"], "remainder map mismatch")
        maps[name] = {"constants": constants, "rows": linear}
    return {"n": N, "vertices": integers, "denominator": denominator, "box": box,
            "sign_rows": rows, "remainder_maps": maps, "basis": basis, "data": data}


def box_maximum(normal, prefix, box):
    return dot(normal, prefix) + sum(max(h * lo, h * hi)
                                    for h, (lo, hi) in zip(normal[len(prefix):], box[len(prefix):]))


def separated(normal, prefix, problem):
    return min(dot(normal, v) for v in problem["vertices"]) > problem["denominator"] * box_maximum(normal, prefix, problem["box"])


def coordinate_bound(sign, normal, scale, prefix, problem):
    residual = max(sign * scale * v[len(prefix)] - dot(normal, v) for v in problem["vertices"])
    return (problem["denominator"] * box_maximum(normal, prefix, problem["box"]) + residual) // (problem["denominator"] * scale)


def integer_vector(vector, length):
    require(isinstance(vector, list) and len(vector) == length and all(type(x) is int for x in vector), "invalid integer vector")
    return vector


def verify_step(entry, prefix, problem):
    n = problem["n"]
    require(len(prefix) < n, "internal entry at leaf")
    require(isinstance(entry, list), "invalid hint")
    if len(entry) == 2 and entry[0] == "separate":
        normal = integer_vector(entry[1], n)
        require(separated(normal, prefix, problem), "failed exact strict separation")
        return []
    require(len(entry) == 3 and entry[0] == "bounds", "invalid bound entry")
    lo, hi = problem["box"][len(prefix)]
    for sign, vector in zip((-1, 1), entry[1:]):
        scale, *normal = integer_vector(vector, n + 1)
        require(scale > 0, "nonpositive scale")
        bound = coordinate_bound(sign, normal, scale, prefix, problem)
        if sign == -1:
            lo = max(lo, -bound)
        else:
            hi = min(hi, bound)
    return list(range(lo, hi + 1))


def classify_leaf(prefix, problem):
    integer_vector(list(prefix), problem["n"])
    require(all(lo <= x <= hi for x, (lo, hi) in zip(prefix, problem["box"])), "leaf outside box")
    signs = [dot(row[:-1], prefix) + row[-1] for row in problem["sign_rows"]]
    failed = [i for i, value in enumerate(signs) if value <= 0]
    remainders = {name: [constant + dot(row, prefix) for constant, row in zip(mapping["constants"], mapping["rows"])]
                  for name, mapping in problem["remainder_maps"].items()}
    fibers = [name for name, remainder in remainders.items() if not any(remainder)]
    reason = "failed_strict_signs" if failed else "known_core_fiber" if fibers else "survivor"
    result = {"reason": reason, "failed_sign_indices": failed, "remainders": remainders,
              "divisible_by": fibers}
    if reason == "survivor":
        result["coefficients_ascending"] = [1, *prefix, *reversed(prefix[:-1]), 1]
        result["strict_integer_sign_values"] = signs
    return result


class BudgetStop(Exception):
    pass


class SuggestionSolver:
    """Floating hints only; no status or unverified bound can prune a prefix."""
    def __init__(self, problem, deadline, emit):
        import highspy
        import numpy
        self.problem, self.deadline, self.emit = problem, deadline, emit
        self.highspy = highspy
        self.values = numpy.array([[x / problem["denominator"] for x in row] for row in problem["vertices"]])
        self.indices = numpy.arange(len(self.values), dtype=numpy.int32)
        self.solver = highspy.Highs()
        for name, value in OPTIONS.items():
            require(self.solver.setOptionValue(name, value) == highspy.HighsStatus.kOk, "unsupported LP option " + name)
        weights = self.solver.addVariables(len(self.values), lb=0, ub=1)
        self.solver.addConstr(self.solver.qsum(weights) == 1)
        self.rows = []
        for j, (lo, hi) in enumerate(problem["box"]):
            row = self.solver.addConstr(self.solver.qsum(value * weights[i] for i, value in enumerate(self.values[:, j])) <= hi)
            self.solver.changeRowBounds(row.index, lo, hi)
            self.rows.append(row)
        self.calls = 0
        emit("LP_model", highspy_version=self.solver.version(), numpy_version=numpy.__version__,
             vertices=len(self.values), coordinate_rows=len(self.rows), options=OPTIONS)

    def hint(self, prefix, sequence):
        for j, row in enumerate(self.rows):
            lo, hi = (prefix[j], prefix[j]) if j < len(prefix) else self.problem["box"][j]
            self.solver.changeRowBounds(row.index, lo, hi)
        entry = ["bounds"]
        for sign in (-1, 1):
            remaining = self.deadline - time.perf_counter()
            if remaining <= 0:
                raise BudgetStop()
            self.solver.changeColsCost(len(self.values), self.indices, sign * self.values[:, len(prefix)])
            self.solver.setMaximize()
            require(self.solver.setOptionValue("time_limit", remaining) == self.highspy.HighsStatus.kOk, "LP time limit refused")
            self.calls += 1
            self.emit("LP_start", sequence=sequence, sign=sign, call=self.calls, remaining_seconds=remaining)
            self.solver.run()
            status = self.solver.getModelStatus()
            self.emit("LP_return", sequence=sequence, sign=sign, call=self.calls,
                      status=self.solver.modelStatusToString(status))
            if time.perf_counter() >= self.deadline:
                raise BudgetStop()
            if status == self.highspy.HighsModelStatus.kOptimal:
                values = list(self.solver.getSolution().row_dual[1:])
                if len(values) == self.problem["n"] and all(isfinite(value) for value in values):
                    vector = [SCALE] + [int(round(SCALE * value)) for value in values]
                    common = gcd(*vector)
                    entry.append([value // common for value in vector])
                    continue
            if status == self.highspy.HighsModelStatus.kInfeasible:
                remaining = self.deadline - time.perf_counter()
                if remaining <= 0:
                    raise BudgetStop()
                require(self.solver.setOptionValue("time_limit", remaining) == self.highspy.HighsStatus.kOk, "ray time limit refused")
                self.emit("LP_ray_start", sequence=sequence, sign=sign)
                _, exists, ray = self.solver.getDualRay()
                if time.perf_counter() >= self.deadline:
                    raise BudgetStop()
                if exists and len(ray) == self.problem["n"] + 1 and all(isfinite(value) for value in ray[1:]):
                    vector = [int(round(SCALE * value)) for value in ray[1:]]
                    common = gcd(*vector) or 1
                    for orientation in (-1, 1):
                        normal = [orientation * value // common for value in vector]
                        if separated(normal, prefix, self.problem):
                            return ["separate", normal]
            self.solver.setBasis()
            entry.append([1] + [0] * self.problem["n"])
        return entry


def worker(started, journal):
    from trace56_milp import Journal
    deadline = started + WALL_SECONDS
    stack, internal, leaves, sequence = [()], 0, 0, 0
    with journal.open("x", encoding="utf-8") as stream:
        emit = Journal(stream, started).emit
        emit("configuration", protocol=PROTOCOL, parameters=PARAMETERS, input=INPUT.name)
        try:
            problem = prepare(json.loads(INPUT.read_text(encoding="utf-8")))
            emit("prepared", denominator=problem["denominator"], box=problem["box"], vertices=len(problem["vertices"]))
            solver = SuggestionSolver(problem, deadline, emit)
            reason = "complete"
            while stack:
                if time.perf_counter() >= deadline:
                    reason = "wall_limit"
                    break
                prefix = stack[-1]
                if len(prefix) < N and internal >= INTERNAL_CAP:
                    reason = "internal_prefix_limit"
                    break
                emit("prefix_begin", sequence=sequence, prefix=prefix, node_type="leaf" if len(prefix) == N else "internal")
                if len(prefix) == N:
                    result = classify_leaf(prefix, problem)
                    if time.perf_counter() >= deadline:
                        reason = "wall_limit"
                        break
                    emit("leaf", sequence=sequence, prefix=prefix, result=result)
                    stack.pop()
                    leaves += 1
                    sequence += 1
                    if result["reason"] == "survivor":
                        reason = "survivor_retained_stop"
                        break
                    continue
                hint = solver.hint(prefix, sequence)
                choices = verify_step(hint, prefix, problem)
                if time.perf_counter() >= deadline:
                    reason = "wall_limit"
                    break
                emit("node", sequence=sequence, prefix=prefix, hint=hint)
                stack.pop()
                stack.extend(prefix + (value,) for value in reversed(choices))
                internal += 1
                sequence += 1
            emit("finish", reason=reason, internal_prefixes=internal, leaves=leaves,
                 LP_run_calls=solver.calls, frontier=[list(prefix) for prefix in stack])
        except BudgetStop:
            emit("finish", reason="wall_limit", internal_prefixes=internal, leaves=leaves,
                 frontier=[list(prefix) for prefix in stack])
        except Exception as error:
            emit("worker_failure", error=repr(error), frontier=[list(prefix) for prefix in stack],
                 internal_prefixes=internal, leaves=leaves)
            raise


def parse_journal(text):
    lines = text.splitlines(keepends=True)
    events, tail = [], ""
    for i, line in enumerate(lines):
        if not line.endswith("\n"):
            require(i == len(lines) - 1, "nonterminal unfinished line")
            tail = line
        else:
            events.append(json.loads(line))
    return events, tail


def read_journal(path):
    return parse_journal(path.read_text(encoding="utf-8")) if path.exists() else ([], "")


def replay(events, problem):
    """Exact DFS coverage, including incomplete frontier; no solver is imported."""
    stack, internal, leaves, sequence = [()], 0, 0, 0
    depths, reasons, fibers = Counter(), Counter(), Counter()
    surviving, finish, pending = None, None, None
    after_limit = []
    for position, event in enumerate(events):
        kind = event["kind"]
        require(surviving is None or kind in ("finish", "worker_failure"), "generation continued after a survivor")
        if kind == "prefix_begin":
            require(stack and event["prefix"] == list(stack[-1]) and event["sequence"] == sequence, "pending prefix mismatch")
            pending = event
        elif kind in ("node", "leaf"):
            require(stack and event["prefix"] == list(stack[-1]) and event["sequence"] == sequence, "DFS coverage mismatch")
            if event.get("elapsed", 0) >= WALL_SECONDS:
                after_limit.append(position)
            prefix = stack[-1]
            if kind == "node":
                require(internal < INTERNAL_CAP, "internal prefix cap exceeded")
                choices = verify_step(event["hint"], prefix, problem)
                stack.pop()
                stack.extend(prefix + (value,) for value in reversed(choices))
                internal += 1
            else:
                require(len(prefix) == problem["n"], "leaf has wrong degree")
                result = classify_leaf(prefix, problem)
                require(result == event["result"], "leaf classification mismatch")
                stack.pop()
                leaves += 1
                reasons[result["reason"]] += 1
                if not result["failed_sign_indices"]:
                    for name in result["divisible_by"]:
                        fibers[name] += 1
                if result["reason"] == "survivor":
                    surviving = {"prefix": list(prefix), **result}
            depths[len(prefix)] += 1
            sequence += 1
            pending = None
        elif kind in ("finish", "worker_failure"):
            require(event["frontier"] == [list(prefix) for prefix in stack], "retained frontier mismatch")
            require((event["internal_prefixes"], event["leaves"]) == (internal, leaves), "retained counts mismatch")
            require(finish is None, "multiple terminal records")
            finish = event
        else:
            require(kind in ("configuration", "prepared", "LP_model", "LP_start", "LP_return", "LP_ray_start"), "unknown event kind")
        if finish is not None:
            require(position == len(events) - 1, "events after terminal record")
    if finish and finish["kind"] == "finish":
        require(finish["reason"] != "complete" or (not stack and surviving is None), "false complete marker")
        require(finish["reason"] != "survivor_retained_stop" or surviving is not None, "false survivor marker")
    closed = not stack and surviving is None
    on_time_complete = bool(closed and finish and finish.get("reason") == "complete"
                            and finish.get("elapsed", 0) < WALL_SECONDS and not after_limit)
    return {"exact_replay": "pass", "closed_tree_without_survivor": closed,
            "complete_within_generation_budget": on_time_complete,
            "internal_prefixes": internal, "leaves": leaves,
            "processed_counts_by_depth": [depths[j] for j in range(problem["n"] + 1)],
            "leaf_reasons": dict(reasons), "strict_cell_fibers": dict(fibers),
            "survivor": surviving, "frontier": [list(prefix) for prefix in stack],
            "pending_started_prefix": pending, "terminal_record": finish,
            "complete_records_at_or_after_wall_limit": after_limit}


def write_new(path, data):
    require(not path.exists(), "preserve existing result: " + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2, allow_nan=False)
        stream.write("\n")


def retain():
    journal, observation = OUTPUT / (LABEL + ".jsonl"), OUTPUT / (LABEL + ".json")
    require(not PROOF.exists(), "preserve retained proof attempt")
    supervision = json.loads(observation.read_text(encoding="utf-8"))
    require(journal.exists() or (supervision["returncode"] == -1 and not supervision["killed_at_cap"]),
            "missing generation journal without an observed startup-failure exception")
    events, tail = read_journal(journal)
    data = {"protocol": PROTOCOL, "input": INPUT.name, "parameters": PARAMETERS,
            "supervision": supervision, "events": events, "unfinished_last_line": tail,
            "retention_scope": "lossless event retention after generation; no new hints, LP or leaf evaluations"}
    with PROOF.open("xb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
            compressed.write(json.dumps(data, separators=(",", ":"), allow_nan=False).encode("utf-8"))
    print(json.dumps({"retained_native": PROOF.name, "complete_journal_events": len(events), "unfinished_tail_characters": len(tail)}))


def generate():
    from trace56_milp import supervise_child
    OUTPUT.mkdir(parents=True, exist_ok=True)
    journal, observation = OUTPUT / (LABEL + ".jsonl"), OUTPUT / (LABEL + ".json")
    require(not any(path.exists() for path in (journal, observation, PROOF)), "the one attempt already exists; no repeat")
    started = time.perf_counter()
    command = [sys.executable, "-B", str(Path(__file__).resolve()), "_worker", "--started", str(started), "--journal", str(journal)]
    supervision = supervise_child(command, started, WALL_SECONDS)
    write_new(observation, supervision)
    retain()
    print(json.dumps(supervision))


def verify(path):
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        proof = json.load(stream)
    require(proof["protocol"] == PROTOCOL and proof["input"] == INPUT.name and proof["parameters"] == PARAMETERS, "proof scope mismatch")
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    problem = prepare(data)
    events = proof["events"]
    if events:
        require(events[0]["kind"] == "configuration" and events[0]["parameters"] == PARAMETERS
                and events[0]["protocol"] == PROTOCOL and events[0]["input"] == INPUT.name, "configuration mismatch")
    for event in events:
        require(isinstance(event["elapsed"], (int, float)) and isfinite(event["elapsed"]) and event["elapsed"] >= 0, "invalid event time")
        if event["kind"] == "prepared":
            require(event["denominator"] == problem["denominator"] and event["box"] == problem["box"]
                    and event["vertices"] == len(problem["vertices"]), "prepared payload mismatch")
    require(all(a["elapsed"] <= b["elapsed"] for a, b in zip(events, events[1:])), "event times are not ordered")
    result = replay(events, problem)
    result["generation_supervision"] = proof["supervision"]
    result["unfinished_tail_characters"] = len(proof["unfinished_last_line"])
    result["solver_imported"] = any(name in sys.modules for name in ("highspy", "numpy", "flint"))
    result["finite_conclusion"] = ("Every strict-cell integer point in the declared height-four box is divisible by qL or qH"
                                    if result["complete_within_generation_budget"] else "No complete exclusion claimed")
    return result


def controls():
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    problem = prepare(data)
    parent = tuple(data["parent_free_descending"])
    parent_result = classify_leaf(parent, problem)
    require(parent_result["reason"] == "known_core_fiber" and parent_result["divisible_by"] == ["qL"], "parent control failed")
    child = (*parent[:-1], parent[-1] + 1)
    require(classify_leaf(child, problem)["failed_sign_indices"] == [5, 7, 13, 15, 17, 19, 23], "child control failed")
    triangle = {"n": 2, "vertices": [[0, 0], [2, 0], [0, 2]], "denominator": 1, "box": [[0, 2], [0, 2]]}
    points = [(x, y) for x in range(3) for y in range(3) if x + y <= 2]
    exact_cases = 0
    for prefix in [(), (0,), (1,), (2,)]:
        feasible = [point for point in points if point[:len(prefix)] == prefix]
        for normal in itertools.product(range(-2, 3), repeat=2):
            for scale in (1, 2, 3):
                for sign in (-1, 1):
                    bound = coordinate_bound(sign, normal, scale, prefix, triangle)
                    require(all(sign * point[len(prefix)] <= bound for point in feasible), "small exact bound failed")
                    exact_cases += 1
    require(separated([-1, -1], (2, 1), triangle), "small strict separation failed")
    rejected = []
    def must_reject(label, action):
        try:
            action()
        except ValueError:
            rejected.append(label)
        else:
            raise AssertionError("invalid control accepted: " + label)
    must_reject("false separation", lambda: verify_step(["separate", [0, 0]], (), triangle))
    must_reject("zero scale", lambda: verify_step(["bounds", [0, 0, 0], [1, 0, 0]], (), triangle))
    singleton = {**problem, "box": [[x, x] for x in parent]}
    records = [{"kind": "node", "sequence": j, "prefix": list(parent[:j]),
                "hint": ["bounds", [1] + [0] * N, [1] + [0] * N]} for j in range(N)]
    records.append({"kind": "leaf", "sequence": N, "prefix": list(parent), "result": parent_result})
    records.append({"kind": "finish", "reason": "complete", "internal_prefixes": N, "leaves": 1, "frontier": []})
    complete = replay(records, singleton)
    require(complete["complete_within_generation_budget"], "singleton coverage control failed")
    partial = replay(records[:5], singleton)
    require(not partial["closed_tree_without_survivor"] and partial["frontier"] == [list(parent[:5])], "partial frontier control failed")
    must_reject("missing internal entry", lambda: replay(records[:4] + records[5:], singleton))
    must_reject("missing leaf", lambda: replay(records[:-2] + records[-1:], singleton))
    bad_leaf = {**records[-2], "result": {**parent_result, "reason": "failed_strict_signs"}}
    must_reject("changed leaf classification", lambda: replay(records[:-2] + [bad_leaf, records[-1]], singleton))
    parsed, unfinished = parse_journal(json.dumps(records[0]) + "\n" + '{"kind":"node"')
    require(parsed == records[:1] and unfinished == '{"kind":"node"', "truncated line retention failed")
    must_reject("corrupt complete line", lambda: parse_journal('{"kind":}\n'))
    must_reject("entry after finish", lambda: replay(records + [records[0]], singleton))
    # These two tiny LP fixtures are separate from the selected D56 attempt.
    observations = []
    emit = lambda kind, **values: observations.append({"kind": kind, **values})
    deadline = time.perf_counter() + 2.0
    solver = SuggestionSolver(triangle, deadline, emit)
    hint = solver.hint((2,), 0)
    require(verify_step(hint, (2,), triangle) == [0], "tiny LP coordinate interface failed")
    empty_triangle = {**triangle, "box": [[0, 2], [1, 2]]}
    second = SuggestionSolver(empty_triangle, deadline, emit)
    empty_hint = second.hint((2,), 1)
    require(verify_step(empty_hint, (2,), empty_triangle) == [], "tiny LP separation interface failed")
    return {"fixed_29_vertex_and_sign_row_reconstruction": "pass", "common_positive_denominator": problem["denominator"],
            "actual_box": problem["box"], "complete_remainder_maps": "pass", "parent_known_qL_fiber": parent_result,
            "center_child_failed_signs": [5, 7, 13, 15, 17, 19, 23], "small_exact_bound_cases": exact_cases,
            "pure_replay_singleton_and_partial_frontier": "pass", "rejected_bad_inputs": rejected,
            "truncated_last_line_preserved_without_removing_frontier": "pass",
            "tiny_LP_only_dimension": 2, "tiny_LP_total_run_calls": solver.calls + second.calls,
            "tiny_LP_hints": [hint, empty_hint], "tiny_LP_observations": observations,
            "D56_LP_search_calls": 0, "Mahler_root_calls": 0, "selected_tree_attempt": "not run"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("generate")
    commands.add_parser("retain")
    commands.add_parser("controls").add_argument("--output", type=Path, required=True)
    verification = commands.add_parser("verify")
    verification.add_argument("--proof", type=Path, default=PROOF)
    verification.add_argument("--output", type=Path, required=True)
    internal = commands.add_parser("_worker")
    internal.add_argument("--started", type=float, required=True)
    internal.add_argument("--journal", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "generate":
        generate()
    elif args.command == "retain":
        retain()
    elif args.command == "_worker":
        worker(args.started, args.journal)
    else:
        require(not args.output.exists(), "preserve earlier checking output")
        result = controls() if args.command == "controls" else verify(args.proof)
        write_new(args.output, result)
        print(json.dumps({key: value for key, value in result.items() if key not in ("tiny_LP_observations", "frontier", "terminal_record", "pending_started_prefix")}, indent=2))
