# GGOW20: Operator Scaling and Noncommutative Rank

This audit uses the **full published article** *Operator Scaling: Theory and Applications*, Foundations of Computational Mathematics 20 (2020), pp. 223-290: [primary PDF](../../../literature/pdf/GGOW20.pdf), sole bibliographic.
The user-requested key GGOW20 is retained across the version replacement.
The main PDF has 68 pages; its printed page number is its one-based PDF page number plus 222.

On 2026-09-12 the user clarified that the supplied nine-page FOCS extended abstract was insufficient and requested replacement by the full article, without retaining the conference PDF.
The published author-hosted copy replaced it after title, authors, DOI, length validation.
The conference PDF was not archived.
All current unit locators and proof assessments below refer to the full published article.
No conference-only proof-sketch assessment is transferred to it.

## Reusable inputs and coverage

| Unit | Exact scope | Assessment |
| --- | --- | --- |
| [GGOW20-U001: rank and shrunk subspaces](Yin_U001.md#ggow20-u001) | Theorem 1.4 p. 227; Sections 1.1-1.3 pp. 228-233; invariant-theory interfaces pp. 237-240 | Source statements read; elementary block/range translations checked. Free-field and invariant-ring foundations accepted with original-proof boundaries. |
| [GGOW20-U002: capacity and scaling progress](Yin_U002.md#ggow20-u002) | Section 2 pp. 243-253, especially Theorems 2.12/2.14/2.18/2.20 | Complete local proof chain checked with retained blow-up and finite-grid inputs; [original root finding](../../reviews/Yin_R_F0008_v2.md#capacity-ggow20-finding) on the integral-capacity proof and normalization repairs, with unknown inherited-context relationship. |
| [GGOW20-U003: near minimizers and tensor products](Yin_U003.md#ggow20-u003) | Section 3 pp. 253-261; dual variational formula p. 242 | Complete local proofs checked with domain, small-error and adjoint conventions; the same original root finding on the precisely bounded near-minimizer chain, with unknown inherited-context relationship. |
| [GGOW20-U004: numerical precision and approximation](Yin_U004.md#ggow20-u004) | Sections 4-5 pp. 261-279 | Full text read. Rational recurrences and a conservative polynomial-precision reconstruction checked. Literal printed constants and the complete quantitative continuity proof remain questioned at specified steps. |
| [GGOW20-U005: polynomial matrices and rank algorithms](Yin_U005.md#ggow20-u005) | Appendix A pp. 281-287; Remark 1.19 p. 233 | Complete local reductions checked, including polynomial coefficient-bit growth, the zero-rank case and explicit rational Kraus matrices; main algorithm and free-field foundations retained. |

The full source's abstract, contents and introductory discussion (pp. 223-243), concluding questions and acknowledgments (pp. 279-281), and bibliography (pp. 287-290) were inspected for scope, version, provenance and dependencies.
Reading the introduction does not certify every historical comparison or every theorem quoted from another paper.
The dated open problems are not assertions about their present-day status.

This is a substantive audit of the full article's mathematical and algorithmic proof structure, with the precise limits above.
It is **not** a blanket claim that every displayed constant, external foundational proof or quantitative continuity statement has been independently verified.
The [original interface finding](../../reviews/Yin_R_F0008_v2.md#capacity-ggow20-finding) identifies the exact passages root checked separately from the assigned readers, without establishing the missing initial context-isolation facts.

## Main usable chain

For a homogeneous complex matrix pencil, the checked source interfaces connect free-field singularity, shrunk subspaces, rank decrease of its completely positive coefficient map, and vanishing finite-dimensional matrix substitutions.
The [Gur04 audit](../Gur04/readme.md) supplies the exact qualitative capacity and approximate-scaling background.

The full article's central integral estimate is

\[
 A_i\in M_n(\mathbb Z),\quad T_A\text{ rank non-decreasing}
 \quad\Longrightarrow\quad
 \operatorname{cap}(T_A)\geq n^{-2n}.
\]

Its proof uses a nonzero integer blow-up determinant, a finite-grid coefficient bound, a unital normalization and a Hilbert-Schmidt estimate.
The blow-up dimension cancels; no effective degree upper bound is required in this version.
Normalizing the input and tracking its denominator then gives a polynomial scaling-iteration bound.
Numerical precision is a separate part of the argument, treated in U004.

The near-minimizer result controls the finite-dimensional marginal error after scaling.
It is a particularly useful input for [MS24](../MS24/readme.md), which improves the capacity lower bound for integral Kraus data.
Tensor multiplicativity and the polynomial-rank reductions are separate reusable interfaces.

These results do not assert exact attainment of a doubly stochastic scaling, convergence or bounded condition numbers of the scaling factors, or a bounded inverse for a pencil evaluated in a von Neumann algebra.
Any free-probability use must separately verify the algebraic realization and the required analytic norm estimates.

## Corrections and unresolved details

The authoritative arguments and their review depths remain in the units:

- **U002 F1-F2:** the complex trace identity in Lemma 2.17 is replaced by a valid Hilbert-Schmidt proof; Theorem 2.20's denominator uses the original marginal before normalization.
- **U003 F3-F8:** the small-error range is explicit; row-sum terminology is corrected; Lemma 3.6's large-variance case is excluded; Lemma 3.10 requires \(T(C)>0\) and retains \(e^{-\delta}\); tensor multiplicativity uses the correct arbitrary-complex approximate-scaling input.
- **U004 [quantitative corrections](Yin_U004.md#quantitative-corrections):** singular marginals, iteration growth, reciprocal relative errors and rounded precision require repairs.
  A conservative asymptotic polynomial-time interface is recorded.
  Theorem 4.5's full quantitative modulus is still questioned pending consistent adjoint objectives and complete tolerance propagation.
- **U005:** Proposition A.2 preserves leaf descriptions, but collected coefficients can have larger bit size; a polynomial bound suffices.
  The rank algorithm explicitly returns zero if every positive threshold fails.
  The CP reduction has an explicit rational Kraus presentation.

The main integral-capacity and near-minimizer interfaces remain usable under their corrected assumptions.
The unresolved quantitative continuity details are not prerequisites of MS24's main determinant/capacity argument.
No project Claim, theorem designation or goal-completion status is created merely by this source intake.

## Search and version evidence

The initial trigger was the user's explicit intake and audit request.
The later trigger was the user's observation that GGOW20.pdf had only nine pages and request for the complete work.
Local inspection identified an extended abstract; its own full-version link led to arXiv 1511.03730.
The [version-specific arXiv record](https://arxiv.org/abs/1511.03730v4) identifies the expanded title and the January 2019 revision.
A bounded search for that title with the authors and publication year found the [author's IAS publication record](https://www.math.ias.edu/avi/node/2549) and its [published full PDF](https://www.math.ias.edu/~avi/PUBLICATIONS/GargGOW20.pdf).

The arXiv v4 PDF was temporarily inspected while the journal copy downloaded.
Once the published copy was validated, it became the sole retained main artifact; the temporary arXiv PDF was removed rather than retaining a redundant version.
Earlier conference theorem numbers such as I.12/I.13 are not used as locators for the full paper's Theorems 2.18/2.20 or Lemma 3.10.

Search stopped after obtaining the correct primary full text and enough evidence for the selected external interfaces.
No claim of an exhaustive errata search is made.
All proof coverage is tied to the retained journal artifact and the review date, 2026-09-12.
No algorithm implementation or proof-assistant verification was performed.
