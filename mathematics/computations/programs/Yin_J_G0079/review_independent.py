"""Independent quotient-basis reconstruction of all fifteen J79 projections."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from math import comb, lcm
import argparse,json,time,platform
BASE=(_J_PROGRAM / 'review_independent.py').parent
START=time.monotonic()
CAP=120
def gate():
    if time.monotonic()-START>CAP: raise RuntimeError("Declared reviewer runtime cap exceeded")
def inverse(matrix):
    n=len(matrix)
    a=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(matrix)]
    for col in range(n):
        gate()
        piv=next(i for i in range(col,n) if a[i][col])
        a[col],a[piv]=a[piv],a[col]
        s=a[col][col];a[col]=[v/s for v in a[col]]
        for i in range(n):
            if i!=col and a[i][col]:
                s=a[i][col];a[i]=[v-s*w for v,w in zip(a[i],a[col])]
    return [row[n:] for row in a]
def lift(coeff,q):
    out=[0]*((len(coeff)-1)*q+1)
    for j,c in enumerate(coeff):out[j*q]=c
    return out
lehmer=[1,1,0,-1,-1,-1,-1,-1,0,1,1]
INPUTS=[("quadratic",[1,-3,1],"actual"),("quartic",[1,-1,-1,-1,1],"actual"),
        ("sextic",[1,-1,0,-1,0,-1,1],"actual"),("lehmer",lehmer,"actual"),
        ("lehmer_square",lift(lehmer,2),"actual"),("lehmer_fourth",lift(lehmer,4),"actual")]
INPUTS += [(f"cyclotomic_{p}",[1]*p,"calibration") for p in (3,5,7,11,17)]
INPUTS += [(f"repeated_{d}",[comb(d,j)*(-1)**(d-j) for j in range(d+1)],"calibration") for d in (2,4,8,12)]
lo=2*sum((F(1,3**(2*k+1)*(2*k+1)) for k in range(20)),F(0))
hi=lo+F(2,3**41*41)/(1-F(1,9))
def reconstruct(name,coeff,scope):
    d=len(coeff)-1;n=2*d
    # Columns are remainders of t^j modulo the monic P, not coefficient multiples.
    rem=[[int(i==j) for i in range(d)] for j in range(d)]
    for j in range(d,n):
        prev=rem[-1];top=prev[-1]
        rem.append([(-top*coeff[i])+(prev[i-1] if i else 0) for i in range(d)])
    gram=[[sum(v[i]*v[j] for v in rem) for j in range(d)] for i in range(d)]
    inv=inverse(gram)
    dual=[[sum((row[k]*v[k] for k in range(d)),F(0)) for v in rem] for row in inv]
    R=[[sum((rem[i][k]*dual[k][j] for k in range(d)),F(0)) for j in range(n)] for i in range(n)]
    q=lcm(*(v.denominator for row in R for v in row))
    C=[[int(q*v) for v in row] for row in R]
    assert all(F(C[i][j],q)==R[i][j] for i in range(n) for j in range(n))
    # Independently recover each multiplier by exact descending monic polynomial division.
    U=[[0]*n for _ in range(n-d)]
    for j in range(n):
        v=[q*int(i==j)-C[i][j] for i in range(n)]
        for power in range(n-1,d-1,-1):
            u=v[power];U[power-d][j]=u
            for h,a in enumerate(coeff):v[power-d+h]-=u*a
        assert all(x==0 for x in v)
    assert all(C[i][j]==C[j][i] for i in range(n) for j in range(n))
    assert sum(C[i][i] for i in range(n))==q*d
    for i in range(n):
        gate()
        for j in range(n):
            assert sum(C[i][k]*C[k][j] for k in range(n))==q*C[i][j]
    a=[sum((R[j][j+h] for j in range(n-h)),F(0)) for h in range(1,n)]
    kap=2*sum(map(abs,a),F(0))/d
    test="true-certified" if kap<=1+lo else "false-certified" if kap>1+hi else "undecided-at-declared-precision"
    return {"name":name,"scope":scope,"coefficients_ascending":coeff,"d":d,"N":n,
            "q":str(q),"C_rows":[list(map(str,row)) for row in C],
            "U_rows":[list(map(str,row)) for row in U],
            "signed_diagonal_sums":list(map(str,a)),"kappa":str(kap),
            "endpoint_diagonals":[str(R[0][0]),str(R[-1][-1])],
            "kappa_le_2":bool(kap<=2),"kappa_le_1_plus_log2":test,
            "identity_checks":["C+A*U=qI","C.T=C","C*C=qC","trace(C)=qd"]}
leaves=0
def compare(a,b,path=""):
    global leaves
    assert type(a) is type(b),(path,type(a),type(b))
    if isinstance(a,dict):
        assert set(a)==set(b),(path,set(a)^set(b))
        for k in a:compare(a[k],b[k],path+"/"+k)
    elif isinstance(a,list):
        assert len(a)==len(b),(path,len(a),len(b))
        for i,(x,y) in enumerate(zip(a,b)):compare(x,y,path+f"/{i}")
    else:
        assert a==b,(path,a,b)
        leaves+=1
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=(_J_OUTPUT / 'review-result.json'))
    args=parser.parse_args()
    paths=[(_J_PROGRAM / 'author.py'),(_J_OUTPUT / 'author-output.json'),(_J_PROGRAM / 'readme.md')]
    before={p:p.read_bytes() for p in paths}
    native=json.loads(before[paths[1]])
    assert set(native)=={'log2_interval', 'records', 'status'}
    compare(native["status"],"complete","status")
    compare(native["log2_interval"],[str(lo),str(hi)],"log2_interval")
    pass
    assert len(native["records"])==len(INPUTS)==15
    results=[];last=0
    for row,(name,coeff,scope) in zip(native["records"],INPUTS):
        gate()
        expected=reconstruct(name,coeff,scope)
        assert set(row)==set(expected)
        pass
        compare(row,expected,name)
        results.append({"name":name,"d":expected["d"],"N":expected["N"],"kappa":expected["kappa"],
                        "matrix_entries":sum(len(r) for r in expected["C_rows"]+expected["U_rows"]),
                        "complete_native_match":True})
        print(name,expected["kappa"],"complete match",flush=True)
    assert all(p.read_bytes()==b for p,b in before.items()),"Read-only author inputs changed during review"
    gate()
    output={'status': 'complete', 'method': 'quotient-monomial remainders, Fraction row-Gram inverse, monic division', 'declared_domain_count': 15, 'records': results, 'mathematical_scalar_leaves': leaves, 'all_author_mathematical_fields_match': True}
    target=args.output.resolve()
    assert target.parent==_J_OUTPUT.resolve(),"Keep reviewer outputs in this computation group"
    target.write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in output.items() if k!="records"}),flush=True)
if __name__=="__main__":main()
