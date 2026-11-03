"""Separately implemented exact review of J59; never imports author programs.

Declared complete cap: 20 * 57**3 short-root triples; at most 20,000
pivot-graph calls; two symbolic/finite controls; 240 seconds overall.
D129 is an optional within-run no-write observation, never a required input.
Only review_result.json is written. No stored fingerprint gate is used.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import comb, factorial
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time

import numpy as np
import sympy as sp

HERE = (_J_PROGRAM / 'review_independent.py').parent
START = time.perf_counter()
CAP_SECONDS = 240


def deadline():
    assert time.perf_counter() - START < CAP_SECONDS, 'review runtime cap'


def load(name):
    return json.loads((((_J_PROGRAM if name in ('costs.py', 'exterior.py', 'readme.md', 'review_independent.py', 'search.py') else _J_OUTPUT) / name)).read_text(encoding='utf-8'))


def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i + 1, len(p))) % 2 else 1


def tr(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def determinant(a):
    a = [[Q(x) for x in row] for row in a]
    value = Q(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            value = -value
        z = a[j][j]
        value *= z
        for i in range(j + 1, len(a)):
            c = a[i][j] / z
            for k in range(j + 1, len(a)):
                a[i][k] -= c * a[j][k]
    return value


def inverse(a):
    n = len(a)
    w = [[Q(x) for x in row] + [Q(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        p = next(i for i in range(j, n) if w[i][j])
        w[j], w[p] = w[p], w[j]
        z = w[j][j]
        w[j] = [x / z for x in w[j]]
        for i in range(n):
            if i != j:
                z = w[i][j]
                w[i] = [x - z * y for x, y in zip(w[i], w[j])]
    return [row[n:] for row in w]


def integral(a):
    out = []
    for row in a:
        assert all(Q(x).denominator == 1 for x in row)
        out.append([int(x) for x in row])
    return out


def convolution(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def pencil_leibniz(v):
    """Full coefficients of det(t V + V^t), by permutation polynomial products."""
    n = len(v)
    out = [0] * (n + 1)
    for p in permutations(range(n)):
        term = [parity(p)]
        for i, j in enumerate(p):
            term = convolution(term, [v[j][i], v[i][j]])
        out = [x + y for x, y in zip(out, term)]
    return out


def pencil_newton(v):
    """Independent complete polynomial via rational inverse and Newton traces."""
    n = len(v)
    w = mm(inverse(v), tr(v))
    c = [[-x for x in row] for row in w]
    powers, coeffs, traces = eye(n), [Q(1)], []
    for k in range(1, n + 1):
        powers = mm(powers, c)
        traces.append(sum(powers[i][i] for i in range(n)))
        coeffs.append(-sum(coeffs[k - j] * traces[j - 1]
                           for j in range(1, k + 1)) / k)
    values = [determinant(v) * x for x in reversed(coeffs)]
    assert all(x.denominator == 1 for x in values)
    return [int(x) for x in values]


def update_hist(counter, values):
    vals, counts = np.unique(values, return_counts=True)
    counter.update({str(int(x)): int(y) for x, y in zip(vals, counts)})


def complete_short_roots():
    saved = load('search_result.json')
    g = np.array([[2, 1, 1, 1, 1, 1], [1, 2, 1, -1, -1, 1],
                  [1, 1, 2, 1, -1, -1], [1, -1, 1, 2, 1, -1],
                  [1, -1, -1, 1, 2, 1], [1, 1, -1, -1, 1, 2]],
                 dtype=np.int64)
    conference = g - 2 * np.eye(6, dtype=np.int64)
    assert np.array_equal(conference @ conference, 5 * np.eye(6, dtype=np.int64))
    assert determinant(g.tolist()) == -1
    q0 = np.eye(6, dtype=np.int64) - np.eye(6, k=1, dtype=np.int64)
    assert determinant(q0.tolist()) == 1
    root_cube = np.array(list(product((-1, 0, 1), repeat=6)), dtype=np.int64)
    norms = np.einsum('bi,ij,bj->b', root_cube, g, root_cube)
    all_roots = root_cube[norms == 2]
    roots = np.array([x for x in all_roots if next(int(y) for y in x if y) > 0])
    assert all_roots.tolist() == saved['all_roots']
    assert roots.tolist() == saved['normalized_roots']
    assert len(all_roots) == 114 and len(roots) == 57
    coords = roots @ np.array(integral(inverse(q0.tolist())), dtype=np.int64).T
    old = q0.T
    old_signs = np.array([x if next(int(y) for y in x if y) > 0 else -x for x in old])
    rr, ro, base = roots @ g @ roots.T, roots @ g @ q0, q0.T @ g @ q0
    assert np.array_equal(np.diag(base),np.full(6,2))
    bound = max(int(abs(x).max()) for x in (rr, ro, base))
    # An explicit conservative bound protects all vectorized int64 operations.
    assert factorial(6) * (2 * bound) ** 6 < 2**63
    edges = list(combinations(range(6), 2))
    edge_no = {e: i for i, e in enumerate(edges)}
    # Direct determinant coefficient: each permutation contributes t^u(1+t)^f.
    first_terms = Counter()
    pf_terms = Counter()
    for p in permutations(range(6)):
        ups = sum(i < p[i] for i in range(6))
        fixed = sum(i == p[i] for i in range(6))
        if 0 <= 5 - ups <= fixed:
            word = tuple(sorted(edge_no[tuple(sorted((i, p[i])))]
                                for i in range(6) if i != p[i]))
            first_terms[word] += parity(p) * comb(fixed, 5 - ups)
        pairs = [p[j:j + 2] for j in (0, 2, 4)]
        sign = parity(p) * (-1 if sum(a > b for a, b in pairs) % 2 else 1)
        word = tuple(sorted(edge_no[tuple(sorted(pair))] for pair in pairs))
        pf_terms[word] += sign
    assert all(c % 48 == 0 for c in pf_terms.values())
    pf_terms = {w: c // 48 for w, c in pf_terms.items() if c}
    assert len(pf_terms) == 15
    ir, js, kt = np.indices((57, 57, 57))
    grid = [ir, js, kt]
    totals, energies, pfs, mods = Counter(), Counter(), Counter(), Counter()
    per_positions = []
    for positions in combinations(range(6), 3):
        deadline()
        i, j, k = positions
        # Alternating 3-by-3 determinant over all ordered triples, no pair-cofactor loop.
        minor = np.zeros((57, 57, 57), dtype=np.int64)
        for p in permutations(range(3)):
            term = np.ones_like(minor)
            for row in range(3):
                term *= coords[grid[p[row]], positions[row]]
            minor += parity(p) * term
        unit = abs(minor) == 1
        olds = np.zeros_like(unit)
        for slot, position in enumerate(positions):
            equal = np.all(roots == old_signs[position], axis=1)
            olds |= equal[grid[slot]]
        genuine = unit & ~olds
        cnt = Counter(triples=57**3, singular=int(np.sum(minor == 0)),
                      nonunit_nonsingular=int(np.sum((minor != 0) & ~unit)),
                      unit_minor=int(np.sum(unit)), old_controls=int(np.sum(unit & olds)),
                      genuine=int(np.sum(genuine)))
        rids = [z[genuine] for z in grid]
        slot_for = {pos: slot for slot, pos in enumerate(positions)}
        grams = []
        for a, b in edges:
            if a in slot_for and b in slot_for:
                val = rr[rids[slot_for[a]], rids[slot_for[b]]]
            elif a in slot_for:
                val = ro[rids[slot_for[a]], b]
            elif b in slot_for:
                val = ro[rids[slot_for[b]], a]
            else:
                val = np.full(cnt['genuine'], base[a, b], dtype=np.int64)
            grams.append(val)
        def evaluate(terms):
            ans = np.zeros(cnt['genuine'], dtype=np.int64)
            for word, c in terms.items():
                term = np.full(cnt['genuine'], c, dtype=np.int64)
                for e in word:
                    term *= grams[e]
                ans += term
            return ans
        first, pf = evaluate(first_terms), evaluate(pf_terms)
        assert np.all((pf * pf - 5) % 4 == 0)
        second = (pf * pf - 5) // 4
        assert not np.any((first == -2) & (abs(pf) == 3))
        assert not np.any((first == 0) & (abs(pf) == 1))
        assert not np.any((first % 2 == 0) & ((first + second) % 4 != 1))
        update_hist(energies, sum(x * x for x in grams))
        update_hist(pfs, pf)
        modnums, counts = np.unique(4 * (first % 4) + second % 4, return_counts=True)
        mods.update({f'{int(x)//4},{int(x)%4}': int(y) for x, y in zip(modnums, counts)})
        totals.update(cnt)
        expected = saved['position_counts'][len(per_positions)]
        assert list(positions) == expected['positions'] and dict(cnt) == expected['counts']
        per_positions.append(dict(positions=list(positions), counts=dict(cnt)))
    assert dict(totals) == saved['counts']
    assert dict(energies) == saved['energy_histogram']
    assert dict(pfs) == saved['pfaffian_histogram']
    assert dict(mods) == saved['coefficient_mod4_histogram']
    assert saved['complete'] and not saved['target_hits'] and not saved['first20_congruence_escape_controls']
    return dict(counts=dict(totals), position_counts=per_positions,
                energy_histogram=dict(energies), pfaffian_histogram=dict(pfs),
                coefficient_mod4_histogram=dict(mods), safe_integer_entry_bound=bound,
                root_vectors=729, norm_two_roots=114, sign_representatives=57,
                determinant_coefficient_terms=len(first_terms), pfaffian_terms=15)


def exterior_symbolic_and_costs():
    saved, exterior = load('costs_result.json'), load('exterior_result.json')
    a, k, t = sp.symbols('a k t')
    A = sp.Matrix([[0, 0, 0, -1], [1, 0, 0, k], [0, 1, 0, a], [0, 0, 1, k + 1]])
    pairs = list(combinations(range(4), 2))
    C = sp.Matrix([[sp.expand(A[i, u] * A[j, v] - A[i, v] * A[j, u])
                    for u, v in pairs] for i, j in pairs])
    G = sp.Matrix([[parity(x + y) if len(set(x + y)) == 4 else 0
                    for y in pairs] for x in pairs])
    assert G * G == sp.eye(6) and determinant(G.tolist()) == -1
    assert all(sp.expand(x) == 0 for x in C.T * G * C - G)
    # Derive the characteristic polynomial from traces, then its resolvent at one.
    cp, powers, traces = [sp.Integer(1)], sp.eye(6), []
    for j in range(1, 7):
        powers = powers * C
        traces.append(sp.expand(sp.trace(powers)))
        cp.append(sp.expand(-sum(cp[j-i]*traces[i-1] for i in range(1,j+1))/j))
    p = sum(cp[j] * t**(6-j) for j in range(7))
    expected = t**6+a*t**5+(k*(k+1)-1)*t**4-(2*a+2*k*(k+1)+1)*t**3+(k*(k+1)-1)*t**2+a*t+1
    assert sp.expand(p-expected) == 0 and sp.expand(p.subs(t,1)) == -1
    synthetic = [cp[0]]
    for c in cp[1:-1]: synthetic.append(sp.expand(c+synthetic[-1]))
    resolvent = sp.zeros(6)
    for c in synthetic: resolvent = resolvent * C + c*sp.eye(6)
    inverse_one = -resolvent.applyfunc(sp.expand)
    assert all(sp.expand(x)==0 for x in (sp.eye(6)-C)*inverse_one-sp.eye(6))
    V = (G*inverse_one).applyfunc(sp.expand)
    assert all(sp.expand(x)==0 for x in V+V.T-G)
    assert all(sp.Poly(x,a,k).domain == sp.ZZ for x in V if x)
    assert all(sp.expand(V[i,j]-sp.sympify(saved['matrix_V_formula'][i][j],locals={'a':a,'k':k})) == 0
               for i in range(6) for j in range(6))
    # Absolute-value chambers are handled through nonnegative symbols, not sampling.
    u, K = sp.symbols('u K', nonnegative=True)
    chamber = V.subs({a:u-1,k:K}).applyfunc(sp.expand)
    absolute = chamber.applyfunc(lambda x:-sp.Abs(x))
    general_absolute = [sp.expand(x) for x in pencil_leibniz(absolute.tolist())]
    L=(2*K+1)*u-3; M=-K*(K+1)+(8*K+4)*u-3; R=-2*K*(K+1)+(12*K+6)*u-3
    assert all(sp.expand(x-y)==0 for x,y in zip(general_absolute,[-1,L,M,R,M,L,-1]))
    assert sp.expand(sum(x*x for x in chamber)-(6*K*K+6*K+17+4*u*u))==0
    absolute_expression=sum(x*t**i for i,x in enumerate(general_absolute))
    assert sp.expand(absolute_expression-sp.sympify(saved['full_absolute_formula'],locals={'t':t,'k':K,'u':u}))==0
    assert saved['absolute_determinant']==-1
    controls = []
    for item in saved['controls']:
        deadline()
        subst = {a:item['a'], k:item['k']}
        v = integral(V.subs(subst).tolist())
        c = integral(C.subs(subst).tolist())
        av = integral(A.subs(subst).tolist())
        assert v==item['V'] and c==item['C'] and av==item['A'] and G.tolist()==item['G']
        negative = [[-abs(x) for x in row] for row in v]
        # Build each entry as its complete two-dimensional sign representation.
        cover = [[0]*12 for _ in range(12)]
        for i in range(6):
            for j in range(6):
                for s in range(2):
                    cover[2*i+s][2*j+(s ^ int(v[i][j]>0))] = -abs(v[i][j])
        assert negative==item['full_absolute_B'] and cover==item['cover_W']
        p0, pm, pc = pencil_leibniz(v), pencil_leibniz(negative), pencil_newton(cover)
        assert p0==pencil_newton(v) and pm==pencil_newton(negative)
        assert pc==convolution(p0,pm)
        assert p0==item['original_polynomial'] and pm==item['absolute_polynomial'] and pc==item['full_cover_polynomial']
        assert sp.expand(sp.sympify(item['absolute_factorization'],locals={'t':t}) - sum(x*t**i for i,x in enumerate(pm))) == 0
        stats=dict(V_determinant=int(determinant(v)),absolute_determinant=int(determinant(negative)),
                   cover_determinant=int(determinant(cover)),original_degree=len(p0)-1,
                   absolute_degree=len(pm)-1,cover_degree=len(pc)-1,
                   height=max(abs(x) for row in v for x in row),squared_entry_sum=sum(x*x for row in v for x in row),
                   cover_height=max(abs(x) for row in cover for x in row),cover_squared_entry_sum=sum(x*x for row in cover for x in row))
        assert all(item[key]==val for key,val in stats.items())
        for z in range(-6,7):
            assert determinant([[z*cover[i][j]+cover[j][i] for j in range(12)] for i in range(12)]) == sum(x*z**i for i,x in enumerate(pc))
        controls.append(dict(label=item['label'], original_polynomial=p0,absolute_polynomial=pm,
                             full_cover_polynomial=pc,**stats))
    assert exterior['matrix_A']==saved['controls'][0]['A']
    assert exterior['exterior_C']==saved['controls'][0]['C']
    assert exterior['pairing_G']==saved['controls'][0]['G']
    assert exterior['bilinear_V0']==saved['controls'][0]['V']
    assert exterior['initial_polynomial']==list(reversed(controls[0]['original_polynomial']))
    trace_checks=[]
    for coefficients, points, expected_values in [
        ([-11,-10,0,1],[Q(-3),Q(-2),Q(-1),Q(3),Q(4)],[-8,1,-2,-14,13]),
        ([-7,-4,2,1],[Q(-5,2),Q(-12,5),Q(-2),Q(-1),Q(1),Q(2)],
         [Q(-1,8),Q(37,125),1,-2,-8,1])]:
        values=[sum(Q(c)*z**i for i,c in enumerate(coefficients)) for z in points]
        assert values==expected_values
        trace_checks.append(dict(coefficients=coefficients,points=list(map(str,points)),values=list(map(str,values))))
    return dict(symbolic_parameter_identity=True, symbolic_isometry=True,
                full_absolute_parameter_identity=True, whole_entry_cost_identity=True,
                absolute_trace_interval_checks=trace_checks,
                polynomial_resolvent_integral=True, controls=controls,
                full_cover_value_checks=26, full_polynomial_checks=6)


def pivot_graph():
    saved = load('exterior_result.json')
    initial = tuple(map(tuple,saved['bilinear_V0']))
    levels={6:{initial}}
    calls=Counter({6:1}); dead_count=0; graph_edges=0; maxentry=0
    cache={}
    def roots(form):
        n=len(form)
        if n not in cache:
            cache[n]=[x for x in product((-1,0,1),repeat=n) if any(x) and next(y for y in x if y)>0]
        a=np.array(form,dtype=np.int64); x=np.array(cache[n],dtype=np.int64)
        values=np.einsum('bi,ij,bj->b',x,a,x)
        return [tuple(map(int,row)) for row in x[values==1]]
    def child(form,x):
        n=len(form); pivot=next(i for i,z in enumerate(x) if z)
        assert x[pivot]==1
        right=[sum(form[i][j]*x[j] for j in range(n)) for i in range(n)]
        left=[sum(x[i]*form[i][j] for i in range(n)) for j in range(n)]
        assert sum(x[i]*right[i] for i in range(n))==1
        return tuple(tuple(form[i][j]-right[i]*left[j] for j in range(n) if j!=pivot)
                     for i in range(n) if i!=pivot)
    unique_counts={}
    for n in range(6,0,-1):
        deadline()
        forms=levels.get(n,set()); unique_counts[n]=len(forms)
        if not forms: continue
        next_forms=set()
        for form in forms:
            maxentry=max(maxentry,max(abs(x) for row in form for x in row))
            assert determinant(form)==1
            if n==1:
                assert form != ((1,),), 'unexpected successful declared branch'
                continue
            candidates=roots(form)
            dead_count += not candidates
            graph_edges += len(candidates)
            assert 1+graph_edges<=20000
            calls[n-1] += len(candidates)
            for x in candidates: next_forms.add(child(form,x))
        levels[n-1]=next_forms
    count=dict(nodes=sum(calls.values()),duplicate_forms=sum(calls.values())-sum(unique_counts.values()),
               tested_norm_one_pivots=graph_edges,no_small_norm_one_pivot=dead_count)
    count.update({f'dimension_{n}':v for n,v in calls.items() if v})
    assert count == saved['counts']
    assert maxentry == saved['max_intermediate_entry']
    assert saved['finite_tree_complete'] and not saved['found'] and saved['stop_reason'] is None
    for witness in saved['first20_dead_forms']:
        form=initial
        for x in witness['path']:
            assert tuple(x) in roots(form)
            form=child(form,x)
        assert list(map(list,form))==witness['form'] and not roots(form)
    return dict(counts=count, unique_forms_by_dimension=unique_counts,
                max_intermediate_entry=maxentry, saved_dead_paths_checked=len(saved['first20_dead_forms']),
                full_declared_tree_complete=True, any_success=False)


def main():
    native={p:p.read_bytes() for p in (*HERE.iterdir(), *_J_OUTPUT.iterdir())
            if p.is_file() and not p.name.startswith('review_')}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0129.md')
    observed=draft.read_bytes() if draft.is_file() else None
    short=complete_short_roots()
    exterior=exterior_symbolic_and_costs()
    tree=pivot_graph()
    assert all(p.read_bytes()==b for p,b in native.items())
    if observed is not None: assert draft.read_bytes()==observed
    out=dict(passed=True, implementation='No author-program imports; vectorized integer permutation polynomials; Newton/Cayley-Hamilton resolvent; breadth-first rank-one pivot graph.', declared_cap=dict(short_root_triples=3703860, pivot_calls=20000), short_root_check=short, exterior_and_cost_check=exterior, pivot_graph_check=tree, author_native_files=list(sorted((p.name for p in native))))
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(passed=True, triples=short['counts']['triples'], genuine=short['counts']['genuine'], pivot_nodes=tree['counts']['nodes'], author_files=len(native))))


if __name__=='__main__':
    main()
