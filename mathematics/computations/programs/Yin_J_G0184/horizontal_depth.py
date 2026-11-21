"""Test horizontal collision depth by exact quotient-ring arithmetic."""

from argparse import ArgumentParser
from math import gcd

from flint import fmpz_mod_poly_ctx
from sympy import factorint, primerange


EXCLUDED = {2, 5, 23, 1039}


def quartic(ring, modulus):
    return ring([1, -29, 799 * pow(4, -1, modulus), -29, 1])


def deep_factors(p):
    modulus = p * p
    ring = fmpz_mod_poly_ctx(modulus)
    residue = fmpz_mod_poly_ctx(p)
    defect = ring.gen().pow_mod((p**4 - 1) // 2, quartic(ring, modulus)) - 1
    coefficients = [int(c) for c in defect.coeffs()]
    assert all(c % p == 0 for c in coefficients)
    digit = residue([c // p for c in coefficients])
    return digit.gcd(quartic(residue, p))


def scalar_lift(ring, value):
    return ring([int(c) for c in value.coeffs()])


def digit(ring, value, p, depth):
    coefficients = [int(c) for c in value.coeffs()]
    assert all(c % p**depth == 0 for c in coefficients)
    return ring([c // p**depth for c in coefficients])


def order(unit, factor, size):
    n = size - 1
    for prime in factorint(n):
        while n % prime == 0 and unit.pow_mod(n // prime, factor) == 1:
            n //= prime
    return n


def A(u):
    return (u*u - 3*u - 1) * (u*u - 4*u - 1)


def F(u, v):
    return A(u)*v*v + u*u*v + (1 - 3*u - u*u)*(1 - 4*u - u*u)


def inspect(p, factor):
    residue = fmpz_mod_poly_ctx(p)
    ring = fmpz_mod_poly_ctx(p**4)
    lift_factor = scalar_lift(ring, factor)
    size = p**factor.degree()
    u = residue.gen() % factor
    v = -u*u*(2*A(u)).inverse_mod(factor) % factor
    U = scalar_lift(ring, u).pow_mod(size**3, lift_factor)
    V = scalar_lift(ring, v).pow_mod(size**3, lift_factor)
    D = (-4*U**8 + 116*U**6 - 799*U**4 + 116*U**2 - 4) % lift_factor
    depth_digit = digit(residue, D, p, 2)
    assert depth_digit != 0
    C = digit(residue, F(U, V) % lift_factor, p, 2)
    J = A(u)*v*v % factor
    B = digit(residue, (2*A(U)*V*V + U*U*V) % lift_factor, p, 1)
    K = u*((4*u**3 - 21*u*u + 20*u + 7)*v*v + 2*u*v
           + 4*u**3 + 21*u*u + 20*u - 7) % factor
    print('orbit', factor, 'orders', order(u, factor, size), order(v, factor, size),
          'depth digit', depth_digit)
    if p == 17167:
        assert (4*J*C).pow_mod((p-1)//2, factor) == p-1
        if u != 1237:
            return
        for k, ell, expected in ((51501, 1541, 12064), (154503, 1762, 812)):
            assert gcd(k, ell) == 1 and u.pow_mod(ell, factor) == v.pow_mod(k, factor)
            linear = (ell*B + (k//p)*K) % factor
            quadratic = ell**2 * J % factor
            disc = (linear**2 - 4*quadratic*C) % factor
            assert disc == expected
            for y in (0, 1, -1):
                z = ring(1+p*y)
                value = F(U*z.pow_mod(k, lift_factor), V*z.pow_mod(ell, lift_factor)) % lift_factor
                assert digit(residue, value, p, 2) == (quadratic*y*y + linear*y + C) % factor
            print('direction', k, ell, 'quadratic', quadratic, linear, C, 'disc', disc,
                  'character', disc.pow_mod((p-1)//2, factor))
    if p == 8447:
        log_v = 8421 if factor[1] == 3850 else 4251
        assert u.pow_mod(log_v, factor) == v
        slopes = [t for t in range(p) if ((B+t*K)**2-4*J*C) % factor == 0]
        print('log', log_v, 'singular slopes', slopes)
        if factor[1] == 3850:
            k, ell = 523284765695, 27
            assert gcd(k, ell) == 1 and u.pow_mod(ell, factor) == v.pow_mod(k, factor)
            slope = (k//p)*pow(ell, -1, p) % p
            assert slope == 3713 and slope in slopes
            assert ((B+slope*K)*K) % factor != 0
            y = -(B+slope*K)*(2*ell*J).inverse_mod(factor) % factor
            z = 1+p*scalar_lift(ring, y)
            value = F(U*z.pow_mod(k, lift_factor), V*z.pow_mod(ell, lift_factor)) % lift_factor
            critical_digit = digit(residue, value, p, 3)
            assert critical_digit == residue([2299, 8013])
            print('direction', k, ell, 'double root', y, 'third digit', critical_digit)



def survey(limit):
    tested = 0
    for p in primerange(3, limit + 1):
        if p in EXCLUDED:
            continue
        tested += 1
        hit = deep_factors(p)
        if hit.degree() > 0:
            print(p, hit, flush=True)
            ring = fmpz_mod_poly_ctx(p)
            for factor, multiplicity in hit(ring.gen()**2).factor()[1]:
                assert multiplicity == 1
                if p in (8447, 17167):
                    inspect(p, factor)
                else:
                    print('Additional deep orbit:', factor)
    print('Eligible primes:', tested)


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--limit', type=int, default=1_000_000)
    survey(parser.parse_args().limit)
