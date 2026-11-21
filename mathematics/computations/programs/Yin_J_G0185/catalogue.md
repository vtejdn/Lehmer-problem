---
author: Yin
---

# The consecutive-coefficient sections at 72 small Salem numbers

<a id="catalogue"></a>
## The unique catalogue solution

Let \(\lambda\) be any of the 72 positive Salem numbers listed by Mossinghoff, let \(q\ge1\) be an integer, and let \(0<U<V\) be integers.
Among all choices \(|a|=q,\ |b|=q+1,\ \epsilon=\pm1\), the equation
\[
a(1+\epsilon\lambda^{U+V})+b(\lambda^U+\epsilon\lambda^V)=0
\]
holds only for rank 23, with \((q,U,V,\epsilon)=(1,3,14,+1)\) and \((a,b)=\pm(1,-2)\).
The number is displayed as \(1.280638156268\) and has minimal polynomial \(F=X^8-X^5-X^4-X^3+1\).
Multiplication gives the exact witness
\[
1-2X^3-2X^{14}+X^{17}
=(X+1)F(X)(X^8-X^7+X^6-2X^5+3X^4-2X^3+X^2-X+1).
\]
The signs \(F(1)=-1,\ F(2)=201\) already give a real root greater than one, which is a unit because \(F\) is monic with constant term one.
The result includes all common dilations \(U=gu,\ V=gv\), and the sole solution has \(\gcd(3,14)=1\).

Mossinghoff reports that his catalogue is complete for Salem numbers strictly below \(13/10\) of degree at most 44.
Of the 72 inputs, exactly 46 satisfy both conditions, as checked by the degree and exact sign at \(13/10\).
Consequently rank 23 is the unique positive Salem number in this complete range occurring in any of the indicated sections, and is the least such positive Salem number of degree at most 44.
At larger degrees or above the source's completeness cutoff, the calculation covers the listed inputs. [Fixed source table](https://github.com/mossinghoff/Mahler-Measure-Database/blob/27df0451b18cf711c9ff2a5dacbc46eec33a15a4/SalemList.txt)

<a id="short-one"></a>
## Degree at short exponent one

Suppose \(u=1\) and \(q\ge4\), and let \(z\) be a nontorsion unit root of a section at any dilation \(g\).
After the [sign normalization and pole-norm argument](../../../claims/Yin_C_G0345_v877.md#sign), the minimal polynomial of the normalized primitive unit \(\pm z^g\) has one positive exterior root \(\alpha\), its reciprocal, and all other conjugates on the unit circle.
Moreover \(1<\alpha<(q+1)/q\le5/4\).
A quadratic reciprocal unit in this interval would have integer trace strictly between \(2\) and \(5/4+4/5=41/20\), which is impossible.
Thus \(\alpha\) is a Salem number and satisfies the normalized section equation with short exponent one.
If its degree were at most 44, it would belong to the complete range just tested, whose sole solution has \(q=1,\ U=3\).
It follows that \(\deg(z^g)=\deg(\alpha)\ge46\) by evenness, and hence \(\deg z\ge46\).

<a id="bounds"></a>
## Finite bounds for each source polynomial

For each input \(P\), exact sign evaluation at rational endpoints gives \(1<l<\lambda<h\), since the source identifies \(P\) as a monic Salem minimal polynomial with a unique real zero greater than one.
The signs of \(1+\epsilon\lambda^{U+V}\) and \(\lambda^U+\epsilon\lambda^V\) agree, so a zero requires \(b/a=-(q+1)/q\).
Setting \(T=\lambda^U\) in the [radial bound](../../../claims/Yin_C_G0345_v869.md#radius) gives \(q<2T/(T-1)^2\).
Since the right side decreases for \(T>1\), we test only \(1\le q\le\lfloor2l^U/(l^U-1)^2\rfloor\), ending the search at the first \(U\) where this bound is zero.

For a remaining \(q,U\), the equation forces
\[
\epsilon=\operatorname{sgn}\big(qT-(q+1)\big),\qquad
\lambda^V=G_q(T)=\frac{(q+1)T-q}{|qT-(q+1)|}.
\]
The positive unit \(T>1\) is irrational, since a rational algebraic unit is \(1\) or \(-1\).
Thus bisection eventually puts \(q l^U-(q+1)\) and \(q h^U-(q+1)\) strictly on the same side of zero.
On this interval \(G_q\) is monotone, with derivative of absolute value \((2q+1)/|qT-(q+1)|^2\).
Write \(A\) and \(B\) for the smaller and larger endpoint values.
Every solution requires \(l^V\le B\) and \(h^V\ge A\).

Across the 72 source ranks, the radial bound leaves 3,367 choices of \((q,U)\), counted separately for each rank.
The upper bound \(l^V\le B\) leaves 6,887 choices of \((q,U,V)\) across these ranks.
The largest \(q,U,V,U+V\) retained in the respective tests are \(75,8,53,54\).
The lower bound \(h^V\ge A\) leaves only the displayed witness.
As a second check, for every one of the 6,887 candidates the program reduces the signed parent modulo the source polynomial in \(\mathbb Z[X]\), using successive multiplication by \(X\) modulo \(P\).
Only the rank-23 remainder vanishes.
For a separate arithmetic check, the computation author used SymPy integer polynomial division on all monomials through degree 61 and all 55,872 choices of rank, \(1\le U\le8,\ U<V\le53,\ \epsilon=\pm1\).
With \(C=X^U+\epsilon X^V\) and \(D=1+\epsilon X^{U+V}-C\), a solution requires \(qD=C\bmod P\).
Solving for \(q\) at one nonzero coefficient of the remainder of \(D\) and checking all the other coefficients recovers exactly the same hit.
Whenever \(D\) reduces to zero, \(C\) has a nonzero remainder.

<a id="reproduction"></a>
## Reproduction

Run the [catalogue calculation](catalogue.py) from the repository root with Python 3 and its standard library.
It reuses the [J173 source reader and integral sign evaluation](../Yin_J_G0173/least_exponents.py) for the [registered Mos26b table](../../../audits/literature/Mos26b/readme.md).
The [J173 source instructions](../Yin_J_G0173/readme.md#reproduction) give the fixed revision and the retrieval command for an empty source store.

~~~sh
python -B mathematics/computations/programs/Yin_J_G0185/catalogue.py
python -B mathematics/computations/programs/Yin_J_G0185/catalogue.py --bounds
~~~

The first command prints each source rank, the exact hits, finite counts and exponent bounds.
The second also prints the excluded height and short-exponent ranges, all rational denominator enclosures, the last long exponent allowed by the upper bound, and the integer range surviving both graph bounds.
