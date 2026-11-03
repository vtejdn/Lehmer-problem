---
author: Yin
---

# Exact integer multiplier variation and jointly priced normalizer-window minima

This retains the complete necessary mathematical argument from [the original repaired integer multiplier proof](../ledger/Yin_L_G0359_v1.md#integer-multiplier-variational-formula).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

The preceding registered v1 summary left the epsilon domain conditional.
This version explicitly states epsilon>0 and m(P)=log M(P), with the complete original proof unchanged; v1 was never adopted and remains open.

## Statement

Let P be any nonzero integer polynomial, with Laurent inputs reduced by a monomial, and let O_k be exactly the integer polynomials Q with positive integer Q(0)=k and no zeros on the closed unit disk.
Using the complete coefficient Euclidean norm, M(P)^2 is precisely inf_(k>=1) inf_(Q in O_k) ||PQ||_2^2/k^2.
Every displayed trial is an upper estimate; reflection, rational zero-free approximation and fixed-input dominated convergence prove equality even with circle roots, without a uniform approximation degree, denominator or rate.
For a nonmonomial P no finite Q attains that unrestricted infimum, including when the larger bounded-weight class has an attained minimum.
At every fixed positive integer k, ||PQ||_2^2>=k^2+1 and the nonempty energy set has a minimum; for every positive integer K the restriction 1<=k<=K also has an attained minimum at least 1+1/K^2.
For every epsilon>0, any trial satisfying one-half log(||PQ||_2^2/k^2)<=m(P)+epsilon, with m(P)=log M(P), necessarily pays k>=[exp(2(m(P)+epsilon))-1]^(-1/2).
Here m(P)>=0 and epsilon>0 make the displayed denominator positive; this is not a denominator upper bound or a Mahler gap.
For every positive integer s,k and integer n>=0, N=n+1 and k=Na+b with integers a>=0 and 0<=b<N, the exact minimum over all integer Q(0)=k of degree at most sn is k^2+Na^2+(2a+1)b.
The residue-chain proof and explicit decreasing-coefficient construction attain it within O_k itself, with full closed-disk zero-freeness, including n=0 and k<N.
The added energy is k^2/N+b(N-b)/N and the ratio is at least 1+max(1/N,1/k).
For N>=k it is exactly 1+1/k; with arbitrary degree and 1<=k<=K for a positive integer K it is exactly 1+1/K.
The s=1,N=3,k=3 and k=4 hand-checks prove that a fixed-window ratio need not decrease with k.
The original K-integrality and s-specialization scope findings remain recorded; none of these finite arithmetic floors yields a uniform lower Mahler gap or a novelty claim.

## Current assessment
[Selected decision](#decision-unsupported-summary-domains)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:39 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact scalar functional and bounded-weight class](../ledger/Yin_L_G0431_v1.md#single-haar-formulation) | Only the defining functional and admissibility of the scalar multiple of the squared absolute multiplier; the complete multiplier infimum and its zero-free approximation are proved here, without importing a stronger quantitative prediction theorem. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:41 |
| status | proved |
| reason | Adopt the complete necessary retained proof through its actual whole self-check, preserving the exact parameter types, all original negative/repair/reread history, source depth, degree/normalizer/common-period costs and noncompletion boundaries. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](../ledger/Yin_L_G0431_v1.md#single-haar-formulation) | Only the defining functional and admissibility of the scalar multiple of the squared absolute multiplier; the complete multiplier infimum and its zero-free approximation are proved here, without importing a stronger quantitative prediction theorem. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0587_v1.md#integer-multiplier-whole-current-finding) | Entire current exact statement and full retained mathematical argument, all direct interfaces and original useful limits; actual SELF with no new independent claim. |


### Decision unsupported-summary-domains

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:00 |
| status | open |
| reason | Withdraw the current proved selection because the new summary does not explicitly restrict the exact energy minimum to P=1-t^s or its fixed-k floor to nonmonomial P. The original full proof is unchanged; retain the exact finite controls and the initial self-check miss. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](../ledger/Yin_L_G0431_v1.md#single-haar-formulation) | Only the defining functional and admissibility of the scalar multiple of the squared absolute multiplier; the complete multiplier infimum and its zero-free approximation are proved here, without importing a stronger quantitative prediction theorem. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0587_v1.md#new-multiplier-summary-domain-failure) | Only the exact unsupported summary domains and product specification; the full original proof is retained with its original hypotheses. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

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
