---
author: Yin
---

# Coefficient certificates for cyclotomic multiples

<a id="lehmer-phi4"></a>
## A circle norm attained at the primitive fourth roots

The [integer verifier](lehmer_phi4.py) checks the cyclotomic multiple \(R=L^6\Phi_9^2\Phi_{10}^2\Phi_{15}\Phi_{21}\) of Lehmer's polynomial in the [order-four avoidance argument](../../../claims/Yin_C_G0901_v16.md#lehmer).
Its inputs are the coefficients of \(L\), the six cyclotomic orders with repetition and the sixteen intervals \([j/4,(j+1)/4]\) for \(-8\le j<8\).
All are specified in the program.
Run it from the repository root with Python 3.9 or later.

~~~~powershell
python -B mathematics/computations/programs/Yin_J_G0186/lehmer_phi4.py
~~~~

The verifier constructs the cyclotomic factors by exact monic division of \(z^n-1\), multiplies in \(z\), and obtains the trace polynomial \(W(x)=z^{-50}R(z)\), \(x=z+z^{-1}\), by the recurrence for \(z^j+z^{-j}\).
It compares this with the product of the individual trace polynomials.
It checks the contact \(W(0)=729,\ W'(0)=0\) and prints all sixteen floors of the minimum Bernstein coefficients for each of the two polynomials in the claim.
The executed calculation gave positive minima on every interval, with smallest floors \(4\) for \(729+W\) and \(13\) for \((729-W)/x^2\).
Integer arithmetic and floor division suffice throughout.
The printed interval values reproduce the table in the claim.

<a id="below-two"></a>
## A multiple below base two without a zero at one

Let \(C=\prod_n\Phi_n^{c_n}\), with all unlisted multiplicities zero.
The following are the complete inputs for the [finite-forbidden-set bound](../../../claims/Yin_C_G0901_v22.md#statement).

| \(n\) | 2 | 3 | 4 | 5 | 6 | 10 | 12 | 14 | 15 | 21 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(c_n\) | 64 | 15 | 40 | 12 | 54 | 60 | 12 | 43 | 45 | 6 |

| \(n\) | 22 | 26 | 33 | 35 | 48 | 54 | 55 | 76 | 77 | 80 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(c_n\) | 17 | 9 | 14 | 14 | 9 | 17 | 7 | 6 | 10 | 5 |

The [coefficient verifier](lehmer_below_two.py) constructs these factors with the [integer polynomial arithmetic](lehmer_phi4.py), multiplies them with all 160 copies of \(L\), and sums the absolute values of the resulting coefficients.
Run it from the repository root with Python 3.9 or later.

~~~~powershell
python -B mathematics/computations/programs/Yin_J_G0186/lehmer_below_two.py
~~~~

The exact calculation gave \(\deg C=3908\), \(C(1)=71052345981129072096647871486492672000000000000=2^{104}3^{15}5^{12}\), and \(\deg(L^{160}C)=5508\).
The coefficient norm was \(1021447200076579342416613392732943233813204502112\), strictly below \((7/10)\,2^{160}\).
