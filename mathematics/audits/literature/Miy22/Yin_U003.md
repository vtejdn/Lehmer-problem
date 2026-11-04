---
author: Yin
---

<a id="miy22-u003"></a>
# Miy22-U003: Commutators as Residual Operators

- Source: [Miy22](../../../literature/pdf/Miy22.pdf), published version.
- Locators: Lemmas 3.2-3.3, pp. 9-10; Proposition 3.9, pp. 16-17; Theorem 3.1 proof and Remarks 3.10-3.11, pp. 17-18.
- Record: 2026-09-08, audit by the coordinating agent and independent commutator-check agent; definitions and universal identities reconstructed, rendered formulas inspected, and a finite exact word-action check performed separately.
- Kind: source proof mechanism.
- Dependencies: [U001](Yin_U001.md#miy22-u001), [U002](Yin_U002.md#miy22-u002).

## Polynomial Cut Formula

Use $M,P,U_w,r_i$ from U001, with $[T,a]=Ta-aT$.
The fundamental identity is

\[
[r_i^*,s_j]=\delta_{ij}P_\Omega.
\]

On every nonempty word, the left and right actions commute; the vacuum contributes the displayed rank-one defect.
Lemma 3.2 gives

\[
[r_i^*,U_k(s_j)]
=\delta_{ij}\sum_{p=0}^{k-1}U_p(s_j)P_\Omega U_{k-1-p}(s_j),\qquad k\geq1.
\]

The source proof uses the Chebyshev recurrence and the commutator Leibniz rule.
With the sum denoted $S_k$, direct recurrence gives

\[
s_jS_k=S_{k+1}-P_\Omega U_k(s_j)+S_{k-1},\qquad S_0=0,
\]

which verifies the induction, including the $U_{-1}=0$ boundary.

Applying Leibniz across runs in $v$ yields the equivalent cut formula

\[
[r_i^*,U_v]=\sum_{v=p i q}U_pP_\Omega U_q.
\]

Because $U_q^*=U_{q^{\mathrm{rev}}}$, the vacuum projection retains exactly the cut with $q=w^{\mathrm{rev}}$ when applied to $e_w$.
Thus Lemma 3.3 is

\[
[r_i^*,U_v]e_w=
\begin{cases}
e_p,&v=p i w^{\mathrm{rev}},\\
0,&\text{otherwise}.
\end{cases}
\]

The suffix is $i w^{\mathrm{rev}}$, not $w^{\mathrm{rev}}i$.
Empty $v$ gives zero; empty $w$ removes a terminal $i$; removing the whole word returns the vacuum, not zero.
Each polynomial commutator is finite rank.

## Bounded Coefficients and Residual Spaces

Let $a\in M$ and write $a\Omega=\sum_v\alpha_ve_v$, where $\sum_v|\alpha_v|^2<\infty$.
Then

\[
[r_i^*,a]e_w=\sum_p\alpha_{p i w^{\mathrm{rev}}}e_p.
\]

The extension from polynomials uses $L^2$ convergence, not an unproved operator-norm convergence of word truncations.
For polynomial truncations $a_N\to a$ in $L^2$, both $a_N U_w\Omega\to aU_w\Omega$ and the analogous expressions involving $r_i^*e_w$ converge, since right multiplication by a fixed $U_w\in M$ is $L^2$-bounded.
This justifies passage in each commutator column.
Each residual coefficient sequence also converges in $\ell^2$.

Every nonempty suffix $t$ has the form $i w^{\mathrm{rev}}$.
Consequently, finite ranks for all $d$ commutators imply that the right residual space of $Z=\sum_v\alpha_vX^v$ lies in the span of $Z$ and the finitely many commutator ranges, hence is finite dimensional.
By U002, $Z$ is recognizable and rational.

This is the algebraic half of Proposition 3.9.
Concluding that the original $a$ lies in bounded division closure still requires the analytic realization in [U004](Yin_U004.md#miy22-u004).
The coefficient-to-word map is not multiplicative.

## Closure Direction of the Bounded Theorem

Let $\mathcal C=\{a\in M:[r_i^*,a]\text{ is finite rank for every }i\}$.
The Leibniz identity makes $\mathcal C$ a unital algebra containing $P$.
If $X\in M_n(\mathcal C)$ is invertible in $M_n(M)$ and $D_i=I_n\otimes r_i^*$, then

\[
[D_i,X^{-1}]=-X^{-1}[D_i,X]X^{-1}.
\]

A finite matrix of finite-rank entries is finite rank on $\mathcal F(H)^n$.
Its products with bounded operators remain finite rank, so every entry of $X^{-1}$ belongs to $\mathcal C$.
Hence $C_{\mathrm{rat}}(s)\subseteq\mathcal C$.
Proposition 3.9 supplies the reverse inclusion into $C_{\mathrm{div}}(s)$; together with the defining inclusion $C_{\mathrm{div}}\subseteq C_{\mathrm{rat}}$, this proves their equality with $\mathcal C$.

The norm-closure inclusion uses inverse-closedness of the unital $C^*$-algebra $A\subseteq M$, or directly the norm realization from U005.
It does not identify $A$ with the smaller rational algebra.

## Right Creation, Adjoints, and Dual Systems

The right semicircular operator $r_i+r_i^*$ commutes with every $s_j$, hence with $M$, by its strongly closed commutant.
Therefore, for $a\in M$,

\[
[r_i,a]=-[r_i^*,a],\qquad
[r_i^*,a]^*=[r_i^*,a^*].
\]

Remark 3.11 permits replacing $r_i^*$ by any **bounded dual system for the same semicircular tuple**, meaning bounded $D_i$ with $[D_i,s_j]=\delta_{ij}P_\Omega$: $D_i-r_i^*\in M'$, so the commutators agree on $M$.
This does not prove the corresponding theorem for a general operator tuple merely admitting a dual system; the paper explicitly leaves that question open.

## Verification and Reuse

The universal word and closure calculations above were checked algebraically by two agents.
A separate exact computation exercises finite word cases without truncating intermediate support.
The native program and exact J locator for the historical 64,325-item check have not been located in the selected current computation index/program metadata.
The recorded result and rerun scope remain historical evidence; reproducing them requires that native input, and no new run or claim that the original program never existed is made.
Its evidence concerns those finite cases only; it does not prove the bounded analytic converse or the affiliated theorem.

Use this unit to translate a finite-rank commutator hypothesis into a finite residual space, to prove the rational-to-finite-rank direction, and to normalize suffix/reversal and adjoint signs.
Never apply its bounded-operator formulas directly to an arbitrary affiliated $u$; the domain-safe replacement is [U006](Yin_U006.md#miy22-u006).

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Miy22, the retained 24-page published Journal of Functional Analysis 283 (2022), article 109609, DOI 10.1016/j.jfa.2022.109609. Printed and PDF pages agree, treating the opening article page as p. 1. The related 20-page arXiv preprint was not compared line by line; its locators are not substituted here.

Passages: Lemmas 3.2-3.3, pp. 9-10; Proposition 3.9, pp. 16-17; Theorem 3.1 proof and Remarks 3.10-3.11, pp. 17-18.

Inspection: 2026-09-08: universal word and closure identities reconstructed and checked by two agents. The recorded exact computation covers only finite word cases; it proves neither the analytic converse nor the affiliated theorem. Bounded dual systems remain for the same semicircular tuple, and bounded formulas do not transfer silently to arbitrary affiliated operators.
