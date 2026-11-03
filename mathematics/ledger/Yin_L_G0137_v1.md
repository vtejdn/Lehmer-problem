---
author: Yin
---

# A long bounded-energy window on actual irreducible Salem inputs

Date: 2026-10-08.
Direct bounded G0001 derivation by the assigned execution_and_deliverables AI for Yin.
The coordinator requested a new finite-energy mechanism or an exact obstruction to a proposed degree-independent shortcut.
This note supplies an actual algebraic control, not another compactness or computability theorem.
Its final section records a separate direct consequence of the existing L G0132/L G0135 interfaces when the orbit length is free to grow.
No numerical experiment, optimization or source acquisition has been performed.
Completed independent full review is recorded below.

## The exact closed-cube quantity

For a monic integral polynomial P of degree d and an integer R>=0, write (Sx)_j=x_(j+1), I_R={-R,...,R+d}, and use exactly

    E_R(P)=min { sum_(j in I_R) x_j^2 :
                 x in [-1/2,1/2]^(I_R),
                 (P(S)x)_j in Z for -R<=j<=R,
                 (P(S)x)_0!=0 }.                         (1)

The value is infinity for an empty feasible set.
On the positive-Mahler irreducible unit domain with central roots, this is the quantity of [L G0130](Yin_L_G0130_v1.md#finite-rational-energy-coercivity), [L G0132](Yin_L_G0132_v1.md#tunable-salem-finite-energy-envelope), [L G0135](Yin_L_G0135_v1.md#coefficient-only-coercivity-radius) and [L G0136](Yin_L_G0136_v1.md#rational-energy-dual-certificates).
The preliminary construction below needs neither irreducibility nor that domain; Section 2 places it on an actual accepted irreducible Salem family.

The cube in (1) is closed.
Our witnesses attain some coordinates at +/-1/2.
They are not asserted to be rounding-error sequences of integral trace multipliers, and their cosine products would not furnish a positive amplitude.
They are legitimate upper witnesses for the exact energy minimum that the retained lower certificates must bound.

<a id="two-block-bounded-energy-witness"></a>
## 1. A two-block witness with no degree loss in its energy

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
## 2. An actual irreducible unbounded-degree family

Use precisely the accepted direct family of [L G0038](Yin_L_G0038_v1.md#family-cyclotomic-factors) and the no-padding progression checked in [L G0131](Yin_L_G0131_v1.md):

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
## 3. What this rules out for an energy or dual shortcut

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
## 4. With free orbit length, cutoff overlap is possible but gives no lower amplitude

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

## Contributions and review

The assigned execution_and_deliverables AI derived and checked (1)--(15), including the shift support endpoints, actual-family specialization and the separate tunable-length consequence.
The coordinator requested the direction and received progress reports but did not contribute the witness or derivation.
The two direct family interfaces were read at their fixed scope; no external construction or original-source proof was imported.

On 2026-10-08 the coordinating AI for Yin independently checked the complete (1)--(15) and all subsequent scope statements.
It received the direction and progress outlines, so the review was not blind; it contributed neither the witness nor its derivation.
Coverage includes the bilateral shift convention, r=0 and both signs, disjoint blocks and exact supports, restriction to I_R and all endpoint inequalities, the nonzero origin, the six explicit Salem coordinates and central polynomial, the actual no-padding progression, the logarithmic/radius/dual consequences and their varying-input scope, and the separate rational orbit-length threshold and cutoff comparison.
The reviewer directly read the used L G0038/L G0131 family statements, L G0132 threshold and cutoff arguments, L G0135 explicit radius, L G0129 eventual guards and L G0136 weak-dual interface.
No substantive defect or missing hypothesis was found.

This is complete independent written-proof review; it does not claim an executed mathematical experiment, a formal proof or a new audit of external source proofs.
The coordinator accepted the finding for fixed preservation on 2026-10-08.
The unrestricted G0001 Task is unresolved.
