"""Produce the sixteen exact divided whole-order rows over F_2."""

import argparse
import json
from pathlib import Path


def remainder(a, modulus):
    while a.bit_length() >= modulus.bit_length():
        a ^= modulus << (a.bit_length() - modulus.bit_length())
    return a


def multiply(a, b, modulus):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a.bit_length() >= modulus.bit_length():
            a ^= modulus
    return result


def power(a, exponent, modulus):
    result = 1
    while exponent:
        if exponent & 1:
            result = multiply(result, a, modulus)
        a = multiply(a, a, modulus)
        exponent >>= 1
    return result


def inverse(a, modulus):
    u, v, x, y = a, modulus, 1, 0
    while u != 1:
        if not u:
            raise ValueError("The required polynomial is not a unit")
        shift = u.bit_length() - v.bit_length()
        if shift < 0:
            u, v, x, y = v, u, y, x
            shift = -shift
        u ^= v << shift
        x ^= y << shift
    result = remainder(x, modulus)
    assert multiply(a, result, modulus) == 1
    return result


def derivative(a):
    result = 0
    for j in range(1, a.bit_length(), 2):
        result ^= ((a >> j) & 1) << (j - 1)
    return result


def compose(a, b, modulus):
    result = 0
    for j in reversed(range(a.bit_length())):
        result = multiply(result, b, modulus) ^ ((a >> j) & 1)
    return result


def matrix_multiply(a, b, modulus):
    return [[multiply(a[i][0], b[0][j], modulus)
             ^ multiply(a[i][1], b[1][j], modulus)
             for j in range(2)] for i in range(2)]


def matrix_power(a, exponent, modulus):
    result = [[1, 0], [0, 1]]
    for _ in range(exponent):
        result = matrix_multiply(result, a, modulus)
    return result


def character(value):
    return ((value >> 13) ^ (value >> 15)) & 1


def quotient(a, divisor):
    q = 0
    while a.bit_length() >= divisor.bit_length():
        shift = a.bit_length() - divisor.bit_length()
        q ^= 1 << shift
        a ^= divisor << shift
    return q, a


def certificate():
    phi = 7
    modulus = (1 << 20) | (1 << 12) | (1 << 4)
    predivision = (modulus << 2) ^ (modulus << 1) ^ modulus
    assert derivative(modulus) == 0
    assert predivision.bit_length() - 1 == 22
    matrix = matrix_power([[2, 1], [1, 0]], 80, predivision)
    assert matrix == [[1, 0], [0, 1]]
    previous, current = 1, 3
    trace = {1: previous, 3: current}
    for j in range(2, 80):
        previous, current = current, multiply(2, current, predivision) ^ previous
        trace[2 * j + 1] = current
    chi = multiply(2, power(phi, 2, modulus), modulus)
    psi = multiply(chi, chi, modulus) ^ chi ^ 1
    rows = []
    for n in range(5, 160, 10):
        value, residue = quotient(trace[n], phi)
        assert residue == 0 and value.bit_length() <= 20
        assert ((value << 2) ^ (value << 1) ^ value) == trace[n]
        reciprocal = inverse(value, modulus)
        dlog = multiply(derivative(value), reciprocal, modulus)
        assert character(dlog) == 0
        if n == 25:
            assert value == psi
        rows.append({"n": n, "B_predivision": trace[n], "D": value,
                     "division_remainder": residue, "inverse": reciprocal,
                     "dlog": dlog, "character": 0})
    return {"field": "F_2", "phi": phi, "modulus": modulus,
            "predivision_modulus": predivision, "dimension": 20,
            "predivision_dimension": 22, "odd_order_period": 160,
            "recurrence_matrix_power80": matrix, "functional_coefficients": [13, 15],
            "order25_Psi": psi, "rows": rows,
            "result": "all_sixteen_divided_rows_have_character_zero"}


def default_output():
    group = Path(__file__).resolve().parent
    return group.parents[2] / "computations" / "outputs" / group.name / "certificate.json"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    data = certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "rows": len(data["rows"]),
                      "result": data["result"]}))
