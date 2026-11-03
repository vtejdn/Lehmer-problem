"""Exact declared D154 verification. No discovery search; cap 120 seconds."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from time import perf_counter
import json, sys, traceback
import sympy as sp

HERE=(_J_PROGRAM / 'verify.py').parent
T=sp.Symbol('t'); s=T+1
START=perf_counter()
CAP=120

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
    if perf_counter()-START>CAP:
        raise TimeoutError('Declared aggregate120-second cap exceeded')

def array(M): return [[int(z) for z in row] for row in M.tolist()]
def coeff(p): return [int(z) for z in sp.Poly(sp.expand(p),T).all_coeffs()[::-1]]
def polynomial(V):
    tick()
    assert V.is_upper and all(V[i,i]==1 for i in range(V.rows))
    return sp.Poly((-V.inv()*V.T).charpoly(T).as_expr(),T).as_expr().expand()
def absolute(V):
    n=V.rows
    return sp.Matrix(n,n,lambda i,j: 1 if i==j else (-abs(V[i,j]) if i<j else 0))
def cover(V):
    n=V.rows; W=sp.eye(2*n)
    for i in range(n):
        for j in range(i+1,n):
            a=int(V[i,j])
            if a<=0: W[2*i,2*j]=W[2*i+1,2*j+1]=a
            else: W[2*i,2*j+1]=W[2*i+1,2*j]=-a
    return W

def cost(V):
    return {'rank':V.rows,'height':int(max([abs(V[i,j]) for i in range(V.rows) for j in range(i+1,V.rows)]+[0])),
            'energy':int(sum(V[i,j]**2 for i in range(V.rows) for j in range(i+1,V.rows)))}

def pencil_checks(V,p):
    n=V.rows
    values=[]
    for k in range(n+1):
        tick()
        actual=int((k*V+V.T).det(method='domain-ge'))
        expected=int(p.subs(T,k))
        assert actual==expected
        values.append(actual)
    return values

def full_record(V,label):
    A=absolute(V); W=cover(V)
    p=polynomial(V); a=polynomial(A); w=polynomial(W)
    assert sp.expand(w-p*a)==0
    assert cost(W)['energy']==2*cost(V)['energy']
    return {'label':label,'matrix':array(V),'absolute_matrix':array(A),'proper_cover_matrix':array(W),
            'original_polynomial':coeff(p),'absolute_polynomial':coeff(a),'cover_polynomial':coeff(w),
            'original_cost':cost(V),'absolute_cost':cost(A),'cover_cost':cost(W),
            'pencil_values':{'original':pencil_checks(V,p),'absolute':pencil_checks(A,a),'cover':pencil_checks(W,w)}}

def cyclic(V):
    n=V.rows; Q=sp.zeros(n)
    for j in range(1,n):
        Q[j,j-1]=1; Q[0,j-1]=-V[0,j]
    Q[0,n-1]=-1
    U=Q.T*V*Q
    expected=sp.zeros(n)
    expected[:n-1,:n-1]=V[1:,1:]
    expected[:n-1,n-1]=V[0,1:].T
    expected[n-1,n-1]=1
    assert Q.det() in (-1,1) and U==expected
    return U,Q

def main():
    B=sp.Matrix([[1,1],[0,1],[0,1],[0,1]])
    A=B.T*B; U=sp.eye(6); U[:4,4:]=-B
    P=T**4-T**3-T**2-T+1
    assert polynomial(U)==sp.expand(s**2*P)
    xs=sp.symbols('x0:4'); ys=sp.symbols('y0:2')
    x=sp.Matrix(xs); y=sp.Matrix(ys); c=x.col_join(y); v=B.T*x
    M=T*U+U.T; adj=M.adjugate(method='berkowitz')
    actual=sp.expand((c.T*adj*c)[0])
    D=s*s*sp.eye(2)-T*A
    predicted=sp.expand(s*P*(x.T*x)[0]+s*(T*(v.T*D.adjugate()*v)[0]+s*s*(v.T*D.adjugate()*y)[0]+s*s*(y.T*D.adjugate()*y)[0]))
    assert sp.expand(actual-predicted)==0
    aa,bb=sp.symbols('a b',integer=True)
    xp=sp.Matrix([0,aa,bb,-aa-bb]); N=2*(aa*aa+aa*bb+bb*bb)
    substitutions=dict(zip(xs,list(xp))); substitutions.update(dict(zip(ys,[0,0])))
    assert sp.expand(actual.subs(substitutions)-s*P*N)==0
    extension=sp.expand(s*polynomial(U)-T*actual.subs(substitutions))
    assert sp.expand(extension-s*P*(s*s-T*N))==0
    L=sp.Symbol('L'); z=sp.Symbol('z')
    C=sp.Matrix([[1,1,0],[1,4,L],[0,L,N]])
    chi=sp.expand((z-N)*(z*z-5*z+3)-L*L*(z-1))
    assert sp.expand(C.charpoly(z).as_expr()-chi)==0
    symbolic={'adjugate_coefficients_in_t':[str(sp.expand(actual).coeff(T,k)) for k in range(6)],
              'kernel_norm':str(N),'full_family_original':str(extension),'absolute_gram_characteristic':str(chi),
              'all_symbolic_equalities':True}
    pairs=[(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1),(0,0)]
    records=[]; cyclic_records=[]
    for a,b in pairs:
        xx=sp.Matrix([0,a,b,-a-b]); col=xx.col_join(sp.zeros(2,1))
        V=sp.eye(7); V[:6,:6]=U; V[:6,6]=col
        rec=full_record(V,f'kernel_{a}_{b}')
        n=int((xx.T*xx)[0]); ell=sum(abs(int(z)) for z in xx)
        H=sp.expand(T**3*chi.subs({aa:a,bb:b,L:ell,z:T+2+1/T}))
        assert rec['original_polynomial']==coeff(s*P*(s*s-T*n))
        assert rec['absolute_polynomial']==coeff(s*H)
        rec['parameters']={'a':a,'b':b,'N':n,'L':ell}
        records.append(rec)
        if n==0: continue
        core=U.copy(); coupling=col.copy()
        for phase in range(6):
            W=sp.eye(7); W[:6,:6]=core; W[:6,6]=coupling
            po=polynomial(W); pa=polynomial(absolute(W))
            assert po==sp.expand(s*P*(T*T+1))
            costs=cost(W)
            insertion=[]; last=6
            for rotation in range(7):
                assert polynomial(W)==po
                assert polynomial(absolute(W))==pa
                assert cost(W)==costs
                insertion.append(last)
                W,_=cyclic(W); last=(last-1)%7
            assert sorted(insertion)==list(range(7))
            cyclic_records.append({'a':a,'b':b,'core_phase':phase,'insertion_positions':insertion,
                                   'original_polynomial':coeff(po),'absolute_polynomial':coeff(pa),
                                   'proper_cover_polynomial':coeff(po*pa),'cost':costs})
            core,Q=cyclic(core); coupling=Q.T*coupling
    boundary=sp.Matrix([[1,0,-2,-1],[0,1,0,0],[0,0,1,1],[0,0,0,1]])
    rec=full_record(boundary,'closed_endpoint_lambda4')
    assert rec['original_polynomial']==coeff(s*s*(T-1)**2)
    assert rec['absolute_polynomial']==coeff(s*s*(T*T-6*T+1))
    records.append(rec)
    h=T**3-T**2-7*T-4
    cubic=[int(h.subs(T,k)) for k in (-2,-1,0,3,4)]
    assert cubic==[-2,1,-4,-7,16]
    return {'scope': {'discovery_search': False, 'finite_controls': 8, 'core_phases': 6, 'insertion_positions': 7, 'norm2_pairs': 6}, 'symbolic': symbolic, 'controls': records, 'cyclic_controls': cyclic_records, 'cyclic_cases': 252, 'cubic_endpoint_values': cubic, 'pencil_evaluations': sum((sum((len(x) for x in r['pencil_values'].values())) for r in records)), 'passed': True}

if __name__=='__main__':
    try:
        result=main(); ((_J_OUTPUT / 'result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({k:result[k] for k in ('passed','cyclic_cases','pencil_evaluations')}))
    except Exception as exc:
        failure={'error':_record_text(repr(exc)),'traceback':_record_text(traceback.format_exc()),'elapsed':perf_counter()-START,'passed':False}
        ((_J_OUTPUT / 'failure.json')).write_text(json.dumps(failure,indent=2)+'\n',encoding='utf-8')
        raise
