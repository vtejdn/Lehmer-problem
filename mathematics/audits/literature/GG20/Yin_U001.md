---
author: Yin
---

# Counting Salem numbers of a fixed degree

<a id="gg20-u001"></a>
## The height parameter and the dependence on degree

Fix an integer \(m\ge1\), and let \(N_m(Q)\) count Salem numbers \(\alpha\) of exact degree \(2m+2\) with \(1<\alpha\le Q\).
Each such \(\alpha\) is the unique exterior root of its minimal polynomial, so \(Q\) also bounds its multiplicative Mahler measure.
Götze and Gusakova's Theorem 1.1 gives, as \(Q\to\infty\),
\[
  N_m(Q)=\omega_m Q^{m+1}+O_m(Q^m),\qquad
  \omega_m=\frac{2^{m(m+1)}}{m+1}
             \prod_{j=0}^{m-1}\frac{(j!)^2}{(2j+1)!}.
\]
The authors use \(\operatorname{Sal}_m(Q)\) for the set being counted. [Section 1.1 and equation (1), p. 2](../../../literature/pdf/GG20--arxiv-v1.pdf#page=2)

The leading coefficient is explicit for each \(m\).
In the lattice-point estimate of Lemma 2.1 the error constant can depend on \(m,k,l\), and the reducible-polynomial estimate of Lemma 2.2 allows its constant to depend on \(m\).
Equation (17) uses both estimates.
Consequently Theorem 1.1 supplies a large-\(Q\) asymptotic for each fixed degree and leaves the growth of \(N_m(B)\) at fixed \(B>1\) and \(m\to\infty\) undetermined. [Section 2, Lemmas 2.1–2.2 and equation (17), p. 7](../../../literature/pdf/GG20--arxiv-v1.pdf#page=7)

The inspection covered the definition of the counted set, the exact leading coefficient, and the stated dependence of the error estimates in the [author edition](readme.md#edition).
The proofs of the lattice-point, reducibility and volume estimates were outside its scope.
