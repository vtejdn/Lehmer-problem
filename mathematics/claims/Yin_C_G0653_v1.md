---
author: Yin
---

# Exact one-pole phase structure and costs of the present Fourier-band contract

Human author Yin.
Phase_bands supplied the actual fixed-band coefficient bound, full cardinality consequence, improved residue constant and coupled cap comparison.
The aligned_energy_lead contributor supplied and checked the exact inside-root count, negative-frequency formulas, signed energy, variation and separate-rank obstruction, and checked the later residue, finite correction and cardinality calculations.
Both are contributors, not independent reviewers.
The work retains the two actual C648 families and all original probability, dimension and source boundaries.
No mathematical program, prime enumeration or numerical experiment is used.

## Statement

Use the EXACT two actual families and full original-window objects of the adopted [C648 statement](Yin_C_G0648_v1.md#statement).
For clarity their common fixed exponent and moving parameters are

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))),
    a_j=min{p prime:p>(j+1)K},
    b_j=min{p prime:p>(K+a_j+3)^2},
    L_j=K+a_j+b_j+2, M_j=floor(a_j/4),
    c_j^square=min{p prime:p>(L_j+1)^2},
    n_j=min{N positive integer:N^11>=(L_j+1)^25},
    c_j^balanced=min{p prime:p>n_j},
    d_j^sigma=c_j^sigma+L_j-3, sigma in{square,balanced}.

In particular K>=16 and K,a_j,b_j are pairwise coprime.
All Haar measures have mass one and Fourier coefficients use the negative exponential convention.
On the three-torus put

    R=(z^K-1)(u-1)(v-1),
    S=(z^K+1)(u-1)(v-1)+(z^K-1)(u+1)(v-1)+(z^K-1)(u-1)(v+1),
    Acal=-(z^2-1)R-zR/2+zS/2,
    Bcal=(z^2-1)R-zR/2-zS/2,
    U=Acal/Bcal off their common zeros, U=0 on those zeros.

For one j, abbreviate a=a_j,b=b_j,L=L_j and define
A(z)=Acal(z,z^a,z^b), B(z)=Bcal(z,z^a,z^b), A_0=A/(z-1)^2 and N_phase=L-2.
The smooth circle extension U_j=A/B has U_j(1)=-1.
Set varphi_j(z)=U_j(z^-1).
The actual polynomial in either family is

    P_j^sigma=(A+z^(c_j^sigma)B)/(z-1)^3.

It is the same actual monic integral irreducible Salem minimal polynomial as C648, with no further cyclotomic factor and log2<m(P_j^sigma)<log4.
The symbol beta_phase below is a root of A_0, not a root or conjugate of P_j^sigma.

### Exact one-pole phase and a sharper aligned estimate

The degree-N_phase polynomial A_0 has EXACTLY ONE root in the open unit disk, counted with multiplicity.
That root beta_phase is simple, real and satisfies

    1/3<beta_phase<sqrt(2)-1.                                 (OP1)

All other N_phase-1 roots of A_0 are outside the closed disk.
There are a finite disk Blaschke product B_in of degree N_phase-1 and abs(eta)=1 such that on the circle

    varphi_j=eta B_in/B_beta,
    B_beta(z)=(z-beta_phase)/(1-beta_phase z).

Write q_neg=abs(B_in(beta_phase))^2.
Then

    0<q_neg<1/32,
    varphihat_j(-r)
       =eta B_in(beta_phase)(1-beta_phase^2)beta_phase^(r-1),
                           EVERY integer r>=1,               (OP2)
    sum_(r>=1)r abs(varphihat_j(-r))^2=q_neg,
    sum_(n in Z)n abs(varphihat_j(n))^2=L-4,
    sum_(n in Z)abs(n)abs(varphihat_j(n))^2=L-4+2q_neg,
    V(varphi_j)=2pi(L-4).                                     (OP3)

V denotes UNNORMALIZED angular total variation.
For every positive integer c, the negative-frequency part of the continuous Fejer defect is exactly

    sum_(r>=1)min{r/c,1}abs(varphihat_j(-r))^2
       =q_neg(1-beta_phase^(2c))/c.                            (OP4)

