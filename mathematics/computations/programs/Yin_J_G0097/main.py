"""Exact four-input prescribed-value diagnostic; no search or window expansion."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "repository/config.json").is_file())
OUTPUT = ROOT / "mathematics/computations/outputs" / HERE.name
TIMEOUT_SECONDS = 180


def save(name, value):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT / (name + ".writing")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    temporary.replace(OUTPUT / name)


def worker():
    import sympy as s

    t, z = s.symbols("t z")
    specification = json.loads((HERE / "input.json").read_text(encoding="utf-8"))
    assert specification["window_multiple"] == 2 and specification["threshold"] == 4
    assert len(specification["inputs"]) == 4
    completed = []

    def coeff(poly, length=None):
        n = length if length is not None else max(1, int(poly.degree()) + 1) if not poly.is_zero else 1
        return [int(poly.nth(i)) for i in range(n)]

    def interval_horner(poly, left, right):
        low = high = s.Rational(0)
        for a in poly.all_coeffs():
            endpoints = (low * left, low * right, high * left, high * right)
            low, high = min(endpoints) + a, max(endpoints) + a
        return low, high

    try:
        for item in specification["inputs"]:
            coefficients = item["coefficients_ascending"]
            P = s.Poly(sum(a * t**i for i, a in enumerate(coefficients)), t, domain=s.ZZ)
            d = P.degree()
            assert d >= 2 and d % 2 == 0
            assert P.LC() == P.nth(0) == 1 and coefficients == coefficients[::-1]
            assert P.is_irreducible and not P.is_cyclotomic
            r = d // 2
            cheb = [s.Poly(2, z, domain=s.ZZ), s.Poly(z, z, domain=s.ZZ)]
            for k in range(2, max(r, 5) + 1):
                cheb.append(s.Poly(z, z) * cheb[-1] - cheb[-2])
            T = s.Poly(P.nth(r), z, domain=s.ZZ)
            for k in range(1, r + 1):
                T += P.nth(r + k) * cheb[k]
            assert T.degree() == r and T.is_irreducible
            assert s.expand(t**r * T.as_expr().subs(z, t + 1/t) - P.as_expr()) == 0
            intervals = T.intervals(eps=s.Rational(1, 2**80))
            assert sum(multiplicity for _, multiplicity in intervals) == r
            assert all(multiplicity == 1 for _, multiplicity in intervals)
            theta = {}
            for p in (2, 3, 5):
                remainder = T.compose(cheb[p]).rem(T)
                assert all(remainder.nth(i) % p == 0 for i in range(r))
                theta[p] = s.Poly(remainder.as_expr()/p, z, domain=s.ZZ)
                assert not theta[p].is_zero
            a, b, c = (theta[p] for p in (2, 3, 5))
            defects = {"e": (b**2 - a**3).rem(T),
                       "f": (2*c**2 - 3*a**5).rem(T),
                       "g": (c**3 - 2*b**5).rem(T)}
            h = sum((v**2 for v in defects.values()), s.Poly(0, z, domain=s.ZZ)).rem(T)
            assert not h.is_zero
            tinverse = s.Poly(s.invert(t, P.as_expr()), t, domain=s.QQ)
            zvalue = (s.Poly(t, t, domain=s.QQ) + tinverse).rem(P)

            def lift(poly):
                value = s.Poly(0, t, domain=s.QQ)
                for q in poly.all_coeffs():
                    value = (value * zvalue + s.Poly(q, t, domain=s.QQ)).rem(P)
                return value

            for p in (2, 3, 5):
                phase_value = (s.Poly(t**(r*p), t) * lift(theta[p])).rem(P)
                original_value = s.Poly(P.as_expr().subs(t, t**p)/p, t, domain=s.QQ).rem(P)
                assert phase_value == original_value
            target = lift(h)
            assert all(target.nth(i).q == 1 for i in range(d))
            rhs = s.Matrix(coeff(target, d))
            A = s.Matrix.hstack(*(s.Matrix(coeff(s.Poly(t**k, t).rem(P), d)) for k in range(2*d)))
            assert A[:, :d] == s.eye(d)
            gram = A * A.T
            y = gram.inv(method="DM") * rhs
            xstar = A.T * y
            assert gram*y == rhs and A*xstar == rhs
            energy = (rhs.T*y)[0]
            assert energy == (xstar.T*xstar)[0] and energy > 0
            assert all(s.denom(q) > 0 for q in xstar)
            normtrace = s.resultant(T.as_expr(), h.as_expr(), z)
            normoriginal = s.resultant(P.as_expr(), target.as_expr(), t)
            assert normtrace >= 2**r and normoriginal == normtrace**2
            contacts = []
            for (left, right), multiplicity in intervals:
                if -2 < left <= right < 2:
                    low, high = interval_horner(h, left, right)
                    contacts.append({"trace_interval": [str(left), str(right)],
                                     "h_interval": [str(low), str(high)],
                                     "strict_gt_two": bool(low > 2)})
            difference = energy - 4
            record = {
                "name": item["name"], "p_coefficients_ascending": coefficients,
                "degree": d, "trace_coefficients_ascending": coeff(T),
                "trace_isolating_intervals": [[str(left), str(right), mult] for (left, right), mult in intervals],
                "theta_coefficients": {str(p): coeff(theta[p], r) for p in (2, 3, 5)},
                "defect_trace_coefficients": {name: coeff(poly, r) for name, poly in defects.items()},
                "h_trace_coefficients": coeff(h, r), "r_h": [str(v) for v in rhs],
                "A_rows": [[int(v) for v in row] for row in A.tolist()],
                "gram_rows": [[int(v) for v in row] for row in gram.tolist()],
                "y": [str(v) for v in y], "x_star": [str(v) for v in xstar],
                "energy": str(energy), "energy_decimal_display_only": str(s.N(energy, 18)),
                "energy_minus_four": str(difference),
                "energy_sign": "above" if difference > 0 else "below" if difference < 0 else "equal",
                "trace_norm": str(normtrace), "original_norm": str(normoriginal),
                "circle_contacts": contacts,
                "checks": {"C155_input_valid": True, "all_trace_roots_real": True,
                           "original_phase_identities": True, "same_integral_residue": True,
                           "normal_equations_and_feasibility": True, "exact_energy_identity": True,
                           "full_norm_identity_and_floor": True}}
            completed.append(record)
            save("partial.json", {"complete": False, "inputs": completed})
            print(item["name"], "degree", d, "energy", record["energy_decimal_display_only"],
                  record["energy_sign"], "circle_contacts_gt2", sum(q["strict_gt_two"] for q in contacts), flush=True)
        result = {"complete": True, "arithmetic": "exact rational; SymPy " + s.__version__,
                  "window_multiple": 2, "threshold": 4, "inputs": completed}
        save("results.json", result)
        (OUTPUT / "partial.json").unlink()
    except Exception as error:
        save("partial.json", {"complete": False, "error": repr(error), "inputs": completed})
        raise


if __name__ == "__main__":
    if sys.argv[1:] == ["--worker"]:
        worker()
    elif not sys.argv[1:]:
        try:
            result = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()), "--worker"], timeout=TIMEOUT_SECONDS)
            raise SystemExit(result.returncode)
        except subprocess.TimeoutExpired:
            print("Stopped: full author invocation exceeded 180 seconds; any partial.json is incomplete.", file=sys.stderr)
            raise SystemExit(124)
    else:
        raise SystemExit("No scope-changing command-line options are supported.")
