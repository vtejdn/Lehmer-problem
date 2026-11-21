---
author: Yin
---

# Quantitative height limit for multiplicatively dependent points on \(X+Y=1\)

<a id="hab09-u001"></a>
## The line, the height and the error in the degree

Let \(\mathcal M\) consist of the algebraic numbers \(x\ne0,1\) such that \(x^r(1-x)^s=1\) for some \((r,s)\in\mathbb Z^2\setminus\{(0,0)\}\).
Habegger's Theorem 1 states that for any sequence of distinct \(x\) in \(\mathcal M\), the projective tuple heights \(h(1:x:1-x)\) tend to \(S_0=m(X+Y-1)\), where \(m\) is logarithmic Mahler measure.
Theorem 4 gives, for each \(\epsilon>0\) and every such \(x\) of degree \(D=[\mathbb Q(x):\mathbb Q]\),
\[
 \bigl|h(1:x:1-x)-S_0\bigr|
   \le \frac{c(\epsilon)}D
       \exp\!\left((\epsilon+\log2)\frac{\log D}{\log\log(3D)}\right).
\]
The error is \(D^{-1+o(1)}\) as \(D\) tends to infinity. [Edition and journal locators](readme.md#edition) · [Theorem 1](../../../literature/pdf/Hab09--author.pdf#page=1) · [Theorem 4](../../../literature/pdf/Hab09--author.pdf#page=17)

The intended height is \(h(x,y)=h(1:x:y)\), with local contribution \(\log\max(1,|x|_w,|y|_w)\) weighted by the local degree and divided by the number-field degree.
The author copy's displayed equation (4) omits the logarithm before the maximum, an omission also visible in the extracted journal equation (2.1).
The printed summands would equal a positive local degree weight at almost every finite place even for \(x=y=1\), making their sum divergent.
Inserting the logarithm gives the stated Weil height, consistent with the immediately following identities \(h(z^k)=|k|h(z)\) and \(h(z)=m(P_z)/\deg P_z\) for a nonzero algebraic number \(z\) and its primitive integer minimal polynomial. [Displayed formula](../../../literature/pdf/Hab09--author.pdf#page=4) · [Power and minimal-polynomial identities](../../../literature/pdf/Hab09--author.pdf#page=5)

In particular, for \(x=\xi z^a,\ y=\eta z^b\) with \(\xi,\eta\) roots of unity, this height is \((\max(0,a,b)-\min(0,a,b))h(z)\).
The formula follows from \(|\xi|_w=|\eta|_w=1\) and the product formula, separating \(|z|_w\ge1\) and \(|z|_w<1\).
For the maximum of the two individual coordinate heights, Corollary 2 instead gives the full accumulation interval \([S_0/2,S_0]\). [Height definition](../../../literature/pdf/Hab09--author.pdf#page=4) · [Corollary 2](../../../literature/pdf/Hab09--author.pdf#page=2) · [Existing projective-height convention](../AD99/Yin_U001.md#ad99-height-obstruction-conventions)

Theorem 1 and its quantitative form concern the particular line \(X+Y=1\).
The introduction cites Bombieri, Masser and Zannier for bounded height on an irreducible curve in a torus outside the proper-coset case.
The inspected passage attributes a bound depending on the curve and gives no general-curve convergence or error estimate.
The hypotheses, both height conventions, the quantitative statement and this comparison were checked.
The factorization and analytic estimates underlying the line theorem are accepted at their stated scope. [General-curve comparison](../../../literature/pdf/Hab09--author.pdf#page=2) · [Theorem 4 and its proof](../../../literature/pdf/Hab09--author.pdf#page=17)
