"""Verify the two-prime certificate for the quadratic diagonal at k = 361."""

from argparse import ArgumentParser
from itertools import combinations
from math import prod

from flint import ctx, nmod_poly

from modular_degrees import signed_divisors_mod, trace


K = 361
ELL = K**2 + 1
DEGREE = ELL + 2 * K
POINTS = (-2, -1)
DEGREES_3 = (1, 24, 298, 2975, 5327, 6874, 115545)
# Each row records degree, value at -2, and value at -1.
ROWS_19 = (
    (1, 10, 11),
    (3, 6, 14),
    (5, 18, 6),
    (8, 18, 17),
    (89, 4, 18),
    (625, 18, 10),
    (869, 7, 12),
    (1285, 18, 18),
    (1604, 7, 11),
    (4696, 11, 2),
    (10128, 5, 11),
    (10292, 18, 5),
    (13217, 7, 16),
    (25203, 8, 8),
    (27274, 5, 10),
    (35745, 12, 11),
)


def factor_rows(prime, points):
    x = nmod_poly([0, 1], prime)
    one = nmod_poly([1], prime)
    polynomial = trace(K, ELL, x, one)
    assert polynomial.degree() == DEGREE and polynomial.leading_coefficient() == 1
    leading, factors = polynomial.factor()
    assert leading == 1 and all(exponent == 1 for _, exponent in factors)
    assert prod((factor for factor, _ in factors), start=one) == polynomial
    return tuple(sorted((factor.degree(), *(int(factor(t)) for t in points))
                        for factor, _ in factors))


def proper_degrees(degrees):
    sums = {0}
    for degree in degrees:
        sums.update(value + degree for value in tuple(sums))
    return {value for value in sums if 0 < value <= DEGREE // 2}


def check():
    assert sum(DEGREES_3) == sum(row[0] for row in ROWS_19) == DEGREE
    candidates = proper_degrees(DEGREES_3)
    assert len(candidates) == 63
    values = [trace(K, ELL, point, 1) for point in POINTS]
    assert values == [25, -29]
    allowed = [signed_divisors_mod(value, 19) for value in values]
    rows = []
    for size in range(1, len(ROWS_19) + 1):
        for factors in combinations(ROWS_19, size):
            degree = sum(row[0] for row in factors)
            if degree in candidates:
                residues = [prod(row[i] for row in factors) % 19 for i in (1, 2)]
                rows.append((degree, *residues))
    first = [row for row in rows if row[1] in allowed[0]]
    both = [row for row in first if row[2] in allowed[1]]
    assert (len(rows), len(first), len(both)) == (9, 2, 0)
    for row in sorted(rows):
        print(*row)
    print("Modular divisors before and after integer evaluations:", len(rows), len(first), len(both))


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--refactor", action="store_true", help="recompute both finite-field factorizations")
    parser.add_argument("--threads", type=int, default=1, help="FLINT thread count for refactorization")
    args = parser.parse_args()
    if args.threads < 1:
        parser.error("--threads must be positive")
    if args.refactor:
        ctx.threads = args.threads
        assert factor_rows(19, POINTS) == ROWS_19
        assert factor_rows(3, ()) == tuple((degree,) for degree in DEGREES_3)
    check()
