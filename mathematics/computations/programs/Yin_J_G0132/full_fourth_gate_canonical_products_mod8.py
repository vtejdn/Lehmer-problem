"""Completed AUTHOR probes of TWO literal canonical203/0 full-gate corrections.

Both actual products are evaluated separately modulo8 at the unchanged J144.
The integer endpoint480 identity is an additional control, not a replacement
for either computation. No exponent reduction, q substitution or F/8 class.
"""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import argparse
import json

from main import add, mul, rem, power, compose, chebyshev
from endpoint_word_mod8 import canonical, ringpower, integer_kernel, kernel, value_through_mod8
from endpoint_full_triple_image import totient
from odd_support_probe import binary_order, binary_initial_unit
from full_fourth_gate_known_word_span import Budget, publish

INPUT = 'inputs/full_fourth_gate_canonical_products.json'
NAMES = ('a','b','c','F','G','X_plus','X_minus')
PRIMES = (2,3,5)


def diagnostics(arrays,P):
    result = {}
    for name,values in arrays.items():
        quotients = []
        for shift in (1,2):
            if all(v % (1 << shift) == 0 for v in values):
                q = [v // (1 << shift) for v in values]
                quotients.append(dict(division_power=shift,coefficient_modulus=8 >> shift,
                    coefficients=q,binary_f15_order=binary_order(q,P),
                    binary_initial_unit=binary_initial_unit(q,P)))
        result[name] = dict(coefficient_valuation_through_mod8=value_through_mod8(values),
            binary_f15_order=binary_order(values,P),binary_initial_unit=binary_initial_unit(values,P),
            integral_dyadic_quotient_classes=quotients)
    return result


def main():
    here = Path(__file__).resolve().parent
    out = here.parents[1] / 'outputs' / here.name
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=out/'full_fourth_gate_canonical_products_mod8.json')
    parser.add_argument('--max-seconds',type=float,default=1800)
    parser.add_argument('--max-working-mib',type=float,default=1024)
    args = parser.parse_args()
    budget = Budget(args.max_seconds,args.max_working_mib)
    source = json.loads((here/INPUT).read_text(encoding='utf-8'))
    assert source['required_result_inputs'] == [
        'full_fourth_gate_known_word_span.json','full_fourth_gate_known_word_span_verification.json']
    span,checked = [json.loads((out/name).read_text(encoding='utf-8'))
                    for name in source['required_result_inputs']]
    for key in ('parameters','base','summary','generators','odd_lifts','principal_lifts',
                'relations','basis_lifts','known_words','source_basis','cases','selected_case_ids'):
        assert span[key] == checked[key]
    assert checked['all_positive_correction_raw_sources_and_full_costs_checked']
    assert checked['all32_reference_arrays_and64_full_targets_checked']
    row = next(r for r in span['cases'] if (r['source_mask'],r['coset_bits']) == (203,0))
    reference = row['reference']
    labels = [r['actual_label'] for r in span['generators']]
    assert source['source_selection'] == dict(source_mask=203,coset_bits=0)
    assert source['reference_bundle_words'] == reference['bundle_words']
    assert source['reference_literal_word'] == reference['literal_word']
    assert source['reference_costs'] == reference['costs']
    assert source['actual_endpoint_factor'] == 'X-2'
    assert source['original_exponents_retained_without_reduction']
    assert source['actual_q_not_residue'] and source['no_word_optimization']
    assert source['no_F_over8_class_or_mod16']
    assert [r['selected_sign'] for r in source['products']] == ['X_plus','X_minus']
    for product in source['products']:
        sign = product['selected_sign']; decision = row['targets'][sign]
        assert decision['member']
        correction = decision['correction']
        assert product['target_bits'] == decision['target_bits']
        assert product['source_basis_mask'] == decision['source_mask']
        assert product['correction_coordinates'] == correction['coordinates']
        assert product['correction_word'] == correction['word']
        assert product['correction_costs'] == correction['costs']
        bundles = dict(reference['bundle_words'])
        bundles['full_gate_correction'] = correction['word']
        assert product['bundle_words'] == bundles
        assert product['literal_word'] == [t for word in bundles.values() for t in word]
        terms = []
        for name,word in bundles.items():
            for position,(index,e) in enumerate(word):
                label = labels[index]
                term = {k:label[k] for k in ('kind','n','q','a','b','trace_degree') if k in label}
                term.update(index=index,exponent=e,degree_contribution=e*label['trace_degree'],
                            parent_word=name,parent_term_position=position)
                terms.append(term)
        assert product['terms'] == terms
        assert all(t['exponent'] > 0 for t in terms)
        counts = Counter({3:4,5:6,9:8,11:2,15:4,17:2,187:2,960:1})
        endpoint,degree = 4,374
        for term in terms:
            degree += term['degree_contribution']
            if term['kind'] == 'endpoint':
                endpoint += term['exponent']
            else:
                assert term['q'] == 3**term['a']*5**term['b']
                for r in range(2,term['n']+1):
                    if term['n'] % r == 0:
                        for a in range(term['a']+1):
                            for b in range(term['b']+1):
                                counts[r*3**a*5**b] += term['exponent']
        reciprocal = {1:2*endpoint,**counts}
        assert degree == endpoint+sum(e*totient(n)//2 for n,e in counts.items())
        assert 2*degree == sum(e*totient(n) for n,e in reciprocal.items())
        assert product['full_trace_factor_multiplicities'] == [
            dict(order=n,multiplicity=e) for n,e in sorted(counts.items())]
        assert product['full_reciprocal_cyclotomic_multiplicities'] == [
            dict(order=n,multiplicity=e) for n,e in sorted(reciprocal.items())]
        assert product['costs'] == dict(literal_term_count=len(terms),
            cofactor_trace_degree=degree-374,original_trace_degree=degree,
            original_reciprocal_degree=2*degree,cofactor_endpoint_exponent=endpoint-4,
            full_endpoint_trace_multiplicity=endpoint)
        assert degree == correction['resulting_original_trace_degree']
        assert endpoint == correction['resulting_endpoint_exponent']
    plus_input,minus_input = source['products']
    difference = Counter(dict(plus_input['correction_word']))
    difference.subtract(dict(minus_input['correction_word']))
    assert {i:e for i,e in difference.items() if e} == {0:480}
    assert source['endpoint_shift'] == dict(positive='X_plus',base='X_minus',
        extra_endpoint_exponent=480,exact_integer_exponent_difference=[[0,480]],
        no_mod960_reduction_in_this_identity=True)
    assert [len(r['terms']) for r in source['products']] == [432,431]
    assert [r['costs']['original_trace_degree'] for r in source['products']] == [181259583,181259103]
    P,F30 = [1,4,-4,-1,1],[1,-4,-4,1,1]
    V = compose(F30,chebyshev(32)); J = mul(power(P,4),V)
    H0 = power([-2,1],2)
    for factor,e in (([1,1],2),([-1,1,1],3),([1,-3,0,1],4),(integer_kernel(187),1)):
        H0 = mul(H0,power(factor,e))
    T0 = mul(J,power(H0,2))
    assert len(J) == 145 and len(T0) == 375
    assert (P,V,J,H0,T0) == tuple(span['base'][k] for k in ('P','V','J','H0','T0'))
    base_full,base_j,j_can,base_H = {},{},{},{}
    for p in PRIMES:
        key = str(p)
        base_full[key] = canonical(T0,p)  # numerator modulus8p, then integer /p
        base_j[key] = rem(base_full[key],J,8)
        j_can[key] = canonical(J,p)
        base_H[key] = ringpower(compose(H0,chebyshev(p),J,8),2,J)
        assert base_j[key] == rem(mul(base_H[key],j_can[key],8),J,8)
    assert base_full == span['base']['base_canonical_mod8']
    assert base_j == span['base']['base_restricted_mod8']
    assert j_can == span['base']['j_canonical_mod8']
    assert base_H == span['base']['base_H_evaluations_mod8']
    budget.check()

    @lru_cache(None)
    def cheb_pair(n):
        if n == 0:
            return (2,),(0,1)
        a,b = cheb_pair(n//2)
        even = rem(add(mul(list(a),list(a),8),[-2],modulus=8),J,8)
        odd = rem(add(mul(list(a),list(b),8),[0,1],-1,8),J,8)
        return (tuple(even),tuple(odd)) if n % 2 == 0 else (
            tuple(odd),tuple(rem(add(mul(list(b),list(b),8),[-2],modulus=8),J,8)))

    @lru_cache(None)
    def factor_value(index,p):
        label = labels[index]
        if label['kind'] == 'endpoint':
            value = add(chebyshev(p),[-2],modulus=8)
        else:
            argument = list(cheb_pair(p*label['q'])[0])
            value = kernel(label['n'],argument,J)
        return tuple(value)

    @lru_cache(None)
    def powered_value(index,p,e):
        return tuple(ringpower(list(factor_value(index,p)),e,J))

    products = []
    for selected in source['products']:
        original,weights,Hweights,bundle_weights,bindings = {},{},{},{},{}
        for p,name in zip(PRIMES,('a','b','c')):
            key = str(p); weight = [1]
            bundles = {k:[1] for k in selected['bundle_words']}
            binding = []
            for position,term in enumerate(selected['terms']):
                i,e = term['index'],term['exponent']
                powered = list(powered_value(i,p,e))
                weight = rem(mul(weight,powered,8),J,8)
                parent = term['parent_word']
                bundles[parent] = rem(mul(bundles[parent],powered,8),J,8)
                binding.append(dict(term_position=position,index=i,exponent=e,
                    parent_word=parent,parent_term_position=term['parent_term_position'],
                    factor_key=[i,p],power_key=[i,p,e]))
                if position % 32 == 0:
                    budget.check()
            ref_weight = [1]
            for parent in reference['bundle_words']:
                ref_weight = rem(mul(ref_weight,bundles[parent],8),J,8)
            assert ref_weight == reference['weights'][key]
            assert weight == rem(mul(ref_weight,bundles['full_gate_correction'],8),J,8)
            assert rem(mul(ref_weight,base_j[key],8),J,8) == reference['original_restrictions_mod8'][name]
            weights[key] = weight
            Hweights[key] = rem(mul(base_H[key],weight,8),J,8)
            bundle_weights[key] = bundles
            bindings[key] = binding
            original[name] = rem(mul(weight,base_j[key],8),J,8)
            assert original[name] == rem(mul(Hweights[key],j_can[key],8),J,8)
        a,b,c = (original[k] for k in ('a','b','c'))
        a3,a5,b2,b5,c2,c3 = [ringpower(v,e,J) for v,e in
            ((a,3),(a,5),(b,2),(b,5),(c,2),(c,3))]
        original['F'] = rem(add([2*v for v in c2],a5,-3),J,8)
        original['G'] = rem(add(c3,b5,-2),J,8)
        second = add(b2,a3,-1)
        original['X_plus'] = rem(add(second,original['G']),J,8)
        original['X_minus'] = rem(add(second,original['G'],-1),J,8)
        assert rem(add(original['X_plus'],original['X_minus'],-1),J,8) == rem([2*v for v in original['G']],J,8)
        gates = {f'{name}_mod{m}':all(v % m == 0 for v in original[name])
                 for name in ('F','X_plus','X_minus') for m in (2,4,8)}
        gates['G_nonzero_mod2'] = any(v % 2 for v in original['G'])
        products.append(dict(selected_sign=selected['selected_sign'],input_product=selected,
            Q_evaluations_mod8=weights,full_H_evaluations_mod8=Hweights,
            source_bundles_evaluations_mod8=bundle_weights,term_bindings=bindings,
            original_restrictions_mod8=original,diagnostics=diagnostics(original,P),
            global_residual_gates_via_H_unit_degree=gates,
            source_character_prediction_matches=(gates['F_mod8'] and gates[selected['selected_sign']+'_mod4'])))
        publish(args.output.with_suffix('.incomplete.json'),
                dict(complete=False,completed_products=products,resources=budget.check()))
        print(json.dumps(dict(selected_sign=selected['selected_sign'],gates=gates)),flush=True)
    factor_keys = sorted({(t['index'],p) for r in source['products'] for t in r['terms'] for p in PRIMES})
    power_keys = sorted({(t['index'],p,t['exponent']) for r in source['products'] for t in r['terms'] for p in PRIMES})
    assert len(factor_keys) == 495 and len(power_keys) == 1263
    factors = [dict(index=i,p=p,actual_label=labels[i],value=list(factor_value(i,p))) for i,p in factor_keys]
    powers = [dict(index=i,p=p,exponent=e,value=list(powered_value(i,p,e))) for i,p,e in power_keys]
    plus,minus = (r['original_restrictions_mod8'] for r in products)
    controls = dict(exact_integer_endpoint480_word_identity=True,
        C863_lower_gates_hold=all(r['global_residual_gates_via_H_unit_degree']['F_mod4'] and
            r['global_residual_gates_via_H_unit_degree']['X_plus_mod2'] for r in products),
        F_mod8_restrictions_equal=(plus['F'] == minus['F']),
        X_plus_mod4_equals_other_X_minus=(rem(plus['X_plus'],J,4)==rem(minus['X_minus'],J,4)),
        X_minus_mod4_equals_other_X_plus=(rem(plus['X_minus'],J,4)==rem(minus['X_plus'],J,4)),
        each_input_has_nonzero_binary_G=all(r['global_residual_gates_via_H_unit_degree']['G_nonzero_mod2'] for r in products))
    result = dict(scope='ONLY canonical203/0 plus/minus literal products; two complete own-originalmod8 calculations',
        selected_input=INPUT,required_result_inputs=source['required_result_inputs'],
        source_selection=source['source_selection'],endpoint_shift=source['endpoint_shift'],
        P_coefficients=P,V_coefficients=V,J_coefficients=J,H0_coefficients=H0,T20_base_coefficients=T0,
        quotient_degree=144,base_degree=374,actual_single_F960=True,
        canonical_scalar_precisions={'2':16,'3':24,'5':40},
        base_full_canonical_mod8=base_full,base_canonical_restricted_J_mod8=base_j,
        own_J_canonical_mod8=j_can,base_H_evaluations_mod8=base_H,
        factor_values=factors,powered_values=powers,products=products,endpoint480_controls=controls,
        summary=dict(product_count=2,literal_term_counts=[432,431],factor_value_count=495,
            powered_value_count=1263,term_prime_occurrences=2589,full_original_array_count=14,
            original_trace_degrees=[r['costs']['original_trace_degree'] for r in source['products']],
            predicted_selected_gate_matches=[r['source_character_prediction_matches'] for r in products]),
        no_actual_exponent_reduction=True,no_actual_q_residue_substitution=True,
        no_F_over8_class_or_mod16_inference=True,no_full_integer_word_expansion=True,
        no_other_word_profile_or_optimization=True,author_self_check=True,independent_review=False,
        resources=budget.check())
    publish(args.output,result,budget)
    checkpoint = args.output.with_suffix('.incomplete.json')
    if checkpoint.exists():
        checkpoint.unlink()
    print(json.dumps(dict(summary=result['summary'],endpoint480_controls=controls)),flush=True)


if __name__ == '__main__':
    main()
