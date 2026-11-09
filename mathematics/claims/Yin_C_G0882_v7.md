---
author: Yin
---

# Two distinct unit atoms in the five residual degree-seven models

<a id="statement"></a>
## Statement and inherited setting

Use the fixed negative-one setting of [C882v6](Yin_C_G0882_v6.md#statement): conductor \(19683\), cut \(k=1990\), the prescribed signs and norm \(2^{4391}\), strict endpoint, and \((K,L,N,U)=(3,4,7,1)\).
The present statement concerns the residual moment interface, without asserting that any residual triple comes from an integral input.
Its five triples and cut interval are exactly
\[
 \mathcal R=\{(10,18,27),(11,20,33),(11,20,34),(11,21,36),(11,21,37)\},
 \qquad I=[-1609663/10^6,-1609662/10^6].
\]
For each \((O,V,W)\in\mathcal R\), define the linear functional \(\mathcal D\) on real polynomials of degree at most seven by
\[
\begin{split}
 \mathcal D(1)&=1,\qquad
 \mathcal D(t)=\mathcal D(t^2)=\mathcal D(t^3)=-2,\qquad
 \mathcal D(t^4)=-10,\\
 \mathcal D(t^5)&=48-5O,\qquad
 \mathcal D(t^6)=-44+12O-6V,\qquad
 \mathcal D(t^7)=-7O+14V-7W-2.
\end{split}
\]
These are the same seven trace differences and constant trace difference as in C882v6.

For each triple there exist two fixed distinct rational numbers \(-2<a<b<2\), independent of \(c\in I\), with the following property.
For every \(c\in I\), there is a step function \(w_c:[-2,2]\to[0,1]\) on the 256 cells with endpoints \(t_i=-2+i/64\), such that, simultaneously for every real polynomial \(f\) of degree at most seven,
\[
 \boxed{\mathcal D(f)+f(c)=f(a)+f(b)
                    -\int_{-2}^2w_c(t)f'(t)\,dt.}
 \tag{1}
\]
The atomic measure on the right is exactly \(\delta_a+\delta_b\): there are two distinct atoms and each has mass one.
The masses are fixed constants, not optimization variables or unrestricted positive weights.

In particular, writing \(V_-(f)=\int_{-2}^2\max(0,-f'(t))\,dt\), one has
\[
 \mathcal D(f)+f(c)-V_-(f)\le f(a)+f(b)
                          \le2\max_{[-2,2]}f.
 \tag{2}
\]
The actual unpaired pole \(b_{7851}\) lies in the interior of \(I\), so these identities and inequalities apply to its cut position.
Both trace atoms lift to reciprocal pairs of unit-circle points.
Thus the seven-moment system and \(0\le w\le1\) remain compatible with two distinct individual exceptional trace roots having exterior radii one.
Restoring this two-unit-atom condition alone does not exclude any of the five residual triples or force a positive complete-Mahler gap within that relaxed system.
No actual integral \(h\), polynomial \(Q\), complete root pairing, or original \(P\) with \(M(P)=1\) is asserted to exist.

## Inputs and computation scope

[C882v6 statement](Yin_C_G0882_v6.md#statement) supplies the exact five-triple residual set, functional \(\mathcal D\), and cut interval.
[C882v6 complete-root argument](Yin_C_G0882_v6.md#whole-measure) supplies the meaning of the two exceptional traces and their exterior radii in the original construction.
[C882v6 interval proof](Yin_C_G0882_v6.md#relaxation-barrier) supplies the actual cut inclusion and the earlier unrestricted mass-two comparison.
The thirteen strict complete-measure bounds and their proofs remain at that fixed version; they are not part of the new assertion here.

[J151 two-atom program](../computations/programs/Yin_J_G0151/two_atom_models.py) supplies the five fixed rational atom pairs, fixed-one and free occupancy columns in `MODELS`, and the default exact verifier.
[J151 finite specification](../computations/programs/Yin_J_G0151/two_atom_models.md#certificate) supplies the seven-row matrix and forty rational control systems, with the exact inherited native polynomial and cut helpers.
The program verifies that every pair is distinct and lies in \((-2,2)\), that its five rows correspond exactly to \(\mathcal R\), and that every required rational system has the stated bounded solution.
These fixed finite certificates are the computational inputs to the proof below.
The optional bounded numerical search only proposed the retained roots and columns; numerical feasibility is not a premise.
The [independent complete finding](../audits/reviews/Yin_R_G1107_v19.md#two-atom-models-review) checks this assembly and all fixed rational systems; the assessment below adopts that exact scope.

<a id="two-atom-argument"></a>
## Two fixed unit atoms and the finite rational systems

Fix one triple and its rational pair \((a,b)\) in the native `MODELS` table.
Use \(q_j=T_j\), \(1\le j\le7\), with the convention \(T_j(z+z^{-1})=z^j+z^{-j}\).
For occupancies \(\omega_i\) on the cells \([t_i,t_{i+1}]\), define the rational matrix and right side
\[
 A_{j,i}=q_j(t_i)-q_j(t_{i+1}),\qquad
 g_j(c)=\mathcal D(q_j)+q_j(c)-q_j(a)-q_j(b),
 \quad 1\le j\le7,\quad0\le i<256.
\]
The two atomic values enter \(g\) with coefficients exactly one before solving any system.
Each occupancy column equals \(-\int_{t_i}^{t_{i+1}}q_j'(t)\,dt\), so \(A\omega=g(c)\) is exactly (1) on the seven nonconstant basis elements.
For the constant basis element it holds identically, since \(\mathcal D(1)+1=1+1=2\) and the integral is zero.

The certificate fixes some occupancy coordinates at one and exactly seven distinct coordinates as free; all remaining coordinates are zero.
Their complete finite lists are given in the same native row, and the free set is disjoint from the fixed-one set.
Let \(F\) denote the fixed-one indices and \(J\) the seven free indices.
The corresponding seven-column matrix \(A_J\) is nonsingular, as checked by exact rational elimination.

Write \(c=c_0+\delta s\), where \(c_0=-1609663/10^6\), \(\delta=10^{-6}\), and \(0\le s\le1\).
Since every \(g_j(c)\) has degree at most seven, there are rational control vectors \(g^{(r)}\) with
\[
 g(c_0+\delta s)=\sum_{r=0}^7g^{(r)}\binom7r s^r(1-s)^{7-r}.
\]
These are exact polynomial coefficients, not values at sampled cut positions.
Explicitly, if a component expands as \(\sum_{m=0}^7A_ms^m\), its \(r\)-th control is \(\sum_{m=0}^rA_m\binom rm/\binom7m\).
The fixed atom values are subtracted from every control, because the Bernstein weights sum to one.

For each \(r=0,\ldots,7\), solve
\[
 A_Jx^{(r)}=g^{(r)}-\sum_{i\in F}A_i.
 \tag{3}
\]
For all five triples, the default rational verifier solves these forty systems and checks the solutions by direct substitution.
Every one of the seven coordinates in every solution satisfies
\[
                 \frac1{1000}<x_j^{(r)}<\frac{999}{1000}.
 \tag{4}
\]
Reinsert the fixed zero and one coordinates to obtain \(\omega^{(r)}\in[0,1]^{256}\) with \(A\omega^{(r)}=g^{(r)}\).
Thus the finite certificates already impose the two fixed unit atoms and all seven nonconstant moment equations simultaneously.

<a id="whole-interval"></a>
## Whole-interval construction and exact method boundary

For \(c=c_0+\delta s\), define
\[
 \omega(c)=\sum_{r=0}^7\omega^{(r)}\binom7r s^r(1-s)^{7-r}.
\]
The weights are nonnegative and sum to one.
Consequently \(\omega(c)\in[0,1]^{256}\), its fixed coordinates remain fixed, and linearity gives \(A\omega(c)=g(c)\) for every \(c\in I\).
Let \(w_c\) take these occupancy values on the corresponding cells; values at cell boundaries can be assigned arbitrarily without changing the integrals.
The preceding matrix identity proves (1) on \(T_1,\ldots,T_7\), and the constant identity was already checked.
Since \(1,T_1,\ldots,T_7\) span all real polynomials of degree at most seven, (1) holds simultaneously for every test in that space.

Pointwise, \(0\le w_c\le1\) gives \(-w_cf'\le\max(0,-f')\).
Subtracting \(V_-(f)\) from (1) yields the first inequality in (2), and the second follows from \(a,b\in[-2,2]\).
The strict interior condition \(-2<a<b<2\) also gives unit-modulus roots for both \(z^2-az+1\) and \(z^2-bz+1\).
Hence both proposed exceptional exterior radii equal one and their product is one in the relaxed model.
This establishes an exact feasible model even after replacing an arbitrary positive measure of mass two by two distinct atoms of mass one each.

The occupation functions constructed here need not be indicators of disjoint actual pairing intervals terminating at the fixed poles.
They do not reconstruct the remaining trace roots or impose the full integral and resultant constraints of the original construction.
Thus this strengthened feasibility statement identifies a remaining relaxation boundary; it neither produces a counterexample nor precludes an argument using those additional constraints.
Its scope is the five fixed triples, the stated cut interval and all real polynomial tests of degree at most seven.

## Assessment history

### Decision two-unit-atoms-19683

| Field | Value |
| --- | --- |
| date | 2026-11-09T14:23 |
| status | proved |
| reason | Complete independent review and a separate monomial-basis rational reconstruction verified all five fixed two-unit-atom models, forty systems and whole-interval quantifiers; actual integer and pole-pairing realization remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Two unit atoms](#statement) | Five residual triples, two distinct fixed rational atoms of unit mass, all cut positions and all real polynomial tests of degree at most seven. |
| argument | [Exact finite systems](#two-atom-argument) | Seven occupancy rows, fixed atomic terms, constant identity, all forty systems and strict control bounds. |
| argument | [Whole interval and boundary](#whole-interval) | Bernstein convex combinations, simultaneous identities, negative variation, unit-circle lifts and the remaining original-realization obligations. |
| dependency | [Inherited residual interface](Yin_C_G0882_v6.md#statement) | Exact five triples, trace functional and cut interval. |
| dependency | [Original root interpretation](Yin_C_G0882_v6.md#whole-measure) | Meaning of the exceptional trace roots and complete Mahler product. |
| dependency | [Cut inclusion](Yin_C_G0882_v6.md#relaxation-barrier) | Actual unpaired pole lies in the stated interval. |
| dependency | [Fixed native models](../computations/programs/Yin_J_G0151/two_atom_models.py) | Five MODELS rows, forty exact control systems and necessary inherited helpers; no numerical proposal as proof. |
| review | [Independent complete finding](../audits/reviews/Yin_R_G1107_v19.md#two-atom-models-review) | Entire C/J assembly, default reproduction, independent monomial-basis rational checks and exact scope limits. |

## Current assessment

[Selected decision](#decision-two-unit-atoms-19683)
