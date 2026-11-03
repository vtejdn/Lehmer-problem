---
author: Yin
---

# Exact binary support and expanding-neighborhood volume rates

This retains the entire original 2026-10-07 [L83 argument](../ledger/Yin_L_G0083_v1.md).
All original hypotheses, complete proofs, useful failures, source/evidence limits and remaining obligations are retained.
No source inspection or native calculation is newly executed.

## Statement

Let alpha be a nontorsion algebraic unit, P its monic irreducible polynomial, m=log M(P)>0, and U its full expanding real Minkowski space of dimension r>=1, counting each expanding complex pair twice.
Let s count the analogous real dimension of its unit-circle embeddings.
In the real scalar/complex scale-rotation coordinates let A be multiplication by alpha on U, v=pi_U(1), and B the closed unit ball.
The projection pi_U is injective on Q(alpha), ||A^(-1)||<1 and |det A|=exp(m).
For T_n={sum_(j<n)epsilon_j alpha^j:epsilon_j in{0,1}}, E_n=pi_U(T_n), N_n=|T_n|=|E_n| and H=lim log N_n/n=inf log N_n/n, define the compact attractor and its neighborhoods by

    K={sum_(j>=1)epsilon_j A^(-j)v:epsilon_j in{0,1}},
    V_n=Vol_r(K+A^(-n)B).

Set C_st=product_(|beta|<1)(1-|beta|)^(-1), counting both members of a contracting complex pair.
For all n>=1, distinct E_n points have separation at least C_st^(-1/r)n^(-s/r).
With omega_r the unit-ball volume, c1=omega_r/(3^r C_st)>0 and c2=Vol_r(K+B)>0,

    c1 n^(-s) N_n exp(-nm)<=V_n<=c2 N_n exp(-nm),
    lim_n log V_n/n=H-m, H<=m,
    V_n decreases to Vol_r(K).

The proof retains exact norm integrality, every complex-pair factor, disjoint packing, A^n K=E_n+K and continuity of measure.
Positive volume implies H=m.
When s=0 the converse holds and H=m iff Vol_r(K)>0.
For every s, H=m iff the neighborhood volumes have zero exponential rate, and H=m implies V_n>=c1 n^(-s) for every n.
If H<m, the exact neighborhood-volume loss rate is m-H and K has zero volume.
When s>0 the polynomial lower bound alone proves no positive-volume converse and neither constructs nor excludes H=m with zero volume.
The already accepted degree22 unit has r=3,s=16, so the actual separation exponent is-16/3 and the packing loses n^16; it is outside the hyperbolic converse.
These are full expanding-space support statements, with no inference from coordinate projections, positive volume to interior, M<2 to positive volume, probability entropy equality or a uniform Mahler gap.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:37 |
| status | open |
| reason | Register the complete original mathematics and exact existing inputs; actual current whole review and adoption follow separately. No independent-review claim, new source audit, native execution or Task resumption is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Full arithmetic/Minkowski setup and all constants, exact separation/volume rate, hyperbolic iff and general central-loss alternatives, precise degree22 r=3/s=16 control and every probability/positivity boundary. |
| argument | [Entire original proof](#argument) | Entire original norm packing with complex multiplicities, disjoint balls and set identity, nested-neighborhood/measure limit, subadditive-infimum converse and all central-loss/counterexample limitations. |
| dependency | [Existing volume and canonical-body controls](Yin_C_G0239_v1.md#positive-volume-support-interface) | Exact positive-volume support implication; the same complete C retains the all-power-preserving canonical convex obstruction. This proof supplies its own full reverse estimate. |
| dependency | [Canonical-body obstruction](Yin_C_G0239_v1.md#power-stable-canonical-obstruction) | Only the previously established failure of the canonical joint cover on the multiple-expanding degree-stable domain; it does not decide actual attractor volume. |
| support | [Exact degree22 core](Yin_C_G0249_v1.md#degree22-small-core-counterexample) | Existing full root certificate gives three real expanding dimensions and sixteen unit-circle dimensions; reused unchanged with no native rerun. |
| support | [Arithmetic packing and probability comparison](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Recorded norm-packing attribution and accepted strict Shannon inequality only at its nonzero/no-unit-circle/M<2 scope; no fresh source proof is used. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:45 |
| status | proved |
| reason | Adopt the complete original two-sided neighborhood-volume theorem, exact rate and hyperbolic converse after actual whole self-review. Every norm/complex dimension/packing/measure step is retained, with the explicit n^(-s) loss and no unsupported positive-volume converse when s>0 or probability-entropy equality. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Full arithmetic/Minkowski setup and all constants, exact separation/volume rate, hyperbolic iff and general central-loss alternatives, precise degree22 r=3/s=16 control and every probability/positivity boundary. |
| argument | [Argument](#argument) | Entire original norm packing with complex multiplicities, disjoint balls and set identity, nested-neighborhood/measure limit, subadditive-infimum converse and all central-loss/counterexample limitations. |
| dependency | [Dependency](Yin_C_G0239_v1.md#positive-volume-support-interface) | Exact positive-volume support implication; the same complete C retains the all-power-preserving canonical convex obstruction. This proof supplies its own full reverse estimate. |
| dependency | [Dependency](Yin_C_G0239_v1.md#power-stable-canonical-obstruction) | Only the previously established failure of the canonical joint cover on the multiple-expanding degree-stable domain; it does not decide actual attractor volume. |
| support | [Support](Yin_C_G0249_v1.md#degree22-small-core-counterexample) | Existing full root certificate gives three real expanding dimensions and sixteen unit-circle dimensions; reused unchanged with no native rerun. |
| support | [Support](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Recorded norm-packing attribution and accepted strict Shannon inequality only at its nonzero/no-unit-circle/M<2 scope; no fresh source proof is used. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0533_v1.md#current-neighborhood-volume-finding) | Entire current statement, complete original argument and all selected interfaces at their exact scope, self-reviewed; old findings keep their original fixed inputs and relationships. |

## Complete retained argument

<a id="argument"></a>

<a id="expanding-neighborhood-volume-rate"></a>
### Exact arithmetic setup and volume-rate formula

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
### Norm integrality supplies the separation and its exact loss

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
### A converse when there are no unit-circle conjugates

The compact sets K+A^(-n)B decrease to K.
Indeed the balls decrease under A^(-1), and their diameters tend to zero; compactness and closedness of K identify the intersection.
Their volumes are finite, so continuity of measure from above gives

    V_n decreases to Vol_r(K).                            (6)

If Vol_r(K)>0, (2) implies H=m.
This direction is already proved by the direct covering argument in [L G0035](Yin_C_G0239_v1.md#positive-volume-support-interface).

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
### Consequences and limitations for the multiple-expanding core

The canonical convex hull has already been ruled out as a binary covering body in the multiple-expanding, all-power degree-preserving domain by [L G0035](Yin_C_G0239_v1.md#power-stable-canonical-obstruction).
That fact does not determine the measure of K.
The present argument does not silently replace this failed joint cover by coordinatewise interval covers.

For the actual degree-22 core in [L G0039](Yin_C_G0249_v1.md#degree22-small-core-counterexample), the retained root certificate gives r=3 and s=16.
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
