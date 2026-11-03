"""IMPLEMENTATION ONLY: C882 full60-bit ambient screen of32 actual references.

No execution until the new symbolic theorem is adopted and root authorizes it.
Only the fixed C878 member cases are consumed. Both FULL112-bit targets remain
separate. Ambient membership never asserts an actual cofactor or full X4 word.
"""
from pathlib import Path
from collections import Counter
import json

from main import add, mul, power, compose, chebyshev
from second_half_ambient_response import bits, bmul, bdiv, brem, bpow, compose as bcompose, reduce_vector

INPUTS = ['complete_four_coset_next_half_screen.json',
          'complete_four_coset_next_half_screen_verification.json']
MASKS = [203,235,331,363,715,747,843,875,1171,1203,1299,1331,1683,1715,1811,1843]


def xor_columns(columns, source_mask):
    assert 0 <= source_mask < (1 << 60)
    result = 0
    for row in columns:
        if source_mask >> row['index'] & 1:
            result ^= row['image_bits']
    return result


def source_coordinates(mask):
    assert 0 <= mask < (1 << 60)
    return dict(r_coefficients_bits=mask & ((1 << 28)-1),
                w_epsilon_coefficients_bits=(mask >> 28) & 255,
                s_epsilon_coefficients_bits=mask >> 36)


def input_case_equal(first, second):
    assert {k:v for k,v in first.items() if k != 'next_half'} == {
        k:v for k,v in second.items() if k != 'next_half'}
    for key in ('genuine_half_arrays_mod4','beta_R30_bits','gamma_R32_bits',
                'coefficient_classes_R4','columns','all256_source_images','rank','outcome'):
        assert first['next_half'][key] == second['next_half'][key]
    for name in ('X_plus','X_minus'):
        for key in ('target_bits','member','matching_source_masks'):
            assert first['next_half']['targets'][name][key] == second['next_half']['targets'][name][key]


