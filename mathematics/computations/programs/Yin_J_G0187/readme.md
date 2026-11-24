---
author: Yin
---

# An exact cut for the degree-bounded Salem-orthogonal minimum

<a id="cut"></a>
## Exact comparisons at \(601/500\)

Run from the checkout root with standard Python:

~~~text
python -B mathematics/computations/programs/Yin_J_G0187/small_cores.py
~~~

The input is Mossinghoff's 31 May 2026 native table at logical path
<code>mathematics/literature/pdf/Mos26/AllSmallMeasures_200.txt</code>.
Its [pinned edition and completeness scope](../../../audits/literature/Mos26/readme.md#complete-small-cores) distinguish the exhaustive list through degree 44 from the higher-degree records.
The [integer verifier](small_cores.py) uses the [existing parser](../Yin_J_G0185/pole_catalogue.py) for degrees and coefficients and [the existing Graeffe implementation](../Yin_J_G0144/pilot.py) for simultaneous root squaring.
It discards both numerical source columns when deciding the cut and the root signatures.

After \(j\) squarings a monic even-degree polynomial \(P\) gives a monic polynomial \(G\) of the same degree \(d\) with \(M(G)=M(P)^{2^j}\).
For every coefficient \(g_k\) the inequalities
\[
             |g_k|/\binom dk\le M(G)\le\sum_{l=0}^d|g_l|
\]
follow respectively from elementary symmetric functions and the circle norm.
Multiplying by \(500^{2^j}\) gives strict integer comparisons against \(601^{2^j}\).
At most 14 squarings were used, and every row was decided.
Of the 944 primitive cores through degree 44, four are strictly below \(601/500\) and the other 940 strictly above.
At degrees \(46,48,50,52,54\), all \(107,80,76,66,66\) listed rows respectively are strictly above.
The five latter lists include the [proved minimum at each degree](../../../audits/literature/MRW08/Yin_U001.md#degree); their exhaustiveness below \(1.3\) is unnecessary and was not assumed.

<a id="signatures"></a>
## Identifying the four survivors

For the three rows below, the program reconstructs the trace polynomial using \(T_0=2,\ T_1=X,\ T_{j+1}=XT_j-T_{j-1}\).
Sign changes between consecutive grid points \(j/1000\) from \(-3\) to \(3\) are evaluated by integer homogeneous Horner arithmetic.
They account for the entire trace degree, with no roots at grid points, so they certify the counts in the last two columns.

| Leading through central coefficients | Trace roots in \((-2,2)\) | Trace roots outside \([-2,2]\) |
| --- | ---: | ---: |
| \(1,1,0,-1,-1,-1\) | 4 | 1 |
| \(1,0,0,1,-1,0,0,-1\) | 6 | 1 |
| \(1,1,1,1,0,0,-1,-1,-1,-1\) | 8 | 1 |

The other survivor has leading half \(1,1,1,0,0,-1,0,-1,0,-1\).
The [degree-18 trace certificate](../Yin_J_G0144/trace_control.py) supplies the seven interior real traces, one nonreal conjugate pair and the strict Mahler interval for this specific row.
The [degree-bounded classification](../../../claims/Yin_C_G0901_v56.md#statement) uses the four survivors, the published extent of the primitive search, and the splitting-field test for this last row.
An [independent recomputation](../../../audits/reviews/Yin_R_G0562_v1113.md#computation) checked all 1339 rows, matched the five higher-degree minimizing polynomials to the published table and verified the survivor signatures.
