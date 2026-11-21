"""Test all positive exterior roots in the fixed Mos26b Salem catalogue."""

import argparse
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path


GROUP = Path(__file__).resolve().parent
sys.path.insert(0, str(GROUP.parent / "Yin_J_G0173"))
from least_exponents import homogeneous_value, source_rows


def sign_at(half, x):
    return homogeneous_value(half, x.numerator, x.denominator)


def bisect(half, lo, hi):
    mid = (lo + hi) / 2
    value = sign_at(half, mid)
    if value == 0:
        raise ArithmeticError("Unexpected rational Salem root")
    return (mid, hi) if value < 0 else (lo, mid)


def initial_bracket(half, displayed):
    # Decimal digits suggest endpoints. Exact substitutions certify their signs.
    radius = Fraction(1, 10**12)
    lo, hi = Fraction(displayed) - radius, Fraction(displayed) + radius
    if not (lo > 1 and sign_at(half, lo) < 0 < sign_at(half, hi)):
        lo, hi = Fraction(7, 6), Fraction(49, 37)
        if not (sign_at(half, lo) < 0 < sign_at(half, hi)):
            raise ValueError("Source root outside the catalogue window")
        while hi - lo > 2 * radius:
            lo, hi = bisect(half, lo, hi)
    return lo, hi


def power_remainders(half):
    # The reciprocal monic polynomial reads in either coefficient order.
    full = half + half[-2::-1]
    degree = len(full) - 1
    powers = [(1,) + (0,) * (degree - 1)]

    def power(n):
        while len(powers) <= n:
            last = powers[-1]
            shifted = (0,) + last[:-1]
            powers.append(tuple(x - last[-1] * c for x, c in zip(shifted, full)))
        return powers[n]

    return power


def test_rank(rank, half, displayed, show_bounds):
    lo, hi = initial_bracket(half, displayed)
    power = power_remainders(half)
    totals = Counter()
    maxima = Counter()
    hits = []
    short = 1
    while True:
        base = lo**short
        bound = 2 * base / (base - 1)**2
        max_q = bound.numerator // bound.denominator
        if not max_q:
            if show_bounds:
                print(f"rank={rank} U>={short} all q excluded by radius")
            break
        maxima["U"] = short
        maxima["q"] = max(maxima["q"], max_q)
        if show_bounds:
            print(f"rank={rank} U={short} q>{max_q} excluded by radius")
        for q in range(1, max_q + 1):
            while True:
                t0, t1 = lo**short, hi**short
                d0, d1 = q*t0 - (q + 1), q*t1 - (q + 1)
                if d0*d1 > 0:
                    break
                lo, hi = bisect(half, lo, hi)
            sign = 1 if d0 > 0 else -1
            ratios = [((q + 1)*t - q)/abs(d) for t, d in ((t0, d0), (t1, d1))]
            low_y, high_y = min(ratios), max(ratios)
            totals["pairs"] += 1
            long = short + 1
            first_overlap = None
            while lo**long <= high_y:
                maxima["V"] = max(maxima["V"], long)
                maxima["U+V"] = max(maxima["U+V"], short + long)
                totals["remainders"] += 1
                overlap = hi**long >= low_y
                if overlap:
                    totals["overlaps"] += 1
                    if first_overlap is None:
                        first_overlap = long
                vectors = zip(power(0), power(short), power(long), power(short + long))
                zero = all(q*(a + sign*d) == (q + 1)*(b + sign*c) for a, b, c, d in vectors)
                if zero:
                    if not overlap:
                        raise ArithmeticError("Exact division contradicts the graph bounds")
                    hit = (rank, q, short, long, sign)
                    hits.append(hit)
                    print("HIT rank,q,U,V,epsilon", *hit, flush=True)
                long += 1
            if show_bounds:
                overlap_range = "empty" if first_overlap is None else f"{first_overlap}..{long-1}"
                print(f"rank={rank} U={short} q={q} eps={sign:+} "
                      f"qT-(q+1)=[{d0},{d1}] V<={long-1} "
                      f"graph_overlap={overlap_range}")
        short += 1
    return totals, maxima, hits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bounds", action="store_true",
                        help="show every radius cutoff, denominator interval and V range")
    args = parser.parse_args()
    totals, maxima = Counter(), Counter()
    hits, complete_ranks = [], []
    print("rank degree pairs remainders graph_overlaps max_q max_U max_V max_U+V")
    for rank, degree, displayed, half in source_rows():
        counts, limits, found = test_rank(rank, half, displayed, args.bounds)
        print(rank, degree, counts["pairs"], counts["remainders"], counts["overlaps"],
              limits["q"], limits["U"], limits["V"], limits["U+V"])
        totals.update(counts)
        maxima |= limits
        hits.extend(found)
        if degree <= 44 and sign_at(half, Fraction(13, 10)) > 0:
            complete_ranks.append(rank)
    print("totals", dict(totals))
    print("maxima", dict(maxima))
    print("hits", hits)
    print("complete source range: degree <= 44 and root < 13/10", complete_ranks)


if __name__ == "__main__":
    main()
