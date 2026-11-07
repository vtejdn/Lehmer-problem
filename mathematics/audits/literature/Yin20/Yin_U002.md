---
author: Yin
---

<a id="yin20-u002"></a>
# Yin20-U002: Complete Chapter III — Inner Rank

- Source: [Yin20, Chapter III](../../../literature/pdf/Yin20.pdf#page%3D47), printed pp. 37–48 / PDF pp. 47–58.
- Record: 2026-09-10, the Chapter III authoring agent, for [Yin20 inner-rank source audit](readme.md#yin20-inner-rank-source-audit).
- Evidence: every assigned page was text-read and visually inspected in a Poppler render, including the blank final page, PDF p. 58.
- Scope: all of III.1–III.4, including definitions, examples, unnumbered deductions, and cited proof interfaces.
  This is a complete chapter-level mathematical reconstruction with the external foundations explicitly retained below, not a claim to have audited the whole Cohn book or later analytic chapters.
- Review state at authorship: ready for independent review.
  The author's verification is not described as independent review.

## Coverage and Disposition

All rings below are nonzero and unital, and homomorphisms preserve the unit when an ambient unital complex algebra is involved.
The zero matrix has inner rank zero.
Empty blocks have their displayed dimensions and rank zero; calling an empty block “full” is shorthand for the rank equality, since Definition III.1.2 literally defines fullness for nonzero matrices.

| Source item | Printed / PDF pages | Checked conclusion and proof disposition |
| --- | --- | --- |
| Chapter introduction | 37 / 47 | Algebraic scope and later-chapter dependencies separated; no analytic rank identity imported here. |
| Definitions III.1.1–III.1.2; polynomial example | 38 / 48 | Inner rank, rank factorization, fullness, and the displayed rank-one factorization checked. |
| Remark III.1.3(i)–(v) | 38–39 / 48–49 | All five factorization arguments reconstructed. |
| Example III.1.4 | 39 / 49 | Invertible but nonfull identity; a nonzero model of the presented algebra supplied below. |
| Definition III.1.5 | 39 / 49 | Stable finiteness retained at every use. |
| Proposition III.1.6 | 39 / 49 | Same-ambient Schur/rank equivalence proved directly, including the lower bound. |
| Lemma III.1.7 | 39–40 / 49–50 | Division-ring Gaussian elimination checked; the thesis includes the required pivot normalization. |
| Proposition III.1.8 | 40 / 50 | Rectangular normal form and its identification with inner rank reconstructed. |
| Definition III.2.1; following rank law | 41 / 51 | Zero-product axiom and its equivalence to the full Sylvester inequality proved directly. |
| Division-ring example | 41–42 / 51–52 | Correct argument retained after two rectangular-block dimension repairs. |
| Full products; Lemma III.2.2 | 42 / 52 | Product closure and diagonal-sum additivity proved directly from the axiom. |
| Theorem III.2.3 | 42 / 52 | Full square submatrix theorem reconstructed by induction, under both stated closure hypotheses. |
| Trivialization discussion and example | 42–43 / 52–53 | Matrix order and example checked; semifir/weak-algorithm foundation explicitly external. |
| Example III.2.4 | 43 / 53 | Free algebra is Sylvester via the accepted structural input; missing “full square” qualification repaired. |
| Remark III.2.5 | 43–44 / 53–54 | Positive cases retained as a precise Cohn input; the three-variable counterexample's omitted fullness proof supplied. |
| Zero-block factorization; Definition III.3.1 | 44 / 54 | Intermediate dimension \(2n-r-s\), hollow criterion, and block multiplication checked. |
| Definition III.3.2 | 45 / 55 | “Linear” includes a constant term; homogeneous part distinguished. |
| Theorem III.3.3 | 45 / 55 | Scalar block form reconstructed from the matched-degree input; rank assertion about \(B\) proved. |
| Definition III.4.1 and surrounding prose | 45–46 / 55–56 | Ambient dependence retained; two overbroad prose assertions corrected below. |
| Proposition III.4.2 | 46 / 56 | At most \(n\) central eigenvalues proved using a rank-preserving division-ring embedding and eigenvector independence. |
| Proposition III.4.3(i)–(ii) | 47 / 57 | Both conclusions reconstructed, retaining the common zero block and constant coefficient. |
| Final assigned page | 48 / 58 | Blank, visually confirmed. |

## III.1: Elementary Rank and the Schur Argument

For a nonzero \(m\times n\) matrix \(A\), \(\rho_R(A)\) is the least \(r>0\) for which \(A=PQ\), with \(P\in M_{m,r}(R)\) and \(Q\in M_{r,n}(R)\).
The p. 38 example multiplies the column \((y,yx)^T\) by the row \((y,xy)\), producing all four displayed entries in their correct noncommutative order.
Since the product is nonzero, its inner rank is exactly one.

Every assertion in Remark III.1.3 follows by composing rank factorizations:

1. Multiplication by invertible matrices cannot increase rank; applying their inverses gives the reverse inequality.
2. Factoring either factor of a product proves \(\rho(AB)\leq\min(\rho(A),\rho(B))\).
3. Row and column selection are matrix multiplications, so submatrix rank cannot increase; adjoining zero rows or columns gives the reverse bound by padding a factorization.
4. Direct sums of factorizations give \(\rho(A\oplus B)\leq\rho(A)+\rho(B)\), while selecting diagonal blocks gives the maximum lower bound.
5. Applying a homomorphism to a factorization proves \(\rho(\phi(A))\leq\rho(A)\), including when the image is zero.

These arguments do not assert rank additivity over an arbitrary algebra.
That stronger statement is proved under the Sylvester hypothesis in III.2.

### Example III.1.4 and Stable Finiteness

The presented algebra with \(AB=I_n\), \(A\in M_{n,m}(R)\), \(B\in M_{m,n}(R)\), and \(m<n\), has \(\rho_R(I_n)\leq m<n\).
To verify that the presentation need not collapse to the zero ring, take a countably infinite-dimensional complex vector space \(V\).
Choose inverse linear isomorphisms \(V^m\leftrightarrow V^n\), and regard their block entries as elements of \(\operatorname{End}_{\mathbb C}(V)\).
They satisfy the defining relation in a nonzero unital complex algebra.
Thus the example really exhibits an invertible nonfull matrix.

If \(R\) is stably finite, \(I_m\) cannot factor through \(r<m\): padding \(P\in M_{m,r}(R)\), \(Q\in M_{r,m}(R)\) with zeros gives square matrices \(P'Q'=I_m\), while \(Q'P'\) has a zero lower-right block and differs from \(I_m\).
Consequently every invertible \(m\times m\) matrix is full over \(R\).

### Proposition III.1.6, with the Ambient Algebra Fixed

Assume \(R\) is stably finite, and let

\[
A=\begin{pmatrix}B&C\\D&E\end{pmatrix},
\qquad B\in GL_m(R),\qquad S=E-DB^{-1}C.
\]

Invertible block triangular row and column operations reduce \(A\) to \(\operatorname{diag}(I_m,S)\).
Selecting the identity block proves \(\rho_R(A)\geq m\).
If \(S=0\), the reduced matrix factors through \(m\), giving equality.
Conversely, a factorization through \(m\) can be split as

\[
\begin{pmatrix}I_m&0\\0&S\end{pmatrix}
=\begin{pmatrix}P_1\\P_2\end{pmatrix}
 \begin{pmatrix}Q_1&Q_2\end{pmatrix}.
\]

Here \(P_1,Q_1\in M_m(R)\), and \(P_1Q_1=I_m\).
Stable finiteness gives \(Q_1P_1=I_m\).
The off-diagonal equalities give \(Q_2=Q_1(P_1Q_2)=0\) and \(P_2=(P_2Q_1)P_1=0\), hence \(S=P_2Q_2=0\).
This proves precisely

\[
\rho_R(A)=m\quad\Longleftrightarrow\quad E=DB^{-1}C.
\]

The premise \(B\in GL_m(R)\) is essential to the statement and proof.
An application with \(R=U(M)\) uses an affiliated inverse; an application with \(R=M\) needs a bounded inverse already in \(M_m(M)\).
The result neither changes the ambient ring nor supplies a different invertible pivot.
This agrees with [MSY23-U001](../MSY23/Yin_U001.md#msy23-u001) and the bounded-linearization recheck.

### Lemma III.1.7 and Proposition III.1.8

Over a division ring, move a nonzero entry to the top-left corner by row and column permutations.
For \(A=\left(\begin{smallmatrix}a&b\\c&D\end{smallmatrix}\right)\), the thesis correctly uses

\[
U=\begin{pmatrix}1&0\\-ca^{-1}&I\end{pmatrix},
\qquad V=\begin{pmatrix}a^{-1}&-a^{-1}b\\0&I\end{pmatrix},
\qquad UAV=\begin{pmatrix}1&0\\0&D-ca^{-1}b\end{pmatrix}.
\]

Both multiplying matrices are invertible.
If a full \((n+1)\times(n+1)\) matrix had a nonfull lower-right \(n\times n\) block here, the direct-sum upper bound would give rank at most \(n\), a contradiction.
Induction proves that every full square matrix over a division ring is invertible.
The \(a^{-1}\) entry in \(V\) is present in this thesis; a normalization omission in a different source must not be attributed to this page.

The same elimination applies to rectangular matrices until the residual block is zero, producing \(\operatorname{diag}(I_k,0)\).
A division ring is stably finite because a surjective endomorphism of a finite-dimensional right vector space is injective.
Thus the identity block has inner rank \(k\), and selecting it and factoring through its coordinates show that the rectangular normal form has inner rank exactly \(k\).
This identifies the Gaussian elimination parameter with \(\rho(A)\) and proves Proposition III.1.8, including the zero case.

## III.2: Sylvester Domains and Full Submatrices

### The Defining Axiom and the General Rank Inequality

The defining axiom says that \(AB=0\), for \(A\in M_{m,n}(R)\) and \(B\in M_{n,s}(R)\), implies \(\rho(A)+\rho(B)\leq n\).
For scalars it rules out two nonzero factors with zero product, so \(R\) is a domain.
For the claimed equivalent general inequality, let \(AB=PQ\) be a rank factorization through \(r=\rho(AB)\).
Then

\[
\begin{pmatrix}A&-P\end{pmatrix}
\begin{pmatrix}B\\Q\end{pmatrix}=0.
\]

The axiom and submatrix monotonicity give

\[
\rho(A)+\rho(B)
\leq\rho\begin{pmatrix}A&-P\end{pmatrix}
   +\rho\begin{pmatrix}B\\Q\end{pmatrix}
\leq n+r.
\]

For \(r=0\), this is the original zero-product axiom.
Conversely the general inequality implies the axiom by setting \(AB=0\).
This fills the proof omitted after Definition III.2.1.
For full square \(A,B\in M_n(R)\), it gives \(n\leq\rho(AB)\leq n\), proving product closure.

A division ring satisfies the axiom by the rectangular normal form of III.1.8.
After changing bases, \(A\) has an identity block of size \(r=\rho(A)\), so \(AB=0\) forces the first \(r\) rows of the transformed \(B\) to vanish.
The remaining \(n-r\) rows give \(\rho(B)\leq n-r\).
This is the intended source proof, but its block called \(B_1\) on p. 41 cannot be square for an arbitrary \(B\in M_{n,s}(R)\), and the final row block on p. 42 has \(s\) columns, not \(n\).
Only a horizontal split into \(r\times s\) and \((n-r)\times s\) blocks is needed.

### Lemma III.2.2: Direct-Sum Additivity

Factor \(\operatorname{diag}(A,B)=PQ\) through \(k=\rho(A\oplus B)\), splitting \(P=(P_1;P_2)\), \(Q=(Q_1,Q_2)\) according to the diagonal blocks.
Then \(P_1Q_2=0\), \(A=P_1Q_1\), and \(B=P_2Q_2\).
The axiom gives

\[
\rho(A)+\rho(B)\leq\rho(P_1)+\rho(Q_2)\leq k.
\]

The opposite inequality is Remark III.1.3(iv), proving equality.
This proves the diagonal-sum closure needed in Theorem III.2.3.

### Theorem III.2.3: Exact Inductive Proof

Assume square full matrices are closed under products and diagonal sums.
First take an \(m\times n\) full-row matrix \(A\), with \(m\leq n\).
We prove existence of a full \(m\times m\) column submatrix by induction, reducing either the number of columns or both dimensions.
The case \(n=m\) is immediate; the case \(m=1\) follows by selecting a nonzero entry.
Write \(A=(a,A')\).
If \(A'\) remains full-row, apply induction to it.
Otherwise \(\rho(A')\leq m-1\); adjoining \(a\) raises rank by at most one, so \(\rho(A')=m-1\).
Take \(A'=PQ\) through \(m-1\) coordinates and write

\[
A=\begin{pmatrix}a&P\end{pmatrix}(1\oplus Q).
\]

The square first factor is full, since otherwise \(A\) would not be full-row.
Also \(Q\in M_{m-1,n-1}(R)\) is full-row by the same rank bound.
Induction selects a full \((m-1)\times(m-1)\) column submatrix \(Q_J\).
The corresponding submatrix of \(A\), including its first column, is

\[
\begin{pmatrix}a&P\end{pmatrix}(1\oplus Q_J),
\]

which is full by the two closure hypotheses.
The row version follows by the same argument with rows; equivalently transpose into the opposite ring, where both hypotheses are preserved.
For general rank \(r>0\), factor \(A=PQ\) through \(r\).
Then \(P\) is full-column and \(Q\) is full-row.
Choose \(r\) rows \(I\) with \(P_I\) full square and \(r\) columns \(J\) with \(Q_J\) full square.
The submatrix \(A_{I,J}=P_IQ_J\) is full.
A larger full square submatrix is excluded by rank monotonicity.
For \(A=0\), use the empty \(0\times0\) convention; the literal nonzero definition of fullness cannot require a positive-size full submatrix.

This is the mechanism of Cohn's Theorem 5.4.9, previously primary-source checked in MSY23-U001, with the intermediate factorizations now explicit.

### Free-Algebra Trivialization and Example III.2.4

If every relation \(AB=0\) can be transformed by an invertible \(U\) into

\[
AU=(C,0),\qquad U^{-1}B=\begin{pmatrix}0\\D\end{pmatrix}
\]

with complementary coordinate groups of sizes \(k,n-k\), then \(\rho(A)\leq k\) and \(\rho(B)\leq n-k\).
The p. 42 occurrence of \(\rho(BU^{-1})\) is an order/dimension typo; it must be \(\rho(U^{-1}B)\).
For the example \(A=(x,xy)\), \(B=(yz,-z)^T\), the matrix \(U=\left(\begin{smallmatrix}1&y\\0&-1\end{smallmatrix}\right)\) satisfies \(U^{-1}=U\), \(AU=(x,0)\), and \(U^{-1}B=(0,z)^T\), in the stated noncommutative order.

The source's passage through semifirs and the weak algorithm is an external structural input identified below.
With that input, the free algebra is Sylvester, and the preceding theorem shows that inner rank is the maximum size of a **full square** submatrix.
The last sentence of Example III.2.4 omits this qualification; maximum size of arbitrary submatrices cannot equal inner rank in general.

### Remark III.2.5: The Commutative Counterexample

For positive \(d\), the claim that \(\mathbb C[x_1,\ldots,x_d]\) is Sylvester for \(d=1,2\) is retained as the cited structural input from Cohn, Theorem 5.5.4.
For \(d=1\), diagonal reduction over the Euclidean domain \(\mathbb C[x]\) also identifies inner rank with fraction-field rank.
The two-variable structural proof is not silently represented as reconstructed from the dissertation, which supplies none.

Here is a direct proof of the omitted negative case.
Over \(R=\mathbb C[x,y,z]\), set

\[
K=\begin{pmatrix}0&z&-y\\-z&0&x\\y&-x&0\end{pmatrix},
\qquad v=\begin{pmatrix}x\\y\\z\end{pmatrix}.
\]

Then \(Kv=0\), \(v^TK=0\), and \(\rho_R(v)=1\).
Over the fraction field, \(K\) has rank two: one \(2\times2\) minor is nonzero and \(Kv=0\).
If \(K=PQ\) factored through two coordinates over \(R\), both factors would have fraction-field rank two.
A right inverse of \(Q\) over that field and \(v^TPQ=0\) would imply \(v^TP=0\).
For each column \(p\) of \(P\), the linear part of \(xp_1+yp_2+zp_3=0\) forces its constant coefficients to vanish.
Thus \(P\) has no constant term and the degree-one part of \(K=PQ\) is \(P^{(1)}Q^{(0)}\).
The three columns would lie in the complex span of the two columns of \(P^{(1)}\).
But the three displayed columns of \(K\) are complex-linearly independent: the first row of a constant relation forces the second and third coefficients to vanish, and the second row forces the first to vanish.
This contradiction proves \(\rho_R(K)=3\).

An independently supplied simplification by the evaluation-and-closure agent, received before whole-artifact review, uses also a left inverse of \(P\) to deduce \(Qv=0\).
Its degree-one part forces \(Q^{(0)}=0\), so both \(P\) and \(Q\) have zero constant term and \(PQ\) cannot have a degree-one term at all.
Both arguments prove the same fullness assertion; this preliminary contribution is disclosed for the later reviewer.

Thus \(\rho_R(K)+\rho_R(v)=4>3\), violating the Sylvester axiom.
For \(d>3\), setting the other variables to zero would carry any smaller factorization to one in the three-variable ring, so the same violation persists.
If zero variables are allowed, \(\mathbb C\) is also Sylvester; the source takes \(d>0\).

## III.3: Linear Matrices and the Exact Degree Input

For an \(n\times n\) matrix with a zero \(r\times s\) top-right block, the p. 44 factorization is

\[
\begin{pmatrix}B&0\\C&D\end{pmatrix}
=\begin{pmatrix}B&0\\0&I_{n-r}\end{pmatrix}
 \begin{pmatrix}I_{n-s}&0\\C&D\end{pmatrix}.
\]

The intermediate dimension is \((n-s)+(n-r)=2n-r-s\).
Thus a hollow matrix, for which \(r+s>n\), is nonfull.
Permutations move a zero submatrix to this position without changing dimensions or rank.

For Theorem III.3.3, let \(r=\rho(A)\) and take a minimal factorization \(A=PQ\) through \(r\).
The external input is matched-degree reduction: after an invertible internal change of basis, the degrees \(\alpha_j\) of column \(j\) of \(P\) and \(\beta_j\) of row \(j\) of \(Q\) satisfy \(\alpha_j+\beta_j\leq\deg A\).
For affine-linear \(A\), the bound is at most one.
The usable locator is the proof of Cohn 2006, Lemma 5.8.7, printed p. 316, documented by the primary-source check in MSY23-U001.
The adjacent Theorem 5.8.8, pp. 316–317, concerns a different full-monic reducibility statement.
The thesis acknowledges that the cited proof aims at something different; the exact needed input is the preceding lemma's matched-degree step.
The alternative Cohn 1995 Corollary 6.3.6 remains a cited source, not a freshly audited second proof here.

Reorder coordinates so that \(s\) columns of \(P\) have degree zero and the remaining \(r-s\) corresponding rows of \(Q\) have degree zero.
The constant columns are complex-linearly independent: otherwise a constant change of internal coordinates would make a column of \(P\) zero and shorten the factorization of \(A\), contrary to minimality.
The \(r-s\) constant rows of \(Q\) are independent by the same argument.
Choose \(U\in GL_n(\mathbb C)\) to put the constant columns in the last \(s\) coordinates, and \(V\in GL_n(\mathbb C)\) to put those constant rows in the first \(r-s\) coordinates.
Then

\[
UAV=\begin{pmatrix}B&0\\C&D\end{pmatrix},
\qquad B\in M_{n-s,r-s}(\mathbb C\langle x\rangle).
\]

For the additional rank assertion, factor \(B=P_0Q_0\) through \(t=\rho(B)\).
The whole displayed matrix factors as

\[
\begin{pmatrix}P_0&0\\0&I_s\end{pmatrix}
\begin{pmatrix}Q_0&0\\C&D\end{pmatrix},
\]

so \(r\leq t+s\).
Its number of columns gives \(t\leq r-s\), hence \(t=r-s\).
The zero block has size \((n-s)\times(n-r+s)\); its dimensions sum to \(2n-r>n\) when \(r<n\).
The zero matrix and \(s=r\) cases use the previously stated rank-zero and empty-block conventions.
This proves the exact block-rank statement needed later, not merely existence of some hollow form.

## III.4: Central Eigenvalues and Scope Corrections

Definition III.4.1 is ambient-dependent:

\[
\sigma_R^{\mathrm{full}}(A)
=\{\lambda\in\mathbb C:\rho_R(A-\lambda I_n)<n\}.
\]

It does not define ordinary bounded operator spectrum.
Over a division ring it coincides with failure of invertibility, by III.1.7 and stable finiteness.

Two surrounding assertions need narrower scope.
First, scalar matrices need not retain their usual inner ranks or central eigenvalues in an arbitrary unital complex algebra.
In Example III.1.4, \(I_n\) is nonfull, and every nonzero scalar multiple of \(I_n\) is nonfull by invertible scalar multiplication.
Thus \(\sigma_R^{\mathrm{full}}(I_n)=\mathbb C\), although its usual complex spectrum is \(\{1\}\).
This corrects the unrestricted p. 46 scalar-matrix sentence and any reading of the p. 38 “agrees” sentence as scalar-rank preservation in an arbitrary ambient algebra.
Both assertions are valid over a stably finite complex algebra: reduce the scalar matrix to \(\operatorname{diag}(I_k,0)\) over \(\mathbb C\), then use fullness of \(I_k\).
In particular, they hold for the free algebra used in the numbered propositions.

Second, an arbitrary unital complex algebra need not have center exactly \(\mathbb C\), and the free algebra has center \(\mathbb C[x_1]\) when \(d=1\).
For the free algebra, “center exactly \(\mathbb C\)” requires \(d\geq2\).
The definition and both numbered propositions remain valid with complex scalar parameters for every positive \(d\).

### Proposition III.4.2 without the Later Analytic Argument

Use the exact input of IV.2.5: the free algebra embeds in a division ring \(F\) with all matrix inner ranks preserved.
Restrict to the division ring generated by its image, as in the universal field of fractions, so the complex scalars remain central.
Matrix inner ranks remain preserved under this restriction, since \(\rho_{\text{original overring}}\leq\rho_{\text{generated division subring}}\leq\rho_R\) and the two outer quantities agree.
For each \(\lambda\in\sigma^{\mathrm{full}}(A)\), the matrix \(A-\lambda I_n\) is singular over \(F\) and has a nonzero right kernel vector \(v_\lambda\in F^n\).
Thus \(Av_\lambda=v_\lambda\lambda\).

Eigenvectors for distinct such scalars are right-linearly independent.
Take a minimal nontrivial relation \(\sum_{j=1}^k v_{\lambda_j}c_j=0\), with every \(c_j\ne0\).
For \(k=1\), a nonzero coordinate of \(v_{\lambda_1}\) rules out the relation.
For \(k>1\), applying \(A-\lambda_k I_n\) gives

\[
\sum_{j=1}^{k-1}v_{\lambda_j}(\lambda_j-\lambda_k)c_j=0.
\]

Every coefficient is nonzero in the division ring, contradicting minimality.
There are at most \(n\) independent vectors in \(F^n\), proving the bound.
This uses the rank-preserving embedding input, but neither Cohn 1985 Proposition 8.4.1 and its rational-parameter proof nor the promised analytic argument in VI.2.
It therefore avoids a later analytic dependency cycle.
The companion Chapter IV auditor, the rational-expression agent, independently confirmed the stated IV.2.5 embedding interface before this draft; this is a scoped source-interface contribution, not a review of the whole present artifact.

### Proposition III.4.3

For \(A=A_0+\sum_jA_jx_j\) and a central eigenvalue \(\lambda\), III.3.3 gives scalar invertible \(U,V\) such that \(U(A-\lambda I_n)V\) has a hollow zero block.
The free words \(1,x_1,\ldots,x_d\) are complex-linearly independent, so every coefficient vanishes on that same block.
Both \(U(A_0-\lambda I_n)V\) and \(U(A-A_0)V\) are hollow.
The constant matrix is singular, giving \(\lambda\in\sigma_{\mathbb C}(A_0)\); the homogeneous part is nonfull, so a full homogeneous part rules out all central eigenvalues.
For (i) alone, augmentation \(x_j\mapsto0\) gives the shorter proof \(\rho_{\mathbb C}(A_0-\lambda I_n)\leq\rho(A-\lambda I_n)<n\).
The source's common-block argument correctly proves both conclusions together.
Neither is a statement about absence of ordinary bounded spectral values.

## Accepted External Inputs and Depth

The remaining algebraic foundations are distinguished below from the local proofs.
The dissertation's [Coh06b] is the 2006 book; the repository key for it is Coh06, whereas Coh06b denotes a separate historical survey.

| Input | Exact source locator | Depth accepted in this unit |
| --- | --- | --- |
| Free complex algebra is a fir/semifir, has relation trivialization, and is Sylvester | Cohn, Free Ideal Rings and Localization in General Rings (2006), §2.3; Theorems 2.4.4 and 2.5.1; Corollary 2.5.2 and following paragraph, p. 135 | Structural interface accepted; the complete weak-algorithm foundation is not recursively audited. |
| Positive cases \(\mathbb C[x]\), \(\mathbb C[x,y]\) are Sylvester | Same book, Theorem 5.5.4, p. 292; Yin20 Remark III.2.5, pp. 43–44 | The cited positive classification input is retained; the negative cases are proved directly above. |
| Matched-degree reduction of a free-algebra rank factorization | Same book, proof of Lemma 5.8.7, p. 316; distinguish Theorem 5.8.8, pp. 316–317 | Precise degree inequality accepted; the scalar hollow form and its block-rank assertion are deduced above. |
| Rank-preserving division-ring embedding of the free algebra | Yin20 IV.2.5; [companion IV.1–IV.3 audit](Yin_U003.md#yin20-u003) | Algebraic embedding interface accepted here; no analytic evaluation theorem is used. |

The [primary Cohn book](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/cohnfr.pdf) passages at pp. 135, 285–287, 292, and 316–317 were previously read in the primary parsed PDF for [MSY23-U001](../MSY23/Yin_U001.md#msy23-u001).
This unit reuses that explicitly scoped verification and reconstructs the local consequences anew; it does not claim a new full-book audit or a successful fresh visual check of those online book pages.
The same prior check covers Proposition 5.4.6 and Theorem 5.4.9, whose relevant arguments are fully supplied above.
The alternative references DS78, Cohn 1995, and Cohn 1985 are not promoted to newly audited sources here.
No historical or priority claim in the chapter is needed for these deductions.

## Consequence for the Current Research Question

Chapter III supplies the exact inner-rank Schur criterion, full-submatrix machinery, and scalar hollow forms for the later rational-function arguments.
It supplies no norm, Hilbert-space domain, bounded-inverse realization theorem, or procedure upgrading an affiliated inverse to a bounded matrix inverse.
Proposition III.1.6 applies in the selected ambient algebra and presupposes the invertible pivot there.
The fresh chapter audit therefore leaves the bounded-linearization distinction intact.
It does not by itself close the small-core analytic extension question.
The representation obstruction reported under former Yin_C_F0012 is located at the [fixed original project proof and review homes](../MSY23/Yin_U003.md#original-project-obstruction).
Their source-only access and exact review limits remain in force; Chapter III alone supplies no such obstruction and no local theorem is newly adopted.

The repairs are the arbitrary-ambient scalar-rank/eigenvalue scope, the center qualification, two rectangular dimensions, the order of \(U^{-1}B\), the missing full-square qualification, the empty-block convention, and the exact matched-degree citation locator.
With those repairs and the explicit external inputs, every numbered Chapter III result has its claimed algebraic conclusion.

## Independent Complete-Artifact Review

On 2026-09-10, the evaluation-and-closure agent independently reviewed the complete mathematical artifact.
Every supplied source page in PDF pp. 47–58 / printed pp. 37–48 was text-read and visually inspected, including the blank final page.
The review compared every numbered item and the surrounding examples, deductions, and source qualifications with the written reconstruction.
It also read the existing MSY23-U001 record to verify the exact scope of the Cohn primary-source checks reused here.

The stable-finite identity-rank argument and both directions of Proposition III.1.6 are correct.
In particular, after factoring the reduced matrix through the pivot size, stable finiteness makes both square pivot factors invertible, and the two off-diagonal equations force the remaining block to vanish.
The nonzero infinite-dimensional model really realizes Example III.1.4, so the arbitrary-ambient scalar-rank and central-eigenvalue corrections are necessary.
The Gaussian matrices in III.1.7 have the required normalization, and rectangular elimination identifies its final identity size with inner rank without assuming an unproved additivity formula.

For III.2, the augmented zero-product factorization proves the general Sylvester inequality with the displayed dimensions, including the rank-zero convention.
The cross-block relation in a minimal factorization of a direct sum proves rank additivity from the original Sylvester axiom.
The induction for full square submatrices strictly reduces the stated dimensions, and its final product is full using exactly the two given closure hypotheses.
Transposition into the opposite ring preserves those hypotheses and legitimately supplies the row version.
Both the author's complex-linear-column proof and the separately disclosed simultaneous constant-term proof of the three-variable skew matrix's fullness are valid.
Specialization supplies the asserted extension to more variables.

For III.3, the matched-degree inequality remains an explicit structural input, not an independently rederived theorem in this record.
Given that inequality, minimality ensures the independence of the selected constant columns and rows, and the two scalar basis changes force precisely the displayed zero block.
The extended factorization then proves the additional full-rank assertion about its upper-left block.
The block dimensions, hollow inequality, zero-rank case, and empty-width convention all agree with the source theorem after the stated clarification.

For III.4, passage to the division subring generated by the polynomial image preserves rank by the recorded two-sided rank inequality and makes the scalar parameters central.
The minimal right-linear eigenvector relation therefore shortens after applying the last scalar shift, proving the finite cardinality bound.
The common zero block for the constant and homogeneous coefficients proves both parts of III.4.3; augmentation gives the separate shorter proof of its first part.
These conclusions concern algebraic fullness and do not exclude ordinary bounded spectral values.

The reviewer requested two premise clarifications before acceptance: explicitly declare stable finiteness at the start of III.1.6, and record rank preservation after restricting the embedding overring in III.4.2.
The reviewer also supplied preliminary source-scope observations and the already disclosed optional simplification of the commutative counterexample before the final artifact review.
The reviewer-contributed optional simplification is not independently covered by its contributor's own final artifact conclusion.
The author's original argument remains a distinct checked input.
The record does not establish the exact use of the preliminary observations or whether a complete initial judgment on that original argument preceded them, so the overlapping initial-review relationship is unknown rather than certified by the final independent wording.

Outcome: accepted under the explicitly retained weak-algorithm, positive commutative Sylvester, matched-degree, and rank-preserving embedding inputs.
No unresolved mathematical correction remains within the assigned chapter scope.
The source's exact same-ambient Schur premise is retained, so the stated boundary concerning bounded linearization follows.
This review does not recursively audit the Cohn books, DS78, or the later analytic chapters, and does not claim a fresh visual check of the external Cohn PDF, proof-assistant verification, or external human review.
This section is the independent reviewer's only change to the released artifact.

## Source and inspection

Source edition: Yin20, the supplied 109-page doctoral dissertation with title-page year 2019; its defense date 2020-01-27 and public repository metadata are separate facts. Printed Arabic page = PDF page minus 10. Other source editions retain their separate exact locators.

Passages: All Chapter III, Sections III.1-III.4, printed pp. 37-48 / PDF pp. 47-58, including definitions, examples, deductions and the blank final verso.

Inspection: 2026-09-10: complete chapter reading, rendered-page inspection and local proof reconstruction, followed by the appended independent artifact review. Weak-algorithm, positive commutative Sylvester, matched-degree and rank-preserving embedding inputs remain explicit; stable-finiteness and same-ambient Schur premises are retained. The optional reviewer-contributed simplification has SELF coverage; its exact use and initial-check timing remain unknown at the overlapping scope, without withdrawing the performed source and proof checks. No recursive book audit or formal/human review.
