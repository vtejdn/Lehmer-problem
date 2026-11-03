---
author: Yin
---

# Actual inverse-Gram contact ratios, phase cells and a finite relative-error interface

Human author Yin.
Root assigned the actual coupled Gram/phase question after the adopted new-family theorem.
Phase_bands supplied the finite extremal identity, geometric ratio bound, exact exceptional-cell scope, relative-error return and fixed-input contact profile.
These are contributions, not independent review.
No native computation, prime scan or new source proof inspection is used.

## Statement

Use ANY ONE of the THREE actual adopted families: the square and25/11 families of C648/C656, or the logarithmically balanced21/11 family of C658.
Explicitly retain the common

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))),
    a_j=min{p prime:p>(j+1)K},
    b_j=min{p prime:p>(K+a_j+3)^2},
    L_j=K+a_j+b_j+2, M_j=floor(a_j/4), j>=1.

The three choices for c_j are respectively the least prime above

    (L_j+1)^2,
    ceil((L_j+1)^(25/11)),
    ceil((L_j+1)^(21/11))*ceil(log_2(L_j+1)).

Each threshold is an integer, and d_j=c_j+L_j-3 is the ACTUAL minimal-polynomial degree.
For a fixed j abbreviate a,b,L,M,c,d accordingly.
Use the full numerator

    Qraw(x)=(x^2-1)product_(e in {K,a,b,c})(x^e-1)
       -(x/2)sum_(e in {K,a,b,c})(x^e+1)
                              product_(f in {K,a,b,c},f!=e)(x^f-1),
    P=Qraw/(x-1)^3.

These are the source-certified monic integral irreducible Salem polynomials of the selected family, with no further cyclotomic factor, even degree, trace-1 and log2<m(P)<log4.
No arbitrary-input or near-one coverage is asserted.

In the ORIGINAL2d coordinates let A_rel have ALL d columns P,xP,...,x^(d-1)P, and set

    G=A_rel^T A_rel, Pi=A_rel G^-1 A_rel^T, R_orig=I-Pi,
    v_n(z)=(1,z,...,z^(n-1))^T,
    k(z)=v_(2d)(z)^*R_orig v_(2d)(z)/(2d), h_orig=1-k,
    G_d(z)=v_d(z)^*G^-1 v_d(z).

The full G is positive definite and G_d>0 on the circle.
Circle Haar nu_1 has mass one; V(w) denotes unnormalized angular total variation.
Write f_tau=(1-h_orig/tau)_+.
Use fhat(n)=integral f(z)z^(-n)dnu_1 and the corresponding negative-exponential convention on the torus, and put W_*(f)=sum_(n!=0)abs(fhat(n)).

Define the same actual polynomials

    R_0=(z^K-1)(z^a-1)(z^b-1),
    S_0=sum_(e in {K,a,b})(z^e+1)
                              product_(f in {K,a,b},f!=e)(z^f-1),
    A=-(z^2-1)R_0-zR_0/2+zS_0/2,
    B= (z^2-1)R_0-zR_0/2-zS_0/2, A_0=A/(z-1)^2,
    varphi(z)=(A/B)(z^-1)=B(z)/A(z) on the circle,
    h_phase=(1+Re(z^c varphi(z)))/2, F_tau^phase=(1-h_phase/tau)_+.

The ratio A/B is its smooth extension, with varphi(1)=-1 and A_0 nonzero on the circle.
The two exact identities and their coupled form are

    h_orig=abs(P)^2 G_d/(2d),
    h_phase=abs(z-1)^2 abs(P)^2/[4abs(A_0)^2],
    r(z)=2abs(A_0(z))^2G_d(z)/[d abs(z-1)^2],
    h_orig=r*h_phase, z!=1.                                (GR1)

The last identity holds also at unit-circle roots of P without division by P.
Its cross-multiplied form holds at1.
One has h_orig(1)>0 and r(z)->infinity as z->1.

### Finite variational meaning of the full inverse Gram

