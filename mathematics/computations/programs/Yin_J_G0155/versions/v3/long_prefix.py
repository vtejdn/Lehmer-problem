"""Certify integer zero-profile completions through index six, 39 <= p <= 55."""

import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache
import json
from pathlib import Path
import sys
import tempfile

from sympy import cyclotomic_poly, I, Poly, Rational


GROUP = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(GROUP / "versions" / "v2"))
import fixed_prefix as v2


PREFIX = (2, 0, 4, 0, 4)
WITNESS = (2, 0, 4, 0, 4, 0, 3, 0, 2, 0, 1, 0, 0, 0, -1, 0,
           -2, 0, -2, 0, -1, 0, 0, 0, 0, 0, 0)
grid_rows = lru_cache(maxsize=None)(v2.grid_rows)


def enumerate_cut(parameters):
    p, kappa = parameters
    n = (p - 1) // 2
    rows = grid_rows(p)
    signs = [1] * (n - kappa) + [-1] * kappa
    box = [(p*p*(i + 1) + 3) // 4 for i in range(n)]
    matrix, rhs = [], []
    for (row, error), sign in zip(rows, signs):
        matrix.append([-sign * value for value in row])
        rhs.append(sum(limit * e for limit, e in zip(box, error)))
    matrix.append([-v2.ROW_SCALE * (-1)**i for i in range(n)])
    rhs.append(v2.ROW_SCALE)
    stats = Counter(outer_leaves=0, grid_zero_leaves=0)
    accepted = []

    def visit(coefficients, target):
        i = len(coefficients)
        if i == n:
            if min(target) >= 0:
                stats["outer_leaves"] += 1
                actual = v2.exact_signs(p, coefficients, rows)
                if actual is None:
                    stats["grid_zero_leaves"] += 1
                elif actual == signs:
                    assert 2 + sum((-1)**j * a for j, a in enumerate(coefficients)) > 0
                    accepted.append(coefficients)
            return
        remaining = [row[i:] for row in matrix]
        for value in v2.integer_ranges(remaining, target, box[i:]):
            visit(coefficients + (value,),
                  [b - row[i] * value for b, row in zip(target, matrix)])

    target = [b - sum(a * v for a, v in zip(PREFIX, row)) for b, row in zip(rhs, matrix)]
    visit(PREFIX, target)
    return {"p": p, "kappa": kappa, **stats, "strict_completions": accepted}


def verify_witness():
    p, n = 55, 27
    t, z = v2.t, v2.z
    e = v2.basis(n+1, Poly(t, t))
    b = [Poly(1, t)] + [e[i] + e[i-1] for i in range(1, n+1)]
    assert v2.exact_signs(p, WITNESS, grid_rows(p)) == [1]*26 + [-1]
    h = sum((a * f for a, f in zip(WITNESS, e)), Poly(0, t))
    u = Poly(t*t - 2, t)
    trace2, trace5 = u**2 - 2, u**5 - 5*u**3 + 5*u
    assert h == u*(u+1)*(u+2)*(1 + trace2 - trace2*trace5)
    remainder = sum((a * b[n-i-1] for i, a in enumerate(WITNESS)), Poly(0, t))
    assert remainder.degree() == 26 and remainder.LC() == 2
    q = Poly(t, t) * b[n] + remainder
    assert q.eval(-2) / b[n].eval(-2) == -12
    lift = sum((Poly(a*z**(n+1-i)*(1+z*z)**i, z) for (i,), a in q.terms()), Poly(0, z))
    assert lift.degree() == 56 and lift.all_coeffs() == list(reversed(lift.all_coeffs()))
    difference = Poly((1-z)*(1-z*z), z)*lift - Poly((1+z*z)**2, z)
    assert all(difference.nth(i) == 0 for i in range(8)) and difference.nth(8) == -1
    # At the roots of the monic B_n the remainder and Q have the same values.
    signed_resultant = b[n].resultant(remainder)
    assert signed_resultant == 7303
    unit, factors = lift.factor_list()
    product = Poly(unit, z)
    for factor, power in factors:
        product *= factor**power
    cyclotomics = {Poly(cyclotomic_poly(i, z), z) for i in (3, 4, 6, 8)}
    assert product == lift and unit == 1 and len(factors) == 5
    assert {f for f, k in factors if k == 1 and f.degree() < 46} == cyclotomics
    core, = [f for f, k in factors if f.degree() == 46 and k == 1]
    extra = {2, 3, 8, 9, 10, 11, 35, 36, 37, 38, 43, 44}
    assert core == Poly(sum((1 + (i in extra))*z**i for i in range(47)), z)
    # C881 v10 implies that the two exterior roots are one conjugate pair.
    x0, x1, y0, y1 = (Rational(i, 10**10) for i in
                      (3079691, 3079692, 12253983046, 12253983047))
    assert core.count_roots(x0 + I*y0, x1 + I*y1) == 1
    lower, upper = x0*x0 + y0*y0, x1*x1 + y1*y1
    assert Rational("1.5016010997") < lower < upper < Rational("1.5016011001")
    return {"p": p, "kappa": 1, "coefficients": WITNESS, "endpoint_ratio": -12,
            "resultant": int(signed_resultant), "last_matching_index": 7,
            "first_discrepancy": -1, "cyclotomic_orders": [3, 4, 6, 8],
            "irreducible_core_coefficients": [int(a) for a in core.all_coeffs()],
            "exterior_rectangle": list(map(str, (x0, x1, y0, y1))),
            "whole_measure_bounds": list(map(str, (lower, upper)))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--witness-only", action="store_true")
    parser.add_argument("--jobs", type=int, default=1, help="parallel cut enumerations")
    args = parser.parse_args()
    result = {"witness": verify_witness()}
    name = "long_prefix_witness.json"
    if not args.witness_only:
        pairs = [(p, k) for p in range(55, 38, -2) for k in range(1, (p-1)//2)
                 if 6 * (2*k+1) <= p]
        with ProcessPoolExecutor(max_workers=args.jobs) as pool:
            records = sorted(pool.map(enumerate_cut, pairs), key=lambda r: (r["p"], r["kappa"]))
        strict = [(r["p"], r["kappa"], a) for r in records for a in r["strict_completions"]]
        assert strict == [(55, 1, WITNESS)]
        result["enumeration"] = records
        name = "long_prefix_enumeration.json"
    out = GROUP.parents[1] / "outputs" / GROUP.name / name
    out.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=out.parent,
                                         delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(result, stream, indent=2)
            stream.write("\n")
        temporary.replace(out)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    print(out)


if __name__ == "__main__":
    main()
