"""Signed layer norms and two rectified positive nonsquare inputs at p=81.

This is an arithmetic supply certificate, not a small-Mahler-measure search.
Existing J154 programs are imported for exact cyclic arithmetic only.
"""

import json
from math import gcd
from pathlib import Path

from flint import arb, ctx, fmpq, fmpz_poly

from galois_filters import (
    moments, multiply, normalize, representative, trace_polynomials,
    trace_word, twice_inverse, word_polynomial,
)


TRACE = fmpz_poly([3, 4, -5, -5, 1, 1])


def signed_layer_norms(count=8):
    # F_l=1+T_(3^(l-1)) has odd degree, as does TRACE.
    # Reducing F_l modulo TRACE preserves Res(TRACE,F_l), not the
    # swapped-order sign. Hence the signed layer norm is its negative.
    reduced_trace = fmpz_poly([0, 1])
    direct_trace = fmpz_poly([0, 1])
    records = []
    for layer in range(1, count + 1):
        value = -int(TRACE.resultant(1 + reduced_trace))
        if layer <= 4:
            assert int((1 + direct_trace).resultant(TRACE)) == value
            direct_trace = direct_trace**3 - 3 * direct_trace
        records.append({"layer": layer, "order": 3**layer,
                        "signed_norm": value, "negative_parity": int(value < 0)})
        reduced_trace = (reduced_trace**3 - 3 * reduced_trace) % TRACE
    assert [item["signed_norm"] for item in records[:5]] == [-1, -1, -1, -163, -19100773]
    assert [item["negative_parity"] for item in records] == [1, 1, 1, 1, 1, 0, 1, 0]
    return records


