"""Count complete J179 vectors eliminated by cyclotomic tests on short prefixes."""

import json
import runpy
from fractions import Fraction as F
from itertools import combinations
from math import lcm, prod
from pathlib import Path

import numpy as np


GROUP = Path(__file__).resolve().parents[2]
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name
BASE = runpy.run_path(str(GROUP / "count_prefixes.py"))
prime_powers = BASE["prime_powers"]
R, T = F(21, 25), F(1089, 1000)
DEPTH = 15
HORIZONS = (10, 12, 15)
SCALE = 10**10
ORDERS = (1, 2, 3, 4, 6)
PERIODS = {1: (1,), 2: (1, -1), 3: (2, -1, -1),
           4: (2, 0, -2, 0), 6: (2, 1, -1, -2, -1, 1)}


def geometric_tail(degree, n):
    j = n+1
    return ((degree-2)*R**j/(1-R) + (R*T)**j/(1-R*T)
            + (R/T)**j/(1-R/T)) / j


def inequalities(degree, certified):
    """Normalized weights and caps, all rational, for each order and prefix length."""
    half = degree//2
    result = {}
    for m in ORDERS:
        c = PERIODS[m]
        w = [F(0)] + [R**k*c[k % m]/(k*c[0]) for k in range(1, half+1)]
        floors = [int(wk*SCALE // 1) for wk in w]
        for n in range(1, DEPTH+1):
            direct = geometric_tail(degree, n)
            split = (sum(abs(w[k])*certified[k-1] for k in range(n+1, half+1))
                     + geometric_tail(degree, half))
            for label, tail in (("geometric", direct), ("trace_box", min(direct, split))):
                cap = F(7*degree, 80) + tail
                denom = lcm(cap.denominator, *(wk.denominator for wk in w[1:n+1]))
                exact = [int(wk*denom) for wk in w[1:n+1]]
                result[label, m, n] = (floors[n], int(cap*SCALE // 1),
                                        exact, int(cap*denom))
    return result


def completion_factors(bounds):
    """Sum out the indices past DEPTH, leaving small tables on prefix variables."""
    sizes = {k: 2*b+1 for k, b in enumerate(bounds, 1)}
    values = {k: np.arange(-b, b+1) for k, b in enumerate(bounds, 1)}
    factors = []
    high = list(range(DEPTH+1, len(bounds)+1))
    for k in high:
        for p, modulus in prime_powers(k):
            j = k//p
            difference = values[j][:, None] - values[k][None, :]
            factors.append(((j, k), (difference % modulus == 0).astype(np.uint64)))
    peak = 0
    while high:
        bags = {k: sorted(set().union(*(scope for scope, _ in factors if k in scope)))
                for k in high}
        k = min(high, key=lambda j: prod(sizes[a] for a in bags[j]))
        bag = bags[k]
        peak = max(peak, prod(sizes[a] for a in bag))
        joint = np.array(1, dtype=np.uint64)
        rest = []
        for scope, arr in factors:
            if k not in scope:
                rest.append((scope, arr))
                continue
            joint = joint * arr.reshape(tuple(sizes[a] if a in scope else 1 for a in bag))
        rest.append((tuple(a for a in bag if a != k), joint.sum(axis=bag.index(k))))
        factors = rest
        high.remove(k)
    return factors, peak


def prefixes(bounds, first, second):
    """Generate the legal low sums extending one prescribed legal first pair."""
    rows = np.array([[first, second]], dtype=np.int16)
    for k in range(3, DEPTH+1):
        blocks = []
        for val in range(-bounds[k-1], bounds[k-1]+1):
            match = np.ones(len(rows), dtype=bool)
            for p, modulus in prime_powers(k):
                match &= (rows[:, k//p-1] - val) % modulus == 0
            subset = rows[match]
            if len(subset):
                blocks.append(np.column_stack((subset, np.full(len(subset), val, dtype=np.int16))))
        if not blocks:
            return np.empty((0, DEPTH), dtype=np.int16)
        rows = np.concatenate(blocks)
    return rows


def compare(rows, scores, precision, test):
    """Resolve the integer margin exactly when the scaled floor estimate overlaps it."""
    _, cap_floor, exact, cap = test
    rejected = scores > cap_floor + precision
    uncertain = np.flatnonzero((scores <= cap_floor + precision) & (scores > cap_floor - precision))
    for index in uncertain:
        rejected[index] = sum(int(a)*b for a, b in zip(rows[index], exact)) > cap
    return rejected, len(uncertain)


def count_selection(degree, bounds, tests):
    """Count entire vectors via prefix weights, before power-substitution exclusions."""
    factors, peak = completion_factors(bounds)
    profiles = {(method, n, group): 0 for method in ("geometric", "trace_box")
                for n in HORIZONS for group in ("endpoints", "all_orders")}
    total = prefix_count = exact_cases = example = 0
    first_pairs = ((a, b) for a in range(-bounds[0], bounds[0]+1)
                   for b in range(-bounds[1], bounds[1]+1) if (a-b) % 2 == 0)
    for first, second in first_pairs:
        rows = prefixes(bounds, first, second)
        if not len(rows):
            continue
        prefix_count += len(rows)
        completions = np.ones(len(rows), dtype=np.uint64)
        for scope, table in factors:
            indices = tuple(rows[:, k-1] + bounds[k-1] for k in scope)
            completions *= table[indices]
        total += int(completions.sum())
        if abs(first) == 6:
            example_row = [6 if first > 0 or k % 2 == 0 else -6 for k in range(1, 11)]
            example += int(completions[np.all(rows[:, :10] == example_row, axis=1)].sum())
        for method in ("geometric", "trace_box"):
            scores = {m: np.zeros(len(rows), dtype=np.int64) for m in ORDERS}
            failed = {m: np.zeros(len(rows), dtype=bool) for m in ORDERS}
            for n in range(1, DEPTH+1):
                values = rows[:, n-1].astype(np.int64)
                precision = sum(bounds[:n])
                for m in ORDERS:
                    test = tests[method, m, n]
                    scores[m] += test[0]*values
                    reject, cases = compare(rows, scores[m], precision, test)
                    failed[m] |= reject
                    exact_cases += cases
                if n in HORIZONS:
                    endpoints = failed[1] | failed[2]
                    profiles[method, n, "endpoints"] += int(completions[endpoints].sum())
                    rejected = endpoints | failed[3] | failed[4] | failed[6]
                    profiles[method, n, "all_orders"] += int(completions[rejected].sum())
    result = {f"{method}_through_{n}_{group}": v for (method, n, group), v in profiles.items()}
    result.update(total=total, named_pair=example)
    return result, {"prefix_count": prefix_count, "largest_high_table_entries": peak,
                    "exact_margin_comparisons": exact_cases}


def constant_six_count(bounds):
    """Independent Euler-coordinate count for s_1=...=s_10=6 through index 29."""
    half = len(bounds)
    if not 10 <= half <= 29 or min(bounds[:10]) < 6:
        raise ValueError("The named prefix formula requires ten admissible sixes and index at most 29")
    paired = set()
    result = 1
    for j in range(11, half//2+1):
        paired.update((j, 2*j))
        result *= sum(1 for s in range(-bounds[j-1], bounds[j-1]+1) if (s-6) % j == 0
                      for u in range(-bounds[2*j-1], bounds[2*j-1]+1) if (u-s) % (2*j) == 0)
    for j in range(11, half+1):
        if j not in paired:
            result *= sum((s-6) % j == 0 for s in range(-bounds[j-1], bounds[j-1]+1))
    return result


def census(degree, bounds, baseline):
    tests = inequalities(degree, bounds)
    raw, diagnostics = count_selection(degree, bounds, tests)
    assert raw["total"] == baseline["count"]
    primitive = raw.copy()
    primes = [p for p, _ in prime_powers(degree)]
    for n in range(1, len(primes)+1):
        for selected in combinations(primes, n):
            divisor = prod(selected)
            restricted = [b if k % divisor == 0 else 0 for k, b in enumerate(bounds, 1)]
            subset, _ = count_selection(degree, restricted, tests)
            for key in primitive:
                primitive[key] += (-1)**n * subset[key]
    assert all(v % 2 == 0 for v in primitive.values())
    representatives = {key: v//2 for key, v in primitive.items()}
    assert representatives["total"] == baseline["no_power_substitution_up_to_sign"]
    assert representatives["named_pair"] == constant_six_count(bounds)
    assert 0 < representatives["named_pair"] <= representatives["geometric_through_10_endpoints"]
    return {"all_vectors": raw, "no_power_substitution_up_to_sign": representatives,
            "diagnostics_all_vectors": diagnostics}


def main():
    assert R*T*T <= 1
    inputs = json.loads((OUTPUT / "prefixes.json").read_text(encoding="utf-8"))
    report = {}
    for degree in (56, 58):
        baseline = inputs[str(degree)]["certified_all_available"]
        report[str(degree)] = census(degree, baseline["bounds"], baseline)
    destination = OUTPUT / "versions" / "v2" / "results.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
