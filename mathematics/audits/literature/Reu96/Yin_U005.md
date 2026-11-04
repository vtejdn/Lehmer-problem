---
author: Yin
---

# Exact Inversion Height of Generic Matrix Inverses

## Reu96-U005

- Source: [Reu96](../../../literature/pdf/Reu96.pdf), the 17-page published journal article, Selecta Mathematica 2 (1996), 93-109.
- Locators: Theorem 2.1, printed pp. 96-97 (PDF pp. 4-5); its proof, printed p. 98 (PDF p. 6); height structures and Theorem 2.2, printed p. 97 (PDF p. 5).
- Review: 2026-09-08, the source reconstruction agent; statement and displayed proof read, key formulas visually checked, and the compressed algebraic steps reconstructed below.
  This is an internal mathematical review, not formal verification.
- Purpose: supplies the generic-matrix application for [Reu96 free-field source audit](readme.md#reu96-free-field-source-audit).

### Statement and Setting

Let $k$ be a commutative field and let $X$ contain $n^2$ distinct noncommuting variables $x_{ij}$, with $n\geq1$.
In the universal field of fractions of $k\langle X\rangle$, every entry of

\[
G^{-1},\qquad G=(x_{ij})_{1\leq i,j\leq n},
\]

has inversion height exactly $n$ relative to $k\langle X\rangle$.
Height counts nested scalar inversions in a rational expression and is minimized over all expressions for the element.
It is not the number of inverse symbols in a chosen formula, matrix size in an arbitrary representation, or a numerical conditioning measure.

The result permits additional variables in $X$.
It does not by itself establish unbounded inversion height in a fixed two-variable free field; Section 5.2 discusses that as a suggested direction, as recorded in [U006](Yin_U006.md#reu96-u006).

### Dependencies and Their Inspection Boundary

| Input | Role and inspection depth |
| --- | --- |
| [U001](Yin_U001.md#reu96-u001) | Free tensor rings, universal fields, full matrices, height, and minimal representations. |
| [U004](Yin_U004.md#reu96-u004), Theorem 2.2 | Converts a hypothetical height bound into a height structure on some minimal representation, over a division ring with infinite center and infinite dimension over that center. |
| Reu96 reference [8], P. M. Cohn, *Skew Field Constructions* (1977), cited on printed p. 98 | Embedding under arbitrary extension of the commutative coefficient field. This preserves the polynomial subring and hence cannot increase inversion height. The original reference was not directly read; this part remains secondary-reported. |
| [CR94-U001](../CR94/Yin_U001.md#cr94-u001), Theorem 3.2, Theorem 4.1, and Corollary 4.2 | The scalar free field over $k$ embeds into the free tensor field over $D$; independent left and right families characterize minimality; two minimal representations differ by invertible constant matrices on both sides. Exact primary statements and applicability were checked by the CR94 reviewer and accepted, with original proofs unreviewed. These interfaces assume finite $X$, $k=Z(D)$, infinite $k$, and $[D:k]=\infty$. |

The source also uses the existence, after making $k$ infinite, of a division ring $D$ with center $k$ and $[D:k]=\infty$.
This existence and arbitrary commutative coefficient-extension embeddings remain secondary-reported external inputs; the local calculations below do not construct such a $D$.
The more specific comparison embedding and minimal-representation interfaces are now primary-statement-checked in CR94-U001, with their original proofs unreviewed.

### Fullness and the Upper Bound

Work first over any coefficient division ring $D$ with central field $k$, in the free tensor ring

\[
R=D*_{k}k\langle X\rangle.
\]

A square generic matrix of size $m$ is full: otherwise a factorization through fewer than $m$ columns, evaluated at the assignment sending that generic matrix to $I_m$, would factor $I_m$ through a smaller-dimensional $D$-space.
Such evaluation is a homomorphism of the polynomial free tensor ring; no rational expression is evaluated in this argument.
Every square generic submatrix is full for the same reason.
Their images in the universal field are therefore invertible.

For $n>1$, partition $G$ as

\[
G=\begin{pmatrix}a&b\\c&H\end{pmatrix},
\qquad s=a-bH^{-1}c.
\]

Both $G$ and the generic $(n-1)\times(n-1)$ matrix $H$ are invertible, so $s\neq0$.
The block inverse is

\[
G^{-1}=
\begin{pmatrix}
s^{-1}&-s^{-1}bH^{-1}\\
-H^{-1}cs^{-1}&H^{-1}+H^{-1}cs^{-1}bH^{-1}
\end{pmatrix}.
\]

Induction bounds the height of entries of $H^{-1}$ by $n-1$, that of $s$ by $n-1$, and that of every displayed entry by $n$.
The initial case is the single inverse $x_{11}^{-1}$.
Thus the claimed upper bound uses only legitimate nonzero scalar pivots.

### Genericity: No Nonzero Constant Row-Column Pairing Vanishes

The printed proof asserts that

\[
uG^{-1}v=0,\qquad u\in D^{1\times n},\quad v\in D^{n\times1},
\]

implies $u=0$ or $v=0$.
Here is a reconstruction that uses no numerical sampling or rational specialization.

First, every entry of $G^{-1}$ is nonzero.
For a chosen entry, independently permute rows and columns of $G$ so that the relevant inverse entry is the top-left entry.
The complementary generic $(n-1)\times(n-1)$ block is invertible.
The Schur formula identifies that entry with $s^{-1}$, which is nonzero.
For $n=1$ this is immediate.

Now suppose $u,v$ are nonzero.
Complete $u$ to the first row of an invertible matrix $P^{-1}$ and $v$ to the first column of an invertible matrix $Q^{-1}$ over $D$.
The substitution

\[
G\longmapsto QGP
\]

defines an automorphism of $R$ fixing $D$: its inverse substitutes $Q^{-1}GP^{-1}$.
This follows directly from the universal property of the free tensor ring, with all other variables fixed.
It preserves fullness and extends to the universal field by its universal property.
Consequently every inverse entry of the transformed generic matrix remains nonzero, whereas

\[
e_1^{\mathsf T}(QGP)^{-1}e_1
=e_1^{\mathsf T}P^{-1}G^{-1}Q^{-1}e_1
=uG^{-1}v.
\]

This proves the asserted nonvanishing with the required noncommutative coefficient order.

### Minimality and Constant Equivalence

Fix an entry $f=e_r^{\mathsf T}G^{-1}e_s$.
In CR94's convention, its size-$n$ representation has left family $G^{-1}e_s$ (a column) and right family $e_r^{\mathsf T}G^{-1}$ (a row).

- A left $D$-linear dependence among the left-family entries would be $uG^{-1}e_s=0$.
- A right $D$-linear dependence among the right-family entries would be $e_r^{\mathsf T}G^{-1}v=0$.

The preceding nonvanishing property rules out both unless the coefficient row or column is zero.
The minimality criterion imported from [10, Corollary 4.2] therefore makes this a minimal representation.

Theorem 4.1 of that reference then states that any other minimal representation of $f$ has the form

\[
(\lambda P,\;QGP,\;Q\gamma),
\]

where $\lambda=e_r^{\mathsf T}$, $\gamma=e_s$, and $P,Q\in\mathrm{GL}_n(D)$.
This uses two independently invertible constant matrices; it is not restricted to similarity transformations.

### The Lower Bound and the Height-Zero Case

Suppose, toward a contradiction, that the original entry over $k$ has height at most $n-1$.
Extend $k$ to an infinite commutative field if necessary, and then use the retained embeddings into a free tensor field over a division ring $D$ with infinite center and infinite dimension over that center.
The same rational expression is still valid and has height at most $n-1$ there.
Only nonincrease under extension is needed; equality of heights under extension is not assumed.

By U004 there is a minimal representation with canonically invertible matrix

\[
G'=QGP
\]

and a height function $h:\{1,\ldots,n\}\to\{0,\ldots,n-1\}$.
Recall the exact conditions:

\[
h(i)=0\quad\Longrightarrow\quad g'_{ii}=1,\quad g'_{ij}=0\ (j>i);
\]

if $h(i)\geq1$, let $n(i)=\min\{j>i:h(j)\geq h(i)\}$ when this set is nonempty; then $g'_{ij}=0$ for all $j\geq n(i)$.

If some $i<j$ has $h(i)\leq h(j)$, then $g'_{ij}=0$.
For $h(i)\geq1$, use $n(i)\leq j$ and the second condition.
For $h(i)=0$, use the first condition instead.
If no such pair exists, $h(1),\ldots,h(n)$ is strictly decreasing in a set of $n$ values, so $h(i)=n-i$ and $g'_{nn}=1$.
In every case some entry of $QGP$ is constant.

This is impossible.
The degree-one component of the free tensor ring is

\[
R_1=\bigoplus_{x\in X}(D\otimes_k D)_x.
\]

For a fixed entry $(a,b)$ of $QGP$, choose $i,j$ with $Q_{ai}\neq0$ and $P_{jb}\neq0$, possible because the relevant row and column are nonzero.
Its coefficient in the $x_{ij}$ summand is the nonzero pure tensor $Q_{ai}\otimes P_{jb}$.
Distinct variables belong to different direct summands, so it cannot cancel with another variable's coefficient.
Thus every entry of $QGP$ is nonzero homogeneous of degree one and cannot be constant.
The contradiction proves the lower bound $n$.

### Source Corrections, Verification Facts, and Limits

The source's printed p. 98 cites (2.2) for the zero-entry conclusion even when $h(i)=0$; that case must use (2.1).
The reconstruction above supplies this local case distinction without changing the theorem.

The extracted text misreads several weak inequalities in (2.2).
The rendered page confirms $h(i)\geq1$, $h(j)\geq h(i)$, and $j\geq n(i)$.
These are transcription hazards, not source errors.
The introductory description of height zero as a strictly triangular matrix must be read through (2.1), which requires diagonal entries equal to one.

The proof checks in this unit cover generic fullness, legal Schur pivots, the height upper bound, the nonvanishing constant pairing, both minimal families, the constant-equivalence formula, and the full height-function contradiction.
No computation, proof assistant, or independent web/errata search was performed for this unit.
Foundational free-field facts, the coefficient-extension theorem, and the minimal-representation theorems retain the explicit dependency boundary above.

The main statement is reconstructed under those interfaces and U004.
It provides exact heights for the generic matrix entries at the stated variable count.
It does not establish a uniform formula for nongeneric matrices, invariance under arbitrary field extension, a two-variable unboundedness theorem, or an algorithm computing height.

On 2026-09-08, the family labels were aligned with CR94's column/left and row/right convention; the independence equations and proof were unchanged.
The CR94 interfaces were also updated to the primary statement and applicability checks in CR94-U001.
This does not remove the separate book/existence dependencies or claim an independent review of CR94's original proofs.

Independent review, 2026-09-08: the separate reviewing agent compared this reconstruction with rendered Reu96 p. 98.
It checked fullness by polynomial evaluation, nonzero inverse entries, the invertible two-sided substitution, both independence sides, the degree-one tensor contradiction, and nonincrease under scalar extension.
No additional local gap was found; the external infrastructure retains the stated limits.

## Exact passage and inspection limits


Passages: Theorem 2.1, printed pp. 96-97 / PDF pp. 4-5, and proof, printed p. 98 / PDF p. 6; height structures and Theorem 2.2, printed p. 97 / PDF p. 5.

Inspection: 2026-09-08: generic fullness, upper bound, two-sided minimal families, tensor contradiction and exact lower bound reconstructed and independently reviewed. CR94 primary-statement checks do not remove book/existence and coefficient-extension dependencies or supply original-proof review. No general field-extension invariance, algorithm, independent errata search, computation or formal verification.
