---
author: Yin
---

# Open hyperbolic realizations with prescribed boundary periods

<a id="volume"></a>
## Cost per boundary orbit

Let \(P\) be monic, integral, reciprocal, irreducible and noncyclotomic of degree \(2g\), where \(g\ge2\), and suppose \(P\notin\mathbb Z[x^k]\) for every \(k>1\).
Write \(s=\#\{1\le i<g:[x^{2g-i}]P\ne0\}\).
Prescribe any nonempty list \(h_1,\ldots,h_t\) of positive integers, allowing repetitions, and put
\[
 B=\sum_{i=1}^t h_i,\qquad C(x)=\frac{\prod_{i=1}^t(x^{h_i}-1)}{x-1}.
\]
There is a finite-volume orientable hyperbolic bundle \(Y\) with fiber a genus-\(g\) surface with \(B\) boundary components, with the specified boundary cycle lengths, such that
\[
 P_{\rm open}=PC,\qquad P_{\rm capped}=P,\qquad
                 \operatorname{vol}(Y)\le K(1+s+t)
\]
for an absolute constant \(K\).
The closed bundle obtained by simultaneous capping is hyperbolic.
Here the volume cost counts cycles, independently of their lengths and of the coefficient magnitudes.
For a proposed monic cyclotomic \(C\), [Möbius inversion of its multiplicities](Yin_C_G0883_v8.md#cycles) therefore gives a necessary and sufficient condition for some such open realization with that closed polynomial.
This assertion allows the choice of the closed monodromy within the prescribed homological action.

<a id="filling"></a>
## A filling family joining the marked points

Start with the [closed handle model](Yin_C_G0883_v7.md#support) for \(P\) and write \(f\) for its mapping class.
It is pseudo-Anosov by the [closed homological criterion](Yin_C_G0883_v2.md#mapping-tori).
Choose a disk \(D\) fixed pointwise by the word representative, using the position specified below.
In \(D\) choose \(t\) smaller disjoint disks \(D_i\), with \(h_i\) marked points arranged on a circle in \(D_i\).
In each disk use a one-step rotation interpolated to the identity at its boundary.
The resulting marked mapping class \(F\) induces the prescribed permutation of points, and forgetting all the marks gives \(f\).
Curves and intersection numbers below refer to the surface with the marks removed, or equivalently truncated to boundary circles that are allowed to move.

Choose the following essential simple closed curves.
For each \(h_i\ge2\) take the boundary of a small disk containing exactly two cyclic neighbors in \(D_i\).
Between \(D_i\) and \(D_{i+1}\) take the boundary of a disk formed along an arc joining one marked point from each, enclosing just that pair.
The orbits of these disk curves supply edges of a connected graph on all \(B\) points.
Indeed within each \(D_i\) the images of its chosen pair run through the edges of the cyclic polygon, and the consecutive disks are joined by the specified edges.
For \(B=1\) the single vertex suffices.

Choose one further curve \(c\) which bounds a one-holed torus after filling the marks and has exactly one marked point on its designated genus-one side.
Take the boundary of a regular neighborhood of one handle, a small disk about a mark in \(D_1\), and an embedded band connecting the two.
Both sides have positive genus after filling since \(g\ge2\).
The orbits of the chosen curves fill the marked surface.
In fact, if an essential test curve remains essential on the closed surface, it meets an iterate of \(c\) there because the orbit of its closed image under the pseudo-Anosov \(f\) fills.
A finite segment suffices for all such test curves. [Hirose, Kalfagianni and Kin, Remark 7](https://arxiv.org/pdf/2208.02977v2#page=8)
Filling the marks can only decrease geometric intersection, since it allows more isotopies.

Otherwise the test curve bounds a disk containing a set \(S\) of at least two marked points.
The side which is a disk is uniquely determined on this positive-genus surface.
If \(S\) is proper, a graph edge has one endpoint in \(S\) and the other outside it.
The edge disk and the test disk then have overlapping, nonnested mark sets since \(|S|\ge2\).
Their boundaries cannot have disjoint representatives, because disks with disjoint boundaries on this surface are disjoint or nested.
If \(S\) contains all marks, with \(B\ge2\), the two sides of \(c\) contain marks.
A test disk disjoint from \(c\) cannot contain \(c\), which is essential after filling, and hence cannot contain marks on both sides.
The finite polygon edges, joining edges and the finite closed orbit segment prove filling in the finite-segment sense.

Keep one chosen curve from each distinct \(F\)-orbit.
This leaves the union of the full orbits unchanged, and finite filling persists by enlarging the segment to account for the finitely many identifications.
Theorem 5(a) of Hirose, Kalfagianni and Kin makes the composition of \(F\) with sufficiently large powers of the twists about these curves pseudo-Anosov, attaching the twists at separate levels in their specified order.
Their mapping class group allows permutations of the boundary, and the theorem assumes \(3g-3+B>0\). [Definitions and Theorem 5](https://arxiv.org/pdf/2208.02977v2#page=3)
Twisting fixes each mark and hence keeps the permutation.
The pair curves become inessential on closing, and \(c\) becomes separating.
It follows that every added twist acts trivially on closed homology.
Thus the resulting marked class \(G\) is pseudo-Anosov and its capped class still has the original homology action, so is pseudo-Anosov by the same closed criterion.
The twist in \(c\) can change the closed mapping class.
Truncating the punctures gives the open bundle, and the [capping exact sequence](Yin_C_G0883_v5.md#hironaka) gives the asserted whole polynomials.

<a id="layers"></a>
## A bounded layer for each rotation and each drilling

In the closed model the handle blocks attach to a planar surface, and the local switches and twists join neighboring blocks by thin bands in that planar surface.
There is at least one active edge since otherwise \(P=x^{2g}+c_gx^g+1\) would be compressed.
Choose \(D\) as a small disk in the planar surface next to the first block boundary and outside all joining bands.
The end block has at most one such band.
The disk can be given three boundary edges by a bounded subdivision of the adjacent fixed local pattern.
It is untouched by the rotations of the handle blocks and by the closed local maps, whose supports outside the blocks lie in the bands.
One outermost seam handle of the first block has an access path to \(D\) through boundedly many triangles by the [seam construction](Yin_C_G0883_v7.md#interfaces).
This path may cross an old support because the new twist uses a separate level.

Replace the interior triangulation of \(D\) by the chain of \(D_i\).
The planar region between their three-edge boundaries and the boundary of \(D\) has a triangulation of \(O(t)\) triangles with bounded corridors from \(D\)'s boundary to \(D_1\) and between each consecutive pair.
For instance cut the region to a disk along the chain of arcs through these holes, give each strip around a cutting arc the same rectangular pattern, and cone the complementary polygon.
The endpoints of the strips can use interiors of boundary edges.
Each hole is used at most twice, independently of \(t\).

Inside \(D_i\) take a belt of \(h_i\) equal sectors, each carrying one small three-edge puncture boundary.
Cap the inner side by a coned disk, and interpolate the outer side to the fixed three-edge boundary by the [annular fan](Yin_C_G0883_v7.md#fan).
There are \(O(h_i)\) triangles once, and rotation through one sector changes the triangulation by a bounded number of flips because the belt and cap rotate simplicially and the annular shear moves only one sector.
A singleton uses a fixed disk-with-hole triangulation and the identity rotation.
At the two sectors adjacent across the fan seam, each point has an access path to the outer boundary of \(D_i\) through boundedly many triangles as in the handle construction.
Use these sectors for the adjacent pair and for the joining arcs between disks.
Two neighboring punctures connect through their adjacent sectors, and the joining arcs use the indicated planar strips.
Their small neighborhoods and the boundaries of the two-point disks have bounded triangulated complexity.
The curve \(c\) likewise uses just the first seam handle, the short band to \(D\) and the access to one seam sector of \(D_1\).
All paths can avoid the high-valence fan vertices and polar vertices, traversing the interiors of the seam triangles.
Local subdivisions to insert and undo a twist layer therefore have bounded size as in the closed construction.
Intersections between curves used at different levels incur no common subdivision.

The initial perforated surface now has \(O(g+B)\) triangles.
In a single word the closed layers cost \(O(1+s)\) tetrahedra and the disk rotations cost \(O(t)\).
There are at most \(2t\) additional twist curves, each in a bounded local model.
Drill its horizontal copy before filling with its twist coefficient, which gives bounded cost independent of the chosen power. [Marked twist layers](Yin_C_G0883_v5.md#layers)
Use transported markings when stacking and repeat the word \(a\) times.
As in the [cyclic-cover construction](Yin_C_G0883_v7.md#interfaces), a compact triangulated parent has at most \(K_0(g+B)+aK_1(1+s+t)\) tetrahedra and fills to the compact core of the cyclic cover \(Y_a\) with monodromy \(G^a\).
For fixed \(a\), fill the remaining cusps of the hyperbolic \(Y_a\) along a sequence of long slopes to get closed hyperbolic volumes converging to \(\operatorname{vol}(Y_a)\) by hyperbolic Dehn filling.
All these closed fillings come from the same triangulated parent.
The [straightening bound for closed fillings](Yin_C_G0883_v5.md#layers) gives each volume at most \(v_{\rm tet}(K_0(g+B)+aK_1(1+s+t))\).
Pass to the limit, divide by \(a\) using \(\operatorname{vol}(Y_a)=a\operatorname{vol}(Y)\), and let \(a\) grow.
This proves the claimed bound independently of the total number of points.

<a id="records"></a>
## What the bound controls on growing records

Every sufficiently late reciprocal strict record satisfies the input hypotheses by [degree compression and the closed realization](Yin_C_G0883_v2.md#mapping-tori).
Consequently every candidate sparse multiple \(PC\) that passes the cycle inversion test admits this open construction in its own degree and closes back to that record polynomial.
If \(k\) is the number of nonzero coefficients of \(PC\), then \(t\le k\).
Indeed \(C\) vanishes at one to order \(t-1\), and a polynomial with \(k\) terms has at most \(k-1\) positive zeros with multiplicities by Descartes' rule.
Thus the construction gives \(O(1+s+k)\), and in particular \(O(k)\) on any class with \(s=O(k)\).
It does not price a dense closed polynomial solely by the support of its much sparser open multiple.
On a sequence of strict records with \(M(P)\to1\), the [closed volume lower bound](Yin_C_G0883_v3.md#statement) tends to infinity, and hyperbolic filling gives smaller closed volume than the volume of the open realization.
Any bound depending on the open support on this branch must allow that support to grow.

## Assessment history

### Decision open-boundary-volume

| Field | Value |
| --- | --- |
| date | 2026-11-28T08:07 |
| status | proved |
| reason | A filling set of curves realizes the prescribed boundary action by twists that act trivially on closed homology. Rotation and drilled twist layers have bounded cost per cycle. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Volume bound](#volume) | All nonempty lists of boundary lengths and the specified closed characteristic polynomial. |
| argument | [Filling the marked surface](#filling) | Choice of curves, actual pseudo-Anosov monodromy and capping. |
| argument | [Triangulated layers](#layers) | Costs independent of cycle lengths and twist exponents. |
| argument | [Growing records](#records) | Support of the open multiple, admissibility and the remaining volume question. |
| dependency | [Closed components](Yin_C_G0883_v7.md#interfaces) | The marked block realization and stable triangulation bound. |
| dependency | [Boundary module](Yin_C_G0883_v8.md#cycles) | Unique profile and homology under capping. |
| dependency | [Volume lower bound](Yin_C_G0883_v3.md#statement) | Divergence on record sequences whose measures tend to one. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1300.md#finding) | All four sections, including the source hypotheses, stable volume argument and scope on shrinking records. |

## Current assessment

[Selected decision](#decision-open-boundary-volume)
