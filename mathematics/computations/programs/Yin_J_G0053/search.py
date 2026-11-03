"""Bounded changed integral root-basis discovery; exact retained certificates.

The 25000 proposal cap is not an exhaustive integral-basis search.  Floating
acceptance scores choose candidates only.  All target coefficients and the
retained basis/polynomials are checked by exact integer/symbolic arithmetic.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import math
import random
import time
import sympy as sp

BASE = (_J_PROGRAM / 'search.py').parent
N = 6
CAP = 25000
RNG_SEED = 11320261010
ENERGY_CAP = 1000
BASIS_ENTRY_CAP = 1000000


def identity():
    return [[int(i == j) for j in range(N)] for i in range(N)]


def seed():
    g = [[2*int(i == j) for j in range(N)] for i in range(N)]
    for i in range(1, N):
        g[0][i] = g[i][0] = 1
    for i in range(1, N):
        for j in range(1, N):
            if i != j:
                g[i][j] = 1 if (i-j) % 5 in (1, 4) else -1
    return g


def upper(g):
    return [[int(i == j) if j <= i else g[i][j]
             for j in range(N)] for i in range(N)]


def energy(g):
    return sum(g[i][j]**2 for i in range(N) for j in range(i+1, N))


def multiply(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]


def first_coefficients(g):
    v = upper(g)
    c = [[0]*N for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(N):
            c[i][j] = -v[j][i]-sum(v[i][k]*c[k][j] for k in range(i+1, N))
    s1 = sum(c[i][i] for i in range(N))
    s2 = sum(c[i][j]*c[j][i] for i in range(N) for j in range(N))
    assert (s1*s1-s2) % 2 == 0
    return -s1, (s1*s1-s2)//2


def transform(g, q, move):
    g = [row[:] for row in g]
    q = [row[:] for row in q]
    kind, i, j = move
    if kind == 'swap':
        g[i], g[j] = g[j], g[i]
        for row in g:
            row[i], row[j] = row[j], row[i]
        for row in q:
            row[i], row[j] = row[j], row[i]
    else:
        a = g[i][j]
        for k in range(N):
            if k != i:
                g[i][k] = g[k][i] = g[i][k]-a*g[j][k]
        g[i][i] = 2
        for row in q:
            row[i] -= a*row[j]
    return g, q


def score(coeffs, g):
    return math.log1p(abs(coeffs[0]+2)+abs(coeffs[1]-1)) + .002*math.log1p(energy(g))


def run():
    rng = random.Random(RNG_SEED)
    start = time.perf_counter()
    g0 = seed()
    g, q, steps = g0, identity(), []
    coeffs = first_coefficients(g)
    best = (score(coeffs, g), g, q, steps, coeffs, 0)
    accepted = rejected_cap = 0
    found = False
    records = []
    for proposal in range(1, CAP+1):
        if proposal % 1000 == 0:
            g, q, steps = seed(), identity(), []
        i, j = rng.sample(range(N), 2)
        move = ['swap' if rng.random() < .25 else 'reflect', i, j]
        candidate_g, candidate_q = transform(g, q, move)
        if energy(candidate_g) > ENERGY_CAP or max(abs(v) for row in candidate_q for v in row) > BASIS_ENTRY_CAP:
            rejected_cap += 1
            continue
        candidate_c = first_coefficients(candidate_g)
        candidate_score = score(candidate_c, candidate_g)
        old_score = score(first_coefficients(g), g)
        temperature = .08 + .9*(1-(proposal % 1000)/1000)
        if candidate_score < old_score or rng.random() < math.exp((old_score-candidate_score)/temperature):
            g, q, steps = candidate_g, candidate_q, steps+[move]
            accepted += 1
            if candidate_score < best[0]:
                best = (candidate_score, g, q, steps, candidate_c, proposal)
                records.append({'proposal': proposal, 'first_coefficients': list(candidate_c), 'energy': energy(g)})
            if candidate_c == (-2, 1):
                best = (candidate_score, g, q, steps, candidate_c, proposal)
                found = True
                break
    _, g, q, steps, coeffs, selected_at = best
    replay_g, replay_q = seed(), identity()
    for move in steps:
        replay_g, replay_q = transform(replay_g, replay_q, move)
    assert replay_g == g and replay_q == q
    G0, G, Q = map(sp.Matrix, (g0, g, q))
    assert Q.det() in (-1, 1) and Q.T*G0*Q == G
    assert list(G.diagonal()) == [2]*N and G.det() == -1
    V = sp.Matrix(upper(g)); Vm = sp.eye(N)
    for i in range(N):
        for j in range(i+1, N):
            Vm[i, j] = -abs(V[i, j])
    t = sp.symbols('t')
    p = sp.Poly((t*V+V.T).det(), t)
    target = sp.Poly((t*t-t+1)*(t**4-t**3-t*t-t+1), t)
    if found:
        assert p == target
    absolute = sp.Poly((t*Vm+Vm.T).det(), t)
    result = {'scope': {'proposal_cap': CAP, 'random_seed': RNG_SEED, 'energy_cap': ENERGY_CAP, 'basis_entry_cap': BASIS_ENTRY_CAP, 'rank': N, 'target_coefficients_descending': [int(v) for v in target.all_coeffs()]}, 'found': found, 'proposals_executed': proposal, 'accepted_moves': accepted, 'cap_rejections': rejected_cap, 'selected_at': selected_at, 'seed_gram': g0, 'integral_basis': q, 'basis_determinant': int(Q.det()), 'selected_steps': steps, 'gram': g, 'unitriangular': upper(g), 'energy': energy(g), 'height': max((abs(v) for row in upper(g) for v in row)), 'polynomial_descending': [int(v) for v in p.all_coeffs()], 'factorization': str(sp.factor(p.as_expr())), 'absolute_polynomial_descending': [int(v) for v in absolute.all_coeffs()], 'absolute_factorization': str(sp.factor(absolute.as_expr())), 'cover_polynomial_descending': [int(v) for v in (p * absolute).all_coeffs()], 'improvement_records': records}
    ((_J_OUTPUT / 'search_result.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('found','proposals_executed','selected_at','energy','height','polynomial_descending','absolute_polynomial_descending')}))


if __name__ == '__main__':
    run()