For c=c_j^sigma use theta_l=2pi l/c and the ACTUAL interpolant

    Fej_c(t)=c^-1 abs(sum_(r=0)^(c-1)exp(irt))^2,
    q_j^sigma(exp(i theta))=c^-1 sum_(l=1)^(c-1)
                        varphi_j(exp(i theta_l))Fej_c(theta-theta_l).

Its sample at1 is replaced by0, exactly as in C648.
Keep

    Delta_j^sigma=integral[1-Re(conjugate(varphi_j)q_j^sigma)],
    E_j^sigma=[1+pi L_j(5+2log c_j^sigma)]/c_j^sigma.

Then

    0<=Delta_j^sigma
       <=[(1+4pi)(L_j-4)+2q_neg+1]/c_j^sigma
       <=Delta_sharp,j^sigma,
    Delta_sharp,j^sigma=[(1+4pi)(L_j-4)+17/16]/c_j^sigma.       (OP5)

The missing-sample cost remains1/c.
The unweighted L1 bound remains E_j^sigma, including its logarithm.
Equation(OP3) implies that the total weighted phase energy cannot be o(L_j).
It does NOT imply a comparable lower bound for the truncated or discrete aligned defect.

### A complete improved finite cyclic cap cost

Write v_n(z)=(1,z,...,z^(n-1))^T.
Let Pi_P be the full original relation projection for ALL d=d_j^sigma coefficient columns of P_j^sigma in the ORIGINAL2d coordinates.
Let Pi_V and k_V be the actual embedded cyclic projection and scalar from C648, with c=c_j^sigma.
Put

    k=1-(2d)^-1 v_(2d)^*Pi_P v_(2d),
    k_V=1-(2d)^-1 v_(2d)^*Pi_V v_(2d),
    K_q=(1-Re(z^c q_j^sigma))/2,
    h_q=1-K_q, h_V=1-k_V,
    psi_tau(s)=(1-(1-s)/tau)_+.

For every0<tau<=1,

    h_V=(c/d)h_q-Fej_c/(2d), 0<=h_V<=h_q,
    0<=psi_tau(k_V)-psi_tau(K_q)
       <=(L-3)/d+Fej_c/(2d tau),                              (OP6)
    ||psi_tau(k_V)-psi_tau(K_q)||_1
       <=min{(L-2)/(2d tau),(L-3)/d+1/(2d tau)}.

The second bound inside the minimum is strictly better for tau<1/2.
Use the actual inverse phase

    V(z,u,v)=U(z^-1,u^-1,v^-1),
    Kcal=(1-Re(wV))/2, F_tau=psi_tau(Kcal),

and define

    eta_partial^sigma(j,tau)
       =[(3L_j-2)/(2d_j^sigma)+4Delta_sharp,j^sigma]/tau
              +(L_j-3)/d_j^sigma+E_j^sigma/sqrt(tau).

Then

    ||psi_tau(k_j^sigma)-F_tau composed with iota_j^sigma||_1
       <=eta_partial^sigma(j,tau),                            (OP7)

where iota_j^sigma(z)=(z,z^a_j,z^b_j,z^(c_j^sigma)).
The difference is bounded by1, so its L^(4/3) norm is at most eta_partial^(3/4).

For EVERY M=M_j>=max{2,c_weight,K},0<tau<=1/64, and finite Gamma in the CLOSED integer box[-M,M]^4, the complete adopted C648 return therefore improves to

    sum_(gamma in Gamma)
       abs(fhat_(j,tau)^sigma(H_j^sigma(gamma))-Fhat_tau(gamma))
       <=8 card(Gamma)^(3/4)
          [eta_partial^sigma(j,tau)^(3/4)
                       +C_return2,K M^-1 tau^-1/8].           (OP8)

