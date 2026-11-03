"""Exact finite controls for D77; not a rerun or completion of Search.cs."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as s

HERE = Path(__file__).resolve().parent
t, u, lam = s.symbols('t u lam')
P = t**6-t**5-t**3-t+1
B = s.Matrix([[1,1,0],[1,0,1],[1,0,0],[0,1,0],[0,1,0]])
A = B.T*B
assert A == s.Matrix([[3,1,1],[1,3,0],[1,0,1]])
assert A.charpoly(lam).as_expr() == lam**3-7*lam**2+13*lam-5
assert s.expand(((u+2)*s.eye(3)-A).det()) == u**3-u**2-3*u+1
assert s.expand(t**3*(u**3-u**2-3*u+1).subs(u,t+1/t)) == P
V = s.eye(8)
V[:5,5:] = -B
p = s.Poly((t*V+V.T).det(method='domain-ge'),t)
assert p.as_expr() == s.expand((t+1)**2*P)
energy = sum(V[i,j]**2 for i in range(8) for j in range(i+1,8))
assert energy == 7 and all(V[i,i] == 1 for i in range(8))
assert all(V[i,j] in (0,-1) for i in range(8) for j in range(i+1,8))
assert (V+V.T).det() == -4
# Explicit doubled matrix, in vertex-pair order, swapping sheets at each
# negative edge, as in the retained signed-cover convention.
W = s.eye(16)
for i in range(8):
    for j in range(i+1,8):
        if V[i,j] == -1:
            W[2*i,2*j+1] = W[2*i+1,2*j] = -1
wp = s.Poly((t*W+W.T).det(method='domain-ge'),t)
assert wp.as_expr() == s.expand((t+1)**4*P**2)
assert sum(W[i,j]**2 for i in range(16) for j in range(i+1,16)) == 14

# Exact constants of the universal written energy argument; these arithmetic
# checks do not replace the signature/gluing or eigenvalue inequalities.
trial = (Q(2,3)/3)**3*((14+Q(2,3))/4)**4
square_lower = Q(2,3)**2/3+(14+Q(2,3))**2/4
energy_lower = (square_lower-28)/2
assert trial == Q(117128,59049) < 2
assert square_lower == Q(1456,27)
assert energy_lower == Q(350,27) and 12 < energy_lower < 13
allowed = [k for k in range(1,8,2) if (7-2*k)%8 in (1,7)]
assert allowed == [3,7] # k=7 is excluded by the positive diagonal in the proof.
assert s.expand((t+1)*P) == t**7-t**5-t**4-t**3-t**2+1

saved = json.loads((HERE/'search.json').read_text())
assert saved['matrix_cap'] == saved['signed_matrices_examined'] == 250000
assert saved['connected_supports_started'] == 62501
assert saved['trace_filter_passes'] == 70032
assert saved['cap_reached'] is True and saved['found'] is False
out = {
    'scope': 'exact symbolic rank8 and doubled control plus rational bounds; not a C# rerun',
    'rank8_matrix': [list(map(int,V.row(i))) for i in range(8)],
    'rank8_polynomial_ascending': list(map(int,reversed(p.all_coeffs()))),
    'rank8_energy': int(energy),
    'rank8_endpoint_determinant': -4,
    'cover_rank': 16,
    'cover_polynomial_ascending': list(map(int,reversed(wp.all_coeffs()))),
    'cover_energy': 14,
    'trial_product': str(trial),
    'square_sum_lower': str(square_lower),
    'energy_strict_lower': str(energy_lower),
    'required_integer_energy': 13,
    'negative_indices_permitted_before_positive_diagonal': allowed,
    'search_scope_read_and_checked': True,
    'passed': True
}
(HERE/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
