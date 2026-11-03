---
author: Yin
---

# Exact weighted carry and radical-product controls

## Original question and native inputs

This computation home retains the complete original Python program from [L5](../../../ledger/Yin_L_G0005_v1.md), dated 2026-10-06, and the complete actually retained execution record.
The [native source](carry_controls.py) enumerates exact integer coefficient reductions, collision multiplicities and the golden five-state transition matrix; the [retained observations](observed-results.md) contain the original matrix, all table entries, asserted finite test domains, original Python versions and execution limitations.
The old material retained these observations rather than a raw complete JSON stdout file, so none is fabricated here.
No mathematical program is run during this maintenance.

## Reproduction and original execution

From the repository root, the retained standalone source can be run with:

    .venv/Scripts/python.exe -X utf8 mathematics/computations/programs/Yin_J_G0115/carry_controls.py

It prints a JSON summary to stdout and creates no result file itself.
The author executed the original embedded source with CPython 3.13.15 on 2026-10-06.
A later coordinating reproduction on that date used CPython 3.14.7, with the same finite assertions passing.
The standalone path is a current retention path and did not exist at those original execution times.
Source retention changes only CRLF to LF and the final newline.

## Results and boundaries

The original direct digit-enumeration and complete five-state carry-matrix probabilities agree for n=0 through 20.
The radical product equalities pass for r=1,2,4,8 and n=0 through 16, with cyclotomic and nonunit controls retained.
The rational vector gives the exact all-length theta=5/8 inequality by the separately retained mathematical proof, rather than by finite extrapolation.
The finite entropy values are upper bounds for the limiting collision rates, and the radical equality requires the full relative-degree hypothesis.
These fixed controls do not establish a parameter-independent return estimate or the unresolved reciprocal Mahler gap.
This maintenance checks static Python syntax and retained evidence only, without a new run or an independent native-program reconstruction.
