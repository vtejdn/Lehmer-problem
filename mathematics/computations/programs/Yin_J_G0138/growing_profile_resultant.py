"""Exact whole-measure lower bound for one growing neutral-profile input.

The fixed input is A=Phi_60*Phi_84*Phi_140 and
P=A*(1+z+...+z^922)-z^505, of degree 1010.
For m=2053, R=abs(Res(P,z^m-1)) satisfies
R <= 2^1010*M(P)^m, including all factors and multiplicities.
The program checks R*4^m > 2^1010*11^m, proving M(P)>11/4.

An exact reciprocal-trace calculation separately checks
R=P(1)*Res(B_1026,Q)^2, with P=z^505 Q(z+1/z) and
z^1026 B_1026(z+1/z)=(z^2053-1)/(z-1).
Both resultants rely on the same trusted python-flint/FLINT backend;
this is an author control, not an independent implementation review.
No factorization, root isolation, random sampling or previous output is used.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import platform
import tempfile

import flint
from flint import fmpz_poly


def integer_coefficients(poly: fmpz_poly) -> list[int]:
    return [int(coefficient) for coefficient in poly]


def reciprocal_trace(poly: fmpz_poly) -> fmpz_poly:
    degree = poly.degree()
    assert degree % 2 == 0
    coefficients = integer_coefficients(poly)
    assert coefficients == coefficients[::-1]
    half = degree // 2
    t = fmpz_poly([0, 1])
    previous, current = fmpz_poly([2]), t
    trace = fmpz_poly([poly[half]])
    for index in range(1, half + 1):
        trace += poly[half + index] * current
        previous, current = current, t * current - previous

    # Reconstruct the Laurent lift by direct binomial expansion.
    from math import comb

    lifted = [0] * (degree + 1)
    for index, coefficient in enumerate(trace):
        for selected in range(index + 1):
            lifted[half + index - 2 * selected] += int(coefficient) * comb(
                index, selected
            )
    assert lifted == coefficients
    return trace


def odd_grid_trace(index: int) -> fmpz_poly:
    assert index >= 1
    t = fmpz_poly([0, 1])
    previous, current = fmpz_poly([1]), t + 1
    for _ in range(2, index + 1):
        previous, current = current, t * current - previous
    return current


def calculate() -> dict:
    orders = [60, 84, 140]
    neutral = fmpz_poly([1])
    for order in orders:
        neutral *= fmpz_poly.cyclotomic(order)
    assert neutral.degree() == 88
    assert neutral(1) == neutral(-1) == 1
    assert integer_coefficients(neutral)[:4] == [1, 0, 3, 0]

    r, center, power = 923, 505, 2053
    polynomial = neutral * fmpz_poly([1] * r) - fmpz_poly([0] * center + [1])
    degree = polynomial.degree()
    assert degree == 1010
    assert polynomial[0] == polynomial[degree] == 1
    assert polynomial(1) == 922 and polynomial(-1) == 2
    assert integer_coefficients(polynomial)[:4] == [1, 1, 4, 4]
    prefix_difference = fmpz_poly([1, -1]) * polynomial - neutral
    assert all(prefix_difference[index] == 0 for index in range(505))

    trace = reciprocal_trace(polynomial)
    assert trace.degree() == center
    test_polynomial = fmpz_poly([-1] + [0] * (power - 1) + [1])
    resultant = abs(polynomial.resultant(test_polynomial))
    grid = odd_grid_trace((power - 1) // 2)
    trace_resultant = grid.resultant(trace)
    assert resultant == polynomial(1) * trace_resultant * trace_resultant
    assert resultant > 0

    lower_numerator, lower_denominator = 11, 4
    left = resultant * lower_denominator**power
    right = 2**degree * lower_numerator**power
    assert left > right

    # This is only a conditional upper bound: the input fails its sign premise.
    match_length, reference_degree_sum = 504, 89
    q = match_length // 2
    upper_base = 8 * q + reference_degree_sum + 3
    assert upper_base == 2108 and q == 252
    assert upper_base * 5**126 < 6**126

    return {
        "input": {
            "cyclotomic_orders": orders,
            "r": r,
            "central_exponent": center,
            "neutral_coefficients_ascending": integer_coefficients(neutral),
            "polynomial_coefficients_ascending": integer_coefficients(polynomial),
            "trace_coefficients_ascending": integer_coefficients(trace),
        },
        "resultant_certificate": {
            "power": power,
            "polynomial_degree": degree,
            "absolute_resultant": str(resultant),
            "resultant_bit_length": resultant.bit_length(),
            "trace_resultant": str(trace_resultant),
            "trace_grid_degree": grid.degree(),
            "reciprocal_resultant_identity": True,
            "strict_integer_comparison": True,
            "whole_measure_strict_lower_bound": {
                "numerator": lower_numerator,
                "denominator": lower_denominator,
            },
        },
        "conditional_prefix_comparison": {
            "matching_length": match_length,
            "reference_total_degree": reference_degree_sum,
            "q": q,
            "upper_base": upper_base,
            "upper_exponent_numerator": 1,
            "upper_exponent_denominator": 126,
            "conditional_upper_is_below_6_over_5": True,
            "strict_sign_premise_verified_by_program": False,
        },
        "scope": {
            "whole_original_polynomial": True,
            "proper_factor_measures_determined": False,
            "independent_review": False,
        },
        "versions": {"python": platform.python_version(), "python_flint": flint.__version__},
    }


def main() -> None:
    result = calculate()
    group = Path(__file__).resolve().parent
    output_directory = group.parents[1] / "outputs" / group.name
    output_directory.mkdir(parents=True, exist_ok=True)
    output_path = output_directory / "growing_profile_resultant.json"
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=output_directory, delete=False
        ) as stream:
            temporary_path = Path(stream.name)
            json.dump(result, stream, indent=2)
            stream.write("\n")
        os.replace(temporary_path, output_path)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()
    print(json.dumps({
        "output": str(output_path),
        "degree": result["resultant_certificate"]["polynomial_degree"],
        "resultant_bits": result["resultant_certificate"]["resultant_bit_length"],
        "whole_measure": "> 11/4",
        "trace_identity": True,
    }))


if __name__ == "__main__":
    main()
