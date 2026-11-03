"""A<=12 exact trinomial residual pilot, hard 120-second arithmetic deadline.

Factorization, cyclotomic flags and reciprocal trace root counts are exact.
NumPy Mahler estimates are explicitly discovery-only; no conclusion uses
their numerical precision as a certificate.
"""

from math import gcd, log
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time
import signal

import numpy as np
import sympy as sp

HERE = (_J_PROGRAM / 'pilot.py').parent
t,x = sp.symbols("t x")
CAP_SECONDS = 120


def chebyshev(n):
    if n==0:return sp.Integer(2)
    previous,current = sp.Integer(2),x
    for _ in range(1,n):previous,current = current,sp.expand(x*current-previous)
    return current


def trace_polynomial(poly):
    d = poly.degree()
    coeff = poly.all_coeffs()
    if d%2 or coeff != coeff[::-1]:return None
    s = d//2
    return sp.Poly(poly.nth(s)+sum(poly.nth(s+j)*chebyshev(j) for j in range(1,s+1)),x)


def approximate_measure(poly):
    coefficients = np.array([float(v) for v in poly.all_coeffs()])
    roots = np.roots(coefficients)
    return float(log(abs(coefficients[0]))+sum(max(0.0,log(abs(z))) for z in roots))


def main():
    started = time.perf_counter()
    # Windows's exact SymPy operations are synchronous. A daemon watchdog
    # interrupts the main thread, and finally retains every completed row.
    import threading,_thread
    timer = threading.Timer(CAP_SECONDS,_thread.interrupt_main)
    timer.daemon = True
    timer.start()
    rows = []
    completed = False
    stopped = None
    try:
        for a in range(2,13):
            for b in range(1,a):
                if gcd(a,b)!=1:continue
                assert time.perf_counter()-started<CAP_SECONDS
                seed = sp.Poly(t**a-t**b-1,t)
                reverse = 1-t**(a-b)-t**a
                G = sp.Poly(sp.expand((reverse**2*seed.as_expr().subs(t,t*t)+seed.as_expr()**2*reverse.subs(t,t*t))/2),t)
                assert G.eval(1)==-1
                ell = min(b,a-b)
                W = sp.Poly(sp.div(G.as_expr(),t**ell,t)[0],t)
                assert sp.expand(G.as_expr()-t**ell*W.as_expr())==0
                trace = sp.Poly(chebyshev(a+b)+chebyshev(2*a-b)-chebyshev(2*b)-2*chebyshev(b)+chebyshev(abs(a-2*b))-1,x)
                assert trace_polynomial(W)==trace
                assert W.all_coeffs()==W.all_coeffs()[::-1]
                content,factors = sp.factor_list(W)
                entries = []
                for fac,multiplicity in factors:
                    cyclotomic = bool(fac.is_cyclotomic)
                    T = trace_polynomial(fac)
                    entry = {"polynomial":str(fac.as_expr()),"coefficients_descending":[int(c) for c in fac.all_coeffs()],
                             "degree":fac.degree(),"multiplicity":multiplicity,
                             "monic":fac.LC()==1,"cyclotomic":cyclotomic,
                             "reciprocal":T is not None}
                    if T is not None and not cyclotomic:
                        inside = int(T.count_roots(-2,2))
                        positive = int(T.count_roots(2,sp.oo))
                        negative = int(T.count_roots(-sp.oo,-2))
                        nonreal = T.degree()-inside-positive-negative
                        assert T.eval(-2)!=0 and T.eval(2)!=0
                        expanding = T.degree()-inside
                        entry.update({"trace_polynomial":str(T.as_expr()),"trace_coefficients_descending":[int(c) for c in T.all_coeffs()],
                                      "unit_circle_pairs":inside,"positive_real_expanding":positive,
                                      "negative_real_expanding":negative,"nonreal_trace_roots":nonreal,
                                      "total_expanding_roots":expanding,
                                      "type":"Salem" if fac.LC()==1 and positive==1 and expanding==1 else
                                             "negative_Salem" if fac.LC()==1 and negative==1 and expanding==1 else
                                             "multiple_expanding" if expanding>1 else "nonmonic_one_expanding"})
                    elif not cyclotomic:
                        entry["type"] = "nonreciprocal_unclassified"
                    entry["discovery_log_M"] = approximate_measure(fac)
                    entries.append(entry)
                mf = approximate_measure(seed)
                mg = log(abs(float(content)))+sum(e["multiplicity"]*e["discovery_log_M"] for e in entries)
                rows.append({"a":a,"b":b,"ell":ell,"W_degree":W.degree(),"W_leading":int(W.LC()),
                             "content":int(content),"factors":entries,"discovery_m_f":mf,"discovery_m_G":mg,
                             "discovery_delta":log(2)+mg-3*mf})
        completed = True
    except KeyboardInterrupt:
        stopped = "120-second execution watchdog"
    except AssertionError:
        stopped = "deadline or mathematical assertion; see exception"
        raise
    finally:
        timer.cancel()
        result = {'completed': completed, 'stop': stopped, 'range': '2<=a<=12, 0<b<a, gcd(a,b)=1', 'rows': rows, 'root_classification': 'Exact irreducible factorization and trace Sturm root counts where reciprocal. Nonreciprocal factors are explicitly unclassified.', 'measure_values': 'NumPy-root discovery estimates only; not validated bounds or rankings.'}
        ((_J_OUTPUT / 'pilot.json')).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print("completed",completed,"rows",len(rows))
    for row in rows:
        factors = [(v["degree"],v.get("type","cyclotomic"),v.get("total_expanding_roots")) for v in row["factors"]]
        print(row["a"],row["b"],factors,"Delta discovery",round(row["discovery_delta"],8))


if __name__ == "__main__":main()
