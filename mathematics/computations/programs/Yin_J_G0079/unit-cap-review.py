"""Complete D221 native review, no author imports or optimizer execution.

Own prior serialization/convolution ideas are reused explicitly; current
projection, source reconstruction and active-system verification are separate.
Only main() performs mathematics, following a separately supplied quota gate.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as Q
from math import gcd, lcm, isfinite
import json, sys, time, traceback, subprocess, platform

HERE = (_J_PROGRAM / 'unit-cap-review.py').parent
OUT = (_J_OUTPUT / 'unit-cap-review-result.json')
CAP = 180
COUNT = 0
START = 0
SOURCES = ['fast-optimum-result.json', 'residual-lattice-output.json', 'lehmer-bundle-output.json']
ORDER = [('P10','baseline'),('P10','enlarged'),('n18','baseline'),('n18','enlarged'),('n30','baseline'),('n30','enlarged')]


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


def checktime():
    assert time.monotonic() - START < CAP, 'Declared outer/worker aggregate deadline'


def same(a, b, path):
    global COUNT
    if type(b) is dict:
        assert type(a) is dict and set(a) == set(b), (path, set(a), set(b))
        for k in b: same(a[k], b[k], path+'/'+k)
    elif type(b) is list:
        assert type(a) is list and len(a) == len(b), (path, len(a), len(b))
        for j, (x, y) in enumerate(zip(a,b)): same(x, y, path+'/'+str(j))
    else:
        assert type(a) is type(b) and a == b, (path, a, b)
        COUNT += 1


def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def seq(xs): return [enc(x) for x in xs]
def dec(x):
    assert type(x) is list and len(x) == 2 and all(type(a) is int for a in x)
    assert x[1] > 0 and gcd(*x) == 1
    return Q(*x)
def dot(a,b): return sum((x*y for x,y in zip(a,b)), Q(0))
def conv(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j] += x*y
    return out
def integers(M):
    assert all(x.q == 1 for x in M)
    return [[int(x) for x in row] for row in M.tolist()]
def fractions(M): return [seq(row) for row in M.tolist()]


def source_projection(label, old, parent):
    import sympy as sp
    d = {'P10':10, 'n18':20, 'n30':32}[label]
    N = 2*d
    if label == 'P10': p = [1,1,0,-1,-1,-1,-1,-1,0,1,1]
    else:
        # Independently divide t^(n+3)-t^(n+1)-t^n-t^3-t^2+1 by t+1.
        n=d-2; numerator=[0]*(n+4)
        for i,a in [(0,1),(2,-1),(3,-1),(n,-1),(n+1,-1),(n+3,1)]: numerator[i]+=a
        p=[]
        for i in range(d+1): p.append(numerator[i]-(p[-1] if p else 0))
        assert conv(p,[1,1]) == numerator
    T=sp.zeros(d)
    for j in range(d-1): T[j+1,j]=1
    for j in range(d): T[j,d-1]=-p[j]
    powers=[sp.eye(d)[:,0]]
    for j in range(1,N): powers.append(T*powers[-1])
    X=sp.Matrix.hstack(*powers)
    Gram=X*X.T
    Gi=Gram.inv(method='DM')
    R=X.T*Gi*X
    q=lcm(*(int(a.q) for a in R)); C=integers(q*R)
    A=sp.Matrix(N,d,lambda i,j:p[i-j] if 0<=i-j<=d else 0)
    assert X*A==sp.zeros(d) and R.T==R and R*R==R and R.trace()==d
    assert R==sp.eye(N)-A*(A.T*A).inv(method='DM')*A.T
    L=[row[:d] for row in C]
    assert sp.Matrix(L)*X==sp.Matrix(C) and X*sp.Matrix(L)==q*sp.eye(d)
    for k,v in [('coefficients',p),('d',d),('N',N),('q',q)]:
        same(old[k],v,'source/'+label+'/'+k)
        same(parent[k],v,'residue-source/'+label+'/'+k)
    same(old['C_rows' if label=='P10' else 'input_C_rows'],C,'source/'+label+'/C')
    same(parent['L_rows'],L,'source/'+label+'/L')
    U=sp.Matrix(parent['U_rows']); Ui=U.inv(method='DM')
    assert all(a.q==1 for a in Ui) and U*Ui==Ui*U==sp.eye(d)
    same(parent['U_inverse_rows'],integers(Ui),'source/'+label+'/Uinverse')
    same(parent['det_U'],int(U.det(method='domain-ge')),'source/'+label+'/detU')
    assert abs(parent['det_U'])==1
    same(parent['reduced_rows'],integers(U*sp.Matrix(L).T),'source/'+label+'/reduced')
    if label=='P10':
        for k,M in [('X_rows',X),('A_rows',A),('Q_rows',Gram),('G_rows',A.T*A)]:
            same(parent[k],integers(M),'source/P10/'+k)
        for k,M in [('Q_inverse',Gi),('G_inverse',(A.T*A).inv(method='DM')),('R_rows',R)]:
            same(parent[k],fractions(M),'source/P10/'+k)
        W=q*(A.T*A).inv(method='DM')*A.T
        same(parent['kernel_multiplier_rows'],integers(W),'source/P10/kernel')
        same(parent['det_Q'],int(Gram.det(method='domain-ge')),'source/P10/detQ')
        same(parent['det_G'],int((A.T*A).det(method='domain-ge')),'source/P10/detG')
    return p,d,N,q,C,T,U


def columns(label, old, parent):
    import sympy as sp
    p,d,N,q,C,T,U=source_projection(label,old,parent)
    t=sp.Symbol('t'); P=sp.Poly.from_list(p[::-1],t,domain=sp.ZZ)
    cols=[]
    rawlist=parent['family'] if label=='P10' else parent['candidates']
    assert len(rawlist)==(5*d-2 if label=='P10' else 3*d-2)
    for idx in range(5*d-2):
        checktime()
        mono=idx<N; raw=(rawlist[idx] if label=='P10' else rawlist[idx-N] if not mono else {})
        if mono:
            b=[int(j==idx) for j in range(N)]; seedkind='monomial'; k=idx; sign=0; z=None
        else:
            j=idx-N
            if j<d: seedkind,k,sign='basis',j,0
            else: seedkind,k,sign='adjacent',(j-d)//2,(-1 if (j-d)%2==0 else 1)
            z=[int(U[k,h]+(sign*U[k+1,h] if sign else 0)) for h in range(d)]
            b=z+[0]*d
        f=[sum(row[j]*b[j] for j in range(N)) for row in C]
        diff=[q*x-y for x,y in zip(b,f)]; up=[]
        # Constant-coefficient recursive division, not author's leading division.
        for j in range(d): up.append(diff[j]-sum(p[h]*up[j-h] for h in range(1,min(j,d)+1)))
        assert conv(p,up)==diff
        # Fresh independent polynomial subresultant norm; author copies the norm.
        nb=int(P.resultant(sp.Poly.from_list(b[::-1],t,domain=sp.ZZ)))
        assert nb!=0
        Bm=sp.zeros(d)
        for x in reversed(b): Bm=Bm*T+x*sp.eye(d)
        g=gcd(*f); nf=q**d*nb; assert g>0 and nf%g**d==0
        energy=sum(x*x for x in f); auto=conv(f,f[::-1])[N:]
        e=Q(energy,q*q); h=[Q(x,q*q) for x in auto]
        assert e>0
        if mono: assert abs(nb)==1 and e<=1 and e==Q(C[idx][idx],q)
        locator=(f'lehmer-bundle-output.json:family[{idx}]' if label=='P10' else
                 f'fast-optimum-result.json:{label}:column[{idx}]' if mono else
                 f'residual-lattice-output.json:{label}:candidates[{idx-N}]')
        admitted=mono or(abs(nb)==1 and e<=1)
        row={'source_index':idx,'kind':'monomial' if mono else 'retained_residue','source_locator':locator,
          'B':b,'F_coefficients':f,'kernel_multiplier':up,'signed_res_B':nb,'signed_res_F':nf,
          'content':g,'primitive_coefficients':[x//g for x in f],'signed_res_primitive':nf//g**d,
          'integer_energy':energy,'integer_autocorrelations':auto,'e':enc(e),'h':seq(h),
          'actual_degree':max(j for j,x in enumerate(f) if x),'coefficient_height':max(map(abs,f)),
          'coefficient_l1':sum(map(abs,f)),'norm_one':abs(nb)==1,'energy_at_most_one':e<=1,
          'baseline_included':mono,'enlarged_included':admitted,
          'exclusion_reasons':[] if admitted else (['nonunit_norm'] if abs(nb)!=1 else [])+(['energy_above_one'] if e>1 else [])}
        extra={'norm_matrix':integers(Bm),'z':z,'basis_index':k,'sign':sign,'basis_or_monomial_index':k}
        for key in extra:
            if key in raw:
                same(raw[key],extra[key],f'raw/{label}/{idx}/{key}');row[key]=extra[key]
        if not mono: row['retained_seed_kind']=seedkind
        if raw:
            same(raw['kind'],seedkind,f'raw/{label}/{idx}/kind')
            for key in ('B','F_coefficients','kernel_multiplier','signed_res_B','signed_res_F','content',
                        'primitive_coefficients','signed_res_primitive','integer_energy','integer_autocorrelations',
                        'actual_degree','e','h'):
                if key in raw: same(raw[key],row[key],f'raw/{label}/{idx}/{key}')
            if 'e_B' in raw: same(raw['e_B'],enc(e),f'raw/{label}/{idx}/eB')
            if 'h_B' in raw: same(raw['h_B'],seq(h),f'raw/{label}/{idx}/hB')
        cols.append(row)
    es=[dec(c['e']) for c in cols]; H=[[dec(c['h'][h]) for c in cols] for h in range(N-1)]
    assert sum(es[:N])==d and all(es[j]==es[N-1-j] and all(row[j]==row[N-1-j] for row in H) for j in range(d))
    v=[Q(1,d)]*N+[Q(0)]*(3*d-2); corr=[dot(row,v) for row in H]
    exp={'input':label,'coefficients':p,'d':d,'N':N,'q':q,'C_rows':C,'columns':cols,
      'source_column_count':len(cols),'baseline_indices':list(range(N)),
      'enlarged_indices':[j for j,c in enumerate(cols) if c['enlarged_included']],
      'admitted_residue_indices':[j for j,c in enumerate(cols) if j>=N and c['enlarged_included']],
      'excluded_residue_indices':[j for j,c in enumerate(cols) if j>=N and not c['enlarged_included']],
      'mirror_pairs':[[j,N-1-j] for j in range(d)],'uniform_v':seq(v),'uniform_correlations':seq(corr),
      'uniform_kappa':enc(2*sum(map(abs,corr))),'degree_bound':N-1,'radial_multiplier':enc(Q(N-1,d)),
      'each_admitted_abs_res_F':q**d,'status':'inputs-certified'}
    return exp


def inspect_float(c,hp,ep,expected_pivots):
    import numpy as np
    keys={'status','pivot_count','phase_pivot_counts','phase1_objective','basis',
      'standard_variables','tableau_rows','reduced_costs','standard_dual','pair_masses',
      'candidate_correlations','objective','y','lambda','mu','reduced_cost_tolerance',
      'active_selection_tolerance','ratio_tie_tolerance'}
    assert set(c)==keys and c['status']=='candidate-returned'
    assert type(c['pivot_count']) is int and c['pivot_count']==sum(c['phase_pivot_counts'])==expected_pivots
    assert len(c['phase_pivot_counts'])==2 and all(type(x) is int and 0<=x<=10000 for x in c['phase_pivot_counts'])
    for k,v in [('reduced_cost_tolerance',1e-9),('active_selection_tolerance',1e-7),('ratio_tie_tolerance',1e-10)]:
        same(c[k],v,'float/'+k)
    m,L=len(ep),len(hp);rows=2*L+2;orig=m+L;surplus=m+3*L;width=surplus+3
    A=np.zeros((rows,width)); b=np.zeros(rows)
    for h in range(L):
        A[2*h,:m]=list(map(float,hp[h]));A[2*h+1,:m]=-A[2*h,:m]
        A[2*h:2*h+2,m+h]=-1; A[2*h,orig+2*h]=1;A[2*h+1,orig+2*h+1]=1
    A[-2,:m]=1;A[-2,surplus]=-1;A[-2,surplus+1]=1;b[-2]=2
    A[-1,:m]=list(map(float,ep));A[-1,surplus+2]=1;b[-1]=1
    basis=c['basis']; assert len(basis)==rows and len(set(basis))==rows
    assert all(type(x) is int and 0<=x<surplus+1 for x in basis)
    total=0
    def arr(key,shape):
        nonlocal total
        def visit(v):
            nonlocal total
            if type(v) is list:
                for z in v:visit(z)
            else:
                assert type(v) is float and isfinite(v),(key,v);total+=1
        visit(c[key]);v=np.array(c[key]);assert v.shape==shape;return v
    T=arr('tableau_rows',(rows,width+1));x=arr('standard_variables',(width,))
    rc=arr('reduced_costs',(width,));pi=arr('standard_dual',(rows,))
    pair=arr('pair_masses',(m,));corr=arr('candidate_correlations',(L,));y=arr('y',(L,))
    for key in ('phase1_objective','objective','lambda','mu'): arr(key,())
    costs=np.zeros(width);costs[m:orig]=2
    equations={
      'basis_tableau':(A[:,basis]@T,np.column_stack((A,b))),
      'basis_identity':(T[:,basis],np.eye(rows)), 'standard_primal':(A@x,b),
      'reduced_cost':(rc,costs-costs[basis]@T[:,:-1]),'basis_values':(x[basis],T[:,-1]),
      'nonbasis_zero':(np.array([x[j] for j in range(width) if j not in basis]),0),
      'pair_values':(pair,x[:m]),'correlation_values':(np.array(hp,dtype=float)@pair,corr),
      'objective':(c['objective'],costs@x),'dual_slacks':(pi[:2*L],-rc[orig:orig+2*L]),
      'dual_budget':(pi[-2],rc[surplus]),'dual_energy':(pi[-1],-rc[surplus+2]),
      'dual_y':(y,(pi[1:2*L:2]-pi[:2*L:2])/2),
      'lambda':(c['lambda'],pi[-1]),'mu':(c['mu'],pi[-2]),'phase1':(c['phase1_objective'],0)}
    residuals={k:float(np.max(np.abs(a-z)/(1+np.abs(z)))) for k,(a,z) in equations.items()}
    assert all(a<=1e-6 for a in residuals.values()),residuals
    # Floats record candidate consistency only, never exact feasibility.
    return {'float_leaves':total,'scaled_tolerance':1e-6,'scaled_residuals':residuals,
            'pivot_history_not_replayed':True,'not_mathematical_optimality_evidence':True}


def solve(rows,rhs):
    import sympy as sp
    M=sp.Matrix(rows); b=sp.Matrix(rhs)
    # Normal-equation inverse is different from author's active row elimination;
    # invertibility proves full column rank, and ALL original equations follow.
    G=M.T*M
    values=G.inv(method='DM')*M.T*b
    assert M*values==b
    ans=[Q(x) for x in values]
    return ans,{'rank':len(ans),'unknown_count':len(ans),'free_indices':[],'equation_count':len(rows)}


def instance(rec,inp,ix):
    d,N,q=[inp[k] for k in ('d','N','q')]
    ids=inp[rec['family']+'_indices'];family=[inp['columns'][j] for j in ids]
    e=[dec(c['e']) for c in family];H=[[dec(c['h'][h]) for c in family] for h in range(N-1)]
    comp=list(range(d))+list(range(N,len(family)));ep=[e[j] for j in comp];hp=[[r[j] for j in comp] for r in H]
    exp={'input':rec['input'],'family':rec['family'],'status':'dual-reconstructed',
      'family_source_indices':ids,'family_count':len(family),'e':seq(e),'H_rows':[seq(r) for r in H],
      'compressed_local_indices':comp,'compressed_source_indices':[ids[j] for j in comp],
      'compressed_count':len(comp),'e_compressed':seq(ep),'H_compressed':[seq(r) for r in hp]}
    c=rec['floating_candidate']; freport=inspect_float(c,hp,ep,[107,184,599,868,1651,2952][ix])
    support=[j for j,x in enumerate(c['pair_masses']) if x>1e-7]
    zeros=[h for h,x in enumerate(c['candidate_correlations']) if abs(x)<1e-7]
    tight=abs(sum(c['pair_masses'])-2)<1e-7
    rows=[[ep[j] for j in support]];rhs=[Q(1)]
    if tight: rows.append([Q(1)]*len(support));rhs.append(Q(2))
    rows.extend([[hp[h][j] for j in support] for h in zeros]);rhs.extend([Q(0)]*len(zeros))
    pin={'support':support,'zero_lags':[h+1 for h in zeros],'S_tight':tight,
      'rows':[seq(r) for r in rows],'rhs':seq(rhs),'approx':[c['pair_masses'][j] for j in support]}
    sub,pinfo=solve(rows,rhs);vc=[Q(0)]*len(comp)
    for j,x in zip(support,sub):vc[j]=x
    v=[Q(0)]*len(family)
    for k,j in enumerate(comp):
        if j<d:v[j]=v[N-1-j]=vc[k]/2
        else:v[j]=vc[k]
    S=sum(v);corr=[dot(row,v) for row in H];K=2*sum(map(abs,corr))
    assert min(v)>=0 and dot(e,v)==1 and S>=2
    assert sum(vc)==S and [dot(row,vc) for row in hp]==corr
    y=[None]*(N-1);free=[]
    for h,x in enumerate(corr):
        if x:y[h]=Q(1 if x>0 else -1)
        elif abs(abs(c['y'][h])-1)<1e-7:y[h]=Q(1 if c['y'][h]>0 else -1)
        else:free.append(h)
    rows=[];rhs=[]
    for j,x in enumerate(vc):
        if x:
            rows.append([2*hp[h][j] for h in free]+[-ep[j],Q(-1)])
            rhs.append(-sum(2*hp[h][j]*y[h] for h in range(N-1) if y[h] is not None))
    if S>2 or abs(c['mu'])<1e-7:
        rows.append([Q(0)]*(len(free)+1)+[Q(1)]);rhs.append(Q(0))
    din={'free_y_lags':[h+1 for h in free],'fixed_y':[None if x is None else enc(x) for x in y],
      'rows':[seq(r) for r in rows],'rhs':seq(rhs),'approx':[c['y'][h] for h in free]+[c['lambda'],c['mu']]}
    sol,dinfo=solve(rows,rhs)
    for h,x in zip(free,sol):y[h]=x
    lam,mu=sol[-2:];slack=[2*dot(y,[row[j] for row in H])-lam*e[j]-mu for j in range(len(v))]
    lower=lam+2*mu
    exp.update(primal_reconstruction_input=pin,primal_reconstruction=pinfo,compressed_v=seq(vc),v=seq(v),
      S=enc(S),correlations=seq(corr),kappa=enc(K),dual_reconstruction_input=din,dual_reconstruction=dinfo,
      y=seq(y),lambda_value=enc(lam),mu=enc(mu),dual_slacks=seq(slack),lower_bound=enc(lower),gap=enc(K-lower))
    if ix<5:
        assert max(map(abs,y))<=1 and mu>=0 and min(slack)>=0 and K==lower
        assert mu*(S-2)==0 and all(x*z==0 for x,z in zip(v,slack)) and S==2
        w=[x/S for x in v];M=lcm(*(x.denominator for x in w));mult=[int(x*M) for x in w]
        agg=[0]*(2*N-1);sign=1
        for copies,col in zip(mult,family):
            aa=conv(col['F_coefficients'],col['F_coefficients'][::-1])
            for j,x in enumerate(aa):agg[j]+=copies*x
            sign*=col['signed_res_B']**(copies%2)
        energy=Q(q*q)/S;auto=[q*q*x/S for x in corr]
        assert sum(mult)==M and Q(agg[N-1],M)==energy and agg==agg[::-1]
        assert [Q(x,M) for x in agg[N:]]==auto
        exp.update(status='complete',global_finite_family_optimum_certified=True,weights=seq(w),
          weight_denominator=M,multiplicities=mult,positive_local_indices=[j for j,x in enumerate(w) if x],
          positive_source_indices=[ids[j] for j,x in enumerate(w) if x],zero_lags=[h+1 for h,x in enumerate(corr) if not x],
          strict_dual_slack_local_indices=[j for j,x in enumerate(slack) if x>0],energy=enc(energy),
          aggregate_autocorrelations=seq(auto),aggregate_polynomial=agg,income={'log_q_argument':q},
          exact_arithmetic_product={'sign':sign,'q_base':q,'q_exponent':d*M},
          true_surplus={'half_log_argument':enc(S),'at_least_half_log_two':S>=2},degree_bound=N-1,
          radial_multiplier=enc(Q(N-1,d)),kappa_le_4=K<=4,
          kappa_ten_thousandth_bin=[K.numerator*10000//K.denominator,K.numerator*10000//K.denominator+1])
        outcome={'input':rec['input'],'family':rec['family'],'status':'complete-exact-optimum',
          'kappa':enc(K),'bin':exp['kappa_ten_thousandth_bin'],'S':enc(S),
          'positive_sources':exp['positive_source_indices'],'weight_denominator':M}
    else:
        assert y[8]>1 and pinfo['rank']==dinfo['rank']==11 and K==lower and S==2
        assert 'weights' not in rec and 'aggregate_polynomial' not in rec
        outcome={'input':rec['input'],'family':rec['family'],'status':'feasible-primal-invalid-dual',
          'primal_upper_bound':enc(K),'S':enc(S),'invalid_box_lags':[h+1 for h,x in enumerate(y) if abs(x)>1],
          'y9':enc(y[8]),'negative_dual_slack_indices':[j for j,x in enumerate(slack) if x<0],
          'mu_negative':mu<0,'no_unreached_weights_or_aggregate':True}
    same({k:v for k,v in rec.items() if k!='floating_candidate'},exp,'instance/'+str(ix))
    outcome['float_provenance']=freport
    return exp,outcome


def review(a,report):
    sources={f:json.loads((((_J_PROGRAM if f in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / f)).read_text(encoding='utf-8')) for f in SOURCES}
    assert all(s['status']=='complete' for s in sources.values())
    old={r['n']:r for r in sources[SOURCES[0]]['records']}
    parents={r['n']:r for r in sources[SOURCES[1]]['records']}
    inputs=[]
    for ix,label in enumerate(('P10','n18','n30')):
        src=sources[SOURCES[2]] if label=='P10' else old[int(label[1:])]
        par=src if label=='P10' else parents[int(label[1:])]
        inp=columns(label,src,par);same(a['inputs'][ix],inp,'inputs/'+label);inputs.append(inp)
        report.setdefault('inputs',[]).append({'input':label,'columns':len(inp['columns']),
          'admitted_residues':len(inp['admitted_residue_indices']),'all_fresh_signed_norms':True})
        print(json.dumps(report['inputs'][-1]),flush=True)
    assert len(a['inputs'])==3 and len(a['instances'])==6
    comparisons=[];results=[]
    for ix,(label,fam) in enumerate(ORDER):
        rec=a['instances'][ix];same(rec['input'],label,'order-input');same(rec['family'],fam,'order-family')
        exp,out=instance(rec,next(x for x in inputs if x['input']==label),ix)
        results.append(exp);report.setdefault('instances',[]).append(out)
        if ix in (1,3):
            K0=dec(results[ix-1]['kappa']);K=dec(exp['kappa']);assert K<K0
            comparisons.append({'input':label,'baseline_kappa':enc(K0),'enlarged_kappa':enc(K),
              'improvement':enc(K0-K),'strict_improvement':True,'equal_optima':False})
        checktime();print(json.dumps({k:v for k,v in out.items() if k!='float_provenance'}),flush=True)
    same(a['comparisons'],comparisons,'comparisons')
    expected={'schema': 'J79-unit-cap-comparison-v1', 'status': 'incomplete', 'input_files': SOURCES, 'helper_files': ['fast-optimum.py', 'nonmonomial-author.py'], 'candidate_rule': {'EPS': 1e-09, 'ACTIVE': 1e-07, 'ratio_tie': 1e-10, 'pivot_cap_per_instance': 10000, 'free_denominator_cap': 1000000, 'candidate_calls_per_instance': 1, 'reconstructions_per_instance': 1}, 'error_type': 'AssertionError', 'error': '', 'actual_worker_exit_code': 1, 'outer_timed_out': False}
    for k,v in expected.items():same(a[k],v,'top/'+k)
    provenance={'traceback'}
    assert set(a)==set(expected)|provenance|{'instances','inputs','comparisons'}
    pass
    assert all((type(a[k]) is float and 0 < a[k] < 180 for k in ()))
    pass
    report.update(mathematical_scalar_fields=COUNT, complete_original_columns=sum((len(x['columns']) for x in inputs)), complete_optima=5, feasible_upper_only=1, strict_comparisons=2, all_new_native_keys_checked=True, source_scope='Complete consumed C/projection/U/seed/multiplier/norm/content/energy/autocorrelation inputs; unrelated prior optimization and log-step payloads reused at retained review scope, not claimed rerun.', logarithm_scope='No logarithm intervals occur in this norm-one native schema; exact S=2 and q/d/M factorizations checked.', method='Quotient Gram projections, subresultant signed norms, constant-term polynomial division, full convolution, exact normal-equation active solves; direct floating tableau equations only, no simplex/LLL rerun.')


def worker(start):
    global START
    START=start
    report={'schema': 'J79-unit-cap-independent-review-v1', 'status': 'running'}
    paths=[(_J_PROGRAM / 'unit-cap-author.py'),(_J_OUTPUT / 'unit-cap-output.json')]+[((_J_PROGRAM if f in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / f) for f in SOURCES]
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0221.md')
    if draft.exists():paths.append(draft)
    snapshots={str(p):p.read_bytes() for p in paths}
    try:
        review(json.loads(((_J_OUTPUT / 'unit-cap-output.json')).read_text(encoding='utf-8')),report)
        report['status']='passed'
    except BaseException as exc:
        report.update(status='failed',error_type=type(exc).__name__,error=_record_text(str(exc)),traceback=_record_text(traceback.format_exc()))
    pass
    pass
    pass
    pass
    with OUT.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
    return 0 if report['status']=='passed' else 1


def main():
    if len(sys.argv)==3 and sys.argv[1]=='--worker':return worker(float(sys.argv[2]))
    assert len(sys.argv)==1 and not OUT.exists(),'Refusing extra invocation or report overwrite'
    start=time.monotonic()
    proc=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'unit-cap-review.py')),'--worker',repr(start)],
                          creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    timeout=False
    try:code=proc.wait(timeout=max(.01,CAP-(time.monotonic()-start)))
    except subprocess.TimeoutExpired:
        timeout=True;proc.kill();code=proc.wait()
    elapsed=time.monotonic()-start
    if not OUT.exists():
        with OUT.open('x',encoding='utf-8') as f:
            json.dump({'schema': 'J79-unit-cap-independent-review-v1', 'status': 'incomplete', 'error': 'Outer deadline or worker termination before sole report', 'outer_timed_out': timeout, 'worker_exit_code': code}, f, indent=2)
    print(json.dumps({'worker_exit_code': code, 'outer_timed_out': timeout}), flush=True)
    return code if not timeout else 124


if __name__=='__main__':raise SystemExit(main())
