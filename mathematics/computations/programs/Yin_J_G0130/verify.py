"""Separate dense/Laurent author checker for the fixed A0=16 certificate.

No main.py import, no recurrence generation, and no subgroup insertion.
This is a second author implementation, not independent agent review.
No arithmetic starts on import or without --execute.
"""
import argparse
import json
from math import gcd
import os
from pathlib import Path
import time

PHI = [1, 1, 1]
DIM = 157
ROW_COUNT = 640
P64 = MODULUS = PRE = None
_deadline = None
_whole_cache = {}


def check_budget():
    if _deadline is not None and time.monotonic() > _deadline:
        raise TimeoutError("Declared live deadline exceeded; no new verification published")


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def decode(a):
    assert isinstance(a, int) and a >= 0
    return [(a >> i) & 1 for i in range(a.bit_length())]


def encode(a):
    assert all(v in (0, 1) for v in a)
    return sum(v << i for i, v in enumerate(a))


def add(a, b):
    result = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        result[i] ^= value
    for i, value in enumerate(b):
        result[i] ^= value
    return trim(result)


def divide(a, b):
    check_budget()
    a, b = trim(a), trim(b)
    assert b
    support = [i for i, value in enumerate(b) if value]
    quotient = [0] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        j = len(a) - len(b)
        quotient[j] = 1
        for k in support:
            a[j + k] ^= 1
        a = trim(a)
    return trim(quotient), a


def multiply(a, b, modulus=None):
    check_budget()
    if not a or not b:
        return []
    # The integer digit base exceeds every possible convolution coefficient.
    # No coefficient can carry to its neighbour; parity yields the F2 product.
    width = (min(len(a), len(b)) + 1).bit_length()
    aa = sum(value << (width * i) for i, value in enumerate(a) if value)
    bb = sum(value << (width * i) for i, value in enumerate(b) if value)
    packed = aa * bb
    result = trim([(packed >> (width * i)) & 1 for i in range(len(a) + len(b) - 1)])
    return divide(result, modulus)[1] if modulus is not None else result


def powmod(a, n, modulus=None):
    assert n >= 0
    result = [1]
    while n:
        if n % 2:
            result = multiply(result, a, modulus)
        a = multiply(a, a, modulus)
        n //= 2
    return result


def inv(a, modulus):
    # Euclid, entirely separate from the generator's finite-exponent inverse.
    old_r, r, old_s, s = list(modulus), list(a), [], [1]
    while r:
        quotient, new_r = divide(old_r, r)
        old_r, r = r, new_r
        old_s, s = s, add(old_s, multiply(quotient, s))
    assert old_r == [1]
    result = divide(old_s, modulus)[1]
    assert multiply(a, result, modulus) == [1]
    return result


def initialize():
    global P64, MODULUS, PRE
    P64 = powmod(PHI, 64)
    MODULUS = [0] * 32 + P64
    PRE = [0] * 32 + powmod(PHI, 65)
    assert len(MODULUS) == 161 and len(PRE) == 163


def whole_trace(n):
    """Invert the complete symmetric Laurent polynomial, without B recurrence."""
    assert isinstance(n, int) and 1 <= n <= 3835 and n % 2
    if n in _whole_cache:
        return list(_whole_cache[n])
    degree = (n - 1) // 2
    remainder = [1] * (degree + 1)  # nonnegative Laurent coefficients
    result = [0] * (degree + 1)
    for k in range(degree, -1, -1):
        check_budget()
        if remainder[k]:
            result[k] = 1
            # Binary Frobenius expansion of (z+z^-1)^k.
            j = k
            while True:
                if 2 * j <= k:
                    remainder[k - 2 * j] ^= 1
                if j == 0:
                    break
                j = (j - 1) & k
    assert not any(remainder)
    value = trim(result)
    assert len(value) == degree + 1 and value[0] == 1
    _whole_cache[n] = tuple(value)
    return value


def compose(a, b):
    result = []
    for coefficient in reversed(a):
        result = multiply(result, b)
        if coefficient:
            result = add(result, [1])
    return result


def first_bit(value):
    assert value and value[0] == 1 and divide(value, PHI)[1] == [1]
    low = add(value[:32], [1])
    if low:
        assert low[0] == 0
        return next(i - 1 for i in range(1, len(low)) if low[i])
    remainder = add(divide(value, P64)[1], [1])
    j = 0
    while remainder:
        remainder, digit = divide(remainder, PHI)
        if digit:
            assert 1 <= j <= 63
            return 31 + 2 * (j - 1) + (0 if digit[0] else 1)
        j += 1
    return None


