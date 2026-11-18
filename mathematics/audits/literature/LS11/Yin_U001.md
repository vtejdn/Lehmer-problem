---
author: Yin
---

# The second logarithmic Mahler measure of one cyclotomic polynomial

<a id="ls11-u001"></a>
## The diagonal case of Theorem 5

For each integer \(n\ge1\), let \(\Phi_n\) be the monic \(n\)-th cyclotomic polynomial, \(\varphi\) Euler's totient and \(\omega(n)\) the number of distinct primes dividing \(n\), with \(\omega(1)=0\).
Lalín and Sinha's Theorem 5 gives
\[
 m_2(\Phi_n)=\frac{\pi^2}{12}\,2^{\omega(n)}\frac{\varphi(n)}{n}.
\]
The formula allows arbitrary prime-power multiplicities and gives \(\pi^2/12\) at \(n=1\). [Journal edition](readme.md#edition) · [Theorem 5, printed p. 259](../../../literature/pdf/LS11--published.pdf#page=3)

<a id="definitions"></a>
**Higher and multiple Mahler measures.**
With \(d\mu=dt/(2\pi)\) and \(z=e^{it}\) for \(0\le t<2\pi\), Definition 1 sets \(m_k(P)=\int_{\mathbb T}(\log|P(z)|)^k\,d\mu\) for every nonzero \(P\in\mathbb C[X]\) and positive integer \(k\).
Definition 2 sets \(m(P_1,\ldots,P_l)=\int_{\mathbb T}\prod_{i=1}^l\log|P_i(z)|\,d\mu\) for finitely many nonzero polynomials.
Circle zeros have measure zero and their logarithmic singularities are integrable to every finite power.
The mixed moment with \(k\) copies of \(P\) equals \(m_k(P)\). [Definitions 1 and 2, printed pp. 257–258](../../../literature/pdf/LS11--published.pdf#page=1)

Theorem 21 on printed page 270 gives \(\int f_a f_b\,d\mu=(\pi^2/12)\gcd(a,b)^2/(ab)\) for \(f_a(z)=\log|z^a-1|\), \(a,b\ge1\).
One can check this normalization directly by Parseval from \(\log|1-e^{it}|=-\sum_{k\ge1}\cos(kt)/k\) in \(L^2\).
For \(f_a\) and \(f_b\), frequencies coincide at the positive multiples of \(\operatorname{lcm}(a,b)\), giving the stated inner product since \(\sum k^{-2}=\pi^2/6\).
Proposition 22 then expands \(\log|\Phi_n|\) as \(\sum_{d\mid n}\mu_{\rm M}(n/d)f_d\) almost everywhere, where \(\mu_{\rm M}\) is the Möbius function.
In the diagonal double sum for \(p^e\Vert n\), each of the two divisor exponents is \(e\) or \(e-1\).
The two equal-exponent terms contribute \(1\) each and the other two contribute \(-1/p\) each.
Multiplication over \(p\mid n\) yields \(\prod_{p\mid n}(2-2/p)\), verifying the diagonal formula directly from the divisor sum. [Theorem 21, printed p. 270](../../../literature/pdf/LS11--published.pdf#page=14) · [Proposition 22, printed p. 271](../../../literature/pdf/LS11--published.pdf#page=15)

For \(G=\log|\Phi_n|\), the circle mean is zero, so the centered variance \(V(\Phi_n)\) equals \(m_2(\Phi_n)\).
The positive-part integral \(J(\Phi_n)=\int G_+\,d\mu\) instead equals \(\tfrac12\int|G|\,d\mu\), giving \(J(\Phi_n)\le\tfrac12\sqrt{m_2(\Phi_n)}\) by Cauchy–Schwarz.
For the selected squarefree conductors the lower bound for \(J(\Phi_n)\) uses the separate fourth-moment argument in [L225](../../../ledger/Yin_L_G0462_v225.md#moments).

<a id="mixed"></a>
## A counterexample to the printed off-diagonal formula

At \(m=4,\ n=2\), the mixed expression in Theorem 5 gives \(+\pi^2/24\), as does the first case of Proposition 23 with \(p=2,\ k=2,\ l=1\) and coprime-to-\(p\) parts both one.
From \(\Phi_4=(X^4-1)/(X^2-1)\) and \(\Phi_2=(X^2-1)/(X-1)\), Theorem 21 instead gives
\[
 m(\Phi_4,\Phi_2)=\int(f_4-f_2)(f_2-f_1)\,d\mu
   =\frac{\pi^2}{12}\left(\frac12-\frac14-1+\frac12\right)
   =-\frac{\pi^2}{48}.
\]
The discrepancy enters Proposition 23(1) on printed pages 271–272 and carries into the product in the proof of Theorem 5 on page 273.
For a common prime \(p\) with unequal exponents \(a>b\ge1\), put \(\Delta=a-b\).
Its four terms in Proposition 22 give \(2p^{-\Delta}-p^{-(\Delta-1)}-p^{-(\Delta+1)}=-(p-1)^2/p^{\Delta+1}\), whereas Proposition 23(1) prints \(2p^{-\Delta}(1-1/p)\).
For \(a=b>0\) the direct sum gives the printed \(2(1-1/p)\), and for \(a>0=b\) the two terms give \(p^{-a}-p^{-(a-1)}=-(p-1)/p^a\), as in Proposition 23(2).
Thus the earlier gcd kernel and Möbius divisor sum support the diagonal result used here.
The inspection covers Definitions 1–2, the second-moment statements and the relevant steps of the proof in §3, including the displayed prime-product evaluation on printed page 273. [Printed mixed formula, p. 259](../../../literature/pdf/LS11--published.pdf#page=3) · [Proposition 23, pp. 271–272](../../../literature/pdf/LS11--published.pdf#page=15) · [Proof of Theorem 5, p. 273](../../../literature/pdf/LS11--published.pdf#page=17)
