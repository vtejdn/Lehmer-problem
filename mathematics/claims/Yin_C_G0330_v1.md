---
author: Yin
---

# Height-free central transition collapse and the complete subexponential-height orbit budget

This retains the complete original [L125 mathematical argument](../ledger/Yin_L_G0125_v1.md), with its original 2026-10-07 precision and attribution.
The original assess_shortness_route agent supplied the complete compactness and actual-budget proof for Yin, building on the coordinator translated-defect mechanism.
No current Task/E execution, source acquisition or mathematical program run is selected by this maintenance.

## Statement

Fix a positive-Mahler algebraic unit alpha with monic irreducible P and q>0 central conjugates.
For every nonzero theta in O_K, call an integer J>=0 admissible when abs(u_(J+r))<=1/16 and abs(v_(-J-r))<=1/16 for every integer r>=1.
For every sequence of such multipliers with every central conjugate tending to zero, and every choice of admissible J, the exact bilateral mixed transition product C(theta,J) tends to zero.
Equivalently, for every c>0 there is a fixed-input delta(P,c)>0 that makes C<c whenever the central conjugates are at most delta and J is admissible.
This main theorem has no height restriction, no relation between J and height, and no effective modulus or rate.
The full proof retains the inverse-Vandermonde weak-tail estimate, the uniformly close globally l2-bounded proxy, the translated fixed nonzero integer defect, the Fatou limit and the exact c0 cube obstruction.
For multipliers indexed by word length N, the additional hypothesis log H_N=o(N), H_N=max_sigma abs(sigma(theta_N)), and the standard admissible J_N imply that the complete actual smoothed nonnegative-time mixed-trace g budget is o(N), with no lacunarity restriction.
The boundary times and exact real/disc exterior-noise costs are explicitly included.
The conclusion neither improves o(N) to O(log N), bounds full relative entropy, decides h_1=m, nor excludes other frequency/noise/height regimes or proves a uniform Mahler gap.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:26 |
| status | open |
| reason | Retain the complete exact original theorem and argument; actual current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(10): height-free all-admissible-window quantifiers, weak-tail Vandermonde, exact rounding/support, nonzero defect, uniformly close l2 proxy and translated Fatou contradiction, full actual t>=0 budget with its additional subexponential-height hypothesis and all limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(10): height-free all-admissible-window quantifiers, weak-tail Vandermonde, exact rounding/support, nonzero defect, uniformly close l2 proxy and translated Fatou contradiction, full actual t>=0 budget with its additional subexponential-height hypothesis and all limits. |
| dependency | [Exact retained input](Yin_C_G0316_v1.md#unit-circle-c0-integer-forcing) | Complete irreducible unit-circle c0/closed-cube integer-forcing rigidity, applied to the translated l2 limit. |
| dependency | [Exact retained input](Yin_C_G0317_v1.md#unit-circle-scattering-coefficients) | Complete bounded homogeneous classification, used to prove that the original rounded defect cannot vanish. |
| dependency | [Exact retained input](Yin_C_G0321_v1.md#finite-window-stable-central-smoothing) | Exact actual mixed sign law and uniform interval/disc smoothing. |
| dependency | [Exact retained input](Yin_C_G0327_v1.md#exact-noise-exterior-trace-decay) | Exact actual exterior noise bound, with its real and complex factors. |
| dependency | [Exact retained input](Yin_C_G0328_v1.md#mixed-trace-transition-product) | Exact standard transition product, admissible height window and true trace phase convention. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:31 |
| status | proved |
| reason | Adopt the complete exact original theorem and retained argument after actual whole self-review with resolved used inputs, retaining every height, actual-amplitude, source, finite-window and uniformity limitation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(10): height-free all-admissible-window quantifiers, weak-tail Vandermonde, exact rounding/support, nonzero defect, uniformly close l2 proxy and translated Fatou contradiction, full actual t>=0 budget with its additional subexponential-height hypothesis and all limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(10): height-free all-admissible-window quantifiers, weak-tail Vandermonde, exact rounding/support, nonzero defect, uniformly close l2 proxy and translated Fatou contradiction, full actual t>=0 budget with its additional subexponential-height hypothesis and all limits. |
| dependency | [Exact retained input](Yin_C_G0316_v1.md#unit-circle-c0-integer-forcing) | Complete irreducible unit-circle c0/closed-cube integer-forcing rigidity, applied to the translated l2 limit. |
| dependency | [Exact retained input](Yin_C_G0317_v1.md#unit-circle-scattering-coefficients) | Complete bounded homogeneous classification, used to prove that the original rounded defect cannot vanish. |
| dependency | [Exact retained input](Yin_C_G0321_v1.md#finite-window-stable-central-smoothing) | Exact actual mixed sign law and uniform interval/disc smoothing. |
| dependency | [Exact retained input](Yin_C_G0327_v1.md#exact-noise-exterior-trace-decay) | Exact actual exterior noise bound, with its real and complex factors. |
| dependency | [Exact retained input](Yin_C_G0328_v1.md#mixed-trace-transition-product) | Exact standard transition product, admissible height window and true trace phase convention. |
| review | [Actual current whole self-check](../audits/reviews/Yin_R_G0553_v1.md#current-transition-collapse-finding) | Exact current statement, complete retained proof and used interfaces; self-reviewed. Every old finding retains its actual original input and relationship. |

## Complete retained argument

<a id="argument"></a>
Fix an algebraic unit alpha with monic irreducible P, degree d, positive log Mahler measure, and q>0 central conjugates.
There are stable and expanding conjugates.
All trace sums count every embedding, including both members of a complex pair.
For theta in O_K minus {0}, write u_j, v_j, w_j for its stable, expanding and central weighted traces, respectively, as in [L G0123](Yin_C_G0328_v1.md#mixed-trace-transition-product).
Their sum is the integer Tr(theta alpha^j) for all j.

Put b=1/16.
Call an integer J>=0 admissible for theta if

    |u_(J+r)|<=b and |v_(-J-r)|<=b for every r>=1.     (1)

Such J exist.
In particular the standard L G0123 choice J=ceil(log(16dH)/(-log rho)), with H the largest conjugate modulus of theta and rho the largest hyperbolic contraction modulus, is admissible.
No height bound or prescribed growth rate of J is imposed in the main theorem.

<a id="central-small-transition-collapse"></a>
### The height-independent transition obstruction

Define exactly the L G0123 transition product

    C(theta,J)=product_(j=-J)^(-1)|cos(2pi v_j)|
                       product_(j=0)^J|cos(2pi(u_j+w_j))|.

For every sequence of nonzero integral multipliers theta_n whose central conjugates all tend to zero, and every choice of admissible J_n,

    C(theta_n,J_n) -> 0.                              (2)

Equivalently, for every c>0 there exists delta(P,c)>0 such that max_central|sigma(theta)|<=delta(P,c) and admissibility of J imply C(theta,J)<c.
The proof below establishes this uniform-in-J implication by contradiction; it supplies no explicit modulus delta or decay rate.

We first record why the weak tail condition (1), by itself, supplies uniform square-summable hyperbolic tails.
List the stable roots as lambda_1,...,lambda_s and let V_s=(lambda_i^r)_(0<=r<s,1<=i<=s).
This Vandermonde matrix is invertible.
Set

    B_s=sum_(i,r)|(V_s^(-1))_(i,r)|,
    rho_s=max_i|lambda_i|<1.

Apply its inverse to the first s values of u_(J+1),u_(J+2)....
The resulting exponential coefficients have total modulus at most b B_s.
Consequently |u_(J+r)|<=b B_s rho_s^(r-1) for every r>=1.
For the expanding tail use the distinct reciprocal roots lambda_i=beta_i^(-1), and define B_u and rho_u analogously.
The same argument gives |v_(-J-r)|<=b B_u rho_u^(r-1).
Thus the finite constant

    E_P=4b^2[B_s^2/(1-rho_s^2)+B_u^2/(1-rho_u^2)]    (3)

bounds four times the sum of the two squared tail traces, uniformly over all theta and J satisfying (1).
Root separation costs are retained in the two inverse matrices.

<a id="transition-defect-compactness"></a>
### A translated nonzero defect cannot disappear

Suppose (2) fails.
After passing to a subsequence choose 0<c<1 with C(theta_n,J_n)>=c.
Write epsilon_n=max_central|sigma(theta_n)|, so epsilon_n->0.
For each n and every j, let e_(n,j) be the nearest-integer error of 2(u_j+w_j).
All these coordinates are in the strict interval (-1/2,1/2): a tie would make the algebraic integer u_j+w_j a nonintegral rational with denominator four.
Set z_n=P(S)e_n, where (Se)_j=e_(j+1).
Since P(S)(u+w)=0, z_n is an integer sequence.

For all sufficiently large n, q epsilon_n<=b.
The trace identity and (1) then identify the tails without ambiguity:

    e_(n,j)=-2v_j,              j<-J_n,
    e_(n,j)=2u_j+2w_j,          j>J_n.                 (4)

Indeed the respective phases have moduli at most b and 2b, so doubling them stays strictly within the rounding interval.
On the core, the product is exactly product_(j=-J_n)^(J_n) cos(pi e_(n,j)).
Each factor is at least c, since all other factors are at most one.
The inequality -log cos(pi x)>=pi^2 x^2/2 therefore gives

    sum_(|j|<=J_n)e_(n,j)^2<=-2log(c)/pi^2,
    sup_j|e_(n,j)|<=s_c:=max(arccos(c)/pi,4b)<1/2.     (5)

Subtract only the small positive central tail and put

    h_(n,j)=e_(n,j)-2w_j 1_(j>J_n).

Its core is e_n and its two tails are -2v_j and 2u_j.
Equations (3)--(5) give the global estimates

    ||h_n||_2^2<=-2log(c)/pi^2+E_P=:E,
    ||e_n-h_n||_infinity<=2q epsilon_n ->0.             (6)

These estimates address the persistent central tail: e_n itself need not be in l2, but differs uniformly from an l2-bounded sequence by a quantity tending to zero.

The integer defect z_n has finite support, contained in [-J_n-d,J_n].
Outside that interval every term used by P(S) lies in one of the homogeneous tails (4).
Moreover z_n is nonzero.
If P(S)e_n=0, the bounded homogeneous classification of [L G0116](Yin_C_G0317_v1.md#unit-circle-scattering-coefficients) makes e_n a sum of center modes only.
Its negative tail tends to zero, so the Vandermonde argument forces all those modes to vanish.
Then e_n=0, and (4) makes v_j eventually zero at negative infinity.
Applying a Vandermonde matrix to the reciprocal expanding roots forces every expanding coefficient sigma(theta_n) to vanish.
This contradicts theta_n!=0 and the injectivity of field embeddings.

Choose an index k_n with (z_n)_(k_n)!=0, and translate e_n and h_n by that same index.
Every defect entry is bounded by ||P||_1 s_c.
Passing to a subsequence first makes the defect at the new origin one fixed nonzero integer.
A diagonal subsequence of the translated e_n, whose coordinates lie in [-s_c,s_c], converges at every integer coordinate to e_infinity.
By (6), the translated h_n have the same pointwise limit.
Fatou's inequality on every finite interval, followed by increasing those intervals, gives ||e_infinity||_2^2<=E.

Finite-coordinate continuity of P(S) shows that P(S)e_infinity is integer-valued everywhere and has the fixed nonzero defect at the origin.
Also ||e_infinity||_infinity<=s_c<1/2.
This contradicts [L G0115](Yin_C_G0316_v1.md#unit-circle-c0-integer-forcing), which permits only zero for such a decaying cube response.
The contradiction proves (2).

No spatial tightness of the energy or bound on k_n was assumed.
Defects at the edge of the transition or drifting to infinity are covered by the same translation and global l2 bound.
This is also why no comparison between J_n and multiplier height is needed in the main theorem.

<a id="subexponential-height-mixed-budget-collapse"></a>
### The complete actual orbit budget for subexponential height

There is a direct consequence for the actual Fourier amplitudes, stronger than merely weakening a lower amplitude estimate.
Now index the multipliers by the sign-word length N, assume their central conjugates tend to zero, and impose the additional hypothesis

    log H_N=o(N),
    H_N=max_sigma|sigma(theta_N)|>=1.                 (7)

Choose the standard L G0123 admissible J_N from (1).
It has J_N=O_P(1+log H_N)=o(N).
Put C_N=C(theta_N,J_N).
For every t whose Fourier window [-t,N-1-t] contains [-J_N,J_N], the product identity of L G0123 shows that the actual unsmoothed amplitude is at most C_N: all the additional factors have modulus at most one.
Smoothing cannot increase it.
Among 0<=t<=N there are at most 2J_N+1 other times, including cases in which the core does not fit.
Hence, using the same g as L G0120 and g<=log2,

    sum_(t=0)^N g(|hat f_N(zeta_(theta_N,t)^(sc))|)
       <=N g(C_N)+(2J_N+1)log2.                        (8)

The exterior times must also be accounted for.
Select one fixed stable place beta_* and write rho_*=|beta_*|.
The exact L G0122 interval/disc noise estimate gives |hat f_N(zeta_(theta_N,N+r)^(sc))| <=min(1,D_N rho_*^r), r>=1, where

    D_N=K_*/|sigma_*(theta_N)|,
    K_*=1/(2pi a) for a real selected place,
    K_*=1/(pi^2 a) for a complex selected place.

The notation K_* here is only this fixed noise constant.
Integer norm gives |sigma_*(theta_N)|>=H_N^(-(d-1)), so D_N<=K_*H_N^(d-1).
Define the nonnegative integer R_N=ceil(log_+(D_N)/(-log rho_*)).
Since g(x)<=(log2)x^2, splitting at R_N yields

    sum_(t>N)g(|hat f_N(zeta_(theta_N,t)^(sc))|)
       <=(log2)[R_N+rho_*^2/(1-rho_*^2)],
    R_N=O_P(1+log H_N).                                (9)

For the remaining geometric tail use D_N rho_*^(R_N)<=1; the formula also holds if D_N<=1 and R_N=0.
Thus (2), (7)--(9) prove the full statement

    sum_(t>=0)g(|hat f_N(zeta_(theta_N,t)^(sc))|)=o(N). (10)

No lacunarity restriction is required for this upper bound.
Any selection of that orbit satisfying the L G0120 frequency conditions has no larger budget.
In particular (7) includes every polynomial-height family constructed in L G0123.
The conclusion concerns the actual smoothed amplitudes, not only the particular lower envelope b_N used there.

### Scope and limits

The main transition theorem is uniform over admissible windows and needs no height assumption.
The complete orbit-budget consequence (10) explicitly needs (7) to control the number of boundary times and the exterior noise cost.
Without that assumption, (2) still holds, but (10) has not been proved here.

This excludes a positive linear asymptotic budget from this particular central-small, subexponential-height mixed trace family.
It does not decide whether h_1=m, does not upper-bound the full relative entropy, and does not render finite arithmetic consistency tests useless.
No effective rate for C_N->0 is provided; in particular no conclusion upgrades o(N) to O(log N).
Different frequency families, unrestricted center corrections, changed smoothing, and superexponential or exponential height regimes remain outside (10).
No uniform Mahler gap is asserted.
