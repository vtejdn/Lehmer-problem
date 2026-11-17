"""Check the neutral full outputs from the two real fibers, using cyclotomic fields."""

from fractions import Fraction
from itertools import product
from math import gcd
from sympy import Poly, Symbol, cyclotomic_poly, sqrt, totient

X = Symbol("X")


def real_trace(n, degree):
    # Triangular recovery of S from Phi_n(Z) = Z^degree S(Z + Z^-1).
    coeffs = Poly(cyclotomic_poly(n, X), X).all_coeffs()[:degree+1]
    prev, curr = Poly(2, X), Poly(X, X)
    result = Poly(coeffs[-1], X)
    for j in range(1, degree + 1):
        result += coeffs[-1-j] * curr
        prev, curr = curr, Poly(X, X)*curr - prev
    return result


def field_blocks(conductor, max_degree):
    radical = sqrt(5 if conductor == 5 else 2)
    blocks = {}
    # phi(n) >= sqrt(n/2) and the reciprocal degree is at most 2*max_degree.
    for n in range(3, 2*(2*max_degree)**2 + 1):
        degree = int(totient(n))//2
        if degree > max_degree:
            continue
        trace = real_trace(n, degree)
        factors = Poly(trace.as_expr(), X, extension=radical).factor_list()[1]
        assert len(factors) == (2 if n % conductor == 0 else 1)
        if len(factors) == 1:
            continue
        positive = (1, 4) if conductor == 5 else (1, 7)
        blocks[n] = [
            (Fraction(a, n), a % conductor in positive)
            for a in range(1, (n+1)//2) if gcd(a, n) == 1
        ]
        assert len(blocks[n]) == degree
    return blocks


def neutral_outputs(conductor, max_degree):
    blocks = field_blocks(conductor, max_degree)
    orders = list(blocks)
    presentations = []

    def visit(start, selected, degree):
        if degree >= 4:
            # For each primitive block choose which conjugate fiber receives its first orbit.
            for flips in product((False, True), repeat=len(selected)):
                roots = sorted(
                    ((angle, positive ^ flip) for n, flip in zip(selected, flips)
                     for angle, positive in blocks[n]), reverse=True
                )
                if all(positive == bool(j % 2) for j, (_, positive) in enumerate(roots)):
                    presentations.append((selected, flips))
        for j in range(start, len(orders)):
            n = orders[j]
            next_degree = degree + len(blocks[n])
            if next_degree <= max_degree:
                visit(j + 1, selected + (n,), next_degree)

    visit(0, (), 0)
    return presentations


if __name__ == "__main__":
    for conductor, degree, expected in ((5, 16, [(15,), (30,)]), (8, 4, [(24,)])):
        found = neutral_outputs(conductor, degree)
        assert [blocks for blocks, _ in found] == expected
        print("source conductor", conductor, "full cyclotomic orders and conjugate choices", found)
