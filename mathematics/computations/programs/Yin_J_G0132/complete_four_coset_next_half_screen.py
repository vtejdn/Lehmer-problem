"""IMPLEMENTATION ONLY: all16 x four actual Theta cosets, next-half ambient screen.

Adopted C875 inputs supply the59/57 image. C877 supplies the next response and
complete four-coset implication, subject to its actual adoption before execution.
No new group image, higher modulus, word optimization or full cofactor expansion.
"""
from pathlib import Path
from functools import lru_cache
from collections import Counter
from math import gcd
import json

from main import add, mul, rem, power, compose, chebyshev
from endpoint_word_mod8 import canonical, ringpower, integer_kernel, kernel, value_through_mod8
from second_half_ambient_response import bits, bmul, bdiv, brem, bpow, compose as bcompose, reduce_vector
from full_eighth_kernel_image import MixedRing, add_word, encode_word
from first_gate_character import multiply as binary_multiply
from endpoint_full_triple_image import totient
from odd_support_probe import binary_order, binary_initial_unit

MASKS = [203,235,331,363,715,747,843,875,1171,1203,1299,1331,1683,1715,1811,1843]
INPUTS = ['joint_eighth_second_half_kernel_image.json',
          'joint_eighth_second_half_kernel_image_verification.json',
          'complete_local_target_second_half_screen.json',
          'complete_local_target_second_half_screen_verification.json']
MASK112 = (1 << 112)-1


def response(value, columns):
    result = 0
    for i, column in enumerate(columns):
        if value >> i & 1:
            result ^= column
    return result


def projected(vector, columns):
    return (vector & MASK112) | (response(vector >> 112, columns) << 112)


def xor_selected(values, coefficients):
    result = 0
    for i, value in enumerate(values):
        if coefficients >> i & 1:
            result ^= value
    return result


def nullspace_certificate(rows, columns):
    """Ordered high-pivot elimination with explicit source coefficient tracking."""
    pivots, records, nulls = {}, [], []
    source = [r['vector'] for r in rows]
    images = [projected(v, columns) for v in source]
    for index, image in enumerate(images):
        value, used = reduce_vector(image, pivots)
        coeff = used ^ (1 << index)
        assert coeff >> index == 1 and xor_selected(images, coeff) == value
        record = dict(index=index, kernel_basis_position=rows[index]['position'],
                      image_bits=image, remainder_bits=value, coefficients_bits=coeff)
        if value:
            pivot = value.bit_length()-1
            pivots[pivot] = (value, coeff)
            record['pivot'] = pivot
        else:
            vector = xor_selected(source, coeff)
            assert vector and projected(vector, columns) == 0
            nulls.append(dict(coefficients_bits=coeff, vector=vector, new_source_index=index))
        records.append(record)
    assert len(pivots) == 57 and len(nulls) == 2
    assert nulls[0]['vector'] != nulls[1]['vector']
    for record in records:
        value, used = reduce_vector(record['image_bits'], pivots)
        assert value == 0
        record['full_basis_reduction_coefficients'] = used
        record['null_residue_coefficients'] = used ^ (1 << record['index'])
        assert xor_selected(images, record['null_residue_coefficients']) == 0
        coefficients = record['null_residue_coefficients']
        matches = [m for m in range(4) if xor_selected(
            [r['coefficients_bits'] for r in nulls], m) == coefficients]
        assert len(matches) == 1
        record['null_basis_coordinates'] = matches[0]
    return dict(basis_image_records=records, rank=len(pivots), nullity=len(nulls),
                image_basis=[dict(pivot=p, vector=v, coefficients_bits=c)
                             for p,(v,c) in sorted(pivots.items(), reverse=True)],
                null_basis=nulls)


