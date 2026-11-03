"""Independent integer checks of the fixed Lehmer two-prime control.

Uses polynomial remainders, integer Newton identities for e_d, and the dual
Toeplitz Gram determinant. Imports neither the author program nor SymPy.
No numerical roots, parameter search, or irreducibility inference.
"""
from fractions import Fraction
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
from math import comb


def transpose(a):
    return list(map(list, zip(*a)))


def product(a, b):
    bt = transpose(b)
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def determinant(a):
    a = [row[:] for row in a]
    n = len(a)
    sign, old = 1, 1
    for k in range(n-1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        current = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j]*current-a[i][k]*a[k][j]
                value, remainder = divmod(numerator, old)
                assert not remainder
                a[i][j] = value
            a[i][k] = 0
        old = current
    return sign*a[-1][-1]


def remainder(a, p):
    a = a[:] + [0]*max(0, len(p)-1-len(a))
    d = len(p)-1
    for j in range(len(a)-1, d-1, -1):
        c = a[j]
        for k in range(d+1):
            a[j-d+k] -= c*p[k]
    return a[:d]


def toeplitz_gram(p, k):
    def correlation(j):
        return sum(p[i]*p[i+j] for i in range(len(p)-j)) if j < len(p) else 0
    return [[correlation(abs(i-j)) for j in range(k)] for i in range(k)]


p = [1,1,0,-1,-1,-1,-1,-1,0,1,1]
d = len(p)-1
N = 4*d
assert p == list(reversed(p)) and p[0] == p[-1] == 1
e_columns, f_columns = [], []
for ell in (2, 3):
    for j in range(d):
        polynomial = [0]*N
        for k, a in enumerate(p):
            polynomial[j+ell*k] = a
        e_columns.append(polynomial)
        f_columns.append(remainder(polynomial, p))
E = transpose(e_columns)
F = transpose(f_columns)
Q = product(transpose(E), E)
J = determinant(product(F, transpose(F)))
det_Q = determinant(Q)

# Compute e_d(Q) by exact Newton identities, not a characteristic polynomial.
traces = []
power = [[int(i == j) for j in range(2*d)] for i in range(2*d)]
for k in range(1, 2*d+1):
    power = product(power, Q)
    traces.append(sum(power[i][i] for i in range(2*d)))
elementary = [1]
for k in range(1, 2*d+1):
    numerator = sum((-1)**(j-1)*elementary[k-j]*traces[j-1] for j in range(1, k+1))
    value, rem = divmod(numerator, k)
    assert not rem
    elementary.append(value)
C = elementary[d]
assert elementary[-1] == det_Q

# Norm of p'(t) in Z[t]/p is the signed polynomial discriminant.
derivative = [j*p[j] for j in range(1, d+1)]
derivative_columns = [remainder([0]*j+derivative, p) for j in range(d)]
delta = abs(determinant(transpose(derivative_columns)))
G = determinant(toeplitz_gram(p, N-d))
ratio = Fraction(delta*J, N**d*C)
orbit_ratio = Fraction(delta*G, N**d)
prime_determinants = {}
for block, ell in enumerate((2, 3)):
    square = transpose(f_columns[block*d:(block+1)*d])
    assert all(x % ell == 0 for row in square for x in row)
    prime_determinants[str(ell)] = determinant(square)
    assert prime_determinants[str(ell)] != 0
    assert prime_determinants[str(ell)] % ell**d == 0

unit_minor = determinant(E[2*d:4*d])
assert abs(unit_minor) == 1
assert delta == 1332031009 and G == 18006972477
assert J >= 13**d and J <= G*C
assert C >= 1 and det_Q >= 1
operator_floor_failure = (delta*J)**2 < N**(2*d)*det_Q
operator_combinatorial_ratio = ratio*comb(2*d, d)
assert operator_combinatorial_ratio < 1

# Schur complement: abs(det [[Q,F^T],[F,0]])/det(Q)=det(F Q^-1 F^T).
block = [Q[i]+transpose(F)[i] for i in range(2*d)]
block += [F[i]+[0]*d for i in range(d)]
schur_determinant = determinant(block)
H = Fraction((-1)**d*schur_determinant, det_Q)
assert 0 < H <= G
subspace_ratio = Fraction(delta, N**d)*H
value_at_13_10 = sum(Fraction(a)*Fraction(13,10)**j for j,a in enumerate(p))
assert value_at_13_10 > 0

