"""Reviewer-only D117/J54 verifier; no author implementation is imported.

Full polynomials are recovered from seven scalar integer Bareiss determinants,
not triangular traces or subset determinant DP. Pfaffians use the 6! alternating
sum definition. Coefficients are certified on a signed unisolvent stencil.
All modular survivor sets and the bounded solve use these recovered polynomials.
Draft presence is optional; its bytes are only observed for no-write protection.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product, permutations, combinations
from fractions import Fraction
from math import factorial, isqrt
from time import perf_counter
import json
import sympy as sp

BASE=(_J_PROGRAM / 'review_independent.py').parent
G=[[2,1,1,1,1,1],[1,2,1,-1,-1,1],[1,1,2,1,-1,-1],
   [1,-1,1,2,1,-1],[1,-1,-1,1,2,1],[1,1,-1,-1,1,2]]
Q=[[int(i==j)-int(i==j-1) for j in range(6)] for i in range(6)]
X=sp.symbols('x0:6')
PERMS=[(p,(-1)**sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))) for p in permutations(range(6))]
NATIVE=['readme.md','equations.py','equations.json','residues.py','residues.json',
        'solve_column.py','solve_column.json','two_adic.py','two_adic.json',
        'other_columns.py','other_columns.json','last_column_residues.py',
        'last_column_residues.json','verify.py','verification.json']

def det(A):
    A=[r[:] for r in A]; n=len(A); old=1; sign=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if A[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:A[k],A[pivot]=A[pivot],A[k];sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=A[i][j]*p-A[i][k]*A[k][j]
                assert v%old==0
                A[i][j]=v//old
        for i in range(k+1,n):A[i][k]=0
        old=p
    return sign*A[-1][-1]

def mm(A,B):return [[sum(a*b for a,b in zip(r,c)) for c in zip(*B)] for r in A]
def transpose(A):return [list(r) for r in zip(*A)]
H=mm(mm(transpose(Q),G),Q)

def full_poly(V):
    vals=[det([[t*V[i][j]+V[j][i] for j in range(6)] for i in range(6)]) for t in range(7)]
    # Newton forward differences in the falling-factorial polynomial basis.
    ans=[Fraction(0) for _ in range(7)]; basis=[Fraction(1)]
    dif=vals[:]
    for k in range(7):
        for j,b in enumerate(basis):ans[j]+=Fraction(dif[0],factorial(k))*b
        dif=[b-a for a,b in zip(dif,dif[1:])]
        new=[Fraction(0)]*(len(basis)+1)
        for j,b in enumerate(basis):new[j]-=k*b;new[j+1]+=b
        basis=new
    assert all(a.denominator==1 for a in ans)
    return [int(a) for a in ans]

def wedge_pf(A):
    s=0
    for p,sg in PERMS:s+=sg*A[p[0]][p[1]]*A[p[2]][p[3]]*A[p[4]][p[5]]
    assert s%48==0
    return s//48

def actual(i,c):
    R=[r[:] for r in Q]
    v=[sum(a*b for a,b in zip(row,c)) for row in Q]
    for j in range(6):R[j][i]=v[j]
    assert det(R)==c[i]
    gram=mm(mm(transpose(R),G),R)
    V=[[int(a==b)+(gram[a][b] if a<b else 0) for b in range(6)] for a in range(6)]
    poly=full_poly(V)
    skew=[[V[a][b]-V[b][a] for b in range(6)] for a in range(6)]
    pf=wedge_pf(skew)
    assert det(skew)==pf*pf
    assert poly==poly[::-1] and poly[0]==poly[-1]==1
    assert sum(v*((-1)**j) for j,v in enumerate(poly))==pf*pf
    assert gram[i][i]%2==0
    norm=gram[i][i]//2-1
    if norm==0:
        assert sum(poly)==-1
        assert poly[3]==-3-2*poly[5]-2*poly[4]
        assert pf*pf==5+4*poly[4]
    return (norm,poly[5],pf),poly

def recover(i):
    free=[j for j in range(6) if j!=i]
    def sample(point):
        c=[0]*6;c[i]=1
        for j,v in zip(free,point):c[j]=v
        return actual(i,c)[0]
    zero=[0]*5; base=sample(zero)
    out=[sp.Integer(a) for a in base];lin=[];squares=[]
    for a,j in enumerate(free):
        plus=zero[:];minus=zero[:];plus[a]=1;minus[a]=-1
        f=sample(plus);g=sample(minus)
        l=[sp.Rational(f[k]-g[k],2) for k in range(3)]
        s=[sp.Rational(f[k]+g[k]-2*base[k],2) for k in range(3)]
        for k in range(3):out[k]+=l[k]*X[j]+s[k]*X[j]**2
        lin.append(l);squares.append(s)
    for a,b in combinations(range(5),2):
        point=zero[:];point[a]=point[b]=1;f=sample(point)
        for k in range(3):
            cross=f[k]-base[k]-lin[a][k]-lin[b][k]-squares[a][k]-squares[b][k]
            out[k]+=cross*X[free[a]]*X[free[b]]
    return [sp.expand(e) for e in out]

def compile_int(expr,variables):
    terms=[(powers,int(coeff)) for powers,coeff in sp.Poly(expr,*variables).terms()]
    assert all(coeff==int(coeff) for _,coeff in sp.Poly(expr,*variables).terms())
    def f(point):
        total=0
        for powers,coeff in terms:
            value=coeff
            for x,p in zip(point,powers):value*=x**p
            total+=value
        return total
    return f

def main():
    start=perf_counter();before={name:(((_J_PROGRAM if name in ('equations.py', 'last_column_residues.py', 'other_columns.py', 'readme.md', 'residues.py', 'review_independent.py', 'solve_column.py', 'two_adic.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes() for name in NATIVE}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0117.md')
    fixed=(_J_ROOT / 'mathematics/ledger/Yin_L_G0250_v1.md')
    observed={p:p.read_bytes() for p in (draft,fixed) if p.exists()}
    assert det(G)==-1 and det(Q)==1
    C=[[G[i][j]-2*int(i==j) for j in range(6)] for i in range(6)]
    assert mm(C,C)==[[5*int(i==j) for j in range(6)] for i in range(6)]
    data=json.loads(before['equations.json'])
    assert data['passed'] and data['gram_path']==H
    rows=data['columns']+json.loads(before['other_columns.json'])['columns']
    recovered={};cases={};expression_checks=0
    for row in rows:
        i=row['column'];n,a,p=recover(i);recovered[i]=(n,a,p)
        for value,key in zip((n,a,p),('norm_equation','first_coefficient','pfaffian')):
            assert sp.expand(value-sp.sympify(row[key]))==0
            expression_checks+=1
        for case in row['cases']:
            var=sp.Symbol(case['eliminate']);repl=sp.sympify(case['replacement']);sg=case['pfaffian']
            assert sp.expand(p.subs(var,repl)-sg)==0
            nn=sp.expand(n.subs(var,repl));aa=sp.expand((a+2).subs(var,repl))
            for value,key in ((nn,'norm_equation'),(aa,'coefficient_equation'),(aa-nn,'difference')):
                assert sp.expand(value-sp.sympify(case[key]))==0
                expression_checks+=1
            cases[(i,sg)]=(nn,aa)
    # Independently verify the author's 84 separately claimed sample checks/count24.
    pts=[[0]*5]
    for a in range(5):
        for v in (1,2):p=[0]*5;p[a]=v;pts.append(p)
    for a,b in combinations(range(5),2):p=[0]*5;p[a]=p[b]=1;pts.append(p)
    norm_count=0
    for i in (1,2,3,4):
        free=[j for j in range(6) if j!=i]
        fs=[compile_int(e,[X[j] for j in free]) for e in recovered[i]]
        for point in pts:
            c=[0]*6;c[i]=1
            for j,v in zip(free,point):c[j]=v
            val,poly=actual(i,c)
            assert list(val)==[f(point) for f in fs]
            norm_count+=val[0]==0
    author_ver=json.loads(before['verification.json'])
    assert norm_count==author_ver['norm_two_endpoint_checks']==24
    assert author_ver['direct_full_polynomial_checks']==84
    assert author_ver['quadratic_interpolation_points_per_column']==21
    assert author_ver['columns']==[1,2,3,4] and author_ver['passed']
    # Complete residue survivor sets, deriving values from the recovered identities.
    totals={};survivor_counts=[]
    for name,key in [('residues.json','declared_total_tuple_cap'),('two_adic.json','declared_residue_cap'),('last_column_residues.json','declared_residue_cap')]:
        saved=json.loads(before[name]);total=0
        for row in saved['systems']:
            nn,aa=cases[(row['column'],row['pfaffian'])]
            vs=sorted(nn.free_symbols|aa.free_symbols,key=str)
            assert len(vs)==4
            if 'variables' in row:assert row['variables']==[str(v) for v in vs]
            fn=compile_int(nn,vs);fa=compile_int(aa,vs);m=row['modulus']
            good=[list(p) for p in product(range(m),repeat=4) if fn(p)%m==0 and fa(p)%m==0]
            assert good==row['survivors'] and len(good)==row['survivor_count']
            assert row['tuples']==m**4
            total+=m**4;survivor_counts.append([row['column'],row['pfaffian'],m,len(good)])
        assert total==saved['total_tuples']==saved[key] and saved['passed']
        totals[name]=total
    # Every printed generic equation and all singular-lift claims, derived anew.
    x,b,v,w,y,z,c,d,k=sp.symbols('x b v w y z c d k')
    N2=x*x-x*b+b*b+6*b*v+4*b*w-(2*k+1)*b+7*v*v+12*v*w-(5*k+5)*v+4*w*w-(4*k+3)*w+k*k+k
    R2=(4*b+4*v+8*w-2*k-4)*x-4*b*b-8*b*v-16*b*w+(4*k+6)*b-11*v*v-28*v*w+(9*k+5)*v-20*w*w+(12*k+11)*w-2*k*k-2*k-3
    D3=x*x+4*x*y+y*y-k*x-(k+1)*y+k-3
    N3=21*x*x+4*x*y-10*x*v+10*x*z-(9*k+10)*x+y*y-(k+1)*y+v*v+(2*k+3)*v-3*v*z+z*z-(2*k+2)*z+k*k+2*k
    N4=x*x-x*b+b*b+3*b*c-2*b*d-(2*k+2)*b+c*c-3*c*d-(2*k+2)*c+d*d+(2*k+3)*d+k*k+k
    A4=-3*x*x+2*x*b+x*c+x*d-x-3*b*b-8*b*c+7*b*d+(6*k+4)*b-5*c*c+10*c*d+(8*k+5)*c-5*d*d-(8*k+5)*d-4*k*k-3
    printed=[(2,N2,R2,{X[0]:x,X[1]:b,X[4]:v,X[5]:w},3),
             (3,N3,D3,{X[0]:x,X[2]:y+2*v,X[4]:v,X[5]:z},-1),
             (4,N4,A4,{X[0]:x,X[1]:b,X[2]:c,X[3]:d},0)]
    for kv in (1,4):
        sg=5-2*kv
        for i,nn,bb,sub,mul in printed:
            cn,ca=cases[(i,sg)]
            assert sp.expand(nn.subs(k,kv)-cn.subs(sub))==0
            assert sp.expand(bb.subs(k,kv)-(ca+mul*cn).subs(sub))==0
        # Verify gradients at every relevant class and all small lifting residues.
        for point in product(range(2),repeat=4):
            sub=dict(zip((x,b,v,w),point));sub[k]=kv
            nv=int(N2.subs(sub));rv=int(R2.subs(sub))
            if nv%2==rv%2==0:
                assert point[0]==1 and point[1]==0 and (kv*point[2]+point[3])%2==1
                assert all(int(sp.diff(R2-N2,j).subs(sub))%2==0 for j in (x,b,v,w))
                assert (rv-nv)%4==2
        for point in product(range(3),repeat=4):
            sub=dict(zip((x,y,v,z),point));sub[k]=kv
            if int(D3.subs(sub))%3==int(N3.subs(sub))%3==0:
                assert all(int(sp.diff(e,j).subs(sub))%3==0 for e in (D3,N3) for j in (x,y,v,z))
                assert not (int(D3.subs(sub))%9==0 and int(N3.subs(sub))%9==0)
        sub={x:1,b:0,c:1,d:0,k:kv}
        assert int(A4.subs(sub))%4==2
        assert all(int(sp.diff(A4,j).subs(sub))%2==0 for j in (x,b,c,d))
    # Bounded control: solve norm quadratic FIRST, then test R, distinct from
    # the author's primary linear-elimination procedure. Count side categories.
    bound=json.loads(before['solve_column.json'])['declared_bound'];assert bound==20
    total=singular=integral=targets=0
    for kv in (1,4):
        norm=sp.Poly(N2.subs(k,kv),x);rr=sp.Poly(R2.subs(k,kv),x)
        nf=[compile_int(norm.coeff_monomial(x**i),(b,v,w)) for i in range(2)]
        rf=[compile_int(rr.coeff_monomial(x**i),(b,v,w)) for i in range(2)]
        assert norm.coeff_monomial(x*x)==1
        for point in product(range(-bound,bound+1),repeat=3):
            total+=1;const,lin=nf[0](point),nf[1](point);rc,rl=rf[0](point),rf[1](point)
            singular+=rl==0;integral+=rl!=0 and (-rc)%rl==0
            disc=lin*lin-4*const
            if disc<0:continue
            root=isqrt(disc)
            if root*root!=disc:continue
            for num in {-lin-root,-lin+root}:
                if num%2==0 and rl*(num//2)+rc==0:targets+=1
    saved=json.loads(before['solve_column.json'])
    assert total==saved['triples_tested']==saved['declared_triple_cap']==137842
    assert singular==saved['singular_linear_cases']==838
    assert integral==saved['nonsingular_integral_x0_cases']==2953
    assert targets==saved['target_count']==0 and saved['all_targets']==[] and saved['passed']
    # Independently enumerate all F2 classes; canonical eight-vertex edge form.
    binary=[];phi7=[1]*7;target=[1,0,1,1,1,0,1]
    for i in range(6):
        count=0;parts={};polys={}
        for coeff in product(range(2),repeat=6):
            quad=sum(coeff[a]*H[a][b]*coeff[b] for a in range(6) for b in range(6))//2
            if coeff[i]!=1 or quad%2!=1:continue
            edge=0
            for j,a in enumerate(coeff):
                if a:edge^=(1<<j)|(1<<(j+1))
            if edge.bit_count()==6:edge^=255
            assert edge.bit_count()==2
            edges=[(j,j+1) for j in range(6) if j!=i]
            ends=[j for j in range(8) if edge>>j&1];edges.append(tuple(ends))
            parent=list(range(8))
            def find(a):
                while parent[a]!=a:a=parent[a]
                return a
            for a,b0 in edges:
                ra,rb=find(a),find(b0);assert ra!=rb;parent[ra]=rb
            sizes=sorted(sum(find(v0)==r for v0 in range(8)) for r in {find(v0) for v0 in range(8)})
            assert len(sizes)==2 and all(n%2 for n in sizes)
            _,poly=actual(i,list(coeff));mp=tuple(v0%2 for v0 in poly)
            if sizes==[1,7]:assert list(mp)==phi7
            else:assert sizes==[3,5] and list(mp)==target
            if i in (0,5):assert sizes==[1,7]
            count+=1;parts[str(sizes)]=parts.get(str(sizes),0)+1;polys[str(list(mp))]=polys.get(str(list(mp)),0)+1
        binary.append({'column':i,'admissible_quadratic_classes':count,'partitions':parts,'polynomials_mod2':polys})
    assert all((((_J_PROGRAM if n in ('equations.py', 'last_column_residues.py', 'other_columns.py', 'readme.md', 'residues.py', 'review_independent.py', 'solve_column.py', 'two_adic.py', 'verify.py') else _J_OUTPUT) / n)).read_bytes()==v0 for n,v0 in before.items())
    assert all(p.read_bytes()==b for p,b in observed.items())
    result={'passed': True, 'implementation': 'Integer Bareiss at seven t values plus rational Newton interpolation; 6! wedge Pfaffian; signed multivariate unisolvent stencil; no author imports', 'recovered_columns': [1, 2, 3, 4], 'signed_unisolvent_points_per_column': 21, 'independent_full_polynomials_for_identity_recovery': 84, 'independent_scalar_determinants_for_identity_recovery': 588, 'author_sample_rechecked_full_polynomials': 84, 'author_sample_norm2_count': norm_count, 'saved_expression_identities': expression_checks, 'residue_totals': totals, 'complete_survivor_counts': survivor_counts, 'printed_equations_and_singular_lift_checks': True, 'bounded_quadratic_first_solve': {'triples': total, 'singular_linear_cases': singular, 'nonsingular_integral_x0_cases': integral, 'target_count': targets}, 'binary_all_class_checks': binary}
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
