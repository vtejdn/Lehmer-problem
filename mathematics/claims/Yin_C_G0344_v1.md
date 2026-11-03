---
author: Yin
---

# All-central finite-energy coercivity, tower costs and exact sufficient-radius cutoff comparisons

This retains the complete original 2026-10-08 [L138 mathematical argument](../ledger/Yin_L_G0138_v1.md).
The entropy_status agent derived and checked the refinements and comparisons; the coordinator checked the complete assembled argument and supplied the ancillary Gamma bound, with exact original checking relationships retained.
No current Task/E execution, source acquisition, mathematical program run or algorithm implementation is selected by this maintenance.

## Statement

Fix the original monic irreducible positive-Mahler unit P with q>0 central roots, full d,W,Z,C_1,Gamma,m costs, and rational B>0.
The capped coefficient mass A_*=min(K,Z(ell+1)) and all-q norm give the complete improved collar (1), K=floor(W^2 B) iterations (2), and E_R>B for every R>=R_*(P,B), including the separate K=0 case.
The exact ceiling and Euler comparison (7)--(8) require their supplied lambda C K regime, without asserting that its failure precludes another good bound.
For every conditional Salem input 0<m<=1/32 and rational B>=B_m, the exact coefficient arithmetic forces y_(j+1)>y_j+2exp(y_j) and R_*(P,B)>q t_K/(2m).
This tower is a lower bound only on the displayed sufficient radius, not on the first successful actual energy window; the abstract placement (15) is sharp only for support count and empty-collar information and is not a feasible cube response.
The exact same-input cutoff comparison (16) makes that guaranteed-radius range trivial at the stated small N, while B>B_m and the full condition (17) suffice for strict C_delta<16m, including equality in N.
Every tail, height-dependent enlarged product, root/degree/coefficient cost and distinct quantifier remains; there is no early exact certificate, executed optimization, true-window lower bound, product lower bound or uniform Mahler gap.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T10:23 |
| status | open |
| reason | Retain the complete exact original theorem and argument; actual current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(18), all-central norm and capped integer mass, finite collars/spectral/cluster proof, K0 and algebraic terms, exact Euler regime, both P(1) cases and strict tower, ancillary Gamma bound, abstract-model limits, exact U(M)/M cutoff and strict sufficient N comparison with every cost and scope. |
| argument | [Complete argument](#argument) | Entire original (1)--(18), all-central norm and capped integer mass, finite collars/spectral/cluster proof, K0 and algebraic terms, exact Euler regime, both P(1) cases and strict tower, ancillary Gamma bound, abstract-model limits, exact U(M)/M cutoff and strict sufficient N comparison with every cost and scope. |
| dependency | [Exact retained input](Yin_C_G0341_v1.md#explicit-finite-energy-coercivity-radius) | Complete finite cluster, boundary, monic division, two-end spectral and final collar proof with the same constants. |
| dependency | [Exact retained input](Yin_C_G0337_v1.md#tunable-salem-finite-energy-envelope) | Exact original enlarged-product envelope, complete logarithmic witness constants, finite cutoff and B_m domain. |
| dependency | [Exact retained input](Yin_C_G0342_v1.md#sparse-energy-threshold-decision) | Only exact earlier-window testing and fixed-P/B complexity as an application; it supplies no first-successful radius. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T10:29 |
| status | proved |
| reason | Adopt the complete exact original theorem and retained argument after actual current whole self-review, preserving every finite quantifier, source/native limit, exact cost, original input and sufficient-versus-actual boundary. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(18), all-central norm and capped integer mass, finite collars/spectral/cluster proof, K0 and algebraic terms, exact Euler regime, both P(1) cases and strict tower, ancillary Gamma bound, abstract-model limits, exact U(M)/M cutoff and strict sufficient N comparison with every cost and scope. |
| argument | [Complete argument](#argument) | Entire original (1)--(18), all-central norm and capped integer mass, finite collars/spectral/cluster proof, K0 and algebraic terms, exact Euler regime, both P(1) cases and strict tower, ancillary Gamma bound, abstract-model limits, exact U(M)/M cutoff and strict sufficient N comparison with every cost and scope. |
| dependency | [Exact retained input](Yin_C_G0341_v1.md#explicit-finite-energy-coercivity-radius) | Complete finite cluster, boundary, monic division, two-end spectral and final collar proof with the same constants. |
| dependency | [Exact retained input](Yin_C_G0337_v1.md#tunable-salem-finite-energy-envelope) | Exact original enlarged-product envelope, complete logarithmic witness constants, finite cutoff and B_m domain. |
| dependency | [Exact retained input](Yin_C_G0342_v1.md#sparse-energy-threshold-decision) | Only exact earlier-window testing and fixed-P/B complexity as an application; it supplies no first-successful radius. |
| review | [Actual current whole self-check](../audits/reviews/Yin_R_G0562_v1.md#current-all-central-radius-finding) | Complete current statement, retained proof and every directly used interface; self-reviewed. All old findings retain their actual original inputs, dates, contexts and mathematical limits. |

## Complete retained argument

<a id="argument"></a>
<a id="all-central-coercivity-radius"></a>
### Domain and an improved collar length

Keep the L G0135 domain: P is monic irreducible, has constant coefficient +/-1, positive logarithmic Mahler measure m, and q>0 unit-circle roots.
Put d=deg P, h=d-q, M=exp(m)>1, and retain

    W=||P||_1,  Z=floor(W/2),  C_1=sum_i i|p_i|,
    Gamma=sum_(i,j)|(V^(-1))_(i,j)|,
    V=(beta_i^j)_(0<=j<d,1<=i<=d).

For a rational B>0 let K=floor(W^2 B).
If K=0, the old defect count already proves E_R>B at every R.
Suppose K>=1.
Define

    A_*(ell)=min(K,Z(ell+1)),
    T_*(ell)=1+ceil[4 C_1^2 B A_*(ell)^(2h/q)
                                  exp(2m ell/q)
                            +16 Gamma^2 B],
    L_*(ell)=d T_*(ell),                    ell>=0.       (1)

All these quantities are effective from the fixed input.
Positive rational upper bounds for the real algebraic constants and terms may be used to choose integer T instead.
In particular the fractional power of the positive integer A_* has an exact real-algebraic meaning.
The function L_* is nondecreasing.
Define

    s_0=0,  s_(j+1)=s_j+L_*(s_j),  0<=j<K,
    R_*(P,B)=s_K.                                      (2)

Then

    R>=R_*(P,B)  implies  E_R>B.                       (3)

Here E_R remains the exact box-constrained quantity of L G0130, not a cube-free Gram relaxation.
This is a pointwise improvement of the collar and radius bounds in L G0135, with its same constants: A_*<=Z(ell+1), h/q<=d-1, q>=1 and M>1 make every new collar term no larger than its old counterpart.
It need not be strictly smaller at every parameter value.

To prove (3), assume a feasible x has energy at most B.
Its integer defects z_j=P(S)x_j satisfy the stronger coefficient budget

    sum_j |z_j|<=sum_j z_j^2<=K.                        (4)

The first inequality holds separately for every integer z_j, and the second is the old Young estimate with its integer floor.
Thus a cluster polynomial Z_c(t)=sum_(j=a)^b z_j t^(b-j), of span ell=b-a, has coefficient l1 norm at most A_*(ell), not only Z(ell+1).

Suppose this cluster has two zero-defect collars of length dT, where T=T_*(ell), inside [-R,R].
The disjoint complete d-coordinate blocks in the left and right collars supply boundary states of norms at most sqrt(B/T), exactly as in L G0135.
The same boundary identity at EVERY central root beta gives

    |Z_c(beta)|<=2 C_1 sqrt(B/T).                       (5)

This uses each conjugate, counting both members of every complex pair.
If P does not divide Z_c, irreducibility makes every conjugate value nonzero and their product is a nonzero integer.
At each of the h off-circle roots use |Z_c(beta_i)|<=A_*(ell) max(1,|beta_i|)^ell.
Multiplication gives

    1<=|Norm(Z_c(beta))|
      <=[2 C_1 sqrt(B/T)]^q A_*(ell)^h exp(m ell).       (6)

The q central roots contribute no Mahler factor.
Formula (1) makes the final expression strictly smaller than one.
Consequently P divides Z_c.
Monic division gives the same finite nonzero integer response w, supported in [a+d,b], as in L G0135.
On both complete boundary states w is zero.
For x-w, stable and central homogeneous modes are bounded from the left boundary and expanding modes from the right.
Thus on [a,b]

    |x_j-w_j|<=2 Gamma sqrt(B/T)<1/2.

Some w_j is a nonzero integer, contradicting the closed cube for x.
All recurrences and blocks use precisely the two finite collars; no infinite sequence, missing endpoint state or homogeneous gap outside [-R,R] is assumed.
If the cluster polynomial has degree below d, its divisibility is already impossible.

The final cluster closure is unchanged: begin with the origin, adjoin one new defect from a nonempty collar, and bound the new span by s_(j+1).
For R>=s_K all K required collars fit.
The last step would produce K+1 distinct defects, violating (4).
Compactness of the finite-dimensional feasible set yields the strict minimum statement (3).

For Salem inputs h=2 and q=d-2.
The old span exponential exp(2m ell) has therefore become exp(2m ell/q), while its polynomial factor in ell is capped by the fixed energy budget K^(4/q).
This is an actual parameter improvement, not just a repetition of qualitative divergence or of the existence of a terminating search.

### An explicit bounded-growth comparison and its exact hypothesis

Let

    lambda=2m/q,
    A=4 C_1^2 B K^(2h/q),  D=16 Gamma^2 B,
    C=d(A+D+2).

The ceiling cost is retained: 1+ceil(u)<=u+2, so

    L_*(ell)<=C exp(lambda ell).                        (7)

If lambda C K<1, comparison with the increasing solution y(t)=-lambda^(-1) log(1-lambda C t) of y'=C exp(lambda y) gives

    s_K<=-log(1-lambda C K)/lambda.

Indeed on every full unit interval within [0,K], y(t+1)-y(t) is at least C exp(lambda y(t)); induction compares the discrete recursion (2) with these increments.
In particular

    lambda C K<=1/2  implies  s_K<=2CK.                 (8)

The last estimate uses -log(1-u)<=u/(1-u)<=2u for 0<=u<=1/2.
This is a sufficient, explicitly checkable parameter regime.
No claim is made that its failure precludes some other good bound on the same recursion or a substantially smaller true energy threshold.

<a id="salem-target-guaranteed-radius-cost"></a>
### At the Salem transition target this radius necessarily iterates large steps

Now use the conditional Salem domain of L G0129/L G0132:

    0<m<=1/32,  q=d-2,  d>=4,
    B_m=-2log(16m)/pi^2 + m exp(-2m)/(32d^2).            (9)

Take any rational B>=B_m.
Since 16m<=1/2, log2>2/3 and pi^2<10,

    B>=B_m>=2log2/pi^2>2/15.                           (10)

The elementary inequality log2>2/3 follows, for example, by strict convexity of 1/t integrated on [1,2]; the standard pi<22/7 gives pi^2<10.
Also W>=3: W=2 for a monic unit polynomial would give t^d+1 or t^d-1, whose Mahler measure is one.
Hence K>=1.

Two arithmetic coefficient facts are decisive.
First C_1>=d.
Second P(1) is a nonzero integer, since P is the irreducible Salem polynomial and alpha=exp(m)>1 is a root.
Therefore

    1<=|P(1)|=|P(1)-P(exp(m))|
       <=sum_i |p_i|(exp(im)-1)
       <=m exp(dm) C_1.                               (11)

The final inequality follows by integrating the derivative of exp(it) between 0 and m, or from exp(im)-1<=im exp(im).
In addition d^2/q>=8, because (d-4)^2>=0.

These facts imply the lower bound

    lambda d (4 C_1^2 B)>128/45>2.                     (12)

Here are both cases with their constants.
If dm<=1, (11) gives m C_1>=exp(-dm)>=1/e.
Consequently the left side of (12) is 8m d C_1^2 B/q>=8d^2 B/(q e)>=64B/e>128/45, using e<3.
If dm>1, that side is greater than 8 C_1^2 B/q>=64B>128/15.
The estimate does not discard any growth of degree or coefficients as m varies.
It does not require a new degree--Mahler lower theorem.

Since A_*(ell)>=1, the actual integer collar in (1) satisfies

    lambda L_*(ell)>2 exp(lambda ell).

Writing y_j=lambda s_j, its exact recursion therefore obeys

    y_(j+1)>y_j+2 exp(y_j),  y_0=0.                    (13)

In particular define t_1=2 and t_(j+1)=exp(t_j).
Induction gives

    R_*(P,B)=s_K> q t_K/(2m).                         (14)

This is a lower bound on the radius returned by this sufficient coercivity construction.
It is NOT a lower bound on the first R at which the actual E_R exceeds B.
The same arithmetic also shows lambda C>2 and hence lambda C K>2, so neither hypothesis in (8) or its preceding logarithmic comparison can hold in the target range (9)--(10).
Thus the simple all-central and coefficient-budget improvements do not remove the iterated growth of this particular guaranteed radius at that target.

The endpoint cost remains present even though (12) needs only C_1.
For each central root, its inverse-V row has l1 norm at least one: its product with its own V column, whose entries have modulus one, equals one.
Thus Gamma>=q.
This observation is consistent with, but is not needed to strengthen, the obstruction (12)--(14).

<a id="abstract-collar-model-sharpness"></a>
### A sharp limit of the support-count and empty-collar information alone

There is also a purely combinatorial reason why merely charging the same unit defects differently cannot shorten the K-step bound.
Let L be ANY positive nondecreasing integer-valued function on nonnegative integers and define s_0=0, s_(j+1)=s_j+L(s_j).
Place K unit defects at

    S={s_0,...,s_(K-1)},  R=s_K-1.                     (15)

They have total squared and absolute defect mass exactly K and include the origin.
Every interval [a,b] containing zero, with both length-L(b-a) collars inside [-R,R], has a nonempty right collar.
To prove this, let s_j be its last contained defect.
If j<K-1, then b>=s_j and b-a>=s_j, and

    b < s_(j+1)=s_j+L(s_j)<=b+L(b-a).

So the next defect belongs to the right collar.
If j=K-1, the same monotonicity instead gives b+L(b-a)>=s_K>R, contradicting the assumed containment of the collars.
This proves the assertion.

Thus the support budget and prohibition of two empty collars, taken alone, permit a defect configuration all the way to R=s_K-1.
The iteration radius is sharp as a consequence of precisely those two pieces of information, even when every defect has magnitude one.
This model also meets the inherited defect coefficient bound since Z>=1.
It is NOT asserted to equal P(S)x for a feasible cube vector, or to have such a vector of energy B.
Additional recurrence, phase, sign or local-energy information may rule it out; none is supplied by the two isolated conditions just modeled.
In particular this is not a counterexample to a logarithmic lower growth theorem for E_R.

<a id="guaranteed-radius-cutoff-comparison"></a>
### Exact comparison with the finite candidate cutoff

Continue in the Salem scope.
Every conclusion about C_delta below uses exactly the actual L G0132 enlarged product: theta is nonzero and integral, its central conjugates have modulus at most sqrt(m)/(16q sqrt(N)), H>=1 bounds all its conjugate moduli, delta_tail^2=m(1-exp(-2m))/256, and J=ceil(log(dH/delta_tail)/m).
No shorter transition product is substituted, and the additional entropy/noise guards are not needed for this upper-envelope comparison.

Use the actual L G0132 logarithmic upper witness, with its complete constants,

    E_R<=U(M_R):=a_P log M_R+b_P,
    M_R=2R+d+1,  a_P=q/(8m)>0,  b_P>0.

No degree, coefficient-height or root term in the existing b_P is being dropped; it is precisely the b_P specified in L G0132 (3).
Fix B>=B_m and let R_*=R_*(P,B), M_*=2R_*+d+1.
If a proposed Fourier length N>=1 satisfies

    N <= m M_*/[64 U(M_*)],                            (16)

then every energy window with R>=R_* gives only the trivial value one in the L G0132 actual-product upper envelope.
Indeed M_*>=d+1>3, and U(M)/M is strictly decreasing there.
For every M_R>=M_*,

    E_R<=U(M_R)<=m M_R/(64N).

Consequently sqrt(E_R)-sqrt(mM_R/(64N))<=0, so the positive-part term in that envelope vanishes and its minimum with one equals one.
This is an exact exclusion of the guaranteed-radius range for that particular test at those N.
Earlier R<R_* remain available and may have much better exact E_R than the sufficient construction predicts.
It is therefore incorrect to read (16) as failure of the actual finite-energy method or as a lower bound on C_delta.

Conversely, if B>B_m and one uses only the certified strict bound E_(R_*)>B, the explicit sufficient condition

    N >= m M_*/[64(sqrt(B)-sqrt(B_m))^2]                 (17)

does imply C_delta<16m by the same actual-product envelope.
Equality in (17) is harmless here because the certified energy comparison is strict.
Formula (14) shows that the right side in this particular sufficient N-condition is greater than

    q t_K/[64(sqrt(B)-sqrt(B_m))^2] > q t_K/(64B).        (18)

Again these are costs of the displayed sufficient combination, not necessary lengths for every actual product certificate.
The statements keep the quantifiers for each varying hypothetical P; no fixed-P asymptotic is being applied uniformly across those inputs.

### Consequence for the next finite test

The new lower mechanism uses all q central embeddings in one integer norm and charges the cluster's actual integer coefficient budget.
It gives an improved explicit coercivity radius.
The cost analysis proves that these two changes alone still leave that radius in an iterated-growth regime at the Salem target, and (15) shows exactly what additional information a better cluster argument would need to use.

L G0136 can test earlier windows exactly, including every cube face needed for the threshold and its equality boundary.
Its polynomial cost in R for fixed P,B does not bound the necessary R or become a uniform complexity bound as K and d vary.
The genuinely useful next certificate would be a strict energy lower bound at an R below the L G0132 candidate cutoff, or a new constraint excluding the abstract long-gap configuration (15).
Repeating only the same defect-count and empty-collar implications cannot supply that gain.

No such early exact certificate or further recurrence constraint is claimed here.
No actual E_R value, feasible long-gap response, transition-product lower bound, uniform Mahler gap or resolution of G0001 has been produced.
