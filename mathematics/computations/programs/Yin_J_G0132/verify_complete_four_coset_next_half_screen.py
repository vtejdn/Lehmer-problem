"""Different AUTHOR verifier for the complete C877 sixteen-by-four screen.

The producer is not imported.  Accepted C875 data are reused at their exact
scope.  GF(2) matrix ranks and coefficient identities check the full tracked
nullspace; actual Theta words use separate coefficient arithmetic.  All448
original arrays use faithful Laurent degree288 arithmetic and true ZZ prime
divisions.  New next-half images are directly evaluated with SymPy GF(2).
"""
from pathlib import Path
from functools import lru_cache
from collections import Counter
from math import gcd
import argparse
import json
import sympy as sp
from verify_complete_local_target_second_half_screen import (
    IndependentArithmetic, binary_poly, from_bits, bits, rref2,
)
from verify_positive_word_residuals import coefficients, binary_diagnostic, x
from verify_full_eighth_kernel_image import CharacterRing, full_trace_factor
from verify_augmented_endpoint_kernel_image import Ring, division


MASKS = [203,235,331,363,715,747,843,875,1171,1203,1299,1331,1683,1715,1811,1843]
INPUTS = ['joint_eighth_second_half_kernel_image.json',
          'joint_eighth_second_half_kernel_image_verification.json',
          'complete_local_target_second_half_screen.json',
          'complete_local_target_second_half_screen_verification.json']
MASK112 = (1<<112)-1


def matrix_rank(columns, height):
    matrix = sp.Matrix(height,len(columns),lambda i,j:(columns[j]>>i)&1)
    return len(rref2(matrix)[1])


def selected_xor(values, coefficients):
    assert type(coefficients) is int and 0<=coefficients<(1<<len(values))
    result = 0
    for i,value in enumerate(values):
        if (coefficients>>i)&1:
            result ^= value
    return result


def projection(vector, columns):
    assert 0<=vector<1<<120
    return (vector&MASK112) | (selected_xor(columns,vector>>112)<<112)


def add_actual_words(*words):
    counts = Counter()
    for word in words:
        for index,exponent in word:
            assert type(index) is int and 0<=index<4193
            assert type(exponent) is int and 0<exponent<960
            counts[index] += exponent
    return [[i,e%960] for i,e in sorted(counts.items()) if e%960]


