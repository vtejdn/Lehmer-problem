---
author: Yin
---

# The26-U001: prime-binomial irreducibility attribution and exact revision boundary

Original source reading: 2026-10-09, as recorded in [L_G159](../../../ledger/Yin_L_G0159_v1.md#prime-binomial-source-attribution).
This maintenance retains that actual statement and attribution record, rather than performing another source inspection.

<a id="the26-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Official Mathlib.FieldTheory.KummerPolynomial documentation and the directly inspected source revision 389347a7c1cfa76f6bd5be2ca35d4cb621610ad3. The subsequently retained live documentation links revision 6be3d352cec3ceabd28bf85266d28646e02f1975; these are distinct recorded source versions.

Passages: Native declaration X_pow_sub_C_irreducible_iff_of_prime in the [retained official HTML](../../../literature/pdf/The26/documentation-20261009.html#X_pow_sub_C_irreducible_iff_of_prime), and [KummerPolynomial.lean at the directly inspected revision](https://github.com/leanprover-community/mathlib4/blob/389347a7c1cfa76f6bd5be2ca35d4cb621610ad3/Mathlib/FieldTheory/KummerPolynomial.lean).

Inspection: Read statement and recognized-known-result attribution on 2026-10-09. Both displayed declarations were compared at the exact field/prime/no-root hypotheses and conclusion. The recorded norm/Bezout mechanism matches the complete elementary argument retained in L159. No full software proof audit, whole-revision equivalence, local Lean compilation or formal verification was performed.


**Read, statement and attribution scope.**
The original directly inspected revision is not replaced by the later source link in the retained HTML.
The old complete review account in [R_G58](../../reviews/Yin_R_G0058_v1.md#short-order-capacity-independent-review) preserves its initial mathematical-domain request and the later domain/HTML/version-distinction reread.
Its original independent label does not establish unrecorded initial isolation.

## Exact statement and hypotheses

For every field K, every prime positive integer q and every a in K, the polynomial X^q-a in K[X] is irreducible if and only if there is no b in K with b^q=a.
The notation X_pow_sub_C_irreducible_iff_of_prime uses the polynomial indeterminate X, exponent q and constant polynomial C(a).
The field hypothesis and primality of q are part of the statement; no arbitrary composite-exponent irreducibility theorem is substituted.
The original reading found this precise declaration in the official documentation after a bounded local search for binomial irreducibility and Capelli found no matching project input.
That local search was not an exhaustive absence or novelty claim.

## Attribution and local role

The prime-binomial step is a recognized general field fact, with no priority claim.
For the Lehmer-radical application, K=Q(alpha), q is a rational prime greater than forty, and the complete project argument first proves that alpha has no q-th root in K.
It then proves the required irreducibility directly by the root-product and Bezout argument.
The source is attribution for that known fact, rather than an extra proof premise, an irreducibility assertion for an arbitrary composite exponent or a formalization of the project result.
The [complete project radical proof](../../../claims/Yin_C_G0376_v2.md#irreducible-lehmer-radical-control) retains the actual all-q, fixed-measure, power-degree-drop and singleton-prime restrictions.

## Inspection and version limits

The directly inspected source revision was 389347a7c1cfa76f6bd5be2ca35d4cb621610ad3.
The subsequently retained live documentation links source revision 6be3d352cec3ceabd28bf85266d28646e02f1975.
The two displayed prime-binomial declarations were compared with the same field, prime and no-root hypotheses and the same irreducibility conclusion.
No equivalence of their entire source files or whole revisions was asserted.
The reading and comparison establish the recorded statement attribution only; they do not report a local Lean run, a complete software-proof inspection, a complete website mirror or new source acquisition.
Current retention preserves the original reading date, exact revisions and limited comparison, without upgrading its inspection depth or retrospectively certifying an independent arrangement.
