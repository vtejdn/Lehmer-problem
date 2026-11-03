---
author: Yin
---

# Retained project review: Frobenius saturation and exact primitive auxiliary denominators

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0194_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="saturated-resultant-independent-review"></a>

### Separate complete noncontributor review

On 2026-10-10 the assigned resultant_research AI for Yin independently read and checked the complete proof in Sections1-4, its reuse interfaces and its final scope.
The reviewer supplied none of the saturated-order, interpolation, primitivity, adjugate or radical-lift derivations.
It had shared G0001 context, had previously reviewed D61, and received the author's present statement and review checklist.
This is therefore a separately organized noncontributor review, not a blind or human review.
No mathematical defect or required correction was found.
This review was appended without changing the preceding author text.

The hypotheses force d even: a reciprocal odd-degree polynomial has -1 as a root, which the irreducible nontorsion domain excludes.
Consequently the complete squared-root polynomial satisfies Q(z^2)=P(z)P(-z) with the displayed sign.
Modulo2, equality with P(z^2) and injectivity of polynomial substitution z^2 prove Q=P modulo2 coefficientwise, so W=(Q-P)/2 is integral.
Evaluation on all d conjugates gives Norm(W(alpha))=R/2^d.
This is exactly the determinant of its multiplication matrix in the monic power basis of O=Z[alpha], including when O is not maximal.
Under saturation this determinant is plus or minus one.
The integral inverse matrix applied to the class of1 produces a genuine inverse B_2 of W in O, with its unique degree-less-than-d representative; it is not merely an inverse in the ambient field or a localization.
Monic division then yields the integral A_2, and the degree of B_2 Q-2 is less than2d, giving deg A_2<d.
Identity(4) and Q-P=2W establish both ideal inclusions in(2).

The quotient by (P,2) has the actual free F2 basis1,t,...,t^(d-1).
Thus compatibility of the prescribed residues requires D(t^2-t-1) to vanish there.
The strict degree inequality2<d forces D even, with no squarefreeness requirement on P modulo2.
The constructed seed attains2.
This correctly keeps the degree-two case outside the conclusion and does not invoke an integral comaximal Chinese remainder theorem.

The primitivity proof uses the unit hypothesis at the exact point required: if c is the content of f_2, then f_2(alpha)/(c alpha)=2/c is a rational algebraic integer, so c divides2.
If c=2, write f_2=2g.
In an identity f_2-2t=P H, reduction modulo2 gives Pbar Hbar=0 in F2[t].
Since P is monic, Pbar is nonzero and the polynomial ring is a domain, so H is divisible coefficientwise by2.
The same argument for f_2-2(t^2-1)=Q J uses the nonzero monic Qbar.
Dividing both identities therefore gives an integral seed g with forbidden scalar1.
This argument does not require the quotient F2[t]/Pbar itself to be a domain.
Thus f_2 is primitive.
Its nonzero evaluation2alpha proves nonvanishing and the stated degree upper bound follows directly from the bounded Bezout degrees.

Nonzero resultant ensures P and Q are coprime over Q, so a pair of coefficients both of degree less than d representing any fixed scalar is unique.
The explicit scalar-2 pair therefore identifies the actual signed L174 adjugate pair as (R/2)(A_2,B_2), after its sign convention is fixed.
It follows that f_R=(R/2)f_2 and that its positive coefficient content is exactly |R/2|=2^(d-1).
The primitive polynomial f_R/content(f_R) is sign(R) f_2; the remaining signed scalar is accordingly plus or minus2.
Keeping the sign in this way is valid even though the reciprocal setting also has a stronger positive-square resultant interface elsewhere.
No estimate on the size of the integral inverse of W follows merely from its determinant, and the proof explicitly avoids that inference.

For each odd q, the qth roots above one nonzero base conjugate form a full fiber.
Squaring sends this fiber bijectively to the full qth-root fiber above its square because multiplication by2 permutes the qth roots of unity.
If different base conjugates have the same square, their entire fiber contributions still occur with the correct multiplicities.
This proves Q_q=Q_0(t^q) as a full polynomial.
Evaluating that polynomial on all q roots in each original fiber repeats the base factor exactly q times, proving the signed identity R_q=R_0^q.
Grouping the moduli in the same way proves M(P_q)=M(P_0), without an asymptotic argument.
Irreducibility of P_q is explicitly assumed in Section3 and separately supplied for the Section4 application; reciprocal unit status and nontorsion then hold at its actual degree eq.

Substitution in the base scalar-2 Bezout identity preserves integrality and gives coefficient degrees below eq.
Uniqueness therefore identifies this substituted pair with the actual degree-bounded pair for the lifted input.
The degrees of A_0P_0 and B_0Q_0 are at most2e-1, so the stated seed bound (2e-1)q+2 accounts for both outside multipliers.
Polynomial substitution preserves coefficient sum norm; the triangle and product inequalities yield C_0 even if supports overlap or leading terms cancel.
The general primitivity proof applies to every irreducible lift.
All subsequent reversal and degree statements correctly refer to the actual seed degree, rather than forcing equality in this upper bound.

The complete retained L174 cancellation, characteristic-two integrality, rational-functional-equation nonvanishing and actual-reversal arguments apply to the scalar-2 evaluations at the reciprocal conjugates.
They give a nonzero integer auxiliary, with P_q an integral factor, and an actual reciprocal integer cofactor after removal of the initial monomial.
The cubic coefficient bound includes both summands and the division by2.
Mahler multiplicativity with the complete factorization then gives exactly(10), including any scalar in C_q; its nonnegativity follows because C_q is a nonzero integer polynomial.
These are fixed-base bounds, and C_0 is not asserted uniformly bounded over all saturated inputs.

