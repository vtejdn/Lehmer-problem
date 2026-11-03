"""Independent reconstruction of precisely J130's fixed two-target question.

See reviewer_contract.md, retained before execution and before author-code
inspection.  No contributor imports.  Whole traces use explicit binomial
coefficients; arithmetic follows this reviewer's earlier block-convolution
design.  Author certificate/verification inputs are read, never overwritten.
"""

import argparse
from collections import deque
from functools import lru_cache
import json
from math import comb, gcd
import os
from pathlib import Path
import time


DEADLINE = None
PHI = 7
LOW = 1 << 32
PRIMARY = MODULUS = PRE = None
DIM = 157
COUNT = 640


def budget():
    if DEADLINE is not None and time.monotonic() > DEADLINE:
        raise TimeoutError('Reviewer deadline exceeded; no successful result published')


def divide(a, b):
    budget()
    assert type(a) is int and a >= 0 and type(b) is int and b > 0
    quotient = 0
    size = b.bit_length()
    while a and a.bit_length() >= size:
        shift = a.bit_length() - size
        quotient ^= 1 << shift
        a ^= b << shift
    return quotient, a


def rem(a, modulus):
    return divide(a, modulus)[1]


@lru_cache(maxsize=512)
def blocks(b):
    values = [0]
    for i in range(4):
        values += [v ^ (b << i) for v in values]
    return tuple(values)


def multiply(a, b, modulus=None):
    budget()
    result, shift = 0, 0
    table = blocks(b)
    while a:
        result ^= table[a & 15] << shift
        a >>= 4
        shift += 4
    return rem(result, modulus) if modulus else result


def square(a, modulus=None):
    budget()
    result = 0
    while a:
        bit = a & -a
        result ^= 1 << (2 * (bit.bit_length() - 1))
        a ^= bit
    return rem(result, modulus) if modulus else result


def power(a, exponent, modulus=None):
    assert exponent >= 0
    result = 1
    while exponent:
        if exponent & 1:
            result = multiply(result, a, modulus)
        exponent >>= 1
        a = square(a, modulus)
    return result


