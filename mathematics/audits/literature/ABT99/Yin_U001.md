---
author: Yin
---

# The sum of the points of a scale-invariant Poisson process

<a id="abt99-u001"></a>
## The density on the first unit interval

For \(\theta>0\), the scale-invariant Poisson process on \((0,\infty)\) has intensity \(\theta\,dx/x\).
Counts in disjoint intervals are independent, and the count in \((a,b]\), where \(0<a<b<\infty\), has a Poisson distribution with mean \(\theta\log(b/a)\).
Let \(T\) be the sum of the locations of its points in \((0,1]\).
This sum is finite almost surely, since its mean is \(\theta\).
Arratia, Barbour and Tavaré give the Laplace transform of \(T\) in (2.4), following its definition in (2.3), and give an integral equation for its density \(g_\theta\) in (2.5). [Edition](readme.md#edition) · [Section 2, printed pages 408–409](../../../literature/pdf/ABT99.pdf#page=2)

Write \(F_\theta(x)=\mathbb P(T\le x)\).
For \(0<x\le1\), (2.5) reads \(xg_\theta(x)=\theta F_\theta(x)\).
Thus \(F_\theta(x)=x^\theta F_\theta(1)\), with \(F_\theta(1)=g_\theta(1)/\theta\).
On printed page 410, comparing the two normalized densities in (1.2) and (3.2) identifies \(g_\theta(1)=e^{-\gamma\theta}/\Gamma(\theta)\), where \(\gamma\) is Euler's constant.
Consequently \(F_\theta(x)=e^{-\gamma\theta}x^\theta/\Gamma(\theta+1)\) throughout this interval.
The inspection checked the point process, its sum, the two displayed density equations and the normalization comparison.
The input density formulas are accepted as stated. [Section 2, equations (2.3)–(2.6)](../../../literature/pdf/ABT99.pdf#page=3) · [Section 3, immediately after (3.2)](../../../literature/pdf/ABT99.pdf#page=4)
