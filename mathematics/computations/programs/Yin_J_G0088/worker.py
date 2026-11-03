"""Fixed rational atom search; float discovery is never a proof oracle."""
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time
import traceback
import numpy as np
import sympy as sp

HERE = (_J_PROGRAM / 'worker.py').parent
P = [1,1,0,-1,-1,-1,-1,-1,0,1,1]
D, N, Q0, CAP, PIVOT_CAP = 10, 11, 9, 180, 2000
EPS, PIVOT_EPS, RATIO_EPS = 1e-9, 1e-10, 1e-10
START = time.monotonic()
REPORT = {'status': 'started', 'coefficients': P, 'd': D, 'allowed_T': D, 'N': N, 'parameters': {'ternary_coordinates': D, 'first_nonzero': 1, 'k': [-2, -1, 0, 1, 2], 'coefficient_denominator_divides': Q0, 'atom_energy_cap': 4, 'pivot_cap': PIVOT_CAP, 'reduced_cost_tolerance': EPS, 'pivot_tolerance': PIVOT_EPS, 'ratio_tie_tolerance': RATIO_EPS}}

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


def cap():
    if time.monotonic()-START >= CAP:
        raise TimeoutError('Declared aggregate 180-second worker cap')

def pair(x):
    x = F(x)
    return [x.numerator, x.denominator]

def exact_solve(matrix, rhs):
    m = [[F(x) for x in row]+[F(b)] for row,b in zip(matrix,rhs)]
    n = len(rhs)
    for j in range(n):
        row = next(i for i in range(j,n) if m[i][j])
        m[j],m[row] = m[row],m[j]
        v=m[j][j]
        m[j] = [x/v for x in m[j]]
        for i in range(n):
            if i!=j and m[i][j]:
                v=m[i][j]
                m[i] = [x-v*y for x,y in zip(m[i],m[j])]
    return [row[-1] for row in m]

def reduce_poly(coeff):
    c = list(coeff)
    if len(c)<D: c += [0]*(D-len(c))
    for j in range(len(c)-1,D-1,-1):
        a=c[j]
        for k in range(D+1): c[j-D+k] -= a*P[k]
    return c[:D]

def norm_by_multiplication(residue):
    columns = [reduce_poly([0]*j+residue) for j in range(D)]
    return int(sp.Matrix(D,D,lambda i,j:columns[j][i]).det(method='bareiss'))

def save(name, payload):
    pass
    pending=_J_OUTPUT/(name+'.pending')
    pending.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf8')
    pending.replace(((_J_PROGRAM if name in ('exact-validation.py', 'main.py', 'readme.md', 'review-check.py', 'worker.py') else _J_OUTPUT) / name))

