---
author: Yin
---
# Exact order and cyclic-rotation checks for principal control blocks

## Question and scope

Verify the specific degree-six integer identities, powered-order obstruction and cyclic-rotation illustration used in [complete C489](../../../claims/Yin_C_G0489_v1.md#principal-block-control-fixed-scope).
The proposed length-six generator/negative/zero blocks induce the ternary law at theta=beta^6 after scaling by beta^6(1-beta^(-3)).
The actual suborder Z[theta] does not equal O=Z[beta].
D68 also proves a symbolic cyclic-rotation repair of this algebraic obstruction, and a distinct real-boundary obstruction even for a module-complete family.
This computation concerns those restricted block alphabets, not a counterexample to the full original law.

## Files

- [verify.py](verify.py) implements degree-six integer polynomial arithmetic, a Bareiss determinant, rational linear solving and rational interval evaluation, using only the Python standard library.
- verification.json (`mathematics/computations/outputs/Yin_J_G0041/verification.json`) retains the reconstructed matrix, coordinates, actual return path, real enclosures, prefix basis and seven cyclic rotations for h=7.

The program contains no state enumeration, random search or floating-point calculation.
It reconstructs each asserted identity from the fixed polynomial P=t^6-t^5-t^3-t+1.
The irreducible Salem property, actual root interval and ideal identification are reused from [complete C476](../../../claims/Yin_C_G0476_v1.md#degree-six-return-core-fixed-scope) and [complete C478](../../../claims/Yin_C_G0478_v1.md#degree-six-principal-saturation-fixed-scope), rather than claimed as newly certified here.

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0041/verify.py
```

The exact check passed.
It writes verification.json after all assertions pass.
The finite executed checks are:

- det(C6)=1024 and beta's exact theta-basis coordinates with last coordinate1/16;
- the fixed generator's original six-digit return and its translation;
- two actual ideal witnesses with nonintegral theta-basis coordinates;
- the first witness's complete original return path, reaching zero at digit5 then appending zero;
- exact rational real-coordinate bounds for that witness and both strict macro windows for the second witness;
- the return word from1, all seven prefix states, enclosures within[-1,1], and determinant1 of the first six prefix columns;
- all seven cyclic rotations for h=7, their actual translations and the exact divided-prefix identity, and the corresponding return of1-beta^(-7).

The proof for every h>=7 is D68's symbolic argument.
The one h=7 execution is a finite illustration and sign/order check, not a proof by numerical extrapolation.
The wider Horner interval for the fifth prefix is deliberately retained as executed; D68's sharper reciprocal enclosure follows from the separately checked identity s_5=-beta^(-1).

## Results and limits

The exact arithmetic confirms [O:Z[beta^6]]=1024, an original-returning actual ideal state obstructed for the three generator blocks, and a second obstructed ideal state strictly within the macro law's own real windows.
The cyclic prefix basis supplies a concrete algebraic repair.
D68 proves that the resulting family of signed cyclic rotations still preserves the half-line x_+>=1, so it does not give the full strict real-cell control needed by the compact-descent interface.

The program and proof are the structural research agent's author work.
There is no new literature intake, full-return or entropy claim, general termination theorem, optimal-margin computation, exhaustive search failure, or modification of the fixed L199 original-law result.
Full joint geometry after principal scaling and its explicit conditional costs are in [complete C489 Section5](../../../claims/Yin_C_G0489_v1.md#principal-scaling-full-neutral-cost).


## Complete separate review and fixed retention

The complete current C489 decision adopts the [actual whole SELF in R701](../../../audits/reviews/Yin_R_G0701_v1.md#current-principal-block-whole-finding).
The [entire original R103 proof/program finding](../../../audits/reviews/Yin_R_G0103_v1.md#principal-block-complete-independent-review) retains its03:42 scope and UNKNOWN initial relationship; the original listed author checks remain separately SELF.
The reviewer authored and executed [review_exact.py](review_exact.py), using companion matrices, permutation determinants and Cramer's rule without importing or executing the author code.
Its review_result.json (`mathematics/computations/outputs/Yin_J_G0041/review_result.json`) records the finite checks.
The full varying-input, all-h and metric claims were checked as written arguments.
The review discloses earlier dependency contributions.

The current reviewer program reads the retained L204 argument.
Its retained result comes from a successful rerun after that path update; the original independent review keeps its stated scope.

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0041/review_exact.py
```

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
