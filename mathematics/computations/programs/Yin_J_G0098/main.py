"""Certified existing-B3 Haar averages on exactly four retained inputs.

The direct integral uses analytic complex ball quadrature and exact trace
normalization. No finite sampling or precision agreement is an error bound.
"""
from __future__ import annotations

from decimal import Decimal, localcontext
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "repository/config.json").is_file())
INPUT = ROOT / "mathematics/computations/programs/Yin_J_G0097/input.json"
OUTPUT = ROOT / "mathematics/computations/outputs" / HERE.name
TIMEOUT_SECONDS = 300
EXPECTED = [
    ("quadratic_A3", [1, -3, 1]),
    ("quartic_Salem_seed", [1, -1, -1, -1, 1]),
    ("quartic_radical_A4", [1, 0, -4, 0, 1]),
    ("Lehmer_degree10", [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]),
]


def save(name, payload):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT / (name + ".writing")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(OUTPUT / name)


def worker():
    import flint
    from flint import acb, arb, ctx
    import sympy as s

    ctx.prec = 192
    tolerance = arb("1e-18")
    logtwo = arb(2).log()
    t, z = s.symbols("t z")
    specification = json.loads(INPUT.read_text(encoding="utf-8"))
    assert [(q["name"], q["coefficients_ascending"]) for q in specification["inputs"]] == EXPECTED
    completed = []

    def coefficients(poly, n=None):
        n = n or max(1, int(poly.degree()) + 1)
        return [str(poly.nth(i)) for i in range(n)]

    def certified(value):
        assert value.is_finite() and value.rad() < arb("1e-12")
        with localcontext() as dec:
            dec.prec = 65
            center = Decimal(value.mid().str(50, radius=False)).quantize(Decimal("1e-12"))
        center = format(center, "f")
        assert abs(value - arb(center)) < arb("1e-10")
        return {"ball": value.str(50, more=True), "decimal": center,
                "absolute_error_bound": "1e-10",
                "sign": "positive" if value > 0 else "negative" if value < 0 else "undetermined"}

    try:
        for name, pcoeffs in EXPECTED:
            P = s.Poly(sum(a*t**i for i, a in enumerate(pcoeffs)), t, domain=s.ZZ)
            d, r = P.degree(), P.degree()//2
            assert P.is_irreducible and not P.is_cyclotomic
            assert pcoeffs == pcoeffs[::-1] and pcoeffs[0] == pcoeffs[-1] == 1
            cheb = [s.Poly(2,z), s.Poly(z,z)]
            for k in range(2,max(r,5)+1):
                cheb.append(s.Poly(z,z)*cheb[-1]-cheb[-2])
            T = s.Poly(P.nth(r),z)
            for k in range(1,r+1):
                T += P.nth(r+k)*cheb[k]
            assert T.is_irreducible and T.degree()==r
            assert s.expand(t**r*T.as_expr().subs(z,t+1/t)-P.as_expr())==0
            roots = T.intervals(eps=s.Rational(1,2**50))
            assert sum(mult for _,mult in roots)==r and all(mult==1 for _,mult in roots)
            # These are unreduced circle polynomials, not the residue modulo T.
            ag,bg,cg = (s.Poly(T.compose(cheb[p]).as_expr()/p,z,domain=s.QQ) for p in (2,3,5))
            eg,fg,gg = bg**2-ag**3, 2*cg**2-3*ag**5, cg**3-2*bg**5
            common = s.gcd(s.gcd(eg,fg),gg)
            assert common.degree()==0  # Q is strictly positive for all real z.
            h = (eg**2+fg**2+gg**2).rem(T)
            assert all(v.q==1 for v in h.all_coeffs())
            normtrace = int(s.resultant(T.as_expr(),h.as_expr(),z))
            assert normtrace>=2**r
            original_mean = arb(normtrace).log()/r
            trace_coeffs = [int(v) for v in T.all_coeffs()]
            pi = arb.pi()
            calls = [0]

            def evaluate_trace(w):
                value = acb(0)
                for q in trace_coeffs:
                    value = value*w+q
                return value

            def integrand(u, analytic):
                calls[0] += 1
                angle = u*pi
                a = evaluate_trace(2*(2*angle).cos())/2
                b = evaluate_trace(2*(3*angle).cos())/3
                c = evaluate_trace(2*(5*angle).cos())/5
                e,f,g = b**2-a**3, 2*c**2-3*a**5, c**3-2*b**5
                q = e**2+f**2+g**2
                # Forward the analytic flag: the integrator must reject boxes
                # crossing the logarithm's branch cut or containing a zero.
                return q.log(analytic=analytic)

            integral = acb.integral(integrand,0,1,rel_tol=tolerance,abs_tol=tolerance,
                                    deg_limit=100,eval_limit=200000,depth_limit=30)
            assert integral.is_finite() and integral.imag.contains(0)
            haar = integral.real
            quantities = {"haar":haar,"original":original_mean,"log2":logtwo,
                          "haar_minus_log2":haar-logtwo,
                          "original_minus_log2":original_mean-logtwo,
                          "original_minus_haar":original_mean-haar}
            result = {"name":name,"p_coefficients_ascending":pcoeffs,"degree":d,
                      "trace_coefficients_ascending":coefficients(T),
                      "global_defect_coefficients":{k:coefficients(v) for k,v in zip(("e","f","g"),(eg,fg,gg))},
                      "global_defect_gcd":str(common.as_expr()),
                      "h_trace_coefficients":coefficients(h,r),"trace_norm":str(normtrace),
                      "original_norm":str(normtrace**2),
                      "quantities":{k:certified(v) for k,v in quantities.items()},
                      "integral_imaginary_ball":integral.imag.str(50,more=True),
                      "integrand_evaluations":calls[0]}
            completed.append(result)
            save("partial.json",{"complete":False,"inputs":completed})
            print(name, "I",result["quantities"]["haar"]["decimal"],
                  "Lambda",result["quantities"]["original"]["decimal"],
                  "Lambda-I",result["quantities"]["original_minus_haar"]["decimal"],flush=True)
        save("results.json",{"complete":True,"object":"C155 original B3, L=972000",
                             "method":"Direct analytic acb quadrature on u in [0,1], theta=pi*u",
                             "precision_bits":192,"flint_version":flint.__version__,
                             "absolute_tolerance_goal":"1e-18","relative_tolerance_goal":"1e-18",
                             "reported_absolute_error_bound":"1e-10","inputs":completed})
        (OUTPUT/"partial.json").unlink()
    except Exception as error:
        save("partial.json",{"complete":False,"error":repr(error),"inputs":completed})
        raise


if __name__=="__main__":
    if sys.argv[1:]==["--worker"]:
        worker()
    elif not sys.argv[1:]:
        try:
            run=subprocess.run([sys.executable,"-B",str(Path(__file__).resolve()),"--worker"],timeout=TIMEOUT_SECONDS)
            raise SystemExit(run.returncode)
        except subprocess.TimeoutExpired:
            print("Author integration stopped at its 300-second bound; partial output is not complete.",file=sys.stderr)
            raise SystemExit(124)
    else:
        raise SystemExit("No input or auxiliary changes are supported.")
