"""Exact single-position double-unit-atom models for five N=7 triples.

The default verifies fixed rational certificates with no numerical solver.
Optional --explore tests only s=-2+j/32, j=0,...,128, and stops at the first
sign-admissible exact model per triple, 645 LPs, or 60 seconds.
"""

import argparse
from fractions import Fraction as F
from math import comb
import json
from time import perf_counter

from exterior19683 import evaluate
from negative_one_higher import chebyshev_polynomial
from negative_one_seven import RELAXATIONS, relaxation_system, solve_exact
from two_atom_models import compress_ranges


SIZE = 256
POINTS = tuple(F(-2) + F(index, 32) for index in range(129))

# Triple, fixed grid index, inclusive fixed-one occupancy ranges, seven free
# occupancy columns. All unlisted coordinates are zero; both atom masses are 1.
MODELS = [
    ((10, 18, 27), 34, [(66, 109), (160, 220), (254, 255)], [0, 65, 110, 112, 159, 221, 253]),
    ((11, 20, 33), 33, [(25, 25), (27, 29), (88, 89), (99, 162), (166, 168), (207, 217), (219, 233), (236, 239)], [0, 23, 87, 163, 192, 218, 243]),
    ((11, 20, 34), 33, [(0, 1), (63, 64), (66, 66), (87, 89), (93, 104), (112, 149), (155, 155), (166, 168), (174, 181), (185, 195), (207, 208), (213, 218), (224, 230), (232, 232), (236, 239), (243, 243), (255, 255)], [2, 65, 92, 156, 199, 231, 254]),
    ((11, 21, 36), 30, [(17, 17), (24, 24), (114, 173), (177, 179), (184, 184), (189, 195), (207, 208), (225, 232), (236, 240), (243, 243), (253, 255)], [0, 37, 99, 113, 181, 218, 252]),
    ((11, 21, 37), 30, [(0, 0), (100, 100), (103, 106), (110, 127), (129, 140), (160, 203), (207, 208), (247, 255)], [1, 99, 128, 141, 155, 204, 246]),
]


def sign_admissible(point):
    """Z(t)=(t-point)^2 is strictly positive at -2 and every actual pole."""
    if point == -2:
        return False
    numerator, denominator = point.as_integer_ratio()
    previous, current = 1, numerator + denominator
    for _ in range(2, 9842):
        previous, current = current, numerator * current - denominator**2 * previous
    return current != 0


def exact_model(matrix, controls, atom_values, full, free):
    if len(free) != len(set(free)) or len(free) != 7:
        return None
    if len(full) != len(set(full)) or set(full) & set(free):
        return None
    assert all(0 <= index < SIZE for index in full + free)
    square = [[row[index] for index in free] for row in matrix]
    minimum, maximum = F(1), F(0)
    for control in range(8):
        rhs = [row[control] - 2 * atom_values[j] - sum(matrix[j][index] for index in full) for j, row in enumerate(controls)]
        try:
            values = solve_exact(square, rhs)
        except (StopIteration, AssertionError):
            return None
        if not all(0 <= value <= 1 for value in values):
            return None
        minimum, maximum = min(minimum, *values), max(maximum, *values)
    return {"full": compress_ranges(full), "free": free, "minimum": str(minimum), "maximum": str(maximum)}


def explore():
    import numpy as np
    from scipy.optimize import linprog
    start = perf_counter()
    attempts = 0
    basis = [chebyshev_polynomial([F(0)] * (degree - 1) + [F(1)]) for degree in range(1, 8)]
    atom_values = [[evaluate(polynomial, point) for polynomial in basis] for point in POINTS]
    exhausted = False
    for triple, _, _ in RELAXATIONS:
        old_matrix, old_controls = relaxation_system(triple, SIZE)
        matrix = [row[SIZE + 1:] for row in old_matrix[1:]]
        controls = old_controls[1:]
        cut_rhs = [sum(row[index] * F(comb(7, index), 128) for index in range(8)) for row in controls]
        numeric_matrix = np.array(matrix, dtype=float)
        statuses = {}
        tested = 0
        numerical_hits = []
        inadmissible_exact_hits = []
        certified = None
        for index, point in enumerate(POINTS):
            remaining = 60 - (perf_counter() - start)
            if attempts >= 645 or remaining <= 0:
                exhausted = True
                break
            rhs = [value - 2 * atom for value, atom in zip(cut_rhs, atom_values[index])]
            attempts += 1
            tested += 1
            result = linprog(np.zeros(SIZE), A_eq=numeric_matrix, b_eq=np.array(rhs, dtype=float), bounds=(0, 1), method="highs", options={"time_limit": max(0.001, remaining)})
            statuses[str(result.status)] = statuses.get(str(result.status), 0) + 1
            if not result.success:
                continue
            numerical_hits.append(index)
            full = [j for j, value in enumerate(result.x) if value > 1 - 1e-7]
            free = [j for j, value in enumerate(result.x) if 1e-7 < value < 1 - 1e-7]
            certificate = exact_model(matrix, controls, atom_values[index], full, free)
            if certificate is not None:
                if not sign_admissible(point):
                    inadmissible_exact_hits.append(index)
                    continue
                certified = {"grid_index": index, "atom": str(point), **certificate}
                break
        print(json.dumps({"triple": triple, "tested": tested, "last_index": tested - 1, "solver_status_counts": statuses, "numerical_hits": numerical_hits, "inadmissible_exact_hits": inadmissible_exact_hits, "exact_certificate": certified, "full_129_grid_tested": tested == 129}), flush=True)
        if exhausted:
            break
    print(json.dumps({"attempts": attempts, "seconds": perf_counter() - start, "budget_stop": exhausted, "scope": "only the prescribed 129 positions, five triples, and 256-cell occupancy relaxation; numerical failure is not proof of infeasibility"}), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--explore", action="store_true")
    args = parser.parse_args()
    if args.explore:
        explore()
        return
    assert len(MODELS) == len({row[0] for row in MODELS}) == 5
    assert {row[0] for row in MODELS} == {row[0] for row in RELAXATIONS}
    assert not sign_admissible(F(-2)) and not sign_admissible(F(-1))
    basis = [chebyshev_polynomial([F(0)] * (degree - 1) + [F(1)]) for degree in range(1, 8)]
    for triple, index, ranges, free in MODELS:
        point = POINTS[index]
        assert F(-2) < point < F(2) and sign_admissible(point)
        matrix, controls = relaxation_system(triple, SIZE)
        assert all(value == 2 for value in controls[0])
        occupancy = [row[SIZE + 1:] for row in matrix[1:]]
        atoms = [evaluate(polynomial, point) for polynomial in basis]
        full = [j for left, right in ranges for j in range(left, right + 1)]
        certificate = exact_model(occupancy, controls[1:], atoms, full, free)
        assert certificate is not None
        assert F(certificate["minimum"]) > F(1, 10)
        assert F(certificate["maximum"]) < F(999, 1000)
        print("Exact diagonal model", triple, "s =", point, "; B(s) != 0 and s != -2; all 8 controls: 1/10 < free occupancy < 999/1000")
    print("All five residual triples have sign-admissible double-unit-atom models on the entire inherited cut interval; no actual integer polynomial is constructed.")


if __name__ == "__main__":
    main()
