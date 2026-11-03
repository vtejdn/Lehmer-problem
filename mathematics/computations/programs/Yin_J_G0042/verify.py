"""Bounded exact algebra certificate for D70; no numerical-root premises."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as s

t, u = s.symbols('t u')
H = t**3+6*t**2+21*t+12
J = t**3-42*t**2+21*t-36


def reverse(f):
    d = s.degree(f, t)
    return s.Poly(f, t).all_coeffs()[::-1]


def star(f):
    d = s.degree(f, t)
    return s.expand(t**d*f.subs(t, 1/t))


def matrix(k, absolute=False):
    v = s.eye(4+k)
    for i,j,a in ((0,1,2),(1,2,3),(2,3,2),(0,3,-2)):
        v[i,j] = -abs(a) if absolute else a
    if k: v[1,4] = -1 if absolute else 1
    for i in range(4,3+k): v[i,i+1] = -1 if absolute else 1
    return v


def formula(k, h):
    q,r = s.div(t**(k+2)*h-star(h),t-1,t)
    assert r == 0
    return s.expand(q)


def main():
    rows=[]
    for k in range(7):
        out={'k':k,'dimension':k+4}
        for label,absolute,h in (('original',False,H),('absolute',True,J)):
            v=matrix(k,absolute)
            # Characteristic polynomial is independently computed from the
            # actual integer transformation, not the determinant recurrence.
            f=(-v.inv()*v.T).charpoly(t).as_expr().expand()
            assert f==formula(k,h)
            assert f==star(f)
            assert all(v[i,i]==1 for i in range(k+4))
            assert max(abs(a) for a in v)==3
            assert sum(v[i,j]**2 for i in range(k+4) for j in range(i+1,k+4))==k+21
            out[label]=[int(x) for x in s.Poly(f,t).all_coeffs()]
            out[label+'_factorization']=str(s.factor(f))
        rows.append(out)
    P=formula(2,H)
    U=u**3+7*u**2+25*u+26
    assert s.expand(t**3*U.subs(u,t+1/t))==P
    assert s.Poly(P,t).is_irreducible and s.Poly(U,u).is_irreducible
    assert s.discriminant(s.diff(U,u),u)==-104
    assert U.subs(u,-2)==-4 and U.subs(u,-1)==7
    assert s.expand(H.subs(t,-s.Rational(3,4)))<0<s.expand(H.subs(t,-s.Rational(2,3)))
    assert s.discriminant(H,t)<0 and s.discriminant(J,t)<0
    assert J.subs(t,41)<0<J.subs(t,42)
    assert s.gcd(H,star(H))==1
    assert s.Poly(H,t).is_irreducible
    U3=u**3+6*u**2+19*u+6
    assert s.expand((t+1)*t**3*U3.subs(u,t+1/t))==formula(3,H)
    assert s.discriminant(s.diff(U3,u),u)==-84
    assert U3.subs(u,-s.Rational(1,2))<0<U3.subs(u,0)
    for k in range(7):
        assert formula(k,J).subs(t,1)==-56*k-64
        assert all(c>0 for c in s.Poly(formula(k,H),t).all_coeffs())
    assert 2**6*5>193
    # Exact requested-versus-produced coefficient test, not a successful
    # arbitrary-input realization claim.
    independent_small_salem=t**6-t**5-t**3-t+1
    assert P!=independent_small_salem
    output={'checked_chain_lengths':list(range(7)), 'all_actual_matrix_identities':True,
            'H':str(H),'J':str(J),'degree_six_irreducible':True,
            'degree_six_trace':str(U),'H_discriminant':int(s.discriminant(H,t)),
            'J_discriminant':int(s.discriminant(J,t)), 'rows':rows,
            'scope':'Exact finite checks supplement the all-k written recurrence and bounds; no irreducibility for all k.'}
    (_J_OUTPUT / 'verification.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k!='rows'}))


if __name__=='__main__': main()
