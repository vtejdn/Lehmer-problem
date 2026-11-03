"""D171 actual selected anti columns. Three exact inputs, fifteen windows,120s total cap.
No search, expansion, numerical roots, or old program/result imports.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from time import perf_counter
import json, math, platform, traceback
import sympy as sp

HERE=(_J_PROGRAM / 'verify.py').parent
START=perf_counter(); CAP=120
t,x,y=sp.symbols('t x y')

# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def tick():
    if perf_counter()-START>CAP:raise TimeoutError('Declared120-second aggregate author cap exceeded')

def coeff(f,z=t,length=None):
    p=sp.Poly(f,z)
    n=int(p.degree())+1 if length is None else length
    return [int(p.nth(j)) for j in range(n)]

def poly(v,z):return sum(a*z**j for j,a in enumerate(v))
def ml(M):return [[int(v) for v in row] for row in M.tolist()]
def il(M):return [int(v) for v in M]
def content(v):return math.gcd(*[abs(int(a)) for a in v])

def norm(f,Q):return int(sp.resultant(Q,f,x))

def trace(f,Q,s):
    return sp.cancel(sum(sp.Poly(sp.rem(f*x**j,Q,x),x).nth(j) for j in range(s)))

def anti(c,n):return sp.expand(sum(c[l-1]*(t**(n+l)-t**(n-l)) for l in range(1,n+1)))

def edge(F,P,n,d):
    whole=sp.Poly(sp.expand(P*F),t)
    A=sum(whole.nth(j)*t**j for j in range(d))
    star=sum(whole.nth(j)*t**(d-1-j) for j in range(d))
    assert sp.expand(P*F-A+t**(2*n+1)*star)==0
    return sp.expand(A)

def costs(F):
    cs=coeff(F);inds=[j for j,a in enumerate(cs) if a]
    assert inds
    e=sum(a*a for a in cs);l1=sum(map(abs,cs))
    return dict(actual_degree=len(cs)-1,monomial_degree=inds[0],degree_without_monomial=len(cs)-1-inds[0],
                content=content(cs),height=max(map(abs,cs)),leading_coefficient=cs[-1],
                S1=l1,S2_squared=e,rho=str(sp.Rational(l1*l1,e)),
                mahler_lower_leading=abs(cs[-1]),mahler_upper_squared=e)

def trace_polynomial(P,s):
    residual=sp.expand(P/t**s);Q=0
    for j in range(s,-1,-1):
        a=sp.expand(residual).coeff(t,j);Q+=a*x**j
        residual=sp.expand(residual-a*(t+1/t)**j)
    assert residual==0 and sp.expand(t**s*Q.subs(x,t+1/t)-P)==0
    return sp.expand(Q)

def main():
    inputs=[('quartic',t**4-t**3-t**2-t+1),('sextic',t**6-t**5-t**3-t+1),
            ('Lehmer',t**10+t**9-t**7-t**6-t**5-t**4-t**3+t+1)]
    results=[];basis_count=0;diagonal_count=0
    for label,P in inputs:
        tick();d=sp.degree(P,t);d=int(d);s=d//2
        assert sp.Poly(P,t).is_irreducible
        Q=trace_polynomial(P,s);assert sp.Poly(Q,x).is_irreducible
        qc=coeff(Q,x);S=sp.Matrix(s,s,lambda i,j:qc[i+j+1] if i+j<s else 0)
        assert S.det()==(-1)**(s*(s-1)//2)
        kernel=sum(S[i,j]*x**i*y**j for i in range(s) for j in range(s))
        assert sp.expand((x-y)*kernel-Q+Q.subs(x,y))==0
        U=[sp.Integer(1),x]
        for j in range(2,3*s):U.append(sp.expand(x*U[-1]-U[-2]))
        inv_t=sp.invert(t,P,t);tau_t=t+inv_t
        inv_qprime=sp.invert(sp.diff(Q,x),Q,x)
        windows=[]
        for n in [s,2*s-1,2*s,2*s+1,3*s]:
            tick()
            remainders=[sp.rem(U[j],Q,x) for j in range(n)]
            R=sp.Matrix.hstack(*[sp.Matrix(coeff(z,x,s)) for z in remainders])
            H=R*R.T;Delta=int(H.det());Hi=H.inv();assert Delta>0
            ell=[(R[:,j].T*Hi*R[:,j])[0] for j in range(n)]
            assert all(a>0 for a in ell) and sum(ell)==s
            minimizers=[j+1 for j,a in enumerate(ell) if a==min(ell)];k=minimizers[0]
            rk=R[:,k-1];delta=content(rk);u=rk/delta
            v=H.adjugate()*u;gamma=content(v);assert Delta%gamma==0
            L=Delta//gamma;w=v/gamma;q=sp.Rational(L,delta)
            assert w==q*Hi*rk and content(w)==1 and H*w==L*u
            assert all(a.q==1 for a in w)
            c=R.T*w;F=anti(c,n);A=edge(F,P,n,d);aw=poly(il(S*w),x)
            expA=sp.rem(sp.expand(t**(n+s)*aw.subs(x,tau_t)),P,t)
            assert sp.expand(expA-A)==0
            basis_edges=[]
            for j in range(s):
                tick();ej=sp.eye(s)[:,j]
                Fj=anti(R.T*ej,n);Aj=edge(Fj,P,n,d);aj=poly(il(S*ej),x)
                expected=sp.rem(sp.expand(t**(n+s)*aj.subs(x,tau_t)),P,t)
                assert sp.expand(Aj-expected)==0
                basis_edges.append(coeff(Aj));basis_count+=1
            dual_values=[trace(sp.rem(aw*U[j]*inv_qprime,Q,x),Q,s) for j in range(n)]
            assert dual_values==list(c)
            vpoly=poly(il(H*w),x);upoly=poly(il(u),x)
            nf=int(sp.resultant(P,F,t));na=int(sp.resultant(P,A,t))
            nt=norm(aw,Q);nu=norm(upoly,Q);nv=norm(vpoly,Q)
            endpoint=int(P.subs(t,1)*P.subs(t,-1))
            assert nf==endpoint*nv*nv==L**d*endpoint*nu*nu and na==nt*nt>0
            cyc=int(sp.resultant(P,t**(2*k)-1,t));assert nf==q**d*cyc
            fc,ac=costs(F),costs(A)
            assert fc['content']==ac['content']==content(coeff(aw,x))==1
            assert fc['S2_squared']==2*(w.T*H*w)[0]==2*q*q*ell[k-1]
            frem=sp.rem(F,P,t);order_content=content(coeff(frem,t,d))
            assert order_content%L==0 and fc['height']<=Delta
            basis_record=dict(R=ml(R),H=ml(H),Delta=Delta,S_Q=ml(S),all_projection_diagonals=[str(z) for z in ell],
                minimizing_indices=minimizers,selected_index=k,delta=delta,u=il(u),gamma=gamma,L=L,q=str(q),
                w=il(w),c=il(c),trace_edge_coefficients=coeff(aw,x,s),trace_value_coefficients=coeff(vpoly,x,s),
                F_coefficients=coeff(F),A_coefficients=coeff(A),basis_edge_coefficients=basis_edges,
                dual_trace_coefficients=[int(z) for z in dual_values],F_resultant=nf,A_resultant=na,
                trace_edge_norm=nt,primitive_trace_remainder_norm=nu,cyclic_resultant=cyc,
                endpoint_product=endpoint,F_cost=fc,A_cost=ac,actual_order_remainder=coeff(frem,t,d),
                actual_order_remainder_content=order_content,L_prime_factors={str(p):int(e) for p,e in sp.factorint(L).items()},
                full_net_ratio=str(sp.Rational(abs(nf),fc['S2_squared']**s)),
                edge_to_F_energy_ratio=str(sp.Rational(na,fc['S2_squared']**s)),
                scalar_floor_energy_squared_ratio=str(sp.Rational(L*L,fc['S2_squared'])),
                radial_charge_multiple_of_m=str(sp.Rational(fc['degree_without_monomial'],d)),
                edge_is_unit=(abs(nt)==1))
            windows.append(dict(n=n,**basis_record));diagonal_count+=n
        results.append(dict(label=label,P_coefficients=coeff(P),Q_coefficients=qc,actual_degree=d,trace_degree=s,
                            original_irreducible=True,trace_irreducible=True,windows=windows))
    assert basis_count==50 and diagonal_count==100
    return dict(scope='Exactly three named actual inputs and n in {s,2s-1,2s,2s+1,3s};15 windows;120s aggregate cap',
                coefficient_order='ascending',inputs=results,window_count=15,basis_edges_checked=basis_count,
                projection_diagonals_checked=diagonal_count,all_exact_checks_passed=True)

if __name__=='__main__':
    try:
        result=main();tick()
        pass
        ((_J_OUTPUT / 'result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'passed':True,'windows':15,'basis_edges':50,'projection_diagonals':100}))
    except BaseException:
        fail=dict(traceback=_record_text(traceback.format_exc()))
        dest=(_J_OUTPUT / 'failure.json');i=1
        dest.write_text(json.dumps(fail,indent=2)+'\n',encoding='utf-8');raise
