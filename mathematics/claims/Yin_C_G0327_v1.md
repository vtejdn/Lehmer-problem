---
author: Yin
---

# Exact mixed-trace smoothing budgets with bounded central corrections and repeated times

This retains the complete original 2026-10-07 [L122 mathematical argument](../ledger/Yin_L_G0122_v1.md).
The original assess_shortness_route agent derived the mixed orbit/noise estimates and repeated-time split for Yin; the coordinator supplied the bounded-center annulus mechanism.
No current Task/E execution, source acquisition or mathematical program run is selected by this maintenance.

## Statement

Fix a positive-Mahler irreducible algebraic unit P with a unit-circle conjugate and a nonzero integral multiplier theta.
Use exactly the stable-central sign law, product uniform interval/disc noise and Fourier normalization of the complete finite-window Gaussian construction.
For the mixed trace covectors at all integer t>=0, the actual smoothed spectral sum sum_t g(abs(fhat_N(zeta_(theta,t)))) is at most the explicit B_theta in (4), uniformly over every N>=1.
The unsmoothed exterior amplitudes instead tend to one.
For every fixed central covector bound R_c and choices y_t with norm<=R_c, at most one at each integer time, the actual sum is at most the explicit B_corr in (7), uniformly in N.
For every finite ratio-four whitened family, now allowing repeated times and independently chosen bounded center covectors, the complete actual sum is at most

    B_corr+(log2/log4)log_+(sqrt(2)max(1,R_c)sqrt(N)).

