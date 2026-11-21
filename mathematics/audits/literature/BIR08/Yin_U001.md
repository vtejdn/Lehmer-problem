---
author: Yin
---

# Logarithmic averages over a cyclotomic orbit at a complex embedding

<a id="bir08-u001"></a>
<a id="torsion-logarithm"></a>
## The archimedean step of Theorem 0.1

Fix a number field \(K\subset\mathbb C\) with this embedding, and fix \(\lambda\in K\) of ordinary complex modulus one which is not a root of unity.
For a root of unity \(\zeta\) of order \(N\), let \(D=[K(\zeta):K]\).
The archimedean argument for (6) gives
\[
       \lim_{N\to\infty}\frac1D
       \sum_{\sigma:K(\zeta)\hookrightarrow\mathbb C,\ \sigma|_K=\mathrm{id}}
             \log|\sigma(\zeta)-\lambda|=0.
\]
Here the conjugates range over the full orbit over the fixed embedded field and the logarithm uses the ordinary complex modulus.
The paper's global normalization divides (6) by \([K(\zeta):\mathbb Q]\) and uses the first or second power of the ordinary modulus at an archimedean place.
Its proof at this place explicitly uses the displayed relative average.
The finite-place integrality hypothesis of Theorem 0.1 enters the global product-formula argument before (6).
The proof of the archimedean limit applies to every sequence with \(N\to\infty\). [Edition](readme.md#edition) · [Setup and formula (6), printed pages 220–221](../../../literature/pdf/BIR08.pdf#page=6) · [Formulas (7)–(9), printed pages 222–223](../../../literature/pdf/BIR08.pdf#page=8)

Jensen's formula (7) identifies the Haar integral of the logarithm with zero.
In Proposition 1.3 the fraction of the \(D\) conjugates in any arc differs from its normalized length by \(O_{K,\gamma}(D^{-\gamma})\) for each fixed \(0<\gamma<1\).
The proof describes the allowed primitive exponents using residue classes of bounded conductor for the fixed field and counts them by inclusion and exclusion.
Proposition 1.2 supplies the separate lower bound \(N^{-C_\lambda}\), for large \(N\), on the angular distance from \(\lambda\) of the nearest point of order \(N\).
This linear-forms-in-logarithms estimate is accepted at the stated scope. [Propositions 1.2–1.3, printed pages 222–223](../../../literature/pdf/BIR08.pdf#page=8) · [Lemma 1.4 and proof of Proposition 1.3, printed pages 226–227](../../../literature/pdf/BIR08.pdf#page=12)

For a fixed small arc around \(\lambda\), the paper subtracts a local logarithm so that the remaining function is continuous on the circle.
It partitions the arc into \(2\lceil\sqrt D\rceil\) pieces and uses Proposition 1.3 with \(\gamma=2/3\).
On the two central pieces the normalized singular contribution tends to zero by the distance estimate and \(\log N/\sqrt D\to0\), since \(D\ge\varphi(N)/[K:\mathbb Q]\).
On the remaining pieces a Riemann-sum bound for the logarithm makes the singular contribution \(O(\epsilon)\) for arc size \(O(\epsilon)\).
This gives the required control of the singularity in addition to weak convergence.
The inspection checked the orbit normalization, the use of the two propositions and the truncation in (9)–(12).
The field and \(\lambda\) stay fixed throughout. [Truncation and subarc bounds, printed pages 223–225](../../../literature/pdf/BIR08.pdf#page=9)
