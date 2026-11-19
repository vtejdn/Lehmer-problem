---
author: Yin
---

# Reciprocal degrees 56, 58, 60 and 62 at Mahler measure 1.091

<a id="census"></a>
## Complete classifications

There is no monic irreducible noncyclotomic reciprocal polynomial \(P\in\mathbb Z[X]\) of any of the four degrees \(D=56,58,60,62\) with \(M(P)\le T=1091/1000\).
The cutoff is the same as in the [degree-64](../v8/readme.md#census) and [degree-66](../v9/readme.md#census) computations.
Write \(h=D/2\).

| Applied condition | Degree 56 | Degree 58 | Degree 60 | Degree 62 |
| --- | ---: | ---: | ---: | ---: |
| First-half box, after power substitutions and sign symmetry | 256,394,919 | 642,515,687 | 1,619,542,805 | 10,687,611,707 |
| First reflected sum \(s_{h+1}\) | 21,258,075 | 42,383,117 | 109,211,379 | 589,441,505 |
| All reflected sums through \(s_{h+9}\) | 3,065,253 | 5,198,191 | 11,163,362 | 39,060,034 |
| Nonzero at \(1\) and \(-1\) | 1,315,339 | 1,991,501 | 4,330,238 | 13,512,959 |
| All reflected sums through \(s_{120}\) | 362,745 | 587,877 | 1,294,912 | 3,818,545 |
| Indivisible by \(\Phi_3,\Phi_4,\Phi_6\) | 100,307 | 149,835 | 344,340 | 761,131 |
| Also pass modular Graeffe comparisons | 2,869 | 3,895 | 5,343 | 10,761 |
| Also pass exact cyclotomic division | 0 | 0 | 0 | 0 |

The generated summaries give every final cyclotomic classification and the direct prefix checks in [degree 56](../../../../outputs/Yin_J_G0179/versions/v10/d56/summary.json), [degree 58](../../../../outputs/Yin_J_G0179/versions/v10/d58/summary.json), [degree 60](../../../../outputs/Yin_J_G0179/versions/v10/d60/summary.json) and [degree 62](../../../../outputs/Yin_J_G0179/versions/v10/d62/summary.json).

<a id="boxes"></a>
## Certified Newton boxes at the common cutoff

Use the [34 auxiliaries and degree-64 weight rows](../v7/readme.md#weights) at the same \(T\).
For each index \(k\le h\), those weights give certified upper bounds \(U_{0,k}\) and \(U_{k,k}\) on the unit and outer ellipses.
The [ellipse inequality](../../readme.md#ellipse) bounds \(\lvert s_k\rvert\) by \((h-1)U_{0,k}+U_{k,k}\).
The two maxima depend on the radii and the chosen row, so the degree-64 certificates certify these same maxima at each smaller degree.
The program takes the floor after multiplying the unit-radius bound by the actual \(h-1\).
The nonvanishing hypothesis holds in every case.
Indeed, a vanishing auxiliary on either signed power trace would force the power field to have degree at most sixteen, whereas [power-field descent](../../../../../ledger/Yin_L_G0462_v270.md#descent) and the [published degree theorem](../../../../../audits/literature/MRW08/Yin_U001.md#degree) give degree at least 56 for the stated small positive measure.
The [computed boxes](../../../../outputs/Yin_J_G0179/versions/v10/boxes.json) give every resulting integer bound and the initial tensor counts.

<a id="enumeration"></a>
## Suffixes, symmetries and arithmetic

The [native program](Reciprocal.cs) extends the [two-list Newton calculation](../v8/readme.md#suffix) with a common fixed prefix through 16.
The low block consists of \(17,\ldots,24\) and the high block of \(25,\ldots,h\).
All the upper sums have proper divisors at most 16 and one or two independent choices each.
In the nine reflected tests \(h+1\le k\le h+9\), the logarithm needs only its linear and quadratic terms, since the cubic term starts at degree 51 while \(h+9\le40\).
For \(U_j=V_j/P_0=X^j+O(X^{h+1})\), replacing \(U_i U_j\) by \(X^{i+j}\) in this range is exact, and \(17+25=42>h+9\) places every quadratic contribution in the low block.
The endpoint calculation doubles all terms strictly below the center before adding the central coefficient once, to the even or the odd part according to \(h\).

A polynomial of form \(S(X^q)\), \(q>1\), has the same Mahler measure as \(S\), whose degree is at most 31 here, below the published threshold.
For enumeration it suffices to test \(q\) running over prime divisors of \(D\).
The condition \(P\in\mathbb Z[X^q]\) is already decided by the fixed prefix, as in the [degree-66 argument](../v9/readme.md#suffix), since every upper bound \(B_j\) at \(j>16\) is strictly less than \(j\).
The odd prime divisors at degrees \(56,58,60,62\) are respectively \(7\), \(29\), \(3,5\), and \(31\).
The prime 2 and sign symmetry are handled by requiring a positive first nonzero odd-indexed sum.

The reflected caps are \(\lfloor D-2+T^k+T^{-k}\rfloor\), and the Graeffe coefficient caps use \(\binom{D}{i}T^{2^g}\).
For the [coefficient and Newton arithmetic bounds](../v8/readme.md#finishing), the following maxima justify signed integer divisions through \(h\), centered 32-bit residues at the first nine reflections and direct signed 64-bit Newton sums thereafter.
At a reflected stage the bound assumes precisely that all earlier trace comparisons passed.

| \(D\) | \(\sum_{i=0}^h C_i\) | First-half numerator | First nine reflected numerators | Remaining numerators through 120 |
| ---: | ---: | ---: | ---: | ---: |
| 56 | 574,250 | 13,207,750 | 9,663,652 | 3,608,741,989 |
| 58 | 756,022 | 18,900,550 | 12,895,985 | 4,388,472,657 |
| 60 | 931,229 | 24,211,954 | 16,110,905 | 5,006,526,607 |
| 62 | 1,883,987 | 52,751,636 | 33,721,058 | 9,256,235,975 |

<a id="reproduction"></a>
## Reproduction and checks

From the repository root use Python and NumPy with the .NET Framework C# compiler on Windows or Mono on Unix.
The first command rebuilds the [ellipse certificates](../v7/readme.md#weights) from their tracked rational weights.

~~~text
python -B mathematics/computations/programs/Yin_J_G0179/versions/v7/larger_boxes.py
python -B mathematics/computations/programs/Yin_J_G0179/versions/v10/sieve.py --workers 6
python -B mathematics/computations/programs/Yin_J_G0179/versions/v10/verify.py
~~~

The [driver](sieve.py) computes the four boxes and saves each disjoint \((s_1,s_2)\) slice, including witnesses for any final integer Graeffe exclusion or polynomial left unclassified.
The [verification program](verify.py) applies the congruence tensors and inclusion and exclusion over the prime divisors of each degree independently of the native Newton recursion.
The pair counts agree in all 33 slices of each of the first three degrees and all 39 slices of degree 62.
At each degree it also enumerates complete suffixes on specified sixteen-sum prefixes by unrestricted-precision Newton recurrences, checking power substitutions on the actual coefficients and comparing the counts throughout the sieve.
