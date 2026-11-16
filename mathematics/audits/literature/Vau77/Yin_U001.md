---
author: Yin
---

<a id="vau77-u001"></a>
# Vaughan's estimate for one exponential sum over prime powers

<a id="prime-exponential-sum"></a>
## Theorem 1 with one frequency

Use \(e(t)=\exp(2\pi i t)\) for real \(t\).
The von Mangoldt function on positive integers is \(\Lambda(n)=\log\ell\) if \(n=\ell^j\) with \(\ell\) prime and \(j\ge1\), and zero otherwise.
Let \(\gamma\in\mathbb R\), \(X\ge2\) be an integer, and let \(a,q\) be coprime integers with \(q\ge1\) and \(|\gamma-a/q|\le q^{-2}\).
Setting \(H=1\) in [Vau77, Theorem 1, (2), printed p. 136](readme.md#published) gives
\[
 \left|\sum_{n\le X}\Lambda(n)e(\gamma n)\right|
     \ll \log^7(2X)\big(X q^{-1/2}+X^{4/5}+(Xq)^{1/2}\big).
\]
The maximum of the truncated divisor count in the source is then one, and its separate term \(X^{3/4}\) is absorbed by \(X^{4/5}\).
I checked the hypotheses, exponents and divisor-count normalization on the rendered journal page and accept this specialization without an independent review of Vaughan's proof.
The rational approximation in this bound must be chosen with a sufficiently large denominator when applying it to an irrational frequency.
