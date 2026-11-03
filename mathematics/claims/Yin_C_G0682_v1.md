---
author: Yin
---
# Actual two-factor Salem caps at the inverse-square shrinking-width scale

Human author Yin.
Root supplied the two-factor actual family and the complete TF1--TF7 candidate.
The paid_comparison contributor checked the source applicability, full original window, smooth interpolation, pole absorption, every translated law, finite curvature band and complete shrinking-width return, and supplied the explicit derivative onset and cutoff constants below.
Both are mathematical contributors; this initial open record requires fresh isolated whole review.

This family differs from the weighted three-factor and four-factor families retained elsewhere.
No fixed family is replaced.
The proof uses the [accepted MS05 construction interface](../audits/literature/MS05/Yin_U001.md#ms05-arbitrary-distinct-prime-construction), the finite mechanisms of [C171](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer), [C172](Yin_C_G0172_v1.md#moving-cubic-original-l1-return), [C663](Yin_C_G0663_v1.md#statement) and [C637](Yin_C_G0637_v1.md#complete-argument), with every changed input rechecked below.
The oscillatory step uses only the elementary first-derivative integration-by-parts mechanism retained in [C398](Yin_C_G0398_v1.md#paid-oscillatory-moment-decay) and attributed at [Tao26-U001](../audits/literature/Tao26/Yin_U001.md#tao26-u001).
No stationary-phase expansion, Beurling--Helson theorem, uninspected source extension, prime enumeration or numerical experiment is an input.

## Statement

### Actual family and full original projection

Fix the ACTUAL even integer

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))).

For every integer j>=4K let c=c_j be the least rational prime greater than (j+1)K.
Set L=K+2 and

    Q(z)=(z^2-1)(z^K-1)(z^c-1)
          -(z/2)[(z^K+1)(z^c-1)+(z^c+1)(z^K-1)],
    P(z)=Q(z)/(z-1), d=c+K+1=c+L-1.

Then P is the ACTUAL monic integral irreducible Salem minimal polynomial, with even degree d, trace 0, and no further cyclotomic factor.
Its exterior root beta satisfies

    (1+sqrt(5))/2<beta, beta+beta^(-1)<=3, beta<3.

In particular its total logarithmic Mahler measure stays between log((1+sqrt(5))/2) and log 3.
This is not a near-one construction.

Use all d columns P,zP,...,z^(d-1)P in the ORIGINAL 2d coefficient coordinates.
Write A_rel for that real matrix,

    G=A_rel^t A_rel, Pi=A_rel G^(-1)A_rel^t,
    v_N(z)=(1,z,...,z^(N-1))^t,
    h_orig(z)=v_(2d)(z)^*Pi v_(2d)(z)/(2d),
    G_d(z)=v_d(z)^*G^(-1)v_d(z),
    f_tau(z)=(1-h_orig(z)/tau)_+.

All Haar measures have mass one, Fourier coefficients use negative exponentials, and

    W_*(f)=sum_(n in Z,n!=0)|fhat(n)|.

For each fixed member and 0<tau<=1/64, f_tau has finite Wiener norm and takes value 1 at every circle root of P.
Its mean is at most 1/2, so its actual contact-minus-mean margin is at least 1/2.

### Fixed phase and complete comparison costs

Define the FIXED degree-L integral polynomials

    A(z)=-(z^2-1)(z^K-1)+z,
    B(z)= (z^2-1)(z^K-1)-z^(K+1).

They satisfy Q=A+z^c B, A+B=-z(z^K-1), A(1)=1 and B(1)=-1.
They have no common zero and neither has a unit-circle zero.
The fixed smooth unimodular phases are

    U(z)=A(z)/B(z), V(z)=U(z^(-1))=B(z)/A(z)=exp(i psi(t)),
    D(t)=4sin t+cot(Kt/2), z=exp(it),
    U=(1+iD)/(1-iD).

Choose the smooth lift psi(0)=pi.
Its derivative is strictly positive, its winding is K, and

    psi'=-2D'/(1+D^2), 0<psi'<=D_psi<=34K+8<c,
    D_psi=||psi'||_infinity,
    psi'(0)=K,
    psi'(pi/K)=(K-8cos(pi/K))/(1+16sin^2(pi/K))<K.

The formulas at cotangent poles mean their smooth limits.
Thus psi is nonaffine and has nonzero second derivative on some closed regular interval.

