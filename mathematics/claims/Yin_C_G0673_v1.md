---
author: Yin
---
# Exact chronological translation scale and original Doob costs

Human author Yin.
Root proposed examining the actual C405 small-real translations against the original positive Perron/Doob branch.
The paid_comparison contributor derived the sharp chronological geometric cost, its explicit matching construction and the exact probability comparison retained here.
This is author work, initially open for fresh isolated whole review.
The [active Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) and its current execution boundary authorize this continuation.

Focused reuse read [C602v2](Yin_C_G0602_v2.md#statement), [C645](Yin_C_G0645_v1.md#statement), [C647](Yin_C_G0647_v1.md#statement) and [C405](Yin_C_G0405_v1.md#salem-strip-all-power-essential-norm).
The actual critical ratios and finite-mean limits were read in [C204](Yin_C_G0204_v1.md#true-harmonic-ratio-limits), together with [C563's explicit nonattainment warning](Yin_C_G0563_v1.md#critical-convolution-bounded-density-test).
The bounded C/L/D search for beta^(-n)h and exponential neutral translation costs supplied C405/L173's fixed-time mechanism, not the quantitative exponent-scale statement below.
[C509](Yin_C_G0509_v1.md#statement) concerns limiting Gaussian-tail translations on a different ambient object.
The proof reuses the retained integral-norm, disk-packing and elementary pigeonhole mechanisms; no new general lattice theorem, external source input or numerical experiment is claimed.

## Statement

Fix the actual irreducible Salem polynomial P(t)=t^4-t^3-t^2-t+1, its exterior root beta, a neutral conjugate zeta and the original order O=Z[beta].
For x in O let x_+,x_- be its embeddings at beta,beta^(-1), and put rho(x)=|x(zeta)|.
Set B=1/(beta-1), S=beta B and retain the actual full zero-to-zero core

    D={x in O:|x_+|<B,|x_-|<S}.

The chronological original kernel is K(x,beta x+eta)=p_eta whenever the endpoint remains in D, and is killed upon exit, with p_0=1/2 and p_1=p_-1=1/4.
All powers use ORIGINAL digit time and complete word probabilities.

For every integer m>=0 and every nonempty finite F,G subset D, define the complete legal translation set

    H_m(F,G)={h in O:F+h subset D, G+beta^(-m)h subset D}.

Here F indexes input columns and G output rows of K^m.
Then every h in H_m satisfies the EXACT full-weight rectangular covariance

    K^m(x+beta^(-m)h,y+h)=K^m(x,y), x in G,y in F.       (CT0)

This is the prescribed displacement-preserving construction, not a classification of all numerical coincidences between kernel entries.

Every distinct pair h,h' in H_m satisfies

    rho(h-h')>d_m=beta^(m/2)/(2sqrt(BS)).                 (CT1)

For every complex center a and r>=0,

    card{h in H_m:|h(zeta)-a|<=r}
       <=(1+4sqrt(BS)r beta^(-m/2))^2.                   (CT2)

Put D(r)={x in D:rho(x)<=r}.
If beta^m>=16BS r^2, at most ONE h in H_m has F+h subset D(r).
This applies also to m-dependent F,G.
In particular, such uniqueness holds at every sufficiently large m for any prescribed r_m=o(beta^(m/2)), including every fixed polynomial radius C(m+1)^a with C>0 and a>=0.

For a matching upper construction, fix F,G independent of m and use their actual strict margins

    u=min_(z in F union G)(B-|z_+|)>0,
    v=min_(z in F union G)(S-|z_-|)>0,
    A_+=sum_(j=0)^3 beta^j, A_-=sum_(j=0)^3 beta^(-j),
    C(F,G)=(1+A_+/u)(1+A_-/v),
    N_m=ceil(sqrt(C(F,G))*beta^(m/2)).

For EVERY integer m>=0 there is a NONZERO h_m in H_m(F,G) with

    |(h_m)_+|<u, |(h_m)_-|<v beta^(-m),
    rho(h_m)<=4N_m.                                    (CT3)

It can be chosen as a difference of two coefficient vectors in {0,...,N_m}^4 in the ACTUAL basis 1,beta,beta^2,beta^3.
No native enumeration is executed or selected by this existence proof.
The smallest nonzero legal translation radius therefore exists and obeys

    d_m<min_(h in H_m, h!=0)rho(h)<=4N_m.                (CT4)

Its exact exponential order for each fixed patch is Theta_(F,G,beta)(beta^(m/2)).
The upper constant is not asserted uniform over patches with shrinking real margins.

For the current C647 route window, put m=n-2 and use its unchanged
R_n=2A_rad sqrt(n log128)+B_rad.
Whenever

    beta^(n-2)>=16BS R_n^2,                             (CT5)

at most one legal translated input copy fits entirely in that route window.
Condition (CT5) holds for every sufficiently large n at the fixed quartic and its fixed route constants.
Thus the C405 construction cannot provide two such copies in C647's square-root window at growing original tail time.
This does not improve or remove the existing 4^(3T_n) lower-count expense, and asserts no impossibility for other endpoint comparisons.
The returned-word resampling kernel and its n+2 digit-work price remain separate from chronological K.

Finally retain C204's actual critical radius R=exp(h_2), positive first-hit harmonic H, and recurrent Doob kernel Q(x,y)=R K(x,y)H(y)/H(x).
No identity R=beta is assumed.
For every legal h,

    Q^m(x+beta^(-m)h,y+h)
       =Q^m(x,y) H(y+h)H(x)/[H(x+beta^(-m)h)H(y)]       (CT6)

on the same rectangle.
All H values are positive; the equality also covers zero entries.
No bound or equality to 1 for this ratio is supplied.

If the ACTUAL critical mean mu=sum_(j>=1)jR^j f_j is finite, C204 supplies
pi(x)=H(x)H(Jx)/mu, Jx=beta^(-1)iota(x), iota(beta)=beta^(-1).
For fixed m,F,G and any sequence h_j in H_m whose translated F supports are pairwise disjoint, let f be any complex function supported on F and f_j(y+h_j)=f(y), zero elsewhere.
Then

    sum_j ||f_j||_(l2(pi))^2<=||f||_infinity^2,
    ||f_j||_(l2(pi))->0.                                (CT7)

Consequently the counting-l2 copies in C405 are not unit stationary-probability copies in the hypothetical finite-mean branch.
Normalization would require their actual masses and the ratios (CT6).
The theorem does not decide finite versus infinite mean, assert a uniformly paid sign flow, change the true critical radius, or resolve the unrestricted Task.

## Argument

### Actual law, two supports and legal copies

Fix P(t)=t^4-t^3-t^2-t+1, exterior root beta, neutral conjugate zeta, O=Z[beta], B=1/(beta-1) and S=beta B.
Keep its actual original core D={x in O:|x_+|<B,|x_-|<S}.
Write rho(x)=|x(zeta)|.
The original chronological kernel K has digit weights p_0=1/2,p_1=p_-1=1/4, with exits from D killed.
For every integer m>=0 and actual endpoints x,y in D, C405 gives exactly

    K^m(x,y)=nu_m(y-beta^m x),

where nu_m is the COMPLETE original displacement law.
Every ambient word joining core endpoints has core intermediates, by preceding and following it with actual zero-to-endpoint and endpoint-to-zero words.

Let F,G be nonempty finite subsets of D, with y in F the input columns and x in G the output rows.
For m>=0 define the entire legal displacement-preserving translation set

    H_m(F,G)={h in O:F+h subset D, G+beta^(-m)h subset D}.

It contains 0, and unit status ensures beta^(-m)h is in the SAME order.
For every h in H_m(F,G),

    K^m(x+beta^(-m)h,y+h)=K^m(x,y) for x in G,y in F.

The equality follows from the exact displacement identity, retaining every original word and probability.
It identifies this rectangular block; it does not identify all rows or turn the killed kernel into an unweighted or renormalized law.
The claim concerns this prescribed displacement-preserving translation, not every possible numerical coincidence of kernel entries.

### Exponential separation and the current-window obstruction

For h,h' in H_m(F,G), h!=h', put v=h-h'.
Using one fixed f in F and g in G, legality gives

    |v_+|<2B,
    |beta^(-m)v|_-=beta^m |v_-|<2S.

Because v is a nonzero algebraic integer in the original quartic field,

    1<=|Norm(v)|=|v_+v_-|rho(v)^2
                 <4BS beta^(-m)rho(v)^2.

Consequently EVERY pair of distinct legal translations satisfies

    rho(h-h')>d_m=beta^(m/2)/(2sqrt(BS)).                 (TR1)

This holds even when F,G depend on m; no fixed positive margin is used for the lower bound.
In particular every nonzero h in H_m satisfies rho(h)>d_m.

For any complex center a and r>=0, disks of radius d_m/2 around the legal neutral images are disjoint.
Those with |h(zeta)-a|<=r lie in a disk of radius r+d_m/2.
Applying area comparison to each finite subcollection gives the complete packing bound

    card{h in H_m:|h(zeta)-a|<=r}
        <=(1+4sqrt(BS)r beta^(-m/2))^2.                  (TR2)

The same bound also establishes finiteness; no continuum or uniform lattice probability is substituted.
If two translated copies F+h and F+h' both lie in D(r)={x in D:rho(x)<=r}, then a fixed f in F gives rho(h-h')<=2r.
Thus at most ONE legal translated copy fits in D(r) whenever

    beta^m>=16BS r^2.                                   (TR3)

For any r_m=o(beta^(m/2)), this uniqueness holds at all sufficiently large m.
In particular it holds for every fixed polynomial radius C(m+1)^a, C>0,a>=0.
The logarithmic horizon in (TR3), not a critical-radius identity, prevents these copies from staying in a diffusive window at growing original time.

For C647's actual tail time m=n-2 and route radius R_n=A_rad*2sqrt(n log128)+B_rad, the explicit sufficient condition is

    beta^(n-2)>=16BS R_n^2.

It holds at every sufficiently large n with its original fixed constants.
Hence the C405 scheme cannot create two such legal copies entirely inside that growing route window.
This is a restriction on this scheme; it neither removes C647's 4^(3T_n) word expense nor disproves some other weighted endpoint comparison.
The returned-word heat-bath clock K_n and its n+2 digit-work factor remain distinct from this chronological K^m.

### Matching upper construction for every fixed patch

The exponential exponent is attained up to fixed patch-dependent constants by the same original order.
Fix F,G once and define their ACTUAL strict margins

    u=min_(z in F union G)(B-|z_+|)>0,
    v=min_(z in F union G)(S-|z_-|)>0,
    A_+=sum_(j=0)^3 beta^j, A_-=sum_(j=0)^3 beta^(-j),
    C(F,G)=(1+A_+/u)(1+A_-/v),
    N_m=ceil(sqrt(C(F,G))*beta^(m/2)).

Consider the (N_m+1)^4 distinct algebraic integers sum_(j=0)^3 a_j beta^j with every a_j in {0,...,N_m}.
They are distinct because P has degree four and is the actual minimal polynomial.
Their two real coordinates lie in [0,N_m A_+] and [0,N_m A_-].
Partition the first real axis into half-open cells of width u and the second into half-open cells of width v beta^(-m).
The number of occupied pairs is at most

    (N_m A_+/u+1)(N_m A_- beta^m/v+1)
       <=(N_m+1)^2 C(F,G) beta^m
       <(N_m+1)^4.

The last strict inequality follows from N_m+1>sqrt(C(F,G))*beta^(m/2).
Two distinct coefficient vectors therefore give a nonzero difference h_m in O with

    |(h_m)_+|<u, |(h_m)_-|<v beta^(-m),
    rho(h_m)<=4N_m.                                    (TR4)

For F+h_m both coordinate shifts are below the corresponding original margins.
For G+beta^(-m)h_m the expanding coordinate shift has size beta^(-m)|(h_m)_+|<u, while the contracting shift is beta^m|(h_m)_-|<v.
Thus h_m is ACTUALLY in H_m(F,G), at the SAME m.
Every intermediate word remains legal by the endpoint fact above.
This is an analytic existence construction by a completely specified finite coefficient box and pigeonhole proof; no native box enumeration is executed or selected.

Combining (TR1) and (TR4), for every fixed nonempty finite patch there exists a nonzero legal translation, and its least possible neutral radius is bounded below by d_m and above by 4ceil(sqrt(C(F,G))*beta^(m/2)).
The least radius exists: (TR2) makes every bounded-radius subcollection finite, and (TR4) provides a nonempty one.
Therefore the scale is Theta_(F,G,beta)(beta^(m/2)).
This does not assert a uniform upper constant for patches whose strict real margins shrink with m.
It sharpens C405's fixed-time existence while retaining its valid essential-norm conclusion.

### Exact Doob and probability cost

Use C204's actual recurrent quartic at its TRUE radius R=exp(h_2).
Its positive first-hit harmonic function H satisfies H(0)=1 and

    Q^m(x,y)=R^m K^m(x,y)H(y)/H(x).

No equality R=beta is used.
For each legal h the exact transformed block is therefore

    Q^m(x+beta^(-m)h,y+h)
      =Q^m(x,y) H(y+h)H(x)/[H(x+beta^(-m)h)H(y)].        (TR5)

Every H value is positive, so (TR5) also holds when the common original kernel entry is zero.
The ratio need not be 1; the unweighted covariance supplies no uniform comparison of these four actual H values.

If the actual critical mean mu is finite, C204 supplies the stationary probability pi(x)=H(x)H(Jx)/mu, Jx=beta^(-1)iota(x).
For any fixed f supported on F and disjoint legal translates F+h_j, the usual translate f_j(y+h_j)=f(y) obeys

    sum_j ||f_j||_(l2(pi))^2
       <=||f||_infinity^2 sum_j pi(F+h_j)
       <=||f||_infinity^2,
    ||f_j||_(l2(pi))->0.                               (TR6)

Thus C405's unit counting-l2 copies are not unit stationary-probability copies in this branch.
Renormalizing them would require the actual masses in (TR6) and ratios in (TR5), neither supplied by the essential-norm statement.
This conditional fact is compatible with finite mean and does not refute it.
The actual mean, a useful uniform endpoint lower comparison and a uniformly paid sign flow remain unresolved.

No new native experiment, order/window extension, R=beta assumption or inference from essential radius alone is made.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:38 |
| status | open |
| reason | Retain the exact original chronological translation covariance with its exponential neutral separation, complete packing/uniqueness bounds and matching fixed-patch four-coordinate construction. The C647 square-root-window obstruction and exact Doob/stationary-weight costs delimit the proposed C405 multi-copy mechanism without deciding the original critical mean. All time, order, full probability and patch-margin scopes are retained. Fresh isolated whole mathematical review is required; no native experiment or new mean branch is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire translation and probability statement](#statement) | CT0--CT7, all original inputs and integer times, varying-patch lower bounds versus fixed-patch matching construction, current route-window consequence, exact H ratios and conditional finite-mean mass boundary. |
| argument | [Complete quantitative construction and limitation](#argument) | Actual endpoint legality and full weights, integral norm at all four embeddings, every-center disk count, strict margins and four-coordinate pigeonhole proof, unchanged clocks, Doob telescoping and summable disjoint-copy masses. |
| dependency | [Original strip operator and exact covariance](Yin_C_G0405_v1.md#salem-strip-all-power-essential-norm) | Same actual quartic/core/order, complete displacement matrix, different domain/range shifts and valid fixed-time essential-norm mechanism; no essential-radius-to-positive-recurrence implication. |
| dependency | [Actual critical H and finite-mean limits](Yin_C_G0204_v1.md#true-harmonic-ratio-limits) | True critical radius, positive first-hit H, exact chronological Doob powers and finite-mean stationary probability, at the original recurrence/source scope. |
| support | [Actual integral-norm neutral packing](Yin_C_G0602_v2.md#neutral-packing-and-load-lower-bound) | Existing four-embedding norm and Euclidean disk mechanisms, reused with the new beta^(-m) strip width. |
| dependency | [Existing growing original route window](Yin_C_G0647_v1.md#statement) | CT5 only: actual tail time n-2, unchanged fixed A_rad/B_rad route radius and separate n+2 digit-work clock; no new count/congestion bound. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:50 |
| status | proved |
| reason | Adopt the entire chronological translation theorem after main reading of the complete fixed argument and fresh isolated whole R894. Exact original full-weight covariance, every-pair exponential separation, all-center packing, matching fixed-margin construction and attained minimum establish the stated scale. The growing square-root route-window restriction and actual Doob/probability costs delimit only this displacement-preserving method. Actual core/source depth, true R, both clocks and conditional finite-mean scope remain; no mean-branch decision or improved endpoint-count/sign-flow cost follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire translation and probability statement](#statement) | CT0--CT7, all original inputs and integer times, varying-patch lower bounds versus fixed-patch matching construction, current route-window consequence, exact H ratios and conditional finite-mean mass boundary. |
| argument | [Complete quantitative construction and limitation](#argument) | Actual endpoint legality and full weights, integral norm at all four embeddings, every-center disk count, strict margins and four-coordinate pigeonhole proof, unchanged clocks, Doob telescoping and summable disjoint-copy masses. |
| dependency | [Original strip operator and exact covariance](Yin_C_G0405_v1.md#salem-strip-all-power-essential-norm) | Same actual quartic/core/order, complete displacement matrix, different domain/range shifts and valid fixed-time essential-norm mechanism; no essential-radius-to-positive-recurrence implication. |
| dependency | [Actual critical H and finite-mean limits](Yin_C_G0204_v1.md#true-harmonic-ratio-limits) | True critical radius, positive first-hit H, exact chronological Doob powers and finite-mean stationary probability, at the original recurrence/source scope. |
| support | [Actual integral-norm neutral packing](Yin_C_G0602_v2.md#neutral-packing-and-load-lower-bound) | Existing four-embedding norm and Euclidean disk mechanisms, reused with the new beta^(-m) strip width. |
| dependency | [Existing growing original route window](Yin_C_G0647_v1.md#statement) | CT5 only: actual tail time n-2, unchanged fixed A_rad/B_rad route radius and separate n+2 digit-work clock; no new count/congestion bound. |
| review | [Independent entire chronological finding](../audits/reviews/Yin_R_G0894_v1.md#chronological-translation-whole-independent-finding) | Whole CT0--CT7 and TR1--TR6, actual fixed inputs and complete weights, all strict norm/packing/margin/pigeonhole/minimum and varying-versus-fixed-patch scopes, route-window and exact Doob/conditional probability limits. |

