---
author: Yin
---
# Joint clean-row Gaussian losses and full-density actual inverse constraints

All original seven sections/equations1--28 and complete actual/counter controls are retained.
L271 remains the meaningful development, contribution/source/negative history and original fixed review input; no research Task/E resumes.

## Statement

Put a0=log2. For EVERY A>=a0 define

    kappa(A)=min{sqrt(pi/A)*exp(-pi^2/a0),
                 exp(-25A/16)*(1-2^(-3/2))},
    gamma(A)=kappa(A)/32,K(A)=2+4A^2/gamma(A),
    u(A)=exp(-A)/2,
    Delta_A(t)=u(A)*gamma(A)*t^2/[2*(K(A)*gamma(A)*t^2+log2)].

For EVERY integer b>=1, EVERY real unit upper triangular C, EVERY x in R^b and exponents a_i in[a0,A], on the ENTIRE cube {-1,0,1}^b set

    y_i=x_i+sum_(j>i)C_(i,j)e_j,
    Z=sum_e exp[-sum_i a_i(e_i+y_i)^2],
    P_G(e)=exp[-sum_i a_i(e_i+y_i)^2]/Z,
    c_a=1+2exp(-a), pi_a(e)=exp(-a*e^2)/c_a,
    Pi=product_i pi_(a_i),G=log[(product_i c_(a_i))/Z].

The actual reverse conditionals of P_G generally differ from the normalized scalar Gaussian factors; neither auxiliary law replaces the original difference-digit law below.
Let D_(i,j)=C_(i,j) for j>i and ZERO otherwise, including its diagonal.
Choose q DISTINCT rows i_a and q DISTINCT pivot columns j_a; the two sets MAY overlap and their displayed order need not be physical coordinate order.
If t>eta>=0 satisfies abs(D_(i_a,j_a))>=t and sum_(c<a)abs(D_(i_a,j_c))<=eta for every a, put s=t-eta>0.
All other entries and shifts remain unrestricted.
For EVERY lambda>0,

    G>=q*f_u(lambda)/[K(A)+lambda/(gamma(A)*s^2)],
    f_u(lambda)=-log[1-u(A)*(1-exp(-lambda))],
    Z<=product_i c_(a_i)*exp[-q*Delta_A(s)].

The q0 case is G>=0.
The complete proof charges the quadratic budget once using distinct rows and charges whole-law relative entropy once; it does not add single-entry bounds or declare dependent events/Gibbs digits independent.

For the ACTUAL monic minimal polynomial P=sum_(j=0)^d p_j*t^j of ANY nonzero algebraic integer, d>=1, retain TOTAL m=log M(P), W=sum p_j^2 and ORIGINAL independent difference digits mu(0)=1/2,mu(+/-1)=1/4.
Put p_N=Pr(sum_(j=0)^(N-1)eta_j*alpha^j=0) and h2=lim_N[-log p_N]/N, in natural units.
For1<=N<=d, p_N=2^-N.
For N>d, k=N-d, B_N=[P,tP,...,t^(k-1)P] in ALL N rows, the last k constraints give e=Uh with integral unit-upper U_(i,j)=p_(d+i-j), actual Gram--Schmidt expansion R, T=R U^-1 and a_i=(log2)*delta_(i+1), exp(2m)<=delta_j<=W.
Only the first d coefficient constraints are dropped in the full cube upper sum.
For ANY disjoint consecutive blocks I, if T_I has q_I clean matched pairs with t_I>eta_I>=0 and exponents bounded by A_I, then

    p_N<=U_N*exp[-sum_I q_I*Delta_(A_I)(t_I-eta_I)],
    U_N=2^-N*product_(j=1)^k(1+2^(1-delta_j)),
    U_N<=2^-d*exp[-(N-d)*g(m)],
    g(m)=log[2/(1+2^(1-exp(2m)))].

Every outside tail and original weight remains; R/U/T/delta are rational at each finite input and A_I=Wlog2 suffices.

For m>0, the ACTUAL exterior-root Blaschke product has Bcal(0)=exp(-m), all multiplicities/both nonreal members counted in r, and H=exp(-m)/Bcal=sum_(ell>=0)h_ell*z^ell,h0=1.
The inverse series is formal at0 or analytic near0 only; every h_ell is real.
Let a_infinity=(log2)*exp(2m), v_ell=abs(h_ell)-sum_(j=1)^(ell-1)abs(h_j).
For EVERY FIXED ell with v_ell>0, EVERY A>a_infinity and0<epsilon<v_ell/2, there is an input-dependent all-future index i0, independent of N and suffix length, such that for EVERY N>d,

    p_N<=2^-d*exp[-(N-d)*g(m)]*
         exp[-Delta_A(v_ell-2epsilon)*(N-d-i0-ell)_+],
    h2>=g(m)+Delta_(a_infinity)(v_ell).

The exact selected-row count has density ONE and pays degree/onset/lag as additive boundaries, with no floor division by ell+1.
A supremum over separately proved FIXED-lag rate bounds is allowed, not their sum or a uniform finite-N claim with growing lag.
For every actual m>0 input, a first nonzero lag1<=ell0<=r<=d exists, with tau=h_(ell0)!=0 and all preceding positive coefficients zero, so

    h2>=g(m)+Delta_(a_infinity)(tau)>g(m),
    abs(tau)<=2sinh(m),
    0<Delta_(a_infinity)(tau)<=tau^2/(256log2)
                              <=sinh(m)^2/(64log2).

