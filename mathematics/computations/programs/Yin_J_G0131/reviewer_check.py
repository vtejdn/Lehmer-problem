"""Independent bounded check of C700/J131; no author arithmetic is imported.

Scope fixed before execution: the 128 constant-one polynomials of degree <=7,
the nested 32 degree <=5 candidates, 32 B controls, 15 Theta controls and
15 leading generators; factor degrees <=7 and the proved order bound129.
Use dense F2 coefficient tuples, inverse-free character elimination,
quadratic-algebra multiplicative orders and cyclotomic Laurent recovery.
Read author inputs/outputs; write only independent_verification.json.
"""

import json
from functools import lru_cache
from math import comb, gcd as integer_gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parents[3] / "mathematics" / "computations" / "outputs" / HERE.name
PRECISION = 16


def trim(coefficients):
    c = list(coefficients)
    while c and c[-1] == 0:
        c.pop()
    return tuple(c)


def from_mask(value):
    assert type(value) is int and value >= 0
    return trim((value >> i) & 1 for i in range(value.bit_length()))


def mask(p):
    return sum(c << i for i, c in enumerate(p))


def add(p, q):
    return trim((p[i] if i < len(p) else 0) ^ (q[i] if i < len(q) else 0)
                for i in range(max(len(p), len(q))))


def multiply(p, q, limit=None):
    if not p or not q:
        return ()
    size = len(p) + len(q) - 1
    if limit is not None:
        size = min(size, limit)
    result = [0] * size
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            if i + j < size:
                result[i + j] ^= a & b
    return trim(result)


def power(p, exponent, limit=None):
    assert exponent >= 0
    result = (1,)
    for _ in range(exponent):
        result = multiply(result, p, limit)
    return result


def divide(p, q):
    assert q and q[-1] == 1
    r = p
    result = [0] * max(0, len(p) - len(q) + 1)
    while r and len(r) >= len(q):
        shift = len(r) - len(q)
        result[shift] ^= 1
        r = add(r, (0,) * shift + q)
    return trim(result), r


def exact_divide(p, q):
    quotient, remainder = divide(p, q)
    assert not remainder
    return quotient


def gcd(p, q):
    while q:
        p, q = q, divide(p, q)[1]
    return p


ONE = (1,)
X = (0, 1)
CHI = (0, 1, 0, 1, 0, 1)


def monomial_unit(e):
    assert e > 0
    return (1,) + (0,) * (e - 1) + (1,)


def compose_chi(p):
    result = ()
    for coefficient in reversed(p):
        result = add(multiply(result, CHI, PRECISION), (coefficient,))
    return result


def coefficient(p, j):
    return p[j] if j < len(p) else 0


def character_without_inversion(h):
    # Maintain H * product(selected generators) = numerator/denominator.
    # Equal lower coefficients let coefficient j be tested by direct XOR.
    numerator, denominator, exponent = trim(h[:PRECISION]), ONE, 0
    for j in range(1, PRECISION):
        if coefficient(numerator, j) != coefficient(denominator, j):
            if j & (j - 1) == 0:
                numerator = multiply(numerator, monomial_unit(j), PRECISION)
                exponent += j
            else:
                source = j - 2 * (j & -j)
                unit = monomial_unit(source)
                numerator = multiply(numerator, power(unit, 5, PRECISION), PRECISION)
                denominator = multiply(denominator, compose_chi(unit), PRECISION)
        assert all(coefficient(numerator, i) == coefficient(denominator, i)
                   for i in range(j + 1))
    assert numerator == denominator
    return (-exponent) % 16


def check_certificate(h, g, a):
    assert g and g[0] == 1 and len(g) <= PRECISION
    assert type(a) is int and 0 <= a < 16
    # H = G^5/G(chi) * (1+t)^a, checked without a unit inverse.
    lhs = multiply(h, compose_chi(g), PRECISION)
    rhs = multiply(power(g, 5, PRECISION), power((1, 1), a, PRECISION), PRECISION)
    assert lhs == rhs


def irreducible(p):
    degree = len(p) - 1
    if degree < 1 or p[0] != 1:
        return False
    x = divide(X, p)[1]
    frobenius = x
    for k in range(1, degree + 1):
        frobenius = divide(multiply(frobenius, frobenius), p)[1]
        if k <= degree // 2 and gcd(add(frobenius, x), p) != ONE:
            return False
    return frobenius == x


