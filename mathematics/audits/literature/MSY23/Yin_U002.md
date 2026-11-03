---
author: Yin
---

<a id="msy23-u002"></a>
# MSY23-U002: Delta and Kernels of Full Linear Matrices

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

- Source: [MSY23, supplied as MSY23.pdf](../../../literature/pdf/MSY23.pdf), all of Section 3, printed pp. 12-20.
Page 20's opening of Section 4 is handed to U003.
- Record: 2026-09-08, the unit authoring agent, for [MSY23 free-field and Atiyah source audit](readme.md#msy23-free-field-and-atiyah-source-audit).
- Reading and review: every page read; Theorem 3.1 and Lemmas 3.3-3.5 reconstructed with complex coefficients, transpose conventions, both kernel directions, and all induction cases.
The preceding algebra interfaces are checked in [U001](Yin_U001.md#msy23-u001).
- Result: the Section 3 equivalence passes.
The final sentence on p. 20 abbreviates an adjoint-kernel argument that is made explicit below.
It does not require selfadjoint generators.

## Setting, Delta, and the Three Conditions

The source works in a finite tracial von Neumann algebra with a faithful normal tracial state and bounded X_1,...,X_n.
Neither normality nor selfadjointness of X is assumed, and no hypothesis M=W*(X) is needed in this section.

The source defines Delta from the von Neumann dimension of the Hilbert-Schmidt closure of finite-rank cycles

\[
\sum_k[T_k,JX_k^*J]=0.
\]

For the maximality question only, Delta(X)=n is equivalent to the absence of nonzero finite-rank cycles.
The Hilbert-Schmidt closure is a submodule of the finite standard module: dimension zero means its projection has faithful trace zero, hence the submodule is zero.
It is not necessary to compute any nonzero value of Delta here.
Taking adjoints and conjugating by J changes a right-multiplication cycle into

\[
\sum_k[JT_k^*J,X_k]=0.
\]

This is an involutive correspondence preserving finite rank and nontriviality.
Thus maximality can equivalently be tested with left X_k commutators, as in the subsequent lemmas.
This checks Remark 3.2(i) including its direction and signs.

For a formal polynomial matrix, star conjugates coefficients, reverses words, and transposes the matrix while fixing the formal variables.
Therefore A(X)*=A*(X*) for arbitrary X.
The distinction between X and X* is retained throughout the proof; Remark 3.2(ii) does not assert A(X)*=A*(X).

Theorem 3.1 equates:

1. Delta(X)=n.
2. A linear square formal matrix A must be zero whenever A(X) and A(X)* have kernel vectors f and e respectively, each of whose components is complex-linearly independent.
3. Every full linear square formal matrix A evaluates to an operator with zero kernel.

Zero kernel is not yet bounded invertibility.
In the finite affiliated algebra it will imply affiliated invertibility, an interface consumed later in Section 5.

## Lemma 3.3: Finite Trace and the Adjoint Kernel

For a bounded operator T in a finite von Neumann algebra, write T=v|T|.
Its support projections are v*v=1-p_ker(T) and vv*=1-p_ker(T*).
The trace takes the same value on v*v and vv*, so it gives equal values to the kernel projections.
Faithfulness then implies that one kernel is nonzero if and only if the other is nonzero.
The projections belong to the algebra by spectral calculus.
Apply this to M_N(M) with its finite matrix trace whenever a square matrix is involved.
Normalizing that matrix trace is unnecessary for the equality.

This proves the complete kernel implication used here without imposing normality of T.
It does not provide a bounded inverse from injectivity.

## Lemma 3.4: From Two Kernel Vectors to a Finite-Rank Cycle

This section of the source uses the inner product linear in its first variable, as witnessed by the linear operator xi mapped to <xi,e>f.
All calculations in this unit retain that convention.
This differs from the project Yin_C_F0002 convention but describes the same rank-one operators after conjugating the notation appropriately.

Write A=A^(0)+sum_k A^(k)x_k.
For f in ker A(X) and e in ker A(X)*, define

\[
T_k=\sum_{i,j}A^{(k)}_{ij}\langle\,\cdot,e_i\rangle f_j,
\qquad k=0,\ldots,n.
\]

The i-th row of A(X)f=0, multiplied by the functional <.,e_i> and summed over i, gives

\[
T_0+\sum_k X_kT_k=0.
\]

The i-th row of A(X)*e=0 is

\[
\sum_j\overline{A^{(0)}_{ji}}e_j+
\sum_{k,j}\overline{A^{(k)}_{ji}}X_k^*e_j=0.
\]

Putting that vector in the conjugate-linear second slot of <.,.>, multiplying by f_i, and summing over i removes the coefficient conjugates and gives

\[
T_0+\sum_k T_kX_k=0.
\]

Subtracting proves sum_k[T_k,X_k]=0.
The overbars and transpose in the adjoint equation are present in the rendered source p. 15; they can be lost in plain text extraction.
No independence or orthogonality of e,f is needed in this lemma itself.

## Lemma 3.5: From a Finite-Rank Cycle to a Linear Matrix

Suppose sum_k[T_k,X_k]=0.
If every T_k is zero, there is nothing to construct for the later maximality argument.
Otherwise let f_1,...,f_N be an orthonormal basis of

\[
V=\sum_k(\operatorname{Ran}T_k+\operatorname{Ran}T_k^*).
\]

If Q is the projection onto V, then T_k=QT_kQ.
Hence write

\[
T_k=\sum_{i,j} A^{(k)}_{ij}\langle\,\cdot,f_i\rangle f_j,
\qquad B^{(k)}_{ij}=\langle X_k f_i,f_j\rangle.
\]

The coefficient matrix A^(k) is the transpose of the usual column-coordinate matrix of T_k|_V; B^(k) is likewise the transpose of the usual matrix of QX_k|_V.
This is a transpose, not an adjoint, and is the reason the products below have their printed order.

Apply the commutator relation to f_p.
Since the family is orthonormal,

\[
\sum_{k,j}(B^{(k)}A^{(k)})_{pj}f_j
=\sum_{k,j}A^{(k)}_{pj}X_k f_j.
\tag{1}
\]

Define C=sum_k B^(k)A^(k).
Taking the inner product of (1) with f_q yields

\[
C_{pq}=\sum_{k,j}A^{(k)}_{pj}B^{(k)}_{jq},
\qquad C=\sum_k B^{(k)}A^{(k)}=\sum_k A^{(k)}B^{(k)}.
\tag{2}
\]

Thus the linear formal matrix

\[
A=C-\sum_k A^{(k)}x_k
\]

satisfies A(X)f=0.

For the second kernel, take adjoints of the commutator relation, obtaining sum_k X_k*T_k*=sum_k T_k*X_k*.
Since

\[
T_k^*=\sum_{i,j}\overline{A^{(k)}_{ij}}
\langle\,\cdot,f_j\rangle f_i,
\]

its evaluation at f_l gives

\[
\sum_{k,i}\overline{A^{(k)}_{il}}X_k^*f_i
=\sum_{k,i,j}\overline{A^{(k)}_{ij}B^{(k)}_{jl}}f_i
=\sum_i\overline{C_{il}}f_i.
\]

The last equality uses the second expression for C in (2).
This is exactly A(X)*f=0.
Local render p. 17 confirms the conjugation of the whole coefficient product.
The subspace V need not be invariant under X_k; only the T_k support condition was used.

## Theorem 3.1: All Four Implications Reconstructed

### (i) implies (ii)

Construct the T_k from Lemma 3.4.
Maximal Delta implies T_k=0 for k>=1.
Let

\[
E_{pi}=\langle e_p,e_i\rangle,
\qquad F_{jq}=\langle f_j,f_q\rangle.
\]

The matrix coefficient <T_k e_p,f_q> is precisely (E A^(k) F)_{pq}.
Both Gram matrices are invertible because both component families are independent.
For complex vectors this formula needs neither an additional transpose nor an omitted conjugate: it follows directly from the first-slot-linear convention.
Consequently A^(k)=0 for k>=1.
The remaining equation A^(0)f=0 and independence of the f_j force A^(0)=0.
Thus A=0.

### (ii) implies (i)

Given a nonzero finite-rank cycle, Lemma 3.5 produces one orthonormal component family f that belongs to both kernels of the constructed A(X) and A(X)*.
Condition (ii) forces that formal A to be zero, so each coefficient A^(k) vanishes and every T_k vanishes.
This contradicts the proposed nonzero cycle.
Hence Delta is maximal.
The zero-cycle case is immediate and does not require an empty matrix argument.

### (ii) implies (iii)

Proceed by matrix size.
At size one, a nonzero kernel vector has a nonzero adjoint-kernel partner by Lemma 3.3; condition (ii) forces A=0, incompatible with fullness.

For size N, assume every smaller full linear matrix evaluates injectively at X.
If a nonzero f in ker A(X) has dependent components, choose scalar invertible U with Uf=(f',0), f' nonzero.
Write AU^{-1}=(B,b).
Proposition 2.7 selects a full linear (N-1)-by-(N-1) submatrix B' from B, and B'(X)f'=0 contradicts induction.
Thus f's components are independent.

Lemma 3.3 supplies nonzero e in ker A(X)*.
If its components were dependent, apply the same deletion argument to A* at X*, obtaining a full linear B' of size N-1 with a nonzero kernel at X*.
Lemma 3.3 then gives a nonzero kernel for B'(X*)*=(B')*(X).
Formal star preserves fullness: taking star of any factorization gives a factorization with the same intermediate dimension.
Induction at X, applied to (B')*, now gives the contradiction.
This step does not assume induction for X* without proof.
Both component families are therefore independent; condition (ii) forces A=0, contradicting fullness.

### (iii) implies (ii)

Take A with the two independent component families.
If A were full, (iii) would immediately contradict its nonzero kernel; assume 0<r=rho(A)<N.
Theorem 2.10 gives

\[
UAV=\begin{pmatrix}B&0\\C_1&C_2\end{pmatrix},
\qquad B\in M_{N-S,r-S},\quad \rho(B)=r-S.
\]

If S<r, the first r-S components f' of V^{-1}f form a nonzero independent subfamily and satisfy B(X)f'=0.
Theorem 2.6 selects a square full linear submatrix B' of size r-S, giving B'(X)f'=0, forbidden by (iii).

If S=r, the upper block is zero and UAV consists of N-r zero rows above C_2.
Then rho(C_2)=r: deleting or adjoining zero rows does not change inner rank.
Put e'=(U*)^{-1}e, whose components remain independent, and take its last r components e''.
From the adjoint kernel equation one gets C_2*(X*)e''=0.
The matrix C_2* has full column rank r; Theorem 2.6 selects r rows to give a square full linear B with B(X*)e''=0.
Since e'' is nonzero, Lemma 3.3 gives a nonzero kernel for B(X*)*=B*(X), contradicting (iii).
This fills out the abbreviated last argument on source p. 20.
The only remaining possibility is rho(A)=0, namely A=0.

This completes the exact three-way equivalence.
Each use of a full square submatrix occurs at positive size, and all changes of components are scalar invertible maps preserving complex-linear independence.

## Dependencies, Evidence, and Limits

The external algebra consumed here is precisely Theorems 2.6 and 2.10 plus Proposition 2.7.
Their hypotheses and the repaired Cohn citation are recorded in [U001](Yin_U001.md#msy23-u001).
The trace-kernel lemma is proved directly above.
The definition of Delta uses the standard faithful von Neumann dimension of a closed submodule; no entropy inequality or dual-system existence theorem is required for Section 3.

The assigned published pages were read from local extraction, and pp. 15, 17, 18, 19 and 20 were visually inspected to check complex overbars, Gram products, block dimensions and adjoint substitutions.
No printed coefficient or sign error was found in Lemmas 3.4-3.5.
The danger of losing conjugates is an extraction issue, not a source correction.
No numerical test, proof assistant, or external human review was performed.

The theorem proves injectivity of full linear evaluations.
It does not estimate the inverse, turn it into a bounded operator, or identify the scalar division closure inside M.
Any later use as an affiliated invertibility theorem must retain the finite-tracial affiliated-algebra step supplied by the subsequent unit.

## Independent Review

On 2026-09-08, a separate reviewing agent independently reconstructed the finite-rank correspondence and all four implications of Theorem 3.1 against the source text, with visual checks of published pp. 17 and 20.
In Lemma 3.5 the first-slot-linear convention gives `T_k f_p=sum_j A^(k)_{pj}f_j`, so the compressed products occur as `B^(k)A^(k)` and `A^(k)B^(k)` in exactly the displayed order; the adjoint calculation conjugates their entire product.
The two invertible Gram matrices in the forward implication require no extra transpose.
For `(ii)=>(iii)`, a compressed kernel at `X*` is converted by the finite-trace kernel lemma into a kernel of its formal adjoint at X before induction is applied.
For `(iii)=>(ii)` with `S=r`, the last r components of `(U*)^{-1}e` remain independent; selecting r rows of the full-column matrix `C_2*` preserves their kernel, and a second explicit finite-trace adjoint transfer produces the contradiction at X.
Thus neither argument assumes selfadjoint variables or an unproved induction hypothesis at `X*`.
Rank-zero and empty-block cases were checked separately.
No further proof or coefficient error was found; the abbreviated final source sentence is justified by the supplied expansion.

## Source and inspection

Source edition: MSY23 / MSY23, the user-supplied 50-page published article in Journal of Functional Analysis 285 (2023), article 110016, DOI 10.1016/j.jfa.2023.110016. Printed pages equal PDF pages. The separate 37-page arXiv v2 was not compared in full; other works retain their own versions and inspection limits in the body.

Source passages: Complete Section 3, published pp. 12-20, Theorem 3.1 and Lemmas 3.3-3.5; the start of Section 4 on p. 20 belongs to U003.

Inspection: 2026-09-08: every assigned page read; finite-rank correspondences and all four implications reconstructed and independently reviewed, including adjoint transfers, complex conjugation and degenerate blocks. External algebra retains U001's exact scope and repaired Cohn citation. No selfadjointness assumption, bounded inverse estimate, numerical test, proof assistant or external human review is inferred.

## Additional definition and convention source recheck

<a id="msy23-definition-recheck"></a>

The following exact 2026-09-10 source-reading account was retained from L_F0081 at 2026-10-21T01:35.
It supplies the complete Delta formula missing from the earlier unit and retains the rank, ambient-algebra and tracial-conjugation distinctions.
Its original inspection depth and exclusions are independent of the 2026-09-08 proof review above.
The already sufficient general definitions remain at their linked U001/U003/U004/U006 homes.
The original AP18 construction is separately retained in [AP18-U001](../AP18/Yin_U001.md#tomita-foundational-reference).
References to an unchanged unit or a sidecar in the retained account describe its original 2026-09-10 checkpoint; this maintenance performs no original-source reopening or new proof review.

- Date and reviewer: 2026-09-10, the free-field algebra agent.
- Source: [MSY23, published MSY23.pdf](../../../literature/pdf/MSY23.pdf), JFA 285 (2023), 110016, 50 pages.
  Printed and PDF page numbers agree.
- Existing units: [U001, rank](Yin_U001.md#msy23-u001), [U002, finite-rank cycles](#msy23-u002), [U003, representations and closures](Yin_U003.md#msy23-u003), [U004, affiliated realization](Yin_U004.md#msy23-u004), and [U006, strong Atiyah property](Yin_U006.md#msy23-u006).
  Exact existing definition homes are linked below.
- Scope: a definition and convention sidecar, not a new source unit or project claim.
  The relevant existing audit sections were reread; primary definition passages on pp. 8, 10–13, 20–25, 29 and 42 were freshly checked, with surrounding statements used only to delimit their meaning.
  Rendered pp. 13, 21, 24, 25, 29 and 42 were inspected.
  This is not a fresh complete proof audit of those sections.
- Preservation: the existing units and source PDF are unchanged.
  Their proof assessments, repairs and declared external inputs remain authoritative.
  This note follows the [definition rules](../../../definitions/readme.md) and [reuse rule](../../../../framework/rules/knowledge-reuse.md#reuse-before-proof).

## Existing General Definition Homes

| General entry | Exact existing home | Published locator and convention checked |
| --- | --- | --- |
| Inner rank, rank factorization and fullness | [U001, definitions and elementary matrix arguments](Yin_U001.md#definitions-and-elementary-matrix-arguments) | Definition 2.1, p. 8. For a nonzero \(m\times n\) matrix over a unital complex algebra, inner rank is the least factorization size \(r\); zero has rank zero. Full means rank \(\min(m,n)\). The base algebra belongs to the definition. |
| Stable finiteness, also called weak finiteness | [Same U001 section](Yin_U001.md#definitions-and-elementary-matrix-arguments) | Definition 2.2, p. 8: for every finite \(N\), \(AB=I_N\) implies \(BA=I_N\). This is a matrix condition, not merely the scalar direct-finiteness condition. |
| Hollow square matrix | [Same U001 section](Yin_U001.md#definitions-and-elementary-matrix-arguments) | Definition 2.8, p. 10: an \(N\times N\) matrix has a zero \(K\times L\) block with \(K+L>N\). |
| Linear matrix | [Same U001 section](Yin_U001.md#definitions-and-elementary-matrix-arguments) | Definition 2.9, p. 10: \(A=A_0+\sum_j A_jx_j\), with constant coefficient matrices. “Linear” includes the constant term; invertibility of \(A_0\) is not required. |
| Central eigenvalues relative to complex scalars | [Same U001 section](Yin_U001.md#definitions-and-elementary-matrix-arguments) | Definition 2.12, pp. 11–12: \(\lambda\in\mathbb C\) such that \(\rho(P-\lambda I_N)<N\). The chosen scalar field is not replaced by the entire center of an arbitrary coefficient algebra. |
| Linear representation of a free-field element | [U003, conventions and dependency boundary](Yin_U003.md#conventions-and-dependency-boundary) | Definition 4.2, p. 21: \(r=uA^{-1}v\), with \(A\) full and affine linear over \(\mathbb C\langle x\rangle\), \(u\in M_{1,N}(\mathbb C)\), \(v\in M_{N,1}(\mathbb C)\). Neither minimality nor regularity at zero is part of this definition. |
| Representation domain and free-field function domain in a chosen algebra | [U003, Theorem 4.4 and Definition 4.5](Yin_U003.md#theorem-44-and-definition-45-consistency-on-the-chosen-domain) | Definition 4.5, pp. 22–23. A representation is evaluable when its pencil is invertible in the specified matrix algebra; the function domain is the union over its representations. Theorem 4.4 supplies consistency for stably finite ambient algebras. |
| Matrix rational closure and scalar division closure for a general inclusion | [U003, Definitions 4.7 and 4.10](Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra) | Definition 4.7, p. 24, and Definition 4.10, p. 25. These are general constructions for a unital subalgebra in a fixed unital ambient algebra. |
| Complete division closure | [U003, complete division closure](Yin_U003.md#complete-division-closure-and-proposition-411) | Discussion and Proposition 4.11, pp. 26–27. Inverse closure at every matrix size gives the alternative formulation of matrix rational closure retained in U003. The equivalence is an accepted result, not an additional project definition or a request for a new proof. |
| Analytic rank | [U004, Lemmas 5.1–5.5](Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) | Definition 5.4, p. 29. See the normalization check below. |
| Strong Atiyah property | [U006, setting and closure conventions](Yin_U006.md#setting-and-closure-conventions) | Definition **5.22**, p. 42: every polynomial matrix evaluated at the tuple has integral analytic rank. Theorem 5.23 is a consequence under maximal \(\Delta\), not the definition's number. |

The universal free field discussed in Section 4.1, pp. 20–21, is the universal division ring of fractions of the free polynomial algebra.
The more explicit general definition is already housed in [Yin20-U003, free fields and localization](../Yin20/Yin_U003.md#3-free-fields-and-the-retained-localization-interface).
MSY23 Theorem 4.1 supplies the retained fullness and inner-rank-preservation interface.
Neither that theorem nor an affiliated realization is incorporated into the definition of a linear representation.

## Fixed-Ambient Closure Conventions

The [existing U003 home](Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra) contains the complete general definitions.
With letters standardized to \(A\subseteq B\):

- \(\operatorname{Div}_B(A)\) closes under inverses of scalar elements that are units in \(B\).
- \(\operatorname{Rat}_B(A)\) collects entries of inverses of all finite square matrices over \(A\) that are invertible over \(B\).

This paragraph records a notation conversion, not new definitions for particular parameters.
Taking \(A=\mathbb C\langle X\rangle\), \(B=M\), or \(B=\mathcal U(M)\) belongs at the consuming statement.
Adding generator adjoints changes the chosen \(A\), rather than the general closure operation.
A division-closed subalgebra need not be a division ring.

Source uses of “rational closure” for scalar inverse closure, including the formal-series terminology in [Reu96](../Reu96/Yin_U001.md#formal-series-closure-terminology) and [CR94](../CR94/Yin_U001.md#cr94-no-additional-entry), must be converted explicitly.
The name alone does not identify that construction with matrix rational closure in every ambient algebra.

Theorem 4.4 and Lemma 4.8 operate in the algebra already specified by the domain or rational-closure premise.
They do not change that algebra after observing that one matrix compression is bounded.
The precise source and counterexample boundary remains in the separate bounded-linearization recheck.
Proposition 4.11's division-ring hypothesis concerns the closure in that same ambient algebra.

<a id="delta-finite-rank-cycles"></a>
## The General Finite-Rank-Cycle Definition of Delta

The existing [U002 setting](#setting-delta-and-the-three-conditions) records the cycles and maximality criterion but does not display the entire dimension formula.
This is the supplemental definition home, transcribed from the unnumbered definition on published pp. 12–13.

**Definition (MSY23 convention).**
Let \((M,\tau)\) be a tracial \(W^*\)-probability space with faithful normal tracial state, let \(H=L^2(M,\tau)\), and let \(X=(X_1,\ldots,X_d)\in M^d\).
Write \(\lambda\) for left multiplication and \(J\) for the conjugate-linear isometry extending \(a\mapsto a^*\).
Then

\[
\mathcal C_X=
\left\{(T_1,\ldots,T_d)\in\operatorname{Fin}(H)^d:
  \sum_{j=1}^d[T_j,J\lambda(X_j^*)J]=0\right\},
\qquad
\Delta(X)=d-\dim_{M\bar\otimes M^{\mathrm{op}}}
                  \overline{\mathcal C_X}^{\,\mathrm{HS}}.
\]

Here \(\operatorname{Fin}(H)\) consists of operators with finite-dimensional complex range, and the closure is in \(\mathrm{HS}(H)^d\) with its Hilbert-Schmidt norm.
The dimension is the von Neumann module dimension for the standard Hilbert-Schmidt \(M\bar\otimes M^{\mathrm{op}}\)-module, using the product trace induced by \(\tau\).
The \(d\)-fold ambient module has dimension \(d\).
The operator \(J\lambda(X_j^*)J\) is right multiplication by \(X_j\).

There is no normality, selfadjointness, dual-system assumption, or requirement that this tuple generate all of \(M\) in this definition.
The closure of finite-rank cycles is essential; it is not replaced by the space of all Hilbert-Schmidt solutions or an operator-norm closure.
The number \(d\) is not divided out.
The equivalence of \(\Delta(X)=d\) with absence of a nonzero finite-rank cycle is the faithful-dimension observation retained in U002, rather than a different definition.

No first-introduction claim is made.
MSY23 attributes the invariant and its homological origin in its discussion on pp. 12–13; the present task verifies MSY23's formulation, not that attribution's historical priority.

<a id="analytic-rank-normalization"></a>
## Analytic Rank, Matrix Size, and Representation Dimension

The definition itself remains in [U004](Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness).
Definition 5.4, p. 29, uses

\[
\operatorname{rank}_{\mathrm a}(P)
 =(\operatorname{Tr}_N\otimes\tau)
      (p_{\overline{\operatorname{ran}P}})
 =N-(\operatorname{Tr}_N\otimes\tau)(p_{\ker P}),
 \qquad P\in M_N(\mathcal U(M)).
\]

\(\operatorname{Tr}_N\) is the **unnormalized** matrix trace, so \(\operatorname{rank}_{\mathrm a}(I_N)=N\) and values lie in \([0,N]\).
The preceding use of normalized \(\operatorname{tr}_N\) to equip a matrix amplification with a tracial state does not change this convention.

| Notion | Meaning and normalization |
| --- | --- |
| Polynomial inner rank \(\rho_A(P)\) | Least algebraic factorization size over the specified \(A\). |
| Analytic rank \(\operatorname{rank}_{\mathrm a}(P)\) | Trace of the range projection using \(\operatorname{Tr}_N\otimes\tau\); need not be an integer without hypotheses. |
| Finite-rank operator rank | Complex dimension of an operator's range on \(H\); this is the rank of finite defects and dual commutators. |
| Representation dimension \(N\) | Size of a particular linear representation. A minimum over an explicitly specified representation class is a separate minimality notion. |
| “Rank of a rational series” in CR94/Reu96 terminology | Minimal dimension in the relevant representation class; it is not MSY23 analytic rank. See [CR94's convention check](../CR94/Yin_U001.md#representation-rank-convention). |

Theorem 5.6's equality of evaluated analytic rank with polynomial inner rank has substantive hypotheses; it is not a definitional identification.
The strong Atiyah property in Definition 5.22 requires nonnegative integral analytic ranks for all finite sizes and polynomial matrices.
It does not require equality with their original polynomial inner ranks.

## Citation and Reuse Disposition

<a id="tomita-conjugation"></a>
### Follow-up: Tomita's Conjugation Operator

Date and reviewer: 2026-09-10; the coordinating agent, scoped definition/source check.
The published MSY23, Section 3, p. 13, immediately after the definition of Delta, explicitly identifies \(J\) as Tomita's conjugation operator: the conjugate-linear isometric extension of \(x\mapsto x^*\) from \(M\) to \(L^2(M,\tau)\).
The page was read and visually checked.
The published [ACSY24](../../../literature/pdf/ACSY24.pdf), p. 29, also uses that name and states \(J(x)=x^*\); its passage was checked in extracted text.

In tracial GNS notation this is exactly \(J(x\Omega)=x^*\Omega\).
The involution property \(J^2=I\) follows on the dense subspace \(M\Omega\) from \((x^*)^*=x\), then on all of \(H\) by continuity.
MSY23, p. 13, supplies the definition and terminology, with ACSY24 as corroboration.
This is the tracial conjugation operator; no nontracial modular-domain assertion is imported.
No new definition or Claim ID is allocated, and no whole-source proof review is claimed.

### Earlier Citation Disposition

MSY23 is a suitable candidate for the labels **current formulation**, **notation**, or **standard interface**, with the exact locators above.
It is not labeled **origin** by this recheck.
Known evaluation consistency, complete-closure equivalence, and rank-preservation results can be used at their existing audited interfaces when their hypotheses match; no new C identifier or reconstruction is required merely to use them.

The Claim definition-use record, attached from the Claim registry, records the adopted precise links and distinguishes statement, proof and comparison use.
It does not alter historical theorem dependencies.
Dual-system definitions are handled by the other source group and are not duplicated here.
