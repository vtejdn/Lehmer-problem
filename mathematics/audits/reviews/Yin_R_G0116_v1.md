---
author: Yin
---

# Retained project review: Fractional critical return moments and unbounded exponential convolution

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0252_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="critical-lp-complete-independent-review"></a>

### Complete independent review of the critical integrability argument

Date: 2026-10-10T00:16.
Actor: Yin.
The separate arithmetic/resultant reviewer read the complete frozen author Sections1--5, every equation(1)--(17), and the actual retained interfaces used below.
The coordinator supplied all new derivations in this draft; this reviewer supplied none of its mixture, moment, distribution, approximation or exponential-control arguments.
This is a complete noncontributor mathematical review in shared project context, not a blind review.
The reviewer previously reviewed the proofs now retained in L240 and L248 and reviewed and mechanically retained L206; those earlier roles are disclosed rather than relabelled as new independent source audits.
The reviewer also authored other arithmetic materials, but none is a new premise here.

**Outcome and inspected boundary.**
No mathematical defect or required author correction was found.
The complete stated conclusions pass at their displayed scope: Sections2--3 require the actual critical transience and complete fractional-moment or Abel-modulus hypothesis; Section4 supplies an actual torsion control and no nontorsion near-one classification.
The review independently recalculated every displayed inequality and constant rather than inferring correctness from an earlier summary.
No numerical program, J, new source acquisition, material fingerprint or fixed-material edit was required.

**Original law, actual order and retained interfaces.**
The whole-order construction in L240 uses the actual additive order Z[alpha], its power-basis torus and the original difference probabilities1/2,1/4,1/4.
The reviewer directly checked its transient L1 limits and Section4's complete nonnegative Fourier mass and Fejer bounded-density equivalence.
Its nontorsion ergodicity restriction belongs to the separate recurrent-factor singularity proof; it does not restrict the transient density formula or the bounded-convolution criterion used here.
The reviewer also directly checked L248's full two-parameter overlap, its one-critical limit and its coefficient-monotonicity norm identity.
These yield exactly(2) and(10), including eta_R, for every actual unit in the stated transient domain.
The passage from a_s*b_R to its continuous density and exact supremum uses an absolutely summable full Fourier series, so it does not assume bounded individual factor densities.
Neither parameter is required to exceed one.
In particular the R=1 torsion example is within these interfaces.

**The positive mixture and all its normalizations, (1)--(7).**
Critical transience gives finite U_R and positive eta_R, with the normalized densities genuinely in L1.
Multiplying a_s by U(s)/U_R produces U_R^(-1) sum s^n W_n H; subtracting it from a_R gives exactly the nonnegative second measure displayed after(3).
Its mass is (U_R-U(s))/U_R.
Subtracting a_s instead and using the triangle inequality therefore gives twice that mass in the L1 convention, as asserted in(4).
Convolution with the probability b_R is an L1 contraction by Tonelli.
Independently, eta_s-eta_R=D/[U(s)U_R], which proves the exact divided-difference substitution(5).
U(s)>=1 and eta_R<=1 then give precisely(7), with B=M/U_R.
No first-return derivative or L2 premise is hidden in these steps.
The same mixture proof works with the other factor varying.
This construction would not normalize at an infinite U_R, and the draft explicitly excludes that use.

**Distribution endpoint and quantitative approximation, (8)--(11).**
With p_*=1/(1-a), the choice delta=(4B/y)^p_* makes B delta^(a-1)=y/4.
The two pieces of y_0 ensure both delta<=delta_0 and 1+y/4<=y/2.
On the set C_R>y, the difference from C_s thus exceeds y/2; (4) gives the bound (4B/y)^p_* exactly.
The bounded lower y interval and this tail prove the weak endpoint, and integrating p y^(p-1) proves(9), with denominator p_*-p positive only in the stated strict range.
This does not establish the strong endpoint.

