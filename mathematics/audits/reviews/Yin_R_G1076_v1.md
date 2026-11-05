---
author: Yin
---
# Independent review of powered-polynomial precision and Hankel degree costs

Review act: 2026-11-04T17:08 UTC.
The human record author is Yin.
This is a separately organized agent review of the fixed [C0860 statement](../../claims/Yin_C_G0860_v1.md#statement) and [complete argument](../../claims/Yin_C_G0860_v1.md#argument), including all five parts and their direct dependency interfaces.
The reviewer did not participate in substantive development of C0860 and received no proof-development conversation, proposing-agent mathematical summary or earlier C0860 review conclusion.
The actual fixed proof, current rules, original Task contract and necessary fixed mathematical dependencies were read directly.
D15 and the development conversations were not consulted, and no substantive proof repair was supplied.
The fixed artifact's own provenance and author-checking paragraphs were present but were not treated as review evidence.
The reviewer first checked the displayed conclusions and calculations, then consulted the existing C231, C219 and C858 review findings to delimit reused input evidence.
Those earlier findings concern the dependencies; their relationships and source-inspection limits are not expanded by this review.

<a id="precision-budget-whole"></a>
## Complete precision-budget finding

**Finding:** no unresolved mathematical gap was found in the complete stated theorem and argument of C0860 under its exact hypotheses.
The review covers parts A--E, every displayed bound, the full-power degree and original-root conventions, all-place rational descent, the analytic limit order, and the actual relation to the unrestricted Task.
The result supplies the stated conditional inequalities and the logarithmic-depth family gap.
It supplies neither a universal small-measure input-coverage theorem nor completion of [G0001](../../tasks/Yin_T_G0001_v1.md#lehmer-entropy-growth).
This review selects no C assessment or Task decision.

### Coefficient precision, orders and the finite determinant

The polynomial identity in (13) has the correct sign: multiplying A(s) by A(-s) contributes (-1)^d before extracting the polynomial in s squared.
In (14), E(s)R(-s)+R(s)E(-s) is F(s)+F(-s), so every surviving even coefficient is divisible by two, and the odd coefficients vanish.
The other product is integral in s squared, and 2v>=v+1 includes the endpoint v=1.
No division by two or separability premise enters the coefficient extraction.
Consequently the congruence gains at least one digit at each squaring, and telescoping yields the asserted bound L+r-1 for every r<s without assuming that the depth is maximal.

The [C231 order-index interface](../../claims/Yin_C_G0231_v1.md#powered-order-index) applies to all powers used here.
Power stability makes the full original d-root polynomial squarefree and the two monogenic orders have the same rank, so the index is finite and positive and the discriminant is exactly Delta times its square.
This is the index between \(\mathbb Z[\alpha]\) and \(\mathbb Z[\alpha^n]\), not an index in the maximal order.
The [C231 mixed-power interface](../../claims/Yin_C_G0231_v1.md#mixed-power-resultant-identities) excludes common roots at distinct positive exponents.
The finite Galois-iteration argument applies: an equality \(\alpha_i^a=\alpha_j^b\), followed around a finite-order conjugacy automorphism, would force a nonzero root of unity when a differs from b.
Thus every within-level and between-level factor of the determinant is nonzero.

Evaluation of the congruence at all d roots gives the asserted resultant factor \(2^{d(L+r-1)}\); there is no division by a degree-drop multiplicity.
The discriminants and squared cross resultants occur as separate factors of one squared Vandermonde determinant.
Their divisibilities can therefore be multiplied even when prime divisors overlap.
The two weighted sums in (18) are k(k-1)/2 and k(k-1)(k-2)/6.
After taking logarithms and dividing by dk, their contributions are L(k-1) log 2 and (k-1)(k-2) log 2/3.
The remaining order-index contribution is precisely 2/(dk) times the sum of log I_(2^r).

At level 2^r the total logarithmic Mahler measure is 2^r m, counted over the original d roots.
There are kd rows and kd columns, and the row-norm exponent is 2(kd-1).
Since the sum of the levels is 2^(k+1)-2, division by dk gives (4-4/(dk))(2^k-1), with no hidden degree normalization.
Moving log Delta/d to the other side gives log(kD), establishing (2).
Dropping only nonnegative terms and enlarging the positive radial coefficient gives (3); at k=2 the exact coefficient is 12-6/d as in (20).

### Constants, small-measure limits and the discriminant parameter

The nonzero integral polynomial discriminant gives D<=d.
The logarithmic-depth hypothesis therefore yields (21) with coefficient c(k-1)-1 in front of log d.
The defining k_c exists because its linear term eventually dominates log_2 k.
At this k_c, that coefficient is at least 1+log_2 k_c, so d>=2 gives a numerator at least log 2 and exactly the positive constant in (4).
Formula (5) retains the actual numerator and is asserted only when it is positive.
No uniform choice of k depending on a varying c is required.

For bounded m and d tending to infinity, fixing any c>0 and then fixing k with c(k-1)>1 excludes an infinite subsequence with L>=c log_2 d.
This proves L/log d tending to zero, with the harmless conversion between natural and base-two logarithms.
For a vanishing-measure sequence, the [C219 discriminant-escape argument](../../claims/Yin_C_G0219_v1.md#discriminant-escape) applies because all-power stability implies every prime-degree condition used there.
For each fixed bound on D, that argument fixes one sufficiently large prime and obtains a positive measure lower bound.
It follows that D and hence d tend to infinity.
The maximum coefficient depth is finite because equality of Q_2 and Q_4 would contradict mixed-power nonvanishing.
These arguments cover both maximal and smaller valid depths.

For part C, k=floor(log_2(1/m)) is at least two and 2^k m<=1, including m=1/4.
The radial contribution in (2) is at most four, which gives (7) after dropping only the nonnegative index term.
The inequality k-1>=log_2(1/m)-2 gives (8) and retains the full 2L log 2 loss.
No bound on the rate of degree growth is silently inserted, and no fixed-input limit is exchanged with the sequence limit.

### Higher-depth rational approximation and simultaneous valuation levels

The reciprocal, noncyclotomic, irreducible input with constant term one has even degree, its roots are permuted by inversion, and their product is one.
Thus Q_n(x) agrees exactly with the normalized product of (1-alpha_i^n x), so the objects in part D are the same ones used by C858.
Condition (9) implies the depth-three premise of [C858](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) without changing the polynomial, orbit, mask or trace.
The full Galois orbit may have one member, and the full mask is allowed; nonemptiness ensures B>0.

For n>=1 the reduced denominator of binom(1/2,n) is a power of two, as also follows from its signed Catalan-number formula with denominator 2^(2n-1).
Together with the exact valuation (lambda-2)n+s_2(n), this establishes the integrality of each scaled binomial coefficient, including at odd places.
A_J has zero constant coefficient and D_J has constant coefficient one, so coefficientwise expansion uses only finitely many summands.
The rational coefficient valuation is valid simultaneously at every prime above two.
There is no inference from a congruence at only one residue place.

For a=lambda-2>=1, the chosen r_s is zero exactly for s=1,...,a+1.
For every omitted n>=r_s+1, an+1>=s, including all cases with r_s=0.
Each retained numerator has degree at most r_s deg D_J, and the common product denominator has degree at most Br_s and constant term one.
Full-orbit Galois invariance gives numerator and denominator in Z[x], without division by the orbit size.
The global coefficient congruence then descends to 2^s Z[[x]], with no missing ramification or trace factor.
The coefficient recurrence of the proper shifted rational function gives rank at most b_s over Q_2; when b_s=0, that shifted function is zero.

The elementary-divisor implication in C858 applies separately to every s for the same Hankel matrix.
Summing the counts of divisors with valuation at least s is legitimate and includes a zero determinant with valuation infinity.
There are a+1 zero-rank levels, followed by exactly a levels for each positive rank bound rB.
This proves (10), including h<=B and exact multiples of B, with ell=floor((h-1)/B).
For fixed input and mask, the resulting quadratic coefficient is a/(2B).
This is a simultaneous level count, not the maximum of single-level estimates.

### Nonrationality, radius and the actual certificate boundary

The complete C858 argument and its selected [R1074 F2](Yin_R_G1074_v1.md#hankel-all-place-whole) were checked for applicability to this same normalized trace.
Power stability excludes root-of-unity quotients within a powered conjugate set, and mixed-power nonvanishing excludes coincidences between the squared and fourth-powered sets after clearing the rotation roots of unity.
Each rotated basic radicand therefore has private simple zeros.
Their odd valuations give independent square classes, and the multiquadratic character decomposition prevents a sum of distinct nonempty mask terms from becoming rational.
The higher-depth premise changes none of this nonrationality argument.

The accepted leading-Hankel criterion is the BNZ22 arXiv-v3 Section 2.2 Corollary 2.3 interface retained and inspected in C858 and R1074 F2.
Its shifted application to (f-f(0))/x gives infinitely many nonzero determinants with precisely the indexing in C0860.
That source inspection is reused at its actual selected-passage scope; the present reviewer did not perform a new original-PDF or whole-paper proof audit.
The C858 finite recurrence and elementary-divisor reasoning were read directly, rather than replaced by an infinite-operator assertion.

The disk |x|<H^(-4) contains no zero of any numerator or denominator, and each normalized square root is holomorphic on it.
For fixed rho in that disk, the Cauchy coefficient estimate and the displayed row and column factors have total exponent h squared.
The remaining Hadamard term is h log M_rho+(h/2)log h, and M_rho is positive and fixed before h tends to infinity.
Along the unbounded nonzero determinant indices, integrality permits the real lower bound v_2(D_h) log 2.
Dividing by h squared, taking h to infinity first and then rho to H^(-4) gives a log 2/(2B)<=4 log H.
Since total m>=log H, both constants in (11) follow.

For inherited precision, substitution and multiplication establish (9) with lambda=L, while any higher actual mask precision requires separate evidence.
The inequalities B>=d and L/log d tending to zero give exactly the vanishing upper bound on the displayed lower-certificate value in (12).
A positive uniform certificate value eta would require lambda-2>=8 eta B/log 2.
This conclusion bounds that certificate rather than the actual measure, and does not exclude mask-specific cancellation, a smaller approximation rank or a different complex estimate.
The original [G0001 contract](../../tasks/Yin_T_G0001_v1.md#lehmer-entropy-growth) requires an unrestricted uniform total-measure gap or a sequence proving its absence, neither of which is provided here.
The [C231 norm descent](../../claims/Yin_C_G0231_v1.md#all-positive-power-existence-descent) applies only to existence reduction and may change the original input and all its congruence and discriminant data.
Every condition in C0860 must still be verified on the same reduced polynomial.

### Source and reuse limits

The [C219 finite determinant argument](../../claims/Yin_C_G0219_v1.md#finite-prime-discriminant-gap) and [Mat96 inspection](../literature/Mat96/Yin_U001.md#mat96-u001) identify the established determinant mechanism at the explicitly corrected nontorsion and degree-preserving scope.
The finite determinant calculations used in C0860 are complete in its own text and were checked above.
The accepted nonreciprocal threshold used only in the existence reduction retains the statement/applicability boundary recorded in [Smy08 U002](../literature/Smy08/Yin_U002.md#smy08-reciprocal-number); its original proof was not newly audited.
The selected [C231 review](Yin_R_G0515_v1.md#current-arithmetic-norm-finding) and [C219 review](Yin_R_G0509_v1.md#current-finite-prime-finding) remain self-reviews at their recorded scopes.
This independent C0860 finding does not relabel them or assert a recursive review of their unrelated branches.

The C232v2 statement was checked only to confirm the separate floor-only optimization scope; no optimization conclusion is used here.
The C857 statement was checked only to confirm that its arbitrary-precision examples have m>log 2 and supply no near-one input.
Neither comparison is a proof premise for A--E.
No new external theorem, source acquisition, numerical certification, native computation or proof-assistant verification was used in this review.
No unresolved source attribution affecting the displayed proof was found at the stated retained-input scope; no exhaustive novelty search or full literature audit is claimed.
The inspected erratum contained no current objection affecting these selected inputs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete precision-budget finding](#precision-budget-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete precision-budget finding](#precision-budget-whole) | [C0860 statement](../../claims/Yin_C_G0860_v1.md#statement) | Entire parts A--E, every hypothesis, quantifier, constant, sequence conclusion and actual certificate/Task boundary. |
| [Complete precision-budget finding](#precision-budget-whole) | [C0860 complete argument](../../claims/Yin_C_G0860_v1.md#argument) | Entire fixed argument through its limits, including coefficient gain, finite determinant, logarithmic-depth gap, growing-L remainder, all-place rank descent and original disk limit. |
| [Complete precision-budget finding](#precision-budget-whole) | [C231 order index](../../claims/Yin_C_G0231_v1.md#powered-order-index) | Full original-root squarefreeness, same-field order index and exact discriminant identity at the powers used by C0860. |
| [Complete precision-budget finding](#precision-budget-whole) | [C231 mixed powers](../../claims/Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Nonzero distinct-positive-exponent full cross resultants; no use of the separate cyclic surplus or finite controls. |
| [Complete precision-budget finding](#precision-budget-whole) | [C219 finite determinant](../../claims/Yin_C_G0219_v1.md#finite-prime-discriminant-gap) | Fixed-prime discriminant gap and attribution interface needed for the stated escape consequence. |
| [Complete precision-budget finding](#precision-budget-whole) | [C219 discriminant escape](../../claims/Yin_C_G0219_v1.md#discriminant-escape) | D and degree tending to infinity for the same power-stable vanishing-measure sequence. |
| [Complete precision-budget finding](#precision-budget-whole) | [C858 all-place argument](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) | Integral nonrational same trace, finite rank and elementary-divisor implication, and infinitely many nonzero shifted determinants with inherited source limits. |
| [Complete precision-budget finding](#precision-budget-whole) | [C858 disk argument](../../claims/Yin_C_G0858_v1.md#cauchy-radius-cost) | Same original analytic radius and Cauchy/Hadamard cost; no stronger complex estimate is assumed. |
| [Complete precision-budget finding](#precision-budget-whole) | [C231 existence descent](../../claims/Yin_C_G0231_v1.md#all-positive-power-existence-descent) | Existence-only power-stable reciprocal endpoint with no larger positive measure in the accepted small window; no preservation of original residue, input or discriminant data. |
| [Complete precision-budget finding](#precision-budget-whole) | [G0001 contract](../../tasks/Yin_T_G0001_v1.md#lehmer-entropy-growth) | Comparison of C0860's scope with the unrestricted total-Mahler objective only; this is not a completion review. |
