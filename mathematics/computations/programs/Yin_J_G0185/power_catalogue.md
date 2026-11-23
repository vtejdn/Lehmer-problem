---
author: Yin
---

# No primitive unit root through degree 44 at coefficient height five or higher

<a id="coverage"></a>
## The primitive generator and its short power

Let \(q\ge5,\ p=q+1,\ |a|=q,\ |b|=p,\ \epsilon=\pm1\), and let \(0<u<v\) be coprime integers.
Write \(P(X)=a(1+\epsilon X^{u+v})+b(X^u+\epsilon X^v)\).
If a nontorsion algebraic unit \(z\) satisfies \(P(z^g)=0\) for an integer \(g\ge1\), then the degree \(D\) of \(\beta=z^g\) is greater than 44.
This applies to both coefficient signs and all conjugate signatures.
In fact \(D\) is even and at least 46.

The [uniform measure bound](../../../claims/Yin_C_G0345_v886.md#statement) gives \(M(\beta)<13/10\) and \(u<2D\).
At every degree the minimal polynomial is reciprocal by [Smyth's nonreciprocal bound](../../../audits/literature/Smy71/Yin_U001.md#smy71-statement-and-conventions), since \(13/10\) lies below the real root of \(X^3-X-1\).
A reciprocal polynomial of odd degree vanishes at \(-1\), which is impossible for the irreducible polynomial of a nontorsion unit.

It remains to exclude \(D\le44\).
The minimal polynomial of \(\beta\) cannot be a composition \(f(X^k)\) with \(k>1\), since that would give a distinct conjugate differing from \(\beta\) by a root of unity, contrary to the [torsion-translate exclusion](../../../claims/Yin_C_G0345_v882.md#statement).
Consequently the [complete small-measure classification](../../../audits/literature/Mos26/readme.md#complete-small-cores) includes the minimal polynomial of \(\beta\) up to \(X\mapsto-X\).
There are 944 polynomials in this degree range and each is reciprocal of even degree.
For \(q\ge7\), the [degree inequality](../../../claims/Yin_C_G0345_v869.md#statement) gives \(qu\le12D/\log2<18D\).
The calculation takes all \(u<2D\) at \(q=5,6\) and all \(qu<18D\) at \(q\ge7\).

Put \(s=\operatorname{sgn}(b/a)\), \(T=-s\beta^u\) and \(Y=\epsilon s\beta^v\).
Then \(Y=(pT-q)/(p-qT)\) and
\[
                    (p-qT)(1+Y)=1+T.
\]
Since \(Y\) is integral, the norm of \(p-qT\) in \(\mathbb Q(\beta)\) divides the norm of \(1+T\).
The endpoints are nonzero because \(T\) is a nontorsion unit.
Testing both signs of \(\beta^u\) also covers the omitted reflection of every catalogue generator.

<a id="calculation"></a>
## Exact norms of powers of the 944 generators

For the roots \(\beta_1,\ldots,\beta_D\) of each catalogue polynomial, the [program](power_catalogue.py) builds
\[
                  S(X)=\prod_{i=1}^D (X-\sigma\beta_i^u),
                  \qquad \sigma\in\{1,-1\}.
\]
Newton's identities give the source power sums \(s_k=\sum_i\beta_i^k\) directly from the integer coefficient vector.
For \(\sigma=1\), the coefficient \(c_j\) of \(X^{D-j}\) satisfies \(jc_j=-\sum_{k=1}^j c_{j-k}s_{uk}\) with \(c_0=1\).
The search computes the coefficients through \(j=D/2\) and mirrors them because inversion preserves the multiset of powered roots and their product is one.
Changing the sign multiplies \(c_j\) by \((-1)^j\).

Let \(F(Q)=Q^D S((Q+1)/Q)\).
The two norms to test are \(F(q)\) and \(S(-1)\) because \(D\) is even.
From the [reciprocal endpoint calculation](pole_catalogue.md#endpoint), if \(F(q)\ne1\) divides \(S(-1)\), then \(q(q+1)\le |S(-1)|+1\).
If \(F(q)=1\), the [linear coefficient test](pole_catalogue.md#filter) gives \(q(q+1)\mid D+c_1\), a condition which retains every \(q\) when \(D+c_1=0\).
For each tuple surviving either test, the program evaluates \(F(q)\) over the integers and tests signed divisibility.

| Coefficient height \(q\) | Signed tuples (source row, \(u,\sigma,q\)) | Exact pole evaluations | Pole divisors |
| --- | ---: | ---: | ---: |
| \(5,6\) | 239,376 | 163,580 | 0 |
| \(7\) through \(11\) | 616,960 | 405,746 | 0 |
| \(12\) and above | 3,860,262 | 458,571 | 0 |

The 77,616 generator–exponent pairs in the union of the three ranges yield no integral graph partner at any admissible height.
The catalogue lookup uses the generator's minimal polynomial.
The calculation constructs the powered characteristic polynomial even when its measure exceeds the catalogue cutoff.

<a id="reproduction"></a>
## Reproduction

Use the fixed [source table and retrieval command](pole_catalogue.md#reproduction) and run from the repository root with Python 3.

~~~sh
python -B mathematics/computations/programs/Yin_J_G0185/power_catalogue.py
~~~
