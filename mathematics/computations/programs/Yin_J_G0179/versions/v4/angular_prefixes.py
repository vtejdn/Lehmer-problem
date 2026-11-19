"""Count complete vectors removed by angular Fejer tests and the version-two sieve."""

import json
import runpy
from fractions import Fraction
from itertools import combinations
from math import lcm, prod
from pathlib import Path

import numpy as np


VERSION = Path(__file__).resolve().parent
PREVIOUS = runpy.run_path(str(VERSION.parent / "v2" / "cyclotomic_prefixes.py"))
OUTPUT = PREVIOUS["OUTPUT"]
DEPTH = PREVIOUS["DEPTH"]
T = PREVIOUS["T"]
SCALE = 10**7
HORIZONS = (10, 15)
COSINES = tuple(sorted({Fraction(j, 8) for j in range(-8, 9)} |
                       {sign * Fraction(j, d) for sign in (-1, 1)
                        for j, d in ((15, 16), (31, 32), (63, 64))}))


def angular_tests(degree):
    """Construct the signed integer numerator, denominator and cap of every test."""
    tests = []
    for cosine in COSINES:
        multiples = [Fraction(1), cosine]
        for k in range(2, DEPTH + 1):
            multiples.append(2 * cosine * multiples[-1] - multiples[-2])
        for n in HORIZONS:
            weights = [Fraction(-2 * (n+1-k), n+1) * multiples[k] for k in range(1, n+1)]
            cap = degree + sum(abs(w) * (T**k + T**(-k) - 2)
                               for k, w in enumerate(weights, 1))
            denom = lcm(cap.denominator, *(w.denominator for w in weights))
            exact = [int(w * denom) for w in weights]
            floors = [int(w * SCALE // 1) for w in weights]
            tests.append((n, floors, int(cap * SCALE // 1), exact, int(cap * denom)))
    return tests


def reject_angular(rows, bounds, tests):
    failed = np.zeros(len(rows), dtype=bool)
    for n, weights, cap, exact, rhs in tests:
        # Each individual score has magnitude below 2 * SCALE * sum(bounds[:15])
        # in these boxes, so a signed 64-bit product and sum are exact.
        scores = rows[:, :n] @ np.array(weights, dtype=np.int64)
        precision = sum(bounds[:n])
        failed |= scores > cap + precision
        uncertain = np.flatnonzero(~failed & (scores > cap - precision))
        for i in uncertain:
            failed[i] = sum(int(x) * y for x, y in zip(rows[i], exact)) > rhs
    return failed


def reject_previous(rows, bounds, tests):
    rejected = np.zeros(len(rows), dtype=bool)
    for m in PREVIOUS["ORDERS"]:
        scores = np.zeros(len(rows), dtype=np.int64)
        for n in range(1, DEPTH + 1):
            test = tests["trace_box", m, n]
            scores += test[0] * rows[:, n-1].astype(np.int64)
            new, _ = PREVIOUS["compare"](rows, scores, sum(bounds[:n]), test)
            rejected |= new
    return rejected


def reject_matrices(rows, bounds, degree, n):
    """Use exact symmetric Toeplitz bordering once per distinct prefix."""
    if not len(rows):
        return np.empty(0, dtype=bool)
    error = sum(T**(2*j-n) + T**(n-2*j) - 2 for j in range(n+1)) / 2
    shift = Fraction(int(100 * error // 1) + 1, 100)
    scale = shift.denominator
    diagonal = degree * scale + shift.numerator
    keys = np.zeros(len(rows), dtype=np.int64)
    parent_keys = np.array([0], dtype=np.int64)
    coefficients = np.array([[1]], dtype=object)
    determinant = np.array([diagonal], dtype=object)
    for k in range(1, n + 1):
        # Every batch has a fixed first pair. Only later indices need encoding.
        base = 1 if k <= 2 else 2*bounds[k-1] + 1
        if k > 2:
            keys = keys * base + (rows[:, k-1] + bounds[k-1])
        current_keys, first, inverse = np.unique(keys, return_index=True, return_inverse=True)
        parent = np.searchsorted(parent_keys, current_keys // base)
        d = determinant[parent]
        a = coefficients[parent, :]
        traces = rows[first, :k].astype(np.int64) * scale
        x = a[:, 0] * traces[:, -1]
        for j in range(1, k):
            x += a[:, j] * traces[:, -1-j]
        valid = abs(x) < d
        if k == n:
            return ~valid[inverse]
        # Failed parents have zero determinant and stay failed. Only the live
        # entries need bordering; each indicated division is an integer identity.
        new_d = np.zeros(len(first), dtype=object)
        new_a = np.zeros((len(first), k + 1), dtype=object)
        live = np.flatnonzero(valid)
        p = a[live, 0]
        dx, xx = d[live], x[live]
        new_d[live] = (dx * dx - xx * xx) // p
        new_a[live, 0] = dx
        new_a[live, k] = -xx
        for j in range(1, k):
            new_a[live, j] = (dx * a[live, j] - xx * a[live, k-j]) // p
        determinant, coefficients, parent_keys = new_d, new_a, current_keys
    raise AssertionError("missing final Toeplitz test")


def count_box(degree, bounds, angular, previous):
    factors, _ = PREVIOUS["completion_factors"](bounds)
    counts = [0, 0, 0, 0, 0, 0]
    for first in range(-bounds[0], bounds[0] + 1):
        for second in range(-bounds[1], bounds[1] + 1):
            if (first - second) % 2:
                continue
            rows = PREVIOUS["prefixes"](bounds, first, second)
            if not len(rows):
                continue
            extensions = np.ones(len(rows), dtype=np.uint64)
            for scope, table in factors:
                indices = tuple(rows[:, k-1] + bounds[k-1] for k in scope)
                extensions *= table[indices]
            old = reject_previous(rows, bounds, previous)
            new = reject_angular(rows, bounds, angular)
            candidate = ~old & ~new
            excluded = []
            for n in HORIZONS:
                active = np.flatnonzero(candidate)
                fail = reject_matrices(rows[active], bounds, degree, n)
                indices = active[fail]
                excluded.append(indices)
                candidate[indices] = False
            masks = (candidate, *excluded, ~old & new, old & ~new, old & new)
            for i, mask in enumerate(masks):
                counts[i] += int(extensions[mask].sum())
    return counts


def named_prefix(degree, bounds, previous):
    """Certify the comparisons for every extension of the ten negative sixes."""
    n = 10
    error = sum(Fraction(2 * (n+1-k), n+1) * (T**k + T**(-k) - 2)
                for k in range(1, n+1))
    assert error < Fraction(1647, 1000) and degree - 60 + error < 0
    worst = Fraction(0)
    for order in PREVIOUS["ORDERS"]:
        for n in range(1, DEPTH + 1):
            _, _, weights, cap = previous["trace_box", order, n]
            score = sum(-6*w for w in weights[:10])
            score += sum(bounds[k] * abs(weights[k]) for k in range(10, n))
            worst = max(worst, Fraction(score, cap))
    assert worst < Fraction(4, 5)
    return PREVIOUS["constant_six_count"](bounds)


def census(degree, bounds, previous_remaining):
    angular = angular_tests(degree)
    previous = PREVIOUS["inequalities"](degree, bounds)
    named = named_prefix(degree, bounds, previous)
    counts = count_box(degree, bounds, angular, previous)
    primes = [p for p, _ in PREVIOUS["prime_powers"](degree)]
    for size in range(1, len(primes) + 1):
        for selection in combinations(primes, size):
            divisor = prod(selection)
            restricted = [b if i % divisor == 0 else 0 for i, b in enumerate(bounds, 1)]
            terms = count_box(degree, restricted, angular, previous)
            counts = [v + (-1)**size * w for v, w in zip(counts, terms)]
    assert all(v % 2 == 0 for v in counts)
    counts = [v // 2 for v in counts]
    assert sum(counts[:4]) == previous_remaining
    assert counts[3] >= named
    return dict(zip(("remaining", "matrix_10_extra", "matrix_15_extra", "angular_only",
                     "previous_only", "previous_and_angular"), counts))


def main():
    inputs = json.loads((OUTPUT / "prefixes.json").read_text(encoding="utf-8"))
    earlier = json.loads((OUTPUT / "versions" / "v2" / "results.json").read_text(encoding="utf-8"))
    results = {}
    for degree in (56, 58):
        baseline = inputs[str(degree)]["certified_all_available"]
        old = earlier[str(degree)]["no_power_substitution_up_to_sign"]
        results[str(degree)] = census(degree, baseline["bounds"],
                                      old["total"] - old["trace_box_through_15_all_orders"])
        assert sum(results[str(degree)].values()) == baseline["no_power_substitution_up_to_sign"]
    destination = OUTPUT / "versions" / "v4" / "results.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
