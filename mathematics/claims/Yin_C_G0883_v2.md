---
author: Yin
---

# A homological Mahler gap for hyperbolic mapping tori of bounded volume

For every fixed volume ceiling, the total logarithmic Mahler measures of the whole monodromy polynomials of closed orientable hyperbolic surface bundles have a gap above zero.
The proof includes fillings whose cores the fibration sends to zero.
Every sufficiently late reciprocal strict record can be realized on such a bundle if its volume is allowed to vary.

<a id="mapping-tori"></a>
## Realizing the whole record polynomial in a hyperbolic three-manifold

Let \(P\) be the minimum of a sufficiently late strict degree record below the plastic number, so it is a monic reciprocal irreducible noncyclotomic polynomial of degree \(2g\) with \(g\ge2\). [Record hypotheses](../claims/Yin_C_G0901_v163.md#statement)
It cannot have the form \(Q(X^k)\) with \(k>1\), since then the smaller-degree integer polynomial \(Q\) would have the same positive Mahler measure.
Every such \(P\) occurs as the characteristic polynomial of an integral symplectic matrix \(A\).
Lift \(A\) through the homology action of the orientation-preserving mapping class group of the closed orientable surface \(S_g\).
The [Margalit–Spallone criterion](../audits/literature/MS07/readme.md) makes every lift \(f\) pseudo-Anosov, so its mapping torus \(M_f\) is a closed hyperbolic three-manifold by Thurston's fiber theorem. [Fiber theorem and Torelli cosets](../audits/literature/Riv14/readme.md)

For the cyclic cover of order \(j\) in this particular fibration, abelianizing \(\pi_1(S_g)\rtimes_{f^j}\mathbb Z\) gives
\[
 H_1(M_{f^j};\mathbb Z)\simeq\mathbb Z\oplus\operatorname{coker}(A^j-I),\qquad
 |\operatorname{Tor}H_1(M_{f^j};\mathbb Z)|=|\operatorname{Res}(P,X^j-1)|.
\]
The cokernel is finite since \(P\) has no root of unity.
Thus all these covers have first Betti number one, and their torsion growth rate per cover degree is exactly \(m(P)\) by the fixed-polynomial periodic point formula for integral toral automorphisms. [Lind, Section 4](../audits/literature/Lin82/readme.md)
In the resultant product the [unit-circle lower bound](../audits/literature/Wus02/Yin_U001.md#unit-circle) gives \(j^{-1}\log|\alpha^j-1|\to0\) for every fixed nontorsion algebraic root of modulus one.
For the closed hyperbolic surface bundles whose whole homological polynomial is irreducible, noncyclotomic and not a polynomial in a proper power of \(X\), a uniform positive lower bound for this original cyclic growth rate is equivalent to the unrestricted Lehmer gap.
One direction follows from integrality and the other from the realization of every late record along a putative sequence tending to zero.
The dimension of the hyperbolic manifold is always three; the fiber genus carries the unbounded polynomial degree.
The [Silver–Williams branched-cover theorem](../audits/literature/SW02/readme.md) gives a related dynamical interpretation for link exteriors and their branched covers.
Here the cyclic subgroups, their torsion orders and the complete polynomial are identified directly.

<a id="bounded-volume"></a>
### A volume ceiling for the whole homological polynomial

For each \(V<\infty\) there is \(\delta(V)>0\) such that every closed orientable hyperbolic mapping torus \(N=M_f\) of volume at most \(V\), with closed connected orientable fiber and orientation-preserving monodromy, satisfies
\[
 m(P_f)=0\quad\hbox{or}\quad m(P_f)\ge\delta(V),\qquad
 P_f(t)=\det(tI-f_*|H_1(S_g;\mathbb Z)).
\]
The bound applies to the entire polynomial, including possible repeated and cyclotomic factors.
Here is a cellular derivation allowing every Dehn filling slope and every fibered class of the resulting closed manifold.

By [Thurston's finite-parent theorem](../audits/literature/Thu80/readme.md), it suffices to fix a compact oriented parent \(X\) with torus boundary and consider its closed fillings, allowing also a fixed closed parent.
Choose a finite genuine triangulation of \(X\).
For a filling of a boundary component \(T_i\), attach the mapping cylinder of a cellular map \(T_i\to S_i^1\) whose kernel on the peripheral group is the filling slope.
This gives the homotopy type of the filled manifold, since the map is homotopic to inclusion into the filling solid torus followed by its retraction onto the core.
Use one vertex and one edge on the target circle, send all boundary vertices to its vertex, send every oriented boundary edge around the circle an integral number \(k\) of times, and extend across each triangle whose signed edge sum is zero.
The integers on edges can be chosen as a cellular cocycle representing the desired primitive homomorphism.
The dimensions of the resulting cellular chain groups are now fixed independently of all slopes.

Let \(\phi:\pi_1(N)\twoheadrightarrow\mathbb Z\) be the fibration and \(c_i=\phi(S_i^1)\), with either choice of core orientation.
Use cellular lifts in its infinite cyclic cover, over \(\mathbb Z[t^{\pm1}]\).
In the middle boundary matrix \(\partial_2\), the old triangles have their usual three edge incidences.
The prism over a boundary edge has two vertical sides, the original edge and its image edge path on the target circle.
Each fixed incidence contributes a signed monomial, and the edge path contributes, up to sign and a monomial, the geometric sum \((t^{kc_i}-1)/(t^{c_i}-1)\) if \(c_i\ne0\) and the integer \(k\) if \(c_i=0\).
This formula covers negative and zero winding numbers as Laurent polynomials.
Multiplying the entire matrix by \(D(t)=\prod_{i:c_i\ne0}(t^{c_i}-1)\) therefore bounds the number of terms in every entry of \(D\partial_2\) by a constant depending only on the triangulation, irrespective of coefficients or exponents.

We describe choices of two square minors for the end boundaries over \(\mathbb Q(t)\).
For \(\partial_1\) choose the columns of a spanning tree of the full one-skeleton and one further edge whose fundamental cycle has nonzero \(\phi\)-value.
Such a cycle exists since the one-skeleton surjects onto the fundamental group.
After changing vertex and edge lifts along the tree, eliminating the tree gives determinant \(\pm t^a(t^u-1)\) with \(u\ne0\).
For \(\partial_3\), use the internal dual graph of the tetrahedra of \(X\).
Loops there surject onto \(\pi_1(X)\), since interior loops can be put in general position away from the one-skeleton and read across the internal faces.
The map from \(\pi_1(X)\) to the filled group is onto, so some fundamental cycle of this graph has nonzero \(\phi\)-value.
Choose a dual spanning tree and one such extra edge.
Attach each new three-cell, the prism over a boundary triangle, as a leaf via that original triangle.
The corresponding rows of \(\partial_3\) are an oriented weighted incidence matrix of this enlarged dual graph, transposed relative to \(\partial_1\): each selected internal or boundary triangle is incident to precisely the two indicated three-cells with opposite signs.
Lifts determine the edge weights, and going around the chosen internal dual cycle has deck translation \(t^v\) with \(v\ne0\).
Deleting the leaves and eliminating the dual tree gives determinant \(\pm t^b(t^v-1)\).
The other prism faces do not enter this minor.

The specialized chain complex is acyclic over \(\mathbb Q(t)\), since the infinite cyclic cover is homotopy equivalent to the fiber and its integral homology is finitely generated over \(\mathbb Z\).
Delete from \(\partial_2\) the rows indexing the chosen \(\partial_1\) columns and the columns indexing the chosen \(\partial_3\) rows.
The remaining square matrix \(B\) has nonzero determinant by exactness.
With the convention \(\tau(S^1,t)=1/(t-1)\), the based acyclic torsion equals \(\det B\) divided by those two end minors, up to \(\pm t^a\).
Indeed one can lift the boundary bases in degrees zero and two using the chosen end pivots, and in degree one project along the chosen rows to obtain the complementary determinant.
On the mapping torus the same torsion is \(P_f(t)/(t-1)^2\), up to a signed Laurent unit.
For an integral verification, the alternating product of the orders of \(H_i\) of the cyclic cover has the middle homology order in the numerator and the end orders in the denominator.
Localizing the free integral Laurent complex at each height-one prime gives this identity by diagonalization over a discrete valuation ring, so the ambiguity over \(\mathbb Z[t^{\pm1}]\) is just \(\pm t^a\).
The fiber homology has two trivial end actions and the integral action \(f_*\) in the middle; reversing the deck convention gives the same Laurent order by reciprocity.

If \(s\) is the size of \(B\), the nonzero integral Laurent polynomial \(L=\det(DB)=D^s\det B\) has at most \(K_X\) terms for a constant depending only on the fixed cells.
All other factors in the two torsion expressions are Laurent monomials or binomials \(t^h-1\), so \(m(P_f)=m(L)\).
The [Dobrowolski–Smyth bounded-support theorem](../audits/literature/DS17/Yin_U001.md#ds17-u001) now gives zero or a uniform positive gap for \(X\), independent even of the sizes of the integral coefficients appearing when a core has \(c_i=0\).
Taking the minimum over the finite parents proves the volume assertion.
For fillings with all \(c_i\ne0\), [Turaev's surgery formula](../audits/literature/Tur01/readme.md) supplies a second check, since filling changes the specialized torsion by the inverse product of the core binomials, up to units.
That particular division requires nonzero \(c_i\); the cellular proof treats the remaining case as well.

Consequently if strict record measures tend to one, the infimum of the volumes of closed hyperbolic mapping tori realizing each record as their **whole** first-homology polynomial tends to infinity.
Otherwise a bounded-volume subsequence of realizations would violate the displayed gap.
The earlier [normalized-entropy restriction](../claims/Yin_C_G0883_v1.md#statement) gives a second quantity that must diverge, the infimum of \((2g-2)\log\lambda(f)\) over those same lifts.
Conversely one can increase volume at fixed \(A\) and fixed fiber genus: take a lift times a varying element of a finitely generated nonelementary subgroup of the Torelli group.
[Rivin's coset volume result](../audits/literature/Riv14/readme.md) gives unbounded volume there, although the homology of every cover in the original cyclic tower stays fixed.
Thus a large-volume representative alone places no restriction on the record.
The relevant geometric quantity is the smallest volume attainable for that whole polynomial, or a bound that retains its force as that volume tends to infinity.

## Assessment history

### Decision bounded-volume-homological-gap

| Field | Value |
| --- | --- |
| date | 2026-11-27T11:12 |
| status | proved |
| reason | The cellular calculation covers every filling core, and the independent review verified both end minors, the integral torsion normalization, the support bound and the whole-polynomial realization. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Volume ceiling](#bounded-volume) | Positive gap for the whole homological polynomial at every fixed hyperbolic volume bound. |
| argument | [Cellular and torsion proof](#bounded-volume) | All fillings of each finite parent, including trivial core character. |
| argument | [Realization and cyclic tower](#mapping-tori) | Full homological actions of late strict records and torsion growth in their original fibrations. |
| dependency | [Finite-parent and sparse-polynomial inputs](#bounded-volume) | Thurston's finite parents and the Dobrowolski–Smyth fixed-support gap, with the normalized-entropy result used for the separate entropy consequence. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1277.md#finding) | Both arguments and their consequences at the indicated external theorem interfaces. |

## Current assessment

[Selected decision](#decision-bounded-volume-homological-gap)
