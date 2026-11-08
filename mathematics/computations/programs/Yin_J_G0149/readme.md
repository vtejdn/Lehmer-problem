---
author: Yin
---

# Exact cyclotomic completions at prescribed odd-grid cuts

<a id="fixed-cut-census"></a>
## The complete target through conductor 43

Put \(p=2n+1\), \(D=p+1\), and use all \(n\) trace nodes \(2\cos(2\pi j/p)\), including nonprimitive nodes at composite conductors.
For the [strict odd-grid chamber](../../../ledger/Yin_L_G0464_v5.md#odd-grid-product), prescribe the number of negative residues in increasing pole order as \(k=\lfloor p/\log p\rfloor\).
The logarithm is natural.
We include every monic reciprocal integer polynomial \(P=z^{n+1}Q(z+z^{-1})\) of degree \(D\), with unrestricted coefficient height and resultant.
In the strict shell \(1<M(P)<13/10\) the following are all the target hits at odd \(13\le p\le43\).

| \(p\) | \(k\) | Multiplicative measure, rounded | \(\lvert\mathrm{Res}(B,Q)\rvert\) | Shift \(a\) |
| ---: | ---: | ---: | ---: | ---: |
| 13 | 5 | 1.25509352 | 1 | 1 |
| 15 | 5 | 1.27281837 | 2 | 1 |

Every odd conductor from 17 through 43 gives zero target hits below \(13/10\).
For all 16 conductors the target shell below \(6/5\) is empty.
Requiring just the eventual shift \(a=2x,\ x\in\{-2,-1,0,1,2\}\) in addition to the prescribed cut already gives zero below \(13/10\) throughout the tested range.
The application of the published irreducible classification is specified [below](#core-coverage).

| \(p\) | \(k\) | Chamber at any cut, \(1<M<6/5\) | Chamber at any cut, \(1<M<13/10\) |
| ---: | ---: | ---: | ---: |
| 13 | 5 | 0 | 6 |
| 15 | 5 | 0 | 3 |
| 17 | 6 | 0 | 6 |
| 19 | 6 | 1 | 6 |
| 21 | 6 | 0 | 2 |
| 23 | 7 | 1 | 9 |
| 25 | 7 | 1 | 3 |
| 27 | 8 | 0 | 5 |
| 29 | 8 | 1 | 2 |
| 31 | 9 | 0 | 2 |
| 33 | 9 | 0 | 1 |
| 35 | 9 | 0 | 0 |
| 37 | 10 | 0 | 1 |
| 39 | 10 | 0 | 0 |
| 41 | 11 | 0 | 0 |
| 43 | 11 | 0 | 0 |

The previously independent [all-height Newton enumeration](../Yin_J_G0147/readme.md#whole-shell) gives the same \(6/5\) chamber counts for 13, 17 and 19.

<a id="nonunit-atom"></a>
## A binary nonunit example with two exterior roots

At \(p=15\) the unique input is
\[
               P(z)=1+\sum_{j=3}^{13}z^j+z^{16}.
\]
It factors as \(\Phi_{12}\) times the reciprocal degree-12 database core with leading-to-central coefficients \((1,0,1,1,1,2,1)\).
The trace denominator has seven poles.
Direct checks give five negative residues followed by two positive residues, \(P(-1)=1\), absolute resultant two, and \(1.272<M(P)<1.274\).
The trace polynomial has exactly six real roots, all in \((-2,2)\), and one nonreal conjugate pair.
The pair supplies both exterior roots of the original lift.
When the eight free coefficients of a degree-16 monic reciprocal input are independent fair bits, the joint probability of this prescribed chamber, nonunit resultant and \(1<M<13/10\) is exactly \(2^{-8}\).
The larger-conductor census above concerns a fixed positive radius.

<a id="core-coverage"></a>
## Reconstructing every input in the shell

Mossinghoff, Rhin and Wu computed the primitive irreducible polynomials of measure below 1.3 through degree 44.
The [published paper](https://doi.org/10.1080/10586458.2008.10128872), the [author's pinned data and normalization](https://github.com/mossinghoff/Mahler-Measure-Database/blob/7e3798516710370a758e16eb5de6bccbee98bb6a/AllSmallMeasures_200.txt) and the [source-table inspection](../../../audits/literature/Mos26/readme.md#complete-small-cores) give the external scope.
We use that published completeness result.
The original exhaustive search establishing completeness was not independently reproduced in this computation.

The source table has 944 representative rows of degree at most 44 and retains only one of \(F(z),F(-z)\).
The program uses the integer coefficient vectors to verify \(M(F)>23/20\) for every row, so two positive irreducible factors, including repetitions, would give \(M(P)>(23/20)^2>13/10\).
Mahler measure is multiplicative and is preserved under \(z\mapsto\pm z^m\).
For an irreducible factor with a common divisor \(m\) of its nonconstant exponents, writing it as \(F(z^m)\) gives irreducible \(F\).
Taking the maximal such \(m\) places \(F\) within the normalized primitive list, up to sign substitution.
Thus the algorithm forms both signs and every substitution fitting the degree and retains irreducible compositions.
Kronecker's theorem gives a cyclotomic product for the remaining factor.
No circular-unit or bounded-height assumption enters this reconstruction.

The left endpoint is exactly \(P(-1)>0\).
Each allowed cyclotomic factor has positive value at \(-1\), while \(\Phi_2\) gives zero there.
The multiplicity of \(1\) is even in a reciprocal even-degree trace lift, so the real linear factor enters as \((z-1)^2\).
For orders \(m\ge3\), enumerate all factors with \(\varphi(m)\) no greater than the unfilled degree, using \(m\le2\varphi(m)^2\) as in [J147](../Yin_J_G0147/readme.md#measure-and-chamber).
Generate their multisets in one fixed order with repetition.
Factors sharing a grid pole cannot satisfy strict signs and are discarded.

For each factor the program computes its trace polynomial and a binary mask of its negative values at the increasing nodes.
It isolates the nodes in rational intervals, encloses those intervals on a common integer grid and uses interval Horner arithmetic, aborting on an undecided sign.
Masks add by exclusive-or under multiplication, and the signs of \(B'\) alternate from the largest node, where \(B'>0\).
For each admissible core and cut the program records the required mask and degree of the completion.
It counts a multiset exactly when both match and multiplies the absolute integer trace resultants.
The angular cut index is certified with rational upper and lower bounds on \(\log p=2\operatorname{atanh}((p-1)/(p+1))\).
Each target hit is reconstructed as a polynomial and its endpoint, residue mask, resultant and strict \(13/10\) comparison are checked again.
The \(6/5\) subcounts and the lower bound \(23/20\) use exact Graeffe or real-endpoint inequalities.

<a id="replay"></a>
## Reproduction

Run from the repository root with Python and SymPy, using the author's [native table](../../../literature/pdf/Mos26/AllSmallMeasures_200.txt) or a downloaded copy of the pinned file above.

~~~text
python -B mathematics/computations/programs/Yin_J_G0149/completions.py mathematics/literature/pdf/Mos26/AllSmallMeasures_200.txt --show
~~~

The [program](completions.py) prints \(p,k\), the two all-cut counts, the two target counts, the nonunit target counts at \(13/10\) and \(6/5\), the target count having a profile shift, and the first target's source data.
The optional witness output records the source measure label, sign and substitution power, cyclotomic orders, absolute resultant and shift.
