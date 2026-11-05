---
author: Yin
---
# Independent review of all-place binary masks and coherent centers

Review act: 2026-11-04T20:29 UTC.
The human record author is Yin.
This is a separately organized whole-proof agent review of the fixed [C857 v2 statement](../../claims/Yin_C_G0857_v2.md#statement) and [complete argument](../../claims/Yin_C_G0857_v2.md#argument), including A1--A15 and the exact dependency and source interfaces below.
The reviewer did not develop this proof and received no substantive development conversation, proposing-agent mathematical summary or earlier conclusion about this candidate.
The fixed proof, current rules and necessary fixed mathematical inputs were read directly.
No Draft, temporary mathematical account, contributor chat or proof-generation note was used as a substitute input.
The mathematical obligations and initial findings were formed from those inputs before the earlier R1074 findings were read for their retained scope.
No substantive proof repair was supplied by this reviewer.

The earlier [binary-mask and high-precision finding](Yin_R_G1074_v1.md#binary-masks-whole) and [all-place Hankel and disk-cost finding](Yin_R_G1074_v1.md#hankel-all-place-whole) remain separate at R1074 v1 and their actual C857 v1 and C858 v1 targets.
Their bodies, relationships and earlier review time are not changed or extended to this new proof.
The present finding concerns the new C857 v2 mathematics and its stated interfaces; it does not repeat or retrospectively enlarge those older whole-proof reviews.

<a id="all-place-mask-whole"></a>
## Complete all-place mask and coherent-center finding

**Finding:** no unresolved mathematical gap was found in the entire C857 v2 statement and complete argument A1--A15 under their exact original-input hypotheses.
The finite-field reduction, every all-place mask case, symmetry integer, coherent centers, integral approximation precision and shifted-rank bound are supported at the stated scope.
The exact source and dependency corrections identified during inspection were checked in the final fixed text before this conclusion.
This finding supplies review evidence only; it selects no Claim assessment and does not complete the unrestricted Lehmer Task.

### Original inputs and accepted interfaces

All powered polynomials use the original d conjugates of the same reciprocal, irreducible, noncyclotomic, power-stable integer unit polynomial.
No powered field of smaller degree, modified original polynomial, squarefree reduction assumption or degree-normalized Mahler measure enters the proof.
The equal constant and leading coefficients of U and V give W(0)=0 and deg W<d once divisibility by four is supplied, while bar U retains degree d and constant coefficient one.
Thus r is proper, regular at zero, zero there and has reduced denominator degree at most d, even with repeated reduction factors.

The unconditional divisibility V-U in 4 Z[x] is available in the exact [C860 v2 statement](../../claims/Yin_C_G0860_v2.md#statement) at its [selected assessment](../../claims/Yin_C_G0860_v2.md#decision-whole-independent-review-2026-11-04).
That input explicitly identifies Dimitrov, arXiv:1912.12545v1, Lemma 2.1, printed pages 3--4, as the source of L>=2.
The earlier candidate dependency row had assigned this unconditional fact to C860 v1, whose stated precision result is conditional; the final row now identifies C860 v2 separately and correctly.
This is a correction of the exact dependency interface, not a new proof of the source congruence.
The already accepted source statement and its retained inspection limits are reused; this review does not claim another inspection of Dimitrov's original proof.

Only the scaled-binomial valuation from [C860 v1's higher-depth argument](../../claims/Yin_C_G0860_v1.md#higher-depth-hankel-comparison) is used for A13.
Its exact expression, (lambda-2)v+s_2(v), applies to every integer lambda>=3 independently of the original uncentered mask depth.
Only the finite rational-series recurrence in [C858](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) is needed for A15.
The current proof does not import C858's uncentered depth-three premise, nonrationality theorem, determinant lower bound or disk comparison for the new centers.

The [Bel17 U001 integer-ring statement](../literature/Bel17/Yin_U001.md#bel17-u001) supplies O_K=Z[zeta_q] and the minimal-polynomial degree q-1.
Its stated scope and explicit absence of a fresh original integer-ring proof audit were checked and retained.
For odd q, z^q-1 has derivative z^(q-1) in characteristic two and is squarefree, so Phi_q is squarefree as well.
The resulting quotient O_K/2O_K=F_2[z]/(Phi_q) is the product of its distinct residue fields; no irreducibility of Phi_q modulo two is required.

### A1, A5 and A6: reduced representative and normalized solution

The partial fractions are finite because r is rational and proper, and none of their poles is zero.
For an exponent 2^s u with u odd, squaring the l-th summand in A6 cancels the preceding summand, leaving exactly the original term and its odd-order reduction.
The characteristic-two sign convention is correct.
Inverse Frobenius powers are unique in the algebraic closure and commute with coefficient Frobenius, including its permutation of geometric poles.
Consequently both the reduced sum c and the explicit proper solution h_0 descend to F_2(x).
This is an actual finite-field descent argument, not an assumed algebraically closed source conclusion over F_2.

At zero, h_0(0) is in F_2, so wp(h_0(0))=0 and c(0)=r(0)=0.
Adding h_0(0) to h_0 preserves its Artin--Schreier image, gives h(0)=0, and keeps it regular at infinity.
The constant addition explains why the numerator degree of h may equal its denominator degree.
At a geometric pole of order m_beta in r, every term of h_0 has order at most floor(m_beta/2), and every surviving odd term of c has order at most m_beta.
Summing pole orders gives e<=sum_beta floor(m_beta/2)<=floor(d/2), with geometric multiplicities counted correctly.
Cancellation can only improve these upper bounds.

A nonzero reduced proper rational function has a pole of odd order, whereas a rational Artin--Schreier image with a pole has even highest pole order.
A pole at infinity in a prospective preimage would likewise force a pole at infinity in its image, which is excluded by properness.
If there are no poles, the image is constant and properness forces zero.
This proves uniqueness of c by applying the same reasoning to the difference of two reduced representatives.
Two rational solutions then differ by zero or one, and their values at zero distinguish them.
The cases r=0, c=0 and h=0 are included; e=0 gives the allowed trivial center.

### A2, A7 and A8: local solvability and all residue factors

Scaling x by xi^j preserves properness and odd partial-fraction orders.
A sum of these reduced functions again has only odd negative exponents, including after cancellations.
Hence a mask sum can be an Artin--Schreier image only if its reduced sum vanishes; conversely the corresponding sum of h(xi^j x) is an explicit solution in the actual residue field.
It is normalized to vanish at zero, so no omitted finite-field constant class obstructs the reverse implication.
This verifies both directions of A7 rather than only a test after extending constants.

Each prime above two corresponds to an irreducible factor of Phi_q modulo two, and the embeddings of these residue fields list all primitive q-th roots xi^a for a nonzero modulo q.
Since r, c and h have F_2 coefficients, solvability is preserved by each Frobenius embedding.
Thus simultaneous solvability at the actual primes is exactly A8, with the same binary mask and chosen cyclotomic root throughout.
Multipliers permute these equations, and translation of the mask follows by scaling x within each equation.
The proof therefore imposes the all-place intersection rather than silently replacing it by one chosen residue-place kernel.

### A3, A4 and A9: all four spaces and finite symmetry

Taylor expansion at zero is valid for c and for every scaled copy, so A8 is equivalent to the coefficient conditions A9.
For c=0 no condition remains.
For nonzero c whose supported exponents are all divisible by q, A9 is exactly even weight, and the odd prime's full mask is excluded from that space.
If some supported exponent is not divisible by q, its multiples by all nonzero a run through every nonzero residue class, forcing A_epsilon to vanish at every primitive root.
Divisibility by the full degree-(q-1) polynomial Phi_q then leaves only zero and Phi_q, whether or not Phi_q is irreducible over F_2.
The latter satisfies A9 precisely when there is no supported exponent divisible by q, because Phi_q(1)=1 in F_2.
Mixed support leaves only zero.
These cases are mutually exclusive and exhaustive.

The gcd of the nonempty positive Taylor support is well defined.
A nonzero c has an odd-order pole, so its derivative has a nonzero leading pole term; therefore at least one supported exponent is odd and g is odd.
A primitive g-th root exists in the algebraic closure.
Support divisibility gives c(eta x)=c(x), and uniqueness of coprime numerator and denominator with denominator constant one forces each of these polynomials separately to be invariant.
Their positive exponents are consequently multiples of g, proving c=s(x^g) over F_2.
Conversely a common divisor of those polynomial exponents divides the Taylor support, so the displayed finite polynomial gcd really computes the same g.

Multiplication by eta acts freely on the nonzero finite poles and preserves their orders.
Every pole orbit has length g, so g divides both the number of distinct poles and the sum of their orders.
The poles are among the roots of bar U, giving g<=d and the sharper squarefree-part bound for each prime divisor q.
For distinct such primes their product divides g and both counts.
For q>=3 the even-weight space contains nonempty proper masks, while the zero and full-mask-line spaces do not; this verifies the asserted existence equivalence, including q=3.
The normalized solution also verifies that r becomes an Artin--Schreier image over a finite constant extension if and only if it already is one over F_2.
At zero a solution has value zero or one, and the uniquely normalized solution is fixed by every constant-field Frobenius.

### A10 and A11: one coherent center and simultaneous precision

Writing h=a/b with b(0)=1 gives integer lifts A and B and C=B+2A, all with the required constant terms.
The exact identity V B^2-U C^2=4[W B^2-U(AB+A^2)] verifies integrality, zero constant term and the mod-two formula A10.
Reduction of B/C is legitimate as a formal series because both denominators have constant coefficient one.
The resulting reduced function is c, using the same h as in A1.

Each rotated centered ratio is 1+4 times an integral formal series.
In a product, terms involving at least two such increments vanish after division by four and reduction modulo two.
The remaining sum is precisely the reduced mask sum of c.
Multiplication or division by D_I C_I^2 preserves coefficient divisibility because its constant coefficient is one and its formal inverse is integral.
The squarefree cyclotomic residue decomposition makes simultaneous vanishing equivalent to divisibility by two in O_K, so the original integral polynomial difference is divisible by eight exactly for the masks in K_q^all(r).
This establishes both directions of A11 at the global coefficient level.

Every factor in C_I/B_I uses the same rational function at a mask position.
A mask stabilizer merely permutes those factors, giving the asserted coherence without a division by the stabilizer order.
All masks in a full Galois orbit inherit any common global valid depth.
No equality between that centered depth and a maximal uncentered depth in C860 v2 is assumed.

### A12--A15: integral approximants, remainder and paid rank

For each orbit mask J, Z_J has zero constant term and belongs to 2^lambda O_K[[x]] at every common valid integer depth lambda>=3.
The normalized identity G_J=(C_J/B_J)(1+Z_J)^(1/2) has constant coefficient one and squares to the original N_J/D_J, so it is the required original radical.
For every omitted binomial index v>=t+1, C860 v1's exact valuation is at least (lambda-2)(t+1)+1.
The prefactor C_J/B_J has integral Taylor coefficients and preserves that divisibility.
Every coefficient of the formal binomial series uses finitely many indices because Z_J(0)=0.
There is no analytic convergence or interchange of infinite limits in A13.

The binomial coefficients have no odd prime in their reduced denominators, and the stated valuation supplies their powers of two after multiplication by Z_J^v.
Thus each truncation and each full radical has algebraic-integral Taylor coefficients.
Their remainder has the indicated coefficient divisibility.
The full orbit sum is Galois invariant; hence F_t and f have integer coefficients and the divided remainder is rational integral coefficientwise.
This proves the congruence in Z[[x]], not merely in one two-adic completion, with no orbit-size or trace-division loss.

The union S is Galois invariant, so each Q_X has integer coefficients and constant coefficient one.
For a single J, putting every term through index t over B_J D_J^t C_J^(2t-1) gives numerator and denominator degree at most t|J|(d+2e).
The v=0 term contributes numerator D_J^t C_J^(2t), obeying the same bound; t=1 has no negative exponent in the chosen denominator.
The factors missing from J but present in S add at most t(|S|-|J|)(d+2e), since deg B and deg C are at most e and deg U=d.
This verifies the numerator bound as well as the common denominator A14, including possible degree cancellations in C.
Multiplying the integral series F_t by that integer common denominator shows that its polynomial numerator is integral.

For b=t|S|(d+2e), subtracting F_t(0) and dividing by x gives a rational series with numerator degree less than b and denominator degree at most b, with constant coefficient one.
The directly checked finite recurrence from C858 therefore bounds every shifted Hankel matrix by rank b over Q or Q_2.
The inequality e<=floor(d/2) then gives b<=2td|S| exactly as stated.
This is an upper rank bound and supplies neither a matching lower bound nor a claim of optimal approximation.

### Source attribution, preserved v1 scope and limits

The actual retained [Dang v3 PDF](../../literature/pdf/Dan20--arxiv-v3.pdf#page=4) was read at its first page and at printed/PDF page 4, with a rendered-page check of Example 2.1 and Remark 2.2.
The title, author and arXiv:2002.03719v3 date 3 January 2021 match the cited edition.
Remark 2.2 states the prime-to-characteristic reduced partial-fraction form over an algebraically closed field, matching the standard attribution used here.
Example 2.1 contains a sign slip in characteristic five: adding wp(-1/x) to 1/x^5 gives +1/x, while equation (3) prints -1/x.
The final [Dan20 source notes](../literature/Dan20/readme.md) retain this limitation, and the final C857 v2 attribution explicitly distinguishes the source reading from the directly proved binary identities A5--A6.
The slip supplies no premise to those characteristic-two calculations and creates no unresolved mathematical dependency in this claim.
No whole-paper inspection, deformation-theorem input or novelty determination is asserted.

The actual [C857 v1 statement](../../claims/Yin_C_G0857_v1.md#statement) and its fixed argument were compared with the v2 scope.
The arbitrary finite-field, one-place cyclic-ideal classification remains at v1, including its ord_q(2) dependence and its simple-pole specialization.
The four-space conclusion for every odd q in v2 applies to the original F_2 rational function and the simultaneous residue-place condition, so it does not replace that more general one-place theorem.
The [large-period controls](../../claims/Yin_C_G0857_v1.md#large-period-full-mask) retain their original m(P)>log 2 hypothesis and arbitrary prescribed finite precision.
When their r is zero, the new c is zero as well, but this observation does not change their large-measure domain or provide near-one input supply.

No implication from positive total m(P) tending to zero to c=0, g>1 or a favorable precision-to-actual-rank ratio was proved or used.
The automatic center supplies depth three and a cost of order d|S|, exactly as the final limitations state.
No unrestricted Mahler gap, near-one counterexample family, Task completion, numerical certification or proof-assistant verification follows from this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole all-place finding](#all-place-mask-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole all-place finding](#all-place-mask-whole) | [C857 v2 statement](../../claims/Yin_C_G0857_v2.md#statement) | Entire exact statement A1--A15, all original-input hypotheses, all odd primes, degenerate cases, symmetry counts, center precision and shifted-rank conclusions. |
| [Whole all-place finding](#all-place-mask-whole) | [C857 v2 complete argument](../../claims/Yin_C_G0857_v2.md#argument) | Complete reduction, all-place classification, symmetry, center and approximation proof, exact dependency interfaces, source attribution and limitations. |
| [Whole all-place finding](#all-place-mask-whole) | [C857 v2 reduction and attribution](../../claims/Yin_C_G0857_v2.md#reduced-representative) | A5--A6 checked directly; Dang v3 page 4 attribution checked in the original, with the Example 2.1 sign slip retained and no whole-source proof claim. |
| [Whole all-place finding](#all-place-mask-whole) | [C860 v2 original input](../../claims/Yin_C_G0860_v2.md#statement) | Only the accepted unconditional V-U in 4 Z[x] for the identical original polynomials and its retained Dimitrov v1 Lemma 2.1 source interface; no fresh audit of that original proof. |
| [Whole all-place finding](#all-place-mask-whole) | [C860 v1 binomial argument](../../claims/Yin_C_G0860_v1.md#higher-depth-hankel-comparison) | Only the exact scaled-binomial valuation and formal truncation remainder for integer lambda>=3, checked for use after multiplication by the integral center. |
| [Whole all-place finding](#all-place-mask-whole) | [C858 finite rank interface](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) | Only the finite coefficient recurrence converting numerator/denominator degree at most b into shifted Hankel rank at most b; no transfer of its uncentered hypotheses or other conclusions. |
| [Whole all-place finding](#all-place-mask-whole) | [Bel17 integer-ring input](../literature/Bel17/Yin_U001.md#bel17-u001) | Accepted cyclotomic integer ring and degree matched to every odd prime q; squarefree mod-two decomposition checked locally, original integer-ring proof still not re-audited. |
| [Whole all-place finding](#all-place-mask-whole) | [C857 v1 retained statement](../../claims/Yin_C_G0857_v1.md#statement) | Comparison preserving the arbitrary-field one-place classification and simple-pole domain; this binding is not another whole-v1 proof review. |
| [Whole all-place finding](#all-place-mask-whole) | [C857 v1 large-measure controls](../../claims/Yin_C_G0857_v1.md#large-period-full-mask) | Preservation of the original m(P)>log 2 control domain, finite precision and absence of near-one supply; earlier full-proof evidence remains R1074 v1. |
