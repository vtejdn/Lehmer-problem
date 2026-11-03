---
author: Yin
---
# Cubic Fourier expense on the moving-prime Salem family

Date: 2026-10-18T16:12.
Human author Yin.
Root supplied the proposed bounded-variation and discrete-Fejer transfer from the accepted C171 cyclic projection to the actual C158 cubic, including its torus-discontinuity mechanism.
The angular_envelope_review agent checks and develops the complete estimates, phase orientation and original-kernel return below.
Root and angular_envelope_review are contributors; neither can independently review the whole new argument.
This fixed author proof is initially registered as proof draft and unreviewed, with no numerical execution or adoption.

<a id="moving-cubic-question"></a>
## Exact changed question and reuse

For the SAME actual moving-prime Salem polynomials in [C171](Yin_C_G0171_v1.md#two-block-torus-statement), does the nonconstant Wiener norm of the original [C158 cubic](Yin_C_G0158_v1.md#statement) tend to infinity?
C171 proves this for the linear coherence and hence for the full logarithm through C158, but does not already prove it for the fixed cubic.
The new step must transfer the full finite kernel in Haar L1 before polynomial composition; individual coefficient convergence alone is insufficient.
The original d, window2d and exact removal of(x-1)^3 remain fixed by the same [L402 family](../ledger/Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule), with log2<m(P_j)<log4.
No near-one conclusion, rate in the original degree or numerical certificate is proposed.

The actual C158/C171 definitions and cyclic formulas, C171's complete initial/accepted declarations, and [L264's exact Blaschke derivative identity](../ledger/Yin_L_G0264_v1.md#exact-blaschke-two-moment-budget) were reread.
L264 already retains the primary GMR18 attribution for the Poisson derivative and its elementary complete derivation; no new source theorem or original-source proof audit is needed here.
Existing D38 concerns effective-support/small-measure controls and is not an adequate home for this distinct fixed-family cubic proof.
The present author contributed upstream C171; its separately accepted [R417](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) is reused rather than reclassified as an independent self-review.

With C171's shift S_c e_i=e_(i+1), the positive z^c cross term interpolates U_j(z^-1), not U_j(z).
The eventual four-torus target must therefore retain the conjugated orientation

    Kcal(z,u,v,w)=(1-Re[w U(z^-1,u^-1,v^-1)])/2.

This convention does not affect the w=1 discontinuity test, but it fixes every selected Fourier coefficient sign.
The complete bound must also pay the removed omega=1 sample, the finite Dirichlet-kernel term, the O(L) cyclic boundary rank and the original rank-three correction.

<a id="moving-cubic-statement"></a>
## 1. Exact original inputs and author conclusion

Use precisely C171/L402's fixed K and separated prime sequence a_j,b_j,c_j, with

    L_j=K+a_j+b_j+2, d_j=c_j+L_j-3, N_j=2d_j,
    Q_j=(t-1)^3 P_j=A_j+t^(c_j)B_j.

The original P_j is the actual monic irreducible Salem polynomial, of trace -1, with log2<m(P_j)<log4.
Let R_j be the orthogonal residual projection for ALL d_j coefficient columns P_j,tP_j,...,t^(d_j-1)P_j in R^(2d_j), and define the exact C158 functions

    k_j(z)=(2d_j)^(-1)v_(2d_j)(z^-1)^t R_j v_(2d_j)(z),
    Phi(s)=log2-(1-s)/2-(1-s)^2/8-(1-s)^3/24,
    G_(3,j)(z)=Phi(k_j(z)).                              (1)

Every Fourier coefficient uses normalized unit-circle Haar measure.
The author conclusion proved below is

    sum_(h in Z, h!=0)|Ghat_(3,j)(h)| -> infinity.        (2)

The sum retains both signed nonzero frequencies and is finite for each j, because G_(3,j) has Laurent degree at most3(2d_j-1).
This is the SAME actual cubic and original polynomial as C158, without a changed polynomial degree, scalar, spectral cutoff or normalization.
The proof supplies no numerical rate, small-total-measure counterexample or new unrestricted gap conclusion.

<a id="moving-cubic-phase-variation"></a>
## 2. The actual phase extends across the common circle root with controlled variation

Write L,a,b,c for one member and let S_c be C171's shift.
In this section U_j(z)=A_j(z)/B_j(z) denotes its smooth extension on the circle after cancellation, including z=1.
It is distinct from the sampled torus phase of C171, whose value at the common-zero point was assigned0.
The latter assignment was appropriate for the rank-deficient cyclic matrix and will be paid explicitly below.

The exact A,B expressions give A+B=-z R_0, where R_0=(z^K-1)(z^a-1)(z^b-1).
Their constant coefficients are-1 and1, respectively, so zero is not a common root.
Every other common root therefore lies on the unit circle.
C171's common-zero calculation and pairwise coprimality of K,a,b show that the only such root is1.
L402's exact order-two values are

    [A/(z-1)^2](1)=Ka+Kb+ab,
    [B/(z-1)^2](1)=-(Ka+Kb+ab).

They are nonzero, so the full greatest common divisor is precisely(z-1)^2, up to a nonzero scalar.
Thus U_j is a rational function with no zero or pole on the circle, has modulus1 everywhere there, and U_j(1)=-1.

For the degree-L reciprocal-conjugate operation F^*(z)=z^L conjugate(F(1/conjugate(z))), the real-coefficient formulas give B=-A^*.
Indeed R_0 is anti-reciprocal, the corresponding three-term S is reciprocal, and the factors(z^2-1),z have exactly the degrees displayed in L402.
After removing the reciprocal factor(z-1)^2, put m=L-2 and A_0=A/(z-1)^2.
Then B/(z-1)^2=-A_0^*, now with degree m, and A_0 has nonzero constant term and no unit-circle root.
Factoring A_0, with roots rho_1,...,rho_m counted with multiplicity, gives

    U_j(z)=lambda product_(l=1)^m (z-rho_l)/(1-conjugate(rho_l)z),
    |lambda|=1.                                         (3)

This is an exact rational identity, not a claim that every rho_l lies inside the unit disk.
For a single factor on z=exp(it), direct differentiation gives

    d/dt arg[(z-rho)/(1-conjugate(rho)z)]
                         =(1-|rho|^2)/|exp(it)-rho|^2.

For |rho|<1 this is the Poisson kernel, whose integral is2pi by its geometric series.
For |rho|>1 its absolute value is the Poisson kernel for1/conjugate(rho), again with integral2pi.
This is the elementary identity already attributed and proved in L264; arbitrary proximity to the unit circle changes no integral.
Taking the derivative of the product in(3) and using that every factor has modulus1 yields the UNNORMALIZED total variation bound

    V_j:=integral_(-pi)^pi |d/dt U_j(exp(it))| dt
                   <=2pi(L-2)<=4pi L.                  (4)

Inversion z to z^-1 leaves this bound unchanged.
Every function at a finite j is smooth; the estimate is uniform in the root-to-circle distances, not a uniform derivative-supremum estimate.

<a id="moving-cubic-discrete-fejer"></a>
## 3. Complete discrete Fejer error, including the missing mode

For a smooth periodic complex function f define V(f)=integral_(-pi)^pi |f'(t)|dt.
Let theta_l=2pi l/c and let

    F_c(t)=(1/c)|sum_(r=0)^(c-1) exp(irt)|^2,
    I_c f(theta)=(1/c)sum_(l=0)^(c-1) f(theta_l)F_c(theta-theta_l).

The kernel is nonnegative and has normalized Haar integral1.
Its trigonometric frequencies lie between-(c-1) and c-1, so grid orthogonality proves

    (1/c)sum_l F_c(theta-theta_l)=1.                    (5)

For |t|<=pi, the fundamental theorem of calculus bounds |f(theta_l+t)-f(theta_l)| by the variation on the oriented arc of length |t|.
Except at irrelevant endpoints, any point of the circle belongs to at most c|t|/(2pi)+1 of these equally spaced arcs.
Summing the arc integrals gives

    (1/c)sum_l |f(theta_l+t)-f(theta_l)|
                       <=V(f)(|t|/(2pi)+1/c).           (6)

This includes arcs crossing the chosen angle origin and either sign of t.
No pointwise derivative bound has been substituted for the variation.
By positivity, (5), integration and the change of variable t=theta-theta_l,

    ||I_c f-f||_(L1(Haar))
       <=V(f)[1/c+(1/(2pi)) integral |t|F_c(t)dt/(2pi)].

For0<|t|<=pi the geometric sum and sin(|t|/2)>=|t|/pi give

    F_c(t)<=min(c,pi^2/(c t^2)).

Splitting the positive half of the Haar integral at pi/c proves

    integral |t|F_c(t)dt/(2pi)<=pi(1/2+log c)/c,
    ||I_c f-f||_1<=V(f)(5/4+(log c)/2)/c.               (7)

All c in the actual schedule are greater than1.

Now put f_j(exp(it))=U_j(exp(-it)).
Let q_j be the same discrete interpolant except that the sample at theta_0=0 is0 instead of f_j(1)=-1.
Equivalently, in C171's sampling orientation,

    q_j(z)=(1/c)sum_(omega^c=1) U(omega,omega^a,omega^b)F_c(arg(z omega)),

where the torus U is assigned0 at its common-zero set.
This is a trigonometric polynomial of degree at most c-1.
By (5), |q_j(z)|<=1 for every circle point.
The difference from I_c f_j is exactly one sample times F_c/c, so its Haar L1 norm is1/c.
Using (4)--(7) gives the convenient explicit estimate

    ||q_j-U_j(z^-1)||_1<=E_j,
    E_j=[1+pi L_j(5+2log c_j)]/c_j ->0.                (8)

Indeed c_j>(L_j+1)^2 and log x/x decreases for x>e, so L_j log(c_j)/c_j<=2log(L_j)/L_j for all sufficiently large j.
All other terms in(8) also tend to zero.
This is an error estimate for the ACTUAL moving rational functions, not just for a fixed phase while the interpolation degree grows.

<a id="moving-cubic-original-l1-return"></a>
## 4. Haar L1 return from the cyclic proof device to the original kernel

Let Pi_Q be C171's raw relation projection and Pi_V its embedded cyclic range projection, and let Pi_P=I-R_j be the original full P_j relation projection.
C171 gives ||Pi_Q-Pi_V||_trace<=3L-6.
The same-window original-factor correction has rank3, and therefore

    ||Pi_P-Pi_V||_trace<=3L-3.                          (9)

For any self-adjoint H, |v^*Hv|<=v^*|H|v.
Haar integration of v_N(z)v_N(z)^* is I_N, so

    integral |v_N(z)^*H v_N(z)| dHaar<=trace|H|.

Define k_V=1-(2d)^(-1)v_(2d)^*Pi_V v_(2d).
Both k_j and k_V take values in[0,1], since both residual matrices are orthogonal projections in the SAME2d coordinates.
Equation(9) gives

    ||k_j-k_V||_1<=(3L-3)/(2d).                        (10)

C171's exact block formula, with the phase orientation fixed above, gives

    v_(2d)^*Pi_V v_(2d)
       =c-|sum_(r=0)^(c-1)z^r|^2/c+c Re[z^c q_j(z)].

Put K_q=(1-Re[z^c q_j(z)])/2, which also belongs to[0,1].
Then

    k_V-K_q=((d-c)/(2d))(1+Re[z^c q_j(z)])+F_c(arg z)/(2d)>=0.

Since q_j has degree at most c-1, z^c q_j has no constant coefficient.
Haar integration therefore yields the exact finite correction

    ||k_V-K_q||_1=(d-c+1)/(2d)=(L-2)/(2d).             (11)

In particular the Dirichlet/Fejer term and the missing cyclic zero mode were not dropped pointwise.
Combining (8), (10) and (11), and putting

    K_j^phase(z)=(1-Re[z^c U_j(z^-1)])/2,
    epsilon_j=(4L_j-5)/(2d_j)+E_j/2,

proves

    ||k_j-K_j^phase||_1<=epsilon_j ->0.                (12)

All original normalization is by2d_j, not by2c_j or the raw numerator degree.
The actual phase kernel also belongs to[0,1].
On this entire interval

    1/2<=Phi'(s)=1/2+(1-s)/4+(1-s)^2/8<=7/8.

Thus the actual cubic obeys

    ||G_(3,j)-Phi(K_j^phase)||_1<=(7/8)epsilon_j ->0.   (13)

This step pays a full-function error before composing, which coefficientwise convergence of k_j alone would not justify.

<a id="moving-cubic-four-torus-limit"></a>
## 5. Exact four-torus Fourier coefficient limits

Let U(z,u,v) be the bounded C171 torus phase and set

    V(z,u,v)=U(z^-1,u^-1,v^-1),
    Kcal(z,u,v,w)=(1-Re[w V(z,u,v)])/2,
    Fcal=Phi(Kcal).                                    (14)

The value U=0 on C171's measure-zero common-zero set is retained.
Hence Kcal lies in[0,1] and Fcal is bounded everywhere.
The actual phase pullback equals K_j^phase almost everywhere on the one-dimensional circle: the only actual removable common zero is z=1, which has Haar measure zero.

For any fixed gamma in Z^4, put

    H_j(gamma)=gamma_0+gamma_1 a_j+gamma_2 b_j+gamma_3 c_j.

The pushforward of circle Haar measure by(z,z^a,z^b,z^c) has character integral0 unless H_j(gamma)=0.
The separated scales make this integer nonzero eventually for every nonzero gamma, starting with its highest nonzero scale.
C171's elementary product-Fejer approximation therefore proves convergence to four-torus Haar measure for all continuous tests.
For every fixed finite set of distinct gamma, the numbers H_j(gamma) are eventually distinct, and nonzero gamma give nonzero original frequencies.

For completeness the singular phase is handled by the SAME paid regularization as C171, now composed with Phi.
Let g=|Acal|^2+|Bcal|^2 and U_delta=2 Acal conjugate(Bcal)/(g+delta).
The inequality |U_delta|<=1 keeps the corresponding Kcal_delta in[0,1].
It is continuous, as is Fcal_delta=Phi(Kcal_delta), and

    |Fcal-Fcal_delta|
          <=(7/16) delta/(g(z^-1,u^-1,v^-1)+delta).

This holds also on the common-zero set because both definitions use U=U_delta=0 there.
For each fixed delta the right side is a continuous bounded test for the pushforward measures.
Its Haar integral tends to zero as delta decreases to zero, since the common-zero set has Haar measure zero.
First passing j to infinity at fixed delta and then decreasing delta to zero proves convergence for Fcal times every fixed character.
Together with (13), this gives

    Ghat_(3,j)(H_j(gamma)) -> Fcalhat(gamma)
                         for every fixed gamma in Z^4. (15)

This statement concerns the ACTUAL original cubic coefficients.
No limit interchange for an infinite absolute coefficient sum is used.

<a id="moving-cubic-first-band-divergence"></a>
## 6. A nonzero first harmonic retains the singular phase

The scalar cubic does not cancel the phase in this limit.
Outside the measure-zero exceptional set, |V|=1.
Writing C=Re(wV), direct expansion of the fixed cubic gives

    Phi((1-C)/2)=log2-55/192-(21/64)C-(3/64)C^2-C^3/192.

Therefore, almost everywhere on the four-torus,

    Fcal=log2-119/384
       -(85/512)[wV+w^-1 conjugate(V)]
       -(3/256)[w^2 V^2+w^-2 conjugate(V)^2]
       -(1/1536)[w^3 V^3+w^-3 conjugate(V)^3].           (16)

In particular the first positive w coefficient is exactly-(85/512)V, and for eta in Z^3,

    Fcalhat(eta,1)=-(85/512) Uhat(-eta).

Using (15) with gamma=(eta,1) yields the explicit original first-band limit

    Ghat_(3,j)(c_j+eta_0+eta_1 a_j+eta_2 b_j)
                         ->-(85/512) Uhat(-eta).        (17)

These selected frequencies are positive for all sufficiently large j and are pairwise distinct for every fixed finite set of eta.
They lie inside the actual cubic support since they equal c_j+O(b_j), whereas3(2d_j-1)>c_j+O(b_j) eventually.
The rational constant85/512 is nonzero; no lower bound on a cubic Wiener norm is inferred merely from linear coherence growth.

C171 proves sum_(eta in Z^3)|Uhat(eta)|=infinity through the essential discontinuity of its phase and elementary Fejer uniqueness.
For any finite set E subset Z^3, formula(17) and nonnegative absolute values give

    liminf_j sum_(h!=0)|Ghat_(3,j)(h)|
                   >=(85/512)sum_(eta in E)|Uhat(-eta)|.

The right side can be made arbitrarily large by a finite choice of E, proving(2).
All selected original frequencies are nonzero even when eta=0.

The direct discontinuity check proposed by root gives the same conclusion about the limiting function.
At z_0=exp(i pi/K),w=1, the regular path u=v=exp(it) has V tending to-1 and Kcal tending to1.
On the path u=exp(it),v=exp(-it), inversion conjugates C171's finite phase value, leaving its real part unchanged, and

    Kcal ->16sin^2(pi/K)/(1+16sin^2(pi/K))<1.

The derivative bound Phi'>=1/2 makes the two Fcal limits distinct.
Thus Fcal has no continuous representative; this is consistent with its explicit unsummable first w band in(16).
No value assigned solely on the singular set can change either conclusion.

<a id="moving-cubic-scope-and-inputs"></a>
## 7. Exact scope and input roles

The actual fixed-degree-three polynomial certificate has unbounded total nonconstant Fourier expense on a genuinely irreducible Salem family with bounded total logarithmic Mahler measure.
Its scalar degree remains three while its expanded original frequency support grows with d_j.
The conclusion strengthens the accepted C171 linear-coherence control, rather than applying an invalid converse from the full logarithm to its cubic truncation.
C158's rational nonconstant coefficients, degree3(2d_j-1), original values log2 and Haar upper bound remain unchanged.
No resultant or algebraic norm is assigned to the real constant log2.

The total measures stay in(log2,log4), so sufficiently-small-total-measure uniform bounds and the unrestricted Lehmer-gap Task remain unresolved.
No quantitative growth rate, optimized constant, numerical sample, new source acquisition or wider-family generalization is asserted.
Root and this author contributed the new transfer, so any whole independent review must be separately organized with a noncontributor.

| Input | Actual role |
| --- | --- |
| [C158 actual cubic](Yin_C_G0158_v1.md#statement) | Original rank-d projection,2d normalization, range[0,1], exact Phi and actual Laurent degree/contact/mean conventions. |
| [C171 family and projection](Yin_C_G0171_v1.md#two-block-torus-statement) | Same exact L402 sequence, original degrees and positive total-measure interval; no near-one premise. |
| [C171 cyclic comparison](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Same-window rank and trace-norm price3L-6 before the rank-three original-factor correction. |
| [C171 cyclic phase](Yin_C_G0171_v1.md#two-block-torus-phase) | Exact matrix orientation, sampled phase and common-zero set, including the omitted omega=1 mode. |
| [C171 torus limits](Yin_C_G0171_v1.md#two-block-discrete-torus-limit) and [phase divergence](Yin_C_G0171_v1.md#two-block-singular-phase-divergence) | Elementary character/Fejer density, bounded regularization and nonabsolute summability of the three-torus phase; the four-variable application is proved above. |
| [R417 accepted C171 review](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) | Separate upstream whole review, reused with the present author's C171 contribution disclosed; no independent self-review claimed. |
| [L402 exact blocks](../ledger/Yin_L_G0402_v1.md#moving-exponent-gram-feasibility) | Complete A,B factors and order-two values at1, same K and prime scales, source arithmetic preserved at its retained MS05/RY26 scope. |
| [C160 original-factor correction](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Positive rank-three difference in the common2d window; present author's accepted upstream contribution is disclosed. |
| [L264 finite Blaschke derivative](../ledger/Yin_L_G0264_v1.md#exact-blaschke-two-moment-budget) | Existing primary GMR18 attribution and elementary Poisson derivative identity only; no exterior-root count or finite-input onset is imported as a uniform estimate. |


## Current assessment
[Selected decision](#decision-current-complete-moving-family-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T16:19 |
| status | open |
| reason | Register the complete actual cubic Wiener-divergence proof on the same moving-prime Salem family for a separate noncontributor whole review. Original2d kernel, fixed scalar cubic, full signed frequencies, variation/interpolation and rank costs, exact first-band coefficient and fixed-positive-measure boundary are retained. Root and angular_envelope_review contributed the new proof. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Actual cubic conclusion](#moving-cubic-statement) | Nonconstant Wiener norm tends to infinity for the exact original C158 cubic on the C171/L402 family, with all original degrees, ranges and exclusions. |
| argument | [Complete variation-to-cubic proof](#moving-cubic-phase-variation) | Entire Sections2--6, formulas3--17, common-root cancellation, allpass variation, discrete Fejer error, original-kernel Haar L1 return, four-torus coefficient limits and exact -85/512 first band. |
| dependency | [C158 exact cubic](Yin_C_G0158_v1.md#statement) | Original rank-d residual projection,2d normalization, range[0,1], exact Phi and retained Laurent degree/contact/mean conventions. |
| dependency | [C171 actual family](Yin_C_G0171_v1.md#two-block-torus-statement) | Same exact Salem sequence, original degree and bounded positive total measure; no near-one premise. |
| dependency | [C171 cyclic rank comparison](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Complete finite cyclic relation projection and trace-norm price3L-6 in the same2d window. |
| dependency | [C171 cyclic phase](Yin_C_G0171_v1.md#two-block-torus-phase) | Exact block orientation, equal-modulus channels, common-zero set and omitted zero sample. |
| dependency | [C171 torus limit](Yin_C_G0171_v1.md#two-block-discrete-torus-limit) | Existing elementary character/Fejer density and bounded regularization; the new four-variable use is proved here. |
| dependency | [C171 singular phase](Yin_C_G0171_v1.md#two-block-singular-phase-divergence) | Nonabsolute summability of Uhat and essential path discontinuity, at its accepted scope. |
| dependency | [L402 exact blocks](../ledger/Yin_L_G0402_v1.md#moving-exponent-gram-feasibility) | Actual A,B formulas and exact order-two values, fixed K, separated prime scales and unchanged arithmetic/source boundary. |
| dependency | [C160 rank correction](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Positive rank-three difference and trace cost in the original common window; author's accepted upstream contribution disclosed. |
| support | [Complete fixed inputs](#moving-cubic-scope-and-inputs) | All nine input roles, authorship, source scope and original measure/degree/rate limits. |
| support | [R417 upstream independent review](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) | Accepted complete C171 review, not a review of the new cubic transfer by either contributor. |
| support | [L264 Blaschke identity](../ledger/Yin_L_G0264_v1.md#exact-blaschke-two-moment-budget) | Existing GMR18 primary attribution and elementary Poisson derivative identity only; no new original-source proof audit or uniform-onset input. |

### Decision whole-reviewed-2026-10-19

| Field | Value |
| --- | --- |
| date | 2026-10-18T16:25 |
| status | proved |
| reason | Adopt actual cubic Wiener divergence after the whole noncontributor R420 review. All17 formulas and nine input roles, complete finite projection/BV/Fejer costs, inverse phase orientation, exact -85/512 band and fixed-positive-measure scope are retained; no near-one, rate or unrestricted-gap conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Actual cubic conclusion](#moving-cubic-statement) | Nonconstant Wiener norm tends to infinity for the exact original C158 cubic on the C171/L402 family, with all original degrees, ranges and exclusions. |
| argument | [Complete variation-to-cubic proof](#moving-cubic-phase-variation) | Entire Sections2--6, formulas3--17, common-root cancellation, allpass variation, discrete Fejer error, original-kernel Haar L1 return, four-torus coefficient limits and exact -85/512 first band. |
| dependency | [C158 exact cubic](Yin_C_G0158_v1.md#statement) | Original rank-d residual projection,2d normalization, range[0,1], exact Phi and retained Laurent degree/contact/mean conventions. |
| dependency | [C171 actual family](Yin_C_G0171_v1.md#two-block-torus-statement) | Same exact Salem sequence, original degree and bounded positive total measure; no near-one premise. |
| dependency | [C171 cyclic rank comparison](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Complete finite cyclic relation projection and trace-norm price3L-6 in the same2d window. |
| dependency | [C171 cyclic phase](Yin_C_G0171_v1.md#two-block-torus-phase) | Exact block orientation, equal-modulus channels, common-zero set and omitted zero sample. |
| dependency | [C171 torus limit](Yin_C_G0171_v1.md#two-block-discrete-torus-limit) | Existing elementary character/Fejer density and bounded regularization; the new four-variable use is proved here. |
| dependency | [C171 singular phase](Yin_C_G0171_v1.md#two-block-singular-phase-divergence) | Nonabsolute summability of Uhat and essential path discontinuity, at its accepted scope. |
| dependency | [L402 exact blocks](../ledger/Yin_L_G0402_v1.md#moving-exponent-gram-feasibility) | Actual A,B formulas and exact order-two values, fixed K, separated prime scales and unchanged arithmetic/source boundary. |
| dependency | [C160 rank correction](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Positive rank-three difference and trace cost in the original common window; author's accepted upstream contribution disclosed. |
| support | [Complete fixed inputs](#moving-cubic-scope-and-inputs) | All nine input roles, authorship, source scope and original measure/degree/rate limits. |
| support | [R417 upstream independent review](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) | Accepted complete C171 review, not a review of the new cubic transfer by either contributor. |
| support | [L264 Blaschke identity](../ledger/Yin_L_G0264_v1.md#exact-blaschke-two-moment-budget) | Existing GMR18 primary attribution and elementary Poisson derivative identity only; no new original-source proof audit or uniform-onset input. |
| review | [Whole moving-cubic finding](../audits/reviews/Yin_R_G0420_v1.md#moving-cubic-whole-independent-finding) | Complete exact statement, whole Sections2--7 and all17 formulas, nine fixed input roles and actual first-band/normalization/source boundaries. |


### Decision current-derivative-home-maintenance

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:34 |
| status | proved |
| reason | Maintain only the current same-object derivative proof home at complete C461 Section2 after actual full C172/R420 reading and exact derivative/inside-outside local applicability comparison. Original statement, whole argument/17 formulas/family/normalization/source boundary, all OTHER selected tuples/reviews and both dated old decisions remain unchanged. R420 retains the entire original UNKNOWN scope and actual L264 input; the new R667 finding is a narrow administrative SELF home comparison, not a new whole or isolated mathematical review, source-proof read, computation, wider family or Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Actual cubic conclusion](#moving-cubic-statement) | Nonconstant Wiener norm tends to infinity for the exact original C158 cubic on the C171/L402 family, with all original degrees, ranges and exclusions. |
| argument | [Complete variation-to-cubic proof](#moving-cubic-phase-variation) | Entire Sections2--6, formulas3--17, common-root cancellation, allpass variation, discrete Fejer error, original-kernel Haar L1 return, four-torus coefficient limits and exact -85/512 first band. |
| dependency | [C158 exact cubic](Yin_C_G0158_v1.md#statement) | Original rank-d residual projection,2d normalization, range[0,1], exact Phi and retained Laurent degree/contact/mean conventions. |
| dependency | [C171 actual family](Yin_C_G0171_v1.md#two-block-torus-statement) | Same exact Salem sequence, original degree and bounded positive total measure; no near-one premise. |
| dependency | [C171 cyclic rank comparison](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Complete finite cyclic relation projection and trace-norm price3L-6 in the same2d window. |
| dependency | [C171 cyclic phase](Yin_C_G0171_v1.md#two-block-torus-phase) | Exact block orientation, equal-modulus channels, common-zero set and omitted zero sample. |
| dependency | [C171 torus limit](Yin_C_G0171_v1.md#two-block-discrete-torus-limit) | Existing elementary character/Fejer density and bounded regularization; the new four-variable use is proved here. |
| dependency | [C171 singular phase](Yin_C_G0171_v1.md#two-block-singular-phase-divergence) | Nonabsolute summability of Uhat and essential path discontinuity, at its accepted scope. |
| dependency | [L402 exact blocks](../ledger/Yin_L_G0402_v1.md#moving-exponent-gram-feasibility) | Actual A,B formulas and exact order-two values, fixed K, separated prime scales and unchanged arithmetic/source boundary. |
| dependency | [C160 rank correction](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Positive rank-three difference and trace cost in the original common window; author's accepted upstream contribution disclosed. |
| support | [Complete fixed inputs](#moving-cubic-scope-and-inputs) | All nine input roles, authorship, source scope and original measure/degree/rate limits. |
| support | [R417 upstream independent review](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) | Accepted complete C171 review, not a review of the new cubic transfer by either contributor. |
| support | [Complete current Blaschke derivative proof](Yin_C_G0461_v1.md#exact-blaschke-two-moment-budget) | Same existing GMR18 primary attribution and complete elementary Poisson derivative/circle mean only, with exterior single-factor adaptation already local in this C172 proof; no actual exterior-root count, coefficient budget, new original-source proof audit or uniform-onset input. |
| review | [Whole moving-cubic finding](../audits/reviews/Yin_R_G0420_v1.md#moving-cubic-whole-independent-finding) | Complete exact statement, whole Sections2--7 and all17 formulas, nine fixed input roles and actual first-band/normalization/source boundaries. |
| review | [Actual derivative-home SELF finding](../audits/reviews/Yin_R_G0667_v1.md#moving-cubic-derivative-home-finding) | Narrow same-object current derivative proof/source-home and already local outside-disk adaptation only; no new whole C172 verdict, changed mathematical scope or fresh isolated coverage. Original R420 whole UNKNOWN and old fixed inputs remain. |


### Decision current-complete-moving-family-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T01:21 |
| status | proved |
| reason | Select the complete C494 home for exactly the already used L402 family/blocks/original-degree joint-projection interface. Preserve the statement, entire proof, status, authority, all other input and review tuples/scopes. This same-object maintenance supplies no fresh whole or isolated review and does not backdate C494 as an old input. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#moving-cubic-statement) | Nonconstant Wiener norm tends to infinity for the exact original C158 cubic on the C171/L402 family, with all original degrees, ranges and exclusions. |
| argument | [Exact argument](#moving-cubic-phase-variation) | Entire Sections2--6, formulas3--17, common-root cancellation, allpass variation, discrete Fejer error, original-kernel Haar L1 return, four-torus coefficient limits and exact -85/512 first band. |
| dependency | [Exact dependency](Yin_C_G0158_v1.md#statement) | Original rank-d residual projection,2d normalization, range[0,1], exact Phi and retained Laurent degree/contact/mean conventions. |
| dependency | [Exact dependency](Yin_C_G0171_v1.md#two-block-torus-statement) | Same exact Salem sequence, original degree and bounded positive total measure; no near-one premise. |
| dependency | [Exact dependency](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Complete finite cyclic relation projection and trace-norm price3L-6 in the same2d window. |
| dependency | [Exact dependency](Yin_C_G0171_v1.md#two-block-torus-phase) | Exact block orientation, equal-modulus channels, common-zero set and omitted zero sample. |
| dependency | [Exact dependency](Yin_C_G0171_v1.md#two-block-discrete-torus-limit) | Existing elementary character/Fejer density and bounded regularization; the new four-variable use is proved here. |
| dependency | [Exact dependency](Yin_C_G0171_v1.md#two-block-singular-phase-divergence) | Nonabsolute summability of Uhat and essential path discontinuity, at its accepted scope. |
| dependency | [Exact dependency](Yin_C_G0494_v1.md#moving-exponent-gram-feasibility) | Actual A,B formulas and exact order-two values, fixed K, separated prime scales and unchanged arithmetic/source boundary. |
| dependency | [Exact dependency](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Positive rank-three difference and trace cost in the original common window; author's accepted upstream contribution disclosed. |
| support | [Exact support](#moving-cubic-scope-and-inputs) | All nine input roles, authorship, source scope and original measure/degree/rate limits. |
| support | [Exact support](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) | Accepted complete C171 review, not a review of the new cubic transfer by either contributor. |
| support | [Exact support](Yin_C_G0461_v1.md#exact-blaschke-two-moment-budget) | Same existing GMR18 primary attribution and complete elementary Poisson derivative/circle mean only, with exterior single-factor adaptation already local in this C172 proof; no actual exterior-root count, coefficient budget, new original-source proof audit or uniform-onset input. |
| review | [Exact review](../audits/reviews/Yin_R_G0420_v1.md#moving-cubic-whole-independent-finding) | Complete exact statement, whole Sections2--7 and all17 formulas, nine fixed input roles and actual first-band/normalization/source boundaries. |
| review | [Exact review](../audits/reviews/Yin_R_G0667_v1.md#moving-cubic-derivative-home-finding) | Narrow same-object current derivative proof/source-home and already local outside-disk adaptation only; no new whole C172 verdict, changed mathematical scope or fresh isolated coverage. Original R420 whole UNKNOWN and old fixed inputs remain. |

