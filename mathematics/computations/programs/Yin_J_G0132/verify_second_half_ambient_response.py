"""Different exact SymPy verification of ONE ambient eight-bit source image.

Reconstruct F15 and F960 from full cyclotomic polynomials over ZZ.
Use the prior DIFFERENT verifier's complete original arrays, not a numerical oracle.
Evaluate all256 source polynomials directly and use DomainMatrix over GF(2).
Import no producer arithmetic; compute no original residual or cofactor image.
"""
from pathlib import Path
import argparse
import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix

X,z=sp.symbols('X z')


def trace_factor(n):
    cyclo=sp.Poly(sp.cyclotomic_poly(n,z),z,domain=sp.ZZ)
    degree=int(cyclo.degree());assert degree%2==0
    d=degree//2
    traces=[sp.Poly(2,X,domain=sp.ZZ),sp.Poly(X,X,domain=sp.ZZ)]
    for j in range(2,d+1):traces.append(sp.Poly(X,X,domain=sp.ZZ)*traces[-1]-traces[-2])
    result=sp.Poly(cyclo.nth(d),X,domain=sp.ZZ)
    for j in range(1,d+1):
        assert cyclo.nth(d+j)==cyclo.nth(d-j)
        result+=int(cyclo.nth(d+j))*traces[j]
    assert result.degree()==d and result.LC()==1
    return result


def zz_array(poly):
    if poly.is_zero:return [0]
    return [int(poly.nth(i)) for i in range(int(poly.degree())+1)]


def from_array(a,modulus=None):
    expression=sum(int(c)*X**i for i,c in enumerate(a))
    return sp.Poly(expression,X,modulus=modulus) if modulus else sp.Poly(expression,X,domain=sp.ZZ)


def encoded(poly):
    if poly.is_zero:return 0
    return sum((int(poly.nth(i))%2)*2**i for i in range(int(poly.degree())+1))


def bit_poly(value):
    return sp.Poly(sum(((value>>i)&1)*X**i for i in range(value.bit_length())),X,modulus=2)


def exact_div(poly,divisor):
    q,r=poly.div(divisor);assert r.is_zero
    return q


def gf2_rref(matrix):
    reduced,pivots=DomainMatrix.from_Matrix(matrix).convert_to(sp.GF(2)).rref()
    return reduced.to_Matrix(),tuple(int(i) for i in pivots)


