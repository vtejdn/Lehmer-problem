---
author: Yin
---

# Independent review of the post-run sampling-law mass diagnostic

<a id="law-mass-diagnostic-review"></a>
## Finding and arrangement

At 2026-11-09T18:14, a reviewing agent acting for Yin completed a separate independent inspection of J156's post-run law diagnostic and reproduced its documented short calibration calculation.
The reviewer did not develop or repair this diagnostic and received its stable native source, documentation, required journal and reference census directly, without inherited development discussion or prior review conclusions about this diagnostic.
The review reused the unchanged applicable sampler and census findings in [R1111v1](Yin_R_G1111_v1.md), then read the actual interfaces invoked by the new program.
No source repair was made.

The verdict is **PASS for committed-update replay and the stated approximate conditional target-mass calculation on completed journals from the frozen protocol**.
The documented short calibration result was independently reproduced, including an additional exact rational reconstruction of every law snapshot.
No mathematical or implementation defect was found within this scope.
This finding is distinct from the earlier sampler implementation review and from any review of first-pilot performance.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Law-mass diagnostic](#law-mass-diagnostic-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Law-mass diagnostic](#law-mass-diagnostic-review) | [Complete diagnostic source](../../computations/programs/Yin_J_G0156/law_mass_diagnostic.py) | Every function: committed-event replay, exact law updates, approximate finite target sum, output and interpretation. |
| [Law-mass diagnostic](#law-mass-diagnostic-review) | [Documented diagnostic](../../computations/programs/Yin_J_G0156/readme.md#post-run-law-diagnostic) | Entire method, short calibration figures, arithmetic limits and separation from live training and experimental yield. |
| [Law-mass diagnostic](#law-mass-diagnostic-review) | [Frozen sampler interfaces](../../computations/programs/Yin_J_G0156/sampler.py) | Law initialization/update, worker proposal/evaluation/commit event semantics, fixed batch size, and the comparison's exact run-file selection. |
| [Law-mass diagnostic](#law-mass-diagnostic-review) | [Baseline producer](../../computations/programs/Yin_J_G0156/baseline_mass.py) | Degree-specific unique target-prefix list, initial fixed-mixture probability and separation from proposal generation. |
| [Law-mass diagnostic](#law-mass-diagnostic-review) | [Prior sampler finding](Yin_R_G1111_v1.md#sampler-implementation-review) | Reused exact law, score eligibility, core collapse and committed-event interfaces; no expansion to a new pilot verdict. |
| [Law-mass diagnostic](#law-mass-diagnostic-review) | [Prior census finding](Yin_R_G1111_v1.md#baseline-census-review) | Reused completeness and exact finite-box interpretation of the target lists and fixed-law probabilities. |
| [Law-mass diagnostic](#law-mass-diagnostic-review) | [S10 metrics](../../strategies/Yin_S_G0010.md#metrics) | Whole-polynomial target versus distinct certified values, and the separate status of later reference replay. |
| [Law-mass diagnostic](#law-mass-diagnostic-review) | [S10 experiment](../../strategies/Yin_S_G0010.md#first-experiment) | The unchanged one-tenth uniform mixture, adaptive blocks and 256-proposal update rule that the diagnostic reconstructs. |

## Actual inputs and replay verification

The reproduced journal is `mathematics/computations/outputs/Yin_J_G0156/calibration3_adaptive_d14_adaptive_s0.jsonl`.
Its configuration specifies the S10 first-experiment protocol, degree 14, adaptive arm, seed zero, three seconds and batch size 256.
The reference is `mathematics/computations/outputs/Yin_J_G0156/baseline_mass.json`, selecting its degree-14 row and all 26 unique target prefixes.
These are the actual native journal and already checked census, not a new training set or a newly claimed box enumeration.

The diagnostic holds the most recent proposal and evaluation until a commit arrives.
It admits a commit only when its recorded elapsed time is at most the run budget, and it asserts agreement of all three proposal identifiers.
Thus the final unfinished proposal and any final evaluation without an eligible commit do not enter a batch.
A truncated final JSON record ends reading without manufacturing another committed event.

For each admitted event, the diagnostic excludes unresolved errors, unresolved rankings and neutral outputs from the eligible positive batch.
At each multiple of 256 proposals, it applies the unchanged exact update rule and compares the computed update record with the journal's eligible count, unique-core count, elite size and exact elite vectors.
The record comparison is exact; the floating-point scores are the recorded ranking inputs, with JSON round-trip preserving those binary64 values.
The batch then resets.
An incomplete trailing batch changes no law, so the last recorded snapshot is also the law after the remaining committed proposals.

The actual calibration journal has 3432 consecutive committed proposals, one unfinished proposal, 13 update boundaries and 104 committed proposals after the last update at proposal 3328.
All 13 reconstructed update records agree with the journal.
The diagnostic does not need to draw the proposals again: its conditional law is determined by the recorded eligible history and the exact update recurrence.
It does not thereby authenticate arbitrary journals, independently re-certify each historical score, or verify the random-generator history.
Those are separate questions from the assigned replay and mass calculation.

## Conditional probability and arithmetic

Let \(\mathcal T_D\) be the unique target-prefix set from the complete box census, let \(n=D/2\), and let \(w_b(s)\) be the current integer weight of block state \(s\).
The probability of a target polynomial under the reconstructed law is
\[
 q=
 \frac{|\mathcal T_D|}{10\,9^n}
 +\frac9{10}\sum_{a\in\mathcal T_D}
       \prod_b\frac{w_b(a_b)}{\sum_s w_b(s)}.
\]
The first term is the full-vector uniform exploration component, not a separate uniform mixture inside each block.
The blocks partition the entire free vector, including the final singleton at degree 14, so their product gives the biased component's probability of exactly that polynomial.
Summation over unique prefixes counts polynomial events without identifying equal Mahler measures.
The target is the complete polynomial's strict interval \(1<M<6/5\), not a small extracted factor.

The code implements this formula and checks its initial value against the reference's fixed-mixture probability.
The block weights and updates remain exact integers.
The divisions, products, finite sum, factor 0.9 and reported ratio use binary64 arithmetic, as explicitly stated in the native source, result interpretation and README.
The production diagnostic supplies no interval error bound or arithmetic certificate for these sums.
Its approximate values are not converted into certified probabilities, statistical confidence bounds, distinct-value counts or an estimate under the uniform population law.

The reviewer additionally reconstructed the calibration independently using rational block probabilities, without calling either `Law.update` or `target_mass`.
For each committed batch, that reconstruction independently collapsed equal cores, selected the score-ordered elite and verified the exact recorded update metadata.
It then applied
\[
 p_b'(s)=\frac45p_b(s)
       +\frac15\frac{1+N_b(s)}{|\mathcal S_b|+e},
\]
where \(e\) is the elite size, \(\mathcal S_b\) is the block state space and \(N_b(s)\) counts the elite observations.
The rational probabilities summed to one in every block after every update.
Using the displayed target formula, the initial rational sum equalled the census's exact fixed-mixture probability, and all 14 probability snapshots were compared directly with the diagnostic's binary64 values.
The largest relative discrepancy was approximately \(4.231457640776478\times10^{-16}\), and an exact rational comparison placed every discrepancy below \(10^{-14}\).
This additional check concerns these 14 calibration sums; it does not change the native diagnostic into a generally certified arithmetic implementation.

## Reproduced calibration and separation from the pilot

The native reproduction returned
\[
 q_0\approx0.0006508394870701001,
 \qquad
 q_{13}\approx0.00007624683267336697,
 \qquad
 q_{13}/q_0\approx0.11715151613896259.
\]
The independent rational reconstruction rounded to the same documented figures.
These endpoints identify a change in the conditional one-proposal target mass for this short calibration history.
They do not assert monotonicity across updates, a time-normalized discovery advantage, an expected count under wall-clock stopping, or a distinct-value performance comparison.

Reproduction used the documented command with an explicitly separate destination:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/law_mass_diagnostic.py mathematics/computations/outputs/Yin_J_G0156/calibration3_adaptive_d14_adaptive_s0.jsonl --output mathematics/computations/outputs/Yin_J_G0156/independent_law_mass_calibration.json
~~~

The supplementary rational snapshot checks are retained in the generated `mathematics/computations/outputs/Yin_J_G0156/independent_law_mass_exact_check.json`.
The required interpreter and python-flint dependency are those already specified by J156.

The diagnostic creates its own local law object and consumes only the completed journal when reconstructing updates.
Its target census is read solely to evaluate a law snapshot; the target set is not passed to the update rule.
The live sampler neither imports this diagnostic nor reads its output, and the default `.law_mass.json` filename is outside the comparison's exact run-summary filenames.
No proposal, score, elite selection, primary yield or completed run summary is modified by this calculation.
The extra reference work occurs after the selected run and is not added to that run's charged discovery count.

## Limits

This pass applies to completed native journals from the frozen S10 protocol and to the checked degree-specific reference target sets.
The standalone parser does not establish that a run has finished or passed the supervisor's validity checks; the caller must select an actually completed journal.
A partial or foreign-protocol journal, corrupted middle records or an unverified target census is outside this verdict.
The review did not run the optional completed degree-14 pilot diagnostic or inspect the still-running degree-18 and degree-20 comparison outcomes.
The earlier implementation and census findings retain their original scope, while eventual pilot performance requires separate factual evaluation.
No adaptive advantage, novel small measure, asymptotic probability claim or unrestricted Lehmer conclusion is established here.
