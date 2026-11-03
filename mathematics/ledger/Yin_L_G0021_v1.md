---
author: Yin
---

# G0001: entropy overhead in symmetric-matrix realizations

Date: 2026-10-06.
The current complete mathematical home is [the matrix realization and metric theorem](../claims/Yin_C_G0227_v1.md#argument), with [actual complete self-review](../audits/reviews/Yin_R_G0512_v1.md#current-matrix-realization-finding).
The original mathematical body remains here as its dated review input and substantive exploration.
A bounded test of a possible algebraic-entropy representation, following the controlled-completion criterion of [L G0019](Yin_L_G0019_v1.md).
The established matrix gap and the explicit excluded measure are accepted at the [MS12 source scope](../audits/literature/MS12/readme.md).
Their classification proofs remain external.
The calculations here are direct and self-reviewed, with no novelty claim.

<a id="symmetric-entropy-lift"></a>
## The actual entropy-bearing automorphism

For an N-by-N symmetric integer matrix A set

    B_A = [[A,-I],[I,0]],   J=[[0,I],[-I,0]].

Block multiplication gives B_A^T J B_A=J.
Its inverse is [[0,I],[-I,A]], so it is an integer automorphism, and its determinant is 1.
The Schur-complement identity, first for t nonzero and then as a polynomial identity, gives

    det(tI-B_A)=t^N det((t+t^-1)I-A)=R_A(t).

The accepted rational entropy formula therefore gives h_alg(B_A)=m(R_A).
This is the entropy of the full 2N-dimensional automorphism, with no normalization by N.

If chi_A=Q*r for monic integer Q of degree d and monic integer r, define

    P=t^d Q(t+t^-1),   C=t^(N-d)r(t+t^-1).

Both are monic integer polynomials with constant coefficient 1, and R_A=P*C.
Hence

    h_alg(B_A)=m(P)+m(C).

Even when a desired algebraic number occurs among the eigenvalues of A, this only identifies a factor; it does not eliminate m(C).
If m(C)<=a*m(P) with fixed a>=0 and m(P)>0, the accepted matrix gap would give m(P)>=log(lambda_0)/(1+a).
Establishing such controlled overhead is an additional obligation.
Real symmetry also requires all roots of Q to be real, so this representation cannot automatically cover the full reciprocal core with nonreal trace roots.

<a id="no-neutral-symmetric-completion"></a>
## An explicit failure even allowing neutral padding

Take the source's exact pair

    Q(x)=x^7-8x^5+19x^3-12x+1,
    P(t)=t^7 Q(t+t^-1)=t^14-t^12+t^7-t^2+1.

Write tau=M(P).
The accepted source statement places 1<tau<1.3 and excludes tau from its sixteen matrix measures below 1.3.
The displayed approximation 1.20261 is only an identifier, not a new numerical certificate.
In particular, tau is a measure, not a claimed positive root of the displayed P; its sign pattern must be retained.

There is no symmetric integer A such that chi_A=Q*r and all roots of r lie in [-2,2].
Indeed that spectral condition gives m(C)=0, so M(R_A)=tau.
Permute A into indecomposable symmetric integer blocks.
Their reciprocal measures multiply.
Each noncyclotomic block has measure at least lambda_0; since lambda_0^2>1.3, there can be only one such block when the product is tau<1.3.
Its measure would be tau, contrary to Theorem4 and the explicit exclusion.
Here lambda_0 is the exact Lehmer root from Corollary2; the coarse inequality lambda_0^2>1.3 is far from the numerical boundary.
Thus adding arbitrarily many neutral eigenvalues cannot repair this example.

More generally, for any A with Q dividing chi_A, the extra entropy is bounded away from zero, provided such a realization is chosen.
Let F be the finite set of sixteen exact measures specified by the source's graph catalogue, and put

    gamma=min({13/10} union {v in F : v>tau}).

Then gamma>tau, and the same block argument shows M(R_A)>=gamma: below 1.3 there is at most one noncyclotomic block, its measure is in F, multiplicativity gives M(R_A)>=tau, and equality is excluded.
Consequently m(C)>=log(gamma/tau)>0.
No rounded table number is substituted for gamma, and no effective numerical overhead is claimed.

## Search, scope and consequence

Local reuse checked the Smy08 Section5.4 matrix report, the inverse-trace distinction in L G0009, and L G0019's multiplicative overhead argument.
On 2026-10-06 the bounded search "Estes totally real algebraic integer eigenvalue symmetric integer matrix characteristic polynomial power entropy Lehmer McKee Smyth" led to primary matrix-realization abstracts and the MS12 paper.
Only the latter's registered statements are used.
A general eigenvalue-existence theorem is neither required nor upgraded to an entropy-preserving realization here.

The primary route should therefore not assume zero-overhead symmetric realization, even for this explicit small-measure five-term polynomial.
A positive-overhead bound could still be useful, and the whole-core nonreal-trace obstruction remains separate.
This does not refute Lehmer, whose known matrix subcase remains valid.

The original2026-10-06 formal author check is retained at [its exact finding](../audits/reviews/Yin_R_G0512_v1.md#original-symmetric-overhead-check).
