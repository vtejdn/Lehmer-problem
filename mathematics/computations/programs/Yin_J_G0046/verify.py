"""Exact finite controls for D81, distinct from its all-stabilizer proof."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as s

HERE = (_J_PROGRAM / 'verify.py').parent
t, a, b = s.symbols('t a b')
P = t**6-t**5-t**3-t+1
B = s.Matrix([[1,1,0],[1,0,1],[1,0,0],[0,1,0],[0,1,0]])
V = s.eye(8)
V[:5,5:] = -B
A = V.T-V
K = s.Matrix([[1,0],[0,0],[-1,0],[0,1],[-1,-1],[0,0],[0,0],[0,0]])
G = K.T*V*K
assert G == s.Matrix([[3,1],[1,2]])
assert A*K == s.zeros(8,2)
assert B.extract([2,3,1],[0,1,2]).det() in (1,-1)
# The displayed integer solution parameterization is complete: the bottom
# three equations force x1+x2+x3=0, x1+x4+x5=0 and x2=0.
x = s.Matrix(s.symbols('x1:6'))
assert B.T*x == s.Matrix([x[0]+x[1]+x[2],x[0]+x[3]+x[4],x[1]])
assert K*s.Matrix([a,b]) == s.Matrix([a,0,-a,b,-a-b,0,0,0])
projection = s.zeros(2,8)
projection[0,0] = projection[1,3] = 1
assert projection*K == s.eye(2)
Q = K.row_join(s.eye(8)[:,[1,2,4,5,6,7]])
assert Q.det() in (1,-1)
adapted_V = Q.T*V*Q
adapted_A = Q.T*A*Q
assert adapted_A[:2,:] == s.zeros(2,8)
assert adapted_A[:,:2] == s.zeros(8,2)
assert adapted_V[:2,:2] == G
A0 = adapted_A[2:,2:]
assert A0.det() == 1
polynomial = s.Poly((t*V+V.T).det(method='domain-ge'),t)
assert polynomial.as_expr() == s.expand((t+1)**2*P)
assert P.subs(t,-1) == 5
assert s.diff((t+1)*P,t).subs(t,-1) == 5
assert s.diff(polynomial.as_expr(),t,2).subs(t,-1)/2 == G.det()*A0.det() == 5
change5 = s.Matrix([[1,1],[0,2]])
assert change5.det()%5 != 0
assert (change5.T*G*change5).applyfunc(lambda x:int(x)%5) == s.diag(3,0)
assert set((x*x)%5 for x in range(1,5)) == {1,4}

def quotient_discriminant(matrix,p=5):
    """Symmetric elimination, disc of quotient by radical; no inverse of zero."""
    m = [[int(x)%p for x in matrix.row(i)] for i in range(matrix.rows)]
    rank,disc = 0,1
    while m:
        n = len(m)
        pivot = next((i for i in range(n) if m[i][i]),None)
        if pivot is None:
            pair = next(((i,j) for i in range(n) for j in range(i+1,n) if m[i][j]),None)
            if pair is None:
                break # the whole remaining form is radical
            i,j = pair
            # Congruence replacing e_i by e_i+e_j, leaving other basis vectors.
            for k in range(n):
                m[k][i] = (m[k][i]+m[k][j])%p
            for k in range(n):
                m[i][k] = (m[i][k]+m[j][k])%p
            pivot = i
            assert m[pivot][pivot]
        order = [pivot]+[i for i in range(n) if i != pivot]
        m = [[m[i][j] for j in order] for i in order]
        c = m[0][0]
        rank += 1
        disc = disc*c%p
        inv = pow(c,-1,p)
        m = [[(m[i][j]-m[i][0]*m[0][j]*inv)%p for j in range(1,n)] for i in range(1,n)]
    square_class = 1 if pow(disc,(p-1)//2,p)==1 else -1
    return {'rank':rank,'determinant_representative':disc,'quadratic_character':square_class}

assert quotient_discriminant(G)['quadratic_character'] == -1
# This is the *necessary kernel form* for a hypothetical Z+[1], not a Z.
target_form = s.diag(5,1)
assert quotient_discriminant(target_form)['quadratic_character'] == 1

def chain(n):
    w = s.eye(n)
    for i in range(n-1):
        w[i,i+1] = -1
    if n%2:
        kernel = s.Matrix([1 if i%2==0 else 0 for i in range(n)])
        assert (w.T-w)*kernel == s.zeros(n,1)
        assert (w.T-w).rank() == n-1 and kernel[0] == 1
        gram = kernel.T*w*kernel
        assert gram == s.Matrix([[(n+1)//2]])
    else:
        assert (w.T-w).det() == 1
        gram = s.zeros(0,0)
    cp = (t*w+w.T).det(method='domain-ge').expand()
    assert cp == sum(t**k for k in range(n+1))
    return w,gram,cp

controls = []
# Odd chain9 has a nonzero integral kernel whose mod5 form is entirely radical;
# chain5 has a nonsquare one-dimensional quotient; the sum has both features.
for sizes in [[],[2],[5],[9],[5,9]]:
    parts = [chain(n) for n in sizes]
    wg = s.diag(*(z[1] for z in parts)) if parts else s.zeros(0,0)
    wc = s.prod(z[2] for z in parts)
    left = quotient_discriminant(s.diag(G,wg))
    right = quotient_discriminant(s.diag(target_form,wg))
    mid = quotient_discriminant(wg)
    assert left['rank'] == right['rank'] == mid['rank']+1
    assert left['quadratic_character'] == -right['quadratic_character']
    assert right['quadratic_character'] == mid['quadratic_character']
    controls.append({
        'neutral_chain_block_sizes':sizes,
        'rank_W':sum(sizes),
        'kernel_gram_W':[list(map(int,wg.row(i))) for i in range(wg.rows)],
        'full_cyclotomic_polynomial_W':str(s.expand(wc)),
        'energy_W':sum(n-1 for n in sizes),
        'quotient_W':mid,
        'quotient_V8_plus_W':left,
        'quotient_necessary_Z_plus_1_plus_W':right
    })

# Exercise the zero-diagonal/off-diagonal pivot branch, plus a radical part.
assert quotient_discriminant(s.Matrix([[0,1,0],[1,0,0],[0,0,0]])) == {
    'rank':2,'determinant_representative':4,'quadratic_character':1}
out = {
    'scope':'finite exact actual V8 and five neutral stabilizer controls; no rank7 construction or scan',
    'kernel_basis_columns':[list(map(int,K[:,i])) for i in range(2)],
    'complete_integer_kernel_verified_by_equations':True,
    'adapted_basis_determinant':int(Q.det()),
    'kernel_gram':[list(map(int,G.row(i))) for i in range(2)],
    'skew_quotient_determinant':int(A0.det()),
    'full_polynomial_V8':str(polynomial.as_expr()),
    'leading_coefficient_at_minus_one':5,
    'kernel_mod5_quotient':quotient_discriminant(G),
    'hypothetical_rank7_kernel_norm_forced':5,
    'necessary_Z_plus_1_kernel_mod5_quotient':quotient_discriminant(target_form),
    'original_energy':7,
    'cover_energy':14,
    'full_cover_polynomial':str(s.expand(polynomial.as_expr()**2)),
    'controls':controls,
    'all_passed':True
}
((_J_OUTPUT / 'verification.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
