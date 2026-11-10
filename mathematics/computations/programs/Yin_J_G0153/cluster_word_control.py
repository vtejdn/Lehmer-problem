"""One exact 24-cluster scope control, with its complete Mahler certificate.

The fixed matrix word is C889 v2 equation (27), at g=72.
The input is generated twice: from its exact polynomial trace, and from the
original integral rotating-shear matrix. No numerical screen or sampling is used.
"""

import importlib.util
import json
from math import comb
from pathlib import Path
import platform
import time

import flint
from flint import fmpz_mat, fmpz_poly


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name / "cluster_word_control.json"
EVALUATOR = HERE.parent / "Yin_J_G0156" / "sampler.py"
GENUS = 72
RUNS = ((1, 1), (-1, 1), (1, 2), (-1, 7), (1, 5), (-1, 4), (1, 4))


def multiply(first, second):
    return [[sum((first[i][k] * second[k][j] for k in range(2)),
                 fmpz_poly([0])) for j in range(2)] for i in range(2)]


def trace_input(matrix_word):
    t = fmpz_poly([0, 1])
    one, zero = fmpz_poly([1]), fmpz_poly([0])
    product = [[one, zero], [zero, one]]
    for sign in matrix_word:
        letter = [[t*t - 3, sign*(2-t)], [-sign*(2+t), one]]
        assert letter[0][0]*letter[1][1] - letter[0][1]*letter[1][0] == one
        product = multiply(product, letter)
    trace = product[0][0] + product[1][1]
    assert trace(2) == 2
    assert trace % (t*t - 3) == fmpz_poly([-2])
    coefficients = [0] * (2*GENUS + 1)
    coefficients[0] = coefficients[-1] = 1
    for power, coefficient in enumerate(trace):
        for choice in range(power + 1):
            exponent = GENUS + power - 2*choice
            assert 0 < exponent < 2*GENUS
            coefficients[exponent] -= int(coefficient) * comb(power, choice)
    return trace, fmpz_poly(coefficients)


def original_matrix(physical_word):
    first = [[0]*GENUS for _ in range(GENUS)]
    second = [[0]*GENUS for _ in range(GENUS)]
    sites, epsilon, eta = [], [], []
    for cluster, sign in enumerate(physical_word):
        for offset, first_sign, second_sign in ((0, sign, -sign), (1, sign, sign)):
            site = 3*cluster + offset
            following = (site + 1) % GENUS
            sites.append(site)
            epsilon.append(first_sign)
            eta.append(second_sign)
            first[site][site] += first_sign
            first[following][following] += first_sign
            first[site][following] -= first_sign
            first[following][site] -= first_sign
            second[site][site] += second_sign
            second[following][following] += second_sign
            second[site][following] += second_sign
            second[following][site] += second_sign
    assert len(sites) == 48 and len(set(sites)) == 48
    assert sum(epsilon) == sum(eta) == 0
    d, e = fmpz_mat(first), fmpz_mat(second)
    assert d.transpose() == d and e.transpose() == e
    de = d*e
    matrix = fmpz_mat(2*GENUS, 2*GENUS)
    for row in range(GENUS):
        source = (row - 1) % GENUS
        for column in range(GENUS):
            unit = int(source == column)
            matrix[row, column] = de[source, column] + unit
            matrix[row, GENUS + column] = d[source, column]
            matrix[GENUS + row, column] = e[source, column]
            matrix[GENUS + row, GENUS + column] = unit
    return matrix, {"sites_zero_based": sites, "epsilon": epsilon, "eta": eta}


def main():
    started = time.monotonic()
    matrix_word = [sign for sign, count in RUNS for _ in range(count)]
    assert len(matrix_word) == 24 and sum(matrix_word) == 0
    physical_word = matrix_word[::-1]
    trace, polynomial = trace_input(matrix_word)
    matrix, original_input = original_matrix(physical_word)
    assert matrix.charpoly() == polynomial
    coefficients = [int(value) for value in polynomial]
    assert polynomial.degree() == 2*GENUS
    assert coefficients == coefficients[::-1]
    assert coefficients[0] == coefficients[-1] == 1
    specification = importlib.util.spec_from_file_location("j156_cluster_measure", EVALUATOR)
    evaluator = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(evaluator)
    certificate = evaluator.certify_polynomial(coefficients)
    assert certificate["root_count_with_multiplicity"] == 2*GENUS
    result = {
        "python_version": platform.python_version(),
        "python_flint_version": flint.__version__,
        "genus": GENUS,
        "matrix_word_runs_left_to_right": RUNS,
        "physical_cluster_signs_in_cyclic_order": physical_word,
        "original_input": original_input,
        "trace_coefficients_ascending": [int(value) for value in trace],
        "exact_controls": {
            "trace_at_2": 2,
            "trace_remainder_mod_t2_minus_3": [-2],
            "original_matrix_charpoly_matches_trace_lift": True,
            "balanced_sign_vectors": True,
        },
        "certificate": certificate,
        "elapsed_seconds": time.monotonic() - started,
        "scope": "One fixed globally balanced 24-cluster input at g=72; no family exclusion.",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    temporary.replace(OUTPUT)
    print(json.dumps({
        "degree": polynomial.degree(),
        "trace_degree": trace.degree(),
        "measure_ball": certificate["measure_ball"],
        "target_6_5": certificate["thresholds"]["6/5"],
        "neutral": certificate["neutral"],
        "factor_degrees": [[row["degree"], row["exponent"], row["cyclotomic"]]
                           for row in certificate["factors"]],
        "elapsed_seconds": result["elapsed_seconds"],
    }, indent=2))


if __name__ == "__main__":
    main()