def matrix_product(a, b, modulus):
    return [[add(multiply(a[i][0], b[0][j], modulus),
                 multiply(a[i][1], b[1][j], modulus))
             for j in range(2)] for i in range(2)]


def matrix_power(n, modulus):
    a = [[[0, 1], [1]], [[1], []]]
    result = [[[1], []], [[], [1]]]
    while n:
        if n % 2:
            result = matrix_product(result, a, modulus)
        a = matrix_product(a, a, modulus)
        n //= 2
    return result


def generator_squares(generators):
    answer = []
    for g in generators:
        row = [g]
        for _ in range(7):
            row.append(multiply(row[-1], row[-1], MODULUS))
        answer.append(row)
    return answer


def expression(exponents, squares):
    assert len(exponents) == len(squares) == ROW_COUNT
    result = [1]
    for exponent, row in zip(exponents, squares):
        assert isinstance(exponent, int) and 0 <= exponent < 192
        for j in range(8):
            if exponent & (1 << j):
                result = multiply(result, row[j], MODULUS)
    return result


def reduce_member(value, teich, pivots, inverses):
    residue = divide(value, PHI)[1]
    j = next(j for j in range(3) if divide(powmod(teich, j, MODULUS), PHI)[1] == residue)
    value = multiply(value, powmod(teich, (-j) % 3, MODULUS), MODULUS)
    trace = []
    bit = first_bit(value)
    while bit is not None and bit in pivots:
        value = multiply(value, inverses[bit], MODULUS)
        trace.append(bit)
        next_bit = first_bit(value)
        assert next_bit is None or next_bit > bit
        bit = next_bit
        assert len(trace) <= DIM
    return value, bit, trace


