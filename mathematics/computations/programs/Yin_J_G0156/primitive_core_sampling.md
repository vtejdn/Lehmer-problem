# Degree-56 primitive-core implementation and bounded controls

This is the implementation of [S10's frozen primitive-core comparison](../../../strategies/Yin_S_G0010.md#primitive-core-comparison) in the existing J156 group.
It compares fixed Lehmer parents from sparse completions with DP closure parents at degree 56, without online core or template feedback.
The implementation and the actual bounded controls have passed the [independent composition finding](../../../audits/reviews/Yin_R_G1111_v11.md#primitive-implementation-review) and [corrected-retention finding](../../../audits/reviews/Yin_R_G1111_v11.md#primitive-retention-review).
The unchanged formal ten-run comparison is complete, with its [actual results](#primitive-comparison-results), native inputs and separate witness recertification retained below.
The formal results have passed the [independent actual-result finding](../../../audits/reviews/Yin_R_G1111_v12.md#primitive-results-review), [native-retention finding](../../../audits/reviews/Yin_R_G1111_v12.md#primitive-results-retention-review) and [interpretation finding](../../../audits/reviews/Yin_R_G1111_v12.md#primitive-results-interpretation-review).

## Programs and reuse boundary

[primitive_core_sampling.py](primitive_core_sampling.py) owns the dedicated worker, exact structural diagnostics, separate ledgers, run identities and summaries.
It calls the unchanged [full evaluator](sampler.py) and [hard supervisor](sampling_runtime.py).
The common precision remains 128 bits, the ranking tolerance remains `1e-12`, and the exact-polynomial LRU cache has 4096 entries and resets for every run.
Complete polynomial factorization, all exterior-root contributions and multiplicities remain the evaluator's responsibility.
Structural information independent of the parent is cached with the certificate; the current parent's neutral diagnostic is recomputed and charged even for a cached whole polynomial.
The unchanged [DP helper](cyclotomic_parent_sampling.py) and its [reviewed probability scope](../../../audits/reviews/Yin_R_G1111_v10.md#parent-law-review) supply integer counts, ranks and final height rejection, not a new-core discovery assertion.
The previously reviewed archive sampler, DP helper, evaluator and runtime are not edited.

[primitive_core_sampling_checks.py](primitive_core_sampling_checks.py) contains exact polynomial fixtures, deterministic stopping and incomplete-input controls, the five bounded child controls, and retention regressions.
[primitive_core_sampling_export.py](primitive_core_sampling_export.py) retains observations and exact inputs, reconstructs generation from those inputs, and never computes a Mahler certificate during export or generation replay.

## Parent generation, write-ahead records and stopping

Every run certifies the sole supplied Lehmer core inside its own clock and then builds either the direct parents or the DP table.
There are ten distinct direct sparse parents at degree 56, stored in lexicographic free-prefix order.
The DP table uses neutral degree limit 46 and the helper's explicit order-bound budget of 20000.
No precomputed parent output or second target core enters either worker's generator.
The two-core local catalog is read only by post-run classification.

The proposal law is the frozen one-tenth uniform box mixture with the specified one-to-three-coordinate unit mutation otherwise.
Coordinates are sampled without replacement, sorted, and then assigned independent uniform signs in the same order as the archive comparison.
An out-of-box move returns the unchanged parent and records the actual change as zero.
The full parent coefficients, substitution index, sign, exact neutral polynomial and mutation are retained for a generated parent-based proposal.
Uniform-box draws record the parent diagnostic as inapplicable.

`LoggedParentSampler` is a small subclass whose raw selection uses exactly the helper's three integer `randrange` choices and its unchanged `select_k` and `construct` methods.
Before these choices, `raw_attempt_intent` is flushed with request, global attempt and request-local attempt identifiers.
Before polynomial construction, `raw_attempt_ticket` is flushed with the substitution ticket, selected index, sign ticket, sign and neutral rank.
The observational callback records each completed acceptance or height rejection and its charged construction time.
Raw rejected polynomials can be reconstructed from their tickets; their complete coefficient arrays are not duplicated in the native retention.
Accepted raw outcomes retain their exact coefficients and factor multiplicities.

Generation requests, branch choices, returned parents and mutation intents have separate events before a complete `proposal` event exists.
A hard interruption can therefore leave a selection pending, a raw construction pending, a completed accepted parent awaiting return, or a mutation awaiting a whole proposal.
Portable replay identifies that actual last recorded stage and reconstructs deterministic pending inputs where possible.
Such reconstructed inputs are explicitly labelled as replayed pending inputs, not observed completed parents, evaluations or discoveries.
Every journalled proposal is covered, including a final proposal whose elapsed time exceeds the budget and is consequently omitted from the frozen within-budget proposal count.

Each DP parent call has an immutable limit of 4096 raw attempts.
Exhaustion stops the run without a substitute parent or uniform fallback and overrides the old runtime's generic validity with `parent_attempt_limit`, invalid for a full-budget comparison even if the recorded elapsed time reaches the deadline.
Arithmetic failures, unresolved numerical results, ordinary hard deadlines and parent-supply exhaustion remain distinct.
The hard supervisor can interrupt an in-flight attempt; the ideal accepted-parent law is not asserted to remain conditionally uniform after selecting returns by hard completion time.

Setup, all rejected attempts, diagnostics, factorization, roots, cache handling and journal writes occur within the run clock.
The same predeadline evaluation-commit boundary controls every discovery and structural count.
An uncommitted evaluation can carry a certificate as retained evidence but contributes no measured yield.
Completed raw construction times and parent-call elapsed times are retained with a warning that these totals overlap; the observed run clock also charges unfinished generation and serialization.
Post-run native export is bookkeeping and cannot promote a pending input into an experimental completion.

## Exact structure, value ledgers and minimum enclosure

The primary structural class consists of whole outputs that are themselves noncyclotomic, irreducible, degree 56 and exponent gcd one.
It is checked from the exact factorization of the original output, rather than inferred from the degree of an aggregate normalized core.
Monicity already gives coefficient-content primitiveness; the separately tested exponent gcd is the substitution condition in this protocol.
A single irreducible cyclotomic polynomial such as \(\Phi_{87}\), of degree \(\varphi(87)=56\) and exponent gcd one, is neutral and excluded from this primary class.

For a parent \(P=F(\varepsilon z^j)C\), the implementation records the actual \(\Delta\) and computes \(G=\gcd(C,\Delta)\) exactly.
Because \(G\) divides both \(P\) and \(\Delta\), it divides the child and bounds its noncyclotomic total degree by \(56-\deg G\).
This calculation is a diagnostic, never an implicit rejection or redraw rule.
The child's complete cyclotomic part is retained separately, and its quotient by \(G\) records additional neutral multiplicities, including additional copies of an order already present in the parent.
The raw noncyclotomic product retains multiplicities; its exponent compression and the frozen sign-normalized whole core are separate fields.
Each irreducible factor retains its own original coefficients, degree, multiplicity and exponent gcd.
The compressed/sign-normalized factor field applies only to noncyclotomic factors; cyclotomic items explicitly have `noncyclotomic_normalization_applicable=false` and a null normalized-coefficient field.
This prevents the frozen whole-core operation, which removes a cyclotomic factor entirely, from being mistaken for exponent compression of that factor itself.
The normalized whole core is not asserted irreducible merely because its factors have been aggregated.
Neutral retention, added neutral factors, reducibility and exponent compression may overlap as explanations.

One independent gcd fixture uses a single noncentral paired move
\[
 \Delta=\pm z^i(1+z^{56-2i}),\qquad 1\le i<28.
\]
Writing \(r=56-2i\), the factor \(\Phi_m\) divides \(1+z^r\) exactly when \(m\mid2r\) and \(m\nmid r\).
All roots of \(1+z^r\) are simple, so this move retains exactly one copy of such an order from \(\Phi_m^e\mid C\), irrespective of \(e\ge1\).
The central move is a signed monomial and is coprime to every such \(C\), which has constant coefficient one.
The zero change from a boundary return instead gives \(G=C\).
These order-based predictions are compared with polynomial gcd on a neutral polynomial containing repeated orders 2, 4 and 12.

Whole-target and primary-target value ledgers are independent and both begin with the supplied Lehmer reference, which receives no discovery credit.
Different coefficient cores with overlapping measure enclosures remain explicit unresolved equalities.
All whole targets, seed recoveries, strictly-below-seed witnesses, and small irreducible factors remain visible even when the whole output is outside the primary class.
Every factor certificate has its exact whole parent, full parent measure, generation branch and charged per-proposal costs in the retained evaluation record.
Primary coefficient-core counts are separate from separated-value counts.

The primitive near-miss interval requires certified \(M\ge6/5\) and \(M<13/10\); a threshold overlap is not rounded into that interval.
For primitive minima, `PrimitiveBest` keeps every coefficient core not proved worse than the smallest current upper bound, along with its first occurrence.
If the candidate enclosures are \([a_i,b_i]\), the observed finite minimum is enclosed by \([\min_i a_i,\min_i b_i]\).
A core with lower bound larger than the smallest upper bound is safely removed from the contender set.
Overlapping contenders remain explicit, and the selected witness is not called the uniquely certified minimizing core unless only one coefficient core remains.

## Native retention and portable replay

Formal defaults are `inputs/primitive_comparison.json.gz` and `inputs/primitive_witnesses.json`; occupied destinations are refused, and an incomplete ten-run set requires explicit `--allow-partial`.
The gzip comparison contains the same native JSON document, with no field selection or mathematical transformation; the exporter reads either plain JSON or gzip JSON.
This storage extension was added after the formal runs because the complete plain comparison occupied 245930042 bytes, and its actual lossless retention is separate from the earlier implementation review.
Each run retains its original configuration, supervision, counts, costs, thresholds, committed and incomplete scope, all generation inputs, and every journalled successful whole evaluation's compact certificate with exact irreducible factors.
Compact certificates retain coefficients, normalization, dyadic whole/factor intervals, precision, threshold outcomes, factor multiplicities and root counts; the original full root records remain reproducible from the exact witnesses.
Failed or unresolved inputs and final incomplete whole proposals remain separate retry records.
Pending parent-generation evidence remains available even when no whole proposal was formed.
No retry or replay increases the historical yield.

`generation_trace.schemas` supplies each event kind and its ordered field names.
Every `generation_trace.rows` entry begins with a schema index and then supplies those exact field values in that order.
Different actual field sets have different schemas, so an absent field stays distinguishable from an explicitly present JSON null.
Identifiers, ranks, degrees, coefficients and factor powers remain exact JSON integers; acceptance flags remain Booleans, elapsed times and observed costs remain the original finite numeric observations, and arrays and dictionaries retain their original structure.
Raw rejection rows need only exact tickets, completion and acceptance state, height, elapsed time and charged construction time; complete rejected coefficients and powers can be rebuilt.
There is no second copy of every ticket inside the replay summary.
The exporter checks lossless row-table round trips before publishing native data.

Before retaining a run, the exporter rebuilds its full raw summary from the available journal and compares every field and scalar type with the saved summary.
This checks initialization, generation and pending-attempt counts, completions, costs, certificate ledgers, structural metrics and validity together; an invalid run still requires its known generated inputs.
The supervisor's original observations are reused, rather than inferred from a missing journal.
Only its explicit recorded failure to obtain a worker configuration can permit absent or empty journal evidence, and the entire summary must agree with zero generation and the empty startup-failure ledgers.
An absent journal is therefore not itself evidence that the worker never produced one.
A missing, empty or shortened journal that contradicts the original summary raises an error before export publication or witness insertion for that run.
A normal hard deadline can still leave no `finish` event and a partial final JSON line; the frozen reader's complete prefix is accepted when it reconstructs the recorded summary exactly.
This is a consistency check against retained observations, not a claim that a summary hashes every original journal byte or can restore evidence already lost before that summary was recorded.

## Actual bounded implementation controls

Exact factorization fixtures pass for a genuinely primitive low-degree polynomial, repeated factors, an exponent-compressed degree-56 polynomial, a reducible polynomial whose normalized aggregate core still has degree 56, and the neutral \(\Phi_{87}\) case.
These fixtures require no new high-degree Mahler roots.
The independent paired-move/order gcd checks pass at five coordinates, together with the central, unchanged-parent and uniform-branch cases.
A deterministic rejection stub exercises all 4096 helper attempts and confirms exhaustion remains invalid even under a simulated reached hard cap.
Mechanical replay checks cover interruption before and after the raw ticket, pending mutation, the after-cap whole-proposal boundary, and the ten-identity rotated schedule.
A mocked `Popen` error exercises the actual runtime's no-configuration startup-failure branch without launching a child; that recorded failure remains invalid and exports no invented candidate.
Separate interval fixtures check seed exclusion in both independent ledgers, unresolved seed overlap and conservative minimum contenders.

Exactly the following five actual child controls were executed, all under two-second ceilings and outside the formal seeds:

| Arm | Seed | Proposal limit | Completed proposals | Termination | Primary structural occurrences | DP raw attempts | Height rejections | Accepted DP parents |
| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| direct | 100 | 32 | 32 | proposal limit | 12 | 0 | 0 | 0 |
| dp_closure | 101 | 32 | 32 | proposal limit | 13 | 3092 | 3063 | 29 |
| direct | 102 | none | 237 | deadline | 77 | 0 | 0 | 0 |
| dp_closure | 103 | none | 92 | deadline | 42 | 7136 | 7051 | 85 |
| dp_closure | 104 | none | 0 | deliberate worker failure | 0 | 0 | 0 | 0 |

The aggregate authorized subprocess budget ceiling was ten seconds.
The two proposal-limited controls stopped after approximately 0.507 and 0.996 seconds; the deadline controls each used the two-second observed cap.
Each deadline control retained one incomplete whole proposal.
The deliberately failed DP-arm control stopped after its first whole proposal, which happened to use the uniform branch, and is invalid with zero completions.
It therefore checks worker failure after proposal generation, not a measured DP-construction interruption; the latter boundary is covered by the mechanical fixtures.
No numerical evaluation error was observed in the four successful controls.
The direct deadline control had four cache hits; the others had none.
Every control has zero primary target values, zero nonseed whole-target values and zero primitive near-miss cores below \(13/10\).
The DP controls each recovered the supplied seed once, which contributes no discovery credit.

The smallest primitive whole-measure enclosures selected in the four successful controls have decimal centers approximately 1.7781755012, 2.1618420773, 1.6850396767 and 2.0823236789 in the row order above.
Their exact dyadic intervals, witnesses and first occurrences remain in the control records; these decimal displays do not classify any value near a threshold.
These short controls demonstrate executable behavior and checked scope, not a comparative mechanism advantage or a new small measure.

All 396 journalled whole proposals, including the three incomplete or failed ones, and all 10228 completed DP raw attempts reproduce from the preserved generation inputs.
The temporary compact comparison contains 651 distinct exact whole/factor/seed certificate witnesses.
The retention refinement reduced its comparison file from 33181261 to 5282054 bytes by removing a duplicate ticket list, encoding generation events as a lossless row table and omitting decorative JSON whitespace.
The regression compared all 33329 generation events and checked exact JSON values and scalar types for all certificates, metrics, timing, costs and failure inputs.
It also checked that the 10228 removed ticket copies are already present in the retained generation events.
No additional sampling or root certification was performed for this retention regression.

The first five control journals used the frozen whole-core convention `[1]` in the cyclotomic factor's normalized-coefficient field; those original observations are preserved.
The current interface explicitly marks that field inapplicable instead, retaining the original irreducible factor coefficients and degree.
A pure exact-factor-data regression checked all 395 journalled diagnostic records and their 395 compact-native counterparts, including 517 cyclotomic factor entries in each copy.
Only the applicability declaration and the replacement of that cyclotomic field by null differ; every coefficient, degree, structural classification and primary count is unchanged.
This representation correction required no new sampling or root certification.

The journal-evidence regression reconstructs all five original control summaries exactly and rejects eleven insufficient-evidence fixtures.
These include the original 32-completion summary with a missing, empty, config-only or commit-31 prefix journal, the genuinely failed seed-104 run after its first proposal with missing or empty input, and a failed DP-prefix fixture with zero whole proposals but a known pending raw attempt.
The latter fixture uses the observed first raw-attempt prefix from seed 101 and explicitly synthetic failure supervision, without inventing any completion.
It also rejects a no-configuration marker contradicted by recorded generation or by a nonempty generation journal lacking configuration.
Five permitted fixtures cover the preserved pending DP input, the actual runtime's mocked startup-exception branch with absent, empty or incomplete initial journal, and the observed direct deadline prefix with an appended partial final line and no `finish` event.
These checks neither launch subprocesses nor perform sampling or root certification, and they leave the original history unchanged.
Re-export and generation replay of the same five controls still retain 396 whole proposals, 10228 raw attempts and 651 exact witnesses; the compact comparison and witness files are byte-identical to their earlier compact counterparts.

The actual local results are `control_primitive_impl_v1_checks.json`, `control_primitive_retention_v2_checks.json`, `control_primitive_payload_v3_checks.json`, `control_primitive_structure_v4_checks.json`, `control_primitive_final_mechanical_v5_checks.json`, `control_primitive_evidence_v6_checks.json` and `control_primitive_retention_v7_checks.json` under `mathematics/computations/outputs/Yin_J_G0156/`.
The latest checked temporary native comparison and witnesses use the `control_primitive_retention_v7_native_` prefix under that same output directory; the previous outputs remain preserved.

## Reproduction and formal commands

Use Python 3.14.7 with the existing `python-flint==0.9.0` dependency, from the repository root.
A fresh label reproduces mechanical and exact fixtures without stochastic child runs:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/primitive_core_sampling_checks.py --label control_primitive_mechanism_recheck
~~~

The following mode executes exactly the five two-second child controls; observed deadline prefixes and historical timing need not match on another execution:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/primitive_core_sampling_checks.py --label control_primitive_recheck --actual-controls
~~~

Existing child journals can instead be exported and replayed without new sampling or Mahler roots:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/primitive_core_sampling_checks.py --label control_primitive_retention_recheck --export-controls control_primitive_impl_v1
python -B mathematics/computations/programs/Yin_J_G0156/primitive_core_sampling_checks.py --label control_primitive_evidence_recheck --evidence-controls control_primitive_impl_v1
python -B mathematics/computations/programs/Yin_J_G0156/primitive_core_sampling_export.py replay-retained mathematics/computations/outputs/Yin_J_G0156/control_primitive_retention_v7_native_comparison.json
~~~

The frozen formal command sequence is:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/primitive_core_sampling.py compare --label s10_primitive_core_comparison
python -B mathematics/computations/programs/Yin_J_G0156/primitive_core_sampling.py report --label s10_primitive_core_comparison
python -B mathematics/computations/programs/Yin_J_G0156/primitive_core_sampling_export.py export --label s10_primitive_core_comparison
python -B mathematics/computations/programs/Yin_J_G0156/primitive_core_sampling_export.py replay-retained mathematics/computations/programs/Yin_J_G0156/inputs/primitive_comparison.json.gz
~~~

The formal schedule is direct then DP for seed 30, DP then direct for seed 31, alternating through seed 34, at twenty seconds per run.
No failed identity is automatically rerun or replaced.
All ten identities must be valid before a full-budget comparison, and zero-zero outcomes are not improvements or significance results.
Separate full witness recertification, when selected, uses the unchanged `sampler.py verify-witnesses` command and a fresh output path; it does not recreate the historical timing or add discoveries.

<a id="primitive-comparison-results"></a>
## Completed formal degree-56 comparison

All ten prescribed identities completed with valid twenty-second deadlines, totaling 200 seconds of formal sampling budgets.
The declared alternating serial order was retained, without reruns, substituted seeds, online core feedback or a change to the proposal laws.
All ten primary discovery counts and all ten nonseed whole-target counts are zero.
Every primary first-hit time is therefore censored at twenty seconds.
No primitive degree-56 near-miss in \([6/5,13/10)\) occurred, and no whole output or separate factor was certified below the supplied Lehmer value.

The following minima are complete whole measures within the specified noncyclotomic, irreducible degree-56, exponent-gcd-one class.
Their decimal centers are displays only; the original dyadic enclosures and exact witnesses determine comparisons.
Each run's surviving minimum set contains one certified minimizing coefficient core among that run's observed primary outputs.
The last column is the first committed occurrence of that selected core.
Times in the table are rounded to seven decimal places.

| Arm | Seed | Completed evaluations | Primary occurrences | Distinct primary coefficient cores within run | Minimum \(M\), approximate | First minimum, seconds |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| direct | 30 | 2992 | 907 | 879 | 1.4481829018 | 5.9554125 |
| direct | 31 | 2940 | 869 | 848 | 1.4821881437 | 4.3512612 |
| direct | 32 | 3015 | 910 | 882 | 1.4481829018 | 5.9685236 |
| direct | 33 | 3030 | 939 | 903 | 1.4481829018 | 15.7237791 |
| direct | 34 | 3037 | 896 | 864 | 1.3606107463 | 7.6544307 |
| dp_closure | 30 | 1076 | 521 | 521 | 1.7745592271 | 5.3307475 |
| dp_closure | 31 | 1072 | 495 | 495 | 1.9040838203 | 9.0476239 |
| dp_closure | 32 | 1090 | 508 | 508 | 1.6951471325 | 8.0440840 |
| dp_closure | 33 | 1063 | 493 | 493 | 1.8650643290 | 13.8584934 |
| dp_closure | 34 | 1063 | 521 | 521 | 1.9401586029 | 16.4429528 |

The next table sums run-local counts; its distinct-core column is not a deduplicated union across seeds.
Primary occurrences are structural outputs, not discoveries below the target.

| Arm | Completed | Primary occurrences | Sum of within-run primary core counts | Fresh evaluations | Cache hits and repeated proposals | Neutral outputs | Seed recoveries |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| direct | 15014 | 4521 | 4376 | 12597 | 2417 | 117 | 15 |
| dp_closure | 5364 | 2538 | 2538 | 5364 | 0 | 0 | 208 |

The DP arm has the larger primary fraction among completed outputs, \(2538/5364\) versus \(4521/15014\), but fewer primary occurrences under the equal total arm budgets.
Its primitive minimum is also larger in each same-seed comparison.
These are observations of the ten fixed runs, not significance statements or a general ranking of the kernels.
The zero-zero target outcome supplies no improvement in the primary discovery metric.

The DP history retains 383953 completed raw parent attempts, including 379107 height rejections and 4846 accepted raw parents.
The recorded committed generation-and-proposal-I/O fields total approximately 51.2003 seconds for DP and 1.1078 seconds for direct; committed root-certification fields total approximately 41.9167 and 85.5201 seconds respectively.
Those are their named stage fields, not a partition of all clock time; initialization, unfinished work and remaining serialization are paid by the same observed budgets, and separate parent-call and raw-construction totals overlap.
The direct initialization events occur approximately between 0.2514032 and 0.2768719 seconds, and the DP events between 0.2501314 and 0.2850354 seconds, including the pre-launch clock boundary.

Residual mechanisms remain distinct and can overlap.
Direct has 3691 committed outputs retaining old neutral factors, 7789 with additional neutral factors, 1542 with output exponent gcd greater than one, 1513 with compressed raw noncyclotomic products, and 13 with reducible noncyclotomic products.
The corresponding DP counts are 2606, 285, 7, 45 and 2.
Neither the old-neutral gcd condition nor aggregate noncyclotomic degree alone explains the primary class.

All 223 raw whole-target recoveries have the supplied Lehmer core.
Every separated factor value below \(6/5\) also normalizes to that core; factor observations do not add whole-output yield.
There are no committed numerical evaluation failures, unresolved rankings or threshold classifications, and no unresolved whole-value or primary-value equalities.
Two separate factor-value equalities remain unresolved in the direct arm, both certified above \(13/10\) and below \(7/5\); they do not affect the target conclusion.

### Exact observed minima

Write the supplied canonical core as
\[
 F(z)=z^{10}-z^9+z^7-z^6+z^5-z^4+z^3-z+1.
\]
The direct minimum is seed 34, proposal 1074, witness `w14506` in [the native witness document](inputs/primitive_witnesses.json).
Its exact polynomial is
\[
 P_{\rm direct}(z)=F(-z^3)(1+z^{26})
                 +z^{14}(1+z^3)(1+z^{25}),
\]
and the retained enclosure proves
\[
 1.36061074625003<M(P_{\rm direct})<1.36061074625004.
\]
The DP minimum is seed 32, proposal 448, witness `w20305`, with
\[
 P_{\rm DP}(z)=F(z)\Phi_3(z)\Phi_4(z)\Phi_7(z)\Phi_{12}(z)
                      \Phi_{15}(z)\Phi_{30}(z)\Phi_{60}(z)+z^{28},
\]
and
\[
 1.69514713254698<M(P_{\rm DP})<1.69514713254699.
\]
Exact polynomial multiplication agrees with both retained coefficient arrays, and exact rational comparison places their dyadic enclosures strictly within the displayed decimal brackets.
These are finite observed minima above the near-miss threshold, not new global minimum claims or selected shrinking-measure families.

### Retained evidence and reproduction limits

The [gzip native comparison](inputs/primitive_comparison.json.gz) preserves all ten summaries, generation traces, original costs, evaluation observations and incomplete states.
Its decompressed bytes agree exactly with the original 245930042-byte plain export; the gzip file occupies 36848465 bytes, and the redundant plain input was removed after that comparison.
The [native witness document](inputs/primitive_witnesses.json) retains 24425 distinct exact seed, whole and factor inputs with their roles and run associations.
The separate `primitive_witness_verification.json` under the J156 output home freshly certifies every one of those inputs with the unchanged full evaluator.
Their exact coefficient arrays agree one-to-one with the witness document.

Portable replay completed for all 20388 generation requests, all 383953 raw attempt inputs and all 20385 journalled whole proposals.
There are 20378 committed evaluations, seven incomplete whole proposals and three final DP generation requests with no whole proposal.
No completed raw attempt is represented as an interrupted raw construction.
The actual replay output is `primitive_retained_replay.json` under the J156 output home.
Neither replay, new root certification nor storage compression adds a historical completion or discovery.

The additional reproduction command for the witness check is

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py verify-witnesses mathematics/computations/programs/Yin_J_G0156/inputs/primitive_witnesses.json --output mathematics/computations/outputs/Yin_J_G0156/primitive_witness_verification_recheck.json
~~~

Use a fresh verification output path and preserve the existing actual result.
The [independent formal-result review](../../../audits/reviews/Yin_R_G1111_v12.md#primitive-results-review) checks all ten original histories, exact structural classifications, complete certificate interfaces and finite outcomes.
Its [retention finding](../../../audits/reviews/Yin_R_G1111_v12.md#primitive-results-retention-review) checks every retained mathematical field against the original histories and the gzip interface; the comparison with the removed plain export remains the main agent's actual byte check.
Its [interpretation finding](../../../audits/reviews/Yin_R_G1111_v12.md#primitive-results-interpretation-review) checks the result tables, exact minimum formulas and fixed-support deduction, without reviewing the separate later root-cost diagnostic or a future search law.
