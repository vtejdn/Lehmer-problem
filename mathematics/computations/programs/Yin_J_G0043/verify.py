"""Author exact verification of D73 symbolic identities and actual matrices.

No numerical roots or Mahler-integral approximations are used. The full
all-integer forest exclusion and measure inequalities are D73's written proof.
"""
from itertools import combinations, product
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as s

t = s.Symbol('t')
A, B, C, Ci, Cj, D = s.symbols('A B C Ci Cj D')
p = t**4+A*t**3+B*t**2+A*t+1
q = t**3+C*t**2+C*t+1
qi = q.subs(C, Ci)
qj = q.subs(C, Cj)
r = t**2+D*t+1
st = t+1
c2 = t*t+t+1
P = t**6-t**5-t**3-t+1
TARGET = s.expand(st*P)


def coeffs(poly, powers):
    pp = s.Poly(s.expand(poly), t)
    return [s.expand(pp.nth(k)) for k in powers]


def char(V):
    return s.Poly((-V.inv()*V.T).charpoly(t).as_expr(), t)


def deletion(V, removed):
    keep = [i for i in range(V.rows) if i not in removed]
    return char(V.extract(keep, keep)).as_expr() if keep else s.Integer(1)


def absolute(V):
    W = s.eye(V.rows)
    for i in range(V.rows):
        for j in range(i+1, V.rows):
            W[i, j] = -abs(V[i, j])
    return W


def energy(V):
    return sum(int(V[i, j])**2 for i in range(V.rows) for j in range(i+1, V.rows))


def path_sum(n):
    return sum(t**k for k in range(n+1))