Put

    A_1=sum_(n in Z)|n|*|Vhat(n)|<infinity,
    E_K=2L-1+A_1, epsilon=E_K/c,
    h_phase(z)=(1+Re(z^c V(z)))/2.

The complete original-window comparison is

    ||h_orig-h_phase||_1
       <=(4L-2)/(2d)+A_1/c<=epsilon.                     (TF1)

Every cyclic mode, INCLUDING the sample V(1)=-1, is retained.

Set

    delta_*=[28(1+60pi)]^(-2),
    C_obs=2/delta_*, C_stab=33C_obs+3.

For every tau>0, with F_tau^phase=(1-h_phase/tau)_+,

    ||f_tau-F_tau^phase||_1<=min{1,C_stab epsilon},
    ||f_tau-F_tau^phase||_2<=min{1,sqrt(C_stab E_K/c)}.    (TF2)

The actual ratio has a genuine pole, which is included in these estimates:

    r=h_orig/h_phase=2|A|^2G_d/[d|z-1|^2], z!=1,
    r=u+sigma, u(t)=kappa/[4sin^2(t/2)],
    kappa=4h_orig(1)/(c+K)^2<=4/c^2,
    deg_Fourier sigma<=d+L-2=c+2L-3<3c.

Here r is defined by the displayed positive expression at the other phase contacts; the identity h_orig=r h_phase does not divide by P.
The numerator and sigma are real even, and the pole is not canceled.

On T^2 define

    h(z,w)=(1+Re(wV(z)))/2,
    F_tau(z,w)=(1-h(z,w)/tau)_+,
    iota_c(z)=(z,z^c), H_c(p,k)=p+ck,
    M=floor(c/4), C_sm=3pi sqrt(2)(D_psi+1).

For EVERY 0<tau<=1/64 and finite Gamma subset [-M,M]^2 intersect Z^2,

    sum_(gamma in Gamma)
       |fhat_tau(H_c(gamma))-Fhat_tau(gamma)|
       <=sqrt(card Gamma)
          [sqrt(C_stab E_K/c)+2C_sm M^(-1)tau^(-1/4)].  (TF3)

The corresponding l2 coefficient-vector bound is the same bracket.
The entire CLOSED 2M alias condition is verified.
Both original-circle and torus smoothing errors are included, with all intermediate translated-circle laws treated directly.
There is no phase regularization cost in this globally smooth case.

### Finite curvature band with every constant paid

