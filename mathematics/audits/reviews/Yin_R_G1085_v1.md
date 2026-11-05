---
author: Yin
---

# VG19 v2: independent review of the field identification and two real-case proof steps

## Review arrangement and exact inputs

Review performed at 2026-11-04T19:47 UTC; human record author: Yin.
This is a separately organized independent source inspection by an agent outside substantive development of the source-unit objections.
The assignment supplied fixed source and source-unit paths, page ranges and requested questions, without contributor dialogue, proof-generation notes or prior mathematical findings.
The reviewer read the original passages and formed the local findings before consulting the source unit.
The subsequent comparison used the source unit as the exact reviewed text, without modifying it or contributing a repair of the paper's arguments.

The inspected original is [VG19, arXiv:1911.10590v2](../literature/VG19/readme.md), revised 29 October 2021, with 114 PDF pages whose numbering matches the printed pages.
The original [PDF](../../literature/pdf/VG19--arxiv-v2.pdf) was read at page 4, pages 61--68 and pages 92--96, with all those pages also rendered and visually inspected.
The fixed local review input is [Yin_U001](../literature/VG19/Yin_U001.md#vg19-u001), in its working-copy text read during this review, specifically the two anchors bound below.
The page-4 Main Case condition was checked directly; the source-unit account of Section 5.9.1, pages 87--88, was not independently checked here.

This is a proof-step review and a comparison of the corresponding local source observations.
It is not a complete audit of the 114-page paper, an audit of an earlier edition, a proof of a counterexample under the full theorem hypotheses, or a review completing G0001.
The source's references [67], [81] and [102] were not read; Theorem 5.31 was examined only as stated in this paper.
No external source proof, auxiliary analytic theorem, numerical constant or associated code was independently validated by this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Field identification](#field-identification) | independently reviewed |
| [Rational-coordinate identification](#rational-coordinate-identification) | independently reviewed |
| [Uniform alphabet inference](#uniform-alphabet-inference) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Field identification](#field-identification) | [U: house to original field](../literature/VG19/Yin_U001.md#house-to-original-field) | VG19 arXiv v2, page 4 Important Nota (N)(A), Theorem 6.1 on pages 92--94, especially (6.1.10)--(6.1.11); the explicit dependency on that identification in Sections 6.2--6.3 on pages 95--96. |
| [Rational-coordinate identification](#rational-coordinate-identification) | [U: real-case obligations](../literature/VG19/Yin_U001.md#real-case-proof-obligations) | Only the first local concern: equations (5.4.9)--(5.4.14), pages 61--62, and the bound used in Proposition 5.28 on page 63. |
| [Uniform alphabet inference](#uniform-alphabet-inference) | [U: real-case obligations](../literature/VG19/Yin_U001.md#real-case-proof-obligations) | Only the second local concern: the stated representation theorem and equation (5.4.29), pages 67--68, their relation to (5.4.23) on page 65 and the uniform conclusion used in (5.4.32). |

## Field identification

Theorem 6.1 assumes a nonreal reciprocal algebraic integer alpha, beta equal to its real house, 1 < beta < theta_5^(-1), and M(alpha) < 1.176280... .
The additional assertions, including P_alpha = P_beta, assume dyg(beta) >= 260.
The page-4 global note restricts the main statements through Section 7 to the Main Case, excluding the specified polynomial compositions with exponent at least two.
The objection below uses the actual nonreal alpha and real beta premises and is unaffected by that restriction; it uses no radical family as a putative example satisfying the theorem.

On page 94 the source introduces a Q-endomorphism sigma of K = Q(alpha,beta), sending alpha^(-1) to beta^(-1) and leaving F = Q(beta) invariant.
The displayed substitution in (6.1.11) also keeps beta^(-1) fixed.
The preceding tail equality is an equality of values; it does not show that this substitution respects all algebraic relations.

The proposed field map is impossible under either usual interpretation of invariance.
If F is fixed pointwise, the nonzero element alpha^(-1) - beta^(-1) would map to zero, contrary to injectivity of a unital field homomorphism.
If invariance means only sigma(F) is contained in F, a Q-endomorphism of the number field K is still injective and, by finite dimension, surjective.
But sigma(alpha) = beta and sigma(F) contained in F imply sigma(K) contained in F.
Since F is real and K contains nonreal alpha, F is a proper subfield, contradicting surjectivity.

Even without the invariance condition, assuming a Q-field homomorphism with sigma(alpha^(-1)) = beta^(-1) already gives

    0 = sigma(P_alpha(alpha^(-1))) = P_alpha(beta^(-1)).

This is the root conclusion the proof is trying to obtain; reciprocity supplies P_alpha(alpha^(-1)) = 0.
Renaming the proposed substitution as conjugation cannot justify its existence.

The source unit's field-map objection is accepted at this exact proof-step scope.
The passage (6.1.10) to (6.1.11) does not establish the identification, and the displayed argument on pages 95--96 explicitly uses Theorem 6.1 for the house-to-original Mahler comparison.
Those uses cannot be accepted on the strength of this derivation.
This finding neither asserts existence of inputs satisfying every near-one premise nor refutes the theorem's conclusion or Lehmer's conjecture.
A valid replacement argument would need its own review.

## Rational-coordinate identification

On pages 61--62 the source groups the tail into analytic functions

    g_(q,j)(z) = sum_(k>=0) t_(q+1+j+kd) z^(kd),  0 <= j < d,

and writes its value as beta^(-(q+1)) times the sum of g_(q,j)(beta^(-1)) beta^(-j).
The polynomial rewriting coefficients h_(q,j) in (5.4.13) are integers.
Comparison at beta^(-1) gives one scalar equality; comparison in the Q-basis {1,beta^(-1),...,beta^(-(d-1))} determines individual coordinates only when their coefficients lie in Q.
The inspected text does not establish rationality of the analytic values g_(q,j)(beta^(-1)) before deducing (5.4.14), either at the first step or in the recursion.
Convergence and positivity of the sums supply no such rationality statement.

Thus the stated reason does not establish h_(q,j) = g_(q,j)(beta^(-1)).
The q-uniform analytic bound (5.4.10) cannot be transferred to the integer coefficients by that identification as written.
At the beginning of page 63, Proposition 5.28 uses precisely that transferred bound to make its remainder tend to zero.

The source unit's first real-case concern is accepted as a local failure of justification.
This does not prove (5.4.14) false for an input satisfying all source hypotheses or rule out another argument for the required remainder estimate.
It does not certify the complete proof of Proposition 5.28 or its other dependencies.

## Uniform alphabet inference

Theorem 5.31, as quoted on page 67, provides a finite integer alphabet for an individual algebraic base with no conjugate on the unit circle.
Its separate applications to gamma_s do not by themselves provide one alphabet independent of s.
The proof tries to obtain that uniformity from (5.4.23) and the representation (5.4.29).

Write B = (2^d - 1)H + 2^d for the coefficient bound claimed in (5.4.23).
On pages 67--68, (5.4.29) is expressly an identity after specialization X = gamma_s^(-1).
It need not be a polynomial identity after clearing denominators: the difference can be a nonzero multiple of the minimal polynomial of gamma_s^(-1).
It therefore does not permit the asserted polynomial coefficient comparison.
Even granting equality of the cleared polynomials, upper bounds by 2B and by 3m for their heights would not imply m <= 2B/3.
Two upper bounds for one quantity give no such upper bound on m.
Thus the displayed reasoning does not prove the claimed uniform choice m = ceil(2B/3).

Page 68 also replaces a base-dependent leading-index constant by one positive constant independent of s and concludes u_s tends to infinity.
Its references to [81] and [67] were not checked here, so this review does not decide whether an applicable external result supplies that separate uniformity.
The quoted per-base existence result and displayed height estimates alone do not discharge the uniform alphabet and leading-index obligations needed for (5.4.32).

The source unit's second real-case concern is accepted with exactly these limits.
Failure of this displayed inference does not prove that a uniformly bounded alphabet or suitable leading-index estimate cannot exist.
Possible further arguments in [67] remain outside the reviewed evidence.
