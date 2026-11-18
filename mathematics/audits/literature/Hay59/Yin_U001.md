---
author: Yin
---

# Jensen's formula and zeros on the bounding circle

<a id="hay59-u001"></a>
## Part I, Section 1.2

I inspected the [TIFR electronic edition](readme.md#edition), printed pages 1–4, including the theorem display across the page break and the [centered corollary (1.2)](../../../literature/pdf/Hay59--tifr17.pdf#page=8).
For a function analytic on a neighborhood of the closed disk of radius \(R\), nonzero at its center, the boundary mean of its log modulus minus the log modulus of its center value equals the sum of \(\log(R/|z_j|)\) over its interior zeros, counted with multiplicity.
Zeros on the circle have zero contribution to the sum and logarithmically integrable boundary values.

The [electronic Theorem 1 display](../../../literature/pdf/Hay59--tifr17.pdf#page=5) prints the left-hand logarithm without the absolute value and has a malformed boundary integrand.
The proof on printed page 2 gives the real logarithmic modulus and Poisson-weighted boundary integral explicitly for a zero-free function.
On pages 3–4 the proof removes interior zeros and poles by disk factors of unit boundary modulus and treats boundary zeros by an indentation with error of order \(\rho|\log\rho|\).
The centered formula (1.2) gives the signs for zeros and poles directly.
This inspection concerns the electronic exposition and does not attribute the display issue to the original printing.

In the [weighted pencil identity](../../../claims/Yin_C_G0345_v381.md#jensen) the function for each phase is analytic after the source disk change of coordinates, its center value is nonzero, and the contribution of every counted zero has the positive sign in the boundary-minus-center difference.
The target disk change and its resulting phase weight are derived in that argument.
