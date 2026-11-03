---
author: Yin
---

# Rational Scaling, Precision, and Capacity Approximation

## Source and inspection

Source edition: Source: [GGOW20 source index](readme.md), full published *Operator Scaling: Theory and Applications*, Foundations of Computational Mathematics 20 (2020), pp. 223-290.

Passages: Locators: Proposition 4.1, Lemmas 4.2-4.4 and equations (15)-(20), pp. 261-269; Theorem 4.5, pp. 269-274; Lemmas 5.1-5.2, Theorems 5.3-5.4 and Algorithms 3-4, pp. 274-279.

Inspection: Rational recurrences, sensitivity mechanism and a conservative polynomial-precision reconstruction are audited within the scope below.


## GGOW20-U004

- Source: [GGOW20 source index](readme.md), full published *Operator Scaling: Theory and Applications*, Foundations of Computational Mathematics 20 (2020), pp. 223-290.
The registered key is retained; this unit supersedes no result of a different version silently.
- Artifact: [GGOW20.pdf](../../../literature/pdf/GGOW20.pdf), 68 pages.
Printed page equals PDF page plus 222.
- Locators: Proposition 4.1, Lemmas 4.2-4.4 and equations (15)-(20), pp. 261-269; Theorem 4.5, pp. 269-274; Lemmas 5.1-5.2, Theorems 5.3-5.4 and Algorithms 3-4, pp. 274-279.
- Record: 2026-09-12, delegated source-audit agent, self-review.
Complete supplied Sections 4-5 were read.
Rational recurrences, sensitivity mechanism and a conservative polynomial-precision reconstruction are audited within the scope below.
Literal printed quantitative constants and the complete quantitative continuity proof are **Questioned** where indicated.
- Kind: computational theorem interface, proof mechanism, and corrections.
No algorithm was implemented or run.

### Reusable mathematical interface

For a completely positive map
\[
T:M_n(\mathbb C)\longrightarrow M_n(\mathbb C),\qquad
T(X)=\sum_{i=1}^m A_iXA_i^*,
\]
with integer matrix input \(A_i\), there is a deterministic algorithm using a polynomial number of bit operations to decide whether \(T\) is rank non-decreasing.
There is also a deterministic polynomial-time algorithm, polynomial in the input bit length and \(1/\varepsilon\), that returns zero when capacity is zero and otherwise an estimate \(\widehat c\) satisfying
\[
(1-\varepsilon)\operatorname{cap}(T)\leq\widehat c
\leq(1+\varepsilon)\operatorname{cap}(T),\qquad 0<\varepsilon<1.
\]

This is the asymptotic interface of Theorems 1.27, 5.3-5.4, with the conservative error-budget reconstruction below.
It is not a certification of Algorithms 3-4 with every literal printed constant.
Rational inputs require denominator clearing and the corresponding determinant scaling factor; no arbitrary-real-number oracle bit model is asserted.
The scalar case \(n=1\) is evaluated directly: capacity is \(\sum_i|A_i|^2\).

Retain the actual input tuple when computing capacity.
Removing redundant Kraus matrices merely because they belong to the same span preserves the rank-nondecrease question but can change the map and its capacity.
The source often works with \(m\leq n^2\); a computational use must check that convention or carry the actual \(m\) in its input-size and norm bounds.

### Exact rational recurrence and what its trace measures

For \(T(I),T^*(I)>0\), set \(S_{-2}=S_{-1}=I\), \(S_0=T^*(I)\), and
\[
S_j=\begin{cases}
T(S_{j-1}^{-1}),&j\geq1\ \text{odd},\\
T^*(S_{j-1}^{-1}),&j\geq1\ \text{even}.
\end{cases}
\]
If \(T_j\) is the map obtained after \(j\) alternating normalizations, beginning with right normalization, equations (18)-(20) give, for \(j\geq1\),
\[
e_j=\operatorname{ds}(T_j)
=\operatorname{Tr}\bigl((S_{j-2}^{-1}S_j-I)^2\bigr),
\qquad
\operatorname{cap}(T_j)
=\frac{\operatorname{cap}(T)}
{\det(S_{j-2})\det(S_{j-1})}.
\]
Here the source's \(\operatorname{ds}\) is the sum of squared Hilbert-Schmidt marginal defects, as in Gur04-U001.
The product \(S_{j-2}^{-1}S_j\) need not be Hermitian.
Its trace-of-square expression is valid by **similarity** to the Hermitian marginal of \(T_j\); replacing it by its Hilbert-Schmidt norm is generally incorrect.

