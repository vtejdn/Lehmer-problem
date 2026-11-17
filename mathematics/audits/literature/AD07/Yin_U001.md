---
author: Yin
---

<a id="ad07-u001"></a>
# Relative height over abelian extensions

<a id="theorem-1-3"></a>
## Unconditional Theorem 1.3

Let \(K\) be a number field of degree \(d\), \(L/K\) abelian, and \(\alpha\) a nonzero algebraic number of infinite multiplicative order.
Write \(D=[L(\alpha):L]\) and \(A=g(d)|\operatorname{disc}K|\), where \(g(d)=1\) if \(K/\mathbb Q\) admits a tower of normal steps and \(g(d)=d!\) otherwise.
For \(A>1\), Theorem 1.3 gives an absolute \(c>0\) such that
\[
 h(\alpha)\ \ge\ A^{-c}\,\frac{(\log\log(5D))^3}{D\,(\log(2D))^4}.
\]
Here \(h\) is the [absolute logarithmic Weil height](../Smy08/Yin_U001.md#smy08-height-normalization).
The source prints \(\Delta\) in the theorem and uses \(A=g(d)|\Delta|\) in §5.
Theorem 1.2 assumes GRH and Theorem 1.1 recalls the earlier exponent \(13\). [ESI preprint, manuscript pp. 2–4, 19–23](readme.md#edition)

In the last unramified case, the term containing the height in (4.16), as repeated on p. 22, is \(2(T+|\Lambda_2|)(T+\sum_{\mathfrak p\in\Lambda_2}p)D h(\alpha)\).
The bounds immediately following (4.16) therefore give a lower bound for \(D h(\alpha)\).
The printed display (5.26) drops the corresponding \(D\) in the denominator for \(h(\alpha)\).
Restoring it gives the bound in Theorem 1.3, together with (5.19) and (5.25). [End of §5](readme.md#edition)

<a id="rational-base"></a>
## The rational base

There is an absolute \(c_0>0\) such that, for every abelian extension \(L/\mathbb Q\) and every \(\alpha\) as above,
\[
 h(\alpha)\ \ge\ c_0\,\frac{(\log\log(5D))^3}{D\,(\log(2D))^4},
 \qquad D=[L(\alpha):L].
\]
The constant needs care because §2 uses \(\log|\operatorname{disc}K|\ge c_1d\), which fails at \(K=\mathbb Q\).
Literal substitution of \(A=1\) also fails numerically.
For \(\alpha=(1+\sqrt5)/2\) in \(L=\mathbb Q(\sqrt5)\), the height is \((\log\alpha)/2<0.241\), while the right side for \(D=c_0=1\) exceeds \(0.466\). [Theorem 1.3 and §2](readme.md#edition)

Apply the theorem with the fixed base \(K=\mathbb Q(\sqrt5)\), for which \(A=5\), and the abelian extension \(LK/K\).
For a finite \(L\), the tower law gives \(D/2\le D'=[LK(\alpha):LK]\le D\).
The ratio \(\log\log(5\max(1,D/2))/\log\log(5D)\) is positive for \(D\ge1\) and tends to one, so replacing \(D'\) by \(D\) costs at most an absolute factor.
For an infinite \(L\), the coefficients of the minimal polynomial of \(\alpha\) over \(L\) lie in a finite abelian subextension \(L_0/\mathbb Q\), and its irreducibility over \(L\) gives \([L_0(\alpha):L_0]=D\).
For \(L=\mathbb Q^{\rm ab}\) one can include \(K\) in \(L_0\), retain the exact degree \(D\) and use the prefactor \(5^{-c}\).
The numerical value of \(c\) is unspecified.
Theorem 1.3 is accepted within this scope after checking the statement, the discriminant exception, the power of each logarithm and the final height normalization.
The full determinant and ramification arguments were not independently reviewed.
