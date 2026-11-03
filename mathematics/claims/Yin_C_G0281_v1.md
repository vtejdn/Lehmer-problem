---
author: Yin
---

# Absolute norm-grid binary support bounds and effective height-one costs

This retains the entire original2026-10-07 [L91 argument](../ledger/Yin_L_G0091_v1.md).
Every hypothesis, complete derivation, exact cost and source/probability/uniformity boundary is retained.
No source or computation is newly executed and no Task is resumed.

## Statement

Let alpha be a nonzero algebraic integer with monic irreducible minimal polynomial P of degree d>=1 and m=log M(P)>=0.
For n>=1 let T_n={sum_(j<n)epsilon_j alpha^j:epsilon_j in{0,1}}.
No unit or all-power degree hypothesis is imposed.
The complete real/complex norm-cell argument gives the absolute bound

    |T_n|<=(4n)^d M(P)^(n-1),

without an unspecified input constant, maximal-order assumption, discriminant or covolume cost.

If m<log2, put delta=log2-m>0 and
N=ceil[(2d/delta)log(8d/delta)].
Then two distinct length-N binary words coincide.
Trimming zero-end coefficients and choosing the leading sign gives a monic Q in{-1,0,1}[t] with nonzero constant coefficient and

    P divides Q, d<=deg Q<=N-1, support(Q)<=N.

Its integral multiplier C=Q/P is monic; if P is a unit polynomial then C has constant coefficient+/-1.
Exactly,

    0<=m(C)<=log(support(Q))/2-m<=log N/2-m.

For every fixed m0<log2, N=O_(m0)(d log(d+1)) uniformly for m<=m0.
The least binary collision length satisfies d+1<=N_first<=N.
This supplies no O(d) bound, bounded support, zero overhead or multiplier cost proportional to m.
The existing degree-stable sparse neutral-completion delay is compatible and does not refute an O(d) bound.

For integers1<=k<=n, an exact constant-weight sufficient condition is

    binomial(n,k)>(5k)^d M(P)^(n-1).

