---
author: Yin
---

# Retained project review: Cyclotomic stabilization costs and compressed upper-unitriangular realizations

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0190_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="cyclotomic-stabilization-independent-review"></a>

### Complete separate noncontributor review

On 2026-10-10 the separately assigned resultant_research AI for Yin read and independently checked all of the frozen D57, Sections1--5 and equations(1)--(11).
Its pre-review inspection fingerprint was directly matched before this append.
No mathematical defect or required correction was found.
The coordinator proposed the realization question and the Pfaffian/odd-rank endpoint test, and the author developed the assembled arguments and constructions.
This reviewer contributed none of them.
It had the shared G0001 context and assignment summary, so the review is separately organized and noncontributing, not blind, personal human inspection or formal verification.
All frozen author bytes remain unchanged as the file prefix.

The reviewer directly checked D9's original monic reciprocal determinant convention, its signed-cover factorization and its recorded classical endpoint attribution.
The fixed L184/L185 cycle and positive-cover scopes were inspected as the disclosed comparison boundary; no unrestricted realization or simple-graph theorem was imported from them.
The reviewer had previously reviewed components of those retained results, which does not substitute for checking the new stabilization proof.
The present argument needs no new source theorem, classification or computational program, and does not enlarge D9's external source-inspection depth.

At t=-1 the matrix is exactly V^T-V.
Its even-rank determinant is the square of the integral Pfaffian, including the zero possibility, and its odd-rank determinant vanishes.
Monicity, degree, constant coefficient one and reciprocity follow respectively from det V=1, det V^T=1 and transposition after t inversion.
For any proposed identity p_V=P C, the normalization P(0)=1 therefore forces C(0)=1.
With nonzero C(-1), Phi2 is absent and the only negative-constant cyclotomic factor Phi1 has even multiplicity.
All remaining factors have even degree.
This ensures both even matrix rank and strictly positive C(-1), so a negative P(-1) cannot be repaired within that class.

The evaluation table(2) is complete.
Dividing t^N-1 by t-1 and evaluating at one yields the positive integer divisor product N.
Induction gives the prime-power values p and the other values one.
For odd n>1, negation takes primitive nth roots to primitive2nth roots; for n=2m with odd m the reverse substitution applies; when4 divides n, negation preserves primitive nth roots.
These facts give exactly the stated values at minus one, with Phi1 and Phi2 handled separately.
In particular no factor in the nonzero-endpoint class contributes two different odd primes.
Each odd prime in the squarefree part delta therefore forces an odd number of its own Phi_(2p^k) factors, with degree at least p-1.
A prime2 parity defect cannot be fixed by the even Phi1 multiplicity and forces a factor Phi_(2^k), k>=2, of degree at least two.
Summing these disjoint costs proves the lower bound D(delta); the explicit product C_delta attains it at the endpoint, has constant coefficient one and zero measure, and gives a C_delta(-1)=(s delta)^2.
The empty product and a=0 cases are correctly separated.
No matrix existence is inferred from this parity repair.

For the weighted-arm construction, the central-to-arm row is(-t b_j,0) and the reverse column is(-b_j,0)^T with the stated vertex order.
The inverse of the arm block has its first diagonal entry s/F, so its exact Schur contribution is t b_j^2 s/F.
Multiplying by all r arm determinants gives s F^(r-1)(F-A t), proving(5) in the rational function field and hence as an entire polynomial.
Clearing this algebraic identity preserves all multiplicities at F=0.
It includes r=1, arbitrary signs of the nonzero integer weights, and the positive weights used in the cost statement.

The base-four construction has exactly r=sum d_j arms and squared central-edge sum A.
Its largest weight is2^k because the top digit is nonzero, and2^k<=sqrt A.
Thus dimension2r+1<=6 floor(log_4 A)+7 and strict-upper squared-entry sum A+r are correct, including A=1.
The full extra factor is exactly Phi2 Phi3^(r-1), with degree2r-1; it has no omitted scalar or monomial factor.
For A>=4 the remaining monic unit quadratic has trace A-1>2, so its single expanding root gives m=arcosh((A-1)/2).
When the chosen entries are all negative, V equals its own absolute presentation; D9's cover identity consequently gives p_W=p_V^2 and total measure2m, with added cost m.
This is an attained example, without a minimality inference or transfer of weighted entries to a canonical simple-graph representation.

