---
author: Yin
---

# Exact integer posterior residuals, nontorsion endpoint nonlinearity and finite corrections

This retains the complete original2026-10-07 [L98 argument](../ledger/Yin_L_G0098_v1.md).
The assigned review_matrix_completion agent authored the direct proof; the coordinator contributed the cubic orthogonal test.
The actual original checks are retained in the formal review linked by L98.
No source, computation or Task is newly executed.

## Statement

Let V be an integer d-by-N matrix of rank d with nonzero columns, xi independent fair signs,Y=V xi,W=VV^T,G=det W and Pi=V^TW^(-1)V.
For a fixed j put a_i=Pi_(j,i),l=Pi_jj,L=sum_i a_i xi_i,b=E[xi_j given Y],R=E(b-L)².
Then E b²=l+R.
For each attained y let c_y count its sign fiber,r_y count its signed j-bias and k_y=D_j L(y),where
D_j=G/gcd(G,v_j^Tadj(W)v_0,...,v_j^Tadj(W)v_(N-1)).
With Q=2^N and C=max c_y<=2^(N-d),

    R=(1/(Q D_j²))sum_y(D_j r_y-k_y c_y)²/c_y.
    If R>0, R>=2/(2^N D_j² C)>=2^(d+1-2N)/D_j².

Exact linear posteriors exist, so positivity cannot be assumed for arbitrary V.
If the columns are pairwise distinct up to sign and l<1, then R>0.
In particular every last endpoint N>d of a nontorsion nonzero algebraic integer power matrix has R>0, with no all-power-degree condition.
Let f(t)=g(sqrt(t)) and D(m) be the retained posterior/fourth-moment comparison.
For that endpoint,

    Delta_N>=f(l+R)>=f(l)+R/2,
    Delta_N>=D(m)+2^(d-2N)/D_j²,
    R>=2^(d+1-2N)N^(-2d)exp[-4(N-1)m].

These are strict finite corrections that can vanish with N and give no positive limiting excess.

For l>0 set s4=sum a_i^4,s6=sum a_i^6,c=(3l²-2s4)/l,T=L³-cL and
D_T=6l³-18l s4+16s6-4s4²/l.
If D_T>0, then R>=gamma3=4(s4-l³)²/D_T and I(xi_j;Y)>=f(l+gamma3),with l+gamma3<=1.
If D_T=0, the numerator is zero and this test assigns gamma3=0.
All entries are rational from Gram minors, without enumerating fibers.
At the first dependent window N=d+1 of a monic irreducible nontorsion integer P with nonzero constant,
L0=sum_(i<d)p_i²>=2,Q0=sum p_i^4 and
l=L0/(L0+1),s4-l³=(Q0-L0³)/(L0+1)^4<0,so the cubic test is strictly positive there.
No later-window or uniform detection is asserted.

Every rank-d real matrix with no zero columns has at least2^d singleton sign fibers.
Consequently, with u=E b² and p0=2^(d-N),

    I(xi_j;Y)>=f(u)+Var(b²)/12
       >=f(u)+(p0/12)(1-u)²
       >=f(l)+(2^(d-N)/12)(1-l)².

