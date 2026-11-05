---
author: Yin
---
# The capacity cost for every admissible compact exterior cut

This fixed result removes the finite-graph restriction from the independently adopted [C855 v5 exterior-cut theorem](Yin_C_G0855_v5.md#decision-whole-independent-review-2026-11-04).
The coordinating research agent developed the extension for Yin, and the selected assessment adopts its independent whole review at the exact stated scope.
All prior versions retain their exact statements, proofs, assessments and source limits.
The new step is an explicit finite-square approximation and a direct proof of decreasing-compact capacity continuity from finite transfinite diameters.

## Statement

Use the actual Salem polynomial P, original degree d, total measure 0<m<=1, odd prime q, nonempty mask I, multiplier orbit O, used-position union S and exterior germ F(z)=f(1/z) exactly as defined in [C855 v5's statement](Yin_C_G0855_v5.md#statement).
Thus every original conjugate is retained, and S is {0}, F_q^* or F_q.
Let K be any nonempty compact subset of C, and let Omega_K be the unbounded component of C minus K.
Suppose the exterior germ F has single-valued holomorphic continuation throughout Omega_K.
No regularity, connectedness, finite-component condition, containment of the branch points in K, or continuation on bounded complementary components is assumed.
Then an absolute D0 independent of P,q,I,K gives, for all d>=D0,

    log cap(K)>=m^2/log d.                                  (AC1)

For S={0}, one also has the stronger eventual estimate

    log cap(K)>=3m^2/[log(4/m)+5].                           (AC2)

Both thresholds and their uniformity are inherited without loss from the adopted finite-graph theorem and are not numerically evaluated.
On a hypothetical actual Salem sequence with m tending to zero, log cap(K)/(log d/d) tends uniformly to infinity over all these compact cuts and rotations.
No such sequence is asserted to exist.
This class includes standard admissible compact cuts for continuation of the original exterior germ; it does not include a different function, a meromorphic map on a covering surface or a determinant estimate not using this capacity envelope.
The result is not a lower bound for actual Hankel determinants, an upper bound for their arithmetic valuations, or a positive total Mahler gap.

## Exact inputs and source boundaries

The quantitative input is the complete independently adopted [C855 v5 EX1--EX2](Yin_C_G0855_v5.md#decision-whole-independent-review-2026-11-04) and its stated sequence consequence.
That theorem retains C855 v4's actual-root discriminant, finite discrepancy and arithmetic lower-bound inputs, including their exact source-proof limitations.
No fresh theorem about root distribution, arithmetic, equilibrium measures or capacity regularity is imported here.
The only classical capacity interface is the accepted equality with transfinite diameter retained in [C855 v2](Yin_C_G0855_v2.md#sources-and-proof-interfaces).
The new continuity assertion is proved directly below, rather than cited as an additional external result.
The maximum-modulus principle is applied only to polynomials on bounded polygonal domains.
No mutable Draft or numerical experiment is a premise.

## Argument

### Explicit outer polygonal approximations

For each integer n>=0, take the closed squares of the standard dyadic grid of side 2^(-n) that meet K, and let K_n be their union.
The union is finite because K is bounded, and it contains K.
The common grid convention includes every square meeting a boundary point, so each selected child square lies in a selected parent square.
Consequently K_(n+1) is a subset of K_n.
Every point of K_n lies within sqrt(2) 2^(-n) of K, and therefore the intersection of all K_n is exactly K.
Each K_n is a nonempty compact finite union of closed squares with nonempty interior.

Let Gamma_n be the topological boundary of K_n.
It is a compact finite embedded graph of polygonal arcs; corners, shared edges and point contacts are resolved into finitely many vertices, and redundant collinear subdivisions may be removed.
The unbounded components of C minus Gamma_n and C minus K_n agree.
Indeed any path from infinity into the interior of K_n must first meet Gamma_n; conversely the unbounded component of C minus K_n avoids that boundary.
This common unbounded domain lies inside Omega_K, because K is a subset of K_n.
The given single-valued holomorphic exterior function therefore restricts to the unbounded complement of Gamma_n.
The adopted finite-graph theorem applies to Gamma_n with exactly the same P,d,m,q,I,S.
There is no degree or conductor depending on n.

### The polygonal boundary has the same capacity

For k>=2, write D_k(E) for the maximum k-point Vandermonde product on a nonempty compact E, raised to the power 2/[k(k-1)].
For fixed other coordinates in K_n, that product as a function of one coordinate is a constant times the modulus of a polynomial.
If the coordinate lies in the interior of K_n, the maximum-modulus principle on its bounded polygonal interior component moves it to Gamma_n without decreasing the product.
If it is on Gamma_n, no movement is needed.
The zero-polynomial-product case satisfies the same inequality immediately.
Replacing all coordinates successively shows

    D_k(K_n)=D_k(Gamma_n), k>=2.

The accepted transfinite-diameter identity, taking k to infinity, therefore gives

    cap(K_n)=cap(Gamma_n).                                  (AC3)

In particular no assertion about an arbitrary boundary's equilibrium measure or Dirichlet regularity is used.
The graph theorem and (AC3) imply both displayed lower capacity bounds for every K_n once the corresponding fixed original-degree threshold is met.

### Continuity for this decreasing compact sequence

For fixed k, the continuous Vandermonde product attains its maximum on K_n^k.
The maxima decrease with n.
Choose maximizing tuples; compactness of K_0^k gives a convergent subsequence.
Its limit lies in K_j^k for every fixed j, because every sufficiently late tuple does and K_j is closed.
Thus the limit lies in K^k.
Continuity of the product proves

    D_k(K_n) decreases to D_k(K), for each fixed k>=2.        (AC4)

Capacity is monotone, so cap(K_n) decreases to a limit c>=cap(K).
For every k and n, the elementary transfinite-diameter inequality gives cap(K_n)<=D_k(K_n).
Taking n to infinity and then the infimum over k, using that D_k(K) decreases to cap(K), yields

    c<=inf_(k>=2)D_k(K)=cap(K).

Hence cap(K_n) decreases to cap(K).
For completeness the monotonicity of D_k used here follows by multiplying the Vandermonde products of all k-point subtuples of a (k+1)-point tuple: every pair occurs exactly k-1 times, giving D_(k+1)(E)<=D_k(E).
This proves the needed continuity directly, including the case cap(K)=0.

### Quantitative passage to the actual compact cut

The same original-degree threshold makes cap(K_n) at least exp(m^2/log d) for every n.
The decreasing limit proves (AC1) and in particular proves that K has positive capacity, so the logarithm is legitimate without an extra hypothesis.
The identical limit argument with the stronger single-rotation constant proves (AC2).
The approximation introduces no loss in either numerical bound and no cutoff depending on K.
The sequence comparison follows directly from the adopted v5 consequence, or its retained original numerical inequality d m^2/(log d)^2 tending to infinity.
No limit exchanging the original input with the determinant index occurs in this proof.
All original-input, source-proof and determinant-direction limits remain as stated above.
The unrestricted G0001 objective remains unresolved.

## Assessment history

### Decision whole-independent-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T00:01 |
| status | proved |
| reason | Adopt the entire arbitrary-compact exterior-cut statement and AC1--AC4 argument after independent R1086 v5. Explicit nested square unions, polygonal boundary capacity and fixed-k transfinite-diameter limits remove all graph, boundary-regularity and finite-component restrictions without changing the original function, threshold or constants. The exact adopted finite-graph input and its source-proof limits remain unchanged. This lower bound for the capacity envelope supplies neither a determinant lower bound nor the unrestricted positive total Mahler gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete compact-cut statement](#statement) | AC1--AC2 and uniform hypothetical-sequence consequence for every nonempty compact K admitting the specified exterior continuation, with all original roots, prime masks and exact exclusions. |
| argument | [Complete approximation argument](#argument) | Every step of the nested dyadic-square construction, common unbounded domain, boundary-capacity equality, fixed-k maximum limit, decreasing-capacity proof including polar sets and uniform quantitative passage. |
| dependency | [Adopted finite-graph exterior theorem](Yin_C_G0855_v5.md#decision-whole-independent-review-2026-11-04) | Exact EX1--EX2 and sequence consequence, applied at the same original input to each polygonal boundary; the retained C855 v4 root, arithmetic and source limits are unchanged. |
| dependency | [Original trace definition](Yin_C_G0855_v5.md#statement) | Actual Salem polynomial, total measure, all conjugates, full multiplier orbit, used-position union and identical exterior germ. |
| dependency | [Capacity identity](Yin_C_G0855_v2.md#sources-and-proof-interfaces) | Only the accepted capacity/transfinite-diameter identity and normalization; the new compact-continuity proof is explicit here. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1086_v5.md#compact-exterior-salem-cut-whole) | Entire current statement and AC1--AC4, all compact-set and uniformity quantifiers, exact source-interface limits and no G0001 completion. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-05)
