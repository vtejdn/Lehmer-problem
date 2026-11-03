---
author: Yin
---

<a id="msy23-u005"></a>
# MSY23-U005: Rational Matrices, Atoms, and Central Eigenvalues

- Source: [MSY23.pdf](../../../literature/pdf/MSY23.pdf), the 50-page published version registered as MSY23.
- Locators: Corollaries 5.12-5.13, pp. 34-35; Section 5.2, pp. 35-39; Section 5.3, pp. 39-41; Definition 5.22 and Theorem 5.23, pp. 41-42.
- Record: 2026-09-08, the original unit authoring agent, for the [MSY23 source audit](readme.md).
- Kind: source statements and reconstructed proofs.
The unbounded-domain gap in Lemma 5.19 is repaired below.
These are repairs to the source proof, not a new project conjecture or a novelty claim.

## Setting and dependencies

Let `(M,tau)` be finite tracial with faithful normal normalized trace, let `A=U(M)` be its algebra of affiliated operators, and let `X=(X_1,...,X_n)` be a bounded tuple with `Delta(X)=n`.
Neither normality nor selfadjointness of the tuple is assumed unless specified.
Let `F` be the free skew field on the listed variables.
[U004](Yin_U004.md#msy23-u004) supplies the injective evaluation homomorphism `F -> A` and rank preservation.
[U001](Yin_U001.md#msy23-u001) supplies the algebraic inner rank, central eigenvalues, and the linear-matrix facts used in Section 5.3.

For `T in M_N(A)` use the unnormalized analytic rank

\[
\operatorname{rk}(T)
 =N-(\operatorname{Tr}_N\otimes\tau)(p_{\ker T}).
\]

The probability distribution of a normal matrix-affiliated operator instead uses the normalized trace `tr_N tensor tau`.
These two normalizations must not be interchanged.
Matrix sums, products, and inverses in A mean the affiliated-algebra operations, with their canonical closed realizations.

## Rational functions and matrix ranks

Corollary 5.12 states that every nonzero `r in F` has an affiliated evaluation which is nonzero, invertible in A, and has no left or right zero divisors.
For every `P in M_N(F)`,

\[
\operatorname{rk}(P(X))=\rho_F(P).
\tag{1}
\]

To verify the matrix extension, diagonalize P over the division ring F: if `rho_F(P)=k`, invertible matrices U,V over F give `UPV=diag(I_k,0)`.
All their entries evaluate by U004, and the evaluated U,V stay invertible because their inverse identities evaluate.
Analytic rank is invariant under these affiliated invertible factors.
Thus (1) follows from the rank of the diagonal matrix.
This argument requires the full field homomorphism available under `Delta(X)=n`; it is not an arbitrary-tuple substitution in a rank factorization with potentially undefined denominators.

For Corollary 5.13 additionally assume that all `X_j` are selfadjoint and `r=r*` is a nonconstant element of F with its formal involution.
The involution-preserving evaluation from U004 makes `r(X)` selfadjoint affiliated.
An atom at a real number lambda would give the nonzero spectral projection

\[
p=1_{\{\lambda\}}(r(X)),\qquad (r(X)-\lambda)p=0.
\]

Since `r-lambda` is a nonzero element of F, Corollary 5.12 contradicts this equation.
No boundedness of `r(X)` is used.
The source's spectral-projection subscript `r(x)` on p. 35 is read as `r(X)`.

## Point spectrum and exact atomic masses

For an affiliated matrix T, finite traciality gives

\[
\sigma_p(T)
 =\{\lambda:\operatorname{rk}(T-\lambda I_N)<N\}
 =\{\lambda:T-\lambda I_N\text{ is not invertible in }M_N(A)\}.
\tag{2}
\]

The last set is the source's `sigma_A(T)`.
It is not the ordinary spectrum defined by failure of a **bounded** inverse.
For example, a semicircular operator has no eigenvalues, so its affiliated spectrum in this sense is empty, while its ordinary bounded spectrum is an interval.

Theorem 5.14 follows by applying (1) to `P-lambda I_N` for each scalar lambda:

\[
\rho_F(P-\lambda I_N)
 =\operatorname{rk}(P(X)-\lambda I_N),
\qquad
\sigma^{\rm full}(P)=\sigma_p(P(X)).
\tag{3}
\]

Here `sigma^full(P)` consists of scalar lambda for which `P-lambda I_N` is not full over F.
The term central eigenvalue refers to the scalar coefficient field, not to the center of M.
The theorem does not require `P(X)` to be normal.

The preliminary arbitrary-domain aside on p. 36 requires a separate argument: a free-field rank factorization cannot simply be substituted at a tuple where its new denominators may be undefined.
The [U004 supplement](Yin_U004.md#supplement-for-the-arbitrary-domain-aside-on-p-36) repairs the analytic rank bound by polynomial block linearization, and proves the stronger affiliated inner-rank bound with an explicit finite-von-Neumann projection-comparison input.
Neither repair is needed for (3), where the full field homomorphism is already available.

When `T=P(X)` is normal, its spectral measure satisfies

\[
\mu_T(\{\lambda\})
 =\frac1N(\operatorname{Tr}_N\otimes\tau)(p_{\ker(T-\lambda I_N)})
 =\frac{N-\rho_F(P-\lambda I_N)}{N}.
\tag{4}
\]

This reconstructs Corollary 5.15: atoms occur exactly at the central eigenvalues, and each positive atom has weight at least `1/N`.
Normality is essential for interpreting the kernel projections as a probability spectral measure; it is unnecessary for the rank identities.

Remark 5.16 assumes further that T is selfadjoint and bounded.
The one-variable free-entropy-dimension formula then gives

\[
\delta^*(T)
 =1-\frac1{N^2}\sum_{\lambda\in\sigma^{\rm full}(P)}
       \bigl(N-\rho_F(P-\lambda I_N)\bigr)^2
 \in\{k/N^2:0\le k\le N^2\}.
\]

The dimension formula is an imported entropy interface described in [U006](Yin_U006.md#msy23-u006); the finite matrix-trace calculation here is direct.
This statement does not assign entropy to arbitrary unbounded normal rational functions.

## Lemma 5.19: a necessary domain repair

The source proves that for a closed densely defined affiliated operator T and distinct eigenvalues `lambda_1,...,lambda_k`, with eigenprojections `p_1,...,p_k`,

\[
\sum_{j=1}^k\tau(p_j)=\tau\!\left(\bigvee_{j=1}^kp_j\right).
\tag{5}
\]

**Problem in the printed proof, p. 38.**
It chooses a norm-convergent sequence of finite sums of eigenvectors and passes T through that limit.
Closedness alone does not imply convergence of the images; graph convergence or another argument is needed.
The bar over the sum of eigenspaces and the unbounded-operator passage were checked in the rendered published page.
The printed inference is unsupported as written.

**Repair by a bounded row operator.**
Set `H=L2(M,tau)`, `p=diag(p_1,...,p_k)`, and

\[
B=(p_1\ \cdots\ p_k):H^k\longrightarrow H.
\]

This is a bounded matrix over M.
Its restriction to `pH^k` is injective.
Indeed, suppose `eta_j in p_jH` and `sum_j eta_j=0`.
Each eigenvector is in every power domain of T.
Applying `T^m` to this finite sum, for `m=0,...,k-1`, gives

\[
\sum_{j=1}^k\lambda_j^m\eta_j=0.
\]

The scalar Vandermonde matrix is invertible because the eigenvalues are distinct.
Hence every eta_j is zero.
No limit is passed through an unbounded operator.

Since B vanishes on `(I-p)H^k`, its kernel is exactly `(I-p)H^k`.
Its initial support in the polar decomposition is therefore p, and its final support is the projection onto the closure of `sum_j p_jH`, namely `bigvee_j p_j`.
For its rectangular partial isometry v, traciality gives

\[
\tau(vv^*)=(\operatorname{Tr}_k\otimes\tau)(v^*v)
 =\sum_j\tau(p_j).
\]

This proves (5).
Standard polar decomposition in a finite von Neumann algebra is the only structural input.
In particular, the proof requires neither orthogonality of the eigenspaces nor closedness of their algebraic sum, and it does not import the source's projection-join reference.

For Proposition 5.18 apply (5) in `M_N(M)` with its normalized trace.
By (3), each eigenprojection of `P(X)` has trace at least `1/N`.
Any k distinct eigenvalues therefore satisfy `k/N <= 1`, proving `k<=N`.
This also proves Proposition 5.17's purely algebraic bound: choose a semicircular model realizing F, apply (3), and transfer the bound back to the central eigenvalues of P.
The existence of that model is supplied by the elementary semicircular dual and the audited free-field theorem, without the separate Cohn proposition quoted in the source.

**Notation repair, p. 39.**
The sentence asserting an integer strictly below N must use `rho(P-lambda I_N)`, not the printed `rho(P)`.
The surrounding displayed equality already uses the correct shifted matrix.
The conclusion is unchanged after correction.

<a id="lemma-519-counterexample-2026-09-11"></a>
### Follow-up: explicit counterexample to the limit passage, 2026-09-11

At the user's request, the coordinating agent reread published pp. 37-38 in extracted text and rendered pages, and p. 28 for the precise polar-decomposition and kernel-projection inputs.
The standalone note now gives a concrete counterexample to the p. 38 inference and a complete presentation of the bounded-row repair above.
The original source assessment and its independent review are preserved; the new example and presentation received coordinating-agent self-review only.

Let `M=L^infinity((0,1);M_3(C))` with `tau=(1/3) integral Tr_3`, acting by left multiplication on `H=L^2(M,tau)`.
Define the maximal multiplication operator

\[
T\xi(t)=\bigl(t^{-1}e_{12}+e_{22}+2e_{33}\bigr)\xi(t),
\qquad
\operatorname{Dom}T=\{\xi\in H:t^{-1}e_{12}\xi\in H\}.
\]

It is closed: the singular multiplication term is closed by an almost-everywhere subsequence argument, and the remaining multiplier is bounded.
Its domain is dense because it contains every central-cutoff range `1_[1/m,1) H`.
These cutoffs also verify affiliation: `T c_m` is in M, so commutation with a commutant unitary holds on each cutoff range; graph convergence and closedness then extend it to the full domain.
Its distinct eigenvalues include 0, 1 and 2.

Put `f_n=sqrt(3n) 1_(0,1/n)`, `u_n=-f_n e_11`, and `v_n=f_n(e_11+t e_21)`.
Then `T u_n=0`, `T v_n=v_n`, and

\[
s_n=u_n+v_n=tf_ne_{21}\longrightarrow0,
\qquad Ts_n=v_n,
\qquad
\|s_n\|_2^2=\frac{1}{3n^2},\quad
\|Ts_n\|_2^2=1+\frac{1}{3n^2}.
\]

Thus `T(lim s_n)=0`, but `lim T s_n` does not exist in Hilbert-space norm.
The additional printed premise that the limit lies in a third eigenspace is satisfied: zero belongs to `ker(T-2)`.
This refutes the inference used by the proof, **not Lemma 5.19's trace identity**.
In this example the orthogonal eigenprojections are `e_11`, the projection onto the pointwise vector `(1,t,0)`, and `e_33`; each has trace 1/3 and their join is 1.
The two-eigenspace algebraic sum is not closed: `1_[1/m,1)e_21` is a sum of 0- and 1-eigenvectors and converges to `e_21`, which is outside the operator domain.

The note's repaired proof uses the already audited bounded row `B=(p_1,...,p_k)`.
Polynomial interpolation on the finite algebraic sum replaces the Vandermonde calculation; both establish the same kernel identity without taking an unbounded-operator limit.
The polar-decomposition input is now cited directly to **MSY23 Lemma 5.1, p. 28**, applied to a square block amplification of B.
The final trace equality is expanded entry by entry, so no matrix-trace normalization is implicit.
No new reusable project Claim, lemma Role, theorem designation or mathematical priority claim is introduced.

Source-search boundary: the existing audit already supplied the repair.
A bounded external search for the published title, lemma and corrections confirmed the [publisher identity](https://www.sciencedirect.com/science/article/pii/S0022123623001738) and the distinct [1905.08187 preprint record](https://arxiv.org/abs/1905.08187); it supplied no additional repair used here.
The earlier 1805.04150 work returned by a number-only search is not the target version.
No exhaustive errata or priority search is claimed.
The note's record owns its whole-document citation check and build evidence.

## Linear matrices and the scope of regularity

Section 5.3 compares a matrix-valued semicircular Dyson-equation setting with the weaker hypotheses needed only for atom statements.
For selfadjoint coefficient matrices `b_j`, its completely positive self-energy map is

\[
L(b)=\sum_{j=1}^n b_j b b_j.
\]

If `L(b)>=c tr_N(b) I_N` for positive b and some `c>0`, then `L(b)` has full rank whenever b is nonzero positive.
In particular L is nowhere rank-decreasing.
The algebraic criterion in U001 makes `sum b_j x_j` full; adding a constant matrix preserves fullness by the linear-matrix result there.
This is Remark 5.20's one-way implication.

The converse fails in the source's checked two-by-two example:

\[
P=\begin{pmatrix}0&x_1\\x_1&x_2\end{pmatrix},\quad
P^{-1}=\begin{pmatrix}-x_1^{-1}x_2x_1^{-1}&x_1^{-1}\\x_1^{-1}&0\end{pmatrix}.
\]

Both products with the displayed inverse equal the identity by direct multiplication over F.
Thus P is full.
But `L(diag(1,0))=diag(0,1)`, which cannot dominate `c I_2/2`.
This verifies the strictness without relying on a random-matrix simulation or a Dyson-equation theorem.

Theorem 5.21 lets the original tuple be arbitrary with `Delta(X)=n`, and requires only that the evaluated linear matrix

\[
T=b_0+\sum_j b_jX_j
\]

be normal.
Formula (4) still applies.
Additionally, atoms can occur only at eigenvalues of the scalar matrix `b_0`; and if the homogeneous part is full, there are no atoms.
The first inclusion is also immediate algebraically: when `b_0-lambda I_N` is invertible, scalar evaluation at `x=0` proves `P-lambda I_N` full.
The second assertion uses fullness of the homogeneous part under addition of any constant matrix, from U001.

These are statements about atoms.
Neither atomlessness nor affiliated invertibility proves a bounded inverse, absolute continuity, analytic density, or equality of Brown support with ordinary spectrum.
The Dyson-equation literature in the introduction of Section 5.3 is contextual; its stronger analytic regularity results are not consumed by this proof.

Definition 5.22 and Theorem 5.23, pp. 41-42, record the strong Atiyah property: the unnormalized analytic rank of every polynomial matrix is a nonnegative integer.
Equation (1) proves it under maximal Delta.
The weaker property and its converse characterization are treated in U006.

## External comparison and verification boundary

The claim about CS16 (Charlesworth-Shlyakhtenko), Conjecture 5(b), was checked against their [public arXiv v2](https://arxiv.org/pdf/1408.0580v2), p. 4: the requested normalized atom lattice for selfadjoint polynomial matrices is exactly supplied by (4).
The older preprint title is *Regularity of Polynomials in Free Variables*; the [author publication page](https://www.ilcharle.com/papers.php) and [publisher record](https://www.sciencedirect.com/science/article/pii/S0022123616300830) identify the published 2016 title cited by MSY23.
This is a statement comparison, not an audit of the older paper or its other conjectures.

The [SS15 (Shlyakhtenko-Skoufranis) preprint](https://arxiv.org/pdf/1305.1920v1), Theorem 3.4, p. 8, confirms the prior atom-lattice theorem for normal freely independent variables and their generated star algebra.
Its all-page proof is not an input here.
Source references [2], [3], and [21] describe the contextual Dyson/random-matrix regularity theory; no such theorem is assumed in the above reconstruction.

All assigned text on published pp. 34-42 was read, together with the relevant bibliography on pp. 49-50.
Published pp. 36, 38 and 39 were visually inspected for the spectral formulas and the two identified proof/notation issues; other selected pages were checked elsewhere in this source audit.
The polar/Vandermonde repair, inverse example, rank normalization, and implication boundaries were reconstructed directly.
Independent cross-review is recorded separately when completed.
No formal verification, numerical certificate, author-confirmed erratum, or full recursive audit of the cited literature is claimed.

Independent review, 2026-09-08, a separate reviewing agent: compared the unit with the published pp. 34-42 and recomputed the decisive steps.
The row operator in the Lemma 5.19 repair has kernel exactly the complement of the diagonal eigenprojection, because powers are applied only to finite sums of genuine eigenvectors; its rectangular polar factor gives the stated trace identity even when the eigenspace sum is not closed.
The nonnormal point-spectrum bound therefore does not assume orthogonality.
The normalized atom formula has the required factor 1/N, and the entropy formula consequently has 1/N^2.
Both ordered products in the two-by-two inverse example were checked.
The p. 39 missing shift and Theorem 5.21's constant-term/full homogeneous-part implications match the source after the recorded correction.
The unrelated arbitrary-domain aside on p. 36 requires the separate supplement in [U004](Yin_U004.md#msy23-u004); the main maximal-Delta spectral theorem already follows from the audited full-field rank equality.
No further substantive mismatch was found in this unit's reconstructed conclusions.

## Source and inspection

Source edition: MSY23 / MSY23, the user-supplied 50-page published article in Journal of Functional Analysis 285 (2023), article 110016, DOI 10.1016/j.jfa.2023.110016. Printed pages equal PDF pages. The separate 37-page arXiv v2 was not compared in full; other works retain their own versions and inspection limits in the body.

Passages: Corollaries 5.12-5.13, published pp. 34-35; Section 5.2, pp. 35-39; Section 5.3, pp. 39-41; Definition 5.22 and Theorem 5.23, pp. 41-42. The 2026-09-11 follow-up rechecks the p. 38 limit inference and p. 28 operator inputs.

Inspection: 2026-09-08: assigned pages and references pp. 49-50 read, local spectral proofs and the Lemma 5.19 domain repair independently reviewed. The 2026-09-11 counterexample and new presentation received coordinating-agent self-review only; they challenge the source's limit inference, not its repaired trace identity. CS16 and SS15 remain selected statement comparisons, not whole-source proof audits; other spectral context is not silently accepted as a premise. No author-confirmed erratum, exhaustive errata/priority search, numerical certificate or formal verification.
