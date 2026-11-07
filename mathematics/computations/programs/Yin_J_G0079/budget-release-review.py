"""Complete release review: no author import, optimizer or new candidate.

Explicit reuse of orbit's earlier exact/log/schema helpers only.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as Q
from math import gcd,lcm
import importlib.util,json,time,sys,traceback,subprocess,platform
import sympy as sp

HERE=(_J_PROGRAM / 'budget-release-review.py').parent
OUT=(_J_OUTPUT / 'budget-release-review-result.json')
CAP=30
spec=importlib.util.spec_from_file_location('own_release_exact',(_J_PROGRAM / 'nonmonomial-norm-review.py'))
own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
same,enc,seq,dec,dot,conv=own.same,own.enc,own.seq,own.dec,own.dot,own.conv

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


def review(a,old,parent):
    d,N=20,40
    sparse=[0]*22
    for j,x in [(0,1),(2,-1),(3,-1),(18,-1),(19,-1),(21,1)]:sparse[j]=x
    p=[1]
    for j in range(1,21):p.append(sparse[j]-p[-1])
    assert conv(p,[1,1])==sparse and p==p[::-1]
    powers=[own.remainder([0]*j+[1],p) for j in range(N)]
    X=sp.Matrix(powers).T; R=X.T*(X*X.T).inv(method='DM')*X
    q=lcm(*(int(x.q) for x in R));assert q==36887312
    C=[[int(q*x) for x in row] for row in R.tolist()]
    assert R*R==R and R.trace()==d and R.T==R
    U=sp.Matrix(parent['U_rows']);Ui=sp.Matrix(parent['U_inverse_rows'])
    assert U*Ui==Ui*U==sp.eye(d) and U.det(method='domain-ge')==-1
    family=[];t=sp.Symbol('t');P=sp.Poly.from_list(p[::-1],t,domain=sp.ZZ)
    for index in range(98):
        if index<N:
            b=[int(j==index) for j in range(N)];meta={'kind':'monomial','index':index}
            cert=None;ell=Q(0)
        else:
            j=index-N
            if j<d:kind,k,sgn='basis',j,0
            else:kind,k,sgn='adjacent',(j-d)//2,(-1 if (j-d)%2==0 else 1)
            z=[int(U[k,i]+(sgn*U[k+1,i] if sgn else 0)) for i in range(d)]
            b=z+[0]*d
            meta={'kind':'frozen_residue','index':j,'seed_kind':kind,'basis_index':k,'seed_sign':sgn,'z':z}
        norm=int(sp.resultant(P,sp.Poly.from_list(b[::-1],t,domain=sp.ZZ)));assert norm!=0
        if index>=N:cert=own.logcert(abs(norm),d);ell=dec(cert['ell_lower'])
        else:assert norm==1
        f=[sum(x*y for x,y in zip(row,b)) for row in C]
        diff=[q*x-y for x,y in zip(b,f)];up=[]
        for j in range(d):up.append(diff[j]-sum(p[k]*up[j-k] for k in range(1,j+1)))
        assert conv(p,up)==diff and own.remainder(f,p)==[q*x for x in own.remainder(b,p)]
        content=gcd(*f);nf=q**d*norm;assert content>0 and nf%content**d==0
        energy=sum(x*x for x in f);corr=own.correlations(f)
        family.append(dict(meta,B=b,F_coefficients=f,kernel_multiplier=up,signed_res_B=norm,signed_res_F=nf,
            content=content,ell=enc(ell),log_certificate=cert,D=abs(norm),integer_energy=energy,
            integer_autocorrelations=corr,e=enc(Q(energy,q*q)),h=seq([Q(x,q*q) for x in corr]),
            a=enc(1+2*ell),primitive_coefficients=[x//content for x in f],signed_res_primitive=nf//content**d,
            actual_degree=max(j for j,x in enumerate(f) if x)))
    same(old['family'],family,'old-full-family')
    e=[dec(c['e']) for c in family];ell=[dec(c['ell']) for c in family];aa=[1+2*x for x in ell]
    H=[[dec(c['h'][h]) for c in family] for h in range(39)]
    assert all(e[j]==e[N-1-j] and aa[j]==aa[N-1-j]==1 and all(row[j]==row[N-1-j] for row in H) for j in range(d))
    comp=list(range(d))+list(range(N,98));ep=[e[j]/aa[j] for j in comp]
    hp=[[row[j]/aa[j] for j in comp] for row in H]
    same(old['compressed_indices'],comp,'old-compression');same(old['r_prime'],seq(ep),'old-eprime')
    same(old['H_prime'],[seq(row) for row in hp],'old-Hprime')
    uc=list(map(dec,old['compressed_u']));assert len(uc)==78 and min(uc)>=0 and sum(uc)==2 and dot(ep,uc)==1
    corr=[dot(row,uc) for row in hp];K0=2*sum(map(abs,corr))
    same(old['correlations'],seq(corr),'old-correlations');same(old['kappa'],enc(K0),'old-K')
    y=list(map(dec,old['y']));lam=dec(old['lambda_value']);mu=dec(old['mu'])
    assert len(y)==39 and max(map(abs,y))<=1 and mu>0 and K0==lam+2*mu
    slacks=[2*dot(y,[row[j] for row in hp])-lam*ep[j]-mu for j in range(78)]
    assert min(slacks)>=0 and all(v*g==0 for v,g in zip(uc,slacks))
    assert all(not x or y[h]==(1 if x>0 else -1) for h,x in enumerate(corr))
    original_slacks=[2*dot(y,[row[j] for row in H])-lam*e[j]-mu*aa[j] for j in range(98)]
    assert min(original_slacks)>=0
    I=[j for j,x in enumerate(uc) if x];Z=[h for h,x in enumerate(corr) if not x]
    rows=[[ep[j] for j in I],[Q(1)]*len(I)]+[[hp[h][j] for j in I] for h in Z]
    rhs=[Q(0),Q(-1)]+[Q(0)]*len(Z)
    matrix=sp.Matrix(rows);assert matrix.rows==matrix.cols==13 and matrix.det(method='domain-ge')!=0
    sol=[Q(x) for x in matrix.inv(method='DM')*sp.Matrix(rhs)]
    assert all(dot(row,sol)==b for row,b in zip(rows,rhs))
    delta=[Q(0)]*78
    for j,x in zip(I,sol):delta[j]=x
    dc=[dot(row,delta) for row in hp]
    assert dot(ep,delta)==0 and sum(delta)==-1 and all(dc[h]==0 for h in Z) and 2*dot(y,dc)==-mu
    S0=sum(uc[k]/aa[j] for k,j in enumerate(comp));sigma=sum(delta[k]/aa[j] for k,j in enumerate(comp))
    same(old['S'],enc(S0),'old-S');assert 0<S0<2
    M=(2-S0)**2/4;D=1+abs(sigma)*(2/S0-1)
    bounds=[{'kind':'unit','index':-1,'value':[1,1]},{'kind':'surplus','index':-1,'value':enc(M/(2*D))}]
    bounds.extend({'kind':'mass','index':j,'value':enc(-uc[j]/x)} for j,x in enumerate(delta) if x<0)
    bounds.extend({'kind':'sign','index':h+1,'value':enc(-corr[h]/x)} for h,x in enumerate(dc) if corr[h]*x<0)
    tau=min(dec(b['value']) for b in bounds);assert tau>0
    ties=[j for j,b in enumerate(bounds) if dec(b['value'])==tau]
    unew=[u+tau*z for u,z in zip(uc,delta)];v=[Q(0)]*98;dv=[Q(0)]*98
    for k,j in enumerate(comp):
        if j<d:v[j]=v[N-1-j]=unew[k]/2;dv[j]=dv[N-1-j]=delta[k]/2
        else:v[j]=unew[k]/aa[j];dv[j]=delta[k]/aa[j]
    S=sum(v);LL=dot(ell,v);cn=[dot(row,v) for row in H];K=2*sum(map(abs,cn))
    assert min(v)>=0 and dot(e,v)==1 and S>0 and S==S0+tau*sigma
    assert S+2*LL==sum(unew)==2-tau and sum(dv)==sigma and [dot(row,dv) for row in H]==dc
    assert cn==[x+tau*z for x,z in zip(corr,dc)] and all(x*y>=0 for x,y in zip(corr,cn))
    assert all(cn[h]==0 for h in Z) and K==K0-mu*tau<K0
    tl=M-tau*D;margin=tl/(2*S);assert tl>=M/2>0
    w=[x/S for x in v];den=lcm(*(x.denominator for x in w));mult=[int(den*x) for x in w]
    aggregate=[0]*79
    for m,c in zip(mult,family):
        poly=conv(c['F_coefficients'],c['F_coefficients'][::-1])
        aggregate=[x+m*z for x,z in zip(aggregate,poly)]
    energy=Q(q*q)/S;ac=[q*q*x/S for x in cn]
    assert sum(mult)==den and aggregate==aggregate[::-1] and Q(aggregate[39],den)==energy
    assert [Q(aggregate[39+h],den) for h in range(1,N)]==ac
    exp={'schema': 'J79-exact-nonlinear-budget-release-v1', 'status': 'complete', 'input': 'inputs/joint-budget-n18.json', 'input_n': 18, 'd': d, 'N': N, 'q': q, 'coefficients': p, 'family': family, 'compressed_indices': comp, 'r_prime': seq(ep), 'H_prime': [seq(row) for row in hp], 'old_compressed_u': seq(uc), 'support': I, 'zero_lags': [h + 1 for h in Z], 'solve_matrix': [seq(row) for row in rows], 'solve_rhs': seq(rhs), 'solve_info': {'rank': 13, 'unknown_count': 13, 'free_indices': [], 'equation_count': 13}, 'delta_compressed_u': seq(delta), 'delta_original_v': seq(dv), 'delta_correlations': seq(dc), 'old_correlations': seq(corr), 'y': seq(y), 'lambda_value': enc(lam), 'mu': enc(mu), 'compressed_dual_slacks': seq(slacks), 'old_S': enc(S0), 'sigma': enc(sigma), 'M': enc(M), 'D': enc(D), 'bounds': bounds, 'tau': enc(tau), 'limiting_bound_indices': ties, 'new_compressed_u': seq(unew), 'v': seq(v), 'S': enc(S), 'L': enc(LL), 'budget': enc(S + 2 * LL), 'correlations': seq(cn), 'old_kappa': enc(K0), 'kappa': enc(K), 'strict_gap': enc(mu * tau), 'tangent_lower': enc(tl), 'actual_surplus_margin_lower': enc(margin), 'weights': seq(w), 'weight_denominator': den, 'multiplicities': mult, 'positive_indices': [j for j, x in enumerate(w) if x], 'energy': enc(energy), 'aggregate_autocorrelations': seq(ac), 'aggregate_polynomial': aggregate, 'income': {'log_q_argument': q, 'norm_terms': [{'D': c['D'], 'coefficient': enc(w[j] / d)} for j, c in enumerate(family)]}, 'exact_arithmetic_product': {'q_base': q, 'q_exponent': d * den, 'norm_factors': [{'D': c['D'], 'exponent': mult[j]} for j, c in enumerate(family)]}, 'degree_bound': 39, 'radial_multiplier': [39, 20], 'strict_actual_surplus': True, 'strictly_below_old': True, 'kappa_le_4': K <= 4, 'kappa_ten_thousandth_bin': [K.numerator * 10000 // K.denominator, K.numerator * 10000 // K.denominator + 1], 'actual_worker_exit_code': 0, 'outer_timed_out': False}
    history=[]
    assert set(a)==set(exp)|set(history)
    same({k:v for k,v in a.items() if k not in history},exp,'whole-native')
    pass
    assert all((type(a[k]) is float and 0 < a[k] < CAP for k in ()))
    assert [bounds[j]['kind'] for j in ties]==['mass'] and bounds[ties[0]]['index']==16
    assert v[16]==v[23]==0 and len(exp['positive_indices'])==17
    assert Q(37016,10000)<=K<Q(37017,10000) and mu*tau>=Q(3916,10**6) and margin>=Q(13395,10**6)
    return {'directions': 98, 'fresh_full_resultants': 98, 'full_lag_fields': 98 * 39, 'rank': 13, 'all_bound_records': len(bounds), 'limiting_bounds': [bounds[j] for j in ties], 'kappa': enc(K), 'strict_gap': enc(mu * tau), 'surplus_margin': enc(margin), 'positive_support': exp['positive_indices'], 'all_new_native_math_fields_checked': True}

def worker(output):
    start=time.perf_counter()
    before={'budget-release-output.json':(_J_OUTPUT/'budget-release-output.json').read_bytes()}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0217.md');db=draft.read_bytes() if draft.exists() else None
    out={'schema': 'J79-budget-release-independent-review-v1'}
    try:
        spec=importlib.util.spec_from_file_location('release_fixed_reviewer',_J_PROGRAM/'nonlinear-bound-review.py')
        fixed=importlib.util.module_from_spec(spec);spec.loader.exec_module(fixed)
        old=fixed.fixed_record()
        source=json.loads((_J_PROGRAM/'inputs/unit-cap-certificates.json').read_text())
        raw=next(r for r in source['inputs'] if r['name']=='P20')
        U=sp.Matrix([c['B'][:20] for c in raw['columns'][40:60]])
        Ui=U.inv(method='DM')
        assert all(x.q==1 for x in Ui)
        parent={'U_rows':U.tolist(),'U_inverse_rows':Ui.tolist()}
        out['complete_result']=review(json.loads(before['budget-release-output.json']),old,parent)
        out.update(status='passed',exact_scalar_comparisons=own.COUNT,author_replayed=False,optimizer_replayed=False)
    except BaseException as exc:out.update(status='failed',error_type=type(exc).__name__,error=_record_text(str(exc)),traceback=_record_text(traceback.format_exc()))
    pass
    pass
    pass;pass
    with output.open('x',encoding='utf8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='complete_result'}));return 0 if out['status']=='passed' else 1

if __name__=='__main__':
    if '--output' in sys.argv:OUT=Path(sys.argv[sys.argv.index('--output')+1]).resolve()
    if '--worker' in sys.argv:sys.exit(worker(OUT))
    if OUT.exists():raise SystemExit('Preserve first reviewer output')
    start=time.perf_counter();p=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'budget-release-review.py')),'--worker','--output',str(OUT)],creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    try:code=p.wait(timeout=CAP)
    except subprocess.TimeoutExpired:
        p.kill();p.wait();code=1
        if not OUT.exists():OUT.write_text(json.dumps({'status': 'incomplete', 'error': 'outer30secondcap'}) + '\n')
    sys.exit(code)
