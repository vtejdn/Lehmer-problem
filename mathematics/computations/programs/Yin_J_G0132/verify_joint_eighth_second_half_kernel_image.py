"""Different AUTHOR check of the C873 joint kernel and all16 C872 references.

Implementation only until explicit execution authorization.  Adopted Omega and
A data are reused, never regenerated.  Only the new source28/14 coordinates
are reconstructed in faithful degree56 Laurent quotients; target polynomials
are independently reconstructed with SymPy.  No new original residual probe.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
import argparse
import json
import sympy as sp
from verify_augmented_endpoint_kernel_image import Ring, bits, division
from verify_full_eighth_kernel_image import (
    CharacterRing, full_trace_factor, xi_unpack, binary_inverse,
)


X,Z = sp.symbols('X Z')
EXPONENT = 960
MASK112 = (1<<112)-1
REMAINING = [203,235,331,363,715,747,843,875,1171,1203,1299,1331,1683,1715,1811,1843]
INPUTS = ['full_eighth_kernel_image.json','full_eighth_kernel_image_verification.json',
          'complete_local_target_second_half_screen.json',
          'complete_local_target_second_half_screen_verification.json']


def bit_poly(value):
    return sp.Poly.from_dict({(i,):1 for i in range(value.bit_length()) if (value>>i)&1},X,modulus=2)


def array_poly(values, modulus=2):
    return sp.Poly.from_list(list(reversed(values)),X,**({'modulus':modulus} if modulus else {'domain':sp.ZZ}))


def decode(word):
    assert type(word) is list and word == sorted(word)
    assert len(word) == len({i for i,e in word})
    assert all(type(i) is int and 0<=i<4193 and type(e) is int and 0<e<960 for i,e in word)
    return dict(word)


def encoded(word):
    return [[i,e] for i,e in sorted(word.items()) if e]


def add_word(first, second, scale=1):
    answer = dict(first)
    for i,e in second.items():
        value = (answer.get(i,0)+scale*e)%960
        if value:
            answer[i] = value
        else:
            answer.pop(i,None)
    return answer


def sum_words(words):
    value = {}
    for word in words:
        value = add_word(value,word)
    return value


def high_rank(vectors):
    """A separate high-pivot elimination, not the producer's low-pivot basis."""
    basis = {}
    for vector in vectors:
        while vector:
            pivot = vector.bit_length()-1
            if pivot not in basis:
                basis[pivot] = vector
                break
            vector ^= basis[pivot]
    return len(basis)


def supplied_reduction(value, rows, supplied):
    lookup = {r['position']:r for r in rows}
    used = supplied['used_positions']
    assert used == sorted(set(used)) and all(p in lookup for p in used)
    remainder = value
    for p in used:
        remainder ^= lookup[p]['vector']
    assert remainder == supplied['remainder']
    assert all(((remainder>>p)&1)==0 for p in lookup)
    # Canonical low-pivot normal form is checked after independent rank/spanning.
    normal = value
    actual_used = []
    for row in sorted(rows,key=lambda r:r['position']):
        if (normal>>row['position'])&1:
            normal ^= row['vector']
            actual_used.append(row['position'])
    assert actual_used == used and normal == remainder
    return remainder


