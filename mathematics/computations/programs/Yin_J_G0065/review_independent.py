"""Separate D146 review, declared before execution.
Complete domain: ALL 32768 binary upper forms by direct F2 determinant subset DP;
all 375 selected coefficient derivatives via deleted-row/column cofactors;
all ordered norm-one bases of each of the three changed forms and all native
Gram witnesses; full original/absolute/literal rank12 coefficient determinants.
120-second cap. No author imports, external packages or source-data hash gates.
Elementary helper arithmetic is reused from root's independent J63 checker.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from time import perf_counter
from collections import Counter
import json,platform
HOME=(_J_PROGRAM / 'review_independent.py').parent
N=6
UP=[(i,j) for i in range(6) for j in range(i+1,6)]
POS=[(i,j) for i in range(6) for j in range(i)]+[(i,i) for i in range(6)]
NATIVE=("changed.py","changed_result.json","target.py","target_result.json","verify.py","verification.json","readme.md")
def tr(a):
    return [list(c) for c in zip(*a)]

def mul(a,b):
    return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]

def bits(a):
    return tuple(sum((x&1)<<j for j,x in enumerate(r)) for r in a)

def matrix(rows):
    return [[(r>>j)&1 for j in range(N)] for r in rows]

def column_rows(cols):
    return tuple(sum(((v>>i)&1)<<j for j,v in enumerate(cols)) for i in range(N))

def span(columns):
    """Image-space echelon basis, highest set bit; no row left-kernel reduction."""
    basis = {}
    for c in columns:
        while c:
            p=c.bit_length()-1
            if p not in basis:
                basis[p]=c
                break
            c ^= basis[p]
    return basis

def residue(value,basis):
    for p in sorted(basis,reverse=True):
        if (value>>p)&1:
            value ^= basis[p]
    return value

def act(cols,v):
    answer=0
    for j,c in enumerate(cols):
        if (v>>j)&1:
            answer ^= c
    return answer

def cyclic_columns(cols,v):
    ans=[]
    for _ in range(N):
        ans.append(v)
        v=act(cols,v)
    return ans

def annihilated(cols):
    # Evaluate I+C^2+C^3+C^4+C^6 on each standard basis vector.
    for j in range(N):
        w=1<<j
        value=0
        for k in range(7):
            if k in (0,2,3,4,6):
                value ^= w
            w=act(cols,w)
        if value:
            return False
    return True

def solve_binary(a,rhs):
    # Tiny augmented elimination, used ONLY to derive C0, not for compatibility.
    b=[[x&1 for x in r]+[(rhs[i]>>0)&1] for i,r in enumerate(a)]
    for j in range(len(a)):
        p=next(i for i in range(j,len(a)) if b[i][j])
        b[j],b[p]=b[p],b[j]
        for i in range(len(a)):
            if i!=j and b[i][j]:
                b[i]=[x^y for x,y in zip(b[i],b[j])]
    return sum(b[i][-1]<<i for i in range(len(a)))

def determinant(a):
    a=[r[:] for r in a]
    n=len(a);sign=1;previous=1
    for k in range(n-1):
        if not a[k][k]:
            p=next((i for i in range(k+1,n) if a[i][k]),None)
            if p is None:
                return 0
            a[k],a[p]=a[p],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*pivot-a[i][k]*a[k][j]
                assert value%previous==0
                a[i][j]=value//previous
            a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]

def pencil(a):
    """Full coefficient determinant by subset/permutation DP, no interpolation."""
    n=len(a)
    dp={0:[1]}
    for row in range(n):
        nxt={}
        for mask,p in dp.items():
            for col in range(n):
                if (mask>>col)&1:
                    continue
                c0=a[col][row];c1=a[row][col]
                if c0==c1==0:
                    continue
                sign=-1 if (mask>>(col+1)).bit_count()%2 else 1
                out=nxt.setdefault(mask|(1<<col),[0]*(row+2))
                for k,coef in enumerate(p):
                    out[k]+=sign*c0*coef
                    out[k+1]+=sign*c1*coef
        dp=nxt
    return dp[(1<<n)-1]

def convolve(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j]+=a*b
    return out


def f2det(poly):
    n=len(poly);dp=[0]*(1<<n);dp[0]=1
    for mask in range((1<<n)-1):
        row=mask.bit_count();value=dp[mask]
        if not value:continue
        for j,p in enumerate(poly[row]):
            if mask>>j&1 or not p:continue
            term=(value if p&1 else 0)^((value<<1) if p&2 else 0)
            dp[mask|1<<j]^=term
    return dp[-1]

def abc_bits(p):
    return ((p>>5)&1)|(((p>>4)&1)<<1)|(((p>>3)&1)<<2)

def run():
    start=perf_counter()
    def cap():assert perf_counter()-start<120,"Independent120-secondcap"
    original={x:(((_J_PROGRAM if x in ('changed.py', 'readme.md', 'review_independent.py', 'target.py', 'verify.py') else _J_OUTPUT) / x)).read_bytes() for x in NATIVE}
    changed=json.loads(original["changed_result.json"]);target=json.loads(original["target_result.json"])
    assert changed["complete"] and target["complete"]
    assert target["scope"]["all_residue_matrices"]==4**15
    target_map={x["upper_mask"]:x for x in target["forms"]}
    full_parity=sum(1<<j for j in (0,2,3,4,6))
    matches=[];residues=Counter();derivatives=0
    stages={'processed_upper_forms':32768,'nonsingular_symmetric_forms':0,'annihilator_forms':0,'cyclic_forms':0}
    for mask in range(32768):
        if mask%128==0:cap()
        u=[[int(i==j) for j in range(6)] for i in range(6)]
        for k,(i,j) in enumerate(UP):u[i][j]=(mask>>k)&1
        symcols=[sum((u[i][j]^u[j][i])<<i for i in range(6)) for j in range(6)]
        if len(span(symcols))==6:
            stages["nonsingular_symmetric_forms"]+=1
            ccols=[]
            for j in range(6):
                xx=[0]*6
                for i in reversed(range(6)):
                    xx[i]=(u[j][i]+sum(u[i][k]*xx[k] for k in range(i+1,6)))&1
                ccols.append(sum(z<<i for i,z in enumerate(xx)))
            if annihilated(ccols):
                stages["annihilator_forms"]+=1
                if any(len(span(cyclic_columns(ccols,z)))==6 for z in range(64)):
                    stages["cyclic_forms"]+=1
        entries=[[u[j][i]|(u[i][j]<<1) for j in range(6)] for i in range(6)]
        p=f2det(entries)
        if p!=full_parity:continue
        matches.append(mask)
        exact=pencil(u);abc=[exact[k] for k in (5,4,3)]
        rec=target_map[mask]
        assert abc==rec["integer_coefficients"] and bits(u)==tuple(rec["upper_rows"])
        assert [x%4 for x in abc]==[2,3,3]
        columns=[]
        for i,j in UP:
            # formal determinant derivative: t cofactor(i,j)+cofactor(j,i)
            first=f2det([[entries[a][b] for b in range(6) if b!=j] for a in range(6) if a!=i])
            second=f2det([[entries[a][b] for b in range(6) if b!=i] for a in range(6) if a!=j])
            columns.append(abc_bits((first<<1)^second))
        assert columns==rec["derivative_columns"];derivatives+=len(columns)
        image={0}
        for c in columns:image|={v^c for v in tuple(image)}
        assert sorted(image)==rec["image_vectors"]==[0,3]
        rhs=sum((((a-b)//2)&1)<<i for i,(a,b) in enumerate(zip((-2,1,-1),abc)))
        assert rhs==rec["right_side"] and rhs not in image
        assert rec["inconsistency_witness"]==3 and (rhs&3).bit_count()%2==1
        residues[tuple(x%4 for x in abc)]+=1
    assert matches==sorted(target_map) and len(matches)==375 and derivatives==5625
    assert stages==changed["common_counts"]
    cap()
    v=changed["V"];c=changed["C"];r=changed["R"];ri=changed["R_inverse"]
    ident=[[int(i==j) for j in range(6)] for i in range(6)]
    assert determinant(v)==determinant(c)==determinant(r)==1
    assert mul(v,c)==[[-x for x in row] for row in tr(v)]
    assert mul(r,ri)==mul(ri,r)==ident and mul(tr(r),v)==mul(v,r)
    c2=mul(c,c);c4=mul(c2,c2)
    assert mul(r,c2)==[[c4[i][j]+ident[i][j] for j in range(6)] for i in range(6)]
    assert mul(r,c)==mul(c,r)
    form_results=[]
    for model in changed["classifications"]:
        b=model["matrix"]
        pair=[[sum(((x>>i)&1)*b[i][j]*((y>>j)&1) for i in range(6) for j in range(6))
               for y in range(64)] for x in range(64)]
        normone=[x for x in range(64) if pair[x][x]&1]
        found={};levels=[0]*7
        def extend(cols,candidates):
            levels[len(cols)]+=1
            if len(cols)==6:
                key=column_rows(cols);assert key not in found
                gram=[[pair[x][y] for y in cols] for x in cols]
                mask=sum((gram[i][j]&1)<<k for k,(i,j) in enumerate(UP))
                found[key]=(mask,gram);return
            for x in candidates:
                extend(cols+[x],[y for y in candidates if pair[y][x]%2==0])
        extend([],normone);cap()
        assert len(found)==5625
        saved=set();rank_counts=Counter()
        for form in model["forms"]:
            u=matrix(form["upper_rows"]);mask=form["upper_mask"]
            images=[sum(((int(j==bb)*u[i][aa]+int(i==bb)*u[aa][j])&1)<<k
                        for k,(i,j) in enumerate(POS)) for aa in range(6) for bb in range(6)]
            image_space=span(images);rank=len(image_space)
            assert rank==form["linear_rank"]==19;rank_counts[rank]+=1
            kernel=form["left_kernel_basis"]
            assert len(kernel)==len(span(kernel))==2
            assert all((z&im).bit_count()%2==0 for z in kernel for im in images)
            for rec in form["bases"]:
                key=tuple(rec["Q_rows"]);assert key not in saved;saved.add(key)
                found_mask,gram=found[key];assert found_mask==mask
                assert bits(gram)==tuple(form["upper_rows"])
                error=0
                for k,(i,j) in enumerate(POS):
                    value=gram[i][j]-int(i==j);assert value%2==0
                    error|=((value//2)&1)<<k
                assert error==rec["error_bits"] and residue(error,image_space)!=0
                z=rec["inconsistency_witness"]
                assert all((z&im).bit_count()%2==0 for im in images)
                assert (z&error).bit_count()%2==1
            cap()
        assert saved==set(found)
        assert model["counts"]=={"congruent_forms":375,"binary_bases":5625,"liftable_bases":0,"nonliftable_bases":5625}
        form_results.append({"name":model["name"],"norm_one_count":len(normone),
                             "prefix_counts":levels,"complete_basis_count":len(found),
                             "linear_rank_counts":dict(rank_counts)})
    costs=[]
    for rec in changed["costs"]:
        b=rec["matrix"];ab=[[-abs(x) for x in row] for row in b]
        cover=[[0]*12 for _ in range(12)]
        for i in range(6):
            for j in range(6):
                for sheet in range(2):cover[2*i+sheet][2*j+(sheet if b[i][j]<=0 else 1-sheet)]=-abs(b[i][j])
        assert rec["absolute_matrix"]==ab and rec["literal_cover"]==cover
        mats=[b,ab,cover];polys=[pencil(x) for x in mats]
        assert polys==[rec["original_polynomial"],rec["absolute_polynomial"],rec["cover_polynomial"]]
        assert polys[2]==convolve(polys[0],polys[1])
        assert polys[0]==[1,-2,1,-1,1,-2,1]
        assert all(determinant(x)!=0 for x in mats) and rec["ranks"]==[6,6,12]
        assert rec["degrees"]==[len(x)-1 for x in polys]
        assert rec["heights"]==[max(abs(x) for row in m for x in row) for m in mats]
        assert rec["whole_squared_entry_sums"]==[sum(x*x for row in m for x in row) for m in mats]
        assert rec["absolute_coefficient_l1"]==sum(abs(x) for x in polys[1])
        assert rec["absolute_zero"] is False and rec["proper_upper_unitriangular"] is False
        for t in range(-6,7):
            value=determinant([[t*cover[i][j]+cover[j][i] for j in range(12)] for i in range(12)])
            assert value==sum(x*t**j for j,x in enumerate(polys[2]))
        assert rec["direct_cover_evaluations"]==13
        costs.append({"name":rec["name"],"polynomials":polys});cap()
    assert all((((_J_PROGRAM if name in ('changed.py', 'readme.md', 'review_independent.py', 'target.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes()==raw for name,raw in original.items())
    return {'passed': True, 'method': 'unfiltered F2 subset determinants, deleted-row/column cofactor derivatives, direct norm-one column recursion, full integer subset determinants', 'author_imports': False, 'third_party_imports': False, 'complete_binary_domain': 32768, 'changed_form_stages': stages, 'target_parity_forms': 375, 'all_derivative_columns': derivatives, 'base_residues': {str(k): v for k, v in residues.items()}, 'lift_residues': [[2, 3, 3], [0, 1, 3]], 'changed_form_full_enumerations': form_results, 'full_costs': costs}
if __name__=="__main__":
    report=run()
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))
