"""Primitive nine-position signed rows at a quartic Salem unit and its square."""

import json
import runpy
from math import gcd
from pathlib import Path


GROUP = Path(__file__).resolve().parents[2]
BASE = runpy.run_path(str(GROUP / "minimum.py"))
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name / "versions" / "v5" / "results.json"
P = (1, -1, -1, -1, 1)
P2 = (1, -3, 1, -3, 1)


def multiply(f, g):
    product = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            product[i + j] += a * b
    return product


def remainder(poly, modulus):
    """Integer long division by a monic polynomial, with ascending coefficients."""
    r = poly.copy()
    for degree in range(len(r) - 1, len(modulus) - 2, -1):
        leading = r.pop()
        if leading:
            offset = degree + 1 - len(modulus)
            for j, coefficient in enumerate(modulus[:-1]):
                r[offset + j] -= leading * coefficient
    return r


def check_row(n, width, sign, omitted, row):
    assert gcd(*row) == 1
    assert all(bool(a) == (j != omitted) for j, a in enumerate(row))
    numerator = [0] * (n * width + 1)
    graph = [0] * (n * width + 2)
    for j, a in enumerate(row):
        numerator[n * j] = a
        graph[n * j] += a
        graph[n * (width - j) + 1] += sign * a
    for factor in (P, P2):
        assert not any(remainder(graph, multiply(factor, factor)))
        assert any(remainder(numerator, factor))


def records(n, width):
    _, kernels = BASE["row_system"](multiply(P, P2), n, width)
    for sign, basis in zip((1, -1), kernels):
        assert len(basis) == width - 7
        for omitted in ([None] if width == 8 else range(width + 1)):
            if omitted is not None:
                u, v = basis
                row = [v[omitted] * a - u[omitted] * b for a, b in zip(u, v)]
            else:
                row, = basis
            content = gcd(*row)
            assert content
            if next(a for a in row if a) < 0:
                content = -content
            row = [a // content for a in row]
            check_row(n, width, sign, omitted, row)
            yield dict(n=n, width=width, sign=sign, omitted=omitted, coefficients=row,
                       one_norm=sum(map(abs, row)))


if __name__ == "__main__":
    rows = [r for n in (16, 32, 64, 128) for width in (8, 9) for r in records(n, width)]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(f"Checked {len(rows)} primitive rows. Wrote {OUTPUT}")
