"""Verify the conductor-21 cubic correction over the rational numbers."""

import json
from pathlib import Path
import tempfile

from sympy import I, Poly, QQ, Rational, ZZ, sign, symbols


t, z = symbols("t z")


def main():
    e = [Poly(1, t), Poly(t, t)]
    for _ in range(2, 11):
        e.append(e[-1] * Poly(t, t) - e[-2])
    b = [e[0]] + [e[k] + e[k - 1] for k in range(1, 11)]
    q = Poly(t**3, t) * b[8] + Poly(t - t**3, t)
    c = q - Poly(t, t) * b[10]
    assert c.degree() == 9 and c.LC() == 2
    endpoint = q.eval(-2) / b[10].eval(-2)
    assert endpoint == -2

    centers = [1911, 1652, 1247, 731, 149, -445, -1000, -1466, -1802, -1978]
    assert all(x - y > 2 for x, y in zip(centers, centers[1:]))
    residue_signs = []
    for j, center in enumerate(centers, start=1):
        left, right = [Rational(center + delta, 1000) for delta in (-1, 1)]
        assert b[10].eval(left) * b[10].eval(right) < 0
        assert q.eval(left) * q.eval(right) > 0 and q.count_roots(left, right) == 0
        residue_signs.append(int((-1)**(j-1) * sign(q.eval(left))))
    assert residue_signs == [1]*9 + [-1]

    # Reconstruct the entire reciprocal polynomial by both defining formulas.
    p = Poly(0, z, domain=ZZ)
    for (degree,), coeff in q.terms():
        p += Poly(coeff * z**(11-degree) * (1 + z*z)**degree, z)
    parent = Poly((1 + z*z)**3, z)
    central = Poly(-z**8 - 2*z**10 - 2*z**12 - z**14, z)
    assert p == parent * Poly(sum(z**j for j in range(17)), z) + central
    prefix_difference = Poly(1-z, z)*p - parent
    assert all(prefix_difference.nth(j) == 0 for j in range(8))
    assert prefix_difference.nth(8) == -1
    core = Poly(z**16 + 2*z**14 + z**12 + z**11 + 2*z**9 - z**8
                + 2*z**7 + z**5 + z**4 + 2*z**2 + 1, z, domain=QQ)
    assert p == (Poly(z**2 + 1, z) * Poly(z**4 + z**3 + z**2 + z + 1, z)
                 * core.set_domain(ZZ))

    # C881 v10 gives exactly two exterior roots. Locate the upper one.
    x0, x1, y0, y1 = [Rational(k, 10**8) for k in
                      (-5427783, -5427782, 126621203, 126621204)]
    assert core.count_roots(x0 + I*y0, x1 + I*y1) == 1
    lower, upper = x1*x1 + y0*y0, x0*x0 + y1*y1
    assert Rational("1.60623898") < lower <= upper < Rational("1.60623902")
    result = {"residue_signs": residue_signs, "endpoint_ratio": int(endpoint),
              "last_matching_degree": 7, "first_differing_degree": 8,
              "reciprocal_coefficients": [int(a) for a in p.all_coeffs()],
              "exterior_upper_root_rectangle": list(map(str, (x0, x1, y0, y1))),
              "whole_measure_bounds": list(map(str, (lower, upper)))}
    group = Path(__file__).resolve().parent
    out = group.parents[1] / "outputs" / group.name / "p21_cubic_witness.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                         dir=out.parent, delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(result, stream, indent=2)
            stream.write("\n")
        temporary.replace(out)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    print(f"Verified c=9, endpoint -2, and {lower} <= M(P) <= {upper}.")


if __name__ == "__main__":
    main()
