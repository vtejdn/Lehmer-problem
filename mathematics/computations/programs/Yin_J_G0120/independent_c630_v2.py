"""Independent C630v2 review arithmetic, using dense polynomial lists.

No author program is imported. Whole-root polynomials are reconstructed from
their symmetric Laurent identity rather than from the author recurrence.
The finite checks support the separately recorded mathematical review; they
do not replace its all-order identities or accepted original-input interfaces.
"""

import json
import math
import re
from pathlib import Path


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    result = [0] * max(len(a), len(b))
    for j, value in enumerate(a):
        result[j] ^= value
    for j, value in enumerate(b):
        result[j] ^= value
    return trim(result)


def mul(a, b):
    if not a or not b:
        return []
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] ^= x & y
    return trim(result)


def divide(a, b):
    a, b = trim(a), trim(b)
    if not b:
        raise ZeroDivisionError
    quotient = [0] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        offset = len(a) - len(b)
        quotient[offset] = 1
        a = add(a, [0] * offset + b)
    return trim(quotient), a


def mod(a, modulus):
    return divide(a, modulus)[1]


def power(a, n, modulus=None):
    result = [1]
    for _ in range(n):
        result = mul(result, a)
        if modulus is not None:
            result = mod(result, modulus)
    return result


def reciprocal(a, modulus):
    r0, r1, t0, t1 = modulus, a, [], [1]
    while r1:
        q, remainder = divide(r0, r1)
        r0, r1, t0, t1 = r1, remainder, t1, add(t0, mul(q, t1))
    assert r0 == [1]
    answer = mod(t0, modulus)
    assert mod(mul(a, answer), modulus) == [1]
    return answer


def derivative(a):
    return trim([a[j] if j % 2 else 0 for j in range(1, len(a))])


def compose(a, b):
    result = []
    for coefficient in reversed(a):
        result = add(mul(result, b), [coefficient])
    return result


def encode(a):
    return sum(value * 2 ** j for j, value in enumerate(a))


def decode(n):
    return [int(c) for c in bin(n)[2:][::-1]] if n else []


def character(a):
    return sum(a[j] for j in (13, 15) if j < len(a)) % 2


def whole_root(n):
    """Invert sum(z**j, -h<=j<=h) = B_n(z+z**-1)."""
    assert n > 0 and n % 2 == 1
    h = (n - 1) // 2
    laurent = {j: 1 for j in range(-h, h + 1)}
    result = [0] * (h + 1)
    for degree in range(h, -1, -1):
        if laurent.get(degree, 0):
            result[degree] = 1
            for k in range(degree + 1):
                if math.comb(degree, k) % 2:
                    exponent = degree - 2 * k
                    laurent[exponent] = laurent.get(exponent, 0) ^ 1
    assert not any(laurent.values())
    return trim(result)


def matrix_product(a, b, modulus):
    return [[mod(add(mul(a[i][0], b[0][j]), mul(a[i][1], b[1][j])), modulus)
             for j in range(2)] for i in range(2)]


def matrix_power(n, modulus):
    value = [[[1], []], [[], [1]]]
    step = [[[0, 1], [1]], [[1], []]]
    for _ in range(n):
        value = matrix_product(value, step, modulus)
    return value


