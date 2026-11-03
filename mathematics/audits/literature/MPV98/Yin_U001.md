---
author: Yin
---

<a id="mpv98-u001"></a>
# MPV98-U001: Central perturbation intervals and exact trace scaling

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [MPV98 author version](../../../literature/pdf/MPV98--author-ps.pdf), an undated prepublication PostScript version publicly linked by coauthor Pinner, converted to a19-page PDF for reading. The placeholder journal header is retained. This is distinct from the published Math.Comp.67(224)(1998),1707--1726 article. Provenance.

Passages: Author-version pp.2--3: cyclotomic perturbation context and Theorems2.1--2.2; pp.3--4 trace reduction; pp.4--6 monotone root-count and capacity proof mechanism. All locators are internal author/PDFpages, not journal pages.

Inspection: 2026-10-11T13:54, Yin, root direct AI reading and self-check. The full first7pages were text-read; complete pp.2--3 were rendered and visually checked because extraction drops signs and Greek letters. Exact statements, root/endpoint normalization and scaling checked. Capacity identities are read as established source inputs; their cited original proofs and the entire article were not re-audited.


## Separate original review reading

The [original central-descent whole review](../../reviews/Yin_R_G0201_v1.md#whole-central-descent-finding), recorded 2026-10-11T14:10, separately text-read complete author-version pp.2–3 and rendered and visually inspected them, then text-read the p.4 trace reduction.
The inspected version remained the same undated author PostScript converted to19-page PDF, without journal-version equivalence.
This is distinct from the original central source unit's 21:54 first7pages text and pp.2–3 visual record.
The project finding's known initial author-self-check exposure establishes SELF for that project whole; it does not erase these actual primary-page reading facts or create an independent source-proof audit.
This retention performs no new PDF reading, conversion, acquisition, proof inspection or comparison of source editions.

## Exact accepted statements

Theorem2.1: if f is a monic real polynomial of even degree2N>=2 with all roots on the unit circle, then the set of beta in C for which all zeros of f(t)-beta t^N remain on the circle is a closed real interval of length at most4.
Equality can occur only for f=t^(2N)+c t^N+1.

Theorem2.2: if p is monic real of degree N>=1 with all roots in[-1,1], the set of alpha in C for which all roots of p-alpha remain in[-1,1] is a closed real interval of length at most2^(2-N).
Equality can occur only when p=2^(1-N)T_N+c, with T_N the usual Chebyshev polynomial.

These established theorems are accepted at exact statement/applicability scope.
The retained proof discusses endpoint/repeated-root exclusions, Rolle root counting, transfinite diameter and its polynomial preimage property.
This reading does not constitute an independent proof audit of the potential-theory inputs or the equality characterization.

For the G trace convention Q(x) monic of degree s on[-2,2], set p(y)=2^-s Q(2y).
It is monic on[-1,1], and Q-lambda corresponds to p-2^-s lambda.
Thus the admissible lambda interval has length at most4.
This is a direct normalization check, not a new capacity theorem.
At most5 integer shifts can lie in this interval.

## Domain and arithmetic limits

The all-circle/all-interval hypothesis is essential.
A genuine Salem trace polynomial has one root above2, so Theorem2.2 cannot be invoked on it directly.
It can apply after a proved shift puts every trace root in[-2,2].
Nor does the interval-length bound control Mahler measure immediately outside the interval, distance of its endpoints from integers, or all possible coefficient lines at unbounded degree.

For f(0)=-1, the source separates the anti-reciprocal case, in which the central coefficient is zero and the admissible perturbation set is the singleton0.
In the reciprocal case f(0)=1, original roots at+/-1 have even multiplicity and map to trace endpoints with half that multiplicity.
Those factors cannot be dropped when applying the trace convention.

The author version p.2 explicitly records the classical identity for Lehmer's polynomial

    P_L=Phi_1^2 Phi_2^2 Phi_3^2 Phi_6-t^5.

This existing construction is attributed to the source, not introduced as new G work.
Its resultant-unit motivation and later finite searches are contextual; the historical numerical counts and algorithmic complexity are not reverified or used to settle the current Task.
Theorem4.1's integer-shift classification is not adopted by this selected unit.

## Search and acquisition boundary

The source was located during the bounded reuse screen for G0001 central integer-coefficient descent.
The exact title and coauthor's institutional publication list led to the publicly linked original PostScript.
The AMS PDF request encountered a browser challenge and supplied no usable PDF; no challenge was bypassed.
The author's independent public copy was retrieved and converted in safe mode, preserving its own pagination and placeholder header.
The comparison is to that retained author artifact only; no journal byte/version equivalence is assumed.

The new G question is a completely scoped one-step Salem trace criterion and its full Mahler consequences.
Such deductions require their own argument and review; this source unit supplies the known framework and its capacity/normalization boundary, not a uniform gap.
