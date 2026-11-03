"""One264-term Q1: EXACT ambient eight-bit lowest-second-half image only.

Consume the saved original-mod8 producer and completed different verifier.
No original residual, word, cofactor image, higher modulus or new profile is computed.
Polynomial arrays are ascending integer coefficients; binary integers use bit i for X^i.
"""
from pathlib import Path
import argparse
import json
from math import gcd


def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def zmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)


def zpow(a,n):
    r=[1]
    while n:
        if n&1:r=zmul(r,a)
        a=zmul(a,a);n>>=1
    return r


def zdiv(a,b):
    a=trim(a);b=trim(b)
    assert b[-1]==1
    q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        shift=len(a)-len(b);v=a[-1];q[shift]=v
        for j,x in enumerate(b):a[shift+j]-=v*x
        a=trim(a)
    return trim(q),a


def bits(a):
    return sum((int(c)&1)<<i for i,c in enumerate(a))


def bmul(a,b):
    c=0
    while b:
        if b&1:c^=a
        a<<=1;b>>=1
    return c


def bdiv(a,b):
    assert b
    q=0
    while a and a.bit_length()>=b.bit_length():
        j=a.bit_length()-b.bit_length();q^=1<<j;a^=b<<j
    return q,a


def brem(a,m):return bdiv(a,m)[1]


def bpow(a,n,m=None):
    r=1
    while n:
        if n&1:r=bmul(r,a);r=brem(r,m) if m else r
        a=bmul(a,a);a=brem(a,m) if m else a;n>>=1
    return r


def compose(a,b,m):
    r=0
    for i in range(a.bit_length()-1,-1,-1):
        r=brem(bmul(r,b),m)^((a>>i)&1)
    return r


def reduce_vector(v,basis):
    witness=0
    for pivot in sorted(basis,reverse=True):
        if (v>>pivot)&1:
            row,word=basis[pivot];v^=row;witness^=word
    return v,witness


def load_inputs(here,out):
    source=json.loads((out/'full_eighth_positive_product_mod8.json').read_text(encoding='utf-8'))
    verified=json.loads((out/'full_eighth_positive_product_mod8_verification.json').read_text(encoding='utf-8'))
    word=json.loads((here/'inputs/full_eighth_positive_product_word.json').read_text(encoding='utf-8'))
    assert source['selected_input']=='inputs/full_eighth_positive_product_word.json'
    assert len(source['terms'])==len(word['terms'])==264 and source['terms']==word['terms']
    assert word['source_mask']==819 and word['branch']==2
    assert source['costs']==verified['costs']==word['costs']
    assert source['quotient_degree']==verified['quotient_trace_degree']==144
    assert source['actual_single_F960'] and verified['exact_single_F960_and_integral_trace_identity_checked']
    assert verified['all7_full_mod8_trace_arrays_recovered_and_matched']
    assert verified['true_full_Z_base_and_J_prime_divisions_checked']
    assert verified['all792_term_values_and_powers_checked']
    assert source['original_restrictions_mod8']==verified['original_restrictions_mod8']
    arrays=source['original_restrictions_mod8']
    assert set(arrays)=={'a','b','c','F','G','X_plus','X_minus'}
    assert all(type(c) is int and 0<=c<8 for a in arrays.values() for c in a)
    assert all(c==0 for c in arrays['F'])
    assert all(c%2==0 for name in ('X_plus','X_minus') for c in arrays[name])
    assert all(t['kind']=='endpoint' or (t['kind']=='rectangle' and t['n']>1 and gcd(t['n'],30)==1 and t['q']==3**t['a']*5**t['b']) for t in word['terms'])
    return source,verified,word,arrays


