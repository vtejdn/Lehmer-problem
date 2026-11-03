---
author: Yin
---

# G0001: binary entropy as expanding-neighborhood volume loss

Date: 2026-10-07.
Direct argument by assigned AI assess_shortness_route for Yin.
The coordinator identified the existing positive-volume implication in L G0035 and requested a converse or a precise remaining condition.
The new content is the two-sided neighborhood-volume estimate below and its converse when there are no unit-circle conjugates.
No source acquisition or computation is used.

<a id="expanding-neighborhood-volume-rate"></a>
## Exact arithmetic setup and volume-rate formula

Let alpha be a nontorsion algebraic unit with monic irreducible minimal polynomial P, degree d and m=log M(P)>0.
Let U be its expanding real Minkowski space.
Its dimension r counts expanding real embeddings once and expanding complex pairs twice.
Let s be the analogous real dimension of the unit-circle embeddings.
In particular r>=1.
Choose Euclidean coordinates in which each real block is multiplication by its conjugate and each complex block is its usual two-dimensional scale-rotation matrix.

Let pi_U:Q(alpha)->U be this expanding projection, let A be multiplication by alpha on U, and set v=pi_U(1).
Every block of A expands, so ||A^(-1)||<1, and

    |det A|=M(P)=exp(m).

The projection pi_U is injective on the number field: any one of its embedding coordinates already sends only zero to zero.
For n>=1 put

    T_n={sum_(j=0)^(n-1) epsilon_j alpha^j : epsilon_j in {0,1}},
    E_n=pi_U(T_n),    N_n=|T_n|=|E_n|,
    H=lim_n (log N_n)/n.

The limit exists and equals inf_n (log N_n)/n, because N_(n+k)<=N_n N_k.
Define the binary expanding attractor

    K={sum_(j>=1) epsilon_j A^(-j)v : epsilon_j in {0,1}},

and let B be the closed unit ball in U.
Uniform convergence of the series makes K compact, and 0 belongs to K.
For each n let

    V_n=Vol_r(K+A^(-n)B).

There are constants c_1,c_2>0, depending on P and these fixed coordinates but not on n, such that

    c_1 n^(-s) N_n exp(-nm) <= V_n
                             <= c_2 N_n exp(-nm).          (1)

Consequently

    lim_n (log V_n)/n = H-m.                               (2)

This identifies an actual jointly defined r-dimensional volume rate.
It is not the sum of separate one-dimensional covering conclusions.

<a id="norm-separation-with-central-loss"></a>
## Norm integrality supplies the separation and its exact loss

Set

    C_st=product_(|beta|<1) (1-|beta|)^(-1),

where beta runs over all contracting conjugates, with both members of a complex pair counted.
Thus C_st>=1, including the empty-product convention.
For two distinct elements of T_n, their difference is R(alpha)!=0 for a polynomial with coefficients in {-1,0,1} and degree at most n-1.
It is a nonzero algebraic integer, so its absolute norm is at least one.
At a contracting conjugate beta,

    |R(beta)|<=1/(1-|beta|),

and at a unit-circle conjugate it is at most n.
Therefore

    product_(|beta|>1) |R(beta)| >= C_st^(-1)n^(-s).

Every factor on the left is bounded by the Euclidean norm of pi_U(R(alpha)), with a complex pair contributing the corresponding squared modulus.
There are r such factors.
It follows that distinct points of E_n are separated by at least

    C_st^(-1/r)n^(-s/r).                                  (3)

This is uniform separation if s=0.
With unit-circle conjugates, the stated argument provides only the explicit polynomial loss.
It does not discard these conjugates or replace a projected coordinate difference by an integer.

Let omega_r be the volume of the unit ball and set

    delta_n=(1/3)C_st^(-1/r)n^(-s/r)<=1,
    c_1=omega_r/(3^r C_st),
    c_2=Vol_r(K+B).

The radius-delta_n balls centered at E_n are disjoint by (3), and all lie in E_n+K+B because 0 belongs to K.
Thus

    Vol_r(E_n+K+B)>=c_1 n^(-s)N_n.

The union of the N_n translates of K+B, on the other hand, has volume at most c_2 N_n.
The exact self-affine identity

    A^n K=E_n+K

now gives

    V_n=exp(-nm)Vol_r(E_n+K+B),                             (4)

which proves both sides of (1).
Taking logarithms and dividing by n proves (2), since s log n/n tends to zero.