Then two k-one binary words collide and their nonzero height-one difference R has
P dividing R,deg R<n,support(R)<=2k,R(1)=0.
For noncyclotomic P its multiplier contains t-1, with no condition on other factors.
Trimming a power of t and changing sign preserve these properties.
The elementary condition klog(n/k)>dlog(5k)+(n-1)m is sufficient as well.
These tests are not necessary characterizations and, at fixed m>0,k, arbitrarily increasing n cannot make this inequality produce a fixed-support annihilator.
The exact binomial test can use positive support density but gives no bounded absolute support or neutral completion theorem.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:13 |
| status | open |
| reason | Register the complete original mathematical conclusions and exact existing inputs; actual current whole review and adoption follow separately. No unsupported uniform gap or inherited independent review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire nonzero algebraic-integer domain, absolute real/complex norm grid and all n, exact first-collision ceiling/monic/unit/multiplier costs, full sparse constant-weight certificate and every delay/support/overhead limitation. |
| argument | [Entire original proof](#argument) | Complete original strict half-open norm-cell injection and real/complex counts, exact cutoff monotonicity/rounding, trimmed monic division and Parseval/Jensen overhead, sparse grid/binomial/neutral-factor arguments and finite-test boundaries. |
| support | [Complete earlier height-one boundary](Yin_C_G0221_v1.md#binary-relations-boundary) | Existing eventual binary collision and its uncontrolled multiplier limit; the new absolute constant and effective cutoff are completely proved here. |
| support | [Controlled-completion criterion](Yin_C_G0221_v1.md#controlled-entropy-completion) | Only the distinction from bounded support with multiplier entropy controlled relative to m; the logarithmic overhead here does not meet that hypothesis. |
| support | [Actual degree-stable delay](Yin_C_G0222_v1.md#no-uniform-finite-time-rate) | Existing complete all-power-degree-stable six-term neutral Salem delay, with its ineffective construction threshold and positive fixed-limit boundary; no O(d) counterexample is inferred. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:21 |
| status | proved |
| reason | Adopt the complete original absolute norm-grid theorem, effective first-collision ceiling, exact monic/unit multiplier cost and sparse binomial test after actual whole self-review. All nonunit, complex multiplicity, strict-cell, support/degree/entropy-overhead and delay boundaries remain; no neutral completion or common gap is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire nonzero algebraic-integer domain, absolute real/complex norm grid and all n, exact first-collision ceiling/monic/unit/multiplier costs, full sparse constant-weight certificate and every delay/support/overhead limitation. |
| argument | [Argument](#argument) | Complete original strict half-open norm-cell injection and real/complex counts, exact cutoff monotonicity/rounding, trimmed monic division and Parseval/Jensen overhead, sparse grid/binomial/neutral-factor arguments and finite-test boundaries. |
| support | [Support](Yin_C_G0221_v1.md#binary-relations-boundary) | Existing eventual binary collision and its uncontrolled multiplier limit; the new absolute constant and effective cutoff are completely proved here. |
| support | [Support](Yin_C_G0221_v1.md#controlled-entropy-completion) | Only the distinction from bounded support with multiplier entropy controlled relative to m; the logarithmic overhead here does not meet that hypothesis. |
| support | [Support](Yin_C_G0222_v1.md#no-uniform-finite-time-rate) | Existing complete all-power-degree-stable six-term neutral Salem delay, with its ineffective construction threshold and positive fixed-limit boundary; no O(d) counterexample is inferred. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0535_v1.md#current-effective-height-one-finding) | Entire exact current statement, complete retained original argument and every selected interface, self-reviewed; old findings retain their actual fixed inputs and relationship scopes. |

## Complete retained argument

<a id="argument"></a>

Let alpha be a nonzero algebraic integer with monic minimal polynomial P of degree d.
Write m=log M(P), and let

    T_n={sum_(j=0)^(n-1) epsilon_j alpha^j: epsilon_j in {0,1}}.

The proof applies without an all-power degree-preservation hypothesis and without assuming alpha is a unit.
In the intended unit core, every resulting monic multiple can additionally be stripped of its zero root to be a monic unit polynomial.

<a id="norm-grid-support-bound"></a>
### 1. A support bound with no unspecified input constant

In the Minkowski coordinates R^r x C^s of K=Q(alpha), use intervals of length 1 on each real coordinate and intervals of length 1/sqrt(2) on both Cartesian coordinates of each complex place.
If distinct algebraic integers x,y lie in the same product cell, every real conjugate of x-y has modulus less than 1 and every complex conjugate has modulus less than 1.
This contradicts the nonzero integer norm having absolute value at least 1.
Hence each cell contains at most one algebraic integer.

Center the embedded binary sums at half the sum of their n orbit vectors.
At a place with |sigma(alpha)|=rho the centered points have modulus at most

    R=(n/2) max(1,rho)^(n-1).

A real interval of radius R meets at most 2R+2 cells.
A complex disc of radius R is contained in a square meeting at most (2 sqrt(2) R+2)^2 cells.
Since n max(1,rho)^(n-1)>=1, these counts are at most 3n max(1,rho)^(n-1) and [4n max(1,rho)^(n-1)]^2 respectively.
Multiplying over the r real and s complex places gives

    |T_n| <= (4n)^d M(P)^(n-1).                         (1)

The embedding cell count does not assume the monogenic order is the maximal order, and no discriminant or covolume estimate is hidden in its constant.

<a id="effective-first-height-one-relation"></a>
### 2. An explicit first-collision cutoff

Assume m<log 2, put delta=log 2-m, and define

    N=ceil[(2d/delta) log(8d/delta)].                    (2)

Then two distinct length-N binary words coincide.
Indeed, for the positive real number x=(2d/delta) log(8d/delta), put u=8d/delta>1.
We have

    x delta=2d log u > d log(u log u)=d log(4x),

because log u<u.
The function y delta-d log(4y) is increasing for y>=x, since x>d/delta.
Thus N delta>d log(4N), and (1) gives |T_N|<2^N.

Subtracting the two words, removing any zero coefficients at the two ends, and changing the overall sign produces a monic polynomial Q with coefficients in {-1,0,1}, nonzero constant coefficient, and

    P | Q,       d <= deg Q <= N-1,
    number of nonzero coefficients of Q <= N.          (3)

Polynomial division by the monic P gives Q=P C with C integral and monic.
If P is a unit polynomial, then C also has constant coefficient +/-1.
Parseval and Jensen give the explicit overhead bound

    0 <= m(C)=m(Q)-m(P)
       <= (1/2) log(number of nonzero coefficients of Q)-m
       <= (1/2) log N-m.                               (4)

For every fixed m0<log 2, (2) is O_(m0)(d log(d+1)) uniformly for m<=m0.
The construction does not give O(d), bounded support, or an overhead proportional to m.
In particular, (4) is not the hypothesis required in L G0019.

If N_first denotes the least binary collision length, irreducibility gives N_first>=d+1; (2) supplies an explicit upper bound.
The known L G0020 delay family already forces the lower endpoint to grow with d even under all-power preservation and sparse neutral completion.
That family does not disprove an O(d) upper bound.
No such upper bound or counterexample is asserted here.

<a id="degree-support-tradeoff"></a>
### 3. A finite degree-versus-support test

There is also a sparse version of the same packing argument.
Fix integers 1<=k<=n and restrict to binary words of exactly k ones.
Their embedded sums lie in discs or intervals of radius k max(1,rho)^(n-1), without centering.
The real cell count is at most 4k max(1,rho)^(n-1), and the complex count at most [5k max(1,rho)^(n-1)]^2.
Consequently, if

    binomial(n,k) > (5k)^d M(P)^(n-1),                 (5)

two such words coincide.
Their difference R is a height-one multiple of P with

    deg R<n,       support(R)<=2k,       R(1)=0.        (6)

For noncyclotomic P, the last identity means that the multiplier contains the neutral factor t-1.
It says nothing about its other factors.
Removing a power of t or changing sign preserves all statements in (6).

Condition (5) is an explicit sufficient test, not a necessary characterization of sparse multiples.
For example, the elementary estimate binomial(n,k)>=(n/k)^k shows that

    k log(n/k) > d log(5k)+(n-1)m                      (7)

suffices.
The factorial estimate follows by multiplying (n-i)/(k-i)>=n/k for 0<=i<k.
At fixed positive m and fixed k the left side grows only logarithmically in n while the right side grows linearly; simply allowing ever longer delays cannot make this test produce a fixed-support annihilator.
This identifies the actual cost of this counting route, without asserting nonexistence of such an annihilator.

One may instead take k proportional to n: the finite exact inequality (5), rather than an asymptotic approximation to the binomial coefficient, is the stated certificate.
Low entropy can make the required support density small, but this does not keep the absolute support bounded as degree and observation length escape.
