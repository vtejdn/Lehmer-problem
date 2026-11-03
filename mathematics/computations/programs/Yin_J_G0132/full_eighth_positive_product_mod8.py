"""ONE literal138+126-term Q0L product: all ORIGINAL residues modulo8.
No actual exponent reduction, residue-q substitution or other word is used.
Only unchanged fixed producer functions are imported as arithmetic helpers.
"""
from pathlib import Path
from functools import lru_cache
from collections import Counter
from math import gcd
import json
from main import add,mul,rem,power,compose,chebyshev
from odd_support_probe import binary_order,binary_initial_unit
from endpoint_word_mod8 import ringpower,integer_kernel,kernel,canonical,value_through_mod8
from endpoint_full_triple_image import totient

def main():
    here=Path(__file__).resolve().parent
    output=here.parents[3]/'mathematics/computations/outputs'/here.name
    source=json.loads((here/'inputs/full_eighth_positive_product_word.json').read_text(encoding='utf-8'))
    terms=source['terms']
    assert len(terms)==264 and source['source_mask']==819 and source['branch']==2
    assert source['no_F_over8_class_or_mod16_inference']
    old_q=json.loads((here/source['source_Q0']).read_text(encoding='utf-8'))
    kernel_word=json.loads((here/source['source_L']).read_text(encoding='utf-8'))
    expected=[]
    for label,word in [('Q0',old_q),('L',kernel_word)]:
        for position,term in enumerate(word['terms']):
            expected.append(dict(term,parent_word=label,parent_term_position=position))
    assert terms==expected and len(old_q['terms'])==138 and len(kernel_word['terms'])==126
    assert source['full_additive_target']==kernel_word['target']
    assert source['original_exponents_retained_without_mod960'] and source['actual_q_not_residue']
    old_data=json.loads((output/'endpoint_kernel_product_mod8.json').read_text(encoding='utf-8'))
    assert old_data['terms']==old_q['terms']
    counts=Counter({3:4,5:6,9:8,11:2,15:4,17:2,187:2,960:1})
    for term in terms:
        if term['kind']=='rectangle':
            for r in range(2,term['n']+1):
                if term['n']%r==0:
                    for a in range(term['a']+1):
                        for b in range(term['b']+1):
                            counts[r*3**a*5**b]+=term['exponent']
    assert source['full_trace_factor_multiplicities']==[dict(order=n,multiplicity=e) for n,e in sorted(counts.items())]
    assert source['full_endpoint_trace_multiplicity']==455
    assert 455+sum(e*totient(n)//2 for n,e in counts.items())==93162348
    assert source['actual_endpoint_factor']=='X-2'
    assert terms[0]['kind']=='endpoint' and terms[0]['exponent']==211
    assert all(t['kind']=='endpoint' or (t['kind']=='rectangle' and t['n']>1 and gcd(t['n'],30)==1
               and t['q']==3**t['a']*5**t['b']) for t in terms)
    assert sum(t['exponent'] for t in terms if t['kind']=='endpoint')==451
    assert sum(t['degree_contribution'] for t in terms)==source['costs']['cofactor_trace_degree']==93161974
    assert source['costs']['original_trace_degree']==93162348 and source['costs']['original_reciprocal_degree']==186324696
    f3,f5,f9=[1,1],[-1,1,1],[1,-3,0,1]
    ff,f30=[1,4,-4,-1,1],[1,-4,-4,1,1]
    v32=compose(f30,chebyshev(32))
    divisor=mul(power(ff,4),v32)
    h0=power([-2,1],2)
    for factor,exponent in ((f3,2),(f5,3),(f9,4),(integer_kernel(187),1)):
        h0=mul(h0,power(factor,exponent))
    base=mul(divisor,power(h0,2))
    assert len(divisor)-1==144 and len(h0)-1==115 and len(base)-1==374

    @lru_cache(None)
    def cheb_pair(n):
        if n==0:
            return (2,),(0,1)
        a,b=cheb_pair(n//2)
        even=rem(add(mul(list(a),list(a),8),[-2],modulus=8),divisor,8)
        odd=rem(add(mul(list(a),list(b),8),[0,1],-1,8),divisor,8)
        if n%2==0:
            return tuple(even),tuple(odd)
        following=rem(add(mul(list(b),list(b),8),[-2],modulus=8),divisor,8)
        return tuple(odd),tuple(following)

    base_canonical,base_restricted,j_canonical={},{},{}
    q_weights,h_weights,each_term,original={},{},{},{}
    bundle_weights={}
    for p,name in ((2,'a'),(3,'b'),(5,'c')):
        # Full actual T_(2,0) canonical numerator modulo8p, then INTEGER /p.
        base_can=canonical(base,p)
        base_j=rem(base_can,divisor,8)
        theta_j=canonical(divisor,p)
        hp=compose(h0,chebyshev(p),divisor,8)
        hp2=ringpower(hp,2,divisor)
        assert base_j==rem(mul(hp2,theta_j,8),divisor,8)
        base_canonical[p],base_restricted[p],j_canonical[p]=base_can,base_j,theta_j
        weight=[1]
        bundle={'Q0':[1],'L':[1]}
        records=[]
        for term in terms:
            if term['kind']=='endpoint':
                value=add(chebyshev(p),[-2],modulus=8)
            else:
                # Exact C_(p*q) doubling identities, with ACTUAL q and no mod8 period assumption.
                argument=list(cheb_pair(p*term['q'])[0])
                value=kernel(term['n'],argument,divisor)
            powered=ringpower(value,term['exponent'],divisor)
            weight=rem(mul(weight,powered,8),divisor,8)
            label=term['parent_word']
            bundle[label]=rem(mul(bundle[label],powered,8),divisor,8)
            records.append(dict(**term,evaluated_factor=value,evaluated_power=powered))
        assert bundle['Q0']==old_data['Q_evaluations_mod8'][str(p)]
        assert weight==rem(mul(bundle['Q0'],bundle['L'],8),divisor,8)
        bundle_weights[p]=bundle
        q_weights[p]=weight
        h_weights[p]=rem(mul(hp2,weight,8),divisor,8)
        each_term[p]=records
        original[name]=rem(mul(weight,base_j,8),divisor,8)
        assert original[name]==rem(mul(h_weights[p],theta_j,8),divisor,8)
    a,b,c=[original[key] for key in ('a','b','c')]
    ap={e:ringpower(a,e,divisor) for e in (3,5)}
    bp={e:ringpower(b,e,divisor) for e in (2,5)}
    cp={e:ringpower(c,e,divisor) for e in (2,3)}
    original['F']=rem(add([2*v for v in cp[2]],ap[5],-3),divisor,8)
    original['G']=rem(add(cp[3],bp[5],-2),divisor,8)
    second=add(bp[2],ap[3],-1)
    original['X_plus']=rem(add(second,original['G']),divisor,8)
    original['X_minus']=rem(add(second,original['G'],-1),divisor,8)
    assert rem(add(original['X_plus'],original['X_minus'],-1),divisor,8)==rem([2*v for v in original['G']],divisor,8)
    diagnostics={}
    for name,poly in original.items():
        quotients=[]
        for shift in (1,2):
            if all(v%(1<<shift)==0 for v in poly):
                q=[v//(1<<shift) for v in poly]
                quotients.append(dict(division_power=shift,coefficient_modulus=8//(1<<shift),
                    coefficients=q,binary_f15_order=binary_order(q,ff),binary_initial_unit=binary_initial_unit(q,ff)))
        diagnostics[name]=dict(coefficient_valuation_through_mod8=value_through_mod8(poly),
            binary_f15_order=binary_order(poly,ff),binary_initial_unit=binary_initial_unit(poly,ff),
            integral_dyadic_quotient_classes=quotients)
    gates={f'{name}_mod{m}':all(v%m==0 for v in original[name])
           for name in ('F','X_plus','X_minus') for m in (2,4,8)}
    gates['G_nonzero_mod2']=any(v%2 for v in original['G'])
    quarter=next((d for d in diagnostics['F']['integral_dyadic_quotient_classes'] if d['division_power']==2),None)
    lowest_cancelled=quarter is not None and (quarter['binary_f15_order']=='infinity' or quarter['binary_f15_order']>=8)
    result=dict(scope='ONLY literal138+126-term Q0L product; all7 ORIGINAL classes modulo8',
        selected_input='inputs/full_eighth_positive_product_word.json',terms=terms,costs=source['costs'],
        J_coefficients=divisor,H0_coefficients=h0,T20_base_coefficients=base,
        quotient_degree=144,base_degree=374,full_trace_degree=93162348,full_reciprocal_degree=186324696,
        actual_single_F960=True,canonical_scalar_precisions={'2':16,'3':24,'5':40},
        base_full_canonical_mod8=base_canonical,base_canonical_restricted_J_mod8=base_restricted,
        own_J_canonical_mod8=j_canonical,Q_evaluations_mod8=q_weights,full_H_evaluations_mod8=h_weights,
        all792_term_evaluations_mod8=each_term,source_Q0_and_L_evaluations_mod8=bundle_weights,original_restrictions_mod8=original,
        diagnostics=diagnostics,global_residual_gates_via_EPX_H_unit_degree=gates,
        lowest_quarter_mod_f8_cancelled=lowest_cancelled,
        no_F_over8_class_or_mod16_inference=True,
        predicted_full_F8_matches=gates['F_mod8'],
        no_actual_exponent_reduction=True,no_actual_q_residue_substitution=True,
        initial_F4_X2_prediction_matches=(gates['F_mod4'] and gates['X_plus_mod2'] and gates['X_minus_mod2']),
        no_full_integer_word_expansion=True,no_other_word_or_profile=True,
        author_self_check=True,independent_review=False)
    output.mkdir(parents=True,exist_ok=True)
    temporary=output/'full_eighth_positive_product_mod8.json.partial'
    temporary.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    temporary.replace(output/'full_eighth_positive_product_mod8.json')
    print(json.dumps(dict(gates=gates,lowest_quarter_mod_f8_cancelled=lowest_cancelled,
        diagnostics={name:{k:v for k,v in row.items() if k!='integral_dyadic_quotient_classes'}|dict(
            divided=[{k:v for k,v in q.items() if k!='coefficients'} for q in row['integral_dyadic_quotient_classes']])
            for name,row in diagnostics.items()})))


if __name__=='__main__':
    main()
