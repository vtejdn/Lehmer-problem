"""Different AUTHOR verification of ALL4192 Xi16 triples and ALL256 kernel targets.

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
        # Base256 exceeds every binary convolution coefficient (degree<=128).
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
    assert a.bit_length()<=64 and b.bit_length()<=24 and c.bit_length()<=24
    return a | (b<<64) | (c<<88)


def unpack(value):
    return value&((1<<64)-1),(value>>64)&((1<<24)-1),value>>88



def recompute_old_word_data(output):
    source=json.loads((output/'endpoint_word_mod8_verification.json').read_text(encoding='utf-8'))
    original=json.loads((output/'endpoint_word_mod8.json').read_text(encoding='utf-8'))
    arrays=source['original_restrictions_mod8']
    assert arrays==original['original_restrictions_mod8']
    assert source['all7_full_mod8_trace_arrays_recovered_and_matched']
    def poly(values,modulus=None):
        return sp.Poly.from_list(list(reversed(values)),z,**({'modulus':modulus} if modulus else {'domain':sp.ZZ}))
    f=sp.Poly(z**4+z**3+1,z,modulus=2)
    cp=poly(arrays['c'],2)
    gamma=cp.exquo(f**4).rem(f**2)
    assert all(v%4==0 for v in arrays['F'])
    quarter=poly([v//4 for v in arrays['F']],2)
    g=quarter.exquo(f**4).rem(f**4)
    assert g.diff().is_zero
    rho=sp.Poly(sum(int(g.nth(2*i))*z**i for i in range(8)),z,modulus=2)
    assert rho**2==g
    # Reconstruct complete primitive traces from independent cyclotomic coefficients.
    cheb=[sp.Poly(2,z),sp.Poly(z,z)]
    for _ in range(2,129):
        cheb.append(sp.Poly(z,z)*cheb[-1]-cheb[-2])
    t=sp.symbols('t')
    def trace_factor(n):
        cyclo=sp.Poly(sp.cyclotomic_poly(n,t),t,domain=sp.ZZ)
        degree=cyclo.degree()//2
        result=sp.Poly(int(cyclo.nth(degree)),z)
        for j in range(1,degree+1):
            result+=int(cyclo.nth(degree+j))*cheb[j]
        return result
    pf=trace_factor(15)
    v480=trace_factor(480)
    j=poly(original['J_coefficients'])
    v960=j.exquo(pf**4)
    assert v960==trace_factor(960)==v480.compose(cheb[2])
    diff16=v480-pf**16
    diff32=v960-pf**32
    assert all(int(v)%2==0 for v in diff16.all_coeffs()+diff32.all_coeffs())
    delta16=sp.Poly.from_list([int(v)//2 for v in diff16.all_coeffs()],z,domain=sp.ZZ)
    delta32=sp.Poly.from_list([int(v)//2 for v in diff32.all_coeffs()],z,domain=sp.ZZ)
    db16=sp.Poly(delta16,z,modulus=2)
    db32=sp.Poly(delta32,z,modulus=2)
    assert db16**2==db32
    dm=db16.rem(f**2)
    denom=(dm*gamma).rem(f**2)
    target=(rho*sp.invert(denom,f**2)).rem(f**2)
    return dict(input_mod8='endpoint_word_mod8.json',
        input_verification='endpoint_word_mod8_verification.json',
        c_binary=bits(cp),quarter_binary=bits(quarter),normalized_quarter_mod_f4=bits(g),
        unique_square_root_mod_f2=bits(rho),gamma_Q_mod_f2=bits(gamma),
        actual_V960_coefficients=[int(v960.nth(i)) for i in range(129)],
        actual_delta32_coefficients=[int(delta32.nth(i)) for i in range(129)],
        delta32_binary=bits(db32),delta16_binary=bits(db16),delta16_mod_f2=bits(dm),
        denominator_mod_f2=bits(denom),required_h=bits(target),
        no_root_supplied_target_constant=True)


def main():
    here=Path(__file__).resolve().parent
    output=here.parents[3]/'mathematics/computations/outputs'/here.name
    saved=json.loads((output/'augmented_endpoint_kernel_image.json').read_text(encoding='utf-8'))
    old=json.loads((output/'endpoint_full_triple_image.json').read_text(encoding='utf-8'))
    actual_data=recompute_old_word_data(output)
    assert actual_data==saved['computed_old_word_data']
    desired_h=actual_data['required_h']
    polynomials=[sp.Poly((z**4+z**3+1)**16,z,modulus=2),
                 sp.Poly((z+1)**24,z,modulus=2),sp.Poly((z**2+z+1)**12,z,modulus=2)]
    rings=[Ring(bits(p)) for p in polynomials]
    assert [r.modulus for r in rings]==saved['moduli']
    assert [r.degree for r in rings]==saved['component_degrees']==[64,24,24]
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
    for order,multiplicity,period,target_ring in zip((15,3,5),(16,24,12),(240,96,80),rings):
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

    old_ring=Ring(bits(sp.Poly((z**4+z**3+1)**14,z,modulus=2)))
    assert old['subgroup_order']==45*(1<<85) and len(old['generators'])==4192
    for label,image,old_label in zip(labels,images,old['generators']):
        assert {k:v for k,v in label.items() if k not in ('image','components')}=={
            k:v for k,v in old_label.items() if k not in ('image','components')}
        assert [old_ring.reduce(image[0]),image[1],image[2]]==old_label['components']
    assert saved['old_projection']==dict(old_certificate='endpoint_full_triple_image.json',
        generators_checked=4192,old_subgroup_order=old['subgroup_order'],old_principal_rank=old['principal_rank'])

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
        for unit,prime,degree,length,offset in zip(value,(25,3,7),(4,1,2),(16,24,12),(0,60,83)):
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
    assert positions==sorted(set(positions)) and len(positions)<=105
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
    assert len(decisions)==256 and saved['all256_targets_tested']
    checked=[];attained=[]
    f14=sp.Poly((z**4+z**3+1)**14,z,modulus=2)
    for h,row in enumerate(decisions):
        hp=sp.Poly(sum(((h>>i)&1)*z**i for i in range(8)),z,modulus=2)
        target=(bits(sp.Poly(1,z,modulus=2)+f14*hp),1,1)
        assert gpower(target,2)==identity
        assert row['h']==h and pack(target)==row['target'] and list(target)==row['components']
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
                kernel_trace_degree=degree,kernel_reciprocal_degree=2*degree,
                resulting_T_trace_degree_not_tested=3390998+degree,
                resulting_T_reciprocal_degree_not_tested=2*(3390998+degree))
            assert endpoint%2==0
            attained.append(row)
        else:
            assert row['word'] is None and row['word_costs'] is None
        checked.append(dict(h=h,target_member=member,principal_remainder=result,
                            positive_word_checked=member,word_costs=row['word_costs']))
    assert len(attained)==saved['attained_target_count']
    attained_h={r['h'] for r in attained}
    assert sorted(attained_h)==saved['attained_h'] and 0 in attained_h
    assert all(a^b in attained_h for a in attained_h for b in attained_h)
    assert saved['subgroup_order']==old['subgroup_order']*len(attained)
    assert saved['desired_h']==desired_h and saved['desired_target_attained']==decisions[desired_h]['target_member']
    chosen=saved['selected_kernel_word']
    if decisions[desired_h]['target_member']:
        wanted=decisions[desired_h]
        assert chosen['required_h']==desired_h and chosen['word']==wanted['word']
        assert chosen['costs']==wanted['word_costs'] and chosen['target']==wanted['components']
        counts=Counter();terms=[]
        for index,exponent in decode(chosen['word']):
            label=labels[index]
            terms.append({k:label[k] for k in ('kind','n','q','a','b','trace_degree') if k in label}
                         |dict(index=index,exponent=exponent,degree_contribution=exponent*label['trace_degree']))
            if index:
                for r in sp.divisors(label['n'])[1:]:
                    for a in range(label['a']+1):
                        for b in range(label['b']+1):
                            counts[int(r)*3**a*5**b]+=exponent
        assert chosen['terms']==terms
        assert chosen['trace_factor_multiplicities']==[dict(order=n,multiplicity=e) for n,e in sorted(counts.items())]
        endpoint=dict(chosen['word']).get(0,0)
        assert chosen['endpoint_trace_multiplicity']==endpoint and chosen['actual_endpoint_factor']=='X-2'
        reciprocal=dict(counts)
        if endpoint:reciprocal[1]=2*endpoint
        assert chosen['reciprocal_cyclotomic_multiplicities']==[dict(order=n,multiplicity=e) for n,e in sorted(reciprocal.items())]
        degree=endpoint+sum(int(sp.totient(n))*e//2 for n,e in counts.items())
        assert degree==chosen['costs']['kernel_trace_degree']
        assert sum(int(sp.totient(n))*e for n,e in reciprocal.items())==2*degree
        assert chosen['certifies_only_augmented_kernel_target'] and chosen['no_product_residual_probe']
    else:
        assert chosen is None
    result=dict(scope='ALL4192 actual Xi16 triples and ALL256 eight-bit kernel targets',
        faithful_Laurent_moduli=['Phi15^16','Phi3^24','Phi5^12'],Laurent_degrees=[128,48,48],
        Laurent_z_periods=[240,96,80],verified_generators=4192,verified_old_image_projections=4192,
        verified_odd_generator_coordinates=4192,verified_odd_words=len(odd),
        actual_odd_subgroup_pairs=[list(p) for p in sorted(odd)],
        verified_pivot_words=len(basis),verified_later_square_relations=len(basis),
        verified_original_principal_reductions=4192,principal_rank=len(basis),
        principal_component_pivot_counts=[sum(a<=p<b for p in positions) for a,b in ((0,60),(60,83),(83,105))],
        odd_subgroup_order=len(odd),subgroup_order=len(odd)*(1<<len(basis)),
        old_subgroup_order=old['subgroup_order'],kernel_size_by_projection_ratio=len(attained),
        target_decisions=checked,attained_target_count=len(attained),attained_h=sorted(attained_h),
        all256_target_normalforms_and_positive_words_checked=True,
        recomputed_old_word_data=actual_data,desired_h=desired_h,desired_target_attained=bool(chosen),
        chosen_kernel_word_and_factor_costs_checked=bool(chosen),
        chosen_kernel_costs=chosen['costs'] if chosen else None,
        arithmetic='faithful Laurent kernels and carry-free integer convolution; target from actual adopted arrays and independent integral cyclotomic traces',
        sympy_version=sp.__version__,author_self_check=True,independent_review=False,
        no_product_residual_probe=True,no_full_integer_word_expansion=True,no_other_word_optimization=True)
    temporary=output/'augmented_endpoint_kernel_image_verification.json.partial'
    temporary.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    temporary.replace(output/'augmented_endpoint_kernel_image_verification.json')
    print(json.dumps({k:result[k] for k in ('verified_generators','principal_rank',
        'principal_component_pivot_counts','odd_subgroup_order','attained_target_count',
        'desired_h','desired_target_attained','chosen_kernel_costs')}))


if __name__=='__main__':
    main()
