---
author: Yin
---

# Shannon constraints and near-one stationary quantile escape

The complete repeated-block, stationary-information and integer-grid argument is retained from [L216](../ledger/Yin_L_G0216_v1.md#complete-retained-proof-and-review).
The [v1 Statement](Yin_C_G0523_v1.md#statement) permits arbitrary b in (1/2,A) but assigns the stronger A-only rate proved for the midpoint choice.
This version fixes b=(A+1/2)/2 in that explicit-rate assertion; the underlying original argument already uses precisely that choice.
The original finite-quotient and stationary-law results, near-one probability escape, full observation costs and unresolved stronger quantile and gap questions are unchanged.
The [original R112 finding](../audits/reviews/Yin_R_G0112_v1.md#stationary-quantile-complete-independent-review) retains its frozen input and actual review facts.
It has no Review relationships declaration; no historical context isolation or inspection of this revised C is inferred.
The revised statement remains open pending actual complete review of its exact Statement and Argument.

## Statement
Let alpha be an algebraic unit of actual degree d, O=Z[alpha], and q>=2 any integer; the quotient O/qO need not be a field and has M=q^d elements under normalized counting measure.
Use the original digit law p_0=1/2, p_+=p_-=1/4 and the chronological update x->alpha x+eta.
In the formulas below pi_number denotes the mathematical constant pi, while pi denotes a stationary probability.
Let T be the d-step transition operator on O/qO, so that T=U C_q^(tensor d) and T*=C_q^(tensor d) U^(-1), where multiplication by alpha^d is the permutation U and C_q f(x)=[2f(x)+f(x-1)+f(x+1)]/4.
Put delta_q=1-cos^4(pi_number/q), epsilon_q=delta_q/(2+log q), p_q=2-epsilon_q and theta_q=2(p_q-1)/p_q in(0,1).
For every integer k>=1 and every x,y in O/qO, T^(2k)(x,y)<=M^(-1+theta_q^k), and 1-theta_q>=2/[q^2(2+log q)], theta_q^k<=exp[-2k/(q^2(2+log q))].
The bound concerns the actual original process at time2kd and includes q=2 and every composite q.

Let Q be any admissible law: an irreducible positive recurrent Markov chain on a subset S of the actual return core containing0, using only original allowed edges, with stationary probability pi and finite original-digit information I=I(Q) as defined in the retained stationary-information interface.
Infinite support, infinite full-state Shannon entropy and infinite neutral moments are allowed.
Put nu=pi mod qO.
Then for every q>=2 and integer k>=1, H(pi mod qO)>=d[(1-theta_q^k)log q-2kI], D(pi mod qO||Unif)<=d E(q,k,I) and E(q,k,I)=theta_q^k log q+2kI.
For any actual subset A whose residue image has at most N_A<M elements, pi(A)<=min(1,[d E(q,k,I)+log2]/log(M/N_A)).
In particular pi(0)=a implies I(Q)>=[(a-theta_q^k)log q-(log2)/d]/(2k), and the retained exact L212 frontier J(a) is at least the supremum of this right side over all integers q>=2,k>=1, its earlier nonnegative and collision-rate bounds remaining valid.

For alpha=beta>1 Salem of degree d=2s+2, s>=1, put m=log beta.
For actual returning states the necessary real strips are |x_+|<B=1/(beta-1), |x_-|<S=beta/(beta-1), and rho(x)^2=sum_(j=1)^s |sigma_j(x)|^2.
For A_R={x:rho(x)<=R}, |A_R|<=N_R=A_real[C(1+R/sqrt s)]^(d-2), A_real=(2B+2)(2S+2) and C=sqrt(2*pi_number*exp(1)).
The count uses the original order; no maximal-order or discriminant assumption is introduced, and the necessary strips are not assumed sufficient.

For every fixed A>1/2, uniformly over hypothetical near-one Salem inputs and all their admissible stationary laws with I<=2m, pi{rho<=sqrt s/[sqrt m(log(1/m))^A]}->0 as m decreases to zero.
More explicitly, with L=log(1/m) and the fixed choice b=(A+1/2)/2 in(1/2,A), the bound pi{rho<=sqrt s/(sqrt m L^A)}<=min(1,[1/(2L)+4L^(-2b)(2+L/2)log L+4m+(log2)^2/L]/G_A(L)) holds for all sufficiently large L, where G_A(L)=(A-b)log L-log(4C)-C_0 is positive there and C_0=log2*(2+(log24)/2); whence the right side is O_A(L^(-(A-1/2))+1/(L log L)).
Constants and the threshold may depend on the fixed A only; the statement is otherwise input-uniform and retains the original degree and every neutral coordinate.

This is necessary-condition form: no near-one Salem sequence is asserted to exist, and no matching constant-times-sqrt(s/m) quantile bound, contrary upper concentration, critical/attainment classification, full-strip equality or unrestricted reciprocal-unit gap follows.
The logarithmic loss and A>1/2 are retained; A=1/2 is not included.
The I<=2m hypothesis is a relevant approximation class by the retained finite actual Perron interface, not an existence claim.
Laws with finite or infinite support are included, and the probability conclusion is not inferred from a second moment.

## Current assessment
[Selected decision](#decision-complete-corrected-independent-adoption)

## Assessment history

### Decision midpoint-rate-correction-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T17:50 |
| status | open |
| reason | Correct the new v1 summary's arbitrary-b rate to the midpoint choice already proved in the original complete argument. Retain v1 and its actual decisions; no original proof failure, broader quantile theorem, current whole-review pass or research resumption is inferred. Complete review of this exact revised statement and argument remains pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact revised statement](#statement) | Entire exact statement and complete Sections 1--5/equations (1)--(23), with fixed b=(A+1/2)/2 for the A-only explicit rate, every actual quotient and stationary-law quantifier, full time and integer-grid costs, and the necessary-only limits. |
| argument | [Complete retained argument](#argument) | Entire exact statement and complete Sections 1--5/equations (1)--(23), with fixed b=(A+1/2)/2 for the A-only explicit rate, every actual quotient and stationary-law quantifier, full time and integer-grid costs, and the necessary-only limits. |
| dependency | [Exact fixed dependency](Yin_C_G0479_v1.md#stationary-information-fixed-scope) | Only the actual admissible-law/Perron approximation interface, original-digit information and finite/infinite-support admissibility; no new source reading or proof audit. |
| dependency | [Exact fixed dependency](Yin_C_G0508_v2.md#stationary-geometry-fixed-scope) | Actual stationary residue geometry, return-core/admissibility scope and the explicit limitation that the single-block second-moment bound yields no strong quantile scale. |
| dependency | [Exact fixed dependency](Yin_C_G0508_v2.md#cyclic-noise-tensor-contraction) | Exactly L211's retained finite cyclic contraction/tensorization and delta_q>=4/q^2 bound; no second-moment-to-quantile inference and no new contraction proof. |
| dependency | [Exact fixed dependency](Yin_C_G0511_v1.md#prescribed-mass-fixed-scope) | The exact prescribed-zero-mass frontier J(a) and its actual competitor admissibility; the new quotient constraints change neither that frontier nor its attainment status. |


### Decision complete-corrected-independent-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:03 |
| status | proved |
| reason | Adopt the actual new independent complete re-review of the exact midpoint-b Statement and entire repeated-block, Shannon, grid and near-one probability argument. The v1 arbitrary-b rate finding and original R112 scope remain; no stronger constant quantile, hypothetical-sequence existence, unrestricted gap or research resumption follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire exact statement and complete Sections 1--5/equations (1)--(23), with fixed b=(A+1/2)/2 for the A-only explicit rate, every actual quotient and stationary-law quantifier, full time and integer-grid costs, and the necessary-only limits. |
| argument | [Exact argument](#argument) | Entire exact statement and complete Sections 1--5/equations (1)--(23), with fixed b=(A+1/2)/2 for the A-only explicit rate, every actual quotient and stationary-law quantifier, full time and integer-grid costs, and the necessary-only limits. |
| dependency | [Exact dependency](Yin_C_G0479_v1.md#stationary-information-fixed-scope) | Only the actual admissible-law/Perron approximation interface, original-digit information and finite/infinite-support admissibility; no new source reading or proof audit. |
| dependency | [Exact dependency](Yin_C_G0508_v2.md#stationary-geometry-fixed-scope) | Actual stationary residue geometry, return-core/admissibility scope and the explicit limitation that the single-block second-moment bound yields no strong quantile scale. |
| dependency | [Exact dependency](Yin_C_G0508_v2.md#cyclic-noise-tensor-contraction) | Exactly L211's retained finite cyclic contraction/tensorization and delta_q>=4/q^2 bound; no second-moment-to-quantile inference and no new contraction proof. |
| dependency | [Exact dependency](Yin_C_G0511_v1.md#prescribed-mass-fixed-scope) | The exact prescribed-zero-mass frontier J(a) and its actual competitor admissibility; the new quotient constraints change neither that frontier nor its attainment status. |
| review | [Complete corrected independent finding](../audits/reviews/Yin_R_G0733_v1.md#corrected-c529-v2-complete-independent-finding) | Entire exact current Statement and Argument, complete correction and affected necessary input chain at the explicitly bound scopes; actual independent re-review, without widening source, native-computation or Task authority. |

## Complete retained argument

<a id="argument"></a>
<a id="complete-retained-proof-and-review"></a>
<a id="stationary-quantile-fixed-scope"></a>

Date: 2026-10-10.
Starting question: Investigate a concrete coupling between L211 actual stationary geometry and L212 exact prescribed-zero-mass information frontier.
Seek a rigorous multiscale concentration, occupation-return relation, or actual-input discriminator; do not turn a large second moment into a probability bound or assume critical attainment.

### Reuse and changed mechanism

[L211](../ledger/Yin_L_G0211_v1.md#stationary-geometry-fixed-scope) proves an elementary dimension-free p-to2 contraction for the actual d-step quotient kernel and obtains a one-block Renyi bound.
It explicitly does not infer a strong quantile scale from its second-moment bound; its separate norm-isolation argument supplies only a smaller probability-escape ball.
Here repeated actual blocks, applied on both sides of the kernel, turn that contraction into a uniform pointwise transition upper bound.
Stationary path entropy then gives a Shannon bound.
A Euclidean-ball version of the integer norm grid converts it to a substantially stronger near-one probability scale.

[L212](../ledger/Yin_L_G0212_v1.md#prescribed-mass-fixed-scope) supplies the exact stationary zero-mass frontier and its actual-state admissibility.
The present proof adds necessary quotient constraints on its competitors; it neither changes that exact frontier nor classifies unknown Salem critical returns.
Norm interpolation and the smoothing mechanism are classical; the needed proof is written locally from L211's already proved finite inequality, with no new external theorem or source.
No computation is required.

<a id="repeated-actual-block-pointwise-bound"></a>
### 1. Repeated actual quotient blocks with no hidden degree cost

Let alpha be an algebraic unit of actual degree d, O=Z[alpha], and q>=2 an integer; the quotient O/qO need not be a field.
Let M=q^d, and use normalized counting measure on its M elements.
The original digit law is p_0=1/2,p_+=p_-=1/4 and the update is x -> alpha x+eta.
Let T be its d-step transition operator modulo qO.
The actual integral power basis makes the d-step noise a product of d copies of the cyclic noise

    C_q f(x)=[2f(x)+f(x-1)+f(x+1)]/4.

Multiplication by alpha^d is a permutation of the quotient.
Thus T=U C_q^(tensor d), where U is the corresponding permutation operator; its adjoint is T*=C_q^(tensor d)U^(-1).
Both are positive and preserve the uniform measure and constants.
The factorization does not assert that later block noises have unchanged coordinates: their intervening permutations are retained in every operator power.

Reuse the fully proved [L211 contraction](../ledger/Yin_L_G0211_v1.md#cyclic-noise-tensor-contraction), with

    delta_q=1-cos^4(pi_number/q),
    epsilon_q=delta_q/(2+log q),
    p_q=2-epsilon_q,
    theta_q=2(p_q-1)/p_q in(0,1).                         (1)

It gives ||C_q^(tensor d)f||_2<=||f||_(p_q) for f>=0.
Norm-preserving permutations on either side show that the same holds for T and T*.
Holder interpolation between L1 and L2 gives, for f>=0 with mean one,

    ||f||_(p_q)<=||f||_1^(1-theta_q)||f||_2^theta_q
                 =||f||_2^theta_q.                         (2)

The exponent follows from1/p_q=(1-theta_q)+theta_q/2.
Iteration is legitimate because every intervening density remains nonnegative with mean one.
Starting at the point density M*1_{x}, whose L2 norm is sqrt M, we obtain for every integer k>=1

    ||T^k(M*1_x)||_2<=M^(theta_q^k/2),
    ||(T*)^k(M*1_x)||_2<=M^(theta_q^k/2).                    (3)

Writing the 2k-step matrix entry as the pairing of a forward row and backward column density and applying Cauchy--Schwarz now yields

    T^(2k)(x,y)<=M^(-1+theta_q^k)  for every x,y.           (4)

Explicitly the two densities are M T^k(x,z) and M T^k(z,y); their normalized pairing equals M T^(2k)(x,y).
They are respectively an adjoint and a forward iterate as in(3).
This checks both the factor M and the operator orientation.
No reversibility of the affine kernel is assumed.
Zeros in the transition matrix cause no problem, since only an upper bound is needed.
Equation(4) is about the actual original process at time2kd, not a substituted independent product process at that later time.

The time bound remains explicit and independent of degree apart from this factor d.
L211 gives delta_q>=4/q^2, hence

    1-theta_q=epsilon_q/p_q
       >=2/[q^2(2+log q)],
    theta_q^k<=exp[-2k/(q^2(2+log q))].                    (5)

The endpoints q=2 and every composite q are included.
For q=2 the exact d-step uniformization is stronger than(4), but it is not needed below.

<a id="actual-stationary-all-modulus-shannon"></a>
### 2. A Shannon bound for every actual stationary law

Let Q be any admissible irreducible positive recurrent law on a subset of the actual return core containing zero, with invariant probability pi and original-digit information I=I(Q), in the sense of L201/L212.
Infinite support, infinite full-state Shannon entropy and infinite neutral moments are allowed.
Let nu=pi mod qO.
Compare a stationary Q path of length N=2kd with the original iid-digit path started in the same pi.
The chain rule gives relative entropy exactly NI.
As in L211, the finite-alphabet row log likelihood is absolutely integrable; no full-state entropy is being subtracted.

Data processing to the two endpoint residues gives

    D(J || nu T^(2k))<=2kd I,                              (6)

where J is a finite joint law whose two marginals are nu.
With X,Y its two coordinates,

    D(J || nu T^(2k))
       =-H_J(Y|X)-sum_(x,y)J(x,y)log T^(2k)(x,y)
       >=-H(nu)+(1-theta_q^k)log M.                        (7)

The comparison law is positive on every J-supported transition, by absolute continuity of original digit paths; zero rows outside that support do not enter the logarithm.
Combining(6)--(7) proves

    H(pi mod qO)
       >=d[(1-theta_q^k)log q-2kI],                        (8)
    D(pi mod qO || Unif)
       <=d E(q,k,I),
    E(q,k,I)=theta_q^k log q+2kI.                           (9)

This is a Shannon statement, unlike the single-block Renyi conclusion in L211.
Its larger path time is explicitly charged.
The actual quotient need not inherit a Markov law from Q, and no such premise is used.
Ineffective choices of q,k merely give a weak bound, not a false uniform-mixing assertion.

For any actual subset A whose residue image has at most N_A<M elements, binary log-sum onto that image and its complement yields

    pi(A)<=min(1,[d E(q,k,I)+log2]/log(M/N_A)).              (10)

Indeed if the image has uniform mass b<=N_A/M and stationary mass v>=pi(A), then D(nu||Unif)>=v log(1/b)-H_binary(v)>=pi(A)log(M/N_A)-log2.
No condition pi(A)>=b is necessary.
One may replace N_A by any known real upper bound strictly between zero and M; an empty A is immediate.

The single-state case gives the actual prescribed-mass condition

    pi(0)=a implies
    I(Q)>=[(a-theta_q^k)log q-(log2)/d]/(2k).               (11)

Consequently L212's exact J(a) is at least the supremum of the right side over integers q>=2,k>=1, as well as its previously known nonnegative and collision-rate bounds.
This does not claim the new quotient lower bound is sharp or uniformly better than every old zero-mass inequality.
It is a valid additional constraint on exactly the same actual competitors, without assuming the infimum is attained.

<a id="euclidean-neutral-norm-grid"></a>
### 3. A Euclidean-ball count in the actual Salem order

Now let alpha=beta>1 be Salem of degree d=2s+2, s>=1, and put m=log beta.
For actual returning states the necessary real strips are

    |x_+|<B=1/(beta-1),
    |x_-|<S=beta/(beta-1),
    rho(x)^2=sum_(j=1)^s |sigma_j(x)|^2.                   (12)

No sufficient full-strip theorem or compact-termination premise is required.
For the actual set A_R={x:rho(x)<=R}, the improved norm-grid count is

    |A_R|<=N_R=A_real [C(1+R/sqrt s)]^(d-2),
    A_real=(2B+2)(2S+2),     C=sqrt(2*pi_number*exp(1)).     (13)

Here is the complete count.
Partition each real embedding axis into half-open unit intervals, and each of the2s real/imaginary neutral coordinates into half-open intervals of length1/sqrt2.
At most one algebraic integer lies in each complete product cell: two distinct such integers have both real differences of absolute value less than1 and each complex difference of modulus less than1, contradicting their nonzero integer norm.
The original order O suffices; no maximal-order or discriminant assumption is introduced.

The two real strips meet at most2B+2 and2S+2 cells.
The neutral cells meeting a Euclidean ball of radius R are disjoint, each has volume2^(-s), and their union lies inside the ball of radius R+sqrt s: their diameter is sqrt s.
Thus their number is at most

    (2*pi_number)^s (R+sqrt s)^(2s)/s!
       <=(2*pi_number*exp(1))^s(1+R/sqrt s)^(2s).          (14)

The last step uses s!>=(s/exp(1))^s; for example sum_(j=1)^s log j>=integral_1^s log t dt=s log s-s+1 proves it, including s=1.
This gives(13).
Unlike a bounding cube, the ball count retains the sqrt s normalization, which is essential when degree varies.

Combining(10) and(13) proves, whenever its denominator is positive,

    pi{rho<=R}
      <=min(1, [d(theta_q^k log q+2kI)+log2]
          /[d log q-log A_real
                  -(d-2)log(C(1+R/sqrt s))]).              (15)

This is an explicit finite-parameter probability bound.
It concerns the actual stationary law, not the measure of a uniform quotient surrogate.
It applies without any finite second moment or bound on the full support.

<a id="near-one-logarithmic-loss-quantile-escape"></a>
### 4. Near-one probability escape up to a logarithmic loss

For every fixed A>1/2, uniformly over hypothetical near-one Salem inputs and all their admissible stationary laws with I<=2m, one has

    pi{rho<=sqrt s/[sqrt m (log(1/m))^A]} ->0
                     as m decreases to zero.              (16)

The quantifier is necessary-condition form: no sequence of Salem numbers tending to one is asserted to exist.
Every actual input/law in the specified range obeys the bound below.
Finite and infinite supported laws are both included.

Write L=log(1/m), choose b=(A+1/2)/2, so1/2<b<A, and for sufficiently large L set

    q=floor[m^(-1/2)L^(-b)]>=2,
    k=ceil[q^2(2+log q)log L],
    R=sqrt s*m^(-1/2)L^(-A).                              (17)

By(5), theta_q^k<=L^(-2).
Since log q<=L/2 and I<=2m,

    E(q,k,I)
       <=1/(2L)+4 L^(-2b)(2+L/2)log L+4m.                (18)

This retains the entire2kd observation cost.
The right side tends to zero because b>1/2.
In particular no limit interchanges k,d and the input without a displayed uniform estimate.

It remains to ensure that the actual real strips and degree do not consume the denominator.
For0<m<=1, B<=1/m, S=B+1 and

    A_real<=24/m^2.                                       (19)

Also the nonzero integer P(1) gives, exactly as in L211,

    BS<=product_j |1-zeta_j|^2<=4^s.

Since exp(m)-1<=exp(1)m, we have BS>=exp(-2)m^(-2), hence

    d=2s+2>=2+(2L-2)/log2>=L/log2       for L>=2.          (20)

Thus log A_real/d<=C_0:=log2*(2+(log24)/2), an absolute constant in that range.
No stronger accepted house theorem is needed.

Put x=m^(-1/2)L^(-A), which tends to infinity.
For sufficiently large L, the floor in(17) gives q>=m^(-1/2)L^(-b)/2 and1+x<=2x.
It follows that

    log[q/(C(1+x))] >=(A-b)log L-log(4C).

Since C(1+x)>1, the denominator in(15), divided by d, is at least

    G_A(L)=(A-b)log L-log(4C)-C_0.                        (21)

It is positive for sufficiently large L.
Equations(15),(18),(20) now give the explicit uniform consequence

    pi{rho<=sqrt s/[sqrt m L^A]}
       <=min(1, [1/(2L)+4 L^(-2b)(2+L/2)log L
                        +4m+(log2)^2/L]/G_A(L)).         (22)

This tends to zero, proving(16).
In particular the displayed bound is

    O_A(L^(-(A-1/2)) +1/(L log L))                         (23)

as L tends to infinity.
Constants and the threshold may depend on the fixed exponent A only.
The statement is input-uniform otherwise, with original degree and every neutral coordinate retained.

Equivalently, every fixed positive quantile of rho must eventually exceed sqrt s/(sqrt m L^A), for every fixed A>1/2.
This is much stronger than L211's sqrt s/2 isolation ball and approaches its sqrt(s/m) full-support/second-moment scale up to a power of log(1/m).
It is not a matching constant-times-sqrt(s/m) quantile theorem.
Crucially, the new probability bound comes from Shannon entropy at a fully charged longer path time and the actual ball count; it is not inferred from a large second moment.

### 5. What this adds to the critical frontier and what remains open

L201 guarantees finite actual stationary laws with information arbitrarily close to h_2(beta)<=m, so the I<=2m condition is a relevant approximation class for any sufficiently small positive m input.
L212 determines the exact information price at a specified zero mass and shows why some minimizing families use very long excursions.
Every one of those actual competitors also obeys(8)--(15), and on a hypothetical near-one Salem sequence obeys(16).
Thus even their bulk neutral scale, not only their second moment or one atom, must grow almost as fast as m^(-1/2) per sqrt s, subject to the explicit logarithmic loss.

This is still a necessary geometric price, not a contradiction: no independent upper quantile, occupation-radius cap or prohibited return-time law has been established.
The actual infinite cores already retained for named Salem inputs allow unbounded neutral radius.
Nor does the argument decide whether their critical information minimum is attained, prove a general full-strip identity, identify R_f with the collision radius, or turn Salem-only constraints into a theorem for all reciprocal units.

The next changed question is whether actual algebraic return paths, several moduli simultaneously or a cost for coupling expanding/stable coordinates to this bulk neutral scale impose an incompatible upper bound or further information loss.
A repeated calculation of the second moment, the old one-block Renyi estimate or the isolation ball would no longer test that question.
Conjectural candidates remain eligible, with the missing uniform estimate explicit.
The unrestricted positive-gap question remains unresolved.

### Contribution and author checking

The coordinating AI for Yin developed this full argument; assigned agents did not contribute its interpolation, Shannon, ball-count or varying-input deductions.
The previous L211 contraction and L201/L212 admissibility/frontier are explicit fixed dependencies.
Author self-check covers both forward and adjoint powers, normalized row/column density factors, the actual permutation between blocks, repeated-path KL and all2kd costs, Shannon versus Renyi, finite-image binary entropy, grid diameter and factorial bound, necessary rather than sufficient real strips, the degree lower bound from P(1), every floor/ceiling and logarithmic exponent, and the exact quantifiers in(16)--(23).



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0112_v1.md#stationary-quantile-complete-independent-review), with its original inspected scope and relationship.
