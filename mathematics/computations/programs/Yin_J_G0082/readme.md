---
author: Yin
---

<a id="complete-positive-scalar-review-declaration"></a>
<a id="complete-positive-scalar-independent-review"></a>
<a id="binary-invariant-pre-run"></a>
<a id="binary-invariant-author-outcome"></a>
<a id="binary-invariant-independent-declaration"></a>
<a id="binary-invariant-complete-independent-review"></a>
<a id="actual-mutation-probe-declaration"></a>
<a id="actual-mutation-probe-author-outcome"></a>
<a id="actual-mutation-complete-review-declaration"></a>
<a id="actual-mutation-complete-native-review"></a>
<a id="repeated-cell-pre-run"></a>
<a id="repeated-cell-author-outcome"></a>
<a id="repeated-cell-independent-declaration"></a>
<a id="repeated-cell-complete-native-review"></a>

# Positive scalar sparse completion and congruence controls

This J contains four distinct completed computations with different mathematical scopes.
Their responsible proofs and whole reviews are [C595 complete positive-scalar proof](../../../claims/Yin_C_G0595_v1.md#positive-diamond-reuse-and-construction)/[current whole SELF](../../../audits/reviews/Yin_R_G0765_v1.md#current-g325-complete-self-finding), [C295 complete binary proof](../../../claims/Yin_C_G0295_v1.md#argument)/[original R159](../../../audits/reviews/Yin_R_G0159_v1.md#binary-congruence-complete-independent-review), [C311 complete congruence proof](../../../claims/Yin_C_G0311_v1.md#argument)/[original R163](../../../audits/reviews/Yin_R_G0163_v1.md) and [C347 complete repeated-cell proof](../../../claims/Yin_C_G0347_v1.md#argument)/[original R171](../../../audits/reviews/Yin_R_G0171_v1.md#repeated-cell-complete-independent-review).
The finite data do not enlarge their all-k, congruence or measure conclusions.

## Native programs, inputs and reproduction

| Stage | Author program/output | Different-method reviewer/output |
| --- | --- | --- |
| Positive scalar | [verify.py](verify.py), result.json (`mathematics/computations/outputs/Yin_J_G0082/result.json`) | [review_independent.py](review_independent.py), review_result.json (`mathematics/computations/outputs/Yin_J_G0082/review_result.json`) |
| Binary invariant | [binary-invariants.py](binary-invariants.py), binary-invariants.json (`mathematics/computations/outputs/Yin_J_G0082/binary-invariants.json`) | [binary-review.py](binary-review.py), binary-review-result.json (`mathematics/computations/outputs/Yin_J_G0082/binary-review-result.json`) |
| Capped mutation | [mutation-probe.py](mutation-probe.py), mutation-probe.json (`mathematics/computations/outputs/Yin_J_G0082/mutation-probe.json`) | [mutation-review.py](mutation-review.py), mutation-review-result.json (`mathematics/computations/outputs/Yin_J_G0082/mutation-review-result.json`) |
| Repeated cells | [repeated-cell-author.py](repeated-cell-author.py), repeated-cell-output.json (`mathematics/computations/outputs/Yin_J_G0082/repeated-cell-output.json`) | [repeated-cell-review.py](repeated-cell-review.py), repeated-cell-review-result.json (`mathematics/computations/outputs/Yin_J_G0082/repeated-cell-review-result.json`) |

From the repository root run `.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0082/<program>`.
Generated files belong to `mathematics/computations/outputs/Yin_J_G0082/`.
Each checker requires its corresponding completed author payload; binary/mutation stages also consume the original positive-scalar matrices.
The binary author explicitly reuses the graph constructor from review_independent.py; mutation-review reuses its labelled-graph/Bareiss helpers, without rerunning the earlier determinant domain.
SymPy is needed for the author determinant/root stages and repeated-cell reviewer; other reviewers use exact standard-library arithmetic.
Programs protect existing results; where provided, `--output` selects a distinct filename in this J output home.
For the original verify.py, inspect useful prior failure facts before replacing its explicitly selected result when unused.
Live author limits are120,60,90,120 seconds respectively; review limits are120,180,180,120 seconds.
Incomplete output remains incomplete, without automatic extension or retry.

## Positive-scalar and binary-invariant scopes

For k=r=3,4,5,6 the positive-scalar stage constructs diamond-plus-long-path V and forked-cycle plus neutral-block Z, with each absolute companion and literal proper cover:24 matrices, maximum rank50.
It retains every full polynomial, complete factor product, C/T continuant, mixed trace, rank, height, strict energy, total squared-entry sum and measure-bound field.
The comparison is equality of full scalar/rank/energy, not assumed integral congruence.
The reviewer independently builds labelled graphs, uses dimension+1 Bareiss pencils, closed matching sums, coefficient convolution and explicit increasing paths.
All632 pencils,24 factor products,40 continuants,72 mixed-trace entries and40651 typed scalar comparisons passed.
Factor products were verified, without independently classifying the library's residual irreducible factors.

The binary stage retains eight full original/symmetrized matrices, every invertible row operation and transform, complete RREF/pivots and both free-coordinate and formula kernel bases.
V ranks are8,12,14,18; Z ranks are6,8,8,10, giving differences2,4,6,8=2k-4.
The reviewer uses independent labelled graphs and highest-bit column cancellation instead of author row RREF.
It checked316 operations,136 full kernel vectors,32 column-span computations and23264 typed comparisons.
Its upstream L330 authorship is disclosed; it contributed none of the new L334 rank/kernel argument.
The original whole-proof context relationship remains unknown because the actual content and initial order of its shared summaries are not established.
The current complete self check and unchanged-native replay are [R540](../../../audits/reviews/Yin_R_G0540_v1.md#current-complete-binary-congruence-finding); the old typed counter23264 and current23259 are separate execution facts, with all mathematical report fields and other counters equal.
The exact conclusion excludes these two forms, including arbitrary same-block stabilization, without excluding every cheaper representative in V's class.

## Capped mutation: complete saved partial search

The complete current mathematics is [C311](../../../claims/Yin_C_G0311_v1.md#statement), with its actual fresh whole proof/native independent finding in [R551](../../../audits/reviews/Yin_R_G0551_v1.md#actual-congruence-whole).
The2026-10-21 read-only full replay matches every mathematical field and other report counter, with current scalar tally2139366 versus saved2139367; both remain distinct execution facts.
The old R163 context relationship remains unknown, and the original capped-search and reported-run facts below are preserved without a new producer or expanded orbit.

Only k3 and k4 original V inputs were searched, with at most4000 sign-normalized states each and E≤5k+5.
Both adjacent Stokes congruence directions are allowed.
The canonical sign gauge traverses the smallest root first and increasing-index breadth-first neighbors, making forest edges negative; zero positive edges means switchable.
The heap priority is positive-edge count, full absolute monodromy trace, energy, depth, state ID.
Each state expands adjacent indices in increasing order, forward then inverse.
Trace is a priority proxy, not a Mahler certificate.
Every admitted full matrix, generator, normalization, parent, cost and every rejected/duplicate/capped attempt remains retained.

The k3 search has4000 states,8040 attempts and3665 unexpanded heap entries, capped at state3943/index11/inverse.
The k4 search has4000 states,7367 attempts and3769 heap entries, capped at state3096/index3/forward.
Each partially expanded current state is additional to its saved heap.
The first unadmitted candidate is reconstructible from its full parent, pair/direction and recorded energy.
`complete-declared-probe` means both bounded probes finished; neither orbit is closed.

Best-priority, minimum-energy and minimum-trace rules deduplicate to k3 state3930 and k4 state0.
The k3 path IDs1,3930 use forward indices0,1 with pair coefficients-1, energies17,18,17, final height1, positive edges3, binary rank8 and absolute trace5.
Its full Q has determinant1.
The k4 endpoint is its initial normalized state with energy22, height1, positive edges4, binary rank12, trace22 and det Q=1.
No improvement at capped k4 is an impossibility or optimality statement.

[C311](../../../claims/Yin_C_G0311_v1.md#statement) retains the complete all-k two-move basis change and sharp temporary-energy barrier.
At k3 the full absolute factor changes from(t-1)²(t+1)^5(t^6-16t^5+3t^4-28t³+3t²-16t+1) to(t-1)²(t+1)³(t^8-6t^7-12t^6-14t^5-10t^4-14t³-12t²-6t+1).
Exact trace-root intervals prove full Mahler saving greater than log(7/4), equally for full covers because the original scalar is unchanged.
The all-k trace reduction2^k alone proves no all-k measure saving.

The reviewer checked all8000 states,15407 attempts,15409 generic bilinear congruences,8000 row ranks,8006 full linear-system traces, six selected matrices/polynomials,126 Bareiss pencils and six factor products:2139367 typed comparisons.
It used generic bilinear multiplication instead of edge updates, row elimination instead of column insertion and full systems instead of DAG traces.
Both incomplete frontiers and partial expansions were checked without extending the search.

## Repeated-cell scope and partial root coverage

The complete current mathematics is [C347](../../../claims/Yin_C_G0347_v1.md#statement), with the actual [R563 whole current self-review](../../../audits/reviews/Yin_R_G0563_v1.md#complete-repeated-cell-current-finding).
Its stdout-only original-domain reconstruction covers the entire mathematical schema and all finite root/undecided outcomes below.
The current exact scalar tally is142272 versus the original saved142275; all other report counters and mathematical records agree, and the three-count difference is retained without an asserted cause.
All four selected program/native files remained byte-identical across that replay; no producer, root-isolation routine, larger domain or output write was performed.
The old R171 whole account retains its actual historical scope and unknown initial substantive context.

For k3–6 all2^k selected-cell subsets give120 full Q/X records and22 companions for s=0,...,k.
The author checks complete congruences, det Q=1, properness, costs and degree-plus-one pencils; all-selected cases retain12 full original/absolute/cover matrices.
There are3084 saved pencils and52 ordered s-pair comparisons.
Exactly one forced(t+1) is removed for trace conversion, with the entire substitution verified.
Real-root intervals use precision2^-24; exterior radii use64-bit dyadic bounds and complete rational products.
Overlapping comparison intervals remain undecided.

Full-product certificates exist for exactly8 companions: k3/s0,1,2,3; k4/s0,3; k5/s4; k6/s5.
The other14 each retain two nonreal trace roots and undecided total cost.
All six k3 comparisons and k4/s0 versus s3 are strict; the remaining comparisons are undecided.
At k3, s2 is cheaper than s1 and s3 dearer than s2; at k4, s3 is dearer than s0.
No largest-root-only comparison replaces complete measure.

The reviewer independently builds graphs/bases and computes Berkowitz characteristic polynomials from full linear systems, then evaluates every saved pencil node.
Descending Laurent conversion, squarefree Sturm remainder sequences and rational binary square-root bounds check all trace/interval/product fields by different methods, without author imports.
All120 subsets,22 companions,3084 pencils,12 matrices,52 comparisons and149 Sturm intervals passed, totaling142275 typed comparisons.
This verifies the exact finite partial root scope; growing-s asymptotics and an optimum over all congruent bases remain outside it.

The [stdout-only complete repeated-cell verifier](repeated-cell-isolated-review.py) reconstructs the original fixed domain in memory and checks it by independent characteristic polynomials and exact Fraction Sturm arithmetic.
Its actual isolated inspection, source limits and comparison with earlier findings are recorded in [R565](../../../audits/reviews/Yin_R_G0565_v1.md#complete-repeated-cell-isolated-finding).

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.

## Recorded runs

The local output names below identify the particular recorded runs used by the linked fixed materials.
Those records retain the original inputs, parameters, known dates and checked scopes; the existing instructions above identify the programs and reproduction commands.
These links locate the original results and checks, without asserting verification of the present README or a new execution.
Generated output files remain local and are not synchronized.

| Local run output | Original result or check record |
| --- | --- |
| `binary-invariants.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0540_v1.md#current-complete-binary-congruence-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0542_v1.md#independent-whole-binary-congruence); [Claim support and recorded result](../../../claims/Yin_C_G0295_v1.md) |
| `binary-review-result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0540_v1.md#current-complete-binary-congruence-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0542_v1.md#independent-whole-binary-congruence); [Claim support and recorded result](../../../claims/Yin_C_G0295_v1.md) |
| `mutation-probe.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0551_v1.md#actual-congruence-whole); [Claim support and recorded result](../../../claims/Yin_C_G0311_v1.md) |
| `mutation-review-result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0551_v1.md#actual-congruence-whole) |
| `repeated-cell-output.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0171_v1.md#repeated-cell-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0563_v1.md#complete-repeated-cell-current-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0564_v1.md#complete-repeated-cell-separate-self-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0565_v1.md#complete-repeated-cell-isolated-finding); [Claim support and recorded result](../../../claims/Yin_C_G0347_v1.md) |
| `result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0542_v1.md#independent-whole-binary-congruence); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0551_v1.md#actual-congruence-whole) |
