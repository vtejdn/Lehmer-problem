---
author: Yin
---

# Coefficient-scale lower bounds for the true positive-log remainder

Date:2026-10-11T15:19.
Root coordinating AI for Yin fixes the complete restricted author account below under the continuing G0001 weekly authorization, after separately organized complete review in [the responsible R](../audits/reviews/Yin_R_G0208_v1.md#coefficient-scale-tail-whole-finding).
Adopt exactly its stated hypotheses, original costs, failures and source/review limits.
No unrestricted Mahler gap, canonical Claim or Task completion is asserted.

<a id="coupled-method-fixed-scope"></a>
## Fixed scope and preservation

The entire author account follows, with only title depth, navigation and final blank-line normalization.
Allocation-era pending-review statements remain history; the linked fixed R supplies the actual completed review scope.
Proposed or unrun computations remain unrun.
No new allowance, input-uniform conditioning or actual unit/covariance realization is inferred.
Further mathematics uses a distinct draft.

The current complete true-tail/coefficient-scale accuracy theorem is retained in [C446](../claims/Yin_C_G0446_v1.md#complete-positive-log-coefficient-tail-cost), adopted after [R650 whole self-review](../audits/reviews/Yin_R_G0650_v1.md#current-coefficient-tail-whole-finding).
The full original account below preserves its day-precision author freeze,23:16 R208 report,23:19 retention, exact source/no-run boundaries and distinction between accurate uncorrected truncation and a positive corrected lower certificate.
No current Task/E or original Lehmer computation resumes.

## Complete retained account


## Coefficient-scale obstruction to accurate positive-log truncation

Date:2026-10-11.
Root AI for Yin under continuing G0001 authority.
This draft concerns the exact estimator in [L378](Yin_L_G0378_v1.md#positive-log-moment-identity) and its fast evaluation in [L379](Yin_L_G0379_v1.md#fast-positive-moment-arithmetic-cost), not a new Mahler gap.
The reuse screen found their complete positive-tail identity, but neither fixes a lower bound on the TRUE omitted tail in terms of the original coefficient scale and total measure.
The derivation below is a direct supporting-line calculation for that exact scalar remainder; no external asymptotic or source theorem is needed.
Known sparse-gap inputs DS17 and L19 already force support escape under hypothetical near-one sequences, and are only used at their accepted exact scope.
No program is proposed.

## Responsible input and question

Let P be a nonzero integer polynomial, H=sum|a_j| and M=exp(m(P)).
Keep original P, all factors and multiplicities.
L378 fixes

    nu_n=integral (1-|P|^2/H^2)^n dmu,
    T_N=log H-(1/2)sum_(n=1)^N nu_n/n,
    T_N-m(P)=(1/2)sum_(n>N)nu_n/n>=0.                 (1)

Its proof applies even when P is not squarefree; squarefreeness is needed only for its particular upper-tail geometry.
L379 speeds up finite evaluation but does not change the true remainder in(1).
Determine a necessary scale for approximating m(P) by T_N to fixed absolute accuracy.
This is not the question whether ANY lower certificate can be positive after a sharp cancellation against a large upper-tail bound.

<a id="geometric-mean-positive-tail-lower-bound"></a>
## 1. Exact lower bound from the original geometric mean

For0<x<=1 define

    r_N(x)=(1/2)sum_(n>N)(1-x)^n/n,
    x_P=M^2/H^2 in(0,1].                              (2)

For every N>=1,

    T_N-m(P)>=r_N(x_P).                               (3)

Proof.
The original random variable X=|P(e^(i theta))|^2/H^2 belongs to[0,1] and is positive almost everywhere.
Y=log X is integrable with integral Y=2m(P)-2log H=log x_P.
The geometric-series remainder differentiates on0<x<1 to r_N'(x)=-(1-x)^N/(2x).
Hence g_N(y)=r_N(e^y), y<=0, satisfies

    g_N'(y)=-(1-e^y)^N/2,
    g_N''(y)=N e^y(1-e^y)^(N-1)/2>=0.                (4)

The bounded first derivative also proves that g_N(Y) is integrable.
Its tangent at the finite mean log x_P lies below its graph; integrate that supporting-line inequality.
Nonnegative termwise integration in(1) identifies integral g_N(Y) with T_N-m(P), giving(3).
End value x_P=1 gives zero and needs no derivative formula at minus infinity.
No interchange of an uncontrolled signed series is made.
For a monomial M=H and every nu_n=0, so equality holds trivially.
For a nonmonomial the modulus is nonconstant and x_P<1; strictness is not needed below.

This lower bound uses the geometric mean of the ORIGINAL modulus.
Substituting coefficient energy or a selected conjugate for M would be a different estimate and is not done.

<a id="necessary-quadratic-coefficient-scale"></a>
## 2. Explicit accuracy cost and quantifiers

Summing only n=N+1,...,2N in(2) yields

    r_N(x)>=(1/4)(1-x)^(2N).                          (5)

Consequently, for0<delta<1/4 and a nonmonomial P, the accuracy premise T_N-m(P)<=delta implies

    N>=log(1/(4delta))/[-2log(1-x_P)]
      >=(1/2)(H^2/M^2-1)log(1/(4delta)).              (6)

The last step uses -log(1-x)<=x/(1-x).
Every direction and sign is retained; this is NECESSARY for accuracy, not sufficient.
At fixed upper bound M<=B and fixed delta, useful finite accuracy therefore requires N at least a positive delta-dependent multiple of H^2/B^2 minus a fixed constant.
The recurrence's O(Nd^2) count still pays this growing window; faster evaluation does not remove it.

A complementary bound follows directly from0<=nu_n<=1 and H_N<=1+log N:

    T_N-m(P)>=log(H/M)-H_N/2
             >=(1/2)log(H^2/(e M^2 N)).              (7)

The right side may be negative; it is a valid lower estimate, alongside the nonnegative actual remainder.
In particular bounded M, H^2/N tending to infinity forces the true omitted tail to infinity, not merely an inefficient displayed upper bound.

If the finite window is N<=C d and the same fixed delta accuracy is required, (6) forces H^2<=M^2[1+2Cd/log(1/(4delta))].
Since integer coefficients give H>=k, where k is the number of nonzero coefficients, it also forces k=O(sqrt d) when M is bounded.
This condition does not exclude hypothetical near-one inputs with sufficiently sparse support and does not supply an actual near-one family.

The already accepted [DS17 bounded-support theorem](../audits/literature/DS17/readme.md#bounded-support-gap), as used in [L19](Yin_L_G0019_v1.md), says each fixed k has a positive gap.
Thus a hypothetical sequence with0<m(P)->0 has k->infinity and H->infinity.
Formula(6) adds the necessary coefficient-scale window for this particular positive-log estimator.
It does not strengthen the unrestricted Mahler bound itself, and the original DS17 proof-inspection limits remain unchanged.

<a id="squarefree-integer-padding-control"></a>
## 3. An actual squarefree noncyclotomic growing-cost control

For a prime p>=3 take

    P_p(t)=(t^2-3t+1)(1+t+...+t^(p-1)).

This is a squarefree integer polynomial: the prime cyclotomic factor has simple circle roots and is disjoint from the two distinct positive off-circle quadratic roots.
Its degree is p+1, total M=(3+sqrt5)/2 is fixed, and the COMPLETE coefficient list is

    1,-2, then p-2 entries equal to-1, then-2,1.

Consequently H=p+4.
Every factor and coefficient is retained; the cyclotomic factor contributes zero measure but affects the actual normalized moments.
For N<=C(p+1), (7) gives a true remainder diverging at least as (1/2)log p-O_C(1).
Accuracy by this normalized truncation cannot be degree-linear on this actual family.
It is reducible and has fixed positive measure, so it is neither an irreducible-hard-core obstruction nor a counterexample to Lehmer.
Its role is to separate a genuine estimator cost from a possibly crude tail proof.

Even replacing H by ANY valid scalar upper normalization L>=max_circle|P_p| does not remove this control: |P_p(1)|=p, so L>=p.
The same proof applies with x=M^2/L^2 and T_N normalized by L, and the same divergence follows at linear windows.
No assertion is made that H is optimal on other inputs or that every determinant method uses such a normalization.

## 4. Interpretation, limits and freeze

The local positive-moment exponent in L378 and the exact state recurrence in L379 remain valid.
Their actual finite-accuracy cost must retain coefficient scale, even when simple-zero or critical-level tail constants are ideally evaluated.
The original Lehmer computation planned at H=9,N=4096 is not challenged by this growing-H result; this draft performs no calculation on it.

Most importantly, (3)--(7) are lower bounds on T_N-m(P).
They DO NOT prove that every finite lower certificate at smaller N is nonpositive: a sufficiently accurate upper estimate of a large tail might cancel a large T_N and still leave a useful positive answer.
Such a mechanism would need its own proof.
Nor do they exclude another normalization, rational approximation, direct root method, oscillatory certificate or an algebraically accelerated treatment of the entire tail.
The theorem identifies the precise cost for making the uncorrected positive-log truncation accurate, and a boundary that must be stated in any claimed uniform finite-window strategy.

Author self-check reconstructed the positive infinite-tail identity, log integrability at every finite-multiplicity root, supporting-line convexity and derivative signs, monomial/nonmonomial branches, block lower bound, the reversed negative-log division in(6), all original M/H/k/d quantifiers, fixed-input versus sequence assertions, the complete padding coefficients/squarefreeness/measure/degree and normalized-circle maximum, and the distinction between accuracy and positivity after tail cancellation.
Sections1--4/equations(1)--(7) are frozen for separate whole noncontributor review.
No native computation, new external theorem adoption, source-proof upgrade or unrestricted resolution is asserted.