The exact real/disc Fourier constants, both time ends, compact coefficient annulus with possibly zero coordinates and low/high norm multiplicity split are part of the theorem.
Fixed finite multiplier families, including each fixed conjugate-height cap, retain these bounds.
They control this family of lower certificates, without bounding the full relative entropy or proving the actual deficit zero.
Negative times, growing center/multiplier families, other stable directions, noises or tests and polynomial-uniform rates remain outside the statement.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:16 |
| status | open |
| reason | Retain the complete exact original theorem and argument; actual current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(9): exact mixed trace orientations and compact recurrence, actual real/disc noise transform, complete nonnegative-time sums, bounded-center annulus and two-sided count, every repeated-time low/high whitened class and all actual-deficit/family/uniformity limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(9): exact mixed trace orientations and compact recurrence, actual real/disc noise transform, complete nonnegative-time sums, bounded-center annulus and two-sided count, every repeated-time low/high whitened class and all actual-deficit/family/uniformity limits. |
| dependency | [Exact retained input](Yin_C_G0321_v1.md#finite-window-stable-central-smoothing) | Exact original stable-central law/noise, whitening, weighted actual-amplitude budget and ratio-four test conditions. |
| dependency | [Exact retained input](Yin_C_G0302_v1.md#weighted-central-trace-prefix-decay) | Complete elementary non-root-of-unity finite-alphabet/Vandermonde and compact-group bounded-gap method, and fixed-height family finiteness. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:20 |
| status | proved |
| reason | Adopt the exact complete original theorem and retained argument after actual whole self-review with resolved used inputs, preserving every nonlinear, boundary, moment, actual-noise, finite-window and input-dependent limitation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(9): exact mixed trace orientations and compact recurrence, actual real/disc noise transform, complete nonnegative-time sums, bounded-center annulus and two-sided count, every repeated-time low/high whitened class and all actual-deficit/family/uniformity limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(9): exact mixed trace orientations and compact recurrence, actual real/disc noise transform, complete nonnegative-time sums, bounded-center annulus and two-sided count, every repeated-time low/high whitened class and all actual-deficit/family/uniformity limits. |
| dependency | [Exact retained input](Yin_C_G0321_v1.md#finite-window-stable-central-smoothing) | Exact original stable-central law/noise, whitening, weighted actual-amplitude budget and ratio-four test conditions. |
| dependency | [Exact retained input](Yin_C_G0302_v1.md#weighted-central-trace-prefix-decay) | Complete elementary non-root-of-unity finite-alphabet/Vandermonde and compact-group bounded-gap method, and fixed-height family finiteness. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0552_v1.md#current-mixed-budget-finding) | Exact current statement, complete original proof and directly used interfaces; self-reviewed, with exact original findings and actual relationships retained separately. |

## Complete retained argument

<a id="argument"></a>
Fix an algebraic unit alpha with monic irreducible P, m=log M(P)>0, and at least one unit-circle conjugate.
Fix theta in O_K minus {0}.
Stable and expanding places both exist.
No conjugate is a root of unity, since that would make P cyclotomic.
In particular central places are nonreal conjugate pairs.
Use the real/complex coordinate convention, actual stable-central sign law mu_N, and product uniform noise U_N on a K_N of [L G0120](Yin_C_G0321_v1.md#finite-window-stable-central-smoothing).
Write f_N=mu_N*U_N.
The radius a>0 is that fixed input's L G0120 radius, with stable noise radii a|beta|^N and central radii a.
All trace sums below count both members of a complex pair, whereas a complex coordinate occupies its ordinary Euclidean plane.

<a id="mixed-trace-positive-block-decay"></a>
### The actual mixed trace orbit and its two sides

Let u_j, w_j and v_j be the stable, central and expanding weighted traces of theta alpha^j.
They are real, and

    u_j+w_j+v_j=Tr(theta alpha^j) in Z, j in Z.

At a real stable place define the covector component sigma(theta) beta^(-t).
At each chosen complex stable or central representative define the two components (2Re(sigma(theta)beta^(-t)), -2Im(sigma(theta)beta^(-t))).
Denote the resulting covector by zeta_(theta,t)^(sc).
For integer t>=0 its pairing with iota_sc(alpha^j) is u_(j-t)+w_(j-t).
Consequently

    |hat mu_N(zeta_(theta,t)^(sc))|
       =product_(j=0)^(N-1)
                 |cos(2pi[u_(j-t)+w_(j-t)])|.          (1)

There are C_theta>=1 and eta_theta>0, independent of N>=1 and t>=0, such that

    |hat mu_N(zeta_(theta,t)^(sc))|
       <=C_theta exp[-eta_theta (N-t)_+].              (2)

Here the decaying block is on the opposite side from the stable-only frequency bound in [L G0105](Yin_C_G0302_v1.md#weighted-central-trace-prefix-decay).
For completeness, the same elementary proof can be applied to the forward central sequence w_k=sum_C sigma_beta(theta) beta^k.
It cannot be half-integral at every k>=0: that would be a bounded finite-alphabet recurrence sequence, hence eventually periodic by repetition of a block of length |C|.
Subtracting a period and using a Vandermonde matrix would force every coefficient to vanish, since no beta is a root of unity.
Each coefficient is nonzero.

A compactness argument on the closure of the powers of the central root tuple now gives integers B,K>=0 and epsilon in (0,1/2) such that every block of B+1 nonnegative indices contains a central factor of absolute value at most 1-2epsilon, and |u_k|<=epsilon/(2pi) for k>=K.
The compact closure is a group, and rotation by the tuple has dense forward orbit from every point; a finite cover of translates of the bad-factor open set proves the bounded-gap assertion.
This is the same compact-group argument retained in L G0105, with positive powers and a stable remainder.
Cosine is 2pi-Lipschitz in its trace argument, so at those visits past K the perturbed factor is at most 1-epsilon.
The positive block in (1) has length (N-t)_+, giving (2), for example with eta_theta=-log(1-epsilon)/(B+1) and C_theta=exp(eta_theta K)/(1-epsilon).

For j-t<0 the integer trace instead gives |cos(2pi[u_(j-t)+w_(j-t)])|=|cos(2pi v_(j-t))|.
Since v_k tends to zero as k tends to negative infinity, for each fixed N the unsmoothed coefficient in (1) tends to one as t tends to infinity.
Thus its spectral budget over all exterior times is not summable.
The actual smoothing must be retained in the next step.

<a id="exact-noise-exterior-trace-decay"></a>
### The exact noise suppresses every exterior time

Choose any stable place beta_* and put rho=|beta_*|<1.
Its embedding theta_*=sigma_*(theta) is nonzero.
The product uniform noise has independent coordinate factors, all Fourier factors of absolute value at most one.

At a real place the interval Fourier factor is sin(2pi R xi)/(2pi R xi), with R=a rho^N and |xi|=|theta_*|rho^(-t).
At a complex place, rotating the frequency reduces the disc factor to the Fourier transform of its one-coordinate marginal

    p_R(x)=2sqrt(R^2-x^2)/(pi R^2), |x|<=R.

This density vanishes at both endpoints and has integrable derivative with integral |p'_R|=4/(pi R).
Integration by parts therefore gives |hat p_R(xi)|<=2/(pi^2 R|xi|), without using a Bessel estimate.
Here the real two-dimensional frequency has norm 2|theta_*|rho^(-t).
In both cases,

    |hat f_N(zeta_(theta,t)^(sc))|
       <=min(1,D_theta rho^(t-N)), t>N,
    D_theta=1/(2pi a|theta_*|) at a real place,
    D_theta=1/(pi^2 a|theta_*|) at a complex place.      (3)

The same bound holds if the central covector is changed arbitrarily while the stable covector is kept fixed.
It is a bound for the actual L G0120 noise, not its sufficient small-phase approximation.

Define g(b)=[(1+b)log(1+b)+(1-b)log(1-b)]/2 for 0<=b<=1.
Its nonnegative series g(b)=sum_(r>=1)b^(2r)/[2r(2r-1)] gives

    g(b)<=(log2)b^2.

Using |hat U_N|<=1 inside the window, (2)--(3) prove

    sum_(t>=0) g(|hat f_N(zeta_(theta,t)^(sc))|)
       <=B_theta,
    B_theta=(log2)[C_theta^2/(1-exp(-2eta_theta))
                   +D_theta^2 rho^2/(1-rho^2)].        (4)

This bound is uniform in N.
It controls every subset of the nonnegative time orbit, even before imposing the lacunarity required by L G0120.
The unsmoothed exterior sum, by contrast, diverges because its terms tend to g(1)=log2.
A fixed finite set of multipliers is covered by summing its individual constants.

<a id="bounded-central-correction-decay"></a>
### Optimizing a bounded central correction

The coordinator contributed the following extension.
Keep the same stable covector zeta_(theta,t)^s but replace the central part by any y of Euclidean norm at most R_c, independently for every test.
Set D=max(1,R_c).
A complex central covector (y_1,y_2) corresponds to coefficients d_beta=(y_1-i y_2)/2 and d_(conjugate beta)=conjugate(d_beta).
Thus

    <y,iota_c(alpha^j)>=sum_C d_beta beta^j,
    ||d||_2^2=||y||^2/2.

Let c_beta=sigma_beta(theta), c_0=||c||_2>0, and d'_beta=d_beta beta^t.
At k=j-t the central coefficient on the positive side is d'; on the negative side, after subtracting the integer full trace, it is d'-c.
At least one of their norms is at least c_0/2, and both are at most D+c_0.
Therefore one side belongs to the fixed compact coefficient annulus

    c_0/2<=||a||_2<=D+c_0,
    a_(conjugate beta)=conjugate(a_beta).              (5)

For every nonzero coefficient vector a, some k>=0 has |cos(2pi sum_C a_beta beta^k)|<1.
The same finite-alphabet recurrence and Vandermonde proof used above applies even when some coordinates of a vanish.
Continuity and a finite cover of the compact annulus give a uniform B and epsilon in (0,1/2): every a has such a factor at some k in 0,...,B with value at most 1-2epsilon.
Rotating the coefficients by beta^j preserves the annulus, so this is a uniform bound in every block.
The negative orientation obeys the same assertion, by conjugating/relabeling the coefficient vector; alternatively take the larger of the two finite block lengths.

Stable positive tails u_k and expanding negative tails v_(-k) are both at most epsilon/(2pi) beyond one fixed K.
These tails depend on theta, not on y or t.
Applying the bad-factor count to whichever side has the large coefficient gives constants C>=1, eta>0 depending only on P,theta,R_c with

    |hat mu_N(zeta_(theta,t)^s,y)|
       <=C exp[-eta min(t,N-t)], 0<=t<=N.             (6)

The large side may be the shorter side, which is why min(t,N-t), rather than N-t, occurs here.
For t>N the exact-noise bound (3) is still valid independently of y.
Consequently, if at most one y_t is chosen at each integer time, then

    sum_(t>=0) g(|hat f_N(zeta_(theta,t)^s,y_t)|)
       <=B_corr,
    B_corr=(log2)[2C^2/(1-exp(-2eta))
                        +D_theta^2 rho^2/(1-rho^2)].   (7)

This is again independent of N.
The factor two counts the two ends of the interior window.
It does not silently permit arbitrary multiplicity at a fixed t.

<a id="bounded-center-lacunary-budget"></a>
### All bounded-center lacunary selections, including repeated times

Consider any finite L G0120 test family (zeta_(theta,t_l)^s,y_l), with integer t_l>=0, ||y_l||<=R_c, and whitened frequencies

    nu_l=(zeta_(theta,t_l)^s,sqrt(N)y_l),
    ||nu_l||>=4^l,  ||nu_(l+1)||>=4||nu_l||.           (8)

Repeated times t_l are allowed.
Let v_t be the norm of the stable covector.
If v_t<D sqrt(N), then ||nu_l||<sqrt(2)D sqrt(N).
All tests in this low-norm class together number at most

    log_+(sqrt(2)D sqrt(N))/log4.

For the remaining class v_t>=D sqrt(N), each fixed time has all its possible whitened norms in [v_t,sqrt(2)v_t].
The ratio-four condition permits at most one test at that time.
Its budget is bounded by (7).
Since g<=log2, the whole family therefore obeys

    sum_l g(|hat f_N(zeta_(theta,t_l)^s,y_l)|)
       <=B_corr+(log2/log4)
                           log_+(sqrt(2)D sqrt(N)).    (9)

Here log_+(x)=max(0,log x).
In this formula its argument is at least sqrt(2), since D,N>=1.
The subsequence count is valid even if its members are interspersed with other tests: their inherited indices and lacunarity only strengthen the bound.

Thus the complete fixed mixed trace orbit has O(1) actual budget, while arbitrary bounded-center corrections, allowing repeated times and optimizing every L G0120 test coefficient, have O(log N) budget.
The second conclusion does not incorrectly treat different central covectors at the same time as a single test.
A fixed finite collection of stable trace multipliers is covered by summing these bounds.

### Consequence and actual review scope

The weighted L G0120 lower certificate for Nm-H_N uses precisely the sum in (9), followed by subtraction of a logarithmic central cost and fixed constants.
The families proved here therefore cannot make that certificate linear and positive in N for this fixed input.
This does not assert that the actual entropy deficit is zero, or give an upper bound on the full relative entropy.
It bounds only the stated family of spectral lower certificates.

Fixed finite multiplier families remain covered.
The bounded-conjugate-size finiteness proved in L G0105 also makes each fixed height cap a finite family.
Multiplier sets or center bounds growing with N, unboundedly changing arithmetic directions, non-trace stable covectors, other noise/reference choices, and tests outside this lacunary mechanism are not resolved.
Negative time indices are not part of the family quantified in (4), (7), or (9).
No uniformity in P or a Lehmer gap is claimed.
