"""Necessary higher moments for the p=19683, x=-1, N=7 or 8 chambers.

The default run uses exact rational arithmetic.  --explore runs a sampled
linear-programming search; its output is exploratory, never a certificate.
The hypotheses are those of C882v3, including U=1 and the cut y=-161/100.
No extra agreement with an arcsine profile is assumed by the moment filters.
"""

from fractions import Fraction as F
import argparse
from math import comb

from conductor19683 import linear_layer_weights, minimum_weighted_sum
from exterior19683 import add, scale, evaluate, separator_certificate


def bernstein_bounds(polynomial, left, right):
    degree = len(polynomial) - 1
    shifted = [sum(polynomial[j] * comb(j, i) * left**(j-i) * (right-left)**i for j in range(i, degree+1)) for i in range(degree+1)]
    bernstein = [sum(shifted[j] * F(comb(i, j), comb(degree, j)) for j in range(i+1)) for i in range(degree+1)]
    return min(bernstein), max(bernstein)


def chebyshev_polynomial(coefficients):
    previous, current = [F(2)], [F(0), F(1)]
    polynomial = [F(0)]
    for index, coefficient in enumerate(coefficients, 1):
        if index > 1:
            previous, current = current, add([F(0), *current], scale(previous, -1))
        polynomial = add(polynomial, scale(current, coefficient))
    return polynomial


def pairing_certificate(second, third, fourth, coefficients, measure, divisions=1024):
    """Rigorous full-Mahler exclusion by rational Bernstein enclosures.

    If its returned margin is positive then M(P)>measure.  Root pairing
    gives sum Re f(v)>=D(f)+min_cut f-V_-(f).  The two exterior radii
    have product M(P), so their total Chebyshev radial error is at most
    sum |c_j| (M^j+M^-j-2), including real or nonreal exceptional roots.
    """
    polynomial = chebyshev_polynomial(list(map(F, coefficients)))
    derivative = [index * polynomial[index] for index in range(1, len(polynomial))]
    variation_upper = F(0)
    maximum_upper = max(evaluate(polynomial, F(-2)), evaluate(polynomial, F(2)))
    for index in range(divisions):
        left, right = F(-2) + F(4*index, divisions), F(-2) + F(4*(index+1), divisions)
        minimum_derivative, maximum_derivative = bernstein_bounds(derivative, left, right)
        if maximum_derivative <= 0:
            variation_upper += evaluate(polynomial, left) - evaluate(polynomial, right)
            maximum_upper = max(maximum_upper, evaluate(polynomial, left))
        elif minimum_derivative >= 0:
            maximum_upper = max(maximum_upper, evaluate(polynomial, right))
        else:
            variation_upper += (right-left) * max(F(0), -minimum_derivative)
            maximum_upper = max(maximum_upper, bernstein_bounds(polynomial, left, right)[1])
    cut_minimum = bernstein_bounds(polynomial, F(-161, 100), F(-1006, 625))[0]
    moments = [3, 4, second, third]
    if fourth is not None:
        moments.append(fourth)
    differences = trace_differences(moments)
    trace = sum(value * differences[index] for index, value in enumerate(polynomial))
    cost = sum(abs(value) * (measure**index + measure**-index - 2) for index, value in enumerate(coefficients, 1))
    return trace + cut_minimum - variation_upper - 2*maximum_upper - cost


