---
author: Yin
---

# Independent exact checks of D21 cycle surgery and barriers

## Question and scope

Independently reproduce the retained [J G0025](../Yin_J_G0025/readme.md) programs without replacing their author outputs and separately implement selected exact identities underlying the complete [C437v2 cycle argument](../../../claims/Yin_C_G0437_v2.md#retained-cycle-proof).
The retained [whole review](../../../audits/reviews/Yin_R_G0083_v1.md#independent-cycle-surgery-review) owns its complete all-size mathematical finding; finite tests do not substitute for those proofs.

## Programs and reproduction

From the repository root, run [review.py](review.py) with Python and SymPy:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0031/review.py
```

The independent part uses sparse permutation-expansion determinant coefficients, not the author's characteristic-polynomial or interpolation methods.
Path checks use accumulated basis columns and exact T T^T-I coupling matrices, which control any number of earlier/later outside coordinates.
All arithmetic is exact; no random input, numerical root or optimization is used.
It imports no author function for those checks.

The final rerun stage loads both inspected author programs and passes this J's explicit output paths to their main functions.
Only the output destination changes.
The author source and outputs remain untouched.
The resulting controls.json (`mathematics/computations/outputs/Yin_J_G0031/controls.json`) and verification.json (`mathematics/computations/outputs/Yin_J_G0031/verification.json`) reproduce every mathematical JSON field in the corresponding J25 outputs.
review-results.json (`mathematics/computations/outputs/Yin_J_G0031/review-results.json`) records the independent results and rerun comparisons.

## Actual results

All 436 ordered-cycle cases of sizes 3--7 passed for both sign products; all 233 rank-four E<=3 inputs exclude the target.
The program passed 119 prefix/final path-basis and coupling-matrix checks for m=3--16.
It also checks the entire collection of 249 rank-four triangle-free signed graphs: all 1494 directed moves obey the degree formula and every one of the 1014 zero changes has the explicit signed-graph permutation/gauge equivalence.
Both author reruns passed and all retained mathematical payloads matched.

The first independent run failed because its zero-move test accidentally demanded equality of ordered bilinear matrices after a vertex permutation.
The actual theorem concerns the symmetric signed graph.
The checker was corrected to that stated object, and the whole run then passed.
This was a reviewer-code error; no author assertion or data was changed.

## Evidence boundary

The reviewer did not contribute to D21 or J25, but received the root's earlier review outcome and shared research context.
The final D31 finding retains the complete written checks of the arbitrary-size arguments.
Its [whole relationship is self-reviewed](../../../audits/reviews/Yin_R_G0083_v1.md#review-relationships) because the earlier written mathematical review and target cycle calculation were supplied before checking; the separate arithmetic implementation and original executions remain distinct facts.
These finite computations alone do not prove an all-size theorem, successful descent for the pendant family, a stabilized congruence obstruction, any small-Mahler-measure coverage or a scalar gap.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
