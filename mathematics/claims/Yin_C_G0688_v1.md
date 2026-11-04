---
author: Yin
---

# All positive fixed widths and logarithmic Fourier growth of the weighted original projection

Human author Yin.
Phase_bands derived and checked this all-width extension of the adopted weighted three-factor family, using the original-law interfaces of C684 and the actual torus bands of C681.
The author is a contributor, not an independent reviewer.
The small fixed-width consequence already contained in C684 is not presented as a new critical shrinking-width exponent.
The new conclusions include every fixed tau>0, uniformity on compact positive-width intervals, and logarithmic Fourier growth of the actual full original projection profile itself.
No new family, native computation or external source theorem is introduced.

## Statement

Use exactly the adopted C684 weighted three-factor family, for integers j>=4K:

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))),
    a_j=min{p prime:p>(j+1)K}, L_j=K+a_j+2, M_j=floor(a_j/4),
    n_j=min{n positive integer:n^8>=(L_j+1)^17},
    ell_j=min{ell positive integer:2^ell>=L_j+1},
    c_j=min{p prime:p>n_j ell_j}, d_j=c_j+L_j-2.

Thus the last prime threshold is the INTEGER product ceil((L_j+1)^(17/8))*ceil(log_2(L_j+1)).
For e=(K,a_j,c_j) and w=(1,1,2), the actual polynomial is

    Qraw_j(x)=(x^2-1)product_(i=1)^3(x^e_i-1)
       -(x/2)sum_(i=1)^3 w_i(x^e_i+1)product_(l!=i)(x^e_l-1),
    P_j(x)=Qraw_j(x)/(x-1)^2.                              (AP1)

C684 establishes that P_j is monic integral irreducible Salem, of even actual degree d_j and trace0, with

    log2<m(P_j)<log4,
    M_j^(17/8)(1+log M_j)<d_j<2^15 M_j^(17/8)(1+log M_j).

The actual composite K, weighted source eligibility, exact cyclotomic removal and all source-inspection limits remain those of that adopted family.
Use ALL d_j columns and the full ORIGINAL2d_j coordinates:

    A_rel,j=[P_j,xP_j,...,x^(d_j-1)P_j],
    G_j=A_rel,j^T A_rel,j, Pi_j=A_rel,j G_j^-1 A_rel,j^T,
    v_n(z)=(1,z,...,z^(n-1))^T,
    h_orig,j=v_(2d_j)^*Pi_j v_(2d_j)/(2d_j),
    f_(j,tau)=(1-h_orig,j/tau)_+, tau>0.                  (AP2)

All Haar measures have mass1, Fourier coefficients use negative exponentials, and W_*(f)=sum_(n!=0)abs(fhat(n)).
For every fixed j,tau>0 this sum is finite.
The actual projection satisfies0<=h_orig,j<=1 and integral h_orig,j=1/2.
Every actual circle root of P_j has cap value1; for tau<=1 its margin above Haar mean is at least1/2, while for tau>=1 the margin is exactly1/(2tau).

