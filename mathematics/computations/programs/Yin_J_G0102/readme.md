---
author: Yin
---
# Three-rotation determinant screen for the rational two-shear family

## Question and scope

Under the [continuing G0001 instruction](../../../tasks/Yin_T_G0001_v1.md#decision-continue-until-stop-2026-10-18), test the changed circle family

    B=q(E+sG)^2+q^(-1)(F_0+tG)^2+bG^2.

Its complete rational arithmetic gate was adopted in [C157v3](../../../claims/Yin_C_G0157_v3.md#decision-whole-reviewed-2026-10-18), through [R396](../../../audits/reviews/Yin_R_G0396_v1.md#rational-two-shear-whole-independent-finding), before this computation ran.
The circle screen itself covers ALL real s,t, all real q>0 and b>=2; that larger analytic domain is not an arithmetic extension.
Use exactly the original quartic_Salem_seed and Lehmer_degree10 entries of [J97 input](../Yin_J_G0097/input.json).
The other two J97 inputs are not part of this test.
The old J100/J101 one-shear exclusions are not reused as certificates for the changed family.

The complete [three-rotation Hadamard argument](record.md#three-rotation-screen) was developed and separately reconstructed before calculation.
It reduces a parameter-uniform lower bound to the complete Mahler measure of one exact integer residue-determinant polynomial K per input, with the whole factor L^3, L=972000, retained.
A lower bound at least log2 excludes every positive Haar saving.
A lower bound strictly above log2-1/16 excludes only the predeclared operational target.
Either certificate skips that input's parameter grid.

## Files

[record.md](record.md) owns the complete analytic proof, exact normalization and predeclared stop/fallback rules.
[screen.py](screen.py) constructs the integer residue determinant and certifies its Mahler measure.
[verify_screen.py](verify_screen.py) independently reconstructs the coefficients and the full rotation identity, then computes its own root enclosure and checks the retained author evidence.
[main.py](main.py) owns the bounded fallback and records why no grid was run when the screen succeeds.

Actual author outputs are screen.json (`mathematics/computations/outputs/Yin_J_G0102/screen.json`), quartic certificate (`mathematics/computations/outputs/Yin_J_G0102/quartic_Salem_seed_screen.json`), Lehmer certificate (`mathematics/computations/outputs/Yin_J_G0102/Lehmer_degree10_screen.json`) and fallback disposition (`mathematics/computations/outputs/Yin_J_G0102/results.json`).
Actual independent evidence is screen-verification.json (`mathematics/computations/outputs/Yin_J_G0102/screen-verification.json`), with its two per-input verification files in the same output directory.
Generated outputs are ignored by Git and may be absent from a clone; the native commands regenerate them.
The original J97 JSON is the only cross-J input and is not replaced by a same-name fallback.

## Reproduction

From the repository root with python-flint0.9.0:

    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0102/screen.py
    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0102/main.py
    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0102/verify_screen.py

The screen needs no prior generated numerical output.
The fallback reads its actual same-J screen.json, and the verification-only command requires the actual author screen certificates for its final comparison.
Both author and checker use256-bit working precision, at most one512-bit escalation, a1e-30 root-radius target and a300-second subprocess bound per input.
Every squarefree factor, exact content, leading coefficient and original root multiplicity is retained.
Circle roots are handled by outward log(max(1,abs(root))) balls, not discarded or classified from a rounded center.

The checker uses Python integer Laurent dictionaries and a cofactor determinant rather than the author's FLINT polynomial construction and permutation sum.
It additionally expands the complete three-rotation determinant directly in Z[omega]/(omega^2+omega+1), checking the factor3(omega^2-omega), all exponents and the exact scalar L^3.
No author helper is imported.
The arrangement is non-blind: the checker read the author program and was told its reported values before its own execution.
Both programs share python-flint and FLINT's certified root/ball primitives; they are not independent numerical libraries.

The fallback, declared before execution, remains exactly s,t in{-2,-1,0,1,2}, q in{1/4,1/2,1,2,4}, b=2 on any surviving input.
Its125 candidates use8192 and16384 midpoint nodes on theta in[0,pi] for exploratory ranking only.
It selects the smallest16384-node average with lexicographic(s,t,q) tie breaking, then attempts one192-bit analytic quadrature certificate per surviving input, tolerance goals1e-18 and300 seconds per input.
No continuous optimizer, enlarged grid or third sample pass is authorized by this record.
Those midpoint arrays and quadratures were NOT evaluated in the completed round, because both inputs failed the preceding uniform screen at the operational target.
NumPy2.3.5 and SymPy1.14.0 were available for that unrun fallback; their presence is not evidence of an executed parameter calculation.

<a id="certified-results"></a>
## Results and limits

Both exact determinant screens and both independent reconstructions completed at256 bits, with no escalation or timeout.
The determinant degrees and full root counts with multiplicity are40 and102.
All exact coefficient, rotation-identity, leading/content, scalar and root-count checks passed.
The independently propagated balls overlap the author's reported enclosures.

| Original input | Uniform Haar lower bound | Lower bound minus log2 | Lower bound minus(log2-1/16) | Certified consequence |
| --- | --- | --- | --- | --- |
| Quartic Salem | 0.634297835607472 | -0.058849344952474 | 0.003650655047526 | Every real two-shear/weight/buffer choice misses the1/16 target; a smaller positive saving is not excluded. |
| Lehmer degree10 | 2.390676477033497 | 1.697529296473551 | 1.760029296473551 | Every real two-shear/weight/buffer choice has Haar logarithm above log2. |

These numbers are LOWER BOUNDS, not evaluated Haar averages at selected parameters and not attained minima.
The decimals summarize the retained outward balls with absolute error below1e-10; every strict comparison uses those balls rather than decimal agreement.
In particular the certified safe statements are I>0.6342978356 for the quartic and I>2.3906764770 for Lehmer throughout the whole stated real parameter domain.

The exact author determinant offsets are-21 and-52, with leading coefficients+1091225520000 and-1091225520000 respectively.
The squarefree factorization retains contents+14171760000 and-14171760000, rather than treating K as monic or primitive without its scalar.
No original field norm at a selected parameter, midpoint parameter grid or direct quadrature was evaluated.
The fallback disposition records zero grid runs on both inputs.

The two distinct exclusions are finite-input results for this entire stated quadratic family.
They neither exclude all quadratic forms nor establish an all-input obstruction, uniform original-root/Haar transfer or an unrestricted Mahler gap.
The complete independent [R397 finding](../../../audits/reviews/Yin_R_G0397_v1.md#three-rotation-j102-whole-independent-finding) checks this entire analytic reduction, actual finite evidence and scope; its separate reconstruction shares the FLINT numerical engine.

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
| `results.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0397_v1.md#three-rotation-j102-whole-independent-finding) |
| `screen-verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0397_v1.md#three-rotation-j102-whole-independent-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0398_v1.md#constant-spd-whole-independent-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0698_v1.md#complete-constant-spd-whole-self-finding) |
| `screen.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0397_v1.md#three-rotation-j102-whole-independent-finding) |
