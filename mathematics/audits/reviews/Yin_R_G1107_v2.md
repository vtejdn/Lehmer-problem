---
author: Yin
---

# Review of the prescribed-cut finite censuses

<a id="cut-census-review"></a>
## Published cores, cyclotomic completions and circular-unit boxes

At 2026-11-08T03:46 UTC a separately assigned agent for Yin independently inspected the fixed J148 and J149 descriptions, their programs and the imported arithmetic used in the censuses.
The reviewer did not develop either computation and received no proof-generation dialogue or prior review verdict for these inputs.

### All coefficient heights through conductor 43

Mossinghoff, Rhin and Wu classify primitive irreducible noncyclotomic integer polynomials of measure below \(13/10\) through degree 44, where primitive excludes a substitution \(X\mapsto X^m\) with \(m>1\) ([published paper](https://doi.org/10.1080/10586458.2008.10128872)).
The local [coefficient table](../../literature/pdf/Mos26/AllSmallMeasures_200.txt) matched the blob at the [author's pinned revision](https://github.com/mossinghoff/Mahler-Measure-Database/blob/7e3798516710370a758e16eb5de6bccbee98bb6a/AllSmallMeasures_200.txt).
I counted the 944 primitive representatives and checked their exponent gcds, reciprocal reconstruction and sign convention.
Completeness of the source table rests on the published search, whose exhaustive computations were outside this review.

Every irreducible divisor of measure greater than one descends by its maximal exponent gcd to an irreducible primitive core with the same measure.
The strict \(23/20\) lower tests on these cores and \((23/20)^2>13/10\) leave precisely one such divisor with multiplicity one.
Irreducible signed compositions with positive value at \(-1\) supply 1,725 distinct possible divisors through degree 44.
All other factors are cyclotomic by Kronecker, with \(\Phi_2\) excluded by the endpoint and \(\Phi_1\) occurring to even order by reciprocity at \(z=1\).
The bound \(m\le2\varphi(m)^2\) covers the remaining orders, and unique factorization justifies counting multiplicity vectors.
I checked the fixed program's trace recurrence, certified node signs, derivative orientation, resultant multiplication, rational logarithm tail and strict Graeffe tests.

I reran the fixed program on all 16 odd conductors and counted the completions separately by accumulating multiplicities in increasing degree for each allowed cyclotomic factor.
For this second count I bracketed the cosine nodes on a rational mesh and certified the brackets by opposite signs of \(B\) on \(n\) disjoint intervals.
Summing the reciprocal coefficients directly against the bracketed cosine values certified the signs without using the program's interval Horner masks.
The independent counts reproduced every all-cut row and both target counts, using the source measure labels to partition the second count at \(6/5\).
The fixed program's integer comparisons certify the strict partition.
Only \(p=13,15\) contribute at the prescribed cut, each with shift one, respective absolute resultants one and two, and \(P(-1)=1\).
Rational real and complex root isolation independently gave \(1.2550935167<M(P_{13})<1.2550935168\) and \(1.2728183650<M(P_{15})<1.2728183653\).
The latter trace has six roots in \((-2,2)\) and one nonreal conjugate pair, hence exactly two exterior roots of the lift.
Its displayed polynomial has binary coefficients, so uniqueness among all inputs gives mass \(2^{-8}\) under the stated independent eight-bit law.

### Prime circular-unit boxes through conductor 67

For J148 the sine ratio gives the stated column bit \(\lfloor2jl/p\rfloor\bmod2\), and the positive multiplier \(2-b_l\) preserves it with absolute norm \(B(2)=p\).
I checked elimination including the explicit parity obstruction at \(29\), enumeration of both exponents for each odd parity, cyclic multiplication and inversion, and subtraction of the common coefficient at the two extreme conjugate positions.
The resulting Laurent lift yields the endpoint by alternating evaluation, and expansion of the stated limiting profile gives the quadratic and cubic coefficient tests.
For a reciprocal pair with outer radius \(\rho\), its absolute contribution to Newton sum \(h\) is at most \(\rho^h+\rho^{-h}\).
Concentrating all positive log-radii in one pair maximizes this bound by convexity and gives the program's Newton cutoff.
Coefficient bounds and the Euclidean norm after Graeffe squaring certify the remaining strict measure comparisons.
All 11 primes were replayed, including the paired \(p=43\) endpoint and measure windows.
A separate traversal of all \(3^{10}\) exponent vectors and both signs at \(p=23\), with direct convolution modulo \(z^{23}-1\), reproduced the 128 sign words and 75 unit and 10 norm-23 chamber atoms.
Over the full prescribed box the program reproduced 21,478 unit and 11,464 norm-\(p\) chamber atoms, with measures respectively above \(29/20\) and \(12/5\).
None match the cubic prefix.
The J148 bounds apply to its exponent and shift boxes, and the unrestricted J149 exclusion applies at its stated degrees and prescribed cut.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finite censuses](#cut-census-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finite censuses](#cut-census-review) | [J149 shell](../../computations/programs/Yin_J_G0149/readme.md#fixed-cut-census) | All 16 conductors, both strict radii, target shifts and all-cut counts. |
| [Finite censuses](#cut-census-review) | [J149 nonunit](../../computations/programs/Yin_J_G0149/readme.md#nonunit-atom) | Unique binary witness, resultant, full measure, exterior roots and probability. |
| [Finite censuses](#cut-census-review) | [J149 core coverage](../../computations/programs/Yin_J_G0149/readme.md#core-coverage) | Published completeness at statement level, coefficient-table normalization, substitutions and cyclotomic completion. |
| [Finite censuses](#cut-census-review) | [J149 program](../../computations/programs/Yin_J_G0149/completions.py) | Whole fixed program, imported arithmetic used and full replay. |
| [Finite censuses](#cut-census-review) | [J148 families](../../computations/programs/Yin_J_G0148/readme.md#prescribed-cut) | Sign orientations, multiplier, resultant and parameter ranges. |
| [Finite censuses](#cut-census-review) | [J148 counts](../../computations/programs/Yin_J_G0148/readme.md#finite-box) | Complete prime table, endpoint, measure and profile tests. |
| [Finite censuses](#cut-census-review) | [J148 witnesses](../../computations/programs/Yin_J_G0148/readme.md#paired-example) | Paired unit and nonunit at the same cut. |
| [Finite censuses](#cut-census-review) | [J148 program](../../computations/programs/Yin_J_G0148/cuts.py) | Whole fixed program, full replay and direct convolution check at 23. |
