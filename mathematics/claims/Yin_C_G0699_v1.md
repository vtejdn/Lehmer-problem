---
author: Yin
---
# Actual factor-compatible modulo-eight lifts and a same-degree two-test modulo-sixteen reduction

Human author Yin.
The [renewed all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-resume-until-two-percent-remaining-2026-10-25) authorizes this continuation.
Root identified the actual-factor compatibility question and the value of retaining the integer derivative at the next precision.
Same_trace developed the stronger factorized CRT lifts, checked every actual degree and composition requirement, and proved the unchanged-degree reduction below.
This is author mathematics, not independent review.
Focused reuse read adopted C686/C689/C692/C694 and C695 WP3--WP8, particularly its explicit power-lift applicability in the complete low-carry argument.
The stronger integer factors are not inferred merely from reduction or a divisible coefficient0/1 lift.
No native computation, support scan, external theorem or enlarged primary precision is used.

The [D1 compatible-factor section](../drafts/Yin_D_G0001.md#actual-factor-compatible-mod-eight-lifts) is development provenance, not a logical premise.
This entire theorem is initially open for fresh isolated whole review.

## Statement

### CP1: complete input and two conclusions

Let a>=2 be even, phi=X^2+X+1 over F_2, chi=Xphi^2 and Psi=phi(chi).
Let Y_b be monic and prime to Xphi, with Y_b|Y_b(chi) and Y_b|Y_b(X^3+X).
Set

    H_b0=X^aY_b, h_b=degH_b0,
    C_b0=X^aY_b(chi)Psi^(7a),
    H_b0^6=C_b0^21 modulo phi^(4a), h_b>=34a.         (CP1)

The last two conditions are hypotheses.
Choose one monic integer lift P_psi for every irreducible of H_b0, with P_X=X, and use the full exponents to set H_b=X^a mathcal_Y_b.
For a power q of2 with q>=512 put

    A=aq, H_0=H_b0^q, h=qh_b, d=h+14A,
    U=H_0phi^(7A), mathcal_H=H_b^q,
    Phi=X^2+X+1 over Z, chi_0=X Phi^2,
    C_b=X^a mathcal_Y_b(chi_0)Phi(chi_0)^(7a),
    C=C_b^q, C_0=C_b0^q,
    S=(H_bPhi^(7a))^(q/2),
    J_3=H_b^(3q/4), J_2=H_b^(q/2).                  (CP2)

Here J_3 and J_2 are ACTUAL integer polynomials.
Their reductions are denoted j_3 and j_2; in particular j_2^2=H_0.
For each separately fixed sign s in{1,-1}, there exist actual integer K_*,W_* such that

    T_*=S^2+2Phi^A K_*+4W_*,
    degK_*<d-2A, degW_*<d,
    J_3|K_* and J_2|W_* OVER Z.                     (CP3)

The monic T_* has degree d and reduction U.
Its SAME canonical divided remainders and residuals are

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a_T=rem_T(T(C_2))/2,
    b_T=rem_T(T(C_3))/3, c_T=rem_T(T(C_5))/5,
    F(T)=rem_T(2c_T^2-3a_T^5),
    X_s(T)=rem_T(b_T^2-a_T^3+s(c_T^3-2b_T^5)).

For an integer polynomial B, Delta(B)=(B(C_2)-B^2)/2 denotes its actual integer dyadic half-difference.
The two residuals satisfy coefficientwise

    F(T_*)=X_s(T_*)=0 modulo8.                       (CP4)

On EVERY H_0-primary they already vanish modulo16 by C694 NP7.
Thus the actual integer factor requirements are now compatible with the phi-root, both modulo8 residuals and the original degree.
The constructed k_*=K_*bar satisfies k_*^11=H_0C_0^2 modulo phi^(4A), j_2|k_* and X^(3A/2)|k_*, which include every global low coefficient constraint of C689.

For every q>=4096, the construction can additionally ensure

    T_*'=0 coefficientwise modulo16,
    E_F=(F(T_*)/8)bar and E_X=(X_s(T_*)/8)bar
                         are GLOBAL square polynomials. (CP5)

The prime is ordinary INTEGER differentiation.
No residual modulo16 conclusion at phi is included in CP5.

For these q>=4096 choices, the ENTIRE C689 modulo16 lifting question above T_* modulo8 reduces to the following TWO actual tests.
First require

    ord_phi E_F>=9A/2.                               (CP6)

When CP6 holds, in F_2[X]/phi^(5A/2) define

    r=H_0E_F/(phi^(9A/2)k_*^10),
    t=phi^(A/2)/k_*,
    u=r+t r^2+t^3 r^4.

The phi^(9A/2) division is exact at the stated precision; all remaining denominators are units.
Let u_0 be the representative of degree<5A, U_0 its coefficient0/1 integer lift, and put

    T'=T_*+8Phi^(3A/2)U_0.                           (CP7)

Then F(T')=0 modulo16 and X_s(T')=0 modulo8.
The second and final test is

    ord_phi[(X_s(T')/8)bar]>=4A.                      (CP8)

There exists a monic T_new=T_* modulo8 of degree d with BOTH residuals zero modulo16 if and only if CP6 and CP8 hold.
When they hold, C689's full fiber remains exactly2^(2d-47A/4) modulo32.
That count is over ALL lifts above the fixed modulo8 class, not a count restricted by the actual factors in CP3.
No proof that CP6 or CP8 holds for a particular constructed input is claimed here.

For the complete C667/C698/C691 families, take a=2m and Y_b=Y_0 with their already paid full representative.
Their fresh-factor margin gives h_b>181a, so CP1's34a condition costs no new degree or support.
The quantities

    A=2mq, d=q(30m+degY_0),
    original layer weight=12mq,
    canonical degree gap=q(5m-Q-5degH)

remain unchanged; for C691 the last expression is q(m-8-5degH).
Actual maximal q is retained where proved by the original normalized nonsquare input; generic CP1 merely specifies the raised q.
No equality G_int=G_can, characteristic-zero residual identity, irreducibility, total reality or Task completion is inferred.

## Argument

### CP2: exact factorized lifts and the initial structured base

We use the following elementary lift choice throughout.
If a binary polynomial f is divisible by the reduction of a fixed monic integer polynomial D, write f=Dbar g and lift g coefficientwise.
Then D times that lift is an ACTUAL D-divisible integer lift of f, of exactly the same degree.
This changes no prescribed residue or bound and makes no claim that a coefficient0/1 lift already has that integer factor.

Let k_b be the CRT root modulo phi^(4a), zero modulo H_b0X^(a/2), of degree<h_b+17a/2.
Instead of its coefficient0/1 lift, choose K_b exactly divisible over Z by H_bX^(a/2) using the preceding rule.
Set K_0=K_b^q.
All C683/C686 structured-base arguments use this actual q-th power, its reduction, and its degree; their genuine integer half-remainders hold for this lift as well.
In particular

    k_0^11=H_0C_0^2 modulo phi^(4A),
    X^(3A/2)|K_0 over Z, J_3|K_0 over Z,
    degK_0<h+17A/2<d-2A.

The full actual C699 eta is e_s^q for a lower class e_s modulo phi^(3a).
The sign-dependent integer halves remain M_+bar=0 and M_-bar=rem_(phi^A)(k_0^6), and Delta(K_0)bar=0.
Thus no new integer-half condition is assumed in describing e_s.

Choose rho=e_s modulo phi^(3a), rho=0 modulo H_b0, with degrho<h_b+6a.
Lift it as an ACTUAL H_b-divisible R_b and put W_0=R_b^(q/2).
Then

    J_2|W_0 over Z, degW_0<h/2+3A<d,
    T_0=S^2+2Phi^AK_0+4W_0.

C699/C702 give both residuals zero modulo4 for this exact T_0.
The C683 FP3--FP4 integer fourth-power remainder calculation applies unchanged: K_0,C are q-th powers, W_0 a q/2-th power, and S is an integer square.
Its actual low second quarter belongs to I_low=phi^A Fr(F_2[X]/phi^(4A)).
C694 NP7 already makes both residuals zero modulo16 on H_0-primary components of T_0.

### CP3: the first correction with an actual three-quarter factor

The actual first half-remainder has the full C686 power identity

    M_Fbar=phi^(2A)rem_(phi^A)(V_Fbar Q_Fbar),
    U_F=(H_b C_b^2)^(q/2), V_F=K_b^(11q/2),
    U_F-V_F=Phi^(2A)Q_F+2R_F.

It follows by taking the actual remainder modulo Phi^(3A) of U_F^2+3V_F^2 modulo4 and then its legitimate half.
Consequently O_F=(F(T_0)/4)bar is a q/2-th power in B_phi=F_2[X]/phi^(7A).
The complete first-quarter formula, not merely its low-order truncation, is used.
It has order at least2A.

Put A_F=C_0^2+phi^(4A)k_0^8W_0bar^2.
The required first correction residue is

    ell_1=H_0 A_F^(-1)(O_F/phi^(2A))
                                      modulo phi^(5A),
    ell_1=0 modulo j_3X^(5A/2).                      (CP9)

Let r_1=q/4.
The high target is an r_1-th power, and the two moduli are r_1-th powers of phi^(20a) and H_b0^3X^(10a).
Solve their lower CRT, obtaining ell_b of degree<3h_b+50a.
Use the ACTUAL lift L_b divisible by H_b^3X^(10a), and set

    L_1=L_b^(q/4), K_1=K_0+Phi^(4A)L_1,
    T_1=T_0+2Phi^(5A)L_1.                            (CP10)

Then J_3|L_1 over Z and X^(13A/4)|L_1 over Z.
The decisive original degree bound is

    degL_1<3h/4+25A/2<=h+4A,                         (CP11)

which follows exactly from h>=34A.
The low modulus in CP9 contains j_2X^(5A/2), and hence all the lower constraints required by C677.
Thus F(T_1)=0 modulo8 and X_s(T_1)=0 modulo4, with the same W_0 and actual J_3|K_1.

The entire low carry remains the C686 HP12 expression

    O_1+O_0=phi^(2A)
          [k_0^6ell_1^2/H_0^2+(k_0/H_0)Rbar ell_1]
                                       modulo phi^(4A), (CP12)

where R is the actual quotient obtained from the old canonical numerator as in that proof.
That argument uses actual X^(3A)|L_1 and its reduction, not a coefficient0/1 lift.
Both facts are verified here, and Rbar remains a q-th power because the old structured numerator and divisor are q-th powers.
C695 WP5 also explicitly verifies this lift independence.
Therefore O_1 remains in I_low.
The actual J_3/J_2 factors are maintained, so C694 controls all non-phi components.

The exact T_1 is a sum of terms with integer exponents q,q/2,q/4 and their stated scalar coefficients.
C686's coefficient-subring and actual monic-division lemmas give

    T_1 modulo16 belongs to Z_16[X^(q/32)],
    O_1=(X_s(T_1)/4)bar belongs to F_2[X^E],
    E=q/64, p=E/2=q/128>=4.                          (CP13)

Here O_1 is the GLOBAL canonical quarter, and T_1' is divisible by8.
This is the conservative subring guaranteed by the smaller q/4-th first lift.

### CP4: the second correction with exact factors and arbitrary supported power lifts

The exact low-elimination target is

    v^2=H_0 O_1/(phi^A k_1^5) modulo phi^(3A).         (CP14)

The polynomial O_1 is divisible by phi^A.
It is an E-th power, E divides A, k_1 is a q/4-th power after reduction, and the modulus is an E-th power.
Thus the full target in CP14 is an E-th power and its square-root class modulo phi^(3A/2) is a p-th power.
Impose additionally v=0 modulo j_2.
The lower p-th-root CRT moduli are phi^(192a) and H_b0^64.
Choose its representative r_v and an ACTUAL H_b^64-divisible lift R_v, and put

    v=r_v^p, V=R_v^p,
    J_2|V over Z, degV<h/2+3A<h+11A.                 (CP15)

Let w=W_0bar and A_F1=C_0^2+phi^(4A)k_1^8w^2.
The restoring residue is

    ell_2=[phi^(3A)k_1^9v^2+phi^(5A/2)k_1^10v]/A_F1
                                         modulo phi^(5A),
    ell_2=0 modulo j_3X^(5A/2).                      (CP16)

The target and both moduli are p-th powers, not merely fourth powers.
Their lower moduli are phi^(640a) and H_b0^96X^(320a).
Choose the least CRT representative ell_2.
It is a p-th power of degree<3h/4+25A/2 and is polynomially divisible by phi^(5A/2).
Write ell_2/phi^(5A/2)=m_b^p.
The lower polynomial m_b is divisible by H_b0^96X^(320a).
Choose its ACTUAL H_b^96X^(320a)-divisible lift M_b and put

    M=M_b^p, L_2=Phi^(5A/2)M,
    D=Phi^(3A/2)V, Q_2=Phi^(5A)L_2,
    K_2=K_1+Phi^(4A)L_2,
    W_2=W_0+D, T_2=T_1+2Q_2+4D.                     (CP17)

Thus J_3|L_2 and J_2|D over Z, and X^(13A/4)|M over Z.
All original bounds hold: degL_2<h+4A, degK_2<d-2A and degW_2<d.
Both exact integer factors J_3|K_2 and J_2|W_2 are preserved.
Moreover k_2 is a p-th power over F_2, since each summand of its displayed construction is such a power.

C695 WP7 rechecks the entire C680 low calculation for ACTUAL power lifts: its only required extra conditions on M are its integer X^(3A) factor and degree, while V enters by actual composition.
Our stronger factor lifts satisfy precisely those conditions.
Explicitly, the same divisor relation is

    T_2=(1+2Phi^(A/2)M/mathcal_H)T_1
           +4Phi^(3A/2)(V-K_1M/mathcal_H)
           -8Phi^(A/2)W_0M/mathcal_H.

The old canonical numerator quotient has phi-order at least3A, so the legitimate quarter of its divisor carry starts beyond4A.
The C5 change uses the actual X^(3A)|M to divide Q_2(C_5) by Phi^(6A) before taking its even remainder.
The dyadic change is the exact polynomial

    Q_2(C_2)+2Q_2^2+2D(C_2)+4(Phi^A K_1)Q_2
                                      -4Q_2Delta(S).

After the same divisor reductions its complete low contribution is

    O_2+O_1=phi^A(k_1^5/H_0)v^2 modulo phi^(4A).      (CP18)

These are the full adopted C680/C695 identities, with the different actual lifts checked rather than assumed equivalent from their reductions.
CP14 kills the low part, while CP16 restores F modulo8 and preserves the same new W modulo4.
Thus F(T_2)=0 modulo8, X_s(T_2)=0 modulo4 and phi^(4A)|O_2.
C694 additionally proves both residuals modulo16 on every H_0-primary.

Since p>=4, the ordinary derivatives of V and M are divisible by4.
The powers3A/2 and15A/2 are also divisible by4.
Thus T_2' is divisible by8.
The C686 actual monic-division derivative lemma gives that O_2 is a global square.
Its exact division by phi^(4A)k_2^4 is therefore square modulo phi^(3A).

### CP5: controlled final correction and exact C694 compatibility

Choose a root z of

    z^2=O_2/(phi^(4A)k_2^4) modulo phi^(3A),

and impose z=0 modulo j_2.
The coprime CRT has a representative of degree<h/2+3A.
Lift it as an ACTUAL J_2-divisible integer Z of that degree.
The shared correction T_*=T_2+8Z gives both residuals modulo8 by C675, and absorbing it into W_*=W_2+2Z preserves exact J_2 divisibility.
K_*=K_2 remains exactly divisible by J_3.
This proves CP3--CP4, without increasing degree or changing U.

The actual NP7 factors of C694 are exactly J_3 and J_2 here, because all original multiplicities were raised by q.
They are not only reduced divisibility statements or congruences modulo8.
C694 therefore proves first and second modulo16 vanishing on all H_0-primary components of this same T_*.
This establishes the requested compatibility; the phi component has not yet been promoted to modulo16.

### CP6: preserving derivative modulo16 and making both eighth-errors square

Now let q>=4096, retaining the SAME construction but choosing the final Z with additional power structure.
The complete integer T_2 has the form

    F_0^q+2F_1^q+4F_2^(q/2)+2F_3^(q/4)
                                    +4F_4^p+2F_5^p,

where F_0=H_bPhi^(7a), F_1=Phi^aK_b, F_2=R_b, F_3=Phi^(20a)L_b, F_4=Phi^(192a)R_v and F_5=Phi^(960a)M_b are actual integer polynomials.
For the scalar2 terms, the power polynomial is needed only modulo8; for scalar4, only modulo4.
C686's coefficient-power lemma therefore shows

    T_2 modulo16 belongs to Z_16[X^N],
    N=p/4=q/512>=8.

Its actual canonical quarter O_2 consequently belongs to F_2[X^(N/2)], by the full C2/C3/C5 monic-division subring argument.
Put E_2=q/1024>=4 and r_z=E_2/2=q/2048>=2.
The exact quotient O_2/(phi^(4A)k_2^4) modulo phi^(3A) is an E_2-th power: k_2 is a p-th power after reduction, and all divisor exponents are multiples of E_2.
Thus its square-root class is an r_z-th power.

Take the lower CRT with moduli phi^(3072a) and H_b0^1024, and lift its root as an ACTUAL H_b^1024-divisible Z_b.
Then use Z=Z_b^(r_z).
It has exactly the same bound degZ<h/2+3A, the same correct high residue and exact J_2 divisibility.
The final construction in CP5 therefore still applies.

The derivatives of the last two terms of T_2 are divisible by4p and2p respectively, and the first four terms have still higher divisibility.
Since p>=32, T_2' is divisible by16.
Also Z' is divisible by r_z>=2, so

    T_*'=T_2'+8Z'=0 modulo16.

For completeness the integer derivative lemma holds at modulus16 as at8.
If B=QT+R is actual monic division and T',B' are divisible by16, then R'=-Q'T modulo16 and degR'<degT force R'=0 coefficientwise.
For a_T use the exact identity Delta(T)'=X T'(C_2)-TT'; for b_T,c_T differentiate T(C_p) and invert the odd p.
Both canonical residual numerators and their remainders then have derivative divisible by16.
Since the actual F(T_*),X_s(T_*) are divisible by8, their coefficient eighths have derivative zero modulo2, hence are GLOBAL square polynomials.
This proves CP5.

### CP7: the exact unchanged-degree reduction to two phi tests

C694 already makes E_F and E_X vanish in B_H=F_2[X]/H_0.
Thus C689's first requirement is exactly CP6.
When it holds, the actual E_F is a global square divisible by the square phi^(9A/2).
The factors H_0,k_*^10 and the modulus phi^(5A/2) are squares, and k_* is itself a p-th power after reduction.
Consequently r and t in CP7 are square classes, and u=r+t r^2+t^3r^4 is a square class.
Its canonical representative u_0 uses only even powers of X.
The coefficient lift U_0 has even derivative; Phi^(3A/2) also has even derivative.
Hence the actual first correction in CP7 preserves coefficientwise divisibility of the INTEGER derivative by16.

C689 proves F(T')=0 modulo16 and X_s(T')=0 modulo8.
The derivative argument above makes E'_X=(X_s(T')/8)bar a global square.
C694 NP6 also shows its B_H part is unchanged by this8V correction: P,S and their actual divisions stay fixed, and W changes by an even polynomial.
Therefore E'_X is already zero on B_H.

If CP8 holds, exact division of the global square E'_X by the square phi^(4A), followed by the square unit k_*^4, leaves a square modulo phi^(3A).
Its derivative is zero, so the full C689 high derivative-image condition holds.
The final16Z correction then exists.
Conversely CP6 and CP8 are necessary by the complete C689 classification of all lifts above this fixed modulo8 class.
This proves the iff and preserves its stated full fiber.

The unresolved content is now precisely the actual first phi-order CP6 and, after its prescribed integer correction, the actual second phi-order CP8.
Neither high q, the doubled support of C691, the exact integer factors, nor the derivative argument has been used to assert those two orders without evaluation.
The construction supplies no characteristic-zero realization and no new original branch exclusion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-25T05:22 |
| status | open |
| reason | Register actual NP7-compatible same-degree modulo8 lifts for every stated strong-forward input with h_b>=34a and q>=512, and at q>=4096 an actual derivative16 lift with globally square eighth-errors reducing the complete same-degree modulo16 question to two precisely specified phi-order tests. All integer factors, lower CRTs, changed power lifts, monic quotients, original costs and unresolved test values are retained. No passing global modulo16 input or characteristic-zero realization is asserted. Fresh isolated whole review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete factor-compatible construction](#statement) | CP1--CP8, full normalized strong-forward input and actual integer lift factors, q>=512 construction at original degree, all non-phi modulo16 components, q>=4096 derivative/square enhancement, exact two-test iff and full C689 fiber, with unchanged original costs and unproved test values. |
| argument | [Whole bounded lift proof](#argument) | CP9--CP18 and CP2--CP7, exact factorized lifts, every power/CRT and degree, actual integer halves and canonical carry, supported second correction and final root, weighted coefficient subrings, derivative16 and unchanged-degree test reduction. |
| dependency | [Actual structured base and low carry](Yin_C_G0683_v1.md#argument) | FP2--FP4 genuine power-input eta/half-remainders and initial low image, FP6 actual first-retuning carry; matched to the new exact factor lifts and original degrees. |
| dependency | [Complete exact first correction](Yin_C_G0677_v1.md#statement) | HC2--HC8 for arbitrary bounded integer L, same-W preservation and F8; applied with the stronger actual three-quarter factor and verified low X order. |
| dependency | [High-power integer and canonical lemmas](Yin_C_G0686_v1.md#argument) | HP7 actual M_F identity, HP12 genuine first carry, HP14--HP16 coefficient subrings and actual monic division, and integer derivative/final root mechanism; the new exponents and actual factors are proved here. |
| dependency | [Actual power-lift low calculation](Yin_C_G0695_v1.md#split-weak-forward-argument) | WP3--WP8 only at the strong-forward unit-seed endpoint: supported W, exact first half and carry, WP7 independence from coefficient0/1 V/M lifts once actual X order/degree are checked, and final controlled root. No missing weak-forward theorem is substituted. |
| dependency | [Exact low error equation](Yin_C_G0680_v1.md#statement) | LR1--LR7 target and first-restoring residue, with actual lift applicability checked through C695 WP7; no count for the new restricted factor family is imported. |
| dependency | [Final same-polynomial correction](Yin_C_G0675_v1.md#statement) | MQ7--MQ8 full shared8Z criterion after actual low error, global square and all primary hypotheses have been checked. |
| dependency | [Actual non-phi factors](Yin_C_G0694_v1.md#statement) | NP7 applied with exact integer J_3 dividing K and J_2 dividing W, and NP6 invariance under the later8V correction; this proves all non-phi modulo16 vanishing and compatibility, not phi success. |
| dependency | [Complete modulo16 classification](Yin_C_G0689_v1.md#statement) | SX4--SX9 actual first correction, complete low/high conditions and full fiber; both extra conditions are removed only by the proved integer-factor and derivative properties. |
| support | [Paid complete canonical input](Yin_C_G0667_v1.md#statement) | Application only: actual full forward data, fresh-factor margin, original degree/layers/gap/maximal q and complete repeated factors; no new degree expense or original realization is inferred. |
| support | [Adopted doubled-support input](Yin_C_G0691_v1.md#statement) | Additional applicable complete family with the same paid costs; doubled phi support is not used to presume either remaining actual error test. |
| support | [Two-term failure boundary](Yin_C_G0692_v1.md#statement) | Useful failed simplification retained; the present independent coefficient corrections are not collapsed into that excluded family. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T05:32 |
| status | proved |
| reason | Adopt the corrected physical-v2 independent whole review of CP1--CP18. The actual stronger factorized CRT lifts preserve the original degree and solve both residuals modulo8 for q>=512, with all non-phi components modulo16; for q>=4096 the derivative16 construction removes the extra high test and gives the exact two-phi-test all-lift criterion and fiber. Neither remaining actual phi test is proved to pass. Preserve R919v1 and its corrected endpoint wording; C699 mathematics is unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete factor-compatible construction](#statement) | CP1--CP8, full normalized strong-forward input and actual integer lift factors, q>=512 construction at original degree, all non-phi modulo16 components, q>=4096 derivative/square enhancement, exact two-test iff and full C689 fiber, with unchanged original costs and unproved test values. |
| argument | [Whole bounded lift proof](#argument) | CP9--CP18 and CP2--CP7, exact factorized lifts, every power/CRT and degree, actual integer halves and canonical carry, supported second correction and final root, weighted coefficient subrings, derivative16 and unchanged-degree test reduction. |
| dependency | [Actual structured base and low carry](Yin_C_G0683_v1.md#argument) | FP2--FP4 genuine power-input eta/half-remainders and initial low image, FP6 actual first-retuning carry; matched to the new exact factor lifts and original degrees. |
| dependency | [Complete exact first correction](Yin_C_G0677_v1.md#statement) | HC2--HC8 for arbitrary bounded integer L, same-W preservation and F8; applied with the stronger actual three-quarter factor and verified low X order. |
| dependency | [High-power integer and canonical lemmas](Yin_C_G0686_v1.md#argument) | HP7 actual M_F identity, HP12 genuine first carry, HP14--HP16 coefficient subrings and actual monic division, and integer derivative/final root mechanism; the new exponents and actual factors are proved here. |
| dependency | [Actual power-lift low calculation](Yin_C_G0695_v1.md#split-weak-forward-argument) | WP3--WP8 only at the strong-forward unit-seed endpoint: supported W, exact first half and carry, WP7 independence from coefficient0/1 V/M lifts once actual X order/degree are checked, and final controlled root. No missing weak-forward theorem is substituted. |
| dependency | [Exact low error equation](Yin_C_G0680_v1.md#statement) | LR1--LR7 target and first-restoring residue, with actual lift applicability checked through C695 WP7; no count for the new restricted factor family is imported. |
| dependency | [Final same-polynomial correction](Yin_C_G0675_v1.md#statement) | MQ7--MQ8 full shared8Z criterion after actual low error, global square and all primary hypotheses have been checked. |
| dependency | [Actual non-phi factors](Yin_C_G0694_v1.md#statement) | NP7 applied with exact integer J_3 dividing K and J_2 dividing W, and NP6 invariance under the later8V correction; this proves all non-phi modulo16 vanishing and compatibility, not phi success. |
| dependency | [Complete modulo16 classification](Yin_C_G0689_v1.md#statement) | SX4--SX9 actual first correction, complete low/high conditions and full fiber; both extra conditions are removed only by the proved integer-factor and derivative properties. |
| support | [Paid complete canonical input](Yin_C_G0667_v1.md#statement) | Application only: actual full forward data, fresh-factor margin, original degree/layers/gap/maximal q and complete repeated factors; no new degree expense or original realization is inferred. |
| support | [Adopted doubled-support input](Yin_C_G0691_v1.md#statement) | Additional applicable complete family with the same paid costs; doubled phi support is not used to presume either remaining actual error test. |
| support | [Two-term failure boundary](Yin_C_G0692_v1.md#statement) | Useful failed simplification retained; the present independent coefficient corrections are not collapsed into that excluded family. |
| review | [Fresh isolated whole review](../audits/reviews/Yin_R_G0919_v2.md#whole-factor-compatible-lift-finding) | Entire current fixed statement and argument, all actual direct interfaces, full quantifiers and exact remaining limits; independently reviewed. |
