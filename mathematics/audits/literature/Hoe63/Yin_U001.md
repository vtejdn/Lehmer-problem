---
author: Yin
---
# Hoeffding's inequality for independent bounded summands

<a id="hoe63-u001"></a>
<a id="independent-sum"></a>
## One-sided concentration and the exponential moment

Let \(X_1,\ldots,X_n\) be independent real random variables with \(a_i\le X_i\le b_i\) almost surely and finite endpoints.
Set \(S=\sum_i X_i\), \(\bar X=S/n\), \(\mu=\mathbb E\bar X\) and \(V=\sum_i(b_i-a_i)^2\).
For \(V>0\) and \(t>0\), Hoeffding's Theorem 2 gives
\[
 \Pr(\bar X-\mu\ge t)\le \exp(-2n^2t^2/V).
\]
Equivalently \(\Pr(S-\mathbb ES\ge u)\le \exp(-2u^2/V)\) for \(u>0\).
Applying the same bound to the negatives and adding gives \(\Pr(|S-\mathbb ES|\ge u)\le 2\exp(-2u^2/V)\).
Constant summands disappear after centering, and for \(V=0\) the centered sum vanishes. [Definitions and two tails, printed p. 13, (1.1)–(1.4)](../../../literature/pdf/Hoe63.pdf#page=2) · [Theorem 2, printed p. 16, (2.6)](../../../literature/pdf/Hoe63.pdf#page=5)

On printed p. 22 Hoeffding bounds the exponential moment of each centered summand by interpolating the exponential at its two endpoints.
For a nonconstant interval write \(w=b_i-a_i\), \(v=(\mathbb E X_i-a_i)/w\) and \(L(s)=\log(1-v+v e^s)-vs\).
Here \(L(0)=L'(0)=0\), while \(L''(s)=q(1-q)\le1/4\) with \(q=v e^s/(1-v+v e^s)\).
Thus (4.15) gives \(L(hw)\le h^2 w^2/8\), and (4.16) bounds \(\mathbb E e^{h(X_i-\mathbb EX_i)}\) by \(\exp(h^2 w^2/8)\).
Independence gives the product estimate, and exponential Markov at \(h=4u/V\) yields the stated upper tail. [Proof of Theorem 2, printed p. 22, (4.11)–(4.16)](../../../literature/pdf/Hoe63.pdf#page=11)

For at most \(h\ge1\) independent centered summands with interval widths at most two, \(V\le4h\).
The two-sided bound at \(u=\sqrt{2h\log(4h)}\) is then at most \(1/(2h)\).
For \(h\) such sums, a union bound gives a simultaneous failure probability at most \(1/2\), even when different sums share the same random variables.
The integral interpolation construction supplies these per-node widths and the common choice of rounded coefficients. [Project application](../../../claims/Yin_C_G0345_v369.md#square-interpolation)

The journal scan was directly checked for the definitions, the theorem's hypotheses and exponent, and the endpoint and second-derivative estimates in the indicated proof.
The source supports the independent-sum statement and its exponential-moment bound at this scope. [Inspected edition](readme.md#edition)
