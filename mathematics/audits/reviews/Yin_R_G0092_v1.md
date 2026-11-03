---
author: Yin
---

# Retained project review: Exact resultant content collapse in an irreducible reciprocal family

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0193_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="exact-resultant-content-independent-review"></a>

### Separate complete noncontributor review

On 2026-10-10 the assigned resultant_research AI for Yin independently reviewed the entire argument, Sections1-4 and its reuse/conclusion boundaries.
The reviewer contributed none of the family selection, irreducibility argument, ideal or interpolation calculation, adjugate normalization, or auxiliary/cofactor estimates.
It had shared G0001 context and received the author's proposed result and requested review points, so this is a separately organized noncontributor review, not a blind or human review.
The exact pre-review author file had The full preceding author text was retained unchanged when this review was appended.
No mathematical defect or required proof correction was found.

For irreducibility, a proper factor of X^p-beta over K really does give a selected-root product c in K with c^p=beta^r, even though its individual roots need not lie in K.
The removed constant-term sign is necessary for this statement and is present.
Primality of p and 1<=r<p permit ar+bp=1, hence gamma=c^a beta^b has gamma^p=beta.
The negative exponents do not impair integrality: the displayed equations for gamma and gamma^(-1), with integral beta and beta^(-1), imply both are algebraic integers by transitivity of integrality.
Their norm is one because its pth power is one and p is odd.
Both embeddings of K are real, so gamma at the designated embedding is the positive unique real pth root of beta, and its other embedding is its inverse.
The trace is an integer strictly between2 and3.
This contradiction proves irreducibility over K, and K subset Q(alpha) then gives the asserted full degree2p over Q.
The two distinct radial groups of p roots yield exactly M(P)=beta, with no omitted multiplicity or unit-circle roots.

For the full powered polynomial, oddness of p makes squaring a permutation on each pth-root-of-unity group.
The two squared radial groups remain distinct.
Thus Q=u^2-7u+1 is the full degree-d squared-root polynomial, and evaluating Q at each root of P gives -4 alpha_i^p.
Monicity, even d and constant coefficient one give product_i alpha_i=1, so the signed product is indeed positive4^d.
This calculation does not replace the full polynomial by an assumed smaller minimal polynomial.
The reviewer expanded identity(2) and checked both inclusions in (P,Q)=(P,4).
Monic division over Z/4 gives the stated free module of rank d, so the constant intersection is exactly4Z, the quotient has4^d elements, and its additive annihilator exponent is exactly4.
These three facts are distinct and correctly used.

The interpolation minimum follows from compatibility in that common quotient: subtracting the two prescribed residues forces D(t^2-t-1)=0.
Since degree2<d, its coefficients vanish modulo4, including the leading coefficient D, so4 divides D.
Formula(5) supplies an integral solution with D=4 by identity(2).
The proof requires no integral comaximal Chinese remainder theorem and asserts no such comaximality.

For the actual adjugate representative, nonzero resultant gives coprimality over Q.
If two degree-less-than-d pairs represent the same constant, their difference satisfies AP=-BQ, whence Q divides A and the degree restriction forces both differences to vanish.
The explicit pair 4^(d-1)(7-u), 4^(d-1)(u-3) has the required degrees and gives R=4^d.
It is therefore precisely the L174 pair after the stated Sylvester sign convention has been fixed, rather than merely an alternative small-denominator construction.
In f, the second term has degree3p+2 with coefficient-1, while the first has degree3p+1; consequently f is primitive regardless of any lower-degree overlaps.
This proves the content c=4^(d-1) of the specific seed f_R and R/c=4.
The coefficient sum estimate116 follows from submultiplicativity, invariance under multiplication by a monomial and the triangle inequality; no disjoint-support assumption is used.
Evaluation modulo P and Q gives all four scalar-4 identities required in L174.

The reviewer separately reread the complete retained L174 construction, cancellation, rational-function nonvanishing proof, formal-reversal argument and primitive-content boundary.
Its use here is valid with the nonzero scalar4: the target is an actual irreducible reciprocal nontorsion unit polynomial, and the reciprocal-root evaluations hold with the actual degree k=3p+2.
Reduction modulo2 makes G_f integral.
Its vanishing at alpha and monic division give P|G_f in Z[t].
If it were the zero polynomial, L174's Laurent-series proof would force -f*/f=t^j; evaluation at alpha would then force a nonzero power of alpha to equal-1, or1=-1.
Thus this is a nonzero auxiliary.
Scaling f by its positive content c scales G_f by exactly c^3.
The formal reversal has length4k; removing the initial monomial yields an actual reciprocal polynomial, and division by the monic reciprocal P, whose constant term is one, leaves an integral nonzero reciprocal C.
None of these steps assumes f or G_f monic or removes a scalar from the cofactor.

