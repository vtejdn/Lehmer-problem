"""Complete different-method review of frozen adaptive-weight native data."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from math import gcd,lcm
import argparse,json,time,platform,traceback
import review_independent as quotient

BASE=(_J_PROGRAM / 'weights-review.py').parent
CAP=120
START=time.monotonic()
quotient.START=START
quotient.CAP=CAP
LEAVES=0
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


def gate():
    if time.monotonic()-START>CAP:raise TimeoutError("Declared120second review cap")
def compare(a,b,path=""):
    global LEAVES
    assert type(a) is type(b),(path,type(a),type(b))
    if isinstance(a,dict):
        assert set(a)==set(b),(path,set(a)^set(b))
        for k in a:compare(a[k],b[k],path+"/"+k)
    elif isinstance(a,list):
        assert len(a)==len(b),(path,len(a),len(b))
        for i,(x,y) in enumerate(zip(a,b)):compare(x,y,path+"/"+str(i))
    else:
        assert a==b,(path,a,b)
        LEAVES+=1
def pair(x):
    x=F(x);return [x.numerator,x.denominator]
def vec(xs):return [pair(x) for x in xs]
def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))
def mv(A,v):return [dot(row,v) for row in A]
def bins(x):
    b=x.numerator*1000//x.denominator
    assert F(b,1000)<=x<F(b+1,1000)
    return [b,b+1]
def convolution(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def matrix_data(n,coeff):
    base=quotient.reconstruct("adaptive_"+str(n),coeff,"actual")
    C=[[int(x) for x in row] for row in base["C_rows"]]
    q=int(base["q"]);d=len(coeff)-1;N=2*d
    columns=list(map(list,zip(*C)))
    polys=[convolution(c,c[::-1]) for c in columns]
    H=[[F(polys[j][N-1+h],q*q) for j in range(N)] for h in range(1,N)]
    # The middle coefficient is a direct column energy, independent of diagonal extraction.
    r=[F(polys[j][N-1],q*q) for j in range(N)]
    assert r==[F(C[j][j],q) for j in range(N)]
    assert sum(r)==d and all(x>0 for x in r)
    assert all(row==row[::-1] for row in H) and r==r[::-1]
    v0=[F(1,d)]*N;a=mv(H,v0);k0=2*sum(map(abs,a))
    assert k0==F(base["kappa"])
    return C,q,d,N,columns,H,r,v0,a,k0
def reconstruct(n,coeff):
    C,q,d,N,columns,H,r,v0,a,k0=matrix_data(n,coeff)
    assert all(a)
    g=mv(list(map(list,zip(*H))),[2 if x>0 else -2 for x in a])
    # Orthogonalize {1,r}: center r, project onto this orthogonal pair.
    rmean=sum(r)/N
    rc=[x-rmean for x in r]
    gmean=sum(g)/N
    rc2=dot(rc,rc)
    cr=dot(g,rc)/rc2 if rc2 else F(0)
    c1=gmean-cr*rmean
    z=[g[j]-gmean-cr*rc[j] for j in range(N)]
    delta=[-x for x in z];norm2=dot(z,z)
    assert norm2>0 and sum(z)==dot(z,r)==0 and dot(g,delta)==-norm2
    Hd=mv(H,delta)
    positivity=[{"column":j,"ratio":pair(-v0[j]/(2*delta[j]))} for j in range(N) if delta[j]<0]
    sign_limits=[{"lag":h+1,"ratio":pair(abs(a[h]/Hd[h])/2)} for h in range(N-1) if Hd[h]]
    tau=min([F(1)]+[F(*x["ratio"]) for x in positivity+sign_limits])
    v1=[v0[j]+tau*delta[j] for j in range(N)]
    assert min(v1)>0 and sum(v1)==2 and dot(r,v1)==1
    w=[x/2 for x in v1];L=lcm(*(x.denominator for x in w))
    mult=[int(L*x) for x in w]
    # Reconstruct the complete aggregate polynomial from integer multiplicities.
    poly=[0]*(2*N-1)
    for j in range(N):
        conv=convolution(columns[j],columns[j][::-1])
        for h,value in enumerate(conv):poly[h]+=mult[j]*value
    energy=F(poly[N-1],L)
    aggregate=[F(poly[N-1+h],L) for h in range(1,N)]
    a1=[2*x/(q*q) for x in aggregate]
    assert a1==mv(H,v1) and all(x*y>0 for x,y in zip(a,a1))
    k1=2*sum(map(abs,aggregate))/energy
    decrement=k0-k1
    assert decrement==tau*norm2>0 and energy==F(q*q,2)
    return {"n":n,"coefficients":coeff,"d":d,"N":N,"q":q,"C_rows":C,
        "column_contents":[gcd(*c) for c in columns],"r":vec(r),"H_rows":[vec(row) for row in H],
        "v0":vec(v0),"uniform_correlations":vec(a),"uniform_kappa":pair(k0),
        "uniform_kappa_thousandth_bin":bins(k0),"zero_uniform_correlations":[],
        "status":"strict-improvement-certified","gradient":vec(g),
        "normalization_span_rank":2 if rc2 else 1,"span_coefficients_one_r":vec([c1,cr]),
        "span_gram_determinant":pair(N*rc2),"z":vec(z),"delta":vec(delta),
        "gradient_projection_squared_norm":pair(norm2),"H_delta":vec(Hd),
        "positivity_half_breakpoints":positivity,"sign_half_breakpoints":sign_limits,
        "tau":pair(tau),"v1":vec(v1),"new_correlations":vec(a1),"new_kappa":pair(k1),
        "decrement":pair(decrement),"new_kappa_thousandth_bin":bins(k1),
        "decrement_thousandth_bin":bins(decrement),"weights":vec(w),"weight_denominator":L,
        "multiplicities":mult,"positive_weight_count":sum(x>0 for x in mult),
        "energy":pair(energy),"aggregate_autocorrelations":vec(aggregate),
        "each_full_resultant_abs":q**d,"income_log_argument":q,"surplus_half_log_argument":[2,1],
        "degree_bound":N-1,"radial_multiplier":pair(F(N-1,d)),"new_kappa_le_4":k1<=4}
def provenance(data,direct):
    expected={'schema': 'J79-direct-weights-v1' if direct else 'J79-adaptive-weights-v1', 'domain_n': [18, 30], 'input': 'family-output.json', 'status': 'complete' if direct else 'incomplete', 'outer_deadline_triggered': not direct}
    if direct:expected.update(worker_exit_code=0,supervisor_exit_code=0)
    else:expected.update(worker_returncode=124,error_type="OuterDeadline",
        error="Worker killed at the declared aggregate 180-second deadline")
    special={'records'}
    assert set(data)==set(expected)|special
    for k,v in expected.items():compare(data[k],v,"provenance/"+k)
    pass
    pass;pass
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,default=(_J_OUTPUT / 'weights-review-result.json'))
    target=parser.parse_args().output.resolve();assert target.parent==_J_OUTPUT
    handle=target.open("x",encoding="utf8")
    out={'status': 'started', 'domain_n': [18, 30], 'records': []}
    try:
        names=["weights-author.py","weights-output.json","direct-author.py","direct-output.json","family-output.json"]
        before={name:(((_J_PROGRAM if name in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / name)).read_bytes() for name in names}
        partial=json.loads(before["weights-output.json"]);direct=json.loads(before["direct-output.json"])
        family=json.loads(before["family-output.json"])
        provenance(partial,False);provenance(direct,True)
        assert len(partial["records"])==1 and len(direct["records"])==2
        last=0
        for i,n in enumerate((18,30)):
            gate()
            parent=next(x for x in family["records"] if x["n"]==n)
            factors=[x for x in parent["factors"] if x["selected"]]
            assert len(factors)==1 and factors[0]["status"]=="actual-certified"
            expect=reconstruct(n,factors[0]["coefficients"])
            native=direct["records"][i]
            assert set(native)==set(expect)
            pass
            compare(native,expect,"direct/"+str(n))
            if n==18:
                p={"n":n,"coefficients":expect["coefficients"],"d":expect["d"],"N":expect["N"],
                   "q":expect["q"],"input_C_rows":expect["C_rows"],"r":expect["r"],"H_rows":expect["H_rows"],
                   "mirror_pairs":[[j,expect["N"]-1-j] for j in range(expect["d"])],
                   "uniform_kappa":expect["uniform_kappa"],"surplus_mass_threshold":2,"stage":"matrices-ready"}
                compare(partial["records"][0],p,"partial/18")
            out["records"].append({"n":n,"all_native_math_fields_match":True,
                "old_kappa":expect["uniform_kappa"],"new_kappa":expect["new_kappa"],
                "decrement":expect["decrement"],"positive_weights":expect["positive_weight_count"],
                "weight_denominator":expect["weight_denominator"]})
            print("complete native comparison",n,flush=True)
        gate()
        out.update(status='complete', mathematical_and_status_scalar_comparisons=LEAVES, simplex_matrix_stage_complete=True, simplex_n30_unstarted=True, no_simplex_optimality_certificate=True, methods=['quotient monomial remainder row-space projection', 'full integer polynomial convolution', 'centered orthogonal normalization projection', 'full multiplicity aggregate polynomial'])
    except Exception as error:
        out.update(status="incomplete",error_type=type(error).__name__,error=_record_text(str(error)),traceback=_record_text(traceback.format_exc()))
        raise
    finally:
        out.update()
        json.dump(out,handle,indent=2);handle.write("\n");handle.close()
        print(json.dumps({k:v for k,v in out.items() if k!="records"}),flush=True)
if __name__=="__main__":main()

