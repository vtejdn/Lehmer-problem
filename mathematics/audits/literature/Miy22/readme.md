<a id="yin-source-edition"></a>
# Miy22: Source Audit and Reusable Proof Inputs

Author: Yin

Audit date: **2026-09-08**.
Goal: [Miy22 source audit](#miy22-source-audit).

Source: [Miy22](../../../literature/pdf/Miy22.pdf), Akihiro Miyagawa, *A characterization of rationality in free semicircular operators*, Journal of Functional Analysis 283 (2022), article 109609.
[references.bib](../../../literature/references.bib) is the canonical bibliography.

## Audit Outcome

Follow-up, 2026-09-09: the user's Kronecker/Yin_C_F0004 comparison adds [Miy22-U009](Yin_U009.md#miy22-u009), a complete local reconstruction of Theorem 2.8 and its exact rank formula.
This extends the original eight-unit audit; its historical imported-theorem limits below describe the earlier checkpoint.
The new unit separately records independent review, primary-book reading, the two Haar Hankel blocks, and the boundary for general spectral measures.

The 24-page local journal version has been read and organized into eight reusable units.
The bounded and affiliated proof chains were reconstructed, including the analytic realization, denominator independence, and cofinite-domain arguments.
The checked chains support the stated Theorems 3.1 and 4.5 and Proposition 4.12 **with the local corrections below and the explicitly retained foundational inputs**.
No counterexample to those main statements was found in this audit.

The printed proof contains false auxiliary assertions, omitted-case bookkeeping, and typographical issues.
These are documented with their repairs; this is not a clean transcription or an assertion that the original text needs no correction.
The full rational-series equivalence and the underlying Fock/affiliated-operator theories were not independently re-established from all cited original sources.
Source-audit completion does not mean formal verification, external human review, or proof of novelty.

## Source Identity and Version Check

- Audited artifact: `mathematics/literature/pdf/Miy22.pdf`, 24 pages; printed page numbers 2-24 agree with PDF pages 2-24, with the opening article page treated as p. 1.
  The 2026-10-14 comparison read U001–U009 individually against the current formal passages: the Fock/residual conventions, exact Kronecker rank formula, bounded realization and regular-fraction/domain chain agree with the retained interfaces and corrections.
  The original review dates, later follow-up and proof/import boundaries are unchanged.
- The original audit compared extraction with rendered formulas to resolve bars, stars, subscripts and domains.
  Current-file maintenance does not assert continuity of its bytes with the original review input.
- The [publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0022123622002294) identifies volume 283, issue 8, article 109609 and the journal title used here.
- The [arXiv record](https://arxiv.org/abs/2109.08841) identifies a related preprint under the title *A characterization of rationality for operators in free semicircular elements*: v1 on 2021-09-18 and v2 on 2022-06-27, with the same journal DOI.
  Its listed 20-page preprint was not downloaded or compared line by line; all audit locators refer to the 24-page local journal PDF.
- A bounded version/errata search checked that record, the publisher listing, the [author's publication page](https://sites.google.com/view/akihiromiyagawahomepage), and title/DOI searches with correction terms on 2026-09-08.
  No correction notice was identified in the inspected results.
  This does not establish that no correction exists.
  The findings below are local audit findings, not author-confirmed errata.

## Unit Navigation

| Unit | Mathematical input | Source location |
| --- | --- | --- |
| [Miy22-U009](Yin_U009.md#miy22-u009) | Complete Kronecker proof, exact rank/pole count, formal difference-kernel identity and Haar comparison | Theorem 2.8, pp. 7-8; user-requested follow-up, 2026-09-09 |
| [Miy22-U001](Yin_U001.md#miy22-u001) | Full Fock model, monic Chebyshev word basis, trace, cancellation notation, and bounded versus affiliated closures | Sections 2.1-2.2, pp. 3-6; pp. 8, 19 |
| [Miy22-U002](Yin_U002.md#miy22-u002) | Finite residual spaces, minimal representations, Hadamard product, and repaired scalar rational decay | Definition 2.4, Theorems 2.5-2.8, Corollary 2.9, pp. 6-8 |
| [Miy22-U003](Yin_U003.md#miy22-u003) | Rank-one cut formula, bounded coefficient residuals, inverse closure, and dual-system scope | Lemmas 3.2-3.3 and Proposition 3.9, pp. 9-10, 16-18 |
| [Miy22-U004](Yin_U004.md#miy22-u004) | Matrix realization of word polynomials, Haagerup bounds, and rational square-summability to norm convergence | Lemmas 3.4-3.6 and Corollary 3.7, pp. 11-16 |
| [Miy22-U005](Yin_U005.md#miy22-u005) | Scalar-division resolvent construction, minimality, and the complete bounded theorem | Lemma 3.8, Proposition 3.9, Theorem 3.1, pp. 8, 16-18 |
| [Miy22-U006](Yin_U006.md#miy22-u006) | Regular fractions, common denominators, and representation-independent bounded defects | Lemmas 4.1-4.3 and 4.6, pp. 19-20 |
| [Miy22-U007](Yin_U007.md#miy22-u007) | Affiliated rationality criterion, closure operations, and bounded rational numerators/denominators | Theorem 4.5 and Lemmas 4.8-4.11, pp. 20-22 |
| [Miy22-U008](Yin_U008.md#miy22-u008) | Algebraically cofinite commutation with exact domains, including the creation variant | Proposition 4.12 and Remark 4.13, pp. 22-24 |

For use of the bounded theorem, read U001, U003, and U005, following the U002/U004 dependencies where needed.
For unbounded rational expressions, also read U006-U008; bounded commutator syntax does not automatically extend to an affiliated operator.

The [global source-audit index](../index.md) registers these units.
This page provides navigation and the integrated assessment; each unit contains its authoritative content, proof checks, and limitations.

## Main Statements and Proof Chain

<a id="f0001-common-denominator-comparison"></a>
### Common-denominator source comparison, 2026-10-12

At the user's request, the authoring AI agent reread the retained published Section 4 opening and Lemma 4.1, printed/PDF p.19, in extracted text and a rendered page.
Lemma 4.1 proves that two affiliated elements have common bounded left and right fraction representatives.
Starting from bounded regular denominators f_1,f_2, its left construction writes f_1 f_2^{-1}=x^{-1}y and takes f=x f_1=y f_2; the right construction is analogous.
Iteration of this algebraic common-multiple mechanism supplies the finite-family conclusion.
Although the paper is in the semicircular setting, this particular argument uses only the finite von Neumann algebra's bounded fraction calculus; that applicability was checked.
It does not display a row/column functional-calculus formula.
[U006](Yin_U006.md#miy22-u006) retains the earlier proof reconstruction and its bounded-representative correction; no fixed unit or earlier review scope was rewritten.
[The Lin00 comparison](../Lin00/readme.md#f0001-common-denominator-comparison) distinguishes an explicit finite-family assertion from a proof.
Search stopped after both original passages and the proof correspondence were verified.

With $P=\mathbb C\langle s\rangle\subset A=C^*(s)\subset M=W^*(s)$ on full Fock space over a finite-dimensional one-particle space, the bounded theorem states

\[
\{a\in M:\operatorname{rank}[r_i^*,a]<\infty\text{ for all }i\}
=C_{\mathrm{div}}(s)=C_{\mathrm{rat}}(s)\subseteq A.
\]

For a closed densely defined affiliated operator $u=f^{-1}a=bg^{-1}$, where $a,b,f,g\in M$ and $f,g$ are regular, the criterion uses the **bounded** defects

\[
\Delta_i=f r_i^*b-a r_i^*g.
\]

Finite rank for every $i$, in one such representation, is equivalent to the condition in every representation and to $u\in D(s)$.
Moreover,

\[
D(s)\cap M=C_{\mathrm{div}}(s),
\]

and rational bounded numerators and denominators may be chosen.
The domain-sensitive cofinite reformulation is stated exactly in U008, including the joint annihilation-domain equality and the stronger individual creation-domain equalities.

| Proof obligation | Checked mechanism and evidence | Dependency limit |
| --- | --- | --- |
| Convert finite rank to finite residual dimension | U003's exact suffix formula, extended by bounded right multiplication in $L^2$ | Requires the tracial Fock identification in U001 |
| Obtain and control a finite linear representation | U002's residual equivalence and minimality; U005's shifted-coefficient $\ell^2$ bound | Full rational/recognizable equivalence is imported as stated in Miy22 |
| Realize the word basis multiplicatively | U004's $2d$-dimensional matrices and fixed compression | Direct substitution $X^v\mapsto U_v$ is not multiplicative |
| Establish convergence before taking an inverse | U004's homogeneous estimates, Hadamard squares, and repaired scalar decay | F01-F04 below must be reflected in reuse |
| Stay in scalar division closure | U005's small-power argument and scalar Schur pivots for Lemma 3.8 | Does not assume general division/rational closure equality |
| Identify the bounded operator and close the equivalence | U005's separating vacuum plus U003's matrix inverse commutator formula | Applies to this semicircular tuple, not an arbitrary dual-system tuple |
| Make the affiliated defect representation independent | U006's regular common denominators and injective/dense-range cancellation | Uses standard affiliated-algebra infrastructure |
| Establish affiliated closure and bounded intersection | U007's sum/product/inverse/adjoint identities and bounded regularization | Uses the bounded theorem; does not need the optional free-skew-field identification |
| Justify domains in cofinite commutation | U008's literal compositions, finite-codimensional inverse images, and valid $V_2^i$ choice | Algebraic finite codimension; no closedness or graph-density strengthening |

## Findings and Required Corrections

The finding identifiers below belong to this audit and do not create new bibliographic keys or project theorem IDs.

| Finding | Location | Issue and resolution |
| --- | --- | --- |
| F01 | p. 8, paragraph before Corollary 2.9 | The exponential estimate at exactly the maximal pole modulus is false for repeated poles. The sequence $(n+1)r^n$, $0<r<1$, is an explicit witness. Choose a strictly larger rate below one; U002 gives a complete scalar repair. |
| F02 | Lemma 3.5 proof, pp. 13-14 | Coefficient-word lengths and summation ranges switch from the fixed degree $m$ to the input tensor degree $n$. U004 restores $m$ and $m-k$ and checks the norm estimate. |
| F03 | Lemma 3.6 proof, p. 15 | The endpoint factorization assumes at least two runs, although a word of length at least two may have one run. U004 supplies the direct single-run matrix-power calculation; the final bound remains valid. |
| F04 | Corollary 3.7 proof, p. 16 | The matrix estimate with factor $4d^2$ invokes Lemma 3.6, although the printed reference says Lemma 3.5. |
| F05 | Lemma 4.1 proof, p. 19 | The opening representatives must be chosen bounded, as supplied by the preceding paragraph; their printed affiliated-algebra membership is too weak to specify the proof's inputs. U006 makes boundedness and regularity explicit. |
| F06 | Remark 4.4, p. 20 | The hypothesis swaps the two numerators. Use $f r_i^*b-a r_i^*g$, matching the definition and displayed argument; U007 records the corrected calculation. |
| F07 | Lemma 4.10 proof, p. 21 | The final conclusion must read $u^{-1}\in R(s)$, as its statement and defect computation require. |
| F08 | Proposition 4.12 proof, p. 23 | The first suggested auxiliary cofinite space can have infinite codimension: $f=I$, $d\geq2$ gives the range of $r_i$. The alternative inverse-image construction in the same sentence is valid and is verified in U008. |

F01 and F08 are explicit failures of auxiliary assertions; F03 needs an omitted case supplied.
The other entries are notation or reference corrections.
None of these observations by itself refutes a main theorem.
The precise repaired implications, rather than the labels in this table, are the evidence for subsequent use.

## Review Coverage and Verification Boundary

- **Direct source reading:** all sections of the local 24-page journal paper were covered.
  The main mathematical pages were visually inspected in addition to extraction, including the images at every reported finding.
- **Primary reconstruction:** the coordinating agent reviewed the model, rational-series interfaces, decay repair, and residual mechanism; the analytic reviewer reconstructed Lemmas 3.4-3.8 and Proposition 3.9; the affiliated reviewer reconstructed Section 4, including the terse creation-domain variant.
- **Cross-checks:** an independent commutator reviewer reconstructed Lemmas 3.2-3.3 and the bounded closure direction and reviewed U001-U003, including the repaired boundary-pole estimate and the $L^2$ passage.
  The coordinating agent checked the analytic and affiliated reconstructions against their source formulas.
  The affiliated reviewer independently checked U004-U005's scalar pivots, minimality, convergence, and compression.
  The analytic reviewer independently checked U006-U008's denominator cancellation, absence of a dependency cycle, and both domain constructions against rendered pp. 19-24.
  These reviews found no unresolved local implication in the repaired arguments under the recorded inputs.
  Reviews concern stated arguments and assumptions, not merely agent agreement.
- **Exact finite computation:** the word-action record reports 64,325 passing integer equalities in the specified finite domain.
  Intermediate word support was not truncated.
  No numerical rank test or finite run proves the all-word, norm-convergence, or affiliated conclusions.
- **Artifact checks:** on 2026-09-08, a repository check covered 19 Markdown files, 152 local file/anchor links, all eight unique unit anchors, English-language text, balanced math/code delimiters.
  These checks verify record integrity, not mathematical truth.
- **Imported foundational theory:** the full rational-series equivalence quoted from Miy22's reference [2], the textbook Fock trace/semicircular facts, and the standard affiliated-operator algebra remain explicit inputs.
  Individual consequences needed in the proof were reconstructed where described.
  This is not an audit of every cited textbook or paper.
- **Optional identification:** the claim that $D(s)$ realizes the free skew field is quoted by Miy22 from its reference [13].
  It was not independently audited, and it is not needed for the proof of Theorem 4.5 with $D(s)$ defined as division closure.
- **Not performed:** proof-assistant verification, external human review, author confirmation of the findings, or exhaustive errata/version comparison.
  No project theorem or novelty claim was registered.

<a id="goal-completion-review"></a>
## Goal Completion Review and Safe Reuse

Review date: **2026-09-08**.
The analytic reviewer (the reviewing agent) independently compared the source-audit deliverables with the original Miy22 source audit contract; the coordinating agent performed the final integration review.
This is a source-study completion review, not a new project-theorem proof audit.

| Original criterion | Completion evidence and boundary |
| --- | --- |
| Exact artifact and version record | The source-identity section records the 24-page journal PDF and page mapping, and the actual limited version/errata search. |
| Stable reusable units | U001-U008 supply source links, locators, hypotheses, mechanisms, and dependency limits; the global source-unit index registers all eight. |
| Bounded and affiliated proof-chain review | The obligation map and unit reconstructions cover both main chains and exact-domain reformulation; F01-F08 and external inputs remain explicit. |
| Reproducible finite computations | The historical account reports 64,325 exact equalities. The selected current computation index/program metadata does not locate its native program/J; U003 retains the finite scope and concrete reproduction limit. |
| Integrated outcome and project handoff | This record supplies coverage, correction evidence, and reuse guidance; the goal index and current assessment identify the completed source-audit scope. |

Miy22 source audit's deliverables are supplied by the edition and pagination explanation, eight units, the proof-obligation map, correction evidence, and the registered finite computation.
The completed deliverable is a **source audit with explicit corrections and trust boundaries**.
It is not a claim that every statement in the paper has been independently certified from first principles.

For a future research goal, cite the specific unit, retain its assumptions and relevant corrections, and discharge any local adaptation.
If the future argument depends essentially on a currently imported theorem or on the optional free-field identification, audit that exact external interface before upgrading its verification status.
No new research route is activated by these possible follow-ups.

<a id="historical-contract-v1"></a>
<a id="miy22-source-audit"></a>
## Miy22 source audit: Audit Miy22 as a Reusable Research Input

Origin and authorization: user-assigned on 2026-09-08, requesting the first literature audit of Miy22.

### Original Question

Read and audit [Miy22](../../../literature/pdf/Miy22.pdf), *A characterization of rationality in free semicircular operators*, and organize its mathematical content into inputs another agent can understand and use.
Identify exact statements, hypotheses, proof mechanisms, dependencies, verified steps, and unresolved limitations.

### Scope and Exclusions

Cover the complete 24-page local journal version: preliminaries, the bounded finite-rank commutator criterion, and the affiliated-operator extension, including the domain-sensitive reformulation.
Inspect mathematical arguments and critical formulas, distinguish directly checked steps from imported theorems, and record any suspected error with evidence.

This is a source-audit goal.
It does not require resolving every external reference, inventing a new theorem, proving novelty, creating a manuscript, or formalizing the article.
A completed audit may retain explicitly delimited unverified dependencies or unresolved objections; those conditions limit downstream use and cannot be described as a completed proof verification.

### Notation and Conventions

Use the source's finite-dimensional complex full Fock space, variance-one free semicircular generators, vacuum trace, bounded von Neumann algebra, and algebra of affiliated operators.
Distinguish scalar and matrix inverse closure, formal series and operator convergence, and bounded commutators from domain-sensitive affiliated defects.
Normalize ambiguous source notation explicitly in the audit units.

### Completion Criteria

1. Record the exact local source edition and page mapping, and any version/errata search actually performed.
2. Extract stable source units covering the main definitions, statements, proof mechanisms, and dependencies, with exact source locators and original-file links.
3. Review the bounded and affiliated proof chains, identifying checks, imported inputs, gaps, and limitations rather than relying only on the published status.
4. Preserve any supporting finite computations with their exact scope and execution evidence; computations do not replace the general arguments.
5. Provide an integrated audit outcome, coverage and dependency map, usable-input guidance, and a truthful verification boundary.
   Update the source-unit index and current project assessment.

### Related Records

- [Integrated Miy22 audit and completion evidence](readme.md).
- [Source-unit registry](../index.md).
- [Goal state and completion evidence](../../../tasks/index.md).
- Exact finite commutator execution record and [computation index](../../../computations/readme.md).

### Contract Changes

- 2026-09-08: initial user-authorized source-audit scope recorded.
  No new mathematical research claim is assigned by this goal.


<a id="presentation-observations"></a>
## Selected rationality terminology and exposition

The selected presentation reading recorded 2026-09-10 covered published pp. 18–20 and 22–23.
Remark 3.11, p. 18, discusses dual systems using bounded acting operators; its right annihilation model is a particular construction.
Section 4, p. 19, introduces both regular-denominator fractions before the bounded cleared defect.
The complete [fraction and defect definitions](Yin_U006.md#statements-assumptions-and-notation) keep affiliated invertibility distinct from bounded invertibility.
Lemma 4.6, p. 20, concerns independence of the finite-rank condition, not equality of individual defects.
Theorem 4.5, p. 20, and its proof, p. 22, distinguish affiliated rationality, the bounded-intersection equality and bounded rational fraction entries.
Proposition 4.12, pp. 22–23, has an exact domain/equality interface; a forward inclusion alone is weaker.
The exposition introduces fractions, boundedness and change-of-fraction invariance before algebraic operations.
These source observations supply no broader tuple hypotheses or new proof coverage.