For every z in T, with the extrema over complex polynomials,

    G_d(z)=sup_(q polynomial,deg q<d,q!=0)
                          abs(q(z))^2/integral_T abs(Pq)^2dnu_1,
    G_d(z)^-1=min_(deg q<d,q(z)=1)integral_T abs(Pq)^2dnu_1. (GR2)

The minimum is attained uniquely.
Define the explicit finite convolution

    K_d^P(z)=integral_T abs(P(w))^2 Fej_d(arg w-arg z)dnu_1(w),
    Fej_d(t)=d^-1 abs(sum_(n=0)^(d-1)exp(int))^2.

Then K_d^P is continuous and strictly positive, and

    G_d(z)>=d/K_d^P(z),
    r(z)>=2abs(A_0(z))^2/[abs(z-1)^2 K_d^P(z)], z!=1.        (GR3)

Consequently the exact numbers

    lambda=min{1,inf_(z!=1)r(z)},
    lambda_D=min{1,inf_(z!=1)
                2abs(A_0(z))^2/[abs(z-1)^2 K_d^P(z)]}

satisfy0<lambda_D<=lambda<=1.
They depend on the actual finite input; no uniform-in-j positive lower bound is asserted.

### An actual upper bound on every genuine-root phase cell

Choose the smooth lift psi with varphi(exp(it))=exp(i psi(t)), psi(0)=pi and

    psi'(t)>0, psi(t+2pi)=psi(t)+2pi(L-4),
    Theta(t)=ct+psi(t).

Put D_turn=c+L-4=d-1.
There are exactly D_turn phase zeros per circle, with representatives t_m defined by

    Theta(t_m)=pi+2pi m, m=0,...,D_turn-1, t_0=0.

All exp(i t_m),m>=1, are the d-2 distinct unit-circle roots of P.
The extra center m=0 is1.
Let I_m be the closed phase cell given by

    abs(Theta(t)-Theta(t_m))<=pi,

using the continuous lift about its center and periodic identification.
The cells partition the circle up to endpoints and each has angular length at most2pi/c.
For every m>=1 and every z=exp(it) in I_m,

    r(z)<=R_cell:=pi^2(4d^2-1)/(12c^2).                    (GR4)

The value at the root itself is the continuous value from(GR1).
All these estimates retain the full2d window.
Since d<2c in each specified family, R_cell<4pi^2/3 uniformly in j.

For the extra cell I_0,

    nu_1(I_0)<=1/c,
    nu_1(I_0 intersect {h_phase<=tau})<=sqrt(tau)/c,
                                               0<tau<=1. (GR5)

These are phase-contact bounds.
They are NOT a bound for the full original cap difference on I_0.
That difference has the unconditional fourth-thirds integral bound1/c on I_0.
For each fixed input,
eta_0=min_(I_0)h_orig>0; only when0<tau<=eta_0 does the stronger bound sqrt(tau)/c apply to that integral.
No uniform lower bound on eta_0 is supplied.

### A fully specified relative cap budget and its remaining controls

For z!=1 put

    eta_r(z)=abs(r(z)-1)/max{1,r(z)},
    w_r(z)=eta_r(z)^(4/3),

and extend eta_r(1)=w_r(1)=1.
These are continuous BV functions.
Define the actual finite functional

    B_rel=integral_T w_r dnu_1+[(L-4)+V(w_r)]/c.

For every0<tau<=1,

    integral_T abs(f_tau-F_tau^phase)^(4/3)dnu_1
                         <=sqrt(tau/lambda) B_rel,
    ||f_tau-F_tau^phase||_(4/3)
                         <=tau^(3/8)lambda^(-3/8)B_rel^(3/4). (GR6)

Replacing lambda by the explicit smaller lambda_D gives another valid bound.
The full inverse Gram and all correlation remain inside these finite quantities.

For a paid comparison with existing input, put

    E=[1+pi L(5+2log c)]/c, epsilon=(4L-5)/(2d)+E/2,
    V_bar=80pi L[1+log(4d)]+pi c E
              +26pi(L-4)[1+log(2c)]+2pi+pi(L-4),
    B_bar=epsilon+[V_bar+L-4]/c,
    N_deg=d+L-3.

