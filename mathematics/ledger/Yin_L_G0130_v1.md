---
author: Yin
---

# An effective finite-energy modulus for central-small transition collapse

Current checking scope is owned by [R556](../audits/reviews/Yin_R_G0556_v1.md), with its exact findings and declared relationships.
Retained review narration and relationship labels below preserve historical declarations; they do not establish an independent current relationship beyond those responsible findings.


Date: 2026-10-08.
Direct derivation by the coordinating Codex AI for Yin, under the current G0001 exploration instruction.
This supplies a terminating finite rational algorithm for the modulus left unspecified in [L G0125](Yin_L_G0125_v1.md#central-small-transition-collapse).
It does not supply a practical running-time bound, a degree-uniform decay rate, or a positive Mahler gap.
No numerical experiment, new source or novelty assertion is a premise.
The completed checking account is retained below at its responsible finding scope.

## Domain and question

Let P(t)=sum_(i=0)^d p_i t^i be the monic irreducible minimal polynomial of an algebraic unit alpha, with positive logarithmic Mahler measure and q>0 central embeddings.
Complex conjugates are counted separately.
Keep b=1/16 and exactly the traces, admissible windows, transition product C(theta,J), and Fourier smoothing used in L G0125.
The qualitative result there proves C(theta,J)->0 as all central conjugates of the nonzero integral multiplier theta tend to zero, uniformly in the admissible J and without a height assumption.

Here, for every rational 0<c<1, a terminating algorithm computes a positive rational delta(P,c) such that

    max_central |sigma(theta)| <= delta(P,c)
       and J admissible imply C(theta,J)<c.          (1)

The algorithm involves exact rational finite optimization.
Its termination is proved, not inferred from an experiment.
A separate consequence makes the actual o(N) orbit budget effective when explicit polynomial height and central-smallness bounds are supplied.

<a id="finite-rational-energy-coercivity"></a>
## A nested family of finite rational energy problems

For each integer R>=0, put

    I_R={-R,...,R+d},  M_R=2R+d+1,
    Z_P=floor((1/2) sum_(i=0)^d |p_i|).

Let K_R be the set of real vectors x=(x_j)_(j in I_R) satisfying

    |x_j|<=1/2 for all j in I_R,
    sum_(i=0)^d p_i x_(j+i) is an integer for -R<=j<=R,
    sum_(i=0)^d p_i x_i !=0.                         (2)

Every integer in (2) is between -Z_P and Z_P.
Thus K_R is a finite union of compact rational polytopes, one for each possible integer defect vector with a nonzero entry at j=0.
Define

    E_R=min_(x in K_R) sum_(j in I_R) x_j^2,         (3)

with E_R=+infinity if K_R is empty.
Each finite E_R is rational and can be computed exactly as follows.
Enumerate the integer defect vectors, then the box faces (each coordinate fixed to -1/2, fixed to 1/2, or free).
For each consistent affine equality system, compute the orthogonal projection of zero onto its affine solution space by rational Gaussian elimination.
Retain the projection if it satisfies the box inequalities; minimize its rational squared norm over the retained points.
Empty affine systems and projections outside the box are discarded.
This finite procedure finds every relevant optimum: at a minimizer, take its smallest box face; relative to the equalities and that face its free directions have zero first derivative, so the point is exactly the indicated affine projection.
Redundant equations do not change this argument or rationality.

Restriction from I_(R+1) to I_R preserves every condition (2), and discarding coordinates cannot increase energy.
Consequently

    E_R <= E_(R+1),             E_R -> +infinity.    (4)

For the second assertion, suppose that E_R<=B for arbitrarily large R.
Choose minimizers at such R.
Their coordinates lie in the fixed compact interval [-1/2,1/2].
Diagonal extraction on the integers yields a pointwise limit x.
Pass first to a subsequence on which the defect at zero is one fixed nonzero integer; there are finitely many choices.
Finite-coordinate continuity then gives P(S)x integer-valued everywhere with nonzero defect at zero, where (Sx)_j=x_(j+1).
Fatou on each finite interval gives sum_(j in Z)x_j^2<=B, hence x is in l2 and therefore c0.
But [L G0115](Yin_L_G0115_v1.md#unit-circle-c0-integer-forcing) allows only zero for a c0 sequence in the closed cube with integer P(S)x.
This contradicts the nonzero defect.
This proves (4), including the possibility that a finite K_R is already empty.
No bound on the position of any defect in an original infinite sequence was used.

Two exact controls clarify this auxiliary statement, which itself only needs the L G0115 unit-circle hypothesis.
For P=t+1, a nonzero integer defect at zero forces x_0=x_1=1/2 or x_0=x_1=-1/2.
Integrality of every adjacent sum then propagates |x_j|=1/2 throughout I_R.
Conversely such sign choices with equal middle signs are feasible, so E_R=(2R+2)/4.
This is an analytic check, not an executed enumeration.
If the unit-circle hypothesis is removed, divergence can fail: for P=t-2 the sequence x_j=2^(j-1) for j<=0 and x_j=0 for j>0 has defect -1 at zero, zero elsewhere, lies in the closed cube, and has energy 1/3.
Its restrictions give E_R<=1/3 for every R.
These controls concern the auxiliary energy problem, not the positive-Mahler unit domain of the transition theorem.

<a id="effective-central-transition-modulus"></a>
## A computable modulus uniform in height and admissible window

Use the explicit fixed-P tail constant of L G0125,

    E_P=4b^2[B_s^2/(1-rho_s^2)+B_u^2/(1-rho_u^2)], (5)

where B_s and B_u are the sums of absolute values of the respective inverse Vandermonde entries, and rho_s,rho_u are the largest stable and reciprocal-expanding moduli.
These are finite real algebraic quantities.
Certified rational upper bounds can be obtained from isolations of the distinct algebraic roots and exact algebraic arithmetic; no transcendental comparison is needed for (5).

Choose an integer B>=1 with

    B > E_P+2/c > E_P-2log(c)/pi^2.                 (6)

Search R=0,1,2,... until the exact procedure (3) reports E_R>4B.
By (4) this search terminates.
Set

    delta(P,c)=min(1/(16q),1/(4q M_R)).             (7)

This is a positive rational determined by a finite, terminating algorithm from P and c (different certified upper choices of B are allowed).
No bound on the terminal R or the algorithm's complexity is asserted.

To prove (1), suppose that epsilon=max_central|sigma(theta)|<=delta and C(theta,J)>=c for an admissible J.
L G0125's complete rounding construction supplies real sequences e,h on Z with

    |e_j|<1/2,
    P(S)e integer-valued and not identically zero,
    ||h||_2^2 <= E_P-2log(c)/pi^2 < B,
    ||e-h||_infinity <=2q epsilon.                 (8)

Its tail-identification hypothesis q epsilon<=b follows from (7).
In detail, e is the nearest-integer error of twice the stable-plus-central trace, and h subtracts just the positive central tail from e.
The main argument uses a uniformly small error from an l2 sequence; it does not falsely assert e itself is in l2.
The integer defect is nonzero by the bounded homogeneous-mode and negative-tail argument of L G0125, which applies at these same hypotheses.

Translate e and h so one nonzero defect occurs at zero.
On I_R the translated e is an element of K_R, whereas (7)--(8) give

    ||e|_(I_R)||_2
       <= ||h||_2 + sqrt(M_R)||e-h||_infinity
       < sqrt(B)+1/(2sqrt(M_R))
       <= sqrt(B)+1/2 < 2sqrt(B).                  (9)

Its energy is strictly below 4B, contradicting E_R>4B.
This proves the asserted modulus for every height and every admissible J.
The argument gives a finite certificate once R and E_R are found, not merely an undecidable test for an infinite limiting condition.

<a id="effective-polynomial-height-orbit-budget"></a>
## Effective full orbit budget under explicit growth bounds

Suppose now that for every integer N>=1 a nonzero integral theta_N is supplied with certified bounds

    max_central |sigma(theta_N)| <= kappa/sqrt(N),
    H_N=max_sigma|sigma(theta_N)| <= C_0 N^A,
    C_0>=1, A>=0, kappa>0,                         (10)

where the constants are fixed and effectively given (rational upper bounds suffice).
Use the standard admissible window J_N=ceil(log(16dH_N)/lambda), lambda=-log rho>0, and the exact actual smoothing and nonnegative-time orbit of L G0125.
For every rational gamma>0 one can compute an integer N_0 such that

    sum_(t>=0) g(|hat f_N(zeta_(theta_N,t))|)
         <= gamma N for every N>=N_0.              (11)

Here g is the same binary information function as L G0120.
To verify this, choose rational 0<c<1 with c^2<=gamma/2, and compute delta(P,c).
For N>=(kappa/delta)^2, (1) gives C_N=C(theta_N,J_N)<c.
The exact L G0125 budget estimate is

    sum_(t>=0)g(|hat f_N|)
      <= N g(C_N)
         +(2J_N+1+R_N+rho_*^2/(1-rho_*^2))log2,    (12)

where one fixed stable place beta_* is chosen, rho_*=|beta_*|, lambda_*=-log rho_*>0, D_N=K_*/|sigma_*(theta_N)|, R_N=ceil(log_+(D_N)/lambda_*), and K_*>0 is precisely the real-interval or complex-disc noise constant given in L G0125.
Its integer norm estimate gives D_N<=K_*H_N^(d-1).
Consequently the second term of (12) is at most K_0+K_1 log N, where

    K_0=log2 [2log(16dC_0)/lambda+4
               +log_+(K_* C_0^(d-1))/lambda_*
               +rho_*^2/(1-rho_*^2)],
    K_1=log2 [2A/lambda+A(d-1)/lambda_*].           (13)

Both are nonnegative and effectively bounded from above.
The four units in K_0 include both ceilings in 2J_N and R_N and the separate one in (12); no endpoint time is omitted.

Using rational upper bounds for these constants, choose N_0>=3 with N_0>=(kappa/delta)^2 and

    (K_0+K_1 log N_0)/N_0 < gamma/2.               (14)

Doubling N_0 until a certified strict comparison succeeds terminates.
For N>=3 the left-hand ratio is nonincreasing, as its derivative is [K_1-K_0-K_1 log N]/N^2<=0.
Finally g(C_N)<=g(c)<=log2 c^2<=gamma/2; substituting into (12) proves (11).
This is a uniform statement over every sequence satisfying the supplied bounds (10), with P and those bounds fixed.
It includes the explicit polynomial-height family of L G0123.
It requires no actual enumeration of that family's multipliers.

## Consequence and limits

The original qualitative collapse in L G0125 remains valid and fixed.
This note adds an algorithmically effective modulus by finite rational energy exclusion, rather than changing the theorem's hypotheses.
For the explicit height/central bounds (10), it also adds a computable threshold for the whole actual nonnegative-time o(N) budget.

The proof does not supply a simple rate as a function of N, a uniform bound over P or its degree, or a practicable complexity guarantee.
The required R and N_0 may be extremely large.
It does not upper-bound the complete relative entropy, identify h_1 with m, or rule out other frequency families, different smoothing or effective finite-window tests before the computed threshold.
It does not supply the amplitude lower bound needed for a Mahler contradiction.

No implementation of (3) or numerical output E_R has been produced in this round.
The deliverable is a proved terminating algorithm and its mathematical consequences, not a claimed executed optimization.
The next useful use is a certified finite exclusion for an actual fixed P and threshold c, if its cost informs a concrete amplitude search.

## Contribution and actual review

The coordinator derived (2)--(14) and checked rational optimization, compactness, the translated finite certificate and every growth-cost constant against the used L G0115 and L G0125 interfaces.
This is author verification.

On 2026-10-08, the separately assigned entropy_status AI for Yin independently checked the complete final (1)--(14), including the two analytic controls.
The author's outline was supplied beforehand, so the review was not blind; the reviewer did not contribute to this proof.
It rederived the finite defect range, rational-polytope/box-face projection algorithm, rationality and completeness of the minima, restriction monotonicity, diagonal/Fatou coercivity and closed-cube contradiction.
It directly checked the full used L G0115 c0 argument and the L G0125 Vandermonde, rounding, nonzero-defect and full budget interfaces.
It verified algebraic computability of (5), rational B and delta, defect translation, all norm/error inequalities, both controls, the K_0/K_1 coefficients including all four ceiling/endpoint units, and the effective overhead threshold and its extension to every N>=N_0.
No substantive defect was found.
This review covers the proved algorithm and fixed-input consequence, not an executed optimization, a practical complexity bound, degree-uniform rate or full relative-entropy estimate.
No file edit, new source inspection or numerical computation was part of that review.

The coordinator accepted this effective refinement for fixed-ledger preservation on 2026-10-08.
Earlier fixed qualitative proofs are preserved; G0001 remains unresolved.
