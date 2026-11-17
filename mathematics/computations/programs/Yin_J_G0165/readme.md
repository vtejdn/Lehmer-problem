---
author: Yin
---

# The three full interlacing inverse images of Mahler measure one

<a id="zero-measure-presentations"></a>
## All presentations modulo integer translation

For [Yin's Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract), this computation tests measure one for the [full interlacing inverse polynomials](../../../claims/Yin_C_G0345_v122.md#statement) with a monic irreducible integral source \(S\) of degree at least two and a map \(g=A/B\) other than an integer translation.
The three rows give every presentation up to replacing \(g\) by \(g+n\) and \(S(Y)\) by \(S(Y-n)\) for the same \(n\in\mathbb Z\).
Both the maximum rational map degree and the maximum full polynomial degree are attained on every row, at two and eight respectively.

| Source \(S(Y)\) | Map \(g(X)\) | \(g(-2)\) | \(g(2)\) | Full polynomial |
| --- | --- | --- | --- | --- |
| \(Y^2-Y-1\) | \(X-1/(X+1)\) | \(-1\) | \(5/3\) | \(\Phi_{30}\) |
| \(Y^2-Y-1\) | \(X+1-1/(X-1)\) | \(-2/3\) | \(2\) | \(\Phi_{15}\) |
| \(Y^2-2\) | \(X-1/X\) | \(-3/2\) | \(3/2\) | \(\Phi_{24}\) |

Translating the second row by \(n=-1\) gives the representative with source \(Y^2+Y-1\) used in the [analytic classification](../../../claims/Yin_C_G0345_v123.md#statement).
The computation contributor checked the bounded search below and the complete cyclotomic factor of every accepted map.

<a id="pole-bound"></a>
## A finite pole bound from the source span

The [conductor reduction](../../../claims/Yin_C_G0345_v123.md#sources) gives the two displayed source representatives, a monic denominator \(B\), and total pole mass one.
Write \(p=\deg B\ge1\), \(g=X+c-R/B\), and \(R/B=\sum_{i=1}^p w_i/(X-b_i)\) with \(w_i>0\) and \(\sum_i w_i=1\).
The monic division makes \(c\) integral and \(R\) a monic integer polynomial of degree \(p-1\).
Every real fiber has one root between consecutive poles and one on each outer branch.
Measure one places all inverse traces in \([-2,2]\), hence every pole lies strictly inside this interval.
For the extreme source roots \(d_-,d_+\) and span \(D=d_+-d_-\), the two outer branches give
\[
 g(-2)\le d_-,\qquad g(2)\ge d_+,\qquad
 \sum_i\frac{4w_i}{4-b_i^2}=4-g(2)+g(-2)\le4-D .
\]
Also \(g(-2)>-2+c\) and \(g(2)<2+c\), which give \(c\in\{0,1\}\) for \(Y^2-Y-1\) and \(c=0\) for \(Y^2-2\).

Write \(b_i=2\cos\theta_i\), \(0<\theta_i<\pi\).
The polynomials \(V_j(2\cos\theta)=\sin((j+1)\theta)/\sin\theta\) are monic and integral by the recurrence \(V_0=1,V_1=X,V_{j+1}=XV_j-V_{j-1}\).
For \(0\le j<p\), \(\sum_i w_i V_j(b_i)^2\) is positive because \(V_j\) cannot vanish at all \(p\) distinct points.
It is an integer because the expansion of \(R/B\) at infinity has integral coefficients \(\sum_iw_i b_i^h\).
Thus each such sum is at least one.
The nonnegative Fejér sum
\[
 1+2\sum_{l=1}^p (1-l/(p+1))\cos(2l\theta)
 =\frac1{p+1}\left|\sum_{h=0}^p e^{2ih\theta}\right|^2
\]
gives \(\sum_{l=1}^p(1-l/(p+1))\sin^2(l\theta)\le(p+1)/4\).
Weight the preceding integer bounds by \(1-l/(p+1)\) with \(j=l-1\), sum, and apply this inequality at each pole.
It follows that
\[
 \frac p2\le\frac{p+1}{4}\sum_i\frac{w_i}{\sin^2\theta_i}
 \le\frac{p+1}{4}(4-D).
\]
Thus \(p\le(4-D)/(D-2)\), giving \(p\le7\) for \(D=\sqrt5\) and \(p\le1\) for \(D=2\sqrt2\).
These bounds determine the search ranges without using the analytic single-pole conclusion.

<a id="enumeration"></a>
## Enumeration by primitive angles

The rational function \(R/B\) decreases from \(+\infty\) to \(-\infty\) in each open pole gap, so \(R\) has one simple zero there and no others.
Conversely, monic \(B,R\) of consecutive degrees with these strict interlacing roots give positive residues \(R(b_i)/B'(b_i)\) by their signs.
Their sum is one by monicity.
Both polynomials are squarefree with all roots in \((-2,2)\), including \(R=1\) at \(p=1\).
For either polynomial \(H\), [Kronecker's theorem](../../../audits/literature/Smy08/Yin_U001.md#smy08-u001) applied to \(z^{\deg H}H(z+z^{-1})\) gives a product of distinct cyclotomics of orders \(n>2\).
Thus \(H\) is a product of distinct monic trace polynomials with roots \(2\cos(2\pi a/n)\) for \(0<a/n<1/2,\ (a,n)=1\).
Each block has degree \(\varphi(n)/2\le7\).
The identity \(\varphi(n)^2/n=\prod_{\ell^e\parallel n}\ell^{e-2}(\ell-1)^2\) gives \(\varphi(n)^2/n\ge1/2\), since only the prime two can contribute a factor smaller than one.
Testing \(3\le n\le392\) therefore lists every allowed block.

The program enumerates products of the indicated degrees and compares their sorted primitive fractions exactly.
The cosine decreases on this half-circle, so strict alternation of these fractions is equivalent to strict interlacing of the roots.
For an interlacing pair, \(g\) is strictly increasing on each real branch and its interior branches already lie in \((-2,2)\).
Thus both fibers lie in \([-2,2]\) exactly when the outer-branch endpoint inequalities hold.
For \(S=Y^2+tY+u\) the program compares \(2g(-2)+t\) with \(-\sqrt{t^2-4u}\) and \(2g(2)+t\) with \(+\sqrt{t^2-4u}\) using rational signs and squares.

| Pole degree \(p\) | All pairs \(B,R\) | Strictly interlacing pairs | Tests for \(Y^2-Y-1\) | Accepted |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 3 | 3 | 6 | 2 |
| 2 | 21 | 11 | 22 | 0 |
| 3 | 119 | 23 | 46 | 0 |
| 4 | 595 | 51 | 102 | 0 |
| 5 | 2345 | 23 | 46 | 0 |
| 6 | 8509 | 47 | 94 | 0 |
| 7 | 28575 | 37 | 74 | 0 |

The \(Y^2-2\) search tests the same three degree-one pairs at \(c=0\) and accepts one.
For each accepted map the program forms \(A=(X+c)B-R\), expands \(z^{2(p+1)}(A^2+tAB+uB^2)(z+z^{-1})\), and divides by cyclotomic polynomials in \(\mathbb Z[z]\) until the quotient equals one.
The [results](../../outputs/Yin_J_G0165/classifications.json) record all conductor blocks, counts by degree, endpoint values, maps and output factorizations.
From the repository root run `python mathematics/computations/programs/Yin_J_G0165/classify.py` with Python 3.9 or newer.
The [program](classify.py) uses only the standard library.

<a id="independent-verification"></a>
## An independent enumeration from the two fibers

The main researcher checked the table from the output side with the [independent program](verify.py).
The pole bound gives total trace degree at most sixteen for discriminant five and four for discriminant eight.
The two fibers are real and disjoint, and their roots alternate strictly, beginning with a root of the smaller source conjugate.
This follows from \(g'>0\) on each branch, which contains one root from each fiber.
Neither endpoint can be a root, since \(g(\pm2)\) is rational when defined and the source roots are irrational.
Thus the trace polynomial of a full output of measure one is a product of distinct primitive cyclotomic trace blocks.

In each block the source root is \(g(\zeta_n+\zeta_n^{-1})\), so its quadratic field is contained in that of the primitive trace.
The program factors every candidate trace block over the relevant quadratic field, covering all orders by the same totient bound used above.
The blocks that split in this degree range have orders divisible by five for discriminant five and by eight for discriminant eight.
For each such block the two halves correspond exactly to the two values of the quadratic character on the primitive indices \(a\).
Indeed \(\sqrt5=1+2(\zeta_5+\zeta_5^{-1})\) and \(\sqrt2=\zeta_8+\zeta_8^{-1}\), so the positive signs are \(a\equiv\pm1\) modulo five and eight respectively.
The verifier chooses one of the two assignments on each entire block and sorts all roots by the rational angles \(a/n\).
It retains a choice only if the two assigned fibers alternate in the required order.
Their monic polynomials \(F_\pm=A-y_\pm B\) determine \(A,B\) uniquely by subtraction, where \(y_-<y_+\) are the two fixed source roots.
The candidates left by alternation are exactly the single blocks of orders fifteen, thirty and twenty-four, with one assignment for each.
The displayed maps realize all three.

Run the independent check with Python and SymPy.

~~~powershell
python mathematics/computations/programs/Yin_J_G0165/verify.py
~~~
