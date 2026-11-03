"""Separate exact check of the retained fixed-degree witness, no SymPy import.

The coordinating reviewer wrote this from D9's determinant statement and
literal saved matrix. It does not rerun the authoring random discovery search.
"""
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)


def det_integer(matrix):
    a = [row[:] for row in matrix]
    sign, previous = 1, 1
    for k in range(len(a) - 1):
        pivot_row = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


def determinant_value(v, t):
    return det_integer([[t * v[i][j] + v[j][i] for j in range(len(v))] for i in range(len(v))])


def lehmer_value(t):
    return t**10 + t**9 - t**7 - t**6 - t**5 - t**4 - t**3 + t + 1


def main():
    directory = _J_OUTPUT
    retained = json.loads((directory / "results.json").read_text(encoding="utf-8"))
    v = retained["fixed_degree_growth"]["matrix"]
    n = len(v)
    assert n == 10
    h = [[int(i == j) for j in range(n)] for i in range(n)]
    h[1][1], h[1][2], h[2][1], h[2][2] = 1, -3, 3, -8
    records = []
    for k in range(7):
        assert all(v[i][i] == 1 for i in range(n))
        assert all(v[i][j] == 0 for i in range(n) for j in range(i))
        for t in range(-5, 6):
            assert determinant_value(v, t) == lehmer_value(t)
        energy = sum(v[i][j] ** 2 for i in range(n) for j in range(i + 1, n))
        old = retained["fixed_degree_growth"]["records"][k]
        assert energy == old["energy"]
        assert v[0][1:3] == old["coupling_row"]
        records.append({"k": k, "energy": energy, "coupling_row": v[0][1:3]})
        v = multiply(transpose(h), multiply(v, h))
    result = {"method": "integer Bareiss determinants and constant bilinear congruence", "exact_determinant_checks": 77, "members": records, "scope": "fixed-degree witness only; no full random-search rerun or external source audit"}
    (directory / "review-witness.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