Define the same two-coordinate phase and three-coordinate cap:

    R(z,u)=(z^K-1)(u-1), S(z,u)=2(z^K u-1),
    Acal=-(z^2-1)R-zR+zS/2,
    Bcal= (z^2-1)R-zR-zS/2,
    g_0=abs(Acal)^2+abs(Bcal)^2, Ncal=2Acal conjugate(Bcal),
    U=Acal/Bcal off common zeros, U=0 at common zeros,
    V(z,u)=U(z^-1,u^-1), g(z,u)=g_0(z^-1,u^-1),
    h(z,u,w)=(1+Re(wV))/2, F_tau=(1-h/tau)_+,
    iota_j(z)=(z,z^a_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+c_j gamma_2.             (AP3)

Write mu_(j,t) for the pushforward of circle Haar by z to t*iota_j(z), for EVERY t in T^3, and nu_r for product Haar on T^r.
These are the actual correlated original and translated laws, not independent phase models.

### A finite return valid for every positive width

Suppress j in a,c,d,L,M, and retain the exact original error and constants

    epsilon_j=(4L-3)/(2d)+[1+pi L(5+2log c)]/(2c),
    E_bal=4(3+3pi), epsilon_j<=E_bal M^(-9/8),
    delta_*=[28(1+60pi)]^-2,
    C_obs=2/delta_*, C_stab=33C_obs+3,
    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity, l=1,2,
    G_K=sqrt(||g||_infinity),
    C_w=6pi[1+10(D_1+D_2)+2(G_K+1)],
    C_s,all=3pi[18*48^(2/3)(D_1+D_2)+1],
    C_all=24^(2/3)C_w+2C_s,all.                           (AP4)

For M>=max{2,C_w} put rho=(C_w/M)^2 and

    V_rho=Ncal(z^-1,u^-1)/(g+rho),
    h_rho=(1+Re(wV_rho))/2, F_(tau,rho)=(1-h_rho/tau)_+,
    Fej_N(s)=N^-1 abs(sum_(r=0)^(N-1)exp(irs))^2,
    P_M=Fej_N^2/[(2N^2+1)/(3N)], N=floor(M/2)+1,
    Q_(tau,rho)=F_(tau,rho)*(three-coordinate product of P_M).

For a probability measure mu define

    N_mu(v)=sup_(E measurable,mu(E)>0)mu(E)^(-1/3)integral_E abs(v)dmu.

For EVERY tau>0 the complete five-cost estimate is

    N_nu1(f_(j,tau)-Q_(tau,rho) composed with iota_j)
       +N_nu3(F_tau-Q_(tau,rho))<=B_all(j,tau),
    B_all(j,tau)=min{1,(C_stab epsilon_j)^(2/3)}
                                      +C_all/(M tau).    (AP5)

For tau>=1 the sharper admissible budget is

    B_aff(j,tau)=[epsilon_j^(2/3)+C_all/M]/tau.           (AP6)

Consequently for EVERY finite Gamma in the CLOSED integer box[-M,M]^3,

    sum_(gamma in Gamma)
       abs(fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma))
          <=5 card(Gamma)^(2/3)B_all(j,tau).              (AP7)

For tau>=1, B_aff may replace B_all in(AP7).
Empty sets, all signs, zero, ties and all closed-box endpoints are included.
The entire selected original image is distinct, and the original comparison, TWO regularizations and TWO smoothings are all paid.

### An actual first-harmonic band for every positive width

Define the positive scalar

    r_tau=2arcsin(sqrt(tau)), 0<tau<=1,
    a(tau)=[r_tau-sin(r_tau)cos(r_tau)]/(4pi tau), 0<tau<=1,
    a(tau)=1/(4tau), tau>=1.                              (AP8)

