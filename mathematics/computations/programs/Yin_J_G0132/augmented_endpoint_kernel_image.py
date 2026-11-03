"""Complete4192-label augmented Xi16 image and ALL256 kernel-jet targets.

No cofactor candidate scan, full integer expansion or original residual probe.
Sparse tracked words are materialized only for new pivots and target certificates.
"""
from pathlib import Path
from collections import deque
from math import gcd
import json
from first_gate_character import rawmul, remainder, multiply, power, inverse

F, P = 25, 7
EXPONENT = 480
MASK64, MASK24 = (1<<64)-1, (1<<24)-1


def rawpower(a,n):
    out=1
    for _ in range(n):
        out=rawmul(out,a)
    return out


MODS=(rawpower(F,16),rawpower(3,24),rawpower(P,12))


def unpack(value):
    return value & MASK64,(value>>64)&MASK24,value>>88


def pack(values):
    a,b,c=values
    return a | (b<<64) | (c<<88)


ONE=pack((1,1,1))


def gmultiply(a,b):
    return pack([multiply(u,v,m) for u,v,m in zip(unpack(a),unpack(b),MODS)])


def gpower(a,n):
    return pack([power(u,n,m) for u,m in zip(unpack(a),MODS)])


def ginverse(a):
    return pack([inverse(u,m) for u,m in zip(unpack(a),MODS)])


def divide(a,b):
    q=0
    while a and a.bit_length()>=b.bit_length():
        shift=a.bit_length()-b.bit_length()
        q ^= 1<<shift
        a ^= b<<shift
    return q,a


def leading(value):
    if value==ONE:
        return None
    for component,(unit,prime,degree,length,offset) in enumerate(zip(
            unpack(value),(F,3,P),(4,1,2),(16,24,12),(0,60,83))):
        if unit==1:
            continue
        work,layer=unit^1,0
        while True:
            q,r=divide(work,prime)
            if r:
                break
            work,layer=q,layer+1
        assert 1<=layer<length,(component,layer)
        bit=(r&-r).bit_length()-1
        return offset+degree*(layer-1)+bit
    raise AssertionError('nonidentity principal element has a leading position')


def addword(first,second,scale=1):
    result=dict(first)
    for i,e in second.items():
        value=(result.get(i,0)+scale*e)%EXPONENT
        if value:
            result[i]=value
        else:
            result.pop(i,None)
    return result


def encoded(word):
    return [[i,e] for i,e in sorted(word.items())]


def totient(n):
    result,remaining,d=n,n,2
    while d*d<=remaining:
        if remaining%d==0:
            result-=result//d
            while remaining%d==0:
                remaining//=d
        d+=1
    if remaining>1:
        result-=result//remaining
    return result



def imultiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c


def ipower(a,n):
    result=[1]
    for _ in range(n):
        result=imultiply(result,a)
    return result


def idivide(a,b):
    assert b[-1]==1
    work=list(a)
    out=[0]*max(1,len(work)-len(b)+1)
    for i in range(len(work)-len(b),-1,-1):
        coefficient=work[i+len(b)-1]
        out[i]=coefficient
        for j,v in enumerate(b):
            work[i+j]-=coefficient*v
    assert not any(work)
    return out


def binary(values):
    return sum((v%2)<<i for i,v in enumerate(values))


