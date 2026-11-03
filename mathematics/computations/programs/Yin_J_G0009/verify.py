"""Independent exact algorithms for the J output result.json; imports no author code.

Powered polynomials: Newton power sums from original coefficients.
Discriminants/resultants: pure-Python Sylvester matrices and Bareiss elimination.
Block constants: determinant of the actual integer binomial Gram matrix.
This is an algorithmic cross-check by the authoring agent, not independent review.
"""
from fractions import Fraction
from math import comb, gcd, isqrt
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json


def det(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    if not n:
        return 1
    sign, previous = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((j for j in range(k+1, n) if a[j][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                quotient, remainder = divmod(numerator, previous)
                assert remainder == 0
                a[i][j] = quotient
            a[i][k] = 0
        previous = pivot
    return sign * a[n-1][n-1]


def resultant(a, b):
    """Ascending coefficients, conventional Res(a,b)."""
    m, n = len(a)-1, len(b)-1
    matrix = []
    for j in range(n):
        matrix.append([0]*j + a[::-1] + [0]*(n-j-1))
    for j in range(m):
        matrix.append([0]*j + b[::-1] + [0]*(m-j-1))
    return det(matrix)


def discriminant(a):
    n = len(a)-1
    derivative = [j*a[j] for j in range(1, n+1)]
    assert a[-1] == 1
    return (-1)**(n*(n-1)//2) * resultant(a, derivative)


def power_sums(a, limit):
    n = len(a)-1
    assert a[-1] == 1
    s = [n]
    for m in range(1, limit+1):
        if m <= n:
            value = -m*a[n-m] - sum(a[n-j]*s[m-j] for j in range(1, m))
        else:
            value = -sum(a[n-j]*s[m-j] for j in range(1, n+1))
        s.append(value)
    return s


def powered_coefficients(a, ell):
    n = len(a)-1
    s = power_sums(a, n*ell)
    descending = [1]
    for k in range(1, n+1):
        numerator = -sum(descending[k-j]*s[ell*j] for j in range(1, k+1))
        quotient, remainder = divmod(numerator, k)
        assert remainder == 0
        descending.append(quotient)
    return descending[::-1]


def main():
    result = json.loads((_J_OUTPUT / "result.json").read_text(encoding="utf-8"))
    checks = []

    def check(name, actual, expected):
        assert actual == expected, (name, actual, expected)
        checks.append(name)

    a = result["coefficients_ascending"]
    check("original retained input", a, [1,1,0,-1,-1,-1,-1,-1,0,1,1])
    n = len(a)-1
    check("degree", result["degree"], n)
    delta = abs(discriminant(a))
    check("original discriminant", str(delta), result["discriminant_abs"])
    qs, squares, norms = {}, {}, {}
    for ell in (2, 3):
        q = powered_coefficients(a, ell)
        data = result["powered_polynomials"][str(ell)]
        check(f"Q{ell} coefficients", q, data["coefficients_ascending"])
        disc = abs(discriminant(q))
        check(f"Q{ell} discriminant", str(disc), data["discriminant_abs"])
        square = Fraction(disc, delta)
        check(f"Q{ell} integral index square", square.denominator, 1)
        check(f"Q{ell} index square", str(square.numerator), data["index_square"])
        b_abs = isqrt(square.numerator)
        check(f"Q{ell} square root exact", b_abs*b_abs, square.numerator)
        check(f"Q{ell} index absolute", str(b_abs), data["index_abs"])
        res = resultant(a, q)
        check(f"Res(P,Q{ell})", str(res), data["resultant_P_Q"])
        norm = Fraction(res, ell**n)
        check(f"Q{ell} normalized resultant integral", norm.denominator, 1)
        check(f"Q{ell} normalized resultant", str(norm.numerator), data["normalized_resultant"])
        qs[ell], squares[ell], norms[ell] = q, square.numerator, norm.numerator
    cross = resultant(qs[2], qs[3])
    check("cross resultant", str(cross), result["resultant_Q2_Q3"])
    constant = squares[2]*squares[3]*cross**2
    base = norms[2]*norms[3]
    check("all-k surplus constant", str(constant), result["Q_arith_constant"])
    check("all-k surplus base", str(base), result["Q_arith_base"])
    cyclic = {}
    for j in range(1, 7):
        cyclic[j] = resultant(a, [-1]+[0]*(j-1)+[1])
        check(f"cyclic resultant c{j}", str(cyclic[j]), result["cyclic_resultants"][str(j)])
    cyclic_constant, cyclic_base = 1, 1
    for ell in (2, 3):
        factor = Fraction(cyclic[2*ell], cyclic[2])
        check(f"cyclic index factor {ell} integral", factor.denominator, 1)
        check(f"cyclic index factor {ell}", str(factor.numerator), result["cyclic_index_square_floors"][str(ell)])
        D_ell = abs(cyclic[ell-1]*cyclic[ell+1])
        overlap = gcd(D_ell, ell**n)
        data = result["cyclic_base_resultant_floors"][str(ell)]
        check(f"cyclic D_{ell}", str(D_ell), data["D_p"])
        check(f"cyclic Frobenius overlap {ell}", str(overlap), data["gcd_with_Frobenius_floor"])
        check(f"normalized cyclic floor {ell}", str(D_ell//overlap), data["normalized_cyclic_floor"])
        cyclic_constant *= factor.numerator
        cyclic_base *= D_ell//overlap
    cyclic_cross = abs(cyclic[1]*cyclic[5])
    cyclic_constant *= cyclic_cross**2
    check("cyclic cross floor", str(cyclic_cross), result["cyclic_cross_resultant_floor"])
    check("cyclic surplus constant", str(cyclic_constant), result["cyclic_surplus_constant"])
    check("cyclic surplus base", str(cyclic_base), result["cyclic_surplus_base"])
    check("all-k cyclic surplus saturation", cyclic_constant == constant and cyclic_base == abs(base),
          result["cyclic_lower_bound_saturates_actual_surplus_all_k"])
    check("bounded tested multiplicities", result["tested_k"], [1,2])
    for data in result["comparisons"]:
        k, S = data["k"], data["S"]
        N = n*(k+S)
        gram = [[sum(comb(r,i)*comb(r,j) for r in range(N))
                 for j in range(k)] for i in range(k)]
        A = det(gram)
        surplus = constant*base**(2*k)
        arithmetic = delta**(k*k+S)*6**(2*n*k)*surplus
        cost = (N**S*A)**n
        exponent = 2*(k*(N-k)+(N-1)*5)
        prefix = f"k={k} "
        for key, value in (("N",N),("block_Gram_determinant",str(A)),
                           ("Q_arith",str(surplus)),
                           ("determinant_squared_arithmetic_exact",str(arithmetic)),
                           ("block_constant",str(cost)),("Mahler_exponent",exponent),
                           ("positive_certificate",arithmetic>cost),
                           ("ratio_exceeds_27",arithmetic>27*cost),
                           ("without_surplus_ratio_exceeds_3",arithmetic//surplus>3*cost)):
            check(prefix+key, value, data[key])
        for key, value in (("ratio",Fraction(arithmetic,cost)),
                           ("without_surplus_ratio",Fraction(arithmetic//surplus,cost))):
            check(prefix+key, value, Fraction(int(data[key]["numerator"]), int(data[key]["denominator"])))
    verification = {
                "method": "Pure Python Newton identities, Sylvester/Bareiss determinants, and binomial Gram matrices",
        "scope": "Mathematical payload, no byte/hash or metadata gate; no independent human/agent proof review claimed",
        "checks_passed": len(checks), "checks": checks, "status": "passed",
    }
    (_J_OUTPUT / "verification.json").write_text(json.dumps(verification,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(verification,indent=2))


if __name__ == "__main__":
    main()