def integral_half(word):
    assert all(value % 2 == 0 for value in word)
    return tuple(value // 2 for value in word)


def signed_quotient(p, column):
    scale = 1
    while column % (3 * scale) == 0:
        scale *= 3
    forward = integral_half(multiply(trace_word(p, column), twice_inverse(p, scale)))
    inverse = integral_half(multiply(trace_word(p, scale), twice_inverse(p, column)))
    assert multiply(forward, inverse) == (1,) + (0,) * (p - 1)
    return scale, forward, inverse


def sign_cosine(p, index):
    residue = index % p
    return int(p < 4 * residue < 3 * p)


def rectifier(p, target_signs):
    n = p // 2
    one = (1,) + (0,) * (p - 1)
    columns = [{"label": "-1", "signs": [1] * n,
                "forward": tuple(-value for value in one),
                "inverse": tuple(-value for value in one)}]
    for column in range(1, n + 1):
        scale = 1
        while column % (3 * scale) == 0:
            scale *= 3
        if column == scale:
            continue
        _, forward, inverse = signed_quotient(p, column)
        columns.append({"label": f"T{column}/T{scale}",
                        "signs": [sign_cosine(p, j * column) ^ sign_cosine(p, j * scale)
                                  for j in range(1, n + 1)],
                        "forward": forward, "inverse": inverse})

    width = len(columns)
    rows = [sum(column["signs"][j] << i for i, column in enumerate(columns))
            | (target_signs[j] << width) for j in range(n)]
    pivot_row = 0
    pivots = []
    for column in range(width):
        source = next((i for i in range(pivot_row, n) if (rows[i] >> column) & 1), None)
        if source is None:
            continue
        rows[pivot_row], rows[source] = rows[source], rows[pivot_row]
        for i in range(n):
            if i != pivot_row and (rows[i] >> column) & 1:
                rows[i] ^= rows[pivot_row]
        pivots.append(column)
        pivot_row += 1
    assert all(row == 0 for row in rows[pivot_row:]), "signature outside the unit image"
    selected = [column for i, column in enumerate(pivots) if (rows[i] >> width) & 1]
    result, inverse = one, one
    signature = [0] * n
    for index in selected:
        column = columns[index]
        result = multiply(result, column["forward"])
        inverse = multiply(inverse, column["inverse"])
        signature = [a ^ b for a, b in zip(signature, column["signs"])]
    assert signature == target_signs
    assert multiply(result, inverse) == one
    return result, inverse, {"rank": len(pivots), "column_count": width,
                             "selected_columns": [columns[index]["label"] for index in selected]}


def filter_word(p, index):
    result = [0] * p
    result[0] = -1
    for degree, coefficient in ((5, 1), (4, 1), (2, -1), (1, -1)):
        result[(degree * index) % p] += coefficient
        result[(-degree * index) % p] += coefficient
    return normalize(result)


def evaluate_mod(polynomial, value, modulus):
    result = 0
    for coefficient in reversed(list(polynomial)):
        result = (result * value + int(coefficient)) % modulus
    return result


def nonsquare_witness(polynomial, B, p=81, prime=163):
    beta = next(value for value in range(2, prime)
                if pow(value, p, prime) == 1 and pow(value, p // 3, prime) != 1)
    correction = (-((beta**p - 1) // prime)
                  * pow((p * pow(beta, p - 1, prime)) % prime, -1, prime)) % prime
    modulus = prime**2
    lifted = beta + prime * correction
    assert pow(lifted, p, modulus) == 1
    witnesses = []
    for index in range(1, p // 2 + 1):
        if gcd(index, p) != 1:
            continue
        node = (pow(lifted, index, modulus) + pow(lifted, -index, modulus)) % modulus
        assert evaluate_mod(B, node, modulus) == 0
        value = evaluate_mod(polynomial, node, modulus)
        if value % prime == 0:
            assert value != 0
            witnesses.append({"primitive_index": index, "node_mod_prime_squared": node,
                              "value_mod_prime_squared": value})
    assert witnesses
    return {"prime": prime, "modulus": modulus, "primitive_root": beta,
            "lifted_root": lifted, "odd_valuation_witnesses": witnesses}


def balanced_base(p=81):
    # The existing balanced control's exact net word, without rerunning descent.
    base, _, _ = representative(p, 9)
    one = (1,) + (0,) * (p - 1)
    inverse_U1_root = integral_half(twice_inverse(p, (p + 1) // 2))
    inverse_U1 = multiply(inverse_U1_root, inverse_U1_root)
    U2 = multiply(trace_word(p, 1), trace_word(p, 1))
    _, _, inverse_J5T3 = signed_quotient(p, 15)
    correction = one
    for _ in range(6):
        correction = multiply(correction, U2)
    correction = multiply(correction, inverse_U1)
    correction = multiply(correction, multiply(inverse_J5T3, inverse_J5T3))
    result = multiply(base, correction)
    assert moments(result) == (-3, 10)
    return result


def construct(indices):
    p, n = 81, 40
    ctx.prec = 512
    traces = trace_polynomials(n)
    B = fmpz_poly([1]) + sum(traces[1:], fmpz_poly())
    nodes = [2 * arb.cos_pi_fmpq(fmpq(2 * j, p)) for j in range(1, n + 1)]
    raw = (1,) + (0,) * (p - 1)
    for index in indices:
        raw = multiply(raw, filter_word(p, index))
    raw_polynomial = word_polynomial(raw, traces)
    signs = []
    for node in nodes:
        value = raw_polynomial(node)
        assert value > 0 or value < 0
        signs.append(int(value < 0))
    q, inverse_q, rectification = rectifier(p, signs)
    positive = multiply(q, raw)
    q_polynomial = word_polynomial(q, traces)
    positive_polynomial = word_polynomial(positive, traces)
    assert abs(int(B.resultant(q_polynomial))) == 1
    assert abs(int(B.resultant(positive_polynomial))) == 163 ** len(indices)
    assert all(positive_polynomial(node) > 0 for node in nodes)

    base = balanced_base(p)
    base_polynomial = word_polynomial(base, traces)
    assert abs(int(B.resultant(base_polynomial))) == 32
    supplied = multiply(base, positive)
    supplied_polynomial = word_polynomial(supplied, traces)
    norm = abs(int(B.resultant(supplied_polynomial)))
    assert norm == 32 * 163 ** len(indices)
    for index, node in enumerate(nodes, 1):
        value = supplied_polynomial(node)
        assert value > 0 if index <= n - 9 else value < 0
    K, L = moments(supplied)
    endpoint_U = supplied[0] - supplied[1]
    targets = {(x*x + 2, -4*x): x for x in range(-2, 3)}
    return {"p": p, "cut": 9, "filter_indices": indices,
            "rectification": rectification, "rectifier_word": q,
            "inverse_rectifier_word": inverse_q, "positive_multiplier_word": positive,
            "multiplier_norm": 163 ** len(indices),
            "nonsquare_certificate": nonsquare_witness(positive_polynomial, B),
            "input_word": supplied, "input_norm": norm, "K_L": [K, L],
            "energy_2L_plus_3K": 2*L + 3*K,
            "endpoint_U": endpoint_U,
            "P_minus_one_by_x": {str(x): 2 + 2*x + endpoint_U for x in range(-2, 3)},
            "joint_target": targets.get((K, L)),
            "whole_measure_computed": False}


def main():
    result = {"signed_layers": signed_layer_norms(),
              "constructions": [construct([1]), construct([1, 2])]}
    output = Path(__file__).resolve().parents[2] / "outputs" / "Yin_J_G0154"
    output.mkdir(parents=True, exist_ok=True)
    (output / "signed_filters.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"signed_layers": result["signed_layers"],
                      "constructions": [{key: item[key] for key in (
                          "filter_indices", "rectification", "multiplier_norm",
                          "input_norm", "K_L", "energy_2L_plus_3K", "joint_target",
                          "nonsquare_certificate")}
                                        for item in result["constructions"]]}, indent=2))


if __name__ == "__main__":
    main()
