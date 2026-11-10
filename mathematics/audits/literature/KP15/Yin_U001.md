---
author: Yin
---

# KP15: the open continuant and Alexander interface

<a id="kp15-u001"></a>
## Inspected scope

The inspected source is the [arXiv v2 edition](readme.md#yin-arxiv-v2).
Text inspection covered its contents, Section 2 equations (1)--(2), Theorem 3.1, Section 5's substitution and Lemma 5.1 with its short matrix proof, and Theorem 6.4 with its displayed argument.
The retained local PDF's pages 1, 3, 6 and 11 were also text-extracted and checked against the online text.
No diagram was visually reviewed; the attempted web screenshots were unavailable.
This is statement, convention and applicability Preparation, not an independent audit of the knot-theoretic identification, the cited Siebenmann/Conway theory or the root-region proof.

<a id="euler-continuant"></a>
## The exact recurrence and source identification

For $m\ge1$ and nonzero integers $b_1,\ldots,b_m$, the source's extended Euler continuant $D_m(b_1,\ldots,b_m)(X)$ is the determinant with diagonal $b_jX$, upper diagonal $-1$ and lower diagonal $1$.
With $D_{-1}=0$ and $D_0=1$, equation (2) is
\[
 D_j=b_jX D_{j-1}+D_{j-2}.
\]
Theorem 3.1 on printed/PDF page 6 identifies it as the Conway polynomial of the oriented two-bridge link $C(2b_1,-2b_2,\ldots,(-1)^{m-1}2b_m)$.
Its Alexander substitution on page 11 is $X=u^{1/2}-u^{-1/2}$.
Lemma 5.1 uses the Fibonacci matrix $\begin{pmatrix}X&1\\1&0\end{pmatrix}$ and its eigenvalues $u^{1/2},-u^{-1/2}$.
Theorem 6.4 on pages 16--17 encloses Alexander roots in $-3/2<\operatorname{Re}\alpha<3+2\sqrt2$, with $3-2\sqrt2<\alpha<3+2\sqrt2$ for real roots.
It supplies no complete Mahler lower bound in the inspected passage.

<a id="cyclic-applicability-limit"></a>
## Cyclic-boundary limitation

The source identification is for an open continuant.
The [separate author derivation](../../../drafts/Yin_D_G0024.md#paired-continuant-interface) identifies the rotating-shear trace as the sum of two such continuants, followed by a determinant closure with multiplier $z^g$.
Neither that sum nor that closure is identified by Theorem 3.1 with the same two-bridge Alexander polynomial.
The source therefore supplies terminology and an exact open-chain interface, without supplying a complete-measure theorem for the project word.
