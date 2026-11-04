<a id="yin-source-edition"></a>
# Yin20: Chapters III and IV

Author: Yin

Source: the supplied [Yin20 dissertation](../../../literature/pdf/Yin20.pdf).
Goal: [Yin20 inner-rank source audit](#yin20-inner-rank-source-audit), explicitly assigned on 2026-09-10.

## Artifact and Coverage

The source has 109 PDF pages, with printed Arabic pages offset by ten PDF pages.
The requested Chapter III covers printed pp. 37-48 / PDF pp. 47-58; Chapter IV covers printed pp. 49-62 / PDF pp. 59-72.
The chapter boundary and all subsection headings were checked against the table of contents and actual pages.
No source PDF is edited or replaced.

Current state, 2026-09-10: all 26 assigned pages have been read, their mathematical arguments reconstructed, and all three new units independently reviewed.
This is a complete audit of the two requested chapters, with the external foundations explicitly retained below; it is not a whole-dissertation audit.

| Unit | Scope | Printed / PDF pages | Author; complete independent reviewer |
| --- | --- | --- | --- |
| [Yin20-U001](Yin_U001.md#yin20-u001) | Preserved earlier division-closure definition and recursion | 60 / 70, with stated adjacent context | the coordinating agent; historical selected self-review |
| [Yin20-U002](Yin_U002.md#yin20-u002) | Complete Chapter III: inner rank, Sylvester domains, linear matrices and central eigenvalues | 37-48 / 47-58 | another AI agent; another AI agent, concluding review section |
| [Yin20-U003](Yin_U003.md#yin20-u003) | Chapter IV introduction and IV.1-IV.3: expressions, free field and linear representations | 49-56 / 59-66 | another AI agent; the coordinating agent, Section 9 |
| [Yin20-U004](Yin_U004.md#yin20-u004) | IV.4-IV.5: evaluation, rational closure and division closure | 56-62 / 66-72 | another AI agent; another AI agent, Section 9 |

The overlap at printed p. 56 preserves the transition between representations and evaluation.
Printed pp. 48 and 62 are blank versos and were inspected as part of this coverage.

## Accepted Proof Chain and Corrections

The algebraic chain is: the free algebra's weak algorithm supplies its Sylvester-domain structure; inner-rank factorization and a rank-preserving free-field embedding then support full linear representations; corrected recursive operations produce these representations while preserving an existing ambient evaluation domain; rank preservation proves evaluation consistency; the closure arguments finally identify rational and scalar division closures when the same-ambient division-ring premise holds.
The central-eigenvalue bound uses the algebraic embedding, without relying on a later analytic realization theorem.
Every Schur calculation requires its pivot to be invertible in the algebra in which that calculation is performed.

The complete units give proofs and local locators for all corrections; the consequential findings include the following.

- Chapter III's statements about the rank of scalar matrices and central eigenvalues in an arbitrary overring require a stable-finiteness qualification; invertibility need not imply fullness in an arbitrary ring.
- The rectangular Sylvester proof needs the stated block-dimension repair and correct left/right multiplication order; the full-submatrix conclusion refers to square submatrices.
- Chapter IV's rational-expression circuit needs acyclicity, and overlap agreement over an arbitrary algebra is not transitive; U003 supplies an explicit unilateral-shift example and separates the valid free-field construction.
- Algorithm IV.3.4(iii), printed p. 56, omits a minus sign in the inverse representation; the same sign issue recurs in the inverse expression on p. 59.
- The evaluation-consistency proof, printed p. 58, cannot apply the Schur rank theorem directly in the polynomial algebra when the pivot is merely full; the repaired proof computes rank in the free field and returns through rank preservation before evaluating a polynomial factorization.
- The division-closure citation mixes versions: the published Rei06 result is Proposition 4.9 and the following remark, printed p. 122; Proposition 13.15 and Note 13.16 occur in the inspected title-page-1998 dissertation, printed p. 103.

These are internal audit findings, not author-confirmed errata.
No unresolved correction remains in the assigned proof chains after the explicit repairs and accepted foundational inputs.

## External Inputs and Inspection Boundaries

The units retain Cohn's weak-algorithm and semifir foundations, the positive Sylvester result for two commuting indeterminates, the matched-degree factorization lemma, and universal localization as established algebraic inputs with their hypotheses and applicability checked.
U002 uses the previously primary-checked Coh06 locators for weak algorithms, full submatrices and Schur rank, and the matched-degree statement at printed p. 316.
U003 freshly checks the primary text of Theorem 7.5.13, especially clauses (a), (b), (e), (f), and the specialization framework at printed pp. 419-422, with the theorem on p. 450.
It reads the relevant proof while retaining its declared earlier book dependencies; this is not a complete Cohn-book audit.
The source's Ami66 and KV12 citations remain historical construction references, not freshly audited originals or prerequisites for the independently reconstructed recursive representation argument.
U004 directly checks the selected published Reich result and the dissertation locator; neither entire external work is audited.
Canonical bibliographic identities are in [references.bib](../../../literature/references.bib).

## Integration and Research Follow-Up

The fresh attempt produces Yin_C_F0028: on the starred polynomial core, vacuum adjoints, dual relations and bounded starred-generator commutators suffice for a complete finite-rank criterion for bounded functions of one normal coordinate.
The proof establishes atomlessness by bounded regularization, obtains a rational divided-difference kernel from the weak form, cancels scalar polynomial poles on the spectral support, and only then invokes the domain-preserving inverse calculus.
For one normal generator this also proves the equality of bounded affiliated-field elements, bounded rational closure and bounded division closure; the commutator rank is the reduced rational degree.
The complete independent proof review owns the exact inspected argument and accepted scope.

For general jointly dependent functions, the source audit supplies no implication from bounded scalar affiliated output to a bounded inverse representation.
The same-ambient requirement persists through Schur complements, linearization and the division-ring closure theorem.
The earlier account reports a counterexample under former Yin_C_F0012 and reviewed statements under former Yin_C_F0025--Yin_C_F0027; their original fixed proof/review homes remain unlocated in the current retained F-family collection.
Those reports supply no currently reusable project obstruction or reviewed theorem here; the general small-core converse remains open.

## Goal Completion Review

Date and integration reviewer: 2026-09-10, the coordinating agent.
The coordinating agent read every assigned source page in extracted text and every complete reconstruction, followed the cross-review corrections, and checked the combined proof chain and retained input boundaries.
Rendered checks include the full Chapter III by its author, all of IV.4-IV.5 by its author and independent reviewer, the consequential expression/representation pages by the U003 author, and the coordinating agent's additional checks of the circuit and specialization diagrams on printed pp. 51 and 53 and the rank and Schur arguments on pp. 58 and 61.
Each independent review discloses preliminary contributions and distinguishes accepted external statements from freshly reconstructed proofs.

Yin20 inner-rank source audit's five criteria are satisfied: artifact and pagination verified; all 26 pages covered by stable units; consequential formulas and local repairs checked with explicit external boundaries; all units independently reviewed with an acyclic integrated proof chain; and a fresh research attempt recorded as Yin_C_F0028 with complete independent review and synchronized project records.
Completion concerns the assigned source audit and subsequent attempt, not resolution of Yin_T_F0001's remaining general problem.

Each review records the pre-append mathematical body it actually checked.

### Independent Integration Review

On 2026-09-10, another AI agent independently reviewed this complete integration page at pre-append against Yin20 inner-rank source audit's exact contract, the three completed source units and their appended reviews, and the Yin_C_F0028 statement and complete proof-review record.
The coverage accounts for all 26 distinct assigned PDF pages, including the shared p. 66 boundary and blank pp. 58 and 72.
The reviewer identified the earlier index-only locator typo for Algorithm IV.3.4(iii); the reviewed version correctly says printed p. 56.

The integrated dependency chain is acyclic: the Sylvester and universal-localization foundation supplies the rank-preserving free field before the central-eigenvalue and evaluation-consistency deductions use it.
The corrected recursive construction preserves an existing expression domain in the same ambient algebra, and the Schur and closure statements retain that ambient throughout.
The external-inspection summary matches the units' distinction between previous primary checks, fresh selected Cohn passages, selected Reich text comparison, and retained original proofs.
The source, proof, goal and route registry entries inspected for this integration agree with that scope.

Yin_C_F0028's reported criterion concerns bounded functions in a single coordinate algebra; its affiliated-intersection equality is restricted to one normal generator.
Its rank statement uses the maximum of the reduced numerator and denominator degrees, with constants assigned rank zero.
The index correctly leaves the general Yin_S_F0011 problem open and does not equate completion of Yin20 inner-rank source audit with resolution of Yin_T_F0001.
This integration review accepts the fidelity of that summary to Yin_C_F0028 and its existing complete independent review; it is not a second complete mathematical proof review of Yin_C_F0028.

Contribution disclosure: this reviewer authored U003 and independently reviewed U004, so the present review concerns the combined coverage, dependencies and completion claims rather than claiming independent authorship-free discovery of every component.
Outcome: accepted as a completion record for the assigned chapter audit and subsequent restricted research attempt, with the stated external foundations and remaining general problem preserved.

<a id="historical-contract-v1"></a>
<a id="yin20-inner-rank-source-audit"></a>
## Yin20 inner-rank source audit: Audit Yin20 Chapters III and IV

Origin and authorization: user-assigned on 2026-09-10, with an explicit request to retry the current research question after the audit.

### Question and Scope

Audit Chapter III, Inner rank, printed pp. 37-48, and Chapter IV, Free field, printed pp. 49-62, of the supplied Yin20 doctoral dissertation.
The corresponding PDF pages are 47-72.
Read every page in this interval, reconstruct the arguments and their hypotheses, and check necessary external interfaces at their stated depth.
The earlier Yin20-U001 definition audit remains a separate preserved record.

Pay particular attention to same-ambient inversion, Schur complements, rank factorizations, rational-expression domains, linear representations, and rational versus division closure.
Reconsider the proposed bounded inverse representation inference against the actual thesis proofs and the earlier reported counterexample, whose original project proof remains unlocated, rather than assuming either previous assessment settles the new source review.
After the chapter audit, use its mechanisms in a fresh attempt on the small-core dual criterion under the existing Yin_T_F0001 authorization.

### Completion Criteria

1. Verify the supplied artifact, chapter boundaries and printed/PDF pagination.
2. Read all 26 pages in the two chapters and record stable source units covering all definitions, assertions and proof chains.
3. Inspect consequential rendered formulas, resolve local errors or state precise remaining qualifications, and identify retained external theorems without claiming their entire proofs were audited.
4. Obtain independent reviews of the chapter reconstructions and check their combined dependency chain.
5. Record a fresh research attempt and its outcome, synchronize affected records.

The source-audit goal does not require a proof of the unresolved Yin_T_F0001 small-core equivalence, an audit of the whole dissertation, a formalization, or a historical-priority claim.

### Related Records

- [Chapter audit index](readme.md).
- Small-core route Yin_S_F0011.
- Earlier MSY23 source recheck.
- Yin_C_F0028 new one-coordinate criterion and its complete independent review.

### Completed Outcome

Completed on 2026-09-10 at the stated two-chapter-and-retry scope.
The [source completion review](#goal-completion-review) checks all five criteria and records the three independently reviewed units, source corrections, retained external inputs, rendered inspections and their actual inspected mathematical scope.
The subsequent research attempt proves Yin_C_F0028, extending the complete one-normal-coordinate criterion to polynomial-core duals with bounded starred-generator commutators and proving actual closed-domain invariance and the exact rank formula.
The general bounded inverse representation inference remains invalid, and Yin_T_F0001's general small-core converse remains open.
Artifact-consistency checks are recorded in the current status independently of mathematical review.

### Contract History

- 2026-09-10: registered the explicit two-chapter audit and subsequent research attempt; work in progress.
- 2026-09-10: completed the original source-study contract after all three source units and the new Yin_C_F0028 proof passed complete independent review; the remaining general research belongs to the still-active Yin_T_F0001.


<a id="presentation-observations"></a>
## Definition and explanatory-remark observations

The selected reading recorded 2026-09-10 covered printed pp. 59–60 / PDF pp. 69–70, especially Definition IV.5.5 and Remark IV.5.6.
A concise defining property is followed by a remark relating it to nearby closures and a finite operational construction.
The [complete scalar division-closure account](Yin_U004.md#61-definition-iv55-and-all-parts-of-remark-iv56) retains the ambient algebra and every allowed inverse, with the stage-union characterization proved separately.
The [matrix rational-closure account](../MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra) keeps scalar inversion distinct from entries of inverse matrices.
The explanatory consequences are not additional definition clauses.
The dissertation's chapter scale is not a prescribed length for a journal article, and this selected reading adds no whole-dissertation proof inspection.
