---
author: Yin
---

# Two integer moments and whole Mahler measures in fixed ternary resultant classes

<a id="fixed-cut-moments"></a>
## Fixed signatures and positive-unit choices

For the [G0001 small-shell investigation](../../../tasks/Yin_T_G0001_v1.md#decision-resume-small-shell-2026-11-08), take the full odd trace grid at \(p=27,81\) and the [integral representative \(h_0\)](../../../ledger/Yin_L_G0464_v8.md#integral-sign-representative) for the specified cut.
Write \(n=(p-1)/2,\ b_j=2\cos(2\pi j/p),\ B=1+\sum_{i=1}^{n}T_i,\ D=B-T_n\), where \(T_i(z+1/z)=z^i+z^{-i}\).
The residues \(r_j=(4-b_j^2)h(b_j)/p\) are negative at the \(k\) smallest poles and positive elsewhere.
Set \(C=Dh\bmod B,\ Q=(t-2x)B+C,\ P=z^{n+1}Q(z+1/z)\) for \(x\in\{-2,-1,0,1,2\}\).
The sampled words test the [two required moments](../../../ledger/Yin_L_G0464_v7.md#prefix-cut) \(K=\sum r_j=x^2+2,\ L=\sum b_jr_j=-4x\).

At \(p=27\), multiply \(h_0\) by powers of the following ordered ten units.
\[
  2+T_j\quad(j=1,2,4,5,7,8,10,11),\qquad (T_{15}/T_3)^2,\quad(T_{21}/T_3)^2.
\]
For the logarithmic cut \(k=\lfloor p/\log p\rfloor=8\), the sign construction selects cosine columns \(4,5,6,8,9,10,13\).
Use the box of radius three about the exponent vector \((0,2,0,0,0,0,0,0,0,0)\).
For the [second ternary cut](../../../ledger/Yin_L_G0464_v8.md#small-norm-terminal-block) \(k=3^{3-2}=3\), the selected columns are \(1,2,5,6,9,10\), and the box has radius two about zero.
Both cases have \(\Delta=|\operatorname{Res}(B,Q)|=32\).

At \(p=81,\ k=\lfloor p/\log p\rfloor=18\), the selected columns are \(2,6,14,16,17,19,23,24,26,28,31,33,36,37,39,40\), and \(\Delta=16\).
For each selected column independently take either its original quotient \(J_u(T_{3^e})\) in \(h_0\), or its inverse, using the odd representative \(u\) in the construction.
Multiply by \(\prod_j(2+T_j)^{e_j}\) for \(j=1,2,4,5,7,8\) and \(-1\le e_j\le1\).
Inverting a quotient multiplies the representative by its inverse square.
Each quotient square and each \(2+T_j\) is positive at every pole, and the program checks that each inverse has integral coefficients modulo \(B\).
Thus every word retains the prescribed signs and exact nonunit resultant.

<a id="whole-measures"></a>
## Joint survivors and complete measures

The first-moment columns count exponent words once for the stated integer \(K\).
The joint column counts pairs of a word and a compatible \(x\) satisfying both equations, before any endpoint test.
Distinct polynomials are counted using the normalized \(h\) and \(x\), which are determined by the lift since multiplication by \(D\) modulo \(B\) is invertible.

| \(p\) | \(k\) | Words | \(K=2\) | \(K=3\) | \(K=6\) | Joint | Distinct joint \(P\) | Joint with \(P(-1)>0\) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 27 | 8 | 282,475,249 | 6,391 | 6,218 | 6,236 | 2 | 2 | 0 |
| 81 | 18 | 47,775,744 | 33,843 | 33,786 | 34,367 | 70 | 14 | 0 |
| 27 | 3 | 9,765,625 | 1,211 | 1,309 | 1,363 | 48 | 48 | 1 |

For \(p=27,k=8\), the two joint survivors both have \(x=-2\).
The word \((0,3,1,0,0,0,0,0,-1,0)\) has \(P(-1)=-33\) and \(7.773973\le M(P)<7.773974\).
The word \((1,3,1,1,0,0,1,0,0,0)\) has \(P(-1)=-1\) and \(5.744036\le M(P)<5.744037\).
For \(p=81,k=18\), the minimum over the 14 polynomials lies in \([7.162445,7.162446)\) and the maximum in \([18.538189,18.538190)\).
The [integer endpoint bounds](../../../ledger/Yin_L_G0464_v11.md#endpoint-moment-test) address a wider scope than these word counts.

For \(p=27,k=3\), the minimum over the 48 polynomials lies in \([2.867493,2.867494)\) and the maximum in \([32.452990,32.452991)\).
The unique strict-endpoint word is \((0,2,0,1,0,1,0,1,0,0)\) with \(x=0,\ P(-1)=1,\ 3.349927\le M(P)<3.349928\).
With uniform independent exponents and \(x\), this event has probability \(1/(5^{10}\cdot5)=1/48{,}828{,}125\).
This finite positive mass concerns the second cut and the displayed measure interval.

<a id="two-orbits-243"></a>
## Two balanced searches at conductor 243

For \(p=243,\ k=44,\ \Delta=2^{53}\), the [layer and endpoint tests](../../../ledger/Yin_L_G0464_v11.md#layer-valuations-and-orbits) leave \(x=0\) and two possible valuation vectors.
Their base representatives on the full grid are \(h_0\) and \(h_1=h_0T_3^8/T_9^2\).
For each orbit, choose a center and 16 unit directions as fixed explicitly in [the conductor-243 program](ternary243.py).
Positive direction labels \(a=3^e u\) denote \((T_a/T_{3^e})^2\), while negative labels \(-a\) denote \(T_a^2\) for \(3\nmid a\).
Each of the 16 exponents ranges independently over \(-1,0,1\), giving \(3^{16}=43{,}046{,}721\) words per orbit.
The program checks all inverse identities by integral cyclic multiplication and computes the five absolute layer norms of both centers as exact resultants.

The centers were selected by numerically minimizing \(T=L+33K/40=\sum_j(b_j+33/40)r_j>0\).
For each orbit, 1,000 initial random quotient sign-exponents \(+1,-1\) were adjusted by greedy single unit steps in both directions using quotient squares and order-coprime cosine squares.
The 16 sampled directions have the smallest one-step costs around the chosen center, taking the better of the two orientations for each direction.
The stored integer centers and directions fix the sampled boxes independently of the numerical heuristic.

| Layer valuation vector | Center \((K,L)\) | Words with \(K=2\) | Minimum \(L\) at \(K=2\) | Words with \((K,L)=(2,0)\) | Minimum \(40L+33K\) over all words |
| --- | ---: | ---: | ---: | ---: | ---: |
| \((2,2,2,1,0)\) | \((-25,159)\) | 114 | 353 | 0 | 5,535 |
| \((8,0,2,1,0)\) | \((778,-529)\) | 137 | 403 | 0 | 4,514 |

In each row the center uniquely attains the last minimum, and the first-moment minimum for \(L\) is also attained by one word.
The exact target for \(40L+33K\) is 66.
The first projection has solutions in both boxes, while no word passes the second moment for whole-measure evaluation.
These minima apply within the displayed finite boxes.

The program normalizes cyclic coefficient words and encodes nonnegative shifted coefficients in a sufficiently large power-of-two base, so one integer multiplication followed by cyclic reduction implements convolution without carries.
For the orbit change it uses the finite alternating sum for \(2/T_9\) on the odd grid, verifies the coefficientwise division by four and checks \(h_1T_9^2=h_0T_3^8\).
To count \(K=2\) it screens the bilinear first moment modulo \(100{,}000{,}007\) and checks the preimages and their second moments by integer dot products.
For the separate minimum computation, the known positivity of \(40L+33K\) means its least nonnegative residue never exceeds its actual value.
Starting with the center as a known upper bound, each modular value at most the incumbent is therefore an exhaustive candidate for an equal or smaller integer value and is tested exactly.
To replay this search from the same directory, run the following command with the dependencies below.

~~~text
python -B ternary243.py
~~~

<a id="moment-replay"></a>
## Exact sieve and reproduction

Represent a symmetric cyclic coefficient vector \(w\) modulo \(1+z+\cdots+z^{p-1}\) by setting \(w_n=w_{n+1}=0\).
Summing over the \(p\)-th roots of unity, with zero weight at \(z=1\) and equal terms at inverse pairs, gives \(K=w_0-w_2,\ L=w_1-w_3\), since \(4-(z+z^{-1})^2=2-z^2-z^{-2}\).
The [program](moments.py) multiplies the words in two halves and evaluates \(K\) as a bilinear form modulo 65521 with a checked 64-bit accumulator bound.
It recomputes every modular match over the integers before counting \(K\), and computes \(L\) using an integer dot product.
On joint survivors it independently checks \(K=[t^{n-1}]C,\ L=[t^{n-2}]C-[t^{n-1}]B\,K\) and computes the exact resultant and \(P(-1)\).

The program isolates all real roots of \(Q\) in rational intervals of width at most \(10^{-20}\), including multiplicities.
Each real trace \(b\) with \(|b|>2\) contributes \(\rho(|b|)\), where \(\rho(s)=(s+\sqrt{s^2-4})/2\), and traces in \([-2,2]\) contribute one.
Same-sign gaps give at least \(n-2\) real traces, so at most one nonreal conjugate pair remains.
Its sum and sum of squares follow by subtracting all the real roots from the first two Newton sums, giving the pair product and the two distances \(|q\pm2|\).
The pair contributes \(\rho((|q+2|+|q-2|)/2)^2\), since \(|q\pm2|=|\lambda\pm1|^2/|\lambda|\) when \(\lambda+\lambda^{-1}=q\).
The products use 45-decimal-place outward-rounded interval arithmetic, and the output gives endpoints in millionths for every joint survivor.

From this directory use Python with NumPy, SymPy and mpmath.
The calculation was run with versions 2.3.5, 1.14.0 and 1.3.0 respectively and imports the [checked logarithmic floor](../Yin_J_G0148/cuts.py) from J148.

~~~text
python -B moments.py 27 3 --center 0 2 0 0 0 0 0 0 0 0
python -B moments.py 81 1 --flips 6
python -B moments.py 27 2 --cut 3
~~~
