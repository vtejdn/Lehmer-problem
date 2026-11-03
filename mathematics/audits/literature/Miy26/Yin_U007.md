---
author: Yin
---

# Observable eigenvalues and the spectral-radius shortcut

<a id="miy26-u007"></a>
## Miy26-U007 — Remarks 1.5 and 4.7 and Figure 1

- Source: [Miy26](../../../literature/pdf/Miy26.pdf), the exact arXiv v2 artifact, 2026-04-21.
- Locator: Remark 1.5 and Figure 1, pp. 3-4; complete Remark 4.7, pp. 19-21.
- Record: 2026-09-08, quadratic-spectrum audit agent; direct reading, rendered-formula inspection, reconstructed finite-dimensional proof, and exact tests.
The separate circular-section agent independently cross-reviewed the proof and reproduced the computation on the same date.
- Kind/state: a restricted spectral-radius replacement and four examples; audited within scope after two displayed-formula corrections and explicit treatment of zero cases.
No unrestricted replacement or convergence result is claimed.
- Use: [Miy26 spectral source audit](readme.md#miy26-spectral-source-audit); depends on [U006](Yin_U006.md#miy26-u006).

### Exact scope and conventions

Use \(B=A/\lambda\), \(d=b/\lambda\), \(S=\operatorname{Tr}(B^*B)\), \(\beta=d^*d\), and \(Q=Q_\lambda\) from U006, always with \(\lambda\ne0\).
A bar is entrywise conjugation.
The source proves

\[
 Q^ne_1\not\longrightarrow0\quad\Longleftrightarrow\quad r(Q)\ge1
\]

provided at least one of the following holds: \(b=0\); \(\overline AA\) does not have two distinct real eigenvalues; or \(A=A^T\).
Symmetry means complex transpose symmetry, not Hermitian symmetry.
These conditions remain unchanged under the scaling by \(\lambda\), since \(\overline BB=|\lambda|^{-2}\overline AA\).

For arbitrary \(A,b\), \(r(Q)<1\) always implies decay.
The exact unconditional converse uses \(r(Q|_{K_\lambda})\), with \(K_\lambda\) defined in U006.
The source explicitly says it has no counterexample to unrestricted replacement; this audit neither supplies one nor turns that lack into a theorem.
For illustration of the general linear-algebra obstruction only, \(\operatorname{diag}(0,2)^ne_1\to0\) although its spectral radius is two.
This illustrative matrix is not asserted to be a Miy26 matrix.

### Hidden maximal eigenvalues and the nonsymmetric case

Suppose an eigenvalue \(\rho\ne0\) of maximal modulus is absent from the generalized-eigenspace decomposition of \(e_1\).
Every left eigenvector \(v\) for \(\rho\) then annihilates \(e_1\).
Writing it in blocks as \((v_1,v_2,u,w)\), the equations \(vQ=\rho v\) give

\[
 v_1=v_2=0,\qquad u\overline d+wd=0,\qquad
 (u,w)H=\rho(u,w),\quad
 H=\begin{pmatrix}0&\overline B\\B&0\end{pmatrix}.
\]

Only this necessary implication is used: annihilation by ordinary left eigenvectors alone is not asserted to characterize absence from generalized eigenspaces.

If \(b=0\), \(Q\) is the direct sum of \(\begin{pmatrix}0&S\\1&0\end{pmatrix}\) and \(H\).
For \(S>0\), the first block contributes both \(\pm\sqrt S\) to the cyclic subspace.
Also \(r(H)\le\|H\|=\|B\|\le\sqrt S\).
Thus the cyclic and full radii coincide.
If \(S=0\), then \(B=0\) and \(Q\) is nilpotent.
The source's p. 19 eigenvalue \(\sqrt{\operatorname{Tr}(|B|)}\) must therefore be \(\sqrt{\operatorname{Tr}(|B|^2)}=\sqrt S\).
For example, \(B=\operatorname{diag}(4,0)\) has a top-block eigenvalue four, not the printed value two.

For the remaining cases, let \(\mu_1,\mu_2\) be the eigenvalues of \(B\overline B\), ordered by modulus.
They are also the eigenvalues of \(\overline BB\), because the characteristic polynomials of the two products agree.
Their sum is real and their product is \(\delta^2\), where \(\delta=|\det B|\).
They are therefore a conjugate pair or real with nonnegative product.
Moreover,

\[
 \det Q=-S\delta^2,\quad S\ge2\delta,
 \quad\max_j|\mu_j|\le\|B\|^2\le S.
\]

The determinant identity follows by expanding column two and then the remaining first row; the result is independent of \(d\).
If the \(\mu_j\) are conjugate, including repeated real eigenvalues, a nonzero hidden \(\rho\) would have \(|\rho|^2=\delta>0\).
Maximality would give \(S\delta^2=|\det Q|\le|\rho|^6=\delta^3\), contradicting \(S\ge2\delta\).
If \(\delta=0\) in this conjugate case, both \(\mu_j=0\), which contradicts \(\rho\ne0\) before any division is made.
This proves the second listed condition, including singular and zero matrices.

For use in the symmetric case, continue under distinct real \(\mu_j\).
A nonzero real simple eigenvalue of \(\overline BB\) is positive: the antilinear map \(x\mapsto\overline B\overline x\) preserves its one-dimensional eigenspace and squares there to \(\overline BB\); if its scalar is \(\alpha\), the eigenvalue is \(|\alpha|^2>0\).
Hence \(\mu_1>\mu_2\ge0\).
A maximal hidden \(\rho\) cannot square to the smaller eigenvalue.
If \(\mu_2=0\), this is immediate; otherwise maximality would imply \(S\mu_1\mu_2\le\mu_2^3\), whereas \(S\ge\mu_1>\mu_2\).
Thus necessarily \(\rho=\pm\sqrt{\mu_1}\).

### Symmetric case: Schur complement and all endpoint cases

Assume \(B=B^T\).
Then \(T=B\overline B=BB^*\) is Hermitian positive semidefinite.
The equal-eigenvalue case was just handled, so take \(\mu_1>\mu_2\ge0\).
Decompose \(d=d_1+d_2\) into the orthogonal spectral subspaces of \(T\); a component is allowed to be zero.
For each nonzero component there is a scalar \(\alpha_j\) satisfying

\[
 \overline B d_j=\alpha_j\overline{d_j},\qquad |\alpha_j|^2=\mu_j.
\]

For a zero component choose any \(\alpha_j\) of the stated modulus; equations involving that component remain zero.
Set \(\beta_j=\|d_j\|^2\), so \(\beta=\beta_1+\beta_2\) and \(S=\mu_1+\mu_2\).

Let \((u,w)\) be the nonzero left eigenvector of \(H\) above.
The simple Hermitian eigenspaces give \(wd=wd_1\) and \(u\overline d=u\overline{d_1}\).
From \(u\overline B=\rho w\) and the annihilation equation one gets \((\rho+\alpha_1)wd_1=0\).
If \(wd_1=0\), nonzero \(w\) is a left eigenvector for the simple eigenvalue \(\mu_1\), so \(d_1=0\).
Otherwise \(\alpha_1=-\rho\).
This proves the source's two-case reduction without calling a zero projection an eigenvector.

For real \(x>\sqrt{\mu_1}\), put

\[
 D(x)=x^2+\beta x-S
 -x^2(d^T,d^*)(xI_4-H)^{-1}(\overline d,d)^T.
\]

The ordinary Schur complement gives

\[
 \det(xI_6-Q)=\det(xI_4-H)D(x).
\]

In the spectral decomposition above, inversion of the two-by-two blocks yields

\[
 (d^T,d^*)(xI_4-H)^{-1}(\overline d,d)^T
 =\sum_{j=1}^2\frac{2x+\alpha_j+\overline{\alpha_j}}{x^2-\mu_j}\,\beta_j.
\]

Thus

\[
 D(x)=x^2-S-\sum_{j=1}^2
 \frac{x|x+\alpha_j|^2}{x^2-\mu_j}\,\beta_j.
\]

It tends to \(+\infty\) as \(x\to+\infty\).
In the case \(d_1=0\),

\[
 D(\sqrt{\mu_1})=-\mu_2-
 \frac{\sqrt{\mu_1}|\sqrt{\mu_1}+\alpha_2|^2}{\mu_1-\mu_2}\,\beta_2<0,
\]

unless \(\mu_2=\beta_2=0\), which is already the \(b=0\) case.
The strict inequality follows from \(|\alpha_2|=\sqrt{\mu_2}<\sqrt{\mu_1}\).
Continuity then produces an eigenvalue \(x>\sqrt{\mu_1}=|\rho|\), contradicting maximality.

In the other case take \(d_1\ne0\), so \(\beta_1>0\), and \(\alpha_1=-\rho\).
The corrected expression is

\[
 D(x)=x^2-S-
 x\frac{x-\rho}{x+\rho}\,\boxed{\beta_1}
 -\frac{x|x+\alpha_2|^2}{x^2-\mu_2}\,\beta_2.
\]

The boxed factor is absent in the source's corresponding line on p. 21.
If \(\rho=-\sqrt{\mu_1}\), the \(\beta_1\) term forces \(D(x)\to-\infty\) as \(x\downarrow\sqrt{\mu_1}\), and again a larger eigenvalue exists.
If \(\rho=+\sqrt{\mu_1}\), evaluating at that endpoint gives the same nonpositive expression as in the preceding case.
It is strictly negative unless \(\mu_2=\beta_2=0\).
The omitted factor therefore does not alter either argument, but it must be restored for a correct identity.

In the remaining endpoint, \(d=d_1\), \(\mu_2=0\), \(S=\rho^2\), and \(\overline B d=-\rho\overline d\).
Direct multiplication shows that

\[
 \ell=(1,\rho,-\tfrac12d^T,-\tfrac12d^*)
 \quad\text{satisfies}\quad \ell Q=\rho\ell,\qquad \ell e_1=1.
\]

For example, its first component is \(\beta+\rho-\beta/2-\beta/2=\rho\), its second is \(S=\rho^2\), and symmetry gives the remaining components.
Thus \(\rho\) is not hidden, also contradicting the starting hypothesis.
This completes the source's symmetric case including the singular endpoint.

The argument proves that some eigenvalue of full maximal modulus participates in the cyclic subspace in each stated case.
Combined with the Jordan criterion in U006, this is enough for the claimed spectral-radius replacement; diagonalizability of \(Q\) was not assumed.

### Four figures and their actual evidential scope

The polynomial coefficients in Figure 1 and Remark 1.5 agree:

| Figure | \(A\) | \(b\) | Applicable case |
| --- | --- | --- | --- |
| A | \(\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}\) | \((1/2,1/2)^T\) | Symmetric |
| B | \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) | \((1,1)^T\) | Symmetric |
| C | \(\begin{pmatrix}1&0\\1&-1\end{pmatrix}\) | \((1,i)^T\) | \(\overline AA=A^2=I\), repeated eigenvalue |
| D | \(\begin{pmatrix}i/2&1\\2&1\end{pmatrix}\) | \(0\) | Homogeneous, \(b=0\) |

