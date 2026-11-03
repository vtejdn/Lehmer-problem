"""Independent exact verification of the retained C627/J118 finite inputs.

No code is imported from the author certificate or discovery programs.
Polynomial long division and signed monomial interval sums reconstruct the
quotient-ring and real-place tests independently of their implementations.
"""
from fractions import Fraction
from itertools import permutations, product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE.parents[3] / "mathematics" / "computations" / "outputs" / HERE.name
P = (1, -1, -1, -1, 1)


def reduce_polynomial(coefficients):
    result = list(coefficients) + [0] * max(0, 4 - len(coefficients))
    for degree in range(len(result) - 1, 3, -1):
        leading = result[degree]
        for j, coefficient in enumerate(P):
            result[degree - 4 + j] -= leading * coefficient
    return tuple(result[:4])


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return reduce_polynomial(result)


def ring_power(value, exponent):
    result = (1, 0, 0, 0)
    for _ in range(exponent):
        result = multiply(result, value)
    return result


def interval_polynomial(coefficients, lower, upper):
    assert 0 < lower <= upper
    low = high = Fraction(0)
    for exponent, coefficient in enumerate(coefficients):
        endpoints = (coefficient * lower**exponent,
                     coefficient * upper**exponent)
        low += min(endpoints)
        high += max(endpoints)
    return low, high


def absolute_interval(interval):
    low, high = interval
    lower = 0 if low <= 0 <= high else min(abs(low), abs(high))
    return Fraction(lower), max(abs(low), abs(high))


def scale_nonnegative(interval, lower, upper):
    assert 0 <= interval[0] <= interval[1] and 0 < lower <= upper
    return interval[0] * lower, interval[1] * upper


def determinant(matrix):
    total = 0
    for permutation in permutations(range(len(matrix))):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(len(matrix))
                         for j in range(i + 1, len(matrix)))
        term = (-1)**inversions
        for i, j in enumerate(permutation):
            term *= matrix[i][j]
        total += term
    return total


def encode(value):
    if isinstance(value, Fraction):
        return [value.numerator, value.denominator]
    if isinstance(value, (list, tuple)):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    return value


def main():
    data = json.loads((HERE / "inputs.json").read_text(encoding="utf-8"))
    assert data["polynomial_ascending"] == list(P)
    lower = Fraction(*data["beta_lower"])
    upper = Fraction(*data["beta_upper"])
    assert Fraction(17, 10) < lower < upper < Fraction(18, 10)
    root_signs = [interval_polynomial(P, value, value)[0]
                  for value in (lower, upper)]
    assert root_signs[0] < 0 < root_signs[1]

    records, accepted = [], []
    for digits in product((-1, 0, 1), repeat=4):
        tests = [scale_nonnegative(
            absolute_interval(interval_polynomial(polynomial, lower, upper)),
            lower - 1, upper - 1)
            for polynomial in (digits, digits[::-1])]
        inside = all(test[1] < 2 for test in tests)
        outside = any(test[0] > 2 for test in tests)
        assert inside != outside, (digits, tests)
        records.append({"digits": digits, "tests": tests, "accepted": inside})
        if inside:
            accepted.append(digits)
    positive = [(-1, 1, 0, 0), (0, -1, 1, 0),
                (0, 0, -1, 1), (-1, 1, 1, -1)]
    expected = {(0, 0, 0, 0)} | set(positive)
    expected |= {tuple(-value for value in row) for row in positive}
    assert len(records) == 81 and set(accepted) == expected

    one = (1, 0, 0, 0)
    beta = (0, 1, 0, 0)
    beta_inverse = (1, 1, 1, -1)
    difference_inverse = (-2, -1, 0, 1)
    assert multiply(beta, beta_inverse) == one
    assert multiply((-1, 1, 0, 0), difference_inverse) == one
    factor = multiply(ring_power(beta, 4), difference_inverse)
    columns = [multiply(factor, tuple(int(i == j) for i in range(4)))
               for j in range(4)]
    matrix = [list(row) for row in zip(*columns)]
    assert abs(determinant(matrix)) == 1
    functional = matrix[3]
    assert factor == (-1, 0, 1, 2) and functional == [2, 3, 5, 9]
    inverse_factor = multiply(ring_power(beta_inverse, 4), (-1, 1, 0, 0))
    assert multiply(factor, inverse_factor) == one
    kernel_basis = [multiply(inverse_factor, tuple(int(i == j) for i in range(4)))
                    for j in range(3)]
    for j, generator in enumerate(kernel_basis):
        assert multiply(factor, generator) == tuple(int(i == j) for i in range(4))
    translations = [multiply(ring_power(beta_inverse, 4), theta)
                    for theta in accepted]
    assert all(sum(x * y for x, y in zip(functional, step)) == 0
               for step in translations)

    c = tuple(data["c"])
    assert c == (-3, 3, 1, -1)
    coordinate = sum(a * b for a, b in zip(functional, c))
    assert coordinate == -1
    expanding = scale_nonnegative(absolute_interval(interval_polynomial(
        multiply(ring_power(beta, 4), c), lower, upper)), lower - 1, upper - 1)
    stable = scale_nonnegative(absolute_interval(interval_polynomial(
        c, 1 / upper, 1 / lower)), lower - 1, upper - 1)
    assert expanding[1] < 1 and stable[1] < lower

    k, left, right = data["tail_length"], data["left"], data["right"]
    assert k == 24 and len(left) == len(right) == k
    word = left + [0] * 4 + right
    assert all(type(digit) is int and digit in (-1, 0, 1) for digit in word)
    left_target = tuple(-a for a in multiply(ring_power(beta, k + 4), c))
    assert reduce_polynomial(left) == left_target
    assert reduce_polynomial(right) == c
    assert reduce_polynomial(word) == (0, 0, 0, 0)
    assert len(word) == 52 and word.count(0) == 15
    probability = Fraction(1)
    for digit in word:
        probability *= Fraction(1, 2 if digit == 0 else 4)
    assert probability == Fraction(1, 2**89)

    output = {"method": "independent polynomial long division and monomial intervals",
              "root_bracket": [lower, upper], "P_endpoint_values": root_signs,
              "patterns": records, "accepted": accepted,
              "functional": functional, "factor_matrix": matrix,
              "factor_determinant": determinant(matrix),
              "kernel_basis": kernel_basis, "witness_c": c,
              "witness_coordinate": coordinate, "witness_expanding_test": expanding,
              "witness_stable_test": stable, "stable_upper_threshold_lower": lower,
              "left_endpoint": reduce_polynomial(left),
              "right_endpoint": reduce_polynomial(right), "word": word,
              "word_zero_count": word.count(0), "unconditional_probability": probability,
              "return_value": reduce_polynomial(word), "discovery_rerun": False}
    encoded = json.dumps(encode(output), indent=2) + "\n"
    assert len(encoded.encode("utf-8")) < 262144
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "verification.json").write_text(encoded, encoding="utf-8")
    print(json.dumps({"patterns": len(records), "accepted": len(accepted),
                      "functional": functional, "factor_determinant": determinant(matrix),
                      "witness_coordinate": coordinate, "word_length": len(word),
                      "word_zero_count": word.count(0), "probability": str(probability),
                      "return_verified": True, "discovery_rerun": False}))


if __name__ == "__main__":
    main()
