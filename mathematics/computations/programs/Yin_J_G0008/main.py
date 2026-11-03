"""Exact single-control test of L G0054's two-prime certificate.

Input: the retained Lehmer degree-ten coefficient vector from L G0004.
No parameter scan, approximate roots, or numerical determinants are used.
Independent verification is coordinator-owned; this file never imports it.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import math
import sympy as sp

t,z = sp.symbols('t z')
a = [1,1,0,-1,-1,-1,-1,-1,0,1,1]
d = len(a)-1
N = 4*d
p = sp.Poly(sum(value*t**j for j,value in enumerate(a)),t,domain=sp.ZZ)

# Multiplication by t in the power basis, column-vector convention.
A = sp.zeros(d)
for j in range(d-1):
    A[j+1,j] = 1
for j in range(d):
    A[j,d-1] = -a[j]
assert A.charpoly(t).as_expr() == p.as_expr()

def matrix_polynomial(B):
    out = sp.zeros(d)
    for coefficient in reversed(a):
        out = out*B+coefficient*sp.eye(d)
    return out

F2,F3 = matrix_polynomial(A**2),matrix_polynomial(A**3)
F = F2.row_join(F3)
for ell,block in ((2,F2),(3,F3)):
    assert all(int(entry)%ell == 0 for entry in block)

def coefficient_matrix(ell):
    out = sp.zeros(N,d)
    for column in range(d):
        for exponent,coefficient in enumerate(a):
            out[ell*exponent+column,column] = coefficient
    return out

E2,E3 = coefficient_matrix(2),coefficient_matrix(3)
E = E2.row_join(E3)
vector = sp.eye(d)[:,0]
vectors = []
for j in range(N):
    vectors.append(vector)
    vector = A*vector
V = sp.Matrix.hstack(*vectors)
assert V*E == F
assert int(E2[2*d:3*d,:].det()) == 1
assert abs(int(E[2*d:4*d,:].det())) == 1

S = E.T*E
char = sp.Poly(S.charpoly(z).as_expr(),z)
elementary = [int((-1)**j*char.nth(2*d-j)) for j in range(2*d+1)]
C = elementary[d]
det_EtE = int(S.det(method='domain-ge'))
assert elementary[-1] == det_EtE
J = int((F*F.T).det(method='domain-ge'))
G = int((V*V.T).det(method='domain-ge'))
Delta = abs(int(sp.discriminant(p.as_expr(),t)))
p_at_13_over_10 = p.eval(sp.Rational(13,10))
assert p.eval(1) == -1 and p_at_13_over_10 > 0
ratio = sp.Rational(Delta*J,N**d*C)
full_gram_ratio = sp.Rational(Delta*G,N**d)

# This exact rational solve is independent of the coordinator's Schur-block
# determinant computation of the same compressed Gram volume.
solution = S.inv(method='DM')*F.T
assert S*solution == F.T
compressed_gram = F*solution
H = sp.factor(compressed_gram.det(method='domain-ge'))
assert H.is_Rational and H>0
Hratio = sp.Rational(Delta,N**d)*H
assert sp.Rational(J,C) <= H <= G

binomial = math.comb(2*d,d)
K_lower_certificate = {
    'inference':'K >= C/binomial(2d,d); Delta*J*binomial < N^d*C excludes positive raw optimal operator-cost certificate',
    'binomial_2d_d':str(binomial),
    'left_integer':str(Delta*J*binomial),
    'right_integer':str(N**d*C),
    'strict_less':bool(Delta*J*binomial < N**d*C),
}
sqrt_certificate = {
    'inference':'K >= sqrt(det(E^T E)); compare squares',
    'left_integer':str((Delta*J)**2),
    'right_integer':str(N**(2*d)*det_EtE),
    'strict_less':bool((Delta*J)**2 < N**(2*d)*det_EtE),
}

def rational_data(value):
    value = sp.Rational(value)
    return {'numerator':str(value.p),'denominator':str(value.q)}

def matrix_data(value):
    return [[str(value[i,j]) for j in range(value.cols)] for i in range(value.rows)]

control = {
    'name':'retained_Lehmer_degree10',
    'input_provenance':'mathematics/ledger/Yin_L_G0004_v1.md, embedded inputs[lehmer] ascending coefficient vector; L G0033 Lehmer realization for the existing arithmetic scope',
    'degree':d,'coefficients_ascending':a,'N':N,
    'p_at_one':str(p.eval(1)),
    'p_at_13_over_10':rational_data(p_at_13_over_10),
    'scope_note':'The retained irreducible Salem classification supplies exactly one positive root >1 and no other expanding root; the exact endpoint signs give 1<M(p)<13/10. No fresh classification proof is supplied by this computation.',
    'discriminant_abs':str(Delta),'J':str(J),'C':str(C),'G_4d':str(G),
    'det_EtE':str(det_EtE),'det_F2':str(F2.det()),'det_F3':str(F3.det()),
    'ratio':rational_data(ratio),'ratio_less_than_one':bool(ratio<1),
    'full_gram_ratio':rational_data(full_gram_ratio),
    'full_gram_ratio_greater_than_one':bool(full_gram_ratio>1),
    'joint_floor_13_pow_d':bool(J>=13**d),
    'comparison_J_le_GC':bool(J<=G*C),
    'raw_optimal_cost_binomial_certificate':K_lower_certificate,
    'raw_optimal_cost_determinant_certificate':sqrt_certificate,
    'H':rational_data(H),'H_ratio':rational_data(Hratio),
    'H_ratio_less_than_one':bool(Hratio<1),
    'comparison_J_over_C_le_H_le_G':True,
    'elementary_coefficients_det_I_plus_z_EtE':[str(x) for x in elementary],
    'matrices':{'A':matrix_data(A),'E':matrix_data(E),'F2':matrix_data(F2),
                'F3':matrix_data(F3),'EtE':matrix_data(S),'V_4d':matrix_data(V),
                'compressed_gram_F_EtE_inverse_Ft':matrix_data(compressed_gram)},
}
payload = {
    'question':'One exact retained admissible control for the fixed two-prime, N=4d certificate; no finite parameter scan',
    'arithmetic':'exact SymPy integer/rational matrices; no floating point',
    'coefficient_order':'ascending',
    'scope':'A failing sufficient certificate does not refute Lehmer or the valid entropy upper/lower comparisons',
    'controls':[control],
}
(_J_OUTPUT / 'result.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:control[key] for key in
                ('degree','discriminant_abs','J','C','G_4d','det_EtE','ratio','H','H_ratio',
                 'ratio_less_than_one','H_ratio_less_than_one')}))
print('Raw optimal exterior cost excluded:',K_lower_certificate['strict_less'])
print('Square-root determinant cost screen:',sqrt_certificate['strict_less'])
print('Full Gram positivity survives:',control['full_gram_ratio_greater_than_one'])
