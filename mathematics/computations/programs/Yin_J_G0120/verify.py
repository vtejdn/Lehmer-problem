"""Check the sixteen divided whole-order rows using coefficient sets.

This verifier does not import main.py or use its polynomial Euclidean inverse.
Both programs were authored by the same contributor; independent code paths do
not constitute independent agent review.
"""

import argparse
import json
from pathlib import Path


def decode(value):
    return {i for i in range(value.bit_length()) if (value >> i) & 1}


def encode(value):
    return sum(1 << i for i in value)


def raw_product(a, b):
    result = set()
    for i in a:
        for j in b:
            result.symmetric_difference_update({i + j})
    return result


def reduce(value, modulus):
    result = set(value)
    degree = max(modulus)
    while result and max(result) >= degree:
        shift = max(result) - degree
        result.symmetric_difference_update({i + shift for i in modulus})
    return result


def product(a, b, modulus):
    return reduce(raw_product(a, b), modulus)


def exponent(a, n, modulus):
    result = {0}
    for _ in range(n):
        result = product(result, a, modulus)
    return result


def reciprocal_by_linear_system(a, modulus):
    dimension = max(modulus)
    basis = {}
    for j in range(dimension):
        column, solution = product(a, {j}, modulus), {j}
        while column:
            pivot = max(column)
            if pivot not in basis:
                basis[pivot] = (column, solution)
                break
            column = column ^ basis[pivot][0]
            solution = solution ^ basis[pivot][1]
        if not column:
            raise ValueError("Multiplication by the stated unit is singular")
    column, solution = {0}, set()
    while column:
        pivot = max(column)
        if pivot not in basis:
            raise ValueError("No inverse exists")
        column = column ^ basis[pivot][0]
        solution = solution ^ basis[pivot][1]
    assert product(a, solution, modulus) == {0}
    return solution


def derivative(a):
    return {i - 1 for i in a if i % 2 == 1}


def compose(a, b, modulus):
    result = set()
    for j in a:
        result = result ^ exponent(b, j, modulus)
    return result


def matrix_product(a, b, modulus):
    return [[product(a[i][0], b[0][j], modulus)
             ^ product(a[i][1], b[1][j], modulus)
             for j in range(2)] for i in range(2)]


def divide_by_phi(value):
    remaining = set(value)
    result = set()
    while remaining and max(remaining) >= 2:
        shift = max(remaining) - 2
        result.symmetric_difference_update({shift})
        remaining.symmetric_difference_update({shift, shift + 1, shift + 2})
    return result, remaining


def check(data):
    phi = {0, 1, 2}
    modulus = {4, 12, 20}
    predivision = raw_product(modulus, phi)
    fixed = {"field": "F_2", "phi": 7, "modulus": encode(modulus),
             "predivision_modulus": encode(predivision), "dimension": 20,
             "predivision_dimension": 22, "odd_order_period": 160,
             "functional_coefficients": [13, 15],
             "result": "all_sixteen_divided_rows_have_character_zero"}
    assert all(data[k] == v for k, v in fixed.items())
    assert set(data) == set(fixed) | {"recurrence_matrix_power80", "rows", "order25_Psi"}
    assert not derivative(modulus)
    matrix = [[{0}, set()], [set(), {0}]]
    recurrence = [[{1}, {0}], [{0}, set()]]
    for _ in range(80):
        matrix = matrix_product(matrix, recurrence, predivision)
    assert matrix == [[{0}, set()], [set(), {0}]]
    assert data["recurrence_matrix_power80"] == [[encode(v) for v in row] for row in matrix]
    earlier, current = {0}, {0, 1}
    values = {1: earlier, 3: current}
    for j in range(2, 80):
        earlier, current = current, product({1}, current, predivision) ^ earlier
        values[2 * j + 1] = current
    expected_orders = list(range(5, 160, 10))
    assert [row["n"] for row in data["rows"]] == expected_orders
    chi = product({1}, exponent(phi, 2, modulus), modulus)
    psi = product(chi, chi, modulus) ^ chi ^ {0}
    assert data["order25_Psi"] == encode(psi)
    for row in data["rows"]:
        value, residue = divide_by_phi(values[row["n"]])
        assert not residue and max(value) < 20
        assert raw_product(value, phi) == values[row["n"]]
        inverse = reciprocal_by_linear_system(value, modulus)
        dlog = product(derivative(value), inverse, modulus)
        if row["n"] == 25:
            assert value == psi
        expected = {"n": row["n"], "B_predivision": encode(values[row["n"]]),
                    "D": encode(value), "division_remainder": 0,
                    "inverse": encode(inverse), "dlog": encode(dlog),
                    "character": len(dlog & {13, 15}) % 2}
        assert row == expected and expected["character"] == 0
    return {"verified": True, "row_count": 16,
            "method": "coefficient_sets_exact_division_and_multiplication_linear_systems",
            "result": "all_sixteen_divided_rows_have_character_zero"}


def default_input():
    group = Path(__file__).resolve().parent
    return group.parents[2] / "computations" / "outputs" / group.name / "certificate.json"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=default_input())
    args = parser.parse_args()
    report = check(json.loads(args.input.read_text(encoding="utf-8")))
    output = args.input.with_name("verification.json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report))
