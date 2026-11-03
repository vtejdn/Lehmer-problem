---
author: Yin
---

# Original coefficient scale and the true positive-log tail: whole independent review

Date: 2026-10-11T15:16.
Human record author: Yin.
This is a separately organized AI noncontributor review, not a claim of personal human inspection.

The exact target is the complete [D30 author account](../../ledger/Yin_L_G0382_v1.md), dated 2026-10-11, Sections 1--4 and equations (1)--(7), including the Section 4 author freeze supplied for this review.
The input contains no minute-specific freeze timestamp; none is inferred here.
The author is stopped for the assigned inspection.
No native computation, new finite test or modification of D30 is part of this review.

## Arrangement, input disclosure and source depth

Root authored the new tail argument and supplied only the whole-review assignment, its exact scope and the requirement to distinguish accuracy from positivity after a large-tail cancellation.
This reviewer contributed no proof or candidate to D30.
The complete D30 body and its author self-check were read, after identifying obligations for the geometric-mean comparison, all inequality directions, precise quantifiers, exceptional branches and the original padding family.
No proof-generation dialogue, separate author explanation or previous D30 review conclusion was consulted.
General repository and G0001 context was available.

The reviewer read the relevant exact positive-moment identity in L378, the retained L379 recurrence/cost interface, the complete canonical DS17 bounded-support source account and L19's actual application.
The reviewer previously independently reviewed L379's precursor; that is prior supporting-interface inspection, not authorship of D30 or a substitute for the new scalar argument.
DS17 is an already accepted external statement with recorded proof dependencies.
The original PDF and the external proofs cited by DS17 were not freshly reaudited here.
No new source acceptance, proof-depth upgrade or whole-paper review is claimed.

All new D30 mathematics is checked directly below.
In particular the convex comparison is obtained from its actual derivatives and a supporting-line inequality, rather than an uninspected general theorem.
No numerical execution is needed to verify any displayed identity or example.

