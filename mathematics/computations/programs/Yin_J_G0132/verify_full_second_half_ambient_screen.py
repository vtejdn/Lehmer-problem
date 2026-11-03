"""Different AUTHOR full112-bit second-half ambient verification, all32 refs.

Implementation only until the new source-bound theorem is adopted and a run
is explicitly authorized.  Read adopted C878 arrays; do not recompute original
weights or residuals.  SymPy ZZ reconstructs delta, and GF(2) polynomials and
DomainMatrix independently reconstruct all60 columns and both FULL targets.
The canonical epsilon-polynomial w/s conventions are retained literally.
"""
from pathlib import Path
import argparse
import json
from collections import Counter
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from verify_positive_word_residuals import trace_factor, coefficients, binary_diagnostic, x


INPUTS = ['complete_four_coset_next_half_screen.json',
          'complete_four_coset_next_half_screen_verification.json']


def poly(values,modulus=2):
    return sp.Poly.from_list(list(reversed(values)),x,
                            **({'modulus':modulus} if modulus else {'domain':sp.ZZ}))


def bit_poly(value):
    assert type(value) is int and value>=0
    return sp.Poly.from_dict({(i,):1 for i in range(value.bit_length()) if (value>>i)&1},x,modulus=2)


def bits(value):
    return sum((int(value.nth(i))%2)<<i for i in range(int(value.degree())+1)) if not value.is_zero else 0


def binary_rref(columns,height=112):
    matrix = sp.Matrix(height,len(columns),lambda i,j:(columns[j]>>i)&1)
    reduced,pivots = DomainMatrix.from_Matrix(matrix).convert_to(sp.GF(2)).rref()
    return reduced.to_Matrix(),tuple(int(i) for i in pivots)


def xor_columns(columns,mask):
    assert type(mask) is int and 0<=mask<1<<60 and len(columns)==60
    value=0
    for i,column in enumerate(columns):
        if (mask>>i)&1:value^=column
    return value


def bind_inputs(out):
    source,verified=[json.loads((out/n).read_text(encoding='utf-8')) for n in INPUTS]
    assert source['summary']==verified['summary']
    assert source['base']==verified['base']
    assert source['fibers']==verified['fibers']
    assert source['masks']==verified['masks'] and len(source['masks'])==16
    assert source['nullspace_certificate']==verified['nullspace_certificate']
    assert verified['all448_original_mod8_arrays_checked']
    assert verified['all64_four_coset_bindings_independently_derived']
    assert verified['true_full_Z_base_and_J_prime_divisions_checked']
    assert verified['all_required_factors_powers_and_bundle_weights_checked']
    assert verified['all64_next_half_targets_and_all256_images_checked']
    assert len(source['cases'])==len(verified['cases'])==64
    lookup={(r['source_mask'],r['coset_bits']):r for r in verified['cases']}
    assert len(lookup)==64
    assert [(r['source_mask'],r['coset_bits']) for r in source['cases']]==[(m,c) for m in source['masks'] for c in range(4)]
    selected=[]
    for case in source['cases']:
        key=case['source_mask'],case['coset_bits']
        prior=lookup[key]
        assert {k:v for k,v in case.items() if k!='next_half'}=={k:v for k,v in prior.items() if k!='next_half'}
        for field in ('outcome','rank','columns','all256_source_images','genuine_half_arrays_mod4',
                      'beta_R30_bits','gamma_R32_bits','coefficient_classes_R4'):
            assert case['next_half'][field]==prior['next_half'][field]
        for name in ('X_plus','X_minus'):
            for field in ('target_bits','member','matching_source_masks'):
                assert case['next_half']['targets'][name][field]==prior['next_half']['targets'][name][field]
        if case['next_half']['outcome']=='unresolved_ambient_member':
            selected.append(case)
    assert len(selected)==32
    assert Counter(r['source_mask'] for r in selected)=={m:2 for m in source['masks']}
    return source,verified,selected


