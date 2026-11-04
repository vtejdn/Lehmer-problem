---
author: Yin
---
# Normalized many-vertex Lehmer displacement certificates

## Native input availability

The selected217 original words and32 cell/axis barycentric certificates in pilot.json are unavailable in this checkout and its selected local Git history.
The normalized-descent proof and original checking accounts do not encode that full native selection.
The author verifier and J27 cannot currently replay it.
Supply only the original selected cell/word/barycentric payload at this group's tracked inputs/ and update those consumers; a new floating LP selection would supply different evidence.

## Scope

Compare normalized joint displacement bodies c/||c||^2 with the preceding simplex certificate.
Retain numerical discoveries separately from exact certificates.

The responsible proof and domain are [C399 normalized descent](../../../claims/Yin_C_G0399_v1.md#normalized-lehmer-radius-eight).

## Files and reproduction

- [probe.py](probe.py): numerical radial linear programs for normalized joint vectors over the two wide cells, followed by positive barycentric witness discovery at fixed rational axis targets.
- pilot.json (`mathematics/computations/outputs/Yin_J_G0024/pilot.json`): retained integer words and nonbinding numerical diagnostics.
- [verify.py](verify.py): exact denominator, full-cell and positive-barycentric checks using the J G0022 interval primitives.
- verification.json (`mathematics/computations/outputs/Yin_J_G0024/verification.json`): the completed exact result.

From repository root:

For discovery, select a compatible Python environment containing the declared NumPy and SciPy dependencies; the shared baseline dependency file does not include SciPy.
The commands below use normal package resolution.
The exact verifier requires only the Python standard library and the retained `pilot.json` integer words.

```powershell
python -B mathematics/computations/programs/Yin_J_G0024/probe.py
python -B mathematics/computations/programs/Yin_J_G0024/verify.py
```

Discovery requires NumPy and SciPy; exact verification uses the standard library.

## Result and limits

Both closed cells [1/2,3/4] and [3/4,1] pass.
Their complete eight-dimensional normalized hulls contain all sixteen signed coordinate targets at rational radii 101/500 and 207/1000.
Thirty-two nine-word certificates use 288 word occurrences, 217 distinct original words, with maximum length eleven.

The exact verifier checks every squared displacement denominator is positive, every word maps the full assigned interval strictly into (-1,1), and every retained axis point has strictly positive exact barycentric coordinates.
It then proves the common Euclidean neutral threshold eight and squared-norm drop at least 57/100.
Saved floating-point roots, weights and radial optima are not accepted by the verifier.

This certifies a new descent mechanism and reduction to a radius-eight compact residue.
It does not enumerate that residue, supply its complete paths to zero, identify an infinite actual Lehmer core, or establish any uniform full-law probability estimate.
The [complete SELF normalized-body review](../../../audits/reviews/Yin_R_G0069_v1.md#normalized-lehmer-radius-eight-review) and [J G0027](../Yin_J_G0027/readme.md) record the complete proof scope and separately implemented finite checks.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
