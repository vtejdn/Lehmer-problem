"""Degree-seven whole-measure tests for the eighteen N=7 moment triples.

The sampled LP mode only proposes integer polynomial coefficients. Final
certificates use rational trace differences and Bernstein enclosures.
"""

import argparse
from fractions import Fraction as F
import json
from math import comb

from exterior19683 import evaluate, separator_certificate
from negative_one_higher import (
    bernstein_bounds,
    chebyshev_polynomial,
    fifth_residue_moment_interval,
    fourth_residue_moment_interval,
    sampled_pairing_lp,
    third_residue_moment_interval,
    trace_differences,
)


# Each row gives (O,V,W), R, coefficients of T_1,...,T_7, and a strict
# integer lower bound for the rational separation margin.
CERTIFICATES = [
    ((10, 17, 25), F(26, 25), [15314, -36720, 21298, -5411, 1201, 11500, -8556], 43320),
    ((10, 17, 26), F(26, 25), [0, -29710, 20986, 0, 0, 26010, -23294], 147611),
    ((10, 18, 26), F(101, 100), [29758, -25680, 19735, -12851, 7585, -3203, 1188], 1125),
    ((10, 18, 28), F(26, 25), [0, -45036, 26448, 0, 7315, 6543, -14658], 65839),
    ((11, 19, 30), F(26, 25), [0, -15282, 10757, -4795, 0, 38237, 30928], 242102),
    ((11, 19, 31), F(26, 25), [-11460, -4342, 31154, 0, 0, 33406, 19637], 63475),
    ((11, 19, 32), F(26, 25), [23252, -28362, 21851, -6555, -6239, 9692, -4048], 16844),
    ((11, 20, 32), F(26, 25), [-6946, 0, 39625, -13878, 0, 10776, 28774], 83851),
    ((11, 20, 35), F(101, 100), [32512, -28224, 19621, -5385, -2892, 6428, -4937], 208),
    ((12, 22, 39), F(26, 25), [0, 0, 3728, 0, -11941, 20332, 64000], 399582),
    ((12, 22, 40), F(26, 25), [0, 0, 31714, -8155, -24787, 11895, 23449], 133229),
    ((12, 23, 42), F(26, 25), [0, 0, 37803, -13400, -24145, -1108, 23544], 112108),
    ((12, 23, 43), F(26, 25), [-47375, 0, 26188, -2254, -14467, -2269, 7447], 9696),
]

# Inclusive ranges of occupancy variables fixed at 1; all other nonfree
# variables are 0. Columns 0..256 are positive-measure masses, while column
# 257+i is occupancy on [-2+i/64,-2+(i+1)/64]. Every free basis has 8 columns.
RELAXATIONS = [
    ((10, 18, 27), [(66, 110), (160, 220), (254, 255)], [64, 68, 72, 257, 368, 413, 478, 510]),
    ((11, 20, 33), [(63, 64), (87, 158), (166, 166), (168, 168), (192, 196), (206, 223), (229, 235), (237, 239), (243, 243)], [4, 53, 79, 260, 343, 424, 448, 493]),
    ((11, 20, 34), [(0, 0), (5, 5), (63, 64), (82, 126), (129, 143), (145, 145), (155, 156), (166, 168), (179, 201), (207, 208), (215, 223), (229, 230), (232, 232), (238, 238), (243, 243), (250, 252)], [53, 79, 261, 338, 385, 435, 488, 506]),
    ((11, 21, 36), [(63, 64), (87, 89), (99, 147), (155, 156), (166, 168), (170, 196), (207, 208), (218, 218), (220, 223), (229, 229), (231, 231), (238, 238), (243, 243), (248, 252), (255, 255)], [37, 53, 79, 260, 405, 454, 487, 504]),
    ((11, 21, 37), [(2, 2), (63, 64), (79, 97), (99, 100), (110, 116), (124, 126), (129, 131), (134, 145), (155, 156), (159, 201), (207, 208), (218, 218), (247, 255)], [53, 79, 258, 355, 384, 459, 478, 500]),
]


