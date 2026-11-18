---
author: Yin
---

# Rational factors of the quartic section at exponent three

<a id="census"></a>
## One nontorsion factor in every primitive direction through 720

For each \(1\le b\le720\) coprime to \(3\), the monic polynomial
\[
  H_b(X)=1+X^3-X^{12}+X^b(X^{12}+X^9-1)
\]
has exactly one nontorsion irreducible factor \(P_b\) over \(\mathbb Q\), of multiplicity one.
All 480 factors are reciprocal and have unit-circle roots.
This census tests the [quartic splitting criterion at \(a=3\)](../../../ledger/Yin_L_G0462_v205.md#quartic) on the actual factors of the parent in the [Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract).

| Inclusive \(b\) bound | Coprime directions | Empty nontorsion part | One factor | Multiple factors | Range of \(\deg P_b\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 360 | 240 | 0 | 240 | 0 | 12–370 |
| 720 | 480 | 0 | 480 | 0 | 12–730 |

In this range \(\Phi_2\) occurs exactly for odd \(b\), \(\Phi_4\) exactly for \(b\equiv0\bmod4\), and \(\Phi_{10}\) exactly for \(b\equiv3\bmod10\).
Their respective occurrence counts are \(240,120,48\), and each has multiplicity one.
There are no other cyclotomic factors in the census.
Thus the parent and the three congruences also specify the actual \(P_b\) throughout the stated finite range.

<a id="exterior"></a>
## The eight exceptions to the three-exterior-root signature

Let \(d_b=\deg P_b\).
The negative and positive columns count individual real exterior roots, and the nonreal column counts complex conjugate pairs of exterior roots.

| Admissible \(b\) | Count through 360 | Count through 720 | Negative | Positive | Nonreal pairs | Unit-circle roots of \(P_b\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| \(2,4\) | 2 | 2 | 1 | 0 | 0 | \(d_b-2=12\) |
| \(1,5,7,11,13,17\) | 6 | 6 | 0 | 0 | 1 | \(d_b-4\) |
| All other admissible \(b\) | 232 | 472 | 1 | 0 | 1 | \(d_b-6\) |

At \(b=2,4\) the polynomials \(P_b(-X)\) are Salem polynomials of degree 14.
Their positive exterior roots lie respectively in \((27/20,7/5)\) and \((5/4,13/10)\), by opposite signs at the rational endpoints and the uniqueness of the exterior root.
The underlying factors are
\[
\begin{aligned}
 P_2(X)&=X^{14}-X^{12}+X^{11}+X^3-X^2+1,\\
 P_4(X)&=X^{14}-X^{12}+X^{11}-X^9+X^7-X^5+X^3-X^2+1.
\end{aligned}
\]
The former is the whole parent, while \(H_4=(X^2+1)P_4\).
The trace Sturm variations for both are \((7,6,0,0)\) at \(-\infty,-2,2,+\infty\).
All admissible \(17<b\le720\) have the three exterior roots in the third row, so the negative real exterior root shares its rational factor with the nonreal pair.
The last case where this fails, \(b=17\), requires any all-direction large-slope threshold guaranteeing that signature to exceed \(17/3\) if the endpoint is included.
The computation leaves open whether a later nontorsion part splits.

<a id="method"></a>
## Exact arithmetic and reproduction

Run the [census program](census.py) from the repository root using Python with python-flint.
The completed run used Python 3.14.3 and python-flint 0.9.0.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0175/census.py --bound 720 --workers 4
~~~~

One worker gives the same enumeration and result.
The [replaceable output](../../outputs/Yin_J_G0175/census_b720.json) records each admissible \(b\), cyclotomic orders with multiplicities, nontorsion polynomials with descending integer coefficients and multiplicities, exact Sturm variations and root counts.
No input files are needed.

The program factors \(H_b\) over the integers by FLINT, reconstructs each parent with multiplicities, and independently constructs \(\Phi_j\) for each positive order returned by FLINT's cyclotomic test.
Monicity makes this the rational factorization.
For each nontorsion factor \(P\) the program checks reciprocity, constructs its trace polynomial \(T\) by the [J170 Chebyshev recurrence](../Yin_J_G0170/readme.md#method), and recovers every coefficient of \(P(X)=X^{\deg T}T(X+X^{-1})\) by homogeneous Horner evaluation.
It forms the negative Euclidean remainders over \(\mathbb Q\), clearing positive denominators and dividing by positive content at every step.
Sturm variations at the four ordered cutoffs count real trace roots below \(-2\), inside \((-2,2)\), and above \(2\).
The code checks squarefreeness, excludes roots at the cutoffs, and checks the parity of the number of nonreal trace roots.
A trace in \((-2,2)\) lifts to two circle roots, a real trace outside that interval gives one exterior root of the same sign, and each conjugate pair of nonreal traces gives one conjugate pair of exterior roots.
Thus the finite classification uses exact arithmetic throughout.
For larger bounds the same program requires even-degree reciprocal nontorsion factors, and raises an error if it encounters a factor outside that case.

As a separate arithmetic check, all 17 admissible \(b\le25\) were also factored directly by SymPy 1.14.0 without the FLINT backend.
The nontorsion coefficients and multiplicities agreed in every case.
The [J170 verifier](../Yin_J_G0170/verify_traces.py) recovered the trace by subtracting centered binomial lifts and recomputed the same variations with integer pseudo-remainders.
Exact rational isolation using the [J170 interval routine](../Yin_J_G0170/census.py) also agreed on all four signature counts for these 17 cases, which include all eight exceptional signatures.
The [independent census review](../../../audits/reviews/Yin_R_G0562_v457.md#finding) certified every trace irreducibility by modular factor degrees and checked all 480 signatures with integer Sturm chains.
