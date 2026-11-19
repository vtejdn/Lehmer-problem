---
author: Yin
---

# Reciprocal measures in degrees 86, 88 and 92 at the cutoffs for prime 503

<a id="census"></a>
## Three complete enumerations

The [driver](run.py) enumerated all monic reciprocal irreducible noncyclotomic integer candidates of the indicated degree with Mahler measure at most \(T\).
All 2,198 final polynomials have a cyclotomic divisor.
The initial counts include one sign representative of each integral first-half trace tuple after excluding power substitutions.
The first two filters retain the polynomials passing one and nine reflected traces.

| Degree and summary | \(T\) | Initial count | One reflection | Nine reflections | Final division |
| ---: | ---: | ---: | ---: | ---: | ---: |
| [86](../../../../outputs/Yin_J_G0179/versions/v15/d86/summary.json) | 1.04902 | 60,816,713 | 1,199,108 | 299,217 | 1,752 |
| [88](../../../../outputs/Yin_J_G0179/versions/v15/d88/summary.json) | 1.04116 | 8,711,399 | 428,305 | 159,988 | 446 |
| [92](../../../../outputs/Yin_J_G0179/versions/v15/d92/summary.json) | 1.02769 | 768,332 | 92,527 | 44,759 | 0 |

<a id="scope"></a>
## Necessary conditions and exact verification

Each \(T<1.06\), so the [degree-86 theorem](../../../../../claims/Yin_C_G0345_v438.md#degree) applies to every power field of a candidate.
In particular no signed power trace is a zero of any of the [auxiliaries of degree at most eight](../v7/readme.md#weights).
A nontrivial substitution preserves measure in degree at most 46 and is excluded by the same degree theorem.

The driver reuses the [v13 bounds and native Newton recursion](../v13/readme.md#bounds) at the three new exact rational cutoffs.
It constructs the certified trace bounds through index 120, verifies the signed integer ranges, and reflects the integral first-half coefficients to impose reciprocity.
After nine successful reflections it tests the endpoints, the remaining trace bounds and the quadratic cyclotomic divisors, then performs integer cyclotomic division on the final polynomials. [Enumeration and arithmetic bounds](../v13/readme.md#enumeration)

The [verifier](check_results.py) checks all 360 selected bounds by rational arithmetic at the actual cutoffs and degree, including the power inequalities for the logarithmic chord and the unweighted bound where selected.
It checks every one of the 180 disjoint first-pair slice counts by tensor contractions and inclusion and exclusion on the prime divisors of the degree.
Each final polynomial has the right degree, sign, slice, first-half trace bounds and substitution exclusions.
For its claimed cyclotomic divisor \(\Phi_m\), the verifier checks that \(\sum_{\zeta\ {\rm primitive}\ m{\rm th}} |P(\zeta)|^2=0\) by [integer Ramanujan sums](../v12/verify.py).
In each degree it also compares a complete subtree on a fixed eight-trace prefix against direct Newton recursion in unrestricted integers.
These subtrees have 112, 48 and 6 representatives, respectively, and each of the first two contains a final divisor.
The same verifier enumerates the [degree deficits and ordered degree triples](../../../../../claims/Yin_C_G0345_v455.md#sums) at the updated cutoffs.

From the repository root use Python with NumPy and the C# compiler and runtime specified for the [v13 computation](../v13/readme.md#verification).
If the v7 certificate output is absent, first regenerate it from the [retained weights](../v7/readme.md#weights).

~~~text
python -B mathematics/computations/programs/Yin_J_G0179/versions/v7/larger_boxes.py
python -B mathematics/computations/programs/Yin_J_G0179/versions/v15/run.py --workers 5
python -B mathematics/computations/programs/Yin_J_G0179/versions/v15/check_results.py
~~~
