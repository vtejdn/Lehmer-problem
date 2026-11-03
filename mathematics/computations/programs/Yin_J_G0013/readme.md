---
author: Yin
---
# Replay of the OpenAI family 153 degree-31 certificate

Context: [Ope26c-U003](../../../audits/literature/Ope26c/Yin_U003.md#ope26c-u003), acquired at Yin's explicit source-audit request on 2026-10-07.
This bounded audit does not resume the paused autonomous G0001 run.

## Question and scope

Reproduce the source's finite exact-arithmetic certificate for its single degree-31 polynomial and independently check the displayed rational margins connecting the estimates.
There is no parameter scan, new counterexample search, or floating-point premise.

## Files

| File | Role |
| --- | --- |
| [verify.py](verify.py) | Byte-preserved OpenAI source program, originally `verification/verify_degree31.py` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Original author attribution remains OpenAI. |
| [LICENSE](LICENSE) | Byte-preserved upstream Apache License 2.0 accompanying the copied OpenAI program, from the same fixed commit. |
| [verify_bounds.py](verify_bounds.py) | Coordinator's independent Fraction checks of displayed analytic constants; imports none of the source verifier's helpers. |
| Exact certificate values (`mathematics/computations/outputs/Yin_J_G0013/certificate.txt`) | Retained root counts, coefficient extrema, moment/Gram numerators and anisotropy factors from the successful source replay. |

The 19 exact scalar-margin conditions remain explicit in `verify_bounds.py`; all passed in the recorded inspection below.

## Reproduction

From the repository root, follow the [computation tool-selection guidance](../../../../framework/rules/computations.md#computation-tool-selection) and use the standard library with assertions enabled; on POSIX use `.venv/bin/python`.

```powershell
.venv/Scripts/python.exe -X utf8 -B mathematics/computations/programs/Yin_J_G0013/verify.py
.venv/Scripts/python.exe -X utf8 -B mathematics/computations/programs/Yin_J_G0013/verify_bounds.py
```

The source program uses `S=10^30`, root-center denominator `E=10^40`, weight denominator `W=10^9`, `R=3000`, `H=100`, `K=2000`.
All finite assertions use integer/Fraction arithmetic and the prescribed rounding order.
The byte-preserved source imports only Fraction and performs no file/network/process operations; both programs print their results.
Retained mathematical values use `mathematics/computations/outputs/Yin_J_G0013/certificate.txt`, outside Git.
A fresh clone can lack that file; reading the group does not replay the source.

## Results and limits

Both programs completed successfully.
The source replay verified 31 disjoint root disks, coefficient arrays, 753 nonzero predictor rows, exact correlation/variance/Gram numerators and three upper-rounded anisotropy products.
The independent program passed all 19 displayed rational-margin conditions.

The replay reproduces the supplied finite certificate; it is not a separately implemented recomputation of all moments.
The independent script checks selected scalar margins, not the entire root/character calculation.
Infinite-product error bounds, forbidden-frequency elimination, typical-word concentration and the lattice-counting-to-singularity argument remain obligations reviewed in the linked source unit.
No Lean/kernel check was performed and no Lehmer gap is certified by this computation.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
