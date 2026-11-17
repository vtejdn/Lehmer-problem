---
author: Yin
---

# Quantitative torsion collisions in rational relations

This continuing calculation for [G0001](../tasks/Yin_T_G0001_v1.md#contract) gives a quantitative version of [C345v300's tuple criterion](../claims/Yin_C_G0345_v300.md#statement).
The coordinating agent proposed the normalized radial comparison and the reflected-discriminant angular argument.
The agent-S contributor checked the arbitrary-number normalization, used the retained Voutier bound to recover the logarithmic refinement, and supplied the explicit constants and output costs below.
These are author calculations awaiting independent review, not an adopted fixed theorem.

<a id="statement"></a>
## A bound depending on the actual number of terms

All logarithms are natural, and \(h\) denotes absolute logarithmic Weil height.
For every integer \(s\ge2\), put
\[
 L_s=\log(4s),\qquad
 \tau_s=e^{-100}\frac{(\log L_s)^3}{s^2L_s^4}.
                                                               \tag{1}
\]
Suppose \(u_1,\ldots,u_s\) are nonzero algebraic numbers and
\[
 \sum_{i=1}^s c_i u_i=0,\qquad c_i\in\mathbb Q^*,\qquad
 H=\max_i h(u_i/u_1).
                                                               \tag{2}
\]
Then at least one of the following holds:

1. Some \(u_i/u_j\), with \(i\ne j\), is a root of unity of order at most \(32s^2\).
2. \(H>\tau_s\).

The number of terms may grow.
There is no restriction on the rational coefficients, their heights or denominators, the individual heights \(h(u_i)\), or any ambient or individual field degree.
The reference term in (2) belongs to the actual support of the relation.
If instead \(\max_i h(u_i)\le H_0\), the sufficient smallness condition is \(2H_0\le\tau_s\).
The constant in (1) is deliberately conservative.
In particular the bound has the form
\[
 H\gg \frac{(\log\log(4s))^3}{s^2\log^4(4s)}
                                                               \tag{3}
\]
when the small-order torsion alternative is absent.

<a id="reuse"></a>
## Existing arguments and the exact external input

The [short-annihilator Gram argument](../claims/Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) already compares a lower phase energy with a radial error for rational relations among powers of one algebraic unit.
The [refined unit phase estimate](../claims/Yin_C_G0159_v1.md#statement) already gives a bound of order \(\sqrt u\log^2(1/u)\), including the degree of the actual power and its conjugate multiplicities.
The [reflected-discriminant calculation](../claims/Yin_C_G0345_v108.md#phases) already supplies the radial reflection and Fourier-energy mechanism for units.
The tuple and bounded-order torsion conclusion in [C345v300](../claims/Yin_C_G0345_v300.md#phase) uses qualitative one-dimensional equidistribution.
The present calculation retains that tuple scope, makes the support-size dependence explicit, includes nonintegral algebraic quotients, and obtains the factor \((\log\log(1/u))^{-3/2}\) in the angular estimate.
It does not claim a new underlying phase-orthogonality mechanism.

The only external lower-bound input used below is [Vou96-U001](../audits/literature/Vou96/Yin_U001.md#height).
For every nonzero nontorsion algebraic number of actual degree \(D\ge2\) and height \(u\), it gives
\[
 Du>\frac14\left(\frac{\log\log D}{\log D}\right)^3,
 \qquad Du>\frac{2}{\log^3(3D)}.
                                                               \tag{4}
\]
Both statements apply to arbitrary algebraic numbers, not only algebraic integers or units.
Their accepted source scope is the statement and applicability inspection of the identified author manuscript, pp. 1 and 3–4; its original determinant proof and numerical parameter verification are not newly audited here.
The [absolute-height normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) includes the positive leading coefficient of the primitive minimal polynomial and the finite-place contributions.
The proof below does not use Bilu or an independent quantitative equidistribution theorem as an additional premise.

<a id="phase-degree"></a>
## Angular mean from a primitive polynomial discriminant

Let \(x\ne0\) be algebraic of degree \(D\ge2\), with primitive irreducible polynomial
\[
 P(X)=a\prod_{i=1}^D(X-z_i),\qquad a\in\mathbb Z_{>0},
 \qquad u=h(x).
\]
Write
\[
 r_i=|z_i|,\quad p_i=z_i/r_i,\quad m_i=\max(1,r_i),\quad
 w_i=\min(r_i,r_i^{-1})p_i.
\]
For distinct indices,
\[
 \frac{|z_i-z_j|}{m_i m_j}\le |1-\overline w_iw_j|.
                                                               \tag{5}
\]
If both radii are at most one, the difference of the squared right and left sides is \((1-r_i^2)(1-r_j^2)\).
If both exceed one, the same calculation uses their inverse radii.
For one radius on each side of one, the two sides are equal.
For \(|z|\le1\) and \(0<t<1\),
\[
 |1-z|\le t^{-1/2}|1-tz|,
\]
since \(|1-tz|^2-t|1-z|^2=(1-t)(1-t|z|^2)\ge0\).
The integer discriminant of \(P\) is nonzero.
Consequently (5) gives
\[
 \begin{aligned}
 0&\le (2D-2)\log a+\sum_{i\ne j}\log|z_i-z_j|\\
  &\le 2D(D-1)u+
       \sum_{i\ne j}\log|1-t\overline w_iw_j|
           -\frac{D(D-1)}2\log t .
 \end{aligned}                                                   \tag{6}
\]
Here \(\log a+\sum_i\log m_i=Du\); dropping \(\log a\) would make (6) invalid for nonintegral inputs.
The absolutely convergent logarithmic expansion gives
\[
 \sum_{i,j}\log|1-t\overline w_iw_j|
    =-\sum_{n\ge1}\frac{t^n}{n}\left|\sum_iw_i^n\right|^2
    \le-t\left|\sum_iw_i\right|^2.
                                                               \tag{7}
\]
Each diagonal logarithm is at least \(\log(1-t)\).
Taking \(t=1-1/D\) in (6)–(7) therefore yields
\[
 \left|\frac1D\sum_iw_i\right|^2
 \le 2u+\frac{\log D}{D-1}-\frac12\log(1-1/D).
                                                               \tag{8}
\]
Height invariance under inversion and the archimedean part of height give
\[
 \frac1D\sum_i|\log r_i|\le h(x)+h(x^{-1})=2u.
\]
Since \(|p_i-w_i|\le|\log r_i|\), (8) implies
\[
 \left|\frac1D\sum_i p_i\right|
 \le 2u+\sqrt{2u+\frac{\log D}{D-1}-\frac12\log(1-1/D)}
 \le 2u+\sqrt{2u+\frac{2\log(2D)}D}.
                                                               \tag{9}
\]
The last inequality follows from \(-\log(1-1/D)\le1/(D-1)\), \(D/(D-1)\le2\), and \(1/2<\log2\).
This is a finite-degree bound with no integrality assumption on \(x\).

<a id="phase-height"></a>
## A height-only estimate, including the logarithmic refinement

Suppose now that \(x\) is nontorsion and \(0<u\le e^{-40}\).
Define
\[
 L=\log(1/u),\qquad
 \Phi(u)=8\sqrt u\frac{L^2}{(\log L)^{3/2}}.
                                                               \tag{10}
\]
Then the conjugate phase mean in (9) has absolute value at most \(\Phi(u)\).

For completeness, degree one is excluded because a nonzero rational number other than \(1,-1\) has height at least \(\log2\).
The second bound in (4) excludes \(D<e^e\): in that range \(D<27\), \(\log(3D)<7\), and hence \(u>2/(27\cdot7^3)>1/5000>e^{-40}\).
Thus \(y=\log D\ge e\).
If \(D\ge1/u\), monotonicity of \(\log(2D)/D\) gives
\[
 \frac{\log(2D)}D\le u(L+\log2)\le2uL.
\]
If \(D<1/u\), the first bound in (4), and the increase of \(y/\log y\) for \(y\ge e\), give
\[
 \frac1D<4u\left(\frac y{\log y}\right)^3
       \le4u\left(\frac L{\log L}\right)^3.
\]
In both cases,
\[
 \frac{\log(2D)}D\le8u\frac{L^4}{(\log L)^3}.
                                                               \tag{11}
\]
Since \(L^4/(\log L)^3\ge1\), substituting (11) in (9) proves (10), with the safe constant \(8>2+\sqrt{18}\).
The function \(\Phi\) increases on \((0,e^{-40}]\) and tends to zero at zero.
Indeed its logarithmic derivative with respect to \(L\) is \(-1/2+2/L-3/(2L\log L)<0\).
Set \(\Phi(0)=0\) for the limiting convention; no nontorsion number has height zero.

<a id="torsion"></a>
## Torsion and common-field averages

For a primitive root of unity \(\zeta\) of order \(k\), the average of its conjugates is
\[
 \mathbb E\operatorname{ph}(\zeta)=\frac{\mu(k)}{\varphi(k)},
 \qquad
 \left|\mathbb E\operatorname{ph}(\zeta)\right|
                \le\sqrt{2/k}.
                                                               \tag{12}
\]
The conjugate sum is \(\mu(k)\): grouping all \(k\)-th roots according to exact order and applying Möbius inversion proves this formula, including \(k=1\).
The elementary inequality \(\varphi(k)^2/k\ge1/2\) follows by multiplying the factors \(p^{a-2}(p-1)^2\) for \(p^a\Vert k\).
Every odd-prime factor is at least one, and the only factor below one is \(1/2\) from \(2^1\).

Give the embeddings of any number field containing the numbers under discussion equal probability.
Restriction to the field generated by one number gives every conjugate with the same multiplicity.
Therefore (9)–(12) apply to that common-field average using the degree of the actual number, even when a quotient or a power has smaller degree than the original inputs.
For two nonzero numbers \(v_i,v_j\), their phase Gram entry is precisely
\[
 \mathbb E\!\left[
 \operatorname{ph}(\sigma v_i)\overline{\operatorname{ph}(\sigma v_j)}
 \right]=\mathbb E\operatorname{ph}(\sigma(v_i/v_j)).
                                                               \tag{13}
\]

<a id="gram"></a>
## The radial and Gram bounds for arbitrary tuples

Put \(v_i=u_i/u_1\), so \(v_1=1\).
Normalize the original rational coefficients by their real Euclidean norm:
\[
 a_i=\frac{c_i}{(\sum_jc_j^2)^{1/2}},\qquad\sum_i a_i^2=1.
\]
The normalized coefficients need not be rational.
Nevertheless every embedding satisfies \(\sum_i a_i\sigma(v_i)=0\), because it first fixes the original rational coefficients and one then divides by the same real scalar.
At an embedding let \(r_i=|\sigma(v_i)|\), \(p_i=\operatorname{ph}(\sigma v_i)\), and \(M=\max(1,r_1,\ldots,r_s)\).
The exact relation divided by \(M\), followed by Cauchy–Schwarz, gives
\[
 \left|\sum_i a_i p_i\right|^2
 =\left|\sum_i a_i(1-r_i/M)p_i\right|^2
 \le\sum_i(1-r_i/M)^2
 \le\sum_i(\log M-\log r_i).
                                                               \tag{14}
\]
Here \((1-t)^2\le-\log t\) for \(0<t\le1\).
Since \(\mathbb E\log M\le\sum_i h(v_i)\) and \(-\mathbb E\log r_i\le h(v_i^{-1})=h(v_i)\),
\[
 \mathbb E\left|\sum_i a_i p_i\right|^2
 \le(s+1)\sum_i h(v_i)\le(s^2-1)H.
                                                               \tag{15}
\]
This bound uses no positive radial moment and no coefficient-height bound.

If all off-diagonal entries (13) have absolute value at most \(\epsilon\), then
\[
 \mathbb E\left|\sum_i a_i p_i\right|^2
 \ge1-\epsilon\sum_{i\ne j}|a_i a_j|
 \ge1-(s-1)\epsilon.
                                                               \tag{16}
\]
Every quotient has height at most \(2H\).
If there is no torsion quotient of order at most \(32s^2\), (10) and (12) allow
\[
 \epsilon=\max\{\Phi(2H),1/(4s)\},\qquad 0<2H\le e^{-40}.
                                                               \tag{17}
\]
Equations (15)–(17) are a finite, parameter-dependent necessary test before the explicit simplification (1).
If \(H=0\), every quotient is torsion by the height-zero characterization; use only (12), (15) and (16), without applying (10) to a nontorsion number of height zero.

<a id="constants"></a>
## Checking the explicit support threshold

Assume that no small-order torsion quotient exists and \(0<H\le\tau_s\).
Write \(L_s=L_0>2\), and set
\[
 L_* =\log(1/(2\tau_s))
 =100-\log2+2\log s+4\log L_0-3\log\log L_0.
\]
One has
\[
               2\tau_s<e^{-40},\qquad L_0\le L_*\le60L_0.
                                                               \tag{18}
\]
For the lower bound, \(2\log s=2L_0-2\log4>2L_0-4\), and \(4y-3\log y>0\) for \(y=\log L_0>0\), using \(\log y\le y-1\).
For the upper bound, \(\log L_0>\log2>1/2\) gives \(-3\log\log L_0<3\), while \(2\log s\le2L_0\) and \(4\log L_0\le4L_0\).
Thus \(L_*<103+6L_0<60L_0\).
Also \((\log L_0)^3/L_0^4\le1/L_0<1/2\), which proves the first assertion of (18).
By monotonicity and (18),
\[
 \Phi(2H)\le\Phi(2\tau_s)
 \le\frac{8\sqrt2\,60^2 e^{-50}}s<\frac1{4s}.
                                                               \tag{19}
\]
The last numerical inequality follows already from \(e^{50}>2^{50}>230400\) and \(\sqrt2<2\).
Thus (16) exceeds \(3/4\), whereas (15) is at most
\[
 (s^2-1)\tau_s<e^{-100}\frac{(\log L_0)^3}{L_0^4}<1/4.
\]
This is a contradiction.
For \(H=0\), (15) is zero while the torsion-only version of (16) exceeds \(3/4\).
This proves the alternative in (1)–(2).

<a id="output"></a>
## Quantitative cost for a sparse algebraic output

Let \(\Gamma\) be a multiplicative group of nonzero algebraic numbers, and suppose an actual relation is
\[
 \sum_{i=1}^s c_i a_i y^{k_i}=0,\qquad
 c_i\in\mathbb Q^*,\quad a_i\in\Gamma,\quad k_i\in\mathbb Z,
 \quad y\ne0.
                                                               \tag{20}
\]
Assume that equal powers \(k_i=k_j\) never have \(a_i/a_j\) torsion of order at most \(32s^2\).
If
\[
 \max_i\left(h(a_i/a_1)+|k_i-k_1|h(y)\right)\le\tau_s,
                                                               \tag{21}
\]
then (1)–(2) give
\[
 y^{k_i-k_j}=\zeta\,a_j/a_i,
 \qquad k_i\ne k_j,\qquad \operatorname{ord}(\zeta)\le32s^2.
                                                               \tag{22}
\]
Thus \(y\) belongs to the radical saturation \(\widetilde\Gamma\) used in [C345v300](../claims/Yin_C_G0345_v300.md#sparse-output).
If \(K=\max_{i,j}|k_i-k_j|\), raising (22) to the torsion order gives an actual power of \(y\) in \(\Gamma\), with nonzero exponent of absolute value at most \(32s^2K\).
The same-power condition is necessary: a relation involving a single power of \(y\) could vanish identically after its coefficients are evaluated.
The faithful collection of values in C345v300 must therefore precede this test; \(s\) here is the number of surviving nonzero terms.

More explicitly, write \(a_i=\prod_j\alpha_j^{n_{ij}}\).
A sufficient budget in (21) is
\[
 \max_i\left(\sum_j|n_{ij}-n_{1j}|h(\alpha_j)
                       +|k_i-k_1|h(y)\right)\le\tau_s.
                                                               \tag{23}
\]
For roots of a monic irreducible unit polynomial \(P\) of degree \(d\) and total logarithmic measure \(\mu\), all \(h(\alpha_j)=\mu/d\).
If \(A=\max_i\sum_j|n_{ij}-n_{1j}|\) and \(B=\max_i|k_i-k_1|\), a sufficient form of (23) is
\[
                       A\mu/d+B h(y)\le\tau_s.
                                                               \tag{24}
\]
For the absolute exponent bounds \(\sum_j|n_{ij}|\le L\), \(|k_i|\le K\) in [C345v300's height budget](../claims/Yin_C_G0345_v300.md#height-budget), the sufficient condition is \(2(L\mu/d+K h(y))\le\tau_s\).
It is uniform in growing support precisely when this explicitly shrinking threshold is paid.

Under the additional full-permutation real-circuit hypotheses of [C345v299](../claims/Yin_C_G0345_v299.md#saturation), (22) lets one apply its existing exterior-count obstruction.
Every nontorsion output then has at least three exterior conjugates, and more precisely at least \(\nu(e)\) as stated there.
This consequence remains conditional on the input and its specified action; no shrinking input sequence or unrestricted Mahler gap is constructed.
For a nontorsion output with at most two exterior conjugates and a faithful collected relation satisfying the same-power condition, the necessary escape is that the actual left side of (21) exceeds \(\tau_s\).
Equations (23)–(24) are sufficient upper budgets for that left side, not lower bounds on it.

<a id="powers"></a>
## Powers, degree drops and the remaining limitation

Taking powers does not preserve the small height for free.
For every integer \(n\ne0\), \(h(x^n)=|n|h(x)\), so the angular estimate for that power must use \(u=|n|h(x)\) and its actual minimal-polynomial degree.
Averaging its phases over the original conjugates is legitimate because the restriction multiplicities are equal, not because the degree stays unchanged.
For all frequencies \(1\le|n|\le N\), a common bound is \(\Phi(Nh(x))\) when \(0<Nh(x)\le e^{-40}\) and \(x\) is nontorsion.
If \(x\) has torsion order \(k\), its \(n\)-th power has order \(k/\gcd(k,n)\); the sufficient exclusion \(k>32s^2N\) keeps all these power orders above \(32s^2\).
One cannot deduce a relation among the powered terms from an unpowered relation without a separate algebraic identity.

In particular, powers through \(N\) of a degree-\(d\) root of total measure \(\mu\) cost \(N\mu/d\).
If \(N\) is a fixed positive multiple of \(d\), this cost has order \(\mu\), rather than \(\mu/d\).
Growing support additionally costs the threshold (1).
The new content here is the arbitrary-tuple quantitative alternative and its faithful-output budget.
No separate small-term minimal-polynomial lower-bound corollary is asserted, and no comparison with the stronger specialized fewnomial results is needed as a premise.
Dense encodings or encodings exceeding (21) remain outside this argument.
