"""Finite two-shear exploration followed by two certified fixed witnesses.

Midpoint grids rank candidates only.  The reported logarithmic enclosures
come from independent-of-sampling analytic Arb quadrature.
"""
from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import product
import json
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
SHEARS = (-2, -1, 0, 1, 2)
WEIGHTS = tuple(Fraction(q) for q in ("1/4", "1/2", "1", "2", "4"))
NODE_COUNTS = (8192, 16384)
TIMEOUT = 300


def save(name, value):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pending = OUTPUT / (name + ".writing")
    pending.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    pending.replace(OUTPUT / name)


def worker(name):
    import flint
    from flint import acb, arb, ctx
    import numpy as np
    import sympy as sp

    ctx.prec = 192
    specification = json.loads(INPUT.read_text(encoding="utf-8"))
    selected = {v["name"]: v["coefficients_ascending"]
                for v in specification["inputs"] if v["name"] in EXPECTED}
    assert selected == EXPECTED and name in EXPECTED
    pc = EXPECTED[name]
    x, z = sp.symbols("x z")
    P = sp.Poly(sum(c*x**i for i, c in enumerate(pc)), x, domain=sp.ZZ)
    d, r = int(P.degree()), int(P.degree()) // 2
    assert P.is_irreducible and not P.is_cyclotomic
    assert pc == pc[::-1] and pc[0] == pc[-1] == 1
    cheb = [sp.Poly(2, z), sp.Poly(z, z)]
    for k in range(2, max(5, r) + 1):
        cheb.append(sp.Poly(z, z)*cheb[-1] - cheb[-2])
    T = sp.Poly(pc[r], z)
    for k in range(1, r + 1):
        T += pc[r+k]*cheb[k]
    assert sp.expand(x**r*T.as_expr().subs(z, x+1/x)-P.as_expr()) == 0
    intervals = T.intervals(eps=sp.Rational(1, 2**50))
    assert sum(mult for _, mult in intervals) == r
    assert all(mult == 1 for _, mult in intervals)
    trace_desc = [int(v) for v in T.all_coeffs()]
    samples = {}
    for count in NODE_COUNTS:
        angles = np.pi*(np.arange(count, dtype=np.float64)+0.5)/count
        av, bv, cv = (np.polyval(trace_desc, 2*np.cos(p*angles))/p
                      for p in (2, 3, 5))
        ev, fv, gv = bv**2-av**3, 2*cv**2-3*av**5, cv**3-2*bv**5
        for s, t, q in product(SHEARS, SHEARS, WEIGHTS):
            key = (s, t, q)
            value = float(q)*(ev+s*gv)**2 + (fv+t*gv)**2/float(q) + 2*gv**2
            assert np.all(np.isfinite(value)) and np.all(value > 0)
            samples.setdefault(key, {})[str(count)] = float(np.mean(np.log(value)))
    assert len(samples) == 125
    winner = min(samples, key=lambda key: (samples[key]["16384"], key))
    s, t, q = winner
    payload = {
        "complete": False, "name": name, "p_coefficients_ascending": pc,
        "degree": d, "trace_coefficients_ascending": [str(T.nth(i)) for i in range(r+1)],
        "grid": [{"s": a, "t": b, "q": str(c), "midpoint_averages": vals}
                 for (a, b, c), vals in samples.items()],
        "selection_rule": "minimum 16384-node mean, exact-float ties lexicographic(s,t,q)",
        "selected": {"s": s, "t": t, "q": str(q), "buffer": 2},
        "ranking_certified": False,
        "versions": {"numpy": np.__version__, "sympy": sp.__version__, "flint": flint.__version__},
    }
    save(name + ".json", payload)
    print(name, "selected", payload["selected"], "exploratory", samples[winner], flush=True)
    ag, bg, cg = (sp.Poly(T.compose(cheb[p]).as_expr()/p, z, domain=sp.QQ)
                  for p in (2, 3, 5))
    e, f, g = bg**2-ag**3, 2*cg**2-3*ag**5, cg**3-2*bg**5
    common = sp.gcd(sp.gcd(e, f), g)
    assert common.degree() == 0
    rational_q = sp.Rational(q.numerator, q.denominator)
    B = rational_q*(e+s*g)**2 + (f+t*g)**2/rational_q + 2*g**2
    h = B.rem(T)
    trace_norm = sp.resultant(T.as_expr(), h.as_expr(), z)
    assert trace_norm.is_Rational and trace_norm >= 2**r
    norm_num, norm_den = map(int, trace_norm.as_numer_denom())
    assert norm_num > 0 and norm_den > 0
    original = (arb(norm_num).log()-arb(norm_den).log())/r
    calls = [0]
    aq = arb(q.numerator)/q.denominator

    def evaluate_trace(w):
        result = acb(0)
        for coefficient in trace_desc:
            result = result*w+coefficient
        return result

    def integrand(u, analytic):
        calls[0] += 1
        angle = u*arb.pi()
        a = evaluate_trace(2*(2*angle).cos())/2
        b = evaluate_trace(2*(3*angle).cos())/3
        c = evaluate_trace(2*(5*angle).cos())/5
        ee, ff, gg = b**2-a**3, 2*c**2-3*a**5, c**3-2*b**5
        symbol = aq*(ee+s*gg)**2 + (ff+t*gg)**2/aq + 2*gg**2
        return symbol.log(analytic=analytic)

    integral = acb.integral(integrand, 0, 1, rel_tol=arb("1e-18"), abs_tol=arb("1e-18"),
                            deg_limit=100, eval_limit=200000, depth_limit=30)
    assert integral.is_finite() and integral.imag.contains(0)

    def certified(value):
        assert value.is_finite() and value.rad() < arb("1e-12")
        stored = value.str(50, more=True)
        assert arb(stored).contains(value)
        with localcontext() as context:
            context.prec = 65
            decimal = format(Decimal(value.mid().str(50, radius=False)).quantize(Decimal("1e-12")), "f")
        assert abs(arb(stored)-arb(decimal)) < arb("1e-10")
        return {"ball": stored, "decimal": decimal, "absolute_error_bound": "1e-10"}

    haar, logtwo = integral.real, arb(2).log()
    values = {"haar": haar, "original": original, "log2": logtwo,
              "haar_minus_log2": haar-logtwo, "original_minus_haar": original-haar,
              "haar_minus_margin_target": haar-logtwo+arb(1)/16}
    payload.update({
        "complete": True, "precision_bits": 192,
        "method": "analytic acb quadrature theta=pi*u on [0,1], no midpoint error assumption",
        "global_defect_coefficients": {label: [str(poly.nth(i)) for i in range(int(poly.degree())+1)]
                                       for label, poly in (("e", e), ("f", f), ("g", g))},
        "global_defect_gcd": str(common.as_expr()),
        "trace_value_coefficients_ascending": [str(h.nth(i)) for i in range(r)],
        "trace_norm": str(trace_norm), "full_original_norm": str(trace_norm**2),
        "quantities": {key: certified(value) for key, value in values.items()},
        "imaginary_enclosure": integral.imag.str(50, more=True), "integrand_evaluations": calls[0],
        "margin_reached": bool(haar < logtwo-arb(1)/16),
        "comparison_decided": bool(haar < logtwo-arb(1)/16 or haar > logtwo-arb(1)/16),
    })
    save(name + ".json", payload)
    print(name, "certified Haar", payload["quantities"]["haar"]["decimal"],
          "original", payload["quantities"]["original"]["decimal"], flush=True)


