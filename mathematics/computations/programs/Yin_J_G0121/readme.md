---
author: Yin
---

# Three-update zero-middle pattern pairs and a fixed actual connecting chain

## Question and scope

Certify exactly the 81^2 ordered four-digit ternary middle-pattern pairs for both alternating three-update orders, with the strict two-real-place rectangle conditions and complete current-length argument fixed in [C610v1](../../../claims/Yin_C_G0610_v1.md#argument).
Separately test one specified seven-update word chain at the SAME n=26, using original probabilities and full tail representations.
No length scan or subsequent pattern bound is selected.

## Files

- [inputs.json](inputs.json) specifies the exact two intermediate patterns, five complete new tails, the old native input path and fixed k=24.
- [main.py](main.py) certifies all 81^2 pairs, both strict rectangle screens, actual strict core states, the eight full returned words and original probability numerators/denominator endpoints.
- [discover.py](discover.py) preserves the fixed length-24, five-target tail discovery.
- [verify_independent.py](verify_independent.py) independently reconstructs every pair decision, quotient-ring identity, full-word transition and fixed discovery-table count using polynomial division, termwise rational intervals and endpoint sets.
- certificate.json (`mathematics/computations/outputs/Yin_J_G0121/certificate.json`) retains all pair verdicts, rational intervals, the complete chain and its exact transition/conductance expressions.
- discovery.json (`mathematics/computations/outputs/Yin_J_G0121/discovery.json`) retains the actual finite discovery outcome and candidate counts.
- independent_verification.json (`mathematics/computations/outputs/Yin_J_G0121/independent_verification.json`) records the distinct reviewer's completed finite checks and limits.
The exact original n=26 starting word is reused from [J118 inputs](../Yin_J_G0118/inputs.json).

## Reproduction

From the repository root run `python mathematics/computations/programs/Yin_J_G0121/main.py` with standard Python 3.
It needs only this group's inputs.json and the explicitly named J118 native inputs.json, not either group's generated output.
All arithmetic is integer or exact rational interval arithmetic; no numerical tolerance, random seed or external package is used.
Every pattern comparison must be strictly decided or execution stops without enlarging the root bracket precision or finite scope.
The certificate has exactly 81^2 pair records and one eight-word chain and must be smaller than 4 MiB before publication.
Output defaults resolve from the actual containing J directory into its standard ignored output home; reproduction may replace the same generated certificate.

Optional discovery uses `python mathematics/computations/programs/Yin_J_G0121/discover.py`.
It fixes one length-12 endpoint table and five declared length-24 targets; each intermediate table is bounded by 3^j for j<=12.
The discovered words are explicitly retained in inputs.json, so discovery is not required for certificate reproduction.

For the independent output comparison, run both preceding commands and then `python mathematics/computations/programs/Yin_J_G0121/verify_independent.py`.
This distinct verifier imports no contributor module and reconstructs its mathematical data from retained native inputs before comparing certificate.json and discovery.json.
It requires those two declared generated comparison inputs and writes independent_verification.json in this group's standard ignored output home.
All three commands were actually run during the [isolated whole review](../../../audits/reviews/Yin_R_G0811_v1.md#three-update-whole-independent-finding).

## Results and limits

The exact pair certificate completed all 6,561 ordered pairs for both update types.
Each type has exactly 183 rectangle-feasible pairs, of which 36 change the C627 integer coordinate.
The retained three-update excursion changes lambda from -1 to 0 at actual n=26.
Two further short bridges produce a complete seven-update route to the all-zero word; all eight full length-52 words and all seven positive original transitions were checked exactly.
The retained words have zero counts 15,13,15,16,14,16,32,52; target variable-block zero counts are 8,8,10,8,10,26,28.
The generated payload retains every complete endpoint-count denominator symbol and its exact actual endpoint, without substituting a uniform law or a selected-word normalizer.
The explicit following-route lower bound at n=26 is 2^-301.

The fixed discovery used 62,029 half endpoints and 165,528 exact candidate operations and found all five targets without a length scan.
The contributor's main.py and discover.py are by original_law and do not themselves supply independent review.
The distinct isolated reviewer authored verify_independent.py, reproduced all 6,561 pair decisions, the nine shorter-bridge patterns, all eight returned words and seven transitions, and independently rebuilt the fixed half-endpoint set and its candidate-operation count.
Its result was PASS at that exact scope, with formal mathematical findings and accepted-input boundaries in the linked R.
No complete numerical c_28 or c_52 denominator values, finite component census, uniform mass or path-load bound were computed.
The linked mathematical argument supplies the exhaustive update-order reduction, full-fiber extension, all-late symmetric padding, exact original probabilities and limits.
Passing a pair's rectangle screen alone does not establish actual order membership, current tail realization or a paid original-law flow.
No uniform mass, uniform congestion, complete connectivity or critical-mean result is supplied.

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
| `certificate.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0823_v1.md#whole-h-independent-finding) |
