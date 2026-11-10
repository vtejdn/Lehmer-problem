---
author: Yin
---

# GHS09: integral transvection generation and its two-plane boundary

<a id="ghs09-u001"></a>
## Inspected result and scope

Use the [arXiv v1 edition](readme.md#arxiv-v1).
The inspection covers the notation and Theorem 1.1 on printed/PDF pages 2--4, the rational and integral transvection interface in Section 3.1 on pages 8--9, and the definitions and generation statements in Section 3.3 on pages 10--12.
Proposition 3.4 and its notation were also checked visually on page 12 of the retained original.
This is direct source reading and an applicability check for integer Lorentzian constructions, not an independent proof audit of Kneser's theorem, Eichler's criterion, strong approximation or the paper as a whole.

<a id="integral-transvection-groups"></a>
## Source groups and conventions

Let $L$ be a nondegenerate even integral lattice, with dual $L^\vee=\{x\in L\otimes\mathbb Q:(x,L)\subseteq\mathbb Z\}$ and discriminant group $D(L)=L^\vee/L$.
For nonzero $e\in L$, define $\operatorname{div}(e)\mathbb Z=(e,L)$.
The notation $U=\mathbb Ze\oplus\mathbb Zf$ means $e^2=f^2=0$, $(e,f)=1$.
Use the [Eichler formula already retained in L462](../../../ledger/Yin_L_G0462_v13.md#integer-generators), denoted $t(e,a)$ here.
For the source's even lattice, integral $e,a$ with $e^2=(e,a)=0$ make this an integral transvection.
Section 3.3 defines
\[
E(L)=\langle t(e,a):e,a\in L,\ e^2=(e,a)=0,\ \operatorname{div}(e)=1\rangle,
\qquad
E_U(L_1)=\langle t(e,a),t(f,a):a\in L_1\rangle
\]
when $L=U\oplus L_1$.

The source's spinor norm convention is
\[
\operatorname{sn}_K(\sigma_{r_1}\cdots\sigma_{r_s})
=\prod_j\bigl(-(r_j,r_j)/2\bigr)\pmod{(K^\times)^2}.
\]
Its groups are $O'(L)=SO(L)\cap\ker\operatorname{sn}_{\mathbb Q}$ and
\[
\widetilde{SO}^{+}(L)
=SO(L)\cap\ker\operatorname{sn}_{\mathbb R}
 \cap\ker\bigl(O(L)\longrightarrow O(D(L))\bigr).
\]
This meaning of $O'$ differs from the cone-preserving notation used by ERT19.
For a prime $p$, $\operatorname{rank}_p(L)$ is the maximum rank of a sublattice with determinant prime to $p$.
The real Witt index is the maximum dimension of a totally isotropic subspace of $L\otimes\mathbb R$.

<a id="two-plane-generation"></a>
## Exact generation input

Proposition 3.3 assumes an integral orthogonal decomposition $L=U\oplus U_1\oplus L_0$, where $U_1$ is another hyperbolic plane and $L_1=U_1\oplus L_0$.
Its parts (ii)--(iii) give
\[
E(L)=E_U(L_1),\qquad O(L)=\langle E_U(L_1),O(L_1)\rangle.
\]
Proposition 3.4 assumes additionally
\[
\operatorname{rank}_3(L)\ge5,\qquad\operatorname{rank}_2(L)\ge6
\]
and gives
\[
\widetilde{SO}^{+}(L)=O'(L)=E(L)=E_U(L_1).
\]
The proof invokes Proposition 3.3 and Kneser's Theorem 1.1, whose hypotheses include evenness, real Witt index at least two, representation of $-2$, and these local ranks.
The source attributes the foundational reflection theorem to Kneser and the transvection/orbit mechanism to Eichler; those original sources were not inspected here.

<a id="one-plane-and-cost-limits"></a>
## Limits for the selected construction

For positive definite $H$, the real signature of $H\oplus U$ has negative index one, so it cannot contain the two orthogonal hyperbolic planes required above.
Neither increasing the dimension of $H$ nor the parity restriction on chosen transvection vectors repairs that hypothesis.
The generation statements concern finite products with no uniform word-length bound, parameter-height bound or spectral-radius estimate.
They do not identify every single-plane integer isometry with a word in two fixed integral cusp groups.
In particular, the notation $E_U(L_1)$ in Proposition 3.4 must not conceal the second $U_1$ inside $L_1$.

The rational formulas of Section 3.1 are not integer normal-form algorithms: equation (10) uses the parameter $2a/(a,a)$, which need not lie in the lattice.
A rational change of basis, passage to a finite-index subgroup, or stabilization therefore needs its own integral and measure-preserving argument.
No such extension is adopted here.
The [GHS13 formula inspection](../GHS13/readme.md#arxiv-v2) remains the adequate earlier attribution for the individual transvection; this unit adds the distinct generation scope.
