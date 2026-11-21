"""Exact factorization and root counts for the coprime two-pole sections."""

import argparse
from concurrent.futures import ProcessPoolExecutor
from collections import Counter
import json
from math import gcd
from pathlib import Path
from tempfile import NamedTemporaryFile

from flint import fmpq_poly, fmpz_poly


X = fmpz_poly([0, 1])
ONE = fmpz_poly([1])
A = (X**2 - 3*X - 1) * (X**2 - 4*X - 1)
A_STAR = fmpz_poly(A.coeffs()[::-1])


def parent(k, ell):
    return A.inflate(k).left_shift(2*ell) + ONE.left_shift(ell+2*k) + A_STAR.inflate(k)


def trace_polynomial(poly):
    coefficients = poly.coeffs()
    half = poly.degree() // 2
    if poly.degree() != 2*half or coefficients != coefficients[::-1]:
        return None
    trace = fmpz_poly([coefficients[half]])
    previous = 2*ONE
    current = X
    for step in range(1, half+1):
        trace += coefficients[half+step] * current
        previous, current = current, X*current - previous
    return trace


def sturm_signature(trace):
    """Count real trace roots in the three open intervals cut by -2 and 2."""
    if trace(-2) == 0 or trace(2) == 0:
        raise ArithmeticError("an endpoint belongs to a noncyclotomic factor")
    chain = [trace, trace.derivative()]
    while chain[-1].degree() > 0:
        remainder = -(fmpq_poly(chain[-2]) % fmpq_poly(chain[-1])).numer()
        if not remainder:
            raise ArithmeticError("trace has a repeated root")
        chain.append(remainder // remainder.content())
    previous = [0]*4
    changes = [0]*4
    for term in chain:
        leading = term.leading_coefficient()
        values = (leading * (-1)**term.degree(), term(-2), term(2), leading)
        for pos, value in enumerate(values):
            if value:
                sign = 1 if value > 0 else -1
                changes[pos] += previous[pos] == -sign
                previous[pos] = sign
    low, middle, high = (a-b for a, b in zip(changes,changes[1:]))
    exterior = trace.degree() - middle
    if min(low, middle, high, exterior-low-high) < 0 or (exterior-low-high) % 2:
        raise ArithmeticError("invalid Sturm signature")
    return {"negative_real_exterior": low, "positive_real_exterior": high,
            "nonreal_exterior_pairs": (exterior-low-high)//2,
            "unit_circle": 2*middle, "exterior": exterior}


def direction(pair):
    k, ell = pair
    poly = parent(k, ell)
    content, parts = poly.factor()
    rebuilt = fmpz_poly([content])
    core, torsion = [], []
    for factor, mult in parts:
        rebuilt *= factor**mult
        order = int(factor.is_cyclotomic())
        if order:
            torsion.append([order, mult])
            continue
        trace = trace_polynomial(factor)
        if trace is None:
            raise ArithmeticError(f"nonreciprocal factor at {pair}: {factor}")
        signature = sturm_signature(trace)
        core.append({"degree": factor.degree(), "mult": mult, **signature,
                     "coefficients": [int(c) for c in factor.coeffs()]})
    if content != 1 or rebuilt != poly or poly.degree() != 2*ell + 4*k:
        raise ArithmeticError(f"parent reconstruction failed at {pair}")
    return {"k": k, "ell": ell, "torsion": sorted(torsion), "core": core}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--degree", type=int, default=120)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--extra", nargs="*", default=[], metavar="K,L")
    options = parser.parse_args()
    if options.degree < 1 or options.workers < 1:
        parser.error("degree and workers must be positive")
    pairs = {(k, ell) for k in range(1,options.degree//6+1)
             for ell in range(k+1,(options.degree-4*k)//2+1) if gcd(k,ell)==1}
    for spec in options.extra:
        k, ell = map(int, spec.split(","))
        if k < 1 or ell <= k or gcd(k,ell) != 1:
            parser.error("extra pairs must have 0 < K < L and be coprime")
        pairs.add((k,ell))
    ordered = sorted(pairs)
    if options.workers == 1:
        results = [direction(pair) for pair in ordered]
    else:
        with ProcessPoolExecutor(options.workers) as workers:
            results = list(workers.map(direction, ordered, chunksize=1))
    group = Path(__file__).resolve().parent
    target = group.parents[1]/"outputs"/group.name
    target.mkdir(parents=True,exist_ok=True)
    output = target/"census.json"
    with NamedTemporaryFile("w",encoding="utf8",dir=target,delete=False) as pending:
        json.dump(results,pending,separators=(",",":"))
        pending.write("\n")
    Path(pending.name).replace(output)
    print("directions",len(results))
    print("noncyclotomic factors including multiplicity",
          sorted(Counter(sum(f["mult"] for f in r["core"]) for r in results).items()))
    print("two exterior at k>1",
          [(r["k"],r["ell"]) for r in results if r["k"]>1 and any(f["exterior"]==2 for f in r["core"])])
    print("total exterior different from 2k",
          [(r["k"],r["ell"]) for r in results if sum(f["mult"]*f["exterior"] for f in r["core"])!=2*r["k"]])


if __name__ == "__main__":
    main()
