"""Test positive (59*q)-th field radicals at delays 55 through 58."""

import argparse
from functools import cache

import numpy as np
from sympy import Poly, isprime, n_order, primerange, symbols
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import gf_factor, gf_pow_mod


P = 59
X = symbols("X")
TEST_MODULI = (101, 103, 107, 109, 113)


def cofactor_roots(n, sign):
    return [root for root in (-1, 1) if root ** (n - 1) == sign]


@cache
def seed_polynomial(n, sign, seed):
    polynomial = Poly(X ** (n + 1) - seed * X**n + sign * (seed * X - 1), X)
    for root in cofactor_roots(n, sign):
        polynomial = polynomial.exquo(Poly(X - root, X))
    return polynomial


def initial_traces(coefficients, count, modulus=P):
    """Newton sums s_0,...,s_count of a monic polynomial modulo an integer."""
    d = len(coefficients) - 1
    traces = [d]
    for j in range(1, count + 1):
        cross = sum(coefficients[i] * traces[j - i] for i in range(1, j))
        traces.append((-j * coefficients[j] - cross) % modulus)
    return traces


class ResidueRing:
    def __init__(self, coefficients):
        d = len(coefficients) - 1
        relation = (-np.array(coefficients[:0:-1], dtype=np.int64)) % P
        # Row k represents X^k modulo the monic polynomial, in ascending coordinates.
        self.reductions = np.zeros((max(2, 2 * d - 1), d), dtype=np.int64)
        self.reductions[0, 0] = 1
        for k in range(1, len(self.reductions)):
            previous = self.reductions[k - 1]
            self.reductions[k] = previous[-1] * relation
            self.reductions[k, 1:] += previous[:-1]
            self.reductions[k] %= P
        self.one, self.x = self.reductions[:2]
        self.trace = np.array(initial_traces(coefficients, d - 1), dtype=np.int64)

    def multiply(self, left, right):
        product = np.convolve(left, right)
        return (product @ self.reductions[:len(product)]) % P

    def power(self, value, exponent):
        result = self.one
        while exponent:
            if exponent % 2:
                result = self.multiply(result, value)
            exponent //= 2
            if exponent:
                value = self.multiply(value, value)
        return result

    def power_traces(self, base, count):
        result = []
        value = self.one
        for _ in range(count):
            value = self.multiply(value, base)
            result.append(int(value @ self.trace) % P)
        return tuple(result)


@cache
def factor_ring(coefficients):
    return ResidueRing(coefficients)


@cache
def inverse_factor_traces(coefficients, count, q):
    """Traces of powers of the unique q-th root of X in one residue field."""
    ring = factor_ring(coefficients)
    exponent = pow(q, -1, P ** (len(coefficients) - 1) - 1)
    beta = ring.power(ring.x, exponent)
    assert np.array_equal(ring.power(beta, q), ring.x)
    return ring.power_traces(beta, count)


@cache
def factorization(coefficients):
    leading, factors = gf_factor(list(coefficients), P, ZZ)
    assert leading == 1
    return tuple((tuple(factor), multiplicity) for factor, multiplicity in factors)


def inverse_traces(polynomial, q):
    coefficients = tuple(int(c) % P for c in polynomial.all_coeffs())
    assert coefficients[-1] != 0
    count = polynomial.degree() // 2
    residues = [0] * count
    for factor, multiplicity in factorization(coefficients):
        component = inverse_factor_traces(factor, count, q)
        for j, value in enumerate(component):
            residues[j] = (residues[j] + multiplicity * value) % P
    return residues


def lift_polynomials(d, residues):
    bound = d + 7

    def extend(coefficients, traces):
        j = len(coefficients)
        if j > len(residues):
            yield Poly.from_list(coefficients + coefficients[-2::-1], X, domain=ZZ)
            return
        cross = sum(coefficients[i] * traces[j - i] for i in range(1, j))
        first = -bound + (residues[j - 1] + bound) % P
        for trace in range(first, bound + 1, P):
            quotient, remainder = divmod(-trace - cross, j)
            if remainder == 0:
                yield from extend(coefficients + [quotient], traces + [trace])

    yield from extend([1], [d])


def check_inverse(reduced, sums, q):
    """Power the whole reciprocal modular polynomial back to the target."""
    half = len(sums)
    first = [1]
    for j in range(1, half + 1):
        cross = sum(first[i] * sums[j - i - 1] for i in range(j))
        first.append((-cross * pow(j, -1, P)) % P)
    coefficients = first + first[-2::-1]
    ring = ResidueRing(coefficients)
    traces = ring.power_traces(ring.power(ring.x, q), half)
    target = initial_traces([int(c) % P for c in reduced.all_coeffs()], half)
    assert traces == tuple(target[1:])


def second_trace_matches(candidate, n, sign, q, modulus):
    """For the powered root multiset with the linear roots restored, s2=s1**2."""
    coefficients = [int(c) % modulus for c in candidate.all_coeffs()]
    d = candidate.degree()
    trace = initial_traces(coefficients, d - 1, modulus)
    linear = cofactor_roots(n, sign)
    sums = []
    for k in (1, 2):
        image = gf_pow_mod([1, 0], k * P * q, coefficients, modulus, ZZ)
        power_sum = sum(c * trace[i] for i, c in enumerate(reversed(image)))
        sums.append((power_sum + sum(root**k for root in linear)) % modulus)
    return (sums[1] - sums[0] ** 2) % modulus == 0


def main(q):
    if q <= P or not isprime(q) or n_order(P, q) <= 58:
        raise ValueError("The second prime must exceed 59 and ord_q(59) must exceed 58.")
    print(f"prime pair {P} {q}")
    print("delay sign degree classes full_lifts sign_pass irreducible survivors_by_modulus", flush=True)
    for n in range(55, 59):
        for sign in (-1, 1):
            d = n + 1 - len(cofactor_roots(n, sign))
            assert d % 2 == 0 and d < 60
            lifts = sign_pass = irreducible = 0
            survivors = [0] * len(TEST_MODULI)
            for residue in range(P):
                reduced = seed_polynomial(n, sign, residue)
                traces = inverse_traces(reduced, q)
                check_inverse(reduced, traces, q)
                for candidate in lift_polynomials(d, traces):
                    lifts += 1
                    if candidate.eval(1) >= 0 or candidate.eval(-1) <= 0:
                        continue
                    sign_pass += 1
                    if not candidate.is_irreducible:
                        continue
                    irreducible += 1
                    for i, modulus in enumerate(TEST_MODULI):
                        if not second_trace_matches(candidate, n, sign, q, modulus):
                            break
                        survivors[i] += 1
                    else:
                        print("unresolved", n, sign, residue, candidate.all_coeffs())
            print(n, sign, d, P, lifts, sign_pass, irreducible, *survivors, flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--second-prime", type=int, default=61)
    scope.add_argument("--through", type=int)
    arguments = parser.parse_args()
    if arguments.through is None:
        main(arguments.second_prime)
    else:
        for prime in primerange(P + 1, arguments.through + 1):
            if n_order(P, prime) > 58:
                main(prime)
