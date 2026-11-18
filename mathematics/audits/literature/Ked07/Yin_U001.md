---
author: Yin
---

# The Siegel–Walfisz estimate for primes in a reduced residue class

<a id="ked07-u001"></a>
<a id="siegel-walfisz"></a>
## The absolute error in Theorem 4

For real \(x\ge2\), a positive integer \(q\) and an integer \(a\) coprime to \(q\), let \(\pi(x;q,a)\) count the primes \(p\le x\) with \(p\equiv a\bmod q\).
Kedlaya's \(\psi(x;q,a)\) sums the von Mangoldt weights \(\Lambda(m)\) over positive integers \(m\le x\) in the same class. [Weight convention](../Vau77/Yin_U001.md#prime-exponential-sum)

For fixed \(A>0\) and \(\epsilon>0\), Theorem 4 gives, as \(x\to\infty\),
\[
 \pi(x;q,a)=\frac{\operatorname{li}(x)}{\varphi(q)}
       +O_{A,\epsilon}\!\left(\frac{x}{(\log x)^A}\right),\qquad
 \psi(x;q,a)=\frac{x}{\varphi(q)}
       +O_{A,\epsilon}\!\left(\frac{x}{(\log x)^A}\right).
\]
Here \(\operatorname{li}\) is the logarithmic integral and \(\varphi\) is Euler's totient.
The absolute errors are uniform in \(q\) and in the reduced class \(a\bmod q\).
Taking \(\epsilon=1\) gives \(O_A(x/(\log x)^A)\). [Spring 2007 edition](readme.md#edition) · [Theorem 4, printed p. 3](../../../literature/pdf/Ked07.pdf#page=3)

For example, if \(q\le(\log x)^B\) for fixed \(B>0\), the relative error in the prime count is \(O_A((\log x)^{B+1-A})\), since \(\varphi(q)\le q\) and \(\operatorname{li}(x)\sim x/\log x\).
Choosing \(A>B+1\) therefore gives a uniform asymptotic in this range.
The inspection checked the statement, its normalization and the uniformity needed for this use.
The lecture invokes Siegel's exceptional-zero estimate in Theorem 3 and omits the full proof.
Theorem 4 is accepted here at statement scope with ineffective constants and supplies no numerical threshold.
