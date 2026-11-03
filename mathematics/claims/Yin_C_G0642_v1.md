---
author: Yin
---

# Weak four-thirds finite Fourier return and critical sixteen-twenty-fifths widths

Human author Yin.
Root supplied the weak-distribution return proposal and the critical-enlargement consumer.
The phase_bands contributor checked and completed the event-norm, coordinate-path, finite Fourier, support and uniform-width arguments.
Both are contributors, not independent reviewers.
The adopted translated-circle theorem and localized phase-band theorem are used at their exact fixed scopes.
No numerical experiment or new native computation is used.

## Statement

Fix the same even integer K as the actual four-exponent construction,
K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))).
Define psi_tau(s)=max{0,1-(1-s)/tau} for0<tau<=1 and W_*(f)=sum_(h in Z,h!=0)abs(fhat(h)).
Choose the actual primes

    a_j=min{p prime:p>(j+1)K},
    b_j=min{p prime:p>(K+a_j+3)^2},
    c_j=min{p prime:p>(K+a_j+b_j+3)^2},
    ell_j=(K,a_j,b_j,c_j), d_j=K+a_j+b_j+c_j-1.

The exact original monic irreducible Salem input is

    P_j(x)=[2(x^2-1)product_(i=0)^3(x^ell_(j,i)-1)
       -x sum_(q=0)^3(x^ell_(j,q)+1)product_(i!=q)(x^ell_(j,i)-1)]/[2(x-1)^3].

Let A_rel,j be the 2d_j-by-d_j full coefficient matrix of P_j,tP_j,...,t^(d_j-1)P_j.
Set

    R_j=I-A_rel,j(A_rel,j^T A_rel,j)^-1 A_rel,j^T,
    v_j(t)=(1,t,...,t^(2d_j-1))^T,
    k_j(t)=(2d_j)^-1 v_j(t^-1)^T R_j v_j(t).

This is the actual rank-d_j residual projection on the complete original2d_j window.
All Haar measures below have mass one, all Fourier coefficients use exp(-i gamma dot theta), and angular derivatives use radians.
On the three-torus define

    R=(z^K-1)(u-1)(v-1),
    S=(z^K+1)(u-1)(v-1)+(z^K-1)(u+1)(v-1)+(z^K-1)(u-1)(v+1),
    Acal=-(z^2-1)R-zR/2+zS/2,
    Bcal=(z^2-1)R-zR/2-zS/2,
    g=abs(Acal)^2+abs(Bcal)^2, Ncal=2Acal conjugate(Bcal).

Set U=Acal/Bcal off their common-zero set and0 on that set.
For s>0 define r_s=s/(g+s) and U_s=Ncal/(g+s).
On the four-torus put

    g^vee(z,u,v,w)=g(z^-1,u^-1,v^-1),
    r_s^vee(z,u,v,w)=r_s(z^-1,u^-1,v^-1),
    V(z,u,v)=U(z^-1,u^-1,v^-1),
    Kcal=(1-Re(wV))/2, F_tau=psi_tau(Kcal),
    Kcal_s=(1-Re(w U_s(z^-1,u^-1,v^-1)))/2,
    F_(tau,s)=psi_tau(Kcal_s),
    f_(j,tau)=psi_tau(k_j),
    iota_j(z)=(z,z^a_j,z^b_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j gamma_3.

Let nu_4 be four-torus Haar and nu_3 its first-three-coordinate marginal.
For every a in T^4, let mu_(j,a) be the pushforward of original-circle Haar through z to a*iota_j(z).
Define the actual schedule quantities

    L_j=K+a_j+b_j+2, M_j=floor(a_j/4),
    E_j=[1+pi L_j(5+2log c_j)]/c_j,
    epsilon_j=(4L_j-5)/(2d_j)+E_j/2.

Here L_j is distinct from the selected harmonic cutoff L used later.
Set the fixed polynomial constants

    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity, l=1,2,3,
    A_der,K=1+sum_l D_l, C_rel,K=3pi A_der,K,
    c_res,K=2C_rel,K, B_g=32^(3/4),
    C_weak,K=24pi(B_g+1)A_der,K,
    C_return,K=(8+B_g)c_res,K+2C_weak,K.

Use the adopted positive finite kernel, with angular representatives in[-pi,pi],

    Fej_N(t)=N^-1 abs(sum_(l=0)^(N-1)exp(ilt))^2,
    J_N=Fej_N^2/[(2N^2+1)/(3N)],
    P_M=J_(floor(M/2)+1), integer M>=2.

It is nonnegative of mass one, has Fourier support in the CLOSED interval[-M,M], and has first moment at most3pi/M.
Write Q_(tau,s) for convolution of F_(tau,s) with the four-coordinate product of P_M.

### The complete finite return

For every actual j with M=M_j>=max{2,c_res,K}, set

    rho=(c_res,K/M)^2.

For a probability measure mu define, on measurable complex functions modulo almost-everywhere equality,

    N_(4/3,mu)(h)
       =sup_(E measurable,mu(E)>0) mu(E)^(-1/4) integral_E abs(h)dmu.

It is a norm on its finite-valued domain.
Let N_circle use ordinary circle Haar and N_torus use nu_4.
For EVERY width0<tau<=1/64, the complete pair of errors satisfies

    N_circle(f_(j,tau)-Q_(tau,rho) composed with iota_j)
       +N_torus(F_tau-Q_(tau,rho))
       <=(epsilon_j/tau)^(3/4)+C_return,K/(M tau)
       =:E_weak(j,tau).                                         (W1)

For EVERY finite Gamma subset of[-M,M]^4 intersect Z^4, let N_Gamma=card(Gamma).
Then

    sum_(gamma in Gamma)
       abs(fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma))
       <=8N_Gamma^(3/4) E_weak(j,tau).                           (W2)

