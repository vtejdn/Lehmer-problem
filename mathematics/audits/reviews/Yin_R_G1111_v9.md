---
author: Yin
---

# Independent review of the completed reference-seeded archive comparison

## Arrangement and exact scope

At 2026-11-09T21:57, a separately organized reviewer acting for Yin completed the actual-result review below.
The reviewer did not develop the archive implementation, acquire these formal observations, prepare their native export or write the result interpretation.
No substantive implementation-development discussion was supplied.
The reviewer first completed the [v8 implementation finding](Yin_R_G1111_v8.md#archive-implementation-review) and [retention finding](Yin_R_G1111_v8.md#archive-retention-review), and reuses those unchanged sources only at their established scope.
This new review began from the frozen protocol, the completed native inputs, original histories and separately generated certificate output.
The fixed result section was then read and checked against independently reconstructed observations.
No author correction was needed for this result review.

The formal label is `s10_archive_comparison`.
The original histories are every `mathematics/computations/outputs/Yin_J_G0156/s10_archive_comparison_dDEGREE_VARIANT_sSEED.json` and matching `.jsonl`, for exactly degrees 24 and 30, variants fixed/direct/closure, and seeds 20 through 24.
The native inputs are [archive_comparison.json](../../computations/programs/Yin_J_G0156/inputs/archive_comparison.json) and [archive_witnesses.json](../../computations/programs/Yin_J_G0156/inputs/archive_witnesses.json).
The separate full-measure recomputation is [archive_witness_verification.json](../../computations/outputs/Yin_J_G0156/archive_witness_verification.json).
The supplied native-only replay is [archive_retained_replay.json](../../computations/outputs/Yin_J_G0156/archive_retained_replay.json).
These exact inputs and their original-history associations were inspected; successful command return codes were not substituted for their verification.

The new parent-sampling construction, its feasibility experiments and any later algorithm are outside this review.
The existing external degree-classification boundary is reused as the protocol's stated applicability limit; its original exhaustive proof is not reopened.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Completed archive evidence](#archive-results-review) | independently reviewed |
| [Observed inter-core identity](#archive-transition-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Completed archive evidence](#archive-results-review) | [Frozen S10 protocol](../../strategies/Yin_S_G0010.md#cyclotomic-archive-comparison) | Entire declared reference-seeded domain, 30 identities, rotated serial order, twenty-second budgets, whole-target update rule, primary metric, conditional reporting and joint same-seed screen. |
| [Completed archive evidence](#archive-results-review) | [Native observations](../../computations/programs/Yin_J_G0156/inputs/archive_comparison.json) | All thirty configurations, original counts/costs/censors, complete and separate-factor observations, parent joins, archive changes/final states, retry inputs, known-core distinctions and aggregate screen. |
| [Completed archive evidence](#archive-results-review) | [Native witnesses](../../computations/programs/Yin_J_G0156/inputs/archive_witnesses.json) | All 3386 exact vectors, unique IDs, role sets, run memberships and full/factor/parent/seed/archive-template references. |
| [Completed archive evidence](#archive-results-review) | [Separate certificate recomputation](../../computations/outputs/Yin_J_G0156/archive_witness_verification.json) | One-to-one exact-input correspondence, all recorded factor products, multiplicities, cyclotomic status, normalized cores, dyadic threshold implications and compatibility with retained original intervals. |
| [Completed archive evidence](#archive-results-review) | [Portable replay output](../../computations/outputs/Yin_J_G0156/archive_retained_replay.json) | All thirty records, all 352743 proposal reconstructions, 2656 state changes, thirty retry checks and agreement with independent original-history reconstruction. |
| [Completed archive evidence](#archive-results-review) | [Archive source](../../computations/programs/Yin_J_G0156/archive_sampling.py) | Unchanged v8 implementation applied to the actual histories, source identity enumeration, config/report fields, seed-aware accounting and original commit interface. |
| [Completed archive evidence](#archive-results-review) | [Archive exporter](../../computations/programs/Yin_J_G0156/archive_sampling_export.py) | Actual native compaction and associations, complete parent retention, all final retry inputs and the repaired portable-replay interface. |
| [Completed archive evidence](#archive-results-review) | [Frozen worker](../../computations/programs/Yin_J_G0156/sampler.py) | Actual proposal/evaluation/commit stream, 4096-entry per-run LRU, complete certificate interfaces and the unchanged verify-witnesses exact-input loop. |
| [Completed archive evidence](#archive-results-review) | [Shared runtime](../../computations/programs/Yin_J_G0156/sampling_runtime.py) | Actual cap/failure/configuration and observed-duration interface; no new change to supervisor semantics. |
| [Completed archive evidence](#archive-results-review) | [Shared exporter](../../computations/programs/Yin_J_G0156/prior_strength_live_export.py) | Directly reused whole/factor compaction, committed-parent associations and witness role/run definitions as instantiated in the formal export. |
| [Completed archive evidence](#archive-results-review) | [Implementation finding](Yin_R_G1111_v8.md#archive-implementation-review) | Reused fixed and archive probability laws, canonical core assumptions, within-budget composition and seed-aware/same-seed screen semantics; no prior performance conclusion. |
| [Completed archive evidence](#archive-results-review) | [Retention finding](Yin_R_G1111_v8.md#archive-retention-review) | Reused compact recipe and repaired last-retry replay contract; actual thirty-run native contents are newly checked here. |
| [Completed archive evidence](#archive-results-review) | [Original evaluator finding](Yin_R_G1111_v1.md#sampler-implementation-review) | Reused full-root enclosure construction, multiplicity treatment, strict rational threshold contract and trusted FLINT/Arb interface. |
| [Completed archive evidence](#archive-results-review) | [Result prose](../../computations/programs/Yin_J_G0156/readme.md#archive-comparison-results) | Entire completed-result section through its retained-replay subsection: both tables, all numerical claims, actual-parent example, reproduction and finite-result limits; the following larger-class preparation is excluded. |
| [Completed archive evidence](#archive-results-review) | [Independent result checker](../../computations/programs/Yin_J_G0156/checks/independent_archive_results.py) | Complete actual-history reconstruction, exact certificate/native interfaces, aggregate predicate, twelve displayed table rows and the actual transition. |
| [Completed archive evidence](#archive-results-review) | [Independent RNG reference](../../computations/programs/Yin_J_G0156/checks/independent_archive_review.py) | Only ReferenceLaw and the separately implemented sparse coefficient formula, reused at their v8 scope. |
| [Completed archive evidence](#archive-results-review) | [Independent interval helpers](../../computations/programs/Yin_J_G0156/checks/independent_pilot_review.py) | Only exact dyadic bounds, threshold checks, conservative Ledger and independent factor-core normalization. |
| [Observed inter-core identity](#archive-transition-review) | [Result identity](../../computations/programs/Yin_J_G0156/readme.md#archive-comparison-results) | Exact parent/child coefficient statement and both displayed factorization identities for degree 24, closure, seed 20, proposal 7209. |
| [Observed inter-core identity](#archive-transition-review) | [Original transition journal](../../computations/outputs/Yin_J_G0156/s10_archive_comparison_d24_closure_s20.jsonl) | The actual selected parent, zero-based free coordinate two, minus-one sign, evaluated child, complete certificate and on-time commit of proposal 7209. |
| [Observed inter-core identity](#archive-transition-review) | [Two normalized cores](../../computations/programs/Yin_J_G0156/inputs/degree_core_mass_states.json) | The exact normalized Lehmer and degree-eighteen coefficient vectors used in the identity; no new proof of catalog completeness. |
| [Observed inter-core identity](#archive-transition-review) | [Closure generator](../../computations/programs/Yin_J_G0156/cyclotomic_closure.py) | Exact membership of the observed parent in the reviewed seed closure at degree 24 and height four. |
| [Observed inter-core identity](#archive-transition-review) | [Independent result checker](../../computations/programs/Yin_J_G0156/checks/independent_archive_results.py) | Exact polynomial multiplication, observed mutation/commit association and exclusion from the direct initial sparse completions. |

<a id="archive-results-review"></a>
## Completed archive evidence finding

The finding is **PASS for the completed finite comparison, its retained evidence and its qualified interpretation**.
The declared allocation screen passes for these observed thirty runs.
No implementation or evidence discrepancy requiring an author repair was found.
This is an actual finite-result finding, not an assertion that later searches, larger degrees or a different sampler inherit the outcome.

### Complete histories, budgets and state

All thirty required identities are present once, with the requested degree, variant, seed, twenty-second budget, 128-bit evaluator, batch size 256 and fresh per-run 4096-entry cache.
Every configuration matches its original journal and the inspected protocol.
All thirty reached the cap with empty stderr, no worker-failure flag and valid deadline termination.
The original journal creation/finish metadata follows the independently reconstructed rotation, with each journal finished before the next was created.
This corroborates the prescribed serial order alongside the inspected comparison loop; it is not a replay of historical timing.

The reviewer streamed every original proposal, evaluation and commit, checking sequential identities, exact free coefficients, recorded RNG metadata and their independently reconstructed law states.
The check covered 352743 proposal vectors and 352713 on-time completed evaluations.
Each run has exactly one final incomplete proposal, for thirty exact retry inputs.
The original complete histories and the compact native replay agree on the entire proposal prefix, including these final inputs.

Initialization certificates, their committed elapsed times and generated archive classes were checked separately from proposal discoveries.
The initialization stage costs and all committed evaluation stage costs are nonnegative and fit within each twenty-second deadline.
The largest retained evaluation commit time is approximately 19.999932300008368 seconds.
Observed supervisor cleanup exceeds the cap by approximately 0.0106947 to 0.0267527 seconds; that cleanup supplies no discovery credit.
Missing first nonseed hits are censored at twenty seconds in these valid full runs.

Every repeated-proposal flag and cache hit was independently reconstructed with an exact-prefix set and LRU order.
All raw threshold counts, neutral/resolved counts, positive-core repetitions, wider-threshold ledgers, factor ledgers, best updates, first-hit times and stage totals agree with the source summaries and native rows.
The checked totals are 259765 fresh completed evaluations, 92948 cache hits, 101545 repeated proposals and 3790 neutral outputs.
The completed total is 352713.
The distinction between a repeated proposal and a cache hit is preserved after LRU eviction.

Every archive update is associated with an actually committed certified whole target.
No factor-only event or unfinished evaluation changes the reconstructed final archive.
All 2656 state-changing observations, their exact generated/observed template counts and their order agree.
Repeated targets that change no state add neither a template nor extra core weight.
At degree 24, each closure arm begins with 1170 seed templates; precisely seeds 20, 21 and 23 acquire a second core and its 62-template class.
At degree 30, all five closure archives retain the original 5532-template seed class alone.
The displayed initialization ranges, approximately 0.2861710–0.3290282 seconds and 0.7896699–0.8241713 seconds respectively, agree with the original commits.

### Exact metrics and paired screen

The seed-aware ledger was reconstructed with independent rational dyadic endpoint comparisons.
The supplied Lehmer value starts at value zero and contributes no primary discovery credit.
All 3635 raw seed recoveries remain separate.
The 183 raw nonseed target hits represent one known degree-eighteen value, with first discovery in three degree-24 closure runs.
Their three first-hit times are approximately 13.4579694, 17.9530574 and 3.7654560 seconds for seeds 20, 21 and 23.
Their certified measure agrees with the displayed approximation 1.18836814750822358814.
Every other formal run has zero nonseed target values.

| Degree | Closure count nonlosses against fixed | Closure count nonlosses against direct | Joint strict wins on the same seeds |
| ---: | ---: | ---: | --- |
| 24 | 5 | 5 | 3, on seeds 20, 21 and 23 |
| 30 | 5 | 5 | 0 |

The reviewer independently recomputed the whole screen from the verified per-seed metrics.
The three strict wins are joint wins against both comparators on the same paired seeds.
They arise from a larger nonseed-value count, rather than from a small difference between two positive first-hit times.
The remaining zero-zero pairs supply nonlosses but no strict wins.
Completeness, nonloss at both degrees and the required joint-win count therefore all hold.

No observed whole target is outside the supplied two-core catalog or strictly below the seed enclosure.
No target-value equality remains unresolved.
Every recorded separate factor below 6/5 also normalizes to one of these two cores.
This supports the stated finite degree-24 representation-diversity result and the absence of observed nonseed gain at degree 30.
It supplies no literature-new measure, uniform probability ordering or asymptotic improvement.

### Certificates, factor parents and native preservation

The exact witness coefficient set contains 3386 distinct vectors with unique identifiers.
The reviewer checked its one-to-one correspondence, including order, with all 3386 separately recomputed certificates.
For every fresh certificate, exact integer multiplication reconstructs the complete polynomial from its factor powers.
Exact cyclotomic tests agree with their labels; noncyclotomic factor roots and factor exponents give the full recorded degree with multiplicity.
Removing the cyclotomic factors and independently compressing/normalizing the remaining product gives the stated core.
All strict threshold implications were checked with rational endpoints.
Every selected original whole or factor enclosure agrees in its applicable classifications and overlaps the fresh enclosure for the same exact input.

The reviewer additionally checked the same exact factor-product, root-count, normalized-core and threshold interfaces for 3490 distinct coefficient examples present in the original full journal certificates.
Repeated journal observations and their original retained fields were checked at their actual event associations.
The reviewer did not perform another root solve.
The full-root enclosure method and trusted FLINT/Arb implementation retain the [v1 boundary](Yin_R_G1111_v1.md#sampler-implementation-review); these checks validate its actual exact-input and native-evidence use here, not the library's internal proof.

All 1181 run-level whole-discovery records, 1617 separate factor-discovery records, 56 unresolved factor-equality records and 1569 complete parent outputs match their original committed evaluations.
These are within-run associations, not globally distinct measure counts.
Each factor association matches its parent's exact factor, exponent, threshold, whole measure, timestamp, cache/repeat state and charged costs.
The 56 unresolved factor-equality records all have certified measure strictly above 13/10.
They do not represent unresolved 6/5 threshold decisions.
No committed arithmetic-error, ranking-uncertainty or threshold-uncertainty input occurs in the dataset.

Every native whole, seed, best, core-observation, factor and archive-template witness reference was checked against its exact vector.
The complete role sets and run memberships agree, with no missing or unused witness IDs.
Generated template recipes reproduce the actual class, degree, height, ordering and counts.
All original scalar/count/time/configuration fields remain unchanged in the native export.
All thirty final retry inputs preserve their actual prefix, complete reciprocal coefficients, proposal time, unfinished status and any evaluation/certificate that was actually flushed.
Their exclusion from measured yields is maintained.

The reviewer reran portable reconstruction on all thirty native rows and compared every result with the supplied replay output and independent original-history reconstruction.
It reproduces all 352743 proposals, all 2656 state changes and all thirty retry inputs without original journals as generation inputs or another root calculation.
The missing historical timing is not reconstructed by this deterministic replay.

### Result wording and limits

Both README tables, comprising twelve data rows, were checked against the independently reconstructed group statistics and per-seed first hits.
All displayed aggregate counts, known/unknown/below-seed distinctions, factor-equality qualifications, initialization ranges and reproduction claims agree with their actual inputs.
The direct arm's larger completed count includes many cache hits, and its fresh-evaluation counts are much nearer to closure's than the unqualified completed totals suggest.
The result section appropriately avoids a general throughput or probability ordering.

The sample consists of five paired seeds at each of two degrees under a known supplied core.
Passing the fixed allocation screen is a finite exploratory disposition, not a statistical significance claim.
The inspected external classification already covers this calibration range.
Neither a new small-measure primitive core nor a counterexample to the original Lehmer target has been supplied.
The result does not complete the original Task and provides no review coverage for the separate larger-class parent sampler.

<a id="archive-transition-review"></a>
## Observed inter-core identity finding

The finding is **PASS for the exact displayed identity and its association with the actual committed transition**.

At degree 24, closure arm, seed 20, proposal 7209, the original metadata selects the reciprocal parent
\[
P(z)=z^{24}-z^{14}-z^{12}-z^{10}+1.
\]
It selects one free coordinate, indexed two from zero, with sign minus one and no boundary return.
The independent coefficient reconstruction gives
\[
Q(z)=P(z)-z^3-z^{21}.
\]
The event's complete certificate has the catalog's normalized degree-eighteen core, and its commit time is 13.457969400013098 seconds.

For the exact normalized Lehmer core F and the exact normalized degree-eighteen core H in the retained catalog, independent integer polynomial multiplication verifies
\[
P(z)=F(-z^2)(1-z^2+z^4),
\qquad
Q(z)=H(z)(1+z+z^2)(1-z^2+z^4).
\]
The two neutral factors are precisely the stated cyclotomic polynomials of orders three and twelve.
The parent is in the height-four seed closure and absent from the direct arm's initial sparse completion set.
The odd new exponents break the parent's even-power substitution pattern while the order-twelve cyclotomic factor remains.
The resulting noncyclotomic core is the known degree-eighteen H, not a new primitive degree-24 object.

This is a checked retrospective identity for one observed mutation.
It is not a preselected training input, a classification of every successful transition, or proof that all future archive searches reach another core.

## Reproduction

The reviewer-owned [independent_archive_results.py](../../computations/programs/Yin_J_G0156/checks/independent_archive_results.py) retains the full actual-history, exact-certificate, native-association, screen, table and transition checks.
Its directly reused reference functions are bound above; it does not import a new law or change the author inputs.
The actual output is [independent_archive_results_review_v9.json](../../computations/outputs/Yin_J_G0156/independent_archive_results_review_v9.json).
Original journal reconstruction requires the thirty source JSON/JSONL pairs.
Native-only proposal/archive replay remains separately reproducible from the compact comparison and its unchanged generator source, while exact witness inputs support separate complete-measure verification.

The following command uses Python 3.14.7 and python-flint 0.9.0, with the existing J156 packages directory on PYTHONPATH.
Choose an absent output destination to preserve the recorded review output.

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/checks/independent_archive_results.py --output mathematics/computations/outputs/Yin_J_G0156/independent_archive_results_review_v9.json
~~~

