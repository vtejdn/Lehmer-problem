"""Exact filtered-group certificate for the declared phi^8/phi^16 question."""

import json
from collections import deque
from pathlib import Path


def divmod_poly(a, b):
    q = 0
    while a.bit_length() >= b.bit_length():
        j = a.bit_length() - b.bit_length()
        q ^= 1 << j
        a ^= b << j
    return q, a


def mul(a, b, modulus=0):
    c = 0
    while b:
        if b & 1:
            c ^= a
        a <<= 1
        b >>= 1
    return divmod_poly(c, modulus)[1] if modulus else c


def power(a, n, modulus=0):
    c = 1
    while n:
        if n & 1:
            c = mul(c, a, modulus)
        a = mul(a, a, modulus)
        n >>= 1
    return c


def derivative(a):
    return sum(((a >> j) & 1) << (j - 1) for j in range(1, a.bit_length(), 2))


def inverse(a, modulus):
    result = power(a, 47, modulus)
    assert mul(a, result, modulus) == 1
    return result


def leading_bit(a):
    """First nonzero bit of a-1 in phi-adic digits with basis 1,X."""
    v = a ^ 1
    j = 0
    while v:
        v, r = divmod_poly(v, 7)
        if r:
            assert j > 0
            return 2 * (j - 1) + (0 if r & 1 else 1)
        j += 1
    return None


def add_vectors(a, b, scale=1):
    return [(x + scale * y) % 48 for x, y in zip(a, b)]


def product_vector(vector, generators, modulus):
    value = 1
    for e, g in zip(vector, generators):
        value = mul(value, power(g, e, modulus), modulus)
    return value


def generators():
    premodulus = power(7, 17)
    previous, current = 1, 3
    values = {1: previous, 3: current}
    for n in range(5, 317, 2):
        previous, current = current, mul(2, current, premodulus) ^ previous
        values[n] = current
    modulus = power(7, 16)
    rows = []
    for n in range(1, 160, 2):
        if n % 5:
            rows.append({"kind": "B", "n": n,
                         "value": divmod_poly(values[n], modulus)[1]})
    for n in range(5, 320, 10):
        q, r = divmod_poly(values[n], 7)
        assert r == 0
        rows.append({"kind": "D", "n": n, "value": q})
    assert len(rows) == 96
    for row in rows:
        assert divmod_poly(row["value"], 7)[1] != 0
    return rows


def subgroup(rows, N, endpoint):
    modulus = power(7, N)
    labels = [{"kind": r["kind"], "n": r["n"]} for r in rows]
    gs = [divmod_poly(r["value"], modulus)[1] for r in rows]
    if endpoint:
        gs.append(2)
        labels.append({"kind": "X", "n": 1})
    width = len(gs)
    b3_index = labels.index({"kind": "B", "n": 3})
    teich = power(3, N, modulus)
    assert power(teich, 3, modulus) == 1 and teich != 1
    residue_exponent = {divmod_poly(power(teich, r, modulus), 7)[1]: r
                        for r in range(3)}
    pivots = {}
    queue = deque()
    events = cancellations = 0
    for i, g in enumerate(gs):
        e = [0] * width
        e[i] = 1
        r = residue_exponent[divmod_poly(g, 7)[1]]
        g = mul(g, power(teich, (-r) % 3, modulus), modulus)
        e[b3_index] = (e[b3_index] - r * N) % 48
        queue.append((g, e))
    while queue:
        u, e = queue.popleft()
        events += 1
        for _ in range(2 * (N - 1) + 1):
            bit = leading_bit(u)
            if bit is None:
                break
            if bit not in pivots:
                pivots[bit] = {"bit": bit, "value": u, "exponents": e}
                queue.append((mul(u, u, modulus), [(2 * v) % 48 for v in e]))
                break
            p = pivots[bit]
            u = mul(u, inverse(p["value"], modulus), modulus)
            e = add_vectors(e, p["exponents"], -1)
            cancellations += 1
        else:
            raise AssertionError("Insertion exceeded its declared filtration bound")
    ordered = [pivots[i] for i in sorted(pivots)]
    assert events <= width + 2 * (N - 1)
    for p in ordered:
        assert product_vector(p["exponents"], gs, modulus) == p["value"]
    result = {"N": N, "endpoint": endpoint, "modulus": modulus,
              "generator_labels": labels, "generators": gs,
              "teichmuller": teich, "teichmuller_exponent": N,
              "b3_index": b3_index, "pivots": ordered,
              "order": 3 * (1 << len(ordered)),
              "insertions": events, "cancellations": cancellations}
    for g in gs:
        assert membership(g, result)[0]
    for p in ordered:
        assert membership(mul(p["value"], p["value"], modulus), result)[0]
    return result


