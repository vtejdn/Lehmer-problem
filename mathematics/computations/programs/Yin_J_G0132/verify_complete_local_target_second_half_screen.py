"""Different AUTHOR check of the complete32-target bounded second-half screen.

IMPLEMENTATION ONLY until separately authorized to run.  No producer arithmetic
is imported.  The original classes use the faithful degree288 Laurent quotient;
branch derivatives, roots and ambient images use SymPy GF(2) polynomials.
All actual n/q/exponents are retained.  No F/8 class or mod16 is formed.
"""
from pathlib import Path
from functools import lru_cache
from collections import Counter
from math import gcd
import argparse
import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from verify_positive_word_residuals import (
    LaurentRing, trace_factor, coefficients, binary_diagnostic, x, z, C,
)
from verify_endpoint_word_mod8 import poly, reduced_coefficients


MASKS = [147,179,203,235,275,307,331,363,659,691,715,747,787,819,843,875,
         1171,1203,1227,1259,1299,1331,1355,1387,1683,1715,1739,1771,
         1811,1843,1867,1899]
NAMES = ('a','b','c','F','G','X_plus','X_minus')


def binary_poly(values):
    return sp.Poly.from_list(list(reversed(values)), x, modulus=2)


def from_bits(value):
    return sp.Poly.from_dict({(i,):1 for i in range(value.bit_length())
                             if (value >> i) & 1}, x, modulus=2)


def bits(polynomial):
    if polynomial.is_zero:
        return 0
    return sum((int(polynomial.nth(i)) & 1) << i
               for i in range(int(polynomial.degree())+1))


def rref2(matrix):
    rr, pivots = DomainMatrix.from_Matrix(matrix).convert_to(sp.GF(2)).rref()
    return rr.to_Matrix(), tuple(int(i) for i in pivots)


