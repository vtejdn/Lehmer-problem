"""Exact, single-input trace-lattice and integral-U test; standard library only."""

from fractions import Fraction
from itertools import combinations, product
from math import gcd
from pathlib import Path
import json
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INPUT = HERE.parent / "Yin_J_G0144" / "trace56_cell.json"
OUTPUT = ROOT / "mathematics/computations/outputs/Yin_J_G0158/trace_lattice.json"
SUPPORT_CAP = 4
SEARCH_SECONDS = 20


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def matvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def pairing(g, v, w):
    return sum(x * y for x, y in zip(v, matvec(g, w)))


def determinant(a):
    a = [row[:] for row in a]
    n, previous, sign = len(a), 1, 1
    for k in range(n - 1):
        pivot_row = next((i for i in range(k, n) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def inverse_integral(a):
    n = len(a)
    aug = [[Fraction(x) for x in row + identity(n)[i]] for i, row in enumerate(a)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k])
        aug[k], aug[pivot] = aug[pivot], aug[k]
        scale = aug[k][k]
        aug[k] = [x / scale for x in aug[k]]
        for i in range(n):
            if i != k:
                scale = aug[i][k]
                aug[i] = [x - scale * y for x, y in zip(aug[i], aug[k])]
    result = [row[n:] for row in aug]
    assert all(x.denominator == 1 for row in result for x in row)
    result = [[int(x) for x in row] for row in result]
    assert multiply(a, result) == identity(n)
    assert multiply(result, a) == identity(n)
    return result


def inertia(a):
    """Exact symmetric congruence elimination, including zero diagonal pivots."""
    a = [[Fraction(x) for x in row] for row in a]
    positive = negative = zero = 0
    while a:
        n = len(a)
        pivot = next((i for i in range(n) if a[i][i]), None)
        if pivot is None:
            pair = next(((i, j) for i in range(n) for j in range(i + 1, n) if a[i][j]), None)
            if pair is None:
                zero += n
                break
            i, j = pair
            change = identity(n)
            change[j][i] = 1
            a = multiply(transpose(change), multiply(a, change))
            pivot = i
        order = [pivot] + [i for i in range(n) if i != pivot]
        a = [[a[i][j] for j in order] for i in order]
        diagonal = a[0][0]
        positive += int(diagonal > 0)
        negative += int(diagonal < 0)
        a = [[a[i][j] - a[i][0] * a[0][j] / diagonal for j in range(1, n)] for i in range(1, n)]
    return [positive, negative, zero]


def extended_gcd(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t
    return old_r, old_s, old_t


def row_bezout(row):
    """Return unimodular V with row * V = (gcd(row), 0, ...)."""
    original, row = list(row), list(row)
    n, v = len(row), identity(len(row))
    for j in range(1, n):
        a, b = row[0], row[j]
        if a == b == 0:
            continue
        divisor, p, q = extended_gcd(a, b)
        for i in range(n):
            old0, oldj = v[i][0], v[i][j]
            v[i][0] = p * old0 + q * oldj
            v[i][j] = -(b // divisor) * old0 + (a // divisor) * oldj
        row[0], row[j] = divisor, 0
    if row[0] < 0:
        row[0] = -row[0]
        for i in range(n):
            v[i][0] = -v[i][0]
    assert multiply([original], v) == [row]
    assert abs(determinant(v)) == 1
    return v


def trace_gram(p):
    n = len(p) - 1
    assert p[-1] == p[0] == 1 and p == p[::-1]
    coefficients = list(reversed(p[:-1]))
    powers = [n]
    for k in range(1, n):
        powers.append(-sum(coefficients[j - 1] * powers[k - j] for j in range(1, k)) - k * coefficients[k - 1])
    c = [[0] * n for _ in range(n)]
    for i in range(1, n):
        c[i][i - 1] = 1
    for i in range(n):
        c[i][-1] = -p[i]
    actual_power = identity(n)
    for k in range(n):
        assert sum(actual_power[i][i] for i in range(n)) == powers[k]
        actual_power = multiply(actual_power, c)
    g = [[powers[abs(i - j)] for j in range(n)] for i in range(n)]
    assert multiply(transpose(c), multiply(g, c)) == g
    return c, g, powers


def find_isotropic(g):
    n = len(g)
    started = time.monotonic()
    counts = {str(k): 0 for k in range(1, SUPPORT_CAP + 1)}
    isotropic = 0
    for support in range(1, SUPPORT_CAP + 1):
        for positions in combinations(range(n), support):
            for rest in product((-1, 1), repeat=support - 1):
                if time.monotonic() - started >= SEARCH_SECONDS:
                    return None, {"status": "search_allowance_exhausted", "checked_by_support": counts, "isotropic_seen": isotropic}
                signs = (1,) + rest
                norm = sum(g[i][j] * signs[a] * signs[b] for a, i in enumerate(positions) for b, j in enumerate(positions))
                counts[str(support)] += 1
                if norm:
                    continue
                isotropic += 1
                e = [0] * n
                for i, sign in zip(positions, signs):
                    e[i] = sign
                if gcd(*matvec(g, e)) == 1:
                    return e, {"status": "primitive_divisor_one_witness", "checked_by_support": counts, "isotropic_seen": isotropic}
    return None, {"status": "complete_no_divisor_one_witness_in_finite_set", "checked_by_support": counts, "isotropic_seen": isotropic}


def split_plane(g, c, e):
    n = len(g)
    assert pairing(g, e, e) == 0 and gcd(*matvec(g, e)) == 1
    v = row_bezout(matvec(g, e))
    f0 = [row[0] for row in v]
    assert pairing(g, e, f0) == 1
    e_coordinates = matvec(inverse_integral(v), e)
    assert e_coordinates[0] == 0 and gcd(*e_coordinates[1:]) == 1
    kernel_change = transpose(inverse_integral(row_bezout(e_coordinates[1:])))
    kernel_basis = multiply([row[1:] for row in v], kernel_change)
    assert [row[0] for row in kernel_basis] == e
    f0_norm = pairing(g, f0, f0)
    assert f0_norm % 2 == 0
    f = [x - (f0_norm // 2) * y for x, y in zip(f0, e)]
    columns = []
    for k in transpose(kernel_basis)[1:]:
        coefficient = pairing(g, k, f)
        columns.append([x - coefficient * y for x, y in zip(k, e)])
    basis = transpose(columns + [e, f])
    basis_inverse = inverse_integral(basis)
    split = multiply(transpose(basis), multiply(g, basis))
    h = [row[:n - 2] for row in split[:n - 2]]
    expected = [row + [0, 0] for row in h] + [[0] * (n - 2) + [0, 1], [0] * (n - 2) + [1, 0]]
    assert split == expected
    assert abs(determinant(basis)) == 1
    assert inertia(h) == [n - 2, 0, 0]
    a = multiply(basis_inverse, multiply(c, basis))
    assert multiply(basis, a) == multiply(c, basis)
    assert multiply(transpose(a), multiply(split, a)) == split
    return {"e": e, "f": f, "basis_columns_positive_then_e_f": basis,
            "basis_inverse": basis_inverse, "basis_determinant": determinant(basis),
            "positive_gram": h, "split_gram": split, "conjugated_companion": a,
            "positive_inertia": inertia(h), "full_integer_identity_checks": True}


def main():
    p = json.loads(INPUT.read_text(encoding="utf-8"))["H_ascending"]
    assert p == [1, -1, 1, -1, 0, 0, -1, 1, -1, 1, -1, 1, -1, 0, 0, -1, 1, -1, 1]
    c, g, powers = trace_gram(p)
    signature = inertia(g)
    assert signature == [17, 1, 0]
    assert all(g[i][i] % 2 == 0 for i in range(len(g)))
    e, search = find_isotropic(g)
    result = {"polynomial_ascending": p, "companion": c, "trace_powers_zero_through_17": powers,
              "trace_gram": g, "gram_determinant": determinant(g), "gram_inertia": signature,
              "companion_invariance": True, "gram_even": True,
              "search_support_cap": SUPPORT_CAP, "search_seconds_allowance": SEARCH_SECONDS,
              "search": search, "splitting": split_plane(g, c, e) if e is not None else None}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(result, indent=2) + "\n"
    OUTPUT.write_text(serialized, encoding="utf-8")
    print(json.dumps({"output": OUTPUT.relative_to(ROOT).as_posix(), "gram_determinant": result["gram_determinant"],
                      "trace_powers": powers, "search": search, "e": e,
                      "split": result["splitting"] is not None}, indent=2))


if __name__ == "__main__":
    main()
