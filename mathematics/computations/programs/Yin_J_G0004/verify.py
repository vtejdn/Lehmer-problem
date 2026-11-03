"""Independent exact SymPy verification of the adjacent Rouche certificate.

Does not import main.py.  The Taylor coefficients are computed by a Gaussian-
rational polynomial shift, and every retained arithmetic quantity is compared
as a rational value rather than as bytes or prose metadata.
"""

import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

import sympy as sp


HERE = _J_OUTPUT
data = json.loads((HERE / "result.json").read_text(encoding="utf-8"))
t = sp.symbols("t")
q_expression = t**24 - t**17 - t**12 - t**7 + 1
p_expression = (t**22 + t**21 - t**19 - t**18 + t**16 - t**14 - t**13
                + t**11 - t**9 - t**8 + t**6 - t**4 - t**3 + t + 1)
assert sp.expand(sp.cyclotomic_poly(6, t) * p_expression) == q_expression
q = sp.Poly(q_expression, t, domain=sp.QQ_I)
assert data["q_coefficients_ascending"] == [int(q.nth(j)) for j in range(25)]

center_parts = [sp.Rational(value) for value in data["disk_center"]]
assert center_parts == [sp.Rational(-94095, 100000), sp.Rational(-52062, 100000)]
center = center_parts[0] + sp.I * center_parts[1]
radius = sp.Rational(data["disk_radius"])
assert radius == sp.Rational(1, 100000) > 0
assert all(abs(part) > radius for part in center_parts)

# Poly.shift uses exact polynomial translation over the Gaussian rationals;
# it does not reuse the original program's binomial coefficient summation.
shifted = q.shift(center)
assert shifted.degree() == 24
coefficients = [tuple(map(sp.Rational, sp.expand_complex(shifted.nth(j)).as_real_imag()))
                for j in range(25)]
retained_coefficients = [tuple(sp.Rational(part) for part in row)
                         for row in data["taylor_coefficients_ascending"]]
assert len(retained_coefficients) == 25
assert coefficients == retained_coefficients
assert shifted.nth(1) == q.diff().eval(center)


def l1(pair):
    return abs(pair[0]) + abs(pair[1])


constant_upper = l1(coefficients[0])
tail_upper = sum(l1(coefficients[k]) * radius**k for k in range(2, 25))
linear_lower = max(abs(part) for part in coefficients[1]) * radius
assert constant_upper == sp.Rational(data["constant_upper_l1"])
assert tail_upper == sp.Rational(data["higher_tail_upper_l1"])
assert linear_lower == sp.Rational(data["linear_boundary_lower"])
assert constant_upper + tail_upper < linear_lower
assert data["strict_rouche_inequality"] is True

# These optional shorter rational brackets make the strict comparison
# directly legible without rounding the retained long rational values.
assert constant_upper + tail_upper < sp.Rational(19, 100000)
assert linear_lower > sp.Rational(31, 100000)

modulus_squared_lower = sum((abs(part) - radius)**2 for part in center_parts)
assert modulus_squared_lower == sp.Rational(data["root_modulus_squared_lower"])
assert modulus_squared_lower == (sp.Rational(94094, 100000)**2
                                 + sp.Rational(52061, 100000)**2)
assert modulus_squared_lower > 1
# The disk avoids the real axis and is disjoint from its conjugate disk.
assert abs(center_parts[1]) > radius

lambda_lower = sp.Rational(data["positive_root_lower"])
assert lambda_lower == sp.Rational(2727, 2500) > 1
q_at_lambda_lower = sp.Poly(q_expression, t, domain=sp.ZZ).eval(lambda_lower)
assert q_at_lambda_lower == sp.Rational(data["q_at_positive_root_lower"])
assert q_at_lambda_lower < 0

mahler_lower = lambda_lower * modulus_squared_lower
assert mahler_lower == sp.Rational(data["mahler_strict_lower"])
assert mahler_lower == sp.Rational(31535105874939, 25000000000000)
cube_gap = mahler_lower**3 - 2
assert cube_gap == sp.Rational(data["mahler_lower_cubed_minus_two"])
assert cube_gap > 0

out = {
    "status": "passed",
    "input": "result.json",
    "arithmetic": "exact integers, rationals and Gaussian rationals",
    "independent_method": "Gaussian-rational Poly.shift; no import of main.py",
    "q_equals_Phi6_times_p22": True,
    "taylor_coefficients_checked": len(coefficients),
    "constant_and_tail_upper": str(constant_upper + tail_upper),
    "linear_boundary_lower": str(linear_lower),
    "strict_rouche_inequality": True,
    "short_exact_rouche_brackets": {
        "constant_plus_tail_strict_upper": "19/100000",
        "linear_term_strict_lower": "31/100000",
    },
    "disk_and_conjugate_disk_disjoint_and_nonreal": True,
    "root_modulus_squared_strict_lower": str(modulus_squared_lower),
    "positive_root_strict_lower": str(lambda_lower),
    "q_at_positive_root_lower": str(q_at_lambda_lower),
    "mahler_strict_lower": str(mahler_lower),
    "mahler_lower_cubed_minus_two": str(cube_gap),
    "all_retained_arithmetic_quantities_agree": True,
    "proof_boundary": (
        "Rouche gives one root in each conjugate disk. They lie outside the "
        "unit circle and hence are roots of p22, not Phi6. L G0039's unique "
        "positive root above one turns the negative rational evaluation into "
        "the positive-root lower bound. Their three Mahler factors prove "
        "M(p22)^3>2. This only excludes the stated M^3<=2 sufficient criterion; "
        "it does not decide interior or positive volume."
    ),
}
rendered = json.dumps(out, indent=2)
(HERE / "verification.json").write_text(rendered + "\n", encoding="utf-8")
print(rendered)
