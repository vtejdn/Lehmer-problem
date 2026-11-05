---
author: Yin
---
# Anti-reciprocal sign lifts: a three-pair margin and the unresolved four-pair case

This working analysis serves the [unrestricted Lehmer contract](../tasks/Yin_T_G0001_v1.md#contract) and the [binary reflection inquiry](Yin_D_G0013.md#binary-reflection-reduction).
The near_one_geometry contributor derived the original four-frequency calculations under the main agent's research assignment.
They are author work, not an independent mathematical review or an adopted fixed theorem.
The four-frequency uniform good-sign assertion remains unproved.
The three-frequency theorem and exact four-pair second-moment obstruction are adopted in [C862](../claims/Yin_C_G0862_v1.md#decision-whole-independent-review-2026-11-04).
[C863 v4](../claims/Yin_C_G0863_v4.md#decision-whole-independent-review-2026-11-04) now gives the uniform bound in every torus dimension at least two and an explicit finite circle remainder.
The remaining working arguments here concern that pure circle sign problem and failed sufficient estimates.
[C864 v2](../claims/Yin_C_G0864_v2.md#decision-whole-independent-review-2026-11-04) already covers every supplied binary four-pair auxiliary through a finite-period return; finishing the circle problem is not a prerequisite for that arithmetic class and does not supply an auxiliary for unrestricted G0001.

## Exact question and normalization

Let a_1,a_2,a_3,a_4 be distinct positive integers, and put

    S_epsilon(theta)=sum_(j=1..4) epsilon_j sin(a_j theta),
    F_epsilon(z)=sum_(j=1..4) epsilon_j(z^(a_j)-z^(-a_j)).

Here every epsilon_j is either +1 or -1.
Multiplication by one Laurent monomial makes F_epsilon an integer polynomial without changing its logarithmic Mahler measure.
It is nonzero because its eight exponents are distinct.
On the unit circle F_epsilon=2i S_epsilon, so

    m(F_epsilon)=log2+integral_T log|S_epsilon(theta)|.

All circle integrals in this note use normalized Haar measure.
Each displayed logarithm is integrable: after clearing a monomial the function is a nonzero polynomial, whose finitely many circle zeros give only finite-order logarithmic singularities.

The same question for distinct positive half-integers is included.
Writing a_j=k_j/2 with every k_j odd and substituting phi=theta/2 gives the integer-frequency expression on an interval of length pi.
Its absolute value is pi-periodic because all k_j are odd, so its normalized integral equals the full-circle integral for the k_j.
Clearing the common half-integer phase also leaves integer polynomial exponents.
This reduction changes neither the Mahler integral nor the number of sign choices.

The desired assertion is that some sign choice has m(F_epsilon)<log2.
The stronger useful form asks for an eta>0 independent of all four frequencies such that some choice has m(F_epsilon)<=log2-eta.
Neither assertion is established here.

## Exact product of the eight sign classes

Changing every sign simultaneously changes F only by -1.
It therefore suffices to take epsilon_1=1 and all eight choices of the other signs.
At a fixed angle write s_j=sin(a_j theta), u_j=s_j^2, and

    Q(u)=sum_j u_j^2-2 sum_(i<j)u_i u_j,
    D(u)=Q(u)^2-64u_1u_2u_3u_4.

Then the exact polynomial identity is

    product_(epsilon_2,epsilon_3,epsilon_4 in {+1,-1})
        (s_1+epsilon_2 s_2+epsilon_3 s_3+epsilon_4 s_4)
      =D(u).                                                   (1)

For a direct derivation, first fix epsilon_2 and set X=(s_1+epsilon_2 s_2)^2.
Pairing the two choices of epsilon_4, then the two choices of epsilon_3, gives

    product_(epsilon_3,epsilon_4)(s_1+epsilon_2s_2+epsilon_3s_3+epsilon_4s_4)
      =(X-u_3-u_4)^2-4u_3u_4.

Put A=u_1+u_2-u_3-u_4.
Multiplying the remaining two choices of epsilon_2 yields

    [(A+2s_1s_2)^2-4u_3u_4][(A-2s_1s_2)^2-4u_3u_4]
      =(A^2-4u_1u_2-4u_3u_4)^2-64u_1u_2u_3u_4.

Expanding A^2-4u_1u_2-4u_3u_4 gives Q(u), proving (1).
Since every factor is a nonzero trigonometric polynomial, their product is also nonzero, and the logarithmic identity can be integrated through its finite zero set.
Thus

    (1/8)sum_(epsilon_1=1)m(F_epsilon)
      =log2+(1/8)integral_T log|D(sin^2(a_1 theta),...,sin^2(a_4 theta))|.  (2)

A negative upper bound for the last integral would supply a good sign, and a uniform negative bound would supply a uniform margin.
Formula (2) is an exact reformulation for this averaging method, not a proof that this integral is negative.
The existence of one good sign does not conversely require the eight-sign average to be below log2.

There is no sufficient pointwise nonpositive bound.
For s_1=s_2=s_3=1 and s_4=0, one has D=9 and the eight-sign average of log|S_epsilon| is (log9)/8>0.
This is a pointwise algebraic obstruction, not an asserted simultaneous realization by a particular four-frequency circle orbit.

<a id="three-pair-uniform-margin"></a>
## Fixed three-pair margin

The complete three-pair Fourier table, resonance proof and uniform eta_3=log(128/105)/8 are now [C862](../claims/Yin_C_G0862_v1.md#decision-whole-independent-review-2026-11-04), adopted through independent R1078.
The same fixed argument includes integer and half-integer frequencies, one/two-pair cases, the original-window arithmetic consequence and all zero-value boundaries.
These conclusions need no frequency cutoff or separation hypothesis.

<a id="four-pair-second-moment-obstruction"></a>
## Fixed limitation of the four-pair second-moment method

The exact four-pair product table and the actual tuple (1,9,81,729), with second moment 17109/8192>1, are fixed in [C862's comparison](../claims/Yin_C_G0862_v1.md#four-pair-second-moment-obstruction).
This excludes only the universal direct L2/Jensen certificate below one.
It neither excludes a good sign nor estimates the logarithmic average itself.
The remaining working arguments below retain their actual unresolved scope.

## Exact second and fourth moments, and why they do not close the problem

Let E denote joint averaging over the circle and the eight sign classes.
For even functions of S this equals averaging over all sixteen signs.
Sign averaging removes every monomial having an odd multiplicity of some s_j, giving

    E S^2=sum_j integral_T sin^2(a_j theta)=2,
    E S^4=sum_j integral_T sin^4(a_j theta)
             +6sum_(i<j)integral_T sin^2(a_i theta)sin^2(a_j theta)
           =4*(3/8)+6*6*(1/4)=21/2.                    (3)

For the pair integral, expand sin^2(a theta)=(1-cos(2a theta))/2.
The distinct positive frequencies make the mixed cosine integral zero by orthogonality.
These two moments therefore do not depend on any additive relations among the four distinct frequencies.
Also |S|<=4, so T=S^2 is supported on [0,16].

The data E T=2, E T^2=21/2 and 0<=T<=16 alone cannot imply E log|S|<0.
Indeed the abstract probability law

    Pr(T=3/2)=26/27,    Pr(T=15)=1/27

has exactly those two moments, while

    (1/2)E log T=(26log(3/2)+log15)/54>0.              (4)

Both support points exceed one, making the strict sign immediate.
This abstract law is not claimed to come from a sine/sign family.
It proves only that a proof using solely the two moments in (3) and the range bound cannot establish the desired logarithmic sign.
Higher moments or other information about the actual circle orbit remain available but were not controlled here.

## A wider reflection-contraction shortcut is false

One possible shortcut would assert

    M(P(z)-P(z^(-1)))<=M(P)

for every real or integer coefficient polynomial P with P(0)=0.
That statement is false even for a two-term integer polynomial.
Take P(z)=10z+z^3, for which M(P)=10.
Direct multiplication gives

    z^3(P(z)-P(z^(-1)))
      =z^6+10z^4-10z^2-1
      =(z^2-1)(z^4+11z^2+1).

The quadratic polynomial y^2+11y+1 has two negative reciprocal roots.
The larger root modulus is (11+sqrt117)/2, so the two outside z-roots of z^4+11z^2+1 give

    M(P(z)-P(z^(-1)))=(11+sqrt117)/2>10.              (5)

The final inequality follows from sqrt117>9.
This disproves the general reflection-contraction premise only.
It does not disprove a theorem retaining four unit coefficients or the existence of a favorable sign choice.

## Reuse, source search and remaining boundary

The directly read [C844 scalar margin](../claims/Yin_C_G0844_v1.md#uniform-energy-logarithmic-margin) supplies a uniform strict field-free margin for an integer seed of energy at most q^2 after division by q, apart from its specified monomials.
[C845](../claims/Yin_C_G0845_v1.md#statement) supplies the varying-seed phase comparison with its actual separation condition.
[C849](../claims/Yin_C_G0849_v1.md#statement) supplies the fixed-template all-ratio construction with its strict template mean and finite-template hypotheses.
These statements do not themselves assert the present arbitrary-frequency anti-reciprocal sign bound.
In particular (5) prevents removing the phase difficulty by assuming unrestricted reflection contraction.

Bounded web searches used the terms Mahler measure, sine polynomial, random signs, anti-reciprocal, eight terms, and real or imaginary part.
They did not locate a directly usable fixed-four-pair theorem in the material inspected during this round.
Search results about general Littlewood or continuous random coefficient asymptotics were not adopted as proof inputs.
An attempted opening of the Dubickas quadrinomial PDF at the Kyoto EMIS address returned HTTP403, so that attempted source supplies no inspected theorem here.
No external theorem is used in (1)--(5), and no claim of exhaustive search or mathematical novelty is made.

The finite sign diagnostics belong to [J134](../computations/programs/Yin_J_G0134/readme.md#binary-sign-screen) and their interpretation to the separate D13 inquiry.
They are not premises of this analysis and do not certify an all-frequency assertion.
The three-frequency circle question has the complete author proof draft (T1)--(T7), pending separate review.
A bounded follow-up search on 2026-11-05 used the queries “Mahler measure sum three sine functions signs trinomials” and “Mahler measure sine polynomial random signs quadrinomials”; the inspected results did not supply the present sign-product bound, and no external theorem was adopted from that search.
The true remaining analytic question here is whether an actual four-frequency circle orbit always has at least one sign with negative integral of log|S_epsilon|, with or without a uniform strict margin.
This note supplies neither that four-frequency proof nor a counterexample to it.
