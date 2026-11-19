"""Find every genuine double contact of a unit and its square on one fixed row."""

import argparse
import json

from sympy import Poly, QQ, ZZ, factor_list, invert, symbols


Y = symbols("Y")


def polynomial(coefficients):
    return Poly.from_list(list(reversed(coefficients)), Y, domain=ZZ)


def square_argument(poly):
    return poly.compose(Poly(Y**2, Y, domain=poly.domain))


def modular_power(value, exponent, modulus):
    result = Poly(1, Y, domain=QQ)
    while exponent:
        if exponent % 2:
            result = (result * value).rem(modulus)
        exponent //= 2
        if exponent:
            value = (value * value).rem(modulus)
    return result


def square_pairs(coefficients, sign):
    if sign not in (-1, 1) or not any(coefficients):
        raise ValueError("Use a nonzero integral row and a sign of +1 or -1.")
    width = len(coefficients) - 1
    row = polynomial(coefficients)
    reverse = polynomial(coefficients[::-1])
    defect = (square_argument(row) * reverse**2
              + sign * square_argument(reverse) * row**2).exquo_ground(2)
    report = {"width": width, "sign": sign, "one_norm": sum(map(abs, coefficients)),
              "zero_defect": defect.is_zero, "pairs": []}
    if defect.is_zero:
        return report

    variable = Poly(Y, Y, domain=QQ)
    for factor, multiplicity in factor_list(defect)[1]:
        if multiplicity < 2 or not factor.is_monic or abs(factor.TC()) != 1 or factor.is_cyclotomic:
            continue
        modulus = factor.set_domain(QQ)
        at_square = square_argument(row).rem(modulus)
        rev_square = square_argument(reverse).rem(modulus)
        if any(p.rem(modulus).is_zero for p in (row, reverse, at_square, rev_square)):
            continue
        value = (-sign * row * invert(reverse, modulus)).rem(modulus)
        wronskian = row.diff() * reverse - row * reverse.diff()
        log_derivative = (variable * wronskian).rem(modulus)
        if log_derivative.is_zero:
            continue
        exponent = (row * reverse * invert(log_derivative, modulus)).rem(modulus)
        if exponent.degree() != 0:
            continue
        candidate = exponent.TC()
        if candidate.q != 1 or candidate < 2:
            continue
        n = int(candidate)
        if modular_power(value, n, modulus) != variable.rem(modulus):
            continue
        if not (at_square + sign * value**2 * rev_square).rem(modulus).is_zero:
            continue
        derivative_eq = n * variable * wronskian - row * reverse
        if not square_argument(derivative_eq).rem(modulus).is_zero:
            continue
        report["pairs"].append({
            "n": n,
            "powered_minimum_ascending": [int(c) for c in reversed(factor.all_coeffs())],
            "unit_at_powered_root_ascending": [str(c) for c in reversed(value.all_coeffs())],
            "defect_multiplicity": multiplicity,
            "passes_budget": (((2*n*width + 1) * report["one_norm"]**2)**4).bit_length() <= n,
        })
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sign", required=True, type=int, choices=(-1, 1))
    parser.add_argument("coefficients", nargs="+", type=int,
                        help="Ascending coefficients, including zeros up to the formal width.")
    args = parser.parse_args()
    print(json.dumps(square_pairs(args.coefficients, args.sign), indent=2))
