---
author: Yin
---
# Cubic trace units and primitive auxiliary costs

## Question and scope

Exact certificate supporting the complete [C480 theorem](../../../claims/Yin_C_G0480_v1.md#statement), with the original [L269 exploration](../../../ledger/Yin_L_G0269_v1.md) retained: the simplest-cubic trace order, rank-two unit identities and primitive content collapse.
The mathematical domain consists of all-parameter symbolic identities, the complete primitive coefficient-energy domain at most12 and actual parameters1,2,3,6.
No near-one or whole-unit-group assertion follows.

## Files

- `verify.py`: exact SymPy author certificate, all-parameter quotient identities, the complete energy<=12 domain and four declared actual inputs.
- `verification.json`: native final output, exact polynomial data, signed norms/resultants, contents, energies and rational trace-root isolating intervals.

## Reproduction

From the repository root, run:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0062/verify.py
```

Python3 with the repository's SymPy environment is used; no input files, random seeds or external network calls.
The program writes `verification.json` in `mathematics/computations/outputs/Yin_J_G0062/`.
The declared total author execution cap is120 seconds.
The finite domain is the37 primitive sign-representatives y=(u,v,u+w) in{-2,-1,0,1,2}^3 with0<sum y_i^2<=6; all positive integer a in norm equalities are solved symbolically, not scanned.
The separate actual parameters are exactly1,2,3,6.

## Results and limits

The completed output includes exact trace-root isolation, nine norm-H rows with their exceptional positive integer parameters, and the exclusion of every remaining short vector by polynomial arithmetic.
The four actual inputs check all primitive classes, the derivative representative and full signed original resultant.
The complete all-exponent argument belongs to [C480](../../../claims/Yin_C_G0480_v1.md#rank-two-full-orbit-cost).

The global unit-orbit lower bound is proved analytically in C480, not inferred from these37 vectors.
The finite certificate supplies the entire energy<=12 classification and exact four-input controls only.
Neither a whole-unit-group result, a centered-column origin, near-one coverage nor Task completion follows.

## Inspection summary

The author self-check is separate from the noncontributor review below.

## Original inspection and current relationships

The [entire original R697 finding](../../../audits/reviews/Yin_R_G0697_v1.md#l269-and-r168), now explicitly UNKNOWN, discloses the reviewer's scope/source coordination and pre-review norm-sign wording check; it supplied no current derivation.
The [checker](review_independent.py) uses multiplication-matrix determinants and exact quadratic-discriminant parameter solutions without author imports.
All37 sign classes,9 norm rows and4 actual inputs passed, including16 full original resultant/energy controls and exact interval-sign checks.
The result (`mathematics/computations/outputs/Yin_J_G0062/review_result.json`) supplies finite verification, separate from the written all-exponent bound.

The [earlier R691 whole SELF](../../../audits/reviews/Yin_R_G0691_v1.md#rank-two-sextic-whole-self-finding) covers the entire written theorem and every original source/native field.
Its original-domain reviewer-only replay completed in0.7522517000033986seconds within the original120-second cap: all37 representatives/nine rows/four inputs and every report field agreed, with all five original program/readme/native files byte-identical across that replay.
Only the expected report write was intercepted for stdout comparison; no producer, new domain, output file, source reading or Task/E execution occurred.
This replay and whole SELF provide no fresh isolated review and do not retrospectively reclassify the old whole finding; this later documentation maintenance changes no program/native bytes.

C480 is adopted at2026-10-22T00:06 with the [new R697 whole independent finding](../../../audits/reviews/Yin_R_G0697_v1.md#c484-whole-independent-finding), including the entire written proof and complete finite/native/source/negative scope.
Its own original-domain reviewer-only replay completed2026-10-21T23:53 in0.7977412999898661seconds; every report field equaled the retained report and all five actual inputs were byte-identical across that run.
This new isolated checking is distinct from the original10/10 executions and the earlier current SELF replay above; original R168 historical UNKNOWN, author10:30 SELF, R691 SELF and unknown source-reading minutes retain their actual meanings.

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
| `review_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0691_v1.md#rank-two-sextic-whole-self-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0691_v1.md#rank-two-sextic-whole-self-finding) |
