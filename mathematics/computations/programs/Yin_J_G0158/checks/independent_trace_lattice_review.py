"""Independent exact check of the fixed J158 degree-18 certificate.

Run from any directory with a Python standard-library interpreter:
  python -B path/to/independent_trace_lattice_review.py

This checker does not import or execute trace_lattice.py.
It rebuilds multiplication and traces in Q[x]/(p), verifies every supplied
matrix entry through exact identities, and proves the inertia from positive
leading principal minors and the certified hyperbolic-plane splitting.
Only the reported 51-vector search prefix is checked; no further search runs.
The generated review output is distinct from the author's certificate.
"""

import argparse
from fractions import Fraction
from math import gcd
from pathlib import Path
import json


GROUP = Path(__file__).resolve().parents[1]
ROOT = GROUP.parents[3]
DEFAULT_INPUT = GROUP.parent / "Yin_J_G0144" / "trace56_cell.json"
OUTPUT_HOME = ROOT / "mathematics" / "computations" / "outputs" / GROUP.name
EXPECTED_P = [1, -1, 1, -1, 0, 0, -1, 1, -1, 1, -1, 1, -1, 0, 0, -1, 1, -1, 1]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def integer_vector(value, length, name):
    require(isinstance(value, list) and len(value) == length, name + " length")
    require(all(type(x) is int for x in value), name + " integer entries")
    return value


def integer_matrix(value, size, name):
    require(isinstance(value, list) and len(value) == size, name + " row count")
    for row in value:
        integer_vector(row, size, name)
    return value


def eye(size):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def tr(matrix):
    return [list(column) for column in zip(*matrix)]


def mm(left, right):
    rows, inner, columns = len(left), len(right), len(right[0])
    require(all(len(row) == inner for row in left), "matrix product shape")
    require(all(len(row) == columns for row in right), "rectangular right matrix")
    return [[sum(left[i][k] * right[k][j] for k in range(inner))
             for j in range(columns)] for i in range(rows)]


def form(matrix, left, right):
    return sum(left[i] * matrix[i][j] * right[j]
               for i in range(len(left)) for j in range(len(right)))


def rational_determinant(matrix):
    """Ordinary rational row elimination, not the author's Bareiss routine."""
    work = [[Fraction(entry) for entry in row] for row in matrix]
    determinant = Fraction(1)
    for column in range(len(work)):
        pivot_row = next((i for i in range(column, len(work)) if work[i][column]), None)
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            determinant = -determinant
        pivot = work[column][column]
        determinant *= pivot
        for i in range(column + 1, len(work)):
            multiplier = work[i][column] / pivot
            work[i][column] = Fraction(0)
            for j in range(column + 1, len(work)):
                work[i][j] -= multiplier * work[column][j]
    return determinant


def integer(value, label):
    value = Fraction(value)
    require(value.denominator == 1, label + " is integral")
    return value.numerator


