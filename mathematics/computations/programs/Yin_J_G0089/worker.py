"""Changed integer residues, fixed scalar grid, exact primal validation."""
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import os
import time
import traceback
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np
import sympy as sp

HERE=(_J_PROGRAM / 'worker.py').parent
P=[1,1,0,-1,-1,-1,-1,-1,0,1,1]
BETA=[1,0,1,0,0,0,-1,-1,1,1,-1]
U=[-2,-1,-1,0,0,1,1,2,0,0]
V=U.copy();V[8]+=1
RMINUS=[2*x+int(i==8) for i,x in enumerate(U)]
D,N,Q=10,11,36
CAP,PIVOT_CAP,ENTRY_CAP=180,3000,10**6
EPS,PIVOT_EPS,RATIO_EPS,FEAS_EPS=1e-9,1e-10,1e-10,1e-6
START=time.monotonic()
REPORT={'status': 'started', 'coefficients': P, 'd': D, 'allowed_T': D, 'N': N, 'parameters': {'ternary_dimension': D, 'ternary_first_nonzero': 1, 'anchor_rule': 'required primitive r_minus, optional distinct exact-congruence negative witness', 'max_anchors': 2, 'companion_powers': [0, 20], 'orbit_coordinate_modifications': [-1, 1], 'adjacent_orbit_pairs': [-1, 1], 'derived_seed_primitive': True, 'scalar_l': list(range(-12, 13)), 'coefficient_denominator_divides': Q, 'energy_cap': None, 'max_seeds': 30486, 'max_generated_labels': 762161, 'numerator_entry_cap': ENTRY_CAP, 'pivot_cap': PIVOT_CAP, 'reduced_cost_tolerance': EPS, 'pivot_tolerance': PIVOT_EPS, 'ratio_tie_tolerance': RATIO_EPS, 'feasibility_guard': FEAS_EPS, 'early_candidate_objective': 1 - 1e-06}}

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
    if time.monotonic()-START>=CAP:raise TimeoutError('Declared aggregate180-second worker cap')

def pair(x):
    x=F(x);return [x.numerator,x.denominator]

def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))

def qform(h,r):return sum(r[i]*h[i][j]*r[j] for i in range(len(r)) for j in range(len(r)))

