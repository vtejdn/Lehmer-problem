---
author: Yin
---

# Matrix/corner rational L2 transfer; rational-rate free Poisson families

## Current assessment
[Selected decision](#decision-isolated-whole-review-2026-10-22)

## Matrix Rational Models and the L2 Resolvent Criterion

<a id="yin_c_f0001"></a>
Date: 2026-09-11.
Author: another AI agent.
Goal: Yin_T_F0004.
Strategy: Yin_S_F0014.
Initial mathematical assessment: complete proof draft, awaiting independent review.
The [selected assessment](#decision-isolated-whole-review-2026-10-22) records the current mathematical and review assessment; the candidate decision retains its historical scope.

This record extends the scalar rational-image observation to finite matrices and corners.
The reuse search checked Yin_C_F0015, Yin_C_F0017, the Miy26 rational-L2 audit, existing rational-coordinate transfers and the local NS06 cumulant/compression chapters before the proof below.
No existing claim was found with this matrix transfer statement.
The square-integrable rational boundedness input remains Miy26; ordinary finite division-ring elimination is written out to identify the ambient inverse precisely.

## Statement

Let \((\mathcal N,\tau)\) be a finite faithful tracial von Neumann algebra and let \(F\subseteq L^0(\mathcal N)\) be a unital division subring containing \(\mathbb C\), with the property

\[
F\cap L^2(\mathcal N,\tau)\subseteq\mathcal N.
\tag{1}
\]

Fix \(m\ge1\), and let \(e\in M_m(F)\cap M_m(\mathcal N)\) be a nonzero orthogonal projection.
Equip \(eM_m(\mathcal N)e\) with its normalized corner trace.
Let \(X_1,\ldots,X_d\) be any bounded elements of \(eM_m(F)e\), put \(\mathcal M=W^*(e,X_1,\ldots,X_d)\subseteq eM_m(\mathcal N)e\), and define the unital polynomial algebra \(\mathcal A_X=\mathbb C\langle X_1,\ldots,X_d\rangle\), with unit \(e\).
Then

\[
\boxed{\quad
\operatorname{Div}_{L^0(\mathcal M)}\mathcal A_X
\cap L^2(\mathcal M)
\subseteq\mathcal M.
\quad}
\tag{2}
\]

For every \(f\) in that affiliated division closure and every \(\lambda\in\mathbb C\), the resulting pointwise criterion is

\[
\lambda\notin\sigma(f)
\quad\Longleftrightarrow\quad
f-\lambda e\text{ has an affiliated inverse belonging to }L^2(\mathcal M).
\tag{3}
\]

For an unbounded \(f\), the spectrum in (3) is the usual spectrum of its canonical closed affiliated realization: the inverse must be bounded and everywhere defined.
This convention agrees with the spectrum in \(\mathcal M\) when \(f\) is bounded.
The statement does not assert that every nonzero \(f-\lambda e\) has an affiliated inverse.

In particular, (2)-(3) hold for every tuple of bounded matrix rational expressions, or their rational projection corners, in a finite semicircular family.
They also hold for every finite freely independent free-Poisson family with positive rational rates and arbitrary fixed positive jump sizes.
Arbitrary positive **irrational** rates are not claimed here.

<a id="yin_c_f0001-proof"></a>
## Proof

**Matrix inverse closure.**
Put \(R=L^0(\mathcal N)\).
If \(A\in M_m(F)\), elimination over the division ring \(F\) gives invertible \(P,Q\in M_m(F)\) such that

\[
PAQ=\operatorname{diag}(I_r,0)
\]

for some \(r\le m\).
The embedding into \(M_m(R)\) preserves \(P^{-1}\) and \(Q^{-1}\).
If \(A\) is invertible in \(M_m(R)\), then \(r=m\): otherwise the displayed diagonal matrix kills a nonzero standard column, contradicting invertibility.
For \(r=m\) the same equation supplies \(A^{-1}=QP\in M_m(F)\).
Thus \(M_m(F)\) is inverse closed relative to \(M_m(R)\).
It need not itself be a division ring when \(m>1\).

For the corner, let \(a\in eM_m(F)e\) have an inverse \(b\) in \(eM_m(R)e\), where inverses are taken relative to \(e\).
Then

\[
(a+1-e)^{-1}=b+1-e.
\]

Matrix inverse closure gives \(b=(a+1-e)^{-1}-(1-e)\in eM_m(F)e\).
Hence this corner is inverse closed inside the corresponding affiliated corner as well.

**Inclusion and L2 boundedness.**
The canonical trace-preserving inclusion of \(\mathcal M\) into the ambient corner extends to its affiliated algebra, with closed products and inverses preserved.
Minimality of division closure and the preceding inverse-closure argument give

\[
\operatorname{Div}_{L^0(\mathcal M)}\mathcal A_X
\subseteq eM_m(F)e.
\tag{4}
\]

Use the standard identification \(L^0(M_m(\mathcal N))=M_m(L^0(\mathcal N))\).
For \(z=(z_{ab})\), the corresponding Hilbert-space identity is

\[
\|z\|_{2,\operatorname{tr}_m\otimes\tau}^2
=\frac1m\sum_{a,b=1}^m\|z_{ab}\|_{2,\tau}^2.
\tag{5}
\]

Passing between this trace and the normalized corner trace only multiplies squared norms by the fixed positive number \((\operatorname{tr}_m\otimes\tau)(e)^{-1}\).
Therefore a square-integrable element in (4) has all its entries in \(F\cap L^2(\mathcal N)\).
By (1) every entry is bounded, so the finite matrix is bounded.
As it is affiliated with \(\mathcal M\), its bounded representative belongs to \(\mathcal M\).
This proves (2).

If an affiliated inverse \((f-\lambda e)^{-1}\) exists, it belongs to the same division closure by definition.
An L2 inverse is therefore bounded by (2), and is the everywhere defined inverse of the closed realization.
Conversely a resolvent inverse is bounded, affiliated with \(\mathcal M\), and hence in \(\mathcal M\subseteq L^2(\mathcal M)\).
This proves (3).

**Semicircular and free-Poisson models.**
For a finite semicircular family \(S\), use

\[
F=\operatorname{Div}_{L^0(W^*(S))}\mathbb C\langle S\rangle.
\]

The already audited free-field theorem makes \(F\) a division ring, and [Miy26-U002](../audits/literature/Miy26/Yin_U002.md#miy26-u002) supplies (1).
This proves the matrix-rational application, including \(e=I_m\).
The affiliated matrix and L2 identifications in (5) are the usual finite-amplification identities; they impose no hypothesis about boundedness of inverses in a linear representation.

For rates \(\lambda_j=n_j/m>0\), use the exact [NS06 finite rectangular circular model](../audits/literature/NS06/Yin_U002.md#ns06-matrix-models): with one free circular family of entries and \(C_j\in M_{m,n_j}(\mathcal N)\), the matrices

\[
Y_j=m^{-1}C_jC_j^*
\]

are freely independent free Poisson elements with rates \(\lambda_j\) and jump one.
All entries are polynomials in finitely many semicircular coordinates, so \(Y_j\in M_m(F)\cap M_m(\mathcal N)\).
Any finite list of positive rational rates has a common denominator \(m\).
Multiplication by fixed positive jump sizes leaves these entries polynomial, so (2)-(3) apply.
A free-Poisson family in any other faithful tracial realization has the same joint star-law; the standard trace-preserving generated-von-Neumann-algebra identification carries boundedness, affiliated rational evaluation, L2 membership and spectra to that realization.
This proves the last assertion.
QED.

<a id="yin_c_f0001-review"></a>
## Checks and limitations

The author's checks include matrix inverse orientation \(A^{-1}=QP\), a singular matrix (which cannot be inverted in the larger ring), the unit in the corner formula, the normalized trace in (5), and the necessity of requiring an **existing** affiliated inverse in (3).
The circular entry calculation yields \(\tau_m(Y_j)=n_j/m\) and \(\kappa_2(Y_j)=n_j/m\), agreeing with jump-one Poisson normalization.
Its joint entry cumulants were matched against NS06 Theorem 14.18, so freeness is not inferred merely from separate marginal distributions.
A separate proof review remains pending.

The target algebra in (2) can have zero divisors, including the kernels of free-Poisson variables with rates below one.
It is not identified with a free field.
Nor does the argument prove

\[
\operatorname{Div}_{L^0(\mathcal M)}\mathcal A_X\cap\mathcal M
=\operatorname{Div}_{\mathcal M}\mathcal A_X.
\]

Entrywise boundedness of a rational affiliated operator does not reconstruct bounded scalar inverses in the smaller coordinates.
This distinction is essential for the separate bounded-closure goal.
No arbitrary-rate limit, multivariate free-Meixner theorem, general q-Gaussian rational boundedness theorem or matrix-valued version of Miy26's creation-spectrum identity is asserted.

<a id="yin_c_f0001-continuation"></a>
## Continuation beyond finite rational matrix models

At the initial Yin_C_F0001 checkpoint, a finite Jacobi or free-Charlier approach remained a candidate for arbitrary real Poisson parameters.
The proposed Fock model \(X_i=\ell_i+\ell_i^*+a_i\ell_i\ell_i^*\) suggested \([r_i^*,X_j]=\delta_{ij}P_\Omega(1+a_i r_i^*)\), and \(D_i=r_i^*(1+a_i r_i^*)^{-1}\) was bounded only for \(|a_i|<1\).
The generalized orthogonal-Wick residual identity and homogeneous norm estimate were then outstanding.
This initial discovery is retained as provenance, not the current unresolved status.

The subsequent arbitrary-real-rate proof supplies both identities, uses Yin_C_F0034 directly with bounded right annihilation instead of normalized duals, and obtains the full all-rational L2 criterion for **all positive real rates**.
Its proof and review assessment are separate from Yin_C_F0001.
In particular, Yin_C_F0001's finite matrix argument itself has not been retroactively relabeled as an arbitrary-rate approximation theorem.

The discovery search included the existing Ans07 lead on resolvent generating functions, local NS06 free-Poisson/compression/cumulant chapters, and primary-source queries for free-Meixner finite-rank or Haagerup structures.
No checked external theorem establishing the missing arbitrary-rate multivariable residual/boundedness assertion was found in that search.
The finite matrix result above resolves a concrete subclass without claiming that rational approximation closes the remaining gap.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:54 |
| status | proved |
| reason | Adopt the exact actual original finding at its complete reviewed scope while preserving the mathematical assessment, fixed argument, dependencies and historical decisions. The original initial context-isolation fact remains unknown; no new or redated review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0001-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0009_v1.md#matrix-and-corner-inverses) | Actual original complete C_F0001 finding at its disclosed accepted-input scope and unknown initial-context relationship; historical source precision and limits remain at this retained original finding. |


### Decision isolated-whole-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:21 |
| status | proved |
| reason | Adopt the actual new isolated whole-proof finding for the unchanged fixed statement and selected argument; retain all original assessments, source depths and useful negative boundaries at their historical scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0001-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New whole-proof finding](../audits/reviews/Yin_R_F0009_v1.md#fresh-c44-whole) | Actual isolated whole-proof inspection at this exact fixed input, including all necessary accepted-input applicability and stated limits; historical findings remain separately unknown. |

## Historical assessments


<a id="decision-candidate-0002"></a>
### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0001-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0009_v1.md#matrix-and-corner-inverses) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).



These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0009_v1.md#matrix-and-corner-inverses).

Material covered by that review: [Exact material](Yin_C_F0001_v1.md).