# Compare mathematical payload, never hashes or execution metadata.
author = json.loads((_J_OUTPUT / 'result.json').read_text(encoding='utf-8'))['controls'][0]
checks = []
def check(label, actual, expected):
    assert actual == expected, (label, actual, expected)
    checks.append(label)
for label, expected in [('degree',d),('N',N),('coefficients_ascending',p)]:
    check(label, author[label], expected)
for label, expected in [('discriminant_abs',delta),('J',J),('C',C),('G_4d',G),('det_EtE',det_Q),
                        ('det_F2',prime_determinants['2']),('det_F3',prime_determinants['3'])]:
    check(label, int(author[label]), expected)
for label, expected in [('ratio',ratio),('full_gram_ratio',orbit_ratio),('H',H),('H_ratio',subspace_ratio)]:
    v = author[label]
    check(label, Fraction(int(v['numerator']),int(v['denominator'])), expected)
check('all elementary coefficients', list(map(int,author['elementary_coefficients_det_I_plus_z_EtE'])), elementary)
for label, expected in [('E',E),('EtE',Q),('F2',transpose(f_columns[:d])),('F3',transpose(f_columns[d:]))]:
    check(label, [[int(v) for v in row] for row in author['matrices'][label]], expected)
orbit = transpose([remainder([0]*j+[1],p) for j in range(N)])
check('V_4d', [[int(v) for v in row] for row in author['matrices']['V_4d']], orbit)
companion = transpose([remainder([0]*(j+1)+[1],p) for j in range(d)])
check('A', [[int(v) for v in row] for row in author['matrices']['A']], companion)
for label, expected in [('ratio_less_than_one', ratio<1),('full_gram_ratio_greater_than_one',orbit_ratio>1),
                        ('joint_floor_13_pow_d',J>=13**d),('comparison_J_le_GC',J<=G*C),
                        ('H_ratio_less_than_one',subspace_ratio<1),('comparison_J_over_C_le_H_le_G',Fraction(J,C)<=H<=G)]:
    check(label,author[label],expected)
check('operator binomial screen', author['raw_optimal_cost_binomial_certificate']['strict_less'], operator_combinatorial_ratio<1)
check('operator determinant screen', author['raw_optimal_cost_determinant_certificate']['strict_less'], operator_floor_failure)

out = {
    'status': 'passed',
        'scope': 'Independent exact Lehmer control only; no all-degree claim',
    'coefficients_ascending': p,
    'degree': d,
    'author_payload_comparison_count': len(checks),
    'author_payload_comparisons': checks,
    'value_at_13_10': str(value_at_13_10),
    'N': N,
    'discriminant_abs': str(delta),
    'J': str(J),
    'C': str(C),
    'G_4d': str(G),
    'det_EtE': str(det_Q),
    'unit_maximal_minor': unit_minor,
    'prime_determinants': {k: str(v) for k, v in prime_determinants.items()},
    'newton_traces': list(map(str, traces)),
    'newton_elementary': list(map(str, elementary)),
    'ratio_numerator': str(ratio.numerator),
    'ratio_denominator': str(ratio.denominator),
    'ratio_less_than_one': ratio < 1,
    'direct_gram_ratio': str(orbit_ratio),
    'operator_determinant_floor_failure': operator_floor_failure,
    'operator_combinatorial_upper_ratio': str(operator_combinatorial_ratio),
    'operator_combinatorial_failure': operator_combinatorial_ratio < 1,
    'coefficient_subspace_H': str(H),
    'coefficient_subspace_ratio': str(subspace_ratio),
    'coefficient_subspace_positive': subspace_ratio > 1,
    'schur_block_determinant': str(schur_determinant),
    'operator_floor_comparison': {
        'left': str((delta*J)**2),
        'right': str(N**(2*d)*det_Q),
    },
}
(_J_OUTPUT / 'verification.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
print(json.dumps(out, indent=2))