Then

    integral w_r<=min{1,inf_(0<s<=1)
                         [(1+(L-4)/c)sqrt(s)+epsilon/s]},
    V(w_r)<=4(N_deg+2).                                    (GR7)

When epsilon<=1, the first bound is at most
min{1,(2+(L-4)/c)epsilon^(1/3)}.
The second bound is an actual finite degree estimate, not an estimate tending to zero after division by c.
It does not establish decay of B_rel, and(GR3) does not establish a uniform lambda.
These are precise remaining controls for using the ratio mechanism quantitatively.

### Complete five-cost finite return with the better actual first term

Use EXACTLY the fixed-K torus functions F_tau,V,g,Ncal, constants C_w,C_s,C_2, positive kernel P_M, rho=(C_w/M)^2, Q_(tau,rho), map iota and H(gamma) from the adopted C658 statement for its family and the identical definitions in C656 for either older family.
In particular C_2=2*2048^(3/4)C_w+2C_s.
Both translated-law interfaces and the complete closed2M alias property are already proved for each specified family.

For M>=max{2,C_w} and0<tau<=1/64 define

    E_first(j,tau)=min{(32B_bar)^(3/4)tau^(-3/8),
                           tau^(3/8)lambda^(-3/8)B_rel^(3/4)},
    B_full(j,tau)=E_first(j,tau)+C_2 M^-1 tau^(-1/8).

For EVERY finite Gamma in the CLOSED integer box[-M,M]^4,

    sum_(gamma in Gamma)
       abs(fhat_tau(H(gamma))-Fhat_tau(gamma))
       <=8 card(Gamma)^(3/4)B_full(j,tau).                  (GR8)

Empty sets, signed and zero harmonics and all endpoints are included.
This retains two regularizations, two smoothings and the entire exact finite-polynomial return.

For the ENTIRE C638 centered selection G_(L_tau,J) and every integer J>=2, use its exact centers n_(k,m) and define

    L_tau=floor(1/(4sqrt(tau))), J>=2,
    C_loc=ceil(32000pi+1024pi(K+4)),
    C_sup=8[9(C_loc+1)^2]^(3/4)4^(-9/8),
    R_z=ceil(C_loc J^(1/3)), R_u=ceil(C_loc sqrt(L_tau)J^(5/6)),
    G_(L_tau,J)={(-p,-q,m,k):1<=k<=L_tau,1<=m<=J,
                               abs(p)<=R_z,abs(q-n_(k,m))<=R_u},
    N_sel=L_tau J(2R_z+1)(2R_u+1),
    R_z,J,L_tau<=M, 14(L_tau+J)+R_u<=M.

Then every original selected frequency is distinct and positive, and

    W_*(f_tau)>=3log(J+1)/(32768pi)-8N_sel^(3/4)B_full(j,tau). (GR9)

The complete subtracted term is bounded by

    C_sup J^(13/8)[
       min{(32B_bar)^(3/4)tau^(-15/16),
                    lambda^(-3/8)B_rel^(3/4)tau^(-3/16)}
                                  +C_2 M^-1 tau^(-11/16)]. (GR10)

No new width exponent follows without controlling the displayed new functionals.
All currently adopted actual-degree conclusions remain valid through the first term of the minimum.

### Exact fixed-input contact profile

Keep ONE fixed input and put v_m=Theta'(t_m)>0.
At the extra center its value is exactly v_0=c+1/(1/K+1/a+1/b).
For m>=1 let r_m=r(exp(i t_m)), the finite positive value in(GR1).
For p=4/3 define

    A_p(s)=integral_R abs((1-s x^2)_+-(1-x^2)_+)^p dx, s>0,
    A_p(infinity)=integral_(-1)^1(1-x^2)^p dx.

Then

    lim_(tau down to0) tau^(-1/2)
                   integral_T abs(f_tau-F_tau^phase)^p dnu_1
       =(1/pi)[A_p(infinity)/v_0
                          +sum_(m=1)^(d-2) A_p(r_m)/v_m].  (GR11)

