---
author: Yin
---

# BR10-U002: Series definitions, proper star, residuals and formal Hankel rank

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Retained 2010-04-09 line-numbered manuscript, 248 PDF pages, registered as BR10.

Passages: Chapter 1 pp. 4-7, 10-11 / PDF 16-19, 22-23; Chapter 2 pp. 30-31 / PDF 42-43.

Inspection: 2026-09-10 source text and complete rendered definition pages read; Chapter 2 Theorem 1.6 identified, not a new proof audit.


<a id="br10-u002"></a>
## Selected input and original reading

This responsible source home was prepared at 2026-10-21T01:01 from the actual retained original source-reading account.
The original reading dates, exact source version, inspection depth and limitations remain those recorded below.
This maintenance did not reopen the original source, acquire bytes, perform a new source-proof review.

## Retained selected source content

<a id="definition-recheck"></a>

Date: 2026-09-10.
Reviewer: the unbounded-operator agent, primary-definition reading and self-review.
This selected definition supplement complements [BR10-U001](Yin_U001.md#br10-u001).
It adds exact definition passages needed for the current formal-series/Hankel terminology.
It does not extend the earlier selected theorem-proof audit to the whole book.

Source: [BR10](../../../literature/pdf/BR10.pdf), the retained 2010-04-09 line-numbered manuscript, 248 PDF pages.
All locators below refer to this manuscript: PDF page = printed page + 12.

## Actual inspection

The source text and full rendered pages were inspected at Chapter 1, printed pp. 4–7 and 10–11 / PDF pp. 16–19 and 22–23, and Chapter 2, printed pp. 30–31 / PDF pp. 42–43.
The context and statements surrounding those definitions were read.
In particular, Chapter 2 Theorem 1.6 is visible and was read for its role in identifying the conventions; this is not a new complete proof/dependency audit of Chapter 2.
The existing Chapter 1 equivalence proof review remains [BR10-U001](Yin_U001.md#proof-mechanism-checked).

<a id="formal-series"></a>
## Formal series and their coefficient topology

**Source definition, Chapter 1 Section 2, pp. 4–5.**
Fix a finite nonempty alphabet \(A\) and a semiring \(K\).
Its free monoid \(A^*\) consists of finite words, including the empty word \(1\).
A formal series is a function \(S:A^*\to K\), with coefficient \((S,w)\).
Its support is the set of words with nonzero coefficient.
A polynomial has finite support.
Addition is coefficientwise and multiplication is

\[
(ST,w)=\sum_{xy=w}(S,x)(T,y).
\]

The source separately defines left/right scalar multiplication by \(K\); these cannot be conflated for a noncommutative semiring.
The current operator-algebra applications specialize to \(K=\mathbb C\).
The already adopted complex/field formulation is [DR97-U001, Setting and notation](../DR97/Yin_U001.md#setting-and-notation); the present broader source formulation is a citation candidate, not a second complex-series definition.

**Topology convention, Section 3, pp. 5–6.**
The coefficient semiring has the discrete topology and \(K^{A^*}\) the product topology.
Equivalently, for finite \(A\), the source gives \(d(S,T)=\sigma^{\omega(S,T)}\), \(0<\sigma<1\), where \(\omega\) is the first word length at which a coefficient differs and \(\sigma^\infty=0\).
A family is locally finite if each word has nonzero coefficient in only finitely many members.
This is formal coefficient topology, not the affiliated rank metric, the usual complex coefficient topology or operator-norm convergence.
No new topological equivalence proof is required for its current use.

## Proper star and rational series

**Source definitions, Chapter 1 Section 4, pp. 6–7.**
A series is proper when \((S,1)=0\).
For such \(S\), its star is the locally finite formal sum \(S^*=\sum_{n\ge0}S^n\); the superscript here is Kleene star, not adjoint.
Rational operations are addition, multiplication, left/right scalar multiplication and star on proper series.
Rational series form the smallest subset containing the polynomials and closed under these operations.

For ring coefficients, the same source passage explicitly identifies this with scalar inverse closure in the formal-series ring; invertibility means that the constant coefficient is invertible in \(K\).
Over \(\mathbb C\), it means a nonzero constant coefficient.
Thus the operator-algebra papers' formal rationality is an instance of the common scalar division-closure definition.
It is not the general matrix rational-closure construction.
For semiring coefficients, retain proper star as the defining operation rather than using nonexistent subtraction/inverses.

The current complex rational-series home remains [Miy22-U002, Formal Series and Exact Interfaces](../Miy22/Yin_U002.md#formal-series-and-exact-interfaces).
This supplement records the source's semiring formulation and notation, without introducing another ambient-specific Div/Rat registration.

<a id="representations-and-residuals"></a>
## Recognizable representations and residuals

**Source definitions, Chapter 1 Section 5, pp. 10–11.**
A series is recognizable if

\[
(S,w)=\lambda\mu(w)\gamma,\qquad
\mu:A^*\longrightarrow K^{n\times n}
\]

for a monoid morphism \(\mu\), a row \(\lambda\in K^{1\times n}\), and a column \(\gamma\in K^{n\times1}\).
The triple is a linear representation, of dimension \(n\).
The source explicitly admits dimension zero for the zero series.
Over complex coefficients all products here are algebraic; no conjugation is present.

The prefix-removal residual is \(x^{-1}S=\sum_w(S,xw)w\).
A subset is stable when it contains \(x^{-1}S\) for every member \(S\) and every word \(x\).
Chapter 2 p. 30 uses the equivalent notation \(S\circ x=x^{-1}S\), extended linearly in \(x\); \((S\circ P)\circ Q=S\circ(PQ)\).
This is consistent with the prefix/right-module orientation in DR97.
The project also uses suffix residuals, with coefficients \((S,wx)\), as explicitly normalized in [Miy22-U002](../Miy22/Yin_U002.md#formal-series-and-exact-interfaces).

The existence of a finite stable module is an equivalent criterion supplied by the already reviewed Proposition 5.1; it is not the definition of a linear representation.
Over a field the minimal residual span is finite dimensional when such a module exists.
The broader semiring statement should not be replaced by arbitrary field-dimensional language.

<a id="formal-hankel-rank"></a>
## Formal Hankel matrix, series rank and minimal representation

**Source definitions, Chapter 2 Section 1, pp. 30–31.**
Here \(K\) is a commutative field.
The rank of \(S\) is

\[
\dim_K\bigl(S\circ K\langle A\rangle\bigr),
\]

and its Hankel matrix is the formal matrix indexed by \(A^*\times A^*\),

\[
H_S(x,y)=(S,xy).
\]

The matrix rank in this setting is the supremum of the sizes of nonzero finite minors; finite rank is equivalently finite row/column dimension.
A minimal linear representation has the smallest dimension among representations of that series.
These are algebraic definitions: no map on \(\ell^2(A^*)\), summability or boundedness is included.

The equality between series rank, matrix rank and minimal representation dimension is the known Theorem 1.6 on p. 31.
This sidecar identifies that source statement for reuse; it does not register or reprove that theorem.
The special one-letter **bounded Hankel operator** is a separate analytic convention, [Miy22-U009](../Miy22/Yin_U009.md#exact-statement-and-conventions), with its Hilbert-space hypotheses retained.

## Consumers, citation purpose and limits

The existing direct BR10 forward uses are Yin_S_F0004 and the Kronecker strategy discussion, through BR10-U001.
Yin_C_F0015 has its own exact residual/Hankel definitions and directly cites Miy22-U002; the newly located Chapter 2 definition is an exposition/notation reference, not a retrospectively inserted proof dependency.
Yin_C_F0017 similarly cites Miy22-U002 for the recognized/formal-rational interface.

Recommended citation purposes: standard, notation or exposition.
The manuscript's attribution of earlier results was read but no priority investigation was performed; no origin label is warranted.
No general ring/semiring equivalence, Hilbert boundedness theorem, all-exercises review or whole-book audit is asserted by this definition supplement.
The original BR10-U001 and source PDF were preserved.
