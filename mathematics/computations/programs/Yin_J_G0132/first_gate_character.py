"""All256 allowed n classes: exact first-jet separating certificate only.

Bit i of each nonnegative integer is the coefficient of X^i over F2.
No cofactor candidates, subgroup elements or simultaneous X gate are enumerated.
"""
from pathlib import Path
from math import gcd
import json

F = (1 << 4) | (1 << 3) | 1


def rawmul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result


def remainder(a, modulus):
    while a and a.bit_length() >= modulus.bit_length():
        a ^= modulus << (a.bit_length()-modulus.bit_length())
    return a


def multiply(a, b, modulus):
    return remainder(rawmul(a, b), modulus)


def power(a, exponent, modulus):
    result = 1
    while exponent:
        if exponent & 1:
            result = multiply(result, a, modulus)
        a = multiply(a, a, modulus)
        exponent >>= 1
    return result


def inverse(a, modulus):
    u, v, g1, g2 = remainder(a, modulus), modulus, 1, 0
    while u != 1:
        if not u:
            raise ValueError('nonunit in specified quotient')
        shift = u.bit_length()-v.bit_length()
        if shift < 0:
            u, v, g1, g2 = v, u, g2, g1
            shift = -shift
        u ^= v << shift
        g1 ^= g2 << shift
    return remainder(g1, modulus)


def evaluate(poly, argument, modulus):
    result = 0
    for i in range(poly.bit_length()-1, -1, -1):
        result = multiply(result, argument, modulus) ^ ((poly >> i) & 1)
    return result


def derivative(poly):
    return sum(1 << (i-1) for i in range(1, poly.bit_length(), 2) if (poly >> i) & 1)


def field_trace(value):
    result = 0
    value = remainder(value, F)
    for _ in range(4):
        result ^= value
        value = multiply(value, value, F)
    assert result in (0, 1)
    return result


def character(poly):
    residue = remainder(poly, F)
    log = multiply(remainder(derivative(poly), F), inverse(residue, F), F)
    weighted = multiply(2, log, F)
    return dict(logarithmic_derivative_at_f=log,
                weighted_logarithmic_derivative_at_f=weighted,
                trace=field_trace(weighted))


def main():
    modulus = 1
    for _ in range(7):
        modulus = rawmul(modulus, F)
    assert modulus.bit_length()-1 == 28
    cheb = [0, 2]
    for _ in range(2, 16):
        cheb.append(rawmul(2, cheb[-1]) ^ cheb[-2])
    kernels = {}
    for q in (1, 3, 5, 15):
        argument = remainder(cheb[q], modulus)
        values = [1]
        previous, current = 0, argument
        for _ in range(1, 481):
            values.append(values[-1] ^ current)
            previous, current = current, multiply(argument, current, modulus) ^ previous
        kernels[q] = values

    rows = []
    for residue in range(1, 960):
        if gcd(residue, 960) != 1:
            continue
        n = 961 if residue == 1 else residue
        a = (n-1)//2
        b1, b3, b5, b15 = [kernels[q][a] for q in (1, 3, 5, 15)]
        pi1 = multiply(power(b3, 2, modulus), inverse(b1, modulus), modulus)
        pi5 = multiply(power(b15, 2, modulus), inverse(b5, modulus), modulus)
        h = multiply(pi5, inverse(power(pi1, 5, modulus), modulus), modulus)
        assert power(h, 120, modulus) == 1
        rows.append(dict(residue_mod960=residue, n=n, h=h,
                         Pi_at_X=pi1, Pi_at_C5=pi5, character=character(h)))
    assert len(rows) == 256

    x, phi, f9, chi = 2, 7, 11, cheb[5]
    delta = remainder((1 << 56) ^ (1 << 24), modulus)
    d = remainder((1 << 12) ^ (1 << 28), modulus)
    assert power(d, 2, modulus) == delta
    h0 = power(x, 2, modulus)
    for factor, exponent in [(x ^ 1, 2), (phi, 3), (f9, 4), (kernels[1][93], 1)]:
        h0 = multiply(h0, power(factor, exponent, modulus), modulus)
    gamma = power(x ^ 1, 2, modulus)
    for factor, exponent in [(chi, 2), (evaluate(F, chi, modulus), 18),
                             (evaluate(phi, chi, modulus), 3),
                             (evaluate(f9, chi, modulus), 4), (kernels[5][93], 1)]:
        gamma = multiply(gamma, power(factor, exponent, modulus), modulus)
    t = multiply(h0, delta, modulus)
    kappa = multiply(multiply(d, power(t, 5, modulus), modulus), inverse(gamma, modulus), modulus)
    assert power(kappa, 120, modulus) == 1
    target_character = character(kappa)
    duplication = {}
    for row in rows:
        key = row['n'] % 120
        duplication.setdefault(key, set()).add(row['h'])
    period120 = len(duplication) == 32 and all(len(v) == 1 for v in duplication.values())
    all_zero = all(row['character']['trace'] == 0 for row in rows)
    separates = all_zero and target_character['trace'] == 1
    payload = dict(
        scope='all256 admissible n classes modulo960, class1 represented by961; F4 image character only',
        coefficient_encoding='bit i is coefficient of X^i over F2',
        f=F, modulus=modulus, quotient_degree=28,
        character_formula='Tr_F16/F2(x*u_derivative(x)/u(x))',
        actual_base='T187=(X-2)^2 F480 F15^2 F3^2 F5^3 F9^4 B187',
        target=dict(delta=delta, d=d, H0=h0, t=t, gamma=gamma, kappa=kappa,
                    character=target_character),
        generators=rows, generator_count=256, period120_duplication_check=period120,
        distinct_images=len({row['h'] for row in rows}),
        all_generator_character_zero=all_zero,
        target_outside_generated_subgroup_certificate=separates,
        no_subgroup_or_candidate_enumeration=True)
    here = Path(__file__).resolve().parent
    output = here.parents[3] / 'mathematics/computations/outputs' / here.name
    output.mkdir(parents=True, exist_ok=True)
    tmp = output/'first_gate_character.json.partial'
    tmp.write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
    tmp.replace(output/'first_gate_character.json')
    print(json.dumps({key: payload[key] for key in ('generator_count', 'distinct_images',
                     'period120_duplication_check', 'all_generator_character_zero',
                     'target_outside_generated_subgroup_certificate')} | {'target': payload['target']}))


if __name__ == '__main__':
    main()
