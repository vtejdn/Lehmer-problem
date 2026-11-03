"""Independent SymPy verification of the adjacent net-trace repair result.

Reconstructs the mathematical input without importing the original certificate.
Integer/rational and finite-field arithmetic only; no numerical roots or tolerances.
Prose strings in result.json are not comparison gates.
"""

import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

import sympy as sp


HERE = _J_OUTPUT
payload = json.loads((HERE / "result.json").read_text(encoding="utf-8"))
t, y, u = sp.symbols("t y u")
checked_fields = []


def compare(name, value):
    assert payload[name] == value, (name, payload[name], value)
    checked_fields.append(name)


def ascending(poly):
    return [int(poly.nth(j)) for j in range(poly.degree() + 1)]


q = sp.Poly(t**24 - t**17 - t**12 - t**7 + 1, t, domain=sp.ZZ)
phi6 = sp.Poly(sp.cyclotomic_poly(6, t), t, domain=sp.ZZ)
p = q.exquo(phi6)
compare("q_coefficients_ascending", ascending(q))
compare("p_coefficients_ascending", ascending(p))
assert p.degree() == 22 and p.LC() == p.TC() == 1
assert ascending(p) == list(reversed(ascending(p)))

# Construct the trace polynomial through SymPy's Chebyshev polynomials,
# independently of the original recurrence and its handwritten coefficients.
H = sp.Poly(2 * sp.chebyshevt(12, y / 2)
            - 2 * sp.chebyshevt(5, y / 2) - 1, y, domain=sp.ZZ)
Q = H.exquo(sp.Poly(y - 1, y, domain=sp.ZZ))
compare("trace_Q_coefficients_ascending", ascending(Q))
assert sp.expand(t**11 * Q.as_expr().subs(y, t + 1 / t)) == p.as_expr()
compare("verified_identities", {
    "Phi6_times_p_equals_q": True,
    "(y_minus_1)_times_Q_equals_C12_minus_C5_minus_1": True,
    "p_is_monic_reciprocal_with_constant_one": True,
})

Q2 = sp.Poly(Q.as_expr(), y, modulus=2)
assert Q2.is_irreducible
assert Q.is_irreducible
assert p.is_irreducible
compare("Q_mod2_bitmask", sum((int(Q2.nth(j)) % 2) << j
                                 for j in range(Q2.degree() + 1)))
residue = sp.Poly(y, y, modulus=2)
remainders = []
for _ in range(11):
    residue = (residue * residue).rem(Q2)
    remainders.append(sum((int(residue.nth(j)) % 2) << j
                          for j in range(residue.degree() + 1)))
compare("squaring_remainders_for_y_2power1_through11", remainders)
assert residue == sp.Poly(y, y, modulus=2)
compare("Q_0", int(Q.eval(0)))
compare("Q_1", int(Q.eval(1)))
assert Q.eval(0) < 0 < Q.eval(1)

intervals = payload["eight_unit_circle_trace_intervals"]
assert len(intervals) == 8
previous_right = None
for row in intervals:
    left, right = sp.Rational(row["a"]), sp.Rational(row["b"])
    assert -2 <= left < right < 2
    if previous_right is not None:
        assert previous_right < left
    left_value, right_value = Q.eval(left), Q.eval(right)
    assert left_value == sp.Rational(row["Q_a"])
    assert right_value == sp.Rational(row["Q_b"])
    assert left_value * right_value < 0
    previous_right = right
checked_fields.append("eight_unit_circle_trace_intervals")

bound_value = q.eval(sp.Rational(12, 11))
assert bound_value == sp.Rational(payload["q_at_12_over_11"])
assert bound_value > 0
checked_fields.append("q_at_12_over_11")
assert sp.Rational(12, 11)**3 < sp.Rational(13, 10)
assert sp.Rational(13, 10)**3 - sp.Rational(13, 10) - 1 < 0

# Logarithmic derivative of the reciprocal polynomial gives power sums.
# This avoids importing or reproducing the original Newton recursion.
reciprocal = sp.expand(u**p.degree() * p.as_expr().subs(t, 1 / u))
trace_series = sp.series(-u * sp.diff(reciprocal, u) / reciprocal,
                         u, 0, 7).removeO().expand()
