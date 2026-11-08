---
author: Yin
---

# Locating a nonreal trace pair relative to a moving residue sign change

Date: 2026-11-08.
For Yin's [Lehmer objective](../tasks/Yin_T_G0001_v1.md#contract), this derivation tests the [moving sign construction](Yin_L_G0462_v2.md#moving-sign-test) on the input polynomial's own trace grid.
A delegated AI agent derived and checked the partial fractions, endpoint estimates and finite product inequalities; no independent review of this exploration is asserted.

<a id="positive-resolvent"></a>
## A positive measure from the actual nonreal pair

Let \(B\) be monic of degree \(n\ge2\) with simple real roots \(-2<b_1<\cdots<b_n<2\), and let \(Q\) be real monic of degree \(n+1\).
Write \(Q/B=t-a+\sum_i r_i/(t-b_i)\), let \(1\le k<n\), and suppose \(r_i<0\) for \(i\le k\), \(r_i>0\) for \(i>k\) and \(Q(-2)/B(-2)<0\).
Each same-sign gap contains a zero, and so does \((-2,b_1)\), since \(Q/B\) tends to positive infinity on the left of \(b_1\).
These are \(n-1\) distinct real zeros.
Assume that the two other zeros are a nonreal pair \(q=x+iy,\bar q\), with \(y>0\).
For the lift \(P(z)=z^{n+1}Q(z+z^{-1})\), let \(\lambda+\lambda^{-1}=q\) with \(\rho=|\lambda|>1\).
The real zeros cost zero and the pair costs exactly \(M(P)=\rho^2\), where \(M\) denotes multiplicative Mahler measure.

For any separator \(b_k<c<b_{k+1}\), cancelling the pair gives
\[
 H(t)=\frac{(t-c)Q(t)}{(t-q)(t-\bar q)B(t)}
     =1+\sum_{i=1}^n\frac{w_i}{t-b_i},\qquad
 w_i=\frac{(b_i-c)r_i}{|b_i-q|^2}>0.
\]
Indeed, the displayed numbers are the residues at the only possible poles, and both sides tend to one at infinity.
Comparison at infinity and evaluation at \(-2\) give
\[
 W:=\sum_i w_i=2x-a-c,\qquad
 0<\sum_i\frac{w_i}{2+b_i}=1-H(-2)<1.
\]
The upper inequality uses the original strict endpoint sign and \(-2-c<0\); positivity of the sum gives the lower inequality.
In particular \(W<4\), since every \(2+b_i<4\).
The equality \(H(c)=0\) also gives \(\sum_i r_i/|b_i-q|^2=1\).

<a id="moving-gap-mesh"></a>
## Two mesh tests for unbounded variation

Here take the arithmetic midpoint \(c=(b_k+b_{k+1})/2\) and let \(\Delta=b_{k+1}-b_k\).
The identity \(|b_i-q|^2=(b_i-c)^2+2(b_i-c)(c-x)+|q-c|^2\) gives
\[
 V:=\sum_i|r_i|
 \le (4+2|c-x|)W+|q-c|^2\sum_i\frac{w_i}{|b_i-c|}.
\]
Because \(|b_i-c|\ge\Delta/2\), the last sum is at most \(2W/\Delta\).
It is also at most \(1+2(2+c)/\Delta\): divide \((2+b_i)/|b_i-c|\le 1+2(2+c)/\Delta\) by \(2+b_i\) and sum with weights \(w_i\).

On a fixed exterior ellipse bound \(\rho\le\rho_0\), one has \(|q|\le\rho_0+\rho_0^{-1}\).
Thus \(V\to\infty\) implies both \(|q-c|/\sqrt{\Delta}\to\infty\) and \(|q-c|^2(1+2(2+c)/\Delta)\to\infty\).
For integral \(B,Q\), [C880](../claims/Yin_C_G0880_v1.md#statement) requires \(V\to\infty\) on every sequence of positive whole measures with \(m(P)=\log M(P)\to0\), so these are necessary tests on that same sequence.

For the Chebyshev grid \(d=n+1\), \(B(t)=U_{d-1}(t/2)\), the increasing enumeration is \(b_i=-2\cos(\pi i/d)\).
If the number \(k\) of negative poles stays bounded while \(d\) grows, then \(2+c=O((k+1)^2/d^2)\) and \(\Delta=4\sin((2k+1)\pi/(2d))\sin(\pi/(2d))\) has order \((2k+1)/d^2\).
Consequently the endpoint estimate bounds \(V\) uniformly on these fixed-ellipse inputs even when the pair stays far from the cut.
For a cut in a compact interior subinterval, \(\Delta\) has order \(1/d\), so \(V\to\infty\) requires \(\sqrt d\,|q-c|\to\infty\).
The one-sided endpoint bound uses the left endpoint sign, not a symmetric estimate at \(2\).

<a id="angular-midpoint-resultant"></a>
## An arithmetic lower bound at the angular midpoint

Keep the Chebyshev grid, now require \(Q\in\mathbb Z[t]\), and choose the angular midpoint \(c=-2\cos((k+\tfrac12)\pi/d)\) in the same gap.
This choice need not equal the arithmetic midpoint used above.
Then \(|B(c)|=1/\sin((k+\tfrac12)\pi/d)\ge1\) by the sine formula for \(U_{d-1}\).
At \(b_i\), one has \(r_i=Q(b_i)/B'(b_i)\) and \(|B'(b_i)|=d/(2\sin^2(\pi i/d))\).
Using \(\prod_{i=1}^{d-1}\sin(\pi i/d)=d/2^{d-1}\), from evaluating \((z^d-1)/(z-1)\) at one by its roots, yields the exact product
\[
 \prod_i w_i=\frac{d^2}{(2d)^n}
       \frac{|B(c)|\,|\operatorname{Res}(B,Q)|}{|B(q)|^2},\qquad n=d-1.
\]
The resultant is a nonzero integer because \(B,Q\) are monic integral and all residues are strict.
The Chebyshev identity \(B(q)=\sum_{h=0}^{d-1}\lambda^{d-1-2h}\) gives \(|B(q)|\le d\rho^{d-1}\).
Arithmetic-geometric mean therefore gives
\[
 2x-a-c=W\ \ge n\Big(\prod_i w_i\Big)^{1/n}
        \ge \frac{d-1}{2dM(P)}.
\]
In particular \(W\ge\tfrac12-o(1)\) if \(d\to\infty\) and \(M(P)\to1\), independently of the choice of transition gap.

One can use the same product to test a second original coefficient.
Put \(J=\sum_i b_iw_i\) and \(K=\sum_i r_i\), which is an integer because it is the coefficient of \(t^{-1}\) in the expansion of \(Q/B\) at infinity.
Comparison of the coefficients of \(t^{-2}\) in \(H\) gives \(J=K+ac-|q|^2+2xW\).
For real \(s\), every \(1-s b_i+s^2\) is positive and
\[
 \prod_i(1-s b_i+s^2)=\sum_{h=0}^{d-1}s^{2h}\ge1,
\]
by the Chebyshev identity \(s^{d-1}B(s+s^{-1})\), with the value at zero obtained by continuity.
Applying arithmetic-geometric mean to \((1-s b_i+s^2)w_i\) and then taking \(s=J/(2W)\) yields
\[
 W-\frac{J^2}{4W}\ \ge n\Big(\prod_i w_i\Big)^{1/n}
                  \ge\frac{d-1}{2dM(P)}.
\]
These inequalities reject proposed root locations and residue distributions without approximating the cut by a fixed rational point.
They neither construct integral candidates nor exclude a moving transition with unbounded variation and a pair satisfying these tests.