This O(m^2) upper bound concerns only the NEW CERTIFIED increment, not actual entropy or all joint methods.
The actual irreducible dyadic radicals P_r=t^(2r)-t^r-1,r=2^v,v>=1 have degree2r/TOTAL m=log phi, first lag r/tau1 and density-one correction with no1/r rate factor, while all finite degree/lag/input-onset expenses remain.
Their later dominance values at ell=nr are1,phi-1,0 and strictly negative thereafter despite unbounded inverse coefficients.
They supply fixed-positive-measure nonreciprocal controls, not near-one coverage.

For EVERY integer q>=1, a>=log2 and real t, the arbitrary Gaussian matrix C=[[I_q,tJ_q],[0,I_q]],x0,all exponents a, has q^2 equal cross entries/perfect matching but

    0<=G<=log(2q+1),
    Z/c_a^(2q)>=Pr_(pi_a^q)(sum_j f_j=0)>=1/(2q+1).

For fixed q, the first ratio tends exactly to that atom as abs(t)->infinity.
Thus a matching alone gives no universal positive q-linear loss; the clean condition fails on its identical rows.
This countercontrol is not asserted to be an actual irreducible-polynomial T.
No arbitrary-large-coefficient accumulation, uniform onset, actual near-one sequence, entropy floor or unrestricted Mahler gap follows.

<a id="argument"></a>
## Complete original argument

The following entire author text retains its original2026-10-10 development/source/contribution/next-gate context.
Its active/pending/continuation sentences do not select or resume a Task; current authority belongs to the selected assessment below.

<a id="joint-loss-reuse-and-domain"></a>
### 1. Reuse, question and exact probability space

Date: 2026-10-10.
The original argument introduces no numerical experiment or source acquisition.

