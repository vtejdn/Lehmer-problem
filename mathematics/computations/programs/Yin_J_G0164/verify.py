"""Check J164's factor certificates by binomial inversion and Sturm variations."""

import csv
import json
from collections import Counter
from functools import cache
from math import comb
from pathlib import Path

from sympy import Poly, Rational, Symbol, ZZ


BASE = Path(__file__).resolve().parent
X = Symbol("X")


def polynomial(coefficients):
    return Poly.from_list(coefficients, X, domain=ZZ)


def trace_from_lift(lift):
    """Remove Z^m (Z+1/Z)^j, successively from highest nonzero degree."""
    m = lift.degree() // 2
    residual = list(reversed(lift.all_coeffs()))
    trace = []
    for j in range(m, -1, -1):
        coefficient = residual[m + j]
        trace.append(coefficient)
        for i in range(j + 1):
            residual[m + j - 2*i] -= coefficient * comb(j, i)
    assert not any(residual)
    return polynomial(trace)


@cache
def sturm(poly):
    # Make each signed Euclidean remainder primitive by a positive multiplier.
    sequence = [poly, poly.diff()]
    while sequence[-1].degree() > 0:
        remainder = -sequence[-2].to_field().rem(sequence[-1].to_field())
        assert not remainder.is_zero
        integral = remainder.clear_denoms(convert=True)[1]
        sequence.append(integral.primitive()[1])
    return sequence


@cache
def variation(poly, point):
    signs = []
    for term in sturm(poly):
        if point == "-inf":
            value = term.LC() * (-1)**term.degree()
        elif point == "+inf":
            value = term.LC()
        else:
            value = term.eval(point)
        if value:
            signs.append(bool(value > 0))
    return sum(left != right for left, right in zip(signs, signs[1:]))


def load_inputs():
    catalogue, brackets, flipped = {}, {}, []
    with (BASE / "inputs/boyd.tsv").open(encoding="utf-8") as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            label = row["number"]
            half = list(map(int, row["half_polynomial"].split()))
            printed = polynomial(half + half[-2::-1])
            assert printed.degree() == int(row["degree"])
            center = Rational(row["listed_value"])
            radius = Rational(1, 10**10)
            left, right = center - radius, center + radius
            choices = [p for p in (printed, printed.compose(polynomial([-1, 0])))
                       if p.eval(left) < 0 < p.eval(right)]
            assert len(choices) == 1
            if choices[0] != printed:
                flipped.append(label)
                assert printed.eval(1) == 1 and printed.eval(-1) < 0
            trace = trace_from_lift(choices[0])
            lo, hi = left + 1/left, right + 1/right
            assert trace.is_irreducible and 2 < lo < hi
            assert variation(trace, -2) - variation(trace, 2) == trace.degree()-1
            assert variation(trace, lo) - variation(trace, hi) == 1
            assert label not in catalogue and trace not in catalogue.values()
            catalogue[label], brackets[label] = trace, (lo, hi)
    assert flipped == ["39.5"]
    return catalogue, brackets


def root_counts(factor, parent, lo, hi):
    if factor.degree() == 1:
        # A linear monic factor has an integer root; the whole input window is below 3.
        assert hi < 3
        return 1, [], False
    assert factor.eval(-2) and factor.eval(2)
    while (not factor.eval(lo) or not factor.eval(hi)
           or variation(factor, lo) != variation(factor, hi)):
        middle = (lo + hi)/2
        if parent.eval(middle) < 0:
            lo = middle
        else:
            hi = middle
    before = variation(factor, "-inf")
    real = before - variation(factor, "+inf")
    below_two = before - variation(factor, 2)
    below_parent = before - variation(factor, lo)
    window = list(range(below_two, below_parent))
    neutral = variation(factor, -2) - variation(factor, 2)
    return real, window, bool(window) and neutral == factor.degree() - 1