The two formulas agree at tau=1, and a(tau)>0 is continuous on(0,infinity).
For m>=1 let t_(1,m) be the unique point in(0,1/(8K)) with

    b(t)=4sin t+cot(Kt/2), b(t_(1,m))=32sqrt(m),
    theta_(1,m)(t)=(1-m)arctan b(t)+(1+m)arctan(b(t)/3),
    n_(1,m)=floor(theta_(1,m)'(t_(1,m))+1/2),
    C_band=ceil(320000pi K).

These are the actual C681 phase centers; abs(n_(1,m))<=25K(1+m).
For the finite-band conclusions retain M>=max{2,C_w}.
For an integer J>=1 set

    R_J=ceil(C_band J^(5/6)),
    Gamma_J={(-p,m,1):1<=m<=J,abs(p-n_(1,m))<=R_J},
    N_J=J(2R_J+1)<=3(C_band+1)J^(11/6).                  (AP9)

Whenever

    J<=M, 25K(1+J)+R_J<=M,                              (AP10)

every selected original frequency is strictly positive and distinct, and for EVERY tau>0,

    W_*(f_(j,tau))>=a(tau)log(J+1)/1024
                               -5N_J^(2/3)B_all(j,tau). (AP11)

Again B_aff is admissible for tau>=1.
The entire centered band is retained in both the main mass and the returned cost; there is no maximum-coefficient selection.

### Explicit global thresholds and original projection growth

Set

    M_all=ceil(max{2,C_w,(100K)^(4/3),[2(C_band+1)]^(24/19)}),
    j_all=max{4K,ceil(4M_all/K)},
    C_fix=5[3(C_band+1)]^(2/3)max{(C_stab E_bal)^(2/3),C_all},
    C_aff=5[3(C_band+1)]^(2/3)max{E_bal^(2/3),C_all}.       (AP12)

For EVERY actual j with M=M_j>=M_all and EVERY tau>0, the choice J=floor(M^(1/4)) satisfies the entire support condition(AP10), and

    W_*(f_(j,tau))>=a(tau)log M/4096
                    -C_fix[M^(-4/9)+M^(-25/36)/tau].     (AP13)

For EVERY tau>=1 the sharper bound is

    W_*(f_(j,tau))>=[log M/16384
                         -C_aff(M^(-4/9)+M^(-25/36))]/tau. (AP14)

Every integer j>=j_all satisfies the actual M_j threshold.
In particular the SAME full original projection has

    W_*(h_orig,j)>=log M_j/16384
                          -C_aff[M_j^(-4/9)+M_j^(-25/36)]. (AP15)

Also W_*(f_(j,tau))=W_*(h_orig,j)/tau for EVERY tau>=1 and every actual j.
Thus W_*(f_(j,tau)) tends to infinity for each fixed tau>0.
For each compact interval0<tau_-<=tau_+<infinity the divergence is uniform for tau in[tau_-,tau_+].
Since1+log d_j<16(1+log M_j), (AP13) also gives

    W_*(f_(j,tau))>=a(tau)log d_j/65536-15a(tau)/65536
                      -C_fix[M_j^(-4/9)+M_j^(-25/36)/tau] (AP16)

at the same explicit threshold.
For(AP15), its positive term is correspondingly at least(log d_j-15)/262144.

These conclusions preserve the actual log2<m(P_j)<log4 interval and do not establish any near-one family or unrestricted G0001 statement.
The all-width budget(AP5) is not substituted for C684's stronger contact estimate when shrinking tau is considered.
No improved shrinking-width exponent, bounded-enlargement endpoint, optimality or every-degree assertion is made here.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Complete argument

### 1. Exact reuse boundary and original-law inputs

The family(AP1), including the integer product threshold for c, is identical to adopted C684, not a parameter change to C678's square-schedule family.
Its complete source/killer, cyclotomic, integrality, parity, minimality, exterior-root, trace and actual-degree conclusions therefore apply to these exact polynomials.
Its full2d raw-codimension2 comparison, cyclic missing zero sample, complete inverse Gram pole and local observability proof apply to(AP2) unchanged.
We use those actual conclusions, not a uniform relative-ratio hypothesis or an independent reference law.

In particular C684 gives a smooth unimodular phase varphi=(A/B)(z^-1), after cancelling the exact factor z-1 in A(z)=Acal(z,z^a), B(z)=Bcal(z,z^a), and

    h_phase=(1+Re(z^c varphi))/2,
    ||h_orig,j-h_phase||_1<=epsilon_j,
    ||f_(j,tau)-(1-h_phase/tau)_+||_(3/2)
                     <=min{1,(C_stab epsilon_j)^(2/3)}    (AP17)

for ALL tau>0.
The pullback h composed with iota_j equals h_phase away from the finite common-zero exceptional set, so the same comparison holds almost everywhere for F_tau composed with iota_j.
All integrals and Fourier coefficients are unchanged by that finite set.
For tau>=1 both caps are affine, and since h_orig,j and h_phase lie in[0,1],

    ||f_(j,tau)-F_tau composed with iota_j||_(3/2)
                         <=epsilon_j^(2/3)/tau.         (AP18)

This uses abs(h_orig,j-h_phase)<=1 and the exact original L1 error, rather than dividing a contact estimate by tau.

C684 proves a>2M and c>a^2>2M(1+a), hence H_j(delta)!=0 for every nonzero delta in the CLOSED[-2M,2M]^3 box.
Thus H_j is injective on the closed-M box and all polynomial coefficients in that box return exactly under iota_j.
The same proof gives exact torus means of closed-M polynomials under EVERY translated mu_(j,t).

The already paid positive-kernel absorption in C684, Section6, supplies the following particular consequence independently of any width:

    integral r_s dmu<=24s^(3/4), r_s=s/(g+s),
    rho<=s<=1, M sqrt(rho)=C_w,                          (AP19)

for every mu_(j,t), and with no larger constant for nu_3.
Here0<rho<=1 follows from M>=C_w.
The absorption uses all translated laws and their exact polynomial means; it does not assert nonlinear mean equality or coordinate independence on the original circle.
Its fixed-torus amplitude input and pointwise derivatives remain those of the identical two-coordinate Acal,Bcal.
These are sufficient existing accepted inputs for the extension below.

### 2. Both regularizations at every width

Write a_g=g/(g+rho).
The identity h_rho=a_g h+(1-a_g)/2 holds away from common zeros, and also at them because h=h_rho=1/2 there.
The scalar function x to(1-x/tau)_+ is1/tau-Lipschitz for every tau>0.
Consequently

    abs(F_tau-F_(tau,rho))<=r_rho/(2tau).

No one-sided sign or contact-set support claim is needed at widths above1/2.
Since0<=r_rho<=1, (AP19) at s=rho gives on EVERY translated original law and on the torus

    ||F_tau-F_(tau,rho)||_(3/2)
       <=[integral r_rho^(3/2)]^(2/3)/(2tau)
       <=24^(2/3)sqrt(rho)/(2tau).                       (AP20)

Strong3/2 bounds N_mu by Holder.
The two regularizations therefore cost altogether24^(2/3)C_w/(M tau).
This estimate holds without any assumption on rho/tau.

### 3. Every translated amplitude tail and both smoothings

For rho<=s<=1 the pointwise inequality1_(g<=s)<=2r_s and(AP19) give

    mu{g<=s}<=48s^(3/4).                                (AP21)

The factor2 is included; the24 in(AP19) is an integral bound, not itself a sublevel bound.
Let w_0=(g+rho)^(-1/2).
For0<t<=1 use probability at most1.
For1<t<=rho^(-1/2), the event w_0>t is contained in g<t^-2, and s=t^-2 lies in[rho,1].
For t>rho^(-1/2) the event is empty.
It follows for every t>0, under every translated law and under nu_3, that

    mu{w_0>t}<=48t^(-3/2), N_mu(w_0)<=3*48^(2/3).        (AP22)

The second inequality follows from the established event-norm layer-cake formula: for any event E, integrate min{mu(E),48t^(-3/2)} over t, obtaining3*48^(2/3)mu(E)^(1/3).
The same event-first calculation supplies the integral triangle inequality, including integration over positive kernels.

The equal-modulus derivative estimates of C678, Section6, hold for this unchanged phase at every rho>0:

    abs(partial_l h_rho)<=6D_l sqrt(h_rho)/sqrt(g+rho), l=1,2,
    abs(partial_3 h_rho)<=sqrt(h_rho).

Since0<=h_rho<=1, the coordinate-path changes of F_(tau,rho) have global envelopes6D_l w_0/tau for l=1,2 and1/tau for l=3.
One can obtain these bounds by applying the scalar Lipschitz inequality to the smooth h_rho along each path and then its ordinary FTC; there is no restriction of an ambient almost-everywhere derivative to a singular pushed circle.
All intermediate translated circles are among those already covered by(AP22).
For an event on the base circle, its image under any intermediate translated embedding has the same measure because the first coordinate of iota_j is z, so the embedding is injective.
Hence applying(AP22) after first integrating over the event is valid without changing its probability factor.
For torus Haar the same assertion follows from translation invariance.

The positive squared-Fejer kernel P_M has probability mass1, closed support[-M,M] and first angular moment at most3pi/M, with shortest signed angles in[-pi,pi].
Telescope its three coordinate convolutions, integrate each coordinate path first over an arbitrary event and then over its positive kernel, and use N_mu(1)=1.
The cost for EACH smoothing is at most

    (3pi/M)[18*48^(2/3)(D_1+D_2)+1]/tau
                               =C_s,all/(M tau).        (AP23)

This proves both the original-circle smoothing and the torus smoothing, with no width restriction.
In particular the third cap coordinate is included in the+1 term.

Adding(AP17), the TWO(AP20) and TWO(AP23), with the event-norm triangle inequality, proves(AP5).
Using(AP18) in exactly the same five-term decomposition proves(AP6).
This is a new global budget; it does not extend the small-width conclusion of C684 by suppressing its hypothesis.

### 4. Complete finite coefficient return

The finite weak Fourier lemma in adopted C678 states that for any N distinct orthonormal modulus-one characters, the sum of the N coefficient magnitudes of v is at most5N^(2/3)N_mu(v).
Its direct event-height truncation and finite Bessel proof, including ties, applies to each of the two errors in(AP5) or(AP6).
The circle characters indexed by H_j(Gamma) are distinct by the closed2M result of Section1; the torus characters indexed by Gamma are distinct as well.

Q_(tau,rho) has closed-M support because all three P_M factors have that support.
For gamma in the closed-M box, expansion of this finite polynomial and nonaliasing of differences in the closed2M box give

    (Q_(tau,rho) composed with iota_j)hat(H_j(gamma))
                                           =Qhat_(tau,rho)(gamma).

Subtract this exact identity, apply the triangle inequality coefficientwise, and then apply the finite lemma to the two errors.
This proves(AP7) with the complete budget and all selected coefficients.
An empty Gamma has zero sum, so that case is included without division by its cardinality.

### 5. Exact first cap harmonic for all positive widths

Let g_tau(exp(i theta))=(1-(1+cos theta)/(2tau))_+.
For0<tau<=1 its support is theta=pi+x, abs(x)<=r_tau, and on that interval

    g_tau(exp(i(pi+x)))=[cos x-cos r_tau]/(2tau).

The endpoints contribute zero, and symmetry gives

    ghat_tau(1)=-(1/(4pi tau))integral_(-r_tau)^(r_tau)
                                      (cos x-cos r_tau)cos x dx
                =-[r_tau-sin r_tau cos r_tau]/(4pi tau). (AP24)

The numerator is strictly positive for r_tau>0, since it is zero at0 and has derivative2sin^2 r.
For tau>=1 the scalar cap is exactly1-(1+cos theta)/(2tau), giving ghat_tau(1)=-1/(4tau).
At tau=1 both computations give-1/4.
This proves the asserted positivity and continuity of a(tau).

For each point with V nonzero, integrate the w coordinate first in F_tau(z,u,w)=g_tau(wV(z,u)).
This yields the first w coefficient ghat_tau(1)V(z,u).
At a common zero F_tau is constant in w, so its first w coefficient is zero, agreeing with the convention V=0.
Changing z,u to their inverses then proves for EVERY tau>0 and all integer p,m

    Fhat_tau(-p,m,1)=ghat_tau(1)Uhat(p,-m).              (AP25)

This argument is a finite single-coefficient calculation, not an infinite-series exchange or an extension of a small-width harmonic estimate.

### 6. Entire actual centered band and all its original images

The fixed-torus portion of adopted C681 applies to exactly the U and K of(AP3).
For k=1 it proves, for every m>=1 and every integer R>=C_band m^(5/6),

    sum_(abs(p-n_(1,m))<=R)abs(Uhat(p,-m))>=1/(1024m),
    abs(n_(1,m))<=25K(1+m).                              (AP26)

Its explicit weighted Mobius formula, witness b(t0)=32sqrt(m), local amplitude and phase modulation, and positive-kernel tail are retained at their exact accepted scope.
No two-factor band or old three-coordinate rectangle is used.

The common radius R_J satisfies(AP26) for every1<=m<=J.
Different m give disjoint triples, and R_J<=(C_band+1)J^(5/6) because J>=1.
Thus N_J=J(2R_J+1)<=3(C_band+1)J^(11/6), including all integer endpoints.
Combining(AP25) and(AP26), the entire Gamma_J has torus mass at least

    [a(tau)/1024]sum_(m=1)^J 1/m
                              >=a(tau)log(J+1)/1024.

Under(AP10) all three coordinates of every triple lie in the closed-M box.
The centers and radius are paid together: abs(p)<=25K(1+J)+R_J<=M.
Every original image satisfies

    H_j(-p,m,1)=-p+a_j m+c_j>=c_j-M>0.

All images are distinct by the actual closed2M result, so their absolute coefficient sum is a subsum of W_*.
Applying(AP7) to this ENTIRE set proves(AP11).

### 7. Explicit thresholds, exponents, degree and width quantifiers

For M>=M_all, J=floor(M^(1/4))>=1 and J<=M.
The exact radius ceiling and center bound give

    25K(1+J)+R_J<=50K M^(1/4)+(C_band+1)M^(5/24).

The two power thresholds in(AP12) bound these terms respectively by M/2 and M/2.
Hence(AP10) holds at every displayed input, with no implicit large-j support assumption.
If j>=j_all, then a_j>(j+1)K>4M_all, so the actual integer floor M_j is at least M_all.

The complete finite error in(AP11) is at most

    5[3(C_band+1)]^(2/3)J^(11/9)
       *[(C_stab E_bal)^(2/3)M^(-3/4)+C_all/(M tau)].

Since J^(11/9)<=M^(11/36), its two powers are respectively M^(-4/9) and M^(-25/36)/tau.
Also J+1>M^(1/4), giving the positive term a(tau)log M/4096.
This proves(AP13) with its complete constant.
Using(AP6) instead gives the first error coefficient E_bal^(2/3)/tau, and a(tau)=1/(4tau) for tau>=1, proving(AP14).

For every actual j and tau>=1, f_(j,tau)=1-h_orig,j/tau pointwise.
Therefore every nonzero Fourier coefficient is exactly-hhat_orig,j(n)/tau, and W_*(f_(j,tau))=W_*(h_orig,j)/tau.
The projection profile is itself a finite trigonometric polynomial, so this identity involves no convergence question.
Setting tau=1 in(AP14) proves(AP15).

For fixed tau>0 the positive coefficient a(tau)/4096 is nonzero, while both error terms in(AP13) tend to zero as j tends to infinity.
For a compact interval[tau_-,tau_+] in(0,infinity), continuity and strict positivity give a_min=min a(tau)>0 there.
The uniform lower bound is a_min log M/4096-C_fix[M^(-4/9)+M^(-25/36)/tau_-], which tends to infinity.
This gives the stated uniformity without any claim about a sequence tending to0 or to infinity.

C684's actual degree bound yields1+log d<16(1+log M), hence log M>(log d-15)/16.
Substitution proves(AP16) and the displayed genuine-degree version of(AP15).
The degree estimate concerns the actual minimal polynomial; no raw-degree or last-prime substitution is made.

Finally the rank-d projection in2d coordinates has mean1/2 and takes values in[0,1].
At any circle root every relation polynomial vanishes, giving h_orig=0 and cap value1.
For tau<=1 the cap is at most1-h_orig, giving margin at least1/2.
For tau>=1 the affine formula gives mean1-1/(2tau) and margin exactly1/(2tau).
For fixed j,tau>0 the cap is continuous piecewise smooth with square-integrable derivative, since the trigonometric level equation has finitely many roots unless identically zero.
Integration by parts, derivative Bessel and summability of n^-2 give finite W_* for each fixed input, consistently with its proved growth along j.

## Source, reuse and scope boundary

The inspected reusable inputs are C684's exact actual family, full original2d comparison, every-width stability, closed2M aliases and every-translated-law amplitude bound; C678's equal-modulus derivatives, event norm and finite coefficient lemma; C681's actual c-independent first-harmonic bands; and C637's finite positive squared-Fejer kernel.
All polynomials, original projections, phase coordinates and exceptional-set conventions coincide with those inputs.
The new work is the global all-width budget, exact scalar first harmonic and its full finite-band/threshold application, including the original projection itself.
The weaker global estimate is used for positive fixed widths, not to claim an improvement of the contact-weighted shrinking corridor.
C684 already implies divergence at each fixed0<tau<=1/64; that existing consequence is retained, not counted as a new exponent.
The source applicability and inspection depths inherited from C684 remain unchanged: the general MS05 torsion/interlacing and accepted integer Bertrand statements, the locally proved weighted adaptation, and no new whole-source proof audit.
The event-norm and finite height-splitting attribution remains the bounded Tao Notes1 account already retained by C678/C641 v2, while the squared-Fejer attribution remains the C637 account.
No external strong Hausdorff--Young theorem, independent original-circle coordinates, uniform Gram ratio or unregistered family is assumed.
The actual positive measure interval log2<m(P_j)<log4 remains an explicit limitation for G0001.

## Assessment history

### Decision all-positive-width-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:25 |
| status | open |
| reason | Register the complete all-positive-width finite return and actual first-harmonic band application for the exact adopted weighted17/8-log family. All five original costs, translated laws, finite supports and explicit thresholds are paid, giving logarithmic growth for every fixed positive width, uniformly on compact positive-width intervals, and for the actual full original projection itself. The author-checked result awaits fresh independent whole review; no shrinking-exponent, bounded-enlargement, source-depth, near-one or unrestricted Task advancement is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [All positive widths and original projection](#statement) | AP1--AP16: exact actual family and full2d profile, all-width and affine finite budgets, complete first-harmonic bands, explicit support thresholds, fixed-width uniformity and genuine-degree logarithmic growth. |
| argument | [Complete argument](#complete-argument) | Sections1--7/AP17--AP26: actual input reuse, every translated amplitude tail, two regularizations and two smoothings plus original error, complete finite return, exact scalar harmonic, full bands and all quantifiers. |
| dependency | [Adopted exact actual weighted family](Yin_C_G0684_v1.md#decision-whole-reviewed-2026-10-24) | Unchanged17/8 logarithmic prime schedule and actual full2d polynomial/projection; WL1--WL6, closed2M aliases, Section6 width-independent translated amplitude bound and actual degree. Its small-width finite-return conclusion is not silently extended. |
| dependency | [Equal-modulus and finite event mechanisms](Yin_C_G0678_v1.md#decision-whole-reviewed-2026-10-24) | Section6 generic pointwise derivative and event-norm calculations and Section7 finite weak Fourier lemma with constant5; no use of its old square-family original law for this new-family input. |
| dependency | [Adopted actual weighted torus bands](Yin_C_G0681_v1.md#decision-whole-reviewed-2026-10-24) | Exact k=1 weighted Mobius phase, moving witness, modulation center, full centered-band mass and constants for the identical c-independent torus phase. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Exact squared-Fejer normalization, positivity, closed support and first angular moment with the retained source attribution. |
| support | [Source and scope boundary](#source-reuse-and-scope-boundary) | Exact unchanged-family and torus input roles, retained source-depth limits, all-width extension versus old small-width consequence, and positive-measure/unrestricted boundary. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:32 |
| status | proved |
| reason | The entire fixed AP1--AP26 statement and Sections1--7 proof were directly read, followed by all of fresh isolated R908. Adopt the new all-positive-width and affine five-cost returns, exact first harmonic and whole actual band, explicit support thresholds, logarithmic growth of the full original projection, and compact-positive-width uniformity. The exact weighted family and positive Mahler interval remain; no improved shrinking exponent, near-one family or unrestricted Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [All positive widths and original projection](#statement) | AP1--AP16: exact actual family and full2d profile, all-width and affine finite budgets, complete first-harmonic bands, explicit support thresholds, fixed-width uniformity and genuine-degree logarithmic growth. |
| argument | [Complete argument](#complete-argument) | Sections1--7/AP17--AP26: actual input reuse, every translated amplitude tail, two regularizations and two smoothings plus original error, complete finite return, exact scalar harmonic, full bands and all quantifiers. |
| dependency | [Adopted exact actual weighted family](Yin_C_G0684_v1.md#decision-whole-reviewed-2026-10-24) | Unchanged17/8 logarithmic prime schedule and actual full2d polynomial/projection; WL1--WL6, closed2M aliases, Section6 width-independent translated amplitude bound and actual degree. Its small-width finite-return conclusion is not silently extended. |
| dependency | [Equal-modulus and finite event mechanisms](Yin_C_G0678_v1.md#decision-whole-reviewed-2026-10-24) | Section6 generic pointwise derivative and event-norm calculations and Section7 finite weak Fourier lemma with constant5; no use of its old square-family original law for this new-family input. |
| dependency | [Adopted actual weighted torus bands](Yin_C_G0681_v1.md#decision-whole-reviewed-2026-10-24) | Exact k=1 weighted Mobius phase, moving witness, modulation center, full centered-band mass and constants for the identical c-independent torus phase. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Exact squared-Fejer normalization, positivity, closed support and first angular moment with the retained source attribution. |
| support | [Source and scope boundary](#source-reuse-and-scope-boundary) | Exact unchanged-family and torus input roles, retained source-depth limits, all-width extension versus old small-width consequence, and positive-measure/unrestricted boundary. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0908_v1.md#whole-all-positive-width-original-projection-finding) | Entire AP1--AP26 and Sections1--7, all-width and affine costs on all actual laws, complete finite return and scalar/band calculation, full original projection, explicit thresholds and every degree/width quantifier. |
