---
author: Yin
---

# Excluding a cubic sign factor by the integer trace coordinates

<a id="statement"></a>
## The fourth coefficient and a nonreal cubic

Use the [strict odd-grid hypotheses](Yin_C_G0896_v1.md#statement) with the zero-profile coefficients through index four.
Thus \(h=\sum_{i=0}^{n-1}a_iE_i\) is integral with \(a_0=2,\ a_1=0,\ a_2=4\), and its values on the grid in decreasing trace order are strictly positive and then strictly negative, with both signs present.
Let \(G\) be the product, once each and with positive leading coefficients, of the primitive irreducible factors of \(h\) of odd multiplicity having a real root in \((-2,2)\).
At every such conductor, \(G\) cannot be cubic with a nonreal root.
Consequently every sequence of these inputs with \(p\to\infty\) eventually satisfies \(\deg G\ge4\), by the [earlier bound for totally real \(G\)](Yin_C_G0896_v1.md#decision-totally-real-cut-degree-reviewed).
Indeed, each factor of \(G\) has a real root, so \(\deg G\le2\) implies total reality.
The earlier square-root-scale bound continues to apply whenever \(G\) is totally real.

<a id="positive-symbol"></a>
## A positive polynomial on the entire trace interval

Suppose \(G=At^3+Bt^2+Ct+D\) has two nonreal conjugate roots and a real root \(y\).
Since every factor used to form \(G\) has a real root in the interval, \(G\) is irreducible and \(y\) lies strictly in the transition gap.
The integer polynomial \(h/G\) has even multiplicity at every interior real zero and is positive at a node to the right of \(y\), since \(A>0\).
Hence \(h/G\ge0\) throughout \([-2,2]\), and \((t-y)h(t)\ge0\) there.
This argument applies separately to each finite polynomial \(h\), regardless of its degree or the position of further even-multiplicity zeros.

Put \(t=z+z^{-1}=2\cos\theta\) on the unit circle with uniform angular probability \(d\omega\), and let \(d\sigma=(4-t^2)d\omega/2\) denote the semicircle probability in the trace variable.
The sine formula \(E_i(2\cos\theta)=\sin((i+1)\theta)/\sin\theta\) gives \(\int E_i E_j\,d\sigma=\delta_{ij}\).
In what follows set \(a_i=0\) outside the index range of \(h\).
Define
\[
       W=(4-t^2)(t-y)h(t),\qquad
       c_k=\int W\cos(k\theta)\,d\omega .
\]
The circle geometric mean of \(W\) is \(M(h^*)\) with \(h^*(z)=z^{\deg h}h(z+z^{-1})\).
Indeed \(W\ge0\), and all roots of the lifts of \(4-t^2\) and \(t-y\) lie on the unit circle, with leading coefficients of absolute value one.
By the circle mean formula for Mahler measure and integer divisibility, \(M(h^*)\ge M(G^*)=:M\).
The same formula gives, for every polynomial \(R(z)\) with \(R(0)=1\),
\[
         \int W|R(z)|^2d\omega\ \ge\ M(h^*) M(R)^2\ \ge\ M.           \tag{1}
\]
Here the arithmetic-geometric mean inequality applies since the zeros are finite and their logarithms are integrable, and \(M(R)\ge|R(0)|=1\).

The three fixed coefficients give \(\int h\,d\sigma=2,\ \int th\,d\sigma=0,\ \int t^2h\,d\sigma=6\).
Taking \(R=1-z\) in (1) gives \(M\le \int (2-t)W\,d\omega=-12-8y\).
In particular \(-2<y<-3/2\) and \(A\le M<4\).
Write \(q,\bar q\) for the nonreal trace roots and \(\lambda>1\) for the larger modulus of the lifts of \(q\).
Then \(M=A\lambda^2\), so \(\lambda<2\) and \(|q|\le\lambda+\lambda^{-1}\le5/2\).
The elementary symmetric functions of the three roots give the integer box
\[
   1\le A\le3,\quad |B|\le21,\quad |C|\le49,\quad 1\le D\le38.
\]
The last lower bound uses \(D=-Ay|q|^2>0\).

<a id="integer-prediction"></a>
## An integer continuation with a lower bound on every prediction error

The Fourier coefficients of \(W\) are real with \(c_{-k}=c_k\).
They satisfy
\[
 c_0=-4y,\qquad c_1=6,\qquad
 c_k=a_{k+1}-a_{k-3}-y(a_k-a_{k-2})\quad(k\ge2).                     \tag{2}
\]
Indeed for \(k\ge1\) one has \(c_k=\int T_k(t)(t-y)h\,d\sigma\), where \(T_k(2\cos\theta)=2\cos(k\theta)=E_k-E_{k-2}\), with \(E_{-1}=0\).
For \(k\ge2\) use \(tT_k=T_{k+1}+T_{k-1}\) and semicircle orthogonality to get (2).

For \(k\ge0\) minimize \(\int W|R|^2d\omega\) among real polynomials \(R\) with \(R(0)=1\) and degree at most \(k\), and denote the minimum by \(e_k\).
The Gram matrix is positive definite since \(W>0\) except at finitely many points.
If \(R=1-\sum_{j=1}^{k-1}f_j z^j\) achieves the previous minimum \(e=e_{k-1}\), it is orthogonal to \(z,\ldots,z^{k-1}\) in this weighted inner product.
The reversed polynomial \(S=z^kR(1/z)\) has the same norm squared and is orthogonal to those same monomials, by the symmetry of the real moments.
Its inner product with \(R\) is \(c_k-v\), where \(v=\sum_{j=1}^{k-1}f_j c_{k-j}\).
The optimizing polynomial for degree \(k\) is \(R-\phi S\), since the old monomials and \(S\) span \(z,\ldots,z^k\), with
\[
         \phi=(c_k-v)/e,\qquad
         e_k=e-(c_k-v)^2/e .
\]
The initial error is \(e_0=c_0\), and at order one the predictor is \(c_1/c_0\).
By (1) every actual prefix satisfies \(e_k\ge M\).
At each order \(k\ge2\), (2) thus restricts the next integer \(a_{k+1}\) to the interval specified by
\[
       |a_{k+1}-a_{k-3}-y(a_k-a_{k-2})-v|
                             \le\sqrt{e(e-M)}.                           \tag{3}
\]
This remains necessary beyond the degree of \(h\), where its actual coordinate continuation is zero.

The [exhaustive integer calculation](../computations/programs/Yin_J_G0155/versions/v5/readme.md#enumeration) tests the coefficient box, requiring negative cubic discriminant, a root in the indicated open interval and \(M\le-12-8y\).
Twelve cubics remain after this outer test.
Five are excluded by \(e_1<M\), and branching over every integer in (3) excludes all seven remaining cubics by order \(27\).
The calculation uses outward rational enclosures, including when an interval determines which integer branches are visited.
Thus even the necessary finite prefix of moments of a single putative \(h\) cannot exist, which proves the assertion.

## Assessment history

### Decision cubic-prediction-exclusion

| Field | Value |
| --- | --- |
| date | 2026-11-16T10:30 |
| status | open |
| reason | Retain the single-conductor cubic exclusion and its finite moment certificate for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Cubic obstruction](#statement) | All conductors with the fixed fourth zero-profile coefficient and the resulting asymptotic degree floor. |
| argument | [Continuous positivity](#positive-symbol) | Signs between nodes, geometric mean of the symbol and the cubic coefficient box. |
| argument | [Integer prediction](#integer-prediction) | Moments, finite-dimensional projection, and covering ranges for unrestricted subsequent coordinates. |
| dependency | [Finite computation](../computations/programs/Yin_J_G0155/versions/v5/readme.md#enumeration) | All twelve outer candidates and exhaustion of the outward-rounded integer trees. |
| dependency | [Totally real bound](Yin_C_G0896_v1.md#decision-totally-real-cut-degree-reviewed) | Exclusion at bounded degree on the totally real subsequences. |


### Decision cubic-prediction-exclusion-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T10:39 |
| status | proved |
| reason | Adopt the exclusion of a nonreal cubic sign factor at every conductor matching the fourth zero-profile coefficient. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Cubic obstruction](#statement) | All conductors with the fixed fourth zero-profile coefficient and the resulting asymptotic degree floor. |
| argument | [Continuous positivity](#positive-symbol) | Signs between nodes, geometric mean of the symbol and the cubic coefficient box. |
| argument | [Integer prediction](#integer-prediction) | Moments, finite-dimensional projection, and covering ranges for unrestricted subsequent coordinates. |
| dependency | [Finite computation](../computations/programs/Yin_J_G0155/versions/v5/readme.md#enumeration) | All twelve outer candidates and exhaustion of the outward-rounded integer trees. |
| dependency | [Totally real bound](Yin_C_G0896_v1.md#decision-totally-real-cut-degree-reviewed) | Exclusion at bounded degree on the totally real subsequences. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v71.md#cubic-prediction-review) | Independent review of continuous positivity, moment prediction, degree extension and the proof at each conductor. |
| review | [Independent finite computation](../audits/reviews/Yin_R_G1107_v71.md#cubic-enumeration-review) | Exact integer computation and direct numerical check of each finite tree. |

## Current assessment
[Selected decision](#decision-cubic-prediction-exclusion-reviewed)
