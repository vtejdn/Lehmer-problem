"""Different AUTHOR verification of ALL4192 triples and ALL64 decisions.

Images are rebuilt in three faithful Laurent rings.  Group arithmetic uses
carry-free integer convolution, not the producer's binary shift multiplier.
No producer helpers or discovery algorithm are imported.
"""
from pathlib import Path
from collections import Counter
from math import gcd
import json
import sympy as sp

z=sp.symbols('z')


def bits(poly):
    return sum((int(poly.nth(i))%2)<<i for i in range(poly.degree()+1)) if not poly.is_zero else 0


class Ring:
    def __init__(self,modulus):
        self.modulus=modulus
        self.degree=modulus.bit_length()-1
        assert self.degree<256

    def reduce(self,value):
        while value.bit_length()>self.degree:
            value ^= self.modulus << (value.bit_length()-self.degree-1)
        return value

    def multiply(self,a,b):
        if a==0 or b==0:
            return 0
        if a==1:
            return b
        if b==1:
            return a
        # Base256 exceeds every binary convolution coefficient (degree<=112).
        aa=int.from_bytes(bytes((a>>i)&1 for i in range(self.degree)),'little')
        bb=int.from_bytes(bytes((b>>i)&1 for i in range(self.degree)),'little')
        digits=(aa*bb).to_bytes(2*self.degree-1,'little')
        raw=sum((v&1)<<i for i,v in enumerate(digits))
        return self.reduce(raw)

    def power(self,a,n):
        result=1
        while n:
            if n&1:
                result=self.multiply(result,a)
            n//=2
            if n:
                a=self.multiply(a,a)
        return result


def division(a,b):
    quotient=0
    while a and a.bit_length()>=b.bit_length():
        j=a.bit_length()-b.bit_length()
        quotient ^= 1<<j
        a ^= b<<j
    return quotient,a


def pack(value):
    a,b,c=value
    assert a.bit_length()<=56 and b.bit_length()<=24 and c.bit_length()<=24
    return a | (b<<56) | (c<<80)


def unpack(value):
    return value&((1<<56)-1),(value>>56)&((1<<24)-1),value>>80


