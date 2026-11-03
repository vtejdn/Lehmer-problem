"""Identical atom family; ONE pinned HiGHS IPM+crossover; exact primal proof."""
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm, isfinite
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import importlib.metadata
import json
import os
import time
import traceback
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np
import sympy as sp
import highspy

HERE=(_J_PROGRAM / 'highs_worker.py').parent
P=[1,1,0,-1,-1,-1,-1,-1,0,1,1]
BETA=[1,0,1,0,0,0,-1,-1,1,1,-1]
U=[-2,-1,-1,0,0,1,1,2,0,0]
RMINUS=[2*x+int(i==8) for i,x in enumerate(U)]
EXPECTED_NATIVE_WITNESS=[2,4,3,2,0,0,-3,-2,-4,0]
D,N,Q,CAP=10,11,36,180
ENTRY_CAP=10**6
OPTIONS={'solver':'ipm','run_crossover':'on','presolve':'on','parallel':'off',
         'threads':1,'random_seed':0,'time_limit':90.0,'ipm_iteration_limit':100,
         'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9,
         'ipm_optimality_tolerance':1e-10,'output_flag':False,'log_to_console':False}
START=time.monotonic()
REPORT={'status': 'started', 'coefficients': P, 'd': D, 'allowed_T': D, 'N': N, 'phase': 'B', 'solver_options': OPTIONS, 'atom_scope': 'IDENTICAL Phase A; no old output/code mutation'}

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
    if time.monotonic()-START>=CAP:raise TimeoutError('Phase B aggregate180-second cap')

def pair(x):
    x=F(x);return [x.numerator,x.denominator]

def safe_float(x):
    x=float(x);return x if isfinite(x) else str(x)

def save(name,payload):
    assert name in {'highs_progress.json','highs_lead.json','highs_result.json','highs_failure.json'}
    pass
    pending=_J_OUTPUT/(name+'.pending')
    pending.write_text(json.dumps(payload,indent=2,allow_nan=False)+'\n',encoding='utf8')
    pending.replace(((_J_PROGRAM if name in ('highs_main.py', 'highs_worker.py', 'main.py', 'readme.md', 'worker.py') else _J_OUTPUT) / name))

