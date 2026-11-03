"""Exact Rouche certificate: the p22 control lies beyond M^3 <= 2.

Standard-library rational complex arithmetic. The disks certify roots of
q=t^24-t^17-t^12-t^7+1=Phi6*p22; multiplying by Phi6 leaves Mahler measure.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json

Q = {0: 1, 7: -1, 12: -1, 17: -1, 24: 1}
C = (F(-94095, 100000), F(-52062, 100000))
RADIUS = F(1, 100000)
LAMBDA_LOWER = F(2727, 2500)

def add(z, w):
    return z[0]+w[0], z[1]+w[1]

def mul(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]

def power(z, n):
    answer = (F(1), F(0))
    for _ in range(n):
        answer = mul(answer, z)
    return answer

def scale(z, a):
    return a*z[0], a*z[1]

def one_norm(z):
    return abs(z[0])+abs(z[1])

taylor = []
for k in range(25):
    coefficient = (F(0), F(0))
    for j, a in Q.items():
        if j >= k:
            coefficient = add(coefficient, scale(power(C, j-k), a*comb(j, k)))
    taylor.append(coefficient)

constant_upper = one_norm(taylor[0])
linear_lower = max(abs(a) for a in taylor[1])*RADIUS
tail_upper = sum(one_norm(taylor[k])*RADIUS**k for k in range(2, 25))
assert constant_upper+tail_upper < linear_lower
assert abs(C[1]) > RADIUS
modulus_squared_lower = (abs(C[0])-RADIUS)**2+(abs(C[1])-RADIUS)**2
assert modulus_squared_lower > 1
q_at_lambda_lower = sum(a*LAMBDA_LOWER**j for j, a in Q.items())
assert q_at_lambda_lower < 0
mahler_lower = LAMBDA_LOWER*modulus_squared_lower
assert mahler_lower**3 > 2

result = {
    'scope': 'Exact sufficient-condition failure M(p22)^3>2, not failure of interior or positive volume',
    'q_coefficients_ascending': [Q.get(j, 0) for j in range(25)],
    'disk_center': [str(a) for a in C],
    'disk_radius': str(RADIUS),
    'taylor_coefficients_ascending': [[str(a) for a in z] for z in taylor],
    'constant_upper_l1': str(constant_upper),
    'linear_boundary_lower': str(linear_lower),
    'higher_tail_upper_l1': str(tail_upper),
    'strict_rouche_inequality': True,
    'root_modulus_squared_lower': str(modulus_squared_lower),
    'positive_root_lower': str(LAMBDA_LOWER),
    'q_at_positive_root_lower': str(q_at_lambda_lower),
    'mahler_strict_lower': str(mahler_lower),
    'mahler_lower_cubed_minus_two': str(mahler_lower**3-2),
    'conclusion': 'M(p22)^3>2; Har15 Theorem1.1 threshold does not cover this control',
}
out=(_J_OUTPUT / 'result.json')
out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({key:result[key] for key in ('strict_rouche_inequality', 'mahler_strict_lower', 'mahler_lower_cubed_minus_two', 'conclusion')},indent=2))