def main():
    here=Path(__file__).resolve().parent
    output=here.parents[3]/'mathematics/computations/outputs'/here.name
    saved=json.loads((output/'endpoint_full_triple_image.json').read_text(encoding='utf-8'))
    target_data=json.loads((output/'local_source_jet_enumeration.json').read_text(encoding='utf-8'))
    assert target_data['survivor_count']==64 and target_data['pair_count']==10240
    target_rows=target_data['surviving_local_triples']
    assert len(target_rows)==64 and all(r['branch']==2 and r['passes'] for r in target_rows)
    polynomials=[sp.Poly((z**4+z**3+1)**14,z,modulus=2),
                 sp.Poly((z+1)**24,z,modulus=2),sp.Poly((z**2+z+1)**12,z,modulus=2)]
    rings=[Ring(bits(p)) for p in polynomials]
    assert [r.modulus for r in rings]==saved['moduli']
    assert [r.degree for r in rings]==saved['component_degrees']==[56,24,24]
    identity=(1,1,1)
    assert pack(identity)==saved['identity'] and saved['group_exponent']==480
    def gmultiply(a,b):
        return tuple(r.multiply(x,y) for r,x,y in zip(rings,a,b))
    def gpower(a,n):
        return tuple(r.power(x,n) for r,x in zip(rings,a))
    def ginverse(a):
        return tuple(r.power(x,e-1) for r,x,e in zip(rings,a,(240,32,48)))

    # Rebuild the complete actual parameter list by the proved elementary minima.
    mixed={}
    for a in range(1,9):
        for b in range(1,9):
            q=3**a*5**b
            residue=q%480
            mixed[residue]=min(q,mixed.get(residue,q))
    assert len(mixed)==16
    qs=sorted({1,*[3**i for i in range(1,9)],*[5**i for i in range(1,9)],*mixed.values()})
    ns=[n for n in range(2,480) if gcd(n,480)==1]
    assert qs==saved['q_representatives'] and ns==saved['n_representatives']
    assert len(qs)==33 and sum(qs)==539881 and len(ns)==127
    assert sum((n-1)//2 for n in ns)==15296

    # Independent centered Laurent reconstruction at EACH full source precision.
    recoverers=[]
    for order,multiplicity,period,target_ring in zip((15,3,5),(14,24,12),(240,96,80),rings):
        cyclo=sp.Poly(sp.cyclotomic_poly(order,z),z,modulus=2)**multiplicity
        lr=Ring(bits(cyclo))
        d=target_ring.degree
        assert lr.degree==2*d
        powers=[1]
        for _ in range(period):
            powers.append(lr.multiply(powers[-1],2))
        assert powers[period]==1
        trace=powers[1]^powers[-2]
        tp=[1]
        for _ in range(d-1):
            tp.append(lr.multiply(tp[-1],trace))
        shifted=[lr.multiply(powers[d-1],v) for v in tp]
        def recover(value,lr=lr,d=d,powers=powers,shifted=shifted):
            work=lr.multiply(powers[d-1],value)
            assert work.bit_length()<=2*d-1
            result=0
            for j in range(d-1,-1,-1):
                if work>>(d-1+j)&1:
                    result |= 1<<j
                    work ^= shifted[j]
            assert work==0
            return result
        assert recover(trace)==2
        cache={}
        def kernel(n,q,period=period,lr=lr,recover=recover,cache=cache):
            key=(n,q%period)
            if key not in cache:
                coefficient=0
                for j in range(-(n-1)//2,(n-1)//2+1):
                    coefficient ^= 1<<((q*j)%period)
                cache[key]=recover(lr.reduce(coefficient))
            return cache[key]
        recoverers.append(kernel)
    labels=saved['generators']
    assert len(labels)==saved['generator_count']==4192
    assert labels[0]==dict(kind='endpoint',integer_factor='X-2',trace_degree=1,components=[2,2,2],image=pack((2,2,2)))
    images=[(2,2,2)]
    index=1
    for n in ns:
        for q in qs:
            row=labels[index]
            factorization=sp.factorint(q)
            a,b=int(factorization.get(3,0)),int(factorization.get(5,0))
            assert q==3**a*5**b
            image=tuple(fn(n,q) for fn in recoverers)
            assert row==dict(kind='rectangle',n=n,q=q,q_residue=q%480,a=a,b=b,
                             trace_degree=q*(n-1)//2,components=list(image),image=pack(image))
            images.append(image)
            index+=1
    assert index==4192
    assert gpower(images[0],480)==identity
    assert all(gpower(images[0],480//p)!=identity for p in (2,3,5))
    for image in images:
        assert gpower(image,480)==identity

    def decode(word):
        assert word==sorted(word) and len({i for i,e in word})==len(word)
        assert all(0<=i<4192 and isinstance(e,int) and 0<e<480 for i,e in word)
        return word
    power_cache={}
    def word_product(word):
        result=identity
        for i,e in decode(word):
            if i not in power_cache:
                row=[images[i]]
                for _ in range(8):
                    row.append(gmultiply(row[-1],row[-1]))
                power_cache[i]=row
            for j in range(9):
                if e>>j&1:
                    result=gmultiply(result,power_cache[i][j])
        return result

    fields=Ring(25),Ring(7)
    log15={fields[0].power(2,j):j for j in range(15)}
    log3={fields[1].power(2,j):j for j in range(3)}
    assert len(log15)==15 and len(log3)==3
    def oddpair(value):
        assert Ring(3).reduce(value[1])==1
        return log15[fields[0].reduce(value[0])],log3[fields[1].reduce(value[2])]
    pairs=[oddpair(v) for v in images]
    assert [list(p) for p in pairs]==saved['odd_generator_pairs']
    odd={}
    for row in saved['odd_subgroup']:
        pair=tuple(row['pair'])
        assert pair not in odd and 0<=pair[0]<15 and 0<=pair[1]<3
        value=unpack(row['image'])
        assert value==word_product(row['word']) and oddpair(value)==pair
        assert gpower(value,15)==identity
        odd[pair]=value
    assert (0,0) in odd and odd[(0,0)]==identity
    for image,pair in zip(images,pairs):
        assert pair in odd and gpower(image,256)==odd[pair]
        assert gmultiply(gpower(image,256),gpower(image,225))==image
    for pair in odd:
        for g in set(pairs):
            assert ((pair[0]+g[0])%15,(pair[1]+g[1])%3) in odd

    def leading(value):
        if value==identity:
            return None
        for unit,prime,degree,length,offset in zip(value,(25,3,7),(4,1,2),(14,24,12),(0,52,75)):
            if unit==1:
                continue
            work,layer=unit^1,0
            while True:
                quotient,coefficient=division(work,prime)
                if coefficient:
                    break
                work,layer=quotient,layer+1
            assert 1<=layer<length
            bit=next(i for i in range(degree) if coefficient>>i&1)
            return offset+degree*(layer-1)+bit
        raise AssertionError('nonidentity has leading position')
    basis=saved['principal_basis']
    positions=[r['position'] for r in basis]
    assert positions==sorted(set(positions)) and len(positions)<=97
    pivots={}
    for row in basis:
        value=unpack(row['element'])
        assert list(value)==row['components'] and oddpair(value)==(0,0)
        assert leading(value)==row['position'] and word_product(row['word'])==value
        inv=ginverse(value)
        assert gmultiply(value,inv)==identity
        pivots[row['position']]=(value,inv)
    def reduce(value):
        used=[]
        while value!=identity:
            pos=leading(value)
            if pos not in pivots:
                break
            value=gmultiply(value,pivots[pos][1])
            used.append(pos)
            assert value==identity or leading(value)>pos
        return dict(remainder=pack(value),components=list(value),used_positions=used,first_missing_position=leading(value))
    assert len(saved['generator_principal_reductions'])==4192
    for image,record in zip(images,saved['generator_principal_reductions']):
        result=reduce(gpower(image,225))
        assert result==record and result['remainder']==pack(identity)
    for row in basis:
        value=unpack(row['element'])
        result=reduce(gmultiply(value,value))
        assert result==row['square_reduction'] and result['remainder']==pack(identity)
        assert all(p>row['position'] for p in result['used_positions'])
    assert saved['principal_rank']==len(basis) and saved['odd_subgroup_order']==len(odd)
    assert saved['subgroup_order']==len(odd)*(1<<len(basis))

    decisions=saved['target_decisions']
    assert len(decisions)==64
    checked=[]
    attained=[]
    for source,row in zip(target_rows,decisions):
        assert (row['source_mask'],row['branch'])==(source['source_mask'],source['branch'])
        target=source['Q15'],source['Q3_source'],source['Q5_source']
        assert pack(target)==row['target'] and list(target)==row['components']
        pair=oddpair(target)
        assert list(pair)==row['odd_pair'] and row['odd_member']==(pair in odd)
        result=reduce(gpower(target,225))
        assert result==row['principal_reduction']
        assert gmultiply(word_product(row['normalization_word']),unpack(result['remainder']))==gpower(target,225)
        member=pair in odd and result['remainder']==pack(identity)
        assert member==row['target_member']
        if member:
            word=decode(row['word'])
            assert word_product(word)==target
            endpoint=dict(word).get(0,0)
            degree=sum(e*labels[i]['trace_degree'] for i,e in word)
            assert row['word_costs']==dict(endpoint_exponent=endpoint,nonzero_terms=len(word),
                cofactor_trace_degree=degree,original_trace_degree=374+degree,original_reciprocal_degree=2*(374+degree))
            assert endpoint%2==1
            attained.append(row)
        else:
            assert row['word'] is None and row['word_costs'] is None
        checked.append(dict(source_mask=row['source_mask'],branch=row['branch'],target_member=member,
                            principal_remainder=result,positive_word_checked=member,word_costs=row['word_costs']))
    assert len(attained)==saved['attained_target_count']
    chosen=saved['selected_positive_word']
    if attained:
        best=min(attained,key=lambda r:(r['word_costs']['original_trace_degree'],r['source_mask']))
        assert chosen['source_mask']==best['source_mask'] and chosen['branch']==best['branch']
        assert chosen['word']==best['word'] and chosen['costs']==best['word_costs'] and chosen['target']==best['components']
        counts=Counter({3:4,5:6,9:8,11:2,15:4,17:2,187:2,960:1})
        terms=[]
        for index,exponent in decode(chosen['word']):
            label=labels[index]
            terms.append({k:label[k] for k in ('kind','n','q','a','b','trace_degree') if k in label}
                         | dict(index=index,exponent=exponent,degree_contribution=exponent*label['trace_degree']))
            if index:
                for r in sp.divisors(label['n'])[1:]:
                    for a in range(label['a']+1):
                        for b in range(label['b']+1):
                            counts[int(r)*3**a*5**b]+=exponent
        assert chosen['terms']==terms
        assert chosen['full_trace_factor_multiplicities']==[dict(order=n,multiplicity=e) for n,e in sorted(counts.items())]
        endpoint=4+dict(chosen['word']).get(0,0)
        assert chosen['full_endpoint_trace_multiplicity']==endpoint
        reciprocal={1:2*endpoint,**counts}
        assert chosen['full_reciprocal_cyclotomic_multiplicities']==[dict(order=n,multiplicity=e) for n,e in sorted(reciprocal.items())]
        degree=endpoint+sum(int(sp.totient(n))*e//2 for n,e in counts.items())
        assert degree==chosen['costs']['original_trace_degree']
        assert sum(int(sp.totient(n))*e for n,e in reciprocal.items())==2*degree
        assert endpoint%2==1 and chosen['maximal_global_binary_Frobenius_exponent']==1
    else:
        assert chosen is None
    result=dict(scope='ALL4192 actual endpoint/rectangle triples and ALL64 fixedC861 targets',
                faithful_Laurent_moduli=['Phi15^14','Phi3^24','Phi5^12'],
                Laurent_degrees=[112,48,48],Laurent_z_periods=[240,96,80],
                verified_generators=4192,verified_odd_generator_coordinates=4192,
                verified_odd_words=len(odd),actual_odd_subgroup_pairs=[list(p) for p in sorted(odd)],
                verified_pivot_words=len(basis),verified_later_square_relations=len(basis),
                verified_original_principal_reductions=4192,
                principal_rank=len(basis),principal_component_pivot_counts=[sum(a<=p<b for p in positions) for a,b in ((0,52),(52,75),(75,97))],
                odd_subgroup_order=len(odd),subgroup_order=len(odd)*(1<<len(basis)),
                target_decisions=checked,attained_target_count=len(attained),
                all64_target_normalforms_and_positive_words_checked=True,
                chosen_full_word_and_factor_costs_checked=bool(attained),
                chosen_word_costs=(chosen['costs'] if chosen else None),
                arithmetic='different faithful Laurent kernels and carry-free integer convolution; no producer imports',
                sympy_version=sp.__version__,author_self_check=True,independent_review=False,
                no_original_mod4_residual_probe=True,no_full_integer_word_expansion=True)
    tmp=output/'endpoint_full_triple_image_verification.json.partial'
    tmp.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    tmp.replace(output/'endpoint_full_triple_image_verification.json')
    print(json.dumps({k:result[k] for k in ('verified_generators','principal_rank','principal_component_pivot_counts',
                     'odd_subgroup_order','attained_target_count','chosen_word_costs')}))


if __name__=='__main__':
    main()
