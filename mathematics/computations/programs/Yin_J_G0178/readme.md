---
author: Yin
---

# The reciprocal sextic units of multiplicative Mahler measure at most two

<a id="census"></a>
## Seventeen seeds up to the variable sign

Write \(P=X^6+aX^5+bX^4+cX^3+bX^2+aX+1\), \(M=\exp(m(P))\), and let \(g\) count the exterior roots with multiplicities.
Up to \(X\mapsto-X\), the following are all monic irreducible noncyclotomic reciprocal sextics with \(M\le2\).
For every one, the ratio of any two distinct roots has infinite order.

| \(g\) | Certified lower bound | Triples \((a,b,c)\) |
| ---: | --- | --- |
| 1 | \(M>7/5\) | \((0,-2,3),(0,-1,1),(0,-1,2),(1,-1,-1),(1,-1,0),(1,-1,1),(1,0,1),(2,-1,-3),(2,0,-1),(2,1,2),(2,2,3)\) |
| 2 | \(M>17/10\) | \((0,1,2),(0,2,1),(1,0,-2),(1,1,-1),(1,2,3),(2,2,1)\) |

For \(\ell_i=\log|\alpha_i|\) over the roots of \(P\), set \(h=\log M\) and \(D=\sum_{i<j}|\ell_i-\ell_j|\).
Reciprocity gives \(g\) positive and \(g\) negative entries with total absolute value \(h\) in each group.
The differences between these two groups and between either group and the zeros contribute \(2(6-g)h\), so \(D\ge2(6-g)h\).
For every seed in the table and every row degree \(w\le9\), the enumeration therefore verifies
\[
          \frac{2D-(w-2)h}{6}\ \ge\ \frac{4(6-g)-7}{6}\log M>\log2.
\]
In fact \(7^{13}>2^6\,5^{13}\) and \(17^9>2^6\,10^9\).
In a fixed-seed coefficient bound with this expression as the lower limit of \(\log H/p\), the strict margins exclude \(H\le2^p\) for all sufficiently large prime exponents \(p\), uniformly over this finite list by taking the largest onset.
This computation supplies the sextic cases through \(w=9\).
The full coefficient test also admits degree-eight seeds starting at \(w=8\).
The finite enumeration gives no numerical onset for the prime exponents.

<a id="algorithm"></a>
## Exact measure and root-ratio tests

The elementary symmetric coefficient bounds \(|[X^{6-i}]P|\le2\binom6i\) give \(|a|\le12,\ |b|\le30,\ |c|\le40\).
The sign symmetry permits \(a\ge0\) and, if \(a=0\), \(c\ge0\).
The program inspected all \(61\,793\) such triples.

For \(j=1,2,3\) let \(C_j\) be the monic polynomial of all products of \(j\) distinct indexed roots of \(P\).
For a positive rational \(R\ge1\), \(M\le R\) is equivalent to every coefficient of both \(C_j(Z+R)\) and \((-1)^{\deg C_j}C_j(-Z-R)\) being nonnegative for all three \(j\).
Indeed if \(M\le R\), every such product has modulus at most \(R\).
After either shift the real linear factors have nonnegative coefficients, as do the real quadratic factors from nonreal conjugate pairs.
Conversely if \(M>R\), the product of all exterior roots is real, has absolute value \(M\), and uses at most three roots by reciprocity.
One shifted polynomial then has a strictly positive real zero, impossible for a monic polynomial with nonnegative coefficients.
The tests work also for repeated roots and equality at \(R\).
For \(R=N/q\) the program scales all product roots by \(q\) before translating by \(N\), so the comparisons use integers.

The coefficients of the product polynomials are obtained by Newton's identities.
If \(s_n=\sum_i\alpha_i^n\), the power sums at index \(n\) for \(C_2,C_3\) are \((s_n^2-s_{2n})/2\) and \((s_n^3-3s_ns_{2n}+2s_{3n})/6\).
Exactly 60 triples pass at \(R=2\).
Every reducible member has a monic integral factor of degree \(d\le3\), constant coefficient \(\pm1\), and intermediate coefficients bounded by \(2\binom di\), since its multiplicative measure is also at most two.
Trial monic division by all such factors leaves 19 irreducibles, of which two are cyclotomic.

For each remaining polynomial the cubic trace polynomial is \(T=Z^3+aZ^2+(b-3)Z+c-2a\).
Every trace strictly inside \((-2,2)\) gives two roots on the unit circle, and every other trace gives one exterior root.
Irreducibility of \(P\) excludes the endpoints and repeated trace roots.
The exact rational Sturm variation difference gives \(g=3-\#\{T=0\text{ in }(-2,2)\}\).
The same integer shift tests with \(R=7/5\) or \(17/10\) certify the strict lower bounds.

Finally let \(C\) be the degree-30 monic polynomial of all \(\alpha_i/\alpha_j\) with \(i\ne j\).
Reciprocity makes its \(n\)-th power sum \(s_n^2-6\), giving its coefficients by Newton's identities.
A torsion ratio of order \(n\) would force \(\Phi_n\mid C\) and \(\varphi(n)\le30\), hence \(n\le1800\) by \(\varphi(n)^2\ge n/2\).
The latter bound follows by multiplying the prime-power factors of \(\varphi(n)^2/n\), each at least one except possibly the factor at two, which is at least \(1/2\).
The program constructs every such \(\Phi_n\) by monic division of \(X^n-1\) by the preceding proper-divisor polynomials, all of which have \(\varphi(d)\le\varphi(n)\).
Every division test of the 17 ratio polynomials by the eligible cyclotomic polynomials had a nonzero remainder.

<a id="reproduction"></a>
## Reproducing the census

Run the [standard-library Python program](census.py) from the repository root.

```text
python mathematics/computations/programs/Yin_J_G0178/census.py
```

Compare the generated `mathematics/computations/outputs/Yin_J_G0178/results.json` with the fixed census.
The run on Python 3.14.3 produced the [per-seed results](inputs/results.json), including the exterior count, the rational measure bound and the list of torsion-ratio orders for each triple.

The [octic census](versions/v2/readme.md#census) treats the next possible seed degree and gives the separate measure comparisons needed at width eight.