For the dyadic approximation, the triangle inequality through C_R bounds the consecutive L1 difference by 2B(delta_j^a+delta_(j+1)^a)<=4B delta_j^a.
The Fourier differences from L248 are nonnegative coefficients in an absolutely convergent series, hence their sup norm is the coefficient sum at zero even though their real-space function need not be nonnegative.
Dropping the lower K term and using(7) at delta_(j+1) yields at most 1+B 2^(1-a)delta_j^(a-1); delta_j<=1 turns this into D_0 delta_j^(a-1) with the displayed D_0.
Applying the elementary L1/L-infinity norm inequality gives exponent a/p+(a-1)(1-1/p)=a-1+1/p.
Its positivity is exactly p<p_*.
The geometric series has denominator 1-2^(-gamma), and its Lp limit agrees with the already established L1 limit on the probability space.
This checks(11), including p=1.
There is no endpoint or supremum-norm convergence conclusion hidden in this limit order.

**Complete moments and renewal, (12)--(13).**
The inequality 1-(1-delta)^n<=min(1,n delta)<=(n delta)^a holds for all n>=1 and0<a<1, so the entire Green moment gives the stated global Abel modulus.
For(13), the first-return contribution is one nonnegative term of the complete renewal expansion.
In a k-fold convolution, subadditivity of x^a for0<a<=1 gives at most k F(R)^(k-1) Q_a.
Summation of this geometric derivative is Q_a/(1-F(R))^2=Q_a/eta_R^2.
Tonelli permits the infinite-value cases, and positive eta_R makes the two finiteness conditions equivalent.
At a=1 this is the old finite critical derivative regime, as the text states.
A selected set of returned words would only give a lower truncation and cannot replace the upper moment hypothesis.

**The actual degree-four control, (14)--(15).**
The reviewer read the exact product and critical-series scope retained at L206's cyclotomic control.
Translation of t^4+1 gives t^4+4t^3+6t^2+4t+2, so the asserted irreducible degree follows directly by Eisenstein.
The actual order and core are Z^4, with cyclic coordinate updates and the full product p_(4ell+s)=b_ell^(4-s)b_(ell+1)^s.
The retained induction bounds follow from b_(j+1)/b_j=(2j+1)/(2j+2), with both displayed squared inequalities in the required directions.
They are not asymptotic substitutions.
For every residue s, the upper product is at most(ell+1)^(-2), and n+1<=4(ell+1) gives16/(n+1)^2, including n=0.
At n=4ell>=4 the lower product gives n p_n>=1/(4ell).
Consequently U(1) is finite but its first weighted moment diverges; complete renewal then gives F(1)<1 and F'(1)=infinity.
L240's bounded-density equivalence applies to this torsion input and proves essential unboundedness.

For the full Abel difference the reviewer recomputed the split at N=floor(1/delta).
The first N summands are bounded using n/(n+1)^2<=1/(n+1) and the logarithmic integral comparison.
N+1<=2/delta gives the displayed logarithm.
The tail is at most1/(N+1)<=delta, with the inequality direction valid also when1/delta is an integer.
This proves(15) for the entire sequence, not just multiples of four.
The DS84 source record was read at its actual classical-comparison scope: it distinguishes the book's nearest-neighbor walk from this cyclic original law.
No new book theorem or proof audit is being adopted by this review; the relevant algebraic law and estimates are already supplied and checked locally.

**Exponential tail, constants and Fourier conclusion, (16)--(17).**
Substituting delta=e^(-v) into(4),(5),(15), and retaining U_R,U(s)>=1, gives the stated bounds with A=17+16 log2.
Setting y=2A+32v makes the sup bound exactly y/2.
The resulting probability bound has numerator64(v+log2+1); comparison with2 follows from 4A-64(log2+1)=4.
The threshold v>=log2 is exactly delta<=1/2, and y_0=34+64 log2 is correct.
The exponential layer integral below y_0 is bounded by exp(y_0/64), which equals2 exp(17/32).
Its remaining integral equals2 exp(17/32) as well, proving the explicit constant4 exp(17/32).
This uses Tonelli on nonnegative tails and does not require prior exponential integrability.
Every finite Lp norm follows, including L2.
Parseval then gives square-summable complete coefficients, whereas absolute summability would yield a continuous bounded density, contrary to the verified infinite critical mean.
The asserted unboundedness is essential, not an artifact of the Fourier series value at one point.

