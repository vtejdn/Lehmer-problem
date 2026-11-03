---
author: Yin
---

# Actual scalar window-flattening cost and the precise Dirichlet certificate failure

This retains the complete original2026-10-07 [L112 proof](../ledger/Yin_L_G0112_v1.md),authored by assess_shortness_route for Yin.
The exact old complete checks and ambiguous coordinator test attribution remain at their sufficient [R33 home](../audits/reviews/Yin_R_G0033_v1.md#contribution-and-review).
No source,computation or Task is newly executed.

## Statement

Let alpha be a hyperbolic algebraic unit of degree d,with monic irreducible P and m=log M(P)>0.
Fix theta in O_K minus{0},H=max_sigma abs(sigma(theta))>=1,and
sigma0=max(max_stable abs(beta),max_expanding abs(beta)^(-1))<1.
Let e_j(n) be the exact nearest-integer error of2n u_j(theta) for a positive integer n.
For any nonzero integer multiple R of P,put A_R=sum abs(R_i),Q_R=max_T abs(R).
The actual defect premises give sup abs(e)>=1/A_R and sum e²>=2/Q_R².

For every integer J>=0,the complete stable/expanding tail count proves

    sum_(abs(j)>J)e_j(n)²
       <=4n²H²d² sigma0^(2J+2)/(1-sigma0²).

Consequently,if E_J(n)=sum_(abs(j)<=J)e_j(n)²<=delta<2/Q_R²,then

    n>=sigma0^(-J-1)/(2Hd)
       sqrt((2/Q_R²-delta)(1-sigma0²)).

If every central abs(e_j(n))<1/A_R,then n>=sigma0^(-J-1)/(2A_R H d).
These are lower costs of genuine successful windows,not whole-product bounds.

For an integer Q>=3 and L=2J+1,simultaneous half-open pigeonholing supplies an actual
1<=n<=Q^L with every central abs(e_j(n))<1/Q.
If that actual n also satisfies2nHd sigma0^(J+1)<=1/(2pi),then

    c_P(n theta)>=cos(pi/Q)^L
       exp(-4pi²n²H²d² sigma0^(2J+2)/(1-sigma0²)).

The bare worst-case substitution n=Q^(2J+1) has tail quantity
2Hd Q sigma0 (Q²sigma0)^J.
When M(P)<2,unit norm gives sigma0>=exp(-m)>1/2.
Thus this worst-case quantity is greater than2 for every J>=0,even allowing Q=2,and never certifies the required threshold.
This is failure of the stated guarantee,not failure of every good actual multiplier or better recurrence-aware method.

Keeping this particular central lower certificate above exp(-K),with fixed K>0,requires Q>=pi sqrt(L/(2K)).
Its available bound Q^L then has logarithm at least(L/2)log L+O_K(L).
This is a cost of that certificate,not a lower bound on every actual approximation.
No optimizer,full-product amplitude floor,uniform entropy gap or small-Mahler counterfamily is proved.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:41 |
| status | open |
| reason | Complete original exact scalar window/tail costs, simultaneous-box full-product certificate and worst-case small-Mahler failure proof retained; current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire actual integral scalar-multiplier window energy/sup costs, exact Dirichlet central/full-product certificate, every-J worst-case failure in M<2 and central certificate growth cost,with all actual-versus-guaranteed and optimized-amplitude limits. |
| argument | [Complete argument](#argument) | Full original1–8: both candidate integer tails and separate multiplicities/factor4, genuine multiplier lower costs, strict half-open pigeonhole, log-cosine full tail, stable unit-norm sigma guard and precise worst-case/central-product distinctions. |
| dependency | [Actual integral recurrence sup cap](Yin_C_G0298_v1.md#uniform-multiplier-recurrence-cap) | Exact some rounded error at least1/A_R for every nonzero integral multiplier and annihilating multiple; no cap for arbitrary real recurrence data. |
| dependency | [Energy-two defect floor](Yin_C_G0304_v1.md#two-unit-defect-energy-floor) | Exact sum e²>=2/Q_R² for every integer multiple,including extra unit-circle factors in R. |
| support | [Actual amplitude budget](Yin_C_G0306_v1.md#optimizing-convolution-fourier-tests) | Only the separate full-product target motivating the boundary; central window flattening and its failed worst-case certificate do not settle it. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:44 |
| status | proved |
| reason | Adopt the complete original true window-flattening multiplier lower costs and exact Dirichlet full-product certificate/failure theorem after whole self-review,retaining every actual-versus-worst-case and optimized-amplitude limitation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire actual integral scalar-multiplier window energy/sup costs, exact Dirichlet central/full-product certificate, every-J worst-case failure in M<2 and central certificate growth cost,with all actual-versus-guaranteed and optimized-amplitude limits. |
| argument | [Argument](#argument) | Full original1–8: both candidate integer tails and separate multiplicities/factor4, genuine multiplier lower costs, strict half-open pigeonhole, log-cosine full tail, stable unit-norm sigma guard and precise worst-case/central-product distinctions. |
| dependency | [Dependency](Yin_C_G0298_v1.md#uniform-multiplier-recurrence-cap) | Exact some rounded error at least1/A_R for every nonzero integral multiplier and annihilating multiple; no cap for arbitrary real recurrence data. |
| dependency | [Dependency](Yin_C_G0304_v1.md#two-unit-defect-energy-floor) | Exact sum e²>=2/Q_R² for every integer multiple,including extra unit-circle factors in R. |
| support | [Support](Yin_C_G0306_v1.md#optimizing-convolution-fourier-tests) | Only the separate full-product target motivating the boundary; central window flattening and its failed worst-case certificate do not settle it. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0546_v1.md#current-window-cost-finding) | Exact current full statement,complete retained original proof and all selected interfaces,self-reviewed; historical findings retain their actual old inputs and precise partial/contributor/whole relationships. |

## Complete retained argument

<a id="argument"></a>
Let alpha be a hyperbolic algebraic unit of degree d, m=log M(P)>0, and fix theta in O_K minus {0}.
Put

    H=max_sigma |sigma(theta)|>=1,
    sigma_0=max(max_stable |beta|, max_expanding |beta|^(-1))<1.

Let s be the number of stable embeddings, counting each complex pair twice, so the expanding count is d-s.
Use the stable and expanding traces u_j(theta),v_j(theta) and the nearest-integer errors of the multiplier n theta, for a positive integer n:

    e_j(n)=2n u_j(theta)-nearest_integer(2n u_j(theta)).

There are no ties for integral multipliers.
The exact Fourier amplitude is product_(j in Z) cos(pi e_j(n)).
For every nonzero R in Z[t] divisible by P, write

    A_R=sum_i |R_i|,  Q_R=max_(|z|=1)|R(z)|.

The retained integer-defect results give

    sup_j |e_j(n)|>=1/A_R,
    sum_j e_j(n)^2>=2/Q_R^2.                            (1)

The second uses the energy-two refinement of L G0107.
These are arithmetic restrictions on actual multipliers, not guarantees about an arbitrary real recurrence.

<a id="finite-trace-window-tail-cost"></a>
### A genuine lower cost for a flat window

For j>=1, distance to an integer is bounded by the distance to the candidate integer zero.
For j<=-1 use the candidate 2n Tr(theta alpha^j).
Thus

    |e_j(n)|<=2nHs sigma_0^j               (j>=1),
    |e_(-j)(n)|<=2nH(d-s) sigma_0^j        (j>=1).

For an integer J>=0 put E_J(n)=sum_(|j|<=J)e_j(n)^2.
The two tail counts are retained separately, giving

    sum_(|j|>J)e_j(n)^2
       <=4n^2 H^2 [s^2+(d-s)^2]
                      sigma_0^(2J+2)/(1-sigma_0^2)
       <=4n^2 H^2 d^2 sigma_0^(2J+2)/(1-sigma_0^2).     (2)

This explains the factor four: bounding each tail separately by d before adding would instead give eight.
Combining (1)--(2), whenever E_J(n)<=delta<2/Q_R^2,

    n >= sigma_0^(-J-1)/(2Hd)
             *sqrt[(2/Q_R^2-delta)(1-sigma_0^2)].        (3)

There is a parallel sup-norm statement.
If every error in |j|<=J is strictly less than 1/A_R, the error required by the first part of (1) occurs outside the window.
The pointwise tail bound therefore forces

    n>=sigma_0^(-J-1)/(2A_R H d).                       (4)

These lower bounds on n concern true successful window approximations.
For fixed P,theta,R and a fixed energy margin delta<2/Q_R^2, flattening longer windows requires exponential multiplier growth.
They do not themselves upper-bound or lower-bound the full Fourier product: the nonzero rounded defect has been forced into the tail, not removed.

<a id="dirichlet-window-certificate"></a>
### What the usual simultaneous box estimate actually certifies

Let Q>=3 be an integer and L=2J+1.
Pigeonholing the Q^L+1 torus points formed by the first Q^L+1 multiples of the vector (2u_j(theta))_(|j|<=J) into Q^L half-open boxes gives some positive integer n with

    n<=Q^L,       |e_j(n)|<1/Q for every |j|<=J.         (5)

Consequently the central product is at least cos(pi/Q)^L.
To turn this into a certificate for the whole bilateral product, a sufficient tail condition is

    2nHd sigma_0^(J+1)<=1/(2pi).                       (6)

Indeed all tail arguments pi e_j then have absolute value at most 1/2.
On that interval log cos x>=-x^2, as follows by integrating tan x<=2x.
Equations (2), (5) and (6) therefore give the fully quantified bound

    c_P(n theta)>=cos(pi/Q)^L
       *exp[-4pi^2 n^2 H^2 d^2
                         sigma_0^(2J+2)/(1-sigma_0^2)]. (7)

One can test (6) for the actual n found.
The bare Dirichlet guarantee replaces n by Q^(2J+1), and its tail-control quantity is then

    2Hd Q sigma_0 (Q^2 sigma_0)^J.                     (8)

For fixed Q it decays with J only if Q^2 sigma_0<1.
This condition is unavailable in the target range M(P)<2.
In fact the product of all stable moduli, counting embeddings, is exp(-m).
Each stable modulus is at least that product.
Hence sigma_0>=exp(-m)>1/2, so Q^2 sigma_0>1 for every Q>=2.
More strongly, even allowing Q=2 in (8), its value is greater than 2 for every J>=0, since H>=1 and d>=1.
Thus this worst-case replacement never certifies the threshold 1/(2pi) in (6) anywhere in the stated small-Mahler domain.

This is a precise failure of the displayed worst-case estimate, not a theorem that a good actual n does not exist.
The actual n can be much smaller than Q^L.
Nor does the argument claim that all better uses of the algebraic recurrence, smaller-dimensional targets, or non-scalar multipliers suffer this same cost.

There is a second cost if this particular central product bound is to remain above a fixed exp(-K), with K>0 independent of J.
Since

    -log cos(pi/Q)>=pi^2/(2Q^2),

the certificate cos(pi/Q)^L>=exp(-K) itself requires Q>=pi sqrt[L/(2K)].
The available bound Q^L for n then has logarithm at least (L/2)log L+O_K(L).
Again this is a cost of that certificate, not a lower bound on every actual simultaneous approximation.

<a id="amplitude-optimization-boundary"></a>
### Consequence for the optimized amplitude

The arithmetic bounds (3)--(4) and the certificate failure (8) are different conclusions.
The former force genuine multiplier growth when a fixed central window becomes sufficiently flat.
The latter explains why simply combining a simultaneous Dirichlet box with exponential trace tails does not furnish an amplitude floor in the near-one branch.

Neither proves that c_opt is attained.
Neither rules out useful optimization by actual multipliers, nor replaces the positive input-dependent construction being pursued through the exact Green-defect residue class.
Any improvement intended to contradict the L G0109 amplitude budget must control the complete product, rather than its arbitrarily long central segments alone.
No new uniform entropy gap or small-Mahler counterfamily is claimed.
