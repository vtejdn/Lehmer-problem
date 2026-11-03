"""Author exact self-check by integer polynomial determinants and interpolation.

This does not import the symbolic equation generator. It is a separate
calculation by the author, not an independent noncontributor review.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import combinations
import json
import sympy as s
BASE=(_J_PROGRAM / 'verify.py').parent
G0=[[2,1,1,1,1,1],[1,2,1,-1,-1,1],[1,1,2,1,-1,-1],
    [1,-1,1,2,1,-1],[1,-1,-1,1,2,1],[1,1,-1,-1,1,2]]
Q0=[[int(i==j)-int(i==j-1) for j in range(6)] for i in range(6)]

def mul(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def tr(A):return list(map(list,zip(*A)))

def polynomial(V):
    dp={0:[1]};n=len(V)
    for mask in range(1<<n):
        if mask not in dp:continue
        i=mask.bit_count()
        if i==n:continue
        for j in range(n):
            if mask>>j&1:continue
            sg=(-1)**(i-(mask&((1<<j)-1)).bit_count())
            coeff=(V[j][i],V[i][j])
            nxt=mask|1<<j
            dest=dp.setdefault(nxt,[0]*(i+2))
            for k,a in enumerate(dp[mask]):
                for d,b in enumerate(coeff):dest[k+d]+=sg*a*b
    return dp[(1<<n)-1]

def pf(A):
    if not A:return 1
    total=0
    for j in range(1,len(A)):
        remain=[a for a in range(len(A)) if a not in (0,j)]
        total+=(-1)**(j+1)*A[0][j]*pf([[A[a][b] for b in remain] for a in remain])
    return total

def main():
    data=json.loads(((_J_OUTPUT / 'equations.json')).read_text(encoding='utf-8'))['columns']
    data+=json.loads(((_J_OUTPUT / 'other_columns.json')).read_text(encoding='utf-8'))['columns']
    points=[];n=5
    points.append([0]*n)
    for i in range(n):
        for k in (1,2):
            p=[0]*n;p[i]=k;points.append(p)
    for i,j in combinations(range(n),2):
        p=[0]*n;p[i]=p[j]=1;points.append(p)
    assert len(points)==21
    checked=0;norm_two_samples=0
    for row in data:
        i=row['column'];free=[j for j in range(6) if j!=i]
        expressions=[s.sympify(row[k]) for k in ('norm_equation','first_coefficient','pfaffian')]
        for point in points:
            c=[0]*6;c[i]=1
            for j,a in zip(free,point):c[j]=a
            r=[sum(a*b for a,b in zip(q,c)) for q in Q0]
            Q=[list(q) for q in Q0]
            for j in range(6):Q[j][i]=r[j]
            G=mul(mul(tr(Q),G0),Q)
            V=[[int(a==b)+(G[a][b] if a<b else 0) for b in range(6)] for a in range(6)]
            p=polynomial(V)
            f=pf([[V[a][b]-V[b][a] for b in range(6)] for a in range(6)])
            actual=[G[i][i]//2-1,p[5],f]
            substitution={s.Symbol('x'+str(j)):c[j] for j in range(6)}
            expected=[int(e.subs(substitution)) for e in expressions]
            assert actual==expected,(i,c,actual,expected)
            assert p==p[::-1] and p[0]==p[-1]==1
            assert sum((-1)**j*a for j,a in enumerate(p))==f*f
            if G[i][i]==2:
                norm_two_samples+=1
                assert sum(p)==-1
                assert p[3]==-3-2*p[5]-2*p[4]
                assert f*f==5+4*p[4]
            checked+=1
    # Check every printed general position4 formula, separately from code generation.
    x,b,c,d,k=s.symbols('x b c d k')
    N=x*x-x*b+b*b+3*b*c-2*b*d-(2*k+2)*b+c*c-3*c*d-(2*k+2)*c+d*d+(2*k+3)*d+k*k+k
    A=-3*x*x+2*x*b+x*c+x*d-x-3*b*b-8*b*c+7*b*d+(6*k+4)*b-5*c*c+10*c*d+(8*k+5)*c-5*d*d-(8*k+5)*d-4*k*k-3
    position4=next(row for row in data if row['column']==4)
    for case in position4['cases']:
        kv=(5-case['pfaffian'])//2
        sub={s.Symbol('x0'):x,s.Symbol('x1'):b,s.Symbol('x2'):c,s.Symbol('x3'):d}
        assert s.expand(N.subs(k,kv)-s.sympify(case['norm_equation']).subs(sub))==0
        assert s.expand(A.subs(k,kv)-s.sympify(case['coefficient_equation']).subs(sub))==0
        assert int(A.subs({x:1,b:0,c:1,d:0,k:kv}))%4==2
        for variable in (x,b,c,d):assert int(s.diff(A,variable).subs({x:1,b:0,c:1,d:0,k:kv}))%2==0
    result={'passed':True,'columns':[1,2,3,4],'quadratic_interpolation_points_per_column':21,
            'direct_full_polynomial_checks':checked,'norm_two_endpoint_checks':norm_two_samples,
            'printed_position4_formulas_and_mod4_gradient_checked':True,
            'mathematical_scope':'all printed coefficients are degree at most two; 21 unisolvent points determine each in five variables'}
    assert checked==84
    ((_J_OUTPUT / 'verification.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':main()
