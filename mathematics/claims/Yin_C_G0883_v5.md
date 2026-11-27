---
author: Yin
---

# Realization volume from the cyclic positions of the coefficients

<a id="positions"></a>
Let \(P\in\mathbb Z[t]\) be monic, reciprocal, irreducible and noncyclotomic of degree \(2g\), \(g\ge2\), and assume \(P\notin\mathbb Z[t^k]\) for every \(k>1\).
Let \(V_{\min}(P)\) be the infimum of the volumes of closed orientable hyperbolic surface bundles with whole homological polynomial \(P\).
Write \(I=\{1\le i<g:[t^{2g-i}]P\ne0\}\) and \(\|x\|_g=\min_{k\in\mathbb Z}|x-kg|\).
There is an absolute \(C\) such that
\[
 V_{\min}(P)\le C\left(1+
     \min_{u\in(\mathbb Z/g\mathbb Z)^\times}\sum_{i\in I}\|ui\|_g\right).
\]
If \(I=\{i\}\), compression forces \(\gcd(i,g)=1\), since any common divisor divides every exponent of \(P\).
Choosing \(u=i^{-1}\bmod g\) gives \(V_{\min}(P)\le 2C\), uniformly in the genus, both free coefficient magnitudes and the position \(i\).
More generally, \(s\) positions carried by one unit into the residues represented by \([-w,w]\) give \(V_{\min}(P)\le C(1+sw)\).
The coefficient estimate complements the [dyadic position bound](Yin_C_G0883_v4.md#upper-bound).
Compression of strict records supplies the coprimality in the single-position case, while the simultaneous placement of several positions under a common unit is an additional condition.
An unbounded sequence with \(M(P)\to1\) must also have unbounded support by the [bounded-support Mahler gap](../audits/literature/Dob06/Yin_U001.md#sparse-measure).

<a id="circle"></a>
## A realization by local maps on a circle of handles

Use the [signed-shift factorization](Yin_C_G0883_v4.md#homology) obtained from the Margalit–Spallone matrix with polynomial \(P\).
After changing basis by a quarter-turn power on each handle, its permutation part is a pure cyclic shift followed by a quarter-turn power on one handle.
Each active index \(i\) contributes an integral power of a product of three twists along disjoint curves with classes \(v,w,v+w\), where \(v,w\) are signed axes on handles \(0,i\).
The middle coefficient contributes one axis twist on handle zero.
Any choices of lifts with these actions give a pseudo-Anosov product by the [homological criterion](../audits/literature/MS07/readme.md).

Fix the unit \(u\) and arrange the \(g\) one-holed tori around the equator of a sphere with \(g\) holes, putting label \(j\) in position \(uj\bmod g\).
A rotation through \(u\) sectors now realizes the pure shift \(j\mapsto j+1\).
Choose a rotation-invariant triangulation of the closed surface using \(O(g)\) triangles.
For example, decompose an equatorial annulus into \(g\) identical rectangles, replace a small disk inside each rectangle by a marked one-holed torus, and triangulate this fixed piece relative to its four sides.
Cone the outer polygon of vertices on each side of the belt to its respective pole.
Uniform subdivision gives a triangulation also in small genus.
Use subsurfaces inside one rectangle or a union of two neighboring rectangles and the attached handles for the local operations below.
The union of two adjacent rectangles is a disk before attaching the handles when \(g\ge3\), and the cases \(g=2\) are covered by the [linear bound in fixed genus](Yin_C_G0883_v4.md#upper-bound).
Add the chosen boundaries of the neighborhoods of one handle and of two adjacent handles to the equatorial triangulation in every sector by a fixed refinement.
Such neighborhoods can be bounded by small regular neighborhoods of the handle disks and, for two handles, the equatorial arc joining them.
Each one meets only boundedly many translates and can be given the same finite subdivision on each sector.

There is a homeomorphism supported in a neighboring pair of handles and their joining region which interchanges the handles with their marked bases.
On the planar part take a half-twist interchanging the two removed disks and adjust the parametrizations of their boundaries before extending over the tori.
Its action on the other handle bases is trivial.
For \(m=\|ui\|_g\), use \(m-1\) such exchanges along a shortest circular path to bring the handle labelled \(i\) next to handle zero without moving zero.
Perform the local three-curve multitwist on the neighboring pair, then conjugate back by the inverse exchanges.
The three curve representatives in the local genus-two subsurface exist by the [disjoint band construction](Yin_C_G0883_v4.md#trees).
Only finitely many local marked models occur for either direction of the path and the choices of signed axes.
One handle also supports the middle twist and the quarter-turn correction.
We obtain the required mapping class \(f\) as a word in the simplicial rotation, fixed one- or two-handle maps, and powers of fixed local twists.
Apart from the rotation there are at most \(C_0(1+\sum_{i\in I}\|ui\|_g)\) factors, counting a powered multitwist as one.

<a id="layers"></a>
## The volume cost of a supported factor

Let \(K\) be the triangulation just chosen.
For a fixed map \(h\) supported on a local subsurface \(U\), use a product layer on \(U\) with its bottom marked by \(K|_U\) and its top by \(h(K)|_U\).
The map is the identity near \(\partial U\).
A piecewise linear function on \(U\), positive on its interior and zero on its boundary, makes the region between its graph and \(U\) a layer tapering to zero thickness at \(\partial U\).
Attach the layer by its lower face to the current top surface, keeping the rest of that surface intact.
This just raises the top through a collar and preserves the underlying product cobordism.
The two compatible boundary triangulations extend over this compact piece after choosing a collar interpolation and an interior triangulation.
The finite list of marked one- and two-handle models therefore has one common upper bound on the number of tetrahedra in each layer.

For a powered multitwist, use this same tapered product with the original marking on both faces and drill its fixed horizontal curves at an interior height away from the taper.
There are at most three disjoint curves chosen from fixed models.
The triangulated layer with their open tubular neighborhoods removed again has bounded size, independent of the exponents.
Filling each drilled torus with the slope for the required twist power gives the marked mapping cylinder of that power, by cutting and regluing along the horizontal annulus around the curve in the fiber.
Equivalently, use \(K|_U\) as the coordinate marking on both free faces of every block and encode a fixed map \(h\) in the upper parametrization of its local product.
In these coordinates stacking the blocks composes the specified maps after filling, and their exposed triangles always match the same labelled model.
The rotation is simplicial and can be inserted by changing this parametrization, with no layer.

For \(n\) periods start with one triangulated collar of the entire surface of size \(O(g)\), then stack \(n\) copies of the sequence of marked local layers.
Identify its last and first surfaces by matching the coordinates.
The resulting compact manifold \(Y_n\) fills to the mapping torus \(M_{f^n}\), and its triangulation uses at most
\[
                  C_1 g + n C_2\left(1+\sum_{i\in I}\|ui\|_g\right)
\]
tetrahedra.
Every local layer is added only on its support, so the triangulation of the unchanged portion of the fiber incurs no extra cost at that step.
One may subdivide a bounded number of times per simplex to remove face identifications in this triangulation.

Here is a direct volume estimate which also applies when \(Y_n\) itself lacks a hyperbolic metric.
Extend the boundary triangulation across each filled solid torus with any finite number of tetrahedra.
In the universal cover of the closed hyperbolic manifold \(M_{f^n}\), the stabilizer of each lifted filling piece is the cyclic image of its fundamental group.
Choose images for the vertices of this piece equivariantly on the axis of a generator, or at one point if the stabilizer is trivial.
Distinct lifts of the filling pieces have disjoint sets of vertices and the choices extend equivariantly to all their translates.
Choose images for the remaining vertices, straighten equivariantly, and descend to the closed manifold.
The resulting map is homotopic to the identity by geodesic interpolation from the lifted identity map.
Its signed volume equals \(\operatorname{vol}(M_{f^n})\), and all tetrahedra in filling pieces have zero straightened volume.
Each remaining tetrahedron has absolute volume at most \(v_{\rm tet}\), the maximal volume of a hyperbolic tetrahedron.
Divide by \(n\) using the \(n\)-sheeted cyclic cover of \(M_f\), then let \(n\to\infty\) at fixed \(g\).
This proves the stated bound independently of the starting collar and the filling slopes.

<a id="hironaka"></a>
## A coefficient identity giving fillings of a single manifold

Let \(X\) be Hironaka's two-cusped simplest hyperbolic braid exterior.
Take coprime integers \(|a|<b\) with \(b\ge6\) and set \(e_1=\gcd(3,a)\), \(e_2=\gcd(3,b)\).
The whole polynomial on the closed fiber after capping the fiber of class \((a,b)\) is
\[
 P_{a,b}(t)=
  \frac{(t-1)^2
     (t^{2b}+t^{b+a}-t^b+t^{b-a}+1)}
       {(t^{e_1}-1)(t^{e_2}-1)} .
\]
Consequently \(V_{\min}(P_{a,b})<\operatorname{vol}(X)\), with no irreducibility assumption on this family.
This gives a direct coefficient test even when division by \(\Phi_3\) creates many nonzero coefficients.

Hironaka describes the fibered cone just before equation (3), which gives the normalized link Alexander polynomial in the indicated meridian coordinates.
Her Propositions 3.3 and 3.5 give \(e_i\) boundary components on cusp \(i\), with prong numbers \(3b/e_1\) and \(b/e_2\) respectively. [Hironaka, Section 3](../audits/literature/Hir10/readme.md)
Both prong numbers are at least two, so the invariant foliations extend after capping, with a regular point where the prong number is two.
The extended monodromy is pseudo-Anosov, and its closed hyperbolic mapping torus is obtained by filling the two cusps of \(X\) along the fiber boundary slopes.
Hyperbolic Dehn filling strictly decreases the volume. [Hyperbolic filling](../audits/literature/Thu80/readme.md)

For the homological computation, the braid exterior has the deficiency-one two-dimensional presentation complex of the mapping torus of a graph spine of the punctured disk.
Its universal abelian boundary \(\partial_1\) has entries \(h_j-1\) with \(h_j\) generating the free abelian group of rank two.
Their gcd in its integral Laurent ring is one, since every \(h-1\) belongs to the ideal generated by these entries, including the differences for the two independent coordinate generators.
The signed maximal minors of \(\partial_2\) are proportional over the fraction field to \(\partial_1\), by the cofactor identity and the nonzero link Alexander polynomial.
The gcd of these minors is that Alexander polynomial, so their common proportionality factor equals it up to a Laurent unit.
Specialize the variables to \(t^a,t^b\) and choose a column of \(\partial_1\) whose specialization is nonzero.
Dividing the corresponding specialized minor by that boundary entry gives the torsion of the specialized complex, hence Hironaka's specialized Alexander polynomial up to a signed monomial.
The same torsion computed from the open fiber is its \(H_1\) characteristic polynomial divided by \(t-1\), since the connected fiber has \(H_2=0\).

On capping, the kernel on \(H_1\) is generated by the oriented boundary circles with the single invariant relation that their sum is zero.
The monodromy permutes the circles in exactly two cycles of lengths \(e_1,e_2\), one for each boundary torus.
The kernel therefore has characteristic polynomial \((t^{e_1}-1)(t^{e_2}-1)/(t-1)\).
Dividing the open-fiber polynomial by this kernel polynomial and normalizing its leading coefficient and lowest exponent gives the displayed \(P_{a,b}\).
Coprimality of \(a,b\) makes the boundary factor removed from the five-term specialization equal to \(1\) or \(\Phi_3\).
For \((a,b)=(1,6)\) the identity is
\[
 t^{12}+t^7-t^6+t^5+1=(t^2+t+1)P_{\rm Lehmer}(-t),
 \quad
 P_{\rm Lehmer}(t)=t^{10}+t^9-t^7-t^6-t^5-t^4-t^3+t+1 .
\]
This realization has characteristic polynomial \(P_{\rm Lehmer}(-t)\).
It has the same Mahler measure as \(P_{\rm Lehmer}(t)\), while a prescribed choice of sign for a homological realization requires its own polynomial identity.
Every member of this family has a completion with five terms, so the [sparse measure bound](../audits/literature/Dob06/Yin_U001.md#sparse-measure) excludes a sequence of measures tending to one from above in the family.

## Assessment history

### Decision cyclic-coefficient-positions

| Field | Value |
| --- | --- |
| date | 2026-11-27T12:32 |
| status | proved |
| reason | The local drilled layers realize the selected homological action with uniformly bounded cost per adjacent exchange, and the braid specialization retains the full polynomial after capping. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Cyclic-position bound](#positions) | Uniform coefficient-independent volume bound and the single-position case. |
| argument | [Handle circle](#circle) | Signed shift and local realizations. |
| argument | [Drilled layers](#layers) | Tetrahedron counts, fillings, straightening and cyclic division. |
| argument | [Closed Hironaka fibers](#hironaka) | Whole-polynomial identities, degree, capping and filling volume. |
| dependency | [Signed shifts](Yin_C_G0883_v4.md#homology) | Prescribed symplectic polynomial and its twist factors. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1285.md#finding) | Entire fixed argument and applicability of the stated geometric inputs. |

## Current assessment

[Selected decision](#decision-cyclic-coefficient-positions)
