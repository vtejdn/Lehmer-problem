"""Author self-check using determinant permutations and Boolean coefficients.

All 32768 binary coefficient triples are rebuilt without the annihilator
filter or triangular trace formulas. Derivatives are formal derivatives
of the integer determinant monomials, not finite differences. This remains
an author self-check; separately assigned whole review is still required.
"""
import itertools,json,math,time
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

HERE=(_J_PROGRAM / 'verify.py').parent
UP=[(i,j) for i in range(6) for j in range(i+1,6)]
INDEX={ij:k for k,ij in enumerate(UP)}
SELECT=[(i,j) for i in range(6) for j in range(i)]+[(i,i) for i in range(6)]

def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def tr(a):return [list(x) for x in zip(*a)]
def decode(rows):return [[(r>>j)&1 for j in range(6)] for r in rows]
def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

PERMS=[]
for p in itertools.permutations(range(6)):
    sign=(-1)**sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))
    PERMS.append((p,sign))

def pencil(a):
    out=[0]*7
    for p,sign in PERMS:
        term=[sign]
        for i,j in enumerate(p):term=poly_mul(term,[a[j][i],a[i][j]])
        for k,x in enumerate(term):out[k]+=x
    return out

def run():
    start=time.monotonic()
    data=json.loads(((_J_OUTPUT / 'target_result.json')).read_text(encoding='utf-8'))
    changed=json.loads(((_J_OUTPUT / 'changed_result.json')).read_text(encoding='utf-8'))
    assert data['complete'] and changed['complete']
    table=[[0,0,0] for _ in range(32768)]
    deriv=[{} for _ in range(15)]
    for perm,sign in PERMS:
        counts=[0]*15;fixed=0;degree=0
        for i,j in enumerate(perm):
            if i==j:fixed+=1
            else:
                counts[INDEX[min(i,j),max(i,j)]]+=1
                degree+=int(i<j)
        support=sum((count>0)<<i for i,count in enumerate(counts))
        vals=[sign*math.comb(fixed,d-degree) if 0<=d-degree<=fixed else 0 for d in [5,4,3]]
        for i in range(3):table[support][i]+=vals[i]
        bits=sum((x%2)<<i for i,x in enumerate(vals))
        if bits:
            for j,count in enumerate(counts):
                if count%2:
                    # A permutation uses an off-diagonal variable at most twice.
                    assert count==1
                    s=support^(1<<j)
                    deriv[j][s]=deriv[j].get(s,0)^bits
    for j in range(15):
        bit=1<<j
        for mask in range(32768):
            if mask&bit:
                for k in range(3):table[mask][k]+=table[mask^bit][k]
    matching=[mask for mask,abc in enumerate(table) if [x%2 for x in abc]==[0,1,1]]
    assert len(matching)==375 and matching==[r['upper_mask'] for r in data['forms']]
    residues={};images={}
    for rec in data['forms']:
        mask=rec['upper_mask'];f=table[mask]
        assert f==rec['integer_coefficients']
        cols=[]
        for j in range(15):
            value=0
            for s,c in deriv[j].items():
                if mask&s==s:value ^= c
            cols.append(value)
        assert cols==rec['derivative_columns']
        image={0}
        for c in cols:image |= {x^c for x in tuple(image)}
        assert sorted(image)==rec['image_vectors']==[0,3]
        assert [x%4 for x in f]==[2,3,3]
        rhs=sum((((a-b)//2)%2)<<i for i,(a,b) in enumerate(zip([-2,1,-1],f)))
        assert rhs==rec['right_side'] and rhs not in image
        assert rec['inconsistency_witness']==3 and (rhs&3).bit_count()%2==1
        residues[str(tuple(x%4 for x in f))]=residues.get(str(tuple(x%4 for x in f)),0)+1
        images[str(tuple(sorted(image)))]=images.get(str(tuple(sorted(image))),0)+1
    base=changed['V'];r=changed['R'];ri=changed['R_inverse'];c=changed['C']
    identity=[[int(i==j) for j in range(6)] for i in range(6)]
    assert mm(r,ri)==identity and mm(ri,r)==identity and mm(tr(r),base)==mm(base,r)
    assert mm(tr(c),mm(base,c))==base and mm(c,r)==mm(r,c)
    class_checks=[]
    for model in changed['classifications']:
        b=model['matrix'];checked=0;seen=set()
        for form in model['forms']:
            u=decode(form['upper_rows'])
            masks=[sum((((bb==i)*u[a][j]+(bb==j)*u[i][a])%2)<<(6*a+bb)
                       for a in range(6) for bb in range(6)) for i,j in SELECT]
            for rec in form['bases']:
                key=tuple(rec['Q_rows']);assert key not in seen;seen.add(key)
                q=decode(key);g=mm(tr(q),mm(b,q))
                assert [[x%2 for x in row] for row in g]==u
                e=sum((((g[i][j]-int(i==j))//2)%2)<<k for k,(i,j) in enumerate(SELECT))
                assert e==rec['error_bits']
                z=rec['inconsistency_witness'];lhs=0
                for j,m in enumerate(masks):
                    if z>>j&1:lhs ^= m
                assert lhs==0 and (z&e).bit_count()%2==1
                checked+=1
        assert checked==5625
        class_checks.append({'name':model['name'],'saved_certificates_checked':checked})
    for cost in changed['costs']:
        b=cost['matrix'];a=[[-abs(x) for x in row] for row in b]
        pb=pencil(b);pa=pencil(a)
        assert pb==cost['original_polynomial'] and pa==cost['absolute_polynomial']
        assert poly_mul(pb,pa)==cost['cover_polynomial']
        assert a==cost['absolute_matrix']
        w=cost['literal_cover']
        assert all(w[2*i+s][2*j+z]==(-abs(b[i][j]) if z==(s if b[i][j]<=0 else 1-s) else 0)
                   for i in range(6) for j in range(6) for s in range(2) for z in range(2))
        assert [max(abs(x) for row in m for x in row) for m in [b,a,w]]==cost['heights']
        assert [sum(x*x for row in m for x in row) for m in [b,a,w]]==cost['whole_squared_entry_sums']
        assert sum(abs(x) for x in pa)==cost['absolute_coefficient_l1']
    return {'all_binary_coefficient_triples_rebuilt': 32768, 'target_parity_forms': 375, 'all_derivative_columns_checked': 5625, 'base_residues': residues, 'derivative_images': images, 'allowed_lift_residues': [[2, 3, 3], [0, 1, 3]], 'changed_form_certificates': class_checks, 'full_original_absolute_cover_products_checked': 4, 'literal_cover_entry_definitions_checked': 4, 'method': 'integer permutation determinant monomials, Boolean subset sums, formal derivatives', 'role': 'author self-check, not separate noncontributor review'}

if __name__=='__main__':
    out=run();((_J_OUTPUT / 'verification.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
