"""Review-only cross-check of C860's fixed word and two native interfaces.

Run after the four selected producer/verifier commands.
This imports no author arithmetic and does not discover or repair a proof.
It consumes the regenerated group certificate and original weighted residues.
"""
from collections import Counter
from math import gcd
from pathlib import Path
import json
import re
import sympy as sp


x = sp.Symbol('x')


def binary(value):
    return sp.Poly.from_list(
        [(value >> i) & 1 for i in range(value.bit_length() - 1, -1, -1)] or [0],
        x, modulus=2)


def bits(poly):
    return sum((int(c) % 2) << i for (i,), c in poly.terms())


def modular_power(poly, exponent, modulus):
    value = sp.Poly(1, x, modulus=2)
    while exponent:
        if exponent % 2:
            value = (value * poly).rem(modulus)
        poly = (poly * poly).rem(modulus)
        exponent //= 2
    return value


def totient(n):
    return sum(gcd(j, n) == 1 for j in range(1, n + 1))


def main():
    here = Path(__file__).resolve().parent
    root = here.parents[3]
    output = root / 'mathematics/computations/outputs' / here.name
    word = json.loads((here / 'inputs/enlarged_doubled_positive_word.json').read_text(encoding='utf-8'))
    group = json.loads((output / 'joint_necessary_filter_group.json').read_text(encoding='utf-8'))
    residue = json.loads((output / 'positive_word_residuals.json').read_text(encoding='utf-8'))
    claim = (root / 'mathematics/claims/Yin_C_G0814_v1.md').read_text(encoding='utf-8')
    table = claim.split('## D. Selected positive first-gate word and exact failure', 1)[1].split('Every exponent', 1)[0]
    rows = [(int(n), int(b), int(g)) for n, b, g in re.findall(
        r'^\| (\d+) \| (\d+) \| (\d+) \|$', table, re.M)]
    declared = {(family, n): exponent for n, b, g in rows
                for family, exponent in [('B', b), ('Gamma', g)] if exponent}
    actual = {(row['family'], row['n']): row['exponent'] for row in word['terms']}
    assert len(rows) == 19 and len(actual) == len(word['terms']) == 31
    assert actual == declared and residue['terms'] == word['terms']

    costs, exponent_sums, counts = Counter(), Counter(), Counter()
    for (family, n), exponent in actual.items():
        assert family in ('B', 'Gamma') and n > 1 and gcd(n, 30) == 1
        assert 0 < exponent < 240
        costs[family] += exponent * (n - 1) // 2 * (1 if family == 'B' else 3)
        exponent_sums[family] += exponent
        for d in range(2, n + 1):
            if n % d == 0:
                counts[d] += exponent
                if family == 'Gamma':
                    counts[3 * d] += exponent
    assert dict(costs) == {'B': 46020, 'Gamma': 66645}
    assert dict(exponent_sums) == {'B': 2205, 'Gamma': 1695}
    assert sum(e * totient(n) // 2 for n, e in counts.items()) == sum(costs.values()) == 112665
    assert [{'order': n, 'multiplicity': e} for n, e in sorted(counts.items())] == word['cofactor_trace_factor_multiplicities']
    full = counts + Counter({1: 8, 3: 4, 5: 6, 9: 8, 11: 2, 15: 4, 17: 2, 187: 2, 960: 1})
    assert [{'order': n, 'multiplicity': e} for n, e in sorted(full.items())] == word['complete_reciprocal_cyclotomic_multiplicities']
    assert sum(e * totient(n) for n, e in full.items()) == 226078
    binary_counts = Counter()
    for n, e in full.items():
        if n == 1:
            continue
        v2 = 0
        while n % 2 == 0:
            n //= 2
            v2 += 1
        binary_counts[n] += e * (1 if v2 == 0 else 2 ** (v2 - 1))
    assert word['binary_endpoint_exponent'] == full[1] // 2 == 4
    assert [{'odd_order': n, 'exponent': e} for n, e in sorted(binary_counts.items())] == word['complete_binary_odd_order_exponents']
    radical = 1 + sum(totient(n) // 2 for n in binary_counts)
    frobenius = min(e & -e for e in [4] + list(binary_counts.values()))
    assert radical == 801 and frobenius == 1 and binary_counts[11] == 227

    f = sp.Poly(x**4 + x**3 + 1, x, modulus=2)
    m14, m24 = f**14, f**24
    generators = {(row['family'], row['n']): row for row in group['generators']}
    assert len(generators) == 256
    pair_unit, pair_additive = sp.Poly(1, x, modulus=2), sp.Poly(0, x, modulus=2)
    for label, exponent in actual.items():
        row = generators[label]
        pair_unit = (pair_unit * modular_power(binary(row['L']), exponent, m14)).rem(m14)
        if exponent % 2:
            pair_additive += binary(row['Dlog_Q5'])

    # Extract the same Q(X) from its actual Q(C2) weight, without using group images.
    q2 = sp.Poly.from_list(list(reversed(residue['Q_evaluations_mod4']['2'])), x, modulus=2)
    assert all(int(q2.nth(j)) % 2 == 0 for j in range(1, 144, 2))
    qx = sp.Poly(sum((int(q2.nth(2*j)) % 2) * x**j for j in range(72)), x, modulus=2)
    assert qx**2 == q2
    q5 = sp.Poly.from_list(list(reversed(residue['Q_evaluations_mod4']['5'])), x, modulus=2)
    direct_l = (q5 * modular_power(sp.invert(qx, m14), 5, m14)).rem(m14)
    direct_dlog = (q5.diff() * sp.invert(q5, m24)).rem(m24)
    assert pair_unit == direct_l == binary(group['target'])
    assert pair_additive == direct_dlog and not direct_dlog.is_zero
    assert bits(pair_unit) == word['target_bits'] == 19232663035708480

    expected_obstruction = sum(1 << j for j in (23, 31, 47, 63, 71, 79, 87, 95))
    remainder = group['target_principal_reduction']['remainder']
    assert remainder & ((1 << 56) - 1) == 1
    assert remainder >> 56 == expected_obstruction == 39769430595359402857043329024
    additive_pivots = [(row['position'] - 52, row['element'] >> 56)
                       for row in group['principal_basis'] if row['position'] >= 52]
    assert [j for j, _ in additive_pivots] == [0, 1, 2, 4, 12, 14]
    assert group['target_principal_reduction']['first_missing_position'] == 75
    assert 75 not in [row['position'] for row in group['principal_basis']]
    derivative_contributors = [n for (family, n), e in actual.items()
                               if family == 'B' and e % 2 and n % 12 in (5, 7)]
    assert derivative_contributors == [7, 29, 41]
    result = dict(scope='C860 native input and certificate/residue interface corroboration',
                  claim_table_matches_all31_terms=True,
                  factor_counts_and_complete_degrees_match=True,
                  degree_by_family=dict(costs), exponent_sum_by_family=dict(exponent_sums),
                  original_trace_degree=113039, original_reciprocal_degree=226078,
                  full_binary_radical_degree=radical, maximal_binary_Frobenius_exponent=frobenius,
                  odd_binary_orders=[n for n, e in sorted(binary_counts.items()) if e % 2],
                  group_word_matches_actual_Q2_Q5_weights=True,
                  first_gate_target=bits(pair_unit), selected_word_Dlog=bits(direct_dlog),
                  normalized_target_additive_remainder=expected_obstruction,
                  pure_additive_pivots=additive_pivots,
                  derivative_contributors=derivative_contributors,
                  imports_author_arithmetic=False,
                  limitation='Uses inspected and reproduced author output; does not replace the complete native or mathematical review.')
    destination = output / 'review_c860_native_interfaces.json'
    destination.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
