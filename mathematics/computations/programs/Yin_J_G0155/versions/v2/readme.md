---
author: Yin
---

# The first conductor for the fixed zero-profile prefix through degree four

<a id="first-conductor"></a>
## The unique completion at conductor 37

For the [fixed zero profile and the full odd-grid integer chart](../../../../../claims/Yin_C_G0881_v3.md#prefix-coordinates),
\[
                       P_{*,0}(z)=\frac{(1+z^2)^2}{(1-z)(1-z^2)},
\]
the first conductor admitting a strict terminal sign cut, the strict endpoint, and agreement through coefficient index four is \(p=37\).
There is exactly one such integer completion at that conductor.
It agrees through index five, and its coefficient at index six is 13, exceeding the prescribed value 12 by one.
Consequently the maximum matching index is five at \(p=37\).

Put \(p=2n+1\), \(b_j=2\cos(2\pi j/p)\), \(E_{-1}=0\), \(E_0=1\), \(E_{i+1}=tE_i-E_{i-1}\), and \(B_i=E_i+E_{i-1}\).
For \(h=\sum_{i=0}^{n-1} a_iE_i\) use \(Q=tB_n+\sum_{i=0}^{n-1}a_i B_{n-i-1}\), residues \(\rho_j=Q(b_j)/B_n'(b_j)=\nu_jh(b_j)\) with \(\nu_j=(4-b_j^2)/p>0\), and \(P=z^{n+1}Q(z+z^{-1})\).
Agreement through index four prescribes \((a_0,a_1,a_2)=(2,0,4)\), and \(P(-1)=2+\sum_i(-1)^i a_i\) must be positive.
Each \(1\le c<n\) prescribes positive residues through index \(c\) and negative residues thereafter.
The unique solution at \(p=37\) has \(n=18,\ c=17\) and
\[
 (a_0,\ldots,a_{17})=(2,0,4,0,5,0,5,1,4,2,3,3,1,4,-1,4,-3,4).
\]
Its endpoint is \(P(-1)=4\), the quotient \(Q(-2)/B_{18}(-2)=-4\), and \(\operatorname{Res}(B_{18},Q)=5329\).
Every grid sign is checked by a rational enclosure, and direct expansion gives \(P-P_{*,0}=z^6+O(z^7)\).
The [whole-root count](../../../../../claims/Yin_C_G0881_v10.md#nonreal-pair) supplies exactly one exterior conjugate pair because \(Q-tB_{18}\) has degree 17 and leading coefficient two.
Rational complex root counting for the complete degree-38 lift puts one root in
\[
 [-0.04292563,-0.04292562]+i[1.29163798,1.29163799],
\]
so its squared modulus gives \(1.67017127<M(P)<1.67017132\).

<a id="covering-box"></a>
## All coefficients and cuts in the finite enumeration

For each odd \(7\le p\le37\) the program tests all \(n-1\) cuts and every integral extension of the three prescribed coordinates.
There are 152 conductor and cut pairs.
The smaller allowed conductor \(p=5\) has reciprocal lift degree six, so its fourth coefficient equals its second, whereas \(P_{*,0}\) prescribes 8 and 4 respectively.
At \(p=5\) matching through index three would force the constant \(h=2\), which fails the negative block, while \(h=2+2t\) satisfies the cut and endpoint and matches through index two.
For \(p=7\), \(h=2-E_2=3-t^2\) matches through index three with positive endpoint and exactly the last grid value negative, by comparing the three angles \(2\pi j/7\) with \(\pi/6,5\pi/6\).
For all odd \(p\ge9\) the [integral example \(h=(2t+3)(t-1)^2\)](../../../../../claims/Yin_C_G0880_v4.md#statement) matches through index three.
Thus the maximum index is three at every odd conductor from 7 through 35.

To bound heights, take the arithmetic midpoint \(u=(b_c+b_{c+1})/2\).
The [orthogonality of the original grid weights](../../../../../ledger/Yin_L_G0464_v5.md#odd-grid-product) gives \(a_i=\sum_j\rho_j E_i(b_j)\), since every product \(E_i E_k\) here has degree at most \(2n-2=p-3\) and the \(E_i\) are orthonormal for the semicircle measure.
In particular \(\sum_j\rho_j=2\), \(\sum_jb_j\rho_j=0\), and strictness implies
\[
 0<\sum_j|b_j-u|\,|\rho_j|=-2u<4 .
\]
Every node has distance at least half the gap, and
\[
 b_c-b_{c+1}=4\sin((2c+1)\pi/p)\sin(\pi/p)\ge32/p^2
\]
by the sine chord bounds and \(1\le c<n\).
Therefore \(\sum_j|\rho_j|\le p^2/4\), and \(|E_i|\le i+1\) on \([-2,2]\) gives the integer box \(K_i=\lceil p^2(i+1)/4\rceil\) for \(|a_i|\).

The program first isolates the \(n\) ordered roots of the monic \(B_n\) in disjoint rational intervals by evaluating \(B_n\) at their endpoints.
Each interval brackets a root (including exact equality), and the degree exhausts all roots.
Rational bisection refines the intervals to widths at most \(2^{-90}\).
For \(D=2^{40}\), rounding \(D E_i\) at the midpoint gives an integer \(M_{ji}\) and an error bound \(e_{ji}\) from half a rounding unit plus the interval radius times \(D(i+1)i^2\), rounded upward.
Indeed \(E_i(2\cos\theta)\) is the sum of the frequencies \(e^{\mathrm i(i-2k)\theta}\) for \(0\le k\le i\).
Pairing opposite frequencies and using \(|\sin(\ell\theta)|\le\ell\sin\theta\) bounds \(|E_i'|\) on \([-2,2]\) by \((i+1)i^2\).
Thus a necessary integer inequality at node \(j\) of required sign \(\tau_j\) is
\[
 -\tau_j\sum_i M_{ji}a_i\le\sum_i e_{ji}K_i .
\]
The exact endpoint row is \(-\sum_i(-1)^ia_i\le1\).
The algorithm substitutes the three fixed coordinates and then branches over the allowed integer values of each remaining coordinate in order.

<a id="integer-bounds"></a>
## Certifying each branch with integer arithmetic

At any branch let \(A v\le b\) be the remaining integer rows and let \(|v_i|\le K_i\) be its remaining box.
For any vector of nonnegative integers \(\lambda\), integer scale \(S>0\), and \(e=(1,0,\ldots,0)\) or its negative,
\[
 S\, e\cdot v\le \lambda\cdot b+\sum_i |S e_i-(\lambda^{\mathsf T}A)_i|K_i .
\]
Floor division therefore gives a certified upper bound for either sign of the next integer coordinate.
Likewise \(\lambda\cdot b+\sum_i|(\lambda^{\mathsf T}A)_i|K_i<0\) certifies an empty branch.
SciPy supplies proposed multipliers from numerical linear programs with rows divided by \(D\).
The checker rounds the multipliers after scaling by \(2^{40}\), clips each to a nonnegative integer, and uses \(S=D\,2^{40}\) in the first inequality.
A solver status alone discards no assignment.
When it supplies no verified reduction, the program can use the full corresponding coefficient bound.
Every integer value within the resulting bounds is visited, and a completed outer leaf is tested against the original algebraic signs and integer endpoint.
A nonconstant \(\gcd(h,B_n)\) certifies an exact grid zero.
Otherwise the signed midpoint evaluation of \(h\) is certified when its magnitude exceeds \(\sum_i e_{ji}|a_i|\) in scaled units.
An unresolved sign at a nonzero grid value stops the calculation before publication.

Ten pairs of a complete coefficient vector and a cut survived the outer inequalities.
At conductors 27, 33, and 35 there were respectively two, five, and two such pairs, all excluded by grid zeros.
The remaining pair is the strict conductor-37 witness above.
The enumeration covers \(p\le37\) and does not determine which larger conductors admit longer fixed prefixes.

<a id="reproduction"></a>
## Reproducing the conductor-37 calculation

Run the [native checker](fixed_prefix.py) from the repository root.
The author run used Python 3.14.3, SymPy 1.14.0, NumPy 2.4.4, and SciPy 1.17.1.

~~~text
python -B mathematics/computations/programs/Yin_J_G0155/versions/v2/fixed_prefix.py
python -B mathematics/computations/programs/Yin_J_G0155/versions/v2/fixed_prefix.py --witness-only
~~~

The complete command writes the [conductor counts and exact witness](../../../../outputs/Yin_J_G0155/fixed_prefix_first_conductor.json).
The second command verifies just the witness with Python and SymPy and writes the [whole-measure enclosure and lift coefficients](../../../../outputs/Yin_J_G0155/fixed_prefix_witness.json).
Neither command requires an earlier output.
Each publishes its own output atomically after completing its checks.
