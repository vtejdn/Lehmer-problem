---
author: Yin
---

# Unrestricted second-root congruence conditions

## Question and scope

Exact symbolic and modular certificates for the [complete C442 theorem](../../../claims/Yin_C_G0442_v1.md#second-root-congruence-theorem).
The [original L258](../../../ledger/Yin_L_G0258_v1.md) retains the declared experiments, preliminary failure, author freeze/contribution and fixed original review inputs.
The first root is c=(-1,0,1,1,0,1) in the retained path coordinates; all30 ordered positions are included, the other four columns and their order stay fixed, and the second root is any integer vector.
The theorem excludes Phi6 P4 and S6 over this entire unbounded domain.
Its written extension covers actual first roots congruent to +/-c modulo8, including an explicit unbounded family.
No general all-basis or arbitrary-reordering exclusion is claimed.

## Files

- [exact.py](exact.py) derives all120 integer polynomial models and enumerates every4096 residue vectors per position; mod4_result.json (`mathematics/computations/outputs/Yin_J_G0058/mod4_result.json`) retains all models, counts and full survivor lists.
- [lift8.py](lift8.py) performs every64 binary lifts of each retained target-labelled class; mod8_result.json (`mathematics/computations/outputs/Yin_J_G0058/mod8_result.json`) retains the complete empty outcome and each stage count.
- [congruence.py](congruence.py) extracts the stronger coefficient law on the same3584 retained classes; congruence_result.json (`mathematics/computations/outputs/Yin_J_G0058/congruence_result.json`) records every position's histogram.
- [eliminate.py](eliminate.py) solves the two linear equations exactly for position(0,2), with all eight target/sign cases and no parameter-size search; elimination.json (`mathematics/computations/outputs/Yin_J_G0058/elimination.json`) contains the resulting quadratics.
- [verify.py](verify.py) uses a different integer scalar-determinant/interpolation method and alternating-permutation Pfaffians; verification.json (`mathematics/computations/outputs/Yin_J_G0058/verification.json`) contains its checks and both actual complete polynomial/cover controls.

The programs above are author implementations; the [original full R119](../../../audits/reviews/Yin_R_G0119_v1.md#unrestricted-second-root-complete-independent-review) used a distinct implementation but is known SELF because its assignment disclosed target counts and the proposed extension.
The [current complete SELF finding](../../../audits/reviews/Yin_R_G0645_v1.md#second-root-whole-self-finding) covers the whole proof and every fixed native claim, with the old reviewer replayed stdout-only and all program/native bytes unchanged.

## Reproduction

From the repository root, using Python with SymPy:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0058/exact.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0058/lift8.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0058/congruence.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0058/eliminate.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0058/verify.py
```

The first command owns the polynomial/residue input consumed by the second, third and fifth.
All outputs resolve in this J output home.
There is no random seed, precision parameter or floating mathematical decision.
SymPy derives integer symbolic identities; verify.py uses only standard-library integers.
The draft's prose or continued existence is not a mathematical input.

## Results and limits

Before execution D125 declared30*4096=122880 modulus4 vectors and a120-second cap.
That completed with1664 F and1920 S6 classes, so modulus4 alone did not exclude the targets.
Before the next run it declared the reason for modulus8: +/-3 and +/-1 coincide as sets modulo4, whereas modulus8 distinguishes them and exact unit minors from other odd minors.
The complete229376 target-labelled lifts then gave zero survivors.

The compressed identity is A+2D=2 modulo4, D=(Pf^2-ell^2)/8, whenever ell is odd, N=1 modulo4 and A even.
D parity is proved to depend only on the residue modulo4.
For an actual basis this gives a+b=1 modulo4 if a is even, contradicting both targets' a+b=3 modulo4.
The finite certificate is therefore an all-integer obstruction only through that written reduction.
Positions(1,4),(4,1) have identically zero determinant minor and rank-one linear systems; all other28 have rank two.
No dependent case or integrality condition is dropped.

The two complete actual controls are reused L246/J55 matrices, not new realizations.
Their original/absolute polynomials and full rank12 products are retained, with energies24/48 and34/68 and height2.
D125 gives parameter-dependent full cost bounds for the unbounded family and retains the cheaper achieved Phi2^2 P4 control.
No unknown target companion, optimized Mahler value, neutral-factor deletion or gap is inferred.

## Inspection summary

All five author programs completed.
The first exact.py attempt failed a structural SymPy matrix-equality assertion because its product was not expanded.
Replacing that check by expansion of every entry of V V^-1-I corrected the check without changing a formula or scope; it had failed before writing canonical output.
The complete rerun and all subsequent programs passed.
No abandoned output is represented as a complete certificate.

The different author verifier recovered all120 polynomial models from840 interpolation nodes and5040 scalar determinant checks.
It generated signed Pfaffians by the full720 alternating-permutation definition reduced to15 terms, and checked each entire degree12 control cover at13 distinct integers,26 values total.
This is another exact implementation by the same author; it is not an independent noncontributor review.
The initial symbolic and modular outputs remain available along with this checking evidence.
The [full original R119 finding](../../../audits/reviews/Yin_R_G0119_v1.md#unrestricted-second-root-complete-independent-review) retains its actual execution, whole scope and no-author-repair verdict at the explicit known SELF relationship.

The independent checker remains runnable after retirement of D125; draft presence supplies no mathematical input.

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
| `congruence_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0119_v1.md#unrestricted-second-root-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0645_v1.md#second-root-whole-self-finding) |
| `elimination.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0119_v1.md#unrestricted-second-root-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0645_v1.md#second-root-whole-self-finding) |
| `mod4_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0119_v1.md#unrestricted-second-root-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0645_v1.md#second-root-whole-self-finding); [Claim support and recorded result](../../../claims/Yin_C_G0442_v1.md) |
| `mod8_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0119_v1.md#unrestricted-second-root-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0645_v1.md#second-root-whole-self-finding) |
| `review_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0119_v1.md#unrestricted-second-root-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0645_v1.md#second-root-whole-self-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0119_v1.md#unrestricted-second-root-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0645_v1.md#second-root-whole-self-finding) |
