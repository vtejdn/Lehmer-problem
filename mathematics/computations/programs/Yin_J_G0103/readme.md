---
author: Yin
---
# Bounded signed quadratic-norm diagnostic on the original two controls

## Question and scope

Prepare a first finite test of the signed form N=(X+sG)^2-pG^2, with X equal to E or F_0, on exactly the original quartic_Salem_seed and Lehmer_degree10 entries of [J97 input](../Yin_J_G0097/input.json).
Its complete [C167 gate](../../../claims/Yin_C_G0167_v1.md#decision-whole-reviewed-2026-10-18) is adopted after the separate [R400 whole finding](../../../audits/reviews/Yin_R_G0400_v1.md#signed-defect-whole-independent-finding).
That finding covers the complete mathematical gate and planned interface, not either native implementation or a numerical result.
For the selected primes the actual trace fields exclude sqrt(p), so the proposed integral value is nonzero and its complete original norm floor is1, with logarithmic threshold0.
The positive-form threshold log2 is not used for this changed object.
The Haar integrand is log ABS N and may have circle singularities; no positivity of N is asserted.
The operational useful margin is I<=-1/16.

The bounded grid is exactly X in{E,F_0}, s in{-2,-1,0,1,2}, p in{2,3,5,7}:40 candidates per input.
Use8192 and16384 midpoints on theta in[0,pi] for exploratory ranking only.
If a candidate has any zero or nonfinite floating sample, mark its ranking unresolved rather than replacing its logarithm by an invented finite value.
Select at most one candidate per input by the smallest finite16384-node average, with exact-floating ties broken lexicographically by(X,s,p), using E before F_0.
No continuous optimizer, enlarged parameter range or third resolution is included.
This sample selection does not certify a grid minimum or any parameter-family exclusion.

For each selected candidate, construct the complete ordinary INTEGER numerator

    A=(X_aligned+sZ)^2-pZ^2,
    X_aligned=13500 z^(9d/2)H23 or1215 z^(5d/2)H25,
    Z=32H35, L=972000,
    N=z^(-15d)A/L^2.

Its exact degree30d and signed leading coefficient50176(s^2-p) are retained.
Certify I=m(A)-2log L by complete-root Jensen with squarefree multiplicities, signed content and absolute leading coefficient included.
Use256 bits with at most one512-bit escalation, a1e-30 root-radius goal and300 seconds per selected input.
Compute the selected exact original trace-field norm and its full original-field square, and compare the resulting nonnegative original-conjugate logarithm with the certified Haar value.
A failure of those fixed certification limits is recorded as incomplete without silently changing parameters.
A separate checker must reconstruct the exact numerator and field value independently and verify the same fixed witnesses.

## Files

The native author [main.py](main.py) has completed the declared two-input computation.
The independently authored [verify.py](verify.py) has a separate reconstruction and run; its actual status is stated below.
Generated evidence is retained locally in the matching ignored output directory.
The author aggregate (`mathematics/computations/outputs/Yin_J_G0103/results.json`), quartic certificate (`mathematics/computations/outputs/Yin_J_G0103/quartic_Salem_seed.json`) and Lehmer certificate (`mathematics/computations/outputs/Yin_J_G0103/Lehmer_degree10.json`) retain all original coefficients, sample rankings, exact field norms, factors, roots, scalar balls and actual escalation.
The independent aggregate (`mathematics/computations/outputs/Yin_J_G0103/verification.json`), quartic reconstruction (`mathematics/computations/outputs/Yin_J_G0103/quartic_Salem_seed-verification.json`) and Lehmer reconstruction (`mathematics/computations/outputs/Yin_J_G0103/Lehmer_degree10-verification.json`) retain the separate exact candidates, sample comparisons, multiplication matrices, factors, roots and scalar balls.
A clone need not contain these ignored outputs; reproduce them with the declared commands rather than substituting another input.
The original J97 input JSON is the only cross-J input; no earlier numerical result is required.

## Reproduction

From the repository root, after gate adoption, run `.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0103/main.py`.
The separately authored [verify.py](verify.py) reconstructs every integer candidate, the actual trace/full-field norm matrices and the selected complete-root Jensen certificates.
Run `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0103/verify.py` only after the author command completes; it requires the actual author witness files.
Both implementations share NumPy for exploratory sampling and FLINT for certified root/ball arithmetic; separately implemented arithmetic is not a second numerical library.
The inspected local dependencies are NumPy2.3.5, SymPy1.14.0 and python-flint0.9.0.
The author command precedes the verification-only command, whose selected witness must exist.

<a id="certified-results"></a>
## Certified results and limits

The author run completed at 2026-10-18T13:59 after C167 adoption through R400.
Both inputs evaluated exactly40 labeled candidates at each of the two prescribed exploratory resolutions.
All sampled candidates were rankable, and both selected the SAME signed form

    X=E, s=-1, p=2, N=(E-G)^2-2G^2.

The16384-node sampled means were0.4385988358226013 and2.0774304663413705; these are not certified integrals.
Complete-root Jensen gives the following certified quantities, with every displayed decimal having absolute error less than1e-10.
All strict signs use the retained outward balls.

| Original input | Haar I | Original conjugate mean Lambda | Lambda-I | I-(-1/16) |
| --- | ---: | ---: | ---: | ---: |
| quartic_Salem_seed | 0.438649129321 | 11.846597593869 | 11.407948464548 | 0.501149129321 |
| Lehmer_degree10 | 2.077470112805 | 6.822392824919 | 4.744922712115 | 2.139970112805 |

Thus BOTH SELECTED WITNESSES have I>0 and miss both negative-Haar saving and the operational1/16 target below0.
The original means are computed from the exact signed trace norms-19490542556 and-652586050504103, using Lambda=log|Norm_F U|/[F:Q].
Their complete original norms are respectively379881249127247013136 and425868553312543671380419834609, exactly the squares of those trace norms.
The exact original quotient identity and both full-resultant/trace-square calculations passed.

Both numerators have signed leading and constant coefficient-50176 and signed squarefree content-16.
Their complete degrees/root multiplicity counts are120 and300, and the full L^2=944784000000 denominator is retained.
The quartic completed at256 bits.
The Lehmer256-bit root call returned insufficient precision; its single predeclared512-bit escalation completed successfully.
The native attempt record preserves that failure, and neither input timed out or required a changed parameter.

This is a certificate for at most ONE selected witness per input, not a certified minimum of the40-form grid, a continuous optimum or an exclusion of all integer s and admissible p.
The exploratory failure to select a negative witness does not prove that every unselected candidate has nonnegative Haar cost.
No odd-cross-term quadratic extension, larger grid or alternative input is run as part of this J.
The original-root/Haar discrepancy is substantial on both tested witnesses and is not replaced by a transfer theorem.
No uniform expanded coefficient budget, new near-one coverage or unrestricted Mahler gap is obtained.
The independent native verification completed on both inputs after its own fresh same-window48-percent reading at 2026-10-18T13:59.
It rebuilt all40 integer numerators using Python convolution, reconstructed the trace polynomial by Laurent triangular elimination, and computed the selected trace/full-field norms through quotient multiplication matrices with Bareiss determinants rather than the author's resultants.
SymPy supplied its separate squarefree decomposition, while the author used FLINT factor_squarefree.
All40 candidates were rankable at both resolutions, every exploratory floating mean agreed exactly, and the selected-witness protocol was reproduced; these facts still do not certify a grid minimum.
Each selected numerator has one squarefree factor of multiplicity1; the independent full root counts, signed leading/content, exact scalar and all enclosing quantities agreed with the author.
The independent quartic run also completed at256 bits, and its Lehmer256-bit root call required the same sole512-bit escalation; neither input timed out.
The review is non-blind: the author choices and approximate values were disclosed before independent execution.
Both implementations share NumPy sampling and the FLINT certified root/ball engine, so this is separate exact reconstruction/native execution, not a second numerical library or formal proof.
The complete [R401 whole independent finding](../../../audits/reviews/Yin_R_G0401_v1.md#signed-j103-whole-independent-finding) checks this entire protocol, native evidence, final account and all finite-scope limits.
No Task-level completion follows from these finite certificates.

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
| `Lehmer_degree10-verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0401_v1.md#signed-j103-whole-independent-finding) |
| `Lehmer_degree10.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0401_v1.md#signed-j103-whole-independent-finding) |
| `quartic_Salem_seed-verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0401_v1.md#signed-j103-whole-independent-finding) |
| `quartic_Salem_seed.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0401_v1.md#signed-j103-whole-independent-finding) |
| `results.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0401_v1.md#signed-j103-whole-independent-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0401_v1.md#signed-j103-whole-independent-finding) |
