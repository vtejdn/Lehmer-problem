---
author: Yin
---

<a id="tao26-u001"></a>
# Tao26-U001: Monotone first derivative and explicit local constants

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [Tao26](../../../literature/pdf/Tao26.pdf), author-hosted *Lecture notes8for247B*, Terence Tao; undated retained PDF. The provisional key uses2026access-year basis and asserts no publication/edition date.

Passages: Lemma2.4 and its proof, printed/PDFp.5, using integration-by-parts equation(4) on printed/PDFp.4.

Inspection: 2026-10-11T11:38, Yin, root text-reading of both complete relevant pages and visual inspection of retained p.5. The analytical author separately checked the primary online lemma in its original account, without a separately recorded passage-reading minute. Statement, hypotheses and exact integral identity checked; selected elementary proof reconstructed below. Other lemmas/notes pages and their downstream applications unreviewed. No independent full-source or human review.


## Exact source statement and role

For a smooth real phase phi on an interval J, if |phi'|>=c>0 and phi' is monotone, Lemma2.4 bounds the magnitude of integral_J exp(i lambda phi) by an absolute constant times1/(c lambda), for lambda>0.
Interval length does not enter that bound.
The source does not state the explicit constant4 used in the local G argument.

This is checked attribution for the classical first-derivative van der Corput mechanism.
The responsible project proof derives its explicit constant and applies it only to finitely many paid intervals.
It does not import a general stationary-phase theorem, a universal finite-type exponent or any conclusion about integer coefficients from the source.

## Direct constant reconstruction and applicability boundary

The source equation(4) integrates exp(i lambda phi) by parts with factor1/(i lambda phi').
The two endpoint terms have total magnitude at most2/(c lambda).
Since phi' is monotone and never zero,1/phi' is monotone too; its total variation is at most2/c.
The integral remainder is consequently at most2/(c lambda).
Thus4/(c lambda) is a valid explicit bound.
Smooth finite subintervals suffice; endpoint limits may be taken only after the relevant phase and integral limits have been justified in the actual application.

The project must separately prove a nonzero lower derivative bound, monotonicity, finite partition count, endpoint/cusp treatment and the cost of discarded neighborhoods.
A lower bound on |phi'| alone is inadequate, as the source's preceding discussion and Example2.2 explicitly explain.
The present unit supplies none of the original polynomial's gcd cancellation, algebraic root separation, multiplicity exponent or signed moment-tail summability; these are distinct local proof obligations.

## Search and limits

The trigger was recognition of the classical first-derivative oscillatory method during the integer single-Haar tail study.
The analytical author supplied the primary UCLA PDF locator.
Root checked the same retained p.4--5 rather than searching for a historical earliest source, which is unnecessary without a priority claim.
The author-hosted course page identifies the instructor and links this PDF; neither its URL nor the undated PDF supplies a verified edition date, so no2007date is inferred.
No full lecture audit, formal verification or G0001 completion is asserted.

<a id="original-separate-primary-lemma-reading"></a>
## Original additional primary-page reading

The [original whole local review](../../reviews/Yin_R_G0193_v1.md#whole-oscillatory-certificate-finding), dated2026-10-11T11:46, directly text-read complete printed/PDFpp.4--5 of the retained primary notes and reconstructed the selected integration-by-parts mechanism.
This was another actual reader/occurrence, distinct from the root 11:38 UTC passage check and the analytical author's earlier online lemma reading; the author's 11:36 UTC freeze is not a separately recorded reading minute.
Its higher-derivative/stationary-phase statements and other source pages were not audited.
The local reviewer explicitly read the target proof and author self-check in its initial whole inspection, so that project finding is SELF; this source occurrence supplies no independent full-source audit.
The complete local canceled-phase and finite-moment proof now belongs to [C_G398](../../../claims/Yin_C_G0398_v1.md#oscillatory-moment-reuse-and-domain).
This retention reads the existing account, without a new primary-source passage, PDF acquisition or reconstructed publication date.
