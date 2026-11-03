"""Independent fixed-scope review of the C643v2/J126 certificate.

This reviewer program imports neither contributor implementation.
Polynomials are sets of exponents; complete B_n use explicit binomial sums.
It checks supplied normal-form evidence, never searches new supports.
Its arithmetic kernels are copied from this reviewer's J125 checker.
"""

import json
from math import comb
from pathlib import Path


ONE = frozenset({0})
ZERO = frozenset()
X = frozenset({1})
PHI = frozenset({0, 1, 2})


def unpack(value):
    assert isinstance(value, int) and value >= 0
    return frozenset(i for i in range(value.bit_length()) if (value >> i) & 1)


def pack(value):
    return sum(1 << i for i in value)


def times(a, b):
    result = set()
    for i in a:
        for j in b:
            if i + j in result:
                result.remove(i + j)
            else:
                result.add(i + j)
    return frozenset(result)


def quotient_remainder(a, b):
    assert b
    quotient, remainder = set(), set(a)
    degree = max(b)
    while remainder and max(remainder) >= degree:
        shift = max(remainder) - degree
        quotient.add(shift)
        remainder.symmetric_difference_update(j + shift for j in b)
    return frozenset(quotient), frozenset(remainder)


def rem(a, modulus):
    return quotient_remainder(a, modulus)[1]


def pow_poly(a, exponent, modulus=None):
    assert exponent >= 0
    result = ONE
    while exponent:
        if exponent & 1:
            result = times(result, a)
            if modulus is not None:
                result = rem(result, modulus)
        exponent //= 2
        a = times(a, a)
        if modulus is not None:
            a = rem(a, modulus)
    return result


PHI16 = pow_poly(PHI, 16)
MODULUS = times(frozenset({8}), PHI16)


def multiply(a, b):
    return rem(times(a, b), MODULUS)


