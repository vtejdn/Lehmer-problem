"""ONE retained31-term word: original weighted residuals modulo4 at J2.

This is an author calculation, not an independent review or a search.
The full degree113039 T and degree112665 Q are never expanded.
"""
from pathlib import Path
import json
from math import gcd
from main import add, mul, rem, power, compose, chebyshev, canonical_mod4
from odd_support_probe import binary_order, binary_initial_unit


def modular_power(a, exponent, divisor, modulus=4):
    result = [1]
    while exponent:
        if exponent & 1:
            result = rem(mul(result, a, modulus), divisor, modulus)
        exponent >>= 1
        if exponent:
            a = rem(mul(a, a, modulus), divisor, modulus)
    return result


def kernel(n, argument, divisor):
    previous, current = [2], argument
    result = [1]
    for j in range(1, (n-1)//2+1):
        result = rem(add(result, current, modulus=4), divisor, 4)
        if j < (n-1)//2:
            previous, current = current, rem(
                add(mul(argument, current, 4), previous, -1, 4), divisor, 4)
    return result


def main():
    here = Path(__file__).resolve().parent
    output = here.parents[3]/'mathematics/computations/outputs'/here.name
    selected = json.loads((here/'inputs/enlarged_doubled_positive_word.json').read_text(encoding='utf-8'))
    terms = selected['terms']
    assert len(terms) == 31 and len({row['n'] for row in terms}) == 19
    assert selected['actual_single_F960'] is True
    assert all(row['family'] in ('B', 'Gamma') and row['n'] > 1
               and gcd(row['n'], 30) == 1 and 0 < row['exponent'] < 240 for row in terms)
    cost = sum((1 if row['family'] == 'B' else 3)*(row['n']-1)//2*row['exponent'] for row in terms)
    assert cost == selected['cofactor_degree'] == 112665
    assert selected['original_trace_degree'] == cost+374 == 113039
    assert selected['original_reciprocal_degree'] == 226078
    assert selected['maximal_binary_Frobenius_exponent'] == 1
    assert selected['full_binary_radical_degree'] == 801

    f3, f5, f9 = [1, 1], [-1, 1, 1], [1, -3, 0, 1]
    f15, f30 = [1, 4, -4, -1, 1], [1, -4, -4, 1, 1]
    v32 = compose(f30, chebyshev(32))
    divisor = mul(power(f15, 4), v32)
    assert len(divisor)-1 == 144
    base = [('endpoint', [-2, 1], 4), ('F3', f3, 4),
            ('F5', f5, 6), ('F9', f9, 8)]
    weights, theta, q_weights, term_weights, original = {}, {}, {}, {}, {}
    for p, name in ((2, 'a'), (3, 'b'), (5, 'c')):
        cp, c3p = chebyshev(p), chebyshev(3*p)
        base_weight = [1]
        for _, factor, exponent in base:
            value = compose(factor, cp, divisor, 4)
            base_weight = rem(mul(base_weight, modular_power(value, exponent, divisor), 4), divisor, 4)
        b187 = kernel(187, cp, divisor)
        base_weight = rem(mul(base_weight, modular_power(b187, 2, divisor), 4), divisor, 4)
        q_weight = [1]
        records = []
        for row in terms:
            argument = cp if row['family'] == 'B' else c3p
            value = kernel(row['n'], argument, divisor)
            contribution = modular_power(value, row['exponent'], divisor)
            q_weight = rem(mul(q_weight, contribution, 4), divisor, 4)
            records.append(dict(**row, evaluated_factor=value, evaluated_power=contribution))
        weight = rem(mul(base_weight, q_weight, 4), divisor, 4)
        # canonical_mod4 first reduces the ACTUAL integer numerator modulo4*p
        # and only then divides every coefficient by p (including p=2).
        divided = canonical_mod4(divisor, p)
        theta[p], weights[p], q_weights[p], term_weights[p] = divided, weight, q_weight, records
        original[name] = rem(mul(weight, divided, 4), divisor, 4)
    a, b, c = [original[key] for key in ('a', 'b', 'c')]
    ap = {e: modular_power(a, e, divisor) for e in (3, 5)}
    bp = {e: modular_power(b, e, divisor) for e in (2, 5)}
    cp = {e: modular_power(c, e, divisor) for e in (2, 3)}
    original['F'] = rem(add([2*v for v in cp[2]], ap[5], -3), divisor, 4)
    original['G'] = rem(add(cp[3], bp[5], -2), divisor, 4)
    second_base = add(bp[2], ap[3], -1)
    original['X_plus'] = rem(add(second_base, original['G']), divisor, 4)
    original['X_minus'] = rem(add(second_base, original['G'], -1), divisor, 4)
    assert original['F'] == [0], 'Previously certified first gate must agree with actual weighted residue'
    assert rem(add(original['X_plus'], original['X_minus'], -1), divisor, 4) == rem(
        [2*v for v in original['G']], divisor, 4)
    values = {key: (0 if any(v % 2 for v in poly)
                    else 1 if any(poly) else 'at_least_2') for key, poly in original.items()}
    halves = {key: [v//2 for v in poly] for key, poly in original.items() if not any(v % 2 for v in poly)}
    gates = dict(F_mod4=original['F'] == [0],
                 X_plus_mod2=not any(v % 2 for v in original['X_plus']),
                 X_minus_mod2=not any(v % 2 for v in original['X_minus']),
                 X_plus_mod4=original['X_plus'] == [0],
                 X_minus_mod4=original['X_minus'] == [0],
                 G_nonzero_mod2=any(v % 2 for v in original['G']))
    payload = dict(scope='ONE fixed31-term positive B/Gamma word; weighted ORIGINAL residues only',
                   input='inputs/enlarged_doubled_positive_word.json', terms=terms,
                   quotient_degree=144, full_trace_degree=113039, full_reciprocal_degree=226078,
                   cofactor_degree=cost, maximal_binary_Frobenius_exponent=1, full_binary_radical_degree=801,
                   arithmetic='integer monic trace reduction modulo4p then actual coefficient division by p',
                   global_equivalence='EG2: H divides all residuals and is a unit modulo(J2,4)',
                   J_coefficients=divisor, canonical_J_mod4=theta,
                   Q_evaluations_mod4=q_weights, full_H_evaluations_mod4=weights,
                   each_term_evaluation_mod4=term_weights, original_restrictions_mod4=original,
                   restriction_valuations_through_mod4=values,
                   global_gates_via_EG2=gates,
                   binary_f15_orders={key: binary_order(poly, f15) for key, poly in original.items()},
                   binary_f15_initial_units={key: binary_initial_unit(poly, f15) for key, poly in original.items()},
                   half_f15_orders={key: binary_order(poly, f15) for key, poly in halves.items()},
                   half_f15_initial_units={key: binary_initial_unit(poly, f15) for key, poly in halves.items()},
                   author_self_check=True, independent_review=False,
                   no_full_Q_or_T_expansion=True, no_other_word_tested=True)
    output.mkdir(parents=True, exist_ok=True)
    temporary = output/'positive_word_residuals.json.partial'
    temporary.write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
    temporary.replace(output/'positive_word_residuals.json')
    print(json.dumps({key: payload[key] for key in ('global_gates_via_EG2',
                      'restriction_valuations_through_mod4', 'binary_f15_orders',
                      'binary_f15_initial_units', 'half_f15_orders')}))


if __name__ == '__main__':
    main()