def moment_triples():
    triples = []
    for third in third_residue_moment_interval(7)[2]:
        for fourth in fourth_residue_moment_interval(7, third)[2]:
            for fifth in fifth_residue_moment_interval(7, third, fourth)[3]:
                triples.append((third, fourth, fifth))
    assert len(triples) == 18
    return triples


def rational_certificate(triple, coefficients, measure, divisions=1024):
    polynomial = chebyshev_polynomial(list(map(F, coefficients)))
    derivative = [index * polynomial[index] for index in range(1, len(polynomial))]
    variation_upper = F(0)
    maximum_upper = max(evaluate(polynomial, F(-2)), evaluate(polynomial, F(2)))
    for index in range(divisions):
        left = F(-2) + F(4 * index, divisions)
        right = F(-2) + F(4 * (index + 1), divisions)
        minimum_derivative, maximum_derivative = bernstein_bounds(derivative, left, right)
        if maximum_derivative <= 0:
            variation_upper += evaluate(polynomial, left) - evaluate(polynomial, right)
            maximum_upper = max(maximum_upper, evaluate(polynomial, left))
        elif minimum_derivative >= 0:
            maximum_upper = max(maximum_upper, evaluate(polynomial, right))
        else:
            variation_upper += (right - left) * max(F(0), -minimum_derivative)
            maximum_upper = max(maximum_upper, bernstein_bounds(polynomial, left, right)[1])
    cut_minimum = bernstein_bounds(polynomial, F(-161, 100), F(-1006, 625))[0]
    differences = trace_differences([3, 4, 7, *triple])
    trace = sum(value * differences[index] for index, value in enumerate(polynomial))
    cost = sum(abs(value) * (measure**index + measure**-index - 2) for index, value in enumerate(coefficients, 1))
    return trace + cut_minimum - variation_upper - 2 * maximum_upper - cost


def explore():
    for triple in moment_triples():
        for measure in (F(26, 25), F(101, 100), F(1)):
            margin, coefficients = sampled_pairing_lp(
                7, triple[0], measure=float(measure), degree=7,
                fourth=triple[1], fifth=triple[2],
            )
            integers = [round(float(value) * 100000) for value in coefficients]
            print(json.dumps({"triple": triple, "measure": str(measure), "sampled_margin": float(margin), "coefficients": integers}), flush=True)
            if margin > 0:
                break


