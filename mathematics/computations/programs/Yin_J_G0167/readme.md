---
author: Yin
---

# Three-class multiple tests for the Lehmer polynomial modulo 53 and 29

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

<a id="p29"></a>
## Exclusion at modulus 29 through degree 32

No nonzero multiple of \(L\) in \(\mathbb Q[x]\) of degree at most 32 has support contained modulo 29 in \(\{0,a,b\}\) for \(1\le a<b\le28\).
For any such pair, the allowed exponents are \(0,a,b,29\), together with \(29+a\) if \(a\le3\) and \(29+b\) if \(b\le3\).
Of the \(\binom{28}{2}=378\) supports, 300 have four exponents, 75 have five and three have six.

The [modulus-29 verifier](verify_p29.py) constructs each support by scanning all exponents from zero through 32.
It uses the [integer remainder and maximal-minor routines](checks/maximal_minors.py) to divide the permitted monomials by \(L\) and expand all maximal minors of the resulting coefficient matrix along successive columns.
At least one maximal minor was nonzero for every pair.
Thus each matrix has independent columns over \(\mathbb Q\), proving the exclusion for arbitrary coefficients.
Run the following command from the repository root with Python 3.8 or later and its standard library.

~~~~powershell
python -B mathematics/computations/programs/Yin_J_G0167/verify_p29.py
~~~~

If a cyclotomic multiple of \(L\) occupied two or three residues at 29, the [degree estimate for the surviving factor](../../../claims/Yin_C_G0345_v349.md#degree) would give a diagonal multiple of \(L\) of degree at most \(\lfloor 10\cdot29/(29-20)\rfloor=32\).
The fast width is at most two, so this diagonal occupies at most three residues, including zero after its least exponent is shifted to zero.
The calculation excludes every such multiple, regardless of the degree of the initial cyclotomic multiplier.
The [independent verification](../../../audits/reviews/Yin_R_G0562_v350.md#lehmer-p29-review) also checks the application to every prime at least 29.