def verify():
    parents, brackets = load_inputs()
    names = {poly: label for label, poly in parents.items()}
    saved = BASE.parents[1] / "outputs" / BASE.name / "results.json"
    rows = json.loads(saved.read_text(encoding="utf-8"))
    assert len(rows) == len(parents) == 45 and {r["number"] for r in rows} == set(parents)
    totals, edges, bernstein_levels = Counter(), [], 0
    rational_roots = {}
    for row in rows:
        label = row["number"]
        parent = parents[label]
        m = parent.degree()
        assert polynomial(row["trace_coefficients"]) == parent
        # Shift by 2 using substitution of coefficients in the binomial theorem.
        ascending = list(reversed(parent.all_coeffs()))
        h = [sum(ascending[j] * comb(j, i) * 2**(j-i) for j in range(i, m+1))
             for i in range(m+1)]
        radius = brackets[label][1] - 2
        assert radius < Rational(9, 130)
        # Bernstein control values enclose S on the whole interval [2,2+radius].
        bernstein = [sum(h[j] * radius**j * Rational(comb(i, j), comb(m, j))
                         for j in range(i+1)) for i in range(m+1)]
        tighter_bound = int(-min(bernstein))
        bernstein_levels += tighter_bound
        limit = row["level_magnitude_bound"]
        assert 0 <= tighter_bound <= limit
        assert set(row["levels"]) == {str(-j) for j in range(1, limit+1)}
        assert set(row["Taylor_orders"]) == {str(k) for k in range(1, m)}
        for family in ("levels", "Taylor_orders"):
            for parameter, result in row[family].items():
                k = int(parameter)
                candidate = (parent-k if family == "levels" else
                             polynomial(list(reversed(h[k:]))).shift(-2))
                # Identify the catalogue divisors independently of the saved factors.
                catalogue_hits = {
                    name for name, target in parents.items()
                    if brackets[name][1] < brackets[label][0] and candidate.rem(target).is_zero
                }
                product = polynomial([1])
                total_roots, targets, seen = 0, [], set()
                for data in result["factors"]:
                    factor = polynomial(data["coefficients"])
                    assert factor not in seen and factor.LC() == 1 and factor.is_irreducible
                    seen.add(factor)
                    exponent = data["multiplicity"]
                    assert isinstance(exponent, int) and exponent > 0
                    product *= factor**exponent
                    real, window, salem = root_counts(factor, parent, *brackets[label])
                    assert real == data["real_root_count"] and window == data["window_indices"]
                    total_roots += len(window)
                    if salem:
                        target = names[factor]
                        relation = "equal" if target == "1" else "larger"
                        if target != "1":
                            assert brackets[target][0] > brackets["1"][1]
                        targets.append((target, factor, exponent, relation))
                        edges.append((family, label, k, target))
                assert product == candidate
                if family == "levels" and targets:
                    roots = {int(-f.TC()) for f in seen if f.degree() == 1}
                    assert roots == {i for i in range(-2, 3) if candidate.eval(i) == 0}
                    rational_roots[label] = sorted(roots)
                    if label == "36":
                        sextic = polynomial([1, 0, -5, 1, 6, -1, -1])
                        assert candidate == polynomial([1, -2]) * parents["1"] * sextic
                        assert variation(sextic, "-inf") - variation(sextic, "+inf") == 4
                assert total_roots == result["distinct_traces_in_window"]
                reported = [(t["table_row"], polynomial(t["trace_coefficients"]),
                             t["multiplicity"], t["vs_Lehmer"]) for t in result["Salem_outputs"]]
                assert targets == reported
                assert catalogue_hits == {target for target, _, _, _ in targets}
                assert all(t["Salem_degree"] == 2*len(t["trace_coefficients"])-2
                           for t in result["Salem_outputs"])
                totals[family, "tested"] += 1
                totals[family, "occupied"] += bool(total_roots)
                totals[family, "roots"] += total_roots
    for family in ("levels", "Taylor_orders"):
        print(family, {name: totals[family, name] for name in ("tested", "occupied", "roots")})
        for entry in edges:
            if entry[0] == family:
                print(*entry[1:])
    print("Sum of independent Bernstein level bounds:", bernstein_levels)
    print("Rational trace roots of the successful levels:", rational_roots)
    print("Only row 39.5 required reversing the exterior sign.")


if __name__ == "__main__":
    verify()
