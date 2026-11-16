"""Find every integral fixed-profile completion through degree four for p <= 37."""

import argparse
from collections import Counter
from fractions import Fraction
import json
from math import ceil, cos, pi
from pathlib import Path
import tempfile

from sympy import I, Poly, Rational, symbols


ROW_SCALE = 1 << 40
DUAL_SCALE = 1 << 40
PREFIX = [2, 0, 4]
WITNESS = [2, 0, 4, 0, 5, 0, 5, 1, 4, 2, 3, 3, 1, 4, -1, 4, -3, 4]
t, z = symbols("t z")


def basis(size, value):
    values = [1, value]
    for _ in range(2, size):
        values.append(value * values[-1] - values[-2])
    return values[:size]


def denominator(n, value):
    values = basis(n + 1, value)
    return values[-1] + values[-2]


def isolating_intervals(p):
    n = (p - 1) // 2
    intervals = []
    for j in range(1, n + 1):
        center = round(1024 * 2 * cos(2 * pi * j / p))
        left, right = [Fraction(center + delta, 1024) for delta in (-1, 1)]
        assert -2 < left < right < 2
        assert not intervals or right < intervals[-1][0]
        ls, rs = denominator(n, left), denominator(n, right)
        assert ls * rs <= 0
        if ls == 0:
            right = left
        elif rs == 0:
            left = right
        while right - left > Fraction(1, 1 << 90):
            middle = (left + right) / 2
            value = denominator(n, middle)
            if value == 0:
                left = right = middle
            elif value * ls < 0:
                right = middle
            else:
                left, ls = middle, value
        intervals.append((left, right))
    return intervals


def grid_rows(p):
    n = (p - 1) // 2
    rows = []
    for left, right in isolating_intervals(p):
        values = basis(n, (left + right) / 2)
        scaled = [round(ROW_SCALE * value) for value in values]
        error = [ceil(Fraction(1, 2) + ROW_SCALE * (right - left) / 2 * (i + 1) * i*i)
                 for i in range(n)]
        rows.append((scaled, error))
    return rows


def exact_signs(p, coefficients, rows):
    n = (p - 1) // 2
    polynomials = basis(n + 1, Poly(t, t))
    h = sum((a * e for a, e in zip(coefficients, polynomials)), Poly(0, t))
    b = polynomials[n] + polynomials[n - 1]
    if h.gcd(b).degree() > 0:
        return None
    signs = []
    for row, error in rows:
        midpoint = sum(m * a for m, a in zip(row, coefficients))
        radius = sum(e * abs(a) for e, a in zip(error, coefficients))
        if abs(midpoint) <= radius:
            raise ArithmeticError("Insufficient enclosure for a nonzero grid value")
        signs.append(1 if midpoint > 0 else -1)
    return signs


def integer_ranges(matrix, rhs, box):
    """Obtain outer integer bounds or certify that this projected system is empty."""
    import numpy as np
    from scipy.optimize import linprog

    floating = np.asarray(matrix, dtype=float) / ROW_SCALE
    target = np.asarray(rhs, dtype=float) / ROW_SCALE
    bounds = [(-limit, limit) for limit in box]
    size = len(box)

    def multipliers(result):
        return [max(0, int(round(-value * DUAL_SCALE)))
                for value in result.ineqlin.marginals]

    def combinations(weights):
        combined_rhs = sum(weight * v for weight, v in zip(weights, rhs))
        combined_row = [sum(weight * row[i] for weight, row in zip(weights, matrix))
                        for i in range(size)]
        return combined_rhs, combined_row

    def upper_bound(sign):
        objective = np.zeros(size)
        objective[0] = -sign
        result = linprog(objective, A_ub=floating, b_ub=target, bounds=bounds)
        if not result.success:
            return None
        total, row = combinations(multipliers(result))
        row[0] -= sign * DUAL_SCALE * ROW_SCALE
        total += sum(abs(v) * limit for v, limit in zip(row, box))
        return total // (DUAL_SCALE * ROW_SCALE)

    upper = upper_bound(1)
    if upper is None:
        result = linprog(np.r_[np.zeros(size), -1],
                         A_ub=np.c_[floating, np.ones(len(rhs))], b_ub=target,
                         bounds=bounds + [(None, None)])
        if result.success:
            total, row = combinations(multipliers(result))
            if total + sum(abs(v) * limit for v, limit in zip(row, box)) < 0:
                return range(0)
        upper = box[0]
    negative_lower = upper_bound(-1)
    if negative_lower is None:
        negative_lower = box[0]
    return range(max(-box[0], -negative_lower), min(box[0], upper) + 1)


