---
author: Yin
---
# MG89-U001: self-reciprocal irreducible counts in finite fields

Date: 2026-10-15.
Human author Yin.
The f_unitary_scope reader located and downloaded the primary electronic article, read Section1 pages1--3 and visually checked page3.
Root separately read the retained title and Section1 text, visually checked the actual page3 formula and verified the official publication record.
This source reading is separate from any new arithmetic construction or project proof review.

<a id="mg89-u001"></a>
## Read; accepted classical count and applicability

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Meyn and Goetz, Self-reciprocal Polynomials Over Finite Fields, SLC B21d electronic8-page version, numbered1--8. The official work identity is B21d(1989); this electronic artifact includes an electronic-version proof note on page7 and is not the original Strasbourg scan paginated82--90.

Passages: Section1 definitions on pages1--2, Theorem1 and its proof on page2, Lemma2 and Theorem3 equation3 with the adjacent attribution on page3.

Inspection: Actual primary statement/convention reading with the displayed product/Moebius mechanism inspected in these passages. State Read. No whole-paper review, original Carlitz proof audit or comparison of all electronic-version changes.


The reciprocal of a degree-n polynomial is f*(x)=x^n f(1/x).
Here self-reciprocal means exact equality f=f*, and srim means self-reciprocal, irreducible and monic over F_q.
Such a polynomial of degree2n has constant term1.
Theorem3 gives the number S_q(n) of srim polynomials of degree2n.
Its two branches are

    S_q(n)=(q^n-1)/(2n), if q is odd and n is a power of2;
    S_q(n)=(1/(2n)) sum_(d|n,d odd) mu(d) q^(n/d), otherwise.

Accept this established count at its exact statement/applicability scope.
The project only needs the following direct substitution: for any rational prime p and any odd prime h,

    S_p(h)=(p^h-p)/(2h).

Indeed h is not a power of2, and its odd divisors are1,h with Moebius values1,-1.
This includes p=2; there is no assumption that the characteristic differs from h.
The source counts actual distinct monic irreducible polynomials of the entire degree2h, not all reciprocal polynomials or arbitrary factors of a chosen polynomial.

The inspected mechanism uses the squarefree polynomial x^(q^n+1)-1.
Its non-linear irreducible factors are srim polynomials of degree2d with d|n and n/d odd; the linear factors are treated separately.
Lemma2 inverts that finite product, and taking degrees yields Theorem3.
The source itself credits Carlitz for the earlier count; no direct reading of that earlier work is claimed.
The local specialization above is not a new project counting theorem.

## Exact role and limitations

The trigger is the new finite-prime-pool sparse-auxiliary inquiry for G0001.
This count supplies enough ACTUAL finite-field irreducibles for a proposed avoidance argument.
It does not supply sparse-multiple exclusion, a simultaneous CRT lift to an integer polynomial, integrality in a maximal order, an original norm estimate, a near-one example or any Mahler gap.
Those conclusions require their own complete argument and review.

The [official article record](https://www.mat.univie.ac.at/~slc/opapers/s21meyn.html) identifies SLC B21d(1989),8 pages and its former Strasbourg1990 publication.
Source: [retained electronic artifact](../../../literature/pdf/MG89--electronic.pdf).
This artifact has section headings but no printed table of contents; no contents transcription is fabricated.
The current input is resolved at the stated accepted-theorem scope, without claiming an exhaustive search or new original-proof audit.