def ring_product(left, right, polynomial):
    """Convolution followed by monic polynomial reduction in Q[x]/(p)."""
    degree = len(polynomial) - 1
    raw = [0] * (2 * degree - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            raw[i + j] += a * b
    for power in range(len(raw) - 1, degree - 1, -1):
        coefficient = raw[power]
        if coefficient:
            for i in range(degree + 1):
                raw[power - degree + i] -= coefficient * polynomial[i]
    require(all(x == 0 for x in raw[degree:]), "polynomial reduction")
    return raw[:degree]


def multiplication_operator(element, polynomial):
    degree = len(polynomial) - 1
    columns = [ring_product(element, basis, polynomial) for basis in eye(degree)]
    return tr(columns)


def algebra_trace(element, polynomial):
    operator = multiplication_operator(element, polynomial)
    return sum(operator[i][i] for i in range(len(operator)))


def matrix_characteristic(matrix):
    """Reconstruct coefficients from independently multiplied matrix powers."""
    size = len(matrix)
    current, traces = eye(size), [size]
    for _ in range(size):
        current = mm(current, matrix)
        traces.append(sum(current[i][i] for i in range(size)))
    descending = [Fraction(1)]
    for k in range(1, size + 1):
        descending.append(-sum(descending[k - j] * traces[j]
                               for j in range(1, k + 1)) / k)
    return [integer(x, "characteristic coefficient") for x in reversed(descending)]


def verify(input_path, result_path):
    source = json.loads(input_path.read_text(encoding="utf-8"))
    certificate = json.loads(result_path.read_text(encoding="utf-8"))
    polynomial = integer_vector(source["H_ascending"], 19, "fixed H_ascending")
    require(polynomial == EXPECTED_P, "exact designated degree-18 input")
    require(polynomial == polynomial[::-1] and polynomial[0] == polynomial[-1] == 1,
            "monic reciprocal integer unit polynomial")
    require(certificate["polynomial_ascending"] == polynomial, "certificate input identity")
    size = 18

    one = [1] + [0] * (size - 1)
    alpha = [0, 1] + [0] * (size - 2)
    inverse_alpha = [-coefficient for coefficient in polynomial[1:]]
    require(ring_product(alpha, inverse_alpha, polynomial) == one, "inverse of alpha")
    companion = multiplication_operator(alpha, polynomial)
    actual_c = integer_matrix(certificate["companion"], size, "companion")
    require(actual_c == companion, "every companion entry and column convention")
    positive, negative = [], []
    forward, backward = one, one
    for _ in range(size):
        positive.append(algebra_trace(forward, polynomial))
        negative.append(algebra_trace(backward, polynomial))
        forward = ring_product(forward, alpha, polynomial)
        backward = ring_product(backward, inverse_alpha, polynomial)
    require(positive == negative, "reciprocal positive and negative traces")
    require(certificate["trace_powers_zero_through_17"] == positive, "every reported Newton trace")
    gram = [[positive[i - j] if i >= j else negative[j - i]
             for j in range(size)] for i in range(size)]
    actual_g = integer_matrix(certificate["trace_gram"], size, "trace Gram")
    require(actual_g == gram, "every trace Gram entry")
    require(gram == tr(gram), "Gram symmetry")
    require(all(gram[i][i] % 2 == 0 for i in range(size)), "even integral Gram")
    require(mm(tr(companion), mm(gram, companion)) == gram, "companion Gram invariance")
    require(matrix_characteristic(companion) == polynomial, "full companion characteristic polynomial")
    gram_determinant = integer(rational_determinant(gram), "Gram determinant")
    require(gram_determinant == -2915479459020775961521, "specified Gram determinant")
    require(certificate["gram_determinant"] == gram_determinant, "reported Gram determinant")
    require(certificate["companion_invariance"] is True and certificate["gram_even"] is True,
            "reported established Gram flags")

    split = certificate["splitting"]
    require(isinstance(split, dict), "actual complete splitting")
    e = integer_vector(split["e"], size, "e")
    f = integer_vector(split["f"], size, "f")
    require(e == [1] + [0] * 16 + [-1], "displayed e")
    expected_f = [0] * size
    for index, value in ((0, -24), (1, 1), (2, -1), (9, -1), (17, 24)):
        expected_f[index] = value
    require(f == expected_f, "displayed f")
    dual_e = [sum(gram[i][j] * e[j] for j in range(size)) for i in range(size)]
    require(gcd(*dual_e) == 1 and form(gram, e, e) == 0, "divisor-one isotropic witness")
    require(form(gram, f, f) == 0 and form(gram, e, f) == 1, "integral hyperbolic pair")
    f0 = [0] * size
    f0[1], f0[2], f0[9] = 1, -1, -1
    require(form(gram, e, f0) == 1 and form(gram, f0, f0) == 48, "explicit Bezout partner")
    require(f == [f0[i] - 24 * e[i] for i in range(size)], "even-norm null correction")

    # These are exactly the candidates preceding the supplied witness in the
    # author's order: all 18 positive singletons, then (0,j) with both signs.
    require(all(gram[i][i] != 0 for i in range(size)), "18 preceding singleton norms")
    preceding_pair_norms = [gram[0][0] + gram[j][j] + 2 * sign * gram[0][j]
                            for j in range(1, 17) for sign in (-1, 1)]
    require(len(preceding_pair_norms) == 32 and all(preceding_pair_norms),
            "32 preceding support-two candidates are not isotropic")
    require(gram[0][0] + gram[17][17] - 2 * gram[0][17] == 0, "33rd pair norm")
    require(certificate["search"] == {
        "status": "primitive_divisor_one_witness",
        "checked_by_support": {"1": 18, "2": 33, "3": 0, "4": 0},
        "isotropic_seen": 1}, "exact reported prefix and stopping meaning")
    require(certificate["search_support_cap"] == 4 and certificate["search_seconds_allowance"] == 20,
            "declared finite search settings")

    basis = integer_matrix(split["basis_columns_positive_then_e_f"], size, "basis T")
    basis_inverse = integer_matrix(split["basis_inverse"], size, "basis inverse")
    split_gram = integer_matrix(split["split_gram"], size, "split Gram")
    positive_gram = integer_matrix(split["positive_gram"], size - 2, "positive Gram")
    conjugated = integer_matrix(split["conjugated_companion"], size, "conjugated companion")
    require([row[-2] for row in basis] == e and [row[-1] for row in basis] == f,
            "last basis columns are the actual e and f")
    require(mm(basis, basis_inverse) == eye(size) and mm(basis_inverse, basis) == eye(size),
            "both complete integral inverse identities")
    determinant_t = integer(rational_determinant(basis), "basis determinant")
    require(determinant_t == split["basis_determinant"] == -1, "unimodular basis determinant")
    require(mm(tr(basis), mm(gram, basis)) == split_gram, "every split Gram entry")
    expected_split = [row + [0, 0] for row in positive_gram]
    expected_split += [[0] * 16 + [0, 1], [0] * 16 + [1, 0]]
    require(split_gram == expected_split, "complete positive-plus-U block identity")
    require(positive_gram == tr(positive_gram), "positive Gram symmetry")
    principal_minors = [integer(rational_determinant([row[:k] for row in positive_gram[:k]]),
                                "positive leading principal minor")
                        for k in range(1, 17)]
    require(all(value > 0 for value in principal_minors), "Sylvester positive definiteness")
    require(principal_minors[-1] == -gram_determinant, "split determinant relation")
    require(split["positive_inertia"] == [16, 0, 0] and certificate["gram_inertia"] == [17, 1, 0],
            "inertias proved by positive block and the unimodular U splitting")
    require(mm(basis_inverse, mm(companion, basis)) == conjugated, "every conjugated matrix entry")
    require(mm(companion, basis) == mm(basis, conjugated), "complete CT=TA identity")
    require(mm(tr(conjugated), mm(split_gram, conjugated)) == split_gram,
            "complete split Gram preservation")
    require(matrix_characteristic(conjugated) == polynomial, "full transformed characteristic polynomial")
    require(split["full_integer_identity_checks"] is True, "verified complete-identity flag")

    return {
        "result": "verified",
        "polynomial_ascending": polynomial,
        "degree": size,
        "trace_powers_zero_through_17": positive,
        "gram_determinant": gram_determinant,
        "basis_determinant": determinant_t,
        "gram_inertia": [17, 1, 0],
        "positive_inertia": [16, 0, 0],
        "positive_leading_principal_minors": principal_minors,
        "verified_matrix_fields": ["companion", "trace_gram", "basis_columns_positive_then_e_f",
                                   "basis_inverse", "positive_gram", "split_gram", "conjugated_companion"],
        "verified_search_prefix": certificate["search"],
        "arithmetic": "Python integers and fractions.Fraction; no author-code import",
        "scope": "The fixed degree-18 certificate and its reported search prefix; no further search, numerical roots, historical timing replay or transvection decomposition."
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--result", type=Path, default=OUTPUT_HOME / "trace_lattice.json")
    parser.add_argument("--output", type=Path, default=OUTPUT_HOME / "independent_trace_lattice_review.json")
    args = parser.parse_args()
    require(args.output.resolve() not in {args.input.resolve(), args.result.resolve(), Path(__file__).resolve()},
            "review output must not overwrite an input or the checker")
    report = verify(args.input, args.result)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
