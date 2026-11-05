---
author: Yin
---

# Finite bounded raw-p2 sublevels for real-or-circle algebraic units

Human author Yin.
The arithmetic-return contributor developed the automatic-support argument and the exact shifted-trace cost on 2026-11-05.
The coordinating agent supplied the compact segment tent and the bounded-total-measure strengthening, and checked the mathematical assembly as a contributor.
The complete proof has a selected independent whole assessment at the exact scope stated below.
Its extraction source is [D1's real-or-circle inquiry](../drafts/Yin_D_G0001.md#p2-real-or-circle-output-boundary); that mutable provenance is not a proof dependency.
The fixed argument below includes all necessary field, degree, integrality, norm and counting facts directly.

## Exact inputs and limits

The first mathematical input is the [accepted Pri11 Theorem 3.1 interface](../audits/literature/Pri11/Yin_U001.md#pri11-u001): for an integer polynomial Q of degree D>=55 with simple roots, a real globally A-Lipschitz function supported in the disk of radius R has full-root discrepancy from normalized circle measure at most A(2R+1)sqrt(log(max(D,M(Q)))/D).
Here M(Q) includes the actual leading coefficient.
The retained source is Pritsker's Distribution of algebraic numbers, arXiv:1307.5734v1, Theorem 3.1/equation (3.2), at the recorded statement and applicability scope.
Its potential-theory proof and ancestor inputs are not newly independently audited.

The second mathematical input is exactly the [C147 v5 numerical Dobrowolski consequence](Yin_C_G0147_v5.md#argument), equation (4) multiplied by the actual degree:
for a nontorsion algebraic integer unit beta of degree D>=exp(e),

    m(beta)>=(1/2400)(log log D/log D)^3.             (IN1)

This is the already accepted numerical source statement and elementary logarithm conversion retained there.
The original Dobrowolski proof and a stronger source constant are not newly adopted.
C147's cyclic-norm envelope and its positive-income criterion are not used.

The elementary support comparison in [C855 v1](Yin_C_G0855_v1.md#retained-argument) was a reuse lead.
That unassessed version is not a dependency or adopted premise: the product-formula, support and Cauchy inequalities needed here are proved directly below.
Neither the later universal raw-p2 floor nor an FM13 operator identity is used.
Earlier D1 SF/TU calculations and their source claims are not premises of the fixed proof.
No novelty, unrestricted total-Mahler gap, unit-lattice occupancy theorem or quantitative source-original proof audit is claimed.

## Statement

All logarithms are natural.
For a nonzero algebraic integer unit beta of actual degree D, let beta_1,...,beta_D be all complex embeddings, counting both members of each nonreal pair, and put

    m(beta)=sum_(i=1)^D log^+|beta_i|,
    M_2(beta)=[D sum_(i=1)^D log^2|beta_i|]^(1/2).

The second is the raw degree-weighted p=2 quantity.
All finite-place terms vanish because beta is a unit.
It is not identified with an FM13 operator norm outside that source's restricted arithmetic set.
Write S^1={z in C:|z|=1}.

### A. Uniform divergence at bounded total measure and finite raw sublevels

Fix H>0.
For every nontorsion algebraic integer unit beta with every conjugate in R union S^1 and m(beta)<=H, let k be the number of real conjugates.
Whenever

    D>=max{55,exp(H)},    C_H=2exp(H)+4,

one has

    k/D<=C_H (log D/D)^(1/4),                         (A1)
    M_2(beta)>=[1/(1200sqrt(C_H))]
                  D^(1/8)(log log D)^3/(log D)^(25/8). (A2)

Consequently M_2(beta) tends to infinity uniformly with degree among these units of total measure at most H.
For every B>0 there are only finitely many nontorsion algebraic integer units beta with all conjugates in R union S^1 and M_2(beta)<=B.
Their degrees are bounded by a B-dependent finite constant; no numerical value or enumeration of that finite set is claimed.

### B. Exact broadened trace construction and every radial cost

Let alpha>1 be a genuine Salem number of degree d=2t>=4:
its conjugates are alpha,alpha^(-1) and d-2 nonreal roots on the unit circle.
Put m=log alpha, theta=alpha+alpha^(-1), F=Q(theta), and let P_alpha be the monic integer minimal polynomial of alpha.
Index the t real embeddings rho_j of F by

    theta_0=rho_0(theta)=2cosh(m)>2,
    theta_j=rho_j(theta) in(-2,2) for 1<=j<t.

Let u be any totally positive unit of the FULL integer ring O_F, and put u_j=rho_j(u)>0.
Define

    gamma=2+(theta-2)/u,
    beta=(gamma_0+sqrt(gamma_0^2-4))/2>1,
    gamma_j=rho_j(gamma).

Then gamma is integral and generates F.
Every gamma_j avoids 2 and -2; gamma_0>2 and gamma_j<2 for j>0.
The number beta is a nontorsion algebraic integer unit with every conjugate in R union S^1.
Writing

    e=[F(beta):F] in {1,2},  D=[Q(beta):Q]=et,

retains its exact own degree.
If any gamma_j belongs to(-2,2), then e=2 and D=d.
If e=1, then beta is totally real, all |gamma_j|>2 and D=t=d/2.
When all |gamma_j|>2, the alternative e=2 is also permitted.

Define

    r_0=2asinh(sinh(m/2)/sqrt(u_0)),
    epsilon_j=max{0,log((2-theta_j)/(4u_j))},
    r_j=2arcosh(exp(epsilon_j/2)) for 1<=j<t.

The complete raw norm and lower-face costs are

    sum_(sigma:Q(beta)->C) log^2|sigma(beta)|
        =e sum_(j=0)^(t-1)r_j^2,
    M_2(beta)^2=e^2t sum_(j=0)^(t-1)r_j^2,          (B1)

    epsilon_j=2log cosh(r_j/2)<=r_j^2/4,
    sum_(j>0)epsilon_j<=M_2(beta)^2/(4e^2t),          (B2)

    u_0<=[(theta_0-2)4^(t-1)/|P_alpha(1)|]
                     exp(sum_(j>0)epsilon_j).        (B3)

For e=2 the total measure is m(beta)=sum_j r_j, including every negative real expanding pair.
If a fixed C>0 satisfies M_2(beta)<=C m, it necessarily satisfies

    sum_(j>0)epsilon_j<=C^2m^2/(4e^2t),
    u_0>=sinh^2(m/2)/sinh^2(Cm/(2e sqrt(t))).         (B4)

No finite place, radical degree or splitting-field multiplier is suppressed.
The inequalities are costs for an actual unit, not a claim that a suitable unit exists.

### C. The paid return remains a previously controlled source class

For every fixed C>0, the genuine Salem sources alpha with 0<m(alpha)<=1 admitting an actual unit u as in B and output M_2(beta)<=C m(alpha) have bounded original degree and form a finite set.
In particular their positive total measures have a uniform positive lower bound.
This conclusion uses A and the exact D=et accounting, without using a universal raw-p2 floor or supplying such a u.
Allowing many gamma_j below -2 does not produce a new unbounded-degree near-one coverage class by this mechanism.
No unrestricted G0001 conclusion, reduction of arbitrary reciprocal units to Salem numbers, or construction with nonreal off-circle output conjugates is asserted.

<a id="argument"></a>
## Complete argument

<a id="bounded-total-real-circle"></a>
### 1. Root size, radial support and the full original norm

Let beta be a unit of degree D as in A, and set a_i=log|beta_i|.
The unit product formula gives

    sum_i a_i=0,
    sum_i |a_i|=2m(beta).

Cauchy--Schwarz on all D coordinates gives

    2m(beta)<=sqrt(D sum_i a_i^2)=M_2(beta).          (P1)

Every root satisfies |beta_i|<=exp(m(beta))<=exp(H), since each positive logarithm is one summand of m(beta).
A nonreal conjugate has modulus one by the hypothesis R union S^1.
A real conjugate cannot equal 1 or -1: otherwise the irreducible minimal polynomial would have that rational root and beta would be torsion.
Thus precisely the k real conjugates have nonzero radial logarithms.
For the degrees used below, (IN1) ensures m(beta)>0 and hence k>0.
Cauchy--Schwarz on those k coordinates gives

    2m(beta)<=sqrt(k sum_i a_i^2),
    M_2(beta)>=2m(beta)sqrt(D/k).                    (P2)

This argument applies to the raw quantity at the actual degree.
It requires no representability, projection-irreducibility or operator-norm premise.

### 2. A compact tent bounds the actual real-root count

Put L=exp(H)>=1 and, for 0<r<=1, define on C

    phi_r(z)=max{0,r-dist(z,[-L,L])}.

Distance to a closed set is 1-Lipschitz, as are the positive-part and truncation operations in this expression.
Thus phi_r is globally 1-Lipschitz, is nonnegative, and has support in |z|<=L+r<=L+1.
It equals r at every real root beta_i, because every root has modulus at most L.

On the unit circle the nearest point in [-L,L] is the real part of z, since L>=1.
Consequently its distance to that segment is |Im z|=|sin theta|.
For normalized circle probability mu,

    integral phi_r dmu
      <=r mu{|sin(theta)|<=r}
      =r(2/pi)arcsin(r)<=r^2.                        (P3)

The final bound follows from arcsin(r)<=pi r/2 on [0,1], since this convex function lies below the chord joining its endpoint values.
No omitted off-circle root or unsupported angular test is used.

The monic irreducible integer minimal polynomial has D simple roots in characteristic zero.
For D>=max{55,exp(H)}, it satisfies

    log(max(D,M(beta)))=log D,

because M(beta)=exp(m(beta))<=exp(H)<=D.
The accepted Pri11 estimate therefore applies with its actual Lipschitz constant 1 and support radius R=L+1.
It gives

    |(1/D)sum_i phi_r(beta_i)-integral phi_r dmu|
        <=(2exp(H)+3)sqrt(log D/D).                  (P4)

All nonreal-root contributions to the sum are nonnegative.
Combining the contribution kr/D from the real roots with (P3)--(P4) yields

    k/D<=r+(2exp(H)+3)sqrt(log D/D)/r.

Set r=(log D/D)^(1/4), which lies in(0,1] for D>=55.
This proves (A1), with C_H=2exp(H)+4 and all original embeddings counted.

### 3. Dobrowolski pays the remaining support factor

Since D>=55>exp(e), the accepted numerical input (IN1) and (P2) apply.
Using (A1),

    M_2(beta)
      >=(1/1200)(log log D/log D)^3 sqrt(D/k)
      >=[1/(1200sqrt(C_H))]
           D^(1/8)(log log D)^3/(log D)^(25/8).

This is (A2).
For fixed H its right side tends to infinity: the positive power D^(1/8) dominates every fixed power of log D.
No monotonicity at all finite degrees or explicit cutoff evaluation is asserted.

Now fix B>0 and assume M_2(beta)<=B.
By (P1), m(beta)<=B/2.
Apply A with H=B/2; its lower bound excludes every sufficiently large D, while the finitely many D below its displayed threshold cause no difficulty.
Thus all these beta have bounded degree and total measure at most B/2.
For a monic minimal polynomial of degree D, each coefficient is an elementary symmetric sum, and every product in that sum has modulus at most M(beta).
Hence

    |coefficient of X^(D-j)|<=binom(D,j)exp(B/2).

At bounded D these are finite integer coefficient ranges, leaving finitely many polynomials and finitely many roots.
This proves the finite raw sublevel assertion without a separate finiteness theorem or a new p=2 floor.

<a id="shifted-trace-cost"></a>
### 4. The original trace field and the actual output degree

For the genuine Salem source, every conjugate of theta=alpha+alpha^(-1) is real:
it is theta_0>2 or a trace theta_j in(-2,2) of a unit-circle inverse pair.
Thus F is totally real.
The equation alpha^2-theta alpha+1=0 gives [Q(alpha):F]<=2.
This index cannot equal one, since Q(alpha) has nonreal embeddings whereas F is totally real.
It follows that [Q(alpha):F]=2 and [F:Q]=t.

Let T be the monic minimal polynomial of theta.
It has integer coefficients because theta is an algebraic integer.
Factoring by the original inverse pairs gives directly

    P_alpha(X)=X^t T(X+X^(-1)),
    P_alpha(1)=T(2),
    |P_alpha(1)|=(theta_0-2)
                          product_(j=1)^(t-1)(2-theta_j)>0.   (P5)

No original trace embedding or inverse pair is removed.

Since u and u^(-1) are integral, gamma=2+(theta-2)/u is integral.
Its embeddings satisfy gamma_0>2 and gamma_j<2 for j>0.
If E=Q(gamma) were a proper subfield of F, the embedding of E taking gamma to gamma_0 would extend to [F:E]>1 embeddings of F, repeating that value above 2.
This contradicts its uniqueness.
Hence Q(gamma)=F.
If any embedding took gamma to 2 or -2, injectivity would force gamma itself to equal that rational number, again contradicting gamma_0>2.

The chosen root beta>1 is integral over O_F and hence over Z.
Its inverse gamma-beta is also integral, so beta is a unit and is nontorsion.
The equality gamma=beta+beta^(-1) gives F=Q(gamma) subset Q(beta).
Therefore its exact degree is D=et, where e=[F(beta):F] is one or two.

If some gamma_j lies in(-2,2), then gamma^2-4 is negative at that real embedding and cannot be a square in the totally real field F.
The quadratic is then irreducible over F and e=2.
If e=1, every conjugate of beta is real because beta belongs to F, and its trace beta_j+beta_j^(-1) has absolute value at least 2.
Equality has already been excluded, so all |gamma_j|>2.
If all |gamma_j|>2 the discriminant may or may not be a square; both e values remain allowed.
Each conjugate of beta is a root of a real quadratic X^2-gamma_j X+1.
Such a root is real or, when nonreal, has modulus one because the two roots are conjugate and have product one.
This proves the complete output-class and degree statements.

### 5. Every embedding contributes its actual logarithmic radius

At the distinguished embedding,

    gamma_0=2+4sinh^2(m/2)/u_0.

If r_0=log beta, then cosh(r_0)=gamma_0/2, which gives the stated r_0=2asinh(sinh(m/2)/sqrt(u_0)).
For j>0 put a_j=(2-theta_j)/(4u_j)>0, so gamma_j=2-4a_j.
If a_j<=1, its quadratic roots are on the unit circle and r_j=0.
If a_j>1, then gamma_j<-2, its roots are negative real reciprocals, and their positive logarithmic radius satisfies

    cosh(r_j)=|gamma_j|/2=2a_j-1,
    r_j=2arcosh(sqrt(a_j))
       =2arcosh(exp(epsilon_j/2)).

Every embedding of F has exactly e extensions to Q(beta).
For e=2 the two logarithmic absolute values are +/-r_j, or both zero at a circle pair.
For e=1 just one real root occurs, with squared logarithmic absolute value r_j^2.
Thus the sum of squares is e sum_j r_j^2.
Multiplication by D=et proves (B1).
For e=2 exactly one member of every nonzero reciprocal pair contributes r_j to the positive logarithmic sum, proving m(beta)=sum_j r_j.
All finite places vanish by the unit conclusion already proved.

The identity epsilon_j=2log cosh(r_j/2) also holds at r_j=0.
For x>=0, tanh(x)<=x; integration from zero proves log cosh(x)<=x^2/2.
Consequently epsilon_j<=r_j^2/4.
Summing and using (B1) proves (B2).

If M_2(beta)<=C m, then (B1) gives r_0<=Cm/(e sqrt(t)).
The increasing function sinh and the exact r_0 identity give the second inequality in (B4); the first follows from (B2).
These are necessary coordinate inequalities, not asserted sufficient on their own.

Finally u is a totally positive unit, so product_j u_j=1.
From the definition of epsilon_j,

    u_j>=(2-theta_j)exp(-epsilon_j)/4   for j>0.

Multiplying all these inequalities, then using (P5), yields

    u_0=1/product_(j>0)u_j
       <=4^(t-1)exp(sum_(j>0)epsilon_j)
                          /product_(j>0)(2-theta_j)
       =[(theta_0-2)4^(t-1)/|P_alpha(1)|]
                          exp(sum_(j>0)epsilon_j).

This is (B3), with the actual nonzero integer endpoint norm retained.

### 6. The conditional return pays both source and output degrees

Fix C>0 and consider the sources in C.
Their actual outputs have M_2(beta)<=C because m(alpha)<=1.
Part A gives a C-dependent bound on the output degree D.
Part B gives D=et and d=2t<=2D, hence a bound on the original degree as well.
Their source polynomials have total measures at most 1, so the same elementary coefficient estimate leaves only finitely many monic integer polynomials and finitely many Salem sources.
Every source has log alpha>0 by definition; the finite nonempty class therefore has a positive minimum, and an empty class satisfies any positive lower bound vacuously.

This completes all statement parts.
The result identifies automatic restricted support for this entire output geometry and the exact expense of the broadened trace construction.
It does not manufacture the required positive unit, infer occupancy from a logarithmic lattice or its volume, or extend the output geometry to arbitrary rays or nonreal off-circle conjugates.
The original unrestricted [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract) remains unresolved by this theorem.

## Review and reproduction limits

The complete mathematical proof is written above and uses no numerical experiment, native computation or polynomial enumeration.
The authors checked the own-degree cases, integral inverse and all finite places, complete embedding multiplicities, compact-test support and Lipschitz constant, numerical source normalization, and finite coefficient argument.
Those contributor checks are distinct from the selected independent whole finding.
The selected assessment retains the exact external-statement and original-proof limits described above.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T22:01 |
| status | proved |
| reason | Adopt complete A--C after independent R1087: bounded total Mahler measure forces raw-p2 divergence with degree for real-or-circle units, bounded raw sublevels are finite, and the broadened positive-unit trace construction retains all actual degree and radial costs and only selects a finite small-source class. Exact accepted Pri11 and numerical Dobrowolski interfaces retain their source-proof limits. No universal raw-p2 premise, unit supply, new unbounded near-one coverage or unrestricted G0001 conclusion is used or inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | All A--C, explicit degree thresholds and constants, finite raw sublevels, both quadratic splitting cases and the conditional finite source class. |
| argument | [Complete proof](#argument) | All six sections and IN1/A1--A2/B1--B4/P1--P5, full embedding counts, compact test, actual fields and degrees, units, endpoint norm and coefficient finiteness. |
| dependency | [Exact numerical lower bound](Yin_C_G0147_v5.md#argument) | Only the accepted numerical source bound and its equation (4) converted to total measure at actual degree at least exp(e), with constant 1/2400; no cyclic-norm or small-height premise. |
| support | [Pri11 quantitative discrepancy](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Theorem 3.1/(3.2), simple integral minimal polynomial, global Lipschitz test, support radius and normalized circle measure at the retained statement/applicability scope. |
| support | [Smy08 source and normalization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Retained numerical benchmark and total-measure normalization; no use of the defective resultant explanation or new original-proof audit. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1087_v1.md#real-circle-p2-whole-independent-finding) | Entire A--C and complete proof, exact accepted-source interfaces, both degree branches and all negative and remaining scope limits. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
