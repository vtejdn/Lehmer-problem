"""Declared fifteen-input exact residual-coherence discriminator; no search."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time
import sympy as sp

HOME = (_J_PROGRAM / 'author.py').parent
START = time.monotonic()
CAP = 120
t = sp.Symbol('t')
lehmer = t**10+t**9-t**7-t**6-t**5-t**4-t**3+t+1
inputs = [
    ('quadratic', t**2-3*t+1, 'actual'),
    ('quartic', t**4-t**3-t**2-t+1, 'actual'),
    ('sextic', t**6-t**5-t**3-t+1, 'actual'),
    ('lehmer', lehmer, 'actual'),
    ('lehmer_square', lehmer.subs(t,t**2), 'actual'),
    ('lehmer_fourth', lehmer.subs(t,t**4), 'actual'),
]
inputs += [(f'cyclotomic_{p}', sum(t**j for j in range(p)), 'calibration')
           for p in (3,5,7,11,17)]
inputs += [(f'repeated_{d}', (t-1)**d, 'calibration') for d in (2,4,8,12)]
log2lo = 2*sum(sp.Rational(1, 3**(2*k+1)*(2*k+1)) for k in range(20))
log2hi = log2lo + 2*sp.Rational(1,3**41*41)/(1-sp.Rational(1,9))
records=[]
summary={'log2_interval': [str(log2lo), str(log2hi)], 'records': records}

def save():
    pass
    ((_J_OUTPUT / 'author-output.json')).write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')

for name,expr,scope in inputs:
    if time.monotonic()-START>=CAP:
        summary['status']='cap-stopped'; save(); raise SystemExit('cap reached')
    p=sp.Poly(expr,t)
    d=p.degree(); N=2*d
    coeff=[int(p.nth(j)) for j in range(d+1)]
    A=sp.zeros(N,N-d)
    for j in range(N-d):
        for h,value in enumerate(coeff): A[j+h,j]=value
    G=A.T*A
    Y=G.inv()*A.T
    R=sp.eye(N)-A*Y
    q=sp.ilcm(*[v.q for v in R],*[v.q for v in Y])
    C=(q*R).applyfunc(int); U=(q*Y).applyfunc(int)
    assert C+A*U==q*sp.eye(N)
    assert C.T==C and C*C==q*C and sp.trace(C)==q*d
    a=[sum(R[j,j+h] for j in range(N-h)) for h in range(1,N)]
    kap=2*sum(abs(v) for v in a)/d
    if kap<=1+log2lo: logtest='true-certified'
    elif kap>1+log2hi: logtest='false-certified'
    else: logtest='undecided-at-declared-precision'
    rec={'name': name, 'scope': scope, 'coefficients_ascending': coeff, 'd': d, 'N': N, 'q': str(q), 'C_rows': [[str(C[i, j]) for j in range(N)] for i in range(N)], 'U_rows': [[str(U[i, j]) for j in range(N)] for i in range(N - d)], 'signed_diagonal_sums': [str(v) for v in a], 'kappa': str(kap), 'endpoint_diagonals': [str(R[0, 0]), str(R[N - 1, N - 1])], 'kappa_le_2': bool(kap <= 2), 'kappa_le_1_plus_log2': logtest, 'identity_checks': ['C+A*U=qI', 'C.T=C', 'C*C=qC', 'trace(C)=qd']}
    records.append(rec);save()
    print(name,d,str(kap),bool(kap<=2),logtest,flush=True)
summary['status']='complete';save()