def enumerate_cut(p, cut, rows, stats):
    n = (p - 1) // 2
    box = [(p*p*(i + 1) + 3) // 4 for i in range(n)]
    signs = [1] * cut + [-1] * (n - cut)
    matrix, rhs = [], []
    for (row, error), sign in zip(rows, signs):
        matrix.append([-sign * m for m in row])
        rhs.append(sum(limit * e for limit, e in zip(box, error)))
    matrix.append([-ROW_SCALE * (-1)**i for i in range(n)])
    rhs.append(ROW_SCALE)
    accepted = []

    def visit(coefficients, remaining_matrix, remaining_rhs, remaining_box):
        if not remaining_box:
            if min(remaining_rhs) >= 0:
                stats["outer_leaves"] += 1
                actual_signs = exact_signs(p, coefficients, rows)
                if actual_signs is None:
                    stats["grid_zero_leaves"] += 1
                elif actual_signs == signs:
                    assert 2 + sum((-1)**i * a for i, a in enumerate(coefficients)) >= 1
                    accepted.append({"cut": cut, "coefficients": coefficients})
            return
        children = integer_ranges(remaining_matrix, remaining_rhs, remaining_box)
        tails = [row[1:] for row in remaining_matrix]
        for value in children:
            reduced = [b - row[0] * value for b, row in zip(remaining_rhs, remaining_matrix)]
            visit(coefficients + [value], tails, reduced, remaining_box[1:])

    initial_rhs = [b - sum(a * v for a, v in zip(PREFIX, row)) for b, row in zip(rhs, matrix)]
    visit(PREFIX, [row[3:] for row in matrix], initial_rhs, box[3:])
    return accepted


def verify_witness():
    n, p = 18, 37
    assert exact_signs(p, WITNESS, grid_rows(p)) == [1]*17 + [-1]
    e = basis(n + 1, Poly(t, t))
    b = [Poly(1, t)] + [e[i] + e[i - 1] for i in range(1, n + 1)]
    q = Poly(t, t)*b[n] + sum((a*b[n-i-1] for i, a in enumerate(WITNESS)), Poly(0, t))
    assert q.eval(-2) / b[n].eval(-2) == -4
    remainder = q - Poly(t, t)*b[n]
    assert remainder.degree() == n-1 and remainder.LC() == 2
    lift = sum((Poly(a*z**(n+1-i)*(1+z*z)**i, z) for (i,), a in q.terms()), Poly(0, z))
    difference = Poly((1-z)*(1-z*z), z)*lift - Poly((1+z*z)**2, z)
    assert all(difference.nth(i) == 0 for i in range(6)) and difference.nth(6) == 1
    resultant = b[n].resultant(q)
    assert resultant == 5329
    # C881 v10 supplies exactly one exterior conjugate pair.
    x0, x1, y0, y1 = [Rational(a, 10**8) for a in
                       (-4292563, -4292562, 129163798, 129163799)]
    assert lift.count_roots(x0 + I*y0, x1 + I*y1) == 1
    lower, upper = x1*x1 + y0*y0, x0*x0 + y1*y1
    assert Rational("1.67017127") < lower <= upper < Rational("1.67017132")
    return {"p": p, "cut": 17, "coefficients": WITNESS, "endpoint_ratio": -4,
            "last_matching_index": 5, "lift_coefficients": [int(v) for v in lift.all_coeffs()],
            "resultant": int(resultant), "whole_measure_bounds": list(map(str, (lower, upper)))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--witness-only", action="store_true", help="verify p=37 without SciPy")
    args = parser.parse_args()
    result = {"witness": verify_witness()}
    name = "fixed_prefix_witness.json"
    if not args.witness_only:
        result["enumeration"] = {}
        for p in range(7, 38, 2):
            rows = grid_rows(p)
            stats = Counter(outer_leaves=0, grid_zero_leaves=0)
            successes = []
            for cut in range(1, (p-1)//2):
                successes.extend(enumerate_cut(p, cut, rows, stats))
            assert successes == ([{"cut": 17, "coefficients": WITNESS}] if p == 37 else [])
            result["enumeration"][p] = {**stats, "strict_completions": successes}
        name = "fixed_prefix_first_conductor.json"
    group = Path(__file__).resolve().parents[2]
    out = group.parents[1] / "outputs" / group.name / name
    out.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=out.parent,
                                         delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(result, stream, indent=2)
            stream.write("\n")
        temporary.replace(out)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    print(out)


if __name__ == "__main__":
    main()