At each genuine circle root,

    r_m=2abs(P'(exp(i t_m)))^2G_d(exp(i t_m))/(d v_m^2).     (GR12)

The extra contribution at1 is strictly positive.
This is a fixed-input limit, with input-dependent neighborhoods, positive minima and Taylor remainders.
It is not a uniform joint j,tau asymptotic and supplies no new shrinking-width theorem.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Complete argument

### 1. Full Gram identity and the finite extremum

The original coefficient matrix is real, so A_rel^*v_(2d)=P v_d on the circle.
The projection formula immediately gives the first line of(GR1).
The actual numerator identity A+z^c B=(z-1)^3P and |A|=|B| give
|A+z^cB|^2=4|A|^2h_phase.
Since A=(z-1)^2A_0 and A_0 has no circle zero, cancellation proves the second identity, including its continuous value at1.
Comparing after multiplication gives h_orig=r h_phase without dividing by P.
The factor removal at1 is exact, so P(1)!=0.
Thus h_orig(1)>0 and the numerator of r is continuous and positive at1, proving its pole.

For a polynomial q(w)=sum_(n=0)^(d-1)a_n w^n, finite orthogonality gives
integral |Pq|^2=a^*G a.
Its evaluation is v_d(z)^T a.
Cauchy--Schwarz in the positive G inner product shows that the supremum in(GR2) is
v_d(z)^T G^-1 conjugate(v_d(z)).
This equals G_d(z), because G^-1 is real symmetric.
The unique minimizing coefficient vector under q(z)=1 is

    a=G^-1 conjugate(v_d(z))/G_d(z).

This proves both assertions and uniqueness in(GR2).

Take the ACTUAL degree-(d-1) test polynomial
q_z(w)=d^-1 sum_(n=0)^(d-1)(conjugate(z)w)^n, which has q_z(z)=1.
Its squared modulus is Fej_d(arg w-arg z)/d, so(GR2) gives G_d>=d/K_d^P.
The convolution is strictly positive: its integrand is nonnegative, and neither nonzero polynomial P nor Fej_d vanishes except at finitely many circle points.
This proves(GR3).

Both r and the lower expression in(GR3) are continuous and positive away from1 and tend to infinity there.
They therefore have positive attained minima on a compact set separated from1.
This proves0<lambda_D<=lambda without asserting any uniform size.
The whole inverse Gram has not been replaced by an infinite Toeplitz limit.

### 2. Exact phase cells and the original evaluation-vector bound

The adopted exact phase calculation depends only on K,a,b.
Its inverse phase psi is strictly increasing with increment2pi(L-4); its derivative at each former cotangent pole is positive by the residue calculation.
Thus Theta'>=c and has total increment2pi(d-1).
The stated t_m and cells follow by strict monotonicity.
A cell phase length2pi has angular length at most2pi/c.

For z!=1, h_phase(z)=0 is equivalent to P(z)=0 by(GR1).
There are exactly d-2 such roots because P is the genuine Salem minimal polynomial; they are simple.
The remaining phase zero is1.
The cells contain no other phase zero besides their center.

Fix m>=1 and write Delta=t-t_m on its cell.
At the genuine root z_m, Pi v_(2d)(z_m)=0.
Multiply this zero vector by exp(i(2d-1)Delta/2) and subtract it before applying Pi.
Since Pi is an orthogonal projection,

    h_orig(exp(it))
       <=(1/(2d))sum_(n=0)^(2d-1)
                      abs(exp(i[n-(2d-1)/2]Delta)-1)^2
       <=[(4d^2-1)/12]Delta^2.                             (GR13)

The last step uses |exp(ix)-1|<=|x| and the exact variance of the integers0,...,2d-1.
This argument uses all2d coordinates and no Gram condition-number estimate.

On the same cell, let u=Theta(t)-Theta(t_m), so |u|<=pi and |Delta|<=|u|/c.
Here h_phase=sin^2(u/2)>=u^2/pi^2.
Divide(GR13) by this positive quantity away from the center and then extend by continuity.
This proves(GR4).

The extra cell contains1 and no root of P, including its boundary.
Thus h_orig>0 on that compact cell, proving eta_0>0.
For0<tau<=1, its phase contact interval has phase length4arcsin(sqrt(tau)).
Changing variables with dt/dTheta<=1/c gives probability at most
2arcsin(sqrt(tau))/(pi c)<=sqrt(tau)/c.
The full cell probability is at most1/c.
The cap difference is bounded by1, so its pth power has that unconditional cell integral bound.
If tau<=eta_0, the original cap vanishes on I_0; only the phase cap remains, giving the sharper contact bound.
This distinguishes the known phase measure from the still input-dependent original error near the pole.

### 3. A ratio-supported cap inequality on the same circle

For any r>0,x>=0, direct consideration of the two affine caps gives

    abs((1-rx/tau)_+-(1-x/tau)_+)
       <=abs(r-1)/max(1,r).

If r>=1 its nonzero set lies in x<=tau.
If r<=1 it lies in x<=tau/r.
With the actual r and x=h_phase, it therefore lies in h_phase<=tau/lambda, away from the null point1.
Consequently

    abs(f_tau-F_tau^phase)^(4/3)
       <=w_r 1_(h_phase<=tau/lambda).                       (GR14)

The pole is not removed from r; only the bounded relative error is continuously extended there.
Near1 it is1-1/r, which is smooth with value1 because1/r has a zero of order2.

For the precise BV assertion, put
T(z)=2|A_0(z)|^2G_d(z), D(z)=d|z-1|^2.
T is a strictly positive real trigonometric polynomial of degree at most N_deg=d+L-3, and D has degree1.
On the punctured circle r=T/D.
Its angular derivative numerator T'D-TD' is a trigonometric polynomial of degree at most N_deg+1.
It is not identically zero, because r has the stated pole.
Multiplication by a circle monomial gives an ordinary polynomial of degree at most2(N_deg+1), so it has at most that many zeros.

Remove1 and the derivative zeros to obtain finitely many intervals on which r is monotone.
On a monotone interval, w_r=(1-min(r,1/r))^(4/3) decreases then increases at most once, with range[0,1].
Its variation on that interval is at most2.
There are at most2(N_deg+1)+1 such intervals, and the common limiting value at1 creates no jump.
Hence V(w_r)<=4N_deg+6<=4(N_deg+2).
This proves BV and the second part of(GR7), including the piecewise powers at r=1.
The same monotone-interval argument with power1 proves that eta_r itself is BV.

The same-circle occupation estimate already proved in C656 applies to this continuous BV weight:
for every eta>0,

    integral w_r 1_(h_phase<=eta)
       <=sqrt(eta)[integral w_r+((L-4)sup(w_r)+V(w_r))/c].

Here sup(w_r)=1 due to its value at1.
Apply eta=tau/lambda in(GR14), even when eta>1.
This proves(GR6) with its complete winding and variation terms.

For the first part of(GR7), the signed scalar error satisfies
e=|h_orig-h_phase|=h_phase |r-1| away from1.
The relative error obeys eta_r<=min(1,e/h_phase).
For any0<s<=1, split at h_phase<=s.
On its complement, w_r<=eta_r<=e/s.
The unweighted occupation estimate is at most
(1+(L-4)/c)sqrt(s).
The actual original comparison gives integral e<=epsilon in all three families.
Thus the claimed infimum bound follows.
When epsilon<=1, take s=epsilon^(2/3); epsilon is positive for these inputs, and the displayed simplified bound results.
No estimate of V(w_r) by its mean has been inferred.

### 4. All remaining four costs and the entire selected support

The new original term is(GR6); independently the complete adopted additive BV argument gives
||f_tau-F_tau^phase||_(4/3)<=(32B_bar)^(3/4)tau^-3/8.
The torus pullback differs from the smooth phase only at1, so its norm is the same.
Taking the smaller of these ACTUAL bounds gives E_first.

For each of the three specified actual families, the adopted translated-law theorem supplies two regularization norms
2048^(3/4)sqrt(rho)tau^-1/8 and two smoothing event norms
C_s M^-1 tau^-1/8.
Their full sum after rho=(C_w/M)^2 is C_2 M^-1 tau^-1/8.
The event norm N_mu is bounded by the strong L^(4/3) norm and satisfies its direct triangle inequality.
Thus the full two-space error is bounded by B_full.

Each family has the proved closed2M no-alias inequalities
a>2M,b>2M(1+a),c>2M(1+a+b).
The squared-Fejer finite polynomial has closed-M support, so all coefficient returns are exact and all supplied original characters are distinct.
The adopted finite weak-Fourier bound is8 card(Gamma)^(3/4) times the event norm.
Applying it to the two error functions proves(GR8), including empty sets and signed endpoints.

The entire actual C638 mass uses every k,m rectangle, with the exact count N_sel in the statement.
Its center-plus-radius conditions place every coordinate in the box.
Since k>=1, every original image is at least c-M(1+a+b)>0.
The full torus mass is3log(J+1)/(32768pi), giving(GR9).
Finally
8N_sel^(3/4)<=C_sup J^(13/8)tau^-9/16.
Multiplication by both actual first-term alternatives and the remaining four-cost sum gives precisely(GR10).
No selected frequencies or one of the five comparison costs disappear.

### 5. Fixed-input profile and why it is not a moving-family theorem

Fix this j throughout the limiting argument.
Near a genuine root t_m, smooth Taylor expansion gives

    h_phase(exp(i(t_m+s)))=v_m^2 s^2/4+O(s^3),
    h_orig(exp(i(t_m+s)))=r_m v_m^2 s^2/4+O(s^3).

The second expansion follows from(GR1), or directly from the simple P root and the positive G_d.
The latter calculation gives
h_orig=|P'(z_m)|^2G_d(z_m)s^2/(2d)+O(s^3), proving(GR12).
All constants and neighborhood radii here may depend on the fixed input.

At t_0=0, h_orig(1)>0, so it stays positive on a fixed neighborhood.
The cotangent residue there is2(1/K+1/a+1/b), giving psi'(0)=1/(1/K+1/a+1/b) and the stated exact v_0.
The phase alone has the quadratic expansion v_0^2 s^2/4+O(s^3).
Outside disjoint fixed neighborhoods of all d-1 phase zeros, both nonnegative functions have positive minima.
For small enough tau both caps vanish on that complement; near0 the original cap also vanishes.

In the mth genuine-root neighborhood substitute s=2sqrt(tau)x/v_m.
After division by tau the two scalars converge to r_m x^2 and x^2.
Their active rescaled sets lie in a fixed bounded x interval, because their positive quadratic leading coefficients bound them from below by a positive multiple of s^2.
The cap differences are bounded by1.
Dominated convergence therefore gives the contribution
sqrt(tau)A_p(r_m)/(pi v_m).
The same argument at0, with only the phase cap, gives
sqrt(tau)A_p(infinity)/(pi v_0).
There are finitely many neighborhoods at this fixed input, so summing proves(GR11).

The constant A_p(infinity) is strictly positive.
For s>0, A_p(s) is finite and vanishes exactly at s=1; when s is small its possible size reflects the enlarged original contact interval.
The formula retains every actual root value of G_d.
Neither the uniform cell upper bound on r nor its finite extremal formula gives the missing uniform lower-ratio, relative-variation or Taylor control needed to use this limit along a moving j,tau sequence.

## Reuse and unresolved interface

The focused read covered C653's complete coupled identity, C592v2's actual finite inverse-Gram factorization, and the adopted C499 boundary-predictor representation.
C499 supplies an exact finite expression for G_d through the actual stable predictor and its linked positive factors.
It does not supply a uniform estimate of the present ratio, and its selected entire assessment is SELF; that relationship is not upgraded here.
The existing Sim08-U001 account provides the precise classical CD/Gohberg--Semencul attribution boundary, not a new inverse estimate.
The CRW08-U001 introduction/formula lead and C479 finite-Blaschke defect theorem concern different compression objects and do not prove the needed original coupled ratio control.
No new source-wide theorem or original proof is imported.

The extremal calculation above is proved directly in the finite positive Gram inner product.
The cell bound is proved directly from the ORIGINAL projection and its genuine arithmetic roots.
The relative functional and fixed-input limit are new local deductions about those same objects.

The remaining concrete control is decay of lambda^(-1/2)B_rel, or another estimate of the same actual contact-weighted relative error strong enough to pay(GR10).
The mean component of B_rel has the explicit small bound(GR7), but the proved degree bound for V(w_r)/c is only of constant order as d/c stays bounded, and lambda_D can depend on the full input.
These facts show precisely what the displayed estimates fail to provide; they do NOT prove that the actual relative functional is large or that better control is impossible.
Likewise the strict extra-cell term in the fixed-input limit is compatible with small moving-family costs, because its scale can depend on j.
No new width exponent, uniform r close to1, bounded-enlargement endpoint, near-one family or unrestricted conclusion is claimed.

## Assessment history

### Decision actual-ratio-interface-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T00:23 |
| status | open |
| reason | Register the complete actual full inverse-Gram extremum/lower bound, genuine-root phase-cell upper ratio, separately paid extra cell, relative-event finite return with all five costs and complete support, and exact fixed-input cap profile. All three specified source-certified families retain their original2d laws and positive total measure. Author checking is complete but fresh whole review remains required. The uniform lower-ratio/relative-variation and joint-limit controls remain explicitly unresolved; no new width or near-one conclusion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual-ratio statement](#statement) | GR1--GR12, all three actual families, full finite Gram and2d window, every phase cell and pole, exact finite relative return and complete band support, fixed-input profile and precise missing uniform controls. |
| argument | [Complete argument](#complete-argument) | Sections1--5/GR13--GR14, finite positive-Gram optimization, centered evaluation-vector geometry, actual BV degree and weighted occupation, five-cost finite return and every fixed-input contact neighborhood. |
| dependency | [Actual coupled phase identity](Yin_C_G0653_v1.md#coupled-original-ratio-and-open-control) | Exact original Gram/phase formula and pole, with the new-family hypotheses independently supplied by C658; no P division or uniform ratio approximation. |
| dependency | [Adopted original BV theorem](Yin_C_G0656_v1.md#decision-whole-reviewed-2026-10-23) | Same-circle occupation for every continuous BV weight, actual additive error and all old-family finite interfaces, retained only at the proved scope. |
| dependency | [Adopted new actual family](Yin_C_G0658_v1.md#decision-whole-reviewed-2026-10-24) | Exact21/11-log schedule, actual minimal polynomial, same phase and full original2d laws, every translated/alias and additive/BV input; original total measure is not near one. |
| dependency | [Old actual families](Yin_C_G0648_v1.md#decision-whole-reviewed-2026-10-23) | Exact square/25/11 families, full original normalization and scalar/sample definitions, with accepted source depths preserved. |
| dependency | [Four remaining comparison costs](Yin_C_G0641_v2.md#combined-argument) | Complete finite weak Fourier mechanism and smoothings, with the additional joint-shell proof supplying both regularizations after the actual-family premises are established. |
| dependency | [Joint-shell regularizations](Yin_C_G0641_v2.md#complete-additional-joint-shell-argument) | Both all-rho/tau regularization costs and exact constants, retaining translated laws and all shells. |
| dependency | [Full actual torus bands](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Every k,m center and radius, entire count and torus mass, with actual family positivity and closed-box return paid here. |
| support | [Finite inverse-Gram source account](Yin_C_G0592_v2.md#residual-laurent-square-identity) | Exact finite factorization only, directly rederived; original SELF/source/native boundaries and unrelated H4 examples are not upgraded. |
| support | [Finite boundary representation](Yin_C_G0499_v1.md#joint-boundary-symbol) | Actual predictor and linked product formula as a screened related interface, not a uniform estimate of r or an independent new proof audit. |
| support | [Classical attribution boundary](../audits/literature/Sim08/Yin_U001.md#sim08-u001) | Existing CD/finite-boundary attribution at its actual retained passage and proof depth; no uninspected inverse-Toeplitz theorem is used. |
| support | [Distinct model-space lead](../audits/literature/CRW08/Yin_U001.md#crw08-u001) | Original introduction/formula-related lead only; no uniform original-law or inverse-Gram input inferred. |
| support | [Exact unresolved interface](#reuse-and-unresolved-interface) | Small mean versus unpaid variation/lower ratio, extra-cell versus phase contact, fixed-input versus joint limit, and all actual measure/width boundaries. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T00:33 |
| status | proved |
| reason | Adopt the entire actual full-Gram ratio, finite extremum and phase-cell theorem, relative-error interface with all five costs and complete support, and exact fixed-input contact profile after complete main-agent reading and fresh independent whole R876. The three actual families, original2d objects, exact finite constants and source depths remain fixed. Positive lower ratios, extra-cell thresholds and Taylor neighborhoods are input-dependent; uniform relative variation/lower-ratio control, a joint moving-input limit, a new width rate and unrestricted Task completion remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual-ratio statement](#statement) | GR1--GR12, all three actual families, full finite Gram and2d window, every phase cell and pole, exact finite relative return and complete band support, fixed-input profile and precise missing uniform controls. |
| argument | [Complete argument](#complete-argument) | Sections1--5/GR13--GR14, finite positive-Gram optimization, centered evaluation-vector geometry, actual BV degree and weighted occupation, five-cost finite return and every fixed-input contact neighborhood. |
| dependency | [Actual coupled phase identity](Yin_C_G0653_v1.md#coupled-original-ratio-and-open-control) | Exact original Gram/phase formula and pole, with the new-family hypotheses independently supplied by C658; no P division or uniform ratio approximation. |
| dependency | [Adopted original BV theorem](Yin_C_G0656_v1.md#decision-whole-reviewed-2026-10-23) | Same-circle occupation for every continuous BV weight, actual additive error and all old-family finite interfaces, retained only at the proved scope. |
| dependency | [Adopted new actual family](Yin_C_G0658_v1.md#decision-whole-reviewed-2026-10-24) | Exact21/11-log schedule, actual minimal polynomial, same phase and full original2d laws, every translated/alias and additive/BV input; original total measure is not near one. |
| dependency | [Old actual families](Yin_C_G0648_v1.md#decision-whole-reviewed-2026-10-23) | Exact square/25/11 families, full original normalization and scalar/sample definitions, with accepted source depths preserved. |
| dependency | [Four remaining comparison costs](Yin_C_G0641_v2.md#combined-argument) | Complete finite weak Fourier mechanism and smoothings, with the additional joint-shell proof supplying both regularizations after the actual-family premises are established. |
| dependency | [Joint-shell regularizations](Yin_C_G0641_v2.md#complete-additional-joint-shell-argument) | Both all-rho/tau regularization costs and exact constants, retaining translated laws and all shells. |
| dependency | [Full actual torus bands](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | Every k,m center and radius, entire count and torus mass, with actual family positivity and closed-box return paid here. |
| support | [Finite inverse-Gram source account](Yin_C_G0592_v2.md#residual-laurent-square-identity) | Exact finite factorization only, directly rederived; original SELF/source/native boundaries and unrelated H4 examples are not upgraded. |
| support | [Finite boundary representation](Yin_C_G0499_v1.md#joint-boundary-symbol) | Actual predictor and linked product formula as a screened related interface, not a uniform estimate of r or an independent new proof audit. |
| support | [Classical attribution boundary](../audits/literature/Sim08/Yin_U001.md#sim08-u001) | Existing CD/finite-boundary attribution at its actual retained passage and proof depth; no uninspected inverse-Toeplitz theorem is used. |
| support | [Distinct model-space lead](../audits/literature/CRW08/Yin_U001.md#crw08-u001) | Original introduction/formula-related lead only; no uniform original-law or inverse-Gram input inferred. |
| support | [Exact unresolved interface](#reuse-and-unresolved-interface) | Small mean versus unpaid variation/lower ratio, extra-cell versus phase contact, fixed-input versus joint limit, and all actual measure/width boundaries. |
| review | [Independent entire actual-ratio finding](../audits/reviews/Yin_R_G0876_v1.md#actual-ratio-interface-whole-independent-finding) | Whole GR1--GR14 and Sections1--5, all three original inputs and source scopes, complex Gram extrema, genuine/extra cells, relative BV and finite five-cost return, entire support and exact fixed-input profile with every stated uniformity limitation. |

