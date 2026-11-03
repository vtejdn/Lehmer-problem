"""Exact A0=16 two-target membership generator; see README for execution evidence.

Adapted from J129's author bit-polynomial/normal-form mechanism.
No arithmetic starts on import or without the explicit --execute flag.
Only the fixed X^32 phi^64 contract in this J is accepted.
"""
import argparse
from collections import deque
import json
import os
from pathlib import Path
import time

PHI = 7
EXP = 192
ROW_COUNT = 640
DIM = 157
MAX_SOURCE = 3835
P64 = M = PRE = LOW = None
_deadline = None


def check_budget():
    if _deadline is not None and time.monotonic() > _deadline:
        raise TimeoutError("Declared live deadline exceeded; no new certificate published")


def divmod_poly(a, b):
    assert isinstance(a, int) and a >= 0 and isinstance(b, int) and b > 0
    q = 0
    while a.bit_length() >= b.bit_length():
        j = a.bit_length() - b.bit_length()
        q ^= 1 << j
        a ^= b << j
    return q, a


def mul(a, b, modulus=0):
    check_budget()
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return divmod_poly(result, modulus)[1] if modulus else result


def power(a, n, modulus=0):
    assert n >= 0
    result = 1
    while n:
        if n & 1:
            result = mul(result, a, modulus)
        a = mul(a, a, modulus)
        n >>= 1
    return result


def initialize():
    global P64, M, PRE, LOW
    P64 = power(PHI, 64)
    M = P64 << 32
    PRE = power(PHI, 65) << 32
    LOW = (1 << 32) - 1
    assert M.bit_length() == 161 and PRE.bit_length() == 163


def inverse(a, modulus):
    # EXP=192 is deliberately forbidden as an inverse exponent in PRE.
    assert modulus in (M, P64, 1 << 32)
    result = power(a, EXP - 1, modulus)
    assert mul(a, result, modulus) == 1
    return result


def leading_bit(a):
    assert a & 1 and divmod_poly(a, PHI)[1] == 1
    low = (a ^ 1) & LOW
    if low:
        return (low & -low).bit_length() - 2
    value = divmod_poly(a, P64)[1] ^ 1
    j = 0
    while value:
        value, digit = divmod_poly(value, PHI)
        if digit:
            assert 1 <= j <= 63
            return 31 + 2 * (j - 1) + (0 if digit & 1 else 1)
        j += 1
    return None


def add_vectors(a, b, sign=1):
    assert len(a) == len(b) == ROW_COUNT
    return [(x + sign * y) % EXP for x, y in zip(a, b)]


def product_vector(exponents, generators):
    assert len(exponents) == len(generators) == ROW_COUNT
    result = 1
    for e, g in zip(exponents, generators):
        assert isinstance(e, int) and 0 <= e < EXP
        result = mul(result, power(g, e, M), M)
    return result


def matrix_product(a, b, modulus):
    return [[mul(a[i][0], b[0][j], modulus) ^ mul(a[i][1], b[1][j], modulus)
             for j in range(2)] for i in range(2)]


def matrix_power(n, modulus):
    a = [[2, 1], [1, 0]]
    result = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            result = matrix_product(result, a, modulus)
        a = matrix_product(a, a, modulus)
        n >>= 1
    return result


