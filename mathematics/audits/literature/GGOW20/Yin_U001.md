---
author: Yin
---

# Free-Field Rank and Finite-Dimensional Obstructions

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Source/version: GGOW20, [published full article](../../../literature/pdf/GGOW20.pdf), *Foundations of Computational Mathematics* 20 (2020), 223-290.

Passages: Locators: Theorem 1.4, p. 227 (PDF 5); Sections 1.1-1.3, pp. 228-233 (PDF 6-11), especially Theorems 1.5, 1.7, 1.9, 1.17 and Remark 1.19; Section 1.6, pp. 237-240 (PDF 15-18).

Inspection: Record: 2026-09-12, the operator-scaling source reviewer; source reading and self-review.


<a id="ggow20-u001"></a>
## GGOW20-U001 - Rank, shrunk subspaces, and matrix substitutions

- Source/version: GGOW20, [published full article](../../../literature/pdf/GGOW20.pdf), *Foundations of Computational Mathematics* 20 (2020), 223-290.
  The retained key is GGOW20; the paper's title is *Operator Scaling: Theory and Applications*.
- Locators: Theorem 1.4, p. 227 (PDF 5); Sections 1.1-1.3, pp. 228-233 (PDF 6-11), especially Theorems 1.5, 1.7, 1.9, 1.17 and Remark 1.19; Section 1.6, pp. 237-240 (PDF 15-18).
- Record: 2026-09-12, the operator-scaling source reviewer; source reading and self-review.
  Statements and elementary translations checked; the cited free-field and invariant-theory foundations are retained external inputs, not independently reproved here.
- State: `Read` for the aggregate external equivalence theorem; the elementary range and block translations below were fully checked.
  No whole-foundation proof certification is implied.

### Exact interface and definitions

Let \(A_1,\ldots,A_m\in M_n(\mathbb C)\), \(n\geq1\), and let \(x_1,\ldots,x_m\) be freely noncommuting indeterminates.
Put

\[
 L(x)=\sum_i A_i x_i,\qquad
 \mathcal L(U)=\sum_i A_iU,\qquad
 T_A(P)=\sum_i A_i P A_i^*.
\]

The scalar matrices commute with the indeterminates, so the source's \(\sum_i x_iA_i\) is the same pencil.
Write \(\mathbb C\langle x\rangle\) for the free algebra and \(\mathbb C(\!\langle x\rangle\!)\) for its universal skew field of fractions.
The *inner rank* is the least \(r\) admitting a factorization \(L=KM\) through an \(r\)-dimensional intermediate free module over the free algebra.
Theorem 1.17 identifies it with the rank over the free field; for a linear pencil the factors can be chosen affine linear.

A *shrunk subspace* is a subspace \(U\subseteq\mathbb C^n\) such that \(\dim\mathcal L(U)<\dim U\).
Theorem 1.4 gives the following equivalent failures of full rank:

1. \(L\) is not invertible over the free field, or equivalently has inner rank below \(n\).
2. \(L\) has a shrunk subspace.
3. After invertible scalar changes of row and column bases, \(L\) has an \(i\times j\) zero block with \(i+j>n\).
4. For every \(d\geq1\) and every \(D_1,\ldots,D_m\in M_d(\mathbb C)\), the matrix \(\sum_iD_i\otimes A_i\) is singular.
   Equivalently its determinant is identically zero in the commuting entries of the \(D_i\).
5. \(T_A\) is *rank decreasing*: some positive semidefinite \(P\in M_n(\mathbb C)\) satisfies \(\operatorname{rank}T_A(P)<\operatorname{rank}P\).
6. The tuple \(A\) is in the null cone for the left-right special-linear action, namely all homogeneous invariant polynomials of positive degree vanish at \(A\).

For the action use \((B,C)\cdot A_i=BA_iC^{-1}\), with \(B,C\in SL_n(\mathbb C)\).
The paper writes \(BA_iC\) and explicitly acknowledges the group-action convention in footnote 20, p. 238.
Inversion of the right parameter leaves the orbits and invariant polynomials unchanged.

Theorem 1.17 also gives the quantitative form

\[
 \operatorname{nc-rank}L
 =n-\max_{U\subseteq\mathbb C^n}
       \bigl(\dim U-\dim\mathcal L(U)\bigr).
\]

