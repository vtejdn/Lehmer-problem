"""Enumerate six-term trace lifts using exact Toeplitz and endpoint tests."""

import argparse
from collections import Counter
from itertools import combinations, product
from math import lcm


def exact_div(numerator, denominator):
    value, remainder = divmod(numerator, denominator)
    if remainder:
        raise ArithmeticError("Nonintegral scaled moment or predictor")
    return value


def trace_pair(h, d, e, a, b, coeff):
    """Construct C and B in the trace variable from the reciprocal prefix."""
    from sympy import Poly, QQ, symbols

    x = symbols("x")
    variable = Poly(x, x, domain=QQ)
    one = variable.one
    second = [one, variable]
    first = [2 * one, variable]
    for _ in range(2, h + 2):
        second.append(variable * second[-1] - second[-2])
        first.append(variable * first[-1] - first[-2])
    numerator = 2 * second[h] + a * second[h - d] + b * second[h - e]
    m = h + 1
    denominator = coeff[m] * one + sum(
        (coeff[m - k] * first[k] for k in range(1, m + 1)), 0 * one
    )
    return numerator, denominator


def check_residues(h, d, e, a, b, coeff, equality, q):
    """Check the signed Sturm index and construct a successful input."""
    from sympy import Poly, QQ, symbols

    numerator, denominator = trace_pair(h, d, e, a, b, coeff)
    m = h + 1
    chain = [numerator, (-denominator).rem(numerator)]
    while not chain[-1].is_zero:
        chain.append(-chain[-2].rem(chain[-1]))
    chain.pop()

    def variations(point):
        evaluated = (p.eval(point) for p in chain)
        values = [value for value in evaluated if value != 0]
        return sum(bool(left * right < 0) for left, right in zip(values, values[1:]))

    # Each simple interior pole contributes the sign of -B(y)/C'(y).
    if chain[-1].degree() != 0 or variations(-2) - variations(2) != h:
        return None
    z = symbols("z")
    lift_b = Poly.from_list(coeff[:m] + [coeff[m]] + coeff[:m][::-1], gens=z, domain=QQ)
    trace_c = Poly(0, z, domain=QQ)
    for offset, weight in [(0, 2), (d, a), (e, b)]:
        for index in range(offset, 2 * h - offset + 1, 2):
            trace_c += Poly(weight * z**index, z, domain=QQ)
    zz = Poly(z, z, domain=QQ)
    f = ((q - zz) * lift_b + zz * trace_c) * (1 if equality else 1 + zz)
    return f.exquo(1 - zz**2).as_expr()


def search_case(h, d, e, a, b, divisor, q, center_callback=None):
    m = h + 1
    terminal = 2 * h - 1
    degree = 2 * m
    second_endpoint = 2 * m + a * (-1)**d * (m - d) + b * (-1)**e * (m - e)
    tails = [(d, a), (e, b), (degree - e, -b), (degree - d, -a), (degree, -2)]
    scale = (1 << (terminal + 2)) * lcm(2 * (q - 1), 2 * (q + 1))
    plus = scale // (2 * (q - 1))
    minus = scale // (2 * (q + 1))
    mass = scale + plus - minus
    counts = Counter()
    witnesses = []

    def extend(n, previous, current, predictor, moments, j_coeff, coeff, equality):
        if n == m:
            counts["free"] += 1
            bp = coeff[m] + 2 * sum(coeff[:m])
            bm = coeff[m] + 2 * sum((-1)**(m - i) * v for i, v in enumerate(coeff[:m]))
            left = (-1)**h * (q + 1) * bm
            if bp != -divisor or left > -second_endpoint:
                return
            equality = left == -second_endpoint
            counts["endpoint"] += 1
            if center_callback is not None:
                center_callback(coeff)
        if n >= m:
            counts["deepest"] = max(counts["deepest"], n)
        if n == terminal:
            counts["terminal"] += 1
            f = check_residues(h, d, e, a, b, coeff, equality, q)
            if f is not None:
                witnesses.append(str(f))
            return

        k = n + 1
        prior_terms = sum(weight * j_coeff[k - i] for i, weight in tails if i <= k)
        constant_j = -exact_div(prior_terms, 2)
        constant_moment = exact_div(constant_j, 2) + plus - (-1)**k * minus
        predicted = sum(v * y for v, y in zip(predictor, reversed(moments[1:])))
        offset = previous * constant_moment - predicted
        step = previous * (scale // 2)
        lo = (-current - offset) // step + 1
        hi = (current - 1 - offset) // step
        if k > m:
            mirror = coeff[degree - k]
            lo = max(lo, mirror)
            hi = min(hi, mirror)
        for value in range(lo, hi + 1):
            cross = offset + step * value
            determinant = exact_div(current**2 - cross**2, previous)
            prediction = [
                exact_div(current * v - cross * w, previous)
                for v, w in zip(predictor, reversed(predictor))
            ] + [cross]
            next_moment = constant_moment + (scale // 2) * value
            extend(k, current, determinant, prediction, moments + [next_moment],
                   j_coeff + [constant_j + scale * value], coeff + [value], equality)

    extend(0, 1, mass, [], [mass], [scale], [1], None)
    counts["witnesses"] = len(witnesses)
    return counts, witnesses


def benchmark():
    from sympy import Rational

    candidates = []
    counts, witnesses = search_case(19, 1, 3, 1, 1, 1, 77, candidates.append)
    assert candidates == [[1] + [0] * 18 + [-1, -1]]
    assert counts["free"] == 320 and counts["deepest"] == 20 and not witnesses
    numerator, denominator = trace_pair(19, 1, 3, 1, 1, candidates[0])
    left, right = Rational(11, 10), Rational(23, 20)
    assert numerator.gcd(numerator.diff()).degree() == 0
    assert numerator.count_roots(left, right) == 1 and numerator(left) > 0 > numerator(right)
    assert denominator.count_roots(left, right) == 0 and denominator(left) < 0
    print("q=77 only center prefix:", candidates[0])
    print("One descending root of C and no root of the negative B in (11/10, 23/20).")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--first", type=int, default=2)
    parser.add_argument("--last", type=int, default=22)
    parser.add_argument("--q-min", type=int, default=77)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--benchmark", action="store_true", help="verify the explicit q=77 obstruction")
    args = parser.parse_args()
    if args.benchmark:
        benchmark()
        return
    if not 2 <= args.first <= args.last or args.q_min < 2:
        parser.error("require 2 <= first <= last and q-min >= 2")
    for h in range(args.first, args.last + 1):
        total = Counter()
        for d, e in combinations(range(1, h + 1), 2):
            for a, b in product((1, -1), repeat=2):
                endpoint = 2 * (h + 1) + a * (h + 1 - d) + b * (h + 1 - e)
                for divisor in range(1, endpoint // (args.q_min - 1) + 1):
                    if endpoint % divisor:
                        continue
                    q = 1 + endpoint // divisor
                    counts, witnesses = search_case(h, d, e, a, b, divisor, q)
                    total["cases"] += 1
                    for field in ["free", "endpoint", "terminal", "witnesses"]:
                        total[field] += counts[field]
                    total["deepest"] = max(total["deepest"], counts["deepest"])
                    if args.verbose or witnesses:
                        print(f"h={h} d={d} e={e} a={a} b={b} divisor={divisor} q={q}",
                              dict(counts), witnesses, flush=True)
        print(f"h={h} cases={total['cases']} free={total['free']} endpoint={total['endpoint']}"
              f" deepest={total['deepest']} terminal={total['terminal']}"
              f" witnesses={total['witnesses']}", flush=True)


if __name__ == "__main__":
    main()
