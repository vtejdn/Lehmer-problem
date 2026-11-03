"""Different AUTHOR degree288 Laurent check of the ONE65-term word modulo8.

Actual integer T20 base canonical divisions are done over Z before reduction.
All195 term values/powers use direct Laurent kernels with ACTUAL p*q indices.
No producer arithmetic, full large cofactor or additional word is used.
"""
from pathlib import Path
from functools import lru_cache
import json
import sympy as sp
from verify_positive_word_residuals import LaurentRing,trace_factor,coefficients,binary_diagnostic,x,z,C


def poly(values):
    return sp.Poly.from_list(list(reversed(values)),x,domain=sp.ZZ)


def reduced_coefficients(polynomial,modulus):
    values=[v%modulus for v in coefficients(polynomial)]
    while len(values)>1 and values[-1]==0:
        values.pop()
    return values


def main():
    here=Path(__file__).resolve().parent
    output=here.parents[3]/'mathematics/computations/outputs'/here.name
    word=json.loads((here/'inputs/endpoint_full_triple_positive_word.json').read_text(encoding='utf-8'))
    saved=json.loads((output/'endpoint_word_mod8.json').read_text(encoding='utf-8'))
    assert saved['terms']==word['terms'] and len(word['terms'])==65
    assert saved['costs']==word['costs'] and word['costs']['endpoint_exponent']==211
    assert word['actual_endpoint_factor']=='X-2'
    assert sum(t['degree_contribution'] for t in word['terms'])==3390624
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
    def image(values,modulus=8):
        rr=rings[modulus]
        return rr.evaluate(poly(values),rr.argument(1))

    # A full triangular recovery, valid over Z/8 as well as over fields.
    trace_powers=[ring.one]
    for _ in range(143):
        trace_powers.append(ring.multiply(trace_powers[-1],trace))
    shift=ring.power(ring.z,143)
    shifted=[ring.multiply(shift,p) for p in trace_powers]
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
        total=ring.one
        for _ in range(n-1):
            total=ring.multiply(total,unit)
            total[0]=(total[0]+1)%8
        centered=ring.multiply(ring.power(ring.zi,index*((n-1)//2)),total)
        return tuple(centered)

    actual,base_int_restricted,q_saved,h_saved={},{},{},{}
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
        records=saved['all195_term_evaluations_mod8'][str(p)]
        assert len(records)==65
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
        h_weight=ring.multiply(base_weight,q_weight)
        assert q_weight==image(saved['Q_evaluations_mod8'][str(p)])
        assert h_weight==image(saved['full_H_evaluations_mod8'][str(p)])
        actual[name]=ring.multiply(q_weight,image(reduced_coefficients(base_j,8)))
        assert actual[name]==ring.multiply(h_weight,image(reduced_coefficients(j_canonical,8)))
        base_int_restricted[p]=coefficients(base_j)
        q_saved[p],h_saved[p]=recover(q_weight),recover(h_weight)
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
    gates={f'{name}_mod{m}':all(v%m==0 for v in recovered[name])
           for name in ('F','X_plus','X_minus') for m in (2,4,8)}
    gates['G_nonzero_mod2']=any(v%2 for v in recovered['G'])
    assert gates==saved['global_residual_gates_via_EPX_H_unit_degree']
    result=dict(scope='same ONE retained65-term word, all7 ORIGINAL residue arrays modulo8',
        quotient_trace_degree=144,Laurent_degree=288,actual_base_degree=374,
        costs=word['costs'],true_full_Z_base_and_J_prime_divisions_checked=True,
        exact_single_F960_and_integral_trace_identity_checked=True,
        all195_term_values_and_powers_checked=True,all_three_Q_and_H_weights_checked=True,
        all7_full_mod8_trace_arrays_recovered_and_matched=True,
        original_restrictions_mod8=recovered,original_Laurent_restrictions_mod8=actual,
        Q_evaluations_mod8=q_saved,full_H_evaluations_mod8=h_saved,
        true_integer_base_canonical_J_restrictions=base_int_restricted,
        diagnostics=diagnostics,global_residual_gates_via_EPX_H_unit_degree=gates,
        arithmetic='full-Z SymPy base canonical divisions, direct Laurent kernels, exact integer convolution and triangular trace recovery',
        sympy_version=sp.__version__,author_self_check=True,independent_review=False,
        no_full_integer_word_expansion=True,no_other_word_or_profile=True)
    temporary=output/'endpoint_word_mod8_verification.json.partial'
    temporary.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    temporary.replace(output/'endpoint_word_mod8_verification.json')
    summary={key:result[key] for key in ('all195_term_values_and_powers_checked','all_three_Q_and_H_weights_checked',
             'all7_full_mod8_trace_arrays_recovered_and_matched','global_residual_gates_via_EPX_H_unit_degree')}
    summary['valuations']={name:row['coefficient_valuation_through_mod8'] for name,row in diagnostics.items()}
    summary['nonzero_divided_orders']={name:[(q['division_power'],q['binary_f15_order'],q['binary_initial_unit'])
        for q in row['integral_dyadic_quotient_classes'] if q['binary_f15_order']!='infinity'] for name,row in diagnostics.items()}
    print(json.dumps(summary))


if __name__=='__main__':
    main()
