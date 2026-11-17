---
author: Yin
---
# Alternating sections of a finite group

<a id="bab18-u001"></a>
<a id="thickness"></a>
## Thickness and the order of a primitive group

For a finite group \(G\), a section is a quotient \(H/N\) with \(N\trianglelefteq H\le G\).
Write \(A_t\) for the alternating group of degree \(t\).
Babai's Definition 4.1 sets \(\theta(G)=\max\{t:A_t\text{ is isomorphic to a section of }G\}\) and calls this integer the **thickness** of \(G\).
Taking \(A_2=1\) gives \(\theta(G)\ge2\), and finiteness of \(G\) gives a finite maximum.
The subgroup \(H\) may be any subgroup of \(G\), so a list of the composition factors of \(G\) alone need not contain its largest alternating section. [Manuscript, Definition 4.1, p. 6](../../../literature/pdf/Bab18--nsf.pdf#page=6)

For a finite primitive permutation group \(G\le\operatorname{Sym}(\Omega)\) of degree \(n=|\Omega|\ge2\), Theorem 4.2 gives an absolute constant \(C>0\) such that
\[
   |G|\le n^{C\theta(G)} .
\]
Here the action is transitive and its only invariant partitions are the singleton partition and the one-part partition.
The order is the order of the permutation image, so a group acting with a kernel must first be replaced by that image.
The same \(C\) works for every \(n\) and \(G\).
Babai gives no numerical multiplier and attributes the improved exponent to Pyber, whose entry in the manuscript bibliography describes unpublished work from about 1990. [Manuscript, Theorem 4.2, p. 6](../../../literature/pdf/Bab18--nsf.pdf#page=6) · [Manuscript bibliography, p. 20](../../../literature/pdf/Bab18--nsf.pdf#page=20)

The 1982 paper states a polynomial bound in terms of restrictions on composition factors.
Liebeck and Shalev later gave a published base-size theorem from which the displayed absolute linear exponent follows directly. [1982 statement and attribution](../BCP82/Yin_U001.md#composition-factors) · [Published base theorem and deduction](../LS99/Yin_U001.md#base)
