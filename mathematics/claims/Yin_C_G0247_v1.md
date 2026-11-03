---
author: Yin
---

# Exact excess-two Salem classification and positive primitive realizations

This owns the full original2026-10-07 restricted classification and construction, keeping the corrected source and exact finite evidence separate.

## Statement

For every Salem minimal polynomial p of degree at least4, let L(p) and E(p) be the cyclotomic coefficient-length and integral unimodular Frobenius-excess minima, allowing repeated cyclotomic factors.
Then E(p)=2 if and only if its Salem number is one of the exact thirteen numbers in the accepted MS26 Table1 unit.
There are exactly seventeen admissible length-five completions, of the form t^(2n)−t^(2n−k)−t^n−t^k+1,1<=k<n,gcd(n,k)=1, with n<=10 as listed by the exact adopted source/evidence.
The minimum is the Lehmer number, identified by the exact Phi6 factorization.
Each completion has an explicit primitive nonnegative binary2n-by-2n realization with determinant1 and2n+2 nonzero entries, so both Frobenius and edge excess are2, without zero padding, and dimension is at most20.
The result gives E>=3 and L>=6 for a Salem counterexample below Lehmer; it classifies no multiple-expanding reciprocal branch or all length-six polynomials and proves no unrestricted gap.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:03 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every Salem minimal polynomial of degree>=4, all cyclotomic completions including repetitions, exact E=2 equivalence with the thirteen accepted source numbers, all seventeen completions and primitive zero-free realizations of dimension<=20; no general reciprocal or length6 classification. |
| argument | [Argument](#argument) | Complete two-direction E=2/L=5/source-classification application, exact Lehmer minimum, all-positive two-cycle construction, k=1/n-k=1 cases, common return-walk primitivity and maximum dimension, preserving source-correction and finite-proof boundaries. |
| dependency | [Excess-two theorem](Yin_C_G0234_v1.md#argument) | Complete reciprocal-unit E=2/L=5 implication and explicit nonexceptional length-five realization with both small cycle cases. |
| dependency | [Exact source unit](../audits/literature/MS26/Yin_U001.md#ms26-u001) | Corrected complete length-five Salem classification, repeated-cyclotomic convention, exact seventeen polynomials/thirteen groups and minimum; length6 is excluded. |
| dependency | [Exact terminal evidence](../computations/programs/Yin_J_G0001/readme.md#results-and-limits) | Retained exact57 candidates/seventeen pair matches/thirteen groups/root intervals and Lehmer factorization; no new execution claimed. |
| support | [General primitive existence](Yin_C_G0240_v1.md#perron-neutral-realization) | Distinct zero-padding and absent-uniform-cost scope only; the present positive unimodular realization is proved explicitly. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:15 |
| status | proved |
| reason | Adopt the actually isolated complete C247/source/native finding. Both exact classification directions, every primitive realization, the original PDF passages and corrected analytic reduction were checked, and both finite native programs reproduced at the original scope. No length6, general reciprocal or unrestricted gap conclusion is adopted and no old relationship/date is certified. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every Salem minimal polynomial of degree>=4, all cyclotomic completions including repetitions, exact E=2 equivalence with the thirteen accepted source numbers, all seventeen completions and primitive zero-free realizations of dimension<=20; no general reciprocal or length6 classification. |
| argument | [Argument](#argument) | Complete two-direction E=2/L=5/source-classification application, exact Lehmer minimum, all-positive two-cycle construction, k=1/n-k=1 cases, common return-walk primitivity and maximum dimension, preserving source-correction and finite-proof boundaries. |
| review | [Fresh independent complete finding](../audits/reviews/Yin_R_G0523_v1.md#current-excess-two-salem-finding) | Complete current statement/argument and exact necessary source/native interfaces, including the real primary-page and finite-reproduction scope; actually isolated independent review. |
| dependency | [Excess-two theorem](Yin_C_G0234_v1.md#argument) | Complete reciprocal-unit E=2/L=5 implication and explicit nonexceptional length-five realization with both small cycle cases. |
| dependency | [Exact source unit](../audits/literature/MS26/Yin_U001.md#ms26-u001) | Corrected complete length-five Salem classification, repeated-cyclotomic convention, exact seventeen polynomials/thirteen groups and minimum; length6 is excluded. |
| dependency | [Exact terminal evidence](../computations/programs/Yin_J_G0001/readme.md#results-and-limits) | Retained exact57 candidates/seventeen pair matches/thirteen groups/root intervals and Lehmer factorization; no new execution claimed. |
| support | [General primitive existence](Yin_C_G0240_v1.md#perron-neutral-realization) | Distinct zero-padding and absent-uniform-cost scope only; the present positive unimodular realization is proved explicitly. |

## Argument

<a id="excess-two-salem-classification"></a>
### Exact branch and its minimum

Let p be the monic minimal polynomial of a Salem number lambda>1 (degree at least four).
Let L(p) be the least coefficient length of p times a cyclotomic product, and E(p) the least Frobenius excess among integral unimodular matrices with such characteristic polynomial, as in L G0027.
Repeated cyclotomic factors are allowed.

Then E(p)=2 if and only if lambda is one of the 13 Salem numbers in MS26 Table 1.
In particular,

    E(p)=2  =>  M(p)=lambda >= lambda_Lehmer.

There are exactly 17 coefficient-length-five completions across this entire Salem class, as listed in the [exact computation](../computations/programs/Yin_J_G0001/readme.md).
Different completions can give the same minimal polynomial; the 13 groups were identified both by exact trace-polynomial gcds and independently by factorization of the actual reciprocal polynomials.
The minimum is identified by the exact identity

    (t^2-t+1)p_Lehmer=t^12-t^7-t^6-t^5+1.

Proof: L G0033 gives E=2 => L=5 for every positive reciprocal irreducible unit, without an upper Mahler bound.
A minimal length-five completion of a Salem polynomial is a Salem polynomial in the source's definition, including its cyclotomic multiplicities.
The audited classification applies and gives one of the 17 polynomials and 13 numbers.
Conversely each listed completion has the nonexceptional shape used in the explicit length-five realization of L G0033, so E<=2; its reciprocal noncyclotomic lower bound gives E>=2.
This converse does not need an assumed bound on lambda.
All source-local corrections and the analytic reduction beyond the finite range belong to MS26-U001.

<a id="positive-primitive-two-cycle-realization"></a>
### Every member has a positive primitive realization

Every listed completion is

    q=t^(2n)-t^(2n-k)-t^n-t^k+1,
    1<=k<n, gcd(n,k)=1.

The explicit construction in L G0033 uses cycles of lengths k and 2n-k and two cross arrows creating the additional cycle of length n.
Both cycle signs and both cross-arrow weights are positive in this case.
Hence the resulting matrix A has entries in {0,1}, dimension 2n, determinant 1, and exactly 2n+2 nonzero entries.
In particular its Frobenius excess and its nonnegative edge excess both equal 2.

The graph is strongly connected because the two cross arrows join the two cycles in opposite directions.
Its directed cycles include lengths k, 2n-k and n; their greatest common divisor is gcd(n,k)=1.
More directly, the cycles of lengths k and n both pass through u_0, and every sufficiently large integer is a nonnegative combination of k and n.
Thus all sufficiently large return lengths are available at u_0.
Fixed paths from each initial vertex to u_0 and from u_0 to each final vertex give a common length at which every ordered pair is connected.
Consequently a common power of the adjacency matrix is strictly positive: A is primitive.

Thus every classified Salem number has a primitive nonnegative unimodular realization with exactly the same Mahler measure and edge excess two, with no zero padding.
The largest n among the 17 accepted pairs is 10, so these explicit realizations have dimension at most 20.
This property is established for the finite classified branch, not for all Perron or Salem units.
The general existence theorem in [L G0034](Yin_C_G0240_v1.md#perron-neutral-realization) permits zero padding and supplies no dimension or edge bound; it does not subsume this quantitative claim.

### Changed search boundary

Below the Lehmer number, any Salem counterexample would have E>=3 and L>=6.
The existing bounded-support gap already implies that any hypothetical sequence of positive measures tending to one must have E and L unbounded; the new source does not improve that general implication.
It instead closes the excess-two Salem branch with its exact optimal minimum and an explicit finite list.

The whole excess-two class is not classified here: a reciprocal unit can have several expanding conjugates, and its length-five completion need not be a Salem polynomial.
Nor is an unconditional finite list for length six adopted: the new source separates infinite families, a finite search above 1.01 and a conjectural completeness boundary below that cutoff.
A next useful arithmetic step must cover the multiple-expanding core or control unbounded completion complexity; another equivalent definition or a fixed-degree search alone does neither.
