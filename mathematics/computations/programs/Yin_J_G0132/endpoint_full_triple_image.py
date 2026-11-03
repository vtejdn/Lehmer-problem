"""Complete4192-label endpoint/rectangle Xi-image and ALL64 fixed targets.

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
MASK56, MASK24 = (1<<56)-1, (1<<24)-1


def rawpower(a,n):
    out=1
    for _ in range(n):
        out=rawmul(out,a)
    return out


MODS=(rawpower(F,14),rawpower(3,24),rawpower(P,12))


def unpack(value):
    return value & MASK56,(value>>56)&MASK24,value>>80


def pack(values):
    a,b,c=values
    return a | (b<<56) | (c<<80)


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
            unpack(value),(F,3,P),(4,1,2),(14,24,12),(0,52,75))):
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


def main():
    here=Path(__file__).resolve().parent
    output=here.parents[3]/'mathematics/computations/outputs'/here.name
    target_path=output/'local_source_jet_enumeration.json'
    data=json.loads(target_path.read_text(encoding='utf-8'))
    assert data['pair_count']==10240 and data['survivor_count']==64 and data['image_rank']==24
    targets=data['surviving_local_triples']
    assert len(targets)==64 and len({(r['source_mask'],r['branch']) for r in targets})==64
    assert all(r['branch']==2 and r['passes'] for r in targets)
    assert data['actual_base']['K']==19232663035708480
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
    assert len(pivots)<=97

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
        value=pack([target['Q15'],target['Q3_source'],target['Q5_source']])
        pair=oddpair(value)
        reduced=reduce(gpower(value,225))
        normalization={}
        for pos in reduced['used_positions']:
            normalization=addword(normalization,pivots[pos]['word'])
        assert gmultiply(word_product(normalization),reduced['remainder'])==gpower(value,225)
        member=pair in odd_words and reduced['remainder']==ONE
        word=None
        summary=None
        if member:
            word=addword(odd_words[pair],normalization)
            assert word_product(word)==value
            endpoint=word.get(0,0)
            degree=sum(e*images[i]['trace_degree'] for i,e in word.items())
            assert endpoint%2==1, 'Adopted high-character necessity requires an odd endpoint'
            summary=dict(endpoint_exponent=endpoint,nonzero_terms=len(word),cofactor_trace_degree=degree,
                         original_trace_degree=374+degree,original_reciprocal_degree=2*(374+degree))
        decisions.append(dict(source_mask=target['source_mask'],branch=target['branch'],
                              target=value,components=list(unpack(value)),odd_pair=list(pair),
                              odd_member=pair in odd_words,principal_reduction=reduced,
                              normalization_word=encoded(normalization),target_member=member,
                              word=(encoded(word) if member else None),word_costs=summary))
    assert len(decisions)==64
    attained=[r for r in decisions if r['target_member']]
    chosen=None
    if attained:
        # Choose among already recovered certificates, not an additional word search.
        row=min(attained,key=lambda r:(r['word_costs']['original_trace_degree'],r['source_mask']))
        word=dict(row['word'])
        counts={3:4,5:6,9:8,11:2,15:4,17:2,187:2,960:1}
        terms=[]
        for index,exponent in row['word']:
            label=images[index]
            terms.append({k:label[k] for k in ('kind','n','q','a','b','trace_degree') if k in label}
                         | dict(index=index,exponent=exponent,degree_contribution=exponent*label['trace_degree']))
            if index==0:
                continue
            for r in range(2,label['n']+1):
                if label['n']%r==0:
                    for i in range(label['a']+1):
                        for j in range(label['b']+1):
                            order=r*3**i*5**j
                            counts[order]=counts.get(order,0)+exponent
        endpoint=word.get(0,0)
        full_degree=4+endpoint+sum(e*totient(n)//2 for n,e in counts.items())
        assert full_degree==row['word_costs']['original_trace_degree']
        reciprocal={1:2*(4+endpoint),**counts}
        assert sum(e*totient(n) for n,e in reciprocal.items())==2*full_degree
        chosen=dict(source_mask=row['source_mask'],branch=row['branch'],target=row['components'],
                    terms=terms,word=row['word'],costs=row['word_costs'],
                    full_trace_factor_multiplicities=[dict(order=n,multiplicity=e) for n,e in sorted(counts.items())],
                    full_endpoint_trace_multiplicity=4+endpoint,
                    full_reciprocal_cyclotomic_multiplicities=[dict(order=n,multiplicity=e) for n,e in sorted(reciprocal.items())],
                    maximal_global_binary_Frobenius_exponent=1,
                    no_original_mod4_residual_probe=True,no_full_integer_word_expansion=True)
    payload=dict(scope='EXACT4192 endpoint/rectangle labels and all64 adoptedC861 local targets; full Xi data only',
                 target_input='mathematics/computations/outputs/Yin_J_G0132/local_source_jet_enumeration.json',
                 generator_count=4192,q_representatives=qs,n_representatives=ns,
                 moduli=list(MODS),component_degrees=[56,24,24],component_primary_primes=[F,3,P],
                 group_exponent=480,identity=ONE,
                 packing='bits0..55 R14;56..79 source3;80..103 source5; each coefficient is F2',
                 generators=images,
                 odd_generator_pairs=[list(p) for p in pairs],
                 odd_subgroup=[dict(pair=list(p),image=oddvalue(p),word=encoded(w)) for p,w in sorted(odd_words.items())],
                 principal_basis=basis,generator_principal_reductions=generator_reductions,
                 principal_rank=len(basis),odd_subgroup_order=len(odd_words),
                 subgroup_order=len(odd_words)*(1<<len(basis)),target_decisions=decisions,
                 attained_target_count=len(attained),selected_positive_word=chosen,
                 all64_targets_tested=True,no_candidate_enumeration=True,
                 no_original_mod4_residual_probe=True,no_full_integer_word_expansion=True,
                 author_self_check=True,independent_review=False)
    output.mkdir(parents=True,exist_ok=True)
    tmp=output/'endpoint_full_triple_image.json.partial'
    tmp.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    tmp.replace(output/'endpoint_full_triple_image.json')
    print(json.dumps({k:payload[k] for k in ('generator_count','principal_rank','odd_subgroup_order','subgroup_order','attained_target_count')}
                     | dict(selected_costs=(chosen['costs'] if chosen else None))))


if __name__=='__main__':
    main()
