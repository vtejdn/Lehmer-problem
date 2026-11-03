---
author: Yin
---

# Rational finite-entropy flows: where failure of finite capture can occur

Research-operation record, 2026-10-06, for [G0001](../tasks/Yin_T_G0001_v1.md#decision-single-task-organization), primary [algebraic-entropy strategy](../strategies/Yin_S_G0001.md).
Prepared and self-checked by the coordinating AI agent for Yin.
This is a structural diagnostic assembled from established inputs, not a claimed new Lehmer theorem or a novelty claim.
The original targeted agent review is retained at its actual R home.
The complete current reusable theorem and argument are in [C G0205](../claims/Yin_C_G0205_v1.md#argument).
The mathematical body below remains the original fixed input of [R G0003](../audits/reviews/Yin_R_G0003_v1.md#targeted-review); it is not a competing current Claim assessment.

## Reuse and question

The preceding [assessment](Yin_L_G0001_v1.md) leaves finite capture equivalent to the gap and rules out purely abstract additive-length arguments.
Could nonsemisimple extensions or an infinite zero-entropy part cause failure of capture without infinitely many small positive irreducible Mahler weights?

Use only the rational setting below.
[DGB16-U001](../audits/literature/DGB16/Yin_U001.md#dgb16-u001) supplies monotonicity, finite products, directed unions, and the infinite cyclic-orbit obstruction.
[GBV15-U001](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) supplies rational Yuzvinski and finite-set attainment on finite-dimensional rational spaces, at its recorded accepted-external-input inspection depth.
The rational prime-weight perspective already occurs in [DGB16-U003](../audits/literature/DGB16/Yin_U003.md#dgb16-u003).
The elementary primary splitting below is proved with Bezout, so no uninspected infinite-module classification is an input.

Local reuse was sufficient for the argument.
A bounded primary-source search on 2026-10-06 for "algebraic entropy Q t modules primary decomposition Pinsker finite entropy length function Lehmer" found *The Pinsker subgroup of an algebraic flow* (arXiv:1006.5120) and Lind--Schmidt--Ward's 1990 commuting-automorphism entropy paper as attribution leads.
Neither was acquired or inspected for a matching theorem in this attempt, and neither is a proof input.
The exact antecedent of this combined formulation remains an attribution follow-up, not an assertion of novelty.

<a id="rational-primary-formula"></a>
## Exact rational decomposition

Let V be a rational vector space of arbitrary dimension, A a rational linear endomorphism, and h(A)<infinity.
For each monic irreducible p in Q[t], let p_Z be its primitive integral associate with positive leading coefficient, d_p=deg p, and w_p=m(p_Z).
Set

\[
V_p=\{v\in V:p(A)^jv=0\text{ for some }j\ge1\},\qquad
\ell_p=\dim_{\mathbb Q}(V_p)/d_p\in\mathbb N\cup\{\infty\}.
\]

Then, as Q[t]-modules,

\[
V=\bigoplus_p V_p,\qquad h(A)=\sum_{p:w_p>0}\ell_p w_p.
\tag{1}
\]

Every positive-weight ell_p is finite.
Zero-weight primary components may have arbitrary dimension and contribute zero; the sum in (1) intentionally avoids the undefined notation 0 times infinity.
The sum means the supremum of finite partial sums.
At most countably many positive-weight components can occur.

**Proof.** If one v has linearly independent A-iterates, its integer orbit span is a copy of the shift on Z[t] and has infinite entropy, contradicting monotonicity.
Thus every vector is killed by a nonzero polynomial.
Factoring such a polynomial into coprime irreducible powers and applying polynomial Bezout identities splits each vector into finitely many primary components.
Bezout also proves that their sum is direct.
Every finite subset generates a finite-dimensional invariant rational space: the polynomial recurrence for each of its finitely many vectors bounds its orbit span.
These spaces form a directed union exhausting V.

For a finite-dimensional p-primary space W, its characteristic polynomial is p^ell, where dim_Q W=d_p ell.
The primitive integral characteristic polynomial is p_Z^ell: primitivity of products follows from Gauss's lemma, so the leading-coefficient contribution is retained.
Rational Yuzvinski gives h(A|W)=ell w_p.
In particular such dimensions are multiples of d_p.
Directed continuity on V_p shows h(A|V_p)=ell_p w_p for w_p>0 and zero for w_p=0.
Unbounded finite-dimensional subspaces with w_p>0 would have arbitrarily large entropy, so finite total entropy forces ell_p finite.
Finite products followed by directed continuity over finite sums prove (1).
Finally, for each n only finitely many positive summands can be at least 1/n; their countable union contains every positive summand.
This proves the countability assertion without a countability assumption on V.

<a id="capture-equivalence"></a>
## Capture criterion and consequence

For the same finite-entropy flow, the following are equivalent:

1. Some finite-dimensional invariant rational W has h(A|W)=h(A).
2. Some nonempty finite F in V satisfies H(A,F)=h(A).
3. Only finitely many p have V_p nonzero and w_p>0.

**Proof.** If (3) holds, the sum of those positive primary components is finite-dimensional by (1) and captures all entropy; this proves (1).
Finite-set attainment on that finite-dimensional space proves (2), with F={0} when h=0.
Conversely, a finite F generates a finite-dimensional invariant rational W.
Thus H(A,F)<=h(A|W).
Its primary support is finite.
If infinitely many positive primary components exist, at least one lies outside that support, and (1) gives h(A|W)<h(A), since total entropy is finite.
This contradicts (2).
The same reasoning proves (1) implies (3).

Consequently, in the rational setting, failure of finite capture requires infinitely many **distinct** positive irreducible polynomials with summable Mahler weights.
It cannot be produced by taking more and more Jordan blocks for a fixed positive polynomial, by increasing powers of that polynomial in annihilators, or by adjoining an infinite zero-entropy part.
Distinct primary factors already split; nonsplit extensions within a positive primary component cost positive integer multiples of its fixed weight and exhaust finite entropy after finitely many dimensions.

For every epsilon>0 there are at most h(A)/epsilon positive primary factors whose individual w_p is at least epsilon.
Replacing every positive component by one simple Q[t]/(p) retains a finite-positive-entropy flow with failed capture whenever such a failure exists.
This replacement need not preserve the original entropy value; it preserves the existence of the obstruction and removes nilpotent extensions.
It gives no lower bound for w_p as p varies.

## Boundary and next use

This analysis does not prove a Mahler gap: hypothetical small irreducible weights give exactly the missing infinite direct sum.
It makes the spectral requirement on any proposed finite-capture counterexample explicit.
The arbitrary-abelian-group reduction must still use the separate torsion and rationalization interfaces in DGB16; no blanket decomposition of arbitrary abelian flows into these rational primary blocks is asserted here.

For G0001 the useful next step is therefore an arithmetic bound on cyclic irreducible reciprocal-unit flows, or a genuinely new construction of distinct irreducible weights tending to zero.
Reworking extensions of finitely many known spectral types cannot supply either.
This is a control on route selection, not an additional strategy priority.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0003_v1.md#targeted-review), with its original inspected scope and relationship.
