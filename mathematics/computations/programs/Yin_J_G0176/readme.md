---
author: Yin
---

# False modular candidates for an odd trace factor on square-offset quartic sections

<a id="sample"></a>
## Sixteen rationally irreducible cores

For each \(a=5,7,9,11\), take the first four positive odd integers \(c\) coprime to \(a\) with \(c^2\ge a^3\), and put \(b=6a+c^2\), \(r=b/a\).
Write the monic parent as
\[
  1+X^a-X^{4a}+X^b(X^{4a}+X^{3a}-1)
       = C(X)X^n H(X+X^{-1})
\]
with \(C\) the full cyclotomic divisor.
All 16 polynomials \(X^nH(X+X^{-1})\) are irreducible over \(\mathbb Q\), with degrees ranging from 218 to 1958.
The [square-offset parity criterion](../../../claims/Yin_C_G0345_v400.md#parity) motivates testing for a rational divisor of \(H\) of odd degree \(j<r\).
Modulo three, 13 of the 16 sections have a monic divisor of such a degree.
Across those sections 122 different modular divisor polynomials occupy 103 pairs of a section and a candidate degree.
All 122 are false candidates for rational divisibility.

In the table the two counting columns use only the prime three and the strict inequality \(aj<b\).
The last two columns give the final prime of the prefix of \(3,2,5,7,11\) needed to exclude every such odd degree or every proper positive degree, respectively.

| \(a\) | \(c\) | \(b\) | Trace degree \(n\) | Candidate degrees | Candidate divisors | Odd exclusion | Full exclusion |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 13 | 199 | 109 | 4 | 4 | 5 | 5 |
| 5 | 17 | 319 | 169 | 4 | 4 | 2 | 2 |
| 5 | 19 | 391 | 205 | 7 | 10 | 7 | 11 |
| 5 | 21 | 471 | 245 | 11 | 11 | 2 | 5 |
| 7 | 19 | 403 | 215 | 7 | 9 | 2 | 2 |
| 7 | 23 | 571 | 299 | 22 | 32 | 5 | 7 |
| 7 | 25 | 667 | 345 | 4 | 4 | 2 | 2 |
| 7 | 27 | 771 | 399 | 2 | 2 | 2 | 5 |
| 9 | 29 | 895 | 465 | 0 | 0 | 3 | 7 |
| 9 | 31 | 1015 | 525 | 0 | 0 | 3 | 2 |
| 9 | 35 | 1279 | 655 | 2 | 2 | 2 | 2 |
| 9 | 37 | 1423 | 729 | 2 | 2 | 2 | 5 |
| 11 | 37 | 1435 | 739 | 1 | 1 | 2 | 2 |
| 11 | 39 | 1587 | 815 | 21 | 25 | 2 | 7 |
| 11 | 41 | 1747 | 895 | 0 | 0 | 3 | 5 |
| 11 | 43 | 1915 | 979 | 16 | 16 | 5 | 7 |

<a id="certificate"></a>
## Degree certificates and the negative exterior root

All rational monic trace factors have integer coefficients and preserve their degree at each prime.
If the modular factor degrees and multiplicities are \((v_i,e_i)\), the possible degrees are sums of \(s_i v_i\) with \(0\le s_i\le e_i\).
The number of monic modular divisors of a given degree is its coefficient in \(\prod_i(1+Z^{v_i}+\cdots+Z^{e_iv_i})\).
Intersecting the possible proper degree sets of the indicated prime reductions gives the empty set for every row, proving all 16 traces irreducible.

For \((a,c,b)=(5,13,199)\), the trace factor degrees listed with multiplicity are \(6,9,12,82\) modulo three, \(1,1,7,11,89\) modulo two, and \(16,31,62\) modulo five.
Modulo three the small odd degrees are \(9,15,21,27\).
After intersecting the first two primes the proper degrees are \(9,12,18,91,97,100\), and none occurs modulo five.
A direct integer factorization of the degree-218 core also returns that core with multiplicity one.

In every row \(C=X+1\), except at \((7,25)\) and \((9,35)\), where \(C=(X+1)\Phi_{10}\), by division and the [complete torsion list](../../../ledger/Yin_L_G0462_v212.md#orders).
As \(b>6a\), the [quartic phase count](../../../ledger/Yin_L_G0462_v210.md#phase) gives \(b+2a>\deg C\) simple roots on the unit circle and \(a\) exterior roots.
The core therefore has a circle root away from \(1,-1\), whose trace \(y\) lies in \((-2,2)\).
At this real embedding \(y^2-4<0\), so the quadratic lift of the irreducible trace has twice its degree over \(\mathbb Q\).
This proves the stated rational core factorizations.
The [real root count](../../../ledger/Yin_L_G0462_v210.md#real) places the unique negative exterior root in that core together with its other \(a-1\) exterior conjugates, excluding a Salem number after sign change in each row.
The equivalence between a short odd trace factor and a Salem root has an [unspecified sufficiently large slope](../../../claims/Yin_C_G0345_v400.md#statement).
The conclusions for these finite inputs follow from their full irreducibility certificates and exact root counts.
The existence of a split in other square-offset directions stays open.

<a id="method"></a>
## Reproduction

Run the [diagnostic program](diagnostic.py) from the repository root with Python and python-flint.
The completed run used Python 3.14.3 and python-flint 0.9.0.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0176/diagnostic.py
~~~~

The program enumerates the fixed sample, divides out the cyclotomic polynomials, checks reciprocity, and computes the integral trace using \(C_0=2,\ C_1=Y,\ C_{j+1}=YC_j-C_{j-1}\).
It checks \(H(2)=1\), \(H(-2)=c^2/5^{\mathbf1_{\Phi_{10}\mid C}}\), and reconstructs each modular trace from its irreducible factors before intersecting degrees.
It prints all 16 rows with the removed cyclotomic orders and full core degrees.
An [independent reconstruction](../../../audits/reviews/Yin_R_G0562_v471.md#finding) verified every row and the finite root exclusions.

<a id="single-prime"></a>
## One good prime excludes all short odd degrees in each direction

For each of the same 16 traces, test primes \(2\le p\le199\) in increasing order and skip \(p\) when \(\gcd(\bar H,\bar H')\ne1\), equivalently \(p\mid\operatorname{disc}H\).
At a good prime let \(v_p\) be the smallest odd degree of a monic irreducible factor of \(\bar H\).
Such a factor exists since \(n\) is odd in every row.
Every odd-degree divisor contains an odd-degree irreducible factor, and that factor is itself a divisor.
Thus \(av_p\ge b\) excludes every odd rational trace-divisor degree \(j<b/a\) using \(p\) alone.

| \(a\) | \(c\) | \(b\) | Least good \(p\) with \(av_p\ge b\) | \(v_p\) |
| ---: | ---: | ---: | ---: | ---: |
| 5 | 13 | 199 | 7 | 93 |
| 5 | 17 | 319 | 7 | 89 |
| 5 | 19 | 391 | 29 | 119 |
| 5 | 21 | 471 | 2 | 197 |
| 7 | 19 | 403 | 2 | 171 |
| 7 | 23 | 571 | 157 | 249 |
| 7 | 25 | 667 | 11 | 279 |
| 7 | 27 | 771 | 2 | 237 |
| 9 | 29 | 895 | 3 | 161 |
| 9 | 31 | 1015 | 2 | 273 |
| 9 | 35 | 1279 | 2 | 185 |
| 9 | 37 | 1423 | 53 | 729 |
| 11 | 37 | 1435 | 5 | 451 |
| 11 | 39 | 1587 | 2 | 781 |
| 11 | 41 | 1747 | 3 | 463 |
| 11 | 43 | 1915 | 5 | 195 |

One good prime suffices in all 16 directions, including all 13 in which the original reduction modulo three permitted a short odd degree.
Overall, six directions already work at two.
At \((a,c)=(7,23)\), all 36 primes below 157 are good and all permit a short odd degree.
The conclusion about the negative root in each individual sample still follows from the [full rational irreducibility certificates and exact root counts](#certificate).

Run the [single-prime diagnostic](single_prime.py) from the repository root with the same Python and python-flint versions as above.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0176/single_prime.py
~~~~

For each direction the program prints all skipped primes, every smaller good prime with its minimum odd degree, and the first witness with its minimum.
It reconstructs each factored good reduction and checks the minimum against all attainable odd subset degrees.
A separate Frobenius calculation verified all 92 pairs of a direction and a prime up to its first witness, including seven bad reductions.
For this check one successively removes the degree-\(j\) block \(\gcd(\bar H_{\rm rem},Y^{p^j}-Y)\) from the squarefree remainder in increasing \(j\), stopping at the first odd \(j\) with a nonconstant block or when the remaining polynomial has degree less than \(2j\) and is therefore irreducible.
An [independent resultant and Frobenius check](../../../audits/reviews/Yin_R_G0562_v475.md#finding) reproduced the 16 minima and every smaller good-prime failure.
