---
author: Yin
---

# Complete primitive singular convolution countermodels and the original weighted-row obstruction

The entire [L305](../ledger/Yin_L_G0305_v1.md) mathematical argument is retained at its actual FIXED primitive quartic and relaxed-law scope.
The original formal R204 finding and author/source/terminology history keep their actual inputs and dates.

<a id="statement"></a>
## Complete statement

Fix the ACTUAL composition-primitive irreducible quartic P=t^4-t^3-t^2-t+1,17/10<beta<18/10, unit-circle root zeta, actual O=Z[beta],B=1/(beta-1),S=beta B and rho(x)=|x(zeta)|.
Write x_+=x(beta),x_-=x(beta^-1).
Its COMPLETE ORIGINAL return core is the infinite strict strip D={|x_+|<B,|x_-|<S}.
The reciprocal additive involution T=beta^-1 iota, iota(beta)=beta^-1, preserves O,D,rho, with(Tx)_+=x_-/beta,(Tx)_-=beta x_+,T^2=Id.
The actual original1/4,1/2,1/4 law has true R<=2 and F(R)=1 by the accepted recurrence theorem; actual R and finiteness of mu=RF'(R) remain unclassified.

On X=Hom(O,R/Z), with nu_hat(x)=integral exp(2pi i theta(x))dnu, let tau(v)=(1-|v|)_+.
For EVERY smoothing t>=0, define on ALL O
    A_t(x)=tau(x_-/S)exp(-t rho(x)^2/2),
    B_t(x)=A_t(Tx)=tau(x_+/B)exp(-t rho(x)^2/2),
    sigma_t=A_t B_t=tau(x_+/B)tau(x_-/S)exp(-t rho(x)^2).
There are explicit even Borel probabilities a_t,b_t=(T^vee)_*a_t with those coefficients.
BOTH are purely singular for every t>=0.
Their convolution c_t=a_t*b_t has Fourier coefficients sigma_t, exactly positive on D, normalized1 at0 and strictly less than1 elsewhere.
All three functions are positive definite on the ENTIRE original additive order.

The construction uses real density f_a(u)=a[sin(pi a u)/(pi a u)]^2, f_a(0)=a, with integral1 and exact transform tau(v/a).
Independent U~f_S and centered Y in R² of covariance t I/(4pi²), Y=0 at t0, map to theta(x)=U x_-+Y dot(Re x(zeta),Im x(zeta)) mod1.
This gives a_t directly; its countable compact3-dimensional, or1-dimensional at t0, Lipschitz carrier is Haar-null in the actual4-torus even if dense.
No general Bochner representation or actual-law invariance is assumed.

Let M be the actual4-by-4 real embedding matrix of1,beta,beta²,beta³,
    delta=1/||M^-1||_2,a=delta/4,
    C_up=(2B/a+2)(2S/a+2)(2/a+2)^2,
    A_+=sum_(j=0)^3 beta^j,A_-=sum_(j=0)^3 beta^-j,
    C_bin=(1+2A_+/B)(1+2A_-/S).
For ALL r>=0, #{x in D:rho(x)<=r}<=C_up(r+1)^2.
For ALL r>=4 the INNER strict strip D_in={|x_+|<B/2,|x_-|<S/2} has at least r²/(16C_bin) such points.
These are actual fixed-input constants, with full basis conditioning retained.
For the ENTIRE neutral sum T_t=sum_(x in O)sigma_t(x),
    T_t<=C_up[t^-1+sqrt(pi)t^(-1/2)+1] for every t>0,
    1/(64e C_bin t)<=T_t<=C_up(2+sqrt(pi))/t for0<t<=1/16.
T_0=infinity.
For every t>0, c_t has the nonnegative continuous probability density
    C_t(theta)=sum_x sigma_t(x)chi_(-x)(theta),
    ||C_t||_infinity=C_t(0)=T_t.
At t0 c_0 is PURELY SINGULAR and has no bounded density, rather than an asserted existing unbounded density.

For t>0, pi_t=sigma_t/T_t on D is a constructed full-support discrete probability with unique largest atom0, every finite neutral moment, reciprocal symmetry and full nonnegative Fourier transform C_t/T_t.
Its coefficient sequence is also positive definite.
For EVERY finite-index additive subgroup I of O and projected masses p_I on G=O/I,
    p_I(0)-p_I(g)=|G|^-1 sum_chi pi_t_hat(chi)(1-Re chi(g))>=0,
    p_I(0)>=1/|G|.