The caption says gray denotes \(r(Q_\lambda)<1\), the red curve its boundary, and blue points eigenvalues of a corresponding size-3000 Ginibre model.
The algebraic shortcut is justified for all four examples.
For D, the analytic criterion gives a disk of radius \(\sqrt{\operatorname{Tr}(A^*A)}=5/2\), consistent with the drawn circle.
The original size-3000 experiments were not rerun: the paper supplies no seed, code, or numerical error control in these passages.
No empirical-density convergence, absence of spectral outliers, Hausdorff convergence, or Brown-support equality for general quadratics is proved by Figure 1.
Related external random-matrix reports belong to the separately scoped source interfaces, not to this numerical observation.

### Verification evidence, corrections, and limits

The preserved computation verifies 48 determinant identities, 96 nonsingular Schur identities, and a rank-one endpoint left eigenvector in exact Gaussian-rational arithmetic.
It gives a concrete witness to the missing factor: \(A=\operatorname{diag}(-2,1)\), \(b=(3,0)^T\), \(\lambda=1\), \(x=3\).
The actual and corrected Schur value is \(-7/5\); the printed formula gives \(17/5\).
All recurrence checks and four figure coefficient cases are also retained there.

Independent AI cross-review by the circular-section agent on 2026-09-08 checked the antilinear proof of positivity for simple real product eigenvalues, the determinant zero cases, the corrected Schur sign and missing norm factor, zero spectral projections, the \(\beta_1>0\) case split, and the endpoint left eigenvector.
That agent inspected source renders pp. 18-21 and reproduced the retained exact checks.
No unresolved issue was found within the three restricted cases; the general replacement remains outside the conclusion.

