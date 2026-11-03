---
author: Yin
---

# Exact central boundary flux, shared collars and retained endpoint obstruction

The complete mathematical input is the original 2026-10-08 [L141 argument](../ledger/Yin_L_G0141_v1.md).
Its necessary fixed historical input and the actual old checking arrangements remain preserved.

## Statement

For every monic irreducible integer polynomial P of degree d with constant coefficient plus or minus one, positive logarithmic Mahler measure m and q>0 unit-circle roots, retain every conjugate and the exact finite energy E_R on the closed cube over {-R,...,R+d}, with integer defects P(S)x_j for -R<=j<=R and nonzero origin defect.
An empty feasible set has E_R=+infinity.
The quotient coefficient rows P(t)/(t-beta), their geometric-mean and joint-matrix constant Phi, and the grouped inverse-Vandermonde endpoint constant Psi are exactly those defined in (1)--(7) and (11) below.
For every rational B>0, the shared disjoint collar blocks give (5)--(8), the coefficient bound (9) and the strict improved collar (13); K=floor(W^2 B) iterations give E_R>B for every integer R>=s_K, while K=0 excludes every R immediately.
For the literal family P_N=t^(N+3)-t^(N+1)-t^N+1-t^2-t^3 with N>=9 and N=9 modulo120, Phi<=9d-42 whereas the old scalar C_1^2=9d^2.
In the hypothetical Salem domain 0<m<=1/32, q=d-2>=2 and B>=-2log(16m)/pi^2+m exp(-2m)/(32d^2), with the explicit B>2/15 and K>=1 guards, the retained l1 inverse-row endpoint method has lambda d(4B Psi^2)>1 and cannot enter its sufficient Euler regime.
That obstruction is not a tower lower bound for the new recursion, a necessary true-window bound, an optimized energy value, uniform near-one coverage or a resolution of G0001.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T12:03 |
| status | open |
| reason | Retain the entire original theorem and argument in its current responsible home; actual full review and adoption are recorded separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(17), exact bilinear flux normalization and finite cuts, shared two-collar budget, simultaneous geometric/matrix bounds, coefficient and actual-family control, grouped endpoint propagation, strict finite-cluster coercivity and every endpoint-obstruction and uniformity limit. |
| argument | [Complete argument](#argument) | Entire original (1)--(17), exact bilinear flux normalization and finite cuts, shared two-collar budget, simultaneous geometric/matrix bounds, coefficient and actual-family control, grouped endpoint propagation, strict finite-cluster coercivity and every endpoint-obstruction and uniformity limit. |
| dependency | [Exact finite cube](Yin_C_G0335_v1.md#finite-rational-energy-coercivity) | Exact closed cube, integer defects, nonzero origin and strict compact minimum, with every finite index retained. |
| dependency | [Complete finite-cluster response](Yin_C_G0341_v1.md#explicit-finite-energy-coercivity-radius) | Both collar cuts, monic integral division, quotient support, homogeneous propagation, final K-step closure and low-degree cases. |
| dependency | [All-central coefficient budget](Yin_C_G0344_v1.md#all-central-coercivity-radius) | Capped integer mass and actual all-central norm/iteration, without transferring its separate tower lower bound to this new recursion. |
| dependency | [Actual Salem family](Yin_C_G0336_v1.md#linear-exponent-cyclic-coverage) | The literal six-coefficient irreducible progression and central-root domain only; no new source or root computation. |
| dependency | [Exact target energy](Yin_C_G0337_v1.md#tunable-salem-finite-energy-envelope) | The actual B_m in the hypothetical small-measure Salem domain and its retained input scope, without a product lower bound. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T12:07 |
| status | proved |
| reason | Adopt the actual complete written-proof self finding for the retained exact finite-domain theorem, shared collar and coefficient improvements and endpoint-method limitation. Keep original contributor and shared-context checks at their historical scopes; this is neither isolated independent review nor a new energy computation or Task resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(17), exact bilinear flux normalization and finite cuts, shared two-collar budget, simultaneous geometric/matrix bounds, coefficient and actual-family control, grouped endpoint propagation, strict finite-cluster coercivity and every endpoint-obstruction and uniformity limit. |
| argument | [Complete argument](#argument) | Entire original (1)--(17), exact bilinear flux normalization and finite cuts, shared two-collar budget, simultaneous geometric/matrix bounds, coefficient and actual-family control, grouped endpoint propagation, strict finite-cluster coercivity and every endpoint-obstruction and uniformity limit. |
| dependency | [Exact finite cube](Yin_C_G0335_v1.md#finite-rational-energy-coercivity) | Exact closed cube, integer defects, nonzero origin and strict compact minimum, with every finite index retained. |
| dependency | [Complete finite-cluster response](Yin_C_G0341_v1.md#explicit-finite-energy-coercivity-radius) | Both collar cuts, monic integral division, quotient support, homogeneous propagation, final K-step closure and low-degree cases. |
| dependency | [All-central coefficient budget](Yin_C_G0344_v1.md#all-central-coercivity-radius) | Capped integer mass and actual all-central norm/iteration, without transferring its separate tower lower bound to this new recursion. |
| dependency | [Actual Salem family](Yin_C_G0336_v1.md#linear-exponent-cyclic-coverage) | The literal six-coefficient irreducible progression and central-root domain only; no new source or root computation. |
| dependency | [Exact target energy](Yin_C_G0337_v1.md#tunable-salem-finite-energy-envelope) | The actual B_m in the hypothetical small-measure Salem domain and its retained input scope, without a product lower bound. |
| review | [Complete current self finding](../audits/reviews/Yin_R_G0567_v1.md#central-flux-whole-current-finding) | Entire original (1)--(17), exact bilinear flux normalization and finite cuts, shared two-collar budget, simultaneous geometric/matrix bounds, coefficient and actual-family control, grouped endpoint propagation, strict finite-cluster coercivity and every endpoint-obstruction and uniformity limit. Actual whole relationship is self-reviewed, including the finite indices, K=0/strict final collar, coefficient count and two-case endpoint obstruction. |

## Complete retained argument

<a id="argument"></a>
<a id="exact-central-boundary-flux"></a>
### Domain and exact flux normalization

Use the monic irreducible positive-log-Mahler unit domain of [L G0130](Yin_C_G0335_v1.md#finite-rational-energy-coercivity), [L G0135](Yin_C_G0341_v1.md#explicit-finite-energy-coercivity-radius) and [L G0138](Yin_C_G0344_v1.md#all-central-coercivity-radius).
Write

    P(t)=sum_(i=0)^d p_i t^i,  p_d=1,  p_0 in {1,-1},
    m=log M(P)>0,  q=#unit-circle roots>0,  h=d-q,
    W=sum_i|p_i|,  Z=floor(W/2),  C_1=sum_i i|p_i|.

All conjugates are counted, including both members of complex pairs.
The roots are distinct and nonzero.
For R>=0, E_R is exactly the minimum energy of x in the closed cube on {-R,...,R+d}, with integer z_j=P(S)x_j for -R<=j<=R and z_0!=0, as in the fixed records.

For each central root beta define the polynomial and its coefficient row

    Q_beta(t)=P(t)/(t-beta)=sum_(k=0)^(d-1) q_(beta,k)t^k,
    q_beta=(q_(beta,0)...,q_(beta,d-1)),
    F_beta=||q_beta||_2.

Synthetic division gives the exact coefficients

    q_(beta,k)=sum_(i=k+1)^d p_i beta^(i-k-1).              (1)

For the state X_j=(x_j,...,x_(j+d-1)), multiplication of the polynomial identity (t-beta)Q_beta=P gives

    q_beta X_(j+1)=beta q_beta X_j+z_j.                   (2)

The row acts by the ordinary bilinear coefficient pairing, without complex conjugating its entries.
Its Euclidean norm still supplies the usual absolute-value Cauchy bound.
With V=(beta_i^k)_(0<=k<d,1<=i<=d), it also satisfies

    q_beta=P'(beta) (row_beta V^(-1)).                    (3)

Indeed q_beta applied to the V column of beta_i is Q_beta(beta_i), equal to zero at every other root and P'(beta) at beta.
Thus (2) has forcing coefficient one; a further division by P'(beta) would change the normalization.

Suppose a defect cluster [a,b], containing zero, has zero-defect collars extending to left and right state cuts l and r, where l<=a-d and r>=b+1.
Define

    Z_c(t)=sum_(j=a)^b z_j t^(b-j).

Summing (2) with the appropriate powers gives the exact identity

    beta^(-b-1) Z_c(beta)
      =beta^(-r) q_beta X_r-beta^(-l) q_beta X_l.          (4)

Every power multiplying a flux in (4) has modulus one.
This is the same boundary identity as L G0135 with its actual coefficient row retained, rather than bounded term by term by C_1.

### Two collar blocks share one energy budget

Fix a rational B>0 and assume a feasible x has energy at most B.
Let both empty collars have length dT inside [-R,R], for an integer T>=1.
Use exactly the T disjoint left blocks [a-jd,a-(j-1)d-1] and right blocks [b+1+(j-1)d,b+jd], 1<=j<=T.
Their two total energies B_L,B_R obey B_L+B_R<=B because the collars are disjoint.

Choose a minimum-energy block on each side.
Their starts l and r then satisfy all the finite-index conditions above, and jointly

    ||X_l||_2^2+||X_r||_2^2 <= (B_L+B_R)/T <=B/T.         (5)

This is stronger than charging B separately to both ends.
For each central beta, (4)--(5) give

    |Z_c(beta)|<=F_beta(||X_l||_2+||X_r||_2)
                  <=F_beta sqrt(2B/T).                  (6)

Define two positive real algebraic constants.
Let B_c be the q by d matrix with rows q_beta over all central roots, let ||B_c||_op be its Euclidean operator norm, and put

    F_geo^2=(product_central F_beta^2)^(1/q),
    F_mat^2=||B_c||_op^2/q,
    Phi=min(F_geo^2,F_mat^2).                            (7)

The superscript in F_geo^2 and F_mat^2 denotes the nonnegative squared-norm scale specified by these formulas.
These constants are effectively computable by algebraic root arithmetic and Hermitian eigenvalue isolation, or usable through certified rational upper bounds.
No such computation is executed here.

Multiplying (6) yields the product bound with F_geo.
Independently, the vector of all central Z_c values, up to unit diagonal factors, is a difference of two matrices B_c applied to X_l and X_r.
Hence

    sum_central |Z_c(beta)|^2
       <=2||B_c||_op^2 (||X_l||_2^2+||X_r||_2^2)
       <=2||B_c||_op^2 B/T.

Arithmetic-geometric mean on these q squared moduli supplies the bound with F_mat.
Both together give

    product_central |Z_c(beta)|
                  <=(2B Phi/T)^(q/2).                   (8)

This does not assume independent phases or independent central coordinates.
The same two actual boundary blocks are used for every row.
Repeated conjugate moduli cause no problem.

<a id="actual-family-flux-cost"></a>
### An explicit coefficient bound and an actual family control

For 0<=k<d put A_k=sum_(i=0)^k |p_i|.
Because P(beta)=0 and |beta|=1, (1) can be bounded using either side of that polynomial identity:

    |q_(beta,k)|<=min(A_k,W-A_k).

Consequently

    S(P)=sum_(k=0)^(d-1) min(A_k,W-A_k)^2,
    Phi<=S(P)<=dW^2/4,
    Phi<=C_1^2.                                         (9)

For the last inequality, the l1 norm of q_beta is at most sum_k sum_(i>k)|p_i|=C_1.
The geometric-mean bound follows directly, and the matrix bound follows from ||B_c||_op^2/q<=trace(B_c^*B_c)/q=(sum_beta F_beta^2)/q.
Thus (7) is no worse than the old scalar constant, and (9) can certify a substantive improvement without calculating any roots.

For an explicit already adopted family, take the [L G0131 Salem family](Yin_C_G0336_v1.md#linear-exponent-cyclic-coverage) polynomial

    P_N=t^(N+3)-t^(N+1)-t^N+1-t^2-t^3,
    N=9 mod 120,  N>=9,  d=N+3.

The fixed record proves its irreducibility and central-root domain.
Its six distinct nonzero coefficients give W=6 and C_1=3d.
The prefix minima in (9) are 1,1,2, then N-3 entries equal to 3, then 2,1,1.
Squaring and summing gives the exact control

    S(P_N)=9N-15=9d-42,
    Phi<=9d-42,            C_1^2=9d^2.                  (10)

Thus the certified flux coefficient improves by a factor growing linearly with degree on an actual input family.
This is a symbolic coefficient calculation, not a run of an optimization or a root approximation.
These inputs tend to the plastic-number measure; they are not asserted to lie in the hypothetical small-m Salem range of the later cost obstruction.
No value of E_R is computed.

<a id="joint-collar-flux-radius"></a>
### Grouped endpoint control and the new coercivity radius

Retain V above and split its inverse rows into I={|beta_i|<=1} and E={|beta_i|>1}.
Define

    Gamma_I=sum_(i in I,k)|(V^(-1))_(i,k)|,
    Gamma_E=sum_(i in E,k)|(V^(-1))_(i,k)|,
    Gamma=Gamma_I+Gamma_E,
    Psi^2=Gamma_I^2+Gamma_E^2.                          (11)

If P divides Z_c, the finite integer response w of L G0135 has support [a+d,b] and is zero on both complete boundary states.
The homogeneous difference v=x-w is represented from the left state for modes in I and from the right for modes in E.
On every core coordinate j in [a,b], their propagation moduli are at most one.
The same actual boundary pair (5) therefore gives

    |v_j|<=Gamma_I||X_l||_2+Gamma_E||X_r||_2
                <=Psi sqrt(B/T).                       (12)

Thus T>4B Psi^2 suffices for the strict bound |v_j|<1/2.
This retains the grouped constant rather than replacing it by the larger 16 Gamma^2 B condition of the earlier separate-end estimate.

Let K=floor(W^2 B).
If K=0, E_R>B for every R as before.
Otherwise the integer defect budget supplies ||Z_c||_1<=A_*(ell):=min(K,Z(ell+1)), ell=b-a.
If P does not divide Z_c, its norm is a nonzero integer.
Using (8) on the q central roots and the coefficient bound on the h other roots gives

    1<=|Norm(Z_c(beta))|
      <=(2B Phi/T)^(q/2) A_*(ell)^h exp(m ell).

Hence define

    T_flux(ell)=1+ceil[2B Phi A_*(ell)^(2h/q)
                                       exp(2m ell/q)
                              +4B Psi^2],
    L_flux(ell)=d T_flux(ell).                          (13)

At this collar length the last norm bound is strictly below one, forcing P|Z_c.
Monic integral division gives nonzero integer w; (12) then contradicts the cube at a nonzero coordinate of w.
All indices, the low-degree divisibility case and the finite response support are exactly those of L G0135, with the jointly chosen disjoint blocks (5).
No defect outside the constrained interval or infinite homogeneous extension is used.

Iterate s_0=0, s_(j+1)=s_j+L_flux(s_j) for 0<=j<K.
The same finite defect-cluster closure proves

    R>=s_K  implies  E_R>B.                            (14)

The functions are nondecreasing, every new point consumes a new nonzero integer defect, and R>=s_K contains the final required collar.
Compactness gives the strict minimum conclusion.
From Phi<=C_1^2 and Psi^2<=Gamma^2, (13) is pointwise no larger than the corresponding collar in L G0138; ceilings may hide a strict improvement at an individual parameter value.

<a id="inverse-row-endpoint-cost-boundary"></a>
### What the retained inverse-row endpoint cost still prevents

The following limitation is specific to the l1 inverse-row endpoint method (11)--(12).
Continue in the [L G0132 hypothetical Salem domain](Yin_C_G0337_v1.md#tunable-salem-finite-energy-envelope)

    0<m<=1/32,  q=d-2>=2,
    B>=B_m=-2log(16m)/pi^2+m exp(-2m)/(32d^2),
    B>2/15,  K=floor(W^2B)>=1.                          (15)

The last two elementary bounds were checked in L G0138: W>=3, log2>2/3 and pi^2<10 suffice.
Put lambda=2m/q.
As before (13) obeys L_flux(ell)<=C_flux exp(lambda ell), where

    C_flux=d[2B Phi K^(2h/q)+4B Psi^2+2].

The bounded-growth Euler comparison would require lambda C_flux K<1.
Even the improved endpoint term prevents that:

    lambda d (4B Psi^2)>1.                             (16)

To prove it, the q central rows of V^(-1) each have l1 norm at least one, because their pairing with their own unit-modulus V column is one.
The two other roots are alpha=exp(m) and alpha^-1.
Write v_+,v_- for their V columns and r_+,r_- for the matching inverse rows.
They satisfy

    r_+(v_+-v_-)=1,  r_-(v_+-v_-)=-1,
    ||v_+-v_-||_infinity=2sinh((d-1)m).

Each hyperbolic row therefore has l1 norm at least the reciprocal of this last quantity.
Adding disjoint row contributions gives

    Gamma>=q+1/sinh((d-1)m),
    Psi^2>=Gamma^2/2.                                  (17)

Let x=dm.
If 0<x<=1, convexity gives sinh x<=x sinh1, while e<3 and e^(-1)>1/3 give sinh1<4/3.
Since (d-1)m<x, Gamma>q+3/(4x).
With u=xq>0, it follows that

    x Gamma^2/q>u+3/2+9/(16u)>=3,
    lambda d (4B Psi^2)=8B x Psi^2/q>12B>8/5>1.

The middle comparison is the elementary arithmetic-geometric mean bound u+9/(16u)>=3/2.
If x>1, instead Gamma>=q and Psi^2>=q^2/2 give

    lambda d (4B Psi^2)>4qB>=8B>16/15>1.

This proves (16) in both cases.
In particular lambda C_flux K>1, and even the first scaled step lambda s_1 exceeds one.

This obstruction is NOT a proof of the height-K tower bound of L G0138 for the new flux recursion.
The endpoint term in (13) is additive; after replacing C_1 by Phi, the coefficient of its exponential term may be substantially smaller.
A large first step or failure of the sufficient Euler regime alone does not prove the same tower, a lower bound on the true first successful energy window, or failure of the actual finite-energy test.

### Scope and the remaining endpoint problem

The new facts are the exact normalization (2)--(4), the shared two-collar energy budget, the geometric-mean and joint-matrix central flux constants, the coefficient-only bound with the actual family control (10), and the correspondingly improved rigorous coercivity radius (13)--(14).
These change finite costs; they are not merely different notation for C_1.

The remaining cost calculation isolates the endpoint method that still prevents the previously proposed bounded-growth regime at the Salem target.
It does not apply unchanged to bounds using l2 inverse rows, a Gramian formed from all collar observations, or a direct stable/expanding filter.
Such a replacement must reprove the homogeneous core estimate with its own actual constants and finite indices.
No completed claim for one of those replacements is included here.

Any use with L G0132 still needs an actual certified E_R at a window where its positive-part envelope is nontrivial.
Neither the new constants nor the endpoint obstruction supply a lower bound for the transition product, an optimized energy value, uniform near-one coverage or a resolution of G0001.
