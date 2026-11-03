"""Different AUTHOR check of TWO retained canonical203/0 original products.

Both selected products completed different AUTHOR verification.
The unchanged separately authored helper performs exact ZZ prime divisions and faithful degree288
Laurent arithmetic.  Actual q and every literal exponent remain unchanged.
Both products are computed separately; the endpoint480 identity is a control.
No producer arithmetic, F/8 class, modulus16, or third product is used.
"""
from pathlib import Path
from collections import Counter
import argparse
import json
import sympy as sp

from verify_complete_local_target_second_half_screen import IndependentArithmetic
from verify_positive_word_residuals import coefficients
from verify_joint_eighth_second_half_kernel_image import costs as positive_costs
from verify_full_fourth_gate_known_word_span import Budget, publish


INPUT = 'inputs/full_fourth_gate_canonical_products.json'
PRIMES = (2, 3, 5)
NAMES = ('a', 'b', 'c', 'F', 'G', 'X_plus', 'X_minus')
REQUIRED = ['full_fourth_gate_known_word_span.json',
            'full_fourth_gate_known_word_span_verification.json']


def reduced(values, modulus):
    answer = [v % modulus for v in values]
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def bind_product(product, source_row, labels):
    """Rebuild all literal terms and integral multiplicities before arithmetic."""
    sign = product['selected_sign']
    assert (product['source_mask'], product['coset_bits']) == (203, 0)
    decision = source_row['targets'][sign]
    assert decision['member']
    correction = decision['correction']
    assert product['target_bits'] == decision['target_bits']
    assert product['source_basis_mask'] == decision['source_mask']
    assert product['correction_coordinates'] == correction['coordinates']
    assert product['correction_word'] == correction['word']
    assert len(dict(correction['word'])) == len(correction['word'])
    assert product['correction_costs'] == correction['costs']
    assert positive_costs(dict(correction['word']), labels) == correction['costs']
    bundles = {**source_row['reference']['bundle_words'],
               'full_gate_correction': correction['word']}
    assert product['bundle_words'] == bundles
    literal = [term for word in bundles.values() for term in word]
    assert product['literal_word'] == literal
    terms = []
    for bundle_name, word in bundles.items():
        for position, (index, exponent) in enumerate(word):
            assert type(exponent) is int and exponent > 0
            label = labels[index]
            term = {k: label[k] for k in ('kind', 'n', 'q', 'a', 'b', 'trace_degree') if k in label}
            term.update(index=index, exponent=exponent,
                        degree_contribution=exponent * label['trace_degree'],
                        parent_word=bundle_name, parent_term_position=position)
            terms.append(term)
    assert product['terms'] == terms
    counts = Counter({3: 4, 5: 6, 9: 8, 11: 2, 15: 4, 17: 2, 187: 2, 960: 1})
    endpoint, degree = 4, 374
    for term in terms:
        degree += term['degree_contribution']
        if term['kind'] == 'endpoint':
            assert term['trace_degree'] == 1
            endpoint += term['exponent']
        else:
            assert term['kind'] == 'rectangle'
            assert term['q'] == 3**term['a'] * 5**term['b']
            assert term['trace_degree'] == term['q'] * (term['n'] - 1) // 2
            for divisor in sp.divisors(term['n']):
                if divisor == 1:
                    continue
                for a in range(term['a'] + 1):
                    for b in range(term['b'] + 1):
                        counts[int(divisor) * 3**a * 5**b] += term['exponent']
    trace_factors = [dict(order=n, multiplicity=e) for n, e in sorted(counts.items())]
    reciprocal = {1: 2 * endpoint, **counts}
    reciprocal_factors = [dict(order=n, multiplicity=e) for n, e in sorted(reciprocal.items())]
    assert degree == endpoint + sum(e * int(sp.totient(n)) // 2 for n, e in counts.items())
    assert 2 * degree == sum(e * int(sp.totient(n)) for n, e in reciprocal.items())
    assert product['full_trace_factor_multiplicities'] == trace_factors
    assert product['full_reciprocal_cyclotomic_multiplicities'] == reciprocal_factors
    assert product['costs'] == dict(literal_term_count=len(terms),
        cofactor_trace_degree=degree - 374, original_trace_degree=degree,
        original_reciprocal_degree=2 * degree, cofactor_endpoint_exponent=endpoint - 4,
        full_endpoint_trace_multiplicity=endpoint)
    assert correction['resulting_original_trace_degree'] == degree
    assert correction['resulting_reciprocal_degree'] == 2 * degree
    assert correction['resulting_endpoint_exponent'] == endpoint
    assert correction['resulting_complete_trace_factors'] == trace_factors
    assert correction['resulting_complete_reciprocal_factors'] == reciprocal_factors


def main():
    here = Path(__file__).resolve().parent
    out = here.parents[1] / 'outputs' / here.name
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=out / 'full_fourth_gate_canonical_products_mod8_verification.json')
    parser.add_argument('--max-seconds', type=float, default=1800)
    parser.add_argument('--max-working-mib', type=float, default=1024)
    args = parser.parse_args()
    budget = Budget(args.max_seconds, args.max_working_mib)
    source = json.loads((here / INPUT).read_text(encoding='utf-8'))
    saved = json.loads((out / 'full_fourth_gate_canonical_products_mod8.json').read_text(encoding='utf-8'))
    assert source['required_result_inputs'] == REQUIRED
    span, checked = [json.loads((out / name).read_text(encoding='utf-8')) for name in REQUIRED]
    for key in ('parameters', 'base', 'summary', 'generators', 'odd_lifts', 'principal_lifts',
                'relations', 'basis_lifts', 'known_words', 'source_basis', 'cases', 'selected_case_ids'):
        assert span[key] == checked[key]
    assert checked['all_positive_correction_raw_sources_and_full_costs_checked']
    assert checked['all32_reference_arrays_and64_full_targets_checked']
    source_row = next(r for r in span['cases'] if (r['source_mask'], r['coset_bits']) == (203, 0))
    reference = source_row['reference']
    labels = [r['actual_label'] for r in span['generators']]
    assert source['source_selection'] == dict(source_mask=203, coset_bits=0)
    assert source['reference_bundle_words'] == reference['bundle_words']
    assert source['reference_literal_word'] == reference['literal_word']
    assert source['reference_costs'] == reference['costs']
    assert source['actual_endpoint_factor'] == 'X-2'
    for flag in ('original_exponents_retained_without_reduction', 'actual_q_not_residue',
                 'no_word_optimization', 'no_F_over8_class_or_mod16'):
        assert source[flag]
    assert [p['selected_sign'] for p in source['products']] == ['X_plus', 'X_minus']
    for product in source['products']:
        bind_product(product, source_row, labels)
    plus_input, minus_input = source['products']
    difference = Counter()
    for index, exponent in plus_input['literal_word']:
        difference[index] += exponent
    for index, exponent in minus_input['literal_word']:
        difference[index] -= exponent
    assert {i: e for i, e in difference.items() if e} == {0: 480}
    assert labels[0] == dict(kind='endpoint', integer_factor='X-2', trace_degree=1)
    assert source['endpoint_shift'] == dict(positive='X_plus', base='X_minus',
        extra_endpoint_exponent=480, exact_integer_exponent_difference=[[0, 480]],
        no_mod960_reduction_in_this_identity=True)
    assert [len(p['terms']) for p in source['products']] == [432, 431]
    assert [p['costs']['original_trace_degree'] for p in source['products']] == [181259583, 181259103]
    assert saved['selected_input'] == INPUT and saved['required_result_inputs'] == REQUIRED
    assert saved['source_selection'] == source['source_selection']
    assert saved['endpoint_shift'] == source['endpoint_shift']
    assert len(saved['products']) == 2
    budget.check()

    # This helper independently constructs the exact integral cyclotomic base,
    # divides its three remainders in ZZ, and embeds J144 faithfully into the
    # degree288 reciprocal Laurent ring.  It imports no producer arithmetic.
    budget.phase = 'exact integer base and Laurent quotient'
    arithmetic = IndependentArithmetic(labels)
    ring = arithmetic.ring
    top = dict(P_coefficients=coefficients(arithmetic.P), V_coefficients=coefficients(arithmetic.V),
        J_coefficients=coefficients(arithmetic.J), H0_coefficients=coefficients(arithmetic.H),
        T20_base_coefficients=coefficients(arithmetic.base), quotient_degree=144, base_degree=374,
        actual_single_F960=True, canonical_scalar_precisions={'2': 16, '3': 24, '5': 40},
        base_full_canonical_mod8=arithmetic.base_full,
        base_canonical_restricted_J_mod8=arithmetic.base_restricted,
        own_J_canonical_mod8=arithmetic.j_canonical,
        base_H_evaluations_mod8={str(p): arithmetic.recover(arithmetic.base_weight[p]) for p in PRIMES})
    for key, value in top.items():
        assert saved[key] == value, key
    for key, value in (('base_canonical_mod8', arithmetic.base_full),
                       ('base_restricted_mod8', arithmetic.base_restricted),
                       ('j_canonical_mod8', arithmetic.j_canonical),
                       ('base_H_evaluations_mod8', top['base_H_evaluations_mod8'])):
        assert span['base'][key] == value
    budget.check()
    products = []
    for selected, supplied in zip(source['products'], saved['products']):
        budget.phase = 'literal product ' + selected['selected_sign']
        bundle_images = {}
        for bundle_name, word in selected['bundle_words'].items():
            bundle_images[bundle_name] = arithmetic.weights(word)
            budget.check()
        # Independently multiply the complete literal word, as well as all
        # four retained bundles; no period reduction or shift inference.
        weights = arithmetic.weights(selected['literal_word'])
        bundles, bindings = {}, {}
        for p in PRIMES:
            key = str(p)
            merged = ring.one
            for bundle in bundle_images.values():
                merged = ring.multiply(merged, bundle[p])
            assert merged == weights[p]
            previous = ring.one
            for bundle_name in reference['bundle_words']:
                previous = ring.multiply(previous, bundle_images[bundle_name][p])
            assert arithmetic.recover(previous) == reference['weights'][key]
            old_name = {2: 'a', 3: 'b', 5: 'c'}[p]
            assert ring.multiply(previous, arithmetic.image(arithmetic.base_restricted[key])) == \
                arithmetic.image(reference['original_restrictions_mod8'][old_name])
            bundles[key] = {name: arithmetic.recover(value[p]) for name, value in bundle_images.items()}
            bindings[key] = [dict(term_position=position, index=t['index'], exponent=t['exponent'],
                parent_word=t['parent_word'], parent_term_position=t['parent_term_position'],
                factor_key=[t['index'], p], power_key=[t['index'], p, t['exponent']])
                for position, t in enumerate(selected['terms'])]
        result = arithmetic.reference(weights)
        arrays = result['original_restrictions_mod8']
        assert tuple(arrays) == NAMES
        gates = result.pop('global_residual_gates_via_EPX_H_unit_degree')
        result.update(selected_sign=selected['selected_sign'], input_product=selected,
            source_bundles_evaluations_mod8=bundles, term_bindings=bindings,
            global_residual_gates_via_H_unit_degree=gates,
            source_character_prediction_matches=(gates['F_mod8'] and gates[selected['selected_sign'] + '_mod4']))
        assert result == supplied, selected['selected_sign']
        products.append(result)
        publish(args.output.with_suffix('.incomplete.json'), dict(complete=False,
            completed_products=products, resources=budget.check()), budget)
        print(json.dumps(dict(verified_product=selected['selected_sign'], gates=gates)), flush=True)

    budget.phase = 'all cached literal values and powers'
    factor_keys = sorted({(t['index'], p) for product in source['products'] for t in product['terms'] for p in PRIMES})
    power_keys = sorted({(t['index'], p, t['exponent']) for product in source['products'] for t in product['terms'] for p in PRIMES})
    assert len(factor_keys) == 495 and len(power_keys) == 1263
    assert arithmetic.used_values == {(p, i) for i, p in factor_keys}
    assert arithmetic.used_powers == {(p, i, e) for i, p, e in power_keys}
    factors = [dict(index=i, p=p, actual_label=labels[i],
                    value=arithmetic.recover(list(arithmetic.factor_value(p, i)))) for i, p in factor_keys]
    powers = [dict(index=i, p=p, exponent=e,
                   value=arithmetic.recover(list(arithmetic.factor_power(p, i, e)))) for i, p, e in power_keys]
    assert factors == saved['factor_values']
    assert powers == saved['powered_values']
    plus, minus = (product['original_restrictions_mod8'] for product in products)
    controls = dict(exact_integer_endpoint480_word_identity=True,
        C863_lower_gates_hold=all(r['global_residual_gates_via_H_unit_degree']['F_mod4'] and
            r['global_residual_gates_via_H_unit_degree']['X_plus_mod2'] for r in products),
        F_mod8_restrictions_equal=(plus['F'] == minus['F']),
        X_plus_mod4_equals_other_X_minus=(reduced(plus['X_plus'], 4) == reduced(minus['X_minus'], 4)),
        X_minus_mod4_equals_other_X_plus=(reduced(plus['X_minus'], 4) == reduced(minus['X_plus'], 4)),
        each_input_has_nonzero_binary_G=all(r['global_residual_gates_via_H_unit_degree']['G_nonzero_mod2'] for r in products))
    assert controls == saved['endpoint480_controls']
    summary = dict(product_count=2, literal_term_counts=[432, 431], factor_value_count=495,
        powered_value_count=1263, term_prime_occurrences=sum(3 * len(p['terms']) for p in source['products']),
        full_original_array_count=14,
        original_trace_degrees=[p['costs']['original_trace_degree'] for p in source['products']],
        predicted_selected_gate_matches=[p['source_character_prediction_matches'] for p in products])
    assert summary == saved['summary'] and summary['term_prime_occurrences'] == 2589
    for flag in ('no_actual_exponent_reduction', 'no_actual_q_residue_substitution',
                 'no_F_over8_class_or_mod16_inference', 'no_full_integer_word_expansion',
                 'no_other_word_profile_or_optimization', 'author_self_check'):
        assert saved[flag]
    assert saved['independent_review'] is False
    result = dict(scope='Different AUTHOR Laurent288 check of exactly TWO canonical203/0 products',
        selected_input=INPUT, required_result_inputs=REQUIRED, source_selection=source['source_selection'],
        endpoint_shift=source['endpoint_shift'], **top, factor_values=factors, powered_values=powers,
        products=products, endpoint480_controls=controls, summary=summary,
        all_retained_words_and_integral_factor_costs_independently_checked=True,
        both_original_products_independently_evaluated=True,
        all2589_literal_term_prime_bindings_checked=True,
        all495_factor_values_and1263_powered_values_checked=True,
        all14_original_mod8_arrays_and_genuine_half_quarters_checked=True,
        all_three_base_and_J_prime_divisions_over_ZZ_checked=True,
        endpoint480_identity_checked_without_using_it_to_infer_either_product=True,
        no_actual_exponent_or_q_reduction=True, no_F_over8_class_or_mod16=True,
        no_other_word_profile_optimization_or_full_polynomial_expansion=True,
        author_self_check=True, independent_review=False, resources=budget.check())
    publish(args.output, result, budget)
    checkpoint = args.output.with_suffix('.incomplete.json')
    if checkpoint.exists():
        checkpoint.unlink()
    print(json.dumps(dict(status='PASS', summary=summary, endpoint480_controls=controls,
                         resources=budget.check())), flush=True)


if __name__ == '__main__':
    main()
