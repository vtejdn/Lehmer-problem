---
author: Yin
---

# Quadratic circular polynomials and the six-state recurrence

<a id="miy26-u006"></a>
## Miy26-U006 — Theorems 1.4 and 4.6

- Source: [Miy26](../../../literature/pdf/Miy26.pdf), the exact arXiv v2 artifact, 2026-04-21.
- Locator: Theorem 1.4, pp. 2-3; Theorem 4.6 and its complete proof, pp. 17-19.
  Printed pages equal PDF pages.
- Record: 2026-09-08, quadratic-spectrum audit agent; direct reading, visual formula inspection, independent reconstruction, and exact finite checks.
  The separate circular-section agent independently cross-reviewed this reconstruction and reproduced the computation on the same date.
- Kind/state: spectral criterion and finite recurrence; audited within the stated scope, subject to the explicitly linked analytic interfaces.
  No formal verification.
- Authorized use: [Miy26 spectral source audit](readme.md#miy26-spectral-source-audit), source audit; no new project theorem is claimed.

### Statement, setting, and notation

Let \(c_1,c_2\) be a standard free circular system in its faithful tracial von Neumann algebra: \(\tau(c_i^*c_j)=\delta_{ij}\).
Holomorphic words \(c_w\), including \(c_\varnothing=1\), are orthonormal in the holomorphic \(L^2\) subspace.
The normalization and Fock realization are in [U001](Yin_U001.md#miy26-u001); the holomorphic resolvent interface is in [U004](Yin_U004.md#miy26-u004).

For arbitrary \(A=(a_{ij})\in M_2(\mathbb C)\), \(b=(b_1,b_2)^T\in\mathbb C^2\), set

\[
 f=\sum_{i,j=1}^{2}a_{ij}c_ic_j+\sum_{i=1}^{2}b_ic_i.
\]

The coefficient matrix need not be symmetric: the two ordered monomials \(c_1c_2\) and \(c_2c_1\) are distinct.
For \(\lambda\ne0\), abbreviate \(B=A/\lambda\), \(d=b/\lambda\), \(S=\operatorname{Tr}(B^*B)\), and \(\beta=d^*d\).
The trace here is the ordinary, unnormalized matrix trace.
A bar means entrywise complex conjugation, \(T\) means transpose, and \(*\) means conjugate transpose.
In blocks of sizes \(1,1,2,2\), define

\[
 Q=Q_\lambda=
 \begin{pmatrix}
 \beta&S&d^*B&d^T\overline B\\
 1&0&0&0\\
 \overline d&0&0&\overline B\\
 d&0&B&0
 \end{pmatrix},\qquad e_1=(1,0,0,0,0,0)^T.
\]

Then the precise spectral criterion is

\[
 \operatorname{spec}(f)=\{0\}\cup
 \{\lambda\in\mathbb C\setminus\{0\}:Q_\lambda^ne_1\not\longrightarrow0\}.
\]

The source prints \(\lim Q_\lambda^ne_1\ne0\).
This is read as failure to converge to zero, including unbounded or oscillating orbits; existence of a nonzero limit is not required.
A scalar constant term \(a_0\) simply translates this set by \(a_0\).

### Reconstruction of the coefficient and state identities

For \(\lambda\ne0\), the formal noncommutative inverse is uniquely defined by

\[
 a=\lambda^{-1}\sum_{k\ge0}(f/\lambda)^k=\sum_w\alpha_wc_w.
\]

This is initially a formal series: each word receives contributions from only finitely many powers because \(f\) has no constant term.
Comparing coefficients gives

\[
 \alpha_\varnothing=\lambda^{-1},\quad
 \alpha_i=b_i\lambda^{-2},\quad
 \alpha_{ijw}=B_{ij}\alpha_w+d_i\alpha_{jw}.
\]

Define real nonnegative \(x_n\) and a complex two-vector \(h_n\) by

\[
 x_n=\sum_{|w|=n}|\alpha_w|^2,\qquad
 (h_n)_j=\sum_{|w|=n}\alpha_w\overline{\alpha_{jw}}.
\]

Expanding the squared norm in the coefficient equation, with both cross terms retained, yields

\[
 x_{n+2}=\beta x_{n+1}+Sx_n+d^*Bh_n+d^T\overline B\,\overline{h_n}.
\]

Separately,

\[
 \begin{aligned}
 (h_{n+1})_j
 &=\sum_{i,|w|=n}\alpha_{iw}\overline{\alpha_{jiw}}\\
 &=\overline{d_j}x_{n+1}
   +\sum_i\overline{B_{ji}}\,\overline{(h_n)_i},
 \end{aligned}
\]

so the correct vector recursion is \(h_{n+1}=\overline d\,x_{n+1}+\overline B\,\overline{h_n}\).
Thus, for

\[
 t_n=(x_{n+1},x_n,h_n^T,\overline{h_n}^{\,T})^T,
\]

one has \(t_{n+1}=Qt_n\), and the initial values

\[
 x_0=|\lambda|^{-2},\quad x_1=|\lambda|^{-2}\beta,
 \quad h_0=|\lambda|^{-2}\overline d
\]

give \(t_n=|\lambda|^{-2}Q^{n+1}e_1\).
This verifies the order of every block, transpose, and conjugation in the source matrix.

### Analytic implications, with the converse constructed explicitly

If \(\lambda\) is in the resolvent set, [U004](Yin_U004.md#miy26-u004) puts the resolvent vector in the holomorphic \(L^2\) subspace, and uniqueness makes its coefficients the formal coefficients above.
Square summability gives \(x_n\to0\).
Cauchy-Schwarz gives

\[
 |(h_n)_j|\le\sqrt{x_n\sum_{|w|=n}|\alpha_{jw}|^2}
 \le\sqrt{x_nx_{n+1}},
\]

so \(Q^{n+1}e_1\to0\).

For the converse, start with the formal coefficients, without assuming an existing \(L^2\) inverse.
If \(Q^ne_1\to0\), then the displayed state identity implies \(x_n\to0\).
The sequences of shifts of \((x_n)\) span a finite-dimensional space: each shift is a coordinate sequence of powers of the same six-dimensional matrix.
The finite-dimensional decay lemma, Lemma 3.3 in [U002](Yin_U002.md#miy26-u002), therefore gives exponential decay and \(\sum_nx_n<\infty\).
Equivalently, one may apply the Jordan decomposition to the cyclic subspace described below.

Consequently, \(X=\sum_w\alpha_wc_w\) exists in \(L^2\).
Multiplication by the bounded polynomial \(\lambda-f\) is continuous on \(L^2\), and its coefficient identities give \((\lambda-f)X=1\).
The affiliated inverse identification and Corollary 1.2 in [U003](Yin_U003.md#miy26-u003) then make \(X\) the bounded inverse.
More explicitly, if \(f\ne0\), algebraic freeness and the division-field realization give an affiliated inverse of the nonzero \(\lambda-f\), so the right-inverse equation identifies \(X\) with it; if \(f=0\), the assertion is immediate.
This fills the source proof's compressed step from a formal recurrence to the claimed \(L^2\) inverse.

Finally, \(0\in\operatorname{spec}(f)\).
A bounded inverse, by U004, would have a holomorphic expansion, but the vacuum coefficient of \(-fX\) is zero and cannot equal that of \(1\).
The zero polynomial also has spectrum \(\{0\}\).

### Finite-dimensional interpretation and boundary cases

Let \(K_\lambda=\operatorname{span}\{e_1,Qe_1,\ldots,Q^5e_1\}\).
Cayley-Hamilton makes this a \(Q\)-invariant subspace.
The orbit converges to zero if and only if \(r(Q|_{K_\lambda})<1\): the forward implication holds because powers of \(Q|_K\) converge to zero on its spanning orbit vectors; the reverse follows from Jordan normal form.
Every participating Jordan block of modulus at least one prevents decay.
This supplies an exact finite-dimensional reading of the criterion, without assuming diagonalizability.
It is the subspace generated by the specified input vector that matters, not an arbitrary choice of all six eigenvalues.

When \(A=0\), the criterion reduces to \(\operatorname{spec}(f)=\{|\lambda|\le\|b\|_2\}\): \(x_n=|\lambda|^{-2}(\|b\|_2^2/|\lambda|^2)^n\).
When \(b=0\), \(x_{2k}=|\lambda|^{-2}S^k\) and \(x_{2k+1}=0\), giving radius \(\sqrt{\operatorname{Tr}(A^*A)}\).
These include equality on the boundary.
If \(A=b=0\), \(Q^2=0\) and only the separately included point zero remains.
The general all-eigenvalue shortcut is discussed, with its precise proved cases, in [U007](Yin_U007.md#miy26-u007).

### Findings, evidence, and verification limits

The single compressed \(h\)-recursion on p. 18 has \(h_n\) on its left side; it must be \(h_{n+1}\).
The adjacent scalar equations, the six-state matrix, and the subsequent state identity already have the correct indexing.
This is a local displayed-equation correction, not a counterexample to the theorem.

The exact computation and execution record compare direct finite geometric-series word multiplication against the six-state recurrence for 48 specified Gaussian-rational inputs and all word lengths through seven.
They also check the determinant and Schur identities consumed by U007.
The analytic implications above are mathematical arguments, not consequences of the finite tests.

The circular-section agent independently read this unit and U007, inspected the source renders on pp. 18-21, read the retained script, and reproduced its 14,355 stated finite checks on 2026-09-08.
The native program and execution account are located at [original J_F0007](readme.md#original-native-checks).
The source-only fixed program encodes its required finite inputs and needs no separate dataset.
The recorded result and rerun scope remain historical evidence; this locator repair performs no new run.
That review found no unresolved issue in the formal-to-analytic construction, conjugation conventions, or declared finite-dimensional criterion.
This is an independent AI cross-review, not external human review.

Theorem and proof pages 17-19 and the introductory repetition on pp. 2-3 were read and visually checked against the local PDF.
On 2026-09-08 the public [v2 HTML](https://arxiv.org/html/2603.19528v2#S4) was opened to resolve extraction ambiguities; it agrees with the bars, block order, and indexing typo.
This was a bounded formula/version comparison, not a search establishing absence of later errata.
External original proofs behind U001-U004 were not independently re-audited by this unit.
No claim of random-matrix convergence, Brown-support equality for general quadratic polynomials, human peer review, or formal verification follows.

## Source and inspection

Source edition: Miy26, arXiv:2603.19528v2, dated 2026-04-21; the registered 23-page artifact. Printed page numbers equal PDF page numbers. Other works retain the separate versions and limitations stated in the body.

Passages: Theorem 1.4, pp. 2-3; Theorem 4.6 and its complete proof, pp. 17-19.

Inspection: 2026-09-08: all six recurrence blocks and the formal-to-L2 inverse argument reconstructed and independently cross-reviewed, with rendered-formula inspection and reproduced exact finite checks. The criterion concerns decay of the specified orbit; the general all-eigenvalue shortcut is not proved. No formal verification or external human review.
