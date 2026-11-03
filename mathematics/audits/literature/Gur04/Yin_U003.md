---
author: Yin
---

<a id="gur04-u003"></a>
# Gur04-U003 - Exact scaling, attainment, and indecomposability

## Source and inspection

[Source and edition notes](readme.md).

Source edition: This audit reads the user-supplied published article by Leonid Gurvits, *Classical complexity and quantum entanglement*, Journal of Computer and System Sciences 69 (2004), 448-484, DOI [10.1016/j.jcss.2004.06.003](https://doi.org/10.1016/j.jcss.2004.06.003).

Passages: Locator: Theorem 4.7 and proof, printed pp. 464-465 / PDF pp. 17-18.

Inspection: Record: 2026-09-12, source-audit agent, self-review; audited within the reconstructed scope, with the source normalizer corrected below.


The sole bibliography is the Gur04 intake.

Edition: published JCSS article, 37 PDF pages; printed page equals PDF page plus 447.
Current artifact identity; the original review date and scope below are retained.

The original shared source record, dated checking arrangement and setting are retained once in [Gur04-U002](Yin_U002.md#gur04-u002).
References below to the shared account retain that scope.

- Locator: Theorem 4.7 and proof, printed pp. 464-465 / PDF pp. 17-18.
- Record: 2026-09-12, source-audit agent, self-review; audited within the reconstructed scope, with the source normalizer corrected below.
- Kind: exact-scaling criterion and uniqueness mechanism.

### Exact statement

An invertible scaling of \(T\) is doubly stochastic if and only if \(\operatorname{Cap}(T)>0\) and its defining infimum is attained at some \(C>0\), \(\det C=1\).
In that case

\[
Z(X)=T(C)^{-1/2}T(C^{1/2}XC^{1/2})T(C)^{-1/2}
\]

is doubly stochastic.
For \(N\geq2\), \(T\) is indecomposable if and only if there is exactly one determinant-one positive minimizer.
For \(N=1\), both indecomposability and uniqueness are vacuous/singleton properties; a zero map still has no doubly stochastic scaling, so keep the positive-capacity condition for that conclusion.

### Checked proof of the attainment criterion

At a positive minimizer, differentiate \(\log\det T(X)\) under \(\log\det X=0\) to obtain

\[
T^*(T(C)^{-1})=\alpha C^{-1}.
\]

Pairing with \(C\) gives \(N=\alpha N\).
Consequently \(Z(I)=I\) and \(Z^*(I)=I\).
No converse statement that the adjoint is unital for arbitrary \(C\) is valid.

If \(Z=S_{C_1,C_2}(T)\) is doubly stochastic, then \(\det Z(X)\geq\det X\) for \(X>0\).
To check this last fact directly, diagonalize input and output; the numbers \(v_j^*Z(u_iu_i^*)v_j\) form a doubly stochastic scalar matrix.
Concavity of log applied row by row proves the determinant inequality.
Equality holds at \(I\).
The scaling identity in U002 now gives an attained positive capacity for \(T\), with minimizer

\[
C=|\det C_2|^{-2/N}C_2^*C_2.
\]

The exponent on p. 464 is printed with the opposite sign.
The same paragraph also prints a matrix \(T(C)\) equal to a scalar infimum and a malformed determinant equality.
The determinant-one normalizer and scalar objective above are the corrected forms; the theorem statement itself has the correct \(T(C)^{-1/2},C^{1/2}\) scaling.

### Checked existence and uniqueness mechanism

Here \(N\geq2\).
For an indecomposable \(T\), each tuple \(B_i=T(u_iu_i^*)\) satisfies strict proper-subset rank inequalities.
Replacing \(B_j\) by a second copy of \(B_i\), for \(i\ne j\), leaves a tuple satisfying the non-strict selection inequalities of U002: a repeated index reduces the number of distinct original indices by at most one, which is absorbed by strictness.
Thus all mixed discriminants \(D_U^{ij}\) of the replaced tuples are positive.
Their finite minimum over \(i\ne j\) and the compact unitary group is a constant \(K>0\).

For \(X=U\operatorname{diag}(\lambda_i)U^*\), \(\prod\lambda_i=1\), the determinant polynomial contains the nonnegative monomial

\[
\frac12 D_U^{ij}\lambda_i^2\prod_{\ell\ne i,j}\lambda_\ell
=\frac12 D_U^{ij}\frac{\lambda_i}{\lambda_j}.
\]

Hence \(\det T(X)\leq d\) implies \(\lambda_{\max}/\lambda_{\min}\leq2d/K\).
Combined with determinant one, this confines the sublevel set to a compact set of positive definite matrices; a minimizer exists.
This reconstructs the estimate used from [22] in the source, including the factor two, from the coefficient argument already checked in U002.

Normalize at a minimizer to a doubly stochastic indecomposable map \(Z\).
In the log-concavity determinant proof, equality for a non-scalar \(X\) requires every output eigenvector row to be supported only among input eigenvalues of one value.
For any one proper nonempty eigenvalue group with input projection \(P\), the corresponding output projection \(Q\) then satisfies \(Z(P)=Q\); row and column sums give equal ranks.
This contradicts indecomposability.
Thus the determinant-one minimizer for \(Z\) is uniquely \(I\), and the invertible congruence transfers uniqueness to \(T\).

Conversely, a uniquely attained infimum for \(N\geq2\) must be positive.
If \(T(C)\) were singular for any \(C>0\), order comparison \(X\leq aC\) for every \(X>0\) forces all \(T(X)\) into the same proper support, so all their determinants vanish; uniqueness would fail.
Normalize the positive minimizer to \(Z\).
If \(Z\) is not indecomposable, rank non-decrease gives a proper projection \(P\) with rank \(k\) and support \(Q\) of \(Z(P)\) also rank \(k\).
Since \(0\leq Z(P)\leq I\) and its trace is \(k\), \(Z(P)=Q\).
Then every

\[
X_t=e^{(N-k)t}P+e^{-kt}(I-P)
\]

has determinant one and \(\det Z(X_t)=1\), contradicting uniqueness.
Indecomposability is invariant under invertible scaling.

### Limits, dependencies, and verification

The derivative, corrected normalizer, sublevel estimate and equality/converse arguments above were self-reviewed; the exact pages 464-465 were rendered and visually inspected.
This checks the stated source theorem using elementary supplements to its cited earlier proof shortcuts.
No independent reviewer or proof assistant is claimed here.
The earlier [22] proofs were not inspected.
Exact scaling is stronger than approximate scaling: positive capacity alone does not assert attainment.
Tensor-product capacity multiplicativity and the further inequalities asserted in Remark 4.8 are outside this proof review.
