"""Separate exact review of every retained row, without Mahler approximations.

The reviewed author programs and JSON files are read-only.  This checker does
not import their helpers or use their root-type labels as an oracle.  SymPy
remains a shared arithmetic library; this is not an independent implementation
of polynomial factorization or real-root isolation.
"""

from collections import Counter
from hashlib import sha256
from math import gcd
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time

import sympy as sp

HERE = (_J_PROGRAM / 'review_exact.py').parent
t, x = sp.symbols("t x")
AUTHOR_FILES = ("pilot.py", "pilot.json", "certify_structure.py",
                "structural-certificate.json", "readme.md")


def trace_from_coefficients(poly):
    """Build the invariant Laurent polynomial through the C_j recurrence."""
    degree = poly.degree()
    assert degree % 2 == 0
    assert poly.all_coeffs() == poly.all_coeffs()[::-1]
    half = degree // 2
    c = [sp.Integer(2), x]
    for j in range(2, half + 1):
        c.append(sp.expand(x * c[-1] - c[-2]))
    ans = sp.Poly(poly.nth(half) + sum(
        poly.nth(half + j) * c[j] for j in range(1, half + 1)), x)
    assert sp.expand(t**half * ans.as_expr().subs(x, t + 1/t)
                     - poly.as_expr()) == 0
    return ans


def isolated_real_counts(poly):
    """Count exact rational isolating intervals in the three trace regions."""
    assert poly.eval(-2) != 0 and poly.eval(2) != 0
    counts = [0, 0, 0]  # below -2, inside (-2,2), above 2
    retained_intervals = []
    for (lo, hi), multiplicity in poly.intervals():
        # Irreducible characteristic-zero reciprocal factors give simple
        # traces.  This is checked here rather than assumed in the counts.
        assert multiplicity == 1
        for refinement in range(100):
            if hi <= -2:
                region = 0
                break
            if lo >= -2 and hi <= 2:
                region = 1
                break
            if lo >= 2:
                region = 2
                break
            lo, hi = poly.refine_root(lo, hi, steps=2)
        else:
            raise AssertionError("Root interval failed to separate endpoints")
        counts[region] += multiplicity
        retained_intervals.append([str(lo), str(hi), multiplicity, region])
    nonreal = poly.degree() - sum(counts)
    assert nonreal >= 0 and nonreal % 2 == 0
    return counts, nonreal, retained_intervals


