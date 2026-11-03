"""Exact binary congruence certificates, only k3..6 original V/Z forms."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import argparse,json,time,platform,traceback
from review_independent import graph
BASE=(_J_PROGRAM / 'binary-invariants.py').parent
START=time.perf_counter();CAP=60
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
    if time.perf_counter()-START>=CAP:raise TimeoutError("Declared60second author cap")
def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def product(A,B):
    return [[sum(x*y for x,y in zip(row,col))%2 for col in zip(*B)] for row in A]
def rref(matrix):
    gate();R=[row[:] for row in matrix];m=len(R);n=len(R[0]) if m else 0;E=identity(m)
    pivots=[];ops=[];at=0
    for col in range(n):
        pivot=next((i for i in range(at,m) if R[i][col]),None)
        if pivot is None:continue
        if pivot!=at:
            R[at],R[pivot]=R[pivot],R[at];E[at],E[pivot]=E[pivot],E[at];ops.append(["swap",at,pivot])
        for i in range(m):
            if i!=at and R[i][col]:
                R[i]=[x^y for x,y in zip(R[i],R[at])]
                E[i]=[x^y for x,y in zip(E[i],E[at])]
                ops.append(["add",i,at])
        pivots.append(col);at+=1
        if at==m:break
    assert product(E,matrix)==R
    return R,E,ops,pivots
def kernel(R,pivots):
    n=len(R[0]);free=[j for j in range(n) if j not in pivots];basis=[]
    for j in free:
        vec=[int(h==j) for h in range(n)]
        for row,col in enumerate(pivots):vec[col]=R[row][j]
        basis.append(vec)
    return basis
def theoretical(k,name):
    n=4*k+1;out=[]
    if name=="V":
        size=k+2 if k%2 else k+1
        for h in range(size):
            p=[int(h==j) for j in range(size)]
            A=p[0];T=p[1] if k%2 else A;U=A^T if k%2 else 0
            Bs=p[2:] if k%2 else p[1:];v=[0]*n
            for j in range(k):
                v[3*j]=A;v[3*j+1]=Bs[j];v[3*j+2]=Bs[j]^U
            v[4*k]=A
            for j in range(1,k+1):v[3*k+j-1]=T if j%2 else A
            out.append(v)
    else:
        size=3 if k%2 else 2
        for h in range(size):
            p=[int(h==j) for j in range(size)]
            T=p[0] if k%2 else 0
            left,right=p[1:] if k%2 else p
            v=[0]*n
            for j in range(1,k+1):v[j]=T if j%2 else 0
            v[k+2]=left;v[k+3]=left^T;v[k+4]=right;v[k+5]=right^T
            out.append(v)
        for i in range(k+6,n):out.append([int(j==i) for j in range(n)])
    return out
def compute(k,name,V):
    n=len(V);S=[[(V[i][j]+V[j][i])%2 for j in range(n)] for i in range(n)]
    R,E,ops,pivots=rref(S);basis=kernel(R,pivots);formula=theoretical(k,name)
    zero=[[0]*len(basis) for _ in range(n)]
    assert product(S,list(map(list,zip(*basis))))==zero
    assert product(S,list(map(list,zip(*formula))))==[[0]*len(formula) for _ in range(n)]
    formula_rank=len(rref(formula)[3])
    predicted=3*k-k%2 if name=="V" else k+4-k%2
    assert len(pivots)==predicted and len(basis)==len(formula)==formula_rank==n-predicted
    for op,i,j in ops:assert op in ("swap","add") and i!=j and 0<=i<n and 0<=j<n
    return {"name":name,"k":k,"dimension":n,"original_matrix":V,"binary_symmetrization":S,
            "rref":R,"row_transform":E,"row_operations":ops,"pivot_columns":pivots,
            "nullspace_basis":basis,"formula_kernel_basis":formula,"formula_basis_rank":formula_rank,
            "rank":len(pivots),"nullity":len(basis),"predicted_rank":predicted,
            "all_exact_checks":True}
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,default=(_J_OUTPUT / 'binary-invariants.json'))
    target=parser.parse_args().output.resolve();assert target.parent==_J_OUTPUT
    handle=target.open("x",encoding="utf8")
    out={'status': 'started', 'domain_k': [3, 4, 5, 6], 'input': 'result.json', 'graph_helper': 'review_independent.py:graph', 'instances': []}
    names=("verify.py","result.json","review_independent.py","review_result.json")
    before={name:(((_J_PROGRAM if name in ('binary-invariants.py', 'binary-review.py', 'mutation-probe.py', 'mutation-review.py', 'readme.md', 'repeated-cell-author.py', 'repeated-cell-review.py', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes() for name in names}
    try:
        saved=json.loads(before["result.json"])
        for k in (3,4,5,6):
            gate();V,Z=graph(k)
            old=next(x for x in saved["instances"] if x["k"]==k)
            assert V==old["matrices"]["V"]["matrix"] and Z==old["matrices"]["Z"]["matrix"]
            rv=compute(k,"V",V);rz=compute(k,"Z",Z)
            diff=rv["rank"]-rz["rank"];assert diff==2*k-4>0
            out["instances"].append({"k":k,"V":rv,"Z":rz,"rank_difference":diff,
                                     "not_integrally_congruent":True,"common_stabilization_excluded":True})
            print("k",k,"ranks",rv["rank"],rz["rank"],"difference",diff,flush=True)
        gate();out["status"]="complete"
        pass
    except Exception as error:
        out.update(status="incomplete",error_type=type(error).__name__,error=_record_text(str(error)),traceback=_record_text(traceback.format_exc()))
        raise
    finally:
        out.update()
        json.dump(out,handle,indent=2);handle.write("\n");handle.close()
        print(json.dumps({k:v for k,v in out.items() if k!="instances"}),flush=True)
if __name__=="__main__":main()

