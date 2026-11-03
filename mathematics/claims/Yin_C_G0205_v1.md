---
author: Yin
---

# Rational finite-entropy primary decomposition and finite capture

Provenance: project deduction from accepted entropy interfaces.
The original mathematics dates to 2026-10-06 in [L G0002](../ledger/Yin_L_G0002_v1.md).
This material owns its complete reusable argument; the source record retains its original exploration, source-search and historical review context.
[G0001 remains paused](../tasks/Yin_T_G0001_v1.md#decision-human-pause-after-closeout).

## Statement

Let V be a rational vector space of arbitrary dimension and A a rational linear endomorphism with finite algebraic entropy h(A), defined on the discrete additive group using all nonempty finite subsets and natural logarithms.
For each monic irreducible p in Q[t], let p_Z be its primitive integral associate with positive leading coefficient, let d_p=deg p, and put w_p=m(p_Z).
Define V_p={v:p(A)^j v=0 for some integer j>=1} and ell_p=dim_Q(V_p)/d_p, with infinity allowed.
Then V is the algebraic direct sum of the V_p and

    h(A)=sum_(p:w_p>0) ell_p w_p,

where the sum is the supremum of finite partial sums.
Each positive-weight ell_p is a finite nonnegative integer, each zero-weight primary component contributes zero regardless of dimension, and at most countably many positive-weight components are nonzero.

The following conditions are equivalent: a finite-dimensional invariant rational subspace captures h(A); a nonempty finite subset attains h(A); and only finitely many p with w_p>0 have V_p nonzero.
Consequently failure of capture requires infinitely many distinct positive irreducible Mahler weights with finite positive weighted sum.
Replacing each positive primary component by one simple Q[t]/(p) preserves existence of such a failure, without asserting preservation of its numerical entropy.
The theorem does not give a positive lower bound on w_p as p varies or a decomposition of arbitrary abelian flows.

## Current assessment

[Selected decision](#decision-current)

## Assessment history

### Decision current

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:02 |
| status | proved |
| reason | The full primary-splitting, directed-continuity and capture arguments are retained in C and checked at their exact source interfaces by the selected current agent self-review. No uniform Mahler bound or arbitrary-abelian decomposition is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Arbitrary-dimensional rational finite-entropy flows, exact positive-primary sum and all three finite-capture conditions. |
| argument | [Argument](#argument) | Complete Bezout decomposition, primitive normalization, continuity, countability and capture proofs retained below. |
| dependency | [DGB16 basic interfaces](../audits/literature/DGB16/Yin_U001.md#dgb16-u001) | Monotonicity, infinite cyclic-orbit entropy, finite products and directed invariant unions; their recorded source limits remain. |
| dependency | [GBV15 rational interfaces](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Rational Yuzvinski with the full leading-coefficient term and finite-set attainment on finite-dimensional rational spaces; no new original p-adic proof audit. |
| review | [Rational extraction and proof finding](../audits/reviews/Yin_R_G0497_v1.md#rational-primary-current-finding) | Exact registered statement and complete C argument, including unchanged source applicability and extraction interfaces. |

## Argument

The complete mathematical sections below are retained from L G0002's original argument, with heading depth adjusted.
The source-search attribution follow-up in L G0002 remains unresolved; no novelty claim is made.
The earlier [R G0003](../audits/reviews/Yin_R_G0003_v1.md#targeted-review) remains tied to its actual L input and original date.
It is not retrospectively bound to this new Claim.

<a id="rational-primary-formula"></a>
### Exact rational decomposition

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
### Capture criterion and consequence

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