traces = {j: trace_series.coeff(u, j) for j in range(1, 7)}
normalized = []
for n in range(1, 7):
    value = sum(sp.mobius(n // j) * traces[j] for j in sp.divisors(n)) / n
    assert value.is_Integer
    normalized.append(int(value))
compare("b_p_indices_1_through6", normalized)

canonical_factor = sp.Poly((t - 1) * (t**6 - 1), t, domain=sp.ZZ)
canonical = p * canonical_factor
compare("canonical_repair_degree", int(canonical_factor.degree()))
compare("optimal_repair_degree", int(phi6.degree()))
compare("canonical_completion_coefficients_ascending", ascending(canonical))
compare("canonical_completion_length", sum(abs(a) for a in ascending(canonical)))
compare("optimal_completion_length", sum(abs(a) for a in ascending(q)))
assert canonical.degree() == 29

# Positive rescaling preserves every Sturm endpoint sign.  Retain primitive
# integer versions of the rational Sturm polynomials to keep the exact
# endpoint certificate compact and directly checkable.
sturm_polys = []
for expression in sp.sturm(Q.as_expr(), y):
    rational_poly = sp.Poly(expression, y, domain=sp.QQ)
    denominator = sp.ilcm(1, *(a.q for a in rational_poly.all_coeffs()))
    integer_coeffs = [int(a * denominator) for a in rational_poly.all_coeffs()]
    divisor = sp.igcd(0, *integer_coeffs)
    assert denominator > 0 and divisor > 0
    sturm_polys.append(sp.Poly.from_list(
        [a // divisor for a in integer_coeffs], y, domain=sp.ZZ))


def variations(signs):
    nonzero = [s for s in signs if s]
    return sum(a != b for a, b in zip(nonzero, nonzero[1:]))


sturm_endpoints = {}
for label, point in (("minus_two", -2), ("plus_two", 2)):
    values = [poly.eval(point) for poly in sturm_polys]
    signs = [int(sp.sign(value)) for value in values]
    sturm_endpoints[label] = {
        "point": str(point),
        "exact_values": [str(value) for value in values],
        "signs": signs,
        "variations": variations(signs),
    }
for label, negative in (("minus_infinity", True), ("plus_infinity", False)):
    signs = [int(sp.sign(poly.LC())) * (-1 if negative and poly.degree() % 2 else 1)
             for poly in sturm_polys]
    sturm_endpoints[label] = {"signs": signs, "variations": variations(signs)}
assert Q.eval(-2) != 0 and Q.eval(2) != 0
count_inside = (sturm_endpoints["minus_two"]["variations"]
                - sturm_endpoints["plus_two"]["variations"])
count_all_real = (sturm_endpoints["minus_infinity"]["variations"]
                  - sturm_endpoints["plus_infinity"]["variations"])
count_above_two = (sturm_endpoints["plus_two"]["variations"]
                   - sturm_endpoints["plus_infinity"]["variations"])
count_below_minus_two = (sturm_endpoints["minus_infinity"]["variations"]
                         - sturm_endpoints["minus_two"]["variations"])
assert count_inside == Q.count_roots(-2, 2) == 8
assert count_all_real == Q.count_roots(-sp.oo, sp.oo) == 9
assert count_above_two == Q.count_roots(2, sp.oo) == 1
assert count_below_minus_two == Q.count_roots(-sp.oo, -2) == 0

result = {
    "status": "passed",
    "input": "result.json",
    "arithmetic": "exact integers, rationals and GF(2)",
    "checked_payload_fields": checked_fields,
    "checked_payload_field_count": len(checked_fields),
    "independent_irreducibility_checks": {
        "Q_over_GF2": True, "Q_over_Q": True, "p_over_Q": True,
    },
    "rational_interval_count": len(intervals),
    "canonical_repair_degree": int(canonical_factor.degree()),
    "minimum_repair_candidate_degree": int(phi6.degree()),
    "canonical_completion_length": sum(abs(a) for a in ascending(canonical)),
    "candidate_completion_length": sum(abs(a) for a in ascending(q)),
    "exact_sturm_certificate": {
        "normalization": "Each rational Sturm polynomial rescaled by a positive rational to a primitive integer polynomial",
        "sequence_coefficients_descending": [
            [str(a) for a in poly.all_coeffs()] for poly in sturm_polys
        ],
        "endpoints": sturm_endpoints,
        "open_interval_minus_two_to_two_roots": int(count_inside),
        "total_real_roots": int(count_all_real),
        "real_roots_above_two": int(count_above_two),
        "real_roots_below_minus_two": int(count_below_minus_two),
        "nonreal_trace_roots": int(Q.degree() - count_all_real),
        "agrees_with_sympy_count_roots": True,
    },
    "proof_boundary": (
        "Checks finite arithmetic only. Global net-trace positivity, unique "
        "optimality among all cyclotomic repairs, all-power field degree "
        "preservation, the Mahler bound, and the exact expanding-root count "
        "require the separately recorded graph, field and root-pattern proofs."
    ),
}
rendered = json.dumps(result, indent=2)
(HERE / "verification.json").write_text(rendered + "\n", encoding="utf-8")
print(rendered)
