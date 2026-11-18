---
author: Yin
---

# The three-class multiple test for the Lehmer polynomial at modulus 53

<a id="p53"></a>
## Finite exclusion

Let \(L=x^{10}+x^9-x^7-x^6-x^5-x^4-x^3+x+1\).
No nonzero polynomial in \(\mathbb Q[x]\) divisible by \(L\) has degree at most 106 and support contained modulo 53 in \(\{0,a,b\}\) for \(1\le a<b\le52\).
The coefficients may have either sign and arbitrary height.
In particular this excludes monic reciprocal multiples in the indicated range.
For [Yin's Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract), the range comes from the [degree bound for the surviving factor](../../../claims/Yin_C_G0345_v347.md#statement) at \(D=10,\ p=53,\ s\le2\), since \(10/(1-48/53)=106\).

For each of the \(\binom{52}{2}=1326\) pairs, the allowed exponents in \([0,106]\) are
\[
 0,\ a,\ b,\ 53,\ 53+a,\ 53+b,\ 106 .
\]
Compute the vectors of \(x^e\bmod L\) in the power basis \(1,x,\ldots,x^9\).
The vectors are integral because \(L\) is monic.
A multiple on the indicated support would give a nonzero rational relation among these seven vectors, including the possibility that some coefficients vanish.

<a id="checks"></a>
## Arithmetic and reproduction

Run the [verifier](verify.py) from the repository root with Python 3.8 or later and its standard library.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0167/verify.py
~~~~

Multiplication by \(x\), followed by subtraction of the old top coefficient times \(L\), gives each successive vector exactly.
For every pair, elimination over \(\mathbb F_{1009}\) returned rank seven.
The modulus is prime by trial division through 31.
A nonzero minor modulo 1009 remains nonzero over the rationals.
As a second check on linear independence, the program computed each integer Gram determinant by fraction-free Bareiss elimination.
All determinants were positive, and the least was \(27\,346\,309\,442\), attained at \((a,b)=(15,34)\).
Both rank checks use the same exact power vectors.
This finite result applies at the stated modulus and degree cap.
The [independent reproduction](../../../audits/reviews/Yin_R_G0562_v349.md#p53-review) uses separate polynomial divisions and exact maximal minors and verifies how this computation completes the prime bound for the degree-ten input.
