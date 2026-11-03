"""Distinct all256 image check using Laurent kernels and an actual integer target.

No producer imports.  No full cofactor/subgroup/candidate enumeration.
"""
from pathlib import Path
from math import gcd
import json
import sympy as sp
from verify_odd_support import C, x, z, trace_factor, coefficients


def bits(poly):
    return sum((int(poly.nth(i)) % 2) << i for i in range(poly.degree()+1)) if poly else 0


def binary_poly(value, symbol=x):
    return sp.Poly.from_list([(value >> i) & 1 for i in range(value.bit_length()-1, -1, -1)] or [0], symbol, modulus=2)


def powmod(poly, exponent, modulus):
    result = sp.Poly(1, poly.gens[0], modulus=2)
    while exponent:
        if exponent & 1:
            result = (result*poly).rem(modulus)
        poly = (poly*poly).rem(modulus)
        exponent >>= 1
    return result


def main():
    here = Path(__file__).resolve().parent
    output = here.parents[3] / 'mathematics/computations/outputs' / here.name
    saved = json.loads((output/'first_gate_character.json').read_text(encoding='utf-8'))
    f = sp.Poly(x**4+x**3+1, x, modulus=2)
    modulus = f**7
    assert saved['f'] == bits(f) == 25
    assert saved['modulus'] == bits(modulus) and saved['quotient_degree'] == 28
    cyclo = sp.Poly(sp.cyclotomic_poly(15, z), z, modulus=2)
    laurent_modulus = cyclo**7
    zp = [sp.Poly(1, z, modulus=2)]
    zz = sp.Poly(z, z, modulus=2)
    for _ in range(120):
        zp.append((zp[-1]*zz).rem(laurent_modulus))
    assert zp[120] == zp[0]
    trace_argument = zp[1]+zp[119]
    xp = [sp.Poly(1, z, modulus=2)]
    for _ in range(27):
        xp.append((xp[-1]*trace_argument).rem(laurent_modulus))
    shifted_basis = [(zp[27]*poly).rem(laurent_modulus) for poly in xp]

    def recover_trace(poly):
        work = (zp[27]*poly).rem(laurent_modulus)
        assert work.degree() <= 54 or work.is_zero
        value = 0
        for j in range(27, -1, -1):
            if int(work.nth(27+j)) % 2:
                value |= 1 << j
                work += shifted_basis[j]
        assert work.is_zero
        return binary_poly(value)

    def kernel_laurent(n, q):
        coefficients120 = [0]*120
        a = (n-1)//2
        for j in range(-a, a+1):
            coefficients120[(q*j) % 120] ^= 1
        return sp.Poly.from_list(list(reversed(coefficients120)), z, modulus=2).rem(laurent_modulus)

    def character(poly):
        residue = poly.rem(f)
        log = (poly.diff().rem(f)*sp.invert(residue, f)).rem(f)
        weighted = (sp.Poly(x, x, modulus=2)*log).rem(f)
        total = sp.Poly(0, x, modulus=2)
        term = weighted
        for _ in range(4):
            total += term
            term = (term**2).rem(f)
        assert bits(total) in (0, 1)
        return dict(logarithmic_derivative_at_f=bits(log),
                    weighted_logarithmic_derivative_at_f=bits(weighted), trace=bits(total))

    expected = [r for r in range(1, 960) if gcd(r, 960) == 1]
    assert len(expected) == saved['generator_count'] == len(saved['generators']) == 256
    assert [row['residue_mod960'] for row in saved['generators']] == expected
    true_images, true_characters = {}, {}
    for residue, row in zip(expected, saved['generators']):
        n = 961 if residue == 1 else residue
        assert row['n'] == n
        b1, b3, b5, b15 = [kernel_laurent(n, q) for q in (1, 3, 5, 15)]
        pi1 = (b3**2*sp.invert(b1, laurent_modulus)).rem(laurent_modulus)
        pi5 = (b15**2*sp.invert(b5, laurent_modulus)).rem(laurent_modulus)
        h_laurent = (pi5*powmod(sp.invert(pi1, laurent_modulus), 5, laurent_modulus)).rem(laurent_modulus)
        hp = recover_trace(h_laurent)
        assert bits(recover_trace(pi1)) == row['Pi_at_X']
        assert bits(recover_trace(pi5)) == row['Pi_at_C5']
        assert bits(hp) == row['h'], n
        assert powmod(hp, 120, modulus) == sp.Poly(1, x, modulus=2)
        value = character(hp)
        assert value == row['character'], n
        true_images[n], true_characters[n] = bits(hp), value['trace']

    # Target is reconstructed from actual integer base coefficients, not UG16's formula.
    while len(C) <= 93:
        C.append(sp.Poly(x, x, domain=sp.ZZ)*C[-1]-C[-2])
    ints = {n: trace_factor(n) for n in (3, 5, 9, 11, 15, 17, 187, 480)}
    b187 = ints[11]*ints[17]*ints[187]
    assert b187 == sum(C[1:94], sp.Poly(1, x))
    ff, vv = ints[15], ints[480]
    jj = ff**2*vv
    h0 = sp.Poly((x-2)**2, x)*ints[3]**2*ints[5]**3*ints[9]**4*b187
    numerator = jj.compose(C[5]).rem(jj)
    assert all(int(a) % 5 == 0 for a in numerator.all_coeffs())
    theta5 = sp.Poly.from_list([int(a)//5 for a in numerator.all_coeffs()], x)
    c0 = (h0.compose(C[5]).rem(jj)*theta5).rem(jj)
    assert c0.rem(ff**2).is_zero
    gamma = sp.Poly(c0.exquo(ff**2), x, modulus=2).rem(modulus)
    difference = vv-ff**16
    assert all(int(a) % 2 == 0 for a in difference.all_coeffs())
    delta_integer = sp.Poly.from_list([int(a)//2 for a in difference.all_coeffs()], x)
    delta_full = sp.Poly(delta_integer, x, modulus=2)
    assert bits(delta_full) == (1 << 56) ^ (1 << 24)
    delta = delta_full.rem(modulus)
    d = sp.Poly(x**12*(1+x)**16, x, modulus=2).rem(modulus)
    assert (d**2).rem(modulus) == delta
    h0_binary = sp.Poly(h0, x, modulus=2).rem(modulus)
    t = (h0_binary*delta).rem(modulus)
    kappa = (d*powmod(t, 5, modulus)*sp.invert(gamma, modulus)).rem(modulus)
    for key, poly in [('delta', delta), ('d', d), ('H0', h0_binary),
                      ('t', t), ('gamma', gamma), ('kappa', kappa)]:
        assert saved['target'][key] == bits(poly), key
    target_character = character(kappa)
    assert target_character == saved['target']['character']
    grouping = {}
    for n, value in true_images.items():
        grouping.setdefault(n % 120, set()).add(value)
    period120 = len(grouping) == 32 and all(len(v) == 1 for v in grouping.values())
    all_zero = all(v == 0 for v in true_characters.values())
    separates = all_zero and target_character['trace'] == 1
    assert saved['period120_duplication_check'] == period120
    assert saved['all_generator_character_zero'] == all_zero
    assert saved['target_outside_generated_subgroup_certificate'] == separates
    assert saved['distinct_images'] == len(set(true_images.values()))
    result = dict(
        verified_generators=256, verified_Pi_component_images=512, verified_h_images=256,
        arithmetic='separate F2 Laurent quotient Phi15^7; exact integer base c0 and delta half',
        actual_integer_c0_coefficients=coefficients(c0),
        actual_integer_delta_coefficients=coefficients(delta_integer),
        target_kappa=bits(kappa), target_character=target_character,
        all_generator_character_zero=all_zero, distinct_images=len(set(true_images.values())),
        period120_duplication_check=period120,
        target_outside_generated_subgroup_certificate=separates,
        no_subgroup_or_candidate_enumeration=True, sympy_version=sp.__version__)
    tmp = output/'first_gate_character_verification.json.partial'
    tmp.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    tmp.replace(output/'first_gate_character_verification.json')
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ('actual_integer_c0_coefficients', 'actual_integer_delta_coefficients')}))


if __name__ == '__main__':
    main()