This geometric correction is separate from the residual correction and is not added a second time to its D(m) bound.
None of these finite tests proves a lower bound for m-h1 or a correction surviving the entropy-rate limit.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:58 |
| status | open |
| reason | Entire original rational-fiber, nonlinearity, cubic and singleton proofs retained with all finite/limit distinctions; current complete check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Complete exact integer-fiber residual/denominator theorem, sign-distinct and nontorsion endpoint positivity, rational cubic/first-window certificate and singleton Jensen correction, with all explicit constants and vanishing-rate limits. |
| argument | [Complete argument](#argument) | Full original1–12: conditional projection identity, integer denominator and antipodal count, exponential tilting/tanh rigidity, both separate information corrections, Gram cost, sixth moments/zero denominator/first-window and distinct singleton proof. |
| dependency | [Exact posterior and endpoint identities](Yin_C_G0287_v1.md#argument) | Full conditional projection covariance, f convexity, nonzero algebraic-integer endpoint Gram formula and finite Jensen comparison. |
| dependency | [Cubic posterior and D comparison](Yin_C_G0290_v1.md#argument) | Exact mixed fourth moment, Holder and every-time D(m) bound; increasing E b² contributes R/2 without double-counting the separate singleton correction. |
| dependency | [Discriminant/Gram upper bound](Yin_C_G0209_v1.md#gram-lower-certificate) | Exact finite N inequality abs(disc P)G_N<=N^d M(P)^(2(N-1)) and nonzero integer discriminant, used only for the explicit vanishing denominator-cost bound. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:03 |
| status | proved |
| reason | Adopt the entire original exact integer residual, nontorsion endpoint nonlinearity, rational cubic and singleton proofs after actual whole self-review, including every antipodal/denominator/Gram factor and zero-denominator/first-window guard; finite strictness is not a surviving rate correction. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete exact integer-fiber residual/denominator theorem, sign-distinct and nontorsion endpoint positivity, rational cubic/first-window certificate and singleton Jensen correction, with all explicit constants and vanishing-rate limits. |
| argument | [Argument](#argument) | Full original1–12: conditional projection identity, integer denominator and antipodal count, exponential tilting/tanh rigidity, both separate information corrections, Gram cost, sixth moments/zero denominator/first-window and distinct singleton proof. |
| dependency | [Dependency](Yin_C_G0287_v1.md#argument) | Full conditional projection covariance, f convexity, nonzero algebraic-integer endpoint Gram formula and finite Jensen comparison. |
| dependency | [Dependency](Yin_C_G0290_v1.md#argument) | Exact mixed fourth moment, Holder and every-time D(m) bound; increasing E b² contributes R/2 without double-counting the separate singleton correction. |
| dependency | [Dependency](Yin_C_G0209_v1.md#gram-lower-certificate) | Exact finite N inequality abs(disc P)G_N<=N^d M(P)^(2(N-1)) and nonzero integer discriminant, used only for the explicit vanishing denominator-cost bound. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0539_v1.md#current-finite-posterior-finding) | Entire exact current statement, complete retained original argument and all selected interfaces, self-reviewed; original old checks retain only their actual old inputs and exact relationships. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:59 |
| status | proved |
| reason | Adopt the actual fresh complete mathematical review, formed before the full old-account comparison, at every original statement/proof/necessary-input boundary. Preserve all old decisions and self/unknown facts; no substantive repair, source-depth expansion or unrestricted completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete exact integer-fiber residual/denominator theorem, sign-distinct and nontorsion endpoint positivity, rational cubic/first-window certificate and singleton Jensen correction, with all explicit constants and vanishing-rate limits. |
| argument | [Argument](#argument) | Full original1–12: conditional projection identity, integer denominator and antipodal count, exponential tilting/tanh rigidity, both separate information corrections, Gram cost, sixth moments/zero denominator/first-window and distinct singleton proof. |
| dependency | [Dependency](Yin_C_G0287_v1.md#argument) | Full conditional projection covariance, f convexity, nonzero algebraic-integer endpoint Gram formula and finite Jensen comparison. |
| dependency | [Dependency](Yin_C_G0290_v1.md#argument) | Exact mixed fourth moment, Holder and every-time D(m) bound; increasing E b² contributes R/2 without double-counting the separate singleton correction. |
| dependency | [Dependency](Yin_C_G0209_v1.md#gram-lower-certificate) | Exact finite N inequality abs(disc P)G_N<=N^d M(P)^(2(N-1)) and nonzero integer discriminant, used only for the explicit vanishing denominator-cost bound. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0539_v1.md#current-finite-posterior-finding) | Entire exact current statement, complete retained original argument and all selected interfaces, self-reviewed; original old checks retain only their actual old inputs and exact relationships. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0547_v1.md#f-g292) | Entire actual statement and complete original proof independently inspected, with exact domains, all useful old whole/partial obligations, original source-depth, failed comparisons, costs and limit order; no new mathematical experiment or reconstructed historical isolation. |


## Complete retained argument

<a id="argument"></a>
Let V be an integer d-by-N matrix of rank d, with nonzero columns v_i.
Let xi_i be independent fair signs, Y=V xi, W=VV^T, G=det W, and Pi=V^T W^(-1)V.
For one index j write

    a_i=Pi_(j,i),  l=Pi_(j,j),  L=sum_i a_i xi_i,
    b=E[xi_j | Y],  R=E[(b-L)^2].

The retained covariance calculation, or E[bL]=E[xi_j L]=l and E L^2=l, gives the exact identity

    E b^2=l+R.                                          (1)

Here L is Y-measurable.
Put g(x)=((1+x)/2)log(1+x)+((1-x)/2)log(1-x), f(t)=g(sqrt(t)).
Then I(xi_j;Y)=E g(b), f is increasing and convex, and f'(t)>=1/2 where defined.

<a id="integer-fiber-posterior-separation"></a>
### 1. An exact rational residual and its finite minimum

For each attained y let c_y be its number of sign words and r_y the number having xi_j=1 minus the number having xi_j=-1.
Let D_j be the least positive integer such that every D_j a_i is integral.
It divides G, since W^(-1)=adj(W)/G.
More explicitly, if n_i=v_j^T adj(W)v_i, then

    D_j=G/gcd(G,n_0,...,n_(N-1)).

The value of D_j L on a fiber is an integer k_y.
With Q=2^N and C=max_y c_y we have

    b(y)=r_y/c_y,
    R=(1/(Q D_j^2)) sum_y (D_j r_y-k_y c_y)^2/c_y,
    C<=2^(N-d).                                        (2)

For the last inequality choose any d independent columns: fixing all other signs leaves at most one possible choice on those d columns for a given output.
Thus (2) is an exact rational certificate using integer fiber counts and integer Gram minors.

If R>0, some integer numerator in (2) is nonzero.
Sign reversal pairs that fiber with -y, with the same count and opposite numerator.
At y=0 both b and L are zero by sign symmetry, so this nonzero pair consists of two distinct fibers.
Consequently

    R>=2/(2^N D_j^2 C)>=2^(d+1-2N)/D_j^2.              (3)

Without a separate reason for R>0, (3) is only a conditional separation.
Exact linear posteriors exist: for V=(1,...,1), all b_j equal L_j=(xi_0+...+xi_(N-1))/N.

<a id="nontorsion-endpoint-posterior-nonlinearity"></a>
### 2. Exact nonlinearity for the nontorsion orbit endpoint

Suppose the columns of V are pairwise different up to sign.
If b=L almost surely, multiplication by exp(w dot Y) and conditional expectation give, for every real w,

    tanh(w dot v_j)=sum_i a_i tanh(w dot v_i).           (4)

Indeed both sides arise after dividing the corresponding expectations by the strictly positive product of the cosh(w dot v_i).

Choose w_0 outside the finitely many hyperplanes on which a column evaluates to zero or two column evaluations agree up to sign.
The numbers |w_0 dot v_i| are then positive and distinct.
The functions tanh(c_i s), for distinct positive c_i, are linearly independent over R: in any putative linear relation take s to infinity to remove its constant term, multiply the remaining relation by exp(2 c_min s), and use tanh(c s)-1=-2exp(-2cs)+o(exp(-2cs)) to force the coefficient of the smallest c to vanish.
Repeat for the remaining terms.
Negative c_i only change their coefficient signs.

Applying this to (4) forces a_i to be 1 for i=j and 0 otherwise.
In particular l=1.
Thus

    pairwise sign-distinct columns and l<1 imply R>0.   (5)

For the power matrix v_i=t^i mod P of a nontorsion nonzero algebraic integer alpha, the sign-distinctness holds: equality would say alpha^(i-j)=+/-1.
For the last column at N>d, the preceding N-1 columns already span, and the determinant formula gives 0<l=1-G_(N-1)/G_N<1.
Therefore (3) applies to every such endpoint.
No all-power degree-preservation hypothesis is needed.

By (1) and Jensen,

    Delta_N>=f(l+R)>=f(l)+R/2.                           (6)

The L G0097 fourth-moment argument also retains its full fourth-moment term when E b^2 is increased from l to l+R.
Writing F(l)=l/2+l^2(3-2l)^4/324 and using that record's notation D(m)=max(f(1-exp(-2m)),F(1-exp(-2m))), we obtain

    Delta_N>=D(m)+2^(d-2N)/D_j^2,    N>d.               (7)

This is a strict finite inequality.
It is not a positive excess for the entropy rate.
For example, the retained discriminant/Gram bound and |disc P|>=1 give the explicit but vanishing lower separation

    R>=2^(d+1-2N) N^(-2d) exp[-4(N-1)m].               (8)

The right side tends to zero with N.
Replacing the exact denominator by the uniform estimate does not remove that cost.
The earlier finite integer-log comparisons of L G0092 remain valid, but exact decidability at a fixed N must not be promoted to a rate inequality by ignoring this dependence.

<a id="cubic-orthogonal-posterior-certificate"></a>
### 3. A stronger computable test can avoid enumerating fibers

The coordinator proposed a particular nonlinear statistic whose projection cost is exactly calculable from the rational row a.
Suppose l>0 and put

    s4=sum_i a_i^4,  s6=sum_i a_i^6,
    c=(3l^2-2s4)/l,   T=L^3-cL.

Fair-sign expansions give

    E L^4=3l^2-2s4,
    E L^6=15l^3-30l s4+16s6,
    E[LT]=0,
    E[bT]=2(s4-l^3),
    D_T=E T^2=6l^3-18l s4+16s6-4s4^2/l.               (9)

The sixth-moment formula follows by grouping the surviving terms into index multiplicity patterns 6, 4+2 and 2+2+2.
For the mixed identity use E[b L^3]=E[xi_j L^3]=3l^2-2l^3 and E[bL]=l.
Since T is Y-measurable and orthogonal to L, Cauchy--Schwarz gives

    R>=gamma_3:=4(s4-l^3)^2/D_T  if D_T>0,
    I(xi_j;Y)>=f(l+gamma_3).                            (10)

If D_T=0, T vanishes almost surely and the numerator in (10) is zero; assign gamma_3=0 for this test.
Every number in (9)--(10) is rational and computable from Gram minors without enumerating the 2^N words.
Also l+gamma_3<=1 follows from the proved projection inequality, rather than being an extra numerical assumption.

The test need not detect every nonlinearity: no claim that s4 differs from l^3 at every orbit window is made.
There is an exact first-window check.
At N=d+1 write P(t)=t^d+sum_(i<d)p_i t^i and set L_0=sum_(i<d)p_i^2, Q_0=sum_(i<d)p_i^4.
The one-dimensional relation space gives

    l=L_0/(L_0+1),
    s4-l^3=(Q_0-L_0^3)/(L_0+1)^4.                      (11)

For a monic irreducible nontorsion integer P with nonzero constant coefficient, L_0>=2: the excluded case L_0=1 is t^d+/-1.
Since Q_0<=L_0^2<L_0^3, this test is strictly positive at that first dependent window.
This finite fact supplies neither a uniform positive limiting residual nor a bound on the later windows where increments approach their rate.

<a id="singleton-cube-fiber-correction"></a>
### 4. Some finite strictness already comes from cube geometry

There are at least 2^d singleton output fibers for any rank-d real matrix with no zero columns.
Choose d independent columns.
Their hyperplanes divide the dual space into 2^d nonempty open sign regions.
In each region choose a functional nonzero on every other column.
Maximizing that functional over the sign cube has one unique sign word, so its output fiber is a singleton.
The selected regions give different sign words on the independent columns.
If two such words had the same output, both would maximize the functional chosen for the first word, contradicting its uniqueness.
Thus the selected outputs are distinct.

Thus for the law of U=b^2, its mass at 1 is at least p_0=2^(d-N).
The positive series for f shows that f(t)-t^2/12 is convex on [0,1].
Writing u=E b^2, we get

    I>=f(u)+Var(b^2)/12
      >=f(u)+(p_0/12)(1-u)^2
      >=f(l)+(2^(d-N)/12)(1-l)^2.                       (12)

For the last step, the function f(u)+(p_0/12)(1-u)^2 is increasing: its derivative is at least 1/2-p_0/6>=1/3.
This proves strictness when l<1, even without arithmetic or sign-distinct columns.
It is deliberately separated from (3) and (5).
Its coefficient again decays exponentially with the codimension N-d, so it is not a uniform posterior spread estimate at arbitrarily long times.

### Actual consequence and review boundary

These are three distinct finite inputs: an exact integer-fiber residual formula, nonlinearity forced by the nontorsion orbit, and a rational cubic test that can certify a larger residual in a given row.
The singleton correction is an additional purely geometric control.
They strengthen finite lower certificates for increments.
None is a lower bound on m-h_1, and none proves that a positive correction to L G0097 survives N tending to infinity.
The explicit upper time currently available for approaching m also carries its own d,N error; it cannot be replaced by a claim that a positive finite residual persists at the rate.