def membership(value, group):
    modulus = group["modulus"]
    teich = group["teichmuller"]
    u = divmod_poly(value, modulus)[1]
    residue = divmod_poly(u, 7)[1]
    r = next(r for r in range(3)
             if divmod_poly(power(teich, r, modulus), 7)[1] == residue)
    u = mul(u, power(teich, (-r) % 3, modulus), modulus)
    exponent = [0] * len(group["generators"])
    exponent[group["b3_index"]] = (r * group["N"]) % 48
    pivots = {p["bit"]: p for p in group["pivots"]}
    for _ in range(2 * (group["N"] - 1) + 1):
        bit = leading_bit(u)
        if bit is None:
            return True, exponent, u
        if bit not in pivots:
            return False, exponent, u
        p = pivots[bit]
        u = mul(u, inverse(p["value"], modulus), modulus)
        exponent = add_vectors(exponent, p["exponents"])
    raise AssertionError("Membership exceeded its bound")


def square_test(small, large):
    modulus = large["modulus"]
    elimination = {}
    kernel = []
    for i, p in enumerate(large["pivots"]):
        v = mul(derivative(p["value"]), inverse(p["value"], modulus), modulus)
        word = 1 << i
        while v:
            b = v.bit_length() - 1
            if b not in elimination:
                elimination[b] = (v, word)
                break
            v ^= elimination[b][0]
            word ^= elimination[b][1]
        if not v:
            kernel.append(word)
    rank = len(elimination)
    root_rows = []
    for word in kernel:
        value = 1
        exponents = [0] * len(large["generators"])
        for i, p in enumerate(large["pivots"]):
            if (word >> i) & 1:
                value = mul(value, p["value"], modulus)
                exponents = add_vectors(exponents, p["exponents"])
        assert derivative(value) == 0
        root = sum(((value >> (2 * i)) & 1) << i for i in range(16))
        assert mul(root, root, modulus) == value
        member, expression, residual = membership(root, small)
        root_rows.append({"word": word, "value": value, "root": root,
                          "exponents": exponents, "root_member": member,
                          "root_expression": expression, "root_residual": residual})
    intersection_order = 3 * (1 << (len(large["pivots"]) - rank))
    assert intersection_order % small["order"] == 0
    equality = intersection_order == small["order"]
    assert equality == all(r["root_member"] for r in root_rows)
    target_member, exponents, residual = membership(4, large)
    return {"dlog_rank": rank, "square_intersection_order": intersection_order,
            "square_prior_order": small["order"],
            "saturation": equality, "quotient_order": intersection_order // small["order"],
            "kernel_basis": root_rows, "X_squared_member": target_member,
            "X_squared_expression": exponents, "X_squared_residual": residual}


def main():
    rows = generators()
    groups = {f"{'E' if endpoint else 'G'}{N}": subgroup(rows, N, endpoint)
              for endpoint in (False, True) for N in (8, 16)}
    tests = {prefix: square_test(groups[prefix + "8"], groups[prefix + "16"])
             for prefix in ("G", "E")}
    witness_rows = []
    multiplicities = {}
    degree = 0
    partial = 1
    for row, exponent in zip(rows, tests["G"]["X_squared_expression"]):
        if not exponent:
            continue
        powered = power(row["value"], exponent, power(7, 16))
        partial = mul(partial, powered, power(7, 16))
        witness_rows.append({"kind": row["kind"], "n": row["n"], "exponent": exponent,
                             "factor_residue": row["value"], "powered_residue": powered,
                             "partial_product": partial})
        degree += exponent * ((row["n"] - 1) // 2 - (2 if row["kind"] == "D" else 0))
        for d in range(3, row["n"] + 1, 2):
            if row["n"] % d == 0 and d != 5:
                multiplicities[d] = multiplicities.get(d, 0) + exponent
    assert tests["G"]["X_squared_member"]
    assert any(e % 2 for e in multiplicities.values())
    data = {"phi": 7, "source_rows": rows, "groups": groups, "tests": tests,
            "witness": {"rows": witness_rows, "degree": degree,
                        "complete_group_multiplicities": multiplicities,
                        "odd_complete_orders": [d for d in sorted(multiplicities) if multiplicities[d] % 2],
                        "endpoint_exponent": 0, "phi16_residue": 4, "unique_phi8_root": 2}}
    group = Path(__file__).resolve().parent
    output = group.parents[2] / "computations" / "outputs" / group.name / "certificate.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output),
                      "orders": {k: v["order"] for k, v in groups.items()},
                      "tests": {k: {x: v[x] for x in ("dlog_rank", "saturation", "quotient_order", "X_squared_member")}
                                for k, v in tests.items()}}, indent=2))


if __name__ == "__main__":
    main()
