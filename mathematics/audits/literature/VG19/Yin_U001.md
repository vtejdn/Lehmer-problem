---
author: Yin
---

<a id="vg19-u001"></a>
# VG19-U001: the claimed Lehmer proof and its algebraic identification gaps

## Edition and inspection scope

The [retained v2 edition](readme.md) is the sole proof-claim input assessed here.
The assigned source contributor inspected pages 1--2, 4, 61--69 and 87--96, including rendered pages; root separately inspected the rendered pages 4 and 92--94.
These are bounded source and argument inspections, not a whole-paper audit, a review of the earlier edition, or acceptance of the advertised conclusion.
The source's reference [67], Dutykh--Verger-Gaugry, Research in Number Theory 7:64 (2021), is cited for further details but was not inspected.
The separate [R1085 review](../../reviews/Yin_R_G1085_v1.md) inspected the original page 4, pages 61--68 and 92--96 and independently assessed the three local objections below.
Its source-first findings do not extend to the page-87--88 composition treatment or to original proofs in references [67], [81] and [102].

## Actual composition restriction

Important Nota (N)(A), page 4, restricts the main statements through Section 7 to minimal polynomials not of the form P_tilde(X^r) with r>=2.
Proposition 5.29, page 63, repeats that condition.
Section 5.9.1, pages 87--88, separately treats compositions using the dynamical degree of beta^r and the corresponding Parry function.
A radical family's degree-versus-dynamical-degree comparison therefore cannot be applied unchanged as a counterexample to this edition's main case.

<a id="house-to-original-field"></a>
## Theorem 6.1: the displayed field map cannot exist

Theorem 6.1, pages 92--93, takes a nonreal reciprocal algebraic integer alpha, with beta=house(alpha)>1, the stated upper house and Mahler bounds, and dynamical degree at least260 for its additional conclusions.
One conclusion is equality of the original minimal polynomials P_alpha and P_beta.
The argument on page 94 passes from (6.1.10) to (6.1.11) by introducing a Q-endomorphism sigma of

    K=Q(alpha,beta,beta^(-1))=Q(alpha,beta),
    F=Q(beta,beta^(-1))=Q(beta),

which sends alpha^(-1) to beta^(-1) and leaves F invariant.
The displayed calculation additionally keeps beta^(-1) fixed.

This map is impossible even under the weaker setwise interpretation of invariance.
The number field F is real and K contains the nonreal alpha, so F is a proper subfield of K.
A Q-endomorphism of K is injective and, by finite dimension, surjective.
But the asserted images give

    sigma(K)=Q(sigma(alpha),sigma(F)) subset F,

contradicting surjectivity onto K.
Under pointwise fixing, injectivity already fails on the nonzero element alpha^(-1)-beta^(-1).
Moreover any Q-field homomorphism sending alpha to beta would already imply P_alpha=P_beta, which is the conclusion this step is meant to prove.

The [independent field-identification finding](../../reviews/Yin_R_G1085_v1.md#field-identification) confirms this exact objection.
Thus the displayed step supplies no valid house-to-original-polynomial identification.
It cannot support the subsequent unrestricted Mahler comparison through Sections 6.2--6.3 as written.
This is an objection to a specific proof step under its stated hypothetical inputs; it asserts neither that such near-one inputs exist nor that the theorem's conclusion or Lehmer's conjecture is false.

<a id="real-case-proof-obligations"></a>
## Separately located real-case obligations

The source contributor identified two further local concerns in Section 5.4.2; they are not needed for the preceding field-map objection.
In equations (5.4.9)--(5.4.14), pages 61--62, the tail is grouped into analytic sums

    g_(q,j)(z)=sum_(k>=0)t_(q+1+j+kd) z^(kd).

The argument then identifies their values at beta^(-1) with integer rewriting coefficients by comparison in a Q-basis.
The displayed regrouping only gives equality of scalar sums; it does not establish that the analytic values are rational, which is needed for that coordinate comparison.
For example linear independence of 1 and sqrt(2) over Q does not prevent the real-coefficient relation -sqrt(2)*1+1*sqrt(2)=0.
The unestablished coefficient identity is used by Proposition 5.28 on page 63.
The [independent rational-coordinate finding](../../reviews/Yin_R_G1085_v1.md#rational-coordinate-identification) confirms that this displayed inference lacks its needed rationality premise.

In Proposition 5.29, pages 67--68, the cited representation result supplies a finite alphabet separately for each gamma_s.
The uniform alphabet bound following (5.4.29) is not obtained from the two displayed upper height bounds, and the preceding equality is after algebraic specialization rather than an identity of polynomials.
The asserted uniform alphabet and leading-index control needed for (5.4.32) therefore require an additional argument.
The [independent uniform-alphabet finding](../../reviews/Yin_R_G1085_v1.md#uniform-alphabet-inference) confirms the failure of that inference at the displayed scope.
These are bounded local proof concerns; possible arguments in the uninspected reference [67] have not been assessed.

## Use in G0001

The inspected chain is not adopted as an unrestricted positive-gap theorem.
The established source restrictions must be respected, and the identified algebraic steps must be repaired or replaced before the claimed comparisons can be used.
Other analytic portions of the paper are not declared false by these findings and would need their own exact inspection and applicability checks.
