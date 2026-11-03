"""IMPLEMENTATION ONLY: C873 joint120-bit kernel and all16 C872 references.

Reuse the adopted C869 mixed-characteristic images/A relation coordinates.
Compute only the new depth28/14 binary sources and their complete relations.
No original residual of a new product, optimization or enlarged profile occurs.
"""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import json

import augmented_endpoint_kernel_image as xi
from first_gate_character import rawmul, remainder, multiply, power, inverse
from full_eighth_kernel_image import MixedRing, add_word, encode_word

F, P5, EXPONENT = 25, 7, 960
F4, F8, F28 = (xi.rawpower(F,j) for j in (4,8,28))
S3_24, S3_28 = xi.rawpower(3,24), xi.rawpower(3,28)
S5_12, S5_14 = xi.rawpower(P5,12), xi.rawpower(P5,14)
SOURCE_MODS = (S3_28,S5_14)
MASK112 = (1<<112)-1
REMAINING = [203,235,331,363,715,747,843,875,1171,1203,1299,1331,1683,1715,1811,1843]
INPUTS = ['full_eighth_kernel_image.json','full_eighth_kernel_image_verification.json',
          'complete_local_target_second_half_screen.json',
          'complete_local_target_second_half_screen_verification.json']


def source_multiply(a,b):
    return tuple(multiply(u,v,m) for u,v,m in zip(a,b,SOURCE_MODS))


def source_power(a,n):
    return tuple(power(u,n,m) for u,m in zip(a,SOURCE_MODS))


def source_inverse(a):
    return tuple(inverse(u,m) for u,m in zip(a,SOURCE_MODS))


def source_project(a):
    return [remainder(a[0],S3_24),remainder(a[1],S5_12)]


def kernel_coordinates(source):
    assert source_project(source)==[1,1]
    s,zero=xi.divide(source[0]^1,S3_24);assert zero==0
    r,zero=xi.divide(source[1]^1,S5_12);assert zero==0
    assert s.bit_length()<=4 and r.bit_length()<=4
    return r,s


def linear_reduce(value,basis):
    used=[]
    for position,row in sorted(basis.items()):
        if value>>position&1:
            value^=row['vector'];used.append(position)
    return dict(remainder=value,used_positions=used)


def compose_binary(a,b,modulus):
    value=0
    for i in range(a.bit_length()-1,-1,-1):
        value=multiply(value,b,modulus)^((a>>i)&1)
    return value


