from fractions import Fraction
from math import comb
import json, sys

def det(a):
    a = [list(row) for row in a]
    n = len(a)
    if n == 0: return 1
    sign, old = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            j = next((j for j in range(k+1,n) if a[j][k]), None)
            if j is None: return 0
            a[k], a[j] = a[j], a[k]; sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = a[i][j]*pivot-a[i][k]*a[k][j]
                assert num % old == 0
                a[i][j] = num//old
        for i in range(k+1,n): a[i][k] = 0
        old = pivot
    return sign*a[-1][-1]

def resultant(f,g):
    m,n = len(f)-1,len(g)-1
    f,g = f[::-1],g[::-1]
    a = [[0]*(m+n) for _ in range(m+n)]
    for i in range(n): a[i][i:i+m+1]=f
    for i in range(m): a[n+i][i:i+n+1]=g
    return det(a)

def disc(p):
    d=len(p)-1
    return abs(resultant(p,[i*p[i] for i in range(1,d+1)]))

def gram(p,N):
    d=len(p)-1
    assert p[-1]==1 and N>=d
    v=[1]+[0]*(d-1)
    W=[[0]*d for _ in range(d)]
    for _ in range(N):
        for i in range(d):
            for j in range(d): W[i][j]+=v[i]*v[j]
        lead=v[-1]
        v=[-lead*p[0]]+[v[i-1]-lead*p[i] for i in range(1,d)]
    return det(W)

def relation_gram(p,k):
    d=len(p)-1
    K=[[p[i-j] if 0<=i-j<=d else 0 for j in range(k)]
       for i in range(k+d)]
    return det([[sum(K[r][i]*K[r][j] for r in range(k+d))
                 for j in range(k)] for i in range(k)])

def dilate(p,r):
    q=[0]*((len(p)-1)*r+1)
    for i,a in enumerate(p): q[i*r]=a
    return q

inputs={
    'lehmer':[1,1,0,-1,-1,-1,-1,-1,0,1,1],
    'reciprocal_quadratic':[1,-3,1],
    'cyclotomic_3':[1,1,1],
    'cyclotomic_5':[1,1,1,1,1],
    'cyclotomic_7':[1,1,1,1,1,1,1],
    'nonunit_t5_minus2':[-2,0,0,0,0,1],
}
out={'python':sys.version.split()[0],'cases':{}}
for name,p in inputs.items():
    d=len(p)-1; delta=disc(p)
    assert delta>0
    for k in range(0,9): assert gram(p,d+k)==relation_gram(p,k)
    rows=[]
    for mult in [1,2,4,8,16,32]:
        N=d*mult; G=gram(p,N); X=delta*G
        rows.append({'N':N,'gram':G,'positive_certificate':X>N**d,
                     'log2_over8_certificate':X**4>=N**(4*d)*2**(N-1)})
    out['cases'][name]={'coefficients_ascending':p,'degree':d,
                        'discriminant_abs':delta,'windows':rows}
for ell in [3,5,7]:
    p=[1]*ell; d=ell-1
    for N in [ell,2*ell,3*ell]: assert disc(p)*gram(p,N)==N**d
q=inputs['reciprocal_quadratic']
for r in [2,3,5]:
    p=dilate(q,r); d=len(p)-1
    assert disc(p)==r**d*disc(q)**r
    for L in [2,3,4,8]: assert gram(p,r*L)==gram(q,L)**r
out['identity_checks']='passed: dual Gram, prime-cyclotomic equality, dilation'
print(json.dumps(out,indent=2))
