"""Certify the repeated trace factors for k=p^a and l=p^b +/- 1."""
from math import isqrt, lcm, prod

from sympy import Poly, resultant, symbols

x, z = symbols("x z")
A = Poly((x**2 - 3*x - 1)*(x**2 - 4*x - 1), x)
D = Poly(-4*x**8 + 116*x**6 - 799*x**4 + 116*x**2 - 4, x)
FACTORS = {2: 184, 3: 16, 5: 52, 7: 8, 17: 4, 23: 6, 79: 4,
           223: 4, 1193: 4, 1567: 4, 6644192153: 4}


def certify_resultant():
    reciprocal = Poly.from_list(A.all_coeffs()[::-1], x)
    assert D == Poly(x**4, x) - 4*A*reciprocal
    transformed = sum(c*x**(8-i)*z**i for (i,), c in D.terms())
    raw = Poly(resultant(D.as_expr(), transformed, x), z)
    content, groups = raw.sqf_list()
    assert content == 2**16
    H = prod(f for f, _ in groups)
    assert raw == content*prod(f**m for f, m in groups)
    assert H == raw.sqf_part() and H.degree() == 18 and H.LC() == 64
    numerator, denominator = Poly(-x**2, x), 2*A
    B = Poly(H.LC(), x)
    power = Poly(1, x)
    for coefficient in H.all_coeffs()[1:]:
        power *= denominator
        B = B*numerator + coefficient*power
    R = D.resultant(B)
    assert R == prod(p**e for p, e in FACTORS.items())
    for p in FACTORS:
        assert all(p % n for n in range(2, isqrt(p)+1))
    print('raw content, (degree, exponent, leading coefficient), sign of R:',
          content, [(f.degree(), m, f.LC()) for f, m in groups], R//abs(R))


def quotient_power(value, exponent, reduce):
    answer = value**0
    while exponent:
        if exponent % 2:
            answer = reduce(answer*value)
        value = reduce(value*value)
        exponent //= 2
    return answer


def collisions(p, modulus):
    def reduce(value):
        return value.rem(modulus)

    y = Poly(x, x, modulus=p).rem(modulus)
    orbit = [y]
    for _ in range(1, modulus.degree()):
        orbit.append(quotient_power(orbit[-1], p, reduce))
    assert quotient_power(orbit[-1], p, reduce) == y
    trace = Poly(resultant(modulus.as_expr(), x*z-x**2-1, x), z, modulus=p)
    factor = tuple(map(int, trace.sqf_part().monic().all_coeffs()))
    endpoint = (y*y-1).rem(modulus).is_zero
    leading = (2*A.set_modulus(p)).rem(modulus)
    hits = {}
    for a in range(len(orbit)):
        for b in range(len(orbit)):
            u, v = orbit[-a], orbit[(b-a) % len(orbit)]
            for sign, value in [(1, leading*v*u+y*y), (-1, leading*v+y*y*u)]:
                if value.rem(modulus).is_zero:
                    hits[a, b, sign] = (endpoint, factor)
    if hits and not endpoint:
        certify_lifts(p, modulus, hits)
    return hits


def certify_lifts(p, modulus, hits):
    f = Poly.from_list(modulus.all_coeffs(), x)

    def reduce(value):
        return value.rem(f).trunc(p*p)

    d = f.degree()
    order = p**d - 1
    y = quotient_power(Poly(x, x), p**d, reduce)
    assert quotient_power(y, order, reduce).is_one
    horizontal = reduce(A.compose(y))
    reciprocal = Poly.from_list(A.all_coeffs()[::-1], x)
    constant = reduce(reciprocal.compose(y))
    for a, b, sign in hits:
        exponent = p**((b-a) % d) + sign*p**((-a) % d)
        vertical = quotient_power(y, exponent % order, reduce)
        value = reduce(horizontal*vertical**2 + y**2*vertical + constant)
        assert value.trunc(p).is_zero and not value.is_zero, (p, f, a, b, sign)


def expected(p, a, b, sign):
    if p == 3:
        rows = ({(0, 1), (1, 0), (3, 3)}, {(1, 3), (2, 1), (3, 0)}) if sign == 1 else (
            {(1, 1), (2, 3), (3, 2)}, {(0, 3), (1, 2), (3, 1)})
        for middle, pairs in zip((1, -1), rows):
            if (a % 4, b % 4) in pairs:
                return {(1, middle, -1)}
    if p == 7:
        if b % 2 == (1 if sign == 1 else 0):
            return {(1, 3), (1, -3)}
        if sign == -1:
            return {(1, 0, -3)}
    if p == 79 and b % 2 == (0 if sign == 1 else 1):
        return {(1, sign * 28 * (-1)**(a % 2))}
    return set()


def certify_prime(p):
    factors = [f for f, _ in D.set_modulus(p).factor_list()[1]]
    tables = [(f.degree(), collisions(p, f)) for f in factors]
    period = lcm(4, *(degree for degree, _ in tables))
    for a in range(period):
        for b in range(period):
            for sign in (1, -1):
                hits = {table[a % d, b % d, sign] for d, table in tables
                        if (a % d, b % d, sign) in table}
                endpoints = {f for endpoint, f in hits if endpoint}
                assert endpoints == ({(1, 2), (1, -2)} if p == 5 else set())
                actual = {f for endpoint, f in hits if not endpoint}
                assert actual == expected(p, a, b, sign), (p, a, b, sign, actual)
    count = sum(not endpoint for _, table in tables for endpoint, _ in table.values())
    print(p, 'degrees', [d for d, _ in tables], 'nonendpoint lifts checked', count)


if __name__ == '__main__':
    certify_resultant()
    for prime in FACTORS:
        if prime != 2:
            certify_prime(prime)
