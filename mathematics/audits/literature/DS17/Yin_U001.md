---
author: Yin
---

<a id="ds17-u001"></a>
# DS17-U001: accepted fixed-support Mahler gap

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Edward Dobrowolski and Chris Smyth, *Mahler measures of polynomials that are sums of a bounded number of monomials*, [existing retained DS17.pdf](../../../literature/pdf/DS17.pdf), arXiv:1606.04376v2,23January2017,7PDF pages. The title-page body says17August2016; that is not the version-strip date. No new acquisition or PDF write.

Passages: Printed/PDF p.2: equation(3), definition of H_k and Theorem2, with adjacent Corollary2. Printed/PDF p.5: Section4 proof of Theorem2. Reference[13] bibliographic identity on printed/PDF p.7. Title/normalization context p.1.

Inspection: 2026-10-11T20:17. The current G0001 author separately verified the existing artifact's hash/page count/title/ordered authors/version, text-read the COMPLETE selected pp.2,5 plus reference[13], and visually inspected rendered pp.2,5. The earlier2026-10-06 coordinator inspection remains separately recorded in readme.md. Coverage is Read with selected source-proof mechanism inspection; the foundational external proofs identified below were NOT inspected. This is an accepted external statement/applicability input, not a whole-source or independent full-proof audit.


## Exact source statement and used consequence

For a fixed positive integer K, the selected text considers NONZERO integer Laurent polynomials in any finite number of variables having at most K nonzero monomials.
The number of variables, exponent sizes, total degree, coefficient height and irreducibility are not bounded.
It denotes this class H_K and defines logarithmic Mahler measure by the normalized torus integral in equation(3), with multiplicative M=exp(m).
Theorem2 says that m(H_K) is closed in R_nonnegative and0 is isolated in that set.

The sole accepted mathematical input for the [G0001 Task](../../../tasks/Yin_T_G0001_v1.md#contract) denominator coupling is the direct UNIVARIATE consequence:

    For each fixed integer K>=1 there exists eta_K>0
    such that every NONZERO integer polynomial f
    with at most K nonzero coefficients satisfies
    m(f)=0 or m(f)>=eta_K.

This is logarithmic TOTAL m(f), with no division by degree.
An isolated neighborhood of0 supplies such a positive eta_K.
The theorem applies to the actual original minimal polynomial itself; no cyclotomic completion, specialization to a foreign polynomial or extra factor is required.
No explicit numerical eta_K, effective growth law, monotonicity in K or new sparse-gap theorem is adopted.

## Proof inspection, accepted foundations and monomial boundary

The current inspection read Section4's finite-coefficient-tuple mechanism: for fixed K>=2 and a bounded measure range, Corollary2 bounds height, leaving finitely many integer coefficient tuples.
Each tuple's associated measure set is closed by source reference[13], Theorem1, and its zero, when present, is isolated by reference[13], Theorem2.
A finite union then gives the stated closure/isolation conclusion.
For tuple sets not containing0, closedness supplies a neighborhood of0 disjoint from the set; this is the explicit ordinary finite-union detail already noted in the earlier audit.

Reference[13] is C.J.Smyth, *Closed sets of Mahler measures*, arXiv:1606.04338.
Its ORIGINAL closedness/isolation proofs were not acquired or re-audited in this inspection.
DS17's theorem is accepted as the established external input after exact statement/hypothesis/applicability checks, retaining those foundational proof-inspection limits.
Acceptance resolves the stated external premise; it does not certify those original proofs or upgrade coverage to a full proof audit.
The earlier derivative/height proof scope and its Mahler derivative input remain separate in readme.md and are not newly audited here.

The printed Corollary2 height formula h/2^(K-2) must not be applied to an ACTUAL single monomial using K1: it would incorrectly give2h.
For f=a t^r with a a nonzero integer, M(f)=|a| and m(f)=log|a| directly, so its positive measures are at least log2.
This supplies the K1 gap branch without that formula.
When a fixed class has K>=2 but a particular member has only one term, M=h still gives the needed weaker height bound because2^(K-2)>=1.
The zero polynomial is excluded throughout the accepted consequence.
For the current actual monic integer-unit minimal-polynomial consumer, both endpoints are nonzero and its support has at least two terms, so the monomial branch cannot be used as an actual counterexample input.

## Local applicability and limits

[L_G19](../../../ledger/Yin_L_G0019_v1.md#cyclotomic-support-escape) already proves support escape, even after cyclotomic completion, along any hypothetical sequence of positive measures tending to0.
Taking the completion1 gives original support escape immediately.
That old deduction is credited and is not reproved as a new source result here.
[C_G25](../../../claims/Yin_C_G0025_v1.md#statement) separately supplies the new first-window actual coefficient-denominator obstruction for flat original polynomials.
Their coupling belongs to the responsible project argument; this source theorem supplies neither a packet, lag cancellation, a denominator lower bound, a norm inventory nor a Lehmer gap over unbounded support.

The retained2017preprint is the inspected artifact.
Its original2026-10-06 acquisition remain unchanged; no journal/preprint equivalence audit, source-version revision, original[13]proof review, explicit earlier sparse-bound audit, Lean check or native mathematical program was performed.
PDF text extraction/rendering were operational inspection only.
No unresolved applicability objection remains for the bounded univariate external input at the stated acceptance depth.

Current exact consumer: [C_G27 fixed-denominator and hypothetical-sequence coupling](../../../claims/Yin_C_G0027_v1.md#statement), with its complete retained local proof.
This adds consumer navigation only and does not expand the inspected source theorem, foundational proof coverage or numerical gap information.
