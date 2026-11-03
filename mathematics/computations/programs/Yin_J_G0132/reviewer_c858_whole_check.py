"""Independent finite corroboration for fixed C858; Python standard library only.

Run from the repository root:
    python mathematics/computations/programs/Yin_J_G0132/reviewer_c858_whole_check.py

Constructs the degree-82 base and degree-187 empty move word directly from
the fixed integer definitions, using coefficient arithmetic modulo 8.
The monic numerator remainder is formed before its genuine even
coefficients are divided by 2; this determines canonical a modulo 4.
No author program, generated output, exploration draft, or modular inverse
of 2 is used.  These two cases do not prove the quantified theorem.
The separate R finding contains the whole symbolic argument review.
"""

import json


MODULUS = 8


def trim(poly):
    poly = [value % MODULUS for value in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left, right):
    return trim([
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(max(len(left), len(right)))
    ])


def scale(poly, scalar):
    return trim([scalar * value for value in poly])


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % MODULUS
    return trim(result)


def power(poly, exponent):
    result = [1]
    while exponent:
        if exponent & 1:
            result = multiply(result, poly)
        poly = multiply(poly, poly)
        exponent //= 2
    return result


def compose(poly, argument):
    result = [0]
    for value in reversed(poly):
        result = add(multiply(result, argument), [value])
    return result


def remainder(poly, monic):
    assert monic[-1] % MODULUS == 1
    poly = trim(poly[:])
    while len(poly) >= len(monic) and poly != [0]:
        leading = poly[-1]
        offset = len(poly) - len(monic)
        for i, value in enumerate(monic):
            poly[i + offset] = (poly[i + offset] - leading * value) % MODULUS
        poly = trim(poly)
    return poly


def trace_polynomial(n):
    current, following = [2], [0, 1]
    for _ in range(n):
        current, following = following, add([0] + following, scale(current, -1))
    return current


def complete_row(n):
    result = [1]
    for j in range(1, (n + 1) // 2):
        result = add(result, trace_polynomial(j))
    return result


def binary_f_order(poly):
    global MODULUS
    original_modulus = MODULUS
    try:
        MODULUS = 2
        poly = trim(poly[:])
        divisor = [1, 0, 0, 1, 1]
        order = 0
        if poly == [0]:
            return "infinity"
        while remainder(poly, divisor) == [0]:
            quotient = [0] * (len(poly) - 4)
            while len(poly) >= 5:
                leading = poly[-1]
                offset = len(poly) - 5
                quotient[offset] = leading
                for i, value in enumerate(divisor):
                    poly[i + offset] = (poly[i + offset] - leading * value) % 2
                poly = trim(poly)
            poly = trim(quotient)
            order += 1
        return order
    finally:
        MODULUS = original_modulus


def sparse_mod4(poly):
    return [[i, value % 4] for i, value in enumerate(poly) if value % 4]


def main():
    primitive15 = [1, 4, -4, -1, 1]
    primitive5 = [-1, 1, 1]
    primitive480 = compose([1, -4, -4, 1, 1], trace_polynomial(16))
    shared = multiply(power(primitive15, 2), primitive480)
    cofactor = multiply(
        multiply(power([-2, 1], 2), power([1, 1], 2)),
        power(primitive5, 3),
    )
    base = multiply(shared, cofactor)
    rows = {}
    for label, extra in [
        ("base82", [1]),
        ("empty_move187", multiply(power([1, -3, 0, 1], 4), complete_row(187))),
    ]:
        original = multiply(base, extra)
        numerator = remainder(compose(original, trace_polynomial(2)), original)
        assert all(value % 2 == 0 for value in numerator)
        a_mod4 = [value // 2 for value in numerator]
        # Five is its own inverse modulo eight; the actual numerator was
        # first divided by five over Z in the canonical definition.
        c_mod8 = scale(remainder(compose(original, trace_polynomial(5)), original), 5)
        residual = remainder(add(scale(power(c_mod8, 2), 2), scale(power(a_mod4, 5), -3)), original)
        residual_mod4 = [value % 4 for value in residual]
        assert all(value % 2 == 0 for value in residual_mod4)
        rows[label] = {
            "degree": len(original) - 1,
            "F_even": True,
            "F_half_f_order": binary_f_order([value // 2 for value in residual_mod4]),
            "a_f_order": binary_f_order(a_mod4),
            "c_f_order": binary_f_order(c_mod8),
            "G_f_order": binary_f_order(remainder(power(c_mod8, 3), original)),
        }
    assert rows["base82"] == {"degree": 82, "F_even": True, "F_half_f_order": 4, "a_f_order": 4, "c_f_order": 2, "G_f_order": 6}
    assert rows["empty_move187"] == {"degree": 187, "F_even": True, "F_half_f_order": 6, "a_f_order": 4, "c_f_order": 2, "G_f_order": 6}
    expansions = {
        "C16_mod4": sparse_mod4(trace_polynomial(16)),
        "V_mod4": sparse_mod4(primitive480),
        "P16_mod4": sparse_mod4(power(primitive15, 16)),
    }
    assert expansions["C16_mod4"] == [[0, 2], [16, 1]]
    assert expansions["V_mod4"] == [[0, 1], [32, 2], [48, 1], [64, 1]]
    assert expansions["P16_mod4"] == [[0, 1], [24, 2], [32, 2], [48, 1], [56, 2], [64, 1]]
    print(json.dumps({"finite_cases": rows, "expansions": expansions}, indent=2))


if __name__ == "__main__":
    main()
