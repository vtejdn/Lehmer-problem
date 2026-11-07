---
author: Yin
---

# Exact controls for the reciprocal coefficient and trace searches

This finite computation tests pruning of coefficient prefixes in the reciprocal integer box against a separate classification of every complete input.
The primary controls have degree ten, coefficient height at most one or two, and strict window from one to six fifths.
The search and the certifier use integer or rational arithmetic.

[pilot.py](pilot.py) enumerates the five independent coefficients of a monic integral reciprocal polynomial with constant one.
It compares the single Newton-sum tests with the joint cuts from vectors with entries in \(\{-1,0,1\}\), up to the current coefficient depth and with shifts and overall signs removed.
Separately it classifies every complete input by exact cyclotomic division and Graeffe norm and coefficient bounds, with an explicit undecided output for an insufficient iteration cap.
Both computations can be run from this directory with standard Python.

```text
python -B pilot.py --height 1
python -B pilot.py --height 2
python -B trace_control.py
```

| Coefficient height | All inputs | Single-moment leaves | Joint-cut leaves | Measure one | Strict positive hits below 6/5 | Above 6/5 | Undecided |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 243 | 195 | 185 | 50 | 2 | 191 | 0 |
| 2 | 3125 | 1007 | 801 | 143 | 2 | 2980 | 0 |

In each box the two hits are the degree-ten Lehmer polynomial and its image under \(x\mapsto-x\).
Every positive hit and every measure-one input passed all cuts.
The two boxes overlap and the sign variants have the same measure.

[trace_control.py](trace_control.py) verifies a separate degree-18 input from [Mossinghoff's two-exterior-root row](../../../audits/literature/Mos26/readme.md).
It reconstructs the entire reciprocal polynomial and verifies seven real intervals, the Rouché test on an upper-half-plane disk, and bounds for the enclosing rectangle between two confocal ellipses.
The resulting strict measure interval is \((1.2013475236,1.20143521)\).
The [mathematical search conditions](../../../ledger/Yin_L_G0462_v1.md) supply the interpretation of both controls.
These programs were executed by their developers and rerun by the coordinating agent.