def primitive(r):
    z=list(r);g=gcd(*z);assert g>0
    z=[x//g for x in z]
    if next(x for x in z if x)<0:z=[-x for x in z]
    return tuple(z)

def companion(r):
    last=r[-1]
    return tuple([-last*P[0]]+[r[i-1]-last*P[i] for i in range(1,D)])

def qform(h,r):return sum(r[i]*h[i][j]*r[j] for i in range(D) for j in range(D))

def exact_rectangular(rows,rhs,k):
    """ALL original rows; unique solution only after rank and consistency proof."""
    m=[[F(x) for x in row]+[F(b)] for row,b in zip(rows,rhs)]
    rank=0;pivots=[]
    for j in range(k):
        at=next((i for i in range(rank,len(m)) if m[i][j]),None)
        assert at is not None,'Returned basic columns are exactly rank deficient'
        m[rank],m[at]=m[at],m[rank]
        v=m[rank][j];m[rank]=[x/v for x in m[rank]]
        for i in range(len(m)):
            if i!=rank and m[i][j]:
                v=m[i][j];m[i]=[x-v*y for x,y in zip(m[i],m[rank])]
        pivots.append(j);rank+=1
    assert rank==k and all(any(row[:k]) or row[k]==0 for row in m),'Inconsistent ORIGINAL equality system'
    x=[F(0)]*k
    for i,j in enumerate(pivots):x[j]=m[i][k]
    assert all(sum(F(a)*b for a,b in zip(row,x))==c for row,c in zip(rows,rhs))
    return x,{'rank':rank,'unknown_columns':k,'original_row_count':len(rows),'consistent':True}

def reduce_poly(coeff):
    c=list(coeff)
    if len(c)<D:c+=[0]*(D-len(c))
    for j in range(len(c)-1,D-1,-1):
        a=c[j]
        for i in range(D+1):c[j-D+i]-=a*P[i]
    return c[:D]

def signed_norm(r):
    columns=[reduce_poly([0]*j+list(r)) for j in range(D)]
    return int(sp.Matrix(D,D,lambda i,j:columns[j][i]).det(method='bareiss'))

def regenerate():
    old=json.loads(((_J_OUTPUT / 'progress.json')).read_text(encoding='utf8'))
    matrix=json.loads(((_J_OUTPUT / 'matrix.json')).read_text(encoding='utf8'))
    assert matrix['status']=='complete' and matrix['coefficients']==P and matrix['beta']==BETA
    h0=[[2 if i==j else -BETA[abs(i-j)] for j in range(N)] for i in range(N)]
    h=[row[:D] for row in h0[:D]]
    assert matrix['H0_rows']==h0 and matrix['H_rows']==h and matrix['G_divisor']==2
    assert matrix['congruence_certificate']['negative_integer_witness']==EXPECTED_NATIVE_WITNESS
    assert qform(h,RMINUS)==-2 and qform(h,EXPECTED_NATIVE_WITNESS)==-4
    assert old['coefficients']==P and old['status']=='atoms-ready'
    assert old['parameters']['derived_seed_primitive'] is True
    assert old['parameters']['scalar_l']==list(range(-12,13)) and old['parameters']['energy_cap'] is None
    assert old['parameters']['coefficient_denominator_divides']==Q
    seeds=[];seed_labels=[];seed_index={}
    def add_seed(r,label):
        if not any(r):return
        z=primitive(r)
        if z not in seed_index:
            seed_index[z]=len(seeds);seeds.append(z);seed_labels.append(label)
    for count,r in enumerate(product((-1,0,1),repeat=D)):
        if count%1024==0:cap()
        if any(r) and next(x for x in r if x)==1:add_seed(r,{'kind':'ternary'})
    assert len(seeds)==29524
    anchors=[primitive(RMINUS)]
    other=primitive(EXPECTED_NATIVE_WITNESS)
    if other not in anchors:anchors.append(other)
    assert [list(x) for x in anchors]==old['actual_anchors']
    for ai,anchor in enumerate(anchors):
        current=anchor
        for k in range(21):
            cap();add_seed(current,{'kind':'anchor-orbit','anchor':ai,'power':k})
            for i in range(D):
                for sign in (-1,1):
                    r=list(current);r[i]+=sign
                    add_seed(r,{'kind':'orbit-coordinate','anchor':ai,'power':k,'coordinate':i,'sign':sign})
            if k<20:
                nxt=companion(current)
                for sign in (-1,1):
                    add_seed([x+sign*y for x,y in zip(current,nxt)],
                        {'kind':'adjacent-orbit','anchor':ai,'power':k,'sign':sign})
                current=nxt
    assert len(seeds)==old['seed_count']==30486
    atoms=[];labels=[];indices={};generated=0
    def add_atom(vec,label):
        f=tuple(vec);assert any(f) and max(map(abs,f))<=ENTRY_CAP
        if next(x for x in f if x)<0:f=tuple(-x for x in f)
        if f not in indices:
            indices[f]=len(atoms);atoms.append(f);labels.append(label)
    for si,r in enumerate(seeds):
        if si%128==0:cap()
        rd=sum(r[i]*P[i] for i in range(D))
        for ell in range(-12,13):
            generated+=1;c=ell-4*rd
            add_atom([Q*r[i]+c*P[i] for i in range(D)]+[c],[si,ell])
    initial=[]
    for h in range(N):
        f=[0]*N;f[0]=Q
        if h:f[h]=Q
        add_atom(f,[-1,h]);initial.append(indices[tuple(f)])
    assert generated+N==old['generated_labels']==762161
    assert len(atoms)==old['distinct_atoms']==762150
    assert initial==old['true_initial_basis'] and [list(atoms[j]) for j in initial]==old['true_initial_numerators']
    aa=np.asarray(atoms,dtype=np.int64)
    assert int(np.max(np.abs(aa)))<=ENTRY_CAP
    energies=(aa*aa).sum(axis=1)
    lag=np.asarray([(aa[:,:N-k]*aa[:,k:]).sum(axis=1) for k in range(1,N)],dtype=np.int64)
    for lo in range(0,len(atoms),16384):
        cap();part=aa[lo:lo+16384]
        rem=part[:,:D]-part[:,D:D+1]*np.asarray(P[:D],dtype=np.int64)
        assert np.all(rem%Q==0) and np.all(np.any(rem!=0,axis=1))
    REPORT.update({'status':'identical-atoms-ready','seed_count':len(seeds),'generated_labels':generated+N,
        'distinct_atoms':len(atoms),'actual_anchors':[list(x) for x in anchors],
        'true_initial_basis':initial.copy(),'true_initial_numerators':[list(atoms[j]) for j in initial]})
    save('highs_progress.json',REPORT)
    return atoms,labels,seeds,seed_labels,energies,lag

def worker():
    solver=highspy.Highs()
    pass
    atoms,labels,seeds,seed_labels,energies,lag=regenerate()
    cap();count=len(atoms)
    full=np.vstack([np.ones(count),lag/(Q*Q)])
    values=full.T.ravel();mask=values!=0
    starts=np.concatenate(([0],np.cumsum(np.count_nonzero(full,axis=0),dtype=np.int64)))
    indices=np.tile(np.arange(N,dtype=np.int32),count)[mask]
    values=values[mask]
    assert starts[-1]==len(values)==len(indices) and starts[-1]<2**31
    lp=highspy.HighsLp();lp.num_col_=count;lp.num_row_=N
    lp.sense_=highspy.ObjSense.kMinimize
    lp.col_cost_=energies/(Q*Q)
    lp.col_lower_=np.zeros(count);lp.col_upper_=np.full(count,highspy.kHighsInf)
    rhs=np.array([1.]+[0.]*D)
    lp.row_lower_=rhs.copy();lp.row_upper_=rhs.copy()
    lp.a_matrix_.format_=highspy.MatrixFormat.kColwise
    lp.a_matrix_.num_col_=count;lp.a_matrix_.num_row_=N
    lp.a_matrix_.start_=starts.astype(np.int32)
    lp.a_matrix_.index_=indices;lp.a_matrix_.value_=values
    option_status={}
    for name,value in OPTIONS.items():
        status=solver.setOptionValue(name,value);option_status[name]=str(status)
        assert status==highspy.HighsStatus.kOk,'Declared solver option rejected: '+name
    passed=solver.passModel(lp)
    REPORT.update({'status':'model-passed','model_columns':count,'model_rows':N,
        'model_nonzeros':len(values),'option_status':option_status,'pass_model_status':str(passed)})
    save('highs_progress.json',REPORT)
    assert passed==highspy.HighsStatus.kOk
    del full,mask,starts,indices,values,lp
    cap();run_status=solver.run()
    # Capture returned state before ANY status acceptance or exact postcheck.
    solution=solver.getSolution();basis=solver.getBasis();info=solver.getInfo();model_status=solver.getModelStatus()
    col_values=list(solution.col_value)
    col_status=list(basis.col_status);row_status=list(basis.row_status)
    basic=[j for j,s in enumerate(col_status) if s==highspy.HighsBasisStatus.kBasic]
    default=int(highspy.HighsBasisStatus.kLower)
    compressed={'column_count':len(col_status),'default_column_status':default,
        'column_status_exceptions':[[j,int(s)] for j,s in enumerate(col_status) if int(s)!=default],
        'row_status':[int(s) for s in row_status],
        'basic_original_columns':basic,'valid':bool(basis.valid)}
    lead={'status': 'returned-uncertified-lead', 'coefficients': P, 'allowed_T': D, 'run_status': str(run_status), 'model_status': str(model_status), 'model_status_string': solver.modelStatusToString(model_status), 'objective': safe_float(info.objective_function_value), 'value_valid': bool(solution.value_valid), 'dual_valid': bool(solution.dual_valid), 'primal_solution_status': int(info.primal_solution_status), 'dual_solution_status': int(info.dual_solution_status), 'basis_validity': int(info.basis_validity), 'iterations': {name: int(getattr(info, name)) for name in ['ipm_iteration_count', 'crossover_iteration_count', 'simplex_iteration_count']}, 'nonzero_primal_lead': [[j, safe_float(x)] for j, x in enumerate(col_values) if x != 0.0], 'primal_column_count': len(col_values), 'row_value': [safe_float(x) for x in solution.row_value], 'row_dual': [safe_float(x) for x in solution.row_dual], 'basis': compressed, 'basic_column_numerators': [list(atoms[j]) for j in basic if 0 <= j < count], 'solver_options': OPTIONS, 'limits': 'Floating returned state ONLY; saved before exact original-system/packet proof.'}
    save('highs_lead.json',lead)
    REPORT.update({'status':'returned-lead-saved','lead_file':'highs_lead.json',
                   'model_status':str(model_status),'floating_objective':safe_float(info.objective_function_value),
                   'returned_basic_columns':basic})
    save('highs_progress.json',REPORT)
    print(json.dumps({'stage':'returned-lead-saved','model_status':lead['model_status_string'],
        'objective':lead['objective'],'basic_columns':len(basic),'basis_valid':basis.valid}),flush=True)
    assert run_status!=highspy.HighsStatus.kError
    assert solution.value_valid and basis.valid,'No returned valid primal basis for exact reconstruction'
    assert len(col_values)==count and len(col_status)==count and len(row_status)==N
    assert all(isfinite(float(x)) for x in col_values)
    assert 1<=len(basic)<=N
    assert len(basic)+sum(s==highspy.HighsBasisStatus.kBasic for s in row_status)==N
    cap();k=len(basic)
    system=[[Q*Q]*k]+[[int(lag[h,j]) for j in basic] for h in range(D)]
    weights,proof=exact_rectangular(system,[Q*Q]+[0]*D,k)
    REPORT.update({'status':'exact-system-solved','exact_original_system':system,
        'exact_system_rhs':[Q*Q]+[0]*D,'exact_basis_weights':[pair(w) for w in weights],
        'exact_system_verification':proof})
    save('highs_progress.json',REPORT)
    assert all(w>=0 for w in weights),'Negative exact reconstructed weight'
    assert sum(weights)==1
    support=[(j,w) for j,w in zip(basic,weights) if w]
    assert support and all(w>0 for j,w in support)
    final_lags=[sum(w*F(int(lag[h,j]),Q*Q) for j,w in support) for h in range(D)]
    assert final_lags==[0]*D
    energy=sum(w*F(int(energies[j]),Q*Q) for j,w in support)
    assert energy>0 and energy>=F(451609,508032),'Adopted C26 lower control'
    q=lcm(*(F(x,Q).denominator for j,w in support for x in atoms[j]))
    mw=lcm(*(w.denominator for j,w in support))
    if energy<1:
        assert q>=5,'Adopted C25 coefficient-denominator control'
        assert (mw*energy).denominator==1 and 1<=mw*energy<=mw-1,'Adopted C28 final ME control'
    REPORT.update({'status':'exact-weights-ready','energy':pair(energy),'actual_q':q,'actual_M':mw,
                   'all_lags':[pair(x) for x in final_lags]})
    save('highs_progress.json',REPORT)
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
        auto=[sum(f[i]*f[i+h] for i in range(N-h)) for h in range(1,N)]
        assert auto==[F(int(lag[h,j]),Q*Q) for h in range(D)]
        label=labels[j]
        origin=({'seed':list(seeds[label[0]]),'seed_provenance':seed_labels[label[0]],'scalar_l':label[1]}
                if label[0]>=0 else {'initial_basis_h':label[1]})
        records.append({'atom_index':j,'generator':origin,'coefficients':[pair(x) for x in f],
            'weight':pair(w),'integer_residue':r,'numerator_coefficients':num,'content':content,
            'signed_residue_norm':dn,'signed_numerator_resultant':resultant,
            'multiplicity':int(w*mw),'energy':pair(sum(x*x for x in f)),
            'autocorrelations':[pair(x) for x in auto]})
        REPORT['verified_packet_prefix']=records.copy();save('highs_progress.json',REPORT)
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
        'limits':'One original-input exact packet only; no solver optimum/infeasibility or uniform gap is adopted.'})
    REPORT.pop('verified_packet_prefix',None)
    save('highs_result.json',REPORT);(_J_OUTPUT / 'highs_progress.json').unlink(missing_ok=True)
    print(json.dumps({'outcome': REPORT['outcome'], 'support': len(records), 'energy': pair(energy), 'q': q, 'M': mw}), flush=True)

if __name__=='__main__':
    try:worker()
    except BaseException as error:
        REPORT.update({'status':'failed','error_type':type(error).__name__,'error':_record_text(str(error)),
                       'traceback':_record_text(traceback.format_exc())})
        save('highs_failure.json',REPORT)
        raise
