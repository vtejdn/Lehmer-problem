"""D124: twelve declared exact adjacent-window edge eliminations, author pilot.

The rational projection recipe is reused from J56, with both windows rebuilt.
This is author computation, not independent review or an all-input theorem.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from functools import reduce
from math import gcd
import json
import time
import sympy as sp

t, x = sp.symbols("t x")
START = time.monotonic()
CAP = 120


def coefficients(f):
    return [int(f.nth(i)) for i in range(int(f.degree()) + 1)]


def content(f):
    return reduce(gcd, map(abs, coefficients(f)))


def energy(f):
    return sum(a*a for a in coefficients(f))


def center(P, j):
    d, N = int(P.degree()), 2*j + 1
    B = sp.zeros(N, N-d)
    for k in range(N-d):
        for i in range(d+1):
            B[k+i,k] = P.nth(i)
    e = sp.zeros(N, 1)
    e[j] = 1
    r = e - B*((B.T*B).inv()*B.T*e)
    assert B.T*r == sp.zeros(N-d, 1)
    assert r[j] == (r.T*r)[0]
    den = sp.ilcm(*(a.q for a in r))
    raw = [int(a*den) for a in r]
    c = reduce(gcd, map(abs, raw))
    q = sp.Rational(den,c)
    assert q.q == 1 and q >= 2
    F = sp.Poly(sum((a//c)*t**i for i,a in enumerate(raw)),t)
    assert content(F) == 1
    assert (F-sp.Poly(q*t**j,t)).rem(P).is_zero
    PF = P*F
    A = sp.Poly(sum(PF.nth(i)*t**i for i in range(d)),t)
    edgeB = sp.Poly(sum(A.nth(d-1-i)*t**i for i in range(d)),t)
    assert content(A) == content(edgeB) == 1
    assert PF == A + sp.Poly(t**N,t)*edgeB
    assert int(sp.resultant(P,F,t)) == int(q)**d
    return F,A,edgeB,int(q),str(r[j])


def trace_form(f, s):
    """Given f=t^s V(t+1/t), extract V by triangular integer subtraction."""
    remainder = f
    ans = sp.Poly(0,x)
    for k in range(s,-1,-1):
        a = remainder.nth(s+k)
        basis = sp.Poly(sp.expand(t**s*(t+1/t)**k),t)
        remainder -= a*basis
        ans += sp.Poly(a*x**k,x)
    assert remainder.is_zero
    assert sp.Poly(sp.expand(t**s*ans.as_expr().subs(x,t+1/t)),t) == f
    return ans


def weighted_energy(V):
    f = sp.Poly((4-x*x)*V.as_expr()**2,x)
    total = sum(f.nth(2*k)*sp.binomial(2*k,k) for k in range(int(f.degree())//2+1))
    return int(total)


def one(name, expr, j):
    if time.monotonic()-START > CAP:
        raise TimeoutError("Declared total 120-second author pilot cap exceeded")
    P = sp.Poly(expr,t)
    d = int(P.degree())
    assert d%2 == 0 and P.LC() == P.nth(0) == 1
    assert coefficients(P) == coefficients(P)[::-1]
    assert P.is_irreducible and P.eval(1)<0
    F,A,B,q,l = center(P,j)
    Fn,An,Bn,qn,ln = center(P,j+1)
    H = An*B-sp.Poly(t*t,t)*A*Bn
    C = H.exquo(P)
    assert C == Fn*B-sp.Poly(t*t,t)*F*Bn
    row = {"name":name,"P":coefficients(P),"d":d,"j":j,"N":2*j+1,
           "q":q,"q_next":qn,"centered_norm_squared":l,"next_centered_norm_squared":ln,
           "F":coefficients(F),"F_next":coefficients(Fn),"A":coefficients(A),
           "B":coefficients(B),"A_next":coefficients(An),"B_next":coefficients(Bn),
           "C_zero":bool(C.is_zero)}
    if C.is_zero:
        row.update({"shift_plateau":bool(q*Fn == qn*sp.Poly(t,t)*F),"all_exact_checks_passed":True})
        return row
    assert C.degree()<=d
    assert all(C.nth(i) == -C.nth(d-i) for i in range(d+1))
    assert P.gcd(C).degree() == 0
    W = qn*B-q*sp.Poly(t,t)*Bn
    assert (C-sp.Poly(t**(j+1),t)*W).rem(P).is_zero
    c = content(C)
    C0 = C.exquo(sp.Poly(c,t))
    Q = trace_form(P,d//2)
    V = trace_form(C.exquo(sp.Poly(t*t-1,t)),d//2-1)
    assert content(V) == c and energy(C) == weighted_energy(V)
    V0 = V.exquo(sp.Poly(c,x))
    rC,rC0,rW = (int(sp.resultant(P,Z,t)) for Z in (C,C0,W))
    rQV,rQV0 = (int(sp.resultant(Q,Z,x)) for Z in (V,V0))
    cyclic = int(P.eval(1)*P.eval(-1))
    assert rC == rW == cyclic*rQV*rQV
    assert rC0 == cyclic*rQV0*rQV0 and rC == c**d*rC0
    sign = int(sp.sign(rC0*rC0-energy(C0)**d))
    assert sign == int(sp.sign(rC*rC-energy(C)**d))
    row.update({"C":coefficients(C),"C_degree":int(C.degree()),"C_content":c,
                "C_primitive":coefficients(C0),"C_primitive_energy":energy(C0),
                "Q":coefficients(Q),"V":coefficients(V),"V_primitive":coefficients(V0),
                "C_resultant":rC,"C_primitive_resultant":rC0,
                "trace_resultant":rQV0,"time_two_resultant":cyclic,
                "net_margin_sign":sign,"all_exact_checks_passed":True})
    return row


def main():
    specs=[]
    for name,P in (
        ("quartic",t**4-t**3-t**2-t+1),
        ("degree_six",t**6-t**5-t**3-t+1),
        ("lehmer",t**10+t**9-t**7-t**6-t**5-t**4-t**3+t+1)):
        d=int(sp.degree(P,t))
        specs.extend((name,P,j) for j in (d-1,d,2*d-1))
    specs.extend(("quadratic_a3",t**2-3*t+1,j) for j in (1,4))
    specs.append(("radical_a4_q2",t**4-4*t**2+1,4))
    assert len(specs)==12
    rows=[one(*spec) for spec in specs]
    result={'scope': 'twelve declared exact adjacent centered-window pairs', 'rows': rows, 'all_passed': all((row['all_exact_checks_passed'] for row in rows))}
    assert time.monotonic()-START<=CAP
    dest=(_J_OUTPUT / 'verification.json')
    assert not dest.exists(), 'Preserve existing author output; redirect independent replays explicitly'
    dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'rows': len(rows), 'all_passed': result['all_passed'], 'controls': [[r['name'], r['j'], r['C_zero'], r.get('C_primitive'), r.get('net_margin_sign')] for r in rows]}))


if __name__=='__main__':
    main()
