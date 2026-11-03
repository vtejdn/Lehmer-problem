"""Exact retained Lehmer control for the arithmetic surplus in L G0057.

Author method: SymPy resultants and discriminants.  Only k=1 and k=2
are tested: no derivative repetition, then the first repeated base block.
All mathematical output uses integer/rational arithmetic; no root numerics.
"""
from fractions import Fraction
from math import factorial, gcd, isqrt
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as sp


def astr(poly):
    return [int(poly.nth(i)) for i in range(poly.degree() + 1)]


def rat(value):
    q = Fraction(value)
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def main():
    x, y = sp.symbols("x y")
    coefficients = [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
    p = sp.Poly(sum(c * x**j for j, c in enumerate(coefficients)), x)
    d = p.degree()
    delta = abs(int(sp.discriminant(p.as_expr(), x)))
    powers = {}
    qs = {}
    for ell in (2, 3):
        q = sp.Poly(sp.resultant(p.as_expr(), y - x**ell, x), y)
        assert q.degree() == d and q.LC() == 1
        disc = abs(int(sp.discriminant(q.as_expr(), y)))
        b_squared = Fraction(disc, delta)
        assert b_squared.denominator == 1
        b_abs = isqrt(b_squared.numerator)
        assert b_abs * b_abs == b_squared.numerator
        res = int(sp.resultant(p.as_expr(), q.as_expr().subs(y, x), x))
        normalized = Fraction(res, ell**d)
        assert normalized.denominator == 1 and res != 0
        qs[ell] = q
        powers[str(ell)] = {
            "coefficients_ascending": astr(q),
            "discriminant_abs": str(disc),
            "index_square": str(b_squared.numerator),
            "index_abs": str(b_abs),
            "resultant_P_Q": str(res),
            "normalized_resultant": str(normalized.numerator),
        }
    cross = int(sp.resultant(qs[2].as_expr(), qs[3].as_expr(), y))
    constant = int(powers["2"]["index_square"]) * int(powers["3"]["index_square"]) * cross**2
    base = int(powers["2"]["normalized_resultant"]) * int(powers["3"]["normalized_resultant"])
    # Exactly the six cyclic indices needed by the structural identities for
    # pairs (1,2), (1,3), (2,3) and the two reciprocal index factors.
    cyclic = {n: int(sp.resultant(p.as_expr(), x**n - 1, x)) for n in range(1, 7)}
    cyclic_index_factors = {}
    cyclic_base_factors = {}
    for ell in (2, 3):
        index_floor = Fraction(cyclic[2*ell], cyclic[2])
        assert index_floor.denominator == 1 and index_floor > 0
        D_ell = abs(cyclic[ell-1] * cyclic[ell+1])
        overlap = gcd(D_ell, ell**d)
        cyclic_index_factors[str(ell)] = str(index_floor.numerator)
        cyclic_base_factors[str(ell)] = {
            "D_p": str(D_ell), "gcd_with_Frobenius_floor": str(overlap),
            "normalized_cyclic_floor": str(D_ell // overlap),
        }
    cyclic_cross_floor = abs(cyclic[1]*cyclic[5])
    cyclic_constant = int(cyclic_index_factors["2"])*int(cyclic_index_factors["3"])*cyclic_cross_floor**2
    cyclic_base = int(cyclic_base_factors["2"]["normalized_cyclic_floor"])*int(cyclic_base_factors["3"]["normalized_cyclic_floor"])
    comparisons = []
    for k in (1, 2):
        N = d * (k + 2)
        block = Fraction(1)
        for j in range(k):
            block *= Fraction(factorial(N + j) * factorial(j)**2,
                              (2*j + 1) * factorial(N-j-1) * factorial(2*j)**2)
        assert block.denominator == 1
        surplus = constant * base**(2*k)
        arithmetic = delta**(k*k + 2) * 6**(2*d*k) * surplus
        cost = (N**2 * block.numerator)**d
        exponent = 2 * (k*(N-k) + (N-1)*5)
        ratio = Fraction(arithmetic, cost)
        comparisons.append({
            "k": k, "S": 2, "N": N,
            "block_Gram_determinant": str(block.numerator),
            "Q_arith": str(surplus),
            "determinant_squared_arithmetic_exact": str(arithmetic),
            "block_constant": str(cost),
            "Mahler_exponent": exponent,
            "ratio": rat(ratio),
            "positive_certificate": arithmetic > cost,
            "without_surplus_ratio": rat(Fraction(arithmetic // surplus, cost)),
            "ratio_exceeds_27": arithmetic > 27 * cost,
            "without_surplus_ratio_exceeds_3": arithmetic // surplus > 3 * cost,
        })
    result = {
        "arithmetic": "exact integer and rational; no floating-point estimates",
        "question": "Actual arithmetic surplus for the retained Lehmer polynomial at primes 2 and 3",
        "input_provenance": "L G0055 and J G0008 retained Lehmer control; no new irreducibility or domain claim",
        "coefficients_ascending": coefficients, "degree": d,
        "discriminant_abs": str(delta), "selected_primes": [2, 3],
        "powered_polynomials": powers,
        "resultant_Q2_Q3": str(cross),
        "Q_arith_formula": "constant_times_base_to_2k",
        "Q_arith_constant": str(constant), "Q_arith_base": str(base),
        "cyclic_resultants": {str(n): str(value) for n, value in cyclic.items()},
        "cyclic_index_square_floors": cyclic_index_factors,
        "cyclic_base_resultant_floors": cyclic_base_factors,
        "cyclic_cross_resultant_floor": str(cyclic_cross_floor),
        "cyclic_surplus_constant": str(cyclic_constant),
        "cyclic_surplus_base": str(cyclic_base),
        "cyclic_lower_bound_saturates_actual_surplus_all_k": cyclic_constant == constant and cyclic_base == abs(base),
        "tested_k": [1, 2], "comparisons": comparisons,
        "scope": "Exact finite sufficient certificates on one accepted algebraic-unit control; no uniform inference",
    }
    (_J_OUTPUT / "result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"discriminant_abs": str(delta), "powers": powers,
                      "cross": str(cross), "constant": str(constant), "base": str(base),
                      "cyclic_resultants": result["cyclic_resultants"],
                      "cyclic_base_resultant_floors": cyclic_base_factors,
                      "cyclic_lower_bound_saturates_actual_surplus_all_k": result["cyclic_lower_bound_saturates_actual_surplus_all_k"],
                      "comparisons": comparisons}, indent=2))


if __name__ == "__main__":
    main()
