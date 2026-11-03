---
author: Yin
---

# Complete central scattering, optimized mean energy and finite-window cube bounds

This retains the complete original 2026-10-07 [L116 argument](../ledger/Yin_L_G0116_v1.md).
The original assess_shortness_route agent proved the bounded-solution, finite-window and cube boundaries for Yin; the coordinator co-derived the kernel and scattering normalization.
Original proof attribution and every actual old review retain their exact input/date scopes.
No current Task/E execution, source acquisition or mathematical program run is selected by this maintenance.

## Statement

Fix a monic irreducible P in Z[t] with at least one unit-circle root, and a nonzero finite integer forcing z.
All roots are simple and nonzero, including every member of each complex conjugate pair.
The causal-center Green kernel and Laurent convention in (1)--(3) give every bounded real solution e=e0+sum_C c_beta beta^j, uniquely, with center jump a_beta=Z(beta)/P'(beta).
For every such solution the symmetric mean energy is exactly

    C(c)=sum_C abs(c_beta+a_beta/2)^2+A(P,z)/4,
    A(P,z)=sum_C abs(Z(beta)/P'(beta))^2.

Its least value over all bounded real solutions is A(P,z)/4, attained uniquely at c=-a/2; no cube feasibility is implied.
The complete constants R,rho,D,T,K(c),K* and V_C in (5)--(7) give for every N>=R a full-window energy lower bound and cosine-product decay, with K* uniform over every actual closed-cube solution at this fixed P,z.
Cube feasibility requires A<=1, and a strict uniform norm s<1/2 requires A<=4s^2<1.
If P divides Z, every closed-cube solution has a finite exact zero factor and no solution is coordinatewise in the strict cube.
For nonzero residue, A>0 and the fixed-input exponential bound applies.
Cyclotomic inputs and empty noncentral root sets are included.
No polynomial/forcing-uniform positive rate, cube existence, admissible optimized construction or uniform Mahler gap is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:02 |
| status | open |
| reason | Retain the complete exact original theorem and argument; current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Full original (1)--(8): Green seam and convolution index, complete bounded classification, both exact scattering tails, conjugate-counted Cesaro minimum, every finite middle/off-diagonal/geometric remainder and uniform cube constant, necessary cube factors, and divisible-forcing almost-periodic returns with an actual zero factor. |
| argument | [Complete argument](#argument) | Full original (1)--(8): Green seam and convolution index, complete bounded classification, both exact scattering tails, conjugate-counted Cesaro minimum, every finite middle/off-diagonal/geometric remainder and uniform cube constant, necessary cube factors, and divisible-forcing almost-periodic returns with an actual zero factor. |
| dependency | [Exact retained input](Yin_C_G0304_v1.md#canonical-trace-defect) | Direct Green seam/Lagrange orientation as a consistency interface; the center kernel and all finite constants are derived here. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:04 |
| status | proved |
| reason | Adopt the exact complete original theorem and retained argument after actual whole self-review with resolved used inputs, preserving all fixed-input, hypothesis and uniformity boundaries. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Full original (1)--(8): Green seam and convolution index, complete bounded classification, both exact scattering tails, conjugate-counted Cesaro minimum, every finite middle/off-diagonal/geometric remainder and uniform cube constant, necessary cube factors, and divisible-forcing almost-periodic returns with an actual zero factor. |
| argument | [Complete argument](#argument) | Full original (1)--(8): Green seam and convolution index, complete bounded classification, both exact scattering tails, conjugate-counted Cesaro minimum, every finite middle/off-diagonal/geometric remainder and uniform cube constant, necessary cube factors, and divisible-forcing almost-periodic returns with an actual zero factor. |
| dependency | [Exact retained input](Yin_C_G0304_v1.md#canonical-trace-defect) | Direct Green seam/Lagrange orientation as a consistency interface; the center kernel and all finite constants are derived here. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0549_v1.md#current-scattering-finding) | Exact current statement, complete original proof and directly used interfaces; self-reviewed, with every old checking relationship and exact original input retained separately. |

## Complete retained argument

<a id="argument"></a>
Let P(t)=sum_(i=0)^d p_i t^i be monic irreducible over Z, with at least one unit-circle root.
Its roots are distinct and nonzero.
Let C, S and U be its sets of unit-circle, stable and expanding roots, respectively.
Every complex root is counted, so conjugate pairs contribute twice.
The argument allows the cyclotomic case; its intended application is the positive-Mahler-measure algebraic-unit branch.

Let z be a nonzero finite integer sequence, put

    (Se)_j=e_(j+1),    Z(t)=sum_k z_k t^(-k-1),
    a_beta=Z(beta)/P'(beta)  for every root beta of P.

All statements below keep P and z fixed unless explicitly stated otherwise.
A bounded real solution need not tend to zero.

<a id="unit-circle-scattering-coefficients"></a>
### All bounded solutions and the exact jump

Define the bounded causal-center Green kernel by

    w_j=sum_(beta in S union C) beta^j/P'(beta), j>=0,
    w_j=-sum_(beta in U) beta^j/P'(beta),        j<0.

Then P(S)w=delta_(-1).
To check the seam, at j=-r, 1<=r<=d, the recurrence on each root turns the defect into sum_beta b_r(beta)/P'(beta), where b_r(t)=sum_(i=r)^d p_i t^(i-r).
Lagrange interpolation says this is the coefficient of t^(d-1) in b_r: one if r=1, zero otherwise.
Away from the seam every mode satisfies the homogeneous recurrence.
This also verifies the shift convention directly, consistently with [L G0107](Yin_C_G0304_v1.md#canonical-trace-defect).

Consequently a particular bounded real solution is

    e^0_j=sum_k z_k w_(j-k-1).                         (1)

Every bounded real solution is uniquely of the form

    e_j=e^0_j+sum_(beta in C) c_beta beta^j,
    c_(conjugate beta)=conjugate(c_beta).              (2)

Indeed the difference of two solutions is homogeneous.
Matching d consecutive values with a Vandermonde matrix gives a sum of all root modes.
Boundedness at both ends excludes every stable and expanding mode.
Conversely all the center modes in (2) are bounded.
Thus existence of a bounded solution is automatic; cube membership is not.

Choose

    R=1+max_(z_k!=0)|k+1|,
    c^-_beta=c_beta,    c^+_beta=c_beta+a_beta.

The two tails are exactly

    e_j=sum_C c^+_beta beta^j+sum_S a_beta beta^j,
                                             j>=R,
    e_j=sum_C c^-_beta beta^j-sum_U a_beta beta^j,
                                             j<=-R.  (3)

In particular the right-minus-left center coefficient is a_beta=Z(beta)/P'(beta), with no factor two or additional root power.
Adding a center homogeneous solution changes both sides by the same c_beta and cannot change the jump.

<a id="minimal-central-cesaro-energy"></a>
### Exact mean energy and its optimization

For a finite sum of distinct unit-circle modes, Cesaro averaging eliminates the off-diagonal terms: the sum of (beta conjugate(gamma))^j over any consecutive interval has absolute value at most 2/|1-beta conjugate(gamma)| when beta!=gamma.
The noncentral tails in (3) decay exponentially and make only a bounded contribution to the energy comparison.
It follows that

    lim_(N->infinity) [sum_(j=-N)^N e_j^2]/(2N+1)
       =C(c):=(1/2)sum_C (|c_beta|^2+|c_beta+a_beta|^2)
       =sum_C |c_beta+a_beta/2|^2+A(P,z)/4,
    A(P,z):=sum_C |Z(beta)/P'(beta)|^2.                 (4)

The least symmetric mean-square energy among all bounded real solutions is therefore exactly A(P,z)/4.
It is attained uniquely by c_beta=-a_beta/2.
Conjugation symmetry makes this an allowed real solution.
No claim places that minimizer in the rounding cube.

Because P is irreducible, either P divides Z in the integer Laurent ring, or Z(beta)!=0 at every root of P.
Thus A(P,z)=0 precisely when P divides Z.
In the nonzero-residue case A(P,z)>0, even after optimization over every bounded center homogeneous correction.

<a id="finite-window-central-product-bound"></a>
### A completely specified finite-window estimate

Here are constants for the bounded remainder in (4).
Set

    rho=max({1/2} union {|beta|: beta in S}
                       union {|beta|^(-1): beta in U})<1,
    U_+=sum_S |a_beta|,    U_-=sum_U |a_beta|,
    H_+=sum_C |c^+_beta|, H_-=sum_C |c^-_beta|,
    D(v)=sum_(beta,gamma in C, beta!=gamma)
                 2|v_beta||v_gamma|/|1-beta conjugate(gamma)|,
    T=2(H_+U_++H_-U_-)rho^R/(1-rho)
                         +(U_+^2+U_-^2)rho^(2R)/(1-rho^2),
    K(c)=(2R-1)C(c)+D(c^+)+D(c^-)+T.

Empty sums are zero.
In particular these definitions also apply when every root is central.
For N>=R,

    sum_(j=-N)^N e_j^2 >= (2N+1)C(c)-K(c).             (5)

To verify (5), sum the two tails R<=|j|<=N.
Their diagonal center contribution is 2(N-R+1)C(c), and their off-diagonal losses are at most D(c^+)+D(c^-).
Writing each tail as h_j+r_j gives |e_j^2-h_j^2|<=2|h_j||r_j|+|r_j|^2; its sum is at most T by (3) and geometric series.
The omitted middle energy is nonnegative.
This proves the lower bound.
An upper bound with an additional finite middle energy also proves the limit in (4) directly.

Suppose now this particular solution has |e_j|<=1/2 at every j.
Since cos(pi x)<=exp(-pi^2 x^2/2) on that interval, including its zero endpoints, (5) gives

    product_(j=-N)^N cos(pi e_j)
       <=exp(pi^2 K(c)/2)
                  exp[-(pi^2/2)C(c)(2N+1)]
       <=exp(pi^2 K(c)/2)
                  exp[-pi^2 A(P,z)(2N+1)/8], N>=R.    (6)

This is a fixed-input finite-window estimate; small central-root separations and slow noncentral tails remain in the displayed constants.

There is also a prefactor uniform over all cube solutions for this fixed P and z.
Put q=|C| and, if q>=2, delta=min_(beta!=gamma in C)|1-beta conjugate(gamma)|.
Each half-tail of a cube solution has center mean square at most 1/4.
Hence sum_C |c^+_beta|^2 and sum_C |c^-_beta|^2 are at most 1/4, C(c)<=1/4, and H_+,H_-<=sqrt(q)/2.
In particular K(c)<=K_* where

    K_*=(2R-1)/4+V_C
          +sqrt(q)(U_++U_-)rho^R/(1-rho)
          +(U_+^2+U_-^2)rho^(2R)/(1-rho^2),
    V_C=q/delta if q>=2, and V_C=0 if q=1.             (7)

For the off-diagonal bound use D(v)<=2(sum|v|)^2/delta on each half.
Thus K_* can replace K(c) in the last line of (6), simultaneously for every closed-cube solution.
Cube feasibility also requires A(P,z)<=1; if ||e||_infinity=s<1/2 it requires A(P,z)<=4s^2<1.
These are necessary conditions, not a characterization or proof of feasibility.

<a id="zero-residue-central-cube-boundary"></a>
### The divisible forcing and the cube boundary

Suppose P divides Z and z is nonzero.
Monic Laurent division gives a nonzero finite integer sequence q_0 with z=P(S)q_0.
Every bounded real solution is then

    e=q_0+h,   h_j=sum_C c_beta beta^j.                (8)

The least mean energy is zero, attained by e=q_0; this integer solution does not belong to the strict rounding cube.
In fact no solution of (8) belongs to that cube, even if strictness is only coordinatewise.

To prove it, first suppose |e_j|<=1/2 everywhere.
There are positive integers n_l tending to infinity with beta^(n_l)->1 simultaneously for all beta in C.
This follows by pigeonholing the powers in successively finer finite partitions of the compact torus; if the resulting return indices stay bounded, one is an exact common period and its multiples give the required unbounded returns.
For any fixed j, eventually (q_0)_(j+n_l)=0 and h_(j+n_l)->h_j.
Thus |h_j|<=1/2 at every j.
At an index where the integer (q_0)_j is nonzero, |e_j|>=1/2.
A closed-cube solution must therefore have |e_j|=1/2 at such an index, and its cosine product has an exact zero factor.
A strict-cube solution is impossible.

This treats the A(P,z)=0 degeneracy separately; it does not extract a positive decay rate from zero mean energy.
Together with (6), it says that for every nonzero finite integer forcing, any bounded closed-cube solution either has the positive fixed-input rate in (6), or has a finite zero factor.
For P not dividing Z, cube existence and the actual minimum energy within that constrained class remain separate questions.

### Scope and limits

The conclusion quantifies the nondecaying central tails left outside [L G0115](Yin_C_G0316_v1.md#unit-circle-c0-integer-forcing).
It neither supplies nor assumes a lower bound for A(P,z) uniformly over different forcings, their spans, or different polynomials.
The root separation, forcing evaluations and noncentral decay costs in (5)--(7) are not suppressed.
In particular this is not a uniform Mahler gap, and optimizing the center modes without verifying cube membership does not create an admissible trace construction.
