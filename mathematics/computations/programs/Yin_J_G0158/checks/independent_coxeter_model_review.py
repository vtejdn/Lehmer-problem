"""Independent exact verification of the fixed J158 diagram-model certificate.

Run with a standard-library Python interpreter, from any working directory:
  python -B path/to/independent_coxeter_model_review.py

No author program is imported or executed.  Reflections and transvections are
rebuilt by their actions on individual vectors.  Rational determinant values
at n+1 distinct integers certify each complete degree-n characteristic
polynomial independently of the author's Newton-identity implementation.
The sole polynomial input and the actual author certificate are read only;
the reviewer result is written separately after every check succeeds.
"""

from fractions import Fraction
from pathlib import Path
import json


GROUP = Path(__file__).resolve().parents[1]
ROOT = GROUP.parents[3]
INPUT = GROUP.parent / "Yin_J_G0144" / "trace56_cell.json"
OUTPUT_HOME = ROOT / "mathematics" / "computations" / "outputs" / GROUP.name
CERTIFICATE = OUTPUT_HOME / "coxeter_model.json"
OUTPUT = OUTPUT_HOME / "independent_coxeter_model_review.json"
EXPECTED_P = [1, -1, 1, -1, 0, 0, -1, 1, -1, 1, -1, 1, -1, 0, 0, -1, 1, -1, 1]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def exact_payload(actual, expected, path="certificate"):
    """Compare every field and entry, including integer/Boolean type distinctions."""
    require(type(actual) is type(expected), path + " type")
    if isinstance(expected, dict):
        require(actual.keys() == expected.keys(), path + " field set")
        for key in expected:
            exact_payload(actual[key], expected[key], path + "." + key)
    elif isinstance(expected, list):
        require(len(actual) == len(expected), path + " length")
        for index, value in enumerate(expected):
            exact_payload(actual[index], value, path + f"[{index}]")
    else:
        require(actual == expected, path + " value")


def unit(n, j):
    return [int(i == j) for i in range(n)]


def eye(n):
    return [unit(n, i) for i in range(n)]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def mv(matrix, vector):
    require(all(len(row) == len(vector) for row in matrix), "matrix/vector dimensions")
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def mm(left, right):
    return transpose([mv(left, column) for column in transpose(right)])


def bilinear(gram, left, right):
    return sum(a * b for a, b in zip(left, mv(gram, right)))


def operator_matrix(n, action):
    return transpose([action(unit(n, j)) for j in range(n)])