def solve_exact(matrix, rhs):
    """Unique full-column-rank rational solution, including redundant rows."""
    rows = [[F(value) for value in row] + [F(value)] for row, value in zip(matrix, rhs)]
    width = len(matrix[0])
    for column in range(width):
        pivot = next(index for index in range(column, len(rows)) if rows[index][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        scale = rows[column][column]
        rows[column] = [entry / scale for entry in rows[column]]
        for index, row in enumerate(rows):
            if index != column and row[column]:
                scale = row[column]
                rows[index] = [a - scale * b for a, b in zip(row, rows[column])]
    assert all(not any(row[:width]) and not row[-1] for row in rows[width:])
    solution = [rows[index][-1] for index in range(width)]
    assert all(sum(a * b for a, b in zip(row, solution)) == value for row, value in zip(matrix, rhs))
    return solution


def relaxation_system(triple, size):
    """Columns for a mass-2 positive measure and an interval occupancy in [0,1]."""
    grid = [F(-2) + F(4 * index, size) for index in range(size + 1)]
    basis = [[F(1)]] + [chebyshev_polynomial([F(0)] * (degree - 1) + [F(1)]) for degree in range(1, 8)]
    values = [[evaluate(polynomial, point) for point in grid] for polynomial in basis]
    matrix = [row + [row[index] - row[index + 1] for index in range(size)] for row in values]
    differences = trace_differences([3, 4, 7, *triple])
    traces = [sum(coefficient * differences[index] for index, coefficient in enumerate(polynomial)) for polynomial in basis]
    left, width = F(-1609663, 1000000), F(1, 1000000)
    controls = []
    for polynomial, trace in zip(basis, traces):
        shifted = [sum(polynomial[j] * comb(j, power) * left ** (j - power) * width**power for j in range(power, len(polynomial))) for power in range(8)]
        controls.append([trace + sum(shifted[power] * F(comb(index, power), comb(7, power)) for power in range(index + 1)) for index in range(8)])
    return matrix, controls


def verify_relaxation(triple, full_ranges, free):
    size = 256
    matrix, controls = relaxation_system(triple, size)
    full = [index for left, right in full_ranges for index in range(left, right + 1)]
    assert len(full) == len(set(full)) and len(free) == len(set(free)) == 8
    assert set(size + 1 + index for index in full).isdisjoint(free)
    assert all(0 <= index < size for index in full)
    assert all(0 <= index <= 2 * size for index in free)
    exact_matrix = [[row[index] for index in free] for row in matrix]
    for control in range(8):
        rhs = [row[control] - sum(matrix[index][size + 1 + interval] for interval in full) for index, row in enumerate(controls)]
        values = solve_exact(exact_matrix, rhs)
        assert all(value > F(1, 40) for value in values)
        assert all(value < F(19, 20) for index, value in zip(free, values) if index > size)


def explore_relaxations():
    """Propose bases, then certify each cut control vector using exact arithmetic."""
    import numpy as np
    from scipy.optimize import linprog
    residuals = [(10, 18, 27), (11, 20, 33), (11, 20, 34), (11, 21, 36), (11, 21, 37)]
    for triple in residuals:
        size = 256
        matrix, controls = relaxation_system(triple, size)
        rhs = [sum(row) / 8 for row in controls]
        result = linprog(np.zeros(2 * size + 1), A_eq=np.array(matrix, dtype=float), b_eq=np.array(rhs, dtype=float), bounds=[(0, None)] * (size + 1) + [(0, 1)] * size, method="highs")
        assert result.success, (triple, result.message)
        full = [index for index in range(size) if result.x[size + 1 + index] > 1 - 1e-7]
        free = [index for index, value in enumerate(result.x) if value > 1e-7 and (index <= size or value < 1 - 1e-7)]
        exact_matrix = [[row[index] for index in free] for row in matrix]
        minima = []
        maxima = []
        feasible = True
        for control in range(8):
            exact_rhs = [row[control] - sum(matrix[index][size + 1 + interval] for interval in full) for index, row in enumerate(controls)]
            values = solve_exact(exact_matrix, exact_rhs)
            minima.extend(values)
            maxima.extend(value for index, value in zip(free, values) if index > size)
            feasible &= all(value >= 0 and (index <= size or value <= 1) for index, value in zip(free, values))
        print(json.dumps({"triple":triple,"size":size,"full":full,"free":free,"certified":feasible,"min":float(min(minima)),"max_occupancy":float(max(maxima))}), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--explore", action="store_true")
    parser.add_argument("--relax", action="store_true")
    args = parser.parse_args()
    if args.explore:
        explore()
        return
    if args.relax:
        explore_relaxations()
        return
    assert separator_certificate(19683, 1990, F(-161, 100)) == 7851
    assert separator_certificate(19683, 1991, F(-1006, 625)) == 7850
    assert separator_certificate(19683, 1990, F(-1609663, 1000000)) == 7851
    assert separator_certificate(19683, 1991, F(-804831, 500000)) == 7850
    assert trace_differences([3, 4, 7, 10, 18, 27]) == [1, -2, -2, -2, -10, -2, -32, -9]
    necessary = set(moment_triples())
    certified = {triple for triple, _, _, _ in CERTIFICATES}
    relaxed = {triple for triple, _, _ in RELAXATIONS}
    assert len(certified) == 13 and len(relaxed) == 5
    assert not certified & relaxed and certified | relaxed == necessary
    for triple, measure, coefficients, lower_margin in CERTIFICATES:
        margin = rational_certificate(triple, coefficients, measure)
        assert margin > lower_margin > 0
        print("Strict full-Mahler certificate", triple, "M >", measure, "rational margin >", lower_margin)
    for triple, full_ranges, free in RELAXATIONS:
        verify_relaxation(triple, full_ranges, free)
        print("Exact degree-seven M=1 relaxed model", triple, "on the whole narrow cut bracket; all 8 Bernstein controls verified")
    print("Covered all 18 necessary triples: 13 strict full-Mahler bounds; 5 exact obstructions to this degree-seven separation interface.")


if __name__ == "__main__":
    main()
