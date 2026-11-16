---
author: Yin
---

# Cyclic norm transfer when the Pisot seed and the Salem degree both grow

<a id="statement"></a>
## Uniform transfer to the original algebraic unit

Fix \(1<\theta_0\le\Theta<\infty\).
Let \(f\) be the monic minimal polynomial of any Pisot unit \(\theta\in[\theta_0,\Theta]\) coprime to its reversal \(g=z^rf(1/z)\), where \(r=\deg f\).
For either sign \(\sigma\) put \(D=z^N f-\sigma g\).
There is an \(N_0(\theta_0)\), independent of \(r\), for which all \(N\ge N_0\) give a unique irreducible nontorsion factor \(S\), with a single exterior root.
Write \(d=\deg S,\ H=D/S,\ k=N-d,\ a=\max(k,0),\ b=\max(-k,0)\).
For every fixed positive integer \(j\), set
\[
  C_{jd}=|\operatorname{Res}(S,z^{jd}-1)|,\qquad
  V=(z^a f)^j-(\sigma z^b g)^j,\qquad m=\log M .
\]
Then \(0\le\deg H\le12r,\ -r\le k\le11r\), and
\[
  \left|\log C_{jd}-d\,m(V)\right|
       \le C_{j,\Theta}\,r^3\log(2r)\log(2d).                          \tag{1}
\]
The estimate allows the seed, its degree, its coefficients, the delay, and all cyclotomic multiplicities to change together.

In particular, fix \(K\ge0\) and suppose \(k\ge-K\).
One can choose a single \(j=j(\theta_0,\Theta,K)\) such that for every sequence in this range with \(N,d\to\infty\) and
\[
                   r^3\log(2r)\log(2d)=o(d),
\]
one has \(\log C_{jd}\ge d(\log2+1/2)\) eventually.
Thus the integer norm at this multiple of the original degree certifies \(m(S)\ge 1/(2j)\).
For all offsets, including arbitrarily negative ones, the fixed choice \(j=8\) gives
\[
       \log C_{8d}\ \ge\ c\,d/\log^3(2r)
          - C_{\Theta}\,r^3\log(2r)\log(2d) .                           \tag{2}
\]
In particular the error in (2) is smaller than half the first term eventually if \(r\le d^{1/3-\epsilon}\) for fixed \(0<\epsilon<1/3\).
The lower rate in (2) can decrease with the seed degree.

<a id="cofactor"></a>
## A uniform cutoff and a linear bound on the full torsion cofactor

On \(|z|=R=(1+\theta_0)/2\) one has
\[
 |f(z)/g(z)|\ge \frac{\theta_0-R}{R\theta_0-1}.
\]
Indeed for every interior root \(u\), \(|z-u|\ge|1-\bar u z|\) since the difference of the squares is \((R^2-1)(1-|u|^2)>0\).
The exterior factor has minimum \((\theta-R)/(R\theta-1)\) at \(z=R\), and this ratio increases with \(\theta\).
The factors of the real polynomial may be paired by conjugation in the denominator.
The resulting inequality in cross-multiplied form holds also at zeros of \(g\).
Take \(N_0\) large enough that the displayed lower bound times \(R^{N_0}\) exceeds one.
Rouché's theorem on this circle gives one root of \(D\) outside it, and \(D(R)<0\) shows that this root is real and positive.
On the unit circle the comparison with \(z^Nf-t\sigma g\) for \(0<t<1\), followed by \(t\uparrow1\), gives at most one exterior root counted with multiplicity.
Reciprocity up to sign, the unit constant, and Kronecker's theorem now give \(D=HS\) with \(H\) monic cyclotomic in all its factors, as in the [fixed-seed argument](../ledger/Yin_L_G0462_v27.md#fixed-seed-return).

For the torsion roots of \(D\) the same argument compares \(G=g/f\) at \(z\) and at \(\xi z^u\), for \((\xi,u)=(1,2),(-1,2),(-1,1)\).
For each of the three possibilities the polynomial obtained by clearing \(G(\xi z^u)=\xi^N\sigma^{u-1}G(z)^u\) has degree at most \(2ur\).
Each is nonzero by the unique exterior pole \(\theta\) of \(G\): the exterior poles of the left side have modulus \(\sqrt{\theta}\) if \(u=2\), and its exterior pole for \(u=1\) is \(-\theta\).
Thus the total number of distinct torsion roots is at most \(10r\), and each has degree at most \(4r\).
Every order is at most \(32r^2\), by \(m\le2\varphi(m)^2\).
At a torsion root of multiplicity \(v\), the logarithmic derivative of \(z^N f/g\) vanishes to order \(v-1\) if \(v>1\).
Its numerator after multiplication by \(zfg\) is
\[
                  Nfg+z(f'g-fg').
\]
This polynomial has degree at most \(2r\) and its constant term is nonzero.
It accounts for all excess multiplicities, proving \(\deg H\le12r\) and the stated bounds on \(k=\deg H-r\).

<a id="distances"></a>
## Uniform estimates at the phase roots

