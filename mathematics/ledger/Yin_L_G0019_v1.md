---
author: Yin
---

# G0001: sparse completion with controlled extra entropy

Date: 2026-10-06.
Follow-up to [L G0018](Yin_L_G0018_v1.md#short-annihilator-degree-cost), using the newly inspected [DS17 bounded-support input](../audits/literature/DS17/readme.md#bounded-support-gap).
This is a direct application of an established result, not a new sparse-polynomial theorem or a solution of Lehmer.
The controlling parameter is the number of nonzero coefficients, not degree or coefficient height.

<a id="controlled-entropy-completion"></a>
## A sufficient presentation criterion

Fix K>=2 and A>=0.
Let p be monic irreducible integral, p(0) nonzero, and m(p)>0.
Suppose there is a nonzero c in Z[t] such that q=pc has at most K nonzero coefficients and

    m(c) <= A m(p).

Let eta_K>0 be the accepted external gap in the source audit.
Integer polynomials have nonnegative logarithmic Mahler measure.
Thus

    0 < m(p) <= m(q) = m(p)+m(c) <= (1+A)m(p),
    eta_K <= m(q),
    m(p) >= eta_K/(1+A).                              (1)

No bound on deg(q)/deg(p) is needed.
In particular, cyclotomic completion permits A=0, including repeated cyclotomic factors.
This removes the degree loss of the elementary certificate in L G0018, within the bounded-support hypothesis.
It does not establish that hypothesis for arbitrary small-entropy p.

More generally, for fixed K, if a proposed positive sequence m(p_n)->0 has K-term multiples q_n=p_n c_n, then

    m(c_n) >= eta_K-m(p_n).

Hence for all sufficiently large n, m(c_n)>=eta_K/2 and m(c_n)/m(p_n)->infinity.
Fixed-support completions cannot have even vanishing absolute extra entropy along such a sequence.
This is stronger than merely excluding a fixed relative overhead A.

<a id="cyclotomic-support-escape"></a>
## Necessary complexity escape and finite capture

Define s_cyc(p) as the minimum number of nonzero coefficients of p*c, over monic products c of cyclotomic polynomials, including c=1.
The minimum exists: the possible counts form a nonempty set of positive integers.
This is a support-count invariant; it is not the coefficient-length shortness used by El-Serafy--McKee.

If m(p_n)>0 tends to zero, then s_cyc(p_n)->infinity.
Indeed, for each fixed K, an infinite subsequence with s_cyc<=K would satisfy m(p_n)>=eta_K by (1), a contradiction.
Accordingly, no counterexample search restricted to uniformly bounded cyclotomic support can settle the negative direction, even with unbounded degree and neutral dimension.

For rational flows in [L G0002](Yin_L_G0002_v1.md#capture-equivalence), suppose each positive irreducible primary type admits a completion with the same K,A.
Formula (1) bounds every positive weight below.
The primary entropy sum then shows that finite total entropy permits only finitely many positive types, hence finite capture at that record's exact scope.
Zero-entropy primary parts may still be infinite.
No unrestricted representation theorem has been proved.

## Consequence for the next attempt

The [binary-collision construction](Yin_L_G0018_v1.md#binary-relations-boundary) supplies neither bounded support nor bounded multiplier entropy.
Improving only its coefficient height is insufficient.
A meaningful new structural target is a construction controlling both support and extra entropy, or a proof that any small-entropy sequence forces an incompatible pattern in this support escape.
The known sparse gap alone does not prohibit unbounded support.

Reuse/search, 2026-10-06: began with the fixed L G0018 question and the local Smy08 sparsity report; followed the previous turn's primary-source leads to Dobrowolski--Smyth's versioned paper.
Its accepted scope and source dependencies are recorded in the linked audit, and its retained artifact in the registry.
No original 1991 or 2006 sparse-bound proof was inspected, and no explicit numerical eta_K is adopted.
Further source expansion was unnecessary for the direct implication (1).

The original complete author check is retained at [R510](../audits/reviews/Yin_R_G0510_v1.md#original-sparse-overhead-author-check).
The current complete controlled-overhead and support-escape theorem is [C221](../claims/Yin_C_G0221_v1.md#argument), adopted after the [whole current self-review](../audits/reviews/Yin_R_G0510_v1.md#current-sparse-completion-finding).
