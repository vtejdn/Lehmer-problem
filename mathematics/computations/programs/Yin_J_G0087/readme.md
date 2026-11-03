---
author: Yin
---

# One original Lehmer positive-log certificate with rational critical-level intervals

## Question and scope

[C449](../../../claims/Yin_C_G0449_v1.md#complete-critical-level-positive-log-certificate) owns the complete critical-level reduction, UNRUN quadrature proof, exact original finite certificate and original-cost accounting.
The actual executed method uses the original ascending Lehmer P=[1,1,0,-1,-1,-1,-1,-1,0,1,1], trace Q=[3,4,-5,-5,1,1], d=10, H=9, b=1/4, N=4096 and 160-bit outward fixed-point arithmetic.
An earlier unrun quadrature plan was replaced before execution by the exact [J86](../Yin_J_G0086/readme.md) recurrence; no trigonometric node or numerical quadrature was executed.

The fixed grid [-2,9/4] with step 1/64 isolates degree-exhausting roots of Q, Q', 4Q+1 and 4Q-1, bisecting to width at most 2^-40 within 60 steps while retaining exact grid roots.
All endpoint/critical values must lie outside [-1/4,1/4].
Four interior component covers each use 128 rational cells with fixed derivative sign and positive lower bounds for (4-x^2)Q'(x)^2.
Pi uses 64 terms in each rational arctan bound; log(9) uses 128 positive atanh terms and its explicit remainder.
All square-root roundings satisfy integer-square inequalities.

## Files and reproduction

[main.py](main.py) supervises [worker.py](worker.py) with a live aggregate 180-second limit.
The worker imports only [J86 fast.py](../Yin_J_G0086/fast.py) for its recurrence and requires comparison.json (`mathematics/computations/outputs/Yin_J_G0086/comparison.json`) and lehmer1024.json (`mathematics/computations/outputs/Yin_J_G0086/lehmer1024.json`) as exact n=64/1024 overlap inputs.
It checks the complete upstream input, H, degree, R, depth and state shape before use.
The standard library suffices, and output paths resolve from the actual repository/J location.

```powershell
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0087/main.py
```

The completed certificate.json (`mathematics/computations/outputs/Yin_J_G0087/certificate.json`) retains all rational root/critical/cover data, 512 cell bounds, elementary constants/tails, every 4,096 outward moment-term pair and the final eleven-state vector.
Its scalar comparisons at n=0,8,64,128,256,512,1024,2048,4096 are exact mathematical values, not continuation files.
Complete output is published atomically; failure remains failed or incomplete.

## Results and limits

The author calculation completed on 2026-10-11 using the exact recurrence revision.
All 19 isolated roots exhaust degrees 5/4/5/5, and all six critical/endpoint, four cover and 512 derivative-cell gates passed.
All 40,960 signed divisions, 40,960 extended-state bounds, 45,067 stored-state bounds, 4,097 scalar ranges, 4,096 monotonicity checks and 4,096 summand bounds passed.
Direct original-Laurent convolution independently checked moments 1--8; saved upstream n=64/1024 overlaps also matched.
The calculation retains 1,351,680 recurrence term accumulations, maximum numerator/divisor sizes 25,990/16 bits and 7,816 digits in the final scalar numerator.

The complete rational lower certificate is

    m(P) >= 415041559215166780091538487173593981975777634805
            /2923003274661805836407369665432566039311865085952
         = 0.141991479384568075688962... > 7/50.

The finite T4096 value is approximately 0.214851005982969 and the fully paid outward tail approximately 0.0728595265984006; all acceptance comparisons use the retained rational endpoints.
This is one original-input finite lower bound, not an input-uniform cutoff, unrestricted gap or Task completion.

## Completed separate review

[R209](../../../audits/reviews/Yin_R_G0209_v1.md#critical-positive-tail-whole-finding) retains the complete original argument/program/certificate checks with upstream recurrence authorship and actual initial author-math-check exposure disclosed; its current relationship is SELF.
A separately implemented read-only check covered all geometry, rounded terms and the final rational bound above 7/50.
Recurrence verification through 4096 remains distinct from direct original-Laurent checks through 8.
The earlier L379/R281 scope alone does not review the new tail or geometry.
The current [R654 whole SELF finding](../../../audits/reviews/Yin_R_G0654_v1.md#current-critical-positive-tail-whole-finding) records a separate original-domain reconstruction of all terms, weighted cells and exact lower bound on2026-10-22, disclosing the shared geometry helpers and separately generated recurrence.
No original native bytes or pending-review metadata were changed.

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
| `certificate.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0209_v1.md#critical-positive-tail-whole-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0654_v1.md#current-critical-positive-tail-whole-finding) |
