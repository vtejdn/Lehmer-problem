---
author: Yin
---

<a id="hb26-u001"></a>
# Mahler measure bounds from one or two binomials modulo two

Let \(P\in\mathbb Z[x]\) be monic of degree \(N\ge1\), with no root of unity among its zeros, and let \(\overline P\) be its reduction in \(\mathbb F_2[x]\).
For positive integers \(m,n\), Corollary 2.7 of the [author-posted edition](readme.md#edition) gives
\[
 \overline P\mid x^n-1
 \quad\Longrightarrow\quad
 \log M(P)\ge\frac{N\log 5}{4n},
\]
and, in equation (14),
\[
 \overline P\mid (x^m-1)(x^n-1)
 \quad\Longrightarrow\quad
 \log M(P)\ge\frac{N\log(5/2)}{4(m+n)}.
\]
Here \(M(P)\) is multiplicative Mahler measure and divisibility includes multiplicities.

The proof substitutes explicit auxiliary polynomials into the resultant bound of Proposition 2.3.
I checked the statement of Corollary 2.7, its two substitutions and its constants against equation (3) and the example in §7.1.
The general resultant inequality and its supporting lemmas were outside this proof check.
For the two-binomial estimate to yield a positive lower bound uniform in a family, the hypotheses must also supply an upper bound for \((m+n)/N\).
