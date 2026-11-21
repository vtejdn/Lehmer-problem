---
author: Yin
---

<a id="asz17-u002"></a>
# The point-height bound and the choice of an auxiliary two-torus

In Section 3, Amoroso, Sombra and Zannier prove Theorem 2.3 for a geometric component \(X\) of codimension at least two after bounding the defining degrees, heights and field degree of each component in terms of the original data.
In dimension three, with rational input equations of bounded degree \(d_0\) and logarithmic height at most \(h_0\), equation (3.4) gives \(h(x)\ll_{d_0}1+h_0\) for \(x\in X^\circ\) on a one-dimensional torsion coset.
Here \(h(x)=h(1:x_1:x_2:x_3)\), and \(X^\circ\) excludes all positive-dimensional cosets contained in \(X\), including translates by nontorsion points.
The bound holds independently of the auxiliary two-torus and of whether it cuts out an isolated point at \(x\).
The reduction to components and the two proof branches occupy printed pages 6 and 7. [Retained preprint, Section 3](../../../literature/pdf/ASZ17--arxiv-v2.pdf#page=6)

<a id="isolated"></a>
## Degree and height in the isolated branch

Write \(x_i=\zeta_i\xi^{a_i}\) with \(\xi\) nontorsion, \(a\) primitive, \(A=\|a\|_\infty\), and \(T\) the corresponding torsion curve.
Equation (3.1) chooses a two-dimensional torsion coset \(T_2\supset T\) of degree \(\ll_N A^{(N-2)/(N-1)}\).
For \(E=K(\zeta_1,\ldots,\zeta_N)\), where \(K\) defines the component, primitivity gives \(E(x)=E(\xi)\).
If \(x\) is isolated in \(X\cap T_2\) and \(T_2\) is defined over \(E\), its \(E\)-conjugates are isolated there and Bézout bounds \(D=[E(\xi):E]\le\deg X\deg T_2\), giving (3.2).
Equation (3.3) applies the relative Dobrowolski bound \(h(\xi)\gg_{\varepsilon,[K:\mathbb Q]}D^{-1-\varepsilon}\) over the finite cyclotomic field, because the relative degree there is at most \([K:\mathbb Q]D\).
Equation (3.5) uses \(h(\zeta_i\xi^{a_i})=|a_i|h(\xi)\) and yields \(A h(\xi)\le\sum_i h(x_i)\le N h(x)\).
Thus isolation controls the orbit degree in (3.2), whereas (3.4) controls the height of the original point on \(X\). [Equations (3.1)–(3.5)](../../../literature/pdf/ASZ17--arxiv-v2.pdf#page=7)

For example, in dimension three a pigeonhole argument applied to \(u\mapsto a\cdot u\) on \(\{0,\ldots,M\}^3\) gives a primitive nonzero relation \(a\cdot b=0\) with \(\|b\|_\infty\ll\sqrt A\).
Indeed, for \(M\) a sufficiently large multiple of \(\sqrt A\), there are more inputs than the at most \(3AM+1\) values.
Then \(T_2=\{y^b=\zeta^b\}\) is connected, defined over \(E\), contains \(T\), and has degree \(O(\|b\|_\infty)\) by its cleared binomial equation.
This independently chosen \(T_2\) supplies exactly the necessary degree and field-of-definition properties for (3.2) whenever the point is isolated there.
For mixed-sign exponents the projective degree in the standard embedding is the width of \(\{0,a_1,\ldots,a_N\}\), between \(A\) and \(2A\).
This comparability suffices for all the inequalities here.

<a id="height"></a>
## Antecedent of (3.4) and its parameters in dimension three

ASZ17 credits [Sch00, Appendix, Theorem 1] with the bound for fixed \(X\) and attributes the dependence on the input height to inspection of its proof.
The reference is A. Schinzel's 2000 book with an appendix by U. Zannier.
The separate Schmidt 1996 reference concerns cosets in linear varieties later in the paper. [ASZ17 bibliography](../../../literature/pdf/ASZ17--arxiv-v2.pdf#page=17)

ASZ17 alternatively cites Habegger's Theorem 11 together with the arithmetic Bézout inequality of Krick, Pardo and Sombra, Corollary 2.11.
In Habegger's notation \(r=\dim X\), and his set \((\mathbb G_m^n)^{[s]}\) includes all algebraic subgroups of codimension at least \(s\), also disconnected ones.
For a curve component in a three-torus the parameters are \(n=3,r=1,s=2\).
ASZ17's printed \(r=2\) does not describe this curve.
A torsion translate of a one-torus is contained in a dimension-one algebraic subgroup, obtained by adjoining its translating torsion point.
A positive-dimensional irreducible subvariety of the curve that is 2-anomalous in Habegger's definition must be the curve itself inside a coset of dimension at most one, since the anomalous threshold is \(\max(1,2+\dim H-3+1)\).
Thus the exclusion in \(X^\circ\) puts \(x\) in Habegger's required open set.
Theorem 11(i),(iii) gives \(h(x)\le(2\deg X)^{C(3,1)}(1+h(X))\) in its height conventions, equivalent for points to the projective Weil height up to a bounded additive term in fixed dimension.
At fixed defining degree, the arithmetic Bézout estimate bounds the component degree in terms of \(d_0\) and its height by \(O_{d_0}(1+h_0)\), giving the claimed dependence.
A zero-dimensional component is covered directly by the same component-height estimate.
This verification uses the definition of the anomalous locus and the statement of Theorem 11 on pages 5–6, with no auxiliary \(T_2\) in its hypotheses. [Habegger's Theorem 11 and height conventions](../Hab17/Yin_U001.md#hab17-u001)

<a id="positive"></a>
## A positive-dimensional intersection

In the other branch ASZ17 contains the positive-dimensional component through \(x\) in a maximal anomalous subvariety and invokes the BMZ uniform structure theorem, Theorem 1.4 and its proof's inequality (3.4), for containment in a coset of degree bounded in terms of the original degree and field data.
Intersecting that coset with \(T_2\) gives a component through the positive-dimensional intersection.
If this coset component had dimension one, the intersection component would itself be that coset, contradicting \(x\in X^\circ\).
Therefore the dimension is two, and the containing coset contains \(T_2\) and one of its torsion points.
The containing coset is thus torsion, giving a torsion hypersurface of bounded degree through \(x\), independent of \(h_0\).
For the untwisted subgroup and nontorsion parameter its character gives a bounded integer relation on \(a\).
This branch gives no isolated-point degree estimate for an intersection containing the curve. [Positive-dimensional case, page 7](../../../literature/pdf/ASZ17--arxiv-v2.pdf#page=7)

The source inspection covered the complete proof of Section 3 and its referenced height statement in Habegger at definition and theorem-statement depth.
It uses ASZ17's cited arithmetic Bézout and BMZ inputs at their stated scope without a separate proof audit of either, of Zannier's appendix, or of the relative height theorem.
