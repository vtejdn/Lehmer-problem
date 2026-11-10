"""Independent exact-dyadic check of C881 v5's fixed conductor-401 certificate.

Run with Python 3.14, standard library only, from the repository root:
    python -B mathematics/computations/programs/Yin_J_G0159/checks/grid_polynomial_independent.py
To compare the actual author output, additionally pass:
    --author-output mathematics/computations/outputs/Yin_J_G0159/grid_certificate.json

This program does not import or execute the author program, use Arb, or evaluate the author's 62-term sine functional.
It expands G in the monomial basis and uses integral t^(2r) d(alpha) = binomial(2r,r) to enclose integral t^2 G d(alpha).
Its U list is the nonzero-index list in the fixed Claim; its complement is compared with the author program's literal root list using AST inspection.

All intervals have exact integer endpoints divided by 2**BITS.
Multiplication and positive integer division round outward.
Pi uses the exact Machin identity 16 atan(1/5) - 4 atan(1/239), with rational alternating-series remainders.
Cosine uses its degree-300 Taylor polynomial and the uniform remainder 4**302 / 302!, since every angle has absolute value below 4.
Decimal text is display only; all comparisons and certified endpoints use integers/Fractions.

The default output is outputs/Yin_J_G0159/grid_independent.json.
The optional author output is a declared comparison input, not an oracle for the enclosure.
The mathematical scope is only this fixed real-cell exclusion.
"""

import argparse
import ast
from decimal import Decimal, localcontext
from fractions import Fraction
import json
from math import comb, factorial
from pathlib import Path
import re
import sys


J_HOME = Path(__file__).resolve().parents[1]
OUTPUT = J_HOME.parent.parent / "outputs" / J_HOME.name / "grid_independent.json"
BITS = 1024
SCALE = 1 << BITS
P, N, DEGREE = 401, 200, 138
NONZERO_INDICES = [
    2, 5, 8, 13, 16, 19, 22, 25, 28, 31, 36, 39, 42, 45, 48,
    51, 54, 59, 62, 65, 68, 71, 74, 77, 82, 85, 88, 91, 94,
    97, 102, 105, 108, 111, 114, 117, 120, 125, 128, 131, 134,
    137, 140, 143, 148, 151, 154, 157, 160, 163, 166, 171, 174,
    177, 180, 183, 186, 189, 192, 195, 198, 200,
]


