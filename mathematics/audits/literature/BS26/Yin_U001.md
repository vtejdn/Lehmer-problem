---
author: Yin
---

# Global limit heights for adelic real divisors

<a id="bs26-u001"></a>
<a id="adelic-divisors"></a>
## Metrics and minima

Let \(X\) be a normal projective variety of dimension \(d\ge1\) over a number field \(K\).
An adelic real divisor \(\bar D\) consists of a real Cartier divisor \(D\) and continuous, locally Galois-invariant Green functions \(g_v\) at every place.
For a local real rational equation \(f\) of \(D\), the function \(g_v+\log|f|_v\) extends continuously across its divisor.
One normal integral projective model of \(X\), with a real Cartier divisor extending \(D\), induces these Green functions over a nonempty open subset of \(\operatorname{Spec}\mathcal O_K\).
Semipositivity requires a plurisubharmonic local metric at each infinite place and uniform approximation by vertically nef model metrics at each finite place.
For an integral Cartier divisor, Remark 4.3 identifies this convention with semipositivity of Zhang's metrized line bundle. [Edition](readme.md#edition) · [Definition 4.1 and semipositivity, pages 13–15](../../../literature/pdf/BS26.pdf#page=13)

The global height \(h_{\bar D}(x)\) sums the local Galois-orbit means of the Green functions with weights \([K_v:\mathbf Q_{v_0}]/[K:\mathbf Q]\), where \(v_0\) lies below \(v\).
The product formula permits replacing \(\bar D\) by a linearly equivalent representative whose support avoids \(x\).
The absolute minimum \(\mu^{\rm abs}(\bar D)\) is the infimum of \(h_{\bar D}\) over all algebraic points.
The essential minimum \(\mu^{\rm ess}(\bar D)\) is the supremum of the corresponding infima over nonempty Zariski open subsets.
A generic sequence eventually leaves each proper closed subset, and a \(\bar D\)-small sequence has heights tending to \(\mu^{\rm ess}(\bar D)\). [Sections 2 and 4.2](../../../literature/pdf/BS26.pdf#page=10) · [Sections 4.2 and 4.4, pages 15 and 20–22](../../../literature/pdf/BS26.pdf#page=15)

<a id="equidistribution-height"></a>
## Global heights in arbitrary adelic directions

Suppose \(\bar D\) is semipositive, its geometric divisor \(D\) is big, and its absolute and essential minima agree at \(s\).
For any \(\bar D\)-small generic sequence \((x_i)\) and any adelic real divisor \(\bar E\), Proposition 6.4 and Corollary 6.12 yield
\[
 \lim_{i\to\infty}h_{\bar E}(x_i)
 =\frac{(\bar D^{\,d}\cdot\bar E)-d\,s\,(D^{d-1}\cdot E)}
        {(D^d)}.
\]
Here \(E\) is the geometric divisor of \(\bar E\).
Section 4.2 defines the mixed arithmetic intersection with an arbitrary final adelic entry and differences of semipositive entries in the preceding slots.
In particular this limit applies to every adelic direction at once with the same sequence. [Mixed heights, pages 15–16](../../../literature/pdf/BS26.pdf#page=15) · [Proposition 6.4, page 30](../../../literature/pdf/BS26.pdf#page=30) · [Corollary 6.12, page 32](../../../literature/pdf/BS26.pdf#page=32)

Theorem 4.22 identifies equality of the minima with \(s=(\bar D^{\,d+1})/((d+1)(D^d))\) under the stated positivity hypotheses.
Proposition 6.4 identifies convergence for every such sequence and direction with differentiability of the essential minimum, and identifies the limit with its directional derivative.
Theorem 6.9 proves differentiability using normal modifications \(\phi_n\) and semipositive adelic divisors \(\bar Q_n\) with \(Q_n\) big and \(\phi_n^*\bar D-\bar Q_n\) pseudo-effective.
Its condition is \((\mu^{\rm ess}(\bar D)-\mu^{\rm abs}(\bar Q_n))/r(Q_n;\phi_n^*D)\to0\), where \(r(P;A)=\sup\{t:P-tA\text{ is big}\}\).
Corollary 6.12 uses the constant pair \((\mathrm{id},\bar D)\), whose inradius is one.
This inspection checked the definitions, the theorem hypotheses and the deduction of the global-height formula from differentiability.
It accepts the general approximation theorem and the minima theorem as stated. [Definition 3.1, page 11](../../../literature/pdf/BS26.pdf#page=11) · [Theorem 4.22, page 22](../../../literature/pdf/BS26.pdf#page=22) · [Definition 6.7 and Theorem 6.9, pages 30–31](../../../literature/pdf/BS26.pdf#page=30)

<a id="point-defect"></a>
## Arithmetic intersection with a point on a curve

For a smooth projective curve \(C/K\), a semipositive adelic divisor \(\bar L\) of degree \(D>0\), and an adelic divisor \(\bar Q\) over a \(K\)-rational point \(Q\), equation (4.3) gives
\[
  \frac{(\bar L\cdot\bar Q)}D
    =\frac{h_{\bar L}(Q)}D+\sum_v n_v\int g_{Q,v}\,\frac{c_1(\bar L_v)}D .
\]
The cycle contribution is the point height, and the local measures before division by \(D\) have mass \(D\).
For an adelic divisor over the zero divisor with bounded continuous local functions at finitely many places, equation (4.4) leaves just the weighted integrals of those functions.
The inspection covers the recursive definition, the weights in the orbit averages and the normalization on a curve.
It uses the authors' cited integrability of the Green functions. [Section 4.2, equations (4.2)–(4.4), pages 15–16](../../../literature/pdf/BS26.pdf#page=15)
