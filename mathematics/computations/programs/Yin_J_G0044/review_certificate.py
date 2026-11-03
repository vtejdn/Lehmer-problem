"""Independent certificate check for D74, using radical root enclosures.

Does not import or execute author code or search for new representatives.
Uses the exact trace root (1+sqrt(13))/2, integer-square-root dyadic brackets,
termwise power enclosures and a companion-matrix transition, rather than the
author's quartic bisection, Horner intervals and explicit coefficient update.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json

HERE = (_J_PROGRAM / 'review_certificate.py').parent
DRAFT = (_J_ROOT / 'mathematics/ledger/Yin_L_G0208_v1.md')
SCALE = 1 << 128


def sqrt_bracket(x):
    n = isqrt((x.numerator*SCALE*SCALE)//x.denominator)
    lo, hi = F(n, SCALE), F(n+1, SCALE)
    assert lo*lo <= x < hi*hi
    return lo, hi


def evaluate(coefficients, domain):
    lo, hi = domain
    assert 0 < lo <= hi
    lower = upper = F(0)
    for k, a in enumerate(coefficients):
        values = (a*lo**k, a*hi**k)
        lower += min(values)
        upper += max(values)
    return lower, upper


def parsed(pair):
    return tuple(map(F, pair))


def main():
    native = [p for p in (*HERE.iterdir(), *_J_OUTPUT.iterdir()) if p.is_file() and not p.name.startswith('review_')]
    before = {p:p.read_bytes() for p in native+[DRAFT]}
    data = json.loads(((_J_OUTPUT / 'verification.json')).read_text())
    r13 = sqrt_bracket(F(13))
    trace = ((1+r13[0])/2, (1+r13[1])/2)
    rad_lo = sqrt_bracket(trace[0]**2-4)[0]
    rad_hi = sqrt_bracket(trace[1]**2-4)[1]
    beta = ((trace[0]+rad_lo)/2, (trace[1]+rad_hi)/2)
    stable = ((trace[0]-rad_hi)/2, (trace[1]-rad_lo)/2)
    assert F(17,10) < beta[0] < beta[1] < F(18,10)
    old_beta = parsed(data['root_interval'])
    assert old_beta[0] <= beta[0] <= beta[1] <= old_beta[1]
    B = 1/(beta[1]-1)
    S = beta[1]/(beta[1]-1)
    companion = ((0,0,0,-1),(1,0,0,1),(0,1,0,1),(0,0,1,1))
    initial, incoming = Counter(), Counter()
    classes = set()
    enclosure_checks = 0
    successor_count = 0
    def check_enclosures(state, record, radius_plus, radius_minus):
        nonlocal enclosure_checks
        for key, domain, radius in [('plus', beta, radius_plus), ('minus',stable,radius_minus)]:
            lo, hi = evaluate(state, domain)
            assert -radius < lo <= hi < radius
            author_lo, author_hi = parsed(record[key])
            assert author_lo <= lo <= hi <= author_hi
            enclosure_checks += 1
    assert data['number_of_representatives'] == 16
    assert data['probability_denominator'] == 64
    assert F(data['safe_box_radius']) == F(1,8)
    for record in data['representatives']:
        state = tuple(record['coefficients'])
        residue = tuple(a % 2 for a in state)
        assert residue == tuple(record['residue'])
        assert residue not in classes
        classes.add(residue)
        initial[state] += 4
        check_enclosures(state, record, F(1,8), F(1,8))
        assert len(record['successors']) == 3
        for sub, digit, weight in zip(record['successors'],(-1,0,1),(1,2,1)):
            nxt = [sum(a*b for a,b in zip(row,state)) for row in companion]
            nxt[0] += digit
            target = tuple(nxt)
            assert sub['digit'] == digit and sub['weight_units'] == weight
            assert tuple(sub['target']) == target
            incoming[target] += weight
            check_enclosures(target, sub, B, S)
            successor_count += 1
    assert classes == set(product((0,1),repeat=4))
    assert sum(initial.values()) == sum(incoming.values()) == 64
    before_q, after_q = Counter(), Counter()
    for state,mass in initial.items():
        before_q[tuple(a%2 for a in state)] += mass
    for state,mass in incoming.items():
        after_q[tuple(a%2 for a in state)] += mass
    assert before_q == after_q and set(before_q.values()) == {4}
    chars = []
    for mask in product((0,1),repeat=4):
        def exact_sign(state):
            return 1-2*(sum(a*b for a,b in zip(mask,state))%2)
        left = sum(m*exact_sign(x) for x,m in initial.items())
        right = sum(m*exact_sign(x) for x,m in incoming.items())
        assert left == right == (64 if mask == (0,0,0,0) else 0)
        chars.append({'character':list(mask),'before_units':left,'after_units':right})
    assert chars == data['all_characters']
    integer_typed_characters = all(type(row[k]) is int for row in data['all_characters']
                                    for k in ('before_units','after_units'))
    variation = F(sum(abs(initial[x]-incoming[x]) for x in initial.keys()|incoming.keys()),128)
    assert variation == F(15,16) == F(data['actual_total_variation'])
    assert len(incoming) == data['next_state_count'] == 48
    assert all(p.read_bytes()==b for p,b in before.items())
    output = {'status': 'passed', 'root_method': '128-bit dyadic radical bounds via integer square roots', 'representatives': len(initial), 'successors': successor_count, 'separately_checked_real_enclosures': enclosure_checks, 'full_parity_character_count': len(chars), 'author_character_values_integer_typed': integer_typed_characters, 'next_state_count': len(incoming), 'total_variation': str(variation), 'author_code_imported_or_rerun': False, 'search_rerun': False, 'scope': 'finite certificate only; general all-q and Fourier arguments reviewed in D74'}
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output))


if __name__=='__main__':
    main()
