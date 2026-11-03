---
author: Yin
---

<a id="complete-independent-review-declaration"></a>
<a id="complete-independent-computation-review"></a>
<a id="same-path-reproduction"></a>

# Actual overlapping Salem and Lehmer endpoint profiles

[C594](../../../claims/Yin_C_G0594_v1.md#actual-salem-profile-finite-theorem) owns the complete mathematical argument.
The exact domain is the quartic Salem polynomial[1,-1,-1,-1,1] at consecutive windows b=7,8,9,10 and original Lehmer polynomial[1,1,0,-1,-1,-1,-1,-1,0,1,1] at b=12, all coefficients ascending.
Earlier quartic b≤6 results are reused, not rerun by this calculation.
All618921 original ternary words use probabilities1/4,1/2,1/4.
Every endpoint retains its exact count, full Gram data and rational projection energy A/B, tested by c^B*2^A<=c0^B.

## Programs, data and reproduction

[profile.py](profile.py) uses standard-library integer convolution and Fraction inversions.
result.json (`mathematics/computations/outputs/Yin_J_G0080/result.json`) retains every matrix, projection identity and maximum-energy certificate for each occurring count, with a maximizing endpoint/word.
The five lossless endpoint payloads are quartic b7 (`mathematics/computations/outputs/Yin_J_G0080/quartic_b7.json.gz`), b8 (`mathematics/computations/outputs/Yin_J_G0080/quartic_b8.json.gz`), b9 (`mathematics/computations/outputs/Yin_J_G0080/quartic_b9.json.gz`), b10 (`mathematics/computations/outputs/Yin_J_G0080/quartic_b10.json.gz`) and Lehmer b12 (`mathematics/computations/outputs/Yin_J_G0080/lehmer_b12.json.gz`).
Each row is[endpoint,count,energy numerator,energy denominator,inequality status], in lexical endpoint order.
[review_independent.py](review_independent.py) consumes the complete report and all five payloads, and writes review_result.json (`mathematics/computations/outputs/Yin_J_G0080/review_result.json`).
The reviewer also requires SymPy.

From the repository root run the selected operation:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0080/profile.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0080/review_independent.py
```

Both default operations protect existing outputs.
Before an intentional regeneration, inspect prior useful failure/inspection facts and remove only the selected operation's replaceable outputs in `mathematics/computations/outputs/Yin_J_G0080/` when no agent is using them.
For author reproduction those are result.json and the five payloads; for reviewer reproduction only review_result.json.
Keep all complete author inputs for the reviewer.
A previous review concerns its actual inputs and does not certify newly regenerated output.

## Completion and finite scope

Quartic endpoint counts are1267,2901,6451,13989 with central numerators152,328,708,1532.
Lehmer b12 has465329 endpoints and central numerator4256.
All489937 endpoint comparisons pass, with zero the unique equality endpoint in each domain and605 complete count/maximal-energy classes.
The [actual independent declaration and finding](../../../audits/reviews/Yin_R_G0148_v1.md#retained-j80-reviewer-execution-account) retain the different-method comparison, whole-proof review and participation limits.
No unrestricted C1 or near-one total-measure theorem follows.

The author enforces its120-second live cap during traversal, after serialization and after final report publication.
An exception or late timeout removes only the result created by that invocation and writes `failure.json` with `complete:false`, the actual error and completed-domain boundary.
Previously written completed-domain payloads remain partial evidence; the reviewer requires a complete report.
Mathematical `all_passed` is distinct from operational completion, so a fully traversed domain can retain failed inequalities.
The terminal-publication regression was originally checked on a disposable quartic b5 domain with211 endpoints at controlled119/120/121-second boundaries and a serialization exception; this was no new execution of the five historical domains.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
