"""Bounded ALL32 retained old-Xi fibers; original mod8 and necessary half screen.

Implementation prepared before execution authorization.  The only actual words
are the32 retained C864 words and at most32 retained C867 K_h words.  No group
image, word optimization, higher modulus or large polynomial expansion occurs.
"""
from pathlib import Path
from functools import lru_cache
from collections import Counter
from math import gcd
import json

from main import add, mul, rem, power, compose, chebyshev
from endpoint_word_mod8 import canonical, ringpower, integer_kernel, kernel, value_through_mod8
from second_half_ambient_response import bits, bmul, bdiv, brem, bpow, compose as bcompose, reduce_vector

MASKS = [147,179,203,235,275,307,331,363,659,691,715,747,787,819,843,875,
         1171,1203,1227,1259,1299,1331,1355,1387,1683,1715,1739,1771,1811,1843,1867,1899]
INPUTS = ['endpoint_full_triple_image.json', 'endpoint_full_triple_image_verification.json',
          'augmented_endpoint_kernel_image.json', 'augmented_endpoint_kernel_image_verification.json']


def binverse(a, modulus):
    r0, r1, s0, s1 = modulus, brem(a, modulus), 0, 1
    while r1:
        q, r = bdiv(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, s0 ^ bmul(q, s1)
    assert r0 == 1
    inverse = brem(s0, modulus)
    assert brem(bmul(a, inverse), modulus) == 1
    return inverse


def derivative(a):
    return sum(((a >> i) & 1) << (i-1) for i in range(1, a.bit_length(), 2))


def first_quarter(arrays, f, delta16):
    assert all(v % 4 == 0 for v in arrays['F'])
    f2, f4 = bpow(f, 2), bpow(f, 4)
    quarter = [v//4 for v in arrays['F']]
    q = bits(quarter)
    result = dict(genuine_quarter_mod2=quarter, quarter_bits=q, ell_bits=brem(q, f4))
    if result['ell_bits']:
        result['stage'] = 'first_quarter_low_nonzero'
        return result
    quotient, remainder = bdiv(q, f4)
    assert remainder == 0
    g = brem(quotient, f4)
    deriv = derivative(g)
    result.update(g_bits=g, ordinary_derivative_bits=deriv)
    if deriv:
        result['stage'] = 'first_quarter_derivative_nonzero'
        return result
    rho = sum(((g >> (2*i)) & 1) << i for i in range(8))
    assert bpow(rho, 2, f4) == g
    gamma, remainder = bdiv(bits(arrays['c']), f4)
    assert remainder == 0
    gamma2, delta2 = brem(gamma, f2), brem(bits(delta16), f2)
    denominator = brem(bmul(gamma2, delta2), f2)
    h = brem(bmul(rho, binverse(denominator, f2)), f2)
    assert 0 <= h < 256
    result.update(stage='unique_kernel_jet', rho_bits=rho, gamma_R2_bits=gamma2,
                  delta16_R2_bits=delta2, denominator_R2_bits=denominator, required_h=h)
    return result


def second_half(arrays, f, delta):
    f2, f4 = bpow(f, 2), bpow(f, 4)
    halves, low, targets = {}, {}, {}
    for name in ('X_plus', 'X_minus'):
        assert all(v % 2 == 0 for v in arrays[name])
        halves[name] = [v//2 for v in arrays[name]]
        low[name] = brem(bits(halves[name]), f4)
    assert low['X_plus'] == low['X_minus']
    result = dict(genuine_half_arrays_mod4=halves, lowest_half_classes_R4=low)
    if low['X_plus']:
        result['stage'] = 'second_half_low_nonzero'
        return result
    for name in halves:
        quotient, remainder = bdiv(bits(halves[name]), f4)
        assert remainder == 0
        targets[name] = brem(quotient, f4)
    assert targets['X_plus'] == targets['X_minus']
    beta, remainder = bdiv(bits(arrays['b']), bpow(f, 6)); assert remainder == 0
    gamma, remainder = bdiv(bits(arrays['c']), f4); assert remainder == 0
    coeff = dict(delta_bits=brem(bits(delta), f4), beta_squared_bits=bpow(beta, 2, f4),
                 gamma_cubed_bits=bpow(gamma, 3, f4))
    p, lam = 7, 10
    chi = bmul(2, bpow(p, 2))

    def response(mask):
        r, s = mask & 15, mask >> 4
        u = brem(bmul(bpow(p, 12), bcompose(r, lam, f2)), f2)
        w = brem(bmul(bpow(3, 24), bcompose(s, chi, f4)), f4)
        image = brem(bmul(coeff['delta_bits'],
                    bmul(coeff['beta_squared_bits'], bmul(u, u)) ^ bmul(coeff['gamma_cubed_bits'], w)), f4)
        return dict(source_mask=mask, r_bits=r, s_bits=s, u_bits=u, w_bits=w, image_bits=image)

    images = [response(mask) for mask in range(256)]
    columns = [dict(index=i, source=('r' if i < 4 else 's'), power=i % 4, **images[1 << i]) for i in range(8)]
    basis = {}
    for i, col in enumerate(columns):
        value, mask = reduce_vector(col['image_bits'], basis)
        mask ^= 1 << i
        if value:
            basis[value.bit_length()-1] = (value, mask)
    for mask, row in enumerate(images):
        image = 0
        for i, col in enumerate(columns):
            if mask >> i & 1:
                image ^= col['image_bits']
        assert image == row['image_bits']
    decisions = {}
    for name, target in targets.items():
        remainder, mask = reduce_vector(target, basis)
        matches = [row['source_mask'] for row in images if row['image_bits'] == target]
        assert bool(matches) == (remainder == 0)
        row = dict(target_bits=target, member=(remainder == 0), normal_remainder_bits=remainder,
                   normal_source_mask=mask, matching_source_masks=matches)
        if remainder:
            pos = remainder.bit_length()-1
            separator = sum(((reduce_vector(1 << i, basis)[0] >> pos) & 1) << i for i in range(16))
            assert all((separator & col['image_bits']).bit_count() % 2 == 0 for col in columns)
            assert (separator & target).bit_count() % 2 == 1
            row['separator_bits'] = separator
        decisions[name] = row
    assert len({row['image_bits'] for row in images}) == 1 << len(basis)
    assert decisions['X_plus']['member'] == decisions['X_minus']['member']
    result.update(stage=('unresolved_ambient_member' if decisions['X_plus']['member'] else 'second_half_ambient_nonmember'),
                  beta_R30_bits=beta, gamma_R32_bits=gamma, coefficient_classes_R4=coeff,
                  columns=columns, all256_source_images=images, rank=len(basis), distinct_image_count=1 << len(basis),
                  binary_basis=[dict(pivot=i, image_bits=v, source_mask=w) for i, (v, w) in sorted(basis.items(), reverse=True)],
                  targets=decisions)
    return result


def main():
    here = Path(__file__).resolve().parent
    out = here.parents[3]/'mathematics/computations/outputs'/here.name
    qdata, qcheck, kdata, kcheck = [json.loads((out/name).read_text(encoding='utf-8')) for name in INPUTS]
    assert qdata['all64_targets_tested'] and qcheck['all64_target_normalforms_and_positive_words_checked']
    assert kdata['all256_targets_tested'] and kcheck['all256_target_normalforms_and_positive_words_checked']
    labels = [{k: v for k, v in row.items() if k not in ('components', 'image')} for row in qdata['generators']]
    assert labels == [{k: v for k, v in row.items() if k not in ('components', 'image')} for row in kdata['generators']]
    assert len(labels) == 4192
    qs = sorted((r for r in qdata['target_decisions'] if r['target_member']), key=lambda r: r['source_mask'])
    assert [r['source_mask'] for r in qs] == MASKS and all(r['branch'] == 2 for r in qs)
    qverified = {(r['source_mask'], r['branch']): r for r in qcheck['target_decisions']}
    ks = {r['h']: r for r in kdata['target_decisions']}
    kv = {r['h']: r for r in kcheck['target_decisions']}
    assert set(ks) == set(kv) == set(range(256))
    for h, row in ks.items():
        assert row['target_member'] == kv[h]['target_member'] == ((h & 81).bit_count() % 2 == 0)
        if row['target_member']:
            assert kv[h]['positive_word_checked'] and row['word_costs'] == kv[h]['word_costs']
    for row in qs:
        check = qverified[(row['source_mask'], row['branch'])]
        assert check['target_member'] and check['positive_word_checked'] and check['word_costs'] == row['word_costs']

    def costs(word):
        endpoint, degree = 0, 0
        for index, exponent in word:
            assert type(index) is int and type(exponent) is int and 0 <= index < len(labels) and 0 < exponent < 480
            label = labels[index]
            if label['kind'] == 'endpoint':
                assert label['integer_factor'] == 'X-2' and label['trace_degree'] == 1
                endpoint += exponent
            else:
                assert label['kind'] == 'rectangle' and label['n'] > 1 and gcd(label['n'], 30) == 1
                assert label['q'] == 3**label['a']*5**label['b']
                assert label['trace_degree'] == label['q']*((label['n']-1)//2)
            degree += exponent*label['trace_degree']
        return dict(endpoint_exponent=endpoint, nonzero_terms=len(word), cofactor_trace_degree=degree,
                    original_trace_degree=374+degree, original_reciprocal_degree=2*(374+degree))

    P, F30 = [1,4,-4,-1,1], [1,-4,-4,1,1]
    V = compose(F30, chebyshev(32))
    J = mul(power(P, 4), V)
    H0 = power([-2,1], 2)
    for factor, exponent in (([1,1],2), ([-1,1,1],3), ([1,-3,0,1],4), (integer_kernel(187),1)):
        H0 = mul(H0, power(factor, exponent))
    T0 = mul(J, power(H0, 2))
    assert len(J)-1 == 144 and len(T0)-1 == 374
    delta = add(V, power(P, 32), -1)
    delta16 = add(compose(F30, chebyshev(16)), power(P, 16), -1)
    assert all(v % 2 == 0 for v in delta+delta16)
    delta, delta16 = [v//2 for v in delta], [v//2 for v in delta16]
    f = bits(P)
    assert bits(delta) == bpow(bits(delta16), 2)
    base_canonical, base_j, j_canonical, base_H = {}, {}, {}, {}
    for p in (2,3,5):
        base_canonical[str(p)] = canonical(T0, p)
        base_j[str(p)] = rem(base_canonical[str(p)], J, 8)
        j_canonical[str(p)] = canonical(J, p)
        base_H[str(p)] = ringpower(compose(H0, chebyshev(p), J, 8), 2, J)
        assert base_j[str(p)] == rem(mul(base_H[str(p)], j_canonical[str(p)], 8), J, 8)

    @lru_cache(None)
    def cheb_pair(n):
        if n == 0:
            return (2,), (0,1)
        a, b = cheb_pair(n//2)
        even = rem(add(mul(list(a), list(a), 8), [-2], modulus=8), J, 8)
        odd = rem(add(mul(list(a), list(b), 8), [0,1], -1, 8), J, 8)
        if n % 2 == 0:
            return tuple(even), tuple(odd)
        return tuple(odd), tuple(rem(add(mul(list(b), list(b), 8), [-2], modulus=8), J, 8))

    factors, powers, binary_powers = {}, {}, {}

    def factor_value(p, index):
        key = (p, index)
        if key not in factors:
            label = labels[index]
            if label['kind'] == 'endpoint':
                value = add(chebyshev(p), [-2], modulus=8)
            else:
                value = kernel(label['n'], list(cheb_pair(p*label['q'])[0]), J)
            factors[key] = value
        return factors[key]

    def powered(p, index, exponent):
        key = (p, index, exponent)
        if key not in powers:
            # Cache literal powers of two of the same ACTUAL factor; this is
            # ordinary exponentiation, not reduction of a word exponent.
            squares = binary_powers.setdefault((p,index), [factor_value(p,index)])
            while len(squares) < exponent.bit_length():
                squares.append(rem(mul(squares[-1],squares[-1],8),J,8))
            value = [1]
            for bit in range(exponent.bit_length()):
                if exponent >> bit & 1:
                    value = rem(mul(value,squares[bit],8),J,8)
            powers[key] = value
        return powers[key]

    references = {}

    @lru_cache(None)
    def word_weight(p, word):
        value = [1]
        for index, exponent in word:
            value = rem(mul(value, powered(p,index,exponent), 8), J, 8)
        return tuple(value)

    def reference(name, bundles):
        word = [term for bundle in bundles.values() for term in bundle]
        refcost = costs(word)
        bundle_weights, weights, H_weights, arrays = {}, {}, {}, {}
        for p, variable in ((2,'a'), (3,'b'), (5,'c')):
            each = {}
            for label, bundle in bundles.items():
                each[label] = list(word_weight(p,tuple(tuple(term) for term in bundle)))
            total = [1]
            for value in each.values():
                total = rem(mul(total, value, 8), J, 8)
            bundle_weights[str(p)], weights[str(p)] = each, total
            H_weights[str(p)] = rem(mul(base_H[str(p)], total, 8), J, 8)
            arrays[variable] = rem(mul(total, base_j[str(p)], 8), J, 8)
            assert arrays[variable] == rem(mul(H_weights[str(p)], j_canonical[str(p)], 8), J, 8)
        a, b, c = [arrays[x] for x in ('a','b','c')]
        ap = {e: ringpower(a,e,J) for e in (3,5)}
        bp = {e: ringpower(b,e,J) for e in (2,5)}
        cp = {e: ringpower(c,e,J) for e in (2,3)}
        arrays['F'] = rem(add([2*v for v in cp[2]], ap[5], -3), J, 8)
        arrays['G'] = rem(add(cp[3], bp[5], -2), J, 8)
        second = add(bp[2], ap[3], -1)
        arrays['X_plus'], arrays['X_minus'] = rem(add(second, arrays['G']), J, 8), rem(add(second, arrays['G'], -1), J, 8)
        assert rem(add(arrays['X_plus'], arrays['X_minus'], -1), J, 8) == rem([2*v for v in arrays['G']], J, 8)
        gates = {f'{n}_mod{m}': all(v % m == 0 for v in arrays[n]) for n in ('F','X_plus','X_minus') for m in (2,4,8)}
        gates['G_nonzero_mod2'] = any(v % 2 for v in arrays['G'])
        assert gates['F_mod4'] and gates['X_plus_mod2'] and gates['X_minus_mod2'] and gates['G_nonzero_mod2']
        references[name] = dict(bundle_words=bundles, literal_word=word, costs=refcost,
                                bundle_weights=bundle_weights, weights=weights, H_weights=H_weights,
                                original_restrictions_mod8=arrays, gates=gates,
                                coefficient_valuations={n:value_through_mod8(a) for n,a in arrays.items()})
        return references[name]

    records = []
    for source in qs:
        mask = source['source_mask']
        qname = f'Q:{mask}'
        qref = reference(qname, {'Q': source['word']})
        assert qref['costs'] == source['word_costs']
        first = first_quarter(qref['original_restrictions_mod8'], f, delta16)
        record = dict(source_mask=mask, branch=2, Xi_components=source['components'], Q_reference=qname, first_quarter=first)
        if first['stage'] != 'unique_kernel_jet':
            record['outcome'] = first['stage']
        else:
            h = first['required_h']; selected = ks[h]
            record['selected_kernel'] = dict(h=h, target_member=selected['target_member'], components=selected['components'],
                                             certificate_input=INPUTS[2])
            if not selected['target_member']:
                record['outcome'] = 'kernel_jet_not_attained'
                record['selected_kernel']['principal_reduction'] = selected['principal_reduction']
            else:
                word = selected['word']; kc = costs(word)
                assert kc['cofactor_trace_degree'] == selected['word_costs']['kernel_trace_degree']
                assert kc['endpoint_exponent'] == selected['word_costs']['endpoint_exponent']
                record['selected_kernel'].update(word=word, kernel_trace_degree=kc['cofactor_trace_degree'])
                rname = f'QK:{mask}'
                rref = reference(rname, {'Q': source['word'], 'K': word})
                assert rref['costs']['cofactor_trace_degree'] == qref['costs']['cofactor_trace_degree']+kc['cofactor_trace_degree']
                qbits = bits([v//4 for v in rref['original_restrictions_mod8']['F']])
                assert brem(qbits, bpow(f,8)) == 0
                record['product_reference'] = rname
                record['lowest_quarter_mod_f8_cancelled'] = True
                record['second_half'] = second_half(rref['original_restrictions_mod8'], f, delta)
                record['outcome'] = record['second_half']['stage']
        record['joint_F8_either_X4_excluded_in_old_fiber'] = record['outcome'] != 'unresolved_ambient_member'
        records.append(record)
        print(json.dumps(dict(source_mask=mask, outcome=record['outcome'])), flush=True)

    used_labels = {index for _,index in factors}
    assert len(used_labels) <= 84 and len(factors) <= 252 and len(powers) <= 4269 and len(references) <= 64
    expected_factors = {(p,index) for ref in references.values() for index,e in ref['literal_word'] for p in (2,3,5)}
    expected_powers = {(p,index,e) for ref in references.values() for index,e in ref['literal_word'] for p in (2,3,5)}
    assert set(factors) == expected_factors and set(powers) == expected_powers
    summary = dict(outcome_counts=dict(sorted(Counter(r['outcome'] for r in records).items())),
                   all32_closed=all(r['joint_F8_either_X4_excluded_in_old_fiber'] for r in records),
                   unresolved_masks=[r['source_mask'] for r in records if not r['joint_F8_either_X4_excluded_in_old_fiber']],
                   reference_count=len(references), actual_label_count=len(used_labels),
                   factor_value_count=len(factors), powered_value_count=len(powers))
    result = dict(scope='ALL32 adopted old-Xi targets; C865 first-quarter and C870 ambient second-half necessary screen only',
                  required_inputs=INPUTS, masks=MASKS, labels=labels,
                  base=dict(P=P,V=V,J=J,H0=H0,T0=T0,delta=delta,delta16=delta16,
                            base_canonical_mod8=base_canonical, base_restricted_mod8=base_j,
                            j_canonical_mod8=j_canonical, base_H_evaluations_mod8=base_H,
                            canonical_scalar_precisions={'2':16,'3':24,'5':40}),
                  factor_values=[dict(p=p,generator=i,value=v) for (p,i),v in sorted(factors.items())],
                  powered_values=[dict(p=p,generator=i,exponent=e,value=v) for (p,i,e),v in sorted(powers.items())],
                  references=references, records=records, summary=summary,
                  all32_records_complete=True, actual_exponents_and_q_retained=True,
                  no_new_group_image=True, no_120bit_image=True, no_other_word_or_profile=True,
                  no_full_integer_cofactor_expansion=True, no_F_over8_class_or_mod16=True,
                  author_self_check=True, independent_review=False)
    out.mkdir(parents=True, exist_ok=True)
    path=out/'complete_local_target_second_half_screen.json'
    temporary=path.with_suffix('.json.partial')
    temporary.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    temporary.replace(path)
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
