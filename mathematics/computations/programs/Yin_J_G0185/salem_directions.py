"""Test the remaining short exponents for Salem factors of degree at most 44."""

from fractions import Fraction
from math import gcd

from flint import fmpz_poly

from short_one import first_excluded_v
from witnesses import X


def search(q, u):
    p = q + 1
    stop = first_excluded_v(q)
    count = 0
    hits = []
    for v in range(u + 1, stop):
        if gcd(u, v) != 1:
            continue
        for sign in (-1, 1):
            parent = q * (1 + sign * X**(u + v)) - p * (X**u + sign * X**v)
            content, factors = parent.factor()
            product = fmpz_poly([content])
            for factor, multiplicity in factors:
                product *= factor**multiplicity
                if factor.degree() <= 44 and factor.leading_coefficient() == 1:
                    if abs(factor[0]) == 1 and not factor.is_cyclotomic():
                        hits.append((v, sign, factor, multiplicity))
            if product != parent:
                raise ArithmeticError(f"Factorization failed at {(q, u, v, sign)}")
            count += 1
    print(f"q={q}, u={u}, v<{stop}: {count} parents, hits={hits}", flush=True)
    return count, hits


def main():
    lower = Fraction(13, 10)
    u = 2
    total = 0
    while True:
        t = lower**u
        bound = 2*t/(t - 1)**2
        if bound <= 2:
            break
        for q in range(2, (bound.numerator - 1)//bound.denominator + 1):
            count, hits = search(q, u)
            total += count
            if hits:
                raise ArithmeticError(f"Candidate factors require inspection at {(q, u)}")
        u += 1
    print(f"Total signed parents: {total}")


if __name__ == "__main__":
    main()
