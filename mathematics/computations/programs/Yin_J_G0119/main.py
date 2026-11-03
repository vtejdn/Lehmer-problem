"""Produce the fixed 32-generator logarithmic-derivative certificate over F_2."""

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


def certificate():
    phi = 7
    primary = (1 << 16) | (1 << 8) | 1
    modulus = primary << 4
    assert derivative(modulus) == 0
    matrix = matrix_power([[2, 1], [1, 0]], 40, modulus)
    assert matrix == [[1, 0], [0, 1]]
    previous, current = 1, 3
    trace = {1: previous, 3: current}
    for j in range(2, 40):
        previous, current = current, multiply(2, current, modulus) ^ previous
        trace[2 * j + 1] = current
    rows = []
    for n in range(1, 80, 2):
        if n % 5 == 0:
            continue
        value = trace[n]
        reciprocal = inverse(value, modulus)
        logarithmic_derivative = multiply(derivative(value), reciprocal, modulus)
        assert character(logarithmic_derivative) == 0
        rows.append({"n": n, "B": value, "inverse": reciprocal,
                     "dlog": logarithmic_derivative, "character": 0})
    targets = []
    chi = multiply(2, power(phi, 2, primary), primary)
    psi = multiply(chi, chi, primary) ^ chi ^ 1
    for epsilon in (0, 1):
        local = 2 ^ (multiply(power(phi, 4, primary), power(2, 7, primary), primary)
                     if epsilon else 0)
        target = 5 ^ (multiply(local ^ 5, inverse(16, primary), primary) << 4)
        assert remainder(target, 16) == 5
        assert remainder(target, primary) == local
        h = multiply(4, local, primary)
        v = multiply(power(2, 5, primary), local, primary)
        c = multiply(4, multiply(compose(target, chi, primary),
                                power(psi, 14, primary), primary), primary)
        assert c == 4
        z = power(multiply(h, power(c, 2, primary), primary), 11, primary)
        assert power(z, 11, primary) == multiply(h, power(c, 2, primary), primary)
        correction = multiply(power(2, 4, primary),
                              multiply(power(3, 8, primary), power(phi, 4, primary), primary), primary)
        gate = multiply(z, v ^ power(c, 3, primary), primary)
        if epsilon:
            gate ^= multiply(multiply(h, v, primary), correction, primary)
        old_support = power(h, 6, primary) ^ power(c, 21, primary)
        assert gate == old_support == 0
        reciprocal = inverse(target, modulus)
        logarithmic_derivative = multiply(derivative(target), reciprocal, modulus)
        assert logarithmic_derivative == (1 << 15) | (1 << 7)
        assert character(logarithmic_derivative) == 1
        targets.append({"epsilon": epsilon, "Y": target, "Y_phi": local,
                        "inverse": reciprocal, "dlog": logarithmic_derivative,
                        "character": 1, "C": c, "Z": z,
                        "gate_remainder": gate, "old_support_remainder": old_support})
    return {"field": "F_2", "phi": phi, "modulus": modulus,
            "dimension": 20, "ambient_unit_count": 8 * 3 * 4 ** 7,
            "odd_order_period": 80, "recurrence_matrix_power40": matrix,
            "functional_coefficients": [13, 15], "generators": rows,
            "targets": targets, "result": "both_targets_separated"}


def default_output():
    group = Path(__file__).resolve().parent
    mathematics = group.parents[2]
    return mathematics / "computations" / "outputs" / group.name / "certificate.json"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    data = certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "generators": len(data["generators"]),
                      "targets": len(data["targets"]), "result": data["result"]}))
