---
author: Yin
---

# Nine-position signed rows at a quartic Salem number and its square

<a id="sample"></a>
## Where a missing coefficient costs most

Let \(\delta>1\) be the Salem root of \(P(X)=X^4-X^3-X^2-X+1\), and let \(P_2(X)=X^4-3X^3+X^2-3X+1\) be the minimum of \(\delta^2\).
Indeed \(P_2(X^2)=P(X)P(-X)\), and the squares of the four conjugates are distinct.
For \(n\in\{16,32,64,128\}\) and \(\varepsilon=\pm1\), the primitive integral polynomial \(A(Y)\) was computed up to sign on each nine-position support of formal width \(b=8,9\) subject to
\[
 (P P_2)^2\mid F_{n,b}(A),\qquad
 F_{n,b}(A)=A(X^n)+\varepsilon X^{nb+1}A(X^{-n}).
\]
Every one of the 88 systems has a one-dimensional rational kernel, and its generator uses all nine selected positions.
In every case \(A(c^n)\ne0\) at every root \(c\) of \(P P_2\).

Each entry gives the minimum and maximum binary length \(1+\lfloor\log_2\|A\|_1\rfloor\) over both signs and the indicated supports.
At every tested exponent even the largest cost in each column is strictly smaller than the smallest in the next column.

| \(n\) | Width 8, full | Width 9, omit 0 or 9 | Width 9, omit 1 or 8 | Width 9, omit any of 2 through 7 |
| ---: | ---: | ---: | ---: | ---: |
| 16 | 197 | 203–206 | 226–228 | 232–235 |
| 32 | 441 | 450–452 | 497–498 | 512–518 |
| 64 | 889 | 899–902 | 992–996 | 1038–1041 |
| 128 | 1832 | 1845–1847 | 2040–2041 | 2128–2134 |

For example, at \(n=16,b=8\) the exact norms for \(\varepsilon=+1,-1\), respectively, are
\[
 123544621650430764143853913635900014070443875222192864917351,\qquad
 148108352994032562766083958089371108698344951882942847685473.
\]
The samples compare rows with one missing coefficient at width nine and leave the cheapest unrestricted row at that width undetermined.
They establish the ordering only at these four exponents.

The reflection \(A^*(Y)=Y^b A(1/Y)\) preserves the coefficient norm and satisfies \(F_{-n,b}(A^*)=X^{-nb}F_{n,b}(A)\) in the Laurent ring with the sign fixed.
Thus reflecting an omission from \(j\) to \(b-j\) exchanges exponents \(n\) and \(-n\).
The two reflected supports can have different costs at the same positive exponent, as the two endpoint omissions do at \(n=16\) for each sign.
The shift in the reversal also explains why an endpoint omission at width nine need not reproduce the width-eight norm.
Writing \(A(Y)=Y^u B(Y)\) for \(u=0,1\) (omitting 9 and 0, respectively) gives
\[
 X^{-nu}F_{n,9}(A)=B(X^n)+\varepsilon X^{8n+1+(1-2u)n}B(X^{-n}).
\]

<a id="reproduce"></a>
## Reproducing the integral generators and norms

Run this command from the repository root with Python 3.10 or later and its standard library.

```text
python -B mathematics/computations/programs/Yin_J_G0177/versions/v5/quartic_circuits.py
```

The [program](quartic_circuits.py) calls the [signed integer kernel routine](../../minimum.py) with the coefficient list of \(P P_2\).
That routine forms the remainders of the signed columns modulo \((P P_2)^2\) and uses exact rational elimination with denominator clearing and integral congruences.
At width eight it returns a line, and at width nine it returns a plane with integral basis \(u,v\).
For each omitted position \(j\), the vector \(v_j u-u_j v\) is nonzero, so it spans the line in that plane with coordinate \(j\) zero.
Dividing out its content and fixing the first nonzero sign gives the primitive generator.
The program checks its support and primitivity and uses integer long division on the expanded graph to check both squared factors separately.
Division of the expanded \(A(X^n)\) by each irreducible factor gives a nonzero remainder, which checks all eight target values.
The [generated data](../../../../outputs/Yin_J_G0177/versions/v5/results.json) contain each complete coefficient vector in ascending degree order and its exact one-norm.
