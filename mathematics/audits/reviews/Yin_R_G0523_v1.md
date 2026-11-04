---
author: Yin
---

# Independent review of the excess-two Salem classification and corrected MS26 source application

Date and human record author: 2026-10-21T05:11, Yin.
This is an actual separate agent review of the fixed current WORKTREE inputs, rather than a report of an earlier review.
The reviewer did not contribute to the proof, source corrections, programs or original computations.

## Review arrangement and order

The initial review received the fixed Claim, its necessary mathematical inputs, the exact requested scope and applicable repository instructions.
No proof-development dialogue, author's mathematical summary, exploration notes or prior review conclusions were supplied as additional mathematical context.
The initial scope named the existing finite data set and thirteen groups; these were inspected and reproduced rather than assumed.
The fixed mathematical inputs themselves contain historical labels such as "audited", "independently checked", "L G0033", and references to earlier self-review.
Those embedded labels were visible while reading the necessary inputs and supplied no evidence for the present conclusion or for an earlier agent's isolation.

The reviewer first enumerated the current statement's obligations, read the complete C247 statement and argument, inspected the necessary C234 interfaces, the complete mathematical MS26 unit, both complete native programs and all native output records, and checked the selected original PDF passages.
The mathematical and source-application findings below were formed and reported to the coordinating agent before reading either the old L36 Review section or MS26-U001 Review status.
Only then were those two designated old accounts read for comparison.
No earlier PASS or independence label is used as a premise.

