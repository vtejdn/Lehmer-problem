"""Exact, bounded author pilot for D120; outputs are not a general proof."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time
from math import gcd
from functools import reduce
import sympy as sp

t = sp.Symbol("t")
START = time.monotonic()
CAP = 120


def coeffs(f):
    p = sp.Poly(f, t)
    return [int(p.nth(k)) for k in range(p.degree() + 1)]


def content(f):
    return reduce(gcd, (abs(x) for x in coeffs(f)))


def norm2(f):
    return sum(x * x for x in coeffs(f))


def packq(x):
    return str(sp.Rational(x))


def one(name, P, j):
    if time.monotonic() - START > CAP:
        raise TimeoutError("Declared 120-second pilot cap exceeded")
    P = sp.Poly(P, t)
    d = P.degree()
    D, N = d - 1, 2 * j + 1
    M = sp.zeros(N, N - d)
    for k in range(N - d):
        for i in range(d + 1):
            M[k + i, k] = P.nth(i)
    e = sp.zeros(N, 1)
    e[j] = 1
    r = e - M * ((M.T * M).inv() * M.T * e)
    assert M.T * r == sp.zeros(N - d, 1)
    assert r[j] == (r.T * r)[0]
    denominator = sp.ilcm(*(sp.denom(x) for x in r))
    raw = [int(x * denominator) for x in r]
    common = reduce(gcd, (abs(x) for x in raw))
    q = sp.Rational(denominator, common)
    assert q.q == 1 and q >= 2
    F = sp.Poly(sum((x // common) * t**k for k, x in enumerate(raw)), t)
    assert content(F) == 1
    assert sp.rem(F.as_expr() - q * t**j, P.as_expr(), t) == 0
    PF = P * F
    A = sp.Poly(sum(PF.nth(k) * t**k for k in range(d)), t)
    B = sp.Poly(sum(A.nth(D - k) * t**k for k in range(d)), t)
    assert PF == A + sp.Poly(t**N, t) * B
    assert content(A) == 1
    Z = sp.Poly(t, t) * (A.diff() * B - A * B.diff()) - N * A * B
    Z_alt = sp.Poly(t, t) * B * PF.diff() - (N * B + sp.Poly(t, t) * B.diff()) * PF
    assert Z == Z_alt
    actual_values = q * t ** (j + 1) * P.diff().as_expr() * B.as_expr()
    assert sp.rem(Z.as_expr() - actual_values, P.as_expr(), t) == 0
    c = content(Z)
    Z0 = sp.Poly(Z.as_expr() / c, t)
    assert content(Z0) == 1
    a = coeffs(A)
    b = next(k for k, x in enumerate(a) if x)
    h = len(a) - 1
    assert h > b
    middle = -sum((N + D - 2 * k) * x * x for k, x in enumerate(a))
    extreme = -(N + D - h - b) * a[h] * a[b]
    assert int(Z.nth(D)) == middle
    assert int(Z.LC()) == extreme
    assert Z.degree() == D + h - b
    assert next(k for k, x in enumerate(coeffs(Z)) if x) == D + b - h
    assert abs(middle) >= (N - D) * norm2(A)
    assert norm2(Z) >= middle**2
    rf = int(sp.resultant(P.as_expr(), F.as_expr(), t))
    ra = int(sp.resultant(P.as_expr(), A.as_expr(), t))
    rb = int(sp.resultant(P.as_expr(), B.as_expr(), t))
    rz = int(sp.resultant(P.as_expr(), Z.as_expr(), t))
    rz0 = int(sp.resultant(P.as_expr(), Z0.as_expr(), t))
    disc = int(sp.discriminant(P.as_expr(), t))
    assert rf == int(q)**d
    assert abs(ra) == abs(rb) and ra != 0
    assert abs(rz) == int(q)**d * abs(disc * rb)
    assert rz == c**d * rz0
    zenergy = norm2(Z0)
    sign = sp.sign(rz0**2 - zenergy**d)
    assert sp.sign(rz**2 - norm2(Z)**d) == sign
    return {
        "name": name, "P": coeffs(P), "d": d, "j": j, "N": N,
        "q": int(q), "centered_norm_squared": packq(r[j]),
        "F": coeffs(F), "F_degree": F.degree(), "F_energy": norm2(F),
        "F_resultant": rf, "A": coeffs(A), "B": coeffs(B),
        "A_energy": norm2(A), "A_resultant": ra, "B_resultant": rb,
        "discriminant": disc, "Z": coeffs(Z), "Z_content": c,
        "Z_primitive": coeffs(Z0), "Z_degree": Z.degree(),
        "Z_primitive_energy": zenergy, "Z_resultant": rz,
        "Z_primitive_resultant": rz0, "Z_middle": middle,
        "Z_leading": extreme, "net_margin_sign": int(sign),
        "all_exact_checks_passed": True,
    }


def main():
    specs = []
    for a in (3, 4, 5):
        for j in (1, 2, 4):
            specs.append((f"quadratic_a{a}", t**2 - a*t + 1, j))
    for name, P in (
        ("quartic", t**4-t**3-t**2-t+1),
        ("degree_six", t**6-t**5-t**3-t+1),
        ("lehmer", t**10+t**9-t**7-t**6-t**5-t**4-t**3+t+1),
    ):
        d = sp.degree(P, t)
        for j in (d - 1, d, 2*d - 1):
            specs.append((name, P, int(j)))
    rows = [one(*spec) for spec in specs]
    result = {'scope': '18 declared actual centered projections; exact rational/integer arithmetic', 'rows': rows, 'all_passed': all((row['all_exact_checks_passed'] for row in rows))}
    assert time.monotonic() - START <= CAP
    target = (_J_OUTPUT / 'verification.json')
    assert not target.exists(), "Preserve prior output; explicit review redirection required"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({'rows': len(rows), 'all_passed': result['all_passed'], 'net_margin_signs': [x['net_margin_sign'] for x in rows]}))


if __name__ == "__main__":
    main()
