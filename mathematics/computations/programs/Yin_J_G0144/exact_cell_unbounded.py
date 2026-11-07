"""Verify the degree-64 trace cell over all integer coefficients, with no height cap."""

import argparse
from collections import Counter
import gzip
import json
from math import gcd, prod
from pathlib import Path
from time import monotonic

from exact_cell_hull import (N, SCALE, SuggestionSolver, disk_exclusion, disk_rows,
                             dot, enclosing_vertices, signed_rows, unpack)


DEFAULT_PROOF = Path(__file__).with_name("exact_cell_unbounded_proof.json.gz")


def natural_box(vertices, denominator):
    # A convex combination lies between the extrema; each coordinate is an integer.
    return [(-((-min(v[j] for v in vertices)) // denominator),
             max(v[j] for v in vertices) // denominator) for j in range(N)]


def box_maximum(h, prefix, box):
    return dot(h, prefix) + sum(max(z*lo, z*hi) for z, (lo, hi)
                                in zip(h[len(prefix):], box[len(prefix):]))


def separated(h, prefix, box, vertices, denominator):
    return min(dot(h, v) for v in vertices) > denominator*box_maximum(h, prefix, box)


def coordinate_bound(sign, h, scale, prefix, box, vertices, denominator):
    residual = max(sign*scale*v[len(prefix)] - dot(h, v) for v in vertices)
    return (denominator*box_maximum(h, prefix, box) + residual) // (denominator*scale)


def verify_step(entry, prefix, box, vertices, denominator):
    if isinstance(entry, list) and len(entry) == 2 and entry[0] == "x":
        if not separated(unpack(entry[1], N), prefix, box, vertices, denominator):
            raise ArithmeticError("Failed strict separation")
        return []
    if not isinstance(entry, list) or len(entry) != 3 or entry[0] != "b":
        raise ValueError("Invalid prefix bound")
    lo, hi = box[len(prefix)]
    for sign, vector in zip((-1, 1), entry[1:]):
        scale, *h = unpack(vector, N+1)
        if scale <= 0:
            raise ValueError("Nonpositive scale")
        bound = coordinate_bound(sign, h, scale, prefix, box, vertices, denominator)
        if sign == -1:
            lo = max(lo, -bound)
        else:
            hi = min(hi, bound)
    choices = list(range(lo, hi+1))
    if not prefix:  # Visit the two extremes first, then work inwards.
        choices.sort(key=lambda v: (min(v-lo, hi-v), v))
    return choices


class NaturalSolver(SuggestionSolver):
    def hint(self, prefix, box, vertices, denominator):
        # Replace every LP row bound before solving, including all unset coordinates.
        for j, row in enumerate(self.rows):
            lo, hi = (prefix[j], prefix[j]) if j < len(prefix) else box[j]
            self.solver.changeRowBounds(row.index, lo, hi)
        entry = ["b"]
        for sign in (-1, 1):
            self.solver.changeColsCost(len(vertices), self.indices, sign*self.values[:, len(prefix)])
            self.solver.setMaximize()
            self.solver.run()
            status = self.solver.getModelStatus()
            if status == self.highspy.HighsModelStatus.kOptimal:
                vector = [SCALE] + [int(round(SCALE*z)) for z in self.solver.getSolution().row_dual[1:]]
                divisor = gcd(*vector)
                entry.append([v//divisor for v in vector])
                continue
            if status == self.highspy.HighsModelStatus.kInfeasible:
                _, exists, ray = self.solver.getDualRay()
                if exists:
                    vector = [int(round(SCALE*z)) for z in ray[1:]]
                    divisor = gcd(*vector) or 1
                    for orientation in (-1, 1):
                        h = [orientation*v//divisor for v in vector]
                        if separated(h, prefix, box, vertices, denominator):
                            return ["x", h]
            self.solver.setBasis()
            entry.append([1] + [0]*N)
        return entry


def traverse(records=None):
    generate = records is None
    if generate:
        records = []
    vertices, denominator = enclosing_vertices()
    box = natural_box(vertices, denominator)
    signs, disks = signed_rows(), disk_rows()
    solver = NaturalSolver(vertices, denominator) if generate else None
    start = monotonic()
    work = [()]
    used = 0
    counts = Counter()
    exclusions = Counter()
    while work:
        prefix = work.pop()
        counts[len(prefix)] += 1
        if len(prefix) == N:
            reason = disk_exclusion(prefix, signs, disks)
            exclusions[reason] += 1
            # This also checks nodes on a separator, where a strict real sign failed.
            full = list(reversed(prefix)) + [1]
            jet = [(dot(a, full), dot(b, full)) for a, b in disks]
            constant = max(map(abs, jet[0]))
            tail = sum(abs(a)+abs(b) for a, b in jet[1:])
            if constant <= tail:
                raise ArithmeticError("Closed disk not excluded under weak signs")
            print(f"leaf ({reason}), closed disk empty, constant/tail > {(constant-1)//tail}; "
                  f"center first: {full[:-1]}")
            continue
        if generate:
            if used >= 8000 or monotonic() - start > 115:
                raise RuntimeError("Natural-box generator budget exhausted")
            records.append(solver.hint(prefix, box, vertices, denominator))
        if used >= len(records):
            raise ValueError("Incomplete certificate")
        choices = verify_step(records[used], prefix, box, vertices, denominator)
        work.extend(prefix + (v,) for v in reversed(choices))
        used += 1
    if used != len(records):
        raise ValueError("Extra certificate entries")
    print(f"Natural bounding box: {box}")
    print(f"Domain size {prod(hi-lo+1 for lo, hi in box)}; verified {used} internal prefixes")
    print(f"Counts by depth: {[counts[k] for k in range(N+1)]}; exclusions {dict(exclusions)}")
    return records


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate", action="store_true")
    parser.add_argument("--proof", type=Path, default=DEFAULT_PROOF)
    args = parser.parse_args()
    if args.generate:
        proof = traverse()
        data = json.dumps(proof, separators=(",", ":")).encode("ascii")
        args.proof.write_bytes(gzip.compress(data, compresslevel=9, mtime=0))
    else:
        traverse(json.loads(gzip.decompress(args.proof.read_bytes())))
