"""Check the complete certificate using coefficient sets and linear algebra.

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


def check(data):
    phi = {0, 1, 2}
    primary = {0, 8, 16}
    modulus = {4, 12, 20}
    fixed = {"field": "F_2", "phi": 7, "modulus": encode(modulus),
             "dimension": 20, "ambient_unit_count": 393216,
             "odd_order_period": 80, "functional_coefficients": [13, 15],
             "result": "both_targets_separated"}
    assert all(data[k] == v for k, v in fixed.items())
    assert set(data) == set(fixed) | {"recurrence_matrix_power40", "generators", "targets"}
    assert not derivative(modulus)
    matrix = [[{0}, set()], [set(), {0}]]
    recurrence = [[{1}, {0}], [{0}, set()]]
    for _ in range(40):
        matrix = matrix_product(matrix, recurrence, modulus)
    assert matrix == [[{0}, set()], [set(), {0}]]
    assert data["recurrence_matrix_power40"] == [[encode(v) for v in row] for row in matrix]
    earlier, current = {0}, {0, 1}
    values = {1: earlier, 3: current}
    for j in range(2, 40):
        earlier, current = current, product({1}, current, modulus) ^ earlier
        values[2 * j + 1] = current
    expected_orders = [n for n in range(1, 80, 2) if n % 5]
    assert [row["n"] for row in data["generators"]] == expected_orders
    for row in data["generators"]:
        value = values[row["n"]]
        inverse = reciprocal_by_linear_system(value, modulus)
        dlog = product(derivative(value), inverse, modulus)
        expected = {"n": row["n"], "B": encode(value), "inverse": encode(inverse),
                    "dlog": encode(dlog), "character": len(dlog & {13, 15}) % 2}
        assert row == expected and expected["character"] == 0
    assert [row["epsilon"] for row in data["targets"]] == [0, 1]
    chi = product({1}, exponent(phi, 2, primary), primary)
    psi = product(chi, chi, primary) ^ chi ^ {0}
    for row in data["targets"]:
        epsilon = row["epsilon"]
        local = {1}
        if epsilon:
            local = local ^ product(exponent(phi, 4, primary), {7}, primary)
        inverse_x4 = reciprocal_by_linear_system({4}, primary)
        correction = product(local ^ {0, 2}, inverse_x4, primary)
        target = {0, 2} ^ {j + 4 for j in correction}
        assert reduce(target, {4}) == {0, 2} and reduce(target, primary) == local
        inverse = reciprocal_by_linear_system(target, modulus)
        dlog = product(derivative(target), inverse, modulus)
        assert dlog == {7, 15}
        h = product({2}, local, primary)
        v = product({5}, local, primary)
        c = product({2}, product(compose(target, chi, primary), exponent(psi, 14, primary), primary), primary)
        assert c == {2}
        z = exponent(product(h, exponent(c, 2, primary), primary), 11, primary)
        assert exponent(z, 11, primary) == product(h, exponent(c, 2, primary), primary)
        s = product({4}, product(exponent({0, 1}, 8, primary), exponent(phi, 4, primary), primary), primary)
        gate = product(z, v ^ exponent(c, 3, primary), primary)
        if epsilon:
            gate = gate ^ product(product(h, v, primary), s, primary)
        old_support = exponent(h, 6, primary) ^ exponent(c, 21, primary)
        assert not gate and not old_support
        expected = {"epsilon": epsilon, "Y": encode(target), "Y_phi": encode(local),
                    "inverse": encode(inverse), "dlog": encode(dlog), "character": 1,
                    "C": encode(c), "Z": encode(z), "gate_remainder": 0,
                    "old_support_remainder": 0}
        assert row == expected
    return {"verified": True, "generator_count": 32, "target_count": 2,
            "method": "coefficient_sets_and_multiplication_linear_systems",
            "result": "both_targets_separated"}


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
