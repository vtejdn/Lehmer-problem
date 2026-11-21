"""Certify irreducibility of reciprocal sections by factoring traces over finite fields."""
from argparse import ArgumentParser
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from functools import cache
from math import isqrt, prod

from flint import nmod_poly


WEIGHTS = (1, 7, 10, -7, 1)
POINTS = (-2, -1, 0, 1, 2)
PRIMES = (19, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 41, 43)


def trace(k, ell, x, one):
    @cache
    def chebyshev(n):
        if n == 0:
            return 2 * one
        if n == 1:
            return x
        a = chebyshev(n // 2)
        if n % 2 == 0:
            return a * a - 2 * one
        return a * chebyshev(n // 2 + 1) - x

    return one + sum(weight * chebyshev(abs(ell + (j - 2) * k))
                     for j, weight in enumerate(WEIGHTS))


def signed_divisors_mod(value, p):
    n = abs(value)
    if not n:
        return set(range(p))
    return {s * d % p for i in range(1, isqrt(n) + 1) if n % i == 0
            for d in (i, n // i) for s in (-1, 1)}


def degree_bits(parts, cap):
    bits = 1
    mask = (1 << (cap + 1)) - 1
    for f, exponent in parts:
        for _ in range(exponent):
            bits |= (bits << f.degree()) & mask
    return bits


def evaluated_degrees(parts, possible, values, p):
    """Count monic modular divisors through successive necessary value tests."""
    allowed = [signed_divisors_mod(v, p) for v in values]
    factors = [(f.degree(), e, [int(f(a)) for a in POINTS]) for f, e in parts]
    counts = [0] * (1 + len(POINTS))
    degrees = 0
    cap = possible.bit_length() - 1

    def visit(index, degree, residues):
        nonlocal degrees
        if index == len(factors):
            if not ((possible >> degree) & 1):
                return
            counts[0] += 1
            for j, r in enumerate(residues):
                if r not in allowed[j]:
                    return
                counts[j + 1] += 1
            degrees |= 1 << degree
            return
        d, exponent, evaluations = factors[index]
        for power in range(exponent + 1):
            if degree > cap:
                break
            visit(index + 1, degree, residues)
            if power < exponent:
                degree += d
                residues = [a * b % p for a, b in zip(residues, evaluations)]

    visit(0, 0, [1] * len(POINTS))
    return degrees, counts


def certify(k, ell, verbose=False):
    degree = ell + 2 * k
    cap = degree // 2
    possible = (1 << (cap + 1)) - 2
    values = [trace(k, ell, a, 1) for a in POINTS]
    for index, p in enumerate(PRIMES, 1):
        q = trace(k, ell, nmod_poly([0, 1], p), nmod_poly([1], p))
        assert q.degree() == degree and int(q.leading_coefficient()) == 1
        _, parts = q.factor()
        possible &= degree_bits(parts, cap)
        counts = None
        if possible and prod(e + 1 for _, e in parts) <= 16384:
            possible, counts = evaluated_degrees(parts, possible, values, p)
        if verbose:
            print(k, ell, p, sorted((f.degree(), e) for f, e in parts), values, counts)
        if not possible:
            return index, ()
    return len(PRIMES), tuple(d for d in range(1, cap + 1) if (possible >> d) & 1)


def diagonal(k):
    count, unresolved = certify(k, k * k + 1)
    return k, count, unresolved


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--first', type=int, default=1)
    parser.add_argument('--last', type=int, default=128)
    parser.add_argument('--workers', type=int, default=1)
    parser.add_argument('--example', action='store_true')
    args = parser.parse_args()
    if args.example:
        print(certify(4, 53, verbose=True))
        return
    histogram = Counter()
    with ProcessPoolExecutor(args.workers) as pool:
        for k, count, unresolved in pool.map(diagonal, range(args.first, args.last + 1)):
            print(k, count, unresolved, flush=True)
            if not unresolved:
                histogram[count] += 1
    print('certificates by number of primes', sorted(histogram.items()))


if __name__ == '__main__':
    main()