For \(w^j=1\) let \(Q_w=wz^a f-\sigma z^b g\).
These nonzero polynomials have degree at most \(12r\) and product \(\pm V\).
On the unit circle \(|Q_w|\le2|f|\), so \(M(Q_w)\le2\Theta\) by the integral formula, and \(m(V)\le j\log(2\Theta)\).
Every nonzero root \(v\) of any \(Q_w\) has degree \(O_j(r)\) and absolute logarithmic Mahler measure of its primitive minimal polynomial at most \(j\log(2\Theta)\), by integral factorization of \(V\).
A torsion root therefore has order \(O_j(r^2)\).
Among all distinct torsion points used below with such orders, chordal distances are at least \(c_j/(2r)^4\) in the ordinary complex absolute value, by taking a common denominator for the two arguments.

For a nontorsion \(v\), invert \(v,w\) if \(|v|>1\) and remove the resulting factor \(|v|^d\) from \(|v^d-w|\).
For \(0<|v|\le1\) the factorization of \(v^{jd}-1\) gives \(|v^d-w|\ge |v^{jd}-1|/j\).
If \(|v|^{jd}\le1/2\) this is at least \(1/(2j)\).
Otherwise the [two-logarithm estimate](Yin_C_G0895_v2.md#circle) applied to \(v\) and \(-1\) bounds \(\log|1-v^{jd}|\) below by \(-C_{j,\Theta} r^2\log(2r)\log(2d)\).
Indeed its proof bounds the logarithm of that distance directly using the nearest multiple of \(2\pi\), the field degree, the minimal-polynomial measure, and the positive integer exponent.
The upper distance bound is two after normalization.
For torsion \(v\) with \(v^d\ne w\), the same logarithmic error bound follows from the order bound, and \(v=0\) gives distance one.
Thus for every root away from \(v^d=w\) the logarithm of the distance equals \(d\log\max(1,|v|)\) with error \(O_{j,\Theta}(r^2\log(2r)\log(2d))\).

<a id="transfer"></a>
## Removing shared torsion roots without losing uniformity

Write \(Y_w=\{y:y^d=w\}\) and \(E_w=\{y\in Y_w:H(y)=0\}\).
At these sample points \(Q_w(y)=y^bD(y)\), so the roots of \(Q_w\) in \(Y_w\) are exactly \(E_w\).
Let \(l_w\) be the leading coefficient of \(Q_w\), \(G_w=\prod_{\eta\in E_w}(z-\eta)\), and write \(Q_w=U_w\prod_{\eta\in E_w}(z-\eta)^{t_\eta}\) with \(t_\eta\) the multiplicity in \(Q_w\).
The division is by a monic polynomial invariant over \(\mathbb Q(w)\); \(G_w,U_w\) have algebraic integer coefficients there.
They are relatively prime.
The product of \(\operatorname{Res}(U_w,G_w)\) over all \(j\)-th roots \(w\) is a nonzero rational integer by Galois invariance.
At the upper end \(|\operatorname{Res}(U_w,G_w)|\le 2^{\deg U_w\,|E_w|}M(U_w)^{|E_w|}\), and \(M(U_w)=M(Q_w)\le2\Theta\).
Consequently the logarithm of the absolute product of these resultants lies between zero and \(O_{j,\Theta}(r^2)\).

Taking the product of \(Q_w\) over \(Y_w\setminus E_w\) gives exactly
\[
 \frac{|l_w|^d\,\prod_{U_w(v)=0}|v^d-w|}
      {|\operatorname{Res}(U_w,G_w)|}
 \prod_{\eta\in E_w}
       \left(\frac{d}{\prod_{\xi\in E_w,\ \xi\ne\eta}|\eta-\xi|}\right)^{t_\eta}
\]
in absolute value.
The last factors use the derivative of \(z^d-w\) at the omitted points.
Their total logarithmic size in absolute value is \(O_j(r\log(2d)+r^2\log(2r))\) by the torsion separation and the degrees of the \(Q_w\).
Summing the preceding distance bounds over the \(O_j(r)\) roots of the \(U_w\), and restoring the leading coefficients, gives \(d\,m(V)\) with the error in (1).

It remains to replace the values of \(D\) by those of \(S\).
Put \(E=\bigcup_w E_w\).
For each root \(\eta\) of \(H\), its product of distances from the retained \(jd\)-th roots of unity is
\[
 \frac{|\eta^{jd}-1|}{\prod_{\xi\in E}|\eta-\xi|}\quad(\eta\notin E),
 \qquad
 \frac{jd}{\prod_{\xi\in E,\ \xi\ne\eta}|\eta-\xi|}\quad(\eta\in E).
\]
The nonzero numerator in the first expression has logarithm of absolute size \(O(\log(2r))\), by the order of \(\eta\).
With multiplicities, removing these \(H\) factors changes the logarithm by \(O_j(r\log(2d)+r^2\log(2r))\).
Restoring the omitted \(S\) factors contributes the logarithm of a nonzero absolute integer resultant since \(E\) is Galois-stable.
It is nonnegative.
For a root \(\eta\in E\) of multiplicity \(v\) in \(H\), its value \(|S(\eta)|\) is \(|D^{(v)}(\eta)|/v!\) divided by the product of distances from the other roots of \(H\), counted with multiplicity.
The derivative divided by \(v!\) is bounded by \(2^{r+1}\Theta(N+r)^v\), since the coefficient sum in absolute value of \(f\) is at most \(2^r M(f)\).
Using the torsion separation, \(\sum_{\eta\in E}v\le12r\), and \(N+r=d+\deg H\), the restored logarithm is at most \(O_{j,\Theta}(r\log(2d)+r^2\log(2r))\).
This proves (1) for the complete resultant on the original irreducible polynomial.

<a id="rates"></a>
## Positive norm mass and its range

The [uniform phase theorem](../ledger/Yin_L_G0462_v26.md#uniform-phase) permits one fixed \(j\) with \(m(V)>\log2+1\) throughout the compact seed interval and \(k\ge-K\).
Insert this in (1) and use \(C_{jd}\le 2^d M(S)^{jd}\) to obtain the first positive-rate assertion.
For the [eight-phase theorem](../ledger/Yin_L_G0462_v27.md#eight-phases), every \(V\) at \(j=8\) has \(M(V)>1\).
If its leading coefficient has modulus greater than one, then \(m(V)\ge\log2\).
Otherwise it has a monic nontorsion irreducible factor of positive measure after removing powers of \(z\).
The [polylogarithmic Dobrowolski bound](Yin_C_G0895_v1.md#transfer) gives \(m(V)\ge c/\log^3(2r)\) since \(\deg V=O(r)\), with a smaller absolute constant covering the bounded degrees.
Equation (1) gives (2).
The transfer requires a representation by a Pisot seed; the statements do not supply a representation or an exponent with uniform positive rate for arbitrary noncyclotomic inputs.

## Assessment history

### Decision growing-seed-transfer

| Field | Value |
| --- | --- |
| date | 2026-11-16T12:14 |
| status | open |
| reason | Submit the uniform seed-degree error, full cofactor accounting and the original-unit consequences for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Moving inputs](#statement) | Both signs, variable seed and delay, an explicit error order, bounded-below offsets and all-offset eightfold income. |
| argument | [Torsion multiplicity](#cofactor) | Uniform exterior-root cutoff, degree and orders of torsion roots, and derivative count at repeated roots. |
| argument | [Distances](#distances) | Degree and height control at every phase root, and uniform logarithmic distance. |
| argument | [Original resultant](#transfer) | All common torsion cancellations, integer conjugate products, and restored derivative terms. |
| argument | [Rates](#rates) | Jointly varying original inputs, uniform gap on bounded-below offsets and weaker eightfold rate elsewhere. |
| dependency | [Uniform phase estimate](../ledger/Yin_L_G0462_v26.md#uniform-phase) | Bounded seed measures and bounded-below offsets, all large fixed multipliers. |
| dependency | [Eightfold positivity](../ledger/Yin_L_G0462_v27.md#eight-phases) | All offsets of a genuine nonreciprocal Pisot seed. |
| dependency | [Complex logarithms](../audits/literature/Wus02/Yin_U001.md#wus02-u001) | Fixed two-logarithm theorem with the actual variable degree, minimal-polynomial height and integer exponent. |
| dependency | [Weak degree bound](Yin_C_G0895_v1.md#transfer) | Polylogarithmic bound on the positive measure of an irreducible factor. |


### Decision moving-seed-transfer-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T12:32 |
| status | proved |
| reason | Adopt the uniform transfer to the original Salem polynomial and both growth bounds after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Moving inputs](#statement) | Both signs, variable seed and delay, an explicit error order, bounded-below offsets and all-offset eightfold income. |
| argument | [Torsion multiplicity](#cofactor) | Uniform exterior-root cutoff, degree and orders of torsion roots, and derivative count at repeated roots. |
| argument | [Distances](#distances) | Degree and height control at every phase root, and uniform logarithmic distance. |
| argument | [Original resultant](#transfer) | All common torsion cancellations, integer conjugate products, and restored derivative terms. |
| argument | [Rates](#rates) | Jointly varying original inputs, uniform gap on bounded-below offsets and weaker eightfold rate elsewhere. |
| dependency | [Uniform phase estimate](../ledger/Yin_L_G0462_v26.md#uniform-phase) | Bounded seed measures and bounded-below offsets, all large fixed multipliers. |
| dependency | [Eightfold positivity](../ledger/Yin_L_G0462_v27.md#eight-phases) | All offsets of a genuine nonreciprocal Pisot seed. |
| dependency | [Complex logarithms](../audits/literature/Wus02/Yin_U001.md#wus02-u001) | Fixed two-logarithm theorem with the actual variable degree, minimal-polynomial height and integer exponent. |
| dependency | [Weak degree bound](Yin_C_G0895_v1.md#transfer) | Polylogarithmic bound on the positive measure of an irreducible factor. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G0556_v4.md#moving-seed-transfer) | Full variable-seed proof, including the exterior cutoff, repeated torsion factors, uniform logarithmic errors and the two quantitative consequences. |

## Current assessment
[Selected decision](#decision-moving-seed-transfer-reviewed)
