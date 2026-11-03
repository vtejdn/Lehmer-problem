---
author: Yin
---

# MS24: External Interfaces and Limits

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

## Source and inspection

Source edition: Retained arXiv:2406.15922v1, 19 pages; margin date 2024-06-22 and distinct title-page date 2024-06-25.

Source passages: The reviewed MS24 version has printed/PDF pp. 1-19; Section 5 is pp. 16-17 and references are pp. 17-19.

Inspection: Date/reviewer: 2026-09-12, assigned MS24 reviewer, with the source assignments and the coordinating agent checks identified below.

The registered artifact and acquisition record retain both dates.

## MS24-U005

Date/reviewer: 2026-09-12, assigned MS24 reviewer, with the source assignments and the coordinating agent checks identified below.
This unit records external inputs and the source's concluding questions, not a new project Claim.
The reviewed MS24 version has printed/PDF pp. 1-19; Section 5 is pp. 16-17 and references are pp. 17-19.

The subsequent user-requested [main-proof dependency review](../../../ledger/Yin_L_F0003_v1.md#ms24-dependency-chain) makes MS24 the principal input for this study.
The table below incorporates its focused checks; the original reading limits remain where a broader theorem was not reopened.
The three supplements give the actual proof evidence rather than a blanket assertion that the upstream bibliography has been audited.

## External Inputs and Actual Review Depth

| Input | Primary evidence and exact scope | Decision and boundary |
| --- | --- | --- |
| Multiplicativity of the ordinary Fuglede-Kadison determinant, including bounded operators with zero determinant | [FK52](../../../literature/pdf/FK52.pdf), Theorem 1 pp. 522-524 and Lemma 5 with the following analytic-extension proof pp. 528-529; [analytic supplement](../FK52/Yin_U001.md#fk52-u001). HS07 Proposition 2.5 was the initial interface. | Selected original bounded proofs now read and reconstructed, with the finite tracial application checked. Main scale removal only needs invertible finite-matrix factors. HS07's unbounded extension is not a premise; its original bounded-theorem delegation is made explicit. |
| Positive capacity iff rank non-decreasing; positive attained minima yield double stochasticity; unique minimizer in the indecomposable case | [Gur04 review](../Gur04/readme.md), Lemma 4.5 and Theorem 4.7; [scaling supplement](Yin_U006.md#ms24-scaling-dependency-review). | Qualitative rank/capacity, strict-positivity attainment and minimizer differentiation independently reconstructed. The main lower bound only needs strictly positive perturbations, so general indecomposable uniqueness is not an added premise. Scalar zero-map boundary retained. |
| Near-minimizer scaling with ds<=6delta | Expanded GGOW Lemma 3.10, journal p. 258/PDF p. 36, quoted as MS24 Proposition 2.10, for positive capacity and c>0 with cap>=exp(-delta) det eta(c)/det c, 0<delta<=1/6; [GGOW20-U003](../GGOW20/Yin_U003.md#ggow20-u003). | Exact interface independently proved in the scaling supplement using capacity duality and x-1-log x. Positive capacity ensures the inverses exist; the exponential bound is retained. No numerical precision or full quantitative continuity theorem is used. |
| Rank/capacity versus full homogeneous free-polynomial matrices | Gur04/GGOW rank and shrunk-subspace interfaces, retained in their respective reviews. | Applied only to square homogeneous linear matrices with the same Kraus coefficients; ordinary commutative determinant nonsingularity is not substituted for free-field fullness. |
| Full linear Haar evaluations and the source's free-field realization | [MSY23 inner-rank unit](../MSY23/Yin_U001.md#msy23-u001), [linear-kernel unit](../MSY23/Yin_U002.md#msy23-u002), and [dual/Haar unit](../MSY23/Yin_U006.md#msy23-u006); [integer supplement](Yin_U004.md#complete-retained-algebra-and-haar-interfaces). | Exact source scope, n=1 and the Haar dual sign checked. The smaller sufficient chain uses bounded duals, finite-rank cycles and the existing linear-kernel proof. Cohn's checked degree-reduction/full-submatrix foundations remain accepted. Semicircular free-field realization is unnecessary for the reconstructed formula and its kernel equivalence. |
| Integer free-group determinant lower bound | [Sch01-U001](../Sch01/Yin_U001.md#sch01-u001) gives the original statement and conventions. The [finite-quotient proof](../Sch01/Yin_U001.md#finite-quotient-determinant-proof) reconstructs the exact injective free-group specialization. | Proof independently reviewed, including finite-matrix kernels and fixed-cutoff limits. Applied to T* T, the original unnormalized integral equals 2m log Delta(T). The broader Sch01 closure theorem and general determinant approximation remain outside this proof. |
| Operator-valued semicircular moment expansion and norm control | Local MS17, Chapter 9, Definition 7/equation (9.16), printed p. 236/PDF p. 245; discussion after equation (9.5), printed p. 231/PDF p. 240. | Directly read and visually checked. The nesting convention is accepted; MS24's pairing induction and resulting moment/norm estimates were reconstructed in U002. This is not a review of the whole book. |
| Covariance-to-distribution continuity cited as BM23/Mai22 in the source lower bound | MS24 p. 13 cites these sources. | Not needed by the retained local reconstruction: a fixed free perturbation gives direct operator norm convergence. Their original statements/proofs were not imported or audited in this task. |
| Minkowski determinant inequality for positive matrices | Named and used in MS24 Proposition 2.9, with its Mir55 locator. | Source-stated external finite-dimensional inequality retained for the stronger cap^(1/m) superadditivity assertion; original Mir55 passage not reviewed. Main determinant proof needs only determinant monotonicity, checked directly in U001. |

HS07's checked author file is [HS07--author.pdf](../../../literature/pdf/HS07--author.pdf), obtained from [the author's primary host](https://web.math.ku.dk/~haagerup/publications/unbounded.pdf).
Its 50-page layout is an undated author version, not the 55-page published pagination.
Definition 2.1 and Proposition 2.5 retain the above author-version locators; the statement check is not transferred to uninspected publication pages.
A former publisher download URL returned 404; the author-hosted primary copy supplied the needed exact interface.
The registered key/metadata remain in the sole bibliography.

The version search and source-comparison scope is limited: the coordinating agent checked the MS24 arXiv entry, while this reviewer checked the user-supplied PDF and the specific external primary passages just listed.
No author-issued MS24 erratum was located in this scoped check, and no claim is made that all subsequent literature has been searched.

## Section 5: Questions Are Not Theorems

Question 1 asks which tuples (x_1,...,x_n) satisfy the following property: for every m and integral matrices a_i, every affiliated-invertible linear matrix X=sum_i a_i tensor x_i has Delta(X)>=1, with normalized trace.
The semicircular example first rescales s_i to e^(1/2)s_i.
The unscaled standard semicircular constant is e^(-1/2), not 1.

Conjecture 1 fixes integral a_i with a rank non-decreasing covariance, substitutes independent GUE matrices X_i^(N), and predicts eventual invertibility and convergence of Delta(sum_i a_i tensor X_i^(N)) to cap(eta)^(1/(2m))e^(-1/2), both in expectation and almost surely.
To reuse its formulation, the GUE normalization must be the variance-1/N convention whose limiting scalar law is the standard semicircle, and “eventual invertibility” must have its probabilistic quantifier made explicit.
The source statement does not supply a proof or a quantitative convergence rate.
This audit checks its formulation and motivation, not its current open/solved status.

The introductory references to sofic groups, Novikov-Shubin invariants and quantitative rank algorithms provide context.
No unreviewed quantitative theorem from those references is silently imported as an MS24 conclusion.

## Relationship to the Repository Questions

For Yin_T_F0001, these units provide a clear connection between algebraic full rank, operator scaling, and finite logarithmic singular-value mass for semicircular linear realizations.
This is potentially useful input when a route already reduces a rational question to a finite matrix pencil.

The implication furnished by the determinant is logarithmic integrability near zero.
A bounded inverse requires a spectral gap at zero; an L2 inverse requires integrability of t^(-2) against the singular-value distribution.
Neither follows from integrability of |log t|.
Already a scalar standard semicircular variable has positive determinant and an unbounded inverse, with infinite inverse L2 norm.
Thus MS24 does not settle the repository's rational L2-to-boundedness target for q-Gaussian, holomorphic R-diagonal or transported tuples.
Any such extension needs a separately stated structural input and proof.

## Retained analytic proof interfaces

The following complete original hermitization and truncated-log reconstructions were retained at 2026-10-21T01:19 from [L_F2](../../../ledger/Yin_L_F0002_v1.md#ms24-analytic-dependencies).
Their reading/check date remains 2026-09-12, including the original rendered MS24 pp. 7,12,14 and the explicitly limited coordinating-agent second check.
The source's ordinary bounded product foundation is now retained at [FK52-U001](../FK52/Yin_U001.md#fk52-u001).
The complete semicircular pairing and faithful norm arguments already have a sufficient home in [MS24-U002](Yin_U002.md#pairing-estimates); they are not duplicated here.
The original U005 source questions and all wider uninspected-proof limits remain unchanged.
This preparation performs no new source or mathematical review.

## Hermitization Does Not Need an Inverse

For \(S\in\mathcal N\), set

\[
H=\begin{pmatrix}0&S\\S^*&0\end{pmatrix}\in M_2(\mathcal N),
\qquad
|H|=\operatorname{diag}\bigl((SS^*)^{1/2},(S^*S)^{1/2}\bigr).
\]

Traciality gives \(\sigma((SS^*)^k)=\sigma((S^*S)^k)\) for all positive integers \(k\).
The two compactly supported spectral probability measures therefore agree, including their mass at zero.
Integrating the logarithm with the normalized block trace yields

\[
\Delta_{\operatorname{tr}_2\otimes\sigma}(H)=\Delta_\sigma(S),
\qquad
\Delta_{\operatorname{tr}_2\otimes\sigma}(H^2)=\Delta_\sigma(S)^2.
\]

The second identity also follows directly from the spectral distribution of \(|H|\).
Both survive zero determinant.
Thus there is no hidden injectivity premise in MS24's reduction to a positive operator.

## Positive Log Semicontinuity

Let \(P_j,P\ge0\) be bounded operators in tracial probability spaces, possibly different ones, such that their scalar moments converge and \(\sup_j\|P_j\|\le K<\infty\).
Enlarge \(K\) to include \(\|P\|\).
Polynomial approximation on \([0,K]\) gives weak convergence of their spectral measures \(\mu_j\) to \(\mu\).
For \(\varepsilon>0\), the function \(g_\varepsilon(t)=\log\max(t,\varepsilon)\) is continuous there and

\[
\limsup_j\int\log t\,d\mu_j(t)
 \le\int g_\varepsilon(t)\,d\mu(t).
\]

Taking the decreasing infimum over \(\varepsilon\downarrow0\) gives

\[
\log\Delta(P)\ge\limsup_j\log\Delta(P_j),
\qquad
\Delta(P)\ge\limsup_j\Delta(P_j).
\]

The conclusion includes \(-\infty\) logarithms and zero atoms.
Consequently, MS24 Proposition 2.4 can be used in this form without the source's restriction to trivial kernels.
The printed bound \(\sup_j\|P_j\|\le\infty\) is not the intended finite bound.
The source's cited kernel-omitting determinant theorem is not needed for this elementary ordinary-determinant argument.

For the upper bound in MS24, apply the result to the **squares** \(H_\delta^2\) of the normalized hermitizations and to the square of a standard semicircular element.
These operators are positive and have uniformly bounded norms.
Applying Proposition 2.4 literally to signed \(H_\delta\), as in the display preceding equation (3.7), would not match its hypotheses.
Squaring yields exactly the same required conclusion \(\limsup_\delta\Delta(H_\delta)\le e^{-1/2}\).

For the lower bound, a fixed perturbation \(S_t=S+\sqrt t\,B\) gives norm convergence directly, hence norm convergence of the positive squares of the hermitizations.
No continuity modulus for covariance maps is consumed.
Neither use requires uniform control of negative moments or uniform integrability of \(|\log t|\); only this one-sided semicontinuity is asserted.
