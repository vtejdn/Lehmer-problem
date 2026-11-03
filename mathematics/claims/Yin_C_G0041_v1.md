---
author: Yin
---
# Uniform positive-log tails after one cyclotomic preconditioning on an integer reciprocal family

Date: 2026-10-12T05:09.
Human author Yin.
Provenance: project deduction using the precise retained project and source interfaces.
This organization preserves the ENTIRE original dated author account below.
Its whole-author review is distinct from the actual registered-statement/interface review, which remains pending.

## Statement

Let integers d>=6,a>=2, S_(d,a)=t^d-(a-1)sum_(j=1)^(d-1)t^j+1, F_(d,a)=(t-1)S_(d,a)=t^(d+1)-a t^d+a t-1.
The ORIGINAL degree is d, actual preconditioned degree D=d+1, H_F=2(a+1), and TOTAL m(F)=m(S).
The added zero-measure factor is retained in ALL finite moments; no general irreducibility is assumed.

**A. Complete uniform positive-log tail.**
With circle Haar probability mu, define nu_n(F)=integral(1-|F|^2/H_F^2)^n dmu and T_N(F)=log H_F-(1/2)sum_(n=1)^N nu_n(F)/n.
Put lambda=(a-1)/(a+1), kappa=1/lambda and K_(d,a)=[(d-1)/(d-kappa)]sqrt(pi)/(2lambda).
For ALL integers n,N>=1,

    0<=nu_n(F)<=min{1,K_(d,a)/sqrt(n)},
    0<=T_N(F)-m(S)<=K_(d,a)/sqrt(N)
                         <=5sqrt(pi)/(2sqrt(N))<5/sqrt(N).

Thus N>=max{1,ceil(25/epsilon^2)} suffices for absolute accuracy epsilon>0 simultaneously in d AND a, and m(S)>=T_N(F)-5/sqrt(N).
The exact full-circle phase and its distortion ratio are paid; no circle arc, root or added cyclotomic zero is omitted.

**B. Genuine original-input comparison.**
ONLY on the already adopted actual irreducible genuine-Salem family a=2,d=6n, every valid unchanged-symbol scalar normalization L_d>=max_circle|S| obeys, for0<epsilon<1/4,

    T_N^(L_d)(S)-m(S)<=epsilon
    implies N>=(1/2)[(d-3)^2/4-1]log(1/(4epsilon)).

For fixed C>0 and1<=N<=Cd, its true error is at least (1/2)log[(d-3)^2/(4eCd)], tending to infinity with d.
These are actual errors of the unchanged S estimator; the changed F estimator has the uniform bound A.
This is not a universal improvement theorem for multiplying arbitrary inputs by t-1.

**C. Exact costs and theoretical calibration.**
L379's recurrence evaluates actual moments CT[H_F^2-FF*]^n/H_F^(2n) with D+1=d+2 state integers and O(ND^2) integer operations.
Its paid state/intermediate bit bound is B_N=O((N+1)log(2H_F)+D+log(N+2)+log(D+1)), with conservative bit work O(ND^2 B_N^2), live state O(D B_N), and retained numerator output up to O(N^2 log(2H_F)); input/metadata and actual log H_F enclosures remain additional.
Uniform N is not constant computational cost.
No new native program or exact moment evaluation was run.

Every member of the full a,d domain has a real root in(3/2,a), hence m(S)>log(3/2)>1/3.
The theoretical, UNRUN N=900 consequence is1/6<T_900(F)-1/6<=m(S).
This positivity is deduced using the known real-root interval, not an independently executed certificate or new class gap.

**D. Uniformity boundary.**
The whole class stays away from m=0.
No near-one coverage, short neutral multiplier for arbitrary inputs, unrestricted gap or Task completion is proved.
The previous L18/L28 neutral-completion obstruction and source attribution remain; a later larger-family extension must prove its actual coefficient, degree and phase costs.

