<a id="yin-source-edition"></a>
# DR97: Integrated Source Audit

Author: Yin

Source: [DR97](../../../literature/pdf/DR97.pdf), the registered ten-page published article.
Canonical bibliographic identity is in [references.bib](../../../literature/references.bib).
This audit implements [DR97 rational-series source audit](#dr97-rational-series-source-audit).

Audit date: **2026-09-08**.
Reviewers: the coordinating agent (formal series, tree criterion, and integration), the analytic reviewer (Section 3), the Malcev-Neumann reviewer (Section 4), and the external-interface reviewer (external sources, version comparison, and relationship to Miy22).
Independent AI cross-review scopes are identified below; no external human review is claimed.

## Outcome and Scope

The reconstructed arguments support Theorem 7 (equality of scalar and all matrix inverse closures with the finite-rank algebra in the reduced group C*-algebra), Proposition 9 (rational square-summable reduced-word series admit bounded scalar-inverse realizations), and Theorem 12 with Corollary 13 (the Malcev-Neumann criterion and positive-formal-series intersection).
This assessment uses **finitely many free generators**, the corrected local arguments below, and the expressly accepted external interfaces.

The complete source was read and its local core proofs were reconstructed; this does not certify every preliminary generalization.
Section 2.1's results are reconstructed over a commutative field and finite alphabet.
Its arbitrary-commutative-ring formulations, semiring discussion, and historical attributions were inspected as statements, without a complete proof audit at that broader scope.
The source's initial unspecified alphabet cannot be read as an unrestricted infinite-alphabet convention: the proof uses finiteness, and one preliminary equivalence fails without it.

The accepted Haagerup and Malcev-Neumann inputs have exact source statements and applicability checks in U005, with original-proof boundaries retained.
The optional universal-free-field identification is checked separately and is not a premise of the two rationality criteria.
The audit finds no unresolved local implication in its reconstructed finite-generator chains; it does not claim an author-endorsed erratum, formal verification, or a new project theorem.

## Coverage and Reusable Units

The separately performed 2026-09-10 [definition and notation recheck](Yin_U001.md#definition-recheck) is retained in U001, without enlarging the original proof-review scope.

All page references below are printed pages of the primary published PDF: **printed page = PDF page + 612**.

| Unit | Mathematical content | Original coverage | Verification depth |
| --- | --- | --- | --- |
| [DR97-U001](Yin_U001.md#dr97-u001) | Formal inverse closure, residual spaces, Hadamard product, and minimal representations | Definition 1, Theorems 2-4, pp. 614-616; formula (2), p. 621 | Field-scope local proofs reconstructed and independently reviewed; broader ring/semiring reports delimited. |
| [DR97-U002](Yin_U002.md#dr97-u002) | Cayley-tree operator and finite-rank-to-rational implication | Section 2.2, Remark 2, Proposition 5, pp. 616-618 | Cancellation identity and restricted injectivity reconstructed and independently reviewed; finite exact check recorded. |
| [DR97-U003](Yin_U003.md#dr97-u003) | Equality of all inverse closures and the finite-rank algebra | Definition 6, Lemma 8, Theorem 7, pp. 618-619, 621 | Ambient derivation and nonunital representation repaired; complete inclusion chain cross-reviewed. |
| [DR97-U004](Yin_U004.md#dr97-u004) | Square-summability, decay, Banach matrix inverses, and realization | Lemmas 10-11, Proposition 9, pp. 619-621 | Local analytic proof reconstructed and cross-reviewed; primary-checked Haagerup estimate accepted. |
| [DR97-U005](Yin_U005.md#dr97-u005) | Exact external inputs, comparison with Miy22, and version/search evidence | DR97 dependencies and selected passages in supporting sources | Passage-specific source statements and applicability, not full audits of the supporting works. |

The introduction, pp. 613-614, was checked for closure definitions and intended conclusions.
The bibliography on p. 622 was inspected for dependency identities and misleading locators.
This is complete article reading with the proof-inspection boundaries above, not a recursive audit of all 17 references.

## Source Identity and Version

- Primary artifact: ten-page published journal version, 494,425 bytes.
  Its title page was rechecked for the identified edition.
- The primary file is unchanged.
  DR97 is distinct from Reu96 and its earlier filename history.
  No rename of either primary source occurred in this audit.
- A separately retained author-hosted typeset version was consulted for selected discrepancy checks.
  It is an additional source edition under the same DR97 key.
  The primary locators above are not transferred to that version.
- The publisher record and author-hosted material were inspected in a bounded search.
  The comparison did not establish an author-issued correction of the findings below.
  U005 states the pages and search scope actually checked.

## Findings and Corrective Arguments

These identifiers classify audit findings, including omitted hypotheses, false literal assertions, and compressed steps needing explicit justification.
They are **not author-confirmed errata**.
Each repaired argument is in its authoritative unit.

| ID | Source issue and consequence | Repair and affected units |
| --- | --- | --- |
| F01 | The alphabet is initially unspecified, but p. 618 uses finite $X$. Theorem 2's recognizability/rational-expression equivalence is false for arbitrary infinite alphabets under finite-expression closure. | State finite $X$ throughout the audited chain. U001 gives the two-state series $\sum_xx$ as a counterexample to that broader preliminary reading. U005 identifies further uses of finiteness. |
| F02 | The p. 618 injectivity sentence cannot mean multiplication by $\bar x-1$ on all group coefficient functions: a bilateral series on $\langle x\rangle$ is a counterexample. | U002 proves injectivity on the actual residual span, where appending $\bar x$ causes no cancellation, using its least nonzero degree. The finite residual bound follows. |
| F03 | Pp. 613 and 619 treat general $\ell^2$ coefficients as everywhere-defined convolution operators; boundedness does not follow from square summability. The p. 613 norm notation also omits a square root. | U004 initially uses finite-support inputs, establishes boundedness by normal convergence, and supplies an explicit nonrational $\ell^2(\mathbb Z)$ counterexample to the general boundedness claim. Conventional Hilbert norms are stated. |
| F04 | The p. 619 application of Lemma 8 misidentifies the commutator's ambient algebra; the source representation also has a nonunital scalar block. | U003 uses the algebraic quotient $B(H)/\operatorname{Fin}(H)$, where the representation is unital and its commutator derivation has the right bimodule type. Finite rank is not replaced by compactness. The historical separate algebraic-domain scalar-block treatment remains part of the unlocated Section 4 body; current U005 owns its external interfaces. |
| F05 | Lemma 10(ii)'s contraction estimate fails for polynomial shifts; the printed decay estimate also carries an unjustified unchanged exponential rate from squared coefficients to operator norms. | U004 inserts the finite factors $\|P\|_1\|Q\|_1$ and derives $\|a_m\|\leq\sqrt M(m+1)c^{m/2}$. Both corrections preserve the required normal convergence. |
| F06 | Lemma 11's diagonal Schur formulas on p. 620 have misplaced inverse parentheses. The subsequent decay step cites Lemma 11(i) where Lemma 10(i) supplies the needed estimate. | U004 gives correctly ordered block formulas, a sufficiently-small-power scalar-pivot proof, and the corrected logical reference. Invertibility of a matrix is not assumed to imply arbitrary unpermuted pivots are invertible. |
| F07 | Section 4 compresses inverse commutators and formal-to-group substitution without specifying a common composition domain or all support/pivot conditions. | The historical audit reports a construction on $D\oplus D^X\oplus k$, support preservation, scalar-projection inverse correction, finite polynomial substitution and permuted elimination. Its detailed local body is not located in the current five units; U005 checks the external foundation only. This is a location gap, not a counterexample to Theorem 12. |
| F08 | The bibliography's reference [8] gives a misleading journal/year for Fliess's *Matrices de Hankel*. | U005 records the bibliographic discrepancy and actual evidence depth. U001 reconstructs the field interfaces locally, so no uninspected Fliess erratum or corrected proof is silently imported. |

All downstream uses within this audit are indicated by the unit links.
No pre-existing project claim depends on these new units, and no project claim ID, research route, or ledger theorem is allocated by this source study.

## Proof Obligations and Dependencies

| Conclusion | Forward construction and decisive input | Boundary or checked interface |
| --- | --- | --- |
| Proposition 5 | Edge cancellation gives suffix residuals multiplied by a fixed letter difference; restricted injectivity and finite $X$ give finite residual span. | U001 finite-alphabet field theorem; no multiplication of two arbitrary group coefficient functions. |
| Lemma 10 | A finite representation makes the squared-coefficient generating function rational; summability excludes poles on the closed disk; Cauchy estimates and Haagerup give normal convergence. | U005 checks the homogeneous Haagerup statement; the rational-decay step is proved locally without reliance on a vague Kronecker citation. |
| Proposition 9 | Minimality makes every matrix coefficient series a finite combination of residuals and zero on nonreduced words; powers specialize to exact homogeneous parts; a small power permits scalar inversion. | No unrestricted substitution of infinite word series, no prior boundedness assumption, and no jump from matrix to scalar closure. |
| Theorem 7 | Group polynomials have finite-rank defects; the repaired derivation preserves this under all matrix inverses. Conversely Proposition 5 plus Proposition 9 realizes every finite-rank element in scalar closure. | Equality of coefficients determines a bounded regular operator by right translations. Neither inclusion assumes the desired equality. |
| Theorem 12 | Inverse closure preserves finite rank on the specified Malcev-Neumann space. Conversely residual representations preserve well-ordered support and give a matrix inverse over the division closure. | U005 accepts the exact ordered-series field construction; the optional identification with a universal free field is a separate interface. |
| Corollary 13 | Finite positive generators make the positive free monoid well ordered by the supplied subsequence argument; restrict a doubled-alphabet representation to positive letters. | Positivity is needed for embedding all positive formal series, but is not needed for Theorem 12 itself. |

The dependency graph is acyclic: U001 supplies the common formal machinery; U002 supplies the algebraic criterion; U004 constructs the analytic realization; the separately reported Malcev-Neumann realization body remains unlocated; U003 combines U002 and U004 with the independent closure direction.
U005 documents external interfaces and comparisons.
The Malcev-Neumann proof does not assume an analytic norm theorem.
The historical Section 4 verdict is preserved as that earlier review account; present reuse of Theorem 12/Corollary 13 needs the reported support/inverse/substitution/pivot body to be located or adequately prepared, without retroactively extending the current external-interface U005.

## Reuse Guidance

For a free-group problem, cite the exact unit and retain finite $X$, the coefficient field, the ambient algebra, and the source's scalar/matrix closure convention.
For a semicircular problem, consult U005's comparison with [Miy22](../../../literature/pdf/Miy22.pdf): the shared residual/realization mechanism does not identify their generators, bases, commutators, or affiliated domains.
Neither DR97 nor this audit automatically supplies a theorem about all affiliated operators.

The original free-field identification, where desired, must be cited through its separately checked interface.
The criterion characterizes the division subring generated by the free group inside the Malcev-Neumann field; no identification of that subring with the entire ambient field is asserted.
No novelty or present-day open-problem assessment is made.

## Verification Facts

| Activity | Actual evidence and limits |
| --- | --- |
| Source inspection | All ten primary DR97 pages read; the coordinating agent visually inspected all ten rendered pages, and content agents independently inspected their assigned formula pages. Primary artifact unchanged. Supporting sources and the author version have only the passage-level coverage recorded in U005. |
| Local mathematical reconstruction | U001-U005 contain the proof mechanisms, explicit repairs, and boundary cases. The coordinating agent reviewed the complete analytic and Malcev-Neumann drafts against the relevant rendered source pages. |
| Independent AI cross-review | the analytic reviewer checked U001's residual/inverse/minimality proof and U005's domain/support/pivot/corollary chain. the Malcev-Neumann reviewer checked U002's identity, injectivity, rank, and scalar column, and all U003-U004 local analytic and closure steps. Exact scopes are also in the unit records. This is review within one AI team. |
| Computation | Exact word-action check: 78,185 equalities passed for the specified finite ranks and word lengths, including 1,892 nonzero edge-defect cases. No analytic estimate or general rationality theorem is certified by the run. |
| Artifact checks | Local Markdown links and anchors, six unique source-unit anchors, English-language/trailing-whitespace checks on new records passed. `git diff --check` reported no whitespace errors. These checks do not replace mathematical review. |
| Formal verification | Not performed; no proof-assistant artifact or trusted-axiom audit. |
| External review and priority | External human review, publication of corrections, and a novelty/priority assessment were not performed. |

## Goal Completion Review

Target: [DR97 rational-series source audit](#dr97-rational-series-source-audit), the user-assigned source audit.
Artifact: this dated integrated record, six units, the finite computation.
The contract requires a source audit with accurate boundaries, not a proof of every supporting monograph or an unassigned new theorem.

**Outcome: DR97 rational-series source audit's source-audit criteria are met, 2026-09-08.**
The analytic reviewer independently compared the six units, integrated proof map, findings, source/version records, computation, and original contract.
The coordinating agent performed final integration and artifact checks.
The review found no unresolved local mathematical obligation within the explicitly recorded finite-generator, field-coefficient scope.
The broader preliminary statements and original external proofs retain their declared inspection limits.

| Original acceptance criterion | Completion evidence |
| --- | --- |
| Identity, version, and searches | Primary title page and all ten pages inspected; the author edition is separately identified; U005 records the bounded searches and selected comparison. |
| Stable units with precise hypotheses and locators | The retained U001--U005 cover formal series, the tree criterion, analytic realization and external interfaces. The historical six-unit account included a separate Malcev-Neumann construction whose current detailed home remains unlocated. |
| Local proof reconstruction and justified corrections | U001-U005 supply the explicit arguments; F01-F08 identify findings and consequences. Complementary agents independently inspected the critical algebraic, analytic, domain, and boundary steps. |
| Accurate evidence and trust boundaries | U005 distinguishes primary statements, a published foundational exposition, original-proof limits, and secondary bibliography evidence. The computation record separates its finite checks from universal proofs. |
| Integrated review and project handoff | Independent contract comparison and coordinating-agent review completed; source-unit index, goal index, audit navigation, computation index, and current assessment updated. No unassigned theorem-discovery objective was created. |

The historical independent computation review reports rerunning the script and reproducing all 78,185 equalities.
The native program/J locator remains unlocated as stated in U002; no current reproduction is asserted.
Its 77,688 endpoint/suffix comparisons test two distinct calculations; the 497 auxiliary scalar-column checks have the weaker independence described in the computation record.
Neither count certifies the general rationality conclusions.

During integration, the reviewer flagged an unnecessarily strict comparison between the full Malcev-Neumann field and its generated division subring, which would fail for the included empty-generator case.
The reuse guidance was corrected to state only the actual characterization.
The analytic unit's direct square-summable convolution counterexample was sharpened to show failure to map all of $\ell^2$ into itself, rather than merely absence of a bounded extension.
Both elementary corrections were checked by the coordinating agent before completion.

The static validator ignored fenced code and inline-code examples and checked actual relative file links and anchors.
The pre-completion run covered 35 Markdown files and 368 local links without errors; final added navigation was rechecked after the completion update.
This closes a source-study goal, not a claim that all original source proofs or all possible generalizations have been independently certified.

## Revisions

- 2026-09-08: initial six-unit source audit; primary DR97 artifact preserved; F01-F08 record repairs and limitations.
  Supporting primary statements and a scoped author-version comparison are documented separately.
  No new project theorem is claimed.

<a id="historical-contract-v1"></a>
<a id="dr97-rational-series-source-audit"></a>
## DR97 rational-series source audit: Audit DR97 as a Reusable Research Input

Origin and authorization: user-assigned on 2026-09-08, requesting an audit of the registered DR97 in this repository.

### Original Question

Read and audit [DR97](../../../literature/pdf/DR97.pdf), *Un critere de rationalite provenant de la geometrie non commutative*, and organize its statements, hypotheses, local proofs, dependencies, corrections, and limitations into reusable mathematical inputs.

### Scope and Exclusions

Cover the complete ten-page published article, pp. 613-622: formal rational series; the Cayley-tree finite-rank criterion; reduced group C*-algebra closures and analytic realization; and the Malcev-Neumann criterion and its formal-series corollary.
Check its relationship with the already audited Miy22 where relevant.

Inspect critical external interfaces as needed, distinguishing primary-source checks from secondary reports.
A full audit of every reference, a new project theorem, an exhaustive later-literature survey, a manuscript, and formalization are not required.
A completed source audit may retain precise objections or external-proof boundaries; completion does not certify every theorem from first principles.

### Notation and Conventions

Specify the generator set, coefficient field, free group, doubled alphabet, reduced-word section, and the different products on word series and group series.
Separate algebraic maps from finite-support vectors to all coefficient functions, bounded Hilbert-space operators, and Malcev-Neumann multiplication.
Explicitly track finite-alphabet assumptions, scalar inverse closure versus matrix inverse closure, and analytic versus coefficientwise summation.

### Completion Criteria

1. Recheck source identity, exact version, and printed/PDF page mapping; record searches actually performed.
2. Supply stable source units with exact locators, hypotheses, notation, source links, and dependencies covering the stated scope.
3. Reconstruct the local proof chains, inspect key formulas in rendered pages, and record concrete objections with justified repairs or explicit unresolved limits.
4. Distinguish source statements, local proof review, accepted primary-checked inputs, secondary dependencies, computations if any, and unexamined matters.
5. Complete an integrated scope/dependency review and update the source-unit index, goal index, audit navigation, and current assessment.

### Related Records

- [Integrated source audit and completion review](#goal-completion-review).
- [Source-unit registry](../index.md).
- [Goal state and completion evidence](../../../tasks/index.md).

### Contract Changes

- 2026-09-08: initial user-assigned scope recorded.
  DR97 is the distinct Duchamp-Reutenauer paper already registered at intake; this goal does not reopen the historical Reu96 filename correction.
