"""Different AUTHOR verifier of the old4193-label actual two-source span.

IMPLEMENTATION ONLY until the source/presentation theorem is adopted and root
authorizes execution.  The producer is not imported.  Binary sources use the
faithful Phi5^28 Laurent quotient; mixed sources use Phi3^4 Phi192 with the
additional even ideal2Phi3^24.  Epsilon low/high recovery retains integer carry.
No three-J-weight image, new original residual probe or full-M alphabet scan.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
from math import comb
import argparse
import ctypes
import json
import os
import sys
import time
import sympy as sp
from verify_augmented_endpoint_kernel_image import Ring, division
from verify_full_eighth_kernel_image import ModFourRing, binary_remainder, binary_inverse
from verify_full_second_half_ambient_screen import FullAmbient, poly, bits, bit_poly, binary_rref
from verify_positive_word_residuals import trace_factor, coefficients, x, z
from verify_joint_eighth_second_half_kernel_image import costs as positive_costs


INPUTS=['joint_eighth_second_half_kernel_image.json',
        'joint_eighth_second_half_kernel_image_verification.json',
        'complete_four_coset_next_half_screen.json',
        'complete_four_coset_next_half_screen_verification.json']


class ResourceLimit(RuntimeError):
    pass


class Budget:
    def __init__(self,seconds,mib):
        self.start=time.monotonic();self.seconds=seconds;self.mib=mib
        self.peak=0.0;self.phase='input preparation'

    def check(self):
        elapsed=time.monotonic()-self.start
        if os.name=='nt':
            from ctypes import wintypes
            class Memory(ctypes.Structure):
                _fields_=[('cb',wintypes.DWORD),('faults',wintypes.DWORD)]+[
                    (n,ctypes.c_size_t) for n in ('peak','working','peak_paged','paged',
                        'peak_nonpaged','nonpaged','pagefile','peak_pagefile','private')]
            counters=Memory();counters.cb=ctypes.sizeof(counters)
            kernel=ctypes.WinDLL('kernel32',use_last_error=True)
            psapi=ctypes.WinDLL('psapi',use_last_error=True)
            kernel.GetCurrentProcess.restype=wintypes.HANDLE
            psapi.GetProcessMemoryInfo.argtypes=[wintypes.HANDLE,ctypes.POINTER(Memory),wintypes.DWORD]
            if not psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(),ctypes.byref(counters),counters.cb):
                raise ResourceLimit('could not monitor own-process memory')
            current=counters.working/1048576
            self.peak=max(self.peak,counters.peak/1048576)
        else:
            import resource
            current=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
            self.peak=max(self.peak,current)
        if elapsed>self.seconds or self.peak>self.mib:
            raise ResourceLimit(f'{self.phase}: elapsed={elapsed:.1f}s working={current:.1f}MiB')
        return dict(elapsed_seconds=elapsed,observed_peak_working_mib=self.peak)


def publish(path,payload,budget=None):
    path.parent.mkdir(parents=True,exist_ok=True)
    partial=path.with_suffix(path.suffix+'.partial')
    try:
        with partial.open('w',encoding='utf-8',newline='\n') as handle:
            json.dump(payload,handle,indent=2);handle.write('\n')
        if budget is not None:budget.check()
        partial.replace(path)
    finally:
        if partial.exists():partial.unlink()


def set_bits(value):
    assert type(value) is int and value>=0
    while value:
        low=value&-value
        yield low.bit_length()-1
        value^=low


def word_add(a,b,scale=1):
    result=dict(a)
    for i,e in b.items():
        value=(result.get(i,0)+scale*e)%960
        if value:result[i]=value
        else:result.pop(i,None)
    return result


def encoded(word):
    return [[i,e] for i,e in sorted(word.items()) if e]


def decoded(word):
    assert type(word) is list and word==sorted(word)
    assert len(word)==len({i for i,e in word})
    assert all(type(i) is int and 0<=i<4193 and type(e) is int and 0<e<960 for i,e in word)
    return dict(word)


def xor_mask(values,mask):
    assert type(mask) is int and 0<=mask<1<<len(values)
    result=0
    for i in set_bits(mask):result^=values[i]
    return result


class BinaryFifthSource:
    def __init__(self):
        p=sp.Poly(x*x+x+1,x,modulus=2)
        self.modulus=bits(p**28);self.half_modulus=bits(p**14)
        self.ring=Ring(self.modulus)
        cyclo=sp.Poly(sp.cyclotomic_poly(5,z),z,modulus=2)**28
        self.laurent=Ring(bits(cyclo))
        assert self.ring.degree==56 and self.laurent.degree==112
        self.shifted=[]
        for j in range(56):
            value=sum((comb(j,k)%2)<<(55+j-2*k) for k in range(j+1))
            self.shifted.append(value)
        assert self.laurent.power(2,160)==1
        assert self.recover(2^self.laurent.power(2,159))==2

    def recover(self,value):
        work=self.laurent.reduce(value<<55)
        assert work.bit_length()<=111
        result=0
        for j in range(55,-1,-1):
            if (work>>(55+j))&1:
                result|=1<<j;work^=self.shifted[j]
        assert work==0
        return result

    @lru_cache(None)
    def image(self,n,q):
        total=0;a=(n-1)//2
        for j in range(-a,a+1):total^=1<<((q*j)%160)
        return self.recover(self.laurent.reduce(total))


class MixedThirdSource:
    """Faithful Laurent B5, with actual canonical epsilon low36/high24."""
    one=(1,0)
    zero=(0,0)

    def __init__(self):
        self.F192=trace_factor(192)
        self.J5=sp.Poly((x+1)**4,x)*self.F192
        self.J5eps=self.J5.compose(sp.Poly(x-1,x))
        phi=sp.Poly(z*z+z+1,z,domain=sp.ZZ)
        reciprocal=phi**4*sp.Poly(sp.cyclotomic_poly(192,z),z,domain=sp.ZZ)
        assert reciprocal.degree()==72 and self.J5.degree()==36
        expansion=sp.Poly(0,z,domain=sp.ZZ)
        for j in range(37):
            for k in range(j+1):
                expansion+=sp.Poly(int(self.J5.nth(j))*comb(j,k)*z**(36+j-2*k),z)
        assert expansion==reciprocal
        self.full=ModFourRing(reciprocal)
        self.phi24=bits(sp.Poly(phi.as_expr(),z,modulus=2)**24)
        self.phi36=bits(sp.Poly(phi.as_expr(),z,modulus=2)**36)
        assert self.full.binary_modulus==self.phi36
        self.low_shifted=[];self.high_shifted=[]
        for d,destination in ((36,self.low_shifted),(24,self.high_shifted)):
            for j in range(d):
                destination.append(bits(sp.Poly(phi.as_expr(),z,modulus=2)**j)<<(d-1-j))
        z_value=self.full.reduce([0,1])
        z_inverse=self.full.inverse(z_value)
        self.Y=self.full.add(z_value,z_inverse)
        epsilon=self.full.add(self.Y,self.full.one)
        self.eps_powers=[self.full.one]
        for _ in range(35):self.eps_powers.append(self.full.multiply(self.eps_powers[-1],epsilon))
        self.sparse=[[(i,c) for i,c in enumerate(row) if c] for row in self.eps_powers]
        z_source=self.from_full(z_value)
        self.zpowers=[self.one]
        for _ in range(192):self.zpowers.append(self.multiply(self.zpowers[-1],z_source))
        assert self.zpowers[192]==self.one
        assert self.to_epsilon(self.from_full(self.Y))==(3,1)  # epsilon-1, including its even carry
        self.endpoint=self.from_full(self.full.add(self.Y,self.full.one,-2))
        assert self.to_epsilon(self.endpoint)==(3,0)  # epsilon-3

    def from_full(self,values):
        assert len(values)==72
        low=sum((c&1)<<i for i,c in enumerate(values))
        high=sum(((c>>1)&1)<<i for i,c in enumerate(values))
        return low,binary_remainder(high,self.phi24)

    @lru_cache(maxsize=8192)
    def lift(self,value):
        low,high=value
        assert low.bit_length()<=72 and high.bit_length()<=48
        return tuple(((low>>i)&1)+2*((high>>i)&1) for i in range(72))

    def multiply(self,a,b):
        if a==self.one:return b
        if b==self.one:return a
        return self.from_full(self.full.multiply(self.lift(a),self.lift(b)))

    def add(self,a,b):
        return a[0]^b[0],binary_remainder(a[1]^b[1]^(a[0]&b[0]),self.phi24)

    def negative(self,a):
        return a[0],binary_remainder(a[1]^a[0],self.phi24)

    def power(self,a,n):
        value=self.one
        while n:
            if n&1:value=self.multiply(value,a)
            n>>=1
            if n:a=self.multiply(a,a)
        return value

    @lru_cache(None)
    def inverse(self,a):
        value=self.from_full(self.full.inverse(self.lift(a)))
        assert self.multiply(a,value)==self.one
        return value

    def recover_binary_epsilon(self,value,d):
        modulus,shifted=(self.phi36,self.low_shifted) if d==36 else (self.phi24,self.high_shifted)
        work=binary_remainder(value<<(d-1),modulus)
        assert work.bit_length()<=2*d-1
        answer=0
        for j in range(d-1,-1,-1):
            if (work>>(d-1+j))&1:
                answer|=1<<j;work^=shifted[j]
        assert work==0
        return answer

    def epsilon_lift(self,low,high):
        assert low.bit_length()<=36 and high.bit_length()<=24
        values=[0]*72
        for j in range(36):
            coefficient=((low>>j)&1)+2*((high>>j)&1)
            if coefficient:
                for i,c in self.sparse[j]:values[i]+=coefficient*c
        return tuple(v%4 for v in values)

    @lru_cache(maxsize=32768)
    def to_epsilon(self,value):
        low=self.recover_binary_epsilon(value[0],36)
        # The subtraction uses the ACTUAL0/1 epsilon-polynomial lift.
        # Its integer carry is retained before taking the even quotient.
        lift=self.from_full(self.epsilon_lift(low,0))
        even=self.add(value,self.negative(lift))
        assert even[0]==0
        high=self.recover_binary_epsilon(even[1],24)
        assert self.from_full(self.epsilon_lift(low,high))==value
        return low,high

    @lru_cache(None)
    def image(self,n,q):
        low=high=0;a=(n-1)//2
        for j in range(-a,a+1):
            l,h=self.zpowers[(q*j)%192]
            high^=h^(low&l);low^=l
        return low,binary_remainder(high,self.phi24)


class SourcePair:
    def __init__(self):
        self.B=BinaryFifthSource();self.C=MixedThirdSource();self.one=(1,self.C.one)
        self.epsilon_to_Y=[bits(sp.Poly((x+1)**j,x,modulus=2)) for j in range(28)]

    def image(self,label):
        if label['kind']=='endpoint':return 2,self.C.endpoint
        return self.B.image(label['n'],label['q']),self.C.image(label['n'],label['q'])

    def multiply(self,a,b):
        return self.B.ring.multiply(a[0],b[0]),self.C.multiply(a[1],b[1])

    def square(self,a):return self.multiply(a,a)

    @lru_cache(None)
    def inverse(self,a):
        return binary_inverse(a[0],self.B.modulus),self.C.inverse(a[1])

    def fields(self,a):
        return dict(source_b_bits=a[0],source_c=list(self.C.to_epsilon(a[1])))

    def project(self,a):
        low,_=self.C.to_epsilon(a[1])
        source3=xor_mask(self.epsilon_to_Y,low&((1<<28)-1))
        source5=binary_remainder(a[0],self.B.half_modulus)
        return source3,source5

    def coordinates(self,a):
        r,rem=division(a[0]^1,self.B.half_modulus)
        assert rem==0 and r.bit_length()<=28
        low,s=self.C.to_epsilon(a[1])
        assert (low&((1<<28)-1))==1 and s.bit_length()<=24
        w=low>>28
        assert w.bit_length()<=8
        return dict(r_bits=r,w_epsilon_bits=w,s_epsilon_bits=s,vector60=r|(w<<28)|(s<<36))


def rank_low(values):
    pivots={}
    for value in values:
        while value:
            p=(value&-value).bit_length()-1
            if p not in pivots:
                pivots[p]=value;break
            value^=pivots[p]
    return len(pivots)


def source_word_coordinates_check(pair,value,coords):
    assert pair.coordinates(value)==coords
    r=coords['r_bits'];w=coords['w_epsilon_bits'];s=coords['s_epsilon_bits']
    # Reconstruct the ACTUAL two source classes, including the mixed carry.
    raw=(1^bits(poly([1,1,1])**14*bit_poly(r)),
         pair.C.from_full(pair.C.epsilon_lift(1|(w<<28),s)))
    assert raw==value


def reference_data_columns(reference,ambient):
    arrays=reference['original_restrictions_mod8']
    assert set(arrays)=={'a','b','c','F','G','X_plus','X_minus'}
    assert all(type(v) is int and 0<=v<8 for a in arrays.values() for v in a)
    assert not any(arrays['F']) and any(v%2 for v in arrays['G'])
    beta=poly(arrays['b']).exquo(ambient.f**6)
    gamma=poly(arrays['c']).exquo(ambient.f4)
    beta2=(beta**2).rem(ambient.f28);gamma3=(gamma**3).rem(ambient.f28)
    halves={};full={};targets={}
    for name in ('X_plus','X_minus'):
        assert all(v%2==0 for v in arrays[name])
        halves[name]=[v//2 for v in arrays[name]]
        full[name]=bits(poly(halves[name]))
        target=poly(halves[name]).exquo(ambient.f8)
        assert target.is_zero or target.degree()<112
        targets[name]=bits(target.rem(ambient.f28))
    gdiv=bits(poly(arrays['G']).exquo(ambient.f8).rem(ambient.f28))
    assert gdiv==targets['X_plus']^targets['X_minus']!=0
    assert full['X_plus']^full['X_minus']==bits(poly(arrays['G']))
    assert gdiv==bits((ambient.f4*gamma3).rem(ambient.f28))
    data=dict(genuine_half_arrays_mod4=halves,full_half_bits=full,normalized_targets_bits=targets,
        beta_bits=bits(beta),gamma_bits=bits(gamma),beta_squared_R28=bits(beta2),gamma_cubed_R28=bits(gamma3),
        delta_R28=bits(ambient.delta_bar),target_difference_R28=gdiv,G_div_f8_R28=gdiv)
    columns=[]
    for index in range(60):
        value,U,W,S=ambient.response(1<<index,beta2,gamma3)
        block,power=('r',index) if index<28 else (('w',index-28) if index<36 else ('s',index-36))
        source=ambient.source_polynomials(1<<index)
        columns.append(dict(index=index,block=block,power=power,source_mask=1<<index,
            source_polynomial_bits=bits(source[{'r':0,'w':1,'s':2}[block]]),U_bits=bits(U),
            w_chi_bits=bits(W),s_chi_bits=bits(S),image_bits=bits(value)))
    assert columns[36]['image_bits']==gdiv
    return data,columns,beta2,gamma3


def checked_case_equal(a,b):
    assert {k:v for k,v in a.items() if k!='next_half'}=={k:v for k,v in b.items() if k!='next_half'}
    for key in ('genuine_half_arrays_mod4','beta_R30_bits','gamma_R32_bits',
                'coefficient_classes_R4','columns','all256_source_images','rank','outcome'):
        assert a['next_half'][key]==b['next_half'][key]
    for name in ('X_plus','X_minus'):
        for key in ('target_bits','member','matching_source_masks'):
            assert a['next_half']['targets'][name][key]==b['next_half']['targets'][name][key]


def main():
    here=Path(__file__).resolve().parent;out=here.parents[1]/'outputs'/here.name
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--result',type=Path,default=out/'full_fourth_gate_known_word_span.json')
    parser.add_argument('--output',type=Path,default=out/'full_fourth_gate_known_word_span_verification.json')
    parser.add_argument('--max-seconds',type=float,default=1800)
    parser.add_argument('--max-working-mib',type=float,default=1024)
    args=parser.parse_args();assert args.max_seconds>0 and args.max_working_mib>0
    budget=Budget(args.max_seconds,args.max_working_mib)
    checkpoint=args.output.with_suffix('.incomplete.json')
    progress=dict(complete=False,completed_stage='not started')
    def stage(name,formed):
        budget.phase=name
        progress.update(completed_stage=name,resources=budget.check(),formed_payload=formed)
        publish(checkpoint,progress,budget)
        print(json.dumps(dict(stage=name,**progress['resources'])),flush=True)
    try:
        old,oldcheck,screen,sv=[json.loads((out/n).read_text(encoding='utf-8')) for n in INPUTS]
        saved=json.loads(args.result.read_text(encoding='utf-8'))
        assert saved['required_inputs']==INPUTS
        assert old['generators']==oldcheck['verified_generators']
        assert old['relations']==oldcheck['verified_relations']
        assert old['kernel_basis']==oldcheck['kernel_basis']
        assert old['kernel_rank']==oldcheck['kernel_rank']==59
        assert oldcheck['verified_new_source_count']==4193 and oldcheck['verified_relation_count']==6310
        assert oldcheck['verified_odd_lifts']==45 and oldcheck['verified_principal_lifts']==92
        assert oldcheck['both120_relation_span_inclusions_checked']
        assert oldcheck['all_new_positive_word_images_and_complete_costs_checked']
        assert old['relation_counts']=={'generator':4193,'square':92,'odd':2025}
        assert screen['base']==sv['base']==saved['base'] and screen['summary']==sv['summary']
        assert screen['masks']==sv['masks'] and screen['fibers']==sv['fibers']
        assert screen['nullspace_certificate']==sv['nullspace_certificate']
        assert sv['all448_original_mod8_arrays_checked'] and sv['all64_four_coset_bindings_independently_derived']
        assert sv['true_full_Z_base_and_J_prime_divisions_checked']
        assert len(screen['cases'])==len(sv['cases'])==64
        assert [(r['source_mask'],r['coset_bits']) for r in screen['cases']]==[(m,e) for m in screen['masks'] for e in range(4)]
        chosen=[]
        for i,(a,b) in enumerate(zip(screen['cases'],sv['cases'])):
            checked_case_equal(a,b)
            if a['next_half']['targets']['X_plus']['member']:
                assert a['next_half']['targets']['X_minus']['member'];chosen.append((i,a))
        assert len(chosen)==32 and Counter(r['source_mask'] for _,r in chosen)=={m:2 for m in screen['masks']}
        assert saved['selected_case_ids']==[[r['source_mask'],r['coset_bits']] for _,r in chosen]
        labels=[r['actual_label'] for r in old['generators']]
        assert len(labels)==4193 and labels[-1]['n']==481 and labels[-1]['q']==1
        assert sum(r['trace_degree'] for r in labels)==8258020017
        assert labels==screen['labels']
        for label in labels:
            if label['kind']=='rectangle':
                assert label['q']==3**label['a']*5**label['b']
                assert label['trace_degree']==label['q']*(label['n']-1)//2
        ambient=FullAmbient(screen['base'])
        pair=SourcePair()
        params=dict(exponent=960,binary_source_modulus=pair.B.modulus,binary_half_modulus=pair.B.half_modulus,
            J5_Y=coefficients(pair.C.J5),J5_epsilon=coefficients(pair.C.J5eps),
            epsilon_low_degree=36,epsilon_even_degree=24,source_packing=dict(r=0,w=28,s=36),
            source_dimension=60,target_dimension=112,
            word_list='6310 Z_j times all indicated positive B_p, followed by59 B_p squared',
            full_M_alphabet_not_evaluated=True)
        assert saved['parameters']==params
        budget.phase='4193 faithful Laurent source evaluations'
        generators=[];sources=[]
        assert len(saved['generators'])==4193
        for i,(label,prior) in enumerate(zip(labels,old['generators'])):
            value=pair.image(label)
            assert list(pair.project(value))==prior['Xi_plus_components'][1:]
            assert pair.B.ring.power(value[0],96)==1
            assert pair.C.power(value[1],64)==pair.C.one
            own=dict(prior,**pair.fields(value));assert own==saved['generators'][i]
            generators.append(own);sources.append(value)
            if i%64==0:budget.check()
        stage('all4193_two_source_values_verified',generators)
        budget.phase='45/92 literal lifts and6310 relation recipes'

        @lru_cache(None)
        def generator_power(i,bit):
            return sources[i] if bit==0 else pair.square(generator_power(i,bit-1))
        @lru_cache(maxsize=4096)
        def cached_word_source(word):
            value=pair.one
            for i,e in word:
                assert 0<=i<4193 and 0<e<960
                for bit in set_bits(e):value=pair.multiply(value,generator_power(i,bit))
            return value
        def word_source(word):return cached_word_source(tuple(tuple(t) for t in encoded(word)))
        def degree(word):return sum(labels[i]['trace_degree']*e for i,e in word.items())
        odd={};pivots={};odd_lifts=[];principal_lifts=[]
        for prior in old['odd_lifts']:
            word=decoded(prior['word']);value=word_source(word)
            assert list(pair.project(value))==prior['source28_14']
            odd[tuple(prior['pair'])]=(prior,value);odd_lifts.append(dict(prior,**pair.fields(value)))
        for prior in old['principal_lifts']:
            word=decoded(prior['word']);value=word_source(word)
            assert list(pair.project(value))==prior['source28_14']
            pivots[prior['position']]=(prior,value);principal_lifts.append(dict(prior,**pair.fields(value)))
        assert len(odd)==45 and len(pivots)==92
        assert saved['odd_lifts']==odd_lifts and saved['principal_lifts']==principal_lifts
        relations=[];relation_sources=[]
        for j,prior in enumerate(old['relations']):
            recipe=prior['recipe'];kind=recipe['kind']
            if kind=='generator':
                i=recipe['generator'];o,ov=odd[tuple(recipe['odd_pair'])]
                value=pair.multiply(sources[i],pair.inverse(ov));word=word_add({i:1},decoded(o['word']),-1)
                positions=recipe['positions']
            elif kind=='square':
                p,pv=pivots[recipe['position']]
                assert recipe['later_positions']==p['later_square_positions']
                assert all(k>recipe['position'] for k in recipe['later_positions'])
                value=pair.square(pv);word=word_add({},decoded(p['word']),2);positions=recipe['later_positions']
            else:
                assert kind=='odd'
                a,b,c=[tuple(recipe[k]) for k in ('a','b','c')]
                assert c==((a[0]+b[0])%15,(a[1]+b[1])%3)
                ar,av=odd[a];br,bv=odd[b];cr,cv=odd[c]
                value=pair.multiply(pair.multiply(av,bv),pair.inverse(cv))
                word=word_add(word_add(decoded(ar['word']),decoded(br['word'])),decoded(cr['word']),-1);positions=[]
            for pos in positions:
                pr,pv=pivots[pos]
                value=pair.multiply(value,pair.inverse(pv));word=word_add(word,decoded(pr['word']),-1)
            assert encoded(word)==prior['word']
            assert list(pair.project(value))==prior['source28_14']
            row=dict(prior,**pair.fields(value));assert row==saved['relations'][j]
            relations.append(row);relation_sources.append(value)
            if j%128==0:budget.check()
        assert len(relations)==len(saved['relations'])==6310
        b_lookup={r['position']:r for r in old['kernel_basis']}
        b_values={};basis_lifts=[]
        for prior in sorted(old['kernel_basis'],key=lambda r:r['seed_relation']):
            seed=prior['seed_relation'];word=decoded(relations[seed]['word'])
            value=relation_sources[seed];vector=relations[seed]['vector']
            for pos in prior['construction_positions']:
                assert b_lookup[pos]['seed_relation']<seed
                value=pair.multiply(value,b_values[pos]);word=word_add(word,decoded(b_lookup[pos]['word']))
                vector^=b_lookup[pos]['vector']
            assert encoded(word)==prior['word'] and vector==prior['vector']
            assert positive_costs(word,labels)==prior['costs']
            r=(vector>>112)&15;s=vector>>116
            expected3=1^bits(sp.Poly((x+1)**24,x,modulus=2)*bit_poly(s))
            expected5=1^bits(poly([1,1,1])**12*bit_poly(r))
            assert pair.project(value)==(expected3,expected5)
            b_values[prior['position']]=value;basis_lifts.append(dict(prior,**pair.fields(value)))
        basis_lifts.sort(key=lambda r:r['position'])
        assert len(basis_lifts)==59 and basis_lifts==saved['basis_lifts']
        stage('all6310_recipes_and59_lifts_verified',dict(relations=relations,basis_lifts=basis_lifts))
        budget.phase='6369 actual kernel words and complete source span'
        known=[];known_sources=[]
        for j,row in enumerate(relations):
            positions=row['linear_reduction']['used_positions']
            assert row['linear_reduction']['remainder']==0
            word=decoded(row['word']);value=relation_sources[j];theta=row['vector']
            for pos in positions:
                word=word_add(word,decoded(b_lookup[pos]['word']));value=pair.multiply(value,b_values[pos]);theta^=b_lookup[pos]['vector']
            assert theta==0
            coords=pair.coordinates(value);source_word_coordinates_check(pair,value,coords)
            own=dict(index=j,kind='relation_correction',relation_index=j,correction_positions=positions,
                word=encoded(word),cofactor_degree=degree(word),endpoint_exponent=word.get(0,0),
                **pair.fields(value),coordinates=coords,theta_vector=0)
            assert {k:v for k,v in saved['known_words'][j].items() if k!='linear_reduction'}==own
            known.append(own);known_sources.append(value)
            if j%128==0:budget.check()
        for prior in old['kernel_basis']:
            word=word_add({},decoded(prior['word']),2);value=pair.square(b_values[prior['position']])
            coords=pair.coordinates(value);source_word_coordinates_check(pair,value,coords)
            own=dict(index=len(known),kind='basis_square',basis_position=prior['position'],correction_positions=[],
                word=encoded(word),cofactor_degree=degree(word),endpoint_exponent=word.get(0,0),
                **pair.fields(value),coordinates=coords,theta_vector=prior['vector']^prior['vector'])
            assert {k:v for k,v in saved['known_words'][len(known)].items() if k!='linear_reduction'}==own
            known.append(own);known_sources.append(value)
        assert len(known)==len(saved['known_words'])==6369
        vectors=[r['coordinates']['vector60'] for r in known]
        source_basis=saved['source_basis'];rank=rank_low(vectors)
        assert rank==len(source_basis)<=60
        assert [r['pivot'] for r in source_basis]==sorted({r['pivot'] for r in source_basis},reverse=True)
        assert rank_low([r['vector60'] for r in source_basis])==rank
        def word_from_known(mask):
            assert 0<=mask<1<<6369
            word={}
            for i in set_bits(mask):word=word_add(word,decoded(known[i]['word']))
            return word
        for row in source_basis:
            vector=xor_mask(vectors,row['known_word_mask'])
            assert vector==row['vector60'] and vector.bit_length()-1==row['pivot']
            word=word_from_known(row['known_word_mask']);assert encoded(word)==row['word']
            actual=word_source(word);coords=pair.coordinates(actual)
            assert coords==row['coordinates'] and coords['vector60']==vector
            source_word_coordinates_check(pair,actual,coords)
            for key,v in pair.fields(actual).items():assert row[key]==v
            assert positive_costs(word,labels)==row['costs'];budget.check()
        assert rank_low([r['vector60'] for r in source_basis])==rank
        for row,provided in zip(known,saved['known_words']):
            reduction=provided['linear_reduction'];assert reduction['remainder_bits']==0
            assert xor_mask(vectors,reduction['known_word_mask'])==row['coordinates']['vector60']
            value=row['coordinates']['vector60'];source_mask=0
            for basis in source_basis:
                if (value>>basis['pivot'])&1:
                    value^=basis['vector60'];source_mask^=basis['known_word_mask']
            assert value==0 and source_mask==reduction['known_word_mask']
            row['linear_reduction']=reduction
        stage('all6369_source_vectors_and_complete_span_verified',dict(known_words=known,source_basis=source_basis))
        budget.phase='all32 reference projections and64 full targets'
        cases=[]
        assert len(saved['cases'])==32
        assert saved['selected_case_ids']==[[r['source_mask'],r['coset_bits']] for _,r in chosen]
        source_vectors=[r['vector60'] for r in source_basis]
        for (case_index,reference),reported in zip(chosen,saved['cases']):
            ref={k:v for k,v in reference.items() if k!='next_half'}
            assert reported['reference']==ref and reported['source_case_index']==case_index
            assert reported['source_mask']==reference['source_mask'] and reported['coset_bits']==reference['coset_bits']
            literal=reference['literal_word']
            assert all(0<=i<4193 and 0<e<960 for i,e in literal)
            assert 374+sum(labels[i]['trace_degree']*e for i,e in literal)==reference['costs']['trace_degree']
            assert 4+sum(e for i,e in literal if labels[i]['kind']=='endpoint')==reference['costs']['endpoint_exponent']
            data,columns,beta2,gamma3=reference_data_columns(reference,ambient)
            assert reported['data']==data and reported['columns']==columns
            projected=[]
            for index,row in enumerate(source_basis):
                value=bits(ambient.response(row['vector60'],beta2,gamma3)[0])
                assert value==xor_mask([c['image_bits'] for c in columns],row['vector60'])
                projected.append(dict(source_basis_index=index,vector60=row['vector60'],image_bits=value))
            assert reported['projected_generators']==projected
            image_values=[r['image_bits'] for r in projected]
            pr=rank_low(image_values)
            assert pr==reported['rank']==len(reported['basis'])
            pb=reported['basis'];pivots_list=[r['pivot'] for r in pb]
            assert pivots_list==sorted(set(pivots_list),reverse=True)
            for row in pb:
                value=xor_mask(image_values,row['source_mask'])
                assert value==row['image_bits'] and value.bit_length()-1==row['pivot']
            assert rank_low([r['image_bits'] for r in pb])==pr
            assert len(reported['basis_reductions'])==rank
            for index,reduction in enumerate(reported['basis_reductions']):
                assert reduction['source_basis_index']==index and reduction['remainder_bits']==0
                assert xor_mask(image_values,reduction['source_mask'])==image_values[index]
                rest=image_values[index];normal_mask=0
                for basis in pb:
                    if (rest>>basis['pivot'])&1:
                        rest^=basis['image_bits'];normal_mask^=basis['source_mask']
                assert rest==0 and normal_mask==reduction['source_mask']
            decisions={}
            for name,target in data['normalized_targets_bits'].items():
                decision=reported['targets'][name]
                member=rank_low(image_values+[target])==pr
                assert decision['target_bits']==target and decision['member']==member
                mask=decision['source_mask'];value=xor_mask(image_values,mask)
                remainder=target^value
                assert remainder==decision['normal_remainder_bits']
                assert all(((remainder>>p)&1)==0 for p in pivots_list)
                rest=target;normal_mask=0
                for basis in pb:
                    if (rest>>basis['pivot'])&1:
                        rest^=basis['image_bits'];normal_mask^=basis['source_mask']
                assert rest==remainder and normal_mask==mask
                if not member:
                    sep=decision['separator_bits'];assert type(sep) is int and 0<=sep<1<<112
                    assert all((sep&v).bit_count()%2==0 for v in image_values)
                    assert (sep&target).bit_count()%2==1
                else:
                    assert remainder==0
                    correction=decision['correction'];word={}
                    for i in set_bits(mask):word=word_add(word,decoded(source_basis[i]['word']))
                    assert encoded(word)==correction['word']
                    actual=word_source(word);coords=pair.coordinates(actual)
                    assert coords['vector60']==xor_mask(source_vectors,mask)==correction['coordinates']['vector60']
                    assert coords==correction['coordinates'];source_word_coordinates_check(pair,actual,coords)
                    for key,v in pair.fields(actual).items():assert correction[key]==v
                    assert bits(ambient.response(coords['vector60'],beta2,gamma3)[0])==target
                    costs=positive_costs(word,labels);assert costs==correction['costs']
                    original_degree=reference['costs']['trace_degree']+costs['kernel_trace_degree']
                    tc=Counter({r['order']:r['multiplicity'] for r in reference['costs']['complete_trace_factors']})
                    rc=Counter({r['order']:r['multiplicity'] for r in reference['costs']['complete_reciprocal_factors']})
                    tc.update({r['order']:r['multiplicity'] for r in costs['complete_trace_factors']})
                    rc.update({r['order']:r['multiplicity'] for r in costs['complete_reciprocal_factors']})
                    endpoint=reference['costs']['endpoint_exponent']+costs['endpoint_exponent']
                    assert original_degree==endpoint+sum(e*int(sp.totient(n))//2 for n,e in tc.items())
                    assert 2*original_degree==sum(e*int(sp.totient(n)) for n,e in rc.items())
                    assert correction['resulting_original_trace_degree']==original_degree
                    assert correction['resulting_reciprocal_degree']==2*original_degree
                    assert correction['resulting_endpoint_exponent']==endpoint
                    assert correction['resulting_complete_trace_factors']==[dict(order=n,multiplicity=e) for n,e in sorted(tc.items())]
                    assert correction['resulting_complete_reciprocal_factors']==[dict(order=n,multiplicity=e) for n,e in sorted(rc.items())]
                decisions[name]=decision
            outcome='actual_positive_correction' if any(d['member'] for d in decisions.values()) else 'nonmember_in_old_alphabet_correction_image'
            assert reported['outcome']==outcome
            cases.append(dict(reported));budget.check()
            print(json.dumps(dict(source_mask=reference['source_mask'],coset_bits=reference['coset_bits'],
                verified_rank=pr,verified_members={n:r['member'] for n,r in decisions.items()})),flush=True)
        summary=dict(generator_count=4193,actual_source_value_count=8386,odd_lift_count=45,principal_lift_count=92,
            relation_count=6310,basis_lift_count=59,known_word_count=6369,source_rank=rank,reference_count=32,target_count=64,
            projected_ranks={str(k):v for k,v in Counter(r['rank'] for r in cases).items()},
            member_target_count=sum(d['member'] for r in cases for d in r['targets'].values()),
            nonmember_target_count=sum(not d['member'] for r in cases for d in r['targets'].values()),
            full_M_exclusion_claim=False,no_new_original_residual_probe=True)
        assert summary==saved['summary']
        for flag in ('all_adopted_input_math_bindings_checked','all6310_literal_recipes_checked',
            'all59_basis_construction_words_checked','all6369_Theta_identities_checked','all_source_span_inclusions_checked',
            'all_projected_span_inclusions_checked','all64_full_target_preimages_or_separators_checked',
            'all_positive_word_actual_sources_and_complete_costs_checked','actual_epsilon_integer_carry_retained',
            'old_BF_weights_not_used','actual_q_not_residue_degrees','all_final_word_exponents_mod960',
            'no_full_polynomial_expansion','no_new_original_residual_probe','no_larger_modulus_profile_or_word_optimization'):
            assert saved[flag]
        result=dict(scope='Different AUTHOR complete old4193-label actual two-source word span and64 full targets',
            required_inputs=INPUTS,parameters=params,base=screen['base'],summary=summary,generators=generators,
            odd_lifts=odd_lifts,principal_lifts=principal_lifts,relations=relations,basis_lifts=basis_lifts,
            known_words=known,source_basis=source_basis,cases=cases,selected_case_ids=saved['selected_case_ids'],
            all8386_raw_sources_independently_reconstructed=True,
            faithful_Laurent_degrees=dict(binary_p28=112,mixed_B5=72),
            canonical_epsilon_low36_high24_carry_checked=True,all_source_units_and_old_projections_checked=True,
            all6310_literal_recipes_and59_basis_dependencies_checked=True,
            all6369_actual_Theta_kernel_word_bindings_checked=True,
            theta_identities_use_adopted_C875_injection_and_literal_mod960_binding=True,
            both_actual_source_span_inclusions_checked=True,all32_reference_arrays_and64_full_targets_checked=True,
            all_positive_correction_raw_sources_and_full_costs_checked=True,
            all_projected_span_inclusions_and_target_certificates_checked=True,
            old_BF_weights_not_used=True,no_three_full_J_weight_recomputation=True,
            no_new_original_residual_probe=True,full_M_exclusion_claim=False,
            no_full_polynomial_expansion=True,no_larger_modulus_profile_or_word_optimization=True,
            arithmetic='faithful binary Phi5^28 Laurent source; faithful mixed Phi3^4Phi192/+2Phi3^24 and actual epsilon integer lifts; separate low-pivot ranks; direct SymPy full response projection',
            author_self_check=True,independent_review=False,sympy_version=sp.__version__,resources=budget.check())
        publish(args.output,result,budget)
        if checkpoint.exists():checkpoint.unlink()
        print(json.dumps(summary),flush=True)
    except Exception as error:
        progress.update(complete=False,failure_type=type(error).__name__,failure=str(error),phase=budget.phase)
        publish(checkpoint,progress)
        raise


if __name__=='__main__':
    main()
