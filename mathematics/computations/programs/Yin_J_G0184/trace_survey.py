"""Search for good critical contacts on reciprocal trace sections."""
from functools import cache
from math import gcd

from sympy import Poly, ZZ, primerange, symbols

X = symbols("X")
x = Poly(X, X, domain=ZZ)
one = x.one
h = x**2 - 4
J = (h - 9)*(h - 16)
delta = 1 - 4*J
G = x*h*J*(2*h - 25)*delta


@cache
def chebyshev(n):
    if n == 0:
        return 2*one
    if n == 1:
        return x
    return x*chebyshev(n - 1) - chebyshev(n - 2)


def section(k, l):
    return (10*chebyshev(l) + chebyshev(2*k + l) + chebyshev(abs(2*k - l))
            - 7*chebyshev(k + l) + 7*chebyshev(abs(k - l)) + 1)


def exceptional(k, l):
    A = l*J - 7*k*x*(12-h)
    E = (delta*A**2 - k*k*x**2*h*(2*h-25)**2).exquo(J)
    return int(2*k*l*E.discriminant()*E.resultant(G))


def valuation(n, p):
    assert n
    b = 0
    while n % p == 0:
        n //= p
        b += 1
    return b


def evaluate(coefficients, z, modulus):
    value = 0
    for c in coefficients:
        value = (value*z + c) % modulus
    return value


def linear_contact(Q, p, residue, upper):
    q, q1, q2 = ([int(c) for c in poly.all_coeffs()] for poly in (Q, Q.diff(), Q.diff().diff()))
    z, modulus = residue, p
    second = evaluate(q2, z, p)
    assert second
    for b in range(1, upper + 1):
        next_modulus = modulus*p
        derivative = evaluate(q1, z, next_modulus)
        assert derivative % modulus == 0
        z -= modulus*((derivative//modulus)*pow(second, -1, p) % p)
        value = evaluate(q, z, next_modulus)
        assert value % modulus == 0
        unit = value//modulus % p
        if unit:
            symbol = pow((-2*unit*pow(second, -1, p)) % p, (p - 1)//2, p)
            return b, (-2*unit*pow(second, -1, p)) % p, symbol == 1
        modulus = next_modulus
    raise ArithmeticError("contact exceeds the discriminant valuation")


def main():
    primes = list(primerange(2, 50001))
    directions = 0
    for k in range(1, 17):
        for l in range(k + 1, 101):
            if gcd(k, l) != 1:
                continue
            Q, B = section(k, l), exceptional(k, l)
            disc = int(Q.discriminant())
            if not B or not disc:
                print('excluded', k, l, bool(B), bool(disc))
                continue
            directions += 1
            for p in primes:
                if disc % (p*p) or B % p == 0:
                    continue
                exponent = valuation(disc, p)
                poly = Q.set_modulus(p)
                repeated = poly.gcd(poly.diff())
                accounted = 0
                for factor, multiplicity in repeated.factor_list()[1]:
                    assert multiplicity == 1
                    f = factor.degree()
                    if f == 1:
                        z = -int(factor.TC()) % p
                        b, unit, square = linear_contact(Q, p, z, exponent)
                        accounted += b
                        if b % 2 == 0:
                            print('linear', k, l, p, z, b, unit, square)
                    else:
                        accounted += f
                assert accounted == exponent, (k, l, p, accounted, exponent)
    print('directions', directions, 'primes', len(primes))


if __name__ == '__main__':
    main()