The empty-set value is zero.
All signs and all fourth-coordinate harmonics, including zero, are allowed.
The cardinality is the entire supplied set, and the original characters are distinct by the closed2M difference theorem.
No strong ell4 bound, infinite coefficient-sum comparison, or unregularized negative moment is asserted.

### The complete localized support

Use the exact adopted local phase definitions

    D_0(z)=-2(z-z^-1)+(z^K+1)/(z^K-1),
    b(z)=Im D_0(z), z_0=exp(i pi/K),
    C_loc,K=ceil(32000pi+1024pi(K+4)).

For positive integers k,m let t_(k,m) be the unique value in(-pi,0) satisfying

    -cot(t_(k,m)/2)=16sqrt(km)-b(z_0).

Near this value put phi_z(t)=arctan(2/[b(z)-cot(t/2)]) and define the actual integer center

    n_(k,m)=floor((k+m)phi_(z0)'(t_(k,m))+1/2).

The adopted theorem gives abs(n_(k,m))<=14(k+m).
For positive integers L,J set

    R_z(L,J)=ceil(C_loc,K J^(1/3)),
    R_u(L,J)=ceil(C_loc,K sqrt(L)J^(5/6)),
    G_(L,J)={(-p,-q,m,k): 1<=k<=L, 1<=m<=J,
                    abs(p)<=R_z(L,J), abs(q-n_(k,m))<=R_u(L,J)},
    N_sel=LJ(2R_z(L,J)+1)(2R_u(L,J)+1),
    A_sel,K=9(C_loc,K+1)^2,
    C_pay,K=8A_sel,K^(3/4).

Thus N_sel<=A_sel,K L^(3/2)J^(13/6).
For0<tau<=1/64 use L=L_tau=floor(1/(4sqrt(tau))).
If the COMPLETE closed-box conditions

    R_z(L,J),J,L<=M,
    14(L+J)+R_u(L,J)<=M                                         (W3)

hold, then all original frequencies of G_(L,J) are distinct and strictly positive, and

    W_*(psi_tau(k_j))
       >=3log(J+1)/(32768pi)-8N_sel^(3/4)E_weak(j,tau).           (W4)

In particular the whole subtracted term is at most

    C_pay,K tau^(-9/16)J^(13/8)
       [(epsilon_j/tau)^(3/4)+C_return,K/(M tau)].               (W5)

The centers, both closed endpoints and every band are charged.

### Uniform critical widths with arbitrary diverging enlargement

There exist j0(K) and C_crit,K>0 such that for EVERY j>=j0(K), EVERY real H and EVERY width tau satisfying

    16<=H<=M_j^(16/25)/64,
    M_j^(-16/25)H<=tau<=1/64,                                  (W6)

the choice J=floor(H^(1/4)), L=L_tau and the radii just defined satisfies every condition(W3).
Moreover,

    W_*(psi_tau(k_j))
       >=3log H/(131072pi)
          -C_crit,K[H^(-37/32)
               +M_j^(-33/50)H^(-29/32)(1+log M_j)^(3/4)].        (W7)

The onset is uniform over all H and tau in(W6).
Consequently EVERY actual sequence tau_j->0 with

    M_j^(16/25)tau_j->infinity

has W_*(psi_(tau_j)(k_j))->infinity, with no prescribed logarithmic factor or monotonicity.
Its eventual entry index may depend on the sequence.
Every fixed strict exponent0<theta<16/25 is a consequence.
Bounded enlargement, the pure critical scale and width optimality are not claimed.
The original full2d_j coefficient dimension, original-circle law, contact-minus-Haar margin at least1/2, finite fixed-j Wiener norms and log2<m(P_j)<log4 family remain unchanged.
This is a sufficient moving-width result, not an unrestricted Task or Mahler-gap conclusion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Complete argument

<a id="finite-weak-fourier-return"></a>
### 1. Accepted inputs and the original finite comparison

The actual [C639 translated-circle theorem](Yin_C_G0639_v1.md#decision-whole-reviewed-2026-10-23) was read at its whole adopted scope.
For every0<s<=1 with M sqrt(s)>=2C_rel,K, it gives

    sup_(a in T^4) integral r_s^vee dmu_(j,a)<=16s^(2/3).         (W8)

The same actual amplitude satisfies integral r_s dnu_3<=8s^(2/3) by [C633v2](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument).
All translations in(W8) matter below; no independent-coordinate replacement is made on the original curve.
The exact [C637 positive kernel](Yin_C_G0637_v1.md#exact-positive-kernel-and-closed-support) supplies the stated closed support and first moment.
Its full definition, finite identities and [bounded source account](Yin_C_G0637_v1.md#source-and-reuse-boundary) are the adopted inputs.

The [C565 original comparison](Yin_C_G0565_v2.md#moving-band-fejer-budget) gives

    integral_T abs(k_j-Kcal composed with iota_j)<=epsilon_j.

The two functions lie in[0,1].
Applying the1/tau Lipschitz scalar map gives a difference bounded by1 with L1 norm at most epsilon_j/tau.
This is an integral estimate, not a pointwise error of size epsilon_j.

The [closed alias theorem](Yin_C_G0565_v2.md#moving-band-exact-alias) gives H_j(eta)!=0 for every nonzero integer eta in[-2M,2M]^4.
Since Q_(tau,rho) has closed support[-M,M]^4, its finite expansion shows

    (Q_(tau,rho) composed with iota_j)hat(H_j(gamma))
       =Qhat_(tau,rho)(gamma) for EVERY gamma in[-M,M]^4.        (W9)

Indeed every potentially matching frequency eta has eta-gamma in the closed difference box, so equality of H_j values forces eta=gamma.
The same theorem makes all H_j(Gamma) distinct.
This argument uses only the finite intermediate polynomial.

### 2. The set-integral norm and a finite Fourier bound

Put p=4/3.
On a probability space the functional N_p in the statement is homogeneous and subadditive by integrating the pointwise triangle inequality on each event.
It is nondegenerate because E equal to the whole space detects a nonzero L1 function.
If N_p is finite, this same choice ensures integrability.
Holder on each event gives N_p(h)<=||h||_(4/3) whenever the latter is finite.

Suppose mu{abs(h)>t}<=(B/t)^(4/3) for every t>0, with0<=B<infinity.
For an event E of measure e>0, layer cake gives

    integral_E abs(h)
       <=integral_0^infinity min{e,B^(4/3)t^(-4/3)}dt
       =4B e^(1/4).                                           (W10)

For B>0 the equality follows by splitting at t=B e^(-3/4).
For B=0 the distribution hypothesis makes h zero almost everywhere.
Thus N_p(h)<=4B.
Conversely N_p(h)<=B gives, on E_t={abs(h)>t} with positive measure,

    t mu(E_t)<=integral_(E_t) abs(h)<=B mu(E_t)^(1/4),

so mu(E_t)<=(B/t)^(4/3).
Null events are harmless.
These implications supply the exact constants used below.

For a parameter measure eta and jointly measurable v(s,x), the integral triangle bound follows by doing the event integral first:

    integral_E abs(integral v(s,x)deta(s))
       <=integral integral_E abs(v(s,x))dmu(x)deta(s)
       <=e^(1/4) integral N_p(v(s,.))deta(s).                   (W11)

Take the supremum over E after dividing by e^(1/4).
All applications here have a finite parameter measure and bounded integrands at fixed positive rho; nonnegative versions also follow directly by Tonelli.
No vector-valued interpolation theorem is needed.

Now let h satisfy the distribution hypothesis of(W10).
For T>0 split h=h_lo+h_hi at abs(h)<=T and abs(h)>T.
Layer cake gives

    ||h_hi||_1
       =T mu{abs(h)>T}+integral_T^infinity mu{abs(h)>t}dt
       <=4B^(4/3)T^(-1/3),
    ||h_lo||_2^2
       <=integral_0^T 2t mu{abs(h)>t}dt
       <=3B^(4/3)T^(2/3).                                     (W12)

Consider any finite orthonormal family of characters of absolute value one.
Finite Bessel follows by expanding the squared norm of h_lo minus its projection onto that family; the remainder has nonnegative squared norm.
Thus the sum of the squared low-part coefficients is at most ||h_lo||_2^2.
For B>0 and coefficient threshold alpha>0 choose

    T=(8B^(4/3)/alpha)^3.

Every high-part coefficient has magnitude at most alpha/2.
Consequently, within any such finite family,

    card{chi:abs(hhat(chi))>alpha}
       <=4alpha^-2 ||h_lo||_2^2
       <=768(B/alpha)^4.                                      (W13)

Arrange the N coefficient magnitudes in decreasing order as a_1,...,a_N.
For a_l>0 use alpha<a_l in(W13) and let alpha increase to a_l to handle ties and the strict threshold.
It follows that a_l<=768^(1/4)B l^(-1/4).
Since

    sum_(l=1)^N l^(-1/4)
       <=1+integral_1^N x^(-1/4)dx
       <=(4/3)N^(3/4), 768^(1/4)<6,

one obtains

    sum_(chi in the entire finite family) abs(hhat(chi))
       <=8B N^(3/4).                                         (W14)

B=0 and the empty family were already handled.
This is a finite distribution argument, with no complete Parseval or infinite coefficient rearrangement assumption.
In particular it applies with B=N_p(h) by the converse implication following(W10).

### 3. Resolved weak derivative envelopes

For M>=max{2,c_res,K}, put rho=(c_res,K/M)^2.
Then0<rho<=1, and EVERY s in[rho,1] meets M sqrt(s)>=2C_rel,K.
Since r_s>=1/2 when g<=s, (W8) yields, for every translation a,

    mu_(j,a){g^vee<=s}<=32s^(2/3), rho<=s<=1.                   (W15)

The torus has the same bound with constant16 and hence also with32.
Define v_rho=(g^vee+rho)^(-1/2).
For0<t<=1 the trivial probability bound is at most32t^(-4/3).
For1<t<=rho^(-1/2), the event v_rho>t lies in g^vee<=s with s=t^-2 in[rho,1].
For t>rho^(-1/2) the event is empty.
Therefore, uniformly over every translated original circle and over the torus,

    mu{v_rho>t}<=32t^(-4/3)=(B_g/t)^(4/3),
    N_(4/3,mu)(v_rho)<=4B_g.                                  (W16)

No sublevel estimate below rho or unregularized critical negative moment was used.

For completeness, the adopted amplitude identities give pointwise

    abs(partial_l g)<=2D_l sqrt(g),
    abs(partial_l Ncal)<=2D_l sqrt(g),
    abs(Ncal)<=g,
    abs(partial_l U_rho)<=4D_l sqrt(g)/(g+rho).

The last inequality follows by differentiating Ncal/(g+rho) and using g/(g+rho)<=1.
Thus the coordinate path envelopes for F_(tau,rho) are

    G_l=2D_l/[tau sqrt(g^vee+rho)], l=1,2,3,
    G_4=1/(2tau).                                               (W17)

Inversion of the first three angles preserves the absolute derivative bounds.
These inequalities also hold at common zeros because rho>0.
Their event norms on all translated original circles and on the torus satisfy

    N_p(G_l)<=8B_g D_l/tau, l=1,2,3,
    N_p(G_4)=1/(2tau),
    sum_(l=1)^4 N_p(G_l)
       <=(8B_g+1/2)A_der,K/tau.                                (W18)

Here the norm of a constant on a probability space equals its absolute value.
The same distribution and event-norm bounds hold for each translated pullback on the original circle, since its distribution is exactly the pushforward distribution just bounded.

### 4. Event-first coordinate paths and both smoothing costs

Fix a base point y in T^4 and a coordinate displacement h in[-pi,pi].
The scalar Kcal_rho is smooth along that entire path because its denominator is positive.
The global Lipschitz inequality for psi_tau and ordinary scalar FTC give, for EVERY pair of path endpoints,

    abs(F_(tau,rho)(y exp(i h e_l))-F_(tau,rho)(y))
       <=integral_(the path of length abs(h)) G_l(y_s)ds.        (W19)

This does not differentiate psi_tau at its clipping corner.
It does not restrict an ambient almost-everywhere derivative to a singular curve.

For the original circle, fix any measurable event E in its base parameter z and integrate(W19) over E first.
At every intermediate coordinate displacement, y_s=a_s*iota_j(z) for a fixed translation a_s.
By(W18), the integral over that SAME base event is at most its measure to the1/4 power times the stated uniform norm bound.
The four-coordinate displacement is telescoped one coordinate at a time; each intermediate point is still such a translation.
Consequently the event norm of its full difference is at most the sum of the four displacement lengths times the four constants from(W18).
This uses the translated pullback on the original base event; no equality between nonlinear means on different curves is assumed.
For the torus, exactly the same event-first argument applies using translation-invariant Haar.

Finally integrate the displacement against the nonnegative product kernel and apply(W11).
Each coordinate has first moment at most3pi/M.
On EACH of the two spaces this proves

    N_p(F_(tau,rho)-Q_(tau,rho))
       <=3pi(8B_g+1/2)A_der,K/(M tau)
       <=C_weak,K/(M tau).                                    (W20)

On the original-circle side the difference in(W20) is pulled back through iota_j.
In fact the same bound holds on every translated original circle.
All functions and parameter integrands are bounded for fixed rho>0, so the event integrations and finite path integrals above are justified directly.

### 5. Both regularizations, the true original error and the full return

Let lambda=rho/tau.
The phase identity U_rho=(1-r_rho)U holds off common zeros.
At a common zero both phases are zero, so the inequality

    abs(F_tau-F_(tau,rho))
       <=min{1,rho/[2tau(g^vee+rho)]}

still holds everywhere.
For p=4/3 and b=g^vee/lambda+tau>0,

    min{1,(2b)^(-p)}<=2/(1+b)<=2/(1+g^vee/lambda).

For b<=1/2 the first right side is at least1.
For b>=1/2, the function(1+b)/(2b)^p decreases, since its logarithmic derivative is1/(1+b)-p/b<0, and its value at1/2 is3/2.
This proves the first inequality, including its endpoint.
It follows that

    abs(F_tau-F_(tau,rho))^(4/3)<=2r_lambda^vee.                 (W21)

If lambda<=1, then lambda>=rho because tau<=1.
Hence(W8) is legal at lambda.
The strong L^(4/3) norms of this difference are at most8sqrt(lambda) on the torus and B_g sqrt(lambda) on the original circle.
By Holder these are also upper bounds for their event norms.
If lambda>1, each event norm is at most1, and their sum2 is bounded by(8+B_g)sqrt(lambda).
Thus in ALL cases their total cost is at most

    (8+B_g)sqrt(lambda)
       =(8+B_g)c_res,K/(M sqrt(tau))
       <=(8+B_g)c_res,K/(M tau).                              (W22)

The last step uses only0<tau<=1.
The s<=1 probability theorem has not been applied outside its domain.

The true original difference from Section1 is bounded by1 with L1 norm at most epsilon_j/tau.
Its strong L^(4/3) norm, and therefore its event norm, is at most(epsilon_j/tau)^(3/4).
Combining this original comparison with the two costs(W22) and the two smoothing costs(W20) gives exactly(W1).
All five terms have been charged.

Set h_circle=f_(j,tau)-Q_(tau,rho) composed with iota_j and h_torus=F_tau-Q_(tau,rho).
By(W9), every coefficient difference in(W2) equals the circle coefficient of h_circle at H_j(gamma) minus the torus coefficient of h_torus at gamma.
The original characters are distinct and orthonormal, as are the torus characters.
Apply(W14) separately to these two ENTIRE finite families, with B equal to their respective event norms, and add.
Equation(W1) now proves(W2), including the empty set.
No use of strong Hausdorff--Young with a merely weak source is made.

<a id="complete-support-and-critical-enlargement"></a>
### 6. The full modulated support and its cost

Use the complete adopted [C638 local band theorem](Yin_C_G0638_v1.md#complete-local-modulation-calculation), with its corrected cotangent sign, actual phase and integer centers.
For every k,m the coefficient mass in the closed shifted rectangle is at least1/(512m).
The chosen common radii dominate its required C_loc,K m^(1/3) and C_loc,K sqrt(k)m^(5/6) for every1<=k<=L and1<=m<=J.
The exact count is N_sel=LJ(2R_z+1)(2R_u+1).
Distinct k,m have distinct fourth and third coordinates, so the bands remain distinct even when their q ranges overlap.

Because each cutoff factor is at least1 and ceil(x)<=x+1,

    R_z<=(C_loc,K+1)J^(1/3),
    R_u<=(C_loc,K+1)sqrt(L)J^(5/6).

Since2R+1<=3R for R>=1, these inequalities prove the complete count stated above.
The bound abs(n_(k,m))<=14(k+m) gives every absolute q coordinate at most14(L+J)+R_u.
Thus(W3) puts the ENTIRE set in the closed original four-box, including both endpoints and the centers.

The adopted scalar-cap harmonics and inverse-phase identity in C638 give total torus coefficient mass at least3log(J+1)/(32768pi) when L=L_tau.
Here L>=2 and1/8<=L sqrt(tau)<=1/4.
By the actual c_j>M_j(1+a_j+b_j) dominance, every selected H_j(gamma) is positive, and by the closed difference theorem they are distinct.
Therefore their original coefficient sum is a sub-sum of W_*.
Subtract the complete(W2) error to obtain(W4).
Finally,

    N_sel^(3/4)
       <=A_sel,K^(3/4)L^(9/8)J^(13/8)
       <=A_sel,K^(3/4)tau^(-9/16)J^(13/8),

where the harmless extra factor4^(-9/8) was enlarged to1.
This proves(W5).
There is no partial-band or sparsity discount.

### 7. All floors, ceilings and critical exponents

Assume(W6), and choose J=floor(H^(1/4)) and L=L_tau.
Then J>=2 and L>=2, while

    L<=M^(8/25)H^(-1/2)/4,
    J<=H^(1/4)<=M^(4/25),
    R_z<=(C_loc,K+1)H^(1/12)<=(C_loc,K+1)M^(4/75),
    R_u<=(C_loc,K+1)sqrt(L)J^(5/6)
       <=[(C_loc,K+1)/2]M^(4/25)H^(-1/24)
       <=(C_loc,K+1)M^(4/25).                                 (W23)

All ceiling constants are included.
Uniformly over H and tau in(W6),

    14(L+J)+R_u
       <=(7/2)M^(8/25)+(C_loc,K+15)M^(4/25).

All displayed powers are strictly below1.
Thus for every sufficiently large M, depending only on K, this last expression is at most M, and separately R_z,J,L<=M.
This proves every full condition(W3), not only the unshifted radii condition.

The actual prime schedule gives epsilon_j=O_K(M_j^-2(1+log M_j)) by [C569v2](Yin_C_G0569_v2.md#static-phase-original-return), without an upper bound on prime gaps.
Choose finite constants C_eps,K and M_eps,K so that

    epsilon_j<=C_eps,K M_j^-2(1+log M_j) for M_j>=M_eps,K.

For the new return term in(W5), the COMPLETE support cost satisfies

    J^(13/8)M^-1 tau^(-25/16)
       <=H^(13/32)M^-1[M^(-16/25)H]^(-25/16)
       =H^(-37/32).                                           (W24)

For the true original-comparison term, the COMPLETE cost satisfies

    J^(13/8)epsilon_j^(3/4)tau^(-21/16)
       <=C_eps,K^(3/4)M^(-33/50)
                    H^(-29/32)(1+log M)^(3/4).                (W25)

Here the M exponent is -3/2+21/25=-33/50, and the H exponent is13/32-21/16=-29/32.
The powers -25/16 and -21/16 include the support factor tau^(-9/16).
Take, for example,

    C_crit,K=C_pay,K(C_return,K+C_eps,K^(3/4)).

Choose j0 so that M_j meets M_eps,K, max{2,c_res,K}, and all fixed onset inequalities from(W23).
Such a j0 depends only on K because the actual schedule has M_j->infinity.
Finally J+1>H^(1/4), so log(J+1)>(1/4)log H.
Substitution of(W24)--(W25) in(W4)--(W5) proves(W7).

For a sequence in the statement, put H=M_j^(16/25)tau_j.
Eventually H>=16, tau_j<=1/64 and H<=M_j^(16/25)/64, so it lies in(W6).
The main term tends to infinity.
The first error tends to zero, and the second is at most a fixed multiple of M_j^(-33/50)(1+log M_j)^(3/4), which also tends to zero.
This establishes the actual original Wiener-norm divergence.
No uniform entry time over arbitrary sequences is asserted.
For any fixed0<theta<16/25, choosing H=M_j^(16/25-theta) gives the claimed strict-power consequence on its eventual width strip.
Bounded H makes the logarithmic band growth unavailable, so the proof gives no pure-critical assertion.

<a id="classical-source-and-reuse-scope"></a>
### 8. Classical context and the exact source boundary

The local Claim/source search and the retained Tao09 Fourier text were checked before this weak-space refinement.
The actual retained [Tao09 Fourier notes](../literature/pdf/Tao09/fourier-transform-20090406.html#hy), Section2 after Corollary22, equation(6), states strong Hausdorff--Young for compact probability-Haar groups.
Its p=4/3 case has an ell4 target and applies on the circle and four-torus after the angular coordinate change.
This newly inspected passage is classical context only: it is not covered by the older Parseval-only reading and does not prove a weak-source assertion.

For attribution of the event norm and splitting mechanism, the primary [Tao, 245C Notes1, 2009-03-30](https://terrytao.wordpress.com/2009/03/30/245c-notes-1-interpolation-of-lp-spaces/) was directly inspected at Section2 equation(9), Exercise17, and Section3 in the proof of Theorem27 where the two height pieces are defined.
Exercise17 applied to the nonnegative function abs(h) identifies the event-integral norm on the present finite measure spaces.
The latter proof passage identifies height splitting as a real-interpolation mechanism.
These are bounded attribution checks.
No general interpolation theorem, full source proof or historical-priority claim is an input.
Every needed norm, event integration and finite Fourier estimate with constants4,768,8 is proved in Sections2--5.

The earlier strong L^(4/3) candidate would instead pay a truncated logarithmic moment and its3/4 power.
The weak event-norm argument avoids that moment by(W15)--(W20); it does not falsely upgrade a weak source to strong L^(4/3).
The new project deduction is the resolved original-curve return, its full finite support price and the exact critical-width consumer.
Existing source units, acquisition records, original proofs and historical review scopes are not upgraded by these bounded readings.
The [original fixed contact boundary](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) and arithmetic scope remain unchanged.

## Assessment history

### Decision weak-fourthirds-return-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T21:11 |
| status | open |
| reason | Register the complete event-norm and direct finite weak Fourier return for every closed-box Gamma, all five original costs, the entire adopted modulated support, and uniform critical16/25 widths with arbitrary diverging enlargement. Root and phase_bands are contributors. This new fixed theorem awaits fresh independent whole review; no strong weak-source substitution, pure-critical result, width optimality or unrestricted Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire weak-return statement](#statement) | W1--W7 with exact original polynomial, full2d window, Haar laws, constants, every finite Gamma including empty and signed harmonics, full support and center conditions, and uniform real H/width/sequence quantifiers. |
| argument | [Whole complete proof](#complete-argument) | W8--W25, event-norm equivalence and integral triangle, finite height splitting/Bessel/rearrangement constants, every translated path and clipping corner, both regularizations and smoothings plus actual original comparison, all support counts, floors, ceilings and critical exponents. |
| dependency | [Adopted translated-circle input](Yin_C_G0639_v1.md#decision-whole-reviewed-2026-10-23) | W8 for every translation at every resolved scale, actual amplitude derivatives and pathwise clipping interface; all event-norm and finite weak Fourier costs are proved anew here. |
| dependency | [Complete adopted localized phase bands](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Corrected cotangent convention, exact actual integer centers and bound14(k+m), full closed rectangle mass1/(512m), all common radii and entire torus mass3log(J+1)/(32768pi). |
| dependency | [Exact adopted positive kernel](Yin_C_G0637_v1.md#exact-positive-kernel-and-closed-support) | The specified normalized squared Fejer kernel, closed support including endpoints and first moment3pi/M. |
| dependency | [Kernel attribution and proof limits](Yin_C_G0637_v1.md#source-and-reuse-boundary) | The accepted finite kernel proof, probability normalization and bounded classical source account; no source proof is enlarged here. |
| dependency | [Logarithm-free amplitude probability](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | For the actual g, integral r_s<=8s^(2/3) for every0<s<=1; no amplitude-sharpness claim is converted to Fourier or width optimality. |
| dependency | [Original full input](Yin_C_G0565_v2.md#statement) | Actual K, prime schedule, Salem P_j and full original2d coefficient projection. |
| dependency | [True original L1 comparison](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Exact epsilon_j integral error and bounded range, yielding only the proved(epsilon_j/tau)^(3/4) event-norm cost. |
| dependency | [Closed original alias exclusion](Yin_C_G0565_v2.md#moving-band-exact-alias) | Complete2M integer differences, exact finite Q coefficient equality, distinct original characters and c_j dominance. |
| dependency | [Actual schedule asymptotic](Yin_C_G0569_v2.md#static-phase-original-return) | epsilon_j=O_K(M_j^-2(1+log M_j)) from the original lower prime separations. |
| dependency | [Original fixed contact and limits](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Fixed-j Wiener finiteness, actual contact-minus-Haar margin at least1/2, arithmetic family and separate limits; no near-one or unrestricted conclusion. |
| support | [Bounded classical attribution](#classical-source-and-reuse-scope) | Actual Tao09 Fourier equation6 context and newly checked Tao Notes1 equation9, Exercise17 and Theorem27 height-splitting passage; all required weak-source mathematics proved directly, no general interpolation or original-proof upgrade. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T21:24 |
| status | proved |
| reason | Adopt the entire weak-fourthirds finite return and critical16/25 consumer after main reading of complete C642 and isolated whole R848. Every event-norm and finite Fourier constant, translated coordinate path, both regularizations/smoothings and true original cost is paid. The full actual centered support and two complete errors prove divergence for every shrinking sequence with M_j^(16/25)tau_j tending to infinity. Strong-source substitution, bounded enlargement, optimality and unrestricted Task completion remain excluded. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire weak-return statement](#statement) | W1--W7 with exact original polynomial, full2d window, Haar laws, constants, every finite Gamma including empty and signed harmonics, full support and center conditions, and uniform real H/width/sequence quantifiers. |
| argument | [Whole complete proof](#complete-argument) | W8--W25, event-norm equivalence and integral triangle, finite height splitting/Bessel/rearrangement constants, every translated path and clipping corner, both regularizations and smoothings plus actual original comparison, all support counts, floors, ceilings and critical exponents. |
| dependency | [Adopted translated-circle input](Yin_C_G0639_v1.md#decision-whole-reviewed-2026-10-23) | W8 for every translation at every resolved scale, actual amplitude derivatives and pathwise clipping interface; all event-norm and finite weak Fourier costs are proved anew here. |
| dependency | [Complete adopted localized phase bands](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Corrected cotangent convention, exact actual integer centers and bound14(k+m), full closed rectangle mass1/(512m), all common radii and entire torus mass3log(J+1)/(32768pi). |
| dependency | [Exact adopted positive kernel](Yin_C_G0637_v1.md#exact-positive-kernel-and-closed-support) | The specified normalized squared Fejer kernel, closed support including endpoints and first moment3pi/M. |
| dependency | [Kernel attribution and proof limits](Yin_C_G0637_v1.md#source-and-reuse-boundary) | The accepted finite kernel proof, probability normalization and bounded classical source account; no source proof is enlarged here. |
| dependency | [Logarithm-free amplitude probability](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | For the actual g, integral r_s<=8s^(2/3) for every0<s<=1; no amplitude-sharpness claim is converted to Fourier or width optimality. |
| dependency | [Original full input](Yin_C_G0565_v2.md#statement) | Actual K, prime schedule, Salem P_j and full original2d coefficient projection. |
| dependency | [True original L1 comparison](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Exact epsilon_j integral error and bounded range, yielding only the proved(epsilon_j/tau)^(3/4) event-norm cost. |
| dependency | [Closed original alias exclusion](Yin_C_G0565_v2.md#moving-band-exact-alias) | Complete2M integer differences, exact finite Q coefficient equality, distinct original characters and c_j dominance. |
| dependency | [Actual schedule asymptotic](Yin_C_G0569_v2.md#static-phase-original-return) | epsilon_j=O_K(M_j^-2(1+log M_j)) from the original lower prime separations. |
| dependency | [Original fixed contact and limits](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Fixed-j Wiener finiteness, actual contact-minus-Haar margin at least1/2, arithmetic family and separate limits; no near-one or unrestricted conclusion. |
| support | [Bounded classical attribution](#classical-source-and-reuse-scope) | Actual Tao09 Fourier equation6 context and newly checked Tao Notes1 equation9, Exercise17 and Theorem27 height-splitting passage; all required weak-source mathematics proved directly, no general interpolation or original-proof upgrade. |
| review | [Independent whole weak-return finding](../audits/reviews/Yin_R_G0848_v1.md#whole-weak-fourthirds-finding) | Entire W1--W25, every finite Gamma and resolved path/event case, all five costs, exact support/centers/endpoints and uniform critical errors; bounded classical attribution and earlier source/review limits retained. |