def ceil_div(a, b):
    assert b > 0
    return -((-a) // b)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[1], -x[0]


def mul(x, y):
    values = [a * b for a in x for b in y]
    return min(values) // SCALE, ceil_div(max(values), SCALE)


def times(x, integer):
    if integer < 0:
        return neg(times(x, -integer))
    return x[0] * integer, x[1] * integer


def divide(x, integer):
    assert integer > 0
    return x[0] // integer, ceil_div(x[1], integer)


def dyadic_bounds(lo, hi):
    assert lo <= hi
    return (lo.numerator * SCALE // lo.denominator,
            ceil_div(hi.numerator * SCALE, hi.denominator))


def atan_reciprocal(q, terms):
    partial = sum((Fraction((-1) ** k, (2 * k + 1) * q ** (2 * k + 1))
                   for k in range(terms)), Fraction(0))
    following = Fraction((-1) ** terms, (2 * terms + 1) * q ** (2 * terms + 1))
    return min(partial, partial + following), max(partial, partial + following)


def pi_interval():
    a = atan_reciprocal(5, 250)
    b = atan_reciprocal(239, 70)
    result = dyadic_bounds(16 * a[0] - 4 * b[1], 16 * a[1] - 4 * b[0])
    assert result[0] > 3 * SCALE and 7 * result[1] < 22 * SCALE
    return result


def cosine(x):
    assert 0 <= x[0] <= x[1] < 4 * SCALE
    square = mul(x, x)
    term = total = (SCALE, SCALE)
    for k in range(1, 151):
        term = divide(mul(term, square), (2 * k - 1) * (2 * k))
        total = add(total, neg(term) if k % 2 else term)
    remainder = ceil_div(4 ** 302 * SCALE, factorial(302))
    return total[0] - remainder, total[1] + remainder


def decimal_display(value):
    with localcontext() as context:
        context.prec = 80
        return str(Decimal(value) / Decimal(SCALE))


def parse_ball(text):
    match = re.fullmatch(r"\[([+\-0-9.eE]+) \+/- ([+\-0-9.eE]+)\]", text)
    assert match is not None
    midpoint, radius = map(Fraction, match.groups())
    assert radius >= 0
    return midpoint - radius, midpoint + radius, radius


def calculate(author_output=None):
    assert NONZERO_INDICES == sorted(set(NONZERO_INDICES))
    assert len(NONZERO_INDICES) == 62
    nonzeros = set(NONZERO_INDICES)
    roots = [j for j in range(1, N + 1) if j not in nonzeros]
    assert len(roots) == DEGREE
    source = ast.parse((J_HOME / "grid_certificate.py").read_text(encoding="utf-8"))
    author_roots = [ast.literal_eval(node.value) for node in source.body
                    if isinstance(node, ast.Assign)
                    and any(isinstance(target, ast.Name) and target.id == "ROOT_INDICES"
                            for target in node.targets)]
    assert author_roots == [roots]
    signs = [0 if j not in nonzeros else -((-1) ** sum(i < j for i in roots))
             for j in range(1, N + 1)]
    assert all(signs[j - 1] == (1 if j < N else -1) for j in NONZERO_INDICES)

    pi = pi_interval()
    nodes = {j: times(cosine(divide(times(pi, 2 * j), P)), 2)
             for j in range(1, N + 1)}
    assert all(nodes[j][0] > nodes[j + 1][1] for j in range(1, N))
    coefficients = [(-SCALE, -SCALE)]
    for j in roots:
        new = [(0, 0)] * (len(coefficients) + 1)
        for degree, coefficient in enumerate(coefficients):
            new[degree] = add(new[degree], neg(mul(nodes[j], coefficient)))
            new[degree + 1] = add(new[degree + 1], coefficient)
        coefficients = new
    assert len(coefficients) == DEGREE + 1
    assert coefficients[-1] == (-SCALE, -SCALE)

    functional = (0, 0)
    for degree in range(0, DEGREE + 1, 2):
        moment = comb(degree + 2, (degree + 2) // 2)
        functional = add(functional, times(coefficients[degree], moment))
    assert -56 * SCALE < functional[0] <= functional[1] < -55 * SCALE

    comparison = None
    if author_output is not None:
        author = json.loads(author_output.read_text(encoding="utf-8"))
        assert (author["p"], author["n"], author["prefix_degree"]) == (P, N, DEGREE)
        assert author["root_indices"] == roots
        assert author["polynomial_leading_sign"] == -1
        assert author["exact_grid_signs"] == signs
        assert author["precision_bits"] == 512
        assert author["rational_enclosure"] == [-56, -55]
        assert author["functional_strictly_negative"] is True
        assert [term["node"] for term in author["nonzero_terms"]] == NONZERO_INDICES
        lo, hi, radius = parse_ball(author["fixed_prefix_functional_ball"])
        assert lo <= Fraction(functional[0], SCALE)
        assert Fraction(functional[1], SCALE) <= hi
        assert radius < Fraction("7e-148")
        comparison = {"mathematical_inputs_and_signs_match": True,
                      "independent_interval_inside_author_functional_ball": True,
                      "author_displayed_radius_below_7e_minus148": True,
                      "individual_author_term_balls_recomputed": False}

    return {"p": P, "n": N, "degree_G": DEGREE,
            "method": "exact dyadic monomial coefficients and exact arcsine moments",
            "python": sys.version.split()[0], "external_libraries": [],
            "bits": BITS, "pi_series_terms": {"atan_1_over_5": 250, "atan_1_over_239": 70},
            "cosine_degree": 300, "nonzero_indices": NONZERO_INDICES,
            "root_list_matches_fixed_author_program": True,
            "all_exact_grid_signs_verified": True,
            "functional_lower_numerator": str(functional[0]),
            "functional_upper_numerator": str(functional[1]),
            "functional_denominator_power_of_two": BITS,
            "functional_lower_decimal_display": decimal_display(functional[0]),
            "functional_upper_decimal_display": decimal_display(functional[1]),
            "functional_width_decimal_display": decimal_display(functional[1] - functional[0]),
            "strict_rational_enclosure": [-56, -55],
            "author_output_comparison": comparison,
            "scope": "fixed p401 one-negative-node degree138 real-cell certificate only"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--author-output", type=Path)
    args = parser.parse_args()
    result = calculate(args.author_output)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pending = OUTPUT.with_suffix(".json.part")
    pending.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    pending.replace(OUTPUT)
    print(json.dumps({key: result[key] for key in (
        "strict_rational_enclosure", "functional_lower_decimal_display",
        "functional_width_decimal_display", "author_output_comparison")}, indent=2))


if __name__ == "__main__":
    main()
