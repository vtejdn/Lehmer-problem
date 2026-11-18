"""Exact factor and root-signature census of the primitive cubic directions."""

from argparse import ArgumentParser
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction
from functools import cache
from math import comb, gcd
from pathlib import Path
from tempfile import TemporaryDirectory
import json

from sympy import Poly, ZZ, cyclotomic_poly, symbols


X = symbols("x")
T = symbols("t")
CAP = 104
STURM_CONTROLS = {(5, 61), (8, 77), (5, 89), (17, 53)}
HOME_GROUP = Path(__file__).resolve().parent
COMPUTATIONS = HOME_GROUP.parents[1]


@cache
def cyclotomic_orders():
    # phi(m)^2 >= m/2, as seen on each prime power.
    limit = 2 * CAP**2
    totients = list(range(limit + 1))
    for prime in range(2, limit + 1):
        if totients[prime] == prime:
            for multiple in range(prime, limit + 1, prime):
                totients[multiple] -= totients[multiple] // prime
    return {
        tuple(cyclotomic_poly(m, X, polys=True).all_coeffs()): m
        for m in range(1, limit + 1) if totients[m] <= CAP
    }


def monic_parent(a, b):
    coefficients = {}
    for exponent, value in [(0, 1), (a, 1), (3*a, -1), (b, -1),
                            (b+2*a, 1), (b+3*a, 1)]:
        coefficients[exponent] = coefficients.get(exponent, 0) + value
    return Poly.from_dict(coefficients, X, domain=ZZ)


def reciprocal_trace(descending):
    """Construct the trace by the Chebyshev recurrence and check its lift."""
    if len(descending) % 2 == 0 or descending != descending[::-1]:
        return None
    n = len(descending) // 2
    trace = [descending[n]] + [0] * n
    previous, current = [2], [0, 1]
    for j in range(1, n + 1):
        for i, coefficient in enumerate(current):
            trace[i] += descending[n - j] * coefficient
        following = [0] + current
        for i, coefficient in enumerate(previous):
            following[i] -= coefficient
        previous, current = current, following
    lifted = [0] * (2*n + 1)
    for j, coefficient in enumerate(trace):
        for k in range(j + 1):
            lifted[n - j + 2*k] += coefficient * comb(j, k)
    if lifted != descending[::-1]:
        raise ValueError("Reciprocal trace lift failed to reconstruct its factor")
    return Poly.from_list(trace[::-1], T, domain=ZZ)


