---
author: Yin
---

# Sharp independent-translation Shannon cost, cosets and binary finite-time limits

This retains the complete original2026-10-07 [L95 proof](../ledger/Yin_L_G0095_v1.md), authored by assess_shortness_route for Yin.
The [original R26](../audits/reviews/Yin_R_G0026_v1.md#contribution-and-actual-review-scope) owns the actual old whole checks and their exact recorded context.
No source, computation or Task is newly executed.
The exact algebraic-unit orbit has additional structure beyond these generic independent translations.

## Statement

Let Lambda be a free abelian group of finite rank, let v1,...,vr be Z-linearly independent elements, and let X have a finite probability law mu on Lambda.
Put L=sum_i Z v_i,C=X mod L and epsilon_i=TV(mu,tau_(v_i)mu), with TV half the l1 distance and natural-log entropy.
Each epsilon_i>0, and

    H(X)>=H(C)+sum_i log(1/epsilon_i),
    log|supp mu|>=H(C)+sum_i log(1/epsilon_i).

L may be nonprimitive or not full rank, and no independence between the coset fiber coordinates is assumed.
For independent uniform box coordinates of side Li>=1, independent of any finitely supported coset variable C, epsilon_i=1/Li and the Shannon bound is an equality.
For a single coset the support bound is also an equality.
When Li=2^si, the box is a fair binary sum with weights2^j v_i, without asserting consecutive powers of one algebraic unit.
Thus no additional r log r follows from independent translations alone.

For arbitrary finite laws these hypotheses imply no dimension-proportional min/collision lower bound.
For0<epsilon<1,theta=epsilon/2 and a uniform d-dimensional integer box law u_L with L>=ceil(2/epsilon) containing zero,
mu=theta delta0+(1-theta)u_L has every coordinate translation error at most epsilon, yet H_infinity<=log(2/epsilon) and H2<=2log(2/epsilon), independently of d.
This law is not asserted to be a fair-bit sum.
On the fair-bit subclass, the retained half-Shannon comparison supplies the corresponding half of the displayed Shannon bound.

For an algebraic unit alpha of degree d and0<m=log M(alpha)<1/4, the actual centered binary law with basis translation errors at most2sqrt(m) obeys

    (d/2)log(1/m)-dlog2<=H(nu)<=log|supp nu|<8dlog(8d/m)+2m.

These bounds are compatible and supply no Mahler gap.
For the actual decreasing binary entropy increments Delta_k and N=k+d-1,

    Delta_k>=(1/2)exp[-2(k+d-1)log2/d],
    Delta_k>=(1/(32N²))exp[-2(N-1)m/d].

For k<=d the exact stronger identity is Delta_k=log2.
Thus Delta_k<=delta with delta>0 requires k>=d log(1/(2delta))/(2log2)-d+1.
The separately proved posterior bound k>=1/2+d/(4delta) for0<delta<log2 is stronger.
All these are necessary finite-time costs, not lower bounds for the limit of Delta_k, and do not exclude the compatible small-positive-m resource scenario.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:45 |
| status | open |
| reason | Full original sharp finite-law, control and binary finite-time proof retained; current complete checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire sharp arbitrary finite-law independent-translation Shannon/support theorem with nonprimitive cosets, box/fair-bit equalities, min/collision countercontrol, actual binary resource comparison and both finite-time increment inequalities. |
| argument | [Complete argument](#argument) | Full original1–10: finite-line variation, conditional fiber guessing and entropy chain, all sharpness/countercontrols, power-basis covered-window constants, norm-grid corollary and stronger posterior comparison with every arithmetic/limit boundary. |
| dependency | [Actual binary affine/time proof](Yin_C_G0283_v1.md#effective-binary-near-invariance-time) | Exact unit-domain centered law, basis translation errors, support cost and one-sided punctured marginal estimates; no universal small-Mahler family or uniform convergence is assumed. |
| dependency | [Full norm-grid bound](Yin_C_G0281_v1.md#norm-grid-support-bound) | Exact every-N algebraic-integer support bound(4N)^d exp((N-1)m), used for the alternative finite increment constant. |
| dependency | [Fair-group entropy comparison](Yin_C_G0280_v1.md#abelian-binary-entropy-comparison) | Only the additional fair-bit H_infinity/H2 at least half Shannon, not a property of arbitrary finite mixture laws. |
| support | [Stronger posterior rank/time theorem](Yin_C_G0287_v1.md#punctured-information-time-cost) | Exact separately proved k>=1/2+d/(4delta) for a binary increment at most0<delta<log2; comparison only, not a premise of the sharp translation theorem. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:51 |
| status | proved |
| reason | Adopt the complete original sharp nonprimitive-coset translation theorem, fair and arbitrary-law controls and binary finite-time/resource comparison after actual whole self-review; these necessary costs supply no positive entropy-rate or Mahler gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire sharp arbitrary finite-law independent-translation Shannon/support theorem with nonprimitive cosets, box/fair-bit equalities, min/collision countercontrol, actual binary resource comparison and both finite-time increment inequalities. |
| argument | [Argument](#argument) | Full original1–10: finite-line variation, conditional fiber guessing and entropy chain, all sharpness/countercontrols, power-basis covered-window constants, norm-grid corollary and stronger posterior comparison with every arithmetic/limit boundary. |
| dependency | [Dependency](Yin_C_G0283_v1.md#effective-binary-near-invariance-time) | Exact unit-domain centered law, basis translation errors, support cost and one-sided punctured marginal estimates; no universal small-Mahler family or uniform convergence is assumed. |
| dependency | [Dependency](Yin_C_G0281_v1.md#norm-grid-support-bound) | Exact every-N algebraic-integer support bound(4N)^d exp((N-1)m), used for the alternative finite increment constant. |
| dependency | [Dependency](Yin_C_G0280_v1.md#abelian-binary-entropy-comparison) | Only the additional fair-bit H_infinity/H2 at least half Shannon, not a property of arbitrary finite mixture laws. |
| support | [Support](Yin_C_G0287_v1.md#punctured-information-time-cost) | Exact separately proved k>=1/2+d/(4delta) for a binary increment at most0<delta<log2; comparison only, not a premise of the sharp translation theorem. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0537_v1.md#current-sharp-translation-finding) | Entire exact current statement, complete retained original argument and every selected interface, self-reviewed; old findings keep only their actual fixed inputs and exact relationship scopes. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:59 |
| status | proved |
| reason | Adopt the actual fresh complete mathematical review, formed before the full old-account comparison, at every original statement/proof/necessary-input boundary. Preserve all old decisions and self/unknown facts; no substantive repair, source-depth expansion or unrestricted completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire sharp arbitrary finite-law independent-translation Shannon/support theorem with nonprimitive cosets, box/fair-bit equalities, min/collision countercontrol, actual binary resource comparison and both finite-time increment inequalities. |
| argument | [Argument](#argument) | Full original1–10: finite-line variation, conditional fiber guessing and entropy chain, all sharpness/countercontrols, power-basis covered-window constants, norm-grid corollary and stronger posterior comparison with every arithmetic/limit boundary. |
| dependency | [Dependency](Yin_C_G0283_v1.md#effective-binary-near-invariance-time) | Exact unit-domain centered law, basis translation errors, support cost and one-sided punctured marginal estimates; no universal small-Mahler family or uniform convergence is assumed. |
| dependency | [Dependency](Yin_C_G0281_v1.md#norm-grid-support-bound) | Exact every-N algebraic-integer support bound(4N)^d exp((N-1)m), used for the alternative finite increment constant. |
| dependency | [Dependency](Yin_C_G0280_v1.md#abelian-binary-entropy-comparison) | Only the additional fair-bit H_infinity/H2 at least half Shannon, not a property of arbitrary finite mixture laws. |
| support | [Support](Yin_C_G0287_v1.md#punctured-information-time-cost) | Exact separately proved k>=1/2+d/(4delta) for a binary increment at most0<delta<log2; comparison only, not a premise of the sharp translation theorem. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0537_v1.md#current-sharp-translation-finding) | Entire exact current statement, complete retained original argument and every selected interface, self-reviewed; old findings keep only their actual fixed inputs and exact relationship scopes. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0545_v1.md#f-g289) | Entire actual statement and complete original proof independently inspected, with exact domains, all useful old whole/partial obligations, original source-depth, failed comparisons, costs and limit order; no new mathematical experiment or reconstructed historical isolation. |


## Complete retained argument

<a id="argument"></a>
<a id="sharp-independent-translation-entropy"></a>
### A finite-law inequality with its coset term

Let Lambda be a free abelian group of finite rank, let v_1,...,v_r be Z-linearly independent elements, and put L=sum_i Z v_i.
Let X have a finite probability law mu on Lambda.
Write C for its coset in Lambda/L and

    epsilon_i=TV(mu,tau_(v_i)mu),    1<=i<=r.

Then every epsilon_i is positive, and

    H(X)>=H(C)+sum_(i=1)^r log(1/epsilon_i),
    log|supp mu|>=H(C)+sum_i log(1/epsilon_i).             (1)

All entropies use natural logarithms.
Thus if all errors are at most epsilon in (0,1], the cost is at least H(C)+r log(1/epsilon).
The group L need not be primitive or have full rank.
In particular independent translations need not form a basis of Lambda.
The coset variable is retained rather than incorrectly identifying all of Lambda with L.

Here is a direct proof.
For a finite probability law p on Z, extend its masses by zero and let a be a location of maximum mass.
Telescoping up to a and after a gives

    (1/2)sum_j |p(j)-p(j-1)|>=max_j p(j).                 (2)

Both telescoping sums are finite, and each is at least the maximum mass.
Conditional on a coset C=c, choose one coset representative and express X uniquely as that representative plus sum_i Y_i v_i.
All coordinate laws occurring have finite support.
Conditioning on (C,Y_(minus i)) separates disjoint integer lines, and translation by v_i preserves each line.
Consequently

    epsilon_i=E[TV(law(Y_i|C,Y_(minus i)),
                         its unit translate)]
      >=E[max_j P(Y_i=j|C,Y_(minus i))]=:g_i.             (3)

Every nonempty conditional law has a positive maximum mass.
Its Shannon entropy is at least minus the logarithm of that mass.
Jensen's inequality for -log then gives

    H(Y_i|C,Y_(minus i))>=-log g_i>=-log epsilon_i.         (4)

Finally the entropy chain rule and the fact that conditioning reduces entropy imply

    H(X)-H(C)=H(Y_1,...,Y_r|C)
      =sum_i H(Y_i|C,Y_1,...,Y_(i-1))
      >=sum_i H(Y_i|C,Y_(minus i)).                       (5)

Equations (3)--(5) prove the Shannon bound, and H(X)<=log|supp mu| proves the other bound.
These arguments also show epsilon_i>0; a finite nonzero law cannot be invariant under an infinite-order translation.
No independence between the Y_i is assumed.

<a id="sharp-box-and-fair-bit-controls"></a>
### Sharpness and the entropy-order boundary

For integers L_i>=1, take independent Y_i uniform on {0,...,L_i-1}, independent also of any finitely supported coset variable C.
Define X using fixed representatives as above.
Counting one-dimensional interval intersections gives exactly

    epsilon_i=1/L_i,
    H(X)=H(C)+sum_i log L_i.                              (6)

Thus the Shannon bound in (1) is attained, including its dimension coefficient and its treatment of nonbasis shifts.
For one coset, the support bound is also an equality.
There is no unavoidable additional r log r cost in a bound based only on these independent translations.

If each L_i=2^(s_i), the one-coset example is itself the fair binary sum

    X=sum_i sum_(j=0)^(s_i-1) xi_(i,j) 2^j v_i,

with independent fair bits.
This proves sharpness even with fairness of the input retained.
The displayed weights are not asserted to be consecutive powers of one algebraic unit.
That distinction is exactly the extra structure unavailable to a translation-only cost argument.

For arbitrary finite laws, (1) must not be silently upgraded to a dimension-proportional min-entropy or collision-entropy bound.
Fix epsilon in (0,1), let theta=epsilon/2, and let u_L be uniform on a d-dimensional integer box of side L>=ceil(2/epsilon) containing zero.
The law

    mu=theta delta_0+(1-theta)u_L

satisfies TV(mu,tau_(e_i)mu)<=theta+(1-theta)/L<=epsilon in every coordinate, yet its largest atom is at least theta.
Hence H_infinity(mu)<=log(2/epsilon) and H_2(mu)<=2log(2/epsilon), independently of d.
This does not contradict (1), which concerns Shannon and support entropy.

For the actual fair binary laws of G0001, the additional comparison in [C280](Yin_C_G0280_v1.md#abelian-binary-entropy-comparison) does give H_infinity>=H_1/2 and H_2>=H_1/2.
Thus on that subclass half of (1)'s Shannon lower bound also holds for these two entropies.
The arbitrary mixture just displayed is not claimed to belong to that subclass.

<a id="translation-cost-versus-binary-resource-bound"></a>
### Comparison with the actual binary resource bound

For an algebraic unit alpha of degree d, the shifts 1,alpha,...,alpha^(d-1) form an integral basis of O=Z[alpha].
There is no coset term.
In the notation of [C283](Yin_C_G0283_v1.md#effective-binary-near-invariance-time), let 0<m=log M(alpha)<1/4 and take its centered binary law nu.
Its covered power window contains this basis, and its errors are at most 2sqrt(m).
Equations (1) and L G0092 therefore give

    (d/2)log(1/m)-d log2
       <=H(nu)<=log|supp nu|
       <8d log(8d/m)+2m.                                (7)

The lower and upper bounds are compatible as m tends to zero, even before allowing the degree to grow.
The basis-translation test hence gives no contradiction to L G0092's hypothetical near-zero scenario.
The exact examples (6) rule out improving the generic lower cost beyond r log(1/epsilon) on these hypotheses alone.
They are not examples of small positive Mahler measure or of the same cyclic binary law.

This comparison does not prove that no other argument can use the much longer power window, multiplication by alpha, or the special binary history.
It isolates what is already fully accounted for by d independent translations and their Shannon or support cost.

<a id="translation-cost-finite-increment-corollary"></a>
### A finite-time increment corollary, not an entropy-rate bound

There is also an elementary finite-time consequence of (1).
Let Delta_k be the decreasing increments from L G0092 and put N=k+d-1.
For 0<=j<d, its one-sided punctured marginal bound and convolution contraction give

    TV(mu_N,tau_(alpha^j)mu_N)
       <=sqrt(2 Delta_(N-j))<=sqrt(2 Delta_k).

Using (1) and H_N<=N log2 yields

    Delta_k>=(1/2)exp[-2(k+d-1)log2/d].                   (8)

This remains valid if sqrt(2Delta_k)>1, since then the intermediate entropy lower bound is merely nonpositive.
For k<=d one has the stronger exact identity Delta_k=log2.
In particular a uniform time k<=C d has an explicit positive increment lower bound.
A requested Delta_k<=delta entails

    k>=(d/(2log2))log(1/(2delta))-d+1.                    (9)

The norm-grid bound of [C281](Yin_C_G0281_v1.md#norm-grid-support-bound) can be substituted for N log2 in the same argument, giving the alternative finite inequality

    Delta_k>=(1/(32N^2))exp[-2(N-1)m/d],   N=k+d-1.        (10)

These are costs of making a particular finite increment small, not a lower bound for its limit as k tends to infinity.
The separately proved [posterior-covariance argument](Yin_C_G0287_v1.md#punctured-information-time-cost) gives the stronger necessary condition k>=1/2+d/(4delta) when Delta_k<=delta<log2, using the actual binary bits rather than only a law's translation invariance.
Equations (8)--(10) are retained as consequences of the sharp translation-cost theorem, not as that stronger argument or as a proposed substitute for it.

The remaining question is arithmetic: additional information about the whole orbit and multiplication must improve on the compatible resource window (7), or otherwise prohibit the specific binary approximate invariants.
Neither qualitative amenability nor its sharp independent-coordinate entropy cost alone establishes the Lehmer gap.
