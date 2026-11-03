---
author: Yin
---
# A complete second modulo-eight trace-remainder error for square inputs

Human author Yin.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
Root proposed checking the first-residual quarter, the non-phi vanishing of the second residual, and the remaining shared8V correction after the square-input modulo4 construction.
Same_trace identified the first formula as the already adopted C603 FE4, proved the full actual dyadic and C5-cube expansions below, and derived the complete second quarter with both changing-divisor contributions.
The square-input existence theorem [C672](Yin_C_G0672_v1.md#decision-whole-reviewed-2026-10-24) is actually adopted.
This section is new author mathematics, not an adopted modulo8 theorem or independent review.
Focused reuse read C672, C669, the full C603 coefficient formula and the C202 actual coupled correction/count.
The latter two are reused at their exact scopes rather than reproved as new results.
No native calculation, numerical coefficient search or higher-modulus iteration is used.

The [D1 modulo8 section](../drafts/Yin_D_G0001.md#square-input-next-mod8-candidate) is development provenance, not a logical dependency.
This whole theorem is initially open for fresh isolated whole mathematical review.

## Statement

### MQ1: full actual inputs and explicit auxiliaries

Let A>=2 be even, Phi=X^2+X+1 over Z, phi=Phi mod2, chi=Xphi^2 and Psi=phi(chi).
Let Y in F_2[X] be a monic SQUARE prime to Xphi, satisfying Y|Y(chi) and Y|Y(X^3+X).
Set H_0=X^A Y, U=H_0phi^(7A), h=degH_0, d=h+14A, and C_0=X^A Y(chi)Psi^(7A).
Assume H_0^6=C_0^21 modulo phi^(4A).
For each irreducible psi|H_0 choose a monic integer lift P_psi with P_X=X and retain the full even multiplicity N_psi.
Put

    mathcal_H=product_psi P_psi^(N_psi)=X^A mathcal_Y,
    J_H=product_psi psi^(N_psi/2),
    S=product_psi P_psi^(N_psi/2) Phi^(7A/2).

Thus S is an actual monic integer polynomial, S^2=mathcal_H Phi^(7A), Sbar^2=U and degS=d/2.
Choose integers K,W with

    k=Kbar, k^11=H_0C_0^2 modulo phi^(3A), J_H|k,
    degK<d-2A, degW<d,
    P=Phi^A K, T=S^2+2P+4W.                            (MQ1)

Here A and d belong to the actual U; no Frobenius-normalized exponent is substituted.
Fix s in{1,-1}.
For C_2=X^2-2, C_3=X^3-3X and C_5=X^5-5X^3+5X define the actual canonical integer polynomials

    a=rem_T(T(C_2))/2, b=rem_T(T(C_3))/3,
    c=rem_T(T(C_5))/5,
    F=rem_T(2c^2-3a^5),
    X_s=rem_T(b^2-a^3+s(c^3-2b^5)).

Assume F and X_s are coefficientwise divisible by4.
This is an actual input condition on K,W, not a free local quotient prescription.
Adopted C672 supplies such bases for these polynomial inputs by choosing the stated low K coefficients and then the C669 square root for W.
The present theorem treats every K,W satisfying MQ1 and this actual modulo4 condition.

For any integer polynomial B define Delta(B)=(B(C_2)-B^2)/2.
Use the concrete integer auxiliaries

    chi_0=X Phi^2, Psi_0=Phi(chi_0),
    C=X^A mathcal_Y(chi_0)Psi_0^(7A),
    E_5=(C_5-chi_0)/2,
    P_5=P(C_5), W_5=W(C_5),
    R_5=S(chi_0) E_5 S'(chi_0)+E_5^2 S'(chi_0)^2,
    Xi=Delta(P)+P^2+W(C_2)-2P Delta(S)+Delta(S)^2.       (MQ2)

All are exact integer polynomials; Delta and E_5 are integral.
Ordinary differentiation precedes composition in S'(chi_0).
Perform the actual monic division

    S(C_3)=Q_3 S+2E_3, degE_3<degS,
    B_3=P(C_3)-Q_3^2 P.                                (MQ3)

The remainder is even, as proved below; the formula uses its actual quotient Q_3.

Perform the following THREE specified monic integer divisions:

    mathcal_H C^2+3K^11=Phi^(3A)L_F+2M_F,
                                           degM_F<6A,
    sC^3-K^6=Phi^A L_s+2M_s, degM_s<2A,
    E_s=-P L_s+mathcal_H Phi^(6A)M_s
             +3mathcal_H Phi^(4A)(s C^2P_5-K^4Xi),
    E_s=Phi^(7A)L_E+2M_E, degM_E<14A.                 (MQ4)

The first two even remainders follow from C603/C669 at the stated root/support inputs.
The third even remainder follows from the actual X_s=0 modulo4 and is proved below.
No quotient by2 or4 is taken inside a characteristic-two algebra.
Let

    B_phi=F_2[X]/phi^(7A), w=Wbar, xi=Xibar,
    p_5=P_5bar, w_5=W_5bar, r_5=R_5bar, b_3=B_3bar,
    D_K=Delta(K)bar+k^2.

The letter xi here denotes Xibar, not a chosen root of unity.
Every denominator in the following formulas is a power of the unit H_0, or of k.

### MQ2: the complete quarters and simultaneous criterion

The actual first quarter is the adopted C603 formula

    O_F=(F/4)bar
       =phi^A k L_Fbar/H_0^2
        +phi^(2A)k^9 w^2/H_0
        +phi^(3A)k^10 w/H_0
        +phi^(4A)(M_Fbar+k^9D_K)/H_0 in B_phi.          (MQ5)

The complete actual second quarter is

    O_X=(X_s/4)bar
       =M_Ebar/H_0+phi^A k L_Ebar/H_0^2
        +w L_sbar/H_0+phi^(6A)C_0^3
        +phi^(2A)(C_0 p_5^2+k^2 xi^2)
        +phi^(4A)C_0^2(w_5+r_5)+b_3^2
                                                  in B_phi. (MQ6)

Although the signs disappear after reduction modulo2 in displayed summands, s still enters the actual divisions L_s,M_s,L_E,M_E.
The term involving L_E is the second changing-divisor contribution; the term involving W L_s is the first one's next coefficient.
The Taylor term r_5 is retained, not presumed zero.
For evaluating MQ6 one may use the already proved identity xi=phi^(2A)D_K+w^2 in B_phi, but Xi itself is the actual integer polynomial used in MQ4.

On EVERY non-phi primary component both canonical residuals already vanish modulo8 for the base T.
For an integer V of degree<d let T^+=T+8V and v=Vbar.
Then the whole simultaneous criterion is

    F(T^+)=X_s(T^+)=0 modulo8 for some V
    iff O_F=0 in B_phi and
         O_X in phi^(4A)k^4 Fr(B_phi),                 (MQ7)

where Fr denotes the square image.
Equivalently, first require O_X to be divisible by phi^(4A) in B_phi, take its exact quotient modulo phi^(3A), and require

    v^2=O_X/(phi^(4A)k^4) modulo phi^(3A).              (MQ8)

Existence in MQ8 is equivalent to zero ordinary derivative of its right side in that even-precision ring.
When MQ7 holds, exactly2^(d-3A) monic coefficient classes T^+ modulo16 above the fixed T modulo8 work; otherwise none do.
These are residual solutions modulo8, without an assertion that MQ7 holds for all or any of the present canonical candidates.
Both tests and the count are independent of choosing another integer representative of the same T modulo8, in the precise translated sense of C202.
The count concerns one fixed sign, not simultaneous validity for both signs.

## Argument

### MQ3: actual dyadic quotient through precision8

Since S^2 is the factorized base, direct integer expansion gives

    Delta(S^2)=2S^2 Delta(S)+2Delta(S)^2,
    Delta(T)=Delta(S^2)+P(C_2)+2W(C_2)
                   -2S^2P-4S^2W-2P^2 modulo8.

The actual a is represented by Delta(T) in the quotient by T.
Substitute the SAME divisor relation S^2=-2P-4W to obtain

    a=P(C_2)+2P^2+2W(C_2)-4PDelta(S)+2Delta(S)^2
      =P^2+2Xi modulo8.                                (MQ9)

This is a global congruence in (Z/8Z)[X]/T, before any primary is discarded.
In particular the term Delta(S)^2 is retained even at small A; no unproved valuation truncation is used.
The actual cube is therefore

    a^3=P^6+6P^4 Xi+4P^2 Xi^2 modulo8.                (MQ10)

Unlike a free-coordinate expansion, MQ9 specifies the entire needed next dyadic coefficient from the same integer S,K,W.
Modulo2 its half agrees with C603 FE8, giving the xi substitution stated after MQ6.

### MQ4: C5 Taylor correction and the actual odd quotients

The exact identity C_5=chi_0+2E_5 gives

    S(C_5)^2=S(chi_0)^2+4R_5 modulo8.                  (MQ11)

To verify this for an arbitrary integer polynomial S, its integer Taylor expansion has linear term2E_5S'(chi_0), while its quadratic term is a multiple of4.
Squaring makes the latter's cross term a multiple of8; the surviving linear cross term and square are exactly the two summands of4R_5.
Also S(chi_0)^2=Phi^(2A)C exactly, since S^2=mathcal_H Phi^(7A) and mathcal_H=X^A mathcal_Y.
As5^(-1)=5 modulo8, the actual c is represented by5T(C_5), and

    c=5Phi^(2A)C+2P_5+4(W_5+R_5) modulo8,
    c^3=5Phi^(6A)C^3+6Phi^(4A)C^2P_5
           +4Phi^(4A)C^2(W_5+R_5)
           +4Phi^(2A)C P_5^2 modulo8.                 (MQ12)

All coefficients here come from the actual integer binomial expansion and the same quotient; no independent c error is selected.

The assumptions imply U|U(X^3+X).
Indeed H_0|H_0(X^3+X) follows from the prescribed forward divisibility and X|(X^3+X), while phi|(phi(X^3+X)) ensures its factor of exponent7A.
Since U=Sbar^2, irreducible multiplicities give Sbar|Sbar(X^3+X).
Monic integer division of S(C_3) by S therefore has even remainder, proving MQ3.
Squaring MQ3 gives S(C_3)^2=Q_3^2S^2 modulo4.
Using S^2=-2P-4W and3^(-1)=3 modulo4, one obtains globally

    b=2B_3 modulo4,
    b^2=4B_3^2 modulo8, 2b^5=0 modulo8.               (MQ13)

Only the congruence b/2=B_3 modulo2 is intended; the integer polynomial b/2 need not equal B_3.

### MQ5: all non-phi components

C669 gives a_bar=c_bar=0 on every H_0-primary component.
Their cubes are therefore zero modulo8 there, while2c^2 and3a^5 are also zero modulo8.
To deal with b^2, note that Pbar^2=phi^(2A)k^2 is divisible by H_0 because J_H^2=H_0 and J_H|k.
Furthermore P(C_3)bar^2 is divisible by H_0(X^3+X), which is divisible by H_0.
It follows directly from B_3=P(C_3)-Q_3^2P that B_3bar^2 is zero on every H_0-primary.
Equation MQ13 then proves b^2=0 modulo8 there.
Thus BOTH residuals vanish modulo8 on every non-phi component, for all bases satisfying MQ1 and the modulo4 assumption.

Monic free-coordinate modules and their primary localizations detect coefficientwise vanishing as in C669.
The nilpotent element2 lies in every maximal ideal, whose residue factors are exactly the irreducibles of U.
No unreduced root evaluation is substituted for global polynomial remainder congruences.

### MQ6: the complete second quarter and two divisor corrections

Work at phi in Q_8, the localization of (Z/8Z)[X]/T at polynomials whose reductions are prime to phi.
Here mathcal_H is a unit and

    Phi^(7A)=-(2P+4W)/mathcal_H.

Combine MQ10, MQ12 and MQ13.
First use the actual division sC^3-K^6=Phi^A L_s+2M_s in MQ4, then apply the SAME divisor relation to the term Phi^(7A)L_s.
This gives

    X_s=2E_s/mathcal_H+4B_s modulo8,
    B_s=-W L_s/mathcal_H+sPhi^(6A)C^3
          +Phi^(2A)(s C P_5^2-K^2Xi^2)
          +sPhi^(4A)C^2(W_5+R_5)+B_3^2.              (MQ14)

The sPhi^(6A)C^3 term records the coefficient5 in MQ12; it would be lost by replacing c with its reduction or a modulo4 approximation.
The polynomial E_s is exactly the one specified in MQ4.

The assumed actual X_s=0 modulo4 implies2E_s/mathcal_H=0 in Q_4.
Monicity gives the unique module half modulo2, so E_sbar=0 in B_phi.
Equivalently phi^(7A)|E_sbar as a POLYNOMIAL.
Hence the remainder of actual integer division by Phi^(7A) is even, justifying the L_E,M_E in MQ4.
Substitution into MQ14 gives

    2E_s/mathcal_H
       =2Phi^(7A)L_E/mathcal_H+4M_E/mathcal_H
       =-4P L_E/mathcal_H^2+4M_E/mathcal_H modulo8.    (MQ15)

The term -8W L_E/mathcal_H^2 disappears only at this step.
Because monic free modules have ann(4)=2Q_8 after localization, the legitimate quarter of MQ14--MQ15 reduces uniquely modulo2.
Its expansion is precisely MQ6, including both w L_s/H_0 and phi^A k L_E/H_0^2.
All denominators are actual localized units and all integer halves were taken before reduction.
The first quarter MQ5 is exactly C603 FE4 with H=mathcal_H and this same C, so it supplies no separate new first-error theorem.

### MQ7: shared8V correction, count and applicability boundary

Apply C202's actual changing-divisor identity to T^+=T+8V.
It gives

    a(T^+)=a(T)+4rem_U(v^2) modulo8,
    b(T^+)=b(T), c(T^+)=c(T) modulo8,
    O_F(T^+)=O_F+a_bar^4v^2,
    O_X(T^+)=O_X+a_bar^2v^2.                           (MQ16)

Globally a_bar is zero away from phi, and equals phi^(2A)k^2 at phi.
Thus a_bar^4=0 on the ENTIRE reduced quotient, and the first quarter cannot be changed by8V.
The second changes only at phi, by phi^(4A)k^4v^2.
This proves both directions of MQ7--MQ8 with one shared correction, using the already verified non-phi vanishing.
The square map at precision3A fixes v modulo phi^(3A/2) when soluble.
It has rank3A over F_2, and all other primary coordinates remain free.
Hence exactly2^(d-3A) degree<d correction classes v work when the criterion holds.

Changing the integer representative T by8V_0 leaves O_F unchanged and translates O_X by phi^(4A)k^4v_0^2.
This is precisely C202's base translation, preserving the obstruction and solution count.
It does not erase the dependence on the earlier K,W choice of T modulo8.
In particular every part of O_X below phi^(4A), and the entire O_F, must already be correct before the final8V step.

For a C667/C668 canonical input at actual q>=2, the matching parameters remain A=2mq, Y=Y_0^q and d=q(30m+degY_0).
C672 gives modulo4 bases in that actual domain; the new count, when nonempty, is2^(q(24m+degY_0)).
No quotient of q or integer layer multiplicities is used.
The characteristic-two canonical remainder, original layer weight12mq, strict canonical degree gap q(5m-Q-5degH), and global maximal q remain those of the same fixed input.
The next tests MQ7 have not been shown to pass or fail on all such bases, and no particular passing modulo8 base is asserted here.
The C202 stability of actual G_can modulo8 under8V does not identify it with the independently constructed synthetic G_int.
No characteristic-zero residual identities, irreducibility, total reality, original realization, new A_0 exclusion or Task completion follows.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:53 |
| status | open |
| reason | Register the exact square-input second quarter, actual dyadic coefficient and C5 Taylor correction through modulo8, complete integer half-remainders with two changing-divisor terms, all non-phi vanishing and the full shared8V criterion/count using the adopted first-error and coupled-map interfaces. No passing modulo8 base, native computation, higher iteration or original realization is asserted. Fresh isolated whole review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual next-layer theorem](#statement) | MQ1--MQ8, every actual even A and square complete input in the stated polynomial domain, full S/K/W and actual modulo4 base, exact integer auxiliaries/divisions, both quarters, all-primary iff, count, representative boundary and original costs. |
| argument | [Whole second-quarter proof](#argument) | MQ9--MQ16, actual global dyadic expansion, square Taylor and C5 cube, genuine C3 division and all other primaries, both divisor corrections and legitimate quarter, exact shared correction and all applicability limits. |
| dependency | [Actual modulo4 and root interface](Yin_C_G0669_v1.md#statement) | Verified factorized-base input, all-primary reductions, K^6=C_0^3 at precision4A, actual even first division and the known modulo4 root/error interface; a,c are never independent coordinates. |
| dependency | [Adopted exact first quarter](Yin_C_G0603_v1.md#statement) | FE3--FE4 at H=mathcal_H with the actual C and T: entire first-quarter formula MQ5, including its changing-divisor term; no new proof or independence assertion for that first error. |
| dependency | [Adopted same-input correction and fibers](Yin_C_G0202_v1.md#coupled-layer-statement) | CL3--CL4 and actual CL6--CL12, one8V correction, both residue changes, exact rank/count and integer representative invariance; specialized only after all components are checked here. |
| support | [Adopted square modulo4 existence](Yin_C_G0672_v1.md#statement) | Supplies actual square-family bases for all stated inputs and every q>=2 canonical application; its modulo8 coefficient counts are not residual solutions modulo8. |
| support | [Full canonical original cost interface](Yin_C_G0667_v1.md#statement) | Application only: actual U_0^q and maximal q, all degree/root/layer and synthetic integer data; no identification G_int=G_can. |
| support | [Both complete synthetic families](Yin_C_G0668_v2.md#statement) | Application only via C672 at actual q>=2, preserving every normalized parameter, factor and original degree/layer cost; no passing new quarter is imported. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:05 |
| status | proved |
| reason | Adopt the entire next-layer theorem after full main reading and fresh isolated whole R896. The actual dyadic and C5 expansions, every retained coefficient and Taylor term, three legitimate integer divisions and both changing-divisor contributions give the complete second quarter for the same T. All non-phi residuals vanish modulo8, so the reused first quarter and shared8V map give a full necessary-and-sufficient criterion and exact nonempty fiber count. No particular modulo8 base is proved to pass this criterion by this theorem; all q/layer/degree and original-realization limits remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual next-layer theorem](#statement) | MQ1--MQ8, every actual even A and square complete input in the stated polynomial domain, full S/K/W and actual modulo4 base, exact integer auxiliaries/divisions, both quarters, all-primary iff, count, representative boundary and original costs. |
| argument | [Whole second-quarter proof](#argument) | MQ9--MQ16, actual global dyadic expansion, square Taylor and C5 cube, genuine C3 division and all other primaries, both divisor corrections and legitimate quarter, exact shared correction and all applicability limits. |
| dependency | [Actual modulo4 and root interface](Yin_C_G0669_v1.md#statement) | Verified factorized-base input, all-primary reductions, K^6=C_0^3 at precision4A, actual even first division and the known modulo4 root/error interface; a,c are never independent coordinates. |
| dependency | [Adopted exact first quarter](Yin_C_G0603_v1.md#statement) | FE3--FE4 at H=mathcal_H with the actual C and T: entire first-quarter formula MQ5, including its changing-divisor term; no new proof or independence assertion for that first error. |
| dependency | [Adopted same-input correction and fibers](Yin_C_G0202_v1.md#coupled-layer-statement) | CL3--CL4 and actual CL6--CL12, one8V correction, both residue changes, exact rank/count and integer representative invariance; specialized only after all components are checked here. |
| support | [Adopted square modulo4 existence](Yin_C_G0672_v1.md#statement) | Supplies actual square-family bases for all stated inputs and every q>=2 canonical application; its modulo8 coefficient counts are not residual solutions modulo8. |
| support | [Full canonical original cost interface](Yin_C_G0667_v1.md#statement) | Application only: actual U_0^q and maximal q, all degree/root/layer and synthetic integer data; no identification G_int=G_can. |
| support | [Both complete synthetic families](Yin_C_G0668_v2.md#statement) | Application only via C672 at actual q>=2, preserving every normalized parameter, factor and original degree/layer cost; no passing new quarter is imported. |
| review | [Independent entire modulo-eight error finding](../audits/reviews/Yin_R_G0896_v1.md#whole-square-mod-eight-error-finding) | Whole MQ1--MQ16 and all statement/proof sections, complete actual integer expansions/divisions/quarters, every primary, exact first-error applicability, shared correction, square-image iff/fibers and all actual-q/source boundaries. |
