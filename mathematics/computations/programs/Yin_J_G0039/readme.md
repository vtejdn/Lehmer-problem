---
author: Yin
---
# Exact four-state real-overlap entry certificate

## Question and scope

Certify the finite residue/real-overlap lemma in [complete C467v2](../../../claims/Yin_C_G0467_v2.md#residue-overlap-control-fixed-scope): for every real beta in[3/2,151/100], x in[-1,1] and initial state in F4=F2[b]/(b^2+b+1), an original digit word of length at most4 sends the residue to0 and the real coordinate strictly inside(-1,1).
This is a finite real-entry certificate, not exact return or a normalized neutral-margin certificate.

## Files

- [main.py](main.py) performs the bounded word enumeration, constructs exact inward inverse-word intervals, and saves the selected17-word certificate.json (`mathematics/computations/outputs/Yin_J_G0039/certificate.json`).
- [verify.py](verify.py) imports no search code.
  It uses forward rational interval bounds on17 closed cells and a separate polynomial-basis residue recurrence, saving verification.json (`mathematics/computations/outputs/Yin_J_G0039/verification.json`).
- [C467v2](../../../claims/Yin_C_G0467_v2.md#residue-overlap-control-fixed-scope) owns the complete finite-entry argument, bounded-correction transfer to ideal-preserving control, and exact limitation of that transferred margin expression.

Both programs are author implementations, not independent review.
No external source, floating-point result, or machine-specific library is a premise; they use only the Python standard library.

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0039/main.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0039/verify.py
```

The author checks use Python and passed.
The first considers exactly121 original words of lengths0--4 and four initial residue states.
Inverse endpoint bounds use rational interval arithmetic for the entire closed beta range[3/2,151/100]; the saved simple bounds are rounded inward by exact comparisons.
The second computes a complete closed-cell cover and checks forward images and quotient transitions directly.
Each output is written only after its script's assertions pass.

## Results and limits

The residue-admissible candidate counts are33,28,26,34 for states0,1,b,b+1.
The retained covers use3,6,5,3 words respectively, each of length at most4.
The separate forward implementation checked all17 closed cells, including their endpoints; its minimum exact margin from either final real boundary is27/320.
Thus the selected endpoints satisfy |T_w(x)|<=293/320 throughout the proved cells and beta range.
The theorem is a sufficient witness assertion: no claim about longer words or optimal length follows from the bounded enumeration.

Exact polynomial values P_6(3/2)=-5/64 and P_6(151/100)=50688013301/10^12 locate the already known unique Salem root above1 in the certified beta interval.
The quotient identity P_6 mod2=(t^2+t+1)^3 is displayed and justified in D59; a real beta interval alone does not define an order quotient.

The preliminary approximate interval exploration was used only for discovery.
The retained certificate is entirely rational and does not use SymPy.
Successful construction gives legal entry into an ideal and bounded-cost correction of strong directional control.
It does not establish a normalized radius above the L187 threshold, exact compact termination, an original-law tail estimate or the unrestricted gap.
The original `Yin_R_G0094_v1#residue-overlap-control-independent-review` proof/certificate scope, day-precision occurrence and UNKNOWN initial arrangement are preserved in [R682's complete mathematical comparison](../../../audits/reviews/Yin_R_G0682_v1.md#l195-and-r94).


## Independent certificate and fixed retention

The separately assigned noncontributor reviewer wrote and executed [review_exact.py](review_exact.py), retaining review_verification.json (`mathematics/computations/outputs/Yin_J_G0039/review_verification.json`).
Run `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0039/review_exact.py` from the repository root after the author certificate is available.
It imports neither author program and uses a different17-cell rational partition, polynomial-bit quotient arithmetic and exact Bernstein bounds over the entire beta interval.
It certifies a uniform margin3/40 for that second cover, and separately validates all author open intervals, closed enclosures and their recorded minimum27/320.
It also independently checks all121 candidate words and residue counts, the two root-enclosure endpoints and the full mod2 identity.
This was a separate implementation using the supplied witness words, not independent discovery of them or a rerun of either author program.


## Current retention scope

The complete current C467v2 decision adopts the [new independent whole finding in R682](../../../audits/reviews/Yin_R_G0682_v1.md#residue-entry-isolated-whole).
The [earlier actual whole SELF](../../../audits/reviews/Yin_R_G0675_v1.md#current-residue-entry-whole-finding) and original R94 entire whole UNKNOWN retain their actual scopes; the new independent finding does not establish the original reviewer's isolation.
The retained reviewer code computes and compares hashes of the five named author files in memory before and after checking.
Its output lists author_files and mathematical validations without serializing digest fields; the original R94 assertion of recorded output fingerprints exceeds those available fields.
That historical recorded-output assertion and original execution account remain preserved in R682's comparison, without generating or backfilling hashes or inferring that the original comparison failed or did not happen.
This maintenance reads existing code/reports and maintains proof navigation and retention precision; it reruns neither author program nor checker and changes no native output.

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
| `certificate.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0682_v1.md#residue-entry-isolated-whole) |
| `review_verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0682_v1.md#residue-entry-isolated-whole) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0682_v1.md#residue-entry-isolated-whole) |
