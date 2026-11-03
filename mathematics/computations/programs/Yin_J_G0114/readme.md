---
author: Yin
---

# Exact finite orbit Gram and reciprocal-pattern certificates

## Question and retained scope

This computation home retains the three complete exact-integer Python programs used in [L4](../../../ledger/Yin_L_G0004_v1.md), together with the recorded scopes of their original local outputs.
Their original executions took place on 2026-10-06; this source retention is not a new execution or a new research allowance.
The mathematical general inequalities are proved directly in the original fixed material, and the native evidence records its finite examples and bounded sufficient irreducibility tests.
The later original coordinating reproduction with CPython 3.14.7 is distinct from the author executions with CPython 3.13.15.
No program has been run during this retention.

## Native files and original input

| Program | Local run output | Exact scope |
| --- | --- | --- |
| [examples.py](examples.py) | `examples.json` | Six named polynomials, six window multiples each, all dual-Gram checks at k=0–8, prime-cyclotomic equalities and the stated dilation controls. |
| [reciprocal_probe.py](reciprocal_probe.py) | `reciprocal_probe.json` | All 1,092 degree 2,4,6,8,10,12 reciprocal coefficient patterns in the fixed {-1,0,1} range; the eleven declared primes give sufficient finite-field certificates. |
| [trace_probe.py](trace_probe.py) | `trace_probe.json` | The same finite pattern range, added trace-polynomial certificates and the exact a/4 sign grid, -8<=a<=8. |

The second program reads the first Python block in the retained L_G0004, and the third reads that material's second block and its preceding helpers.
These literal original self-read paths and their mathematical source blocks remain actual required inputs; the saved standalone files do not claim to have existed at the original execution date.
The files preserve all original program text, changing only CRLF to LF and the final newline.
The JSON outputs are local run products; repeat the documented program and checks when their results need verification.

## Reproduction

From the repository root, use the shared environment with one of the exact commands:

    .venv/Scripts/python.exe -X utf8 mathematics/computations/programs/Yin_J_G0114/examples.py
    .venv/Scripts/python.exe -X utf8 mathematics/computations/programs/Yin_J_G0114/reciprocal_probe.py
    .venv/Scripts/python.exe -X utf8 mathematics/computations/programs/Yin_J_G0114/trace_probe.py

Each prints JSON to stdout and creates no result file itself.
The original executions extracted the corresponding retained code block and supplied it to Python from the repository root.
The saved outputs are historical execution evidence, not outputs produced by this maintenance.

## Results and limits

The original combined sufficient certificates cover 592 noncyclotomic irreducible examples: 386 direct finite-field and 206 additional trace cases.
They certify 23 cyclotomic patterns and leave 477 cases unclassified, out of the 1,092-pattern loop.
All 592 core examples pass the weaker N=2d positivity certificate; 16 fail the stronger fixed log(2)/8 sufficient threshold at that window.
Failure to obtain a finite-field or trace certificate is not a reducibility verdict.
The original Lehmer example has absolute discriminant 1332031009, G20=79461 and G40=18006972477; the stronger threshold fails at 20 and passes at 40.
These are finite, fixed-family outcomes, without an optimum, complete irreducibility enumeration, new uniform bound or unrestricted Mahler-gap conclusion.
The original separate reviewer inspected Sections1–5 and the first output without a native rerun; the later coordinating reproduction and the author's own later probe checks retain their different scopes.
This maintenance only retains source/evidence and performs static syntax and file/link checks.
