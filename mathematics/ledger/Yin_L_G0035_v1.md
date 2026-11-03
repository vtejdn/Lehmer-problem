---
author: Yin
---

# G0001: canonical binary convex covers and the remaining interior question

Date: 2026-10-07.
Working proof by the assigned AI ms25_source for Yin, continuing [L G0032's multi-place cover question](Yin_L_G0032_v1.md#strict-width-block-obstruction) within [G0001](../tasks/Yin_T_G0001_v1.md).
This classifies covers by the canonical convex hull.
It does not classify every smaller convex covering body and does not prove a Mahler gap.

The complete current canonical and arbitrary-body convex cover statement and argument are owned by [its responsible Claim](../claims/Yin_C_G0239_v1.md#argument); original source/comparison limits and the fixed review input remain here.

## Scope and literature check

Local inputs are L G0032's exact one-step radical parallelotope and the distinction between support volume and weighted entropy, and [L G0030](Yin_L_G0030_v1.md#renyi-rates) for the entropy conventions.
The proofs below are written out directly; no new external classification theorem is assumed.

A bounded primary-source search used "convex self affine attractor two maps two digits convex hull expanding matrix" and "convex self affine sets two digit parallelotope classification".
Protasov--Zaitseva, *Self-affine 2-attractors and tiles*, arXiv:2007.11279 / Sbornik Mathematics 213 (2022), 794--830, has a relevant infinite-zonotope description in Proposition 2 and a classification in Section 7.
The inspected [publisher HTML](https://www.mathnet.ru/eng/sm9682) imposes an expanding integer matrix and determinant of absolute value 2 for its two-digit class; those classification hypotheses do not apply directly to an expanding place restriction with determinant M<2.
Its Proposition 2 supplied a matching attribution lead, while the convex-hull formula used here has its own elementary proof.

Hare--Sidorov, *Two-dimensional self-affine sets with interior points, and the set of uniqueness*, Nonlinearity 29 (2016), 1--26, [arXiv:1502.07330v3](https://arxiv.org/abs/1502.07330v3), Lemma 4.12 gives the two-dimensional rational-rotation sufficiency of grouping powers into one-dimensional intervals.
The entire statement and proof on PDF pp.21--22 were read and rendered; neither the paper's other proofs nor a general classification is adopted.
Its interior theorems remain leads, and their dimension-dependent constants are not uniform statements for G0001.
No novelty claim follows from this bounded comparison.

Both comparison sources, HS16b and PZ22, are retained in the PDF library at their stated reading boundaries.
Their limited source scopes do not replace the direct proofs below.

<a id="canonical-convex-classification"></a>
## An exact canonical-body criterion

Let U be a real vector space of dimension r>=1.
Let A:U->U be invertible with every complex eigenvalue of modulus greater than one.
Let v be cyclic, meaning that the real span of v,Av,A^2v,... is U.
Define the binary attractor and its continuous-digit counterpart by

    S={sum_(j>=1) epsilon_j A^(-j)v : epsilon_j in {0,1}},
    Z={sum_(j>=1) t_j A^(-j)v : 0<=t_j<=1}.

The series converge uniformly over their digit choices: the norms of A^(-j) decay geometrically up to a polynomial factor.
Thus S and Z are compact; Z is convex.
Cyclicity makes Z full-dimensional.
Moreover Z=conv(S): every finite partial sum of segments is the convex hull of the corresponding binary sums, these binary sums belong to S after adding zero tails, and the tails tend uniformly to zero.
In finite dimension the convex hull of compact S is compact, so limits remain in it.
We have the exact identities

    AS=S union (S+v),       AZ=Z+[0,v].                 (1)

The following are equivalent:

1. AZ subset Z union (Z+v).
2. S is convex, and hence S=Z.
3. Some positive power satisfies A^q v=c v for real c; if q is the least such positive integer, then |c|<=2.

In (3), automatically |c|>1, q>=r, and A^q=cI on U.
The resulting Z is a finite zonotope; it need not be a parallelotope when q>r.
For an explicit continuous example, take U=R^2 and A equal to 2^(1/3) times rotation through pi/3.
Every nonzero v is cyclic, the least projective return is q=3 with c=-2, and det A=2^(2/3)<2.
The three distinct unoriented generator directions make Z a hexagon rather than a parallelotope.
This example is not claimed to be the full expanding restriction of an algebraic unit.

### Why the first two conditions agree

By (1), the union Z union (Z+v) is always contained in AZ.
Thus (1) in the list is equality and makes Z a compact fixed set of the binary affine set map.
Its fixed set is S.
This uniqueness also follows directly: iterate a fixed-set identity n times; the remaining A^(-n) image of the bounded seed tends to {0}, leaving the binary infinite series.
Conversely, if S=Z, its exact identity in (1) gives the cover.

### Why a projective return is necessary

First take r>=2.
Suppose no A^q v is parallel to v.
Then no vector g_j=A^(-j)v, j>=1, is parallel to v.
In the (r-1)-dimensional space of functionals ell satisfying ell(v)=0, each condition ell(g_j)=0 is a proper linear hyperplane.
A countable union of proper hyperplanes cannot cover that space, so choose ell with ell(v)=0 and ell(g_j)!=0 for every j.

The exposed face of Z maximizing ell is a single point z: the unique maximizing choice is t_j=1 if ell(g_j)>0 and t_j=0 otherwise.
The sum of these endpoints converges absolutely.
Any other maximizing representation would have nonnegative losses summing to zero, so every digit choice with nonzero ell(g_j) would have to agree.

The exposed face of Z+[0,v] in this same direction is the entire segment z+[0,v], whereas that of Z union (Z+v) consists of its two endpoints.
They cannot be equal because v!=0.
Therefore a canonical cover is impossible without a projective return.

### The scalar threshold is exactly 2

Let q be the least positive integer with A^qv=cv.
Cyclicity gives A^q=cI on U by applying the equality to every A^jv.
Expansion gives |c|>1, and cyclicity also gives r<=q.
The indices j>=1 for which A^(-j)v is parallel to v are exactly the positive multiples of q: division by q would otherwise give a smaller projective return.

For r>=2 choose ell annihilating v but none of the other, finitely many projective directions.
The exposed face of Z is a translate of the segment

    I_c v,      I_c=sum_(m>=1) c^(-m)[0,1].

Here I_c is an interval, also when c is negative, and its length is

    length(I_c)=sum_(m>=1)|c|^(-m)=1/(|c|-1).

In direction ell, the face of Z+[0,v] is that interval plus [0,1]v.
The face of Z union (Z+v) is the union of the interval and its translate by v.
Equality requires the two intervals to overlap or touch, hence length(I_c)>=1, or |c|<=2.

Conversely, when this inequality holds, split the defining segments of Z into those indexed by multiples of q and all the others, writing Z=Z_0+I_cv.
Since I_c+[0,1]=I_c union (I_c+1),

    Z+[0,v]=Z_0+(I_c+[0,1])v=Z union (Z+v).

This proves sufficiency directly.
Grouping every residue class modulo q turns the infinite sum into finitely many segments, explaining the zonotope statement.
For r=1 there is automatically a return with q=1 and c=A in a scalar coordinate; the same interval-length argument proves the criterion without an exposed functional.

<a id="power-stable-canonical-obstruction"></a>
## Consequence for the all-power-preserving arithmetic core

Let lambda be an algebraic unit with irreducible minimal polynomial p, and let U be its expanding real Minkowski space.
Let A be multiplication by lambda and v the expanding embedding of 1.
Its dimension r counts expanding conjugates with complex conjugates counted separately.
Distinct conjugates make v cyclic by the Vandermonde argument already used in L G0032.

Assume every positive power preserves degree:

    [Q(lambda^q):Q]=[Q(lambda):Q] for every q>=1.

Then, if r>=2, the canonical body Z does not give a binary cover, and S is nonconvex.
Indeed, A^qv=cv would make every expanding conjugate beta satisfy beta^q=c.
At least two distinct conjugates would then have the same q-th power, contradicting degree preservation.
The degree argument is exact: equality of fields Q(lambda^q)=Q(lambda) makes embeddings determined by their value on lambda^q.

This obstruction applies to the stated multiple-expanding, all-power-preserving scope even when p is reciprocal and M(p)<theta_0.
It does not assume that an infinite small-measure family exists.
In contrast, the one-expanding real case has r=1 and the canonical interval cover remains possible when M<=2, as in L G0007.

This is an obstruction to using the whole canonical convex hull, not to binary support entropy attainment, positive volume of S, or a smaller convex body contained in S.

<a id="arbitrary-body-determinant-boundary"></a>
## What follows for an arbitrary convex covering body

Suppose a compact full-dimensional convex K satisfies

    AK subset K union (K+v).                            (2)

Volume gives |det A|<=2.
The equal-determinant boundary admits a complete conclusion: if |det A|=2, the union on the right and AK have the same volume, and the two translates overlap only in a null set.
Inclusion (2) is then equality as sets.
To justify the reverse inclusion, a point of either convex body outside the closed set AK would have a small neighborhood outside AK with positive volume in that body, a contradiction.

Thus K is the binary attractor S and is convex.
The canonical criterion gives A^q=cI with q>=r and |c|<=2, while

    2=|det A|=|c|^(r/q).

It follows that q=r and c=2 or c=-2.
Cyclicity then gives characteristic polynomial t^r-c, and grouping the defining segments in its r independent directions makes K a parallelotope.
Conversely these cyclic binomial cases have the stated canonical parallelotope cover.
No integrality assumption on A is needed for this boundary argument.

For |det A|<2, the equality argument no longer applies.
In particular, (2) does not imply that K equals the canonical hull, nor has a parallelotope classification been proved here.
What always holds is K subset S: write Ax_0=x_1+epsilon_1v with x_1 in K, and iterate this choice to obtain

    x_0=sum_(j=1)^n epsilon_j A^(-j)v + A^(-n)x_n.

The last term tends to zero because K is bounded and A expands.
Hence each x_0 has a binary address and belongs to S.
A full-dimensional convex cover therefore requires nonempty interior of S, but a nonconvex S can still contain a full-dimensional convex subset.
Nonconvexity alone does not exclude (2).

<a id="positive-volume-support-interface"></a>
## Positive volume suffices for support growth, not weighted entropy

Convexity is not needed for the volume lower bound.
If S has positive r-dimensional Lebesgue volume, the exact attractor identity implies, for all n>=1,

    A^nS=D_n+S,
    D_n={sum_(j=0)^(n-1)epsilon_j A^jv : epsilon_j in {0,1}}.

Volume subadditivity gives

    |det A|^n volume(S)<=|D_n| volume(S),
    |D_n|>=|det A|^n.                                  (3)

For the expanding restriction of the integral algebraic-unit flow, |det A|=M(p).
Projection to U cannot increase the full digit support size.
Combining (3) with the already accepted algebraic support upper bound then gives support entropy m(p).
For 1<|det A|<2 this support estimate alone does not establish equality of Shannon or positive-order Renyi entropy with log|det A|: the digit multiplicities remain uncontrolled.
There is a sharp boundary exception at |det A|=2.
Then (3) and |D_n|<=2^n force exactly 2^n distinct sums, each with probability 2^(-n), so every Renyi entropy rate equals log2.
This exception needs positive volume, not convexity.

The changed next action is to distinguish three questions: the canonical convex body is now excluded on the stated multiple-expanding core; a smaller convex body satisfying (2) remains open at determinant less than 2; and positive volume of S would already suffice for support attainment without either convex-body condition.
A useful continuation must establish one of these remaining properties with its arithmetic hypotheses, rather than import a determinant-2 integer-tile classification into the M<2 flow.
None of them by itself supplies a positive lower bound for m(p).



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0008_v1.md#review-status), with its original inspected scope and relationship.
