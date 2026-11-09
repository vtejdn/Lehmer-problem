"""Complete exponent l1 ball of radius two at the fixed conductor-81 base.

This is a labelled finite traversal, not descent.  No intermediate or final
energy condition discards a label.  There are no Galois filters or restarts.
"""

from collections import Counter
from itertools import combinations, product
from math import gcd
from pathlib import Path
import json

from flint import fmpz_poly

from galois_filters import (
    moments, multiply, representative, trace_polynomials, word_polynomial,
)
from balanced_control import (
    certify_measure, energy, plus_unit, polynomial_data, quotient_square_unit,
)


def fixed_base_and_units():
    p = 81
    original, columns, exponent = representative(p, 9)
    assert exponent == 5
    base = original
    U2 = plus_unit(p, 2)
    for _ in range(6):
        base = multiply(base, U2["forward"])
    base = multiply(base, plus_unit(p, 1)["inverse"])
    base = multiply(base, quotient_square_unit(p, 3, 5)["inverse"])
    assert moments(base) == (-3, 10)
    assert energy(base) == 11 and base[0] - base[1] == -30
    units = [plus_unit(p, a) for a in range(1, 41) if gcd(a, p) == 1]
    units += [quotient_square_unit(p, 3, u) for u in (5,7,11,13,17,19,23,25)]
    units += [quotient_square_unit(p, 9, u) for u in (5,7)]
    assert len(units) == 37
    return base, units


def exponent_labels(dimension):
    yield ()
    for index in range(dimension):
        for sign in (1, -1):
            yield ((index, sign),)
    for index in range(dimension):
        for sign in (2, -2):
            yield ((index, sign),)
    for left, right in combinations(range(dimension), 2):
        for first, second in product((1, -1), repeat=2):
            yield ((left, first), (right, second))


def main():
    p = 81
    base, units = fixed_base_and_units()
    traces = trace_polynomials(p//2)
    B = fmpz_poly([1]) + sum(traces[1:], fmpz_poly())
    assert abs(int(B.resultant(word_polynomial(base, traces)))) == 32
    one_step = {
        (index, sign): multiply(base, unit["forward" if sign > 0 else "inverse"])
        for index, unit in enumerate(units) for sign in (1, -1)
    }
    labels = list(exponent_labels(len(units)))
    assert len(labels) == 2813 and len(set(labels)) == 2813
    assert Counter(sum(abs(exponent) for _, exponent in label) for label in labels) == {0:1, 1:74, 2:2738}
    targets = {(x*x+2,-4*x): x for x in range(-2,3)}
    target_energies = {x: 3*(x*x+2) - 8*x for x in range(-2,3)}
    target_rows = {x: [] for x in range(-2,3)}
    histogram = Counter()
    energy_histogram = Counter()
    records = []
    unique_words = []
    word_ids = {}
    whole_polynomials = {}
    polynomial_checks = 0
    D = B - traces[p//2]

    for label_number, label in enumerate(labels):
        if not label:
            word = base
        elif len(label) == 1:
            index, exponent = label[0]
            sign = 1 if exponent > 0 else -1
            word = one_step[index, sign]
            if abs(exponent) == 2:
                word = multiply(word, units[index]["forward" if sign > 0 else "inverse"])
        else:
            (left, first), (right, second) = label
            word = multiply(one_step[left, first], units[right]["forward" if second > 0 else "inverse"])
        if word not in word_ids:
            word_ids[word] = len(unique_words)
            unique_words.append(word)
        word_id = word_ids[word]
        K, L = moments(word)
        E, U = 3*K+2*L, word[0]-word[1]
        assert E > 0
        # Check every exact word through ordinary trace-polynomial reduction.
        h = word_polynomial(word, traces)
        C = (D * h) % B
        assert int(C[p//2-1]) == K
        assert int(C[p//2-2]) - K*int(B[p//2-1]) == L
        assert int(C(-2)) == -U*int(B(-2))
        polynomial_checks += 1
        histogram[K,L,E,U] += 1
        energy_histogram[E] += 1
        record = {
            "label_number": label_number,
            "exponents": [[units[index]["label"], exponent] for index, exponent in label],
            "word_id": word_id, "K": K, "L": L, "E": E, "U": U,
        }
        records.append(record)
        if (K,L) in targets:
            x = targets[K,L]
            target_rows[x].append(label_number)
            if (word_id,x) not in whole_polynomials:
                certificate = polynomial_data(p, word, x, B, traces, 32)
                assert certificate["P_minus_one"] == 2+2*x+U
                certificate.update(word_id=word_id, strict_endpoint=certificate["P_minus_one"] > 0)
                certify_measure(certificate)
                whole_polynomials[word_id,x] = certificate

    multiplicities = Counter(record["word_id"] for record in records)
    summary = {
        "p": p, "cut": 9, "unit_count": len(units), "exponent_l1_radius": 2,
        "labels_tested": len(records), "distinct_h": len(unique_words),
        "ordinary_polynomial_K_L_U_checks": polynomial_checks,
        "word_multiplicity_histogram": sorted(Counter(multiplicities.values()).items()),
        "minimum_energy": min(energy_histogram),
        "maximum_energy": max(energy_histogram),
        "minimum_energy_labels": [record for record in records if record["E"] == min(energy_histogram)],
        "target_energy_label_counts": {str(x): energy_histogram[value] for x,value in target_energies.items()},
        "target_energies": target_energies,
        "joint_target_label_counts": {str(x): len(rows) for x,rows in target_rows.items()},
        "joint_target_distinct_h_counts": {
            str(x): len({records[index]["word_id"] for index in rows}) for x,rows in target_rows.items()
        },
        "distinct_P": len(whole_polynomials),
        "strict_endpoint_distinct_P": sum(certificate["strict_endpoint"] for certificate in whole_polynomials.values()),
    }
    output = Path(__file__).resolve().parents[2] / "outputs" / Path(__file__).resolve().parent.name
    output.mkdir(parents=True, exist_ok=True)
    (output / "unit_ball_81.json").write_text(json.dumps({
        "summary": summary, "base_word": base, "unit_labels": [unit["label"] for unit in units],
        "labels": records, "distinct_words": unique_words,
        "joint_histogram": [[*key,count] for key,count in sorted(histogram.items())],
        "energy_histogram": sorted(energy_histogram.items()),
        "target_label_numbers": target_rows,
        "whole_polynomials": list(whole_polynomials.values()),
    },indent=2)+"\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    for certificate in whole_polynomials.values():
        print("whole polynomial", json.dumps({
            key:value for key,value in certificate.items()
            if key not in ("h_word","P_coefficients_ascending","Q_coefficients_ascending")
        }))


if __name__ == "__main__":
    main()