The needed conclusion is a cumulative loss from many constraints in ONE finite Gaussian partition, with no repeated charge to its total relative entropy.
[L267](Yin_C_G0469_v1.md#statement) controls the entire auxiliary Gibbs law and proves one-entry loss uniformly over every other entry and every real shift.
Summing that one-entry conclusion would be invalid.
[L263](Yin_C_G0459_v1.md#all-lag-actual-center-limits) gives the actual fixed-diagonal inverse limits.
[L264](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) distinguishes these inverse coefficients from the direct square-summable coefficients.
The singular-value/lag-detection theorem of [L268](Yin_C_G0475_v1.md#statement) is related context only and is not a proof input below; a separate coordinator argument is combining L267 with that theorem.

A local reuse screen for matching, product-law entropy, Gaussian centers, tensorization and finite Fourier controls found sufficient methods in L267's full-law inequality, [L102's finite relative-entropy variational identity](Yin_C_G0297_v1.md#disjoint-smoothing-relative-entropy), and [L251's finite Fourier orthogonality mechanism](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments).
The matching certificate in [C522](Yin_C_G0522_v1.md#growth-defect-fixed-scope) concerns normalized Holder block profiles; it does not give the joint exponential-moment estimate needed here.
Its nonaccumulation controls remain valid.
No general entropy, product integration or Fourier orthogonality identity is claimed as new.
No newly recognized external theorem is required: the new step is the specific triangular clean-event construction and its application to the actual integer digit coordinates.

The coordinator supplied the broad accumulation question, and, after receiving the proposed construction and density-one consequence, requested checks of pivot integration order, clean-event substitution and all-future onset.
Those are verification cautions, not a supplied proof step.
After the complete author argument was written, it independently reiterated the first-lag direct-coefficient amplitude comparison already included in Section5.
All deductions below are by structural_research for Yin.
This author also authored L263/L267, whose complete independent reviews retain their separate roles.
No unfinished D139 result is used.

Write a_0=log2.
For A>=a_0 reuse the EXACT L267 constants

    kappa(A)=min{sqrt(pi/A) exp(-pi^2/a_0),
                 exp(-25A/16)(1-2^(-3/2))},
    gamma(A)=kappa(A)/32,
    K(A)=2+4A^2/gamma(A),
    u(A)=exp(-A)/2,
    Delta_A(t)=u(A)gamma(A)t^2 /
                  [2(K(A)gamma(A)t^2+log2)].          (1)

All constants are positive except Delta_A(0)=0.
Delta_A is continuous and even, increasing with |t|, and bounded by u(A)/(2K(A)).
For a in[a_0,A] let

    F_a(y)=sum_(e=-1)^1 exp[-a(e+y)^2],
    c_a=F_a(0)=1+2exp(-a),
    pi_a(e)=exp(-a e^2)/c_a.                          (2)

For b>=1, any real unit upper triangular b-by-b matrix C, any x in R^b, and a_i in[a_0,A], define on the ENTIRE cube {-1,0,1}^b

    y_i(e)=x_i+sum_(j>i) C_(i,j)e_j,
    Z=sum_e exp[-sum_i a_i(e_i+y_i(e))^2],
    P_G(e)=Z^(-1) exp[-sum_i a_i(e_i+y_i(e))^2],
    Pi(e)=product_i pi_(a_i)(e_i),
    G=log[(product_i c_(a_i))/Z].                    (3)

Write D(p||q)=sum_e p(e)log(p(e)/q(e)) for relative entropy of strictly positive finite laws, as used in L267.
The exact consumed L267 conclusions are

    G>=0,
    sum_i E_(P_G) y_i^2 <= G/gamma(A),
    D(P_G||Pi)<=K(A)G.                              (4)

These follow there from the actual reverse conditionals of P_G, which are generally NOT the individual scalar Gaussian factors.
We do not identify the two.
Both P_G and Pi are auxiliary finite laws used to bound a sum; neither replaces the original difference-digit law.
Formula(4) remains valid for arbitrarily large x and arbitrary other entries of C.

<a id="joint-clean-pivot-entropy-loss"></a>
### 2. A joint loss with one entropy payment

Extend the strict upper part of C by zero:

    D_(i,j)=C_(i,j) if j>i, and D_(i,j)=0 otherwise.

In particular its diagonal is ZERO.
Choose q distinct row indices i_1,...,i_q and q distinct column indices j_1,...,j_q.
The row and column sets MAY overlap; neither set must be increasing in its original coordinate order.
Their displayed ordering specifies the matching and the integration order.
Suppose that for some t>0 and 0<=eta<t,

    |D_(i_a,j_a)|>=t,
    sum_(c<a) |D_(i_a,j_c)|<=eta
                        for each 1<=a<=q.            (5)

Thus the selected row-column matrix is upper triangular up to a uniformly bounded TOTAL earlier-column contamination.
Every other entry is unrestricted.
In particular arbitrarily many later selected columns may couple to each row.
Put s=t-eta>0.
Then, for every lambda>0,

    G >= q f_u(lambda)/[K(A)+lambda/(gamma(A)s^2)],
    f_u(lambda)=-log[1-u(A)(1-exp(-lambda))].         (6)

Consequently

    Z<=product_i c_(a_i) exp[-q Delta_A(s)].          (7)

The case q=0 means the already established G>=0; below assume q>=1.

Define the CLEAN centers and their events by

    Y_a^0(e)=y_(i_a)(e)
                 -sum_(c<a) D_(i_a,j_c)e_(j_c),
    E_a={|Y_a^0|>=t},  Q(e)=sum_(a=1)^q 1_(E_a).     (8)

Pointwise on the entire cube, (5) gives |Y_a^0-y_(i_a)|<=eta.
Therefore E_a is a subset of {|y_(i_a)|>=s}, including equality at the boundary, and

    Q(e)<=s^(-2)sum_(a=1)^q y_(i_a)(e)^2,
    E_(P_G) Q <= G/(gamma(A)s^2).                    (9)

The last bound uses DISTINCT ROWS.
There is no factor q on its right side: each selected center is charged at most once against the full sum in(4).
We replace the contaminated centers by these pointwise clean-event subsets BEFORE any conditioning.

Under Pi, first fix every nonpivot coordinate, that is, every e_j with j outside {j_1,...,j_q}.
The remaining coordinates are still independent with their original centered laws pi_(a_j).
By construction Y_a^0 depends only on e_(j_a)...,e_(j_q), with coefficient D_(i_a,j_a) at the first of them.
For fixed later pivot coordinates, its form is z+D_(i_a,j_a)e_(j_a).
The identity

    max{|z+v|,|z-v|}>=|v|

implies at least one sign e_(j_a)=+1 or -1 belongs to E_a.
Each sign has probability exp(-a_(j_a))/c_(a_(j_a))>=exp(-A)/2=u(A).
Hence

    E_(e_(j_a)) exp[-lambda 1_(E_a)]
            <=1-u(A)(1-exp(-lambda)),               (10)

uniformly over the fixed outside coordinates and later pivot digits.

Integrate in the order a=1,2,...,q.
At the first step all later clean indicators E_2,...,E_q are independent of e_(j_1), in the precise sense of having no such coordinate in their defining functions.
Thus(10) removes the first factor and leaves the later factors untouched.
At step a, the earlier factors have already been bounded and removed, while the remaining later clean indicators have no dependence on e_(j_a).
Induction and then averaging over the nonpivot coordinates prove

    E_Pi exp[-lambda Q]
             <=[1-u(A)(1-exp(-lambda))]^q.           (11)

This does NOT assert that the E_a are independent.
It is a conditional product-integration inequality with a direction fixed by the clean upper-triangular dependence.
Overlap between the row set and column set causes no problem: only the distinct pivot COORDINATES are integrated, and the diagonal convention for D has already removed own-digit contributions from each center.

Apply the finite variational inequality to F=-lambda Q:

    D(P_G||Pi)>=-lambda E_(P_G)Q
                       -log E_Pi exp[-lambda Q]
                  >=q f_u(lambda)-lambda G/(gamma(A)s^2).

Combining with(4) proves(6).
In particular lambda=log2 gives f_u(log2)=-log(1-u/2)>=u/2.
Substitution gives exactly q Delta_A(s), proving(7).
The ENTIRE relative entropy D(P_G||Pi) is charged ONCE.
We neither add q copies of L267's single-entry estimate nor tensorize the dependent Gibbs law.

The same proof allows a simultaneous permutation of the displayed matched pairs whenever(5) holds in the new displayed order.
This is a reordering of the event elimination argument, not a claim that arbitrary coordinate permutation preserves upper triangularity of the original Gaussian energy.
No row operation on the digit cube is performed.

<a id="finite-original-joint-block-certificate"></a>
### 3. The original-law certificate with every finite cost

Let P(t)=sum_(j=0)^d p_j t^j be the actual monic minimal polynomial of a nonzero algebraic integer alpha, with p_d=1 and d>=1.
Set m=log M(P), W=sum p_j^2.
Keep the ORIGINAL independent difference law and collision mass

    mu(0)=1/2,  mu(+1)=mu(-1)=1/4,
    p_N=Pr(sum_(j=0)^(N-1) eta_j alpha^j=0),
    h_2(alpha)=lim_(N->infinity) -log(p_N)/N.          (12)

The rate limit is the retained original-word concatenation interface.
If N<=d then p_N=2^(-N).
For N>d put k=N-d and B_N=[P,tP,...,t^(k-1)P] in ALL N coefficient rows.
The exact reused L256/L263 interface is

    p_N=2^(-N) sum_(h in Z^k: ||B_N h||_infinity<=1)
                                exp[-(log2)||B_N h||_2^2],
    p_N<=2^(-N) sum_(e in{-1,0,1}^k)
       exp[-sum_(i=0)^(k-1) a_i
                       (e_i+sum_(j>i) T_(i,j)e_j)^2]. (13)

Here the Gram--Schmidt pivots delta_(i+1) of the actual polynomial shifts give a_i=(log2)delta_(i+1), and R is their unit upper triangular expansion matrix.
The last k coefficient constraints are exactly e=Uh with U_(i,j)=p_(d+i-j), p_l=0 outside0,...,d.
Thus U and its finite inverse are integral and unit upper triangular, e runs bijectively over the full cube, and T=R U^(-1).
Only the first d lower coefficient constraints were dropped in(13).
Neither the unbounded integer quotients h nor the original law are replaced by a finite-alphabet model.
All fixed T entries and pivots agree when k is increased.

The bounds exp(2m)<=delta_j<=W give log2<=a_i<=W log2.
Put

    U_N=2^(-N) product_(j=1)^k (1+2^(1-delta_j)),
    g(m)=log[2/(1+2^(1-exp(2m)))].                   (14)

Then U_N<=2^(-d) exp[-(N-d)g(m)].
For any collection of DISJOINT consecutive blocks I in {0,...,k-1}, suppose the principal matrix T_I satisfies(5) with q_I matched rows/columns, t_I>eta_I>=0, and A_I bounds every a_i in that block.
The new finite certificate is

    p_N<=U_N exp[-sum_I q_I Delta_(A_I)(t_I-eta_I)].  (15)

At a chosen block fix every later digit.
Its influence on the block is an arbitrary real x, covered uniformly by(7).
Eliminate that entire block, then continue in increasing chronological order.
Later energy rows do not depend on already eliminated digits.
At each unselected position use F_(a_i)(y)<=c_(a_i).
This proves(15), with all finite outside digits included and no exceptional-set or height restriction.
Within one block overlapping ROW AND COLUMN sets are legal under Section2; different chronological blocks in(15) remain disjoint.
Thus this statement does not count the same energy row or block loss twice.

For any finite P,N the quantities R,U,T,delta are rational and can be computed exactly.
A_I=W log2 is always an available bound.
Equation(15) is consequently a finite certifiable inequality with every original weight, degree and coordinate cost shown.
No such finite computation was performed for this draft.

<a id="density-one-actual-center-coupling"></a>
### 4. Actual diagonal dominance gives density one

Assume m>0.
Let r be the number of exterior roots with multiplicity, counting both members of every nonreal conjugate pair.
With s_0=exp(-m), let Bcal be the actual exterior-root finite Blaschke product normalized by Bcal(0)=s_0.
Write

    H(z)=s_0/Bcal(z)=sum_(ell>=0) h_ell z^ell,
    h_0=1,  a_infinity=(log2)exp(2m).

This is a formal reciprocal at zero, or an analytic series near zero only.
The accepted L263 limits, including actual unit-circle roots, are

    a_i -> a_infinity,
    T_(i,i+ell) -> h_ell for every FIXED ell>=1.       (16)

Every coefficient is real.
Define the finite-lag dominance margin

    v_ell=|h_ell|-sum_(j=1)^(ell-1)|h_j|.            (17)

Fix any ell with v_ell>0, A>a_infinity and 0<epsilon<v_ell/2.
By finitely many instances of(16) there is an input-dependent integer i_0>=0 such that for ALL i>=i_0,

    a_i<=A,
    |T_(i,i+ell)|>=|h_ell|-epsilon,
    sum_(j=1)^(ell-1)|T_(i,i+j)|
                   <=sum_(j=1)^(ell-1)|h_j|+epsilon. (18)

For ell=1 the empty sum is zero.
One may obtain the last line by assigning total tolerance epsilon to the finitely many shorter diagonals.
This is an all-future statement in i, not merely a check at a finite number of rows.
Its i_0 can depend on P,ell,A,epsilon, but does NOT depend on the later chosen N or the length of a suffix block.
No uniform effective estimate for i_0 is asserted.

When k>i_0+ell, first eliminate indices0,...,i_0-1 by scalar maxima, and take the ENTIRE remaining suffix {i_0,...,k-1} as ONE block.
Let q=k-i_0-ell and choose its q matched rows and columns, in their original labels, as

    i_a=i_0+a-1,  j_a=i_0+a-1+ell,
                            1<=a<=q.                (19)

For c<a, the strict upper entry D_(i_a,j_c) is zero when j_c<=i_a.
Otherwise its lag is ell+c-a, which lies in1,...,ell-1.
As c varies these lags are distinct.
Thus(18) verifies(5) with

    t=|h_ell|-epsilon,
    eta=sum_(j=1)^(ell-1)|h_j|+epsilon,
    t-eta=v_ell-2epsilon>0.

All later-pivot couplings, including arbitrarily many longer inverse diagonals, remain unrestricted.
The row and column sets in(19) usually overlap extensively.
Their overlap is permitted by the exact event argument; it is not a collection of overlapping block estimates.

Equations(15)--(19) prove for EVERY N>d

    p_N<=2^(-d) exp[-(N-d)g(m)]
        exp[-Delta_A(v_ell-2epsilon)
                         (N-d-i_0-ell)_+].           (20)

When k<=i_0+ell there are no selected row events and the additional factor is1, so the same formula includes that case.
The positive part is an integer count of distinct energy rows.
There is NO floor division by ell+1: the onset and lag cost an ADDITIVE boundary of i_0+ell retained coordinates, while the charged row density tends to one.
There is also no outside infinite tail: for each finite N the complete remaining suffix is included, and(18) supplies coefficients uniformly for every future start.

Take logarithms, divide by N, use the rate limit, then let epsilon decrease to zero and A decrease to a_infinity for this fixed input and this fixed ell.
Continuity of(1) gives

    h_2(alpha)>=g(m)+Delta_(a_infinity)(v_ell)
                         whenever v_ell>0.          (21)

One may take the supremum of the last terms over eligible FIXED lags.
This is a supremum of individually proved bounds, not their sum and not a uniform finite-N assertion with lag growing alongside N.
No result about general large inverse coefficients establishing v_ell>0 is being assumed.

<a id="first-nonzero-lag-full-density"></a>
### 5. Every actual positive-measure input and exact radical control

The qualifying set in(21) is nonempty for EVERY actual m>0 input.
For completeness the elementary L263 interface is as follows.
Write

    Bcal(z)/s_0=N_+(z)/D_+(z),
    N_+(z)=product_(|alpha_v|>1)(1-alpha_v z),
    D_+(z)=product_(|alpha_v|>1)(1-z/conj(alpha_v)).

Both polynomials have constant1 and degree r; the moduli of their leading coefficients are exp(m) and exp(-m).
Thus N_+-D_+ is nonzero with first nonzero coefficient at some ell_0 between1 and r.
Dividing by their constant-one denominators and inverting yields

    1<=ell_0<=r<=d,
    h_1=...=h_(ell_0-1)=0,
    tau=h_(ell_0)!=0,
    v_(ell_0)=|tau|.                                (22)

Applying(20)--(21) gives the complete finite original-law estimate with v=|tau|, and the density-one rate consequence

    h_2(alpha)>=g(m)+Delta_((log2)exp(2m))(tau)>g(m).  (23)

This removes the multiplicative lag-density penalty for the first nonzero actual inverse coefficient.
It does NOT assert a uniform positive lower bound for tau, nor replace tau by an arbitrarily later larger coefficient without the extra dominance hypothesis(17).
General nonzero algebraic integers, including nonunits, are covered at the original word-mass scope of(12)--(13).
No actual integer-order kernel or unit-only operator theorem is extended to nonunits.

There is a precise near-one limitation.
L264 proves that the direct coefficients of Bcal/s_0 have absolute value at most2sinh(m).
At the FIRST nonzero lag inversion changes only the sign, so |tau|<=2sinh(m).
Since A>=log2 implies u(A)<=1/4 and gamma(A)<1/32, equation(1) gives

    0<Delta_((log2)exp(2m))(tau)
       <=tau^2/(256log2)
       <=sinh(m)^2/(64log2)=O(m^2) as m decreases to0.
                                                               (24)

This is an UPPER bound on the newly certified increment, not an upper bound on actual h_2-g.
Thus the loss-density improvement alone cannot give a uniform entropy floor near one.
The one-expanding-root [L30 comparison](Yin_C_G0235_v1.md#one-expanding-comparison) remains stronger in its leading near-one term; our lower bound has baseline g(m)/m tending to log2 and the displayed first-lag increment is at most quadratic.
The density-one theorem changes the charging mechanism while leaving an amplitude problem.

An actual unbounded-degree control is the retained irreducible family

    P_r(t)=t^(2r)-t^r-1, r=2^v, v>=1,
    degree(P_r)=2r,  m(P_r)=log phi,
    phi=(1+sqrt5)/2,
    H_r(z)=(1-phi^(-1)z^r)/(1-phi z^r),
    h_(nr)=phi^(n-1) for n>=1,
    h_j=0 when r does not divide j.                 (25)

The actual irreducibility and original residue-law interface come from [L231](Yin_C_G0212_v1.md#radical-collision-control); the displayed inverse formula was also checked in L264.
Here ell_0=r and tau=1.
Thus(23) yields

    h_2(alpha_r)>=g(log phi)+Delta_(phi^2 log2)(1)     (26)

with no factor1/r in the rate correction.
At finite N the degree2r, lag r and actual onset i_0(P_r,r,A,epsilon) remain exactly as in(20); no common finite horizon in r is claimed.
The stronger exact residue decomposition already retained for this special family also avoids a1/r rate loss.
Formula(26) is a validation of the new general mechanism without assuming that decomposition, not a claim to improve the best known entropy for these inputs.
The family is nonreciprocal and has fixed positive m=log phi, so it is not near-one coverage.

It also shows why later large coefficients and the new sufficient criterion must be separated.
At ell=nr,

    v_(nr)=phi^(n-1)-sum_(j=1)^(n-1)phi^(j-1).

This is1 for n=1, phi-1 for n=2, zero for n=3 and negative for n>=4.
Indeed the geometric sum equals phi(phi^(n-1)-1), so v_(nr)=phi-(phi-1)phi^(n-1), strictly decreasing in n.
The inverse coefficients themselves grow without bound, but their large later values do not meet(17) in this actual example.
This is failure of this particular sufficient dominance condition, not an obstruction to a different joint mechanism or to actual entropy growth.

<a id="large-matching-redundant-center-control"></a>
### 6. Many large matched entries can still encode one constraint

The triangular cleanliness hypothesis has real content.
Here is an exact Gaussian control ruling out a naive inference of extensive loss from a large matching alone.
Fix q>=1, a>=log2 and any real t.
In dimension2q take x=0, all exponents equal a, and

    C=[I_q  t J_q; 0  I_q],

where every entry of the q-by-q matrix J_q is1.
There are q^2 cross entries equal t, including a perfect matching with q distinct rows and columns.
Write the cube coordinates as e,f in{-1,0,1}^q and S(f)=sum_j f_j.
Every one of the first q row centers equals tS.
Directly summing over e gives

    Z=sum_f exp[-a||f||^2] F_a(tS(f))^q,
    Z/c_a^(2q)=E_(pi_a^q) [F_a(tS)/c_a]^q
                          >=Pr_(pi_a^q)(S=0).       (27)

We verify the needed atom bound without an asymptotic theorem.
The characteristic function of pi_a is the trigonometric polynomial

    psi(theta)=(1+2exp(-a)cos(theta))/c_a>=0,

where nonnegativity uses a>=log2.
Finite Fourier expansion and integral orthogonality give, for each integer z,

    Pr(S=z)=integral_0^(2pi) psi(theta)^q cos(z theta)
                                                    dtheta/(2pi)
                    <=integral_0^(2pi) psi(theta)^q dtheta/(2pi)
                    =Pr(S=0).

The law is supported on the2q+1 integers -q,...,q, so its largest atom is at least1/(2q+1).
Therefore, for all real t,

    0<=G=log(c_a^(2q)/Z)<=log(2q+1).                 (28)

In fact as |t| tends to infinity with q fixed, every summand with S!=0 tends to zero and there are finitely many summands, so Z/c_a^(2q) tends exactly to Pr(S=0).
No limit in q is used in this assertion.

For any fixed nonzero t, (28) excludes a universal inequality G>=q delta(a,t) with delta(a,t)>0 based solely on the presence of a q-entry matching, even though ALL q^2 entries can have arbitrarily large magnitude.
The selected submatrix here has identical rows.
Every ordering has earlier-pivot contamination at least|t| from its second row onward, violating eta<t in(5).
The clean-event argument correctly refuses to count the same scalar cancellation S=0 as q independent constraints.

This is a control in the arbitrary real unit upper triangular Gaussian class.
No claim is made that C is the actual T of an irreducible polynomial, or that it obstructs an arithmetic strengthening.
It is distinct from the old single-entry saturation example: it rules out linearly adding MANY disjoint-row/disjoint-column entry signals without a condition on their coupled dependence.

<a id="joint-loss-selfcheck-and-next-gate"></a>
### 7. Self-check, limits and the remaining gate

The new mathematical content is(6)--(7), the fully charged original-law application(15)/(20), its density-one first-lag consequence(23), and the exact nonaccumulation control(28).
The arbitrary-translation domain is preserved throughout.
The event proof uses weak inequalities at all boundaries; a zero lower-triangular or diagonal D entry is treated as zero, never as the unit diagonal.
Clean events are constructed pointwise before conditioning.
Only pivot columns are independently integrated; the Gibbs law is never declared independent.
Distinct selected rows ensure a single use of the quadratic budget, and one finite variational inequality charges the full relative entropy once.

The original application uses one suffix block, not overlapping ell+1 blocks.
Its q=(N-d-i_0-ell)_+ is the exact count, and both degree and all-future onset are retained.
The all-future shorter-diagonal bound requires finitely many limits for a fixed ell, not convergence of an increasing-dimensional matrix in operator norm.
First nonzero lag exists by the actual exterior polynomial identity, including conjugate multiplicities and possible unit-circle roots.
General nonunit scope is restricted to original word mass.
No unit-only state/kernel theorem is used.

The exact radical control and the redundant-center countercontrol were checked symbolically, with all identities proved above.
There is no computer run or external proof re-audit to report.
The existing Nat26 scalar-theta scope is inherited only through the accepted L267 constants; no larger source claim is made.
The local reuse screen supplies the required methods, so no external literature search was needed for this bounded derivation.
Absence of an identified prior theorem is not a novelty claim.

The unresolved quantitative gate is to find, for actual inverse Toeplitz coefficients, a family of many clean or otherwise conditionally effective row constraints with margins that remain useful as m decreases to zero.
First-lag density is now one but its amplitude is at most2sinh(m).
Later inverse coefficients can be large, yet the actual radical example violates coefficient dominance after a few nonzero lags, and the Gaussian matching control shows that ignoring dependence is invalid.
A new argument could exploit integer lower coefficient constraints, a proved elimination pattern with bounded earlier contamination, or a different joint event statistic.
None is asserted here.
In particular this draft does not combine L268's detection theorem with a new unproved accumulation rule, does not prove a near-one uniform gap, and does not complete G0001.

### Actual whole checking and retained boundaries

The maintaining agent fully read the only L271 version and ENTIRE R170, then compared the sufficient complete fixed C469/C459/C461 mechanisms and actual finite-variational/Fourier/radical/one-expanding/context/source interfaces.
Every clean pointwise event inclusion, displayed pivot order including overlapping row/column sets and ZERO diagonal convention, single distinct-row budget and single whole-law entropy payment was checked for all finite real cubes and shifts.
Every original word weight/first-d constraint deletion/actual T order/pivot bound/disjoint-block and complete suffix count was checked, including short N, q0, weak boundaries, all-future fixed-lag onset and the fixed-input ordered limits.
The first-nonzero polynomial-degree argument, amplitude inequality direction, exact actual radical degree/product/lag signs and complete logarithmic matching countercontrol were checked without numerical evidence.
R170's generic brief/shared history and upstream roles do not establish exact initial additional target content/order or target contribution; its ENTIRE old finding remains UNKNOWN with exact original inputs/date/verdict/full body.
The original complete author SELF and freeze are explicitly2026-10-10T02:26; the separate10:32 review and unknown source-reading minutes are distinct.
No native program/J run, experiment, external source passage/PDF/proof audit/acquisition or research Task/E execution occurred; no new source unit or mathematical repair was necessary.
Current whole SELF supplies no new isolated replacement of the old whole obligation.

## Current assessment
[Selected decision](#decision-current-binary-matching-proof-home-maintenance)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T00:29 |
| status | open |
| reason | Register the complete original joint clean-event/one-KL/actual-law finite-block/density-one/first-lag theorem and every amplitude/radical/matching/source/contribution/negative boundary after sufficient existing mechanisms were compared. All seven sections/28equations remain; actual whole checking and adoption follow separately without research or source expansion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire joint/density theorem](#statement) | All finite real triangular cubes/all shifts/distinct matched rows and columns/exact clean contamination/full-law entropy and original-law finite blocks; every actual positive-measure algebraic integer/fixed dominant lag/first-nonzero lag/all-future onset/density-one and every amplitude/radical/matching/source/negative limit. |
| argument | [Entire original proof](#argument) | Complete original Sections1--7/equations1--28, pointwise clean events/correct product integration/single row and KL budgets, original weights/coordinate and suffix counts/all ordered limits/full actual controls and failed implications. |
| dependency | [Complete arbitrary-coupling/full-law proof](Yin_C_G0469_v1.md#argument) | Entire scalar logarithmic deficit, exact kappa/gamma/K/u/Delta constants, actual reverse-conditional versus scalar-tilt distinction and whole-law inequalities valid for all real shifts and all other entries; no summation of separate single-entry losses. |
| dependency | [Actual word coordinates and fixed diagonal limits](Yin_C_G0459_v1.md#argument) | Complete monic original-word quotient/first-d dropped constraints/integral U and T=R U^-1/pivots/full residual limit including neutral roots/every fixed lag; no uniform effective onset or unit-only state kernel for nonunits. |
| dependency | [Direct versus inverse coefficient proof](Yin_C_G0461_v1.md#argument) | Actual exterior Blaschke product/multiplicities/direct coefficient bound2sinh(m)/first-nonzero coefficient and inverse distinction/actual radical formula, not a bound on all inverse coefficients. |
| dependency | [Finite variational mechanism](Yin_C_G0297_v1.md#disjoint-smoothing-relative-entropy) | Only bounded-test exponential tilting/nonnegative divergence proof, here applied to strictly positive finite laws; no smoothing/stable geometry/Gaussian reference theorem is imported. |
| support | [Elementary finite character orthogonality](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Only finite integer-character integration method; the new matching countercontrol is directly proved on its own product law and does not adopt a conditioned-endpoint law or independence claim. |
| dependency | [Actual radical degree and residue product](Yin_C_G0212_v1.md#radical-collision-control) | Complete norm-minus-one dyadic irreducibility/actual degree2r/relative degree r and exact original probability product at fixed r; no imported numerical bit-rate constant or varying-r limit. |
| support | [One-expanding comparison](Yin_C_G0235_v1.md#one-expanding-comparison) | Only actual real1<beta<2/all other conjugates at most one/total m and stronger leading rate comparison; not extended to arbitrary exterior-root configurations or a uniform horizon. |
| support | [Earlier matching/nonaccumulation context](../ledger/Yin_L_G0215_v1.md#affine-block-matching-defect) | Exact original normalized Holder profile and its bounded total defect are comparison only, not the new joint conditional-product estimate. Preserve this original fixed input while its separate family is maintained. |
| support | [Existing theta source scope](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Original10/10 DLMF1.2.8 formula/notation/application and failed-access/noartifact/book-proof limits inherited through C469, with no new external occurrence, source proof/PDF or acquisition. |
| support | [Related compression context](Yin_C_G0475_v1.md#statement) | Only the separately retained exact inverse detection context, explicitly NOT a premise or unproved accumulation input for this joint theorem. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T00:31 |
| status | proved |
| reason | Adopt after actual complete C487/R699 whole SELF check of all seven original sections/28equations, arbitrary finite real cubes and clean matching/product integration/one row and whole-KL budgets, original word coordinates/nonunit law/all finite blocks/full suffix count/all-future onset/ordered limits/first-nonzero lag/amplitude/actual radical/matching-control/source/contribution/negative scope. The entire old R170 remains UNKNOWN and original author10:26 whole SELF/freeze remains distinct. No new source proof/PDF, program/native run, fresh isolation or research Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire joint/density theorem](#statement) | All finite real triangular cubes/all shifts/distinct matched rows and columns/exact clean contamination/full-law entropy and original-law finite blocks; every actual positive-measure algebraic integer/fixed dominant lag/first-nonzero lag/all-future onset/density-one and every amplitude/radical/matching/source/negative limit. |
| argument | [Entire original proof](#argument) | Complete original Sections1--7/equations1--28, pointwise clean events/correct product integration/single row and KL budgets, original weights/coordinate and suffix counts/all ordered limits/full actual controls and failed implications. |
| dependency | [Complete arbitrary-coupling/full-law proof](Yin_C_G0469_v1.md#argument) | Entire scalar logarithmic deficit, exact kappa/gamma/K/u/Delta constants, actual reverse-conditional versus scalar-tilt distinction and whole-law inequalities valid for all real shifts and all other entries; no summation of separate single-entry losses. |
| dependency | [Actual word coordinates and fixed diagonal limits](Yin_C_G0459_v1.md#argument) | Complete monic original-word quotient/first-d dropped constraints/integral U and T=R U^-1/pivots/full residual limit including neutral roots/every fixed lag; no uniform effective onset or unit-only state kernel for nonunits. |
| dependency | [Direct versus inverse coefficient proof](Yin_C_G0461_v1.md#argument) | Actual exterior Blaschke product/multiplicities/direct coefficient bound2sinh(m)/first-nonzero coefficient and inverse distinction/actual radical formula, not a bound on all inverse coefficients. |
| dependency | [Finite variational mechanism](Yin_C_G0297_v1.md#disjoint-smoothing-relative-entropy) | Only bounded-test exponential tilting/nonnegative divergence proof, here applied to strictly positive finite laws; no smoothing/stable geometry/Gaussian reference theorem is imported. |
| support | [Elementary finite character orthogonality](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Only finite integer-character integration method; the new matching countercontrol is directly proved on its own product law and does not adopt a conditioned-endpoint law or independence claim. |
| dependency | [Actual radical degree and residue product](Yin_C_G0212_v1.md#radical-collision-control) | Complete norm-minus-one dyadic irreducibility/actual degree2r/relative degree r and exact original probability product at fixed r; no imported numerical bit-rate constant or varying-r limit. |
| support | [One-expanding comparison](Yin_C_G0235_v1.md#one-expanding-comparison) | Only actual real1<beta<2/all other conjugates at most one/total m and stronger leading rate comparison; not extended to arbitrary exterior-root configurations or a uniform horizon. |
| support | [Earlier matching/nonaccumulation context](../ledger/Yin_L_G0215_v1.md#affine-block-matching-defect) | Exact original normalized Holder profile and its bounded total defect are comparison only, not the new joint conditional-product estimate. Preserve this original fixed input while its separate family is maintained. |
| support | [Existing theta source scope](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Original10/10 DLMF1.2.8 formula/notation/application and failed-access/noartifact/book-proof limits inherited through C469, with no new external occurrence, source proof/PDF or acquisition. |
| support | [Related compression context](Yin_C_G0475_v1.md#statement) | Only the separately retained exact inverse detection context, explicitly NOT a premise or unproved accumulation input for this joint theorem. |
| review | [Actual entire whole SELF](../audits/reviews/Yin_R_G0699_v1.md#joint-clean-density-whole-self-finding) | Entire exact statement/argument/selected fixed inputs, all Sections1--7/equations1--28 and every all-real/overlap/zero/short-N/original-law/nonunit/lag/onset/density/amplitude/radical/matching/source/negative boundary; no fresh isolated replacement or summary-only review. |


### Decision current-binary-matching-proof-home-maintenance

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:56 |
| status | proved |
| reason | Maintain only the same-object current L215 interface at the now complete C522 proof home after full scope comparison: original normalized Holder matching profile and bounded total-defect COMPARISON ONLY, not this joint conditional-product theorem. Preserve all mathematical assertions, all other current fields and tuples, exact relation role/scope, every prior decision and every old R binding/date/actual input. Existing review findings retain their actual scopes and do not claim to have read C522. This proof-home/input-locator maintenance supplies no new mathematical verdict, fresh isolated review, source reading, native execution or research Task/E. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | All finite real triangular cubes/all shifts/distinct matched rows and columns/exact clean contamination/full-law entropy and original-law finite blocks; every actual positive-measure algebraic integer/fixed dominant lag/first-nonzero lag/all-future onset/density-one and every amplitude/radical/matching/source/negative limit. |
| argument | [Exact retained argument](#argument) | Complete original Sections1--7/equations1--28, pointwise clean events/correct product integration/single row and KL budgets, original weights/coordinate and suffix counts/all ordered limits/full actual controls and failed implications. |
| dependency | [Exact retained dependency](Yin_C_G0469_v1.md#argument) | Entire scalar logarithmic deficit, exact kappa/gamma/K/u/Delta constants, actual reverse-conditional versus scalar-tilt distinction and whole-law inequalities valid for all real shifts and all other entries; no summation of separate single-entry losses. |
| dependency | [Exact retained dependency](Yin_C_G0459_v1.md#argument) | Complete monic original-word quotient/first-d dropped constraints/integral U and T=R U^-1/pivots/full residual limit including neutral roots/every fixed lag; no uniform effective onset or unit-only state kernel for nonunits. |
| dependency | [Exact retained dependency](Yin_C_G0461_v1.md#argument) | Actual exterior Blaschke product/multiplicities/direct coefficient bound2sinh(m)/first-nonzero coefficient and inverse distinction/actual radical formula, not a bound on all inverse coefficients. |
| dependency | [Exact retained dependency](Yin_C_G0297_v1.md#disjoint-smoothing-relative-entropy) | Only bounded-test exponential tilting/nonnegative divergence proof, here applied to strictly positive finite laws; no smoothing/stable geometry/Gaussian reference theorem is imported. |
| support | [Exact retained support](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Only finite integer-character integration method; the new matching countercontrol is directly proved on its own product law and does not adopt a conditioned-endpoint law or independence claim. |
| dependency | [Exact retained dependency](Yin_C_G0212_v1.md#radical-collision-control) | Complete norm-minus-one dyadic irreducibility/actual degree2r/relative degree r and exact original probability product at fixed r; no imported numerical bit-rate constant or varying-r limit. |
| support | [Exact retained support](Yin_C_G0235_v1.md#one-expanding-comparison) | Only actual real1<beta<2/all other conjugates at most one/total m and stronger leading rate comparison; not extended to arbitrary exterior-root configurations or a uniform horizon. |
| support | [Exact retained support](Yin_C_G0522_v1.md#affine-block-matching-defect) | Exact original normalized Holder profile and its bounded total defect are comparison only, not the new joint conditional-product estimate. Preserve this original fixed input while its separate family is maintained. |
| support | [Exact retained support](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Original10/10 DLMF1.2.8 formula/notation/application and failed-access/noartifact/book-proof limits inherited through C469, with no new external occurrence, source proof/PDF or acquisition. |
| support | [Exact retained support](Yin_C_G0475_v1.md#statement) | Only the separately retained exact inverse detection context, explicitly NOT a premise or unproved accumulation input for this joint theorem. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0699_v1.md#joint-clean-density-whole-self-finding) | Entire exact statement/argument/selected fixed inputs, all Sections1--7/equations1--28 and every all-real/overlap/zero/short-N/original-law/nonunit/lag/onset/density/amplitude/radical/matching/source/negative boundary; no fresh isolated replacement or summary-only review. |

