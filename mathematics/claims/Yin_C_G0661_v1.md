---
author: Yin
---

# Removing the actual Gram-ratio pole yields a decaying relative-variation budget

Human author Yin.
Root proposed seeking quantitative same-input relative contact control after C660.
Phase_bands supplied and checked the exact pole subtraction, the uniform bounded polynomial remainder, the mean-to-variation estimate and its complete finite return.
Both are contributors, not independent reviewers.
No native computation, new source acquisition or original-source proof inspection is used.

## Statement

Retain the ENTIRE three-family input contract and definitions of adopted [C660](Yin_C_G0660_v1.md#statement).
In particular the original polynomial is the actual source-certified Salem minimal polynomial P, its degree is d=c+L-3, and its full relation matrix has ALL d columns in the ORIGINAL2d coordinates.
The three actual c schedules are the least primes above

    (L+1)^2,
    ceil((L+1)^(25/11)),
    ceil((L+1)^(21/11))*ceil(log_2(L+1)).

Their common K,a,b,L,M are exactly those specified in C660; hence

    K>=16, L>4K^2, c>L, c<d<2c, M=floor(a/4).

All circle and torus measures have mass one, Fourier coefficients use negative exponentials, and angular variation V is unnormalized.
Use the SAME original quantities

    G=A_rel^T A_rel, Pi=A_rel G^-1 A_rel^T,
    h_orig(z)=v_(2d)(z)^*Pi v_(2d)(z)/(2d),
    G_d(z)=v_d(z)^*G^-1 v_d(z),
    h_phase=(1+Re(z^c varphi(z)))/2,
    r(z)=2abs(A_0(z))^2G_d(z)/[d abs(z-1)^2], z!=1,
    h_orig=r*h_phase,
    f_tau=(1-h_orig/tau)_+, F_tau^phase=(1-h_phase/tau)_+.

A_0,varphi and all their arithmetic/source conventions are those of the actual C660 phase.
In particular A_0 has real coefficients and no circle zero.
The identity does not divide by P and remains valid at its unit-circle roots.
The point1 is an actual pole of r, with h_orig(1)>0.

Write the exact phase lift as

    Theta(t)=ct+psi(t), psi(0)=pi, psi'(t)>0,
    v_0=Theta'(0)=c+1/(1/K+1/a+1/b).

The extra phase cell I_0 around1 and all genuine-root cells are exactly those of C660.
No moving-family estimate below is inferred from a fixed-j Taylor limit.

### Exact pole subtraction and a uniform remainder

Let h_0=h_orig(1) and define

    kappa=4h_0/v_0^2, 0<kappa<=4/c^2,
    u(t)=kappa/[4sin^2(t/2)], 0<abs(t)<=pi,
    sigma(t)=r(exp(it))-u(t).

Then sigma extends to a REAL EVEN trigonometric polynomial of degree at most

    n_sigma=d+L-4=c+2L-7<3c,

and satisfies the actual uniform estimate

    ||sigma||_infinity<=700.                                (PV1)

The pole is retained exactly in u; it is not discarded or replaced by a uniform r close to1 assumption.

Define the already paid original comparison constants

    E=[1+pi L(5+2log c)]/c, epsilon=(4L-5)/(2d)+E/2,
    A_epsilon=min{1,inf_(0<s<=1)
                       [(1+(L-4)/c)sqrt(s)+epsilon/s]},
    H_c=1+log(6c).

Then

    ||sigma-1||_1<=14A_epsilon+703/c,
    V(sigma)<=60pi c H_c(14A_epsilon+703/c).                 (PV2)

In particular, when epsilon<=1, A_epsilon<=3epsilon^(1/3).
All quantities and constants are finite and specified at the actual input.

### A genuinely decaying relative-variation bound

Retain the same relative error from C660,

    eta_r=abs(r-1)/max{1,r}, w_r=eta_r^(4/3),
    eta_r(1)=w_r(1)=1,
    B_rel=integral w_r dnu_1+[(L-4)+V(w_r)]/c.

Then

    integral eta_r<=A_epsilon, integral w_r<=A_epsilon,
    V(w_r)<=(4/3)V(sigma)+4000.                             (PV3)

Consequently the explicit fully paid bound is

    B_rel<=Xi_j,
    Xi_j=A_epsilon+L/c
                  +80pi H_c(14A_epsilon+703/c)+4000/c.       (PV4)

For the three ACTUAL sequences, Xi_j tends to zero.
Writing T_M=1+log M, the following precise uniform-order consequences hold, with constants independent of j:

    square:          Xi_j=O_K(M^(-2/3)T_M^(4/3)),
    25/11:           Xi_j=O_K(M^(-28/33)T_M^(4/3)),
    21/11 with log:  Xi_j=O_K(M^(-20/33)T_M).                (PV5)

Equation(PV4) is the finite estimate; these O_K statements do not replace its constants.
They improve C660's nondecaying degree bound for V(w_r)/c.
They do NOT prove a lower bound for lambda=min{1,inf_(z!=1)r(z)} independent of j, or decay of lambda^(-1/2)B_rel.

### The small-r region and all five finite-return costs

For every0<tau<=1, one has the unconditional lower-ratio-free comparison

    integral abs(f_tau-F_tau^phase)^(4/3)
                 <=sqrt(2tau)Xi_j+2A_epsilon.               (PV6)

Its second term explicitly pays the possible small-r region; it is not suppressed as a contact-width term.

For M>=max{2,C_w} and0<tau<=1/64, retain EXACTLY C660's constants, finite squared-Fejer kernel, rho, torus regularization and maps iota,H.
In particular C_2=2*2048^(3/4)C_w+2C_s pays both regularizations and both smoothings.
Also put

    V_bar=80pi L[1+log(4d)]+pi c E
              +26pi(L-4)[1+log(2c)]+2pi+pi(L-4),
    B_bar=epsilon+[V_bar+L-4]/c,
    E_pole(j,tau)=min{
       (32B_bar)^(3/4)tau^(-3/8),
       tau^(3/8)lambda^(-3/8)Xi_j^(3/4),
       [sqrt(2tau)Xi_j+2A_epsilon]^(3/4)}.

For EVERY finite Gamma in the CLOSED integer box[-M,M]^4,

    sum_(gamma in Gamma)
       abs(fhat_tau(H(gamma))-Fhat_tau(gamma))
       <=8 card(Gamma)^(3/4)
                        [E_pole(j,tau)+C_2 M^-1 tau^-1/8].  (PV7)

Every zero/negative harmonic, box endpoint and empty set is included.
All supplied original frequencies are distinct.

For the ENTIRE actual C638 centered support, retain its exact n_(k,m), and put

    L_tau=floor(1/(4sqrt(tau))), integer J>=2,
    C_loc=ceil(32000pi+1024pi(K+4)),
    C_sup=8[9(C_loc+1)^2]^(3/4)4^(-9/8),
    R_z=ceil(C_loc J^(1/3)), R_u=ceil(C_loc sqrt(L_tau)J^(5/6)),
    G_(L_tau,J)={(-p,-q,m,k):1<=k<=L_tau,1<=m<=J,
                               abs(p)<=R_z,abs(q-n_(k,m))<=R_u},
    N_sel=L_tau J(2R_z+1)(2R_u+1).

Whenever

    R_z,J,L_tau<=M, 14(L_tau+J)+R_u<=M,

the original selected frequencies are distinct and positive, and

    W_*(f_tau)>=3log(J+1)/(32768pi)
       -8N_sel^(3/4)[E_pole(j,tau)+C_2 M^-1 tau^-1/8].       (PV8)

The complete error is at most

    C_sup J^(13/8)[
       min{(32B_bar)^(3/4)tau^(-15/16),
           lambda^(-3/8)Xi_j^(3/4)tau^(-3/16),
           tau^(-9/16)[sqrt(2tau)Xi_j+2A_epsilon]^(3/4)}
                                         +C_2 M^-1 tau^(-11/16)]. (PV9)

These are finite actual-input inequalities.
No new shrinking-width exponent is concluded without a stronger small-r estimate or a paid lower-ratio bound.
All existing actual-degree criteria remain available from the first branch.
The three actual families still satisfy log2<m(P)<log4 and retain the complete2d original probability laws.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Complete argument

### 1. The exact finite polynomial after removing the pole

Set T(t)=2|A_0(exp(it))|^2G_d(exp(it)).
Because A_0 and G^-1 are real, T is an even real trigonometric polynomial of degree at most N=d+L-3.
It is strictly positive.
The exact ratio is r=T/[d|exp(it)-1|^2].

Every cos(nt) is a polynomial in cos t by the recurrence cos((n+1)t)=2cos t cos(nt)-cos((n-1)t).
Thus T(t)-T(0) is divisible by cos t-1 as such a polynomial.
Since |exp(it)-1|^2=2(1-cos t),

    sigma(t)=[T(t)-T(0)]/[d|exp(it)-1|^2]

extends to a real even trigonometric polynomial of degree at most N-1=n_sigma.
The remaining pole coefficient is kappa=T(0)/d.
By the actual smooth phase expansion at1, h_phase(exp(it))/t^2 tends to v_0^2/4, while h_orig(exp(it)) tends to h_0.
The identity h_orig=r h_phase therefore gives kappa=4h_0/v_0^2.
This calculation identifies an exact finite coefficient; it does not apply a nonuniform Taylor approximation in a moving-width estimate.
The inequalities0<h_0<=1 and v_0>=c prove0<kappa<=4/c^2.

### 2. Explicit uniform phase estimates on the shrinking extra cell

All inequalities below hold at EVERY actual input and every |t|<=pi/c.
They are uniform inequalities, not fixed-input remainder assertions.

Put

    R_0^phase=2(1/K+1/a+1/b)>=2/K,
    D(t)=4sin t+cot(Kt/2)+cot(at/2)+cot(bt/2).

For0<|x|<=pi/2, the identity sin x-x cos x=integral_0^x s sin s ds and sin|x|>=2|x|/pi give

    abs(cot x-1/x)<=pi abs(x)/6.

Every e in{K,a,b} is less than c, so e|t|/2<=pi/2.
Consequently

    D(t)=R_0^phase/t+E_phase(t),
    abs(E_phase(t))<=(L+4)|t|.                              (PV10)

Here4|sin t|<=4|t| and the three cotangent errors sum to at most pi(K+a+b)|t|/12< L|t|.
Since L>4K^2,K>=16,c>L and pi^2<10,

    (L+4)t^2/R_0^phase
       <=(L+4)pi^2 K/(2c^2)
       <pi^2 K/L<pi^2/(4K)<1/2.                            (PV11)

Thus tD(t)>0 and |1/D(t)|<=2|t|/R_0^phase.
The actual continuous phase increment near1 is exactly

    p(t):=Theta(t)-pi=ct+2arctan(1/D(t)),

with its continuous value0 at t=0.
Use |arctan y-y|<=|y|^3/3 and(PV10)--(PV11).
The resulting bounds are

    abs(p(t)-v_0 t)
       <=[K^2(L+4)+(2/3)K^3]|t|^3
       <=3K^2 L|t|^3,
    v_0=c+2/R_0^phase<=2c,
    abs(p(t))<=3c|t|.                                      (PV12)

For the last inequality, the cubic error divided by |t| is at most3K^2L pi^2/c^2<=c.
Indeed c>L and L>4K^2 imply c^3> L^3>3pi^2 K^2L.
These explicitly checked estimates are valid also at0 by continuity.

The function p is odd and strictly increasing.
The extra cell therefore has the form I_0=[-t_*,t_*] on[-pi,pi], with p(t_*)=pi.
The existing lower phase derivative p'>=c and(PV12) imply

    pi/(3c)<=t_*<=pi/c.                                    (PV13)

On this cell |p(t)|<=pi, so h_phase=sin^2(p(t)/2)>=c^2t^2/pi^2.
Also v_0^2sin^2(t/2)>=c^2t^2/pi^2.

The elementary estimate |sin^2 x-x^2|<=|x|^4/3 follows from |sin x-x|<=|x|^3/6 and |sin x+x|<=2|x|.
Together with(PV12), it gives on I_0

    abs(h_phase-v_0^2sin^2(t/2))
       <=[4K^2Lc+2c^4]t^4<=6c^4t^4.                       (PV14)

In detail, the difference of the quadratic terms costs at most(15/4)K^2Lc t^4.
The two sine remainders cost at most(81c^4+4c^2)t^4/48<2c^4t^4.
Finally K^2L<=c^3 follows from c>L>4K^2.
Every constant is uniform in j and t.

### 3. Uniform control of sigma on and off the extra cell

Let N=2d, mu=(N-1)/2 and v_cent(t)=(exp(i(n-mu)t))_(n=0)^(N-1).
It differs from the original v_N only by a unit scalar, so h_orig=||Pi v_cent||^2/N.
The projection is a contraction, ||v_cent'||<=mu sqrt(N), and ||v_cent''||<=mu^2 sqrt(N).
Twice differentiating the finite quadratic expression yields

    abs(h_orig''(t))<=4mu^2<4d^2.

Because Pi is real, h_orig is even and h_orig'(0)=0.
Therefore

    abs(h_orig(exp(it))-h_0)<=2d^2t^2.                      (PV15)

This uses the full original projection; no external Bernstein theorem or Gram conditioning is used.

For0<|t|<=t_* write the exact identity

    sigma=(h_orig-h_0)/h_phase
             +h_0[1/h_phase-1/(v_0^2sin^2(t/2))].

The equality uses kappa=4h_0/v_0^2.
The first term has absolute value at most2pi^2d^2/c^2<8pi^2.
By(PV14) and the two lower denominator bounds after(PV13), the second is at most6pi^4, since h_0<=1.
Thus

    abs(sigma)<=8pi^2+6pi^4<680<700 on I_0.                 (PV16)

The value at0 follows from the polynomial extension.

Outside I_0, the actual C660 genuine-root-cell estimate gives0<r<=pi^2(4d^2-1)/(12c^2)<14.
By(PV13) and sin(|t|/2)>=|t|/pi,

    0<u(t)<=kappa pi^2/(4t^2)<=9.

Hence -9<=sigma<=14 outside I_0.
Together with(PV16) this proves(PV1) globally.

### 4. Small L1 norm of the remainder and its finite variation

The exact same-circle occupation bound from C656/C660, applied with weight1, is

    nu_1{h_phase<=s}<=(1+(L-4)/c)sqrt(s), 0<s<=1.

Away from the null point1, the actual additive error e=|h_orig-h_phase| equals h_phase |r-1|.
Since eta_r<=min(1,e/h_phase), splitting at h_phase<=s gives

    integral eta_r<=(1+(L-4)/c)sqrt(s)+epsilon/s.

Here integral e<=epsilon is the actual original comparison already paid for EACH of the three families.
Also eta_r<=1.
Taking the infimum proves integral eta_r<=A_epsilon, and w_r<=eta_r proves its asserted mean bound.
If epsilon<=1, set s=epsilon^(2/3).
Since(L-4)/c<1, this gives A_epsilon<=3epsilon^(1/3).

On I_0 one has |sigma-1|<=701 and nu_1(I_0)<=1/c.
On its complement, |sigma-1|<=|r-1|+u<=14eta_r+u.
Put delta=pi/(3c).
The entire pole tail is explicitly paid:

    integral_(abs(t)>=delta) u(t)dnu_1
       =kappa cot(delta/2)/(2pi)
       <=kappa/(pi delta)<=12/(pi^2c)<2/c.                  (PV17)

The inequality cot x<=1/x is valid on(0,pi/2].
Since t_*>=delta, this bounds the actual complement integral.
Combining the inside and outside regions proves ||sigma-1||_1<=14A_epsilon+703/c.

The elementary C656 finite Dirichlet proof states, for every trigonometric polynomial T of degree at most n>=1,

    V(T)<=20pi n[1+log(2n)]||T||_1.

Apply this to sigma-1 with the actual allowed n=n_sigma<3c.
Its derivative equals that of sigma, giving the second line of(PV2).
All finite degree and logarithmic costs remain explicit.

### 5. Relative differentiation pays the pole with a constant

Put p_exp=4/3 and define g(r)=(1-min(r,1/r))^(p_exp), for r>0.
This is continuously differentiable, including at r=1, and

    abs(g'(r))<=p_exp for all r>0,
    abs(g'(r))<=p_exp/r^2 when r>=1.

Since r=u+sigma and |sigma|<=700, if u>=T_*=1402 then r>=u-700>=u/2>=1.
In that region |g'(r)|<=4p_exp/u^2.
Elsewhere the first derivative bound applies.

On each open half circle, u is monotone from infinity to kappa/4 or in the reverse direction.
Thus, after changing variables to u in the pole part,

    integral_T abs(g'(r))abs(u')dt
       <=2[p_exp T_*+4p_exp/T_*]<4000.                      (PV18)

The integral here is UNNORMALIZED angular measure, as required for variation.
Using the whole interval[0,T_*] only enlarges the integral if the actual minimum u=kappa/4 is positive.
The sigma derivative contribution is bounded by p_exp V(sigma).
The continuous limit of w_r at0 is1; the displayed integrable derivative bounds justify passage to that endpoint.
The chain rule and(PV18) therefore give V(w_r)<=(4/3)V(sigma)+4000, proving(PV3).

Substitution of(PV2) and the mean bound into the definition of B_rel gives exactly(PV4).
In particular the actual second-order pole creates a constant variation expense after the bounded relative transformation, rather than the former O(d) degree expense.

### 6. Actual uniform decay for all three families

The finite estimates proved so far depend only on the full original objects, c>L, L>4K^2 and their adopted same-circle inputs.
To derive the displayed rates, retain C_epsilon=3+3pi.
The exact scalar simplification from C656 gives for each family

    epsilon<=C_epsilon(L/c)(1+log c).                       (PV19)

For the square and25/11 schedules the actual prime/degree bounds give, respectively,

    L/c<=M^-2 or M^(-28/11),
    1+log c<=64(1+log M).

Thus epsilon=O_K(M^-alpha T_M), with alpha=2 or28/11.
For the21/11 logarithmic family, the proved actual threshold in C658 gives

    (L/c)(1+log c)<=5M^(-20/11),
    H_c=O_K(T_M), c>M^(42/11)T_M.

All epsilons tend to zero, so eventually their cube-root bounds apply.
The same prime bounds give c>M^4 for the square schedule and c>M^(50/11) for25/11.
Inserting these inequalities in the EXPLICIT(PV4) yields exactly(PV5).
The L/c and H_c/c terms decay faster than the displayed cube-root term in each case.
No unspecified onset is used in the finite formula(PV4); only the convenient asymptotic notation uses eventual epsilon<=1.

This is an actual bound for B_rel tending to zero in each family.
It says nothing by itself about the inverse lower ratio multiplying that quantity.

### 7. The small-r split and the complete finite return

Split the original circle into r>=1/2 and r<1/2, ignoring the single null point1 for this notation.
On the first set, the scalar cap comparison from C660 has magnitude at most eta_r and can be nonzero only when h_phase<=2tau.
The same-circle weighted occupation therefore bounds its fourth-thirds integral by sqrt(2tau)B_rel<=sqrt(2tau)Xi_j.
This holds also when2tau>1.

On r<1/2 one has eta_r>1/2, so that event has probability at most2 integral eta_r<=2A_epsilon.
The cap difference is at most1, so its fourth-thirds integral on that event has the same bound.
This proves(PV6).
It is essential that the second term has no extra sqrt(tau) factor.

The other two original comparison alternatives are the adopted additive BV estimate and C660's relative estimate with B_rel replaced by its actual upper bound Xi_j.
Taking the minimum of these three valid strong L^(4/3) bounds gives E_pole.
Both regularization costs and both smoothing costs remain exactly C_2 M^-1 tau^-1/8.
No other finite kernel, rho or probability law changes.

Each specified family already has the complete closed2M no-alias inequalities, and the finite polynomial Q has closed-M support.
The finite weak-Fourier estimate on the two error spaces is8 card(Gamma)^(3/4) times their event-norm sum.
Strong L^(4/3) bounds control those event norms.
This proves(PV7) for every stated finite set and every endpoint.

For the entire centered C638 support, the exact center-plus-radius conditions place every selected index in the box.
Every fourth coordinate k is positive, so all actual images are strictly positive and distinct.
The full torus mass is3log(J+1)/(32768pi), proving(PV8).
Finally, 8N_sel^(3/4)<=C_sup J^(13/8)tau^-9/16.
Multiplying EVERY original alternative and the full remaining four-cost sum proves(PV9).
This retains the complete support price and does not silently declare a new actual-degree criterion.

## Reuse and remaining obstruction

The focused reuse inputs are adopted C660's exact ratio/pole, genuine-cell geometry and full finite-return interfaces, and C656's explicitly proved finite Dirichlet derivative inequality.
The cotangent estimate, uniform small-cell estimates and pole subtraction are proved directly above.
The original projection derivative estimate uses only the complete finite matrix and centered evaluation vector.
No source model-space theorem, inverse-Toeplitz estimate or uniform fixed-j Taylor theorem is invoked.
All original source and SELF-versus-independent boundaries of the reused materials remain at their actual scopes.

This completes a genuine quantitative control absent from C660: the normalized relative variation, and hence B_rel, now decay uniformly along the three actual families.
The fixed pole remains present with its exact coefficient.
The global lower ratio lambda, or a sufficiently strong weighted estimate specifically on its small-value cells, is still unresolved.
The ratio-free split(PV6) pays that missing region by2A_epsilon and does not pretend to retain a contact-width factor there.
Neither the new decaying variation nor the existing fixed-input contact profile alone yields the unproved joint estimate.
No new width exponent, near-one family or unrestricted G0001 conclusion is claimed.

## Assessment history

### Decision pole-relative-variation-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T00:46 |
| status | open |
| reason | Register the exact actual pole subtraction and finite polynomial remainder, uniform bound700 with explicit shrinking-cell estimates, quantitative mean-to-variation bounds and decaying B_rel rates for all three actual families. The small-r alternative and all five finite costs/entire support are retained. Author checking is complete; fresh independent whole review remains required. No uniform lower ratio, new width exponent, near-one family or unrestricted conclusion is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire pole-removal statement](#statement) | PV1--PV9: all three actual full2d families, exact nonremoved pole, bounded polynomial remainder, complete finite relative-variation constants and rates, small-r term and every finite Gamma/full support cost. |
| argument | [Complete argument](#complete-argument) | Sections1--7/PV10--PV19: even-polynomial division, exact pole coefficient, uniform cotangent and projection estimates, inside/outside cell accounting, mean and Dirichlet variation, transformed-pole integral, all family rates and all finite expenses. |
| dependency | [Adopted actual ratio interface](Yin_C_G0660_v1.md#decision-whole-reviewed-2026-10-24) | Exact full Gram/phase ratio, real finite objects, actual pole and v0, genuine-cell bound and widths, weighted occupation and complete five-cost return for all three families. |
| dependency | [Finite Dirichlet and original BV proof](Yin_C_G0656_v1.md#complete-argument) | Explicit elementary degree-n derivative bound and exact finite epsilon simplification; no uninspected general Bernstein theorem. |
| dependency | [Actual new logarithmic family](Yin_C_G0658_v1.md#decision-whole-reviewed-2026-10-24) | Exact integer prime threshold, actual degree and original-law reconstruction, paid logarithmic budget and source/measure limits used in the new decay rate. |
| dependency | [Actual square and25/11 schedules](Yin_C_G0648_v1.md#decision-whole-reviewed-2026-10-23) | Same actual polynomials and c,L,M bounds, original2d comparison and all translated/kernel/alias inputs, with source depth unchanged. |
| dependency | [Four retained comparison costs](Yin_C_G0641_v2.md#combined-argument) | Complete finite weak Fourier mechanism and smoothings, with the additional joint-shell proof retaining both regularizations and all translated-law conditions. |
| dependency | [Both joint-shell regularizations](Yin_C_G0641_v2.md#complete-additional-joint-shell-argument) | Exact all-scale rho/tau regularization constants and no omitted shell. |
| dependency | [Entire centered torus bands](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | All actual n_(k,m), radii, complete selected cardinality and mass, with full original closed-box return retained. |
| support | [Remaining small-r interface](#reuse-and-remaining-obstruction) | Genuine uniform B_rel decay versus still-uncontrolled lambda and explicitly paid bad-region probability; no joint-limit or new-width inference. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T00:59 |
| status | proved |
| reason | Adopt the entire actual pole-subtraction and decaying relative-variation theorem after complete main-agent reading and fresh independent whole R880. The exact pole remains; the uniformly bounded polynomial remainder, all cotangent/projection and interval constants, complete mean/variation integrals, three actual-family rates and all five finite-return costs/entire support are established. B_rel now has an explicit bound tending to zero. The global lower ratio and a stronger small-r contact estimate remain unresolved, with the actual small-r cost2A_epsilon paid without a width factor. No new width exponent, near-one input family or unrestricted completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire pole-removal statement](#statement) | PV1--PV9: all three actual full2d families, exact nonremoved pole, bounded polynomial remainder, complete finite relative-variation constants and rates, small-r term and every finite Gamma/full support cost. |
| argument | [Complete argument](#complete-argument) | Sections1--7/PV10--PV19: even-polynomial division, exact pole coefficient, uniform cotangent and projection estimates, inside/outside cell accounting, mean and Dirichlet variation, transformed-pole integral, all family rates and all finite expenses. |
| dependency | [Adopted actual ratio interface](Yin_C_G0660_v1.md#decision-whole-reviewed-2026-10-24) | Exact full Gram/phase ratio, real finite objects, actual pole and v0, genuine-cell bound and widths, weighted occupation and complete five-cost return for all three families. |
| dependency | [Finite Dirichlet and original BV proof](Yin_C_G0656_v1.md#complete-argument) | Explicit elementary degree-n derivative bound and exact finite epsilon simplification; no uninspected general Bernstein theorem. |
| dependency | [Actual new logarithmic family](Yin_C_G0658_v1.md#decision-whole-reviewed-2026-10-24) | Exact integer prime threshold, actual degree and original-law reconstruction, paid logarithmic budget and source/measure limits used in the new decay rate. |
| dependency | [Actual square and25/11 schedules](Yin_C_G0648_v1.md#decision-whole-reviewed-2026-10-23) | Same actual polynomials and c,L,M bounds, original2d comparison and all translated/kernel/alias inputs, with source depth unchanged. |
| dependency | [Four retained comparison costs](Yin_C_G0641_v2.md#combined-argument) | Complete finite weak Fourier mechanism and smoothings, with the additional joint-shell proof retaining both regularizations and all translated-law conditions. |
| dependency | [Both joint-shell regularizations](Yin_C_G0641_v2.md#complete-additional-joint-shell-argument) | Exact all-scale rho/tau regularization constants and no omitted shell. |
| dependency | [Entire centered torus bands](Yin_C_G0638_v1.md#complete-local-modulation-calculation) | All actual n_(k,m), radii, complete selected cardinality and mass, with full original closed-box return retained. |
| support | [Remaining small-r interface](#reuse-and-remaining-obstruction) | Genuine uniform B_rel decay versus still-uncontrolled lambda and explicitly paid bad-region probability; no joint-limit or new-width inference. |
| review | [Independent entire pole-variation finding](../audits/reviews/Yin_R_G0880_v1.md#pole-relative-variation-whole-independent-finding) | Whole PV1--PV19 and Sections1--7, exact full original objects and pole, uniform700 and4000 constants, all normalized/unnormalized integrals and actual rates, complete five-cost return and support, source depth and lower-ratio/small-r limits. |

