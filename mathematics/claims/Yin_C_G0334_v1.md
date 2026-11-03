---
author: Yin
---

# Complete tunable-tail Fourier certificate and the conditional finite Salem transition target

This retains the complete original 2026-10-08 [L129 mathematical argument](../ledger/Yin_L_G0129_v1.md).
The original entropy_status agent derived the complete finite guards and Salem comparison for Yin from the coordinator tunable-tail mechanism.
No current Task/E execution, source acquisition, algorithm enumeration or mathematical program run is selected by this maintenance.

## Statement

Fix a positive-Mahler algebraic unit alpha with monic irreducible P, degree d, q>0 central conjugates and stable/expanding conjugates, counting every complex embedding.
For every 0<delta<=1/16, 0<kappa<=1/(16q), 0<eta<1 and integer N>=1, let a nonzero integral theta have central conjugates at most kappa/sqrt(N) and all conjugates at most H>=1.
The exact enlarged J_delta, two finite endpoint guards, actual noise condition and count (2),(6)--(9) give the every-window actual-amplitude certificate (10) and necessary original-law consistency inequality (11).
The finite coefficient-box construction (12) supplies such multipliers with polynomial height at fixed input, without replacing any finite guard by an asymptotic count.
For a hypothetical Salem input with 0<m<=1/32, the precise choices (13) give E_delta=5m/256, A_delta>1/sqrt2, ell0<2/m and C_ent(m)<8m^3.
At every window satisfying all three finite guards (17), any actual enlarged transition product must satisfy C_delta(theta)<16m; a proved lower bound C_delta>=16m there would contradict (11).
The artificial ceiling one eventually passes this modified test, but no actual multiplier is asserted to attain it or the target lower bound.
The main certificate keeps all tail, height, transition-length, noise, whitening, endpoint and actual finite count costs.
No negative-time stable-norm version, unrestricted multiple-expanding Salem specialization, positive limiting amplitude, original entropy equality or uniform Mahler gap is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:38 |
| status | open |
| reason | Retain the complete exact original theorem and argument; actual current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(20), every subsequent compatibility statement, exact general-unit finite guards and conditional Salem parameter/cost comparison; enlarged transition product and all original-law/actual-amplitude limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(20), every subsequent compatibility statement, exact general-unit finite guards and conditional Salem parameter/cost comparison; enlarged transition product and all original-law/actual-amplitude limits. |
| dependency | [Exact retained input](Yin_C_G0321_v1.md#central-whitening-fourier-test) | Complete exact all-unit KL/noise/whitening and weighted actual-amplitude comparison. |
| dependency | [Exact retained input](Yin_C_G0328_v1.md#polynomial-height-central-approximation) | Exact central coefficient-box height construction and correct mixed trace/noise/frequency normalizations. |
| dependency | [Exact retained input](Yin_C_G0305_v1.md#quantitative-convolution-entropy-convergence) | Exact original-law k=1 algebraic entropy upper comparison, not toral equality. |
| dependency | [Exact retained input](Yin_C_G0330_v1.md#subexponential-height-mixed-budget-collapse) | Complete collapse compatibility at fixed P; it does not prevent a single finite test or supply an amplitude lower bound. |
| dependency | [Exact retained input](Yin_C_G0332_v1.md#retained-certificate-universal-ceiling) | Only the exact earlier unchanged-constant ceiling, which remains valid in its own scope. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:48 |
| status | proved |
| reason | Adopt the complete exact original theorem and retained argument after actual whole self-review of every stated scope and used interface; preserve every finite guard, unexecuted algorithm, original checking input and nonuniformity limitation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(20), every subsequent compatibility statement, exact general-unit finite guards and conditional Salem parameter/cost comparison; enlarged transition product and all original-law/actual-amplitude limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(20), every subsequent compatibility statement, exact general-unit finite guards and conditional Salem parameter/cost comparison; enlarged transition product and all original-law/actual-amplitude limits. |
| dependency | [Exact retained input](Yin_C_G0321_v1.md#central-whitening-fourier-test) | Complete exact all-unit KL/noise/whitening and weighted actual-amplitude comparison. |
| dependency | [Exact retained input](Yin_C_G0328_v1.md#polynomial-height-central-approximation) | Exact central coefficient-box height construction and correct mixed trace/noise/frequency normalizations. |
| dependency | [Exact retained input](Yin_C_G0305_v1.md#quantitative-convolution-entropy-convergence) | Exact original-law k=1 algebraic entropy upper comparison, not toral equality. |
| dependency | [Exact retained input](Yin_C_G0330_v1.md#subexponential-height-mixed-budget-collapse) | Complete collapse compatibility at fixed P; it does not prevent a single finite test or supply an amplitude lower bound. |
| dependency | [Exact retained input](Yin_C_G0332_v1.md#retained-certificate-universal-ceiling) | Only the exact earlier unchanged-constant ceiling, which remains valid in its own scope. |
| review | [Actual current whole self-check](../audits/reviews/Yin_R_G0556_v1.md#current-tunable-tail-finding) | Complete current statement, retained proof and directly used inputs; self-reviewed. Original findings retain their actual original dates, inputs, corrections and checking relationships. |

## Complete retained argument

<a id="argument"></a>
<a id="tunable-tail-finite-certificate"></a>
### A tunable tail certificate with its actual finite guards

Use the domain of [L G0123](Yin_C_G0328_v1.md#mixed-trace-transition-product).
Thus alpha is an algebraic unit with monic irreducible polynomial P, degree d, and m=log M(P)>0.
There are q>0 central embeddings, s>0 stable embeddings and u>0 expanding embeddings.
All counts include both members of every complex pair, and h=s+u=d-q.
All logarithms are natural.

Choose

    0<delta<=1/16,  0<kappa<=1/(16q),  0<eta<1.       (1)

For an integer N>=1 let epsilon_N=kappa/sqrt(N).
Let theta be a nonzero algebraic integer in Q(alpha) whose central conjugates have modulus at most epsilon_N, and let H>=1 bound all its conjugate moduli.
For all integer j write

    u_j=sum_stable sigma(theta) sigma(alpha)^j,
    v_j=sum_expanding sigma(theta) sigma(alpha)^j,
    w_j=sum_central sigma(theta) sigma(alpha)^j.

These are real numbers.
Since alpha is a unit, even the negative powers are algebraic integers, and

    u_j+v_j+w_j=Tr(theta alpha^j) in Z.

Put

    rho=max(max_stable |beta|, max_expanding |beta|^(-1)),
    rho_s=max_stable |beta|,
    J_delta=ceil(log(dH/delta)/(-log rho)),
    ell_0=ceil(log(4 sqrt(2))/(-log rho_s)),
    C_delta(theta)=product_(j=-J_delta)^(-1)|cos(2pi v_j)|
                   product_(j=0)^(J_delta)|cos(2pi(u_j+w_j))|.
                                                            (2)

The product is strictly positive and at most one: its phases are real algebraic integers, so none can be an odd integer divided by four.
The integer trace identity replaces every negative-index factor by |cos(2pi(u_j+w_j))|.
The enlarged product in (2), not the old J-window product, is the transition cost throughout this note.

Let mu_N be the actual fair-sign law of the stable-plus-central embedding of sum_(j<N) xi_j alpha^j.
Use exactly the noise U_N, its radius a>0, and the smoothed density f_N of [L G0120](Yin_C_G0321_v1.md#finite-window-central-kl-identity).
The mixed trace covector zeta_(theta,0) has coordinate sigma(theta) at a real place and (2 Re sigma(theta),-2 Im sigma(theta)) at a chosen complex place.
If A_sc denotes multiplication by alpha in these real coordinates, put zeta_(theta,t)=(A_sc^T)^(-t)zeta_(theta,0).
Consequently

    |mu_N_hat(zeta_(theta,t))|
       =product_(j=-t)^(N-1-t)|cos(2pi(u_j+w_j))|.       (3)

For j>J_delta, |u_j|<=sH rho^j and |v_(-j)|<=uH rho^j.
The definition of J_delta gives dH rho^(J_delta)<=delta.
Also |w_j|<=q epsilon_N<=1/16.
Thus the negative tail phases have modulus at most delta, and the positive tail phases at most delta+q epsilon_N <=1/8.
When J_delta<=t<=N-1-J_delta, the full product in (3) contains every transition factor in (2).
The sum of squared tail phases is at most

    (u^2+2s^2)H^2 rho^(2J_delta+2)/(1-rho^2)
          +2Nq^2 epsilon_N^2
       <=E_delta:=3delta^2/(1-rho^2)+2q^2 kappa^2.       (4)

Here the factor two on the positive tail is from (u_j+w_j)^2<=2u_j^2+2w_j^2; there are at most N central terms.
On |x|<=1/8 the second derivative of -log cos(2pi x) is at most 8pi^2, so |cos(2pi x)|>=exp(-4pi^2 x^2).
It follows that

    |mu_N_hat(zeta_(theta,t))|
       >=exp(-4pi^2 E_delta) C_delta(theta)              (5)

on that entire interior time interval.

Now impose the explicit finite noise condition

    q kappa/sqrt(N)<=sqrt(2eta)/(4pi a).                 (6)

Define both endpoint guards with the new transition length:

    R_(delta,N)=max{J_delta+1, 0,
       ceil(log(4pi a dH/sqrt(2eta))/(-log rho_s))},
    C_c=sqrt(2q) kappa,
    T_(delta,N)=max{J_delta,
       ceil(log(max(4,C_c)H^(d-1))/(-log rho_s))}.
                                                            (7)

Indeed the exact noise support function is bounded by

    h_(K_N)(zeta_(theta,t))<=dH rho_s^(N-t)+q epsilon_N.

For t<=N-R_(delta,N), its first term is at most sqrt(2eta)/(4pi a), including when the logarithm in (7) is negative.
Equation (6) controls the second term by the same bound.
Therefore 2pi a h_(K_N)(zeta_(theta,t))<=sqrt(2eta), and the exact sufficient noise condition of L G0120 gives U_N_hat(zeta_(theta,t))>=1-eta.
Together with (5), this gives actual smoothed amplitudes at least

    A_delta C_delta(theta),
    A_delta=(1-eta) exp(-4pi^2 E_delta),                 (8)

for T_(delta,N)<=t<=N-R_(delta,N).

For completeness, the frequency count also retains its actual height cost.
Integer norm gives |sigma(theta)|>=H^(-(d-1)) at each embedding.
For t>=0 and ell>=0, the stable covector norm r_t therefore satisfies

    r_t>=rho_s^(-t)H^(-(d-1)),
    r_(t+ell)>=rho_s^(-ell)r_t.

After the L G0120 whitening, the central covector has constant norm in t, bounded by sqrt(2qN) epsilon_N=C_c.
The stable multiplication is normal in these real coordinates.
For t>=T_(delta,N), r_t>=max(4,C_c), so the whitened frequencies nu_t=(zeta_(theta,t)^s,sqrt(N)zeta_(theta,t)^c) obey

    ||nu_t||>=4,
    ||nu_(t+ell_0)||/||nu_t||>=rho_s^(-ell_0)/sqrt(2)>=4.

Select t=T_(delta,N),T_(delta,N)+ell_0,...<=N-R_(delta,N).
If this set is nonempty its exact cardinality is

    k_(delta,N)=floor((N-R_(delta,N)-T_(delta,N))/ell_0)+1;
                                                            (9)

otherwise put k_(delta,N)=0.
Relabeling the selected frequencies from one gives precisely ||nu_l||>=4^l and ||nu_(l+1)||>=4||nu_l||, as required by L G0120.
No asymptotic count replaces (9).

Write H_N for the Shannon entropy of the original algebraic sign sum, and retain the nonnegative constant C_P^KL from L G0120.
Its weighted Fourier test and (8) give

    Nm-H_N>=k_(delta,N)g(A_delta C_delta(theta))-B_N,
    B_N=(q/2)log N+C_P^KL+log 2,
    g(x)=((1+x)log(1+x)+(1-x)log(1-x))/2.               (10)

The original-law k=1 case of [L G0108](Yin_C_G0305_v1.md#quantitative-convolution-entropy-convergence) gives m-h_1<=C_ent(m), where

    C_ent(m)=(5/12)(exp(2m)-1)^2(1-exp(-4m)).

Subadditivity gives H_N>=Nh_1.
Thus every window meeting the stated conditions necessarily satisfies

    k_(delta,N)g(A_delta C_delta(theta))
                 <=N C_ent(m)+B_N.                    (11)

This changes the tail certificate, not the original digit law, smoothing law, Gaussian normalization, or entropy upper comparison.

### Existence of central-small candidates and finite feasibility

The multiplier hypothesis is available without a new arithmetic input.
The finite coefficient-box argument of L G0123 supplies theta in Z[alpha] with strict central bound epsilon_N and full height at most

    A_d=2sqrt(2)d+2,
    Q_N=ceil((2A_d^q epsilon_N^(-q))^(1/h)),
    H=L_P Q_N,
    L_P=sum_(i=0)^(d-1) max(1,max_beta |beta|)^i.        (12)

Every guard above can use this explicit H, whether or not the chosen theta has smaller actual height.
For fixed P,kappa,delta,eta, (12) is a polynomial bound in N; J_delta, R_(delta,N) and T_(delta,N) are therefore O_P(log(N+1)), with all of these parameter dependencies retained.
This eventual statement does not replace the finite checks (6)--(9), assert a degree-independent threshold, or bound the complexity of finding theta.

<a id="salem-linear-transition-target"></a>
### A finite linear-in-m transition target in the Salem scope

Suppose now alpha is a Salem number and

    0<m=log(alpha)<=1/32.

This is a conditional input domain, not an assertion that such a Salem number exists.
It has one stable conjugate alpha^(-1), one expanding conjugate alpha, and q=d-2 central conjugates.
In particular rho=rho_s=exp(-m).
Choose

    eta=1/4,
    kappa=sqrt(m)/(16q),
    delta=sqrt(m(1-exp(-2m)))/16.                      (13)

These satisfy (1), and they give exactly

    E_delta=5m/256,
    A_delta=(3/4)exp(-5pi^2 m/64)>1/sqrt(2).           (14)

For the strict bound, pi^2<10 and m<=1/32 imply 5pi^2 m/64<1/32.
The inequality exp(-x)>=1-x then gives A_delta>(3/4)(31/32)=93/128>1/sqrt(2), the last comparison following from 93^2>128^2/2.
Also log 2<3/4, since the first three terms of exp(3/4) already exceed two.
Hence, with L=log(4sqrt(2)),

    ell_0=ceil(L/m)<=L/m+1
          <(15/8+m)/m<=61/(32m)<2/m.                 (15)

The entropy comparison has the exact elementary identity

    C_ent(m)=(20/3)sinh(m)^3 cosh(m)
          <=(20/3)m^3 exp(4m)
          <=(160/21)m^3<8m^3.                        (16)

Here sinh(m)<=m cosh(m)<=m exp(m), cosh(m)<=exp(m), and exp(4m)<=exp(1/8)<=8/7; the last upper bound follows from exp(x)<=1/(1-x) for 0<=x<1.

Consider an integer N and a central-small multiplier satisfying (12).
Recompute J_delta,R_(delta,N),T_(delta,N) from (2),(7) and (13).
Impose all three finite checks

    N>=pi^2 a^2 m/8,
    N>=2(R_(delta,N)+T_(delta,N)),
    B_N<8Nm^3.                                      (17)

The first is exactly (6) specialized to (13); N>=1 remains in force.
The second makes the frequency set nonempty and, by the actual floor formula (9), yields

    k_(delta,N)>Nm/4.                                (18)

Indeed k_(delta,N)>=(N-R_(delta,N)-T_(delta,N))/ell_0 >=N/(2ell_0)>Nm/4.
No ceiling cost is discarded.

If at this same window one could certify

    C_delta(theta)>=16m,                             (19)

then the positive series for g gives g(x)>=x^2/2 on [0,1], and (14) would imply g(A_delta C_delta)>C_delta^2/4.
Consequently

    k_(delta,N)g(A_delta C_delta)
          >Nm C_delta^2/16>=16Nm^3.

But (16)--(17) make the right side of (11) strictly less than 16Nm^3, a contradiction.
Thus every actual multiplier/window satisfying (13),(17) in this conditional Salem domain must have

    C_delta(theta)<16m.                              (20)

Equation (19) is the explicit sufficient target for excluding such an input, not a lower bound supplied by the construction.

This modified certificate passes its optimistic-ceiling test.
For any fixed hypothetical input in this domain, the polynomial height (12) makes the second condition of (17) eventually true.
The first is a fixed threshold, and B_N/N tends to zero, so the third also eventually holds.
The artificial value C_delta=1 meets (19), since 16m<=1/2.
Hence, with every finite cost retained, that artificial left side does exceed the right side at all sufficiently large admissible windows.
This statement concerns only a ceiling; no actual multiplier is asserted to attain it.

### Remaining arithmetic obligation and compatibility

Reducing delta lengthens the transition product and removes usable endpoint times.
Equations (2),(7),(9),(17) charge those costs exactly.
An estimate for the old shorter product cannot be substituted in (19).
The still-missing statement would have to supply an actual certified window and its new product lower bound under the hypothetical small-m assumption, with all of (17).
No such arithmetic statement is proved here.

This does not contradict [L G0125](Yin_C_G0330_v1.md#subexponential-height-mixed-budget-collapse).
For fixed P, the family (12) has central conjugates tending to zero and log H_N=o(N).
Its actual full nonnegative-time budget remains o(N).
Moreover J_delta is admissible for the height-free transition-collapse statement because delta<=1/16.
That theorem therefore still forces the actual C_delta to tend to zero; this note supplies no positive limiting amplitude and does not require (19) at infinitely many windows of a fixed input.
The artificial ceiling is not an actual-amplitude claim.

The original L G0127 obstruction remains valid for its unchanged constants.
The present argument changes exactly its fixed tail loss while retaining the additional transition and guard costs.
The general unit statement is (11).
The special rho_s=exp(-m) and (15) are Salem properties and are not available on an arbitrary multiple-expanding unit.
No extension to the full sufficiently near-one reciprocal core, uniform Mahler gap, Salem entropy equality or strict entropy inequality is asserted.
