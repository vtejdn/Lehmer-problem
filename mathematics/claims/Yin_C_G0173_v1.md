---
author: Yin
---
# Scalar transforms cannot remove the moving-Salem Fourier expense

Date: 2026-10-18T16:58.
Human author Yin.
Root supplied the broad question about fixed and varying scalar transforms on the accepted C171/C172 family.
The angular_envelope_review agent develops the new continuous-transform and compactness argument; no proof step was supplied by root at this stage.
This Claim registers the complete author argument, with the independently checked compactness attribution below; mathematical review and adoption remain separate.
No numerical program, parameter scan or new external theorem is invoked.

<a id="scalar-transform-question"></a>
## Exact changed question and reuse

The accepted [C171](Yin_C_G0171_v1.md#two-block-torus-statement) proves original projection-coherence divergence on the actual L402 moving-prime Salem family.
[C158](Yin_C_G0158_v1.md#statement) consequently gives full-logarithm divergence, and [C172](Yin_C_G0172_v1.md#moving-cubic-statement) proves divergence for its particular cubic using a nonzero first w-band coefficient.
A different nonconstant transform can have that particular coefficient zero, so the cubic's coefficient argument alone does not settle all scalar transforms.
The changed question is whether the full singularity persists for every continuous nonconstant scalar function, and uniformly for a bounded equi-Lipschitz class kept away from constants.
The actual norm normalization, single circle Haar measure and original frequency return must remain unchanged.

A bounded current G-line search for scalar transforms, contact/Haar margins, equicontinuity and continuous Wiener conclusions found no fixed result answering this question.
The directly inspected C171/C172 interfaces, current S1/S3/S5 frontiers and existing C168 contact comparison supply the relevant retained boundary.
This is a local reuse screen, not a claim of literature novelty.

The present author contributed to C171 and C172.
Their separately accepted [R417](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) and [R420](../audits/reviews/Yin_R_G0420_v1.md#moving-cubic-whole-independent-finding) are reused at their exact scopes, not called independent rechecks by this author.

<a id="scalar-transform-statement"></a>
## 1. Exact actual inputs and author conclusion

Keep precisely the accepted L402/C171 schedule K,a_j,b_j,c_j, its actual original Salem polynomials P_j and

    L_j=K+a_j+b_j+2, d_j=c_j+L_j-3, N_j=2d_j.

Every P_j is monic irreducible Salem of trace-1, with log2<m(P_j)<log4.
Let R_j be the rank-d_j residual projection orthogonal to the complete original relation columns P_j,tP_j,...,t^(d_j-1)P_j in R^(2d_j), and set

    k_j(z)=(2d_j)^(-1) v_(2d_j)(z^-1)^t R_j v_(2d_j)(z).

Thus0<=k_j<=1 on the unit circle.
All one-variable integrals below use its normalized Haar probability measure mu.
For f in L1(mu), write fhat(h)=integral f(z) z^(-h) dmu and

    W_*(f)=sum_(h in Z,h!=0)|fhat(h)|,

interpreted as an extended nonnegative sum, equivalently the supremum of its finite subsums.
Both signs are included; the constant coefficient is excluded.
The author conclusions proved below are:

1. For every fixed nonconstant continuous real psi on[0,1], W_*(psi composed with k_j) tends to infinity.
2. For fixed finite B,A>=0 and fixed delta>0, the same divergence is uniform over psi with |psi|<=B, Lipschitz constant at most A and oscillation at least delta.
3. In particular it holds for varying psi_j in that bounded Lipschitz class with the ACTUAL single-Haar contact margin

       psi_j(1)-integral psi_j(k_j(z)) dmu(z)>=delta.

The uniform assertion means that for every T>0, all sufficiently large j and every eligible psi have W_*(psi composed with k_j)>T; an empty eligible class causes no exception.
Continuous transforms may already have infinite W_* at a finite j, which is allowed by this precise formulation.
No unbounded or discontinuous transform is included automatically.
No rate in d_j, original integer norm, near-one sequence or unrestricted gap conclusion is claimed.

<a id="scalar-transform-proof-development"></a>
## Complete proof structure

The decisive new step proves that the existing torus kernel has every value in[0,1] as a regular-path limit at one singular point.
Every fixed nonconstant continuous transform then lacks a continuous representative there.
The complete function-level Haar L1 estimate from C172 is combined with uniform continuity before transferring fixed Fourier coefficients; coefficient convergence alone cannot justify composition.
Finally, an elementary finite-mesh compactness argument keeps varying transforms from approaching constants while preserving the finite-frequency order of choices.

<a id="scalar-transform-paid-return"></a>
## 2. Paid full-function return and four-torus conventions

Write U=Acal/Bcal off the common-zero set Z from [C171's phase formula](Yin_C_G0171_v1.md#two-block-torus-phase), and put U=0 on Z.
The exact set is

    Z={u=v=1} union {z^K=1,u=1} union {z^K=1,v=1}.

It has three-torus Haar measure zero.
Off Z, U is continuous and |U|=1.
Keep the accepted inverse orientation

    V(z,u,v)=U(z^-1,u^-1,v^-1),
    Kcal(z,u,v,w)=(1-Re[w V(z,u,v)])/2.                (1)

Let nu be normalized four-torus Haar probability measure, and define

    iota_j(z)=(z,z^(a_j),z^(b_j),z^(c_j)),
    H_j(gamma)=gamma_0+gamma_1 a_j+gamma_2 b_j+gamma_3 c_j.

C172's [complete original-kernel L1 return](Yin_C_G0172_v1.md#moving-cubic-original-l1-return), equation12 before cubic composition, gives

    ||k_j-Kcal composed with iota_j||_(L1(mu))<=epsilon_j ->0,
    epsilon_j=(4L_j-5)/(2d_j)+E_j/2,
    E_j=[1+pi L_j(5+2log c_j)]/c_j.                  (2)

Changing the removable phase value at z=1 has no circle Haar effect.
This bound includes the full cyclic boundary rank, original rank-three removal, missing cyclic mode and finite Dirichlet term.
The normalization is still2d_j throughout; no2c_j or raw-numerator replacement is made.
Both functions in(2) lie in[0,1].

The accepted separated scales give

    (iota_j)_*mu -> nu on every continuous torus test. (3)

Indeed each fixed nonzero torus character has pullback exponent H_j(gamma)!=0 eventually, and continuous tests are uniformly approximated by product-Fejer polynomials.
For every fixed finite set of distinct gamma, their H_j(gamma) are eventually distinct; nonzero gamma give nonzero original frequencies.
These are fixed-test assertions, not uniform estimates over a growing frequency set.

For fixed continuous psi:[0,1]->R, put M=||psi||_infinity and let omega_psi(t) be its uniform modulus of continuity.
For any0<eta<=1 and any[0,1]-valued f,g on a probability space,

    ||psi(f)-psi(g)||_1
       <=omega_psi(eta)+(2M/eta)||f-g||_1.            (4)

Split the domain into |f-g|<=eta and its complement, whose measure is bounded by ||f-g||_1/eta.
First keeping eta fixed and letting j grow in(2), then decreasing eta to zero, proves the needed composition error tends to zero.
For an A-Lipschitz psi, the sharper bound is simply A epsilon_j.
No derivative bound on a merely continuous transform is assumed.

<a id="scalar-transform-four-torus-coefficients"></a>
## 3. Every fixed transformed coefficient and the single Haar mean

Define F_psi=psi(Kcal) on the four-torus.
It is bounded and continuous off the inverse of Z times the w circle.
The singular set cannot be discarded from the one-dimensional pullbacks without paying a valid approximation.
Here is the full regularization argument for an arbitrary continuous psi.

Let g=|Acal|^2+|Bcal|^2, use

    U_rho=2 Acal conjugate(Bcal)/(g+rho), rho>0,

and obtain V_rho and Kcal_rho by the SAME inversions and formula(1).
Both Kcal and Kcal_rho lie in[0,1], Kcal_rho is continuous, and

    |Kcal-Kcal_rho|<=rho/[2(g_inv+rho)],
    g_inv(z,u,v)=g(z^-1,u^-1,v^-1).                  (5)

At a common zero both phases are assigned0, so(5) also holds there.
The same split as(4) gives the continuous majorant

    |F_psi-psi(Kcal_rho)|
       <=omega_psi(eta)+(M/eta)rho/(g_inv+rho).       (6)

For fixed rho and eta, all terms on the right and the regularized function times any fixed character are continuous tests for(3).
The nu-integral of rho/(g_inv+rho) tends to zero with rho, since the zero set has nu-measure zero.
Consequently first pass j to infinity at fixed rho,eta, then rho to zero, and finally eta to zero.
Combining this with(2)--(4) proves, for every fixed gamma in Z^4,

    (psi composed with k_j)hat(H_j(gamma))
                    -> F_psihat(gamma).              (7)

The Fourier coefficient on the right is integral F_psi(z,u,v,w) z^(-gamma_0)u^(-gamma_1)v^(-gamma_2)w^(-gamma_3) dnu.
Thus all phase inversions and signed original frequencies are explicit.
Any finite set of these limits can be used simultaneously; no infinite absolute sum was interchanged with a limit.

For gamma=0, integration in the independent w variable uses |V|=1 outside a null set and gives the exact limiting scalar law

    integral psi(k_j) dmu -> S(psi),
    S(psi)=(1/(2pi))integral_0^(2pi) psi((1-cos theta)/2)dtheta
           =(1/pi)integral_0^1 psi(s)/sqrt(s(1-s)) ds. (8)

There is ONE actual original-circle Haar mean on the left.
The four-torus and its arcsine scalar law are limiting proof devices, not averages substituted at finite j.
The endpoint density is integrable, and boundedness of psi suffices.

<a id="scalar-transform-full-cluster"></a>
## 4. Every scalar value occurs near one singular point

The exact channel quotient in C171 is

    U=(-1/2+H)/(-1/2-H),
    H=-(z-z^-1)+(C(z^K)+C(u)+C(v))/2,
    C(w)=(w+1)/(w-1),                                (9)

where the displayed variables are unit complex numbers avoiding the denominator zeros.
The quantity H is purely imaginary.
Set z0=exp(i pi/K), so z0^K=-1, and put H0=-(z0-z0^-1).
Then C(z0^K)=0.
Fix ANY real h.
For small positive t choose

    u(t)=exp(it),
    T_h(t)=2ih-2H0-C(u(t)),
    v_h(t)=(T_h(t)+1)/(T_h(t)-1).                    (10)

The number T_h(t) is purely imaginary, so its denominator is nonzero and |v_h(t)|=1.
Also v_h(t)!=1, since that equality would imply1=-1.
As t decreases to zero, |C(u(t))| tends to infinity; hence v_h(t) tends to1.
Direct substitution gives C(v_h(t))=T_h(t).
Therefore(z0,u(t),v_h(t)) lies off Z and has H=ih EXACTLY, for every such t.

Use the inverse-oriented four-torus path

    x_h(t)=(z0^-1,u(t)^-1,v_h(t)^-1,1).

It remains in the regular set and tends to the SAME point x_*=(z0^-1,1,1,1), independently of h.
Equations(1),(9)--(10) give the constant path value

    Kcal(x_h(t))=4h^2/(1+4h^2).                       (11)

As h varies, these values fill[0,1).
For the endpoint1, take u=v=exp(it) in(9); then |H| tends to infinity, U tends to-1, and the corresponding inverse-oriented path has Kcal tending to1 at the same x_*.
Thus the complete regular-path cluster set of Kcal at x_* is[0,1]; its opposite inclusion follows from its global range.
This strengthens the two specific path values used for C172's monotone cubic.
It does not rely on any scalar first-harmonic coefficient being nonzero.

If psi is nonconstant and continuous on[0,1], two of these regular paths give different limits of F_psi.
Hence F_psi has NO continuous representative, even after changing values on a nu-null set.
To justify the latter assertion, any proposed continuous representative equals F_psi pointwise on the open regular set: their continuous difference there vanishes almost everywhere, and a nonzero value would persist on a nonempty open set of positive Haar measure.
The incompatible regular-path limits then contradict its continuity at x_*.
No value assigned only on the singular set can repair this contradiction.

<a id="scalar-transform-fixed-divergence"></a>
## 5. From the singular transform to actual nonconstant Wiener divergence

Suppose the four-torus Fourier coefficients of F_psi were absolutely summable.
Their Fourier series would converge uniformly to a continuous function Q with the same coefficients.
The difference F_psi-Q has every coefficient zero, so its convolution with every product-Fejer polynomial is identically zero.
At every regular point, that convolution converges to F_psi-Q by local continuity, boundedness and the approximate-identity tail bound already used in C171.
Thus Q=F_psi on the regular set, contradicting Section4.
This is the elementary Fejer uniqueness argument; no uninspected external harmonic-analysis theorem is needed.
The constant coefficient is finite, so necessarily

    sum_(gamma in Z^4,gamma!=0)|F_psihat(gamma)|=infinity. (12)

Given any T>0, select a FINITE set E of nonzero gamma for which the sum in(12) exceeds T+1.
Keep that E fixed.
Equation(7) and eventual injectivity/nonvanishing of H_j on E give

    liminf_j W_*(psi composed with k_j)
             >=sum_(gamma in E)|F_psihat(gamma)|>T.   (13)

First selecting E and only then increasing j is essential.
No total error is claimed for an infinite collection or for a frequency set selected after j.
Since T was arbitrary, this proves the fixed-transform conclusion.
The coefficients are those of the actual transformed original2d kernel, even when psi is not a polynomial and its Fourier support is infinite.
Both signs remain in W_*; no one-sided normalization or raw-polynomial replacement is introduced.

<a id="scalar-transform-varying-compactness"></a>
## 6. Varying bounded Lipschitz transforms with nonzero amplitude

Fix B,A>=0 and delta>0.
Consider the class of real functions psi on[0,1] with ||psi||_infinity<=B, Lipschitz constant at most A and max psi-min psi>=delta.
Every sequence in the bounded Lipschitz class has a uniformly convergent subsequence.
For completeness, choose a countable dense set of points and repeatedly extract a subsequence on which each point value converges, then take a diagonal subsequence.
The common Lipschitz bound and a finite fine mesh upgrade pointwise Cauchy convergence on that dense set to uniform Cauchy convergence on[0,1].
The uniform limit is still real, bounded by B and A-Lipschitz.
Its oscillation is at least delta because maxima and minima each change by at most the uniform distance.
This is the Arzela--Ascoli compactness principle, with [checked source attribution](#scalar-transform-compactness-attribution); the proof just given supplies the complete local step.
If A=0 or the other bounds make the class empty, the stated uniform conclusion is vacuous.

Suppose uniform divergence failed.
Then some T<infinity, a sequence j_l tending to infinity and eligible psi_l would satisfy

    W_*(psi_l composed with k_(j_l))<=T.              (14)

Extract a uniform limit psi_infinity as above; it is nonconstant.
For every original frequency h the coefficient difference between psi_l(k_(j_l)) and psi_infinity(k_(j_l)) has absolute value at most ||psi_l-psi_infinity||_infinity.
Therefore(7), applied to the FIXED limiting transform, yields

    (psi_l composed with k_(j_l))hat(H_(j_l)(gamma))
                     ->F_(psi_infinity)hat(gamma)    (15)

for every fixed gamma.
Choose a finite E whose limiting absolute coefficient sum is greater than T+1 by(12), then take l large enough for both its coefficient limits and frequency separation.
This contradicts(14).
Hence the divergence is uniform over the entire stated class.
This is qualitative uniformity, not a computed onset or degree-dependent rate.

For any real psi, the actual mean integral psi(k_j)dmu lies between its minimum and maximum on[0,1].
Consequently the supplied contact margin

    psi(1)-integral psi(k_j)dmu>=delta                (16)

implies max psi-min psi>=delta at that SAME j.
Thus every varying bounded A-Lipschitz family with this fixed actual margin is covered by the uniform theorem.
In fact the absolute margin could replace the one-sided margin for this implication.
No finite-j Haar average was exchanged for a different measure.

The limiting Haar statement(8) is also uniform over the bounded A-Lipschitz class.
Otherwise a bad sequence would admit a uniformly convergent subsequence, whose difference in either probability integral is bounded by its uniform distance; applying(8) to its fixed limit gives a contradiction.
This confirms that a persistent contact margin cannot disappear into an unpriced change of averaging law.
It is not needed to turn(16) into oscillation, which already holds exactly.

<a id="scalar-transform-scope-and-inputs"></a>
## 7. Boundaries and complete input roles

This author argument proves that fixed continuous nonconstant scalar transforms cannot bound the nonconstant Fourier absolute sum on the SAME actual bounded-positive-measure Salem sequence.
Allowing the transform to vary cannot avoid it while keeping a uniform finite Lipschitz bound, uniform boundedness and a fixed nonzero amplitude or actual contact-minus-Haar margin.
The result includes nonmonotone transforms and transforms with vanishing first scalar harmonic.
It does not merely repeat the cubic's explicit first-band computation.

A constant transform has W_*=0 and zero contact margin, so excluding collapse to constants is necessary for the uniform assertion.
No claim is made for families with unbounded Lipschitz constants, loss of the amplitude condition, discontinuous transforms or general unbounded endpoint singularities.
The already known log(1+k) falls in the continuous domain; a different unbounded logarithm would require its own integrability and approximation costs.
The normalization by2d, the original irreducible P_j, both signed frequencies and the single original Haar integral are unchanged.
The proof gives neither a numerical divergence rate nor a new mathematical program.

The reference value psi(1) is the scalar contact value used in(16), not an automatically established original-field integer norm or complete conjugate-average income.
This argument does not certify arbitrary transformed values as algebraic integers or replace radial costs at the two off-circle Salem roots.
Every input here has log2<m(P_j)<log4, so this is NOT a near-one counterexample or a refutation of a sufficiently-small-total-measure estimate.
Genuine coefficient/moment correlation, other actual families and mechanisms outside the stated scalar-transform class remain open.
No Claim acceptance, strategy change or execution decision is made by this author record.

| Input | Actual role and limit |
| --- | --- |
| [L402 actual schedule](../ledger/Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule) | Exact original irreducible Salem family, K and separated a,b,c, degree and fixed positive measure; retained MS05/RY26 source boundary. |
| [C158 projection definition](Yin_C_G0158_v1.md#statement) | Original residual rank,2d window, circle range and complete signed Fourier convention; no arithmetic status is assigned to an arbitrary psi. |
| [C171 torus phase](Yin_C_G0171_v1.md#two-block-torus-phase) | Exact channels, quotient(9), equal moduli, singular set and inverse-phase input. |
| [C171 coefficient/Fejer argument](Yin_C_G0171_v1.md#two-block-singular-phase-divergence) | Accepted elementary approximate identity and continuous-representative uniqueness mechanism, extended here by the explicit full scalar cluster proof. |
| [C172 full original L1 return](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Its equation12 BEFORE cubic composition, including every finite rank/missing-mode cost and explicit epsilon_j. |
| [C172 four-torus transfer](Yin_C_G0172_v1.md#moving-cubic-four-torus-limit) | Accepted separated-character convergence, phase orientation and paid continuous regularization; new continuous-psi composition is fully proved above. |
| [R417](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) and [R420](../audits/reviews/Yin_R_G0420_v1.md#moving-cubic-whole-independent-finding) | Separate independent reviews of this author's accepted upstream contributions, not an independent review of the present extension. |
| [C168 contact comparison](Yin_C_G0168_v1.md#statement) | Existing paid original-contact/energy scope only; no implication from its Sobolev energy to the present Wiener conclusion is used. |

The author checks the real and extended-sum domains, unit-circle inverse orientation, exact v_h formula and its regularity, every s in[0,1] at the same singular point, local positive-Haar uniqueness, both approximation parameters and their order, finite-frequency separation, compactness without a rate and the exact actual-Haar amplitude implication.
All source facts are reused through the displayed accepted inputs at their existing statement/proof-inspection limits.
The compactness step has its complete local mesh proof and the exact source attribution below; no new external quantitative input or original-source proof audit is asserted.

<a id="scalar-transform-compactness-attribution"></a>
## Checked classical compactness attribution

Root checked the named Arzela--Ascoli step after reviewing the complete local argument.
The bounded local search found no adequate recorded compactness source; the subsequent primary-author search located Terence Tao, Tao09a, 245B Notes10, posted9 February2009, with the page's noted20 February renumbering.
The exact source is [Corollary14, native anchor arz](https://terrytao.wordpress.com/2009/02/09/245b-notes-10-compactness-in-topological-spaces/#arz) and its immediately following Lipschitz example.
The [retained original HTML](../literature/pdf/Tao09a/compactness-20090209.html#arz) agrees in statement with the primary web text.

The corollary states that an equicontinuous, pointwise bounded sequence from a compact metric space into a finite-dimensional real space has a uniformly convergent subsequence with bounded continuous limit.
Its following example explicitly takes uniformly bounded, uniformly Lipschitz real functions on[0,1].
This matches Section6: the common A supplies equicontinuity, B supplies pointwise boundedness, and[0,1] is compact.
The positive oscillation condition is separately closed under the uniform limit, as proved locally.

Inspection covers the complete corollary statement and the exact example through original HTML formula-alt text, not an audit of the preceding general proof, other notes, comments or remote images.
The source is verified attribution for the locally proved compactness step, not an additional unproved quantitative premise, a priority claim or a proof of the new Fourier theorem.
No mathematical proof repair was supplied by this source check.

## Current assessment
[Selected decision](#decision-current-complete-moving-family-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T17:05 |
| status | open |
| reason | Register the complete fixed and uniformly bounded-Lipschitz scalar-transform obstruction on the actual C171/C172 family, with full original Haar/frequency costs and verified classical compactness attribution. No near-one or arbitrary-transform integer-norm assertion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete scalar-transform statement](#scalar-transform-statement) | Fixed nonconstant continuous transforms, uniform bounded-Lipschitz nonzero-amplitude class, actual contact-minus-Haar consequence and original2d signed-frequency domain. |
| argument | [Complete transformed-kernel proof](#scalar-transform-paid-return) | Entire Sections2--7 and formulas1--16, paid composition/regularization, full singular cluster, finite-frequency return and uniform compactness. |
| dependency | [Actual family](../ledger/Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule) | Actual original irreducible Salem sequence and separated prime scales, positive bounded total measure and fixed source/review limits. |
| dependency | [Original kernel](Yin_C_G0158_v1.md#statement) | Full original residual projection,2d normalization, range and signed Fourier convention only. |
| dependency | [Torus phase](Yin_C_G0171_v1.md#two-block-torus-phase) | Exact channels, common-zero set and equal-modulus quotient. |
| dependency | [Whole-kernel return](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Full original Haar L1 estimate before cubic composition, all finite-rank and missing-mode costs. |
| dependency | [Separated four-torus transfer](Yin_C_G0172_v1.md#moving-cubic-four-torus-limit) | Exact orientation, continuous-test character convergence and accepted approximation mechanism. |
| support | [Compactness attribution](#scalar-transform-compactness-attribution) | Primary Tao09a Corollary14 and following exact example, statement/applicability attribution for a locally complete proof; no new quantitative theorem input. |
| support | [Contact comparison](Yin_C_G0168_v1.md#statement) | Distinct accepted Sobolev/contact scope only; not used to infer Wiener divergence. |

### Decision whole-reviewed-2026-10-19

| Field | Value |
| --- | --- |
| date | 2026-10-18T17:11 |
| status | proved |
| reason | Adopt the complete scalar-transform obstruction through whole independent R430. Fixed nonconstant continuous transforms and the stated uniformly bounded-Lipschitz class have divergent actual nonconstant Wiener sums on the original bounded-positive-measure family. All Haar, phase, finite-frequency and compactness costs are checked; the named compactness attribution is now verified. No near-one, rate or arbitrary transformed-value norm assertion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete scalar-transform statement](#scalar-transform-statement) | Fixed nonconstant continuous transforms, uniform bounded-Lipschitz nonzero-amplitude class, actual contact-minus-Haar consequence and original2d signed-frequency domain. |
| argument | [Complete transformed-kernel proof](#scalar-transform-paid-return) | Entire Sections2--7 and formulas1--16, paid composition/regularization, full singular cluster, finite-frequency return and uniform compactness. |
| dependency | [Actual family](../ledger/Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule) | Actual original irreducible Salem sequence and separated prime scales, positive bounded total measure and fixed source/review limits. |
| dependency | [Original kernel](Yin_C_G0158_v1.md#statement) | Full original residual projection,2d normalization, range and signed Fourier convention only. |
| dependency | [Torus phase](Yin_C_G0171_v1.md#two-block-torus-phase) | Exact channels, common-zero set and equal-modulus quotient. |
| dependency | [Whole-kernel return](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Full original Haar L1 estimate before cubic composition, all finite-rank and missing-mode costs. |
| dependency | [Separated four-torus transfer](Yin_C_G0172_v1.md#moving-cubic-four-torus-limit) | Exact orientation, continuous-test character convergence and accepted approximation mechanism. |
| support | [Compactness attribution](#scalar-transform-compactness-attribution) | Primary Tao09a Corollary14 and following exact example, statement/applicability attribution for a locally complete proof; no new quantitative theorem input. |
| support | [Contact comparison](Yin_C_G0168_v1.md#statement) | Distinct accepted Sobolev/contact scope only; not used to infer Wiener divergence. |
| review | [Whole scalar-transform finding](../audits/reviews/Yin_R_G0430_v1.md#scalar-transform-whole-independent-finding) | Entire exact statement, Sections2--7, all16 formulas, all input roles and initial selected relations, primary compactness attribution and complete boundary; no mathematical repair or computation. |


### Decision current-complete-moving-family-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T01:21 |
| status | proved |
| reason | Select the complete C494 home for exactly the already used L402 family/blocks/original-degree joint-projection interface. Preserve the statement, entire proof, status, authority, all other input and review tuples/scopes. This same-object maintenance supplies no fresh whole or isolated review and does not backdate C494 as an old input. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#scalar-transform-statement) | Fixed nonconstant continuous transforms, uniform bounded-Lipschitz nonzero-amplitude class, actual contact-minus-Haar consequence and original2d signed-frequency domain. |
| argument | [Exact argument](#scalar-transform-paid-return) | Entire Sections2--7 and formulas1--16, paid composition/regularization, full singular cluster, finite-frequency return and uniform compactness. |
| dependency | [Exact dependency](Yin_C_G0494_v1.md#fixed-trace-moving-exponent-schedule) | Actual original irreducible Salem sequence and separated prime scales, positive bounded total measure and fixed source/review limits. |
| dependency | [Exact dependency](Yin_C_G0158_v1.md#statement) | Full original residual projection,2d normalization, range and signed Fourier convention only. |
| dependency | [Exact dependency](Yin_C_G0171_v1.md#two-block-torus-phase) | Exact channels, common-zero set and equal-modulus quotient. |
| dependency | [Exact dependency](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Full original Haar L1 estimate before cubic composition, all finite-rank and missing-mode costs. |
| dependency | [Exact dependency](Yin_C_G0172_v1.md#moving-cubic-four-torus-limit) | Exact orientation, continuous-test character convergence and accepted approximation mechanism. |
| support | [Exact support](#scalar-transform-compactness-attribution) | Primary Tao09a Corollary14 and following exact example, statement/applicability attribution for a locally complete proof; no new quantitative theorem input. |
| support | [Exact support](Yin_C_G0168_v1.md#statement) | Distinct accepted Sobolev/contact scope only; not used to infer Wiener divergence. |
| review | [Exact review](../audits/reviews/Yin_R_G0430_v1.md#scalar-transform-whole-independent-finding) | Entire exact statement, Sections2--7, all16 formulas, all input roles and initial selected relations, primary compactness attribution and complete boundary; no mathematical repair or computation. |

