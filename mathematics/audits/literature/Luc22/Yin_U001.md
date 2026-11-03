---
author: Yin
---

<a id="luc22-u001"></a>
# Luc22-U001: Determinant conventions and the four group Lehmer constants

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Luc22, [retained PDF](../../../literature/pdf/Luc22.pdf), Wolfgang Lück, *Lehmer's Problem for arbitrary groups*, arXiv:1901.00827v2, 16 September 2020, 25 pages. The publication-year key is Luc22; this inspection concerns the preprint, not a presumed identical journal rendering.

Passages: Sections 0--5, pp.1--9; Section 9, p.19; Appendix 14, pp.20--24. Printed and PDF pages coincide.

Inspection: 2026-10-06T06:51, human record author Yin. An assigned AI reviewer read the complete mathematical body and checked this unit's definitions, finite-dimensional calculations and transfer arguments. Rendered pp.6,8,22,23 were inspected. This record was self-checked; no independent human review or formal verification is asserted. Original proofs cited from other works were not recursively audited.


## Assessment and reuse boundary

**Audited within scope after the explicit corrections below** for the determinant convention, four infima, subgroup/finite-index transfers, finite-group estimates and torsion obstruction.
**Questioned as printed** for the spectral-density domain in Definition 14.11 and the dimension formula in Lemma 14.8.
Several proof displays in Section 5 also require correction.
The statements of Lemma 5.1 survive the checks and repairs given here.

