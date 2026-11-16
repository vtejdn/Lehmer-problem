---
author: Yin
---

# An arithmetic limit law for normalized residues on the full odd grid

<a id="statement"></a>
## A uniform resultant bound

Use the [strict odd-grid chamber](../ledger/Yin_L_G0464_v5.md#odd-grid-product) with odd \(p=2n+1\), traces \(b_j=2\cos(2\pi j/p)\) for \(1\le j\le n\), and \(B=B_n=\prod_j(t-b_j)\).
Let \(Q=(t-A)B+C\) with \(A\in\mathbb Z\), \(C\in\mathbb Z[t]\), \(\deg C<n\), and write \(\rho_j=Q(b_j)/B'(b_j)\).
The residues are positive through some \(1\le c<n\), negative thereafter, and \(Q(-2)/B(-2)<0\).
Write \(P(z)=z^{n+1}Q(z+z^{-1})\) and \(\Delta=|\operatorname{Res}(B,Q)|\).
For every sequence \(p\to\infty\) with whole measures \(1<M(P)\to1\),
\[
                         \limsup \Delta^{1/n}\le 149/100.                 \tag{1}
\]
This holds for composite and prime conductors and all five possible limiting profiles.

More precisely, pass to a subsequence with [fixed coefficient limit](../ledger/Yin_L_G0464_v5.md#only-left-endpoint) \(P_{*,x}=(1-xz+z^2)^2/((1-z)(1-z^2))\), \(x\in\{-2,-1,0,1,2\}\).
The empirical distributions of \(U_j=p\rho_j/(b_j-x)^2\), omitting any \(b_j=x\), are tight.
Every weak limit \(\eta\) is supported on \([0,\infty)\) and satisfies
\[
 \int u\,d\eta\le2,\qquad
 \int\log u\,d\eta\ge\limsup\frac{\log\Delta}{n},\qquad
 \int\log|F|\,d\eta^{\otimes k}\ge0                                      \tag{2}
\]
for every \(k\ge1\) and \(0\ne F\in\mathbb Z[u_1,\ldots,u_k]\).
The upper limit in (2) is taken along the subsequence realizing \(\eta\).
In particular \(\eta\) has no atoms, by taking \(F(u,v)=u-v\).
The bound concerns the resultant on a hypothetical shrinking sequence and leaves open whether such integral inputs exist.

<a id="normalization"></a>
## A conditional first moment

Let \(a=2\cos((2c+1)\pi/p)\), \(X_j=p(b_j-a)\rho_j>0\), \(D_p(t)=(t-a)(t-x)^2\), and \(D(t)=(t+2)(t-x)^2\).
For \(\alpha\) the arcsine probability on \([-2,2]\), the [matched moments and exact product](../ledger/Yin_L_G0464_v23.md#completed-grid) give \(a\to-2\) and
\[
  \frac1n\sum_j X_j V(b_j)\longrightarrow 2\int D(t)V(t)\,d\alpha(t),
  \qquad
  \frac1n\sum_j\log X_j=\frac{\log\Delta}{n}+o(1)
\]
for every continuous \(V\) in the first limit.
The unweighted grid converges to \(\alpha\).
The joint empirical distributions of \((b_j,X_j)\) are tight because their second coordinate has bounded mean.
Let \(\lambda\) be any joint weak limit and project it onto the first coordinate to obtain \(\alpha\).
For \(V\ge0\), first truncate \(X\) at a fixed height, pass to the limit and then increase the truncation height.
It follows that the measure obtained by projecting \(X\,d\lambda\) onto the trace coordinate is dominated by \(2D\,d\alpha\).
In the joint law set \(u=X/D(t)\) off the \(\alpha\)-null zero set of \(D\).
Integrating the measure domination against \(1/D\) off that set gives \(\int u\,d\lambda\le2\).
Its law \(\eta\) is supported on \([0,\infty)\).
On compact sets avoiding \(t=-2,x\) and with \(X\) bounded, \(X/D_p(t)\) tends uniformly to \(X/D(t)\).
Discarding neighborhoods of these two trace values and the large \(X\) tail costs arbitrarily little empirical probability.
This proves tightness and identifies the subsequential empirical limits in the statement.
In particular any subsequence realizing \(\eta\) admits this joint extraction, also after first approaching the upper limit of the logarithmic resultant rate.

The positive parts of \(\log X_j\) are uniformly integrable, since \(X_j\) have bounded mean and \(\log y/y\to0\) as \(y\to\infty\).
Truncation from below followed by weak convergence therefore gives \(\int\log X\,d\lambda\ge\limsup n^{-1}\sum_j\log X_j\).
For \(v=-2,x\), the angular mean of \(\log|2\cos\theta-v|\) is zero by factoring the corresponding quadratic into two unit-circle factors and the unit-circle mean formula.
These functions are integrable, including at the endpoints, so \(\int\log D\,d\alpha=0\).
Consequently \(\int\log u\,d\eta=\int\log X\,d\lambda\) and the second inequality of (2) follows.

<a id="orbit"></a>
## Vanishing proportions and cleared algebraic integers

Write \(Z_j=p\rho_j\).
In the [integral trace coordinates](Yin_C_G0881_v3.md#prefix-coordinates), \(C=\sum_{i=0}^{n-1}a_iB_{n-i-1}\) with \(a_i\in\mathbb Z\), and \(h=\sum_i a_i E_i\) gives \(Z_j=(4-b_j^2)h(b_j)\).
Thus \(Z_j\) is an algebraic integer equivariant under conjugation of \(b_j\).
The entire grid decomposes by the order \(d>1\) of the root of unity, \(d\mid p\), into complete real cyclotomic orbits.
On orbits avoiding \(b_j=x\), the \(U_j\) are algebraic numbers and equivariant under the same action.

Let \(\kappa=n-c\).
The [terminal-block estimate](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) gives \(\kappa/p\to0\) and \(\kappa=p^{1-o(1)}\).
Discard all orders \(d\le \max(6,p/(2\kappa-1))\).
They contain at most the sum of those positive integers, hence \(p^{o(1)}=o(n)\) nodes, and include every possible \(b_j=x\).
Each remaining orbit contains the index
\[
 j=(p/d)(d-1)/2=(p-p/d)/2> (p-(2\kappa+1))/2=c,
\]
since \((d-1)/2\) is coprime to \(d\).
It contains a negative \(U_j\).
If the algebraic degree of \(U_j\) on such an orbit is at most \(m\), at least a \(1/m\) fraction of its values are negative, because all conjugates occur with equal multiplicity.
Thus all such small-degree orbits together occupy at most \(m\kappa\) nodes.
On each remaining orbit the relative frequency of any individual value is at most \(1/m\).
Writing \(\epsilon_p\) for the largest frequency of any single \(U_j\) among the retained orders, with denominator \(n\), gives \(\limsup\epsilon_p\le1/m\) for each fixed \(m\).
Hence \(\epsilon_p\to0\).

For a fixed \(F\) as in (2), the proportion of ordered grid \(k\)-tuples that either meet a discarded order or satisfy \(F(U_{j_1},\ldots,U_{j_k})=0\) tends to zero.
Indeed a nonzero univariate specialization has at most its degree in roots, each of probability at most \(\epsilon_p\) before renormalization.
When a specialization is identically zero its nonzero formal leading coefficient in the last variable vanishes on the preceding coordinates.
Induction gives the assertion, with independent uniform choices of indices and repetitions allowed.
The set \(\mathcal T_p\) of retained nonzero tuples is invariant under simultaneous conjugation.

Put \(m_i=\deg_{u_i}F\) and \(s_j=(b_j-x)^2\).
On \(\mathcal T_p\) each value
\[
 N_{\mathbf j}=\prod_i s_{j_i}^{m_i}\,F(Z_{j_1}/s_{j_1},\ldots,Z_{j_k}/s_{j_k})
\]
is a nonzero algebraic integer, by expansion of \(F\).
Their product is fixed by the Galois group of the cyclotomic field, so its absolute value is an integer at least one.
Multiply each value by \(\prod_i(b_{j_i}-a)^{m_i}\) to obtain \(K_{\mathbf j}\).
Across all \(n^k\) tuples the normalized log of the absolute multiplier product is \((\sum_i m_i)\log|B(a)|/n\ge0\) by the [midpoint evaluation](../ledger/Yin_L_G0464_v5.md#odd-grid-product).
Omitting \(o(n^k)\) tuples decreases this normalized log by at most \(o(1)\), since every log multiplier is bounded above by \((\sum_i m_i)\log4\).
It follows that \(n^{-k}\sum_{\mathcal T_p}\log|K_{\mathbf j}|\ge-o(1)\).

After expanding \(F\), \(K_{\mathbf j}\) is a fixed polynomial expression in the \(X_{j_i}\) and \(D_p(b_{j_i})\), homogenized separately in each pair of coordinates.
It is defined by that expression on every tuple, including the deleted ones.
Its positive logarithm is bounded by a constant plus \(\sum_i m_i\log(1+X_{j_i})\), uniformly integrable under the empirical product laws.
Those laws converge to \(\lambda^{\otimes k}\), also after removing the tuples of vanishing proportion.
Truncating the log from below and using joint convergence with \(a\to-2\) now gives
\[
 0\le \int\log\left|\prod_i D(t_i)^{m_i}F(u_1,\ldots,u_k)\right|\,d\lambda^{\otimes k}.
\]
The terms in \(\log D\) are integrable with mean zero.
This proves the last assertion of (2), including the energy inequality from \(u_1-u_2\).
Its positive part is integrable by the first-moment bound, so a diagonal atom would contradict the inequality.

<a id="scalar"></a>
## A rational certificate for the numerical bound

Take the six polynomials \(f_i\) and positive integer weights \(w_i\) in the following order.
\[
 (f_i)=(u-1,u-2,u-3,u^2-3u+1,u^2-4u+2,u^2-5u+5),
 \qquad (w_i)=(20,12,1,5,3,2).
\]
On \(u\ge0\) they satisfy
\[
                  u\prod_{i=1}^6 |f_i(u)|^{w_i/40}\,e^{\,2-u}
                        \ \le\ 149/100 .                                 \tag{3}
\]
At zero and the polynomial roots the left side vanishes.
Elsewhere let \(g\) be its logarithm.
Each \(f_i\) has only simple positive real roots, all distinct across the list.
Thus \(g'=1/u-1+\sum_i w_i f_i'/(40 f_i)\) is strictly decreasing on each interval between singularities by the partial fraction expansion.
It changes sign from positive to negative on each such interval, including the first and the unbounded last interval.
There are ten maxima.
The following rational brackets and integer inequalities verify (3) without numerical root finding.

In each row take \(a=r/1000,\ b=(r+1)/1000\), and \(T(a)=\sum_{j=0}^{13}(a-2)^j/j!\).
The integer \(h\) in the second row of the table bounds the maximum on the corresponding bracket by \(h/1000\).

| \(r\) | 283 | 492 | 664 | 1326 | 1581 | 2389 | 2906 | 3128 | 3532 | 4019 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \(h\) | 1429 | 1466 | 1405 | 1281 | 1466 | 1366 | 1452 | 1472 | 1319 | 1489 |

For each column, substitution gives \(g'(a)>0>g'(b)\) and \(T(a)>0\).
No polynomial root or quadratic vertex is inside a bracket, as one also checks from the displayed polynomials.
With \(M_i=\max(|f_i(a)|,|f_i(b)|)\), the rational comparison in each column is
\[
                  b^{40}\prod_i M_i^{w_i}<\big(hT(a)/1000\big)^{40}.
\]
The degree-thirteen Taylor polynomial is a lower bound for \(e^{a-2}\) by its positive even-order remainder.
Since \(e^{u-2}\) is increasing, the rational comparison bounds the maximum as asserted and proves (3).
Integrate its logarithm against \(\eta\) and use (2) with each \(f_i\) and \(\int u\le2\).
This gives \(\int\log u\,d\eta\le\log(149/100)\).
Every subsequence approaching the upper resultant rate admits one of the five profile limits and the joint extraction above, proving (1).

The prime-conductor normalization by the square of the profile factor and the use of integer norms of shifted samples were developed by a delegated researcher for Yin.
The responsible researcher extended the argument to all five profiles, composite grids, multivariate tests, and the explicit bound on 2026-11-16.

## Assessment history

### Decision normalized-residue-tests

| Field | Value |
| --- | --- |
| date | 2026-11-16T09:12 |
| status | open |
| reason | Record the full-grid arithmetic limit law and its explicit resultant bound for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Normalized limit law](#statement) | Five limiting profiles, every odd conductor, polynomial tests of every fixed arity, and the resultant bound. |
| argument | [Conditional moment](#normalization) | Weak limits, positivity, logarithmic comparison and expected normalized residue. |
| argument | [Cleared orbit products](#orbit) | Large-degree concentration, zero tuples, and arithmetic restrictions in the limit. |
| argument | [Numerical certificate](#scalar) | Explicit scalar inequality with rational brackets and its integral. |
| dependency | [Endpoint block size](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) | Conductor growth and the number of negative residues. |
| dependency | [Exact moment and product identities](../ledger/Yin_L_G0464_v23.md#completed-grid) | Positive joint masses and resultant normalization. |


### Decision normalized-residue-tests-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T09:16 |
| status | proved |
| reason | Adopt the arithmetic restrictions on all five normalized residue laws and the uniform resultant ceiling on every odd conductor. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Normalized limit law](#statement) | Five limiting profiles, every odd conductor, polynomial tests of every fixed arity, and the resultant bound. |
| argument | [Conditional moment](#normalization) | Weak limits, positivity, logarithmic comparison and expected normalized residue. |
| argument | [Cleared orbit products](#orbit) | Large-degree concentration, zero tuples, and arithmetic restrictions in the limit. |
| argument | [Numerical certificate](#scalar) | Explicit scalar inequality with rational brackets and its integral. |
| dependency | [Endpoint block size](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) | Conductor growth and the number of negative residues. |
| dependency | [Exact moment and product identities](../ledger/Yin_L_G0464_v23.md#completed-grid) | Positive joint masses and resultant normalization. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v57.md#normalized-residue-review) | Independent assessment of the joint moment, conjugate orbit products, multivariate tests and all ten rational comparisons. |

## Current assessment
[Selected decision](#decision-normalized-residue-tests-reviewed)
