---
author: Yin
---

# The BCH bound for consecutive zeros of a polynomial

<a id="dl24-u001"></a>
## From consecutive zeros to Hamming weight

In [Ding and Li's journal survey](readme.md#journal-edition), §1, pp. 1–2, a cyclic code of length \(n\) over a finite field \(K\) is an ideal in \(K[X]/(X^n-1)\).
The characteristic of \(K\) is coprime to \(n\).
Fix a primitive \(n\)-th root \(\beta\) in a splitting field.
The defining set of a code consists of the indices \(j\bmod n\) at which its generator vanishes at \(\beta^j\).
The BCH bound in §2, Theorem 2.1, p. 2, gives Hamming weight at least \(k+1\) for every nonzero codeword whenever the defining set contains \(k\) consecutive indices modulo \(n\).

For the polynomial form, take a nonzero \(W=\sum_{r=0}^{n-1}d_rX^r\) and the cyclic code it generates.
Evaluation at any \(n\)-th root descends to the quotient, so every zero of \(W\) among these roots is a common zero of the code.
If \(W\) vanishes at \(\beta^{j_0+ia}\) for \(0\le i<k<n\) with \(\gcd(a,n)=1\), the same indices are consecutive relative to the primitive root \(\beta^a\), starting at \(a^{-1}j_0\bmod n\).
Hence \(W\) has at least \(k+1\) nonzero coefficients.
Coefficients in \(\overline{\mathbb F}_{\ell}\) cause no difficulty since a finite extension contains the finitely many coefficients and roots in use.

The weight estimate has a direct Vandermonde proof.
If the support \(R\) of \(W\) had size \(1\le t\le k\), the first \(t\) vanishing equations would give
\[
  \sum_{r\in R}(d_r\beta^{j_0r})(\beta^{ar})^i=0
       \qquad(0\le i<t).
\]
The nodes \(\beta^{ar}\) are pairwise distinct, so the matrix is invertible and all \(d_r\) vanish, a contradiction.
This calculation verifies the polynomial form directly.

Theorem 2.1 states the bound and cites Hocquenghem (1959), reference [26], and Bose and Ray-Chaudhuri (1960), reference [7].
The survey also credits Gorenstein and Zierler (1961), reference [23], for the extension of binary BCH codes to finite fields.
The inspected passages are the code and defining-set conventions on pp. 1–2, Theorem 2.1 on p. 2, the primitive-root comment on p. 3, and those three bibliography entries.
The survey gives no proof of Theorem 2.1 there, and the historical papers were not inspected.
For the [Lehmer application](../../../claims/Yin_C_G0345_v355.md#coset), the classical bound applies once the nonzero residual word and its run of zeros have been obtained.
The cyclotomic multiplicity comparison and the extraction of that word from the padded polynomial are proved in the project claim.
