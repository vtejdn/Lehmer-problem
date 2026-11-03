---
author: Yin
---

<a id="msy23-u001"></a>
# MSY23-U001: Introduction and Inner-Rank Algebra

- Source: [MSY23, supplied as MSY23.pdf](../../../literature/pdf/MSY23.pdf), published pp. 1-12: front matter, Section 1, and all of Section 2.
Section 3 begins at the bottom of p. 12 and belongs to [U002](Yin_U002.md#msy23-u002).
- Record: 2026-09-08, the original unit authoring agent, for [MSY23 free-field and Atiyah source audit](readme.md#msy23-free-field-and-atiyah-source-audit).
The [source index](readme.md) own artifact/version metadata.
- Reading and review: every assigned page read; source statements, local proofs, and the precise external algebra interfaces checked.
Theorem 2.10's cited 2006-book locator requires the repair below.
Its mathematical conclusion remains available.
- Main theorem proofs occur later in the paper.
Their introductory statements are mapped here, not treated as proved by the introduction.

## Exact Introductory Interfaces

Theorem 1.1, printed p. 4, concerns a tuple of bounded, not necessarily selfadjoint elements of a finite tracial von Neumann algebra.
Its five equivalent conditions are: unique injective evaluation of the free field with image equal to the affiliated division closure; affiliated invertibility of all full linear square polynomial matrices; affiliated invertibility of all full square polynomial matrices; equality of analytic rank with polynomial inner rank; and maximal Delta.
The matrix trace is the unnormalized Tr tensor tau.
Invertibility is in matrices over the affiliated algebra, and this theorem does not state bounded invertibility in matrices over M.

Theorem 1.2, printed pp. 6-7, has six conditions in the published version, including the separate condition for linear polynomial matrices that are full over the evaluated affiliated rational closure.
It characterizes a division-ring closure and the strong Atiyah property, without asserting that this division ring must be the free field.
The rank in its last condition is inner rank of the evaluated matrix over the evaluated rational closure, not formal free-algebra inner rank.
The zero matrix requires the integer-rank convention to include zero.
Later units own the proof of these equivalences.

The contextual statements on random matrices, free entropy dimension, and later developments are motivational citations, not inputs to Section 2's deductions.
In particular, the historical claim of what was then unknown is not silently updated into a present-day literature assertion.

### Introductory Scope Corrections

Two informal sentences should not be imported as mathematical conclusions:

1. Printed p. 3 describes taking the strong closure of C<X> as producing W*(X).
For nonselfadjoint generators this requires the adjoint-generated algebra.
For one Haar unitary U, every strong limit of polynomials in U sends Omega into the nonnegative Fourier subspace; U*Omega is outside that subspace.
Thus the holomorphic polynomial strong closure need not be W*(U).
The precise theorem is formulated inside a given tracial von Neumann algebra and does not need the erroneous density assertion.
2. Printed p. 5 informally includes nonconstant selfadjoint matrices in an atomlessness conclusion.
A nonconstant scalar rational function and a nonconstant matrix are different cases.
For a standard semicircular S, diag(S,1) is nonconstant and selfadjoint, but its normalized matrix distribution has an atom of mass 1/2 at 1.
The later central-eigenvalue/rank formulas, rather than this informal blanket statement, govern matrices.
Likewise an assertion that rational functions are invertible must exclude the zero rational function.

Both sentences were checked in local renders.
These are scope corrections to introductory prose, not counterexamples to the precisely stated main equivalences.

## Definitions and Elementary Matrix Arguments

Definitions 2.1-2.2, 2.5, 2.8-2.9, and 2.12 were checked with their intended ambient algebra:

- Inner rank of a nonzero M-by-N matrix is the smallest intermediate dimension in a factorization; the zero matrix has rank zero.
Full means rank min(M,N).
Empty blocks later in the argument are interpreted by their displayed dimensions; no positive-rank conclusion is inferred for an empty block.
- Stable finiteness means square matrices over the ring have no proper one-sided inverses.
It is required in Proposition 2.3 but not in the ordinary Schur-complement inverse identity of Lemma 2.4.
- A linear matrix may have a constant coefficient.
A hollow N-by-N matrix has a zero K-by-L block with K+L>N.
- Central eigenvalues are scalars lambda for which A-lambda I is not full over the stated algebra.
They are not by definition the usual bounded operator spectrum.

### Proposition 2.3 and Lemma 2.4

For the block matrix A=[[B,C],[D,E]] with invertible M-by-M B, boundedness plays no role in this purely algebraic section.
Multiplication by invertible block triangular matrices reduces A to diag(B,E-DB^{-1}C).
This proves Lemma 2.4 over any unital algebra.

For Proposition 2.3, stable finiteness ensures every invertible M-by-M matrix has inner rank M: a factorization through r<M would give square matrices PQ=I_M but QP unequal to I_M after zero padding.
Hence rho(A)>=M.
If rho(A)=M, factor the reduced matrix diag(I_M,S) through M.
The top factors P_1 Q_1=I_M have Q_1 P_1=I_M by stable finiteness; the zero off-diagonal blocks then force the remaining factors to vanish and S=0.
Conversely S=0 gives a factorization through M.
This proves the exact equality criterion and retains its hypothesis.

### User Follow-Up: The Exact Rank Form of Schur Elimination

On 2026-09-09 the user specifically pointed back to Proposition 2.3.
Its operative conclusion, for B of size k, is

\[
\rho_{\mathcal A}\!\begin{pmatrix}B&C\\D&E\end{pmatrix}=k
\quad\Longleftrightarrow\quad E=DB^{-1}C,
\qquad B\in GL_k(\mathcal A),\quad\mathcal A\text{ stably finite}.
\]

It is an inner-rank criterion, not merely the invertibility criterion of Lemma 2.4.
One should not replace it by an unproved general additive formula for inner rank over arbitrary stably finite rings.
The complete proof above uses a factorization through k and stable finiteness to force the residual Schur block to vanish.

In Theorem 4.4, simultaneous row/column permutation puts the bordered matrix in the form \(\left(\begin{smallmatrix}A&v\\u&0\end{smallmatrix}\right)\).
Over the free field its inner rank is N because its Schur complement is zero.
Free-field preservation of polynomial inner rank gives a polynomial factorization through N; evaluation gives inner rank at most N in the chosen ambient algebra.
The existing invertibility of A(X) gives rank at least N, so Proposition 2.3 forces the evaluated Schur complement to be zero.
This direct argument avoids the source's contradiction formulation and agrees with the explicit block calculation in U003.

The choice of ambient algebra remains part of the premise: the same statement works with \(\mathcal A=M\) when \(A(X)\in GL_N(M)\), or with \(\mathcal A=U(M)\) when only affiliated invertibility is known.
The proposition does not select a new invertible pivot.
For bounded descent, an application yielding a bounded formula therefore needs either an already bounded-invertible polynomial block or a separate argument constructing one.

### Theorem 2.6 and Proposition 2.7

Theorem 2.6 requires closure of square full matrices under products and diagonal sums; it does not apply to an arbitrary unital algebra without those hypotheses.
Its statement and Cohn's short proof were checked in the primary book, Theorem 5.4.9.
In a rectangular full-row matrix, either deleting the first column preserves row fullness, or factor the remaining columns through one fewer row to write the original matrix as D(1 direct-sum E), with D square full and E full-row.
Induction and the two closure hypotheses produce the required full square submatrix.
Applying this to both factors of a rank factorization gives a square full submatrix of the original matrix of size its inner rank.
Larger ones are excluded by monotonicity of inner rank under selecting submatrices.

The free complex algebra meets those closure hypotheses by the accepted Sylvester-domain interface below.
For Proposition 2.7 with N>=2, if A=(B,b) is full and rho(B)<N-1, adjoining b would yield rho(A)<=rho(B)+1<N.
Thus B is full, and Theorem 2.6 selects the N-1 rows.
The local [CR94](../../../literature/pdf/CR94.pdf), printed p. 527, Lemma 4, was also read directly: its corresponding statement is for an invertible matrix over a field.
The algebraic free-field embedding provides the usual alternative interpretation, but no analytic evaluation theorem is needed here.

### Hollow Matrices

For a zero K-by-L block, the source's displayed product has intermediate size 2N-K-L.
Its block multiplication was checked directly.
Hence rho(A)<=2N-K-L<N when K+L>N.
Scalar invertible row and column operations preserve inner rank.
This verifies the easy direction of the linear hollow criterion and the precise size count used later.

## Theorem 2.10: Citation Repair and the Needed Block Rank

The theorem asserts that a linear N-by-N A of inner rank r can be put, using scalar invertible U,V, into

\[
UAV=\begin{pmatrix}B&0\\ C_1&C_2\end{pmatrix},
\qquad B\in M_{N-K,r-K}(\mathbb C\langle x\rangle),
\quad 0\le K\le r,
\quad \rho(B)=r-K.
\]

The resulting zero block has dimensions (N-K)-by-(N-r+K), so a nonfull linear matrix becomes hollow.
The rank assertion about B is essential in the proof of Theorem 3.1.

The published source cites Cohn's 1995 Corollary 6.3.6 or 2006 Theorem 5.8.8.
The latter locator is not the asserted theorem: in the inspected 2006 primary book it concerns reducibility of a full monic matrix.
A usable input appears in the proof of the immediately preceding Lemma 5.8.7: after changing the internal basis of a rank factorization A=PQ, the degree alpha_j of column j of P and degree beta_j of row j of Q satisfy alpha_j+beta_j<=deg A.
For linear A this is at most one.
The following argument reconstructs the desired conclusion from that input.

Partition the r matched columns/rows into K columns of P of degree zero and the remaining r-K columns.
Every corresponding row of Q in the second group has degree zero.
The constant columns of P are scalar-linearly independent, since otherwise P and then A would factor through fewer than r coordinates.
Likewise the constant rows of Q in the second group are scalar-linearly independent.
Choose U to put the K constant columns of P in the last K coordinates, and choose V to put the other r-K constant rows of Q in the first r-K column positions.
Their product then has the displayed zero block.
Finally any factorization of B through s coordinates extends to a factorization of the whole displayed matrix through at most s+K coordinates.
Thus r<=rho(B)+K, while the number of columns gives rho(B)<=r-K; equality follows.
This also treats K=r by an empty upper-left block.
The rank-zero matrix is handled separately by taking the whole matrix zero.

This repair supplies the exact block structure and extra rank assertion consumed by Section 3.
It does not merely replace the missing citation with a weaker statement that a nonfull pencil has some zero block.

### Proposition 2.11

The homogeneous hypothesis is essential.
For B>=0 with support V, the positive operator sum_i A_i B A_i* has range equal to sum_i A_i V.
Thus the quantum-map rank decrease is precisely the existence of V with dim(sum_i A_i V)<dim V.
Such a shrunk subspace gives, by scalar changes of bases, a hollow block; conversely the hollow form from Theorem 2.10 gives such a subspace.
This reconstructs the qualitative criterion from the preceding linear-matrix theorem.
No algorithmic complexity claim from the cited identity-testing literature is needed.
If a constant coefficient is present, it must also enter the shrunk-space condition; it cannot simply be omitted from the sum.

### Proposition 2.13

If A-lambda I is not full, Theorem 2.10 supplies a scalar hollow form.
Because the free monomials 1,x_1,...,x_n are independent, every coefficient vanishes on the same zero block.
Both the constant matrix U(A_0-lambda I)V and the homogeneous pencil sum U A_i V x_i are hollow.
Consequently the constant matrix is singular, proving lambda belongs to sigma(A_0); the homogeneous pencil is nonfull, so a full homogeneous part rules out every central eigenvalue.
The same block and the constant term are needed in both conclusions.
This proof does not assert absence of ordinary bounded spectral values.

## External Algebra Inputs and Evidence

The primary [Cohn06a book](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/cohnfr.pdf) was read online at Corollary 2.5.2 (p. 135), Proposition 5.4.6 and Theorem 5.4.9 (pp. 285-287), Theorem 5.5.4 (p. 292), and Lemma 5.8.7 / Theorem 5.8.8 (pp. 316-317).
The free complex algebra is a fir and a Sylvester domain.
Those structural interfaces and the matched degree bound are accepted; their complete weak-algorithm foundations were not recursively audited.
The exact Schur/rank and block consequences are reconstructed above.
`Coh06` is the 2006 book; the existing `Coh06b` key denotes a different historical survey.
No full-book audit or local book acquisition is claimed.

All MSY23 pages in this unit were text-read.
Published pp. 3 and 5 were also visually checked for the two prose corrections.
The cited local CR94 passage was extracted directly; its field hypothesis was retained.
The book check used the parsed primary PDF; no successful rendered-page inspection of that online book is claimed.
No numerical experiment or proof assistant was used.

## Result

Section 2's local deductions and their use in the next unit are valid with the explicit Cohn interface and citation repair above.
Theorem 1.1's full proof remains the joint responsibility of U002 and the affiliated-realization unit; no conclusion about bounded scalar division closure follows from this unit.

## Independent Review

On 2026-09-08, a separate reviewing agent independently read this unit, compared the block theorem with MSY23 pp. 10-11, and reopened the primary Coh06 PDF at Lemma 5.8.7 and Theorem 5.8.8, printed pp. 316-317.
The matched degree inequality occurs in Lemma 5.8.7's proof; the cited Theorem 5.8.8 has the different full-monic hypothesis identified above.
After partitioning the degree-zero columns, the two scalar basis changes really do give a zero block of size `(N-K)` by `(N-r+K)`: the constant columns vanish in the top rows, and the matched constant rows vanish in the right columns.
Extending a factorization of B by the K bottom rows gives `rho(A)<=rho(B)+K`, which proves the extra rank assertion and also covers `K=r`.
The independent check also verified the stable-finite Schur argument, the positive-map range/shrunk-space equivalence, and the separate constant and homogeneous coefficient consequences in Proposition 2.13.
No further defect was found.
This review accepts the explicitly identified weak-algorithm foundation; it does not recursively reprove it or claim a rendered inspection of the external book.

On 2026-09-09, the original unit authoring agent independently reviewed only the later section "User Follow-Up: The Exact Rank Form of Schur Elimination," authored by the coordinating agent.
The displayed equivalence retains both stable finiteness and the existing inverse of the pivot.
In its Theorem 4.4 application, the permuted border has Schur complement \(-uA^{-1}v\); zero formal Schur complement gives inner rank \(N\) over the free field, polynomial inner-rank preservation supplies a factorization through \(N\), and evaluation plus the invertible pivot gives the matching upper and lower bounds.
Proposition 2.3 then forces the evaluated Schur complement to vanish.
The argument uses no unproved general additivity formula for inner rank, and its stated bounded-pivot limitation is accurate.
This paragraph reviews the new follow-up addition only; it is not an independent review of the remainder of this unit, which this reviewer originally authored.

## Source and inspection

Source edition: MSY23 / MSY23, the user-supplied 50-page published article in Journal of Functional Analysis 285 (2023), article 110016, DOI 10.1016/j.jfa.2023.110016. Printed pages equal PDF pages. The separate 37-page arXiv v2 was not compared in full; other works retain their own versions and inspection limits in the body.

Passages: Published pp. 1-12: front matter, Section 1 and Section 2; Theorem 2.10 on pp. 10-11. The beginning of Section 3 on p. 12 belongs to U002.

Inspection: 2026-09-08: assigned pages and local arguments checked, with independent review of the reconstructed algebra and the repaired Cohn locator. Selected primary Cohn statements and the matched degree bound were inspected; weak-algorithm foundations were not recursively audited, and rendered inspection of the external Cohn book was not claimed. The 2026-09-09 independent review covers only the coordinating agent's added Schur section, not the reviewer's own original unit. No bounded scalar descent, numerical test or formal verification.
