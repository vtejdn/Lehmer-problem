---
author: Yin
---

# G0001: bounded integral matrix excess gives a sparse neutral completion

Date: 2026-10-06.
The current complete theorem and proof are at [the responsible Claim](../claims/Yin_C_G0229_v1.md#argument), with [actual whole self-review](../audits/reviews/Yin_R_G0514_v1.md#current-excess-jordan-finding).
The original mathematical body remains the fixed historical input and substantive comparison.
Coordinating AI for Yin; direct self-review only.
This develops the nonnormal route left open by [L G0024](Yin_L_G0024_v1.md#normal-integral-gap), within the [single Task](../tasks/Yin_T_G0001_v1.md#contract).
No novelty or unrestricted Lehmer claim is made.

<a id="bounded-excess-gap"></a>
## Statement and inputs

Let A belong to GL_N(Z), with N unrestricted, and put k=||A||_F^2-N.
For every fixed integer k_0>=1, matrices with k<=k_0 have either zero algebraic entropy or entropy at least eta_{K(k_0)}>0, where

    K(k)=k! 3^k 2^{k(2k-1)}.

Here eta_K is the accepted [DS17 bounded-support gap](../audits/literature/DS17/readme.md#bounded-support-gap).
The other external input is the Task's integral characteristic-polynomial entropy formula h_alg(A)=m(det(tI-A)); m is logarithmic Mahler measure, without dimension normalization.
Normality and a positive metric are not assumed.
The proof constructs a monic integer polynomial F with at most K(k) terms and exactly the same Mahler measure as A.

## Signed permutation reduction

Since det A is nonzero, its determinant expansion contains a nonzero permutation term.
Choose its matching and let P have the signs of the matched entries there and zeros elsewhere.
P is a signed permutation matrix.
Set E=A-P and let s be the number of its nonzero entries.
Entrywise integrality gives

    s <= sum_{i,j}|E_ij| <= sum_{i,j} A_ij^2-N = k.

Indeed, on matching entries |a|-1<=a^2-1; off the matching |a|<=a^2.
Thus k>=0.
If k=0, E=0 and A=P has entropy zero.
In what follows E is nonzero, so 1<=s<=k.

The permutation cycles of P are signed cycles.
A cycle of length l with sign product sigma has characteristic polynomial t^l-sigma, of Mahler measure zero.
Call a cycle active if it contains a row or column index of a nonzero entry of E.
There are r<=2s active cycles.
Every inactive cycle remains a separate invariant block of A: no row or column of E touches it.
Removing these blocks gives A_0=P_0+E_0 with exactly the same Mahler measure as A.
Put

    D(t)=det(tI-P_0)=product_{active cycles}(t^l-sigma).

It has at most 2^r terms and m(D)=0.
Its degree may be arbitrarily large.

## Determinant construction and term count

Write each of the s nonzero entries of E_0 as c_h e_{i_h}e_{j_h}^T, and form U with columns c_h e_{i_h}, V with columns e_{j_h}.
Thus E_0=UV^T.
For R=(tI-P_0)^{-1}, each entry is zero between different cycles; within one cycle it is a signed monomial divided by t^l-sigma.
This follows from

    (tI-P_cycle)^{-1}
      =(t^{l-1}I+t^{l-2}P_cycle+...+P_cycle^{l-1})/(t^l-sigma),

since exactly one of these l powers has a nonzero entry at a fixed pair of positions.
Consequently every entry of D V^T R U is an integer multiple of a monomial times the product of the other r-1 cycle binomials.
It has at most 2^{r-1} terms, including when some cycle binomials coincide.

Define the s by s polynomial matrix B=D I_s-D V^T R U and F=det B.
The matrix determinant lemma over Q(t) gives the polynomial identity

    F=D^s det(I_s-V^T R U)=D^{s-1} det(tI-A_0).

In particular F is nonzero, monic and integral, and m(F)=m(det(tI-A_0))=h_alg(A).
Each entry of B has at most 3*2^{r-1} terms (the diagonal includes D).
Expanding its determinant therefore gives

    number of nonzero terms of F
      <= s! (3*2^{r-1})^s
      <= s! 3^s 2^{s(2s-1)} <= K(k).

Coincident exponents and cancellation only decrease this bound.
Applying DS17 proves the statement; for k<=k_0 use the monotonicity of K.
Neither the number of inactive cycles nor active cycle lengths enter the bound.

<a id="complexity-escape"></a>
## Consequence and remaining obstruction

This realizes the zero-overhead special case of [L G0019](Yin_L_G0019_v1.md#controlled-entropy-completion) using an integral matrix rather than assuming a sparse characteristic polynomial.
Any hypothetical sequence A_n of integral unimodular matrices with 0<h_alg(A_n)->0 must have ||A_n||_F^2-dim(A_n)->infinity.
Otherwise a fixed-k subsequence contradicts the proved gap.

Integer conjugacy can change k; adding signed permutation blocks leaves k unchanged.
One may minimize k over all integral conjugates of all such stabilizations.
This is a nonempty set of nonnegative integers, so a minimum exists.
The same gap applies if this optimized quantity is bounded, and a hypothetical vanishing-entropy sequence forces these minima to infinity as well.
No bound on these minima in terms of small entropy is proved.

For the standard companion matrix of a monic unit polynomial p=t^d+sum_{i<d}a_i t^i, k=sum_{i<d}a_i^2-1 (also for d=1).
Thus the criterion includes familiar bounded-coefficient restrictions.
The missing step is a uniform structural compression of general small-entropy dynamics; bounded excess must not be inferred from small entropy or from a rational realization.

## Exact controls and review scope

For A=[[1,1],[1,0]], choose P=[[0,1],[1,0]].
Then E=e_11, D=t^2-1, R_11=t/(t^2-1), and F=t^2-t-1, with unchanged positive entropy.
For A=[[1,1],[0,1]], choose P=I.
There are two active length-one cycles, D=(t-1)^2, but R_21=0, so F=D and the entropy is zero despite k=1.
These are direct symbolic checks, not a computer experiment.

The original2026-10-06 formal author check is retained at [its exact finding](../audits/reviews/Yin_R_G0514_v1.md#original-excess-author-check).
The primary strategy remains algebraic entropy; the Task remains unresolved.
