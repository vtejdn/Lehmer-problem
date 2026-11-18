"""Bound factor degrees by exact first-Frobenius orbits for 11 <= p <= 131."""

from collections import Counter, defaultdict
from math import gcd, isqrt

from flint import fmpz_poly, nmod_poly


TORSION_ORDERS = (1, 2, 3, 5, 8, 12, 18, 30)
MAX_DIFFERENCE = 2858


def prime_divisors(n):
    divisors = []
    for q in range(2, isqrt(n) + 1):
        if n % q == 0:
            divisors.append(q)
            while n % q == 0:
                n //= q
    if n > 1:
        divisors.append(n)
    return divisors


def key(poly, prime):
    """Use two coefficients for the lookup and compare full residues on a hit."""
    return int(poly[0]) + prime * int(poly[1])


def common_powers(short_base, long_base, short_cap, long_cap, modulus, prime):
    table = defaultdict(list)
    current = nmod_poly([1], prime)
    for i in range(1, short_cap + 1):
        current = current * short_base % modulus
        table[key(current, prime)].append((i, current))
    current = nmod_poly([1], prime)
    for j in range(1, long_cap + 1):
        current = current * long_base % modulus
        for i, other in table.get(key(current, prime), ()):
            if current == other:
                yield i, j


def residual_factors(prime):
    x = fmpz_poly([0, 1])
    g = x**3 - x - 1
    b = 1 - x**2 - x**3
    numerator = g(x**prime) * b**prime + (-g)**prime * b(x**prime)
    correction = numerator // prime
    assert correction * prime == numerator and correction[1] == 1
    def reduce(poly):
        return nmod_poly([int(c) % prime for c in poly], prime)

    t, g, b = map(reduce, (x, g, b))
    torsion = nmod_poly([1], prime)
    for order in TORSION_ORDERS:
        torsion *= reduce(fmpz_poly.cyclotomic(order))
    correction = reduce(correction)
    constant, factors = correction.factor()
    product = nmod_poly([int(constant)], prime)
    for factor, multiplicity in factors:
        degree = factor.degree()
        assert pow(t, prime**degree, factor) == t % factor
        for q in prime_divisors(degree):
            assert (pow(t, prime**(degree // q), factor) - t).gcd(factor) == 1
        product *= factor**multiplicity
    assert product == correction
    for factor, _ in factors:
        if not t % factor or not (g * b * torsion) % factor:
            continue
        one, inverse, _ = b.xgcd(factor)
        assert one == 1
        yield factor, t % factor, (-g * inverse) % factor


def eligible_degrees(prime):
    cap = 270 // prime
    degree_sum = Counter()
    for factor, t, v in residual_factors(prime):
        degree = factor.degree()
        for a, b in common_powers(v, t, cap, 3 * cap + MAX_DIFFERENCE, factor, prime):
            if abs(b - 3 * a) <= MAX_DIFFERENCE and gcd(a, b) == 1:
                degree_sum[a, b] += degree
        for b, a in common_powers(t, v, cap, (MAX_DIFFERENCE + cap) // 3, factor, prime):
            if a > cap and abs(b - 3 * a) <= MAX_DIFFERENCE and gcd(a, b) == 1:
                degree_sum[a, b] += degree
    return degree_sum


def main():
    if not __debug__:
        raise RuntimeError("Run without Python optimization to verify the certificates.")
    for p in range(11, 132, 2):
        if prime_divisors(p) != [p]:
            continue
        totals = eligible_degrees(p)
        largest = max(totals.values(), default=0)
        assert largest <= (0 if p <= 13 else 4)
        print(p, "directions with a residual orbit", len(totals),
              "largest residual degree sum", largest, flush=True)


if __name__ == "__main__":
    main()
