"""Independent fixed-input check for the changed neutral profile.

Reconstruct cyclotomic factors using elementary binomial quotients, and form
the trace as C_A*B_461-1 rather than importing the author's full-P trace code.
Python integers check every coefficient, quotient, lift and final inequality.
The full exact trace resultant still trusts python-flint/FLINT; two fixed
prime-field Euclidean controls below do not certify that implementation.
No parent search, factorization, root approximation or sampling is performed.
"""

from __future__ import annotations

import json
from math import comb, gcd, isqrt
from pathlib import Path
import platform

import flint
from flint import fmpz_poly


def trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def multiply(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    out[i + j] += ai * bj
    return trim(out)


def subtract(a: list[int], b: list[int]) -> list[int]:
    out = a[:] + [0] * max(0, len(b) - len(a))
    for i, bi in enumerate(b):
        out[i] -= bi
    return trim(out)


def monic_divmod(a: list[int], b: list[int]) -> tuple[list[int], list[int]]:
    assert b[-1] == 1
    work = a[:]
    quotient = [0] * max(1, len(a) - len(b) + 1)
    for top in range(len(a) - 1, len(b) - 2, -1):
        coefficient = work[top]
        shift = top - len(b) + 1
        quotient[shift] = coefficient
        for j, bj in enumerate(b):
            work[shift + j] -= coefficient * bj
    return trim(quotient), trim(work)


def one_minus_power(k: int) -> list[int]:
    return [1] + [0] * (k - 1) + [-1]


def factor_four_uv(u: int, v: int) -> list[int]:
    numerator = multiply(one_minus_power(u * v), one_minus_power(1))
    denominator = multiply(one_minus_power(u), one_minus_power(v))
    quotient, remainder = monic_divmod(numerator, denominator)
    assert remainder == [0]
    assert multiply(quotient, denominator) == numerator
    out = [0] * (2 * len(quotient) - 1)
    for j, coefficient in enumerate(quotient):
        out[2 * j] = coefficient * (-1) ** j
    return out


def trace_by_triangular_subtraction(poly: list[int]) -> list[int]:
    assert len(poly) % 2 == 1 and poly == poly[::-1]
    half = (len(poly) - 1) // 2
    remainder = poly[:]
    trace = [0] * (half + 1)
    for degree in range(half, -1, -1):
        coefficient = remainder[half + degree]
        trace[degree] = coefficient
        for chosen in range(degree + 1):
            remainder[half + degree - 2 * chosen] -= coefficient * comb(degree, chosen)
    assert all(value == 0 for value in remainder)
    return trim(trace)


def lift(trace: list[int], half: int) -> list[int]:
    out = [0] * (2 * half + 1)
    for degree, coefficient in enumerate(trace):
        for chosen in range(degree + 1):
            out[half + degree - 2 * chosen] += coefficient * comb(degree, chosen)
    return trim(out)


def e_polynomial(k: int) -> list[int]:
    out = [0] * (k + 1)
    for j in range(k // 2 + 1):
        out[k - 2 * j] = (-1) ** j * comb(k - j, j)
    return out


def grid(k: int) -> list[int]:
    if k == 0:
        return [1]
    return subtract(e_polynomial(k), [-x for x in e_polynomial(k - 1)])


def evaluate(poly: list[int], x: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = result * x + coefficient
    return result


def modular_resultant(first: list[int], second: list[int], prime: int) -> int:
    """Euclidean resultant recurrence over one explicitly fixed prime field."""
    assert all(prime % k for k in range(2, isqrt(prime) + 1))
    f = trim([x % prime for x in first])
    g = trim([x % prime for x in second])
    value = 1
    while len(g) > 1:
        m, n = len(f) - 1, len(g) - 1
        inverse = pow(g[-1], -1, prime)
        remainder = f[:]
        for top in range(m, n - 1, -1):
            scale = remainder[top] * inverse % prime
            if scale:
                shift = top - n
                for j, coefficient in enumerate(g):
                    remainder[shift + j] = (remainder[shift + j] - scale * coefficient) % prime
        trim(remainder)
        if remainder == [0]:
            return 0
        factor = pow(g[-1], m - (len(remainder) - 1), prime)
        if (m * n) % 2:
            factor = -factor
        value = value * factor % prime
        f, g = g, remainder
    return value * pow(g[0], len(f) - 1, prime) % prime


def mobius(k: int) -> int:
    signs = 0
    divisor = 2
    while divisor * divisor <= k:
        if k % divisor == 0:
            k //= divisor
            signs += 1
            if k % divisor == 0:
                return 0
            while k % divisor == 0:
                k //= divisor
        divisor += 1
    if k > 1:
        signs += 1
    return (-1) ** signs


def calculate() -> dict:
    group = Path(__file__).resolve().parents[1]
    output_directory = group.parent.parent / "outputs" / group.name
    author_path = output_directory / "growing_profile_resultant.json"
    author = json.loads(author_path.read_text(encoding="utf-8"))
    orders = [60, 84, 140]
    factors = [factor_four_uv(3, 5), factor_four_uv(3, 7), factor_four_uv(5, 7)]
    assert [len(f) - 1 for f in factors] == [16, 24, 48]
    neutral = multiply(multiply(factors[0], factors[1]), factors[2])
    assert neutral[:6] == [1, 0, 3, 0, 3, 0]
    assert len(neutral) == 89 and neutral == neutral[::-1]
    assert evaluate(neutral, 1) == evaluate(neutral, -1) == 1
    polynomial = multiply(neutral, [1] * 923)
    polynomial[505] -= 1
    assert len(polynomial) == 1011 and polynomial[0] == polynomial[-1] == 1
    assert polynomial == polynomial[::-1]
    assert polynomial[:5] == [1, 1, 4, 4, 7]
    assert evaluate(polynomial, 1) == 922 and evaluate(polynomial, -1) == 2
    difference = subtract(multiply([1, -1], polynomial), neutral)
    assert all(x == 0 for x in difference[:505]) and difference[505] == -1

    neutral_trace = trace_by_triangular_subtraction(neutral)
    trace = multiply(neutral_trace, grid(461))
    trace[0] -= 1
    assert len(trace) == 506
    assert lift(trace, 505) == polynomial
    assert trace_by_triangular_subtraction(polynomial) == trace
    quotient, residual = monic_divmod(trace, grid(504))
    assert quotient == [0, 1] and len(residual) <= 504
    assert evaluate(trace, -2) == -2 and evaluate(grid(504), -2) == 1

    # The full odd-grid coefficient identity reconstructs all canonical a_i.
    baseline = multiply([1, 0, 1], one_minus_power(1009))
    coordinate_difference = subtract(multiply([1, -1], polynomial), baseline)
    coordinates = coordinate_difference[2:506]
    assert len(coordinates) == 504 and coordinates[:2] == [2, 0]
    remainder_check = [0]
    for i, coefficient in enumerate(coordinates):
        if coefficient:
            remainder_check = subtract(remainder_check, [-coefficient * x for x in grid(503 - i)])
    assert remainder_check == residual

    # Independently synthesized C_A*B_461-1 and binomial B_1026 enter FLINT.
    trace_resultant = int(fmpz_poly(trace).resultant(fmpz_poly(grid(1026))))
    # 505*1026 is even, so reversing the resultant's argument order changes no sign.
    resultant = 922 * trace_resultant**2
    assert resultant > 0 and resultant.bit_length() == 4030
    original = author["input"]
    assert original["cyclotomic_orders"] == orders
    assert original["r"] == 923 and original["central_exponent"] == 505
    assert original["neutral_coefficients_ascending"] == neutral
    assert original["polynomial_coefficients_ascending"] == polynomial
    assert original["trace_coefficients_ascending"] == trace
    certificate = author["resultant_certificate"]
    assert certificate["power"] == 2053 and certificate["polynomial_degree"] == 1010
    assert int(certificate["absolute_resultant"]) == resultant
    assert int(certificate["trace_resultant"]) == trace_resultant
    assert certificate["resultant_bit_length"] == 4030 and certificate["trace_grid_degree"] == 1026
    assert certificate["whole_measure_strict_lower_bound"] == {"numerator": 11, "denominator": 4}
    assert certificate["reciprocal_resultant_identity"] is True
    assert certificate["strict_integer_comparison"] is True
    lower_margin = resultant * 4**2053 - 2**1010 * 11**2053
    upper_margin = 6**126 - 2108 * 5**126
    assert lower_margin > 0 and upper_margin > 0
    assert author["conditional_prefix_comparison"] == {
        "matching_length": 504,
        "reference_total_degree": 89,
        "q": 252,
        "upper_base": 2108,
        "upper_exponent_numerator": 1,
        "upper_exponent_denominator": 126,
        "conditional_upper_is_below_6_over_5": True,
        "strict_sign_premise_verified_by_program": False,
    }
    assert author["scope"] == {
        "whole_original_polynomial": True,
        "proper_factor_measures_determined": False,
        "independent_review": False,
    }

    test = [-1] + [0] * 2052 + [1]
    modular_controls = []
    for prime in (1000003, 1000033):
        residue = modular_resultant(polynomial, test, prime)
        assert residue == resultant % prime
        modular_controls.append({"prime": prime, "resultant_residue": residue})

    phase_controls = []
    for index in (9, 11, 504):
        root_count = sum(
            1 for order in orders for a in range(1, (order - 1) // 2 + 1)
            if gcd(a, order) == 1 and 1009 * a < order * index
        )
        mobius_count = sum(
            mobius(divisor) * ((order * index - 1) // (1009 * divisor))
            for order in orders for divisor in range(1, order + 1) if order % divisor == 0
        )
        assert root_count == mobius_count
        exponent = root_count + (86 * index) // 1009
        sign = (-1) ** exponent
        assert sign == (-1 if index in (9, 11) else 1)
        assert 1009 // gcd(1009, index) not in orders
        assert 86 * index % 1009 != 0
        phase_controls.append({"index": index, "crossed_trace_roots": root_count, "sine_parity_floor": (86 * index) // 1009, "sign_W": sign})

    return {
        "input": {"orders": orders, "r": 923, "center": 505, "p": 1009, "n": 504,
                  "neutral_coefficients_ascending": neutral,
                  "polynomial_coefficients_ascending": polynomial,
                  "trace_coefficients_ascending": trace,
                  "canonical_coordinates": coordinates},
        "exact_checks": {"author_payload_matches": True, "trace_quotient": quotient,
                         "trace_remainder_degree": len(residual) - 1,
                         "prefix_matching_length": 504, "first_mismatch_index": 505,
                         "endpoint_ratio": -2,
                         "absolute_resultant": str(resultant), "trace_resultant": str(trace_resultant),
                         "resultant_bit_length": resultant.bit_length(),
                         "strict_lower_comparison_margin": str(lower_margin),
                         "strict_upper_comparison_margin": str(upper_margin)},
        "modular_controls": modular_controls,
        "phase_controls": phase_controls,
        "limits": {"trusted_full_resultant_backend": "python-flint/FLINT", "backend_implementation_verified": False,
                   "modular_controls_certify_full_integer": False, "proper_factor_measures_determined": False,
                   "parent_search_or_sampling": False},
        "versions": {"python": platform.python_version(), "python_flint": flint.__version__},
    }


def main() -> None:
    result = calculate()
    group = Path(__file__).resolve().parents[1]
    output_directory = group.parent.parent / "outputs" / group.name
    output_directory.mkdir(parents=True, exist_ok=True)
    output = output_directory / "growing_profile_independent.json"
    # Publish only a completed check, leaving the author certificate untouched.
    temporary = output.with_suffix(".json.part")
    try:
        temporary.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        temporary.replace(output)
    finally:
        if temporary.exists():
            temporary.unlink()
    print(json.dumps({"output": str(output), "resultant_bits": 4030,
                      "lower_bound": "M(P)>11/4", "author_payload_matches": True,
                      "modular_controls": result["modular_controls"],
                      "phase_controls": result["phase_controls"]}))


if __name__ == "__main__":
    main()
