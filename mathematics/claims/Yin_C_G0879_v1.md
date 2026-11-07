---
author: Yin
---

# Factor degrees and Mahler measures in fixed quadratic templates with measure-one endpoint

The question concerns the proposed measure-one alternative to the [off-circle pole argument](Yin_C_G0877_v1.md#factor-inputs).
The proof combines the all-root angular count and the third-moment observation of the contributing research agent with the [raw degree-weighted square-norm theorem](Yin_C_G0855_v2.md#decision-whole-independent-review-2026-11-04).
The [trace example](Yin_C_G0878_v1.md#statement) studies a specific member by a different method.

<a id="statement"></a>
## Uniform bounds for each positive factor

Fix \(a,b\in\mathbb Z[i][z]\), with \(a\ne0\) and multiplicative Mahler measure \(M(a)=1\).
Put \(Q_N(z)=a(z)(z^{2N}+1)-b(z)z^N\) for positive integers \(N\), and write \(m=\log M\).
There exist \(c,\eta>0\) and \(N_0\), depending only on \(a,b\), such that for \(N\ge N_0\) every monic irreducible factor \(g\) over \(\mathbb Q(i)\) of \(Q_N\) with \(m(g)>0\) satisfies \(\deg g\ge cN\) and \(m(g)\ge\eta\).
The same bounds, with template-dependent constants, hold for every positive-measure monic irreducible rational factor of the coefficient norm \(Q_N\overline{Q_N}\).
The bar conjugates coefficients only.
For \(a,b\in\mathbb Z[z]\) this covers every positive-measure rational irreducible factor of \(Q_N\) itself.
In particular taking \(N=2p\) precludes degrees \(o(p)\) along every sequence of primes.
The constants need not be uniform over different templates.

<a id="root-moments"></a>
## Radial displacement of all the roots

Because \(M(a)=1\), its leading coefficient is a Gaussian unit and all roots have modulus at most one.
Scale both polynomials by the inverse of that leading coefficient and write \(a=z^s a_0\) with \(a_0\) monic and \(a_0(0)\ne0\).
The constant coefficient of \(a_0\) is a nonzero Gaussian integer whose modulus is the product of the moduli of its roots.
Hence it is a unit, and every root of \(a_0\) has modulus one.
Let \(S\) be their finite set, and \(k=\deg a_0\) their number counting multiplicities.
For \(N\) large, \(P_N=z^{-s}Q_N\) is monic, its constant term is \(a_0(0)\), and its degree is \(2N+k\).
Its coefficient one-norm and number of nonzero terms are bounded solely in terms of \(a,b\).
The Cauchy root bound applied to \(P_N\) and its reversed polynomial, normalized by its constant unit, puts all its roots in one fixed annulus \(r_*\le |z|\le R_*\) with \(r_*>0\).
A root at which \(a(z)=0\) has modulus one and contributes zero to every radial moment, including when \(a,b\) have common factors.

For any other root write \(z=r e^{i\theta}\), \(v=|\log r|\).
The equation \(z^N+z^{-N}=b(z)/a(z)\) gives \(e^{Nv}\le 1+|b(z)/a(z)|\), since the smaller summand has modulus at most one.
If \(S\) is empty, the annulus bound gives \(Nv=O(1)\).
Otherwise let \(\delta\in[0,\pi]\) be the least angular distance from \(\theta\) to an element of \(S\).
For every \(\omega\in S\) the identity
\[
 |re^{i\theta}-\omega|^2=(r-1)^2+r|e^{i\theta}-\omega|^2
\]
gives \(|z-\omega|\ge c_0\max(v,\delta)\), because the annulus is fixed and the chord is at least \(2\delta/\pi\).
Together with the bound on \(|b|\) and the lower bound on \(r^s\), this implies
\[
 Nv\le C+k\log^+\!\left(1/\max(v,\delta)\right).
\]
Take the right side at zero in the extended sense.
For \(v\ge 1/N\) the logarithm is bounded both by \(\log N\) and by \(\log^+(1/\delta)\).
For \(v<1/N\) the left side is at most one.
Thus, with \(\log^+(1/0)=+\infty\), all roots satisfy
\[
 Nv\le C'+kX,\qquad X=\min\{\log N,\log^+(1/\delta)\}. \tag{1}
\]
For empty \(S\) use \(X=0\).

<a id="angular-count"></a>
## Counting roots near a pole direction

A degree-\(D\) polynomial with nonzero constant term and at most \(L\) terms has at most \(D|I|/(2\pi)+O(L)\) roots with arguments in any interval \(I\), counting multiplicity.
This elementary form of the sector estimate is also covered by [Hayman's angular distribution theorem](https://doi.org/10.1112/plms/s3-24.4.590).
To see the estimate directly, take two bounding rays containing no zero and intersect the sector with an annulus between radii \(\epsilon,R\).
On each ray choose a constant rotation so that the real part of the rotated polynomial in the positive radial variable is not identically zero.
It has at most \(L-1\) positive zeros by Descartes' rule of signs.
Between successive such zeros the image stays in a half-plane, so its net continuous change in argument has magnitude at most \(\pi\) on each of at most \(L\) subintervals.
The change along the outer circular arc tends to \(D|I|\) as \(R\to\infty\), by uniform domination of the leading term, and the inner arc contributes a term tending to zero as \(\epsilon\downarrow0\).
The argument principle gives the estimate on the sector, with boundary rays included if needed by slight outward perturbation.
Full-circle and empty intervals are immediate.

Applying this to \(P_N\) with its bounded number of terms gives, for \(0\le u\le\log N\),
\[
 \#\{\delta\le e^{-u}\}\le C_1(Ne^{-u}+1).
\]
Indeed the event is a union of at most \(|S|\) arcs of length \(2e^{-u}\).
For \(j=2,3\), integrating the tails up to \(\log N\) gives
\[
 \sum_{P_N(z)=0} X^j
 \le C_1\int_0^{\log N} j u^{j-1}(Ne^{-u}+1)\,du
 =O_j(N+(\log N)^j)=O_j(N).
\]
The number of roots is \(O(N)\), so (1) yields the unnormalized bounds
\[
 \sum_{P_N(z)=0}|\log|z||^2\le C_2/N,\qquad
 \sum_{P_N(z)=0}|\log|z||^3\le C_3/N^2.                 \tag{2}
\]
Every root count in (2) includes multiplicity.
Coefficient conjugation preserves the multiset of radial moduli, hence (2) also holds for \(H_N=P_N\overline{P_N}\), doubling the constants if necessary.

<a id="factor-bounds"></a>
## Transfer to rational and Gaussian irreducible factors

The norm polynomial \(H_N\) is monic in \(\mathbb Z[z]\) with constant term one and degree at most \(BN\) for a fixed \(B\) and large \(N\).
Let \(f\) be a positive-measure monic irreducible rational factor of \(H_N\), of degree \(d\), and write \(u_i=\log|\alpha_i|\) for the logs of the moduli of all its roots.
The \(\alpha_i\) are nontorsion algebraic units.
The [unit case of C855 v2, Part A](Yin_C_G0855_v2.md#statement), with its [fixed independent review](../audits/reviews/Yin_R_G1086_v1.md#raw-p2-whole), supplies \(d\sum_i u_i^2\ge1/10\) at the actual rational degree.
Only this previously established arithmetic inequality is used.
Because every summand is nonnegative, (2) gives \(1/(10d)\le C_2/N\), hence \(d\ge N/(10C_2)\).
Also \(\sum_i|u_i|=2m(f)\) since the product of the root moduli equals one.
Cauchy--Schwarz and (2) now give
\[
 (10BN)^{-2}\le \left(\sum_i u_i^2\right)^2
 \le \left(\sum_i |u_i|\right)\left(\sum_i |u_i|^3\right)
 \le 2m(f) C_3/N^2 .
\]
Consequently \(m(f)\ge1/(200B^2 C_3)\).
The factors removed in passing from \(Q_N\overline{Q_N}\) to \(H_N\) are a scalar unit and powers of \(z\), which have zero logarithmic measure.

For a positive-measure monic irreducible Gaussian factor \(g\mid P_N\), the rational minimal polynomial \(f\) of any root is either \(g\) if \(g=\bar g\), or \(g\bar g\) otherwise.
Indeed \(g\) and \(\bar g\) divide \(f\) over \(\mathbb Q(i)\), while \(f\) divides the rational polynomial \(g\bar g\), and \(g=\bar g\) means \(g\) itself is rational and irreducible.
In both cases \(f\mid H_N\), \(\deg f\le 2\deg g\), and \(0<m(f)\le2m(g)\) by conjugation invariance.
The rational bounds therefore imply the stated Gaussian bounds.
No bound for templates with varying coefficients or support is obtained here.

## Assessment history

### Decision fixed-template-whole

| Field | Value |
| --- | --- |
| date | 2026-11-07T17:27 |
| status | proved |
| reason | Independent review verified the whole-root moment estimates, the adopted rational square-norm input and both factorwise conclusions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Linear degree and uniform positive logarithmic Mahler measure for each positive irreducible factor of a fixed quadratic template with measure-one endpoint. |
| argument | [Proof section](#root-moments) | Root normalization, the uniform annulus and radial displacement near the finitely many pole directions. |
| argument | [Proof section](#angular-count) | A sector count with multiplicity and full-root second- and third-moment upper bounds. |
| argument | [Proof section](#factor-bounds) | Arithmetic square-norm lower bound, degree and measure inequalities, and Gaussian and rational field passage. |
| dependency | [Degree-weighted square norm](Yin_C_G0855_v2.md#decision-whole-independent-review-2026-11-04) | Part A for the actual rational degree and all archimedean conjugates of a nontorsion algebraic unit. |
| review | [Independent finding](../audits/reviews/Yin_R_G1104_v1.md#fixed-template-whole) | All of the selected statement and argument at the source scope specified in the finding. |

## Current assessment

[Selected decision](#decision-fixed-template-whole)