def positive_costs(word,labels):
    counts=Counter();endpoint=0;terms=[]
    for index,e in sorted(word.items()):
        assert 0<e<960
        label=labels[index]
        term={k:label[k] for k in ('kind','n','q','a','b','trace_degree') if k in label}
        term.update(index=index,exponent=e,degree_contribution=e*label['trace_degree'])
        terms.append(term)
        if label['kind']=='endpoint':
            endpoint+=e
        else:
            assert label['q']==3**label['a']*5**label['b']
            for r in range(2,label['n']+1):
                if label['n']%r==0:
                    for a in range(label['a']+1):
                        for b in range(label['b']+1):
                            counts[r*3**a*5**b]+=e
    degree=sum(t['degree_contribution'] for t in terms)
    assert degree==endpoint+sum(e*xi.totient(n)//2 for n,e in counts.items())
    reciprocal=dict(counts)
    if endpoint:reciprocal[1]=2*endpoint
    assert 2*degree==sum(e*xi.totient(n) for n,e in reciprocal.items())
    return dict(terms=terms,endpoint_exponent=endpoint,nonzero_terms=len(word),
                kernel_trace_degree=degree,kernel_reciprocal_degree=2*degree,
                complete_trace_factors=[dict(order=n,multiplicity=e) for n,e in sorted(counts.items())],
                complete_reciprocal_factors=[dict(order=n,multiplicity=e) for n,e in sorted(reciprocal.items())])


def main():
    here=Path(__file__).resolve().parent
    out=here.parents[3]/'mathematics/computations/outputs'/here.name
    old,checked,screen,screencheck=[json.loads((out/n).read_text(encoding='utf-8')) for n in INPUTS]
    assert old['generator_count']==checked['verified_generator_count']==4193
    assert old['additive_rank']==checked['additive_rank']==54
    assert old['quotient_image_order']==45*(1<<92)
    assert checked['both_relation_span_inclusions_checked']
    assert checked['verified_literal_odd_lifts']==45 and checked['verified_literal_principal_lifts']==92
    assert checked['verified_all_relation_count']==len(old['relations'])==6310
    assert len(checked['verified_images'])==4193 and len(checked['verified_relations'])==6310
    assert len(old['odd_lifts'])==45 and len(old['principal_lifts'])==92
    assert old['relation_counts']==checked['relation_counts']=={'generator':4193,'square':92,'odd':2025}
    for row,check in zip(old['generators'],checked['verified_images']):
        assert row['xi_image']==check['xi_image'] and row['omega']==check['omega']
    assert old['relations']==checked['verified_relations']
    assert screen['summary']==screencheck['summary']
    assert screen['summary']['unresolved_masks']==REMAINING
    assert screencheck['all32_branches_independently_derived']
    assert screencheck['all7_full_mod8_arrays_and_genuine_half_quarters_checked']
    assert screen['base']==screencheck['base']
    labels=[{k:v for k,v in row.items() if k not in
             ('xi_image','xi_components','omega','weight_C2','weight_C5')} for row in old['generators']]
    assert len(labels)==4193 and labels[-1]['n']==481 and labels[-1]['q']==1
    assert sum(r['trace_degree'] for r in labels)==1+539881*15296+240

    @lru_cache(None)
    def cheb_pair(n,modulus):
        if n==0:return 0,2
        a,b=cheb_pair(n//2,modulus)
        even=multiply(a,a,modulus)
        odd=multiply(a,b,modulus)^2
        return (even,odd) if n%2==0 else (odd,multiply(b,b,modulus))

    tables={}
    for q in sorted({r['q'] for r in labels if r['kind']=='rectangle'}):
        for modulus in SOURCE_MODS:
            argument=cheb_pair(q,modulus)[0]
            previous,current=0,argument;values=[1]
            for _ in range(240):
                values.append(values[-1]^current)
                previous,current=current,multiply(argument,current,modulus)^previous
            tables[(q,modulus)]=values
    sources=[];generators=[]
    for i,(label,prior) in enumerate(zip(labels,old['generators'])):
        source=(2,2) if label['kind']=='endpoint' else tuple(
            tables[(label['q'],m)][(label['n']-1)//2] for m in SOURCE_MODS)
        assert source_project(source)==prior['xi_components'][1:]
        assert source_power(source,480)==(1,1)
        sources.append(source)
        generators.append(dict(index=i,actual_label=label,
            Xi_plus_components=[prior['xi_components'][0],*source],
            Xi16_components=prior['xi_components'],old_omega=prior['omega']))
    assert sources[-1]==(1^xi.rawpower(3,16),1)
    assert old['generators'][-1]['omega']==[1,0]
    print('all4193 new depth28/14 source values and old projections complete',flush=True)

    ring=MixedRing()
    @lru_cache(None)
    def source_square(i,bit):
        if bit==0:return sources[i]
        v=source_square(i,bit-1);return source_multiply(v,v)
    @lru_cache(None)
    def omega_square(i,bit):
        if bit==0:return tuple(old['generators'][i]['omega'])
        v=omega_square(i,bit-1);return ring.multiply(v,v)
    @lru_cache(None)
    def actual_word_image(encoded):
        source=(1,1);omega=ring.one
        for i,e in encoded:
            assert 0<e<960
            for bit in range(e.bit_length()):
                if e>>bit&1:
                    source=source_multiply(source,source_square(i,bit))
                    omega=ring.multiply(omega,omega_square(i,bit))
        return source,omega
    @lru_cache(None)
    def first_coordinate_word(encoded):
        value=1
        for i,e in encoded:
            value=multiply(value,power(old['generators'][i]['xi_components'][0],e,xi.MODS[0]),xi.MODS[0])
        return value
    def kernel_word_vector(word):
        encoded=tuple(tuple(t) for t in encode_word(word))
        source,omega=actual_word_image(encoded)
        assert first_coordinate_word(encoded)==1
        r,s=kernel_coordinates(source)
        assert omega[0]==1 and omega[1].bit_length()<=112
        return omega[1] | (r<<112) | (s<<116)

    odd={};pivots={}
    for row in old['odd_lifts']:
        source,omega=actual_word_image(tuple(tuple(t) for t in row['word']))
        assert list(omega)==row['omega'] and source_project(source)==list(xi.unpack(row['xi_image'])[1:])
        assert first_coordinate_word(tuple(tuple(t) for t in row['word']))==xi.unpack(row['xi_image'])[0]
        odd[tuple(row['pair'])]=dict(row,source28_14=list(source))
    for row in old['principal_lifts']:
        source,omega=actual_word_image(tuple(tuple(t) for t in row['word']))
        assert list(omega)==row['omega'] and source_project(source)==list(xi.unpack(row['xi_image'])[1:])
        assert first_coordinate_word(tuple(tuple(t) for t in row['word']))==xi.unpack(row['xi_image'])[0]
        pivots[row['position']]=dict(row,source28_14=list(source))
    assert len(odd)==45 and len(pivots)==92 and odd[(0,0)]['word']==[]
    print('all45 odd and92 principal lifted source words complete',flush=True)

    relations=[];kinds=Counter()
    for prior in old['relations']:
        recipe=prior['recipe'];kind=recipe['kind'];kinds[kind]+=1
        if kind=='generator':
            index=recipe['generator'];o=odd[tuple(recipe['odd_pair'])]
            source=source_multiply(sources[index],source_inverse(tuple(o['source28_14'])))
            word=add_word({index:1},dict(o['word']),-1)
            for pos in recipe['positions']:
                source=source_multiply(source,source_inverse(tuple(pivots[pos]['source28_14'])))
                word=add_word(word,dict(pivots[pos]['word']),-1)
        elif kind=='square':
            pivot=pivots[recipe['position']]
            assert recipe['later_positions']==pivot['later_square_positions']
            source=source_power(tuple(pivot['source28_14']),2)
            word=add_word({},dict(pivot['word']),2)
            for pos in recipe['later_positions']:
                assert pos>recipe['position']
                source=source_multiply(source,source_inverse(tuple(pivots[pos]['source28_14'])))
                word=add_word(word,dict(pivots[pos]['word']),-1)
        else:
            assert kind=='odd'
            a,b,c=[tuple(recipe[k]) for k in ('a','b','c')]
            assert c==((a[0]+b[0])%15,(a[1]+b[1])%3)
            oa,ob,oc=odd[a],odd[b],odd[c]
            source=source_multiply(source_multiply(tuple(oa['source28_14']),tuple(ob['source28_14'])),
                                   source_inverse(tuple(oc['source28_14'])))
            word=add_word(add_word(dict(oa['word']),dict(ob['word'])),dict(oc['word']),-1)
        r,s=kernel_coordinates(source)
        A=prior['vector'];assert prior['omega']==[1,A] and A.bit_length()<=112
        vector=A | (r<<112) | (s<<116)
        relations.append(dict(index=prior['index'],recipe=recipe,adopted_A=A,
                              source28_14=list(source),r_bits=r,s_bits=s,vector=vector,
                              word=encode_word(word)))
    assert kinds=={'generator':4193,'square':92,'odd':2025} and len(relations)==6310
    print('all6310 complete lifted relation vectors and literal recipes prepared',flush=True)

    basis={}
    for row in relations:
        reduced=linear_reduce(row['vector'],basis);value=reduced['remainder']
        if value:
            pos=(value&-value).bit_length()-1
            word=dict(row['word'])
            for prev in reduced['used_positions']:word=add_word(word,dict(basis[prev]['word']))
            assert kernel_word_vector(word)==value
            basis[pos]=dict(position=pos,vector=value,seed_relation=row['index'],
                construction_positions=reduced['used_positions'],word=encode_word(word),costs=positive_costs(word,labels))
    assert len(basis)<=62  # adopted A rank54 plus eight new source coordinates
    for row in relations:
        row['linear_reduction']=linear_reduce(row['vector'],basis)
        assert row['linear_reduction']['remainder']==0
    old_basis={r['position']:r for r in old['additive_basis']}
    assert len(old_basis)==54
    for row in basis.values():assert linear_reduce(row['vector']&MASK112,old_basis)['remainder']==0
    # All adopted relation A values occur as projections of the complete new list;
    # their retained old reductions prove the reverse projection inclusion.
    assert [r['adopted_A'] for r in relations]==[r['vector'] for r in old['relations']]
    print('complete120-bit kernel span and positive basis checks complete',flush=True)

    delta=xi.binary(screen['base']['delta'])
    f2=xi.rawpower(F,2);lam=10;chi=rawmul(2,xi.rawpower(7,2))
    projected_spaces=[];map_keys={};targets=[]
    rows={r['source_mask']:r for r in screen['records']}

    def make_columns(beta,gamma):
        cols=[]
        for i in range(8):
            r=(1<<i) if i<4 else 0;s=(1<<(i-4)) if i>=4 else 0
            u=multiply(remainder(xi.rawpower(7,12),f2),compose_binary(r,lam,f2),f2)
            w=multiply(remainder(xi.rawpower(3,24),F4),compose_binary(s,chi,F4),F4)
            cols.append(multiply(remainder(delta,F4),
                multiply(power(beta,2,F4),rawmul(u,u),F4)^multiply(power(gamma,3,F4),w,F4),F4))
        return cols
    def response(sourcebits,columns):
        value=0
        for i,c in enumerate(columns):
            if sourcebits>>i&1:value^=c
        return value
    def project_vector(vector,columns):
        return (vector&MASK112) | (response(vector>>112,columns)<<112)

    for mask in REMAINING:
        row=rows[mask];assert row['outcome']=='unresolved_ambient_member'
        refname=row['product_reference'];ref=screen['references'][refname]
        checkedref=screencheck['references'][refname]
        assert {k:v for k,v in checkedref.items() if k!='diagnostics'}==ref
        arrays=ref['original_restrictions_mod8']
        assert all(v%4==0 for v in arrays['F'])
        quarter=xi.binary([v//4 for v in arrays['F']]);numerator,zero=xi.divide(quarter,F8);assert zero==0
        gamma,zero=xi.divide(xi.binary(arrays['c']),F4);assert zero==0
        beta,zero=xi.divide(xi.binary(arrays['b']),xi.rawpower(F,6));assert zero==0
        numerator=remainder(numerator,F28);gamma28=remainder(gamma,F28)
        gamma2=multiply(gamma28,gamma28,F28)
        t=multiply(numerator,inverse(gamma2,F28),F28)
        gsign={}
        for name in ('X_plus','X_minus'):
            assert all(v%2==0 for v in arrays[name])
            g,zero=xi.divide(xi.binary([v//2 for v in arrays[name]]),F4);assert zero==0
            gsign[name]=remainder(g,F4)
        assert gsign['X_plus']==gsign['X_minus'];g=gsign['X_plus']
        columns=make_columns(beta,gamma)
        assert columns==[r['image_bits'] for r in row['second_half']['columns']]
        key=tuple(columns)
        if key not in map_keys:
            mapid=len(projected_spaces);map_keys[key]=mapid
            pb={};images=[]
            for pos,krow in sorted(basis.items()):
                image=project_vector(krow['vector'],columns)
                reduced=linear_reduce(image,pb);value=reduced['remainder']
                images.append(dict(kernel_basis_position=pos,vector=image))
                if value:
                    lead=(value&-value).bit_length()-1
                    word=dict(krow['word'])
                    for prev in reduced['used_positions']:word=add_word(word,dict(pb[prev]['word']))
                    kv=kernel_word_vector(word);assert project_vector(kv,columns)==value
                    pb[lead]=dict(position=lead,vector=value,seed_kernel_basis_position=pos,
                        construction_positions=reduced['used_positions'],word=encode_word(word),
                        kernel_vector=kv,costs=positive_costs(word,labels))
            for image in images:
                image['linear_reduction']=linear_reduce(image['vector'],pb)
                assert image['linear_reduction']['remainder']==0
            projected_spaces.append(dict(index=mapid,columns=columns,basis=[pb[p] for p in sorted(pb)],
                                         rank=len(pb),all_kernel_basis_images=images))
        mapid=map_keys[key];pb={r['position']:r for r in projected_spaces[mapid]['basis']}
        target=t | (g<<112);reduced=linear_reduce(target,pb)
        word={}
        for pos in reduced['used_positions']:word=add_word(word,dict(pb[pos]['word']))
        kv=kernel_word_vector(word)
        assert project_vector(kv,columns)==target^reduced['remainder']
        member=reduced['remainder']==0
        decision=dict(target_bits=target,member=member,reduction=reduced,
                      normalization_word=encode_word(word),normalization_kernel_vector=kv)
        if member:
            cost=positive_costs(word,labels)
            cost['reference_plus_kernel_cofactor_degree']=ref['costs']['cofactor_trace_degree']+cost['kernel_trace_degree']
            cost['reference_plus_kernel_original_trace_degree_not_probed']=374+cost['reference_plus_kernel_cofactor_degree']
            cost['reference_plus_kernel_original_reciprocal_degree_not_probed']=2*(374+cost['reference_plus_kernel_cofactor_degree'])
            decision.update(word=encode_word(word),costs=cost,
                            conclusion='actual kernel attains F8 and lowest second-half cancellation ONLY; full X4 untested')
        else:
            bit=(reduced['remainder']&-reduced['remainder']).bit_length()-1
            separator=sum(((linear_reduce(1<<i,pb)['remainder']>>bit)&1)<<i for i in range(128))
            assert all((separator&r['vector']).bit_count()%2==0 for r in pb.values())
            assert (separator&target).bit_count()%2==1
            decision.update(separator_bits=separator,conclusion='entire specified Xi16 fiber excluded from F8/either full X4')
        A_reduction=linear_reduce(t,old_basis)
        targets.append(dict(source_mask=mask,reference_key=refname,reference=ref,
            quarter_bits=quarter,quarter_div_f8=numerator,gamma_R28_bits=gamma28,gamma_squared_R28_bits=gamma2,
            beta_R30_bits=beta,gamma_R32_bits=gamma,t_bits=t,g_bits=g,both_g_signs=gsign,
            A_only_reduction=A_reduction,A_only_member=(A_reduction['remainder']==0),
            projected_space_index=mapid,decision=decision))
        print(json.dumps(dict(source_mask=mask,A_only_member=A_reduction['remainder']==0,joint_member=member)),flush=True)
    assert len(targets)==16
    payload=dict(scope='C873 complete new source28/14 joint120 kernel and ALL16 retained C872 references',
        required_inputs=INPUTS,adopted_mixed_images_reused_without_regeneration=True,
        source_moduli=[S3_28,S5_14],source_coordinate_order=['source3_depth28','source5_depth14'],
        kernel_bit_packing={'A':[0,112],'r':[112,4],'s':[116,4]},target_bit_packing={'A':[0,112],'g':[112,16]},
        joint_exponent=960,generators=generators,odd_lifts=[odd[p] for p in sorted(odd)],
        principal_lifts=[pivots[p] for p in sorted(pivots)],relation_counts=dict(kinds),relations=relations,
        kernel_basis=[basis[p] for p in sorted(basis)],kernel_rank=len(basis),
        quotient_image_order=45*(1<<92),joint_image_order=45*(1<<(92+len(basis))),
        projected_spaces=projected_spaces,targets=targets,
        summary=dict(target_count=16,positive_target_count=sum(r['decision']['member'] for r in targets),
                     kernel_rank=len(basis),projected_ranks=[m['rank'] for m in projected_spaces],
                     A_only_members=sum(r['A_only_member'] for r in targets),
                     distinct_A_targets=len({r['t_bits'] for r in targets})),
        all4193_new_source_projections_checked=True,all6310_relations_and_reductions_retained=True,
        positive_words_use_mod960_not480=True,no_original_new_product_probe=True,
        no_full_X4_success_claim=True,no_other_profile_or_target=True,no_word_optimization=True,
        author_self_check=True,independent_review=False)
    path=out/'joint_eighth_second_half_kernel_image.json';tmp=path.with_suffix('.json.partial')
    tmp.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8');tmp.replace(path)
    print(json.dumps(payload['summary']))


if __name__=='__main__':main()
