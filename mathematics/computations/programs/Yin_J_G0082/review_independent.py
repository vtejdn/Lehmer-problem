"""Full J82 review: literal graphs, Bareiss pencils, matching sums and DAG paths."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from math import comb,isfinite
import argparse,json,time,platform,traceback
BASE=(_J_PROGRAM / 'review_independent.py').parent
START=time.perf_counter();CAP=120;LEAVES=0
COUNTS={"matrices":0,"pencil_determinants":0,"factor_products":0,"continuants":0,"mixed_trace_entries":0}
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
    if time.perf_counter()-START>=CAP:raise TimeoutError("Declared120second review cap")
def cmp(a,b,p=""):
    global LEAVES
    assert type(a) is type(b),(p,type(a),type(b))
    if isinstance(a,dict):
        assert set(a)==set(b),(p,set(a)^set(b))
        for k in a:cmp(a[k],b[k],p+"/"+k)
    elif isinstance(a,list):
        assert len(a)==len(b),(p,len(a),len(b))
        for i,(x,y) in enumerate(zip(a,b)):cmp(x,y,p+"/"+str(i))
    else:assert a==b,(p,a,b);LEAVES+=1
def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p
def add(*ps):
    r=[0]*max(map(len,ps))
    for p in ps:
        for j,c in enumerate(p):r[j]+=c
    return trim(r)
def scale(p,c):return trim([c*x for x in p])
def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    return trim(r)
def powp(p,n):
    out=[1]
    for _ in range(n):out=mul(out,p)
    return out
def shift(p,n):return [0]*n+p
def ev(p,x):
    y=0
    for a in p[::-1]:y=y*x+a
    return y
def divide(a,b):
    a=list(a);r=[0]*(len(a)-len(b)+1)
    for j in range(len(r)-1,-1,-1):
        assert a[j+len(b)-1]%b[-1]==0
        s=a[j+len(b)-1]//b[-1];r[j]=s
        for h,x in enumerate(b):a[j+h]-=s*x
    assert not any(a)
    return trim(r)
def determinant(matrix):
    gate()
    a=[list(row) for row in matrix];n=len(a);previous=1;sign=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
        value=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=value*a[i][j]-a[i][k]*a[k][j]
                assert v%previous==0
                a[i][j]=v//previous
            a[i][k]=0
        previous=value
    return sign*a[-1][-1] if n else 1
def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def graph(k):
    labels=[]
    for j in range(k):labels += [("a",j),("b",j),("c",j)]
    labels += [("z",j) for j in range(1,k+1)]+[("a",k)]
    ix={x:i for i,x in enumerate(labels)};V=identity(len(labels))
    def edge(M,i,j,v=-1):M[i][j]=v;assert i<j
    for j in range(k):
        for x,y,v in [(("a",j),("b",j),-1),(("a",j),("c",j),-1),
                      (("b",j),("a",j+1),-1),(("c",j),("a",j+1),1)]:
            edge(V,ix[x],ix[y],v)
    edge(V,ix["a",0],ix["a",k])
    path=[("a",0)]+[("z",j) for j in range(1,k+1)]+[("a",k)]
    for x,y in zip(path,path[1:]):edge(V,ix[x],ix[y])
    labels2=["u"]+["z"+str(j) for j in range(1,k+1)]+["v"]+["leaf"+str(j) for j in range(4)]
    labels2+=["pair"+str(j)+s for j in range(k-1) for s in ("a","b")]
    labels2+=["neutral"+str(j) for j in range(k-3)]
    ix2={x:i for i,x in enumerate(labels2)};Z=identity(len(labels2))
    path2=["u"]+["z"+str(j) for j in range(1,k+1)]+["v"]
    for x,y in zip(path2,path2[1:]):edge(Z,ix2[x],ix2[y])
    edge(Z,ix2["u"],ix2["v"])
    for j in range(4):edge(Z,ix2["u" if j<2 else "v"],ix2["leaf"+str(j)])
    for j in range(k-1):edge(Z,ix2["pair"+str(j)+"a"],ix2["pair"+str(j)+"b"],-2)
    assert len(Z)==len(V)==4*k+1
    return V,Z
def absolute(V):return [[1 if i==j else -abs(x) for j,x in enumerate(row)] for i,row in enumerate(V)]
def lift(V):
    W=identity(2*len(V))
    for i,row in enumerate(V):
        for j in range(i+1,len(V)):
            x=row[j]
            for s in (0,1):W[2*i+s][2*j+(s if x<=0 else 1-s)]=-abs(x)
    return W
def paths(V):
    n=len(V);result=[0]*(n-1)
    adj=[[j for j in range(i+1,n) if V[i][j]] for i in range(n)]
    for initial in range(n):
        todo=[(initial,0)]
        while todo:
            at,length=todo.pop()
            if length and V[initial][at]:result[length-1]+=1
            todo += [(j,length+1) for j in adj[at]]
    return result
def matching(j):
    p=[0]
    for h in range(j//2+1):
        p=add(p,shift(scale(powp([1,-2,1],j-2*h),comb(j-h,h)*(-4)**h),2*h))
    return p
def record(rec,V,label):
    n=len(V);poly=rec["coefficients_ascending"]
    assert all(type(x) is int for x in poly) and len(poly)==n+1
    assert poly[0]==poly[-1]==1 and poly==poly[::-1]
    # n+1 exact distinct evaluations identify the whole degree<=n determinant.
    for at in range(n+1):
        got=determinant([[at*V[i][j]+V[j][i] for j in range(n)] for i in range(n)])
        assert got==ev(poly,at),(label,at,got,ev(poly,at))
        COUNTS["pencil_determinants"]+=1
    f=rec["factorization"];assert set(f)=={"constant","factors"} and type(f["constant"]) is int
    rebuilt=[f["constant"]]
    for factor in f["factors"]:
        assert set(factor)=={"coefficients_ascending","multiplicity"}
        fp=factor["coefficients_ascending"];m=factor["multiplicity"]
        assert type(m) is int and m>=1 and len(fp)>=2 and fp[-1]==1
        assert all(type(x) is int for x in fp)
        rebuilt=mul(rebuilt,powp(fp,m))
    assert rebuilt==poly
    energy=sum(V[i][j]**2 for i in range(n) for j in range(i+1,n))
    expected={"matrix":V,"dimension":n,"height":max(abs(x) for row in V for x in row),
              "strict_energy":energy,"full_squared_sum":energy+n,"coefficients_ascending":poly,
              "factorization":f,"monodromy_trace":-poly[-2],
              "support_degrees":[sum(bool(V[min(i,j)][max(i,j)]) for j in range(n) if j!=i) for i in range(n)]}
    cmp(rec,expected,label)
    COUNTS["factor_products"]+=1;COUNTS["matrices"]+=1
    return poly
def verify(data):
    required={'status', 'domain', 'method', 'seed', 'instances', 'matrix_count'}
    assert set(data)==required
    for k,v in {"status":"passed","domain":[3,4,5,6],"method":"integer triangular inverse and exact characteristic polynomial","matrix_count":24}.items():
        cmp(data[k],v,k)
    pass
    pass
    A=[1,0,-2,-4,1];Ast=A[::-1]
    cmp(data["seed"],{"A":A,"A_reversal":Ast,"A_at_4":ev(A,4),"A_at_5":ev(A,5),"A_reversal_at_5":ev(Ast,5)},"seed")
    assert len(data["instances"])==4
    reports=[]
    for k,row in zip(range(3,7),data["instances"]):
        gate();V,Z=graph(k);U=absolute(V)
        mats={"V":V,"U":U,"WV":lift(V),"Z":Z,"ZU":absolute(Z),"WZ":lift(Z)}
        assert set(row["matrices"])==set(mats)
        polys={name:record(row["matrices"][name],v,str(k)+"/"+name) for name,v in mats.items()}
        C=[[1]*(j+1) for j in range(k+1)];T=[matching(j) for j in range(k)]
        F=divide(add(shift(A,k+1),scale(Ast,-1)),[-1,1])
        q=[1,1];d=[1,0,1];q2=mul(q,q)
        bycycle=add(mul(add(mul(d,d),shift(scale(q2,-1),1)),C[k]),
           shift(scale(mul(mul(d,q),C[k-1]),-2),1),shift(mul(q2,C[k-2]),2),
           mul(scale(q2,-1),add(shift([1],k+1),[0,1])))
        assert F==bycycle
        G=add(mul(F,T[k-1]),
           shift(scale(mul(add(mul(d,C[k]),shift(scale(mul(q,C[k-1]),-1),1)),T[k-2]),-8),2),
           shift(scale(mul(C[k],T[k-3]),16),4),
           scale(mul(q,add(shift(add(C[k],[1]),2*k),shift(C[k],1),shift([1],k+1))),-2**k))
        original=mul(mul(powp(q,k-1),powp([-1,1],2*k-2)),F)
        companion=mul(powp(q,k-1),G)
        assert polys["V"]==polys["Z"]==polys["ZU"]==original
        assert polys["U"]==companion and polys["WV"]==mul(original,companion) and polys["WZ"]==mul(original,original)
        mixed=paths(V)
        assert mixed==[5*k+2 if j==1 else 1 if j==k+1 else 2**k if j==2*k else 0 for j in range(1,4*k+1)]
        expected={"k":k,"r":k,"F":F,"G":G,"C":C,"T":T,"F_at_1":-4*k-12,
                  "mixed_traces":mixed,"matrices":row["matrices"],"reciprocal_trace_rhs":2**k-3*k+5,
                  "exponential_measure_lower":2**k-3*k+4}
        cmp(row,expected,str(k));assert ev(F,1)==-4*k-12
        assert -len(V)+sum(mixed)==-companion[-2]==k+2**k+2
        COUNTS["continuants"]+=len(C)+len(T);COUNTS["mixed_trace_entries"]+=len(mixed)
        reports.append({"k":k,"all_native_mathematics_verified":True,"full_matrices":6,"full_pencil_evaluations":sum(len(v)+1 for v in mats.values())})
    assert COUNTS=={"matrices":24,"pencil_determinants":632,"factor_products":24,"continuants":40,"mixed_trace_entries":72}
    return reports
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,default=(_J_OUTPUT / 'review_result.json'))
    target=parser.parse_args().output.resolve();assert target.parent==_J_OUTPUT
    handle=target.open("x",encoding="utf8")
    result={'status': 'started'}
    before={name:(((_J_PROGRAM if name in ('binary-invariants.py', 'binary-review.py', 'mutation-probe.py', 'mutation-review.py', 'readme.md', 'repeated-cell-author.py', 'repeated-cell-review.py', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes() for name in ("verify.py","result.json","readme.md")}
    try:
        result["instances"]=verify(json.loads(before["result.json"]));gate()
        result.update(status='complete', counts=COUNTS, strict_scalar_comparisons=LEAVES, all_native_math_fields_verified=True, factor_scope='All coefficients and complete product identities; no independent library-factor irreducibility claim')
    except Exception as error:
        result.update(status="incomplete",error_type=type(error).__name__,error=_record_text(str(error)),traceback=_record_text(traceback.format_exc()),counts=COUNTS)
        raise
    finally:
        result.update()
        json.dump(result,handle,indent=2);handle.write("\n");handle.close()
        print(json.dumps({k:v for k,v in result.items() if k!="instances"}),flush=True)
if __name__=="__main__":main()

