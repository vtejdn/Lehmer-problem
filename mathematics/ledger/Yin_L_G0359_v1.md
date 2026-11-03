---
author: Yin
---

# Integer multiplier variation and exact normalizer-window cost

The complete necessary proof is now owned by [the current Claim](../claims/Yin_C_G0380_v3.md#argument).
The fixed original activity and review descriptions below are historical and authorize no present Task/E execution.

Date: 2026-10-11.
Root coordinating AI for Yin fixes this restricted exploration under the renewed G0001 authorization after the separately organized complete review in [the responsible R](../audits/reviews/Yin_R_G0181_v1.md#repaired-whole-account-finding).
The adopted scope is exactly the complete retained author account below, with its hypotheses, costs, failures, source boundaries and review limits.
It supplies no unrestricted Mahler gap and does not complete G0001.

<a id="resumed-batch-fixed-scope"></a>
## Fixed scope and preservation

The entire original author account and subsequent author response/review notices follow, with only navigation relocated.
Allocation-era unrun or pending-review statements are historical and are superseded for the exact inspected scope by the linked fixed review.
For the multiplier account, the initial review's two scope findings and their actual repairs remain visible through R180/R181.
No canonical Claim is registered by this retention.
The Task and all eight routes remain active and unresolved; continued work has a separate draft home.

## Complete retained account


## Integer multiplier weights and the arithmetic cost of single-Haar variation

Date: 2026-10-11.
Human author: Yin; current root AI agent.

## Question and scope

Investigate positive circle weights of the form t*|Q|^2 for integer multiplier polynomials Q, retaining the scalar optimization over t and the full Mahler cost of Q.
The candidate is an arithmetic approximation constraint: integer coefficient energy may discretize the trial values only after an actual denominator/normalizer cost is kept.
Determine an exact variational identity or a sharp obstruction on such trials, without promoting an upper trial value to a Lehmer lower bound.

The original input P is a nonzero integer polynomial, with the noncyclotomic monic-unit hard core used only where its precise hypotheses apply.
All logarithms are natural.
The work must retain unit-circle zeros and unbounded degree; no freeness or bounded inverse is assumed.
The exact scalar identity and regularization baseline are in [scalar weight baseline](Yin_L_G0431_v1.md#single-haar-formulation), and [L4](Yin_L_G0004_v1.md#degree-window-tests) supplies earlier finite Toeplitz boundaries.

No new result, source acceptance, program execution or independent review is asserted by this allocation.
Substantive arguments and useful failures will be developed below before review.

<a id="integer-multiplier-variational-formula"></a>
## 1. An integer multiplier variational representation

Write ||R||_2^2 for the squared Euclidean norm of the complete coefficient vector of a polynomial.
Define
\[
\mathcal O_k=\{Q\in\mathbb Z[t]:Q(0)=k,\quad Q(z)\ne0
\text{ for every }|z|\le1\},\qquad k\ge1.
\]
This is an explicit integer coefficient and zero-location constraint; it contains the constant polynomial k.
For nonzero P in Z[t],
\[
M(P)^2=\inf_{k\ge1}\inf_{Q\in\mathcal O_k}
\frac{\|PQ\|_2^2}{k^2}.                                      \tag{1}
\]
For a Laurent input remove a monomial first.
This does not change either M or the coefficient norm of a product.

The formula is a scalar prediction/weight mechanism with an actual integer normalizer.
It is not claimed novel.
The local reuse check found the classical Toeplitz/residual mechanism and its retained source scope in L4/Den09, and related multiplier inequalities in L9/L94.
It did not identify this exact all-degree integer-normalizer formulation; historical attribution for that formulation is not established.
The proof below is direct and does not import an unreviewed stronger quantitative prediction theorem.

### Lower inequality

For Q in O_k, Jensen's root formula gives M(Q)=Q(0)=k, because Q has no roots in the closed disk.
Parseval and the geometric/arithmetic mean inequality on the circle give
\[
M(P)^2k^2=M(PQ)^2\le\|PQ\|_2^2.
\]
Thus every value in (1) is an upper estimate for M(P)^2.
It is also the scalar-optimized value of the D_G0001 trial weight t|Q|^2: minimizing in t>0 yields log(||PQ||_2^2/k^2) for twice the logarithmic functional.

### Approximation inequality, retaining circle zeros

Factor P over C and reflect its roots through T to obtain a real polynomial O with O(0)=1, no zeros in the open disk, and
\[
|P(z)|=M(P)|O(z)|\quad (|z|=1).
\]
Explicitly an exterior root alpha contributes 1-z/alpha, an interior or circle root contributes 1-conj(alpha)z; conjugate pairs retain real coefficients, and zero roots contribute a monomial of modulus one.
For 0<r<1, O(rz) has no zeros on the closed disk.
Its reciprocal has a uniformly convergent real Taylor series there.

Take a Taylor polynomial and then a rational coefficient approximation with constant term exactly one, close enough uniformly to 1/O(rz) to stay nonzero on the closed disk.
This is possible since that reciprocal has a positive minimum modulus on the compact disk.
Clear a common integer denominator k; the resulting Q belongs to O_k, while Q/k approximates 1/O(rz).
Consequently the infimum in (1) is at most
\[
M(P)^2\int_{\mathbb T}|O(z)/O(rz)|^2\,d\mu.
\]
For each reflected root parameter beta with |beta|<=1,
\[
\frac{|1-\beta z|}{|1-r\beta z|}
\le1+\frac{(1-r)|\beta|}{1-r|\beta|}\le2.
\]
The quotient tends to one away from finitely many circle zeros.
Dominated convergence, with fixed-input bound 4^(deg O), makes the last integral tend to one as r increases to one.
This proves (1), including unit-circle roots.
No uniform degree, denominator or rate estimate is supplied by that dominated-convergence argument.

### Nonattainment in this restricted trial class

If P is not a monomial, (1) is never attained by a finite Q.
Equality in circle geometric/arithmetic mean would force |PQ| constant.
A polynomial of constant modulus on T is a monomial: its highest nonzero autocorrelation between the first and last nonzero coefficients otherwise cannot vanish.
But a nonmonomial P has a nonzero root, so PQ cannot be a monomial.

This is distinct from the full bounded-weight problem.
Even when P has no circle zeros and the full weight minimum is attained, the integer polynomial-square subclass in (1) remains nonattaining.
Do not transfer an attainment criterion across the two trial domains.

<a id="fixed-normalizer-arithmetic-floor"></a>
## 2. Fixed-normalizer arithmetic floor and its actual direction

For an integer nonmonomial P, M(P)>=1.
Strictness in the preceding geometric/arithmetic mean inequality gives
\[
\|PQ\|_2^2>k^2.
\]
The left side is an integer, hence
\[
\frac{\|PQ\|_2^2}{k^2}\ge1+\frac1{k^2}.                       \tag{2}
\]
For an integer K>=1, with 1<=k<=K, the restricted infimum is a minimum: for each k the possible squared energies form a nonempty set of positive integers, and there are only finitely many k.
It is at least 1+1/K^2.

This arithmetic floor holds also for cyclotomic P.
It therefore cannot by itself yield a lower bound for M(P): the unrestricted infimum allows k to grow.
If a trial is within epsilon in logarithmic value,
\[
\tfrac12\log(\|PQ\|_2^2/k^2)\le m(P)+\epsilon,
\]
then (2) forces
\[
k\ge\left(e^{2(m(P)+\epsilon)}-1\right)^{-1/2}.               \tag{3}
\]
Equation (3) is a necessary arithmetic normalizer cost for a near-minimizing trial, not a gap theorem or a denominator upper bound.

<a id="cyclotomic-exact-window-normalizer"></a>
## 3. Exact cyclotomic control: degree and integer normalizer together

Let P=1-t^s, s>=1.
Fix k>=1 and n>=0, and put N=n+1.
For every integer Q with Q(0)=k and degree at most sn,
\[
\|(1-t^s)Q\|_2^2\ge k^2+N a^2+(2a+1)b,\qquad
k=Na+b,\quad 0\le b<N.                                    \tag{4}
\]
Equality is attained by a Q in O_k of degree at most sn.
Thus (4) is the exact minimum even with the zero-free constraint of (1).

To prove the lower bound, split Q into its s residue chains.
Multiplication by 1-t^s acts separately on each chain, so all nonzero residue chains contribute nonnegative energy and cannot reduce the chain starting with k.
On that chain, write coefficients q_0=k,q_1,...,q_n and set q_(n+1)=0.
Its product energy is
\[
k^2+\sum_{i=1}^{N}(q_{i-1}-q_i)^2.
\]
The integer differences d_i=q_(i-1)-q_i sum to k.
A sum of squares with a fixed integer sum is minimized when all d_i differ by at most one: replacing x,y with x-1,y+1 lowers it if x>=y+2.
Hence b differences are a+1 and N-b are a, proving (4).

For attainment, place the larger differences first, take all other residue chains zero and let the coefficients decrease from k by these differences.
They remain nonnegative.
For the resulting polynomial R(z) in z=t^s,
\[
(1-z)R(z)=k-\sum_{i=1}^{N}d_i z^i,\quad
d_i\ge0,\quad \sum_i d_i=k,\quad d_1>0.
\]
If R(z)=0 for |z|<=1 and z!=1, the triangle inequality would force |z|=1 and all positive terms d_i z^i to have phase one.
Since d_1>0, this forces z=1, a contradiction.
Also R(1)>0.
Therefore R, and Q(t)=R(t^s), have no zeros on the closed disk.

The added energy can also be written
\[
N a^2+(2a+1)b=\frac{k^2}{N}+\frac{b(N-b)}{N}.                \tag{5}
\]
The first term is the real-coefficient finite prediction cost; the second is the exact integer rounding price.
In particular every trial here has
\[
\frac{\|(1-t^s)Q\|_2^2}{k^2}
\ge1+\max\{1/N,1/k\}.                                     \tag{6}
\]
The bound by 1/N follows from Cauchy--Schwarz; the bound by 1/k follows from sum d_i^2>=sum |d_i|>=k.
If N>=k, the minimum is exactly 1+1/k and is attained by
\[
Q(t)=k+(k-1)t^s+\cdots+t^{s(k-1)}.
\]
Consequently, allowing arbitrary degree but k<=K for an integer K>=1 gives the exact restricted infimum 1+1/K, while M(1-t^s)^2=1.

For a hand-check at s=1,N=3,k=4, Q=4+2t+t^2 gives product 4-2t-t^2-t^3 with energy22 and ratio22/16.
At s=1,N=3,k=3 the energy is12 and ratio12/9.
Thus the fixed-window ratio need not decrease at every increase of k; choosing only the largest allowed normalizer can miss the optimum.
These are direct arithmetic checks, not an executed parameter scan.

## 4. Consequence, review boundary and next question

The exact representation (1) retains an integer coefficient constraint that generic positive weights hide, but the cyclotomic control shows how its apparent finite arithmetic gap is paid away by normalizer and window growth.
Pure discretization of trial energy, or positivity of every finite sample, is insufficient.
A useful continuation must exploit noncyclotomic arithmetic to relate the normalizer/degree needed for a near-minimizer to another actual cost or lower certificate.

This is a new explicitly scoped synthesis and exact integer-normalizer control within the current G program, not a claim of historical novelty.
Author self-check covered circle-root reflection, rational zero-free approximation, strictness and all-degree versus fixed-window distinction, residue-chain separation, balanced integer differences, the zero-free attaining construction and estimate direction.
Independent review is pending.
No program, new J, numerical optimization, unrestricted gap or F0010 execution is claimed.

### Author response to the first independent review

The separately organized whole-argument review is retained in [R180](../audits/reviews/Yin_R_G0180_v1.md).
Its two required literal-scope repairs are implemented in this unfixed draft: K is explicitly a positive integer wherever the bounded-normalizer minimum is used, and the two written numerical hand-checks explicitly set s=1.
The reviewer found no objection to the intended derivations.
The initial changes-required finding remains fixed; a targeted reread of this repaired revision is pending.
These scope repairs do not assert a new mathematical theorem or Task completion.
