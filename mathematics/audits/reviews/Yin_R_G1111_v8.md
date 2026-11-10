---
author: Yin
---

# Independent review of the reference-seeded archive implementation

## Arrangement and fixed scope

At 2026-11-09T21:25, a separately organized reviewer acting for Yin completed the implementation and retention review below.
The reviewer did not develop these author programs, received no substantive implementation-development discussion, and supplied no repair to the author code.
The initial review used the fixed S10 protocol, the three new source files, the specified README section and directly needed unchanged dependencies.
The reviewer identified the deadline-straddling proposal issue described below and independently checked the author's subsequent bounded repair and its affected interfaces.
The final findings apply to the sources and wording actually inspected at this review act, not to future changes or future experimental observations.

The unchanged full-measure evaluator, normalized cores, fixed coefficient law and conservative value ledger reuse the actual [v1 implementation finding](Yin_R_G1111_v1.md#sampler-implementation-review).
The unchanged subprocess and committed-parent interfaces reuse the applicable [v5 implementation](Yin_R_G1111_v5.md#degree-implementation-review) and [retention](Yin_R_G1111_v5.md#degree-results-review) findings.
The closure generator and its canonical-core interface reuse the [v7 closure finding](Yin_R_G1111_v7.md#cyclotomic-closure-review).
Their new composition, the new seed-aware ledger, native retention and the precise 30-identity screen were checked in this review.
No historical root census or unrelated experiment was rerun.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Online implementation](#archive-implementation-review) | independently reviewed |
| [Retention and portable replay](#archive-retention-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Online implementation](#archive-implementation-review) | [S10 archive protocol](../../strategies/Yin_S_G0010.md#cyclotomic-archive-comparison) | Complete declared domain, reference information, three proposal laws, whole-target update rule, charged costs, 30 identities, rotated serial order, seed-aware metric and joint same-seed allocation screen. |
| [Online implementation](#archive-implementation-review) | [Archive entry point](../../computations/programs/Yin_J_G0156/archive_sampling.py) | Entire new source: direct completion, archive state and RNG, callback composition, seed ledger, deadline/commit integration, post-run classification, validity, schedule, reporting and journal replay. |
| [Online implementation](#archive-implementation-review) | [Author bounded controls](../../computations/programs/Yin_J_G0156/archive_sampling_checks.py) | Entire source and actual independent execution of its deterministic controls and eight labelled subprocess controls, with 16 seconds of aggregate subprocess budget ceilings. |
| [Online implementation](#archive-implementation-review) | [Implementation description](../../computations/programs/Yin_J_G0156/readme.md#archive-comparison-implementation) | New implementation semantics, declared allocation, ordinary author-control table and qualified interpretation; no formal performance result. |
| [Online implementation](#archive-implementation-review) | [Frozen sampler](../../computations/programs/Yin_J_G0156/sampler.py) | Actual Law, DiscoveryLedger, worker callbacks, threshold/certificate retention, deadline/commit, summary and validity interfaces used by the new composition. |
| [Online implementation](#archive-implementation-review) | [Shared runtime](../../computations/programs/Yin_J_G0156/sampling_runtime.py) | Actual child invocation, pre-launch clock, hard cap, configuration/failure retention, post-run summary and observed censor. |
| [Online implementation](#archive-implementation-review) | [Original evaluator review](Yin_R_G1111_v1.md#sampler-implementation-review) | Reused complete-measure/root-multiplicity, exact normalization, fixed-law, cache and original-worker findings at their actual unchanged scope. |
| [Online implementation](#archive-implementation-review) | [Shared-runtime review](Yin_R_G1111_v5.md#degree-implementation-review) | Reused unchanged supervision and failure interfaces; the new configuration, timing composition and 30-identity eligibility are checked here. |
| [Online implementation](#archive-implementation-review) | [Closure generator](../../computations/programs/Yin_J_G0156/cyclotomic_closure.py) | Reused conditional exact generator as called afresh by each initialized or newly added core; no imported precomputed template output. |
| [Online implementation](#archive-implementation-review) | [Closure finding](Yin_R_G1111_v7.md#cyclotomic-closure-review) | Reused completeness under canonical normalized-core hypotheses, exact template order and degree-24/30 initial counts. |
| [Online implementation](#archive-implementation-review) | [Two-core reporting input](../../computations/programs/Yin_J_G0156/inputs/degree_core_mass_states.json) | Only the actual two reference core identities and their certificates used after the timed run; not proposal training or a new classification proof. |
| [Online implementation](#archive-implementation-review) | [Independent bounded checker](../../computations/programs/Yin_J_G0156/checks/independent_archive_review.py) | Independent direct coefficient construction, RNG/state reconstruction, seed/uncertainty fixtures, 500 synthetic screens and labelled actual-journal cross-checks. |
| [Retention and portable replay](#archive-retention-review) | [Archive exporter](../../computations/programs/Yin_J_G0156/archive_sampling_export.py) | Entire source, compact generated-template recipes, native archive and witness associations, unresolved/uncommitted inputs, replay, formal identity selection, partial and overwrite guards, and the repaired deadline suffix. |
| [Retention and portable replay](#archive-retention-review) | [Shared exporter](../../computations/programs/Yin_J_G0156/prior_strength_live_export.py) | Directly reused compact whole/factor certificates, exact witness IDs, committed factor-parent joins, retained run fields and reference validation. |
| [Retention and portable replay](#archive-retention-review) | [Earlier retention finding](Yin_R_G1111_v5.md#degree-results-review) | Reused unchanged complete-parent and factor-multiplicity export interfaces; no new degree-18/20 result review. |
| [Retention and portable replay](#archive-retention-review) | [Implementation description](../../computations/programs/Yin_J_G0156/readme.md#archive-comparison-implementation) | Native reproduction, observed controls, unresolved-input preservation, export/replay scope and the absence of a formal result. |
| [Retention and portable replay](#archive-retention-review) | [Independent bounded checker](../../computations/programs/Yin_J_G0156/checks/independent_archive_review.py) | Exact original-journal versus compact-native comparisons, all retained factor parents and retry inputs, and repaired deadline-suffix behavior. |

<a id="archive-implementation-review"></a>
## Online implementation finding

The finding is **PASS for the specified online implementation and its bounded implementation controls**.
This establishes neither the 30-run allocation outcome nor an empirical advantage of either archive law.

### Proposal law and archive state

For each run, the fixed arm creates one fresh instance of the unchanged original fixed law with the requested seed and delegates every draw to that instance.
Its additional seed certificate and ledger consume no random variates.
The two archive arms implement probability one tenth for the uniform coefficient box, then uniform selection of a core and a distinct template conditional on the other branch.
The number of templates belonging to one core does not change that core's selection weight.
The independent random generator state is reset for every run.

Conditional on a template, k is uniform on one, two and three; the coordinate subset is uniform without replacement, and sorting occurs before independent uniform signs are assigned.
The resulting law is the stated uniform subset-and-sign law.
A coefficient leaving the height-four box returns the parent as a single self-transition; no redraw or rejection renormalization occurs.
Generated templates are distinct and lexicographically ordered, new cores follow encounter order, and direct observed templates are appended once in encounter order.

The direct completion was checked from a separate coefficient formula.
For each allowed dilation and sign it forms the specified substituted core and, when the remaining degree is positive, its product with one plus the appropriate power of z.
This cyclotomic completion has the prescribed degree and reciprocal endpoints; height filtering and exact deduplication give four initial degree-24 templates and six initial degree-30 templates.
A new direct core retains its successful whole-target prefix even when its generated completion set is empty.
The closure arm calls the previously reviewed generator afresh, obtaining 1170 and 5532 initial templates and verifying every newly observed target's membership.

The independent checker compared 7200 deterministic draws, including unchanged fixed streams and archive streams before and after repeated-prefix and second-core insertion.
The matching archive branches included 518 uniform draws, 200 boundary returns and 1493 selections of the second inserted core.
These are implementation fixtures, not research-run outcomes or probability estimates.
Both archive orders and all reconstructed template lists agreed.

### Whole-target updates and timing

Only an evaluation with certified strict whole-output status below 6/5 invokes the seed-aware ledger and archive update.
The frozen threshold contract also requires the whole measure to be strictly above one.
A small factor alone, a ranking score, a threshold overlap or an arithmetic failure does not satisfy that gate.
The fixed arm performs no template update, and the retained frozen batching callback performs no independent marginal fit in any archive arm.

The common clock starts before process launch.
Fresh seed certification, seed-ledger initialization, fresh template generation, later archive construction, sampling, full evaluation, cache access, deduplication and event serialization occur before the evaluation's commit decision.
The archive callback runs inside the frozen evaluation write hook, before the frozen worker checks its finished time and writes an on-time commit.
If that work overruns the cap, the worker ends without any later proposal, and the retained final archive is reconstructed solely from committed updates.
The in-memory update therefore supplies no uncommitted discovery or retained archive state.
Initialization has its own on-time marker and contributes no retained initialized archive when that marker is absent.

The reviewer inspected the actual worker/supervisor paths and executed the author's atomicity controls.
The controls distinguish factor-only observations, a computed but uncommitted newly discovered core, and initialization without a commit.
The deliberate subprocess failure remains an invalid worker failure with its original observed duration and no completed proposal.
Stage costs retain their actual interfaces; they are not asserted to sum to all startup, serialization and supervisory overhead.

### Seed-aware values, catalog and decision rule

The supplied seed is inserted as value zero, without discovery credit.
The unchanged conservative ledger equates identical canonical cores and admits a different value only after certified interval separation from its existing representatives.
A new coefficient core whose interval overlaps the seed or another representative remains an explicit unresolved equality class.
A repeated unresolved core remains conservatively uncounted; a later strictly-below-seed enclosure is nevertheless preserved in the separate below-seed report.
The independent synthetic controls checked all these distinctions, including the later decisive enclosure of an already observed unresolved core.

The two-core catalog is read by post-run enrichment only.
Neither timed proposal generation nor archive construction reads its second-core coefficients or a precomputed closure file.
Classification as seed, second local core or absent from this supplied catalog does not establish literature novelty.
The existing external degree-classification statement is used here only to bound the intended interpretation of degrees 24 and 30; this review does not re-audit that original exhaustive classification.

The actual schedule has exactly degrees 24 and 30, arms fixed/direct/closure and seeds 20 through 24, with the prescribed degree-index-plus-seed-index rotation.
Formal eligibility requires a valid full twenty-second deadline run with the exact protocol identity, no proposal cap and no injected failure.
Missing, duplicate, invalid or nonformal controls cannot satisfy completeness.
For each degree, closure must have at least four count nonlosses against each comparator.
At one degree, at least three paired seeds must each give a strict win over both comparators.
Count is primary; only equal positive counts use an earlier first nonseed-hit time, and zero-zero never wins.
The author boundary fixtures and 500 separately generated finite synthetic datasets agreed with an independent evaluation of that predicate.

### Actual bounded child controls

The reviewer executed six two-second, 257-proposal controls at degrees 24 and 30 with seeds 100, 101 and 102 assigned to fixed, direct and closure.
All six completed exactly 257 proposals, with fresh initialization committed and all 1542 proposal vectors reconstructed independently.
The two closure controls recorded respectively fifteen and five seed-recovery hits; all six had zero nonseed values.
Their ordinary author-control counterparts and all six README table entries were also checked against the actual retained source summaries.

A separate degree-30 closure control with seed 103 completed 436 proposals before its two-second cap and retained one further incomplete proposal.
Its 437 logged vectors and fifteen committed archive updates reconstructed exactly.
The degree-24 direct seed-104 failure control logged one proposal, completed none and remained invalid.
The total subprocess budget ceilings were sixteen seconds.
These controls are deliberately excluded from the formal thirty-run comparison.

<a id="archive-retention-review"></a>
## Retention and portable replay finding

The finding is **PASS for retained inputs and portable replay in the repaired implementation**.
The initial replay coverage gap below was genuine, did not affect the measured law, yields or final archive, and was resolved by the author before this final finding.

### Retained state and failure inputs

The exporter preserves the original counts, configuration, supervision, charged stage totals, seed-aware metrics, first-hit observations and censor.
Whole values, the best candidate, unresolved equalities, seed information and core observations retain compact complete-output certificates.
Generated arrays are replaced by their exact source/core/degree/height/order/count recipe, while observed templates and all state-changing committed updates retain their order and exact coefficients.
Each distinct observed archive template has a whole-polynomial witness.
The update for a repeated observation without a state change consumes no RNG and does not alter either template or core selection, so it needs no additional replay update.

Separate factor findings join to their actual committed parent evaluations.
The parent retains full coefficients, the whole-measure enclosure, proposal and commit time, cache/repeat observations, charged costs and all factor associations for that retained parent.
The compact factor certificate preserves multiplicity and its single-factor scope.
Factor-only information never changes the primary whole-output metric or archive.

Committed arithmetic errors and unresolved ranking or threshold statuses retain exact retry coefficients, timing, reason and any certificate actually present.
An uncommitted candidate is retained separately, whether or not an evaluation record was flushed.
A late commit cannot create discovery credit.
The exporter labels absent certificates as absent and does not turn these retry inputs into certified witnesses.
The synthetic failure-stream fixtures cover all these cases, while the actual deadline and failure controls retain their respective exact final incomplete inputs.

### Initial negative finding and repair

The initial portable replay loop stopped at the frozen summary's proposal count.
That count includes only proposal records whose elapsed timestamp is at most the budget.
A draw can start before the cap and finish writing its proposal record just after the cap, so its exact input remains in the incomplete-input collection while falling outside that count.
Consequently the initial replay could report success without reconstructing that retained final candidate.
The reviewer reproduced this with the actual deadline control's last proposal, numbered 437, in a synthetic timestamp/count fixture: elapsed 2.000001 seconds, 436 within-budget proposals, and the same fifteen committed archive changes.
The old implementation replayed only 436 proposals although the retained candidate 437 was present.

The author changed only the exporter/replay source for this repair.
The repaired loop covers the maximum of the within-budget count and all retained unresolved or incomplete proposal identifiers.
It validates each retry input's full reciprocal coefficient vector and compares its prefix with the reconstructed RNG draw.
It also reports within-budget proposals separately from total reconstructed proposals and reports the number of checked retry inputs.
The reviewer read the changed replay, its new author boundary control and its self-test integration, then reran the actual compact replay and affected native interfaces without starting another worker or root calculation.
The independent fixture now reconstructs all 437 candidates, keeps the within-budget count at 436 and leaves every archive and metric unchanged.
A further committed-unresolved fixture is checked together with the final incomplete input.
Four separate mutations, changing a retry prefix with a correspondingly changed full polynomial or changing only its full coefficients in each collection, are all rejected.
The repaired author export self-test also passed against the reviewer's original eight controls.

### Actual native replay and limits

The reviewer independently exported and checked the six proposal-limited controls, the deadline control and the failure control.
The respective export collections contain 75, 29 and one exact witnesses and 25, seven and zero retained factor parents.
Their collections are separate and these witness counts are not claimed to be disjoint.
Every retained parent was matched to its committed original evaluation and charged costs.
All measured fields compared exactly with their source summaries, every retry input matched its original proposal, and every committed final archive was reconstructed independently.
Partial-input and overwrite refusals passed.
The original actual controls had 1980 logged proposal vectors in total, including the final incomplete deadline and failed proposals.

Compact replay reconstructs deterministic proposal/archive state without redoing roots or historical timing.
Witness verification is a separate full-measure computation and cannot add historical stochastic discoveries.
The formal native files and thirty-run observations did not exist at this review act.
No inference about later discoveries, timing advantage, allocation success, new core coverage or completion of the original Lehmer Task follows from this implementation review.

## Reproduction

The reviewer-owned [independent_archive_review.py](../../computations/programs/Yin_J_G0156/checks/independent_archive_review.py) retains the separate coefficient/RNG, metric, screen, actual-journal and native-interface checks.
The actual subprocess controls use the label `control_archive_independent_v8`, with the deadline and failure suffixes.
Their temporary native exports use `control_archive_independent_export_v8` under `mathematics/computations/outputs/Yin_J_G0156/`.
The independent result is `independent_archive_review_v8.json` in that output directory.
The affected-interface recheck is retained as `independent_archive_repair_review_v8.json` in that output directory.
The repaired author export self-test used the fresh prefix `control_archive_independent_export_repaired_v8` against the same original subprocess controls.
It performs export and deterministic replay only.

The following commands use Python 3.14.7 and python-flint 0.9.0, with the existing J156 packages directory on PYTHONPATH.
Fresh labels and an absent output destination are required when reproducing the acquisition controls.

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/archive_sampling_checks.py --label control_archive_independent_v8
python -B mathematics/computations/programs/Yin_J_G0156/archive_sampling_export.py self-test --label control_archive_independent_export_v8 --control-label control_archive_independent_v8
python -B mathematics/computations/programs/Yin_J_G0156/checks/independent_archive_review.py --control-label control_archive_independent_v8 --export-label control_archive_independent_export_v8 --output mathematics/computations/outputs/Yin_J_G0156/independent_archive_review_v8.json
python -B mathematics/computations/programs/Yin_J_G0156/checks/independent_archive_review.py --control-label control_archive_independent_v8 --export-label control_archive_independent_export_v8 --retention-only --output mathematics/computations/outputs/Yin_J_G0156/independent_archive_repair_review_v8.json
~~~