def determinant(matrix):
    """Exact Gaussian elimination with rational pivots, without Bareiss/Newton."""
    work = [[Fraction(value) for value in row] for row in matrix]
    n, answer = len(work), Fraction(1)
    require(all(len(row) == n for row in work), "determinant square shape")
    for j in range(n):
        pivot = next((i for i in range(j, n) if work[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            work[j], work[pivot] = work[pivot], work[j]
            answer = -answer
        diagonal = work[j][j]
        answer *= diagonal
        for i in range(j + 1, n):
            factor = work[i][j] / diagonal
            work[i][j] = 0
            for k in range(j + 1, n):
                work[i][k] -= factor * work[j][k]
    require(answer.denominator == 1, "integer matrix determinant integrality")
    return answer.numerator


def polynomial_value(coefficients, x):
    result = 0
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


def characteristic_values(matrix, coefficients):
    n = len(matrix)
    require(len(coefficients) == n + 1 and coefficients[-1] == 1,
            "characteristic polynomial degree and leading coefficient")
    values = []
    for x in range(n + 1):
        shifted = [[x * int(i == j) - matrix[i][j] for j in range(n)] for i in range(n)]
        value = determinant(shifted)
        require(value == polynomial_value(coefficients, x), f"characteristic value at {x}")
        values.append(value)
    # Both polynomials have degree at most n; n+1 distinct equalities suffice.
    return values


def power(matrix, exponent):
    result = eye(len(matrix))
    for digit in bin(exponent)[2:]:
        result = mm(result, result)
        if digit == "1":
            result = mm(result, matrix)
    return result


def root_reflection(gram, root):
    require(bilinear(gram, root, root) == 2, "reflection norm two")
    return operator_matrix(len(root), lambda x: [a - bilinear(gram, x, root) * b
                                               for a, b in zip(x, root)])


def main():
    polynomial = json.loads(INPUT.read_text(encoding="utf-8"))["H_ascending"]
    exact_payload(polynomial, EXPECTED_P, "H_ascending")
    data = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    vertices = [f"h{i}" for i in range(1, 18)] + ["left_leaf", "right_leaf"]
    edges = [[i, i + 1] for i in range(16)] + [[2, 17], [14, 18]]
    gram19 = [[2 * int(i == j) for j in range(19)] for i in range(19)]
    for i, j in edges:
        gram19[i][j] = gram19[j][i] = -1
    images = [16 - i for i in range(17)] + [18, 17]

    def symmetry(vector):
        return [vector[images[i]] for i in range(19)]

    def word(vector, indices):
        result = list(vector)
        for i in reversed(indices):
            coefficient = sum(gram19[i][j] * result[j] for j in range(19))
            result[i] -= coefficient
        return result

    color_a, color_b = [0, 2, 4, 6, 8], [1, 3, 5, 7, 17]
    for color in (color_a, color_b):
        require(all(gram19[i][j] == 0 for i in color for j in color if i != j),
                "commuting color reflections")
    sigma = operator_matrix(19, symmetry)
    c = operator_matrix(19, lambda x: word(x, color_a + color_b))
    g = operator_matrix(19, lambda x: symmetry(word(x, color_a + color_b)))
    for matrix in (sigma, c, g):
        require(mm(transpose(matrix), mm(gram19, matrix)) == gram19, "source isometry")
    require(mm(sigma, sigma) == eye(19), "diagram involution")

    left_null = [2, 4, 6, 5, 4, 3, 2, 1] + [0] * 9 + [3, 0]
    right_null = symmetry(left_null)
    radical = [a - b for a, b in zip(left_null, right_null)]
    require(bilinear(gram19, left_null, left_null) == 0, "left affine null norm")
    require(bilinear(gram19, right_null, right_null) == 0, "right affine null norm")
    require(mv(gram19, radical) == [0] * 19, "radical")
    require(mv(g, radical) == [-x for x in radical], "radical eigenvalue minus one")
    omitted, keep = 7, [i for i in range(19) if i != 7]
    require(radical[omitted] == 1, "primitive radical and integral quotient")

    def project(vector):
        return [vector[i] - vector[omitted] * radical[i] for i in keep]

    inclusion = transpose([unit(19, i) for i in keep])
    projection = operator_matrix(19, project)
    gram = [[gram19[i][j] for j in keep] for i in keep]
    aq = operator_matrix(18, lambda x: project(mv(g, mv(inclusion, x))))
    require(mm(projection, inclusion) == eye(18), "quotient section")
    require(mv(projection, radical) == [0] * 18, "quotient kernel")
    require(mm(transpose(projection), mm(gram, projection)) == gram19, "form descends")
    require(mm(projection, g) == mm(aq, projection), "whole quotient intertwining")
    require(mm(transpose(aq), mm(gram, aq)) == gram, "quotient isometry")
    augmented = transpose(transpose(inclusion) + [radical])
    require(abs(determinant(augmented)) == 1, "integral quotient and radical basis")
    augmented_gram = [row + [0] for row in gram] + [[0] * 19]
    require(mm(transpose(augmented), mm(gram19, augmented)) == augmented_gram,
            "source congruence to quotient plus zero")

    left_roots = list(range(7)) + [17]
    right_roots = [images[i] for i in left_roots]
    positive_roots = left_roots + right_roots
    e = project(left_null)
    require(e == project(right_null), "common affine null class")
    f = [-a - b for a, b in zip(project(unit(19, 8)), e)]
    basis = transpose([project(unit(19, i)) for i in positive_roots] + [e, f])
    inverse_basis = data["split_basis_inverse"]
    require(type(inverse_basis) is list and len(inverse_basis) == 18,
            "inverse basis row count")
    require(all(type(row) is list and len(row) == 18 and all(type(x) is int for x in row)
                for row in inverse_basis), "integer inverse basis")
    require(mm(basis, inverse_basis) == mm(inverse_basis, basis) == eye(18),
            "both integral basis inverse identities")
    basis_det = determinant(basis)
    require(abs(basis_det) == 1, "unimodular split basis")
    e8 = [[gram19[i][j] for j in left_roots] for i in left_roots]
    minors = [determinant([row[:j] for row in e8[:j]]) for j in range(1, 9)]
    require(minors == [2, 3, 4, 5, 6, 7, 8, 1], "positive E8 principal minors")
    h = [[e8[i % 8][j % 8] if i // 8 == j // 8 else 0
          for j in range(16)] for i in range(16)]
    split = [row + [0, 0] for row in h] + [[0] * 16 + [0, 1], [0] * 16 + [1, 0]]
    require(mm(transpose(basis), mm(gram, basis)) == split, "complete E8 plus E8 plus U")
    require(determinant(gram) == -1, "quotient determinant")
    require(all(gram[i][i] % 2 == 0 for i in range(18)), "even quotient")
    a = mm(inverse_basis, mm(aq, basis))
    require(mm(basis, a) == mm(aq, basis), "full conjugacy")
    positive_word = [0, 2, 4, 6, 1, 3, 5, 17]
    sigma_p = operator_matrix(19, lambda x: symmetry(word(x, positive_word)))
    r = mm(inverse_basis, mm(projection, mm(sigma_p, mm(inclusion, basis))))
    rp = [row[:16] for row in r[:16]]
    require(r == [row + [0, 0] for row in rp] + [[0] * 16 + [1, 0], [0] * 16 + [0, 1]],
            "positive isometry fixes U")
    require(mm(transpose(rp), mm(h, rp)) == h, "positive form invariance")
    require(power(rp, 60) == eye(16), "positive order divides sixty")
    require(all(power(rp, 60 // prime) != eye(16) for prime in (2, 3, 5)),
            "positive order is exactly sixty")
    theta = [2, 4, 6, 5, 4, 3, 2, 3] + [0] * 8
    theta18 = theta + [0, 0]
    require(bilinear(h, theta, theta) == 2, "theta norm")
    null_e, null_f = unit(18, 16), unit(18, 17)
    h8 = [u - v for u, v in zip(null_e, theta18)]
    require(mv(inverse_basis, project(unit(19, 7))) == h8, "h8 equals e minus theta")
    require(mv(inverse_basis, project(unit(19, 8))) == [-u - v for u, v in zip(null_e, null_f)],
            "h9 equals minus e minus f")

    def transvection(cusp):
        def action(x):
            first, second = bilinear(split, cusp, x), bilinear(split, theta18, x)
            return [xi + first * vi - second * ci - first * ci
                    for xi, vi, ci in zip(x, theta18, cusp)]
        return operator_matrix(18, action)

    te, tf = transvection(null_e), transvection(null_f)
    j = root_reflection(split, [u + v for u, v in zip(null_e, null_f)])
    sh8 = root_reflection(split, h8)
    require(mm(j, sh8) == mm(te, tf), "whole reflection to transvection identity")
    require(a == mm(r, mm(j, sh8)) == mm(r, mm(te, tf)), "whole two transvection identity")
    for matrix in (r, te, tf, a):
        require(mm(transpose(matrix), mm(split, matrix)) == split, "split form invariance")
    require(determinant(a) == 1, "isometry determinant")

    full = [0] * 20
    for i, value in enumerate(polynomial):
        full[i] += value
        full[i + 1] += value
    char_values = {"split_isometry": characteristic_values(a, polynomial),
                   "quotient_isometry": characteristic_values(aq, polynomial),
                   "source_isometry": characteristic_values(g, full)}
    expected = {
        "polynomial_ascending": polynomial,
        "source_vertex_labels": vertices, "source_edges_zero_indexed": edges,
        "color_a_zero_indexed": color_a, "color_b_zero_indexed": color_b,
        "source_gram": gram19, "source_inertia": [17, 1, 1],
        "diagram_involution_images_zero_indexed": images,
        "diagram_involution": sigma, "bicolored_element": c, "source_isometry": g,
        "primitive_radical": radical, "radical_eigenvalue": -1,
        "quotient_omitted_vertex_zero_indexed": omitted,
        "quotient_projection": projection, "quotient_inclusion": inclusion,
        "quotient_gram": gram, "quotient_gram_determinant": -1,
        "quotient_gram_inertia": [17, 1, 0], "quotient_isometry": aq,
        "left_affine_null": left_null, "right_affine_null": right_null,
        "positive_basis_vertices_zero_indexed": positive_roots,
        "split_basis": basis, "split_basis_inverse": inverse_basis,
        "split_basis_determinant": basis_det, "split_gram": split,
        "e8_gram": e8, "e8_leading_principal_minors": minors,
        "positive_gram": h, "positive_isometry": rp, "positive_isometry_order": 60,
        "theta": theta, "theta_squared_norm": 2,
        "extended_positive_isometry": r, "e_transvection": te, "f_transvection": tf,
        "split_isometry": a, "characteristic_polynomial_ascending": polynomial,
        "source_characteristic_polynomial_ascending": full,
        "two_transvection_identity_verified": True, "status": "verified",
    }
    exact_payload(data, expected)
    result = {
        "result": "verified", "polynomial_ascending": polynomial,
        "certificate_fields_checked": list(expected),
        "source_inertia": [17, 1, 1], "quotient_inertia": [17, 1, 0],
        "quotient_determinant": -1, "split_basis_determinant": basis_det,
        "e8_leading_principal_minors": minors,
        "positive_isometry_exact_order": 60, "theta_squared_norm": 2,
        "characteristic_determinants_at_0_through_dimension": char_values,
        "full_characteristic_polynomials_verified": True,
        "full_reflection_and_transvection_identities_verified": True,
        "integral_quotient_and_split_basis_verified": True,
        "source_inspection": "Mathematical figure and source conventions are reviewed separately in R1114v6.",
    }
    OUTPUT_HOME.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": result["result"], "output": OUTPUT.relative_to(ROOT).as_posix(),
                      "fields_checked": len(expected), "split_basis_determinant": basis_det,
                      "positive_isometry_exact_order": 60}, indent=2))


if __name__ == "__main__":
    main()
