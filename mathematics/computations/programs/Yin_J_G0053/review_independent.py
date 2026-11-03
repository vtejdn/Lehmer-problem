"""Separately implemented exact checks of frozen J53 mathematical certificates.

No author module is imported by the independent checks.  Polynomial determinants
use subset dynamic programming over Z[t], not triangular Newton coefficients,
SymPy symbolic determinants, or pointwise determinant interpolation.  The bounded
annealer is additionally replayed with writes intercepted, explicitly separately.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
from fractions import Fraction
import contextlib
import io
import json
import runpy
import time
from unittest.mock import patch

BASE=(_J_PROGRAM / 'review_independent.py').parent
NATIVE=['search.py','search_result.json','verify.py','verification.json',
        'short_replacements.py','short_replacements.json','path_replacements.py',
        'path_replacements.json','changed_control.py','changed_control.json','readme.md']

def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def transpose(a): return list(map(list,zip(*a)))
def mm(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def gram(a,g): return mm(mm(transpose(a),g),a)
def determinant(a):
    a=[r[:] for r in a]; n=len(a); sign=1; prev=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
        v=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*v-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
        for i in range(k+1,n):a[i][k]=0
        prev=v
    return sign*a[-1][-1]

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def full_polynomial(v):
    # A row-to-column bijection accumulates its inversion sign as columns enter.
    n=len(v); dp={0:[1]}
    for row in range(n):
        nxt={}
        for mask,coeffs in dp.items():
            for col in range(n):
                if mask>>col&1:continue
                a,b=v[col][row],v[row][col]
                if not(a or b):continue
                sign=-1 if (mask>>(col+1)).bit_count()%2 else 1
                newmask=mask|1<<col
                target=nxt.setdefault(newmask,[0]*(row+2))
                for k,x in enumerate(coeffs):
                    target[k]+=sign*a*x
                    target[k+1]+=sign*b*x
        dp=nxt
    return dp[(1<<n)-1][::-1]

def upper(g): return [[int(i==j) if j<=i else g[i][j] for j in range(len(g))] for i in range(len(g))]
def energy(g):return sum(g[i][j]**2 for i in range(len(g)) for j in range(i+1,len(g)))
def abs_upper(v):return [[1 if i==j else -abs(v[i][j]) if i<j else 0 for j in range(len(v))] for i in range(len(v))]
def cover(v):
    n=len(v); w=eye(2*n)
    for i in range(n):
        for j in range(i+1,n):
            a=v[i][j]
            for sheet in (0,1): w[2*i+sheet][2*j+(sheet if a<=0 else 1-sheet)]=-abs(a)
    return w

def val(coefs,x):
    result=0
    for c in coefs:result=result*x+c
    return result

def trace(coefs):
    assert len(coefs)==7 and coefs==coefs[::-1] and coefs[0]==1
    return [1,coefs[1],coefs[2]-3,coefs[3]-2*coefs[1]]

def check_intervals(coeffs,intervals):
    prev=None
    assert len(intervals)==3
    for pair,mult in intervals:
        a,b=map(Fraction,pair)
        assert mult==1 and a<b and (prev is None or prev<a)
        assert val(coeffs,a)*val(coeffs,b)<0
        assert b-a<=Fraction(1,100000)
        prev=b

def mutate_basis(q,g0,move):
    kind,i,j=move; g=gram(q,g0); q=[r[:] for r in q]
    if kind=='swap':
        for row in q:row[i],row[j]=row[j],row[i]
    else:
        assert kind=='reflect'
        for row in q:row[i]-=g[i][j]*row[j]
    return q

def matrix_certificate(q,g0):
    assert abs(determinant(q))==1
    g=gram(q,g0)
    assert [g[i][i] for i in range(6)]==[2]*6
    assert determinant(g)==-1
    v=upper(g); vm=abs_upper(v); w=cover(v)
    p=full_polynomial(v); pm=full_polynomial(vm); pw=full_polynomial(w)
    assert pw==conv(p,pm)
    return g,v,vm,w,p,pm,pw

def main():
    started=time.perf_counter()
    before={name:(((_J_PROGRAM if name in ('changed_control.py', 'path_replacements.py', 'readme.md', 'review_independent.py', 'search.py', 'short_replacements.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes() for name in NATIVE}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0113.md')
    # Optional within-run author-prose observation, never a mathematical input
    # or historical fingerprint/size gate; promotion may retire this draft.
    draft_before=draft.read_bytes() if draft.exists() else None
    source=json.loads(before['search_result.json'])
    ver=json.loads(before['verification.json'])
    shorts=json.loads(before['short_replacements.json'])
    paths=json.loads(before['path_replacements.json'])
    changed=json.loads(before['changed_control.json'])
    g0=source['seed_gram']; ident=eye(6)
    c=[[g0[i][j]-2*ident[i][j] for j in range(6)] for i in range(6)]
    assert mm(c,c)==[[5*x for x in row] for row in ident]
    assert sum(c[i][i] for i in range(6))==0 and determinant(g0)==-1
    # Direct check of convention equivalence with source's q=5 Seidel graph.
    for i in range(5):
        for j in range(5):
            if i!=j:
                seidel=-1 if ((2*i-2*j)%5) in (1,4) else 1
                assert c[i+1][j+1]==seidel
    q=ident
    for move in source['selected_steps']:
        q=mutate_basis(q,g0,move)
        assert abs(determinant(q))==1
        assert all(gram(q,g0)[i][i]==2 for i in range(6))
    assert q==source['integral_basis']
    g,v,vm,w,p,pm,pw=matrix_certificate(q,g0)
    assert (g,v,p,pm,pw)==(source['gram'],source['unitriangular'],source['polynomial_descending'],source['absolute_polynomial_descending'],source['cover_polynomial_descending'])
    assert energy(g)==source['energy']==17
    assert max(abs(a) for row in v for a in row)==source['height']==2
    assert determinant(q)==source['basis_determinant']==ver['basis_determinant']==-1
    assert len(source['selected_steps'])==ver['replayed_basis_steps']==8
    assert ver['passed'] is True and ver['seed_square_identity'] is True
    assert ver['gram_determinant']==-1 and ver['full_cover_determinant_points']==13
    assert trace(p)==[1,-3,-2,7] and trace(pm)==[1,-37,-54,23]
    assert ver['trace_polynomial']=='u**3 - 3*u**2 - 2*u + 7'
    assert ver['absolute_trace_polynomial']=='u**3 - 37*u**2 - 54*u + 23'
    check_intervals(trace(p),ver['trace_root_intervals'])
    check_intervals(trace(pm),ver['absolute_trace_root_intervals'])
    # Exhaust all original integer cube vectors, using scalar quadratic sums.
    roots=[]
    for x in product((-1,0,1),repeat=6):
        norm=sum(x[i]*g0[i][j]*x[j] for i in range(6) for j in range(6))
        if norm==2:
            bits=[a%2 for a in x]; wt=sum(bits)+sum(bits)%2
            roots.append({'coordinates':list(x),'mod2_weight':wt})
    assert roots==ver['all_short_roots'] and len(roots)==ver['short_root_count']==114
    exceptional=[r for r in roots if r['mod2_weight']==6]
    assert exceptional==ver['exceptional_weight_six_short_roots']
    for x in product((0,1),repeat=6):
        norm=sum(x[i]*g0[i][j]*x[j] for i in range(6) for j in range(6))
        wt=sum(x)+sum(x)%2
        assert norm%2==0 and (norm//2)%2==(wt//2)%2
    assert ver['binary_quadratic_model_vectors']==64 and ver['short_root_cube_size']==729
    # All actual replacement bases checked by determinant, not the author's
    # coordinate/cofactor admission shortcut; full polynomial for each basis.
    short_records=[]; path_records=[]; desired_path_parity=0
    qpath=eye(6)
    for i in range(1,6):qpath[i-1][i]=-1
    assert qpath==paths['path_basis'] and determinant(qpath)==1
    assert all(gram(qpath,g0)[i][i]==2 for i in range(6))
    for root in roots:
        x=root['coordinates']
        for col in range(6):
            candidate=eye(6)
            for i in range(6):candidate[i][col]=x[i]
            if abs(determinant(candidate))!=1:continue
            gc=gram(candidate,g0); pol=full_polynomial(upper(gc))
            assert [a%2 for a in pol]==[1]*7
            short_records.append({'column':col,'root':x,'mod2_weight':root['mod2_weight'],
                                  'first_coefficients':pol[1:3],'energy':energy(gc)})
        for col in (2,3):
            candidate=[r[:] for r in qpath]
            for i in range(6):candidate[i][col]=x[i]
            if abs(determinant(candidate))!=1:continue
            # Qpath is upper bidiagonal, so the inverse coefficients are suffix sums.
            coefficients=[sum(x[j:]) for j in range(6)]
            assert mm(qpath,[[a] for a in coefficients])==[[a] for a in x]
            gc=gram(candidate,g0); pol=full_polynomial(upper(gc))
            assert [a%2 for a in pol] in ([1]*7,[1,0,1,1,1,0,1])
            desired_path_parity+=int([a%2 for a in pol]==[1,0,1,1,1,0,1])
            path_records.append({'column':col,'root':x,'coefficient_in_path_basis':coefficients,
                                 'first_coefficients':pol[1:3],'energy':energy(gc)})
    assert short_records==shorts['all_admissible_results']
    assert path_records==paths['all_admissible_results']
    assert desired_path_parity==paths['target_mod2_count']==64
    assert shorts['declared_pair_cap']==shorts['all_pairs_tested']==114*6==684
    assert paths['declared_pair_cap']==paths['pairs_tested']==114*2==228
    assert shorts['unimodular_replacements']==len(short_records)
    assert paths['admissible_replacements']==len(path_records)
    assert not any(r['first_coefficients']==[-2,1] for r in short_records+path_records)
    assert shorts['target_count']==paths['target_count']==0
    assert shorts['target_mod2_count']==0
    assert shorts['target_witnesses']==paths['target_witnesses']==[]
    assert shorts['passed'] is True and paths['passed'] is True
    g,v,vm,w,p,pm,pw=matrix_certificate(changed['basis'],g0)
    assert (g,v,vm,w,p,pm,pw)==tuple(changed[k] for k in ('gram','matrix','absolute_matrix','cover_matrix','polynomial','absolute_polynomial','cover_polynomial'))
    assert p==[1,-2,-1,3,-1,-2,1] and pm==[1,-38,-61,-69,-61,-38,1]
    assert determinant(changed['basis'])==changed['basis_determinant']==1
    assert changed['energy']==energy(g)==24 and changed['height']==max(abs(a) for row in v for a in row)==2 and changed['rank']==6
    assert changed['trace_polynomial']=='u**3 - 2*u**2 - 4*u + 7'
    # Recover power traces from independently computed full coefficients.
    s1=-p[1]; s2=-p[1]*s1-2*p[2]; s3=-p[1]*s2-p[2]*s1-3*p[3]
    assert changed['original_first_three_power_traces']==[s1,s2,s3]==[2,6,5]
    assert changed['absolute_trace_polynomial']=='u**3 - 38*u**2 - 64*u + 7'
    assert energy(w)==48
    assert changed['passed'] is True and changed['irreducible_original'] is True
    assert changed['full_cover_det_integer_points']==13
    check_intervals(trace(p),changed['trace_intervals'])
    check_intervals(trace(pm),changed['absolute_trace_intervals'])
    # Irreducibility is established without the author's factorization routine:
    # trace cubic has no rational root; its real embeddings in (-2,2) preclude
    # the discriminant u^2-4 being a square in its totally real cubic field.
    tr=trace(p)
    assert tr==[1,-2,-4,7]
    assert all(val(tr,a)!=0 for a in (-7,-1,1,7))
    intervals=changed['trace_intervals']
    assert all(-2<Fraction(intervals[i][0][0])<Fraction(intervals[i][0][1])<2 for i in (0,1))
    assert 2<Fraction(intervals[2][0][0])<Fraction(intervals[2][0][1])<Fraction(5,2)
    assert val(tr,Fraction(2))<0<val(tr,Fraction(5,2))
    # Independently certify companion's one exterior pair and exact cost intervals.
    atr=trace(pm)
    assert atr==[1,-38,-64,7]
    assert all(-2<Fraction(changed['absolute_trace_intervals'][i][0][0])<Fraction(changed['absolute_trace_intervals'][i][0][1])<2 for i in (0,1))
    assert 39<Fraction(changed['absolute_trace_intervals'][2][0][0])<Fraction(changed['absolute_trace_intervals'][2][0][1])<40
    # Additional same-input author annealer replay, with every write intercepted.
    # This verifies recorded proposal counts/selection chronology; it is NOT the
    # independent determinant/root/candidate enumeration above.
    intercepted={}
    def capture(path,data,*args,**kwargs):
        assert Path(path).name=='search_result.json'
        intercepted[Path(path).name]=json.loads(data)
        return len(data)
    with patch.object(Path,'write_text',capture), contextlib.redirect_stdout(io.StringIO()):
        runpy.run_path(str((_J_PROGRAM / 'search.py')),run_name='__main__')
    replay=intercepted['search_result.json']
    assert replay.keys() == source.keys()
    for key,value in source.items():
        assert replay[key]==value, key
        assert type(replay[key]) is type(value),key
    assert all((((_J_PROGRAM if name in ('changed_control.py', 'path_replacements.py', 'readme.md', 'review_independent.py', 'search.py', 'short_replacements.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes()==content for name,content in before.items())
    if draft_before is not None:
        assert draft.read_bytes()==draft_before
    result={'passed': True, 'method': 'integer Bareiss and polynomial subset determinants; independent full finite candidate enumeration', 'conference_square_and_attribution_permutation': True, 'binary_quadratic_vectors': 64, 'short_cube_vectors': 729, 'short_roots': len(roots), 'short_pairs': 684, 'short_admissible': len(short_records), 'path_pairs': 228, 'path_admissible': len(path_records), 'desired_path_parity_count': desired_path_parity, 'complete_rank12_polynomial_determinants': 2, 'selected_steps_replayed': 8, 'exact_cubic_interval_families': 4, 'changed_original_irreducibility_method': 'irreducible cubic and negative conjugate discriminant', 'bounded_author_annealer_replay_nonindependent': {'proposals': source['proposals_executed'], 'all_non_timing_fields_equal': True}}
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
