---
author: Yin
---

# The degree-eight seeds left by the coefficient norm bound at width eight

<a id="census"></a>
## One octic survives the norm estimate

Among monic irreducible reciprocal octics of multiplicative Mahler measure \(1<M\le2\), the [fixed-seed norm bound](../../../../../claims/Yin_C_G0345_v411.md#statement) at row degree \(b=8\) excludes every seed at the cutoff \(H\le2^p\) for sufficiently large exponents, with one exception up to \(X\mapsto -X\).
The exception and its transform are
\[
               X^8-X^5-X^4-X^3+1,\qquad X^8+X^5-X^4+X^3+1 .
\]
For their common measure \(M\), the exact comparisons give
\[
                         M^{22}<2^8,\qquad M^{45}>2^{16}.
\]
The first inequality puts the norm lower rate strictly below \(\log 2\) for this seed.
The second puts the improved rate \((45/16)\log M\) in the [signed-row ratio argument](../../../../../ledger/Yin_L_G0462_v252.md#ratio) strictly above \(\log2\).

Let \(g\) be the number of roots outside the unit circle.
The enumeration gives 54 seeds up to sign, with \(g=1\) for 23 seeds and \(g=2\) for 31.
For \(h=\log M\) and \(D=\sum_{i<j}|\log|\alpha_i|-\log|\alpha_j||\), reciprocity pairs the positive and negative log moduli, and both groups have total absolute log modulus \(h\).
Pairs of opposite sign contribute \(2gh\), and pairs containing one zero contribute \(2(8-2g)h\).
Consequently \(D\ge2(8-g)h\), with equality for \(g=1\).
At width eight the C411 rate \((2D-6h)/8\) is therefore at least \((26-4g)h/8\).
The integer comparison \(M^{26-4g}>2^8\) excludes 22 of the 23 seeds with \(g=1\) and all 31 with \(g=2\).
There is no numerical onset for the exponent \(p\) in this conclusion.

<a id="algorithm"></a>
## Newton sums, factors and measure comparisons

Write \(P=X^8+aX^7+bX^6+cX^5+dX^4+cX^3+bX^2+aX+1\).
The program chooses \(a\ge0\) and \(c\ge0\) when \(a=0\), giving one representative even for polynomials fixed by the sign change.
For \(s_k=\sum_i\alpha_i^k\), a necessary bound at \(M\le2\) is
\[
                       |s_k|\le6+M^k+M^{-k}\le6+2^k+2^{-k}.
\]
Indeed, choose one root from each inverse pair with modulus \(e^{t_j}\ge1\), so \(\sum_jt_j=\log M\).
The triangle inequality gives \(|s_k|\le \sum_j2\cosh(kt_j)\); the sum increases when two nonnegative arguments are replaced by their sum and zero, since \(\cosh(x+y)-\cosh(x)-\cosh(y)+1\ge0\).
This argument also applies to repeated roots and to nonreal exterior roots.
The integral \(s_k\) therefore has \(|s_k|\le6+2^k\).
At \(k=1,2,3,4\), Newton's identity \(s_k=-k c_k-\sum_{j=1}^{k-1}c_js_{k-j}\), where \(c_j=[X^{8-j}]P\), gives the full integer interval for the next coefficient.
These four tests leave 9,878 tuples, and testing \(5\le k\le16\) leaves 1,504.

For a monic integer polynomial \(F=\sum_{j=0}^d f_jX^{d-j}\), one Graeffe step replaces its roots by their squares and has descending coefficient \(g_j=\sum_i(-1)^if_if_{2j-i}\), taking missing coefficients as zero.
This follows by expanding \((-1)^d F(\sqrt X)F(-\sqrt X)\).
Every iterate satisfies the elementary coefficient bound and the circle mean-square bound
\[
          \max_j |f_j|/\binom dj\ \le\ M(F)\ \le\ \|F\|_2
                       \ \le\ 2^d M(F).
\]
The middle inequality follows from Jensen's inequality for the circle integral of \(\log|F|\) and Parseval's identity.
To compare \(M(F)^u\) with an integer \(B>1\), at step \(s\) compare the two bounds on \(M(F_s)^u\) with \(B^{2^s}\) by raising integers to positive powers.
If equality does not hold, the bounded multiplicative loss on each iterate becomes negligible after taking its \(2^s\)-th root, so one of the tests terminates the loop.
All tested input polynomials are monic integer unit polynomials.
Their exterior roots are closed under complex conjugation, so \(M(F)\) is the absolute value of a real product of algebraic units, itself an algebraic unit up to sign.
Thus \(M(F)^u\) cannot equal the nonunit integer \(B\).

The exact cap \(M\le2\) leaves 276 octics.
Any reducible one has a monic integral factor of degree \(d\le4\), constant coefficient \(\pm1\) and measure at most two.
The program generates all such possible factors using \(|f_j|\le2\binom dj\) and the same exact measure test, then uses monic integer division.
Of the 58 irreducible octics, four have every root on the circle and are cyclotomic by Kronecker's theorem.
For the exterior count the trace polynomial is
\[
             T(S)=S^4+aS^3+(b-4)S^2+(c-3a)S+d-2b+2 .
\]
Irreducibility excludes repeated trace roots and the endpoints \(\pm2\).
Each real trace strictly inside \((-2,2)\) yields two circle roots and each remaining trace gives one exterior root, so \(g=4-\#\{S\in(-2,2):T(S)=0\}\).
The program obtains this number by rational Sturm division at the two endpoints.

<a id="reproduction"></a>
## Reproducing the full list

Run the [standard-library Python program](octic.py) from the repository root.
It reuses monic division and the Newton power sums from the [sextic program](../../census.py) and requires no previously generated output.

~~~text
python mathematics/computations/programs/Yin_J_G0178/versions/v2/octic.py
~~~

Python 3.14.3 produced the [stage counts and all 54 nontorsion seeds](../../../../outputs/Yin_J_G0178/versions/v2/results.json), with the exterior count, tested exponent and cutoff comparison for each.