def word_costs(word, labels, include_base=False):
    counts = Counter({3:4,5:6,9:8,11:2,15:4,17:2,187:2,960:1}) if include_base else Counter()
    endpoint, degree, terms = 4 if include_base else 0, 374 if include_base else 0, []
    for index, exponent in word:
        assert type(index) is int and 0 <= index < len(labels)
        assert type(exponent) is int and 0 < exponent < 960
        label = labels[index]
        if label['kind'] == 'endpoint':
            assert label['integer_factor'] == 'X-2' and label['trace_degree'] == 1
            endpoint += exponent
        else:
            assert label['kind'] == 'rectangle' and label['n'] > 1 and gcd(label['n'],30) == 1
            assert label['q'] == 3**label['a']*5**label['b']
            assert label['trace_degree'] == label['q']*((label['n']-1)//2)
            for r in range(2,label['n']+1):
                if label['n'] % r == 0:
                    for a in range(label['a']+1):
                        for b in range(label['b']+1):
                            counts[r*3**a*5**b] += exponent
        degree += exponent*label['trace_degree']
        terms.append({k:label[k] for k in ('kind','n','q','a','b','trace_degree') if k in label}
                     | dict(index=index, exponent=exponent, degree_contribution=exponent*label['trace_degree']))
    assert degree == endpoint+sum(e*totient(n)//2 for n,e in counts.items())
    reciprocal = dict(counts)
    if endpoint:
        reciprocal[1] = 2*endpoint
    assert 2*degree == sum(e*totient(n) for n,e in reciprocal.items())
    return dict(terms=terms, nonzero_terms=len(word), endpoint_exponent=endpoint,
                trace_degree=degree, reciprocal_degree=2*degree,
                includes_fixed_degree374_base=include_base,
                complete_trace_factors=[dict(order=n,multiplicity=e) for n,e in sorted(counts.items())],
                complete_reciprocal_factors=[dict(order=n,multiplicity=e) for n,e in sorted(reciprocal.items())])


def next_half(arrays, f, delta):
    f2, f4, f8 = bpow(f,2), bpow(f,4), bpow(f,8)
    halves, targets = {}, {}
    for name in ('X_plus','X_minus'):
        assert all(v % 2 == 0 for v in arrays[name])
        halves[name] = [v//2 for v in arrays[name]]
        quotient, zero = bdiv(bits(halves[name]), f8)
        assert zero == 0
        targets[name] = brem(quotient, f4)
    assert targets['X_plus'] == targets['X_minus']
    beta, zero = bdiv(bits(arrays['b']), bpow(f,6)); assert zero == 0
    gamma, zero = bdiv(bits(arrays['c']), f4); assert zero == 0
    coefficients = dict(delta_bits=brem(bits(delta),f4), beta_squared_bits=bpow(beta,2,f4),
                        gamma_cubed_bits=bpow(gamma,3,f4))
    p, lam = 7, 10
    chi = bmul(2,bpow(p,2))
    def source_image(mask):
        r,s = mask & 15, mask >> 4
        u = brem(bmul(bpow(p,14),bcompose(r,lam,f2)),f2)
        w = brem(bmul(bpow(3,28),bcompose(s,chi,f4)),f4)
        image = brem(bmul(coefficients['delta_bits'],
            bmul(coefficients['beta_squared_bits'],bmul(u,u)) ^
            bmul(coefficients['gamma_cubed_bits'],w)),f4)
        return dict(source_mask=mask,r_bits=r,s_bits=s,u_bits=u,w_bits=w,image_bits=image)
    images = [source_image(mask) for mask in range(256)]
    columns = [dict(index=i,source=('r' if i<4 else 's'),power=i%4,**images[1<<i]) for i in range(8)]
    basis = {}
    for i,column in enumerate(columns):
        value, used = reduce_vector(column['image_bits'],basis)
        if value:
            basis[value.bit_length()-1] = (value, used ^ (1<<i))
    for row in images:
        assert response(row['source_mask'],[c['image_bits'] for c in columns]) == row['image_bits']
    assert len({r['image_bits'] for r in images}) == 1 << len(basis)
    decisions = {}
    for name,target in targets.items():
        remainder, used = reduce_vector(target,basis)
        matches = [r['source_mask'] for r in images if r['image_bits'] == target]
        assert bool(matches) == (remainder == 0)
        row = dict(target_bits=target,member=(remainder==0),normal_remainder_bits=remainder,
                   normal_source_mask=used,matching_source_masks=matches)
        if remainder:
            pivot = remainder.bit_length()-1
            separator = sum(((reduce_vector(1<<i,basis)[0]>>pivot)&1)<<i for i in range(16))
            assert all((separator & c['image_bits']).bit_count()%2 == 0 for c in columns)
            assert (separator & target).bit_count()%2 == 1
            row['separator_bits'] = separator
        decisions[name] = row
    assert decisions['X_plus']['member'] == decisions['X_minus']['member']
    return dict(genuine_half_arrays_mod4=halves,beta_R30_bits=beta,gamma_R32_bits=gamma,
                coefficient_classes_R4=coefficients,columns=columns,all256_source_images=images,
                rank=len(basis),binary_basis=[dict(pivot=p,image_bits=v,source_mask=w)
                    for p,(v,w) in sorted(basis.items(),reverse=True)],targets=decisions,
                outcome=('unresolved_ambient_member' if decisions['X_plus']['member']
                         else 'entire_Theta_fiber_excluded'))


def main():
    here = Path(__file__).resolve().parent
    out = here.parents[3]/'mathematics/computations/outputs'/here.name
    joint,jv,screen,sv = [json.loads((out/n).read_text(encoding='utf-8')) for n in INPUTS]
    assert joint['summary'] == jv['summary']
    assert joint['kernel_rank'] == jv['kernel_rank'] == 59
    assert joint['kernel_basis'] == jv['kernel_basis']
    assert joint['projected_spaces'] == jv['projected_spaces'] and len(joint['projected_spaces']) == 1
    assert joint['targets'] == jv['targets']
    assert jv['both120_relation_span_inclusions_checked'] and jv['all_projected_span_and_target_certificates_checked']
    assert len(joint['generators']) == len(jv['verified_generators']) == 4193
    assert joint['generators'] == jv['verified_generators']
    assert screen['summary'] == sv['summary'] and screen['base'] == sv['base']
    assert sv['all32_branches_independently_derived'] and sv['all7_full_mod8_arrays_and_genuine_half_quarters_checked']
    assert screen['summary']['unresolved_masks'] == MASKS
    assert [r['source_mask'] for r in joint['targets']] == MASKS
    labels = [r['actual_label'] for r in joint['generators']]
    assert labels[:4192] == screen['labels']
    rows = joint['kernel_basis']; space = joint['projected_spaces'][0]
    assert space['rank'] == 57 and all(r['projected_space_index']==0 for r in joint['targets'])
    columns = space['columns']
    cert = nullspace_certificate(rows,columns)
    source_vectors = [r['vector'] for r in rows]
    assert [projected(v,columns) for v in source_vectors] == [r['vector'] for r in space['all_kernel_basis_images']]

    mixed = MixedRing()
    moduli = [bpow(25,16),bpow(3,28),bpow(7,14)]
    @lru_cache(None)
    def generator_square(index,bit):
        if bit == 0:
            row = joint['generators'][index]
            return tuple(row['Xi_plus_components']),tuple(row['old_omega'])
        src,omega = generator_square(index,bit-1)
        return tuple(binary_multiply(v,v,m) for v,m in zip(src,moduli)),mixed.multiply(omega,omega)
    @lru_cache(None)
    def kernel_word_vector(encoded):
        src,omega = (1,1,1),mixed.one
        for index,exponent in encoded:
            for bit in range(exponent.bit_length()):
                if exponent>>bit & 1:
                    s,o = generator_square(index,bit)
                    src = tuple(binary_multiply(a,b,m) for a,b,m in zip(src,s,moduli))
                    omega = mixed.multiply(omega,o)
        assert src[0] == 1 and omega[0] == 1
        s,zero = bdiv(src[1]^1,bpow(3,24)); assert zero == 0 and s.bit_length() <= 4
        r,zero = bdiv(src[2]^1,bpow(7,12)); assert zero == 0 and r.bit_length() <= 4
        return omega[1] | (r<<112) | (s<<116)
    for null in cert['null_basis']:
        word = {}
        for i,row in enumerate(rows):
            if null['coefficients_bits']>>i & 1:
                word = add_word(word,dict(row['word']))
        null['word'] = encode_word(word)
        null['costs'] = word_costs(null['word'],labels)
        assert kernel_word_vector(tuple(tuple(t) for t in null['word'])) == null['vector']

    plans = []
    for target in joint['targets']:
        mask = target['source_mask']; ref = target['reference']; key = target['reference_key']
        assert ref == screen['references'][key]
        assert ref == {k:v for k,v in sv['references'][key].items() if k!='diagnostics'}
        assert target['decision']['member'] and target['decision']['target_bits'] == target['t_bits'] | (target['g_bits']<<112)
        K0 = target['decision']['word']; vector0 = target['decision']['normalization_kernel_vector']
        assert kernel_word_vector(tuple(tuple(t) for t in K0)) == vector0
        vectors = set()
        for coset in range(4):
            word = dict(K0); vector = vector0
            for j,null in enumerate(cert['null_basis']):
                if coset>>j & 1:
                    word = add_word(word,dict(null['word'])); vector ^= null['vector']
            encoded = encode_word(word)
            assert kernel_word_vector(tuple(tuple(t) for t in encoded)) == vector
            assert projected(vector,columns) == target['decision']['target_bits']
            vectors.add(vector)
            bundles = dict(ref['bundle_words']); assert 'joint_kernel' not in bundles
            bundles['joint_kernel'] = encoded
            literal = [t for w in bundles.values() for t in w]
            plans.append(dict(source_mask=mask,coset_bits=coset,reference_key=key,
                original_target_bits=target['decision']['target_bits'],kernel_vector=vector,
                bundle_words=bundles,literal_word=literal,
                kernel_costs=word_costs(encoded,labels),costs=word_costs(literal,labels,True)))
        assert len(vectors)==4
    assert len(plans)==64
    # The choices above are now fixed; arithmetic below does not search other words.
    print('complete59-image nullspace and all64 literal representative bindings prepared',flush=True)
    P,F30 = [1,4,-4,-1,1],[1,-4,-4,1,1]
    V = compose(F30,chebyshev(32)); J = mul(power(P,4),V)
    H0 = power([-2,1],2)
    for factor,e in (([1,1],2),([-1,1,1],3),([1,-3,0,1],4),(integer_kernel(187),1)):
        H0 = mul(H0,power(factor,e))
    T0 = mul(J,power(H0,2)); assert len(J)==145 and len(T0)==375
    delta = add(V,power(P,32),-1); assert all(v%2==0 for v in delta)
    delta = [v//2 for v in delta]
    base_full,base_j,j_can,base_H = {},{},{},{}
    for p in (2,3,5):
        base_full[str(p)] = canonical(T0,p)
        base_j[str(p)] = rem(base_full[str(p)],J,8)
        j_can[str(p)] = canonical(J,p)
        base_H[str(p)] = ringpower(compose(H0,chebyshev(p),J,8),2,J)
        assert base_j[str(p)] == rem(mul(base_H[str(p)],j_can[str(p)],8),J,8)
    assert base_full == screen['base']['base_canonical_mod8'] and base_j == screen['base']['base_restricted_mod8']
    @lru_cache(None)
    def cheb_pair(n):
        if n==0:
            return (2,),(0,1)
        a,b = cheb_pair(n//2)
        even = rem(add(mul(list(a),list(a),8),[-2],modulus=8),J,8)
        odd = rem(add(mul(list(a),list(b),8),[0,1],-1,8),J,8)
        return (tuple(even),tuple(odd)) if n%2==0 else (tuple(odd),tuple(rem(add(mul(list(b),list(b),8),[-2],modulus=8),J,8)))
    factors,powers,squares = {},{},{}
    def factor_value(p,index):
        key=(p,index)
        if key not in factors:
            label=labels[index]
            factors[key] = add(chebyshev(p),[-2],modulus=8) if label['kind']=='endpoint' else kernel(label['n'],list(cheb_pair(p*label['q'])[0]),J)
        return factors[key]
    def powered(p,index,exponent):
        key=(p,index,exponent)
        if key not in powers:
            sq=squares.setdefault((p,index),[factor_value(p,index)])
            while len(sq)<exponent.bit_length():
                sq.append(rem(mul(sq[-1],sq[-1],8),J,8))
            value=[1]
            for bit in range(exponent.bit_length()):
                if exponent>>bit & 1:
                    value=rem(mul(value,sq[bit],8),J,8)
            powers[key]=value
        return powers[key]
    @lru_cache(None)
    def word_weight(p,encoded):
        value=[1]
        for index,e in encoded:
            value=rem(mul(value,powered(p,index,e),8),J,8)
        return tuple(value)
    cases=[]
    for plan in plans:
        arrays,weights,bundle_weights,H_weights={},{},{},{}
        ref=screen['references'][plan['reference_key']]
        for p,name in ((2,'a'),(3,'b'),(5,'c')):
            bundle={n:list(word_weight(p,tuple(tuple(t) for t in w))) for n,w in plan['bundle_words'].items()}
            old=[1]
            for n in ref['bundle_words']:
                assert bundle[n]==ref['bundle_weights'][str(p)][n]
                old=rem(mul(old,bundle[n],8),J,8)
            assert old==ref['weights'][str(p)]
            total=rem(mul(old,bundle['joint_kernel'],8),J,8)
            bundle_weights[str(p)],weights[str(p)]=bundle,total
            H_weights[str(p)]=rem(mul(base_H[str(p)],total,8),J,8)
            arrays[name]=rem(mul(base_j[str(p)],total,8),J,8)
            assert arrays[name]==rem(mul(j_can[str(p)],H_weights[str(p)],8),J,8)
        a,b,c=[arrays[n] for n in ('a','b','c')]
        arrays['F']=rem(add([2*v for v in ringpower(c,2,J)],ringpower(a,5,J),-3),J,8)
        arrays['G']=rem(add(ringpower(c,3,J),ringpower(b,5,J),-2),J,8)
        second=add(ringpower(b,2,J),ringpower(a,3,J),-1)
        arrays['X_plus']=rem(add(second,arrays['G']),J,8)
        arrays['X_minus']=rem(add(second,arrays['G'],-1),J,8)
        assert rem(add(arrays['X_plus'],arrays['X_minus'],-1),J,8)==rem([2*v for v in arrays['G']],J,8)
        gates={f'{n}_mod{m}':all(v%m==0 for v in arrays[n]) for n in ('F','X_plus','X_minus') for m in (2,4,8)}
        gates['G_nonzero_mod2']=any(v%2 for v in arrays['G'])
        assert gates['F_mod8'] and gates['X_plus_mod2'] and gates['X_minus_mod2'] and gates['G_nonzero_mod2']
        nxt=next_half(arrays,bits(P),delta)
        assert nxt['coefficient_classes_R4']==dict(delta_bits=257,beta_squared_bits=1088,gamma_cubed_bits=1088)
        diagnostics={n:dict(coefficient_valuation_through_mod8=value_through_mod8(poly),
            binary_f15_order=binary_order(poly,P),binary_initial_unit=binary_initial_unit(poly,P)) for n,poly in arrays.items()}
        for n,half in nxt['genuine_half_arrays_mod4'].items():
            diagnostics[n]['genuine_half_binary_f15_order']=binary_order(half,P)
            diagnostics[n]['genuine_half_initial_unit']=binary_initial_unit(half,P)
        cases.append(dict(**plan,bundle_weights=bundle_weights,weights=weights,H_weights=H_weights,
            original_restrictions_mod8=arrays,gates=gates,diagnostics=diagnostics,next_half=nxt))
        print(json.dumps(dict(source_mask=plan['source_mask'],coset_bits=plan['coset_bits'],outcome=nxt['outcome'])),flush=True)
    expected_factors={(p,i) for plan in plans for i,e in plan['literal_word'] for p in (2,3,5)}
    expected_powers={(p,i,e) for plan in plans for i,e in plan['literal_word'] for p in (2,3,5)}
    assert set(factors)==expected_factors and set(powers)==expected_powers
    support={i for row in rows for i,e in row['word']}
    support.update(i for t in joint['targets'] for i,e in t['decision']['word'])
    support.update(i for t in joint['targets'] for i,e in t['reference']['literal_word'])
    assert len(support)<=129 and len(factors)<=387
    assert len(powers)<=3*(64*len(support)+sum(len(t['reference']['literal_word']) for t in joint['targets']))
    fibers=[]
    for mask in MASKS:
        selected=[r for r in cases if r['source_mask']==mask]
        survivors=[r['coset_bits'] for r in selected if r['next_half']['outcome']=='unresolved_ambient_member']
        fibers.append(dict(source_mask=mask,ambient_surviving_cosets=survivors,
            all_four_Theta_fibers_excluded=not survivors,
            old_Xi_fiber_joint_F8_either_X4_excluded=not survivors))
    summary=dict(case_count=64,kernel_nullity=2,projected_rank=57,
        outcome_counts=dict(Counter(r['next_half']['outcome'] for r in cases)),
        excluded_old_masks=[r['source_mask'] for r in fibers if r['all_four_Theta_fibers_excluded']],
        unresolved_old_masks=[r['source_mask'] for r in fibers if not r['all_four_Theta_fibers_excluded']],
        all_remaining_old_fibers_excluded=all(r['all_four_Theta_fibers_excluded'] for r in fibers),
        actual_label_count=len({i for p,i in factors}),factor_value_count=len(factors),powered_value_count=len(powers),
        literal_factor_occurrences=sum(len(p['literal_word']) for p in plans))
    result=dict(scope='C877 complete16x4 actual Theta-coset ORIGINAL mod8 and next-half ambient screen',
        required_inputs=INPUTS,masks=MASKS,labels=labels,nullspace_certificate=cert,
        original_projected_columns=columns,base=dict(P=P,V=V,J=J,H0=H0,T0=T0,delta=delta,
            base_canonical_mod8=base_full,base_restricted_mod8=base_j,j_canonical_mod8=j_can,
            base_H_evaluations_mod8=base_H,canonical_scalar_precisions={'2':16,'3':24,'5':40}),
        factor_values=[dict(p=p,generator=i,value=v) for (p,i),v in sorted(factors.items())],
        powered_values=[dict(p=p,generator=i,exponent=e,value=v) for (p,i,e),v in sorted(powers.items())],
        cases=cases,fibers=fibers,summary=summary,all64_own_original_arrays_computed=True,
        kernel_words_reduced_mod960_before_original_arithmetic=True,original_reference_words_unchanged=True,
        actual_q_and_selected_exponents_retained=True,ambient_membership_is_unresolved=True,
        no_new_group_image=True,no_higher_modulus_or_profile=True,no_word_optimization=True,
        no_full_integer_cofactor_expansion=True,no_F_over8_class_or_mod16=True,
        author_self_check=True,independent_review=False)
    out.mkdir(parents=True,exist_ok=True)
    path=out/'complete_four_coset_next_half_screen.json';temporary=path.with_suffix('.json.partial')
    temporary.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');temporary.replace(path)
    print(json.dumps(summary))


if __name__=='__main__':
    main()