For the concrete input, the reviewer read L66's retained exact R_(1,2)=2^10 control and its normalized Frobenius-module section, and L159 Section6 with its explicit source-scope paragraph.
L159 invokes exactly L80's accepted statement-level consequence m>=log(2)/(4e) from Dim19 v1; the reviewer read that interface as well.
At degree ten this excludes a qth root in the original Lehmer field for each prime q>40, and L159's displayed root-product/Bezout and field-degree argument gives actual irreducibility of P_0(t^q).
The already retained degree-ten Salem classification gives eight unit-circle roots.
Each has q unit-circle preimages, hence8q actual unit-circle embeddings of the irreducible lift.
The full signed saturation and primitive-content conclusions therefore apply to those genuine inputs.
No fresh numerical resultant, source-code rerun, original Dim19 proof audit or new source acceptance is asserted here.

This complete written review used no new computation, finite scan, source acquisition or literature search.
The work correctly acknowledges the earlier Frobenius-module framework and the reused L174 auxiliary mechanism.
It establishes exact scalar2 and exact adjugate content throughout the stated saturated class, plus bounded complete primitive seed/cofactor cost along the specified fixed-base irreducible odd lifts.
Its unit-circle example confirms that the stronger unnormalized evaluation bound likewise need not survive primitive normalization as an exponential floor.
The examples retain fixed positive total Mahler measure and need not be Salem; they establish neither a vanishing-measure sequence nor uniform inverse/cofactor control in such a sequence.
The unrestricted G0001 target and any fixed retention remain separate from this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original whole saturated-resultant finding](#saturated-resultant-independent-review) | unknown |
| [Original contributor self-check account](#saturation-original-contributor-self-check-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original whole saturated-resultant finding](#saturated-resultant-independent-review) | [Entire original frozen saturation and lift proof](../../ledger/Yin_L_G0194_v1.md#retained-saturated-resultant-proof) | Actual original2026-10-10day-precision whole D62 Sections1--4/equations(1)--(10), exact reuse interfaces and final scope: every monic reciprocal irreducible nontorsion degree>=4/constant1/full squared-conjugate polynomial/abs resultant2^d, coefficientwise Frobenius/actual-order multiplication inverse/no maximal-order assumption/exact ideal and least interpolation scalar2, complete primitive seed and precise actual signed adjugate/content2^(d-1)/no uniform inverse-cost inference, every odd positive q with irreducible fixed-base lift/full fibers and multiplicities/signed resultant/Mahler identity/substituted unique pair/degree and complete coefficient bound, full nonlinear auxiliary and reciprocal cofactor cost with scalars, original-Lehmer actual prime q>40 degree10q and8q unit-circle conjugates at the original accepted Dim19-v1 statement depth, all fixed-positive-measure/not-necessarily-Salem/no-near-one-uniformity/source/nonexecution boundaries. The original whole scope is not narrowed. |
| [Original contributor self-check account](#saturation-original-contributor-self-check-finding) | [Original saturation argument and contribution/self-check section](../../ledger/Yin_L_G0194_v1.md#retained-saturated-resultant-proof) | Actual original2026-10-10day-precision Contribution/self-check account: coordinator supplied every new saturated-order inverse/ideal/interpolation/primitivity/adjugate content/substituted bounded-cost seed/unit-circle radical implication and reused the disclosed fixed auxiliary/resultant/irreducibility interfaces. Preserve the exact then-pending record; no extra original whole author-review event or independently repeated source proof is invented. |

## Exact retained initial-arrangement boundary

All original90lines of the whole written review, original day-precision date, complete verdict/scope, prior-review disclosure, author-text-retention assertion and source/nonexecution boundary remain fixed.
The reviewer supplied none of the saturation, interpolation, primitivity, adjugate or radical-lift derivations.
It had shared G0001 context, had previously reviewed D61 and received the author's present statement and checklist.
Earlier review of D61 or of other fixed inputs is not a new contribution to the D62 target proof.
The actual mathematical contents of the shared G0001 context beyond the stated receipt, and the complete initial target arrangement, are not retained, so isolation is not established either.
Receiving a proof for checking does not by itself show prior shared target derivation.
The entire original whole finding therefore remains UNKNOWN for independent-review purposes.
The actual coordinating-author Contribution/self-check account is separately SELF below at its exact recorded scope.
No extra historical whole author review is inferred, and a current authored whole SELF cannot close the old whole UNKNOWN.
The original Dim19-v1 accepted statement consequence and exact native-resultant inputs retain their prior depths; no source proof or numerical run is added.

<a id="saturation-original-contributor-self-check-finding"></a>
## Original contributor self-check account

Date: 2026-10-10.
The exact original Contribution/self-check and then-pending account follows.

The coordinator supplied every new implication: saturated determinant to a unit in the actual order, the exact ideal and interpolation minimum, primitivity and exact adjugate content, substituted bounded-cost seeds, and the unit-circle radical application.
The proof reuses L174's already reviewed auxiliary argument, L66's retained exact resultant, and L159's actual irreducibility theorem at its disclosed source depth.
No fresh numerical calculation, J, source proof audit or exhaustive literature search is claimed.
Full noncontributor review is pending.
