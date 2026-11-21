---
author: Yin
---

# The finite prime product in a fixed arithmetic progression

<a id="wil74-u001"></a>
<a id="prime-product"></a>
## Theorem 1 at a fixed modulus

Let \(k\ge1\) and let \(1\le l\le k\) be coprime to \(k\).
Section 3, Theorem 1 of Williams's journal article gives a positive constant \(C_{k,l}\) with
\[
 \prod_{\substack{\lambda\le x\\ \lambda\ {\rm prime}\\ \lambda\equiv l\bmod k}}
      (1-1/\lambda)
 = C_{k,l}(\log x)^{-1/\varphi(k)}
       \left(1+O_{k,l}(1/\log x)\right).
\]
I inspected the hypotheses on printed p. 353 and the theorem and its character-product argument on p. 356 in the author's online copy.
The corresponding theorem is on the same printed page of the [local journal copy](../../../literature/pdf/Wil74.pdf#page=4).
The fixed-modulus asymptotic is sufficient for interpreting a finite cutoff in the auxiliary-prime sieve. [Williams, pp. 353 and 356](https://people.math.carleton.ca/~williams/papers/pdf/057.pdf#page=4)

The local surviving fraction at one chosen root in the [integer-seed sieve](../../../claims/Yin_C_G0345_v720.md#sieve) is \(1-1/\lambda+1/\lambda^2\).
Its ratio to the corresponding Williams factor is \(1+1/(\lambda(\lambda-1))\).
The product of the ratios converges to a finite positive limit since their deviations from one are summable, with tail \(O(1/x)\) after truncation at \(x\).
Thus at each fixed modulus and class the product of these local surviving fractions has the same logarithmic exponent.
The density-one theorem itself uses the previously inspected [fixed-progression reciprocal sum](../Sut21/Yin_U001.md#sut21-u001).
A bound uniform in a growing conductor would require control of the modulus dependence as well.
