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
