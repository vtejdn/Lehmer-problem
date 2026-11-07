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
Only the first of these primes has undergone an endpoint lift here.

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
