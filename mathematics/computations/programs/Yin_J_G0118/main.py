"""Exact rational screen of 81 patterns and one retained full-word witness."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[3] / 'mathematics' / 'computations' / 'outputs' / HERE.name
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    v = [x * y for x in a for y in b]
    return (min(v), max(v))


def ev(a, x):
    value = (F(0), F(0))
    for d in reversed(a):
        value = add(mul(value, x), (F(d), F(d)))
    return value


def abs_interval(a):
    lo = F(0) if a[0] <= 0 <= a[1] else min(abs(a[0]), abs(a[1]))
    return lo, max(abs(a[0]), abs(a[1]))


def beta(a):
    a0, a1, a2, a3 = a
    return (-a3, a0 + a3, a1 + a3, a2 + a3)


def power(a, n):
    for _ in range(n):
        a = beta(a)
    return a


def ring_mul(a, b):
    result = [0] * 4
    p = tuple(a)
    for d in b:
        result = [result[i] + d * p[i] for i in range(4)]
        p = beta(p)
    return tuple(result)


def word_value(digits):
    result = ZERO
    for d in reversed(digits):
        result = beta(result)
        result = (result[0] + d, *result[1:])
    return result


def fraction_data(value):
    if isinstance(value, F):
        return [value.numerator, value.denominator]
    if isinstance(value, (list, tuple)):
        return [fraction_data(x) for x in value]
    if isinstance(value, dict):
        return {k: fraction_data(v) for k, v in value.items()}
    return value


def main():
    data = json.loads((HERE / 'inputs.json').read_text(encoding='utf-8'))
    p = data['polynomial_ascending']
    assert p == [1, -1, -1, -1, 1]
    x = (F(*data['beta_lower']), F(*data['beta_upper']))
    assert F(17, 10) < x[0] < x[1] < F(18, 10)
    p_lo = ev(p, (x[0], x[0]))[0]
    p_hi = ev(p, (x[1], x[1]))[0]
    assert p_lo < 0 < p_hi
    # The accepted quartic has exactly one root above 1; this bracket isolates it.
    xm1 = (x[0] - 1, x[1] - 1)
    records = []
    accepted = []
    for theta in product((-1, 0, 1), repeat=4):
        forward = mul(abs_interval(ev(theta, x)), xm1)
        reverse = mul(abs_interval(ev(tuple(reversed(theta)), x)), xm1)
        good = forward[1] < 2 and reverse[1] < 2
        bad = forward[0] > 2 or reverse[0] > 2
        assert good != bad, (theta, forward, reverse)
        records.append({'theta': theta, 'forward': forward, 'reverse': reverse, 'accepted': good})
        if good:
            accepted.append(theta)
    expected = {ZERO, (-1, 1, 0, 0), (1, -1, 0, 0),
                (0, -1, 1, 0), (0, 1, -1, 0),
                (0, 0, -1, 1), (0, 0, 1, -1),
                (-1, 1, 1, -1), (1, -1, -1, 1)}
    assert set(accepted) == expected and len(records) == 81
    inverse = (-2, -1, 0, 1)  # (beta-1)^-1
    assert ring_mul((-1, 1, 0, 0), inverse) == ONE
    factor = power(inverse, 4)
    assert factor == (-1, 0, 1, 2)
    functional = [ring_mul(factor, tuple(int(i == j) for i in range(4)))[3] for j in range(4)]
    for theta in accepted:
        assert ring_mul(inverse, theta)[3] == 0
    c = tuple(data['c'])
    assert c == (-3, 3, 1, -1)
    beta4 = ev((0, 0, 0, 0, 1), x)
    c_expanding = mul(abs_interval(ev(power(c, 4), x)), xm1)
    c_stable = mul(abs_interval(ev(tuple(reversed(c)), x)), xm1)
    assert c_expanding[1] < 1
    assert c_stable[1] < beta4[0]
    coordinate = ring_mul(factor, c)[3]
    assert coordinate == -1
    k = data['tail_length']
    assert k == 24 and len(data['left']) == len(data['right']) == k
    word = data['left'] + [0] * 4 + data['right']
    assert set(word) <= {-1, 0, 1}
    assert word_value(data['right']) == c
    assert word_value(data['left']) == tuple(-a for a in power(c, k + 4))
    assert word_value(word) == ZERO
    payload = {'root_bracket': x, 'P_at_endpoints': [p_lo, p_hi],
               'patterns': records, 'accepted': accepted,
               'functional_basis': functional, 'functional_factor': factor,
               'witness_c': c, 'witness_coordinate': coordinate,
               'witness_expanding_test': c_expanding,
               'witness_stable_test': c_stable, 'beta_fourth_interval': beta4,
               'tail_length': k, 'half_length_n': k + 2, 'word': word,
               'word_zero_count': word.count(0), 'return_verified': True}
    output = json.dumps(fraction_data(payload), indent=2) + '\n'
    assert len(output.encode('utf-8')) < 262144
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'certificate.json').write_text(output, encoding='utf-8')
    print(json.dumps({'patterns': 81, 'accepted': len(accepted), 'nonzero': len(accepted)-1,
                      'functional': functional, 'witness_coordinate': coordinate,
                      'n': k+2, 'word_zero_count': word.count(0), 'return_verified': True}))


if __name__ == '__main__':
    main()
