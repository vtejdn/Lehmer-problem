---
author: Yin
---

# Independent whole review of disconnected Salem branch-cut capacity

Review act: 2026-11-04T23:44 UTC.
The human record author is Yin.
This is a separately organized independent agent review of the complete [C855 v4 statement and DC1--DC16](../../claims/Yin_C_G0855_v4.md#disconnected-cut-capacity), including its application to the original nonempty-mask orbit trace.
The reviewer did not contribute to substantive proof development and received no development dialogue, author explanation, mathematical development summary or rolling Draft.
The fixed candidate and its necessary actual mathematical inputs were read directly.
The earlier [R1086 v2 finding](Yin_R_G1086_v2.md#salem-radial-hull-whole) was consulted as evidence about the separately retained v3 scope after initial checks of the new energy estimates; it was not used as a verdict on v4.
No substantive repair was supplied, and C855 v4 had no selected assessment during this review.

## Retained evidence and exact scope

[R1086 v1](Yin_R_G1086_v1.md#raw-p2-whole) and [R1086 v2](Yin_R_G1086_v2.md#salem-radial-hull-whole) remain at their own fixed C855 v2 and v3 inputs, times, relationships and source limits.
This new finding concerns disconnected finite-graph cuts and does not replace either earlier review.
The obligations checked here are the actual squarefree integer polynomial, the aggregate nearest-separation estimate, finite-energy local measures on the specified graph, the neutral and outer energy bounds, both conductor regimes, the uniform arithmetic limits, and the trace's branch-cut applicability.
The [unrestricted G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) was read for the conclusion's scope only.
The current erratum was empty and supplied no objection to these inputs.

<a id="disconnected-salem-cut-whole"></a>
## Whole disconnected-cut finding

**Finding:** no unresolved mathematical gap was found in the complete C855 v4 statement, argument DC1--DC16, and original-trace application at the stated finite-graph and accepted-source scope.
There is an absolute eventual degree threshold, uniform over the actual Salem inputs with \(0<m\le1\), all three permitted rotation collections and all stated graphs, for

\[
 \log\operatorname{cap}K\ge\frac{m^2}{\log d}.
\]

For the single rotation, the stronger eventual bound is \(3m^2/[\log(4/m)+5]\).
The threshold is existential and was not evaluated numerically.
The conclusion concerns a geometric capacity envelope and supplies neither a lower bound for the Hankel determinants nor a positive total Mahler gap.

### Actual original input and source interfaces

The [unique-expanding-conjugate argument in C855 v3](../../claims/Yin_C_G0855_v3.md#the-mesh-estimate-uses-the-actual-integral-squared-polynomial) proves that distinct Salem conjugates cannot have a root-of-unity quotient.
Indeed an automorphism taking one to the unique expanding conjugate would take the other to a distinct conjugate of the same expanding modulus.
All positive powered conjugate lists therefore retain degree \(d\) and have no repeated roots.
An equality, even up to a root of unity, between a squared and a fourth-powered conjugate would equate their positive absolute heights \(2m/d\) and \(4m/d\), and is impossible.
Consequently A has exactly \(n=2ds\) simple roots.
Each permitted S is stable under the cyclotomic Galois action, and the full original conjugate list is stable under every Galois automorphism, so A is a monic integer polynomial.
Its total logarithmic measure is \(6sm\), its neutral-root count is \(N=2s(d-2)\), and its four off-circle radius orbits contain \(4s\) roots.
These facts use actual original conjugates rather than a freely prescribed angular configuration.

The capacity convention and capacity/transfinite-diameter identity are reused only at the accepted scope of [C855 v2](../../claims/Yin_C_G0855_v2.md#sources-and-proof-interfaces).
The trial-measure inequality in v4 follows in the stated direction by taking the expected logarithm of the Vandermonde product and then its transfinite-diameter limit.
For every measure constructed below the logarithmic kernel is bounded below on its compact support and its positive singular part is integrable, so this expectation is well defined.
The arcsine energy \(\log(4/l)\) for an interval of length \(l\) has the correct factor four; the cosine substitution and circle logarithmic mean compute it directly.

The [canonical Pri11 U001](../literature/Pri11/Yin_U001.md#pri11-u001) supplies the finite estimate for a simple integer polynomial of its actual degree at least 55, with the ordinary total Mahler measure and a real globally Lipschitz compactly supported test.
It does not require irreducibility or roots in the unit disk, so it applies to this A with degree \(n\) and \(\log M(A)=6sm\).
Its original potential-theory proof remains outside this review.
The numerical input at [C147 v5](../../claims/Yin_C_G0147_v5.md#reuse-and-source-scope) is the accepted Smy08 statement \(M(P)>1+(1/1200)(\log\log d/\log d)^3\), not C147's cyclic-norm conclusion.
For \(d\ge55\), its added term lies in \((0,1]\), and \(\log(1+x)\ge x/2\) gives DC4 for the original total measure \(m\), without a factor \(1/d\).
The [Smy08 normalization and proof boundary](../literature/Smy08/Yin_U001.md#smy08-u001) were checked; neither the defective survey resultant explanation nor the original Dobrowolski proof is adopted as newly audited evidence.

### Aggregate separation and local graph measures: DC5--DC8

For two incoming nearest-neighbor segments of lengths \(r\ge t\), nearest-neighbor minimality gives the opposite side length at least \(r\), hence the angle between them has cosine at most \(t/(2r)\le1/2\).
There can be at most six incoming segments.
Adding the chosen outgoing edge bounds the simple undirected graph's degree by seven, and greedy edge coloring needs at most \(2\cdot7-1=13\) colors.
Each color is a matching and each undirected edge represents at most two directed choices, including tied nearest neighbors selected arbitrarily.

For a matching of edges shorter than one, the row replacements are disjoint, so their determinant divisors multiply exactly.
The unchanged and divided-difference row norms are bounded respectively by \(\sqrt n M_u^{n-1}\) and \(n^{3/2}\max(M_u,M_v)^{n-1}\), where \(M_u=\max(1,|u|)\).
Their paired product is at most \(n^2(M_uM_v)^{2(n-1)}\).
The nonzero integer discriminant implies \(|V|\ge1\), while Hadamard gives \(|V|\le\prod_E|u-v|\,n^{n/2+|E|}M(B)^{2(n-1)}\).
Thus one matching contributes at most \(n\log n+2nh\), and the factors thirteen and two give exactly the safe constants \(26n\log n+52nh\) in DC5.
Edges of length at least one contribute zero to the desired positive logarithms.
No external aggregate-separation theorem is needed.

A connected component of a finite embedded graph is path connected.
For each root the second root in its component lies at distance at least \(\delta_i>r_i\), so the first-exit path in DC6 exists, remains in the closed disk and reaches its boundary.
Projection onto its endpoint line covers an interval of length \(r_i\).
The first-hitting parameter at each projected level is Borel: its sublevel sets are images of compact initial path intervals under the continuous projection.
Lifting the atomless arcsine measure by this section cannot decrease pairwise distances and therefore cannot increase logarithmic energy.
This proves DC7 with finite energy, even when the path is not a straight segment.

For distinct roots, \(r_i+r_j\le|b_i-b_j|/(4n)\), giving the mutual-energy error at most \(1/(2n)\).
The identity \(\log(4/r_i)=\log(32n)+\max(\log(1/m),\log(1/\delta_i))\) and \(m\le1\) give DC8.
All these constructions stay in K and require no connectedness between different root components.

### Neutral energy and the uniformly supported discrepancy test: DC9--DC13

The complete ordered off-diagonal energy of the roots is \(-\log|\operatorname{disc}A|\le0\).
There are exactly \(8sN+4s(4s-1)\) ordered pairs involving an off-circle root, and each distance is at most \(2e^4\).
Deleting those pairs therefore raises the remaining energy sum by at most their count times \(L_0\).
The N diagonal local energies use DC8, and their separation contribution is bounded by the full DC5 sum.
Substituting \(h=6sm\), dividing by \(N^2\), and adding the mutual displacement cost yields precisely DC9, including \(312nsm\).

The inequalities \(N\ge n/2\), \(n=2ds\ge2d\), and decreasing \(\log x/x\) on \(x\ge8\) remove every growing-conductor factor from DC9.
In particular \(ns/N^2=O(1/d)\), \(s/N=1/[2(d-2)]\), and \(s^2/N^2=O(1/d^2)\).
Thus DC10 is uniform in both permitted prime collections, including unbounded q.

For an outer root \(a=e^{4m}\zeta^j\), the nearest distinct radius is \(e^{2m}\), at gap at least \(2m\), and distinct rotations at the same radius are at distance at least \(4/q\).
The radii used in DC11 consequently stop before any other root, and the required path exists.
Its support lies where \(e^{3m}\le|z|\le e^4+1\), since \(e^{4m}-m\ge e^{3m}\).
Thus every supported z has distance at least \(3m\) from the unit circle.

For such z, the proposed cutoff is one at all roots of A and on the unit circle, and is supported in the radius-\(R=e^4+1\) disk.
Within that support, \(|\log\max(m,|z-w|)|\le B_m\); the truncated logarithm is \(1/m\)-Lipschitz.
The cutoff product has Lipschitz constant at most \(1/m+B_m\le(2+C_0)/m=C_1/m\), using \(m\log(1/m)\le1/e\).
The same bound extends across the support boundary, where the cutoff vanishes.
At neutral roots and on the unit circle the logarithm is untruncated, and its circular mean is \(\log|z|\).
Every hypothesis and constant of Pri11 therefore matches DC12 with the actual degree n and total measure \(6sm\).

Removing \(4s\) off-circle terms and multiplying the discrepancy by \(n/N\le2\) costs at most \((4s/N)(B_m+5)\), since \(|\log|z||<5\).
Moving a neutral root by at most \(m/(8n)\), from an initial distance at least \(3m\), changes its logarithmic distance by at most \(1/n\).
This proves DC13 for every supported z, so it remains valid after integration against the whole outer local measure.
The bounds \(\log n/n\le\log(2d)/(2d)\) and \(6sm/n=3m/d\) prove the claimed uniformity of eta.

### Mixtures and both conductor regimes: DC2--DC3 and DC14--DC15

When eta is at most m, the cross energy is at most \(-2m\).
Expanding the mixture at \(t=2m/(L+4m+\epsilon)\), which lies strictly between zero and one, gives

\[
 I(\nu)\le\epsilon-
 \frac{4m^2}{L+4m+\epsilon}-
 \frac{4m\epsilon}{L+4m+\epsilon}.
\]

Discarding the last nonpositive term yields DC14 with the correct capacity sign.
For s equal to one, \(\epsilon\le m^2/(L+5)\) implies \(\epsilon\le1\) and \(L+4m+\epsilon\le L+5\), giving DC3.
DC4 bounds \(1/m\) by a fixed power of \(\log d\); all remaining errors are negative powers of d times powers of \(\log d\), \(1/m\) and \(\log(1/m)\).
Hence eta divided by m and \(\epsilon(L+5)/m^2\) tend to zero uniformly over the actual stated Salem class.
Also \(L+5=\log(4/m)+5\le3\log d\) eventually, so DC3 supplies DC2 for the single-rotation option as well.

For \(q\le d\), the same arithmetic bound gives \(L\le2\log d\), then \(L+4m+\epsilon\le3\log d\), eta at most m, and \(\epsilon\le m^2/(3\log d)\), all beyond one absolute degree threshold.
DC14 consequently gives \(4m^2/(3\log d)-m^2/(3\log d)=m^2/\log d\).
The threshold does not depend on q or on the chosen S in this range.

For \(q\ge d\), every outer local support of radius \(r_*\) exists by the same root separation and component argument.
Its diagonal energy is at most \(\log(32q)+\max(\log(1/m),\log q)\).
The pairwise displacement is at most \(1/(4q^2)\), compared with central distance at least \(4/q\), so the mutual error is at most \(1/(8q)\).
The ordered unscaled distance logarithms are \(q\log q\) for the complete roots of unity and \((q-2)\log q\) after removal of one.
The latter follows by deleting both ordered families involving one, whose total is \(2\log q\).
Both are nonnegative, so dropping their negative energy contribution is legitimate.
Scaling by \(e^{4m}\) contributes \(-4m(1-1/s)\), proving DC15.

Uniformly for \(q\ge d\), DC4 eventually gives \(q\ge1/m\).
The positive terms in DC15 are \(O(\log q/q)\le O(\log d/d)=o(m)\), since \(s\ge q-1\), \(m\le1\), and \(\log x/x\) decreases on this range.
Thus \(I(\nu_{\rm out})\le-2m\), which yields the stronger \(\log\operatorname{cap}K\ge2m\ge m^2/\log d\).
The two conductor regimes cover every permitted prime, with no fixed-conductor assumption.
Capacity monotonicity also proves the stated extension to a larger compact set containing one of the specified graphs.

### Original orbit trace, finite-graph topology and DC16

The union of a full orbit of nonempty masks is a nonempty invariant subset for multiplication by \(\mathbb F_q^*\), hence is exactly one of \(\{0\},\mathbb F_q^*,\mathbb F_q\).
The [geometric private-branch argument of C860 v7](../../claims/Yin_C_G0860_v7.md#componentwise-pole-rank), with its [C858 input](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget), applies over \(\mathbb C(x)\), not merely over the cyclotomic constant field.
A local loop around a branch point at a used position changes the signs of exactly the nonempty subcollection of mask terms containing that position.
Those distinct radical characters are linearly independent, so their signed nonempty sum cannot vanish and the monodromy of the trace is nontrivial on every branch.
Reciprocity and the invariance of S under negation identify the branch-point set in the original x-coordinate with the roots in DC1; inversion in the exterior-coordinate contour gives the same set directly.
No branch point can be deleted by cancellation of the trace terms.

For the single-valued continuation off K stipulated in the candidate, a component containing only one branch point is impossible.
A sufficiently small regular neighborhood of that finite-graph component is disjoint from the other graph components and contains exactly that one branch point.
Its boundary may have several loops if the graph has cycles.
The combined monodromy of those boundary loops is the local sign change at the single enclosed branch point, because there are no other branch points in the neighborhood.
If continuation were single valued on the complement of K, every boundary loop would fix the trace, as would their combined action, contradicting the nontrivial local action already checked.
This also handles graph cycles and nested components without assuming that one simple boundary curve encloses no other component.
The single-valuedness condition here is on the complement of K as stated; the finding does not replace it by continuation only on an arbitrarily selected subdomain of that complement.
The geometric theorem itself applies to all graphs satisfying the stated component hypothesis, whether or not they are cuts for the trace.

On an actual Salem near-one sequence, degree tends to infinity: bounded degree and \(M(P)\le e\) bound the integer coefficients and leave only finitely many minimal polynomials.
DC4 gives

\[
 \frac{d m^2}{(\log d)^2}\ge
 \frac{d(\log\log d)^6}{2400^2(\log d)^8}
 \longrightarrow\infty.
\]

Division of DC2 by \(\log d/d\) therefore proves DC16 uniformly over the stated cuts and rotations.
The [C855 v2 contour comparison](../../claims/Yin_C_G0855_v2.md#the-capacity-bound-applies-to-the-same-shifted-hankel-determinants) bounds Hankel growth above by a capacity, so this lower bound for the envelope cannot become a determinant lower bound.
It does not bound actual determinant valuations above, prohibit better joint arithmetic, classify pathological compact cuts or meromorphic-cover constructions, or complete G0001.

### Verification limits

The review checked the complete fixed statement, local proof, quantified uniformity, exact source applicability and original-trace boundary by mathematical reading and direct derivation.
The accepted Pri11, Smy08 and classical capacity inputs retain their actual external statement and source-proof limits.
No original source PDF was newly inspected and no complete external theorem proof was re-audited.
No numerical experiment, threshold evaluation, native computation output or proof-assistant certificate was used.
No Claim assessment, Task decision or navigation file is changed by this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [C855 v4 statement](../../claims/Yin_C_G0855_v4.md#disconnected-cut-capacity) | Complete finite-graph statement DC1--DC3, actual Salem inputs, every permitted rotation collection, absolute eventual threshold, single-rotation strengthening and monotonicity extension. |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [C855 v4 capacity and arithmetic interfaces](../../claims/Yin_C_G0855_v4.md#capacity-and-arithmetic-interfaces) | Trial-measure inequality, interval energy normalization, exact accepted capacity/Pri11/C147 inputs and DC4, with retained external proof limits. |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [C855 v4 complete argument](../../claims/Yin_C_G0855_v4.md#a-discriminant-bound-for-all-nearest-separations) | Entire ensuing argument DC5--DC16: nearest-neighbor matching bound, local graph measures, neutral energy, exterior discrepancy, mixture, both conductor regimes, actual trace applicability and uniform limit. |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [C855 v4 original-trace scope](../../claims/Yin_C_G0855_v4.md#relation-to-the-original-trace-and-what-remains-open) | Genuine branch points, required root-component condition for single-valued continuation off the finite graph, DC16 and exact determinant/Task exclusions. |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [C855 v2 capacity convention](../../claims/Yin_C_G0855_v2.md#sources-and-proof-interfaces) | Only accepted capacity/transfinite-diameter identity and normalization, with retained Dim19 source limits; no new whole review of v2. |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [C855 v2 determinant direction](../../claims/Yin_C_G0855_v2.md#the-capacity-bound-applies-to-the-same-shifted-hankel-determinants) | Only the upper-envelope direction needed to delimit the conclusion; no determinant lower bound. |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [C855 v3 original Salem degree](../../claims/Yin_C_G0855_v3.md#the-mesh-estimate-uses-the-actual-integral-squared-polynomial) | Unique expanding conjugate, absence of torsion quotients and degree preservation, checked directly for the actual v4 input. |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [Canonical Pri11 U001](../literature/Pri11/Yin_U001.md#pri11-u001) | Exact finite Theorem 3.1/(3.2), actual degree n, simple integral A, total log measure 6sm, test support R, Lipschitz C1/m and normalized circle measure; accepted statement/applicability scope. |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [C147 v5 numerical source scope](../../claims/Yin_C_G0147_v5.md#reuse-and-source-scope) | Only the accepted numerical Smy08 Dobrowolski statement, its original total-measure conversion and uniform asymptotic use; no cyclic-norm substitution. |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [Canonical Smy08 U001](../literature/Smy08/Yin_U001.md#smy08-u001) | Measure/height normalization and actual source-proof limits; no reliance on the defective resultant explanation. |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [C860 v7 geometric branch interface](../../claims/Yin_C_G0860_v7.md#componentwise-pole-rank) | Only private original zeros/poles and square-class independence over C(x), with local trace-monodromy consequence; no new whole review of Padé ranks or precision. |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [C858 original mask independence](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) | Only powered-root noncollision, private rotation square classes and independence of distinct mask radicals, applied to genuine branch points of the same original trace. |
| [Whole disconnected-cut finding](#disconnected-salem-cut-whole) | [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) | Objective comparison only; no unrestricted Mahler-gap or Task-completion finding. |
