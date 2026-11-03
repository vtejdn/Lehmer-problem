---
author: Yin
---

# Yin20: Division Closure and Its Recursive Description

<a id="yin20-u001"></a>
## Yin20-U001: Definition IV.5.5 and Remark IV.5.6(iv)

Source: [Yin20](../../../literature/pdf/Yin20.pdf), Sheng Yin's doctoral dissertation, title-page year 2019.
The source edition and bibliographic year are not identified solely by the 2020 defense date.

Record date: 2026-09-09.
Reviewer: the coordinating agent, targeted source reading and self-review requested by the user.
Exact core locator: printed p. 60 / PDF p. 70.
Definition IV.5.5 and all of Remark IV.5.6 fit on that page.
The complete page and title page were visually inspected after rendering; text of the adjacent rational-closure discussion on printed pp. 58-59 / PDF pp. 68-69 was read for context.
This is not a whole-dissertation audit.

## Exact Statement and Conventions

Let $\mathcal A$ be a unital algebra and $\mathcal B$ a subalgebra.
Definition IV.5.5 calls $\mathcal B$ division closed in $\mathcal A$ when it contains $b^{-1}$ for every $b\in\mathcal B$ invertible in $\mathcal A$.
The division closure, also called unit-closure, is the smallest division-closed subalgebra of $\mathcal A$ containing $\mathcal B$.

Remark IV.5.6(iv) constructs it recursively:

\[
R_0(\mathcal B)=\mathcal B,\qquad
R_{k+1}(\mathcal B)=
\operatorname{alg}\!\left(R_k(\mathcal B)\cup
\{b^{-1}:b\in R_k(\mathcal B),\ b\in\mathcal A^\times\}\right),
\]

\[
\operatorname{Div}_{\mathcal A}(\mathcal B)
=\bigcup_{k=0}^{\infty}R_k(\mathcal B).
\]

For project use, $\mathcal B=A_X=\mathbb C\langle X\rangle$ is unital, and the generated algebras are unital complex algebras.
The ambient algebra determines which inverse operations are available.

## Proof Check

Each finite stage lies in every division-closed subalgebra containing $\mathcal B$, by induction.
Their increasing union is a subalgebra containing $\mathcal B$.
If an element in the union is invertible in $\mathcal A$, it appears at some finite stage $R_k$, and its inverse appears in $R_{k+1}$.
Thus the union is itself division closed and has the required minimality.
Every stage uses only finitely many algebraic operations per element, so the union is exactly the set of values of finite expressions whose inverse nodes are admissible in $\mathcal A$.

This verifies the source's recursive argument in the unital setting consumed here.
It does not require a topology, completeness, freeness, or the assumption that every nonzero element of $\mathcal A$ is invertible.

## Consequence for Project Terminology

The phrase "bounded scalar rational expressions" in the project conventions is an explanatory description of $\operatorname{Div}_M A_X$, not an additional algebra or stronger definition.
Prefer "division closure in $M$" as the standard name and specify the ambient algebra.

Replacing $M$ with $U(M)$ gives the affiliated division closure.
Under the separate MSY23 hypotheses this is an embedded free field.
That field identification is a theorem, whereas the recursive description is simply an equivalent construction of division closure.

The source distinguishes this from matrix rational closure: Definition IV.5.1, printed p. 58, uses entries of inverses of polynomial matrices invertible over the ambient algebra; Remark IV.5.6(ii), p. 60, states that it contains division closure.
The well-defined rational-function evaluations in Remark IV.5.3 use the source's matrix-representation evaluation convention.
This should not be read as identifying all such evaluated functions with finite scalar expressions admissible in the same ambient algebra without a further equality theorem.

## Evidence and Limits

The local PDF has 109 pages.
Its title page was read as 2019, and the defense page records 2020-01-27.
Selected text was extracted locally and the core p. 60 was checked visually; no source PDF was edited, replaced or newly downloaded.
An initial console print encountered a Windows encoding error after the extraction file had been written; subsequent UTF-8 reading and page rendering supplied the actual evidence.

The public Saarland repository metadata was located separately for bibliographic identity.
No equality of bytes with the public download was asserted.
The scoped reading does not audit Chapter IV as a whole, its Cohn references, or the adjacent matrix-closure theorems.
No new project claim ID, numerical verification, formalization or novelty assessment is assigned to this standard definition.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Yin20, the supplied 109-page doctoral dissertation with title-page year 2019; its defense date 2020-01-27 and public repository metadata are separate facts. Printed Arabic page = PDF page minus 10. Other source editions retain their separate exact locators.

Passages: Definition IV.5.5 and all of Remark IV.5.6, printed p. 60 / PDF p. 70; adjacent rational-closure text, printed pp. 58-59 / PDF pp. 68-69, read for context.

Inspection: 2026-09-09: targeted source reading and self-review, including visual inspection of the complete core page and title page. This does not audit all of Chapter IV, the Cohn references or adjacent matrix-closure theorems. Public metadata was located separately without asserting byte equality with the supplied artifact; no independent artifact review, numerical verification, formalization or novelty assessment is claimed for this unit.
