"""Fourth residue moment and whole Mahler cost for the x=2 profile.

The input is the p=19683 sign and norm class in conductor19683.py, with
K=6, L=-8 and N=14. All certificate calculations use exact arithmetic.
The final whole-measure conclusion additionally assumes the strict endpoint.
"""

from fractions import Fraction

from conductor19683 import (
    DEGREES,
    P,
    SEPARATOR,
    ceiling_root,
    minimum_weighted_sum,
    separator_certificate,
)
from exterior19683 import add, evaluate, remainder, scale


def linear_resultants(value):
    """Absolute norms of denominator*b - numerator on the nine layers."""
    numerator, denominator = value.numerator, value.denominator
    resultants = []
    for _ in DEGREES:
        resultants.append(abs(numerator + denominator))
        numerator, denominator = (
            numerator**3 - 3 * numerator * denominator**2,
            denominator**3,
        )
    return resultants


def trace_differences(fourth_moment):
    """Newton expansion of log(Q/(t*B)), including D(1)=1."""
    series = [1, -4, 6, -8, 14, fourth_moment]
    differences = [1]
    for degree in range(1, 6):
        value = -degree * series[degree]
        value -= sum(
            differences[index] * series[degree - index]
            for index in range(1, degree)
        )
        differences.append(value)
    return differences


def main():
    assert separator_certificate() == 7851
    y = SEPARATOR
    first, second, third = 6, -8, 14
    positive_mass = second - y * first
    positive_first_moment = third - y * second
    assert positive_mass == Fraction(83, 50)
    assert positive_first_moment == Fraction(28, 25)

    separator_resultants = linear_resultants(y)
    square_resultants = linear_resultants(Fraction(2, 3))
    weights = [
        ceiling_root(3 * first_norm * second_norm**2, degree)
        for degree, first_norm, second_norm in zip(
            DEGREES, separator_resultants, square_resultants
        )
    ]
    assert weights == [4575, 1216, 1010, 900, 916, 904, 904, 901, 900]
    minimum, valuation_vector = minimum_weighted_sum(weights)
    assert minimum == 14032098
    norm_bound = Fraction(minimum, P * 900)
    assert norm_bound == Fraction(779561, 984150)

    offset = -y * third - Fraction(4, 3) * positive_first_moment
    offset += Fraction(4, 9) * positive_mass
    assert offset == Fraction(9803, 450)
    assert -21 + offset == Fraction(353, 450) < norm_bound
    print("Normalized layer traces", weights)
    print("Minimum weighted trace", minimum, "at", valuation_vector)
    print("Fourth moment O satisfies O +", offset, ">=", norm_bound)
    print("Consequently the integral fourth moment satisfies O >= -20.")

    polynomial = list(map(Fraction, [-8, -12, 2, 7, 0, -1]))
    factorization = [Fraction(1)]
    for constant in [-2, -2, 1, 1, 2]:
        factorization = add([Fraction(0)] + factorization, scale(factorization, constant))
    assert scale(factorization, -1) == polynomial
    chebyshev = [
        [2],
        [0, 1],
        [-2, 0, 1],
        [0, -3, 0, 1],
        [2, 0, -4, 0, 1],
        [0, 5, 0, -5, 0, 1],
    ]
    expansion = [Fraction(-4)]
    for degree, coefficient in [(1, -1), (2, 2), (3, 2), (5, -1)]:
        expansion = add(expansion, scale(chebyshev[degree], coefficient))
    assert expansion == polynomial
    critical_quadratic = list(map(Fraction, [-6, 5, 5]))
    reduced = remainder(polynomial, critical_quadratic)
    assert reduced == [Fraction(-248, 25), Fraction(-116, 25)]
    # The two quadratic critical points have sum -1.
    negative_variation = -(2 * reduced[0] - reduced[1])
    assert negative_variation == Fraction(76, 5)
    assert evaluate(critical_quadratic, -2) > 0
    assert evaluate(critical_quadratic, -1) < 0
    assert evaluate(critical_quadratic, 0) < 0
    assert evaluate(critical_quadratic, 1) > 0
    assert evaluate(critical_quadratic, y) < 0
    assert y < -1

    at_lower_moment = trace_differences(-20)
    assert at_lower_moment == [1, 4, 4, 16, 16, 44]
    polynomial_difference = sum(
        coefficient * difference
        for coefficient, difference in zip(polynomial, at_lower_moment)
    )
    next_difference = sum(
        coefficient * difference
        for coefficient, difference in zip(polynomial, trace_differences(-19))
    )
    assert polynomial_difference == 20
    assert next_difference - polynomial_difference == 5
    gap = polynomial_difference - negative_variation + evaluate(polynomial, y)
    assert gap == Fraction(29087946801, 10000000000)

    # f=-T5+2*T3+2*T2-T1-4, and f is nonpositive on [-2,2].
    radius = Fraction(5, 4)
    exterior_cost = sum(
        coefficient * (radius**degree + radius**-degree - 2)
        for degree, coefficient in [(1, 1), (2, 2), (3, 2), (5, 1)]
    )
    assert exterior_cost == Fraction(8847001, 3200000)
    assert gap - exterior_cost == Fraction(360267169, 2500000000) > 0
    print("Pairing lower bound", gap)
    print("Whole exterior cost at M=5/4", exterior_cost)
    print("Strict margin", gap - exterior_cost)
    print("Every strict-endpoint input in this x=2 third-moment class has M(P)>5/4.")

    threshold = Fraction(-12, 7)
    assert -24 - 14 * threshold == 0
    print("At any odd conductor, a separator y>=-12/7 excludes O=-24 by positivity.")


if __name__ == "__main__":
    main()