def third_residue_moment_interval(second):
    """Strict support-localized 2 by 2 Hankel bounds for O=sum b^3 r."""
    s0, s1, s2 = F(261, 100), F(361, 100), F(second) - F(78, 100)
    offset = -F(39, 100) * second + F(156, 100)
    lower = (2 * s1 + s2) ** 2 / (2 * s0 + s1) - 2 * s2 - offset
    upper = 2 * s2 - (2 * s1 - s2) ** 2 / (2 * s0 - s1) - offset
    integers = tuple(value for value in range(lower.numerator // lower.denominator, upper.numerator // upper.denominator + 1) if lower < value < upper)
    return lower, upper, integers


def seventh_moment_weight():
    """Norm bound for (4-b^2)(100b+161)(b-1)^2(b-2)^2 h."""
    weights = linear_layer_weights()[27]
    weights[0] *= 4
    cost, valuations = minimum_weighted_sum(weights)
    return weights, F(cost, 1968300), valuations


def fourth_residue_moment_interval(second, third):
    """Hankel and (4-b^2) localized bounds for V=sum b^4 r."""
    s0, s1, s2 = F(261, 100), F(361, 100), F(second) - F(78, 100)
    s3 = F(third) - F(39, 100) * second + F(156, 100)
    offset = -F(39, 100) * third + F(78, 100) * second - F(312, 100)
    lower = (s2**3 - 2*s1*s2*s3 + s0*s3**2) / (s0*s2 - s1**2) - offset
    upper = 4*s2 - (4*s1-s3)**2 / (4*s0-s2) - offset
    integers = tuple(value for value in range(lower.numerator // lower.denominator, upper.numerator // upper.denominator + 1) if lower < value < upper)
    return lower, upper, integers


def fifth_residue_moment_interval(second, third, fourth):
    """(2+b) and (2-b) localized 3 by 3 strict bounds for W=sum b^5 r."""
    s0, s1, s2 = F(261, 100), F(361, 100), F(second)-F(78, 100)
    s3 = F(third)-F(39, 100)*second+F(156, 100)
    s4 = F(fourth)-F(39, 100)*third+F(78, 100)*second-F(312, 100)
    offset = -F(39, 100)*fourth+F(78, 100)*third-F(156, 100)*second+F(624, 100)
    def schur(sign):
        a,b,c = 2*s0+sign*s1,2*s1+sign*s2,2*s2+sign*s3
        d,e = 2*s2+sign*s3,2*s3+sign*s4
        return (c*d*d-2*b*d*e+a*e*e)/(a*c-b*b)
    lower, upper = schur(1)-2*s4-offset, 2*s4-schur(-1)-offset
    gamma = F(1781643, 1968300)
    norm_lower = gamma+F(439,100)*fourth-F(167,50)*third-F(893,100)*second+F(1049,25)
    integers = tuple(value for value in range(lower.numerator//lower.denominator,upper.numerator//upper.denominator+1) if lower<value<upper and value>=norm_lower)
    return lower, upper, norm_lower, integers


def trace_differences(residue_moments):
    """D_j=sum Q-root^j - sum B-root^j, for Q/B=t+2+sum r/(t-b)."""
    coefficients = [1, 2, *residue_moments]
    differences = [1]  # Q has exactly one more trace root than B.
    for index in range(1, len(coefficients)):
        differences.append(-index * coefficients[index] - sum(coefficients[j] * differences[index - j] for j in range(1, index)))
    return differences


def sampled_pairing_lp(second, third, measure=1.0, degree=5, fourth=None, fifth=None):
    """Explore Chebyshev variation separation; numerical grids are not proofs."""
    import numpy as np
    from numpy.polynomial import Chebyshev, Polynomial
    from scipy.optimize import linprog
    from scipy.sparse import csr_matrix, hstack, vstack, eye

    size = 1000
    grid = np.linspace(-2, 2, size + 1)
    midpoints = (grid[:-1] + grid[1:]) / 2
    basis = [2 * Chebyshev.basis(j, domain=[-2, 2]).convert(kind=Polynomial) for j in range(1, degree + 1)]
    values = np.array([poly(grid) for poly in basis]).T
    slopes = np.array([poly.deriv()(midpoints) for poly in basis]).T
    moments = [3, 4, second, third]
    if fourth is not None:
        moments.append(fourth)
    if fifth is not None:
        moments.append(fifth)
    differences = trace_differences(moments)
    traces = np.array([sum(poly.coef[j] * differences[j] for j in range(len(poly.coef))) for poly in basis])
    yvalues = np.array([poly(-1.61) for poly in basis])
    costs = np.array([measure**j + measure**-j - 2 for j in range(1, degree + 1)])
    # Variables c_plus, c_minus, negative derivative majorants, maximum.
    zeros = csr_matrix((size + 1, size))
    root_rows = hstack([csr_matrix(values), csr_matrix(-values), zeros, csr_matrix(-np.ones((size + 1, 1)))])
    variation_rows = hstack([csr_matrix(-slopes), csr_matrix(slopes), -eye(size), csr_matrix((size, 1))])
    norm_row = csr_matrix([[*np.ones(2 * degree), *np.zeros(size + 1)]])
    inequalities = vstack([root_rows, variation_rows, norm_row]).tocsr()
    rhs = np.r_[np.zeros(2 * size + 1), 1]
    objective = np.r_[-traces - yvalues + costs, traces + yvalues + costs, np.full(size, 4 / size), 2]
    result = linprog(objective, A_ub=inequalities, b_ub=rhs, bounds=[(0, None)] * (2 * degree + size) + [(None, None)], method="highs")
    assert result.success, result.message
    coefficients = result.x[:degree] - result.x[degree:2 * degree]
    return -result.fun, coefficients


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--explore", action="store_true")
    args = parser.parse_args()
    assert separator_certificate(19683, 1990, F(-161, 100)) == 7851
    assert separator_certificate(19683, 1991, F(-1006, 625)) == 7850
    for second, expected in ((7, (10, 11, 12)), (8, (11, 12, 13, 14, 15))):
        lower, upper, survivors = third_residue_moment_interval(second)
        assert survivors == expected
        print("N", second, "strict O interval", lower, upper, "integer survivors", survivors)
    weights, bound, valuations = seventh_moment_weight()
    assert weights == [6588, 355, 139, 114, 103, 102, 101, 101, 101]
    assert bound == F(1781643, 1968300)
    print("g=(t-1)(t-2) layer weights", weights, "bound", bound, "valuations", valuations)
    # For the arcsine x=-1 target sigma=(3,4,8,12,26,40),
    # integral (b-y)(b-1)^2(b-2)^2 r = -40-22y.
    assert -40 - 22 * F(-161, 100) == -F(229, 50)
    print("Cross-conductor target obstruction: y > -20/11 makes -40-22y negative")
    assert trace_differences([3, 4, 8, 12, 26, 40]) == [1, -2, -2, -2, -14, -2, -62, -2]
    expected_seven = {
        (10, 17): (25, 26), (10, 18): (26, 27, 28),
        (11, 19): (30, 31, 32), (11, 20): (32, 33, 34, 35),
        (11, 21): (36, 37), (12, 22): (39, 40),
        (12, 23): (42, 43), (12, 24): (),
    }
    for third in third_residue_moment_interval(7)[2]:
        for fourth in fourth_residue_moment_interval(7, third)[2]:
            survivors = fifth_residue_moment_interval(7, third, fourth)[3]
            assert survivors == expected_seven[(third, fourth)]
            print("N=7 necessary (O,V,W)", third, fourth, survivors)
    assert fourth_residue_moment_interval(8, 14) == (F(72698481, 2906050), F(241321, 8050), (26, 27, 28, 29))
    cases = [
        (11, None, [2383, -2971, 2189, -1400, 1057], 6544),
        (12, None, [2975, -2801, 2206, -1407, 612], 2562),
        (13, None, [3157, -2865, 2246, -1319, 413], 53),
        (14, 29, [673, -2441, 3300, -1307, -1292, 988], 386),
        (15, None, [0, 0, 2275, -3347, -4378], 11815),
    ]
    for third, fourth, coefficients, lower_margin in cases:
        margin = pairing_certificate(8, third, fourth, coefficients, F(23, 20))
        assert margin > lower_margin > 0
        print("N=8 full-Mahler certificate", third, fourth, "M>23/20; rational margin >", lower_margin)
    if args.explore:
        for second in (7, 8):
            for third in third_residue_moment_interval(second)[2]:
                for measure in (1.0, 1.05, 1.175, 1.380625):
                    margin, coefficients = sampled_pairing_lp(second, third, measure)
                    print("sampled LP", second, third, measure, "margin", margin, "T coefficients", coefficients)


if __name__ == "__main__":
    main()
