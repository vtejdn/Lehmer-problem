"""Search the full integer zero-profile chart with coefficients fixed through index eight."""

import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction
from functools import lru_cache
import json
from math import ceil
from pathlib import Path
import sys
import tempfile

import mpmath
import numpy as np
from scipy.optimize._highspy import _core

GROUP = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(GROUP / "versions" / "v2"))
import fixed_prefix as v2


PREFIX = (2, 0, 4, 0, 4, 0, 4)


@lru_cache(maxsize=None)
def grid_rows(p):
    n = (p-1)//2
    scale = 1 << 96
    rows = []
    previous = Fraction(2)
    for j in range(1, n+1):
        with mpmath.workprec(144):
            center = int(mpmath.nint(scale*2*mpmath.cos(2*mpmath.pi*j/p)))
        left, right = Fraction(center-1, scale), Fraction(center+1, scale)
        assert -2 < left < right < previous
        assert v2.denominator(n, left)*v2.denominator(n, right) < 0
        previous = left
        mid = v2.basis(n, Fraction(center, scale))
        row = [round(v2.ROW_SCALE * a) for a in mid]
        error = [ceil(Fraction(1, 2) + Fraction(v2.ROW_SCALE * (i+1) * i*i, scale))
                 for i in range(n)]
        rows.append((row, error))
    return rows


def enumerate_cut(parameters):
    p, kappa = parameters
    n = (p-1)//2
    rows = grid_rows(p)
    signs = [1]*(n-kappa) + [-1]*kappa
    full_box = [(p*p*(i+1)+3)//4 for i in range(n)]
    matrix, rhs = [], []
    for (row, error), sign in zip(rows, signs):
        matrix.append([-sign*a for a in row])
        rhs.append(sum(e*b for e, b in zip(error, full_box)))
    matrix.append([-v2.ROW_SCALE * (-1)**i for i in range(n)])
    rhs.append(v2.ROW_SCALE)
    size = n-len(PREFIX)
    rhs = [b-sum(a*v for a, v in zip(PREFIX, row)) for b, row in zip(rhs, matrix)]
    matrix = [row[len(PREFIX):] for row in matrix]
    box = full_box[len(PREFIX):]
    cols = list(zip(*matrix))
    lp = _core._Highs()
    for name, value in (("output_flag", False), ("presolve", "off"), ("threads", 1)):
        lp.setOptionValue(name, value)
    assert lp.addVars(size, -np.array(box), np.array(box)) == _core.HighsStatus.kOk
    indices = np.arange(size, dtype=np.int32)
    for row, b in zip(matrix, rhs):
        assert lp.addRow(-lp.getInfinity(), b/v2.ROW_SCALE, size, indices,
                         np.array(row)/v2.ROW_SCALE) == _core.HighsStatus.kOk
    counts = Counter(outer_leaves=0, grid_zero_leaves=0)
    accepted = []
    denominator = v2.ROW_SCALE * v2.DUAL_SCALE

    def bound(dual, target, i, sign):
        weights = [max(0, round(-a*v2.DUAL_SCALE)) for a in dual]
        nonzero = [(j,w) for j,w in enumerate(weights) if w]
        total = sum(w*target[j] for j,w in nonzero)
        for k in range(i, size):
            residual = sum(w*cols[k][j] for j,w in nonzero)
            if k == i:
                residual -= sign*denominator
            total += abs(residual)*box[k]
        return total

    def ranges(target, i):
        maximum = []
        for sign in (1, -1):
            lp.changeColCost(i, -sign)
            lp.run()
            if lp.getModelStatus() == _core.HighsModelStatus.kOptimal:
                maximum.append(bound(lp.getSolution().row_dual, target, i, sign)//denominator)
                continue
            _, exists, ray = lp.getDualRay()
            if exists and bound(ray, target, i, 0) < 0:
                lp.changeColCost(i, 0)
                return range(0)
            lp.changeColCost(i, 0)
            return v2.integer_ranges([row[i:] for row in matrix], target, box[i:])
        lp.changeColCost(i, 0)
        return range(max(-box[i], -maximum[1]), min(box[i], maximum[0])+1)

    def visit(tail, target):
        i = len(tail)
        if i == size:
            if min(target) >= 0:
                counts["outer_leaves"] += 1
                vector = PREFIX + tail
                actual = v2.exact_signs(p, vector, rows)
                if actual is None:
                    counts["grid_zero_leaves"] += 1
                elif actual == signs:
                    assert 2+sum((-1)**j*a for j,a in enumerate(vector)) > 0
                    accepted.append(vector)
            return
        for value in ranges(target, i):
            lp.changeColBounds(i, value, value)
            visit(tail+(value,), [b-v*value for b,v in zip(target, cols[i])])
        lp.changeColBounds(i, -box[i], box[i])

    visit((), rhs)
    print(f"p={p}, kappa={kappa}, strict={len(accepted)}", flush=True)
    return {"p": p, "kappa": kappa, **counts, "strict_completions": accepted}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=57)
    parser.add_argument("--end", type=int, default=83)
    parser.add_argument("--jobs", type=int, default=1)
    args = parser.parse_args()
    if args.start < 57 or args.end < args.start or not args.start%2 or not args.end%2:
        parser.error("expected an ordered odd conductor interval starting at or above 57")
    pairs = [(p,k) for p in range(args.end, args.start-1, -2)
             for k in range(1,(p-1)//2) if 6*(2*k+1) <= p]
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        results = sorted(pool.map(enumerate_cut, pairs), key=lambda r:(r["p"],r["kappa"]))
    out = GROUP.parents[1]/"outputs"/GROUP.name/f"prefix_eight_{args.start}_{args.end}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=out.parent,
                                         delete=False) as stream:
            tmp = Path(stream.name)
            json.dump(results, stream, indent=2)
            stream.write("\n")
        tmp.replace(out)
    finally:
        if tmp is not None:
            tmp.unlink(missing_ok=True)
    print(out)


if __name__ == "__main__":
    main()
