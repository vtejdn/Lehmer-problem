"""Bounded exact quartic finite-box experiment. D110 owns the proof."""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction as F
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import time

HEIGHTS = (2, 4, 7, 12, 19)
TIMES = (4, 5, 16, 32, 64)
CAP = 100000
SCALE = 10**6
ZERO = (0, 0, 0, 0)


def ceil(x):
    return -((-x.numerator) // x.denominator)


def floor(x):
    return x.numerator // x.denominator


def frac(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


def poly(t):
    return t**4 - t**3 - t**2 - t + 1


def constants():
    lo, hi, sqrt13_lo = F(861, 500), F(1723, 1000), F(721, 200)
    assert poly(lo) < 0 < poly(hi)
    assert sqrt13_lo**2 < 13
    c0_upper = (hi**2 + 1 / lo) / ((lo - 1) * sqrt13_lo * (lo - 1 / lo))
    c1_squared_upper = F(4) / (13 * (1 + sqrt13_lo) / 2)
    assert c0_upper < F(6, 5)
    assert c1_squared_upper < F(11, 30)**2
    assert [floor(F(6, 5) + F(11, 30) * (n // 2)) for n in (16, 32, 64)] == [4, 7, 12]
    strips = []
    for a, b, bound in ((lo, hi, 1 / (lo - 1)),
                        (1 / hi, 1 / lo, lo / (lo - 1))):
        assert a > F(1, 2)
        coeffs = ((-1 / a, -1 / b),
                  (a*a-a-1, b*b-b-1), (a-1, b-1), (F(1), F(1)))
        intervals = [(floor(x * SCALE), ceil(y * SCALE)) for x, y in coeffs]
        strips.append((intervals, ceil(bound * SCALE)))
    return strips, {"beta_interval": [frac(lo), frac(hi)],
                    "sqrt13_lower": frac(sqrt13_lo),
                    "c0_derived_upper": frac(c0_upper),
                    "c1_squared_derived_upper": frac(c1_squared_upper),
                    "used_c0_upper": frac(F(6, 5)), "used_c1_upper": frac(F(11, 30)),
                    "coefficient_interval_scale": SCALE, "strip_enclosures": strips}


def allowed(q, height, strips):
    if max(map(abs, q)) > height:
        return False
    for intervals, bound in strips:
        lower = sum(x * (a if x >= 0 else b) for x, (a, b) in zip(q, intervals))
        upper = sum(x * (b if x >= 0 else a) for x, (a, b) in zip(q, intervals))
        if lower > bound or upper < -bound:
            return False
    return True


def successors(q):
    base = -q[0] + q[1] + q[2] + q[3]
    return [(e, (q[1], q[2], q[3], base + e)) for e in (-1, 0, 1)]


def graph(height, strips):
    states = [ZERO]
    indices = {ZERO: 0}
    edges = []
    for q in states:
        row = []
        for e, target in successors(q):
            if not allowed(target, height, strips):
                continue
            if target not in indices:
                if len(states) >= CAP:
                    raise RuntimeError(f"Reached-state cap {CAP} hit at H={height}; incomplete")
                indices[target] = len(states)
                states.append(target)
            row.append((indices[target], e))
        edges.append(row)
    reverse = [[] for _ in states]
    for i, row in enumerate(edges):
        for j, _ in row:
            reverse[j].append(i)
    can_return = {0}
    queue = deque([0])
    while queue:
        for predecessor in reverse[queue.popleft()]:
            if predecessor not in can_return:
                can_return.add(predecessor)
                queue.append(predecessor)
    kept = sorted(can_return)
    remap = {j: i for i, j in enumerate(kept)}
    assert kept[0] == 0
    kept_states = [states[i] for i in kept]
    kept_edges = [[(remap[j], e) for j, e in edges[i] if j in remap] for i in kept]
    statistics = {"height": height, "full_box_states": (2*height+1)**4,
                  "forward_reached_states": len(states), "returning_graph_states": len(kept),
                  "retained_edges": sum(map(len, kept_edges)), "cap": CAP}
    return kept_states, kept_edges, statistics


def entries(states, edges, theta):
    assert theta in (F(0), F(1, 2))
    denominator = 4 if theta == 0 else 8
    values = [0] * len(states)
    values[0] = 1
    out = {}
    for n in range(1, max(TIMES) + 1):
        nxt = [0] * len(states)
        for i, value in enumerate(values):
            if not value:
                continue
            even = states[i][0] % 2 == 0
            for j, e in edges[i]:
                weight = (2 if e == 0 else 1) if theta == 0 else ((6 if e == 0 else 1) if even else (2 if e == 0 else 3))
                nxt[j] += value * weight
        values = nxt
        if n in TIMES:
            value = F(values[0], denominator**n)
            out[str(n)] = frac(value)
    return out


def unfrac(record):
    return F(record["numerator"], record["denominator"])


def direct_binary_collision(n):
    """Author cross-control using actual binary endpoint sums, no quotient graph."""
    counts = {ZERO: 1}
    for _ in range(n):
        nxt = {}
        for (a, b, c, d), count in counts.items():
            for digit in (0, 1):
                target = (digit-d, a+d, b+d, c+d)
                nxt[target] = nxt.get(target, 0) + count
        counts = nxt
    assert sum(counts.values()) == 2**n
    numerator = sum(value*value for value in counts.values())
    return {"time": n, "distinct_binary_endpoints": len(counts),
            "total_words": 2**n, "collision_pair_count": numerator,
            "collision": frac(F(numerator, 4**n))}


def exp_negative_interval(x):
    """Reciprocal Taylor enclosure: every operation is rational."""
    assert x >= 0
    if not x:
        return F(1), F(1)
    degree = ceil(2 * x) + 80
    term = total = F(1)
    for k in range(1, degree + 1):
        term *= x / k
        total += term
    next_term = term * x / (degree + 1)
    ratio = x / (degree + 2)
    assert ratio < 1
    remainder_upper = next_term / (1 - ratio)
    return 1 / (total + remainder_upper), 1 / total


def tail(theta, n, height):
    exponent = (F(height) - F(6, 5))**2 / (2 * (1 + theta) * n * F(11, 30)**2)
    lo, hi = exp_negative_interval(exponent)
    return {"exponent": frac(exponent),
            "exp_lower": frac(lo), "exp_upper": frac(hi),
            "original_error_lower": frac(4096 * 4 * lo / (1 + theta)),
            "original_error_upper": frac(4096 * 4 * hi / (1 + theta))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=(_J_OUTPUT / 'result.json'))
    args = parser.parse_args()
    start = time.perf_counter()
    strips, certified_constants = constants()
    out = {"scope": {"polynomial_coefficients_ascending": [1, -1, -1, -1, 1],
                     "theta": [frac(F(0)), frac(F(1, 2))], "times": TIMES, "heights": HEIGHTS,
                     "predeclared_original_error_target": frac(F(1, 16)),
                     "target_time": 64, "target_theta": frac(F(1, 2)), "cap": CAP},
           "constants": certified_constants, "boxes": []}
    for height in HEIGHTS:
        states, edges, stats = graph(height, strips)
        records = {}
        for label, theta in (("zero", F(0)), ("half", F(1, 2))):
            records[label] = entries(states, edges, theta)
            assert unfrac(records[label]["4"]) == ((1 + theta) / 2)**4
            assert unfrac(records[label]["5"]) == (1 + theta)**5 / 32 + (1 + theta)*(1 - theta)**4/512
        out["boxes"].append({**stats, "exact_entries": records})
        print(json.dumps(stats), flush=True)
    boxes = {x["height"]: x for x in out["boxes"]}
    comparisons = []
    for n, complete_height in ((16, 4), (32, 7), (64, 12)):
        for label, theta in (("zero", F(0)), ("half", F(1, 2))):
            full = unfrac(boxes[complete_height]["exact_entries"][label][str(n)])
            for height in HEIGHTS:
                retained = unfrac(boxes[height]["exact_entries"][label][str(n)])
                assert retained <= full
                if height >= complete_height:
                    assert retained == full
                cost = tail(theta, n, height)
                upper = 4096 * retained / (1 + theta) + unfrac(cost["original_error_upper"])
                comparisons.append({"time": n, "theta": label, "height": height,
                                    "deterministic_complete_height": complete_height,
                                    "retained_entry": frac(retained), "full_entry": frac(full),
                                    "exact_omitted_entry": frac(full-retained), "tail_certificate": cost,
                                    "original_upper_with_generic_tail": frac(upper),
                                    "original_upper_with_exact_omission": frac(4096*full/(1+theta))})
    out["comparisons"] = comparisons
    # The first feasible integer H for THIS conservative Gaussian certificate.
    target = F(1, 16)
    low = tail(F(1, 2), 64, 18)
    high = tail(F(1, 2), 64, 19)
    assert unfrac(low["original_error_lower"]) > target
    assert unfrac(high["original_error_upper"]) < target
    out["predeclared_target_verification"] = {"height_18_fails": True, "height_19_passes": True,
                                              "certificate_18": low, "certificate_19": high}
    control = direct_binary_collision(16)
    assert unfrac(control["collision"]) == unfrac(boxes[4]["exact_entries"]["zero"]["16"])
    out["direct_original_binary_control"] = control
    p64 = unfrac(boxes[12]["exact_entries"]["zero"]["64"])
    b64 = unfrac(boxes[12]["exact_entries"]["half"]["64"])
    original_bound = 4096*b64/F(3, 2)
    generic_bound = original_bound + unfrac(high["original_error_upper"])
    claims = (("p64", p64, F("4.5642e-17"), F("4.5643e-17")),
              ("b64_half", b64, F("1.0611e-8"), F("1.0612e-8")),
              ("zero_tail_original_bound_half", original_bound, F("2.8977e-5"), F("2.8978e-5")),
              ("generic_original_bound_half_H19", generic_bound, F("0.05104"), F("0.05105")),
              ("positive_theta_bound_over_exact_p64", original_bound/p64, F(10**11), F(10**12)))
    out["certified_summary_intervals"] = []
    for name, value, lower, upper in claims:
        assert lower < value < upper
        out["certified_summary_intervals"].append({"quantity": name, "lower": frac(lower), "upper": frac(upper)})
    for label, upper in (("zero", F("2.079e-9")), ("half", F("2.702e-19"))):
        full = unfrac(boxes[12]["exact_entries"][label]["64"])
        retained = unfrac(boxes[4]["exact_entries"][label]["64"])
        relative = (full-retained)/full
        assert 0 < relative < upper
        out["certified_summary_intervals"].append({"quantity": f"exact_relative_omission_H4_{label}",
                                                 "exact_value": frac(relative), "lower": frac(F(0)), "upper": frac(upper)})
    pass
    args.output.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    summary = []
    for n, height in ((16, 4), (32, 7), (64, 12)):
        p = unfrac(boxes[height]["exact_entries"]["zero"][str(n)])
        b = unfrac(boxes[height]["exact_entries"]["half"][str(n)])
        summary.append({"n": n, "complete_height": height, "p_exact": frac(p), "b_half_exact": frac(b),
                        "p_decimal_non_evidential": float(p), "b_half_decimal_non_evidential": float(b)})
    print(json.dumps({'summary': summary}))


if __name__ == "__main__":
    main()
