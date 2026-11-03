---
author: Yin
---

# Exact bounded reciprocal degree-window countersearch

## Question and fixed scope

This native computation home retains the complete original [L6 finite countersearch](../../../ledger/Yin_L_G0006_v1.md#bounded-countersearch), its [program](countersearch.py) and [complete original JSON](original-output.json), without a new execution.
It covers all reciprocal monic constant-one coefficient patterns in degree 2,4,6,8,10 with independent coefficients in {-2,-1,0,1,2}, and degree 14,16 with coefficients in {-1,0,1}: exactly 12,653 patterns.
The original cap is 180 seconds between samples/certification attempts; a single atomic arithmetic operation may exceed it.
No additional search batch is authorized or run by this retention.

## Actual program inputs

The exact program reads the three actual Python blocks in [L4](../../../ledger/Yin_L_G0004_v1.md), executing only their declared helper prefixes before sample loops.
Those source blocks remain necessary original native inputs and are retained unchanged; their standalone copies and original outputs also have [J114](../Yin_J_G0114/readme.md) as their native home.
The exact mathematical scalar-Gram and sufficient irreducibility interfaces now have their adopted proof home in [C209](../../../claims/Yin_C_G0209_v1.md#statement).
The retained source and JSON change only CRLF to LF and the final newline.

## Reproduction

From the repository root:

    .venv/Scripts/python.exe -X utf8 mathematics/computations/programs/Yin_J_G0116/countersearch.py

The program prints JSON to stdout and does not append to a fixed material.
The original author run on 2026-10-06 used CPython 3.12.14, returned exit code 0 and completed in 6.203 seconds.
The coordinating replay on that date used CPython 3.14.7, completed in 6.585212 seconds and matched all result fields except interpreter version, start timestamp and elapsed time.
These are original execution facts and do not describe a run of the new standalone retention path.

## Results and limitations

Exact division removes 5,203 patterns with a cyclotomic divisor; all 7,450 squarefree survivors pass |disc p| G_(2d)>(2d)^d.
Every irreducible noncyclotomic polynomial in the stated finite windows survives the exclusions, so the finite no-counterexample result covers the entire specified core there, without requiring all survivors to be irreducibility classified.
All 48 retained smallest-ratio candidates are certified irreducible, so each nonempty window's retained minimum is also its exact core minimum.
The least ratio across these windows is 105844516006149/10240000000000 at the degree-ten signed Lehmer polynomial.
The complete per-window tables, exact minimizer polynomials and assessment remain in L6, and all candidate coefficients, discriminants, Gram values, bounds and certificates are retained in the JSON.
This gives no unrestricted positivity theorem, degree-uniform exponential surplus or Lehmer gap.
Original author-side and coordinating findings retain their scopes in [R799](../../../audits/reviews/Yin_R_G0799_v1.md#original-g0651-account); that retention performed static syntax/JSON checks without an independent rerun or mathematical revalidation of the finite batch.

## Independent finite inspection

The separately arranged [complete finite finding](../../../audits/reviews/Yin_R_G0799_v1.md#complete-isolated-finite-countersearch-finding), dated 2026-10-22T23:51, checked the entire original program, actual L4 helper prefixes, finite Gram/cyclotomic/irreducibility reduction and complete original JSON before comparing the old review conclusions.
The [retained verification program](reviewer_exact/check.py) imports none of the original helpers.
It independently reconstructs cyclotomic polynomials, exact discriminants and orbit Gram determinants throughout the same 12,653-pattern domain, independently verifies all 48 retained certificates and reruns the unchanged native countersearch.
From the repository root, run:

    python mathematics/computations/programs/Yin_J_G0116/reviewer_exact/check.py

The command resolves the actual repository and J from its own location, so another working directory is also supported.
It requires only Python's standard library, the original JSON and, for the native replay, countersearch.py with its actual L4 inputs.
Its replaceable local result (`mathematics/computations/outputs/Yin_J_G0116/reviewer_exact/result.json`) uses this J's ignored output home; it is generated only after all comparisons pass.
The successful CPython 3.13.15 run from another working directory completed all seven windows and native replay in 46.24 seconds within the verification command's 180-second cap.
All 5,203 cyclotomic exclusions, 7,450 squarefree survivors, zero positivity failures, exact minima, 48 candidate records/certificates and every nonvolatile native output field agree.
The new finding and the complete original SELF/UNKNOWN natural accounts, relationships and bindings are retained together in [R799](../../../audits/reviews/Yin_R_G0799_v1.md).
This review supplies no result outside the original degree/coefficient windows, no whole C209 or original Szego proof audit and no Task/E resumption.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