The recurrence follows by writing \(T_j(X)=C_jT(D_j^*XD_j)C_j^*\), \(P_j=C_j^*C_j\), \(Q_j=D_j^*D_j\).
Odd steps leave \(P_j\) fixed and replace \(Q_j\) by \(T^*(P_j)^{-1}\); even steps leave \(Q_j\) fixed and replace \(P_j\) by \(T(Q_j)^{-1}\).
The determinant factors telescope.
These equations were checked for both parities and the first step.
Although Section 4.1 begins by assuming \(T(I)=I\), these identities for \(j\geq1\) hold for the unnormalized input as well.
The first normalized step is what permits the subsequent capacity upper bound of one.

Use \(j\geq1\) in the rounded recurrence: Algorithm 4's invitation to check \(j=0\) requires values it does not define.
An optional \(j=0\) test must separately use the two actual input marginals, not invent \(U_{-2}\) in a formula justified only for normalized steps.

### Spectral control and stable rounding

Suppose \(n\geq2\), \(|(A_i)_{kl}|\leq M\), \(M\geq1\), and both marginals are nonsingular.
Set
\[
B=M^2n^2m,\qquad \alpha=B^{\,n-1}\geq B.
\]
Proposition 4.1 gives \(\alpha^{-1}I\leq T(I),T^*(I)\leq\alpha I\), and hence
\[
\alpha^{-(j+1)}I\leq S_j\leq\alpha^{j+1}I.
\]
The input lower bound uses the positive integer determinant of each marginal and its spectral upper bound.
Positivity transfers order bounds through \(T,T^*\), and inversion reverses them.
This proves the recurrence estimates inductively.
With \(n=1\), the source's \(\alpha=B^{n-1}=1\) would incorrectly bound an arbitrary nonzero scalar map; handle that case directly as above.

Let \(U_{-1}=I,U_0=S_0\), and round each recurrence value symmetrically, producing Hermitian errors \(\Delta_j\).
Entrywise absolute rounding error at most \(2^{-P}\) gives \(\|\Delta_j\|\leq n2^{-P}\), not merely \(2^{-P}\).
Lemmas 4.2-4.3 show, for \(j\leq t\) and sufficiently small \(\delta\geq\max_j\|\Delta_j\|\),
\[
(2^j\alpha^{j+1})^{-1}I\leq U_j\leq2^j\alpha^{j+1}I,
\qquad
\|S_j-U_j\|\leq(2\alpha)^{(2t+1)(t+1)}\delta.
\]
Their proof is a direct induction using
\[
A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}.
\]
The maintained positive spectral lower bounds are essential: this is not an unconditional stability estimate for inversion near a singular matrix.

Write \(M_j=S_{j-2}^{-1}S_j\) and \(N_j=U_{j-2}^{-1}U_j\).
Decompose their difference as
\[
M_j-N_j=S_{j-2}^{-1}(S_j-U_j)
+(S_{j-2}^{-1}-U_{j-2}^{-1})U_j.
\]
The plus sign before \(U_{j-2}^{-1}U_j\) in one printed line on p. 269 is an algebraic typo; the displayed difference here is the one used by the subsequent norm bound.
A conservative combination of the preceding estimates gives
\[
\|M_j-N_j\|\leq(2\alpha)^{10(t+1)^2}\delta.
\]
For the rounded defect \(\widetilde e_j=\operatorname{Tr}((N_j-I)^2)\), trace cyclicity and \(|\operatorname{Tr}A|\leq n\|A\|\) then give the sufficient uniform estimate
\[
|e_j-\widetilde e_j|
\leq n(2\alpha)^{12(t+1)^2}\delta.
\]
Increasing the fixed exponents only weakens these bounds.
Thus a polynomial number of bits in \(t,\log\alpha,\log(1/\eta),\log n\) makes the defect error at most any prescribed \(\eta>0\).
The literal p. 269 formula involving \(\log M\) without an additive constant would give zero bits at \(M=1\); this audit uses the explicit positive quantities \(\log_2(2\alpha)\) and a sufficient precision bound instead.

### Capacity approximation with a conservative error budget

The source's Lemmas 5.1-5.2 were checked completely.
If positive eigenvalues have sum \(n\) and squared deviation \(a\), their product is at most \(\exp(-\min(a,1)/6)\).
For \(a\leq1\), apply the cubic upper estimate for \(\log(1+x)\); for \(a>1\), contract the eigenvalue deviations radially to squared norm one, using monotonicity of the product along that segment.
Therefore every normalization whose nontrivial marginal has defect \(a\) increases capacity by at least
\[
\exp(\min(a,1)/6).
\]
The factor \(1/6\) must be retained.

