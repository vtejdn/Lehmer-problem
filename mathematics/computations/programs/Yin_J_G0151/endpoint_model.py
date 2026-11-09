"""One fixed endpoint-log occupancy test for the first N=7 residual triple.

The exploratory command makes one LP with 256 cells and a 15-second cap.
Its first occupancy is zero. A retained full/free pattern can be verified
separately by one 256-bit Arb linear solve over the entire inherited cut box.
"""

import argparse
from fractions import Fraction as F
import json
from math import comb, log
from pathlib import Path

from flint import arb, arb_mat, ctx, fmpq

from exterior19683 import evaluate
from negative_one_higher import chebyshev_polynomial, trace_differences
from negative_one_seven import relaxation_system


SIZE = 256
TRIPLE = (10, 18, 27)
ATOM = F(-15, 16)
CUT_LEFT = F(-1609663, 1000000)
CUT_RIGHT = F(-1609662, 1000000)


def ball(value):
    value = F(value)
    return arb(fmpq(value.numerator, value.denominator))


def polynomials():
    return [chebyshev_polynomial([F(0)]*(j-1)+[F(1)]) for j in range(1, 8)]


def data():
    old, controls = relaxation_system(TRIPLE, SIZE)
    return [row[SIZE+1:] for row in old[1:]], controls[1:]


def output_home():
    source = Path(__file__).resolve()
    output = source.parents[2] / "outputs" / source.parent.name
    output.mkdir(parents=True, exist_ok=True)
    return output


def save(name, record):
    (output_home() / name).write_text(json.dumps(record, indent=2) + "\n",
                                    encoding="utf-8")


def verify(native):
    assert native["triple"] == list(TRIPLE) and native["atom"] == [-15, 16]
    full, free = native["full"], native["free"]
    assert len(free) == len(set(free)) == 8 and len(full) == len(set(full))
    assert set(full).isdisjoint(free)
    assert all(type(i) is int and 1 <= i < SIZE for i in full+free)
    ctx.prec = 256
    matrix, _ = data()
    rows = [[ball(x) for x in row] for row in matrix]
    rows.append([arb(0)] + [ball(F(i+1, i)).log() for i in range(1, SIZE)])
    cut = ball(CUT_LEFT).union(ball(CUT_RIGHT))
    differences = trace_differences([3, 4, 7, *TRIPLE])
    rhs = []
    for polynomial in polynomials():
        trace = sum(a*d for a, d in zip(polynomial, differences))
        value = arb(0)
        for a in reversed(polynomial):
            value = value * cut + ball(a)
        rhs.append(ball(trace) + value - 2*ball(evaluate(polynomial, ATOM)))
    rhs.append(2*ball(2+ATOM).log() - (2+cut).log())
    square = arb_mat([[row[i] for i in free] for row in rows])
    remainder = arb_mat([[v-sum((row[i] for i in full), arb(0))]
                         for row, v in zip(rows, rhs)])
    determinant = square.det()
    assert determinant > 0 or determinant < 0
    solution = square.solve(remainder)
    values = [solution[i, 0] for i in range(8)]
    assert all(v > 0 and v < 1 for v in values)
    record = {
        "triple": list(TRIPLE), "atom": [-15, 16], "size": SIZE,
        "precision_bits": 256, "cut_interval": [str(CUT_LEFT), str(CUT_RIGHT)],
        "full": full, "free": free, "determinant_ball": str(determinant),
        "free_value_balls": [str(v) for v in values],
        "whole_cut_interval_verified": True,
        "endpoint_log_identity": True, "first_cell_occupancy": 0,
        "actual_interval_indicators_or_integrality_claimed": False,
    }
    save("endpoint_model_verification.json", record)
    print(json.dumps(record, indent=2))
    return record


def explore():
    import numpy as np
    from scipy.optimize import linprog
    matrix, controls = data()
    basis = polynomials()
    rhs = [sum(v*F(comb(7, j), 128) for j, v in enumerate(row))
           - 2*evaluate(polynomial, ATOM)
           for row, polynomial in zip(controls, basis)]
    rows = [list(map(float, row)) for row in matrix]
    rows.append([0.0] + [log((i+1)/i) for i in range(1, SIZE)])
    midpoint = (CUT_LEFT+CUT_RIGHT)/2
    target = list(map(float, rhs)) + [2*log(float(2+ATOM))-log(float(2+midpoint))]
    result = linprog(np.zeros(SIZE), A_eq=np.array(rows), b_eq=np.array(target),
                     bounds=[(0, 0)] + [(0, 1)]*(SIZE-1), method="highs",
                     options={"time_limit": 15.0})
    record = {
        "lp_calls": 1, "time_limit": 15.0, "status": int(result.status),
        "message": str(result.message), "success": bool(result.success),
        "triple": list(TRIPLE), "atom": [-15, 16], "size": SIZE,
        "solution": result.x.tolist() if result.x is not None else None,
        "exact_infeasibility_claimed": False,
    }
    save("endpoint_model_proposal.json", record)
    print("Endpoint LP", result.status, result.message, flush=True)
    if result.success:
        full = [i for i, v in enumerate(result.x) if v >= 1-1e-7]
        free = [i for i, v in enumerate(result.x) if 1e-7 < v < 1-1e-7]
        native = {"triple": list(TRIPLE), "atom": [-15, 16],
                  "full": full, "free": free}
        save("endpoint_model_pattern.json", native)
        print("Proposed pattern", native, flush=True)
        if len(free) == 8:
            verify(native)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("explore")
    fixed = commands.add_parser("verify")
    fixed.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "explore":
        explore()
    else:
        verify(json.loads(args.input.read_text(encoding="utf-8")))


if __name__ == "__main__":
    main()
