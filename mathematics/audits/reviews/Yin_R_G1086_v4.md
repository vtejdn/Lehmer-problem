---
author: Yin
---

# Independent whole review of standard exterior finite-graph cuts

Review act: 2026-11-04T23:54 UTC.
The human record author is Yin.
This is a separately organized independent agent review of the entire [C855 v5 statement](../../claims/Yin_C_G0855_v5.md#statement), EX1--EX2 and its uniform hypothetical-sequence consequence, and the [complete argument](../../claims/Yin_C_G0855_v5.md#argument).
The reviewer did not participate in developing this extension and received no development dialogue, author explanation, mathematical development summary or rolling Draft.
The fixed v5 candidate and necessary actual inputs were read directly.
The reviewer previously performed the [independent v4 whole review](Yin_R_G1086_v3.md#disconnected-salem-cut-whole); that was a review role, not a development contribution.
The present review reuses the exact [adopted v4 theorem](../../claims/Yin_C_G0855_v4.md#decision-whole-independent-review-2026-11-04) and checks the complete new exterior-domain application.
No substantive repair was supplied, and v5 had no selected assessment during this review.

## Exact extension and retained inputs

The earlier R1086 v1--v3 findings remain at their own physical inputs, relationships, times and source limits.
In particular v4's entire-complement cut application is not relabelled as a proof of v5.
The new hypotheses allow bounded faces without continuation and do not require the original branch points to lie on K.
The obligations are therefore to place them in the filled set, preserve capacity under filling, prove the required filled-component monodromy condition, construct a suitable finite graph inside the filling, and transfer the adopted quantitative bounds without new nonuniform constants.

<a id="exterior-salem-cut-whole"></a>
## Whole exterior-cut finding

**Finding:** no unresolved mathematical gap was found in the complete C855 v5 statement and argument at the stated finite embedded graph and accepted-input scope.
Single-valued holomorphic continuation of the actual exterior germ throughout the unbounded component is sufficient for EX1 and EX2, even when the bounded faces contain original branch points.
The threshold remains absolute and uniform in the actual Salem input, q, mask and graph.
The proof gives a capacity-envelope lower bound and the stated uniform divergence on a hypothetical near-one sequence.
It does not supply a determinant lower bound, an actual determinant-valuation upper bound, arbitrary-compact-cut classification or an unrestricted positive total Mahler gap.

### Actual trace and the location of every branch point

The root noncollision and private-square-class inputs are those already adopted in [C855 v4](../../claims/Yin_C_G0855_v4.md#relation-to-the-original-trace-and-what-remains-open) and retained directly in [C860 v7](../../claims/Yin_C_G0860_v7.md#componentwise-pole-rank).
For a full multiplier orbit of a nonempty mask, the used-position union is one of \(\{0\},\mathbb F_q^*,\mathbb F_q\).
Thus it is exactly a rotation collection allowed by v4.
Every original conjugate is retained, the squared and fourth-power lists are distinct, and the finite branch-point set in the exterior z-coordinate is

\[
 B=\{\zeta^j\alpha_i^2,\zeta^j\alpha_i^4:i=1,\ldots,d,\ j\in S\}.
\]

The equal numerator and denominator degrees cancel the powers of z introduced by inversion.
At z equal to zero their resulting numerator and denominator constants are nonzero, and the original normalization makes the exterior germ holomorphic at infinity.
There is no additional branch point at zero or infinity that could cancel the monodromy used below.
The odd zeros and poles at B are the original private branch points.
Their local sign change acts nontrivially on every trace branch because the changed nonempty subcollection consists of distinct, linearly independent radical characters over \(\mathbb C(x)\).
This uses the genuine-branch statement, not merely nonrationality of the sum.

If any point of B lay in \(\Omega\), a small disk around it inside \(\Omega\) would contradict the required single-valued holomorphic continuation.
Hence \(B\subset H=\mathbb C\setminus\Omega\).
This conclusion is about H, not about K: v5 properly allows the points to lie in bounded faces.
Only continuation of the given germ throughout \(\Omega\) is used.

### Filling preserves capacity

The complement of a compact graph has one unbounded component, and H is its compact filling.
Every bounded face has boundary in K.
For fixed values of the other \(k-1\) coordinates, the modulus of the Vandermonde product in the remaining coordinate is a constant times the modulus of a polynomial.
On the closure of a bounded face, continuity and the maximum-modulus principle place its maximum on the boundary.
If the constant is zero the replacement assertion remains immediate.
A coordinate lying already in K needs no change.

Replacing coordinates successively therefore takes any tuple in \(H^k\) to a tuple in \(K^k\) without decreasing the Vandermonde product.
The reverse maximum inequality follows from \(K\subset H\).
Thus the maximal products, and hence the finite transfinite diameters, agree for every \(k\ge2\).
The exact [accepted capacity/transfinite-diameter identity](../../claims/Yin_C_G0855_v2.md#sources-and-proof-interfaces) gives \(\operatorname{cap}H=\operatorname{cap}K\).
No regularity of the faces for a Dirichlet problem and no new equilibrium-measure theorem is required by this argument.
It remains valid for a graph with isolated vertices.

### Filled components and the outer monodromy loop

The finite-graph scope ensures finitely many graph components and faces.
Filling a bounded face absorbs graph components nested inside it, so H has finitely many compact connected components.
Its components are full: none has a bounded complementary hole left over after the filling.
For this finite graph construction, each filled component has one outer graph component, with any other original graph components nested in its bounded faces.
In particular the boundary exposed to \(\Omega\) belongs to that outer graph component.
Distinct filled components are disjoint compact sets and have positive mutual distance.

The outer boundary of a sufficiently small regular neighborhood of a filled component can be chosen as a simple closed curve in \(\Omega\) enclosing that component and no other filled component.
This is used only for the finite embedded graph with its filled faces.
A finite thickening of its outer graph component has finitely many boundary curves; filling the bounded holes selects its outer boundary.
The neighborhood may be chosen sufficiently small to avoid the other components and their paths to infinity, so that filling this neighborhood does not accidentally enclose a different component.
The assertion needs no radius uniform in the graph.
It also applies to an isolated point, using a small circle.

If one filled component contained exactly one point of B, its outer boundary curve would enclose exactly that one branch point.
The radical monodromy along the curve is therefore its local sign change, which fixes no branch of the trace by the preceding private-character check.
The curve lies wholly in \(\Omega\), where the assumed single-valued holomorphic continuation instead forces trivial monodromy on the continued germ.
This contradiction proves that every root-containing filled component has at least two distinct original branch points.
Root-free filled components cause no problem and need no such restriction.
The reasoning invokes no continuation inside a bounded face.

### The closest-component construction stays inside H

Adjoining all points of B to K produces a finite embedded graph with possibly isolated vertices, still contained in H.
Within a filled component, there are finitely many current graph components.
Two distinct such components are compact and have positive distance, so a globally closest pair among them exists.

For a joining segment of minimal inter-component length, its open segment cannot meet any current graph component.
Indeed a point of intersection belongs either to one endpoint component or to a third component; its distance to an endpoint in a different component would be strictly shorter.
This verifies the argument even when the segment meets an edge rather than a vertex.

The no-exit step also uses the nesting structure of the filled component.
Only its unique outer graph component meets the boundary exposed to \(\Omega\); each still separate component lies in its interior.
Merging components preserves this property: at most one current component contains that outer graph component.
Thus a selected pair of distinct current components always has an endpoint in the interior of H.
Starting from that endpoint, a segment leaving H would meet \(\partial H\subset K\) at an interior point of the segment.
That contradicts the just-verified avoidance of the existing graph.
This confirms the candidate's boundary-crossing argument, including pairs with the other endpoint on the outer graph component.

Each added segment therefore stays inside H, has open interior disjoint from the current graph, and merges exactly two components.
Subdividing an existing edge at a new endpoint preserves the finite embedded graph structure.
After finitely many steps all graph components within each root-containing filled component are connected.
The resulting graph J contains every point of B, remains in H, and induces on B the same component partition as H.
The phrase about the same root-containing components asserts this grouping, not equality of the point sets J and H.
Every root-containing component of J consequently contains at least two distinct roots.
Discarding root-free isolated components leaves a graph made of finitely many compact piecewise smooth arcs at the exact v4 scope.
No root-containing component can be isolated, because it contains at least two distinct roots.

### Quantitative transfer and uniformity

For the remaining graph, capacity monotonicity and the filling equality give

\[
 \operatorname{cap}J\le\operatorname{cap}H
                         =\operatorname{cap}K.
\]

The [adopted v4 statement](../../claims/Yin_C_G0855_v4.md#disconnected-cut-capacity) applies to J with the same original P, m, d and S.
It yields \(\log\operatorname{cap}J\ge m^2/\log d\) beyond its absolute degree threshold, and the stronger \(3m^2/[\log(4/m)+5]\) bound when \(S=\{0\}\).
These inequalities prove EX1 and EX2 for K.
In particular the constructed root-containing graph is nonpolar, so no hidden assumption of positive capacity is needed to take these logarithms.
The construction has no quantitative loss and introduces no degree, conductor, mask, arc-length or separation constant into the thresholds.
The thresholds and their unevaluated numerical status are exactly those already available in v4.

On a hypothetical actual Salem near-one sequence, degree tends to infinity by the fixed-degree coefficient finiteness argument already checked in v4.
The exact [DC16 consequence](../../claims/Yin_C_G0855_v4.md#relation-to-the-original-trace-and-what-remains-open) therefore gives the same lower ratio

\[
 \frac{\log\operatorname{cap}K}{\log d/d}
       \ge\frac{d m^2}{(\log d)^2}\longrightarrow\infty,
\]

uniformly over the present larger class of finite-graph exterior cuts.
No sequence is constructed or assumed to exist.
The direction of the retained contour comparison remains an upper bound for Hankel growth by a capacity, so a positive lower bound on this envelope supplies no lower bound for the determinants.

### Source and review limits

The complete v4 theorem and its exact [independent whole finding](Yin_R_G1086_v3.md#disconnected-salem-cut-whole) are reused as adopted inputs, rather than re-proved in this extension.
Its Pri11, numerical Smy08 and classical capacity inputs keep their already recorded statement, applicability and source-proof limits.
The private-branch interface keeps the exact C860 v7 and C858 scope.
No original source PDF, new external geometric theorem, computation output or mutable Draft was introduced.
There was no numerical threshold evaluation or proof-assistant verification.
This review does not broaden the result to arbitrary compact cuts, covers, determinant-valuation bounds or the unrestricted [G0001 objective](../../tasks/Yin_T_G0001_v1.md#contract).
No Claim assessment, Task decision or navigation file is changed by this record.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole exterior-cut finding](#exterior-salem-cut-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole exterior-cut finding](#exterior-salem-cut-whole) | [C855 v5 statement](../../claims/Yin_C_G0855_v5.md#statement) | Entire EX1--EX2, actual original trace, continuation only on the unbounded component, finite graphs with isolated vertices and branch points in filled faces, uniform thresholds and hypothetical-sequence consequence. |
| [Whole exterior-cut finding](#exterior-salem-cut-whole) | [C855 v5 complete argument](../../claims/Yin_C_G0855_v5.md#argument) | Complete filling equality, finite filled-component topology, outer monodromy, closest-component construction, root-component condition, adopted v4 application and all conclusion limits. |
| [Whole exterior-cut finding](#exterior-salem-cut-whole) | [C855 v5 exact inputs](../../claims/Yin_C_G0855_v5.md#exact-inputs) | Exact adopted v4 theorem, original private-character branches and capacity/transfinite-diameter identity, without new external source-proof coverage. |
| [Whole exterior-cut finding](#exterior-salem-cut-whole) | [C855 v4 adopted theorem](../../claims/Yin_C_G0855_v4.md#decision-whole-independent-review-2026-11-04) | Complete adopted DC1--DC16 at its exact fixed scope; application to the newly constructed graph J rather than automatic transfer of its earlier entire-complement application. |
| [Whole exterior-cut finding](#exterior-salem-cut-whole) | [C855 v4 graph statement](../../claims/Yin_C_G0855_v4.md#disconnected-cut-capacity) | Uniform finite-graph lower bounds with every original root and at least two roots per root-containing component, including single-rotation strengthening. |
| [Whole exterior-cut finding](#exterior-salem-cut-whole) | [C855 v4 branch and sequence interfaces](../../claims/Yin_C_G0855_v4.md#relation-to-the-original-trace-and-what-remains-open) | Genuine branches on every trace branch and DC16, with preserved determinant and total-Mahler exclusions. |
| [Whole exterior-cut finding](#exterior-salem-cut-whole) | [R1086 v3 whole finding](Yin_R_G1086_v3.md#disconnected-salem-cut-whole) | Actual reused independent whole evidence for v4 and its accepted-source limits; no retrospective review of v5. |
| [Whole exterior-cut finding](#exterior-salem-cut-whole) | [C855 v2 capacity interface](../../claims/Yin_C_G0855_v2.md#sources-and-proof-interfaces) | Only capacity normalization and the accepted capacity/transfinite-diameter identity used in the direct filling proof. |
| [Whole exterior-cut finding](#exterior-salem-cut-whole) | [C860 v7 private branch interface](../../claims/Yin_C_G0860_v7.md#componentwise-pole-rank) | Original private roots and square-class independence over C(x), with its C858 input; no new Padé-rank or arithmetic review. |
| [Whole exterior-cut finding](#exterior-salem-cut-whole) | [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) | Scope comparison only; no unrestricted Mahler-gap or Task-completion review. |
