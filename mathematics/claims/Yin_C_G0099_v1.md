---
author: Yin
---
# Uniform triple-density capture in full squarefree divisor downsets

Date: 2026-10-13T04:59.
Human author Yin.
averaged_lcm authored the entire NEW D23 frozen12:54.
Root independently whole-reviewed it in R337 and NOW authors this fixed statement/extraction, becoming a contributor to the actual wrapper.
The earlier retired use of D23 retained in C96 is a different artifact.
R337 covers this new original only; this wrapper awaits distinct actual extraction review.

## Statement

Let Q be a positive squarefree integer and X>=1 any real number.
Set

    D_Q(X)={a:a divides Q,a<=X},
    W=sum_(a in D_Q(X))phi(a),
    T_X=sum_(a,b,c in D_Q(X),lcm(a,b,c)<=X)phi(a)phi(b)phi(c),
    h(n)=sum_(a in D_Q(X),a divides n)phi(a),
    H_X=max_(integer1<=n<=X)h(n), delta=T_X/W^3,
    N=max{a:a divides Q,a<=X},
    B_Q=product_(p|Q)(1-p^-3)/(1-p^-2)
       =product_(p|Q)(1+1/[p(p+1)]).

All capacities are the full INTEGER phi(a); all triples are ORDERED with repeated labels.
The support is exactly the complete threshold divisor downset, not an arbitrary subcollection or lowered capacity array.
Then

    1<=B_Q<exp(1/2)<2,
    H_X=N,
    T_X<=B_Q H_X W^2,
    (H_X/W)^3<=delta<=min(1,B_Q H_X/W).

Thus delta>=delta0>0 forces H_X/W>=delta0/B_Q>delta0/2, uniformly in Q,X and its prime pool.
Q1, N1, noninteger thresholds and X>=Q are included.
No enlargement of the window is used.

For C96's SAME pair-maximizing array, with K_Q=E_Q(N)/(NW), one has delta<=B_Q/K_Q<2/K_Q.
For C98's SAME third-moment array, with kappa_Q=T/(N^2W),

    N/W<=B_Q/kappa_Q,
    delta<=B_Q^2/kappa_Q<4/kappa_Q.

Consequently both previous diverging-moment sequences have triple density tending to zero; the second bound also strengthens C98's older square-root estimate for N/W.
The earlier stronger-normalization counterexamples remain valid.

C98's actual odd-degree good-2 lift has original degree d=W and therefore the same vanishing root triple density.
For its reciprocal lift deleting mass b<=3, let d=W-b and V be its surviving triple mass.
Then

    V/d^3<=B_Q (N/d)(W/d)^2,
    V/d^3<=(B_Q^2/kappa_Q)(W/d)^3.

C98 supplies d->infinity, W/d->1 and N/d->0, so that ACTUAL reciprocal triple density also tends to zero.
Its full binary depths, chosen X=N window and total m=Theta(d) are unchanged.
No new higher-depth bound is inferred for the odd lift.
These particular controls therefore do not refute capture under a positive UNIFORM triple-density premise.

