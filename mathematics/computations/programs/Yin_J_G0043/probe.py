"""Bounded exact adjustable-core inverse-target experiment for D73.

This author discovery program searches only six entries in [-2,2] and two
distinct attachment vertices, with chain lengths1 and2. Failure is scoped to
that box, unless a separate symbolic argument in D73 proves more.
"""
from itertools import product, combinations
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as s

t = s.Symbol('t')
variables = s.symbols('a b c d e f')
edges = list(combinations(range(4), 2))
V = s.eye(4)
for edge, value in zip(edges, variables):
    V[edge[0], edge[1]] = value


def det_poly(keep):
    W = V.extract(keep, keep)
    return s.Poly(s.expand((t*W+W.T).det(method='domain-ge')), t)


def main():
    p = det_poly(list(range(4)))
    qi = [det_poly([k for k in range(4) if k != i]) for i in range(4)]
    A, B = p.nth(3), p.nth(2)
    a_eval = s.lambdify(variables, A, 'math')
    b_eval = s.lambdify(variables, B, 'math')
    c_eval = [s.lambdify(variables, q.nth(2), 'math') for q in qi]
    P = t**6-t**5-t**3-t+1
    target = s.Poly((t+1)*P, t)
    symbolic = []
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            r = det_poly([k for k in range(4) if k not in (i, j)])
            full = s.Poly(s.expand((1+t)*(1+t+t*t)*p.as_expr()
                          - t*(1+t+t*t)*qi[i].as_expr()
                          - t*(1+t)**2*qi[j].as_expr()
                          + t*t*(1+t)*r.as_expr()), t)
            equations = [s.expand(full.nth(k)-target.nth(k)) for k in (6, 5, 4)]
            symbolic.append((i, j, s.lambdify(variables, equations, 'math'), equations))
    successes = []
    patterns = 0
    for entries in product(range(-2, 3), repeat=6):
        for i, j, test, equations in symbolic:
            patterns += 1
            if all(value == 0 for value in test(*entries)):
                W = s.eye(4)
                for edge, value in zip(edges, entries):
                    W[edge[0], edge[1]] = value
                fullV = s.eye(7)
                fullV[:4, :4] = W
                fullV[i, 4] = 1
                fullV[j, 5] = fullV[5, 6] = 1
                actual = (-fullV.inv()*fullV.T).charpoly(t).as_expr()
                assert s.expand(actual-target.as_expr()) == 0
                successes.append({'entries': entries, 'attach_length1': i,
                                  'attach_length2': j,
                                  'core_A_B': [int(a_eval(*entries)), int(b_eval(*entries))],
                                  'deletion_C': [int(fn(*entries)) for fn in c_eval],
                                  'V': [list(map(int, fullV.row(k))) for k in range(7)]})
    result = {'entry_range': [-2, 2], 'core_count': 5**6,
              'ordered_attachment_pairs': 12, 'tested_patterns': patterns,
              'target': str(target.as_expr()),
              'core_coefficient_A': str(A), 'core_coefficient_B': str(B),
              'first_pair_equations': [str(q) for q in symbolic[0][3]],
              'success_count': len(successes), 'successes': successes}
    (_J_OUTPUT / 'probe.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'successes'}))
    if successes:
        print(json.dumps(successes[0]))


if __name__ == '__main__':
    main()
