"""Circular-unit boxes for the negative block floor(p/log(p)) on the odd trace grid."""

from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path
import argparse
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Yin_J_G0144"))
from pilot import graeffe


def target_cut(p):
    with localcontext() as ctx:
        ctx.prec = 40
        log_p = Decimal(p).ln()
        k = int(Decimal(p) / log_p)
        # ln is correctly rounded. Use exact rationals for the floor check.
        assert k * Fraction(log_p.next_plus()) < p < (k + 1) * Fraction(log_p.next_minus())
    return k


def parity_solutions(p, k):
    """Return the rank, every generating sign/parity mask, and any obstruction."""
    n = p // 2
    target = sum(((i % 2) ^ (i >= n-k)) << i for i in range(n))
    columns = [(1 << n) - 1] + [
        sum((2*j*l // p % 2) << (l-1) for l in range(1, n+1)) for j in range(2, n+1)
    ]
    # Row reduction of the embedding equations, carrying their combinations.
    rows = []
    for i in range(n):
        coefficients = sum(((column >> i) & 1) << j for j, column in enumerate(columns))
        rows.append([coefficients, (target >> i) & 1, 1 << i])
    pivots = []
    for j in range(n):
        row = next((h for h in range(len(pivots), n) if rows[h][0] >> j & 1), None)
        if row is None:
            continue
        pos = len(pivots)
        rows[pos], rows[row] = rows[row], rows[pos]
        for h in range(n):
            if h != pos and rows[h][0] >> j & 1:
                rows[h] = [x ^ y for x, y in zip(rows[h], rows[pos])]
        pivots.append(j)
    for coeff, rhs, support in rows[len(pivots):]:
        assert coeff == 0
        if rhs:
            assert all((c & support).bit_count() % 2 == 0 for c in columns)
            assert (target & support).bit_count() % 2 == 1
            return len(pivots), [], support
    free = sorted(set(range(n)) - set(pivots))
    solutions = []
    for bits in range(1 << len(free)):
        mask = sum(((bits >> i) & 1) << j for i, j in enumerate(free))
        for (coeff, rhs, _), j in zip(rows, pivots):
            mask |= (rhs ^ ((mask & coeff).bit_count() % 2)) << j
        result = 0
        for i, column in enumerate(columns):
            if mask >> i & 1:
                result ^= column
        assert result == target
        solutions.append(mask)
    return len(pivots), solutions, None


def normalize(word):
    """Kill the coefficients in positions +/-n by subtracting a multiple of Phi_p."""
    offset = word[len(word)//2]
    return [c - offset for c in word]


def multiply_unit(word, j, sign):
    """Sliding cyclic convolution with u_j or u_j^-1 in Z[zeta]."""
    p = len(word)
    h, s = (j, 1) if sign == 1 else (pow(j, -1, p), j)
    start = (-s * (h-1)) % p
    step = (2*s) % p
    stop = (start + h*step) % p
    total = sum(word[(start+i*step) % p] for i in range(h))
    out = [0]*p
    slot = 0
    for _ in range(p):
        out[slot] = total
        total += word[stop] - word[start]
        start, stop, slot = (start+step) % p, (stop+step) % p, (slot+step) % p
    return normalize(out)


def unit_box(p, parity):
    indices = [j for j in range(2, p//2+1) if parity >> (j-1) & 1]
    one = [-1 if parity & 1 else 1] + [0]*(p-1)
    for j in indices:
        assert multiply_unit(multiply_unit(one, j, 1), j, -1) == one

    def generate(i, word, exponents):
        if i == len(indices):
            yield word, exponents
            return
        j = indices[i]
        for sign in (-1, 1):
            yield from generate(i+1, multiply_unit(word, j, sign), (*exponents, sign*j))

    return generate(0, one, ())


def numerators(unit):
    p = len(unit)
    yield 1, unit
    yield p, normalize([2*c-unit[(i-1)%p]-unit[(i+1)%p] for i, c in enumerate(unit)])


def lift(word, x):
    p, n, a = len(word), len(word)//2, 2*x
    assert word[n] == 0 and word[1:] == word[:0:-1]
    values = [1, 1-a] + [2-a]*(p-2) + [1-a, 1]
    for j in range(1-n, n):
        values[n+1+j] += word[j % p]
    assert values == values[::-1]
    return values


def bounds(p, radius):
    degree = p+1
    newton = [0] + [
        degree - 2 + int(radius**j + radius**(-j)) for j in range(1, degree//2+1)
    ]
    return newton, [comb(degree, j) for j in range(degree+1)]


def exceeds(poly, newton, binomials, radius):
    sums = [0]
    for k, limit in enumerate(newton[1:], 1):
        value = -k*poly[k] - sum(poly[j]*sums[k-j] for j in range(1, k))
        if abs(value) > limit:
            return True
        sums.append(value)
    values = poly
    for depth in range(13):
        threshold = radius**(1 << depth)
        u, v = threshold.numerator, threshold.denominator
        if any(abs(c)*v > b*u for c, b in zip(values, binomials)):
            return True
        if sum(c*c for c in values)*v*v < u*u:
            return False
        if depth < 12:
            values = graeffe(values)
    raise ArithmeticError(f"Undecided threshold {radius} for {poly}")


def paired_control():
    p, x = 43, 1
    n = p//2
    # u_2=b and u_n^{-1}=-b_n. Verify b*u=-b_n directly at all cyclic positions.
    parity, = parity_solutions(p, target_cut(p))[1]
    for unit, exponents in unit_box(p, parity):
        if exponents == (-2, -n):
            break
    else:
        raise ArithmeticError("Missing paired control")
    b_times_u = normalize([unit[(i-1)%p]+unit[(i+1)%p] for i in range(p)])
    assert b_times_u == [int(i not in (n, n+1)) for i in range(p)]
    windows = {1: (Fraction(146,100), Fraction(147,100)),
               p: (Fraction(240,100), Fraction(243,100))}
    for delta, word in numerators(unit):
        poly = lift(word, x)
        assert sum(poly[::2])-sum(poly[1::2]) == (3 if delta == 1 else 1)
        lo, hi = windows[delta]
        assert exceeds(poly, *bounds(p, lo), lo)
        assert not exceeds(poly, *bounds(p, hi), hi)


def census(p, unit_radius, nonunit_radius):
    if p < 5 or any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise ValueError("An odd prime >= 5 is required.")
    n, k = p//2, target_cut(p)
    rank, solutions, obstruction = parity_solutions(p, k)
    if not solutions:
        support = [l for l in range(1, n+1) if obstruction >> (l-1) & 1]
        return k, rank, support, {}
    radii = {1: unit_radius, p: nonunit_radius}
    tests = {delta: bounds(p, radius) for delta, radius in radii.items()}
    counts = {delta: Counter() for delta in (1, p)}
    for parity in solutions:
        for unit, exponents in unit_box(p, parity):
            for delta, word in numerators(unit):
                tally = counts[delta]
                tally['words'] += 1
                c_left = word[0] + 2*sum((-1)**j * word[j] for j in range(1, n))
                for x in range(-2, 3):
                    endpoint = 2 + 2*x - (-1)**n*c_left
                    if endpoint <= 0:
                        continue
                    poly = lift(word, x)
                    assert sum(poly[::2]) - sum(poly[1::2]) == endpoint
                    if delta == p:
                        assert sum(poly) % p == 0
                    tally['chamber'] += 1
                    if poly[2] == x*x - 2*x + 4:
                        tally['z2'] += 1
                        if poly[3] == x*x - 6*x + 4:
                            tally['z3'] += 1
                    if not exceeds(poly, *tests[delta], radii[delta]):
                        tally['below'] += 1
                        print('below', p, delta, x, exponents, endpoint, poly[:n+2])
    return k, rank, [], counts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int, default=[23,29,31,37,41,43,47,53,59,61,67])
    parser.add_argument("--unit-radius", type=Fraction, default=Fraction(29, 20))
    parser.add_argument("--nonunit-radius", type=Fraction, default=Fraction(12, 5))
    args = parser.parse_args()
    if min(args.unit_radius, args.nonunit_radius) <= 1:
        parser.error("each radius must be greater than one")
    paired_control()
    for p in args.primes:
        k, rank, obstruction, counts = census(p, args.unit_radius, args.nonunit_radius)
        print("p, k, rank, obstruction:", p, k, rank, obstruction)
        for delta, tally in counts.items():
            print("norm, words, chamber, z2, z3, below:", delta,
                  *(tally[key] for key in ('words', 'chamber', 'z2', 'z3', 'below')))
