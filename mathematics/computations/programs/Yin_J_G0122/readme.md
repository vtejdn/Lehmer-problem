---
author: Yin
---

# Exact translation margins and a zero-middle greedy-coordinate countercontrol

## Question and scope

Certify the finite real-place margin inequalities that extend the complete C631 seven-edge chain to EVERY actual w with |w_+|<1/100, |w_-|<1/5.
Separately extract all positive coordinate-increment translations from the already complete J121 pair certificate and test their endpoints at c_block=(-3,9,1,-3).
The complete analytic coverage and limits are fixed in [C612v1](../../../claims/Yin_C_G0612_v1.md#argument), whose selected decision owns its current assessment.
This is a finite local identity/margin test, not a coordinate-box or graph-length scan.

## Files

- [inputs.json](inputs.json) fixes the two rational margins, nine base labels, the exact blocked label and both explicit cross-J paths.
- [main.py](main.py) certifies 18 uniform margin inequalities, extracts all positive-increment translations from the retained complete pair table, and checks the six endpoint failures at the actual blocked label.
- certificate.json (`mathematics/computations/outputs/Yin_J_G0122/certificate.json`) retains every exact rational margin, source pair occurrence and blocked-endpoint certificate.
- [verify_independent.py](verify_independent.py) independently rechecks the fixed labels, all chain and coordinate identities, all 18 real margins, every retained pair verdict, and all six blocked-endpoint failures without importing an author program.
- independent_verification.json (`mathematics/computations/outputs/Yin_J_G0122/independent_verification.json`) retains the independent exact lower margins, strict violation bounds and finite checked scope.

The exact named cross-J inputs are [J118 inputs.json](../Yin_J_G0118/inputs.json) and J121 certificate.json (`mathematics/computations/outputs/Yin_J_G0121/certificate.json`).
Missing generated input will be reported rather than silently rebuilt or replaced.

## Reproduction

From the repository root run `python mathematics/computations/programs/Yin_J_G0122/main.py` with standard Python 3 and the two stated cross-J inputs locally present.
All arithmetic is integer or exact rational interval arithmetic, with the existing accepted algebraic-root bracket.
The finite input has five right and four left base labels, exactly six extracted positive translations and one blocked actual label; no coordinate range or word-length search is made.
The previously independently checked J121 classification is a reused input, not a newly executed pair classification or discovery run.
The program checks complete coverage of its 81-by-81 index pairs, exact increment formulas and the retained classification counts before extraction.
Output is limited to 256 KiB and resolves from the actual containing J directory into its standard ignored output home.
Reproduction may replace this generated certificate at the same path.

After that command, run `python mathematics/computations/programs/Yin_J_G0122/verify_independent.py` from the repository root for the independent verification.
It requires both stated cross-J inputs and the generated J122 certificate, and writes only its distinct generated verification output.
It independently recomputes all 13,122 order verdicts for the retained 6,561 pair rows using signed monomial rational enclosures, and rechecks the 81-pattern shorter-bridge screen.
It does not run a new coordinate-box, original-word length or graph discovery search and does not silently rebuild missing J121 output.

## Results and limits

All 18 strict margin inequalities passed, certifying the entire real box |w_+|<1/100, |w_-|<1/5 through the stated triangle-inequality argument.
All positive increments in the retained accepted pair table are +1, with 36 positive occurrences across the two orders and exactly six distinct translations.
The exact actual label c_block=(-3,9,1,-3) is strictly inside Z0 and has lambda=-1; all six possible positive-increment endpoints strictly fail at least one Z0 bound.
The full actual-state, finite-onset, original-word probability and unbounded-family arguments are in the linked mathematical material, not supplied by these finite inequalities alone.
The original `main.py` program and author checks are by contributor original_law.
The separately authored verifier passed all 18 strict margins, all 6,561 pair rows in both orders, all 81 shorter patterns, the 36 positive occurrences and six distinct translations, and every blocked-endpoint failure.
In C612's displayed order, the first translation violates only the expanding bound, the fifth only the stable bound, and the other four both bounds.
The [whole isolated independent finding](../../../audits/reviews/Yin_R_G0815_v1.md#translated-family-whole-independent-finding) records the analytical review, finite verification, actual independence and accepted-input/source limits.
The result does not infer whole-Z0 connectivity, terminal-fiber connection to zero, a uniform onset, uniform positive mass, bounded congestion or a critical-mean conclusion.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
