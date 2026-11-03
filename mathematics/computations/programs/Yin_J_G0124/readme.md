---
author: Yin
---

# Exact three-update column domains in the actual zero-coordinate fiber

## Question and scope

Extract the complete lambda-zero actual column domains from the existing fixed C631/J121 middle-pair certificate and C636's three-column H geometry.
The analytical domain, exact current-tail sufficiency and complete H-connectivity construction are fixed in [C620v1](../../../claims/Yin_C_G0620_v1.md#argument), whose selected decision owns their assessment.
Each accepted lambda-zero pair is intersected with precisely the three source columns m=-1,0,1 and its explicit intermediate-core interval.
This finite local symbolic extraction is not a coordinate-box, original-word, graph-path or word-length scan.

## Files

- [inputs.json](inputs.json) fixes the original quartic, the existing root input, the required generated pair table, the three source columns and the output limit.
- [main.py](main.py) retains all attempted column domains, exact nonempty intervals, original middle-pair witnesses and merged transition domains, then checks full endpoint-overlap equality and the two selected whole-column bridges.
- domains.json (`mathematics/computations/outputs/Yin_J_G0124/domains.json`) is the complete exact generated result.
- [verify_whole_independent.py](verify_whole_independent.py) independently reconstructs every original pair decision and exact domain, without importing contributor modules.
- whole_independent_verification.json (`mathematics/computations/outputs/Yin_J_G0124/whole_independent_verification.json`) retains the complete independent finite result.

The explicitly required cross-J inputs are [J118 inputs.json](../Yin_J_G0118/inputs.json) and J121 certificate.json (`mathematics/computations/outputs/Yin_J_G0121/certificate.json`).
The existing generated J121 input is required and is never silently rebuilt or replaced.

## Reproduction

From the repository root run `python mathematics/computations/programs/Yin_J_G0124/main.py` with standard Python 3 after the explicitly named J118 and J121 inputs are present.
All field arithmetic uses exact rational coefficients modulo the ORIGINAL quartic; endpoint ordering uses the existing rational beta bracket and rejects unresolved signs.
The fixed scope is the 147 accepted lambda-zero pairs per order, each in three source columns; no automatic enlargement is permitted.
The complete output is limited to 2 MiB and is published only on success.
Reproduction may overwrite the same generated output.

## Results and limits

The extraction completed at its fixed scope: each order has 147 lambda-zero pairs, 441 column cases and 259 nonempty cases.
There are exactly 33 directed transition types after combining the orders, with one open interval per type, each exactly equal to its entire source/target endpoint overlap.
Both selected CYC pairs independently cover the complete outer column I_(-1); their source indices and exact intervals are retained in the output.
Displayed decimal endpoints in standard output are explanatory only; no floating-point value controls a decision or appears in the exact certificate.
The complete actual connectivity, terminating coefficient reduction, finite shared-tail onsets and original probabilities require the linked mathematical argument.
Native author work is by contributor original_law and supplies no independent-review claim.
A nonempty interval retains x in Z[t], the actual intermediate order point and its individual shared-tail onset; it supplies neither uniform current support nor connectivity, mass or conductance by itself.

The isolated [R823 whole finding](../../../audits/reviews/Yin_R_G0823_v1.md#whole-h-independent-finding) independently reconstructed all6561 pair decisions,882 column cases,518 nonempty cases,33 full open unions and both whole-column bridges.
Run `python mathematics/computations/programs/Yin_J_G0124/verify_whole_independent.py` after the declared native inputs and domains output are present.
Its scope remains the fixed finite domain extraction; the separate C620 decision owns adoption of the complete analytic result.

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
| `domains.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0823_v1.md#whole-h-independent-finding) |
