"""Forty signed forms per fixed input; certify only the selected witnesses."""
from __future__ import annotations

from decimal import Decimal, localcontext
from itertools import product
import json
from math import isqrt
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "repository/config.json").is_file())
INPUT = ROOT / "mathematics/computations/programs/Yin_J_G0097/input.json"
OUTPUT = ROOT / "mathematics/computations/outputs" / HERE.name
EXPECTED = {
    "quartic_Salem_seed": [1, -1, -1, -1, 1],
    "Lehmer_degree10": [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1],
}
PRIMES = (2, 3, 5, 7)
SHEARS = (-2, -1, 0, 1, 2)
COUNTS = (8192, 16384)
L = 972000
TIMEOUT = 300


class Unresolved(Exception):
    pass


def save(name, payload):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pending = OUTPUT / (name + ".writing")
    pending.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    pending.replace(OUTPUT / name)


def worker(name):
    import numpy as np
    import sympy as sp
    import flint
    from flint import acb_poly, arb, ctx, fmpz_poly

    specification = json.loads(INPUT.read_text(encoding="utf-8"))
    selected_inputs = {v["name"]: v["coefficients_ascending"]
                       for v in specification["inputs"] if v["name"] in EXPECTED}
    assert selected_inputs == EXPECTED and name in EXPECTED
    pc = EXPECTED[name]
    x, z = sp.symbols("x z")
    P = sp.Poly(sum(c*x**i for i, c in enumerate(pc)), x, domain=sp.ZZ)
    d, r = int(P.degree()), int(P.degree())//2
    assert P.is_irreducible and not P.is_cyclotomic
    assert pc == pc[::-1] and pc[0] == pc[-1] == 1
    cheb = [sp.Poly(2, z), sp.Poly(z, z)]
    for k in range(2, max(5, r)+1):
        cheb.append(sp.Poly(z, z)*cheb[-1]-cheb[-2])
    T = sp.Poly(pc[r], z)
    for k in range(1, r+1):
        T += pc[r+k]*cheb[k]
    assert T.is_irreducible and T.degree() == r
    assert sp.expand(x**r*T.as_expr().subs(z, x+1/x)-P.as_expr()) == 0
    real_roots = T.intervals(eps=sp.Rational(1, 2**50))
    assert sum(m for _, m in real_roots) == r and all(m == 1 for _, m in real_roots)
    if r % 2:
        field_evidence = {"criterion": "odd trace-field degree excludes every quadratic subfield", "degree": r}
    else:
        assert r == 2
        discriminant = int(sp.discriminant(T.as_expr(), z))
        assert discriminant == 13
        for prime in PRIMES:
            ratio = sp.Rational(discriminant, prime)
            numerator, denominator = map(int, ratio.as_numer_denom())
            assert not (isqrt(numerator)**2 == numerator and isqrt(denominator)**2 == denominator)
        field_evidence = {"criterion": "quadratic trace field with discriminant13", "discriminant": discriminant}
    trace_desc = [int(c) for c in T.all_coeffs()]
    sample_data = {(component, shear, prime): {} for component, shear, prime
                   in product(("E", "F_0"), SHEARS, PRIMES)}
    for count in COUNTS:
        theta = np.pi*(np.arange(count, dtype=np.float64)+0.5)/count
        av, bv, cv = (np.polyval(trace_desc, 2*np.cos(k*theta))/k for k in (2, 3, 5))
        ev, fv, gv = bv**2-av**3, 2*cv**2-3*av**5, cv**3-2*bv**5
        for key in sample_data:
            component, shear, prime = key
            xv = ev if component == "E" else fv
            signed = (xv+shear*gv)**2-prime*gv**2
            finite = bool(np.all(np.isfinite(signed)) and np.all(signed != 0))
            sample_data[key][str(count)] = float(np.mean(np.log(np.abs(signed)))) if finite else None
    rankable = [key for key, values in sample_data.items() if all(v is not None for v in values.values())]
    payload = {
        "complete": False, "name": name, "p_coefficients_ascending": pc, "degree": d,
        "trace_coefficients_ascending": [str(T.nth(i)) for i in range(r+1)],
        "field_exclusion": field_evidence,
        "grid": [{"component": a, "s": b, "p": c, "midpoint_means": values}
                 for (a, b, c), values in sample_data.items()],
        "ranking_certified": False,
        "selection_rule": "least finite16384-node mean; exact-floating ties lexicographic(component,s,p)",
        "versions": {"numpy": np.__version__, "sympy": sp.__version__, "flint": flint.__version__},
    }
    if not rankable:
        payload["finding"] = "no rankable sampled candidate; no witness selected"
        save(name + ".json", payload)
        raise Unresolved(payload["finding"])
    winner = min(rankable, key=lambda key: (sample_data[key]["16384"], key))
    component, shear, prime = winner
    payload["selected"] = {"component": component, "s": shear, "p": prime}
    save(name + ".json", payload)
    print(name, "selected", payload["selected"], "exploratory", sample_data[winner], flush=True)

    def inflate(k):
        coefficients = [0]*(k*d+1)
        for i, c in enumerate(pc):
            coefficients[k*i] = c
        return fmpz_poly(coefficients)

    P2, P3, P5 = (inflate(k) for k in (2, 3, 5))
    H23, H25, H35 = 9*P2**3-8*P3**2, 75*P2**5-64*P5**2, 250*P3**5-243*P5**3
    X = fmpz_poly([0]*(9*d//2)+[13500*int(c) for c in H23]) if component == "E" else fmpz_poly([0]*(5*d//2)+[1215*int(c) for c in H25])
    Z = 32*H35
    A = (X+shear*Z)**2-prime*Z**2
    assert A.degree() == 30*d
    assert int(A[0]) == int(A[30*d]) == 50176*(shear**2-prime)
    assert [int(c) for c in A] == [int(c) for c in A][::-1]
    ag, bg, cg = (sp.Poly(T.compose(cheb[k]).as_expr()/k, z, domain=sp.QQ) for k in (2, 3, 5))
    e, f, g = bg**2-ag**3, 2*cg**2-3*ag**5, cg**3-2*bg**5
    chosen = e if component == "E" else f
    h = ((chosen+shear*g)**2-prime*g**2).rem(T)
    assert not h.is_zero and all(c.q == 1 for c in h.all_coeffs())
    trace_norm = sp.resultant(T.as_expr(), h.as_expr(), z)
    assert trace_norm.is_Integer and trace_norm != 0
    trace_norm = int(trace_norm)
    PQ = sp.Poly(P, x, domain=sp.QQ)
    inverse_x = sp.invert(sp.Poly(x, x, domain=sp.QQ), PQ)
    trace_x = (sp.Poly(x, x, domain=sp.QQ)+inverse_x).rem(PQ)
    hK = sp.Poly(0, x, domain=sp.QQ)
    for coefficient in h.all_coeffs():
        hK = (hK*trace_x+sp.Poly(coefficient, x, domain=sp.QQ)).rem(PQ)
    AQ = sp.Poly(sum(int(c)*x**i for i, c in enumerate(A)), x, domain=sp.QQ)
    inverse_phase = sp.invert(sp.Poly(x**(15*d), x, domain=sp.QQ), PQ)
    assert (AQ.rem(PQ)*inverse_phase).rem(PQ) == L**2*hK
    full_norm = int(sp.resultant(PQ.as_expr(), hK.as_expr(), x))
    assert full_norm == trace_norm**2 >= 1
    payload.update({"numerator_coefficients_ascending": [int(c) for c in A],
                    "numerator_degree": A.degree(), "scalar_denominator": L**2,
                    "center_shift": 15*d, "trace_value_coefficients_ascending": [str(h.nth(i)) for i in range(r)],
                    "trace_norm": str(trace_norm), "full_original_norm": str(full_norm),
                    "exact_original_value_identity_checked": True, "attempts": []})
    save(name + ".json", payload)

    def certify(value):
        if not value.is_finite() or not value.rad() < arb("1e-12"):
            raise Unresolved("insufficient logarithmic enclosure")
        stored = value.str(50, more=True)
        assert arb(stored).contains(value)
        with localcontext() as context:
            context.prec = 65
            decimal = format(Decimal(value.mid().str(50, radius=False)).quantize(Decimal("1e-12")), "f")
        assert abs(arb(stored)-arb(decimal)) < arb("1e-10")
        return {"ball": stored, "decimal": decimal, "absolute_error_bound": "1e-10"}

    for bits in (256, 512):
        ctx.prec = bits
        try:
            content, factors = A.factor_squarefree()
            restored = fmpz_poly([content])
            measure = arb(abs(int(A[A.degree()]))).log()
            count, witnesses = 0, []
            for factor, multiplicity in factors:
                restored *= factor**multiplicity
                assert factor.gcd(factor.derivative()).degree() == 0
                roots = acb_poly(factor).roots(tol=arb("1e-30"), maxprec=bits)
                if len(roots) != factor.degree():
                    raise Unresolved("incomplete isolated-root count")
                assert all(not roots[i].overlaps(roots[j]) for i in range(len(roots)) for j in range(i))
                root_data = []
                for root in roots:
                    contribution = arb(1).max(abs(root)).log()
                    measure += multiplicity*contribution
                    root_data.append({"real": root.real.str(50, more=True), "imag": root.imag.str(50, more=True),
                                      "log_plus_modulus": certify(contribution)})
                count += multiplicity*len(roots)
                witnesses.append({"factor_coefficients_ascending": [int(c) for c in factor],
                                  "multiplicity": multiplicity, "roots": root_data})
            assert restored == A and count == 30*d
            haar = measure-2*arb(L).log()
            original = arb(abs(trace_norm)).log()/r
            quantities = {"haar": haar, "original": original, "mahler_numerator": measure,
                          "haar_minus_margin_target": haar+arb(1)/16, "original_minus_haar": original-haar}
            payload.update({"complete": True, "precision_bits": bits, "factorization_content": int(content),
                            "root_count_with_multiplicity": count, "factors": witnesses,
                            "quantities": {key: certify(value) for key, value in quantities.items()},
                            "negative_haar": bool(haar < 0), "margin_reached": bool(haar < -arb(1)/16)})
            save(name + ".json", payload)
            print(name, "certified signed Haar", payload["quantities"]["haar"]["decimal"],
                  "original", payload["quantities"]["original"]["decimal"], flush=True)
            return
        except (Unresolved, ValueError) as error:
            payload["attempts"].append({"precision_bits": bits, "error": str(error)})
            save(name + ".json", payload)
    raise Unresolved("fixed certification attempts exhausted")


def main():
    statuses = []
    for name in EXPECTED:
        save(name + ".json", {"complete": False, "name": name, "state": "current worker not completed"})
        try:
            process = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()), "--worker", name], timeout=TIMEOUT)
            statuses.append({"name": name, "exit_code": process.returncode, "timed_out": False})
        except subprocess.TimeoutExpired:
            statuses.append({"name": name, "exit_code": 124, "timed_out": True})
    inputs = [json.loads((OUTPUT/(name+".json")).read_text(encoding="utf-8")) for name in EXPECTED]
    complete = all(row["exit_code"] == 0 for row in statuses) and all(row["complete"] for row in inputs)
    save("results.json", {"complete": complete, "statuses": statuses, "inputs": inputs})
    raise SystemExit(0 if complete else 1)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--worker" and sys.argv[2] in EXPECTED:
        worker(sys.argv[2])
    elif not sys.argv[1:]:
        main()
    else:
        raise SystemExit("Only the declared two-input signed-form diagnostic is supported.")
