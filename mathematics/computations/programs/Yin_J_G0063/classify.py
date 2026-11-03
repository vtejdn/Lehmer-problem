"""All binary congruence classes and their full Gram lift modulo four.

Rows of a binary 6x6 matrix are six integers in [0,64); entry(i,j)
is bit j of row i. A basis record stores these rows; upper forms are
15-bit masks in lexicographic (i,j), i<j order. All finite sets retained.
"""
import json
import time
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

N = 6
V = [[0,-1,-2,0,-1,0],[1,0,-1,1,0,1],[2,1,0,2,1,1],
     [0,-1,-1,0,-1,0],[1,-1,-1,1,0,1],[1,-1,-1,0,-1,0]]
UP = [(i,j) for i in range(N) for j in range(i+1,N)]
SELECT = [(i,j) for i in range(N) for j in range(i)] + [(i,i) for i in range(N)]
IDENT = [1 << i for i in range(N)]
CAP_SECONDS = 120

def rows(a):
    return [sum((x & 1) << j for j,x in enumerate(row)) for row in a]

def transpose(a):
    return [sum(((a[i] >> j) & 1) << i for i in range(N)) for j in range(N)]

def mv(a,v):
    return sum(((r & v).bit_count() & 1) << i for i,r in enumerate(a))

def mm(a,b):
    out=[]
    for r in a:
        s=0
        while r:
            bit=r & -r
            s ^= b[bit.bit_length()-1]
            r ^= bit
        out.append(s)
    return out

def inv(a):
    b=[r | (1 << (N+i)) for i,r in enumerate(a)]
    for j in range(N):
        pivot=next((i for i in range(j,N) if (b[i] >> j)&1),None)
        if pivot is None:
            return None
        b[j],b[pivot]=b[pivot],b[j]
        for i in range(N):
            if i != j and (b[i] >> j)&1:
                b[i] ^= b[j]
    return [r >> N for r in b]

def krylov(c,v):
    columns=[]
    for _ in range(N):
        columns.append(v)
        v=mv(c,v)
    return transpose(columns)

def annihilates(c):
    # F mod2 = t^6+t^4+t^3+t^2+1.
    p=[0]*N
    for coefficient in [1,0,1,1,1,0,1]:
        p=mm(p,c)
        if coefficient:
            p=[x^y for x,y in zip(p,IDENT)]
    return not any(p)

def reduction(u):
    a=[]
    for i,j in SELECT:
        row=0
        for v in range(N):
            for w in range(N):
                coefficient=((w==i) and ((u[v]>>j)&1)) ^ ((w==j) and ((u[i]>>v)&1))
                row |= int(coefficient) << (N*v+w)
        a.append(row)
    original=a[:]
    ops=[1<<i for i in range(len(a))]
    rank=0
    pivots=[]
    for col in range(N*N):
        pivot=next((i for i in range(rank,len(a)) if (a[i]>>col)&1),None)
        if pivot is None:
            continue
        a[rank],a[pivot]=a[pivot],a[rank]
        ops[rank],ops[pivot]=ops[pivot],ops[rank]
        for i in range(len(a)):
            if i != rank and ((a[i]>>col)&1):
                a[i] ^= a[rank]
                ops[i] ^= ops[rank]
        pivots.append(col)
        rank+=1
    for witness in ops[rank:]:
        check=0
        for i in range(len(original)):
            if (witness>>i)&1:
                check ^= original[i]
        assert check == 0
    return rank,a,ops,pivots

def run():
    started=time.monotonic()
    def within_cap():
        if time.monotonic()-started > CAP_SECONDS:
            raise TimeoutError("Declared 120-second finite classification cap reached")
    v2=rows(V)
    c0=mm(inv(v2),transpose(v2))
    assert annihilates(c0)
    k0={w:krylov(c0,w) for w in range(64)}
    cyclic0={w:k for w,k in k0.items() if inv(k) is not None}
    assert cyclic0
    pair=[[sum(((a>>i)&1)*V[i][j]*((b>>j)&1)
               for i in range(N) for j in range(N)) for b in range(64)] for a in range(64)]
    result={"domain":{"all_upper_forms":32768,"all_vector_images":64,"modulus":4},
            "V0":V,"C0_rows":c0,"cyclic_vectors_C0":list(cyclic0),
            "counts":{"processed_upper_forms":0,"nonsingular_symmetric_forms":0,"annihilator_forms":0,
                      "cyclic_forms":0,"congruent_forms":0,"binary_bases":0,"liftable_bases":0,"nonliftable_bases":0},
            "forms":[],"complete":False}
    seen=set()
    counts=result["counts"]
    try:
        for mask in range(32768):
            if mask%32==0:
                within_cap()
            u=IDENT[:]
            for k,(i,j) in enumerate(UP):
                u[i] |= ((mask>>k)&1)<<j
            counts["processed_upper_forms"]+=1
            ut=transpose(u)
            if inv([a^b for a,b in zip(u,ut)]) is None:
                continue
            counts["nonsingular_symmetric_forms"]+=1
            cu=mm(inv(u),ut)
            if not annihilates(cu):
                continue
            counts["annihilator_forms"]+=1
            vu=None
            for candidate in range(64):
                ki=inv(krylov(cu,candidate))
                if ki is not None:
                    vu=candidate
                    break
            if vu is None:
                continue
            counts["cyclic_forms"]+=1
            bases=[]
            for w,k in cyclic0.items():
                q=mm(k,ki)
                assert inv(q) is not None
                cols=transpose(q)
                b=[[pair[a][bb] for bb in cols] for a in cols]
                if rows(b) != u:
                    continue
                tq=tuple(q)
                assert tq not in seen
                seen.add(tq)
                bases.append((q,b,w))
            if not bases:
                continue
            counts["congruent_forms"]+=1
            rank,rr,ops,pivots=reduction(u)
            frecord={"upper_mask":mask,"upper_rows":u,"cyclic_vector":vu,
                     "linear_rank":rank,"left_kernel_basis":ops[rank:],"bases":[]}
            for q,b,w in bases:
                counts["binary_bases"]+=1
                e=0
                for k,(i,j) in enumerate(SELECT):
                    numerator=b[i][j]-int(i==j)
                    assert numerator%2==0
                    e |= ((numerator//2)&1)<<k
                witness=next((z for z in ops[rank:] if (z&e).bit_count()&1),None)
                record={"Q_rows":q,"image_vector":w,"error_bits":e}
                if witness is not None:
                    counts["nonliftable_bases"]+=1
                    record["inconsistency_witness"]=witness
                else:
                    counts["liftable_bases"]+=1
                    x=sum(((ops[i]&e).bit_count()&1)<<pivots[i] for i in range(rank))
                    xx=[(x>>(N*i))&63 for i in range(N)]
                    h=[a^bb for a,bb in zip(mm(transpose(xx),u),mm(u,xx))]
                    gram=[[(b[i][j]+2*((h[i]>>j)&1))%4 for j in range(N)] for i in range(N)]
                    assert all(gram[i][j]==int(i==j) for i,j in SELECT)
                    record.update({"correction_bits":x,"gram_mod4":gram})
                frecord["bases"].append(record)
            result["forms"].append(frecord)
        within_cap()
        result["complete"]=True
    except TimeoutError as exc:
        result["cap_failure"]=str(exc)
    pass
    return result

if __name__ == "__main__":
    result=run()
    (_J_OUTPUT / 'classification.json').write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k not in ["V0","forms"]},indent=2))
