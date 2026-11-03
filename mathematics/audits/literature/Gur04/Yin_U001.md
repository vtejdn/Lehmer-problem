---
author: Yin
---

# Positive Maps, Rank, and the Edmonds-Rado Promise

## Source and inspection

Source edition: This audit reads the user-supplied published article by Leonid Gurvits, *Classical complexity and quantum entanglement*, Journal of Computer and System Sciences 69 (2004), 448-484, DOI [10.1016/j.jcss.2004.06.003](https://doi.org/10.1016/j.jcss.2004.06.003).

Passages: Locators: Definitions 2.1, 2.3, 2.5-2.6; Theorem 2.7; Example 2.9; printed pp. 450-456 / PDF pp. 3-9.

Inspection: Definitions and the elementary rank/ERP boundary are audited within this scope.


The sole bibliography is the Gur04 intake.

Edition: published JCSS article, 37 PDF pages; printed page equals PDF page plus 447.
Current artifact identity; the original review date and scope below are retained.

## Gur04-U001

- Source/version: Gur04, supplied published PDF, JCSS 69 (2004), pp. 448-484; exact artifact in the [source record](readme.md#source-version).
- Locators: Definitions 2.1, 2.3, 2.5-2.6; Theorem 2.7; Example 2.9; printed pp. 450-456 / PDF pp. 3-9.
- Record: 2026-09-12, source-audit agent; self-review.
Definitions and the elementary rank/ERP boundary are audited within this scope.
Theorem 2.7's full matroid-intersection dependency is read, not independently audited.
- Kind: definitions, exact source interface, and limitation example.

<a id="positive-maps-and-rank"></a>
### Definitions and conventions

Let \(M_N=M_N(\mathbb C)=\mathcal B(\mathbb C^N)\), with the ordinary, unnormalized trace \(\operatorname{Tr}\).
A complex-linear map \(T:M_N\to M_N\) is positive when \(X\geq0\) implies \(T(X)\geq0\).
Its adjoint \(T^*\) is for the Hilbert-Schmidt inner product \(\operatorname{Tr}(XY^*)\).
The source denotes matrix adjoints by a dagger; stars on maps here have the same meaning as in the source.

For a completely positive map, use a Kraus presentation

\[
T(X)=\sum_{i=1}^k A_iXA_i^*,\qquad
T^*(X)=\sum_{i=1}^k A_i^*XA_i.
\]

Its Choi matrix is \(\mathrm{CH}(T)=[T(E_{ij})]_{i,j=1}^N\).
Complete positivity is equivalent to positivity of this block matrix; the source cites Choi [9] for this standard finite-dimensional equivalence.
That original proof was not inspected.
All subsequent statements about merely positive maps remain meaningful without a Kraus presentation.

The source calls \(T\) **rank non-decreasing** if

\[
\operatorname{rank}T(X)\geq\operatorname{rank}X\quad(X\geq0),
\]

and **indecomposable** if the inequality is strict whenever \(0<\operatorname{rank}X<N\).
Its **doubly stochastic** normalization means \(T(I)=T^*(I)=I\).
Write

\[
\mathrm{DS}(T)=\|T(I)-I\|_{\mathrm{HS}}^2+
\|T^*(I)-I\|_{\mathrm{HS}}^2.
\]

An epsilon-doubly stochastic map in Definition 2.3 satisfies \(\mathrm{DS}(T)\leq\epsilon^2\), not \(\mathrm{DS}(T)\leq\epsilon\).

For \(N=1\), the strict-rank condition defining indecomposability is vacuous, even for the zero map.
Preserve the separate positive-capacity hypothesis when invoking exact scaling in [U003](Yin_U003.md#gur04-u003).

<a id="edmonds-rado-property"></a>
### Matrix-space interface and its boundary

Put \(V=\operatorname{span}_{\mathbb C}\{A_1,\ldots,A_k\}\).
For every subspace \(W\subseteq\mathbb C^N\) and its orthogonal projection \(P_W\),

\[
\operatorname{ran}T(P_W)=\sum_i A_iW=VW.
\]

Indeed, the kernel of a sum of positive matrices is the intersection of their kernels.
For arbitrary \(X\geq0\), its positive restriction to its support gives the same range identity with \(W=\operatorname{ran}X\).
Consequently rank non-decrease is exactly

\[
\dim VW\geq\dim W\quad\text{for every }W\subseteq\mathbb C^N.
\]

This depends on \(V\), not the spanning tuple.
If \(V\) contains an invertible matrix, it necessarily holds.
The **Edmonds-Rado property (ERP)** is the additional promise that this necessary condition is also sufficient for an invertible matrix in \(V\).
Equivalently, whenever every matrix of \(V\) is singular, there are subspaces \(W,Y\) with \(\dim Y<\dim W\) and \(VW\subseteq Y\).

Theorem 2.7 supplies ERP when \(V\) is spanned by rank-one matrices \(x_iy_i^*\), whether or not that rank-one presentation is supplied as input.
The rank criterion is equivalent to finding \(N\) indices for which both selected families \((x_i)\) and \((y_i)\) are linearly independent.
The source proves the equivalence with the matroid-intersection rank formula displayed as (10), attributed to its reference [14], Corollary 7.5.17.
That external theorem's original source was not reviewed here; this particular ERP class is a primary-statement-checked Gur04 input with that proof boundary.

The same theorem also permits an invertible \(A\) such that \(T-A(\cdot)A^*\) is completely positive.
The scale of \(A\) matters: if an invertible \(B\) belongs to the Kraus span, its vectorization belongs to the support of \(\mathrm{CH}(T)\), so a sufficiently small nonzero multiple of \(B\) yields this positive rank-one subtraction.
An arbitrary fixed invertible \(B\) need not do so.

### Checked counterexample: ordinary rank is a different problem

Example 2.9, printed p. 456, takes \(N=3\), \(A_{ij}=E_{ij}-E_{ji}\) for \(i<j\), and

\[
T(X)=\frac12\sum_{i<j}A_{ij}XA_{ij}^*.
\]

Directly \(\sum A_{ij}A_{ij}^*=\sum A_{ij}^*A_{ij}=2I\), so this map is doubly stochastic and rank non-decreasing.
Every matrix in its Kraus span is skew-symmetric of odd size, hence singular: \(\det A=\det A^{\mathsf T}=\det(-A)=-\det A\).
This source example rules out the unqualified inference from capacity positivity or approximate scaling to an invertible **scalar** linear combination.
The later references to "Example 2.8" on pp. 462, 466 and 472 refer to this Example 2.9.

### Inspection, intended use, and limits

The displayed range equality, tuple independence, scaled subtraction, and the 3-by-3 example were checked directly.
Positivity of \(T^*\), trace duality and finite-dimensional spectral calculus are retained elementary foundations.
No proof assistant or computational rank search was used.
The elementary proof that double stochasticity prevents rank decrease is supplied in [U002](Yin_U002.md#gur04-u002).

This unit provides conventions for comparing Gur04 with GGOW20 and MS24; it does not register a new project Claim or assert a free-field theorem.
Sections 2.1 F1-F5 were read as a list of ERP examples; their complete simultaneous-triangularization and closure proofs were not audited.
No formal erratum was found in the bounded search recorded in the [source index](readme.md#search-and-coverage).
