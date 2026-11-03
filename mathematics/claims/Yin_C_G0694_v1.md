---
author: Yin
---
# Actual non-quadratic-primary modulo-sixteen residuals and factor control

Human author Yin.
The [active all-strategy G0001 Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
Root proposed the actual primary ideal (f^2,2f,4) as a way to test the first modulo16 error and suggested stronger factor conditions for the second.
Same_trace verified the global compositions and actual monic-division ideal, proved the automatic first-component vanishing, derived the complete second eighth-error with its integer quotient/half terms, and checked the stated sufficient actual factor condition.
This is author mathematics, not independent review.
Focused reuse read C675's actual dyadic representative and non-phi argument, adopted C686's real constructed input, and C689's entire new obstruction.
The new component proof is retained directly below and does not infer integer ideal membership merely from a reduced root order.
No native computation, coefficient scan or external source theorem is used.

The [D1 non-phi section](../drafts/Yin_D_G0001.md#actual-nonphi-sixteen-errors) is development provenance, not a logical input.
This entire theorem is initially open for fresh isolated whole review.

## Statement

### NP1: complete input and the actual conclusions

Let A>=2 be even, phi=X^2+X+1 over F_2, chi=Xphi^2 and Phi=X^2+X+1 over Z.
Let Y be a monic square prime to Xphi, with Y|Y(chi) and Y|Y(X^3+X).
Put

    H_0=X^A Y=product_psi psi^(n_psi),
    U=H_0phi^(7A), d=degU, J_H=product psi^(n_psi/2).

All n_psi are the full positive even exponents, and psi ranges over EVERY irreducible of H_0.
Choose monic integer lifts P_psi, with P_X=X, and set

    S=product P_psi^(n_psi/2)Phi^(7A/2),
    mathcal_H=product P_psi^(n_psi),
    P=Phi^A K, T=S^2+2P+4W.                          (NP1)

Choose arbitrary integer K,W with degK<d-2A, degW<d and J_H|Kbar.
No eleventh-root relation or old-support congruence is needed for the component theorem below.
T is an actual monic polynomial of degree d and reduction U.
Define a,b,c,F,X_s by the actual canonical integer divisions

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a=rem_T(T(C_2))/2,
    b=rem_T(T(C_3))/3, c=rem_T(T(C_5))/5,
    F=rem_T(2c^2-3a^5),
    X_s=rem_T(b^2-a^3+s(c^3-2b^5)), s in{1,-1}.

Throughout this component theorem, Delta(B)=(B(C_2)-B^2)/2 is the actual integer half-difference of an integer polynomial B.

On EVERY H_0-primary component in the actual localized quotient modulo16 one has

    F=0 modulo16, X_s=0 modulo8.                     (NP2)

In particular, if F is globally coefficientwise divisible by8, then

    (F/8)bar=0 in F_2[X]/H_0.                        (NP3)

Thus the first non-phi requirement in C689 SX4 is AUTOMATIC for its entire square-input domain.

For the more precise second formula assume additionally that A and every n_psi are divisible by4, so S is an actual integer square.
Fix psi and put f=P_psi^(n_psi/2), S=f s_psi, u_psi=s_psibar^2.
Perform these THREE actual monic integer divisions:

    P=f p_psi+2e_psi,
    S(C_3)=f r_psi+2g_psi,
    P(C_3)=f t_psi+2h_psi.                            (NP4)

Each remainder is even and has degree below degf, as proved below.
Define in B_psi=F_2[X]/psi^(n_psi)

    f_0=fbar=psi^(n_psi/2), p_0=p_psibar,
    w_0=(W+e_psi)bar,
    beta_psi=t_psibar+p_0 r_psibar^2/u_psi.           (NP5)

The denominator u_psi is a unit.
If X_s is globally coefficientwise divisible by8, its actual error on this primary is EXACTLY

    (X_s/8)bar
       =w_0^6+(f_0/u_psi)
                        (p_0^3 w_0^4+p_0 beta_psi^2)
                                                    in B_psi. (NP6)

This formula applies to both signs and uses actual integer halves and quotients in NP4, not unspecified local parameters.
Its right side is also the unique local eighth of X_s from NP2 when a global eighth is not available.

A concrete sufficient condition eliminating EVERY such second component is

    P is divisible over Z by
                J_(3/4)=product P_psi^(3n_psi/4),
    W is divisible over Z by
                J_(1/2)=product P_psi^(n_psi/2).      (NP7)

Under NP7 both residuals vanish modulo16 on all H_0-primary components.
The theorem does not claim that the earlier phi-primary root and correction constraints can already be realized together with NP7 within their degree bounds.
That compatibility is a separate construction question.
For C686 and the adopted high-q C691 inputs, all n_psi and A are divisible by4 and NP6 therefore computes the actual outstanding second non-phi error.
It is not presumed to vanish for the currently chosen lifts.

## Argument

### NP2: actual ideals, compositions and monic reduction

Fix psi, n=n_psi and f=P_psi^(n/2).
Let I=(f,2) in Z[X], so I^2=(f^2,2f,4).
Since S is exactly divisible by f and Pbar is divisible by fbar, monic division gives the first relation in NP4 with an even remainder.
Thus

    T=f^2 s_psi^2+2f p_psi+4(W+e_psi) in I^2.         (NP8)

Both global forward hypotheses imply H_0|H_0(chi) and H_0|H_0(X^3+X), including the full X factor.
Taking their polynomial square roots gives

    J_H|J_H(chi), J_H|J_H(X^3+X).

Since Sbar=J_Hphi^(7A/2) and J_H|Pbar, the reductions of S(C_p) and P(C_p), for p=3,5, are divisible by fbar.
Their monic division by the ACTUAL f consequently has an even remainder.
This proves the other two even remainders in NP4 and the analogous C5 relations.
In particular S(C_p),P(C_p) belong to I as actual integer polynomials.
It follows that

    T(C_p)=S(C_p)^2+2P(C_p)+4W(C_p) belongs to I^2
                                                       (p=3,5).

The numerator and the actual divisor T both lie in this same global ideal.
Therefore the actual remainder T(C_p)-Q_pT also lies in I^2, for its genuine monic quotient Q_p.
Modulo16, division by p is multiplication by a unit.
Hence the ACTUAL canonical b and c modulo16 lie in I^2.
This proof uses the integer composed polynomials before reduction, not composition of a local psi-class.

In the localization Q_(psi,16) of (Z/16Z)[X]/T at reductions prime to psi, s_psi^2 is a unit.
Equation NP8 gives

    f^2=-2f p_psi/s_psi^2
                    -4(W+e_psi)/s_psi^2.             (NP9)

It follows that both b and c belong to (2f,4) there.
Thus for suitable actual localized representatives,

    b=2f B+4B_1, c=2f C+4C_1 modulo16.

Their exact products satisfy

    2c^2=8f^2 C^2=0 modulo16,
    b^2=4f^2 B^2
                  =-8f p_psi B^2/s_psi^2 modulo16,
    c^3=8f^3 C^3=0 modulo16, 2b^5=0 modulo16.         (NP10)

The vanishing uses NP9 with its actual even coefficients, not just f_0^2=0 after reduction.

Also a is even on this component.
Indeed Delta(S^2) is an even integer polynomial, and direct expansion of Delta(T) modulo2 gives a_bar=Pbar^2, which is zero modulo psi^n.
Thus a^5=0 modulo16 and a^3 is divisible by8.
Equations NP10 prove NP2 for either sign.

The canonical coefficient module is free because T is monic.
Localization preserves its exact kernels of multiplication by powers of2; in particular ann(8)=2Q_(psi,16).
Thus an element locally divisible by8 has a unique eighth modulo2.
If its canonical coefficients are globally divisible by8, that local eighth is precisely the localization of their integer coefficient quotient.
This proves NP3 and the meaning of NP6 without dividing a zero divisor arbitrarily.

### NP3: the exact half of a for the fourth-power input

Now assume all n_psi and A are divisible by4.
Both f and S are actual integer squares, so Delta(f)bar=Delta(S)bar=0.
Expand Delta(T) over Z and use the SAME divisor relation S^2=-2P-4W.
Modulo4 the canonical class is

    a=P^2+2[Delta(P)+P^2+W(C_2)+Delta(S)^2].           (NP11)

This is the precision4 restriction of the actual C675 identity and also follows directly from Delta(S^2)=2S^2Delta(S)+2Delta(S)^2 and the cross terms.
No higher dyadic remainder is selected independently.

In B_psi, Pbar^2=0 and Delta(S)bar=0.
From the actual division P=f p_psi+2e_psi,

    Delta(P)bar
       =f_0^2 Delta(p_psi)bar
                       +p_0^2 Delta(f)bar+e_psibar^2
       =e_psibar^2 in B_psi.                          (NP12)

Here Delta(B+2E)bar=Delta(B)bar+Ebar^2 follows by the exact integer expansion, and f_0^2=0 only at this final reduction.

For the first term P^2 in NP11, use P^2=f^2p_psi^2 modulo4 and then NP9.
Its legitimate half contributes f_0p_0^3/u_psi.
The remaining terms in NP11 contribute e_psibar^2+Wbar^2.
Consequently the unique half of the actual even a is

    (a/2)bar=f_0p_0^3/u_psi+w_0^2 in B_psi.           (NP13)

This is a local coefficient half of the actual canonical a, not the assumption that its coefficients are even at other primary components.

Since f_0^2=0, taking the third power of NP13 gives

    (a^3/8)bar=w_0^6+f_0p_0^3w_0^4/u_psi.           (NP14)

Every term has retained its full primary multiplicity.

### NP4: the actual C3 half and the complete second eighth

Use the last two exact divisions in NP4.
Modulo4,

    S(C_3)^2+2P(C_3)+4W(C_3)
       =f^2r_psi^2+2f t_psi.

Substitute NP9 and divide by the odd unit3.
The resulting actual canonical class satisfies

    b=2f B modulo4,
    Bbar=t_psibar+p_0 r_psibar^2/u_psi=beta_psi.       (NP15)

Reduction is legitimate because these are identities in the SAME quotient by T, and the original monic remainder has been retained.
Squaring and using NP9 once more yields

    (b^2/8)bar=f_0p_0 beta_psi^2/u_psi.               (NP16)

The terms in c^3 and2b^5 vanish modulo16 by NP10.
Combining NP14 and NP16 proves the complete formula NP6.
The sign no longer appears because those actual odd-cube terms have already vanished, not because signs were discarded before an integer half.

For a fixed actual T modulo8, the quantities in NP6 give the same unchangeable non-phi eighth-error described by C689.
In particular T->T+8V leaves P and the divisions in NP4 fixed and changes W by2V, so w_0 and NP6 are unchanged.
A final16Z changes W by4Z and likewise cannot alter this component.
No independently adjustable a/2, b/2 or c/2 coordinate is being used.

### NP5: sufficient actual factors and the remaining phi problem

Assume NP7.
For each psi the actual division of P by f has e_psi=0, and p_0 has psi-order at least n/4.
Also w_0=Wbar has order at least n/2, so w_0^4=w_0^6=0 in B_psi.

Let J_0=product psi^(n_psi/4), so H_0=J_0^4.
The complete forward divisibility H_0|H_0(X^3+X) implies J_0|J_0(X^3+X) by comparing polynomial multiplicities.
Thus J_0^3|J_0^3(X^3+X).
Since Pbar is divisible by J_0^3, P(C_3)bar has psi-order at least3n/4.
After dividing by fbar, t_psibar has order at least n/4.
The other summand p_0 r_psibar^2/u_psi in beta_psi has at least the same order.
Therefore

    ord_psi(f_0p_0 beta_psi^2)
          >=n/2+n/4+2(n/4)=5n/4>=n.

Formula NP6 vanishes.
Together with NP3 this proves the claimed complete non-phi modulo16 conclusion under NP7.

The automatic first-component result requires neither NP7 nor a root precision beyond the original square-input assumptions.
It removes the B_H condition from the first test in C689 for every actual input of that theorem.
The second formula explains exactly what must still be controlled, and NP7 is a sufficient actual integer factor condition, not a claim of compatibility with the phi roots and original degree bounds.
Any construction using it must verify those conditions simultaneously on the same K,W and actual monic T.
No phi-component modulo16 solution, characteristic-zero equation or original realization follows from this component result alone.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:58 |
| status | open |
| reason | Register automatic first-residual modulo16 vanishing on every full H_0-primary, exact second eighth-error for actual fourth-power bases with all integer quotient/half terms, and a sufficient actual three-quarter/half factor condition eliminating that component too. No compatibility of the extra factors with the phi-root/degree constraints, phi modulo16 solution or original realization is presumed. Fresh isolated whole review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete component theorem](#statement) | NP1--NP7, every actual square factorized forward input and full repeated primary including X, first modulo16 and second modulo8 vanishing, full fourth-power-input second formula, global-half interpretation and exact sufficient actual factor condition. |
| argument | [Whole actual ideal and half proof](#argument) | NP8--NP16 and NP2--NP5, true compositions and monic reduction in I^2, actual divisor relation, all coefficient powers and local division kernels, actual C2/C3 quotient halves, both signs, all multiplicities and sufficient-factor valuations. |
| dependency | [Actual dyadic polynomial representative](Yin_C_G0675_v1.md#argument) | MQ3 modulo4 restriction only, with the elementary expansion repeated in NP3; no old-support hypothesis is imported into this component theorem. |
| support | [Prior non-phi modulo8 calculation](Yin_C_G0675_v1.md#statement) | Earlier complete-domain comparison, strengthened here by an actual integer ideal argument and full next second component; its modulo8 result is not silently promoted. |
| support | [Actual high-power constructed inputs](Yin_C_G0686_v1.md#statement) | Application only: A and all H_0 multiplicities divisible by4, actual factorized S/K/W with J_H condition, same degree/reduction and unchanged original cost. No automatic vanishing of the new second formula is imported. |
| support | [Exact next-layer obstruction](Yin_C_G0689_v1.md#statement) | SX4/SX7 application: the first B_H requirement is proved automatic here; the second is now explicitly computed and vanishes under NP7, whose simultaneous global realizability remains separate. |
| support | [Adopted doubled-support family](Yin_C_G0691_v1.md#statement) | Additional applicable canonical input through its actual high-q construction only; stronger phi jets do not replace the integer ideal and half argument. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T05:08 |
| status | proved |
| reason | Adopt the fresh isolated whole review of NP1--NP16 and the entire actual component proof. The full square-input domain has automatic first-residual modulo16 and second-residual modulo8 vanishing on every non-phi primary, including X. The exact stronger-domain second eighth and sufficient actual integer factor condition retain all local halves, repeated multiplicities and both signs. Compatibility of those factors with the phi constraints and original degree bounds remains unproved; no passing global modulo16 input, characteristic-zero realization or unrestricted completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete component theorem](#statement) | NP1--NP7, every actual square factorized forward input and full repeated primary including X, first modulo16 and second modulo8 vanishing, full fourth-power-input second formula, global-half interpretation and exact sufficient actual factor condition. |
| argument | [Whole actual ideal and half proof](#argument) | NP8--NP16 and NP2--NP5, true compositions and monic reduction in I^2, actual divisor relation, all coefficient powers and local division kernels, actual C2/C3 quotient halves, both signs, all multiplicities and sufficient-factor valuations. |
| dependency | [Actual dyadic polynomial representative](Yin_C_G0675_v1.md#argument) | MQ3 modulo4 restriction only, with the elementary expansion repeated in NP3; no old-support hypothesis is imported into this component theorem. |
| support | [Prior non-phi modulo8 calculation](Yin_C_G0675_v1.md#statement) | Earlier complete-domain comparison, strengthened here by an actual integer ideal argument and full next second component; its modulo8 result is not silently promoted. |
| support | [Actual high-power constructed inputs](Yin_C_G0686_v1.md#statement) | Application only: A and all H_0 multiplicities divisible by4, actual factorized S/K/W with J_H condition, same degree/reduction and unchanged original cost. No automatic vanishing of the new second formula is imported. |
| support | [Exact next-layer obstruction](Yin_C_G0689_v1.md#statement) | SX4/SX7 application: the first B_H requirement is proved automatic here; the second is now explicitly computed and vanishes under NP7, whose simultaneous global realizability remains separate. |
| support | [Adopted doubled-support family](Yin_C_G0691_v1.md#statement) | Additional applicable canonical input through its actual high-q construction only; stronger phi jets do not replace the integer ideal and half argument. |
| review | [Fresh isolated whole review](../audits/reviews/Yin_R_G0915_v1.md#whole-nonphi-sixteen-component-finding) | Entire NP1--NP16 statement and argument, every actual monic-quotient/half step, all direct fixed interfaces and precise component/compatibility limits; independently reviewed. |