def invert(a):
    old_r, r, old_s, s = MODULUS, a, ZERO, ONE
    while r:
        q, remainder = quotient_remainder(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s ^ times(q, s)
    assert old_r == ONE
    result = rem(old_s, MODULUS)
    assert multiply(a, result) == ONE
    return result


def whole_trace(n):
    # B_(2d+1)=F_(d+1)+F_d; Pascal's identity gives the trace recurrence.
    assert n > 0 and n % 2 == 1
    d = (n - 1) // 2
    first = {d - 2*j for j in range(d // 2 + 1) if comb(d - j, j) % 2}
    second = {d - 1 - 2*j for j in range((d - 1) // 2 + 1)
              if comb(d - 1 - j, j) % 2}
    return frozenset(first ^ second)


def leading(value):
    assert rem(value, PHI) == ONE and 0 in value
    low = frozenset(i for i in value ^ ONE if i < 8)
    if low:
        return min(low) - 1
    principal = rem(value, PHI16) ^ ONE
    j = 0
    while principal:
        principal, digit = quotient_remainder(principal, PHI)
        if digit:
            assert j >= 1
            return 7 + 2*(j - 1) + min(digit)
        j += 1
    return None


def matrix_times(a, b, modulus=None):
    answer = [[times(a[i][0], b[0][j]) ^ times(a[i][1], b[1][j])
               for j in range(2)] for i in range(2)]
    return [[rem(v, modulus) if modulus else v for v in row] for row in answer]


def matrix_power(n):
    a = [[X, ONE], [ONE, ZERO]]
    result = [[ONE, ZERO], [ZERO, ONE]]
    for _ in range(n):
        result = matrix_times(result, a)
    return result


def compose(a, b, modulus=None):
    result = ZERO
    for exponent in a:
        result ^= pow_poly(b, exponent, modulus)
    return result


def main():
    home = Path(__file__).resolve().parent
    out = home.parents[2] / 'computations' / 'outputs' / home.name
    data = json.loads((out / 'certificate.json').read_text(encoding='utf-8'))
    assert data['phi'] == pack(PHI) and data['M'] == pack(MODULUS)
    assert MODULUS == frozenset({8, 24, 40})
    premodulus = times(frozenset({8}), pow_poly(PHI, 17))
    assert pack(premodulus) == data['predivision_M']
    identity = [[ONE, ZERO], [ZERO, ONE]]
    a8, a16, a5, a = matrix_power(8), matrix_power(16), matrix_power(5), matrix_power(1)
    for i in range(2):
        for j in range(2):
            assert a16[i][j] ^ identity[i][j] == times(frozenset({8}), a8[i][j])
            rhs = times(PHI, times(PHI, a[i][j]) ^ times(X ^ ONE, identity[i][j]))
            assert a5[i][j] ^ identity[i][j] == rhs
    assert [[rem(v, MODULUS) for v in row] for row in matrix_power(80)] == identity
    assert [[rem(v, premodulus) for v in row] for row in matrix_power(160)] == identity
    expected = [('B', n) for n in range(1, 160, 2) if n % 5]
    expected += [('D', n) for n in range(5, 320, 10)]
    rows = data['rows']
    assert [(r['kind'], r['n']) for r in rows] == expected and len(rows) == 96
    gs = []
    source_checks = []
    chi = times(X, pow_poly(PHI, 2))
    for row in rows:
        n, m = row['n'], row['m']
        bn, bm = whole_trace(n), whole_trace(m)
        if row['kind'] == 'B':
            assert m == (n if n % 3 else n + 160) and m % 3 and m % 5
            assert m <= 319
        else:
            r = n // 5
            k = next(k for k in range(3) if (r + 64*k) % 3 and (r + 64*k) % 5)
            ell = r + 64*k
            assert row['ell'] == ell and row['k'] == k and m == 5*ell
            assert ell <= 191 and m <= 955 and m == n + 320*k
            assert rem(bn ^ bm, premodulus) == ZERO
            bn, remainder_n = quotient_remainder(bn, PHI)
            bm, remainder_m = quotient_remainder(bm, PHI)
            assert remainder_n == remainder_m == ZERO
            assert rem(bn, PHI) and rem(bm, PHI)
            assert bm == compose(whole_trace(ell), chi)
            # Inspect actual complete divisor sets, without irreducible pairing.
            actual = {d for d in range(3, m+1, 2) if m % d == 0 and d != 5}
            small = {d for d in range(3, ell+1, 2) if ell % d == 0}
            assert actual == small | {5*d for d in small}
            assert all(d % 3 and d % 25 for d in actual)
            assert all(d // 5 in actual for d in actual if d % 5 == 0)
        value = rem(bn, MODULUS)
        assert value == rem(bm, MODULUS) == unpack(row['value'])
        assert multiply(value, invert(value)) == ONE
        assert pow_poly(value, 48, MODULUS) == ONE
        gs.append(value)
        source_checks.append({'kind': row['kind'], 'n': n, 'm': m,
                              'residue': hex(pack(value)), 'verified': True})
    assert max(whole_trace(961)) == 480
    assert rem(whole_trace(961), MODULUS) == ONE
    assert 961 % 3 and 961 % 5 and all(row['m'] < 961 for row in rows)
    group = data['group']
    assert group['generators'] == [pack(g) for g in gs]
    assert group['modulus'] == pack(MODULUS)
    b3 = group['b3_index']
    assert rows[b3]['n'] == 3 and gs[b3] == X ^ ONE
    t = pow_poly(gs[b3], 16, MODULUS)
    assert pack(t) == group['teichmuller'] and t != ONE
    assert pow_poly(t, 3, MODULUS) == ONE
    assert frozenset(i for i in t if i < 8) == ONE
    tpowers = [pow_poly(t, j, MODULUS) for j in range(3)]
    residues = [rem(v, PHI) for v in tpowers]
    assert len(set(residues)) == 3
    powers = [[pow_poly(g, e, MODULUS) for e in range(48)] for g in gs]

    def expression(exponents):
        assert len(exponents) == 96
        value = ONE
        for i, e in enumerate(exponents):
            assert isinstance(e, int) and 0 <= e < 48
            value = multiply(value, powers[i][e])
        return value

    pivots = group['pivots']
    bits = [p['bit'] for p in pivots]
    assert bits == sorted(set(bits)) and all(0 <= bit < 37 for bit in bits)
    lookup = {}
    for p in pivots:
        value = unpack(p['value'])
        assert max(value) < 40 and leading(value) == p['bit']
        assert expression(p['exponents']) == value
        lookup[p['bit']] = (value, invert(value))

    def reduce(value, after=-1):
        residue_index = residues.index(rem(value, PHI))
        if after >= 0:
            assert residue_index == 0
        value = multiply(value, tpowers[(-residue_index) % 3])
        used = []
        while (bit := leading(value)) is not None and bit in lookup:
            assert bit > after
            used.append(bit)
            value = multiply(value, lookup[bit][1])
            next_bit = leading(value)
            assert next_bit is None or next_bit > bit
        return value, leading(value), used

    square_rows = []
    for p in pivots:
        square = multiply(unpack(p['value']), unpack(p['value']))
        remainder, missing, used = reduce(square, after=p['bit'])
        assert remainder == ONE and missing is None
        square_rows.append({'bit': p['bit'], 'later_pivots': used})
    for g in gs:
        assert reduce(g)[0] == ONE
    assert len(bits) == 34 and 20 not in bits
    assert group['order'] == 3 * 2**len(bits) == 51539607552
    assert data['ambient_order'] == 3 * 2**37
    assert group['insertions'] == 130 and group['cancellations'] == 754
    assert [row['epsilon'] for row in data['targets']] == [0, 1]
    target_rows = []
    for row in data['targets']:
        eps = row['epsilon']
        y = frozenset({2}) ^ times(PHI16, frozenset({0, 2, 4}))
        if eps:
            y ^= times(frozenset({14}), pow_poly(PHI, 8))
        assert pack(y) == row['target']
        assert frozenset(i for i in y if i < 8) == frozenset({0, 4})
        residual, missing, used = reduce(y)
        assert residual != ONE and missing == 20 and row['member'] is False
        assert pack(residual) == row['residual'] and row['first_missing_bit'] == 20
        assert multiply(expression(row['expression']), residual) == y
        # Direct check of the formal converse, with the full correction factor.
        chi = times(X, pow_poly(PHI, 2))
        psi = compose(PHI, chi, PHI16)
        c = rem(times(frozenset({4}), times(compose(y, chi, PHI16), pow_poly(psi, 28, PHI16))), PHI16)
        h, v = rem(times(frozenset({4}), y), PHI16), rem(times(frozenset({10}), y), PHI16)
        assert c == frozenset({4})
        z = pow_poly(rem(times(h, pow_poly(c, 2, PHI16)), PHI16), 35, pow_poly(PHI, 12))
        d = v ^ pow_poly(c, 3, PHI16)
        assert rem(d, pow_poly(PHI, 8)) == ZERO
        correction = times(frozenset({8}), times(pow_poly(X ^ ONE, 16), pow_poly(PHI, 8))) if eps else ZERO
        assert rem(times(z, d) ^ times(times(h, v), correction), PHI16) == ZERO
        assert pow_poly(h, 6, PHI16) == pow_poly(c, 21, PHI16)
        target_rows.append({'epsilon': eps, 'target': hex(pack(y)), 'residual': hex(pack(residual)), 'first_missing_bit': missing, 'pivots_used': used})
    assert data['witness'] is None
    chi = times(X, pow_poly(PHI, 2))
    psi = compose(PHI, chi, PHI16)
    allowed_low = []
    for mask in range(8):
        y = ONE | frozenset(2*(j+1) for j in range(3) if (mask >> j) & 1)
        f = rem(times(compose(y, chi, PHI16), pow_poly(psi, 28, PHI16)), PHI16)
        if pow_poly(f, 3, PHI16) == ONE:
            allowed_low.append(pack(y))
    assert allowed_low == [17]
    result = {'result': 'verified', 'scope': 'C643v2 fixed targets and complete J126 certificate only',
              'arithmetic': 'exact F2 exponent-set polynomials; no contributor imports',
              'complete_generators': 96, 'coprime_rows': 64, 'divided_rows': 32,
              'predivision_matrix_period': 160, 'divided_index_period': 320,
              'exact_divided_compositions': 32, 'principal_pivots': 34,
              'group_order': group['order'], 'ambient_index': 8,
              'complete_source_checks': source_checks,
              'later_square_relations': square_rows, 'targets': target_rows,
              'formal_low_X_candidates': 8, 'formal_low_X_survivors': allowed_low,
              'limits': 'No alternate support, original integer coefficient search, or formal proof assistant verification.'}
    (out / 'reviewer_verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('complete_source_checks', 'later_square_relations', 'targets')}, indent=2))


if __name__ == '__main__':
    main()