def primitive(r):
    a=[F(x) for x in r]
    den=lcm(*(x.denominator for x in a))
    z=[int(x*den) for x in a];g=gcd(*z)
    assert g>0
    z=[x//g for x in z]
    if next(x for x in z if x)<0:z=[-x for x in z]
    return tuple(z)

def save(name,payload):
    pass
    pending=_J_OUTPUT/(name+'.pending')
    pending.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf8')
    pending.replace(((_J_PROGRAM if name in ('highs_main.py', 'highs_worker.py', 'main.py', 'readme.md', 'worker.py') else _J_OUTPUT) / name))

def exact_solve(rows,rhs):
    m=[[F(x) for x in row]+[F(b)] for row,b in zip(rows,rhs)]
    for j in range(len(rhs)):
        at=next(i for i in range(j,len(m)) if m[i][j])
        m[j],m[at]=m[at],m[j]
        v=m[j][j];m[j]=[x/v for x in m[j]]
        for i in range(len(m)):
            if i!=j and m[i][j]:
                v=m[i][j];m[i]=[x-v*y for x,y in zip(m[i],m[j])]
    return [r[-1] for r in m]

def congruence(h):
    """Exact square completions; retain the full invertible congruence."""
    m=[[F(x) for x in row] for row in h]
    cols=[[F(int(i==j)) for i in range(D)] for j in range(D)]
    accepted=[];blocks=[];pos=neg=zero=0;negative=None
    while m:
        cap(); n=len(m)
        diag=next((i for i in range(n) if m[i][i]),None)
        if diag is not None:
            order=[diag]+[i for i in range(n) if i!=diag]
            m=[[m[i][j] for j in order] for i in order];cols=[cols[i] for i in order]
            a=m[0][0];b=m[0][1:];q0=cols[0]
            accepted.append(q0);blocks.append([[a]])
            if a>0:pos+=1
            else:
                neg+=1
                if negative is None:negative=primitive(q0)
            cols=[[x-(bj/a)*y for x,y in zip(qj,q0)] for qj,bj in zip(cols[1:],b)]
            m=[[m[i][j]-m[i][0]*m[0][j]/a for j in range(1,n)] for i in range(1,n)]
        else:
            off=next(((i,j) for i in range(n) for j in range(i+1,n) if m[i][j]),None)
            if off is None:
                accepted.extend(cols)
                for _ in range(n):blocks.append([[F(0)]])
                zero+=n;m=[];cols=[];continue
            i,j=off;order=[i,j]+[k for k in range(n) if k not in (i,j)]
            m=[[m[i][j] for j in order] for i in order];cols=[cols[i] for i in order]
            b=m[0][1];q0,q1=cols[:2]
            accepted.extend((q0,q1));blocks.append([[F(0),b],[b,F(0)]]);pos+=1;neg+=1
            if negative is None:
                sg=1 if b>0 else -1
                negative=primitive([x-sg*y for x,y in zip(q0,q1)])
            cols=[[x-(m[1][j]/b)*y-(m[0][j]/b)*z for x,y,z in zip(cols[j],q0,q1)]
                  for j in range(2,n)]
            m=[[m[i][j]-(m[i][0]*m[1][j]+m[i][1]*m[0][j])/b for j in range(2,n)]
               for i in range(2,n)]
    assert len(accepted)==D and pos+neg+zero==D
    s=[[accepted[j][i] for j in range(D)] for i in range(D)]
    block=[[F(0) for _ in range(D)] for _ in range(D)];at=0
    for b in blocks:
        for i,row in enumerate(b):
            for j,x in enumerate(row):block[at+i][at+j]=x
        at+=len(b)
    assert at==D
    for i in range(D):
        for j in range(D):
            assert sum(s[k][i]*h[k][l]*s[l][j] for k in range(D) for l in range(D))==block[i][j]
    det=sp.Matrix([[sp.Rational(x.numerator,x.denominator) for x in row] for row in s]).det()
    assert det!=0
    assert negative is not None and qform(h,negative)<0
    return {'inertia':{'positive':pos,'negative':neg,'zero':zero},
        'basis_rows':[[pair(x) for x in row] for row in s],
        'block_rows':[[pair(x) for x in row] for row in block],
        'basis_determinant':pair(F(int(det.p),int(det.q))),
        'negative_integer_witness':list(negative),
        'negative_H_value':qform(h,negative)}

def companion(r):
    last=r[-1]
    return tuple([-last*P[0]]+[r[i-1]-last*P[i] for i in range(1,D)])

def reduce_poly(coeff):
    c=list(coeff)
    if len(c)<D:c+=[0]*(D-len(c))
    for j in range(len(c)-1,D-1,-1):
        a=c[j]
        for k in range(D+1):c[j-D+k]-=a*P[k]
    return c[:D]

def signed_norm(r):
    cols=[reduce_poly([0]*j+list(r)) for j in range(D)]
    return int(sp.Matrix(D,D,lambda i,j:cols[j][i]).det(method='bareiss'))

def worker():
    assert P==P[::-1] and sum(x*x for x in P)==9
    h0=[[2 if i==j else -BETA[abs(i-j)] for j in range(N)] for i in range(N)]
    h=[row[:D] for row in h0[:D]]
    actual_auto=[sum(P[i]*P[i+k] for i in range(N-k)) for k in range(1,N)]
    assert actual_auto==[6,1,-2,-3,-4,-4,-2,1,2,1]
    assert sum(BETA[k]*actual_auto[k-1] for k in range(1,N))==9
    hp=[sum(row[j]*P[j] for j in range(N)) for row in h0]
    assert hp==[0]*N
    a=[[int(i==j) for j in range(D)]+[-P[i]] for i in range(D)]
    assert all(sum(a[k][i]*h[k][l]*a[l][j] for k in range(D) for l in range(D))==h0[i][j]
               for i in range(N) for j in range(N))
    hu=[sum(row[j]*U[j] for j in range(D)) for row in h]
    assert hu==[-int(i==8) for i in range(D)]
    assert qform(h,U)==qform(h,V)==0 and qform(h,RMINUS)==-2
    cert=congruence(h)
    ternary=[r for r in product((-1,0,1),repeat=D) if any(r) and next(x for x in r if x)==1]
    assert len(ternary)==29524
    ar=np.asarray(ternary,dtype=np.int64);hh=np.asarray(h,dtype=np.int64)
    assert int(np.max(np.abs(hh)))<=2
    vals=np.einsum('bi,ij,bj->b',ar,hh,ar,dtype=np.int64)
    minimum=int(vals.min());idx=int(np.flatnonzero(vals==minimum)[0]);tv=ternary[idx]
    assert qform(h,tv)==minimum
    matrix={'status':'complete','coefficients':P,'beta':BETA,'A_rows':a,'H0_rows':h0,
        'H_rows':h,'G_divisor':2,'autocorrelations':actual_auto,'H0_times_p':hp,
        'root_supplied_checks':{'u':U,'v':V,'r_minus':RMINUS,'H_times_u':hu,
            'u_G_value':[0,1],'v_G_value':[0,1],'r_minus_G_value':[-1,1]},
        'congruence_certificate':cert,'ternary_scan':{'canonical_count':len(ternary),
            'minimum_H_value':minimum,'first_minimum_vector':list(tv)},
        'limits':'Exact ORIGINAL residue form and bounded scan; no E10 identity or coefficient-energy/norm inference from an indefinite value.'}
    save('matrix.json',matrix)
    print(json.dumps({'stage':'matrix-complete','inertia':cert['inertia'],
        'negative_witness':cert['negative_integer_witness'],'ternary_min_H':minimum}),flush=True)
    seeds=[];seed_labels=[];seed_index={}
    def add_seed(r,label):
        if not any(r):return
        z=primitive(r)
        if z not in seed_index:
            seed_index[z]=len(seeds);seeds.append(z);seed_labels.append(label)
    for r in ternary:add_seed(r,{'kind':'ternary'})
    anchors=[primitive(RMINUS)]
    other=primitive(cert['negative_integer_witness'])
    if other not in anchors:anchors.append(other)
    assert len(anchors)<=2 and all(qform(h,r)<0 for r in anchors)
    for anchor_index,anchor in enumerate(anchors):
        current=anchor
        for k in range(21):
            cap();add_seed(current,{'kind':'anchor-orbit','anchor':anchor_index,'power':k})
            for i in range(D):
                for sign in (-1,1):
                    r=list(current);r[i]+=sign
                    add_seed(r,{'kind':'orbit-coordinate','anchor':anchor_index,'power':k,'coordinate':i,'sign':sign})
            if k<20:
                nxt=companion(current)
                for sign in (-1,1):
                    add_seed([x+sign*y for x,y in zip(current,nxt)],
                        {'kind':'adjacent-orbit','anchor':anchor_index,'power':k,'sign':sign})
                current=nxt
    assert len(seeds)<=30486 and primitive(U) in seed_index and primitive(V) in seed_index
    atoms=[];labels=[];atom_index={};generated=0
    def add_atom(vec,label):
        f=tuple(vec)
        assert any(f) and max(map(abs,f))<=ENTRY_CAP
        if next(x for x in f if x)<0:f=tuple(-x for x in f)
        if f not in atom_index:
            atom_index[f]=len(atoms);atoms.append(f);labels.append(label)
    for si,r in enumerate(seeds):
        if si%128==0:cap()
        rd=sum(r[j]*P[j] for j in range(D))
        for ell in range(-12,13):
            generated+=1;c=ell-4*rd
            f=[Q*r[j]+c*P[j] for j in range(D)]+[c]
            assert max(map(abs,f))<=ENTRY_CAP,'Declared numerator-entry guard'
            add_atom(f,[si,ell])
    basis=[]
    for hlag in range(N):
        f=[0]*N;f[0]=Q
        if hlag:f[hlag]=Q
        add_atom(f,[-1,hlag]);basis.append(atom_index[tuple(f)])
    assert generated+N<=762161 and len(set(basis))==N
    aa=np.asarray(atoms,dtype=np.int64)
    assert int(np.max(np.abs(aa)))<=ENTRY_CAP
    energies=(aa*aa).sum(axis=1)
    lag=np.asarray([(aa[:,:N-k]*aa[:,k:]).sum(axis=1) for k in range(1,N)],dtype=np.int64)
    for lo in range(0,len(atoms),16384):
        cap();part=aa[lo:lo+16384]
        rem=part[:,:D]-part[:,D:D+1]*np.asarray(P[:D],dtype=np.int64)
        assert np.all(rem%Q==0) and np.all(np.any(rem!=0,axis=1))
    for k,j in enumerate(basis):
        assert int(energies[j])==(1 if k==0 else 2)*Q*Q
        assert all(int(lag[t,j])==(Q*Q if t+1==k else 0) for t in range(D))
    REPORT.update({'status':'atoms-ready','actual_anchors':[list(x) for x in anchors],
        'seed_count':len(seeds),'generated_labels':generated+N,'distinct_atoms':len(atoms),
        'true_initial_basis':basis.copy(),'true_initial_numerators':[list(atoms[j]) for j in basis]})
    save('progress.json',REPORT)
    mat=np.vstack([np.ones(len(atoms)),lag/(Q*Q)])
    tab=mat.copy();tab[0]-=tab[1:].sum(axis=0)
    tab=np.column_stack([tab,np.array([1.]+[0.]*D)])
    costs=energies/(Q*Q);pivots=0;lowest=None
    while True:
        cap();assert float(tab[:,-1].min())>=-FEAS_EPS,'Floating basic-feasibility guard'
        objective=float(costs[basis]@tab[:,-1])
        if objective<=1-1e-6:
            why='first-strict-candidate';break
        rc=costs-costs[basis]@tab[:,:-1];rc[basis]=np.inf
        lowest=float(rc.min())
        if lowest>=-EPS:
            why='floating-termination';break
        assert pivots<PIVOT_CAP,'Declared3000-pivot cap'
        enter=int(np.flatnonzero(rc<=lowest+1e-12)[0])
        eligible=np.flatnonzero(tab[:,enter]>PIVOT_EPS)
        assert len(eligible),'Floating unbounded lead direction'
        ratios=np.maximum(tab[eligible,-1],0)/tab[eligible,enter]
        low=float(ratios.min())
        tied=[int(i) for i,r in zip(eligible,ratios) if r<=low+RATIO_EPS]
        leave=min(tied,key=lambda i:basis[i])
        tab[leave]/=tab[leave,enter]
        col=tab[:,enter].copy();col[leave]=0
        tab-=col[:,None]*tab[leave]
        basis[leave]=enter;pivots+=1
    REPORT.update({'status':'candidate-returned','floating_lead':{'status':'candidate-only',
        'termination':why,'pivot_count':pivots,'basis':basis.copy(),'weights':tab[:,-1].tolist(),
        'objective':objective,'last_min_nonbasic_reduced_cost':lowest},
        'returned_basis_numerators':[list(atoms[j]) for j in basis],
        'returned_basis_generator_labels':[labels[j] for j in basis]})
    save('progress.json',REPORT)
    system=[[Q*Q]*N]+[[int(lag[k,j]) for j in basis] for k in range(D)]
    weights=exact_solve(system,[Q*Q]+[0]*D)
    assert all(w>=0 for w in weights),'Negative exact reconstructed weight'
    assert sum(weights)==1
    support=[(j,w) for j,w in zip(basis,weights) if w]
    assert support and all(w>0 for j,w in support)
    final_lags=[sum(w*F(int(lag[k,j]),Q*Q) for j,w in support) for k in range(D)]
    assert final_lags==[0]*D
    energy=sum(w*F(int(energies[j]),Q*Q) for j,w in support)
    assert energy>0 and energy>=F(451609,508032),'Adopted C26 lower control'
    q=lcm(*(F(x,Q).denominator for j,w in support for x in atoms[j]))
    mw=lcm(*(w.denominator for j,w in support))
    if energy<1:
        assert q>=5,'Adopted C25 actual coefficient-denominator control'
        assert (energy*mw).denominator==1 and 1<=energy*mw<=mw-1,'Adopted C28 ME integer control'
    REPORT.update({'status':'exact-weights-ready','exact_original_system':system,
        'exact_basis_weights':[pair(w) for w in weights],'energy':pair(energy),
        'actual_q':q,'actual_M':mw,'all_lags':[pair(x) for x in final_lags]})
    save('progress.json',REPORT)
    t=sp.Symbol('t');pp=sum(P[i]*t**i for i in range(N));records=[]
    for j,w in support:
        cap();f=[F(x,Q) for x in atoms[j]];num=[int(q*x) for x in f]
        assert all(F(x,q)==y for x,y in zip(num,f))
        rr=[f[i]-f[-1]*P[i] for i in range(D)]
        assert all(x.denominator==1 for x in rr) and any(rr)
        r=[int(x) for x in rr];dn=signed_norm(r)
        resultant=int(sp.resultant(pp,sum(num[i]*t**i for i in range(N)),t))
        assert dn and resultant==q**D*dn,'Full signed norm/resultant disagreement'
        content=gcd(*num);assert content>0 and resultant%content**D==0
        auto=[sum(f[i]*f[i+k] for i in range(N-k)) for k in range(1,N)]
        assert auto==[F(int(lag[k,j]),Q*Q) for k in range(D)]
        label=labels[j]
        provenance=({'seed':list(seeds[label[0]]),'seed_provenance':seed_labels[label[0]],'scalar_l':label[1]}
                    if label[0]>=0 else {'initial_basis_h':label[1]})
        records.append({'atom_index':j,'generator':provenance,'coefficients':[pair(x) for x in f],
            'weight':pair(w),'integer_residue':r,'numerator_coefficients':num,'content':content,
            'signed_residue_norm':dn,'signed_numerator_resultant':resultant,
            'multiplicity':int(w*mw),'energy':pair(sum(x*x for x in f)),
            'autocorrelations':[pair(x) for x in auto]})
    positions=[i for rec in records for i,x in enumerate(rec['numerator_coefficients']) if x]
    width=max(positions)-min(positions)
    if energy<1:assert width==D,'Actual first-window width control'
    assert sum(rec['multiplicity'] for rec in records)==mw
    sign=(-1)**sum(rec['multiplicity'] for rec in records if rec['signed_residue_norm']<0)
    REPORT.update({'status':'complete','outcome':'exact-first-window-packet-below-one' if energy<1 else 'no-below-one-witness-returned',
        'packet':records,'actual_union_width':width,'integer_numerator_energy_S':pair(q*q*energy),
        'copied_full_signed_product':{'sign':sign,'scalar_factor':[q,D*mw],
            'absolute_residue_factors':[[abs(rec['signed_residue_norm']),rec['multiplicity']] for rec in records]},
        'ME':pair(mw*energy),'norm_income_formula':'log(q)+(1/10)*sum omega_b log(abs(D_b))',
        'normalized_surplus_formula':'(1/10)*sum omega_b log(abs(D_b))-(1/2)*log(E)',
        'actual_expense_formula':'(actual_union_width/10)*m(P)',
        'limits':'One original-input finite construction; no optimizer, whole-family finite optimum, uniform gap or near-one family.'})
    save('result.json',REPORT);((_J_OUTPUT / 'progress.json')).unlink(missing_ok=True)
    print(json.dumps({'outcome': REPORT['outcome'], 'seeds': len(seeds), 'atoms': len(atoms), 'pivots': pivots, 'support': len(records), 'energy': pair(energy), 'q': q, 'M': mw}), flush=True)

if __name__=='__main__':
    try:worker()
    except BaseException as error:
        REPORT.update({'status':'failed','error_type':type(error).__name__,'error':_record_text(str(error)),
                       'traceback':_record_text(traceback.format_exc())})
        save('failure.json',REPORT)
        raise
