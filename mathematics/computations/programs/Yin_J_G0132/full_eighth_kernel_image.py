"""Complete4193 joint labels, ALL6310 kernel relations and ONE full F8 target.

Author producer. Actual positive words use joint exponent960, never480.
No new original-residual probe or high-degree polynomial expansion occurs.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
import json
import augmented_endpoint_kernel_image as xi
from first_gate_character import rawmul, remainder, multiply, power, inverse

F=25
F28=xi.rawpower(F,28)
F32=xi.rawpower(F,32)
MASK128=(1<<128)-1
JOINT_EXPONENT=960


@lru_cache(maxsize=4096)
def spread_binary(value):
    return int.from_bytes(bytes((value>>i)&1 for i in range(128)), 'little')


class MixedRing:
    """Exact B normal form L+2H; binary deg L<128 and deg H<112."""
    one=(1,0)

    @staticmethod
    def normalize(low,high):
        # Actual V modulo4 is X128+X96+2X64+1.
        while (low|high)>>128:
            ql,qh=low>>128,high>>128
            low&=MASK128;high&=MASK128
            for shift in (0,96):
                nl=ql<<shift
                nh=(qh^ql)<<shift
                high^=nh^(low&nl)
                low^=nl
            high^=ql<<64
        return low,remainder(high,F28)

    def add(self,a,b):
        return self.normalize(a[0]^b[0],a[1]^b[1]^(a[0]&b[0]))

    def negative(self,a):
        return self.normalize(a[0],a[1]^a[0])

    def from_coefficients(self,values):
        low=sum((v&1)<<i for i,v in enumerate(values))
        high=sum(((v%4)>>1)<<i for i,v in enumerate(values))
        return self.normalize(low,high)

    def multiply(self,a,b):
        if a==self.one:return b
        if b==self.one:return a
        if a==(0,0) or b==(0,0):return (0,0)
        digits=(spread_binary(a[0])*spread_binary(b[0])).to_bytes(255,'little')
        low=sum((v&1)<<i for i,v in enumerate(digits))
        high=sum(((v>>1)&1)<<i for i,v in enumerate(digits))
        high^=rawmul(a[0],b[1])^rawmul(a[1],b[0])
        return self.normalize(low,high)

    def power(self,a,n):
        result=self.one
        while n:
            if n&1:result=self.multiply(result,a)
            n//=2
            if n:a=self.multiply(a,a)
        return result

    def inverse(self,a):
        seed=(inverse(a[0],F32),0)
        error=self.multiply(a,seed)
        assert error[0]==1
        result=self.multiply(seed,(1,error[1]))
        assert self.multiply(a,result)==self.one
        return result


def add_word(first,second,scale=1):
    result=dict(first)
    for i,e in second.items():
        value=(result.get(i,0)+scale*e)%JOINT_EXPONENT
        if value:result[i]=value
        else:result.pop(i,None)
    return result


def encode_word(word):
    return [[i,e] for i,e in sorted(word.items())]


def word_costs(word,labels):
    counts=Counter();endpoint=0;terms=[]
    for i,e in sorted(word.items()):
        label=labels[i]
        assert 0<e<960
        terms.append({k:label[k] for k in ('kind','n','q','a','b','trace_degree') if k in label}
                     |dict(index=i,exponent=e,degree_contribution=e*label['trace_degree']))
        if label['kind']=='endpoint':endpoint+=e
        else:
            for r in range(2,label['n']+1):
                if label['n']%r==0:
                    for a in range(label['a']+1):
                        for b in range(label['b']+1):counts[r*3**a*5**b]+=e
    degree=sum(t['degree_contribution'] for t in terms)
    assert degree==endpoint+sum(e*xi.totient(n)//2 for n,e in counts.items())
    reciprocal=dict(counts)
    if endpoint:reciprocal[1]=2*endpoint
    assert 2*degree==sum(e*xi.totient(n) for n,e in reciprocal.items())
    return dict(terms=terms,endpoint_exponent=endpoint,nonzero_terms=len(word),
                kernel_trace_degree=degree,kernel_reciprocal_degree=2*degree,
                resulting_T_trace_degree_not_tested=6520358+degree,
                resulting_T_reciprocal_degree_not_tested=2*(6520358+degree),
                complete_trace_factors=[dict(order=n,multiplicity=e) for n,e in sorted(counts.items())],
                complete_reciprocal_factors=[dict(order=n,multiplicity=e) for n,e in sorted(reciprocal.items())])


def actual_target(output):
    source=json.loads((output/'endpoint_kernel_product_mod8.json').read_text(encoding='utf-8'))
    check=json.loads((output/'endpoint_kernel_product_mod8_verification.json').read_text(encoding='utf-8'))
    assert source['original_restrictions_mod8']==check['original_restrictions_mod8']
    assert source['full_trace_degree']==6520358 and source['lowest_quarter_mod_f8_cancelled']
    rows=source['original_restrictions_mod8']
    assert all(v%4==0 for v in rows['F'])
    quarter=xi.binary([v//4 for v in rows['F']])
    numerator,zero=xi.divide(quarter,xi.rawpower(F,8))
    assert zero==0
    numerator=remainder(numerator,F28)
    cb=xi.binary(rows['c'])
    gamma,zero=xi.divide(cb,xi.rawpower(F,4))
    assert zero==0
    gamma=remainder(gamma,F28)
    gamma2=multiply(gamma,gamma,F28)
    target=multiply(numerator,inverse(gamma2,F28),F28)
    return dict(source_result='endpoint_kernel_product_mod8.json',
                source_verification='endpoint_kernel_product_mod8_verification.json',
                c_binary=cb,quarter_binary=quarter,quarter_div_f8=numerator,
                gamma_mod_f28=gamma,gamma_squared_mod_f28=gamma2,target=target)


def main():
    here=Path(__file__).resolve().parent
    output=here.parents[3]/'mathematics/computations/outputs'/here.name
    quotient=json.loads((output/'augmented_endpoint_kernel_image.json').read_text(encoding='utf-8'))
    old_product=json.loads((output/'endpoint_kernel_product_mod8.json').read_text(encoding='utf-8'))
    assert quotient['generator_count']==4192 and quotient['principal_rank']==92
    assert quotient['odd_subgroup_order']==45 and quotient['subgroup_order']==45*(1<<92)
    target_data=actual_target(output)
    actual_v=xi.idivide(old_product['J_coefficients'],xi.ipower([1,4,-4,-1,1],4))
    v4=[v%4 for v in actual_v];expected=[0]*129
    for i,c in ((0,1),(64,2),(96,1),(128,1)):expected[i]=c
    assert v4==expected
    ring=MixedRing()
    labels=[]
    for row in quotient['generators']:
        labels.append({k:v for k,v in row.items() if k not in ('image','components')}
                      |dict(xi_image=row['image'],xi_components=row['components']))
    shift=xi.gpower(labels[0]['xi_image'],240)
    labels.append(dict(kind='rectangle',n=481,q=1,q_residue=1,a=0,b=0,trace_degree=240,
                       xi_image=shift,xi_components=list(xi.unpack(shift))))
    assert len(labels)==4193
    cheb=[(0,1),(2,0)]
    for _ in range(2,960):
        cheb.append(ring.add(ring.multiply((2,0),cheb[-1]),ring.negative(cheb[-2])))
    tables={}
    for q in quotient['q_representatives']:
        for p in (2,5):
            argument=cheb[(p*q)%960]
            previous,current=(0,1),argument
            values=[ring.one]
            for _ in range(1,241):
                values.append(ring.add(values[-1],current))
                previous,current=current,ring.add(ring.multiply(argument,current),ring.negative(previous))
            tables[(q,p)]=values
    print('mixed characteristic kernels prepared',flush=True)
    omegas=[]
    for i,label in enumerate(labels):
        if i==0:
            w2=ring.add(cheb[2],(0,1));w5=ring.add(cheb[5],(0,1))
        else:
            w2=tables[(label['q'],2)][(label['n']-1)//2]
            w5=tables[(label['q'],5)][(label['n']-1)//2]
        omega=ring.multiply(ring.power(w5,2),ring.power(ring.inverse(w2),5))
        assert ring.power(omega,960)==ring.one
        label.update(weight_C2=list(w2),weight_C5=list(w5),omega=list(omega))
        omegas.append(omega)
    assert omegas[-1]==ring.one
    print('all4193 mixed characteristic joint images complete',flush=True)
    powers={}
    def omega_word(word):
        value=ring.one
        for i,e in sorted(word.items()):
            if i not in powers:
                values=[omegas[i]]
                for _ in range(9):values.append(ring.multiply(values[-1],values[-1]))
                powers[i]=values
            for j in range(10):
                if e>>j&1:value=ring.multiply(value,powers[i][j])
        return value
    def xi_word(word):
        value=xi.ONE
        for i,e in word.items():value=xi.gmultiply(value,xi.gpower(labels[i]['xi_image'],e))
        return value
    odd={}
    for row in quotient['odd_subgroup']:
        pair=tuple(row['pair']);word=dict(row['word'])
        assert xi_word(word)==row['image']
        odd[pair]=dict(pair=list(pair),xi_image=row['image'],omega=list(omega_word(word)),word=encode_word(word))
    assert odd[(0,0)]['word']==[]
    pivots={}
    for row in quotient['principal_basis']:
        word=dict(row['word']);assert xi_word(word)==row['element']
        pivots[row['position']]=dict(position=row['position'],xi_image=row['element'],
            omega=list(omega_word(word)),word=encode_word(word),
            later_square_positions=row['square_reduction']['used_positions'])
    print('all45 odd and92 principal actual lifts complete',flush=True)
    inv_pivots={pos:xi.ginverse(v['xi_image']) for pos,v in pivots.items()}
    log15={power(2,j,F):j for j in range(15)}
    log3={power(2,j,7):j for j in range(3)}
    def section(value):
        a,b,c=xi.unpack(value)
        pair=(log15[remainder(a,F)],log3[remainder(c,7)])
        work=xi.gpower(value,225);used=[]
        while work!=xi.ONE:
            pos=xi.leading(work);assert pos in pivots
            work=xi.gmultiply(work,inv_pivots[pos]);used.append(pos)
            assert work==xi.ONE or xi.leading(work)>pos
        word=dict(odd[pair]['word']);mixed=tuple(odd[pair]['omega'])
        for pos in used:
            word=add_word(word,dict(pivots[pos]['word']))
            mixed=ring.multiply(mixed,tuple(pivots[pos]['omega']))
        return pair,used,word,mixed
    relations=[];relation_words=[]
    def retain_relation(recipe,word,mixed,projected):
        assert projected==xi.ONE and mixed[0]==1
        vector=mixed[1];assert vector.bit_length()<=112
        relations.append(dict(index=len(relations),recipe=recipe,omega=list(mixed),vector=vector))
        relation_words.append(word)
    for i,label in enumerate(labels):
        pair,positions,word,mixed=section(label['xi_image'])
        relation_word=add_word({i:1},word,-1)
        result=ring.multiply(omegas[i],ring.inverse(mixed))
        projected=xi.gmultiply(label['xi_image'],xi.ginverse(odd[pair]['xi_image']))
        for pos in positions:projected=xi.gmultiply(projected,inv_pivots[pos])
        retain_relation(dict(kind='generator',generator=i,odd_pair=list(pair),positions=positions),relation_word,result,projected)
    for pos,pivot in sorted(pivots.items()):
        word=add_word({},dict(pivot['word']),2)
        mixed=ring.power(tuple(pivot['omega']),2);projected=xi.gpower(pivot['xi_image'],2)
        for later in pivot['later_square_positions']:
            assert later>pos
            word=add_word(word,dict(pivots[later]['word']),-1)
            mixed=ring.multiply(mixed,ring.inverse(tuple(pivots[later]['omega'])))
            projected=xi.gmultiply(projected,inv_pivots[later])
        retain_relation(dict(kind='square',position=pos,later_positions=pivot['later_square_positions']),word,mixed,projected)
    for a,oa in sorted(odd.items()):
        for b,ob in sorted(odd.items()):
            c=((a[0]+b[0])%15,(a[1]+b[1])%3);oc=odd[c]
            word=add_word(dict(oa['word']),dict(ob['word']))
            word=add_word(word,dict(oc['word']),-1)
            mixed=ring.multiply(ring.multiply(tuple(oa['omega']),tuple(ob['omega'])),ring.inverse(tuple(oc['omega'])))
            projected=xi.gmultiply(xi.gmultiply(oa['xi_image'],ob['xi_image']),xi.ginverse(oc['xi_image']))
            retain_relation(dict(kind='odd',a=list(a),b=list(b),c=list(c)),word,mixed,projected)
    assert len(relations)==4193+92+2025==6310
    print('all6310 relation identities complete',flush=True)
    basis={}
    for relation,seed_word in zip(relations,relation_words):
        value=relation['vector'];used=[]
        while value:
            pos=(value&-value).bit_length()-1
            if pos not in basis:
                word=dict(seed_word)
                for oldpos in used:word=add_word(word,dict(basis[oldpos]['word']))
                assert xi_word(word)==xi.ONE and omega_word(word)==(1,value)
                basis[pos]=dict(position=pos,vector=value,seed_relation=relation['index'],
                    construction_positions=used,word=encode_word(word),costs=word_costs(word,labels))
                break
            value^=basis[pos]['vector'];used.append(pos)
            assert not value or (value&-value).bit_length()-1>pos
    assert len(basis)<=112
    def linear_reduce(value):
        used=[]
        while value:
            pos=(value&-value).bit_length()-1
            if pos not in basis:break
            value^=basis[pos]['vector'];used.append(pos)
            assert not value or (value&-value).bit_length()-1>pos
        return dict(remainder=value,used_positions=used,
                    first_missing_position=((value&-value).bit_length()-1 if value else None))
    for relation in relations:
        reduced=linear_reduce(relation['vector'])
        assert reduced['remainder']==0
        relation['linear_reduction']=reduced
    target=target_data['target'];reduced=linear_reduce(target)
    normalized_word={}
    for pos in reduced['used_positions']:
        normalized_word=add_word(normalized_word,dict(basis[pos]['word']))
    normalized_vector=target^reduced['remainder']
    assert xi_word(normalized_word)==xi.ONE
    assert omega_word(normalized_word)==(1,normalized_vector)
    member=reduced['remainder']==0
    decision=dict(target=target,reduction=reduced,target_member=member,
        normalization_word=encode_word(normalized_word),normalization_vector=normalized_vector,
        word=(encode_word(normalized_word) if member else None),
        costs=(word_costs(normalized_word,labels) if member else None))
    payload=dict(scope='EXACT4193 actual joint labels, ALL6310 relations, ONE full112-bit original-quarter target',
        quotient_required_input='augmented_endpoint_kernel_image.json',
        target_required_inputs=['endpoint_kernel_product_mod8.json','endpoint_kernel_product_mod8_verification.json'],
        actual_V_coefficients=actual_v,V_coefficients_mod4=v4,
        mixed_normal_form='L+2H, binary degL<128,degH<112; represented as [L,H]',
        high_modulus=F28,binary_V_modulus=F32,joint_exponent=960,
        generator_count=len(labels),generators=labels,
        odd_lifts=[odd[k] for k in sorted(odd)],principal_lifts=[pivots[k] for k in sorted(pivots)],
        relation_counts={'generator':4193,'square':92,'odd':2025},relations=relations,
        additive_basis=[basis[k] for k in sorted(basis)],additive_rank=len(basis),
        quotient_image_order=quotient['subgroup_order'],joint_image_order=quotient['subgroup_order']*(1<<len(basis)),
        target_data=target_data,target_decision=decision,
        all6310_relations_complete_before_target=True,all_relation_reductions_zero=True,
        all_basis_positive_words_and_costs_checked=True,
        author_self_check=True,independent_review=False,no_new_original_residual_probe=True,
        no_other_target_or_profile=True,no_word_optimization=True,no_full_large_polynomial_expansion=True)
    output.mkdir(parents=True,exist_ok=True)
    temporary=output/'full_eighth_kernel_image.json.partial'
    temporary.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    temporary.replace(output/'full_eighth_kernel_image.json')
    print(json.dumps(dict(generator_count=len(labels),relation_count=len(relations),
        additive_rank=len(basis),target=target,target_member=member,
        target_remainder=reduced['remainder'],joint_image_order=payload['joint_image_order'],
        positive_word_costs=(None if not member else {k:v for k,v in decision['costs'].items()
            if k not in ('terms','complete_trace_factors','complete_reciprocal_factors')}))),flush=True)


if __name__=='__main__':
    main()

