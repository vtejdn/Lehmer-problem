---
author: Yin
---

# Paired-sign continuants and the remaining rotating-shear word

<a id="paired-continuant-interface"></a>
## Exact question and algebraic interface

This is ordinary author Preparation, not an independent review or an adopted theorem about a larger word class.
The actual input is [C889 v2, remaining monomial-pivot type](../claims/Yin_C_G0889_v2.md#remaining-type-control), rather than its different internally balanced positive-entry family.
For $t=z+z^{-1}$, $q=2-t$, $p=2+t$, put
\[
 E_s(t)=\begin{pmatrix}t^2-3&sq\\-sp&1\end{pmatrix},\qquad s\in\{1,-1\}.
\]
For an even word length $n\ge2$ with equal sign counts and $g\ge3n$, the full polynomial is
\[
 P_{g,\boldsymbol s}(z)=z^{2g}-z^g\operatorname{tr}(E_{s_n}\cdots E_{s_1})+1.
\]
No irreducible factor is extracted in the question.

Set $x=z-z^{-1}$, so $pq=-x^2$, and define $T=\operatorname{diag}(q,x)$ over $\mathbb Q(z)$.
Direct multiplication gives
\[
 T^{-1}E_sT=\begin{pmatrix}1+x^2&sx\\sx&1\end{pmatrix}
 =F_s(x)^2,\qquad
 F_s(x)=\begin{pmatrix}sx&1\\1&0\end{pmatrix}.                 \tag{1}
\]
For example the lower left entry is $-spq/x=sx$, and the upper right entry is $sqx/q=sx$.
The same $T$ works for both signs and every word position.
It is singular at $z=1$ or $-1$, so (1) is a rational-function similarity, not an integral conjugacy at all spectral parameters.
The resulting trace equality is an identity of Laurent polynomials and therefore extends through these exceptional parameters without dropping roots or factors.

Let $(b_1,\ldots,b_{2n})=(s_1,s_1,s_2,s_2,\ldots,s_n,s_n)$ and $M=2n$.
Write $K(b_i,\ldots,b_j;x)$ for the continuant defined by $K(\varnothing;x)=1$, $K$ of length $-1$ equal to zero, and
\[
 K(b_1,\ldots,b_j;x)=b_jxK(b_1,\ldots,b_{j-1};x)+K(b_1,\ldots,b_{j-2};x).
\]
Here $F_s$ is auxiliary notation, unrelated to the internally balanced cluster matrix in C889 v2.
Induction on the product of the $F_{b_j}$ gives
\[
 F_{b_M}\cdots F_{b_1}=
 \begin{pmatrix}
 K(b_1,\ldots,b_M;x)&K(b_2,\ldots,b_M;x)\\
 K(b_1,\ldots,b_{M-1};x)&K(b_2,\ldots,b_{M-1};x)
 \end{pmatrix}.                                             \tag{2}
\]
The first case is the displayed $F_{b_1}$, with the stated empty and length-minus-one conventions.
Left multiplication by the next $F$ gives exactly the recurrence in both columns, proving the formula.
Consequently the actual word trace is
\[
 \tau_{\boldsymbol s}(x)=K(b_1,\ldots,b_{2n};x)+K(b_2,\ldots,b_{2n-1};x),
 \quad
 P_{g,\boldsymbol s}(z)=\det\left(z^gI-F_{b_{2n}}(x)\cdots F_{b_1}(x)\right).       \tag{3}
\]
The determinant of the product is one because there are $2n$ factors of determinant $-1$.
Thus (3) preserves the complete polynomial and its multiplicities.

<a id="source-applicability-boundary"></a>
## What the inspected source does and does not identify

[KP15-U001](../audits/literature/KP15/Yin_U001.md#kp15-u001) retains the original continuant recurrence, Theorem 3.1 and the Alexander substitution from the exact inspected edition.
In its notation, the first continuant in (3) is the Conway polynomial of the oriented two-bridge knot with entries $2b_1,-2b_2,\ldots,-2b_{2n}$.
The second continuant is another such open-chain polynomial, of length $2n-2$.
The source variable substitution is $x=u^{1/2}-u^{-1/2}$; the present instance is $u=z^2$.
This identifies the two summands, not their sum or the determinant with boundary eigenvalue $z^g$ as the Alexander polynomial of either knot.
Mahler measure is not additive under this sum or under subtraction from $z^{2g}+1$.
In particular, a root bound for an individual open continuant cannot be transferred to (3) without a new argument.
The paper's Theorem 6.4 is an enclosing region for roots of two-bridge Alexander polynomials, not a positive lower bound for their complete Mahler measure or a result about (3).
Its original theorem proof was not adopted for the present polynomial.

The retained [McM02 canonical scope](../audits/literature/McM02/Yin_U002.md#canonical-coxeter-gap-input) requires an actual canonical real Coxeter action.
A rational-function similarity to (1), or a topological name for its recurrence, supplies no such action on the original $2g$-dimensional integral matrix.
The [DGT23 source interface](../audits/literature/DGT23/readme.md) requires an actual graph mapping torus and its specific Alexander specialization.
No such realization or fixed mapping torus has been supplied for all the present growing sign words.
The earlier restricted pretzel result in [Smy08-U004](../audits/literature/Smy08/Yin_U004.md) does not cover arbitrary paired-sign continuants or their cyclic closure.

<a id="bounded-search-and-next-question"></a>
## Bounded conclusion and first applicability question

The bounded 10 November 2026 comparison first searched the local bibliography, contents and relevant U/L source homes for Burau, braid, Alexander, Squier and continuant interfaces.
The actual reused readings were the McM02 canonical-scope unit, DGT23 source account, L462 v5 and Smy08-U004's restricted knot paragraph.
Targeted primary discovery for the matrix/continuant and two-bridge Mahler connection led to KP15; only that newly selected primary source was acquired and prepared.
Other discovery hits about mixed-sign Coxeter mapping classes and Burau representations were not accepted as exact identifications or read deeply enough to become theorem inputs.
This is not evidence that no other identification or theorem exists.

The useful output is the exact paired-sign continuant interface (1)--(3), with its closure obstruction.
It does not add new integer inputs to the already specified word family, nor identify known near-one complete measures.
Further word sampling is not justified by this source comparison alone.
The smallest meaningful next applicability question is whether the *cyclic* continuant determinant in (3), with the dependent boundary multiplier $z^g$, has an explicit topological or canonical representation whose complete characteristic polynomial equals $P_{g,\boldsymbol s}$ up to only Laurent units and proved cyclotomic factors.
A usable answer must give the parameter map, the boundary relation and every factor; an open numerator identity or a house-only estimate would not answer it.
A matched existing complete-measure bound would close the family at its actual hypotheses; a matched source construction with certified small complete values would instead supply a concrete finite discriminator.
No such matched result was found in the inspected scope, so the present recommendation is to defer this word-search branch unless that boundary question gains a concrete source or exact construction.
