"""Complete independent J73 verification; scope/cap declared in readme before run.

No author-module or SymPy imports.  Enumerates binary words then autocorrelates
integer fibers, independently classifies degree<=5 polynomials, and solves
Gram systems by Fraction elimination.  Reuses the reviewer-owned J71 counting
idea.  D161 presence is optional after promotion. No hashes/historical gates.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time

HERE = (_J_PROGRAM / 'review_independent.py').parent
CAP = 120
NATIVE = ('readme.md', 'probe.py', 'result.json',
          'certificate_quadratic.py', 'quadratic_certificate.json')


def identical(a, b):
    assert type(a) is type(b), (type(a), type(b))
    if isinstance(a, dict):
        assert a.keys() == b.keys(), (a.keys(), b.keys())
        for k in a:
            identical(a[k], b[k])
    elif isinstance(a, list):
        assert len(a) == len(b)
        for x, y in zip(a, b):
            identical(x, y)
    else:
        assert a == b, (a, b)


def remainder(p, f):
    # All divisors here are monic. Ascending integer coefficients throughout.
    r = list(p)
    for j in range(len(r)-len(f), -1, -1):
        c = r[j+len(f)-1]
        for i, v in enumerate(f):
            r[j+i] -= c*v
    return r[:len(f)-1]


def irreducible(p):
    # Rational-root theorem plus complete bounded quadratic-divisor enumeration.
    for a in (-1, 1):
        if not any(remainder(p, [a, 1])):
            return False
    if len(p)-1 >= 4:
        for a, b in product(range(-4, 5), (-1, 1)):
            if not any(remainder(p, [b, a, 1])):
                return False
    return True


def columns(p, n):
    return [tuple(remainder([0]*j+[1]+[0]*max(0, len(p)-2-j), p))
            for j in range(n)]


def autocorrelation(cols):
    d = len(cols[0])
    nu = Counter()
    for mask in range(1 << len(cols)):
        z = tuple(sum(cols[k][i] for k in range(len(cols)) if mask >> k & 1)
                  for i in range(d))
        nu[z] += 1
    mu = Counter()
    for x, cx in nu.items():
        for y, cy in nu.items():
            mu[tuple(a-b for a, b in zip(x, y))] += cx*cy
    assert sum(nu.values()) == 2**len(cols)
    assert sum(mu.values()) == 4**len(cols)
    assert all(mu[z] == mu[tuple(-x for x in z)] for z in mu)
    return mu


def gram_inverse(cols):
    d = len(cols[0])
    q = [[sum(c[i]*c[j] for c in cols) for j in range(d)] for i in range(d)]
    a = [[F(v) for v in row]+[F(i == j) for j in range(d)]
         for i, row in enumerate(q)]
    determinant = F(1)
    for i in range(d):
        pivot = a[i][i]
        assert pivot > 0  # All leading principal Gram minors are positive.
        determinant *= pivot
        a[i] = [v/pivot for v in a[i]]
        for j in range(d):
            if j != i:
                c = a[j][i]
                a[j] = [u-c*v for u, v in zip(a[j], a[i])]
    assert determinant.denominator == 1
    inv = [row[d:] for row in a]
    # Explicit two-sided multiplication is independent of endpoint comparisons.
    assert all(sum(q[i][k]*inv[k][j] for k in range(d)) == (i == j)
               for i in range(d) for j in range(d))
    return q, int(determinant), inv


def energies(cols, counts):
    q, det, inv = gram_inverse(cols)
    d = len(q)
    # Convert the separately obtained rational inverse to an integral numerator
    # solely to avoid repeated Fraction allocations for170,931 endpoint values.
    adj = [[int(x*det) for x in row] for row in inv]
    assert all(F(adj[i][j], det) == inv[i][j]
               for i in range(d) for j in range(d))
    out = []
    for z, count in sorted(counts.items()):
        value = F(sum(z[i]*adj[i][j]*z[j] for i in range(d) for j in range(d)), det)
        out.append([list(z), count, value.numerator, value.denominator])
    return q, det, out


def run():
    start = time.perf_counter()
    before = {n: (((_J_PROGRAM if n in ('certificate_quadratic.py', 'probe.py', 'readme.md', 'review_independent.py') else _J_OUTPUT) / n)).read_bytes() for n in NATIVE}
    draft = (_J_ROOT / 'mathematics/drafts/Yin_D_G0161.md')
    author = draft.read_bytes() if draft.exists() else None
    box = json.loads(before['result.json'])
    residual = json.loads(before['quadratic_certificate.json'])
    expected_records, excluded = [], []
    classifications = []
    endpoint_count, binary_words = 0, 0
    for d in range(2, 6):
        for const in (-1, 1):
            for middle in product((-1, 0, 1), repeat=d-1):
                p = [const, *middle, 1]
                irr = irreducible(p)
                classifications.append([p, irr])
                if not irr:
                    excluded.append(p)
                    continue
                n = d+2
                cols = columns(p, n)
                assert len(cols) == n and all(len(c) == d for c in cols)
                counts = autocorrelation(cols)
                q, det, distribution = energies(cols, counts)
                zero = counts[(0,)*d]
                payload = []
                for z, c, a, b in distribution:
                    passed = c**b * 2**a <= zero**b
                    assert passed
                    payload.append([z, c, a, b, passed])
                r0, r1 = p+[0], [0]+p
                assert all(sum(r[j]*cols[j][i] for j in range(n)) == 0
                           for r in (r0, r1) for i in range(d))
                expected_records.append(dict(coefficients=p, degree=d, length=n,
                    columns=[list(c) for c in cols], covariance_gram=q,
                    determinant=det, relation_overlap=[j for j in range(n) if r0[j] and r1[j]],
                    zero_count=zero, distribution=payload, failure_count=0))
                endpoint_count += len(distribution)
                binary_words += 2**n
                assert time.perf_counter()-start < CAP
    assert len(classifications) == 240 and len(expected_records) == 155
    assert endpoint_count == 170931
    expected_box = dict(scope=dict(degrees=[2, 3, 4, 5], constants=[-1, 1], middle=[-1, 0, 1], monic=True, irreducible_over='QQ', length='d+2', original_numerator_weights=[1, 2, 1]), records=expected_records, excluded_reducible=excluded, failures=[], polynomial_count=155, endpoint_count=endpoint_count, total_box_count=240, universal_profile_proved=False)
    identical(box, expected_box)
    pass

    cert_records = []
    for a, b in product((0,1,2), (-2,-1,1,2)):
        cols = columns([b,a,1], 4)
        counts = autocorrelation(cols)
        q, det, distribution = energies(cols, counts)
        zero = counts[(0,0)]
        groups = {}
        for z, c, num, den in distribution:
            e = F(num,den)
            if c not in groups or e > groups[c][0]:
                groups[c] = (e,z)
            assert c**den * 2**num <= zero**den
        certificates = []
        for c, (e,z) in sorted(groups.items()):
            left, right = c**e.denominator * 2**e.numerator, zero**e.denominator
            assert left <= right
            certificates.append(dict(count=c, max_energy=[e.numerator,e.denominator],
                witness=z, left=left, right=right, passed=True))
        cert_records.append(dict(a=a,b=b,columns=[list(c) for c in cols],gram=q,
            determinant=det,zero_count=zero,distribution=distribution,certificate=certificates))
        assert time.perf_counter()-start < CAP
    expected_residual = dict(scope=dict(a=[0, 1, 2], b=[-2, -1, 1, 2], length=4), records=cert_records, count=12, endpoint_count=sum((len(r['distribution']) for r in cert_records)), certificate_count=sum((len(r['certificate']) for r in cert_records)))
    assert expected_residual['endpoint_count'] == 560
    assert expected_residual['certificate_count'] == 98
    identical(residual, expected_residual)
    pass
    pass
    assert all((((_J_PROGRAM if n in ('certificate_quadratic.py', 'probe.py', 'readme.md', 'review_independent.py') else _J_OUTPUT) / n)).read_bytes() == data for n,data in before.items())
    if author is not None:
        assert draft.read_bytes() == author
    elapsed = time.perf_counter()-start
    assert elapsed < CAP
    return dict(passed=True, classification_method='complete monic integer divisors degree1/2; no SymPy', counting_method='explicit fair binary words, then full fiber autocorrelation', gram_method='independent rational Gaussian elimination', complete_classification=classifications, box_polynomials=240, retained_irreducibles=155, excluded_reducibles=len(excluded), binary_words=binary_words, box_endpoint_inequalities=endpoint_count, residual_maps=12, residual_endpoints=560, residual_compressed_certificates=98, all_nontiming_mathematical_payload_fields_and_types_matched=True, author_program_imported=False, external_irreducibility_oracle=False, claimed_new_theorem=False)


if __name__ == '__main__':
    result = run()
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'complete_classification'}))