The finite proof compares the G3 atom law with the intermediate G2 law for gcds of independent squarefree product variables, then uses the elementary event inclusion q2<=q1^2.
Its summable Euler-factor loss is retained explicitly.
The failed direct G3/U comparison and its nonsummable loss are preserved as history.
No new external theorem, native computation or asymptotic prime estimate is used.
The estimate is NOT established for arbitrary capacities, arbitrary actual inventories, near-one coverage or unrestricted G0001.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T04:59 |
| status | open |
| reason | Register full-squarefree-threshold triple capture and the exact vanishing-density consequences for the previous abstract and actual controls. Preserve the complete NEW12:54 D23, failed comparison/source history and whole R337. Root authored this wrapper, which needs a distinct actual extraction review; no unrestricted capacity or near-one theorem is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact full-model result](#statement) | Uniform finite B_Q, real thresholds, exact H, all ordered densities, same-array moment bounds and actual bounded-deletion consequences. |
| argument | [Entire original proof](#argument) | Complete NEW12:54 D23, all seven explicit anchors, equations1--13, failed first comparison, sources and freeze. |
| dependency | [C96 exact law and pair family](Yin_C_G0096_v1.md#averaged-short-lcm-tail-interpretation) | Totient-weighted squarefree product law and same pair-extremal selection, fully rederived finite normalization; no general capacity law. |
| dependency | [C98 actual controls](Yin_C_G0098_v1.md#statement) | Third-moment kappa and finite selection, exact inventories, deleted mass b<=3 and original degree/measure/depth limits. |
| support | [Whole new original review](../audits/reviews/Yin_R_G0337_v1.md#squarefree-density-whole-independent-finding) | Entire NEW12:54 original only, not this later statement/extraction. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-13T05:19 |
| status | proved |
| reason | Adopt R337 original whole review and R339 distinct actual extraction review. The complete squarefree threshold model has T<=B_Q H W^2 with B_Q<2, and the SAME C96/C98 extremal arrays and both actual C98 realizations have triple density tending to zero. Arbitrary capacity arrays, automatic near-one coverage and unrestricted G0001 remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact full-model result](#statement) | Uniform finite B_Q, real thresholds, exact H, all ordered densities, same-array moment bounds and actual bounded-deletion consequences. |
| argument | [Entire original proof](#argument) | Complete NEW12:54 D23, all seven explicit anchors, equations1--13, failed first comparison, sources and freeze. |
| dependency | [C96 exact law and pair family](Yin_C_G0096_v1.md#averaged-short-lcm-tail-interpretation) | Totient-weighted squarefree product law and same pair-extremal selection, fully rederived finite normalization; no general capacity law. |
| dependency | [C98 actual controls](Yin_C_G0098_v1.md#statement) | Third-moment kappa and finite selection, exact inventories, deleted mass b<=3 and original degree/measure/depth limits. |
| support | [Whole new original review](../audits/reviews/Yin_R_G0337_v1.md#squarefree-density-whole-independent-finding) | Entire NEW12:54 original only, not this later statement/extraction. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0339_v1.md#c99-squarefree-density-actual-extraction-finding) | Complete actual statement and preserved argument, all finite and limiting cases, direct source/interfaces and remaining unrestricted scope. |

## Registration and complete preservation

The complete new original follows with only duplicate short frontmatter removed and its first title demoted.
All original history, failed comparison, source limits and seven anchors are retained.
The working draft remains until actual extraction review, adoption, whole-body comparison and exact incoming-locator repair.

## Argument

## Triple-density tails in squarefree divisor downsets

Date: 2026-10-13.
Human author Yin.
A new author inquiry by averaged_lcm under root's active G0001 assignment.
This draft owns only the squarefree-divisor model; the general arbitrary-capacity fixed-density question is assigned separately.

## Question and starting scope

For squarefree Q and a divisor N of Q, let D_Q(N)={a:a divides Q,a<=N}, W=sum_(a in D_Q(N))phi(a), H=N, and T the full ordered totient-weighted triple mass with lcm at most N.
Decide whether T/W^3 can stay bounded below while W/N tends to infinity, especially along the finite moment-extremal selections in C96 and C98.
Seek a uniform nonlinear tail bound or a genuine positive-density counterfamily, keeping abstract order statistics distinct from actual polynomial realization and total Mahler cost.

## Inputs and current status

- [C96 finite pair moments and exact tail model](Yin_C_G0096_v1.md#averaged-short-lcm-tail-interpretation).
- [C98 third-moment obstruction and actual realization limits](Yin_C_G0098_v1.md#direct-triple-finite-moment-obstruction).
- [G0001 unchanged contract](../tasks/Yin_T_G0001_v1.md#contract).

Author exploration started; no candidate theorem or independent review yet.
All useful derivations and failures will remain here.
No native mathematical program has been run.

<a id="squarefree-density-reuse-and-failure"></a>
## Reuse, bounded search and the failed direct comparison

The author read the adopted C96/C98 statements, their exact squarefree moment and tail interfaces, and their current fixed-density limitations.
C96 supplies the finite law of a totient-weighted divisor and the exact H=N identity.
C98 supplies the ordered third moment, its maximizing-divisor family and the bounded deletion of orders1 and3 in the actual reciprocal construction.
No open universal averaged K or uniform linear-in-density estimate from those earlier attempts is used.

A bounded local screen for squarefree tails, product measures, intersection laws and related inequalities in the Claims, ledger, source audits and bibliography returned the existing C96/C98 interfaces and unrelated hypercontractive material; no ready-made tail comparison was located.
A bounded external screen on2026-10-13 used "Jordan totient inequality divisor sum", "divisor closed totient inequality", and "product measure intersection threshold Bernoulli tail inequality".
Returned Jordan-function and matrix/summation leads did not supply an exact checked theorem for the needed quotient.
No external theorem, named correlation inequality, source acquisition or novelty claim enters the proof below.
The finite probability identities are rederived directly from the retained C96 law.

The first natural likelihood comparison was too weak for a uniform conclusion.
If G_k is the gcd of k independent copies of U, where U includes each prime p of squarefree Q with probability1/p, then the atom likelihood of G_3 relative to U contains

    A_Q=product_(p|Q)(1-p^(-3))/(1-p^(-1))
       =product_(p|Q)(1+p^(-1)+p^(-2)).

It gives only delta<=A_Q(N/W)^2.
Along the prime products in C96, A_Q is unbounded by the same elementary reciprocal-prime divergence already used there.
Thus this direct comparison does not supply a uniform tail estimate solely in W/N.
It is not a counterexample to such an estimate.
The successful change is to compare G_3 to G_2 first, then use the exact event inclusion that bounds the G_2 tail by the square of the U tail.
This moves the Euler-factor loss from order1/p to order1/p^2.

<a id="squarefree-density-exact-model"></a>
## 1. Exact finite model and statement

Let Q be a positive squarefree integer, let N be a positive divisor of Q, and put

    D={a:a divides Q, a<=N},
    W=sum_(a in D)phi(a),
    T=sum_(a,b,c divide Q,lcm(a,b,c)<=N)phi(a)phi(b)phi(c),
    delta=T/W^3,
    z=W/N,
    B_Q=product_(p|Q)(1-p^(-3))/(1-p^(-2))
       =product_(p|Q)(1+1/[p(p+1)]).

Every tuple is ORDERED, including every repeated label and diagonal.
The lcm condition implies that all three entries belong to D.
Empty products at Q1 equal1.
Let

    h(n)=sum_(a in D,a divides n)phi(a),
    H_N=max_(integer1<=n<=N)h(n).

Then the following UNIFORM bound holds for every such finite model:

    1<=B_Q<exp(1/2)<2,
    H_N=N,
    T<=B_Q N W^2,
    z^(-3)<=delta<=min(1,B_Q/z).                        (1)

Consequently delta>=delta0>0 implies

    H_N/W=N/W>=delta0/B_Q>delta0/2.                     (2)

In particular no sequence of these squarefree downsets can satisfy W/N->infinity while retaining a positive lower bound for delta.
The statement applies to every chosen divisor N, including but not limited to the finite moment maximizers.
It does not claim that B_Q is optimal or that the same estimate holds for arbitrary capacity arrays.

<a id="squarefree-density-atom-proof"></a>
## 2. Atom comparison and complete proof

Choose A among the divisors of Q with probability phi(A)/Q.
The probabilities sum to1, since

    sum_(a|Q)phi(a)=product_(p|Q)[1+(p-1)]=Q.

The choices whether p divides A are independent, with inclusion probability1-1/p.
Therefore U=Q/A has independent prime inclusions1/p.
Let U_1,U_2,U_3 be independent copies and G_k=gcd(U_1,...,U_k), for k1,2,3, taking G_1=U_1.
Set R=Q/N>=1 and

    q_k=Pr(G_k>=R).

For every k, the prime inclusions in G_k are independent with probability p^(-k).
In particular, for every u dividing Q,

    Pr(G_k=u)=u^(-k) product_(p|Q,p not dividing u)(1-p^(-k)).
                                                               (3)

There are finitely many atoms and every one is positive.
The exact C96 complement identity, extended to three copies, gives

    W=Q q_1,
    T=Q^3 q_3,
    z=R q_1,
    delta=q_3/q_1^3.                                   (4)

Indeed gcd(Q/A_1,...,Q/A_k)=Q/lcm(A_1,...,A_k) for divisors of Q, and lcm<=N is equivalent to G_k>=R.
The condition G_k>=R already implies U_i>=R for every i.
No independence is asserted after conditioning on this tail event.

The first useful bound is the elementary event inclusion

    {G_2>=R} subset {U_1>=R and U_2>=R},
    q_2<=q_1^2.                                        (5)

It holds because a positive gcd is at most each argument, and the two original copies are independent.

Next divide the k3 and k2 atomic formulas in(3).
For every u|Q,

    Pr(G_3=u)/Pr(G_2=u)
       =u^(-1) product_(p|Q,p not dividing u)
                      (1-p^(-3))/(1-p^(-2))
       <=B_Q/u.                                        (6)

Each factor exceeds1, so adjoining the missing present-prime factors only increases the product.
On the finite tail u>=R, (6) is at most B_Q/R.
Summation over precisely these atoms, followed by(5), gives

    q_3<=B_Q q_2/R<=B_Q q_1^2/R.                       (7)

There is no division by a zero tail: q_1>0 because U=Q occurs with probability1/Q and Q>=R.
Substituting(4) into(7) proves T<=B_Q N W^2 and delta<=B_Q/z.

For the uniform constant, every finite prime set satisfies

    log B_Q=sum_(p|Q)log(1+1/[p(p+1)])
           <=sum_(p|Q)1/[p(p+1)]
           <sum_(n=2)^infinity 1/[n(n+1)]=1/2.          (8)

The last series telescopes, and the strict inequality holds even for the empty prime set.
Thus B_Q<exp(1/2)<2.
For example exp(1/2)<2 follows from log2=int_1^2 dx/x>1/2, so no numerical approximation or zeta-value evaluation is required.

The standard finite divisor identity also shows h(n)=gcd(n,Q) for n<=N: every divisor of gcd(n,Q) belongs to D, and its totients sum to that gcd.
Since N divides Q, time n=N gives h(N)=N while h(n)<=n<=N.
This proves H_N=N and W>=N.
Every triple of divisors of N is included in T and has total ordered weight [sum_(a|N)phi(a)]^3=N^3; hence delta>=N^3/W^3=z^(-3).
Finally T<=W^3 gives delta<=1.
Q1 and N1 give W=T=H=1 and satisfy every asserted inequality.
Equations(1)--(2) follow.

<a id="squarefree-density-real-threshold"></a>
## 3. Physical thresholds which are not divisors

For completeness the same capture conclusion holds for any real X>=1 in the squarefree-threshold model.
Put

    N=max{a:a divides Q,a<=X}.

The set is finite and contains1.
Every occurring order and every lcm of divisors of Q is itself a divisor of Q.
Therefore D_Q(X)=D_Q(N), and its ordered compatible triple mass at threshold X equals that at N.
For every integer n<=X, gcd(n,Q) is a divisor of Q no larger than X, hence at most N.
At n=N it equals N.
Thus H_X=N and(1) gives

    T_Q(X)<=B_Q H_X W_Q(X)^2,
    T_Q(X)/W_Q(X)^3<=B_Q H_X/W_Q(X).                   (9)

This replacement uses the largest eligible divisor, not a dilation or change of original weights.
The result concerns exactly the full threshold downset D_Q(X).
An arbitrary subset or arbitrary lowered capacities need not have the product-law tail formulas(3)--(4); they are not covered by this theorem.

<a id="squarefree-density-moment-consequences"></a>
## 4. What the previous moment obstructions permit

For the pair-extremal divisor chosen in C96, write

    K_Q=E_Q(N)/(N W),

where E is its ordered pair mass.
Since E<=W^2, one has z=W/N>=K_Q.
Consequently the PRESENT triple-density theorem gives

    delta<=B_Q/z<=B_Q/K_Q<2/K_Q.                       (10)

Along every C96 sequence with K_Q->infinity, the actual normalized triple density of that same abstract array tends to0.
This now resolves the previously unproved density boundary for that sequence; the unbounded averaged pair ratio and its actual proof remain valid.

For the third-moment maximizing divisor chosen in C98, write

    kappa_Q=T/(N^2 W)=delta*z^2.

Equation(1) now gives the improved finite relations

    kappa_Q<=B_Q*z,
    N/W=1/z<=B_Q/kappa_Q,
    delta<=B_Q^2/kappa_Q<4/kappa_Q.                    (11)

Here kappa_Q>0 because the order1 diagonal is present.
In particular kappa_Q->infinity forces delta->0, and improves C98's previously sufficient N/W<=kappa_Q^(-1/2) to N/W<=B_Q/kappa_Q.
It does not identify an asymptotic value of the maximizer or prove an exact density rate.
The finite lower Euler-product bounds from C96/C98 can be substituted into(10)--(11) if a bound in their prime-product parameters is wanted.

There is no conflict with C98's refutation.
That refuted estimate was

    T<=K X H_X W,

which becomes T<=K N^2 W here.
The PRESENT supported estimate is T<=B_Q N W^2.
It has one fewer factor N and one more factor W; their ratio z=W/N diverges in the counterfamilies.
Equivalently the present positive conclusion H>=delta*W/B_Q does not assert the refuted stronger H>=c*delta*W^2/X.
The original linear-in-density obstruction can therefore coexist with fixed-positive-density capture throughout this squarefree model.

<a id="squarefree-density-actual-family-boundary"></a>
## 5. The retained actual polynomial controls also have vanishing density

C98's actual odd-degree lift realizes the entire full downset inventory with original degree d=W at good prime2.
This theorem therefore applies to its root-count statistics exactly: along its moment-extremal choices,

    T/d^3<=B_Q N/d->0.                                 (12)

No new statement about that lift's unprescribed deeper valuations is inferred.

For C98's reciprocal family, let b<=3 be the mass deleted with orders1 and3, d=W-b the ACTUAL surviving degree, and V its compatible triple mass.
Removing groups cannot increase the nonnegative ordered triple sum, so0<=V<=T.
Thus

    V/d^3 <= B_Q N W^2/d^3
            =B_Q (N/d)(W/d)^2,
    V/d^3 <=(B_Q^2/kappa_Q)(W/d)^3.                    (13)

Along the actual C98 sequence d->infinity, W/d=1+b/d->1 and N/d->0; either form proves V/d^3->0.
All ordered repeats are retained on both sides.
This is an upper bound for the actual surviving triple density, not a claim that deletion preserves a positive density.

The already proved reciprocal all-depth income max_(n<=N)A_2(n)/d->0 and total m(P*)=Theta(d) retain their exact C98 scopes.
The new conclusion closes only their previously unresolved fixed-density boundary: these particular actual controls cannot refute a theorem assuming a positive UNIFORM triple density.
No new realization, local valuation calculation, all-prime norm bound, near-one polynomial, or unrestricted Mahler-gap conclusion is produced.

The remaining question for the separately assigned general inquiry is whether another argument gives a fixed-density capture relation for arbitrary actual root inventories or arbitrary integer-capacity arrays.
The atom ratio and event inclusion above depend on the complete squarefree-threshold inventory.
They cannot simply be asserted after changing its capacities, discarding arbitrary groups, or imposing general Frobenius/reciprocity constraints.
The general G0001 same-exponent income gate remains open.

<a id="squarefree-density-entire-author-freeze"></a>
## Entire author freeze and contribution scope

2026-10-13T04:54.
The author checked the finite probability normalization, complete ordered tuple conventions, all atom factors, event inclusion before conditioning, positive tail denominator, uniform telescoping constant, Q1/N1, largest-divisor threshold reduction, H=N, both directions of the moment comparisons, deletion normalization and actual-control limits.
Root supplied the model inquiry and coordination only; the present author derived the intermediate-second-tail method and all new inequalities.
Earlier C96 is this author's prior work; C98's third-moment and actual realizations are reused as credited fixed inputs, not independently rediscovered.
No mathematical native program, new J, source acquisition, formal assistant or remote operation occurred.
The ENTIRE present original, including the failed direct comparison, equations(1)--(13), source/reuse scope and actual-family boundary, is frozen for separate whole noncontributor review.
No new result is adopted by this author freeze.
