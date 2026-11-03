---
author: Yin
---

# Complete mass-scaled cyclotomic capture, efficient-order fragmentation and circle cost

The complete original L221 Sections 1--6/(1)--(26) are retained, including bad/index primes, original multiplicities, every cyclotomic complement, the explicit modulus inversion and the full lifted degree.
The original [R791 whole](../audits/reviews/Yin_R_G0791_v1.md#order-auxiliary-complete-independent-review) retains its 2026-10-09T21:39 review of the original 21:32 frozen argument, all conclusions and source scope.
Its checkpoint/common-context account does not establish the actual additional mathematics or initial order; no later C binding or relationship declaration is inserted into that old finding.

## Statement

<a id="order-auxiliary-fixed-scope"></a>

Let P in Z[t] be any monic irreducible nontorsion unit polynomial, d=deg P, m=log M(P)>0, and C_n=|Res(P,t^n-1)| for n>=1.
Fix a prime p and factor its complete reduction as Pbar=product_phi phi^(e_phi).
For every occurring p-free root order o put
\[
f_o=\operatorname{ord}_o(p),\ f_1=1,\quad
w_o=\sum_{\phi\ {\rm of\ order}\ o}e_\phi f_o,\quad
E_o=\max_{\phi\ {\rm of\ order}\ o}e_\phi,\quad
k_o=\lceil\log_p E_o\rceil,\quad r_o=k_o+1,\quad N_o=o p^{r_o}.
\]
All maxima concern occurring factors; repeated reduction, ramification and power-basis index primes are included.
Choose a nonempty set O of occurring orders with o/f_o<=B, where B>=1, and put W=sum_(o in O)w_o, Gamma=W/d.
Define
\[
H(t)=\prod_{o\in O}\Phi_o(t^{p^{r_o}}),\quad
D=\sum_{o\in O}\phi(o)p^{r_o},\quad
\mathcal C=\max_{|t|=1}|H(t)|.
\]
Then H is monic integral squarefree cyclotomic over Q, M(H)=1, and
D<=sum_o N_o<=p^2 B W.
Squarefree reduction modulo p is not asserted.

Normalize each original root valuation by v(p)=1.
Its individual local ramification index e satisfies e<=e_phi<=E_o; this does not identify reduction multiplicity with e or bound splitting-field ramification.
For
\[
V_o=\sum_{\operatorname{ord}(\bar\alpha_i)=o}v(\alpha_i^{N_o}-1)
\]
one has V_o>=2w_o, and for every integer n>=1 its full original-root contribution A_o(n) satisfies
\[
A_o(n)\le(\log p)V_o+w_o\log^+(n/N_o)
 \le(\log p)V_o+w_o\log^+(n/w_o).
\]
The value is zero unless o divides n; after capture each additional p-power adds exactly w_o to the sum of valuations.
The exact auxiliary norm is
\[
v_p Res(P,H)=\sum_{o\in O}V_o,\quad
\log|Res(P,H)|\ge2W\log p.
\]
For G=product_o(t^(N_o)-1) and J=G/H, J is an integral cyclotomic product, retaining repeated factors,
deg G=sum N_o, deg J=sum N_o-D, and
product_o C_(N_o)=|Res(P,H)| |Res(P,J)|.
Both norms are nonzero integers; the complementary norm may not be deleted from that equality.
This is one auxiliary resultant, not one common-time cyclic norm.

Use the fixed C504 modulus
\[
c=\log2/4,\ h_0=ce^{-20},\quad
b(h)=\max(h,\sqrt{h/c}\log\sqrt{c/h}),\quad
\Omega(h)=19b(h)^{1/6},\quad0<h\le h_0.
\]
Put a=p^2 Bm and gamma_o=w_o/d.
If 0<a<=h_0, then
\[
2\gamma_o\log p\le(\log p)V_o/d\le\Omega(a\gamma_o),\quad
A_o(n)/d\le\Omega(a\gamma_o)+\gamma_o\log^+(n/(d\gamma_o)).
\]
With K_0=max(1,(2sqrt(c))^(-1)), K=19K_0^(1/6)/(2log2), define
\[
\chi(a)=\min\{1,\max\{a,[K^{12}a(1+2\log(1/a))^2]^{1/11}\}\}.
\]
Every selected class has gamma_o<=chi(a), with chi(a)=O(a^(1/11)(1+log(1/a))^(2/11))->0, increasing on this interval.
Thus j=|O|>=Gamma/chi(a).
For q_o=gamma_o/Gamma, its entropy H(q)>=max(0,log(Gamma/chi(a))).
For every fixed epsilon in (0,1), the growing range p^2 B<=m^(-1+epsilon) has gamma_o<=chi(m^epsilon) for sufficiently small m, uniformly in actual degrees, primes and B.
The complete joint bounds retain every order class:
\[
2\Gamma\log p\le\log|Res(P,H)|/d\le\sum_o\Omega(a\gamma_o),
\]
\[
\sum_o A_o(n)/d\le\sum_o\Omega(a\gamma_o)
 +\Gamma\log^+(n/(d\Gamma))+\Gamma H(q).
\]
No replacement of the sum by Omega(a Gamma) is made, and selected total mass Gamma is not proved to vanish.

For every integer R>=0, H_R(t)=H(t^(p^R)) is squarefree cyclotomic with degree p^R D, the same circle maximum mathcal C, and exact p-valuation sum_o V_o+RW.
Consequently
\[
(R+2)\Gamma\log p\le\log\mathcal C+p^R(D/d)m
 \le\log\mathcal C+p^R a\Gamma .
\]
For 0<a<=1 the fully charged choice R=floor(log_p(1/a)) proves
\[
\log\mathcal C\ge\Gamma[\log(1/(pBm))-1].
\]
Whenever its numerator is positive, the conditional inequality
\[
m\ge\frac{(R+2)\Gamma\log p-\log\mathcal C}
 {p^{R+2}B\Gamma}
\]
holds.
The finite upper bound log mathcal C<=sum_o log C(Phi_o)<=(log2)sum_o phi(o) supplies no favorable uniform upper constant.

The actual ramified control P=t^2-4t+1,p=2 has o=f=1,w=E=2,k=1,r=2,N=4,H=t^4-1,V=6 and later gain W=2.
For the complete fixed-prime C527 family, p=2,E_o=1,r_o=1,o/f_o=15/4, D=2d, sum N_o=15d/4, exact captured valuation 2d and full complement degree 7d/4.
Both controls have fixed-positive or degree-linear growing original measure and are not near-one families.
Efficient-order coverage, favorable joint values, a favorable circle upper bound, common-time income and an unrestricted gap remain unresolved.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:07 |
| status | open |
| reason | Register the exact complete statement and every necessary original argument, with genuine author, source, finite-evidence and failure boundaries. Current whole mathematical inspection and adoption are separate actual acts; no old review is backfilled with this C input and no research execution is resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Every nontorsion unit and actual complete modular factorization, nonempty efficient-order set with all bad/index multiplicities, exact captured depths/resultant/complement/full degrees, explicit C504 modulus/chi inversion and all-time fragmentation/entropy costs, every further R lift/circle bound and both exact actual controls, with all coverage and expense limits. |
| argument | [Complete argument](#argument) | Entire original Sections1--6/equations(1)--(26), including individual-field ramification proof, exceptional p2 capture and exact stable slope, disjoint p-free cyclotomic blocks and complete cofactor, exact small-height modulus inversion/monotonicity and same-n dispersion, circle-average/maximum distinction and fully charged lift optimization, original contribution/source/negative scopes. |
| dependency | [Full powered-height modulus](Yin_C_G0504_v1.md#statement) | Exact original-degree C_n modulus Omega at actual powered height, including degree drops and norm multiplicity; Pri11/Dim19 source interfaces remain at existing statement/application depth. |
| dependency | [Maximum-circle full norm bound](Yin_C_G0244_v1.md#scalar-congruence-norm-domain) | Complete original field norm <=circle maximum^d times M(P)^degree; no scalar-divisibility or dyadic optimality premise imported. |
| support | [Actual stable valuation convention](Yin_C_G0256_v1.md#fixed-prime-actual-growth) | Original-root normalized p-valuations, all initial cancellation and exact stable p-power slopes, including p2 and bad primes. |
| support | [Fixed-prime actual control](Yin_C_G0527_v1.md#statement) | Only the complete efficient 3/5-order family and exact two binary depths/full measure comparison, used as a different auxiliary-vs-common-time calibration. |
| support | [Ramified exact control](Yin_C_G0512_v2.md#full-depth-fixed-scope) | Only alpha=2+sqrt3,P=t2-4t+1,p2 and exact original per-root depths at1,2,4; not a small-height application. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:21 |
| status | proved |
| reason | Adopt the exact complete current Statement and entire retained argument after the actual whole SELF inspection recorded in R735. Every used mathematical dependency is resolved at its explicit scope, the complete original proof and necessary source/native/failure facts are retained, and no unresolved mathematical issue affects this restricted theorem. The old whole review retains its missing declaration and unestablished initial context; this current SELF neither creates independent evidence nor closes M04 or any research Task. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Every nontorsion unit and actual complete modular factorization, nonempty efficient-order set with all bad/index multiplicities, exact captured depths/resultant/complement/full degrees, explicit C504 modulus/chi inversion and all-time fragmentation/entropy costs, every further R lift/circle bound and both exact actual controls, with all coverage and expense limits. |
| argument | [Complete argument](#argument) | Entire original Sections1--6/equations(1)--(26), including individual-field ramification proof, exceptional p2 capture and exact stable slope, disjoint p-free cyclotomic blocks and complete cofactor, exact small-height modulus inversion/monotonicity and same-n dispersion, circle-average/maximum distinction and fully charged lift optimization, original contribution/source/negative scopes. |
| dependency | [Full powered-height modulus](Yin_C_G0504_v1.md#statement) | Exact original-degree C_n modulus Omega at actual powered height, including degree drops and norm multiplicity; Pri11/Dim19 source interfaces remain at existing statement/application depth. |
| dependency | [Maximum-circle full norm bound](Yin_C_G0244_v1.md#scalar-congruence-norm-domain) | Complete original field norm <=circle maximum^d times M(P)^degree; no scalar-divisibility or dyadic optimality premise imported. |
| support | [Actual stable valuation convention](Yin_C_G0256_v1.md#fixed-prime-actual-growth) | Original-root normalized p-valuations, all initial cancellation and exact stable p-power slopes, including p2 and bad primes. |
| support | [Fixed-prime actual control](Yin_C_G0527_v1.md#statement) | Only the complete efficient 3/5-order family and exact two binary depths/full measure comparison, used as a different auxiliary-vs-common-time calibration. |
| support | [Ramified exact control](Yin_C_G0512_v2.md#full-depth-fixed-scope) | Only alpha=2+sqrt3,P=t2-4t+1,p2 and exact original per-root depths at1,2,4; not a small-height application. |
| review | [Actual current whole SELF](../audits/reviews/Yin_R_G0735_v1.md#current-g221-whole-self-finding) | Entire exact current statement and complete argument with every explicit domain, input interface, full mathematical proof, source/native/control scope and limitation inspected at this current C; actual SELF, not a retrospective old review or isolated replacement. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:48 |
| status | proved |
| reason | Adopt the entire exact current Statement and complete retained Argument after the actual independently reviewed whole finding in R791. All eight batch initial conclusions preceded every old target finding and Assessment. Necessary inputs are resolved at their exact fixed scopes, original mathematical and evidence/source/failure/negative history is retained, and no unresolved issue affects this restricted result. This is a new actual current adoption, with no old relationship or binding backfill and no Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Every nontorsion unit and actual complete modular factorization, nonempty efficient-order set with all bad/index multiplicities, exact captured depths/resultant/complement/full degrees, explicit C504 modulus/chi inversion and all-time fragmentation/entropy costs, every further R lift/circle bound and both exact actual controls, with all coverage and expense limits. |
| argument | [Complete argument](#argument) | Entire original Sections1--6/equations(1)--(26), including individual-field ramification proof, exceptional p2 capture and exact stable slope, disjoint p-free cyclotomic blocks and complete cofactor, exact small-height modulus inversion/monotonicity and same-n dispersion, circle-average/maximum distinction and fully charged lift optimization, original contribution/source/negative scopes. |
| dependency | [Full powered-height modulus](Yin_C_G0504_v1.md#statement) | Exact original-degree C_n modulus Omega at actual powered height, including degree drops and norm multiplicity; Pri11/Dim19 source interfaces remain at existing statement/application depth. |
| dependency | [Maximum-circle full norm bound](Yin_C_G0244_v1.md#scalar-congruence-norm-domain) | Complete original field norm <=circle maximum^d times M(P)^degree; no scalar-divisibility or dyadic optimality premise imported. |
| support | [Actual stable valuation convention](Yin_C_G0256_v1.md#fixed-prime-actual-growth) | Original-root normalized p-valuations, all initial cancellation and exact stable p-power slopes, including p2 and bad primes. |
| support | [Fixed-prime actual control](Yin_C_G0527_v1.md#statement) | Only the complete efficient 3/5-order family and exact two binary depths/full measure comparison, used as a different auxiliary-vs-common-time calibration. |
| support | [Ramified exact control](Yin_C_G0512_v2.md#full-depth-fixed-scope) | Only alpha=2+sqrt3,P=t2-4t+1,p2 and exact original per-root depths at1,2,4; not a small-height application. |
| review | [Actual current whole independent finding](../audits/reviews/Yin_R_G0791_v1.md#order-auxiliary-current-independent) | Entire exact current Statement and complete Argument, with every actual domain, fixed mathematical interface, complete proof, finite/source/failure/control boundary and cost; true isolated initial mathematical conclusion 2026-10-22T21:38, followed by old-scope comparison, without rewriting historical relations or resuming research. |

## Complete argument

<a id="argument"></a>

<a id="order-adapted-cyclotomic-auxiliary"></a>
### 1. Reuse, domain and result

The comparison inputs are [L213's full selected-depth bounds](Yin_C_G0512_v2.md#full-depth-fixed-scope) and [L217's fixed-prime efficient-order obstruction](Yin_C_G0527_v1.md#efficient-order-fixed-scope).
The latter has total measure of order its degree; it does not settle the near-one question.
Here the local capture is scaled by each actual reduction multiplicity, rather than by the whole degree.
The resulting order blocks can be joined in a degree-linear squarefree auxiliary, with no assertion that their incomes occur at a common cyclic time.

The precise reused interfaces are [L74's original-root valuations and stable lift](Yin_C_G0256_v1.md#fixed-prime-actual-growth), [L78's cyclotomic local layers](Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers), [L209's actual-powered-height modulus](Yin_C_G0504_v1.md#height-uniform-cyclic-cost-modulus), and the [L67 maximum-circle norm inequality](Yin_C_G0244_v1.md#scalar-congruence-norm-domain).
The bounded local screen also included [L68's positive-mass cyclic criterion](../ledger/Yin_L_G0068_v1.md#cyclic-norm-residue-density), [L152's joint-circle existence-floor ceiling](../ledger/Yin_L_G0152_v1.md#joint-circle-existence-floor-ceiling) and [L188's normalized layer averaging](../ledger/Yin_L_G0188_v1.md#complete-cyclic-layer-average).
The generic norm inequality and prime-power lifting are reused mechanisms.
The contribution is the multiplicity-scaled, disjoint-order auxiliary and its full actual-income, degree and near-one complexity account.
No exhaustive priority search or historical novelty claim is made.

Let P be monic irreducible in Z[t], with constant term plus or minus one, whose roots are not roots of unity.
Let d=deg P, m=log M(P)>0 and

\[
 C_n=|\operatorname{Res}(P,t^n-1)|.
\]

All measures and norms are unnormalized.
The result applies to general nontorsion units, including the whole reciprocal hard core; reciprocity is not a premise.
Fix a rational prime p and factor the complete reduction

\[
 \overline P=\prod_{\varphi}\varphi^{e_\varphi}
                  \quad\hbox{over }\mathbb F_p.
\]

The factors have nonzero constant terms.
For each occurring residue order o, which is prime to p, let f_o=ord_o(p), using f_1=1.
Every irreducible factor whose roots have order o has degree f_o.
Put

\[
 w_o=\sum_{\varphi\text{ of order }o}e_\varphi f_o,
 \quad E_o=\max_{\varphi\text{ of order }o}e_\varphi,
 \quad k_o=\lceil\log_p E_o\rceil,
 \quad r_o=k_o+1,
 \quad N_o=o p^{r_o}.                                  \tag{1}
\]

Thus w_o is the complete original-root mass of that order, including all repeated reductions.
An occurring order has w_o>0 and E_o>=1; no maximum over an empty set is taken.
Let O be a nonempty set of occurring orders, and assume

\[
 o/f_o\le B\quad(o\in O),\qquad
 W=\sum_{o\in O}w_o,\qquad \Gamma=W/d.                  \tag{2}
\]

Here B>=1 may vary with the input.
The fixed-degree meaning of f_o and all original multiplicities are retained even at ramified or power-basis index primes.

Define the actual auxiliary

\[
 H(t)=\prod_{o\in O}\Phi_o(t^{p^{r_o}}),\qquad
 D=\deg H=\sum_{o\in O}\phi(o)p^{r_o},
 \qquad \mathcal C=\max_{|t|=1}|H(t)|.                 \tag{3}
\]

The proof below establishes that H is monic, integral, squarefree and cyclotomic, with M(H)=1, and

\[
 D\le\sum_{o\in O}N_o\le p^2 B W,
 \qquad \log|\operatorname{Res}(P,H)|\ge2W\log p.       \tag{4}
\]

The entire resultant, not a primitive factor or a normalized cofactor, is the object here.
Its p-valuation is determined exactly by the full captured depths in Section3.
Under a=p^2 Bm<=1 the same object necessarily satisfies

\[
 \log\mathcal C
    \ge\Gamma\left(\log\frac1{pBm}-1\right).           \tag{5}
\]

Consequently, for fixed p,B and positive lower bound on Gamma, genuinely small total m would force its circle maximum to diverge at least as a power of 1/m, despite M(H)=1 and D=O(d).
This is a necessary expense, not a contradiction.
Section4 also gives a quantitative vanishing bound for every individual efficient-order mass and hence forces fragmentation across many different orders.
The sole external statements used there are the already accepted Pri11 and retained Dim19 inputs inside L209, with their original statement/applicability and source-proof limits unchanged.
No new source is needed for the local construction, (4) or (5).

<a id="local-multiplicity-scaled-depth-capture"></a>
### 2. Actual reduction multiplicity controls the transient depth cost

Label original roots in a p-adic splitting field and normalize v(p)=1.
Fix a root alpha_i reducing to a root of the factor varphi.
Its individual field L=Q_p(alpha_i) has degree e F, where e is its ramification index and F its residue-field degree.
The residue of alpha_i generates a subfield of degree f=deg varphi, so f divides F.

Here the stronger bound

\[
 e\le e_\varphi\le E_o                               \tag{6}
\]

is available.
To prove it, let g be the minimal polynomial of alpha_i over Q_p.
Its roots are conjugate under the local absolute Galois group, whose action on residues is by finite-field automorphisms.
Their reductions therefore all belong to the Frobenius orbit cut out by varphi.
The monic polynomial g has coefficients in Z_p because all its roots are integral.
Its reduction, which also has coefficients in F_p, is consequently a power of varphi; comparison of degrees gives

\[
 \overline g=\varphi^{e F/f}.
\]

The quotient P/g is monic and has integral roots as well, hence belongs to Z_p[t].
Thus eF/f<=e_varphi.
Since F/f>=1, (6) follows.
This argument neither assumes the power basis is maximal nor identifies a reduction multiplicity with a local ramification index; several local factors or a residue-field extension may account for the strict inequality.
The common splitting field is used only to label roots and supplies no ramification estimate.

If the reduced order is o, then alpha_i^o-1 is nonzero and belongs to the maximal ideal of L, whence v(alpha_i^o-1)>=1/e>=1/E_o.
The retained binomial inequality

\[
 v(x^p-1)\ge\min(pv(x-1),1+v(x-1))
\]

implies min(v(x^p-1),1)>=min(pv(x-1),1).
Therefore k_o powerings raise the valuation to at least one, and the extra powering in r_o raises it to at least two.
Every exceptional cancellation before that point is kept; no finite upper bound on its depth has been assumed.

At a valuation t>=2, the linear term in (1+y)^p-1 has valuation 1+t, all intermediate terms have valuation at least 1+2t, and the last has valuation pt>1+t.
Thus all further p-powerings have exact increment one, including p=2.
A power prime to p preserves a positive valuation because its geometric-sum quotient is a unit.
Define the actual finite captured value

\[
 V_o=\sum_{i:\operatorname{ord}(\overline\alpha_i)=o}
                v(\alpha_i^{N_o}-1),
 \qquad V_o\ge2w_o.                                   \tag{7}
\]

For every target n>=1 its full contribution A_o(n) obeys

\[
 \begin{split}
 A_o(n)&=(\log p)\sum_{i:\operatorname{ord}(\overline\alpha_i)=o}
                              v(\alpha_i^n-1),\\
 A_o(n)&\le(\log p)V_o+w_o\log^+(n/N_o)
        \le(\log p)V_o+w_o\log^+(n/w_o).                \tag{8}
 \end{split}
\]

Indeed A_o(n)=0 unless o divides n.
Otherwise write n=o p^r u with p not dividing u.
Valuations are nondecreasing before r_o, and after r_o their difference is exactly r-r_o.
If r>r_o, then (r-r_o)log p<=log(n/N_o), proving the first bound.

For the second, there are exactly phi(o)/f_o irreducible factors of Phi_o modulo p: it has simple roots because p does not divide o, and all these roots have degree f_o.
The factors appearing in P form a subset, so

\[
 w_o\le\phi(o)E_o\le oE_o\le N_o/p.
\]

On the other side minimality of k_o gives p^{r_o}<=p^2 E_o, also when E_o=1.
Since f_o E_o<=w_o, (2) gives

\[
 N_o\le p^2 o E_o\le p^2 B w_o.                       \tag{9}
\]

These lower and upper comparisons explain why the center in (8) and the capture degree can be charged to the order-class mass itself.
Equation (8) concerns actual contributions at a single n; it is not an identity of the different N_o.

<a id="disjoint-order-squarefree-resultant"></a>
### 3. One squarefree auxiliary with exact arithmetic income and full degree

For p not dividing o, elementary root orders give

\[
 \Phi_o(t^{p^r})=\prod_{j=0}^{r}\Phi_{op^j}(t)
                        \quad(r\ge0).                 \tag{10}
\]

Both sides are monic and have precisely the roots whose p^r-th power has exact order o.
Every such root has order op^j for exactly one 0<=j<=r; all roots are simple over characteristic zero.
This proves (10), including o=1, without a coefficient or multiplicity shortcut.
Its degree is phi(o)p^r.

Distinct o in O are distinct p-free parts of these indices.
Hence every cyclotomic factor in (3),(10) occurs exactly once.
H is squarefree over Q, has constant term plus or minus one, and has M(H)=1.
It need not have squarefree reduction modulo p; that is not asserted.
Equations (9)--(10) prove the full degree bound in (4).

For a root alpha_i of residue order o, factoring t^o-1 into its cyclotomic factors and evaluating at alpha_i^{p^{r_o}} shows

\[
 v\bigl(\Phi_o(\alpha_i^{p^{r_o}})\bigr)
                   =v(\alpha_i^{N_o}-1).               \tag{11}
\]

All proper-divisor factors are units: alpha_i^{p^{r_o}} still has residue order o, whereas Phi_b modulo p has roots of exact order b for b dividing o.
Moreover Phi_b(t^{p^r}) reduces modulo p to Phi_b(t)^{p^r}, so a block with p-free order b different from o evaluates to a unit at alpha_i.
Thus roots outside O contribute zero and the full resultant has the exact identity

\[
 v_p\operatorname{Res}(P,H)=\sum_{o\in O}V_o.           \tag{12}
\]

There is no additional residue-degree divisor: every one of the original d roots is counted.
The absolute resultant is a nonzero integer, because a common complex root would make a conjugate of P a root of unity.
Equations (7),(12) give the income in (4), including every actual initial depth.

For completeness the cyclic-product complement is also exact.
Let

\[
 G(t)=\prod_{o\in O}(t^{N_o}-1),\qquad J(t)=G(t)/H(t).
\]

Each block of H divides its corresponding factor of G, so J is a monic integral cyclotomic product.
Repeated factors of G or J are retained.
The complete degrees and norms are

\[
 \deg G=\sum_oN_o,\quad \deg J=\sum_oN_o-D,\quad
 \prod_o C_{N_o}
       =|\operatorname{Res}(P,H)|\,|\operatorname{Res}(P,J)|.  \tag{13}
\]

Both resultants are nonzero integers, and M(G)=M(J)=1.
Their ordinary integer norms need not equal one; the second norm cannot be discarded from an equality or an income claim.
Its lower bound one does give the valid upper bound |Res(P,H)|<=product_o C_(N_o).
No primitive normalization or passage to a smaller powered field is used.
The new income belongs to this single complete auxiliary resultant; it is not renamed as income in one cyclic norm C_n.

<a id="small-measure-efficient-order-fragmentation"></a>
### 4. Genuine small-measure inputs require order fragmentation

Write gamma_o=w_o/d, a=p^2 Bm, and retain the exact L209 modulus

\[
 \begin{split}
 c&=\log2/4,\qquad h_0=c e^{-20},\\
 b(h)&=\max\{h,\sqrt{h/c}\log\sqrt{c/h}\},\\
 \Omega(h)&=19b(h)^{1/6},\qquad 0<h\le h_0.
 \end{split}
\]

Its adopted theorem is log C_n/d<=Omega(nm/d) whenever nm/d<=h_0, with all actual powered-degree drops and norm multiplicities included.
Suppose 0<a<=h_0.
Equation (9) gives N_o m/d<=a gamma_o.
Nonnegativity of the omitted local valuations and (7) therefore imply

\[
 2\gamma_o\log p
   \le \frac{(\log p)V_o}{d}
   \le \frac{\log C_{N_o}}d
   \le\Omega(a\gamma_o).                              \tag{14}
\]

This controls an efficient order class even if its residue degree is very large; it is not a bound requiring f_o to lie below L213's cutoff.
All original reduction multiplicities remain present.
The full-depth consequence of (8) is

\[
 \frac{A_o(n)}d\le\Omega(a\gamma_o)
                    +\gamma_o\log^+\frac{n}{d\gamma_o}
                      \quad(n\ge1).                   \tag{15}
\]

There is also a concrete uniform inversion of (14).
Define

\[
 K_0=\max\{1,(2\sqrt c)^{-1}\},\qquad
 K=\frac{19K_0^{1/6}}{2\log2},
\]

and, for 0<a<=h_0, put

\[
 \chi(a)=\min\left\{1,\max\left\{a,
       [K^{12}a(1+2\log(1/a))^2]^{1/11}\right\}\right\}.
                                                               \tag{16}
\]

Then every selected class satisfies gamma_o<=chi(a).
To verify this directly, for 0<h<=h_0<1 one has b(h)<=K_0 sqrt(h)(1+log(1/h)), because c<1.
If gamma_o<a, the first alternative in (16) suffices.
Otherwise a gamma_o>=a^2, so log(1/(a gamma_o))<=2log(1/a).
Raising (14), with log p>=log2, to the twelfth power and dividing by gamma_o>0 gives

\[
 \gamma_o^{11}\le K^{12}a(1+2\log(1/a))^2,
\]

which proves (16); the outer minimum uses gamma_o<=1.
In particular

\[
 \chi(a)=O\bigl(a^{1/11}(1+\log(1/a))^{2/11}\bigr)
                       \longrightarrow0.              \tag{17}
\]

The displayed expression is increasing on (0,h_0]: for its nontrivial term, the logarithmic derivative with respect to log a has the sign of 1-4/(1+2log(1/a)), which is positive there.
Thus for fixed 0<epsilon<1, the growing range p^2 B<=m^{-1+epsilon} gives gamma_o<=chi(m^epsilon) for sufficiently small m, uniformly in all actual degrees and all such primes and order-efficiency bounds.

Let j=|O|.
Since sum gamma_o=Gamma, (16) proves

\[
 j\ge\Gamma/\chi(a).
\]

For the finite normalized order distribution q_o=gamma_o/Gamma, its Shannon entropy satisfies

\[
 \mathcal H(q)=-\sum_o q_o\log q_o
       \ge\max\{0,\log(\Gamma/\chi(a))\}.              \tag{18}
\]

Indeed q_o<=chi(a)/Gamma.
For example a positive fraction Gamma>=gamma_0>0 of efficient orders at bounded p,B on a hypothetical m->0 family requires at least a constant multiple of m^{-1/11}(1+log(1/m))^{-2/11} distinct orders.
This is a necessary fragmentation theorem on actual small-total-measure inputs.
It supplies neither such a family nor a bound on the total efficient-order mass Gamma.

The exact combined expense, using (13), is

\[
 2\Gamma\log p
     \le\frac{\log|\operatorname{Res}(P,H)|}{d}
     \le\sum_{o\in O}\Omega(a\gamma_o).                \tag{19}
\]

The sum must retain the number and masses of the different order classes.
Concavity-type small-power expenses cannot be replaced by Omega(a Gamma) without a new theorem.
In particular (19) does not become a contradiction merely because a tends to zero while j grows.
For the actual contribution at one target n, summing (15) gives the explicit additional dispersion cost

\[
 \frac{\sum_{o\in O}A_o(n)}d
 \le\sum_o\Omega(a\gamma_o)
       +\Gamma\log^+\frac{n}{d\Gamma}
       +\Gamma\mathcal H(q).                           \tag{20}
\]

Here log^+(x/q)<=log^+x+log(1/q) for 0<q<=1 proves the inequality.
Every A_o is evaluated at that same n.
This bound neither counts the auxiliary as a cyclic norm nor replaces the sharper full-norm small-height bound when that already applies.

<a id="order-auxiliary-circle-complexity-cost"></a>
### 5. The entire circle expense and an actual near-one obstruction to bounding it

The reused maximum-modulus inequality gives

\[
 \log|\operatorname{Res}(P,H)|\le d\log\mathcal C+D m.  \tag{21}
\]

All factors of H and all original conjugates of P occur.
Its Mahler measure one only states the circle average of log|H|; the maximum mathcal C in (21) is a different quantity.

The same selected order blocks admit exact additional lifts.
For every integer R>=0 define H_R(t)=H(t^{p^R}).
Then H_R is again squarefree cyclotomic, has degree p^R D, and

\[
 \begin{split}
 \max_{|t|=1}|H_R(t)|&=\mathcal C,\\
 v_p\operatorname{Res}(P,H_R)&=\sum_o V_o+R W.
 \end{split}                                          \tag{22}
\]

The first identity uses surjectivity of the power map on the full unit circle.
The second follows from the same disjoint p-free orders as (11)--(12), with all valuations already beyond the exceptional stage, where every further power has exact slope one.
Roots outside O still contribute zero.
Thus the entire degree cost and arithmetic gain, for every R, give

\[
 (R+2)\Gamma\log p
      \le\log\mathcal C+p^R(D/d)m
      \le\log\mathcal C+p^R a\Gamma.                  \tag{23}
\]

Suppose now 0<a<=1 and take R=floor(log_p(1/a)), so R>=0, p^R a<=1 and R>=log_p(1/a)-1.
Rearranging (23) proves exactly

\[
 \log\mathcal C\ge\Gamma[\log(1/a)+\log p-1]
                =\Gamma\left[\log\frac1{pBm}-1\right],
\]

which is (5).
This lower bound is substantive even though it need not be positive for every admitted input.
For fixed p,B and Gamma>=gamma_0>0 it forces unbounded circle complexity as m->0.
The lift used to obtain it has actual degree p^R D and its full measure expense was charged in (23); no large power is free.

Conversely a uniform upper bound on mathcal C on a genuinely small-m positive-mass class would be useful.
The exact inequality gives, whenever its numerator is positive,

\[
 m\ge
 \frac{(R+2)\Gamma\log p-\log\mathcal C}
            {p^{R+2}B\Gamma}.                          \tag{24}
\]

This is a restricted conditional implication, not a proved upper bound on mathcal C.
The scalar norm inequality and the idea of lifting at fixed circle maximum are classical/reused from L67; here they apply to the newly constructed mass-scaled disjoint-order auxiliary rather than to a full scalar collapse in the monogenic order.

There is a finite computable upper cost, but no uniform favorable one is obtained here:

\[
 \log\mathcal C
     \le\sum_{o\in O}\log C(\Phi_o)
     \le(\log2)\sum_{o\in O}\phi(o).                  \tag{25}
\]

For the first inequality each power substitution has the same circle maximum as Phi_o.
For the second, a monic polynomial with phi(o) unit-modulus roots has coefficient sum at most 2^{phi(o)}, by the elementary-symmetric expansion.
Thus (25) is legitimate for every tuple, but may grow with the input and does not supply the uniform circle bound in (24).
Formula (19) is the alternative complete actual-value bound when its capture heights are small.
Neither bound permits deleting complexity because H is squarefree, cyclotomic or of degree O(d).

<a id="order-auxiliary-controls-and-scope"></a>
### 6. Exact controls, retained limitations and contribution

The already retained ramified control alpha=2+sqrt3, P=t^2-4t+1 and p=2 checks the multiplicity-scaled threshold.
Here Pbar=(t+1)^2, o=f=1, w=E=2, k=1, r=2, N=4 and H=t^4-1.
L213's exact hand calculation gives per-root valuations 1/2,1,3 at exponents 1,2,4 and hence V=6.
Thus v_2 Res(P,H)=6, including the exceptional jump, and all later lifts add exactly W=2.
The full auxiliary degree is 4.
This reuses an actual fixed-positive-measure control; it is not a new numerical experiment or a small-a application of (14).

There is also a concrete distinction from common-time coordination on the actual L217 family.
That family has p=2, E_o=1, r_o=1 and o/f_o=15/4 for all its groups.
Its complete degree is d=sum_o phi(o), and the new auxiliary is

\[
 H(t)=\prod_o\Phi_o(t^2)
     =\prod_o\Phi_o(t)\Phi_{2o}(t),\qquad D=2d.
\]

L217 proved v(alpha_i^o-1)=v(alpha_i^o+1)=1 at every root in that group, so every capture at 2o has depth two.
Consequently

\[
 v_2\operatorname{Res}(P_K,H)=2d,
 \qquad \sum_o N_o=\frac{15}{4}d.                      \tag{26}
\]

The cofactor in (13) has degree (15/4)d-2d=(7/4)d and remains cyclotomic; these degrees are integers for the actual family.
Thus the same actual inputs with o(d) maximum 2-primary income on every fixed degree-linear cyclic window have a squarefree degree-2d auxiliary with exactly 2d units of 2-adic valuation.
This is a changed arithmetic object, not a violation of the common-time obstruction.
Its full resultant may have other prime factors and these are not calculated away.
The original m(P_K) is of order d, so no near-one conclusion follows from this control.

The genuinely small-m conclusions here are (14)--(18) and (5): efficient high-degree root mass must fragment into many order classes, and the complete auxiliary for a persistent positive fraction must have growing circle maximum.
The total selected mass is not proved to vanish; no theorem forces enough efficient orders to exist on every near-one input.
Nor is there a theorem saying small m supplies a favorable common exponent.
A possible next bridge would control the joint actual values of these disjoint-order blocks more strongly than the separate sum in (19), or constrain their full circle complexity in a class that actually covers near-one inputs.
Either would need a new arithmetic fact.
General-input examples, a zero Mahler measure for H, individual order efficiency or dropping the complete cofactor are insufficient replacements.

The coordinator supplied only the broad question and received checkpoints after these deductions were developed.
The arithmetic author developed the local reduction-multiplicity refinement, mass-scaled capture, squarefree disjoint-order construction, exact resultant and degree accounting, explicit fragmentation bound, all-lift circle-complexity lower bound and the two control comparisons.
Existing local-field ramification/residue conventions, cyclotomic identities, stable binomial lifting, scalar maximum-modulus norms and L209's source-backed expense modulus are explicitly reused.
Historical novelty is not claimed.

The [complete original author checking/evidence account](../audits/reviews/Yin_R_G0735_v1.md#original-g221-author-self-finding) retains its actual original input, recorded precision and scope, separately from the current whole SELF finding.

Author freeze: 2026-10-09T21:32.
No numerical program or source-proof audit is claimed.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0791_v1.md#order-auxiliary-complete-independent-review), with its original inspected scope and relationship.