def trace_order_in_quadratic_algebra(f):
    # z^2 + x*z + 1 = 0 over F2[x]/f; z*(a+b*z)=b+(a+x*b)*z.
    degree = len(f) - 1
    a, b = ONE, ()
    for order in range(1, (1 << degree) + 2):
        a, b = b, divide(add(a, multiply(X, b)), f)[1]
        if (a, b) == (ONE, ()):
            assert order >= 3 and order % 2 == 1
            assert ((1 << degree) - 1) % order == 0 or ((1 << degree) + 1) % order == 0
            return order
    raise AssertionError("proved order bound failed")


@lru_cache(None)
def cyclotomic(n):
    assert n >= 1 and n % 2 == 1
    result = monomial_unit(n)
    for d in range(1, n):
        if n % d == 0:
            result = exact_divide(result, cyclotomic(d))
    return result


def recover_trace(reciprocal):
    degree = len(reciprocal) - 1
    assert degree % 2 == 0 and reciprocal == tuple(reversed(reciprocal))
    half = degree // 2
    remaining = list(reciprocal)
    result = [0] * (half + 1)
    for i in range(half, -1, -1):
        if remaining[half + i]:
            result[i] = 1
            for k in range(i + 1):
                remaining[half + i - 2 * k] ^= comb(i, k) & 1
    assert not any(remaining)
    answer = trim(result)
    assert answer[0] == 1
    return answer


def B_from_laurent(n):
    assert n >= 1 and n % 2 == 1
    return recover_trace((1,) * n)


def whole_trace(n):
    result = recover_trace(cyclotomic(n))
    assert len(result) - 1 == sum(integer_gcd(k, n) == 1 for k in range(1, n)) // 2
    derivative = trim((i & 1) * result[i] for i in range(1, len(result)))
    assert gcd(result, derivative) == ONE
    return result


def polynomial(p):
    return "+".join("1" if i == 0 else "t" if i == 1 else f"t^{i}"
                    for i, bit in enumerate(p) if bit) or "0"


def check_factors(row, all_irreducibles):
    remaining, reconstructed = from_mask(row["mask"]), ONE
    expected_factors, groups = [], {}
    for f in all_irreducibles:
        multiplicity = 0
        while remaining != ONE and not divide(remaining, f)[1]:
            remaining = exact_divide(remaining, f)
            multiplicity += 1
        if multiplicity:
            order = trace_order_in_quadratic_algebra(f)
            fp = power(f, multiplicity)
            reconstructed = multiply(reconstructed, fp)
            groups[order] = multiply(groups.get(order, ONE), fp)
            expected_factors.append({"mask": mask(f), "polynomial": polynomial(f),
                                     "degree": len(f) - 1, "multiplicity": multiplicity,
                                     "trace_order": order})
    assert remaining == ONE and reconstructed == from_mask(row["mask"])
    assert row["factors"] == expected_factors
    expected_groups = []
    for order, group in sorted(groups.items()):
        whole = whole_trace(order)
        exponent, residue = divmod(len(group) - 1, len(whole) - 1)
        complete = residue == 0 and exponent > 0 and power(whole, exponent) == group
        expected_groups.append({"order": order, "group_mask": mask(group),
                                "whole_mask": mask(whole), "whole_polynomial": polynomial(whole),
                                "whole_degree": len(whole) - 1, "complete": complete,
                                "whole_multiplicity": exponent if complete else None})
    assert row["order_groups"] == expected_groups
    assert row["complete_product"] == all(item["complete"] for item in expected_groups)
    return {"mask": row["mask"], "factors": expected_factors,
            "order_groups": expected_groups, "complete_product": row["complete_product"]}


