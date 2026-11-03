"""Exact targeted five-core/two-tail test; no floating point or random search.

All 3^10 signed unit-entry cores are represented modulo diagonal sign changes.
An ordered greedy spanning forest is fixed negative, with no vertex reordering.
Each surviving core's five possible attachment vertices is checked. The target
is precisely (t+1)(t^6-t^5-t^3-t+1); no factors are silently removed.
"""
from itertools import permutations, combinations, product
from math import comb
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as s

EDGES = list(combinations(range(5), 2))


def terms(vertices):
    n = len(vertices)
    out = []
    for perm in permutations(range(n)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        factors = []
        ascents = fixed = 0
        for i, j in enumerate(perm):
            if i == j:
                fixed += 1
            else:
                edge = tuple(sorted((vertices[i], vertices[j])))
                factors.append(EDGES.index(edge))
                ascents += int(i < j)
        coeffs = [(ascents+k, sign*comb(fixed, k)) for k in range(fixed+1)]
        out.append((factors, coeffs))
    return out


def poly(entries, tt, n):
    answer = [0]*(n+1)
    for factors, cc in tt:
        value = 1
        for i in factors:
            value *= entries[i]
            if not value:
                break
        if value:
            for k, c in cc:
                answer[k] += c*value
    return answer


def forest_negative(entries):
    parent = list(range(5))
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for (i, j), value in zip(EDGES, entries):
        if not value:
            continue
        a, b = find(i), find(j)
        if a != b:
            if value != -1:
                return False
            parent[a] = b
    return True


def main():
    pp = terms(list(range(5)))
    qq = [terms([i for i in range(5) if i != j]) for j in range(5)]
    count = coeff0 = tested = 0
    successes = []
    t = s.Symbol('t')
    target = (t+1)*(t**6-t**5-t**3-t+1)
    for entries in product((-1, 0, 1), repeat=10):
        if not forest_negative(entries):
            continue
        count += 1
        p = poly(entries, pp, 5)
        assert p == p[::-1]
        if p[4] != 0:
            continue
        coeff0 += 1
        B = p[3]
        for j in range(5):
            tested += 1
            q = poly(entries, qq[j], 4)
            if q[3] != B+1 or q[2] != B:
                continue
            V = s.eye(7)
            for edge, value in zip(EDGES, entries):
                V[edge[0], edge[1]] = value
            V[j, 5] = V[5, 6] = 1
            actual = (-V.inv()*V.T).charpoly(t).as_expr()
            assert s.expand(actual-target) == 0
            Vm = s.eye(7)
            for i in range(7):
                for k in range(i+1, 7):
                    Vm[i, k] = -abs(V[i, k])
            absolute = s.factor((-Vm.inv()*Vm.T).charpoly(t).as_expr())
            successes.append({'entries': entries, 'attachment': j,
                              'core': p, 'deletion': q,
                              'matrix': [list(map(int, V.row(k))) for k in range(7)],
                              'absolute_polynomial': str(absolute),
                              'energy': sum(int(x)**2 for x in entries)+2})
    result = {'raw_entry_box_size': 3**10, 'forest_negative_representatives': count,
              'zero_t4_cores': coeff0, 'attachment_tests_after_filter': tested,
              'target': str(s.expand(target)), 'success_count': len(successes),
              'successes': successes,
              'scope': 'signed-unit five-core with one two-vertex unit tail; gauge quotient only, no order quotient'}
    (_J_OUTPUT / 'probe5.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'successes'}))
    if successes:
        print(json.dumps(successes[0]))


if __name__ == '__main__':
    main()
