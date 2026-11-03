"""Complete different-method verifier for D212/J82; no author imports."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from math import comb
import json, time, sys, argparse, subprocess, traceback, platform
HERE=(_J_PROGRAM / 'repeated-cell-review.py').parent
CAP=120
START=time.perf_counter()
COUNTS={"scalar_comparisons":0,"subsets":0,"companions":0,"pencil_values":0,"full_matrices":0,"pair_comparisons":0,"sturm_intervals":0}
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
    if time.perf_counter()-START>CAP:raise TimeoutError("aggregate120second cap")
def same(a,b):
    assert type(a) is type(b),(type(a),type(b))
    if isinstance(a,dict):
        assert set(a)==set(b),(set(a),set(b))
        for key in a:same(a[key],b[key])
    elif isinstance(a,list):
        assert len(a)==len(b),(len(a),len(b))
        for x,y in zip(a,b):same(x,y)
    else:
        assert a==b,(a,b)
        COUNTS["scalar_comparisons"]+=1
def rat(a):return {"numerator":a.numerator,"denominator":a.denominator}
def read(a):
    assert set(a)=={"numerator","denominator"}
    assert type(a["numerator"]) is int and type(a["denominator"]) is int
    r=F(a["numerator"],a["denominator"]);same(a,rat(r));return r
def matrixlist(A):return [[int(x) for x in row] for row in A.tolist()]
def coefficients(p):return [int(x) for x in reversed(p.all_coeffs())]
def original(k,sp):
    n=4*k+1
    names=[(i,c) for i in range(k) for c in ("a","b","c")]+[("z",i) for i in range(1,k+1)]+[(k,"a")]
    index={v:i for i,v in enumerate(names)}
    A=sp.eye(n)
    def edge(u,v,c):
        a,b=index[u],index[v];assert a<b;A[a,b]=c
    for i in range(k):
        edge((i,"a"),(i,"b"),-1);edge((i,"a"),(i,"c"),-1)
        edge((i,"b"),(i+1,"a"),-1);edge((i,"c"),(i+1,"a"),1)
    edge((0,"a"),(k,"a"),-1)
    path=[(0,"a")]+[("z",i) for i in range(1,k+1)]+[(k,"a")]
    for u,v in zip(path,path[1:]):edge(u,v,-1)
    return A
def polynomial(A,t,sp):
    n=A.rows;assert A==sp.eye(n)+sp.Matrix(n,n,lambda i,j:A[i,j] if j>i else 0)
    # Explicit triangular solve for the full monodromy, then Berkowitz charpoly.
    M=sp.zeros(n,n)
    for c in range(n):
        for i in range(n-1,-1,-1):
            M[i,c]=-A[c,i]-sum(A[i,j]*M[j,c] for j in range(i+1,n))
    p=sp.Poly(M.charpoly(t).as_expr(),t)
    assert p.degree()==n and p.LC()==1
    return p
def costs(A):
    n=A.rows
    return {"rank":n,"height":int(max(abs(x) for x in A)),"energy":int(sum(A[i,j]**2 for i in range(n) for j in range(i+1,n))),"full_squared_sum":int(sum(x*x for x in A))}
def lift(A,sp):
    n=A.rows;neg=sp.eye(n);pos=sp.zeros(n)
    for i in range(n):
        for j in range(i+1,n):
            if A[i,j]<0:neg[i,j]=A[i,j]
            else:pos[i,j]=-A[i,j]
    block=neg.row_join(pos).col_join(pos.row_join(neg))
    order=[v for i in range(n) for v in (i,n+i)]
    return block.extract(order,order)
def variations(values):
    signs=[1 if v>0 else -1 for v in values if v]
    return sum(a!=b for a,b in zip(signs,signs[1:]))
def sturm(p):
    seq=[p,p.diff()]
    while not seq[-1].is_zero:
        q=-seq[-2].rem(seq[-1])
        if q.is_zero:break
        seq.append(q)
    return seq
def varat(seq,x):return variations([p.eval(x) for p in seq])
def varinf(seq,positive):
    return variations([p.LC()*(1 if positive or p.degree()%2==0 else -1) for p in seq])
def rootcount(seq,a=None,b=None):
    return (varinf(seq,False) if a is None else varat(seq,a))-(varinf(seq,True) if b is None else varat(seq,b))
def floor_sqrt_rational(x):
    # Integer binary search, independent of author's isqrt.
    scale=1<<64;target=x*scale*scale
    low=0;high=1
    while high*high<=target:high*=2
    while high-low>1:
        mid=(high+low)//2
        if mid*mid<=target:low=mid
        else:high=mid
    return F(low,scale),F(high,scale)
def root_certificate(p,saved,t,sp):
    q,r=p.div(sp.Poly(t+1,t));assert r.is_zero
    c=coefficients(q);assert c==c[::-1]
    h=q.degree()//2
    # Descending Laurent elimination using binomial coefficients, not Chebyshev recurrence.
    laurent={i-h:F(v) for i,v in enumerate(c)}
    rc=[F(0)]*(h+1)
    for j in range(h,-1,-1):
        lead=laurent.get(j,F(0));rc[j]=lead
        for v in range(j+1):
            power=j-2*v
            laurent[power]=laurent.get(power,F(0))-lead*comb(j,v)
    assert all(v==0 for v in laurent.values())
    assert all(v.denominator==1 for v in rc)
    z=sp.Symbol("z");R=sp.Poly(sum(int(v)*z**i for i,v in enumerate(rc)),z,domain=sp.QQ)
    sfunit,sfs=R.sqf_list()
    sequences=[(f,m,sturm(f)) for f,m in sfs]
    realcount=sum(m*rootcount(seq) for f,m,seq in sequences)
    fresh=[];lo=hi=F(1);previous=None;covered=0
    for item in saved["real_intervals"]:
        a,b=read(item["lower"]),read(item["upper"]);assert a<=b and b-a<=F(1,1<<24)
        assert previous is None or previous<a
        previous=b;mult=0
        for f,m,seq in sequences:
            if a==b:count=int(f.eval(a)==0)
            else:
                assert f.eval(a)!=0 and f.eval(b)!=0
                count=rootcount(seq,a,b)
            assert count in (0,1)
            if count:assert mult==0;mult=m
        assert mult>0
        covered+=mult;COUNTS["sturm_intervals"]+=1
        current={"lower":rat(a),"upper":rat(b),"multiplicity":int(mult)}
        if -2<=a<=b<=2:current["type"]="unit-circle"
        elif a>2 or b<-2:
            x,y=(a,b) if a>2 else(-b,-a)
            l=(x+floor_sqrt_rational(x*x-4)[0])/2
            u=(y+floor_sqrt_rational(y*y-4)[1])/2
            lo*=l**mult;hi*=u**mult
            current.update(type="exterior-pair",outer_lower=rat(l),outer_upper=rat(u))
        else:current["type"]="boundary-undecided"
        same(item,current);fresh.append(current)
    assert covered==realcount
    certain=covered==R.degree() and all(v["type"]!="boundary-undecided" for v in fresh)
    out={"trace_coefficients":[int(v) for v in rc],"trace_degree":R.degree(),"real_root_count":int(realcount),"real_intervals":fresh,"all_trace_roots_real":covered==R.degree(),"complete_mahler_product_certified":certain}
    if certain:out["mahler_product_bounds"]={"lower":rat(lo),"upper":rat(hi)}
    same(saved,out);return out
def worker(output):
    import sympy as sp
    report={'schema': 'J82-repeated-cell-review-v1', 'status': 'running'}
    paths=[(_J_PROGRAM / 'repeated-cell-author.py'),(_J_OUTPUT / 'repeated-cell-output.json')]
    frozen={p:p.read_bytes() for p in paths}
    try:
        source=json.loads(frozen[paths[1]])
        assert set(source)=={'schema', 'status', 'inputs', 'counts', 'worker_returncode', 'outer_deadline_triggered'}
        same(source["schema"],"J82-repeated-cell-v1");same(source["status"],"complete");pass
        pass;same(source["worker_returncode"],0);same(source["outer_deadline_triggered"],False)
        pass
        for key in ():
            assert type(source[key]) is float and 0<source[key]<CAP
        assert len(source["inputs"])==4
        t=sp.Symbol("t")
        fullcert=[]
        for k,record in zip(range(3,7),source["inputs"]):
            gate();n=4*k+1;V=original(k,sp);op=polynomial(V,t,sp)
            assert set(record)=={"k","original_matrix","original_coefficients","subsets","companions","all_selected_complete","pairwise_measure_comparisons"}
            same(record["k"],k);same(record["original_matrix"],matrixlist(V));same(record["original_coefficients"],coefficients(op))
            assert len(record["subsets"])==1<<k and len(record["companions"])==k+1
            found={}
            for mask,item in enumerate(record["subsets"]):
                gate();selected=[i for i in range(k) if mask&(1<<i)]
                cols=[]
                for i in range(k):
                    basis=[sp.eye(n)[:,3*i+j] for j in range(3)]
                    cols.extend([basis[1],basis[2],sum(basis,sp.zeros(n,1))] if i in selected else basis)
                cols.extend(sp.eye(n)[:,j] for j in range(3*k,n))
                Q=sp.Matrix.hstack(*cols);assert Q.det(method="berkowitz")==1
                X=Q.T*V*Q;U=X.applyfunc(lambda v:-abs(v))
                for i in range(n):U[i,i]=1
                p=polynomial(U,t,sp);s=len(selected)
                if s in found:assert p==found[s]
                else:found[s]=p
                values=[int(p.eval(x)) for x in range(n+1)]
                expected={"mask":mask,"selected_cells":selected,"Q":matrixlist(Q),"det_Q":1,"X":matrixlist(X),"cost":costs(X),"companion_s":s,"pencil_nodes":list(range(n+1)),"pencil_values":values}
                same(item,expected);COUNTS["subsets"]+=1;COUNTS["pencil_values"]+=len(values)
                if s==k:
                    full=[]
                    for name,A in (("original",X),("absolute",U),("proper_cover",lift(X,sp))):
                        poly=polynomial(A,t,sp)
                        if name=="original":assert poly==op
                        if name=="proper_cover":assert poly==op*p
                        nodes=list(range(A.rows+1));vals=[int(poly.eval(x)) for x in nodes]
                        full.append({"name":name,"matrix":matrixlist(A),"cost":costs(A),"coefficients":coefficients(poly),"nodes":nodes,"values":vals})
                        COUNTS["full_matrices"]+=1;COUNTS["pencil_values"]+=len(vals)
                    same(record["all_selected_complete"],full)
            for s,pr in enumerate(record["companions"]):
                gate();assert set(pr)=={"s","coefficients","factorization","root_certificate"}
                same(pr["s"],s);p=found[s];same(pr["coefficients"],coefficients(p))
                fac=pr["factorization"];assert set(fac)=={"unit","factors"} and type(fac["unit"]) is int and fac["unit"]!=0
                prod=sp.Poly(fac["unit"],t)
                for factor in fac["factors"]:
                    assert set(factor)=={"coefficients","multiplicity"}
                    assert type(factor["multiplicity"]) is int and factor["multiplicity"]>0
                    assert all(type(v) is int for v in factor["coefficients"])
                    fp=sp.Poly(sum(v*t**j for j,v in enumerate(factor["coefficients"])),t)
                    assert fp.degree()>0 and fp.LC()>0 and fp.is_irreducible
                    prod*=fp**factor["multiplicity"]
                assert prod==p
                root_certificate(p,pr["root_certificate"],t,sp)
                if pr["root_certificate"]["complete_mahler_product_certified"]:fullcert.append([k,s])
                COUNTS["companions"]+=1
            comparisons=[]
            for a in range(k+1):
                for b in range(a+1,k+1):
                    ca=record["companions"][a]["root_certificate"];cb=record["companions"][b]["root_certificate"];status="undecided"
                    if ca["complete_mahler_product_certified"] and cb["complete_mahler_product_certified"]:
                        aa=ca["mahler_product_bounds"];bb=cb["mahler_product_bounds"]
                        if read(aa["upper"])<read(bb["lower"]):status="first-strictly-smaller"
                        elif read(bb["upper"])<read(aa["lower"]):status="second-strictly-smaller"
                    comparisons.append({"s_first":a,"s_second":b,"decision":status});COUNTS["pair_comparisons"]+=1
            same(record["pairwise_measure_comparisons"],comparisons)
        same(source["counts"],{"subsets":120,"companion_polynomials":22,"pencil_evaluations":3084,"full_selected_matrices":12})
        assert COUNTS["subsets"]==120 and COUNTS["companions"]==22 and COUNTS["pencil_values"]==3084 and COUNTS["full_matrices"]==12 and COUNTS["pair_comparisons"]==52
        assert fullcert==[[3,0],[3,1],[3,2],[3,3],[4,0],[4,3],[5,4],[6,5]]
        report.update(status="pass",complete_mahler_certificates=fullcert)
    except BaseException:report.update(status="failed",exception=_record_text(traceback.format_exc()))
    report.update(counts=COUNTS)
    output.write_text(json.dumps(report,indent=2),encoding="utf-8")
    return int(report["status"]!="pass")
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--worker",action="store_true");ap.add_argument("--output",type=Path,default=(_J_OUTPUT / 'repeated-cell-review-result.json'));args=ap.parse_args()
    path=args.output.resolve();assert path.parent == _J_OUTPUT
    if args.worker:return worker(path)
    if path.exists():raise FileExistsError(path)
    child=subprocess.Popen([sys.executable,__file__,"--worker","--output",str(path)])
    timeout=False
    try:code=child.wait(timeout=CAP)
    except subprocess.TimeoutExpired:child.kill();code=child.wait();timeout=True
    report=json.loads(path.read_text()) if path.exists() else {"status":"no-checkpoint","counts":{}}
    report.update(worker_returncode=code, outer_deadline_triggered=timeout)
    if timeout:report["status"]="timeout-partial"
    path.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report))
    return code or int(timeout)
if __name__=="__main__":raise SystemExit(main())