def main():
    started = time.perf_counter()
    old_hashes = {name: sha256((((_J_PROGRAM if name in ('certify_structure.py', 'pilot.py', 'readme.md', 'review_exact.py') else _J_OUTPUT) / name)).read_bytes()).hexdigest()
                  for name in AUTHOR_FILES}
    data = json.loads(((_J_OUTPUT / 'pilot.json')).read_text(encoding="utf-8"))
    assert data["completed"] and data["stop"] is None
    expected = {(a, b) for a in range(2, 13) for b in range(1, a)
                if gcd(a, b) == 1}
    pairs = [(row["a"], row["b"]) for row in data["rows"]]
    assert len(expected) == len(pairs) == len(set(pairs)) == 45
    assert set(pairs) == expected
    cyclo = {k: sp.Poly(sp.cyclotomic_poly(k, t), t)
             for k in (6, 12, 15)}
    lehmer = sp.Poly(t**10+t**9-t**7-t**6-t**5-t**4-t**3+t+1, t)
    types = Counter()
    orders = Counter()
    observed_salem = []
    reviewed = []
    for row in data["rows"]:
        assert time.perf_counter() - started < 120
        a, b = row["a"], row["b"]
        ell = min(b, a-b)
        seed = t**a-t**b-1
        reverse = 1-t**(a-b)-t**a
        actual = sp.Poly(sp.expand((reverse**2*seed.subs(t, t**2)
                                   + seed**2*reverse.subs(t, t**2))/2), t)
        assert actual.eval(1) == -1
        W, remainder = sp.div(actual, sp.Poly(t**ell, t))
        assert remainder.is_zero and row["ell"] == ell
        assert W.degree() == row["W_degree"] == 4*a-2*ell
        assert W.LC() == W.nth(0) == row["W_leading"]
        assert W.LC() == (2 if (a, b) == (2, 1) else 1)
        content, primitive = W.primitive()
        assert content == row["content"] == 1
        product = sp.Poly(content, t)
        noncyclotomic = []
        factor_records = []
        for entry in row["factors"]:
            factor = sp.Poly.from_list(entry["coefficients_descending"], t)
            assert factor.as_expr() == sp.sympify(entry["polynomial"],
                                                 locals={"t": t})
            assert factor.degree() == entry["degree"]
            assert factor.is_irreducible
            assert entry["monic"] == (factor.LC() == 1)
            multiplicity = entry["multiplicity"]
            assert isinstance(multiplicity, int) and multiplicity > 0
            product *= factor**multiplicity
            matching = [k for k, c in cyclo.items() if c == factor]
            if matching:
                assert len(matching) == 1 and entry["cyclotomic"]
                orders[matching[0]] += 1
                factor_records.append({"cyclotomic_order": matching[0],
                                       "multiplicity": multiplicity})
                continue
            T = trace_from_coefficients(factor)
            assert entry["reciprocal"] and not entry["cyclotomic"]
            assert T.as_expr() == sp.sympify(entry["trace_polynomial"],
                                            locals={"x": x})
            assert T.all_coeffs() == entry["trace_coefficients_descending"]
            (negative, inside, positive), nonreal, intervals = isolated_real_counts(T)
            expanding = positive + negative + nonreal
            # A certified off-circle root also independently excludes all
            # other cyclotomic orders, without trusting the stored flag.
            assert expanding > 0
            actual_counts = (inside, positive, negative, nonreal, expanding)
            stored_counts = tuple(entry[k] for k in (
                "unit_circle_pairs", "positive_real_expanding",
                "negative_real_expanding", "nonreal_trace_roots",
                "total_expanding_roots"))
            assert actual_counts == stored_counts
            if factor.LC() == 1 and expanding == positive == 1:
                kind = "Salem"
                observed_salem.append((a, b))
                assert factor == lehmer
            elif expanding > 1:
                kind = "multiple_expanding"
            else:
                assert factor.LC() != 1 and expanding == 1
                kind = "nonmonic_one_expanding"
            assert kind == entry["type"]
            assert multiplicity == 1
            noncyclotomic.append(factor)
            types[kind] += 1
            factor_records.append({"degree": factor.degree(), "type": kind,
                "trace": str(T.as_expr()), "trace_intervals": intervals,
                "counts_inside_positive_negative_nonreal_expanding": actual_counts})
        assert product == W and len(noncyclotomic) == 1
        has_phi6 = a % 6 in (1, 5) and b % 6 == (2*a) % 6
        quotient, remainder = sp.div(sp.Poly(seed, t), cyclo[6])
        assert remainder.is_zero == has_phi6
        reviewed.append({"a": a, "b": b, "factors": factor_records})
    assert observed_salem == [(3, 1), (5, 4)]
    assert types == {"Salem": 2, "multiple_expanding": 42,
                     "nonmonic_one_expanding": 1}
    new_hashes = {name: sha256((((_J_PROGRAM if name in ('certify_structure.py', 'pilot.py', 'readme.md', 'review_exact.py') else _J_OUTPUT) / name)).read_bytes()).hexdigest()
                  for name in AUTHOR_FILES}
    assert old_hashes == new_hashes
    result = {'all_assertions_passed': True, 'complete_expected_pair_set': True, 'reviewed_rows': 45, 'types': dict(types), 'cyclotomic_factor_row_occurrences': dict(orders), 'salem_pairs_both_exact_lehmer': observed_salem, 'author_files': list(AUTHOR_FILES), 'rows': reviewed, 'scope': 'Separate complete exact retained-data checker using rational real-root isolation, not author count_roots labels; shares SymPy exact arithmetic and irreducibility backend. No Mahler decimals, Delta sign certification, enlarged scan or rerun of the author programs.'}
    ((_J_OUTPUT / 'review-exact.json')).write_text(
        json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items()
                      if k != "rows"}, indent=2))


if __name__ == "__main__":
    main()
