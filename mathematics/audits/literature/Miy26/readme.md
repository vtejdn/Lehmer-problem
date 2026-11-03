<a id="yin-source-edition"></a>
# Miy26: Integrated Source Audit

Author: Yin

Source: [Miy26](../../../literature/pdf/Miy26.pdf), the registered 23-page arXiv:2603.19528v2 artifact, dated 2026-04-21.
Canonical bibliographic identity is in [references.bib](../../../literature/references.bib).
This record implements [Miy26 spectral source audit](#miy26-spectral-source-audit).

Audit date: **2026-09-08**.
Reviewers: the coordinating agent (foundations, main theorem, and integration), the spectral-interface reviewer (spectral and external interfaces), the circular-resolvent reviewer (circular resolvents and examples), and the quadratic-case reviewer (quadratic recurrence and spectral-radius cases).
Independent review means complementary review within this AI team; no external human review is claimed.

## Outcome and Scope

The reconstructed local arguments support Theorem 1.1, its spectral Corollary 1.2, the Haar-unitary variant, Corollary 4.2, the homogeneous and free-walk spectral formulas, and the quadratic criterion in Theorem 4.6.
This assessment uses the explicit finite-tracial hypotheses, corrected estimates and displayed formulas below, and the exact accepted external interfaces in U008.
No unresolved local implication remains in these reconstructed chains at the recorded scope.

The main conclusion is that a rational affiliated function of finitely many standard free semicircular variables is bounded whenever it belongs to $L^2$.
The proof does not establish boundedness of arbitrary $L^2$ operators.
Its spectral application detects an existing rational inverse by square integrability.
For holomorphic quadratic circular polynomials, the exact finite-dimensional condition is failure of $Q_\lambda^ne_1$ to tend to zero.
Replacing this by $r(Q_\lambda)\geq1$ is justified in the three cases of Remark 4.7; an unrestricted replacement is not proved.

The complete article was read.
Local proofs, mathematical examples, and the four figure panels were inspected with the boundaries below.
General Brown-support/spectrum equality, random-matrix convergence, every original proof in the bibliography, author-endorsed corrections, novelty, and formal verification are not established by this audit.

## Coverage and Reusable Units

For the primary artifact, **printed page = PDF page**.

| Unit | Content and source locator | Verification depth |
| --- | --- | --- |
| [Miy26-U001](Yin_U001.md#miy26-u001) | Fock, trace, affiliated $L^2$, rational closures and Miy22 inputs; Section 2, pp. 4-6 | Definitions, normalization, core domains, and consumed interfaces checked; standard foundational inputs retained. |
| [Miy26-U002](Yin_U002.md#miy26-u002) | Theorem 1.1 and Lemmas 3.1-3.4, pp. 1, 6-10 | Complete local regularization/residual/decay/boundedness chain reconstructed and cross-reviewed, including explicit corrections. |
| [Miy26-U003](Yin_U003.md#miy26-u003) | Corollary 1.2, Theorem 3.5, Remark 3.6, Proposition 3.7 and Remark 3.8; pp. 1-2, 10-12 | Resolvent and Haar proofs, integrability counterexamples, radius and RD arguments reconstructed; precise external field/intersection inputs accepted. |
| [Miy26-U004](Yin_U004.md#miy26-u004) | Lemma 4.1 and Corollary 4.2, pp. 12-14 | Mixed-word commutators, holomorphic inverse, and both spectral inclusions reconstructed and cross-reviewed. |
| [Miy26-U005](Yin_U005.md#miy26-u005) | Example 4.3, Proposition 4.4, Example 4.5, pp. 14-17 | Coefficients, R-diagonal adaptation, transfer matrix, inverse construction, and all scalar boundary cases reconstructed; specified Brown-support inputs accepted. |
| [Miy26-U006](Yin_U006.md#miy26-u006) | Theorems 1.4 and 4.6, pp. 2-3, 17-19 | All six recurrence blocks and the formal-to-$L^2$ inverse argument reconstructed and cross-reviewed. |
| [Miy26-U007](Yin_U007.md#miy26-u007) | Remarks 1.5 and 4.7, Figure 1, pp. 3-4, 19-21 | Three proved spectral-radius cases, Schur calculation and singular endpoints reconstructed; figure coefficients and evidence limits inspected. |
| [Miy26-U008](Yin_U008.md#miy26-u008) | Exact external inputs and relation to Miy22/DR97; consumed references on pp. 2, 5-6, 10, 15, 17, 22-23 | Identified primary statements and applicability checked, with explicit version and original-proof limits; no recursive whole-source audits. |

The introduction and main-statement repetitions on pp. 1-4 were compared with their proof sections.
The bibliography on pp. 22-23 was inspected to identify the consumed sources.
Introductory reports on general random matrices and other contextual citations retain statement/context coverage rather than independent proof review.

## Artifact and Search Evidence

Its original user acquisition URL and date are unknown.
All 23 pages were extracted and rendered for the audit; the retained PDF, unit locators, and mathematical transcriptions identify the evidence after temporary reading files are removed.

The [public arXiv record](https://arxiv.org/abs/2603.19528) was checked on 2026-09-08.
It lists v2 as the latest revision and describes typo fixes and the addition of Corollary 4.2.
The public v2 HTML was consulted at the disputed quadratic formulas and agrees with the local PDF.
No full v1/v2 comparison, later author-issued erratum, or journal publication was established.
Source corrections below are local audit findings, not purported author notices.

Concrete dependency questions triggered primary-source searches for the free-field realization, canonical square-integrable affiliated operators, the Haar bounded intersection, R-diagonal Brown support, homogeneous cumulants, and the free-walk support formula.
U008 and U005 record sources, inspected passages, version limitations, extraction issues, and stopping reasons.
The six supporting works were consulted online; no local originals are asserted for that reading.
Search stopped once the consumed interfaces and the disputed local steps were resolved.
This is not an exhaustive literature or errata survey.

## Findings and Corrective Arguments

The following identifiers group false literal assertions, displayed errors, necessary scope restrictions, and compressed proof steps.
They do not count independent failed theorems.
The linked units own the full repairs.

| ID | Source issue | Corrective argument and consequence |
| --- | --- | --- |
| F01 | Section 2's factor description on p. 5 is false for one semicircular generator. | U001 uses a finite von Neumann algebra with faithful normal trace. For $d=1$ the algebra is abelian; factoriality is unnecessary for the audited theorem. |
| F02 | Lemma 3.1 and the subsequent coefficient passage compress domains for an initially unbounded $f$; the Haar analogue needs an additional affiliated/bounded bridge. | U002 proves the regularizer identity on the algebraic core and passes coefficients using bounded right multiplication in $L^2$. U003 uses Lin00 and repairs the tree representation's scalar block. Neither proof assumes the desired boundedness or identifies Malcev-Neumann operators with affiliated ones. |
| F03 | Lemma 3.2 says the squared-residual space is spanned by all pair products; equality can fail. | U002 proves the sufficient containment and gives a bounded rational one-generator example with squared-residual dimension one and pair-product dimension two. The finite-dimensional conclusion is unchanged. |
| F04 | Lemma 3.3 chooses the matrix spectral radius itself as an exponential decay rate on p. 9. | Jordan blocks invalidate that choice: $(n+1)2^{-n}$ is a counterexample. U002 takes any $r(B)<A<1$, treats nilpotent/zero cases, and converts squared-coefficient decay to the summable bound $\sqrt M(n+1)(\sqrt A)^n$.
The theorem's existential decay and boundedness conclusions survive. |
| F05 | Theorem 1.3's annulus on p. 2 omits $|\lambda|$; Proposition 3.7's norm estimate on p. 11 prints an equality where only an inequality holds. | U008 restores the modulus. U003 gives the correct degree-growth sandwich, the RD extension's scope, and the Bernoulli example; the spectral-radius conclusion is preserved. A formal recurrence alone does not supply an existing inverse. |
| F06 | Lemma 4.1 has mixed-word indexing errors and suppresses the passage from a square-integrable inverse to a bounded inverse commutator. Corollary 4.2 compresses an inverse inclusion. | U004 first invokes Corollary 1.2, takes residuals over the full mixed alphabet, and proves the creation-operator comparison by invariance of the holomorphic subspace. The result concerns scalar holomorphic polynomials; no free-ball, matrix-coefficient, or arbitrary rational extension is inferred. |
| F07 | Proposition 4.4 abbreviates the homogeneous R-diagonal argument; Example 4.5's quotient and intermediate divisions exclude parameters that its final spectral claim must cover. | U005 checks the color-independent cumulant mechanism against NS06, proves zero Brown inner radius via the vacuum coefficient, and replaces the quotient by a finite geometric sum. It treats $t=0$, $\lambda=0,1$, $|\lambda|=1$, $k=1$, and closure of the strict support region explicitly. |
| F08 | Theorem 4.6's compressed $h$-recursion on p. 18 has the wrong left subscript. | U006 uses $h_{n+1}$; the source's six-state matrix already has the correct index and conjugations. The converse constructs the formal inverse in $L^2$ before invoking boundedness. |
| F09 | Remark 4.7 prints $\sqrt{\operatorname{Tr}|B|}$ instead of $\sqrt{\operatorname{Tr}|B|^2}$ on p. 19 and omits $\|d_1\|^2$ in the symmetric Schur expression on p. 21. | U007 restores both. For $B=\operatorname{diag}(-2,1)$, $d=(3,0)$ and $x=3$, the corrected Schur value is $-7/5$, while the printed one is $17/5$. Its sign/pole proof and rank-one endpoint remain valid after correction. |
| F10 | The notation $\lim Q_\lambda^ne_1\ne0$ can obscure oscillating/divergent orbits; full matrix radius is not automatically the radius detected by $e_1$. Figure 1 is numerical evidence. | U006 defines failure to tend to zero via the invariant cyclic subspace. U007 proves equality of cyclic and full radii only in the three stated cases, verifies that all four figures satisfy one of them, and separates their plots from Brown-support or random-matrix convergence theorems. |

Minor index and symbol corrections are recorded in the corresponding units, including the ascent endpoint in Example 4.5.
The finite computations supplement the counterexamples and identities; they do not establish infinite-dimensional conclusions by sampling.

## Proof Map and Retained Inputs

| Conclusion | Reconstructed mechanism | Input and boundary |
| --- | --- | --- |
| Theorem 1.1 | Bounded rational regularizers give finite core defects; suffix residuals give finite squared-residual and length-shift spaces; corrected exponential decay and the homogeneous norm bound give a bounded operator with the same $L^2$ vector. | Miy22 bounded-intersection/commutator results, the existing reconstructed homogeneous estimate, and canonical tracial affiliation. No use of the later spectral applications. |
| Corollary 1.2 and Haar Theorem 3.5 | In the rational field, inverse square integrability implies boundedness. The Haar proof repeats the regularization on the tree before using DR97's reduced-word realization. | MSY23 free-field property and AP18 affiliation; Lin00 supplies the Haar bounded intersection. DR97 alone does not supply the affiliated theorem. Scalar resolvents are handled separately. |
| Lemma 4.1 and Corollary 4.2 | Vanishing barred-letter residuals put an inverse in the holomorphic subspace. Creation operators are restrictions there; conversely a creation inverse gives an $L^2$ right inverse in the finite algebra. | U003 makes the affiliated inverse bounded; finite trace and canonical multiplication justify inverse identification. Holomorphic and full $L^2$ spaces remain distinct. |
| Homogeneous and free-walk examples | Unique word segmentation gives exact inverse coefficients; finite length-energy recurrence gives summability. Construct the inverse for the converse. | NS06 product-cumulant infrastructure with its specific homogeneous mechanism inspected. HL00 and DHH+25 Brown-support statements accepted at exact hypotheses; their full original proofs unreviewed. |
| Theorem 4.6 | Formal coefficient recursion closes in six states. Decay of the specified orbit is equivalent to summability and hence an actual bounded inverse; zero is treated by the vacuum equation. | U002-U004; no assumption that a formal recurrence already represents a resolvent. |
| Remark 4.7 | Maximal hidden eigenvalues satisfy a four-state auxiliary equation; determinant bounds or the corrected symmetric Schur formula exclude them in the stated cases. | Elementary finite-dimensional linear algebra, explicit zero/singular cases, and participating generalized eigenspaces. General replacement remains outside the proved scope. |

The dependency order is acyclic.
U001-U002 establish boundedness; U003 draws its spectral consequences; U004 establishes the circular interface; U005-U007 apply it.
U008 records the independently accepted external statements.
The free-field property is a theorem used at the indicated points, not part of the definition of division closure.

For reuse, retain the finite number of generators, variance-one normalization, faithful finite trace, scalar coefficients, exact operator domains, and inverse-existence conventions.
The broader R-diagonal remark in U005 concerns R-diagonality only; its circular disk formula is not transferred to an arbitrary R-diagonal tuple.
The previous Miy22 and DR97 assessments remain historical records of their own evidence; newly inspected external statements are recorded here without silently upgrading their entire source audits.
No project claim ID or theorem-discovery route is allocated by this study.

## Verification Facts

| Activity | Evidence and limits |
| --- | --- |
| Source inspection | All 23 primary pages read. The coordinating agent inspected main-theorem and circular formulas visually; content agents visually inspected all assigned circular/quadratic proof pages and the four figures. References and introductory contextual claims have the coverage stated above. |
| Local reconstruction | U001-U007 give the domain, inverse, convergence, coefficient, matrix and boundary arguments. The coordinating agent read all eight completed units and both preserved scripts. |
| Independent AI review | the spectral-interface reviewer checked U001-U002's regularizer, coefficient limit, residual spaces, decay and final identification. the quadratic-case reviewer checked U004-U005, including the primary NS06 mechanism. the circular-resolvent reviewer checked U006-U007, including Schur and zero cases. The coordinating agent separately reviewed U003-U008. This is not external peer review. |
| Exact computation | Circular check: 193,363 checks of the stated mixed-word, holomorphic and product-formula finite cases. Quadratic check: 14,355 state, coefficient, determinant, Schur and boundary checks. Both scripts use only exact standard-library arithmetic and were independently rerun by the coordinating agent; the quadratic script was also rerun by the circular reviewer. |
| Numerical figures | Coefficients, hypotheses, captions and analytic homogeneous radius checked. The original size-3000 Ginibre experiments were not rerun; no seed, source code, or numerical error control was supplied in those passages. |
| External proofs | Precise statements and applicability of the recorded interfaces accepted. The main original proofs of MSY23, AP18, Lin00, HL00 and DHH+25 and the general NS06 product formula were not independently audited. The short MSY23 dual-system argument and the relevant NS06 homogeneous combinatorial proof were inspected. |
| Artifact validation | Repository Markdown links and anchors, eight unique source-unit anchors, English-language and trailing-whitespace checks on all 14 new Miy26 content files passed. `git diff --check` found no whitespace errors; its line-ending conversion notices do not indicate changed source bytes. |
| Formal/external review | No proof-assistant check, trusted-axiom audit, author confirmation, external human review, or publication of corrections performed. |

## Goal Completion Review

Target: [Miy26 spectral source audit](#miy26-spectral-source-audit), the user-assigned source audit of this exact artifact.
The contract requires complete source coverage with honest proof and dependency boundaries; it does not require proving the general Brown-support question or all original external theorems.

**Outcome: Miy26 spectral source audit's source-audit criteria are met, 2026-09-08.**
The independent quadratic-case reviewer compared all eight units, this integration, both computation records, and the original contract.
The coordinating agent completed the artifact checks and navigation updates.
The review found no unresolved local mathematical obligation in the stated scope; the explicitly accepted external theorems retain their original-proof limits.

The final comparison caught an omitted $t\ne0$ qualification in U008's transcription of the strict-sublevel Brown-support formula and clarified that its radial quotient, rather than the full threshold, continues to $1/k$.
Both were corrected; the already separate $t=0$ proof in U005 remains the authoritative boundary argument.
The comparison also aligned U001's starting page and the recorded computation reruns.
These are corrections to the audit records, distinct from the source findings F01-F10.

| Original acceptance criterion | Evidence submitted for completion review |
| --- | --- |
| Identity, version, pagination and searches | Exact local v2 identity, all-page reading/rendering, arXiv history check and scoped primary-source searches. |
| Stable units with exact statements and hypotheses | U001-U008 cover the source's core theorem, spectral consequences, Haar/RD observations, circular examples, quadratic criterion, figures and necessary interfaces. |
| Local proof review and justified corrections | Explicit F01-F10 repairs/restrictions, counterexamples to false literal assertions, complementary mathematical cross-reviews, and actual inverse constructions. |
| Accurate verification boundaries and preserved checks | Two scripts and execution records; exact finite scope; figures distinguished from convergence proofs; original external proofs and contextual citations delimited. |
| Integrated review and project handoff | Independent contract comparison and coordinating-agent review completed; source-unit navigation, goal and completion indexes, audit navigation, computation index and current assessment updated.
No new project mathematical claim or unassigned research route created. |

<a id="historical-contract-v1"></a>
<a id="miy26-spectral-source-audit"></a>
## Miy26 spectral source audit: Audit Miy26 as a Reusable Research Input

Origin and authorization: user-assigned on 2026-09-08, requesting an audit of Miy26 after the completed DR97 source audit.

### Original Question

Read and audit [Miy26](../../../literature/pdf/Miy26.pdf), *The spectra of polynomials in free (semi)circular operators*, and record its exact statements, hypotheses, proof mechanisms, dependencies, corrections, and limitations as reusable mathematical inputs.

### Scope and Exclusions

Cover the complete 23-page local arXiv:2603.19528v2 artifact: the rational L2-to-bounded theorem and spectral corollary; finite commutators and coefficient decay; the Haar-unitary variant and spectral-radius observations; holomorphic circular resolvents and the creation-operator spectral corollary; homogeneous and free-random-walk examples; and the quadratic matrix recurrence and its spectral-radius replacement cases.
Inspect figures and their stated evidential scope.

Use the existing Miy22 and DR97 audits where their exact hypotheses supply an interface.
Inspect additional primary sources when critical.
This does not require proving the general Brown-measure/spectrum question, strong convergence of arbitrary nonnormal random matrix polynomials, auditing every cited monograph, an exhaustive novelty survey, author contact, or formalization.
A completed source audit can retain explicit unresolved objections and original-proof boundaries; it is not universal certification of all cited results.

### Notation and Conventions

Use a finite variance-one semicircular system and normalized trace, with distinct bounded von Neumann, L2, and affiliated-operator spaces.
Define scalar division closure and any imported free-field property.
Track algebraic-core domains in commutator identities and the identification of an L2 vector with its affiliated operator.
For circular variables distinguish holomorphic L2 from the full star-algebra L2 space.
Specify circle/disk boundaries, inverse existence at scalar values, creation-operator conventions, complex conjugation versus transpose, and stability of a matrix on a specified cyclic subspace rather than its entire spectrum.

### Completion Criteria

1. Validate source identity, public version and pagination; record substantive searches and any version comparisons actually performed.
2. Provide stable audit units covering the stated scope with exact locators, hypotheses, proof and dependency details, and source links.
3. Reconstruct local proof chains and inspect rendered formulas; record false literal claims, missing cases, or unresolved implications with justified repairs or precise restrictions.
4. Distinguish imported primary-statement checks, local mathematical review, supporting exact or numerical computation, figure inspection, and unexamined material.
   Preserve meaningful computation scripts and their finite scope if performed.
5. Perform an integrated completion review against this contract and update the source-unit index, goal index, audit navigation, computation index if applicable, and current assessment.

### Related Records

- [Integrated source audit and completion review](#goal-completion-review), completed 2026-09-08 against the original criteria above; no change in the assigned source-study objective.
- [Source-unit registry](../index.md).
- [Goal state and completion evidence](../../../tasks/index.md).

### Contract Changes

- 2026-09-08: initial user-assigned source-audit scope recorded; no new theorem-discovery objective is assigned.
- 2026-09-08: corrected the initial topic label for Corollary 4.2 to its actual statement, spectral equality with creation operators.
  The assigned whole-source audit is unchanged; no separate free-ball result is required.

<a id="decision-candidate-0001"></a>
<a id="decision-candidate-0002"></a>
<a id="decision-candidate-0003"></a>
<a id="decision-candidate-0004"></a>
## Historical recorded completion

The four historical publications `Miy26 spectral source audit_v1` through `Miy26 spectral source audit_v4` retain one unchanged source-audit disposition: **completed within the original assignment scope**.
The substantive inspection and completion dates remain those stated in the audit and contract above.
The record registration time is 2026-09-14T01:14; it is not a new inspection or inferred historical completion date.

Recorded by: Yin.
Recorded event: 2026-09-14T01:14.
Original transition: no prior recorded disposition to `completed`.
No resumption condition was recorded.

Contract: [original audit assignment, physical v1](#historical-contract-v1).
Selected completion evidence: [Source-audit completion review](#goal-completion-review).
Covered materials are this source audit and that assignment.
Original reviewed publication: `Miy26 spectral source audit_v1`.
The evidence basis is the recorded completion review; its actual inspection relationship and limitations remain in the review itself.
No separately declared fixed dependencies or independent review classification is invented.

Recorded scope: The original completion criteria and limitations in the cited completion comparison for Miy26 spectral source audit.
Preserve recorded lifecycle and completion evidence; historical review classification is not inferred.

Recorded reason: Preserve the completed disposition already recorded at registration; this timestamp is registration, not an inferred historical completion date.

Recorded authority: initial recorded disposition in `Miy26 spectral source audit_v1`, preserving the [original assignment and criteria](#historical-contract-v1).
This is a historical account of the retired registration, not a new audit-task lifecycle.

| Historical publication | Recorded update | Meaning of the recording |
| --- | --- | --- |
| `Miy26 spectral source audit_v1` | 2026-09-14T02:10 | Yin, 2026-09-14T01:14: registration |
| `Miy26 spectral source audit_v2` | 2026-09-14T04:01 | Yin, 2026-09-14T04:01: Register previously selected proof/review support; verified legacy correspondence, no new mathematical audit |
| `Miy26 spectral source audit_v3` | 2026-09-14T14:42 | Yin, 2026-09-14T14:42: Approved framework separation: relocate mathematical material and rebase local documentation locators; preserve mathematics, assessments and historical evidence. |
| `Miy26 spectral source audit_v4` | 2026-09-15T08:24 | Yin, 2026-09-15T08:24: Separate execution metadata from existing Task bodies; preserve mathematical contracts, lifecycle, historical evidence and prior review classification. |

<a id="integrability-terminology"></a>
## Integrability terminology in the opening statements

The selected presentation reading recorded 2026-09-10 covered retained arXiv-v2 printed/PDF pp. 1–2, including Theorem 1.1 and Corollary 1.2.
The source calls a rational element with finite L2 norm an L2-bounded rational function.
Its condition is square integrability, distinct from membership in the bounded operator algebra M.
The [ambient-space account](Yin_U001.md#three-ambient-spaces-and-two-closures) retains the rational subalgebra and affiliated realization, with the L2 vector domain and boundedness distinction explicit.
Theorem 1.1 assumes free semicircular generators; a bounded dual system alone is not its stated hypothesis.
Its integrability-to-boundedness assertion and the spectral consequences in Corollary 1.2 are separate results.
The opening motivates the explicit integrability inclusion separately from the bounded division-closure equality.
A preferred replacement term in a manuscript requires the applicable writing choice; these observations adopt no new personal rule.
