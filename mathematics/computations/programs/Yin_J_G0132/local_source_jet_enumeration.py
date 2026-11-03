"""Complete LOCAL enumeration: exactly2048 source square roots x5 branches.

No actual cofactor word, CRT realization, new profile or generator image is tested.
Old C860-selected files and inputs are read-only.
"""
from pathlib import Path
import json
from first_gate_character import F, rawmul, remainder, multiply, power, inverse, evaluate
from main import compose, chebyshev, power as integer_power


def divide(a, b):
    quotient = 0
    while a and a.bit_length() >= b.bit_length():
        shift = a.bit_length()-b.bit_length()
        quotient ^= 1 << shift
        a ^= b << shift
    return quotient, a


def main():
    here = Path(__file__).resolve().parent
    output = here.parents[3]/'mathematics/computations/outputs'/here.name
    mods = {0: 1}
    for j in range(1, 31):
        mods[j] = rawmul(mods[j-1], F)
    m7, m12, m14, m18, m24 = [mods[j] for j in (7, 12, 14, 18, 24)]
    x, phi, f9 = 2, 7, 11
    cheb = [0, x]
    for _ in range(2, 94):
        cheb.append(rawmul(x, cheb[-1]) ^ cheb[-2])
    lam, chi = cheb[3], cheb[5]
    assert chi ^ 1 == rawmul(x ^ 1, F)
    assert rawmul(lam,lam) ^ lam ^ 1 == rawmul(phi,F)
    b187 = 1
    for c in cheb[1:94]:
        b187 ^= c
    h0 = rawmul(rawmul(rawmul(rawmul(rawmul(x,x),rawmul(x ^ 1,x ^ 1)),
                                      rawmul(rawmul(phi,phi),phi)),
                               rawmul(rawmul(f9,f9),rawmul(f9,f9))),b187)
    u0 = rawmul(mods[18], h0)
    assert h0.bit_length()-1 == 115 and u0.bit_length()-1 == 187
    b0 = evaluate(u0, lam, m18)
    c0 = evaluate(u0, chi, m18)
    beta_old, br = divide(b0, mods[3])
    gamma, cr = divide(c0, mods[2])
    assert br == cr == 0 and remainder(beta_old,F) and remainder(gamma,F)
    # Genuine integer delta16: subtract actual integer polynomials before /2.
    ff, f30 = [1,4,-4,-1,1], [1,-4,-4,1,1]
    v16 = compose(f30, chebyshev(16))
    f16 = integer_power(ff,16)
    delta_integer = [(a-b)//2 for a,b in zip(v16,f16)]
    assert len(v16)==len(f16)==65 and all((a-b)%2==0 for a,b in zip(v16,f16))
    delta = sum((v%2)<<i for i,v in enumerate(delta_integer))
    assert delta == (1<<56) ^ (1<<24)
    t = remainder(rawmul(h0,delta),m7)
    d = remainder((1<<12) ^ (1<<28),m7)
    old_k = multiply(multiply(d,power(t,5,m7),m7),inverse(remainder(gamma,m7),m7),m7)
    target = power(old_k,2,m14)
    assert old_k==182570536 and target==19232663035708480
    beta2 = power(beta_old,2,mods[30])
    beta_inv = inverse(remainder(beta2,m12),m12)
    gamma3 = power(remainder(gamma,m12),3,m12)
    t2 = power(t,2,m12)
    tau = power(x,16,m14)
    assert power(tau,15,m14)==1 and len({power(tau,3*j,m14) for j in range(5)})==5
    target_inv = inverse(target,m14)

    # Exact24-column source-image basis, with tracked original coordinates.
    p_lam = evaluate(phi,lam,m12)
    basis = []
    source_basis = []
    for k in range(12):
        for epsilon in (0,1):
            basis.append(multiply(power(lam,epsilon,m12),power(p_lam,k,m12),m12))
            raw_pk=1
            for _ in range(k):
                raw_pk=rawmul(raw_pk,phi)
            source_basis.append(rawmul(raw_pk,x if epsilon else 1))
    pivots = {}
    for i,column in enumerate(basis):
        value, coordinates = column, 1<<i
        while value:
            bit=value.bit_length()-1
            if bit not in pivots:
                pivots[bit]=(value,coordinates)
                break
            v,c=pivots[bit]
            value ^= v
            coordinates ^= c
        assert value, 'Source injection requires24 independent columns'
    assert len(pivots)==24

    def recover(value):
        coords=0
        for bit in sorted(pivots,reverse=True):
            if value>>bit&1:
                v,c=pivots[bit]
                value ^= v
                coords ^= c
        source=0
        for i,column in enumerate(source_basis):
            if coords>>i&1:
                source ^= column
        return value,coords,source

    eps_powers=[1]
    source_powers=[1]
    for _ in range(11):
        eps_powers.append(multiply(eps_powers[-1],chi ^ 1,m12))
        source_powers.append(rawmul(source_powers[-1],x ^ 1))
    rows, survivors = [], []
    for mask in range(2048):
        s,source_s=1,1
        for k in range(1,12):
            if mask>>(k-1)&1:
                s ^= eps_powers[k]
                source_s ^= source_powers[k]
        source_square=rawmul(source_s,source_s)
        q5=rawmul(s,s)
        assert q5==evaluate(source_square,chi,m24)
        u=multiply(remainder(q5,m14),target_inv,m14)
        assert remainder(u,F)==1
        root=power(u,13,m14)
        for branch in range(5):
            a=multiply(power(tau,3*branch,m14),root,m14)
            assert power(a,5,m14)==u
            inner=multiply(t2,remainder(a,m12),m12)
            w=multiply(beta_inv,multiply(mods[6],power(inner,3,m12),m12)
                       ^ multiply(gamma3,power(s,3,m12),m12),m12)
            assert remainder(w,F)==1
            residual,coords,q5src=recover(w)
            assert evaluate(q5src,lam,m12) ^ residual == w
            row=dict(source_mask=mask,branch=branch,source_S=source_s,
                     Q15=a,Q3_source=source_square,W=w,
                     image_remainder=residual,image_coordinates=coords,passes=residual==0)
            if residual==0:
                row['Q5_source']=q5src
                assert evaluate(q5src,lam,m12)==w
                # Both original normalized equations, including precision24.
                assert multiply(remainder(q5,m14),inverse(power(a,5,m14),m14),m14)==target
                normalized=(multiply(power(beta2,2,m24),power(w,2,m24),m24)
                            ^ multiply(power(gamma,6,m24),power(q5,3,m24),m24)
                            ^ multiply(mods[12],power(multiply(power(t,4,m24),power(a,2,m24),m24),3,m24),m24))
                assert normalized==0
                survivors.append(dict(row))
            rows.append(row)
    assert len(rows)==10240 and {(r['source_mask'],r['branch']) for r in rows}=={(m,j) for m in range(2048) for j in range(5)}
    # A compact description of the ALREADY enumerated surviving masks.
    directions=[32,88,138,266,512,1024]
    affine=[]
    for choice in range(64):
        value=25
        for i,direction in enumerate(directions):
            if choice>>i&1:
                value ^= direction
        affine.append(value)
    assert len(set(affine))==64
    assert {(r['source_mask'],r['branch']) for r in survivors}=={(m,2) for m in affine}
    result=dict(scope='exactly2048 source units times5 branches; LOCAL triples only, no cofactor realization',
                source_count=2048,branch_count=5,pair_count=10240,
                coefficient_encoding='bit i is coefficient of X^i, or Y^i for source fields, over F2',
                f=F,moduli=mods,lambda_polynomial=lam,chi_polynomial=chi,
                actual_base=dict(U0=u0,H0=h0,b0_binary=b0,c0_binary=c0,
                    beta_old=beta_old,beta2=beta2,gamma_old=gamma,t_old=t,
                    delta16_integer=delta_integer,delta16_binary=delta,old_kappa=old_k,K=target),
                source_image_basis=basis,source_polynomial_basis=source_basis,
                image_rank=24,image_pivots=[dict(position=k,vector=v,coordinates=c) for k,(v,c) in sorted(pivots.items(),reverse=True)],
                pairs=rows,survivor_count=len(survivors),surviving_local_triples=survivors,
                surviving_mask_affine_description=dict(base=25,directions=directions,branch=2),
                distinct_coordinate_counts=dict(Q15=len({r['Q15'] for r in survivors}),
                    Q3_source=len({r['Q3_source'] for r in survivors}),Q5_source=len({r['Q5_source'] for r in survivors})),
                every_pair_tested=True,all_survivors_original_normalized_equations_checked=True,
                no_actual_cofactor_word_test=True,no_CRT_or_global_realization_claim=True,
                author_self_check=True,independent_review=False)
    output.mkdir(parents=True,exist_ok=True)
    tmp=output/'local_source_jet_enumeration.json.partial'
    tmp.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    tmp.replace(output/'local_source_jet_enumeration.json')
    print(json.dumps({k:result[k] for k in ('pair_count','image_rank','survivor_count','every_pair_tested')}))


if __name__=='__main__':
    main()
