"""Attempt all 32 height-three variables with HiGHS; verify any hit exactly."""

import argparse
from fractions import Fraction

import highspy
import numpy as np

from trace64_cell import D, N, SEPARATORS, certificate, disk_rows, seed_vector, signed_rows
from trace64_cell import dot


def search(direction, seconds, nodes, seed, signs, disks):
    solver = highspy.Highs()
    solver.setOptionValue("output_flag", False)
    solver.setOptionValue("threads", 1)
    solver.setOptionValue("random_seed", 0)
    solver.setOptionValue("time_limit", seconds)
    solver.setOptionValue("mip_max_nodes", nodes)
    solver.setOptionValue("mip_feasibility_tolerance", 1.e-8)
    unknowns = solver.addVariables(N, lb=-3, ub=3, type=highspy.HighsVarType.kInteger)

    def expression(row, denominator):
        values = [float(Fraction(entry, denominator)) for entry in row]
        return solver.qsum(values[i] * unknowns[i] for i in range(N)) + values[N]

    for numerator, row in zip(SEPARATORS, signs):
        denominator = Fraction(numerator, 1000).denominator**N
        solver.addConstr(expression(row, denominator) >= float(Fraction(1, denominator)))

    # Omitting k>=2 gives an outer relaxation of each directional certificate.
    # Multiplication by 100 rescales the projected derivative at this small radius.
    axis = 0 if direction[-1] == "r" else 1
    sign = 1 if direction[0] == "+" else -1
    first = sign * expression(disks[1][axis], D**N) * 100
    residual = solver.addVariable(lb=-highspy.kHighsInf, obj=1)
    real = expression(disks[0][0], D**N) * 100
    imag = expression(disks[0][1], D**N) * 100
    for real_sign in (-1, 1):
        for imag_sign in (-1, 1):
            solver.addConstr(residual >= real_sign * real + imag_sign * imag - first)
    seed_full = seed + [1]
    seed_cost = (sum(abs(dot(row, seed_full)) for row in disks[0])
                 - sign * dot(disks[1][axis], seed_full))
    warm_start = seed + [float(Fraction(100 * seed_cost, D**N))]
    solver.setSolution(N+1, np.arange(N+1, dtype=np.int32), np.array(warm_start))
    solver.run()
    info = solver.getInfo()
    status = solver.modelStatusToString(solver.getModelStatus())
    print(f"{direction} status={status} nodes={info.mip_node_count} "
          f"incumbent={info.objective_function_value:.10g} dual={info.mip_dual_bound:.10g}")
    solution = solver.getSolution()
    if solution.value_valid:
        free = [int(round(v)) for v in solution.col_value[:N]]
        success, reason = certificate(free, signs, disks)
        print(f"exact={reason}, seed={free == seed}, vector={free}", flush=True)
        return success
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directions", nargs="+", default=["+i", "-r", "-i", "+r"])
    parser.add_argument("--seconds", type=float, default=60)
    parser.add_argument("--nodes", type=int, default=4096)
    args = parser.parse_args()
    if any(value not in ("+i", "-i", "+r", "-r") for value in args.directions):
        parser.error("Directions must be +r, -r, +i or -i.")
    signs, disks, seed = signed_rows(), disk_rows(), seed_vector()
    for direction in args.directions:
        search(direction, args.seconds, args.nodes, seed, signs, disks)
