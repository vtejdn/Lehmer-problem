"""Exhaust the squarefree central-subtraction cases of degree at most 60."""

import json
from collections import Counter
from functools import cache
from math import gcd, lcm
from pathlib import Path


DEGREE = 60


def totients(bound):
    phi = list(range(bound + 1))
    for prime in range(2, bound + 1):
        if phi[prime] == prime:
            for multiple in range(prime, bound + 1, prime):
                phi[multiple] -= phi[multiple] // prime
    return phi


@cache
def cyclotomic(order):
    poly = [-1] + [0] * (order - 1) + [1]
    for factor in range(1, order):
        if order % factor:
            continue
        divisor = cyclotomic(factor)
        quotient = [0] * (len(poly) - len(divisor) + 1)
        for k in reversed(range(len(quotient))):
            quotient[k] = poly[k + len(divisor) - 1]
            for i, a in enumerate(divisor):
                poly[k + i] -= quotient[k] * a
        assert not any(poly)
        poly = quotient
    return tuple(poly)


def eligible_parents():
    factors = []
    for q, degree in enumerate(totients(2 * DEGREE**2)):
        if q >= 3 and degree <= DEGREE:
            poly = cyclotomic(q)
            assert len(poly) == degree + 1 and poly[0] == 1
            a, b, c = (poly + (0, 0, 0))[1:4]
            endpoint = sum(poly[::2]) - sum(poly[1::2])
            factors.append((degree, q, a, b, c, endpoint))
    factors.sort()

    def extend(start, degree, a, b, c, endpoint, orders):
        if (a, b, c) == (0, 3, 0):
            yield degree, tuple(sorted(orders)), endpoint
        for i in range(start, len(factors)):
            step, q, x, y, z, value = factors[i]
            if degree + step > DEGREE:
                break
            yield from extend(i + 1, degree + step, a + x, b + a*x + y,
                              c + b*x + a*y + z, endpoint * value, orders + (q,))

    yield from extend(0, 0, 0, 0, 0, 1, ())


@cache
def parent_phase(p, q):
    """Two masks for the sign changes and exact zeros of the q factor."""
    n = (p - 1) // 2
    full = (1 << n) - 1
    negative = zero = 0
    for a in range(1, (q + 1) // 2):
        if gcd(a, q) != 1:
            continue
        below, remainder = divmod(a*p, q)
        negative ^= full ^ ((1 << below) - 1)
        if remainder == 0:
            zero |= 1 << (below - 1)
    return negative, zero


@cache
def sine_phase(p, d):
    n = (p - 1) // 2
    negative = zero = odd = 0
    for j in range(1, n + 1):
        bit = 1 << (j - 1)
        quotient, remainder = divmod(2*(d-1)*j, p)
        if quotient % 2:
            negative |= bit
        if remainder == 0:
            zero |= bit
        if j % 2:
            odd |= bit
    return negative, zero, odd, ((1 << n) - 1) ^ odd


def phase_cuts(p, d, orders):
    n = (p - 1) // 2
    negative, zero, odd, even = sine_phase(p, d)
    for q in orders:
        signs, shared = parent_phase(p, q)
        negative ^= signs
        zero |= shared
    forced_negative = odd & (negative | zero)
    forced_positive = even & (~negative | zero)
    lower = max(1, forced_positive.bit_length())
    first_negative = (forced_negative & -forced_negative).bit_length()
    upper = min(n-1, first_negative-1) if forced_negative else n-1
    return lower, upper


def conductor_ceiling(d, orders):
    """Any larger p hits an odd nonpositive node before an even nonnegative one."""
    step = 2 * (d - 1)
    scale = lcm(step, *orders)
    toggles = set()
    for q in orders:
        factor_roots = {a * (scale // q) for a in range(1, (q + 1) // 2)
                        if gcd(a, q) == 1}
        toggles.symmetric_difference_update(factor_roots)
    toggles.symmetric_difference_update(k * (scale // step) for k in range(1, d - 1))
    positive = True
    start = largest_negative = separation = 0
    for end in sorted(toggles) + [scale // 2]:
        length = end - start
        if positive:
            separation = max(separation, min(largest_negative, length))
        else:
            largest_negative = max(largest_negative, length)
        positive = not positive
        start = end
    assert separation > 0
    return 2 * scale // separation


def main():
    counts = Counter()
    survivors = []
    largest_ceiling = 0
    by_degree = {}
    for degree, orders, endpoint in eligible_parents():
        counts["prefix_parents"] += 1
        row = by_degree.setdefault(degree, Counter())
        row["prefix_parents"] += 1
        d = degree // 2
        ceiling = conductor_ceiling(d, orders) if endpoint > 1 else 0
        largest_ceiling = max(largest_ceiling, ceiling)
        if endpoint > 1:
            counts["endpoint_parents"] += 1
        last_r = max(8*d, ceiling - 2*d + 2)
        for r in range(degree + 3, last_r + 1, 2):
            p = r + 2*d - 2
            n = (p - 1) // 2
            band = "initial" if r <= 8*d else "extension"
            counts[band + "_pairs"] += 1
            if n % 2 == 0 or endpoint <= 1 or orders[-1] > p:
                continue
            counts[band + "_phase_tests"] += 1
            row[band + "_phase_tests"] += 1
            low, high = phase_cuts(p, d, orders)
            if low <= high:
                survivors.append((orders, degree, r, p, low, high))
    counts["phase_survivors"] = len(survivors)
    output = Path(__file__).resolve().parent
    output = output.parents[1] / "outputs" / output.name / "central_parent_screen.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"maximum_parent_ceiling": largest_ceiling,
                                 "counts": counts, "by_degree": dict(sorted(by_degree.items())),
                                 "phase_survivors": survivors},
                                 indent=2) + "\n", encoding="utf-8")
    print(dict(counts), "largest conductor ceiling:", largest_ceiling)


if __name__ == "__main__":
    main()
