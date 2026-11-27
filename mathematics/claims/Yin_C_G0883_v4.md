---
author: Yin
---

# Volume of a closed surface bundle with prescribed homological polynomial

<a id="upper-bound"></a>
Let \(P\in\mathbb Z[X]\) be monic, reciprocal, irreducible and noncyclotomic of degree \(2g\), where \(g\ge2\).
Suppose \(P\) does not have the form \(Q(X^k)\) for \(Q\in\mathbb Z[X]\) and \(k>1\).
Write \(c_i=[X^{2g-i}]P\), \(I=\{1\le i<g:c_i\ne0\}\), \(h=\lceil\log_2 g\rceil\), and let \(v_2\) denote the 2-adic valuation.
Let \(V_{\min}(P)\) be the infimum of the hyperbolic volumes of closed, orientable surface bundles whose monodromy has characteristic polynomial \(P\) on the first integral homology of the fiber.
There is an absolute constant \(C\) such that
\[
 V_{\min}(P)\le C\min\left\{g,\;
 1+h-v_2(g)+\sum_{i\in I}\bigl(1+h-v_2(i)\bigr)\right\}.
\]
In particular \(V_{\min}(P)\ll\min\{g,(1+|I|)\log(2g)\}\), independently of the coefficient magnitudes and the middle coefficient \(c_g\).
For the linear term one also has the explicit estimate \(V_{\min}(P)<40v_{\rm tet}g\), where \(v_{\rm tet}\) is the volume of a regular ideal tetrahedron.
The hypotheses hold for every sufficiently late reciprocal strict degree record on a putative sequence of positive Mahler measures tending to zero. [Record realization](Yin_C_G0883_v2.md#mapping-tori)

<a id="homology"></a>
## Locating the twists for the nonzero coefficients

Use the symplectic basis \(x_j,y_j\) of the \(g\) handles, initially numbered \(1,\ldots,g\).
The Steinberg product of Margalit and Spallone gives a matrix of characteristic polynomial \(P\) in the form
\[
 A=\prod_{i=1}^g E_i^{t_i}W_i,\qquad t_i=(-1)^i c_i .
\]
For \(i<g\), \(W_i\) exchanges the \(i\)-th and \((i+1)\)-st handles and acts within the exchanged bases by powers of the quarter-turn \(J(x,y)=(-y,x)\).
The factor \(W_g\) is a quarter-turn on the last handle.
The action \(E_i\) has a lift given by twists about disjoint curves with homology classes \(u,v,u+v\), where \(u,v\) are basis axes on the two handles, with the twist signs specified by the matrix.
The factor \(E_g\) is a single signed axis twist.
These assertions use the matrix identity and its lifts for a prescribed reciprocal polynomial. [Margalit and Spallone, p. 854, Theorem 9 and Lemmas 10–11](../audits/literature/MS07/readme.md)

Put \(H_i=W_1\cdots W_{i-1}\) and \(R=W_1\cdots W_g\).
Moving the switches to the right gives \(A=(\prod_i (H_iE_iH_i^{-1})^{t_i})R\).
On the handle labels \(H_i\) acts by \((1\,2\,\cdots\,i)\), sending \(i\) to \(1\) and fixing \(i+1\) for \(i<g\).
Renumber the handles \(0,\ldots,g-1\) by subtracting one.
The triple of the \(i\)-th coefficient now uses handles \(0,i\), and the single middle-coefficient twist uses handle \(0\).
The signed permutation \(R\) shifts the labels by one modulo \(g\).
Conjugating by a quarter-turn power independently on each handle makes this a pure shift followed by a quarter-turn power on one handle.
Indeed, choose the basis on handle zero, transport it successively under \(R\), and retain the discrepancy on the last return.
This conjugation preserves the characteristic polynomial and leaves all the axes in the twist factors among the signed \(x\)- and \(y\)-axes.
We may realize each new factor by any mapping class with its specified homological action.
Their product is pseudo-Anosov by Proposition 2 of Margalit and Spallone, so its closed mapping torus is hyperbolic. [Homological criterion](../audits/literature/MS07/readme.md) [Hyperbolization of the bundle](Yin_C_G0883_v2.md#mapping-tori)

<a id="trees"></a>
## Pants moves for a shift and for an individual twist factor

For \(g\ge3\), glue \(g\) marked one-holed tori to a sphere with \(g\) holes.
A trivalent tree with the boundary components as labelled leaves specifies a pants decomposition of the central sphere up to a homeomorphism preserving its boundary labels.
It is realized by gluing one pair of pants per internal vertex.
Include the handle boundaries and one fixed axis \(x_j\) in every handle to obtain a pants decomposition \(D\) of the closed surface.
An internal-edge rotation of the tree is realized by one elementary pants move in the four-holed sphere formed by its two incident pairs of pants.
Both alternative pairings are possible by choosing a curve meeting the old curve twice.
An isomorphism between two such labelled trees with prescribed permutation of the leaves lifts to an orientation-preserving homeomorphism of the decomposed spheres by matching the pairs of pants and their boundary identifications.
It extends over the handles with the indicated permutation of their marked bases, since the boundary identifications can be adjusted in collars.

Use as the tree the nested residue classes of \(0,\ldots,g-1\) modulo \(2^k\) for \(0\le k\le h\).
Split each class into its two residue subclasses until reaching singletons, discard empty branches, collapse unary vertices, and suppress the degree-two root to obtain an unrooted trivalent tree \(T\).
Write \(\sigma(j)=j+1\bmod g\).
After deleting leaf zero and suppressing the resulting unary vertices, the hierarchies for \(T\) and \(\sigma T\) agree on all remaining labels.
Indeed, if \(A_{k,r}\) is the class of \(r\bmod 2^k\) among the labels, then
\[
 \sigma(A_{k,r})\setminus\{0\}
 = A_{k,r+1}\setminus\{0\}.
\]
For \(a=v_2(g)\), the classes modulo \(2^a\) are permuted exactly.
Within every such target class other than \(0\bmod 2^a\) no element wraps, so the deeper hierarchies there also agree.
The possible change is confined to the subtree on the labels \(0\bmod 2^a\), of height at most \(h-a\).
Inside it the two trees differ only in the edge at which the deleted leaf is reinserted, allowing the attachment edge above its root.
Moving a leaf attachment from one edge to an adjacent edge takes one internal-edge rotation around their common trivalent vertex.
The two insertion edges are therefore joined by \(O(1+h-a)\) rotations, since the common reduced subtree has diameter at most \(2(h-a)+O(1)\).
A subtree of at most two leaves has no internal rearrangement, and when \(g\) is a power of two the full shift already preserves the tree.
Lift this sequence of rotations to actual pants moves starting at \(D\).
At its endpoint the tree has the form \(\sigma T\), so the extension over marked handles just described realizes the pure shift with that endpoint.
The remaining quarter-turn power changes at most one \(x_j\) to \(y_j\), requiring at most one move in a one-holed torus.
This constructs a lift of \(R\) with displacement \(O(1+h-v_2(g))\) at \(D\).

The leaves \(0\) and \(i\), for \(1\le i<g\), have a common residue class through level \(v_2(i)\).
Their tree distance is at most \(2(h-v_2(i))+O(1)\).
By sliding the attachment of leaf zero along this path, bring the two leaves to the same pair of pants in \(O(1+h-v_2(i))\) moves.
Their handles and this pair of pants now form a genus-two subsurface with one boundary.
In this subsurface choose simple curves for the two required signed axes \(u,v\) and a disjoint curve representing \(u+v\).
For the last curve take parallel copies of the first two and join them with an embedded band on their chosen sides.
An arc for this band exists because cutting along the two axes leaves the subsurface connected.
The resulting three disjoint curves extend to a pants decomposition of the subsurface.
The displacement needed to reach such a decomposition inside the subsurface is bounded by an absolute constant.
Indeed, after matching the two marked handles and the joining pants to one fixed model, there are only finitely many choices of the signed axes, and for each choice one may fix a completion and a path in the connected pants graph of that model.
Extend each path by the unchanged decomposition outside.
The specified multitwist fixes its completed decomposition for every integral power.
Taking the path there and its image back bounds displacement at \(D\) by \(O(1+h-v_2(i))\) for the entire \(i\)-th factor, independent of \(t_i\).
For \(t_i=0\) choose the identity.
The middle twist fixes a decomposition obtained by changing at most one handle axis, giving \(O(1)\) displacement for every \(t_g\).

<a id="volume"></a>
## Passing from pants moves to volume

For mapping classes acting isometrically on the pants graph, displacement of a product at \(D\) is at most the sum of the displacements of its factors at \(D\).
The preceding construction bounds the displacement by the second quantity in the minimum.
For the linear bound use the original unfactored product on a tree whose internal vertices form a path, with handle labels placed in order along it.
Consecutive handles have uniformly bounded tree distance, so each original twist factor has uniformly bounded displacement by the same local construction.
Each \(W_i\), \(i<g\), also has bounded displacement.
Move the two consecutive handles to sibling leaves, exchange the siblings by a homeomorphism preserving that decomposition, and realize the two indicated quarter-turn powers in their individual handles.
Returning along the image of the first path incurs the same bounded cost.
For \(g=2\) the original two handles are already adjacent along their common separating circle.
The switch is realized by exchanging those handles and adjusting their axes.
The triple twists and the single twist again fix completions at bounded distance in this one fixed genus.
These estimates give \(O(g)\) uniformly, absorbing genus two into the absolute constant for both bounds.

For any of the resulting pseudo-Anosov lifts \(F\), choose a pants path of length \(L\) from \(D\) to \(FD\).
Concatenate \(k\) successive translates to obtain a path to \(F^kD\).
For sufficiently large \(k\), \(FD\) and \(F^kD\) have no common curve, since an equality between the iterates of a given pair of curves at two distinct exponents would give a periodic curve.
The concatenated path thus satisfies the common-curve condition in Agol's construction.
His volume bound charges at most two regular ideal octahedra per move, and the mapping torus of \(F^k\) is a degree-\(k\) cover of that of \(F\).
Dividing by \(k\) gives \(\operatorname{vol}(M_F)\le 2v_{\rm oct} L\), with \(v_{\rm oct}\) the volume of the regular ideal octahedron. [Agol, Section 2 and Corollary 2.4](../audits/literature/Ago03/readme.md)

At fixed genus and fixed coefficient support, the curve representatives and their separate levels in the mapping torus of the chosen lift of \(R\) can also be fixed in advance.
Drilling one horizontal curve for each twist gives at most \(3|I|+1\) boundary tori.
Filling a drilled curve at reciprocal integral twist slope in the fiber framing inserts the corresponding twist power, as is seen by cutting along the fiber and regluing its annular neighborhood by the twist.
Thus the same drilled manifold supplies every choice of coefficient magnitudes for this support.
The volume estimate above comes from the pants path and holds irrespective of the geometry of this common drilled manifold.
For bounded \(|I|\) this construction costs at most logarithmically many moves in the genus.
The displayed arithmetic bound still contains at least \(1+h\) in its second entry for every polynomial under consideration.
If \(g\) is odd this contribution comes from the shift.
If \(g\) is even, some \(i\in I\) must be odd, since otherwise all nonzero exponents of \(P\) would be even.
Consequently the estimate leaves a degree-dependent cost even for a sparse strict record.

<a id="linear-bound"></a>
## An explicit linear bound from a fibered two-component link

Stoimenow's Theorem 4.1 already yields the linear dependence after filling a link exterior.
Put \(z=t^{1/2}-t^{-1/2}\) and \(\Delta(t)=z\,t^{-g}P(t)\).
The symmetric Laurent polynomial \(t^{-g}P(t)\) lies in \(\mathbb Z[t+t^{-1}]=\mathbb Z[z^2]\), so the corresponding Conway polynomial belongs to \(z\mathbb Z[z^2]\), the admissibility condition for two components.
Its Alexander polynomial is monic with span \(d=2g+1>1\).
Stoimenow constructs a fibered hyperbolic two-component link in \(S^3\) with this polynomial and exterior volume at most \(20v_{\rm tet}(d-1)=40v_{\rm tet}g\). [Stoimenow, Section 2.3 and Theorem 4.1](../audits/literature/Sto10/readme.md)

The infinite cyclic cover for total linking number is the pullback of the fiber bundle to the real line.
It retracts to the fiber, and its deck transformation acts on homology by the monodromy up to inversion.
Thus the one-variable Alexander polynomial, the order of this homology module, agrees up to normalization with the characteristic polynomial on the fiber.
In the monic integral normalization the latter is \((t-1)P(t)\), which is invariant under reversal up to sign.
Fill the exterior along both page boundaries, extending the monodromy by the identity over the two capping disks.
The map from the homology of the fiber to that of its capped surface is surjective with kernel generated by either oriented boundary circle, since the two boundary classes sum to zero.
The action fixes this rank-one kernel, so the capped monodromy has characteristic polynomial exactly \(P\).
The homological criterion makes this closed bundle hyperbolic, and its two-cusp filling strictly lowers volume by Thurston's Theorem 6.5.6. [Homological criterion](../audits/literature/MS07/readme.md) [Thurston's lecture notes](../audits/literature/Thu80/readme.md)

## Assessment history

### Decision volume-from-coefficient-positions

| Field | Value |
| --- | --- |
| date | 2026-11-27T12:07 |
| status | proved |
| reason | The checked surface construction realizes the full polynomial and bounds pants moves independently of the coefficient magnitudes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Volume upper bound](#upper-bound) | Explicit position-dependent bound for reciprocal compressed irreducible polynomials. |
| argument | [Homology action](#homology) | Exact realization of the coefficient factors and handle shift. |
| argument | [Pants decompositions](#trees) | Tree displacement and local lifts of the twist factors. |
| argument | [Volume bound](#volume) | Volume per pants move, the common drilled manifold and the logarithmic limitation. |
| argument | [Explicit linear bound](#linear-bound) | Two-component fibered link, capping and hyperbolic volume decrease. |
| dependency | [Matrix construction](#homology) | Margalit and Spallone's symplectic realization and pseudo-Anosov criterion. |
| dependency | [Path-volume estimate](#volume) | Agol's octahedral volume cost of the elementary pants moves. |
| dependency | [Fibered link](#linear-bound) | Stoimenow's two-component realization of the normalized Alexander polynomial. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1280.md#finding) | All five sections, including the linear bound. |

## Current assessment

[Selected decision](#decision-volume-from-coefficient-positions)
