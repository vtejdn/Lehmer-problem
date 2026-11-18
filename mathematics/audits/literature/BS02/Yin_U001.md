---
author: Yin
---

<a id="bs02-u001"></a>
# Cyclotomic point counts in terms of Newton polygon area

<a id="newton-area"></a>
## The area bound

In Section 4.1, p. 7 of the [author edition](readme.md#editions), the unnumbered theorem concerns a nonzero complex Laurent polynomial in two variables.
Let \(V\) denote the ordinary Euclidean area of the convex hull of its exponent vectors.
If its curve has finitely many ordered pairs of roots of unity, their number is at most \(22V\).
An infinite set of such pairs forces a factor \(x^iy^j-\omega\), where \((i,j)\ne(0,0)\) and \(\omega\) is a root of unity.
The theorem also gives \(4V\) when every absolutely irreducible factor is nonreciprocal in the authors' conjugate-reciprocal convention.
It counts points of all orders and imposes no parity restriction on either coordinate.

Lemma 2 on the same page bounds the number of intersections in the two-dimensional torus for two curves with no common component by the area of the Minkowski sum of their Newton polygons minus the two individual areas.
The proof of the main theorem in Section 4.4 uses sign changes and coordinate squaring to produce intersections counted by that lemma.
The theorem statement, area convention and this proof step were checked on 2026-11-16.

<a id="intersection-multiplicities"></a>
## Torus intersections counted with multiplicity

Lemma 2 in Section 4.2, p. 7 of the [author edition](readme.md#editions), counts the distinct common zeros of two complex Laurent polynomials \(f,g\) whose curves have no common component.
The proof on p. 8 gives a bound on the sum of their local intersection multiplicities \(i_z(f,g)\) over all common zeros in \(T=(\mathbb C^\times)^2\).
Writing \(P,Q\) for the respective Newton polygons and \(V\) for ordinary Euclidean area, the bound is
\[
\sum_{\substack{z\in T\\ f(z)=g(z)=0}} i_z(f,g)
\le V(P+Q)-V(P)-V(Q).
\]
Beukers and Smyth identify the right side with twice the mixed volume in their convention and invoke Fulton's strengthening of the Bernstein–Kouchnirenko–Khovanskii bound, citing [F], p. 122.
Their special case assumes that \(g\) has the same support as \(f(x^k,y^k)\) for a positive integer \(k\).
Then \(Q=kP\), so the mixed area is \(((1+k)^2-1-k^2)V(P)=2kV(P)\).
The 2026-11-18 inspection covered the lemma and both paragraphs of its proof in the author edition.

<a id="support-lattice"></a>
## Exponent lattices and sign changes

In the [author edition](readme.md#editions), Section 3.4, pp. 4–5, treats an irreducible rational Laurent polynomial whose support differences generate \(\mathbb Z^2\).
The four separate sign changes in its two coordinates are pairwise nonassociate, since invariance up to a scalar would place all support differences in a proper parity sublattice.
If the original polynomial divided one of its signed coordinate-square transforms, all four sign changes would divide that transform, contrary to its degree.
Section 3.7, p. 6, uses monomials attached to a basis of the exponent lattice to reduce a rank-two polynomial to full lattice.
For the count of all torsion points the covering degree is the index of that lattice.
These passages were checked against the retained edition on 2026-11-18.
Restricting to a single parametrized subtorus requires a separate count of the power substitution on its parameter.
