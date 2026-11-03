"""Declared complete constraint Jacobians and coherent lifts at p=2,3 only."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json,time
import sympy as sp

V=sp.Matrix([[0,-1,-2,0,-1,0],[1,0,-1,1,0,1],[2,1,0,2,1,1],
             [0,-1,-1,0,-1,0],[1,-1,-1,1,0,1],[1,-1,-1,0,-1,0]])
LOWER=[(i,j) for i in range(6) for j in range(i)]
DIAG=[(i,i) for i in range(5)]
POSITIONS=LOWER+DIAG
T=sp.Symbol('t')
F=[1,-2,1,-1,1,-2,1]
def array(a):return [[int(v) for v in row] for row in a.tolist()]
def reduce(a,m):return a.applyfunc(lambda x:int(x)%m)
def equations(q):
    b=q.T*V*q
    return [int(q.det())-1]+[int(b[i,j])-int(i==j) for i,j in POSITIONS]
def jacobian(b,p):
    cols=[]
    for i in range(6):
        for j in range(6):
            x=sp.zeros(6);x[i,j]=1;d=x.T*b+b*x
            cols.append([int(i==j)]+[int(d[a,c])%p for a,c in POSITIONS])
    return [list(row) for row in zip(*cols)]
def rref(a,p):
    a=[[v%p for v in row] for row in a];piv=[];r=0
    for c in range(len(a[0])):
        pos=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pos is None:continue
        a[r],a[pos]=a[pos],a[r];s=pow(a[r][c],-1,p)
        a[r]=[v*s%p for v in a[r]]
        for i in range(len(a)):
            if i!=r:
                s=a[i][c];a[i]=[(v-s*w)%p for v,w in zip(a[i],a[r])]
        piv.append(c);r+=1
        if r==len(a):break
    return a,piv
def solve(a,b,p):
    z,piv=rref([row+[v] for row,v in zip(a,b)],p)
    assert len(piv)==len(a) and max(piv)<len(a[0])
    x=[0]*len(a[0])
    for i,c in enumerate(piv):x[c]=z[i][-1]
    assert all(sum(u*v for u,v in zip(row,x))%p==b0%p for row,b0 in zip(a,b))
    return x
def verify(q,modulus):
    assert all(v%modulus==0 for v in equations(q))
    b=reduce(q.T*V*q,modulus)
    assert all(b[i,i]==1 for i in range(6))
    assert all(b[i,j]==0 for i,j in LOWER)
    coeff=[int(c)%modulus for c in sp.Poly((T*b+b.T).det(method='domain-ge'),T).all_coeffs()][::-1]
    assert coeff==[a%modulus for a in F]
    return dict(basis=array(q),determinant_modulus=int(q.det())%modulus,
                transformed_matrix=array(b),full_original_polynomial_modulus=coeff,
                integer_representative_determinant=int(q.det()))
def run():
    start=time.perf_counter();src=(_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0060/congruence_result.json')
    data=json.loads(src.read_text(encoding='utf8'));out=[]
    assert V.det()==1
    assert [int(c) for c in sp.Poly((T*V+V.T).det(method='domain-ge'),T).all_coeffs()][::-1]==F
    for old in data['field_tests']:
        p=old['prime'];assert p in (2,3);q=sp.Matrix(old['basis']);rawdet=int(q.det())%p
        flip=rawdet==p-1 and p!=2
        if flip:q[:,5]=-q[:,5]
        q=reduce(q,p);assert int(q.det())%p==1
        initial=verify(q,p);b=reduce(q.T*V*q,p);a=jacobian(b,p);rr,piv=rref(a,p)
        row=dict(prime=p,original_basis_determinant_modp=rawdet,last_column_sign_changed=flip,
                 initial=initial,jacobian=a,rank=len(piv),pivot_columns=piv,steps=[])
        if len(piv)!=21:
            row['stop_reason']='derivative_not_surjective';out.append(row);continue
        minor=sp.Matrix([[r[c] for c in piv] for r in a]);det=int(minor.det(method='domain-ge'))
        assert det%p!=0;row['maximal_minor_integer_determinant']=det
        m=p
        for exponent in range(2,5):
            assert time.perf_counter()-start<120
            err=equations(q);assert all(v%m==0 for v in err)
            rhs=[-(v//m)%p for v in err];flat=solve(a,rhs,p);x=sp.Matrix(6,6,flat)
            oldq=q;q=reduce(q*(sp.eye(6)+m*x),m*p)
            assert reduce(q,p)==reduce(oldq,p) and reduce(q,m)==oldq
            step=dict(exponent=exponent,modulus=m*p,error_quotient_modp=[(v//m)%p for v in err],
                      correction_matrix=array(x),**verify(q,m*p))
            row['steps'].append(step);m*=p
        row['stop_reason']='declared_p4_completed';out.append(row)
    return dict(scope=dict(primes=[2, 3], maximum_exponent=4, variables=36, equations=21, equation_order=['determinant'] + POSITIONS), initial_matrix=array(V), full_original_polynomial=F, tests=out)
if __name__=='__main__':
    out=run();(_J_OUTPUT / 'lift_result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
    print(json.dumps([{k:v for k,v in row.items() if k in ['prime','rank','stop_reason','maximal_minor_integer_determinant']} for row in out['tests']]))