def verify():
    group = Path(__file__).resolve().parent
    root = group.parents[3]
    output = group.parents[2] / 'computations' / 'outputs' / group.name
    x, phi = [0, 1], [1, 1, 1]
    s, phi4, phi6 = power(phi, 8), power(phi, 4), power(phi, 6)
    modulus = mul(power(x, 4), s)
    predivision = mul(modulus, phi)
    identity = [[[1], []], [[], [1]]]
    assert matrix_power(40, modulus) == identity
    assert matrix_power(80, predivision) == identity
    assert derivative(modulus) == derivative(s) == []

    # This exact displayed table is the finite logical input retained in v2.
    c629 = (root / 'mathematics/claims/Yin_C_G0608_v1.md').read_text(encoding='utf-8')
    table = [(int(n), int(b, 16), int(d, 16)) for n, b, d in re.findall(
        r'^\| (\d+) \| (0x[0-9a-f]+) \| (0x[0-9a-f]+) \|$', c629, re.M)]
    assert [n for n, _, _ in table] == [n for n in range(1, 80, 2) if n % 5]
    for n, b, d in table:
        value = mod(whole_root(n), modulus)
        dlog = mod(mul(derivative(value), reciprocal(value, modulus)), modulus)
        assert (encode(value), encode(dlog), character(dlog)) == (b, d, 0)
        assert character(dlog) == character(mod(dlog, s))

    # Independently recover both CRT targets and their complete local gates.
    chi = mul(x, power(phi, 2))
    psi = compose(phi, chi)
    targets = []
    for epsilon, expected in enumerate((0x70705, 0x78f85)):
        local = mod(add(x, mul(phi4, power(x, 7)) if epsilon else []), s)
        candidates = [add(local, mul(s, decode(k))) for k in range(16)]
        valid = [a for a in candidates if mod(a, power(x, 4)) == [1, 0, 1]]
        assert len(valid) == 1 and encode(valid[0]) == expected
        y = valid[0]
        h = mul(power(x, 2), y)
        c = mod(mul(mul(power(x, 2), compose(y, chi)), power(psi, 14, s)), s)
        v = mul(power(x, 5), y)
        z = power(mod(mul(h, power(c, 2, phi6)), phi6), 11, phi6)
        assert power(z, 11, phi6) == mod(mul(h, power(c, 2, phi6)), phi6)
        gate = mul(z, add(v, power(c, 3, s)))
        if epsilon:
            gate = add(gate, mul(mul(h, v), mul(power(x, 4), mul(power([1, 1], 8), phi4))))
        assert mod(gate, s) == []
        assert power(h, 6, s) == power(c, 21, s)
        dlog = mod(mul(derivative(y), reciprocal(y, modulus)), modulus)
        assert encode(dlog) == (1 << 15) + (1 << 7) and character(dlog) == 1
        targets.append({'epsilon': epsilon, 'target': expected, 'character': 1})

    data = json.loads((output / 'certificate.json').read_text(encoding='utf-8'))
    expected_fixed = {'field': 'F_2', 'phi': 7, 'modulus': encode(modulus),
                      'predivision_modulus': encode(predivision), 'dimension': 20,
                      'predivision_dimension': 22, 'odd_order_period': 160,
                      'recurrence_matrix_power80': [[1, 0], [0, 1]],
                      'functional_coefficients': [13, 15], 'order25_Psi': encode(psi),
                      'result': 'all_sixteen_divided_rows_have_character_zero'}
    assert set(data) == set(expected_fixed) | {'rows'}
    assert all(data[k] == v for k, v in expected_fixed.items())
    assert [row['n'] for row in data['rows']] == list(range(5, 160, 10))
    for row in data['rows']:
        n = row['n']
        full = whole_root(n)
        value, remainder = divide(mod(full, predivision), phi)
        assert not remainder
        inv = reciprocal(value, modulus)
        dlog = mod(mul(derivative(value), inv), modulus)
        assert row == {'n': n, 'B_predivision': encode(mod(full, predivision)),
                       'D': encode(value), 'division_remainder': 0,
                       'inverse': encode(inv), 'dlog': encode(dlog), 'character': 0}
        assert character(dlog) == 0
        composed = compose(whole_root(n // 5), chi)
        assert full == mul(phi, composed)
        assert derivative(composed) == mul(power(phi, 2), compose(derivative(whole_root(n // 5)), chi))
    assert mod(mul(x, add(power(x, 15), power(x, 7))), s) == [1]
    assert character(add(power(x, 15), power(x, 7))) == 1
    assert all(character(a) == 0 for a in (power(phi, 2), mul(x, power(phi, 4)), mul(power(x, 2), power(phi, 6))))
    return output, {'verified': True, 'c629_logical_input_rows': len(table),
                    'c629_targets': targets, 'j120_corroborating_rows': len(data['rows']),
                    'recurrence_matrix_powers': [40, 80], 'odd_order_periods': [80, 160],
                    'composition_orders': list(range(5, 160, 10)),
                    'method': 'dense_F2_lists_and_symmetric_Laurent_reconstruction',
                    'limit': 'finite arithmetic corroborates the separately reviewed all-order proof; no original-input construction or recursive predecessor audit'}


if __name__ == '__main__':
    directory, result = verify()
    directory.mkdir(parents=True, exist_ok=True)
    (directory / 'independent_c630_v2_verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result))