This proof also supplies the familiar support upper bound without an additional entropy theorem.
Since A^(-n)B is contained in B, V_n<=c_2.
The first inequality of (1) gives

    N_n<=(c_2/c_1)n^s exp(nm),
    H<=m.                                                 (5)

The upper-bound mechanism is the arithmetic packing already retained in BV20; the additional use here is the matching volume estimate and the converse below.
No independence of digits or assertion about their probabilities is involved.

<a id="hyperbolic-binary-volume-equivalence"></a>
## A converse when there are no unit-circle conjugates

The compact sets K+A^(-n)B decrease to K.
Indeed the balls decrease under A^(-1), and their diameters tend to zero; compactness and closedness of K identify the intersection.
Their volumes are finite, so continuity of measure from above gives

    V_n decreases to Vol_r(K).                            (6)

If Vol_r(K)>0, (2) implies H=m.
This direction is already proved by the direct covering argument in [L G0035](Yin_L_G0035_v1.md#positive-volume-support-interface).

Suppose now s=0.
If H=m, subadditivity gives

    N_n>=exp(nH)=exp(nm) for every n.

Equation (1) then yields V_n>=c_1 for every n.
By (6), Vol_r(K)>=c_1>0.
Consequently, in the hyperbolic arithmetic case, meaning that no conjugate is on the unit circle,

    H_binary=m  if and only if  Vol_r(K)>0.                (7)

Equivalently, Vol_r(K)=0 implies the strict inequality H_binary<m in that case.
The converse is valid for the entire expanding projection, not because any collection of scalar attractor projections happens to have intervals.
No implication between positive volume and interior is needed or asserted in (7).

For every s, (2) gives the exact weaker equivalence

    H_binary=m  if and only if
        lim_n (log Vol_r(K+A^(-n)B))/n=0.                  (8)

Also H_binary=m implies the explicit all-n lower bound

    Vol_r(K+A^(-n)B)>=c_1 n^(-s).                        (9)

When s>0 this lower bound tends to zero, so (6) does not give positive volume.
A positive-volume converse in that case requires another argument.
Conversely H_binary<m forces the neighborhoods to lose volume exponentially at the exact rate m-H_binary, and in particular forces K to have zero volume.
These statements neither exhibit nor exclude an arithmetic example with H_binary=m and K of zero volume when unit-circle conjugates are present.

<a id="multiple-expansion-coverage-boundary"></a>
## Consequences and limitations for the multiple-expanding core

The canonical convex hull has already been ruled out as a binary covering body in the multiple-expanding, all-power degree-preserving domain by [L G0035](Yin_L_G0035_v1.md#power-stable-canonical-obstruction).
That fact does not determine the measure of K.
The present argument does not silently replace this failed joint cover by coordinatewise interval covers.

For the actual degree-22 core in [L G0039](Yin_L_G0039_v1.md#degree22-small-core-counterexample), the retained root certificate gives r=3 and s=16.
Hence the separation bound (3) has the exponent -16/3 and the volume comparison (1) loses n^16.
This input is not covered by the hyperbolic equivalence (7).
Its canonical-hull failure does not settle H_binary=m or positive volume; (8)--(9) state precisely what the current argument does provide.

No implication from M(P)<2 alone to positive volume has been proved here.
The formulas (1)--(9) hold more generally for the stated positive unit domain; the small-Mahler restriction does not remove their central-coordinate loss.
They are support-cardinality statements.
Positive volume and support attainment do not identify Shannon or Renyi entropy rates.
The one-expanding golden-ratio control and the accepted strict Shannon inequality in the no-unit-circle, M<2 scope of [BV20-U001](../audits/literature/BV20/Yin_U001.md#bv20-random-walk-entropy) already keep those quantities distinct.

Thus (7) is an exact geometric criterion in the hyperbolic case, and (2) is an exact volume-loss criterion in general.
Neither one supplies the missing positivity of the volume or a uniform lower bound on m.
No full classification of binary self-affine interiors, new source theorem, or claim of a Lehmer gap is included.

## Current proof and retained checking scope

The complete current statement and every original mathematical proof are retained in [C274](../claims/Yin_C_G0274_v1.md#argument), with its actual selected assessment.
The [current whole finding](../audits/reviews/Yin_R_G0533_v1.md#current-neighborhood-volume-finding) is self-reviewed.
The [original checking account and exact relationship findings](../audits/reviews/Yin_R_G0533_v1.md#historical-volume-author-finding) retain their original2026-10-07 inputs, contributions, scopes and limitations.
Original independent wording records the performed checks; it does not establish unrecorded initial isolation or transfer a finding to the new C.
