"""Independent dense-coefficient and Laurent-expansion check of C629/J119.

No author program is imported.  B_n is reconstructed from the Laurent identity,
not its recurrence.  Every assertion concerns a fixed finite identity; the
all-order proof is separately reviewed in the linked R finding.
"""

import argparse
import json
import math
from pathlib import Path
import re


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) ^
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def mul(a, b):
    if not a or not b:
        return []
    p = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            p[i + j] ^= x & y
    return trim(p)


def rem(a, modulus):
    p = trim(a)
    while len(p) >= len(modulus):
        shift = len(p) - len(modulus)
        for i, value in enumerate(modulus):
            p[i + shift] ^= value
        p = trim(p)
    return p


def power(a, n, modulus=None):
    result = [1]
    for _ in range(n):
        result = mul(result, a)
        if modulus is not None:
            result = rem(result, modulus)
    return result


def decode(n):
    return [(n >> i) & 1 for i in range(n.bit_length())]


def encode(p):
    return sum(c << i for i, c in enumerate(p))


def deriv(p):
    return trim([p[i] if i % 2 else 0 for i in range(1, len(p))])


def compose(p, x, modulus):
    out = []
    for i, c in enumerate(p):
        if c:
            out = add(out, power(x, i, modulus))
    return rem(out, modulus)


def trace_from_laurent(n):
    """Triangular inversion of sum(z**j, -m <= j <= m), m=(n-1)/2."""
    m = (n - 1) // 2
    laurent = [1] * n
    polynomial = [0] * (m + 1)
    for degree in range(m, -1, -1):
        if laurent[m + degree]:
            polynomial[degree] = 1
            for j in range(degree + 1):
                laurent[m + degree - 2 * j] ^= math.comb(degree, j) % 2
    assert not any(laurent)
    return trim(polynomial)


def matmul(a, b):
    return [[add(mul(a[i][0], b[0][j]), mul(a[i][1], b[1][j]))
             for j in range(2)] for i in range(2)]


def matadd(a, b):
    return [[add(a[i][j], b[i][j]) for j in range(2)] for i in range(2)]


def scale(a, scalar):
    return [[mul(x, scalar) for x in row] for row in a]


def verify(data, claim):
    one, x, phi = [1], [0, 1], [1, 1, 1]
    primary = power(phi, 8)
    phi6 = power(phi, 6)
    modulus = mul(power(x, 4), primary)
    assert encode(modulus) == 0x101010 and not deriv(modulus)
    identity = [[one, []], [[], one]]
    a = [[x, one], [one, []]]
    matrices = [identity]
    for _ in range(40):
        matrices.append(matmul(matrices[-1], a))
    assert matrices[2] == matadd(scale(a, x), identity)
    assert matadd(matrices[8], identity) == scale(matrices[4], power(x, 4))
    assert matadd(matrices[5], identity) == scale(
        matadd(scale(a, phi), scale(identity, add(x, one))), phi)
    reduced_matrix = [[encode(rem(p, modulus)) for p in row] for row in matrices[40]]
    assert reduced_matrix == [[1, 0], [0, 1]]
    fixed = {"field": "F_2", "phi": 7, "modulus": encode(modulus),
             "dimension": 20, "ambient_unit_count": 393216,
             "odd_order_period": 80, "functional_coefficients": [13, 15],
             "recurrence_matrix_power40": reduced_matrix,
             "result": "both_targets_separated"}
    assert set(data) == set(fixed) | {"generators", "targets"}
    assert all(data[k] == value for k, value in fixed.items())
    orders = [n for n in range(1, 80, 2) if n % 5]
    assert [row["n"] for row in data["generators"]] == orders
    table = [(int(n), int(b, 16), int(d, 16)) for n, b, d in re.findall(
        r"^\| (\d+) \| (0x[0-9a-f]+) \| (0x[0-9a-f]+) \|$", claim, re.M)]
    assert len(table) == 32
    for row, displayed in zip(data["generators"], table):
        b = rem(trace_from_laurent(row["n"]), modulus)
        inverse = power(b, 23, modulus)
        assert rem(mul(b, inverse), modulus) == one
        dlog = rem(mul(deriv(b), inverse), modulus)
        assert rem(mul(b, dlog), modulus) == deriv(b)
        character = (encode(dlog) >> 13 ^ encode(dlog) >> 15) & 1
        assert character == 0
        assert row == {"n": row["n"], "B": encode(b), "inverse": encode(inverse),
                       "dlog": encode(dlog), "character": character}
        assert displayed == (row["n"], encode(b), encode(dlog))
    chi = mul(x, power(phi, 2))
    psi = compose(phi, chi, primary)
    assert [row["epsilon"] for row in data["targets"]] == [0, 1]
    lift_count = 0
    for row in data["targets"]:
        eps = row["epsilon"]
        local = add(x, mul(power(phi, 4), power(x, 7)) if eps else [])
        local = rem(local, primary)
        candidates = [add(local, mul(primary, decode(q))) for q in range(16)]
        candidates = [p for p in candidates if rem(p, power(x, 4)) == decode(5)]
        assert len(candidates) == 1
        target = candidates[0]
        h, v = rem(mul(power(x, 2), target), primary), rem(mul(power(x, 5), target), primary)
        c = rem(mul(power(x, 2), mul(compose(target, chi, primary), power(psi, 14, primary))), primary)
        assert c == power(x, 2)
        root_rhs = rem(mul(h, power(c, 2, primary)), primary)
        z = power(root_rhs, 11, primary)
        assert power(z, 11, primary) == root_rhs
        correction = rem(mul(mul(h, v), mul(power(x, 4),
                         mul(power(add(x, one), 8), power(phi, 4)))), primary) if eps else []
        difference = add(v, power(c, 3, primary))
        assert not rem(add(mul(z, difference), correction), primary)
        assert not add(power(h, 6, primary), power(c, 21, primary))
        root6 = rem(z, phi6)
        for q in range(16):
            lifted = add(root6, mul(phi6, decode(q)))
            assert power(lifted, 11, phi6) == rem(root_rhs, phi6)
            assert not rem(add(mul(lifted, difference), correction), primary)
            lift_count += 1
        inverse = power(target, 23, modulus)
        assert rem(mul(target, inverse), modulus) == one
        dlog = rem(mul(deriv(target), inverse), modulus)
        assert encode(dlog) == 0x8080
        expected = {"epsilon": eps, "Y": encode(target), "Y_phi": encode(local),
                    "inverse": encode(inverse), "dlog": encode(dlog), "character": 1,
                    "C": encode(c), "Z": encode(z), "gate_remainder": 0,
                    "old_support_remainder": 0}
        assert row == expected
    return {"verified": True, "method": "dense_coefficients_and_direct_Laurent_expansion",
            "generator_count": 32, "target_count": 2, "root_lifts_checked": lift_count,
            "claim_table_rows_checked": 32, "polynomial_matrix_identities_checked": 3,
            "result": "both_targets_separated"}


if __name__ == "__main__":
    group = Path(__file__).resolve().parent
    mathematics = group.parents[2]
    output_home = mathematics / "computations" / "outputs" / group.name
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=output_home / "certificate.json")
    parser.add_argument("--output", type=Path, default=output_home / "independent_verification.json")
    parser.add_argument("--claim", type=Path, default=mathematics / "claims" / "Yin_C_G0608_v1.md")
    args = parser.parse_args()
    report = verify(json.loads(args.input.read_text(encoding="utf-8")),
                    args.claim.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report))
