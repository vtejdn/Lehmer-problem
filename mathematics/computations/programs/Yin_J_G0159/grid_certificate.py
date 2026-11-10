"""Validated grid-polynomial obstruction, independent of the numerical LP.

The exact integer root-index list is the certificate input. No LP output,
floating trigonometry, NumPy or HiGHS is used by this checker.
"""

import json
from pathlib import Path

from flint import arb, ctx

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
P, N, PREFIX_DEGREE = 401, 200, 138
ROOT_INDICES = [
    1, 3, 4, 6, 7, 9, 10, 11, 12, 14, 15, 17, 18, 20, 21,
    23, 24, 26, 27, 29, 30, 32, 33, 34, 35, 37, 38, 40, 41,
    43, 44, 46, 47, 49, 50, 52, 53, 55, 56, 57, 58, 60, 61,
    63, 64, 66, 67, 69, 70, 72, 73, 75, 76, 78, 79, 80, 81,
    83, 84, 86, 87, 89, 90, 92, 93, 95, 96, 98, 99, 100, 101,
    103, 104, 106, 107, 109, 110, 112, 113, 115, 116, 118, 119,
    121, 122, 123, 124, 126, 127, 129, 130, 132, 133, 135, 136,
    138, 139, 141, 142, 144, 145, 146, 147, 149, 150, 152, 153,
    155, 156, 158, 159, 161, 162, 164, 165, 167, 168, 169, 170,
    172, 173, 175, 176, 178, 179, 181, 182, 184, 185, 187, 188,
    190, 191, 193, 194, 196, 197, 199,
]


def calculate():
    ctx.prec = 512
    ctx.threads = 1
    assert ROOT_INDICES == sorted(set(ROOT_INDICES))
    assert len(ROOT_INDICES) == PREFIX_DEGREE
    assert all(1 <= index <= N for index in ROOT_INDICES)
    zeros = set(ROOT_INDICES)
    # b_j strictly decreases with j. This proves all exact nonzero signs.
    sign_checks = []
    for j in range(1, N + 1):
        if j in zeros:
            sign = 0
        else:
            sign = -((-1) ** sum(index < j for index in ROOT_INDICES))
        assert sign == 0 or sign == (1 if j < N else -1)
        sign_checks.append(sign)
    assert sign_checks[-1] == -1

    angles = {j: 2 * arb.pi() * j / P for j in range(1, N + 1)}
    nodes = {j: 2 * angle.cos() for j, angle in angles.items()}
    functional = arb(0)
    terms = []
    for j in range(1, N + 1):
        if j in zeros:
            # This is an exact algebraic zero, not an interval approximation.
            continue
        value = arb(-1)
        for index in ROOT_INDICES:
            value *= nodes[j] - nodes[index]
        assert sign_checks[j - 1] * value > 0
        theta = angles[j]
        fixed_sine = 2 * theta.sin()
        for i in range(2, PREFIX_DEGREE + 1, 2):
            fixed_sine += 4 * ((i + 1) * theta).sin()
        # nu_j G(b_j) h_fixed(b_j) = 4 sin(theta_j) G(b_j) S_fixed / p.
        term = 4 * theta.sin() * value * fixed_sine / P
        functional += term
        terms.append({"node": j, "G_ball": str(value), "functional_term_ball": str(term)})
    assert arb(-56) < functional < arb(-55)
    return {"p": P, "n": N, "prefix_degree": PREFIX_DEGREE,
            "root_indices": ROOT_INDICES, "polynomial_leading_sign": -1,
            "precision_bits": 512, "exact_grid_signs": sign_checks,
            "fixed_prefix_functional_ball": str(functional),
            "rational_enclosure": [-56, -55],
            "functional_strictly_negative": bool(functional < 0),
            "nonzero_terms": terms,
            "scope": "strict one-negative-node real cell excluded; no endpoint or integrality premise"}


def main():
    result = calculate()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    path = OUTPUT / "grid_certificate.json"
    pending = path.with_suffix(".json.part")
    pending.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    pending.replace(path)
    print(json.dumps({key: result[key] for key in ("p", "prefix_degree", "fixed_prefix_functional_ball", "functional_strictly_negative")}))


if __name__ == "__main__":
    main()