Current arrangement clarification (2026-10-21T20:28): the explicitly supplied complete initial body included the author mathematical self-check.
This known exposure makes the actual original whole relationship SELF under the current isolation requirement, preserving all direct reconstructions, eight original bindings,23:16 date and source/no-native limits.
The earlier supporting-interface role is not the basis for target-contribution or isolation inference.
The author freeze has day precision only;23:19 ledger retention does not supply a missing minute.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#coefficient-scale-tail-whole-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#coefficient-scale-tail-whole-finding) | [D30 whole account](../../ledger/Yin_L_G0382_v1.md) | Entire 2026-10-11 author-frozen body, Sections 1--4/equations (1)--(7), exact original normalization, all claims and limitations. |
| [Whole finding](#coefficient-scale-tail-whole-finding) | [Geometric-mean lower bound](../../ledger/Yin_L_G0382_v1.md#geometric-mean-positive-tail-lower-bound) | Original X and integrable log X, derivative identities, supporting-line comparison, nonnegative termwise integration and monomial/nonmonomial branches. |
| [Whole finding](#coefficient-scale-tail-whole-finding) | [Necessary accuracy window](../../ledger/Yin_L_G0382_v1.md#necessary-quadratic-coefficient-scale) | Block bound, all negative-log inequality directions, delta/M/H/N/d/k quantifiers, harmonic-tail comparison and exact sparse-support consequence. |
| [Whole finding](#coefficient-scale-tail-whole-finding) | [Squarefree padding example](../../ledger/Yin_L_G0382_v1.md#squarefree-integer-padding-control) | Complete coefficients, degree, coefficient sum, roots/squarefreeness, full Mahler measure, true linear-window divergence and arbitrary valid scalar-normalization variant. |
| [Whole finding](#coefficient-scale-tail-whole-finding) | [Positive-log identity](../../ledger/Yin_L_G0378_v1.md#positive-log-moment-identity) | The exact positive series and actual omitted tail for the original polynomial, including all finite root multiplicities; no re-review of the separate simple-zero upper-tail estimates. |
| [Whole finding](#coefficient-scale-tail-whole-finding) | [Fast recurrence cost](../../ledger/Yin_L_G0379_v1.md#fast-positive-moment-arithmetic-cost) | The retained O(Nd^2) arithmetic count and its bit/output qualifications; no fresh program run or broad re-review of J86. |
| [Whole finding](#coefficient-scale-tail-whole-finding) | [DS17 bounded-support statement](../literature/DS17/readme.md#bounded-support-gap) | Already accepted fixed-support positive gap for nonzero integer polynomials, including the separately handled monomial case; original external proof-depth limits retained. |
| [Whole finding](#coefficient-scale-tail-whole-finding) | [L19 support consequence](../../ledger/Yin_L_G0019_v1.md#cyclotomic-support-escape) | Actual fixed-K quantifiers and support escape under hypothetical positive-measure sequences tending to zero; no claimed new sparse-gap theorem. |

<a id="coefficient-scale-tail-whole-finding"></a>

## Whole finding

All D30 claims are valid at their stated scope.
No mathematical correction is required.
The inequalities are lower bounds on the TRUE omitted positive tail, and the resulting coefficient-scale window is necessary for fixed absolute accuracy of the uncorrected truncation.
They do not imply failure of every smaller-window positive lower certificate after a separately controlled tail subtraction, nor an obstruction for every estimator or irreducible near-one input.

### Original random variable and exact convex comparison

For nonzero integer P, its circle modulus is bounded by the original H.
Its circle zeros are finite, and the logarithmic singularity of each finite-multiplicity zero is integrable.
Thus X=|P|^2/H^2 is positive almost everywhere, takes values in [0,1], and Y=log X is integrable after any harmless definition on its zero-measure zero set.
Its exact mean is 2m(P)-2log H=log(M^2/H^2).
In particular 0<M^2/H^2<=1; the leading coefficient, every factor and all multiplicities are present in M.

For fixed 0<x<1, the derivative of the nonnegative remainder series is justified on any compact subinterval away from x=0.
It gives r_N'(x)=-(1-x)^N/(2x).
Under x=exp(y), direct differentiation yields

    g_N'(y)=-(1-exp(y))^N/2,
    g_N''(y)=N exp(y)(1-exp(y))^(N-1)/2>=0,

for finite y<0, N>=1.
The endpoint value g_N(0)=0 and derivative bound -1/2<=g_N'<=0 imply 0<=g_N(y)<=-y/2 for y<=0.
This proves g_N(Y) integrable without assuming the circle modulus is bounded below away from zero.

At the finite mean a=integral Y, the derivative monotonicity implies g_N(y)>=g_N(a)+g_N'(a)(y-a) whenever a<0.
Integration gives integral g_N(Y)>=g_N(a).
Nonnegative termwise integration identifies the left side with the original T_N-m(P), so D30 (3) follows.
If a=0, then Y<=0 and mean zero imply X=1 almost everywhere, and both sides vanish.
The proof uses one actual circle law, with no independent-phase replacement or substitution of an energy mean for the geometric mean.

For a monomial P=a z^j, M=H=|a| and every positive moment vanishes.
For a nonmonomial, choose its actual smallest/largest nonzero coefficient exponents.
Their product is a nonzero extreme autocorrelation, so the modulus cannot be constant on the whole circle.
Continuity and X<=1 then force integral log X<0, giving x_P<1.
The strictness assertion is correct, although the later inequalities only require the displayed nonmonomial range.

### Explicit bounds and correct directions

For n=N+1,...,2N, one has 1/n>=1/(2N) and (1-x)^n>=(1-x)^(2N).
There are N terms, and the leading factor 1/2 therefore gives r_N(x)>=(1/4)(1-x)^(2N).
This also holds at x=1 with both sides zero.

For nonmonomial P and 0<delta<1/4, the accuracy assumption and this bound imply (1-x_P)^(2N)<=4delta.
Since log(1-x_P)<0, division reverses the inequality and gives exactly

    N>=log(1/(4delta))/[-2log(1-x_P)].

The elementary integral estimate -log(1-x)=integral_0^x du/(1-u)<=x/(1-x) gives the second lower bound in D30 (6).
All denominators are positive after the minus sign is included.
The bound is necessary only; it does not control the actual tail from above.

If M<=B and delta is fixed, the lower estimate is a fixed positive multiple of H^2/B^2 minus a constant.
If additionally N<=C d, rearranging gives H^2<=M^2[1+2Cd/log(1/(4delta))].
Integer nonzero coefficients each have absolute value at least one, so H>=k.
Consequently fixed B,C,delta imply k=O(sqrt(d)).
The draft correctly notes that this does not exclude support tending to infinity below that rate, or establish existence of such a near-one family.

Separately, T_N-m(P)=log(H/M)-(1/2)sum_{n=1}^N nu_n/n and 0<=nu_n<=1 give the harmonic lower bound.
The elementary H_N<=1+log N, valid also at N=1, gives D30 (7) with the factor e exactly as displayed.
Its right side can be negative; the actual tail is still nonnegative.
For bounded M and H^2/N tending to infinity, the right side tends to infinity, proving a true remainder effect rather than a poor choice of an upper bound.

The accepted DS17 theorem states a positive gap for each fixed bound K on the number of nonzero coefficients of a nonzero integer polynomial, without irreducibility or degree restrictions.
If a positive-measure sequence tending to zero had infinitely many members with k<=K, that gap would be contradicted.
Thus k tends to infinity, hence H does too.
This invocation has exactly the source's accepted scope.
The new estimator window does not itself improve that external Mahler-gap statement or show that H^2/d must diverge along every hypothetical near-one sequence.

### Complete padding example and normalization variant

For every prime p>=3, write Q=t^2-3t+1 and S_p=sum_{j=0}^{p-1}t^j.
The quadratic has distinct positive reciprocal roots, both off the circle.
S_p has the nontrivial p-th roots of unity, all simple, as its roots.
Therefore the factors have no common root and their product is squarefree.
Its degree is p+1 and its full Mahler measure is (3+sqrt(5))/2: the leading coefficient is one, the larger quadratic root supplies that value, and all cyclotomic roots contribute one.

Coefficient multiplication gives 1 at exponents 0,p+1, -2 at exponents 1,p, and -1 at every exponent 2 through p-1.
There are exactly p-2 entries in the latter range, including the smallest case p=3.
Hence the displayed entire coefficient list and H=p+4 are correct; no cyclotomic factor or coefficient has been discarded.

For 1<=N<=C(p+1), the lower bound (7) is at least

    (1/2)log[(p+4)^2/(e M^2 C(p+1))]
      =(1/2)log p-O_C(1).

Thus the true remainder diverges on this actual squarefree family at every such linear window.
The example is reducible and has fixed positive measure, so it establishes neither an irreducible hard-core barrier nor a near-one sequence.
Both limitations are correctly explicit.

For any scalar normalization L>=max_circle |P_p|, the same probability/convexity argument works with |P_p|^2/L^2 and mean M^2/L^2.
Since P_p(1)=-p, L>=p.
Therefore L^2/[C(p+1)] still grows at least linearly in p, and the harmonic lower bound has the same divergence.
This verifies the stronger normalization claim on this particular family.
It does not assert optimality of H or universality over unrelated estimator constructions.

### Accuracy, subtraction and scope of the conclusion

The proved object is the error T_N-m(P).
A certified lower estimator normally has the form T_N-U_N, with U_N an independently verified upper bound for that tail.
Even if both T_N and the true tail are large, U_N may in principle approximate the tail closely enough that T_N-U_N>0.
The displayed lower bounds alone do not prohibit that cancellation.
D30 states this distinction explicitly and does not claim otherwise.

The unchanged fixed-input positive-moment asymptotics in L378 and the exact recurrence in L379 are compatible with all these bounds.
Faster finite evaluation still pays the necessary N for uncorrected accuracy.
This does not exclude an algebraic treatment of the full tail, other rational/oscillatory approximations, root methods or another estimator.
No claim about the success or failure of the separate H=9 finite Lehmer computation is inferred, and this review performs no computation on that input.

## Verification facts and limits

The reviewer independently reconstructed all derivatives, endpoint/integrability conditions, supporting-line and harmonic estimates, negative-log directions, parameter rearrangements and complete family coefficients/roots/measure.
No mathematical native run, numerical quadrature, parameter scan, new source theorem or formal verification was performed or required for these exact arguments.
The scoped material check is a separate repository-format check, not proof evidence.

The canonical DS17 source account was read with its already recorded inspection depth, including its original unreviewed proof dependencies and one-term boundary correction.
No missing source hypothesis is imported into the new elementary tail proof.
This whole finding covers the exact dated D30 body, not a later substantive revision or the full chain needed for G0001 completion.

This R changes no Task lifecycle, Claim assessment, author artifact or native output.