No T-invariance of I is required.
As t decreases to0, pi_t(0)=1/T_t->0 and pi_t(K)->0 for EVERY fixed finite K.
No discrete limiting pi_0 is asserted.
The dual convolutions converge weakly to singular c_0.
Thus exact ACTUAL support, all additive/quotient positivity, reciprocity and singular factors alone bound neither these fixed-input convolution norms nor their distinguished discrete atom.

These are RELAXED models and NONE is an actual critical pair.
The genuine first-hit H_R=B_R, normalizedH_R(0)=1, satisfies at every nonzero state the ORIGINAL weighted row
    H_R(x)=R[H_R(beta x-1)/4+H_R(beta x)/2+H_R(beta x+1)/4].
At actual state1, beta/beta+1 cannot return whereas beta-1 does, and1 lies in D.
Consequently H_R(1)>0 and H_R(beta-1)/H_R(1)=4/R>=2.
For EVERY candidate t>=0 and EVERY0<R'<=2, put Delta=(1+sqrt13)/2>0.
Its exact values are
    B_t(1)=(2-beta)exp(-t/2)>0,
    B_t(beta-1)=beta(2-beta)exp(-t|zeta-1|²/2),
    B_t(beta)=B_t(beta+1)=0,
    R' sum_eta p_eta B_t(beta+eta)/B_t(1)
          =(R'beta/4)exp(-t Delta/2)<=beta/2<1.
The RELATIVE row residual is therefore at least1-beta/2 uniformly in t,R'.
Its absolute residual may vanish as t->infinity, while it is bounded away from0 as t decreases to0 at this fixed input.
The sole legal successor's probability1/4 is essential.
No arbitrary small global-residual-to-mean theorem is claimed.

T_t is not RF'(R), pi_t is not an actual stationary/occupation law, and t is not a return-time parameter.
The actual quartic mean remains possibly finite or infinite.
No finite row collection, complete actual-law neutral-tail/compactness estimate, varying-degree/small-total-m uniform statement, near-one sequence or unrestricted gap follows.
All source roles retain the selected Tao09 HTML conventions/attribution only; the local triangular/Gaussian/pushforward/counting proofs are complete.
The original2026-10-10T07:16 freeze and2026-10-10T07:23 singular-versus-unbounded-density terminology clarification remain, with no formula or proof change, program/native run or acquisition.

## Complete argument

<a id="argument"></a>

<a id="primitive-singular-convolution-reuse"></a>
### 1. Reuse, actual input and the precise relaxation being tested

The [L301 composition normalization](Yin_C_G0558_v1.md#canonical-composition-mean-normalization) removes an explicit radical-power expense but does not classify the critical mean even for the original quartic.
We therefore fix that composition-primitive input throughout this argument:

    P(t)=t^4-t^3-t^2-t+1,  beta>1,  O=Z[beta],
    B=1/(beta-1),  S=beta B,  rho(x)=|x(zeta)|,        (1)

where zeta is its upper-half-plane unit-circle root.
The [complete quartic proof in L169](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) gives irreducibility, 17/10<beta<18/10, and the full rank-four lattice embedding

    x -> (x_+,x_-,Re z,Im z),
    x_+=x(beta), x_-=x(beta^(-1)), z=x(zeta).

The polynomial has a nonzero coefficient of t, so its exponent gcd is one: no nontrivial substitution P=Q(t^r), r>1, is present.
In particular this is a primitive, nontorsion actual unit, without an increasing-degree composition parameter.
The [exact-strip theorem in L170](Yin_C_G0400_v1.md#exact-salem-return-strip), which explicitly applies to L169, identifies its actual original-digit return core as

    D={x in O: |x_+|<B and |x_-|<S}.                 (2)

This core is infinite.
Neither a larger fractional module nor a neutral-radius truncation is used.
The reciprocal additive involution is

    T(x)=beta^(-1)iota(x),  iota(beta)=beta^(-1),
    (Tx)_+=x_-/beta,  (Tx)_-=beta x_+,
    (Tx)(zeta)=zeta^(-1) conjugate(z),  T^2=Id.       (3)

It preserves O and D.
Its existence, orientation and actual-word interpretation are retained in L169 and [L240](Yin_C_G0563_v1.md#critical-convolution-bounded-density-test).

We reuse the following precise probability interfaces.
Original increments eta=-1,0,1 have probabilities 1/4,1/2,1/4 and act by x -> beta x+eta.
If p_n is the original zero-return probability, write R=exp(h_2) for its critical radius, F for the first-return series, and mu=R F'(R) for the possibly infinite critical mean when F(R)=1.
The all-zero word implies R<=2.
[L285](Yin_C_G0526_v1.md#quartic-critical-recurrence-and-sextic-approximation) already proves F(R)=1 for this quartic; the value of R and the finiteness of mu remain unclassified.
This recurrence premise is reused, not reproved or inferred from the construction below.

On X=Hom(O,R/Z), a four-dimensional torus in the power basis, write chi_x(theta)=exp(2 pi i theta(x)) and use nu_hat(x)=integral chi_x dnu.
The results [L236](Yin_C_G0563_v1.md#critical-fourier-positive-occupation) and [L240](Yin_C_G0563_v1.md#whole-order-critical-abel-limits) construct the ACTUAL limiting dual probabilities a_R,b_R with nonnegative real Fourier coefficients A_R,B_R.
They obey B_R=A_R composed with T, A_R(0)=B_R(0)=1, and sigma_R=A_R B_R is positive exactly on D.
At recurrence both factors are purely singular.
Their convolution has a bounded density exactly when mu is finite, with density norm mu.
These implications use the actual weighted eigenmeasure equations, not just support or positive definiteness.

Here a function c on the discrete group O is positive definite if every finite quadratic form sum_(j,k) u_j conjugate(u_k)c(x_j-x_k) is nonnegative.
We use the terminology already attributed to [Tao09](../audits/literature/Tao09/readme.md#positive-definite-attribution).
Its verification below is direct integration against explicitly constructed probabilities.
We do not invoke the uninspected general Bochner proof.
The classical Gaussian Fourier transform and measure convolution identities were additionally inspected this round in the author's [online lecture](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/), Section 1, Exercises 14--16, and Section 3, Exercise 41.
They supply attribution for elementary formulas that are proved or verified below; no new source theorem about actual return laws is imported.
The existing HTML/no-retained-PDF acquisition boundary remains unchanged.

**Question tested.**
Do exact actual-core support, all additive Fourier positivity, reciprocal pairing and pure singularity of the two dual factors together classify their convolution regularity or bound its norm?
The next sections give a negative answer at this one fixed primitive infinite-core input.
The constructed measures are explicitly a relaxation of the actual critical measures.
Section 5 proves a uniform violation of the original weighted equation at an actual core state, preventing any misidentification with a stationary or critical law.

<a id="primitive-reciprocal-singular-model"></a>
### 2. Explicit singular reciprocal factors on the actual order

Put tau(v)=(1-|v|)_+.
For every t>=0 define functions on ALL O by

    A_t(x)=tau(x_-/S) exp(-t rho(x)^2/2),
    B_t(x)=A_t(Tx)=tau(x_+/B) exp(-t rho(x)^2/2),
    sigma_t(x)=A_t(x)B_t(x)
       =tau(x_+/B)tau(x_-/S) exp(-t rho(x)^2).        (4)

The subscript t is a Gaussian smoothing parameter; it is neither time nor a return-series variable.
All coefficients in(4) lie in[0,1], are even and real, and equal one at zero.
The support of sigma_t is EXACTLY D for every finite t>=0, including the strict real boundaries.
For every nonzero x, sigma_t(x)<1: if x belongs to D then injectivity of the expanding field embedding gives x_+!=0 and hence tau(x_+/B)<1; if x is outside D its coefficient is zero.

**Proposition 1.**
For every t>=0 there are explicitly constructed even Borel probability measures a_t,b_t on X with Fourier coefficients A_t,B_t.
They are both purely singular with respect to Haar measure, and

    b_t=(T^vee)_*a_t,  c_t=a_t*b_t,
    c_t_hat(x)=sigma_t(x),
    (T^vee theta)(x)=theta(Tx).                       (5)

Consequently all three coefficient functions are positive definite on the entire actual order, not just on a prescribed finite set or finite quotient.

*Proof.*
We first give the real probability whose characteristic function is triangular.
For a>0 put

    f_a(s)=a [sin(pi a s)/(pi a s)]^2,
    f_a(0)=a.

This function is nonnegative and integrable, by its boundedness near zero and O(s^(-2)) decay at infinity.
Its exact Fourier transform, with the convention integral exp(2 pi i v s) f_a(s) ds, is

    integral_R exp(2 pi i v s) f_a(s) ds=tau(v/a).   (6)

For completeness, write I_a=[-a/2,a/2] and expand

    f_a(s)=a^(-1) integral_(I_a) integral_(I_a)
                       exp(2 pi i s(u-v')) du dv'.

Multiply by exp(-pi epsilon s^2), epsilon>0, before integrating in s.
Fubini is then justified on the finite rectangle by the integrable Gaussian.
The identity

    integral_R exp(-pi epsilon s^2+2 pi i w s) ds
           =epsilon^(-1/2) exp(-pi w^2/epsilon)

shows that the regularized transform is the convolution, evaluated at v, of the continuous compactly supported function tau(v/a) with the probability Gaussian kernel epsilon^(-1/2)exp(-pi v^2/epsilon).
This converges to tau(v/a) as epsilon decreases to zero: split the convolution into a small interval, where uniform continuity applies, and its Gaussian tail.
Dominated convergence by f_a also gives the unregularized transform.
The displayed Gaussian transform follows directly by differentiating its integral in w, integrating by parts in s, and solving G'(w)=-(2 pi w/epsilon)G(w), with G(0)=epsilon^(-1/2).
Thus(6) uses no general positive-definite representation theorem.
At v=0 it gives integral f_a=1.

Take a real random variable U with density f_S, and independently a vector Y=(Y_1,Y_2) with centered two-dimensional Gaussian law of covariance t/(4 pi^2) times the identity.
At t=0 set Y=0 deterministically.
The same one-dimensional Gaussian formula, applied twice, gives

    E exp(2 pi i Y dot (Re z,Im z))=exp(-t|z|^2/2).

Map (U,Y) to the character

    theta_(U,Y)(x)=U x_-+Y_1 Re z+Y_2 Im z mod1.    (7)

The pushforward probability is a_t.
Independence and(6) give its Fourier coefficient A_t(x).
Define b_t by the pushforward in(5); equation(3) gives its coefficient B_t.
Symmetry of U,Y gives evenness.
Independence in the convolution proves the product coefficient in(5) by Fubini.
For any such probability nu, integration of |sum_j u_j exp(2 pi i theta(x_j))|^2 proves positive definiteness directly.

To check pure singularity, identify X with R^4/Z^4 through the power basis of O.
For t>0 the measure a_t is carried by the image of the linear map R^3 -> X in(7).
The image of every compact parameter cube has four-dimensional Haar measure zero: subdividing that cube into O(delta^(-3)) cubes of side delta covers its Lipschitz image by O(delta^(-3)) torus balls of diameter O(delta), of total Haar volume O(delta).
Letting delta tend to zero proves the assertion.
The union of these compact images over integer cube sizes is a Borel Haar-null carrier for a_t, even if the image is dense.
At t=0 the same argument uses an image of R instead.
An additive torus automorphism preserves Haar-null sets, so b_t is also purely singular.
This proves all assertions.
No assertion of invariance under multiplication by beta was used.

<a id="primitive-convolution-complete-mass"></a>
### 3. Complete neutral tail and exact convolution norm

We next control the entire sum, including arbitrarily large neutral coordinates:

    T_t=sum_(x in O) sigma_t(x).                     (8)

The count in [L170](Yin_C_G0400_v1.md#return-core-neutral-growth) predicts the power t^(-1) here.
We give the needed upper count and the INNER-strip lower count explicitly so that no full-strip bound is silently transferred to a smaller strip.

Let M be the real embedding matrix of the power basis, with columns (beta^j,beta^(-j),Re zeta^j,Im zeta^j), 0<=j<=3.
Define

    delta=1/||M^(-1)||_2,  a=delta/4,
    C_up=(2B/a+2)(2S/a+2)(2/a+2)^2.

Every two distinct embedded order elements are separated in Euclidean norm by at least delta, since their coefficient difference is a nonzero integer vector.
Each half-open grid cube of side a has diameter 2a<delta, so it contains at most one order point.
The box |x_+|<B, |x_-|<S, |Re z|,|Im z|<=r meets at most (2B/a+2)(2S/a+2)(2r/a+2)^2 grid cubes.
Therefore, for every r>=0,

    N(r)=#{x in D:rho(x)<=r}<=C_up(r+1)^2.           (9)

These constants concern this actual rank-four lattice.
Their conditioning is retained, not replaced by a degree-uniform bound.

For the lower count put

    A_+=sum_(j=0)^3 beta^j,  A_-=sum_(j=0)^3 beta^(-j),
    C_bin=(1+2A_+/B)(1+2A_-/S),
    D_in={x in O:|x_+|<B/2, |x_-|<S/2}.

For every integer N>=0, the (N+1)^4 distinct elements sum a_j beta^j, 0<=a_j<=N, have real coordinates in [0,A_+N] times[0,A_-N].
Assign these points to the global half-open rectangular grid with widths B/2 and S/2, based at zero.
The numbers of occupied coordinate cells are at most floor(2A_+N/B)+1 and floor(2A_-N/S)+1, respectively, so at most C_bin(N+1)^2 cells are required.
One cell contains at least (N+1)^2/C_bin elements.
Subtract a fixed one of them from every member of that cell.
The resulting states are distinct, belong to D_in with strict inequalities, and have rho at most 4N, because each of their four coefficient differences has absolute value at most N and |zeta|=1.
For r>=4, taking N=floor(r/4) yields

    #{x in D_in:rho(x)<=r}>=r^2/(16 C_bin).          (10)

The zero difference may be included and does not impair the growing lower bound.
On D_in, the product of triangular factors is greater than 1/4.

**Proposition 2.**
For 0<t<=1/16 the complete mass is finite and satisfies

    1/(64 e C_bin t)<=T_t<=C_up(2+sqrt(pi))/t.       (11)

It is finite for every t>0 and infinite at t=0.
For every t>0, c_t has a continuous probability density C_t on X, and

    C_t(theta)=sum_(x in O) sigma_t(x) chi_(-x)(theta),
    ||C_t||_infinity=C_t(0)=T_t.                     (12)

At t=0, c_0 is purely singular and has no bounded density.

*Proof.*
For t>0, Tonelli and(9) give the complete bound

    T_t<=sum_(x in D) exp(-t rho(x)^2)
       =integral_0^infinity 2tr exp(-tr^2) N(r) dr
       <=C_up[t^(-1)+sqrt(pi)t^(-1/2)+1].            (13)

The equality includes x=0 because the integral from rho(0)=0 equals one.
The three integrals result by expanding(r+1)^2; there is no omitted neutral tail.
For t<=1 this upper bound implies the right side of(11).
If t<=1/16, choose r=t^(-1/2)>=4 in(10).
Every state counted has sigma_t(x)>(1/4)e^(-1).
This proves the lower side of(11).
At t=0, the same inner-strip count proves T_0=infinity.

The summability just proved gives absolute uniform convergence in(12).
Its coefficient at zero is one.
Equality of all Fourier coefficients identifies C_t times Haar with the positive probability c_t from Proposition 1: the uniqueness used here is the same elementary torus fact as in L240, since trigonometric polynomials are uniformly dense in continuous functions.
In particular C_t is nonnegative everywhere.
The triangle inequality bounds its absolute value by T_t, and equality is attained at the identity character.
Thus its essential supremum equals T_t as well, by continuity and positivity of Haar measure on open sets.

At t=0 the parameters for a_0 and b_0 are one-dimensional.
Their sum maps R^2 linearly to X, so c_0 is carried by the countable union of compact two-dimensional Lipschitz images.
The same covering proof as in Proposition 1 makes this carrier Haar-null.
Thus c_0 is a singular probability and cannot have an essentially bounded density.
This also agrees with the nonnegative-coefficient Fejer test in L240 and T_0=infinity.
No assumption of square-integrable singular factors, or of absolute continuity of either factor, appears anywhere in this proof.

<a id="primitive-relaxation-fourier-consequences"></a>
### 4. What the models satisfy, including every finite quotient

For t>0 define the probability pi_t on the discrete actual core by

    pi_t(x)=sigma_t(x)/T_t,  x in D.                 (14)

This is a constructed probability, not an occupation law of the original chain.
It is positive at every actual state, has unique largest atom at zero, and has all finite neutral moments.
The latter assertion follows from(9) and Gaussian decay, by splitting rho into integer shells and summing a polynomial times exp(-t n^2).
Its characteristic function on X is the nonnegative continuous function C_t/T_t, so it satisfies the full additive Fourier positivity constraint, not just finitely many tests.
Its coefficient sequence is also positive definite by Proposition 1 and division by the positive constant T_t.

For explicit quotient scope, let I be any finite-index additive subgroup of O, and project pi_t to G=O/I.
All characters of G lift to X, so every Fourier value of the projected probability is nonnegative and real.
If p_I denotes its masses, finite Fourier inversion gives, for every coset g,

    p_I(0)-p_I(g)
       =|G|^(-1) sum_(chi in Ghat) pi_t_hat(chi)
                                      (1-Re chi(g))>=0,
    p_I(0)>=1/|G|.                                  (15)

The second inequality follows also by averaging the first over g.
Thus every finite quotient, every finite positive-definite Gram test, reciprocal symmetry pi_t(Tx)=pi_t(x), and the exact infinite support are simultaneously present.
Formula(11) gives

    pi_t(0)=1/T_t ->0 as t decreases to0,
    pi_t(K)->0 for every fixed finite subset K of O. (16)

Indeed sigma_t<=1 implies pi_t(K)<=|K|/T_t.
In particular these conditions do not themselves give even a fixed-input upper bound for T_t or a positive lower bound for the distinguished atom.
The measures c_t converge weakly to c_0, as follows either from the explicit random construction or from convergence of all coefficients plus trigonometric approximation.
No assertion of a limiting discrete probability pi_0 is made; its mass escapes every finite subset.

This answers a narrower but complete question than classification of the original critical mean.
On the same primitive quartic actual order and actual infinite core, two purely singular reciprocal dual probabilities can have a bounded convolution with arbitrarily large finite norm, or a convolution with no bounded density (here purely singular), while all the support and positivity data above remain the same.
The theorem does not replace the actual critical radius by an adjustable parameter or assert that these alternatives occur for actual critical laws.

<a id="primitive-original-row-obstruction"></a>
### 5. A single actual row rejects the entire family

The discarded condition can be made explicit with the original probabilities.
Let H_R(x) be the actual first-hit generating function of zero, normalized H_R(0)=1, on all O.
It is B_R of L240.
At a nonzero state it satisfies, by conditioning on the FIRST original digit,

    H_R(x)=R[H_R(beta x-1)/4+H_R(beta x)/2
                                  +H_R(beta x+1)/4]. (17)

Nonnegative first-hit series justify the identity at the critical radius by monotone convergence from subcritical radii.
Its entries are finite and at most one by the actual autocorrelation argument retained in L240.
States from which return is impossible have value zero.
This is also the Fourier-coefficient form of b_R=R (S_beta)_*(w b_R), with w(theta)=cos^2(pi theta(1)) and (S_beta theta)(x)=theta(beta x).
The toral automorphism S_beta is distinct from the scalar strip width S in(1).
It is an equation on the actual order with the original weights; it is not translation invariance or an arbitrary stationary law on D.

For our beta, beta>B.
Indeed beta>17/10 gives beta^2-beta-1>0.
The real necessary return strip rules out return from beta and beta+1; beta-1 is a returning state by(2).
Also1 belongs to D since 1<B and 1<S.
Thus(17) at x=1 is the exact one-edge equation

    H_R(1)=(R/4)H_R(beta-1),
    H_R(beta-1)/H_R(1)=4/R>=2.                       (18)

Here H_R(1)>0 by actual co-return, not by a putative model.
This ratio does not use knowledge of R beyond R<=2 and remains valid with its actual unknown value.
It is a local constraint of the genuine recurrent model; by itself it does not bound its total occupation mass.

For the candidate in(4), write v=zeta+conjugate(zeta)=(1-sqrt(13))/2 and

    Delta=|zeta-1|^2-1=1-v=(1+sqrt(13))/2>0.

The expanding triangular factors can be evaluated exactly:

    B_t(1)=(2-beta)exp(-t/2)>0,
    B_t(beta-1)=beta(2-beta)exp(-t|zeta-1|^2/2),
    B_t(beta)=B_t(beta+1)=0.

Consequently, for EVERY t>=0 and EVERY 0<R'<=2,

    [R' sum_eta p_eta B_t(beta+eta)]/B_t(1)
       =(R'beta/4)exp(-t Delta/2)<=beta/2<1,
    [B_t(1)-R' sum_eta p_eta B_t(beta+eta)]/B_t(1)
       >=1-beta/2>0.                                (19)

The notation R' emphasizes that even allowing any possible critical radius in the full elementary interval cannot fix the defect.
Equivalently B_t(beta-1)/B_t(1)=beta exp(-t Delta/2)<2, in direct conflict with(18).
The factor1/4 of the sole legal successor is essential.
Assigning an unweighted legal-edge equation would erase the actual obstruction.

**Proposition 3.**
None of b_t, t>=0, solves the actual critical weighted eigenmeasure equation for any radius0<R'<=2.
None of the pairs(a_t,b_t) can be the actual limiting pair for this input.
The relative failure at the fixed actual state1 is bounded below by1-beta/2 independently of t.
Therefore even the whole family approaching the singular convolution c_0 is uniformly separated from satisfying this particular normalized row equation.

The proposition follows directly from(19) and equality of Fourier coefficients.
The absolute residual can tend to zero when B_t(1) tends to zero as t tends to infinity, so only the displayed relative statement is asserted.
As t decreases to zero, B_t(1) tends to2-beta>0; in that regime even the absolute residual has a positive fixed-input lower bound.
No inference that an arbitrary small residual globally implies a bounded mean is made.

<a id="primitive-singular-convolution-scope"></a>
### 6. Consequences, changed next gate and self-check

The completed result is a precise obstruction to a proposed package of geometric and Fourier sufficient conditions.
It already uses a fixed composition-primitive Salem unit, its actual full infinite core, complete neutral sums and all finite quotient tests.
It therefore survives the composition normalization in L301 and cannot be dismissed as a radical-copy cost, a finite-support model or an omitted neutral tail.
It is also distinct from the [L247 fixed-box obstruction](../ledger/Yin_L_G0247_v1.md): that result concerns actual return-conditioned paths escaping a fixed box; here the entire actual-state geometry is retained while the original weighted equations are deliberately relaxed and then tested.

The actual quartic is known critically recurrent from L285.
Its critical mean may still be finite or infinite.
Propositions1--3 neither prove one alternative nor exhibit a different actual law on this core.
The bounded and unbounded convolution alternatives are countermodels only to the listed relaxed implications.
In particular T_t is not R F'(R), pi_t is not the critical stationary law, and t does not parameterize an original first-return distribution.
All claims of actual behavior in this draft are confined to the fixed geometry, recurrence premise and the exact first-hit row(18).

The changed next question is to use several original weighted row equations, such as(18), together with positive definiteness and reciprocal pairing to control a COMPLETE neutral tail.
A valid bound must act on the actual solution of those equations at its unknown R, not merely on a probability satisfying all finite quotient tests.
The present family is a concrete control that such a proposed argument must reject.
No finite collection is proved sufficient here.
In particular, excluding this Gaussian-triangular family does not establish compactness of the actual critical occupation laws or an upper bound for mu.

All constants in(9)--(13) are explicitly fixed-input constants.
The degree is four, with two real neutral coordinates; the power t^(-1) reflects this dimension.
No statement is uniform over degree, over small Mahler measure, or over a varying family of primitive units.
There is no new lower bound for unrestricted Mahler measure, no proved all-late overlap bound, and no new general critical-mean theorem.
The G0001 contract remains unresolved and its current execution is paused.


<a id="primitive-singular-convolution-author-freeze"></a>
### Author freeze

At 2026-10-10T07:16 the author completed and froze the entire Sections 1--6, Propositions 1--3 and equations (1)--(19), including source and actual-law boundaries.
The scoped material check passed before this freeze.
No program or numerical experiment was run.
The original author body is held for a separately organized full noncontributor review; no independent verdict or fixed adoption is asserted here.

At 2026-10-10T07:23, the author resolved the noncontributor reviewer's Section4 terminology request: 'unbounded-density convolution' was replaced by 'a convolution with no bounded density (here purely singular)'.
The original phrase could suggest an existing unbounded density although Proposition2 proves singularity at t=0.
No formula, proof or claimed alternative changed.
The complete author body is refrozen after this precise clarification.




## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:04 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Actual quartic input](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) | Fixed irreducible quartic, complete Minkowski embedding and actual original narrow co-return, not a varying-degree theorem. |
| dependency | [Exact actual strict strip](Yin_C_G0400_v1.md#exact-salem-return-strip) | Exact full actual core and reciprocal strip at this quartic with its established narrow-return premise; the inner-strip lower count is proved locally. |
| dependency | [Actual whole-order critical law](Yin_C_G0563_v1.md#critical-convolution-bounded-density-test) | Original weighted equations, reciprocal dual pair, whole-order bounded-convolution iff finite mean; never identification of the constructed relaxed family as an actual law. |
| dependency | [True actual quartic recurrence](Yin_C_G0526_v1.md#quartic-critical-recurrence-and-sextic-approximation) | Only F(R)=1 at the actual unknown critical radius, with mean unresolved; no R=exp(m) substitution. |
| support | [Composition normalization](Yin_C_G0558_v1.md#canonical-composition-mean-normalization) | Coefficient exponent-gcd primitive boundary and prior radical-cost distinction; no changing-degree premise here. |
| support | [Original entire proof/input](../ledger/Yin_L_G0305_v1.md#complete-retained-proof-and-review) | Whole original Sections1--6/Propositions1--3/equations1--19, every author/source/correction/no-program limit and original R204 input. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:06 |
| status | proved |
| reason | Adopt the entire precise fixed-input relaxed-model result after actual complete Statement and whole Argument SELF, with original UNKNOWN relationship, author/terminology/source and true actual-law boundaries retained. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Actual quartic input](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) | Fixed irreducible quartic, complete Minkowski embedding and actual original narrow co-return, not a varying-degree theorem. |
| dependency | [Exact actual strict strip](Yin_C_G0400_v1.md#exact-salem-return-strip) | Exact full actual core and reciprocal strip at this quartic with its established narrow-return premise; the inner-strip lower count is proved locally. |
| dependency | [Actual whole-order critical law](Yin_C_G0563_v1.md#critical-convolution-bounded-density-test) | Original weighted equations, reciprocal dual pair, whole-order bounded-convolution iff finite mean; never identification of the constructed relaxed family as an actual law. |
| dependency | [True actual quartic recurrence](Yin_C_G0526_v1.md#quartic-critical-recurrence-and-sextic-approximation) | Only F(R)=1 at the actual unknown critical radius, with mean unresolved; no R=exp(m) substitution. |
| support | [Composition normalization](Yin_C_G0558_v1.md#canonical-composition-mean-normalization) | Coefficient exponent-gcd primitive boundary and prior radical-cost distinction; no changing-degree premise here. |
| support | [Original entire proof/input](../ledger/Yin_L_G0305_v1.md#complete-retained-proof-and-review) | Whole original Sections1--6/Propositions1--3/equations1--19, every author/source/correction/no-program limit and original R204 input. |
| review | [Actual whole current SELF](../audits/reviews/Yin_R_G0762_v1.md#primitive-model-whole-self) | Entire Statement and complete original proof, every fixed-input constant/parameter/quotient/weighted-row scope and source/negative limit; SELF only, no M04 independent replacement. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:26 |
| status | proved |
| reason | Adopt the ENTIRE unchanged current Statement and all complete mathematical Arguments after the actual isolated whole review, necessary fixed interfaces and bounded original finite-evidence check where applicable; all original mathematical/source/native/correction/negative scopes and historical checking relationships remain distinct. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Actual quartic input](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) | Fixed irreducible quartic, complete Minkowski embedding and actual original narrow co-return, not a varying-degree theorem. |
| dependency | [Exact actual strict strip](Yin_C_G0400_v1.md#exact-salem-return-strip) | Exact full actual core and reciprocal strip at this quartic with its established narrow-return premise; the inner-strip lower count is proved locally. |
| dependency | [Actual whole-order critical law](Yin_C_G0563_v1.md#critical-convolution-bounded-density-test) | Original weighted equations, reciprocal dual pair, whole-order bounded-convolution iff finite mean; never identification of the constructed relaxed family as an actual law. |
| dependency | [True actual quartic recurrence](Yin_C_G0526_v1.md#quartic-critical-recurrence-and-sextic-approximation) | Only F(R)=1 at the actual unknown critical radius, with mean unresolved; no R=exp(m) substitution. |
| support | [Composition normalization](Yin_C_G0558_v1.md#canonical-composition-mean-normalization) | Coefficient exponent-gcd primitive boundary and prior radical-cost distinction; no changing-degree premise here. |
| support | [Original entire proof/input](../ledger/Yin_L_G0305_v1.md#complete-retained-proof-and-review) | Whole original Sections1--6/Propositions1--3/equations1--19, every author/source/correction/no-program limit and original R204 input. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0786_v1.md#primitive-model-current-independent) | Entire exact current Statement and complete Argument, every original quantified input, complete proof chain/cost, actual finite versus universal evidence, source-depth/contribution/correction/negative limit; real independently reviewed arrangement and exact current bindings in R786. |