def exact_targets():
    x = [0, 1]
    x32 = [0] * 32 + [1]
    low = [1] + [0] * 15 + [1]
    primary0 = powmod(x, 8, P64)
    correction = multiply(powmod(x, 24, P64),
                          multiply(powmod([1, 1], 64, P64), powmod(PHI, 32, P64), P64), P64)
    assert correction
    targets = []
    for epsilon in (0, 1):
        primary = add(primary0, correction) if epsilon else primary0
        # Recombine from the LOW component, unlike main.py's high-component CRT.
        adjustment = multiply(inv(x32, P64), add(primary, divide(low, P64)[1]), P64)
        full = add(low, multiply(x32, adjustment))
        assert len(full) < len(MODULUS)
        assert divide(full, x32)[1] == low and divide(full, P64)[1] == primary
        targets.append((low, primary, full))
    assert targets[0][2] != targets[1][2]
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
    home = Path(__file__).resolve().parent
    output = home.parents[2] / "computations" / "outputs" / home.name
    certificate = output / "certificate.json"
    if not certificate.is_file():
        raise FileNotFoundError("Verification requires this J's actual certificate.json")
    if certificate.stat().st_size > 64 * 1024 * 1024:
        raise ValueError("Certificate exceeds the declared 64 MiB verification input cap")
    data = json.loads(certificate.read_text(encoding="utf-8"))
    initialize()
    assert data["schema"] == "full-a16-membership-v1"
    assert data["phi"] == encode(PHI) and data["M"] == encode(MODULUS)
    assert data["predivision_M"] == encode(PRE)
    assert data["exponent"] == 192 and data["ambient_order"] == 3 * 2 ** DIM
    assert data["matrix_period"] == 640 and data["odd_index_period"] == 1280
    assert data["scope"] == "Only two HC6 eta=0 targets; no positive witness construction"
    identity = [[[1], []], [[], [1]]]
    assert matrix_power(640, MODULUS) == matrix_power(640, PRE) == identity
    expected = [("B", n) for n in range(1, 1280, 2) if n % 5]
    expected += [("D", 5 * r) for r in range(1, 256, 2)]
    rows = data["rows"]
    assert len(rows) == ROW_COUNT and [(r["kind"], r["n"]) for r in rows] == expected
    chi = multiply([0, 1], powmod(PHI, 2))
    generators = []
    for row in rows:
        n, m = row["n"], row["m"]
        original, lifted = whole_trace(n), whole_trace(m)
        pre_original = divide(original, PRE)[1]
        pre_lifted = divide(lifted, PRE)[1]
        assert pre_original == pre_lifted
        assert encode(pre_original) == row["pre_original"]
        assert encode(pre_lifted) == row["pre_representative"]
        if row["kind"] == "B":
            assert m == (n if n % 3 else n + 1280) and m <= 2559 and gcd(m, 15) == 1
            reduced = divide(original, MODULUS)[1]
        else:
            r = n // 5
            k = next(k for k in range(3) if gcd(r + 256 * k, 15) == 1)
            ell = r + 256 * k
            assert row["r"] == r and row["k"] == k and row["ell"] == ell
            assert m == 5 * ell and ell <= 767 and m <= 3835
            original, remainder = divide(original, PHI)
            lifted, remainder_lift = divide(lifted, PHI)
            divided_pre, remainder_pre = divide(pre_original, PHI)
            assert not remainder and not remainder_lift and not remainder_pre
            assert lifted == compose(whole_trace(ell), chi)
            # Check exact quotient AFTER whole PRE reduction against whole division.
            reduced = divide(original, MODULUS)[1]
            assert divided_pre == reduced
        assert divide(lifted, MODULUS)[1] == reduced
        assert encode(reduced) == row["value"]
        assert reduced and reduced[0] == 1 and divide(reduced, PHI)[1]
        assert powmod(reduced, 192, MODULUS) == [1]
        generators.append(reduced)
    group = data["group"]
    assert group["modulus"] == data["M"]
    assert group["generators"] == [encode(g) for g in generators]
    b3 = next(i for i, row in enumerate(rows) if row["kind"] == "B" and row["n"] == 3)
    assert group["b3_index"] == b3 and generators[b3] == [1, 1]
    teich = powmod([1, 1], 64, MODULUS)
    assert powmod(generators[b3], 64, MODULUS) == teich
    assert encode(teich) == group["teichmuller"] and trim(teich[:32]) == [1]
    assert powmod(teich, 3, MODULUS) == [1] and teich != [1]
    bits = [p["bit"] for p in group["pivots"]]
    assert bits == sorted(set(bits)) and all(0 <= bit < DIM for bit in bits)
    assert len(bits) <= DIM and group["order"] == 3 * 2 ** len(bits)
    assert group["insertions"] == ROW_COUNT + len(bits) <= 797
    assert 0 <= group["cancellations"] <= 797 * DIM
    squares = generator_squares(generators)
    pivots = {p["bit"]: decode(p["value"]) for p in group["pivots"]}
    inverses = {bit: inv(value, MODULUS) for bit, value in pivots.items()}
    assert len(group["square_reductions"]) == len(bits)
    for pivot, closure in zip(group["pivots"], group["square_reductions"]):
        value = decode(pivot["value"])
        assert len(value) < len(MODULUS)
        assert first_bit(value) == pivot["bit"]
        assert expression(pivot["exponents"], squares) == value
        remainder, bit, trace = reduce_member(multiply(value, value, MODULUS), teich, pivots, inverses)
        assert remainder == [1] and bit is None
        assert closure == {"bit": pivot["bit"], "trace": trace, "residual": 1}
    assert len(group["source_reductions"]) == ROW_COUNT
    for i, generator in enumerate(generators):
        remainder, bit, trace = reduce_member(generator, teich, pivots, inverses)
        assert remainder == [1] and bit is None
        assert group["source_reductions"][i] == {"index": i, "trace": trace, "residual": 1}
    summaries = []
    assert len(data["targets"]) == 2
    total_target_steps = 0
    for epsilon, ((low, primary, expected_value), target) in enumerate(zip(exact_targets(), data["targets"])):
        assert target["epsilon"] == epsilon
        value = decode(target["target"])
        assert value == expected_value
        assert target["low_X"] == encode(low) and target["phi_primary"] == encode(primary)
        remainder, bit, trace = reduce_member(value, teich, pivots, inverses)
        assert encode(remainder) == target["residual"] and bit == target["first_missing_bit"]
        assert trace == target["trace"] and target["member"] == (remainder == [1])
        assert multiply(expression(target["expression"], squares), remainder, MODULUS) == value
        total_target_steps += len(trace)
        summaries.append({"epsilon": epsilon, "member": target["member"], "first_missing_bit": bit,
                          "full_CRT": True, "complete_vector_product_identity": True})
    assert total_target_steps <= 314
    result = {"verified": True, "reconstructed_rows": ROW_COUNT,
              "matrix_periods": [640, 640], "odd_index_periods": [1280, 1280],
              "pivot_expressions": len(bits), "pivot_square_closures": len(bits),
              "source_reductions": ROW_COUNT, "group_order": group["order"],
              "ambient_index": data["ambient_order"] // group["order"], "targets": summaries,
              "scope": "Fixed two-target certificate only; no positive or original witness construction"}
    publish_json(output / "verification.json", result)
    print(json.dumps(result, indent=2))


def main():
    global _deadline
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true", help="Explicitly verify this J's fixed mathematical certificate")
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