def recompute_old_word_data(output):
    saved=json.loads((output/'endpoint_word_mod8.json').read_text(encoding='utf-8'))
    check=json.loads((output/'endpoint_word_mod8_verification.json').read_text(encoding='utf-8'))
    assert saved['original_restrictions_mod8']==check['original_restrictions_mod8']
    assert saved['full_trace_degree']==3390998 and saved['actual_single_F960']
    rows=saved['original_restrictions_mod8']
    ff4=rawpower(F,4)
    cb= binary(rows['c'])
    gamma,zero=divide(cb,ff4)
    assert zero==0
    gamma=remainder(gamma,rawpower(F,2))
    assert all(v%4==0 for v in rows['F'])
    quarter=binary([v//4 for v in rows['F']])
    normalized,zero=divide(quarter,ff4)
    assert zero==0
    g=remainder(normalized,ff4)
    assert all((g>>i)&1==0 for i in range(1,16,2))
    rho=sum(((g>>(2*i))&1)<<i for i in range(8))
    assert rawmul(rho,rho)==g
    ff=[1,4,-4,-1,1]
    v960=idivide(saved['J_coefficients'],ipower(ff,4))
    f32=ipower(ff,32)
    assert len(v960)==len(f32)==129
    difference=[a-b for a,b in zip(v960,f32)]
    assert all(v%2==0 for v in difference)
    delta32=[v//2 for v in difference]
    db=binary(delta32)
    assert all((db>>i)&1==0 for i in range(1,db.bit_length(),2))
    delta16=sum(((db>>(2*i))&1)<<i for i in range((db.bit_length()+1)//2))
    assert rawmul(delta16,delta16)==db
    delta16_mod=remainder(delta16,rawpower(F,2))
    denominator=multiply(delta16_mod,gamma,rawpower(F,2))
    desired=multiply(rho,inverse(denominator,rawpower(F,2)),rawpower(F,2))
    return dict(input_mod8='endpoint_word_mod8.json',
        input_verification='endpoint_word_mod8_verification.json',
        c_binary=cb,quarter_binary=quarter,normalized_quarter_mod_f4=g,
        unique_square_root_mod_f2=rho,gamma_Q_mod_f2=gamma,
        actual_V960_coefficients=v960,actual_delta32_coefficients=delta32,
        delta32_binary=db,delta16_binary=delta16,delta16_mod_f2=delta16_mod,
        denominator_mod_f2=denominator,required_h=desired,
        no_root_supplied_target_constant=True)


def main():
    here=Path(__file__).resolve().parent
    output=here.parents[3]/'mathematics/computations/outputs'/here.name
    old=json.loads((output/'endpoint_full_triple_image.json').read_text(encoding='utf-8'))
    actual_data=recompute_old_word_data(output)
    desired_h=actual_data['required_h']
    targets=[dict(h=h,components=[1^rawmul(rawpower(F,14),h),1,1]) for h in range(256)]
    qs=sorted({1,*[3**i for i in range(1,9)],*[5**i for i in range(1,9)],
               15,45,75,2025,135,1125,675,225,1215,3645,6075,5625,375,405,1875,18225})
    ns=[n for n in range(2,480) if gcd(n,480)==1]
    assert len(qs)==33 and len({q%480 for q in qs})==33 and sum(qs)==539881
    assert len(ns)==127 and sum((n-1)//2 for n in ns)==15296
    q_parameters={}
    for q in qs:
        work,a,b=q,0,0
        while work%3==0:
            a+=1;work//=3
        while work%5==0:
            b+=1;work//=5
        assert work==1
        q_parameters[q]=(a,b)

    # Compute every declared kernel directly in each full trace/source quotient.
    kernels=[]
    for modulus in MODS:
        cheb=[0,2]
        for _ in range(2,480):
            cheb.append(multiply(2,cheb[-1],modulus)^cheb[-2])
        table={}
        for q in qs:
            argument=cheb[q%480]
            previous,current,values=0,argument,[1]
            for _ in range(1,240):
                values.append(values[-1]^current)
                previous,current=current,multiply(argument,current,modulus)^previous
            table[q]=values
        kernels.append(table)
    images=[dict(kind='endpoint',integer_factor='X-2',trace_degree=1,
                 components=[2,2,2],image=pack((2,2,2)))]
    for n in ns:
        for q in qs:
            values=[table[q][(n-1)//2] for table in kernels]
            a,b=q_parameters[q]
            images.append(dict(kind='rectangle',n=n,q=q,q_residue=q%480,a=a,b=b,
                               trace_degree=q*(n-1)//2,components=values,image=pack(values)))
    assert len(images)==4192
    hs=[r['image'] for r in images]
    assert gpower(hs[0],480)==ONE and all(gpower(hs[0],480//p)!=ONE for p in (2,3,5))
    for value in hs:
        assert gpower(value,480)==ONE

    assert len(old['generators'])==4192 and old['subgroup_order']==45*(1<<85)
    old_mod=rawpower(F,14)
    for current,previous in zip(images,old['generators']):
        assert {k:v for k,v in current.items() if k not in ('image','components')}=={
            k:v for k,v in previous.items() if k not in ('image','components')}
        a,b,c=current['components']
        assert [remainder(a,old_mod),b,c]==previous['components']
    projection=dict(old_certificate='endpoint_full_triple_image.json',generators_checked=4192,
                    old_subgroup_order=old['subgroup_order'],old_principal_rank=old['principal_rank'])
    
    # Actual odd part: BOTH residue coordinates, not an assumed cyclic group.
    log15={power(2,j,F):j for j in range(15)}
    log3={power(2,j,P):j for j in range(3)}
    tau15,tau3=power(2,16,MODS[0]),power(2,16,MODS[2])
    def oddpair(value):
        a,b,c=unpack(value)
        assert remainder(b,3)==1
        return log15[remainder(a,F)],log3[remainder(c,P)]
    def oddvalue(pair):
        return pack((power(tau15,pair[0],MODS[0]),1,power(tau3,pair[1],MODS[2])))
    pairs=[oddpair(h) for h in hs]
    representatives={}
    for i,pair in enumerate(pairs):
        representatives.setdefault(pair,i)
        assert gpower(hs[i],256)==oddvalue(pair)
    odd_words={(0,0):{}}
    odd_queue=deque([(0,0)])
    while odd_queue:
        pair=odd_queue.popleft()
        for generator,i in representatives.items():
            result=((pair[0]+generator[0])%15,(pair[1]+generator[1])%3)
            if result not in odd_words:
                odd_words[result]=addword(odd_words[pair],{i:256})
                odd_queue.append(result)
    assert len(odd_words)<=45

    def word_product(word):
        value=ONE
        for i,e in word.items():
            value=gmultiply(value,gpower(hs[i],e))
        return value
    for pair,word in odd_words.items():
        assert word_product(word)==oddvalue(pair)

    # Lazy sparse word collection avoids dense4192-coordinate work on reductions.
    pivots={}
    queue=deque((gpower(h,225),{i:225}) for i,h in enumerate(hs))
    while queue:
        value,seed=queue.popleft()
        used=[]
        while value!=ONE:
            position=leading(value)
            if position not in pivots:
                word=seed
                for pos in used:
                    word=addword(word,pivots[pos]['word'],-1)
                assert oddpair(value)==(0,0) and word_product(word)==value
                pivots[position]=dict(position=position,element=value,word=word,inverse=ginverse(value))
                squared={i:(2*e)%480 for i,e in word.items() if (2*e)%480}
                queue.append((gmultiply(value,value),squared))
                break
            value=gmultiply(value,pivots[position]['inverse'])
            used.append(position)
            assert value==ONE or leading(value)>position
    assert len(pivots)<=105

    def reduce(value):
        used=[]
        while value!=ONE:
            pos=leading(value)
            if pos not in pivots:
                break
            value=gmultiply(value,pivots[pos]['inverse'])
            used.append(pos)
            assert value==ONE or leading(value)>pos
        return dict(remainder=value,components=list(unpack(value)),used_positions=used,
                    first_missing_position=leading(value))
    generator_reductions=[]
    for h in hs:
        record=reduce(gpower(h,225))
        assert record['remainder']==ONE
        generator_reductions.append(record)
    basis=[]
    for pos,pivot in sorted(pivots.items()):
        square=reduce(gmultiply(pivot['element'],pivot['element']))
        assert square['remainder']==ONE and all(j>pos for j in square['used_positions'])
        basis.append(dict(position=pos,element=pivot['element'],components=list(unpack(pivot['element'])),
                          word=encoded(pivot['word']),square_reduction=square))


    decisions=[]
    for target in targets:
        value=pack(target['components'])
        assert gpower(value,2)==ONE
        pair=oddpair(value)
        reduced=reduce(gpower(value,225))
        normalization={}
        for pos in reduced['used_positions']:
            normalization=addword(normalization,pivots[pos]['word'])
        assert gmultiply(word_product(normalization),reduced['remainder'])==gpower(value,225)
        member=pair in odd_words and reduced['remainder']==ONE
        word=None;costs=None
        if member:
            word=addword(odd_words[pair],normalization)
            assert word_product(word)==value
            endpoint=word.get(0,0)
            degree=sum(e*images[i]['trace_degree'] for i,e in word.items())
            assert endpoint%2==0
            costs=dict(endpoint_exponent=endpoint,nonzero_terms=len(word),kernel_trace_degree=degree,
                       kernel_reciprocal_degree=2*degree,
                       resulting_T_trace_degree_not_tested=3390998+degree,
                       resulting_T_reciprocal_degree_not_tested=2*(3390998+degree))
        decisions.append(dict(h=target['h'],target=value,components=target['components'],
            odd_pair=list(pair),odd_member=pair in odd_words,principal_reduction=reduced,
            normalization_word=encoded(normalization),target_member=member,
            word=encoded(word) if member else None,word_costs=costs))
    assert len(decisions)==256
    attained=[r for r in decisions if r['target_member']]
    size=len(odd_words)*(1<<len(basis))
    assert size%old['subgroup_order']==0
    assert len(attained)==size//old['subgroup_order']
    hs_attained={r['h'] for r in attained}
    assert 0 in hs_attained and all(a^b in hs_attained for a in hs_attained for b in hs_attained)
    row=decisions[desired_h]
    chosen=None
    if row['target_member']:
        counts={};terms=[]
        for index,exponent in row['word']:
            label=images[index]
            terms.append({k:label[k] for k in ('kind','n','q','a','b','trace_degree') if k in label}
                |dict(index=index,exponent=exponent,degree_contribution=exponent*label['trace_degree']))
            if index:
                for r in range(2,label['n']+1):
                    if label['n']%r==0:
                        for i in range(label['a']+1):
                            for j in range(label['b']+1):
                                order=r*3**i*5**j
                                counts[order]=counts.get(order,0)+exponent
        endpoint=dict(row['word']).get(0,0)
        degree=endpoint+sum(e*totient(n)//2 for n,e in counts.items())
        assert degree==row['word_costs']['kernel_trace_degree']
        reciprocal={**counts}
        if endpoint: reciprocal[1]=2*endpoint
        assert sum(e*totient(n) for n,e in reciprocal.items())==2*degree
        chosen=dict(required_h=desired_h,target=row['components'],word=row['word'],terms=terms,
            costs=row['word_costs'],actual_endpoint_factor='X-2',endpoint_trace_multiplicity=endpoint,
            trace_factor_multiplicities=[dict(order=n,multiplicity=e) for n,e in sorted(counts.items())],
            reciprocal_cyclotomic_multiplicities=[dict(order=n,multiplicity=e) for n,e in sorted(reciprocal.items())],
            old_selected_word='inputs/endpoint_full_triple_positive_word.json',
            certifies_only_augmented_kernel_target=True,no_product_residual_probe=True,
            no_full_integer_word_expansion=True,no_other_word_optimization=True)
    payload=dict(scope='EXACT4192 actual Xi16 labels and ALL256 eight-bit kernel targets; no product residual probe',
        mod8_required_inputs=['endpoint_word_mod8.json','endpoint_word_mod8_verification.json'],
        old_image_required_input='endpoint_full_triple_image.json',
        generator_count=4192,q_representatives=qs,n_representatives=ns,
        moduli=list(MODS),component_degrees=[64,24,24],component_primary_primes=[F,3,P],
        group_exponent=480,identity=ONE,packing='bits0..63 R16;64..87 source3;88..111 source5',
        generators=images,odd_generator_pairs=[list(p) for p in pairs],
        odd_subgroup=[dict(pair=list(p),image=oddvalue(p),word=encoded(w)) for p,w in sorted(odd_words.items())],
        principal_basis=basis,generator_principal_reductions=generator_reductions,
        principal_rank=len(basis),odd_subgroup_order=len(odd_words),subgroup_order=size,
        old_projection=projection,computed_old_word_data=actual_data,
        target_decisions=decisions,attained_target_count=len(attained),attained_h=sorted(hs_attained),
        desired_h=desired_h,desired_target_attained=row['target_member'],selected_kernel_word=chosen,
        all256_targets_tested=True,author_self_check=True,independent_review=False,
        no_product_residual_probe=True,no_full_integer_word_expansion=True,no_other_word_optimization=True)
    output.mkdir(parents=True,exist_ok=True)
    temporary=output/'augmented_endpoint_kernel_image.json.partial'
    temporary.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    temporary.replace(output/'augmented_endpoint_kernel_image.json')
    print(json.dumps({k:payload[k] for k in ('generator_count','principal_rank','odd_subgroup_order',
        'subgroup_order','attained_target_count','desired_h','desired_target_attained')}
        |dict(selected_kernel_costs=(chosen['costs'] if chosen else None),recomputed_data={
            k:actual_data[k] for k in ('normalized_quarter_mod_f4','unique_square_root_mod_f2',
                'gamma_Q_mod_f2','delta16_mod_f2','denominator_mod_f2','required_h')})))


if __name__=='__main__':
    main()
