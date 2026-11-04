---
author: Yin
---
# Complete fractional critical-moment regularity and exponential unbounded control

This retains the complete original L252 theorem/proof, all required transient dual/Fourier interfaces and all negative, endpoint and input-dependent boundaries.
Original exploration, source comparison and old R116 inputs remain fixed.
No Task/E execution or source proof reading resumes.

## Statement

Let alpha be any algebraic unit, O=Z[alpha], X=Hom(O,R/Z) its compact additive dual and H normalized Haar measure.
Use precisely independent digits0,+1,-1 of probabilities1/2,1/4,1/4.
Let p_n be the complete zero-return probability, f_n the complete first positive-return probability,

    U(t)=sum_(n>=0)p_n t^n=1/(1-F(t)),
    F(t)=sum_(n>=1)f_n t^n,
    R=(lim_n p_n^(1/n))^(-1) in[1,2].

Assume actual CRITICAL TRANSIENCE U_R=U(R)<infinity, eta_R=1/U_R>0.
Set a_n=R^n p_n and q_n=R^n f_n, so sum q_n=1-eta_R<1.
Define S(theta)(x)=theta(alpha x), w(theta)=cos^2(pi theta(1)),

    W_n=product_(j=0)^(n-1) w composed with S^j,
    V_n=product_(j=1)^n w composed with S^(-j),
    u_t=U(t)^(-1)sum_(n>=0)t^n W_n,
    v_t=U(t)^(-1)sum_(n>=0)t^n V_n,
    a_t=u_t H, b_t=v_t H, 0<t<=R,
    C_R=u_R*v_R,
    C_s the continuous density of a_s*b_R, 0<s<R,
    D(delta)=sum_(n>=1)a_n[1-(1-delta)^n],
    delta=1-s/R in(0,1).

The notation a_n for scalar Green weights is distinct from the probability measures a_t.
These are the complete original-law densities on the full actual order, not countable-core stationary probabilities or a positive-theta auxiliary law.
Then

    ||C_R-C_s||_1<=2D(delta)/U_R,
    ||C_s||_infinity=eta_R+D(delta)/[delta U(s)U_R].

For any a in(0,1), delta_0 in(0,1/2] and M>0 such that D(delta)<=M delta^a for every0<delta<=delta_0, put

    B=M/U_R, p_*=1/(1-a),
    y_0=max{4,4B delta_0^(-(1-a))}.

The complete critical convolution C_R is weak L^(p_*), with

    H{C_R>y}<=(4B/y)^p_* for every y>=y_0.

For every real p in[1,p_*) it belongs to strong Lp, obeys the full bound9, and, for every0<delta<=delta_0,

    ||C_R-C_(R(1-delta))||_p
       <=[(4B)^(1/p)(1+B2^(1-a))^(1-1/p)
                        /(1-2^(-gamma))]delta^gamma,
    gamma=a-1+1/p>0.

There is no strong-endpoint p=p_* or supremum-norm convergence assertion.
A sufficient complete hypothesis is M_a=sum_(n>=1)n^a a_n<infinity, giving M=M_a and delta_0=1/2.
For every a in(0,1], complete first-return and Green moments satisfy, including infinite values,

    Q_a=sum_(n>=1)n^a q_n,
    Q_a<=M_a<=Q_a/eta_R^2.

Thus finiteness is equivalent at each actual transient input; the a1 endpoint is the earlier finite-derivative/bounded-density regime, not a new weak-endpoint claim.

For every alpha with actual irreducible polynomial t^4+1, the original complete cyclic law has R=1 and satisfies critical transience but F'(1)=infinity.
Its complete both-critical density is essentially unbounded and nevertheless

    integral_X exp(C_R/64)dH<=4exp(17/32).

It belongs to every finite Lp, with square-summable but not absolutely summable complete Fourier coefficients.
The exact all-residue return law, harmonic divergence and complete exponential-tail calculation remain in Section4.
This is a torsion zero-Mahler-measure control.
No unknown nontorsion transience or moment, recurrent-case density formula, input/degree-uniform moment/cost, finite critical mean from finite-p bounds, near-one family or positive Mahler gap is asserted.

