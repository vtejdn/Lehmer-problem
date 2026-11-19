"""Count roots above a rational radius for several reciprocal middle coefficients."""

from pathlib import Path
import json

from sympy import Poly, Rational, Symbol, cyclotomic_poly


X = Symbol("X")
ONE = Poly(1, X)
VAR = Poly(X, X)


def boundary_parts(outer, radius):
    """Scaled real part and imaginary part divided by sin(theta), at x=cos(theta)."""
    p, q = int(radius.p), int(radius.q)
    h = len(outer)
    scale = (p * q) ** h
    real = imag = Poly(0, X)
    t_prev, t = ONE, VAR
    u_prev, u = Poly(0, X), ONE
    for j in range(1, h + 1):
        factor = outer[h - j] * (p * q) ** (h - j)
        real += factor * (p ** (2 * j) + q ** (2 * j)) * t
        imag += factor * (p ** (2 * j) - q ** (2 * j)) * u
        t_prev, t = t, 2 * VAR * t - t_prev
        u_prev, u = u, 2 * VAR * u - u_prev
    return real, imag, scale


def interval_value(coefficients, a, b):
    """Rational interval Horner enclosure."""
    lo = hi = 0
    for c in coefficients:
        products = (a * lo, a * hi, b * lo, b * hi)
        lo, hi = c + min(products), c + max(products)
    return lo, hi


def sign(value):
    return 1 if value > 0 else -1 if value < 0 else 0


def exterior_counts(outer, centers, radius):
    """Return a root count for each integral center, with outer coefficients fixed."""
    if not outer or outer[0] != 1 or radius <= 1:
        raise ValueError("Use a monic reciprocal pencil and a rational radius above one.")
    real, imag, scale = boundary_parts(outer, radius)
    simple = imag.sqf_part()
    for endpoint in (-1, 1):
        if simple.eval(endpoint) == 0:
            simple = simple.exquo(VAR - endpoint)
    # Use decreasing x, i.e. increasing upper-semicircle angle.
    intervals = simple.intervals(eps=Rational(1, 10**12), inf=-1, sup=1)
    intervals = [bounds for bounds, _ in reversed(intervals)]
    edges = [(1, 1), *intervals, (-1, -1)]
    while any(top[0] <= bottom[1] for top, bottom in zip(edges, edges[1:])):
        intervals = [(a, b) if a == b else simple.refine_root(a, b, eps=(b - a) / 256)
                     for a, b in intervals]
        edges = [(1, 1), *intervals, (-1, -1)]
    directions = [sign(imag.eval(Rational(top[0] + bottom[1], 2)))
                  for top, bottom in zip(edges, edges[1:])]
    if 0 in directions:
        raise ArithmeticError("A sign sample coincides with an unisolated imaginary zero.")

    crossings = [directions[0]] + [b - a for a, b in zip(directions, directions[1:])]
    crossings.append(-directions[-1])
    counts = {}
    coefficients = real.all_coeffs()
    for center in centers:
        winding = 0
        for (a, b), jump in zip(edges, crossings):
            if not jump:
                continue
            while True:
                lo, hi = interval_value(coefficients, a, b)
                if lo + center * scale > 0:
                    winding += jump
                    break
                if hi + center * scale < 0:
                    break
                if a == b:
                    raise ArithmeticError("Integral unit on a rational circle above one.")
                a, b = simple.refine_root(a, b, eps=(b - a) / 256)
        counts[int(center)] = len(outer) - winding
    return counts


def main():
    product = ONE
    for m in (49, 16, 9):
        product *= Poly(cyclotomic_poly(m, X), X)
    outer = product.all_coeffs()[:28]
    assert product.nth(28) == 2
    radii = (Rational(101, 100), Rational(21, 20), Rational(1089, 1000))
    report = {str(r): exterior_counts(outer, (1, 2), r) for r in radii}
    assert report == {"101/100": {1: 12, 2: 0}, "21/20": {1: 6, 2: 0},
                      "1089/1000": {1: 0, 2: 0}}
    group = Path(__file__).resolve().parents[2]
    out = group.parents[1] / "outputs" / group.name / "versions" / "v5"
    out.mkdir(parents=True, exist_ok=True)
    (out / "counts.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
