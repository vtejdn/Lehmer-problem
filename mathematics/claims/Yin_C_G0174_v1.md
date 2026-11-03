---
author: Yin
---
# Narrow contact layers and the order of Fourier limits

Date: 2026-10-18T17:11.
Human author Yin.
Root supplied the boundary-layer question after the fixed continuous-transform result C173.
The angular_envelope_review agent develops the local contact and full Fourier-price analysis below.
This fixed author argument is registered as proof draft and unreviewed; independent review and adoption are separate, and no numerical scan is claimed.

<a id="narrow-contact-question"></a>
## Exact question and bounded reuse

On the SAME actual L402/C171 original Salem family and C158 kernel k_j in the original2d_j window, consider

    psi_tau(s)=max(0,1-(1-s)/tau), 0<tau<=1,
    f_(j,tau)=psi_tau composed with k_j.

Does any choice tau_j->0 retain psi_tau(1)=1 and a positive ACTUAL single-Haar margin while keeping the complete nonconstant Wiener sum bounded?
C173 cannot answer this because the Lipschitz constant1/tau is unbounded.
Almost-everywhere convergence of a shrinking peak to zero supplies no conclusion about its Fourier absolute sum.

The bounded G-line search inspected existing narrow-peak, boundary-layer, Wiener and Salem-independence records.
[C158](Yin_C_G0158_v1.md#argument) and [L321](Yin_C_G0592_v2.md#residual-laurent-square-identity) supply the exact positive factorization of1-k; [C165](Yin_C_G0165_v1.md#off-pair-salem-ratio-proof) supplies multiplicative independence of distinct inverse-pair representatives.
The [C173 fixed-transform statement](Yin_C_G0173_v1.md#scalar-transform-statement) is relevant only with tau fixed; its varying-transform domain is not assumed here.
The earlier effective-support draft is not an adequate home for this distinct local two-limit analysis.

The bounded result below settles the fixed-j limit tau->0 completely, including ALL true maxima, local widths, the constant Haar term, signed Fourier coefficients and their total absolute price.
It also records exactly what this implies, and does not imply, for growing j.
A quantitative joint-limit estimate is not inferred from fixed-input torus equidistribution.

<a id="narrow-contact-development"></a>
## Complete local mechanism

For a fixed original Salem polynomial P of degree d, write r=d/2-1 for the number of nonreal inverse pairs.
The exact contact identity is1-k=|P|^2 B_d/(2d), with B_d positive on the circle.
It makes the d-2 simple unit-circle roots the complete maximum set, with quadratic vanishing of1-k at each root and inverse-pair equal curvature.
The positive-part rescaling then has the compact cap profile(1-x^2)_+.

The full Fourier limit must retain interference among all contact points.
The accepted actual inverse-pair independence permits a fixed-input linear torus average over the Fourier index, but gives no uniform onset as d grows.
The checked classical attribution is Tao's author-hosted2010-03-28 Notes1, Proposition1 and Exercises3,5 on linear and weighted equidistribution; the local proof and its exact fixed-input limits are retained below.
No sampling or peak theorem is being imported from an unidentified snippet.

<a id="narrow-contact-source-interface"></a>
## 1. Exact classical source scope

The new work [Tao10](../literature/pdf/Tao10/equidistribution-20100328.html) is distinct from the already registered Tao09 Fourier lecture and Tao09a compactness lecture.
The source has [native navigation](../literature/contents/Tao10/equidistribution-20100328.html.md).
On2026-10-19 the author directly read the retained original HTML/TeX-alt text and primary online text for Section1 Proposition1, its proof, Exercise3 and Exercise5.
Proposition1 identifies Haar equidistribution by vanishing nontrivial character averages; Exercise5 treats linear torus orbits; Exercise3 states the compactly supported weighted-average variant.
These are the classical qualitative ingredients recognized here.
No solution of the exercises, original historical proof, quantitative onset or later sections were source-audited.
The needed fixed-input derivation is supplied below, including its two-variable test and tail.

The existing [Tao09 original HTML](../literature/pdf/Tao09/fourier-transform-20090406.html#planch) was also directly read at Section2 Theorem21, its torus-density argument and Corollary22.
Corollary22 gives Parseval for probability Haar measure: the squared L2 norm equals the sum of squared Fourier coefficients.
Only its circle instance is used below, also for an absolutely continuous periodic function's derivative via integration by parts.
The arbitrary compact-group proof, general LCA theory and the real-line Plancherel theorem are not new premises or proof-audit claims.
No external sampling or peak-asymptotic theorem is invoked.

<a id="narrow-contact-fixed-statement"></a>
## 2. Fixed-input theorem and exact remaining joint question

Fix one ACTUAL P=P_j of original degree d, and set r=d/2-1>=1.
Keep exactly C158's original coefficient matrix A_rel, Gram G=A_rel^t A_rel, residual projection R and N=2d.
Let

    q(theta)=1-k(exp(i theta)),
    f_tau(theta)=(1-q(theta)/tau)_+,
    epsilon=sqrt(tau),
    W_*(f)=sum_(m in Z,m!=0)|fhat(m)|,
    fhat(m)=(1/(2pi))integral_(-pi)^pi f(theta) exp(-im theta)dtheta.

All circle means use that SAME normalized Haar probability measure.
Choose the r unit-circle root representatives zeta_l=exp(i theta_l) with0<theta_l<pi; their inverses are the remaining unit roots.
Define

    a_l=|P'(zeta_l)|^2 B_d(zeta_l)/(2d)>0,
    b_l=a_l^(-1/2),
    B_d(z)=v_d(z)^* G^(-1)v_d(z),
    g(x)=(1-x^2)_+,
    F(y)=integral_R g(x)exp(-iyx)dx,
    J=integral_0^infinity |F(y)|dy.                   (1)

The following fixed-input conclusions are proved below.
The complete maximum set k=1 is exactly the2r unit-circle roots, with quadratic contact at each and no other maximum point.
For every0<tau<=1 the Fourier coefficients of f_tau are absolutely summable and

    1-integral f_tau dmu>=1/2.                       (2)

As tau decreases to zero while P stays FIXED,

    integral f_tau dmu=(4epsilon/(3pi))sum_(l=1)^r b_l+o_P(epsilon),
    W_*(f_tau) -> V(P)<infinity,                      (3)
    V(P)=(2/pi)integral_0^infinity
           E_(Theta in T^r)|sum_(l=1)^r b_l F(xb_l)cos Theta_l|dx.

Here Theta_l are independent uniform angles in[0,2pi), solely in the limiting proof device.
The explicit bounds are

    2/3<=J<=28/3,
    V(P)>=(2J/(pi sqrt6))sqrt r
             >=[4/(3pi sqrt6)]sqrt r,
    V(P)<=(4J/pi^2)r.                                (4)

In addition V(P)>=1 by the actual contact value and the vanishing mean.
The width data b_l are the ACTUAL original projection curvatures; they are neither dropped nor replaced by uniform constants in formula(3).
The curvature-independent lower bound in(4) follows only after paying their complete Fourier integral.

On the accepted family, r_j tends to infinity, so

    lim_(j->infinity) lim_(tau->0) W_*(f_(j,tau))=infinity. (5)

C173 separately controls tau in every fixed interval[eta,1] with eta>0.
Neither fact by itself settles an ARBITRARY simultaneous sequence tau_j->0.
That joint question remains open here, and no interchange of these limits is asserted.

<a id="narrow-contact-maxima"></a>
## 3. All actual maxima and their widths

The accepted exact Laurent factorization restricts on the circle to

    q(theta)=|P(exp(i theta))|^2 B_d(exp(i theta))/(2d). (6)

The relation columns are independent, so G is positive definite.
Thus B_d(z)>0 for every |z|=1, since v_d(z) is nonzero.
Consequently q=0 if and only if P(z)=0 on that circle.
A genuine irreducible Salem polynomial has exactly d-2 simple unit-circle roots, none equal+/-1; its remaining real pair is off the circle.
This proves the complete asserted maximum set, with no unaccounted phase maximum at1 or-1.

Since P has simple roots, expansion at zeta_l gives

    q(theta_l+x)=a_l x^2+O_P(x^3),
    q'(theta_l+x)=2a_l x+O_P(x^2).                    (7)

All coefficients in the original projection are real, so q is even and the curvature at-theta_l equals a_l.
The function q is a real analytic trigonometric polynomial.
For fixed P choose disjoint neighborhoods of all2r contact angles, small enough that q decreases to and then increases from its unique zero in each neighborhood.
On their compact complement q has a strictly positive minimum.
For all sufficiently small tau, the support of f_tau is therefore exactly2r disjoint short intervals, one at each contact.
Their endpoints relative to the contact are

    x_-= -epsilon b_l+O_P(epsilon^2),
    x_+=  epsilon b_l+O_P(epsilon^2).                 (8)

For example(7) first confines x/epsilon to a compact interval and then q(x)=epsilon^2 gives x/epsilon=+/-b_l+O_P(epsilon).
No neighborhood radius, curvature bound or remainder constant is asserted uniform in P or j.

For all tau in(0,1], the elementary scalar inequality psi_tau(s)<=s on[0,1] gives integral f_tau<=integral k=1/2.
Also f_tau(theta_l)=1, proving the contact part of(2).
The composition is periodic Lipschitz for each fixed positive tau, with weak derivative-q'/tau where q<tau and zero where q>tau.
It therefore has finite L2 derivative and absolutely summable Fourier coefficients by the bound in the next section with epsilon=1.
Thus its contact values are values of its actual absolutely convergent Fourier series; W_*>=1-integral f_tau.
The lower margin is automatic for this family and every tau, not a further arithmetic hypothesis.

<a id="narrow-contact-wiener-model"></a>
## 4. Parabolic caps approximate the ENTIRE Fourier absolute sum

Let the sum below range over all2r contact angles, assigning equal b to inverse pairs, and periodize the compact caps:

    p_epsilon(theta)=sum_contacts sum_(k in Z)
                  g((theta-theta_contact-2pi k)/(epsilon b_contact)). (9)

For small epsilon these supports are disjoint.
For one contact choose a fixed symmetric coordinate neighborhood(-delta_l,delta_l) as in Section3, and use x=(theta-theta_contact)/epsilon.
Define the LOCAL profile, extended by zero outside that neighborhood, by

    h_(epsilon,l)(x)=(1-q(theta_contact+epsilon x)/epsilon^2)_+
                        if |epsilon x|<delta_l,
                     0 otherwise.

Equations(7)--(8) put all its supports in one fixed compact x interval, for fixed P.
For small epsilon the positive-part expression already vanishes near both neighborhood boundaries, so this zero extension creates no value jump or extra weak-derivative term.
They imply uniform convergence to(1-a_l x^2)_+.
Its derivative is-[q'(theta_contact+epsilon x)/epsilon] times the sublevel indicator.
It converges almost everywhere, except at the two limiting boundary points, to-2a_l x times1_(a_l x^2<1), and is uniformly bounded on that compact interval.
Dominated convergence proves convergence in H1(R), meaning convergence of both the function and its first weak derivative in L2.
This argument allows the derivative jumps at the cap edges.

Put e_epsilon=f_(epsilon^2)-p_epsilon on the original circle.
Changing variables separately in the disjoint neighborhoods gives

    ||e_epsilon||_(L2(mu))^2=o_P(epsilon),
    ||e_epsilon'||_(L2(mu))^2=o_P(epsilon^(-1)).       (10)

For any absolutely continuous periodic e with e' in L2, Parseval and finite-sum Cauchy--Schwarz give

    sum_m |ehat(m)|
      <=[sum_m (1+epsilon^2 m^2)^(-1)]^(1/2)
         [||e||_2^2+epsilon^2||e'||_2^2]^(1/2)
      <=[1+pi/epsilon]^(1/2)
         [||e||_2^2+epsilon^2||e'||_2^2]^(1/2).      (11)

The second bound follows by comparing the decreasing positive tail with the integral of1/(1+epsilon^2 x^2) on the positive half-line.
Apply first to finite Fourier sums and increase the finite set; thus no prior absolute summability is assumed in using this estimate.
Equations(10)--(11) prove

    ||f_(epsilon^2)-p_epsilon||_W=o_P(1).             (12)

This is a COMPLETE Wiener-norm approximation, not a coefficientwise or almost-everywhere approximation.
The same local L1 change of variables yields an o_P(epsilon) mean error.
Since integral_R g=4/3 and there are two copies of each b_l, that proves the mean formula in(3).

<a id="narrow-contact-frequency-limit"></a>
## 5. Exact peak transform and fixed-input phase average

Elementary integration gives

    F(y)=4(sin y-y cos y)/y^3 for y!=0,
    F(0)=4/3.                                       (13)

It is real, even and continuous.
The integral definition gives |F(y)|<=4/3, and for y>=1 the displayed formula gives |F(y)|<=8/y^2.
Also for0<=y<=1, cos(yx)>=1/2 on[-1,1], so F(y)>=2/3.
These inequalities prove the two bounds on J in(4), including its finiteness, without a sampled integral or a Fourier-inversion constant.

The exact Fourier coefficient of the periodic model is

    p_epsilonhat(m)=(epsilon/pi)sum_(l=1)^r
                     b_l F(epsilon m b_l)cos(m theta_l). (14)

This formula retains both inverse roots, every curvature and the original Haar factor2pi.
The model is real and even, so the complete nonconstant absolute sum is twice the sum for positive m.

The representatives zeta_l are multiplicatively independent by C165's actual Salem inverse-pair lemma.
Hence for every nonzero integer vector h, exp(i sum_l h_l theta_l)!=1.
The geometric-series formula makes the Cesaro mean of exp(i m sum_l h_l theta_l) tend to zero as the number of indices grows.
Product-Fejer approximation, or the precisely attributed Tao10 criterion, therefore proves Haar equidistribution of(m theta_1,...,m theta_r) modulo2pi for this FIXED P and r.
It supplies no bound for that onset as j increases.

For completeness the exact weighted version needed here can be proved directly.
For any continuous H(x,Theta) on[0,M] times T^r, split[0,M] into finitely many intervals and replace x by a representative on each interval.
Uniform continuity bounds the normalized total error by M times its modulus.
On each interval, the difference of two prefix Cesaro sums gives

    epsilon sum_(m>=1, epsilon m in I) H(x_I,m theta)
                       ->|I| integral_(T^r) H(x_I,Theta)dTheta.

Then refine the partition.
This works for arbitrary real epsilon decreasing to zero, not just reciprocal integers.
It is the qualitative weighted-linear averaging in Tao10 Exercise3, with the joint continuous test treated by this finite partition.

Apply it to H(x,Theta)=|sum_l b_l F(xb_l)cos Theta_l|.
For x>=max_l1/b_l, its upper bound is8(sum_l1/b_l)/x^2.
The same bound controls the epsilon-weighted discrete tail by a constant times1/M for all sufficiently small epsilon, using the integral bound for sum_(m>M/epsilon)m^(-2).
For fixed P this pays both tails uniformly in epsilon; only after that may M increase to infinity.
Consequently(14) gives

    W_*(p_epsilon) ->(2/pi)integral_0^infinity
                     E|sum_l b_l F(xb_l)cos Theta_l|dx. (15)

Together with(12), this proves the complete finite limit(3).
The order is fixed P, fixed finite M and partition, epsilon->0, partition refinement, then M->infinity.
No independent-angle assertion is made about the original finite conjugate average or about a growing-dimensional torus at a fixed Fourier cutoff.

<a id="narrow-contact-rank-price"></a>
## 6. The complete limiting price grows at least as the square root of the contact-pair count

For arbitrary real c_l put X=sum_l c_l cos Theta_l with independent uniform angles.
Direct integration gives

    E X^2=(1/2)sum_l c_l^2,
    E X^4=(3/8)sum_l c_l^4+(3/2)sum_(l<k)c_l^2 c_k^2
                    <=(3/4)(sum_l c_l^2)^2.

Holder applied to |X|^(2/3)|X|^(4/3) gives E X^2<=(E|X|)^(2/3)(E X^4)^(1/3).
Thus, with the zero-vector case separate,

    E|X|>=||c||_2/sqrt6,
    E|X|<=(2/pi)sum_l |c_l|.                         (16)

The upper estimate uses E|cos Theta_l|=2/pi.
This is a complete elementary second/fourth-moment calculation, with no uninspected probabilistic inequality constant.

Use c_l(x)=b_l F(xb_l).
For every x, ||c(x)||_2>=sum_l|c_l(x)|/sqrt r, while change of variables gives integral_0^infinity |c_l(x)|dx=J for EVERY l.
Integrating(16) in(15) proves exactly

    (2J/(pi sqrt6))sqrt r<=V(P)<=(4J/pi^2)r.          (17)

Thus even arbitrarily different fixed-input peak widths cannot make the thin-layer limit uniformly bounded as the number of actual Salem contact pairs increases.
Every width is integrated before the lower bound is made independent of it.
For a single fixed P the limit is nevertheless finite, while the actual Haar mean tends to zero.
This explicitly prevents an inference of Wiener-norm decay from almost-everywhere zero convergence.

<a id="narrow-contact-two-limits"></a>
## 7. What this settles and the precise uncontrolled corridor

Set c_*=4/(3pi sqrt6)>0.
For every fixed j, formulas(3)--(4) give a positive threshold sigma_j, which may be decreased to at most1/j, such that

    0<tau<=sigma_j => W_*(f_(j,tau))>=(c_*/2)sqrt(r_j),
                     integral f_(j,tau)dmu<=1/j.      (18)

No effective, degree-only or uniform lower bound for sigma_j has been obtained.
The additional mean requirement follows from the same fixed-input limit(3).
Consequently every diagonal chosen below these actual fixed-input thresholds has Wiener divergence and actual contact margin tending to1.
This includes existence of arbitrarily thin diagonals with divergence, not a claim about every diagonal.

For each eta>0, the class {psi_tau: eta<=tau<=1} has sup norm1, oscillation1 and Lipschitz constant at most1/eta.
The accepted C173 uniform theorem therefore gives divergence uniformly over that fixed interval as j grows.
Combining the two proved ends does NOT cover the moving corridor

    sigma_j<tau_j->0.                                (19)

In particular both iterated divergence statements can hold while a diagonal remains uncontrolled.
No bounded-Wiener diagonal has been constructed, and no theorem excluding every such diagonal is proved here.

A genuinely decisive next estimate would have to control that corridor using the ACTUAL minimum separation and curvatures of the unit roots, the scaled profile errors in(10), and quantitative character averages for the actual angle vector at Fourier scale comparable to tau^(-1/2) times the curvature widths.
Multiplicative independence supplies no such uniform rate by itself.
The alternate four-torus C172 approximation pays a composition error of order epsilon_j/tau, which also cannot be discarded for an arbitrary shrinking tau.
A new scan of widths or degrees is not selected by this fixed-input theorem.

All polynomials in this result remain the original actual P_j, with d_j and2d_j unchanged and log2<m(P_j)<log4.
The independent-angle integral is a fixed-input Fourier-index limit, not a replacement for the original Haar mean or an arithmetic conjugate law.
The clipped real scalar transform is not asserted to be an integral Laurent auxiliary or to have an original-field resultant.
No near-one counterexample, unrestricted Mahler conclusion, numerical rate or changed Task/strategy/execution decision follows.

<a id="narrow-contact-fixed-inputs"></a>
## 8. Complete input and author boundaries

The present author contributed the upstream C171/C172/C173 arguments.
Their accepted independent R417/R420/R430 findings are reused at their actual scopes, not independently re-reviewed by this author.
Root supplied the new boundary-layer question but no contact, cap, Fourier-limit or moment proof step here.

| Input | Actual role and limit |
| --- | --- |
| [L402 actual family](../ledger/Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule) | The SAME actual irreducible Salem P_j, original d_j and separated parameter schedule, fixed positive total-measure range and accepted source limits. |
| [C158 original projection](Yin_C_G0158_v1.md#statement) and [exact factorization](Yin_C_G0158_v1.md#argument) | Rank-d residual in2d coordinates, actual q=abs(P)^2 B_d/(2d), circle range/mean and complete signed Fourier convention. |
| [L321 Laurent identity](Yin_C_G0592_v2.md#residual-laurent-square-identity) | Exact original Gram inverse and polynomial factorization, retaining all original coefficients; no asymptotic Toeplitz inverse is inserted. |
| [C165 Salem independence](Yin_C_G0165_v1.md#off-pair-salem-ratio-proof) | Actual distinct inverse-pair representatives are multiplicatively independent; no normal-trace, full Galois group or growing-rank Diophantine rate is required or inferred. |
| [C173 fixed/varying theorem](Yin_C_G0173_v1.md#scalar-transform-statement), [accepted decision](Yin_C_G0173_v1.md#decision-whole-reviewed-2026-10-19) | Only tau in a fixed interval[eta,1] uses its bounded-Lipschitz class; no claim that1/tau_j remains bounded. |
| [C172 paid L1 return](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Comparison explaining the epsilon_j/tau composition loss; not a source of an unpriced joint limit. |
| [Tao10 selected source inspection](#narrow-contact-source-interface) | Retained original HTML Section1 Proposition1 and Exercises3,5, qualitative fixed-torus averaging attribution; the complete needed fixed-input derivation is supplied here with all tails. |
| [Tao09 selected Parseval scope](#narrow-contact-source-interface) | Directly read retained Section2 Theorem21/Corollary22, probability Haar circle normalization only; no new general LCA or original-source proof claim. |
| [R417](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding), [R420](../audits/reviews/Yin_R_G0420_v1.md#moving-cubic-whole-independent-finding), [R430](../audits/reviews/Yin_R_G0430_v1.md#scalar-transform-whole-independent-finding) | Independent upstream findings for this author's earlier contributions, not a review of the present narrow-layer argument. |

The author checked the full maximum set, real off-circle pair exclusion, positive original Gram factor, simple-root curvature and inverse equality, all cap support endpoints, H1 errors and their epsilon weights, both Fourier signs and2pi factors, the complete discrete and integral tails, fixed-rank independence, second/fourth-moment constants and every limit order.
The scalar margin is proved for every actual input/tau before the asymptotics.
The only unresolved mathematical conclusion is the stated arbitrary-diagonal corridor; the fixed-input theorem and both controlled ends do not require its resolution.

## Current assessment
[Selected decision](#decision-current-complete-moving-family-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T17:26 |
| status | open |
| reason | Register the complete reusable fixed-input narrow-layer theorem and its full author proof, preserving every original contact, curvature, Haar, Fourier, fixed-torus and tail cost. The integrated primary-source attribution and actual source-inspection limits are retained. No uniform arbitrary-diagonal theorem, numerical rate, near-one counterexample or acceptance is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete fixed-input theorem](#narrow-contact-fixed-statement) | Actual original P_j and2d_j kernel; every maximum, automatic contact margin, fixed-input mean and complete Wiener limit, explicit sqrt(r) lower/r upper bounds, controlled ends and unresolved arbitrary diagonal. |
| argument | [Complete contact-to-Fourier proof](#narrow-contact-maxima) | Entire Sections3--7, formulas6--19, all local zero extensions, H1-to-Wiener errors, actual phase interference, fixed-input weighted torus averaging and every limit-order qualification. |
| dependency | [Actual Salem family](../ledger/Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule) | Exact original irreducible P_j, degree/window and fixed positive total measure, with accepted MS05/RY26 source boundaries. |
| dependency | [Original projection definition](Yin_C_G0158_v1.md#statement) | Actual coefficient matrix, residual projection, rank,2d normalization, circle mean/range and complete signed Fourier convention. |
| dependency | [Exact original factorization](../ledger/Yin_L_G0321_v1.md#residual-laurent-square-identity) | q=abs(P)^2 B_d/(2d) on the circle, with positive actual Gram inverse and no missing conjugate or replacement polynomial. |
| dependency | [Actual inverse-pair independence](Yin_C_G0165_v1.md#off-pair-salem-ratio-proof) | Multiplicative independence of the selected actual unit-circle representatives; no quantitative growing-rank torus onset. |
| dependency | [Accepted bounded-Lipschitz theorem](Yin_C_G0173_v1.md#scalar-transform-statement) | Only the tau in fixed[eta,1] comparison; it is not applied to a class with unbounded1/tau. |
| dependency | [Classical source interfaces](#narrow-contact-source-interface) | Exact retained Tao09 Section2 Theorem21/Corollary22 probability-Haar circle Parseval and Tao10 Section1 Proposition1/Exercises3,5 qualitative averaging, with complete local derivations and recorded proof-inspection limits. |
| support | [Paid phase return comparison](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | The epsilon_j/tau composition loss only; no unpriced approximation for the arbitrary-diagonal corridor. |
| support | [Complete input roles](#narrow-contact-fixed-inputs) | All nine actual dependency/source/comparison rows, author relationships and no-computation boundary. |
| support | [C171 independent upstream review](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) | Accepted upstream scope, not a new independent review by its author or of this extension. |
| support | [C172 independent upstream review](../audits/reviews/Yin_R_G0420_v1.md#moving-cubic-whole-independent-finding) | Accepted upstream scope, not prospective review of the present narrow-layer proof. |
| support | [C173 independent upstream review](../audits/reviews/Yin_R_G0430_v1.md#scalar-transform-whole-independent-finding) | Accepted fixed/equi-Lipschitz scope and compactness attribution, with its actual stated limits. |

### Decision whole-reviewed-2026-10-19

| Field | Value |
| --- | --- |
| date | 2026-10-18T17:29 |
| status | proved |
| reason | Adopt the complete fixed-input narrow-contact theorem through whole independent R434. All actual maxima, curvatures, full Wiener approximation, phase interference, both Fourier signs, weighted torus tails and square-root contact-count price are checked. The actual contact margin is at least one half; the arbitrary simultaneous shrinking-layer corridor remains unresolved. No mathematical repair, new numerical evidence or uniform Mahler conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete fixed-input theorem](#narrow-contact-fixed-statement) | Actual original P_j and2d_j kernel; every maximum, automatic contact margin, fixed-input mean and complete Wiener limit, explicit sqrt(r) lower/r upper bounds, controlled ends and unresolved arbitrary diagonal. |
| argument | [Complete contact-to-Fourier proof](#narrow-contact-maxima) | Entire Sections3--7, formulas6--19, all local zero extensions, H1-to-Wiener errors, actual phase interference, fixed-input weighted torus averaging and every limit-order qualification. |
| dependency | [Actual Salem family](../ledger/Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule) | Exact original irreducible P_j, degree/window and fixed positive total measure, with accepted MS05/RY26 source boundaries. |
| dependency | [Original projection definition](Yin_C_G0158_v1.md#statement) | Actual coefficient matrix, residual projection, rank,2d normalization, circle mean/range and complete signed Fourier convention. |
| dependency | [Exact original factorization](../ledger/Yin_L_G0321_v1.md#residual-laurent-square-identity) | q=abs(P)^2 B_d/(2d) on the circle, with positive actual Gram inverse and no missing conjugate or replacement polynomial. |
| dependency | [Actual inverse-pair independence](Yin_C_G0165_v1.md#off-pair-salem-ratio-proof) | Multiplicative independence of the selected actual unit-circle representatives; no quantitative growing-rank torus onset. |
| dependency | [Accepted bounded-Lipschitz theorem](Yin_C_G0173_v1.md#scalar-transform-statement) | Only the tau in fixed[eta,1] comparison; it is not applied to a class with unbounded1/tau. |
| dependency | [Classical source interfaces](#narrow-contact-source-interface) | Exact retained Tao09 Section2 Theorem21/Corollary22 probability-Haar circle Parseval and Tao10 Section1 Proposition1/Exercises3,5 qualitative averaging, with complete local derivations and recorded proof-inspection limits. |
| support | [Paid phase return comparison](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | The epsilon_j/tau composition loss only; no unpriced approximation for the arbitrary-diagonal corridor. |
| support | [Complete input roles](#narrow-contact-fixed-inputs) | All nine actual dependency/source/comparison rows, author relationships and no-computation boundary. |
| support | [C171 independent upstream review](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) | Accepted upstream scope, not a new independent review by its author or of this extension. |
| support | [C172 independent upstream review](../audits/reviews/Yin_R_G0420_v1.md#moving-cubic-whole-independent-finding) | Accepted upstream scope, not prospective review of the present narrow-layer proof. |
| support | [C173 independent upstream review](../audits/reviews/Yin_R_G0430_v1.md#scalar-transform-whole-independent-finding) | Accepted fixed/equi-Lipschitz scope and compactness attribution, with its actual stated limits. |
| review | [Whole narrow-contact finding](../audits/reviews/Yin_R_G0434_v1.md#narrow-contact-whole-independent-finding) | Entire fixed statement and argument, Sections1--8, all19 formulas, nine input rows, initial selected relations and exact primary-source scope; independent noncontributor review without mathematical repair. |

### Decision current-complete-moving-family-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T01:21 |
| status | proved |
| reason | Select the complete C494 home for exactly the already used L402 family/blocks/original-degree joint-projection interface. Preserve the statement, entire proof, status, authority, all other input and review tuples/scopes. This same-object maintenance supplies no fresh whole or isolated review and does not backdate C494 as an old input. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#narrow-contact-fixed-statement) | Actual original P_j and2d_j kernel; every maximum, automatic contact margin, fixed-input mean and complete Wiener limit, explicit sqrt(r) lower/r upper bounds, controlled ends and unresolved arbitrary diagonal. |
| argument | [Exact argument](#narrow-contact-maxima) | Entire Sections3--7, formulas6--19, all local zero extensions, H1-to-Wiener errors, actual phase interference, fixed-input weighted torus averaging and every limit-order qualification. |
| dependency | [Exact dependency](Yin_C_G0494_v1.md#fixed-trace-moving-exponent-schedule) | Exact original irreducible P_j, degree/window and fixed positive total measure, with accepted MS05/RY26 source boundaries. |
| dependency | [Exact dependency](Yin_C_G0158_v1.md#statement) | Actual coefficient matrix, residual projection, rank,2d normalization, circle mean/range and complete signed Fourier convention. |
| dependency | [Exact dependency](Yin_C_G0592_v2.md#residual-laurent-square-identity) | q=abs(P)^2 B_d/(2d) on the circle, with positive actual Gram inverse and no missing conjugate or replacement polynomial. |
| dependency | [Exact dependency](Yin_C_G0165_v1.md#off-pair-salem-ratio-proof) | Multiplicative independence of the selected actual unit-circle representatives; no quantitative growing-rank torus onset. |
| dependency | [Exact dependency](Yin_C_G0173_v1.md#scalar-transform-statement) | Only the tau in fixed[eta,1] comparison; it is not applied to a class with unbounded1/tau. |
| dependency | [Exact dependency](#narrow-contact-source-interface) | Exact retained Tao09 Section2 Theorem21/Corollary22 probability-Haar circle Parseval and Tao10 Section1 Proposition1/Exercises3,5 qualitative averaging, with complete local derivations and recorded proof-inspection limits. |
| support | [Exact support](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | The epsilon_j/tau composition loss only; no unpriced approximation for the arbitrary-diagonal corridor. |
| support | [Exact support](#narrow-contact-fixed-inputs) | All nine actual dependency/source/comparison rows, author relationships and no-computation boundary. |
| support | [Exact support](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) | Accepted upstream scope, not a new independent review by its author or of this extension. |
| support | [Exact support](../audits/reviews/Yin_R_G0420_v1.md#moving-cubic-whole-independent-finding) | Accepted upstream scope, not prospective review of the present narrow-layer proof. |
| support | [Exact support](../audits/reviews/Yin_R_G0430_v1.md#scalar-transform-whole-independent-finding) | Accepted fixed/equi-Lipschitz scope and compactness attribution, with its actual stated limits. |
| review | [Exact review](../audits/reviews/Yin_R_G0434_v1.md#narrow-contact-whole-independent-finding) | Entire fixed statement and argument, Sections1--8, all19 formulas, nine input rows, initial selected relations and exact primary-source scope; independent noncontributor review without mathematical repair. |
