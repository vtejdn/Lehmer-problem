---
author: Yin
---

# Unit-circle inverse pairs in the complete small-measure list through degree 44

<a id="circle"></a>
## The catalogue and the rational check

The [native table](../../../literature/pdf/Mos26/AllSmallMeasures_200.txt) and its [coverage statement](../../../audits/literature/Mos26/readme.md#complete-small-cores) supply all primitive irreducible noncyclotomic polynomials of multiplicative measure below \(1.3\) through degree 44, up to \(X\mapsto-X\).
Run the [verifier](angular_cores.py) from the checkout root with standard Python.

~~~text
python -B mathematics/computations/programs/Yin_J_G0189/angular_cores.py
~~~

The verifier consumes the degree and coefficient vector from each of the 944 qualifying rows.
For each reciprocal polynomial \(P(X)=X^nQ(X+X^{-1})\) it counts the roots of \(Q\) in \((-2,2)\) by the [exact trace transformation and rational Sturm calculation](../Yin_J_G0188/readme.md#signatures).
Each such root contributes exactly one inverse pair on the unit circle.
The polynomial has no endpoint trace and the Sturm computation checks simplicity.
The table's rounded measure and its exterior-count column do not enter the signature calculation.

The minimum count was three, at source lines 152, 158 and 159, of degrees 8, 10 and 10 respectively.
For counts \(3,4,\ldots,21\) of unit-circle inverse pairs, the corresponding row counts were
\[
  3,\ 12,\ 6,\ 32,\ 16,\ 78,\ 33,\ 100,\ 62,\ 158,\
      54,\ 143,\ 54,\ 108,\ 28,\ 49,\ 5,\ 2,\ 1 .
\]
The exhaustion uses the source's stated completeness, while the counts use only its exact coefficients.
The [argument-rank reduction](../../../claims/Yin_C_G0901_v74.md#catalogue) applies this computation to the explicitly bounded compressed degree.