def main():
    here=Path(__file__).resolve().parent
    out=here.parents[3]/'mathematics/computations/outputs'/here.name
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=out/'second_half_ambient_response.json')
    args=parser.parse_args()
    source,verified,word,arrays=load_inputs(here,out)
    # Fixed integer F15; V and its true half are recovered from the ACTUAL saved J.
    P=[1,4,-4,-1,1]
    J=source['J_coefficients']
    V,left=zdiv(J,zpow(P,4));assert left==[0] and len(V)==129
    P32=zpow(P,32)
    difference=[(V[i] if i<len(V) else 0)-(P32[i] if i<len(P32) else 0) for i in range(max(len(V),len(P32)))]
    assert all(c%2==0 for c in difference)
    delta=trim([c//2 for c in difference])
    f=bits(P);f2=bpow(f,2);f4=bpow(f,4)
    beta,left=bdiv(bits(arrays['b']),bpow(f,6));assert left==0
    gamma,left=bdiv(bits(arrays['c']),bpow(f,4));assert left==0
    assert brem(beta,f)!=0 and brem(gamma,f)!=0 and brem(bits(delta),f)!=0
    half_arrays={};target_classes={}
    for name in ('X_plus','X_minus'):
        half=[c//2 for c in arrays[name]]
        normalized,left=bdiv(bits(half),f4);assert left==0
        half_arrays[name]=half
        target_classes[name]=brem(normalized,f4)
    p=bits([1,1,1]);lam=bits([0,1,0,1]);chi=bmul(bits([0,1]),bpow(p,2))
    coeff_delta=brem(bits(delta),f4)
    coeff_beta2=bpow(beta,2,f4)
    coeff_gamma3=bpow(gamma,3,f4)

    def response(mask):
        r=mask&15;s=mask>>4
        u=brem(bmul(bpow(p,12),compose(r,lam,f2)),f2)
        w=brem(bmul(bpow(bits([1,1]),24),compose(s,chi,f4)),f4)
        value=brem(bmul(coeff_delta,bmul(coeff_beta2,bmul(u,u))^bmul(coeff_gamma3,w)),f4)
        return dict(source_mask=mask,r_bits=r,s_bits=s,u_bits=u,w_bits=w,image_bits=value)

    images=[response(mask) for mask in range(256)]
    columns=[dict(index=i,source=('r' if i<4 else 's'),power=i%4,**images[1<<i]) for i in range(8)]
    for mask,item in enumerate(images):
        linear=0
        for i,col in enumerate(columns):
            if (mask>>i)&1:linear^=col['image_bits']
        assert item['image_bits']==linear
    basis={}
    for i,col in enumerate(columns):
        value,wordmask=reduce_vector(col['image_bits'],basis)
        wordmask^=1<<i
        if value:basis[value.bit_length()-1]=(value,wordmask)
    targets={}
    for name,target in target_classes.items():
        remainder,wordmask=reduce_vector(target,basis)
        matches=[row['source_mask'] for row in images if row['image_bits']==target]
        assert bool(matches)==(remainder==0)
        record=dict(target_bits=target,member=(remainder==0),matching_source_masks=matches,normal_remainder_bits=remainder,normal_source_mask=wordmask)
        if remainder:
            obstruction_bit=remainder.bit_length()-1
            separator=sum((((reduce_vector(1<<i,basis)[0]>>obstruction_bit)&1)<<i) for i in range(16))
            assert all((separator&col['image_bits']).bit_count()%2==0 for col in columns)
            assert (separator&target).bit_count()%2==1
            record['separator_bits']=separator
        targets[name]=record
    assert len({row['image_bits'] for row in images})==1<<len(basis)
    result=dict(
        scope='ONLY literal264-term Q1; ambient8 source bits, all256 images, both genuine second halves',
        input_files=['full_eighth_positive_product_mod8.json','full_eighth_positive_product_mod8_verification.json','inputs/full_eighth_positive_product_word.json'],
        source_costs=source['costs'],source_terms=source['terms'],
        all7_input_mod8_arrays_matched=True,
        P_coefficients=P,V_coefficients=V,delta_coefficients=delta,
        f_bits=f,modulus_f4_bits=f4,
        beta_R30_bits=beta,gamma_R32_bits=gamma,
        coefficient_classes_R4=dict(delta_bits=coeff_delta,beta_squared_bits=coeff_beta2,gamma_cubed_bits=coeff_gamma3),
        genuine_integer_half_arrays_mod4=half_arrays,
        columns=columns,all256_source_images=images,rank=len(basis),distinct_image_count=1<<len(basis),
        binary_basis=[dict(pivot=pivot,image_bits=value,source_mask=mask) for pivot,(value,mask) in sorted(basis.items(),reverse=True)],
        targets=targets,
        arithmetic='integer monic J/P4 division and true delta half; carryless binary polynomial arithmetic; exact XOR elimination',
        no_original_residual_recalculation=True,no_other_word_or_image=True,no_120bit_image=True,no_higher_modulus=True,
        author_self_check=True,independent_review=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    partial=args.output.with_suffix(args.output.suffix+'.partial')
    try:
        partial.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        partial.replace(args.output)
    finally:
        if partial.exists():partial.unlink()
    print(json.dumps(dict(rank=result['rank'],distinct_images=result['distinct_image_count'],targets=targets)))


if __name__=='__main__':main()
