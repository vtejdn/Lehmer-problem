"""Bounded Stage1 component-log screen for two original reciprocal inputs.

U uses analytic ball integration of unreduced trace defects when their exact
gcd proves positivity. V uses complete-root Jensen with exact multiplicities.
No q-grid is evaluated by this Stage1 program.
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
EXPECTED = [
    ("quartic_Salem_seed", [1, -1, -1, -1, 1]),
    ("Lehmer_degree10", [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]),
]
TIMEOUT_SECONDS = 300
PRECISIONS = (256, 512)


class Unresolved(Exception):
    pass


def save(name, payload):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pending = OUTPUT / (name + ".writing")
    pending.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    pending.replace(OUTPUT / name)


def worker():
    import flint
    from flint import acb, acb_poly, arb, ctx, fmpz_poly
    import sympy as s

    source = json.loads(INPUT.read_text(encoding="utf-8"))
    selected = [(p["name"], p["coefficients_ascending"])
                for p in source["inputs"] if p["name"] in dict(EXPECTED)]
    assert selected == EXPECTED
    t, z = s.symbols("t z")
    completed = []

    def coeffs(poly):
        return [str(poly.nth(i)) for i in range(int(poly.degree()) + 1)]

    def ball(x):
        if not x.is_finite() or not x.rad() < arb("1e-12"):
            raise Unresolved("nonfinite or insufficient scalar enclosure")
        persisted = x.str(50, more=True)
        assert arb(persisted).contains(x)
        with localcontext() as dec:
            dec.prec = 65
            center = format(Decimal(x.mid().str(50, radius=False)).quantize(Decimal("1e-12")), "f")
        assert abs(arb(persisted) - arb(center)) < arb("1e-10")
        return {"ball": persisted, "decimal": center, "absolute_error_bound": "1e-10",
                "sign": "positive" if x > 0 else "negative" if x < 0 else "undetermined"}

    def centered(trace_poly):
        # Exact t^n F(t+t^-1); no reduction modulo the original trace T.
        n = int(trace_poly.degree())
        value = s.Poly(s.expand(t**n * trace_poly.as_expr().subs(z, t+1/t)), t, domain=s.QQ)
        denominator, integer = value.clear_denoms(convert=True)
        assert integer.degree() == 2*n
        return int(denominator), fmpz_poly([int(integer.nth(i)) for i in range(2*n+1)]), n

    def jensen(poly, bits):
        content, factors = poly.factor_squarefree()
        product = fmpz_poly([content])
        value = arb(abs(int(poly[poly.degree()]))).log()
        count = 0
        evidence = []
        for factor, multiplicity in factors:
            product *= factor**multiplicity
            assert factor.gcd(factor.derivative()).degree() == 0
            try:
                roots = acb_poly(factor).roots(tol=arb("1e-30"), maxprec=bits)
            except ValueError as error:
                raise Unresolved(str(error)) from error
            if len(roots) != factor.degree():
                raise Unresolved("incomplete isolated-root count")
            assert all(not roots[i].overlaps(roots[j]) for i in range(len(roots)) for j in range(i))
            count += len(roots)*multiplicity
            records = []
            for root in roots:
                contribution = arb(1).max(abs(root)).log()
                value += multiplicity*contribution
                records.append({"real":root.real.str(50, more=True),
                                "imag":root.imag.str(50, more=True),
                                "log_plus_modulus":ball(contribution)})
            evidence.append({"factor_coefficients_ascending":[int(x) for x in factor],
                             "multiplicity":multiplicity,"roots":records})
        assert product == poly and count == poly.degree()
        return value, {"content":int(content),"degree_with_multiplicity":count,"factors":evidence}

    try:
        for name, pc in EXPECTED:
            P = s.Poly(sum(c*t**i for i,c in enumerate(pc)),t,domain=s.ZZ)
            d, r = P.degree(), P.degree()//2
            assert P.is_irreducible and not P.is_cyclotomic
            assert pc == pc[::-1] and pc[0] == pc[-1] == 1
            cheb = [s.Poly(2,z),s.Poly(z,z)]
            for k in range(2,max(r,5)+1):
                cheb.append(s.Poly(z,z)*cheb[-1]-cheb[-2])
            T = s.Poly(P.nth(r),z)
            for k in range(1,r+1):
                T += P.nth(r+k)*cheb[k]
            assert T.is_irreducible and T.degree()==r
            assert s.expand(t**r*T.as_expr().subs(z,t+1/t)-P.as_expr()) == 0
            intervals = T.intervals(eps=s.Rational(1,2**50))
            assert sum(m for _,m in intervals)==r and all(m==1 for _,m in intervals)
            a,b,c = (s.Poly(T.compose(cheb[p]).as_expr()/p,z,domain=s.QQ) for p in (2,3,5))
            e,f,g = b**2-a**3,2*c**2-3*a**5,c**3-2*b**5
            common = s.gcd(e,g)
            den_v, poly_v, shift_v = centered(f)
            assert shift_v == 5*d and poly_v.degree()==10*d
            trace_desc = [int(v) for v in T.all_coeffs()]
            attempts = []
            result = None
            for bits in PRECISIONS:
                ctx.prec = bits
                try:
                    m_v, v_roots = jensen(poly_v,bits)
                    j_v = 2*(m_v-arb(den_v).log())
                    if common.degree()==0:
                        # e,g cannot vanish together on the real trace line.
                        pi = arb.pi()
                        calls = [0]
                        def evaluate(w):
                            total = acb(0)
                            for q in trace_desc:
                                total = total*w+q
                            return total
                        def integrand(u, analytic):
                            calls[0] += 1
                            angle = u*pi
                            av,bv,cv = (evaluate(2*(p*angle).cos())/p for p in (2,3,5))
                            ev,gv = bv**2-av**3,cv**3-2*bv**5
                            return (ev**2+gv**2).log(analytic=analytic)
                        integral = acb.integral(integrand,0,1,rel_tol=arb("1e-18"),abs_tol=arb("1e-18"),
                                                deg_limit=100,eval_limit=200000,depth_limit=30)
                        if not integral.is_finite() or not integral.imag.contains(0):
                            raise Unresolved("unresolved analytic U integral")
                        j_u = integral.real
                        u_evidence = {"method":"analytic acb quadrature theta=pi*u", "calls":calls[0],
                                      "imaginary_ball":integral.imag.str(50,more=True)}
                    else:
                        den_u, poly_u, shift_u = centered(e**2+g**2)
                        m_u,u_roots = jensen(poly_u,bits)
                        j_u = m_u-arb(den_u).log()
                        u_evidence = {"method":"Jensen fallback for possible common zeros", "denominator":den_u,
                                      "shift":shift_u,"polynomial":[int(x) for x in poly_u],"roots":u_roots}
                    total = j_u+j_v
                    values = {"J_U":j_u,"J_V":j_v,"component_sum":total,"log2":arb(2).log(),
                              "lower_envelope":arb(2).log()+total/2,"lower_envelope_minus_log2":total/2}
                    quantities = {k:ball(v) for k,v in values.items()}
                    if not (total>0 or total<0):
                        raise Unresolved("component-sum sign unresolved")
                    result = {"name":name,"p_coefficients_ascending":pc,"degree":d,
                              "trace_coefficients_ascending":coeffs(T),
                              "global_defect_coefficients":{k:coeffs(v) for k,v in zip(("e","f","g"),(e,f,g))},
                              "global_e_g_gcd":str(common.as_expr()),
                              "V_centered_f_polynomial":[int(x) for x in poly_v],
                              "V_scalar_denominator":den_v,"V_centering_shift":shift_v,
                              "V_root_evidence":v_roots,"U_evidence":u_evidence,
                              "precision_bits":bits,"earlier_unresolved_attempts":attempts,"quantities":quantities,
                              "screen":"excluded_all_positive_q" if total>0 else "stage2_pending",
                              "weighted_grid_evaluations":0}
                    break
                except Unresolved as error:
                    attempts.append({"bits":bits,"reason":str(error)})
            if result is None:
                raise Unresolved(f"{name}: fixed precision limit exhausted: {attempts}")
            completed.append(result)
            save("partial.json",{"complete":False,"inputs":completed})
            print(name,{k:v["decimal"] for k,v in result["quantities"].items()},result["screen"],flush=True)
        save("results.json",{"complete":True,"stage":"component-log screen only","flint_version":flint.__version__,
                             "sympy_version":s.__version__,"precision_schedule_bits":list(PRECISIONS),
                             "reported_absolute_error_bound":"1e-10","batch_timeout_seconds":TIMEOUT_SECONDS,
                             "inputs":completed,"weighted_grid_evaluations":0})
        (OUTPUT/"partial.json").unlink()
    except Exception as error:
        save("partial.json",{"complete":False,"error":repr(error),"inputs":completed})
        raise


if __name__ == "__main__":
    if sys.argv[1:] == ["--worker"]:
        worker()
    elif not sys.argv[1:]:
        try:
            run = subprocess.run([sys.executable,"-B",str(Path(__file__).resolve()),"--worker"],timeout=TIMEOUT_SECONDS)
            raise SystemExit(run.returncode)
        except subprocess.TimeoutExpired:
            print("Stage1 stopped at the 300-second batch cap; partial output is incomplete.",file=sys.stderr)
            raise SystemExit(124)
    else:
        raise SystemExit("Only the declared two-input Stage1 is supported.")