def worker():
    assert len(P)==N and P==list(reversed(P)) and P[0]==P[-1]==1
    assert sum(x*x for x in P)==Q0
    atoms=[]
    labels=[]
    seen={}
    generated=0
    def add(vec,label):
        v=tuple(vec)
        assert any(v)
        if next(x for x in v if x)<0: v=tuple(-x for x in v)
        if v not in seen:
            seen[v]=len(atoms); atoms.append(v); labels.append(label)
    for count,r in enumerate(product((-1,0,1),repeat=D)):
        if count%1024==0: cap()
        if not any(r) or next(x for x in r if x)!=1: continue
        dot=sum(a*b for a,b in zip(r,P))
        for k in (-2,-1,0,1,2):
            generated+=1
            a=k-dot
            v=[Q0*r[j]+a*P[j] for j in range(D)]+[a]
            if sum(x*x for x in v)<=4*Q0*Q0:
                add(v,{'r':list(r),'k':k})
    assert generated==147620
    basis=[]
    for h in range(N):
        v=[0]*N; v[0]=Q0
        if h: v[h]=Q0
        add(v,{'initial_basis_h':h})
        basis.append(seen[tuple(v)])
    assert len(set(basis))==N and generated+N<=147631
    cap()
    aa=np.asarray(atoms,dtype=np.int64)
    energies=(aa*aa).sum(axis=1)
    lags=np.asarray([(aa[:,:N-h]*aa[:,h:]).sum(axis=1) for h in range(1,N)])
    assert np.all(energies<=4*Q0*Q0)
    for h,j in enumerate(basis):
        assert energies[j]==(1 if h==0 else 2)*Q0*Q0
        assert all(int(lags[k,j])==(Q0*Q0 if k+1==h else 0) for k in range(D))
    REPORT.update({'status':'atoms-ready','generated_labels':generated+N,
                   'distinct_atoms':len(atoms),'initial_basis':basis})
    save('progress.json', REPORT)
    # Explicit inverse of [1 ... 1; 0 I] gives a feasible degenerate tableau.
    mat=np.vstack([np.ones(len(atoms)),lags/(Q0*Q0)])
    tab=mat.copy()
    tab[0]-=tab[1:].sum(axis=0)
    tab=np.column_stack([tab,np.array([1.]+[0.]*D)])
    costs=energies/(Q0*Q0)
    pivots=0
    while True:
        cap()
        rc=costs-costs[basis]@tab[:,:-1]
        rc[basis]=np.inf
        lowest=float(np.min(rc))
        if lowest>=-EPS: break
        assert pivots<PIVOT_CAP, 'Declared floating pivot cap'
        enter=int(np.flatnonzero(rc<=lowest+1e-12)[0])
        eligible=np.flatnonzero(tab[:,enter]>PIVOT_EPS)
        assert len(eligible), 'Floating unbounded candidate direction'
        ratios=np.maximum(tab[eligible,-1],0)/tab[eligible,enter]
        low=float(np.min(ratios))
        tied=[int(i) for i,r in zip(eligible,ratios) if r<=low+RATIO_EPS]
        leave=min(tied,key=lambda i:basis[i])
        tab[leave]/=tab[leave,enter]
        col=tab[:,enter].copy(); col[leave]=0
        tab-=col[:,None]*tab[leave]
        basis[leave]=enter; pivots+=1
    REPORT['floating_lead']={'pivot_count':pivots,'basis':basis,
        'basis_weights':tab[:,-1].tolist(),'objective':float(costs[basis]@tab[:,-1]),
        'minimum_nonbasic_reduced_cost':lowest,'status':'candidate-only'}
    REPORT['status']='candidate-returned'
    save('progress.json',REPORT)
    cap()
    exact_matrix=[[Q0*Q0]*N]+[[int(lags[h,j]) for j in basis] for h in range(D)]
    weights=exact_solve(exact_matrix,[Q0*Q0]+[0]*D)
    assert all(w>=0 for w in weights), 'Negative exact reconstructed weight'
    assert sum(weights)==1
    support=[(j,w) for j,w in zip(basis,weights) if w]
    assert support and all(w>0 for j,w in support)
    final_lags=[sum(w*F(int(lags[h,j]),Q0*Q0) for j,w in support) for h in range(D)]
    assert final_lags==[0]*D
    energy=sum(w*F(int(energies[j]),Q0*Q0) for j,w in support)
    assert energy>0
    q=lcm(*(F(a,Q0).denominator for j,w in support for a in atoms[j]))
    mw=lcm(*(w.denominator for j,w in support))
    t=sp.Symbol('t')
    pp=sp.Poly.from_list(list(reversed(P)),gens=t)
    records=[]
    for j,w in support:
        cap()
        f=[F(a,Q0) for a in atoms[j]]
        num=[int(a*q) for a in f]
        assert all(F(a,q)==b for a,b in zip(num,f))
        residue=[f[i]-f[-1]*P[i] for i in range(D)]
        assert all(a.denominator==1 for a in residue) and any(residue)
        r=[int(a) for a in residue]
        dn=norm_by_multiplication(r)
        res=int(sp.resultant(pp.as_expr(),sp.Poly.from_list(list(reversed(num)),gens=t).as_expr(),t))
        assert dn and res==q**D*dn
        content=gcd(*num)
        assert content>0 and res%content**D==0
        # Reconstruct every individual lag directly, outside the NumPy matrix.
        auto=[sum(f[i]*f[i+h] for i in range(N-h)) for h in range(1,N)]
        assert auto==[F(int(lags[h,j]),Q0*Q0) for h in range(D)]
        records.append({'atom_index':j,'generator_label':labels[j],
            'coefficients':[pair(a) for a in f],'weight':pair(w),
            'integer_residue':r,'numerator_coefficients':num,'content':content,
            'signed_residue_norm':dn,'signed_numerator_resultant':res,
            'multiplicity':int(w*mw),'energy':pair(sum(a*a for a in f)),
            'autocorrelations':[pair(a) for a in auto]})
    positions=[i for rec in records for i,x in enumerate(rec['numerator_coefficients']) if x]
    actual_width=max(positions)-min(positions)
    if energy<1: assert actual_width==D
    assert sum(rec['multiplicity'] for rec in records)==mw
    sign=(-1)**sum(rec['multiplicity'] for rec in records if rec['signed_residue_norm']<0)
    REPORT.update({'status':'complete','outcome':'exact-packet-below-one' if energy<1 else 'no-below-one-witness-returned',
        'A_rows':[[int(i==j) for j in range(D)]+[-P[i]] for i in range(D)],
        'packet':records,'energy':pair(energy),'all_lags':[pair(a) for a in final_lags],
        'actual_coefficient_denominator':q,'actual_weight_denominator':mw,
        'integer_numerator_energy_S':pair(q*q*energy),'actual_union_width':actual_width,
        'copied_full_signed_product':{'sign':sign,'scalar_factor':[q,D*mw],
            'absolute_residue_factors':[[abs(rec['signed_residue_norm']),rec['multiplicity']] for rec in records]},
        'norm_income_formula':'log(q)+(1/d)*sum_b omega_b log(abs(D_b))',
        'surplus_formula':'(1/d)*sum_b omega_b log(abs(D_b))-(1/2)*log(E)',
        'expense_formula':'(actual_width/d)*m(P)',
        'limits':'One exact finite packet only; floating discovery proves neither finite-family optimality nor full-capacity attainment, uniformity or gap.'})
    save('result.json',REPORT)
    ((_J_OUTPUT / 'progress.json')).unlink(missing_ok=True)
    print(json.dumps({'outcome': REPORT['outcome'], 'atoms': len(atoms), 'pivots': pivots, 'support': len(records), 'energy': pair(energy), 'q': q, 'M': mw}))

if __name__=='__main__':
    try:
        worker()
    except BaseException as error:
        REPORT.update({'status':'failed','error_type':type(error).__name__,'error':_record_text(str(error)),
                       'traceback':_record_text(traceback.format_exc())})
        save('failure.json',REPORT)
        raise
