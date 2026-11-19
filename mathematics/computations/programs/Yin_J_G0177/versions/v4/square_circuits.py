"""Exact cofactor certificates for five signed coefficients at a unit and its square."""

from functools import reduce
from itertools import combinations, permutations

from sympy import Poly, ZZ, symbols
from sympy.polys.rings import ring


RING, Z, X, C = ring("z,x,c", ZZ)
VARIABLE = symbols("z")
PRIME = 1009
TRACE = 3
ROOT = next(i for i in range(PRIME) if (i * i - TRACE * i + 1) % PRIME == 0)
PARAMETER = 7
TEST_POINT = 2


def cofactors(width, support, sign):
    rows = [[] for _ in range(4)]
    for j in support:
        for k in (1, 2):
            direct = Z ** (k * j)
            reverse = sign * C**k * Z ** (k * (width - j))
            rows[2 * k - 2].append(direct + reverse)
            rows[2 * k - 1].append(j * X * direct + ((width - j) * X + 1) * reverse)
    result = []
    for omitted in range(5):
        determinant = RING.zero
        for order in permutations(i for i in range(5) if i != omitted):
            inversions = sum(a > b for a, b in combinations(order, 2))
            term = (-1) ** (omitted + inversions)
            for row, column in enumerate(order):
                term *= rows[row][column]
            determinant += term
        result.append(determinant)
    return result


def specialize(polynomial):
    coefficients = {}
    for (degree, x_power, c_power), coefficient in polynomial.items():
        value = coefficient * pow(PARAMETER, x_power, PRIME) * pow(ROOT, c_power, PRIME)
        coefficients[degree] = (coefficients.get(degree, 0) + value) % PRIME
    return Poly.from_dict(coefficients, VARIABLE, modulus=PRIME)


def certify(width, support, sign):
    minors = cofactors(width, support, sign)
    low = min(degree for minor in minors for degree, _, _ in minor)
    high = max(degree for minor in minors for degree, _, _ in minor)
    divisor = Z**low * (Z - 1) ** 4
    reduced = [minor.exquo(divisor) for minor in minors]
    residues = [specialize(f) for f in reduced]
    spread = high - low - 4
    assert all(not f.is_zero for f in residues)
    assert max(f.degree() for f in residues) == spread
    assert reduce(lambda f, g: f.gcd(g), residues).is_one
    values = [int(f.eval(TEST_POINT)) for f in residues]
    node_tests = [sum(a * pow(TEST_POINT, k * j, PRIME) for a, j in zip(values, support)) % PRIME
                  for k in (1, 2)]
    assert all(node_tests)
    return low, high, spread, node_tests


def main():
    print(f"p={PRIME} c={ROOT} x={PARAMETER} z={TEST_POINT}")
    print("width support sign raw_min raw_max reduced_spread numerator_tests")
    for width in range(4, 13):
        if width <= 5:
            supports = combinations(range(width + 1), 5)
        else:
            supports = [(0, 1, 2, 3, width)]
        for support in supports:
            for sign in (-1, 1):
                print(width, support, sign, *certify(width, support, sign))


if __name__ == "__main__":
    main()
