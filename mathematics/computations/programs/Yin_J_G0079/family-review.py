"""Whole changed-family reviewer: quotient projection and independent dense GF arithmetic."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from math import comb
import argparse, importlib.util, json, time, platform, traceback
import sympy as sp
from sympy.polys import galoistools as gf
from sympy.polys.domains import ZZ
BASE=(_J_PROGRAM / 'family-review.py').parent
CAP=240
PRIMES=[2,3,5,7,11,13,17,19,23,29,31]
START=time.monotonic()
spec=importlib.util.spec_from_file_location("j79_quotient_reviewer",(_J_PROGRAM / 'review_independent.py'))
qr=importlib.util.module_from_spec(spec);spec.loader.exec_module(qr)
qr.START=START;qr.CAP=CAP

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
    if time.monotonic()-START>CAP:raise TimeoutError("Declared whole reviewer cap exceeded")
def check(actual,expected,path):
    qr.compare(actual,expected,path)
def trim(c):
    c=list(c)
    while len(c)>1 and not c[-1]:c.pop()
    return c or [0]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def divide(a,b):
    a=trim(a);b=trim(b);assert b[-1]==1
    q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        j=len(a)-len(b);v=a[-1];q[j]=v
        for h,w in enumerate(b):a[j+h]-=v*w
        a=trim(a)
    return trim(q),a
def phi(m):
    a=[-1]+[0]*(m-1)+[1]
    for j in range(1,m):
        if m%j==0:
            a,r=divide(a,phi(j));assert r==[0]
    return a
CYCLO={tuple(phi(m)):m for m in [2,8,12,18,30]}
def value(c,x):
    out=0
    for a in reversed(c):out=out*x+a
    return out
def rat(x):
    x=F(x);return [x.numerator,x.denominator]
def desc(a,p):
    a=trim([int(v)%p for v in a])
    return [] if a==[0] else list(reversed(a))
def asc(a):
    return list(reversed(list(map(int,a)))) or [0]
def prime_divisors(n):
    return [p for p in range(2,n+1) if n%p==0 and all(p%q for q in range(2,int(p**0.5)+1))]
def witness_poly(a,p,path):
    assert isinstance(a,list) and len(a)>0,path
    for j,v in enumerate(a):
        assert type(v) is int and 0<=v<p,(path,j,v)
    assert trim(a)==a,path
    check(a,asc(desc(a,p)),path+"/canonical")

def verify_attempts(c,attempts,path):
    assert isinstance(attempts,list) and 1<=len(attempts)<=len(PRIMES)
    winner=None
    for index,a in enumerate(attempts):
        gate();p=PRIMES[index];d=len(c)-1
        modulus=desc(c,p)
        xr=gf.gf_rem([1,0],modulus,p,ZZ)
        residues={d:gf.gf_pow_mod([1,0],p**d,modulus,p,ZZ)}
        expectedtests=[]
        assert len(a["proper_degree_tests"])==len(prime_divisors(d))
        for j,ell in enumerate(prime_divisors(d)):
            step=d//ell
            residue=gf.gf_pow_mod([1,0],p**step,modulus,p,ZZ)
            difference=gf.gf_sub(residue,xr,p,ZZ)
            gcd=gf.gf_gcd(modulus,difference,p,ZZ)
            test=a["proper_degree_tests"][j]
            assert set(test)=={"degree_prime_divisor","step","frobenius_residue","difference","gcd","bezout_f","bezout_difference"}
            expected={"degree_prime_divisor":ell,"step":step,"frobenius_residue":asc(residue),"difference":asc(difference),"gcd":asc(gcd)}
            check({k:test[k] for k in expected},expected,path+f"/prime{p}/test{j}")
            s,v=test["bezout_f"],test["bezout_difference"]
            witness_poly(s,p,path+"/bezout_f");witness_poly(v,p,path+"/bezout_difference")
            lhs=gf.gf_add(gf.gf_mul(desc(s,p),modulus,p,ZZ),gf.gf_mul(desc(v,p),difference,p,ZZ),p,ZZ)
            check(asc(lhs),asc(gcd),path+"/complete_bezout_identity")
            # Canonical extended-Euclidean degree range makes every coefficient meaningful.
            if difference:
                assert len(desc(s,p))<len(difference) or not desc(s,p)
                assert len(desc(v,p))<len(modulus) or not desc(v,p)
            else:
                check(s,[1],path+"/zero_difference_s");check(v,[0],path+"/zero_difference_v")
            expectedtests.append(expected)
        passed=residues[d]==xr and all(z["gcd"]==[1] for z in expectedtests)
        expected={"prime":p,"reduced_polynomial":asc(modulus),"degree":d,
                  "residue_at_degree":asc(residues[d]),"x_remainder":asc(xr),"passed":passed}
        assert set(a)==set(expected)|{"proper_degree_tests"}
        check({k:a[k] for k in expected},expected,path+f"/prime{p}")
        if passed:
            winner=p
            assert index==len(attempts)-1,"An attempt follows first success"
    assert winner is not None or len(attempts)==len(PRIMES)
    return winner

def trace_coeff(c):
    d=len(c)-1;assert d%2==0 and c==c[::-1]
    r=d//2
    q=[0]*(r+1)
    for k in range(r,-1,-1):
        q[k]=c[r+k]-sum(q[j]*comb(j,(j-k)//2) for j in range(k+2,r+1,2))
    actual=[0]*(d+1)
    for j,w in enumerate(q):
        for h in range(j+1):actual[r+j-2*h]+=w*comb(j,h)
    check(actual,c,"trace_full_laurent_identity")
    return q

def projection(c):
    d=len(c)-1;N=2*d
    r=qr.reconstruct("family",c,"declared")
    ac=[sum(c[i]*c[i+h] for i in range(d+1-h)) for h in range(d+1)]
    G=[[ac[abs(i-j)] for j in range(d)] for i in range(d)]
    theta=F(max(sum(abs(G[i][j]) for i in range(d) if i!=j) for j in range(d)),ac[0])
    k=F(r["kappa"])
    return {"d":d,"N":N,"G_rows":G,"q":int(r["q"]),
            "C_rows":[list(map(int,row)) for row in r["C_rows"]],
            "U_rows":[list(map(int,row)) for row in r["U_rows"]],
            "signed_diagonal_sums":[rat(x) for x in r["signed_diagonal_sums"]],
            "endpoint_diagonals":[rat(x) for x in r["endpoint_diagonals"]],
            "kappa":rat(k),"autocorrelations":ac,"B":ac[0],"theta":rat(theta),
            "gamma":rat(F(2*sum(map(abs,ac[1:])),ac[0])),"H4_passed":bool(k<=4),
            "identity_checks":r["identity_checks"]}

def main():
    global START
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=(_J_OUTPUT / 'family-review-result.json'))
    args=parser.parse_args();target=args.output.resolve()
    assert target.parent==_J_OUTPUT.resolve()
    report={'schema': 'J79-family-whole-review-v1', 'status': 'started', 'records': []}
    with target.open("x",encoding="utf8") as f:json.dump(report,f,indent=2)
    paths=[((_J_PROGRAM if n in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / n) for n in ["family-author.py","family-output.json","author.py","author-output.json"]]
    before={p:p.read_bytes() for p in paths}
    native=json.loads(before[(_J_OUTPUT / 'family-output.json')])
    try:
        assert set(native)=={'schema', 'n_domain', 'prime_domain', 'trace_quarter_grid', 'status', 'records', 'selected_factor_count', 'certified_actual_count', 'actual_counterexamples'}
        check(native["schema"],"J79-reciprocal-family-v1","schema")
        check(native["status"],"complete","status")
        check(native["n_domain"],list(range(4,33)),"domain")
        check(native["prime_domain"],PRIMES,"primes")
        check(native["trace_quarter_grid"],list(range(-8,9)),"grid")
        pass
        pass
        assert len(native["records"])==29
        selected_count=actual_count=0;violations=[];last=0
        for n,rec in zip(range(4,33),native["records"]):
            gate()
            p=[0]*(n+4)
            for j,v in [(n+3,1),(n+1,-1),(n,-1),(3,-1),(2,-1),(0,1)]:p[j]+=v
            expected={"n":n,"polynomial":p,"degree":n+3,"values_at_1_2":[-2,5*2**n-11],
                      "coefficient_square_sum":6,"factor_unit":1,"factor_product_verified":True,"complete":True}
            assert set(rec)==set(expected)|{'factors'}
            check({k:rec[k] for k in expected},expected,f"n{n}")
            pass
            pass
            product=[1];ordering=[];selected_here=[]
            for j,f in enumerate(rec["factors"]):
                c=f["coefficients"];m=f["multiplicity"]
                assert isinstance(c,list) and len(c)>1 and c[-1]==1 and c[0] in (-1,1)
                assert all(type(v) is int for v in c) and type(m) is int and m>=1
                ordering.append((len(c)-1,c))
                for _ in range(m):product=mul(product,c)
                ends=[value(c,1),value(c,2)];sel=c==c[::-1] and ends[0]*ends[1]<0
                expected={"coefficients":c,"multiplicity":m,"reciprocal":c==c[::-1],"values_at_1_2":ends,"selected":sel}
                check({k:f[k] for k in expected},expected,f"n{n}/factor{j}")
                if not sel:
                    assert tuple(c) in CYCLO,("Unexpected nonselected factor",c)
                    check(c,phi(CYCLO[tuple(c)]),f"n{n}/cyclotomic")
                    assert set(f)==set(expected)|{"status"}
                    check(f["status"],"not-selected","nonselectedstatus")
                    continue
                selected_count+=1
                cert=f["irreducibility"]
                prime=verify_attempts(c,cert["direct_attempts"],f"n{n}/direct")
                if prime is not None:
                    assert set(cert)=={"direct_attempts","method","prime"}
                    method="direct-modular"
                    check(cert["prime"],prime,"directprime")
                else:
                    q=trace_coeff(c)
                    check(cert["trace_polynomial"],q,"tracepoly")
                    check(cert["trace_identity_verified"],True,"traceidentity")
                    qprime=verify_attempts(q,cert["trace_attempts"],f"n{n}/trace")
                    grid=[value(q,F(a,4)) for a in range(-8,9)]
                    check(cert["quarter_grid_values"],[rat(v) for v in grid],"gridvalues")
                    bracket=next(([-8+i,-7+i] for i in range(16) if grid[i]*grid[i+1]<0),None)
                    check(cert["quarter_grid_bracket_numerators"],bracket,"bracket")
                    method="trace-modular-and-interior-sign" if qprime is not None and bracket is not None else "uncertified"
                    keys={"direct_attempts","method","trace_polynomial","trace_identity_verified","trace_attempts","quarter_grid_values","quarter_grid_bracket_numerators"}
                    if method!="uncertified":
                        keys.add("prime");check(cert["prime"],qprime,"traceprime")
                    assert set(cert)==keys
                check(cert["method"],method,"method")
                actual=method!="uncertified";actual_count+=actual
                status="actual-certified" if actual else "conditional-uncertified"
                check(f["status"],status,"actualstatus")
                proj=projection(c)
                check(f["projection"],proj,f"n{n}/full_projection")
                failed=actual and not proj["H4_passed"]
                check(f["actual_H4_counterexample"],failed,"actualcounter")
                assert set(f)==set(expected)|{"status","irreducibility","projection","actual_H4_counterexample"}
                if failed:violations.append({"n":n,"factor_index":j})
                selected_here.append({"factor_index":j,"degree":proj["d"],"status":status,"method":method,"kappa":proj["kappa"],"theta":proj["theta"],"all_native_projection_fields_match":True})
            check(product,p,f"n{n}/complete_original_factor_product")
            check(ordering,sorted(ordering),"factor_order")
            report["records"].append({"n":n,"selected":selected_here,"all_factor_and_certificate_fields_checked":True})
            print("complete",n,selected_here,flush=True)
        check(native["selected_factor_count"],selected_count,"selected_count")
        check(native["certified_actual_count"],actual_count,"actual_count")
        check(native["actual_counterexamples"],violations,"actualcounterexamples")
        gate()
        report.update({'status': 'complete', 'all_native_mathematical_fields_checked': True, 'selected_factor_count': selected_count, 'certified_actual_count': actual_count, 'actual_counterexamples': violations, 'scalar_comparisons': qr.leaves, 'method': 'quotient-row Fraction projection, dense GF powers/gcd and full Bezout identities, binomial trace inversion'})
    except Exception as error:
        report.update({'status': 'incomplete', 'error_type': type(error).__name__, 'error': _record_text(str(error)), 'traceback': _record_text(traceback.format_exc())})
        target.write_text(json.dumps(report,indent=2)+"\n",encoding="utf8")
        raise
    target.write_text(json.dumps(report,indent=2)+"\n",encoding="utf8")
    print(json.dumps({k:v for k,v in report.items() if k!="records"}),flush=True)
if __name__=="__main__":main()

