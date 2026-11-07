---
author: Yin
---

# Exact degree and endpoint filters in the odd-prime square family

The [factor reconstruction strategy](../../../ledger/Yin_L_G0462_v1.md#factor-reconstruction) uses the [indivisible binary block theorem](../../../claims/Yin_C_G0871_v1.md#statement) and the uniform height estimate in [L458 v4](../../../ledger/Yin_L_G0458_v4.md#prime-square-root-height-upper).
Run the programs from this directory using standard Python 3.10 or later with assertions enabled.

- Run [degree_screen.py](degree_screen.py) with the option --max-prime 13367 to reproduce the prime and degree list.
- Run [small_lift.py](small_lift.py) with its defaults to check the full modulus 65536 product and endpoint counts at 8191.
- The options --prime 7 --bits 16 on the same program check the small Mersenne control, including the independently computed reciprocal-block lift.

The degree screen first checks \(H_3\bmod\Phi_3=2\) and the two lifted mod-four cubic blocks at \(p=7\).
It uses the sufficient bound \(270e<7(2p-10)\) and the exact block sizes from C871.
It eliminates the old degrees 88 and 90 at \(p=2113\).
Through 13367 the two surviving primes are 8191 with degrees \(208,210,416,418\) and 13367 with degrees \(656,658\).
Both primes have undergone complete endpoint tests at the listed degrees.

For \(p=8191\) the binary program enumerates the irreducible polynomials of degree 13, which at this Mersenne prime correspond exactly to the primitive Frobenius orbits.
It lifts one multiplicity-eight block per reciprocal pair, constructs the monic reciprocal partner, and lifts the degree-two endpoint block.
The final endpoint tests count each unordered choice of one or two pairs, with and without the endpoint block.
They require the two original evaluations to agree with the positive divisor values \(1,1\) or \(2,2\).
Both the initial block assignment and these exact endpoint conditions are required for the finite exclusion.

| Modulus | Degree 208 | Degree 210 | Degree 416 | Degree 418 |
| ---: | ---: | ---: | ---: | ---: |
| 16 | 315 | 315 | 49455 | 49455 |
| 256 | 5 | 8 | 402 | 1542 |
| 1024 | 0 | 0 | 26 | 98 |
| 8192 | 0 | 0 | 1 | 2 |
| 16384 | 0 | 0 | 0 | 1 |
| 32768 | 0 | 0 | 0 | 0 |

The complete product of the 630 lifted primitive blocks and the endpoint block agrees modulo 65536 with all 65523 coefficients of \(H_{8191}\) generated directly from \((A^2+B^2)/2\).
The factor-search developer executed both methods and the coordinating agent reran the full test.
The four candidate degrees are excluded for this polynomial.
Small measures at other degrees, global irreducibility and an unbounded prime family remain open to this computation.

<a id="prime-13367"></a>
## The two factor degrees at 13367

Run [small_lift.py](small_lift.py) with the options --prime 13367 --bits 12.
The program constructs the field of order \(2^{41}\) with defining polynomial \(x^{41}+x^3+1\), checks its irreducibility by Frobenius and exclusion of linear factors, and checks that the projected nonidentity field element has order 13367.
All 326 primitive Frobenius orbits give distinct monic binary polynomials of degree 41.
Inversion partitions them into 163 pairs.
For degree 656 use one pair with its full multiplicities and for 658 include the unique endpoint block.
The two required endpoint values are both one for the former and both two for the latter.

| Modulus | Degree 656 | Degree 658 |
| ---: | ---: | ---: |
| 16 | 163 | 163 |
| 32 | 82 | 163 |
| 64 | 25 | 81 |
| 128 | 9 | 16 |
| 256 | 4 | 3 |
| 512 | 0 | 0 |
| 4096 | 0 | 0 |

The full product of the 326 local factors and the degree-two endpoint factor agrees modulo 4096 with every one of the 106931 coefficients of \(H_{13367}\) constructed from its original square formula.
The developer executed the test and the coordinating agent reproduced it.
Thus no integral factor exists in the two tested degrees, without any need for a high-precision lift of a survivor.

<a id="even-degree-blocks-at-683"></a>
## The improved height screen at 683

The [Gaussian trace height bound](../../../claims/Yin_C_G0873_v1.md#argument) gives \(M(f)\le C^{e/2727}\) at \(p=683\), where \(e=\deg f\) and \(C=(4+2\sqrt2)(1+\sqrt5)/2\).
Degrees 176 and 178 would both give \(M(f)<1.171\), using \(C<111/10\) and the rational inequality \((111/10)^{178}<(1171/1000)^{2727}\).
The original [sublinear-degree criterion](../../../ledger/Yin_L_G0458_v4.md#prime-square-sublinear-factor-criterion) gives a larger finite upper bound.
Here \(2^{11}\equiv-1\bmod683\) and the order is 22.
Inversion fixes each binary Frobenius orbit, so each minimum-size primitive block is the eighth power of one self-reciprocal binary irreducible of degree 22.
The [finite-field enumeration and endpoint test](orbit_lift.py) tries all \(2^{11}\) monic reciprocal degree-22 binary polynomials of constant one and keeps the 31 dividing \(\overline{\Phi_{683}}\).
Every such divisor is irreducible since all primitive binary residue degrees are 22.

Run the program with the options --prime 683 --bits 12 using standard Python 3.10 or later with assertions enabled.
The saved implementation was run by its developer with exact integer arithmetic.
It uses the local block lifts and direct full-product check in [small_lift.py](small_lift.py).
The product of the endpoint block and all 31 lifted blocks agrees with each of the 5459 defining coefficients modulo 4096.

| Modulus | Degree 176 | Degree 178 |
| ---: | ---: | ---: |
| 8 | 31 | 31 |
| 16 | 0 | 31 |
| 64 | 0 | 14 |
| 128 | 0 | 3 |
| 256 | 0 | 1 |
| 512 | 0 | 1 |
| 1024 | 0 | 0 |

Thus \(H_{683}\) has no divisor of either degree.
This computation covers these two degrees for the specified prime.

<a id="degree-floor-and-mersenne-orbits"></a>
## Degree floors before lifting

The [inspected Voutier theorem](../../../audits/literature/JT26/Yin_U001.md#external-inputs), p. 3 of the [author's version](https://arxiv.org/abs/1211.3110), gives \(e h(\beta)>\frac14(\log\log e/\log e)^3\) for every nontorsion root here of degree \(e\ge2\).
Write \(D=8p-6\).
The [binary block theorem](../../../claims/Yin_C_G0871_v1.md#statement) implies \(16\le e\le D\), since \(\operatorname{ord}_p(2)\ge2\).
The ratio \(\log\log x/\log x\) is decreasing for \(x>\exp(\exp(1))\), by differentiation.
Combining Voutier with the explicit [trace height bound](../../../claims/Yin_C_G0873_v1.md#argument) gives the effective necessary condition
\[
 e>\frac{4p-5}{4\log C}
       \left(\frac{\log\log D}{\log D}\right)^3.
\]
The version retaining \(e\) inside the logarithms is stronger and can be applied directly to a candidate degree.
Even the [earlier upper bound](../../../ledger/Yin_L_G0458_v4.md#prime-square-root-height-upper) combined with Voutier gives the same asymptotic order \(e\gg p(\log\log p/\log p)^3\).
The trace estimate improves the explicit constant.
In particular no family of degrees \(O(p^{1-\epsilon})\), for fixed \(\epsilon>0\), can occur.

For a Mersenne prime \(p=2^\rho-1>3\), the exponent \(\rho\) is odd and equals the order of two.
A reciprocal factor has \(e=16\rho k+\delta\), with exactly \(k\) inversion pairs of primitive orbits and \(\delta\in\{0,2\}\).
Thus along any unbounded sequence of these primes one must have
\[
 k\gg \frac{p(\log\log p)^3}{(\log p)^4}.
\]
This rules out a bounded number of orbit pairs in a construction along these primes.
The estimate still permits degrees sublinear in \(p\).

For \(p=131071=2^{17}-1\) the first four reciprocal pair counts have \(e\le1090\).
At \(e=1090\) the upper bound is below \(0.00500\) while the Voutier lower bound exceeds \(0.00537\), both for \(\log M\).
The upper bound increases with \(e\) and the lower one decreases on the applicable range, so every reciprocal factor at this prime contains at least five pairs.
For reproducible rational bounds, \(C<221/20<\exp(2.403)\), \(6.993<\log1090<6.995\), and \(\exp(1.9448)<6.993\).
The first inequality follows using \(\sqrt2<1.41422,\sqrt5<2.23607\).
Each exponential comparison follows by bracketing \(\exp(x)\) between \(S_{64}(x)=\sum_{j=0}^{64}x^j/j!\) and \(S_{64}(x)+(x^{65}/65!)/(1-x/66)\).
These give the strict bounds \(1090(2.403)/524279<0.00500\) and \((1.9448/6.995)^3/4>0.00537\), without a modular factor computation at 131071.
