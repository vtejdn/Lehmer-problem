"""Three fixed exact controls for D100; no auxiliary box search."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import argparse
import json
import math
import sympy as sp

t = sp.Symbol("t")


def rem2(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def mul2(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
    return out


def quotient2(a, b):
    q = 0
    while a and a.bit_length() >= b.bit_length():
        j = a.bit_length() - b.bit_length()
        q ^= 1 << j
        a ^= b << j
    assert a == 0
    return q


def factors2(a):
    out = []
    j = 1
    while j <= (a.bit_length()-1)//2:
        for middle in range(1 << (j-1)):
            divisor = (1 << j) | (middle << 1) | 1
            e = 0
            while a != 1 and rem2(a, divisor) == 0:
                a = quotient2(a, divisor)
                e += 1
            if e:
                out.append((divisor, e))
        j += 1
    if a != 1:
        out.append((a, 1))
    return out


def pow2(a, n, mod):
    out = 1
    while n:
        if n & 1:
            out = rem2(mul2(out, a), mod)
        a = rem2(mul2(a, a), mod)
        n >>= 1
    return out


def bits(poly):
    poly = sp.Poly(poly, t)
    return sum((int(poly.nth(i)) & 1) << i for i in range(poly.degree() + 1))


def ascending(poly):
    poly = sp.Poly(poly, t, domain=sp.ZZ)
    return [int(poly.nth(i)) for i in range(poly.degree() + 1)]


def val(n, p):
    n = abs(int(n))
    assert n
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def exact_norm(P, F):
    d = sp.degree(P, t)
    cols = []
    for j in range(d):
        rem = sp.Poly(sp.rem(F*t**j, P, t), t, domain=sp.ZZ)
        cols.append(sp.Matrix([rem.nth(i) for i in range(d)]))
    matrix = sp.Matrix.hstack(*cols)
    determinant = int(matrix.det(method="bareiss"))
    resultant = int(sp.resultant(P, F, t))
    assert determinant == resultant != 0
    return resultant


def control(name, P, F):
    d = int(sp.degree(P, t))
    assert sp.Poly(P, t).LC() == 1
    assert sp.expand(t**d * P.subs(t, 1/t)) == P
    assert sp.Poly(P, t).is_irreducible
    G = bits(P)
    factors = []
    product = 1
    for g, e in factors2(G):
        f = g.bit_length() - 1
        # Exhaustive tiny-factor irreducibility check, in the same bit arithmetic.
        for j in range(1, f//2 + 1):
            for middle in range(1 << (j-1)):
                divisor = (1 << j) | (middle << 1) | 1
                assert rem2(g, divisor) != 0
        order = next(int(n) for n in sp.divisors(2**f - 1)
                     if pow2(2, int(n), g) == 1)
        for _ in range(e):
            product = mul2(product, g)
        factors.append({"binary_bits": g, "degree": f,
                        "multiplicity": int(e), "root_order": order})
    assert product == G
    E = max(x["multiplicity"] for x in factors)
    k = (E-1).bit_length()
    L = math.lcm(*(x["root_order"] for x in factors))
    h = (1 << k)*L
    assert pow2(2, h, G) == 1
    for p in sp.factorint(h):
        assert pow2(2, h//int(p), G) != 1
    orders3 = [val(x["root_order"], 3) for x in factors]
    triples = min(orders3) > 0 and len(set(orders3)) == 1
    if triples:
        assert rem2(1 | (1 << (h//3)) | (1 << (2*h//3)), G) == 0
    quotient, remainder = sp.div(F, P, t, domain=sp.ZZ)
    rem_coeffs = ascending(remainder)
    assert all(x % 2 == 0 for x in rem_coeffs)
    V = sp.expand(remainder/2)
    assert sp.expand(F-P*quotient-2*V) == 0
    coeffs = ascending(F)
    content = math.gcd(*coeffs)
    S1 = sum(abs(c) for c in coeffs)
    S2sq = sum(c*c for c in coeffs)
    R = exact_norm(P, F)
    Vnorm = exact_norm(P, V)
    assert R == 2**d * Vnorm
    assert abs(R) % (2**d) == 0
    return {"name": name, "P_ascending": ascending(P), "degree": d,
            "binary_factors": factors, "E": E, "L": L, "k": k,
            "full_quotient_order": h, "trinomial_exists": triples,
            "minimum_degree_at_S2_lt_2": 2*h//3 if triples else h,
            "F_ascending": coeffs, "F_degree": int(sp.degree(F,t)),
            "quotient_U_ascending": ascending(quotient),
            "half_remainder_V_ascending": ascending(V),
            "half_remainder_norm": Vnorm,
            "content": content, "S1": S1, "S2_squared": S2sq,
            "rho": str(sp.Rational(S1*S1, S2sq)),
            "signed_resultant": R,
            "absolute_resultant_factorization": {
                str(p):int(e) for p,e in sp.factorint(abs(R)).items()},
            "v2_resultant": val(R,2),
            "extra_norms": {
                "Phi3_signed_resultant": exact_norm(P,t*t+t+1),
                "signed_full_order_resultant": exact_norm(P,t**h-1)}}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=(_J_OUTPUT / 'verification.json'))
    args=parser.parse_args()
    cases=[("quartic",t**4-t**3-t**2-t+1,t**5-1),
           ("degree_six",t**6-t**5-t**3-t+1,t**8+t**4+1),
           ("original_lehmer",t**10+t**9-t**7-t**6-t**5-t**4-t**3+t+1,t**31-1)]
    result={'scope': 'Three fixed inputs; binary factor/order certificates and complete norms; no auxiliary search.', 'cases': [control(*case) for case in cases]}
    args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(args.output),
                      "results":[[x["name"],x["full_quotient_order"],x["signed_resultant"]]
                                 for x in result["cases"]]}))


if __name__=="__main__":
    main()
