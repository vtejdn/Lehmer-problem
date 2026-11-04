---
author: Yin
---

<a id="reu96-u004"></a>
# Reu96-U004: Inversion Height and Canonical Elimination

- Source: [Reu96](../../../literature/pdf/Reu96.pdf), Christophe Reutenauer, *Inversion Height in Free Fields*, published journal version, 17 PDF pages.
- Locators: Theorem 2.2 and conditions (2.1)-(2.2), printed p. 97 / PDF p. 5; Section 4 and Lemmas 4.1-4.2, printed pp. 105-107 / PDF pp. 13-15.
  Series representation conventions are on printed p. 98 / PDF p. 6.
- Record: 2026-09-08, the Section 4 reconstruction agent; source text read and all of the above rendered pages visually inspected.
  Local proof reconstruction and self-review; source dependency boundaries are listed below.
- Kind: characterization theorem, proof transfer, and elimination mechanism.
- Goal: [Reu96 free-field source audit](readme.md#reu96-free-field-source-audit).
- Prerequisites: [U001, foundations](Yin_U001.md#reu96-u001); [U002, rational series and height bases](Yin_U002.md#reu96-u002).

## Statement and Conventions

Let \(D\) be a division ring whose center \(k\) is infinite, with \([D:k]=\infty\), and use a finite set \(X\) of variables, as in the verified representation interfaces.
Write \(R=D_k\langle X\rangle\) for the free tensor ring, \(F\) for its universal field of fractions, and \(S=D_k\langle\!\langle X\rangle\!\rangle\) for its \(X\)-adic series completion.
Inversion height is measured relative to \(R\); every element of \(D\), including its inverses, therefore has height zero.

For an integer \(\ell\geq0\), Theorem 2.2 states that \(f\in F\) has inversion height at most \(\ell\) if and only if there is a **minimal** linear representation

\[
f=\lambda M^{-1}\gamma,\qquad
\lambda\in D^{1\times n},\quad \gamma\in D^{n\times1},
\]

whose full matrix \(M\in R^{n\times n}\) has entries of \(X\)-degree at most one, is canonically invertible, and admits a height structure at most \(\ell\).

Canonical invertibility uses the specified order \(1<\cdots<n\): eliminate variable \(x_n\) with equation \(n\), then \(x_{n-1}\) with the resulting equation, and continue without pivot permutations.
Every required pivot must be nonzero.
Arbitrary invertibility does not imply this property in a fixed order.

A height structure is a function \(h:\{1,\ldots,n\}\to\{0,\ldots,\ell\}\) satisfying:

1. If \(h(i)=0\), then \(m_{ii}=1\) and \(m_{ij}=0\) for every \(j>i\).
2. If \(h(i)\geq1\), define
   \[
   n(i)=\min\{j>i:h(j)\geq h(i)\}.
   \]
   Then \(m_{ij}=0\) for every \(j\geq n(i)\).
   If the set is empty, take \(n(i)=\infty\), so this last constraint is empty.

Both inequalities involving \(n(i)\) are **weak**.
Replacing either by a strict inequality changes the statement and breaks the block separation used below.
These symbols were checked in the rendered printed p. 97.

The necessity direction needs the stated hypotheses on the center and its dimension through specialization.
The sufficiency argument below is elementary elimination over any division ring and does not use those two infinitude assumptions.
It also does not use minimality; minimality is the stronger conclusion furnished by the necessity direction.

## From Inversion Height to a Minimal Height Representation

### Translation to a rational tensor series

Start with a rational expression \(E\) for \(f\) of inversion height at most \(\ell\).
Section 4 invokes Cohn's specialization lemma to choose finitely many constants \(a_x\in D\) such that, after the translation \(x\mapsto x+a_x\), **every inverted subexpression** has a defined, nonzero value at the origin.
Thus the translated expression \(E'\) defines a rational element \(f'\) of \(S\), with all its inversions taken at units of \(S\).

Nonzero constant terms must hold simultaneously for the denominators throughout this chosen expression, not just for its outermost value.
A translation that merely makes \(f'\) regular as an element would not, without further work, justify the source's expression-by-expression height bound.

The source also invokes a canonical embedding of \(F\) into the universal field of fractions of \(S\), allowing the free-field and tensor-series interpretations to be compared.
This embedding is now a primary-statement-checked input from [CR94-U001](../CR94/Yin_U001.md#cr94-u001), Theorem 3.2.
The book specialization input remains retained separately; acquiring CR94 does not claim to verify its original proof in reference [8].

### Replacing inverses by stars without increasing height

For a proper series \(G\), write \(G^*=(1-G)^{-1}\); a star is counted once in star height.
Process the inversions in \(E'\) from the inside outward.
Suppose the already converted expression to be inverted is \(H\), with nonzero constant term \(d\in D\).

The source explains how to exhibit a proper expression \(Q=d-H\) without increasing the current star height.
Expand sums and products into terms whose nonconstant factors are proper expressions or stars of proper expressions.
In each starred factor use \(G^*=1+GG^*\).
Each resulting nonconstant product then contains a proper factor, while the constant products sum to \(d\).
The operation preserves star depth.

The ordered factorization and inverse formula are

\[
H=d-Q=d(1-d^{-1}Q),\qquad
H^{-1}=(d^{-1}Q)^*d^{-1}.
\]

The factor \(d^{-1}\) is on the **right** of the final star.
No commutation of coefficients of \(D\) with variables is permitted.
Since \(d^{-1}\) has height zero and \(d^{-1}Q\) is proper, this adds at most the one nesting level already occupied by the original inversion.
Induction through the finite expression proves that \(f'\) has star height at most \(\ell\).

### Representation and minimality transfer

Theorem 3.1, audited in [U003-U003](Yin_U003.md#reu96-u003), supplies a minimal series representation

\[
f'=\lambda(1-N)^{-1}\gamma
\]

with the required height structure, where every entry of \(N\) is homogeneous of \(X\)-degree one.

The matrix \(1-N\) is canonically invertible.
Its last diagonal entry has constant term one.
On eliminating that pivot, the remaining Schur matrix again has identity constant matrix: the off-diagonal factors are proper, and the inverse pivot has constant term one.
Repeating this argument makes every successive pivot a series with constant term one, hence nonzero in the common ambient field.
This supplies the source's assertion that canonical solvability is automatic here.

Minimality among series representations is not automatically minimality among all affine linear free-field representations.
Printed p. 106 explicitly invokes [10], Proposition 2.10 and Corollary 4.2, for this passage.
Their exact statements and hypotheses were subsequently checked in the primary source [CR94-U001](../CR94/Yin_U001.md#cr94-u001), printed pp. 522 and 527, and accepted as external inputs with original proofs unreviewed.
Proposition 2.10 gives left and right independence of the series families.
Through CR94's Theorem 3.2 comparison embedding, those same families are independent over \(D\) in the free field.
Corollary 4.2 then gives free-field minimality.
The hypotheses on \(D,k,X\) match; the two optimization problems have not been identified merely by definition.

Finally apply the inverse translation \(x\mapsto x-a_x\).
This is a \(D\)-fixing automorphism of the tensor ring, extended to its universal field.
It preserves the degree-at-most-one condition, zeros, diagonal entries equal to one, and nonzero canonical pivots.
It also preserves minimality: any smaller representation after translation would translate back to a smaller representation of \(f'\).
This gives the representation required for \(f\).

## Block Restrictions: Lemma 4.1

Let

\[
M=\begin{pmatrix}A&B\\ C&D_0\end{pmatrix}
\]

be a canonically invertible matrix, where \(A\) occupies an initial interval of indices and \(D_0\) the complementary final interval.
The subscript distinguishes this block from the coefficient division ring.

The canonical elimination process starts entirely in the final block.
Its pivots are the pivots of \(D_0\), so \(D_0\) is canonically invertible.
If \(B=0\), those elimination steps never alter the initial equations; the remaining pivots are therefore the pivots of \(A\), making \(A\) canonically invertible as well.

The restricted height functions make each diagonal block a height matrix with the corresponding maximal height.
For a row in the final interval, the next eligible index is unchanged.
For a row in the initial interval, its next eligible index either stays inside that interval or disappears, in which case the block has no corresponding upper restriction.
The height-zero diagonal and upper-zero conditions also restrict correctly.

**Local source correction:** in the proof of Lemma 4.1(ii), printed p. 106, the sentence saying that (2.1) holds for “\(A\) and \(B\)” must read “\(A\) and \(D\).”
The claimed lemma and subsequent proof concern the two diagonal square blocks.
This is a block-label error, not a failure of the lemma.

## Height Bound for Inverse Entries: Lemma 4.2

The lemma applies to any canonically invertible matrix \(M\) over a division ring \(K\) with a height structure at most \(\ell\).
It states that every solution coordinate of \(Mx=\gamma\) has the form

\[
x_i=\sum_j b_{ij}\gamma_j,
\]

where each coefficient \(b_{ij}\) has inversion height at most \(\ell\) relative to the entries of \(M\).
In particular, this bounds the entries of \(M^{-1}\).
It does **not** assign height zero to an arbitrary \(\gamma\in K^{n\times1}\).

The argument can be made a precise induction on matrix size, carrying the maximal allowed height as a bound.

### Height zero

All rows have \(h(i)=0\), so \(M\) is unit lower triangular.
Forward substitution

\[
x_i=\gamma_i-\sum_{j<i}m_{ij}x_j
\]

uses only sums and products, with coefficients on the left of each \(\gamma_j\).
Thus every inverse entry has height zero.

### A unique maximal height in the first row

Let \(t=\max_i h(i)>0\), and first suppose \(h(1)=t\) while all later heights are at most \(t-1\).
Write

\[
M=\begin{pmatrix}a&R_0\\ C_0&N\end{pmatrix}.
\]

By Lemma 4.1, \(N\) is canonically invertible and has height structure at most \(t-1\).
Induction gives entries of \(B_0=N^{-1}\) of inversion height at most \(t-1\).
The lower equations give

\[
x'=B_0\gamma'-B_0C_0x_1.
\]

Substitution into the first equation yields

\[
q x_1=\gamma_1-R_0B_0\gamma',\qquad
q=a-R_0B_0C_0.
\]

Canonical invertibility ensures \(q\ne0\): it is the last remaining pivot after elimination of \(N\).
The entries of \(R_0,C_0,a\) have height zero, so \(q\) has height at most \(t-1\), and \(q^{-1}\) has height at most \(t\).
Therefore

\[
x_1=q^{-1}\gamma_1-q^{-1}R_0B_0\gamma'.
\]

Substitute this expression into the displayed formula for \(x'\).
The resulting coefficients involve only sums and products of entries already of height at most \(t\); no further inversion is required.
This bounds all inverse entries by \(t\), with the multiplication order matching the source's printed p. 107.

### Remaining cases: split at the last maximal row

Choose the **last** index \(i\) of height \(t\), and split immediately before it:

\[
M=\begin{pmatrix}A&0\\ C&D_0\end{pmatrix}.
\]

This includes a unique maximal-height row occurring after row one.
The upper-right block is zero for the following reason.
A preceding row of height zero has no nonzero entries to its right.
For a preceding row \(r\) of positive height, index \(i\) is a later index of height at least \(h(r)\); hence \(n(r)\leq i\).
Condition (2.2) annihilates every entry of that row in columns at least \(i\).

The initial block \(A\) can still have maximal height \(t\), but it has smaller size.
The final block \(D_0\) has a unique maximal-height row at its beginning.
Thus induction handles \(A\), and the previous case handles \(D_0\).
Lemma 4.1 supplies their canonical invertibility.
Their inverse blocks combine as

\[
M^{-1}=
\begin{pmatrix}
A^{-1}&0\\
-D_0^{-1}CA^{-1}&D_0^{-1}
\end{pmatrix}.
\]

These products introduce no additional nested inversion, completing the bound.
When \(i=1\), the initial block is absent and the preceding unique-maximum case already applies.
The source's brief “Lemma 4.1 and induction” is valid with this size induction; an induction solely on the maximal height would not justify the initial block \(A\).

### Specialization to the converse of Theorem 3.1

The elimination proof of Lemma 4.2 is independent of Theorem 3.1.
For a series matrix \(T=I-M\), with \(M\) homogeneous of degree one, it directly gives the corresponding **star** bound needed for that theorem's converse.
In the unique-maximum step, the blocks \(R_0,C_0\) are proper, the scalar entry \(a\) has constant term one, and the inverse \(B_0=N^{-1}\) has identity constant matrix.
Thus

\[
q^{-1}=(1-q)^*,\qquad 1-q=(1-a)+R_0B_0C_0
\]

is the star of a proper expression of star depth at most \(t-1\).
It has star depth at most \(t\).
The remaining substitutions and block products introduce no new star.
Height zero again gives a polynomial inverse.
This argument avoids any hidden cost for converting arbitrary inverses to stars, and it avoids a logical cycle: the necessity direction of Theorem 2.2 uses Theorem 3.1, while the independently proved elimination lemma can supply Theorem 3.1's converse.

## Completing Theorem 2.2 and Reuse

Apply Lemma 4.2 to the matrix of the representation.
Its entries belong to \(R\), and \(\lambda,\gamma\) belong to \(D\subset R\), all of height zero.
Hence

\[
f=\lambda M^{-1}\gamma
\]

has inversion height at most \(\ell\) relative to \(R\).
This proves the sufficiency direction.
The elimination lemma supplies an upper bound; it does not by itself prove minimality or a lower bound on inversion height.

This unit supplies the height characterization used by [U005, the generic-matrix argument](Yin_U005.md#reu96-u005).
Applying it to a scalar free field over an arbitrary ground field requires the extension-and-embedding steps recorded there; one cannot drop the infinitude assumptions from the necessity statement without justification.
It also does not assert that inversion height is preserved by arbitrary extension of scalars; [U006](Yin_U006.md#reu96-u006) addresses that issue.

## Dependencies and Verification Boundary

| Input | Source locator and actual inspection | Role and retained limit |
| --- | --- | --- |
| Tensor ring, universal field, affine representations | Reu96 printed p. 97; [U001](Yin_U001.md#reu96-u001) | Basic framework; original construction in reference [10] is not independently proved here. |
| Rational-series height theorem | Reu96 Theorem 3.1, printed pp. 98-105; [U003-U003](Yin_U003.md#reu96-u003) | Supplies a minimal series representation of the required height; its audit is owned by those units. |
| Specialization/translation | Reu96 printed p. 105, citing [8], P. M. Cohn, *Skew Field Constructions* (1977); also restated in CR94 printed p. 525 with book locator Lemma 6.3.1 | Book not opened; retained as cited, with the simultaneous-denominator and infinitude hypotheses explicitly exposed. |
| Comparison embedding | CR94, Theorem 3.2, printed p. 525 / PDF p. 9; [CR94-U001](../CR94/Yin_U001.md#cr94-u001) | Exact primary statement and matching hypotheses checked and accepted; original proof not independently audited. |
| Series-to-free-field minimality | Reu96 printed p. 106; CR94, Proposition 2.10 and Corollary 4.2, printed pp. 522 and 527 / PDF pp. 6 and 11; [CR94-U001](../CR94/Yin_U001.md#cr94-u001) | Primary statements and the comparison-embedding application checked and accepted; original theorem proofs remain unreviewed. |
| Canonical elimination and height bookkeeping | Reu96 Lemmas 4.1-4.2, printed pp. 106-107 | Complete local argument reconstructed above; no unresolved local algebraic gap found. |

The source's statements and local Section 4 proof have been inspected within this scope, retaining the identified external infrastructure.
This does not constitute primary verification of every cited theorem or an independent reconstruction of free-field theory.
No new project theorem, computer experiment, or formal verification is asserted.

The only concrete printed correction found in this unit is the diagonal-block label in Lemma 4.1(ii).
The clarified weak inequalities, simultaneous denominator condition, ordered inverse formula, and size induction are safeguards for correct reuse; they do not change the source theorem.
No author-confirmed erratum search or comparison with another edition was performed by this unit's reviewer.

On 2026-09-08, the comparison and minimality interfaces from reference [10] were upgraded from secondary-only reporting to the primary statement and applicability checks in CR94-U001.
This does not change their original-proof inspection status or remove the separately retained Cohn book dependency.

Independent review, 2026-09-08: the height-machinery reviewing agent checked this reconstruction against rendered Reu96 pp. 105-107 and the CR94-U001 interface record.
The review covered simultaneous denominator translation, multiplication order in the inverse-to-star conversion, minimality transfer, canonical pivots, block restrictions, size induction, and the independent star-height converse.
No unresolved local implication was found; the separate book dependency remains.

## Exact passage and inspection limits


Passages: Theorem 2.2 and conditions (2.1)-(2.2), printed p. 97 / PDF p. 5; Section 4 and Lemmas 4.1-4.2, printed pp. 105-107 / PDF pp. 13-15; series conventions, printed p. 98 / PDF p. 6.

Inspection: 2026-09-08: translation, ordered elimination, block restrictions and induction reconstructed and independently reviewed. CR94 comparison/minimality statements and applicability were checked, but their original proofs were not audited. The separate Cohn book specialization/translation input was not opened and remains secondhand, with simultaneous denominators and infinitude hypotheses explicit. No formal verification or claim that all external infrastructure was proved.
