---
author: Yin
---

# C868: independent whole-proof review of analytic damping and the cyclotomic three-block gap

Review act: 2026-11-05T18:04, UTC.
The human record author is Yin.
This is the first whole-proof inspection by a separately assigned AI reviewer who did not contribute to the candidate's proof development and received no inherited substantive development discussion, derivation summary, author explanation or earlier review conclusion.
The supplied mathematical candidate was the actual fixed [C868 v1](../../claims/Yin_C_G0868_v1.md#statement), including its complete argument.
The subsequent input-synchronization notice concerned removal of a duplicate statement anchor and clarification that the H2 norm definition is squared; the actual current candidate was checked.
No L133 development body, strategy, proof-generation dialogue or earlier project-review finding was consulted.
The reviewer enumerated obligations from the statement, checked the argument and formed initial mathematical findings before reading the BM05 source-comparison unit.
No previous project proof review supplies any part of the present conclusion.

## Inputs

- [C868 exact statement](../../claims/Yin_C_G0868_v1.md#statement) and [complete argument](../../claims/Yin_C_G0868_v1.md#argument): the full AM1-AM2 and CG1-CG5 assertions, zero classification, constants, specializations and scope qualifications.
- [Den09 U002](../literature/Den09/Yin_U002.md#den09-u002): the retained arXiv:0905.0604v1 Theorem14/Example15 Lawton statement, specifically the fixed Laurent polynomial, sup-norm relation parameter and permission for torus zeros.
  Its statement and application are checked here; its original proof is an accepted external input and is not newly audited.
- [BM05 quadratic source mechanism](../literature/BM05/Yin_U001.md#source-quadratic-families), [finite-cover comparison](../literature/BM05/Yin_U001.md#finite-cover-and-exact-control) and [scope boundary](../literature/BM05/Yin_U001.md#numerical-scope-and-prefix-boundary): inspected as recorded attribution and comparison, not as premises supplying the unrestricted gap.
  The original BM05 article and numerical searches were not newly inspected or reproduced.
- [Original G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract): the unrestricted, unnormalized positive Mahler-gap objective, used only to check the candidate's explicit noncompletion boundary.

The candidate's C224, C10, C296 and L133 references describe provenance or comparison rather than necessary logical premises of its supplied proof.
Their proof bodies and prior assessments are not used by this finding.
The present independent evidence is new and belongs in this R; it does not replace the proof or select a C assessment.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [C868 statement](../../claims/Yin_C_G0868_v1.md#statement) | Entire AM1-AM2 and CG1-CG5 statement, precise zero cases, normalization, quantifiers and stated limitations. |
| [Whole-proof finding](#whole-proof-finding) | [C868 argument](../../claims/Yin_C_G0868_v1.md#argument) | Entire six-section argument, including integrability, Poisson boundary passage, first crossing, short polynomials and fixed-pair return. |
| [Whole-proof finding](#whole-proof-finding) | [Den09 Lawton input](../literature/Den09/Yin_U002.md#den09-u002) | Theorem14/Example15 statement and its application to the fixed nonzero Laurent polynomial F and vectors (1,N); no original-proof audit or review of the unit's other results. |
| [Whole-proof finding](#whole-proof-finding) | [BM05 quadratic mechanism](../literature/BM05/Yin_U001.md#source-quadratic-families) | Recorded source attribution for the reciprocal quadratic Jensen mechanism; no dependency on a source proof for the locally supplied calculation. |
| [Whole-proof finding](#whole-proof-finding) | [BM05 comparison boundary](../literature/BM05/Yin_U001.md#numerical-scope-and-prefix-boundary) | The retained bounded source comparison supplies no unrestricted-pair gap or priority conclusion. |
| [Whole-proof finding](#whole-proof-finding) | [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) | Comparison of the unrestricted total-Mahler target with the candidate's family and fixed-pair limit; explicitly not a completion review. |

## Obligations and decisive checks

### Analytic-majorant assertion

The obligations are to construct the damping from merely integrable nonnegative g, obtain coefficient H2 estimates without an H2 hypothesis on f, justify truncating the product, and minimize over every first integer energy crossing.
The kernel defining H has a uniformly convergent analytic series on each compact subdisk, dominated by an integrable multiple of g.
Thus H is analytic, Re H=P[g]>=0 and H(0)=epsilon.
The functions q=exp(-H) and b=fq satisfy |q|<=1, q(0)=exp(-epsilon) and |b|<=2, including at zeros of f.
Radial orthogonality and monotone convergence of coefficient sums give ||q||_H2<=1 and ||b||_H2<=2.
Expanding against the constant coefficient gives ||1-q||_H2^2<=2(1-exp(-epsilon))<=2epsilon.
The radial multiplier estimate uses |P(r zeta)|<=L(P), so it applies to P(1-q) without assuming a boundary value for f.

At the first index N with prefix energy at least5, N>=1 because c_0=1.
All earlier nonzero coefficients have modulus1: a modulus at least2 would already contribute energy at least5 together with c_0.
Hence s is an integer in {1,2,3,4}, c=|c_N|>=1, L(P)=s+c and ||P||_H2=sqrt(s+c^2).
The vanishing order of f-P proves the exact identity S_N b=S_N(Pq); no uncontrolled tail is estimated in H2.
Truncation is applied only to b and P(1-q), whose H2 membership has already been proved.
This yields sqrt(s+c^2)<=2+(s+c)sqrt(2epsilon).

The integer minimization covers all admissible cases.
For c=1 one must have s=4, attaining (sqrt(5)-2)/5.
For c=2,s=1 the same numerator has denominator3; for c=2,s>=2 the ratio is at least (sqrt(6)-2)/6>1/15.
For c>=3 it is at least (c-2)/(c+4)>=1/7.
Both latter bounds exceed (sqrt(5)-2)/5<1/20.
Squaring the resulting nonnegative inequality gives exactly epsilon>=(sqrt(5)-2)^2/50=gamma.
If no crossing exists, total coefficient energy is at most4; integrality makes the support finite.
This proves the stated contrapositive without a degree, frequency, boundary-regularity or support assumption.

### Cyclotomic quotient, integrability and Poisson passage

All roots of A0 and B0 lie on T, so f=B0/A0 is holomorphic and nonzero in the open disk.
The constant coefficient1 of A0 gives integer Taylor coefficients recursively, with c_0=1.
Reciprocity and real coefficients make A,B real on T, and |B/A|=|f| outside the finite exceptional set.
These facts include empty products, common roots and repeated factors.

For each regular x-fiber, the reciprocal quadratic y^2-ty+1 has root-modulus contribution phi(t).
The normalized factor log|1-r y| has mean0 and L1 norm at most2log2 for 0<=r<=1; the boundary endpoint is justified by the subsequent radial L1 argument.
The two root factors therefore give the bound phi(t)+4log2 for the fiber's absolute logarithmic integral.
The inequality phi(t)<=log^+|B0(x)|+log^-|A0(x)| has an integrable right side, and log|A(x)| is integrable as a finite sum of logarithmic boundary-root factors.
Tonelli on absolute values supplies absolute integrability of log|F| before Fubini is invoked.
Fibers over the finitely many zeros of A0, including an identically zero fiber at a common root, form a null set.
The zero Mahler measure of A0 then proves CG1.

For one boundary-root factor, |1-rho exp(i theta)|>=sqrt(2)|theta|/pi for rho>=1/2 follows from (1-rho)^2+2rho(1-cos(theta)).
This gives an integrable logarithmic dominator, while positive parts are bounded by log2.
The radial logarithms converge in L1, and the bounded Poisson kernel at a fixed interior point permits passage to the harmonic limit.
Finite signed sums give the exact Poisson identity for log|f|, with no residual singular boundary measure.
The inequality log|f|<=log2+phi(B/A), followed by positivity and mass1 of the Poisson kernel, supplies AM1 with epsilon=m_2(F).
There is no circular dependence on Lawton or the sought gap.

### Short-polynomial completion and exact zero cases

When epsilon<gamma, the analytic assertion makes f an integer polynomial of energy at most4.
The identity A0 f=B0 then gives monicity, constant coefficient1, even degree2(b-a), and reciprocity by reversal and cancellation.
These properties are obtained only after polynomiality.
Energy1 gives f=1, while energy2 gives f=1+z^(2h), h>=1.
A coefficient of modulus at least2 would violate the energy bound together with the constant coefficient, so all nonzero coefficients have modulus1.
At energy3, reciprocity forces the third coefficient to be central, giving 1+sigma z^h+z^(2h).
The set sigma cos(h theta)>=sqrt(3)/2 has normalized measure1/6, independently of h, and forces |f|>5/2.
Thus epsilon>=log2/6.

At energy4, X=|f|^2-4 has mean0, lies in [-4,12], and its two extreme Fourier coefficients are1, because the constant and leading coefficients of f are1.
Orthogonality gives E X^2>=2.
The bound X^2<=12X_++4X_- and E X_+=E X_- give E X_+>=1/8.
On X>0, phi(B/A)>=log(|f|/2)=(1/2)log(1+X/4)>=X/32, hence epsilon>=1/256.
Both positive bounds strictly exceed gamma<1/800.
The energy4 calculation includes every arrangement of four coefficients and uses no unrecorded sparse-polynomial classification.
Thus epsilon<gamma leaves exactly the first two polynomial forms.

For f=1, b=a and B=A; for f=1+z^(2h), b=a+h and B/A=x^h+x^(-h).
The stated factorizations, or CG1 directly, give epsilon=0 in both cases.
This proves both directions of CG3 and the non-strict lower alternative epsilon>=gamma for every other pair.

### Fixed-pair return and original-target boundary

For N>max(0,b-a), k=N+a-b is positive and k+2b=N+a+b<2(N+a).
The shifted B0 block cannot cancel the constant or top coefficient of the two A0 blocks.
The actual degree is2(N+a), both endpoint coefficients are1, and reflection about degree N+a exchanges the A0 blocks while preserving the shifted B0 block.
This verifies integrality, monicity and reciprocity, even when blocks overlap or share factors.
The exact identity P_N=t^(N+a)F(t,t^N) preserves logarithmic measures.

The nonzero integer relations on (1,N) are (-Nj,j), j nonzero, so their least sup norm is N.
The retained Den09 Theorem14/Example15 statement applies to this fixed nonzero F and allows its torus zeros.
Its multiplicative measure limit passes to logarithmic measures because the limiting measure is exp(m_2(F))>0, establishing CG5.
No varying-polynomial theorem or zero-free restriction is substituted for this input.
For a fixed pair outside CG3, convergence to a value at least gamma gives the eventual lower bound gamma/2, with a pair-dependent delay.

The example A0=1+t^2, B0=1, N=1 satisfies the delay condition and gives P_N=t^4+t^2+1=(t^6-1)/(t^2-1), of measure0, although the pair lies outside CG3.
It correctly excludes a positive bound for every permitted finite delay.
The counterfactual choice of a separate sufficiently large N_j for each positive epsilon_j tending to zero preserves total measures, positivity and the actual full degree; CG2 excludes that premise.
This does not cover varying pairs and delays without vanishing two-variable costs, arbitrary primitive integer polynomials, irreducibility or a Task-specific all-power property.
The original unrestricted G0001 contract therefore remains unresolved.

## Source applicability and limits

The only accepted external theorem needed for the argument is the fixed-Laurent-polynomial Lawton theorem recorded in Den09 U002 for arXiv:0905.0604v1, Theorem14 and Example15.
This review reuses that adequate source statement and verifies its entire application; it makes no new original-PDF inspection or Lawton-proof claim.
The locally supplied logarithmic, Fourier, Poisson and short-polynomial arguments are checked above.
BM05 U001 identifies the established reciprocal-quadratic Jensen mechanism and its source subfamilies, while expressly limiting the numerical and unrestricted-gap scope.
C868 accurately treats that material as attribution and comparison and derives CG2 locally.
No unresolved source-statement or hypothesis mismatch was found for the proof inputs actually used.
Historical contribution assertions, comparisons of other project C proofs, literature priority and an exhaustive novelty search are outside this review's source conclusion.

## Whole-proof finding

The entire supplied C868 v1 statement and complete argument are mathematically supported under their exact hypotheses, with no gap found.
This is an independently reviewed whole-proof finding for AM1-AM2, CG1-CG5 and the exact zero classification, using Lawton only at the disclosed accepted-theorem interface.
No substantive repair was supplied by this reviewer.
The finding supports adoption of the candidate at that scope; it supplies neither an effective or pair-uniform specialization cutoff nor a solution of G0001.
No C assessment, Task decision, strategy or execution boundary is changed by this review record.