The exact primary target is [C247 v1 Statement](../../claims/Yin_C_G0247_v1.md#statement) and its [Argument](../../claims/Yin_C_G0247_v1.md#argument), including both the classification and every positive primitive realization.
The inspected registration decision is [retained-registration](../../claims/Yin_C_G0247_v1.md#decision-retained-registration), dated 2026-10-21T05:03.
Its open state was treated as awaiting an actual review/adoption decision, not as a mathematical objection or a preset verdict.
This review records current inspection only and makes no retrospective assertion about the 2026-10-07 review arrangements.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Current independent finding](#current-excess-two-salem-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Current independent finding](#current-excess-two-salem-finding) | [C247 exact statement](../../claims/Yin_C_G0247_v1.md#statement) | Every Salem minimal polynomial of degree at least four; repeated cyclotomic factors; exact excess-two equivalence with the thirteen source numbers, all seventeen completions, the Lehmer minimum and primitive binary determinant-one realizations of dimension at most twenty; all stated exclusions. |
| [Current independent finding](#current-excess-two-salem-finding) | [C247 complete argument](../../claims/Yin_C_G0247_v1.md#argument) | Both classification directions, application of corrected MS26, exact terminal evidence, all-positive two-cycle construction, small-cycle cases, return-walk primitivity, maximum dimension and below-Lehmer consequences. |
| [Current independent finding](#current-excess-two-salem-finding) | [C234 argument](../../claims/Yin_C_G0234_v1.md#argument) | Reciprocal coefficient-length lower bound, signed-matching analysis for excess at most two, one/two permutation-cycle determinant formulas, E=2 implies L=5 without a Mahler upper bound, and the complete nonexceptional length-five construction; no new review of the general cycle-count corollary. |
| [Current independent finding](#current-excess-two-salem-finding) | [Completion invariants](../../claims/Yin_C_G0233_v1.md#completion-invariants) | Exact minima over arbitrary integral unimodular presentations and monic cyclotomic products with repetitions, existence of the minima and the companion-matrix comparison; no claimed uniform complexity bound. |
| [Current independent finding](#current-excess-two-salem-finding) | [Signed matching input](../../claims/Yin_C_G0229_v1.md#bounded-excess-gap) | Nonzero determinant matching, entrywise integral excess inequality, zero-excess signed permutations and active signed cycles used in the C234 interface; bounded-support source theorem retained at its existing stated scope. |
| [Current independent finding](#current-excess-two-salem-finding) | [MS26-U001 mathematical unit](../literature/MS26/Yin_U001.md#ms26-u001) | Actual retained arXiv v1 definitions, Theorem 1/Table 1, the needed conclusions and proofs of Lemmas 2.1/2.2, Section 3, all three recorded corrections, trace-pattern completeness and local application limits; historical review claims compared only afterward. |
| [Current independent finding](#current-excess-two-salem-finding) | [J G0001 scope and results](../../computations/programs/Yin_J_G0001/readme.md#results-and-limits) | Complete original finite scope, both native programs, every one of the 57 candidate records, all thirteen exact group intervals and the exact Lehmer minimum; both original programs actually reproduced without extending the range. |
| [Current independent finding](#current-excess-two-salem-finding) | [Primitive and graph definitions](../../ledger/Yin_L_G0034_v1.md#scope-and-accepted-interface) | Definition of primitive nonnegative matrix only; the separate zero-padding existence theorem is comparison context and is not used to prove C247. |
| [Current independent finding](#current-excess-two-salem-finding) | [Edge excess definition](../../ledger/Yin_L_G0034_v1.md#graph-excess-length-bound) | Edge count with multiplicity M=sum A_ij and edge excess e=M-N, including its distinction from Frobenius excess for general nonnegative integer matrices. |

<a id="current-excess-two-salem-finding"></a>
## Current independent finding

No mathematical gap was found in the complete current C247 statement and argument at the scopes bound above.
The fixed source corrections are necessary and sufficient for the adopted length-five proof; the uncorrected printed argument is not being certified.
The finite computation supplies the terminal classification only after the separately checked analytic reduction.

### Excess, coefficient length and the Salem interface

For the monic Salem minimal polynomial p, the same L(p) and E(p) definitions are used in C247, C234 and C233.
The admissible cyclotomic products are monic, include the empty product and allow multiplicities.
The companion matrix supplies a nonempty admissible set; integral nonnegative excess and integer coefficient length give actual minima.

The C234 lower-bound argument was rechecked.
Every such reciprocal completion is reciprocal up to its constant sign.
Leading and constant coefficients use two units of length; the remaining possibilities of length at most four are the stated central quadratic forms or the two binomial-product forms, all cyclotomic.
Thus L(p) is at least five.
For excess at most two, a determinant matching forces all entries to have magnitude at most one, with at most two off-matching arrows.
The component containing p has one permutation cycle or two cycles joined by the two opposite intercycle arrows.
In the one-cycle determinant formula, the second-order numerator is a difference of two signed monomials of degrees at most 2N-2 divisible by t^N-sigma.
Its nonzero quotient is a signed monomial; shared indices, coincident exponents and N=1 do not create an omitted term.
The two-cycle formula likewise has only a single mixed monomial.
These give coefficient length at most five, while excess zero or one cannot contain the noncyclotomic reciprocal factor.
Hence E(p) is at least two and E(p)=2 implies L(p)=5 without an upper bound on the Salem number.

A length-five completion p c is exactly a Salem polynomial under the retained source's definition on printed/PDF page 1.
No square-free convention or prohibition of repeated cyclotomic factors is imported.
The corrected source classification therefore applies to every admissible completion of length five.
Conversely every listed completion is nonexceptional for the C234 explicit construction, which supplies E(p) at most two.
The lower bound gives equality.
Neither direction assumes in advance that the Salem number is below Lehmer or below the exceptional quadratic threshold.

### Actual source edition, original pages and corrections

The selected local [MS26 PDF](../../literature/pdf/MS26.pdf) was opened without network retrieval or replacement.
The inspected artifact identifies the authors and arXiv:2605.19013v1 strip dated 18 May 2026 and has twenty-one pages.
PDF and printed pagination coincide.

PDF pages 1, 2, 3, 4, 8, 9 and 10 were read as text and actually rendered and viewed.
The mathematical source scope is the page-1 definitions, page-2 Theorem 1, page-3 Table 1, the relevant Lemma 2.1 conclusion and its proof, Lemma 2.2, and Section 3 on pages 8-10.
Other statements sharing those physical pages were not thereby audited.
In particular Theorem 2, the length-six proof, later algorithms/tables and the rest of the twenty-one-page paper remain outside this finding.

The adopted definition of cyclotomic polynomial explicitly allows products, repetitions and 1.
Theorem 1 states seventeen length-five Salem polynomials and thirteen Salem numbers, rather than a classification conditional on a lower bound for the Salem number.
All seventeen first-column polynomials in Table 1 were compared with the program's exact pair transcription.
The factorization column was not adopted wholesale; exact irreducible-factor grouping and the Lehmer factor were checked separately through J.

The three source slips recorded by U were independently located in the actual PDF and checked algebraically.
On page 4 both appearances of j'+ra must be j'-ra: only the latter preserves (i'-rb)a-(j'-ra)b=1.
Choosing the odd member as a, taking a signed representative with 0<i<b/2, and setting j=(ia-epsilon)/b gives j>0 and j<(a+1)/2.
Integrality then yields j<a/2; swapping a and b changes the permitted sign only.
Thus the corrected proof establishes the stated Lemma 2.2.

At the top of page 10 the correct inherited bounds are 2 ell<2n-k and 2m<k.
They put both doubled zeros inside (0,2 pi).
Their separation 4 pi/[k(2n-k)] is less than both grid spacings because both odd factors are at least three, so no third grid zero intervenes.
The final finite range on page 10 must start at n=2 rather than n=4, as is also forced by the degree-four and degree-six rows of Table 1.
The original J range contains those cases.

The proof uses only the between-consecutive-distinct-zeros conclusion of Lemma 2.1.
For the sine product, its logarithmic derivative is a sum of cotangents with strictly negative derivative and endpoint limits of opposite infinite signs on each such interval.
There is exactly one interior critical point.
Shared sine zeros can also be derivative zeros, so the broader literal interlacing wording is not relied on.

### Full analytic reduction and multiplicity

Odd length excludes q(1)=0 and q(-1)=0 by reduction modulo two.
The completion is consequently reciprocal of even degree with leading and constant coefficients one.
Its value at 1 is negative: the Salem real reciprocal pair contributes a negative factor and the other conjugate pairs and permitted cyclotomic factors contribute positive factors.
The remaining coefficient mass is therefore entirely negative.
The central shape t^(2n)-3t^n+1 has n expanding roots, and n=1 gives a quadratic Pisot number.
It cannot supply a degree-at-least-four Salem polynomial.
The remaining case is q_(n,k)=t^(2n)-t^(2n-k)-t^n-t^k+1 with 1<=k<n and n>=2.
If gcd(n,k)>1, a positive expanding root of the lower-degree polynomial lifts to more than one expanding root; coprimality is therefore necessary.

For s(theta)=-4 sin((2n-k)theta/2) sin(k theta/2), the required circle roots correspond to s(theta)=1.
When k=2k', n is odd and the consecutive-grid interval has modulus bounded by pi^2/[k'(n-k')].
For n>=11 its denominator is at least n-1>pi^2.
Reflection theta to pi-theta changes the sign, so a small interval of either sign yields a positive interval with maximum below one.
For k=1 the second interval is positive and has modulus at most 8 pi/(2n-1), below one for n>=14.
For odd k>=3, the corrected Bezout interval, doubled if necessary to obtain even index sum, is positive and has modulus at most 4 pi^2/[k(2n-k)].
This is at most 4 pi^2/[3(2n-3)]<1 for n>=9.
The corrected endpoint and adjacency check above justifies the doubled interval.

There are n-1 positive humps over (0,2 pi) in either parity case.
Each can contribute at most two roots counted with multiplicity.
At an interior critical point the logarithmic-derivative calculation gives a nonzero second derivative, so tangency at height one has multiplicity exactly two rather than creating extra roots.
A lost positive hump therefore prevents the required 2n-2 unit-circle roots, even if other humps are tangent.
The three cases imply n<=13, independently of any finite data or floating-point picture.

### Native terminal computation and exact minimum

The complete [main.py](../../computations/programs/Yin_J_G0001/main.py), [verify.py](../../computations/programs/Yin_J_G0001/verify.py), result.json (`mathematics/computations/outputs/Yin_J_G0001/result.json`) and verification.json (`mathematics/computations/outputs/Yin_J_G0001/verification.json`) were read.
Every coefficient list, endpoint value, derivative-gcd degree, multiplicity root count and acceptance flag for all 57 coprime pairs in 2<=n<=13 was inspected, together with all thirteen groups and rational intervals.

The trace identity q=t^n H(t+t^-1), with H=C_n-C_(n-k)-1, is exact.
The Fraction implementation uses square-free Sturm counts and repeated derivative-gcd layers for multiplicity.
The separate SymPy implementation reconstructs the trace polynomial from Chebyshev expressions, factors the actual reciprocal q, and compares all counts, groups and isolating intervals without importing the main program.
The endpoint checks exclude -2, 2 and 3.
All 57 trace polynomials are square-free as a checked result.

The accepted trace pattern consists of n-1 roots in (-2,2), one in (2,3), and no remaining roots.
It gives exactly one expanding positive root and its reciprocal in q.
Every monic irreducible factor is a unit, so the sole expanding root and sole contracting root must belong to the same factor.
The remaining factors are cyclotomic by the retained [Kronecker criterion](../literature/Smy08/Yin_U001.md#smy08-u001).
A quadratic exceptional factor would have integral trace in (2,3), which is impossible; hence the exceptional factor has degree at least four and is Salem.
This proves sufficiency as well as necessity of the tested pattern.
The height-one bound gives root modulus below two and Salem trace below 5/2, so the endpoint three omits no Salem candidate.

Both original reproduction commands were actually run from the repository root:

    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0001/main.py
    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0001/verify.py

Both exited zero under Python 3.12.14; the second used SymPy 1.14.0.
Only the original 57-candidate range and original output homes were used.
The existing native JSON payloads were read before execution and compared as parsed objects with the regenerated files; both were identical.
No native program or input was changed and no search was extended.

The exact accepted set is

    (2,1), (3,1), (3,2), (4,1), (4,3),
    (5,1), (5,2), (5,3), (5,4), (6,1), (6,5),
    (7,1), (7,2), (7,3), (8,1), (9,1), (10,1).

Exact gcd grouping and exact irreducible-factor grouping both give thirteen distinct Salem numbers.
All thirteen rational isolating intervals are disjoint and ordered.
The minimum group is exactly (6,5),(7,3).
Exact multiplication gives q_(6,5)=(t^2-t+1)(t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1), identifying Lehmer's number.
The 45-digit decimal displays decide none of these conclusions.

### Explicit primitive matrices and quantitative scope

Substitute a=n-k into the C234 construction.
The two positive cycles have lengths k and 2n-k.
The added arrows are u_(k-1) to v_0 and v_(n-k-1) to u_0, both with weight one.
Their new mixed cycle has length k+(n-k)=n and positive weight, contributing -t^n in the characteristic polynomial.
The two original disjoint cycles give (t^k-1)(t^(2n-k)-1), so the determinant polynomial is exactly the required q.

The cross arrows occupy different off-matching positions even for k=1 or n-k=1.
A length-one base cycle is simply a loop and contributes one binary matrix entry.
Thus the dimension is 2n, every entry is zero or one, exactly 2n+2 entries are nonzero, and the constant term gives determinant one.
Frobenius and edge excess consequently both equal two, and no zero eigenvalue or zero padding is introduced.

The two intercycle arrows make the graph strongly connected.
The k-cycle and n-cycle both pass through u_0 and gcd(k,n)=1.
Every sufficiently large integer is a nonnegative combination of k and n, including the k=1 case.
Fix paths from every initial vertex to u_0 and from u_0 to every final vertex.
Choose one common length larger than the representation threshold plus the maximum sum of these finitely many path lengths.
The residual return length is then available for every ordered pair, so one common matrix power is strictly positive.
This checks the stated definition of primitivity directly.
The accepted list has maximum n=10, giving dimension at most twenty.

The distinct general primitive-existence theorem in C240/L34 allows zero padding and gives no uniform dimension or edge cost; it is not a premise of this construction.
The below-Lehmer consequences E>=3 and L>=6 follow from the exact classification and the checked reciprocal lower bounds.
The retained [DS17 fixed-support gap](../literature/DS17/Yin_U001.md#ds17-u001), together with the C233/C234 complexity comparisons, supports only the stated escape of L and E along a hypothetical positive-measure sequence tending to one.
Its original proof was not re-audited here.
No multiple-expanding reciprocal classification, length-six completeness, uniform bounded complexity, unrestricted Lehmer gap or Task completion follows.

## Comparison with the designated earlier accounts

After the initial findings had been formed and reported, the reviewer read [the retained original L36 account](Yin_R_G0524_v1.md#original-salem-synthesis-contributor-finding) and [the retained original MS26-U001 account](Yin_R_G0524_v1.md#original-ms26-author-finding).
Their mathematical conclusions agree with the current checks; no new mathematical correction is needed in C247 or the adopted corrected source reasoning.

The old L36 account says that an assigned agent checked the synthesis and also supplied the direct k/n return-walk proof.
That account does not establish isolated independent review of the agent's own contribution to the final proof.
The old U account records substantive checks and two executions but does not specify isolated mathematical input conditions.
The present review neither certifies those earlier arrangements nor rewrites their dates, relationships or findings.
The new independent relationship belongs only to the actual current review described above.
Historical relationship and locator maintenance remain with the coordinating agent.

## Outcome and retained limits

The complete current C247 proof and corrected MS26 application are supported at the exact bound scopes, including the original finite terminal evidence and all small-cycle and multiplicity cases.
There is no remaining mathematical or source-applicability objection within those scopes.
A responsible C decision must separately select and adopt this finding; creating R does not change C247's assessment.

The source artifact is the retained v1 only; no later source version, author response or journal publication was checked.
Kronecker's theorem, the fixed-support gap and the ordinary algebraic setting remain accepted inputs at their recorded scopes, without fresh original-proof audits.
This is mathematical and native-computation review, not a Lean/formal verification, human review, whole-paper audit or research execution.
Ignored J outputs are present locally and were regenerated in their existing home; a fresh clone can lack them.
