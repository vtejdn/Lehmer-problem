"""Two retained controls, exact GF(2) orders and complete divisor profiles.

Power/gcd/Rabin/rank operations are independent integer-bitset routines.
python-flint proposes the GF(2) factorization; SymPy performs the one exact
integer quotient defining the retained degree-22 input.  No root numerics.
"""
from fractions import Fraction
from math import prod
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as sp
import flint


def code(coefficients):
    return sum((int(c) & 1) << j for j, c in enumerate(coefficients))


def coefficients(value, length=None):
    if length is None:
        length = max(1, value.bit_length())
    return [(value >> j) & 1 for j in range(length)]


def remainder(value, modulus):
    while value and value.bit_length() >= modulus.bit_length():
        value ^= modulus << (value.bit_length() - modulus.bit_length())
    return value


def multiply(a, b, modulus):
    value = 0
    while b:
        if b & 1:
            value ^= a
        a <<= 1
        b >>= 1
    return remainder(value, modulus)


def power(a, exponent, modulus):
    result = 1
    while exponent:
        if exponent & 1:
            result = multiply(result, a, modulus)
        a = multiply(a, a, modulus)
        exponent >>= 1
    return result


def gcd(a, b):
    while b:
        a, b = b, remainder(a, b)
    return a


def prime_factors(n):
    result = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0)+1
    return result


def divisors(n):
    result = [1]
    for p, e in prime_factors(n).items():
        result = [a*p**j for a in result for j in range(e+1)]
    return sorted(result)


def binary_rank(columns):
    pivots = {}
    for column in columns:
        while column:
            pivot = column.bit_length()-1
            if pivot not in pivots:
                pivots[pivot] = column
                break
            column ^= pivots[pivot]
    return len(pivots)


def multiplication_columns(element, modulus, d):
    return [multiply(element, 1 << j, modulus) for j in range(d)]


def sylvester_nullity(left_columns, right_columns, d):
    # Row-major bit positions in the d-by-d output matrix.
    outputs = []
    for i in range(d):
        for j in range(d):
            column = 0
            for k in range(d):
                if (left_columns[i] >> k) & 1:
                    column ^= 1 << (k*d+j)
                if (right_columns[k] >> j) & 1:
                    column ^= 1 << (i*d+k)
            outputs.append(column)
    rank = binary_rank(outputs)
    return d*d-rank, rank


