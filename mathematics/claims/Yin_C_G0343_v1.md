---
author: Yin
---

# Closed-cube bounded-energy windows on actual Salem inputs and free-length certificate overlap

This retains the complete original 2026-10-08 [L137 mathematical argument](../ledger/Yin_L_G0137_v1.md).
The execution_and_deliverables agent derived and checked the complete witness and free-length consequence for Yin; the coordinator contributed no witness or derivation and its original shared-progress whole check is retained.
No current Task/E execution, source acquisition, mathematical program run or algorithm implementation is selected by this maintenance.

## Statement

For every monic integer seed f of degree r>=0 with constant coefficient in {1,-1} and coefficients in {0,1,-1}, every N>r and both signs sigma, the exact two-block vector (3) gives E_R(t^N f+sigma f*)<=H_f/2 for every 0<=R<=N-r-1.
The full shift identities retain both exterior half-integral defect blocks, the nonzero origin sigma H_f and every finite restriction endpoint.
On the retained actual irreducible no-padding Salem progression N=9 modulo120, N>=9, this gives E_R(P_N)<=3/2 for every 0<=R<=d_N-7, with the six exact half-cube coordinates and origin defect three.
The additional N>=16 compact-measure and length-six controls yield the exact input-uniform logarithmic/radius/dual obstructions in Section3, without approaching measure one or excluding fixed-P lower bounds.
Separately, for each hypothetical Salem input 0<m<=1/32, rational 8m<c<16m, mu=1/32 and the full B_bar, the coefficient-only radius at threshold 4B_bar gives the finite n_* in (13).
Every n>=n_* forces the actual enlarged product C_delta<16m for every multiplier satisfying its exact central bound, and places that energy window strictly below every valid same-input cutoff.
The witness uses the closed cube and does not supply a positive amplitude or a trace-rounding multiplier; no practical or varying-input uniform overlap, product lower bound, experiment or Mahler gap is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T10:23 |
| status | open |
| reason | Retain the complete exact original theorem and argument; actual current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(15) and Sections1--4, exact finite domain/closed cube, r0/two-sign/shift/support endpoints, true irreducible progression and N16 geometry, all varying-input log/radius/dual obstructions, distinct free orbit length, rational n_* and strict cutoff overlap, all amplitude/uniformity limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(15) and Sections1--4, exact finite domain/closed cube, r0/two-sign/shift/support endpoints, true irreducible progression and N16 geometry, all varying-input log/radius/dual obstructions, distinct free orbit length, rational n_* and strict cutoff overlap, all amplitude/uniformity limits. |
| dependency | [Exact retained input](Yin_C_G0335_v1.md#finite-rational-energy-coercivity) | Exactly the original closed-cube finite energy and its fixed-input qualitative divergence. |
| dependency | [Exact retained input](Yin_C_G0248_v1.md#family-cyclotomic-factors) | Complete direct all-N Salem factorization and exact cyclotomic table, without an external threshold. |
| dependency | [Exact retained input](Yin_C_G0336_v1.md#linear-exponent-cyclic-coverage) | Exact no-padding N=9mod120 progression and actual degree N+3. |
| dependency | [Exact retained input](Yin_C_G0337_v1.md#tunable-salem-finite-energy-envelope) | Complete actual enlarged-product rational threshold and candidate cutoff, preserving all parameter guards. |
| dependency | [Exact retained input](Yin_C_G0341_v1.md#coefficient-only-coercivity-radius) | Full coefficient-only sufficient energy radius at the rational threshold 4B_bar. |
| dependency | [Exact retained input](Yin_C_G0342_v1.md#rational-energy-dual-certificates) | Exact weak-dual interface on the same feasible box vector. |
| dependency | [Exact retained input](Yin_C_G0334_v1.md#salem-linear-transition-target) | Only the original fixed-input eventual polynomial-height guards and actual enlarged product for the final compatibility statement. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T10:29 |
| status | proved |
| reason | Adopt the complete exact original theorem and retained argument after actual current whole self-review, preserving every finite quantifier, source/native limit, exact cost, original input and sufficient-versus-actual boundary. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(15) and Sections1--4, exact finite domain/closed cube, r0/two-sign/shift/support endpoints, true irreducible progression and N16 geometry, all varying-input log/radius/dual obstructions, distinct free orbit length, rational n_* and strict cutoff overlap, all amplitude/uniformity limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(15) and Sections1--4, exact finite domain/closed cube, r0/two-sign/shift/support endpoints, true irreducible progression and N16 geometry, all varying-input log/radius/dual obstructions, distinct free orbit length, rational n_* and strict cutoff overlap, all amplitude/uniformity limits. |
| dependency | [Exact retained input](Yin_C_G0335_v1.md#finite-rational-energy-coercivity) | Exactly the original closed-cube finite energy and its fixed-input qualitative divergence. |
| dependency | [Exact retained input](Yin_C_G0248_v1.md#family-cyclotomic-factors) | Complete direct all-N Salem factorization and exact cyclotomic table, without an external threshold. |
| dependency | [Exact retained input](Yin_C_G0336_v1.md#linear-exponent-cyclic-coverage) | Exact no-padding N=9mod120 progression and actual degree N+3. |
| dependency | [Exact retained input](Yin_C_G0337_v1.md#tunable-salem-finite-energy-envelope) | Complete actual enlarged-product rational threshold and candidate cutoff, preserving all parameter guards. |
| dependency | [Exact retained input](Yin_C_G0341_v1.md#coefficient-only-coercivity-radius) | Full coefficient-only sufficient energy radius at the rational threshold 4B_bar. |
| dependency | [Exact retained input](Yin_C_G0342_v1.md#rational-energy-dual-certificates) | Exact weak-dual interface on the same feasible box vector. |
| dependency | [Exact retained input](Yin_C_G0334_v1.md#salem-linear-transition-target) | Only the original fixed-input eventual polynomial-height guards and actual enlarged product for the final compatibility statement. |
| review | [Actual current whole self-check](../audits/reviews/Yin_R_G0562_v1.md#current-bounded-energy-window-finding) | Complete current statement, retained proof and every directly used interface; self-reviewed. All old findings retain their actual original inputs, dates, contexts and mathematical limits. |

## Complete retained argument

<a id="argument"></a>
### The exact closed-cube quantity

For a monic integral polynomial P of degree d and an integer R>=0, write (Sx)_j=x_(j+1), I_R={-R,...,R+d}, and use exactly

    E_R(P)=min { sum_(j in I_R) x_j^2 :
                 x in [-1/2,1/2]^(I_R),
                 (P(S)x)_j in Z for -R<=j<=R,
                 (P(S)x)_0!=0 }.                         (1)

The value is infinity for an empty feasible set.
On the positive-Mahler irreducible unit domain with central roots, this is the quantity of [L G0130](Yin_C_G0335_v1.md#finite-rational-energy-coercivity), [L G0132](Yin_C_G0337_v1.md#tunable-salem-finite-energy-envelope), [L G0135](Yin_C_G0341_v1.md#coefficient-only-coercivity-radius) and [L G0136](Yin_C_G0342_v1.md#rational-energy-dual-certificates).
The preliminary construction below needs neither irreducibility nor that domain; Section 2 places it on an actual accepted irreducible Salem family.

The cube in (1) is closed.
Our witnesses attain some coordinates at +/-1/2.
They are not asserted to be rounding-error sequences of integral trace multipliers, and their cosine products would not furnish a positive amplitude.
They are legitimate upper witnesses for the exact energy minimum that the retained lower certificates must bound.

<a id="two-block-bounded-energy-witness"></a>
### 1. A two-block witness with no degree loss in its energy

Let f(t)=sum_(i=0)^r a_i t^i be monic and integral with a_0 in {1,-1} and every a_i in {0,1,-1}.
Degree r=0 is allowed.
Write f*(t)=t^r f(t^(-1)) and

    P_(N,sigma)=t^N f+sigma f*,
    N>r, sigma in {1,-1}, d=N+r,
    H_f=sum_(i=0)^r a_i^2.                               (2)

Because N>r, its two coefficient blocks do not overlap.
It is monic of degree d, with constant coefficient sigma.
No minimal-polynomial assertion is made for this general P_(N,sigma).

Let delta_r be the bilateral sequence that is one at r and zero elsewhere.
Define the finite sequence

    x=(1/2)[f(S)+sigma S^(-N) f*(S)] delta_r.             (3)

The first block has support in [0,r]; the second has support in [N,N+r].
The blocks are disjoint, each coordinate is 0 or +/-1/2, and both blocks lie in I_R for every R>=0.
Thus

    sum_j x_j^2=H_f/2.                                  (4)

Commuting the finite shift polynomials gives the exact identity

    P_(N,sigma)(S)x
      =sigma f(S)f*(S)delta_r
         +(1/2)S^N f(S)^2 delta_r
         +(1/2)S^(-N) f*(S)^2 delta_r.                   (5)

The three terms have respective supports contained in

    [-r,r],    [-N-r,-N+r],    [N-r,N+r].                (6)

In particular, if 0<=R<=N-r-1, the two outer supports lie strictly outside the tested defect interval [-R,R].
The middle defect on that interval is the integer sequence sigma f(S)f*(S)delta_r.
At the origin its value is

    sigma [t^r](f f*)=sigma sum_i a_i^2
                         =sigma H_f !=0.                (7)

The coefficient identity follows by pairing a_i with the coefficient a_i of t^(r-i) in f*.
Equations (3)--(7) therefore give the exact finite-energy upper bound

    E_R(P_(N,sigma))<=H_f/2,
                 0<=R<=N-r-1.                           (8)

All endpoint inequalities are strict where needed: at the largest allowed R=N-r-1, the nearest possible outer defects are at +/- (N-r)=+/-(R+1).
Values of x outside I_R are zero, so the finite recurrence in (1) agrees with the bilateral calculation.
No exterior recurrence or integrality beyond [-R,R] was assumed.

<a id="actual-salem-bounded-energy-window"></a>
### 2. An actual irreducible unbounded-degree family

Use precisely the accepted direct family of [L G0038](Yin_C_G0248_v1.md#family-cyclotomic-factors) and the no-padding progression checked in [L G0131](Yin_C_G0336_v1.md):

    f=t^3-t-1,   f*=1-t^2-t^3,
    P_N=t^(N+3)-t^(N+1)-t^N+1-t^2-t^3,
    N=9 mod120, N>=9.                                   (9)

The retained complete cyclotomic table excludes every cyclotomic factor on this progression.
The retained direct family theorem then says P_N itself is the monic irreducible Salem minimal polynomial, with degree d_N=N+3.
This argument uses L G0038's actual all-N scope; it does not import an unspecified sufficiently-large external Salem-construction threshold.

Here H_f=3 and r=3, so (8) proves

    E_R(P_N)<=3/2 for every 0<=R<=N-4=d_N-7.              (10)

For an explicit coordinate check, the only nonzero entries of x are

    x_0=1/2, x_2=-1/2, x_3=-1/2,
    x_N=-1/2, x_(N+1)=-1/2, x_(N+3)=1/2.

They are six distinct coordinates because N>=9.
The central integer polynomial in (5) is

    f f*=-t^6-t^5+t^4+3t^3+t^2-t-1,

so the origin defect is exactly 3.
Its outer half-integral defect blocks are outside the tested interval by (6).
This is an exact symbolic identity and its written verification, not an executed computation or a claimed numerical optimum.

The degree and root geometry are those of actual algebraic inputs.
For all N>=16 in this progression, the retained result also gives, with theta the plastic number,

    ||P_N||_1=6,
    theta<M(P_N)<4/3,    M(P_N)->theta>1.                 (11)

In particular the coefficient length is fixed and the positive logarithmic Mahler measures remain in the fixed compact interval [log theta,log(4/3)].
These controls do not approach measure one; they do not establish or refute a statement restricted to a sufficiently smaller near-one interval.

<a id="varying-degree-energy-lower-bound-boundary"></a>
### 3. What this rules out for an energy or dual shortcut

For each fixed P_N, E_R(P_N) still tends to infinity by L G0130.
Equation (10) instead lets the input vary, and its bounded-energy window has radius tending to infinity.
Therefore:

* There are no constants c>0 and C<infinity for which E_R(P)>=c log(R+1)-C holds for every R and every input P in even this coefficient-length-six, compact-measure family.
  Set R=d_N-7 in (10) and let N tend to infinity.
* A sufficient radius guaranteeing E_R(P)>3/2 cannot depend only on coefficient length and the threshold, independently of degree or other input data.
  On this family any valid integer threshold radius for that conclusion must exceed N-4, and hence be at least d_N-6.
* Every exact lower certificate for the unchanged closed-cube problem must respect (10), including dual certificates that use recurrence or stable/central information.

The last point has a direct dual form.
Let A be the recurrence matrix in L G0136 and z=Ax for the witness (3).
For any rational y, its clipped-quadratic dual expression D_z(y) satisfies

    D_z(y)<=||x||_2^2=3/2                                (12)

by weak duality.
Thus a complete certificate for E_R>3/2 cannot pass this one actual feasible defect when R<=d_N-7.
This obstruction retains both the box and every required integer defect; it is stronger in this respect than the previously retained cube-free Gram ceiling of one.

None of these statements rules out a fixed-P logarithmic lower bound with sufficiently P-dependent constants, or a bound whose radius or logarithm explicitly scales with degree.
They do not settle the sharper near-one Salem energy problem.
They do show that replacing compactness by an allegedly degree-independent dual logarithmic estimate cannot be justified by the existing energy problem alone, even on actual irreducible inputs.

<a id="tunable-orbit-length-energy-overlap"></a>
### 4. With free orbit length, cutoff overlap is possible but gives no lower amplitude

This separate consequence concerns the hypothetical Salem domain of L G0129, 0<m<=1/32, not the plastic family in (9)--(11).
Use its exact enlarged J_delta, central bound sqrt(m)/(16q sqrt(n)), and actual product C_delta at orbit length n.
Here n denotes the Fourier orbit length and is independent of the delay parameter N used above.

Choose the rational parameters of L G0132, for example

    8m<c<16m, mu=1/32,
    k=min {j>=1: 2^j c>=1},
    B_bar=k/6+mu/(32d^2).

Let R_* be the coefficient-only radius of L G0135 for the rational energy threshold 4 B_bar, and put

    M_*=2R_*+d+1,
    n_*=max(1,ceil(mu M_*/(64 B_bar))).                    (13)

Every quantity is explicitly finite for the fixed hypothetical input and its certified rational parameter choices.
By L G0135, E_(R_*)>4 B_bar.
By the exact rational implication in L G0132,

    n>=n_*  implies  C_delta<16m                         (14)

for every nonzero integral multiplier satisfying the stated central bound, at its actual height-dependent enlarged window.
No polynomial-height assumption or entropy/noise/time guards are needed for (14).

There is also exact compatibility with the finite candidate cutoff in L G0132.
Let M_cap be any valid such cutoff for this P and n.
If M_*>=M_cap, that result would give

    E_(R_*)<=m M_*/(64n)<=mu M_*/(64n)<=B_bar,

contradicting E_(R_*)>4 B_bar.
Therefore for every n>=n_*,

    M_*<M_cap.                                          (15)

Thus allowing the orbit length to grow does ensure a nontrivial finite-energy certificate below the relevant cutoff.
No claim of a practical size, overlap at a preassigned orbit length, or uniform cost as the input varies follows.
A statement that overlap is unproved should distinguish those quantitative aims from the elementary existence consequence (13)--(15).

For the polynomial-height multiplier family of L G0129, all its entropy/noise/time guards hold eventually for fixed P.
Taking n larger than their threshold and (13) is consistent: both mechanisms yield the same necessary upper restriction on C_delta.
This supplies no actual lower bound C_delta>=16m and therefore no Mahler contradiction.
An arithmetic lower-bound mechanism would have to confront these actual upper certificates; increasing n alone cannot supply the missing direction.
