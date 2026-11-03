---
author: Yin
---

# A geometric crossing bounds actual Salem transition products

Date: 2026-10-09.
Direct bounded G0001 derivation by the assigned entropy_status AI for Yin.
This candidate concerns the actual transition product, including all noninteger phases.
It does not use the retained full-defect-budget radius or a lower bound on integer resonance mass.
Completed independent AI proof review is recorded below.
No mathematical numerical run, new source, or claim of novelty is involved.

Local reuse checked the actual traces and windows of [L129](Yin_L_G0129_v1.md#tunable-tail-finite-certificate), the exact finite Fejer identity of [L126](Yin_L_G0126_v1.md#finite-fejer-transition-average), and the actual Salem integer-resonance result of [L151](Yin_L_G0151_v1.md#actual-salem-resonance-bound).
The fixed L89/L97 original-law comparisons used in L151 were also read.
The new product bound below does not depend on those entropy estimates.

The direct reuse check of L111, L112 and L119 found different retained statements: respectively a hyperbolic forcing/Jensen amplitude cap, the costs of flattening a trace window, and the fixed-input optimized binomial transient.
None of those statements is used as a premise for the finite geometric-crossing argument below.
This is a local reuse assessment, not a literature-wide originality assertion.

<a id="finite-geometric-cosine-crossing"></a>
## 1. An elementary finite geometric crossing

Let m>0, t>0, and let J>=0 be an integer.
Suppose

    t exp(-Jm) <= 1/8,    t exp(Jm) >= 3/8.             (1)

For the increasing sequence x_j=t exp(jm), the real interval of indices for which 1/8<=x_j<=3/8 is

    [log(1/(8t))/m, log(3/(8t))/m].

It is contained in [-J,J] by (1) and has length log(3)/m.
The number n_c of integers in a closed real interval [a,b] is max(0,floor(b)-ceil(a)+1), and hence is at least b-a-1.
Consequently

    n_c >= log(3)/m-1.                                 (2)

This lower bound is valid even if its right side is negative; no unstated small-m requirement is needed.
Every corresponding phase 2pi x_j belongs to [pi/4,3pi/4], where |cos(2pi x_j)|<=1/sqrt(2).
All other factors have absolute value at most one.
Therefore

    product_(j=-J)^J |cos(2pi t exp(jm))|
       <=2^(-n_c/2)
       <=A(m):=sqrt(2) exp[-a/m],
    a=(log(2) log(3))/2.                               (3)

Both interval endpoints are included.
If a cosine factor vanishes, the estimate remains valid.
For large m the right side can exceed one; one may always replace it by min(1,A(m)).

<a id="actual-salem-geometric-product-bound"></a>
## 2. The actual trace window necessarily crosses this interval

Let alpha>1 be a Salem number, P its monic irreducible polynomial, d=q+2>=4 its degree, and K0=Q(alpha).
There is exactly one expanding embedding sigma_+ with sigma_+(alpha)=alpha, one stable embedding sigma_- with sigma_-(alpha)=alpha^(-1), and q central embeddings.
All complex conjugate embeddings are counted separately.
Put

    m=log(alpha)=log M(P)>0.

Let theta be any nonzero algebraic integer in the full field K0, not necessarily in Z[alpha].
Assume

    |sigma(theta)|<=1 at every central embedding,
    H>=1 and |sigma(theta)|<=H at every embedding,
    0<delta<=1/16,
    integer J>=ceil[log(dH/delta)/m].                  (4)

For all integer j write

    u_j=sigma_-(theta) alpha^(-j),
    v_j=sigma_+(theta) alpha^j,
    w_j=sum_central sigma(theta) sigma(alpha)^j.

Since alpha is a unit, theta alpha^j is an algebraic integer also for negative j.
Hence u_j+v_j+w_j is an integer for every j.
Define the actual transition product at this window by

    C(theta,J)=product_(j=-J)^(-1)|cos(2pi v_j)|
                product_(j=0)^J |cos(2pi(u_j+w_j))|.

The integer trace identity and the evenness of cosine imply exactly

    C(theta,J)=product_(j=-J)^J |cos(2pi t alpha^j)|,
    t=|sigma_+(theta)|>0.                              (5)

There is no approximation of the central trace in (5), and no change of multiplier or observation window.
Nonzero t follows from injectivity of the field embedding.

The left endpoint in (1) follows directly from (4):

    t alpha^(-J)<=H alpha^(-J)<=delta/d<=1/64<1/8.
                                                               (6)

For the right endpoint, the nonzero integral field norm gives

    1<=|Norm(theta)|
      =t |sigma_-(theta)| product_central |sigma(theta)|
      <=tH.

Thus the same height window also satisfies

    t alpha^J >= (dH/delta)t >= d/delta >=64>3/8.       (7)

This use of the norm is why the two tail endpoints cannot both remain below the crossing interval for an actual admissible multiplier.
No degree, height, discriminant, or embedding constant is omitted.
Equations (3), (5)--(7) prove the uniform actual upper bound

    C(theta,J)<=min(1,A(m))
      =min(1,sqrt(2) exp[-log(2)log(3)/(2m)]).          (8)

Only the displayed hypotheses (4) are needed.
In particular, (8) has no orbit-length, frequency-count, noise, or entropy premise.

<a id="tunable-salem-target-crossing-obstruction"></a>
## 3. Consequence for the specified L129 transition target

In the L129 Salem specialization 0<m<=1/32 and N>=1,

    epsilon_N=sqrt(m)/(16q sqrt(N)),
    delta=sqrt(m(1-exp(-2m)))/16,
    J_delta=ceil[log(dH/delta)/m].

Its required central multiplier bound is at most one and its delta is at most 1/16.
Hence (4) holds and (8) applies to exactly its enlarged product C_delta(theta)=C(theta,J_delta), for every nonzero integral multiplier satisfying those central and height conditions.

For an entirely elementary comparison, log(2)>=2/3 follows from log(2)=2 atanh(1/3), and log(3)>1 follows from exp(1)<3.
Consequently a>1/3.
Since exp(x)>x for x>0, (3) gives

    A(m)<sqrt(2)m/a<3sqrt(2)m<16m.                    (9)

Thus the proposed actual lower threshold C_delta(theta)>=16m cannot hold anywhere in this specified near-one Salem domain.
This assertion does not need the later L129 finite noise/time guards.
A multiplier search at the retained enlarged window cannot rescue that threshold.

This is an upper restriction on a particular Fourier construction, not a nonexistence result for Salem inputs of small positive measure.
It proves no Mahler gap and supplies no lower bound for the product.
Removing factors by shortening the window changes the product and requires paying the omitted tail factors separately; such a changed certificate is not covered merely by renaming its product C_delta.

<a id="actual-tunable-certificate-ceiling"></a>
## 4. The entire retained L129 inequality has an actual ceiling

Keep the Salem domain 0<m<=1/32, but now allow every parameter choice permitted by the general L129 certificate:

    0<delta<=1/16, 0<kappa<=1/(16q), 0<eta<1,
    N>=1 integral, epsilon_N=kappa/sqrt(N).

Let theta be any nonzero integral multiplier with central conjugates at most epsilon_N and full height bounded by H>=1.
These hypotheses again imply (4) for L129's J_delta, independently of its additional noise/time guards.
Its exact lower-envelope amplitude factor satisfies 0<A_delta<=1.
Every selected integer time belongs to [0,N-1]: its lower endpoint T_(delta,N)>=J_delta>=0 and its upper endpoint N-R_(delta,N)<=N-1.
Its cardinality, including the empty set, therefore satisfies 0<=k_(delta,N)<=N.

Equation (9) gives C_delta<3sqrt(2)m<1/2.
On [0,1/2], the exact binary information function used by L129 satisfies g(0)=g'(0)=0 and g''(x)=1/(1-x^2)<=4/3.
Twice integrating gives g(x)<=2x^2/3<=x^2.
Thus its complete retained income has the actual upper bound

    k_(delta,N) g(A_delta C_delta)
       <=N C_delta^2 <=2N exp(-2a/m).                 (10)

All strict numerical comparisons can be made without approximations.
Since a>1/3 and exp(x)>x^5/120 for x>0,

    2exp(-2a/m)<240(3m/2)^5
       =(3645/2)m^5<2m^3,       0<m<=1/32.            (11)

For the last strict inequality use m^2<=1/1024 and 3645/2048<2.
The exact L129/L108 entropy budget is

    C_ent(m)=(5/12)(exp(2m)-1)^2(1-exp(-4m))
            =(20/3)sinh(m)^3 cosh(m)>=(20/3)m^3.

Consequently, for every permitted parameter and actual multiplier,

    k_(delta,N) g(A_delta C_delta)
          <2Nm^3<N C_ent(m).                          (12)

This holds even before paying L129's positive B_N=(q/2)log N+C_P^KL+log 2.
Whenever the retained certificate is valid, its left side therefore cannot violate its necessary inequality k_(delta,N)g(A_delta C_delta)<=N C_ent(m)+B_N.
It is not enough to change delta, kappa, eta, height, or orbit length within this certificate.
This is an actual-product ceiling for the entire retained Salem test, not merely the failure of the particular 16m threshold.
It does not exclude different windows with separately proved omitted-factor costs, different tests, or the multiple-expanding branch.

<a id="actual-off-integer-fejer-ceiling"></a>
## 5. The full finite Fejer mass, including off-integer contributions

Let K>=2 be an integer and b=K-1.
Take a nonzero integral seed theta and a height bound H>=1, and assume every central conjugate of theta has modulus at most 1/b.
Use 0<delta<=1/16 and a common integer window

    J>=ceil[log(dbH/delta)/m].                          (13)

For each 1<=k<K, the multiplier k theta has central conjugates bounded by one, has full height at most bH, and is nonzero integral.
Therefore the preceding proof applies individually, at this same J, and gives

    Q(k):=C(k theta,J)<=min(1,A(m)).                    (14)

These are sufficient simultaneous hypotheses.
No necessity is asserted for selecting one individually admissible multiplier outside them.

For the actual fair-sign sum S=sum_(j=-J)^J xi_j alpha^j and its independent copy S', put

    psi_theta(x)=sum_(sigma != sigma_+) sigma(theta x),
    Z=psi_theta(S-S'),
    p=Pr(Z in Z),
    F_K(z)=(1/K)|sum_(a=0)^(K-1) exp(2pi i a z)|^2.

The precise L126 identity is

    E F_K(Z)=1+2 sum_(k=1)^(K-1)(1-k/K)Q(k)^2.

The weights of the nonzero terms sum to K-1.
Thus the full mass, with no deletion or estimate of noninteger near-resonances, satisfies

    1<=E F_K(Z)<=1+(K-1)min(1,A(m)^2),
    0<=[E F_K(Z)-1]/(K-1)<=min(1,2exp[-log(2)log(3)/m]).
                                                               (15)

If O_K=E[F_K(Z) 1_(Z notin Z)] denotes only its off-integer part, F_K=K at integers gives the more explicit statement

    1-Kp <= O_K
          <=1-Kp+(K-1)min(1,A(m)^2).                 (16)

In L151's smaller simultaneous domain, Kp<1/4, so in particular O_K>3/4.
The off-integer contribution is therefore substantial; it cannot be treated as zero.
Nevertheless (15) bounds exactly the surplus above the zero-multiplier contribution.
By (9) that normalized surplus is strictly smaller than (16m)^2 on the L129 target interval, for every K satisfying (13).
Neither the true integer resonance mass nor the full off-integer Fejer mass can produce that target through this simultaneous test.
Equation (14) is stronger: it upper-bounds every actual candidate, rather than only a selection lower certificate.

The argument is restricted to the specified one-expanding Salem configuration and retained height-certified windows.
With several expanding embeddings, the complementary trace is a sum of modes and (5)'s single increasing geometric phase is unavailable.
No extension to that unresolved branch is asserted here.

## Contribution and current review status

The assigned entropy_status AI derived Sections 1--3 and 5, equations (1)--(9) and (13)--(16), and checked the exact trace reduction, full-field integrality, both height/norm endpoint inequalities, the closed-interval count, all constants, the L129 parameter substitution, and the complete actual-law Fejer normalization.
The coordinator requested this bounded actual off-integer test and asked for the geometric crossing to be written after receiving its derivation.
It subsequently derived Section 4, equations (10)--(12), which the assigned author checked and incorporated.
The coordinator's separate probability-return work is not used here.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0053_v1.md#actual-salem-geometric-independent-review), with its original inspected scope and relationship.
