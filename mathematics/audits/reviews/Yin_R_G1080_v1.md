---
author: Yin
---
# Independent whole-proof review of the four-pair torus partial bounds

Review act: 2026-11-04T17:51 UTC minute; human record author Yin.
This initial independent review covers the complete working-tree v1 of [C863](../../claims/Yin_C_G0863_v1.md), all eight numbered statements, every proof section and its order 4096, bits 40 native computation premise.
The reviewed text includes the corrected factual description that the current generator and certificate both use 81/25; no moment, result or mathematical argument changed in that correction.

The reviewer did not participate in proof development and supplied no mathematical repair.
It received the fixed proof, necessary input locations and parameters, review scope, authorization facts and current rules.
It formed its findings without reading D17, D18, proof-generation dialogue, contributor explanations outside the fixed proof or previous C863 reviews.
Necessary existing source and theorem interfaces were consulted with the original-proof limits stated below.
The independent checker was implemented and read back by this reviewer; no separate independent audit or formal verification of that checker is claimed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Statement](../../claims/Yin_C_G0863_v1.md#statement) | All eight statements, exact hypotheses, Haar normalization, sign and uniformity quantifiers. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Limit tori](../../claims/Yin_C_G0863_v1.md#admissible-limit-tori) | Complete positive-frequency characterization, saturation, compact space, inversions and nondegeneracy. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Strict-to-uniform argument](../../claims/Yin_C_G0863_v1.md#strict-to-uniform) | Complete regularization, upper semicontinuity, finite-sign minimum, attained maximum and conditional uniformity; comparison boundaries. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Independent torus](../../claims/Yin_C_G0863_v1.md#independent-torus-certificate) | Complete IC1--IC6, finite-log analytic bridge and actual 4096-order exact computation. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Coloop](../../claims/Yin_C_G0863_v1.md#coloop-bound) | Product Haar, conditional Jensen, hyperbolic estimate, second moments and 5/1296 margin. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Common phase](../../claims/Yin_C_G0863_v1.md#common-phase-bound) | Integral cocharacter, distinct residual exponents, Jensen, extreme lag, variance and 1/512 margin. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Finite fibers](../../claims/Yin_C_G0863_v1.md#finite-fiber-bound) | Complete fiber argument, rank-three cutoff 6, every-rank cutoff 128, and deletion-index formulas. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Rank-two cross](../../claims/Yin_C_G0863_v1.md#rank-two-cross-margin) | All sixteen signs, quadratic Jensen, reduced nonsingular integral and strict log(184/93) bound. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Rank stratification](../../claims/Yin_C_G0863_v1.md#rank-stratification) | Finite residual rank-three family, sign classes, unresolved example, Lawton obstruction interpretation and conditional finite rank-one reduction. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Input roles](../../claims/Yin_C_G0863_v1.md#exact-inputs-and-reuse-roles) | Proof premises distinguished from attribution, comparison and extraction provenance. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Arithmetic boundary](../../claims/Yin_C_G0863_v1.md#contribution-and-arithmetic-return-boundary) | No universal sign theorem, automatic original-input auxiliary supply or unrestricted Task completion follows. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Author generator](../../computations/programs/Yin_J_G0134/independent-torus.py) | Entire source inspected for IC1--IC3 and current 81/25 comparison; independently recomputed rather than newly executing this generator. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Native certificate](../../computations/programs/Yin_J_G0134/inputs/independent-torus-certificate.json) | All seven integer fields matched by complete independent order 4096, bits 40 recomputation. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Independent checker](../../computations/programs/Yin_J_G0134/verify-independent-torus.py) | Reviewer-authored source read back and actually executed in full; its own code inspection is by its implementer. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Den09 Mahler conventions](../literature/Den09/Yin_U001.md#mahler-measure) | Accepted logarithmic integrability, circle Jensen through zeros and monomial invariance, without a new original-proof audit. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Den09 marked groups](../literature/Den09/Yin_U002.md#marked-groups) | Attribution and normalization for the upper-semicontinuity mechanism proved directly in C863. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [Den09 Lawton interface](../literature/Den09/Yin_U002.md#specializations-and-remaining-source-reports) | Retained Theorem 14/Example 15 for a fixed Laurent polynomial including zeros; only the conditional obstruction interpretation uses full convergence. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [C844 extreme lag](../../claims/Yin_C_G0844_v1.md#uniform-energy-logarithmic-margin) | Mechanism comparison and complete multivariate adaptation rechecked locally, not the rest of C844. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [BGMP24](../literature/BGMP24/Yin_U001.md#accepted-regularization-interface) | Comparison of rho>D with ambient D=2; neither its estimate nor its disputed later constant is a proof premise. |
| [Whole proof and exact computation](#whole-proof-and-exact-computation) | [C849](../../claims/Yin_C_G0849_v1.md#fixed-bivariate-template-specialization-class) | Fixed-template comparison and preserved arithmetic hypotheses, not a new full proof audit or an auxiliary-supply premise. |

## Whole proof and exact computation

**Finding: all eight stated partial results and their complete supporting argument are supported, with no mathematical gap found.**
The necessary exact finite calculation was independently completed, not assumed from its certificate.
This supports C863 only at its stated partial scope.

### Compactness and uniformity

Subgroup and saturation axioms are closed membership-coordinate conditions, and LT1 imposes finitely many closed exclusions, so K is compact.
Character integrals identify the limiting Haar measure.
A finite basis of a limiting lattice is eventually present, giving the necessary positive distinct vector in its orthogonal complement.
Conversely, saturation makes every additional forbidden relation a proper rational hyperplane.
A finite union of these cannot exhaust the positive relatively open cone, yielding the required approximating integer vectors.
The same argument outside the coordinate and pairwise-equality hyperplanes, followed by coordinate inversions, proves the stated equality of sign-minimum suprema.

LT1 gives eight distinct nonzero character terms, so every restricted Laurent polynomial is nonzero and logarithmically integrable.
Continuous regularizations decrease to the actual logarithm, giving upper semicontinuity in the stated direction.
The finite minimum is upper semicontinuous and attains its maximum.
Thus one common positive margin follows only from strict inequality at every H in K.
The proof does not replace this hypothesis by separately checked circle margins.

### Coloop and common phase

The coloop condition removes every relation involving that coordinate, so the corresponding joint Haar image is a product even without individual primitivity.
Circle Jensen gives h(|A|), and the displayed cosh-square estimate yields h(x)<=3x^2/(2sqrt11).
Noncollision and torsion-freeness give the three sine terms total second moment 3/2.
The resulting gamma and its strict comparisons with 11/16 and 56/81 yield the stated 5/1296 margin.

The common-phase homomorphism is well-defined on the free character lattice.
A primitive cocharacter extends to torus coordinates, and coincident residual exponents would violate LT1.
A separating linear functional makes the extreme support difference arise from exactly one ordered pair.
Its two opposite Fourier coefficients give variance at least 1/8, without an interior cancellation exception.
Strong concavity of log on (0,4] then proves the 1/512 margin, with integrability justifying zeros and Fubini.
The entire multivariate adaptation was checked directly.

### Exact native computation and its analytic bridge

The balanced-walk count proves IC1 with A_0,A_1,A_2,A_3=1,8,168,5120.
The finite logarithm inequality integrates without an infinite-series interchange.
The moment interpretation gives 0<=B_j<=64^j, and every IC3 floor rounds downward.

The independent checker does not import or execute the author generator.
For a two-coordinate sum S, Vandermonde gives CT(S^(2k))=binom(2k,k)^2, and its odd moments vanish.
Splitting four coordinates into two pairs yields the independently implemented formula

    A_n=sum_(k=0..n)binom(2n,2k)*binom(2k,k)^2
                         *binom(2n-2k,n-k)^2.

The checker evaluates this symmetric convolution with exact divisions, unlike the author's inner binomial-square summation.
It evaluates every B_j by Horner's rule, checks its complete interval bound, and performs the prescribed integer floor.
Direct four-dimensional lattice-walk counting through length 8 separately gives

    A_0,...,A_4 = 1,8,168,5120,190120.

The following command actually completed from the repository root:

    python mathematics/computations/programs/Yin_J_G0134/verify-independent-torus.py

It recomputed every moment through 4096 and every transform and floor for 1<=j<=4096 using standard-library arbitrary-precision integers.
All seven native fields matched exactly:

    order=4096, rounding_bits=40,
    N=3565677176283, D=1099511627776,
    target_numerator=81, target_denominator=25,
    positive_integer_margin=25*N-81*D=81487557219>0.

The replaceable local result is `mathematics/computations/outputs/Yin_J_G0134/independent-torus-verification.json`.
The retained program, native input, parameters and mathematical bridge permit reproduction; the ignored output is not the sole fixed evidence.
This is complete independent integer recomputation, not a smaller control run, inspection of the claimed sum or a formal proof-assistant result.
The checker itself received its implementer's readback, not a separate independent code audit.

The atanh tail estimates give 56/81<log2<1123/1620<52/75, with final difference 1/8100.
Combining log64<104/25 with S4096>=N/D>81/25 proves m_free<23/50.

### Finite fibers and the different rank cutoffs

At rank three, deleting the coordinate with relation coefficient modulus q gives a surjection onto the full three-torus with uniform q-point fibers.
The product over z^q=w equals the quadratic-root product used in LT10 and costs at most 2log2/q.
Nonzeroness and logarithmic integrability justify integrating through exceptional zero fibers.

For general rank, X/X_j is cyclic because the omitted character and X_j generate X.
When finite, its order is q_j and the omitted character identifies the kernel with the q_j-th roots of unity.
The projected characters retain nontriviality and noncollision in X_j.
Thus their sine second moment is still 3/2, without independence, proving the general gamma+2log2/q_j estimate and cutoff 128.
The exact comparison 49sqrt11>162 proves eta_large>0.
The circle gcd formula and the rank-two gcd-of-relation-coordinates formula follow from the same cyclic quotient.
Rank drop on deletion is the coloop case.

Only at rank three is the projected base the full independent three-torus.
There its integral of h equals m_free, giving the stronger 23/50+2log2/q bound.
For q>=6 the difference from log2 is greater than (2/3)(56/81)-23/50=11/12150.
The proof does not transfer cutoff 6 to lower rank.

### Cross template, sign classes and residual configurations

Translations and global reversal give the eight sign flips with equal third and fourth entries.
Swapping the two torus variables connects the remaining two orbits, establishing equality of all sixteen means.
The quadratic Jensen calculation gives XC2 including A=0, and the reduced R satisfies 3/5<=R<=3.
The explicit integrals of |A| and |sin y| on I yield ER<=1/3+(2sqrt3+8/5)/pi.
The radical comparisons and the inscribed regular twelve-gon prove the strict rational bound ER<184/93<2.
Jensen then proves XC6 without quadrature or a singular-log cutoff.
The conclusion concerns the Haar template, not every circle specialization.

Removing zero coefficients, equal-weight partitions and coefficient modulus at least 6 leaves the stated finite rank-three family.
Primitivity makes the sign-translation subgroup have index two.
An odd coefficient sum places global reversal outside it and therefore makes all signs equivalent.
The vector (1,2,5,4) is positive, distinct and orthogonal to (1,1,1,-2).
The possible obstruction argument requires full Lawton convergence within this fixed torus, exactly as distinguished from upper semicontinuity in the proof.

Dimension at least two is closed because three independent limit relations would eventually occur together.
Under the stated strict-good-sign hypothesis, finitely many open neighborhoods cover that compact subset.
The compact complement consists of rank-one tori, each isolated by its three basis relations.
Saturation excludes a proper enlargement of equal rank, and LT1 excludes a rank-four enlargement.
This compact discrete complement is finite.
The reduction is conditional and establishes no missing rank-two or rank-three inequality.

### Source and completion limits

The accepted Den09-U001 integrability and circle-Jensen interfaces are used at their recorded scope.
Den09-U002 supplies the full Lawton theorem at statement/applicability depth, including zeros; its original proof was not re-audited.
The upper-semicontinuity mechanism and the multivariate energy adaptation were directly checked in C863.
BGMP24 and C849 remain comparisons with their exact retained qualifications, rather than unexamined premises of the partial bounds.
No new original-source proof audit, novelty search or priority claim is made.

The general small-index rank-two configurations, untested finite rank-three family and remaining actual rank-one tuples remain unresolved.
The universal four-pair strict hypothesis, original-input auxiliary supply and unrestricted Lehmer Task are not completed by this finding.
