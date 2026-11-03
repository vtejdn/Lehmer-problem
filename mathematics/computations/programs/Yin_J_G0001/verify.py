"""Independent exact reconstruction; does not import main.py or its helpers."""
import json
import math
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as sp

root = _J_OUTPUT
data = json.loads((root / 'result.json').read_text(encoding='utf-8'))
x, t = sp.symbols('x t')
rows = {(r['n'], r['k']): r for r in data['all_rows']}
expected_pairs = {(n, k) for n in range(2, 14) for k in range(1, n)
                  if math.gcd(n, k) == 1}
assert set(rows) == expected_pairs and len(rows) == 57
accepted = set()
factors = {}
trace_polys = {}
for n, k in sorted(expected_pairs):
    h = sp.Poly(2*sp.chebyshevt(n, x/2)-2*sp.chebyshevt(n-k, x/2)-1, x)
    trace_polys[(n, k)] = h
    row = rows[(n, k)]
    assert list(reversed(h.all_coeffs())) == row['H_coefficients_ascending']
    assert h.gcd(h.diff()).degree() == row['derivative_gcd_degree'] == 0
    assert all(str(h.eval(a)) == row['endpoint_values'][str(a)] for a in [-2, 2, 3])
    fac = sp.factor_list(h)[1]
    def count(a, b):
        return sum(int(f.count_roots(a, b))*multiplicity for f, multiplicity in fac)
    counts = {'below_minus_two': count(-sp.oo, -2),
              'inside_minus_two_two': count(-2, 2),
              'above_two': count(2, sp.oo),
              'above_three': count(3, sp.oo)}
    counts['nonreal'] = n-sum(counts[z] for z in ['below_minus_two', 'inside_minus_two_two', 'above_two'])
    assert counts == row['root_counts_with_multiplicity']
    ok = counts == {'below_minus_two': 0, 'inside_minus_two_two': n-1,
                    'above_two': 1, 'above_three': 0, 'nonreal': 0}
    assert ok == row['is_Salem_polynomial'] == row['in_source_Table1']
    if ok:
        accepted.add((n, k))
        q = sp.Poly(t**(2*n)-t**(2*n-k)-t**n-t**k+1, t)
        noncyc = [(f, m) for f, m in sp.factor_list(q)[1] if not f.is_cyclotomic]
        assert len(noncyc) == 1
        p, multiplicity = noncyc[0]
        assert multiplicity == 1 and p.degree() >= 4
        assert p.all_coeffs() == list(reversed(p.all_coeffs()))
        factors[(n, k)] = tuple(map(int, p.all_coeffs()))
assert len(accepted) == 17 and len(set(factors.values())) == 13

seen = set()
previous_upper = sp.Rational(2)
for group in data['exact_groups_and_isolations']:
    pairs = {tuple(z) for z in group['pairs']}
    assert not (seen & pairs)
    seen |= pairs
    representative = min(pairs)
    assert pairs == {p for p in accepted if factors[p] == factors[representative]}
    lower, upper = map(sp.Rational, (group['trace_lower'], group['trace_upper']))
    assert previous_upper < lower < upper < 3
    assert trace_polys[representative].count_roots(lower, upper) == 1
    previous_upper = upper
assert seen == accepted
minimum = {tuple(z) for z in data['exact_groups_and_isolations'][0]['pairs']}
assert minimum == {(6, 5), (7, 3)}
lehmer = sp.Poly(t**10+t**9-t**7-t**6-t**5-t**4-t**3+t+1, t)
assert factors[(6, 5)] == tuple(map(int, lehmer.all_coeffs()))
assert sp.expand(lehmer.as_expr()*(t*t-t+1)) == t**12-t**7-t**6-t**5+1
report = {'candidate_records_verified': len(rows), 'accepted_polynomials': len(accepted),
          'distinct_irreducible_Salem_factors': len(set(factors.values())),
          'all_source_pair_flags_match': True,
          'all_isolating_intervals_and_group_order_verified': True,
          'minimum_is_standard_Lehmer_factor': True,
          'author_program_imported': False,
          'analytic_large_degree_reduction_checked_by_program': False}
(root / 'verification.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
print(json.dumps(report, indent=2))
