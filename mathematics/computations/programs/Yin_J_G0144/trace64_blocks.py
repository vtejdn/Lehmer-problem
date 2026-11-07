"""Exact subbox exclusion using floating LP suggestions and integer dual checks."""

import argparse
from math import floor, isqrt, prod
from fractions import Fraction
from math import lcm

import highspy
import numpy as np

from trace64_cell import D, N, R, SEPARATORS, U, V, certificate, disk_rows, dot, seed_vector, signed_rows


def restrict(row, active, seed):
    constant = row[-1] + sum(row[j]*seed[j] for j in range(N) if j not in active)
    return [row[j] for j in active] + [constant]


def ceiling_sqrt(integer):
    root = isqrt(integer)
    return root + (root*root < integer)


def interlacing_rows(signs):
    """Apply the mass and first moment of B(t)=Q(t)/((t-w)(t-wbar))."""
    ys = [Fraction(k, 1000) for k in SEPARATORS]
    u, v, radius = Fraction(U,D), Fraction(V,D), Fraction(R,D)
    bounds = []
    for i,y in enumerate(ys):
        # The node residue p=Q(y)/H'(y) is positive by the alternating signs.
        denominator = y.denominator**N * abs(prod(y-z for j,z in enumerate(ys) if j != i))
        residue = [value/denominator for value in signs[i]]
        distance_squared = (y-u)**2 + v*v
        error = 2*radius*(abs(y-u)+v)
        lo, hi = distance_squared-error, distance_squared+error+radius**2
        assert lo > 0
        bounds.append(([p/hi for p in residue], [p/lo for p in residue]))

    def integer_row(entries):
        scale = lcm(*(Fraction(x).denominator for x in entries))
        return [int(x*scale) for x in entries]

    unit = [0]*N+[1]
    mass_lo = [sum(row[0][j] for row in bounds) for j in range(N+1)]
    mass_hi = [sum(row[1][j] for row in bounds) for j in range(N+1)]
    yield integer_row([a-b for a,b in zip(unit, mass_lo)])
    yield integer_row([a-b for a,b in zip(mass_hi, unit)])
    for kappa in (-2, u, -1, 0, 1, 2):
        lo, hi = [0]*(N+1), [0]*(N+1)
        for y, (lower, upper) in zip(ys, bounds):
            weight = y-kappa
            if weight < 0:
                lower, upper = upper, lower
            for j in range(N+1):
                lo[j] += weight*lower[j]
                hi[j] += weight*upper[j]
        target = [0]*(N+1)
        target[N-1] = 1
        target[N] = sum(ys) + 2*u-kappa
        lo_row = [a-b for a,b in zip(target, lo)]
        hi_row = [a-b for a,b in zip(hi, target)]
        lo_row[-1] += 2*radius
        hi_row[-1] += 2*radius
        yield integer_row(lo_row)
        yield integer_row(hi_row)


