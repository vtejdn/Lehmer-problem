---
author: Yin
---

# Finite-time Fourier and Gaussian estimates for Mahler measure on companion tori

The estimates concern the [total logarithmic Mahler measure](../tasks/Yin_T_G0001_v1.md#contract) of a nontorsion algebraic unit.
Both observables use the power basis to fix the norm on integer characters.

<a id="periodic"></a>
## Periodic Fourier resolution for an irreducible unit companion

Let \(P\in\mathbb Z[X]\) be the monic minimal polynomial of a nontorsion algebraic unit \(\alpha\), and set \(d=\deg P\).
On \(\mathbb R^d/\mathbb Z^d\) use the toral automorphism \(A\) whose transpose is multiplication by \(\alpha\) in the power basis of \(\mathbb Z[\alpha]\).
Write \(N_j=|\operatorname{Fix}(A^j)|=|\det(A^j-I)|\) and \(r_j=\min\{\|k\|_\infty:0\ne k\in ((A^\mathsf T)^j-I)\mathbb Z^d\}\).
The integer \(r_j\) is the smallest sup norm of a Fourier frequency on which averaging over \(\operatorname{Fix}(A^j)\) differs from Haar integration, by finite-group character orthogonality.
For every \(j\ge1\),
\[
 \frac{N_j^{1/d}}{d\,M(P)^{1-1/d}}\ \le\ r_j\ \le\ \lfloor N_j^{1/d}\rfloor . \tag{1}
\]
The upper bound follows by taking integer vectors in a cube of side \(\lfloor N_j^{1/d}\rfloor+1\) modulo a sublattice of index \(N_j\).
For a vector in that sublattice, the corresponding polynomial value \(V(\alpha)=\sum_{l<d}k_l\alpha^l\) lies in \((\alpha^j-1)\mathbb Z[\alpha]\).
For nonzero \(k\), its nonzero absolute field norm is at least \(N_j\) and at most \((d\|k\|_\infty)^d M(P)^{d-1}\), by multiplying the individual archimedean bounds.
This proves (1).
The fixed-polynomial periodic point growth formula gives \(\lim_{j\to\infty} j^{-1}\log r_j=(\log M(P))/d\), including algebraic nontorsion eigenvalues on the circle. [Lind, Section 4](../audits/literature/Lin82/readme.md)
On bounded-measure Salem polynomials of growing degree, this fixed-polynomial rate tends to zero.
For finite times, (1) incurs a logarithmic error of at most \(d\log d+(d-1)\log M(P)\) when recovering \(\log N_j\) from \(d\log r_j\).
The unit-circle factors in \(N_j=\prod_i|\alpha_i^j-1|\) still enter the estimate of \(\log N_j\).

<a id="finite-time-dynamics"></a>
## Recovering total measure from finite-time Fourier resolution

Let \(P\) be an irreducible nontorsion unit polynomial of degree \(d\), write \(m=\log M(P)\), and retain the power basis and \(N_j,r_j\) of [(1)](#periodic).
Put \(Y=\lceil d(\log(2d))^4\rceil\).
Along every sequence with \(d\to\infty\), for each fixed \(\eta>0\) one has
\[
 \frac{1}{Y}\#\left\{Y\le j\le2Y:
 \left|\frac{d\log r_j}{jm}-1\right|>\eta\right\}\longrightarrow0 .
\]
Indeed the [cyclic resultant estimate](../ledger/Yin_L_G0462_v70.md#linear) gives \(\log N_j/(jm)\to1\) in density as soon as \(Y/d\to\infty\).
The difference \(\log N_j-d\log r_j\) lies between zero and \(d\log d+(d-1)m\) by (1).
After division by \(Ym\) this tends to zero, since the [degree-dependent lower bound](Yin_C_G0147_v5.md#argument) gives \(m\gg(\log\log d/\log d)^3\) for large \(d\).
In particular the median of \(d\log r_j/j\) recovers total logarithmic measure with relative error tending to zero uniformly in \(P\).
A uniform positive lower bound for these medians at all sufficiently large degrees is equivalent to a positive Lehmer gap.
Indeed bounded degree has a positive gap by finiteness at bounded Mahler measure, and every input with positive logarithmic measure below \(\log 2\) has a nontorsion monic unit factor up to sign after removing zero roots.

<a id="salem"></a>
## Short-time behavior on two Salem families

For \(j<d\) every such companion has \(r_j=1\), since \(X^j-1\) already represents a nonzero vector of sup norm one in the annihilator.
At times \(d\le j\le2d\), even \(r_j\ge2\) can fail on almost every time for a genuine Salem family.
Take the [irreducible Salem polynomials tending to the cubic Pisot unit](Yin_C_G0901_v195.md#cubic), with \(m\to\log\rho\) and \(\rho^3=\rho+1\).
On this shorter window the same cyclic resultant estimate gives \(\log N_j\le(1+o(1))jm\) outside \(o(d)\) orders.
Then \(\log r_j\le(2+o(1))\log\rho<\log2\) since \(\rho<4/3\), so \(r_j=1\) at all those times.

Even the successive growth of the full periodic counts can give a different exponential rate throughout a prescribed initial interval.
For each \(H\ge2\), Dirichlet's theorem supplies a prime \(r\ge5\) congruent to one modulo \(\operatorname{lcm}(1,\ldots,H)\).
Use the [Salem minimum](Yin_C_G0901_v195.md#integer) \(F_d=X^d+1-\sum_{l=1}^{d-1}X^l\), \(d=r-1\).
Here \(F_d(1)=3-d\).
For \(1\le j\le H\), every nontrivial \(j\)-th root of unity \(\zeta\) satisfies \(\zeta^d=1\), and evaluation of \((X-1)F_d=X^d(X-2)+2X-1\) gives \(F_d(\zeta)=3\).
It follows by the resultant identity that \(N_j=(d-3)3^{j-1}\) throughout the interval.
Thus \(N_{j+1}/N_j=3\) there whenever \(j<H\), although \(M(F_d)\to2\).

<a id="heat"></a>
## Gaussian noise on the companion torus

For \(\varepsilon>0\), let \(G_\varepsilon\) be the Gaussian convolution with Fourier multiplier \(\exp(-\varepsilon\|v\|_2^2)\) at the character \(e_v\), and let \(U_A\) be the Koopman operator of \(A\).
On mean-zero \(L^2\) one has \(\|(G_\varepsilon U_A)^n\|=\exp(-\varepsilon\kappa_n(P))\), where
\[
 \kappa_n(P)=\min_{v\in\mathbb Z^d\setminus\{0\}}\sum_{i=0}^{n-1}\|(A^\mathsf T)^iv\|_2^2 .
\]
Indeed \(U_A\) permutes the characters and \(A^\mathsf T\) bijects the nonzero lattice vectors, so starting the sum at \(i=0\) gives the same minimum as starting at \(i=1\).
For a fixed irreducible companion, the time when the norm first falls below \(e^{-1}\) is asymptotic to \(d\log(1/\varepsilon)/(2m)\) as \(\varepsilon\downarrow0\), by the ergodic diagonalizable case of [Fannjiang and Wołowski, Theorem 3](../audits/literature/FW03/readme.md).
In the power basis one has exactly \(\kappa_n=n\) for \(1\le n\le d\) and \(\kappa_{d+1}>d+1\).
Every summand is at least one, and the orbit of \(1\) starts with the \(d\) basis vectors.
Any vector attaining equality for \(d+1\) steps would have to follow signed coordinate vectors through the last basis vector.
Its next image has squared norm at least two, since the unit constant coefficient and at least one intermediate coefficient of \(P\) are nonzero.
Consequently at fixed noise strength and large enough degree the dissipation time is exactly \(\lfloor1/\varepsilon\rfloor+1\), independently of \(m\).

<a id="deterministic"></a>
## Recovering total measure at a single time

At a single deterministic time \(T=\lceil d^2(\log(2d))^4\rceil\), one recovers \(m\) with relative error tending to zero uniformly as \(d\to\infty\) from \(d\log\kappa_T/(2(T-1))\).
For every \(n\ge1\), the finite-time error satisfies
\[
 -\log d-2(d-1)m
 \ \le\ \log\kappa_n-\frac{2(n-1)m}{d}
 \ \le\ (d+2)\log d+2(d-1)m+\log n .
\]
To prove this, let \(V_{il}=\alpha_i^l\) for the roots \(\alpha_i\) of \(P\) and \(0\le l<d\), and set \(w_i=\sum_{h=0}^{n-1}|\alpha_i|^{2h}\).
In embedding coordinates the energy is \(W(v)=\sum_i w_i|(Vv)_i|^2\), since multiplication by \(\alpha\) is diagonal there.
It lies between \(\|V^{-1}\|_2^{-2}\) and \(\|V\|_2^2\) times the corresponding power-basis orbit energy.
For nonzero integer \(v\), the product of \(|(Vv)_i|\) is the absolute norm of a nonzero algebraic integer and is at least one.
The arithmetic-geometric mean therefore gives \(W(v)\ge d(\prod_i w_i)^{1/d}\).
Conversely its minimum on these vectors is at most \(d|\det V|^{2/d}(\prod_iw_i)^{1/d}\) by Minkowski's convex body theorem on the real ellipsoid of \(W\).
Indeed the real Gram matrix \(V^*\operatorname{diag}(w_i)V\) has determinant \(|\det V|^2\prod_i w_i\), and the Euclidean unit ball contains a cube of side \(2/\sqrt d\).

Write \(M=e^m\).
The row bounds give \(\|V\|_2\le dM^{d-1}\).
By Hadamard's inequality every cofactor has modulus at most \(d^{(d-1)/2}M^{d-1}\), using each selected root's row bound \(\sqrt d\max(1,|\alpha_i|)^{d-1}\) once.
Thus \(\|V^{-1}\|_2\le d^{(d+1)/2}M^{d-1}/|\det V|\).
Finally \(|\det V|\ge1\) by the integral nonzero discriminant and \(M^{2(n-1)}\le\prod_iw_i\le n^d M^{2(n-1)}\).
Substitution proves both bounds.
At \(n=T\) the dimension and measure errors divided by \(2(T-1)m/d\) tend to zero by the same degree-dependent lower bound used above.
Periodicity and approximation to roots of unity play no role in this estimate.

<a id="substitution"></a>
## Substitution in the companion polynomial

For \(P(X)=Q(X^k)\) and \(n=ks\), the power basis splits orthogonally into the \(k\) exponent classes modulo \(k\).
One step cycles the classes, applying the companion multiplication \(B\) of \(Q\) only on the step from the last class to the first.
For a vector \(u\) in class \(a\), \(0\le a<k\), its energy over \(ks\) times is
\[
 (k-a)\sum_{l=0}^{s-1}\|B^lu\|_2^2+a\sum_{l=1}^{s}\|B^lu\|_2^2 .
\]
Distinct classes contribute orthogonally at each time, and both sums are at least \(\kappa_s(Q)\) when \(u\ne0\).
Taking a minimizing \(u\) in class zero gives \(\kappa_{ks}(P)=k\kappa_s(Q)\).
The \(k\)-th power of the companion acts by \(B\) on each class, so \(r_{ks}(P)=r_s(Q)\) and \(N_{ks}(P)=N_s(Q)^k\).
These identities already hold for irreducible polynomials of unbounded degree with fixed measure.
For example take \(Q=X^2-X-1\), \(\phi=(1+\sqrt5)/2\), and \(k=2^a\).
At each stage the positive root \(\phi^{1/k}\) has norm \(-1\) by the even-degree minimal polynomial \(Q(X^k)\), so it cannot be a square in its field.
Adjoining its square root doubles the degree and proves irreducibility for the next stage, starting with \(k=1\).
Here \(M(Q(X^k))=\phi\) by the root formula.

## Assessment history

### Decision finite-time-observables

| Field | Value |
| --- | --- |
| date | 2026-11-27T11:12 |
| status | proved |
| reason | The independent proof check recovered both finite-time estimates with their explicit dependence on degree, the two Salem controls and the exact substitution identities. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Finite-time reconstruction](#finite-time-dynamics) | Uniform relative recovery on the periodic window, the equivalent median gap, and the companion heat estimate at the deterministic time below. |
| argument | [Lattice bounds](#periodic) | Cyclic-resultant comparison for the periodic annihilator. |
| argument | [Salem families](#salem) | Failure of short-window tests on genuine Salem polynomials. |
| argument | [Gaussian dissipation](#heat) | Operator norm, fixed-noise plateau and fixed-map small-noise asymptotic. |
| argument | [Weighted embedding lattice](#deterministic) | Explicit two-sided error and the deterministic time. |
| argument | [Power substitutions](#substitution) | Exact formulas and irreducible examples. |
| dependency | [Cyclic resultants](../ledger/Yin_L_G0462_v70.md#linear) | Density-one estimates in windows of the indicated lengths. |
| dependency | [Lower height bound](Yin_C_G0147_v5.md#argument) | The degree-dependent lower bound for total logarithmic measure. |
| dependency | [Cubic Salem family](Yin_C_G0901_v195.md#cubic) | Irreducible Salem examples approaching the plastic number. |
| dependency | [Integer Salem family](Yin_C_G0901_v195.md#integer) | Irreducible Salem examples approaching two. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1278.md#finding) | Six sections, including the operator and shortest-vector normalizations. |

## Current assessment

[Selected decision](#decision-finite-time-observables)
