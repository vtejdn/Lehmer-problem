---
author: Yin
---

# Finite set checks for cyclic induction and rectangular alphabets

## Question and scope

This retains the exact standard-library Python source supplied through PowerShell stdin on 2026-10-06 in the original [L G0003](../../../ledger/Yin_L_G0003_v1.md#g0001-cyclic-induction) exploration.
It checks the finite trajectory and rectangular-alphabet set identities now proved in [C G0206](../../../claims/Yin_C_G0206_v1.md#argument).
No mathematical computation was run during this source retention.

The exact integer arithmetic covers B=Z/MZ for M=4,5,6, every multiplier 0<=a<M and induction lengths k=1,2,3.
The single-coordinate alphabets are {1}, {1,2}, {0,1,2}, with 0<=n<=9.
Rectangles alternate {0,1} and {1,2}, with 0<=q<=3.
The checks include noninjective maps and alphabets that omit zero.

## Files

| File | Role |
| --- | --- |
| [verify.py](verify.py) | Original supplied Python program, retaining the 1,530 exact mathematical comparisons and its original local-document assertions. Its saved file is a retention of that stdin source, not a newly claimed execution. |
| [Original mathematical input](../../../ledger/Yin_L_G0003_v1.md) | Retained fixed historical statement and argument; the program's literal path and equation-text assertion still refer to this actual input. |

## Reproduction

From the repository root, use `.venv/Scripts/python.exe -X utf8 mathematics/computations/programs/Yin_J_G0113/verify.py` with the shared repository environment.
The source requires the retained L G0003 mathematical input and its local link targets.
It prints to stdout and creates no generated output file.
The historical execution supplied the same Python source through a PowerShell here-string to `python -X utf8 -`; no standalone source file existed at that date.
The saved `verify.py` has not been executed during this maintenance.

## Results and limits

The recorded original process completed with exit code zero and stdout:

    {'trajectory_set_checks': 1530, 'local_link_targets': 'passed', 'control_characters': 'passed', 'formula_5_4_spacing': 'passed'}

The mathematical count is 1,350 comparisons of the single-coordinate trajectory identity and 180 rectangular-alphabet comparisons: 15 modulus/multiplier pairs, three induction lengths, 30 single-coordinate cases and four rectangular cases per pair and length.
The document assertions describe that original execution's then-current input; later source retention is not a claim that those operational checks have been rerun.
All analytic entropy, attainment, norm-height and positive-delay conclusions use the complete proofs in C G0206.
Finite checks do not prove entropy limits or a positive entropy gap.
The historical separate reviewer did not rerun this enumeration.
