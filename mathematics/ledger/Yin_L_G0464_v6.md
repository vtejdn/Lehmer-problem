---
author: Yin
---

# A resultant ceiling for nonunit inputs on the full odd trace grid

<a id="norm-ceiling"></a>
## A necessary cost bound for a shrinking shell

Use the [full odd grid and strict chamber](Yin_L_G0464_v5.md#odd-grid-product), with \(p=2n+1\) odd, \(Q=(t-a)B+C\), and \(P=z^{n+1}Q(z+z^{-1})\).
Set \(\Delta=|\operatorname{Res}(B,Q)|\), with no prescribed arithmetic type for \(C\).
Along any sequence with \(p\to\infty\) and \(1<M(P)\to1\), one necessarily has
\[
                   \limsup \Delta^{1/n}<2\exp(-2^{-22}).
\]
In particular an ensemble supported on \(\Delta^{1/n}\ge2\exp(-2^{-22})\) has a uniform gap for the positive whole measures in this chamber.
This follows for unbounded \(p\) by contradiction with the sequence statement, and for bounded \(p\) from the usual coefficient bound at bounded degree and measure.
Both real and nonreal exceptional trace roots are covered.
The [degree-20 example](../computations/programs/Yin_J_G0147/readme.md#unique-input) has \(\Delta=4313>2^9\).
It demonstrates why both the resultant and the radius of the shell matter when proposing a nonunit ensemble.
The ceiling permits norms between one and the displayed exponential rate.

<a id="weighted-product"></a>
## Exact product and its limiting density

Pass to a subsequence with a [limiting profile](Yin_L_G0464_v5.md#only-left-endpoint)
\(H_x=(t-x)^2/(t^2-4)\), \(x\in\{-2,-1,0,1,2\}\), and midpoint \(c_p\to-2\).
In the decomposition \(Q/B\to (z^{-1}-z)H_x=(t-2z)H_x\), take the fixed positive grid weight and integral polynomial
\[
                    w(t)=4-t^2,\qquad G(t)=-2w(t)H_x(t)=2(t-x)^2 .
\]
The polynomial \(w(t)tH_x(t)\) is integral as well.
The [exact moment argument](../claims/Yin_C_G0881_v1.md#moments) and [odd-grid quadrature](Yin_L_G0464_v5.md#five-cuts-and-original-profiles) give, for each fixed polynomial \(h\), eventual equality of the sums of \(h(b_j)w(b_j)r_j\) and \(h(b_j)G(b_j)\nu_j\).
With \(X_j=nw(b_j)(b_j-c_p)r_j>0\), the angular measures \(n^{-1}\sum X_j\delta_{\theta_j}\) therefore converge weakly to \(f(\theta)d\theta/\pi\), where
\[
          f(\theta)=(4-t^2)(t+2)(t-x)^2,\qquad t=2\cos\theta .
\]
Here \(n\nu_j=2(1-1/p)\sin^2\theta_j\) and \(0\le f\le256\).
Write \(\langle\,\cdot\,\rangle\) for the uniform angular mean on \([0,\pi]\) and \(\mathbb E_p\) for the uniform mean on the \(n\) nodes.
For each \(v\in[-2,2]\), one has \(\langle\log|t-v|\rangle=0\) by the unit-circle mean formula applied to \(z^2-vz+1\).
All logarithms here are integrable, so \(\langle\log f\rangle=0\).

Since \(B(2)=p\) and \(|B(-2)|=1\), one has \(\prod_j w(b_j)=p\).
The [midpoint product](Yin_L_G0464_v5.md#odd-grid-product) gives
\[
      \mathbb E_p\log X=\log(n/p)
        +\frac{\log\Delta+\log(p^2|B(c_p)|)}{n}.
\]
The factor \(1\le |B(c_p)|\le p\) contributes \(o(1)\) to the mean.
In particular weak convergence of \(\mathbb E_pX\) and the arithmetic-geometric mean bound keep \(\log\Delta/n\) bounded above on the subsequence.

<a id="quantitative-recovery"></a>
## A small logarithmic deficit forces exact integral moments

Suppose the asserted ceiling fails.
After subsequence selection, \(\liminf\mathbb E_p\log X\ge-\gamma\), where \(\gamma=2^{-22}\).
For fixed \(\epsilon>0\) set \(Y_j=X_j/(f(\theta_j)+\epsilon)\).
Weak convergence and equidistribution give
\[
 \limsup\mathbb E_p(Y-1-\log Y)
 \le \left\langle f/(f+\epsilon)\right\rangle-1
            +\langle\log(f+\epsilon)\rangle+\gamma .
\]
As \(\epsilon\downarrow0\) the right side tends to \(\gamma\), since \(f>0\) almost everywhere and \(\log f\) is integrable.
Also \(\lim\mathbb E_pY=\langle f/(f+\epsilon)\rangle\le1\).
Using \((y-1)^2\le2\max(1,y)(y-1-\log y)\), Cauchy–Schwarz and \(\max(1,Y)\le1+Y\) bounds \(\limsup\mathbb E_p|X-f|\) by \(2\|f\|_\infty\sqrt\gamma\le1/4\), upon letting \(\epsilon\downarrow0\).
Indeed \(|X-f|\le(\|f\|_\infty+\epsilon)|Y-1|+\epsilon\).

Put \(e_j=w(b_j)r_j-G(b_j)\nu_j\).
The quantities \(n(b_j-c_p)G(b_j)\nu_j\) converge uniformly to \(f(\theta_j)\) on this changing grid by the formula for \(n\nu_j\) and by \(c_p\to-2\).
Consequently \(\limsup\sum_j|(b_j-c_p)e_j|\le1/4\).
The first two moment differences vanish eventually by the exact moment identity above.
All cosine moments of the difference are integers because both rational functions \(wQ/B\) and \(GB_{n-1}/B\) have integral numerator and monic denominator.
The [integer recurrence](../claims/Yin_C_G0881_v1.md#integer-recurrence) applies once the weighted error is less than \(1/2\), and gives \(e_j=0\) at every node.
Hence \(\sum|w(b_j)r_j|\le\max_{[-2,2]}|G|\le32\), contradicting the [fixed-weight necessity](../claims/Yin_C_G0880_v2.md#statement) for \(1<M(P)\to1\).
