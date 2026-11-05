---
author: Yin
---
# Independent review of exact all-place mask depths and uniform certificate loss

Review act: 2026-11-04T19:47 UTC.
The human record author is Yin.
This is a separately organized whole-proof agent review of the frozen [C0860v2 statement](../../claims/Yin_C_G0860_v2.md#statement) and [complete argument](../../claims/Yin_C_G0860_v2.md#argument), including all new parts A--C and their exact fixed dependency interfaces.
The reviewer did not participate in substantive proof development and received no proof-generation discussion, author explanation, proposing-agent mathematical summary or earlier conclusion about the v2 proof.
The fixed v2 text was read first; the necessary fixed C0860v1, C0858, C0219 and Bel17 inputs were then read directly.
Initial checks of the new depth, denominator and limiting arguments preceded consultation of R1076v1 and R1074 F2 to delimit reused evidence.
The candidate's own provenance and contributor-check paragraphs were visible but were not used as review evidence.
No rolling Draft or development conversation was consulted, and no substantive proof repair was supplied.
The candidate had no selected mathematical assessment during this review.

## Earlier finding and exact reuse

The [earlier complete precision-budget finding](Yin_R_G1076_v1.md#precision-budget-whole) remains at its original fixed R1076v1 locator and covers C0860v1 A--E only.
That earlier review and its historical adoption are preserved unchanged, rather than relabelled as a review of the new mask formulas or v2 conclusion.
This same-topic physical revision retains the new independent inspection below; it does not replace the earlier finding's input, time or scope.
The new review uses the accepted v1 theorem at its exact hypothesis and source boundaries, rechecking its changed invocations in v2.
The unchanged original multilevel theorem is not represented as newly re-audited in all of its unrelated consequences.

<a id="mask-depth-whole"></a>
## Complete all-place mask-depth finding

**Finding:** no unresolved mathematical gap was found in the complete new statement and argument of C0860v2 under its stated hypotheses and retained accepted-input limits.
The finding covers M1--M9, the whole v2 argument, its direct interfaces, and the distinction between a vanishing displayed lower certificate and the unrestricted total-Mahler objective.
It does not select a Claim assessment or Task decision.

### Input, exact coefficient depth and formal logarithms

The irreducible reciprocal noncyclotomic polynomial with constant term one has even degree, and its conjugates are permuted by inversion.
Consequently the normalized products P_n(x) equal the monic powered polynomials Q_n(x) of v1, with the same original d roots and total logarithmic measure.
Power stability excludes a root-of-unity quotient between distinct conjugates: a common positive power would collapse the degree below d.
Positive absolute height, invariant under conjugacy and multiplication by roots of unity, excludes a rotated squared conjugate from coinciding with a rotated fourth-powered conjugate.
The resulting private simple zeros show that U differs from V and that every nonempty mask has N_I/D_I different from one.
Thus every maximal coefficient depth used in the theorem is finite.

The actual retained [Dimitrov v1 PDF](../../literature/pdf/Dim19.pdf) identifies arXiv:1912.12545v1, 28 December 2019.
Lemma 2.1 and its finite argument on printed pages 3--4 were read from that PDF in this review.
Its assumption is a monic integer polynomial, and its conclusion is Q_4 congruent to Q_2 modulo four.
The displayed Newton identities give the power-sum congruence, and applying it to the integral polynomial of products over each k-element subset gives every coefficient congruence.
The input here meets those assumptions, so L is at least two.
This is selected-passage source and applicability checking, not a whole-paper review or a review of Dimitrov's house theorem.

The [Bel17 accepted input](../literature/Bel17/Yin_U001.md#bel17-u001) supplies the full integer ring Z[zeta] and the degree q-1, hence its stated integral power basis.
Its integer-ring assertion is accepted at the existing statement/applicability scope; the underlying Neukirch proof was not newly inspected.
In particular A is free over Z_2 on that basis, so O_K intersected with 2^a A is exactly 2^a O_K.
The coefficientwise global depth is therefore measured by this common Z_2-module divisibility.
It is not the valuation at an arbitrarily selected single place above two.

For z in 2^a xA[[x]] with a at least two, the r-th logarithm term has depth at least ar-v_2(r).
For r at least two this is at least a+1, while the r=1 term is z itself.
At a coefficient of exact depth a the higher terms cannot cancel its residue modulo 2^(a+1), proving the claimed depth isometry.
Every coefficient uses finitely many summands because z has zero constant coefficient.
The coefficients belong to A, where odd denominators are units; no algebraic-integrality assertion for the individual logarithm coefficients is needed.
The nonzero integral series has a finite minimum coefficient valuation, so applying the isometry at its exact depth is legitimate.
Multiplication by U or D_I, each with constant coefficient one and integral formal inverse, preserves divisibility in both directions.
This identifies the polynomial depths with the depths of R-1 and N_I/D_I-1 exactly.

### Proper and full masks

The formal derivative and zero-constant-term argument proves additivity of logarithms, yielding the displayed coefficient ell_n c_I(n) without an analytic convergence premise.
For q not dividing n, multiplication by n permutes Z/qZ and maps a nonempty proper binary mask to another such mask.
In F_2[z]/(Phi_q), the only multiples of Phi_q of degree at most q-1 are zero and Phi_q itself.
The two excluded masks are exactly those two cases, so c_I(n) does not belong to 2A.
This does not assert that c_I(n) is a unit in A or in each of its local factors.
It only asserts that at least one coordinate in the integral basis is odd, which is exactly what the common depth requires.
Since ell_n is a scalar in Q_2, its valuation adds to this common coefficient depth even if c_I(n) is not a unit at some places.

For q dividing n the multiplier is the integer k=|I|, adding v_2(k) to the depth.
Taking the two minima therefore gives M1, and the logarithm isometry for the original R gives min(a_q,b_q)=L.
The infinity convention for a zero coefficient group is compatible with these minima; both groups cannot have infinite depth because R is not one.
For a full mask the nonmultiple coefficients vanish and the remaining multiplier is the odd unit q, proving M2.
The already established finite full-mask depth also ensures b_q is finite for the actual inputs.
For a proper mask, if a_q=L then M1 is at most L, and if b_q=L then it is at most L+v_2(k); these cases establish M3.
For odd k its extra valuation is zero, so the depth is exactly L.
All proper masks of a fixed size have the same common depth.
No irreducibility of Phi_q modulo two, chosen residue factor, or restriction on ord_q(2) is inserted.
The empty mask and the even prime q=2 are outside the theorem's domain.

### The union denominator and integral rational approximants

The orbit O is the complete orbit under the original Galois group, acting by multiplication on positions.
Its union S is invariant and nonempty; its three possible forms for prime q are exactly the sets listed in the proof.
Each factor U(zeta^j x) has degree d and nonzero leading coefficient, so Q has degree b=d|S|, not merely a formal degree bound, and Q(0)=1.
Invariance and algebraic integrality give Q in Z[x].
Galois automorphisms preserve the ideals 2^lambda O_K, so all orbit masks have the same maximal actual depth.

For lambda at least three, a=lambda-2 is a positive integer and A_J=(N_J-D_J)/2^lambda is integral with zero constant coefficient.
For r at least one, the coefficient 2^(lambda r) binom(1/2,r) is an integer: the binomial denominator has only powers of two, and its exact two-adic valuation is ar+s_2(r).
This is the same scalar calculation as in v1; the valuation is common to all places above two, and integrality also holds at the odd places.
For every r at most t, Q^t/D_J^r is an integral polynomial because J is a subset of S.
The displayed degree calculation gives at most tb for each numerator term, including the r=0 term.
Repeated rotations shared by several masks require no repeated denominator factor at the same truncation level.
The common truncation rule and full orbit make the numerator over Q^t Galois invariant, hence rational integral, with no averaging or division by |O|.

For each s at least one, t=max(0,floor((s-2)/a)) has the stated remainder property: every omitted r at least t+1 satisfies ar+1 at least s.
The cases t=0, including s=1, are covered by the same inequality.
Thus f minus the rational approximant belongs to 2^s Z[[x]], and both polynomial degrees are at most b_s=bt.
The unit constant denominator makes the approximant's coefficients integral.
After subtracting its constant term and dividing by x, its numerator degree is strictly below b_s; when b_s=0 the shifted series is zero.
The finite coefficient recurrence gives shifted Hankel rank at most b_s over Q_2.
This is an upper rank bound for these particular approximants, with no claim of exact or minimal rank.

### Nonrationality, valuation counting and complex cost

The [C0858 private-zero argument](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) applies to the identical normalized orbit sum.
Private odd zero valuations make the basic rotated square classes independent, and the multiquadratic character basis separates every distinct nonempty mask product over K(x).
Multiplication of individual terms by nonzero rational factors does not destroy that independence, so the sum is nonrational, including a one-member orbit or the full mask.
The integral binomial expansions and full-orbit invariance give f in Z[[x]].
The exact shifted leading-Hankel criterion retained in [R1074 F2](Yin_R_G1074_v1.md#hankel-all-place-whole), from BNZ22 arXiv v3 Section 2.2 Corollary 2.3, therefore supplies infinitely many nonzero determinants.
The application is to (f-f(0))/x with the source index shifted by one, exactly as in C0858 and v1.
That selected-source inspection is reused at its true scope; no new BNZ22 whole-paper or original-PDF inspection is claimed here.

The finite elementary-divisor comparison in C0858 was read directly and applies to each s for the same integral Hankel matrix.
The congruent matrix of rank at most b_s forces at least h-b_s elementary-divisor valuations to be at least s whenever that number is positive.
Summing these counts is valid also for a zero determinant, assigned infinite valuation.
There are exactly a+1 initial values of s with b_s=0, and exactly a subsequent values for each positive bound rb.
This gives M7a, including small h and h divisible by b, with quadratic coefficient a/(2b) as h grows for the fixed input.

The original radius H^(-4) contains no zero of any numerator or denominator, so every normalized square root and their sum are holomorphic there.
For fixed rho below this radius, the Cauchy bound and row/column factors contribute exactly -h^2 log rho.
The remaining Hadamard terms are h log M_rho+(h/2)log h.
Along the unbounded nonzero integer determinants, division by h^2 and the h limit give a log 2/(2b) at most -log rho.
Only then does rho increase to H^(-4), yielding log H at least a log 2/(8b).
Total m is at least log H, proving M7b with the unchanged normalization.
There is no uniform-in-q assertion about M_rho or interchange of the fixed-input Hankel limit with a varying-input limit.

### Uniformity and the scope of the obstruction

For a proper mask of size k, |S| at least k and v_2(k)/k at most 1/2 give M8a exactly as a valid, deliberately weaker upper bound on the displayed certificate.
The [C0219 escape interface](../../claims/Yin_C_G0219_v1.md#discriminant-escape) applies to the same power-stable positive-measure vanishing sequence, and its nonzero integral discriminant gives D at most d.
Hence d tends to infinity.
The [v1 B conclusion](../../claims/Yin_C_G0860_v1.md#statement) applies to the maximal finite original depth L and gives L=o(log d).
These facts make the proper-mask bound tend to zero independently of q and k.

For a full mask, the product identity over all q rotations gives exactly D_I(x)=P_(2q)(x^q) and N_I(x)=P_(4q)(x^q).
Substitution of x^q preserves coefficient depth, and the union has size q, so b=dq.
The polynomial P_q is the minimal polynomial of alpha^q: power stability retains degree d, and its coefficients are integral and its roots reciprocal.
It is noncyclotomic and power-stable at every further positive power, with total measure qm.
Thus the [v1 k=2 budget](../../claims/Yin_C_G0860_v1.md#multilevel-precision-budget) applies to its original depth lambda.
Dropping nonnegative index terms and using its integral discriminant D_q at most d gives lambda log 2 at most log(2d)+12qm.
Dividing by the actual full-mask cost 8dq gives M9a, with the term 3m/(2d).
Only q at least three is used to replace the first term by log(2d)/(24d).
No bound or smallness assumption on qm is needed, so arbitrarily growing primes remain covered.

The supremum over proper and full masks is bounded by the maximum of these two input-only bounds, both of which tend to zero.
The convention for an empty depth-at-least-three indexing set is consistent with this argument.
Replacing the maximal actual depth by any smaller supplied integer depth at least three decreases the certificate, and replacing b by the earlier B also decreases it because |S| is at most |I||O|.
Depths equal to two remain within the logarithm identities but outside the positive-a truncation certificate; no division by a=0 is made.

The conclusion concerns the specified scalar product depth, binomial approximants and elementary disk comparison.
It does not control extra cancellation only after summing differently weighted trace terms, different weights at separate finite places, or the true smallest approximation rank.
It also does not exclude a different complex quadratic estimate.
In particular it is not an upper bound on actual Mahler measure and does not assert a near-one input family or solve the [unrestricted G0001 contract](../../tasks/Yin_T_G0001_v1.md#lehmer-entropy-growth).
No computation, numerical estimate, native output or proof-assistant certificate is a premise of this finding.
The source and dependency checks above resolve the interfaces used by v2 without converting accepted textbook statements or earlier scoped reviews into newly performed source-wide or recursive proof audits.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole mask-depth finding](#mask-depth-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole mask-depth finding](#mask-depth-whole) | [C0860v2 exact statement](../../claims/Yin_C_G0860_v2.md#statement) | Entire new A--C, all M1--M9 formulas, hypotheses, finite and infinite coefficient-minimum conventions, lambda domain, uniform quantifiers and certificate exclusions. |
| [Whole mask-depth finding](#mask-depth-whole) | [C0860v2 complete argument](../../claims/Yin_C_G0860_v2.md#argument) | Whole new proof, its original-input and dependency interfaces, and all source, normalization and Task limits. |
| [Whole mask-depth finding](#mask-depth-whole) | [Exact proper/full depths](../../claims/Yin_C_G0860_v2.md#proper-mask-depth) | Formal logarithm isometry in O_K tensor Z_2, integral power basis, global coefficient depth, M1--M3, no single-place or residue-irreducibility substitution. |
| [Whole mask-depth finding](#mask-depth-whole) | [Union denominator](../../claims/Yin_C_G0860_v2.md#overlap-denominator) | Q and degree b, integral rational approximants, finite ranks, all valuation levels, nonrational same trace and exact Cauchy cost. |
| [Whole mask-depth finding](#mask-depth-whole) | [Uniform certificate loss](../../claims/Yin_C_G0860_v2.md#uniform-mask-certificate-vanishing) | Proper and full masks, arbitrarily growing q without qm tending to zero, supremum, lower supplied depths and earlier B cost. |
| [Whole mask-depth finding](#mask-depth-whole) | [C0860v1 statement](../../claims/Yin_C_G0860_v1.md#statement) | Accepted original A--E retained at v1; precise use of B for maximal L, A at k=2 on P_q, and D's truncation/disk interfaces, without transferring old review coverage to v2 additions. |
| [Whole mask-depth finding](#mask-depth-whole) | [C0860v1 multilevel budget](../../claims/Yin_C_G0860_v1.md#multilevel-precision-budget) | k=2 invocation on the same-degree power-stable reciprocal P_q, its total measure qm, D_q at most d, and lambda log 2 at most log(2d)+12qm. |
| [Whole mask-depth finding](#mask-depth-whole) | [C0860v1 higher-depth approximants](../../claims/Yin_C_G0860_v1.md#higher-depth-hankel-comparison) | Exact scaled-binomial valuation, integral coefficients, truncation levels and elementary-divisor assembly with the newly proved b bound. |
| [Whole mask-depth finding](#mask-depth-whole) | [C0860v1 disk comparison](../../claims/Yin_C_G0860_v1.md#higher-depth-disk-cost) | Same original radius, h-squared exponent, nonzero-index comparison and fixed-input order of limits. |
| [Whole mask-depth finding](#mask-depth-whole) | [C0858 all-place construction](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) | Original noncollision/private-zero and nonrationality argument, integrality of identical orbit sum, finite rank-to-elementary-divisor implication and shifted leading-Hankel criterion at retained BNZ22 source scope. |
| [Whole mask-depth finding](#mask-depth-whole) | [C0858 disk radius](../../claims/Yin_C_G0858_v1.md#cauchy-radius-cost) | Original holomorphy radius and Cauchy/Hadamard calculation; no stronger complex estimate assumed. |
| [Whole mask-depth finding](#mask-depth-whole) | [C0219 discriminant escape](../../claims/Yin_C_G0219_v1.md#discriminant-escape) | D and hence d tending to infinity on the stated power-stable vanishing-positive-measure sequence. |
| [Whole mask-depth finding](#mask-depth-whole) | [Bel17 integral power basis](../literature/Bel17/Yin_U001.md#bel17-u001) | Exact accepted integer-ring and degree statements for prime q and their reduction in A; inherited original-proof limits preserved. |
| [Whole mask-depth finding](#mask-depth-whole) | [C0860v2 exact source interface](../../claims/Yin_C_G0860_v2.md#exact-dependencies-and-source-scope) | In particular Dimitrov arXiv:1912.12545v1 Lemma 2.1, printed pages 3--4: exact monic-integer hypothesis, modulo-four statement and finite symmetric-product argument read in the retained v1 PDF; no whole-paper review. |
| [Whole mask-depth finding](#mask-depth-whole) | [G0001 contract](../../tasks/Yin_T_G0001_v1.md#lehmer-entropy-growth) | Comparison with unrestricted total-Mahler gap or counterexample objective only; not a completion review. |