def main():
    inputs = json.loads((HERE / "inputs.json").read_text(encoding="utf-8"))
    data = json.loads((OUTPUT / "classification.json").read_text(encoding="utf-8"))
    author_check = json.loads((OUTPUT / "verification.json").read_text(encoding="utf-8"))
    cases = [
        {"id": "m12_q32", "m": 12, "Q": 32, "epsilon": 0, "max_degree": 5,
         "candidate_count": 32, "target_character": 10},
        {"id": "m14_q32", "m": 14, "Q": 32, "epsilon": 0, "max_degree": 7,
         "candidate_count": 128, "target_character": 9}]
    expected_scope = {"precision": 16, "character_modulus": 16, "cases": cases,
                      "calibration_odd_indices": list(range(1, 64, 2)),
                      "theta_calibration_exponents": list(range(1, 16)),
                      "maximum_irreducible_degree": 7, "maximum_trace_order": 129}
    assert inputs == expected_scope and data["scope"] == expected_scope
    assert data["status"] == "complete" and data["unique_polynomials"] == 128
    assert [r["mask"] for r in data["rows"]] == list(range(1, 256, 2))
    irreducibles = [from_mask(m) for d in range(1, 8)
                   for m in range((1 << d) + 1, 1 << (d + 1), 2)
                   if irreducible(from_mask(m))]
    characters, factor_checks = [], []
    for row in data["rows"]:
        h, g = from_mask(row["mask"]), from_mask(row["source_g_mask"])
        a = character_without_inversion(h)
        assert row["ell_mod16"] == a
        check_certificate(h, g, a)
        assert row["degree"] == len(h) - 1 and row["polynomial"] == polynomial(h)
        steps = row["eliminated_orders"]
        assert steps == sorted(set(steps)) and all(1 <= j <= 15 for j in steps)
        step_g, step_a = ONE, 0
        for j in steps:
            if j & (j - 1) == 0:
                step_a += j
            else:
                step_g = multiply(step_g, monomial_unit(j - 2 * (j & -j)), PRECISION)
        assert (g, a) == (step_g, step_a)
        passes = [c["id"] for c in cases if len(h) - 1 <= c["max_degree"]
                  and a == c["target_character"]]
        assert row["passes"] == passes
        if passes:
            factor_checks.append(check_factors(row, irreducibles))
        characters.append({"mask": mask(h), "ell_mod16": a})
    checked_cases = []
    for case in cases:
        eligible = [r for r in characters if r["mask"] < 1 << (case["max_degree"] + 1)]
        assert len(eligible) == case["candidate_count"]
        passing = [r["mask"] for r in eligible if r["ell_mod16"] == case["target_character"]]
        checked_cases.append({**case, "passing_masks": passing, "passing_count": len(passing)})
    assert data["cases"] == checked_cases and author_check["cases"] == checked_cases
    assert data["leading_generators_checked"] == len(data["generators"]) == 15
    for item, j in zip(data["generators"], range(1, 16)):
        source = None if j & (j - 1) == 0 else j - 2 * (j & -j)
        generator = from_mask(item["mask"])
        assert item["order"] == j and item["source_exponent"] == source
        assert min(i for i in range(1, len(generator)) if generator[i]) == j
        if source is None:
            assert generator == monomial_unit(j)
        else:
            check_certificate(generator, monomial_unit(source), 0)
    assert len(data["B_calibration"]) == 32
    for item, n in zip(data["B_calibration"], range(1, 64, 2)):
        b = B_from_laurent(n)
        expected = ((1 - (1 if n % 4 == 1 else -1) * n) // 4) % 16
        assert item["n"] == n and item["character"] == item["expected"] == expected
        assert character_without_inversion(b) == expected
        check_certificate(b, from_mask(item["source_g_mask"]), expected)
    assert data["theta_controls_checked"] == len(data["theta_controls"]) == 15
    for item, e in zip(data["theta_controls"], range(1, 16)):
        unit = from_mask(item["unit_mask"])
        assert item["exponent"] == e and item["character"] == 0
        check_certificate(unit, monomial_unit(e), 0)
        check_certificate(unit, from_mask(item["source_g_mask"]), 0)
        assert character_without_inversion(unit) == 0
    assert author_check["status"] == "verified"
    assert author_check["relationship"] == "author verification, not independent review"
    for field, value in {"jet_precision": 16, "character_modulus": 16,
                         "complete_candidate_certificates": 128,
                         "passing_factorizations_and_complete_statuses": 9,
                         "B_calibration_certificates": 32, "theta_control_certificates": 15,
                         "leading_generator_checks": 15}.items():
        assert author_check[field] == value
    result = {"status": "verified", "relationship": "independent reviewer computation",
              "scope": expected_scope, "candidate_certificates_checked": 128,
              "characters_recomputed": characters, "cases": checked_cases,
              "passing_factor_checks": factor_checks,
              "B_controls_checked": 32, "theta_controls_checked": 15,
              "leading_generators_checked": 15,
              "method": "dense coefficients; inverse-free character computation; cross-multiplied certificates; Frobenius/gcd irreducibility; direct quadratic-algebra orders; cyclotomic Laurent whole-trace reconstruction",
              "limits": "only the stated finite character filters; no original realization or multiplicity exclusion"}
    OUTPUT.mkdir(parents=True, exist_ok=True)
    destination = OUTPUT / "independent_verification.json"
    partial = destination.with_suffix(".json.partial")
    partial.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    partial.replace(destination)
    print(json.dumps({"status": result["status"], "cases": checked_cases,
                      "candidate_certificates_checked": 128, "factor_rows": len(factor_checks),
                      "B_controls": 32, "theta_controls": 15, "leading_generators": 15,
                      "output": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
