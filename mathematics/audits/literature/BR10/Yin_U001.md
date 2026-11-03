---
author: Yin
---

<a id="br10-u001"></a>
# BR10-U001: Finite Stable Spaces and Rational Series

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Retained [BR10 manuscript](../../../literature/pdf/BR10.pdf), dated 2010-04-09.

Passages: Chapter 1: Proposition 5.1 and Corollary 5.4, printed pp.11–14 / PDF pp.23–26; Theorem 7.1 and Lemmas 7.2–7.3, printed pp.17–20 / PDF pp.29–32.

Inspection: 2026-09-08: coordinating-agent targeted self-review of the listed scope, supplementing the earlier lightweight intake; not a whole-book audit.


Source: [BR10](../../../literature/pdf/BR10.pdf), retained 2010-04-09 manuscript.
Date/reviewer: 2026-09-08, the coordinating agent, targeted self-review.
Scope: Chapter 1, Proposition 5.1 and Corollary 5.4, printed pp. 11-14 / PDF pp. 23-26; Theorem 7.1 and Lemmas 7.2-7.3, printed pp. 17-20 / PDF pp. 29-32.
This supplements the earlier lightweight intake; it is not a whole-book audit.

## Exact Input

For a finite alphabet and complex scalar coefficients, a formal noncommutative series S is recognizable precisely when it is contained in a finite-dimensional space stable under all prefix-removal residuals.
The smallest such space is the span of w^{-1}S.
Recognizable and rational formal series coincide.
Word reversal gives the corresponding suffix formulation used in Miy22.

## Proof Mechanism Checked

A representation (lambda,mu,gamma) supplies finitely many state series S_i(w)=(mu(w)gamma)_i, and left residuals act by the matrices mu(a).
Conversely, a stable finite basis gives those transition matrices and gamma by empty-word evaluation, recovering the coefficient formula.
Over C, subspaces of a finite-dimensional space remain finite dimensional, so the minimal residual space is finite as well; no general non-Noetherian semiring inference is needed.

Theorem 7.1's inspected proof closes recognizable series under addition, product, and proper star, using the residual Leibniz identity.
Conversely, for m=sum_a mu(a)a, coefficientwise summation of m^k gives all words with the correct matrix products.
Lemma 7.3 uses a block induction with proper-series stars, yielding scalar rational expressions for entries of m*.
Every coefficient sum is finite in each word degree.
These are formal-series operations, not assertions of operator-norm convergence after evaluation.

## Applicability and Limits

This supplies the algebraic interface in Yin_S_F0004, alongside [Miy22-U002](../Miy22/Yin_U002.md#miy22-u002).
It does not construct a residual space from arbitrary dual commutators, identify a total basis for a normal tuple, or prove bounded inverse evaluation.
The formal Wick substitution is not automatically multiplicative.
No independent second review of this book unit, source-figure audit, or full Chapter 1 exercise audit was performed.
Text extraction of the named statements and proofs was inspected locally; artifact identity remains the unchanged registered BR10.
