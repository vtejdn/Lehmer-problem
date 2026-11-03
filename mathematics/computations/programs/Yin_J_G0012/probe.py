"""Retained bounded diagnostics for the explicit Bre20 p.31 example.

The proof draft gives an enumeration-free exact argument. Numerical roots below
are exploratory only. This reproduces all consequential inline probes, with
the final compact rational endpoints added. No parameter scan is performed.
"""
import json
from fractions import Fraction as F
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as s

x = s.symbols('x')
p = x**6+x**5+x**4-x**3+x**2+x+1
a = [1, 1, 1, -1, 1, 1, 1]
v = (1, 0, 0, 0, 0, 0)
pw = []
for j in range(8):
    pw.append(v)
    z = v[-1]
    v = tuple((v[i-1] if i else 0)-z*a[i] for i in range(6))
fibers = {}
for n in range(256):
    value = tuple(sum(((n >> j) & 1)*pw[j][i] for j in range(8)) for i in range(6))
    fibers.setdefault(value, []).append(n)

def T(u):
    return u**3+u**2-2*u-3

def G(m,u):
    z = m+1/m
    return z*z+(2-u*u-u)*z+1-u*u

old_us = [F(15468,10000), F(15469,10000)]
old_ms = [F(19961,10000), F(19962,10000), F(2)]
out = {
    'scope': 'one retained Bre20 p.31 example; exact checks plus labeled numerical diagnostics',
    'coefficients_ascending': a,
    'factor_list_exact_library_output': str(s.factor_list(p)),
    'discriminant': str(s.discriminant(p,x)),
    'numerical_roots_exploratory_default_15_digits': [str(z) for z in s.nroots(p)],
    'powers_mod_p': pw,
    'support_size_n8': len(fibers),
    'nontrivial_fibers_bitmask_low_power_first': sorted(z for z in fibers.values() if len(z)>1),
    'initial_endpoint_probes': [
        {'u': str(u), 'T': str(T(u)), 'G': {str(m):str(G(m,u)) for m in old_ms}}
        for u in old_us
    ],
    'initial_M8_minus_252': str(F(19961,10000)**8-252),
    'discarded_coarse_upper_u': {'u':'31/20','T':str(T(F(31,20))),'G_M2':str(G(F(2),F(31,20)))},
    'final_certificate': {
        'u_lower':'3867/2500','u_upper':'1547/1000','M_lower':'511/256','M_upper':'2',
        'T_u_lower':str(T(F(3867,2500))),
        'T_u_upper':str(T(F(1547,1000))),
        'G_Mlower_ulower':str(G(F(511,256),F(3867,2500))),
        'G_Mupper_uupper':str(G(F(2),F(1547,1000))),
    }
}
target = (_J_OUTPUT / 'probe.json')
target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out['final_certificate'],indent=2))
print('support_size_n8 =',len(fibers))
print('nontrivial_fibers =',out['nontrivial_fibers_bitmask_low_power_first'])
