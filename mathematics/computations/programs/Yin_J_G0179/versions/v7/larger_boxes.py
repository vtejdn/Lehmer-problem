"""Prepare and verify wider degree-64 and degree-66 boxes for any test prime."""

import argparse
import json
import re
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
GROUP = HERE.parents[1]
sys.path.insert(0, str(GROUP))
import count_prefixes
import trace_bounds as cert

T = Fraction(1091, 1000)


def auxiliary_polynomials():
    from sympy import Poly, Symbol, cyclotomic_poly, totient

    x = Symbol("x")
    polynomials = set(cert.POLYNOMIALS)
    for order in range(3, 513):
        degree = int(totient(order))
        if degree > 16:
            continue
        coefficients = Poly(cyclotomic_poly(order, x), x).all_coeffs()
        half = degree // 2
        trace = Poly(coefficients[half], x)
        previous, current = Poly(2, x), Poly(x, x)
        for j in range(1, half + 1):
            trace += coefficients[half - j] * current
            previous, current = current, Poly(x, x) * current - previous
        polynomials.add(tuple(map(int, trace.all_coeffs())))
    for poly in tuple(polynomials):
        polynomials.add(tuple((-1)**j * c for j, c in enumerate(poly)))
    return sorted(polynomials, key=lambda p: (len(p), p))


def choose_weights(polynomials):
    import numpy as np
    from scipy.optimize import linprog

    n = 1100
    angles = (np.arange(n) + 0.5) * np.pi / n
    cosines, sines = np.cos(angles), np.sin(angles)

    @lru_cache(maxsize=None)
    def samples(k):
        r = float(T)**k
        z = (r + 1 / r) * cosines + 1j * (r - 1 / r) * sines
        return np.column_stack([np.log(np.maximum(abs(np.polyval(p, z)), 1e-280))
                                for p in polynomials])

    weights = {}
    for degree in (64, 66):
        half = degree // 2
        rows = []
        for k in range(1, half + 1):
            r = float(T)**k
            A = np.block([[samples(0), -np.ones((n, 1)), np.zeros((n, 1))],
                          [samples(k), np.zeros((n, 1)), -np.ones((n, 1))]])
            rhs = np.concatenate([2 * cosines, (r + 1 / r) * cosines])
            result = linprog([0] * len(polynomials) + [half - 1, 1], A_ub=A, b_ub=rhs,
                             bounds=[(0, 3)] * len(polynomials) + [(None, None)] * 2)
            if not result.success:
                raise ArithmeticError(result.message)
            rows.append([int(np.rint(w * 10**8)) for w in result.x[:-2]])
        weights[str(degree)] = rows
    return {"polynomials": polynomials, "weights": weights}


def certify(inputs):
    cert.T = T
    cert.POLYNOMIALS = tuple(tuple(p) for p in inputs["polynomials"])
    if not all(p and p[0] == 1 and len(p) <= 9 for p in cert.POLYNOMIALS):
        raise ValueError("Expected monic integer auxiliaries of degree at most eight.")
    cert.DEGREE = 2 * max(len(p) - 1 for p in cert.POLYNOMIALS)
    cert.squared_moduli.cache_clear()
    report = {}
    for degree in (64, 66):
        rows = inputs["weights"][str(degree)]
        if len(rows) != degree // 2:
            raise ValueError("Expected a weight vector for each first-half Newton sum.")
        bounds, certificates = [], []
        for k, weights in enumerate(rows, 1):
            if len(weights) != len(cert.POLYNOMIALS) or any(type(w) is not int or w < 0 for w in weights):
                raise ValueError("Invalid integral weight vector.")
            unit, outer = [cert.certify(j, weights, cert.guide(j, weights), 10**8) for j in (0, k)]
            bounds.append(((degree // 2 - 1) * unit["upper"] + outer["upper"]) // cert.LOG_SCALE)
            certificates.append({"unit": unit, "outer": outer})
        count = count_prefixes.full_reciprocal_box(degree, bounds)
        report[str(degree)] = {"certificates": certificates, "certified_all_available": count}
        print(degree, bounds, count["no_power_substitution_up_to_sign"], flush=True)
    out = GROUP.parents[1] / "outputs" / GROUP.name / "versions" / "v7"
    out.mkdir(parents=True, exist_ok=True)
    (out / "boxes.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--choose-weights", action="store_true")
    args = parser.parse_args()
    target = HERE / "weights.json"
    if args.choose_weights:
        design = choose_weights(auxiliary_polynomials())
        layout = json.dumps(design, indent=2)
        layout = re.sub(r"\[\s*(-?\d+(?:,\s*-?\d+)*)\s*\]",
                        lambda m: "[" + "".join(m[1].split()) + "]", layout)
        target.write_text(layout + "\n", encoding="utf-8")
    certify(json.loads(target.read_text(encoding="utf-8")))
