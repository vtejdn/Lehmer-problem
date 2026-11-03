---
author: Yin
---

# The multiplier cost of flattening a finite trace window

The current complete mathematical proof is retained in [C309](../claims/Yin_C_G0309_v1.md#argument).
The original mathematical text below remains the fixed old input,with its original date and exact old review bindings.

Date: 2026-10-07.
Bounded direct proof by the assigned assess_shortness_route AI for Yin.
The coordinator checked the proposed energy normalization and requested comparison with the complete Dirichlet window/tail certificate.
The integer-defect premises are those of L G0103 and L G0107.
No computation, new source, or novelty claim is involved.

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
## A genuine lower cost for a flat window

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
## What the usual simultaneous box estimate actually certifies

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
## Consequence for the optimized amplitude

The arithmetic bounds (3)--(4) and the certificate failure (8) are different conclusions.
The former force genuine multiplier growth when a fixed central window becomes sufficiently flat.
The latter explains why simply combining a simultaneous Dirichlet box with exponential trace tails does not furnish an amplitude floor in the near-one branch.

Neither proves that c_opt is attained.
Neither rules out useful optimization by actual multipliers, nor replaces the positive input-dependent construction being pursued through the exact Green-defect residue class.
Any improvement intended to contradict the L G0109 amplitude budget must control the complete product, rather than its arbitrarily long central segments alone.
No new uniform entropy gap or small-Mahler counterfamily is claimed.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0033_v1.md#contribution-and-review), with its original inspected scope and relationship.
