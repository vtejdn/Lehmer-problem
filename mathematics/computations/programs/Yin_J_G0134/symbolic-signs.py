"""Exact Laurent expansion for the three-/four-sine sign products.

Run from the repository root:
    python mathematics/computations/programs/Yin_J_G0134/symbolic-signs.py

Uses only integer arithmetic and the Python standard library.
No frequency grid or numerical circle integration occurs.
The mathematical resonance bound is proved separately in Yin_C_G0862_v1.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path
import platform


def add(*terms):
    result = defaultdict(int)
    for scale, polynomial in terms:
        for exponent, coefficient in polynomial.items():
            result[exponent] += scale * coefficient
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def multiply(left, right):
    result = defaultdict(int)
    for a, ca in left.items():
        for b, cb in right.items():
            result[tuple(x + y for x, y in zip(a, b))] += ca * cb
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def orbit_table(polynomial):
    table = {}
    for exponent, coefficient in polynomial.items():
        shape = tuple(sorted(map(abs, exponent), reverse=True))
        entry = table.setdefault(shape, {"coefficient": coefficient, "multiplicity": 0})
        assert entry["coefficient"] == coefficient, (shape, entry, coefficient)
        entry["multiplicity"] += 1
    return [{"shape": list(shape), **table[shape]} for shape in sorted(table)]


def q_numerator(dimension):
    # U_j = 4 sin^2(a_j theta) = 2 - X_j - X_j^-1.
    zero = (0,) * dimension
    u = []
    for j in range(dimension):
        polynomial = {zero: 2}
        for sign in (-1, 1):
            exponent = [0] * dimension
            exponent[j] = sign
            polynomial[tuple(exponent)] = -1
        u.append(polynomial)
    q = add(*[(1, multiply(v, v)) for v in u],
            *[(-2, multiply(u[i], u[j])) for i, j in combinations(range(dimension), 2)])
    # An independently assembled cosine-expression coefficient list.
    expected = {zero: 2 * dimension * (5 - 2 * dimension)}
    # The constant is 16*(3n/8 - n(n-1)/4) = 2n(5-2n).
    for j in range(dimension):
        for sign in (-1, 1):
            for magnitude, coefficient in ((1, 4 * (dimension - 2)), (2, 1)):
                exponent = [0] * dimension
                exponent[j] = sign * magnitude
                expected[tuple(exponent)] = coefficient
    for i, j in combinations(range(dimension), 2):
        for a, b in product((-1, 1), repeat=2):
            exponent = [0] * dimension
            exponent[i], exponent[j] = a, b
            expected[tuple(exponent)] = -2
    assert q == expected
    return q, u


def main():
    q3, _ = q_numerator(3)
    q3_square = multiply(q3, q3)
    expected_orbits = {
        (0, 0, 0): (186, 1), (1, 0, 0): (-104, 6),
        (2, 0, 0): (20, 6), (1, 1, 0): (64, 12),
        (3, 0, 0): (8, 6), (2, 1, 0): (-8, 24),
        (1, 1, 1): (-48, 8), (4, 0, 0): (1, 6),
        (2, 2, 0): (6, 12), (3, 1, 0): (-4, 24),
        (2, 1, 1): (4, 24),
    }
    q3_table = orbit_table(q3_square)
    assert {tuple(r["shape"]): (r["coefficient"], r["multiplicity"])
            for r in q3_table} == expected_orbits
    assert sum(q3_square.values()) == 0  # All U_j vanish at X_j=1.
    q4, u4 = q_numerator(4)
    u_product = {(0, 0, 0, 0): 1}
    for u in u4:
        u_product = multiply(u_product, u)
    d4 = add((1, multiply(q4, q4)), (-64, u_product))
    assert sum(d4.values()) == 0
    generic_d4_second_moment = Fraction(sum(c * c for c in d4.values()), 256**2)
    payload = {
        "runtime": platform.python_version(),
        "arithmetic": "exact Python integers; rational summaries use Fraction",
        "scope": "complete formal Laurent expansion; no frequency tuple enumeration",
        "three": {
            "normalization": "q3=16Q; the table expands q3^2=256Q^2",
            "q3_squared_orbits": q3_table,
            "generic_second_moment": "93/128",
            "proved_resonance_upper_bound_in_draft": "105/128",
            "margin_expression": "log(128/105)/8",
        },
        "four": {
            "normalization": "d4=256D",
            "d4_orbits": orbit_table(d4),
            "generic_second_moment": str(generic_d4_second_moment),
            "limitation": "A generic moment greater than one cannot yield a strict Jensen bound via this second-moment method.",
        },
    }
    group = Path(__file__).resolve().parent
    output = group.parent.parent / "outputs" / group.name / "symbolic-signs.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"three": payload["three"],
                      "four_generic_second_moment": str(generic_d4_second_moment)}, indent=2))


if __name__ == "__main__":
    main()