Fix once a closed regular interval I of length less than 2pi on which |psi''|>=lambda>0.
Choose a nonzero real C^3 periodic bump chi supported strictly inside I.
For any angular function a put I_1(a)=integral_(-pi)^pi |a(t)|dt; all L2 norms below use probability Haar.
Define

    s=||chi||_2^2>0,
    C_osc=(6||chi||_infinity+2I_1(chi'))/(pi sqrt(lambda)),
    C_chi=I_1(chi''')/(2pi),
    A_chi=sum_(r in Z)|chihat(r)|,
    B_der=||chi'||_2+D_psi||chi||_2,
    C_0=max{1,2B_der/sqrt(s),
             [12sqrt(2/5)C_osc C_chi/s]^(2/3)},
    B_band=ceil(2C_0+2), a_band=s/(2C_osc A_chi)>0.

The fixed bump exists, for example by rescaling (1-x^2)_+^4 inside I.
All constants depend only on the fixed phase and that fixed bump.
They do not vary with c, tau or the harmonic k.

For every integer k>=1 and EVERY n in Z, putting g_k=chi V^k gives

    |ghat_k(n)|<=C_osc k^(-1/2).                        (TF4)

The actual finite band satisfies

    sum_(|p|<=B_band k)|(V^k)hat(p)|>=a_band sqrt(k)
                                        for every k>=1. (TF5)

No unbounded-band limit or unpriced cutoff convolution is used.

### Complete support and inverse-square width return

For 0<tau<=1/64 put

    L_tau=floor(1/(4sqrt(tau))),
    Gamma_tau={(-p,k):1<=k<=L_tau, |p|<=B_band k}.

Its size is at most (2B_band+1)L_tau^2.
Its torus Fourier mass satisfies

    sum_(gamma in Gamma_tau)|Fhat_tau(gamma)|
       >=C_mass tau^(-1/4),
    C_mass=a_band/(64sqrt(2)pi)>0.                      (TF6)

Let H=c^2 tau and define

    C_err=sqrt(2B_band+1)/4
                  *max{sqrt(C_stab E_K),16C_sm}.

Whenever H>=4B_band^2, the ENTIRE Gamma_tau lies in the closed box [-M,M]^2 and all original frequencies H_c(Gamma_tau) are distinct and strictly positive.
The fully returned ORIGINAL bound is

    W_*(f_tau)>=tau^(-1/4)
        [C_mass-C_err(H^(-1/4)+H^(-1/2))].               (TF7)

In particular, set

    H_*=max{1,4B_band^2,(4C_err/C_mass)^4}.

For every declared family member and 0<tau<=1/64 with c^2 tau>=H_*,

    W_*(f_tau)>=(C_mass/2)tau^(-1/4).

Consequently, for EVERY positive sequence tau_j tending to zero with d_j^2 tau_j tending to infinity,

    W_*(f_(j,tau_j))->infinity.

For every fixed H>=H_* and all sufficiently large j, tau_j=H/c_j^2 gives the explicit lower bound
W_*(f_(j,tau_j))>=[C_mass/(2H^(1/4))]sqrt(c_j).
The actual degrees satisfy d_j/c_j->1 and c_j<d_j<2c_j.
This is a joint shrinking-width conclusion for this actual bounded-positive-measure family.
It does not assert divergence at a fixed positive width, supply a near-one family or resolve the unrestricted Lehmer Task.

## Argument

### 1. Actual two-factor construction, exact removal and degree

The two-factor MS05 hypersurface has support size at most 12, ambient dimension 3 and squared support diameter 6.
Its sufficient lcm endpoint is ceil(6^3*3^(3/2))<1296.
The fixed K displayed above is a multiple of the corresponding two-factor common exponent: its prime product includes every prime at most 12 and its lcm contains every integer up to that endpoint.
It is even and K>=16.

Every c_j is an odd prime strictly larger than K, hence coprime to K.
The inspected MS05-U001 arbitrary-distinct-eligible-prime proof applies at EVEN q=2, using the same accepted circular-interlacing and torsion-coset inputs.
It gives exactly Q=(z-1)P, the actual monic integral irreducible Salem polynomial, degree c+K+1 and trace 1-q/2=0.
The torsion exclusion removes every further cyclotomic factor; the degree exceeds two, excluding the reciprocal quadratic Pisot alternative.
No optimized degree theorem or uninspected extension of the source is used.

Directly, the half-sum simplifies to z(z^(K+c)-1), so Q is integral and Q'(1)=-(K+c).
Thus the removed root at 1 is simple and P(1)=-(K+c)!=0.
Even degree also follows from c odd and K even.

At the exterior root, the exact rational equation is

    beta-beta^(-1)
       =(1/2)[(beta^K+1)/(beta^K-1)
                    +(beta^c+1)/(beta^c-1)].

The right side is strictly larger than 1, yielding beta>(1+sqrt(5))/2.
Each fraction is at most (beta+1)/(beta-1), yielding (beta-1)^2<=beta and hence beta+beta^(-1)<=3.
This implies beta<3.
All other roots have modulus at most 1, so m(P)=log beta and the stated positive-measure boundary follows.
The existence of arbitrarily large primes makes c_j tend to infinity; no upper prime-gap bound is needed.

### 2. Fixed smooth inverse phase and an explicit derivative ceiling

The displayed A,B expand to Q=A+z^c B.
Their constants are -1,1 and A+B=-z(z^K-1).
A common zero would therefore be zero or a Kth root of unity.
Neither occurs: A(0)=-1 and A(z)=z when z^K=1.

For real-coefficient degree-L reciprocal polynomials, direct reversal gives A^*=-B and B^*=-A.
Thus |A|=|B| on the circle.
A circle zero of either would be common, so neither occurs.
The rational circle phase is smooth and unimodular, with V=U(z^(-1))=B/A and V(1)=-1.

Away from cotangent poles, division by z exp(iKt/2) gives U=(1+iD)/(1-iD).
Here

    D'=4cos t-(K/2)csc^2(Kt/2)<0

because K>=16.
Thus psi'=-2D'/(1+D^2)>0.
Near any pole t_0, D=2/[K(t-t_0)]+O_K(1), and the smooth phase derivative tends to K.
On each of the K intervals between consecutive poles, D decreases from positive infinity to negative infinity and the continuous lift of V increases by 2pi.
Therefore its winding is K and psi(0)=pi defines the stated lift.

For the global ceiling, put x=cot(Kt/2) and b=4sin t.
Then |b|<=4 and

    1+x^2=1+(x+b-b)^2<=34[1+(x+b)^2].

The numerator K(1+x^2)-8cos t in psi' is positive and at most
(34K+8)[1+(x+b)^2].
The pole limits retain the same bound.
Hence D_psi<=34K+8.

The ACTUAL schedule j>=4K gives c>(4K+1)K>34K+8, so c>=D_psi without an unspecified later onset.
It also gives c>L and c>=8.
At t=pi/K the stated derivative is strictly smaller than K, since cos(pi/K)>0.
The smooth derivative is therefore nonconstant; continuity of psi'' supplies an interval I and positive lambda as used in TF4.
One can choose I away from the finitely many cotangent pole locations.

### 3. The original 2d rank comparison and every cyclic sample

The d shifts of P are linearly independent.
Thus G is positive definite and Pi is the rank-d orthogonal projection in the ORIGINAL 2d-dimensional space.
The raw Q shifts have d-1=c+L-2 independent columns.
Because Q=(z-1)P, their range is contained in the original P range with codimension exactly one.

Let S_c e_i=e_(i+1 mod c) and form

    V_c=[A(S_c); B(S_c); 0_(2L-2)-by-c]

in those SAME 2d rows.
No cyclic mode has A=B=0, including omega=1, so V_c has rank c.
Let T_0 be the first c raw Q columns.
For 0<=i<c-L its ith column equals that of V_c.
Only the last L columns can differ, so their projection difference has trace norm at most 2L: the two ranges have at most L missing dimensions over their common intersection, and a difference of orthogonal projections has operator norm at most one.
The other L-2 independent raw columns add exactly that rank.
The final original P correction adds rank one.
Consequently

    ||Pi-Pi_V||_trace<=3L-1.

For every selfadjoint matrix T, |v^*Tv|<=v^*|T|v, and normalized circle integration of v_(2d)v_(2d)^* is the identity.
The entire original L1 error from this projection difference is therefore at most (3L-1)/(2d).

For the cyclic eigenvector (1,omega,...,omega^(c-1))^t the eigenvalue of S_c is omega^(-1).
The upper-right block of Pi_V consequently has multiplier
A(omega^(-1))/B(omega^(-1))=V(omega), with diagonal blocks I_c/2.
Define

    Fej_c(t)=c^(-1)|sum_(r=0)^(c-1)exp(irt)|^2,
    q_c(exp(it))=c^(-1)sum_(omega^c=1)V(omega)Fej_c(t-arg omega).

Finite spectral decomposition gives exactly

    v_(2d)^*Pi_V v_(2d)=c+c Re(z^c q_c(z)).

Every sample occurs; in particular the omega=1 sample is V(1)=-1, not zero.
There is no missing-mode Fejer correction.
The nonnegative function 1+Re(z^c q_c) has mean one, since q_c has frequencies strictly between -c and c and |q_c|<=1.
Thus replacing its normalization c/(2d) by 1/2 costs exactly (L-1)/(2d) in L1.

For a character z^n with 0<|n|<c, full-grid Fejer interpolation is

    (1-|n|/c)z^n+(|n|/c)z^(n-sign(n)c).

Its L1 error is at most 2|n|/c; the constant character is exact.
For |n|>=c the operator is an L-infinity contraction, so the error is at most 2<=2|n|/c.
Three integrations by parts for the FIXED smooth V imply A_1<infinity.
Absolute Fourier summation then gives ||q_c-V||_1<=2A_1/c.
Adding every rank, normalization and interpolation cost proves TF1.
This replaces the old varying-phase logarithmic interpolation estimate only for the new fixed smooth phase.

### 4. Genuine Gram pole and local observability

The exact Gram identity is h_orig=|P|^2G_d/(2d).
Since V=B/A and Q=(z-1)P,

    h_phase=|A+z^cB|^2/(4|A|^2)
           =|z-1|^2|P|^2/(4|A|^2).

Hence the positive ratio expression in the statement is exact without dividing by P.
Its numerator N(t)=2|A|^2G_d/d is real even of degree at most d+L-1.
At t=0 it equals kappa=4h_orig(1)/(c+K)^2>0.
Orthogonal projection gives h_orig(1)<=1 and kappa<=4/c^2.
Writing N as a polynomial in cos t and dividing N(t)-N(0) by 2-2cos t proves that sigma is real even of degree at most d+L-2=c+2L-3<3c.

For any interval of length 2pi/c, the phase Theta(t)=ct+psi(t) has derivative at least c and total increment at most 4pi, since c>=D_psi.
The set (1+cos s)/2<=delta consists of bands of phase length
4arcsin(sqrt(delta))<=2pi sqrt(delta).
The interval meets at most seven such bands, a deliberately conservative bound covering endpoints.
Its contact preimage therefore occupies at most 7sqrt(delta) times its length.

For completeness C663's generic finite reproduction uses
K_n^rep=2Fej_(2n)-Fej_n, whose multipliers are exactly one on [-n,n].
The finite geometric expansion and Cauchy--Schwarz give
||Fej_n'||_1<=2n, hence ||T'||_1<=10n||T||_1 and V(T)<=20pi n||T||_1 for every degree-at-most-n trigonometric polynomial.
These use probability L1 and unnormalized variation.

Partition into c equal cells.
On each cell, the supremum of |T| is at most its cell mean plus its variation.
The preceding contact proportion then gives

    integral_(h_phase<=delta)|T|
       <=7sqrt(delta)[||T||_1+V(T)/c].

For degree at most 3c and delta=delta_*, the right side is at most ||T||_1/4.
On the complement h_phase>delta_*.
It follows that ||T||_1<=C_obs integral h_phase|T|.
This applies to the actual T=sigma-1 and imports no independent phase coordinate.

The pole is paid explicitly.
On I_0={|t|<=pi/c}, the lift psi(0)=pi and c>=D_psi give

    |Theta(t)-pi|<=(c+D_psi)|t|<=2c|t|,
    h_phase<=c^2t^2,
    u<=kappa pi^2/(4t^2).

Thus h_phase u<=pi^2 there.
Its probability length is 1/c.
On the complement, direct integration of that pole bound gives
integral_(I_0^c)u<=kappa(c-1)/4<=1/c.
Consequently integral h_phase u<=(pi^2+1)/c<32/c.

Now h_phase|sigma-1|<=|h_orig-h_phase|+h_phase u, so

    ||sigma-1||_1<=C_obs(epsilon+32/c).

Let eta_r=|r-1|/max(1,r).
It costs at most 1/c on I_0, and at most ||sigma-1||_1+1/c outside.
Since E_K>=1 and epsilon=E_K/c, this yields
integral eta_r<=(33C_obs+3)epsilon.
The elementary scalar inequality

    |(1-rx/tau)_+-(1-x/tau)_+|<=|r-1|/max(1,r)

holds for every r>0,x>=0,tau>0.
Its maximum occurs at x=tau/r when r>=1 and at x=tau when r<=1.
Applying it to the exact actual ratio proves TF2 in L1.
The difference is bounded by one, so its squared integral is no larger than its absolute integral, proving the L2 bound.
The single pole point has zero Haar measure and no neighborhood has been discarded.

### 5. Every translated law, positive smoothing and finite Fourier return

For the translate of the ORIGINAL circle given by
(z,w)=(exp(i(t+alpha)),exp(i(ct+beta_0))), its phase derivative is c+psi'(t+alpha)>=c and its total increment is 2pi(c+K).
For 0<eta<=1 its contact probability is at most

    [(c+K)/c]*(2/pi)arcsin(sqrt(eta))<=2sqrt(eta).

This is obtained by changing the monotone phase variable over its exact integer number of turns.
Under product Haar, conditioning on z gives a uniform w phase and the stronger bound sqrt(eta).
All translations alpha,beta_0 are included.

Along each actual one-coordinate path, clipping a smooth h by (1-h/tau)_+ is absolutely continuous.
On its open contact components the derivative has magnitude at most
D_psi tau^(-1/2) or tau^(-1/2) in the two respective coordinates, and vanishes off contact.
The corners are handled by one-variable absolute continuity and FTC on that path, rather than restricting an ambient almost-everywhere derivative to a singular curve.
The contact bounds above give L2 derivative norms at most
sqrt(2)(D_psi,1)tau^(-1/4) on EVERY intermediate translated original law, and the same bounds on the torus.

For the actual C637 positive kernel, let N_M=floor(M/2)+1 and

    P_M(t)=Fej_(N_M)(t)^2/c_(N_M),
    c_N=(2N^2+1)/(3N).

It is nonnegative, has integral one, is supported in the CLOSED Fourier interval [-M,M], and has first angular moment at most 3pi/M.
These are the exact fixed kernel facts, not a new normalization.

Coordinate FTC and the L2 bounds give a translation difference at most
sqrt(2)tau^(-1/4)(D_psi|a|+|b|).
The integral triangle inequality needed for convolution follows directly by expanding its squared norm as a double integral and applying Cauchy--Schwarz to each inner product.
It is valid here for the bounded functions and probability kernels.
Thus for Q_tau=F_tau*(P_M tensor P_M), BOTH errors

    ||F_tau-Q_tau||_(L2(T^2)),
    ||F_tau composed iota_c-Q_tau composed iota_c||_(L2(T))

are at most C_sm M^(-1)tau^(-1/4).
There is no regularization term.

If |delta_0|,|delta_1|<=2M and delta_0+c delta_1=0, then delta_1=0 because 2M<c, and then delta_0=0.
Finite expansion therefore gives exact coefficient return for every Q supported in [-M,M]^2 and every selected index in that CLOSED box.
It also gives the correct mean under every translated original circle and pairwise distinct returned characters.

For any finite orthonormal character set, expansion of the squared norm of the residual after projection proves finite Bessel directly.
Apply it to the original and torus errors, using exact equality of the selected Q_tau coefficients.
The actual comparison TF2 and the TWO smoothing errors give the l2 coefficient bound in TF3.
Finite Cauchy--Schwarz gives its displayed l1 bound, including the empty set.

### 6. Curvature cutoff and a fully finite power band

The nonaffinity proved in Section 2 supplies the fixed interval I and lambda.
For k>=1 and any integer n, let phi(t)=kpsi(t)-nt on I.
Its derivative is monotone and |phi''|>=k lambda, with constant sign.
Set a=sqrt(k lambda).
The sublevel |phi'|<=a has length at most 2/sqrt(k lambda), so its unnormalized weighted integral has magnitude at most 2||chi||_infinity/sqrt(k lambda).

The complement has at most two intervals, each with |phi'|>=a.
Integrating chi exp(i phi) by parts on each gives two endpoint terms, the chi' integral and the variation of 1/phi'.
The combined endpoint bound is 4||chi||_infinity/a.
Monotonicity bounds the combined reciprocal-derivative variation by 4/a, and the amplitude derivative costs at most I_1(chi')/a.
After adding the sublevel and dividing by 2pi, the result is at most

    [10||chi||_infinity+I_1(chi')]
                    /(2pi sqrt(k lambda))
       <=C_osc k^(-1/2).

Open endpoints follow by bounded limits.
This proves TF4 uniformly in n, including empty sublevels and intervals.
It is the complete elementary first-derivative mechanism attributed to C398/Tao26, with no stationary-phase expansion.

For g_k=chi V^k, the product rule gives
||g_k'||_2<=||chi'||_2+kD_psi||chi||_2<=kB_der.
For R_k=ceil(C_0 k), derivative Bessel gives a Fourier squared tail at most s/4 outside [-R_k,R_k].
The full squared sum is s.
One may verify the latter without an additional completeness premise: three integrations by parts give an absolutely summable Fourier series for this fixed C^3 function, the positive P_M approximate identity identifies that series with g_k uniformly, and finite orthogonality passes to the limit.
Hence

    sum_(|n|<=R_k)|ghat_k(n)|^2>=3s/4,
    sum_(|n|<=R_k)|ghat_k(n)|
                         >=3s sqrt(k)/(4C_osc).

For chi itself, three integrations by parts give
|chihat(r)|<=C_chi|r|^(-3) for r!=0, proving A_chi<infinity.
Absolute Fourier expansion of chi justifies ghat_k=chihat*(V^k)hat.
The portion from |m|>2R_k in the preceding finite sum is bounded, using Parseval ||V^k||_2=1, by

    (2R_k+1)
       [sum_(|r|>R_k)|chihat(r)|^2]^(1/2)
       <=3sqrt(2/5)C_chi R_k^(-3/2).

The last step uses 2R_k+1<=3R_k and
sum_(|r|>R_k)|r|^(-6)<=2/(5R_k^5).
For the smooth V^k the same approximate-identity argument supplies the used Parseval identity, or finite Bessel alone supplies the required upper bound one.

Our explicit choice of C_0 makes this tail at most
s sqrt(k)/(4C_osc) for every k>=1.
The remaining convolution part is at most
A_chi sum_(|m|<=2R_k)|(V^k)hat(m)|.
Since 2R_k<=(2C_0+2)k<=B_band k, subtraction proves TF5 with a_band as stated.
No discarded frequency tail or bump norm remains unpaid.

### 7. Scalar harmonics, every selected frequency and the joint limit

Let b_tau(theta)=(1-(1+cos theta)/(2tau))_+.
Writing theta=pi+x gives support |x|<=2arcsin(sqrt(tau)).
For 1<=k<=L_tau, cos(kx) is nonnegative on the whole support because
2k arcsin(sqrt(tau))<=pi/4.
On |x|<=sqrt(tau), the cap is at least 3/4 and cos(kx)>=1/2.
Therefore its exact scalar coefficient satisfies

    |bhat_tau(k)|>=3sqrt(tau)/(8pi).

With negative-exponential Fourier coefficients, conditioning on w gives EXACTLY

    Fhat_tau(p,k)=bhat_tau(k)*(V^k)hat(p).

The sign in Gamma_tau merely reverses the symmetric p-band.
Using TF5 and
sum_(k=1)^L sqrt(k)>=2L^(3/2)/3,
together with L_tau>=1/(8sqrt(tau)), gives TF6 and its constant.
The latter floor bound holds because 1/(4sqrt(tau))>=2.

The exact cardinality is
B_band L_tau(L_tau+1)+L_tau<=(2B_band+1)L_tau^2.
If H=c^2tau>=4B_band^2 then
B_band L_tau<=B_band/(4sqrt(tau))<=c/8<=M.
Thus the entire Gamma_tau lies in the closed box.
Also tau<=1/64 implies c>=16B_band, so ck-p>0 for every selected index.
The previous closed-box alias check proves distinctness.

The original nonconstant Wiener sum dominates the sum over these positive frequencies.
Subtract TF3 from TF6 and use
sqrt(card Gamma_tau)<=sqrt(2B_band+1)/(4sqrt(tau))
and M>=c/8.
The complete error is at most

    [sqrt(2B_band+1)/4]
       [sqrt(C_stab E_K)c^(-1/2)tau^(-1/2)
                        +16C_sm c^(-1)tau^(-3/4)].

Factoring out tau^(-1/4) gives respectively H^(-1/4) and H^(-1/2).
This is exactly TF7 with the stated C_err.
For H>=H_*, their total error is at most C_mass/2.

For clarity the original cap has finite Wiener norm at each fixed c,tau.
The function h_orig is a nonconstant trigonometric polynomial: it vanishes at circle roots of the actual Salem P while h_orig(1)>0.
Its level set h_orig=tau is finite unless that polynomial is identically constant, which was excluded.
Thus f_tau is continuous and piecewise smooth with derivative of bounded variation; piecewise integration by parts twice gives Fourier coefficients O_(c,tau)(|n|^(-2)).
No uniform value of that bound is needed.
Moreover 0<=h_orig<=1, its mean is trace(Pi)/(2d)=1/2, and for tau<=1 the scalar bound f_tau<=1-h_orig proves its mean is at most 1/2.
At actual circle roots it equals 1, proving the retained contact margin.

Finally d=c+K+1 with fixed K, so d/c tends to 1 and c<d<2c.
Every sequence in the statement therefore has H=c^2tau tending to infinity and eventually meets all support and width conditions.
The lower bound tends to infinity because tau tends to zero.
For fixed H>=H_* the same bound gives the displayed sqrt(c) estimate once H/c^2<=1/64.
All conclusions concern this new actual two-factor family, its full original degree/window and the stated joint width regime.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:46 |
| status | open |
| reason | Register the entire actual two-factor Salem construction and TF1--TF7 inverse-square shrinking-width return, after complete author checking of the accepted source use, original 2d/full-grid comparison, genuine pole absorption, all-translated-law smoothing, finite curvature band and complete support/cardinality costs. Every positive tau_j tending to zero with d_j^2 tau_j tending to infinity has the stated original Wiener divergence. Fresh isolated whole review is required; this is a distinct fixed-positive-measure family, with no fixed-width or unrestricted Lehmer conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual-family and width statement](#statement) | Exact actual q=2 family, all original degrees/roots/projections, TF1--TF7 and constants, finite support and every-sequence joint limit, with all exclusions. |
| argument | [Complete seven-part proof](#argument) | Actual source specialization, no missing cyclic sample, rank-one original removal, fixed smooth interpolation, genuine Gram pole, local absorption, every translated law and path, finite oscillatory band and complete original return. |
| dependency | [Accepted arbitrary-prime source construction](../audits/literature/MS05/Yin_U001.md#ms05-u001) | EVEN q=2 with the actual common multiple K and eligible c; exact sole (z-1) removal, irreducible Salem degree and trace, at the existing source-statement/selected-proof depth. |
| support | [Original cyclic rank mechanism](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Finite shared-column and projection trace-norm mechanism only, rebuilt at the new original 2d, rank c and codimension one. |
| support | [Original phase orientation and L1 return](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Negative-power cyclic orientation, complete same-window normalization mechanism; its old missing-zero sample and logarithmic error are not imported. |
| dependency | [Generic finite observability mechanism](Yin_C_G0663_v1.md#complete-argument) | Exact finite reproduction/variation and scalar cap inequality; new family geometry, pole coefficient, weighted pole cost and absorption premises proved here. |
| dependency | [Exact positive kernel](Yin_C_G0637_v1.md#complete-argument) | Squared-Fejer normalization, closed support, first moment and finite Bessel mechanisms; every new alias and translated-law cost proved here. |
| support | [Elementary oscillatory mechanism](Yin_C_G0398_v1.md#paid-oscillatory-moment-decay) | Monotone first-derivative integration by parts only, with new cutoff, curvature, uniform-frequency and finite-band costs proved in full. |
| support | [Checked classical attribution](../audits/literature/Tao26/Yin_U001.md#tao26-u001) | Existing selected primary first-derivative lemma/IBP attribution; no stationary-phase or higher-type source theorem invoked. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:57 |
| status | proved |
| reason | The entire fixed TF1--TF7 statement and seven-section actual-family proof were directly read, followed by the complete fresh isolated R903. Adopt the new q2 Salem family and full original2d return, every cyclic sample, no-log fixed-phase interpolation, genuine pole and all-width stability, all translated laws, both smoothing costs, complete finite curvature band and inverse-square shrinking-width conclusion. Every positive tau_j tending to zero with actual d_j squared times tau_j tending to infinity has diverging original Wiener norm; the stated fixed-large-H scale is also included. Source inspection depths remain unchanged; fixed-positive-width divergence, optimality, near-one coverage and unrestricted Lehmer completion are not asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual-family and width statement](#statement) | Exact actual q=2 family, all original degrees/roots/projections, TF1--TF7 and constants, finite support and every-sequence joint limit, with all exclusions. |
| argument | [Complete seven-part proof](#argument) | Actual source specialization, no missing cyclic sample, rank-one original removal, fixed smooth interpolation, genuine Gram pole, local absorption, every translated law and path, finite oscillatory band and complete original return. |
| dependency | [Accepted arbitrary-prime source construction](../audits/literature/MS05/Yin_U001.md#ms05-u001) | EVEN q=2 with the actual common multiple K and eligible c; exact sole (z-1) removal, irreducible Salem degree and trace, at the existing source-statement/selected-proof depth. |
| support | [Original cyclic rank mechanism](Yin_C_G0171_v1.md#two-block-circulant-rank-transfer) | Finite shared-column and projection trace-norm mechanism only, rebuilt at the new original 2d, rank c and codimension one. |
| support | [Original phase orientation and L1 return](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Negative-power cyclic orientation, complete same-window normalization mechanism; its old missing-zero sample and logarithmic error are not imported. |
| dependency | [Generic finite observability mechanism](Yin_C_G0663_v1.md#complete-argument) | Exact finite reproduction/variation and scalar cap inequality; new family geometry, pole coefficient, weighted pole cost and absorption premises proved here. |
| dependency | [Exact positive kernel](Yin_C_G0637_v1.md#complete-argument) | Squared-Fejer normalization, closed support, first moment and finite Bessel mechanisms; every new alias and translated-law cost proved here. |
| support | [Elementary oscillatory mechanism](Yin_C_G0398_v1.md#paid-oscillatory-moment-decay) | Monotone first-derivative integration by parts only, with new cutoff, curvature, uniform-frequency and finite-band costs proved in full. |
| support | [Checked classical attribution](../audits/literature/Tao26/Yin_U001.md#tao26-u001) | Existing selected primary first-derivative lemma/IBP attribution; no stationary-phase or higher-type source theorem invoked. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0903_v1.md#two-factor-inverse-square-width-whole-independent-finding) | Whole actual construction, source applicability, original window/pole/translated laws, finite band and every constant, support and sequence quantifier; no old family or uninspected oscillatory theorem is substituted. |
