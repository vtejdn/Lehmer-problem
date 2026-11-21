---
author: Yin
---

# Reciprocal factors and the fixed coefficient hypothesis in Filaseta’s theorem

<a id="fil22-u001"></a>
## The two-pole sections with varying coefficient degrees

In the [preprint](readme.md#preprint), pp. 1–4, Theorem 1.1 fixes integer polynomials \(f_0,\ldots,f_r\) with common divisor one, \(f_0(0)\ne0\) and \(f_r\ne0\).
For sufficiently large \(n\), it treats \(\sum_{j=0}^r f_j(X)X^{nj}\) under irreducibility conditions on two families of bivariate twists, up to powers of \(X\).
For every representation \(n=h q\pm t\) with \(h\ge2\max_j\deg f_j\) and \(0\le t<h/(r(r+1))\), the plus sign tests \(\sum_j f_j(X)X^{jt}Y^{qj}\) and the minus sign tests \(\sum_j f_j(X)X^{(r-j)t}Y^{qj}\).
Removing every reciprocal irreducible factor with its multiplicity leaves one or an irreducible polynomial.
For a reciprocal input, each nonreciprocal irreducible factor would have a distinct reciprocal partner, so the conclusion forces the remainder to equal one.
The [earlier comparison](../../../ledger/Yin_L_G0450_v2.md#delayed-factorization-source-boundary) applies this observation to fixed coefficient polynomials in a different family.

For the [two-pole section](../../../claims/Yin_C_G0345_v805.md#statement) the coefficient list at \(n=l\) is \(A^*(X^k),X^{2k},A(X^k)\).
These polynomials have common divisor one because the outside coefficients have unit constant terms and the middle coefficient is a monomial.
Their maximum degree is \(4k\), so the twist tests have \(h\ge8k\), and the coefficients themselves change as \(k\) grows.
The fixed-coefficient formulation alone gives no uniform threshold along all sequences with \(k\to\infty\) and \(l/k\to\infty\).
Even if the thresholds and twists were settled in that regime, the remaining part is already one by the independent reciprocity result for every rational irreducible factor of the section.
Theorem 1.1 therefore gives neither a count nor a degree bound for those factors.
The separate degree observation at the bottom of p. 4 assumes Lehmer’s conjecture and allows its positive constant to depend on the coefficient list.
The comparison uses the statement and adjacent remarks.
