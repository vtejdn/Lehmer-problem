---
author: Yin
---

# Independent whole review of arbitrary compact exterior cuts

Review act: 2026-11-04T23:59 UTC.
The human record author is Yin.
This is a separately organized independent agent review of the entire [C855 v6 statement](../../claims/Yin_C_G0855_v6.md#statement), AC1--AC4 and the uniform sequence consequence, and its [complete argument](../../claims/Yin_C_G0855_v6.md#argument).
The reviewer did not participate in developing this extension and received no development dialogue, author explanation, mathematical development summary or rolling Draft.
The fixed v6 candidate and its necessary actual inputs were read directly.
The reviewer's earlier [v5 whole inspection](Yin_R_G1086_v4.md#exterior-salem-cut-whole) was a review role, not proof development.
This finding reuses the exact [independently adopted v5 theorem](../../claims/Yin_C_G0855_v5.md#decision-whole-independent-review-2026-11-04) and checks every new step removing the finite-graph restriction.
No substantive repair was supplied, and v6 had no selected assessment during this review.

## Retained input and exact new scope

Earlier R1086 findings remain at their own fixed C855 versions, relationships, times and source limits.
In particular the finite-graph review does not itself certify arbitrary compact cuts.
The new obligations are the nested dyadic-square construction, the finite-graph boundary and its exact unbounded domain, equality of the square union's capacity with its boundary, the fixed-k maximum limit, the subsequent capacity limit and the uniform quantitative transfer.
The new statement includes nonempty compact sets with infinitely many components, no regular boundary, and branch points in bounded complementary components.
Its only analytic continuation hypothesis remains that of the same original exterior germ throughout the unbounded complementary component.

<a id="compact-exterior-salem-cut-whole"></a>
## Whole arbitrary-compact-cut finding

**Finding:** no unresolved mathematical gap was found in the entire C855 v6 statement and argument AC1--AC4 at the stated actual-input and accepted-source scope.
The finite-graph restriction is removed by the displayed approximation and directly proved capacity continuity.
The bounds \(m^2/\log d\) and, for \(S=\{0\}\), \(3m^2/[\log(4/m)+5]\) retain exactly the absolute eventual degree thresholds available from v5, without loss or dependence on K.
The hypothetical near-one sequence comparison is uniform over all stated compact cuts and rotations.
The result remains a capacity-envelope lower bound and gives no determinant lower bound, determinant-valuation upper bound or unrestricted positive total Mahler gap.

### The quantitative premise is the actual adopted exterior theorem

The [v5 statement](../../claims/Yin_C_G0855_v5.md#statement) fixes the actual Salem polynomial, original degree and total measure, every original conjugate, the prime multiplier orbit and the exterior germ \(F(z)=f(1/z)\).
The allowed S are exactly \(\{0\},\mathbb F_q^*,\mathbb F_q\), including the single unrotated radical.
V6 uses this same data throughout every approximation.
The v5 theorem needs only single-valued holomorphic continuation on the unbounded complement of its finite graph, allows isolated graph vertices and branch points in filled faces, and has thresholds independent of the graph and conductor.
Its actual [adoption](../../claims/Yin_C_G0855_v5.md#decision-whole-independent-review-2026-11-04) selects the exact [R1086 v4 whole finding](Yin_R_G1086_v4.md#exterior-salem-cut-whole).
The present application therefore does not rely on the more restrictive entire-complement hypothesis of older versions or on an unadopted extension.

### The square construction and exterior restriction

For each \(n\ge0\), a bounded K meets only finitely many standard dyadic squares of side \(2^{-n}\), including all squares incident to any boundary point of K.
Every selected square is closed, so \(K_n\) is compact; it contains K and has nonempty interior because K is nonempty.
Each selected child square is contained in a dyadic parent that also meets K.
The convention of including all meeting squares handles points on grid lines and vertices and gives \(K_{n+1}\subset K_n\) without an exceptional boundary case.
Every point of \(K_n\) lies at distance at most \(\sqrt2\,2^{-n}\) from a point of K in the same square.
Since K is closed, these bounds prove \(\bigcap_nK_n=K\).

The topological boundary \(\Gamma_n\) is a finite union of axis-parallel segments, subdivided at their endpoints and contacts.
Point contacts, polygonal corners and holes cause only finitely many vertices.
Segments internal to the union are absent from this boundary, and the remaining segments form a compact finite embedded graph at exactly the v5 scope.
Because the square union is nonempty and bounded with interior, its boundary is nonempty.

The complement of \(\Gamma_n\) separates into the exterior of \(K_n\) and the interior of \(K_n\).
Every interior component is bounded and cannot connect to infinity without meeting \(\Gamma_n\).
Thus the unbounded components of \(\mathbb C\setminus\Gamma_n\) and \(\mathbb C\setminus K_n\) coincide.
Because \(K\subset K_n\), that common connected unbounded domain is contained in \(\Omega_K\).
The given single-valued holomorphic exterior function restricts to it and retains the original germ at infinity.
Consequently v5 applies to every \(\Gamma_n\) with the same P, d, m, q, I and S.
No assertion about continuation on any bounded face of \(K_n\), \(\Gamma_n\) or K is used.

### Boundary capacity: AC3

Write

\[
 V_k(E)=\max_{(z_1,\ldots,z_k)\in E^k}
                  \prod_{1\le i<j\le k}|z_i-z_j|,
 \qquad
 D_k(E)=V_k(E)^{2/[k(k-1)]}.
\]

These maxima exist for every nonempty compact E, including finite or polar sets.
For fixed other coordinates in \(K_n\), the Vandermonde modulus in the remaining coordinate is a nonnegative constant times the modulus of a polynomial.
If the constant is zero, any coordinate replacement preserves the required inequality.
Otherwise the maximum-modulus principle on the bounded polygonal interior component puts its maximum on the component boundary, which lies in \(\Gamma_n\).
Points of \(K_n\) outside its interior already lie on \(\Gamma_n\).
The boundary inclusion also holds for components separated by point contacts.

Successive coordinate replacements give \(V_k(K_n)\le V_k(\Gamma_n)\), while \(\Gamma_n\subset K_n\) gives the reverse inequality.
Hence \(D_k(K_n)=D_k(\Gamma_n)\) for every \(k\ge2\).
Taking the transfinite-diameter limit using the [accepted classical identity](../../claims/Yin_C_G0855_v2.md#sources-and-proof-interfaces) proves AC3.
This step requires only polynomial maximum modulus on the explicit polygonal domains.
No equilibrium-measure description of a possibly irregular boundary is used.

### Fixed-k continuity and the capacity limit: AC4

For fixed k, the numbers \(V_k(K_n)\) decrease and are bounded below by \(V_k(K)\).
A maximizing tuple for each n lies in the fixed compact product \(K_0^k\), so a subsequence with indices tending to infinity converges.
For every fixed j, the sufficiently late tuples belong to the closed set \(K_j^k\); hence the limiting tuple belongs to their intersection \(K^k\).
Continuity of the Vandermonde modulus identifies its value with \(\lim_nV_k(K_n)\).
Maximality on K and the reverse inclusion inequality therefore give equality with \(V_k(K)\).
Taking the positive power \(2/[k(k-1)]\) proves AC4, also when the limit is zero.
A different convergent tuple subsequence may be used for each fixed k; no simultaneous maximizing tuple is assumed.

The elementary monotonicity in k has the correct exponent.
Multiplying the Vandermonde products of the \(k+1\) different k-point subtuples of a \((k+1)\)-point tuple counts each pair exactly \(k-1\) times.
Bounding each subtuple product by \(V_k(E)\) yields

\[
 V_{k+1}(E)^{k-1}\le V_k(E)^{k+1},
 \qquad D_{k+1}(E)\le D_k(E).
\]

These inequalities involve no division by a Vandermonde product and remain valid when it is zero.
Together with the accepted identity they give \(\operatorname{cap}E=\inf_{k\ge2}D_k(E)\).
Capacity monotonicity under inclusion also follows directly from these finite maxima.

Let \(c=\lim_n\operatorname{cap}K_n\), which exists as a finite nonnegative number because the sets decrease inside \(K_0\).
Inclusion gives \(c\ge\operatorname{cap}K\).
For every fixed k, the inequalities \(\operatorname{cap}K_n\le D_k(K_n)\) and AC4 give \(c\le D_k(K)\).
Taking the infimum only after that fixed-k passage gives \(c\le\operatorname{cap}K\).
Thus \(\operatorname{cap}K_n\downarrow\operatorname{cap}K\).
This is a direct two-inequality argument, not an unproved exchange of an infimum with a limit.
It explicitly includes the initially possible case \(\operatorname{cap}K=0\).

### Bounds, quantifiers and sequence scope

Once d reaches the fixed v5 threshold, every graph \(\Gamma_n\) satisfies its lower bound for the same original input.
AC3 therefore gives \(\operatorname{cap}K_n\ge\exp(m^2/\log d)\) for every n.
The decreasing-capacity limit gives the same positive lower bound for K, proving AC1.
Taking logarithms is consequently justified by a proved positive capacity, not by an omitted nonpolarity assumption.
For \(S=\{0\}\), the identical argument gives AC2 with its full displayed constant.

No approximation accuracy is chosen as a function of m, d, q or K, and every n uses exactly the same degree threshold.
There is no loss in the bounds and no hidden cutoff depending on component count or boundary regularity.
The theorem thus covers all nonempty compact sets meeting the stated exterior-continuation hypothesis, not merely regular or finitely connected ones.

On a hypothetical actual Salem sequence with \(m\to0\), the retained fixed-degree finiteness argument gives \(d\to\infty\).
The accepted quantitative premise supplies

\[
 \frac{\log\operatorname{cap}K}{\log d/d}
       \ge\frac{d m^2}{(\log d)^2}\longrightarrow\infty,
\]

with the original numerical Dobrowolski consequence and its actual source limits.
Because the right side is independent of the compact cut and rotations, the claimed uniformity follows.
No actual near-one sequence is constructed, and no determinant-index limit is interchanged with the compact approximation.
The result concerns the same exterior function and its capacity envelope; it does not extend to another function, a covering-surface construction or an estimate bypassing that envelope.
The unrestricted [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) is therefore not completed.

### Source and verification limits

The complete v5 theorem and its independently reviewed v4 support are reused at their exact adopted scopes.
The original degree, actual-root, Pri11 and numerical Smy08 inputs keep the source-proof boundaries recorded in those materials and their actual R1086 findings.
The capacity/transfinite-diameter equality remains the same accepted classical interface; AC3, AC4 and the needed continuity were checked directly here.
No additional theorem on arbitrary-compact capacity continuity or equilibrium measures is a premise.
No original source PDF was newly inspected, and no external source proof was newly audited.
No numerical experiment, threshold evaluation, native computation output or proof-assistant certificate was used.
No Claim assessment, Task decision or navigation file is changed by this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole arbitrary-compact-cut finding](#compact-exterior-salem-cut-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole arbitrary-compact-cut finding](#compact-exterior-salem-cut-whole) | [C855 v6 statement](../../claims/Yin_C_G0855_v6.md#statement) | Complete AC1--AC2 and hypothetical-sequence consequence for every nonempty compact exterior cut, exact original function, no boundary or finite-component restriction, absolute thresholds and all exclusions. |
| [Whole arbitrary-compact-cut finding](#compact-exterior-salem-cut-whole) | [C855 v6 complete argument](../../claims/Yin_C_G0855_v6.md#argument) | Entire nested-square construction, finite polygonal boundary, exact unbounded-domain restriction, AC3, AC4, monotonic transfinite diameters, decreasing capacity limit and lossless quantitative transfer. |
| [Whole arbitrary-compact-cut finding](#compact-exterior-salem-cut-whole) | [C855 v6 exact source interfaces](../../claims/Yin_C_G0855_v6.md#exact-inputs-and-source-boundaries) | Adopted v5 quantitative theorem and retained classical capacity identity, with no new external regularity, equilibrium-measure, root-distribution or arithmetic theorem. |
| [Whole arbitrary-compact-cut finding](#compact-exterior-salem-cut-whole) | [C855 v5 adopted theorem](../../claims/Yin_C_G0855_v5.md#decision-whole-independent-review-2026-11-04) | Exact adopted EX1--EX2 and sequence consequence, applied to every Gamma_n with the same original data and no conductor or graph dependence in the threshold. |
| [Whole arbitrary-compact-cut finding](#compact-exterior-salem-cut-whole) | [C855 v5 statement](../../claims/Yin_C_G0855_v5.md#statement) | Original Salem trace definition, all conjugates and permitted unions S, and continuation only on the unbounded complement of a finite embedded graph. |
| [Whole arbitrary-compact-cut finding](#compact-exterior-salem-cut-whole) | [R1086 v4 whole finding](Yin_R_G1086_v4.md#exterior-salem-cut-whole) | Actual reused independent evidence for the adopted finite-graph exterior theorem; no retrospective coverage of the new arbitrary-compact extension. |
| [Whole arbitrary-compact-cut finding](#compact-exterior-salem-cut-whole) | [C855 v2 capacity interface](../../claims/Yin_C_G0855_v2.md#sources-and-proof-interfaces) | Only the accepted capacity/transfinite-diameter equality and normalization; new boundary equality and decreasing-compact continuity are checked directly. |
| [Whole arbitrary-compact-cut finding](#compact-exterior-salem-cut-whole) | [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) | Scope comparison only; no unrestricted total-Mahler gap or Task-completion finding. |
