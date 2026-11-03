---
author: Yin
---

# G0001: neutral Jordan blocks obstruct whole-flow complexity compression

Date: 2026-10-06.
The current complete theorem and proof are at [the responsible Claim](../claims/Yin_C_G0229_v1.md#argument), with [actual whole self-review](../audits/reviews/Yin_R_G0514_v1.md#current-excess-jordan-finding).
The original mathematical body remains the fixed historical input and substantive comparison.
Coordinating AI for Yin, self-review only.
This tests the missing compression condition in [L G0025](Yin_L_G0025_v1.md#complexity-escape), within the [Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
It rules out an overstrong whole-flow target, not the positive-primary route or Lehmer.

<a id="jordan-complexity-obstruction"></a>
## A multiplicity bound

Write K(k)=k!3^k2^{k(2k-1)} for k>=1.
Suppose an integral unimodular matrix A has a Jordan block of size n>=2 at a nonzero eigenvalue z.
Then its Frobenius excess k=||A||_F^2-dim(A) satisfies

    n <= K(k)-1.

To prove this, use the signed permutation decomposition of L G0025.
If k=0, A is a signed permutation and is diagonalizable over C, contradicting n>=2.
For k>=1, remove the inactive signed cycles to obtain the active block A_0.
Inactive cycles are diagonalizable: their polynomials t^l-sigma have simple roots in characteristic zero.
Hence the size-n Jordan block must occur in A_0.
The polynomial

    F=D^{s-1} det(tI-A_0)

constructed there is nonzero, has at most K(k) nonzero terms, and has a root of multiplicity at least n at z.

For completeness, a nonzero polynomial with q distinct nonzero terms has multiplicity at most q-1 at any z!=0.
Write f(t)=sum_{j=1}^q c_j t^{a_j}, with distinct nonnegative integers a_j.
If its multiplicity were at least q, then applying (t d/dt)^r for 0<=r<q and evaluating at z gives

    sum_j a_j^r c_j z^{a_j}=0.

These vanish because each such differential operator is a linear combination of derivatives of order at most r multiplied by powers of t.
The Vandermonde matrix (a_j^r) is invertible, forcing every c_j z^{a_j}=0, a contradiction.
This proves the bound, including complex z.

<a id="neutral-padding-failure"></a>
## Counterfamily to entropy-only whole-flow compression

Let J_n be the integral unipotent Jordan block of size n.
Its characteristic polynomial is (t-1)^n, so h_alg(J_n)=0.
Let k_min be the minimum excess over all integral conjugates after adjoining arbitrary signed permutation blocks, exactly as in L G0025.
Such operations retain its size-n Jordan block.
Thus, for every fixed k_0>=1, n>K(k_0)-1 implies k_min(J_n)>k_0.
Consequently k_min(J_n) tends to infinity despite identically zero entropy.

For any fixed integral unimodular B, the same reasoning applies to B direct-sum J_n, whose entropy is exactly h_alg(B).
In particular B=[[1,1],[1,0]] gives strictly positive constant entropy log((1+sqrt(5))/2) with unbounded optimized excess.
More generally, if a positive-entropy matrix lies below any proposed threshold, adjoining these neutral blocks preserves that same entropy while defeating any uniform excess bound for all flows in that threshold class.
This conditional observation assumes no arbitrarily small positive entropy exists.

Thus no finite-valued bound on this whole-flow complexity depending only on entropy can hold, even after the stated stabilization and integral basis optimization.
This does not contradict L G0025's sufficient condition or its vanishing-entropy escape consequence.
It shows that neutral algebraic multiplicity is an independent source of complexity.

<a id="positive-primary-restriction"></a>
## Revised target

An entropy-preserving deletion of a neutral primary component is stronger than adjoining signed permutation blocks and conjugating.
The bounded-excess approach must first allow such deletion, or restrict directly to the companion matrices of irreducible positive-Mahler unit polynomials.
For the counterfamily above, deleting the (t-1)-primary component removes the obstruction entirely.
General rational primary decomposition does not by itself produce an integral direct-sum basis; an argument may instead choose a new integral companion representative of the relevant polynomial.
No bounded excess for these positive irreducible representatives is established here.

The next meaningful question is therefore compression of the positive irreducible unit core, rather than of arbitrary finite-rank flows.
Its degree remains unbounded; the full Task and algebraic-entropy priority are unchanged.

## Evidence and review

The proof uses L G0025's explicit polynomial construction and the existing characteristic-polynomial entropy formula.
The multiplicity lemma is proved here directly; no new literature theorem or computer experiment is used.
The original2026-10-06 formal author check is retained at [its exact finding](../audits/reviews/Yin_R_G0514_v1.md#original-jordan-author-check).