def source_rows():
    # Intermediate recurrence terms are deterministic dependencies, not extra tests.
    previous, current = 1, 3
    values = {1: previous, 3: current}
    for n in range(5, MAX_SOURCE + 1, 2):
        previous, current = current, mul(2, current, PRE) ^ previous
        values[n] = current
    assert matrix_power(640, M) == matrix_power(640, PRE) == [[1, 0], [0, 1]]
    rows = []
    for n in range(1, 1280, 2):
        if n % 5:
            m = n if n % 3 else n + 1280
            assert m <= 2559 and m % 3 and m % 5
            assert values[n] == values[m]
            rows.append({"kind": "B", "n": n, "m": m,
                         "pre_original": values[n], "pre_representative": values[m],
                         "value": divmod_poly(values[n], M)[1]})
    assert len(rows) == 512
    for r in range(1, 256, 2):
        n = 5 * r
        k = next(k for k in range(3) if (r + 256 * k) % 3 and (r + 256 * k) % 5)
        ell = r + 256 * k
        m = 5 * ell
        assert ell <= 767 and m <= MAX_SOURCE and values[n] == values[m]
        value, remainder = divmod_poly(values[n], PHI)
        lifted, remainder_lift = divmod_poly(values[m], PHI)
        assert remainder == remainder_lift == 0 and value == lifted
        assert value.bit_length() <= 160
        rows.append({"kind": "D", "n": n, "r": r, "k": k, "ell": ell, "m": m,
                     "pre_original": values[n], "pre_representative": values[m],
                     "value": value})
    assert len(rows) == ROW_COUNT
    for row in rows:
        value = row["value"]
        assert value & 1 and divmod_poly(value, PHI)[1] != 0
        assert power(value, EXP, M) == 1
    return rows


def membership(value, group):
    assert 0 <= value < (1 << 160) and value & 1
    teich = group["teichmuller"]
    residue = divmod_poly(value, PHI)[1]
    r = next(i for i in range(3) if divmod_poly(power(teich, i, M), PHI)[1] == residue)
    u = mul(value, power(teich, (-r) % 3, M), M)
    trace = []
    expression = [0] * ROW_COUNT
    expression[group["b3_index"]] = 64 * r
    pivots = {p["bit"]: p for p in group["pivots"]}
    for _ in range(DIM + 1):
        bit = leading_bit(u)
        if bit is None or bit not in pivots:
            return {"member": bit is None, "expression": expression,
                    "residual": u, "first_missing_bit": bit, "trace": trace}
        p = pivots[bit]
        trace.append(bit)
        u = mul(u, inverse(p["value"], M), M)
        expression = add_vectors(expression, p["exponents"])
        next_bit = leading_bit(u)
        assert next_bit is None or next_bit > bit
    raise AssertionError("Target cancellation bound exceeded")


def subgroup(rows):
    generators = [row["value"] for row in rows]
    b3 = next(i for i, row in enumerate(rows) if row["kind"] == "B" and row["n"] == 3)
    teich = power(3, 64, M)
    assert generators[b3] == 3 and power(generators[b3], 64, M) == teich
    assert teich & LOW == 1 and power(teich, 3, M) == 1 and teich != 1
    residues = {divmod_poly(power(teich, j, M), PHI)[1]: j for j in range(3)}
    queue = deque()
    for i, g in enumerate(generators):
        r = residues[divmod_poly(g, PHI)[1]]
        e = [0] * ROW_COUNT
        e[i] = 1
        e[b3] = (e[b3] - 64 * r) % EXP
        queue.append((mul(g, power(teich, (-r) % 3, M), M), e))
    pivots = {}
    events = cancellations = 0
    while queue:
        check_budget()
        u, e = queue.popleft()
        events += 1
        assert events <= ROW_COUNT + DIM
        for _ in range(DIM + 1):
            bit = leading_bit(u)
            if bit is None:
                break
            assert 0 <= bit < DIM
            if bit not in pivots:
                pivots[bit] = {"bit": bit, "value": u, "exponents": e}
                queue.append((mul(u, u, M), [(2 * v) % EXP for v in e]))
                break
            pivot = pivots[bit]
            u = mul(u, inverse(pivot["value"], M), M)
            e = add_vectors(e, pivot["exponents"], -1)
            cancellations += 1
            next_bit = leading_bit(u)
            assert next_bit is None or next_bit > bit
        else:
            raise AssertionError("Insertion filtration bound exceeded")
    assert len(pivots) <= DIM and events == ROW_COUNT + len(pivots)
    assert cancellations <= (ROW_COUNT + DIM) * DIM
    group = {"modulus": M, "generators": generators, "teichmuller": teich,
             "b3_index": b3, "pivots": [pivots[b] for b in sorted(pivots)],
             "insertions": events, "cancellations": cancellations,
             "order": 3 * 2 ** len(pivots)}
    square_checks = []
    for p in group["pivots"]:
        assert product_vector(p["exponents"], generators) == p["value"]
        result = membership(mul(p["value"], p["value"], M), group)
        assert result["member"] and result["residual"] == 1
        square_checks.append({"bit": p["bit"], "trace": result["trace"], "residual": 1})
    source_checks = []
    for i, g in enumerate(generators):
        result = membership(g, group)
        assert result["member"] and result["residual"] == 1
        source_checks.append({"index": i, "trace": result["trace"], "residual": 1})
    group["square_reductions"] = square_checks
    group["source_reductions"] = source_checks
    return group


