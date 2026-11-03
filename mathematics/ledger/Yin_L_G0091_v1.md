---
author: Yin
---

# G0001: an effective height-one relation and its exact costs

Date: 2026-10-07.
This direct argument strengthens the eventual collision in [C221 binary-relation boundary](../claims/Yin_C_G0221_v1.md#binary-relations-boundary) by giving a uniform degree-dependent cutoff.
It does not construct a bounded-support or zero-extra-entropy completion.
The existing [controlled-completion boundary](../claims/Yin_C_G0221_v1.md#controlled-entropy-completion) and [all-power-stable delay family](../claims/Yin_C_G0222_v1.md#no-uniform-finite-time-rate) remain applicable.
No new external source or computation is used, and no novelty is claimed.

Let alpha be a nonzero algebraic integer with monic minimal polynomial P of degree d.
Write m=log M(P), and let

    T_n={sum_(j=0)^(n-1) epsilon_j alpha^j: epsilon_j in {0,1}}.

The proof applies without an all-power degree-preservation hypothesis and without assuming alpha is a unit.
In the intended unit core, every resulting monic multiple can additionally be stripped of its zero root to be a monic unit polynomial.

<a id="norm-grid-support-bound"></a>
## 1. A support bound with no unspecified input constant

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
## 2. An explicit first-collision cutoff

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
## 3. A finite degree-versus-support test

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

## Current proof and retained checking scope

The complete current statement and every original mathematical argument are retained in [C281](../claims/Yin_C_G0281_v1.md#argument), with its actual selected assessment.
The [current whole finding](../audits/reviews/Yin_R_G0535_v1.md#current-effective-height-one-finding) is self-reviewed.
The [complete original checking account and precise findings](../audits/reviews/Yin_R_G0535_v1.md#historical-height-one-author-finding) retain their original2026-10-07 inputs, actual contributions, coverage and limitations.
Original independent or collaborator wording does not establish unrecorded initial context or bind a later C to an old finding.
