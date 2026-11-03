"""Check the entire certificate with dense arithmetic and Laurent reconstruction.

This is a second implementation by the same author, not independent agent review.
It does not import main.py or reproduce its subgroup-insertion algorithm.
"""

import json
from pathlib import Path


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def decode(a):
    return [(a >> i) & 1 for i in range(a.bit_length())]


def encode(a):
    return sum(v << i for i, v in enumerate(a))


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] ^= v
    for i, v in enumerate(b):
        c[i] ^= v
    return trim(c)


def divide(a, b):
    a = trim(a)
    q = [0] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        j = len(a) - len(b)
        q[j] = 1
        for k, v in enumerate(b):
            a[j + k] ^= v
        a = trim(a)
    return trim(q), a


def multiply(a, b, modulus=None):
    c = [0] * max(0, len(a) + len(b) - 1)
    for i, v in enumerate(a):
        if v:
            for j, w in enumerate(b):
                c[i + j] ^= w
    c = trim(c)
    return divide(c, modulus)[1] if modulus else c


def powmod(a, n, modulus=None):
    c = [1]
    while n:
        if n % 2:
            c = multiply(c, a, modulus)
        n //= 2
        a = multiply(a, a, modulus)
    return c


def inv(a, modulus):
    # Extended Euclid, separate from main.py's finite exponent inverse.
    old_r, r, old_s, s = modulus, a, [], [1]
    while r:
        q, new_r = divide(old_r, r)
        old_r, r = r, new_r
        old_s, s = s, add(old_s, multiply(q, s))
    assert old_r == [1]
    result = divide(old_s, modulus)[1]
    assert multiply(a, result, modulus) == [1]
    return result


def deriv(a):
    return trim([a[j + 1] if j % 2 == 0 else 0 for j in range(max(0, len(a) - 1))])


