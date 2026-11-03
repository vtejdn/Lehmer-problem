"""ONE retained65-term endpoint/rectangle word: actual ORIGINAL residues mod8.

Only the degree374 base and degree144 divisor are expanded.  The full
degree3390998 input is evaluated through exact canonical cofactor transfer.
"""
from pathlib import Path
from functools import lru_cache
import json
from math import gcd
from main import add,mul,rem,power,compose,chebyshev,trim
from odd_support_probe import binary_order,binary_initial_unit


def ringpower(value,exponent,divisor,modulus=8):
    result=[1]
    while exponent:
        if exponent&1:
            result=rem(mul(result,value,modulus),divisor,modulus)
        exponent//=2
        if exponent:
            value=rem(mul(value,value,modulus),divisor,modulus)
    return result


def integer_kernel(n):
    result=[1]
    for j in range(1,(n-1)//2+1):
        result=add(result,chebyshev(j))
    return result


def kernel(n,argument,divisor):
    previous,current,result=[2],argument,[1]
    for j in range(1,(n-1)//2+1):
        result=rem(add(result,current,modulus=8),divisor,8)
        if j<(n-1)//2:
            previous,current=current,rem(add(mul(argument,current,8),previous,-1,8),divisor,8)
    return result


def canonical(poly,p):
    numerator=compose(poly,chebyshev(p),poly,8*p)
    assert all(value%p==0 for value in numerator)
    return trim([value//p for value in numerator])


def value_through_mod8(poly):
    if not any(poly):
        return 'at_least_3'
    return min((value&-value).bit_length()-1 for value in poly if value)


def main():
    here=Path(__file__).resolve().parent
    output=here.parents[3]/'mathematics/computations/outputs'/here.name
    source=json.loads((here/'inputs/endpoint_full_triple_positive_word.json').read_text(encoding='utf-8'))
    terms=source['terms']
    assert len(terms)==65 and source['source_mask']==819 and source['branch']==2
    assert source['actual_endpoint_factor']=='X-2'
    assert terms[0]['kind']=='endpoint' and terms[0]['exponent']==211
    assert all(t['kind']=='rectangle' and t['n']>1 and gcd(t['n'],30)==1
               and t['q']==3**t['a']*5**t['b'] for t in terms[1:])
    assert sum(t['degree_contribution'] for t in terms)==source['costs']['cofactor_trace_degree']==3390624
    assert source['costs']['original_trace_degree']==3390998 and source['costs']['original_reciprocal_degree']==6781996
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
            records.append(dict(**term,evaluated_factor=value,evaluated_power=powered))
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
    result=dict(scope='ONLY retained mask819 branch2 actual65-term word; all7 ORIGINAL classes modulo8',
        selected_input='inputs/endpoint_full_triple_positive_word.json',terms=terms,costs=source['costs'],
        J_coefficients=divisor,H0_coefficients=h0,T20_base_coefficients=base,
        quotient_degree=144,base_degree=374,full_trace_degree=3390998,full_reciprocal_degree=6781996,
        actual_single_F960=True,canonical_scalar_precisions={'2':16,'3':24,'5':40},
        base_full_canonical_mod8=base_canonical,base_canonical_restricted_J_mod8=base_restricted,
        own_J_canonical_mod8=j_canonical,Q_evaluations_mod8=q_weights,full_H_evaluations_mod8=h_weights,
        all195_term_evaluations_mod8=each_term,original_restrictions_mod8=original,
        diagnostics=diagnostics,global_residual_gates_via_EPX_H_unit_degree=gates,
        initial_F4_X2_prediction_matches=(gates['F_mod4'] and gates['X_plus_mod2'] and gates['X_minus_mod2']),
        no_full_integer_word_expansion=True,no_other_word_or_profile=True,
        author_self_check=True,independent_review=False)
    output.mkdir(parents=True,exist_ok=True)
    temporary=output/'endpoint_word_mod8.json.partial'
    temporary.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    temporary.replace(output/'endpoint_word_mod8.json')
    print(json.dumps(dict(gates=gates,diagnostics=diagnostics)))


if __name__=='__main__':
    main()
