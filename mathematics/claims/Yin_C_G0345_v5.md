---
author: Yin
---

# A strict moment bound for positive-constant Pisot polynomials near their norm

<a id="statement"></a>
## No saturated nonzero moment on the square-root window

Let \(f\) be a Pisot minimal polynomial with positive constant \(q\ge2\), exterior root \(\theta\), reversal \(g=f^*\) and \(D=zf+g\).
Use the [integer-series normalization](../ledger/Yin_L_G0462_v36.md#limit)
\[
 K_q(z)=\frac{(1-z^2)^2}{z}\left(\frac{f(z)}{D(z)}-
                         \frac{q-z}{1-z^2}\right)=j+\sum_{k\ge1}A(k)z^k,
 \qquad A(0)=2j,\quad A(-k)=A(k).
\]
For every fixed integer \(j\ge1\) there is a constant \(c_j>0\) such that every such input with \(K_q(0)=j\) and sufficiently large \(q\) satisfies
\[
                       |A(k)|\le2j-1\qquad(1\le k\le c_j\sqrt q).      \tag{1}
\]
Consequently every subsequential limit of the [normalized radial-deficit measures](../ledger/Yin_L_G0462_v36.md#weights) on this branch has an absolutely continuous component of mass at least \(1/(2j)\).
For \(j=1\) the complete remaining possibilities for this probability measure are normalized arclength, the density \(1\pm\cos(k t)\) against normalized arclength for \(k\ge1\), or equal parts normalized arclength and the uniform measure on \(z^h=\pm1\) for an integer \(h\ge1\).
The theorem does not establish realizability of these remaining limits.
The main researcher derived the recurrence obstruction and the finite window, and agent-S supplied the ordinary Schur reduction and uniqueness argument used below.

<a id="reflection"></a>
## Saturation forces reflection as well as translation

Write \(\lambda_q\) for the probability measure of the [finite moment comparison](../ledger/Yin_L_G0462_v39.md#coefficient-window) and \(M(k)=2j\int v^k\,d\lambda_q(v)\).
For \(n=\lfloor b\sqrt q\rfloor\) with small fixed \(b>0\), this comparison gives \(|A(k)-M(k)|\le E=C_j(1+n^2)/q\) throughout \(|k|\le n\).
Choose \(b\) within the stated range and sufficiently small that \(2E+2\sqrt{jE}<1\) for all large \(q\).
In particular \(|A(k)|\le2j\) throughout the window by integrality.
Suppose \(1\le L\le n/2\) and \(A(L)=2j\tau\), where \(\tau=\pm1\).
Then \(\int |v^L-\tau|^2\,d\lambda_q\le E/j\).
Cauchy–Schwarz gives \(|M(k+L)-\tau M(k)|\le2\sqrt{jE}\) for every integer \(k\).
For \(|k|,|k+L|\le n\), integrality therefore gives the exact equality \(A(k+L)=\tau A(k)\).
In particular \(A(L-k)=\tau A(k)\) for \(1\le k<L\).

Form the rational function
\[
 K_*(z)=\frac{j(1+\tau z^L)+\sum_{k=1}^{L-1}A(k)z^k}{1-\tau z^L} .
\]
It agrees with \(K_q\) in Taylor degrees zero through \(n\) by the recurrence, and the reflection identity gives \(K_*(1/z)=-K_*(z)\).
This step requires no positivity for the periodic extension.

<a id="schur"></a>
## Uniqueness from a finite Schur interpolation problem

For \(K=K_q\) or \(K_*\), put
\[
 Y=\frac{q-z}{1-z^2}+\frac{zK}{(1-z^2)^2},\qquad
 F=\frac{Y}{1-zY},\qquad S=\frac{z(qF-1)}{F-q} .
\]
The common constant \(K(0)=j\) gives \(F(0)=q\), \(F'(0)=q^2-1+j\ne0\), so \(S\) is regular at zero.
For \(K_q\), \(F=f/g\) and \(S=z(qf-g)/(f-qg)\) is a Schur function (holomorphic in the unit disk and bounded there by one).
Indeed \(g\) has just one disk zero, \(1/\theta\), and \(|qg|>|f|\) on the circle because \(|g|=|f|>0\) there.
By Rouché's theorem \(f-qg\) has one disk zero with multiplicity, located at zero and canceled by the numerator.
On the circle \(|qf-g|=|f-qg|\), so boundedness follows from the maximum principle.

For \(K_*\), mark the corresponding functions by stars as subscripts.
Antisymmetry gives \(Y_*(1/z)=z-z^2Y_*(z)\) and hence \(F_*(1/z)F_*(z)=1\), \(S_*(1/z)S_*(z)=1\) as rational identities.
The formulas use real coefficients, so the reduced rational function \(S_*\) has modulus one on the circle and has no zero or pole there, by continuity of its modulus along the punctured circle.
It is a quotient \(\alpha/\beta\) of finite Blaschke products, allowing unimodular constants: multiply by the Blaschke factors of its poles in the disk, then divide by the Blaschke factors of its remaining zeros there.
The resulting analytic nonvanishing function and its reciprocal have modulus one on the boundary, so it is constant.
The degree of \(\alpha\) is at most \(L+6\), since the numerator and denominator of \(K_*\) have degree at most \(L\), those of \(Y_*\) at most \(L+4\), and the last two rational operations each increase that bound by at most one.
The Blaschke factors used to cancel poles add no interior zeros after cancellation with the poles, so the same degree bound applies to the numerator Blaschke product.

The agreement of \(K_q\) and \(K_*\) through degree \(n\) gives \(Y-Y_*=O(z^{n+2})\), then \(F-F_*=O(z^{n+2})\) and \(S-S_*=O(z^{n+1})\); the last step divides by two functions with simple zeros and has one compensating factor \(z\).
Thus the Schur function \(S\beta\) agrees with \(\alpha\) through degree \(n\).
A finite Blaschke product of degree \(a\) is the only Schur function with its Taylor coefficients through degree \(a\).
To see this, at common constant \(w\) with \(|w|<1\) apply the Schur transformation \((H-w)/(z(1-\overline w H))\).
It preserves the Schur class by Schwarz's lemma, reduces the order of Taylor agreement by one, and lowers the Blaschke degree by one because the disk automorphism preserves that degree before the zero at the origin is removed.
At degree zero equality follows from the common unimodular constant and the maximum principle; inverting the transformations proves uniqueness.

For all large \(q\), \(L\le n/2\) implies \(L+6\le n\), so \(S\beta=\alpha\) and \(S=S_*\).
The rational transformations are injective, since \(q^2\ne1\), and give \(K_q=K_*\).
But \(K_q\) has a [genuine pole](../ledger/Yin_L_G0462_v36.md#periodic) in \((0,1)\) at the reciprocal of the exterior root of \(D\), whereas \(K_*\) has poles only at roots of unity.
This contradiction proves (1), for example with \(c_j=b/3\).

<a id="radial-limits"></a>
## Consequences for the location of radial loss

For a subsequential limit \(\mu/j\) in the radial-deficit normalization of L462v36, the [integer Fourier–Stieltjes decomposition](../ledger/Yin_L_G0462_v36.md#periodic) writes \(2\mu\) as a positive atomic part on finitely many roots of unity plus a nonnegative trigonometric-polynomial density against normalized arclength.
The Fourier sequences of both parts are integer-valued, by extending the eventual integer periodic part to all indices and taking the finitely supported difference.
Their masses are therefore nonnegative integers summing to \(2j\).
If the density had zero mass, a common multiple \(L\) of the support orders would give moment \(2j\) for \(2\mu\).
On the convergent subsequence the integer coefficient \(A(L)\) would eventually equal \(2j\), contradicting (1).
Thus the density has mass at least one before normalization by \(2j\).
For \(j=1\) the atomic mass is now zero or one and the [two corresponding cases](../ledger/Yin_L_G0462_v38.md#mass) give exactly the displayed necessary forms.
The [opposite-sign constructions](../ledger/Yin_L_G0462_v38.md#opposite-sign) show why the sign of the original constant matters to this restriction.

## Assessment history

### Decision finite-schur-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-16T13:17 |
| status | open |
| reason | Submit the strict finite coefficient window and the resulting positive continuous radial mass for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Strict finite window](#statement) | Every fixed positive branch and the consequent necessary radial distributions. |
| argument | [Reflection and recurrence](#reflection) | Uniform comparison, signed saturation and construction of an antisymmetric rational extension. |
| argument | [Schur uniqueness](#schur) | Positive-sign disk function, finite-degree interpolation, reconstruction and contradiction at the interior pole. |
| argument | [Limiting mass](#radial-limits) | At least one unit of continuous mass and the remaining first-branch shapes. |
| dependency | [Finite comparison](../ledger/Yin_L_G0462_v39.md#coefficient-window) | Uniform approximation of the integer sequence by Fourier moments up to square-root order. |
| dependency | [Integer limits and pole](../ledger/Yin_L_G0462_v36.md#periodic) | Integer periodic-plus-finite coefficient decomposition and the actual interior pole. |
| dependency | [Smallest branch](../ledger/Yin_L_G0462_v38.md#mass) | Harmonic classification when the atomic mass is zero or one. |

### Decision strict-moment-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T13:22 |
| status | proved |
| reason | Adopt the strict square-root window and the necessary continuous radial mass after independent inspection of the finite interpolation and limiting arguments. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Strict finite window](#statement) | Every fixed positive branch and the consequent necessary radial distributions. |
| argument | [Reflection and recurrence](#reflection) | Uniform comparison, signed saturation and construction of an antisymmetric rational extension. |
| argument | [Schur uniqueness](#schur) | Positive-sign disk function, finite-degree interpolation, reconstruction and contradiction at the interior pole. |
| argument | [Limiting mass](#radial-limits) | At least one unit of continuous mass and the remaining first-branch shapes. |
| dependency | [Finite comparison](../ledger/Yin_L_G0462_v39.md#coefficient-window) | Uniform approximation of the integer sequence by Fourier moments up to square-root order. |
| dependency | [Integer limits and pole](../ledger/Yin_L_G0462_v36.md#periodic) | Integer periodic-plus-finite coefficient decomposition and the actual interior pole. |
| dependency | [Smallest branch](../ledger/Yin_L_G0462_v38.md#mass) | Harmonic classification when the atomic mass is zero or one. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v5.md#strict-moment-review) | Both signs of saturation, rational cancellations, finite Schur interpolation and positive continuous mass at every fixed branch. |

## Current assessment

[Selected decision](#decision-strict-moment-reviewed)
