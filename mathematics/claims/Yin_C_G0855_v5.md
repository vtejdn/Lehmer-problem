---
author: Yin
---
# The capacity cost for standard exterior finite-graph cuts

This fixed result extends the geometric application of [C855 v4](Yin_C_G0855_v4.md#decision-whole-independent-review-2026-11-04) to single-valued continuation only on the unbounded complementary domain.
That exact independently adopted theorem, the earlier radial-hull result and the separately adopted raw-p2 result retain their fixed scopes.
The coordinating agent developed the extension for Yin, and the selected assessment adopts its independent whole review at the exact stated scope.

## Statement

Let P be the minimal polynomial of an actual Salem number lambda=exp(m), with degree d>=4 and 0<m<=1.
Fix an odd prime q, a primitive q-th root of unity zeta and a nonempty mask I in F_q.
Let O be the full multiplier orbit of I, S its union of positions, and put

    P_k(x)=product_i(1-alpha_i^k x), k=2,4,
    G_J(x)=sqrt(product_(j in J) P_4(zeta^j x)/P_2(zeta^j x)),
    G_J(0)=1, f(x)=sum_(J in O)G_J(x), F(z)=f(1/z).

Every original conjugate alpha_i is included.
The allowed unions S are {0}, F_q^* and F_q; the single unrotated radical is the case I={0}.
Let K be a nonempty compact finite embedded graph made of finitely many compact piecewise smooth arcs and possibly isolated vertices.
Suppose the exterior germ F has single-valued holomorphic continuation throughout the unbounded component Omega of C minus K.
No continuation on the bounded complementary faces is assumed, and the branch points need not lie on K itself.
Then there is an absolute D0, independent of P,q,I,K, such that for all d>=D0,

    log cap(K)>=m^2/log d.                                  (EX1)

When S={0}, one also has, uniformly beyond an absolute degree threshold,

    log cap(K)>=3m^2/[log(4/m)+5].                           (EX2)

Along a hypothetical actual Salem sequence with m tending to zero, the ratio of this capacity logarithm to log d/d tends to infinity, uniformly over the stated cuts and rotations.
No existence of that sequence is asserted.
These are geometric envelope bounds, not lower bounds on actual Hankel determinants or an unrestricted total-Mahler gap.
Arbitrary compact cuts and meromorphic-cover constructions are not classified.

## Exact inputs

The sole new geometric application uses the complete independently adopted [C855 v4 DC1--DC16](Yin_C_G0855_v4.md#decision-whole-independent-review-2026-11-04), including its genuine branch-point statement on every trace branch and its uniform root-component graph theorem.
Its accepted Pri11, numerical Smy08, classical capacity and original degree/source limits remain unchanged; those external theorems are not newly audited here.
The private radical-character argument over C(x) is also available directly in [C860 v7](Yin_C_G0860_v7.md#componentwise-pole-rank), with its C858 input.
The capacity/transfinite-diameter identity is reused at [C855 v2's exact interface](Yin_C_G0855_v2.md#sources-and-proof-interfaces); the filled-set equality needed below is proved directly.
No new source theorem, computation or mutable Draft is a proof premise.

## Argument

Let K be a compact finite embedded graph of finitely many compact piecewise smooth arcs and isolated vertices.
Write Omega for the unbounded component of C minus K and H=C minus Omega for the filled compact set.
For the same actual Salem original trace and rotation set as C855 v4, assume its exterior germ has a single-valued holomorphic continuation throughout Omega.
Then all genuine branch points belong to H.
Indeed a branch point in Omega would contradict local single-valued holomorphy; C855 v4 and C860 v7 prove that every original root in the specified union is a genuine branch point on every trace branch.

First cap(H)=cap(K).
For each fixed tuple of k-1 points in H, the Vandermonde product as a function of its remaining coordinate is the modulus of a polynomial.
On every bounded complementary face its maximum is attained on the boundary, which belongs to K, by the maximum-modulus principle.
Replacing the coordinates successively therefore shows that the maximum k-point Vandermonde product over H equals that over K.
Their finite transfinite diameters are equal for every k>=2, and the accepted capacity/transfinite-diameter identity gives the claim.
This argument does not invoke an additional equilibrium-measure theorem.

The filled set H has finitely many connected components; filling merges the graph components nested in bounded faces.
Each such component is full, meaning its complement is connected, and distinct components have positive distance.
A sufficiently small outer regular-neighborhood boundary of one component lies in Omega, surrounds that component and no other component of H, and can be chosen as a simple closed curve.
These assertions hold for a finite embedded graph and its filled faces: a finite thickening gives a regular neighborhood, filling its bounded holes retains its outer boundary, and the positive distances separate the finitely many components.
A component of H cannot contain exactly one genuine branch point.
Such a boundary would have the nontrivial local sign monodromy of that one point, contradicting the assumed single-valued continuation on Omega.
A component may contain no branch point, and no condition is imposed on it.

Now adjoin the finitely many branch points to K and join graph components lying in the same component of H until they are connected.
At each step choose a closest pair among the finitely many still distinct compact components within that filled component and adjoin their joining straight segment.
The open segment cannot meet an existing component, since that would shorten the selected inter-component distance.
It cannot leave H: leaving would first cross its boundary in K and again shorten the selected distance.
Thus each step stays inside H, joins two components and adds only an arc whose interior avoids the existing graph.
After finitely many steps the resulting finite embedded graph J contains every branch point, stays in H, and has the same root-containing connected components as H.
Each root-containing component therefore contains at least two branch points.
Capacity monotonicity and the previous equality give cap(J)<=cap(H)=cap(K).

Discard root-free isolated components of J if necessary, and apply the independently adopted C855 v4 theorem to the remaining graph.
It gives log cap(K)>=m^2/log d for all sufficiently large actual d, uniformly in K and the stated rotation collections.
For a single rotation it gives the stronger 3m^2/[log(4/m)+5] bound.
The existing DC16 comparison and all original-input/source limits carry over by this explicit graph construction.
The proof concerns finite-graph exterior cuts; it does not classify arbitrary compact sets, meromorphic charts on covers or determinant valuations.
No universal total-Mahler gap follows.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T23:57 |
| status | proved |
| reason | Adopt complete EX1--EX2 and the full exterior finite-graph argument after independent R1086 v4. Single-valued continuation is needed only on the unbounded complementary domain; filling, monodromy and a capacity-preserving graph construction supply the exact adopted v4 hypotheses. Uniform constants and all source/degree limits are retained. This is a geometric envelope result, not a determinant lower bound or an unrestricted Mahler-gap conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete exterior statement](#statement) | EX1--EX2 and uniform hypothetical-sequence consequence for all stated finite embedded graphs, allowing isolated vertices and branch points in bounded faces. |
| argument | [Complete argument](#argument) | Capacity under filling, root placement, outer monodromy loops, finite closest-component construction and quantitative transfer without additional cost. |
| dependency | [Adopted component theorem](Yin_C_G0855_v4.md#decision-whole-independent-review-2026-11-04) | Complete DC1--DC16 and actual source limits, applied to the explicitly constructed graph; no automatic extension of the older entire-complement scope. |
| dependency | [Capacity convention](Yin_C_G0855_v2.md#sources-and-proof-interfaces) | Only accepted capacity/transfinite-diameter identity, used in the direct filling proof. |
| dependency | [Genuine original branches](Yin_C_G0860_v7.md#componentwise-pole-rank) | Private roots and distinct radical characters over C(x), at retained C858 input scope. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1086_v4.md#exterior-salem-cut-whole) | Entire new exterior-domain statement and proof, actual finite-graph topology, no continuation on bounded faces, uniform costs and retained exclusions. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
