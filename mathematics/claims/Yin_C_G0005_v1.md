---
author: Yin
---

# Simple-factor annihilators with explicit degree and coefficient costs

Date: 2026-10-10T14:59.
Human author: Yin.
Provenance: project deduction.
Organization requested by Yin; [G0001 remains paused](../tasks/Yin_T_G0001_v1.md#decision-human-pause-after-closeout).

## Current assessment
[Selected decision](#decision-current-norm-grid-proof-home)

## Assessment history
### Decision initial
The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-10T14:59 |
| status | open |
| reason | The complete local candidate is fixed for reuse; historical author self-checks are retained, but no acceptance review or proved judgment is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only the enumerated conclusions under their stated hypotheses and exclusions. |
| argument | [Argument](#argument) | The selected retained derivations and declared fixed inputs; open transfers and source-screen conclusions are excluded. |
| dependency | [Norm-grid method](../ledger/Yin_L_G0091_v1.md#norm-grid-support-bound) | Existing lattice-cell/norm interface, adapted in the retained complete calculation with explicit alphabet and dimension costs. |


### Decision open-candidate

| Field | Value |
| --- | --- |
| date | 2026-10-20T21:22 |
| status | open |
| reason | The exact finite digit-grid, simple-factor multiple and derivative-comparison conclusions remain candidates awaiting an applicable acceptance review; no annihilator propagation/cost transfer or near-one gap is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only Parts A-C under their original nonzero algebraic-integer, degree, height and coefficient hypotheses. |
| argument | [Retained candidate](#argument) | Complete equations (1)-(5), including strict pigeonhole, degree guard and divided-derivative integrality; later residue/finite-cut formulas and missing transfers remain unadopted context. |
| dependency | [Norm-grid interface](../ledger/Yin_L_G0091_v1.md#norm-grid-support-bound) | Existing lattice-cell/norm interface, adapted in the retained calculation with explicit alphabet and dimension costs. |


### Decision current-norm-grid-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:23 |
| status | open |
| reason | Select C281 as the complete responsible home of the same original norm-grid proof already used by this candidate. The exact nonzero algebraic-integer/real-complex cell interface is unchanged and the candidate retains its own explicit alphabet/dimension adaptation. This is a current same-content locator adoption, with no new mathematics, acceptance review, change to Parts A-C or adoption of the later unadopted context; all original dated decisions and fixed review inputs remain intact. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only Parts A-C under their original nonzero algebraic-integer, degree, height and coefficient hypotheses. |
| argument | [Argument](#argument) | Complete equations (1)-(5), including strict pigeonhole, degree guard and divided-derivative integrality; later residue/finite-cut formulas and missing transfers remain unadopted context. |
| dependency | [Dependency](Yin_C_G0281_v1.md#norm-grid-support-bound) | Existing lattice-cell/norm interface, adapted in the retained calculation with explicit alphabet and dimension costs. |

## Statement

Let P be the monic irreducible minimal polynomial of a nonzero algebraic integer alpha, with degree d and logarithmic Mahler measure m.
All digit coefficients below are integers.

**A. Finite digit grid.** For integers n,H>=1, the set T_(n,H) of sums sum_(j=0)^(n-1) a_j alpha^j with 0<=a_j<=H satisfies

    |T_(n,H)| <= (4Hn)^d exp((n-1)m).

**B. Simple-factor multiple.** For every integer H>8d exp(2m), there is a nonzero R=P Q in Z[t] with deg R<=2d-1, height(R)<=H, Q(alpha)!=0 and

    ||R||_1, ||R||_(circle,infinity) <= 2dH.

In particular, when 0<m<=1/32, H=16d gives height(R)<=16d and ||R||_1<=32d^2.
This does not assert a monic, height-one or bounded-support R.

**C. Derivative comparison.** If a nonzero height-one integer relation R_0 of degree D has P multiplicity r>=1, its (r-1)-st derivative divided by (r-1)! is an integer simple-P multiple.
Its coefficient l1 norm is at most binom(D+1,r), with r<=floor(D/d).
Here differentiation, not an ordinary polynomial power, is meant.

This is a registered complete local candidate, pending an acceptance review.
The later actual-defect formulas (6)--(9), their precise Salem/window hypotheses, and the three missing propagation/cost transfers are retained below as unadopted follow-up material; they are not additional assertions of this Claim.
No finite enumeration, favorable new transition-product budget or near-one gap is asserted.

## Argument

Parts A--C select only the complete section [simple-factor construction](#simple-factor-annihilator-candidate), equations (1)--(5).
Its actual grid argument, strict pigeonhole inequality, degree guard and derivative integrality are retained in full.
The later residue, finite-cut and missing-transfer sections remain candidate research context at their original self-check scope; no acceptance finding is selected for them or for A--C.

## Organization and retained complete draft

The full original D G0005 body follows, preserving all formulas, titles, open questions, source screens, contribution disclosures and historical reviews.
Only heading depth and relocated links change.
Historical descriptions as a working draft, unadopted result or pending fixed review refer to the original date; the Current assessment above owns the present judgment.
Fixing this record does not reopen exploration.
Necessary programs/data remain in their existing J groups.
The old D can be removed only after full-body preservation and consumer repair checks.

### Simple-factor annihilators and the missing finite-window transfer

Date: 2026-10-09.
Unadopted working draft by the assigned entropy_status AI for Yin.
The coordinator requested a bounded check of whether changing the integral annihilator can avoid the retained L149 full-defect-budget cost.
The construction and calculations below are self-checked only; there is no complete independent proof-review claim, mathematical adoption, numerical run, new source, or assertion of novelty.
The coordinator retains this unbound work as a rolling D draft for [G0001](../tasks/Yin_T_G0001_v1.md#contract) and [S G0005](../strategies/Yin_S_G0005.md#bounded-next-test).
The bounded attempt supplied no useful cost transfer; it is not an active proof input or a new fixed mathematical result.
Full review is required before any later mathematical adoption.

The reused interfaces are [L91's norm-grid argument](../ledger/Yin_L_G0091_v1.md#norm-grid-support-bound), [L107's trace-defect residue](../ledger/Yin_L_G0107_v1.md#rounded-defect-residue-class), [L116's central scattering identity](../ledger/Yin_L_G0116_v1.md#unit-circle-scattering-coefficients), and the actual rounded trace and tails in [L125](../ledger/Yin_L_G0125_v1.md#central-small-transition-collapse).
L107 itself has a hyperbolic domain; its central extension used below is justified separately through L116, rather than silently enlarging L107.

<a id="simple-factor-annihilator-candidate"></a>
#### A simple-factor multiple with explicit degree and coefficient costs

Let P be the monic irreducible minimal polynomial of a nonzero algebraic integer alpha, of degree d and logarithmic Mahler measure m.
For integers n,H>=1, form

    T_(n,H)={sum_(j=0)^(n-1) a_j alpha^j : 0<=a_j<=H, a_j integral}.

The exact same grid used in L91 gives

    |T_(n,H)| <= (4Hn)^d exp((n-1)m).                 (1)

Indeed center the digit box at H/2 at each coefficient.
At an embedding of modulus rho the resulting sums lie in a disc or interval of radius (Hn/2) max(1,rho)^(n-1).
A real coordinate meets at most 3Hn max(1,rho)^(n-1) of the unit intervals.
A complex coordinate meets at most [4Hn max(1,rho)^(n-1)]^2 of the square cells of side 1/sqrt(2).
The product is at most the right side of (1).
Two distinct embedded algebraic integers cannot share a cell: all real conjugate differences then have modulus less than one and all complex differences have modulus less than one, contradicting the nonzero integral norm.
This argument counts complex conjugate pairs with their usual multiplicity two and does not assume the power order is maximal.

Choose n=2d and an integer

    H > 8d exp(2m).                                   (2)

Then (H+1)^2>8dH exp(2m), so (H+1)^(2d) is strictly greater than (8dH)^d exp((2d-1)m).
By (1), two distinct digit words coincide.
Their difference is a nonzero R in Z[t] with

    P | R,   deg R<=2d-1,   height(R)<=H,
    ||R||_1<=2dH,   ||R||_(circle,infinity)<=2dH.       (3)

Because deg(P^2)=2d, P^2 does not divide R.
Monic polynomial division therefore gives R=P Q with Q in Z[t] and Q(alpha)!=0.
No assertion makes R monic or its constant coefficient nonzero.
Removing an initial power of t, if desired, preserves the costs and simple P factor because alpha is nonzero.

In the near-one interval 0<m<=1/32, the explicit integer H=16d satisfies (2), since exp(2m)<=exp(1/16)<2.
Thus

    deg R<2d,   height(R)<=16d,   ||R||_1<=32d^2.      (4)

This is an existence statement with a finite enumeration prescription; no enumeration has been performed.
It supplies a simple P factor at polynomial degree/coefficient cost, but it does not supply a height-one or bounded-support multiple.

The height-one multiple in L91 has degree O(d log d) on this measure range, but that record does not ensure multiplicity one at P.
Choosing a relation of least degree within the height-one class does not itself justify differentiating inside that class.
If such a relation R_0 has degree D and P multiplicity r, then

    R=R_0^(r-1)/(r-1)!

is an integral simple-P multiple.
The direct coefficient estimate is

    sum_(i=r-1)^D binom(i,r-1)=binom(D+1,r),
    r<=floor(D/d).                                    (5)

Its leading coefficient need not be one.
Formula (4) avoids the possible superpolynomial coefficient cost of this derivative estimate; it is not claimed smaller for every individual R_0 and r.
Neither argument proves that a cheap squarefree-at-P height-one relation always exists, or that one cannot exist.

#### What actual trace defects retain, and what they do not yet transfer

For the actual rounded error e of L125, its finite integer forcing z_P=P(S)e is supported in [-J-d,J].
Under the Laurent convention

    Z_P(t)=sum_j (z_P)_j t^(-j-1),

the exact residue is

    Z_P(alpha)=2P'(alpha)theta !=0.                   (6)

To justify (6) on the central branch, the negative tail of e has zero central coefficient and its positive tail has coefficients 2 sigma_beta(theta).
L116 identifies their difference with Z_P(beta)/P'(beta).
Equality at any central embedding is equality of the corresponding field elements and proves (6).
This uses the actual integral multiplier theta and finite actual forcing; it does not claim a converse cube construction from a prescribed residue.

For any R=P Q with Q(alpha)!=0, let D=deg R.
Then

    z_R=R(S)e=Q(S)z_P,
    supp(z_R) subset [-J-D,J],
    Z_R(alpha)=Q(alpha)Z_P(alpha)!=0.                  (7)

The Laurent identity follows by shifting each summation index: the transform of S^i z is t^i Z(t).
Thus any partition of the finite support of z_R into polynomial clusters must contain at least one cluster whose Laurent polynomial is not P-divisible.
If every cluster were P-divisible, their sum Z_R would be P-divisible, contradicting (7).
This is a global residue observation, not an every-cluster assertion.

There is a finite actual-energy budget for this forcing, despite e not being square summable on the central branch.
For precision retain the Salem specialization of L129/L132 with r=exp(-m),

    delta^2=m(1-r^2)/256,
    max_central |sigma(theta)|<=sqrt(m)/(16q sqrt(N)),

and suppose its actual transition product is at least c in (0,1).
Set

    B_c=-2 log(c)/pi^2 + m r^2/(32d^2).

Subtract the central positive tail from e as in L125/L132: h=e-2w 1_(j>J).
The core cosine bound and the two geometric tails give ||h||_2^2<=B_c.
On the finite input interval [-J-D,J+D] required for the defects in (7), the difference e-h is supported on only D positive tail coordinates and has norm at most sqrt(Dm/(64N)).
Zero-extend e from this finite interval and apply finite convolution/Plancherel.
All defect coordinates in (7) are unchanged.
Consequently

    ||z_R||_1 <= ||z_R||_2^2
       <= ||R||_(circle,infinity)^2
              [sqrt(B_c)+sqrt(Dm/(64N))]^2.           (8)

The first inequality uses integrality of z_R.
Thus (4) supplies the explicit integer budget given by the floor of

    1024 d^4 [sqrt(B_c)+sqrt((2d-1)m/(64N))]^2.        (9)

The finite-cut term in (8) cannot be dropped by claiming e is in l2.
There is no J factor hidden in this estimate, but the degree and central tail term are real costs.
Formula (9) is an upper budget for a chosen annihilator, not a lower bound on the actual defect count.

<a id="annihilator-transfer-missing-obligations"></a>
#### Why this bounded test does not yet improve the near-one certificate

The simple-root guard is repairable by (4); it is not the remaining obstruction.
Three different unresolved transfers remain.

1. The guaranteed budget (9) has d^4 rather than a bounded or small degree cost.
   L149 only supplies a necessary lower bound of order B_c/m^2 for its old P budget; comparing a new upper bound with that old lower bound proves no improvement of the actual budgets.
   No near-one input coverage for a favorable comparison was established.

2. A zero z_R gap says Q(S)z_P=0 there, not z_P=0.
   A P-divisible z_R cluster need not yield a finite integer response for R(S).
   The local integer-response branch of L135/L141 therefore cannot be copied with P replaced by R.
   In particular the old every-cluster premise for L143 has not been proved for these new defects.

3. The global nonzero residue (7) ensures only that some cluster is nondivisible.
   Discarding divisible clusters, or tracking the surviving cluster through merges, requires its own finite propagation and boundary-cost proof.
   That proof is not supplied by (7), and no favorable actual-product lower bound follows from it.

Accordingly this round retains the proposed construction and the precise missing transfer as unadopted continuing mathematics only.
It does not retain another conditional cheap-annihilator theorem or declare the changed-annihilator route impossible.
A later attempt should first provide an actual smaller simple-P annihilator budget together with the missing global cluster propagation, or directly produce a finite product lower bound; it should not merely substitute (9) into the unchanged old radius formulas.