---
author: Yin
---

# Bor96: the Leech chamber quotient and the canonical-reflection boundary

<a id="bor96-u001"></a>
## Source and inspection

Use the [retained publisher scan and bibliographic-year explanation](readme.md#publisher-scan).
The title and opening pages 1--5, including Section 1, were checked visually.
The scan has no usable extracted text layer.
The selected content is Borcherds's exposition of Conway's description of the reflection chamber and its stabilizer for $II_{25,1}$.
The original Conway proof, the Leech covering-radius theorem and the rest of the article were not audited.
This is a concrete boundary for extrapolating the [McM02 degree-18 reflection extension](../McM02/Yin_U002.md#lorentzian-root-subgroup), not a classification of $II_{8k+1,1}$ for all $k$.

<a id="leech-root-convention"></a>
## Lattice and simple-root convention

The source uses a positive Leech lattice $\Lambda$ and
\[
II_{25,1}=\Lambda\oplus II_{1,1},\qquad
(x,m,n)^2=(x,x)-2mn.
\]
Thus the two null basis vectors in this displayed hyperbolic plane have pairing $-1$.
Changing the sign of one null basis vector converts it to the project's convention $(e,f)=1$; the sign convention must be changed in the transvection formula at the same time.

On pages 3--4 the cone-preserving group $\operatorname{Aut}(L)^+$ preserves a selected connected component of the negative cone.
Its reflection subgroup $W$ has a fundamental chamber, and the full cone-preserving group is a semidirect product of $W$ with the chamber stabilizer.
For $II_{25,1}$ the simple norm-two roots of the selected chamber are
\[
r_\lambda=(\lambda,1,(\lambda,\lambda)/2-1),\qquad \lambda\in\Lambda.
\]
Their root reflections act by $s_r(v)=v-(v,r)r$.
The source obtains this chamber using the norm-zero Weyl vector $(0,0,1)$ and Conway's covering-radius argument.

<a id="affine-chamber-quotient"></a>
## Infinite chamber quotient

Page 5 identifies the chamber stabilizer with the affine isometry group of $\Lambda$:
\[
\operatorname{Aut}(II_{25,1})^+
=W\rtimes\bigl(\Lambda\rtimes O(\Lambda)\bigr),
\qquad O(\Lambda)\cong 2\mathbin{.}Co_1.
\]
The text begins this conclusion with the cone-preserving group; this unit does not read the final display's omitted superscript as a separate assertion about the full orthogonal group.
The determinant character and a rational spinor-norm kernel are separate from this choice of cone component.
The chamber quotient contains the free abelian translation group $\Lambda$, so $W$ has infinite index and the quotient is not a bounded-exponent finite group.

For clarity, the coordinate realization of the source's affine translation by $a\in\Lambda$ is
\[
T_a(x,m,n)
=\bigl(x+ma,\ m,\ n+(x,a)+m(a,a)/2\bigr).
\]
This is a direct coordinate translation of the stated chamber action, not a formula printed in the source.
Substitution preserves $(x,x)-2mn$ and sends $r_\lambda$ to $r_{\lambda+a}$, while fixing the null vector $(0,0,1)$.
It is the corresponding integral fixed-cusp transvection in this sign convention.
For nonzero $a$, its image in the chamber quotient has infinite order, even though the individual transvection is unipotent and has Mahler measure one.
Thus no positive power of every permitted cusp translation can be forced into $W$ by the index-two argument applicable to $II_{17,1}$.
This concerns group coverage, not the complete Mahler measure of products involving several cusps.

<a id="canonical-normalization-boundary"></a>
## Root-reflection membership does not by itself supply the canonical spectral action

The displayed roots have pairings
\[
(r_\lambda,r_\mu)=2-\frac12\|\lambda-\mu\|^2,
\]
by direct substitution in the source form.
They are unbounded below as $\lambda-\mu$ ranges through the lattice.
In particular, the actual pairing can be less than $-2$ when the product of the two root reflections has infinite order.
McM02's [canonical geometric representation](../McM02/Yin_U002.md#canonical-coxeter-gap-input) instead normalizes every infinite Coxeter exponent to pairing $-2$ for norm-two simple roots.
The Leech chamber's lattice representation therefore cannot be called that canonical representation solely because its reflections generate a Coxeter group.
Any required spectral comparison or representation transfer would need a separate argument.
An infinite set of simple roots alone is not the decisive obstacle, since an individual finite word uses finitely many simple reflections; the actual Gram normalization still matters.

The change is already present at $k=3$ in $II_{8k+1,1}$.
No conclusion about all $k\ge4$, an effective finite-index bound there, or the unrestricted Mahler gap is supplied by this bounded reading.
