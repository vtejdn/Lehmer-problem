"""Count cyclotomic completions from the published primitive small-measure list."""
import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from math import comb
from pathlib import Path
import re
import sys

from sympy import Poly, Rational, cyclotomic_poly, floor, symbols, totient

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "Yin_J_G0147"))
from census import classify, graeffe, to_trace, trace_basis

t, z = symbols("t z")
BASIS = trace_basis(22)
SCALE = 10**35


def compare(poly, num, den):
    """Strict whole-measure comparison, using signed endpoints and Graeffe."""
    degree = len(poly) - 1
    bins = [comb(degree, j) for j in range(degree + 1)]
    for endpoint in (num, -num):
        value = scale = 1
        for a in poly[1:]:
            scale *= den
            value = endpoint * value + scale * a
        if value < 0:
            return 1
    for step in range(18):
        if any(abs(a)*den > num*b for a, b in zip(poly, bins)):
            return 1
        if den**2 * sum(a*a for a in poly) < num**2:
            return -1
        poly = graeffe(poly)
        num, den = num*num, den*den
    raise ArithmeticError("Unresolved measure comparison")


@dataclass(frozen=True)
class Core:
    poly: tuple
    low: bool
    row: str
    subst: tuple


def cores(table):
    rows = []
    options = []
    for line in table.read_text().splitlines():
        if not re.match(r"^\s*\d+\s+1\.\d+\s+\d+\s", line):
            continue
        d, approx, _, *coeff = line.split()
        degree = int(d)
        if degree > 44:
            continue
        half = tuple(map(int, coeff))
        assert 2*(len(half)-1) == degree
        original = half + half[-2::-1]
        assert compare(original, 23, 20) == 1
        low = classify(original, [comb(degree,i) for i in range(degree+1)]) == "inside"
        rows.append(original)
        for m in range(1, 44//degree + 1):
            for sign in (1, -1):
                lifted = [0]*(m*degree + 1)
                lifted[::m] = [a*sign**i for i, a in enumerate(original)]
                if m > 1 and not Poly.from_list(lifted, z).is_irreducible:
                    continue
                if sum(a*(-1)**i for i,a in enumerate(lifted)) > 0:
                    options.append(Core(tuple(lifted), low, approx, (sign,m)))
    assert len(set(rows)) == len(rows) == 944
    assert len({row.poly for row in options}) == len(options)
    return options


def mask_on_grid(poly, intervals):
    co = list(map(int, poly.all_coeffs()))
    mask = 0
    for i,(left,right) in enumerate(intervals):
        lo = hi = co[0]
        scale = 1
        for c in co[1:]:
            scale *= SCALE
            values = (lo*left, lo*right, hi*left, hi*right)
            lo, hi = min(values)+c*scale, max(values)+c*scale
        if hi < 0:
            mask |= 1 << i
        elif lo <= 0:
            raise ArithmeticError("Unresolved grid sign")
    return mask


@lru_cache(None)
def cyclotomics(maxdeg):
    parts = [(1, (1,-2,1))]
    for m in range(3, 2*maxdeg**2+1):
        if totient(m) <= maxdeg:
            parts.append((m, tuple(map(int, Poly(cyclotomic_poly(m,z),z).all_coeffs()))))
    return sorted(parts, key=lambda item: len(item[1]))


def run(p, options, show):
    n = (p-1)//2
    degree = p+1
    B = Poly(1,t) + sum(BASIS[1:n+1], Poly(0,t))
    intervals = [(int(floor(l*SCALE)), int(floor(r*SCALE))+1)
                 for (l,r),_ in B.intervals(eps=Rational(1, SCALE*10))]
    assert len(intervals) == n
    # Strict floors certified by the atanh series in the README helper below.
    k = target_block(p)
    derivative = sum(1<<i for i in range(n) if (n-1-i)%2)
    wanted = defaultdict(lambda: defaultdict(list))
    norm_cache = {}
    for row in options:
        space = degree - len(row.poly) + 1
        if space < 0:
            continue
        trace = to_trace(row.poly, BASIS)
        mask = mask_on_grid(trace, intervals) ^ derivative
        for cut in range(1,n):
            wanted[space][mask ^ ((1<<cut)-1)].append((row,trace,cut))
    maxdeg = max(wanted)
    parts = []
    for order, poly in cyclotomics(maxdeg):
        trace = to_trace(poly, BASIS)
        norm = abs(int(B.resultant(trace)))
        if norm:
            parts.append((len(poly)-1, order, mask_on_grid(trace,intervals), norm))
    counts = Counter()
    by_cut = Counter()
    target = []
    chosen = []

    def visit(space, mask, norm, start):
        for row,trace,cut in wanted.get(space,{}).get(mask,()):
            by_cut[cut] += 1
            if row.low:
                counts["small"] += 1
            if cut != k:
                continue
            if row.poly not in norm_cache:
                norm_cache[row.poly] = abs(int(B.resultant(trace)))
            delta = norm * norm_cache[row.poly]
            assert delta > 0
            counts["target"] += 1
            counts["target_small"] += row.low
            counts["target_nonunit"] += delta > 1
            counts["target_small_nonunit"] += row.low and delta > 1
            product = Poly.from_list(row.poly, z)
            for order in chosen:
                factor = (z-1)**2 if order == 1 else cyclotomic_poly(order,z)
                product *= Poly(factor,z)
            coeffs = list(map(int, product.all_coeffs()))
            full_trace = to_trace(coeffs, BASIS)
            assert product.eval(-1) > 0 and abs(B.resultant(full_trace)) == delta
            assert mask_on_grid(full_trace, intervals) ^ derivative == (1<<k)-1
            assert compare(coeffs, 13, 10) == -1
            shift = 1 - coeffs[1]
            counts["target_profile_shift"] += shift in (-4,-2,0,2,4)
            if p == 15:
                assert coeffs == [1,0,0] + [1]*11 + [0,0,1]
                assert full_trace.count_roots(-2,2) == 6
                assert full_trace.count_roots() == 6
                assert compare(coeffs,1272,1000) == 1 and compare(coeffs,1274,1000) == -1
            target.append((row.row, row.subst, tuple(chosen), delta, shift))
        for j in range(start,len(parts)):
            width, order, extra, factor_norm = parts[j]
            if space + width > maxdeg:
                break
            chosen.append(order)
            visit(space+width, mask^extra, norm*factor_norm, j)
            chosen.pop()
    visit(0,0,1,0)
    print(p, k, counts["small"], sum(by_cut.values()), counts["target_small"],
          counts["target"], counts["target_nonunit"], counts["target_small_nonunit"],
          counts["target_profile_shift"], min(target,default=None), flush=True)
    if show:
        for witness in sorted(target):
            print("  ", witness)
    return counts, target


def target_block(p):
    # p / log(p), via log(p) = 2 atanh((p-1)/(p+1)).
    v = Rational(p-1,p+1)
    term = v
    lower = 0
    for j in range(160):
        lower += 2*term/(2*j+1)
        term *= v*v
    upper = lower + 2*term/(321*(1-v*v))
    small, large = floor(p/upper), floor(p/lower)
    assert small == large
    return int(small)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("table", type=Path)
    parser.add_argument("conductors", type=int, nargs="*", default=list(range(13,44,2)))
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()
    options = cores(args.table)
    for p in args.conductors:
        if p not in range(13,44,2):
            parser.error("Supported conductors are odd and between 13 and 43.")
        run(p, options, args.show)
