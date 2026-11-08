---
author: Yin
---

# Conditional probability in a strict Mahler shell at a fixed degree

The [finite coefficient-box criterion](Yin_C_G0870_v1.md#statement) asks whether every sufficiently narrow strict shell contains an integer polynomial.
This project deduction determines a limiting conditional probability for each fixed shell and tests what it can distinguish.

<a id="statement"></a>
## A zero or one limit

Fix \(R>1\).
In half-degree \(n\), choose uniformly from all monic reciprocal integer polynomials \(P\) of degree \(2n\) with constant one and \(M(P)<R\).
This is a finite nonempty law: coefficient \(j\) has magnitude at most \(R\binom{2n}j\), and \((x-1)^{2n}\) is admissible.
It is also the uniform reciprocal coefficient-box law conditioned on \(M<R\) at any height covering that bound.
Let \(p_n(R)\) be the probability of \(1<M(P)<R\) under this law.
If no such strict witness exists in any half-degree, every \(p_n(R)=0\).
If there is even one strict witness, then
\[
                         1-p_n(R)=O_R(n^{-1/2})
\]
as \(n\) tends to infinity, with a constant allowed to depend on a witness.
In particular \(p_n(6/5)\to1\) by the [degree-ten control](../computations/programs/Yin_J_G0144/readme.md).
The unrestricted refutation of Lehmer's gap is equivalent to this limit being one for every \(1<R<2\), by [the reciprocal reduction](Yin_C_G0870_v1.md#argument).

<a id="neutral-count"></a>
## The exact atom at one

Write \(Z_n\) for the number of measure-one inputs, with \(Z_0=1\).
Kronecker's theorem and unique factorization identify them with products of cyclotomic polynomials.
The exponents of \(x-1\) and \(x+1\) must both be even: the first fixes the constant term, and then even degree forces the second.
Every other cyclotomic polynomial is reciprocal of even degree.
Consequently
\[
       \sum_{n\ge0} Z_n y^n=
       (1-y)^{-2}\prod_{m\ge3}(1-y^{\varphi(m)/2})^{-1}.
\]
Let \(c(d)\) count all degree-\(d\) monic products of cyclotomic polynomials, allowing repetition and excluding the factor \(x\).
In odd degree the exponents of \(x-1,x+1\) have opposite parities.
Removing one copy of the uniquely odd endpoint factor therefore gives the exact identity \(c(2n+1)=2 Z_n\).
Conversely multiplying a neutral even-even product by either endpoint factor gives the two disjoint inverse branches.

The Boyd–Montgomery cyclotomic partition asymptotic, as stated in [Mossinghoff–Pinner–Vaaler, published §3.2](../audits/literature/MPV98/Yin_U002.md#unrestricted-cyclotomic-products), has the form
\[
 c(d)\sim A\frac{\exp(B\sqrt d)}{d\sqrt{\log d}}\qquad(A,B>0).
\]
Only its leading asymptotic at integer degrees is used.
In particular there is an absolute \(\kappa>0\) such that \(Z_{n-h}\ge\kappa Z_n\) for every integer \(0\le h\le\sqrt n\) and every sufficiently large \(n\).
Indeed the two asymptotic relative errors tend uniformly to zero over these indices, the algebraic and logarithmic prefactors have ratio tending uniformly to one, and \(\sqrt{2n+1}-\sqrt{2(n-h)+1}\) is bounded throughout the window.

<a id="amplification"></a>
## Many inputs from one fixed value

From any strict witness remove all its cyclotomic factors.
The resulting nonconstant \(F\) is still monic reciprocal of even degree \(2r\) and constant one: the removed endpoint exponents are even, since a reciprocal even-degree polynomial has even multiplicities at \(1,-1\), as follows from its trace representation \(x^nQ(x+x^{-1})\).
Its measure is unchanged.
For every \(j\ge1\), \(F(x^j)\) has no root of unity and has exactly the same total measure, because the \(j\)-th roots of each root \(\alpha\) contribute \(\max(1,|\alpha|)\) in product.
At half-degree \(n\) multiply \(F(x^j)\) by any neutral polynomial of half-degree \(n-jr\).
Unique cyclotomic removal recovers \(F(x^j)\), and its degree distinguishes different \(j\).
If \(T_n(R)\) counts the whole sublevel including the neutral atom, then for all large \(n\)
\[
    T_n(R)-Z_n\ \ge\ \sum_{j=1}^{\lfloor\sqrt n/r\rfloor} Z_{n-jr}
                \ \ge\ \kappa\lfloor\sqrt n/r\rfloor Z_n .
\]
Division by \(T_n(R)\) gives the asserted estimate.
The positive mass in this lower bound is entirely at \(M(F)\).
Thus a conditional probability tending to one at a fixed \(R\) can arise from a single positive value, and the proof gives no witness in a shell lying below all supplied seeds.
For \(R\downarrow1\), the unresolved input is a strict excess \(T_n(R)>Z_n\) in some degree before applying this amplification.

## Assessment history

### Decision conditional-shell

| Field | Value |
| --- | --- |
| date | 2026-11-08T02:13 |
| status | proved |
| reason | Independent review verifies the strict sublevel dichotomy at fixed threshold, with the cost and dependence on a supplied witness explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed-threshold probability](#statement) | Uniform conditional law over all reciprocal integer inputs of a fixed even degree. |
| argument | [Atom at one](#neutral-count) | Exact odd-degree identity and lower count throughout a square-root degree window. |
| argument | [Single-seed amplification](#amplification) | Exact recovery of the cyclotomic part and substitution degree at unchanged measure. |
| dependency | [MPV98 counting estimate](../audits/literature/MPV98/Yin_U002.md#mpv98-u002) | Boyd–Montgomery's unrestricted product count as reported by MPV98. |
| review | [Whole probability finding](../audits/reviews/Yin_R_G1094_v2.md#conditional-sublevel-finding) | Independent proof and model checks, retaining the fixed-threshold restriction. |

## Current assessment

[Selected decision](#decision-conditional-shell)
