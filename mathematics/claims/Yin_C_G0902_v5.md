---
author: Yin
---

# Integral fractional linear functions of the Chebyshev unit

2026-11-24T19:48 UTC.

<a id="statement"></a>
## A measure bound from the common prime divisors

Use the [Chebyshev trace family](Yin_C_G0902_v1.md#minimum) with \(p=q+1,\ M=pq,\ L=2q+1\), and even \(n\ge4\) satisfying \(4^{n-1}\le2M\).
Write \(d_0=n-3,\ B=\mathbb Q(w)\), and \(K=\mathbb Q(T)\), with \(T>1\) and \(T+T^{-1}=2+w\).
For coprime integers \(a,b\) put
\[
                 Z=\frac{aT-b}{a-bT},\qquad A=ab,\quad k=a-b,\quad S=a+b .
\]
The denominator is nonzero since \(T\) is irrational.
If \(a=b\) or \(a=-b\) then \(Z=-1\) or \(1\), respectively.
If \(ab=0\) the output is \(T\) when \(b=0\) and \(T^{-1}\) when \(a=0\), with known [measure \(m(T)\sim\log M\)](Yin_C_G0902_v1.md#conjugates).
In what follows assume \(ab\ne0,\ a\ne\pm b\), and \(Z\) an algebraic integer.
Inversion \(\iota\) on \(K/B\) sends \(Z\) to \(Z^{-1}\), so \(Z\) is a unit, and the inverse fractional linear transformation gives \(\mathbb Q(Z)=K\).

Define \(E\) as the full divisor of \(|S|\) supported on the odd primes \(\ell\mid\gcd(S,L)\) for which \(1-2^{2n-1}\) is a square modulo \(\ell\), including the residue zero.
For all sufficiently large \(q\), with absolute implied constants, the following conclusions hold.

* If \(A>0\), then \(m(Z)\ge (n-1)\log(A/E^2)-O(1)\).
  When \(E=1\), integrality forces \(A\gg M k^2\) and \(m(Z)\ge(n-1)\log M-O(n)\).
  If also \(|k|=1\), the only possibilities for the unordered pair of positive coefficient magnitudes are \(\{q,q+1\}\).
  Every other such pair with \(E=1\) requires \(|k|\gg M^{(n-2)/2}\) and \(m(Z)\ge (n-1)^2\log M-O(n)\).
* If \(A<0\), then \(m(Z)>(\log M)/110\).
* Along any sequence of such inputs with \(q\to\infty\) and \(m(Z)\to0\), eventually \(A>0\) and \(|S|/E\in\{1,2\}\).

When \(L\) is a power of three, \(1-2^{2n-1}\equiv2\bmod3\), so \(E=1\) for every coefficient pair.
Thus on this entire subfamily no nonconstant rational fractional linear function of \(T\) taking algebraic integer values can supply positive measures tending to zero.
For general \(L\) the first conclusion controls the contribution of the prime divisors shared by the two parameter choices.

<a id="norm"></a>
## The norm of the denominator

The relevant denominator in \(B\) is \(D=k^2-Aw=(a-bT)(a-b/T)\).
The graph identity gives
\[
                      Z+Z^{-1}-2=S^2w/D .
\]
Since \(Z^{\pm1}\) are integral, the absolute value of \(N=N_{B/\mathbb Q}D\) divides \(S^{2n}|N_{B/\mathbb Q}w|\).
With \(C=C_{d_0}\) and \(H\) as in the [trace calculation](Yin_C_G0902_v3.md#statement), direct evaluation gives
\[
 \begin{split}
 N&=A^n H(k^2/A)=k^{2n-2} S^2+2(Mk^2-A)A^{n-1}C(k^2/A)\\
  &=S^2(k^{2n-2}-V)+V L^2 k^2,\qquad V=\tfrac12 A^{n-1}C(k^2/A).
 \end{split}
\]
Here \(S^2=k^2+4A\), \(4M+1=L^2\), and \(2V\) is an integer because \(\deg C=n-3\).

For any odd prime \(\ell\mid S\), both \(k,A\) are units modulo \(\ell\) by coprimality.
Also \(k^2/A\equiv-4\bmod\ell\) and \(C(-4)=-1\).
Thus \(V\) is an \(\ell\)-adic unit and
\[
                    V\equiv k^{2n-2}2^{-(2n-1)}\pmod\ell
\]
since \(A\equiv-k^2/4\) and \(n\) is even.
If \(\ell\nmid L\), this proves that \(\ell\nmid N\).
Suppose \(\ell\mid L\) and \(1-2^{2n-1}\) is a nonsquare modulo \(\ell\).
Put \(u=v_\ell(S),\ v=v_\ell(L)\).
Multiplying the second formula for \(N\) by the local unit \(2^{2n-1}/k^{2n-2}\), the coefficient of \(S^2\) is congruent to \(2^{2n-1}-1\) and the coefficient of \(L^2 k^2\) is congruent to one.
Both coefficients are units.
If \(u\ne v\), the smaller valuation determines the sum.
If \(u=v\), cancellation after dividing by \(\ell^{2u}\) would express \(1-2^{2n-1}\) as the square of the ratio of two nonzero residues.
Hence \(v_\ell(N)=2\min(u,v)\) in both cases.
In particular at \(\ell=3\mid S,L\) one has \(V\equiv-1\bmod3\), and the nonsquare condition holds for every even \(n\).

If \(S\) is even, \(a,b\) are odd and \(k\) is even.
At the [unique dyadic place of \(B\)](Yin_C_G0902_v3.md#two), \(w\) has valuation one, \(2\) has valuation \(n\), and \(A\) is a unit.
Therefore \(D\) has valuation one, so \(v_2(N)=1\).
If \(S\) is odd, the dyadic part is already bounded by that of \(N_{B/\mathbb Q}w=-2(2n-5)\).
At odd primes dividing \(E\) we retain the original norm divisibility, and primes outside \(S\) also satisfy that divisibility.
The remaining shared primes contribute at most the square of the part of \(|S|\) coprime to \(E\).
Consequently
\[
                  |N|\le |N_{B/\mathbb Q} w|\,S^2 E^{2n-2}.                \tag{1}
\]

<a id="places"></a>
## The real and nonreal embeddings

Assume \(A>0\).
For every negative real conjugate \(w_i\), one has \(|k^2-Aw_i|\ge A|w_i|\).
The two nonreal conjugates \(\xi,\bar\xi\) satisfy \(|\operatorname{Re}\xi|=O(n)\) and \(|\operatorname{Im}\xi|^2\ge2M-8\) by the [first two trace moments](Yin_C_G0902_v1.md#conjugates).
As \(n=O(\log M)\), each gives \(|k^2-A\xi|\ge A|\operatorname{Im}\xi|\ge\tfrac12 A|\xi|\) uniformly for large \(M\).
Thus the product of the \(n-1\) denominator factors away from \(w\) is at least \(\tfrac14 A^{n-1}|N_{B/\mathbb Q}w|/w\).
From (1) it follows that
\[
      |k^2-Aw|\le\frac{4S^2w E^{2n-2}}{A^{n-1}},\qquad
      |Z+Z^{-1}-2|\ge\tfrac14(A/E^2)^{n-1}.                             \tag{2}
\]
At the distinguished real place, \(|Z+Z^{-1}-2|\le4\max(|Z|,|Z|^{-1})\).
Both values are conjugate moduli, giving \(m(Z)\ge(n-1)\log(A/E^2)-\log16\).

For \(E=1\), dividing the first inequality of (2) by \(k^2\ge1\) gives \(|1-Aw/k^2|\le20w\) since \(S^2=k^2+4A\) and \(A\ge1,\ n\ge4\).
Thus \(A\gg M k^2\) by \(w=M^{-1}+O(M^{-n})\), and the measure estimate follows.
For \(|k|=1,\ E=1\) there is also an exact test.
Here \(A>0\) has the form \(v(v+1)\) for a positive integer \(v\), and \(S^2=4A+1\).
At every odd prime dividing \(S\) the preceding calculation gives \(v_\ell(N)\le2v_\ell(S)\).
The relation \(D=1-Aw\) gives \(D\) coprime to \(w\) in \(\mathcal O_B\).
Hence integrality of \(S^2 w/D\) implies \(D\mid S^2\), so \(N\) is supported on primes dividing \(S\).
Consequently \(|N|\le S^2\).
If \(A\ne M\), the integer \(|M-A|\ge1\), and \(C(1/A)\ge2n-5\ge3\) by the hyperbolic Chebyshev identity.
The perturbation \(2(M-A)A^{n-1}C(1/A)\) in \(N=S^2+2(M-A)A^{n-1}C(1/A)\) has modulus greater than \(2S^2\), since \(A=v(v+1)\ge2\), \(n\ge4\).
This contradicts \(|N|\le S^2\), so \(A=M\) and \(v=q\).
The two resulting transformations give \(Y\) and \(Y^{-1}\), known units.

For the remaining positive pairs with \(E=1\), the preceding estimate \(|1-Aw/k^2|\le20w\) gives \(A/(Mk^2)=1+O(1/M)\).
Since \(n=O(\log M)\), we have \(A^{n-1}\gg(Mk^2)^{n-1}\), uniformly.
The first inequality in (2) now gives
\[
       |A/k^2-1/w|\le4(S^2/k^2)/A^{n-1}
                  \ll M^{2-n}|k|^{-2(n-1)} .
\]
Also \(1/w-M=O(M^{2-n})\), so \(|A-Mk^2|\ll k^2 M^{2-n}\).
The integer on the left cannot vanish unless \(|k|=1\), since \(\gcd(A,k)=1\).
This gives the stated lower bound for \(|k|\), then \(A\gg M^{n-1}\) and the stronger measure estimate follows from (2).

For \(A<0\) set \(s=k/S\), \(t=(T-1)/(T+1)\).
One has \(|s|>1\), \(t=O(M^{-1/2})\), and \(Z=(s+t)/(s-t)\).
In particular \(Z>0\) and \(|Z-1|=O(M^{-1/2})\), uniformly in \(a,b\).
The [endpoint estimate](Yin_C_G0902_v4.md#division) applies directly.
In detail the monic minimum has degree \(2n\), and either \(Z\) or its reciprocal lies inside the unit disk at distance \(O(M^{-1/2})\) from \(1\).
Integration of its derivative to \(1\) gives \(\log\|P\|_{\mathbb T}\ge\tfrac12\log M-O(\log(2n))\).
The upper bound proved there from the finite circle estimate is incompatible with \(m(Z)\le(\log M)/110\), proving the assertion.

<a id="shrinking"></a>
## Prime support in a shrinking sequence and other fractional linear maps

Suppose \(m(Z)\to0\) along \(q\to\infty\).
Then \(A>0\) eventually, \(n\to\infty\) by bounded-degree finiteness, and every conjugate modulus of \(Z\) tends uniformly to one, using reciprocity for those inside the circle.
Choose \(\zeta=\sigma T\) as in [the two-place calculation](Yin_C_G0902_v1.md#products), so \(r=|\zeta|\to\infty\).
The identity
\[
         |\sigma Z|^2-1=\frac{(a^2-b^2)(r^2-1)}{|a-b\zeta|^2}
\]
also applies on exchanging \(a,b\), which replaces \(Z\) by \(1/Z\).
We may assume \(R=|a/b|\ge1\).
The right side is at least \((R^2-1)(r^2-1)/(R+r)^2\).
If \(R\ge r\), this is unbounded as \(r\to\infty\).
If \(1\le R<r\), it is bounded below by \((R^2-1)(1-r^{-2})/4\).
Thus \(R\to1\), and \(|S|/\sqrt A\to2\).
By (2) one has \(A/E^2\le (16\exp(m(Z)))^{1/(n-1)}\), so \(|S|/E\le2+o(1)\).
This is a positive integer, proving the third assertion.

Finally, for a nonconstant \(f\in\mathbb Q(X)\) of degree one, \(f(T)\) generates \(K\).
If \(f(T)\iota f(T)=1\), then \(f(X)f(1/X)=1\) identically, since clearing denominators gives degree at most two and \(T\) has degree \(2n\).
Writing \(f(X)=(aX+b)/(cX+d)\) equates \(ab=cd,\ a^2+b^2=c^2+d^2\).
Therefore \(c+d=\pm(a+b)\) and \(c-d=\pm(a-b)\), forcing the denominator coefficient pair to be the numerator pair or its swap up to overall sign.
Nonconstancy leaves exactly the signed transformations treated above, after scaling to coprime integers.
If \(f(T)\) is integral and its absolute height tends to zero, it has relative norm one eventually by the [neutral-place estimate](Yin_C_G0345_v75.md#statement), since \((n-3)/n\ge1/4\).
Positive total measures tending to zero imply this height condition.
This proves the exclusion for all such fractional linear maps on the powers-of-three branch.

## Assessment history

### Decision integral-fractional-linear-images

| Field | Value |
| --- | --- |
| date | 2026-11-24T19:57 |
| status | proved |
| reason | Denominator norm valuations restrict shared primes. The two archimedean places then bound the actual transformed measure, and the reciprocal-norm identity classifies potential rational maps on a shrinking sequence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform measure constraints on integral fractional linear functions on the Chebyshev family and exclusion along the full ternary branch. |
| argument | [norm](#norm) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [places](#places) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [shrinking](#shrinking) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0902_v1.md#conjugates) | The trace polynomial, trace roots and field degrees. |
| dependency | [Input](Yin_C_G0902_v1.md#products) | The original denominator norm and exterior place estimates. |
| dependency | [Input](Yin_C_G0902_v3.md#two) | The normalized dyadic valuations. |
| dependency | [Input](Yin_C_G0902_v4.md#division) | The endpoint smallness estimate for a generating real value. |
| dependency | [Input](Yin_C_G0345_v75.md#statement) | The relative-norm restriction from the neutral places. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1070.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-integral-fractional-linear-images)