def outer_rows(active, seed, signs, disks, geometry):
    rows = [restrict(row, active, seed) for row in signs]
    shifted = [(restrict(real, active, seed), restrict(imag, active, seed))
               for real, imag in disks]
    # If a zero lies in the closed disk, |b0| <= sum_{k>=1} |bk|,
    # where bk is the coefficient of s^k after the affine substitution.
    tail = 0
    for real, imag in shifted[1:]:
        x = abs(real[-1]) + 3*sum(map(abs, real[:-1]))
        y = abs(imag[-1]) + 3*sum(map(abs, imag[:-1]))
        tail += ceiling_sqrt(x*x+y*y)
    if geometry:
        rows.extend(restrict(row, active, seed) for row in geometry)
        # |Q(c)| <= r (2 Im(c)+r) times the product of 30 endpoint bounds.
        distances = [(U-k*(D//1000))**2 + V*V for k in SEPARATORS]
        squared_product = prod(max(a,b) for a,b in zip(distances, distances[1:]))
        geometric_bound = ceiling_sqrt((R*(2*V+R))**2*squared_product)
        tail = min(tail, geometric_bound)
    real, imag = shifted[0]
    for a,b in ((1,0), (0,1), (1,1), (1,-1), (2,1), (2,-1), (1,2), (1,-2)):
        bound = ceiling_sqrt((a*a+b*b)*tail*tail)
        for sign in (-1,1):
            row = [sign*(a*x+b*y) for x,y in zip(real, imag)]
            row[-1] += bound
            rows.append(row)
    # Replace each exact row by a weaker small integer row valid on [-3,3]^m.
    # This outer rounding makes the subsequent ray verification inexpensive.
    scale = 1 << 23
    rounded_rows = []
    for row in rows:
        norm = max(map(abs, row))
        if not norm:
            continue
        rounded = [(2*x*scale+norm)//(2*norm) for x in row]
        errors = [abs(x*scale-y*norm) for x,y in zip(row, rounded)]
        allowance = 3*sum(errors[:-1]) + errors[-1]
        rounded[-1] += (allowance+norm-1)//norm
        rounded_rows.append(rounded)
    return np.array(rounded_rows, dtype=np.int64)


def enumerate_block(active, cap, signs, disks, seed, geometry):
    m = len(active)
    matrix = outer_rows(active, seed, signs, disks, geometry)
    # The following guard bounds every int64 product/sum in the exact dual test.
    max_integer = int(np.abs(matrix).max())
    weight_scale = 1 << 20
    assert max_integer*weight_scale*len(matrix)*(1+3*m) < 2**63
    solver = highspy.Highs()
    solver.setOptionValue("output_flag", False)
    solver.setOptionValue("threads", 1)
    solver.setOptionValue("solver", "simplex")
    solver.setOptionValue("presolve", "off")
    xs = solver.addVariables(m, lb=-3, ub=3)
    for row in matrix:
        terms = solver.qsum(float(row[i]/2**23)*xs[i] for i in range(m))
        solver.addConstr(terms >= float(-row[-1]/2**23))
    bounds_low = np.full(m, -3, dtype=np.int64)
    bounds_high = np.full(m, 3, dtype=np.int64)
    counts = dict(nodes=0, dual_nodes=0, dual_points=0, leaves=0, candidates=0,
                  disk_empty=0, undecided=0, failures=0, pending=0)
    hits = []

    def visit():
        widths = bounds_high-bounds_low
        volume = prod(int(x)+1 for x in widths)
        if counts["nodes"] >= cap:
            counts["pending"] += volume
            return
        counts["nodes"] += 1
        if volume == 1:
            full = seed.copy()
            for i,j in enumerate(active):
                full[j] = int(bounds_low[i])
            if np.all(matrix[:,:m] @ bounds_low + matrix[:,m] >= 0):
                counts["candidates"] += 1
                witness, reason = certificate(full, signs, disks)
                if witness:
                    hits.append(full)
                elif reason == "disk":
                    coeff = [(dot(real, full+[1]), dot(imag, full+[1]))
                             for real,imag in disks]
                    tail = sum(ceiling_sqrt(x*x+y*y) for x,y in coeff[1:])
                    x, y = coeff[0]
                    if x*x+y*y > tail*tail:
                        counts["disk_empty"] += 1
                    else:
                        counts["undecided"] += 1
            counts["leaves"] += 1
            return
        solver.run()
        status = solver.getModelStatus()
        if status == highspy.HighsModelStatus.kInfeasible:
            _, valid, ray = solver.getDualRay()
            if valid and max(ray) > 0:
                weights = np.rint(np.maximum(ray, 0) / max(ray) * weight_scale).astype(np.int64)
                combined = weights @ matrix
                maximum = combined[-1] + np.maximum(combined[:m]*bounds_low,
                                                    combined[:m]*bounds_high).sum()
                if maximum < 0:
                    counts["dual_nodes"] += 1
                    counts["dual_points"] += volume
                    return
            counts["failures"] += 1
        # The proposed branching order changes cost only: both sides are searched.
        index = int(widths.argmax())
        split = (int(bounds_low[index])+int(bounds_high[index]))//2
        if status == highspy.HighsModelStatus.kOptimal:
            solution = np.clip(solver.getSolution().col_value, bounds_low, bounds_high)
            distance = np.abs(solution-np.rint(solution))
            if max(distance) > 1.e-6:
                index = int(distance.argmax())
                split = floor(solution[index])
        left, right = int(bounds_low[index]), int(bounds_high[index])
        assert left <= split < right
        bounds_high[index] = split
        solver.changeColBounds(index, left, split)
        visit()
        bounds_low[index], bounds_high[index] = split+1, right
        solver.changeColBounds(index, split+1, right)
        visit()
        bounds_low[index] = left
        solver.changeColBounds(index, left, right)

    visit()
    assert counts["dual_points"] + counts["leaves"] + counts["pending"] == 7**m
    print(f"active={active} {counts} hits={hits}", flush=True)
    return counts, hits


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--width", type=int, default=16)
    parser.add_argument("--starts", type=int, nargs="+", default=[0,16])
    parser.add_argument("--cap", type=int, default=100000)
    parser.add_argument("--basic", action="store_true", help="Omit interlacing moment cuts.")
    args = parser.parse_args()
    signs, disks, seed = signed_rows(), disk_rows(), seed_vector()
    geometry = [] if args.basic else list(interlacing_rows(signs))
    for start in args.starts:
        if not 1 <= args.width <= N or not 0 <= start <= N-args.width:
            parser.error("Invalid Chebyshev coefficient block.")
        enumerate_block(list(range(start, start+args.width)), args.cap, signs, disks, seed, geometry)
