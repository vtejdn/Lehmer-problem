"""IMPLEMENTATION ONLY: exact old4193-alphabet full-X4 source image.

No execution until the new source/presentation theorem is adopted and root GO.
The two actual sources replace three large cofactor weights, using the proved
canonical epsilon carry. ALL6369 words, ALL32 references and BOTH full targets
are retained. No new original-mod8 probe, full-M alphabet or optimization.
"""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import argparse
import ctypes
import json
import os
import time

from main import add, mul, power as zpower, compose as zcompose, chebyshev
from first_gate_character import rawmul, remainder, multiply, power, inverse
from full_eighth_kernel_image import add_word, encode_word
from joint_eighth_second_half_kernel_image import positive_costs
from augmented_endpoint_kernel_image import totient
from full_second_half_ambient_screen import (
    MASKS, input_case_equal, recover_data, make_columns)
from second_half_ambient_response import bits, bpow, bdiv, compose, reduce_vector

INPUTS = [
    'joint_eighth_second_half_kernel_image.json',
    'joint_eighth_second_half_kernel_image_verification.json',
    'complete_four_coset_next_half_screen.json',
    'complete_four_coset_next_half_screen_verification.json']
P5, EXPONENT = 7, 960


class Budget:
    """Own-process working set and elapsed cap; no system process enumeration."""
    def __init__(self, seconds, mib):
        self.start = time.monotonic()
        self.seconds, self.mib, self.peak_mib = seconds, mib, 0.0

    def check(self):
        elapsed = time.monotonic() - self.start
        if os.name == 'nt':
            from ctypes import wintypes
            class Counters(ctypes.Structure):
                _fields_ = [('cb', wintypes.DWORD), ('PageFaultCount', wintypes.DWORD)] + [
                    (n, ctypes.c_size_t) for n in (
                        'PeakWorkingSetSize', 'WorkingSetSize', 'QuotaPeakPagedPoolUsage',
                        'QuotaPagedPoolUsage', 'QuotaPeakNonPagedPoolUsage',
                        'QuotaNonPagedPoolUsage', 'PagefileUsage', 'PeakPagefileUsage')]
            c = Counters()
            c.cb = ctypes.sizeof(c)
            kernel = ctypes.WinDLL('kernel32', use_last_error=True)
            psapi = ctypes.WinDLL('psapi', use_last_error=True)
            kernel.GetCurrentProcess.restype = wintypes.HANDLE
            psapi.GetProcessMemoryInfo.argtypes = [
                wintypes.HANDLE, ctypes.POINTER(Counters), wintypes.DWORD]
            assert psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(c), c.cb)
            current = c.WorkingSetSize / 1048576
            self.peak_mib = max(self.peak_mib, c.PeakWorkingSetSize / 1048576)
        else:
            import resource
            current = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
            self.peak_mib = max(self.peak_mib, current)
        if elapsed > self.seconds or self.peak_mib > self.mib:
            raise RuntimeError(f'resource cap: elapsed={elapsed:.1f}s working={current:.1f}MiB')
        return dict(elapsed_seconds=elapsed, observed_peak_working_mib=self.peak_mib)


def publish(path, payload, budget=None):
    temporary = path.with_suffix(path.suffix + '.partial')
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with temporary.open('w', encoding='utf-8', newline='\n') as handle:
            json.dump(payload, handle, indent=2)
            handle.write('\n')
        if budget is not None:
            budget.check()
        temporary.replace(path)
    finally:
        if temporary.exists():
            temporary.unlink()


@lru_cache(maxsize=8192)
def spread36(value):
    assert value.bit_length() <= 36
    return int.from_bytes(bytes((value >> i) & 1 for i in range(36)), 'little')


