---
author: Yin
---

# A universal ceiling for the retained finite-window Fourier certificate

Date: 2026-10-08.
Direct G0001 derivation by the coordinating Codex AI for Yin, under Yin's instruction to begin exploration with G0001 as the goal.
This is the bounded feasibility test assigned by [S G0005](../strategies/Yin_S_G0005.md#bounded-next-test).
It tests the exact constants already retained in [L G0123](Yin_L_G0123_v1.md#finite-transition-product-consistency-test), before any new multiplier enumeration.
No external source, numerical experiment, or novelty claim is involved.
The completed independent review is recorded below.

<a id="retained-certificate-universal-ceiling"></a>
## Statement and exact scope

Use the domain and definitions of L G0123: a monic irreducible algebraic unit polynomial P, positive logarithmic Mahler measure m, q>0 central embeddings, at least one stable and one expanding embedding, H>=1, 0<kappa<=1/(16q), and 0<eta<1.
Keep precisely its choices

    rho=max(max_stable |beta|, max_expanding |beta|^(-1)),
    rho_s=max_stable |beta|,
    J=ceil(log(16dH)/(-log rho)),
    ell_0=ceil(log(4 sqrt(2))/(-log rho_s)),
    E_0=3/[256(1-rho^2)]+2q^2 kappa^2,
    A_*=(1-eta) exp(-4 pi^2 E_0),
    T_N>=J, R_N>=J+1,
    k_N=floor((N-R_N-T_N)/ell_0)+1.                 (1)

Only use the last formula for a nonempty admissible frequency window; otherwise put k_N=0.
Let C_tr=C(theta,J) in (0,1] be the actual transition product, and put

    g(x)=((1+x)log(1+x)+(1-x)log(1-x))/2,
    C_ent(m)=(5/12)(exp(2m)-1)^2(1-exp(-4m)),
    K_0=8192/(75 e^2 pi^4)<1/5.                    (2)

For every such finite window, irrespective of the choice of integral multiplier or of its transition product,

    k_N g(A_* C_tr) <= K_0 N C_ent(m)
                       < (1/5) N C_ent(m).         (3)

The weak first inequality also holds with the artificial ceiling C_tr=1.
Consequently the retained L G0123 equation (13), with these exact amplitude and spacing constants, cannot exclude any putative input: even its idealized left side is already strictly below N C_ent(m), before the nonnegative logarithmic and KL overhead is added.

This is an obstruction to that particular certified lower envelope.
It is not an upper bound for the actual Fourier amplitudes, their weighted sum, or the relative entropy.
It does not refute the validity of L G0123, and it does not decide h_1=m or the unrestricted Mahler gap.

## Proof

Since alpha is a unit, the sum of the negative logarithms of its stable conjugates, counting both members of complex pairs, is exactly m.
Therefore, with L=log(4 sqrt(2))=(5/2)log 2,

    0 < -log rho_s <= m,
    1-rho^2 <= 1-rho_s^2 <= 2(-log rho_s) <= 2m,
    ell_0 >= L/m.                                 (4)

The middle inequality is 1-exp(-2x)<=2x for x>0.
For the finite count, log(16dH)>L, and -log rho<=-log rho_s.
Hence J>=ell_0.
Since T_N+R_N>=2J+1>=ell_0, a nonempty window has

    k_N <= (N-R_N-T_N)/ell_0+1 <= N/ell_0.          (5)

For 0<=x<=1, the convergent positive series

    g(x)=sum_(r>=1) x^(2r)/[(2r)(2r-1)]
         <= (log 2)x^2                            (6)

also holds at x=1 by monotone convergence.
Dropping the positive central part of E_0 and the factor (1-eta)^2 can only raise the ceiling.
Thus, with a_0=3 pi^2/64, equations (1), (4), (5), and (6) give

    [k_N/N] g(A_* C_tr)
       <= [log 2/ell_0] exp[-8 pi^2 E_0]
       <= [m log 2/L] exp[-a_0/m].                 (7)

No large-N limit, existence of a near-zero Mahler sequence, or numerical estimate has been used.

The entropy comparison constant admits the exact identity

    C_ent(m)=(20/3) sinh(m)^3 cosh(m)
             >= (20/3)m^3.                        (8)

For every m>0, setting y=a_0/m gives

    exp(-a_0/m)/m^2 = y^2 exp(-y)/a_0^2
                       <= 4/(e^2 a_0^2).          (9)

The last maximum follows by differentiation, at y=2.
Dividing (7) by (8) and using log 2/L=2/5 proves

    [k_N g(A_* C_tr)]/[N C_ent(m)]
       <= [3 log 2/(20 L)] 4/(e^2 a_0^2)
        = 8192/(75 e^2 pi^4)=K_0.                 (10)

For an entirely elementary strict bound, e>8/3 and pi>3 imply K_0<8192/43200=128/675<1/5.
The zero-frequency case is immediate.
Finally C_ent(m)>0, q log N/2>=0 for N>=1, and the constant C_P^KL in L G0120 bounds an absolute value and is nonnegative.
This proves the stated failure of the finite consistency certificate.

## Consequence for the next investigation

The ceiling test completes the bounded test for the unchanged L G0123 constants across all its inputs, including quartic Salem, Lehmer degree ten, and the multiple-expanding degree-twenty-two controls.
Separate numerical scans of these examples cannot improve this particular test.
No empirical inequality violation is asserted; such a violation would signal an inconsistent implementation or an invalid input contract.

A larger transition lower bound alone cannot fix the failure, since (3) already permits C_tr=1.
A useful reopening must change at least one of the actual losses: certify sharper tail amplitudes, use a stronger entropy-deficit upper bound, improve the effective frequency budget, or use actual amplitudes in the general L G0120 interface.
Replacing an upper entropy bound by equality is not allowed.
This note makes no claim that these alternatives are feasible.

The proof uses the retained L G0108 k=1 algebraic entropy upper comparison, L G0123 definitions and finite count, and the nonnegative overhead from [L G0120](Yin_L_G0120_v1.md#finite-window-central-kl-identity).
It does not depend on the separate [central-small compactness argument](Yin_L_G0125_v1.md#central-small-transition-collapse).



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0037_v1.md#actual-review), with its original inspected scope and relationship.