def inverse(a, modulus):
    old_r, r, old_s, s = modulus, a, 0, 1
    while r:
        quotient, remainder = divide(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s ^ multiply(quotient, s)
    assert old_r == 1
    result = rem(old_s, modulus)
    assert multiply(a, result, modulus) == 1
    return result


@lru_cache(maxsize=1408)
def whole_b(n):
    """F_(d+1)+F_d, with F_(j+1)=sum_i binom(j-i,i) X^(j-2i)."""
    assert type(n) is int and 1 <= n <= 3835 and n & 1
    d, result = (n-1)//2, 0
    for j in (d, d-1):
        if j < 0:
            continue
        for i in range(j//2+1):
            budget()
            if comb(j-i, i) & 1:
                result ^= 1 << (j-2*i)
    assert result & 1 and result.bit_length()-1 == d
    return result


def compose(a, b):
    result = 0
    for i in reversed(range(a.bit_length())):
        result = multiply(result, b) ^ ((a >> i) & 1)
    return result


def first_coordinate(value):
    assert value & 1 and rem(value, PHI) == 1
    low = rem(value ^ 1, LOW)
    if low:
        return (low & -low).bit_length()-2
    remaining, order = rem(value, PRIMARY) ^ 1, 0
    while remaining:
        remaining, digit = divide(remaining, PHI)
        if digit:
            assert 1 <= order <= 63
            return 31 + 2*(order-1) + (0 if digit & 1 else 1)
        order += 1
    return None


def matrix_product(a, b, modulus):
    return tuple(tuple(multiply(a[i][0], b[0][j], modulus) ^
                       multiply(a[i][1], b[1][j], modulus)
                       for j in range(2)) for i in range(2))


def check_period(modulus):
    result, factor, exponent = ((1, 0), (0, 1)), ((2, 1), (1, 0)), 640
    while exponent:
        if exponent & 1:
            result = matrix_product(result, factor, modulus)
        factor = matrix_product(factor, factor, modulus)
        exponent >>= 1
    assert result == ((1, 0), (0, 1))


def bounded_json(path):
    if path.stat().st_size > 64*1024*1024:
        raise ValueError('Reviewer input exceeds the declared 64 MiB cap')
    value = json.loads(path.read_text(encoding='utf-8'))
    budget()
    return value


def publish(path, result):
    budget()
    payload = json.dumps(result, indent=2) + '\n'
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_name('reviewer_verification.pending.json')
    try:
        with pending.open('w', encoding='utf-8', newline='\n') as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        budget()
        os.replace(pending, path)
    finally:
        if pending.exists():
            pending.unlink()


def run(limit):
    global PRIMARY, MODULUS, PRE
    home = Path(__file__).resolve().parent
    out = home.parents[2] / 'computations' / 'outputs' / home.name
    data = bounded_json(out / 'certificate.json')
    author = bounded_json(out / 'verification.json')
    PRIMARY = power(PHI, 64)
    MODULUS = multiply(LOW, PRIMARY)
    PRE = multiply(LOW, power(PHI, 65))
    assert PRIMARY == (1 << 128) ^ (1 << 64) ^ 1
    assert MODULUS.bit_length() == 161 and PRE.bit_length() == 163
    assert data['schema'] == 'full-a16-membership-v1'
    assert data['phi'] == PHI and data['M'] == MODULUS and data['predivision_M'] == PRE
    assert data['exponent'] == 192 and data['ambient_order'] == 3*2**157
    assert data['matrix_period'] == 640 and data['odd_index_period'] == 1280
    assert data['scope'] == 'Only two HC6 eta=0 targets; no positive witness construction'
    for modulus in (MODULUS, PRE):
        check_period(modulus)

    expected = [('B', n) for n in range(1, 1280, 2) if n % 5]
    expected += [('D', 5*r) for r in range(1, 256, 2)]
    rows = data['rows']
    assert len(rows) == COUNT and [(r['kind'], r['n']) for r in rows] == expected
    chi = multiply(2, square(PHI))
    generators = []
    for row in rows:
        n, m = row['n'], row['m']
        if row['kind'] == 'B':
            assert m == (n if n % 3 else n+1280) and m <= 2559 and gcd(m, 15) == 1
        else:
            r = n//5
            k = next(k for k in range(3) if gcd(r+256*k, 15) == 1)
            ell = r+256*k
            assert row['r'] == r and row['k'] == k and row['ell'] == ell
            assert m == 5*ell and ell <= 767 and m <= 3835
        original, lifted = whole_b(n), whole_b(m)
        pre_original, pre_lifted = rem(original, PRE), rem(lifted, PRE)
        assert pre_original == pre_lifted == row['pre_original'] == row['pre_representative']
        if row['kind'] == 'D':
            predivided, pre_remainder = divide(pre_original, PHI)
            original, original_remainder = divide(original, PHI)
            lifted, lifted_remainder = divide(lifted, PHI)
            assert pre_remainder == original_remainder == lifted_remainder == 0
            assert predivided == rem(original, MODULUS)
            assert lifted == compose(whole_b(ell), chi)
            assert lifted.bit_length()-1 <= 1915
        value = rem(original, MODULUS)
        assert value == rem(lifted, MODULUS) == row['value']
        assert value & 1 and rem(value, PHI) != 0
        assert power(value, 192, MODULUS) == 1
        generators.append(value)
    print('Independent whole reconstruction: all 640 rows, lifts, divisions and both periods verified.', flush=True)

    group = data['group']
    assert group['modulus'] == MODULUS and group['generators'] == generators
    b3 = next(i for i, r in enumerate(rows) if (r['kind'], r['n']) == ('B', 3))
    assert group['b3_index'] == b3 and generators[b3] == 3
    teich = power(generators[b3], 64, MODULUS)
    assert group['teichmuller'] == teich and rem(teich, LOW) == 1
    assert teich != 1 and power(teich, 3, MODULUS) == 1
    tpowers = [power(teich, i, MODULUS) for i in range(3)]
    residues = {rem(value, PHI): i for i, value in enumerate(tpowers)}
    assert len(residues) == 3
    bits = [p['bit'] for p in group['pivots']]
    assert bits == [i for i in range(DIM) if i not in (36, 44, 60, 92, 156)]
    assert len(bits) == 152 and group['order'] == 3*2**152
    assert len(group['square_reductions']) == 152 and len(group['source_reductions']) == COUNT
    assert len(data['targets']) == 2
    for p in group['pivots']:
        assert type(p['value']) is int and 0 < p['value'] < (1 << 160)
    for vector in [p['exponents'] for p in group['pivots']] + [t['expression'] for t in data['targets']]:
        assert len(vector) == COUNT
        assert all(type(e) is int and 0 <= e < 192 for e in vector)
    pivots = {p['bit']: p['value'] for p in group['pivots']}
    pivot_inverses = {i: inverse(p, MODULUS) for i, p in pivots.items()}
    squares = []
    for generator in generators:
        powers = [generator]
        for _ in range(7):
            powers.append(square(powers[-1], MODULUS))
        squares.append(powers)

    def expression(vector):
        value = 1
        for e, powers in zip(vector, squares):
            for j in range(8):
                if e & (1 << j):
                    value = multiply(value, powers[j], MODULUS)
        return value

    def remove_residue(value):
        r = residues[rem(value, PHI)]
        return multiply(value, tpowers[(-r) % 3], MODULUS)

    def reduce(value):
        value, trace = remove_residue(value), []
        while (coordinate := first_coordinate(value)) in pivots:
            trace.append(coordinate)
            value = multiply(value, pivot_inverses[coordinate], MODULUS)
            later = first_coordinate(value)
            assert later is None or later > coordinate
            assert len(trace) <= DIM
        return value, first_coordinate(value), trace

    for p, closure in zip(group['pivots'], group['square_reductions']):
        coordinate, value = p['bit'], p['value']
        assert first_coordinate(value) == coordinate
        assert expression(p['exponents']) == value
        residual, missing, trace = reduce(square(value, MODULUS))
        assert residual == 1 and missing is None and all(i > coordinate for i in trace)
        assert closure == {'bit': coordinate, 'trace': trace, 'residual': 1}
    for i, g in enumerate(generators):
        residual, missing, trace = reduce(g)
        assert residual == 1 and missing is None
        assert group['source_reductions'][i] == {'index': i, 'trace': trace, 'residual': 1}
    print('All 152 complete pivot products/squares and all 640 source reductions verified.', flush=True)

    # Reviewer-owned value-only replay, separate from the completeness proof.
    queue = deque(remove_residue(g) for g in generators)
    replayed, replay_inverse = {}, {}
    events = cancellations = 0
    while queue:
        budget()
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
            assert local_steps <= DIM
        assert events <= 797 and cancellations <= 125129
    assert replayed == pivots
    assert events == group['insertions'] == 792
    assert cancellations == group['cancellations'] == 20877

    # General Bezout CRT idempotents, followed by both component checks.
    id_low = multiply(PRIMARY, inverse(rem(PRIMARY, LOW), LOW), MODULUS)
    id_primary = multiply(LOW, inverse(rem(LOW, PRIMARY), PRIMARY), MODULUS)
    assert id_low ^ id_primary == 1
    low = 1 ^ (1 << 16)
    correction = multiply(1 << 24, multiply(power(3, 64), power(PHI, 32)), PRIMARY)
    assert correction != 0
    expected_targets = [0x1010100000000000101010000000000010001,
                        0x1010101000000010101010100000000010001]
    expected_residuals = [0x56ace74b76e70f3ec03c62884dfd331800000001,
                          0xe0778afdad8bb9e51b50d453204ae87500000001]
    summaries = []
    for epsilon, row in enumerate(data['targets']):
        assert row['epsilon'] == epsilon
        primary = (1 << 8) ^ (correction if epsilon else 0)
        target = multiply(low, id_low, MODULUS) ^ multiply(primary, id_primary, MODULUS)
        assert target.bit_length() <= 160
        assert rem(target, LOW) == low and rem(target, PRIMARY) == primary
        assert row['target'] == target == expected_targets[epsilon]
        assert row['low_X'] == low and row['phi_primary'] == primary
        residual, missing, trace = reduce(target)
        assert residual == row['residual'] == expected_residuals[epsilon]
        assert missing == row['first_missing_bit'] == 92
        assert trace == row['trace'] and len(trace) == 38
        assert row['member'] is False
        assert multiply(expression(row['expression']), residual, MODULUS) == target
        summaries.append({'epsilon': epsilon, 'target': hex(target), 'residual': hex(residual),
                          'first_missing_coordinate': missing, 'cancellations': len(trace),
                          'full_CRT_and_640_factor_product': True, 'member': False})
    assert data['targets'][0]['expression'] == data['targets'][1]['expression']
    assert data['targets'][0]['trace'] == data['targets'][1]['trace']

    expected_author = {'verified': True, 'reconstructed_rows': COUNT,
                      'matrix_periods': [640, 640], 'odd_index_periods': [1280, 1280],
                      'pivot_expressions': 152, 'pivot_square_closures': 152,
                      'source_reductions': COUNT, 'group_order': group['order'], 'ambient_index': 32,
                      'targets': [{'epsilon': e, 'member': False, 'first_missing_bit': 92,
                                   'full_CRT': True, 'complete_vector_product_identity': True} for e in (0, 1)],
                      'scope': 'Fixed two-target certificate only; no positive or original witness construction'}
    assert author == expected_author
    result = {'verified': True, 'scope': 'Whole fixed J130 question: exactly 640 rows and epsilon 0,1',
              'source_method': 'Whole binomial Fibonacci-polynomial formula; no author imports',
              'arithmetic': 'Four-coefficient binary convolution, Euclidean inverses, Bezout CRT',
              'matrix_periods': [640, 640], 'odd_index_periods': [1280, 1280],
              'reconstructed_rows': COUNT, 'pivot_products_and_square_closures': 152,
              'source_reductions': COUNT, 'stored_source_and_square_traces_checked': True,
              'missing_coordinates': [36, 44, 60, 92, 156], 'group_order': group['order'],
              'ambient_index': data['ambient_order']//group['order'],
              'replayed_insertions': events, 'replayed_cancellations': cancellations,
              'targets': summaries, 'same_target_expression_and_trace': True,
              'author_verification_payload_consistent': True, 'positive_witnesses': [],
              'max_seconds': limit, 'contract': 'reviewer_contract.md',
              'limits': 'No author command replay or author output modification; no earlier-J input, new precision, additional target, positive witness or original construction. Historical author runtime is not independently certified.'}
    publish(out / 'reviewer_verification.json', result)
    print(json.dumps(result, indent=2), flush=True)


def main():
    global DEADLINE
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--max-seconds', type=int, default=1800)
    args = parser.parse_args()
    if not args.execute:
        parser.error('Explicit --execute is required for the fixed reconstruction contract')
    if not 1 <= args.max_seconds <= 1800:
        parser.error('--max-seconds must lie in 1,...,1800')
    if not __debug__:
        raise RuntimeError('Optimized Python would disable exact certificate assertions')
    DEADLINE = time.monotonic() + args.max_seconds
    run(args.max_seconds)


if __name__ == '__main__':
    main()