def factor_payload(integer_coefficients, modulus):
    _, factors = flint.nmod_poly([c & 1 for c in integer_coefficients],2).factor()
    payload = []
    recombined = 1
    # Ordinary binary multiplication, with a harmless sufficiently high modulus.
    large_modulus = 1 << (2*modulus.bit_length()+1)
    for factor, multiplicity in factors:
        cs = [int(factor[j]) & 1 for j in range(factor.degree()+1)]
        f = code(cs)
        degree = f.bit_length()-1
        final = power(2, 1 << degree, f)
        tests = {str(p): gcd(power(2, 1 << (degree//p), f) ^ 2, f)
                 for p in prime_factors(degree)}
        assert final == 2 and all(value == 1 for value in tests.values())
        for _ in range(multiplicity):
            recombined = multiply(recombined, f, large_modulus)
        payload.append({"code": f, "coefficients_ascending": cs,
                        "degree": degree, "multiplicity": multiplicity,
                        "frobenius_final_code": final,
                        "irreducibility_gcd_codes": tests})
    assert recombined == modulus
    return sorted(payload, key=lambda f: (f["degree"], f["code"]))


def compare_profiles(candidate, previous, d):
    # Compare log(2^nu/(2d)^d)/a without approximating logarithms.
    s, t = candidate["a"], previous["a"]
    two_exponent = candidate["nu"]*t-previous["nu"]*s
    degree_base_exponent = d*(t-s)
    lhs = 2**max(two_exponent,0)*(2*d)**max(-degree_base_exponent,0)
    rhs = 2**max(-two_exponent,0)*(2*d)**max(degree_base_exponent,0)
    sign = (lhs > rhs)-(lhs < rhs)
    return sign, {"candidate_a": s, "previous_a": t,
                  "two_exponent": two_exponent,
                  "base_2d_exponent": degree_base_exponent,
                  "comparison_sign": sign}


def control(name, cs, candidates, provenance):
    d = len(cs)-1
    modulus = code(cs)
    derivative = sum(((modulus >> j)&1) << (j-1) for j in range(1,d+1,2))
    squarefree = gcd(modulus, derivative)
    assert squarefree == 1 and cs[0] & 1
    candidate_tests = {str(a): power(2,a,modulus) for a in candidates}
    found = [a for a in candidates if candidate_tests[str(a)] == 1]
    assert found, (name, candidate_tests)
    order = min(found)
    for ell in prime_factors(order):
        while order % ell == 0 and power(2,order//ell,modulus) == 1:
            order //= ell
    order_tests = {str(ell): power(2,order//ell,modulus)
                   for ell in prime_factors(order)}
    assert power(2,order,modulus) == 1 and all(v != 1 for v in order_tests.values())
    profiles, comparisons = [], []
    best = None
    for a in divisors(order):
        residue = power(2,a,modulus)
        twice = multiply(residue,residue,modulus)
        nu, rank = sylvester_nullity(multiplication_columns(residue,modulus,d),
                                    multiplication_columns(twice,modulus,d),d)
        ratio = Fraction(2**nu,(2*d)**d)
        profile = {"a": a, "nu": nu, "sylvester_rank": rank,
                   "power_remainder_code": residue,
                   "power_coefficients_ascending": coefficients(residue,d),
                   "a_over_d": {"numerator": str(Fraction(a,d).numerator),
                                "denominator": str(Fraction(a,d).denominator)},
                   "entropy_log_ratio": {"numerator": str(ratio.numerator),
                                         "denominator": str(ratio.denominator)},
                   "entropy_denominator": 3*(2*d-1)*a,
                   "positive_certificate": ratio > 1}
        profiles.append(profile)
        if profile["positive_certificate"]:
            if best is None:
                best = profile
            else:
                sign, test = compare_profiles(profile,best,d)
                comparisons.append(test)
                if sign > 0:
                    best = profile
    return {"name": name, "input_provenance": provenance,
            "coefficients": cs, "degree": d, "modulus_code": modulus,
            "squarefree_gcd_code": squarefree, "gf2_factorization": factor_payload(cs,modulus),
            "candidate_order_tests": candidate_tests,
            "order": order, "order_prime_factorization": {str(k): v for k,v in prime_factors(order).items()},
            "order_prime_tests": order_tests,
            "divisor_profiles": profiles, "exact_comparisons": comparisons,
            "best_a": None if best is None else best["a"],
            "all_exponent_optimum_scope": "Positive part of p=2,r=1 collision certificate; all a reduce to gcd(a,order), whose denominator is no larger"}


def main():
    x = sp.Symbol("x")
    q = sp.Poly(x**24-x**17-x**12-x**7+1,x)
    cyclo = sp.Poly(x*x-x+1,x)
    p22, rem = sp.div(q,cyclo)
    assert rem.is_zero
    controls = [
        control("lehmer",[1,1,0,-1,-1,-1,-1,-1,0,1,1],[31,33],
                "Retained L G0055 / J G0008 Lehmer input and its accepted all-power-stable domain"),
        control("degree22",[int(p22.nth(j)) for j in range(23)],[2047,2049],
                "L G0039 / J G0003: (t^24-t^17-t^12-t^7+1)/Phi6; retained irreducibility, small measure and all-power-stable scope"),
    ]
    result = {"prime": 2, "prime_power_r": 1,
              "coefficient_order": "ascending",
              "arithmetic": "Exact integer bitset GF(2) powers, gcds, Rabin certificates, Sylvester ranks and integer certificate comparisons",
              "input_count": 2, "inputs": controls,
              "scope": "Two retained inputs only; no new irreducibility, root count, Mahler or uniform coverage claim"}
    (_J_OUTPUT / "result.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps([{"name": c["name"], "degree": c["degree"], "order": c["order"],
                       "factors": [(f["degree"],f["code"]) for f in c["gf2_factorization"]],
                       "profiles": [(p["a"],p["nu"],p["positive_certificate"]) for p in c["divisor_profiles"]],
                       "best_a": c["best_a"]} for c in controls],indent=2))


if __name__ == "__main__":
    main()
