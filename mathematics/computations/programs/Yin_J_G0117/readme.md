---
author: Yin
---

# Exact quartic carry and cyclotomic truncation controls

## Original scope and files

This retains the complete original [L8](../../../ledger/Yin_L_G0008_v1.md) source [carry_domination.py](carry_domination.py) and [finite execution account/table](observed-results.md), dated 2026-10-06.
The `original-output.json` address identifies the local output of that recorded run.
The exact polynomial is t^4-t^3-t^2-t+1, reduced in its actual power basis, alongside the genuine quotient modulo 2 and the cyclotomic lambda=1 killed-state control.
The standalone source preserves the original program and assertions; its printed JSON is a local run product.
No program is run during this retention.

## Reproduction

From the repository root:

    .venv/Scripts/python.exe -X utf8 mathematics/computations/programs/Yin_J_G0117/carry_domination.py

The program prints JSON to stdout and creates no result file itself.
The original author run used CPython 3.13.15 and the coordinating replay used CPython 3.14.7, both on 2026-10-06 with exit code 0.
Every original output field and rational table entry matched in that replay except interpreter version.
These are historical executions of the original retained block, not executions of the new standalone path.

## Outcomes and mathematical boundary

All quartic assertions for n=0 through16 and all cyclotomic truncation assertions for n=0 through64 passed in the original executions.
At quartic n=16 the support is 35,662, q_n=5339/134217728, modular q_n=1/16 and the block upper bound is 6561/65536.
The all-length domination, quotient plateau, projection obstruction and continuous integral ceiling require the separately retained mathematical arguments; finite tables supply only their stated control checks.
No arbitrary truncated matrix, polynomial endpoint count or numerical spectral gap is promoted to an all-length or uniform arithmetic estimate.
Current retention checks syntax and JSON without a rerun or independent program reconstruction.