For the prime targets P_p, p(p-4) has p-adic valuation one for every prime p>=5 and is not a square, proving irreducibility.
Trace p-2>2 gives a positive expanding root and nontorsion unit scope; direct evaluation gives P_p(-1)=p.
The exact endpoint minimum therefore yields deg C>=p-1 and total rank at least p+1 whenever C(-1) is nonzero.
Setting A=p-1 in the weighted construction matches the target coefficient exactly and gives every bound in(9).
The p=17 instance has r=1, b_1=4 and determinant(t+1)(t^2-15t+1), while the nonvanishing-endpoint rank bound is18.
Infinitely many primes provide the claimed unbounded separation between a necessary linear scale in one allowed class and an achieved logarithmic scale in the other.
The former need not be attainable for this comparison.
The measure arcosh((p-2)/2) grows, and the text correctly supplies no near-one family or general realization criterion.

The reviewer independently expanded the arbitrary rank-three determinant as

    (t+1)^3-t(t+1)(a^2+b^2+c^2)+t(t+1)abc,

which gives(10) and derivative(11) with the correct signs.
Modulo four, all-even entries give0 and exactly one odd entry gives1; two odd entries give2 minus0 or2, and three odd entries give3 minus1 or3.
Thus the value is never3.
The quadratic t^2+3t+1 is irreducible with discriminant5 and is a nontorsion reciprocal unit polynomial; its endpoint is-1.
No nonzero-endpoint cyclotomic stabilization can realize it.
Multiplication by just t+1 would force the rank-three derivative to remain-1, contradicting the proved congruence.
More generally q congruent to3 modulo4 gives endpoint2-q congruent to3 and the same exclusion.
This is a rank-three derivative constraint only, with no unproved all-rank congruence or classification of the cubic expression.

This full proof-only review supports the exact nonzero-endpoint minimum, the all-parameter weighted-arm and base-four realization, the prime-family dimension separation, and the residual minimal-rank obstruction with their stated hypotheses and costs.
No proof correction, program rerun, J, source acquisition or new external theorem was needed.
Arbitrary cyclotomic-stabilized realization, optimized cover cost in a small-measure class, and unrestricted G0001 remain unresolved.
Later substantive changes require a corresponding scoped review.

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete stabilization finding](#cyclotomic-stabilization-independent-review) | [Entire retained stabilization argument](../../ledger/Yin_L_G0190_v1.md#retained-cyclotomic-stabilization-proof) | Entire D57 Sections1--5 and equations(1)--(11): normalization and endpoint parity, complete cyclotomic evaluations and exact degree minimum, weighted-arm determinant with all factors, base-four dimension/height/energy costs, prime-target irreducibility and separation, rank-three derivative congruence, and every realization/measure/stabilization boundary. No new external theorem or program is needed; no general sufficiency, minimal realized dimension, near-one family or all-rank derivative constraint is asserted. |
| [Original listed stabilization author checks](#stabilization-original-author-check-finding) | [Original complete stabilization proof](../../ledger/Yin_L_G0190_v1.md#retained-cyclotomic-stabilization-proof) | Actual original2026-10-10day-precision listed author checks: complete cyclotomic endpoint evaluation/parity, disjoint prime-valuation degree costs, weighted Schur-complement denominator clearing, every base-four dimension/height/energy cost, prime-target irreducibility/measure and all rank-three derivative congruence cases. No extra original whole author-review event is invented. |

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete stabilization finding](#cyclotomic-stabilization-independent-review) | unknown |
| [Original listed stabilization author checks](#stabilization-original-author-check-finding) | self-reviewed |

## Exact retained initial-arrangement boundary

The complete original whole account, every mathematical check/verdict, day precision, pre-append fingerprint-match assertion and original whole binding remain fixed.
The coordinator proposed the realization question and the specific Pfaffian/odd-rank endpoint test; the structural author developed the arguments and constructions.
That actual supplied mathematical test remains disclosed and is not rewritten as a purely administrative contribution.
The separately assigned whole reviewer contributed none of those target deductions.
It had shared G0001 context and an assignment summary, but the actual mathematical contents of that summary and the complete initial target-proof arrangement are not retained.
These descriptions establish neither initial isolation nor known substantive prior target mathematics.
Its earlier review of fixed comparison interfaces is ordinary upstream activity, not new-target participation.
The entire original D57 Sections1--5/equations(1)--(11) whole finding therefore has relationship unknown for independent-review purposes.
The original precise listed author checks are SELF below, without inventing another original whole author-review event.
A current authored whole check cannot close that original whole UNKNOWN obligation.
The classical endpoint source attribution stays at its original reading depth, and no hash/finer historical time/source-proof inspection/native evidence is generated.

<a id="stabilization-original-author-check-finding"></a>
## Original listed stabilization author checks

Date: 2026-10-10.
The exact original author-check and then-pending account follows.

The author checked the cyclotomic endpoint classification and its parity guard, disjoint prime-valuation lower bounds, denominator clearing in the weighted Schur complement, every base-four cost, irreducibility and measure of (7), and all rank-three congruence cases.
These are self-checks; a complete separate review remains required before fixed adoption.
No universal coverage or unrestricted G0001 conclusion is claimed.
