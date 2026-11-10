---
author: Yin
---
# Resolve Lehmer's conjecture

## Task coordination

| Field | Value |
| --- | --- |
| joint-task | [Adopted common Lehmer contract](Yin_T_G0002_v1.md#contract) |

Yin's instruction to establish a joint Task for G0001 authorizes this individual Task's adoption of the full common contract.
Participation covers the common question through the formulations, completion criteria and source-use boundaries retained below.
The primitive normalization below preserves that question: for an integer polynomial \(f=c f_0\) with primitive \(f_0\), one has \(M(f)=|c|M(f_0)\), and nonprimitive inputs have \(M(f)\ge2\).
The selected individual decision and its effective execution conditions govern this participation.

<a id="lehmer-entropy-growth"></a>
## Contract

### Original question and authority

On 2026-10-06 Yin requested a new G-series Task to prove Lehmer's conjecture or find a counterexample, initially emphasizing geometric group theory, then explicitly added DGB16's algebraic-entropy formulation and set the order: **algebraic entropy first, linear-group growth second; other directions may be selected and ranked by the agent**.
This paragraph preserves the original authorization history.
Yin subsequently clarified that all formulations belong to one Task and that their current ordering belongs to the strategy priorities.
G is the research-line letter within the numbered T family, not a revival of retired short goal identifiers.

This is **Yin's individual Lehmer Task, Yin_T_G0001**.
Its mathematical objective and completion criteria are common to all formulations below.
The associated rolling S materials own route priorities, dispositions and next steps; no formulation is a separate Task.
Use the full T/S identifiers to distinguish the objective from its routes.
Changing a strategy's priority does not change this contract or create another Task.

Resolve the classical **existence of a positive Mahler gap**.
For a nonzero primitive polynomial
\(f(t)=a_d\prod_{j=1}^d(t-\alpha_j)\in\mathbb Z[t]\), put
\[
M(f)=|a_d|\prod_{j=1}^d\max\{1,|\alpha_j|\},\qquad
m(f)=\ln M(f),\qquad
\mathfrak L=\inf\{m(f):m(f)>0\}.
\]
The target is to prove \(\mathfrak L>0\), or to prove \(\mathfrak L=0\).
Degree and coefficients are unrestricted.
Multiplicities count, zero roots contribute zero, and the primitive normalization is essential when passing to a rational companion endomorphism.
This is not the stronger assertion that Lehmer's degree-ten number gives the optimal positive measure, nor the house/Schinzel--Zassenhaus conjecture.

For an algebraic number \(\lambda\), write \(m(\lambda)=m(p_\lambda)\), where \(p_\lambda\) is its primitive irreducible integer polynomial, determined up to sign.

<a id="algebraic-entropy-contract"></a>
### Equivalent formulation: algebraic entropy

Let \(G\) be any discrete abelian group, written additively, and \(\phi\in\operatorname{End}(G)\).
For every **nonempty finite subset** \(F\subseteq G\), set
\[
T_n(\phi,F)=F+\phi(F)+\cdots+\phi^{n-1}(F),\qquad
H(\phi,F)=\lim_{n\to\infty}\frac{\ln|T_n(\phi,F)|}{n},\qquad
h_{\rm alg}(\phi)=\sup_F H(\phi,F)\in[0,\infty].
\]
There is no general restriction that \(F\) be a subgroup or contain zero.
This is DGB16's finite-subset entropy \(h\), not the older finite-subgroup entropy \(\operatorname{ent}\).
The equivalent uniform-gap question is
\[
\exists\eta>0\ \forall G\text{ abelian}\ \forall\phi\in\operatorname{End}(G):
\quad h_{\rm alg}(\phi)=0\ \text{or}\ h_{\rm alg}(\phi)\ge\eta.
\]
Infinite entropy satisfies the second alternative.
DGB16 Theorem 1.5 identifies the infimum of these positive entropies with \(\mathfrak L\), and with the infimum over \(A\in GL_n(\mathbb Q)\), **all** \(n\ge1\), acting on \(\mathbb Q^n\).
The constant must be independent of rank, group, and endomorphism.
The relevant reductions and their external-input limits are in [DGB16-U004](../audits/literature/DGB16/Yin_U004.md#dgb16-u004).

For a monic rational characteristic polynomial \(\chi_A\), use the primitive integer rescaling \(s\chi_A\), where \(s\) is the least positive integer clearing its denominators: \(h_{\rm alg}(A)=m(s\chi_A)\).
The leading-coefficient term \(\ln s\) must not be dropped.
Do not divide entropy or Mahler measure by rank/degree; the absolute Weil height is a different normalization.

DGB16 Theorem 1.7 provides the associated finite-set attainment question:
\[
\forall G\text{ abelian}\ \forall\phi\in\operatorname{End}(G),\qquad
h_{\rm alg}(\phi)<\infty\ \Longrightarrow\
\exists F\subseteq G\text{ finite nonempty}: H(\phi,F)=h_{\rm alg}(\phi).
\]
Attainment concerns the **same endomorphism** and a finite subset, not a different flow with the same entropy value or attainment by a finite subgroup.
The audit checks the in-paper mechanism with repairs, but the printed reverse implication retains a not-yet-inspected original spectral input (DGB16 Theorem 7.4, cited from its reference [11]).
Any solution through this route must check the implication actually used, or replace it by a complete argument; its status cannot be upgraded merely by citing the equivalence.
In particular, a nonattainment refutation uses only the contrapositive of positive gap implying universal attainment, whose proof does not use that exact-spectrum input.
Finite-entropy torsion flows and torsion-free finite-rank flows already attain; the unrestricted domain remains essential.

<a id="linear-growth-contract"></a>
### Equivalent formulation: linear-group growth

For a nonempty finite set \(S\subset GL_d(\mathbb C)\), let \(S^n\) mean products of exactly \(n\) elements of \(S\), and set
\[
\rho_2(S)=\lim_{n\to\infty}\frac{1}{n}\log_2|S^n|.
\]
Sets need not be symmetric.
Adjoining the identity preserves the rate, whereas replacing a set by a symmetric generating set needs its own comparison.
The equivalent target of BV20 Theorem 4 is
\[
\forall d\ge1\ \exists\varepsilon_d>0\
\forall\,\varnothing\ne S\subset GL_d(\mathbb C)\text{ finite}:\qquad
\rho_2(S)=0\ \text{or}\ \rho_2(S)\ge\varepsilon_d.
\]
Uniformity is over both the subgroup and generating set at each fixed matrix dimension.
The source's strict positive lower bound is equivalent after shrinking the constant.

The two-dimensional affine model
\[
S_\lambda=\left\{\begin{pmatrix}\lambda&1\\0&1\end{pmatrix},
\begin{pmatrix}\lambda&-1\\0&1\end{pmatrix}\right\},
\qquad \lambda\in\overline{\mathbb Q}\setminus\{0\},
\]
gives a focused equivalent core.
With BV20's base-two random-walk Shannon entropy \(h_{\rm rw,2}(\lambda)\), the audited bounds are
\[
c_0\min\{1,m(\lambda)/\ln2\}\le h_{\rm rw,2}(\lambda)
\le\rho_2(S_\lambda)\le m(\lambda)/\ln2,
\qquad c_0>0.
\]
Thus a uniform gap in this affine family is equivalent to the classical gap.
**Shannon entropy here is not DGB16's algebraic entropy**.
The rational-flow bridge uses \(h_{\rm alg}(C(f))=m(f)\), for the correctly normalized primitive polynomial.
Zero factors must be removed when an invertible companion map is required.
Use the symbolic constant \(c_0\), not the source's uncertified numerical value \(0.44\).
The full complex-linear reduction is retained at the precise repaired scope of [BV20-U003](../audits/literature/BV20/Yin_U003.md#bv20-u003), with its external structural inputs explicit.

### Other directions and scope boundaries

Group determinants and topology may supply auxiliary routes, provided an exact bridge back to the original scalar problem is proved.
In Luc22's kernel-removed convention,
\(\Lambda_1(\mathbb Z)=\Lambda_1^w(\mathbb Z)=\Lambda^w(\mathbb Z)\) represents the classical constant; the unrestricted rectangular-matrix \(\Lambda(\mathbb Z)\) must not be silently identified with it.
Values for varying groups or unrestricted rectangular or singular matrices do not by themselves resolve this Task.
Square weak isomorphisms over \(\mathbb Z[\mathbb Z]\) do admit the audited scalar-determinant reduction, with matrix size unrestricted.
Preserve the canonical group trace and **unnormalized** matrix amplification; dividing by matrix size would change the question.

Arithmetic and certified computation are supporting tools for all routes.
Bounded degree, rank, support, coefficient ranges, or finite-word experiments may test a mechanism but cannot silently replace the universal domain.
A result conditional on Lehmer positivity, determinant approximation, or another unresolved premise is partial progress unless that premise is separately discharged.
General solvable-group or entropy analogies require an actual implication back to this contract.

### Completion criteria

Complete this Task only with a full argument resolving the original gap, together with a covering completion review:

1. **Proof:** establish some \(\delta>0\) for every positive \(m(f)\), directly or through one of the exact formulations with all needed bridges checked.
   An explicit numerical optimal value is not required; a rank-dependent lower bound alone is insufficient.
2. **Refutation:** prove arbitrarily small positive values, for example a family with \(0<m(f_k)<1/k\), or a rigorously justified equivalent existence statement.
   Exact positive finite algebraic entropies tending to zero also suffice through the checked infimum bridge.
   In the growth formulation, a sequence with \(0<\rho_2(S_k)\to0\) must lie in **one fixed** \(GL_d(\mathbb C)\); a sequence of growing dimensions alone does not negate it.
3. **Attainment-based resolution:** prove universal finite-set attainment, or construct one flow with \(0<h_{\rm alg}(\phi)<\infty\) and \(H(\phi,F)<h_{\rm alg}(\phi)\) for every nonempty finite \(F\), and verify the precise Lehmer implication being used.
   A nonattainment example already assuming arbitrarily small positive entropy is not an unconditional counterexample.

A single polynomial with measure between one and Lehmer's number would only disprove the optimal-bound variant.
No finite numerical search, failure of a stronger sufficient statement, or reproduction of an equivalence completes this Task.

The coordinating research agent must arrange separate review of key new bridge/proof steps and of the full logical chain at resolution.
The completion finding must bind the exact contract and all adopted fixed support, identify self-review versus independent review truthfully, check every quantifier and retained external input, and account for unbounded degree/rank and degenerate cases.
No proof or completion review is claimed by this setup.

## Starting sources and reuse limits

| Source | Starting use and boundary |
| --- | --- |
| [DGB16-U001](../audits/literature/DGB16/Yin_U001.md#dgb16-u001), [U002](../audits/literature/DGB16/Yin_U002.md#dgb16-u002), [U004](../audits/literature/DGB16/Yin_U004.md#dgb16-u004) | Algebraic entropy, addition/reduction interfaces, Theorems 1.5/1.7 and attainment. Preserve corrected zero roots, companion normalization, finite-subgroup hypotheses and external-input limits. |
| [GBV15-U001](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Rational Algebraic Yuzvinski Formula and finite-rank realization at the retained preprint's actual numbering and inspection depth. |
| [BV20-U001](../audits/literature/BV20/Yin_U001.md#bv20-u001), [U003](../audits/literature/BV20/Yin_U003.md#bv20-u003) | Qualitative entropy/Mahler bounds and growth equivalence with local repairs. The quantitative constant and disputed field-of-definition refinement are not accepted premises. |
| [Luc22-U001](../audits/literature/Luc22/Yin_U001.md#luc22-u001), [U002](../audits/literature/Luc22/Yin_U002.md#luc22-u002), [U003](../audits/literature/Luc22/Yin_U003.md#luc22-u003) | Determinant conventions, four distinct constants, abelian comparison and conditional approximation. Retain the corrected separation hypothesis and weak/unrestricted distinctions. |

These sources provide formulations and starting mechanisms, not a solution.
Apply the repository's knowledge-reuse and source-check rules before substantial new proof investment; recorded source dates do not certify a current exhaustive literature survey.

## Continuation and execution

The [derived strategy navigation](../strategies/index.md) supplies the routes associated to this exact Task contract; their S materials own current priorities, dispositions and next tests under Yin's instructions.
Consult those records for current work ordering.
Autonomous internal decomposition and additional route selection are authorized within the unchanged objective.

Use the [execution rules](../../framework/rules/execution.md) and the applicable stopping conditions in the selected Task decision when an actual autonomous run begins.
Registration and activation alone grant no research execution.
The Task remains mathematically unresolved.
The [responsible strategy entrance](../strategies/Yin_S_G0001.md#entropy-gap-route) locates the retained allocation across all routes and their inquiries and review limits; the selected decision below owns lifecycle.

## Current decision
[Selected decision](#decision-pause-after-neutral-reference-round-2026-11-10)

## Lifecycle and completion

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-06T07:14 |
| status | active |
| authority | Yin's 2026-10-06 instruction to open a G-series Task to prove or refute Lehmer's conjecture, followed by explicit inclusion and first priority of DGB16 algebraic entropy, linear-group growth second, and autonomous ranking of other in-scope directions. |
| reason | Establish the assigned universal-gap objective with exact equivalent formulations, source limitations and rigorous proof/refutation criteria; no mathematical resolution is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Contract](#contract) | Full classical Mahler-gap objective, primary algebraic-entropy and secondary growth formulations, scope, human ordering and completion criteria. |

### Decision single-task-organization

| Field | Value |
| --- | --- |
| date | 2026-10-06T07:57 |
| status | active |
| authority | Yin's explicit instruction to use one Lehmer Task and represent formulation priorities through its strategies. |
| reason | Confirm the existing single Task Yin_T_G0001, clarify the neutral objective title and formulation headings, and place current work ordering in the rolling S materials. The mathematical domain, gap target and completion criteria are unchanged; no separate T_G0002 or T_G0003 existed to retire or merge. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Contract](#contract) | One unrestricted classical Mahler-gap objective with exact equivalent formulations and common proof/refutation criteria; strategy priorities are managed in the associated S materials. |

### Decision human-pause-after-closeout

| Field | Value |
| --- | --- |
| date | 2026-10-10T13:56 |
| status | paused |
| authority | Yin's explicit instruction in the current conversation: complete closeout, then pause the Task. |
| reason | Deliberately suspend G0001 after preserving completed work and the actual unfinished handoff. Fixed results through L353 retain their complete author and review scopes; D221 remains incomplete and unreviewed, with its proposed comparison unrun. The unrestricted mathematical contract remains unresolved. Existing candidate directions and their evidence remain available, without any current execution mandate. Resume only on Yin's explicit continuation instruction, an applicable active Task decision. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged contract](#contract) | Preserve the entire unrestricted classical Mahler-gap objective, equivalent formulations, quantifiers and completion criteria. This is a human-directed lifecycle pause, with no mathematical completion or obstruction claim. |


### Decision bounded-d221-continuation
| Field | Value |
| --- | --- |
| date | 2026-10-10T15:13 |
| status | active |
| authority | Yin explicitly instructed in this conversation: complete draft D221, then organize and fix it. |
| reason | Resume only the existing D221 norm-one energy-capped finite comparison, its necessary proof/native review and fixed retention. Preserve the unchanged six-instance maximum, original inputs and solver settings, aggregate 180-second author-run cap and first-failure stop; no new direction, retry, enlarged domain or general G0001 exploration is authorized by this bounded continuation. Return to the previously requested Task pause after this work is fixed or an applicable stop prevents completion. The unrestricted mathematical objective remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged contract](#contract) | The original unrestricted Mahler-gap objective and completion criteria remain unchanged; the present work is only its existing finite D221 comparison. |


### Decision human-pause-after-d221-closeout

| Field | Value |
| --- | --- |
| date | 2026-10-10T15:39 |
| status | paused |
| authority | Yin's instruction to finish closeout and pause the Task, together with the later explicitly bounded instruction to complete D221 and organize its fixed retention. |
| reason | The bounded D221 investigation and necessary review are concluded and retained in [L355](../ledger/Yin_L_G0355_v1.md#unit-cap-fixed-scope). Five finite optimum certificates and two strict comparisons are reviewed; the sixth enlarged optimum remains uncertified beyond its feasible primal, with both the invalid exact dual and failed floating consistency retained. All author and review histories and native evidence are preserved. Return to the human-requested pause without a retry or new exploration mandate. The unrestricted mathematical contract remains unresolved. Candidate directions remain available for a future explicitly authorized continuation. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged contract](#contract) | Preserve the full unrestricted objective, equivalent formulations, quantifiers and completion criteria. This is a lifecycle pause after bounded closeout, not mathematical Task completion or a route-wide obstruction. |

### Decision weekly-resume-2026-10-11

| Field | Value |
| --- | --- |
| date | 2026-10-11T10:51 |
| status | active |
| authority | Yin explicitly instructed in this conversation: advance with G0001 as the goal, and when weekly usage is exhausted organize the existing drafts and then stop. |
| reason | Resume the unrestricted unchanged Lehmer-gap objective after the human-requested pause. Follow the current integer-coefficient emphasis and coupled analytic, algebraic and structural strategies, preserving all fixed results and failures. Stop new exploration on weekly exhaustion; complete proportionate draft/evidence closeout and a continuation handoff before ending the period. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged contract](#contract) | The full unrestricted classical Mahler-gap objective and its exact completion criteria remain unchanged. This decision restores research authority; it claims no mathematical resolution. |


### Decision human-pause-after-progress-closeout-2026-10-13

| Field | Value |
| --- | --- |
| date | 2026-10-12T18:35 |
| status | paused |
| authority | Yin explicitly instructed in the current conversation: inspect G0001, organize its current unfinished progress, then pause the Task. |
| reason | Deliberately suspend the unchanged G0001 objective and all eight associated routes after organizing their responsible continuation points. Preserve already adopted results through C91/C92 at their exact partial, conditional and fixed-rank scopes, and the author-complete but unreviewed D48 checkpoint. The unrestricted Mahler-gap contract, actual same-exponent positive-income coverage and C91 uniform extremal bound remain unresolved. The responsible strategy handoff records the outstanding review, original-law, analytic and realization obligations. This human-directed pause supersedes the prior weekly continuation authority; it is neither mathematical completion nor a claim that quota was exhausted. Resume only on Yin's explicit continuation instruction, an applicable active Task decision. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged contract](#contract) | Preserve the entire unrestricted classical positive-Mahler-gap or zero-gap-family objective, exact equivalent formulations, original quantifiers and completion criteria. This is a human-directed lifecycle pause after progress organization, with no new mathematical acceptance or completion finding. |

### Decision human-resume-2026-10-13

| Field | Value |
| --- | --- |
| date | 2026-10-13T03:26 |
| status | active |
| authority | Yin explicitly instructed in this conversation: continue Task G0001. |
| reason | Resume the unchanged unrestricted Mahler-gap objective after the human-directed pause, using the preserved responsible handoff. Begin with the entire independent review of the author-complete D48 candidate and the remaining C91 arithmetic-density question; coordinate necessary extraction and actual review without promoting unreviewed work. Preserve adopted C91/C92, every earlier mathematical limitation. No mathematical completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged contract](#contract) | Entire unrestricted classical positive Mahler gap or rigorously established zero-gap family, exact equivalent formulations, original quantifiers and completion criteria. |

### Decision human-pause-after-new-window-closeout-2026-10-13

| Field | Value |
| --- | --- |
| date | 2026-10-13T05:38 |
| status | paused |
| authority | Yin explicitly instructed in this conversation: finish this exploration round, organize drafts, then pause. |
| reason | Pause the unchanged unrestricted G0001 objective and all eight associated routes after completing this bounded round and its fixed-material organization. C99--C101 select their separate whole-original and actual-extraction reviews; complete extension explorations are fixed in L395/L396 with R456/R455 whole findings. Entire original drafts and failed methods are preserved, incoming locators repaired and redundant working copies retired. General no-loss density capture, higher-efficiency localization and automatic near-one coverage remain unresolved. This human-directed pause supersedes the preceding continuation authority; it is not mathematical completion or a quota-exhaustion claim. Resume only on explicit human continuation, an applicable active Task decision. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged original contract](#contract) | Entire unrestricted positive Mahler gap or rigorously established zero-gap family, all equivalent formulations and original quantifiers. This is a lifecycle pause after organization, with no completion assertion. |

### Decision parallel-algebraic-haar-resume-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:06 |
| status | active |
| authority | Yin explicitly instructed this conversation to advance G0001 as the goal, pursuing the algebraic line and the F-series-inspired line in parallel, freely adjusting other routes according to progress, and making exploratory leaps in addition to explicit quantitative tests. |
| reason | Resume the unchanged original objective after the human-directed pause. Coordinate algebraic and arithmetic structure with the completed F0010 single-Haar determinant and coefficient-Gram interfaces, without requiring every exploratory question to begin as a predetermined certificate. Preserve all previous fixed results, failed methods and review limits. Other routes may be selected or reprioritized within the unchanged objective. No mathematical completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged original contract](#contract) | Entire unrestricted positive Mahler gap or rigorously established zero-gap family, exact equivalent formulations, original quantifiers and completion criteria. |

### Decision human-pause-after-parallel-round-closeout-2026-10-16

| Field | Value |
| --- | --- |
| date | 2026-10-15T16:41 |
| status | paused |
| authority | Yin explicitly instructed in the current conversation: finish the current round, organize progress, then pause the Task. |
| reason | Pause the unchanged unrestricted G0001 objective after completing the current algebraic/F-inspired round and its assigned independent reviews. Preserve adopted C150/C151/C152/C153v2/C154 at their exact scopes, the uncorrected C153v1 and its changes-required review, and the explicitly unreviewed complete D35 pause checkpoint. The responsible strategies retain exact continuation and review obligations. This human-directed pause supersedes further autonomous exploration under the preceding parallel-line instruction; it is neither mathematical completion nor quota exhaustion. Resume only on explicit human continuation, an applicable active Task decision. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged original contract](#contract) | Entire unrestricted positive Mahler gap or rigorously established arbitrarily small positive values, all equivalent formulations, original quantifiers and completion criteria. This is a lifecycle pause after progress organization, not a completion finding. |

### Decision bounded-joint-norm-review-pause-2026-10-16

| Field | Value |
| --- | --- |
| date | 2026-10-15T17:01 |
| status | paused |
| authority | Yin explicitly requested completion of the independent review of D35's joint norm lower bound, organization of its result, and continued G0001 pause. This is bounded review authority, not general research resumption. |
| reason | Retain the unchanged unrestricted objective and paused lifecycle after the requested review. The complete former D35 Section8 is now fixed and independently accepted in C155 through R518, including the total-reality hypothesis, original norm and analytic costs, and the restricted old-covariance comparison. Earlier D35 Sections1--7 remain continuing author material outside this review. All eight routes remain paused; no new exploration, native computation or further review is authorized by this closeout. The original objective remains unresolved, and this is neither completion nor quota exhaustion. Resume only on explicit human continuation, an applicable active Task decision. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged original contract](#contract) | Entire unrestricted positive Mahler gap or rigorously established arbitrarily small positive values, with unchanged quantifiers and completion criteria. This is a continued-pause decision, not a completion finding. |

### Decision bounded-fixed-2d-test-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T07:57 |
| status | active |
| authority | Yin explicitly requested: resume G0001 only for the first fixed-2d-window, energy-four test; organize results and recommendations and pause the Task again after completion. |
| reason | Authorize only the retained prescribed-C155-value diagnostic in the ordinary 2d coefficient window, exact input validation and energy comparison, warranted circle-contact checks, independent finite-scope verification, and result/handoff organization. No larger scan, alternate auxiliary, logarithmic-branch exploration or general G0001 advancement is authorized. Stop on the stated test limits or an execution stop; return to paused after bounded closeout. The unrestricted mathematical objective remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged original contract](#contract) | Entire unrestricted positive Mahler gap or rigorously established arbitrarily small positive values; only the explicitly bounded diagnostic is resumed. |


### Decision fixed-2d-test-closeout-pause-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T08:08 |
| status | paused |
| authority | Yin explicitly requested only the fixed2d energy-four first round, followed by result organization, recommendations and renewed pause. |
| reason | The declared four-input diagnostic is complete in [J97](../computations/programs/Yin_J_G0097/readme.md#finite-results), with actual independent finite-scope [R374](../audits/reviews/Yin_R_G0374_v1.md#fixed-2d-finite-finding). All four exact energies exceed4; original-circle certificates additionally exclude strict supremum below2 for the same value at every window length on the quartic Salem and Lehmer controls. These are finite-input results, not a universal energy barrier or resolution of the original objective. Restore the requested pause after preserving native evidence and scoped recommendations. No broader scan, direct-logarithm investigation or further assignment is authorized. Resume only on explicit human continuation, an applicable active Task decision. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged original contract](#contract) | Entire unrestricted positive Mahler gap or rigorously established arbitrarily small positive values; unresolved. This is a human-directed pause after bounded finite-test closeout, not Task completion. |

### Decision bounded-b3-log-diagnostic-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T08:17 |
| status | active |
| authority | Yin explicitly requested resumption only for the existing B3 direct-logarithmic first-round diagnostic on the same four inputs, with error-certified Haar logarithmic averages and comparison to the original-conjugate averages and log2, followed by result organization, recommendations and renewed pause. |
| reason | Authorize only those four fixed original inputs and the unchanged C155 B3 object, certified evaluation with necessary analytic error control and independent finite-scope checking. No new inputs, altered auxiliary values, representative search or general G0001 exploration is authorized. Preserve the original normalization, all conjugates and exact norm multiplicities. Finish the bounded diagnostic or preserve any applicable failure, then pause again. The unrestricted mathematical objective remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged original contract](#contract) | Entire unrestricted positive Mahler gap or rigorously established arbitrarily small positive values; only the explicitly bounded direct-logarithmic diagnostic is resumed. |


### Decision b3-log-closeout-pause-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T08:25 |
| status | paused |
| authority | Yin explicitly requested only the existing-B3 certified direct-logarithmic first round on the same four inputs, followed by result organization, recommendations and renewed pause. |
| reason | The declared four-input diagnostic is complete in [J98](../computations/programs/Yin_J_G0098/readme.md#certified-results), with actual independent finite-scope [R375](../audits/reviews/Yin_R_G0375_v1.md#four-input-logarithmic-finding). Both direct analytic ball integration and complete-root Jensen/full-resultant reconstruction certify Lambda_P>I_P>log2 on all four inputs, with every reported decimal error below1e-10. Preserve the exact original B3, full norms, scalar normalization, finite limits and unexecuted recommendations, then restore the requested pause. No uniform margin, original-root/Haar transfer law or resolution of G0001 is claimed. No new inputs, auxiliary changes or further assignments are authorized. Resume only on explicit human continuation, an applicable active Task decision. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged original contract](#contract) | Entire unrestricted positive Mahler gap or rigorously established arbitrarily small positive values; unresolved. This is a human-directed pause after the bounded logarithmic diagnostic, not Task completion. |

### Decision resume-balanced-weight-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T09:02 |
| status | active |
| authority | Yin explicitly instructed in the current conversation: resume G0001. This supersedes the preceding analysis-only pause; it does not request an automatic renewed pause. |
| reason | Resume the unchanged unrestricted objective through the retained balanced-H25-weight continuation. First establish and independently review the complete changed-value arithmetic, original normalization and lower-envelope gate. Then execute only the two-input component screen and, only for surviving inputs, the predeclared six-point grid with its certification, time and stop limits. Preserve failed or inconclusive outcomes without expanding the test automatically. Later research allocation must follow the mathematical evidence; this decision asserts no theorem, computation result or Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged original contract](#contract) | Entire unrestricted positive Mahler gap or rigorously established arbitrarily small positive values, with unchanged quantifiers and completion criteria. |

### Decision continue-until-stop-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T09:56 |
| status | active |
| authority | Yin explicitly instructed: continue the Task until the stopping condition is reached. |
| reason | Continue autonomous advancement of the unchanged unrestricted G0001 objective beyond the completed balanced-weight diagnostic. Candidate-specific failure or a completed bounded test redirects research and does not by itself end the authorized run. Apply the existing weekly-exhaustion and monitoring/account-change stop policy, any later human stop, and the original reviewed mathematical completion criteria. Select further concrete mechanisms, necessary literature, bounded computations and separate reviews under the responsible strategies; do not infer a new quota allowance or mark an unresolved objective complete. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged original contract](#contract) | Entire unrestricted positive Mahler gap or rigorously established arbitrarily small positive values, with all original quantifiers, exact bridges and covering completion review. |

### Decision continue-until-ten-percent-remaining-2026-10-19

| Field | Value |
| --- | --- |
| date | 2026-10-18T16:56 |
| status | active |
| authority | Yin explicitly instructed in the current conversation: pause the Task when ten percent of the weekly usage remains. This narrows the previous until-stop continuation authority. |
| reason | Continue the unchanged unrestricted G0001 objective and integrated active strategies only until weekly usage reaches ninety percent, or an earlier applicable monitoring/account stop or reviewed mathematical completion. On the threshold observation stop new exploration, preserve available evidence and a concise handoff, and append the human-directed paused Task decision. Candidate-specific failures still redirect research rather than causing an early stop. Resume after the conditional pause only on explicit human instruction. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged original contract](#contract) | Entire unrestricted positive Mahler gap or rigorously established arbitrarily small positive values, with unchanged quantifiers, bridges and completion criteria; only the authorized execution threshold is narrowed. |

### Decision weekly-ten-percent-pause-2026-10-19

| Field | Value |
| --- | --- |
| date | 2026-10-18T18:04 |
| status | paused |
| authority | Yin explicitly instructed that G0001 pause when ten percent of the weekly usage remains. |
| reason | The human-directed usage condition has been observed. Stop autonomous exploration, preserve completed evidence and continuing responsible drafts, and pause all eight associated strategies including their subroutes. The unrestricted mathematical objective remains unresolved; finite results and route obstructions do not complete or refute it. Resume only on explicit human continuation and applicable execution conditions. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged unrestricted contract](#contract) | Entire classical positive Mahler gap or a rigorously established zero-gap family, with all original quantifiers, equivalent formulations and completion requirements; unresolved and paused under the explicit human resource condition. |


### Decision resume-retained-draft-inquiries-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T09:04 |
| status | active |
| authority | Yin explicitly instructed: continue advancing until the tasks in the retained drafts are completed. This authorizes research continuation of D35, D36, D37 and D42 after the preceding preservation-only round. |
| reason | Resume the unchanged G0001 contract through the four retained mathematical inquiries: positive arithmetic and original-root transfer, mixed-form Schur residual and transfer costs, the unbuffered singleton, and a controlled powered-Frobenius application outside known coverage. The current account/window has been verified under this explicit continuation; the human weekly ninety-percent stopping threshold remains effective. Resolve the actual stated obligations with the applicable evidence and review, preserving negative results and unresolved scope; fixing or retiring a draft alone is not completion. Coordinate all eight strategies only for these inquiries and their necessary interfaces, without opening unrelated research branches. Stop this authorized round when all four inquiries are genuinely resolved, on the usage threshold or another applicable stop, and retain the unrestricted Task as unresolved unless its original completion criteria are independently met. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged unrestricted contract](#contract) | Entire classical positive Mahler gap or rigorously established arbitrarily small positive values, with all original quantifiers and completion criteria. The current work allocation is limited to the four retained draft inquiries and necessary supporting interfaces. |


### Decision human-pause-after-draft-scope-closeout-2026-10-21

| Field | Value |
| --- | --- |
| date | 2026-10-20T17:55 |
| status | paused |
| authority | Yin explicitly instructed in the current conversation: complete the current step, then pause. |
| reason | Pause after completing the original-draft scope audit, exact preservation and consumer repair. The redundant mixed-form D36 is retired with its mathematics and unresolved comparison at existing fixed homes. D35 retains the actual new SAME-T author work, failed support construction and precise undecided coefficients without independent acceptance. The previously adopted bounded results remain at their exact C/L/R scopes. This is a human-directed pause before the weekly resource threshold, not completion of the two open comparison obligations, the four-inquiry research round or the unrestricted Lehmer contract. No new exploration, computation or higher-modulus continuation is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged unrestricted contract](#contract) | Entire classical positive Mahler gap or rigorously established arbitrarily small positive values, all original quantifiers and completion criteria. The retained-inquiry mathematical obligations remain unresolved at their exact recorded scopes; this decision pauses execution after the requested current-step closeout. |

### Decision all-strategies-resume-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T14:18 |
| status | active |
| authority | Yin explicitly instructed in this conversation: activate all strategies, then continue the Task. |
| reason | Resume the unchanged unrestricted Lehmer objective and all eight strategies after the preceding human pause. The current authenticated account and weekly window permit continuation under the retained ninety-percent-used threshold. Advance the same-original-input compatibility and fully paid original-root comparison while allowing the other active entropy, growth, determinant and arithmetic mechanisms to supply alternatives and shared inputs. Preserve completed bounded inquiries, exact finite failures, current review relationships and unadopted author work. A completed test redirects research rather than automatically pausing the Task; no mathematical completion or new quota allowance is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged unrestricted contract](#contract) | Entire classical positive Mahler gap or rigorously established arbitrarily small positive values, with all original hypotheses, quantifiers, equivalent formulations and completion criteria. |


### Decision human-pause-after-current-work-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T05:20 |
| status | paused |
| authority | Yin explicitly instructed in the current conversation: complete the work at hand, then pause. This later instruction narrows the preceding continuation to its already underway writing, reviews and necessary closeout. |
| reason | The underway fixed results, independent whole reviews, actual adoptions, draft retention and responsible consumers have been closed out. Pause G0001 and all eight associated strategies, including their subroutes, before any further exploration, computation or higher-precision construction. The original unrestricted Mahler-gap objective remains unresolved: finite-modulus results and fixed-positive-measure Fourier families do not supply a characteristic-zero realization or a uniform gap. This is the explicit human closeout pause, not mathematical completion or a claim that the ninety-five-percent usage threshold was reached. Resume only on explicit human continuation with applicable execution conditions; unused allowance, a reset or a new session is insufficient. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged unrestricted contract](#contract) | Entire classical positive Mahler gap or rigorously established arbitrarily small positive values, with all original hypotheses, quantifiers, equivalent formulations and completion criteria. The contract remains unresolved and is paused after the requested current-work closeout. |


### Decision resume-until-two-percent-remaining-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T05:06 |
| status | active |
| authority | Yin explicitly instructed in the current conversation: continue the Task until two percent of the quota remains. This resumes the preceding current-work pause and changes the effective weekly stopping threshold to ninety-eight percent used. |
| reason | Continue the unchanged unrestricted Lehmer objective with all eight retained strategies. The current authenticated account and weekly window have been checked and permit advancement. Resume actual same-polynomial higher-residual compatibility, fully paid original-law/Fourier comparisons and alternative entropy, growth, arithmetic and determinant mechanisms according to their retained evidence. Stop new exploration at the first observation of weekly use at least ninety-eight percent, or an earlier applicable monitoring/account stop or reviewed mathematical completion; retain available results and pause under that human condition. A completed bounded result redirects research rather than ending this continuation. No finite-modulus theorem, positive-measure family or conditional criterion is Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged unrestricted contract](#contract) | Entire classical positive Mahler gap or rigorously established arbitrarily small positive values, with all original hypotheses, quantifiers, equivalent formulations and completion criteria; only execution authority and its absolute weekly stopping threshold are changed. |


### Decision human-account-switch-pause-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T05:36 |
| status | paused |
| authority | Yin explicitly instructed: pause now and prepare the account-switch handoff. This interrupts the preceding until-two-percent-remaining continuation. |
| reason | Stop new derivation, computation and mathematical review immediately. Preserve already adopted fixed results and already formed but unadopted candidates/findings at their existing responsible homes, with their actual unfinished obligations; this pause does not claim that underway research or reviews were completed. All eight strategies and their subroutes are paused. The unrestricted Lehmer objective remains unresolved. The ninety-eight-percent weekly stop is retained for an explicitly authorized continuation, but switching accounts or windows transfers no allowance or execution authority. Resume only after explicit human continuation and a reliable check of the actual account, weekly bucket/window and applicable conditions. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged unrestricted contract](#contract) | Entire classical positive Mahler gap or rigorously established arbitrarily small positive values, with all original hypotheses, quantifiers, equivalent formulations and completion criteria; unresolved and paused for the human-requested account switch. |


### Decision resume-after-account-handoff-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T06:16 |
| status | active |
| authority | Yin explicitly instructed in the current conversation: continue G0001, after the account-switch handoff pause. |
| reason | Resume the unchanged unrestricted objective and all eight retained strategies after fresh reliable verification of the current authenticated interface and applicable weekly window. The explicit continuation applies to the currently verified window, without transferring an old allowance or inferring an identity switch merely from a usage change. Retain the human absolute stopping threshold of ninety-eight percent weekly use. Complete the preserved C734 review-adoption step and continue the actual earlier-coefficient compatibility and changed-prime original-law inquiries at their exact saved scopes; other active mechanisms may supply alternatives and shared inputs. Stop new exploration on the first threshold observation or an earlier applicable monitoring/account stop or reviewed mathematical completion. No partial theorem or completed bounded test resolves the unrestricted Task. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged unrestricted contract](#contract) | Entire classical positive Mahler gap or rigorously established arbitrarily small positive values, with all original hypotheses, quantifiers, equivalent formulations and completion criteria; unresolved and explicitly resumed under the retained weekly threshold. |

### Decision human-pause-after-rotation-closeout-2026-11-06

| Field | Value |
| --- | --- |
| date | 2026-11-06T13:54 |
| status | paused |
| authority | Yin explicitly instructed in this conversation: finish the current work, then pause. |
| reason | The underway rotation-iteration check is complete and retained in L458 v6, with the earlier constructions, exact computations and root tests preserved at their responsible homes. Pause G0001 and all nine associated strategies, including their subroutes, before any further exploration, computation or mathematical review. The unrestricted Lehmer contract remains unresolved. Retain the counterexample-first allocation and small complementary S9 effort for a later explicit resumption, together with the ninety-eight-percent weekly stopping threshold. Neither this closeout, unused quota nor a reset authorizes resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged unrestricted contract](#contract) | Entire classical positive Mahler gap or rigorously established arbitrarily small positive values, with all original hypotheses, quantifiers, equivalent formulations and completion criteria; unresolved and paused on the human's instruction after current-work closeout. |

### Decision bounded-strategy-discovery-2026-11-07

| Field | Value |
| --- | --- |
| date | 2026-11-07T17:53 |
| status | active |
| authority | Yin requested a progress assessment, a next direction from the main research agent and independent exploration by agent-S. |
| reason | Resume for this strategic exploration and its bounded first test, retaining the weekly stop at 98 percent used and the counterexample-first allocation. The assignment ends with the comparison and handoff. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unrestricted Lehmer contract](#contract) | Identify a next investigation that could change the prospects for a uniform gap or a sequence of positive total measures tending to zero. |

### Decision strategy-handoff-2026-11-07

| Field | Value |
| --- | --- |
| date | 2026-11-07T18:07 |
| status | paused |
| authority | Yin requested a progress assessment, a next direction and a bounded independent exploration by agent-S. |
| reason | The requested comparison and first tests have returned. Retain the moving signed-residue construction for further work under S4 and the limited complementary S9 allocation. The prior general pause resumes at this handoff. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unrestricted Lehmer contract](#contract) | A uniform gap and the existence of arbitrarily small positive measures are both unresolved. |
| support | [Fixed template factors](../claims/Yin_C_G0879_v2.md#decision-general-template-whole) | Each positive divisor of the rotated dyadic family has a uniform positive floor. |
| support | [Whole lifts with cyclotomic trace poles](../claims/Yin_C_G0880_v1.md#decision-whole-residue-gap) | Positive residues and bounded signed total variation each imply a whole-output gap. |
| support | [Moving sign test](../ledger/Yin_L_G0462_v2.md#moving-sign-test) | Bounded first tests and the remaining simultaneous construction problem. |

### Decision resume-small-shell-2026-11-08

| Field | Value |
| --- | --- |
| date | 2026-11-08T01:52 |
| status | active |
| authority | Yin explicitly requested continuation of G0001 after discussing probabilistic existence. |
| reason | Resume the unrestricted objective with counterexample-first priority, seeking discrete positive mass in arbitrarily small strict Mahler shells and testing the moving trace construction under the shared weekly stop. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unrestricted Lehmer contract](#contract) | A uniform positive gap or a proof of arbitrarily small positive total measures, including nonconstructive existence. |

### Decision pause-after-pole-round-2026-11-09

| Field | Value |
| --- | --- |
| date | 2026-11-09T16:42 |
| status | paused |
| authority | Yin explicitly instructed in the current conversation: finish this exploration round, then pause. |
| reason | The current integer-pole exploration and independent reviews are complete and retained at their responsible homes. Pause G0001 and its routes before any new exploration, computation or mathematical review. The unrestricted objective remains unresolved; further research requires Yin's explicit resumption, with the shared ninety-eight-percent weekly stopping threshold and monitoring conditions retained. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged unrestricted contract](#contract) | A uniform positive gap or a rigorous proof of arbitrarily small positive total measures, including nonconstructive existence; unresolved and paused after the current round. |


### Decision resume-adaptive-sampling-2026-11-09

| Field | Value |
| --- | --- |
| date | 2026-11-09T17:24 |
| status | active |
| authority | Yin explicitly appointed this chat's agent as the main research agent and requested that G0001 be started as a goal and advanced. |
| reason | Resume the unchanged unrestricted Lehmer objective with counterexample-first priority, initially implementing and testing S10's bounded adaptive-sampling comparison alongside S4's retained integer constructions. The shared weekly stopping threshold remains ninety-eight percent; stop on reaching it, loss of reliable monitoring or an account change. A finite experiment, improved example or conditional construction does not complete the Task. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged unrestricted contract](#contract) | A uniform positive gap or a rigorous proof of arbitrarily small positive total measures, including nonconstructive existence, with unrestricted degree and coefficients. |


### Decision pause-after-neutral-reference-round-2026-11-10

| Field | Value |
| --- | --- |
| date | 2026-11-10T11:44 |
| status | paused |
| authority | Yin explicitly instructed in this conversation: finish this exploration round, then pause. |
| reason | The variable-neutral-reference argument, squarefree-parent construction test, exact whole-measure certificate and their independent reviews are complete and retained at their responsible C/L/J/R homes. Pause G0001 and all ten associated strategies, including subroutes, before any new exploration, computation or mathematical review. The unrestricted objective remains unresolved. Further research requires Yin's explicit resumption; retain the shared ninety-eight-percent weekly stopping threshold and monitoring/account conditions. The saved construction questions are continuation material, not authorization to start another test. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Unchanged unrestricted contract](#contract) | A uniform positive gap or a rigorous proof of arbitrarily small positive total Mahler measures, including nonconstructive existence and unrestricted degree and coefficients; unresolved and paused after this exploration round. |

## Execution boundary

Current local family boundary: `execution/Yin_E_G0001.md`.
