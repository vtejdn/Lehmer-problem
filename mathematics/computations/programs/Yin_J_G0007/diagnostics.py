"""Exploratory limiting-integral diagnostics; not certified bounds.

This reproduces the disposable initial check which selected the analytic route.
mpmath quadrature crosses a threshold cusp, so the displayed precision is not
a rigorous accuracy statement. No proof uses these values.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import mpmath as m
m.mp.dps=30
results=[]
for n in [3,5,7,9,11,21]:
    def f(u):
        a=m.mpf(n)/2 if not u else abs(m.sin(n*u))/(2*m.sin(u))
        return m.acosh(a) if a>1 else m.mpf(0)
    points=sorted(set([m.mpf(0),m.pi/6]+[j*m.pi/(2*n) for j in range(1,n) if j*m.pi/(2*n)<m.pi/6]))
    value=2/m.pi*m.quad(f,points)
    results.append({'odd_frequency':n,'r':(n-1)//2,
                    'uncertified_log_measure':str(value),
                    'uncertified_measure':str(m.exp(value))})
out={'status':'exploratory only; not certified','mpmath_precision':30,
     'scope':'Six limiting analytic integrals; not a finite polynomial/root sweep',
     'values':results}
(_J_OUTPUT / 'diagnostics.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
