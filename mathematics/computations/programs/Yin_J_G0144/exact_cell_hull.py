"""Generate or verify an integer separation tree for the degree-64 trace cell."""

import argparse
from collections import Counter, deque
import gzip
import json
from math import gcd
from pathlib import Path

from trace64_cell import D, N, R, SEPARATORS, U, V, chebyshev_basis, disk_rows, dot, signed_rows


HEIGHT = 3
SCALE = 2**36
DEFAULT_PROOF = Path(__file__).with_name("exact_cell_hull_proof.json.gz")


def enclosing_vertices():
    """Descending free Chebyshev coordinates, each scaled by a common denominator."""
    denominator = 1000**30 * D**2
    basis = chebyshev_basis()
    vertices = []
    for i in range(len(SEPARATORS)):
        # Ascending monomial coefficients of 1000^30 times S(x)/(x-s_i).
        poly = [1]
        for j, numerator in enumerate(SEPARATORS):
            if j != i:
                poly = [a - numerator*b for a, b in zip([0] + [1000*x for x in poly], poly + [0])]
        for linear in (-2*(U-R)*D, -2*(U+R)*D):
            for constant in ((abs(U)-R)**2 + (V-R)**2, (abs(U)+R)**2 + (V+R)**2):
                # All quadratic coefficients are scaled by D^2.
                monomials = [a+b+c for a, b, c in zip(
                    [0, 0] + [D**2*x for x in poly],
                    [0] + [linear*x for x in poly] + [0],
                    [constant*x for x in poly] + [0, 0])]
                descending = []
                for k in range(N, -1, -1):
                    leading = monomials[k]
                    descending.append(leading)
                    for j, value in enumerate(basis[k]):
                        monomials[j] -= leading*value
                if any(monomials) or descending[0] != denominator:
                    raise ArithmeticError("Invalid monic Chebyshev expansion")
                vertices.append(descending[1:])
    return vertices, denominator


def max_in_box(normal, prefix):
    return dot(normal, prefix) + HEIGHT*sum(abs(a) for a in normal[len(prefix):])


def homogeneous_cut(normal, prefix, vertices, denominator):
    """The hull and the prefix box must have intersecting normal projections."""
    return min(dot(normal, v) for v in vertices) > denominator*max_in_box(normal, prefix)


def upper_coordinate(normal, scale, sign, prefix, vertices, denominator):
    """Integer upper bound on sign*x_k from arbitrary integral dual coefficients."""
    k = len(prefix)
    # sign*scale*x_k <= normal.x + max_v(sign*scale*v_k - normal.v).
    residual = max(sign*scale*v[k] - dot(normal, v) for v in vertices)
    return (denominator*max_in_box(normal, prefix) + residual) // (denominator*scale)


def unpack(vector, length):
    if len(vector) != length or any(type(v) is not int for v in vector):
        raise ValueError("Invalid certificate vector")
    return vector


def verify_step(hint, prefix, vertices, denominator):
    if isinstance(hint, list) and len(hint) == 2 and hint[0] == "separate":
        if not homogeneous_cut(unpack(hint[1], N), prefix, vertices, denominator):
            raise ArithmeticError("Prefix separation failed")
        return range(0)
    if not isinstance(hint, list) or len(hint) != 3 or hint[0] != "bounds":
        raise ValueError("Invalid tree entry")
    limits = []
    for sign, vector in zip((-1, 1), hint[1:]):
        scale, *normal = unpack(vector, N+1)
        if scale <= 0:
            raise ValueError("Nonpositive scale")
        limits.append(upper_coordinate(normal, scale, sign, prefix, vertices, denominator))
    return range(max(-HEIGHT, -limits[0]), min(HEIGHT, limits[1])+1)


def disk_exclusion(descending, signs, disks):
    full = list(reversed(descending)) + [1]
    if not all(dot(row, full) > 0 for row in signs):
        return "real signs"
    values = [(dot(real, full), dot(imag, full)) for real, imag in disks]
    # On the whole closed disk the constant term dominates the entire tail.
    if max(map(abs, values[0])) > sum(abs(a)+abs(b) for a, b in values[1:]):
        return "empty disk"
    raise ArithmeticError(f"Physical root condition unresolved for {full[:-1]}")


