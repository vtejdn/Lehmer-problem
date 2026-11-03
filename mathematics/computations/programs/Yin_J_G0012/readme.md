---
author: Yin
---

# Exact eight-digit support of the Mercat example reported in BV20

Context: [G0001](../../../tasks/Yin_T_G0001_v1.md#contract) and [the complete current direct proof](../../../claims/Yin_C_G0273_v1.md#binary-support-counterexample-algebra).

## Question and scope

For the single polynomial P=t^6+t^5+t^4-t^3+t^2+t+1, retain the executed eight-digit diagnostic and independently check its finite exact payload.
The question is whether its 256 binary words give fewer than M(P)^8 distinct values, contradicting universal binary support attainment throughout M<2.
This is an existing source example, not a discovered Lehmer counterexample.
The linked written proof supplies an enumeration-free argument, irreducibility, conjugate locations and the all-length consequence.

## Files

| File | Role |
| --- | --- |
| [probe.py](probe.py) | Original single-input diagnostic; recursive integer power remainders and rational endpoints, with separately labeled numerical roots. |
| probe.json (`mathematics/computations/outputs/Yin_J_G0012/probe.json`) | Complete original structured output, including initial and unsuccessful coarse endpoint probes. |
| [verify.py](verify.py) | Separate standard-library verifier using all pairwise polynomial divisions and exact rational comparisons; imports no author helpers. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0012/verification.json`) | Actual verifier output and exact finite comparison scope. |

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0012/probe.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0012/verify.py
```

The original diagnostic uses SymPy with its default 15-digit `nroots`; those root observations remain exploratory.
Integer and Fraction fields are exact, with no random seed, parameter scan or other input file.
The verifier uses only the standard library and requires the actual `probe.json`.
It compares the named mathematical payload, not timestamps or dependency metadata.
Numerical roots, library factorization and the sextic discriminant remain outside its certification scope.

Generated output uses `mathematics/computations/outputs/Yin_J_G0012/`, independently of the caller's directory.
Actual retained output is local and Git-ignored; a clone may lack it.
Verification reports missing required inputs without substituting other data or implicitly running a producer.
These are current reproduction instructions, not a new execution or proof review.

## Results and limits

The original diagnostic found 252 distinct values and four disjoint two-word collision fibers.
The exact signs support 511/256<M(P)<2 and (511/256)^8>252 under the written algebraic reduction.
An earlier coarse upper trace endpoint 31/20 failed the intended upper measure sign; both its value and that failure are preserved.

The separately implemented verifier passed all 32,640 unordered word-pair divisions, eight power remainders and every retained rational comparison.
The diagnostic's floating-point fields remain exploratory.
The linked full proof establishes rho<=log(252)/8<log M(P), with no floating-point premise.
This refutes a proposed intermediate universal equality for binary alphabets below measure two.
It does not refute the Lehmer gap, give a near-one family, or decide equality for every input in a smaller Mahler window.

The original2026-10-07 written input remains [L82](../../../ledger/Yin_L_G0082_v1.md#binary-support-counterexample-algebra).
The [retained original coordinator finding](../../../audits/reviews/Yin_R_G0533_v1.md#historical-mercat-coordinator-finding) covers the complete proof and the retained independent computation at its stated scope, with its actual shared collision contribution.
The verifier's separate implementation is a computational fact; it does not establish an isolated agent context.
The [current whole proof finding](../../../audits/reviews/Yin_R_G0533_v1.md#current-mercat-sextic-finding) includes complete static reading of both programs and both JSON outputs, with AST/JSON parsing only and no new execution or certification of the exploratory fields.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
