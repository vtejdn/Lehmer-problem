"""Separate declared twelve-map residual certificate; exact standard-library code."""
import itertools
import json
from fractions import Fraction
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from time import perf_counter

def run():
    start = perf_counter()
    records = []
    for a, b in itertools.product((0, 1, 2), (-2, -1, 1, 2)):
        columns = [(1, 0), (0, 1), (-b, -a), (a*b, a*a-b)]
        counts = {}
        for digits in itertools.product((-1, 0, 1), repeat=4):
            z = tuple(sum(d*c[j] for d,c in zip(digits, columns)) for j in range(2))
            counts[z] = counts.get(z, 0) + 2**digits.count(0)
        assert sum(counts.values()) == 256
        q00 = sum(c[0]**2 for c in columns)
        q01 = sum(c[0]*c[1] for c in columns)
        q11 = sum(c[1]**2 for c in columns)
        det = q00*q11-q01*q01
        assert det > 0
        distribution = []
        by_count = {}
        for (x,y), c in sorted(counts.items()):
            e = Fraction(q11*x*x-2*q01*x*y+q00*y*y, det)
            distribution.append([[x,y], c, e.numerator, e.denominator])
            if c not in by_count or e > by_count[c][0]:
                by_count[c] = (e, [x,y])
        cert = []
        for c, (e, z) in sorted(by_count.items()):
            left = c**e.denominator * 2**e.numerator
            right = counts[(0,0)]**e.denominator
            assert left <= right
            cert.append(dict(count=c, max_energy=[e.numerator, e.denominator], witness=z,
                             left=left, right=right, passed=True))
        records.append(dict(a=a,b=b,columns=columns,gram=[[q00,q01],[q01,q11]],determinant=det,
                            zero_count=counts[(0,0)], distribution=distribution,certificate=cert))
        assert perf_counter()-start < 60
    return dict(scope=dict(a=[0, 1, 2], b=[-2, -1, 1, 2], length=4), records=records, count=len(records), endpoint_count=sum((len(r['distribution']) for r in records)), certificate_count=sum((len(r['certificate']) for r in records)))

if __name__ == '__main__':
    r=run()
    (_J_OUTPUT / 'quadratic_certificate.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='records'}))
    for c in r['records']:
        print(c['a'],c['b'],c['zero_count'],[(z['count'],z['max_energy']) for z in c['certificate']])
