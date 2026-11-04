<a id="yin-source-edition"></a>
# Reu96 Source Audit

Author: Yin

Source: [Reu96](../../../literature/pdf/Reu96.pdf), the published article *Inversion Height in Free Fields*.
Canonical bibliographic identity is in [references.bib](../../../literature/references.bib).
This audit implements [Reu96 free-field source audit](#reu96-free-field-source-audit).

Audit date: **2026-09-08**.
Reviewers: the coordinating agent; the Section 3 reviewer for Section 3; the Section 4 reviewer for Section 4 and supporting primary interfaces; the reviewing agent for the generic-matrix theorem and Section 5.
Independent cross-review within this AI team is recorded below.

## Outcome and Reading Order

The entire 17-page article was read and organized into six reusable units.
The local proof chain supports the rational tensor-series height characterization, the free-field height characterization under its stronger coefficient hypotheses, the exact height of generic inverse entries, and the real/complex example, with the corrections and external-input boundaries below.

This is a source audit with reconstructed local proofs.
It is not a proof of every imported free-field theorem.
The core representation interfaces from [CR94](../../../literature/pdf/CR94.pdf) were inspected in their primary source and accepted at the scope of [CR94-U001](../CR94/Yin_U001.md#cr94-u001).
The source's separate book inputs on specialization, coefficient extensions, and suitable auxiliary division rings remain explicitly secondhand.
The characterization and lower-bound applications depend on those inputs; the purely local linear-algebra and elimination arguments can be reused at their own stated scope.

| Unit | Reusable input | Printed / PDF pages | Inspection and use |
| --- | --- | --- | --- |
| [Reu96-U001](Yin_U001.md#reu96-u001) | Free tensor rings, inversion height, representations, full matrices, and ordered height structures | 93-98 / 1-6 | Definitions and elementary consequences checked; foundational field construction retained. Read first. |
| [Reu96-U002](Yin_U002.md#reu96-u002) | Rational tensor series, transductions, minimal state spaces, and Theorem 3.1 | 98-101, 105 / 6-9, 13 | Statements and local realization steps reconstructed; accepted CR94 interfaces; elimination supplies the converse. |
| [Reu96-U003](Yin_U003.md#reu96-u003) | Height families, critical-support reduction, invariant subspaces, and Lemmas 3.3-3.6 | 100-105 / 8-13 | Full local height-preservation mechanism reconstructed with the p. 104 repairs. |
| [Reu96-U004](Yin_U004.md#reu96-u004) | Theorem 2.2, translation, minimality transfer, and canonical elimination | 97, 105-107 / 5, 13-15 | Full local transfer and elimination argument reconstructed; specialization remains a cited external input. |
| [Reu96-U005](Yin_U005.md#reu96-u005) | Theorem 2.1: every entry of a generic $n\times n$ inverse has height exactly $n$ | 96-98 / 4-6 | Upper bound, generic pairing, minimality, and height contradiction reconstructed; extension infrastructure retained. |
| [Reu96-U006](Yin_U006.md#reu96-u006) | Real height two versus complex height one; scope of the language analogy | 107-108 / 15-16 | Example reconstructed, including minimality over the auxiliary division ring; existence input and Boolean references retained as secondhand. |

The introduction on pp. 93-96 was read for motivation, scope, and conventions; bibliography pp. 108-109 was checked for dependency identities and locators.
Historical priority claims and every cited language-theory result were not independently audited merely because their references were read.

## Artifact and Version Evidence

- Local artifact: 17 PDF pages, printed pp. 93-109; **printed page = PDF page + 92**.
- The title page identifies Christophe Reutenauer, the 1996 Selecta Mathematica article.
  The user supplied it under the unregistered filename `DR97.pdf` and explicitly approved the correction to `Reu96.pdf`.
  Renaming preserved its bytes.
  The old filename is not an alias for citations.
- The [publisher record](https://link.springer.com/article/10.1007/BF01587940) and [author publication list](https://reutenauer.math.uqam.ca/publications/) corroborate the identity.
  A public author copy was located, but no second version was retained or compared.
  All mathematical locators refer to the supplied artifact.
- The scan has unreliable extracted inequalities and subscripts.
  Rendered pages were used to check the height definitions, critical-support proof, block formulas, diagrams, and concluding example.
  OCR output is not an authoritative source.

## Findings and Corrections

The identifiers below are local to Reu96.
These are audit findings, not author-confirmed errata.
Repairs are given in the linked units, so a future agent need not infer them from this summary.

| Finding | Locator | Issue and justified reading | Affected units |
| --- | --- | --- | --- |
| Reu96-F01 | Equation (3.8), p. 104 / PDF p. 12 | The next-index definition prints $j\ge i$, making $n(i)=i$. Use $j>i$, consistent with (3.2), the earlier matrix definition, and the required positive-height feedback in the star construction. This defining inequality requires correction. | U003, then U002 and U004-U006 |
| Reu96-F02 | Lemma 3.6, step 1, p. 104 / PDF p. 12 | The dependence selects $v_r$, but the deletion is printed as $I\setminus\{k\}$. Delete $r$. The initial-segment argument then preserves every height constraint. | U003 and its consumers |
| Reu96-F03 | Lemma 4.1(ii) proof, p. 106 / PDF p. 14 | The height-zero condition is said to hold for blocks $A,B$; the two diagonal square blocks are $A,D$. The lemma's statement already uses the correct blocks. | U004 and its consumers |
| Reu96-F04 | Theorem 2.1 proof, p. 98 / PDF p. 6 | The zero-entry argument cites (2.2) even when $h(i)=0$. That case uses (2.1); the positive-height case uses (2.2). The lower bound is unchanged. | U005 |
| Reu96-F05 | Section 5.1, p. 107 / PDF p. 15 | Height one is described relative to the complex free-field symbol. The intended base is $\mathbb C\langle x,y\rangle$; relative to the entire field every element would have height zero. | U006 |

Two minor conventions are normalized in the units: the height-zero matrix is unit lower triangular (its off-identity part is strictly lower triangular), and the maximum of a basis height function is taken over the basis, not the whole vector space.
These are separate from F01's necessary inequality repair.

Several compressed steps also required explicit justification: generic nonvanishing via a two-sided tensor-ring automorphism; the left/right minimality criteria; simultaneous regularity of all inverted subexpressions under translation; the coefficient order in $(d^{-1}Q)^*d^{-1}$; and induction on matrix size in Lemma 4.2.
The units supply these arguments or expose the exact external input.
They are not all printed errors.

## Proof Obligations and Dependency Map

| Target | Decisive argument and interface | Boundary |
| --- | --- | --- |
| Theorem 3.1, forward | Star expression → finite height family → height basis → invariant subspace $L(f)$ → minimal representation. Lemma 3.4 orders a reduced basis by critical support positions and preserves all $e(dv)$ cutoffs. | U003 local proof checked; rationality/realization inputs accepted from CR94 Section 2. |
| Theorem 3.1, converse | The proper-matrix specialization of Lemma 4.2: Schur pivots have constant term one and contribute one star only at a highest-height row. | U004 elimination is proved independently of Theorem 3.1. No circular use of Theorem 2.2 is needed. |
| Theorem 2.2, necessity | Translate the chosen rational expression to regular series, replace inverses by proper stars, use Theorem 3.1, transfer minimality via the two-family criteria and comparison embedding, then translate back. | Requires infinite center and infinite dimension over it. CR94 interfaces checked; the separate specialization lemma remains secondhand. |
| Theorem 2.2, sufficiency | Canonical elimination bounds every inverse coefficient by the matrix's height structure; scalar representation vectors have height zero. | Local size induction checked. This direction does not require minimality or the infinitude assumptions. |
| Theorem 2.1 | Legal Schur inverses give the upper bound. Generic pairing gives a minimal representation. A smaller height would force a constant entry of $QGP$, impossible in its independent degree-one tensor summands. | Uses U004 and coefficient-extension/auxiliary-ring infrastructure, some still secondhand. Only nonincrease of height under an embedding is used. |
| Section 5.1 | The displayed expression has complex height one and real height at most two. A hypothetical real height one forces a constant entry of a transformed minimal $2\times2$ matrix, which forces a square root of $-1$ in the chosen $D$. | Ordered cancellations checked; the cited existence of an appropriate $D$ remains secondhand. |

The dependence of U002 on U004 concerns only the independently reconstructed elimination lemma.
U004's necessity direction then uses the completed U002 theorem.
Section 3's arbitrary central-subfield assumptions are not confused with Section 4's stronger hypotheses.

No conclusion here identifies a free field with an operator algebra from Miy22.
The generic-matrix theorem uses $n^2$ distinct variables; the final comments about fixed two-variable height and language algorithms are not results proved in this article.
Their present-day research status was not determined in this audit.

## Searches and Stopping Decisions

All searches below took place on 2026-09-08 within Reu96 free-field source audit.

| Trigger | Action and evidence | Result and stop |
| --- | --- | --- |
| Supplied filename disagreed with title page | Searched the exact article title with Reutenauer and 1996; inspected the publisher record and author publication list linked above. | Identity resolved; user chose the actual PDF and Reu96. No different article was substituted. |
| Need to distinguish source errors from possible corrections | Searched the exact title with `erratum` and with `correction`. | No applicable correction notice was identified in the inspected results. This bounded search does not establish that no erratum exists. No author correspondence occurred. |
| Repeated critical use of Reu96 reference [10] | Searched `"A normal form in free fields" Cohn Reutenauer 1994 pdf`, using author and publisher domains; validated and downloaded the author-hosted CR94 copy. | Exact representation, embedding, and minimality statements and section hypotheses checked in [CR94-U001](../CR94/Yin_U001.md#cr94-u001); original proofs not fully audited. |
| Decide whether to expand further | Compared remaining needs with the source-audit contract and mapped the separate book inputs. | Stopped after primary verification of the critical normal-form interfaces. Broad monograph audits, a later-literature survey, and new two-variable research are not required for this source-audit deliverable. |

Search leads were not promoted to theorem evidence without opening the relevant source.
No duplicate Reu96 download or silent PDF replacement occurred.
A future proof depending on a still-secondhand book interface should inspect that exact interface before promoting it to an accepted primary-checked input.

## Verification Facts

| Activity | Evidence and actual scope |
| --- | --- |
| Source inspection | All 17 Reu96 pages read across the audit team; key formulas and all Section 3-5 proof pages visually checked. CR94 receives only the separate passage-level primary checks. |
| Internal mathematical review | Local proof reconstructions in U002-U006; the coordinating agent checked integration, hypotheses, key source errors, generic pairing, and coefficient order. |
| Independent AI cross-review | the reviewing agent checked U002-U004: critical-support cutoffs, family order, star construction, p. 104 repairs, minimality transfer, and Schur/size induction. the Section 3 reviewer checked U005-U006: generic pairing, tensor-degree obstruction, scalar extension, and the real/complex example. the Section 4 reviewer independently checked U001, source identity, hashes, and the integrated scope/dependency boundary. Exact coverage is recorded in the units. These are independent readings within one AI team, not external peer review. |
| Artifact checks | Repository Markdown links and anchors checked by a local validator; source hashes and byte lengths recomputed; new records checked for English text and trailing whitespace; `git diff --check` passed. See the completion review. |
| Mathematical computation | Not performed. The source arguments were checked symbolically in prose; no finite numerical experiment is used as proof evidence. |
| Formal verification | Not performed; no proof-assistant artifact or trusted-axiom audit. |
| External review and novelty | Not performed. Published source status does not certify these audit repairs, and the audit makes no priority or new-theorem claim. |

## Goal Completion Review

Target: [Reu96 free-field source audit](#reu96-free-field-source-audit), the user-confirmed audit of the supplied Reu96 article.
Artifact: this dated index, six source units, CR94-U001.
Integration and acceptance-criteria review: the coordinating agent.

**Outcome: Reu96 free-field source audit's source-audit criteria are met, 2026-09-08.**
The source-study goal does not require independently proving every cited monograph result; the retained limits qualify mathematical reuse rather than silently broadening the assigned task.

| Original criterion | Completion evidence |
| --- | --- |
| Identity, artifact, and actual searches | Title page and publisher/author records agree; the user confirmed Reu96; source hash and page mapping recorded; rename preserved bytes; bounded identity, correction, and dependency searches documented above. |
| Stable units covering the source | U001-U006 cover definitions, all three main theorems, the invariant-subspace mechanism, and Section 5; supporting CR94-U001 records exactly the primary interfaces checked. |
| Local proof-chain audit and repairs | U002-U006 give the expanded arguments; F01-F05 identify source errors or omitted cases and their repairs. Complementary agents cross-reviewed the series/elimination chain and the generic/real-complex applications; no additional unresolved local implication was found. |
| Honest dependency and verification limits | Primary accepted statements, reconstructed local arguments, and secondhand book inputs are separated. No computation, formalization, external peer review, or novelty result is claimed. |
| Integration and record checks | Source-unit index, goal index, completion-audit index, and current assessment updated. Local Markdown link/anchor checks and whitespace checks passed. |

The local validator excluded literal Markdown examples in code spans and blocks; it checked real relative links, target files, anchors, and the unique authoritative anchors for the six Reu96 units and CR94-U001.
New audit/goal records contain no CJK text or trailing whitespace.
`git diff --check` found no whitespace errors in tracked changes.
At Reu96 free-field source audit completion, filename searches found the former DR97 label only in explicit identity/authorization history, not in a live source link.
A distinct DR97 source was registered subsequently, as recorded below.

Independent integration review by the Section 4 reviewer checked U001, this index, the original Reu96 free-field source audit contract.
It found no material identity, hypothesis, or completion-scope mismatch.
The final index and status edits are maintained by the coordinating agent.
Completion creates no new project theorem or claim ID.

## Revisions and Downstream Effects

- 2026-09-08: initial six-unit audit; supplied-file identity corrected with user confirmation; CR94 added for scoped primary-interface checks.
  F01-F05 and the secondhand infrastructure are explicit.
  No new project mathematical claim, route, or ledger proof is registered.
- 2026-09-08, after Reu96 free-field source audit completion: the subsequently supplied [DR97](../../../literature/pdf/DR97.pdf) was identified and registered as the distinct Duchamp-Reutenauer 1997 article.
  The earlier filename correction in this audit concerns only the Reu96 artifact; it does not rename or audit that later DR97 source.

<a id="historical-contract-v1"></a>
<a id="reu96-free-field-source-audit"></a>
## Reu96 free-field source audit: Audit Reu96 as a Reusable Research Input

Origin and authorization: user-assigned on 2026-09-08.
The initial request named the supplied file DR97.
After its title page identified a different work, the user explicitly chose to audit that PDF under the correct key Reu96.

### Original Question

Read and audit [Reu96](../../../literature/pdf/Reu96.pdf), *Inversion Height in Free Fields*, and organize its definitions, results, proof mechanisms, dependencies, corrections, and limitations into reusable research inputs.

### Scope and Exclusions

Cover the complete 17-page local journal article: free fields and height conventions; the rational tensor-series theorem and invariant-subspace machinery; the inversion-height characterization; generic matrix inverses; and the real/complex example and final methodological discussion.

Inspect necessary external interfaces when they are critical to this audit.
In particular, check the relevant minimal-representation statements in CR94.
This does not require a complete audit of CR94, the cited monographs, or every bibliography entry.
No new free-probability theorem, solution of a later research problem, novelty determination, manuscript, or formalization is assigned.

Completion means a source audit with explicit verification boundaries.
It may identify unresolved external inputs or objections; such boundaries must remain visible and must not be reported as complete proof verification.

### Notation and Conventions

Use finite noncommuting variable sets, a specified coefficient division ring and central subfield, the corresponding free tensor ring and universal field of fractions, and inversion height relative to the stated polynomial ring.
Distinguish expression depth from intrinsic height, formal star height from analytic convergence, and ordered canonical elimination from arbitrary matrix invertibility.

The authoritative conventions are in [Reu96-U001](Yin_U001.md#reu96-u001).
State the infinitude assumptions needed for the characterization separately from the arbitrary commutative-field scope of the generic-matrix theorem.

### Completion Criteria

1. Verify the supplied source's identity and version; record its page mapping and any necessary filename correspondence, and searches actually performed.
2. Provide stable source units covering the listed scope, with exact locators, hypotheses, dependencies, and original-file links.
3. Reconstruct the local proof chain and critical algebraic steps, including the minimization mechanism, elimination bound, generic-matrix lower bound, and coefficient-field example.
   Record concrete source errors and justified repairs.
4. Distinguish primary statement checks, reconstructed proofs, secondhand infrastructure, and unexamined material.
   Preserve any supporting computation actually performed with its scope; computation is optional.
5. Integrate the audit outcome and a completion review, and update the source-unit index, goal index, and current assessment.

### Related Records

- [Integrated source audit](readme.md).
- [Source-unit registry](../index.md).
- [Goal state and completion evidence](../../../tasks/index.md).

### Contract Changes

- 2026-09-08: the user resolved the identity mismatch by choosing the supplied Reutenauer article and approving Reu96 as its key.
  This corrects the file identity; it does not substitute the distinct Duchamp-Reutenauer work for the chosen source.