**Contribution and remaining mathematical obligations.**
The automatic transient L1 density, mixed-parameter norm, complete torsion return law and critical-type classification are accurately identified as reuse.
The new deductions are the fractional-moment regularity and rate and the explicit exponential regularity calibration in the unbounded case.
No exhaustive novelty claim is justified or needed.
This review does not turn the torsion m=0 example into a positive-small-measure family, infer unknown Salem transience or a complete fractional upper moment, bound constants uniformly in input or degree, prove a strong endpoint, or obtain finite critical mean from finite-p regularity.
The Section5 distinction from fixed killed-box lower truncations and from L247's fixed-height escape is sound.
The unrestricted G0001 goal remains active and unresolved.
The full proposed result is eligible for the coordinator's scoped adoption; this review itself does not create a fixed ledger or promote any broader claim.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original complete finding](#critical-lp-complete-independent-review) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original complete finding](#critical-lp-complete-independent-review) | [Original full L252](../../ledger/Yin_L_G0252_v1.md#complete-retained-proof-and-review) | Entire frozen Sections1--5/equations1--17, actual transient law, mixtures/moments/weak endpoint/strict strong-Lp/rate, whole torsion exponential control and every source/uniformity/negative boundary. |
| [Original complete finding](#critical-lp-complete-independent-review) | [Original whole-order critical construction](../../ledger/Yin_L_G0240_v1.md#whole-order-critical-abel-limits) | Actual transient L1 limits, full actual order/original digits; nontorsion ergodicity restriction not imported into the transient formulas. |
| [Original complete finding](#critical-lp-complete-independent-review) | [Original full bounded-density criterion](../../ledger/Yin_L_G0240_v1.md#critical-convolution-bounded-density-test) | Complete nonnegative Fourier occupation mass and both directions of the Fejer essential-boundedness/finite-critical-mean equivalence, including torsion. |
| [Original complete finding](#critical-lp-complete-independent-review) | [Original mixed overlap](../../ledger/Yin_L_G0248_v1.md#mixed-parameter-full-overlap) | Complete two-parameter original-law overlap and continuous density norm, not an individual-factor Lp assumption. |
| [Original complete finding](#critical-lp-complete-independent-review) | [Original one-critical bound](../../ledger/Yin_L_G0248_v1.md#one-critical-factor-smoothing) | Exact K(s,R) including eta_R and arbitrary R1/torsion, full summability and continuous density. |
| [Original complete finding](#critical-lp-complete-independent-review) | [Original norm monotonicity](../../ledger/Yin_L_G0248_v1.md#exact-critical-convolution-modulus) | Nonnegative Fourier coefficient differences, their exact sup norm and actual first-return moment limits; no pointwise positivity of difference densities. |
| [Original complete finding](#critical-lp-complete-independent-review) | [Original actual cyclotomic control](../../ledger/Yin_L_G0206_v1.md#cyclotomic-radical-critical-thresholds) | Actual irreducible t4+1 order/core, cyclic all-residue binomial product, induction bounds and complete critical-series classification. |
| [Original complete finding](#critical-lp-complete-independent-review) | [Original DS84 comparison](../literature/DS84/readme.md) | Actual classical attribution/model-comparison scope only; nearest-neighbor book walk is not the cyclic algebraic law and no new book proof is imported. |

The original separate noncontributor account states shared project context and nonblind review but does not preserve the initial target-development content supplied or consulted before its own findings.
Its upstream reviews and unrelated arithmetic authorship establish neither isolation nor actual shared substantive development of this target.
The whole original relationship is therefore unknown at the complete bound scope above; the original independent title does not resolve that missing fact.
Original date, verdict, every inequality/constant, source boundary and no-program-run facts remain unchanged.
No current self-check or later C is backdated into the original finding.