<a id="argument"></a>
## Complete argument

### Complete consumed transient dual and mixed-overlap interface

The following is the exact transient part of the already proved L240/L248 mechanism, made explicit here so that no required norm/monotonicity argument is hidden in an L support.
It does not use their separate nontorsion ergodicity theorem or its source foundation.
The existence of the original h2 limit and hence R in[1,2] is the accepted general-unit C405 interface, including torsion and the possibly zero entropy.
The first-return decomposition gives U=1/(1-F), with all coefficients nonnegative; at finite U_R it gives F(R)=1-1/U_R<1 by monotone limits.

S preserves H because multiplication by the unit is integral unimodular on the power basis.
Each nonnegative finite product W_n is the squared modulus of the original fair-binary endpoint characteristic function; its Fourier coefficients are the full difference probabilities mu_n(x), and its Haar integral is p_n.
Since V_n=W_n composed with S^(-n), its coefficients are mu_n(alpha^n x), with the same integral p_n.
All functions/coefficient sequences are real and even.
At every0<t<=R, the integrals of the defining nonnegative series sum to U(t)<infinity.
They therefore define nonnegative L1 densities of integral one; the normalization and monotone series give L1 convergence as t increases to R.
The convolution C_R is consequently an L1 probability density, without an L2 or bounded-factor premise.

Write A_t(x),B_t(x) for the Fourier coefficients of a_t,b_t.
They are nonnegative and at most one, with value one at zero.
For x!=0, decomposing every path0 to x at its last visit to zero gives sum_n t^n mu_n(x)=U(t)L_t(x), where L_t is the original nonnegative no-further-zero path series.
Decomposing a path from x to zero at its first hit gives sum_n t^n mu_n(alpha^n x)=U(t)H_t(x), using the original digit-sign symmetry for the endpoint sign.
Set L_t(0)=H_t(0)=1.
Thus A_t=L_t and B_t=H_t, proving coefficientwise monotonicity in t on the whole order, not just its actual return core.
The critical coefficients are the same limits by the L1 convergence above.

For s,t<R, finite-product Fourier multiplication and Haar invariance give

    sum_x mu_n(x)mu_m(alpha^m x)
          =integral_X W_n V_m dH=p_(n+m).

Indeed composition with S^m makes the exponents one contiguous interval0,...,n+m-1.
Tonelli and nonnegative coefficients yield

    K(s,t)=sum_x A_s(x)B_t(x)
       =[sU(s)-tU(t)]/[(s-t)U(s)U(t)]
       =[s eta_t-t eta_s]/(s-t), s!=t,
    K(s,s)=eta_s+sF'(s).

The double sum is finite because max(s,t)<R and sum_(k>=0)(k+1)max(s,t)^k p_k converges.
The divided difference uses the exact finite geometric sum over n+m=k; the diagonal follows by differentiating strictly inside the power-series radius.
Increasing t to R and using nonnegative monotonicity gives, for every0<s<R,

    K(s,R)=sum_x A_s(x)B_R(x)
       =[R eta_s-s eta_R]/(R-s)
       =eta_R+[eta_s-eta_R]/(1-s/R)<infinity.

The absolutely summable nonnegative coefficient sequence defines the continuous convolution density C_s by its full Fourier series.
Equality of Fourier coefficients identifies it with the positive convolution probability; continuity and positivity as a measure give pointwise nonnegativity.
The triangle bound and value at zero give ||C_s||_infinity=K(s,R).
For0<s<u<R the coefficient difference is also nonnegative and summable, hence

    ||C_u-C_s||_infinity=K(u,R)-K(s,R).

This is a sup-norm equality, without pointwise nonnegativity of the difference function.

At both-criticality, coefficientwise limits of K(t,t) give

    sum_x A_R(x)B_R(x)=eta_R+RF'(R),