Here f_(j,tau)^sigma=psi_tau(k_j^sigma),
H_j^sigma(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j^sigma gamma_3, and the fixed constants are EXACTLY those in C648:

    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity,
    G_K=sqrt(||abs(Acal)^2+abs(Bcal)^2||_infinity),
    c_weight,K=6pi[1+10sum_(l=1)^3 D_l+2(G_K+1)],
    C_smooth,K=3pi[24*64^(3/4)sum_(l=1)^3 D_l+4^(3/4)],
    C_return2,K=2*2048^(3/4)c_weight,K+2C_smooth,K.

Both regularizations, both contact-supported smoothings, all endpoints, empty sets and signed harmonics retain that full scope.
No new width exponent is inferred from the smaller finite budget.

To state the limit of the remaining separate estimate, put delta=(L-2)/(2d).
Exactly,

    integral(k-k_V)=-delta, ||k-k_V||_1>=delta,
    integral(k_V-K_q)=||k_V-K_q||_1=delta,
    integral(k-K_q)=0.                                       (OP9)

Thus a proof that continues to pay the first comparison solely as ||k-k_V||_1/tau retains a budget at least delta/tau.
A proof paying BOTH comparisons by separate global1/tau Lipschitz bounds retains at least2delta/tau.
These are limitations of those stated estimates, NOT lower bounds for the actual composed cap error.
The two means cancel, so coupled cancellation remains a genuine possibility.

### Actual coefficient and cardinality bounds for the current band contract

For the SAME actual fixed-K torus U and every integer k>=1, let

    F_(k,1)(z,u)=integral_T U(z,u,v)^k v dHaar(v).

Then

    ||F_(k,1)||_(L1(T^2))<=64/sqrt(k),
    abs((U^k)hat(p,q,-1))<=64/sqrt(k)
                  for EVERY(p,q) in Z^2.                    (OP10)

The torus law here is actual PRODUCT Haar for the original torus coefficients.
It is not an independence claim for a pushed original circle.

For every integer L_harm>=1 and arbitrary finite sets S_k subset Z^2,1<=k<=L_harm, assume the SAME per-k mass contract used by C638 at m=1:

    sum_((p,q) in S_k)abs((U^k)hat(p,q,-1))>=1/512
                                    for EVERY k.             (OP11)

Then, for their actual four-dimensional selection
Gamma_1={(-p,-q,1,k):(p,q) in S_k,1<=k<=L_harm},

    card(S_k)>=sqrt(k)/32768,
    card(Gamma_1)>=L_harm^(3/2)/49152.                        (OP12)

This allows disconnected or nonrectangular S_k.
It shows that the leading L_harm^(3/2) order cannot be lowered while retaining this per-k m=1 capture contract.
It does not exclude other global, weighted or different-m selections, and it does not prove that8/25 is an optimal width exponent.

### Exact coupled ratio and the unresolved quantitative input

Let A_rel have ALL d columns of the actual P_j^sigma in2d coordinates and G=A_rel^T A_rel.
Set

    G_d(z)=v_d(z)^*G^-1v_d(z)>0,
    h_orig=1-k_j^sigma,
    h_phase=(1+Re(z^c varphi_j(z)))/2.

For every z on the circle,

    h_orig=abs(P_j^sigma(z))^2 G_d(z)/(2d),
    h_phase=abs(z-1)^2 abs(P_j^sigma(z))^2/[4abs(A_0(z))^2].    (OP13)

For every z!=1 this yields, WITHOUT dividing by P,

    h_orig=r_j^sigma(z)h_phase,
    r_j^sigma(z)=2abs(A_0(z))^2G_d(z)/[d abs(z-1)^2]>0.         (OP14)

Thus the relation remains valid at original unit-circle roots of P.
Its cross-multiplied form holds also at1.
The scalar identity implies, at z!=1 and EVERY tau>0,

    abs((1-h_orig/tau)_+-(1-h_phase/tau)_+)
       <=abs(r_j^sigma-1)/max{1,r_j^sigma}<=1.                (OP15)

However r_j^sigma(z)->infinity as z->1, because A_0(1)!=0 and G_d(1)>0.
No all-circle estimate r_j^sigma=1+O(L/d), no quantitative integral control of(OP15), and no new contact error rate follows from the ratio alone.
Obtaining and paying such a coupled estimate is an unresolved input, not a theorem of this material.
All current families still have log2<m(P_j^sigma)<log4; no unrestricted or near-one conclusion follows.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Complete argument

<a id="actual-one-pole-count"></a>
### 1. The exact real phase and unique internal root

The actual A,B cancellation, reciprocal relation and smooth extension are the adopted C172/C648 input.
In particular A_0 has degree N_phase=K+a+b, has nonzero constant term, no circle roots, and is coprime to its reciprocal conjugate A_0^*.
Put

    D_phase(t)=4sin t+cot(Kt/2)+cot(at/2)+cot(bt/2).

Direct division of the actual A,B by zR_0, with R_0=(z^K-1)(z^a-1)(z^b-1), gives

    U_j(exp(it))=(1+iD_phase(t))/(1-iD_phase(t)),
    D_phase'(t)
       =4cos t-[K csc^2(Kt/2)+a csc^2(at/2)+b csc^2(bt/2)]/2
       <=4-N_phase/2<0.                                     (OP16)

The three root sets have exactly one common point, namely1, and every pair intersects only there.
Their union has K+a+b-2=N_phase-2 points.
Every pole has a positive residue in D_phase.
On each successive open arc, D_phase decreases from positive infinity to negative infinity.
The angular phase derivative of U_j is2D_phase'/(1+D_phase^2), so its integral on each arc is-2pi.
Consequently its full integral is-2pi(N_phase-2).

C172's exact rational factorization has N_phase off-circle roots alpha_l, counted with multiplicity.
Each inside-root factor contributes2pi to the phase integral, and each outside-root factor contributes-2pi, by the already proved Poisson derivative calculation.
If r is the inside-root count, equality of the two complete integrals gives

    2r-N_phase=-(N_phase-2), hence r=1.

This uses the actual inside AND outside factors, not a general all-inside assertion.
Because the derivative in(OP16) has one sign, its absolute integral is2pi(N_phase-2).
Inversion of the circle preserves variation, proving the last line of(OP3).

For0<x<1 set

    F_base(x)=x^-1-x-2-sum_(ell in {K,a,b}) x^ell/(1-x^ell).

The exact polynomial identities are

    A=xR_0 F_base, B=-xR_0(1+F_base).                          (OP17)

At x=1/3, the sum is at most3/8 since every ell>=2, whereas x^-1-x-2=2/3.
At x=sqrt(2)-1 the latter quantity is zero and the sum is strictly positive.
Since xR_0(x)<0, A has opposite signs at these two points.
The intermediate value theorem supplies a positive root between them.
The total inside-root multiplicity is one, so it is the unique inside root and is simple.
This proves(OP1).

### 2. Exact negative frequencies, residue and total energy

Reflect all N_phase-1 outside roots and invert the circle exactly as in C648.
The resulting boundary expression is varphi_j=eta B_in/B_beta with degree B_in=N_phase-1.
The sole denominator factor has the real zero beta=beta_phase.
The identity

    B_in(z)/B_beta(z)
       =B_in(beta)(1-beta z)/(z-beta)
          +(1-beta z)[B_in(z)-B_in(beta)]/(z-beta)

has an analytic second term on a neighborhood of the closed disk.
Expand the first term on abs(z)=1 using the convergent geometric series in beta/z.
Its negative-r coefficient is
B_in(beta)(1-beta^2)beta^(r-1), proving(OP2).
The sum of r beta^(2r-2) is(1-beta^2)^-2, so the negative weighted energy is exactly q_neg.
The phase integral reverses sign under inversion.
Differentiated Fourier orthogonality consequently gives
sum_n n abs(varphihat_j(n))^2=N_phase-2=L-4.
Adding twice the negative weighted energy proves the total-energy identity in(OP3).
All series and differentiated series converge at this fixed smooth rational input.

Equation(OP17) and the real reciprocal symmetry give the rational identity

    varphi_j=B/A=-1-1/F_base.

At beta the residue is-1/F_base'(beta)>0, with

    -F_base'(beta)
       =beta^-2+1+sum_(ell in {K,a,b})
                           ell beta^(ell-1)/(1-beta^ell)^2.

Comparing this residue with eta B_in(beta)(1-beta^2) proves

    abs(B_in(beta))
       =1/{(1-beta^2)[beta^-2+1+
             sum_ell ell beta^(ell-1)/(1-beta^ell)^2]}
       <beta^2/(1-beta^4)<1/(4sqrt(2)).                        (OP18)

The final inequality uses beta<sqrt(2)-1 and the increasing function x^2/(1-x^4) on(0,1).
At x=sqrt(2)-1 its value is exactly1/(4sqrt(2)).
The residue is nonzero, so0<q_neg<1/32.

To prove(OP4), put u=beta^2 and sum the geometric identity

    (1-u)^2 sum_(r>=1)min{r/c,1}u^(r-1)=(1-u^c)/c.

This follows by splitting at r=c and differentiating the finite geometric sum; the r=c endpoint has weight1 in both expressions.
Multiplication by q_neg proves the claim.

C648's continuous aligned defect is at most the total weighted energy divided by c.
Its quadrature price is at most2V(varphi_j)/c, and its actual omitted sample costs1/c.
Substituting(OP3) and(OP18) proves(OP5).
Since L-4<=the total energy<L-4+1/16, refining that total energy itself cannot produce o(L).
The min{abs(n)/c,1} truncation and the possible quadrature cancellation prevent any converse lower bound for Delta from this calculation.

<a id="contact-finite-correction-and-separate-cost"></a>
### 3. Improved finite correction and the exact separate-rank limitation

The full original C648 cyclic identity gives

    k_V-K_q=((d-c)/(2d))(1+Re(z^c q_j^sigma))+Fej_c/(2d).

Because h_q=(1+Re(z^c q_j^sigma))/2 and d-c=L-3, it rearranges to the first line of(OP6).
The bounds0<=h_V<=h_q follow from the projection range and the nonnegative displayed correction.

For0<a<=1,x>=0 and F_tau(x)=(1-x/tau)_+, direct consideration of
x<=tau, tau<x<tau/a and x>=tau/a gives

    0<=F_tau(ax)-F_tau(x)<=1-a.

Apply this with a=c/d and x=h_q.
The further displacement from(c/d)h_q to h_V costs at most Fej_c/(2d tau) by global Lipschitz continuity.
This proves the pointwise inequality(OP6).
Its integral uses the normalized Fejer mass one.
The other bound inside the minimum is the exact original L1 correction(L-2)/(2d) followed by1/tau Lipschitz continuity.
Their difference, old minus new, equals(L-3)(1-2tau)/(2d tau), positive for tau<1/2.

Keep the full existing original-to-cyclic error(3L-3)/(2d tau).
Use the improved finite correction, then the C648 pointwise aligned cap comparison with Delta_sharp and the unchanged E/sqrt(tau).
Adding gives exactly(OP7), including the1/(2d tau) part of the finite correction.
Every scalar function still lies in[0,1], so the L^(4/3) bound follows.
The remaining two joint-shell regularizations and two contact-supported smoothings are unchanged.
Applying the entire C648 finite weak Fourier theorem proves(OP8), including empty sets and all signed indices.
This changes a paid term, not the original family, dimension or probability law.

To locate the limitation of the separate estimate, use the ACTUAL ranks

    rank Pi_P=d, rank Pi_V=c-1.

The normalized identity integral vv^*=I_(2d) gives
integral k=1/2 and integral k_V=1/2+(L-2)/(2d).
Also q_j^sigma has Fourier degree at most c-1, hence integral K_q=1/2.
The correction k_V-K_q is nonnegative, so its L1 norm equals delta.
The first L1 norm is at least the absolute value delta of its mean.
This proves(OP9) and both stated limitations of the global Lipschitz triangle budgets.
It does not rule out cancellation after combining the comparisons or composing the cap.
In particular the new(OP6) already avoids applying that global Lipschitz cost to the whole second difference.

<a id="actual-torus-density-and-band-cardinality"></a>
### 4. The true z-law, coefficient envelope and full per-k support count

Use the actual regular-coordinate formula from C629/C638,

    D=i[b_K(theta)+x(t)],
    b_K(theta)=-4sin theta-cot(Ktheta/2),
    x(t)=-cot(t/2).

Under independent probability Haar in the actual z,u torus coordinates, x has density1/[pi(1+x^2)].
This follows directly by its angular substitution.
To bound the actual b_K law, partition the z circle into its K successive cotangent branches and put y=-cot(Ktheta/2).
Each branch has measure dy/[Kpi(1+y^2)].
On that branch

    b_K=y-4sin theta(y),
    db_K/dy=1-8cos theta/[K(1+y^2)]>=1/2,

since the actual K>=16.
The map is strictly increasing onto the real line.
Also abs(b_K-y)<=4 implies
1+b_K^2<=33(1+y^2).
Changing variables on every branch and summing therefore gives the ACTUAL density bound

    density_(b_K)(s)<=66/[pi(1+s^2)].                         (OP19)

No replacement of the actual b_K law by a uniform or exact Cauchy law, and no independence on an original pushed circle, has been presumed.
Only the specified product Haar for the torus coefficient is used.

Convolving with the independent x gives for d_real=b_K+x

    density_(d_real)(s)<=132/[pi(s^2+4)].                     (OP20)

The exact rational integral behind this is
integral_R dt/[(1+t^2)(1+(s-t)^2)]=2pi/(s^2+4), the same elementary Cauchy convolution identity already proved in C629.
The factor pi^-2 from the two probability densities is retained.

At m=1 the exact finite coefficient formula from C638 simplifies, for every k>=1, to

    F_(k,1)=(-1)^k 4kD^(k-1)/(D+2)^(k+1).                    (OP21)

It has the continuous rational meaning at D=0, including k=1.
The regular-coordinate exclusions are Haar null and the original bounded U definition is retained.
Thus(OP20) bounds its true L1 norm by132/pi times

    integral_R 4k abs(s)^(k-1)/(s^2+4)^((k+3)/2) ds
       =(k/2) integral_0^1 t^(k/2-1)sqrt(1-t)dt.              (OP22)

For a=k/2>0, the density a t^(a-1) on(0,1) has mass one.
Cauchy--Schwarz bounds the last expression by
sqrt(a integral_0^1 t^(a-1)(1-t)dt)=1/sqrt(a+1).
Therefore

    ||F_(k,1)||_1
       <=132/[pi sqrt(k/2+1)]
       <=132sqrt(2)/(pi sqrt(k))<64/sqrt(k).

For the last elementary constant, pi>3 and sqrt(2)<16/11 suffice.
Fubini and the triangle inequality bound every Fourier coefficient of F_(k,1) by its L1 norm.
These coefficients are exactly(U^k)hat(p,q,-1), proving(OP10).

Now assume(OP11).
Every selected coefficient is at most64/sqrt(k), so
1/512<=64 card(S_k)/sqrt(k).
The resulting individual bound is the first line of(OP12).
The fourth coordinate is k, so sets belonging to different k never overlap in Gamma_1.
Finally the increasing function sqrt(x) gives
sum_(k=1)^L_harm sqrt(k)>=integral_0^L_harm sqrt(x)dx=(2/3)L_harm^(3/2).
This proves the complete count in(OP12).

C638's actual m=1 band satisfies(OP11) for every selected harmonic.
Thus a mere change of shape or narrower radius cannot reduce its leading harmonic-cardinality power while keeping the same mass requirements.
A different capture contract, simultaneous weighted selection or other phase-band mechanism remains possible.
No general Fourier-support optimality or width threshold is proved.

<a id="coupled-original-ratio-and-open-control"></a>
### 5. An exact coupled identity and its remaining cost

The actual finite inverse-Gram identity was read in [C592v2](Yin_C_G0592_v2.md#residual-laurent-square-identity).
Its currently selected entire adoption is SELF; that historical relationship and its unrelated native examples are not upgraded here.
Only its elementary identity is used, and the needed special case is immediate:
A_rel^*v_(2d)=P v_d on the circle, because the original coefficient matrix is real, so the projection formula gives
1-k=abs(P)^2v_d^*G^-1v_d/(2d).
This proves the first line of(OP13) in the actual full window.

On the circle abs(A)=abs(B), varphi=B/A and
A+z^cB=(z-1)^3P.
Consequently

    abs(A+z^cB)^2=4abs(A)^2 h_phase.

Since A=(z-1)^2A_0 and A_0 never vanishes on the circle, cancellation gives the second line of(OP13), with its smooth value also at1.
Comparing the TWO identities after multiplication, rather than dividing by P, proves(OP14).
Its cross-multiplied form at1 follows by continuity.
Both G_d and abs(A_0)^2 are continuous and strictly positive at1, which proves the claimed divergence of r_j^sigma there.

For r>=1, the maximum over x>=0 of
abs((1-rx/tau)_+-(1-x/tau)_+) is1-1/r.
For0<r<=1 the corresponding maximum is1-r.
These two direct scalar cases prove(OP15), independently of tau.
They isolate a possible coupled proof obligation without supplying its missing uniform integral estimate.
In particular a global ratio-close-to-one assertion is false because of the behavior at1.
No fixed-input Toeplitz limit, generic model space or Clark-measure analogy is substituted for the actual finite inverse Gram.

<a id="reuse-scope-and-exact-boundaries"></a>
### 6. Reuse scope and exact boundaries

The focused phase-band screen found the actual C629/C638 formulas and the C648 aligned proof; their existing results are not recounted as new logarithm removal.
The required classical Poisson identity, differentiated coefficient calculation and signed-factor conventions retain the exact C172, L264 and GMR18-U001 bounded attribution.
The actual Cauchy convolution in(OP20) is the fixed elementary integral from C629v3; all new density changes and normalizations are proved explicitly here.
The root count, residue, geometric negative spectrum, contact correction and per-k cardinality result are local deductions about those actual objects.

A further bounded local screen read C143's finite-projection scope and C479/CRW08-U001's distinct finite Blaschke compression lead.
Neither supplies the uniform ratio control needed in Section5.
Their unrelated H4 examples, original source proof depths and fixed-input limits are not mathematical inputs here.
No external absence, priority or novel general model-space theorem is asserted.

This result improves an actual finite cap budget and fixes two precise limitations of the present estimates.
It does not prove a lower bound for the full original cap error, force all possible coefficient selections to have the same cost, settle the pure endpoint, improve the currently adopted degree exponent, or reach a family with small positive total Mahler measure.

## Assessment history

### Decision one-pole-and-band-contract-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:11 |
| status | open |
| reason | Register exact one-interior-root structure, complete negative Fourier spectrum and sharp energy/variation, a smaller fully paid finite cyclic cap cost, the actual per-k m1 coefficient/cardinality bound, and the exact coupled inverse-Gram identity with its explicit unresolved quantitative control. Phase_bands and aligned_energy_lead are contributors. Fresh independent whole review is required. No actual full cap-error lower bound, all-band optimality, new degree exponent, unweighted log removal, near-one family or unrestricted conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | OP1--OP15 with both actual C648 families, exact original2d and Haar conventions, phase root distinction, all frequencies/parameters, full finite return and scoped cardinality contract, ratio identity and explicit unresolved control. |
| argument | [Complete argument](#complete-argument) | OP16--OP22 and all root/phase/residue/geometric sums, original cyclic and rank means, true z-law change of variables, exact m1 integral and entire selected count, and no-P-division original Gram identity. |
| dependency | [Adopted actual aligned-return input](Yin_C_G0648_v1.md#decision-whole-reviewed-2026-10-23) | Both exact source-certified polynomial families, full original2d matrix identities, all aligned quadrature and missing-sample costs, unchanged E, full five-cost return, exact constants and prior source scopes. |
| dependency | [Actual phase factorization](Yin_C_G0172_v1.md#moving-cubic-phase-variation) | Complete common-factor removal, reciprocal A0 relation, off-circle roots with multiplicities and signed Poisson integral, inverse sampling orientation and smooth value at1. |
| dependency | [Actual phase power and band proof](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Exact finite coefficient formula and its m1 specialization, fixed-K regular coordinates and each-k m1 mass contract; no larger optimality claim. |
| dependency | [Exact Cauchy convolution](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | The fully proved rational real-line integral and probability normalization; the current b_K density is established here. |
| dependency | [Complete finite weak return](Yin_C_G0641_v2.md#combined-argument) | Both regularizations, both smoothings, finite weak Fourier proof and closed-box scope as reused with both actual laws in C648; no cost is removed. |
| dependency | [Finite inverse-Gram identity](Yin_C_G0592_v2.md#residual-laurent-square-identity) | Only the full actual coefficient-projection identity, directly rederived here; current SELF and historical source/native limits remain unchanged. |
| support | [Finite Blaschke attribution](../audits/literature/GMR18/Yin_U001.md#gmr18-u001) | Existing exact Poisson logarithmic derivative and limited2016 author-manuscript passage account; no new original-source proof audit. |
| support | [Classical weighted coefficient calculation](../ledger/Yin_L_G0264_v1.md#exact-blaschke-two-moment-budget) | Existing differentiated orthogonality and geometric-series normalization, with the current one-pole extensions proved here. |
| support | [Reuse and limitations](#reuse-scope-and-exact-boundaries) | Exact screen, separate-estimate versus true-error distinction, per-k contract versus arbitrary support, and unchanged positive total-measure/Task boundaries. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:25 |
| status | proved |
| reason | Adopt the entire OP1--OP22 theorem after main reading of complete C653 and isolated whole R865. The actual one-inner-root phase, every negative frequency and exact signed/absolute energy and variation are proved; the smaller cyclic cap cost is returned through all five original costs. The actual product-Haar density gives the complete per-k m1 cardinality lower bound, confined to that capture contract. The full original inverse-Gram ratio is exact without dividing by P and diverges near1, leaving quantitative coupled control open. Both actual2d families, positive total-measure range, root/source/SELF boundaries and every limitation remain. No new degree exponent, general support optimum, near-one family or unrestricted completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | OP1--OP15 with both actual C648 families, exact original2d and Haar conventions, phase root distinction, all frequencies/parameters, full finite return and scoped cardinality contract, ratio identity and explicit unresolved control. |
| argument | [Complete argument](#complete-argument) | OP16--OP22 and all root/phase/residue/geometric sums, original cyclic and rank means, true z-law change of variables, exact m1 integral and entire selected count, and no-P-division original Gram identity. |
| dependency | [Adopted actual aligned-return input](Yin_C_G0648_v1.md#decision-whole-reviewed-2026-10-23) | Both exact source-certified polynomial families, full original2d matrix identities, all aligned quadrature and missing-sample costs, unchanged E, full five-cost return, exact constants and prior source scopes. |
| dependency | [Actual phase factorization](Yin_C_G0172_v1.md#moving-cubic-phase-variation) | Complete common-factor removal, reciprocal A0 relation, off-circle roots with multiplicities and signed Poisson integral, inverse sampling orientation and smooth value at1. |
| dependency | [Actual phase power and band proof](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Exact finite coefficient formula and its m1 specialization, fixed-K regular coordinates and each-k m1 mass contract; no larger optimality claim. |
| dependency | [Exact Cauchy convolution](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | The fully proved rational real-line integral and probability normalization; the current b_K density is established here. |
| dependency | [Complete finite weak return](Yin_C_G0641_v2.md#combined-argument) | Both regularizations, both smoothings, finite weak Fourier proof and closed-box scope as reused with both actual laws in C648; no cost is removed. |
| dependency | [Finite inverse-Gram identity](Yin_C_G0592_v2.md#residual-laurent-square-identity) | Only the full actual coefficient-projection identity, directly rederived here; current SELF and historical source/native limits remain unchanged. |
| support | [Finite Blaschke attribution](../audits/literature/GMR18/Yin_U001.md#gmr18-u001) | Existing exact Poisson logarithmic derivative and limited2016 author-manuscript passage account; no new original-source proof audit. |
| support | [Classical weighted coefficient calculation](../ledger/Yin_L_G0264_v1.md#exact-blaschke-two-moment-budget) | Existing differentiated orthogonality and geometric-series normalization, with the current one-pole extensions proved here. |
| support | [Reuse and limitations](#reuse-scope-and-exact-boundaries) | Exact screen, separate-estimate versus true-error distinction, per-k contract versus arbitrary support, and unchanged positive total-measure/Task boundaries. |
| review | [Independent entire one-pole and band-contract finding](../audits/reviews/Yin_R_G0865_v1.md#one-pole-band-contract-whole-independent-finding) | Whole OP1--OP22 and Sections1--6, all actual family/phase/finite costs and signed frequencies, true product-Haar density and entire per-k contract, full original Gram/root endpoints and exact unresolved limits, with all inherited source and review depths retained. |

