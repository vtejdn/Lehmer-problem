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

<a id="degree64-cell"></a>
## Finite searches in the degree-64 trace cell

The [exact cell input](trace64_cell.py) specifies the 31 rational separators, the 32 free Chebyshev coefficients, the seed and the closed target disk.
Run it with standard Python to check the sign pattern and the ellipse bound for the proposed measure \(M<(219/200)^2\).

The [height-free proof](../../../claims/Yin_C_G0876_v2.md#argument) excludes the whole specified root configuration by bounding the coefficients with the vertices of its interpolation polytope.
With standard Python, run the following commands from this directory.

~~~text
python -E -B exact_cell_unbounded.py
python -E -B exact_cell_hull.py
~~~

The [unrestricted verifier](exact_cell_unbounded.py) checks the [height-free certificate](exact_cell_unbounded_proof.json.gz) and exhausts 2639 internal prefixes.
Of its two remaining vectors, the seed has no root in the closed disk, and the height-four vector already vanishes at the left separator.
The [height-three verifier and vertex construction](exact_cell_hull.py) checks the [first certificate](exact_cell_hull_proof.json.gz) and exhausts 959 internal prefixes, leaving only the seed.
Each certificate supplies integer separating normals and scales.
The verifiers recompute vertex extrema, prefix bounds and all required branches with integer arithmetic.
The ordinary verification commands require neither a solver nor the scripts used to find the normals.

- [cell_bound_short.py](cell_bound_short.py) enumerates all monic reciprocal integer polynomials of degree 64 and coefficient height at most three that differ from the seed in at most five of the 32 independent coordinates.
  Of the 1,613,593,345 inputs, exactly 38 pass the meet-in-the-middle test for the seed's strict signs \((-1)^i Q(s_i)>0\) at all 31 ordered separators \(s_0<\cdots<s_{30}\), where \(Q\) is the trace polynomial.
  Gaussian-integer Taylor bounds exclude a root of \(Q\) in the closed disk for each of these 38 inputs.
- [cell_bound_measures.py](cell_bound_measures.py) uses cyclotomic division and Graeffe bounds to prove that all 38 polynomials passing those inequalities have whole multiplicative Mahler measure \(M>(219/200)^2=1.199025\).
  The maximum number of root squarings used was 12.
  If each open gap contains a root and two additional real roots lie in different gaps, then \(Q\) has the same sign at the two endpoints of each of those two gaps.
- [cyclotomic_slice.py](cyclotomic_slice.py) exhausts all candidates divisible by the seed's \(\Phi_{47}\), with positive endpoint sign and coefficient height at most three.
  The cofactor \(U\) is reciprocal and monic of degree 18, and \(s=U(1)\) is a plateau coefficient of \(\Phi_{47}U\).
  The positive choices are \(s=1,2,3\).
  If \(B_j\) is the partial sum of the first \(j+1\) outer coefficients of \(U\), then \(B_0=1\), and \(B_j,s-B_j\) occur as coefficients of the product for \(1\le j\le8\).
  The middle coefficient of \(U\) is \(s-2B_8\).
  This gives \(6^8+5^8+4^8=2135777\) vectors, counting all such positive-endpoint choices.
  The degree-nine cofactor trace must supply the upper-half-plane root since the cyclotomic traces are all real.
  A box-wide Taylor bound at the center leaves 17 vectors, and coefficient-specific Taylor bounds exclude the closed disk for all 17.
- [cell_bound_moments.py](cell_bound_moments.py) uses the real brackets and complex disk to enclose all 32 Newton sums by rational arithmetic.
  Exactly 13409 height-three prefixes satisfy these bounds through depth eight.
  The later congruence and interval bounds give at most \(13409\cdot4^{22}\cdot3^2\) complete candidates before applying other constraints.

Run each named script with python -B from this directory.
These subdomains may overlap.
The preliminary [full-variable MILP](trace64_milp.py) used HiGHS 1.15.1 and NumPy 2.5.4 and returned no certified candidate within its node caps.
The [subbox branch search](trace64_blocks.py) checks every cut with integer arithmetic and independently exhausts the frequency intervals 4 through 27 and 8 through 31 when the other eight coefficients are fixed to the seed.
These solver-based runs served as comparisons during construction of the full certificate.

The [degree-64 resultant certificate](trace64-resultant.md) forces a real-root displacement in the target disk search, with an exact bound of \(1/50\) for at least one original control root in the midpoint cells.

<a id="degree56-cell"></a>
## One fixed degree-56 all-real trace cell

The [selected S10 test](../../../strategies/Yin_S_G0010.md#primitive-fixed-cell-test) uses the actual parent of J156's DP seed-32 proposal-448 minimum after the whole-variable sign change.
The [complete cell description](trace56_cell.md) retains its 29 fixed rational nodes, complete \(1<M<6/5\) implication, exact open simplex, coefficient-height-four box and exclusion of both complete known-value fibers.
The [exact preparation program](trace56_cell.py) and [native input](trace56_cell.json) preserve the original-parent correspondence, both positive-exterior trace cores, all vertices, strict integer rows and remainder constraints.
The [numerical suggestion program](trace56_milp.py) has completed its model-building and separate real-process controls and the [single formal test](trace56_cell.md#formal-result).
The [independent preparation finding](../../../audits/reviews/Yin_R_G1111_v14.md#fixed-cell-preparation-review) and [implementation finding](../../../audits/reviews/Yin_R_G1111_v14.md#fixed-cell-implementation-review) verify this fixed input, complete-measure reduction, actual model and retention controls.
Its floating rows are outward relaxations, and every proposed integer polynomial still needs exact checks and the complete original-polynomial certificate.
The formal run returned numerical infeasibility after 13013 reported MIP nodes and approximately 4.175 seconds of total supervisor time, without an observed or returned candidate.
The [complete native observation](trace56_observation.json) preserves the actual model and all events.
The [independent actual-result finding](../../../audits/reviews/Yin_R_G1111_v15.md#fixed-cell-result-review) verifies the complete numerical observation, retention and unresolved interpretation at that stage.

The separate [exact-tree argument and result](trace56_tree.md), [program](trace56_tree.py) and [native proof](trace56_tree_proof.json.gz) now establish that the fixed closed simplex in the height-four integer box contains only the original parent.
The complete certificate has 1504 internal prefixes, one leaf and an empty frontier; all of its pruning bounds are checked with integer arithmetic.
The [independent mathematical finding](../../../audits/reviews/Yin_R_G1111_v16.md#fixed-cell-exact-tree-review) verifies the entire coverage and parent membership, while the [evidence finding](../../../audits/reviews/Yin_R_G1111_v16.md#fixed-cell-exact-tree-evidence-review) verifies the actual program, bounded attempt and complete native retention.
Consequently the selected strict cell contains no height-four integer point outside the known-value fibers, without an exclusion of other cells, heights or degrees.

The separate [conjugate-evaluation resultant test](trace56_resultant.md) checks a fixed sufficient bound on the same vertex simplex, with all five root brackets and 145 vertex-value intervals reproduced by [its program](trace56_resultant.py).
Its separate-maximum product is enclosed between 537718784.872951328062 and 537718784.872951328063, so that particular bound cannot force divisibility by the Lehmer trace.
This useful failure supplies neither a feasible integer candidate nor an exclusion of the cell, and does not optimize the common interpolation weights or the coefficient box.
The [independent auxiliary finding](../../../audits/reviews/Yin_R_G1111_v14.md#fixed-resultant-bound-review) reproduces all intervals and checks that precise insufficient-bound conclusion.