All proof passages pp. 19-21 and figures pp. 3-4 were visually inspected.
The [public v2 HTML](https://arxiv.org/html/2603.19528v2#S4) was opened on 2026-09-08 to disambiguate bars and transposes and confirms both displayed-formula errors; this was a bounded source comparison, not a claim that no later correction exists.
The determinant zero cases, zero spectral projections, and ordinary-versus-generalized left eigenvector issue were separately checked in this reconstruction.
The universal proof uses elementary finite-dimensional linear algebra; finite computations only supplement it.
Original external analytic proofs, unrestricted replacement, original plotting reproducibility, external human review, and formal verification remain outside this unit.

## Source and inspection

Source edition: Miy26, arXiv:2603.19528v2, dated 2026-04-21; the registered 23-page artifact. Printed page numbers equal PDF page numbers. Other works retain the separate versions and limitations stated in the body.

Passages: Remark 1.5 and Figure 1, pp. 3-4; complete Remark 4.7, pp. 19-21.

Inspection: 2026-09-08: the three restricted spectral-radius cases, Schur calculation and singular endpoints reconstructed and independently cross-reviewed, including reproduced exact checks. Figure coefficients and evidence limits were inspected; the general spectral-radius replacement, Brown-support and random-matrix conclusions remain outside the stated result.
