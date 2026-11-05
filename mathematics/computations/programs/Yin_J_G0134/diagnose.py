"""Exact finite binary checks and uncertified cubic Jensen quadrature.

Python standard library only.  No finite-field existence theorem is checked here.
Midpoint trapezoidal sums and algebraic root formulas are exploratory floating
point calculations, with no rigorous error bound.
"""

import argparse
import cmath
import itertools
import json
import math
from pathlib import Path
import sys


def xor_product(a, b):
    out = set()
    for i in a:
        for j in b:
            if i + j in out:
                out.remove(i + j)
            else:
                out.add(i + j)
    return out


def binary_checks():
    checked = []
    for r in range(2, 11):
        n = 2**r
        product = {0}
        for factor in ({0, 1}, {0, n - 1}, {0, 1, n}, {0, n - 1, n}):
            product = xor_product(product, factor)
        expected = set()
        for e in (0, 2, n + 1, n + 2, 2*n - 2, 2*n - 1, 3*n - 2, 3*n):
            if e in expected:
                expected.remove(e)
            else:
                expected.add(e)
        assert product == expected, (r, sorted(product), sorted(expected))
        checked.append(r)
    return checked


def cubic_roots(a, b, c, d):
    """Cardano, with the product-constrained second cube root."""
    aa, bb, cc = b/a, c/a, d/a
    p = bb - aa*aa/3
    q = 2*aa**3/27 - aa*bb/3 + cc
    disc = cmath.sqrt(q*q/4 + p*p*p/27)
    v1, v2 = -q/2 + disc, -q/2 - disc
    target = v1 if abs(v1) >= abs(v2) else v2
    u = target**(1/3) if target else 0j
    v = -p/(3*u) if u else 0j
    omega = complex(-0.5, math.sqrt(3)/2)
    roots = [u*omega**j + v*omega**(-j) - aa/3 for j in range(3)]
    for i, w in enumerate(roots):
        for _ in range(5):
            deriv = (3*a*w+2*b)*w+c
            if not deriv:
                break
            w -= (((a*w+b)*w+c)*w+d)/deriv
        roots[i] = w
    return roots


def jensen_mean(signs, count):
    epsilon, eta, delta = signs
    values = []
    max_residual = 0.0
    max_viete_residual = 0.0
    for j in range(count):
        z = cmath.exp(2j*math.pi*(j+0.5)/count)
        a = delta+z**(-2)
        b = epsilon/z+eta/z**2
        c = epsilon*z+eta*z**2
        d = z*z+delta
        roots = cubic_roots(a, b, c, d)
        values.append(math.log(abs(a))+sum(math.log(max(1.0, abs(w))) for w in roots))
        for w in roots:
            numerator = abs(((a*w+b)*w+c)*w+d)
            denominator = abs(a)*abs(w)**3+abs(b)*abs(w)**2+abs(c)*abs(w)+abs(d)
            max_residual = max(max_residual, numerator/max(denominator, 1e-300))
        s1 = sum(roots)
        s2 = roots[0]*roots[1]+roots[0]*roots[2]+roots[1]*roots[2]
        s3 = roots[0]*roots[1]*roots[2]
        max_viete_residual = max(max_viete_residual,
            abs(a*s1+b)/(abs(a*s1)+abs(b)+1e-300),
            abs(a*s2-c)/(abs(a*s2)+abs(c)+1e-300),
            abs(a*s3+d)/(abs(a*s3)+abs(d)+1e-300))
    return {"points": count, "mean": math.fsum(values)/count,
            "max_normalized_root_residual": max_residual,
            "max_normalized_viete_residual": max_viete_residual}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--points", nargs="+", type=int, default=[1024, 4096, 16384])
    args = parser.parse_args()
    if any(n < 8 or n % 4 for n in args.points):
        raise ValueError("Use positive multiples of four, at least eight")
    result = {"python": sys.version, "binary_checked_r": binary_checks(),
              "quadrature_certified": False, "log2": math.log(2), "signs": []}
    for signs in itertools.product((-1, 1), repeat=3):
        result["signs"].append({"epsilon_eta_delta": signs,
                              "quadratures": [jensen_mean(signs, n) for n in args.points]})
    group = Path(__file__).resolve().parent
    output_dir = group.parent.parent/"outputs"/group.name
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir/"diagnostic.json"
    target.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