def signature(trace):
    endpoints = {cut: trace.eval(cut) for cut in (-2, 2)}
    if 0 in endpoints.values():
        raise ValueError("A noncyclotomic factor has trace +2 or -2")
    below = inside = above = 0
    for (left, right), multiplicity in trace.intervals():
        if multiplicity != 1:
            raise ValueError("A trace of an irreducible factor has a multiple root")

        def is_below(cut):
            if right <= cut:
                return True
            if left >= cut:
                return False
            # The interval contains a unique simple root and straddles the cut.
            return trace.eval(left) * endpoints[cut] < 0

        if is_below(-2):
            below += 1
        elif is_below(2):
            inside += 1
        else:
            above += 1
    nonreal = trace.degree() - below - inside - above
    if nonreal < 0 or nonreal % 2:
        raise ValueError("Invalid count of nonreal trace roots")
    return {"circle_roots": 2 * inside, "negative_real_exterior": below,
            "positive_real_exterior": above, "nonreal_exterior_pairs": nonreal // 2}


def sturm_variations(trace):
    """Integer remainders proportional by positive constants to the Sturm chain."""
    chain = [trace, trace.diff()]
    while chain[-1].degree() > 0:
        a, b = chain[-2:]
        remainder = a.prem(b)
        if remainder.is_zero:
            raise ValueError("A control trace is not squarefree")
        leading_sign = 1 if b.LC() > 0 else -1
        signed = -leading_sign**(a.degree() - b.degree() + 1) * remainder
        chain.append(signed.primitive()[1])
    variations = []
    for cut in ("minus_infinity", -2, 2, "plus_infinity"):
        signs = []
        for polynomial in chain:
            if cut == "minus_infinity":
                value = polynomial.LC() * (-1)**polynomial.degree()
            elif cut == "plus_infinity":
                value = polynomial.LC()
            else:
                value = polynomial.eval(cut)
            if value:
                signs.append(1 if value > 0 else -1)
        variations.append(sum(a != b for a, b in zip(signs, signs[1:])))
    return variations


def factor_direction(direction):
    a, b = direction
    parent = monic_parent(a, b)
    unit, factors = parent.factor_list()
    if unit != 1 or parent.degree() != 3*a + b:
        raise ValueError(f"Unexpected leading term at {direction}")
    reconstructed = Poly(1, X, domain=ZZ)
    orders = cyclotomic_orders()
    torsion, other = [], []
    for factor, multiplicity in factors:
        reconstructed *= factor**multiplicity
        coefficients = [int(c) for c in factor.all_coeffs()]
        order = orders.get(tuple(coefficients))
        if order is not None:
            torsion.append([order, multiplicity])
        else:
            trace = reciprocal_trace(coefficients)
            counts = None if trace is None else signature(trace)
            record = {"degree": factor.degree(), "multiplicity": multiplicity,
                      "coefficients_descending": coefficients, "signature": counts}
            if direction in STURM_CONTROLS and trace is not None:
                variations = sturm_variations(trace)
                low, middle, high = [a - b for a, b in zip(variations, variations[1:])]
                if (low, 2*middle, high) != (counts["negative_real_exterior"],
                                             counts["circle_roots"],
                                             counts["positive_real_exterior"]):
                    raise ValueError(f"Sturm and isolated-root counts disagree at {direction}")
                record["sturm_variations_at_minus_inf_minus2_plus2_plus_inf"] = variations
            other.append(record)
    if reconstructed != parent:
        raise ValueError(f"Factorization failed to multiply back at {direction}")
    return {"a": a, "b": b, "cyclotomic_orders_and_multiplicities": sorted(torsion),
            "nontorsion_factors": other}


def summarize(rows):
    counts = [sum(f["multiplicity"] for f in row["nontorsion_factors"]) for row in rows]
    factors = [(row, f) for row in rows for f in row["nontorsion_factors"]]
    degrees = [f["degree"] for _, f in factors]
    reciprocal = [(row, f["signature"]) for row, f in factors if f["signature"] is not None]
    mismatches = [row for row, s in reciprocal if s["nonreal_exterior_pairs"] != row["a"]]
    largest_mismatch = max(mismatches, key=lambda row: Fraction(row["b"], row["a"]),
                           default=None)
    return {"directions": len(rows), "empty": counts.count(0), "one": counts.count(1),
            "multiple": sum(c >= 2 for c in counts),
            "minimum_factor_degree": min(degrees, default=None),
            "maximum_factor_degree": max(degrees, default=None),
            "reciprocal_factors": len(reciprocal),
            "factors_with_circle_roots": sum(s["circle_roots"] > 0 for _, s in reciprocal),
            "factors_with_real_exterior": sum(s["negative_real_exterior"] +
                                              s["positive_real_exterior"] > 0
                                              for _, s in reciprocal),
            "factors_with_a_nonreal_exterior_pairs": len(reciprocal) - len(mismatches),
            "greatest_ratio_mismatch_direction": None if largest_mismatch is None else
                [largest_mismatch["a"], largest_mismatch["b"]]}


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=1)
    workers = parser.parse_args().workers
    if workers < 1:
        parser.error("--workers must be positive")
    directions = [(a, b) for a in range(1, (CAP - 1)//3 + 1)
                  for b in range(1, CAP - 3*a + 1) if gcd(a, b) == 1]
    if workers == 1:
        rows = list(map(factor_direction, directions))
    else:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            rows = list(pool.map(factor_direction, directions, chunksize=4))
    summaries = {"b_gt_3a": summarize([row for row in rows if row["b"] > 3*row["a"]]),
                 "b_le_3a": summarize([row for row in rows if row["b"] <= 3*row["a"]]),
                 "all": summarize(rows)}
    payload = {"degree_cap": CAP, "summaries": summaries, "directions": rows}
    output = COMPUTATIONS / "outputs" / HOME_GROUP.name / "census.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    scratch = COMPUTATIONS.parents[1] / ".tmp"
    scratch.mkdir(exist_ok=True)
    with TemporaryDirectory(dir=scratch) as temporary:
        result = Path(temporary) / output.name
        result.write_text(json.dumps(payload, separators=(",", ":")) + "\n",
                          encoding="utf-8")
        result.replace(output)
    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()