def main():
    # All six repeated/distinct path coefficient patterns and the rooted fork.
    single = path_sum(3)*p-t*c2*q
    assert coeffs(single, (6,5,4)) == [A, A+B-C, 2*A+B-2*C]
    distinct = st*c2*p-t*c2*qi-t*st**2*qj+t*t*st*r
    assert coeffs(distinct, (6, 5, 4)) == [A, 2*A+B-Ci-Cj, 3*A+2*B-2*Ci-3*Cj+D]
    same = st*c2*p-t*(c2+st**2)*q
    assert coeffs(same, (6, 5, 4)) == [A, 2*A+B-2*C-1, 3*A+2*B-5*C-1]
    repeat = st**2*p-t*st*(2*qi+qj)+2*t*t*r
    assert coeffs(repeat, (5, 4, 3)) == [A-1, 2*A+B-2*Ci-Cj, 2*A+2*B-4*Ci-2*Cj+2*D]
    fork = (t*t+1)*p-t*st*q
    assert coeffs(fork, (5, 4, 3)) == [A-1, B-C, 2*A-2*C]
    C0, C1, C2, D0, D1, D2 = s.symbols('C0 C1 C2 D0 D1 D2')
    three = st**2*p-t*st*sum(q.subs(C, v) for v in (C0, C1, C2))
    three += t*t*sum(r.subs(D, v) for v in (D0, D1, D2))-t**3
    assert coeffs(three, (5, 4, 3)) == [A-1, 2*A+B-C0-C1-C2+1,
                                                    2*A+2*B-2*C0-2*C1-2*C2+D0+D1+D2-1]
    assert s.diff(TARGET, t).subs(t, -1) == 5
    # The separately tested rank-five core / length-two tail has exactly these conditions.
    p5 = t**5+A*t**4+B*t**3+B*t**2+A*t+1
    q4 = t**4+C*t**3+D*t**2+C*t+1
    tail5 = c2*p5-t*st*q4
    assert coeffs(tail5,(6,5,4)) == [A, A+B-C, A+2*B-C-D]
    assert s.expand(tail5.subs({A:0,C:B+1,D:B})-TARGET) == 0
    # Exact residue reductions used in the all-integer proofs.
    cubic_residues = sorted({(a*a+b*b+c*c-a*b*c) % 4 for a,b,c in product(range(4), repeat=3)})
    assert cubic_residues == [0, 1, 2]
    conic_residues = [(u,v,w) for u,v,w in product(range(4), repeat=3)
                     if (u*u+v*v-u*v*w-2) % 4 == 0]
    assert all(u % 2 == v % 2 == 1 and w % 2 == 0 for u,v,w in conic_residues)
    parity_cases = 0
    for x,y,z,u,v,w in product(range(2), repeat=6):
        if u != 1 or v != 1 or w != 0:
            continue
        middle = (x*x*w*w+u*u*z*z+v*v*y*y) % 2
        deleted = (3-y*y-z*z-w*w+y*z*w) % 2
        assert middle != deleted
        parity_cases += 1

    cores = [(0,0,0,0,0,0), (1,2,-1,0,1,2), (2,-1,1,2,-2,1)]
    edges = list(combinations(range(4), 2))
    shapes = {
        'three_path': [(0,4),(4,5),(5,6)],
        'fork': [(0,4),(4,5),(4,6)],
        'two_distinct': [(0,4),(1,5),(5,6)],
        'two_same': [(0,4),(0,5),(5,6)],
        'three_distinct': [(0,4),(1,5),(2,6)],
        'three_repeat': [(0,4),(0,5),(1,6)],
        'three_same': [(0,4),(0,5),(0,6)]}
    actual_count = 0
    records = []
    for entries in cores:
        V = s.eye(4)
        for (i,j), value in zip(edges, entries):
            V[i,j] = value
        for mode, base in [('original', V), ('absolute', absolute(V))]:
            pp = char(base).as_expr()
            qq = [deletion(base, {i}) for i in range(4)]
            rr = {(i,j): deletion(base, {i,j}) for i,j in combinations(range(4), 2)}
            expected = {
                'three_path': path_sum(3)*pp-t*c2*qq[0],
                'fork': st*((t*t+1)*pp-t*st*qq[0]),
                'two_distinct': st*c2*pp-t*c2*qq[0]-t*st**2*qq[1]+t*t*st*rr[(0,1)],
                'two_same': st*c2*pp-t*(c2+st**2)*qq[0],
                'three_distinct': st*(st**2*pp-t*st*sum(qq[:3])
                                  +t*t*sum(rr[(i,j)] for i,j in combinations(range(3), 2))-t**3),
                'three_repeat': st*(st**2*pp-t*st*(2*qq[0]+qq[1])+2*t*t*rr[(0,1)]),
                'three_same': st**2*(st*pp-3*t*qq[0])}
            for name, added in shapes.items():
                W = s.eye(7)
                W[:4,:4] = base
                for i,j in added:
                    W[i,j] = -1 if mode == 'absolute' else 1
                actual = char(W).as_expr()
                assert s.expand(actual-expected[name]) == 0
                assert actual != TARGET
                assert energy(W) == energy(base)+3
                assert all(W[i,i] == 1 for i in range(7))
                actual_count += 1
            # Independently varying lengths, including one empty chain.
            attach = [0,1,2]
            lengths = [0,2,3]
            W = s.eye(9)
            W[:4,:4] = base
            cursor = 4
            for i, length in zip(attach, lengths):
                previous = i
                for _ in range(length):
                    W[previous, cursor] = -1 if mode == 'absolute' else 1
                    previous = cursor
                    cursor += 1
            summed = 0
            constant = 0
            sparse = 0
            for bits in product((0,1), repeat=3):
                subset = {i for i,b in zip(attach,bits) if b}
                minor = deletion(base, subset)
                constant += sum(abs(int(c)) for c in s.Poly(minor,t).all_coeffs())
                term = (-t)**len(subset)*minor
                spterm = term
                for length, bit in zip(lengths,bits):
                    term *= path_sum(length-bit)
                    spterm *= t**(length+1-bit)-1
                summed += term
                sparse += spterm
            actual = char(W).as_expr()
            assert s.expand(actual-summed) == 0
            assert s.expand((t-1)**3*actual-sparse) == 0
            assert energy(W) == energy(base)+5
            records.append({'entries': entries, 'mode': mode, 'chain_lengths': lengths,
                            'complete_polynomial': str(actual),
                            'A_core_coefficient_norm_sum': constant,
                            'full_measure_upper_bound': 'log('+str(8*constant)+')',
                            'rank': 9, 'energy': energy(W)})
    result = {'status':'passed', 'symbolic_coefficient_patterns': 6,
              'five_core_tail_filter_checked': True,
              'cubic_mod4_values': cubic_residues,
              'conic_mod4_solutions': conic_residues,
              'middle_parity_checks': parity_cases,
              'actual_rank7_matrix_checks_original_and_absolute': actual_count,
              'actual_three_chain_checks_including_empty_chain': records,
              'scope':'author self-check; all-integer exclusion and measure bounds require D73 proof'}
    (_J_OUTPUT / 'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'actual_three_chain_checks_including_empty_chain'}))


if __name__ == '__main__':
    main()
