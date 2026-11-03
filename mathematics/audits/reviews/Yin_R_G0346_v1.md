---
author: Yin
---
# Whole review of almost-positive Gram certificates and arithmetic precision

Date: 2026-10-14T20:12.
Human record author Yin.
Root separately reviewed the entire actual C110 v1 author argument, identified the supplemental indefiniteness guard below, obtained the author's confirmation, and checked the actual corrected C110 v2 and its complete difference.
Root assigned the inquiry but supplied none of the new A--D proofs, constants, row-norm argument or quartic sequence.
Root's earlier contributions to accepted C34/C103 are inherited inputs with their own existing reviews, not independently re-certified here.
Shared context and author progress were available; this is not blind review.

The reviewer implemented the explicitly disclosed supplemental domain correction after the author confirmed its intended hypothesis.
That participation is not hidden or described as an untouched proof.
It adds no replacement proof or new mathematical conclusion: the existing eigenvalue-product argument already proves the statement when a negative eigenvalue exists.
The actual v2 primary A--D, all constructions and constants are unchanged.
Separate findings preserve the v1 observation and v2 whole assessment.
The initial shared author-progress context is not specified sufficiently to establish isolation, so the v1 supplemental domain finding has an unknown relationship.
For v2, the reviewer supplied and implemented the necessary negative-eigenvalue hypothesis absent from the original generic tolerance inference; author confirmation of its intention does not make that hypothesis an already explicit original input.
The corrected whole finding is therefore self-reviewed for this supplemental mathematical-domain repair, without attributing the primary A--D proofs or older ancestor contributions to that repair.
The actual complete v2 rereading remains recorded, but independent re-review remains due for the generic characteristic-product separation, its negative-eigenvalue-to-epsilon-floor implication, the PSD exception and affected interfaces, with adequate whole-proof coverage.
Original dates, physical inputs, negative/pass distinction, mathematical checks and binding scopes remain unchanged, with no new review performed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [v1 supplemental domain finding](#almost-positive-v1-negative-eigenvalue-guard) | unknown |
| [v2 actual whole finding](#almost-positive-v2-whole-independent-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [v1 supplemental domain finding](#almost-positive-v1-negative-eigenvalue-guard) | [v1 statement](../../claims/Yin_C_G0110_v1.md#statement) | A--D fully checked and not refuted by the supplemental comparison's missing condition. |
| [v1 supplemental domain finding](#almost-positive-v1-negative-eigenvalue-guard) | [v1 argument](../../claims/Yin_C_G0110_v1.md#argument) | Complete original read; changes required in the last generic spectral-comparison paragraph of Section5. |
| [v2 actual whole finding](#almost-positive-v2-whole-independent-finding) | [v2 statement](../../claims/Yin_C_G0110_v2.md#statement) | Entire A--D, all real/integer/irreducibility/circle-root/width and precision guards. |
| [v2 actual whole finding](#almost-positive-v2-whole-independent-finding) | [v2 complete argument](../../claims/Yin_C_G0110_v2.md#argument) | Every Section2--8/equation1--18, exact controls, source boundaries and explicit supplemental correction. |
| [v2 actual whole finding](#almost-positive-v2-whole-independent-finding) | [C34](../../claims/Yin_C_G0034_v1.md#statement) | Existing rational-affine lag correction, used here without an unproved interior PSD premise. |
| [v2 actual whole finding](#almost-positive-v2-whole-independent-finding) | [C103](../../claims/Yin_C_G0103_v1.md#statement) | Exact original-width rational PSD singleton and explicit actual Salem Gram family. |
| [v2 actual whole finding](#almost-positive-v2-whole-independent-finding) | [C107](../../claims/Yin_C_G0107_v1.md#argument) | Actual coefficient basis and two-place indefinite block method, rechecked at the new parameter. |
| [v2 actual whole finding](#almost-positive-v2-whole-independent-finding) | [F109](../../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp) | Original finite real optimizer and exact same-symbol scalar capacity, at retained source limits. |
| [v2 actual whole finding](#almost-positive-v2-whole-independent-finding) | [F111](../../ledger/Yin_L_F0007_v1.md#matrix-finite-gram-capacity) | Elementary analytic-vector/scalar-Jensen upper bound only; no new matrix factorization theorem invoked. |

## Original observation and actual corrected scope

The v1 supplemental characteristic-polynomial paragraph correctly bounds the magnitude of every NONZERO eigenvalue of a rational matrix with clearing denominator q and norm bound L.
It then infers a lower floor for every supplied epsilon satisfying Q+epsilon I>=0, without explicitly requiring Q to have a negative eigenvalue.
That inference fails for PSD Q: for instance the ordinary rational coefficient Gram aa^T permits every positive epsilon, arbitrarily small, despite having a nonzero eigenvalue.
This objection does not affect A--D or the row-resultant bound.

The actual v2 adds the negative-eigenvalue hypothesis and the PSD exception only in that paragraph, plus the correction/assessment account.
The reviewer checked this complete difference against v1 and re-evaluated the entire proof chain at the actual v2 scope.
With a negative eigenvalue, epsilon is at least its absolute value; the eigenvalue-product argument supplies the stated bound.
The primary certificate, root-norm theorem and quartic example retain their exact arguments.
The original v1 is preserved.

## Sublevel estimate and the true lower certificate

For a circle point z0 in a radius-r disk, every other point of its circle intersection is at chord distance at most2r from z0.
For0<r<1 this confines the intersection to an arc of measure at most2arcsin(r)/pi<=r; the endpoints r0 and r>=1 are handled separately.
Factoring a monic degree-d polynomial and taking a union over all d factors gives the sublevel estimate even with repeated roots or circle roots.
No coefficient-height or root-separation assumption is needed.

The nonnegative level-set formula for log(1+tau/|p|^2) is valid with pointwise infinities at finitely many circle zeros.
With a=1/(2d), the interval(0,1] contributes at most1/(1-a)<=2 and the remaining interval at most2/a=4d.
This gives exactly E_p(tau)<=6d^2 tau^(1/(2d)); d1 is included.
For tau0 the error is zero.

For B=Q+epsilon I the symbol increases by N epsilon, not epsilon.
A finite PSD factor gives a vector polynomial F; projection onto its nonzero constant vector gives a scalar analytic g with g(0)=sqrt(B00) and |g|<=||F||.
The root/Jensen inequality therefore bounds log B00 by the integral of the regularized symbol.
Combining with the sublevel error proves A with coefficient3d^2.
Condition B bounds that subtraction by one quarter of log(1+gamma), while the positive term is at least one half.
This establishes a lower certificate for the ORIGINAL p, not a raw signed-Gram objective.
All lag equations and the operator-order tolerance remain exact hypotheses.

## Exact rational affine correction

Rounding independent entries of the real optimizer to multiples of1/q symmetrically introduces at most1/(2q) error.
Each lag residual is a q-grid number of size at most N/(2q), because the original autocorrelations are integers.
C34's one-entry-per-lag right inverse restores every lag, including padded zeros.
The maximum entry error is at most(N+1)/(2q), yielding operator error N(N+1)/(2q) and the claimed PSD tolerance.
The00 correction cancels its own rounding error, leaving exactly the sum of the other N-1 diagonal errors and the sharper objective bound.

The real optimizer is the actual F109 optimizer; its entries are not asserted computable in polynomial time or supplied by a coefficient-only formula.
At an irreducible circle-root unit input, any rational gain violates C103's exact PSD ceiling and is therefore indefinite.
This proves existence of arbitrarily small negative tolerance with per-input gain, while retaining the q and degree costs.
It does not assert a denominator-free PSD repair.

## All-root arithmetic precision and both guards

The exact zero lag gives trace Q=H.
An eigenvalue lower bound-epsilon makes every positive eigenvalue at most H+(N-1)epsilon and bounds ||Q|| by L=H+N epsilon.
At a circle root, the exact zero symbol and ||v||^2=N give v^*(Q+epsilon I)v=N epsilon.
The finite PSD spectral inequality ||Bv||^2<=||B||v^*Bv and subtraction of epsilon v prove equation7 with its full factor sqrt N.

A row polynomial of qQ not divisible by monic irreducible p has a nonzero integer norm over ALL d original conjugates.
Each of the c circle factors gets the small row bound.
The remaining factors are at most qL sqrt N times max(1,|alpha|)^n.
Their complete product contributes exp(nm(p)), giving D exactly.
If epsilon<=1/N, the displayed bracket is at most2sqrt(H+2)sqrt(epsilon) and L<=H+1.
Taking the2/c power yields E with q^(2d/c), N^(d/c), every H factor and the original nm/c exponent.
No selected norm or smaller field is substituted.

At n=d, if all row polynomials are divisible by p they are scalar multiples of its coefficient vector.
Symmetry makes Q a scalar multiple of aa^T, and the exact symbol fixes that scalar to1.
Thus gain forces a nondivisible row.
At n=d+1, (1+theta)aa^T-theta(Sa)(Sa)^T has the SAME symbol, gain, inertia(1,1) and every row divisible by p; the original-width guard is essential.
The separate diagonal perturbation aa^T+theta E00-theta E11 has inertia(2,1) because a,e0,e1 are independent at d>=2.
These controls distinguish negative rank from error size and do not invalidate the conditional arithmetic floor.

For the supplemental generic comparison, the rank-r nonzero eigenvalue product of qQ is a nonzero integral characteristic coefficient.
Bounding the other r-1 eigenvalues gives the stated q^r L^(r-1) separation.
Since qL>=1, replacing r by N weakens it correctly.
Only an ACTUALLY negative eigenvalue then bounds epsilon below; v2 now states that condition.

## Quartic construction, exact denominator and spectrum

Reduction of the polynomial Gram Gamma(x) modulo monic T=x^2-x-3 gives integer A,B.
Its two actual trace roots yield identical lag data, so lag B=0, lag A is the original symbol and R(x)00=4-x, with B00=-1.
This is an exact algebraic construction, not an unreported symbolic run.

The identity649^2-13*180^2=1, the two recurrences, odd/even parities and coprimality give every stated Pell-power fact directly.
For x_k=(1+P_k/Q_k)/2, the rational error is exactly2/[q_k^2(P_k/Q_k+sqrt13)], with q_k=2Q_k.
The objective numerator7Q_k-P_k is odd and coprime to Q_k, so its reduced denominator is q_k; all other entries have denominator dividing q_k.
This proves the LEAST common denominator assertion, not merely a convenient clearing denominator.

For t_+<x<3, interpolation has alpha>0 and beta<0.
The actual coefficient basis U is invertible.
The block alpha B_+ is positive definite and beta B_- has signs+,-.
Completing its invertible blocks gives the scalar2(3-x)/3>0, so inertia is exactly(4,1).
At the vector U^(-T)(0,0,0,1,1), the first endpoint has zero quadratic value and the second has2delta_-^2.
Its Rayleigh quotient gives the lower linear-in-(x-t_+) negative magnitude.
PSD of the first endpoint and the perturbation norm give the upper bound.
Combining with the exact rational error proves both positive constants in F, bounded matrix norm and q^-2 decay.

The same real endpoint is at distance at most c_+/q_k^2.
C103's original-width rational PSD set is the singleton aa^T, so the objective difference proves distance greater than1/2 from that different feasible set.
The explicit integer C_B bounds the operator norm and gives a rational certified tolerance C_B/q_k^2.
Taking sufficiently large k satisfies B for d4,N5,gamma1/2 and yields the stated paid per-input lower bound.
No k was numerically computed, no varying near-one family is constructed, and no contradiction with the earlier signed-trace example is asserted.

## Source and review limits

The five direct dependencies were checked at their exact invoked interfaces.
Older C34/C103 contributions retain their selected mathematical acceptance; this review concerns the new actual C110 proof and its uses.
F109's external attribution limits remain, and only F111's elementary vector-Jensen mechanism is needed, not its imported matrix factorization theorem.
The known rational projection is credited and its new error bounds checked locally.

Root directly read Keith Conrad's primary13-page online Pell's Equation, I at the p2 table entry for13 and p5 Theorem4.1/Corollary4.2 and their proofs: https://kconrad.math.uconn.edu/blurbs/ugradnumthy/pelleqn1.pdf.
This independently supports the author's method attribution.
No fundamental-unit or general solvability theorem is used; all actual recurrences and costs are proved locally.
No source download, whole-note audit, numerical program, formal proof or novelty claim occurred in this review.

<a id="almost-positive-v1-negative-eigenvalue-guard"></a>

## v1 finding: supplemental domain correction required

CHANGES REQUIRED for the generic tolerance-floor inference without an actually negative eigenvalue.
A PSD coefficient Gram and arbitrarily small positive epsilon give the explicit counterexample.
Whole inspection supports the primary A--D arguments; the supplemental omission does not refute them.
This finding remains attached to physical v1.

<a id="almost-positive-v2-whole-independent-finding"></a>

## Actual v2 whole finding: pass

PASS for the ENTIRE actual corrected C110 v2 A--D, all proofs/controls and declared inputs, with the disclosed reviewer-identified and author-confirmed supplemental guard.
All new primary reasoning was directly reconstructed; the corrected whole relationship and independent re-review obligation are disclosed above.
The result gives paid per-input certificates and precision obstructions, not uniformly available objective gain, free denominators or a solution of G0001.
Root's explicit Claim decision owns adoption.
