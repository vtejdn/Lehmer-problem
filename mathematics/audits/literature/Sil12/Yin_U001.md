---
author: Yin
---

# Silverman's weighted estimate at a fixed period

<a id="sil12-u001"></a>
## The disk estimate and the fixed-period height bound

In the [journal edition](readme.md#edition), Proposition 2.1 on p. 758 bounds the archimedean cost of averaging over powers.
For an integer \(J\ge1\), put \(w_j=1-j/(J+1)\) for \(1\le j\le J\).
Then

\[
\sup_{|z|\le1}\sum_{j=1}^J w_j\log|1-z^j|
\le B_J,\qquad B_J=\tfrac12\bigl(\log(1+J/2)+1\bigr).
\]

Section 6, pp. 769–771, obtains this estimate on the boundary by replacing \(1-e^{ij\theta}\) with \(1-e^{-t}e^{ij\theta}\) at an additive cost of at most \(t/2\) per term.
The nonnegative Fejér kernel gives \(\sum_{j=1}^J w_j\cos(ju)\ge-1/2\).
Expanding the regularized logarithm therefore bounds the weighted sum by \(-\tfrac12\log(1-e^{-t})+Jt/4\).
Taking \(t=\log(1+2/J)\) gives the stated bound.

<a id="fixed-period-valuation"></a>
### The finite-place sum at period \(n\)

Use a number field \(K\) containing a finite collection \(A\) of nonzero algebraic integers, none a root of unity.
For a finite place \(v\) over \(p\), set \(v(x)=-[K_v:\mathbb Q_p]\log|x|_v/[K:\mathbb Q]\), where \(|p|_v=p^{-1}\).
For integers \(m\ge2\) and \(n\ge1\), Silverman's definition on p. 757 is

\[
\Delta(A,m,n)=\frac{1}{n\log m}
  \sum_{\alpha\in A}\sum_{v\mid m}v(\alpha^n-1).
\]

The inner sum runs over the places above the rational prime divisors of \(m\), and the normalization makes it independent of the containing field.
When \(A\) consists of the roots of a monic integer polynomial \(f\), Silverman counts multiplicities, so \(\sum_{\alpha\in A}h(\alpha)=\log M(f)\) by Remark 1.2 on p. 755.

For each \(j\ge1\), the divisibility \(X^n-1\mid X^{jn}-1\) gives \(v(\alpha^{jn}-1)\ge v(\alpha^n-1)\) separately at every such place.
The sum on p. 759 retains its original index \(\alpha\in A\) when powers coincide.
This convention matters for Proposition 1.2 on p. 757, which writes the image of the power map as a set.
For \(A=\{2,-2\}\), \(m=3\) and \(n=j=2\), each original element contributes \(\log 3\) at the place over 3 in \(\mathbb Q\), while the singleton image \(\{4\}\) contributes only \(v_3(15)=\log 3\) in the source normalization.
Summing the pointwise inequality over the original indices justifies the step used on p. 759.

The product formula in (2.2) moves the finite-place sum to the archimedean places.
At each such place, writing a root outside the unit disk as the inverse of a point inside produces the term \(jn h(\alpha)\) after summation over the places.
Using \(\sum w_j=J/2\) and \(\sum j w_j=J(J+2)/6\), Theorem 2.1, pp. 758–759, yields

\[
\frac{Jn\log m}{2}\Delta(A,m,n)
\le \frac{nJ(J+2)}6\sum_{\alpha\in A}h(\alpha)+|A|B_J.
\]

The left side propagates the valuation mass already present at one period \(n\) to its multiples \(jn\).
Estimating mass first appearing at different periods requires additional arithmetic information.

### The congruence hypothesis

For \(0<\varepsilon<1/210\), Corollary 2.1 on p. 760 takes a monic \(f\in\mathbb Z[X]\) of degree \(D\) with no root of unity and assumes that some integers \(m\ge2\) and \(n\ge\max\{2,\varepsilon D\}\) satisfy

\[
1+X+\cdots+X^{n-1}\mid f(X)\qquad\text{in }(\mathbb Z/m\mathbb Z)[X].
\]

The source denotes this entire geometric sum by \(\Phi_{n-1}\).
Proposition 1.1 and Remark 1.3, pp. 756–757, give \(\Delta(A_f,m,n)\ge(n-1)/n\) for the roots of \(f\).
Under these hypotheses, (2.4) states

\[
\log M(f)\ge\frac{\log m}{185\,\varepsilon^{-1}\log(24\varepsilon^{-1})}.
\]

The inspection covered the finite-place normalization and resultant implication, the weighted proof of Theorem 2.1 and the disk estimate in Section 6.
The corollary's explicit constant is quoted from (2.4) without an independent verification of the numerical optimization in Lemma 2.1.
