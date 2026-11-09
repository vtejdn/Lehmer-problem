"""Exact equal-mass two-atom models for the fixed N=7 residual triples.

The optional proposal search fixes two distinct rational atoms first, then
solves only for occupancies. It is capped at 125 LPs and 60 seconds.
"""

import argparse
from fractions import Fraction as F
from math import comb, sqrt
import json
from time import perf_counter

from exterior19683 import evaluate, separator_certificate
from negative_one_higher import chebyshev_polynomial
from negative_one_seven import RELAXATIONS, relaxation_system, solve_exact


SIZE = 256
LEFT = F(-1609663, 1000000)
RIGHT = F(-804831, 500000)

# Each tuple fixes two distinct atom locations, each with mass exactly 1.
# Occupancy intervals are numbered 0..255; ranges below are inclusive.
# Listed ranges have occupancy 1, seven listed coordinates are free, and
# every other coordinate is 0. No atomic mass is a variable in these systems.
MODELS = [
    ((10, 18, 27), (F(-987, 1024), F(-3777, 4096)), [(66, 109), (160, 220), (254, 255)], [0, 65, 110, 112, 159, 221, 253]),
    ((11, 20, 33), (F(-4981, 4096), F(-1289, 2048)), [(0, 0), (88, 163), (166, 166), (208, 237)], [1, 12, 87, 164, 168, 207, 238]),
    ((11, 20, 34), (F(-4487, 4096), F(-91, 128)), [(0, 1), (66, 66), (75, 79), (87, 106), (108, 143), (155, 156), (166, 168), (177, 199), (207, 208), (218, 218), (221, 232), (236, 238), (254, 255)], [2, 37, 64, 107, 176, 220, 253]),
    ((11, 21, 36), (F(-2603, 2048), F(-1419, 2048)), [(64, 64), (87, 89), (99, 100), (102, 108), (110, 152), (155, 156), (165, 172), (181, 181), (183, 201), (207, 208), (218, 218), (223, 223), (227, 227), (230, 231), (238, 240), (243, 243), (252, 255)], [0, 24, 37, 109, 180, 229, 251]),
    ((11, 21, 37), (F(-2369, 2048), F(-3079, 4096)), [(2, 2), (66, 66), (75, 81), (84, 90), (96, 98), (100, 102), (112, 124), (126, 126), (130, 132), (135, 143), (155, 156), (159, 191), (193, 203), (207, 207), (243, 243), (247, 255)], [1, 65, 99, 129, 192, 208, 246]),
]


def equal_mass_seed(triple, ranges, free):
    """Match the old mass distribution's first two moments; proposal only."""
    matrix, controls = relaxation_system(triple, SIZE)
    full = [index for left, right in ranges for index in range(left, right + 1)]
    rhs = [sum(row[index] * F(comb(7, index), 128) for index in range(8)) - sum(matrix[j][SIZE + 1 + index] for index in full) for j, row in enumerate(controls)]
    values = solve_exact([[row[index] for index in free] for row in matrix], rhs)
    masses = [(F(-2) + F(index, 64), value) for index, value in zip(free, values) if index <= SIZE]
    assert sum(value for _, value in masses) == 2
    mean = sum(point * value for point, value in masses) / 2
    variance = sum(point**2 * value for point, value in masses) / 2 - mean**2
    assert variance > 0
    return tuple(F(round((float(mean) + sign * sqrt(float(variance))) * 4096), 4096) for sign in (-1, 1))


def occupancy_system(triple, atoms):
    """Seven nonconstant equations with both atomic masses fixed to exactly 1."""
    assert F(-2) < atoms[0] < atoms[1] < F(2)
    matrix, controls = relaxation_system(triple, SIZE)
    occupancies = [row[SIZE + 1:] for row in matrix[1:]]
    for degree in range(1, 8):
        polynomial = chebyshev_polynomial([F(0)] * (degree - 1) + [F(1)])
        atomic_value = sum(evaluate(polynomial, atom) for atom in atoms)
        controls[degree] = [value - atomic_value for value in controls[degree]]
    # The omitted constant equation is exactly 2 = 1 + 1; occupancy contributes 0.
    assert all(value == 2 for value in controls[0])
    return occupancies, controls[1:]


