"""Exact Figure 7 quotient and two-transvection model for the fixed H input."""

from pathlib import Path
import json

from trace_lattice import (
    determinant, identity, inertia, inverse_integral, matvec, multiply,
    pairing, transpose,
)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INPUT = HERE.parent / "Yin_J_G0144" / "trace56_cell.json"
OUTPUT = ROOT / "mathematics/computations/outputs/Yin_J_G0158/coxeter_model.json"


def columns(vectors):
    return transpose(vectors)


def unit(n, i):
    return [int(j == i) for j in range(n)]


def matrix_power(a, exponent):
    result = identity(len(a))
    while exponent:
        if exponent & 1:
            result = multiply(result, a)
        a = multiply(a, a)
        exponent //= 2
    return result


def characteristic(a):
    """Newton identities, all n coefficients, returned in ascending order."""
    n = len(a)
    power, descending, traces = identity(n), [1], []
    for k in range(1, n + 1):
        power = multiply(power, a)
        traces.append(sum(power[i][i] for i in range(n)))
        numerator = -sum(descending[j] * traces[k - j - 1] for j in range(k))
        assert numerator % k == 0
        descending.append(numerator // k)
    return descending[::-1]


def reflection(gram, i):
    assert gram[i][i] == 2
    result = identity(len(gram))
    result[i] = [x - y for x, y in zip(result[i], gram[i])]
    assert multiply(result, result) == identity(len(gram))
    assert multiply(transpose(result), multiply(gram, result)) == gram
    return result


def ordered_product(matrices, n):
    result = identity(n)
    for matrix in matrices:
        result = multiply(result, matrix)
    return result


def transvection(h, v, cusp):
    n = len(h)
    hv = matvec(h, v)
    norm = sum(x * y for x, y in zip(v, hv))
    assert norm % 2 == 0
    own, other = (n, n + 1) if cusp == "e" else (n + 1, n)
    result = identity(n + 2)
    for i in range(n):
        result[i][other] += v[i]
        result[own][i] -= hv[i]
    result[own][other] -= norm // 2
    return result


def main():
    p = json.loads(INPUT.read_text(encoding="utf-8"))["H_ascending"]
    assert p == [1, -1, 1, -1, 0, 0, -1, 1, -1, 1, -1, 1, -1, 0, 0, -1, 1, -1, 1]
    # Coordinates h1,...,h17,left leaf,right leaf; all edges have Gram -1.
    labels = [f"h{i}" for i in range(1, 18)] + ["left_leaf", "right_leaf"]
    edges = [(i, i + 1) for i in range(16)] + [(2, 17), (14, 18)]
    b = [[2 * int(i == j) for j in range(19)] for i in range(19)]
    for i, j in edges:
        b[i][j] = b[j][i] = -1
    assert inertia(b) == [17, 1, 1]
    reflections = [reflection(b, i) for i in range(19)]
    color_a = [0, 2, 4, 6, 8]
    color_b = [1, 3, 5, 7, 17]
    for color in (color_a, color_b):
        assert all(b[i][j] == 0 for i in color for j in color if i != j)
    c = ordered_product([reflections[i] for i in color_a + color_b], 19)
    sigma_images = list(range(16, -1, -1)) + [18, 17]
    sigma = columns([unit(19, i) for i in sigma_images])
    assert multiply(sigma, sigma) == identity(19)
    assert multiply(transpose(sigma), multiply(b, sigma)) == b
    g = multiply(sigma, c)

    # The two affine-E8 null vectors have a common image in the quotient.
    left_null = [2, 4, 6, 5, 4, 3, 2, 1] + [0] * 9 + [3, 0]
    right_null = matvec(sigma, left_null)
    radical = [x - y for x, y in zip(left_null, right_null)]
    assert matvec(b, radical) == [0] * 19
    assert matvec(g, radical) == [-x for x in radical]
    omitted = 7  # coefficient of h8 in the primitive radical is one.
    assert radical[omitted] == 1
    keep = [i for i in range(19) if i != omitted]
    inclusion = columns([unit(19, i) for i in keep])
    projection = [[int(j == i) if j != omitted else -radical[i]
                   for j in range(19)] for i in keep]
    assert multiply(projection, inclusion) == identity(18)
    assert matvec(projection, radical) == [0] * 18
    gram = multiply(transpose(inclusion), multiply(b, inclusion))
    a_quotient = multiply(projection, multiply(g, inclusion))
    assert multiply(projection, g) == multiply(a_quotient, projection)
    assert multiply(transpose(a_quotient), multiply(gram, a_quotient)) == gram
    assert determinant(gram) == -1
    assert inertia(gram) == [17, 1, 0]
    assert all(gram[i][i] % 2 == 0 for i in range(18))

    # Mirrored finite E8 bases make sigma exchange the two eight-dimensional blocks.
    left_roots = list(range(7)) + [17]
    right_roots = [sigma_images[i] for i in left_roots]
    e = matvec(projection, left_null)
    minus_h9 = [-x for x in unit(19, 8)]
    f = [x - y for x, y in zip(matvec(projection, minus_h9), e)]
    basis = columns([matvec(projection, unit(19, i))
                     for i in left_roots + right_roots] + [e, f])
    inverse_basis = inverse_integral(basis)
    split = multiply(transpose(basis), multiply(gram, basis))
    h = [row[:16] for row in split[:16]]
    k = [row[:8] for row in h[:8]]
    assert h == [[k[i % 8][j % 8] if i // 8 == j // 8 else 0
                  for j in range(16)] for i in range(16)]
    expected_split = [row + [0, 0] for row in h] + [[0] * 16 + [0, 1], [0] * 16 + [1, 0]]
    assert split == expected_split
    assert determinant(k) == 1
    assert [determinant([row[:j] for row in k[:j]]) for j in range(1, 9)] == [2, 3, 4, 5, 6, 7, 8, 1]
    assert inertia(h) == [16, 0, 0]
    a = multiply(inverse_basis, multiply(a_quotient, basis))

    # Exact identity J s_(e-theta) = E_theta F_theta, where J swaps e,f with minus signs.
    positive_indices = [0, 2, 4, 6, 1, 3, 5, 17]
    positive_word = ordered_product([reflections[i] for i in positive_indices], 19)
    r = multiply(inverse_basis, multiply(projection, multiply(multiply(sigma, positive_word), multiply(inclusion, basis))))
    r_positive = [row[:16] for row in r[:16]]
    expected_r = [row + [0, 0] for row in r_positive] + [[0] * 16 + [1, 0], [0] * 16 + [0, 1]]
    assert r == expected_r
    assert multiply(transpose(r_positive), multiply(h, r_positive)) == h
    assert matrix_power(r_positive, 60) == identity(16)
    assert all(matrix_power(r_positive, 60 // prime) != identity(16) for prime in (2, 3, 5))
    theta = [2, 4, 6, 5, 4, 3, 2, 3] + [0] * 8
    assert pairing(h, theta, theta) == 2
    e_theta = transvection(h, theta, "e")
    f_theta = transvection(h, theta, "f")
    for transvection_matrix in (e_theta, f_theta):
        assert multiply(transpose(transvection_matrix), multiply(split, transvection_matrix)) == split
    assert a == multiply(r, multiply(e_theta, f_theta))
    assert multiply(transpose(a), multiply(split, a)) == split
    assert characteristic(a) == p
    assert characteristic(a_quotient) == p
    full_polynomial = [0] * 20
    for i, coefficient in enumerate(p):
        full_polynomial[i] += coefficient
        full_polynomial[i + 1] += coefficient
    assert characteristic(g) == full_polynomial
    assert determinant(a) == 1

    result = {
        "polynomial_ascending": p,
        "source_vertex_labels": labels, "source_edges_zero_indexed": edges,
        "color_a_zero_indexed": color_a, "color_b_zero_indexed": color_b,
        "source_gram": b, "source_inertia": [17, 1, 1],
        "diagram_involution_images_zero_indexed": sigma_images,
        "diagram_involution": sigma, "bicolored_element": c, "source_isometry": g,
        "primitive_radical": radical, "radical_eigenvalue": -1,
        "quotient_omitted_vertex_zero_indexed": omitted,
        "quotient_projection": projection, "quotient_inclusion": inclusion,
        "quotient_gram": gram, "quotient_gram_determinant": -1,
        "quotient_gram_inertia": [17, 1, 0], "quotient_isometry": a_quotient,
        "left_affine_null": left_null, "right_affine_null": right_null,
        "positive_basis_vertices_zero_indexed": left_roots + right_roots,
        "split_basis": basis, "split_basis_inverse": inverse_basis,
        "split_basis_determinant": determinant(basis), "split_gram": split,
        "e8_gram": k, "e8_leading_principal_minors": [2, 3, 4, 5, 6, 7, 8, 1],
        "positive_gram": h, "positive_isometry": r_positive, "positive_isometry_order": 60,
        "theta": theta, "theta_squared_norm": 2,
        "extended_positive_isometry": r, "e_transvection": e_theta, "f_transvection": f_theta,
        "split_isometry": a, "characteristic_polynomial_ascending": characteristic(a),
        "source_characteristic_polynomial_ascending": full_polynomial,
        "two_transvection_identity_verified": True,
        "status": "verified",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": OUTPUT.relative_to(ROOT).as_posix(),
                      "status": result["status"], "gram_determinant": -1,
                      "positive_isometry_order": 60, "theta_squared_norm": 2,
                      "full_polynomial_preserved": True, "two_transvections": True}, indent=2))


if __name__ == "__main__":
    main()
