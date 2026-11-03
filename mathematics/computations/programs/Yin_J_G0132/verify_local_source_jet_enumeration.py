"""Different AUTHOR check of every one of the10240 LOCAL pairs.

Rebuild true integer b0,c0 at full T187 before scalar division and restriction.
Use SymPy polynomial arithmetic and a low-pivot source-image elimination.
No producer arithmetic or enumeration code is imported.
"""
from pathlib import Path
import json
import sympy as sp
from verify_odd_support import C, x, trace_factor, coefficients
from verify_first_gate_character import bits, binary_poly, powmod


def main():
    here=Path(__file__).resolve().parent
    output=here.parents[3]/'mathematics/computations/outputs'/here.name
    saved=json.loads((output/'local_source_jet_enumeration.json').read_text(encoding='utf-8'))
    assert saved['source_count']==2048 and saved['branch_count']==5 and saved['pair_count']==10240
    f=sp.Poly(x**4+x**3+1,x,modulus=2)
    phi=sp.Poly(x**2+x+1,x,modulus=2)
    one=sp.Poly(1,x,modulus=2)
    m7,m12,m14,m18,m24,m30=[f**j for j in (7,12,14,18,24,30)]
    while len(C)<=128:
        C.append(sp.Poly(x,x,domain=sp.ZZ)*C[-1]-C[-2])
    factors={n:trace_factor(n) for n in (3,5,9,11,15,17,187,480,960)}
    h0=(sp.Poly((x-2)**2,x)*factors[3]**2*factors[5]**3*factors[9]**4
        *factors[11]*factors[17]*factors[187])
    j0=factors[15]**2*factors[480]
    t0=j0*h0
    assert h0.degree()==115 and j0.degree()==72 and t0.degree()==187
    actual={}
    for p in (3,5):
        numerator=t0.compose(C[p]).rem(t0)
        assert all(int(v)%p==0 for v in numerator.all_coeffs())
        canonical=sp.Poly.from_list([int(v)//p for v in numerator.all_coeffs()],x,domain=sp.ZZ)
        actual[p]=canonical.rem(j0)
    b0,c0=[sp.Poly(actual[p],x,modulus=2) for p in (3,5)]
    beta_old=b0.exquo(f**3)
    gamma=c0.exquo(f**2)
    beta2=(beta_old**2).rem(m30)
    delta_diff=factors[480]-factors[15]**16
    assert all(int(v)%2==0 for v in delta_diff.all_coeffs())
    delta_int=sp.Poly.from_list([int(v)//2 for v in delta_diff.all_coeffs()],x,domain=sp.ZZ)
    delta=sp.Poly(delta_int,x,modulus=2)
    h0bar=sp.Poly(h0,x,modulus=2)
    t=(h0bar*delta).rem(m7)
    d=sp.Poly(x**12*(1+x)**16,x,modulus=2).rem(m7)
    old_k=(d*powmod(t,5,m7)*sp.invert(gamma.rem(m7),m7)).rem(m7)
    target=(old_k**2).rem(m14)
    base=saved['actual_base']
    expected=dict(U0=bits(sp.Poly(t0,x,modulus=2)),H0=bits(h0bar),b0_binary=bits(b0),c0_binary=bits(c0),
                  beta_old=bits(beta_old),beta2=bits(beta2),gamma_old=bits(gamma),t_old=bits(t),
                  delta16_integer=coefficients(delta_int),delta16_binary=bits(delta),old_kappa=bits(old_k),K=bits(target))
    expected['delta16_integer'] += [0]*(len(base['delta16_integer'])-len(expected['delta16_integer']))
    assert base==expected, [key for key in expected if base[key]!=expected[key]]
    # Confirm actual doubled lift distinction, without constructing any new cofactor.
    assert factors[960]==factors[480].compose(C[2]) and factors[960]!=factors[480]**2
    dd=factors[960]-factors[15]**32
    assert all(int(v)%2==0 for v in dd.all_coeffs())
    delta32=sp.Poly.from_list([int(v)//2 for v in dd.all_coeffs()],x,domain=sp.ZZ)
    assert sp.Poly(delta32,x,modulus=2)==delta**2
    lam,chi=[sp.Poly(C[p],x,modulus=2) for p in (3,5)]
    assert bits(lam)==saved['lambda_polynomial'] and bits(chi)==saved['chi_polynomial']
    assert chi+one==sp.Poly(x+1,x,modulus=2)*f
    assert phi.compose(lam)==phi*f
    target_inverse=sp.invert(target,m14)
    beta_inverse=sp.invert(beta2.rem(m12),m12)
    gamma3=powmod(gamma.rem(m12),3,m12)
    t2=(t**2).rem(m12)
    tau=powmod(sp.Poly(x,x,modulus=2),16,m14)
    branches=[powmod(tau,3*j,m14) for j in range(5)]
    assert len({bits(v) for v in branches})==5 and powmod(tau,15,m14)==one
    basis,source_basis=[],[]
    for k in range(12):
        for epsilon in (0,1):
            src=sp.Poly(x**epsilon,x,modulus=2)*phi**k
            source_basis.append(src)
            basis.append(src.compose(lam).rem(m12))
    assert [bits(v) for v in basis]==saved['source_image_basis']
    assert [bits(v) for v in source_basis]==saved['source_polynomial_basis']
    # Independently eliminate48 coefficient rows with LOW, not high, pivots.
    low_pivots={}
    for i,column in enumerate(basis):
        vector=[int(column.nth(j))%2 for j in range(48)]
        coordinates=[int(i==j) for j in range(24)]
        for j in range(48):
            if vector[j]:
                if j not in low_pivots:
                    low_pivots[j]=(vector,coordinates)
                    break
                v,c=low_pivots[j]
                vector=[a^b for a,b in zip(vector,v)]
                coordinates=[a^b for a,b in zip(coordinates,c)]
        else:
            raise AssertionError('Source-image columns must be independent')
    assert len(low_pivots)==saved['image_rank']==24

    def recover(value):
        vector=[int(value.nth(i))%2 for i in range(48)]
        coordinates=[0]*24
        for j,(v,c) in sorted(low_pivots.items()):
            if vector[j]:
                vector=[a^b for a,b in zip(vector,v)]
                coordinates=[a^b for a,b in zip(coordinates,c)]
        if any(vector):
            return None
        src=sp.Poly(0,x,modulus=2)
        for bit,column in zip(coordinates,source_basis):
            if bit:
                src+=column
        assert src.compose(lam).rem(m12)==value
        return src

    # Check the producer's DIFFERENT high-pivot recovery data without adopting it.
    for row in saved['image_pivots']:
        value=sp.Poly(0,x,modulus=2)
        for i,column in enumerate(basis):
            if row['coordinates']>>i&1:
                value+=column
        assert bits(value)==row['vector'] and value.degree()==row['position']
    source_epsilon=[sp.Poly((x+1)**k,x,modulus=2) for k in range(12)]
    substituted_epsilon=[v.compose(chi).rem(m12) for v in source_epsilon]
    assert len(saved['pairs'])==10240
    survivors=[]
    pair_checks=[]
    for mask in range(2048):
        src,s=one,one
        for k in range(1,12):
            if mask>>(k-1)&1:
                src+=source_epsilon[k]
                s+=substituted_epsilon[k]
        q3src=src**2
        q5=(s**2).rem(m24)
        assert q3src.compose(chi).rem(m24)==q5
        u=(q5.rem(m14)*target_inverse).rem(m14)
        assert u.rem(f)==one
        root=powmod(u,13,m14)
        s_cube=powmod(s,3,m12)
        for branch in range(5):
            row=saved['pairs'][5*mask+branch]
            assert row['source_mask']==mask and row['branch']==branch
            a=(branches[branch]*root).rem(m14)
            assert powmod(a,5,m14)==u
            term=(f**6*powmod((t2*a).rem(m12),3,m12)).rem(m12)
            w=(beta_inverse*(term+gamma3*s_cube)).rem(m12)
            assert w.rem(f)==one
            assert (beta2*w+term+gamma3*s_cube).rem(m12).is_zero
            assert row['source_S']==bits(src) and row['Q3_source']==bits(q3src)
            assert row['Q15']==bits(a) and row['W']==bits(w)
            high_reconstruction=sp.Poly(0,x,modulus=2)
            for i,column in enumerate(basis):
                if row['image_coordinates']>>i&1:
                    high_reconstruction+=column
            assert bits(w+high_reconstruction)==row['image_remainder']
            recovered=recover(w)
            passes=recovered is not None
            assert passes==row['passes']==(row['image_remainder']==0)
            if passes:
                assert bits(recovered)==row['Q5_source']
                assert recovered.rem(phi)==one
                # Both original NORMALIZED equations at their full precisions.
                assert (q5.rem(m14)*sp.invert(powmod(a,5,m14),m14)).rem(m14)==target
                original=(beta2**2*w**2+powmod(gamma,6,m24)*powmod(q5,3,m24)
                          +f**12*powmod(t,12,m24)*powmod(a,6,m24)).rem(m24)
                assert original.is_zero
                survivors.append(dict(row))
            pair_checks.append(dict(source_mask=mask,branch=branch,passes=passes,
                                    recovered_Q5_source=(bits(recovered) if passes else None)))
    assert survivors==saved['surviving_local_triples'] and len(survivors)==saved['survivor_count']
    assert len(pair_checks)==10240
    affine=saved['surviving_mask_affine_description']
    assert affine==dict(base=25,directions=[32,88,138,266,512,1024],branch=2)
    all_masks={affine['base']}
    for direction in affine['directions']:
        all_masks |= {m^direction for m in list(all_masks)}
    assert len(all_masks)==64 and {(r['source_mask'],r['branch']) for r in survivors}=={(m,2) for m in all_masks}
    counts={name:len({row[name] for row in survivors}) for name in ('Q15','Q3_source','Q5_source')}
    assert counts==saved['distinct_coordinate_counts']==dict(Q15=8,Q3_source=64,Q5_source=64)
    result=dict(scope='all10240 LOCAL pairs; true integer old-base constants and distinct source-image arithmetic',
                actual_full_T187_integer_b0_c0_divisions_checked=True,
                true_integer_delta16_and_single_F960_distinction_checked=True,
                actual_base_constants_match=True,source_image_rank=24,
                all10240_pair_values_and_membership_checked=True,
                all10240_prescribed_normalized_equations_checked=True,
                all_survivors_original_normalized_equations_checked=True,
                survivor_count=len(survivors),surviving_local_triples=survivors,pair_checks=pair_checks,
                surviving_mask_affine_description=affine,distinct_coordinate_counts=counts,
                actual_integer_restrictions=dict(b0=coefficients(actual[3]),c0=coefficients(actual[5]),delta16=coefficients(delta_int)),
                implementation='full-Z SymPy canonical division, F2 polynomial powers and low-pivot coefficient-list elimination',
                sympy_version=sp.__version__,author_self_check=True,independent_review=False,
                no_actual_cofactor_word_test=True,no_CRT_or_global_realization_claim=True)
    tmp=output/'local_source_jet_enumeration_verification.json.partial'
    tmp.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    tmp.replace(output/'local_source_jet_enumeration_verification.json')
    print(json.dumps({k:result[k] for k in ('actual_full_T187_integer_b0_c0_divisions_checked',
                     'source_image_rank','all10240_pair_values_and_membership_checked',
                     'all_survivors_original_normalized_equations_checked','survivor_count')}))


if __name__=='__main__':
    main()