where infinity is permitted.
If the sum is finite its Fourier series gives a continuous bounded C_R with that exact norm.
Conversely, if C_R has essential supremum M, convolve it at zero with the product Fejer kernel on the power-basis torus.
Its integral is at most M, and its exact finite expansion is

    sum_(x in Z^d) A_R(x)B_R(x)
             product_(j=1)^d(1-|x_j|/N)_+ <= M.

Each term increases to its full coefficient; monotone convergence gives sum A_R B_R<=M.
The Fejer identity follows by expanding the squared modulus of sum_(j=0)^(N-1)exp(2pi i jt), divided by N, separately in each coordinate.
Thus a bounded both-critical density is equivalent to RF'(R)<infinity, with no nontorsion or individual-factor regularity hypothesis.
This proves every transient dual, mixed-norm, monotonicity and unboundedness interface used in the following original argument.

<a id="critical-lp-reuse-and-exact-scope"></a>
### 1. Reuse, exact question and changed conclusion

The present proof investigates the actual both-critical convolution, without presuming its critical recurrence type on any unknown Salem input.

The local reuse screen read [L240's whole-order Abel construction and critical limits](../ledger/Yin_L_G0240_v1.md#whole-order-critical-abel-limits), its [bounded-convolution criterion](../ledger/Yin_L_G0240_v1.md#critical-convolution-bounded-density-test), [L248's exact mixed overlap](../ledger/Yin_L_G0248_v1.md#mixed-parameter-full-overlap) and [one-critical bound](../ledger/Yin_L_G0248_v1.md#one-critical-factor-smoothing).
L244 already proves the separate atomless and factorwise Lp boundaries.
In particular, transience already supplies two L1 factor densities in L240, and their convolution is therefore L1.
That automatic absolute continuity is reuse, not a new contribution.

The changed question is quantitative integrability strictly between L1 and boundedness when the full critical mean can be infinite.
Below, a fractional COMPLETE return moment supplies a weak Lp endpoint, every strictly lower strong Lp norm and an Lp approximation rate.
The actual fourth-degree torsion control already classified in [L206](../ledger/Yin_L_G0206_v1.md#cyclotomic-radical-critical-thresholds) then has a both-critical convolution with an exponential integrability bound but no bounded density.
Its return law and critical classification are old; the density regularity and explicit bound are the new calculation.
This is a calibration of the distinction, not a nontorsion small-measure counterexample.

L206's classical lattice-recurrence comparison and the [DS84 source scope](../audits/literature/DS84/readme.md) are retained at their original attribution depth.
The actual law here updates coordinates cyclically; it is not silently replaced by a nearest-neighbor lattice walk.
The new estimates use the existing exact Abel identities, a nonnegative mixture decomposition, the elementary distribution-function inequality and displayed scalar bounds.
No interpolation theorem, Riesz-potential identification, new external theorem or historical priority claim is invoked.
A bounded local screen for fractional critical moments, weak Lp and exponential integrability found no earlier result with this conclusion; this is not an exhaustive literature novelty search.
No new computation or J is a premise.

Let alpha be any algebraic unit with its actual power-basis order O=Z[alpha], compact dual X and normalized Haar probability H.
Retain the ORIGINAL iid digits0,+1,-1 with probabilities1/2,1/4,1/4.
Write p_n for their complete zero-return probability and f_n for the complete first positive return probability.
Let

    R=(lim_n p_n^(1/n))^(-1), 1<=R<=2,
    U(t)=sum_(n>=0)p_n t^n=1/(1-F(t)),
    F(t)=sum_(n>=1)f_n t^n, 0<t<R.

Throughout Sections2--4 assume CRITICAL TRANSIENCE:

    U_R:=U(R)<infinity, eta_R=1/U_R>0,
    a_n=R^n p_n, q_n=R^n f_n,
    sum a_n=U_R, sum q_n=F(R)=1-eta_R<1.             (1)

This is an additional hypothesis for an unknown nontorsion input.
It is not inferred from infinite core, high degree or lack of a bounded convolution.
The symbols a_n are scalars and must not be confused with the dual measures a_t below.

Reuse the actual finite trigonometric products W_n,V_n from L240, each nonnegative with Haar integral p_n.
The densities and their measures are

    u_t=U(t)^(-1) sum t^n W_n,  a_t=u_t H,
    v_t=U(t)^(-1) sum t^n V_n,  b_t=v_t H.

At t=R these are genuine L1 probability densities by(1).
Thus c_R=a_R*b_R has an L1 density C_R=u_R*v_R.
Write C_s for the continuous density of a_s*b_R, where0<s<R.
The exact L248 norm is

    ||C_s||_infinity=K(s,R)
       =eta_R+[eta_s-eta_R]/(1-s/R), eta_s=1/U(s).  (2)

All these constructions and(2) apply also to torsion inputs.
The L240 nontorsion ergodicity argument is used only for its separate recurrent-factor dichotomy, which is not an input here.
No parameter greater than one is required in the transient analysis.

<a id="critical-l1-mixture-and-cost"></a>
### 2. A full L1 approximation with its exact Abel cost

Put delta=1-s/R in(0,1) and

    D(delta)=U_R-U(R(1-delta))
            =sum_(n>=1)a_n[1-(1-delta)^n].          (3)

The mixture decomposition is an equality of positive measures:

    a_R = [U(s)/U_R] a_s
          + U_R^(-1) sum_(n>=0)R^n[1-(s/R)^n]W_n H.

The second term has total mass D(delta)/U_R.
Consequently, using L1 rather than the half-normalized total-variation convention,

    ||u_R-u_s||_1<=2D(delta)/U_R,
    ||C_R-C_s||_1<=2D(delta)/U_R.                    (4)

For the second inequality, integrate the absolute value after convolution with the probability b_R and apply Tonelli.
It requires no L2 bound, bounded factor density or finite first-return derivative.
The same statements hold when the other factor is the varying one.
They are ordinary consequences of the retained densities, not an independent absolute-continuity theorem.

Substitution into(2) gives the useful EXACT supremum

    K(s,R)=eta_R+D(delta)/[delta U(s)U_R].           (5)

In particular, if0<a<1 and for0<delta<=delta_0<=1/2 one has

    D(delta)<=M delta^a,    B=M/U_R>0,              (6)

then

    ||C_R-C_s||_1<=2B delta^a,
    ||C_s||_infinity<=1+B delta^(a-1).              (7)

Here U(s)>=1 and eta_R<=1 have been used only for the upper bound.
Neither U_R nor M is asserted input uniform.
The loss delta^(a-1) is real; it is not removed by the L1 convergence.

<a id="critical-fractional-moment-weak-lp"></a>
### 3. Weak endpoint, strong Lp and the approximation rate

Assume(6) and put p_*=1/(1-a)>1.
A measurable function belongs to weak Lp_* here precisely when sup_(y>0)y^p_* H{|C|>y} is finite.
This distribution bound is weaker than strong Lp_* integrability.

For

    y>=y_0:=max{4,4B delta_0^(-(1-a))},
    delta=(4B/y)^p_*<=delta_0,

equation(7) gives ||C_s||_infinity<=1+y/4<=y/2.
If C_R>y, its difference from C_s therefore has absolute value greater than y/2.
Integrating that difference and using(4),(6) proves

    H{C_R>y}<=(2/y)||C_R-C_s||_1
             <=(4B/y)^p_*.                         (8)

This proves C_R is weak Lp_* and, for every1<=p<p_*, that

    ||C_R||_p^p
       <=y_0^p + p(4B)^p_* y_0^(p-p_*)/(p_*-p).   (9)

Indeed integrate p y^(p-1)H{C_R>y} over y>0, bounding the lower interval by its full Haar mass one.
Tonelli justifies this layer integration for a nonnegative density.
There is no strong endpoint assertion in(9).

There is also an explicit approximation rate.
For0<delta<=delta_0 let delta_j=2^(-j)delta, s_j=R(1-delta_j).
Then(4),(6) give

    ||C_(s_(j+1))-C_(s_j)||_1<=4B delta_j^a.

The complete L248 coefficient monotonicity gives exactly

    ||C_(s_(j+1))-C_(s_j)||_infinity
       =K(s_(j+1),R)-K(s_j,R)
       <=D_0 delta_j^(a-1),
    D_0=1+B 2^(1-a).                                (10)

The equality is about the sup norm: the Fourier coefficient differences are nonnegative, but the difference function need not be pointwise nonnegative.
For the inequality use(7) at delta_(j+1) and delta_j<=1.

For any integrable bounded h, integration of |h|^p<=||h||_infinity^(p-1)|h| gives ||h||_p<=||h||_1^(1/p)||h||_infinity^(1-1/p).
Apply this elementary inequality to(10).
For1<=p<p_* put gamma=a-1+1/p>0.
The successive Lp differences are bounded by

    (4B)^(1/p)D_0^(1-1/p)delta^gamma 2^(-j gamma).

Their sum converges.
Its Lp limit equals C_R because(4) already gives L1 convergence, and Haar has mass one.
Therefore

    ||C_R-C_(R(1-delta))||_p
       <=[(4B)^(1/p)D_0^(1-1/p)/(1-2^(-gamma))]
                                                        delta^gamma. (11)

Every constant, the strict p range and the transient premise are displayed.
This rate gives no control at p=p_* and no supremum norm convergence if the critical derivative is infinite.

A directly testable sufficient condition for(6) is the COMPLETE fractional Green moment

    M_a=sum_(n>=1)n^a a_n<infinity, 0<a<1.           (12)

The elementary inequality1-(1-delta)^n<=min{1,n delta}<=(n delta)^a gives D(delta)<=M_a delta^a, for every0<delta<1.
In particular(6) holds with M=M_a and delta_0=1/2.
No subset of returned words suffices for the upper moment in(12).

Equivalently one may use the complete defective first-return moment

    Q_a=sum_(n>=1)n^a q_n.
    Q_a<=M_a<=Q_a/eta_R^2,     0<a<=1.              (13)

For the lower bound the first-return coefficients are included in the renewal coefficients.
For the upper bound, expand U(Rr)=sum_(k>=0)(sum q_n r^n)^k.
For a k-fold word-length sum, (n_1+...+n_k)^a<=sum_i n_i^a.
Its total a-moment is at most k F(R)^(k-1) Q_a.
Summing over k>=1 gives Q_a/(1-F(R))^2.
All rearrangements are of nonnegative terms, so the inequalities remain valid with infinite values.
Since eta_R>0, finiteness is equivalent.
At a=1, finite M_1 instead gives the old finite-derivative/bounded-convolution regime; this endpoint is not advertised as new.

<a id="actual-torsion-exponential-unbounded-control"></a>
### 4. An actual unbounded critical density with exponential integrability

Take alpha a root of t^4+1, so alpha^4=-1.
Translation by one is Eisenstein at two, hence this is the actual irreducible degree-four order, not a reducible direct-product substitute.
The exact actual dyadic-cyclotomic law and full-core calculation now retained in [C419](Yin_C_G0419_v1.md#argument) give the full core Z^4 and

    R=1, n=4ell+s, 0<=s<4,
    p_n=b_ell^(4-s)b_(ell+1)^s,
    b_j=binom(2j,j)/4^j,
    1/(2sqrt j)<=b_j<=1/sqrt(j+1), j>=1, b_0=1.    (14)

These complete original-law identities and binomial bounds are reused; no enumeration or new recurrence-class proof is claimed.

The upper estimate in(14) implies p_n<=1/(ell+1)^2<=16/(n+1)^2 for all n>=0.
Thus U_1<infinity.
On the other hand, at n=4ell with ell>=1, n p_n>=1/(4ell), so sum_n n p_n=infinity.
Consequently F(1)<1 but F'(1)=infinity by complete renewal.
The complete bounded-density criterion proved in the interface above therefore says the L1 convolution density C_R is NOT essentially bounded.
This is the already retained critical classification combined with its applicable convolution criterion; no nontorsion hypothesis is invoked.

A stronger regularity bound follows directly.
For0<delta<=1/2, put N=floor(1/delta).
Then

    D(delta)<=16 sum_(n>=1)min{1,n delta}/(n+1)^2
             <=16 delta[log(2/delta)+1].            (15)

For the first N terms use n/(n+1)^2<=1/(n+1) and sum_(n=1)^N1/(n+1)<=log(N+1)<=log(2/delta).
The remaining sum is at most1/(N+1)<=delta by integral comparison.
Both estimates retain the entire sequence, including the residue classes modulo four.

Put A=17+16log2.
For v>=log2 choose delta=exp(-v) and y=2A+32v.
Equations(4),(5),(15), with U_R,U(s)>=1, give

    ||C_s||_infinity<=A+16v=y/2,
    ||C_R-C_s||_1<=32 exp(-v)(v+log2+1).

As in(8),

    H{C_R>2A+32v}
       <=[64(v+log2+1)/(2A+32v)]exp(-v)
       <=2exp(-v),       v>=log2.                  (16)

The last comparison is exact because4A-64(log2+1)=4>0.
Let y_0=2A+32log2=34+64log2.
For y>=y_0, (16) bounds the tail by2exp((2A-y)/32).
Integrating the exponential by Tonelli yields the explicit estimate

    integral_X exp(C_R/64) dH
       <=exp(y_0/64)
          +(1/64) integral_(y_0)^infinity
                 2exp(2A/32)exp(-y/64)dy
       =4exp(17/32)<infinity.                      (17)

It follows, for instance by bounding each power by a constant multiple of the exponential, that C_R belongs to EVERY finite Lp space, but not to L-infinity.
Its complete Fourier coefficients therefore are square summable and are not absolutely summable, by Parseval and the positive-coefficient boundedness criterion; this last distinction is a consequence, not a new input.

The input is torsion and its total Mahler measure is zero.
It is a concrete regularity control for the actual law, not a sequence of positive measures tending to zero.
It excludes identifying infinite critical mean with failure of all strong Lp estimates or with singularity of the convolution.
It supplies no classification of a nontorsion Salem critical convolution.

<a id="critical-lp-boundary-and-next-step"></a>
### 5. Mathematical boundary and the next discriminator

The new implication under actual critical transience is a fractional COMPLETE return-moment bound -> weak endpoint and lower strong Lp integrability with a quantitative approximation rate.
This is stronger than the automatic L1 convolution already implied by L240, while strictly weaker than the finite first moment required for boundedness.
The explicit t^4+1 control distinguishes these regimes, even providing exponential integrability in the unbounded case.

For an unknown nontorsion input, neither transience nor any fractional moment in(12)/(13) has been established by this argument.
For a hypothetical near-one family, the degree, U_R, moment constants and permitted exponents can degenerate.
In particular a bound in a fixed finite Lp space does not establish finite critical mean, stationary attainment or a positive Mahler gap.
The recurrent case cannot use(4) because U_R is infinite, and remains a genuinely different joint-measure problem.

A useful next test is to estimate one actual complete fractional return moment on an infinite nontorsion core, or to control the recurrent convolution through a different joint identity.
A finite killed-box moment is a lower truncation and cannot supply the required full upper bound.
L247's fixed-height escape remains fully compatible with the present statements.
No program, numerical evidence, source-wide audit or unrestricted result is asserted.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:07 |
| status | open |
| reason | Preserve the complete original fractional moment/weak endpoint/strict strong-Lp/rate and exponential-unbounded-control theorem with all necessary transient dual and Fourier interfaces, complete moments and input-dependent costs for actual whole checking. No new research/source/native execution or unproved nontorsion moment is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full theorem](#statement) | Every actual critically transient algebraic unit, all a/delta/p strict ranges, complete Green/first-return moments, exact rates and actual torsion exponential/unboundedness control. |
| argument | [Entire proof](#argument) | Full transient dual/mixed-overlap/monotonicity/Fejer criterion plus original Sections1--5/equations1--17, all mixture normalizations, distribution/integrability limits, renewal moments and exponential constants. |
| dependency | [General-unit original return convention](Yin_C_G0405_v1.md#collision-operator-fixed-scope) | Exact original core/return law, existence of possibly zero h2 and R in[1,2]; no nontorsion restriction or essential-norm result is imported. |
| dependency | [Exact actual dyadic-cyclotomic control](Yin_C_G0419_v1.md#argument) | Only d4 full actual core/cyclic coordinate law, central-binomial product and all-j induction bounds; this proof derives its own transience/critical-mean and regularity conclusions. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:09 |
| status | proved |
| reason | Adopt after the actual whole C421/R623 check of all transient dual/Fourier/monotonicity/Fejer interfaces and every original mixture, complete moment, weak endpoint, strict strong-Lp, dyadic approximation and exponential-control argument. Reuse the adequate fixed C405/C419 inputs only at the declared original-law/d4 scopes, retaining the full transience and moment hypotheses, every eta_R/root/input cost, endpoint exclusion and torsion/nonuniformity negative. No new native/source proof, fresh isolated coverage, unknown nontorsion moment or Task/E resumption is claimed; original R116 remains whole UNKNOWN. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full theorem](#statement) | Every actual critically transient algebraic unit, all a/delta/p strict ranges, complete Green/first-return moments, exact rates and actual torsion exponential/unboundedness control. |
| argument | [Entire proof](#argument) | Full transient dual/mixed-overlap/monotonicity/Fejer criterion plus original Sections1--5/equations1--17, all mixture normalizations, distribution/integrability limits, renewal moments and exponential constants. |
| dependency | [General-unit original return convention](Yin_C_G0405_v1.md#collision-operator-fixed-scope) | Exact original core/return law, existence of possibly zero h2 and R in[1,2]; no nontorsion restriction or essential-norm result is imported. |
| dependency | [Exact actual dyadic-cyclotomic control](Yin_C_G0419_v1.md#argument) | Only d4 full actual core/cyclic coordinate law, central-binomial product and all-j induction bounds; this proof derives its own transience/critical-mean and regularity conclusions. |
| review | [Actual whole self finding](../audits/reviews/Yin_R_G0623_v1.md#critical-regularity-whole-self-finding) | Exact whole statement/argument/dependencies, full original fractional and exponential/unbounded control, every endpoint/renewal/law/degree/source limit; SELF does not replace original whole UNKNOWN. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:02 |
| status | proved |
| reason | Adopt the actual new isolated whole finding after complete reading of the exact proof, all original whole bindings and useful source/moment/endpoint limits. Keep the sufficient DS84 README as an ordinary attribution account and bind its already retained source-comparison interface through canonical R116, without inventing another U or changing mathematical scope. Original UNKNOWN/SELF, dates and fixed inputs remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every actual critically transient algebraic unit, all a/delta/p strict ranges, complete Green/first-return moments, exact rates and actual torsion exponential/unboundedness control. |
| argument | [Complete selected argument](#argument) | Full transient dual/mixed-overlap/monotonicity/Fejer criterion plus original Sections1--5/equations1--17, all mixture normalizations, distribution/integrability limits, renewal moments and exponential constants. |
| dependency | [Exact accepted input](Yin_C_G0405_v1.md#collision-operator-fixed-scope) | Exact original core/return law, existence of possibly zero h2 and R in[1,2]; no nontorsion restriction or essential-norm result is imported. |
| dependency | [Exact accepted input](Yin_C_G0419_v1.md#argument) | Only d4 full actual core/cyclic coordinate law, central-binomial product and all-j induction bounds; this proof derives its own transience/critical-mean and regularity conclusions. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0639_v1.md#isolated-critical-regularity-whole-finding) | Entire exact current Statement and Argument and original complete L252/R116 whole scope, every transient/mixed/Fejer/moment/endpoint/exponential-control argument and original source/negative limitation. |

