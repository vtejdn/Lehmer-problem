---
author: Yin
---

# Small-record measures exclude modular reversal of separated end blocks

<a id="record"></a>
## The sign of the modular restriction

Let \(Q\in\mathbb Z[X]\) be monic of degree \(r\), write \(Q^*(X)=X^r Q(1/X)\), and take
\[
                D=X^nQ+\varepsilon Q^*,\qquad n>r,\qquad \varepsilon=\pm1.
\]
Suppose the whole \(D\) is irreducible and noncyclotomic.
For a rational prime \(p\) write \(\bar Q=X^tT\) with \(T(0)\ne0\) and reverse \(T\) in its own degree.
If \(T^*=\pm T\), then \(M(D)>\sqrt{3/2}\).
In particular every strict degree record at a degree at least ten that has this complete separated representation has \(T^*\ne\pm T\) at **every** prime.
At coefficient height one the support of its end block must be asymmetric under reflection about the midpoint of its extreme exponents.
Neither the height assumption nor \(r=o(\deg D)\) is required for the measure threshold.

Indeed the degree-ten Lehmer polynomial \(L=X^{10}+X^9-X^7-X^6-X^5-X^4-X^3+X+1\) has a single exterior root, which is positive. [Mossinghoff, Rhin and Wu, p. 2](../audits/literature/MRW08/Yin_U001.md#degree)
It has \(L(1)=-1\), \(L(19/16)=330753263801/16^{10}>0\), and \((19/16)^2<3/2\).
Thus the measure ceiling furnished by this competitor suffices at every such record.
For \(d=\deg D\), the [nonreversal bound](Yin_C_G0904_v3.md#finite-field) now gives, uniformly over all primes,
\[
 \deg\gcd(\bar D,X^j-1)\le 2r+2\sqrt{rj}.
\]
Here \(r\ge1\), as the \(r=0\) polynomials are cyclotomic products.
Returning a fraction \(\eta\) consequently takes \(j\ge(\eta d-2r)_+^2/(4r)\).
If complete record polynomials occur along an unbounded sequence with \(r=o(d)\), their maximal returned fraction at \(j\le Ad\) tends to zero for each fixed \(A\).
The existence or exclusion of such record polynomials remains open.

<a id="binomial"></a>
## A measure bound for containing a signed binomial modulo a prime

Put \(N=n+t\), \(h_0=r-t\), so \(\deg D=N+h_0<2N\).
If \(T^*=\pm T\), then \(\bar D=T(X^N-s)\) for a sign \(s\in\{1,-1\}\).
More generally let \(P\mid D\) be a monic irreducible noncyclotomic factor of degree \(d\), and put \(c=\deg D-d\).
At least \(K=(N-c)_+\) degrees of \(X^N-s\), counted with multiplicity, occur in \(\bar P\).
Indeed the complement of \(\bar P\)'s gcd in this binomial divides the reduction of \(D/P\).

Let \(B\) be the power-basis companion for \(P\), set \(Z=sB^N\), and write \(m=\log M(P)\).
For each integral polynomial \(V\) whose reduction vanishes at one, \(\ker(Z-I)\bmod p\) lies in \(\ker V(Z)\bmod p\).
The first nullity is \(\deg\gcd(\bar P,X^N-s)\) by the cyclic module calculation.
Whenever the determinant is nonzero it is therefore divisible by \(p^K\), including at primes ramified in \(P\). [Multiplication and Smith form](Yin_C_G0904_v2.md#modular)
For any polynomial \(U\) of degree \(l\), the maximum modulus principle inside the unit disk and for its reversed polynomial gives
\[
                 |\det U(Z)|\le \|U\|_\infty^d M(P)^{Nl},
\]
where \(\|U\|_\infty=\max_{|z|=1}|U(z)|\).
All the determinants used below are nonzero since their scalar zeros are roots of unity.

At \(p=2\) use \(U=(Z^2-1)^2(Z^2+1)\) in polynomial notation.
Its five factors \(Z-1,Z-1,Z+1,Z+1,Z^2+1\) vanish at one modulo two.
On the unit circle its absolute value is \(8v^2\sqrt{1-v^2}\) with \(v=|\sin(\arg Z)|\), maximized at \(v^2=2/3\).
At \(p=3\) use \(U=(Z-1)(Z^2+Z+1)=Z^3-1\).
At \(p\ge5\) use \(U=Z-1\).
It follows that
\[
\begin{array}{ll}
6Nm\ge 5K\log2-d\log(16/(3\sqrt3)), & p=2,\\
3Nm\ge 2K\log3-d\log2, & p=3,\\
Nm\ge K\log p-d\log2, & p\ge5 .
\end{array}
\]
For the whole polynomial \(K=N\) and \(d<2N\).
The three lower bounds on \(M(D)\) are then strictly greater than \(\sqrt{3/2}\), \((3/2)^{2/3}\), and \(p/4\), respectively, with the first constant given by \((2^5/(16/(3\sqrt3))^2)^{1/6}=\sqrt{3/2}\).
The last two constants themselves exceed \(\sqrt{3/2}\).
Along any sequence of such presentations with \(c=o(N)\) and a prime of signed reversal on each input, even if that prime varies, the inequalities give \(\liminf M(P)\ge\sqrt{3/2}\).
Thus adding a cofactor of sublinear degree, cyclotomic or otherwise, cannot produce the signed reversal along a sequence of record factors with \(N\to\infty\).

<a id="finite"></a>
## The degree-ten record and a cyclotomic completion

For an even-degree reciprocal polynomial a disjoint presentation as above with \(\varepsilon=1\) requires the middle coefficient to vanish.
The degree-eight minimizer \(X^8-X^5-X^4-X^3+1\) and \(L\) have middle coefficient \(-1\) in these choices of sign for the variable. [Degree table, Theorem 1](../audits/literature/MRW08/Yin_U001.md#degree)
Changing \(X\) to \(-X\) preserves nonvanishing of that coefficient.
Nevertheless the actual ten-degree record has the exact completion
\[
       (X-1)L=X^8 f-f^*,\qquad f=X^3-X-1 .
\]
Its end support \(\{0,1,3\}\) fails reflection symmetry, and the coefficients at \(X\) preclude proportional reversal modulo every prime.
The complete ten-degree record itself does have a full return modulo two at \(j=31\). [Exact binomial divisor](Yin_C_G0904_v4.md#braid)
This finite completion illustrates why the scope of the representation and the limiting width hypothesis matter in applying the sequence criterion.

<a id="exterior"></a>
## The end block must have many exterior roots

Fix \(1<\lambda<\theta\), where \(\theta\) is the positive root of \(X^3-X-1\).
In a complete irreducible noncyclotomic presentation as in the first section with \(M(D)\le\lambda\), let \(k\) count the zeros of \(Q\) of modulus strictly greater than one with multiplicity.
Then \(n\ll_\lambda k^2\), and therefore \(k\gg_\lambda\sqrt{\deg D}\).
This strengthens the [degree-width estimate](Yin_C_G0904_v3.md#record-width) even when the other zeros of the end block are numerous.

Absorb any power \(X^t\) dividing the integral \(Q\) into \(X^n\); this increases \(n\), leaves \(k\) unchanged and preserves the presentation.
If the resulting \(Q\) were equal to its signed reversal then \(D\) would be a multiple of \(X^n\pm1\) with cofactor \(Q\).
The irreducibility and noncyclotomy of \(D\) exclude this.
Thus \(Q\) has an irreducible factor not equal to its signed reversal, and \(m(Q)\ge\log\theta\) by [Smyth's nonreciprocal bound](../audits/literature/Smy71/Yin_U001.md#smy71-statement-and-conventions), with \(m=\log M\).
In particular \(k\ge1\).

Here is a radial estimate independent of the coefficients.
For \(|z|=e^y>1\), consider the factors \((1-\overline\beta z)/(z-\beta)\) over the roots of \(Q\).
Their product is \(Q^*(z)/Q(z)\) since the coefficients are real and \(Q\) is monic.
An interior or unit-circle root contributes modulus at most one by subtracting the squared moduli.
For an exterior root \(|\beta|=e^x\), the maximum on this circle occurs on its radial line, since the ratio squared is one plus \((e^{2y}-1)(e^{2x}-1)/|z-\beta|^2\).
Its logarithm, for \(x\ne y\), is at most
\[
 \log\frac{\sinh((x+y)/2)}{\sinh(|x-y|/2)}
 \ \le\ y+\log\frac{x+y}{|x-y|}.
\]
The last estimate uses \((\log(\sinh v/v))'=\coth v-1/v\le1\) for \(v>0\), which follows from \(e^{2v}-1\ge2v\).
For every \(T>0\) the mean of the last log ratio for \(T\le y\le2T\) is bounded by an absolute constant \(C_0=\log6+2\).
After dividing both variables by \(T\), if \(x/T\ge4\) the ratio is at most three.
For \(0<x/T<4\) the numerator is at most six, and the integral of \(\log^+(1/|x/T-y/T|)\) on the rescaled interval is at most \(\int_{-1}^1-\log|v|\,dv=2\).
Choose \(y\) in that interval avoiding the finite set of root log radii and with
\[
            \log\max_{|z|=e^y}|Q^*(z)/Q(z)|\le (C_0+2T)k .
\]
This follows by averaging the sum of the individual exterior-root bounds.

Let \(\Delta=\log(\theta/\lambda)\), choose a fixed \(0<u<\min(1,\Delta/8)\), and take \(T=u/k\).
If \(n>C_\lambda k^2\) for sufficiently large \(C_\lambda\), then \(ny\ge nu/k\) exceeds \((C_0+2T)k+\log(1/\delta)\), where \(0<\delta<1\) is fixed with \(\log(1-\delta)>-\Delta/4\).
Consequently \(|Q^*/(z^nQ)|\le\delta\) on that circle.
Write \(s_y(F)=\sum_\gamma\log^+(|\gamma|e^{-y})\) over the zeros of a monic polynomial.
Jensen's formula gives
\[
       m(D)\ge s_y(D)\ge s_y(Q)+\log(1-\delta)
                 \ge m(Q)-ky+\log(1-\delta)>\log\lambda ,
\]
because \(ky\le2u\).
This contradiction gives the asserted bound.
It rules out end blocks of bounded exterior-root count at arbitrarily large record degrees, while blocks with a growing population of exterior roots remain possible.

## Assessment history

### Decision end-block-measure

| Field | Value |
| --- | --- |
| date | 2026-11-28T07:29 |
| status | proved |
| reason | A signed reversal introduces a binomial of degree greater than half the full degree. Its three prime-dependent determinant bounds exceed the degree-ten competitor. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Record exclusion](#record) | Both signs and every prime for the complete separated presentation. |
| argument | [Determinant inequalities](#binomial) | Measure thresholds including the cofactor loss. |
| argument | [Finite comparison](#finite) | The genuine degree-ten record and its separate cyclotomic completion. |
| argument | [Exterior-root count](#exterior) | Coefficient-independent lower bound at a fixed measure below the plastic number. |
| dependency | [Cyclic rank](Yin_C_G0904_v2.md#modular) | Modular kernel and determinant divisibility. |
| dependency | [Nonreversal estimate](Yin_C_G0904_v3.md#finite-field) | Uniform upper bound for linear-time ranks. |
| dependency | [Degree-ten competitor](../audits/literature/MRW08/Yin_U001.md#mrw08-u001) | Degree minima and the exterior Lehmer root. |
| dependency | [Smyth bound](../audits/literature/Smy71/Yin_U001.md#smy71-u001) | Measure of a nonreciprocal irreducible factor. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1291.md#finding) | Entire argument, constants, competitor, finite completion and exterior-root estimate. |

## Current assessment

[Selected decision](#decision-end-block-measure)
