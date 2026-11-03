"""Construct and certify one bounded quartic finite-character relaxation.

All discovery and verification arithmetic is integral or Fraction arithmetic.
This is a finite witness construction, not an exhaustive state-space theorem.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def polynomial(x):
    return x**4-x**3-x**2-x+1


def root_interval():
    lo, hi = F(17, 10), F(18, 10)
    assert polynomial(lo) < 0 < polynomial(hi)
    # Strict derivative positivity over this entire bracket.
    assert 4*lo**3-3*hi**2-2*hi-1 > 0
    for _ in range(80):
        mid = (lo+hi)/2
        if polynomial(mid) < 0:
            lo = mid
        else:
            hi = mid
    return lo, hi


def interval_product(left, right):
    values = [x*y for x in left for y in right]
    return min(values), max(values)


def interval_evaluate(coefficients, interval):
    result = F(0), F(0)
    for coefficient in reversed(coefficients):
        result = interval_product(result, interval)
        result = result[0]+coefficient, result[1]+coefficient
    return result


def step(coefficients, digit):
    a, b, c, d = coefficients
    # beta^4=beta^3+beta^2+beta-1.
    return -d+digit, a+d, b+d, c+d


def residue(coefficients):
    return tuple(value % 2 for value in coefficients)


def str_interval(interval):
    return [str(value) for value in interval]


def main():
    root = root_interval()
    inverse = 1/root[1], 1/root[0]
    midpoint = sum(root)/2
    u = midpoint+1/midpoint
    eps = F(1, 8)
    B_lower = 1/(root[1]-1)
    S_lower = root[1]/(root[1]-1)
    assert root[1]*eps+1 < B_lower
    assert inverse[1]*eps+1 < S_lower
    representatives = {}
    visits = 0
    # In the real quadratic representation x=E0+beta*E1, the
    # nearest-integer targets below make both E0 and E1 small.
    for radius in range(201):
        for a2 in range(-radius, radius+1):
            for a3 in range(-radius, radius+1):
                if max(abs(a2), abs(a3)) != radius:
                    continue
                a0_center = round(a2+u*a3)
                a1_center = round(-u*a2-(u+2)*a3)
                for off0, off1 in product((-1, 0, 1), repeat=2):
                    coefficients = (a0_center+off0, a1_center+off1, a2, a3)
                    visits += 1
                    key = residue(coefficients)
                    if key in representatives:
                        continue
                    plus = interval_evaluate(coefficients, root)
                    if not -eps < plus[0] <= plus[1] < eps:
                        continue
                    minus = interval_evaluate(coefficients, inverse)
                    if not -eps < minus[0] <= minus[1] < eps:
                        continue
                    representatives[key] = (coefficients, plus, minus)
        if len(representatives) == 16:
            break
    assert len(representatives) == 16, 'bounded witness search incomplete'

    incoming = Counter()
    initial = Counter()
    records = []
    for key, (coefficients, plus, minus) in sorted(representatives.items()):
        initial[coefficients] = 4  # common probability denominator64
        successors = []
        for digit, weight in ((-1, 1), (0, 2), (1, 1)):
            target = step(coefficients, digit)
            target_plus = interval_evaluate(target, root)
            target_minus = interval_evaluate(target, inverse)
            assert -B_lower < target_plus[0] <= target_plus[1] < B_lower
            assert -S_lower < target_minus[0] <= target_minus[1] < S_lower
            incoming[target] += weight
            successors.append({'digit': digit, 'weight_units': weight, 'target': target,
                               'plus': str_interval(target_plus), 'minus': str_interval(target_minus)})
        records.append({'residue': key, 'coefficients': coefficients,
                        'plus': str_interval(plus), 'minus': str_interval(minus),
                        'successors': successors})
    assert sum(initial.values()) == sum(incoming.values()) == 64
    initial_quotient = Counter()
    next_quotient = Counter()
    for state, mass in initial.items(): initial_quotient[residue(state)] += mass
    for state, mass in incoming.items(): next_quotient[residue(state)] += mass
    assert initial_quotient == next_quotient
    assert set(initial_quotient.values()) == {4}

    character_records = []
    for character in product((0, 1), repeat=4):
        def sign(state): return (-1)**sum(a*b for a, b in zip(character, state))
        before = sum(mass*sign(state) for state, mass in initial.items())
        after = sum(mass*sign(state) for state, mass in incoming.items())
        assert before == after == (64 if not any(character) else 0)
        character_records.append({'character': character, 'before_units': before, 'after_units': after})
    discrepancy = sum(abs(initial[state]-incoming[state]) for state in initial.keys() | incoming.keys())
    assert discrepancy > 0
    variation = F(discrepancy, 128)
    output = {'root_interval': str_interval(root), 'safe_box_radius': str(eps),
              'search_a2_a3_radius': radius, 'candidate_visits': visits,
              'number_of_representatives': len(records),
              'probability_denominator': 64, 'representatives': records,
              'all_characters': character_records,
              'actual_total_variation': str(variation),
              'next_state_count': len(incoming),
              'scope': 'finite original-row Fourier relaxation; not an actual stationary law'}
    Path(__file__).with_name('verification.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({key: value for key, value in output.items()
                      if key not in ('representatives', 'all_characters')}))


if __name__ == '__main__': main()