class SuggestionSolver:
    """Only the generator uses floating-point linear programming."""

    def __init__(self, vertices, denominator):
        import highspy
        import numpy as np
        self.highspy = highspy
        self.np = np
        self.values = np.array([[x/denominator for x in vertex] for vertex in vertices])
        self.indices = np.arange(len(vertices), dtype=np.int32)
        self.solver = highspy.Highs()
        self.solver.setOptionValue("output_flag", False)
        self.solver.setOptionValue("threads", 1)
        self.solver.setOptionValue("presolve", "off")
        weights = self.solver.addVariables(len(vertices), lb=0, ub=1)
        self.solver.addConstr(sum(weights) == 1)
        self.rows = []
        for j in range(N):
            expr = self.solver.qsum(z * weights[i] for i, z in enumerate(self.values[:, j]))
            self.rows.append(self.solver.addConstr(expr <= HEIGHT))

    def suggest(self, prefix, vertices, denominator):
        for j, row in enumerate(self.rows):
            lo, hi = (prefix[j], prefix[j]) if j < len(prefix) else (-HEIGHT, HEIGHT)
            self.solver.changeRowBounds(row.index, lo, hi)
        normals = []
        for sign in (-1, 1):
            self.solver.changeColsCost(len(vertices), self.indices, sign*self.values[:, len(prefix)])
            self.solver.setMaximize()
            self.solver.run()
            if self.solver.getModelStatus() == self.highspy.HighsModelStatus.kInfeasible:
                _, exists, ray = self.solver.getDualRay()
                if exists:
                    proposed = [int(round(SCALE*v)) for v in ray[1:]]
                    g = gcd(*proposed) or 1
                    for orientation in (1, -1):
                        normal = [orientation*v//g for v in proposed]
                        if homogeneous_cut(normal, prefix, vertices, denominator):
                            return ["separate", normal]
                # Branching on the full integer range is always sound.
                normals.append([1] + [0]*N)
            elif self.solver.getModelStatus() == self.highspy.HighsModelStatus.kOptimal:
                proposed = [SCALE] + [int(round(SCALE*v)) for v in self.solver.getSolution().row_dual[1:]]
                g = gcd(*proposed)
                normals.append([v//g for v in proposed])
            else:
                self.solver.setBasis()
                normals.append([1] + [0]*N)
        return ["bounds", *normals]


def traverse(records=None, limit=50000):
    generate = records is None
    if generate:
        records = []
    vertices, denominator = enclosing_vertices()
    solver = SuggestionSolver(vertices, denominator) if generate else None
    signs, disks = signed_rows(), disk_rows()
    queue = deque([()])
    used = 0
    counts, reasons = Counter(), Counter()
    while queue:
        prefix = queue.popleft()
        counts[len(prefix)] += 1
        if len(prefix) == N:
            reason = disk_exclusion(prefix, signs, disks)
            reasons[reason] += 1
            print(f"leaf ({reason}), center first: {list(reversed(prefix))}", flush=True)
            continue
        if generate:
            if used >= limit:
                raise RuntimeError("Generator node budget exhausted")
            records.append(solver.suggest(prefix, vertices, denominator))
        if used >= len(records):
            raise ValueError("Certificate ends before the search tree")
        choices = verify_step(records[used], prefix, vertices, denominator)
        queue.extend(prefix + (v,) for v in choices)
        used += 1
    if used != len(records):
        raise ValueError("Trailing certificate entries")
    print(f"Verified {used} internal prefixes; counts by depth: {[counts[k] for k in range(N+1)]}")
    print(f"Initial domain {7**N}; surviving full inputs {counts[N]}; exclusions {dict(reasons)}")
    return records


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate", action="store_true")
    parser.add_argument("--proof", type=Path, default=DEFAULT_PROOF)
    args = parser.parse_args()
    if args.generate:
        proof = traverse()
        # Publish only the complete, already verified tree.
        encoded = json.dumps(proof, separators=(",", ":")).encode("ascii")
        args.proof.write_bytes(gzip.compress(encoded, compresslevel=9, mtime=0))
    else:
        proof = json.loads(gzip.decompress(args.proof.read_bytes()))
        traverse(proof)
