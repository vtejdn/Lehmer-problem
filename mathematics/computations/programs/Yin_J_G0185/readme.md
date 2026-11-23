---
author: Yin
---

# Salem units in the consecutive-coefficient family

The coefficients \(2,3\) give a nonmonic parent with a degree-six Salem factor. [Exact witness and finite search](witnesses.md#witness)
The [catalogue test](catalogue.md#catalogue) treats the 72 retained Salem numbers, including a degree-eight witness at \(q=1\), and also examines [parents with short exponent one](catalogue.md#short-one).
At short exponent one, the degree-six witness and its sign changes give the [complete classification for \(q\ge2\) through primitive degree 44](short_one.md#classification).
For primitive units with one exterior reciprocal pair, the same sextic gives the [complete degree-44 classification in all directions](salem_directions.md#classification).

For each of Mossinghoff's 10,236 listed small-measure polynomials, the [pole and endpoint norms](pole_catalogue.md#endpoint) exclude its roots and their negatives as short coordinates possessing an integral graph partner at any \(q\ge2\).

<a id="exclusion"></a>
## Exclusion at every coefficient height and dilation

Let \(\lambda>1\) be the largest real zero of the [classical Lehmer polynomial](../../../ledger/Yin_L_G0462_v150.md#lehmer)
\[
 F(X)=X^{10}+X^9-X^7-X^6-X^5-X^4-X^3+X+1.
\]
For every integer \(q\ge1\), \(|a|=q,\ |b|=q+1\), \(\epsilon=\pm1\), and integers \(0<U<V\),
\[
 a(1+\epsilon\lambda^{U+V})+b(\lambda^U+\epsilon\lambda^V)\ne0.
\]
This includes all common dilations \(U=gu,\ V=gv\) and all conjugates of \(\lambda\), since the parent has rational coefficients.
Existence along a sequence \(q\to\infty\) remains open.

Write \(T=\lambda^U,\ Y=\lambda^V\).
The numbers \(1+\epsilon TY\) and \(T+\epsilon Y\) have the same sign because \(1<T<Y\).
Thus any equality requires \(b/a=-(q+1)/q\), and solving for \(Y\) gives
\[
 Y=\frac{(q+1)T-q}{|qT-(q+1)|},\qquad \epsilon=\operatorname{sgn}(qT-(q+1)).
\]
The numerator is positive and a zero denominator cannot solve the original equation.
The [exterior radius bound](../../../claims/Yin_C_G0345_v869.md#radius) gives \(U\log\lambda<\operatorname{arcosh}(1+1/q)\), or \(q<2T/(T-1)^2\).
For nonprimitive \((U,V)\) apply it at \(\lambda^{\gcd(U,V)}\) with the primitive exponents.

Put \(l=117628/100000,\ h=117629/100000\).
Exact substitution gives \(F(l)<0<F(h)\), and \(F(1+X)\) has one coefficient sign change, so \(l<\lambda<h\) by Descartes’ rule.
The function \(2T/(T-1)^2\) decreases for \(T>1\).
At each \(U\) we therefore take \(q\le\lfloor2l^U/(l^U-1)^2\rfloor\), which vanishes at \(U=9\) and every larger \(U\).
For each remaining \((q,U)\), the range \([q l^U-(q+1),q h^U-(q+1)]\) omits zero.
Divide \((q+1)h^U-q\) by the smaller absolute endpoint to obtain a rational upper bound on \(Y\).
Keep \(V>U\) whenever \(l^V\) is at most this bound.

| \(U\) | Maximum \(q\) in the radius test | Remaining triples \((q,U,V)\) | Largest remaining \(V\) |
| ---: | ---: | ---: | ---: |
| 1 | 75 | 157 | 22 |
| 2 | 18 | 57 | 17 |
| 3 | 8 | 29 | 14 |
| 4 | 4 | 24 | 21 |
| 5 | 2 | 13 | 16 |
| 6 | 1 | 5 | 11 |
| 7 | 1 | 2 | 9 |
| 8 | 1 | 0 | — |

All 287 candidates have \(0<V-U<V+U\le30\).
Over \(\mathbb F_2\), the program checks \(X^{31}\equiv1\bmod\overline F\), and \(F(1)=-1\).
Thus each root of \(\overline F\) has order 31, since 31 is prime.
If \(F\) and an integral parent shared a root, their common monic minimal factor would divide both over \(\mathbb Z\), since \(F\) is monic.
Its reduction modulo two keeps its positive degree.
The parent reduces to \(X^U(1+X^{V-U})\) at even \(q\) and \(1+X^{V+U}\) at odd \(q\).
Its nonzero roots therefore have order dividing \(V-U\) or \(V+U\), both strictly between zero and 31.
This contradiction excludes each candidate.

<a id="reproduction"></a>
## Reproduction

Run the [certificate](lehmer_unit.py) from the repository root with Python 3 and its standard library.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0185/lehmer_unit.py
~~~~

The program uses rational arithmetic for the enclosure and exponent bounds.
It also calculates the remainder of each signed parent by \(F\) over the integers by successive multiplication of \(1\) by \(X\) modulo \(F\).
All 287 remainders are nonzero.
The binary order argument excludes common roots independently of any irreducibility test on \(F\).