class FullAmbient:
    def __init__(self,base):
        factors={n:trace_factor(n) for n in (3,5,9,11,15,17,187,960)}
        self.P,self.V=factors[15],factors[960]
        self.J=self.P**4*self.V
        self.H=(sp.Poly((x-2)**2,x)*factors[3]**2*factors[5]**3*factors[9]**4
                *factors[11]*factors[17]*factors[187])
        self.T=self.J*self.H**2
        difference=self.V-self.P**32
        assert all(int(c)%2==0 for c in difference.all_coeffs())
        self.delta=sp.Poly.from_dict({m:int(c)//2 for m,c in difference.terms()},x,domain=sp.ZZ)
        expected=dict(P=coefficients(self.P),V=coefficients(self.V),J=coefficients(self.J),
                      H0=coefficients(self.H),T0=coefficients(self.T),delta=coefficients(self.delta))
        for k,v in expected.items():assert base[k]==v,k
        assert self.J.degree()==144 and self.V.degree()==128 and self.T.degree()==374
        self.f=poly(coefficients(self.P));self.f8=self.f**8;self.f14=self.f**14;self.f28=self.f**28
        assert poly(coefficients(self.J))==self.f**36
        self.delta_bar=poly(coefficients(self.delta)).rem(self.f28)
        self.p=sp.Poly(x*x+x+1,x,modulus=2)
        self.lam=sp.Poly(x**3+x,x,modulus=2)
        self.chi=sp.Poly(x*(x*x+x+1)**2,x,modulus=2)
        self.epsilon_image=self.chi+sp.Poly(1,x,modulus=2)
        self.p14=(self.p**14).rem(self.f14)
        self.xplus28=(sp.Poly(x+1,x,modulus=2)**28).rem(self.f28)
        self.f18=(self.f**18).rem(self.f28)
        self.f4=self.f**4

    def source_polynomials(self,mask):
        assert type(mask) is int and 0<=mask<1<<60
        r=bit_poly(mask&((1<<28)-1))
        wmask=(mask>>28)&255
        smask=mask>>36
        zero=sp.Poly(0,x,modulus=2)
        # Fixed canonical epsilon-polynomials, not arbitrary quotient lifts.
        w=sum((sp.Poly((x+1)**j,x,modulus=2) for j in range(8) if (wmask>>j)&1),zero)
        s=sum((sp.Poly((x+1)**j,x,modulus=2) for j in range(24) if (smask>>j)&1),zero)
        return r,w,s

    def response(self,mask,beta_squared,gamma_cubed):
        r,w,s=self.source_polynomials(mask)
        U=(self.p14*r.compose(self.lam)).rem(self.f14)
        # w/s are evaluated as the full fixed epsilon-polynomials before reduction.
        W=w.compose(self.chi).rem(self.f28)
        S=s.compose(self.chi).rem(self.f28)
        value=(beta_squared*(self.delta_bar*U**2+self.f18*U)
               +gamma_cubed*(self.delta_bar*self.xplus28*W+self.f4*S)).rem(self.f28)
        return value,U,W,S

    def compute_case(self,case):
        arrays=case['original_restrictions_mod8']
        assert set(arrays)=={'a','b','c','F','G','X_plus','X_minus'}
        assert all(type(c) is int and 0<=c<8 for row in arrays.values() for c in row)
        gates={f'{name}_mod{m}':all(c%m==0 for c in arrays[name])
               for name in ('F','X_plus','X_minus') for m in (2,4,8)}
        gates['G_nonzero_mod2']=any(c%2 for c in arrays['G'])
        assert gates==case['gates'] and gates['F_mod8'] and gates['X_plus_mod2'] and gates['X_minus_mod2']
        assert gates['G_nonzero_mod2']
        for name,expected in (('a',8),('b',6),('c',4),('G',12)):
            assert binary_diagnostic(arrays[name],self.f)[0]==expected
        beta=poly(arrays['b']).exquo(self.f**6)
        gamma=poly(arrays['c']).exquo(self.f**4)
        beta_squared=(beta**2).rem(self.f28)
        gamma_cubed=(gamma**3).rem(self.f28)
        halves={};targets={}
        for name in ('X_plus','X_minus'):
            halves[name]=[c//2 for c in arrays[name]]
            normalized=poly(halves[name]).exquo(self.f8)
            assert normalized.degree()<112 or normalized.is_zero
            targets[name]=bits(normalized.rem(self.f28))
        difference=(poly(halves['X_plus'])+poly(halves['X_minus'])).rem(self.f**36)
        assert difference==poly(arrays['G'])
        g_normalized=poly(arrays['G']).exquo(self.f8).rem(self.f28)
        assert not g_normalized.is_zero
        columns=[]
        for index in range(60):
            value,U,W,S=self.response(1<<index,beta_squared,gamma_cubed)
            block,power=('r',index) if index<28 else (('w',index-28) if index<36 else ('s',index-36))
            source=self.source_polynomials(1<<index)
            column=dict(index=index,block=block,power=power,source_mask=1<<index,
                        source_polynomial_bits=bits(source[{'r':0,'w':1,'s':2}[block]]),
                        U_bits=bits(U),w_chi_bits=bits(W),s_chi_bits=bits(S),image_bits=bits(value))
            columns.append(column)
        values=[r['image_bits'] for r in columns]
        assert values[36]==bits(g_normalized)==targets['X_plus']^targets['X_minus']
        reduced,pivots=binary_rref(values)
        decisions={}
        for name,target in targets.items():
            _,aug=binary_rref(values+[target])
            decisions[name]=dict(target_bits=target,member=(len(aug)==len(pivots)),augmented_rank=len(aug))
        assert decisions['X_plus']['member']==decisions['X_minus']['member']
        return dict(gates=gates,beta_R30_bits=bits(beta),gamma_R32_bits=bits(gamma),
            coefficient_classes_R28=dict(delta_bits=bits(self.delta_bar),beta_squared_bits=bits(beta_squared),gamma_cubed_bits=bits(gamma_cubed)),
            genuine_half_arrays_mod4=halves,columns=columns,rank=len(pivots),
            matrix_pivot_columns=list(pivots),matrix_rref_mod2=[[int(reduced[i,j])%2 for j in range(60)] for i in range(112)],
            targets=decisions,sign_translation_bits=bits(g_normalized),sign_translation_source_mask=1<<36,
            outcome=('unresolved_ambient_member' if decisions['X_plus']['member'] else 'entire_Theta_fiber_excluded'))


def check_span(ambient,own,basis,column_reductions,decisions):
    """Check a complete source-tracked image basis and both target certificates."""
    columns=[r['image_bits'] for r in own['columns']]
    beta2=bit_poly(own['coefficient_classes_R28']['beta_squared_bits'])
    gamma3=bit_poly(own['coefficient_classes_R28']['gamma_cubed_bits'])
    assert len(basis)==own['rank']
    pivots=[r['pivot'] for r in basis]
    assert pivots==sorted(set(pivots),reverse=True)
    for row in basis:
        source=row['source_mask']
        assert type(source) is int and 0<=source<1<<60
        value=bits(ambient.response(source,beta2,gamma3)[0])
        assert value==row['image_bits']==xor_columns(columns,source)
        assert row['pivot']==value.bit_length()-1
    assert len(binary_rref([r['image_bits'] for r in basis])[1])==own['rank']
    assert len(column_reductions)==60
    for index,record in enumerate(column_reductions):
        source=record['source_mask']
        assert record['index']==index
        assert record['remainder_bits']==0
        assert xor_columns(columns,source)==columns[index]
        # The complete source certificate, not a rank assertion alone, pays
        # containment of every original column in the recorded image basis.
        value=word=0
        residual=columns[index]
        for row in basis:
            if (residual>>row['pivot'])&1:
                residual^=row['image_bits'];value^=row['image_bits'];word^=row['source_mask']
        assert residual==0 and value==columns[index] and word==source
    for name,computed in own['targets'].items():
        decision=decisions[name]
        assert decision['target_bits']==computed['target_bits']
        assert decision['member']==computed['member']
        normal_source=decision['normal_source_mask']
        assert decision['normal_source_coordinates']==dict(
            r_coefficients_bits=normal_source&((1<<28)-1),
            w_epsilon_coefficients_bits=(normal_source>>28)&255,
            s_epsilon_coefficients_bits=normal_source>>36)
        value=bits(ambient.response(normal_source,beta2,gamma3)[0])
        assert value==xor_columns(columns,normal_source)
        remainder=computed['target_bits']^value
        assert remainder==decision['normal_remainder_bits']
        assert all(((remainder>>p)&1)==0 for p in pivots)
        if computed['member']:
            assert remainder==0
        else:
            separator=decision['separator_bits']
            assert type(separator) is int and 0<=separator<1<<112
            assert all((separator&column).bit_count()%2==0 for column in columns)
            assert (separator&computed['target_bits']).bit_count()%2==1
    assert decisions['X_plus']['normal_remainder_bits']==decisions['X_minus']['normal_remainder_bits']
    if own['targets']['X_plus']['member']:
        translated=decisions['X_plus']['normal_source_mask']^(1<<36)
        assert decisions['X_minus']['translated_plus_ambient_preimage']==translated
        assert bits(ambient.response(translated,beta2,gamma3)[0])==own['targets']['X_minus']['target_bits']


def main():
    here=Path(__file__).resolve().parent
    out=here.parents[1]/'outputs'/here.name
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--result',type=Path,default=out/'full_second_half_ambient_screen.json')
    parser.add_argument('--output',type=Path,default=out/'full_second_half_ambient_screen_verification.json')
    args=parser.parse_args()
    source,prior,selected=bind_inputs(out)
    saved=json.loads(args.result.read_text(encoding='utf-8'))
    assert saved['required_inputs']==INPUTS
    assert saved['base']==source['base']
    assert saved['source_basis_order']==dict(r='Y^j,0<=j<28',w='(Y+1)^j,0<=j<8',s='(Y+1)^j,0<=j<24')
    assert saved['source_block_offsets']==dict(r=0,w=28,s=36)
    assert saved['source_dimension']==60 and saved['target_dimension']==112
    ambient=FullAmbient(source['base'])
    ids=[[r['source_mask'],r['coset_bits']] for r in selected]
    assert len(ids)==len({tuple(i) for i in ids})==32
    assert saved['selected_case_ids']==ids and len(saved['cases'])==32
    index_lookup={(r['source_mask'],r['coset_bits']):i for i,r in enumerate(source['cases'])}
    cases=[]
    for case,reported in zip(selected,saved['cases']):
        mask,coset=case['source_mask'],case['coset_bits']
        assert reported['source_mask']==mask and reported['coset_bits']==coset
        assert reported['source_case_index']==index_lookup[mask,coset]
        reference={k:v for k,v in case.items() if k!='next_half'}
        assert reported['reference']==reference
        own=ambient.compute_case(case)
        data=dict(genuine_half_arrays_mod4=own['genuine_half_arrays_mod4'],
            full_half_bits={n:bits(poly(a)) for n,a in own['genuine_half_arrays_mod4'].items()},
            normalized_targets_bits={n:r['target_bits'] for n,r in own['targets'].items()},
            beta_bits=own['beta_R30_bits'],gamma_bits=own['gamma_R32_bits'],
            beta_squared_R28=own['coefficient_classes_R28']['beta_squared_bits'],
            gamma_cubed_R28=own['coefficient_classes_R28']['gamma_cubed_bits'],
            delta_R28=own['coefficient_classes_R28']['delta_bits'],
            target_difference_R28=own['sign_translation_bits'],G_div_f8_R28=own['sign_translation_bits'])
        assert reported['data']==data
        assert reported['columns']==own['columns'] and reported['rank']==own['rank']
        check_span(ambient,own,reported['basis'],reported['column_reductions'],reported['targets'])
        assert reported['sign_consistency']==dict(source_mask=1<<36,
            image_bits=own['sign_translation_bits'],membership_equal=True)
        assert reported['outcome']==own['outcome']
        cases.append(dict(source_mask=mask,coset_bits=coset,source_case_index=index_lookup[mask,coset],
            reference=reference,data=data,columns=own['columns'],rank=own['rank'],
            matrix_pivot_columns=own['matrix_pivot_columns'],matrix_rref_mod2=own['matrix_rref_mod2'],
            basis=reported['basis'],column_reductions=reported['column_reductions'],
            targets=reported['targets'],independent_target_ranks={n:r['augmented_rank'] for n,r in own['targets'].items()},
            sign_consistency=reported['sign_consistency'],outcome=own['outcome']))
        print(json.dumps(dict(source_mask=mask,coset_bits=coset,verified_rank=own['rank'],
                              verified_outcome=own['outcome'])),flush=True)
    fibers=[]
    for mask in source['masks']:
        rows=[r for r in cases if r['source_mask']==mask]
        assert len(rows)==2
        survivors=[r['coset_bits'] for r in rows if r['outcome']=='unresolved_ambient_member']
        fibers.append(dict(source_mask=mask,remaining_Theta_cosets=survivors,whole_old_fiber_excluded=not survivors))
    assert saved['old_fibers']==fibers
    counts=Counter(r['outcome'] for r in cases)
    summary=dict(reference_count=32,target_count=64,column_count=1920,
        outcome_counts=dict(counts),negative_target_count=2*counts['entire_Theta_fiber_excluded'],
        ambient_member_target_count=2*counts['unresolved_ambient_member'],
        ranks={str(k):v for k,v in Counter(r['rank'] for r in cases).items()},
        additional_excluded_old_masks=[r['source_mask'] for r in fibers if r['whole_old_fiber_excluded']],
        unresolved_old_masks=[r['source_mask'] for r in fibers if not r['whole_old_fiber_excluded']],
        whole_fixed_family_joint_F8_either_X4_excluded=all(r['outcome']=='entire_Theta_fiber_excluded' for r in cases))
    assert saved['summary']==summary
    for flag in ('all32_original_reference_bindings_checked','all64_full_targets_checked',
                 'all1920_columns_and_both_span_inclusions_checked','fixed_canonical_epsilon_lifts',
                 'genuine_halves_before_binary_division','both_distinct_targets_and_ambient_sign_translation_checked',
                 'no_2power60_enumeration','no_actual_cofactor_attainment_claim','no_new_group_or_weight_image',
                 'no_new_original_residual_probe','no_larger_modulus_or_profile','no_F_over8_class_or_mod16'):
        assert saved[flag]
    result=dict(scope='Different AUTHOR complete32 full112-bit second-half ambient screen',
        required_inputs=INPUTS,selected_case_ids=ids,base=source['base'],cases=cases,old_fibers=fibers,summary=summary,
        all32_adopted_reference_array_bindings_checked=True,actual_integer_P_V_delta_reconstructed=True,
        all1920_full_columns_and_canonical_source_representatives_checked=True,
        all64_full112_target_classes_and_memberships_checked=True,
        all_basis_provenance_and_both_span_inclusions_checked=True,
        all_positive_source_words_or_negative_separators_checked=True,
        all_s1_G_over_f8_sign_translations_checked=True,
        arithmetic='SymPy ZZ full primitive traces and genuine delta half; GF(2) canonical polynomial composition; DomainMatrix GF(2) full ranks; direct source-word checks',
        sympy_version=sp.__version__,author_self_check=True,independent_review=False,
        no_original_residual_recalculation=True,no_new_cofactor_image=True,
        no_two_to_sixty_enumeration=True,no_higher_modulus_or_profile=True,
        ambient_membership_is_not_actual_attainment=True)
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
