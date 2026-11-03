"""Independent whole-certificate review of J129's exact bounded question.

No contributor imports and no writes to author outputs.  Whole traces use
explicit binomial coefficients, while arithmetic uses four-coefficient binary
convolution and Euclidean inverses.  The fixed 320 sources, their specified
lifts, complete normal form and precisely epsilon=0,1 are checked here.
"""

import json
from collections import deque
from functools import lru_cache
from math import comb, gcd
from pathlib import Path


def divide(a, b):
    assert isinstance(a, int) and a >= 0 and b > 0
    quotient = 0
    degree = b.bit_length()
    while a and a.bit_length() >= degree:
        shift = a.bit_length() - degree
        quotient ^= 1 << shift
        a ^= b << shift
    return quotient, a


def rem(a, modulus):
    return divide(a, modulus)[1]


@lru_cache(maxsize=512)
def block_products(b):
    # Exact products by the sixteen polynomials of degree below four.
    values = [0]
    for bit in range(4):
        values += [v ^ (b << bit) for v in values]
    return tuple(values)


def multiply(a, b, modulus=None):
    value, shift = 0, 0
    table = block_products(b)
    while a:
        value ^= table[a & 15] << shift
        a >>= 4
        shift += 4
    return rem(value, modulus) if modulus else value


def square(a, modulus=None):
    answer = 0
    while a:
        bit = a & -a
        answer ^= 1 << (2*(bit.bit_length()-1))
        a ^= bit
    return rem(answer, modulus) if modulus else answer


def power(a, n, modulus=None):
    result = 1
    while n:
        if n & 1:
            result = multiply(result, a, modulus)
        n >>= 1
        a = square(a, modulus)
    return result


