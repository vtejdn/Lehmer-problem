---
author: Yin
---

<a id="yua08-u001"></a>
<a id="yuan-equidistribution"></a>
# Geometric equidistribution of small points on a projective curve

In Section 3.1 of the [published article](readme.md), pp. 635–637, Yuan fixes a number field \(K\), a projective variety \(X/K\), an ample line bundle \(L\) with a semipositive adelic metric, and an embedding \(\overline K\hookrightarrow\mathbf C_v\) at each place \(v\), where \(\mathbf C_v\) is the completed algebraic closure of \(K_v\).
For a curve, Theorem 3.1 says that the orbit measures of a generic small sequence converge weakly on \(X^{\rm an}_{\mathbf C_v}\) to \(c_1(\overline L)_v/\deg L\).
At a finite place this is the geometric Berkovich space and the numerator is the Chambert-Loir measure of total mass \(\deg L\).
Section 3.3 proves the finite-place result for the space over \(K_v\) using approximation by model functions, and the passage over finite extensions at the end of Section 3.1 gives the geometric result.

<a id="small-generic-orbits"></a>
## Smallness, genericity and orbit measures

For an algebraic point \(P\), the measure places mass \(1/[K(P):K]\) at each of its distinct \(K\)-conjugates under the fixed embedding.
Weak convergence means convergence of the integrals of every continuous test function on this compact analytic space.
A sequence is generic if each proper closed subvariety contains only finitely many of its terms.
On a geometrically integral curve, pairwise distinct geometric points suffice, since every proper closed subset is finite.
Smallness means that the point heights approach the normalized variety height, which on a curve is \(\widehat c_1(\overline L)^2/(2\deg L)\) in Yuan's normalization.

## Checking a finite pullback

Let \(f:X\to\mathbf P^1_K\) be a fixed finite morphism of degree \(d>0\) from a smooth geometrically integral projective curve, with \(\overline L=f^*\overline{\mathcal O(1)}\) for the standard adelic maximum metric.
The line bundle has degree \(d\), hence is ample, and pullback preserves semipositivity by pulling back the relatively nef model metrics that approximate the target metric.
The maximum metric is canonical for \([u:v]\mapsto[u^m:v^m]\), \(m\ge2\), by the identity \(\max(|u|^m,|v|^m)=\max(|u|,|v|)^m\) at each place.
Section 3.5, p. 647, gives height zero to the full variety with this dynamical metric.
By the arithmetic projection formula the pullback self-intersection is \(d\) times the target self-intersection, so the normalized height of \(X\) is zero as well.
Point heights pull back as \(h_{\overline L}(P)=h_{\overline{\mathcal O(1)}}(f(P))\), so tending to zero verifies smallness here.
Over \(K=\mathbf Q\) the target point height is the usual absolute logarithmic Weil height.
At a finite place the standard target model has one multiplicity-one special-fibre component with line-bundle degree one, giving unit mass at its Gauss point by the model formula in Section 3.3, pp. 642–643.
Theorem 3.1 supplies the normalized curvature measure on the source.
Identifying its individual atoms for a specified map requires the local geometry of that map.

On 2026-11-20 the theorem, its definitions, the finite-place proof interface and the canonical-height normalization were inspected in the published edition.
The arithmetic projection formula and the full proof of equidistribution are used at the level of established results.
