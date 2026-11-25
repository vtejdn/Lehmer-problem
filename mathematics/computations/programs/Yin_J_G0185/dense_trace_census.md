# Trace-pole census for every height through trace degree forty

<a id="census"></a>
## Scope and exact computation

Use the [first nonunit trace pole](../../../claims/Yin_C_G0345_v891.md#return) with \(q,D\ge2\), where \(D\) is the trace degree, the reciprocal degree is \(2D\) and the height parameter is \(q\).
For \(2\le D\le40\) there are **no** integral realizations for any \(q\) or separating grid.
The [all-grid moment search](reflected_trace_search.md#census) was run by the [all-height driver](dense_trace_census.py) on each of the \(39\cdot106=4134\) pairs \(2\le D\le40,\ 2\le q\le107\).
For a true solution the Salem root \(T\) has \(0<\log T<1/q\) and degree \(2D\), so [Voutier's Corollary 2](../../../audits/literature/Vou96/Yin_U001.md#height) gives \(q<(\log(6D))^3/2<108\).
The driver certifies \(\exp(6)>240\) by the first nine terms of its exponential series.

The exact integer moment budget excluded 3687 pairs before a terminal test.
The largest moment used for such an exclusion was 38.
The other 447 pairs reached a terminal search, with no coefficient vector satisfying the exact pole and squarefree root configuration.
Every degree had a conclusive status.
Tests with a shorter depth were retried at the next specified depth wherever a prefix survived.
The previous [small-measure catalogue checks](pole_catalogue.md#pole-norms) use a tabulated list and different degree and measure coverage.
This run uses the [shared discriminant budget](../../../claims/Yin_C_G0345_v896.md#statement) on all possible real grids.
The [polynomial-time enumeration using the graph-coordinate exponents](../../../claims/Yin_C_G0901_v177.md#census) is a separate algorithm.

At height four the [integer moment routine](free_trace_moments.py) additionally excluded all 48 trace degrees from 23 through 70, and at height seven it excluded all 198 from 23 through 220.
In both runs all degrees were rejected by the eighteenth moment or earlier, with no unfinished prefix.
The portion through degree 40 overlaps the all-height run.

To reproduce with Python and SymPy, from this directory run:

```text
python -B dense_trace_census.py
python -B free_trace_moments.py 4 23 70 --depth 18
python -B free_trace_moments.py 7 23 220 --depth 18
```
