---
author: Yin
---

<a id="smy15-u001"></a>
# Smy15-U001: Salem numbers in a fixed Salem field

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [Smy15](../../../literature/pdf/Smy15.pdf), retained25-page author rendering Salem_survey220315.pdf.

Passages: Lemma2 and Proposition3, printed/PDFpp.2--4, including the displayed proof and its final strengthening note.

Inspection: 2026-10-11, root AI for Yin; direct complete text reading of the selected statements and displayed proofs, visual inspection of p.3. Original Salem publications and other survey sections not newly audited.


For a genuine Salem number tau of degree d, every positive integral power is a Salem number of the same degree.
If tau' is any Salem number in K=Q(tau), then Q(tau')=K; if tau'>tau, the quotient tau'/tau is again Salem.
There is a smallest Salem number tau_1 in K, and every Salem number in K is a positive integral power of tau_1.
The source expressly notes that its latter statements strengthen the cited Salem formulation by omitting an initially assumed full-degree condition.

The selected proof checks power-degree preservation, the real trace subfield, exclusion of a lower-degree Salem element via nonreal embeddings, compatibility of the inverse automorphism, the unique expanding conjugate of the quotient, and discreteness from finitely many bounded minimal polynomials.
These displayed steps were read.
The classical fixed-field statements are accepted at their exact scope; no degree-uniform smallest Salem number, regulator bound, algorithm or unrestricted Lehmer reduction follows.

Current use distinguishes the full ring of integers from the actual order Z[alpha].
Passing to the subgroup of powers that are units of that order, showing equality of generated orders after a permissible generator change, and converting an affine two-unit norm identity into an actual Laurent lift require the separate local argument.
The source alone supplies none of those order, denominator, word-length or arithmetic-income bounds.

The search was triggered by recognizing cyclic relative-unit behavior while generalizing the exact quartic lift.
Local L31 supplies the reciprocal involution but no generator theorem; MS05's introduction states the related full-degree fact.
The already retained Smy15 supplies the precise stronger statement and its displayed proof, so no new source acquisition or original-priority search was needed.
The earlier [Smy15 construction-only acceptance](Yin_U002.md#smy15-u002) remains at its original scope.