class EpsilonSource:
    """B5 in the ACTUAL epsilon basis: low<36, even high<24."""
    one, zero = (1, 0), (0, 0)

    def __init__(self, j5_epsilon):
        assert len(j5_epsilon) == 37 and j5_epsilon[-1] == 1
        self.low_modulus = bits(j5_epsilon)
        assert self.low_modulus == 1 << 36
        self.high_modulus = bits([v // 2 for v in j5_epsilon])
        self.low_mask, self.high_mask = (1 << 36)-1, (1 << 24)-1

    def normalize(self, low, high):
        # Subtract the monic epsilon36+2D. Only the high plane changes below36.
        high ^= rawmul(low >> 36, self.high_modulus)
        return low & self.low_mask, high & self.high_mask

    def from_coefficients(self, values):
        return self.normalize(bits(values), bits([v // 2 for v in values]))

    def add(self, a, b):
        return self.normalize(a[0] ^ b[0], a[1] ^ b[1] ^ (a[0] & b[0]))

    def negative(self, a):
        return self.normalize(a[0], a[1] ^ a[0])

    def subtract(self, a, b):
        return self.add(a, self.negative(b))

    def multiply(self, a, b):
        if a == self.one:
            return b
        if b == self.one:
            return a
        if a == self.zero or b == self.zero:
            return self.zero
        # Binary convolution coefficients are at most36, so base256 has no carry.
        digits = (spread36(a[0]) * spread36(b[0])).to_bytes(71, 'little')
        low = sum((v & 1) << i for i, v in enumerate(digits))
        high = sum(((v >> 1) & 1) << i for i, v in enumerate(digits))
        high ^= rawmul(a[0], b[1]) ^ rawmul(a[1], b[0])
        return self.normalize(low, high)

    def power(self, a, n):
        result = self.one
        while n:
            if n & 1:
                result = self.multiply(result, a)
            n >>= 1
            if n:
                a = self.multiply(a, a)
        return result

    def inverse(self, a):
        seed = (inverse(a[0], self.low_modulus), 0)
        error = self.multiply(a, seed)
        assert error[0] == 1
        result = self.multiply(seed, (1, error[1]))
        assert self.multiply(a, result) == self.one
        return result


def set_bits(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length()-1
        mask ^= low


def source_fields(source):
    return dict(source_b_bits=source[0], source_c=list(source[1]))


def main():
    here = Path(__file__).resolve().parent
    out = here.parents[1] / 'outputs' / here.name
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=out/'full_fourth_gate_known_word_span.json')
    parser.add_argument('--max-seconds', type=float, default=1800)
    parser.add_argument('--max-working-mib', type=float, default=1024)
    args = parser.parse_args()
    assert args.max_seconds > 0 and args.max_working_mib > 0
    budget = Budget(args.max_seconds, args.max_working_mib)
    checkpoint = args.output.with_suffix('.incomplete.json')
    old, oldcheck, screen, screencheck = [
        json.loads((out/name).read_text(encoding='utf-8')) for name in INPUTS]
    assert old['generators'] == oldcheck['verified_generators']
    assert old['relations'] == oldcheck['verified_relations']
    assert old['kernel_basis'] == oldcheck['kernel_basis']
    assert old['kernel_rank'] == oldcheck['kernel_rank'] == 59
    assert oldcheck['verified_new_source_count'] == 4193
    assert oldcheck['verified_relation_count'] == 6310
    assert oldcheck['verified_odd_lifts'] == 45 and oldcheck['verified_principal_lifts'] == 92
    assert oldcheck['both120_relation_span_inclusions_checked']
    assert oldcheck['all_new_positive_word_images_and_complete_costs_checked']
    assert old['relation_counts'] == {'generator': 4193, 'square': 92, 'odd': 2025}
    assert screen['base'] == screencheck['base'] and screen['summary'] == screencheck['summary']
    assert screen['masks'] == screencheck['masks'] == MASKS
    assert screen['nullspace_certificate'] == screencheck['nullspace_certificate']
    assert screen['fibers'] == screencheck['fibers']
    assert screencheck['all448_original_mod8_arrays_checked']
    assert screencheck['all64_four_coset_bindings_independently_derived']
    assert screencheck['true_full_Z_base_and_J_prime_divisions_checked']
    chosen = []
    assert len(screen['cases']) == len(screencheck['cases']) == 64
    for index, (a, b) in enumerate(zip(screen['cases'], screencheck['cases'])):
        input_case_equal(a, b)
        if a['next_half']['targets']['X_plus']['member']:
            assert a['next_half']['targets']['X_minus']['member']
            chosen.append((index, a))
    assert len(chosen) == 32 and Counter(a['source_mask'] for _, a in chosen) == {m: 2 for m in MASKS}
    assert [(r['source_mask'], r['coset_bits']) for r in screen['cases']] == [
        (m, e) for m in MASKS for e in range(4)]
    labels = [r['actual_label'] for r in old['generators']]
    assert labels == screen['labels']
    assert len(labels) == 4193 and labels[-1]['n'] == 481 and labels[-1]['q'] == 1
    assert sum(r['trace_degree'] for r in labels) == 8258020017
    for _,reference in chosen:
        assert all(0 <= i < 4193 and e > 0 for i,e in reference['literal_word'])
        assert reference['costs']['trace_degree'] == 374+sum(
            labels[i]['trace_degree']*e for i,e in reference['literal_word'])
        assert reference['costs']['endpoint_exponent'] == 4+sum(
            e for i,e in reference['literal_word'] if i == 0)
    for label in labels:
        if label['kind'] == 'rectangle':
            assert label['q'] == 3**label['a'] * 5**label['b']
            assert label['trace_degree'] == label['q'] * (label['n']-1)//2
    P, F30 = [1,4,-4,-1,1], [1,-4,-4,1,1]
    V = zcompose(F30, chebyshev(32))
    J = mul(zpower(P,4), V)
    delta = add(V, zpower(P,32), -1)
    assert all(v % 2 == 0 for v in delta)
    delta = [v//2 for v in delta]
    assert (P,V,J,delta) == tuple(screen['base'][k] for k in ('P','V','J','delta'))
    F192 = add(chebyshev(32), [-1])
    J5_Y = mul(zpower([1,1],4), F192)
    J5_epsilon = zcompose(J5_Y, [-1,1])
    c_ring = EpsilonSource(J5_epsilon)
    b_modulus, b_half = bpow(P5,28), bpow(P5,14)
    source3_old = bpow(3,28)
    Y_c = c_ring.from_coefficients([-1,1])  # Y=epsilon-1, including coefficient3.
    assert Y_c == (3,1)
    source_one = (1, c_ring.one)

    def source_multiply(a, b):
        return multiply(a[0],b[0],b_modulus), c_ring.multiply(a[1],b[1])

    @lru_cache(None)
    def source_inverse(a):
        return inverse(a[0],b_modulus), c_ring.inverse(a[1])

    def source_square(a):
        return source_multiply(a,a)

    def coordinates(source):
        r, zero = bdiv(source[0] ^ 1, b_half)
        assert zero == 0 and r.bit_length() <= 28
        low, high = source[1]
        assert (low & ((1 << 28)-1)) == 1 and high.bit_length() <= 24
        w = low >> 28
        assert w.bit_length() <= 8
        vector = r | (w << 28) | (high << 36)
        assert source == (1 ^ rawmul(b_half,r),(1 | (w << 28),high))
        return dict(r_bits=r,w_epsilon_bits=w,s_epsilon_bits=high,vector60=vector)

    def report_stage(name, payload):
        resources = budget.check()
        publish(checkpoint, dict(complete=False, completed_stage=name,
                                resources=resources, formed_payload=payload))
        print(json.dumps(dict(stage=name,**resources)), flush=True)

    @lru_cache(None)
    def b_cheb_pair(n):
        if n == 0:
            return 0,2
        a,b = b_cheb_pair(n//2)
        even = multiply(a,a,b_modulus)
        odd = multiply(a,b,b_modulus) ^ 2
        return (even,odd) if n % 2 == 0 else (odd,multiply(b,b,b_modulus))

    @lru_cache(None)
    def c_cheb_pair(n):
        if n == 0:
            return c_ring.from_coefficients([2]),Y_c
        a,b = c_cheb_pair(n//2)
        even = c_ring.subtract(c_ring.multiply(a,a),c_ring.from_coefficients([2]))
        odd = c_ring.subtract(c_ring.multiply(a,b),Y_c)
        return (even,odd) if n % 2 == 0 else (
            odd,c_ring.subtract(c_ring.multiply(b,b),c_ring.from_coefficients([2])))

    tables = {}
    for q in sorted({r['q'] for r in labels if r['kind'] == 'rectangle'}):
        ab,ac = b_cheb_pair(q)[0],c_cheb_pair(q)[0]
        pb,cb,pc,cc = 0,ab,c_ring.from_coefficients([2]),ac
        values = [source_one]
        for _ in range(240):
            values.append((values[-1][0] ^ cb,c_ring.add(values[-1][1],cc)))
            pb,cb = cb,multiply(ab,cb,b_modulus) ^ pb
            pc,cc = cc,c_ring.subtract(c_ring.multiply(ac,cc),pc)
        tables[q] = values
        budget.check()
    generators, sources = [], []
    for i,(label,prior) in enumerate(zip(labels,old['generators'])):
        source = (2,c_ring.from_coefficients([-3,1])) if label['kind'] == 'endpoint' else (
            tables[label['q']][(label['n']-1)//2])
        assert remainder(source[0],b_half) == prior['Xi_plus_components'][2]
        eps_low = source[1][0] & ((1 << 28)-1)
        assert compose(eps_low,3,source3_old) == prior['Xi_plus_components'][1]
        assert power(source[0],96,b_modulus) == 1
        assert c_ring.power(source[1],64) == c_ring.one
        sources.append(source)
        generators.append(dict(prior,**source_fields(source)))
    report_stage('all4193_actual_two_source_values',generators)

    @lru_cache(None)
    def generator_power(i, bit):
        if bit == 0:
            return sources[i]
        return source_square(generator_power(i,bit-1))

    def word_source(word):
        value = source_one
        for i,e in sorted(word.items()):
            assert 0 <= i < 4193 and 0 < e < 960
            for bit in set_bits(e):
                value = source_multiply(value,generator_power(i,bit))
        return value

    def degree(word):
        return sum(labels[i]['trace_degree']*e for i,e in word.items())

    odd, pivots, odd_lifts, principal_lifts = {}, {}, [], []
    for row in old['odd_lifts']:
        value = word_source(dict(row['word']))
        odd[tuple(row['pair'])] = (row,value)
        odd_lifts.append(dict(row,**source_fields(value)))
    for row in old['principal_lifts']:
        value = word_source(dict(row['word']))
        pivots[row['position']] = (row,value)
        principal_lifts.append(dict(row,**source_fields(value)))
    assert len(odd) == 45 and len(pivots) == 92
    relations, relation_sources = [], []
    for prior in old['relations']:
        recipe = prior['recipe']
        if recipe['kind'] == 'generator':
            i = recipe['generator']
            o,ov = odd[tuple(recipe['odd_pair'])]
            value = source_multiply(sources[i],source_inverse(ov))
            word = add_word({i:1},dict(o['word']),-1)
            positions = recipe['positions']
        elif recipe['kind'] == 'square':
            p,pv = pivots[recipe['position']]
            assert recipe['later_positions'] == p['later_square_positions']
            assert all(k > recipe['position'] for k in recipe['later_positions'])
            value = source_square(pv)
            word = add_word({},dict(p['word']),2)
            positions = recipe['later_positions']
        else:
            assert recipe['kind'] == 'odd'
            a,b,c = (tuple(recipe[k]) for k in ('a','b','c'))
            assert c == ((a[0]+b[0])%15,(a[1]+b[1])%3)
            ar,av = odd[a]; br,bv = odd[b]; cr,cv = odd[c]
            value = source_multiply(source_multiply(av,bv),source_inverse(cv))
            word = add_word(add_word(dict(ar['word']),dict(br['word'])),dict(cr['word']),-1)
            positions = []
        for pos in positions:
            pr,pv = pivots[pos]
            value = source_multiply(value,source_inverse(pv))
            word = add_word(word,dict(pr['word']),-1)
        assert encode_word(word) == prior['word']
        relations.append(dict(prior,**source_fields(value)))
        relation_sources.append(value)
        if len(relations) % 128 == 0:
            budget.check()
    assert len(relations) == 6310
    basis_by_position = {r['position']:r for r in old['kernel_basis']}
    basis_values, basis_lifts = {}, []
    for row in sorted(old['kernel_basis'],key=lambda r:r['seed_relation']):
        seed = row['seed_relation']
        word = dict(relations[seed]['word'])
        value, vector = relation_sources[seed],relations[seed]['vector']
        for pos in row['construction_positions']:
            assert basis_by_position[pos]['seed_relation'] < seed
            value = source_multiply(value,basis_values[pos])
            word = add_word(word,dict(basis_by_position[pos]['word']))
            vector ^= basis_by_position[pos]['vector']
        assert encode_word(word) == row['word'] and vector == row['vector']
        assert positive_costs(word,labels) == row['costs']
        basis_values[row['position']] = value
        basis_lifts.append(dict(row,**source_fields(value)))
    basis_lifts.sort(key=lambda r:r['position'])
    report_stage('all6310_recipes_and59_basis_lifts',
                 dict(odd_lifts=odd_lifts,principal_lifts=principal_lifts,
                      relations=relations,basis_lifts=basis_lifts))

    known = []
    for j,row in enumerate(relations):
        positions = row['linear_reduction']['used_positions']
        assert row['linear_reduction']['remainder'] == 0
        word, value, vector = dict(row['word']),relation_sources[j],row['vector']
        for pos in positions:
            word = add_word(word,dict(basis_by_position[pos]['word']))
            value = source_multiply(value,basis_values[pos])
            vector ^= basis_by_position[pos]['vector']
        assert vector == 0
        known.append(dict(index=len(known),kind='relation_correction',relation_index=j,
            correction_positions=positions,word=encode_word(word),cofactor_degree=degree(word),
            endpoint_exponent=word.get(0,0),
            **source_fields(value),coordinates=coordinates(value),theta_vector=vector))
        if j % 128 == 0:
            budget.check()
    for row in old['kernel_basis']:
        word = add_word({},dict(row['word']),2)
        value = source_square(basis_values[row['position']])
        known.append(dict(index=len(known),kind='basis_square',basis_position=row['position'],
            correction_positions=[],word=encode_word(word),cofactor_degree=degree(word),
            endpoint_exponent=word.get(0,0),
            **source_fields(value),coordinates=coordinates(value),theta_vector=0))
    assert len(known) == 6369

    def word_from_known(mask):
        word = {}
        for index in set_bits(mask):
            word = add_word(word,dict(known[index]['word']))
        return word

    linear = {}
    for row in known:
        value, mask = reduce_vector(row['coordinates']['vector60'],linear)
        mask ^= 1 << row['index']
        if value:
            linear[value.bit_length()-1] = (value,mask)
    source_basis = []
    for pivot,(vector,mask) in sorted(linear.items(),reverse=True):
        word = word_from_known(mask)
        actual = word_source(word)
        coords = coordinates(actual)
        assert coords['vector60'] == vector
        source_basis.append(dict(pivot=pivot,vector60=vector,known_word_mask=mask,
            word=encode_word(word),costs=positive_costs(word,labels),
            **source_fields(actual),coordinates=coords))
    for row in known:
        rest,mask = reduce_vector(row['coordinates']['vector60'],linear)
        assert rest == 0
        checked_vector = 0
        for index in set_bits(mask):
            checked_vector ^= known[index]['coordinates']['vector60']
        assert checked_vector == row['coordinates']['vector60']
        row['linear_reduction'] = dict(remainder_bits=rest,known_word_mask=mask)
    report_stage('complete6369_actual_source_span',
                 dict(known_words=known,source_basis=source_basis))

    def image_of_coordinates(columns, vector):
        result = 0
        for bit in set_bits(vector):
            result ^= columns[bit]['image_bits']
        return result

    def correction_from_basis_mask(mask,reference):
        word,vector = {},0
        for index in set_bits(mask):
            row = source_basis[index]
            word = add_word(word,dict(row['word']))
            vector ^= row['vector60']
        actual = word_source(word)
        coords = coordinates(actual)
        assert coords['vector60'] == vector
        costs = positive_costs(word,labels)
        original_degree = reference['costs']['trace_degree']+costs['kernel_trace_degree']
        trace_counts = Counter({r['order']:r['multiplicity']
                                for r in reference['costs']['complete_trace_factors']})
        trace_counts.update({r['order']:r['multiplicity'] for r in costs['complete_trace_factors']})
        rec_counts = Counter({r['order']:r['multiplicity']
                              for r in reference['costs']['complete_reciprocal_factors']})
        rec_counts.update({r['order']:r['multiplicity'] for r in costs['complete_reciprocal_factors']})
        endpoint = reference['costs']['endpoint_exponent']+costs['endpoint_exponent']
        assert original_degree == endpoint+sum(e*totient(n)//2 for n,e in trace_counts.items())
        assert 2*original_degree == sum(e*totient(n) for n,e in rec_counts.items())
        return dict(word=encode_word(word),costs=costs,**source_fields(actual),coordinates=coords,
            resulting_original_trace_degree=original_degree,
            resulting_reciprocal_degree=2*original_degree,
            resulting_endpoint_exponent=endpoint,
            resulting_complete_trace_factors=[dict(order=n,multiplicity=e) for n,e in sorted(trace_counts.items())],
            resulting_complete_reciprocal_factors=[dict(order=n,multiplicity=e) for n,e in sorted(rec_counts.items())])

    cases = []
    for case_index,reference in chosen:
        data = recover_data(reference['original_restrictions_mod8'],bits(P),delta)
        columns = make_columns(data,bits(P))
        projected, projection = [],{}
        for index,row in enumerate(source_basis):
            image = image_of_coordinates(columns,row['vector60'])
            projected.append(dict(source_basis_index=index,vector60=row['vector60'],image_bits=image))
            value,mask = reduce_vector(image,projection)
            mask ^= 1 << index
            if value:
                projection[value.bit_length()-1] = (value,mask)
        reductions = []
        for row in projected:
            rest,mask = reduce_vector(row['image_bits'],projection)
            assert rest == 0
            check = 0
            for index in set_bits(mask):
                check ^= projected[index]['image_bits']
            assert check == row['image_bits']
            reductions.append(dict(source_basis_index=row['source_basis_index'],
                                   remainder_bits=rest,source_mask=mask))
        for value,mask in projection.values():
            check = 0
            for index in set_bits(mask):
                check ^= projected[index]['image_bits']
            assert check == value
        decisions = {}
        for name,target in data['normalized_targets_bits'].items():
            rest,mask = reduce_vector(target,projection)
            decision = dict(target_bits=target,member=(rest==0),
                            normal_remainder_bits=rest,source_mask=mask)
            if rest:
                pivot = rest.bit_length()-1
                separator = sum(((reduce_vector(1<<i,projection)[0]>>pivot)&1)<<i for i in range(112))
                assert all((separator & r['image_bits']).bit_count()%2==0 for r in projected)
                assert (separator & target).bit_count()%2==1
                decision['separator_bits'] = separator
            else:
                correction = correction_from_basis_mask(mask,reference)
                assert image_of_coordinates(columns,correction['coordinates']['vector60']) == target
                decision['correction'] = correction
            decisions[name] = decision
        cases.append(dict(source_mask=reference['source_mask'],coset_bits=reference['coset_bits'],
            source_case_index=case_index,reference={k:v for k,v in reference.items() if k!='next_half'},
            data=data,columns=columns,projected_generators=projected,rank=len(projection),
            basis=[dict(pivot=p,image_bits=v,source_mask=s)
                   for p,(v,s) in sorted(projection.items(),reverse=True)],
            basis_reductions=reductions,targets=decisions,
            outcome='actual_positive_correction' if any(r['member'] for r in decisions.values())
                    else 'nonmember_in_old_alphabet_correction_image'))
        budget.check()
        print(json.dumps(dict(source_mask=reference['source_mask'],coset_bits=reference['coset_bits'],
            projected_rank=len(projection),members={k:v['member'] for k,v in decisions.items()})),flush=True)
    assert len(cases) == 32
    summary = dict(generator_count=4193,actual_source_value_count=8386,
        odd_lift_count=45,principal_lift_count=92,relation_count=6310,basis_lift_count=59,
        known_word_count=6369,source_rank=len(source_basis),reference_count=32,target_count=64,
        projected_ranks=dict(Counter(r['rank'] for r in cases)),
        member_target_count=sum(d['member'] for r in cases for d in r['targets'].values()),
        nonmember_target_count=sum(not d['member'] for r in cases for d in r['targets'].values()),
        full_M_exclusion_claim=False,no_new_original_residual_probe=True)
    payload = dict(scope='Complete old4193-alphabet actual source-kernel span and32 full-X4 reference pairs',
        required_inputs=INPUTS,parameters=dict(exponent=960,binary_source_modulus=b_modulus,
            binary_half_modulus=b_half,J5_Y=J5_Y,J5_epsilon=J5_epsilon,
            epsilon_low_degree=36,epsilon_even_degree=24,source_packing=dict(r=0,w=28,s=36),
            source_dimension=60,target_dimension=112,
            word_list='6310 Z_j times all indicated positive B_p, followed by59 B_p squared',
            full_M_alphabet_not_evaluated=True),
        base=screen['base'],generators=generators,odd_lifts=odd_lifts,
        principal_lifts=principal_lifts,relations=relations,basis_lifts=basis_lifts,
        known_words=known,source_basis=source_basis,cases=cases,summary=summary,
        selected_case_ids=[[r['source_mask'],r['coset_bits']] for _,r in chosen],
        all_adopted_input_math_bindings_checked=True,all6310_literal_recipes_checked=True,
        all59_basis_construction_words_checked=True,all6369_Theta_identities_checked=True,
        all_source_span_inclusions_checked=True,all_projected_span_inclusions_checked=True,
        all64_full_target_preimages_or_separators_checked=True,
        all_positive_word_actual_sources_and_complete_costs_checked=True,
        actual_epsilon_integer_carry_retained=True,old_BF_weights_not_used=True,
        actual_q_not_residue_degrees=True,all_final_word_exponents_mod960=True,
        no_full_polynomial_expansion=True,no_new_original_residual_probe=True,
        no_larger_modulus_profile_or_word_optimization=True,
        author_self_check=True,independent_review=False,resources=budget.check())
    publish(args.output,payload,budget)
    if checkpoint.exists():
        checkpoint.unlink()
    print(json.dumps(summary),flush=True)


if __name__ == '__main__':
    main()
