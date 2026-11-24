---
author: Yin
---

# The cost of a repeated unit factor with extra row coefficients

2026-11-24T17:36 UTC.
A research agent working for Yin derived the following width estimate for the [ordinary two-row coefficient test](../claims/Yin_C_G0345_v408.md#statement) in the [Lehmer task](../tasks/Yin_T_G0001_v1.md#contract).
The calculation examines whether the high cost at the degree of a fixed seed persists when the rows have additional coefficients.

<a id="width"></a>
## An upper bound at each fixed width

Fix a monic reciprocal irreducible polynomial \(P\) of a nontorsion unit \(\alpha\), write \(e=\deg P\) and \(h=m(P)>0\), and fix an integer \(B\ge e\).
For each odd prime \(p\), let \(H_p(P;B)\) be the least \(\max(\|U\|_1,\|V\|_1)\) over nonzero \(U,V\in\mathbb Z[Y]\) of degrees at most \(B\) such that they are coprime over \(\mathbb Q[Y]\),
\[
 P^2\mid U(X^p)+XV(X^p),\qquad UU^\iota-VV^\iota\ne0,\qquad \iota(Y)=Y^{-1}.
\]
Here the coefficient one-norm is the sum of the absolute values, and minimization precedes the height cutoff in the finite test.
Such pairs exist at every sufficiently large prime and, with \(r=B+1-e\),
\[
 h\ \le\ \liminf_p\frac{\log H_p(P;B)}p
 \ \le\ \limsup_p\frac{\log H_p(P;B)}p
 \ \le\ \left(1+\frac{2(e-1)}r\right)h .                         \tag{1}
\]
All prime limits in (1) fix \(P,B\).
The lower bound is the [reflected elimination estimate](../claims/Yin_C_G0345_v408.md#lower).
The [two-jet construction at increasing width](../ledger/Yin_L_G0462_v231.md#separation) gives asymptotic rate \(h\) as the row width tends to infinity.
The estimate here specifies a relative-width cost at each fixed seed, including widths between \(e\) and \(2e\), and keeps nonzero reflected determinant at offset one.

<a id="bad"></a>
## Two obstructions to extracting the rows

Work in the rational vector space of pairs of degree at most \(B\) whose graph \(G=U(X^p)+XV(X^p)\) is divisible by \(P^2\).
Take \(p\) sufficiently large that \(\bar P\) is squarefree in characteristic \(p\) and the conjugates of \(z=\alpha^p\) are distinct.
The second condition follows because among finitely many ratios of distinct conjugates of \(\alpha\), only roots of unity of order \(p\) could cause a collision.
Write \(Q\) for the monic minimum of \(z\), so \(\deg Q=e\) and \(m(Q)=ph\).

First, any rational linear subspace on which \(UU^\iota-VV^\iota\) vanishes identically has dimension at most \(r\).
Intersect it with the full coefficient lattice.
The resulting lattice is saturated, so its reduction modulo \(p\) has dimension equal to its rational rank.
For every integral pair in the subspace, monicity preserves graph divisibility on reduction, and differentiation gives \(\bar P\mid \bar V(X^p)\) since the reduced graph has derivative \(\bar V(X^p)\).
Squarefreeness and \(\bar V(X^p)=\bar V(X)^p\) imply \(\bar P\mid\bar V\), and the graph value gives \(\bar P\mid\bar U\) in the same way.
Thus the reduced first row lies among multiples of \(\bar P\) of degree at most \(B\), a space of dimension \(r\).
Projection to that row is injective on the reduced subspace.
Indeed, if it vanishes, the reduced identity \(\bar V\bar V^\iota=\bar U\bar U^\iota\) forces \(\bar V=0\) in the Laurent polynomial domain.

Second, the rational subspace on which \(U(z)=V(z)=0\) has dimension at most \(d_0=2r-\min(r,e)\).
Writing \(U=QU_1,V=QV_1\) leaves \(r\) coefficients per row and requires \(U_1(z)+\alpha V_1(z)=0\), since \(Q(X^p)\) has only a simple zero at \(\alpha\).
This value map has rank at least \(\min(r,e)\), already on the coefficients of \(U_1\) alone.

For every nonzero integral graph in the two-jet space, the [fixed-seed contraction estimate](../ledger/Yin_L_G0462_v231.md#jets) at multiplicity two gives \(m(G)\ge(1-o(1))ph\).
On the second subspace, apply that estimate at multiplicity one to \(G/Q(X^p)\), which vanishes at \(\alpha\) and still occupies at most two residue classes.
Since \(m(Q(X^p))=ph\), the stronger bound there is \(m(G)\ge(3/2-o(1))ph\).
The cited estimates are uniform in the graph for fixed seed and degree \(O_B(p)\).
A graph on a single class, if needed, contains \(Q(X^p)^j\) at multiplicity \(j\) and satisfies the same inequalities directly.
The coefficient supremum norm of the pair is at least \(\exp(m(G))/(2B+2)\) because \(m(G)\le\log\|G\|_1\).
These estimates bound from below the distance between distinct integral solutions in the respective spaces.

<a id="count"></a>
## Counting and choosing a pair

Fix \(t>t_0=1+2(e-1)/r\), set \(N=2B+2,\ D=pB+1\) and take coefficients in \([0,T]\) with \(T=\lfloor\exp(tph)\rfloor\).
The [integral two-jet count](../claims/Yin_C_G0345_v362.md#jets) bounds the number of distinct values of \((G(\alpha),G'(\alpha))\) by
\[
 (6NT)^{2e}(1+D)^e\exp(2Dh).
\]
Subtract a fixed member of a largest fiber from every member.
The resulting set of integral double-contact pairs has supremum norm at most \(T\), and its cardinality has logarithm at least \((2rt-2B+o(1))ph\).

In a real \(d\)-dimensional linear space with the restricted supremum norm, points separated by distance \(L\) in the ball of radius \(T\) number at most \((1+2T/L)^d\), by comparing disjoint balls of radius \(L/2\) against the ball of radius \(T+L/2\).
Consequently if the rational span of our differences consisted of pairs with zero reflected determinant, the logarithmic count would be at most \((r(t-1)+o(1))ph\).
If all differences lay in the second subspace, the bound would be \((d_0\max(0,t-3/2)+o(1))ph\).

Both upper bounds are strictly smaller than the lower bound.
For the first this follows from \(2rt_0-2B=r(t_0-1)=2(e-1)\) and the larger slope \(2r\).
For the second it suffices to check \(d_0\max(0,t_0-3/2)\le2(e-1)\), since \(d_0<2r\).
When \(r\le e\) one has \(d_0=r\).
When \(r\ge e\), write \(x=r/e\ge1\), \(\nu=(e-1)/e\le1\).
If \(t_0>3/2\), the difference \(2(e-1)-(2r-e)(t_0-3/2)\), divided by \(e\), is
\[
 x-\tfrac12-2\nu(1-1/x)\ \ge\ x-\tfrac52+2/x\ \ge\ 2\sqrt2-\tfrac52>0 .
\]
For \(t_0\le3/2\) the upper exponent for the second subspace at \(t_0\) is zero.

Hence some difference \(J\) avoids the second subspace, and the quadratic expression \(\Delta(U,V)=UU^\iota-VV^\iota\) does not vanish identically on the span of the differences.
One difference or a sum of two differences gives a pair \(F\) with \(\Delta(F)\ne0\), by polarization.
Among \(F+cJ,\ c=0,1,2,3\), at most one lies in the second subspace and at most two have zero reflected determinant, by a nonzero scalar coefficient of the quadratic polynomial \(\Delta(F+cJ)\) in \(c\).
Choose a remaining pair.
Its height is \(O_B(T)\), and the graph equation implies that both row values at \(z\) are nonzero.
A primitive common divisor \(E\) of its two rows therefore has \(E(z)\ne0\).
Dividing it out preserves both copies of \(P\) and the nonzero reflected determinant.
The quotient row \(A/E\) has one-norm at most \(2^B\exp(m(A/E))\le2^B\|A\|_1\) for either row \(A\), by the elementary symmetric bounds on its coefficients, including the leading coefficient, and the nonnegativity of \(m(E)\).
Taking prime limits and then \(t\downarrow t_0\) proves (1).

<a id="consequence"></a>
## What a lower bound at excess width would imply

For every fixed \(\delta>0\), taking \(B=e+\lceil\delta e\rceil\) gives upper rate at most \((1+2/\delta)h\).
A common positive lower bound for the limiting inferior rates at these widths for all reciprocal seeds would therefore imply the unrestricted positive Lehmer gap by the [reduction to reciprocal units](../claims/Yin_C_G0345_v408.md#lower).
Conversely, a positive Lehmer gap gives a common lower bound by the left side of (1).

If the unrestricted infimum is zero, choose reciprocal seeds \(P_j\) of positive measures \(h_j\to0\) and degrees \(e_j\to\infty\).
Bounded-degree monic polynomials of bounded measure have bounded integral coefficients, which justifies the degree assertion.
Take \(k_j=\lceil e_j\sqrt{h_j}\rceil\) and \(B_j=e_j+k_j\).
Then \(k_j/e_j\to0\), and the upper rate in (1) is at most \(h_j+2\sqrt{h_j}\).
For each \(j\), every sufficiently large prime thus admits an ordinary qualifying pair of width \(B_j\) and normalized log height at most \(2h_j+2\sqrt{h_j}\).
This does not prescribe how early those primes occur, or the excess width solely as a function of degree.
The [equal-width rate for independent inverse pairs](../claims/Yin_C_G0345_v414.md#statement) can have a factor of order \(e\) multiplying \(h\) at width \(e\).
The new upper estimate shows why carrying that factor over to width \(e+\lceil\delta e\rceil\) requires a different argument.
The [sharp growing-width rate for a signed row](../claims/Yin_C_G0345_v425.md#statement) by itself supplies a pair with identically zero reflected determinant, and the [ordinary graph constructed at width four times the seed degree](../ledger/Yin_L_G0462_v231.md#width) has a different conclusion about its Mahler measure.
The uniform lower bound for the actual measures of the varying seeds remains open.

## Assessment history

### Decision relative-row-width

| Field | Value |
| --- | --- |
| date | 2026-11-24T17:46 |
| status | proved |
| reason | The dimension and packing estimates apply before the original height cutoff and survive removal of common divisors. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#width) | Ordinary coprime rows at fixed seed and width, including the vanishing-gap diagonal. |
| argument | [Bad](#bad) | Dimensions of the two exceptional spaces and their separation estimates. |
| argument | [Count](#count) | Jet counting, polarization and gcd removal. |
| argument | [Consequence](#consequence) | Relative-width equivalence and the seed-dependent prime thresholds. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1041.md#finding) | The fixed statement, argument and qualifications at the specified inputs. |

## Current assessment

[Selected decision](#decision-relative-row-width)
