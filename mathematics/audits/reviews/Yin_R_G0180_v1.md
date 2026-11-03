---
author: Yin
---
# Integer multiplier variational formula and exact cyclotomic normalizer control: independent whole-proof review

Date and human attribution: 2026-10-11T11:04.
Record author Yin; mathematical inspection by the separately assigned assess_bv19b_current AI reviewer.
No personal human proof inspection or formal verification is asserted.

## Arrangement, inputs and scope

This is an initial whole-proof review of [D_G0005](../../ledger/Yin_L_G0359_v1.md), the root-authored 2026-10-11 revision frozen through Sections1--4.
The reviewer did not contribute to its multiplier/normalizer derivation.
It shares the G0001 conversation and repository context with the author, previously assessed BV19b against G0001, and authored the distinct arithmetic-quotient argument D_G0002.
Those earlier activities did not supply this proof.
The assignment named the obligations to inspect.
No multiplier proof-generation dialogue, author explanation beyond the written draft, or previous independent verdict was consulted before forming the findings below.
The draft's own self-check account was visible but was not used in place of reconstruction.

The review read the complete D_G0005 argument, then the scalar functional in [scalar weight baseline](../../ledger/Yin_L_G0431_v1.md#single-haar-formulation), the finite residual and boundary account in [L4](../../ledger/Yin_L_G0004_v1.md#degree-window-tests), the direct coefficient-Jensen interface [L94](../../ledger/Yin_L_G0094_v1.md), [Den09-U002](../literature/Den09/Yin_U002.md#finite-section-determinant), and the [Smy08 Mahler/Jensen normalization](../literature/Smy08/Yin_U001.md#smy08-height-normalization).
The review does not rerun old computations or re-audit the original Toeplitz/Szego proof: D_G0005 supplies its own approximation proof and uses that finite-section material for comparison and attribution only.

The actual scope covers the exact integer multiplier infimum, zero-free rational approximation including circle roots, scalar minimization, strictness and nonattainment, bounded-normalizer floor and attained minimum, the complete fixed-window/all-degree cyclotomic minimum, its zero-free attaining construction, the nonmonotonic fixed-window normalizer control, and every stated non-gap and non-novelty boundary.
It does not review Task completion, any numerical parameter scan, input-uniform approximation rates, or historical originality.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [D_G0005 integer multiplier formula](../../ledger/Yin_L_G0359_v1.md#integer-multiplier-variational-formula) | Complete Section1: exact all-degree infimum, scalar functional correspondence, circle-root approximation, strictness and nonattainment in the specified zero-free integer polynomial-square class. |
| [Whole-proof finding](#whole-proof-finding) | [D_G0005 bounded normalizer floor](../../ledger/Yin_L_G0359_v1.md#fixed-normalizer-arithmetic-floor) | Complete Section2: integer energy floor, bounded integer-normalizer minimum, necessary logarithmic approximation cost and estimate direction. |
| [Whole-proof finding](#whole-proof-finding) | [D_G0005 exact cyclotomic control](../../ledger/Yin_L_G0359_v1.md#cyclotomic-exact-window-normalizer) | Complete Sections3--4: exact window and all-degree control, zero-free attaining polynomial, explicit hand calculations and retained non-gap/non-novelty scope, with the literal typing corrections identified below required. |
| [Whole-proof finding](#whole-proof-finding) | [Scalar positive-weight functional](../../ledger/Yin_L_G0431_v1.md#single-haar-formulation) | Only the defining scalar functional and its admissible bounded-weight domain needed to check the t times absolute-Q-squared trial; no separate whole-proof acceptance of this other draft. |

## Reconstructed obligations and evidence

1. **All trial values are upper estimates.**
   A zero-free closed-disk Q with Q(0)=k has M(Q)=k by the root formula, including nonmonic Q.
   Parseval and the circle arithmetic/geometric mean yield M(P)^2 k^2<=||PQ||_2^2.
   Unit-circle zeros of P cause only integrable logarithmic singularities.
   No leading coefficient, factor multiplicity or integer normalizer is omitted.
   For t|Q|^2 the scalar functional is t||PQ||_2^2-log t-2log k-1; its derivative vanishes at t=1/||PQ||_2^2, giving log(||PQ||_2^2/k^2), exactly twice the logarithmic trial value.
   This part passes.

2. **Reverse approximation inequality without a spectral gap.**
   Reflect each nonzero root so O(0)=1 and |P|=M(P)|O| on the circle.
   Exterior roots use1-z/alpha, interior roots use1-conj(alpha)z, and conjugate pairs give real coefficients.
   Zero-root monomial factors have circle modulus1 and may be removed before the construction.
   For fixed r<1,1/O(rz) is analytic on a neighborhood of the closed disk and has a positive minimum modulus there.
   Taylor truncation followed by rational approximation preserving constant1 can be chosen uniformly closer than that minimum; it is therefore zero-free by the pointwise triangle inequality.
   Clearing a positive common denominator gives a member of the exact O_k class.
   Every factor |1-beta z|/|1-r beta z| is at most2 for |beta|<=1, so dominated convergence with fixed finite degree proves the infimum is M(P)^2.
   At the finitely many circle zeros the pointwise limit need not equal1, which is harmless for Haar integration.
   No uniform degree/denominator/rate estimate is inferred.
   This part passes.

3. **Attainment and arithmetic discreteness.**
   Equality in the circle mean inequality forces a nonzero polynomial of constant modulus on the circle.
   The autocorrelation at the largest gap between its first and last nonzero coefficients is a single nonzero product, so it must be a monomial.
   A nonmonomial P has a nonzero complex root and cannot divide a monomial; hence no finite trial attains the unrestricted infimum.
   Integer nonzero P has M(P)>=1, and strictness gives integer ||PQ||_2^2>=k^2+1.
   At a fixed integer k the nonempty set of possible positive integer energies has a least element even without a degree bound.
   Finite integer normalizer ranges then have an attained minimum.
   The logarithmic rearrangement in(3) has the correct necessary direction.
   This part passes with the explicit integer type for K required in F1.

4. **Exact finite window and real/rounding costs.**
   For P=1-t^s, splitting coefficient indices modulo the positive integer s makes the product energy a sum over disjoint chains.
   On the chain containing the constant coefficient k, padding to q_n and q_(n+1)=0 gives energy k^2+sum_i d_i^2 with sum_i d_i=k.
   Balancing any two integer differences separated by at least2 strictly reduces the sum of squares.
   The exact optimum therefore has N-b entries a and b entries a+1, k=Na+b,0<=b<N.
   Its added energy is N a^2+(2a+1)b=k^2/N+b(N-b)/N.
   Other chains cannot reduce it.
   This proves the stated lower bound for the entire degree<=sn domain, including coefficients of either sign.

5. **The attaining polynomial obeys the extra zero-free constraint.**
   Put larger differences first.
   All d_i are nonnegative and d_1>0, and all successive q_j are nonnegative with q_0=k.
   The identity(1-z)R(z)=k-sum_i d_i z^i is exact.
   A zero with |z|<1 contradicts the strict triangle inequality.
   A circle zero other than1 would require every positive summand d_i z^i to have phase1; d_1>0 forces z=1.
   Finally R(1)>0.
   Substitution z=t^s preserves zero-freeness of the closed disk.
   Hence the unrestricted integer-chain optimum is attained in the stated smaller class.
   This part passes for all k>=1,n>=0,s>=1 integers, including n=0 and k<N.

6. **All-degree and fixed-window conclusions.**
   Cauchy--Schwarz gives sum d_i^2>=k^2/N, and integer differences give sum d_i^2>=sum|d_i|>=k.
   If N>=k, the differences1 repeated k times and then0 attain k, with Q=k+(k-1)t^s+...+t^(s(k-1)).
   Thus the all-degree fixed-k optimum is1+1/k, and for positive integer K the bounded-k optimum is1+1/K.
   At N=3,s=1 the k=3 and4 ratios are4/3 and11/8 respectively, with11/8>4/3.
   This genuinely shows that a fixed-window optimum over all k<=K need not be found at the largest admissible k.
   F2 below requires the example's s=1 specialization to be stated.

<a id="finding-integer-normalizer-type"></a>

## F1: Exact bounded-normalizer formula needs an integer K

**Trigger and evidence.**
Section3 concludes that arbitrary degree with k<=K has exact restricted infimum1+1/K, but K has no explicit integer type in the frozen revision.
If K is permitted to be real, take K=3/2: the only admissible positive integer normalizer is k=1, whose exact all-degree value is2, whereas1+1/K=5/3.
The earlier Section2 lower bound1+1/K remains valid for real K; the claimed equality does not.

**Impact and correction.**
This is a literal parameter-domain omission, not a defect in the integer balancing argument.
State K is a positive integer in the bounded-normalizer statements, or replace the exact formula by1+1/floor K for real K>=1.
New finding in this first independent review; no old accepted result is challenged.

<a id="finding-handcheck-specialization"></a>

## F2: The explicit hand-check needs the specialization s=1

**Trigger and evidence.**
Under Section3's preceding arbitrary s>=1, the hand-check writes Q=4+2t+t^2 and product4-2t-t^2-t^3, energy22.
This uses P=1-t.
For s=2 the actual product is4+2t-3t^2-2t^3-t^4 and its energy is34, so the displayed product and energy are false under that unspecialized reading.

**Impact and correction.**
State s=1 for the hand-check, or use Q=4+2t^s+t^(2s) and product4-2t^s-t^(2s)-t^(3s) for arbitrary s.
The preceding exact formulas and the intended nonmonotonic example are valid.
New scope/typing finding, not a failure of the main cyclotomic theorem.

<a id="whole-proof-finding"></a>

## Whole-proof finding and source limits

**Initial outcome: changes required only for F1--F2's literal parameter scopes.**
The complete substantive derivations pass independent inspection at the intended positive-integer K and stated s=1 hand-check scope.
No further mathematical gap or hidden Lehmer assumption was found.
The exact representation is an infimum of upper trial values, and the draft consistently refrains from turning its finite arithmetic floors into a lower Mahler gap.
Its unrestricted integer-normalizer infimum remains unattained for nonmonomial P, while bounded-normalizer minima and the individual fixed-window cyclotomic optimum are attained; these are different statements and were checked separately.

Source completeness is bounded: Jensen/Mahler and finite prediction are recognized classical interfaces, and their local source/normalization records were checked.
The proof itself does not depend on an uninspected stronger Szego approximation theorem.
Historical attribution for the exact all-degree integer-normalizer formulation has not been established, exactly as disclosed in the draft; this finding makes no novelty certification.
No code, solver, parameter scan, numerical root test, formal proof or original external-source re-audit was performed for this review.
The two displayed small arithmetic counterexamples were calculated directly in the review.

The root author has been notified of F1--F2.
The frozen draft was not edited by the reviewer.
A targeted reread of the actual corrected revision is needed to close these two findings before calling the complete literal account passed.

## Historical relationship clarification

The retained account does not establish the complete actual initial mathematical context and exposure order needed for an independent relationship.
Availability of the author self-check and a shared conversation does not establish the missing details, and the scope requests themselves are not treated as proof contributions.
The relationship is therefore unknown, without changing the recorded mathematical outcomes, original findings or closure scope, dates, source limits, or exact original-input bindings.
