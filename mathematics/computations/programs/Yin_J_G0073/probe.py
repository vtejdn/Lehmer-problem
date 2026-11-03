"""Declared finite actual b=d+2 profile test; see readme.md and D161."""
from __future__ import annotations
import itertools
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import time
import sympy as sp


def run():
    start = time.perf_counter()
    x = sp.Symbol('x')
    records, excluded, failures = [], [], []
    endpoints = 0
    for d in range(2, 6):
        for const in (-1, 1):
            for middle in itertools.product((-1, 0, 1), repeat=d-1):
                coeff = [const, *middle, 1]
                p = sp.Poly(sum(c*x**i for i, c in enumerate(coeff)), x, domain=sp.QQ)
                if not p.is_irreducible:
                    excluded.append(coeff)
                    continue
                b = d+2
                cols = []
                for j in range(b):
                    rem = sp.rem(sp.Poly(x**j, x), p)
                    cols.append(tuple(int(rem.nth(i)) for i in range(d)))
                counts = {(0,)*d: 1}
                for col in cols:
                    nxt = {}
                    for z, count in counts.items():
                        for digit, weight in ((-1, 1), (0, 2), (1, 1)):
                            zz = tuple(a+digit*c for a, c in zip(z, col))
                            nxt[zz] = nxt.get(zz, 0)+weight*count
                    counts = nxt
                assert sum(counts.values()) == 4**b
                assert all(counts[tuple(-v for v in z)] == c for z, c in counts.items())
                mat = sp.Matrix.hstack(*(sp.Matrix(col) for col in cols))
                q = mat*mat.T
                determinant = int(q.det())
                assert determinant > 0
                adj = [[int(v) for v in row] for row in q.adjugate().tolist()]
                zero_count = counts[(0,)*d]
                payload = []
                local_failures = []
                from math import gcd
                for z, count in sorted(counts.items()):
                    num = sum(z[i]*adj[i][j]*z[j] for i in range(d) for j in range(d))
                    common = gcd(num, determinant)
                    a, den = num//common, determinant//common
                    passed = pow(count, den)*pow(2, a) <= pow(zero_count, den)
                    payload.append([list(z), count, a, den, passed])
                    if not passed:
                        fail = dict(coefficients=coeff, endpoint=list(z), count=count,
                                    zero_count=zero_count, energy=[a, den])
                        local_failures.append(fail)
                        failures.append(fail)
                kernel = sp.Matrix.hstack(sp.Matrix(coeff+[0]), sp.Matrix([0]+coeff))
                assert mat*kernel == sp.zeros(d, 2)
                overlap = [i for i in range(b) if kernel[i, 0] and kernel[i, 1]]
                records.append(dict(coefficients=coeff, degree=d, length=b,
                                    columns=[list(c) for c in cols],
                                    covariance_gram=[[int(v) for v in row] for row in q.tolist()],
                                    determinant=determinant, relation_overlap=overlap,
                                    zero_count=zero_count, distribution=payload,
                                    failure_count=len(local_failures)))
                endpoints += len(payload)
                if time.perf_counter()-start > 120:
                    raise TimeoutError('Declared aggregate 120-second cap exceeded; no complete output published')
    return dict(scope=dict(degrees=[2, 3, 4, 5], constants=[-1, 1], middle=[-1, 0, 1], monic=True, irreducible_over='QQ', length='d+2', original_numerator_weights=[1, 2, 1]), records=records, excluded_reducible=excluded, failures=failures, polynomial_count=len(records), endpoint_count=endpoints, total_box_count=len(records) + len(excluded), universal_profile_proved=False)


if __name__ == '__main__':
    result = run()
    (_J_OUTPUT / 'result.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('polynomial_count', 'endpoint_count', 'total_box_count')}))
    print('failures', len(result['failures']))
    print(json.dumps(result['failures'][:2]))