def verify_model(triple, atoms, full_ranges, free):
    matrix, controls = occupancy_system(triple, atoms)
    full = [index for left, right in full_ranges for index in range(left, right + 1)]
    assert len(full) == len(set(full))
    assert len(free) == len(set(free)) == 7
    assert set(full).isdisjoint(free)
    assert all(0 <= index < SIZE for index in full + free)
    square = [[row[index] for index in free] for row in matrix]
    minimum, maximum = F(1), F(0)
    for control in range(8):
        rhs = [row[control] - sum(matrix[j][index] for index in full) for j, row in enumerate(controls)]
        values = solve_exact(square, rhs)
        if not all(0 <= value <= 1 for value in values):
            return False, min(values), max(values)
        minimum, maximum = min(minimum, *values), max(maximum, *values)
    return True, minimum, maximum


def compress_ranges(indices):
    ranges = []
    for index in indices:
        if ranges and index == ranges[-1][1] + 1:
            ranges[-1][1] = index
        else:
            ranges.append([index, index])
    return ranges


def explore():
    import numpy as np
    from scipy.optimize import linprog
    start = perf_counter()
    attempts = 0
    offsets = sorted(((a, b) for a in range(-2, 3) for b in range(-2, 3)), key=lambda pair: (abs(pair[0]) + abs(pair[1]), pair))
    for triple, ranges, old_free in RELAXATIONS:
        seed = equal_mass_seed(triple, ranges, old_free)
        found = False
        for a, b in offsets:
            if attempts >= 125 or perf_counter() - start >= 60:
                print(json.dumps({"stop": "bounded search", "attempts": attempts, "seconds": perf_counter() - start}), flush=True)
                return
            atoms = (seed[0] + F(a, 128), seed[1] + F(b, 128))
            if not F(-2) < atoms[0] < atoms[1] < F(2):
                continue
            matrix, controls = occupancy_system(triple, atoms)
            rhs = [sum(row[index] * F(comb(7, index), 128) for index in range(8)) for row in controls]
            attempts += 1
            result = linprog(np.zeros(SIZE), A_eq=np.array(matrix, dtype=float), b_eq=np.array(rhs, dtype=float), bounds=(0, 1), method="highs", options={"time_limit": max(0.001, 60 - (perf_counter() - start))})
            if not result.success:
                continue
            full = [index for index, value in enumerate(result.x) if value > 1 - 1e-7]
            free = [index for index, value in enumerate(result.x) if 1e-7 < value < 1 - 1e-7]
            if len(free) != 7:
                continue
            exact, minimum, maximum = verify_model(triple, atoms, compress_ranges(full), free)
            if exact:
                print(json.dumps({"triple": triple, "atoms": [str(atom) for atom in atoms], "full": compress_ranges(full), "free": free, "exact": True, "min": float(minimum), "max": float(maximum), "attempts": attempts}), flush=True)
                found = True
                break
        if not found:
            print(json.dumps({"triple": triple, "finite_search_exhausted": True, "seed": [str(atom) for atom in seed], "attempts": attempts}), flush=True)
    print(json.dumps({"complete_bounded_search": True, "attempts": attempts, "seconds": perf_counter() - start}), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--explore", action="store_true")
    args = parser.parse_args()
    if args.explore:
        explore()
    else:
        assert separator_certificate(19683, 1990, LEFT) == 7851
        assert separator_certificate(19683, 1991, RIGHT) == 7850
        assert len(MODELS) == len({row[0] for row in MODELS}) == 5
        assert {row[0] for row in MODELS} == {row[0] for row in RELAXATIONS}
        for triple, atoms, ranges, free in MODELS:
            exact, minimum, maximum = verify_model(triple, atoms, ranges, free)
            assert exact and minimum > F(1, 1000) and maximum < F(999, 1000)
            print("Exact two-unit-atom model", triple, "atoms", tuple(map(str, atoms)), "all 8 controls: 1/1000 < free occupancy < 999/1000")
        print("All five residual triples verified on the entire cut bracket for every real polynomial of degree at most seven; no integer realization is asserted.")


if __name__ == "__main__":
    main()
