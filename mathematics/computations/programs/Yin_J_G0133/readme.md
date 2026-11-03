---
author: Yin
---

# CFMZ26 complete original P1 lower supersolution verification

## Question and scope

Verify the exact fixed P1 certificate in [CFMZ26](../../../literature/pdf/CFMZ26/arxiv-v1.html) Appendix C under its complete-return criterion in Appendix B, at t=68883/40000, height 180 and 455137 sign representatives.
The source digit probabilities are 1/4,1/2,1/4, and no original trajectory is replaced by a normalized finite-box process.
Only this declared P1 lower certificate is selected; P2 and the upper-bound suite are outside this computation.
The source archive and its original programs remain in the ignored literature store.
The local runner executes the selected unchanged original verifier after source-code inspection and preserves a mathematical result without treating source fingerprints as mathematical evidence.

## Files

The authored [verify_p1.py](verify_p1.py) is the reproduction runner.
Its required original input is the [verification archive](../../../literature/pdf/CFMZ26/Quartic-Salem-Verification-v1.0.zip), with the exact source and edition described in the [CFMZ26 source notes](../../../audits/literature/CFMZ26/readme.md).
It selects only the two lower-verification Python modules and the P1 binary state and supersolution arrays.
Temporary extraction is disposable operational isolation within the J output home.
No original source program or witness is copied into tracked authored publication.

## Reproduction

Run from the repository root with Python 3.10 or later and the standard library:

    .venv/Scripts/python.exe -B -S mathematics/computations/programs/Yin_J_G0133/verify_p1.py

The source verifier uses integer and Fraction arithmetic, 200 exact root bisections and the 2^80 outward strip grid.
The runner permits no change of case, height, tilt or state count.
It writes complete output atomically only after the selected source checks and explicit scope checks succeed.
The selected source code was read completely before the successful native execution.
All mathematical checks remain active because the source uses explicit exceptions.
The source's optional metadata comparison is disabled; this does not disable any root, strip, state, successor, row, endpoint or logarithm inequality.

## Results and limits

The complete result (`mathematics/computations/outputs/Yin_J_G0133/cfmz26_p1_lower.json`) is PASS for all 455137 canonical rows and all 1365411 digit-labelled successors.
The successor counts are 791800 internal, 1 zero, 1104 paid cube exits and 572506 noncompletion exits.
Every state and successor strip comparison was decided by the certified rational intervals, with no constant fallback or unresolved case.
The minimum row residual is exactly 2791379258189148576 at row 329275, and the initial supersolution numerator is 181660711014187729550784 over 2^80.
The source comparison gives

    U(68883/40000) <= 302231454903657293676544000/2894667437079809876755951 < 105.

The full analytic source B.1--B.3 reduction is inspected in [CFMZ26-U001](../../../audits/literature/CFMZ26/Yin_U001.md#complete-return-supersolution).
The completed native/source result is retained separately in [CFMZ26-U003](../../../audits/literature/CFMZ26/Yin_U003.md#cfmz26-u003).
This replays the unchanged source algorithm after code inspection; it is not a second independent implementation or formal verification.
It does not classify the critical first-return mean or verify the source's independent quantitative upper-bound appendices.

## Independent complete P1 verification

The new [reviewer_p1_verify.py](reviewer_p1_verify.py) independently implements the finite certificate check and executes no source verifier or author runner.
It reads only the original archive members Quartic-Salem-Verification-v1.0/verification/lower_p1/states.bin and Quartic-Salem-Verification-v1.0/verification/lower_p1/W.bin.
It derives the coordinate identities modulo P, checks the integral coordinate determinant, uses direct power intervals for the strip coefficients and a centered absolute-error test for membership, and verifies every supplied state, internal successor, paid exit and cleared row inequality.
The witness and mathematical supersolution criterion are shared with the source; the implementation is separate and constructs no new witness.

Run from the repository root:

```powershell
.venv/Scripts/python.exe -B -S mathematics/computations/programs/Yin_J_G0133/reviewer_p1_verify.py
```

The original witness archive is required, and the default --replay-report input is the existing cfmz26_p1_lower.json in this J group's output home.
The source report is read only after independent mathematical verification.
The --output option also remains in the same J output home and defaults to reviewer_p1_result.json (`mathematics/computations/outputs/Yin_J_G0133/reviewer_p1_result.json`).
Complete publication is atomic; a failed check writes a distinct incomplete result.

The independent run checked all 455137 representative rows and all 1365411 digit-labelled edges, reproduced all four edge counts, found no unresolved strip comparison and matched the exact minimum residual, initial numerator and complete Green upper fraction.
Its scope remains height 180, t=68883/40000, state/weight lengths 3641096/7282192 bytes and source archive cap 25000000 bytes.
There is no graph search, larger cutoff, live memory monitor or claimed hard memory ceiling; the fixed input and iteration bounds are the actual resource scope.
The unused logarithmic dimension decimals, P2 and quantitative upper certificates are outside the independent native check.
The whole combined project finding, including the precise reuse of the qualitative source proof and C534 critical recurrence, is [R1017](../../../audits/reviews/Yin_R_G1017_v1.md#whole-source-radius-finding).

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
| `cfmz26_p1_lower.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1017_v1.md#whole-source-radius-finding); [Claim support and recorded result](../../../claims/Yin_C_G0796_v1.md) |
| `reviewer_p1_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1017_v1.md#whole-source-radius-finding) |