def inverse(a, modulus):
    old_r, r, old_s, s = modulus, a, 0, 1
    while r:
        q, remainder = divide(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s ^ multiply(q, s)
    assert old_r == 1
    result = rem(old_s, modulus)
    assert multiply(a, result, modulus) == 1
    return result


@lru_cache(maxsize=None)
def whole_b(n):
    """B_(2d+1)=F_(d+1)+F_d; F_(j+1)=sum binom(j-i,i) X^(j-2i)."""
    assert n > 0 and n & 1
    d, result = (n-1)//2, 0
    for j in (d, d-1):
        if j < 0:
            continue
        for i in range(j//2+1):
            if comb(j-i, i) & 1:
                result ^= 1 << (j-2*i)
    assert result & 1 and result.bit_length()-1 == d
    return result


def compose(a, b):
    result = 0
    for i in reversed(range(a.bit_length())):
        result = multiply(result, b) ^ ((a >> i) & 1)
    return result


PHI = 7
X24 = 1 << 24
PHI48 = power(PHI, 48)
MODULUS = multiply(X24, PHI48)
PRE = multiply(X24, power(PHI, 49))


def first_coordinate(a):
    assert a & 1 and rem(a, PHI) == 1
    low = rem(a ^ 1, X24)
    if low:
        return (low & -low).bit_length()-2
    primary, order = rem(a, PHI48) ^ 1, 0
    while primary:
        primary, digit = divide(primary, PHI)
        if digit:
            assert order > 0
            return 23 + 2*(order-1) + (0 if digit & 1 else 1)
        order += 1
    return None


def matrix_multiply(a, b, modulus):
    return tuple(tuple(multiply(a[i][0], b[0][j], modulus) ^
                       multiply(a[i][1], b[1][j], modulus)
                       for j in range(2)) for i in range(2))


def matrix_period(modulus):
    result, a, n = ((1, 0), (0, 1)), ((2, 1), (1, 0)), 320
    while n:
        if n & 1:
            result = matrix_multiply(result, a, modulus)
        a = matrix_multiply(a, a, modulus)
        n >>= 1
    assert result == ((1, 0), (0, 1))


def main():
    home = Path(__file__).resolve().parent
    out = home.parents[2] / 'computations' / 'outputs' / home.name
    data = json.loads((out / 'certificate.json').read_text(encoding='utf-8'))
    assert data['phi'] == PHI and data['M'] == MODULUS and data['predivision_M'] == PRE
    assert data['exponent'] == 192 and data['ambient_order'] == 3*2**117
    assert PHI48 == sum(1 << j for j in (0, 16, 48, 80, 96))
    for modulus in (MODULUS, PRE):
        matrix_period(modulus)
    rows = data['rows']
    expected = [('B', n) for n in range(1, 640, 2) if n % 5]
    expected += [('D', 5*r) for r in range(1, 128, 2)]
    assert [(row['kind'], row['n']) for row in rows] == expected
    assert len(rows) == 320
    chi = multiply(2, square(PHI))
    generators = []
    for row in rows:
        n, m = row['n'], row['m']
        original, lifted = whole_b(n), whole_b(m)
        if row['kind'] == 'B':
            assert m == (n if n % 3 else n+640) and m <= 1279 and gcd(m, 15) == 1
        else:
            r = n//5
            k = next(k for k in range(3) if gcd(r+128*k, 15) == 1)
            ell = r+128*k
            assert row['k'] == k and row['ell'] == ell and m == 5*ell and m <= 1915
            predivided, pre_remainder = divide(rem(original, PRE), PHI)
            original, original_remainder = divide(original, PHI)
            lifted, lifted_remainder = divide(lifted, PHI)
            assert pre_remainder == original_remainder == lifted_remainder == 0
            assert predivided == rem(original, MODULUS)
            assert lifted == compose(whole_b(ell), chi)
        value = rem(original, MODULUS)
        assert value == rem(lifted, MODULUS) == row['value']
        assert value & 1 and rem(value, PHI) != 0
        assert power(value, 192, MODULUS) == 1
        generators.append(value)
    print('Reconstructed all 320 source rows, exact lifts/divisions/compositions and both periods.', flush=True)

    group = data['group']
    assert group['modulus'] == MODULUS and group['generators'] == generators
    b3_index = next(i for i, r in enumerate(rows) if (r['kind'], r['n']) == ('B', 3))
    assert group['b3_index'] == b3_index and generators[b3_index] == 3
    teich = power(3, 64, MODULUS)
    assert group['teichmuller'] == teich and rem(teich, X24) == 1
    assert teich != 1 and power(teich, 3, MODULUS) == 1
    tpowers = [power(teich, i, MODULUS) for i in range(3)]
    residues = {rem(value, PHI): i for i, value in enumerate(tpowers)}
    assert len(residues) == 3
    bits = [p['bit'] for p in group['pivots']]
    assert bits == [i for i in range(117) if i not in (28, 36, 52, 84)]
    assert len(bits) == 113 and group['order'] == 3*2**113
    pivots = {p['bit']: p['value'] for p in group['pivots']}
    pivot_inverses = {i: inverse(p, MODULUS) for i, p in pivots.items()}
    squares = [[power(g, 1 << j, MODULUS) for j in range(8)] for g in generators]

    def expression(e):
        assert len(e) == 320
        result = 1
        for exponent, powers in zip(e, squares):
            assert type(exponent) is int and 0 <= exponent < 192
            for j in range(8):
                if exponent & (1 << j):
                    result = multiply(result, powers[j], MODULUS)
        return result

    def remove_residue(value):
        r = residues[rem(value, PHI)]
        return multiply(value, tpowers[(-r) % 3], MODULUS)

    def reduce(value):
        value, trace = remove_residue(value), []
        while (coordinate := first_coordinate(value)) in pivots:
            trace.append(coordinate)
            value = multiply(value, pivot_inverses[coordinate], MODULUS)
            next_coordinate = first_coordinate(value)
            assert next_coordinate is None or next_coordinate > coordinate
            assert len(trace) <= 117
        return value, first_coordinate(value), trace

    for p in group['pivots']:
        coordinate, value = p['bit'], p['value']
        assert first_coordinate(value) == coordinate
        assert expression(p['exponents']) == value
        residual, missing, trace = reduce(square(value, MODULUS))
        assert residual == 1 and missing is None
        assert all(i > coordinate for i in trace)
    for g in generators:
        residual, missing, _ = reduce(g)
        assert residual == 1 and missing is None
    print('Verified all 113 pivot products/squares and all 320 source reductions.', flush=True)

    # Replay the declared finite queue using values alone, solely to check its
    # actual insertion/cancellation statistics and full pivot values.
    queue = deque(remove_residue(g) for g in generators)
    replayed, replay_inverse = {}, {}
    events = cancellations = 0
    while queue:
        value = queue.popleft()
        events += 1
        local_steps = 0
        while (coordinate := first_coordinate(value)) is not None:
            if coordinate not in replayed:
                replayed[coordinate] = value
                replay_inverse[coordinate] = inverse(value, MODULUS)
                queue.append(square(value, MODULUS))
                break
            value = multiply(value, replay_inverse[coordinate], MODULUS)
            cancellations += 1
            local_steps += 1
            later = first_coordinate(value)
            assert later is None or later > coordinate
            assert local_steps <= 117
        assert events <= 437
    assert replayed == pivots
    assert events == group['insertions'] == 433
    assert cancellations == group['cancellations'] == 10091

    b = multiply(1 << 10, 1 ^ chi)
    denominator = multiply(power(PHI, 42, 1 << 12), 3, 1 << 12)
    ell = multiply(1 ^ (1 << 8), inverse(denominator, 1 << 12), 1 << 12)
    low = square(ell)
    assert low == 0x5005
    beta = power(2, 64, PHI48)
    ix, ib = inverse(2, PHI48), inverse(b, PHI48)
    base = multiply(power(ix, 12, PHI48), power(ib, 7, PHI48), PHI48)
    correction = multiply(beta, multiply(power(ix, 12, PHI48), power(ib, 13, PHI48), PHI48), PHI48)
    s = multiply(1 << 16, multiply(power(3, 32), power(PHI, 40)), PHI48)
    expected_targets = [0xcf90ca900500cf9ac50a0f9a005005, 0x54154f8e9e854a845e8f8a84005005]
    expected_residuals = [0x88cfc8bf53a27e643e14a509000001, 0x9c9f98fb47f22e202a44f54d000001]
    expected_primary = [0xac00ac00acac000, 0x9b85851e91458fde914f451e]
    assert len(data['targets']) == 2
    summaries = []
    for epsilon, row in enumerate(data['targets']):
        assert row['epsilon'] == epsilon
        primary = base ^ (multiply(correction, s, PHI48) if epsilon else 0)
        adjustment = multiply(low ^ rem(primary, X24), inverse(PHI48, X24), X24)
        target = primary ^ multiply(PHI48, adjustment)
        assert target.bit_length() <= 120
        assert rem(target, X24) == low and rem(target, PHI48) == primary
        assert row['target'] == target == expected_targets[epsilon]
        assert row['low_X'] == low and row['phi_primary'] == primary == expected_primary[epsilon]
        residual, missing, trace = reduce(target)
        assert residual == row['residual'] == expected_residuals[epsilon]
        assert missing == row['first_missing_bit'] == 84
        assert trace == row['trace'] and len(trace) == 35
        assert row['member'] is False
        assert multiply(expression(row['expression']), residual, MODULUS) == target
        summaries.append({'epsilon': epsilon, 'target': hex(target), 'residual': hex(residual),
                          'first_missing_coordinate': missing, 'cancellations': len(trace),
                          'full_CRT_and_320_factor_product': True, 'member': False})
    assert data['targets'][0]['expression'] == data['targets'][1]['expression']
    assert data['targets'][0]['trace'] == data['targets'][1]['trace']
    assert data['witnesses'] == []
    result = {'verified': True, 'scope': 'Whole fixed J129 question, exactly 320 rows and epsilon 0,1',
              'source_method': 'Explicit binomial Fibonacci-polynomial formula; no author imports',
              'arithmetic': 'Exact four-coefficient binary convolution and Euclidean inverses',
              'matrix_periods': [320, 320], 'reconstructed_rows': 320,
              'pivot_products_and_square_closures': 113, 'source_reductions': 320,
              'missing_coordinates': [28, 36, 52, 84], 'group_order': group['order'],
              'ambient_index': data['ambient_order']//group['order'],
              'replayed_insertions': events, 'replayed_cancellations': cancellations,
              'targets': summaries, 'same_target_expression_and_trace': True,
              'positive_witnesses': [],
              'limits': 'No author output modification, earlier-J input/replay, larger precision, additional target, or positive witness construction.'}
    (out / 'reviewer_verification.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
