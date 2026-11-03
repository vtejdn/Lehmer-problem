---
author: Yin
---

# Uniform phase gap for varying low-energy integer seeds

Human author Yin.
Root supplied the degree-uniform regularized phase construction and constant-seed extension.
Contributor core_feedback_structure checked the complete seed margin, phase factorization, bounded regularized Fubini, finite coefficient specialization, ordered cutoff, zero-value guard, original norm expenses and scale boundaries.
Both are proof contributors.
This project deduction is [adopted](#decision-whole-reviewed-2026-10-28) after [whole independent R1065](../audits/reviews/Yin_R_G1065_v1.md#whole-varying-seed-phase-finding) at the complete fixed scope below.
The [D7 source section](../drafts/Yin_D_G0007.md#uniform-varying-seed-phase-gap) supplies extraction provenance only; the entire necessary proof is fixed below, with no mutable Draft premise.

## Statement

Fix an integer q>=2.
An allowed seed is a polynomial H in Z[x] with H(0)!=0, actual degree k>=0, sum_j H_j^2<=q^2, and H different from the two constant polynomials +q and -q.
Define its actual degree-k reversal H*(x)=x^k H(1/x), and let sigma range over{+1,-1}.
The seed may vary with the original input, need not be monic or reciprocal, and is not required to belong to a fixed finite family.
The allowed degree-zero seeds are exactly the integer constants with0<|H|<=q-1.
All energies and coefficient lengths concern true collected coefficients, and all torus integrals use normalized Haar measure.

Use the q-only constants

    B=q^2+1, delta=1/(2q^2 B), eta=1/(8q^4 B^2),
    delta_p=delta*eta, B_p=4q^2+1,
    J_p=ceil(B_p/(eta*delta_p^2)),

and the exact inherited finite-frequency modulus

    c0=log2/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0)log sqrt(c0/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0.

There is a computable positive dyadic rational u_q depending only on q such that

    J_p u_q<h0,
    (1+2q/delta_p)u_q+2^(J_p)epsilon(J_p u_q)<eta,
    (2q^2-1)epsilon(u_q)+4q^2 u_q<1.

The [ordered algorithm](#ordered-cutoff-and-original-norm) certifies the domain inequality BEFORE evaluating either epsilon term, then certifies the remaining two strict inequalities.
Every such u_q has the conclusions below.

**A. Uniform field-free phase certificate.**
For every allowed H and either sign, put f(z,w)=(wH(z)+sigma H*(z))/q and f^dagger(z,w)=f(z^(-1),w^(-1)).
Then

    (1/2)integral_T log(|H/q|^2+delta^2)<=-3eta,
    (1/2)integral_(T^2)log(|f|^2+delta_p^2)<=-5eta/2.

The finite Laurent polynomial

    Y=1-(f f^dagger+delta_p^2)/B_p,
    Phi=(1/2)log B_p-(1/2)sum_(j=1..J_p)Y^j/j

satisfies CT_(z,w)Phi<-2eta.
Its Fourier support has |a|<=kJ_p, |b|<=J_p, so for every positive integer n>kJ_p,

    CT_x Phi(x,x^n)=CT_(z,w)Phi<-2eta.

These parameters and negative margins are independent of H, k, sigma and n.
The identity is exact finite coefficient collection, and no singular specialization limit is assumed.

**B. Original-degree arithmetic exclusion, including a possible zero value.**
Let alpha be any ACTUAL nontorsion algebraic integer unit, P its monic irreducible minimal polynomial, d>=2 its ORIGINAL degree, and m=m(P)>0 its TOTAL logarithmic Mahler measure.
All original d embeddings and every actual powered-field multiplicity are retained.
For every allowed H, either sign and every positive integer n>kJ_p, set

    F_n(x)=x^n H(x)+sigma H*(x), T=n+k.

If F_n(alpha)/q is algebraically integral over Z in Q(alpha), allowing the value zero, then

    T*m/d>u_q.

Algebraic integrality in the full number field is sufficient; membership in Z[alpha] is not required.
The polynomial F_n is nonzero and has true degree and span exactly T>0.
Its number of nonzero terms and effective support are at most2q^2 and its coefficient length is at most2q^2.
The value-zero alternative is excluded by C92 under the contradictory small-height assumption BEFORE a norm logarithm is used.

**C. Uniform conditional class gap in every original degree.**
For each fixed C>0, every actual P admitting the data of B with the additional original window n+k<=C*d satisfies

    m(P)>u_q/C.

The constant is independent of every seed and original degree in this class.
P need not be reciprocal and H need not be monic.
Allowed constant seeds and both signs remain included, with k=0 requiring only n>0.
No low-degree enumeration or bounded-degree completion is needed.

**D. Costs and scope.**
The proof retains the complete radial multiplier1+2q/delta_p, Fourier range J_p T, coefficient price2^(J_p), raw scaling delta_raw=q delta_p and B_raw=q^2 B_p, full signed original norm, and finite matrix size2J_p T+1.
A q-only certificate parameter does not give a bounded matrix size as T grows.
The excluded constants +/-q fail the negative seed margin and make the quotient value automatically integral; no extension to those seeds is asserted.
The actual separation n>kJ_p and integrality/window hypotheses remain necessary assumptions of this statement, without a claim that every possible proof needs the same separation.
The conclusion supplies no automatic seed construction for arbitrary P, periodic-block application, efficient numerical constant, uniform varying-q gap or unrestricted Mahler gap.

## Complete argument

<a id="varying-seed-setting-and-reuse"></a>
### UP1. Preparation, exact scope and reused inputs

The question is whether a finite phase certificate can be uniform over integral seeds whose degrees and exponent patterns vary, rather than over the fixed finite seed family of [C842 EF2--EF5](Yin_C_G0842_v1.md#effective-fixed-reversal-auxiliary-gap).
C842 already supplies the two-variable finite Taylor mechanism, exact frequency separation and raw integral scaling; these mechanisms are reused, not claimed anew.
Its fixed finite family and eventual negative-margin search do not themselves give parameters independent of the varying seed degree.
The [adopted C844](Yin_C_G0844_v1.md#decision-whole-reviewed-2026-10-28), specifically its [field-free ER3 calculation](Yin_C_G0844_v1.md#uniform-energy-logarithmic-margin), supplies the required q-only regularized seed margin for every nonmonomial of coefficient energy at most q^2.
The short calculation below recalls that margin and pays the additional constant-seed case.
No algebraic-integrality premise is used in this field-free seed calculation.

The eventual arithmetic inputs are [C137 Sections1--2 and equations1--7](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument), [C92's short rational annihilator inequality](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support), and [C570's actual finite-frequency modulus and original powered-field multiplicities](Yin_C_G0570_v1.md#uniform-powered-angular-coherence).
The classical scalar Jensen normalization is the checked [Smy08-U001 passage](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization); its source inspection limits are unchanged.
The only phase integral used here follows from the explicit positive factorization in UP3, so no singular multivariate limit or additional external theorem is needed.
These exact retained interfaces suffice for this extension; no BS13 constant, BGMP or Turan estimate, Lawton convergence rate, finite seed classification or bounded-degree C394 completion is invoked.
No new source acquisition or native computation is an input, and no novelty claim is made.

Fix an integer q>=2.
An allowed seed is any H in Z[x] with H(0)!=0, actual degree k>=0, coefficient energy sum_j H_j^2<=q^2, and H different from the two constant polynomials +q and -q.
Its degree-k reversal is H*(x)=x^k H(1/x), and sigma is either +1 or -1.
The seed need not be monic or reciprocal and may vary with the original input.
For a positive integer n define

    F_n(x)=x^n H(x)+sigma H*(x), T=n+k.                 (UP1)

Let alpha be an ACTUAL nontorsion algebraic integer unit, P its monic irreducible minimal polynomial, d>=2 its ORIGINAL degree, and m=m(P)>0 its TOTAL logarithmic Mahler measure.
All original d embeddings and every genuine powered-field repetition are retained.
The value F_n(alpha)/q is assumed algebraically integral over Z in Q(alpha), allowing zero; membership in Z[alpha] is not required.
We will give positive q-only rational delta_p, eta, an integer J_p>=1 and a computable positive dyadic u_q such that

    n>k J_p  implies  (n+k)m/d>u_q.                    (UP2)

Thus for any fixed C>0, the additional original window n+k<=C*d implies m(P)>u_q/C in ALL original degrees.
Both signs, every allowed constant seed and every varying positive-degree seed are included.
The separation n>kJ_p and the actual integrality/window premises remain hypotheses, with no automatic construction of such a certificate for an arbitrary P.

<a id="uniform-seed-margin-including-constants"></a>
### UP2. One q-only regularized seed margin, including constants

Set

    B=q^2+1,
    delta=1/(2q^2 B),
    eta=1/(8q^4 B^2), delta^2=2eta,
    delta_p=delta*eta, e=delta^2, a=delta_p^2/e=eta^2.   (UP3)

All of these quantities are positive rationals depending only on q, and delta_p<1.
On the unit circle with normalized Haar measure put W=|H/q|^2.
Integer coefficients and the energy bound imply

    #supp(H)<=q^2, ||H||_1<=q^2,
    integral W<=1, 0<=W<=q^2.

If k>0, the two endpoint coefficients H_0 and H_k are nonzero, so H has at least two terms.
The Fourier coefficients of W at lags +/-k are H_0 H_k/q^2 and each has absolute value at least1/q^2.
Consequently Parseval gives Var(W)>=2/q^4, independently of k and of collisions at interior lags.
For0<x,mu<=B, strong concavity gives

    log x<=log mu+(x-mu)/mu-(x-mu)^2/(2B^2).

Indeed the difference of the left side and right side has nonpositive second derivative and value and first derivative zero at mu.
Applying this to x=W+delta^2 and mu=integral W+delta^2, integrating and using log(1+delta^2)<=delta^2 gives exactly C844's bound

    (1/2)integral log(W+e)
       <=delta^2/2-1/(2q^4 B^2)=-3eta.                (UP4)

If k=0, write H=A with integer0<|A|<=q-1, using the exclusion of +/-q.
Then W=A^2/q^2<=(q-1)^2/q^2<=1-1/q, while e<=1/(2q).
Hence

    (1/2)log(W+e)<= (1/2)log(1-1/(2q))
                       <=-1/(4q)<=-3eta.

The final inequality follows from3<=2q^3(q^2+1)^2 for q>=2.
Thus UP4 holds for EVERY allowed seed, including constants, with exactly the same q-only margin.
No seed's minimum modulus or zero separation has been used.

<a id="regularized-phase-factorization"></a>
### UP3. The uniform two-variable regularized phase mean

Use independent circle variables z,w and put

    F(z,w)=wH(z)+sigma H*(z), f(z,w)=F(z,w)/q.

For H(z)!=0 let v(z)=H*(z)/H(z), which has modulus1 because H has real coefficients and H*(z)=z^k conjugate(H(z)).
Write x=W(z) and y=|w+sigma v(z)|^2; then |f(z,w)|^2=x*y.
At a zero of H on the circle the reversed polynomial also vanishes, so the same equality holds with x=0 and any assigned unit value of v.
There are only finitely many such z, and this assignment is measurable.
For every x,y>=0 the positive constants in UP3 satisfy the elementary inequality

    xy+delta_p^2 <= (x+e)(y+a),                         (UP5)

since ea=delta_p^2 and the two extra cross terms are nonnegative.
All logarithms to be integrated are bounded after regularization, so ordinary Fubini is legitimate.

For a>0 put s=(sqrt(a+4)+sqrt(a))/2>1.
Then s-s^(-1)=sqrt(a), and after a rotation of the w variable

    y+a = a+2-2 Re w = |s-s^(-1)w|^2.

The linear polynomial s-s^(-1)w has its zero at s^2>1, so scalar Jensen gives

    (1/2)integral_w log(y+a)=log s<=sqrt(a)/2.          (UP6)

For the last inequality, the function (s-s^(-1))/2-log s vanishes at1 and has derivative (s-1)^2/(2s^2)>=0 for s>=1.
This proves the exact integral and bound directly, uniformly in z and sigma, with no limiting or small-value estimate.
Integrating the logarithm of UP5, then applying UP4 and UP6 with sqrt(a)=eta, yields

    (1/2)integral_(T^2)log(|f|^2+delta_p^2)
       <=-3eta+eta/2=-5eta/2.                         (UP7)

The margin remains uniform over all allowed seed degrees and coefficients.

<a id="finite-majorant-and-exact-specialization"></a>
### UP4. A uniform finite majorant and exact separated specialization

The coefficient length of f is2||H||_1/q<=2q, so |f|<=2q on the torus.
Define the q-only parameters and the actual finite Laurent polynomials

    B_p=4q^2+1,
    J_p=ceil(B_p/(eta*delta_p^2)),
    Y=1-(f f^dagger+delta_p^2)/B_p,
    Phi=(1/2)log B_p-(1/2)sum_(j=1..J_p)Y^j/j.        (UP8)

Here f^dagger(z,w)=f(z^(-1),w^(-1)), equal to complex conjugation on the torus; it is different from the degree-k polynomial reversal H*.
Because delta_p^2<1, one has0<=Y<=1-delta_p^2/B_p<1.
The positive logarithm-series tail, exactly as in C137 and C842, satisfies

    0<=Phi-(1/2)log(|f|^2+delta_p^2)
      <=B_p/[2(J_p+1)delta_p^2]<eta/2.

The strict final inequality follows from J_p+1>B_p/(eta*delta_p^2), even if that rational number is already an integer.
Combining this uniform tail with UP7 gives

    c_H,sigma:=CT_(z,w)Phi<-2eta.                      (UP9)

The nonlogarithmic coefficients of Phi are rational and obtained by finite Laurent-polynomial arithmetic.
The only displayed transcendental coefficient is(log B_p)/2.
The proof supplies uniform strict negativity, so neither an enumeration of seeds nor a separate search for each seed's negative margin is necessary.

Every exponent of f has z coordinate between0 and k and w coordinate0 or1.
Thus the support of f f^dagger has |a_0|<=k, |b_0|<=1, and every exponent of Phi satisfies |a_0|<=kJ_p, |b_0|<=J_p.
If n>kJ_p, the equality a_0+n b_0=0 forces b_0=0, then a_0=0.
It follows by exact finite coefficient collection that

    CT_x Phi(x,x^n)=c_H,sigma<-2eta.                   (UP10)

This is an identity of finite coefficients, not an asymptotic torus specialization claim.
For k=0 it holds for every positive integer n; the condition remains n>0.
Since J_p>=1, the assumed n>kJ_p also gives n>k, so the support blocks0,...,k and n,...,n+k in F_n are disjoint.
Its endpoint coefficients are sigma H_k and H_k, both nonzero; hence F_n is nonzero and its TRUE degree and span are exactly T=n+k>0.
Its complete coefficient bounds are

    #supp(F_n)=2#supp(H)<=2q^2,
    ||F_n||_1=2||H||_1<=2q^2,
    rho(F_n)=||F_n||_1^2/||F_n||_2^2<=2q^2.          (UP11)

No cancellation or reduced auxiliary degree is used to remove a cost.

<a id="ordered-cutoff-and-original-norm"></a>
### UP5. Ordered computable cutoff and zero before the full norm

Use precisely C137/C92's inherited finite-frequency modulus

    c0=log2/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0)log sqrt(c0/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0.

It is increasing on this specified positive domain, computable there by certified intervals, and tends to0 as u decreases to0.
Choose a positive dyadic u_q satisfying

    J_p u_q<h0,
    (1+2q/delta_p)u_q+2^(J_p)epsilon(J_p u_q)<eta,
    (2q^2-1)epsilon(u_q)+4q^2 u_q<1.                 (UP12)

The constants J_p, delta_p and eta depend only on q, so such a u_q exists.
An algorithm dovetails dyadic candidates2^(-N), N>=1, and rational interval precisions.
FIRST certify J_p2^(-N)<h0 for a candidate; evaluate epsilon at that candidate and J_p times it only after this domain certificate is obtained.
Then certify the two remaining strict inequalities by interval upper bounds and accept a candidate only when both pass.
Elementary logarithms, exponentials and square roots admit convergent rational bounds, and some sufficiently small candidate has strict margins in all tests, so this algorithm terminates without deciding a boundary equality.
No numerical value or execution of this potentially very expensive search is asserted.

Put h=T*m/d and suppose for contradiction0<h<=u_q.
If F_n(alpha)=0, C92 applies to the actual nonzero rational polynomial F_n of positive span T and effective support bounded in UP11.
It forces

    1<=(rho(F_n)-1)epsilon(h)+2rho(F_n)h
       <=(2q^2-1)epsilon(u_q)+4q^2 u_q<1,

which is impossible.
Only after this zero exclusion do we use algebraic integrality to obtain the FULL ORIGINAL signed identity

    Res(P,F_n)=q^d N,
    N=Norm_(Q(alpha)/Q)(F_n(alpha)/q) in Z minus{0}.    (UP13)

Thus log|Res(P,F_n)|/d>=log q, without an order-membership restriction or deletion of original conjugates.
For C137 choose the raw parameters

    delta_raw=q delta_p, B_raw=q^2 B_p,
    S_raw=||F_n||_1<=2q^2.

They satisfy B_raw>=S_raw^2+delta_raw^2 because B_p=4q^2+1 and delta_p^2<1.
The raw Y is the specialization Y(x,x^n), and the raw finite logarithmic majorant is log q+Phi(x,x^n).
C137's full original-root inequality, the exact UP10 constant and UP12 therefore give

    0<=c_H,sigma+(1+S_raw/(q delta_p))h
                         +2^(J_p)epsilon(J_p h)
      <=c_H,sigma+(1+2q/delta_p)u_q
                         +2^(J_p)epsilon(J_p u_q)
      <-2eta+eta=-eta<0.                              (UP14)

Every modulus evaluation lies in0<J_p h<=J_p u_q<h0.
The complete original radial multiplier, frequency range J_p T, coefficient price2^(J_p) and finite matrix size2J_p T+1 remain paid.
In particular, q-only parameters do not mean a bounded-size certificate when T grows.
This contradiction proves UP2 for every original degree d>=2, including the permitted constant seeds, with no bounded-degree patch.

<a id="all-degree-class-gap-and-scale-boundary"></a>
### UP6. Exact class consequence and remaining scale boundary

If an actual P admits an allowed H, either sign and n satisfying both n>kJ_p and n+k<=C*d, with F_n(alpha)/q algebraically integral, then UP2 gives

    m(P)>u_q/C.                                      (UP15)

The conclusion is uniform over all such H,k,n and all original degrees d, for fixed q and C.
It requires neither a finite seed family nor monicity of H or reciprocity of P.
It keeps the value-zero branch and all original degrees, rather than using a finite low-degree completion.
This is an assembly of the existing finite phase transfer and the new degree-uniform seed regularization, with the complete scale and arithmetic hypotheses retained.

The exclusion H=+/-q is essential to the negative seed margin: these constants have W=1, while F_n(alpha)/q=+/-alpha^n plus a signed1 is automatically integral for every actual unit.
Allowing them would remove the substantive seed restriction and give an unrestricted gap from the same argument; UP4 and UP7 do not hold for those excluded seeds.
No such unrestricted conclusion or refutation of the unrestricted gap is asserted.
The hypothesis n>kJ_p is the actual separation used by UP10; no claim is made that it is necessary for every possible proof, or that failure of it refutes a gap.
Replacing a seed by H(x^r) and n by rn multiplies both n and k by the same positive integer r, so this substitution alone leaves n/k unchanged when k>0 and cannot purchase the missing separation.
When an actual radical construction also multiplies the original degree by r, the ratio (n+k)/d is likewise unchanged; that degree multiplication must be verified for the actual minimal polynomial and is not automatic.
No periodic-block application, general seed-production theorem, efficient numerical constant, uniform varying-q result or unrestricted Lehmer conclusion is supplied here.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision uniform-varying-seed-phase-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T22:27 |
| status | open |
| reason | Fix the complete UP1--UP6 argument and Statement A--D for a q-only phase certificate over all varying-degree low-energy integer seeds with H(0) nonzero and the two saturated constants excluded, both signs and allowed constants, exact n>kJ_p separation, ordered computable cutoff, zero-before-norm guard and all-original-degree conditional gap. Separate whole independent review and adoption remain outstanding; no periodic application or unrestricted input coverage is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete uniform phase statement](#statement) | Entire fixed-q seed domain, actual reversal, all signs/constants, computable parameters, field-free finite certificate, exact separation, original-unit/full-degree/full-integrality arithmetic hypotheses, all-degree window gap and all A--D costs and limitations. |
| argument | [Complete UP1--UP6 argument](#complete-argument) | All fifteen formulas: original varying-seed setting, constant and nonmonomial margin, bounded regularized phase factorization, exact finite Taylor/specialization proof, positive-domain dyadic algorithm, C92 zero guard, original signed norm and C137 costs, plus scale and excluded-seed boundaries. |
| dependency | [Uniform regularized scalar seed margin](Yin_C_G0844_v1.md#uniform-energy-logarithmic-margin) | Adopted ER3 field-free endpoint-variance/strong-concavity calculation through ER5 only: every nonmonomial integer H with coefficient energy at most q^2 has the q-only regularized margin. Its arithmetic, family and scalar-class conclusions are not needed; the allowed constant case is proved here. |
| dependency | [Finite logarithmic original-root certificate](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) | Sections1--2 and equations1--7 only: finite majorant and tail, raw delta/B conditions, complete original radial expense, coefficient price2^J, exact finite-frequency domain and full nonzero algebraic-integer norm floor. No special seed family or bounded-degree completion. |
| dependency | [Short rational annihilator inequality](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Effective-support inequality for a nonzero rational polynomial with positive actual span vanishing at the original unit; used with support at most2q^2 before taking any norm logarithm. |
| dependency | [Exact finite-frequency modulus](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact c0,h0,b,epsilon, monotonicity and zero limit on the positive domain, negative-frequency convention and all original powered-field repetitions; inherited Pri11/Dim19 source-inspection limits unchanged. |
| dependency | [Scalar Jensen and Mahler normalization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | The smy08-height-normalization subsection: checked scalar factorwise Jensen applied only to s-s^(-1)w with s>1, and total logarithmic measure/unit conventions. The positive phase factorization and every estimate are supplied locally; no deeper source theorem is imported. |
| support | [Existing finite two-phase method](Yin_C_G0842_v1.md#effective-fixed-reversal-auxiliary-gap) | Method attribution/comparison for EF2--EF5 finite Taylor majorants, exact frequency separation and raw scaling; its fixed finite seed family and its bounded-degree completion are not logical premises of this varying-seed theorem. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T22:41 |
| status | proved |
| reason | Adopt the complete Statement A--D and UP1--UP6 proof after root read the entire author argument, fixed statement and fresh whole independent R1065. The uniform varying-degree seed margin includes both signs, circle zeros and allowed constants; bounded regularized Fubini, exact phase factorization, finite Taylor specialization, ordered computable cutoff, zero-before-norm guard and every original norm/radial/frequency expense are covered. The resulting conditional gap holds in every original degree under the actual separation, full algebraic-integrality and degree-window hypotheses. No periodic application, varying-q uniformity, practical numerical constant or unrestricted input coverage is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete uniform phase statement](#statement) | Entire fixed-q seed domain, actual reversal, all signs/constants, computable parameters, field-free finite certificate, exact separation, original-unit/full-degree/full-integrality arithmetic hypotheses, all-degree window gap and all A--D costs and limitations. |
| argument | [Complete UP1--UP6 argument](#complete-argument) | All fifteen formulas: original varying-seed setting, constant and nonmonomial margin, bounded regularized phase factorization, exact finite Taylor/specialization proof, positive-domain dyadic algorithm, C92 zero guard, original signed norm and C137 costs, plus scale and excluded-seed boundaries. |
| dependency | [Uniform regularized scalar seed margin](Yin_C_G0844_v1.md#uniform-energy-logarithmic-margin) | Adopted ER3 field-free endpoint-variance/strong-concavity calculation through ER5 only: every nonmonomial integer H with coefficient energy at most q^2 has the q-only regularized margin. Its arithmetic, family and scalar-class conclusions are not needed; the allowed constant case is proved here. |
| dependency | [Finite logarithmic original-root certificate](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) | Sections1--2 and equations1--7 only: finite majorant and tail, raw delta/B conditions, complete original radial expense, coefficient price2^J, exact finite-frequency domain and full nonzero algebraic-integer norm floor. No special seed family or bounded-degree completion. |
| dependency | [Short rational annihilator inequality](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Effective-support inequality for a nonzero rational polynomial with positive actual span vanishing at the original unit; used with support at most2q^2 before taking any norm logarithm. |
| dependency | [Exact finite-frequency modulus](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact c0,h0,b,epsilon, monotonicity and zero limit on the positive domain, negative-frequency convention and all original powered-field repetitions; inherited Pri11/Dim19 source-inspection limits unchanged. |
| dependency | [Scalar Jensen and Mahler normalization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | The smy08-height-normalization subsection: checked scalar factorwise Jensen applied only to s-s^(-1)w with s>1, and total logarithmic measure/unit conventions. The positive phase factorization and every estimate are supplied locally; no deeper source theorem is imported. |
| support | [Existing finite two-phase method](Yin_C_G0842_v1.md#effective-fixed-reversal-auxiliary-gap) | Method attribution/comparison for EF2--EF5 finite Taylor majorants, exact frequency separation and raw scaling; its fixed finite seed family and its bounded-degree completion are not logical premises of this varying-seed theorem. |
| review | [Whole independent varying-seed phase finding](../audits/reviews/Yin_R_G1065_v1.md#whole-varying-seed-phase-finding) | Entire Statement A--D and UP1--UP6, all fifteen formulas, constant and positive-degree seeds, both signs and zeros, bounded phase integration, exact finite coefficient identity, ordered domain and computability, zero exclusion before full signed norm, all raw costs and inherited source boundaries; independent arrangement without mutable Draft or substantive repair. |