def integer_half(polynomial):
    assert all(int(c) % 2 == 0 for c in polynomial.all_coeffs())
    return sp.Poly.from_dict({m:int(c)//2 for m,c in polynomial.terms()}, x,
                            domain=sp.ZZ)


def actual_label(row):
    return {k:v for k,v in row.items() if k not in ('components','image')}


def source_inputs(out):
    q = json.loads((out/'endpoint_full_triple_image.json').read_text(encoding='utf-8'))
    qv = json.loads((out/'endpoint_full_triple_image_verification.json').read_text(encoding='utf-8'))
    k = json.loads((out/'augmented_endpoint_kernel_image.json').read_text(encoding='utf-8'))
    kv = json.loads((out/'augmented_endpoint_kernel_image_verification.json').read_text(encoding='utf-8'))
    assert q['all64_targets_tested'] and qv['all64_target_normalforms_and_positive_words_checked']
    assert k['all256_targets_tested'] and kv['all256_target_normalforms_and_positive_words_checked']
    labels = [actual_label(g) for g in q['generators']]
    assert labels == [actual_label(g) for g in k['generators']]
    assert len(labels) == 4192
    qchecks = {(r['source_mask'],r['branch']):r for r in qv['target_decisions']}
    kchecks = {r['h']:r for r in kv['target_decisions']}
    qrows = [r for r in q['target_decisions'] if r['target_member']]
    assert [r['source_mask'] for r in qrows] == MASKS
    assert all(r['branch'] == 2 for r in qrows)
    for r in q['target_decisions']:
        checked = qchecks[r['source_mask'],r['branch']]
        assert r['target_member'] == checked['target_member']
        if r['target_member']:
            assert checked['positive_word_checked']
            assert r['word_costs'] == checked['word_costs']
    assert len(k['target_decisions']) == 256
    krows = {r['h']:r for r in k['target_decisions']}
    assert set(krows) == set(range(256))
    for h,r in krows.items():
        assert r['target_member'] == kchecks[h]['target_member']
        if r['target_member']:
            assert kchecks[h]['positive_word_checked']
            assert r['word_costs'] == kchecks[h]['word_costs']
    assert len([r for r in krows.values() if r['target_member']]) == 128
    return labels, qrows, krows


def word_costs(word, labels):
    endpoint = degree = 0
    for index, exponent in word:
        assert type(index) is int and 0 <= index < len(labels)
        assert type(exponent) is int and 0 < exponent < 480
        label = labels[index]
        if label['kind'] == 'endpoint':
            assert label['integer_factor'] == 'X-2' and label['trace_degree'] == 1
            endpoint += exponent
            d = 1
        else:
            assert label['kind'] == 'rectangle' and gcd(label['n'],30) == 1
            assert label['n'] > 1 and label['q'] == 3**label['a']*5**label['b']
            d = label['q']*((label['n']-1)//2)
            assert d == label['trace_degree']
        degree += exponent*d
    return dict(endpoint_exponent=endpoint, nonzero_terms=len(word),
                cofactor_trace_degree=degree, original_trace_degree=374+degree,
                original_reciprocal_degree=2*(374+degree))


class IndependentArithmetic:
    def __init__(self, labels):
        self.labels = labels
        factors = {n:trace_factor(n) for n in (3,5,9,11,15,17,187,480,960)}
        self.P, self.V = factors[15], factors[960]
        self.J = self.P**4*self.V
        self.H = (sp.Poly((x-2)**2,x)*factors[3]**2*factors[5]**3*factors[9]**4
                  *factors[11]*factors[17]*factors[187])
        self.base = self.J*self.H**2
        assert self.J.degree() == 144 and self.base.degree() == 374
        assert self.V == factors[480].compose(C[2]) and self.V != factors[480]**2
        self.delta32 = integer_half(self.V-self.P**32)
        self.delta16 = integer_half(factors[480]-self.P**16)
        self.f = binary_poly(coefficients(self.P))
        self.f2, self.f4 = self.f**2, self.f**4
        self.delta_binary = binary_poly(coefficients(self.delta32))
        self.delta16_binary = binary_poly(coefficients(self.delta16))
        reciprocal = sp.Poly(sp.cyclotomic_poly(15,z)**4*sp.cyclotomic_poly(960,z),z,domain=sp.ZZ)
        expansion = sp.Poly(0,z,domain=sp.ZZ)
        for i in range(145):
            for j in range(i+1):
                expansion += sp.Poly(int(self.J.nth(i))*int(sp.binomial(i,j))*z**(144+i-2*j),z)
        assert reciprocal == expansion and reciprocal.degree() == 288
        self.ring = LaurentRing(reciprocal,8)
        rr = self.ring
        self.trace_powers = [rr.one]
        for _ in range(143):
            self.trace_powers.append(rr.multiply(self.trace_powers[-1],rr.argument(1)))
        self.sparse = [[(i,c) for i,c in enumerate(row) if c] for row in self.trace_powers]
        self.shift = rr.power(rr.z,143)
        self.shifted = [rr.multiply(self.shift,row) for row in self.trace_powers]
        self.base_full, self.base_restricted, self.j_canonical = {},{},{}
        self.base_weight = {}
        for p in (2,3,5):
            numerator = self.base.compose(C[p]).rem(self.base)
            assert all(int(v)%p == 0 for v in numerator.all_coeffs())
            canonical = sp.Poly.from_list([int(v)//p for v in numerator.all_coeffs()],x,domain=sp.ZZ)
            self.base_full[str(p)] = reduced_coefficients(canonical,8)
            self.base_restricted[str(p)] = reduced_coefficients(canonical.rem(self.J),8)
            jnum = self.J.compose(C[p]).rem(self.J)
            assert all(int(v)%p == 0 for v in jnum.all_coeffs())
            jcan = sp.Poly.from_list([int(v)//p for v in jnum.all_coeffs()],x,domain=sp.ZZ)
            self.j_canonical[str(p)] = reduced_coefficients(jcan,8)
            hp2 = rr.power(rr.evaluate(self.H,rr.argument(p)),2)
            self.base_weight[p] = hp2
            assert rr.multiply(hp2,self.image(self.j_canonical[str(p)])) == self.image(self.base_restricted[str(p)])
        self.used_values = set()
        self.used_powers = set()

    def image(self, values, modulus=8):
        result = [0]*288
        assert len(values) <= 144
        for i,c in enumerate(values):
            c %= modulus
            if c:
                for j,v in self.sparse[i]:
                    result[j] += c*v
        return [v%modulus for v in result]

    def recover(self, value):
        work = self.ring.multiply(self.shift,value)
        assert work[287] == 0
        result = [0]*144
        for j in range(143,-1,-1):
            c = work[143+j]
            result[j] = c
            if c:
                work = self.ring.add(work,self.shifted[j],-c)
        assert not any(work)
        while len(result)>1 and result[-1] == 0:
            result.pop()
        return result

    @lru_cache(None)
    def factor_value(self, p, index):
        rr, label = self.ring, self.labels[index]
        if label['kind'] == 'endpoint':
            value = rr.argument(p)
            value[0] = (value[0]-2)%8
            return tuple(value)
        n, actual_index = label['n'],p*label['q']
        unit = rr.power(rr.z,actual_index)
        def power_sum(length):
            if length == 0:
                return rr.one,[0]*288
            hp,hs = power_sum(length//2)
            ep = rr.multiply(hp,hp)
            es = rr.add(hs,rr.multiply(hp,hs))
            if length%2:
                return rr.multiply(ep,unit),rr.add(es,ep)
            return ep,es
        # Actual n and p*q are retained; this exact identity uses no image period.
        _,total = power_sum(n)
        return tuple(rr.multiply(rr.power(rr.zi,actual_index*((n-1)//2)),total))

    @lru_cache(None)
    def factor_square(self, p, index, bit):
        if bit == 0:
            return self.factor_value(p,index)
        previous = list(self.factor_square(p,index,bit-1))
        return tuple(self.ring.multiply(previous,previous))

    @lru_cache(None)
    def factor_power(self, p, index, exponent):
        # Share exact powers of two; the literal exponent is never reduced.
        assert type(exponent) is int and exponent > 0
        value = self.ring.one
        for bit in range(exponent.bit_length()):
            if (exponent >> bit)&1:
                value = self.ring.multiply(value,list(self.factor_square(p,index,bit)))
        return tuple(value)

    def weights(self, word):
        result = {}
        for p in (2,3,5):
            weight = self.ring.one
            for index,exponent in word:
                self.used_values.add((p,index))
                self.used_powers.add((p,index,exponent))
                weight = self.ring.multiply(weight,list(self.factor_power(p,index,exponent)))
            result[p] = weight
        return result

    def reference(self, weights):
        rr = self.ring
        values = {name:rr.multiply(weights[p],self.image(self.base_restricted[str(p)]))
                  for p,name in ((2,'a'),(3,'b'),(5,'c'))}
        a,b,c = [values[n] for n in ('a','b','c')]
        values['F'] = rr.add([2*v%8 for v in rr.power(c,2)],rr.power(a,5),-3)
        values['G'] = rr.add(rr.power(c,3),[2*v%8 for v in rr.power(b,5)],-1)
        second = rr.add(rr.power(b,2),rr.power(a,3),-1)
        values['X_plus'] = rr.add(second,values['G'])
        values['X_minus'] = rr.add(second,values['G'],-1)
        assert rr.add(values['X_plus'],values['X_minus'],-1) == [2*v%8 for v in values['G']]
        arrays = {n:self.recover(v) for n,v in values.items()}
        diagnostics = {}
        for n,arr in arrays.items():
            valuation = min((v&-v).bit_length()-1 for v in arr if v) if any(arr) else 'at_least_3'
            order,unit = binary_diagnostic(arr,self.f)
            quotients = []
            for shift in (1,2):
                scale = 1<<shift
                if all(v%scale == 0 for v in arr):
                    divided = [v//scale for v in arr]
                    qorder,qunit = binary_diagnostic(divided,self.f)
                    assert all(v%scale == 0 for v in values[n])
                    assert self.image(divided,8//scale) == [v//scale for v in values[n]]
                    quotients.append(dict(division_power=shift,coefficient_modulus=8//scale,
                        coefficients=divided,binary_f15_order=qorder,binary_initial_unit=qunit))
            diagnostics[n] = dict(coefficient_valuation_through_mod8=valuation,
                binary_f15_order=order,binary_initial_unit=unit,integral_dyadic_quotient_classes=quotients)
        gates = {f'{n}_mod{m}':all(v%m == 0 for v in arrays[n])
                 for n in ('F','X_plus','X_minus') for m in (2,4,8)}
        gates['G_nonzero_mod2'] = any(v%2 for v in arrays['G'])
        return dict(original_restrictions_mod8=arrays,diagnostics=diagnostics,
                    Q_evaluations_mod8={str(p):self.recover(weights[p]) for p in (2,3,5)},
                    full_H_evaluations_mod8={str(p):self.recover(rr.multiply(self.base_weight[p],weights[p])) for p in (2,3,5)},
                    global_residual_gates_via_EPX_H_unit_degree=gates)

    def first_quarter(self, arrays):
        assert all(v%4 == 0 for v in arrays['F'])
        quarter = [v//4 for v in arrays['F']]
        q = binary_poly(quarter)
        ell = q.rem(self.f4)
        result = dict(genuine_quarter_array_mod2=quarter,quarter_binary=bits(q),ell=bits(ell))
        if not ell.is_zero:
            result['stage'] = 'nonzero_first_quarter_ell'
            return result
        g = q.exquo(self.f4).rem(self.f4)
        derivative = g.diff().rem(self.f4)
        result.update(g=bits(g),I=bits(derivative))
        if not derivative.is_zero:
            result['stage'] = 'nonzero_first_quarter_derivative'
            return result
        # The canonical degree<16 polynomial has only even powers; its genuine
        # characteristic-two polynomial square root has degree<8 and is unique.
        rho = sp.Poly.from_dict({(i,):int(g.nth(2*i))%2 for i in range(8)},x,modulus=2)
        assert rho**2 == g
        gamma = binary_poly(arrays['c']).exquo(self.f**4)
        denominator = (self.delta16_binary*gamma).rem(self.f2)
        inverse = sp.invert(denominator,self.f2)
        assert (denominator*inverse).rem(self.f2) == sp.Poly(1,x,modulus=2)
        h = (rho*inverse).rem(self.f2)
        result.update(stage='kernel_membership_required',rho=bits(rho),
                      gamma_mod_f2=bits(gamma.rem(self.f2)),
                      delta16_mod_f2=bits(self.delta16_binary.rem(self.f2)),
                      denominator_mod_f2=bits(denominator),h=bits(h))
        return result

    def second_half(self, arrays):
        beta = binary_poly(arrays['b']).exquo(self.f**6)
        gamma = binary_poly(arrays['c']).exquo(self.f**4)
        assert not beta.rem(self.f).is_zero and not gamma.rem(self.f).is_zero
        beta2,gamma3 = (beta**2).rem(self.f4),(gamma**3).rem(self.f4)
        delta4 = self.delta_binary.rem(self.f4)
        targets = {}
        for name in ('X_plus','X_minus'):
            assert all(v%2 == 0 for v in arrays[name])
            half = [v//2 for v in arrays[name]]
            hp = binary_poly(half)
            ell = hp.rem(self.f4)
            targets[name] = dict(genuine_half_array_mod4=half,ell=bits(ell))
            if ell.is_zero:
                targets[name]['target_bits'] = bits(hp.exquo(self.f4).rem(self.f4))
        result = dict(beta_R30_bits=bits(beta),gamma_R32_bits=bits(gamma),
                      coefficient_classes_R4=dict(delta_bits=bits(delta4),
                          beta_squared_bits=bits(beta2),gamma_cubed_bits=bits(gamma3)),targets=targets)
        if all(r['ell'] for r in targets.values()):
            return result
        p = sp.Poly(x*x+x+1,x,modulus=2)
        lam = sp.Poly(x**3+x,x,modulus=2)
        chi = sp.Poly(x*(x*x+x+1)**2,x,modulus=2)
        uscale = (p**12).rem(self.f2)
        wscale = (sp.Poly(x+1,x,modulus=2)**24).rem(self.f4)
        zero = sp.Poly(0,x,modulus=2)
        images = []
        polys = []
        for source in range(256):
            r = from_bits(source&15).compose(lam).rem(self.f2)
            s = from_bits(source>>4).compose(chi).rem(self.f4)
            u,w = (uscale*r).rem(self.f2),(wscale*s).rem(self.f4)
            response = (delta4*(beta2*u**2+gamma3*w)).rem(self.f4)
            polys.append(response)
            images.append(dict(source_mask=source,r_bits=source&15,s_bits=source>>4,
                               u_bits=bits(u),w_bits=bits(w),image_bits=bits(response)))
        columns = [dict(index=i,source=('r' if i<4 else 's'),power=i%4,**images[1<<i]) for i in range(8)]
        matrix = sp.Matrix(16,8,lambda r,c:int(polys[1<<c].nth(r))%2)
        reduced,pivots = rref2(matrix)
        rank = len(pivots)
        assert len({r['image_bits'] for r in images}) == 1<<rank
        for name,row in targets.items():
            if row['ell']:
                continue
            target = from_bits(row['target_bits'])
            target_column = sp.Matrix(16,1,lambda r,c:int(target.nth(r))%2)
            augmented_rank = len(rref2(matrix.row_join(target_column))[1])
            matches = [r['source_mask'] for r in images if r['image_bits']==row['target_bits']]
            assert bool(matches) == (augmented_rank == rank)
            row.update(member=bool(matches),matching_source_masks=matches,
                       augmented_rank=augmented_rank)
        result.update(columns=columns,all256_source_images=images,rank=rank,
                      distinct_image_count=1<<rank,ambient_matrix_pivots=list(pivots),
                      ambient_matrix_rref=[[int(reduced[i,j])%2 for j in range(8)] for i in range(16)])
        return result


def first_schema(own):
    result = dict(genuine_quarter_mod2=own['genuine_quarter_array_mod2'],
                  quarter_bits=own['quarter_binary'],ell_bits=own['ell'])
    if own['ell']:
        result['stage'] = 'first_quarter_low_nonzero'
        return result
    result.update(g_bits=own['g'],ordinary_derivative_bits=own['I'])
    if own['I']:
        result['stage'] = 'first_quarter_derivative_nonzero'
        return result
    result.update(stage='unique_kernel_jet',rho_bits=own['rho'],
                  gamma_R2_bits=own['gamma_mod_f2'],delta16_R2_bits=own['delta16_mod_f2'],
                  denominator_R2_bits=own['denominator_mod_f2'],required_h=own['h'])
    return result


def check_ambient(own, saved):
    halves = {n:r['genuine_half_array_mod4'] for n,r in own['targets'].items()}
    low = {n:r['ell'] for n,r in own['targets'].items()}
    assert low['X_plus'] == low['X_minus']
    assert saved['genuine_half_arrays_mod4'] == halves
    assert saved['lowest_half_classes_R4'] == low
    if low['X_plus']:
        assert saved == dict(genuine_half_arrays_mod4=halves,lowest_half_classes_R4=low,
                             stage='second_half_low_nonzero')
        return 'second_half_low_nonzero'
    for key in ('beta_R30_bits','gamma_R32_bits','coefficient_classes_R4',
                'columns','all256_source_images','rank','distinct_image_count'):
        assert saved[key] == own[key], key
    columns = [from_bits(r['image_bits']) for r in own['columns']]
    images = own['all256_source_images']
    rank = own['rank']
    basis = saved['binary_basis']
    assert len(basis) == rank
    pivots = [r['pivot'] for r in basis]
    assert pivots == sorted(set(pivots),reverse=True)
    polys = []
    for row in basis:
        assert type(row['source_mask']) is int and 0 <= row['source_mask'] < 256
        expected = images[row['source_mask']]['image_bits']
        assert expected == row['image_bits'] and expected.bit_length()-1 == row['pivot']
        polys.append(from_bits(expected))
    basis_matrix = sp.Matrix(16,rank,lambda i,j:int(polys[j].nth(i))%2)
    assert len(rref2(basis_matrix)[1]) == rank
    for name, target in own['targets'].items():
        supplied = saved['targets'][name]
        for key in ('target_bits','member','matching_source_masks'):
            assert supplied[key] == target[key], (name,key)
        source = supplied['normal_source_mask']
        assert type(source) is int and 0 <= source < 256
        remainder = target['target_bits'] ^ images[source]['image_bits']
        assert remainder == supplied['normal_remainder_bits']
        assert all(((remainder >> pivot)&1) == 0 for pivot in pivots)
        assert bool(remainder) != target['member']
        if remainder:
            sep = supplied['separator_bits']
            assert type(sep) is int and 0 <= sep < 2**16
            assert all((sep&r['image_bits']).bit_count()%2 == 0 for r in images)
            assert (sep&target['target_bits']).bit_count()%2 == 1
        else:
            assert source in target['matching_source_masks']
    assert own['targets']['X_plus']['target_bits'] == own['targets']['X_minus']['target_bits']
    assert own['targets']['X_plus']['member'] == own['targets']['X_minus']['member']
    stage = ('unresolved_ambient_member' if own['targets']['X_plus']['member']
             else 'second_half_ambient_nonmember')
    assert saved['stage'] == stage
    return stage


def main():
    here = Path(__file__).resolve().parent
    out = here.parents[3]/'mathematics/computations/outputs'/here.name
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--result',type=Path,default=out/'complete_local_target_second_half_screen.json')
    parser.add_argument('--output',type=Path,default=out/'complete_local_target_second_half_screen_verification.json')
    args = parser.parse_args()
    labels,qrows,krows = source_inputs(out)
    saved = json.loads(args.result.read_text(encoding='utf-8'))
    assert saved['required_inputs'] == ['endpoint_full_triple_image.json',
        'endpoint_full_triple_image_verification.json','augmented_endpoint_kernel_image.json',
        'augmented_endpoint_kernel_image_verification.json']
    assert saved['labels'] == labels and saved['masks'] == MASKS
    assert len(saved['records']) == 32
    assert [r['source_mask'] for r in saved['records']] == MASKS
    assert saved['all32_records_complete'] and saved['actual_exponents_and_q_retained']
    for h,row in krows.items():
        assert row['target_member'] == (((h&81).bit_count()%2) == 0)
    arithmetic = IndependentArithmetic(labels)
    base = saved['base']
    expected_base = dict(P=coefficients(arithmetic.P),V=coefficients(arithmetic.V),
        J=coefficients(arithmetic.J),H0=coefficients(arithmetic.H),T0=coefficients(arithmetic.base),
        delta=coefficients(arithmetic.delta32),delta16=coefficients(arithmetic.delta16),
        base_canonical_mod8=arithmetic.base_full,base_restricted_mod8=arithmetic.base_restricted,
        j_canonical_mod8=arithmetic.j_canonical,
        base_H_evaluations_mod8={str(p):arithmetic.recover(arithmetic.base_weight[p]) for p in (2,3,5)},
        canonical_scalar_precisions={'2':16,'3':24,'5':40})
    assert base == expected_base
    assert arithmetic.delta_binary == arithmetic.delta16_binary**2
    assert binary_poly(coefficients(arithmetic.V)) == arithmetic.f**32
    references = {}
    bundle_cache = {}

    def bundle_weights(word):
        key = tuple(tuple(t) for t in word)
        if key not in bundle_cache:
            bundle_cache[key] = arithmetic.weights(word)
        return bundle_cache[key]

    def reference(name,bundles):
        literal = [t for word in bundles.values() for t in word]
        cost = word_costs(literal,labels)
        by_bundle = {label:bundle_weights(word) for label,word in bundles.items()}
        total = {}
        for p in (2,3,5):
            value = arithmetic.ring.one
            for weight in by_bundle.values():
                value = arithmetic.ring.multiply(value,weight[p])
            total[p] = value
        own = arithmetic.reference(total)
        target = saved['references'][name]
        valuations = {n:r['coefficient_valuation_through_mod8'] for n,r in own['diagnostics'].items()}
        binding = dict(bundle_words=bundles,literal_word=literal,costs=cost,
            bundle_weights={str(p):{label:arithmetic.recover(w[p]) for label,w in by_bundle.items()}
                            for p in (2,3,5)},weights=own['Q_evaluations_mod8'],
            H_weights=own['full_H_evaluations_mod8'],original_restrictions_mod8=own['original_restrictions_mod8'],
            gates=own['global_residual_gates_via_EPX_H_unit_degree'],coefficient_valuations=valuations)
        assert binding == target, name
        assert binding['gates']['F_mod4'] and binding['gates']['X_plus_mod2']
        assert binding['gates']['X_minus_mod2'] and binding['gates']['G_nonzero_mod2']
        references[name] = dict(**binding,diagnostics=own['diagnostics'])
        return own,cost

    records = []
    required_k = set()
    for source,supplied in zip(qrows,saved['records']):
        mask = source['source_mask']
        qname = f'Q:{mask}'
        assert supplied['source_mask'] == mask and supplied['branch'] == 2
        assert supplied['Xi_components'] == source['components']
        assert supplied['Q_reference'] == qname
        qref,qcost = reference(qname,{'Q':source['word']})
        assert qcost == source['word_costs']
        first = first_schema(arithmetic.first_quarter(qref['original_restrictions_mod8']))
        assert first == supplied['first_quarter']
        own_record = dict(source_mask=mask,branch=2,Q_reference=qname,first_quarter=first)
        if first['stage'] != 'unique_kernel_jet':
            outcome = first['stage']
            assert 'selected_kernel' not in supplied and 'product_reference' not in supplied
            assert 'second_half' not in supplied
        else:
            h = first['required_h']
            selected = krows[h]
            expected_selection = dict(h=h,target_member=selected['target_member'],
                components=selected['components'],certificate_input='augmented_endpoint_kernel_image.json')
            if not selected['target_member']:
                outcome = 'kernel_jet_not_attained'
                expected_selection['principal_reduction'] = selected['principal_reduction']
                assert 'product_reference' not in supplied and 'second_half' not in supplied
            else:
                required_k.add(h)
                word = selected['word']
                kc = word_costs(word,labels)
                assert kc['cofactor_trace_degree'] == selected['word_costs']['kernel_trace_degree']
                assert 2*kc['cofactor_trace_degree'] == selected['word_costs']['kernel_reciprocal_degree']
                assert kc['nonzero_terms'] == selected['word_costs']['nonzero_terms']
                assert kc['endpoint_exponent'] == selected['word_costs']['endpoint_exponent']
                expected_selection.update(word=word,kernel_trace_degree=kc['cofactor_trace_degree'])
                rname = f'QK:{mask}'
                rref,rcost = reference(rname,{'Q':source['word'],'K':word})
                assert rcost['cofactor_trace_degree'] == qcost['cofactor_trace_degree']+kc['cofactor_trace_degree']
                quarter = binary_poly([v//4 for v in rref['original_restrictions_mod8']['F']])
                assert quarter.rem(arithmetic.f**8).is_zero
                assert supplied['product_reference'] == rname
                assert supplied['lowest_quarter_mod_f8_cancelled']
                second = arithmetic.second_half(rref['original_restrictions_mod8'])
                outcome = check_ambient(second,supplied['second_half'])
                own_record.update(product_reference=rname,lowest_quarter_mod_f8_cancelled=True,
                                  second_half=second)
            assert expected_selection == supplied['selected_kernel']
            own_record['selected_kernel'] = expected_selection
        assert outcome == supplied['outcome']
        excluded = outcome != 'unresolved_ambient_member'
        assert supplied['joint_F8_either_X4_excluded_in_old_fiber'] == excluded
        own_record.update(outcome=outcome,joint_F8_either_X4_excluded_in_old_fiber=excluded)
        records.append(own_record)
        print(json.dumps(dict(source_mask=mask,verified_outcome=outcome)),flush=True)
    assert set(saved['references']) == set(references)

    # Inspect every cached entry after deriving the necessary references ourselves.
    # Equality of key sets detects both omitted work and unauthorized extra words.
    supplied_factors = {(r['p'],r['generator']):r['value'] for r in saved['factor_values']}
    supplied_powers = {(r['p'],r['generator'],r['exponent']):r['value'] for r in saved['powered_values']}
    assert len(supplied_factors) == len(saved['factor_values'])
    assert len(supplied_powers) == len(saved['powered_values'])
    assert set(supplied_factors) == arithmetic.used_values
    assert set(supplied_powers) == arithmetic.used_powers
    for key,value in supplied_factors.items():
        assert list(arithmetic.factor_value(*key)) == arithmetic.image(value), key
        assert arithmetic.recover(list(arithmetic.factor_value(*key))) == value
    for key,value in supplied_powers.items():
        assert list(arithmetic.factor_power(*key)) == arithmetic.image(value), key
        assert arithmetic.recover(list(arithmetic.factor_power(*key))) == value
    labels_used = {i for p,i in arithmetic.used_values}
    assert len(labels_used) <= 84 and len(arithmetic.used_values) <= 252
    assert len(arithmetic.used_powers) <= 4269 and len(references) <= 64
    summary = dict(outcome_counts=dict(sorted(Counter(r['outcome'] for r in records).items())),
        all32_closed=all(r['joint_F8_either_X4_excluded_in_old_fiber'] for r in records),
        unresolved_masks=[r['source_mask'] for r in records if not r['joint_F8_either_X4_excluded_in_old_fiber']],
        reference_count=len(references),actual_label_count=len(labels_used),
        factor_value_count=len(arithmetic.used_values),powered_value_count=len(arithmetic.used_powers))
    assert summary == saved['summary']
    for key in ('no_new_group_image','no_120bit_image','no_other_word_or_profile',
                'no_full_integer_cofactor_expansion','no_F_over8_class_or_mod16'):
        assert saved[key]
    result = dict(scope='Different AUTHOR complete32-target Laurent/SymPy branch verification',
        required_inputs=saved['required_inputs'],masks=MASKS,summary=summary,
        base=expected_base,references=references,records=records,
        required_kernel_h=sorted(required_k),
        all32_branches_independently_derived=True,all_required_reference_keys_matched=True,
        all_cache_values_and_actual_powers_matched=True,
        all7_full_mod8_arrays_and_genuine_half_quarters_checked=True,
        true_full_Z_base_and_J_prime_divisions_checked=True,
        exact_single_F960_and_integral_trace_identity_checked=True,
        all_required_ambient_columns_256_images_ranks_and_certificates_checked=True,
        quotient_trace_degree=144,Laurent_degree=288,actual_base_degree=374,
        arithmetic='full-Z SymPy original prime divisions; faithful Laurent mod8; direct GF(2) polynomial jets; DomainMatrix GF(2) ambient ranks',
        sympy_version=sp.__version__,author_self_check=True,independent_review=False,
        no_new_group_image=True,no_120bit_image=True,no_other_word_or_profile=True,
        no_full_integer_cofactor_expansion=True,no_F_over8_class_or_mod16=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    partial = args.output.with_suffix(args.output.suffix+'.partial')
    try:
        partial.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        partial.replace(args.output)
    finally:
        if partial.exists():
            partial.unlink()
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