This unit supplies the conventions used by [Luc22-U002](Yin_U002.md#luc22-u002) and [Luc22-U003](Yin_U003.md#luc22-u003).
It allocates no project Claim or Task.
The source's 2020 statements about the status of soficity, determinant approximation and other conjectures are historical reports, not independently refreshed present-day status claims.

<a id="luc22-von-neumann-dimension"></a>
## Group algebra, trace and dimension

The source uses the left regular action on $\ell^2(G)$ and $\mathcal N(G)=B(\ell^2G)^G$.
Right multiplication by a matrix acts on row vectors: $r_A^{(2)}:\ell^2(G)^r\to\ell^2(G)^s$, and $r_{AB}^{(2)}=r_B^{(2)}\circ r_A^{(2)}$.
The algebra embedding of $\mathbb CG$ into $\mathcal N(G)$ in Section 14.1 sends $g$ to right multiplication by $g^{-1}$.
These two conventions should not be silently identified in noncommutative calculations.

The canonical group trace is $\tau_G(T)=\langle T(e),e\rangle$, with $\tau_G(I)=1$.
On matrices the trace is $\operatorname{Tr}_r\otimes\tau_G$, the **sum** of diagonal group traces, not that sum divided by $r$.
Thus $\dim_{\mathcal N(G)}\ell^2(G)^r=r$.
A finitely generated Hilbert $\mathcal N(G)$-module is a Hilbert space with isometric $G$-action admitting an isometric equivariant embedding into such a finite direct sum.
Its dimension is the trace of a projection onto it.
For finite $G$, dimension is complex dimension divided by $|G|$.

The corrected weak-exactness formula is

$$
\dim_{\mathcal N(G)}V_1
=\dim_{\mathcal N(G)}V_0+\dim_{\mathcal N(G)}V_2
$$

for $0\to V_0\to V_1\to V_2\to0$ weakly exact.
A weak isomorphism means injective with dense image.
For an operator between equal finite free ranks, injectivity and dense image are equivalent, by dimension additivity and the adjoint.
This equivalence does not hold between arbitrary unequal ranks.
The source cites [26, Theorem 1.12 and Lemma 1.13] for these standard Hilbert-module facts; their precise interfaces are stated in the appendix, but their original proofs were not inspected here.

<a id="luc22-kernel-removed-determinant"></a>
## The determinant excludes the kernel

For a bounded equivariant map $f:U\to V$ between finitely generated Hilbert modules, put $|f|=(f^*f)^{1/2}$.
Use the corrected spectral distribution

$$
F_f(\lambda)=\dim_{\mathcal N(G)}
\operatorname{im}1_{[0,\lambda]}(|f|)\quad(\lambda\ge0),
\qquad F_f(\lambda)=0\quad(\lambda<0).
$$

Equivalently, for $\lambda\ge0$ use the spectral projection of $f^*f$ on $[0,\lambda^2]$.
Definition 14.14 is then

$$
\det_{\mathcal N(G)}(f)
=\exp\left(\int_{(0,\infty)}\log\lambda\,dF_f(\lambda)\right),
\qquad \exp(-\infty)=0.
$$

The atom at zero is discarded.
The positive logarithmic part is finite because $f$ is bounded and the trace is finite; divergence means $-\infty$, not an ambiguous signed integral.
The determinant of the zero map is the empty product $1$.
A nonzero kernel does not force this determinant to vanish.
The term “determinant class” means finiteness of this logarithmic integral.

This is the kernel-removed convention, also discussed in [dlH13-U001](../dlH13/Yin_U001.md#dlh13-kernel-removed-determinant).
It differs from the regularized, unmodified determinant in [Den09-U001](../Den09/Yin_U001.md#fk-determinant), which includes zero spectral mass and is zero for a nontrivial kernel.
For an injective map the two spectral integrals agree.
Their agreement for injective maps does not identify their behavior under specialization, since kernels can appear in a quotient.

For finite $G$, if $s_1,\ldots,s_k$ are the positive singular values on the underlying complex vector space, counted with multiplicity, then

$$
\det_{\mathcal N(G)}(f)
=\left(\prod_{j=1}^k s_j\right)^{1/|G|}.
$$

For an invertible complex matrix on $\mathbb CG^r$ this is $|\det_{\mathbb C}f|^{1/|G|}$, with **no further $1/r$**.
For the trivial group and an arbitrary rectangular integer matrix, the square of the determinant is the product of the nonzero eigenvalues of $AA^*$.
That product is the absolute value of the first nonzero characteristic-polynomial coefficient, hence a positive integer.

Fourier transformation identifies $\mathcal N(\mathbb Z^d)$ with $L^\infty(\mathbb T^d)$, using Haar probability.
For a scalar multiplier $p$, the present determinant integrates $\log|p|$ only over $\{p\ne0\}$.
A nonzero Laurent polynomial has a null zero set and integrable logarithm, so the removed-kernel determinant equals its ordinary Mahler measure.
These standard Fourier and Laurent-polynomial facts are retained external inputs; their original analytic proofs were not re-audited.
For $p=0$ the determinant is $1$; this is why Theorem 2.1 assumes $p\ne0$.
Jensen's formula retains the leading coefficient: $M(p)=|c|\prod_i\max(1,|a_i|)$ after removing a Laurent monomial.

Theorem 14.18 supplies the exact retained determinant interfaces:

- $\det(gf)=\det(f)\det(g)$ if $f$ has dense image and $g$ is injective.
- A block upper-triangular map has the product of diagonal determinants when the first diagonal map has dense image and the second is injective.
- $\det(f)=\det(f^*)=\det(f^*f)^{1/2}=\det(ff^*)^{1/2}$.
- Restriction to $H\le G$ of finite index $n$ raises the determinant to power $n$.
- Induction along an injective homomorphism preserves the determinant.

These are the source's explicit statements from [26, Theorem 3.14 and Lemma 3.15(4)], retained without a new audit of their original proofs.
Unrestricted multiplicativity for singular maps would be false: over the trivial group, $f=0$ and $g=2I$ give $\det(gf)=1$ while $\det(f)\det(g)>1$ on any positive-dimensional space.

<a id="luc22-four-lehmer-constants"></a>
## Four distinct infima

Definition 3.2 takes infima only over determinant values **strictly greater than one**, with entries in $\mathbb ZG$:

| Constant | Admissible maps |
| --- | --- |
| $\Lambda(G)$ | All $r\times s$ matrices, $r,s\ge1$ |
| $\Lambda_1(G)$ | Scalar $1\times1$ matrices |
| $\Lambda^w(G)$ | Square matrices whose operators are weak isomorphisms |
| $\Lambda_1^w(G)$ | Scalar matrices whose operators are weak isomorphisms |

All four candidate sets are nonempty because $2e$ has determinant $2$, and the infima lie in $[1,2]$.
Their evident inequalities are

$$
\Lambda\le\Lambda^w\le\Lambda_1^w,
\qquad
\Lambda\le\Lambda_1\le\Lambda_1^w.
$$

There is no general equality or direct comparison of the two middle constants from the definition alone.
A bound on $\Lambda(G)$ says nothing about possible determinants below $1$.
The stronger dichotomy “one or at least $\Lambda(G)$” also needs the Determinant Conjecture, which asserts $\det_{\mathcal N(G)}r_A^{(2)}\ge1$ for every integral group-ring matrix.
Section 4 reports that the class $\mathcal D$ satisfying this conjecture contains all sofic groups, hence all amenable groups.
Its listed closure interfaces are: a normal kernel in $\mathcal D$ with amenable quotient; directed colimits, with no injectivity required of the structure maps; directed inverse limits; subgroups; and quotients of a group in $\mathcal D$ by a finite normal subgroup.
The section also reports closure properties of sofic groups and inclusion of residually amenable groups.
Those classification/status results and the alternative Farrell--Jones route to determinant one for invertible integral matrices are cited external results, not proofs supplied or independently audited by this paper.

The elementary determinant-one argument is checked: if $A$ is invertible over $\mathbb ZG$, multiplicativity gives $\det(A)\det(A^{-1})=1$; the Determinant Conjecture then forces both factors to equal $1$.
The bounded-support question in Remark 3.6 uses the number of nonzero coefficients, not the degree.
Its cited Dobrowolski estimate is [12] (1991), not the usual degree-dependent 1979 estimate: for a monic noncyclotomic polynomial with nonzero constant term and $k$ nonzero coefficients, it gives $M(p)\ge1+1/(a\exp(bk^k))$ for fixed positive constants $a,b$.
For $\mathbb Z$ nonmonic polynomials have Mahler measure at least $2$, and a Laurent monomial can be removed, so the stated monic input suffices for that bounded-support consequence.
The external quantitative estimate itself was not re-proved or checked in [12].

## Transfers and finite-group calculations

For $H\le G$, induction sends every admissible matrix over $H$ to one over $G$ with the same determinant and preserves injectivity.
Thus all four constants for $G$ are at most their counterparts for $H$.
Conversely, a particular matrix has finite support and comes from a finitely generated subgroup; injectivity of the induced map reflects injectivity before induction.
This proves each constant is the infimum over finitely generated subgroups of its counterpart.

If $[G:H]=n<\infty$, restriction turns an $r\times s$ matrix into an $nr\times ns$ matrix and its determinant into the $n$th power.
Therefore

$$
\Lambda(H)^{1/n}\le\Lambda(G),\qquad
\Lambda^w(H)^{1/n}\le\Lambda^w(G).
$$

The same argument does **not** give corresponding scalar-to-scalar inequalities: restriction changes matrix size.

The finite examples were checked directly:

- $\Lambda(\{1\})=\sqrt2$, attained by the rank-one matrix $\left(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\right)$; the other three constants for the trivial group equal $2$.
- For $C_2=\langle t\rangle$, the two character blocks of a square integral group-ring matrix have integer determinants congruent modulo $2$.
  Their nonzero product cannot have absolute value $2$.
  The scalar $2+t$ attains $\sqrt3$, giving $\Lambda^w(C_2)=\Lambda_1^w(C_2)=\sqrt3$.
- For a scalar $a+bt$, its character values are $a+b,a-b$.
  If both are nonzero the previous bound applies.
  If exactly one is zero, the other is a nonzero even integer, and its reduced determinant is at least $\sqrt2$, attained by $1+t$.
  This supplies the missing lower-bound argument for $\Lambda_1(C_2)=\sqrt2$.
- Restriction and the trivial-group value give $2^{1/4}\le\Lambda(C_2)\le\sqrt2$.
- For $m=|G|\ge3$, restriction gives $\Lambda(G)\ge2^{1/(2m)}$ and $\Lambda^w(G)\ge2^{1/m}$.
  With $N_G=\sum_{g\in G}g$, multiplication by $N_G-e$ has eigenvalue $m-1$ on the trivial summand and $-1$ on its complement.
  It is invertible and has determinant $(m-1)^{1/m}$ in the group normalization.
  This proves the upper bounds on all four constants recorded in Lemma 5.1(4).
- For odd $n$, $\prod_{\zeta^n=1}(1+\zeta)=2$, so $1+t$ gives $\Lambda^w(C_n)=\Lambda_1^w(C_n)=2^{1/n}$.
  For $n=1$ use the trivial-group calculation directly.
  The unrestricted bounds are $2^{1/(2n)}\le\Lambda(C_n)\le\Lambda_1(C_n)\le2^{1/n}$.
- For finite abelian $G$, character decomposition sends a square matrix to square complex blocks.
  Its ordinary determinant in the commutative ring $\mathbb ZG$ has, character by character, precisely those block determinants.
  Hence a weakly invertible matrix and this scalar have equal group determinants and $\Lambda^w(G)=\Lambda_1^w(G)$, as in Remark 5.5.

If orders of finite subgroups of $G$ are unbounded, the last upper bound and subgroup monotonicity force $\Lambda_1^w(G)=1$, and therefore all four constants equal $1$.
The lamplighter group provides such a finitely generated example.
The cited embedding of that group into a finitely presented group is retained as an external input ([26, Remark 10.24]); once supplied, the same conclusion for the containing group follows from the checked subgroup inequality.

## Located corrections

All findings are newly recorded against the existing v2 source; no source PDF was altered.

| ID and priority | Source and problem | Evidence, impact and correction |
| --- | --- | --- |
| F01, P2 | Definition 14.11, p.22, defines $F_f$ on all $\mathbb R$ using $E_{\lambda^2}^{f^*f}$. | For $f=I$ on $\mathbb C$, this gives $F(-2)=1$ and $F(0)=0$, contrary to monotonicity; it cannot define the stated positive Stieltjes measure on $\mathbb R$. Use $\lambda\ge0$ and extend by zero for $\lambda<0$. Definitions 14.11 and 14.14 should also allow $f:U\to V$, as the surrounding prose and applications explicitly do. The corrected determinant above is well-defined. |
| F02, P2 | Lemma 14.8, p.22, repeats $\dim V_0$ as both summands. | The weakly exact sequence $0\to0\to\mathbb C\xrightarrow{I}\mathbb C\to0$ contradicts the literal formula. The second summand is $\dim V_2$. Later dimension arguments use this corrected additivity. |
| F03, P2 | Lemma 5.1(3) proof, p.8, derives $\Lambda_1(C_2)\ge\sqrt2$ from finite-index assertion (2). | Assertion (2) controls $\Lambda$ and $\Lambda^w$, not $\Lambda_1$; restriction of a scalar is a $2\times2$ matrix. The character-value calculation above repairs the lower bound. The subsequent $2^{1/4}$ bound uses $\Lambda(\{1\})=\sqrt2$, not the printed reference to $\Lambda_1(\{1\})=2$. Conclusions survive. |
| F04, P3 | Lemma 5.1 proof, pp.6,8--9, has reversed inequalities and mismatched symbols. | The first proof paragraph must conclude $\Lambda(G)\le\Lambda(H)$ and $\Lambda_1(G)\le\Lambda_1(H)$, as its theorem states. In (5), the upper bound for $\Lambda^w$ needs $\Lambda^w(H)$; the induced determinant equality is $\det_G(r_A)=\det_H(r_B)$; the last lower bound for $\Lambda_1^w$ needs $\Lambda_1^w(H)$. The candidate-set proof above checks each intended formula separately. |
| F05, P3 | Lemma 5.1(4), p.8, omits a sign from the ordinary complex determinant; Example 5.2, p.9, calls its integer map an automorphism. | The ordinary determinant of $N_G-e$ is $(-1)^{m-1}(m-1)$, whose absolute value is used correctly afterwards. The odd cyclic map has integer determinant $2$, so is injective and becomes invertible over $\mathbb C$, but is not a $\mathbb Z$-automorphism. Neither correction changes a determinant bound. |
| F06, P3 | Examples 14.10 and 14.17, pp.22--23. | $M_{\chi_X}$ is an orthogonal projection, not generally unitary. In the $d$-torus integral the indicator set must use $\mathbb T^d$, not $S^1$ for arbitrary $d$. These corrections preserve the declared trace and kernel-removal convention. |

## Verification limits

The full relevant source arguments, including the finite abelian reduction and the finite-support passage, were read and reconstructed as above.
The finite-dimensional and spectral counterchecks are exact calculations, not a numerical search.
Source theorem interfaces listed in Appendix 14 were checked for their actual needed assumptions; the separate foundational book proofs, group-class closure theorems, bounded-support estimate and external embedding theorem were not independently read.
No statement is made that all references in the bibliography were audited, or that the literal source is error-free.