This is the zero-block characterization expressed using subspaces, not an additional project theorem.
Indeed a zero block with \(i+j=2n-r\) exhibits a \(j\)-dimensional \(U\) with image of dimension at most \(n-i\); conversely choose domain and codomain bases adapted to \(U\) and \(\mathcal L(U)\).
Include \(U=0\), so the maximum is nonnegative.

### Checked mechanisms and retained foundations

For \(P\geq0\) with range \(U\), finite-dimensional positivity gives

\[
 \ker T_A(P)=\bigcap_i\ker(P^{1/2}A_i^*),
 \qquad \operatorname{ran}T_A(P)=\sum_i A_iU.
\]

Thus the rank-decrease and shrunk-space conditions agree.
A basis change converts a shrunk space to the zero block described above and back.
These elementary arguments were checked in full and agree with the existing [MSY23 inner-rank audit](../MSY23/Yin_U001.md#msy23-u001), which reconstructs the relevant homogeneous-pencil interface.

The free-field/inner-rank/hollow-matrix results are imported from the source's Cohn and Fortin-Reutenauer references, with the existing MSY23 review supplying a separately checked interface.
Theorem 1.4's matrix-substitution characterization and Theorem 1.23's determinantal description of the invariant ring are accepted as the established external foundations stated in this identified source.
Their original papers' complete proofs were not reopened.
This is the external premise used by [U002](Yin_U002.md#ggow20-u002) to obtain a nonzero finite-dimensional determinant; the audit does not manufacture a blow-up witness by assuming the capacity bound being proved.

The positive-degree generators in Theorem 1.23 have the form \(\det(\sum_iD_i\otimes Y_i)\).
Consequently vanishing of every such determinant is exactly null-cone membership.
The degree bounds in Theorems 1.25-1.26 are contextual statements, not premises of the full article's revised capacity proof.
In particular the displayed \(\sigma(n)\leq n-1\) is used only for \(n\geq2\); \(n=1\) is handled directly and should not be read as allowing a dimension-zero determinant test.

### Rational syntax, coefficient fields, and use limits

Theorem 1.5's rational-expression description is used with **valid expressions**, meaning there is a matrix substitution of some size at which every inverse in the expression exists.
An expression with no evaluation domain, such as \(0^{-1}\), is not an element of the free field.
Equality is agreement on common matrix domains at all sizes; one scalar substitution, or even one fixed matrix size, is insufficient.
The source gives a summary of this construction rather than a full domain-intersection proof; see the existing [Yin20 audit](../Yin20/readme.md) for the repository's rational-syntax conventions.

Theorem 1.9 and Corollary 1.10 concern **formulas** with division, and the algorithm uses their descriptions.
Do not extend this to arbitrary compressed circuits or a black-box evaluation oracle without the respective reduction and complexity bound.
Theorem 1.1's deterministic bit-complexity claim is for rational input (integer matrices after denominators are cleared), not an effective finite-bit encoding of arbitrary complex numbers.
The equivalences stated here are safely stated over \(\mathbb C\); the source itself separates characteristic and field-size restrictions.

Remark 1.19 allows an affine pencil \(A_0+\sum_iA_ix_i\) to be homogenized for **algebraic rank computation** by adding \(x_0A_0\).
It does not authorize deleting the constant coefficient from a shrunk-space test or identify analytic evaluation domains after setting \(x_0=1\).

No item above produces a bounded inverse in a represented von Neumann algebra.
Passing to affiliated evaluation requires its own injectivity/rank-preservation theorem, such as the separately audited MSY23 interfaces.
Algebraic full rank, positive capacity and approximate operator scaling are not sufficient assertions of an operator-norm spectral gap.
The present intake creates no new project Claim or automatic reassessment of Yin_T_F0001.

### Verification and revisions

The full journal definitions and theorem statements were read directly, and PDF pp. 5, 10-11 were rendered to inspect the rank and block conventions.
Introductory historical and algorithmic comparisons are reading coverage only; their cited papers were not recursively audited.
No formal verification or algorithm execution was performed.
This initial unit supersedes the abandoned conference-only review plan; no assessment of the nine-page conference proof sketch is transferred to the full article.
