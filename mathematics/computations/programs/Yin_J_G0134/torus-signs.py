"""Uncertified three-variable tests of all four-sine sign orbits.

The first scope is v=(e1,e2,e3,(a,b,c)), with nonzero coefficients
of absolute value at most 3.  Coordinate inversions and permutations reduce
to 1 <= a <= b <= c <= 3.  The (1,1,1) support is excluded because one
sign factors into three sine factors and already has Mahler measure one.
Two further rank-three templates are (3e1,3e2,3e3,(2,2,2)) and
(3e1,3e2,3e3,(2,3,3)).  The sole rank-two template has vectors
(1,0),(0,1),(1,1),(1,-1) and uses its exact one-variable Jensen formula.
No quadrature error or logarithmic clipping error is certified.
"""

import argparse
import itertools
import json
import math
from pathlib import Path
import sys


def orbit_representatives(coefficients, basis_scale=1):
    """Exact primitive-relation parity kernel, including global negation."""
    relation = (*coefficients, -basis_scale)
    divisor = math.gcd(*relation)
    relation = tuple(value // divisor for value in relation)
    subgroup = {
        h for h in itertools.product((0, 1), repeat=4)
        if sum(c * b for c, b in zip(relation, h)) % 2 == 0
    }
    subgroup |= {tuple(1 - value for value in flip) for flip in subgroup}
    unseen = set(itertools.product((0, 1), repeat=4))
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = sorted(tuple(x ^ y for x, y in zip(representative, flip))
                       for flip in subgroup)
        unseen.difference_update(orbit)
        orbits.append({
            "representative": [1 - 2 * bit for bit in representative],
            "all_signs": [[1 - 2 * bit for bit in member] for member in orbit],
        })
    assert len(orbits) == (1 if sum(relation) % 2 else 2)
    assert all(orbit["representative"][:3] == [1, 1, 1] for orbit in orbits)
    return orbits


def quadrature(coefficients, signs, points, shifts, floor, basis_scale=1):
    a, b, c = coefficients
    angular = 2 * math.pi / points
    sines = [[math.sin(basis_scale * angular * (j + shift)) for j in range(points)]
             for shift in shifts]
    offset = sum(x * shift for x, shift in zip(coefficients, shifts))
    fourth = [signs[3] * math.sin(angular * (j + offset))
              for j in range(points)]
    totals = []
    minimum = math.inf
    clipped = 0
    for i in range(points):
        for j in range(points):
            base = sines[0][i] + sines[1][j]
            index = (a * i + b * j) % points
            row_total = 0.0
            for k in range(points):
                absolute = abs(2 * (base + sines[2][k] + fourth[index]))
                minimum = min(minimum, absolute)
                if absolute < floor:
                    clipped += 1
                row_total += math.log(max(absolute, floor))
                index = (index + c) % points
            totals.append(row_total)
    return {
        "points_per_axis": points,
        "point_count": points ** 3,
        "mean_log_absolute": math.fsum(totals) / points ** 3,
        "minimum_sampled_absolute": minimum,
        "clipped_sample_count": clipped,
    }


def cross_jensen_quadrature(points, shift):
    """Exact x-Jensen integrand, then uncertified y quadrature.

    A=1+2 cos(y), B=sin(y).  The positive root expression below stays
    finite at A=0 and is >=3/5 everywhere, so no clipping is used.
    This does not certify numerical arithmetic or integration error.
    """
    values = []
    minimum_root = math.inf
    minimum_a = math.inf
    for j in range(points):
        y = 2 * math.pi * (j + shift) / points
        a = 1 + 2 * math.cos(y)
        b = math.sin(y)
        discriminant = b * b - a * a
        root = (abs(b) + math.sqrt(discriminant)
                if discriminant > 0 else abs(a))
        minimum_root = min(minimum_root, root)
        minimum_a = min(minimum_a, abs(a))
        values.append(math.log(root))
    return {
        "points": points,
        "shift": shift,
        "mean_log_absolute": math.fsum(values) / points,
        "minimum_sampled_root_expression": minimum_root,
        "minimum_sampled_absolute_A": minimum_a,
        "clipping_used": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--points", type=int, nargs="+", default=[48, 96])
    parser.add_argument("--shifts", type=float, nargs=3, default=[0.173, 0.371, 0.619])
    parser.add_argument("--floor", type=float, default=1e-300)
    parser.add_argument("--cross-points", type=int, nargs="+", default=[4096, 16384])
    parser.add_argument("--cross-shift", type=float, default=0.371)
    parser.add_argument("--output", type=Path, default=Path(
        "mathematics/computations/outputs/Yin_J_G0134/torus-signs.json"))
    args = parser.parse_args()
    if min(args.points + args.cross_points) < 2 or not 0 < args.floor < 1:
        parser.error("points must be >=2 and floor must lie strictly between 0 and 1")
    rows = []
    cases = [(1, coefficients) for coefficients in
             itertools.combinations_with_replacement(range(1, 4), 3)
             if coefficients != (1, 1, 1)]
    cases += [(3, (2, 2, 2)), (3, (2, 3, 3))]
    for basis_scale, coefficients in cases:
        orbits = orbit_representatives(coefficients, basis_scale)
        for orbit in orbits:
            orbit["quadratures"] = [
                quadrature(coefficients, orbit["representative"], points,
                           args.shifts, args.floor, basis_scale)
                for points in args.points
            ]
        rows.append({"basis_scale": basis_scale,
                     "coefficients": coefficients, "orbits": orbits})
    result = {
        "evidence": "Exploratory floating-point quadrature only; no certified integration or clipping error.",
        "python": sys.version,
        "scope": "Nine v=(e1,e2,e3,(a,b,c)) graph templates; two further templates with basis scale 3 and coefficients (2,2,2),(2,3,3); one rank-two cross template reduced by exact Jensen integration.",
        "shifts": args.shifts,
        "absolute_floor": args.floor,
        "log_two": math.log(2),
        "templates": rows,
        "rank_two_cross": {
            "vectors": [[1, 0], [0, 1], [1, 1], [1, -1]],
            "quadratures": [cross_jensen_quadrature(points, args.cross_shift)
                            for points in args.cross_points],
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        values = [orbit["quadratures"][-1]["mean_log_absolute"]
                  for orbit in row["orbits"]]
        print("scale", row["basis_scale"], row["coefficients"],
              "orbit means", values, "minimum", min(values))
    print("rank-two cross", result["rank_two_cross"]["quadratures"])
    print("Wrote", args.output)


if __name__ == "__main__":
    main()
