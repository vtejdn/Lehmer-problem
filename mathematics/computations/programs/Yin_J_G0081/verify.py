"""J81: exact five-pair sparse-diamond controls; no search, 120s cap."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import time

import sympy as sp


T = sp.Symbol('t')
KS = list(range(2, 7))
CAP_SECONDS = 120


def coeffs(p):
    return [int(x) for x in reversed(sp.Poly(p, T).all_coeffs())]


def connected(k):
    v = sp.eye(3*k+1)
    for i in range(k):
        a, b, c, an = 3*i, 3*i+1, 3*i+2, 3*i+3
        v[a,b] = v[a,c] = v[b,an] = -1
        v[c,an] = 1
    v[0,3*k] = -1
    return v


def disconnected(k):
    blocks = [sp.Matrix([[1,-2],[0,1]]) for _ in range(k)]
    blocks += [sp.Matrix([[1,-1],[0,1]]), sp.eye(k-1)]
    return sp.diag(*blocks)


def absolute(v):
    n = v.rows
    return sp.Matrix(n,n,lambda i,j: 1 if i==j else -abs(v[i,j]) if i<j else 0)


def cover(v):
    n = v.rows
    w = sp.eye(2*n)
    for i in range(n):
        for j in range(i+1,n):
            a = int(v[i,j])
            if a <= 0:
                w[2*i,2*j] = w[2*i+1,2*j+1] = a
            else:
                w[2*i,2*j+1] = w[2*i+1,2*j] = -a
    return w


def inverse_unitriangular(v):
    n = v.rows
    u = sp.eye(n)
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            u[i,j] = -sum(v[i,h]*u[h,j] for h in range(i+1,j+1))
    assert v*u == sp.eye(n) and u*v == sp.eye(n)
    return u


def matrix_record(v, start):
    assert time.perf_counter()-start < CAP_SECONDS
    n = v.rows
    assert v.cols == n
    assert all(v[i,i] == 1 for i in range(n))
    assert all(v[i,j] == 0 for i in range(n) for j in range(i))
    c = -inverse_unitriangular(v)*v.T
    p = sp.Poly(c.charpoly(T).as_expr(), T)
    ascending = coeffs(p)
    assert ascending[0] == ascending[-1] == 1 and ascending == ascending[::-1]
    content, factors = sp.factor_list(p)
    assert content == 1
    rebuilt = sp.Poly(1,T)
    for f, exponent in factors:
        rebuilt *= f**exponent
    assert rebuilt == p
    energy = int(sum(v[i,j]**2 for i in range(n) for j in range(i+1,n)))
    r = {
        'matrix': [[int(x) for x in row] for row in v.tolist()],
        'dimension': n,
        'height': max(abs(int(x)) for x in v),
        'energy': energy,
        'total_square_sum': n+energy,
        'monodromy_trace': int(sp.trace(c)),
        'polynomial': ascending,
        'integer_factors': [
            {'polynomial': coeffs(f), 'multiplicity': int(exponent)}
            for f, exponent in factors
        ],
    }
    assert r['monodromy_trace'] == -ascending[-2]
    return r,p


def residual(k):
    q,d,e = T+1,T*T+1,(T-1)**2
    fs = {-1:sp.Poly(0,T),0:sp.Poly(1,T),1:sp.Poly(e,T)}
    for j in range(2,k):
        fs[j] = sp.Poly(e,T)*fs[j-1]-sp.Poly(4*T*T,T)*fs[j-2]
    dk = (sp.Poly(d*d-T*q*q,T)*fs[k-1]
          -sp.Poly(8*d*T*T,T)*fs[k-2]
          +sp.Poly(16*T**4,T)*fs[k-3]
          -sp.Poly(2**k*q*(T**(2*k)+T),T))
    return dk,fs


def run():
    start = time.perf_counter()
    rows = []
    for k in KS:
        n = 3*k+1
        dk,fs = residual(k)
        target = sp.Poly((T+1)**(k-1)*(T-1)**(2*k)*(T*T+T+1),T)
        companion = sp.Poly((T+1)**(k-1),T)*dk
        v,z = connected(k),disconnected(k)
        records = {}
        for name,x,expected in [
            ('connected_original',v,target),
            ('connected_absolute',absolute(v),companion),
            ('connected_cover',cover(v),target*companion),
            ('disconnected_original',z,target),
            ('disconnected_absolute',absolute(z),target),
            ('disconnected_cover',cover(z),target*target),
        ]:
            rec,p = matrix_record(x,start)
            assert p == expected, (k,name,coeffs(p),coeffs(expected))
            is_cover = name.endswith('_cover')
            scale = 2 if is_cover else 1
            assert rec['dimension'] == scale*n
            assert rec['energy'] == scale*(4*k+1)
            assert rec['total_square_sum'] == scale*(7*k+2)
            assert rec['height'] == (1 if name.startswith('connected_') else 2)
            records[name] = rec
        nk = sp.eye(n)-absolute(v)
        power = sp.eye(n)
        paths = []
        for j in range(1,n):
            power = power*nk
            val = int(sp.trace(power*nk.T))
            assert val == (4*k+1 if j==1 else 2**k if j==2*k else 0)
            paths.append(val)
        assert records['connected_absolute']['monodromy_trace'] == k+2**k
        rows.append({
            'k': k,
            'target': coeffs(target),
            'residual_D': coeffs(dk),
            'continuants': {str(j):coeffs(f) for j,f in fs.items()},
            'path_terms_j1_to_nminus1': paths,
            'reciprocal_epsilon': n%2,
            'twice_cosh_lower_bound': 2**k-2*k+1+2*(n%2),
            'exp_measure_lower_bound': max(1,2**k-2*k),
            'records': records,
        })
    elapsed = time.perf_counter()-start
    assert elapsed < CAP_SECONDS
    return {'scope': {'k_values': KS, 'paired_controls': 5, 'complete_polynomials': 30, 'search': False, 'coefficient_order': 'ascending', 'arithmetic': 'exact integer'}, 'controls': rows, 'success': True}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=(_J_OUTPUT / 'result.json'))
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'success':True,'controls':len(result['controls']),
                      'polynomials':30}))