def main():
    pre_screen = json.loads((OUTPUT/"screen.json").read_text(encoding="utf-8"))
    screen_inputs = {row["name"]: row for row in pre_screen["inputs"]}
    assert set(screen_inputs) == set(EXPECTED)
    assert all(screen_inputs[name]["p_coefficients_ascending"] == pc for name, pc in EXPECTED.items())
    statuses = []
    for name in EXPECTED:
        row = screen_inputs[name]
        if row["complete"] and (row.get("excludes_below_log2") or row.get("excludes_operational_margin")):
            save(name + ".json", {"complete": True, "name": name,
                                  "state": "grid not run: whole-family determinant screen",
                                  "screen_evidence": name + "_screen.json"})
            statuses.append({"name": name, "exit_code": 0, "timed_out": False, "grid_run": False})
            continue
        save(name + ".json", {"complete": False, "name": name,
                              "state": "current worker not yet completed"})
        try:
            process = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()), "--worker", name],
                                     timeout=TIMEOUT)
            status = {"name": name, "exit_code": process.returncode, "timed_out": False, "grid_run": True}
        except subprocess.TimeoutExpired:
            status = {"name": name, "exit_code": 124, "timed_out": True, "grid_run": True}
        statuses.append(status)
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
        raise SystemExit("Only the two fixed inputs and declared finite grid are supported.")
