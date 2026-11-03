"""Two H35 logarithmic integrals via the unreduced trace defect.

The accepted J99 V enclosures are explicit retained inputs. No parameter grid
or old component recomputation is performed. All root contributions use Jensen.
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
PRIOR = ROOT / "mathematics/computations/outputs/Yin_J_G0099/results.json"
OUTPUT = ROOT / "mathematics/computations/outputs" / HERE.name
EXPECTED = [("quartic_Salem_seed", [1,-1,-1,-1,1]),
            ("Lehmer_degree10", [1,1,0,-1,-1,-1,-1,-1,0,1,1])]
PRECISIONS = (256,512)
TIMEOUT_SECONDS = 300


def save(name, payload):
    OUTPUT.mkdir(parents=True,exist_ok=True)
    pending = OUTPUT/(name+".writing")
    pending.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    pending.replace(OUTPUT/name)


def worker():
    import sympy as s
    import flint
    from flint import arb,acb_poly,ctx,fmpz_poly
    native=json.loads(INPUT.read_text(encoding="utf-8"))
    selected=[(x["name"],x["coefficients_ascending"]) for x in native["inputs"] if x["name"] in dict(EXPECTED)]
    assert selected==EXPECTED
    prior=json.loads(PRIOR.read_text(encoding="utf-8"))
    assert prior["complete"] and prior["reported_absolute_error_bound"]=="1e-10"
    assert [(x["name"],x["p_coefficients_ascending"]) for x in prior["inputs"]]==EXPECTED
    t,z=s.symbols("t z")
    completed=[]

    def certified(x):
        assert x.is_finite() and x.rad()<arb("1e-12")
        persisted=x.str(50,more=True)
        assert arb(persisted).contains(x)
        with localcontext() as dc:
            dc.prec=65
            decimal=format(Decimal(x.mid().str(50,radius=False)).quantize(Decimal("1e-12")),"f")
        assert abs(arb(persisted)-arb(decimal))<arb("1e-10")
        return {"ball":persisted,"decimal":decimal,"absolute_error_bound":"1e-10",
                "sign":"positive" if x>0 else "negative" if x<0 else "undetermined"}

    try:
        for (name,pc),old in zip(EXPECTED,prior["inputs"]):
            d=len(pc)-1;r=d//2
            P=s.Poly(sum(c*t**i for i,c in enumerate(pc)),t,domain=s.ZZ)
            assert pc==pc[::-1] and pc[0]==pc[-1]==1
            assert P.is_irreducible and not P.is_cyclotomic
            cheb=[s.Poly(2,z),s.Poly(z,z)]
            for k in range(2,max(r,5)+1):cheb.append(s.Poly(z,z)*cheb[-1]-cheb[-2])
            T=s.Poly(pc[r],z)
            for k in range(1,r+1):T+=pc[r+k]*cheb[k]
            assert T.is_irreducible and T.degree()==r
            assert s.expand(t**r*T.as_expr().subs(z,t+1/t)-P.as_expr())==0
            intervals=T.intervals(eps=s.Rational(1,2**50))
            assert sum(m for _,m in intervals)==r and all(m==1 for _,m in intervals)
            b=s.Poly(T.compose(cheb[3]).as_expr()/3,z,domain=s.QQ)
            c=s.Poly(T.compose(cheb[5]).as_expr()/5,z,domain=s.QQ)
            g=c**3-2*b**5
            shift=int(g.degree())
            assert shift==15*d//2
            centered=s.Poly(s.expand(t**shift*g.as_expr().subs(z,t+1/t)),t,domain=s.QQ)
            denominator,integer=centered.clear_denoms(convert=True)
            poly=fmpz_poly([int(integer.nth(i)) for i in range(int(integer.degree())+1)])
            assert poly.degree()==15*d and denominator>0
            content,factors=poly.factor_squarefree()
            product=fmpz_poly([content])
            for factor,mult in factors:
                assert factor.gcd(factor.derivative()).degree()==0
                product*=factor**mult
            assert product==poly
            attempts=[];record=None
            for bits in PRECISIONS:
                ctx.prec=bits
                try:
                    measure=arb(abs(int(poly[poly.degree()]))).log()
                    degree=0;evidence=[]
                    for factor,mult in factors:
                        roots=acb_poly(factor).roots(tol=arb("1e-30"),maxprec=bits)
                        assert len(roots)==factor.degree()
                        assert all(not roots[i].overlaps(roots[j]) for i in range(len(roots)) for j in range(i))
                        degree+=len(roots)*mult
                        points=[]
                        for root in roots:
                            term=arb(1).max(abs(root)).log()
                            measure+=mult*term
                            points.append({"real":root.real.str(50,more=True),"imag":root.imag.str(50,more=True),
                                           "log_plus_modulus":certified(term)})
                        evidence.append({"factor_coefficients_ascending":[int(x) for x in factor],
                                         "multiplicity":mult,"roots":points})
                    assert degree==poly.degree()
                    jg=2*(measure-arb(int(denominator)).log())
                    jv=arb(old["quantities"]["J_V"]["ball"])
                    assert jv.is_finite() and jv.rad()<arb("1e-12")
                    assert old["quantities"]["J_V"]["absolute_error_bound"]=="1e-10"
                    log2=arb(2).log();screen=jg+jv+log2
                    values={"J_G":jg,"J_V_reused":jv,"log2":log2,"screen_sum":screen,
                            "all_s_q_lower_envelope":log2+screen/2,
                            "envelope_minus_log2":screen/2}
                    quantities={k:certified(v) for k,v in values.items()}
                    assert screen>0 or screen<0
                    record={"name":name,"p_coefficients_ascending":pc,"degree":d,
                            "trace_coefficients_ascending":[str(T.nth(i)) for i in range(r+1)],
                            "global_g_coefficients_ascending":[str(g.nth(i)) for i in range(shift+1)],
                            "centered_g_integer_coefficients_ascending":[int(x) for x in poly],
                            "centered_g_scalar_denominator":int(denominator),"centering_shift":shift,
                            "squarefree_content":int(content),"degree_with_multiplicity":degree,
                            "factor_root_evidence":evidence,"precision_bits":bits,
                            "earlier_unresolved_attempts":attempts,"quantities":quantities,
                            "screen":"excluded_all_real_s_positive_q" if screen>0 else "screen_inconclusive",
                            "parameter_grid_evaluations":0}
                    break
                except (ValueError,ArithmeticError,AssertionError) as error:
                    attempts.append({"bits":bits,"error":repr(error)})
            if record is None:raise ArithmeticError(f"{name}: precision ceiling exhausted: {attempts}")
            completed.append(record)
            save("partial.json",{"complete":False,"inputs":completed})
            print(name,{k:v["decimal"] for k,v in record["quantities"].items()},record["screen"],flush=True)
        save("results.json",{"complete":True,"object":"buffered shear all-parameter component screen",
                             "flint_version":flint.__version__,"sympy_version":s.__version__,
                             "prior_V_source":"mathematics/computations/outputs/Yin_J_G0099/results.json",
                             "precision_schedule_bits":list(PRECISIONS),"batch_timeout_seconds":TIMEOUT_SECONDS,
                             "reported_absolute_error_bound":"1e-10","inputs":completed,
                             "new_distinct_component_integrals":2,"parameter_grid_evaluations":0})
        (OUTPUT/"partial.json").unlink()
    except Exception as error:
        save("partial.json",{"complete":False,"error":repr(error),"inputs":completed})
        raise


if __name__=="__main__":
    if sys.argv[1:]==["--worker"]:worker()
    elif not sys.argv[1:]:
        try:
            result=subprocess.run([sys.executable,"-B",str(Path(__file__).resolve()),"--worker"],timeout=TIMEOUT_SECONDS)
            raise SystemExit(result.returncode)
        except subprocess.TimeoutExpired:
            print("Stopped at the 300-second author cap; no complete result asserted.",file=sys.stderr)
            raise SystemExit(124)
    else:raise SystemExit("Only the fixed two-input component screen is supported.")