def recover_data(arrays, f, delta):
    f4, f6, f8, f28 = (bpow(f,n) for n in (4,6,8,28))
    assert set(arrays) == {'a','b','c','F','G','X_plus','X_minus'}
    assert all(type(v) is int and 0 <= v < 8 for a in arrays.values() for v in a)
    assert all(v == 0 for v in arrays['F']) and any(v % 2 for v in arrays['G'])
    halves, full, targets = {}, {}, {}
    for name in ('X_plus','X_minus'):
        assert all(v % 2 == 0 for v in arrays[name])
        halves[name] = [v // 2 for v in arrays[name]]
        full[name] = bits(halves[name])
        target, zero = bdiv(full[name],f8)
        assert zero == 0 and target.bit_length() <= 112
        targets[name] = brem(target,f28)
    beta, zero = bdiv(bits(arrays['b']),f6); assert zero == 0
    gamma, zero = bdiv(bits(arrays['c']),f4); assert zero == 0
    gdiv, zero = bdiv(bits(arrays['G']),f8); assert zero == 0
    gdiv = brem(gdiv,f28)
    difference = targets['X_plus'] ^ targets['X_minus']
    gamma3 = bpow(gamma,3,f28)
    assert difference == gdiv == brem(bmul(f4,gamma3),f28) and difference != 0
    assert full['X_plus'] ^ full['X_minus'] == bits(arrays['G'])
    return dict(genuine_half_arrays_mod4=halves,full_half_bits=full,
                normalized_targets_bits=targets,beta_bits=beta,gamma_bits=gamma,
                beta_squared_R28=bpow(beta,2,f28),gamma_cubed_R28=gamma3,
                delta_R28=brem(bits(delta),f28),target_difference_R28=difference,G_div_f8_R28=gdiv)


def make_columns(data,f):
    f4,f14,f18,f28 = (bpow(f,n) for n in (4,14,18,28))
    p, lam = 7, 10
    chi = bmul(2,bpow(p,2))
    p14 = bpow(p,14)
    scale_w = bpow(3,28,f28)
    columns = []
    for index in range(60):
        U = wc = sc = 0
        if index < 28:
            block, j = 'r', index
            source = 1 << j
            U = brem(bmul(p14,bcompose(source,lam,f14)),f14)
        elif index < 36:
            block, j = 'w', index-28
            source = bpow(3,j)  # fixed epsilon polynomial, not arbitrary quotient lift
            wc = bcompose(source,chi,f28)
        else:
            block, j = 's', index-36
            source = bpow(3,j)
            sc = bcompose(source,chi,f28)
        first = bmul(data['beta_squared_R28'],
                     bmul(data['delta_R28'],bmul(U,U)) ^ bmul(f18,U))
        second = bmul(data['gamma_cubed_R28'],
                      bmul(data['delta_R28'],bmul(scale_w,wc)) ^ bmul(f4,sc))
        image = brem(first ^ second,f28)
        columns.append(dict(index=index,block=block,power=j,source_mask=1 << index,
                            source_polynomial_bits=source,U_bits=U,w_chi_bits=wc,s_chi_bits=sc,image_bits=image))
    assert len(columns) == 60 and columns[36]['image_bits'] == data['target_difference_R28']
    return columns


def full_image_certificate(columns,targets):
    basis = {}
    for row in columns:
        value, source = reduce_vector(row['image_bits'],basis)
        source ^= row['source_mask']
        assert xor_columns(columns,source) == value
        if value:
            basis[value.bit_length()-1] = (value,source)
    reductions = []
    for row in columns:
        value, source = reduce_vector(row['image_bits'],basis)
        assert value == 0 and xor_columns(columns,source) == row['image_bits']
        reductions.append(dict(index=row['index'],remainder_bits=value,source_mask=source))
    decisions = {}
    for name,target in targets.items():
        value, source = reduce_vector(target,basis)
        assert xor_columns(columns,source) == target ^ value
        decision = dict(target_bits=target,member=(value == 0),normal_remainder_bits=value,
                        normal_source_mask=source,normal_source_coordinates=source_coordinates(source))
        if value:
            pivot = value.bit_length()-1
            separator = sum(((reduce_vector(1 << i,basis)[0] >> pivot) & 1) << i for i in range(112))
            assert all((separator & row['image_bits']).bit_count() % 2 == 0 for row in columns)
            assert (separator & target).bit_count() % 2 == 1
            decision['separator_bits'] = separator
        decisions[name] = decision
    assert decisions['X_plus']['member'] == decisions['X_minus']['member']
    assert decisions['X_plus']['normal_remainder_bits'] == decisions['X_minus']['normal_remainder_bits']
    if decisions['X_plus']['member']:
        translated = decisions['X_plus']['normal_source_mask'] ^ (1 << 36)
        assert xor_columns(columns,translated) == decisions['X_minus']['target_bits']
        decisions['X_minus']['translated_plus_ambient_preimage'] = translated
    return dict(rank=len(basis),basis=[dict(pivot=p,image_bits=v,source_mask=s)
                                      for p,(v,s) in sorted(basis.items(),reverse=True)],
                column_reductions=reductions,targets=decisions)


def main():
    here = Path(__file__).resolve().parent
    out = here.parents[1] / 'outputs' / here.name
    source,checked = [json.loads((out/name).read_text(encoding='utf-8')) for name in INPUTS]
    assert source['summary'] == checked['summary'] and source['base'] == checked['base']
    assert source['nullspace_certificate'] == checked['nullspace_certificate']
    assert source['fibers'] == checked['fibers'] and source['masks'] == checked['masks'] == MASKS
    assert checked['all448_original_mod8_arrays_checked'] and checked['all64_four_coset_bindings_independently_derived']
    assert checked['all64_next_half_targets_and_all256_images_checked']
    assert checked['true_full_Z_base_and_J_prime_divisions_checked']
    assert len(source['cases']) == len(checked['cases']) == 64
    assert [(r['source_mask'],r['coset_bits']) for r in source['cases']] == [(m,e) for m in MASKS for e in range(4)]
    chosen = []
    for index,(first,second) in enumerate(zip(source['cases'],checked['cases'])):
        input_case_equal(first,second)
        member = first['next_half']['targets']['X_plus']['member']
        assert member == first['next_half']['targets']['X_minus']['member']
        if member:
            chosen.append((index,first))
    assert len(chosen) == 32 and Counter(r['source_mask'] for _,r in chosen) == {m:2 for m in MASKS}
    P,F30 = [1,4,-4,-1,1],[1,-4,-4,1,1]
    V = compose(F30,chebyshev(32)); J = mul(power(P,4),V)
    delta = add(V,power(P,32),-1)
    assert all(v % 2 == 0 for v in delta)
    delta = [v // 2 for v in delta]
    assert source['base']['P'] == P and source['base']['V'] == V
    assert source['base']['J'] == J and source['base']['delta'] == delta
    assert len(J) == 145 and len(V) == 129
    f = bits(P)
    cases = []
    for index,reference in chosen:
        data = recover_data(reference['original_restrictions_mod8'],f,delta)
        columns = make_columns(data,f)
        certificate = full_image_certificate(columns,data['normalized_targets_bits'])
        member = certificate['targets']['X_plus']['member']
        outcome = 'unresolved_ambient_member' if member else 'entire_Theta_fiber_excluded'
        cases.append(dict(source_mask=reference['source_mask'],coset_bits=reference['coset_bits'],
            source_case_index=index,reference={k:v for k,v in reference.items() if k != 'next_half'},
            data=data,columns=columns,**certificate,
            sign_consistency=dict(source_mask=1 << 36,image_bits=data['target_difference_R28'],membership_equal=True),
            outcome=outcome))
        print(json.dumps(dict(source_mask=reference['source_mask'],coset_bits=reference['coset_bits'],
                              rank=certificate['rank'],outcome=outcome)),flush=True)
    fibers = []
    for mask in MASKS:
        rows = [r for r in cases if r['source_mask'] == mask]
        assert len(rows) == 2
        survivors = [r['coset_bits'] for r in rows if r['outcome'] == 'unresolved_ambient_member']
        fibers.append(dict(source_mask=mask,remaining_Theta_cosets=survivors,
                           whole_old_fiber_excluded=not survivors))
    counts = Counter(r['outcome'] for r in cases)
    all_negative = all(r['outcome'] == 'entire_Theta_fiber_excluded' for r in cases)
    summary = dict(reference_count=32,target_count=64,column_count=1920,
        outcome_counts=dict(counts),negative_target_count=2*counts['entire_Theta_fiber_excluded'],
        ambient_member_target_count=2*counts['unresolved_ambient_member'],
        ranks=dict(Counter(r['rank'] for r in cases)),
        additional_excluded_old_masks=[r['source_mask'] for r in fibers if r['whole_old_fiber_excluded']],
        unresolved_old_masks=[r['source_mask'] for r in fibers if not r['whole_old_fiber_excluded']],
        whole_fixed_family_joint_F8_either_X4_excluded=all_negative)
    payload = dict(scope='C882 complete full60-bit ambient screen; EXACT32 retained C878 cases and BOTH full112 targets',
        required_inputs=INPUTS,base=source['base'],selected_case_ids=[[r['source_mask'],r['coset_bits']] for _,r in chosen],
        source_basis_order=dict(r='Y^j,0<=j<28',w='(Y+1)^j,0<=j<8',s='(Y+1)^j,0<=j<24'),
        source_block_offsets=dict(r=0,w=28,s=36),source_dimension=60,target_dimension=112,
        cases=cases,old_fibers=fibers,summary=summary,
        all32_original_reference_bindings_checked=True,all64_full_targets_checked=True,
        all1920_columns_and_both_span_inclusions_checked=True,
        fixed_canonical_epsilon_lifts=True,genuine_halves_before_binary_division=True,
        both_distinct_targets_and_ambient_sign_translation_checked=True,
        no_2power60_enumeration=True,no_actual_cofactor_attainment_claim=True,
        no_new_group_or_weight_image=True,no_new_original_residual_probe=True,
        no_larger_modulus_or_profile=True,no_F_over8_class_or_mod16=True,
        author_self_check=True,independent_review=False)
    out.mkdir(parents=True,exist_ok=True)
    path = out / 'full_second_half_ambient_screen.json'
    temporary = path.with_suffix('.json.partial')
    temporary.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    temporary.replace(path)
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
