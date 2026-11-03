---
author: Yin
---

<a id="unit-cycle-leaf-independent-verification-declaration"></a>
<a id="unit-cycle-leaf-complete-independent-payload-review"></a>

# Unit-cycle leaf full scalar controls

[C567 statement](../../../claims/Yin_C_G0567_v1.md#statement) and [entire proof](../../../claims/Yin_C_G0567_v1.md#argument) retain the all-index theorem, adopted after [the actual isolated current whole review](../../../audits/reviews/Yin_R_G0776_v1.md#current-unit-cycle-leaf).
The original complete [written](../../../audits/reviews/Yin_R_G0776_v1.md#unit-cycle-leaf-complete-written-review) and [computational](../../../audits/reviews/Yin_R_G0776_v1.md#unit-cycle-leaf-complete-computational-review) findings retain the original L299/J75 inputs, real dates and UNKNOWN relationships; separate implementation supplies no isolation.
The exact domain is a=3,4,5,6,7,8.
B0 has diagonal1, superdiagonal1, lower-left-1 and other entries0; append row e1 to obtain B and put D=|B|.
Original and absolute presentations are[[I_(a+1),-B],[0,I_a]] and[[I_(a+1),-D],[0,I_a]].
The proper cover uses interleaved sheets, identity diagonal and the same signed-edge convention as J74.
All complete matrices, original/absolute/cover arrays, full-column-rank minors, Gram determinants and306 integer pencils are retained.

## Programs and reproduction

[verify.py](verify.py) writes result.json (`mathematics/computations/outputs/Yin_J_G0075/result.json`), using SymPy and author helpers reused from J74.
[review_independent.py](review_independent.py) writes review_result.json (`mathematics/computations/outputs/Yin_J_G0075/review_result.json`), using only the standard library.
Run from the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0075/verify.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0075/review_independent.py
```

Both retain120-second limits; the reviewer requires the completed author payload, with no draft dependency.
Generated files belong to `mathematics/computations/outputs/Yin_J_G0075/`.

## Results and actual checking relationship

All six controls,18 full polynomials and306 pencils passed, including formal numerator identities with independent symbolic y.
The a=3,4 original boundary factorizations have zero measure and are not positive successes.
At a=5 the full factors are P=Phi2 Phi10 S6 and A=Phi2 Phi5 Phi6 P4, with the entire cover product and neutral degrees5,7,12 retained.
No complete factor is discarded or normalized away.

The nonblind noncontributor reviewer reused its own J69/J72/J74 elimination, interpolation and sparse-polynomial primitives without importing author code or SymPy.
It independently built every matrix and reconstructed all18 arrays from306 integer Bareiss pencils and Newton interpolation.
An additional24 Fraction determinant checks cover minors and Grams.
Full Laurent expansion checks quotient traces after exact division by t+1; positive Gram values at t=-1 establish multiplicity exactly one in all six controls.
Recursive exact division of t^j-1 constructs the cyclotomic factors; restricted polynomial parsing and convolution check unrestricted bivariate identities.
All S6/P4 arrays, four rational endpoints, five sextic trace evaluations, rational-root candidates and exact schema fields passed.
This computation is distinct from the coordinator's complete all-a proof review.
Root count, threshold, monotonicity, limiting measure, factor-degree bounds and source applications depend on that written proof.
No minimal rank, optimum, near-one coverage or unrestricted gap is inferred.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
