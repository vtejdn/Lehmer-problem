---
author: Yin
---

# Quantum Permanent and Gaussian Polynomial Norms

## Source and inspection

Source edition: This audit reads the user-supplied published article by Leonid Gurvits, *Classical complexity and quantum entanglement*, Journal of Computer and System Sciences 69 (2004), 448-484, DOI [10.1016/j.jcss.2004.06.003](https://doi.org/10.1016/j.jcss.2004.06.003).

Passages: Locators: Definition 3.1, Propositions 3.4 and 3.6, Corollaries 3.5 and 3.7, Theorem 3.8, pp. 456-460 / PDF pp. 9-13; Appendix A, pp. 473-475 / PDF pp. 26-28; Appendix C, pp. 477-480 / PDF pp. 30-33.

Inspection: Main coefficient/norm identity and its rank consequence audited within the reconstruction below.


The sole bibliography is the Gur04 intake.

Edition: published JCSS article, 37 PDF pages; printed page equals PDF page plus 447.
Current artifact identity; the original review date and scope below are retained.

## Gur04-U004

- Source: [Gur04 version record](readme.md#source-version).
- Locators: Definition 3.1, Propositions 3.4 and 3.6, Corollaries 3.5 and 3.7, Theorem 3.8, pp. 456-460 / PDF pp. 9-13; Appendix A, pp. 473-475 / PDF pp. 26-28; Appendix C, pp. 477-480 / PDF pp. 30-33.
- Record: 2026-09-12, source-audit agent, self-review.
Main coefficient/norm identity and its rank consequence audited within the reconstruction below.
The unrestricted Appendix C statements are **Questioned**, with exact counterexamples; their homogeneous/IID Gaussian applications remain valid.
- Kind: definition, determinant identity, proof mechanism, and correction record.

### Definitions and checked statement

The mixed discriminant convention is

\[
D(B_1,\ldots,B_N)=[x_1\cdots x_N]\det\Bigl(\sum_i x_iB_i\Bigr),
\]

without division by \(N!\).
For a block matrix \(\rho=[B_{ij}]\in M_{N^2}(\mathbb C)\), define

\[
\operatorname{QP}(\rho)=\sum_{\sigma\in S_N}\operatorname{sgn}(\sigma)
D(B_{1,\sigma(1)},\ldots,B_{N,\sigma(N)}).
\]

For \(A_1,\ldots,A_k\in M_N(\mathbb C)\), let \(T(X)=\sum_iA_iXA_i^*\), \(\rho_A=\mathrm{CH}(T)\), and \(p(z)=\det(\sum_i z_iA_i)=\sum_{|r|=N}a_rz^r\).
Theorem 3.8 gives

\[
\operatorname{QP}(\rho_A)
=\sum_{|r|=N}|a_r|^2\prod_i r_i!
=\mathbb E\left|p(g_1,\ldots,g_k)\right|^2,
\]

where the \(g_i\) are independent standard complex Gaussian variables: real and imaginary parts have variance (1/2), so \(\mathbb E|g_i|^2=1\).
Consequently

\[
\operatorname{QP}(\rho_A)>0
\iff \det\Bigl(\sum_i z_iA_i\Bigr)\not\equiv0
\iff \operatorname{span}_{\mathbb C}\{A_i\}\text{ contains an invertible matrix}.
\]

Thus quantum permanent detects the ordinary scalar Edmonds problem.
Capacity detects rank non-decrease.
Their positive loci differ without the [ERP promise](Yin_U001.md#edmonds-rado-property).

### Reconstruction and checked constants

Gaussian polar integration gives \(\mathbb E(g^r\overline g^{,s})=\delta_{r,s}r!\); independence proves the polynomial norm identity.
For a multi-index \(r\), let \(A[r]\) contain \(r_i\) copies of \(A_i\).
Determinant polarization gives \(a_r=D(A[r])/\prod_i r_i!\).
Expanding the Choi blocks in the definition of QP and the alternating determinant sums gives Appendix A's \(A.6\),

\[
\operatorname{QP}(\rho_A)
=\frac1{N!}\sum_{i_1,\ldots,i_N}|D(A_{i_1},\ldots,A_{i_N})|^2.
\]

Grouping the \(N!/\prod r_i!\) ordered tuples of each multiplicity yields the claimed coefficient identity.
These finite algebraic steps and factorials were checked, using the source's main definition and Appendix A rather than relying on Appendix C's overstated auxiliary statements.

For \(\rho\geq0\), the bound in Corollary 3.5 is

\[
0\leq\operatorname{QP}(\rho)
\leq N!D(B_{11},\ldots,B_{NN})
\leq N!\det\Bigl(\sum_i B_{ii}\Bigr).
\]

The first upper bound follows by compressing \(\rho^{\otimes N}\) to the permutation-indexed blocks and applying the positive-matrix Cauchy-Schwarz inequality; the second is coefficient nonnegativity.
The normalized alternating vector printed in the proof on p. 459 needs a factor \(N!\) in its mixed-discriminant equality, but this factor occurs in every entry and leaves the inequality intact.

For a separable Choi matrix, Corollary 3.7 gives \(\det T(X)\geq\operatorname{QP}(\rho)\det X\), \(X>0\).
In a rank-one Kraus presentation, Cauchy-Binet expands \(\det T(X)\) as a sum over \(N\)-element subsets.
On each subset, Hadamard applied to the positive Gram matrix \([y_i^*Xy_j]\) gives \(\prod_i y_i^*Xy_i\geq\det X\,|\det[y_i]|^2\).
Summation gives the inequality.
This requires actual separability of the Choi matrix, not just the existence of a rank-one spanning family for its support.

<a id="appendix-c-corrections"></a>
### Reuse restrictions and primary-text corrections

**F01: the vector normalization in Remark 3.2 is incorrect.**
On p. 457 the vector \(Z\) has \((N!)^2\) nonzero entries, each of magnitude \(1/\sqrt{N!}\).
Thus \(\|Z\|^2=N!\), not one.
Equation (17) is consistent with that vector, but its normalized measurement probability is \(\operatorname{QP}(\rho)/N!\).
On p. 459 the alternating vector \(V\) does have norm one, so the mixed-discriminant identity with it must include \(N!\).
Both discrepancies were checked on rendered pages and with the test \(B_i=I\), for which \(D(I,\ldots,I)=N!\).
They do not refute Theorem 3.8.

**F02: Lemma C.2 is false for arbitrary \(g\in L^2(\mathbb C^k,\mu)\).**
It asserts \(\langle P\circ A,g\rangle=\langle P,g\circ A^*\rangle\) for homogeneous holomorphic \(P\) and every matrix \(A\).
Take \(k=N=1\), \(P(z)=z\), \(g(z)=z(|z|^2-2)\), and \(A=2\), with standard complex Gaussian measure.
Both sides are well-defined polynomial integrals, but

\[
\langle2z,g\rangle=2(2-2)=0,
\qquad
\langle z,g(2z)\rangle=2(4\cdot2-2)=12.
\]

The source's orthogonal projection of \(g\) onto degree \(N\) does not justify discarding the orthogonal remainder after a nonunitary substitution.
Restricting \(g\) to a homogeneous holomorphic polynomial of the same degree makes the stated singular-value-decomposition proof valid.
That is precisely the case used by Proposition C.6; an arbitrary Gaussian \(L^2\) extension must not be imported.

**F03: Proposition C.5(1)'s independence hypothesis is insufficient.**
Its p. 479 conditions require zero mean, unit second moment for each matrix entry, and independence along each permutation transversal.
Let \(N=2\), let \(a,d\) be independent symmetric signs, and put

\[
X=\begin{pmatrix}a&a\\d&d\end{pmatrix}.
\]

Both transversals consist of the independent pair \(a,d\), yet \(\det X=0\) identically.
With \(T=\mathrm{Id}_{M_2}\), the claimed expectation is zero whereas \(\operatorname{QP}(\mathrm{CH}(T))=2\).
Full independence of all entries, with the appropriate centered unit-variance moments, suffices for the determinant expectation; the IID Gaussian specialization used in Proposition C.6 meets that stronger condition.

**F04: Proposition C.5(2)'s pairwise moment condition is also insufficient.**
Even adding unit variances does not fix it: let \(r\) equal \(0\) or \(\sqrt2\) with equal probability and let \(\varepsilon_1,\varepsilon_2\) be independent symmetric signs independent of \(r\).
Set \(z_i=r\varepsilon_i\).
These variables are centered, have unit variance and zero cross covariance.
For \(A=I_2\), the claimed permanent formula would give \(1=\mathbb E|z_1z_2|^2=2\).
The fully independent standard complex Gaussian case used for the source's Gaussian formulas is valid.

The relevant full PDF pages 457, 459 and 478-479 were visually inspected.
F02-F04 are exact analytic/finite-distribution counterchecks, not numerical evidence.
The supplied original PDF is preserved.
No formal publisher erratum was identified in the bounded search; these are local audit findings, not an assertion that no correction exists elsewhere.

### Dependencies, use, and unchecked scope

The checked identity uses determinant expansion, finite sums and Gaussian moments.
No external source proof is needed for this reconstruction.
This unit is useful for distinguishing ordinary determinant rank from operator-scaling rank and for reusing the correctly normalized Gaussian polynomial inner product.
It does not provide an unrestricted composition operator on Gaussian \(L^2\), a general random estimator under pairwise independence, or an operator-boundedness theorem in free probability.
The rest of Appendix B's Wick/hafnian reformulation and Appendix C's tensor-index permutations were read for orientation rather than subjected to a complete independent proof audit.
