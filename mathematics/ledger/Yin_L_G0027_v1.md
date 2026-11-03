---
author: Yin
---

# G0001: matrix compression and bounded-length neutral completion

Date: 2026-10-06.
The complete current mathematical home is [the responsible Claim](../claims/Yin_C_G0233_v1.md#argument), with [actual whole self-review](../audits/reviews/Yin_R_G0516_v1.md#current-compression-finding).
The original mathematical body remains its historical fixed input and substantive exploration.
Coordinating AI for Yin; self-review only.
This checks whether the matrix route supplies a genuinely different missing condition after the neutral obstruction in [L G0026](Yin_L_G0026_v1.md#positive-primary-restriction).
The outcome is a quantitative equivalence of boundedness conditions, not a proof of either for the full [Task](../tasks/Yin_T_G0001_v1.md#contract).
No novelty claim is made.

<a id="completion-invariants"></a>
## Two presentation invariants

Let p be monic irreducible in Z[t], p(0)=+1 or -1, and m(p)>0.
Products of cyclotomic polynomials below are monic, may have repetitions, and include 1.
Define

    L(p)=min_c ||p c||_1,
    E(p)=min_{A,c: det(tI-A)=p c} (||A||_F^2-dim A),

where A is any integral unimodular matrix of any size.
These minima exist in nonnegative integers: c=1 and the companion matrix of p give admissible examples.
E(p)>=1, since zero excess would force a signed permutation matrix by L G0025.
Every admissible matrix has entropy exactly m(p).

E permits replacement of the entire integral presentation and arbitrary cyclotomic characteristic factors.
It is not the conjugacy-and-stabilization invariant of a given flow in L G0026.
In particular it retains no prescribed neutral Jordan structure or prescribed integral lattice class.

<a id="boundedness-equivalence"></a>
## Quantitative equivalence

For k>=1 put

    H(k)=k! [(k+2) 2^{2k-1}]^k.

Then

    E(p) <= L(p)^2-1,       L(p) <= H(E(p)).

For the first inequality, choose q=p c attaining L(p) and take its standard companion matrix.
If q=t^d+sum_{i<d} a_i t^i, the excess is sum_{i<d} a_i^2-1, which is at most ||q||_1^2-1.
Its determinant is a unit since q(0)=+1 or -1.

For the second, take A attaining E(p)=k, and use the full construction of [L G0025](Yin_L_G0025_v1.md#bounded-excess-gap).
It writes A=P+E with s<=k nonzero perturbation entries whose absolute values sum to at most k.
There are r<=2s active signed cycles.
Let A_0 be the active block, D its signed-permutation characteristic polynomial, and

    B=D I_s-D V^T(tI-P_0)^{-1}U,
    F=det B=D^{s-1}det(tI-A_0).

The inactive cycles remove only cyclotomic factors from det(tI-A).
Thus p divides det(tI-A_0), and F=p c' with c' again a monic cyclotomic product.
This uses the fact that p is irreducible and noncyclotomic; inactive cycles cannot contain it.

Each entry of D V^T(tI-P_0)^{-1}U is one perturbation coefficient times a signed monomial and r-1 binomials.
Its coefficient l1 norm is at most k 2^{r-1}.
Also ||D||_1<=2^r.
Therefore each entry of B has coefficient l1 norm at most (k+2)2^{r-1}.
The coefficient norm is submultiplicative and satisfies the triangle inequality, so the determinant expansion gives

    ||F||_1 <= s! [(k+2)2^{r-1}]^s
             <= k! [(k+2)2^{2k-1}]^k = H(k).

The construction remains valid with coincident cycle lengths or cancellation; these can only improve the norm bounds.
Since F is an admissible cyclotomic completion, the second inequality follows.

Consequently, on any family of positive irreducible unit polynomials, uniform boundedness of E is equivalent to uniform boundedness of L.
This concerns boundedness across a family, not equality of the minima or preservation of an original flow under conjugacy.

<a id="strategy-consequence"></a>
## Consequence for the entropy route

Bounded L implies bounded support of p c and hence the accepted [DS17 gap](../audits/literature/DS17/readme.md#bounded-support-gap), as already used in [L G0019](Yin_L_G0019_v1.md#controlled-entropy-completion).
The matrix construction supplies an explicit conversion in both directions, but does not remove the need to control cyclotomic completion complexity.
It should not be counted as an independent uniform-gap mechanism alongside bounded-length completion.

This also explains why choosing a new lattice alone is insufficient as a proposed solution: if it genuinely produced uniformly bounded excess after neutral completion, it would already produce uniformly bounded coefficient-length cyclotomic multiples.
No such existence theorem has been proved here, even restricted to small positive entropy.
Conversely, no counterfamily to that positive-core condition has been constructed.

The remaining arithmetic target is to construct controlled neutral completions for the small-measure irreducible unit core, or extract an obstruction from a hypothetical sequence on which both L and E diverge.
A bounded-support completion without an explicit coefficient-length bound is a separate weaker condition; this record does not assert their equivalence without an additional coefficient estimate.
The completion-length comparisons above assume an irreducible positive-measure unit polynomial.
An extension to reducible monic integral unit polynomials, including repeated noncyclotomic factors, is a separate question here; no precise such extension or complete argument is established in this record.
The algebraic-entropy priority and unresolved Task remain unchanged.

## Review scope

The original2026-10-06 formal author/contributor check is retained at [its exact finding](../audits/reviews/Yin_R_G0516_v1.md#original-presentation-invariant-check).