def main():
    here=Path(__file__).resolve().parent
    out=here.parents[3]/'mathematics/computations/outputs'/here.name
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--result',type=Path,default=out/'second_half_ambient_response.json')
    parser.add_argument('--output',type=Path,default=out/'second_half_ambient_response_verification.json')
    args=parser.parse_args()
    original=json.loads((out/'full_eighth_positive_product_mod8.json').read_text(encoding='utf-8'))
    prior=json.loads((out/'full_eighth_positive_product_mod8_verification.json').read_text(encoding='utf-8'))
    word=json.loads((here/'inputs/full_eighth_positive_product_word.json').read_text(encoding='utf-8'))
    assert len(word['terms'])==264 and original['terms']==word['terms']
    assert word['source_mask']==819 and word['branch']==2
    assert original['costs']==prior['costs']==word['costs']
    assert prior['quotient_trace_degree']==144 and prior['Laurent_degree']==288
    assert prior['all7_full_mod8_trace_arrays_recovered_and_matched']
    assert prior['true_full_Z_base_and_J_prime_divisions_checked']
    assert prior['all792_term_values_and_powers_checked']
    assert prior['exact_single_F960_and_integral_trace_identity_checked']
    arrays=prior['original_restrictions_mod8']
    assert arrays==original['original_restrictions_mod8']
    assert set(arrays)=={'a','b','c','F','G','X_plus','X_minus'}
    assert all(type(c) is int and 0<=c<8 for a in arrays.values() for c in a)
    assert not any(arrays['F'])
    P=trace_factor(15);V=trace_factor(960)
    assert P**4*V==from_array(original['J_coefficients'])
    difference=V-P**32
    assert all(int(c)%2==0 for c in difference.all_coeffs())
    delta=sp.Poly.from_dict({monomial:int(c)//2 for monomial,c in difference.terms()},X,domain=sp.ZZ)
    f=sp.Poly(P.as_expr(),X,modulus=2);f2=f**2;f4=f**4
    assert sp.Poly(V.as_expr(),X,modulus=2)==f**32
    beta=exact_div(from_array(arrays['b'],2),f**6)
    gamma=exact_div(from_array(arrays['c'],2),f**4)
    assert not beta.rem(f).is_zero and not gamma.rem(f).is_zero
    delta_bin=sp.Poly(delta.as_expr(),X,modulus=2)
    assert not delta_bin.rem(f).is_zero
    delta4=delta_bin.rem(f4);beta2=(beta**2).rem(f4);gamma3=(gamma**3).rem(f4)
    halves={};target_polys={}
    for name in ('X_plus','X_minus'):
        assert all(c%2==0 for c in arrays[name])
        halves[name]=[int(c)//2 for c in arrays[name]]
        target_polys[name]=exact_div(from_array(halves[name],2),f4).rem(f4)
    p=sp.Poly(X**2+X+1,X,modulus=2)
    lam=sp.Poly(X**3+X,X,modulus=2)
    chi=sp.Poly(X*(X**2+X+1)**2,X,modulus=2)
    u_scale=(p**12).rem(f2)
    w_scale=(sp.Poly(X+1,X,modulus=2)**24).rem(f4)
    lam_powers=[(lam**i).rem(f2) for i in range(4)]
    chi_powers=[(chi**i).rem(f4) for i in range(4)]
    images=[];image_polys=[]
    zero=sp.Poly(0,X,modulus=2)
    for mask in range(256):
        # Direct polynomial evaluation for EACH source, not XOR of supplied columns.
        r_sub=zero;s_sub=zero
        for j in range(4):
            if (mask>>j)&1:r_sub+=lam_powers[j]
            if (mask>>(j+4))&1:s_sub+=chi_powers[j]
        u=(u_scale*r_sub).rem(f2)
        w=(w_scale*s_sub).rem(f4)
        response=(delta4*(beta2*u**2+gamma3*w)).rem(f4)
        image_polys.append(response)
        images.append(dict(source_mask=mask,r_bits=mask&15,s_bits=mask>>4,
                           u_bits=encoded(u),w_bits=encoded(w),image_bits=encoded(response)))
    columns=[dict(index=i,source=('r' if i<4 else 's'),power=i%4,**images[1<<i]) for i in range(8)]
    col_polys=[image_polys[1<<i] for i in range(8)]
    matrix=sp.Matrix(16,8,lambda row,col:int(col_polys[col].nth(row))%2)
    rref,pivots=gf2_rref(matrix);rank=len(pivots)
    target_results={};augmented_ranks={}
    for name,target in target_polys.items():
        column=sp.Matrix(16,1,lambda row,col:int(target.nth(row))%2)
        _,aug_pivots=gf2_rref(matrix.row_join(column))
        augmented_ranks[name]=len(aug_pivots)
        matches=[entry['source_mask'] for entry in images if entry['image_bits']==encoded(target)]
        assert bool(matches)==(len(aug_pivots)==rank)
        target_results[name]=dict(target_bits=encoded(target),member=bool(matches),matching_source_masks=matches)
    assert len({entry['image_bits'] for entry in images})==2**rank
    own=dict(source_costs=original['costs'],source_terms=word['terms'],
             P_coefficients=zz_array(P),V_coefficients=zz_array(V),delta_coefficients=zz_array(delta),
             f_bits=encoded(f),modulus_f4_bits=encoded(f4),beta_R30_bits=encoded(beta),gamma_R32_bits=encoded(gamma),
             coefficient_classes_R4=dict(delta_bits=encoded(delta4),beta_squared_bits=encoded(beta2),gamma_cubed_bits=encoded(gamma3)),
             genuine_integer_half_arrays_mod4=halves,columns=columns,all256_source_images=images,
             rank=rank,distinct_image_count=2**rank)
    # Only after the independent reconstruction, compare the new producer result.
    producer=json.loads(args.result.read_text(encoding='utf-8'))
    for key,value in own.items():assert producer[key]==value,key
    for name,record in target_results.items():
        for key,value in record.items():assert producer['targets'][name][key]==value,(name,key)
        supplied=producer['targets'][name]
        combination=zero
        for j in range(8):
            if (supplied['normal_source_mask']>>j)&1:combination+=col_polys[j]
        assert target_polys[name]+combination==bit_poly(supplied['normal_remainder_bits'])
        if not record['member']:
            sep=supplied['separator_bits']
            def parity(poly):return sum(((sep>>j)&1)*int(poly.nth(j)) for j in range(16))%2
            assert all(parity(poly)==0 for poly in image_polys)
            assert parity(target_polys[name])==1
    supplied_basis=producer['binary_basis']
    assert len(supplied_basis)==rank
    basis_polys=[]
    for row in supplied_basis:
        polynomial=zero
        for j in range(8):
            if (row['source_mask']>>j)&1:polynomial+=col_polys[j]
        assert encoded(polynomial)==row['image_bits']
        assert int(polynomial.degree())==row['pivot']
        basis_polys.append(polynomial)
    basis_matrix=sp.Matrix(16,len(basis_polys),lambda i,j:int(basis_polys[j].nth(i))%2)
    assert len(gf2_rref(basis_matrix)[1])==rank
    result=dict(scope='Different SymPy check: ONE literal264-term input, all8 columns, all256 images, both actual targets',
                recomputed=own,targets=target_results,ambient_matrix_pivot_columns=list(pivots),
                ambient_matrix_rref_mod2=[[int(rref[i,j])%2 for j in range(8)] for i in range(16)],
                augmented_target_ranks=augmented_ranks,
                all_integer_halves_and_cyclotomic_J_checked=True,all8_columns_and256_images_matched=True,
                complete_binary_basis_and_target_certificates_checked=True,
                arithmetic='SymPy ZZ cyclotomic trace reconstruction; Poly over GF(2); direct256 source evaluations; DomainMatrix GF(2) row reduction',
                sympy_version=sp.__version__,no_original_residual_recalculation=True,no_120bit_image=True,
                no_other_word_or_higher_modulus=True,author_self_check=True,independent_review=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    partial=args.output.with_suffix(args.output.suffix+'.partial')
    try:
        partial.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        partial.replace(args.output)
    finally:
        if partial.exists():partial.unlink()
    print(json.dumps(dict(rank=rank,distinct_images=2**rank,targets=target_results,sympy_version=sp.__version__)))


if __name__=='__main__':main()
