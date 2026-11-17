---
author: Yin
---

<a id="dob06-u001"></a>
# Mahler measure bounds in terms of support

<a id="sparse-measure"></a>
## The full polynomial

Let \(k>1\) count the nonzero monomials of \(f\in\mathbb Z[X]\) and let \(M(f)\) be its multiplicative Mahler measure.
For \(M(f)>1\), Theorem 1 gives
\[
 M(f)\ \ge\ 1+\exp\!\left(-a\,3^{\lfloor(k-2)/4\rfloor}k^2\log k\right),
 \qquad a<0.785 .
\]
The support count includes all terms after like exponents have been collected.
Cyclotomic factors may occur with multiplicity.
Removing a monomial factor preserves both \(k\) and \(M(f)\), so the application with \(M(f)>1\) avoids any convention on zero roots.
For a cyclotomic multiple \(f\) of a polynomial \(P\), the bound transfers to \(M(P)=M(f)\) using the support of that actual multiple.
For an integral multiple \(f=PQ\), taking logarithms instead bounds \(\log M(P)+\log M(Q)\) from below by the logarithm of the displayed right side. [Theorem 1, p. 202](readme.md#edition)

<a id="irreducible"></a>
## A divisor or an irreducible polynomial

If \(g\mid f\) is monic and integral, \(g(0)\ne0\), and \(g\) has no cyclotomic factor, Lemma 1 gives
\[
 M(g)\ \ge\ 1+\frac{0.31\,\deg g}{k!\,\deg f}.
\]
For monic irreducible noncyclotomic \(g\) with \(g(0)\ne0\), Proposition 1 gives
\[
 M(g)\ \ge\ 1+\frac{0.17}{2^j j!},\qquad
 j=\left\lceil\frac{|\operatorname{supp}g|}{2}\right\rceil .
\]
Thus Proposition 1 counts the terms of \(g\), while Lemma 1 counts the terms of its multiple \(f\) and uses the degree ratio.
The published section headings on pp. 228–229 interchange the proposition numbers.
Section 5 treats quadrinomials, and §6 uses irreducibility to obtain the \(0.17/(2^j j!)\) bound.
Theorem 1, Lemma 1 and Proposition 1 are accepted in the stated applications after checking the displayed statements and the location of the irreducible argument.
Their full proofs were not independently reviewed. [Statements, pp. 202–203, and §§5–6](readme.md#edition)
