"""Independently verify census.json using the primitive-direction torsion table."""

from collections import Counter
from fractions import Fraction
from math import comb, gcd
from pathlib import Path
import json

from sympy import Poly, ZZ, cyclotomic_poly, symbols


CAP = 104
CONTROLS = {(5, 61), (8, 77), (5, 89), (17, 53)}
x, t = symbols("x t")
X = Poly(x, x, domain=ZZ)
TORSION = {m: cyclotomic_poly(m, x, polys=True) for m in (2, 6, 8, 10, 12, 18, 30)}


def torsion_orders(a, b):
    """Read the congruences of L462 v172, including the parity condition."""
    selected = {
        2: (a - b) % 2 == 1,
        6: gcd(a, 6) == 2 and (b - 3 - 2*a) % 6 == 0,
        8: a % 2 == 1 and (b - a) % 8 == 0,
        10: gcd(a, 10) == 2 and (b - 5 - 3*a) % 10 == 0,
        12: gcd(a, 12) == 1 and (b - 2*a) % 12 == 0,
        18: gcd(a, 18) == 1 and (b - 4*a) % 18 == 0,
        30: gcd(a, 30) == 1 and (b - 9*a) % 30 == 0,
    }
    return [m for m in selected if selected[m]]


def recover_trace(coefficients):
    """Subtract full centered binomial lifts from highest to lowest degree."""
    degree = len(coefficients) - 1
    n = degree // 2
    assert degree == 2*n and coefficients[::-1] == coefficients
    remainder = coefficients[::-1]
    trace = []
    for j in range(n, -1, -1):
        value = remainder[n+j]
        trace.append(value)
        for k in range(j+1):
            remainder[n-j+2*k] -= value * comb(j, k)
    assert not any(remainder)
    return trace


def signed_remainder(dividend, divisor):
    """Ordinary Euclidean cancellation, scaled only by positive integers."""
    rest = dividend.copy()
    while len(rest) >= len(divisor):
        shift = len(rest) - len(divisor)
        common = gcd(rest[-1], divisor[-1])
        scale = abs(divisor[-1]) // common
        multiple = rest[-1] // common
        if divisor[-1] < 0:
            multiple = -multiple
        rest = [scale * value for value in rest]
        for i, value in enumerate(divisor):
            rest[i+shift] -= multiple * value
        while rest and rest[-1] == 0:
            rest.pop()
        if rest:
            content = gcd(*rest)
            rest = [v // content for v in rest]
    return [-v for v in rest]


def sturm(descending):
    first = descending[::-1]
    chain = [first, [i*v for i, v in enumerate(first) if i]]
    while len(chain[-1]) > 1:
        following = signed_remainder(chain[-2], chain[-1])
        assert following, "repeated trace root"
        chain.append(following)
    result = []
    for cutoff in ("left", -2, 2, "right"):
        signs = []
        for poly in chain:
            if cutoff == "left":
                value = poly[-1] * (-1)**(len(poly)-1)
            elif cutoff == "right":
                value = poly[-1]
            else:
                value = 0
                for c in reversed(poly):
                    value = cutoff*value+c
                if poly is first:
                    assert value, "trace root at a cutoff"
            if value:
                signs.append(value > 0)
        result.append(sum(u != v for u, v in zip(signs, signs[1:])))
    return result


def verify_row(a, b, row):
    y = X**a
    core = -(y**3-y-1 + X**b*(1-y**2-y**3))
    orders = torsion_orders(a, b)
    for order in orders:
        core = core.exquo(TORSION[order])
    assert row["cyclotomic_orders_and_multiplicities"] == [[m, 1] for m in orders]
    if core.degree() == 0:
        assert core.is_one and row["nontorsion_factors"] == []
        return None
    coefficients = list(map(int, core.all_coeffs()))
    trace = recover_trace(coefficients)
    trace_poly = Poly.from_list(trace, t, domain=ZZ)
    assert trace_poly.is_irreducible, (a, b, "reducible trace")
    variations = sturm(trace)
    below, middle, above = [u-v for u, v in zip(variations, variations[1:])]
    # An interior real embedding makes t^2-4 negative. The quadratic lift
    # therefore doubles the irreducible trace degree over Q.
    assert middle > 0 and min(below, above) >= 0
    nonreal = trace_poly.degree()-below-middle-above
    assert nonreal >= 0 and nonreal % 2 == 0
    pairs = nonreal // 2
    assert below+above+pairs > 0
    expected = {
        "degree": core.degree(), "multiplicity": 1,
        "coefficients_descending": coefficients,
        "signature": {"circle_roots": 2*middle, "negative_real_exterior": below,
                      "positive_real_exterior": above, "nonreal_exterior_pairs": pairs},
    }
    if (a, b) in CONTROLS:
        expected["sturm_variations_at_minus_inf_minus2_plus2_plus_inf"] = variations
        print((a, b), "orders", orders, "variations", variations,
              "degree", core.degree(), "circle", 2*middle, "pairs", pairs, flush=True)
    assert row["nontorsion_factors"] == [expected], (a, b, "factor or signature")
    return core.degree(), below+above, pairs


def verify_summary(records, reported):
    nonempty = {key: value for key, value in records.items() if value is not None}
    degrees = [value[0] for value in nonempty.values()]
    mismatches = [key for key, value in nonempty.items() if key[0] != value[2]]
    last = max(mismatches, key=lambda key: Fraction(key[1], key[0]))
    expected = dict(directions=len(records), empty=len(records)-len(nonempty),
                    one=len(nonempty), multiple=0, minimum_factor_degree=min(degrees),
                    maximum_factor_degree=max(degrees), reciprocal_factors=len(degrees),
                    factors_with_circle_roots=len(degrees),
                    factors_with_real_exterior=sum(value[1] > 0 for value in nonempty.values()),
                    factors_with_a_nonreal_exterior_pairs=len(degrees)-len(mismatches),
                    greatest_ratio_mismatch_direction=list(last))
    assert reported == expected
    minima = [key for key, value in nonempty.items() if value[0] == min(degrees)]
    print("directions", len(records), "empty", [k for k, v in records.items() if v is None],
          "minimum", min(degrees), minima, "maximum", max(degrees), "last mismatch", last)


def main():
    if not __debug__:
        raise RuntimeError("Run without Python optimization so that all checks execute.")
    group = Path(__file__).resolve().parent
    report = json.loads((group.parents[1]/"outputs"/group.name/"census.json").read_text())
    assert report["degree_cap"] == CAP
    rows = {(row["a"], row["b"]): row for row in report["directions"]}
    assert len(rows) == len(report["directions"])
    records = {}
    orders = Counter()
    for degree in range(4, CAP+1):
        for a in range(1, (degree-1)//3+1):
            b = degree-3*a
            if gcd(a, degree) == 1:
                row = rows[a, b]
                records[a, b] = verify_row(a, b, row)
                orders.update(torsion_orders(a, b))
    assert records.keys() == rows.keys()
    summaries = report["summaries"]
    verify_summary({k: v for k, v in records.items() if k[1] > 3*k[0]}, summaries["b_gt_3a"])
    verify_summary({k: v for k, v in records.items() if k[1] <= 3*k[0]}, summaries["b_le_3a"])
    verify_summary(records, summaries["all"])
    print("verified all", len(records), "directions; cyclotomic occurrences", dict(sorted(orders.items())))


if __name__ == "__main__":
    main()