## Current assessment
[Selected decision](#decision-sufficient-positive-tail-cost-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T05:09 |
| status | open |
| reason | Register the precise statement and retain the complete original proof and history. The separate whole-author finding covers its exact dated original freeze; actual extraction and interface acceptance remain pending. No unrestricted uniform estimate or Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact registered statement, all hypotheses, actual costs and limitations. |
| argument | [Complete retained argument](#argument) | Entire original author account, all proofs, source/reuse boundaries, costs and freeze. |
| dependency | [Positive-log identity](../ledger/Yin_L_G0378_v1.md#positive-log-moment-identity) | Exact nonnegative expansion and full tail, allowing the retained circle zeros and all factors. |
| dependency | [Exact recurrence costs](../ledger/Yin_L_G0379_v1.md#fast-positive-moment-arithmetic-cost) | Actual D+1-state recurrence, arithmetic, bit, live-state and output accounting. |
| dependency | [Unchanged-symbol true tail](../ledger/Yin_L_G0382_v1.md#necessary-quadratic-coefficient-scale) | Supporting-line tail obstruction at any valid scalar normalization; local adaptation to L is explicitly checked. |
| dependency | [Actual original Salem family](Yin_C_G0022_v1.md#statement) | Only a=2,d=6n irreducibility, true Salem scope and full M(S)<2; general-a phase proof is local. |
| support | [Whole-author finding](../audits/reviews/Yin_R_G0238_v1.md#cyclotomic-positive-tail-whole-finding) | Exact original author freeze only, with the actual registered-statement and interface finding still pending. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T05:16 |
| status | proved |
| reason | Adopt the separately performed whole-author and ACTUAL registered-statement/interface findings at their exact scopes. Preserve complete author arguments, costs, source boundaries and review history; the uniform depth is confined to the declared positive-measure family, and no near-one coverage or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact registered statement, all hypotheses, actual costs and limitations. |
| argument | [Complete retained argument](#argument) | Entire original author account, all proofs, source/reuse boundaries, costs and freeze. |
| dependency | [Positive-log identity](../ledger/Yin_L_G0378_v1.md#positive-log-moment-identity) | Exact nonnegative expansion and full tail, allowing the retained circle zeros and all factors. |
| dependency | [Exact recurrence costs](../ledger/Yin_L_G0379_v1.md#fast-positive-moment-arithmetic-cost) | Actual D+1-state recurrence, arithmetic, bit, live-state and output accounting. |
| dependency | [Unchanged-symbol true tail](../ledger/Yin_L_G0382_v1.md#necessary-quadratic-coefficient-scale) | Supporting-line tail obstruction at any valid scalar normalization; local adaptation to L is explicitly checked. |
| dependency | [Actual original Salem family](Yin_C_G0022_v1.md#statement) | Only a=2,d=6n irreducibility, true Salem scope and full M(S)<2; general-a phase proof is local. |
| support | [Whole-author finding](../audits/reviews/Yin_R_G0238_v1.md#cyclotomic-positive-tail-whole-finding) | Exact original author freeze only; the separate actual registered-statement and interface finding is selected below. |
| review | [Actual independent extraction](../audits/reviews/Yin_R_G0238_v1.md#c41-cyclotomic-tail-extraction-finding) | Exact actual registered statement, full selected argument, present dependency interfaces and complete preservation, checked separately from the earlier whole-author scope. |


### Decision sufficient-positive-log-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:55 |
| status | proved |
| reason | Use the complete sufficient accepted home for the same exact nonnegative expansion and full tail. The mathematical input and scope are unchanged; preserve the actual older author reading, review inputs, all other relations and decisions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact registered statement, all hypotheses, actual costs and limitations. |
| argument | [Exact argument](#argument) | Entire original author account, all proofs, source/reuse boundaries, costs and freeze. |
| dependency | [Exact dependency](Yin_C_G0434_v1.md#positive-log-moment-identity) | Exact nonnegative expansion and full tail, allowing the retained circle zeros and all factors. |
| dependency | [Exact dependency](../ledger/Yin_L_G0379_v1.md#fast-positive-moment-arithmetic-cost) | Actual D+1-state recurrence, arithmetic, bit, live-state and output accounting. |
| dependency | [Exact dependency](../ledger/Yin_L_G0382_v1.md#necessary-quadratic-coefficient-scale) | Supporting-line tail obstruction at any valid scalar normalization; local adaptation to L is explicitly checked. |
| dependency | [Exact dependency](Yin_C_G0022_v1.md#statement) | Only a=2,d=6n irreducibility, true Salem scope and full M(S)<2; general-a phase proof is local. |
| support | [Exact support](../audits/reviews/Yin_R_G0238_v1.md#cyclotomic-positive-tail-whole-finding) | Exact original author freeze only; the separate actual registered-statement and interface finding is selected below. |
| review | [Exact review](../audits/reviews/Yin_R_G0238_v1.md#c41-cyclotomic-tail-extraction-finding) | Exact actual registered statement, full selected argument, present dependency interfaces and complete preservation, checked separately from the earlier whole-author scope. |


### Decision sufficient-integer-state-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:04 |
| status | proved |
| reason | Use the complete sufficient accepted finite-state theorem for the same actual recurrence and all arithmetic/bit/live/output costs. Preserve all other current tuples, exact mathematical scope, old decisions, original author reading and old R238 inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact registered statement, all hypotheses, actual costs and limitations. |
| argument | [Exact argument](#argument) | Entire original author account, all proofs, source/reuse boundaries, costs and freeze. |
| dependency | [Exact dependency](Yin_C_G0434_v1.md#positive-log-moment-identity) | Exact nonnegative expansion and full tail, allowing the retained circle zeros and all factors. |
| dependency | [Exact dependency](Yin_C_G0439_v1.md#fast-positive-moment-arithmetic-cost) | Actual D+1-state recurrence, arithmetic, bit, live-state and output accounting. |
| dependency | [Exact dependency](../ledger/Yin_L_G0382_v1.md#necessary-quadratic-coefficient-scale) | Supporting-line tail obstruction at any valid scalar normalization; local adaptation to L is explicitly checked. |
| dependency | [Exact dependency](Yin_C_G0022_v1.md#statement) | Only a=2,d=6n irreducibility, true Salem scope and full M(S)<2; general-a phase proof is local. |
| support | [Exact support](../audits/reviews/Yin_R_G0238_v1.md#cyclotomic-positive-tail-whole-finding) | Exact original author freeze only; the separate actual registered-statement and interface finding is selected below. |
| review | [Exact review](../audits/reviews/Yin_R_G0238_v1.md#c41-cyclotomic-tail-extraction-finding) | Exact actual registered statement, full selected argument, present dependency interfaces and complete preservation, checked separately from the earlier whole-author scope. |


### Decision sufficient-positive-tail-cost-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:28 |
| status | proved |
| reason | Use the complete sufficient accepted home for exactly the same geometric-mean supporting-line and true-tail accuracy interface. Preserve the local scalar-normalization adaptation, every other tuple/field, original author reading, current review and all old decisions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact registered statement, all hypotheses, actual costs and limitations. |
| argument | [Exact argument](#argument) | Entire original author account, all proofs, source/reuse boundaries, costs and freeze. |
| dependency | [Exact dependency](Yin_C_G0434_v1.md#positive-log-moment-identity) | Exact nonnegative expansion and full tail, allowing the retained circle zeros and all factors. |
| dependency | [Exact dependency](Yin_C_G0439_v1.md#fast-positive-moment-arithmetic-cost) | Actual D+1-state recurrence, arithmetic, bit, live-state and output accounting. |
| dependency | [Exact dependency](Yin_C_G0446_v1.md#necessary-quadratic-coefficient-scale) | Supporting-line tail obstruction at any valid scalar normalization; local adaptation to L is explicitly checked. |
| dependency | [Exact dependency](Yin_C_G0022_v1.md#statement) | Only a=2,d=6n irreducibility, true Salem scope and full M(S)<2; general-a phase proof is local. |
| support | [Exact support](../audits/reviews/Yin_R_G0238_v1.md#cyclotomic-positive-tail-whole-finding) | Exact original author freeze only; the separate actual registered-statement and interface finding is selected below. |
| review | [Exact review](../audits/reviews/Yin_R_G0238_v1.md#c41-cyclotomic-tail-extraction-finding) | Exact actual registered statement, full selected argument, present dependency interfaces and complete preservation, checked separately from the earlier whole-author scope. |

## Argument

The complete author account follows, with only front matter, first-title depth and final whitespace normalized.
Earlier pending/status and contributor paragraphs retain their historical scope.
This registration does not turn a contributor into an independent reviewer or enlarge an accepted source inspection.

## Cyclotomic preconditioning of positive-log moments on a reciprocal integer family

Date: 2026-10-12.
Human author: Yin; delegated g0001_strategies AI AUTHOR inquiry on G0001.
This is a bounded analytic inquiry, not an independent review or a Task conclusion.

## Question and starting scope

Seek an input-uniform positive-log tail after exact cyclotomic preconditioning, rather than reusing the original polynomial's coefficient normalization unchanged.
The initial candidate is the full integer reciprocal family S_(d,a) defined by (t-1)S_(d,a)=t^(d+1)-a t^d+a t-1, with integers a>=2 and d>=6.
Multiplication by t-1 preserves the exact total Mahler measure while changing the circle modulus and finite positive moments.
The a=2,d=6n subfamily is already an ACTUAL irreducible genuine Salem family in C22.
Determine whether the exact circle phase gives a tail bound independent of both d and a for the preconditioned positive moments, retaining degree/state/bit/output costs, the added zero at1, and every original factor.
Compare against the already proved L382 true-tail obstruction for the unpreconditioned dense a=2 inputs.
No near-one coverage or novelty is presumed.

Reuse to inspect: L378/L379/L382/L383, C22's complete degree-one Blaschke phase and original family theorem, and D1's scalar Haar direction boundary.
No native mathematical program, search or J is authorized or run by this allocation.
Substantive proof, useful failure and scope limits will remain here; a separate noncontributor whole review is required before adoption.

<a id="cyclotomic-positive-tail-reuse"></a>
## 1. Actual reuse and method boundary

2026-10-12T04:56.
The author read the responsible [Scalar-Haar formulation](../ledger/Yin_L_G0431_v1.md#regularization-and-direction), [L378 exact positive-log identity](../ledger/Yin_L_G0378_v1.md#positive-log-moment-identity), [L379 finite integer recurrence and all costs](../ledger/Yin_L_G0379_v1.md#fast-positive-moment-arithmetic-cost), [L382 true-tail lower bound](../ledger/Yin_L_G0382_v1.md#necessary-quadratic-coefficient-scale), and [L383 critical-level positive tails](../ledger/Yin_L_G0383_v1.md#trace-density-positive-tail).
L383 already removes the crude root-product complement on individual genuine-Salem inputs; it retains actual derivative/level costs.
The present change is an exact change of polynomial by a specified cyclotomic factor, followed by a full-circle phase estimate.
It does not merely tune those old constants.

The [C22 complete phase count](Yin_C_G0022_v1.md#salem-family-complete-circle-root-count) supplies the actual a=2 family and the elementary degree-one Blaschke-phase mechanism.
Its current adopted [statement](Yin_C_G0022_v1.md#statement) supplies genuine Salem irreducibility, all original roots and 1<M(S_d)<2 ONLY for d=6n.
The general integer a>=2 estimate below does not assume or assert irreducibility.
C22 already attributes the classical Salem-Boyd construction and its exact inspected primary-source scope; no new source read or historical novelty is claimed here.
The general-a derivative is proved below, not imported from an unseen result.

The wider neutral-multiplier idea is old: [C221](Yin_C_G0221_v1.md#neutral-completion) retains the complete original L18 proof of exact Mahler preservation and degree cost, and [L28](../ledger/Yin_L_G0028_v1.md#near-one-quantifiers) fixes the missing existential near-one short-completion gate.
Those records were read after the local preconditioning search.
No uniformly short completion for the unrestricted hard core follows here.
The elementary Gaussian integral, positive-log series and nonnegative tail summation are already proved and attributed in L378/L383.
The argument below directly derives the changed full-circle estimate; no additional external theorem is a mathematical input.

<a id="cyclotomic-positive-tail-statement"></a>
## 2. Exact family, finite estimator and theorem

Let d>=6 and a>=2 be integers.
Define the ORIGINAL monic reciprocal integer polynomial and its specified cyclotomic multiple by

    S_(d,a)(t)=t^d-(a-1)sum_(j=1)^(d-1)t^j+1,
    F_(d,a)(t)=(t-1)S_(d,a)(t)
              =t^(d+1)-a t^d+a t-1.                   (1)

The original degree is d; the actual full preconditioned degree is D=d+1.
Its constant term is-1 and all four displayed coefficients occupy distinct powers.
Therefore

    H_F=sum|F_j|=2(a+1),
    H_S=2+(a-1)(d-1),
    m(F)=m(S).                                        (2)

The last equality is exact multiplicativity, with the actual added factor t-1 of zero Mahler measure.
That factor is not cancelled from the finite moments.
Every original root of S, and the added root1, remains in F.

For n>=1 and N>=1 define

    nu_n(F)=integral_T(1-|F|^2/H_F^2)^n dmu,
    T_N(F)=log H_F-(1/2)sum_(n=1)^N nu_n(F)/n,
    lambda=(a-1)/(a+1), kappa=1/lambda,
    K_(d,a)=[(d-1)/(d-kappa)]sqrt(pi)/(2lambda).        (3)

All logarithms are natural and mu is Haar probability.
These are the actual positive-log moments of F.
They are not the moments of S and no independent phase law is substituted as an equality.

**Theorem.** On the entire integer domain above,

    0<=nu_n(F)<=min(1,K_(d,a)/sqrt(n)),
    0<=T_N(F)-m(S)<=K_(d,a)/sqrt(N)
                       <=5sqrt(pi)/(2sqrt(N))
                       <5/sqrt(N).                   (4)

Consequently, for ANY prescribed epsilon>0, the single integer depth

    N>=max(1,ceil(25/epsilon^2))                       (5)

gives an absolute error at most epsilon simultaneously for every d>=6 and a>=2.
A correctly directed finite lower certificate is

    m(S)>=T_N(F)-5/sqrt(N).                            (6)

Its finite rational moments are exactly evaluable by L379 with actual dimension D+1=d+2, not at constant computational cost.
Neither an original-input root isolation, a minimum circle derivative, a smallest critical value nor an off-circle separation parameter appears in(4).
The full-circle distortion is paid by the explicit ratio in(3).

For the ADOPTED genuine Salem subfamily a=2,d=6n, an accuracy obstruction in the unpreconditioned positive-log estimator changes sharply: every valid scalar normalization L_d>=max_T|S_(d,2)| has, for 0<epsilon<1/4,

    T_N^(L_d)(S)-m(S)<=epsilon
      => N>=(1/2)[(d-3)^2/4-1]log(1/(4epsilon)).       (7)

Here T_N^(L) uses log L and moments(1-|S|^2/L^2)^n.
Thus a fixed scalar normalization of the original symbol, even optimized, requires quadratic-in-d depth for fixed accuracy, while the explicitly changed full symbol in(1) has depth(5) independent of d.
This comparison is across an infinite ACTUAL irreducible genuine Salem family, not merely a reducible padding control.
Its total measures tend tolog2 and remain bounded away from0; it is NOT near-one coverage or a Lehmer counterexample.

<a id="cyclotomic-positive-tail-phase-proof"></a>
## 3. Full-circle phase and distortion, with all zeros retained

Put r=1/a in(0,1/2].
For t=exp(i theta), define

    B_a(t)=(t-r)/(1-r t)=(a t-1)/(a-t).

Its denominator is nonzero on the circle and |B_a(t)|=1.
The real part of1-r exp(i theta) is at least1-r>0, so its continuous argument psi(theta) is defined on[0,2pi], with psi(0)=psi(2pi)=0.
The identity

    B_a(t)=t conjugate(1-r t)/(1-r t)

gives a continuous phase phi(theta)=theta-2psi(theta), with phi(0)=0 and phi(2pi)=2pi.
Direct logarithmic differentiation gives

    phi'(theta)=(1-r^2)/|exp(i theta)-r|^2,
    lambda<=phi'(theta)<=kappa,
    1/3<=lambda<1<kappa<=3.                          (8)

For explicit verification, differentiating the logarithm of B_a(exp(i theta)) gives i[t/(t-r)+r t/(1-r t)]; dividing by i and using |t|=1 reduces it to the first real expression in(8).
Its denominator lies between(1-r)^2 and(1+r)^2, giving the stated bounds.

Define h(theta)=d theta-phi(theta).
Then

    h(0)=0, h(2pi)=2pi(d-1),
    d-kappa<=h'(theta)<=d-lambda,
    d-kappa>=d-3>0.                                  (9)

Thus h is a strictly increasing C1 bijection between these two closed intervals.
For any nonnegative integrable2pi-periodic function f, the ordinary change of variable u=h(theta) gives the completely paid comparison

    (1/(2pi))integral_0^(2pi)f(h(theta))dtheta
       <=[1/(2pi(d-kappa))]integral_0^(2pi(d-1))f(u)du
       =[(d-1)/(d-kappa)]integral_T f(u)du/(2pi).      (10)

This is an inequality with its density distortion, not a claim that h pushes Haar to Haar.
Nonnegative measurable cases follow by monotone approximation, though the function used below is continuous.

The exact polynomial factorization is

    F(t)=(t-a)[t^d-B_a(t)].

Since |t-a|>=a-1 and both terms in the bracket have modulus1,

    |F(exp(i theta))|
      =2|exp(i theta)-a||sin(h(theta)/2)|,
    |F|^2/H_F^2
      >=lambda^2 sin^2(h(theta)/2).                  (11)

The exact upper inequality |F|<=H_F follows from its coefficients, so the original positive moments remain nonnegative.
The zeros in(11) include ALL d-1 circle phase crossings and in particular theta=0, the added t-1 zero.
Their h derivatives are nonzero by(9); no arc is removed and no zero's cost is discarded.
No assertion about the locations or irreducibility of the remaining two roots is needed for this tail bound.

<a id="cyclotomic-positive-tail-gaussian-proof"></a>
## 4. Uniform moments and the complete true tail

Equations(10)--(11) and1-v<=exp(-v),0<=v<=1, imply

    nu_n(F)
      <=[(d-1)/(d-kappa)](1/(2pi))
             integral_(-pi)^pi exp[-n lambda^2 sin^2(u/2)]du.

For |u|<=pi, concavity of sine on[0,pi/2] gives sin(|u|/2)>=|u|/pi.
Enlarge the resulting nonnegative Gaussian integral to the real line to obtain

    (1/(2pi))integral_(-pi)^pi exp[-n lambda^2 sin^2(u/2)]du
      <=(1/(2pi))integral_R exp[-n lambda^2 u^2/pi^2]du
      =sqrt(pi)/(2lambda sqrt(n)).                  (12)

This proves the first bound in(4).
Since d>=6 and kappa<=3,

    (d-1)/(d-kappa)<=(d-1)/(d-3)<=5/3,
    1/lambda<=3,
    K_(d,a)<=5sqrt(pi)/2<5.                           (13)

There are finitely many circle zeros and their logarithmic singularities are integrable.
The L378 nonnegative log expansion applies to F without an irreducibility or squarefree hypothesis and gives

    T_N(F)-m(F)=(1/2)sum_(n>N)nu_n(F)/n.

Use(12) and the elementary integral comparison

    sum_(n>N)n^(-3/2)<=integral_N^infinity x^(-3/2)dx
                       =2/sqrt(N).

Together with(2), this proves the full remainder in(4), hence(5)--(6).
No signed-tail cancellation, root limiting argument or interchange uniform in unbounded d/a is presumed: the bounds hold directly for each pair with the same final constants.

<a id="cyclotomic-positive-tail-original-comparison"></a>
## 5. Actual genuine Salem comparison and a bounded calibration

For a=2,d=6n, C22's adopted original-family theorem gives an actual irreducible genuine Salem polynomial S, total multiplicative measure M(S)=beta_d<2 and all original roots.
Its direct coefficient and endpoint values are

    H_S=d+1, S(1)=3-d.

For ANY allowed scalar normalization L_d>=max_T|S|, therefore L_d>=d-3.
L382's supporting-line proof applies verbatim with L_d in place of H: its only analytic normalization premise is0<=|S|^2/L_d^2<=1, and its geometric mean remains the ORIGINAL M(S).
It gives the necessary accuracy estimate

    N>=(1/2)[L_d^2/M(S)^2-1]log(1/(4epsilon)).

Replacing M(S)^2 by4 and L_d by d-3 weakens that bound and proves(7).
It also gives, for any fixed C>0 and any integer N<=C d,

    T_N^(L_d)(S)-m(S)
      >=(1/2)log[(d-3)^2/(4 e C d)] -> infinity.       (14)

The old divergence is an ACTUAL error of that estimator, not merely a poor geometric bound.
Formula(4) evades it by changing the whole polynomial from S to F, using the actual cyclotomic factor, not by claiming L382 is false or by optimally rechoosing an unchanged scalar normalization.
For this a=2 subfamily, H_F=6 and D=d+1 exactly.

A purely theoretical calibration illustrates the changed finite depth on the entire a>=2,d>=6 domain, without any executed moments.
At x=3/2,

    F_(d,a)(x)=x^d(x-a)+a x-1.

Its derivative with respect to a is x-x^d<0.
At a=2 its value is2-(1/2)(3/2)^d<0 for d>=6.
Hence S_(d,a)(3/2)<0, while

    F_(d,a)(a)=a^2-1>0,
    S_(d,a)(a)=a+1>0.

There is an actual real root beta in(3/2,a).
The polynomial S is monic, so its TOTAL multiplicative measure is at least beta>3/2 irrespective of any other factors.
Consequently m(S)>log(3/2)>1/3, where the last strict inequality follows by integrating1/x>2/3 on[1,3/2).
At N=900, (4) gives a true error less than1/6, so

    1/6<T_900(F)-1/6<=m(S).                            (15)

The left positivity here is proved by the known real-root interval and the uniform error; it is NOT an independently executed or newly discovered numerical Mahler certificate.
The earlier class gap is not the contribution.
The changed contribution is a single finite moment depth with a proved all-degree/all-a conditioning bound, contrasted with(7)--(14) for the actual original genuine Salem inputs.

<a id="cyclotomic-positive-tail-costs-and-limits"></a>
## 6. Exact arithmetic costs and unresolved uniform coverage

All integer coefficients of F are retained.
Each exact moment has the form

    nu_n(F)=CT[H_F^2-F(t)F(t^-1)]^n/H_F^(2n).

L379's nonmonomial recurrence applies with actual span D=d+1, nonzero extreme coefficients1 and-1, and H_F=2(a+1).
It uses D+1=d+2 state integers.
Through depth N its already proved accounting is

    O(N D^2) integer arithmetic operations,
    B_N=O((N+1)log(2H_F)+D+log(N+2)+log(D+1)) bits
        for states and paid intermediate products/divisors,
    O(N D^2 B_N^2) conservative elementary bit operations,
    O(D B_N) live state bits.                          (16)

Retaining all scalar numerators costs up to O(N^2 log(2H_F)) bits; actual input and metadata are additional.
The logarithm log H_F needs its own rational enclosure if an actual numerical certificate is executed, and its approximation error must be added to(4).
For fixed requested epsilon, (5) makes N independent of d and a, while(16) still grows with the original degree and coefficient bit length.
The theorem is not a constant-time evaluation or a native program result.
No new program, solver, moment calculation, scan or J was run.

There is no global domination claim for multiplication by t-1 on an arbitrary input.
It may worsen coefficients, create multiple roots, or lose the phase derivative bounds used here.
The domain in(1) has a real root greater than3/2 and is therefore uniformly separated from the unresolved near-one regime.
Old L18/L28 already identify the general short-neutral-completion issue.
Requiring an unrestricted near-one input to admit this particular two-term-seed phase representation is an unproved coverage assertion; making that assumption would not advance the Task.

This bounded inquiry therefore supplies a concrete full-circle estimate and an actual input-class change in the estimator's conditioning.
A legitimate later extension would identify a larger actual integer input class with a controlled cyclotomic multiplier and paid phase density, while keeping its degree, total measure and coefficient normalization.
Repeating the same a/d family at larger parameters would not address the missing near-one coverage.

## 7. Author self-check and handoff

The author checked: the complete coefficient identity(1), original/preconditioned degree and length, exact zero-measure multiplier; continuous endpoint phase and the derivative sign; distortion ratio in(10) rather than a false Haar invariance; every factor and zero in(11), including the added zero1; sine/Gaussian normalization and the1/2 in the tail; all d/a bounds; strict lower-certificate direction; C22's actual d=6n irreducibility domain; the original L-normalization and geometric-mean use in L382; full integer/state/bit/output/log-enclosure costs; and the fact that(15) is a theoretical calibration rather than a computed output.
The proof uses no numerical experiment or uninspected external theorem.

This is an AUTHOR-complete draft, not independent proof acceptance.
Root supplied the bounded strategy assignment but not this preconditioning target or its phase estimate.
Root arranges a separately organized noncontributor whole review, fixes or retains the result at its actual scope, and owns any route/Claim/navigation update.
G0001's unrestricted uniform gap remains unresolved.

<a id="cyclotomic-positive-tail-whole-author-freeze"></a>
## Entire author freeze

2026-10-12T05:04.
The responsible g0001_strategies AUTHOR freezes the ENTIRE actual Sections1--7 and equations(1)--(16) above, including every hypothesis, proof, calibration, source/dependency boundary, original versus preconditioned comparison and full arithmetic/bit/output cost.
This timestamp records the current whole-author freeze, not an earlier unrecorded event.
No mathematical statement or proof has changed in adding this freeze.
The separately arranged reviewer reconstructs this entire scope and records its own finding; this author freeze is not independent acceptance.

## Registration and preservation operation

2026-10-12T05:09.
The full author account was copied from the responsible working material without abridgment.
Every original argument, example, failed transfer, cost, source boundary and author freeze remains above.
The working address is not retired until actual extraction review, acceptance if warranted, exact preservation comparison and consumer repair are complete.

Meaning-preserving relocation repair: the retained D1 comparison link uses ../drafts/ from this Claim home.
R238 records the initial unresolved locator and the actual recheck; the linked target, proof and mathematical dependency scope are unchanged.