def whole_trace(n):
    # Invert the symmetric Laurent expression sum(z^j,-d<=j<=d).
    d = (n - 1) // 2
    remainder = [1] * (d + 1)
    result = [0] * (d + 1)
    for k in range(d, -1, -1):
        if remainder[k]:
            result[k] = 1
            for j in range(k // 2 + 1):
                if j & k == j:
                    remainder[k - 2 * j] ^= 1
    assert not any(remainder)
    return trim(result)


def first_bit(value):
    a = add(value, [1])
    j = 0
    while a:
        a, digit = divide(a, [1, 1, 1])
        if digit:
            assert j > 0
            return 2 * (j - 1) + (0 if digit[0] else 1)
        j += 1
    return None


def expression(exponents, gs, modulus):
    value = [1]
    for e, g in zip(exponents, gs):
        assert 0 <= e < 48
        value = multiply(value, powmod(g, e, modulus), modulus)
    return value


def member(value, group):
    modulus = decode(group["modulus"])
    teich = decode(group["teichmuller"])
    value = divide(value, modulus)[1]
    residue = divide(value, [1, 1, 1])[1]
    r = next(j for j in range(3) if divide(powmod(teich, j, modulus), [1, 1, 1])[1] == residue)
    value = multiply(value, powmod(teich, (-r) % 3, modulus), modulus)
    pivots = {p["bit"]: decode(p["value"]) for p in group["pivots"]}
    count = 0
    while first_bit(value) in pivots:
        bit = first_bit(value)
        value = multiply(value, inv(pivots[bit], modulus), modulus)
        assert first_bit(value) is None or first_bit(value) > bit
        count += 1
        assert count <= 2 * (group["N"] - 1)
    return value == [1], value


def binary_rank(vectors):
    basis = {}
    for vector in vectors:
        v = vector
        while v:
            p = v.bit_length() - 1
            if p not in basis:
                basis[p] = v
                break
            v ^= basis[p]
    return len(basis)


def matrix_product(a, b, modulus):
    return [[add(multiply(a[i][0], b[0][j], modulus),
                 multiply(a[i][1], b[1][j], modulus))
             for j in range(2)] for i in range(2)]


def matrix_power(n, modulus):
    a = [[[0, 1], [1]], [[1], []]]
    c = [[[1], []], [[], [1]]]
    while n:
        if n % 2:
            c = matrix_product(c, a, modulus)
        a = matrix_product(a, a, modulus)
        n //= 2
    return c


def main():
    home = Path(__file__).resolve().parent
    output = home.parents[2] / "computations" / "outputs" / home.name
    data = json.loads((output / "certificate.json").read_text(encoding="utf-8"))
    phi = [1, 1, 1]
    m16 = powmod(phi, 16)
    m17 = powmod(phi, 17)
    identity = [[[1], []], [[], [1]]]
    assert matrix_power(80, m16) == identity
    assert matrix_power(160, m17) == identity
    source = data["source_rows"]
    assert [(r["kind"], r["n"]) for r in source] == (
        [("B", n) for n in range(1, 160, 2) if n % 5]
        + [("D", n) for n in range(5, 320, 10)])
    for row in source:
        b = whole_trace(row["n"])
        if row["kind"] == "D":
            b, remainder = divide(b, phi)
            assert remainder == []
        assert divide(b, phi)[1]
        assert encode(divide(b, m16)[1]) == row["value"]
    for name, group in data["groups"].items():
        N = group["N"]
        modulus = powmod(phi, N)
        assert encode(modulus) == group["modulus"]
        gs = [divide(decode(r["value"]), modulus)[1] for r in source]
        if group["endpoint"]:
            gs.append([0, 1])
        assert [encode(g) for g in gs] == group["generators"]
        teich = powmod([1, 1], N, modulus)
        assert encode(teich) == group["teichmuller"] and powmod(teich, 3, modulus) == [1]
        assert teich != [1]
        bits = []
        for p in group["pivots"]:
            value = decode(p["value"])
            assert first_bit(value) == p["bit"]
            bits.append(p["bit"])
            assert expression(p["exponents"], gs, modulus) == value
            square = multiply(value, value, modulus)
            assert first_bit(square) is None or first_bit(square) > p["bit"]
            assert member(square, group)[0]
        assert bits == sorted(set(bits))
        assert group["order"] == 3 * 2 ** len(bits)
        assert len(bits) <= 2 * (N - 1)
        assert group["insertions"] <= len(gs) + 2 * (N - 1)
        for g in gs:
            assert member(g, group)[0]
    for prefix, test in data["tests"].items():
        small = data["groups"][prefix + "8"]
        large = data["groups"][prefix + "16"]
        vectors = []
        for p in large["pivots"]:
            value = decode(p["value"])
            vectors.append(encode(multiply(deriv(value), inv(value, m16), m16)))
        rank = binary_rank(vectors)
        assert rank == test["dlog_rank"]
        kernel = test["kernel_basis"]
        assert len(kernel) == len(vectors) - rank
        assert binary_rank([r["word"] for r in kernel]) == len(kernel)
        for row in kernel:
            dlog = 0
            value = [1]
            for i, p in enumerate(large["pivots"]):
                if (row["word"] >> i) & 1:
                    dlog ^= vectors[i]
                    value = multiply(value, decode(p["value"]), m16)
            assert dlog == 0 and encode(value) == row["value"]
            assert expression(row["exponents"], [decode(g) for g in large["generators"]], m16) == value
            assert not deriv(value)
            root = trim(value[::2])
            assert encode(root) == row["root"] and multiply(root, root, m16) == value
            flag, residual = member(root, small)
            assert flag == row["root_member"] and encode(residual) == row["root_residual"]
            if flag:
                assert expression(row["root_expression"], [decode(g) for g in small["generators"]], decode(small["modulus"])) == root
        order = 3 * 2 ** (len(vectors) - rank)
        assert order == test["square_intersection_order"]
        assert small["order"] == test["square_prior_order"]
        assert order // small["order"] == test["quotient_order"]
        assert test["saturation"] == (order == small["order"]) == all(r["root_member"] for r in kernel)
        flag, residual = member([0, 0, 1], large)
        assert flag == test["X_squared_member"] and encode(residual) == test["X_squared_residual"]
        if flag:
            assert expression(test["X_squared_expression"], [decode(g) for g in large["generators"]], m16) == [0, 0, 1]
    witness = data["witness"]
    mults = {}
    degree = 0
    value = [1]
    for row in witness["rows"]:
        b = whole_trace(row["n"])
        if row["kind"] == "D":
            b, remainder = divide(b, phi)
            assert not remainder
        degree += row["exponent"] * (len(b) - 1)
        factor = divide(b, m16)[1]
        powered = powmod(factor, row["exponent"], m16)
        assert encode(factor) == row["factor_residue"]
        assert encode(powered) == row["powered_residue"]
        value = multiply(value, powered, m16)
        assert encode(value) == row["partial_product"]
        for d in range(3, row["n"] + 1, 2):
            if row["n"] % d == 0 and d != 5:
                mults[str(d)] = mults.get(str(d), 0) + row["exponent"]
    assert value == [0, 0, 1]
    assert degree == witness["degree"] and mults == witness["complete_group_multiplicities"]
    assert witness["odd_complete_orders"] == sorted(int(d) for d, e in mults.items() if e % 2)
    m8 = powmod(phi, 8)
    x_inverse = inv([0, 1], m8)
    assert encode(x_inverse) == (1 << 15) + (1 << 7)
    assert (x_inverse[13] if len(x_inverse) > 13 else 0) ^ x_inverse[15] == 1
    result = {"result": "verified", "source_rows": 96, "group_certificates": 4,
              "laurent_reconstruction": True, "matrix_periods": [80, 160],
              "orders": {k: g["order"] for k, g in data["groups"].items()},
              "witness_degree": degree, "witness_phi16_residue": encode(value),
              "root_character": 1, "scope": "exact local all-order images only"}
    (output / "verification.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
