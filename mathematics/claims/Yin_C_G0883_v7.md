---
author: Yin
---

# Realization volume linear in the number of nonzero coefficient pairs

<a id="support"></a>
Let \(P\in\mathbb Z[t]\) be monic, reciprocal, irreducible and noncyclotomic of degree \(2g\), where \(g\ge2\), and assume \(P\notin\mathbb Z[t^k]\) for all integers \(k>1\).
Put \(c_i=[t^{2g-i}]P\) and \(s=\#\{1\le i<g:c_i\ne0\}\).
There is an absolute \(C\) such that the least-volume infimum for a closed orientable hyperbolic mapping torus with whole homological characteristic polynomial \(P\) satisfies
\[
                         V_{\min}(P)\le C(1+s).
\]
The estimate is independent of the lengths of the zero runs, the nonzero coefficient magnitudes and the middle coefficient.
It applies to the [reciprocal strict records of growing degree](Yin_C_G0883_v2.md#mapping-tori).
In particular it gives uniform volume for the [two-position examples](Yin_C_G0883_v6.md#positions) even when their optimized sum of circular distances tends to infinity.
On a hypothetical sequence of strictly decreasing measures tending to one, \(s\) must still grow by the [bounded-support gap](../audits/literature/Dob06/Yin_U001.md#sparse-measure).

<a id="runs"></a>
## The matrix product between the occupied positions

Use the [ordered integral symplectic factorization](Yin_C_G0883_v4.md#homology) from Margalit and Spallone on the handles \(1,\ldots,g\).
In that order it is \(\prod_{i=1}^g E_i^{t_i}W_i\), where \(t_i=(-1)^ic_i\).
For \(i<g\), the switch \(W_i\) exchanges the adjacent handle labels \(i,i+1\) and permutes their respective marked axes by signed quarter-turns.
The elementary action \(E_i\) is given by three twists about disjoint curves representing two signed axes and their sum on these two handles.
The middle \(E_g,W_g\) are supported on the last handle. [Margalit and Spallone, p. 854, Theorem 9 and Lemmas 10–11](../audits/literature/MS07/readme.md)

Delete the \(s\) edges \((i,i+1)\) with \(t_i\ne0\) from the path on the \(g\) labels.
Its \(s+1\) components are intervals of handles.
For an interval \([l,r]\), the consecutive inactive factors in the original word are exactly \(W_l\cdots W_{r-1}\).
Their permutation is the cycle \((l,l+1,\ldots,r)\), and their internal axis changes are powers of the quarter-turn.
Choose a marked basis on the first handle of the interval and transport it around the cycle.
In these bases the product is a pure cycle followed by a quarter-turn power on a single handle, with the empty product on an interval of length one.
These basis changes can be performed simultaneously on the disjoint intervals.
The \(s\) active factors still use pairs of signed axes on the last handle of one interval and the first of the next one, and each active switch still exchanges this pair with signed quarter-turn corrections.
Thus there is one rotation to implement per interval, at most \(s+1\) internal quarter-turn corrections and \(O(1+s)\) active local maps, counting an arbitrary powered triple twist as one map.
Their original order is preserved.

<a id="fan"></a>
## Rotating an interval with its boundary fixed

For a block of \(h\) handles take a genus-\(h\) surface with one boundary component.
Build an equatorial belt of \(h\) identical sectors, each containing a marked one-holed torus in place of a disk.
Cap one end of the belt by a triangulated disk coned to its polar vertex.
At the other end attach an annulus from the sector circle to the boundary of the block, which has three edges.
Triangulate the sectors with a fixed triangulation per sector, giving \(M=ch\) edges on the sector circle for a fixed integer \(c\ge3\).
A rotation through one sector permutes the marked handles by the specified cycle and preserves the triangulations of the belt and cap.
In the annulus interpolate that rotation to the identity on the three-edge boundary.
This handle permutation is pure on its marked homology.
For \(h=1\) one may take the identity.

The annulus admits a triangulation in which displacement of the interpolated rotation requires at most \(3c\) diagonal exchanges.
In its universal covering strip label the upper sector vertices \(v_i\), \(i\in\mathbb Z\), and the lower boundary vertices \(q_j\), \(j\in\mathbb Z\).
The deck transformation sends \((v_i,q_j)\) to \((v_{i+M},q_{j+3})\).
In one period use triangles \(q_0v_i v_{i+1}\) for \(0\le i<M\) and \(v_Mq_jq_{j+1}\) for \(0\le j<3\), extending periodically.
Straight segments between the boundaries in the strip give these edges.
Moving the upper vertices by one and fixing the lower ones takes this triangulation to the fan with all upper subscripts increased by one.
Only the quadrilateral strip with lower boundary path \(q_0q_1q_2q_3\) and upper edge \(v_Mv_{M+1}\), and its deck translates, changes.
Flip the diagonals \(q_3v_M,q_2v_M,q_1v_M\) in that order, moving all three lower-edge triangles from apex \(v_M\) to apex \(v_{M+1}\).
This description in the cover descends to the annulus, allowing repeated vertices in a surface triangulation.
Repeating \(c\) times realizes the sector rotation.
Equivalently use the shear of the strip which is a horizontal shift by \(c\) upper vertices on its top and zero on its bottom.
One diagonal exchange of the two surface triangles uses one tetrahedron attached along those two faces; its complementary faces give the new diagonal.
Thus the rotation, as a homeomorphism fixing the boundary, needs only a bounded number of tetrahedra per occurrence after an initial surface collar.
The fan has \(O(h)\) triangles, all included in that initial collar.

<a id="interfaces"></a>
## Joining different intervals and accounting for their twist layers

Attach the block boundaries to the holes of a sphere with \(s+1\) disks removed, using the disk and annulus for one and two holes.
This gives genus \(\sum h=g\).
Place the holes in a line and choose a band between each consecutive pair with disjoint band interiors.
The planar surface has a triangulation of \(O(s+1)\) triangles giving each boundary three edges and each such band a uniformly bounded neighborhood.
For instance cut the planar surface along \(s\) arcs between consecutive holes to obtain a disk, triangulate a narrow rectangle for each cut and cone the remaining polygon to an interior vertex.
There are at most two band ends on any hole.
Choose their endpoints in the interiors of prescribed boundary edges and subdivide these fixed local patterns if necessary.

In each block place the first and last handles in the two sectors on opposite sides of \(v_M\), the seam of the annular fan.
They are neighbors because they are the first and last entries of its cycle.
Each of their handle disks admits an access arc to the three-edge boundary crossing only boundedly many triangles.
Use its own sector, an adjacent upper-edge triangle next to \(v_M\), and the lower-edge triangles coned to \(v_M\).
The latter can be reached across the common spoke from either side since the other seam triangle is its deck translate at the preceding or succeeding period.
In the universal strip, the fans on either side of \(v_M\) use the anchors \(q_0\) and \(q_3\), respectively.
An arc can run through interiors of those few triangles, avoiding their vertices even when an anchor has high valence.
For an interval of length one the same handle can serve both band ends at their separate times.
Together with one planar band these arcs give an embedded corridor between the two handle disks of each active edge.
Its thickening with the two tori is a genus-two subsurface in a bounded number of triangles.
One may choose its boundary inside the indicated triangles with a bounded number of arcs, or use a fixed subdivision there.
Any such subdivisions at the seam have bounded size per block, as do their images under its one-sector rotation.
They can also be inserted and removed in bounded product layers to return to the original fan.
These costs are uniform because each block participates in at most two active edges and all chosen local regions avoid the high-valence poles and fan anchors in their interiors.

On each corridor choose a switch of its two handles and the finitely many quarter-turn corrections needed on their axes.
In that same genus-two subsurface, the [disjoint-curve construction](Yin_C_G0883_v4.md#trees) realizes the powered elementary action.
For a fixed local map use a triangulated mapping cylinder tapered to its support, and for a powered multitwist drill the at most three horizontal curves in the local cylinder.
The surgery coefficients prescribe the exponents after filling.
The finite list of local triangulated models gives bounded cost per active index for all coefficient magnitudes. [Local layers and fillings](Yin_C_G0883_v5.md#layers)
The remaining single-handle maps, including the middle coefficient, use the same fixed models.

Start with a collar of the entire triangulated closed surface containing \(O(g)\) tetrahedra.
In the coordinates on its current marked top face, stack the interval rotations and local layers in the order of the symplectic word.
Transport coordinates through each layer, so a subsequent change uses the same number of tetrahedra as in its displayed block model.
Repeat the word \(n\) times before closing the identification.
The resulting compact manifold has a triangulation with at most \(C_0g+C_1n(1+s)\) tetrahedra and fills to \(M_{f^n}\), where the homological polynomial of \(f\) is \(P\).
The homological criterion makes \(f\) pseudo-Anosov, so this is an \(n\)-fold cover of a closed hyperbolic mapping torus. [Homological criterion](../audits/literature/MS07/readme.md) [Hyperbolization](Yin_C_G0883_v2.md#mapping-tori)
In the [straightening estimate](Yin_C_G0883_v5.md#layers) all tetrahedra inside the attached solid tori have zero signed volume, and each other tetrahedron contributes at most \(v_{\rm tet}\) in absolute value.
Divide by \(n\) and let \(n\) tend to infinity to obtain \(V_{\min}(P)\le \operatorname{vol}(M_f)\le v_{\rm tet} C_1(1+s)\).

## Assessment history

### Decision joint-handle-rotations

| Field | Value |
| --- | --- |
| date | 2026-11-28T07:29 |
| status | proved |
| reason | Each interval of inactive switches has a uniformly bounded flip cost. Drilling the active twists and passing to cyclic covers removes the remaining initial genus cost. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Volume bound](#support) | Entire homological polynomial with the stated irreducibility and compression hypotheses. |
| argument | [Handle intervals](#runs) | Ordered symplectic word and basis changes. |
| argument | [Annular fan](#fan) | Boundary-fixed rotation at bounded flip cost. |
| argument | [Twist interfaces](#interfaces) | Local markings, drilled layers and division by the cyclic degree. |
| dependency | [Symplectic factors](Yin_C_G0883_v4.md#homology) | Prescribed polynomial and elementary factors. |
| dependency | [Drilled layers](Yin_C_G0883_v5.md#layers) | Local fillings and the volume estimate. |
| dependency | [Hyperbolicity](Yin_C_G0883_v2.md#mapping-tori) | Homological criterion and hyperbolization. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1290.md#finding) | All four sections, the local markings and the stable volume estimate. |

## Current assessment

[Selected decision](#decision-joint-handle-rotations)
