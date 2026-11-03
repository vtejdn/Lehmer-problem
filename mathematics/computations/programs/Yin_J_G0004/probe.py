"""Exploratory roots only; exact proof is main.py plus the linked ledger.

Preserves the earlier n=35, maxsteps=300, abs(complex(root))>1.000001
calculation. No certified rounding/error control is asserted.
"""
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as s

here = _J_OUTPUT
data = json.loads((here.parent / 'Yin_J_G0003' / 'result.json').read_text(encoding='utf-8'))
t = s.symbols('t')
p = s.Poly.from_list(list(reversed(data['p_coefficients_ascending'])), t)
roots = s.nroots(p, n=35, maxsteps=300)
outside = [z for z in roots if abs(complex(z)) > 1.000001]
result = {
    'scope': 'exploratory only; no rigorous root or Mahler bounds',
    'input': '../Yin_J_G0003/result.json:p_coefficients_ascending',
    'nroots_digits': 35,
    'nroots_maxsteps': 300,
    'float_modulus_filter': 1.000001,
    'display_digits': 30,
    'observed_outside_roots': [{'root': str(z), 'modulus': str(s.Abs(z).evalf(30))} for z in outside],
    'observed_mahler': str(s.prod(s.Abs(z) for z in outside).evalf(30)),
    'threshold_two_cuberoot': str(s.real_root(2, 3).evalf(30)),
}
rendered = json.dumps(result, indent=2)
(here / 'probe.json').write_text(rendered+'\n', encoding='utf-8')
print(rendered)