def full_targets():
    low = 1 ^ (1 << 16)
    base = power(2, 8, P64)
    correction = mul(power(2, 24, P64),
                     mul(power(3, 64, P64), power(PHI, 32, P64), P64), P64)
    assert correction != 0
    targets = []
    for epsilon in (0, 1):
        primary = base ^ (correction if epsilon else 0)
        adjustment = mul(inverse(P64, 1 << 32), low ^ (primary & LOW), 1 << 32)
        target = primary ^ mul(P64, adjustment)
        assert target.bit_length() <= 160
        assert target & LOW == low and divmod_poly(target, P64)[1] == primary
        targets.append({"epsilon": epsilon, "target": target,
                        "low_X": low, "phi_primary": primary})
    assert targets[0]["target"] != targets[1]["target"]
    return targets


def publish_json(path, data):
    check_budget()
    payload = json.dumps(data, indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_name(path.stem + ".pending.json")
    try:
        with pending.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        check_budget()
        os.replace(pending, path)
    finally:
        if pending.exists():
            pending.unlink()


def run():
    initialize()
    rows = source_rows()
    group = subgroup(rows)
    targets = []
    for item in full_targets():
        result = membership(item["target"], group)
        result.update(item)
        assert len(result["trace"]) <= DIM
        assert mul(product_vector(result["expression"], group["generators"]),
                   result["residual"], M) == result["target"]
        targets.append(result)
    assert sum(len(t["trace"]) for t in targets) <= 314
    home = Path(__file__).resolve().parent
    output = home.parents[2] / "computations" / "outputs" / home.name
    data = {"schema": "full-a16-membership-v1", "phi": PHI, "M": M,
            "predivision_M": PRE, "ambient_order": 3 * 2 ** DIM, "exponent": EXP,
            "matrix_period": 640, "odd_index_period": 1280,
            "rows": rows, "group": group, "targets": targets,
            "scope": "Only two HC6 eta=0 targets; no positive witness construction"}
    publish_json(output / "certificate.json", data)
    print(json.dumps({"complete": True, "rows": len(rows), "pivots": len(group["pivots"]),
                      "order": group["order"], "index": data["ambient_order"] // group["order"],
                      "targets": [{k: t[k] for k in ("epsilon", "member", "first_missing_bit", "residual")}
                                  for t in targets]}, indent=2))


def main():
    global _deadline
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true", help="Explicitly execute the fixed mathematical contract")
    parser.add_argument("--max-seconds", type=int, default=1800)
    args = parser.parse_args()
    if not args.execute:
        parser.error("Prepared only: --execute is required after the responsible instruction")
    if not 1 <= args.max_seconds <= 7200:
        parser.error("--max-seconds must be between 1 and 7200")
    if not __debug__:
        raise RuntimeError("Optimized Python would disable certificate assertions")
    _deadline = time.monotonic() + args.max_seconds
    run()


if __name__ == "__main__":
    main()
