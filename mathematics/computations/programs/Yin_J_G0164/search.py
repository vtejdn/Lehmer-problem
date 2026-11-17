"""Exact integer-level and endpoint-Taylor searches in Boyd's 45 Salem rows."""

import csv
import json
from functools import cache
from pathlib import Path
from tempfile import NamedTemporaryFile

from sympy import Poly, Rational, Symbol, ZZ

X = Symbol("X")
HOME_DIR = Path(__file__).resolve().parent
OUTPUT = HOME_DIR.parents[1] / "outputs" / HOME_DIR.name / "results.json"
RADIUS = Rational(9, 130)
X_POLY = Poly(X, X, domain=ZZ)
TWO = Poly(2, X, domain=ZZ)


def coefficients(poly):
    return [int(value) for value in poly.all_coeffs()]


def trace_polynomial(half):
    degree = len(half) - 1
    previous, current = TWO, X_POLY
    trace = Poly(half[-1], X, domain=ZZ)
    for j in range(1, degree + 1):
        trace += half[-1-j] * current
        previous, current = current, X_POLY * current - previous
    return trace


@cache
def real_roots(poly):
    """Isolating intervals in increasing order for a monic irreducible factor."""
    roots = []
    for (lo, hi), multiplicity in poly.intervals(eps=Rational(1, 10000)):
        assert multiplicity == 1
        roots.append((lo, hi))
    return tuple(roots)


def compare(poly, index, other, other_index):
    if poly == other:
        return (index > other_index) - (index < other_index)
    lo, hi = real_roots(poly)[index]
    other_lo, other_hi = real_roots(other)[other_index]
    while not (hi <= other_lo or other_hi <= lo):
        if hi-lo >= other_hi-other_lo:
            lo, hi = poly.refine_root(lo, hi, steps=1)
        else:
            other_lo, other_hi = other.refine_root(other_lo, other_hi, steps=1)
    return -1 if hi <= other_lo else 1


PLUS_TWO = X_POLY - 2
MINUS_TWO = X_POLY + 2


def index_above_two(factor, index):
    return compare(factor, index, PLUS_TWO, 0) > 0


def classify(candidate, parent, lehmer, catalogue):
    unit, factors = candidate.factor_list()
    assert unit == 1
    product = Poly(1, X, domain=ZZ)
    hits = []
    factor_records = []
    in_window = 0
    for factor, exponent in factors:
        product *= factor**exponent
        roots = real_roots(factor)
        inside_parent = [
            j for j in range(len(roots))
            if index_above_two(factor, j)
            and compare(factor, j, parent, parent.degree()-1) < 0
        ]
        factor_records.append({
            "coefficients": coefficients(factor), "multiplicity": int(exponent),
            "real_root_count": len(roots), "window_indices": inside_parent,
        })
        in_window += len(inside_parent)
        if not inside_parent or factor.degree() < 2 or len(roots) != factor.degree():
            continue
        last = len(roots)-1
        if inside_parent != [last] or compare(factor, 0, MINUS_TWO, 0) <= 0:
            continue
        if compare(factor, last-1, PLUS_TWO, 0) >= 0:
            continue
        relation = compare(factor, last, lehmer, lehmer.degree()-1)
        hits.append({
            "table_row": catalogue.get(factor),
            "trace_coefficients": coefficients(factor),
            "Salem_degree": 2*factor.degree(),
            "multiplicity": int(exponent),
            "vs_Lehmer": ("smaller", "equal", "larger")[relation+1],
        })
    assert product == candidate
    return {"distinct_traces_in_window": in_window, "Salem_outputs": hits, "factors": factor_records}


def certify_input(source):
    half = [int(coefficient) for coefficient in source["half_polynomial"].split()]
    assert len(half) * 2 - 2 == int(source["degree"])
    if source["number"] == "39.5":
        half = [(-1)**j * coefficient for j, coefficient in enumerate(half)]
    trace = trace_polynomial(half)
    assert trace.is_irreducible and trace.LC() == 1
    assert len(real_roots(trace)) == trace.degree()
    assert compare(trace, 0, MINUS_TWO, 0) > 0
    assert compare(trace, trace.degree()-2, PLUS_TWO, 0) < 0
    assert compare(trace, trace.degree()-1, PLUS_TWO, 0) > 0
    estimate = Rational(source["listed_value"])
    error = Rational(1, 10**10)
    lower, upper = estimate - error, estimate + error
    assert 1 < lower < upper < Rational(13, 10)
    assert trace.eval(lower + 1/lower) < 0 < trace.eval(upper + 1/upper)
    return trace


def search_row(number, parent, lehmer, catalogue):
    # Taylor coefficients are integral, in ascending powers of X-2.
    h = list(reversed(parent.shift(2).all_coeffs()))
    limit = int(sum(-c * RADIUS**j for j, c in enumerate(h) if c < 0))
    levels = {}
    for magnitude in range(1, limit+1):
        levels[str(-magnitude)] = classify(parent + magnitude, parent, lehmer, catalogue)
    tails = {}
    quotient = parent
    for k in range(1, parent.degree()):
        quotient = (quotient - h[k-1]).exquo(PLUS_TWO)
        tails[str(k)] = classify(quotient, parent, lehmer, catalogue)
    return {
        "number": number, "trace_coefficients": coefficients(parent),
        "level_magnitude_bound": limit, "levels": levels, "Taylor_orders": tails,
    }


def main():
    with (HOME_DIR / "inputs" / "boyd.tsv").open(encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    expected = [str(i) for i in range(1, 43)] + ["21.5", "39.5", "41.5"]
    assert len(rows) == len(expected) and {row["number"] for row in rows} == set(expected)
    parents = {row["number"]: certify_input(row) for row in rows}
    catalogue = {parent: number for number, parent in parents.items()}
    assert len(catalogue) == len(parents)
    lehmer = parents["1"]
    assert coefficients(lehmer) == [1, 1, -5, -5, 4, 3]
    result = [search_row(n, poly, lehmer, catalogue) for n, poly in parents.items()]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(mode="w", encoding="utf-8", dir=OUTPUT.parent, delete=False) as stream:
        temporary = Path(stream.name)
        json.dump(result, stream, indent=2)
        stream.write("\n")
    temporary.replace(OUTPUT)
    for label in ("levels", "Taylor_orders"):
        tests = [(row["number"], parameter, value)
                 for row in result for parameter, value in row[label].items()]
        print(label, len(tests), "tested,", sum(bool(v["distinct_traces_in_window"]) for _, _, v in tests), "with traces in (2,T)")
        for number, parameter, value in tests:
            for hit in value["Salem_outputs"]:
                print(number, parameter, "->", hit["table_row"], hit["Salem_degree"], hit["vs_Lehmer"], hit["trace_coefficients"])


if __name__ == "__main__":
    main()
