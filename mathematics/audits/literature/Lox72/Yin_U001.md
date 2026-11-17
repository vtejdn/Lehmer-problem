---
author: Yin
---

<a id="lox72-u001"></a>
# Loxton's bounds for the conjugate mean square of a cyclotomic integer

<a id="normalizations"></a>
## Summand count and conjugate means

For a cyclotomic integer \(\beta\), Loxton defines \(N(\beta)\) as the least number of roots of unity whose sum is \(\beta\), with \(N(0)=0\).
The minimization permits repetitions and arbitrary orders for the summands.
For any algebraic number \(\beta\) with \(d\) distinct conjugates, write \(H(\beta)=\max_\sigma|\sigma\beta|\) for its house.
Loxton's \(\mathscr M(\beta)\) is the arithmetic mean \(d^{-1}\sum_\sigma|\sigma\beta|^2\), where \(\sigma\) runs over the embeddings of \(\mathbb Q(\beta)\) into \(\mathbb C\).
For \(\beta\in\mathbb Q(\zeta_m)\), averaging over the \(\varphi(m)\) automorphisms of that cyclotomic field gives the same mean because each embedding of \(\mathbb Q(\beta)\) occurs equally often.
The primitive first absolute mean instead averages \(|\sigma\beta|\) over these automorphisms.
Its square is at most \(\mathscr M(\beta)\) by Cauchy–Schwarz, so a lower bound for \(\mathscr M(\beta)\) alone gives no corresponding lower bound for that first mean. [Published edition, pp. 69–70, §2, (2.1)](readme.md#edition)

<a id="mean-square"></a>
## Theorem 1 and the stronger bound in its proof

Fix \(k>\log 2\) and put \(f_k(t)=t\exp(-k\log t/\log\log t)\) for integers \(t\ge2\), with \(f_k(0)=0\) and \(f_k(1)=1\).
Theorem 1 on p. 69 gives \(H(\beta)^2\ge c_k f_k(N(\beta))\) for every cyclotomic integer \(\beta\), with \(c_k>0\) depending only on \(k\).
The top of p. 82 explicitly gives the stronger chain
\[
 H(\beta)^2\ \ge\ \mathscr M(\beta)\ \ge\ c_k f_k(N(\beta)).
\]
Equation (6.1) on p. 81 uses the auxiliary regularization \(g\) defined on p. 71.
The comparison on pp. 81–82 gives the displayed \(f_k\) bound, and the four cases on pp. 82–83 establish (6.1).
Thus a uniform upper bound for the conjugate mean square bounds the unrestricted summand count, independently of the cyclotomic field, since \(f_k(t)\to\infty\). [Published edition, §§1, 3, 6](readme.md#edition)

<a id="prime-descent"></a>
## A product of odd primes and the mean-square identities

Let \(p_1,p_2,\ldots\) be the odd primes in increasing order and \(P=p_1\cdots p_\nu\).
Lemma 9 on p. 81 gives \(\mathscr M(\beta)\ge 2^{-\nu}N(\beta)\) for every cyclotomic integer \(\beta\in\mathbb Q(\zeta_P)\), including the empty-product case \(P=1\).
The proof uses the identity for \(m=p m_1\), \(p\nmid m_1\), and \(\beta=\sum_{j=0}^{p-1}\alpha_j\zeta_p^j\) with integral \(\alpha_j\in\mathbb Q(\zeta_{m_1})\).
Equation (2.4) gives
\[
 2(p-1)\mathscr M(\beta)=\sum_{i,j=0}^{p-1}\mathscr M(\alpha_i-\alpha_j).
\]
In the repeated-prime case \(p^a\Vert m\), \(a\ge2\), the unique expansion \(\beta=\sum_{j=0}^{p-1}\alpha_j\zeta_{p^a}^j\) over \(\mathbb Q(\zeta_{m/p})\) satisfies \(\mathscr M(\beta)=\sum_j\mathscr M(\alpha_j)\) by (2.8).
Loxton attributes these identities to Cassels. [Published edition, pp. 70–71 and 81](readme.md#edition)

The definitions, statements and passage from (6.1) to the mean-square bound were checked in the published scan.
The proof of Theorem 1 is used at statement scope, including its auxiliary lemmas as established inputs.