The reconstruction retains two exact interfaces within GGOW20: [U002](Yin_U002.md#ggow20-u002)'s effective lower bound after the first normalization in Theorem 2.20, written \(\operatorname{cap}(T_1)\geq e^{-L}>0\) with computable \(L\) polynomial in input bit size; and [U003](Yin_U003.md#ggow20-u003)'s Lemma 3.4 near-doubly-stochastic lower bound
\[
\operatorname{cap}(T_j)\geq(1-\sqrt{n e_j})^n
\]
for a map with one marginal normalized and sufficiently small defect.
Their independent source checks belong to the other units and the [capacity-interface review](../../reviews/Yin_R_F0008_v1.md#capacity-ggow20-finding).
This section checks their use, not their original proof chains.

For a requested \(0<\varepsilon<1\), one adequate bookkeeping choice is
\[
\beta=\frac{\varepsilon^2}{256n^3},\qquad
\eta=\frac\beta4,\qquad
t=2+\left\lceil\frac{12(L+1)}\beta\right\rceil.
\]
Run the rounded recurrence and accept the first \(j\geq1\) with \(\widetilde e_j\leq3\beta/4\).
Ensure \(|e_j-\widetilde e_j|\leq\eta\).
Then acceptance implies \(e_j\leq\beta\).
If capacity is positive, failing to encounter a true \(e_j\leq\beta/2\) by this time would make capacity exceed one by the progress estimate, a contradiction.
Such a true small defect guarantees acceptance.
If capacity is zero, a sufficiently small defect is impossible by Lemma 3.4, so the same error margin prevents a false positive.

At acceptance, \(\operatorname{cap}(T_j)\in[1-\varepsilon/16,1]\) by the near-stochastic bound and Bernoulli's inequality.
Write
\[
Q=\det(S_{j-2})\det(S_{j-1}),\qquad
\widehat Q=\det(U_{j-2})\det(U_{j-1}).
\]
Ensure each eigenvalue of these two \(U\) matrices differs from the corresponding \(S\) eigenvalue by at most \(\varepsilon/(64n)\) times that \(U\) eigenvalue.
Weyl's inequality and the already proved lower spectral bound achieve this by further polynomial precision.
Multiplying the \(2n\) relative eigenvalue factors gives \(Q/\widehat Q\in[1-\varepsilon/16,1+\varepsilon/16]\), with room to spare for \(0<\varepsilon<1\).
Hence
\[
\operatorname{cap}(T)=\operatorname{cap}(T_j)Q
\]
implies \(\widehat Q/\operatorname{cap}(T)\in[1-\varepsilon,1+\varepsilon]\).
This explicitly accounts for the reciprocal when passing from a bound on capacity to a bound on the reported number.

For example, taking an integer \(P\) larger than
\[
30(t+2)^2\log_2(2\alpha)
+\log_2\!\left(\frac{1024n^2}{\varepsilon\beta}\right)+10
\]
satisfies the positivity, defect and relative-determinant error requirements above.
It is a deliberately loose sufficient bound, not the printed exponent in Theorem 5.4.
Every intermediate rounded entry has polynomially many integer and fractional bits; exact rational matrix inversion, multiplication and determinant computation on these matrices have polynomial bit cost.
This establishes the stated existence of a polynomial-time approximation procedure within the retained effective-capacity interfaces.
It does not assert strong polynomiality or dependence polynomial in \(\log(1/\varepsilon)\).

<a id="quantitative-corrections"></a>
### Literal quantitative claims not certified

The following defects were checked against the primary rendered pages; they do not negate the qualitative scaling or noncommutative-rank theorem.

- **Singular marginal argument, p. 276:** the proof of Theorem 5.3 incorrectly infers \(T(I)\) singular from \(T^*(I)\) singular.
  For Kraus matrices \(E_{11},E_{21}\) in \(M_2\), \(T(I)=I\) while \(T^*(I)=2E_{11}\).
  The algorithm's zero-capacity answer remains correct: a kernel vector \(v\) of \(T^*(I)=\sum_iA_i^*A_i\) has \(A_iv=0\) for every \(i\), so \(T(vv^*)=0\).
- **Iteration constant, p. 277:** the proof uses growth \(\exp(\varepsilon^2/n^3)\), although Lemma 5.2 supplies only \(\exp(\varepsilon^2/(6n^3))\) at that threshold.
  Retain a larger iteration budget as above; the printed exact budget is not justified by the displayed proof.
- **Error conversion, pp. 277 and 279:** \((1-\varepsilon)\widehat c\leq c\leq\widehat c\) gives \(\widehat c\leq c/(1-\varepsilon)\), not \(\widehat c\leq(1+\varepsilon)c\).
  On p. 279 the bounds with \((1-\varepsilon/2)^2\) have the same reciprocal problem.
  Reserve smaller internal tolerances before promising a symmetric relative error.
- **Rounded precision, pp. 277-279:** the printed \(P\) grows like \(\varepsilon^{-1}\), whereas the displayed Lemma 4.3 amplification for \(t=O(\varepsilon^{-2})\) has an exponent of order \(t^2\).
  The claimed implication \(\|U_i-S_i\|\leq2^{-P/2}\) does not follow for all small \(\varepsilon\) from those supplied estimates.
  The generic polynomial \(P\) above repairs the asymptotic interface, but the printed precision choice is not certified.
- **Threshold arithmetic, p. 279:** from \(\widetilde e_j\leq\varepsilon^2/(4n^3)\) and \(|e_j-\widetilde e_j|<\varepsilon^2/n^4\), the bound needed to infer \(\operatorname{cap}(T_j)\geq1-\varepsilon/2\) does not follow as written.
  Use a stricter defect-error margin rather than dropping the extra term.

### Continuity theorem: exact source statement and proof boundary

Theorem 4.5 states a quantitative local continuity result around rational-data Kraus tuples of bounded bit complexity: if \(A_i\) have entry bit complexity \(b\) and \(\|A_i-B_i\|\leq\delta\), then for a polynomial \(P(n,b,\log m)\) and sufficiently small \(\delta\leq e^{-P}\), positive capacity of \(T_A\) implies positive capacity of \(T_B\), and
\[
1-\frac{P(n,b,\log m)}{\log(1/\delta)^{1/3}}
\leq\frac{\operatorname{cap}(T_A)}{\operatorname{cap}(T_B)}
\leq1+\frac{P(n,b,\log m)}{\log(1/\delta)^{1/3}}.
\]
The ratio is intended in the positive-capacity case.
This is not a uniform relative guarantee at a zero-capacity map, nor does “bit complexity \(b\)” describe an arbitrary real input without an encoding.

The proof seeks an approximately fixed positive matrix of controlled condition number, transfers its approximate fixed-point property to the perturbed map, and compares determinant objectives.
The operator-norm perturbation estimates
\[
\|T_A(D)-T_B(D)\|
\leq\sum_i(\|A_i\|+\|B_i\|)\|A_i-B_i\|\,\|D\|
\]
and their adjoint analogues were checked.
Inverse perturbation is valid only after the perturbation is smaller than the controlled minimum eigenvalue; its required dependence on the approximate-fixed-point tolerance must be retained.

There is a material orientation mismatch: Section 3.2 defines the relevant fixed-point map using \(T^*(T(X)^{-1})\), whereas Section 4.3 uses \(T(T^*(X)^{-1})\) and still evaluates \(\det T(C)/\det C\).
For the latter orientation apply Lemma 3.9 to **\(T^*\)**, and use \(\det T^*(C)/\det C\), together with \(\operatorname{cap}(T)=\operatorname{cap}(T^*)\).
Both the \(A\) and \(B\) families must be consistently replaced by their adjoints in those objective comparisons.
This correction was independently confirmed by the coordinating agent reviewer.

Equation (33) on p. 273 also omits a dimension factor for the operator norm: the universally valid estimate is
\[
\left|\operatorname{Tr}((D_1-I)^2)-\operatorname{Tr}((D_2-I)^2)\right|
\leq n(\|D_1\|+\|D_2\|+2)\|D_1-D_2\|.
\]
These polynomial factors can be absorbed in enlarged \(Q_i,P\), but doing so is part of a complete quantitative reconstruction, not automatic verification of the printed formulas.
The full modulus with all tolerance dependencies and corrected adjoint objectives is therefore recorded as **primary-statement checked, proof partly inspected and questioned at the identified steps**.
It is not imported here as a fully independently audited quantitative estimate.

### Verification and downstream use

All supplied Section 4 and 5 proof text was read, including the first-step conventions, inverse sensitivity, trace-square calculation, determinant accumulation and error conversion.
PDF pages 39, 51, 54-57 were rendered and visually inspected; the complete page contexts made the printed constants and operator orientations unambiguous.
Direct arithmetic and the \(E_{11},E_{21}\) example provide analytic checks, not evidence from a tested implementation.
No further external search was performed for this unit; it uses the downloaded primary published version and the separate source-interface review.

Use the checked conservative polynomial-bit interface when an algorithmic existence input suffices.
A concrete implementation should specify its exact arithmetic, symmetric rounding, precision, stopping indices and internal relative-error allocation.
The source's literal constants and complete quantitative continuity bound require the repairs recorded above before such use.
