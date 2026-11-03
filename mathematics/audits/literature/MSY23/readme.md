<a id="yin-source-edition"></a>
# MSY23 / MSY23: Free-Field Realization and Atiyah Property

Author: Yin

Source: [MSY23.pdf](../../../literature/pdf/MSY23.pdf), the user's supplied published version of the registered work MSY23.
Goal: [MSY23 free-field and Atiyah source audit](#msy23-free-field-and-atiyah-source-audit).
Reading and unit reviews: 2026-09-08; integration: 2026-09-09.

Coverage: **the complete 50-page published article has been read and audited in six units**.
Local proofs have complementary independent AI reviews, with corrections and retained external inputs specified below.
The earlier selected arXiv statements remain separately recorded in [Miy26-U008](../Miy26/Yin_U008.md#miy26-u008).
Completion of this source audit does not resolve Yin_C_F0001.

## Artifact and Coverage

<a id="universal-derivation-source-check"></a>
Universal-derivation follow-up, 2026-10-11: directly checked [Wod08](../../../literature/pdf/Wod08.pdf), Section 1.1.7, pp.15--16, Lemma 1.11 and Proposition 1.13.
For a unital complex algebra U and its outer tensor bimodule, I=ker(mu:U tensor U -> U) and delta(u)=u tensor 1 - 1 tensor u satisfy the universal factorization property for complex-linear derivations into unital U-bimodules.
The source uses d=-delta; the induced factorization changes sign accordingly.
The source has a harmless ambient-space typo before Lemma 1.11 (I is a sub-bimodule of U tensor U).
Its formulas and proof use the correct ambient space.
In the bar resolution of U, the degree-one differential satisfies partial_1(1 tensor u tensor 1)=delta(u), and im(partial_1)=I.
Restricting the middle tensor factor to a specified subalgebra A_X of U, with U as both outer factors, need not retain all of I as the image.
A restricted-image rationality criterion is therefore not an automatic consequence of the full bar resolution.
Selected definition and proof/formula self-review only, not a full Wod08 source audit.

<a id="hochschild-source-check"></a>
Hochschild terminology follow-up, 2026-10-11: the published p.13 explicitly calls the finite-rank tuples Hochschild 1-cycles and refers to [18], CS05, for the homological setting; it does not develop the chain-complex identification there.
The coordinating agent directly checked the [author-hosted CS05 preprint](https://alainconnes.org/wp-content/uploads/betti.pdf), arXiv math/0309343v1, 39 pages: Sections 1.1 and 2.2.3 (operator actions), Section 2.3, equation (2.8) (bar boundary), and Section 3.1.1, equations (3.1), (3.6), and (3.8) (generator boundary, commutator identification and finite-rank kernel).
These are preprint locators, not asserted locators in the journal edition.
For the right-multiplication anti-representation rho on tracial L2, the coefficient bimodule action a.S.b = rho(b) S rho(a) gives d_1(sum_i T_i tensor X_i) = sum_i [rho(X_i),T_i].
Thus a tuple with vanishing displayed boundary represents a Hochschild 1-cycle.
This is a selected definition/formula and citation self-review, not a complete CS05 proof audit or a change to the scope of the fixed U002/U006 records.

Subsequent project deduction, 2026-09-10: Yin_C_F0024 extends the bounded-dual mechanism of Proposition 6.2 to dual identities on all bounded vectors.
Common right denominators first move finite-rank ranges into the dual domain; only the resulting bounded finite-rank compositions enter trace cyclicity.
This is an additional proof, not an alteration of the source's bounded hypothesis or the source units' inspected mathematical content.
The source's maximal-Delta/free-field equivalence is reused with its exact scope.
The coordinating agent also rechecked arXiv v2 Theorem 1.1, pp. 3-4, and Definition 6.1/Proposition 6.2, pp. 34-35, for those interfaces on this date.

The subsequent user-requested ACSY24 Proposition 3.5 audit records a smaller-core route to maximal Delta, using bounded regularizations whose commutators converge to the dual relations.
It retains the same MSY23 finite-cycle interface and needs no all-M domain inclusion for this step.
The stronger analytic domain hypotheses used for arbitrary denominator defects in Yin_C_F0024 are a separate issue.

The source has 50 PDF pages, matching printed pages 1-50; 829,348 bytes.
Canonical publication identity is in [references.bib](../../../literature/references.bib).
The supplied article is the audit target; no complete textual comparison with the 37-page arXiv v2 is claimed.

| Unit | Scope | Published pages | Author / independent reviewer |
| --- | --- | --- | --- |
| [MSY23-U001](Yin_U001.md#msy23-u001) | Introduction; inner rank, full linear matrices, central eigenvalues | 1-12 | another AI agent / another AI agent |
| [MSY23-U002](Yin_U002.md#msy23-u002) | Section 3: Delta, finite-rank cycles, linear kernel relations | 12-20 | another AI agent / another AI agent |
| [MSY23-U003](Yin_U003.md#msy23-u003) | Section 4: representations, evaluation, rational and division closures | 20-28 | another AI agent / another AI agent |
| [MSY23-U004](Yin_U004.md#msy23-u004) | Section 5.1: affiliated algebra and free-field realization; p. 36 supplement | 28-34; 36 | another AI agent / another AI agent, including separate supplement review |
| [MSY23-U005](Yin_U005.md#msy23-u005) | Sections 5.2-5.3: spectral regularity, central eigenvalues, strong Atiyah implication | 34-42 | another AI agent / another AI agent |
| [MSY23-U006](Yin_U006.md#msy23-u006) | Example 5.24, Section 5.4, entropy, bounded duals, references | 42-50 | another AI agent / another AI agent |

Overlap at section boundaries is intentional; no page or proof is omitted.
Unit reviews identify the actual block products, kernel transfers, domains and limiting arguments checked.
The coordinating agent also read all six reconstructions and checked their interfaces; agreement is not a substitute for those arguments.

## Main Statements and Proof Dependency Map

Let \((M,\tau)\) be finite tracial with faithful normal normalized trace, \(U=U(M)\), and \(B=\mathbb C\langle X_1,\ldots,X_d\rangle\).
The source allows an arbitrary bounded tuple, without a selfadjointness or normality assumption.
Matrix rank below uses the unnormalized trace.

**Theorem 1.1, p. 4.**
Maximal \(\Delta(X)=d\) is equivalent to injectivity of every evaluated full affine linear matrix, to affiliated invertibility of every full polynomial matrix, to equality of analytic rank and free-polynomial inner rank, and to the unique extension of evaluation to an embedded free field.
Its image is \(\operatorname{Div}_U(B)=\operatorname{Rat}_U(B)\).

The complete proof runs as follows; these are lemma dependencies, not merely unit links:

1. The free algebra's rank foundation and Cohn's matched degree bound give the scalar hollow-block reduction with its exact residual rank (U001, Theorem 2.10).
2. Finite-rank cycles give simultaneous right and adjoint kernel vectors for linear matrices, and conversely.
Induction through the hollow blocks, with finite-trace transfers from adjoint kernels back to the original tuple, proves Theorem 3.1: maximal Delta is equivalent to injectivity of all full linear evaluations (U002).
3. Stable-finite Schur arguments make evaluation consistent on overlaps of representation domains.
Constructive sum, product, inverse and polynomial linearizations establish the representations used in the proof (U003).
4. Polar decomposition in the finite affiliated algebra turns injectivity into affiliated invertibility.
Linear representations then define a homomorphism from the free field; division-ring elimination and rank invariance prove the remaining equivalences and rational-matrix rank preservation in Theorem 5.6 (U004).

**Theorem 1.2 / Theorem 5.25, pp. 6-7 / 43-45.**
The strong Atiyah property is equivalent to the affiliated rational closure being a division ring, and to the affiliated division closure being a division ring.
The associated full-matrix and rank statements use inner rank over the *evaluated rational closure*, which need not be the free field.
A bordered matrix associated with a nonzero rational element has rank \(N+\operatorname{rank}(r)\); integrality forces \(\operatorname{rank}(r)=1\), hence affiliated invertibility.
U006 reconstructs every implication.
Example 5.24 shows why algebraic freeness and the strong Atiyah property alone do not give the free field on the specified generators.

**Spectral consequences.**
Rank preservation identifies central eigenvalues and, for normal rational matrices, atom masses \((N-\rho_F(P-\lambda I))/N\).
Scalar nonconstant selfadjoint rational functions have no atoms.
The bound of N on the number of central eigenvalues uses the corrected eigenprojection lemma in U005.
Its auxiliary free semicircular model is available from Proposition 6.2 and the independent free-field chain above, without invoking the strong Atiyah equivalence or the eigenvalue bound itself.
Thus the cross-links between U005 and U006 do not form a logical cycle.

**Proposition 6.2, p. 47.**
A bounded dual system implies maximal Delta by a trace-class cyclicity argument against arbitrary bounded commutant factors.
It works for arbitrary bounded tuples in the standard tracial representation.
The source uses \([X_i,D_j]=\delta_{ij}P\); negate its duals to match Yin_C_F0001's convention.
This exact interface supports Yin_C_F0005.

## Findings and Repairs

These are local audit findings, not author-confirmed errata.
Precise calculations and rendered-page evidence are in the linked units.

| Finding | Source location | Consequence and verified treatment |
| --- | --- | --- |
| F01 | Introductory prose, pp. 3 and 5 | Strong closure of the holomorphic algebra need not equal W*(X) for normal generators; Haar Fourier modes show the distinction. The matrix no-atoms prose also needs restriction: diag(S,1) has an atom. Later exact theorems do not require these overstatements. U001 records both boundaries. |
| F02 | Theorem 2.10, pp. 10-11 | The cited Coh06 Theorem 5.8.8 concerns full monic reducibility. The matched degree bound in Lemma 5.8.7's proof supplies the required hollow block and extra rank assertion through the reconstruction in U001. |
| F03 | Theorem 3.1, pp. 18-20 | The adjoint-kernel induction is abbreviated. U002 supplies both finite-trace transfers; it never assumes the induction hypothesis at X*. Conjugation on p. 15 is present in the rendered source, not a printing error. |
| F04 | Closure proof and Lemma 4.13, pp. 26-27 | The bordered inverse formula needs an inverse and consistent sign; the displayed Gaussian pivot is a before normalization, not 1. U003 gives correct block formulas and checks their products. |
| F05 | Rank arguments, pp. 32 and 36 | Closed affiliated products require closures of ranges. At an arbitrary rational evaluation, a free-field factorization may introduce undefined denominators. U004 uses a common already-defined pencil and polynomial Schur border; its stronger inner-rank aside additionally uses the identified projection-comparison theorem. |
| F06 | Lemma 5.19, p. 38 | Passing a vector limit through an unbounded operator is not justified as written. U005 instead uses Vandermonde independence of finitely many eigenspaces and rectangular polar decomposition to prove trace additivity. |
| F07 | Proposition 5.18 proof, p. 39 | The rank defect is for P-lambda I, not P. U005 restores the shift and keeps the unnormalized trace. |
| F08 | Proposition 6.3, p. 48 | The terminal-deletion operator has the opposite commutator sign from Definition 6.1. Negating it repairs the source convention; the original deletion operator matches the project's convention. U006 checks every reduced-word case. |

With these treatments, the reconstructed main theorems and stated spectral and dual-system consequences have no remaining local proof gap under the retained inputs.
Normality, selfadjointness, formal involution, scalar versus matrix atoms, and affiliated versus bounded spectrum retain their separate hypotheses.

<a id="accepted-inputs"></a>
## Accepted External Inputs and Review Limits

The units distinguish accepted theorem statements from original proofs that were not recursively audited:

- **Free-algebra foundation:** Coh06 Corollary 2.5.2, Proposition 5.4.6, Theorems 5.4.9 and 5.5.4, and Lemma 5.8.7, with exact primary locators in U001.
The free-field and inner-rank foundation is retained in U003.
Local Schur, degree-block, representation and evaluation consequences are reconstructed; no whole Cohn book audit is claimed.
- **Affiliated-operator foundation:** the algebra of closed densely defined affiliated operators, closure operations and matrix amplification, as identified in U004 and the earlier Miy26 interface.
U004 supplies its own polar, inverse, stable-finiteness and rank arguments.
Its p. 36 supplement accepts AP18 Propositions 9.1.6 and 9.1.8, printed p. 142, for center-valued trace and projection comparison.
The independent review checks normalization and partial-isometry orientation.
This additional input is needed only for the stronger arbitrary-domain inner-rank assertion.
- **Entropy interfaces:** CS05 Lemma 4.1, Theorem 4.4 and Corollary 4.6 give the dimension comparisons; exact primary statements and selfadjoint hypotheses were inspected.
The earlier Voi98 scalar comparison and its named analytic inputs retain their recorded limits.
These entropy foundations are not needed for the bounded-dual proof of Proposition 6.2.
- **Context and optional comparisons:** CS16 Conjecture 5(b), SS15 Theorem 3.4, group-theoretic comparisons and remaining references have the scopes classified in U005/U006.
The reference list was read; all 56 cited works were not audited.
- **Bounded-domain comparison:** HMS18 Lemmas 5.5-5.6 and Theorem 5.7 were checked at the selected primary version and hypotheses stated in U003.
They concern existing expression domains and minimal descriptor realizations, including regularity at zero.
They are not an extra bounded-intersection theorem.

## Search and Version Evidence

The 2026-09-08 targeted searches followed the user's free-field and linearization lead, located the published MSY23 interface and HMS18 realization-domain results, and triggered exact Cohn and entropy-source checks.
The user-supplied published file then became the full audit target.
Published Proposition 4.11 corresponds to Proposition 4.9 in the earlier inspected arXiv version; broader textual identity is not inferred.

On 2026-09-09, a scoped public search combined the exact article title with "erratum correction", and its authors/title with "bounded linear representation inverse".
The [publisher article](https://www.sciencedirect.com/science/article/pii/S0022123623001738), [arXiv record](https://arxiv.org/abs/1905.08187), and [author's description of the revision](https://rolandspeicher.com/2019/05/21/the-free-field-realization-via-unbounded-operators-and-atiyah-property/) confirm the affiliated setting and the shift to maximal Delta for general tuples.
No author-confirmed erratum or theorem establishing the requested bounded-intersection equality was located in that search.
This is a limited search outcome, not a claim that neither exists.
Local repairs do not require indefinite searching for author confirmation.
No private manuscript text was sent to a public service.

<a id="bounded-linearization"></a>
## What Linearization Supplies for Yin_C_F0001

**Subsequent assessment, 2026-09-10:** the paragraphs below preserve the source-audit stage, when bounded representation existence was still an open project obligation.
The later Yin_C_F0012 refutes its universal form even for two selfadjoint generators with bounded duals.
The user-requested [source-domain recheck](Yin_U003.md#bounded-linearization-recheck) and the retained counterexample comparison confirms that Definition 4.5, Theorem 4.4 and Lemma 4.8 concern the chosen ambient evaluation domain, and Proposition 2.3 does not change it.
The counterexample excludes every alternative bounded inverse pencil, not merely an arbitrary nonminimal representation.
This supplement leaves the earlier inspected mathematical content and historical completion review intact.

Set \(F_X=\operatorname{Div}_U(B)\) and \(R_X=\operatorname{Div}_M(B)\).
Under Yin_C_F0001's bounded-dual hypotheses, the audited results identify \(F_X=\operatorname{Rat}_U(B)\) with the free field.

Lemma 4.8 preserves an **existing** matrix-inverse evaluation domain in any unital ambient algebra.
In particular, it characterizes membership in \(\operatorname{Rat}_M(B)\) by a representation \(f=uA(X)^{-1}v\) with an affine linear polynomial pencil and \(A(X)^{-1}\) in a matrix algebra over M.
Proposition 4.11 compares rational and scalar division closures in the **same** ambient algebra under its division-ring hypothesis; Remark 5.10 applies it in U.

Consequently the audited inclusions are

\[
\operatorname{Div}_{M}(B)
\subseteq\operatorname{Rat}_{M}(B)
\subseteq F_X\cap M.
\]

The user's proposed argument would reverse them by two further lemmas:

1. **Bounded representation existence:** from \(f\in F_X\cap M\) and the original hypotheses, construct a representation whose *whole inverse pencil* is bounded.
A fixed arbitrary representation may contain unused singular blocks.
U003's padded constant example only defeats that arbitrary-representation inference; it does not disprove an existence or properly justified minimal-representation theorem.
2. **Bounded scalar descent:** convert such a matrix-inverse representation to the scalar division closure required by Yin_C_F0001.
Applying Proposition 4.11 in U, or silently equating matrix and scalar closure in M, does not supply this step.

The full audit has not proved either new lemma.
Theorem 5.6 controls kernels and affiliated inverses; it supplies no positive lower bound on the singular values of a pencil.
HMS18's checked minimal-realization result starts with an expression already defined in the ambient algebra, so using it to establish bounded-domain membership would require an additional argument.

The user's subsequent Proposition 2.3 suggestion gives a useful additional refinement, reconstructed and separately reviewed in U001/U004 on 2026-09-09.
Every bounded matrix C has the same inner rank over M as over U: from an affiliated factorization C=AB and rectangular polar decomposition A=V|A|, obtain the bounded factorization C=V(V*C).
Thus, if f=uA(X)^{-1}v is bounded, the bordered matrix with blocks A(X), v, u, f has inner rank N in both algebras and admits bounded factors through N columns.
This is a positive bounded-factorization result.
Its polar factors are arbitrary elements of M; their membership in a polynomial or bounded rational algebra remains to be shown.
The bounded-descent problem may therefore also be approached by controlling the algebraic nature of this rank factorization.

Thus the linearization route remains viable as a research proposal, with these exact obligations.
The source audit does not assert its failure or the absence of a known result elsewhere.
Yin_S_F0002 records the next step.
Together with the separate project proof Yin_C_F0005, the established relation remains \(R_X\subseteq S_D\subseteq F_X\cap M\); the proposed intersection equality is sufficient for Yin_C_F0001, not currently proved equivalent to it.

<a id="goal-completion-review"></a>
## MSY23 free-field and Atiyah source audit Completion Review

Coordinating-agent integration, 2026-09-09, compares the original five criteria with the delivered scope:

1.
The exact published edition, pagination and source-version boundary are identified.
2. Six stable units cover all 50 pages, including definitions, proof mechanisms, hypotheses, consequences and the reference list.
3. Ambiguous and consequential formulas were visually inspected where recorded in the units.
F01-F08 give corrections, clarifications and downstream effects.
4. All six unit reconstructions have independent mathematical cross-reviews; the later U004 supplement has its own review record.
The lemma dependency map above covers both main equivalence theorems and the spectral/dual branches, without a circular use of the semicircular model.
5. The bounded-linearization interface is assessed above and linked to the original Yin_C_F0001 route.
Completing MSY23 free-field and Atiyah source audit requires this assessment, not a proof of Yin_T_F0001.

Independent integrated-contract review and final mechanical verification are recorded below when performed.
No numerical experiment, proof assistant, external human review, author-confirmed correction, novelty assessment, or complete audit of every cited source is claimed.

Final coordinating-agent verification, 2026-09-09: the independent contract review below passes, and the later Proposition 2.3 / Theorem 4.4 additions have separately identified mathematical reviews.
All 87 permanent Markdown records passed local file/anchor checks; tracked changes passed the whitespace check.
Goal, source, proof-audit, route and status indexes are synchronized.
MSY23 free-field and Atiyah source audit is completed; Yin_T_F0001 remains active with its original target.
These mechanical checks establish record integrity, not mathematical formalization.

### Independent Integrated-Contract Review

2026-09-09, another AI agent: compared the original MSY23 free-field and Atiyah source audit question, exclusions, conventions and five completion criteria with this index, the six units, their actual review records, and the separate U004 supplement review.
The substantive source-audit deliverables meet the contract; no required mathematical correction was identified.
This review does not certify the final mechanical checks or status synchronization performed by the coordinating agent.

The coverage intervals 1-12, 12-20, 20-28, 28-34, 34-42 and 42-50 cover every published page, including front matter and references; the p. 36 supplement adds a proof repair rather than replacing coverage of another page.
F01-F08 accurately distinguish introductory overstatements, a citation mismatch, expanded adjoint bookkeeping, formula errors and domain repairs.
The records preserve which formulas were actually rendered and do not misclassify the p. 15 extraction loss as a printed error.

The main dependency chain is closed under its declared foundations: the matched-degree hollow reduction supplies the residual rank needed by the finite-rank/kernel induction; both adjoint transfers return to X before induction is used; representation consistency then precedes affiliated evaluation, and polar decomposition precedes the conversion of injectivity to affiliated invertibility.
Theorem 5.25's six-way proof uses the evaluated rational closure, not the formal free algebra.
Its integral-rank Schur argument and the subsequent spectral consequences therefore do not assume the desired free-field conclusion for an arbitrary strong-Atiyah tuple.

The auxiliary semicircular model introduces no spectral cycle.
The elementary word-action identity in [Miy22-U003](../Miy22/Yin_U003.md#miy22-u003), \([r_i^*,s_j]=\delta_{ij}P_\Omega\), gives source-convention bounded duals \(-r_i^*\), independently of Miy22's rationality theorem.
Proposition 6.2 then supplies maximal Delta; Theorems 3.1 and 5.6 realize the free field before U005 uses that model to bound central eigenvalues.
The corrected Vandermonde/polar lemma is independent of this existence argument.
The separate p. 36 review checks every central corner before invoking AP18 projection comparison; its bounded partial isometry does not make the other affiliated factor bounded.

The accepted-input map keeps original-proof limits visible for the free-field, affiliated, projection-comparison and entropy foundations; historical comparisons are not extra premises.
Finally, the bounded-linearization assessment retains exactly two obligations, bounded representation existence and bounded scalar descent.
Neither is asserted proved or disproved.
The padded constant example addresses only arbitrary representations, HMS18 starts from an existing ambient expression domain, and the proposed intersection equality is correctly described as sufficient for Yin_C_F0001.
Completing this source audit consequently leaves Yin_T_F0001 and that research route open.

<a id="historical-contract-v1"></a>
<a id="msy23-free-field-and-atiyah-source-audit"></a>
## MSY23 free-field and Atiyah source audit: Audit MSY23 / MSY23 as a Reusable Research Input

Origin and authorization: user-assigned on 2026-09-08, explicitly requesting a full audit of the supplied MSY23 after suggesting that its linearization methods may resolve the bounded-realization step in Yin_T_F0001.
The established canonical work key remains MSY23; MSY23 is the user's label and retained filename for its published version.

### Original Question

Read and audit the complete [MSY23.pdf](../../../literature/pdf/MSY23.pdf), *The free field: Realization via unbounded operators and Atiyah property*, and explain the exact statements, hypotheses, proofs, external inputs, corrections, and potential use of its techniques for Yin_C_F0001.

### Scope and Exclusions

Cover all 50 pages of the published JFA 2023 article: inner rank and linear matrices; the finite-rank-commutator invariant and kernel arguments; rational-function representations and evaluation domains; rational and division closures; affiliated free-field realization; spectral regularity and central eigenvalues; strong Atiyah equivalences; free entropy dimension and bounded dual systems; and the references needed by these arguments.

Pay particular attention to whether boundedness of an affiliated value u A(X)^{-1} v supplies a representation with bounded A(X)^{-1}, and whether such a representation gives the bounded scalar division closure required by Yin_C_F0001.
Distinguish a theorem already in the source, a locally justified adaptation, and an unresolved step.
Do not assume either success or failure of the user's proposed route.

This is a complete source audit, not an instruction to replace Yin_C_F0001, assert a full proof of Yin_T_F0001, audit every cited book, contact authors, claim novelty, or formalize the paper.
Established external inputs may be retained with exact statement/applicability checks and explicit original-proof limits.

### Conventions

Keep the ambient algebra explicit in every closure and inverse.
Distinguish M, U(M), scalar division closure, matrix rational closure, and evaluation domains over each algebra.
Preserve left/right actions, transpose versus adjoint, complex inner-product conventions, ordinary finite rank versus tracial matrix rank, and bounded versus affiliated invertibility.
Use the supplied published pagination; earlier arXiv unit locators do not transfer automatically.

### Completion Criteria

1. Validate the inspected edition and publication facts, pagination, and selected version differences actually inspected.
2. Provide stable source units covering the entire article, with precise statements, hypotheses, reconstructed proof mechanisms, and external dependencies.
3. Inspect rendered formulas where extraction is ambiguous; resolve consequential errors or record their exact remaining scope.
4. Independently cross-review the local mathematical reconstructions and trace the main theorem's complete dependency chain.
5. Assess the linearization interface for Yin_C_F0001 without substituting a different ambient closure, and update source navigation, goal/status records, and affected research routes.

### Related Records

- [Source audit and completion review](readme.md).
- Yin_T_F0001, the continuing original research objective.
- [Earlier arXiv interface in Miy26-U008](../Miy26/Yin_U008.md#miy26-u008), whose version-specific evidence is preserved.

### Contract History

- 2026-09-08: registered the user's full-audit instruction.
The preceding targeted closure search is preliminary evidence, not completion of this source audit.
Yin_C_F0001 remains unchanged.
- 2026-09-09: completed the full source audit under the original criteria.
The independent integrated-contract review and verification limits are in the linked completion record.
Follow-up readings of Theorem 4.4 and Proposition 2.3 clarify Schur elimination and the inner-rank criterion; they do not change Yin_C_F0001 or assert bounded descent.

<a id="decision-candidate-0001"></a>
<a id="decision-candidate-0002"></a>
<a id="decision-candidate-0003"></a>
<a id="decision-candidate-0004"></a>
## Historical recorded completion

The four historical publications `MSY23 free-field and Atiyah source audit_v1` through `MSY23 free-field and Atiyah source audit_v4` retain one unchanged source-audit disposition: **completed within the original assignment scope**.
The substantive inspection and completion dates remain those stated in the audit and contract above.
The record registration time is 2026-09-14T01:14; it is not a new inspection or inferred historical completion date.

Recorded by: Yin.
Recorded event: 2026-09-14T01:14.
Original transition: no prior recorded disposition to `completed`.
No resumption condition was recorded.

Contract: [original audit assignment, physical v1](#historical-contract-v1).
Selected completion evidence: [Completion review](#goal-completion-review).
Covered materials are this source audit and that assignment.
Original reviewed publication: `MSY23 free-field and Atiyah source audit_v1`.
The evidence basis is the recorded completion review; its actual inspection relationship and limitations remain in the review itself.
No separately declared fixed dependencies or independent review classification is invented.

Recorded scope: The original completion criteria and limitations in the cited completion comparison for MSY23 free-field and Atiyah source audit.
Preserve recorded lifecycle and completion evidence; historical review classification is not inferred.

Recorded reason: Preserve the completed disposition already recorded at registration; this timestamp is registration, not an inferred historical completion date.

Recorded authority: initial recorded disposition in `MSY23 free-field and Atiyah source audit_v1`, preserving the [original assignment and criteria](#historical-contract-v1).
This is a historical account of the retired registration, not a new audit-task lifecycle.

| Historical publication | Recorded update | Meaning of the recording |
| --- | --- | --- |
| `MSY23 free-field and Atiyah source audit_v1` | 2026-09-14T02:10 | Yin, 2026-09-14T01:14: registration; Yin, 2026-09-14T01:25: Repair relative links after Goal-to-Task path migration; contract unchanged. |
| `MSY23 free-field and Atiyah source audit_v2` | 2026-09-14T04:01 | Yin, 2026-09-14T04:01: Register previously selected proof/review support; verified legacy correspondence, no new mathematical audit |
| `MSY23 free-field and Atiyah source audit_v3` | 2026-09-14T14:42 | Yin, 2026-09-14T14:42: Approved framework separation: relocate mathematical material and rebase local documentation locators; preserve mathematics, assessments and historical evidence. |
| `MSY23 free-field and Atiyah source audit_v4` | 2026-09-15T08:24 | Yin, 2026-09-15T08:24: Separate execution metadata from existing Task bodies; preserve mathematical contracts, lifecycle, historical evidence and prior review classification. |

## Bibliographic Display Observed in the Published Edition

The following observations concern the retained Journal of Functional Analysis edition, pp. 49-50.
The complete 56-entry bibliography was inspected as text on 2026-10-16; neither each entry's original publication nor the article's BibTeX source was inspected in that reading.
They describe the published output; they do not identify the authors' original `.bib` fields or `.bst` file, and they are not an adopted bibliography policy.

| Aspect | Observed practice | Examples and limits |
| --- | --- | --- |
| Labels and order | The references have numeric labels [1]-[56] and are broadly grouped by the first author's surname. The displayed sequence is not strictly alphabetical. | [1] Arizmendi precedes [2] Ajanki; [8] Atiyah precedes [9] Belinschi. The grouping does not establish a reliable tie-breaking or sorting rule. |
| Names and titles | Author initials precede family names; commas separate the authors and the title. Article titles generally use sentence-style capitalization; book titles generally capitalize principal words. | Compare journal articles [2], [18], [54] with books [4], [12], [32]. These are output choices, not evidence that full given names or protected mathematical capitalization should be discarded from bibliographic data. |
| Journal articles | The usual order is authors, title, abbreviated journal, volume, an issue when supplied, parenthesized year, and pages or an article identifier. | [2] has volume and issue range; [3] omits an issue. The issue field is not printed uniformly for every entry. Journal names such as J. Funct. Anal. and Invent. Math. are abbreviated. |
| Books and chapters | Book entries give the title and available edition, series/volume, publisher, place and year; a chapter also identifies its containing volume and page range. | [12] specifies a second edition and monograph-series volume; [32] identifies a series and volume; [44] is a chapter with its container and pages. The details supplied vary, so the output should not be read as an exhaustive field requirement for every book. |
| Preprints and other works | Preprints are identified as arXiv e-prints with an arXiv identifier and year. Other categories are identified as lecture notes, a thesis or a conference contribution. | Preprints [1], [41], [45]; lecture notes [6]; thesis [36]; conference contribution [22]. These record the cited editions at publication time, not a rule to retain a preprint description after an edition choice changes. |
| DOI and article numbers | Identifiers supplement an entry when used; their display is not uniform across the list. | [11] is an online-publication-style journal entry with a DOI URL. [21] prints 58 after the year, while [38] prints `24, Id/No 109609`. These different forms do not supply a single article-number format to copy. Most entries do not print a DOI. |
| Information once | The ordinary journal entries present journal, volume, year and pages together once. | The list provides a useful compact model for avoiding a second full journal citation in a trailing note. |

The reusable pattern is a compact entry adapted to the kind of work, with a consistent author and venue presentation.
Numeric labels, journal abbreviations and punctuation are display choices.
The irregular order, the differing article-number formats and publication-time preprint descriptions should not be promoted to universal rules.

<a id="presentation-observations"></a>
## Selected exposition observations

The presentation reading recorded 2026-09-10 covered Section 1, pp. 2–4; Section 4.1, p. 20; Section 5.1, p. 28; and Definition 6.1/Proposition 6.2 and proof, pp. 47–48.
Pages 3–4 were also inspected visually.
Section 1 motivates the mathematical question before the generated-algebra/affiliated-rational setting and explains Theorem 1.1's equivalent formulations after its statement.
Section 5.1 introduces the ambient algebra and operator facts before use.
Proposition 6.2 keeps the ordered calculation and final density argument explicit.
This is a presentation reading, separate from the source units' fuller mathematical inspection.
The [bounded dual-system definition](Yin_U006.md#definition-61-and-proposition-62-the-dual-system-route) has generator-first commutator order; reversing the order negates the duals.
The [free-field interface](../Yin20/Yin_U003.md#3-free-fields-and-the-retained-localization-interface) and [scalar/matrix closure definitions](Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra) do not identify division closure with a division ring without a realization theorem.
The general affiliation definition includes domain invariance; closed algebra operations and their foundational inputs retain their stated limits in U004.
These are formulation/exposition references, with no historical-priority conclusion.
