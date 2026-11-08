---
author: Yin
---

# An explicit Chebyshev prefix test and the interior limiting profiles

<a id="statement"></a>
## Interior limits and a finite coefficient test

Keep the original grid, monic integer lift and strict negative-to-positive transition with the left endpoint sign of [v1](Yin_C_G0881_v1.md#statement).
Its five limiting cuts and degree-three classification in a strict shrinking shell continue to apply.
The following refinements specify the interior possibilities and a finite test.

* If the limiting cut is interior, write \(c\in\{-1,0,1\}\) for that cut and \(t=z+z^{-1}\).
  The only possible coefficient limits of \(P\) are
  \[
     \frac{t-c}{t-2},\qquad \frac{t-2}{t-c},\qquad
     \frac{(t-r)^2}{(t-2)(t-c)},\quad
        r\in\{-2,-1,0,1\}\setminus\{c\}.
  \]
  This is a necessary list in the positive shrinking shell.
* For every \(d\ge8192\), agreement with \(P_*=(1+z^2)/(1-z)\) through coefficient index \(2047\) already forces \(Q=t(B+U_{d-2}(t/2))\), and hence \(M(P)=1\), without any upper bound on \(M(P)\).
  Agreement here includes the constant coefficient, so exactly 2048 prescribed coefficients are being tested.

<a id="interior-list"></a>
## Reduced denominators at an interior cut

By [v1](Yin_C_G0881_v1.md#five-cuts) only the first quotient in the list is possible if \(c\) is not a pole.
If it is a pole, write the reduced monic denominator as \((t-c)(t-2)^a(t+2)^b\) with \(a,b\in\{0,1\}\).
The numerator is monic of degree \(1+a+b\), has all roots in \([-2,2]\), avoids the poles and has constant sign \((-1)^{a+1}\) on the interior away from its zeros.
With \(a=b=0\) it must be \(t-2\).
With \(a=0,b=1\) the negative monic quadratic on the interval would need roots at both endpoints, contradicting reducedness at \(-2\).
With \(a=b=1\) all three roots are interior and constant sign is impossible.
With \(a=1,b=0\) the nonnegative quadratic must have a double root in \([-2,2)\), since a simple interior root changes sign.
This root is a rational algebraic integer and cannot be \(c\).
These four cases give the stated list.

The first profile occurs for exact neutral inputs at all three cuts.
Choose odd \(d\ge5\) with \(3\nmid d\), and a fixed positive even \(k<d\) coprime to \(d\), for instance \(k=2\).
The polynomial
\[
 P(z)=(1-cz+z^2)\frac{(1-z^{d-k})(1-z^{d+k})}{(1-z)^2}
\]
is a monic reciprocal cyclotomic product of degree \(2d\).
Its coefficient limit as \(d\to\infty\) with fixed \(k\) is \((t-c)/(t-2)\).
At the internal grid values \(\zeta=e^{\pi i j/d}\) its value is \((t-c)|1-\zeta^{d-k}|^2/(t-2)\).
Here \(\gcd(d-k,2d)=1\), and the nodes avoid \(-1,0,1\) in the trace variable.
Since \(r_j=-\nu_j P(\zeta)\), where \(\nu_j=2\sin^2(\pi j/d)/d\), the signs change strictly at \(c\).
Finally \(Q(-2)/B(-2)=-P(-1)/d=-(2+c)/d<0\).
These controls have measure exactly one.

<a id="finite-filter"></a>
## A positive polynomial test for the prescribed coefficients

In what follows \(c_d\) is the angular midpoint of the actual transition gap.
Use \(n=d-1\), \(b_i=2\cos\theta_i\) with \(\theta_i=\pi i/d\), and \(X_i=n(b_i-c_d)r_i>0\).
For mean over \(1\le i\le n\) write \(\mathbb E_d\), and for continuous angular mean on \([0,\pi]\) write \(\langle\cdot\rangle\).
Let \(f(\theta)=2\sin^2\theta\, b^2=1-\cos(4\theta)\), \(b=2\cos\theta\).
The exact moments from [the central comparison](../ledger/Yin_L_G0464_v3.md#fourth-root) apply through degree \(2045\) for the signed measure \(\sum r_i\delta_{b_i}\).
On this polynomial space the moments agree with \(b\,d\nu\), where \(d\nu=\sqrt{4-b^2}\,db/(2\pi)\).
The [odd quadrature](../ledger/Yin_L_G0464_v3.md#cut-localization) with \(h=1023\) gives \(|c_d|\le2\sin(\pi/1024)<0.007\).
The angular-midpoint product in [v1](Yin_C_G0881_v1.md#saturation) gives \(\mathbb E_d\log X_i\ge-\log2\), since \(2\log d\ge n\log(d/n)\).

Set \(m=512\) and
\[
 S(u)=\sum_{j=0}^{m-1}(1-j/m)u^j,\qquad
 K(u)=\frac1m\sum_{j=1}^m u^j,\qquad
 h_m(\theta)=2|S(e^{4i\theta})|^2 .
\]
Then \((1-u)S=1-K\) and \(h_m f=|1-K|^2\).
On the circle \(2\operatorname{Re}S=1+m^{-1}|\sum_{j=0}^{m-1}u^j|^2\), hence \(h_m\ge1/2\).
As a function of \(b\), \(h_m\) is an even polynomial of degree at most \(4(m-1)=2044\).
For \(Y_i=h_m(\theta_i)X_i\), moment agreement is therefore sufficient for the exact identity
\[
       \mathbb E_d Y_i=\int h_m(b)(b-c_d)b\,d\nu
          =\langle h_m f\rangle=1+1/m .
\]
The term odd in \(b\) integrates to zero and the angular mean of \(|K|^2\) is \(1/m\).

<a id="finite-product"></a>
## A uniform bound for the finite grid product

All zeros \(\beta\) of \(S\) have \(|\beta|\ge m/(m-1)\).
Indeed the coefficients of \(S(mu/(m-1))\) are positive and nonincreasing, with constant one.
Multiplication by \(1-u\) gives one minus a sum of positive powers of \(u\) with nonnegative coefficients of sum one, which cannot vanish inside the open unit disk.

Put \(N=d/\gcd(d,2)\ge4096\).
The numbers \(e^{4\pi i j/d}\) for \(0\le j<d\) range equally over the \(N\)-th roots of unity.
Using \(S(0)=1\) gives the full-grid mean
\[
 \frac1d\sum_{j=0}^{d-1}\log h_m(\pi j/d)
 =\log2+\frac{2}{N}\sum_{S(\beta)=0}\log |1-\beta^{-N}|
 \ge\log2-\frac{2(m-1)}{2000N}.
\]
Indeed \(|\beta|^{-N}\le e^{-N/m}\le e^{-8}<1/2500\), and \(-\log(1-e^{-8})<1/2000\).
Removing \(j=0\), where \(S(1)=(m+1)/2\), gives \(\mathbb E_d\log h_m\ge\log2-1/600\).
For the constants use \(d/n<1.001\), \(2(m-1)/N<1/4\), \(2\log((m+1)/2)<12\) and \(n\ge8191\).

It follows that \(\mathbb E_d(Y_i-1-\log Y_i)\le1/512+1/600<1/250\).
The Cauchy–Schwarz bound from [v1](Yin_C_G0881_v1.md#saturation) now gives \(\mathbb E_d|Y_i-1|<0.127\).
Since \(N\ge m\), the full-grid mean of \(|K|^2\) is \(1/m\) by character orthogonality.
Removing \(j=0\), where \(K(1)=1\), only lowers this mean.
Thus \(\mathbb E_d|1-h_m f|\le2/\sqrt m+1/m<0.091\) and
\[
           \mathbb E_d |X_i-f(\theta_i)|
              \le 2\big(\mathbb E_d|Y_i-1|+\mathbb E_d|1-h_m f|\big)<0.436 .
\]

<a id="finite-conclusion"></a>
## Exact recovery on this grid

Set \(e_i=r_i-b_i\nu_i\).
The difference between \(f(\theta_i)\) and \(n(b_i-c_d)b_i\nu_i\), averaged in absolute value, is at most \(2/d+|c_d|\sum_i|b_i|\nu_i\).
The latter sum is at most one by Cauchy–Schwarz and the semicircle moments of degrees zero and two on this grid.
Consequently \(\sum_i|(b_i-c_d)e_i|<0.436+2/d+0.007<1/2\).
The first two moments of \(e_i\) vanish.
The [integer recurrence](Yin_C_G0881_v1.md#integer-recurrence) therefore forces every \(e_i=0\).
The coefficient of \(z\) fixes \(a=-1\), so the original rational function and its monic numerator equal the neutral comparison.

## Assessment history

### Decision explicit-prefix

| Field | Value |
| --- | --- |
| date | 2026-11-08T03:12 |
| status | proved |
| reason | A separate whole-proof review verified the interior list, each finite-grid estimate and the resulting exact recovery. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Explicit prefix and interior profiles](#statement) | The interior necessary list and the 2048-coefficient implication for every trace degree at least 8192. |
| argument | [Interior profiles](#interior-list) | All reduced numerator and denominator choices permitted at an interior cut. |
| argument | [Positive finite test](#finite-filter) | Angular localization, admissible moment degrees and exact arithmetic mean. |
| argument | [Grid product](#finite-product) | Geometric mean, finite constants and mean absolute error. |
| argument | [Exact recovery](#finite-conclusion) | A weighted error below one half determines the entire integral polynomial. |
| dependency | [Five-cut theorem](Yin_C_G0881_v1.md#statement) | The limiting rational functions and integer recurrence used here. |
| review | [Independent finite and interior finding](../audits/reviews/Yin_R_G1106_v2.md#finite-prefix-review) | Both stated refinements and their precise dependencies. |

## Current assessment

[Selected decision](#decision-explicit-prefix)
