"""Independent D110 review: slab slicing, inverse reachability, backward DP.

No author mathematical function is used by the independent calculation.
The author main is separately replayed with its output intercepted in memory.
Only reviewer_orbit_result.json is written; native inputs are byte-compared.
"""
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import datetime
import importlib.util
import io
import json
import sys
import time

F = Fraction
BASE = (_J_PROGRAM / 'reviewer_orbit_verify.py').parent
HEIGHTS = (2, 4, 7, 12, 19)
TIMES = (4, 5, 16, 32, 64)
ZERO = (0, 0, 0, 0)
SCALE = 1000000
CAP = 100000


def pack(x):
    return dict(numerator=x.numerator, denominator=x.denominator)


def unpack(x):
    assert set(x) == {"numerator", "denominator"}
    assert type(x["numerator"]) is int and type(x["denominator"]) is int
    value = F(x["numerator"], x["denominator"])
    assert pack(value) == x
    return value


def up(x):
    return (x.numerator + x.denominator - 1) // x.denominator


def dn(x):
    return x.numerator // x.denominator


def polynomial(x):
    acc = F(1)
    for coefficient in (-1, -1, -1, 1):
        acc = acc*x + coefficient
    return acc


def independent_constants():
    left, right, root13 = F(861, 500), F(1723, 1000), F(721, 200)
    assert polynomial(left) < 0 < polynomial(right)
    assert root13**2 < 13
    c0 = (right**2 + 1/left) / ((left-1)*root13*(left-1/left))
    c1sq = 8 / (13*(1+root13))
    assert c0 < F(6, 5) and c1sq < F(121, 900)
    assert [dn(F(6, 5)+F(11, 30)*(n//2)) for n in (16, 32, 64)] == [4, 7, 12]
    slabs = []
    for l, u, radius in ((left, right, F(500, 361)),
                         (1/right, 1/left, F(861, 361))):
        assert l > F(1, 2)
        functions = (lambda x: -1/x, lambda x: x*x-x-1,
                     lambda x: x-1, lambda x: F(1))
        intervals = [[dn(f(l)*SCALE), up(f(u)*SCALE)] for f in functions]
        slabs.append([intervals, up(radius*SCALE)])
    record = {"beta_interval": [pack(left), pack(right)],
              "sqrt13_lower": pack(root13), "c0_derived_upper": pack(c0),
              "c1_squared_derived_upper": pack(c1sq),
              "used_c0_upper": pack(F(6, 5)), "used_c1_upper": pack(F(11, 30)),
              "coefficient_interval_scale": SCALE, "strip_enclosures": slabs}
    return slabs, record


def sliced_allowed_set(height, slabs):
    """Enumerate every allowed point by exact q3 interval, before reachability."""
    allowed = set()
    for prefix in product(range(-height, height+1), repeat=3):
        low, high = -height, height
        for intervals, radius in slabs:
            lower = upper = 0
            for value, ends in zip(prefix, intervals[:3]):
                first, last = sorted((value*ends[0], value*ends[1]))
                lower += first
                upper += last
            # q3 has exact coefficient one, hence inclusive integer limits.
            low = max(low, (-radius-upper+SCALE-1)//SCALE)
            high = min(high, (radius-lower)//SCALE)
        for q3 in range(low, high+1):
            allowed.add(prefix+(q3,))
    assert ZERO in allowed
    return allowed


def move(q, digit):
    return q[1], q[2], q[3], digit-q[0]+q[1]+q[2]+q[3]


def predecessor(q, digit):
    return digit+q[0]+q[1]+q[2]-q[3], q[0], q[1], q[2]


def reach(allowed, reverse=False):
    seen = {ZERO}
    stack = [ZERO]
    transformation = predecessor if reverse else move
    while stack:
        current = stack.pop()
        for digit in (0, 1, -1):
            nxt = transformation(current, digit)
            if nxt in allowed and nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
                assert len(seen) < CAP
    return seen


def backward_entries(kept, half):
    """f_n(q) = weighted sum of f_(n-1) at successors, terminal f_0=1_0."""
    states = sorted(kept)
    index = {q: i for i, q in enumerate(states)}
    rows = []
    for q in states:
        row = []
        for digit in (0, 1, -1):
            successor = move(q, digit)
            if successor not in index:
                continue
            if half:
                weight = (6 if digit == 0 else 1) if q[0] % 2 == 0 else (2 if digit == 0 else 3)
            else:
                weight = 2 if digit == 0 else 1
            row.append((index[successor], weight))
        rows.append(row)
    at_zero = index[ZERO]
    values = [int(i == at_zero) for i in range(len(states))]
    denominator = 8 if half else 4
    out = {}
    for step in range(1, 65):
        values = [sum(weight*values[target] for target, weight in row) for row in rows]
        if step in TIMES:
            out[str(step)] = pack(F(values[at_zero], denominator**step))
    return out


def gray_binary_control():
    """All 2^16 words, Gray-code updates of independently reduced powers."""
    powers = [(1, 0, 0, 0)]
    for _ in range(15):
        coefficients = [0]+list(powers[-1])
        leading = coefficients.pop()
        for j, p_j in enumerate((1, -1, -1, -1)):
            coefficients[j] -= leading*p_j
        powers.append(tuple(coefficients))
    counter = Counter({ZERO: 1})
    current = [0, 0, 0, 0]
    previous_gray = 0
    for word in range(1, 1 << 16):
        gray = word ^ (word >> 1)
        changed = gray ^ previous_gray
        position = changed.bit_length()-1
        sign = 1 if gray & changed else -1
        for j in range(4):
            current[j] += sign*powers[position][j]
        counter[tuple(current)] += 1
        previous_gray = gray
    assert sum(counter.values()) == 1 << 16
    pairs = sum(n*n for n in counter.values())
    return {"time": 16, "distinct_binary_endpoints": len(counter),
            "total_words": 1 << 16, "collision_pair_count": pairs,
            "collision": pack(F(pairs, 4**16))}


def independent_tail(theta, n, height):
    x = (F(height)-F(6, 5))**2 / (2*(1+theta)*n*F(121, 900))
    degree = (2*x.numerator+x.denominator-1)//x.denominator + 80
    # Direct factorial/power formula, summed in reverse order; no author recurrence.
    terms = [F(x.numerator**j, x.denominator**j*factorial(j)) for j in range(degree+2)]
    total = sum(reversed(terms[:-1]), F(0))
    ratio = x/(degree+2)
    assert 0 <= ratio < 1
    remainder = terms[-1]/(1-ratio)
    lower, upper = 1/(total+remainder), 1/total
    assert 0 < lower <= upper <= 1
    factor = F(16384)/(1+theta)
    return {"exponent": pack(x), "exp_lower": pack(lower), "exp_upper": pack(upper),
            "original_error_lower": pack(factor*lower),
            "original_error_upper": pack(factor*upper)}


def strict_compare(actual, expected, location="root"):
    assert type(actual) is type(expected), (location, type(actual), type(expected))
    if isinstance(actual, dict):
        assert actual.keys() == expected.keys(), location
        return sum(strict_compare(actual[k], expected[k], location+"."+k) for k in actual)
    if isinstance(actual, list):
        assert len(actual) == len(expected), location
        return sum(strict_compare(a, b, location+f"[{i}]") for i, (a, b) in enumerate(zip(actual, expected)))
    assert actual == expected, (location, actual, expected)
    return 1


def independent_payload():
    slabs, constants = independent_constants()
    boxes = []
    extra_stats = []
    for height in HEIGHTS:
        allowed = sliced_allowed_set(height, slabs)
        forward, backward = reach(allowed), reach(allowed, reverse=True)
        kept = forward & backward
        edges = sum(move(q, e) in kept for q in kept for e in (0, 1, -1))
        records = {"zero": backward_entries(kept, False), "half": backward_entries(kept, True)}
        for label, theta in (("zero", F(0)), ("half", F(1, 2))):
            assert unpack(records[label]["4"]) == ((1+theta)/2)**4
            assert unpack(records[label]["5"]) == ((1+theta)/2)**5 + (1+theta)*(1-theta)**4/512
        boxes.append({"height": height, "full_box_states": (2*height+1)**4,
                      "forward_reached_states": len(forward), "returning_graph_states": len(kept),
                      "retained_edges": edges, "cap": CAP, "exact_entries": records})
        extra_stats.append({"height": height, "all_strip_allowed_points": len(allowed),
                            "forward": len(forward), "backward_in_all_allowed": len(backward),
                            "intersection": len(kept), "edges": edges})
    table = {row["height"]: row for row in boxes}
    comparisons = []
    for n, full_height in ((16, 4), (32, 7), (64, 12)):
        for label, theta in (("zero", F(0)), ("half", F(1, 2))):
            full = unpack(table[full_height]["exact_entries"][label][str(n)])
            for height in HEIGHTS:
                retained = unpack(table[height]["exact_entries"][label][str(n)])
                assert retained <= full
                if height >= full_height:
                    assert retained == full
                cost = independent_tail(theta, n, height)
                comparisons.append({"time": n, "theta": label, "height": height,
                                    "deterministic_complete_height": full_height,
                                    "retained_entry": pack(retained), "full_entry": pack(full),
                                    "exact_omitted_entry": pack(full-retained), "tail_certificate": cost,
                                    "original_upper_with_generic_tail": pack(4096*retained/(1+theta)+unpack(cost["original_error_upper"])),
                                    "original_upper_with_exact_omission": pack(4096*full/(1+theta))})
    eighteen = independent_tail(F(1, 2), 64, 18)
    nineteen = independent_tail(F(1, 2), 64, 19)
    assert unpack(eighteen["original_error_lower"]) > F(1, 16)
    assert unpack(nineteen["original_error_upper"]) < F(1, 16)
    control = gray_binary_control()
    assert control["collision"] == table[4]["exact_entries"]["zero"]["16"]
    p64 = unpack(table[12]["exact_entries"]["zero"]["64"])
    b64 = unpack(table[12]["exact_entries"]["half"]["64"])
    converted = F(8192, 3)*b64
    summaries = []
    for label, value, lower, upper in (
        ("p64", p64, F("4.5642e-17"), F("4.5643e-17")),
        ("b64_half", b64, F("1.0611e-8"), F("1.0612e-8")),
        ("zero_tail_original_bound_half", converted, F("2.8977e-5"), F("2.8978e-5")),
        ("generic_original_bound_half_H19", converted+unpack(nineteen["original_error_upper"]), F("0.05104"), F("0.05105")),
        ("positive_theta_bound_over_exact_p64", converted/p64, F(10**11), F(10**12))):
        assert lower < value < upper
        summaries.append({"quantity": label, "lower": pack(lower), "upper": pack(upper)})
    for label, bound in (("zero", F("2.079e-9")), ("half", F("2.702e-19"))):
        full = unpack(table[12]["exact_entries"][label]["64"])
        retained = unpack(table[4]["exact_entries"][label]["64"])
        relative = (full-retained)/full
        assert 0 < relative < bound
        summaries.append({"quantity": f"exact_relative_omission_H4_{label}",
                          "exact_value": pack(relative), "lower": pack(F(0)), "upper": pack(bound)})
    payload = {"scope": {"polynomial_coefficients_ascending": [1, -1, -1, -1, 1],
                          "theta": [pack(F(0)), pack(F(1, 2))], "times": list(TIMES), "heights": list(HEIGHTS),
                          "predeclared_original_error_target": pack(F(1, 16)), "target_time": 64,
                          "target_theta": pack(F(1, 2)), "cap": CAP},
               "constants": constants, "boxes": boxes, "comparisons": comparisons,
               "predeclared_target_verification": {"height_18_fails": True, "height_19_passes": True,
                                                    "certificate_18": eighteen, "certificate_19": nineteen},
               "direct_original_binary_control": control, "certified_summary_intervals": summaries}
    return payload, extra_stats


def replay_author_in_memory():
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("j52_author_readonly", (_J_PROGRAM / 'experiment.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    destination = _J_OUTPUT/"reviewer_memory_only_no_file.json"
    captured = []
    old_argv, old_write = sys.argv, Path.write_text

    def capture(path, data, *args, **kwargs):
        assert path == destination, path
        captured.append(json.loads(data))
        return len(data)

    try:
        sys.argv = [str((_J_PROGRAM / 'experiment.py')), "--output", str(destination)]
        Path.write_text = capture
        with redirect_stdout(io.StringIO()):
            module.main()
    finally:
        sys.argv, Path.write_text = old_argv, old_write
    assert len(captured) == 1 and not destination.exists()
    return captured[0]


def main():
    author_names = ("experiment.py", "result.json", "initial_result.json", "readme.md")
    native = {name: (((_J_PROGRAM if name in ('experiment.py', 'readme.md', 'reviewer_orbit_verify.py') else _J_OUTPUT) / name)).read_bytes() for name in author_names}
    draft = (_J_ROOT / 'mathematics/drafts/Yin_D_G0110.md')
    # Draft presence and accidental byte changes are operational reminders,
    # never mathematical inputs or gates.  Fixed retention may retire D110.
    draft_bytes = draft.read_bytes() if draft.exists() else None
    final = json.loads(native["result.json"])
    initial = json.loads(native["initial_result.json"])
    start = time.perf_counter()
    independent, graph_details = independent_payload()
    independent_leaves = strict_compare(final, independent)
    initial_leaves = strict_compare(initial, {k: independent[k] for k in initial})
    replayed = replay_author_in_memory()
    replay_leaves = strict_compare(replayed, final)
    preservation = {name: (((_J_PROGRAM if name in ('experiment.py', 'readme.md', 'reviewer_orbit_verify.py') else _J_OUTPUT) / name)).exists() and (((_J_PROGRAM if name in ('experiment.py', 'readme.md', 'reviewer_orbit_verify.py') else _J_OUTPUT) / name)).read_bytes() == data
                    for name, data in native.items()}
    draft_preserved = (None if draft_bytes is None else
                       draft.exists() and draft.read_bytes() == draft_bytes)
    reminders = [name + ": bytes changed or file disappeared; inspect operationally"
                 for name, unchanged in preservation.items() if not unchanged]
    if draft_preserved is False:
        reminders.append("D110: bytes changed or file disappeared; inspect operationally")
    output = {'reviewer': 'orbit_research, noncontributor to D110/J52', 'passed': True, 'independent_methods': ['enumerate full allowed lattice by three-coordinate slab slicing', 'separate forward and inverse-map depth-first reachability', 'backward weighted terminal recursion for both laws', 'direct factorial-power rational exponential intervals', 'all 65536 binary words by Gray-code updates of quotient-ring powers'], 'independent_final_scalar_fields_matched': independent_leaves, 'independent_initial_scalar_fields_matched': initial_leaves, 'author_readonly_replay_scalar_fields_matched': replay_leaves, 'all_50_entries_and_30_comparisons_verified': True, 'all_retained_non_timing_JSON_values_and_types_verified': True, 'independent_graph_details': graph_details, 'direct_binary_control': independent['direct_original_binary_control'], 'independent_box_entries': independent['boxes'], 'certified_summary_intervals': independent['certified_summary_intervals']}
    ((_J_OUTPUT / 'reviewer_orbit_result.json')).write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({'passed': True, 'fields': independent_leaves, 'initial_fields': initial_leaves, 'read_only_replay_fields': replay_leaves, 'graphs': graph_details}))


if __name__ == "__main__":
    main()