Finally, reversal and substitution t -> t^2 preserve the coefficient sum norm, so each cubic summand has norm at most ||f||_1^3 and their half-sum has the same upper bound.
The circle supremum and the logarithmic Mahler integral therefore give m(G_f)<=3 log116, including any circle zeros through the usual integrable logarithm.
Multiplicativity with the complete factorization t^ell P C gives m(C)=m(G_f)-log beta.
The lower bound m(C)>=0 is valid for every nonzero integer polynomial, including a constant cofactor, and includes its leading scalar.
The whole uniform cofactor bound, rather than a bound on a selected noncyclotomic factor, is established.

This proof-only review introduced no computation, external source acquisition or new literature theorem and did not repeat a historical scan.
The substantive general nonvanishing and reversal mechanism is correctly identified as reuse of L174, whose primitive-content warning is confirmed rather than corrected.
The new family supplies an exact obstruction to inferring an exponential primitive interpolation scalar or primitive coefficient floor from resultant size alone, together with an unbounded-degree family of bounded complete auxiliary/cofactor measure.
Its total logarithmic measure remains log beta>0 throughout.
No near-one sequence, near-one-only counterexample, cyclotomic-cofactor assertion, unrestricted Lehmer gap or Task completion follows.
Fixed retention and any later Claim adoption remain separate coordinator actions.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original entire exact-content finding](#exact-resultant-content-independent-review) | unknown |
| [Original listed exact-content author checks](#exact-resultant-content-original-author-check-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original entire exact-content finding](#exact-resultant-content-independent-review) | [Entire original frozen exact-content proof](../../ledger/Yin_L_G0193_v1.md#retained-resultant-content-collapse-proof) | Actual original2026-10-10day-precision whole D61 Sections1--4/equations(1)--(9) with reuse/conclusion boundaries: every odd prime p>=3/full actual degree2p/irreducibility and fixed Mahler measure/no unit-circle roots, full squared-conjugate polynomial and positive signed4^d resultant, exact Bezout identity/common ideal/constant intersection/quotient cardinality versus annihilator exponent, exact least interpolation scalar4 without integral comaximality, actual degree-bounded adjugate pair and unique content4^(d-1)/primitive degree3p+2 seed/leading-1/complete coefficient sum116, all four scalar4 evaluations and complete reused doubling integrality/nonzero/reciprocity/monomial removal/divisibility, entire auxiliary and complementary factor measure with leading scalar included, every fixed-positive-measure/not-near-one/no-cyclotomic-cofactor/no-gap/source/nonexecution limitation. The whole original scope is retained. |
| [Original listed exact-content author checks](#exact-resultant-content-original-author-check-finding) | [Original exact-content proof and author account](../../ledger/Yin_L_G0193_v1.md#retained-resultant-content-collapse-proof) | Actual original2026-10-10day-precision author checks of the complete irreducibility/fixed-measure proof, powered multiplicities/signed resultant, both ideal equalities and interpolation minimum, unique degree-bounded Bezout pair/content/primitive leading coefficient, all coefficient and full-cofactor bounds, with general nonvanishing/reciprocity explicitly reused. No additional historical review event is invented. |

## Exact retained initial-arrangement boundary

All original76lines of the whole written review, its original day-precision date, complete scope, verdict, text-retention assertion and contribution/source/nonexecution boundaries remain fixed.
The reviewer supplied none of the family selection, irreducibility, ideal/interpolation, adjugate or auxiliary/cofactor deductions.
It had shared G0001 context and received the author's proposed result and requested review points.
The actual mathematical contents and complete initial ordering of that shared/proposed context are not retained, so complete initial isolation is unestablished.
Receiving the proof to inspect does not itself establish contribution or a prior shared mathematical derivation.
Neither the independent/noncontributor title nor these generic descriptions supplies the missing initial arrangement.
The entire original whole finding therefore remains UNKNOWN for independent-review purposes.
The coordinating author supplied and checked the entire new mathematics at its actual listed scope; those exact checks are separately SELF below.
A current authored whole SELF does not close the original whole UNKNOWN.
No new source acquisition, fingerprint calculation, numerical scan, program/J, native run or research Task/E is added.

<a id="exact-resultant-content-original-author-check-finding"></a>
## Original listed exact-content author checks

Date: 2026-10-10.
The exact original contribution/check and then-pending account follows.

The coordinator developed and checked the full irreducibility and fixed-measure proof, powered-polynomial multiplicities, signed resultant, both ideal equalities and the exact interpolation minimum, uniqueness of the degree-bounded Bezout pair, exact content and primitive leading coefficient, and all coefficient and full-cofactor bounds.
The general nonvanishing/reciprocity argument is explicitly reused from independently reviewed L174, not newly claimed.
No computation, source acquisition or independent verification has yet occurred for this new combined proof.
