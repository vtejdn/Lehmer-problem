---
author: Yin
---

# Capacity and Positive Operator Scaling

## Source and inspection

Source edition: This audit reads the user-supplied published article by Leonid Gurvits, *Classical complexity and quantum entanglement*, Journal of Computer and System Sciences 69 (2004), 448-484, DOI [10.1016/j.jcss.2004.06.003](https://doi.org/10.1016/j.jcss.2004.06.003).

Passages: Locators: Definitions 4.2 and 4.4, Lemma 4.5, Theorem 4.6, printed pp. 461-464 / PDF pp. 14-17; Proposition 2.4, pp. 452-453 / PDF pp. 5-6.

Inspection: Record: 2026-09-12, source-audit agent, self-review; audited within the explicitly reconstructed qualitative scope below.


The sole bibliography is the Gur04 intake.

Edition: published JCSS article, 37 PDF pages; printed page equals PDF page plus 447.
Current artifact identity; the original review date and scope below are retained.

This entrance also preserves the original carrier's companion [Gur04-U003](Yin_U003.md#gur04-u003).
Its separate unit body and inspection scope are at that exact home.

The exact source artifact and review date are in the [source index](readme.md#source-version).
Throughout, \(T:M_N(\mathbb C)\to M_N(\mathbb C)\) is positive and complex-linear; \(\operatorname{Tr}\), adjoint, and the squared defect \(\mathrm{DS}\) follow [U001](Yin_U001.md#positive-maps-and-rank).
Complete positivity is not required.

<a id="gur04-u002"></a>
## Gur04-U002 - Capacity, rank non-decrease, and approximate scaling

- Locators: Definitions 4.2 and 4.4, Lemma 4.5, Theorem 4.6, printed pp. 461-464 / PDF pp. 14-17; Proposition 2.4, pp. 452-453 / PDF pp. 5-6.
- Record: 2026-09-12, source-audit agent, self-review; audited within the explicitly reconstructed qualitative scope below.
- Kind: definitions, equivalence, and proof mechanism.

<a id="capacity-definition"></a>
### Exact interface

For invertible \(C_1,C_2\in M_N(\mathbb C)\), define

\[
S_{C_1,C_2}(T)(X)=C_1T(C_2^*XC_2)C_1^*,\qquad
\operatorname{Cap}(T)=\inf_{X>0,\ \det X=1}\det T(X).
\]

Then

\[
\operatorname{Cap}(S_{C_1,C_2}(T))=
|\det C_1|^2|\det C_2|^2\operatorname{Cap}(T),
\quad
0\leq\operatorname{Cap}(T)\leq\det T(I)
\leq\left(\frac{\operatorname{Tr}T(I)}N\right)^N.
\]

The following conditions are equivalent:

1. \(T\) is rank non-decreasing.
2. \(\operatorname{Cap}(T)>0\).
3. For every \(\epsilon>0\), some invertible scaling \(S\) of \(T\) satisfies \(\mathrm{DS}(S)\leq\epsilon^2\).
4. Successive row and column normalizations are defined and their defects tend to zero.

Here row normalization is \(R(T)=S_{T(I)^{-1/2},I}(T)\), and column normalization is \(C(T)=S_{I,T^*(I)^{-1/2}}(T)\).
If a required marginal is singular, the iteration is not defined; this already precludes rank non-decrease.
The statement concerns convergence of the **defects**, not convergence of the scaling matrices or a positive attained infimum.

### Reconstruction of the capacity argument

The source uses its displayed mixed-discriminant comparison (32), attributed to earlier Gurvits-Samorodnitsky work.
Its original proof was not retrieved in this audit.
The following reconstruction checks the qualitative equivalence directly and does not import the stronger constant \(N^N/N!\).

For positive semidefinite matrices \(B_1,\ldots,B_N\), let

\[
D(B_1,\ldots,B_N)=[x_1\cdots x_N]\det\Bigl(\sum_i x_iB_i\Bigr).
\]

This is the **unnormalized** mixed discriminant of (12), so \(D(I,\ldots,I)=N!\).
Factor each \(B_i\) into rank-one positive summands.
Cauchy-Binet expresses every coefficient as a sum of nonnegative squared determinants.
In particular, \(D>0\) precisely when one can choose an independent vector from the range of each \(B_i\).
The latter is equivalent to

\[
\dim\sum_{i\in J}\operatorname{ran}B_i\geq |J|\quad(J\subseteq\{1,\ldots,N\}).
\]

For completeness, the sufficiency has an elementary induction.
If a nonempty proper set \(J\) has equality, select an independent family for \(J\) and apply induction to the remaining subspaces in the quotient by their sum; the rank conditions descend by applying the original inequality to \(J\cup K\).
If no proper set has equality, choose a nonzero vector from the last subspace and quotient by its span.
Every nonempty subcollection of the remaining subspaces originally has dimension at least its cardinality plus one, so the quotient still meets the required inequalities.
The singleton case starts the induction.
This verifies the selection interface used here, without asserting a new project result.

If \(T\) is rank non-decreasing and \(U=(u_1,\ldots,u_N)\) is unitary, set \(B_i=T(u_iu_i^*)\).
The inequalities above hold by applying \(T\) to each coordinate projection.
Thus \(D_U=D(B_1,\ldots,B_N)>0\).
It is continuous in \(U\); compactness of the unitary group gives \(d_0=\min_U D_U>0\).
For \(X=U\operatorname{diag}(\lambda_i)U^*>0\) of determinant one, coefficient nonnegativity gives

\[
\det T(X)\geq D_U\prod_i\lambda_i=D_U\geq d_0.
\]

Conversely, if \(P\) has rank \(k<N\) and \(T(P)\) has rank \(r<k\), take

\[
X_t=t^{N-k}P+t^{-k}(I-P),\quad t\longrightarrow\infty.
\]

Then \(\det X_t=1\) and \(\det T(X_t)=t^{-kN}\det(t^NT(P)+T(I-P))=O(t^{N(r-k)})\to0\), since the polynomial inside has degree at most \(r\) in \(t^N\).
If the deficient projection has \(k=N\), positivity implies \(T(X)\) is supported in \(\operatorname{ran}T(I)\) for all \(X>0\), so every determinant is zero.
This also covers the zero map.

### Reconstruction of the scaling argument

Rank non-decrease passes to the adjoint: if \(T(P)\) is supported in a projection \(Q\) of smaller rank, trace duality gives \(\operatorname{Tr}(P T^*(I-Q))=0\); positivity forces \(T^*(I-Q)\) to be supported in \(I-P\), whose rank is smaller than that of \(I-Q\).
Apply the argument to \(T^*\) for the converse.
Invertible scaling preserves the rank inequalities.
These observations ensure both positive definite marginals throughout normalization.

After the first step, one marginal is \(I\), both marginal traces are \(N\), and capacity is at most one.
Each next normalization multiplies capacity by the inverse determinant of the other marginal, a factor at least one by arithmetic-geometric mean.
Positive initial capacity gives an increasing positive bounded sequence; its successive ratios tend to one.
For positive eigenvalues with sum \(N\), product tending to one forces every eigenvalue to tend to one.
Hence \(\mathrm{DS}(T_n)\to0\).

For the converse, a doubly stochastic positive map cannot decrease the rank of a rank-\(k\) projection: \(0\leq T(P)\leq I\) and \(\operatorname{Tr}T(P)=k\), so its support has rank at least \(k\).
The same argument gives the one-marginal certificate of Proposition 2.4.
If \(T(I)=I\), \(\mathrm{DS}(T)\leq1/N\), and \(T(P)\) had rank at most \(k-1\), then \(k<N\) and

\[
\left|\operatorname{Tr}P(T^*(I)-I)\right|
\leq\sqrt{k/N}<1,
\]

contradicting \(\operatorname{Tr}T(P)\leq k-1\).
Use the adjoint if the other marginal is normalized.
For arbitrary scalings whose defects approach zero, first row-normalize: the row marginal and its inverse square root tend to \(I\), and the other marginal still tends to \(I\), by positivity and bounded marginal norms.
The certificate then applies.
The current supplied formal article, p. 453 / PDF p. 6, prints the square root in the Cauchy-Schwarz estimate, agreeing with the bound above.
The earlier assertion here that it was omitted is corrected by direct passage inspection on 2026-10-14; the qualitative reconstruction and its original review scope are unchanged.

### Inspection boundaries and intended use

The qualitative chain and the one-marginal certificate were reconstructed and self-checked as above.
Formula pages 462-464 were visually inspected.
Spectral calculus, Cauchy-Binet, compactness and elementary determinant identities are the retained foundations; no theorem from an inaccessible earlier scaling paper is a premise of this reconstruction.
The exact two-sided estimate (32), the unnormalized threshold in the second part of Proposition 2.4, and quantitative iteration/bit bounds are not claimed audited here.
Theorem 4.6's additional fixed-epsilon formulation was read, but the reusable statement above uses the all-epsilon formulation and the explicitly checked certificate.

This is the finite-dimensional scaling input to the comparison with GGOW20 and MS24.
It gives neither an invertible scalar linear combination without ERP nor boundedness of an affiliated rational operator.
