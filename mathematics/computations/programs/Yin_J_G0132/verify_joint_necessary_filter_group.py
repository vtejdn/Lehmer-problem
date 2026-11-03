"""Distinct AUTHOR complete256 pair-image certificate verification.

Laurent binary arithmetic reconstructs all evaluated components.
The actual single-F960 integer target is rebuilt, not assumed from a bit string.
No producer arithmetic or discovery algorithm is imported.
"""
from pathlib import Path
from math import gcd
import json
import sympy as sp
from verify_odd_support import C, x, z, trace_factor
from verify_first_gate_character import bits, binary_poly, powmod


def square_root(poly):
    assert all(int(poly.nth(i)) % 2 == 0 for i in range(1, poly.degree()+1, 2))
    result=sp.Poly(sum((int(poly.nth(i)) % 2)*x**(i//2)
                      for i in range(0, poly.degree()+1, 2)), x, modulus=2)
    assert result**2 == poly
    return result


def main():
    here=Path(__file__).resolve().parent
    output=here.parents[3]/'mathematics/computations/outputs'/here.name
    saved=json.loads((output/'joint_necessary_filter_group.json').read_text(encoding='utf-8'))
    f=sp.Poly(x**4+x**3+1,x,modulus=2)
    modulus, m24=f**14,f**24
    one, zero=sp.Poly(1,x,modulus=2),sp.Poly(0,x,modulus=2)
    identity=(one,zero)
    assert saved['f']==bits(f)==25
    assert saved['modulus']==bits(modulus) and saved['additive_modulus']==bits(m24)
    assert saved['unit_bits']==56 and saved['additive_degree']==96
    assert saved['group_exponent']==240
    ns=[481 if r==1 else r for r in range(1,480) if gcd(r,480)==1]
    assert len(ns)==saved['n_class_count']==128
    labels=[(family,n) for n in ns for family in ('B','Gamma')]
    assert len(labels)==saved['generator_count']==256
    assert [(r['family'],r['n']) for r in saved['generators']]==labels
    cyclo=sp.Poly(sp.cyclotomic_poly(15,z),z,modulus=2)
    lm=cyclo**24
    zp=[sp.Poly(1,z,modulus=2)]
    for _ in range(480):
        zp.append((zp[-1]*sp.Poly(z,z,modulus=2)).rem(lm))
    assert zp[480]==zp[0]
    trace=zp[1]+zp[479]
    xp=[sp.Poly(1,z,modulus=2)]
    for _ in range(95):
        xp.append((xp[-1]*trace).rem(lm))
    shifted=[(zp[95]*v).rem(lm) for v in xp]

    def recover(poly):
        work=(zp[95]*poly).rem(lm)
        assert work.is_zero or work.degree()<=190
        value=0
        for j in range(95,-1,-1):
            if int(work.nth(95+j)) % 2:
                value |= 1 << j
                work += shifted[j]
        assert work.is_zero
        return binary_poly(value)

    def kernel(n,q):
        coeff=[0]*480
        for j in range(-(n-1)//2,(n-1)//2+1):
            coeff[(q*j) % 480] ^= 1
        return recover(sp.Poly.from_list(list(reversed(coeff)),z,modulus=2).rem(lm))

    def pmul(a,b):
        return ((a[0]*b[0]).rem(modulus),a[1]+b[1])

    def ppower(a,e):
        return (powmod(a[0],e,modulus),a[1] if e%2 else zero)

    def pinverse(a):
        return (sp.invert(a[0],modulus),a[1])

    def unpack(value):
        return binary_poly(value & ((1<<56)-1)),binary_poly(value>>56)

    def pack(value):
        return bits(value[0]) | (bits(value[1])<<56)

    hs=[]
    source_rows=iter(saved['generators'])
    for n in ns:
        b1,b3,b5,b15=[kernel(n,q) for q in (1,3,5,15)]
        for family,at_x,at_c5,weight in (
                ('B',b1,b5,1),('Gamma',b3,b15,3)):
            row=next(source_rows)
            h=(at_c5.rem(modulus)*powmod(sp.invert(at_x.rem(modulus),modulus),5,modulus)).rem(modulus)
            dlog=(at_c5.diff()*sp.invert(at_c5,m24)).rem(m24)
            pair=(h,dlog)
            assert row['family']==family and row['n']==n
            assert row['at_X']==bits(at_x.rem(modulus))
            assert row['at_C5']==bits(at_c5.rem(modulus))
            assert row['at_C5_R24']==bits(at_c5)
            assert row['L']==bits(h) and row['Dlog_Q5']==bits(dlog)
            assert row['h']==pack(pair)
            assert row['trace_degree']==weight*(n-1)//2
            assert ppower(pair,240)==identity
            hs.append(pair)
    word_length=len(hs)
    assert word_length==256
    # Reconstruct the NEW actual single-F960 reference, including its true integer a.
    while len(C) <= 128:
        C.append(sp.Poly(x, x, domain=sp.ZZ)*C[-1]-C[-2])
    ints = {n: trace_factor(n) for n in (3, 5, 9, 11, 15, 17, 187, 480, 960)}
    ff, v16, v32 = ints[15], ints[480], ints[960]
    assert v32 == v16.compose(C[2]) and v32 != v16**2
    h0 = (sp.Poly((x-2)**2, x)*ints[3]**2*ints[5]**3*ints[9]**4
          *ints[11]*ints[17]*ints[187])
    j2 = ff**4*v32
    assert j2.degree() == 144 and h0.degree() == 115
    actual = {}
    for p in (2, 5):
        numerator = j2.compose(C[p]).rem(j2)
        assert all(int(a) % p == 0 for a in numerator.all_coeffs())
        theta = sp.Poly.from_list([int(a)//p for a in numerator.all_coeffs()], x)
        weight = h0.compose(C[p]).rem(j2)
        actual[p] = (weight**2*theta).rem(j2)
        assert actual[p].rem(ff**4).is_zero
    a2, c2 = actual[2], actual[5]
    alpha2 = sp.Poly(a2, x, modulus=2).exquo(f**8)
    assert alpha2.degree() < 112 and alpha2.gcd(f).degree() == 0
    t2 = square_root(alpha2).rem(modulus)
    gamma2 = sp.Poly(c2, x, modulus=2).exquo(f**4).rem(modulus)
    difference = v32-ff**32
    assert all(int(a) % 2 == 0 for a in difference.all_coeffs())
    delta32 = sp.Poly.from_list([int(a)//2 for a in difference.all_coeffs()], x)
    delta32binary = sp.Poly(delta32, x, modulus=2)
    old_difference = v16-ff**16
    assert all(int(a) % 2 == 0 for a in old_difference.all_coeffs())
    old_delta = sp.Poly.from_list([int(a)//2 for a in old_difference.all_coeffs()], x)
    assert delta32binary == sp.Poly(old_delta, x, modulus=2)**2
    d2 = square_root(delta32binary).rem(modulus)
    target = (d2*powmod(t2, 5, modulus)*sp.invert(gamma2, modulus)).rem(modulus)
    old_target = square_root(target)
    assert bits(old_target) == saved['old_target']
    assert bits(target) == saved['target']
    assert powmod(target, 240, modulus) == one


    target_pair=(target,zero)
    logs_lookup={bits(powmod(sp.Poly(x,x,modulus=2),j,f)):j for j in range(15)}
    assert len(logs_lookup)==15
    logs=[logs_lookup[bits(h[0].rem(f))] for h in hs]
    target_log=logs_lookup[bits(target.rem(f))]
    tau=powmod(sp.Poly(x,x,modulus=2),16,modulus)
    for h,log in zip(hs,logs):
        assert ppower(h,16)==(powmod(tau,log,modulus),zero)
    assert powmod(target,16,modulus)==powmod(tau,target_log,modulus)
    odd=saved['odd_part']
    assert odd['logs']==logs and odd['target_log']==target_log
    divisor=15
    for value in logs:
        divisor=gcd(divisor,value)
    assert odd['gcd_with15']==divisor
    assert len(odd['bezout_coefficients'])==word_length
    assert 15*odd['bezout_multiple15']+sum(a*b for a,b in zip(logs,odd['bezout_coefficients']))==divisor
    assert odd['target_member']==(target_log%divisor==0)
    powers=[]
    for h in hs:
        row=[h]
        for _ in range(7):
            row.append(pmul(row[-1],row[-1]))
        powers.append(row)

    def word_product(word):
        assert len(word)==word_length and all(isinstance(e,int) and 0<=e<240 for e in word)
        result=identity
        for row,exponent in zip(powers,word):
            for bit in range(8):
                if (exponent>>bit)&1:
                    result=pmul(result,row[bit])
        return result

    def leading(pair):
        unit,additive=pair
        if pair==identity:
            return None
        if unit==one:
            return 52+next(i for i in range(96) if int(additive.nth(i))%2)
        work,layer=unit+one,0
        while True:
            quotient,coefficient=work.div(f)
            if not coefficient.is_zero:
                break
            work,layer=quotient,layer+1
        assert 1<=layer<=13
        bit=next(j for j in range(4) if int(coefficient.nth(j))%2)
        return 4*(layer-1)+bit

    basis=saved['principal_basis']
    positions=[r['position'] for r in basis]
    assert positions==sorted(set(positions)) and len(positions)<=100
    pivot={}
    for row in basis:
        value=unpack(row['element'])
        assert value[0].rem(f)==one and leading(value)==row['position']
        assert word_product(row['word'])==value
        pivot[row['position']]=(value,pinverse(value))

    def reduce(pair):
        used=[]
        while pair!=identity:
            position=leading(pair)
            if position not in pivot:
                break
            pair=pmul(pair,pivot[position][1])
            used.append(position)
            assert pair==identity or leading(pair)>position
        return dict(remainder=pack(pair),used_positions=used,first_missing_position=leading(pair))

    assert len(saved['generator_principal_reductions'])==word_length
    for h,expected in zip(hs,saved['generator_principal_reductions']):
        result=reduce(ppower(h,225))
        assert result==expected and result['remainder']==1
    for row in basis:
        value=unpack(row['element'])
        result=reduce(pmul(value,value))
        assert result==row['square_reduction'] and result['remainder']==1
        assert all(p>row['position'] for p in result['used_positions'])
    target_principal=ppower(target_pair,225)
    assert pack(target_principal)==saved['target_principal']
    target_reduction=reduce(target_principal)
    assert target_reduction==saved['target_principal_reduction']
    assert pmul(word_product(saved['target_normalization_word']),unpack(target_reduction['remainder']))==target_principal
    if odd['target_member']:
        assert word_product(odd['target_word'])==ppower(target_pair,16)
    member=odd['target_member'] and target_reduction['remainder']==1
    assert member==saved['target_member']
    assert saved['principal_rank']==len(basis)
    assert saved['odd_subgroup_order']==15//divisor
    assert saved['subgroup_order']==(15//divisor)*(1<<len(basis))
    if member:
        witness = saved['witness']
        assert word_product(witness['exponents']) == target_pair
        expected_terms = []
        counts = {}
        for exponent, row in zip(witness['exponents'], saved['generators']):
            weight = 1 if row['family'] == 'B' else 3
            degree = weight*(row['n']-1)//2
            if exponent:
                expected_terms.append(dict(family=row['family'], n=row['n'], exponent=exponent,
                                           degree_contribution=exponent*degree))
                for r in sp.divisors(row['n'])[1:]:
                    counts[int(r)] = counts.get(int(r), 0)+exponent
                    if row['family'] == 'Gamma':
                        counts[3*int(r)] = counts.get(3*int(r), 0)+exponent
        assert witness['terms'] == expected_terms
        cost = sum(row['degree_contribution'] for row in expected_terms)
        assert cost == sum(e*int(sp.totient(r))//2 for r,e in counts.items())
        assert witness['cofactor_degree'] == cost
        assert witness['cofactor_trace_factor_multiplicities'] == [dict(order=r,multiplicity=e) for r,e in sorted(counts.items())]
        full_counts = {1:8, 3:4, 5:6, 9:8, 15:4, 960:1, 11:2, 17:2, 187:2}
        for r,e in counts.items():
            full_counts[r] = full_counts.get(r, 0)+e
        assert witness['complete_reciprocal_cyclotomic_multiplicities'] == [dict(order=r,multiplicity=e) for r,e in sorted(full_counts.items())]
        assert witness['original_trace_degree'] == 374+cost
        assert witness['original_reciprocal_degree'] == 2*(374+cost)
        assert sum(e*int(sp.totient(r)) for r,e in full_counts.items()) == 2*(374+cost)
        binary_exponents = {}
        for order, multiplicity in full_counts.items():
            if order == 1:
                continue
            dyadic = int(sp.factorint(order).get(2, 0))
            odd_order = order//(2**dyadic)
            assert odd_order > 1
            weight = 1 if dyadic == 0 else 2**(dyadic-1)
            binary_exponents[odd_order] = binary_exponents.get(odd_order, 0)+weight*multiplicity
        assert witness['binary_endpoint_exponent'] == 4
        assert witness['complete_binary_odd_order_exponents'] == [dict(odd_order=r,exponent=e) for r,e in sorted(binary_exponents.items())]
        q_binary = 2**min(int(sp.factorint(e).get(2, 0)) for e in [4]+list(binary_exponents.values()))
        assert witness['maximal_binary_Frobenius_exponent'] == q_binary
        assert witness['full_binary_radical_degree'] == 1+sum(int(sp.totient(r))//2 for r in binary_exponents)
        assert witness['first_gate_and_necessary_square_filter_only'] is True and witness['full_second_gate_not_tested'] is True
    else:
        assert saved['witness'] is None
        if odd['target_member']:
            assert target_reduction['remainder'] != 1
            assert target_reduction['first_missing_position'] not in pivot

    obstruction=None
    if not member and odd['target_member']:
        residual=unpack(target_reduction['remainder'])
        position=leading(residual)
        obstruction=dict(missing_position=position,normalized_remainder=pack(residual),
                         unit_remainder=bits(residual[0]),additive_remainder=bits(residual[1]),
                         first_additive_bit=(position-52 if position>=52 else None))
        if position<52:
            layer=position//4+1
            coefficient=(residual[0]+one).exquo(f**layer).rem(f)
            obstruction.update(unit_layer=layer,unit_coefficient=bits(coefficient))
    result=dict(verified_generators=word_length,verified_R14_evaluated_components=2*word_length,
                verified_R24_logarithmic_derivatives=word_length,
                verified_pivot_words=len(basis),verified_pivot_square_relations=len(basis),
                verified_original_principal_reductions=word_length,
                actual_single_F960_target_checked=True,
                actual_base_target_data=dict(a2_binary=bits(sp.Poly(a2,x,modulus=2)),
                    c2_binary=bits(sp.Poly(c2,x,modulus=2)),delta32_binary=bits(delta32binary),
                    d2=bits(d2),t2=bits(t2),gamma2=bits(gamma2),
                    old_target=bits(old_target),target=bits(target)),
                principal_rank=len(basis),odd_subgroup_order=15//divisor,
                subgroup_order=(15//divisor)*(1<<len(basis)),target_member=member,
                graded_obstruction=obstruction,
                unit_coordinate_pivots=sum(p<52 for p in positions),
                additive_coordinate_pivots=sum(p>=52 for p in positions),
                witness_degrees_and_all_factor_counts_checked=(True if member else None),
                arithmetic='separate Laurent R24 recovery, SymPy pair multiplication, actual single-F960 integer target',
                sympy_version=sp.__version__,author_self_check=True,independent_review=False,
                no_full_second_gate_test=True,no_actual_candidate_enumeration=True)
    temporary=output/'joint_necessary_filter_group_verification.json.partial'
    temporary.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    temporary.replace(output/'joint_necessary_filter_group_verification.json')
    print(json.dumps({k:v for k,v in result.items() if k!='actual_base_target_data'}))


if __name__=='__main__':
    main()