def costs(word, labels):
    counts = Counter()
    endpoint = 0
    terms = []
    for index,e in sorted(word.items()):
        assert 0<e<960
        label = labels[index]
        term = {k:label[k] for k in ('kind','n','q','a','b','trace_degree') if k in label}
        term.update(index=index,exponent=e,degree_contribution=e*label['trace_degree'])
        terms.append(term)
        if label['kind']=='endpoint':
            assert label['trace_degree']==1
            endpoint += e
        else:
            assert label['q']==3**label['a']*5**label['b']
            assert label['trace_degree']==label['q']*(label['n']-1)//2
            for r in sp.divisors(label['n']):
                if r>1:
                    for a in range(label['a']+1):
                        for b in range(label['b']+1):
                            counts[int(r)*3**a*5**b] += e
    degree = sum(t['degree_contribution'] for t in terms)
    assert degree == endpoint+sum(e*int(sp.totient(n))//2 for n,e in counts.items())
    reciprocal = dict(counts)
    if endpoint:
        reciprocal[1] = 2*endpoint
    assert 2*degree == sum(e*int(sp.totient(n)) for n,e in reciprocal.items())
    return dict(terms=terms,endpoint_exponent=endpoint,nonzero_terms=len(word),
        kernel_trace_degree=degree,kernel_reciprocal_degree=2*degree,
        complete_trace_factors=[dict(order=n,multiplicity=e) for n,e in sorted(counts.items())],
        complete_reciprocal_factors=[dict(order=n,multiplicity=e) for n,e in sorted(reciprocal.items())])


class NewSources:
    def __init__(self):
        self.moduli = [bits(sp.Poly((X+1)**28,X,modulus=2)),
                       bits(sp.Poly((X*X+X+1)**14,X,modulus=2))]
        self.old_moduli = [bits(sp.Poly((X+1)**24,X,modulus=2)),
                           bits(sp.Poly((X*X+X+1)**12,X,modulus=2))]
        self.rings = [Ring(m) for m in self.moduli]
        self.old_rings = [Ring(m) for m in self.old_moduli]
        self.recoverers = []
        for order,multiplicity,period,target in zip((3,5),(28,14),(96,80),self.rings):
            cyclo = sp.Poly(sp.cyclotomic_poly(order,Z),Z,modulus=2)**multiplicity
            lr = Ring(bits(cyclo))
            d = target.degree
            assert d==28 and lr.degree==56
            powers = [1]
            for _ in range(period):
                powers.append(lr.multiply(powers[-1],2))
            assert powers[period]==1
            trace = powers[1]^powers[period-1]
            tp = [1]
            for _ in range(d-1):
                tp.append(lr.multiply(tp[-1],trace))
            shifted = [lr.multiply(powers[d-1],v) for v in tp]
            def recover(value,lr=lr,d=d,powers=powers,shifted=shifted):
                work = lr.multiply(powers[d-1],value)
                assert work.bit_length()<=2*d-1
                result = 0
                for j in range(d-1,-1,-1):
                    if (work>>(d-1+j))&1:
                        result |= 1<<j
                        work ^= shifted[j]
                assert work==0
                return result
            assert recover(trace)==2
            @lru_cache(None)
            def kernel(n,q,period=period,lr=lr,recover=recover):
                # Actual q/n labels are preserved.  The verified Laurent z period
                # permits reducing monomial exponents inside this exact quotient.
                value = 0
                a = (n-1)//2
                for j in range(-a,a+1):
                    value ^= 1<<((q*j)%period)
                return recover(lr.reduce(value))
            self.recoverers.append(kernel)

    def image(self,label):
        if label['kind']=='endpoint':
            return (2,2)
        return tuple(fn(label['n'],label['q']) for fn in self.recoverers)

    def multiply(self,a,b):
        return tuple(r.multiply(u,v) for r,u,v in zip(self.rings,a,b))

    def power(self,a,n):
        return tuple(r.power(v,n) for r,v in zip(self.rings,a))

    @lru_cache(None)
    def inverse(self,a):
        result = tuple(binary_inverse(v,r.modulus) for r,v in zip(self.rings,a))
        assert self.multiply(a,result)==(1,1)
        return result

    def project(self,a):
        return [r.reduce(v) for r,v in zip(self.old_rings,a)]

    def kernel(self,a):
        assert self.project(a)==[1,1]
        s,rem = division(a[0]^1,self.old_moduli[0])
        assert rem==0
        r,rem = division(a[1]^1,self.old_moduli[1])
        assert rem==0 and 0<=r<16 and 0<=s<16
        return r,s


class WordChecks:
    def __init__(self, source_ring, source_images, old):
        self.S,self.images,self.old = source_ring,source_images,old
        # Only ring arithmetic on ADOPTED Omega values.  No weight_C2/C5 or
        # mixed-characteristic generator is reconstructed in this program.
        self.B = CharacterRing(full_trace_factor(960))
        self.first = Ring(bits(sp.Poly((X**4+X**3+1)**16,X,modulus=2)))
        self.omegas = [self.B.decode(r['omega']) for r in old['generators']]

    @lru_cache(None)
    def source_square(self,i,bit):
        if bit==0:return self.images[i]
        value=self.source_square(i,bit-1)
        return self.S.multiply(value,value)

    @lru_cache(None)
    def omega_square(self,i,bit):
        if bit==0:return self.omegas[i]
        value=self.omega_square(i,bit-1)
        return self.B.multiply(value,value)

    @lru_cache(None)
    def first_square(self,i,bit):
        if bit==0:return self.old['generators'][i]['xi_components'][0]
        value=self.first_square(i,bit-1)
        return self.first.multiply(value,value)

    @lru_cache(None)
    def image(self,word):
        source=(1,1);omega=self.B.one;first=1
        for i,e in word:
            assert 0<e<960
            for bit in range(e.bit_length()):
                if (e>>bit)&1:
                    source=self.S.multiply(source,self.source_square(i,bit))
                    omega=self.B.multiply(omega,self.omega_square(i,bit))
                    first=self.first.multiply(first,self.first_square(i,bit))
        return source,tuple(self.B.encode(omega)),first

    def kernel_vector(self,word):
        source,omega,first=self.image(tuple(tuple(t) for t in encoded(word)))
        assert first==1 and omega[0]==1 and omega[1].bit_length()<=112
        r,s=self.S.kernel(source)
        return omega[1] | (r<<112) | (s<<116)


def target_data(ref,delta):
    arrays=ref['original_restrictions_mod8']
    assert all(v%4==0 for v in arrays['F'])
    f=sp.Poly(X**4+X**3+1,X,modulus=2)
    f2,f4,f28=f**2,f**4,f**28
    quarter=array_poly([v//4 for v in arrays['F']])
    numerator=quarter.exquo(f**8).rem(f28)
    gamma=array_poly(arrays['c']).exquo(f**4)
    beta=array_poly(arrays['b']).exquo(f**6)
    gamma28=gamma.rem(f28)
    gamma2=(gamma28**2).rem(f28)
    t=(numerator*sp.invert(gamma2,f28)).rem(f28)
    signs={}
    for name in ('X_plus','X_minus'):
        assert all(v%2==0 for v in arrays[name])
        signs[name]=bits(array_poly([v//2 for v in arrays[name]]).exquo(f4).rem(f4))
    assert signs['X_plus']==signs['X_minus']
    p=sp.Poly(X*X+X+1,X,modulus=2)
    lam=sp.Poly(X**3+X,X,modulus=2)
    chi=sp.Poly(X*(X*X+X+1)**2,X,modulus=2)
    columns=[]
    for i in range(8):
        r=sp.Poly(X**i if i<4 else 0,X,modulus=2)
        s=sp.Poly(X**(i-4) if i>=4 else 0,X,modulus=2)
        u=(p**12*r.compose(lam)).rem(f2)
        w=(sp.Poly(X+1,X,modulus=2)**24*s.compose(chi)).rem(f4)
        columns.append(bits((delta*(beta**2*u**2+gamma**3*w)).rem(f4)))
    return dict(quarter_bits=bits(quarter),quarter_div_f8=bits(numerator),
        gamma_R28_bits=bits(gamma28),gamma_squared_R28_bits=bits(gamma2),
        beta_R30_bits=bits(beta),gamma_R32_bits=bits(gamma),t_bits=bits(t),
        g_bits=signs['X_plus'],both_g_signs=signs),columns


def project_vector(vector,columns):
    response=0
    for i,c in enumerate(columns):
        if (vector>>(112+i))&1:response^=c
    return (vector&MASK112) | (response<<112)


def main():
    here=Path(__file__).resolve().parent
    out=here.parents[3]/'mathematics/computations/outputs'/here.name
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--result',type=Path,default=out/'joint_eighth_second_half_kernel_image.json')
    parser.add_argument('--output',type=Path,default=out/'joint_eighth_second_half_kernel_image_verification.json')
    args=parser.parse_args()
    old,checked,screen,screencheck=[json.loads((out/n).read_text(encoding='utf-8')) for n in INPUTS]
    saved=json.loads(args.result.read_text(encoding='utf-8'))
    assert saved['required_inputs']==INPUTS
    assert old['generator_count']==checked['verified_generator_count']==4193
    assert old['additive_rank']==checked['additive_rank']==54
    assert checked['both_relation_span_inclusions_checked']
    assert checked['verified_all_relation_count']==len(old['relations'])==6310
    assert old['relations']==checked['verified_relations']
    assert len(checked['verified_images'])==4193
    for row,check in zip(old['generators'],checked['verified_images']):
        assert row['xi_image']==check['xi_image'] and row['omega']==check['omega']
    assert checked['verified_literal_odd_lifts']==45 and checked['verified_literal_principal_lifts']==92
    assert old['quotient_image_order']==45*(1<<92)
    assert screen['summary']==screencheck['summary']
    assert screen['summary']['unresolved_masks']==REMAINING
    assert screencheck['all32_branches_independently_derived']
    assert screencheck['all7_full_mod8_arrays_and_genuine_half_quarters_checked']
    assert screen['base']==screencheck['base']
    labels=[{k:v for k,v in r.items() if k not in
             ('xi_image','xi_components','omega','weight_C2','weight_C5')} for r in old['generators']]
    assert len(labels)==len(saved['generators'])==4193
    assert labels[-1]['n']==481 and labels[-1]['q']==1
    assert sum(r['trace_degree'] for r in labels)==1+539881*15296+240
    sources=NewSources()
    assert saved['source_moduli']==sources.moduli
    actual=[];generator_records=[]
    for i,(label,prior) in enumerate(zip(labels,old['generators'])):
        image=sources.image(label)
        assert sources.project(image)==prior['xi_components'][1:]
        assert sources.power(image,480)==(1,1)
        row=dict(index=i,actual_label=label,Xi_plus_components=[prior['xi_components'][0],*image],
                 Xi16_components=prior['xi_components'],old_omega=prior['omega'])
        assert row==saved['generators'][i]
        actual.append(image);generator_records.append(row)
    assert actual[-1]==(1^bits(sp.Poly((X+1)**16,X,modulus=2)),1)
    assert old['generators'][-1]['omega']==[1,0]
    print('all4193 new source images independently reconstructed and projected',flush=True)
    words=WordChecks(sources,actual,old)
    odd={};pivots={}
    for prior in old['odd_lifts']:
        word=decode(prior['word'])
        source,omega,first=words.image(tuple(tuple(t) for t in encoded(word)))
        assert list(omega)==prior['omega']
        xi=xi_unpack(prior['xi_image'])
        assert sources.project(source)==list(xi[1:]) and first==xi[0]
        odd[tuple(prior['pair'])]=dict(prior,source28_14=list(source))
    for prior in old['principal_lifts']:
        word=decode(prior['word'])
        source,omega,first=words.image(tuple(tuple(t) for t in encoded(word)))
        assert list(omega)==prior['omega']
        xi=xi_unpack(prior['xi_image'])
        assert sources.project(source)==list(xi[1:]) and first==xi[0]
        pivots[prior['position']]=dict(prior,source28_14=list(source))
    assert len(odd)==45 and len(pivots)==92 and odd[(0,0)]['word']==[]
    assert saved['odd_lifts']==[odd[p] for p in sorted(odd)]
    assert saved['principal_lifts']==[pivots[p] for p in sorted(pivots)]
    relations=[];counts=Counter()
    assert len(saved['relations'])==6310
    for prior,reported in zip(old['relations'],saved['relations']):
        recipe=prior['recipe'];kind=recipe['kind'];counts[kind]+=1
        if kind=='generator':
            i=recipe['generator'];o=odd[tuple(recipe['odd_pair'])]
            source=sources.multiply(actual[i],sources.inverse(tuple(o['source28_14'])))
            word=add_word({i:1},decode(o['word']),-1)
            for pos in recipe['positions']:
                source=sources.multiply(source,sources.inverse(tuple(pivots[pos]['source28_14'])))
                word=add_word(word,decode(pivots[pos]['word']),-1)
        elif kind=='square':
            p=pivots[recipe['position']]
            assert recipe['later_positions']==p['later_square_positions']
            source=sources.power(tuple(p['source28_14']),2)
            word=add_word({},decode(p['word']),2)
            for pos in recipe['later_positions']:
                assert pos>recipe['position']
                source=sources.multiply(source,sources.inverse(tuple(pivots[pos]['source28_14'])))
                word=add_word(word,decode(pivots[pos]['word']),-1)
        else:
            assert kind=='odd'
            a,b,c=[tuple(recipe[k]) for k in ('a','b','c')]
            assert c==((a[0]+b[0])%15,(a[1]+b[1])%3)
            source=sources.multiply(sources.multiply(tuple(odd[a]['source28_14']),tuple(odd[b]['source28_14'])),
                                    sources.inverse(tuple(odd[c]['source28_14'])))
            word=add_word(add_word(decode(odd[a]['word']),decode(odd[b]['word'])),decode(odd[c]['word']),-1)
        r,s=sources.kernel(source)
        A=prior['vector'];assert prior['omega']==[1,A] and A.bit_length()<=112
        vector=A | (r<<112) | (s<<116)
        row=dict(index=prior['index'],recipe=recipe,adopted_A=A,source28_14=list(source),
                 r_bits=r,s_bits=s,vector=vector,word=encoded(word))
        assert {k:v for k,v in reported.items() if k!='linear_reduction'}==row
        relations.append(row)
    assert counts=={'generator':4193,'square':92,'odd':2025}
    assert saved['relation_counts']==dict(counts)
    assert [r['index'] for r in relations]==list(range(6310))
    print('all6310 new relation source values and literal recipes checked',flush=True)
    basis=saved['kernel_basis'];basis_by_pos={r['position']:r for r in basis}
    assert len(basis)==saved['kernel_rank']==high_rank([r['vector'] for r in relations])
    assert len(basis_by_pos)==len(basis)
    assert len(basis)<=62
    for row in basis:
        pos=row['position'];value=row['vector']
        assert pos==(value&-value).bit_length()-1
        seed=relations[row['seed_relation']]
        construction=row['construction_positions']
        assert construction==sorted(set(construction)) and all(p in basis_by_pos for p in construction)
        # A prior row can have a numerically larger pivot.  Construction is
        # ordered by relation discovery, not by the final sorted pivot table.
        assert all(basis_by_pos[p]['seed_relation']<row['seed_relation'] for p in construction)
        combined=seed['vector'];word=decode(seed['word'])
        for p in construction:
            combined^=basis_by_pos[p]['vector']
            word=add_word(word,decode(basis_by_pos[p]['word']))
        assert combined==value and encoded(word)==row['word']
        assert words.kernel_vector(word)==value
        assert costs(word,labels)==row['costs']
    assert [r['position'] for r in basis]==sorted(basis_by_pos)
    assert high_rank([r['vector'] for r in basis])==len(basis)
    for row,reported in zip(relations,saved['relations']):
        assert supplied_reduction(row['vector'],basis,reported['linear_reduction'])==0
        row['linear_reduction']=reported['linear_reduction']
    oldbasis=old['additive_basis']
    assert len(oldbasis)==54 and high_rank([r['vector'] for r in oldbasis])==54
    for row in basis:
        assert high_rank([r['vector'] for r in oldbasis]+[row['vector']&MASK112])==54
    assert [r['adopted_A'] for r in relations]==[r['vector'] for r in old['relations']]
    assert high_rank([r['adopted_A'] for r in relations])==54
    assert saved['quotient_image_order']==45*(1<<92)
    assert saved['joint_image_order']==45*(1<<(92+len(basis)))
    print('both120-bit relation-span inclusions and all positive basis words checked',flush=True)

    screen_rows={r['source_mask']:r for r in screen['records']}
    delta=array_poly(screen['base']['delta'])
    targets=[];used_spaces={};expected_space_columns=[]
    assert len(saved['targets'])==16
    for mask,reported in zip(REMAINING,saved['targets']):
        row=screen_rows[mask];assert row['outcome']=='unresolved_ambient_member'
        refkey=row['product_reference'];ref=screen['references'][refkey]
        checkedref=screencheck['references'][refkey]
        assert {k:v for k,v in checkedref.items() if k!='diagnostics'}==ref
        values,columns=target_data(ref,delta)
        assert columns==[r['image_bits'] for r in row['second_half']['columns']]
        for k,v in values.items():assert reported[k]==v,(mask,k)
        assert reported['source_mask']==mask and reported['reference_key']==refkey
        assert reported['reference']==ref
        key=tuple(columns)
        if key not in used_spaces:
            space_id=len(used_spaces);used_spaces[key]=space_id;expected_space_columns.append(columns)
            projected=saved['projected_spaces'][space_id]
            assert projected['index']==space_id and projected['columns']==columns
            images=[dict(kernel_basis_position=r['position'],vector=project_vector(r['vector'],columns)) for r in basis]
            pb=projected['basis'];lookup={r['position']:r for r in pb}
            assert projected['rank']==len(pb)==high_rank([r['vector'] for r in images])
            assert len(lookup)==len(pb)
            for prow in pb:
                pos=prow['position'];vector=prow['vector']
                assert pos==(vector&-vector).bit_length()-1
                seed=basis_by_pos[prow['seed_kernel_basis_position']]
                combined=project_vector(seed['vector'],columns);word=decode(seed['word'])
                prevs=prow['construction_positions']
                assert prevs==sorted(set(prevs)) and all(p in lookup for p in prevs)
                assert all(lookup[p]['seed_kernel_basis_position']<prow['seed_kernel_basis_position'] for p in prevs)
                for p in prevs:
                    combined^=lookup[p]['vector'];word=add_word(word,decode(lookup[p]['word']))
                assert combined==vector and encoded(word)==prow['word']
                kv=words.kernel_vector(word)
                assert kv==prow['kernel_vector'] and project_vector(kv,columns)==vector
                assert costs(word,labels)==prow['costs']
            assert [r['position'] for r in pb]==sorted(lookup)
            assert high_rank([r['vector'] for r in pb])==len(pb)
            assert len(projected['all_kernel_basis_images'])==len(images)
            for img,reported_img in zip(images,projected['all_kernel_basis_images']):
                assert {k:v for k,v in reported_img.items() if k!='linear_reduction'}==img
                assert supplied_reduction(img['vector'],pb,reported_img['linear_reduction'])==0
        space_id=used_spaces[key]
        assert reported['projected_space_index']==space_id
        projected=saved['projected_spaces'][space_id];pb=projected['basis']
        target=values['t_bits'] | (values['g_bits']<<112)
        decision=reported['decision']
        assert decision['target_bits']==target
        remainder=supplied_reduction(target,pb,decision['reduction'])
        member=high_rank([r['vector'] for r in pb]+[target])==len(pb)
        assert member==decision['member']==(remainder==0)
        plookup={r['position']:r for r in pb}
        word=sum_words(decode(plookup[p]['word']) for p in decision['reduction']['used_positions'])
        assert decision['normalization_word']==encoded(word)
        kv=words.kernel_vector(word)
        assert kv==decision['normalization_kernel_vector']
        assert project_vector(kv,columns)==target^remainder
        if member:
            assert decision['word']==encoded(word)
            cost=costs(word,labels)
            degree=ref['costs']['cofactor_trace_degree']+cost['kernel_trace_degree']
            cost.update(reference_plus_kernel_cofactor_degree=degree,
                reference_plus_kernel_original_trace_degree_not_probed=374+degree,
                reference_plus_kernel_original_reciprocal_degree_not_probed=2*(374+degree))
            assert cost==decision['costs']
            assert decision['conclusion']=='actual kernel attains F8 and lowest second-half cancellation ONLY; full X4 untested'
        else:
            sep=decision['separator_bits']
            assert type(sep) is int and 0<=sep<1<<128
            assert all((sep&project_vector(r['vector'],columns)).bit_count()%2==0 for r in basis)
            assert (sep&target).bit_count()%2==1
            assert decision['conclusion']=='entire specified Xi16 fiber excluded from F8/either full X4'
        arem=supplied_reduction(values['t_bits'],oldbasis,reported['A_only_reduction'])
        amember=high_rank([r['vector'] for r in oldbasis]+[values['t_bits']])==54
        assert reported['A_only_member']==amember==(arem==0)
        targets.append(dict(reported))
        print(json.dumps(dict(source_mask=mask,verified_A_only_member=amember,verified_joint_member=member)),flush=True)
    assert len(saved['projected_spaces'])==len(used_spaces)
    assert [r['columns'] for r in saved['projected_spaces']]==expected_space_columns
    summary=dict(target_count=16,positive_target_count=sum(r['decision']['member'] for r in targets),
        kernel_rank=len(basis),projected_ranks=[r['rank'] for r in saved['projected_spaces']],
        A_only_members=sum(r['A_only_member'] for r in targets),distinct_A_targets=len({r['t_bits'] for r in targets}))
    assert summary==saved['summary']
    assert saved['source_coordinate_order']==['source3_depth28','source5_depth14']
    assert saved['kernel_bit_packing']=={'A':[0,112],'r':[112,4],'s':[116,4]}
    assert saved['target_bit_packing']=={'A':[0,112],'g':[112,16]} and saved['joint_exponent']==960
    for flag in ('adopted_mixed_images_reused_without_regeneration','all4193_new_source_projections_checked',
                 'all6310_relations_and_reductions_retained','positive_words_use_mod960_not480',
                 'no_original_new_product_probe','no_full_X4_success_claim','no_other_profile_or_target','no_word_optimization'):
        assert saved[flag]
    result=dict(scope='Different AUTHOR full new source28/14 joint120 kernel and all16 targets',
        required_inputs=INPUTS,summary=summary,verified_generators=generator_records,
        verified_relations=relations,kernel_basis=basis,projected_spaces=saved['projected_spaces'],targets=targets,
        kernel_rank=len(basis),verified_new_source_count=4193,verified_relation_count=6310,
        verified_odd_lifts=45,verified_principal_lifts=92,
        both120_relation_span_inclusions_checked=True,complete_old_A_projection_checked=True,
        all_new_positive_word_images_and_complete_costs_checked=True,
        all16_target_jets_and_A_only_decisions_independently_recomputed=True,
        all_projected_span_and_target_certificates_checked=True,
        faithful_Laurent_moduli=['Phi3^28','Phi5^14'],Laurent_degrees=[56,56],Laurent_z_periods=[96,80],
        arithmetic='faithful binary Laurent source reconstruction; packed-convolution source arithmetic; reused adopted Omega values; SymPy GF(2) target jets; separate high-pivot rank tests',
        adopted_mixed_images_reused_without_regeneration=True,no_original_new_product_probe=True,
        no_full_X4_success_claim=True,no_other_profile_or_target=True,no_word_optimization=True,
        author_self_check=True,independent_review=False,sympy_version=sp.__version__)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    partial=args.output.with_suffix(args.output.suffix+'.partial')
    try:
        partial.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        partial.replace(args.output)
    finally:
        if partial.exists():partial.unlink()
    print(json.dumps(summary))


if __name__=='__main__':
    main()
