---
author: Yin
---
# Quantitative frustration cost for arbitrary-support positive-root companions

Date: 2026-10-23T14:43.
Human author Yin.
Root developed the stationary signed-energy identity and quantitative positive-root crossing under the active G0001 continuation.
The complete author mathematics is retained here; the selected assessment below owns its separate review and adoption.

## Reuse and scope

The local reuse search read the complete relevant [C566 positive-root proof](Yin_C_G0566_v1.md#positive-root-companion-proof), [C568 arbitrary-support equality](Yin_C_G0568_v1.md#general-single-pair-equality-proof), and [C500 weighted resistance argument](Yin_C_G0500_v1.md#perron-weighted-frustration-price).
C566 supplies qualitative positive-root domination and its finite Perron input; C568 characterizes switching equality.
C500 prices frustration in a bipartite singular-value model.
The new step prices an arbitrary-support nonsymmetric pencil using its actual stationary conductances, then converts that price to an explicit larger positive root.
No bipartite reduction, reversible-chain assumption, new external theorem or numerical computation is used.
All statements below are lower-cost comparisons, without an upper realization or uniform original Mahler gap.

## Statement

Let V=I+N be a real upper-unitriangular R-by-R matrix, B=|N| entrywise, and
    p_V(t)=det(tV+V^T), p_abs(t)=det(t(I-B)+(I-B)^T).
Suppose lambda>1 is a positive real root of p_V.
Select a connected component C of the undirected support of B whose original pencil is singular at lambda.
Restrict N and B to C, retaining inherited vertex order, in the following matrix definitions.
Assume no diagonal sign matrix D on C satisfies DND=-B.
Put
    A_t=(tB+B^T)/(t+1), rho=rho(A_lambda).
Choose positive right and left Perron vectors v,l of A_lambda with sum_i l_i v_i=1, and define
    P_ij=(A_lambda)_ij v_j/(rho v_i), pi_i=l_i v_i,
    epsilon_ij=-sign(N_ij) for i<j on support,
    epsilon_ji=epsilon_ij,
    w_ij=(pi_i P_ij+pi_j P_ji)/2 for i<j.
Then P is stochastic, pi is its stationary probability, and every support w_ij is positive.
Choose ANY negative-sign simple cycle Gamma for epsilon, a base vertex o on Gamma, and ANY simple support path L_i from o to every vertex i, with the empty path allowed at o.
Such a negative cycle exists under the stated non-switching assumption.
Define
    R_Gamma=sum_(e in Gamma) 1/w_e,
    R_i=sum_(e in L_i) 1/w_e,
    K=sum_i pi_i (sqrt(R_Gamma)/2+sqrt(R_i))^2.       (1)
For EVERY such choice, K is finite and K>1, and
    rho>=K/(K-1)>1.                                (2)
The COMPLETE p_abs has a positive real root t0 with
    t0>=(lambda+1)rho-1
       >=lambda+(lambda+1)/(K-1),
    m(p_abs)>=log[lambda+(lambda+1)/(K-1)].         (3)
Here m denotes ordinary unnormalized logarithmic Mahler measure, including every factor and multiplicity.
No integrality, bipartiteness, rank/height bound or single-expanding-root hypothesis is needed in (1)--(3).

Suppose additionally V is integral and its ENTIRE polynomial is P0 Q, where P0 is the minimal polynomial of a genuine Salem number lambda occurring once and Q is monic integral with all roots on the unit circle.
Its expanding component is unique.
If that component is not switchable as above, then for the literal full cover p_cover=p_V p_abs,
    m(p_abs)-m(P0)
       >=log[1+(lambda+1)/(lambda(K-1))]>0,
    m(p_cover)-2m(P0)
       >=log[1+(lambda+1)/(lambda(K-1))].           (4)
Every neutral factor remains and R=deg P0+deg Q.
Writing Delta=m(p_abs)-m(P0), every choice in (1) also satisfies
    K>=1+(lambda+1)/(lambda(exp(Delta)-1)).         (5)
Consequently, along ANY sequence under these hypotheses with Delta tending to zero, K tends to infinity for EVERY choice of cycles and paths, even if lambda varies.
No existence of such a sequence is asserted.

The theorem supplies no input-uniform upper bound for K, no upper-cost realization, no matrix for a prescribed P0 and no lower bound for the original m(P0).
A switchable expanding component accompanied by costly neutral components is outside (4); its separate strictness remains in C568.
The actual stationary weights, small conductances and attachment paths cannot be omitted.

## Argument

### Actual stationary normalization

The selected component has an edge, because an isolated pencil is t+1 and is nonsingular at lambda>1.
Every edge gives two positive directed entries in A_t for t>0.
Thus A_t is irreducible, with positive Perron root and left/right vectors by the same finite Perron input used in C566.
The right eigenvector equation gives sum_j P_ij=1.
The left equation gives
    sum_i pi_i P_ij=(v_j/rho)sum_i l_i(A_lambda)_ij
                   =l_j v_j=pi_j.                (6)
This proves stationarity without reversibility or aperiodicity.
All w_e are positive.
Reciprocal positive rescaling of l and v leaves pi,P,w and K unchanged.

Choose a nonzero real kernel vector x for lambda V+V^T on C and set y_i=x_i/v_i.
Coordinates x_i may vanish; no division by x_i occurs.
Let P_epsilon have entries epsilon_ij P_ij on edges and zero otherwise.
Both inherited-order directions of the signed pencil equation give
    P_epsilon y=rho^(-1)y.                       (7)
Indeed epsilon_ij(A_lambda)_ij is the corresponding entry of -(lambda N+N^T)/(lambda+1).

### Exact signed energy and the paid resistance

For any real vector z put E(z)=sum_(i<j) w_ij(z_i-epsilon_ij z_j)^2.
By stochasticity, stationarity and symmetric edge signs,
    E(z)=1/2 sum_(i,j) pi_i P_ij(z_i-epsilon_ij z_j)^2
        =sum_i pi_i z_i^2-sum_(i,j) pi_i P_ij epsilon_ij z_i z_j.
Applying (7) only to its actual real nonzero eigenvector y yields
    E(y)=(1-rho^(-1))sum_i pi_i y_i^2.            (8)
No variational principle for a nonsymmetric spectral radius is invoked.

The spanning-tree chord argument from C568 says that epsilon is a vertex-sign coboundary exactly when every simple cycle has positive product.
Thus the failure of DND=-B gives a negative simple cycle.
Signed telescoping around Gamma and weighted Cauchy--Schwarz yield
    2|z_o|<=sqrt(R_Gamma E(z)).
Telescoping along L_i gives
    |z_i|<=|z_o|+sqrt(R_i E(z)).
Each cycle/path energy is bounded separately by the full nonnegative E(z); overlaps between paths and the cycle are permitted.
Square the last inequality and sum with the SAME pi_i to obtain
    sum_i pi_i z_i^2<=K E(z).                    (9)
For y, equations (8)--(9) give 1<=K(1-1/rho).
Since rho is finite and positive, this forces rho>1, K>1 and (2).

### Quantitative continuous crossing

For every s>=lambda, comparison of each upper and lower support entry gives
    A_s>=[(lambda+1)/(s+1)] A_lambda.
Lower entries have equality; upper entries have the extra factor s/lambda>=1.
Apply this inequality to the positive v and pair with a positive left Perron vector of A_s.
It follows that
    rho(A_s)>=[(lambda+1)/(s+1)]rho.             (10)
Set s0=(lambda+1)rho-1>lambda, so rho(A_s0)>=1.
As t tends to infinity, A_t tends to the strictly upper-triangular B.
The finite-dimensional spectral-radius continuity used in C566 and nilpotence of B show rho(A_t) tends to zero.
Continuity therefore gives t0>=s0 with rho(A_t0)=1.
On C,
    det(t0(I-B)+(I-B)^T)=(t0+1)^|C| det(I-A_t0)=0.
The support-component factorization makes t0 a root of the COMPLETE p_abs, including all other components.
That full polynomial is monic with constant coefficient one, so its Mahler measure is at least log t0.
Together with (2), this proves (3).
No monotonicity of rho(A_t) or uniqueness of the positive crossing is needed.

### Full original and neutral accounting

Under the Salem specialization, m(p_V)=m(P0)=log lambda.
The simple root lies in one component; reciprocal block factorization retains every other original neutral component.
The bound (3) already concerns the full absolute polynomial, so no absolute neutral cost is deleted.
Subtract log lambda to obtain the first line of (4).
The literal full-cover identity of C2 adds m(p_V), giving the second line.
Exponentiating and rearranging gives (5).
Since (lambda+1)/lambda>1, Delta tending to zero forces K tending to infinity without any compactness assumption on lambda.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T14:43 |
| status | open |
| authority | Yin explicitly activated all G0001 strategies and continued the unchanged Task. |
| reason | Register the full arbitrary-support stationary-energy and positive-root theorem for separate checking, retaining every paid parameter and no-uniform-gap boundary. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact theorem](#statement) | Every real upper-unitriangular positive-root component and actual stationary cycle/path price, with complete factors in the integral Salem specialization. |
| argument | [Complete proof](#argument) | Stationarity, actual signed eigenvector energy, full resistance charge, quantitative continuous crossing and complete original/absolute/cover accounting. |
| dependency | [Positive-root pencil input](Yin_C_G0566_v1.md#positive-root-companion-proof) | Finite Perron input, inherited support and nilpotent limit; the quantitative stationary comparison is proved here. |
| dependency | [Literal full cover](Yin_C_G0002_v1.md#signed-cover-identity) | Exact original-times-absolute polynomial and additive unnormalized total measure. |
| support | [Arbitrary-support equality](Yin_C_G0568_v1.md#general-single-pair-equality-proof) | Negative sign convention and full spanning-tree switching criterion; comparison with existing qualitative strictness. |
| support | [Paid bipartite resistance](Yin_C_G0500_v1.md#perron-weighted-frustration-price) | Existing signed telescoping method with overlapping paths; no bipartite singular-value identity is used for the new class. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T15:05 |
| status | proved |
| authority | Yin activated all strategies and continued the unchanged G0001 Task. |
| reason | Adopt the complete arbitrary-support stationary-energy and positive-root crossing theorem after the isolated whole R806 finding. The actual Perron conductances and cycle/path cost remain explicit; the result is a lower companion cost, with no uniform upper realization or original gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact theorem](#statement) | Every real upper-unitriangular positive-root component and actual stationary cycle/path price, with complete factors in the integral Salem specialization. |
| argument | [Complete proof](#argument) | Stationarity, actual signed eigenvector energy, full resistance charge, quantitative continuous crossing and complete original/absolute/cover accounting. |
| dependency | [Positive-root pencil input](Yin_C_G0566_v1.md#positive-root-companion-proof) | Finite Perron input, inherited support and nilpotent limit; the quantitative stationary comparison is proved here. |
| dependency | [Literal full cover](Yin_C_G0002_v1.md#signed-cover-identity) | Exact original-times-absolute polynomial and additive unnormalized total measure. |
| support | [Arbitrary-support equality](Yin_C_G0568_v1.md#general-single-pair-equality-proof) | Negative sign convention and full spanning-tree switching criterion; comparison with existing qualitative strictness. |
| support | [Paid bipartite resistance](Yin_C_G0500_v1.md#perron-weighted-frustration-price) | Existing signed telescoping method with overlapping paths; no bipartite singular-value identity is used for the new class. |
| review | [Whole isolated independent finding](../audits/reviews/Yin_R_G0806_v1.md#arbitrary-support-companion-whole) | Entire exact current statement, complete argument and every selected input at the explicitly bound scope; actual isolated independent review, with all upstream source and non-realization limits preserved. |