def cost(word,labels,include_base=False):
    counts = Counter({3:4,5:6,9:8,11:2,15:4,17:2,187:2,960:1}) if include_base else Counter()
    endpoint = 4 if include_base else 0
    degree = 374 if include_base else 0
    terms = []
    for index,exponent in word:
        assert type(index) is int and 0<=index<len(labels)
        assert type(exponent) is int and 0<exponent<960
        label = labels[index]
        if label['kind']=='endpoint':
            assert label['integer_factor']=='X-2' and label['trace_degree']==1
            endpoint += exponent
        else:
            n,q = label['n'],label['q']
            assert n>1 and gcd(n,30)==1 and q==3**label['a']*5**label['b']
            assert label['trace_degree']==q*(n-1)//2
            for divisor in sp.divisors(n):
                if divisor>1:
                    for a in range(label['a']+1):
                        for b in range(label['b']+1):
                            counts[int(divisor)*3**a*5**b] += exponent
        degree += exponent*label['trace_degree']
        terms.append({k:label[k] for k in ('kind','n','q','a','b','trace_degree') if k in label}
                     | dict(index=index,exponent=exponent,degree_contribution=exponent*label['trace_degree']))
    assert degree==endpoint+sum(e*int(sp.totient(n))//2 for n,e in counts.items())
    reciprocal = dict(counts)
    if endpoint:
        reciprocal[1] = 2*endpoint
    assert 2*degree==sum(e*int(sp.totient(n)) for n,e in reciprocal.items())
    return dict(terms=terms,nonzero_terms=len(word),endpoint_exponent=endpoint,
        trace_degree=degree,reciprocal_degree=2*degree,includes_fixed_degree374_base=include_base,
        complete_trace_factors=[dict(order=n,multiplicity=e) for n,e in sorted(counts.items())],
        complete_reciprocal_factors=[dict(order=n,multiplicity=e) for n,e in sorted(reciprocal.items())])


class ThetaWords:
    """Multiply adopted generator data; do not recompute a generator image."""
    def __init__(self,generators):
        self.generators = generators
        self.B = CharacterRing(full_trace_factor(960))
        self.rings = [Ring(bits(sp.Poly(p,x,modulus=2))) for p in
                      ((x**4+x**3+1)**16,(x+1)**28,(x*x+x+1)**14)]
        self.denominators = [bits(sp.Poly((x+1)**24,x,modulus=2)),
                             bits(sp.Poly((x*x+x+1)**12,x,modulus=2))]

    @lru_cache(None)
    def square(self,index,bit):
        if bit==0:
            g = self.generators[index]
            return tuple(g['Xi_plus_components']),self.B.decode(g['old_omega'])
        source,omega = self.square(index,bit-1)
        return tuple(r.multiply(v,v) for r,v in zip(self.rings,source)),self.B.multiply(omega,omega)

    @lru_cache(None)
    def vector(self,word):
        source = (1,1,1)
        omega = self.B.one
        for index,exponent in word:
            assert 0<exponent<960
            for bit in range(exponent.bit_length()):
                if (exponent>>bit)&1:
                    s,o = self.square(index,bit)
                    source = tuple(r.multiply(a,b) for r,a,b in zip(self.rings,source,s))
                    omega = self.B.multiply(omega,o)
        planes = self.B.encode(omega)
        assert source[0]==1 and planes[0]==1
        s,rem = division(source[1]^1,self.denominators[0])
        assert rem==0 and 0<=s<16
        r,rem = division(source[2]^1,self.denominators[1])
        assert rem==0 and 0<=r<16
        return planes[1] | (r<<112) | (s<<116)


def verify_nullspace(rows,columns,cert,labels,theta):
    assert len(rows)==59 and len(columns)==8
    source = [r['vector'] for r in rows]
    images = [projection(v,columns) for v in source]
    assert matrix_rank(source,120)==59 and matrix_rank(images,128)==57
    assert cert['rank']==57 and cert['nullity']==2
    assert len(cert['basis_image_records'])==59 and len(cert['image_basis'])==57
    assert len(cert['null_basis'])==2
    # Coefficient identities and zero pivot coordinates fix each canonical
    # ordered reduction without calling the producer's elimination routine.
    independent_indices = []
    pivots = []
    discovered = []
    for index,record in enumerate(cert['basis_image_records']):
        assert record['index']==index and record['kernel_basis_position']==rows[index]['position']
        assert record['image_bits']==images[index]
        coefficient = record['coefficients_bits']
        assert coefficient>>index==1
        assert all(((coefficient>>j)&1)==0 for j in range(index) if j not in independent_indices)
        remainder = selected_xor(images,coefficient)
        assert remainder==record['remainder_bits']
        assert all(((remainder>>p)&1)==0 for p in pivots)
        if remainder:
            pivot = remainder.bit_length()-1
            assert record['pivot']==pivot and pivot not in pivots
            independent_indices.append(index)
            pivots.append(pivot)
        else:
            assert 'pivot' not in record
            vector = selected_xor(source,coefficient)
            assert vector and projection(vector,columns)==0
            discovered.append(dict(coefficients_bits=coefficient,vector=vector,new_source_index=index))
    assert len(independent_indices)==57 and len(discovered)==2
    assert matrix_rank([r['coefficients_bits'] for r in discovered],59)==2
    assert matrix_rank([r['vector'] for r in discovered],120)==2
    expected_image_basis = []
    for index in independent_indices:
        row = cert['basis_image_records'][index]
        expected_image_basis.append(dict(pivot=row['pivot'],vector=row['remainder_bits'],
                                         coefficients_bits=row['coefficients_bits']))
    assert cert['image_basis']==sorted(expected_image_basis,key=lambda r:r['pivot'],reverse=True)
    null_coefficients = [r['coefficients_bits'] for r in discovered]
    for index,record in enumerate(cert['basis_image_records']):
        coefficient = record['full_basis_reduction_coefficients']
        assert all(((coefficient>>j)&1)==0 for j in range(59) if j not in independent_indices)
        assert selected_xor(images,coefficient)==images[index]
        residue = coefficient^(1<<index)
        assert residue==record['null_residue_coefficients']
        assert selected_xor(images,residue)==0
        matches = [m for m in range(4) if selected_xor(null_coefficients,m)==residue]
        assert matches==[record['null_basis_coordinates']]
    for own,provided in zip(discovered,cert['null_basis']):
        for k,v in own.items():assert provided[k]==v
        selected = [r['word'] for i,r in enumerate(rows) if (own['coefficients_bits']>>i)&1]
        word = add_actual_words(*selected)
        assert provided['word']==word
        assert provided['costs']==cost(word,labels)
        assert theta.vector(tuple(tuple(t) for t in word))==own['vector']
        own.update(word=word,costs=provided['costs'])
    return discovered,images


def next_half(arrays,arithmetic):
    f,f2,f4 = arithmetic.f,arithmetic.f2,arithmetic.f4
    beta = binary_poly(arrays['b']).exquo(f**6)
    gamma = binary_poly(arrays['c']).exquo(f**4)
    delta = arithmetic.delta_binary.rem(f4)
    beta2,gamma3 = (beta**2).rem(f4),(gamma**3).rem(f4)
    halves = {};targets = {}
    for name in ('X_plus','X_minus'):
        assert all(v%2==0 for v in arrays[name])
        halves[name] = [v//2 for v in arrays[name]]
        targets[name] = bits(binary_poly(halves[name]).exquo(f**8).rem(f4))
    assert targets['X_plus']==targets['X_minus']
    p = sp.Poly(x*x+x+1,x,modulus=2)
    lam = sp.Poly(x**3+x,x,modulus=2)
    chi = sp.Poly(x*(x*x+x+1)**2,x,modulus=2)
    uscale = (p**14).rem(f2)
    wscale = (sp.Poly(x+1,x,modulus=2)**28).rem(f4)
    images = []
    for mask in range(256):
        r = from_bits(mask&15).compose(lam).rem(f2)
        s = from_bits(mask>>4).compose(chi).rem(f4)
        u,w = (uscale*r).rem(f2),(wscale*s).rem(f4)
        value = (delta*(beta2*u**2+gamma3*w)).rem(f4)
        images.append(dict(source_mask=mask,r_bits=mask&15,s_bits=mask>>4,
                           u_bits=bits(u),w_bits=bits(w),image_bits=bits(value)))
    columns = [dict(index=i,source=('r' if i<4 else 's'),power=i%4,**images[1<<i]) for i in range(8)]
    column_values = [r['image_bits'] for r in columns]
    rank = matrix_rank(column_values,16)
    assert len({r['image_bits'] for r in images})==1<<rank
    decisions = {}
    for name,target in targets.items():
        matches = [r['source_mask'] for r in images if r['image_bits']==target]
        augmented_rank = matrix_rank(column_values+[target],16)
        assert bool(matches)==(augmented_rank==rank)
        decisions[name] = dict(target_bits=target,member=bool(matches),matching_source_masks=matches,
                               independently_computed_augmented_rank=augmented_rank)
    outcome = 'unresolved_ambient_member' if decisions['X_plus']['member'] else 'entire_Theta_fiber_excluded'
    return dict(genuine_half_arrays_mod4=halves,beta_R30_bits=bits(beta),gamma_R32_bits=bits(gamma),
        coefficient_classes_R4=dict(delta_bits=bits(delta),beta_squared_bits=bits(beta2),gamma_cubed_bits=bits(gamma3)),
        columns=columns,all256_source_images=images,rank=rank,targets=decisions,outcome=outcome)


def check_ambient(own,reported):
    for key in ('genuine_half_arrays_mod4','beta_R30_bits','gamma_R32_bits','coefficient_classes_R4',
                'columns','all256_source_images','rank','outcome'):
        assert own[key]==reported[key],key
    basis = reported['binary_basis']
    assert len(basis)==own['rank']
    pivots = [r['pivot'] for r in basis]
    assert pivots==sorted(set(pivots),reverse=True)
    images = own['all256_source_images']
    for row in basis:
        assert type(row['source_mask']) is int and 0<=row['source_mask']<256
        assert row['image_bits']==images[row['source_mask']]['image_bits']
        assert row['pivot']==row['image_bits'].bit_length()-1
    assert matrix_rank([r['image_bits'] for r in basis],16)==own['rank']
    for name,target in own['targets'].items():
        decision = reported['targets'][name]
        for key in ('target_bits','member','matching_source_masks'):
            assert decision[key]==target[key]
        source = decision['normal_source_mask']
        assert type(source) is int and 0<=source<256
        remainder = target['target_bits']^images[source]['image_bits']
        assert decision['normal_remainder_bits']==remainder
        assert all(((remainder>>p)&1)==0 for p in pivots)
        if target['member']:
            assert remainder==0 and source in target['matching_source_masks']
        else:
            sep = decision['separator_bits']
            assert type(sep) is int and 0<=sep<1<<16
            assert all((sep&r['image_bits']).bit_count()%2==0 for r in images)
            assert (sep&target['target_bits']).bit_count()%2==1


def main():
    here = Path(__file__).resolve().parent
    out = here.parents[1]/'outputs'/here.name
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--result',type=Path,default=out/'complete_four_coset_next_half_screen.json')
    parser.add_argument('--output',type=Path,default=out/'complete_four_coset_next_half_screen_verification.json')
    args = parser.parse_args()
    joint,jv,screen,sv = [json.loads((out/n).read_text(encoding='utf-8')) for n in INPUTS]
    saved = json.loads(args.result.read_text(encoding='utf-8'))
    assert joint['summary']==jv['summary'] and joint['kernel_rank']==jv['kernel_rank']==59
    assert joint['kernel_basis']==jv['kernel_basis']
    assert joint['projected_spaces']==jv['projected_spaces'] and len(joint['projected_spaces'])==1
    assert joint['targets']==jv['targets']
    assert jv['both120_relation_span_inclusions_checked'] and jv['all_projected_span_and_target_certificates_checked']
    assert joint['generators']==jv['verified_generators'] and len(joint['generators'])==4193
    assert screen['summary']==sv['summary'] and screen['base']==sv['base']
    assert sv['all32_branches_independently_derived'] and sv['all7_full_mod8_arrays_and_genuine_half_quarters_checked']
    assert screen['summary']['unresolved_masks']==MASKS
    assert [r['source_mask'] for r in joint['targets']]==MASKS
    labels = [r['actual_label'] for r in joint['generators']]
    assert labels[:4192]==screen['labels']
    assert saved['required_inputs']==INPUTS and saved['masks']==MASKS and saved['labels']==labels
    rows = joint['kernel_basis'];space = joint['projected_spaces'][0]
    assert space['rank']==57 and all(r['projected_space_index']==0 for r in joint['targets'])
    columns = space['columns']
    assert saved['original_projected_columns']==columns
    theta = ThetaWords(joint['generators'])
    nulls,images = verify_nullspace(rows,columns,saved['nullspace_certificate'],labels,theta)
    assert images==[r['vector'] for r in space['all_kernel_basis_images']]
    print('complete59-image/nullspace and both actual null words independently checked',flush=True)
    plans = []
    for target in joint['targets']:
        mask = target['source_mask'];ref = target['reference'];key = target['reference_key']
        assert ref==screen['references'][key]
        assert ref=={k:v for k,v in sv['references'][key].items() if k!='diagnostics'}
        assert target['decision']['member']
        targetbits = target['t_bits'] | (target['g_bits']<<112)
        assert targetbits==target['decision']['target_bits']
        word0 = target['decision']['word'];vector0 = target['decision']['normalization_kernel_vector']
        assert theta.vector(tuple(tuple(t) for t in word0))==vector0
        vectors = []
        for coset in range(4):
            factors = [word0]+[n['word'] for j,n in enumerate(nulls) if (coset>>j)&1]
            word = add_actual_words(*factors)
            vector = vector0^selected_xor([n['vector'] for n in nulls],coset)
            assert theta.vector(tuple(tuple(t) for t in word))==vector
            assert projection(vector,columns)==targetbits
            vectors.append(vector)
            bundles = dict(ref['bundle_words']);assert 'joint_kernel' not in bundles
            bundles['joint_kernel'] = word
            literal = [t for bundle in bundles.values() for t in bundle]
            plans.append(dict(source_mask=mask,coset_bits=coset,reference_key=key,
                original_target_bits=targetbits,kernel_vector=vector,bundle_words=bundles,literal_word=literal,
                kernel_costs=cost(word,labels),costs=cost(literal,labels,True)))
        assert len(set(vectors))==4
    assert len(plans)==len(saved['cases'])==64
    arithmetic = IndependentArithmetic(labels)
    expected_base = dict(P=coefficients(arithmetic.P),V=coefficients(arithmetic.V),J=coefficients(arithmetic.J),
        H0=coefficients(arithmetic.H),T0=coefficients(arithmetic.base),delta=coefficients(arithmetic.delta32),
        base_canonical_mod8=arithmetic.base_full,base_restricted_mod8=arithmetic.base_restricted,
        j_canonical_mod8=arithmetic.j_canonical,
        base_H_evaluations_mod8={str(p):arithmetic.recover(arithmetic.base_weight[p]) for p in (2,3,5)},
        canonical_scalar_precisions={'2':16,'3':24,'5':40})
    assert saved['base']==expected_base
    assert arithmetic.base_full==screen['base']['base_canonical_mod8']
    assert arithmetic.base_restricted==screen['base']['base_restricted_mod8']
    cache = {}
    def weights(word):
        key = tuple(tuple(t) for t in word)
        if key not in cache:
            cache[key] = arithmetic.weights(word)
        return cache[key]
    cases = []
    for plan,reported in zip(plans,saved['cases']):
        for key,value in plan.items():assert reported[key]==value,key
        ref = screen['references'][plan['reference_key']]
        bundles = {name:weights(word) for name,word in plan['bundle_words'].items()}
        total = {};bundle_values = {}
        for p in (2,3,5):
            old = arithmetic.ring.one
            for name in ref['bundle_words']:
                assert bundles[name][p]==arithmetic.image(ref['bundle_weights'][str(p)][name])
                old = arithmetic.ring.multiply(old,bundles[name][p])
            assert old==arithmetic.image(ref['weights'][str(p)])
            total[p] = arithmetic.ring.multiply(old,bundles['joint_kernel'][p])
            bundle_values[str(p)] = {name:arithmetic.recover(value[p]) for name,value in bundles.items()}
        own = arithmetic.reference(total)
        arrays = own['original_restrictions_mod8']
        assert reported['original_restrictions_mod8']==arrays
        assert reported['bundle_weights']==bundle_values and reported['weights']==own['Q_evaluations_mod8']
        assert reported['H_weights']==own['full_H_evaluations_mod8']
        gates = own['global_residual_gates_via_EPX_H_unit_degree']
        assert reported['gates']==gates
        assert gates['F_mod8'] and gates['X_plus_mod2'] and gates['X_minus_mod2'] and gates['G_nonzero_mod2']
        nxt = next_half(arrays,arithmetic)
        check_ambient(nxt,reported['next_half'])
        diagnostics = {n:{k:v for k,v in r.items() if k!='integral_dyadic_quotient_classes'}
                       for n,r in own['diagnostics'].items()}
        for name,half in nxt['genuine_half_arrays_mod4'].items():
            order,unit = binary_diagnostic(half,arithmetic.f)
            diagnostics[name].update(genuine_half_binary_f15_order=order,genuine_half_initial_unit=unit)
        assert diagnostics==reported['diagnostics']
        cases.append(dict(**plan,bundle_weights=bundle_values,weights=own['Q_evaluations_mod8'],
            H_weights=own['full_H_evaluations_mod8'],original_restrictions_mod8=arrays,gates=gates,
            diagnostics=diagnostics,next_half=nxt))
        print(json.dumps(dict(source_mask=plan['source_mask'],coset_bits=plan['coset_bits'],verified_outcome=nxt['outcome'])),flush=True)
    expected_factors = {(p,i) for plan in plans for i,e in plan['literal_word'] for p in (2,3,5)}
    expected_powers = {(p,i,e) for plan in plans for i,e in plan['literal_word'] for p in (2,3,5)}
    values = {(r['p'],r['generator']):r['value'] for r in saved['factor_values']}
    powers = {(r['p'],r['generator'],r['exponent']):r['value'] for r in saved['powered_values']}
    assert len(values)==len(saved['factor_values']) and len(powers)==len(saved['powered_values'])
    assert set(values)==expected_factors==arithmetic.used_values
    assert set(powers)==expected_powers==arithmetic.used_powers
    for key,value in values.items():
        actual = list(arithmetic.factor_value(*key))
        assert actual==arithmetic.image(value) and arithmetic.recover(actual)==value
    for key,value in powers.items():
        actual = list(arithmetic.factor_power(*key))
        assert actual==arithmetic.image(value) and arithmetic.recover(actual)==value
    support = {i for r in rows for i,e in r['word']}
    support.update(i for t in joint['targets'] for i,e in t['decision']['word'])
    support.update(i for t in joint['targets'] for i,e in t['reference']['literal_word'])
    assert len(support)<=129 and len(values)<=387
    assert len(powers)<=3*(64*len(support)+sum(len(t['reference']['literal_word']) for t in joint['targets']))
    fibers = []
    for mask in MASKS:
        selected = [r for r in cases if r['source_mask']==mask]
        assert [r['coset_bits'] for r in selected]==[0,1,2,3]
        survivors = [r['coset_bits'] for r in selected if r['next_half']['outcome']=='unresolved_ambient_member']
        fibers.append(dict(source_mask=mask,ambient_surviving_cosets=survivors,
            all_four_Theta_fibers_excluded=not survivors,old_Xi_fiber_joint_F8_either_X4_excluded=not survivors))
    assert fibers==saved['fibers']
    summary = dict(case_count=64,kernel_nullity=2,projected_rank=57,
        outcome_counts=dict(Counter(r['next_half']['outcome'] for r in cases)),
        excluded_old_masks=[r['source_mask'] for r in fibers if r['all_four_Theta_fibers_excluded']],
        unresolved_old_masks=[r['source_mask'] for r in fibers if not r['all_four_Theta_fibers_excluded']],
        all_remaining_old_fibers_excluded=all(r['all_four_Theta_fibers_excluded'] for r in fibers),
        actual_label_count=len({i for p,i in values}),factor_value_count=len(values),powered_value_count=len(powers),
        literal_factor_occurrences=sum(len(p['literal_word']) for p in plans))
    assert summary==saved['summary']
    for flag in ('all64_own_original_arrays_computed','kernel_words_reduced_mod960_before_original_arithmetic',
                 'original_reference_words_unchanged','actual_q_and_selected_exponents_retained',
                 'ambient_membership_is_unresolved','no_new_group_image','no_higher_modulus_or_profile',
                 'no_word_optimization','no_full_integer_cofactor_expansion','no_F_over8_class_or_mod16'):
        assert saved[flag]
    result = dict(scope='Different AUTHOR exact C877 complete16x4 original-array and next-half screen',
        required_inputs=INPUTS,summary=summary,masks=MASKS,nullspace_certificate=saved['nullspace_certificate'],
        independently_checked_rank=57,independently_checked_nullity=2,base=expected_base,cases=cases,fibers=fibers,
        all59_image_and_coefficient_records_checked=True,two_actual_null_words_and_full_costs_checked=True,
        all64_four_coset_bindings_independently_derived=True,all448_original_mod8_arrays_checked=True,
        all_required_factors_powers_and_bundle_weights_checked=True,
        true_full_Z_base_and_J_prime_divisions_checked=True,exact_single_F960_and_integral_trace_identity_checked=True,
        all64_next_half_targets_and_all256_images_checked=True,all_binary_ranks_and_target_certificates_checked=True,
        quotient_trace_degree=144,Laurent_degree=288,actual_base_degree=374,
        arithmetic='separate GF(2) matrix ranks and coefficient certificates; accepted-Theta word multiplication; faithful Laurent original mod8 arrays; SymPy direct next-source images',
        sympy_version=sp.__version__,author_self_check=True,independent_review=False,
        no_new_group_image=True,no_higher_modulus_or_profile=True,no_word_optimization=True,
        no_full_integer_cofactor_expansion=True,no_F_over8_class_or_mod16=True,ambient_membership_is_unresolved=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    partial = args.output.with_suffix(args.output.suffix+'.partial')
    try:
        partial.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        partial.replace(args.output)
    finally:
        if partial.exists():partial.unlink()
    print(json.dumps(summary))


if __name__=='__main__':
    main()
