---
author: Yin
---
# Exact inverse-target checks for adjustable two-chain realizations

## Question and scope

This group supports the [complete C497 proof](../../../claims/Yin_C_G0497_v1.md#adjustable-core-forest-fixed-scope).
The [original L207 fixed input](../../../ledger/Yin_L_G0207_v1.md#retained-adjustable-core-forest-proof) retains the actual earlier proof and review-input history.
The independently prescribed target is F=(t+1)(t^6-t^5-t^3-t+1), with exactly the displayed degree-one cyclotomic padding.
It tests adjustable integral cores with several pendant paths, and retains the complete original determinant and absolute presentation.
The degree-six Salem input is reused from [complete C476](../../../claims/Yin_C_G0476_v1.md#degree-six-return-core-fixed-scope), not reproved by these programs.

The useful general result is D73's all-integer obstruction for every way of adding a three-vertex unit pendant forest to an arbitrary integral rank-four core, together with its general independently variable multichain determinant and degree-independent full-measure bound at a fixed core.
The finite failures below do not by themselves prove that obstruction or universal nonrealizability.

## Files

- [probe.py](probe.py) derives symbolic complete rank-four determinant coefficients and checks all15625 six-entry core tuples in[-2,2] and all12 ordered distinct attachment pairs for paths of lengths1 and2.
  Its probe.json (`mathematics/computations/outputs/Yin_J_G0043/probe.json`) retains187500 exact cases and zero successful target realizations.
  There is no sample, random choice, timeout or floating-point filter.
  The later all-integer parity proof in D73 supersedes the entry-box limitation for this architecture.
- [probe5.py](probe5.py) tests signed-unit rank-five cores with one two-vertex unit tail, a changed architecture not excluded by D73's rank-four theorem.
  It covers the3^10 entry box modulo diagonal vertex signs only, using lexicographically selected negative spanning-forest edges.
  This leaves3969 representatives.
  The necessary coefficient A=0 leaves702 cores and3510 attachment tests; none succeeds.
  probe5.json (`mathematics/computations/outputs/Yin_J_G0043/probe5.json`) keeps these actual counts.
  There is no order quotient and no exclusion claim for larger entries or arbitrary rank-seven matrices.
- [verify.py](verify.py) is the author's separate exact algebra and actual-matrix verification.
  It checks all six symbolic core coefficient patterns used in the forest proof, the changed rank-five filter, the complete cubic modulo4 residue table and the forced middle-coefficient parity.
  It also constructs42 actual rank-seven matrices (seven forest forms, three integer cores, original and absolute) and checks every complete characteristic polynomial against the derived formula.
  Six additional actual rank-nine matrices check the general three-chain identity and sparse numerator with independent lengths(0,2,3), including an empty chain, complete coefficient-norm constants and energy.
  verification.json (`mathematics/computations/outputs/Yin_J_G0043/verification.json`) retains all successful finite results and those six complete polynomials and measure-bound constants.

The checks use Python with SymPy and passed, including the single-chain and rank-five coefficient interfaces.
The programs use integer symbolic arithmetic and no approximate roots or Mahler integration.
A second author implementation is not a separately organized independent review.

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0043/probe.py
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0043/probe5.py
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0043/verify.py
```

Each command writes only its corresponding saved JSON after the implemented checks.
Reviewers should intercept writes or use reviewer-only destinations when preserving native author evidence.
No additional broad scan is needed for the current proof.

## Meaning and limits

The rank-four finite experiment motivated a complete all-integer proof which covers arbitrary core entries, all rooted forest shapes on the three added vertices, repeated attachment sites and all signed unit tree edges.
That theorem is a written coefficient/parity argument in D73, not an extrapolation from either entry box.
The rank-five finite failure keeps its explicit signed-unit scope.
Neither result says every cyclotomic stabilization or every general rank-seven presentation is impossible.

D73's independently variable multichain identity keeps every actual determinant factor and the full absolute-cover polynomial.
Its measure bounds depend on the complete fixed core and number of attachments; they supply no uniform small-target ratio or unrestricted coefficient-prescription theorem.
General choices need not have a positive-measure factor at all.
The orbit_research agent supplied all new proofs and programs; the coordinator assigned only the broad question and allocation.


## Complete separate review and read-only replay

The coordinating AI for Yin completed the original 2026-10-09T20:04 whole-proof and program review `Yin_R_G0106_v1#adjustable-core-complete-independent-review`; its actual input/scope/UNKNOWN relationship remain in [the later complete comparison](../../../audits/reviews/Yin_R_G0721_v1.md#natural-comparison-with-the-original-whole-review).
The original reviewer supplied only the broad assignment, not the new proof or programs; its shared context and earlier dependency work remain disclosed in that comparison.
All three author programs were actually rerun with Path.write_text intercepted in memory, and all three proposed parsed JSON outputs exactly equalled the existing native author outputs.
This is a complete proof review and exact replay of the authored programs, not an independently implemented search.
The written all-integer exclusion and its limits remain in the responsible proof.

The complete D73 proof is currently retained in [C497](../../../claims/Yin_C_G0497_v1.md#adjustable-core-forest-fixed-scope), whose 2026-10-22T04:03 decision selects [the new whole independent finding](../../../audits/reviews/Yin_R_G0721_v1.md#entire-forest-multichain-independent-finding).
The earlier [R708 whole SELF](../../../audits/reviews/Yin_R_G0708_v1.md#current-adjustable-forest-multichain-whole-finding) and C497's 09:23 adoption retain their own actual history.
The [complete original R721 comparison](../../../audits/reviews/Yin_R_G0721_v1.md#natural-comparison-with-the-original-whole-review) preserves its whole UNKNOWN relationship because the actual additional initial mathematical context and order are unestablished; its original independent declaration and same-program replay remain history.
The [complete original Section 6 author checks](../../../audits/reviews/Yin_R_G0721_v1.md#original-adjustable-forest-author-checks) remain SELF at 2026-10-10 day precision, and the original L207 input is unchanged.
Current maintenance read all original code and native data without running a producer, checker or search.
D73 textual labels refer to the retained proof.

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
| `probe.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0721_v1.md#entire-forest-multichain-independent-finding) |
| `probe5.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0721_v1.md#entire-forest-multichain-independent-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0721_v1.md#entire-forest-multichain-independent-finding) |
