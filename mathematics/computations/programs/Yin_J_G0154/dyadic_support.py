"""Exact joint moment counts modulo eight for the fixed p=81 paired input.

Fourier inversion uses exact arithmetic in Z[zeta_8], with zeta_8^4=-1.
This is a local-support computation, not an integer small-energy search.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from pathlib import Path
import json

from galois_filters import trace_polynomials, word_polynomial
from low_energy_shell import identity, jacobi, multiply_matrix, separator_certificate
from signed_filters import construct


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def scale(value, factor):
    return tuple(factor * entry for entry in value)


def multiply(left, right):
    result = [0] * 4
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            degree = i + j
            result[degree % 4] += a * b * (1 if degree < 4 else -1)
    return tuple(result)


def phase(exponent):
    exponent %= 8
    result = [0] * 4
    result[exponent % 4] = 1 if exponent < 4 else -1
    return tuple(result)


def conjugate(value):
    result = ZERO
    for i, entry in enumerate(value):
        result = add(result, scale(phase(-i), entry))
    return result


def normalized(matrix, modulus):
    return tuple(tuple(int(value) % modulus for value in row) for row in matrix)


@lru_cache(maxsize=None)
def gauss(matrix, modulus):
    """Sum zeta_8^((8/modulus)*v^T matrix v) over all v modulo modulus."""
    dimension = len(matrix)
    assert modulus in (1, 2, 4, 8)
    assert all(len(row) == dimension for row in matrix)
    assert all(matrix[i][j] == matrix[j][i]
               for i in range(dimension) for j in range(dimension))
    if dimension == 0 or modulus == 1:
        return ONE
    exponent_scale = 8 // modulus
    odd_diagonal = next((i for i in range(dimension) if matrix[i][i] % 2), None)
    if odd_diagonal is not None:
        order = [odd_diagonal] + [i for i in range(dimension) if i != odd_diagonal]
        A = [[matrix[i][j] for j in order] for i in order]
        inverse = pow(A[0][0], -1, modulus)
        rest = tuple(tuple((A[i][j] - A[i][0] * inverse * A[0][j]) % modulus
                           for j in range(1, dimension))
                     for i in range(1, dimension))
        block = ZERO
        for x in range(modulus):
            block = add(block, phase(exponent_scale * A[0][0] * x * x))
        if block == ZERO:
            return ZERO
        return multiply(block, gauss(rest, modulus))
    odd_off_diagonal = next(((i, j) for i in range(dimension)
                             for j in range(i + 1, dimension) if matrix[i][j] % 2), None)
    if odd_off_diagonal is not None:
        first, second = odd_off_diagonal
        order = [first, second] + [i for i in range(dimension) if i not in (first, second)]
        A = [[matrix[i][j] for j in order] for i in order]
        a, b, c = A[0][0], A[0][1], A[1][1]
        inverse = pow((a * c - b * b) % modulus, -1, modulus)
        rest = tuple(tuple(
            (A[i][j] - inverse * (
                A[i][0] * (c * A[0][j] - b * A[1][j])
                + A[i][1] * (-b * A[0][j] + a * A[1][j])
            )) % modulus for j in range(2, dimension))
            for i in range(2, dimension))
        block = ZERO
        for x, y in product(range(modulus), repeat=2):
            block = add(block, phase(exponent_scale * (a*x*x + 2*b*x*y + c*y*y)))
        return multiply(block, gauss(rest, modulus))
    assert all(value % 2 == 0 for row in matrix for value in row)
    half = tuple(tuple(value // 2 for value in row) for row in matrix)
    return scale(gauss(half, modulus // 2), 2**dimension)


def brute_gauss(matrix, modulus):
    result = ZERO
    for vector in product(range(modulus), repeat=len(matrix)):
        value = sum(vector[i] * matrix[i][j] * vector[j]
                    for i in range(len(matrix)) for j in range(len(matrix)))
        result = add(result, phase((8 // modulus) * value))
    return result


def local_controls():
    matrices = [
        [[1]], [[2]], [[0, 1], [1, 0]], [[2, 1], [1, 2]],
        [[2, 2], [2, 4]], [[1, 1], [1, 2]],
        [[2, 1, 0], [1, 2, 1], [0, 1, 2]],
        [[4, 0, 0], [0, 0, 4], [0, 4, 0]],
    ]
    for matrix in matrices:
        for modulus in (2, 4, 8):
            reduced = normalized(matrix, modulus)
            assert gauss(reduced, modulus) == brute_gauss(reduced, modulus)
    assert multiply(phase(1), phase(7)) == ONE
    return {"matrices": len(matrices), "moduli": [2, 4, 8], "comparisons": 24}


def main():
    controls = local_controls()
    construction = construct([1, 2])
    assert construction["p"] == 81 and construction["cut"] == 9
    assert construction["input_norm"] == 850208
    dimension = 40
    traces = trace_polynomials(dimension)
    h = word_polynomial(construction["input_word"], traces)
    J, I = jacobi(dimension), identity(dimension)
    H = multiply_matrix(h, J, I)
    JH = J * H
    assert H == H.transpose() and JH == JH.transpose()
    assert abs(int(H.det())) == 850208
    assert int(J.det()) % 2 == 1
    real_counts = [
        separator_certificate(81, 30, Fraction(4, 3)),
        separator_certificate(81, 9, Fraction(-3, 2)),
        separator_certificate(81, 11, Fraction(-4, 3)),
    ]
    assert real_counts == [10, 31, 29]
    first = normalized(H.tolist(), 8)
    second = normalized(JH.tolist(), 8)
    sums = {}
    for a, b in product(range(8), repeat=2):
        pencil = tuple(tuple((a*first[i][j] + b*second[i][j]) % 8
                             for j in range(dimension)) for i in range(dimension))
        sums[a, b] = gauss(pencil, 8)
    assert sums[0, 0] == scale(ONE, 8**dimension)
    for a, b in sums:
        assert sums[(-a) % 8, (-b) % 8] == conjugate(sums[a, b])
    counts = {}
    for K, L in product(range(8), repeat=2):
        answer = ZERO
        for (a, b), value in sums.items():
            answer = add(answer, multiply(phase(-a*K-b*L), value))
        assert answer[1:] == (0, 0, 0)
        value, remainder = divmod(answer[0], 64)
        assert remainder == 0 and value >= 0
        counts[K, L] = value
    assert sum(counts.values()) == 8**dimension
    assert Counter(counts.values()) == Counter({
        2**114 - 2**80: 4, 2**114: 56, 2**114 + 2**80: 4,
    })
    # Modulo two, a symmetric quadratic form is its diagonal linear form.
    diagonal_one = sum((first[i][i] % 2) << i for i in range(dimension))
    diagonal_two = sum((second[i][i] % 2) << i for i in range(dimension))
    assert diagonal_one and diagonal_two and diagonal_one != diagonal_two
    for parity_K, parity_L in product(range(2), repeat=2):
        total = sum(value for (K, L), value in counts.items()
                    if K % 2 == parity_K and L % 2 == parity_L)
        assert total == 2**118
    threshold = 2**86
    targets = []
    for x in range(-2, 3):
        K, L = x*x + 2, -4*x
        value = counts[K % 8, L % 8]
        assert value == 2**114 + (-1, 0, 1, 0, -1)[x+2] * 2**80
        assert value > threshold
        targets.append({"x": x, "K": K, "L": L, "count_mod_8": value,
                        "bad_parity_upper_bound": threshold,
                        "strictly_above_bound": value > threshold})
    record = {
        "p": 81, "cut": 9, "filter_indices": [1, 2], "dimension": dimension,
        "input_norm": construction["input_norm"],
        "h_coefficients_ascending": list(map(int, h)),
        "H_mod_8": first, "JH_mod_8": second,
        "local_controls": controls,
        "real_separator_counts": real_counts,
        "gauss_sums": [[a, b, *value] for (a, b), value in sorted(sums.items())],
        "joint_counts": [[K, L, value] for (K, L), value in sorted(counts.items())],
        "total_vectors": 8**dimension,
        "count_multiplicities": [[value, count] for value, count in sorted(Counter(counts.values()).items())],
        "targets": targets,
        "global_integer_count_claimed": False,
        "whole_measure_computed": False,
    }
    output = Path(__file__).resolve().parents[2] / "outputs" / "Yin_J_G0154"
    output.mkdir(parents=True, exist_ok=True)
    (output / "dyadic_support_81.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: record[key] for key in (
        "local_controls", "count_multiplicities", "targets")}, indent=2))


if __name__ == "__main__":
    main()
