"""Different AUTHOR degree288 Laurent check of the ONE literal mask203 product.
All268 original terms, unreduced exponents and actual q values are retained.
No new producer code is imported; original prime divisions occur over Z.
"""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import json
import sympy as sp
from verify_positive_word_residuals import LaurentRing,trace_factor,coefficients,binary_diagnostic,x,z,C
from verify_endpoint_word_mod8 import poly,reduced_coefficients

def main():
    here=Path(__file__).resolve().parent
    output=here.parents[3]/'mathematics/computations/outputs'/here.name
    word=json.loads((here/'inputs/joint_mask203_product_word.json').read_text(encoding='utf-8'))
    saved=json.loads((output/'joint_mask203_product_mod8.json').read_text(encoding='utf-8'))
    assert saved['selected_input']=='inputs/joint_mask203_product_word.json'
    assert saved['terms']==word['terms'] and len(word['terms'])==268
    assert word['required_result_inputs']==[
        'complete_local_target_second_half_screen.json',
        'complete_local_target_second_half_screen_verification.json',
        'joint_eighth_second_half_kernel_image.json',
        'joint_eighth_second_half_kernel_image_verification.json']
    screen=json.loads((output/'complete_local_target_second_half_screen.json').read_text(encoding='utf-8'))
    screencheck=json.loads((output/'complete_local_target_second_half_screen_verification.json').read_text(encoding='utf-8'))
    joint=json.loads((output/'joint_eighth_second_half_kernel_image.json').read_text(encoding='utf-8'))
    jointcheck=json.loads((output/'joint_eighth_second_half_kernel_image_verification.json').read_text(encoding='utf-8'))
    assert screen['summary']==screencheck['summary']
    assert screencheck['all32_branches_independently_derived']
    assert screencheck['all7_full_mod8_arrays_and_genuine_half_quarters_checked']
    assert joint['summary']==jointcheck['summary']
    assert jointcheck['both120_relation_span_inclusions_checked']
    assert jointcheck['all16_target_jets_and_A_only_decisions_independently_recomputed']
    source=next(r for r in screen['records'] if r['source_mask']==203)
    assert source['branch']==2 and source['selected_kernel']['h']==44
    assert source['outcome']=='unresolved_ambient_member' and source['product_reference']=='QK:203'
    old_data=screen['references']['QK:203']
    prior=screencheck['references']['QK:203']
    assert old_data=={k:v for k,v in prior.items() if k!='diagnostics'}
    target=next(r for r in joint['targets'] if r['source_mask']==203)
    targetcheck=next(r for r in jointcheck['targets'] if r['source_mask']==203)
    assert target==targetcheck and target['reference']==old_data
    assert target['decision']['member']
    labels=[r['actual_label'] for r in joint['generators']]
    assert labels[:4192]==screen['labels']
    expected_words=[old_data['bundle_words']['Q'],old_data['bundle_words']['K'],target['decision']['word']]
    assert [len(w) for w in expected_words]==[69,72,127]
    # Bind all literal occurrences in the three contiguous retained bundles.
    bundle_labels=[word['terms'][i]['parent_word'] for i in (0,69,141)]
    assert bundle_labels==['Q203','K44','jointK203']
    assert word['bundle_words']==dict(zip(bundle_labels,expected_words))
    assert word['old_kernel_h']==44 and word['reference_key']=='QK:203'
    assert word['joint_target_bits']==target['decision']['target_bits']
    assert word['joint_kernel_vector']==target['decision']['normalization_kernel_vector']
    expected=[]
    for label,bundle in zip(bundle_labels,expected_words):
        for position,(index,exponent) in enumerate(bundle):
            src=labels[index]
            term={k:src[k] for k in ('kind','n','q','a','b','trace_degree') if k in src}
            term.update(index=index,exponent=exponent,degree_contribution=exponent*src['trace_degree'],
                        parent_word=label,parent_term_position=position)
            expected.append(term)
    assert word['terms']==expected and word['source_mask']==203 and word['branch']==2
    assert word['no_F_over8_class_or_mod16_inference']
    assert word['original_exponents_retained_without_mod960'] and word['actual_q_not_residue']
    counts=Counter({3:4,5:6,9:8,11:2,15:4,17:2,187:2,960:1})
    for term in word['terms']:
        if term['kind']=='rectangle':
            for r in sp.divisors(term['n'])[1:]:
                for a in range(term['a']+1):
                    for b in range(term['b']+1):
                        counts[int(r)*3**a*5**b]+=term['exponent']
    assert word['full_trace_factor_multiplicities']==[dict(order=n,multiplicity=e) for n,e in sorted(counts.items())]
    assert word['full_endpoint_trace_multiplicity']==815
    assert word['full_Phi1_multiplicity']==1630 and len(counts)==136
    assert 815+sum(e*int(sp.totient(n))//2 for n,e in counts.items())==65635185
    reciprocal={1:1630,**counts}
    assert word['full_reciprocal_cyclotomic_multiplicities']==[dict(order=n,multiplicity=e) for n,e in sorted(reciprocal.items())]
    assert sum(e*int(sp.totient(n)) for n,e in reciprocal.items())==131270370
    assert saved['costs']==word['costs'] and word['costs']['endpoint_exponent']==811
    assert word['costs']==dict(endpoint_exponent=811,nonzero_terms=268,
        cofactor_trace_degree=65634811,original_trace_degree=65635185,original_reciprocal_degree=131270370)
    assert word['actual_endpoint_factor']=='X-2'
    assert sum(t['exponent'] for t in word['terms'] if t['kind']=='endpoint')==811
    assert sum(t['degree_contribution'] for t in word['terms'])==65634811
    factors={n:trace_factor(n) for n in (3,5,9,11,15,17,187,480,960)}
    h0=(sp.Poly((x-2)**2,x)*factors[3]**2*factors[5]**3*factors[9]**4
        *factors[11]*factors[17]*factors[187])
    j2=factors[15]**4*factors[960]
    base=j2*h0**2
    assert factors[960]==factors[480].compose(C[2]) and factors[960]!=factors[480]**2
    assert base.degree()==374 and j2.degree()==144 and h0.degree()==115
    assert coefficients(base)==saved['T20_base_coefficients']
    assert coefficients(j2)==saved['J_coefficients'] and coefficients(h0)==saved['H0_coefficients']
    reciprocal=sp.Poly(sp.cyclotomic_poly(15,z)**4*sp.cyclotomic_poly(960,z),z,domain=sp.ZZ)
    assert reciprocal.degree()==288
    # Check the exact integral reciprocal identity without evaluating at roots.
    expansion=sp.Poly(0,z,domain=sp.ZZ)
    for i in range(145):
        for k in range(i+1):
            expansion+=sp.Poly(int(j2.nth(i))*int(sp.binomial(i,k))*z**(144+i-2*k),z)
    assert expansion==reciprocal
    rings={m:LaurentRing(reciprocal,m) for m in (2,4,8)}
    ring=rings[8]
    trace=ring.argument(1)

    # A full triangular recovery, valid over Z/8 as well as over fields.
    trace_powers=[ring.one]
    for _ in range(143):
        trace_powers.append(ring.multiply(trace_powers[-1],trace))
    shift=ring.power(ring.z,143)
    shifted=[ring.multiply(shift,p) for p in trace_powers]
    sparse_trace_powers=[[(i,v) for i,v in enumerate(row) if v] for row in trace_powers]
    @lru_cache(maxsize=8192)
    def linear_image(values,modulus):
        # A complete trace polynomial is embedded by its PRECOMPUTED basis,
        # not by recomputing up to143 Laurent multiplications for each array.
        # Reducing those modulo8 basis arrays modulo4 or2 is the same exact
        # monic quotient map, so normalized half/quarter comparisons stay full.
        result=[0]*288
        assert len(values)<=144
        for degree,coefficient in enumerate(values):
            coefficient%=modulus
            if coefficient:
                for i,v in sparse_trace_powers[degree]:
                    result[i]+=coefficient*v
        return tuple(v%modulus for v in result)
    def image(values,modulus=8):
        return list(linear_image(tuple(values),modulus))
    def recover(value):
        work=ring.multiply(shift,value)
        assert work[287]==0
        result=[0]*144
        for j in range(143,-1,-1):
            coefficient=work[143+j]
            result[j]=coefficient
            if coefficient:
                work=ring.add(work,shifted[j],-coefficient)
        assert not any(work)
        while len(result)>1 and result[-1]==0:
            result.pop()
        return result

    @lru_cache(None)
    def kernel(n,index):
        # z^(-index*a) sum_(j=0..n-1) z^(index*j), exact at full modulus8.
        unit=ring.power(ring.z,index)
        def power_and_sum(length):
            # Exact denominator-free identities for t^length and S_length(t).
            # S_(2m)=(1+t^m)S_m; S_(2m+1)=S_(2m)+t^(2m).
            # Actual index=p*q is unchanged; no finite-image period is used.
            if length==0:
                return ring.one,[0]*288
            half_power,half_sum=power_and_sum(length//2)
            even_power=ring.multiply(half_power,half_power)
            even_sum=ring.add(half_sum,ring.multiply(half_power,half_sum))
            if length%2:
                return ring.multiply(even_power,unit),ring.add(even_sum,even_power)
            return even_power,even_sum
        _,total=power_and_sum(n)
        centered=ring.multiply(ring.power(ring.zi,index*((n-1)//2)),total)
        return tuple(centered)

    actual,base_int_restricted,q_saved,h_saved={},{},{},{}
    bundle_saved={}
    for p,name in ((2,'a'),(3,'b'),(5,'c')):
        # TRUE full-Z canonical remainder at the complete degree374 base.
        numerator=base.compose(C[p]).rem(base)
        assert all(int(v)%p==0 for v in numerator.all_coeffs())
        canonical=sp.Poly.from_list([int(v)//p for v in numerator.all_coeffs()],x,domain=sp.ZZ)
        assert reduced_coefficients(canonical,8)==saved['base_full_canonical_mod8'][str(p)]
        base_j=canonical.rem(j2)
        assert reduced_coefficients(base_j,8)==saved['base_canonical_restricted_J_mod8'][str(p)]
        j_numerator=j2.compose(C[p]).rem(j2)
        assert all(int(v)%p==0 for v in j_numerator.all_coeffs())
        j_canonical=sp.Poly.from_list([int(v)//p for v in j_numerator.all_coeffs()],x,domain=sp.ZZ)
        assert reduced_coefficients(j_canonical,8)==saved['own_J_canonical_mod8'][str(p)]
        argument=ring.argument(p)
        base_weight=ring.power(ring.evaluate(h0,argument),2)
        assert ring.multiply(base_weight,image(reduced_coefficients(j_canonical,8)))==image(reduced_coefficients(base_j,8))
        q_weight=ring.one
        bundle={label:ring.one[:] for label in bundle_labels}
        records=saved['all804_term_evaluations_mod8'][str(p)]
        assert len(records)==268
        for term,record in zip(word['terms'],records):
            assert all(record[key]==value for key,value in term.items())
            if term['kind']=='endpoint':
                factor=argument[:]
                factor[0]=(factor[0]-2)%8
            else:
                assert term['q']==3**term['a']*5**term['b']
                factor=list(kernel(term['n'],p*term['q']))
            assert factor==image(record['evaluated_factor'])
            powered=ring.power(factor,term['exponent'])
            assert powered==image(record['evaluated_power'])
            q_weight=ring.multiply(q_weight,powered)
            label=term['parent_word']
            bundle[label]=ring.multiply(bundle[label],powered)
        assert bundle[bundle_labels[0]]==image(old_data['bundle_weights'][str(p)]['Q'])
        assert bundle[bundle_labels[1]]==image(old_data['bundle_weights'][str(p)]['K'])
        prefix=ring.multiply(bundle[bundle_labels[0]],bundle[bundle_labels[1]])
        assert prefix==image(old_data['weights'][str(p)])
        assert q_weight==ring.multiply(prefix,bundle[bundle_labels[2]])
        for label in bundle_labels:
            assert bundle[label]==image(saved['source_bundles_evaluations_mod8'][str(p)][label])
        bundle_saved[p]={label:recover(v) for label,v in bundle.items()}
        h_weight=ring.multiply(base_weight,q_weight)
        assert q_weight==image(saved['Q_evaluations_mod8'][str(p)])
        assert h_weight==image(saved['full_H_evaluations_mod8'][str(p)])
        actual[name]=ring.multiply(q_weight,image(reduced_coefficients(base_j,8)))
        assert actual[name]==ring.multiply(h_weight,image(reduced_coefficients(j_canonical,8)))
        base_int_restricted[p]=coefficients(base_j)
        q_saved[p],h_saved[p]=recover(q_weight),recover(h_weight)
        print(f'all268 actual factors and powers checked at p={p}',flush=True)
    a,b,c=[actual[key] for key in ('a','b','c')]
    ap={e:ring.power(a,e) for e in (3,5)}
    bp={e:ring.power(b,e) for e in (2,5)}
    cp={e:ring.power(c,e) for e in (2,3)}
    actual['F']=ring.add([2*v%8 for v in cp[2]],ap[5],-3)
    actual['G']=ring.add(cp[3],bp[5],-2)
    second=ring.add(bp[2],ap[3],-1)
    actual['X_plus']=ring.add(second,actual['G'])
    actual['X_minus']=ring.add(second,actual['G'],-1)
    assert ring.add(actual['X_plus'],actual['X_minus'],-1)==[2*v%8 for v in actual['G']]
    recovered={name:recover(value) for name,value in actual.items()}
    assert recovered==saved['original_restrictions_mod8']
    f=sp.Poly(x**4+x**3+1,x,modulus=2)
    diagnostics={}
    for name,values in recovered.items():
        valuation=min((v&-v).bit_length()-1 for v in values if v) if any(values) else 'at_least_3'
        order,unit=binary_diagnostic(values,f)
        quotients=[]
        for shift_power in (1,2):
            scale=1<<shift_power
            if all(v%scale==0 for v in values):
                divided=[v//scale for v in values]
                qorder,qunit=binary_diagnostic(divided,f)
                assert all(v%scale==0 for v in actual[name])
                assert image(divided,8//scale)==[v//scale for v in actual[name]]
                quotients.append(dict(division_power=shift_power,coefficient_modulus=8//scale,
                    coefficients=divided,binary_f15_order=qorder,binary_initial_unit=qunit))
        diagnostics[name]=dict(coefficient_valuation_through_mod8=valuation,binary_f15_order=order,
            binary_initial_unit=unit,integral_dyadic_quotient_classes=quotients)
    assert diagnostics==saved['diagnostics']
    assert saved['no_F_over8_class_or_mod16_inference']
    assert all(q['division_power'] in (1,2) for row in diagnostics.values()
               for q in row['integral_dyadic_quotient_classes'])
    gates={f'{name}_mod{m}':all(v%m==0 for v in recovered[name])
           for name in ('F','X_plus','X_minus') for m in (2,4,8)}
    gates['G_nonzero_mod2']=any(v%2 for v in recovered['G'])
    assert gates==saved['global_residual_gates_via_EPX_H_unit_degree']
    quarter=next((d for d in diagnostics['F']['integral_dyadic_quotient_classes'] if d['division_power']==2),None)
    lowest_cancelled=quarter is not None and (quarter['binary_f15_order']=='infinity' or quarter['binary_f15_order']>=8)
    assert lowest_cancelled==saved['lowest_quarter_mod_f8_cancelled']
    result=dict(scope='same ONE literal69+72+127-term mask203 product, all7 ORIGINAL residue arrays modulo8',
        selected_input='inputs/joint_mask203_product_word.json',source_mask=203,branch=2,
        all_three_bundles_bound_to_completed_certificates=True,bundle_words=word['bundle_words'],
        joint_target_bits=word['joint_target_bits'],joint_kernel_vector=word['joint_kernel_vector'],
        quotient_trace_degree=144,Laurent_degree=288,actual_base_degree=374,
        costs=word['costs'],true_full_Z_base_and_J_prime_divisions_checked=True,
        exact_single_F960_and_integral_trace_identity_checked=True,
        all804_term_values_and_powers_checked=True,all_three_Q_and_H_weights_checked=True,
        all7_full_mod8_trace_arrays_recovered_and_matched=True,
        original_restrictions_mod8=recovered,original_Laurent_restrictions_mod8=actual,
        Q_evaluations_mod8=q_saved,full_H_evaluations_mod8=h_saved,source_bundles_evaluations_mod8=bundle_saved,
        lowest_quarter_mod_f8_cancelled=lowest_cancelled,no_actual_exponent_reduction=True,no_actual_q_residue_substitution=True,
        true_integer_base_canonical_J_restrictions=base_int_restricted,
        diagnostics=diagnostics,global_residual_gates_via_EPX_H_unit_degree=gates,
        arithmetic='full-Z SymPy base canonical divisions, denominator-free Laurent geometric sums, exact integer convolution, linear full-trace embeddings and triangular recovery',
        sympy_version=sp.__version__,author_self_check=True,independent_review=False,
        no_F_over8_class_or_mod16_inference=True,
        no_full_integer_word_expansion=True,no_other_word_or_profile=True)
    temporary=output/'joint_mask203_product_mod8_verification.json.partial'
    temporary.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    temporary.replace(output/'joint_mask203_product_mod8_verification.json')
    summary={key:result[key] for key in ('all804_term_values_and_powers_checked','all_three_Q_and_H_weights_checked',
             'all7_full_mod8_trace_arrays_recovered_and_matched','global_residual_gates_via_EPX_H_unit_degree')}
    summary['lowest_quarter_mod_f8_cancelled']=lowest_cancelled
    summary['valuations']={name:row['coefficient_valuation_through_mod8'] for name,row in diagnostics.items()}
    summary['nonzero_divided_orders']={name:[(q['division_power'],q['binary_f15_order'],q['binary_initial_unit'])
        for q in row['integral_dyadic_quotient_classes'] if q['binary_f15_order']!='infinity'] for name,row in diagnostics.items()}
    print(json.dumps(summary))


if __name__=='__main__':
    main()
