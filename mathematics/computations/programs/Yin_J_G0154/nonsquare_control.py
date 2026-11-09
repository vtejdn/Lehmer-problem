"""The p=81 single Lehmer-filter nonsquare class, with a bounded E<=2 scan.

Reconstruct h_new=h_* q V_1 from signed_filters.construct([1]), without
loading generated data.  Traverse all integer square multipliers modulo
simultaneous negation, or explicitly report the fixed traversal boundary.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
from time import monotonic
import json

from flint import fmpz_mat, fmpz_poly

from balanced_control import certify_measure, polynomial_data
from galois_filters import normalize, trace_polynomials, word_polynomial
from low_energy_shell import (
    EnumerationLimit, identity, jacobi, multiply_matrix, quadratic_value,
    root_poly, separator_certificate, upper_pivots,
)
from signed_filters import construct
from two_energy_shell import (
    MAXIMUM_ENERGY, MAXIMUM_NODES, MAXIMUM_SECONDS, half_ball,
)


TARGETS = {(1, 3): 1, (2, 6): 2}
BASE_NORM = 5216


def traversal_controls():
    """Compare the imported recurrence with three small direct integer scans."""
    records = []
    for values in ([[1, 0], [0, 1]], [[2, 1], [1, 2]], [[1, 1], [1, 2]]):
        state = {"nodes": 0, "started": monotonic()}
        actual = set(half_ball(upper_pivots(fmpz_mat(values)), state))
        expected = set()
        for vector in product(range(-3, 4), repeat=2):
            if not any(vector) or next(x for x in reversed(vector) if x) < 0:
                continue
            energy = sum(vector[i] * values[i][j] * vector[j]
                         for i in range(2) for j in range(2))
            if 0 < energy <= 2:
                expected.add((vector, energy))
        assert actual == expected
        records.append({"gram": values, "half_ball": sorted(actual)})
    return records


def polynomial_word(polynomial, p):
    """Evaluate an ordinary polynomial at z+z^-1 by integer cyclic Horner."""
    word = [0] * p
    for coefficient in reversed(list(polynomial)):
        word = [word[(i - 1) % p] + word[(i + 1) % p] for i in range(p)]
        word[0] += int(coefficient)
    return normalize(word)


def lll_certificate(rows):
    """Check exact size reduction and the standard delta=3/4 Lovasz bound."""
    maximum_mu = Fraction(0)
    for i, row in enumerate(rows):
        for entry in row[1:]:
            mu = Fraction(entry, row[0])
            maximum_mu = max(maximum_mu, abs(mu))
            assert abs(mu) <= Fraction(51, 100)
        if i:
            current_norm = Fraction(row[0], rows[i - 1][0])
            previous_norm = Fraction(rows[i - 1][0], rows[i - 2][0] if i > 1 else 1)
            mu = Fraction(rows[i - 1][1], rows[i - 1][0])
            assert current_norm >= (Fraction(3, 4) - mu**2) * previous_norm
    return {"delta_checked": "3/4", "eta_checked": "51/100",
            "maximum_absolute_mu": str(maximum_mu)}


def inspect_hit(vector, original, energy, first, second, h_base, B, traces):
    root = root_poly(original.entries(), traces[1])
    root_resultant = int(B.resultant(root))
    record = {
        "x": TARGETS[(energy, first)], "energy": energy, "K": first, "L": second,
        "reduced_vector": vector,
        "basis_vector": list(map(int, original.entries())),
        "v_coefficients_ascending": list(map(int, root)),
        "root_resultant": root_resultant,
        "root_is_unit": abs(root_resultant) == 1,
        "strict_original_signs": root_resultant != 0,
        "whole_measure_computed": False,
    }
    if root_resultant == 0:
        return record
    h = (h_base * root**2) % B
    word = polynomial_word(h, 81)
    assert word_polynomial(word, traces) == h
    data = polynomial_data(81, word, record["x"], B, traces,
                           BASE_NORM * root_resultant**2)
    record.update(data)
    record["strict_endpoint"] = data["P_minus_one"] > 0
    if record["strict_endpoint"]:
        certify_measure(record)
        record["whole_measure_computed"] = True
    return record


def matrix_list(matrix):
    return [[int(value) for value in row] for row in matrix.tolist()]


def main():
    assert (MAXIMUM_ENERGY, MAXIMUM_NODES, MAXIMUM_SECONDS) == (2, 5_000_000, 120)
    controls = traversal_controls()
    p, cut, dimension = 81, 9, 40
    assert separator_certificate(p, cut, Fraction(-3, 2)) == 31
    # This rechecks the integral inverse of q, all 40 multiplier signs with
    # 512-bit balls, the original cut, exact norms, and the nonsquare witness.
    construction = construct([1])
    assert construction["input_norm"] == BASE_NORM
    assert construction["multiplier_norm"] == 163
    traces = trace_polynomials(dimension)
    B = fmpz_poly([1]) + sum(traces[1:], fmpz_poly())
    h_base = word_polynomial(construction["input_word"], traces)
    q = word_polynomial(construction["rectifier_word"], traces)
    inverse_q = word_polynomial(construction["inverse_rectifier_word"], traces)
    assert (q * inverse_q) % B == 1
    assert abs(int(B.resultant(q))) == 1
    assert abs(int(B.resultant(h_base))) == BASE_NORM

    J, I = jacobi(dimension), identity(dimension)
    H = multiply_matrix(h_base, J, I)
    JH = J * H
    separator_matrix = 2 * J + 3 * I
    G = separator_matrix * H
    assert H == H.transpose() and JH == JH.transpose() and G == G.transpose()
    assert [int(H[0, 0]), int(JH[0, 0])] == construction["K_L"]
    assert int(G[0, 0]) == construction["energy_2L_plus_3K"]
    determinant_H = int(H.det())
    determinant_separator = int(separator_matrix.det())
    assert abs(determinant_H) == BASE_NORM
    original_rows = upper_pivots(G)
    determinant = int(G.det())
    assert original_rows[-1][0] == determinant
    assert determinant == determinant_separator * determinant_H
    assert determinant == 20436467236384 * 163
    reduced_gram, change = G.lll(transform=True, rep="gram", gram="exact")
    change_determinant = int(change.det())
    assert abs(change_determinant) == 1
    assert reduced_gram == change * G * change.transpose()
    rows = upper_pivots(reduced_gram)
    assert rows[-1][0] == determinant
    reduction = lll_certificate(rows)
    reduced_H = change * H * change.transpose()
    reduced_JH = change * JH * change.transpose()
    print("Certified dimension, det(H), det(G), det(change)",
          dimension, determinant_H, determinant, change_determinant, flush=True)
    print("Reduced Gram diagonal", [int(reduced_gram[i, i]) for i in range(dimension)],
          flush=True)

    counts, moment_counts = Counter(), Counter()
    leaves, hits = [], []
    state = {"nodes": 0, "started": monotonic()}
    stop_reason = "complete"
    try:
        for vector, energy in half_ball(rows, state):
            row = fmpz_mat([vector])
            assert quadratic_value(reduced_gram, row) == energy
            first = quadratic_value(reduced_H, row)
            second = quadratic_value(reduced_JH, row)
            assert energy == 3 * first + 2 * second
            counts[energy] += 1
            moment_counts[(energy, first, second)] += 1
            leaves.append({"E": energy, "K": first, "L": second,
                           "reduced_vector": vector})
            if (energy, first) in TARGETS:
                hit = inspect_hit(vector, row * change, energy, first, second,
                                  h_base, B, traces)
                hits.append(hit)
                print("Target hit", json.dumps({key: value for key, value in hit.items()
                                                if "coefficients" not in key
                                                and "vector" not in key
                                                and key != "h_word"}), flush=True)
    except EnumerationLimit as error:
        stop_reason = str(error)
    elapsed = monotonic() - state["started"]
    source = Path(__file__).resolve()
    record = {
        "p": p, "cut": cut, "dimension": dimension, "filter_indices": [1],
        "construction": construction,
        "h_base_coefficients_ascending": list(map(int, h_base)),
        "base_absolute_resultant": BASE_NORM,
        "maximum_energy": MAXIMUM_ENERGY, "maximum_nodes": MAXIMUM_NODES,
        "maximum_seconds": MAXIMUM_SECONDS,
        "time_cap_scope": "enumeration only, after construction and LLL",
        "determinant_H": determinant_H,
        "determinant_separator": determinant_separator,
        "determinant_G": determinant,
        "original_positive_pivots": [row[0] for row in original_rows],
        "determinant_change": change_determinant,
        "change_matrix": matrix_list(change),
        "reduced_gram": matrix_list(reduced_gram),
        "positive_pivots": [row[0] for row in rows],
        "lll_certificate": reduction,
        "two_dimensional_controls": controls,
        "complete": stop_reason == "complete", "stop_reason": stop_reason,
        "nodes": state["nodes"], "enumeration_seconds": elapsed,
        "half_ball_counts": {str(energy): counts[energy] for energy in (1, 2)},
        "moment_counts": [[energy, first, second, count]
                          for (energy, first, second), count in sorted(moment_counts.items())],
        "leaves": leaves, "joint_hits": hits,
        "target_counts": {str(x): sum(hit["x"] == x for hit in hits) for x in (1, 2)},
        "distinct_P_count": len({tuple(hit["P_coefficients_ascending"]) for hit in hits
                                  if "P_coefficients_ascending" in hit}),
    }
    output = source.parents[2] / "outputs" / source.parent.name
    output.mkdir(parents=True, exist_ok=True)
    (output / "nonsquare_control_81.json").write_text(
        json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: record[key] for key in (
        "complete", "stop_reason", "nodes", "enumeration_seconds",
        "half_ball_counts", "moment_counts", "target_counts", "distinct_P_count")}),
        flush=True)


if __name__ == "__main__":
    main()
