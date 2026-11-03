"""D158 exact five-control verification; declared aggregate cap120s, no search."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from time import perf_counter
import json
import traceback
import sympy as sp

HERE = (_J_PROGRAM / 'verify.py').parent
START = perf_counter()
CAP = 120
t, v = sp.symbols('t v')
s = t + 1


# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def tick():
    if perf_counter() - START > CAP:
        raise TimeoutError('Declared120-second aggregate author cap exceeded')


def mat(V):
    return [[int(x) for x in row] for row in V.tolist()]


def coeff(p):
    return [int(x) for x in sp.Poly(sp.expand(p), t).all_coeffs()[::-1]]


def poly(V):
    tick()
    assert V.is_upper and all(V[i, i] == 1 for i in range(V.rows))
    return sp.expand((-V.inv() * V.T).charpoly(t).as_expr())


def absolute(V):
    return sp.Matrix(V.rows, V.rows, lambda i, j:
                     1 if i == j else -abs(V[i, j]) if i < j else 0)


def cover(V):
    W = sp.eye(2 * V.rows)
    for i in range(V.rows):
        for j in range(i + 1, V.rows):
            x = int(V[i, j])
            if x <= 0:
                W[2*i, 2*j] = W[2*i+1, 2*j+1] = x
            else:
                W[2*i, 2*j+1] = W[2*i+1, 2*j] = -x
    return W


def cost(V):
    upper = [int(V[i, j]) for i in range(V.rows) for j in range(i+1, V.rows)]
    return dict(rank=V.rows, height=max([1] + [abs(x) for x in upper]),
                energy=sum(x*x for x in upper))


def pencil(V, p):
    out = []
    for h in range(V.rows + 1):
        tick()
        value = int((h*V + V.T).det(method='domain-ge'))
        assert value == p.subs(t, h)
        out.append(value)
    return out


def paired(U, C):
    n, k = U.rows, C.cols
    Z = sp.eye(n+2*k)
    Z[:n, :n] = U
    Z[:n, n:n+k] = C
    Z[:n, n+k:] = C
    Z[n:n+k, n+k:] = 2*sp.eye(k)
    return Z


def trace_poly(p):
    p = sp.Poly(p, t)
    n = p.degree()
    assert n % 2 == 0
    d = n//2
    cs = [int(p.nth(i)) for i in range(n+1)]
    assert cs == cs[::-1]
    cheb = [sp.Integer(2), v]
    for j in range(2, d+1):
        cheb.append(sp.expand(v*cheb[-1]-cheb[-2]))
    q = sp.Integer(cs[d])
    for j in range(1, d+1):
        q += cs[d+j]*cheb[j]
    q = sp.expand(q)
    assert sp.expand(t**d*q.subs(v, t+1/t)-p.as_expr()) == 0
    return q


def main():
    tick()
    a, b, k, R, L = sp.symbols('a b k R L')
    base = sp.Matrix([[s, t*k], [k, s]])
    perturb = sp.Matrix([[a*a, a*b], [a*b, b*b]])
    delta = a*a+b*b-k*a*b
    assert sp.expand((base-t*R*perturb).det() -
                     (s*s-t*k*k-t*R*s*delta)) == 0
    contractions = []
    for r in (1, 2):
        I = sp.eye(r)
        H = I.row_join(I)
        for sign in (1, -1):
            T = (s*I).row_join(sign*2*t*I).col_join(
                (sign*2*I).row_join(s*I))
            value = (H*T.inv()*H.T).applyfunc(sp.cancel)
            expected = sp.zeros(r) if sign == 1 else 4*s/(t-1)**2*I
            assert (value-expected).applyfunc(sp.cancel) == sp.zeros(r)
            assert sp.factor(T.det()) == (t-1)**(2*r)
            contractions.append(dict(k=r, sign=sign,
                                     contraction=[[str(x) for x in row]
                                                  for row in value.tolist()]))
    B = sp.Matrix([[1, 1], [0, 1], [0, 1], [0, 1]])
    U = sp.eye(6)
    U[:4, 4:] = -B
    P = t**4-t**3-t**2-t+1
    pU = poly(U)
    assert pU == sp.expand(s*s*P)
    M = t*U + U.T
    e1, e2 = sp.eye(6)[:, 0], sp.eye(6)[:, 1]
    assert sp.cancel(s*pU*(e2.T*M.inv()*e2)[0]-s*s*(t**4+1)) == 0
    fL = v**3-(4*L+3)*v*v-v+8*L+6
    HL = sp.expand(t**3*fL.subs(v, t+1/t))
    assert sp.expand(P*(t-1)**2 - 4*t*L*(t**4+1)-HL) == 0
    endpoints = [-2, -1, 1, 2, 4*L+2, 4*L+3]
    signs = [sp.expand(fL.subs(v, x)) for x in endpoints]
    assert signs == [-8*L-12, 4*L+3, 4*L+3, -8*L,
                     -16*L**2-12*L, 4*L+3]
    mod3 = [int((v**3-v*v-v+2).subs(v, x)) % 3 for x in range(3)]
    assert mod3 == [2, 1, 1]
    c = sp.Matrix([0, 1, -1, 0, 0, 0])
    d = c.applyfunc(abs)
    assert sp.cancel(s*pU*(d.T*M.inv()*d)[0] -
                     2*s*s*(s**4-3*t*s*s+t*t)) == 0
    fj = v**3-6*v*v-10*v+3
    J = sp.expand(t**3*fj.subs(v, t+1/t))
    assert sp.expand(P*(t*t+t+1)-6*t*(s**4-3*t*s*s+t*t)-J) == 0
    jpoints = [-2, -1, 0, 1, 7, 8]
    jvalues = [int(fj.subs(v, x)) for x in jpoints]
    assert jvalues == [-9, 6, 3, -12, -18, 51]
    independent_trace = v**4-13*v**3+33*v*v+64*v-44
    independent_factor = sp.expand(t**4*independent_trace.subs(v, t+1/t))
    ipoints = [-2, -1, 0, 1, 6, 7, 8]
    ivalues = [int(independent_trace.subs(v, x)) for x in ipoints]
    assert ivalues == [80, -61, -44, 41, 16, -37, 20]
    ilinear = [int(independent_trace.subs(v, x)) % 3 for x in range(3)]
    assert ilinear == [1, 2, 2]
    quadratics = [v*v+1, v*v+v+2, v*v+2*v+2]
    irems = [[int(sp.Poly(sp.rem(independent_trace, q, domain=sp.GF(3)), v).nth(i)) % 3
              for i in range(2)] for q in quadratics]
    assert irems == [[2, 2], [1, 2], [2, 2]]
    controls = [('pair_m1', e2, 1), ('pair_m2', 2*e2, 4),
                ('two_repeated', e2.row_join(e2), 2),
                ('two_independent', e1.row_join(e2), None)]
    records = []
    for label, C, ell in controls:
        records.append((label, paired(U, C), C, ell))
    Z = sp.eye(8)
    Z[:6, :6] = U
    Z[:6, 6] = Z[:6, 7] = c
    Z[6, 7] = 1
    records.append(('nonbipartite_phi6', Z, None, None))
    payload = []
    for label, Z, C, ell in records:
        tick()
        A = absolute(Z)
        W = cover(Z)
        p, pa, pw = poly(Z), poly(A), poly(W)
        assert sp.expand(pw-p*pa) == 0
        assert cost(A) == cost(Z)
        assert cost(W)['energy'] == 2*cost(Z)['energy']
        schur_values = []
        if C is not None:
            q = C.cols
            assert sp.expand(p-pU*(t-1)**(2*q)) == 0
            D = C.applyfunc(abs)
            for h in range(2, Z.rows+3):
                tick()
                X = h*U+U.T-sp.Rational(4*h*(h+1), (h-1)**2)*(D*D.T)
                value = (h-1)**(2*q)*X.det(method='domain-ge')
                assert value == pa.subs(t, h)
                schur_values.append(int(value))
            if ell is not None:
                assert sp.expand(pa-s*s*(t-1)**(2*q-2)*HL.subs(L, ell)) == 0
            else:
                assert sp.expand(pa-s*s*independent_factor) == 0
            assert cost(Z)['energy'] == 5+2*sum(x*x for x in C)+4*q
        else:
            assert sp.expand(p-s*s*P*(t*t-t+1)) == 0
            assert sp.expand(pa-s*s*J) == 0
            assert cost(Z) == dict(rank=8, height=1, energy=10)
        qabs = trace_poly(pa)
        payload.append(dict(label=label, C=mat(C) if C is not None else None,
                            original_matrix=mat(Z), absolute_matrix=mat(A),
                            proper_cover_matrix=mat(W), original_polynomial=coeff(p),
                            absolute_polynomial=coeff(pa), cover_polynomial=coeff(pw),
                            original_cost=cost(Z), absolute_cost=cost(A), cover_cost=cost(W),
                            absolute_trace_polynomial=str(qabs),
                            absolute_factorization=str(sp.factor(pa)),
                            pencil_values=dict(original=pencil(Z, p), absolute=pencil(A, pa),
                                               proper_cover=pencil(W, pw)),
                            schur_values=schur_values))
    tick()
    return dict(scope='D158 exact five controls; no discovery search', symbolic=dict(rank_one_identity=True, contractions=contractions, full_H_L_coefficients=[str(sp.expand(HL).coeff(t, i)) for i in range(7)], trace_endpoint_values=[str(x) for x in signs], mod3_values=mod3, phi6_trace_values=jvalues, independent_trace_coefficients=[int(independent_trace.coeff(v, i)) for i in range(5)], independent_trace_endpoints=ipoints, independent_trace_values=ivalues, independent_mod3_linear_values=ilinear, independent_mod3_quadratic_remainders=irems), controls=payload, all_exact_checks_passed=True)


if __name__ == '__main__':
    try:
        result = main()
        ((_J_OUTPUT / 'result.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
        print(json.dumps(dict(passed=True, controls=len(result['controls']))))
    except Exception:
        failure = dict(traceback=_record_text(traceback.format_exc()))
        ((_J_OUTPUT / 'failure.json')).write_text(json.dumps(failure, indent=2)+'\n', encoding='utf-8')
        raise
