"""Exact replay of the retained n18 joint-budget selection, without a solver."""
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUT = HERE / 'inputs/joint-budget-n18.json'


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def pair(value):
    value = F(value)
    return [value.numerator, value.denominator]


def vec(values):
    return [pair(value) for value in values]


def solve(rows, rhs):
    n = len(rows)
    assert n and all(len(row) == n for row in rows) and len(rhs) == n
    matrix = [[F(x) for x in row] + [F(b)] for row, b in zip(rows, rhs)]
    for j in range(n):
        at = next(i for i in range(j, n) if matrix[i][j])
        matrix[j], matrix[at] = matrix[at], matrix[j]
        pivot = matrix[j][j]
        matrix[j] = [x / pivot for x in matrix[j]]
        for i in range(n):
            if i != j:
                value = matrix[i][j]
                matrix[i] = [a - value*b for a, b in zip(matrix[i], matrix[j])]
    values = [row[-1] for row in matrix]
    assert all(sum(a*x for a, x in zip(row, values)) == b for row, b in zip(rows, rhs))
    return values


def load():
    fixed = json.loads(INPUT.read_text(encoding='utf8'))
    assert fixed['format'] == 'joint-budget-n18-v1'
    assert fixed['source_family'] == 'unit-cap-certificates.json' and fixed['source_input'] == 'P20'
    assert [fixed[k] for k in ('n', 'd', 'N', 'q')] == [18, 20, 40, 36887312]
    source = json.loads((HERE / 'inputs/unit-cap-certificates.json').read_text(encoding='utf8'))
    sources = [item for item in source['inputs'] if item['name'] == 'P20']
    assert len(sources) == 1
    raw = sources[0]
    checks = module('joint_fixed_source_checks', 'verify_unit_cap_inputs.py')
    exact = checks.verify_input(raw)
    logs = module('joint_fixed_log_bounds', 'norm-funded-author.py')
    l2 = logs.series(F(1, 3))
    assert F(9, 260*3**65) < F(1, logs.GRID)
    family = []
    for j, (column, checked) in enumerate(zip(raw['columns'], exact['columns'])):
        D = abs(column['norm_B'])
        cert = None if j < 40 else logs.logcert(D, 20, l2)
        ell = F(0) if cert is None else F(*cert['ell_lower'])
        meta = {'kind': 'monomial' if j < 40 else 'frozen_residue', 'index': j if j < 40 else j-40}
        if j >= 40:
            k = j-40
            meta.update(seed_kind='basis' if k < 20 else 'adjacent',
                basis_index=k if k < 20 else (k-20)//2,
                seed_sign=0 if k < 20 else (-1 if (k-20)%2 == 0 else 1), z=column['B'][:20])
        full_norm = raw['q']**20*column['norm_B']
        content = column['content_F']
        family.append(dict(meta, B=column['B'],
            F_coefficients=column['F'], kernel_multiplier=column['U'],
            signed_res_B=column['norm_B'], signed_res_F=full_norm, content=content,
            D=D, e=pair(checked['e']), h=vec(checked['h']), ell=pair(ell), log_certificate=cert,
            integer_energy=sum(x*x for x in column['F']),
            integer_autocorrelations=[int(x*raw['q']**2) for x in checked['h']], a=pair(1+2*ell),
            primitive_coefficients=[x//content for x in column['F']],
            signed_res_primitive=full_norm//content**20,
            actual_degree=max(i for i,x in enumerate(column['F']) if x)))
    assert len(family) == 98
    e = [F(*c['e']) for c in family]
    ell = [F(*c['ell']) for c in family]
    aa = [1+2*x for x in ell]
    H = [[F(*c['h'][h]) for c in family] for h in range(39)]
    compressed = list(range(20)) + list(range(40, 98))
    ep = [e[j]/aa[j] for j in compressed]
    hp = [[row[j]/aa[j] for j in compressed] for row in H]
    support, zero_lags = fixed['compressed_support'], fixed['zero_lags']
    assert support == [0,1,2,15,16,17,36,37,42,45,55,66,75]
    assert zero_lags == [1,2,9,10,11,15,20,24,30,35,38]
    rows = [[ep[j] for j in support], [F(1)]*len(support)]
    rows += [[hp[h-1][j] for j in support] for h in zero_lags]
    rhs = [F(1), F(2)] + [F(0)]*len(zero_lags)
    values = solve(rows, rhs)
    uc = [F(0)]*len(compressed)
    for j, value in zip(support, values):
        uc[j] = value
    v = [F(0)]*98
    for j, value in zip(compressed, uc):
        if j < 20:
            v[j] = v[39-j] = value/2
        else:
            v[j] = value/aa[j]
    assert min(v) >= 0 and sum(a*b for a, b in zip(e, v)) == 1
    S = sum(v)
    L = sum(a*b for a, b in zip(ell, v))
    corr = [sum(a*b for a, b in zip(row, v)) for row in H]
    assert 0 < S < 2 and S+2*L == 2
    assert [h+1 for h, value in enumerate(corr) if not value] == zero_lags
    y = [F(*value) for value in fixed['y']]
    assert len(y) == 39 and all(abs(value) <= 1 for value in y)
    free = [h-1 for h in zero_lags]
    for h, value in enumerate(corr):
        if value:
            assert y[h] == (1 if value > 0 else -1)
    dual_rows = [[2*hp[h][j] for h in free] + [-ep[j], F(-1)] for j in support]
    dual_rhs = [-sum(2*hp[h][j]*y[h] for h in range(39) if h not in free) for j in support]
    dual = solve(dual_rows, dual_rhs)
    assert dual[:-2] == [y[h] for h in free]
    lam, mu = dual[-2:]
    assert pair(lam) == fixed['lambda_value'] and pair(mu) == fixed['mu'] and mu > 0
    slacks = [2*sum(y[h]*H[h][j] for h in range(39))-lam*e[j]-mu*aa[j] for j in range(98)]
    K = 2*sum(map(abs, corr))
    assert min(slacks) >= 0 and all(a*b == 0 for a, b in zip(v, slacks))
    assert K == lam+2*mu
    assert pair(K) == [1714168546953605078758047203716801788773584362557009514078913891651411860149161,
                      462591029463190283103106576950550691944921758466862571505279774057966813526445]
    return {'n':18, 'd':20, 'N':40, 'q':raw['q'], 'coefficients':raw['P'],
        'status':'complete', 'global_finite_family_optimum_certified':True,
        'family':family, 'y':vec(y), 'lambda_value':pair(lam), 'mu':pair(mu),
        'dual_slacks':vec(slacks), 'v':vec(v), 'S':pair(S), 'L':pair(L),
        'kappa':pair(K), 'compressed_support':support, 'zero_lags':zero_lags,
        'compressed_indices':compressed, 'r_prime':vec(ep), 'H_prime':[vec(row) for row in hp],
        'compressed_u':vec(uc), 'correlations':vec(corr)}


if __name__ == '__main__':
    record = load()
    print(json.dumps({'status':'passed', 'directions':len(record['family']),
        'dual_coordinates':len(record['y']), 'primal_rank':13, 'dual_rank':13,
        'kappa':record['kappa']}))
