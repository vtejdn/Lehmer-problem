"""Exact factorization and full Mahler measure of one fixed failed-endpoint P.

The only input is the half-coefficient list retained in
energy_six.md#single-candidate.  No search or generated input is used.
"""

import json
from pathlib import Path
from time import monotonic

from flint import arb, ctx, fmpq, fmpz_poly

from galois_filters import moments, trace_polynomials, twice_inverse, word_polynomial
from nonsquare_control import polynomial_word


HALF_COEFFICIENTS = (
    1, 1, 4, 4, 4, 7, 5, 9, 8, 10, 10, 11, 11, 13, 11, 15,
    12, 16, 15, 17, 17, 20, 18, 24, 19, 25, 22, 25, 24, 26, 24, 28,
    24, 30, 26, 30, 29, 32, 30, 35, 30, 36,
)
PRECISION = 512


def reconstruct():
    """Recover Q, C and h and verify the fixed candidate's original constraints."""
    assert len(HALF_COEFFICIENTS) == 42
    coefficients = HALF_COEFFICIENTS + HALF_COEFFICIENTS[-2::-1]
    assert len(coefficients) == 83 and coefficients == coefficients[::-1]
    P = fmpz_poly(list(coefficients))
    assert P.degree() == 82 and P[0] == P[82] == 1 and int(P(-1)) == -104
    traces = trace_polynomials(41)
    t = traces[1]
    Q = fmpz_poly([coefficients[41]]) + sum(
        (coefficients[41 + j] * traces[j] for j in range(1, 42)), fmpz_poly())
    z = fmpz_poly([0, 1])
    lifted = sum((Q[j] * z**(41-j) * (1+z*z)**j for j in range(42)), fmpz_poly())
    assert lifted == P and Q.degree() == 41 and Q[41] == 1
    B = fmpz_poly([1]) + sum(traces[1:41], fmpz_poly())
    C = Q - t * B
    assert C.degree() == 39
    K = int(C[39])
    L = int(C[38] - B[39] * K)
    assert (K, L) == (2, 0)
    signed_resultant = int(B.resultant(Q))
    assert abs(signed_resultant) == 5216
    assert -int(Q(-2)) == int(P(-1)) == -104

    twice_inverse_T40 = twice_inverse(81, 40)
    assert all(value % 2 == 0 for value in twice_inverse_T40)
    inverse_D = -word_polynomial(tuple(value // 2 for value in twice_inverse_T40), traces[:41])
    D = B - traces[40]
    assert (D * inverse_D) % B == 1
    h = (C * inverse_D) % B
    word = polynomial_word(h, 81)
    assert word_polynomial(word, traces[:41]) == h
    assert moments(word) == (2, 0)
    assert (D * h) % B == C and abs(int(B.resultant(h))) == 5216
    assert word[0] - word[1] == -106
    for index in range(1, 41):
        node = 2 * arb.cos_pi_fmpq(fmpq(2 * index, 81))
        value = h(node)
        assert value > 0 if index <= 31 else value < 0
    return P, {
        "p": 81, "cut": 9, "x": 0, "K": K, "L": L, "E": 6,
        "P_coefficients_ascending": list(coefficients),
        "Q_coefficients_ascending": list(map(int, Q)),
        "C_coefficients_ascending": list(map(int, C)),
        "h_coefficients_ascending": list(map(int, h)), "h_word": word,
        "signed_resultant_B_Q": signed_resultant, "absolute_resultant": 5216,
        "endpoint_U": -106, "P_minus_one": -104,
        "strict_original_signs": True, "strict_endpoint": False,
    }


def factor_measure(factor):
    """Enclose max(1,|root|) for every root, keeping exact cyclotomic measure."""
    cyclotomic = bool(factor.is_cyclotomic())
    root_product = arb(abs(int(factor[factor.degree()])))
    root_records = []
    counts = {"inside": 0, "outside": 0, "unit_modulus_unresolved": 0}
    for root, multiplicity in factor.complex_roots():
        modulus = abs(root)
        if modulus < 1:
            contribution, region = arb(1), "inside"
        elif modulus > 1:
            contribution, region = modulus, "outside"
        else:
            contribution, region = arb(1).union(modulus), "unit_modulus_unresolved"
        counts[region] += multiplicity
        root_product *= contribution**multiplicity
        root_records.append({
            "root_ball": str(root), "modulus_ball": str(modulus),
            "contribution_ball": str(contribution),
            "multiplicity": multiplicity, "region": region,
        })
    assert sum(counts.values()) == factor.degree()
    assert root_product.rad() < arb("1e-40")
    if cyclotomic:
        assert factor[factor.degree()] == 1
        assert not (root_product < 1 or root_product > 1)
        measure = arb(1)
    else:
        measure = root_product
    return measure, {
        "coefficients_ascending": list(map(int, factor)),
        "degree": factor.degree(), "cyclotomic": cyclotomic,
        "root_count": sum(counts.values()), "root_regions": counts,
        "roots": root_records, "root_product_ball": str(root_product),
        "measure_ball": str(measure), "log_measure_ball": str(measure.log()),
    }


def main():
    ctx.prec = PRECISION
    P, binding = reconstruct()
    start = monotonic()
    content, factors = P.factor()
    product = fmpz_poly([content])
    for factor, exponent in factors:
        product *= factor**exponent
    assert product == P and int(content) == 1
    assert sum(factor.degree() * exponent for factor, exponent in factors) == 82
    print("Exact factors", [(factor.degree(), int(exponent), str(factor))
                            for factor, exponent in factors], flush=True)

    measure = arb(abs(int(content)))
    total_roots = 0
    regions = {"inside": 0, "outside": 0, "unit_modulus_unresolved": 0}
    records = []
    for factor, exponent in factors:
        factor_start = monotonic()
        factor_ball, record = factor_measure(factor)
        record["exponent"] = int(exponent)
        record["root_seconds"] = monotonic() - factor_start
        measure *= factor_ball**exponent
        total_roots += record["root_count"] * exponent
        for region, count in record["root_regions"].items():
            regions[region] += count * exponent
        records.append(record)
        print("Factor measure", factor.degree(), exponent, record["cyclotomic"],
              record["measure_ball"], flush=True)
    assert total_roots == 82 and sum(regions.values()) == 82
    assert measure.rad() < arb("1e-40") and measure > 1
    lower = "3.72242552293746802492690401570893"
    upper = "3.72242552293746802492690401570894"
    assert arb(lower) < measure < arb(upper)
    result = {
        "binding": binding, "precision_bits": PRECISION,
        "factor_content": int(content), "factorization_verified": True,
        "factors": records, "root_count_with_multiplicity": total_roots,
        "root_regions_with_multiplicity": regions,
        "measure_ball": str(measure), "log_measure_ball": str(measure.log()),
        "certified_decimal_lower": lower, "certified_decimal_upper": upper,
        "strict_positive_measure": bool(measure > 1),
        "strict_endpoint": False, "diagnostic_only": True,
        "factorization_and_root_seconds": monotonic() - start,
    }
    source = Path(__file__).resolve()
    output = source.parents[2] / "outputs" / source.parent.name
    output.mkdir(parents=True, exist_ok=True)
    (output / "candidate_diagnostic_82.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "root_count_with_multiplicity", "root_regions_with_multiplicity",
        "measure_ball", "log_measure_ball", "strict_endpoint",
        "factorization_and_root_seconds")}), flush=True)


if __name__ == "__main__":
    main()
