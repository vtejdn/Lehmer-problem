---
author: Yin
---
# Weighted dyadic triple capture and bounded scale-mass arithmetic income

Date: 2026-10-13T05:21.
Human author Yin.
The direct_triple author supplied the ENTIRE NEW D24, Fixed positive triple density without uniform short-pair constants, at its final13:11 freeze.
The squarefree_extraction_review agent independently WHOLE-reviewed that original in R341 and NOW authors this actual statement/extraction, becoming a wrapper contributor.
R341 covers the original only; a different noncontributor must review this ACTUAL extraction before adoption.
The earlier retired D24 preserved in C97 is a different artifact and supplies no review of this new proof.

## Statement

**A. Accepted source constant and weighted two-band estimate.**
Fix epsilon in(0,1).
The published [GW21-U001](../audits/literature/GW21/Yin_U001.md#gw21-u001) Theorem1.1 supplies a finite K_epsilon>=1, depending only on epsilon, such that for real A,B,D>=1 with D<=min(A,B), finite integer sets I subset[A,2A], J subset[B,2B], and0<rho<=1,

    # {(a,b) in I x J:gcd(a,b)>=D}>=rho*|I|*|J|
    implies |I|*|J|<=K_epsilon*rho^(-2-epsilon)*AB/D^2.

One admissible uniform choice is K_epsilon=1000^(1+pi(p0(epsilon))), using the source's finite epsilon-dependent prime threshold.
No numerical value or unchanged constant as epsilon tends to0 is claimed.
This is an accepted external statement at its recorded published-edition, statement/applicability scope; no complete audit of its source proof is asserted.

Define

    q=2+epsilon, theta=1/q, beta=2/q,
    r=1-theta=1-beta/2,
    B_epsilon=(4K_epsilon)^(1/q),
    c_epsilon=1/[2(2B_epsilon)^(1/beta)].

Thus2/3<beta<1 and1/2<r<2/3.
For real A,B>=1, finite integer sets I subset[A,2A], J subset[B,2B], arbitrary REAL weights0<=u_a<=2A,0<=v_b<=2B, totals U=sum u_a,V=sum v_b, and EVERY REAL Y>0,

    sum_(a in I,b in J,lcm(a,b)<=Y)u_a*v_b
       <=B_epsilon*Y^beta*(UV)^r.                    (A)

All pairs are ORDERED, common labels and diagonals are included, and empty/zero-weight cases are allowed.
The proof separately handles empty compatibility when Y<1 or Y<max(A,B), then applies the source at D=max(1,AB/Y).
The weighted conversion is proved by finite level sets; it is not an unsupported identification of cardinality with root mass.

**B. Exact global scale-mass bound.**
Let S be any nonempty finite set of positive integers, with arbitrary REAL weights0<w_a<=a and W=sum_(a in S)w_a.
Fix an INTEGER X>=1.
For0<=k<L=1+floor(log_2 X), put

    S_k={a in S:2^k<=a<2^(k+1), a<=X},
    W_k=sum_(a in S_k)w_a,
    Z=sum_(k=0)^(L-1)W_k^r,
    L_eff=(sum_(k=0)^(L-1)(W_k/W)^r)^(2/beta).

If no order is eligible, L_eff=0.
Otherwise0<L_eff<=L.
It may be BELOW1: all orders above X remain in W but not in the eligible bands.
For every REAL Y>0, with the SAME eligible set,

    P_2^X(Y)=sum_(a,b in S,a<=X,b<=X,lcm(a,b)<=Y)w_a*w_b
       <=B_epsilon*Y^beta*Z^2
        =B_epsilon*Y^beta*W^(2-beta)*L_eff^beta.       (B)

Every ordered band pair and diagonal is retained.
Equal masses in exactly M occupied bands carrying all W give L_eff=M; this mass identity supplies no triple-compatibility hypothesis.

**C. General compatible-triple capture.**
Retain the data in B and put

    h(n)=sum_(a in S,a divides n)w_a,
    H_X=max_(integer1<=n<=X)h(n),
    U_X(a,b)=sum_(c in S,lcm(a,b,c)<=X)w_c,
    T_X=sum_(a,b,c in S,lcm(a,b,c)<=X)w_a*w_b*w_c.

Triples are ORDERED with every repeated label.
If0<delta<=1 and T_X>=delta*W^3, then L_eff>0 and

    H_X>=c_epsilon*delta^(2+epsilon/2)*W^2/(X*L_eff)
       >=c_epsilon*delta^(2+epsilon/2)*W^2
                        /[X*(1+floor(log_2 X))].      (C)

This holds for the full real-weight domain0<w_a<=a, hence for every finite actual or abstract integer-capacity array1<=w_a<=phi(a).
It imposes no bound on the union of prime factors.
The proof uses the exact residual bucket inequality U_X(a,b)<=X*H_X/lcm(a,b) when that lcm is<=X, zero link otherwise, and splits at

    Y=(W/L_eff)*(delta/(2B_epsilon))^(1/beta).

The proof includes Y<1, Y>X and X=1 without rounding, widening the window or discarding repeated labels.
It assumes neither C96's refuted universal short-pair K nor C98's refuted stronger linear-in-density estimate.

For example epsilon=1/2, fixed delta,gamma,C>0, W>=gamma*d and integer1<=X<=C*d give

    H_X >= [c_(1/2)*delta^(9/4)*gamma^2/C]
                         *d/[1+floor(log_2(C*d))].    (D)

This improves the previous fixed-parameter lower order d^(3/4)/sqrt(log d) to d/log d.
It is STILL sublinear and by itself does not supply a uniform positive fraction of d or discharge L168's income criterion.
No optimal exponent, sharp constant or near-one coverage is asserted.

**D. Bounded scale-mass factor and actual positive measure.**
Fix epsilon in(0,1),0<delta,gamma<=1,C>0 and B0>0.
Let P be an ACTUAL monic irreducible nontorsion integer-unit polynomial of ORIGINAL degree d, alpha a root, K=Q(alpha), m(P)=log M(P)>0, and p a GOOD prime not dividing disc(P).
Select a nonempty set S of COMPLETE occurring reduced-root order groups, with actual integer root counts w_a<=phi(a), each residue factor counted by its degree ONCE.
Write W=sum_(a in S)w_a, so W<=d.
Suppose for an INTEGER1<=X<=C*d,

    W>=gamma*d, T_X>=delta*W^3, L_eff<=B0.            (E)

Then there is ONE actual integer n<=X<=C*d with

    h(n)>=[c_epsilon*delta^(2+epsilon/2)*gamma^2/(C*B0)]*d,
    A_p(n)>=eta*d,
    eta=[c_epsilon*delta^(2+epsilon/2)*gamma^2/(C*B0)]*log2>0,

where the full original norm and actual local income are

    D_n=Norm_(K/Q)(alpha^n-1)=Res(P,t^n-1)
       =product_(all d original roots)(alpha_i^n-1),
    C_n=|D_n| in Z_(>0),
    A_p(n)=(log p)*v_p(C_n)
          =(log p)*sum_(all d original p-adic roots)v_p(alpha_i^n-1),
    log C_n>=A_p(n)>=h(n)*log p>=h(n)*log2.           (F)

The good-prime first-return floor keeps all original roots, all actual initial, exceptional and later depths, including p=2, on the left.
No equality with depth1, smaller powered field, selected norm or combination of different exponents is substituted.
The auxiliary is the single t^n-1 of complete degree n, content1 and squared coefficient norm2.

The accepted [L168 finite criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) therefore yields STRICT m(P)>m0(C,eta)>0 for precisely the class(E), retaining its full norm tower, finite powered-degree escape and accepted Pri11 source scope.
A uniformly bounded number of occupied dyadic order bands is sufficient for the L_eff bound; exact uneven masses may give a smaller value.
This condition restricts order magnitudes and their masses, and does not require C97's bounded UNION of order primes.
No general implication in either direction between those two hypotheses is asserted.

Consequently, along any HYPOTHETICAL sequence with m(P)->0 and actual certificates with fixed gamma,delta,C as above, its L_eff MUST tend to infinity.
Otherwise a bounded subsequence would violate the same positive lower bound.
This necessary escape neither supplies the certificates nor proves the unrestricted original Mahler-gap objective.

**E. Source and remaining scope.**
GW21-U001 is the sole new external mathematical premise; its actual published theorem is accepted at statement/applicability scope, with no local PDF retained at that original reading stage and no complete original proof audit.
The later retained-copy and 2026-10-14 selected theorem/setup comparison are recorded in [GW21-U001](../audits/literature/GW21/Yin_U001.md#gw21-u001); they do not expand that original proof inspection.
The finite weighted adaptation, global scale factor, residual split and original-norm transfer are the project's complete arguments below.
Gou and the Annals paper are screened context only.
The alternative fractional-lcm-moment inequality remains unproved and unused.
The later [C142 v2](Yin_C_G0142_v2.md#statement) proves capture without scale loss for the subclass w_a<=phi(a), using its separately adopted weak-moment argument.
This Claim's published-statement-based adaptation still pays its stated scale factor, and the broader w_a<=a domain is not settled by that subclass result.
Automatic near-one coverage, the unrestricted positive Mahler gap and a zero-gap family remain unresolved.

## Current assessment
[Selected decision](#decision-current-actual-product-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T05:21 |
| status | open |
| reason | Register the proved-candidate weighted two-band adaptation, exact global scale-mass capture, d/log d improvement and bounded-L_eff actual positive-measure class while preserving the entire new13:11 original. R341 independently covers that original only; its reviewer now authored this wrapper, which requires a different actual-extraction review before adoption. No unrestricted no-loss or near-one theorem is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complete statement](#statement) | A--E, every real-weight and integer-X domain, exact constants and effective normalization, actual original-norm bridge and source limits. |
| argument | [Complete original](#argument) | Entire final13:11 NEW D24, equations1--12, ten explicit anchors, search/attribution, failed shortcuts, stopped/resumed history and freeze. |
| dependency | [GW21 accepted theorem](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Actual published Theorem1.1, fixed epsilon and finite uniform constant, exact cardinality hypotheses; statement/applicability acceptance only. |
| dependency | [C91 residual mechanism](Yin_C_G0091_v1.md#global-triple-short-pair-criterion) | Credited residual-bucket and split antecedent, fully proved locally using the new pair bound; the old universal K premise is excluded. |
| dependency | [L74 full original floor](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Same actual exponent, every original root once and all true depths retained, including the binary good-prime case. |
| dependency | [L168 finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive measure only after the bounded-L_eff uniform eta*d certificate at one n<=Cd; powered-degree and source limits unchanged. |
| support | [Whole original review](../audits/reviews/Yin_R_G0341_v1.md#weighted-dyadic-capture-whole-independent-finding) | Entire final13:11 original only; not prospective coverage of this actual wrapper. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-13T05:25 |
| status | proved |
| reason | Adopt R341 original whole and R342 distinct actual extraction review for the complete weighted two-band adaptation, general W^2/(X L_eff) capture, d/log d consequence and bounded-L_eff actual positive-measure class. The complete original and its stopped/resumed history are retained. GW21 is accepted only at its exact published statement/applicability scope; no source-proof audit or retained local PDF is asserted. General no-loss capture and automatic near-one coverage remain open; this does not resolve unrestricted G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complete statement](#statement) | A--E, every real-weight and integer-X domain, exact constants and effective normalization, actual original-norm bridge and source limits. |
| argument | [Complete original](#argument) | Entire final13:11 NEW D24, equations1--12, ten explicit anchors, search/attribution, failed shortcuts, stopped/resumed history and freeze. |
| dependency | [GW21 accepted theorem](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Actual published Theorem1.1, fixed epsilon and finite uniform constant, exact cardinality hypotheses; statement/applicability acceptance only. |
| dependency | [C91 residual mechanism](Yin_C_G0091_v1.md#global-triple-short-pair-criterion) | Credited residual-bucket and split antecedent, fully proved locally using the new pair bound; the old universal K premise is excluded. |
| dependency | [L74 full original floor](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Same actual exponent, every original root once and all true depths retained, including the binary good-prime case. |
| dependency | [L168 finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive measure only after the bounded-L_eff uniform eta*d certificate at one n<=Cd; powered-degree and source limits unchanged. |
| support | [Whole original review](../audits/reviews/Yin_R_G0341_v1.md#weighted-dyadic-capture-whole-independent-finding) | Entire final13:11 original only; not prospective coverage of this actual wrapper. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0342_v1.md#weighted-scale-mass-actual-extraction-finding) | Complete actual A--E and entire preserved proof, exact accepted source adaptation, every weight/window/normalization endpoint and actual original-norm scope. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A--E, every real-weight and integer-X domain, exact constants and effective normalization, actual original-norm bridge and source limits. |
| argument | [Argument](#argument) | Entire final13:11 NEW D24, equations1--12, ten explicit anchors, search/attribution, failed shortcuts, stopped/resumed history and freeze. |
| dependency | [Dependency](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Actual published Theorem1.1, fixed epsilon and finite uniform constant, exact cardinality hypotheses; statement/applicability acceptance only. |
| dependency | [Dependency](Yin_C_G0091_v1.md#global-triple-short-pair-criterion) | Credited residual-bucket and split antecedent, fully proved locally using the new pair bound; the old universal K premise is excluded. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same actual exponent, every original root once and all true depths retained, including the binary good-prime case. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive measure only after the bounded-L_eff uniform eta*d certificate at one n<=Cd; powered-degree and source limits unchanged. |
| support | [Support](../audits/reviews/Yin_R_G0341_v1.md#weighted-dyadic-capture-whole-independent-finding) | Entire final13:11 original only; not prospective coverage of this actual wrapper. |
| review | [Review](../audits/reviews/Yin_R_G0342_v1.md#weighted-scale-mass-actual-extraction-finding) | Complete actual A--E and entire preserved proof, exact accepted source adaptation, every weight/window/normalization endpoint and actual original-norm scope. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | A--E, every real-weight and integer-X domain, exact constants and effective normalization, actual original-norm bridge and source limits. |
| argument | [Exact retained argument](#argument) | Entire final13:11 NEW D24, equations1--12, ten explicit anchors, search/attribution, failed shortcuts, stopped/resumed history and freeze. |
| dependency | [Exact retained dependency](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Actual published Theorem1.1, fixed epsilon and finite uniform constant, exact cardinality hypotheses; statement/applicability acceptance only. |
| dependency | [Exact retained dependency](Yin_C_G0091_v1.md#global-triple-short-pair-criterion) | Credited residual-bucket and split antecedent, fully proved locally using the new pair bound; the old universal K premise is excluded. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same actual exponent, every original root once and all true depths retained, including the binary good-prime case. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Strict positive measure only after the bounded-L_eff uniform eta*d certificate at one n<=Cd; powered-degree and source limits unchanged. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0341_v1.md#weighted-dyadic-capture-whole-independent-finding) | Entire final13:11 original only; not prospective coverage of this actual wrapper. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0342_v1.md#weighted-scale-mass-actual-extraction-finding) | Complete actual A--E and entire preserved proof, exact accepted source adaptation, every weight/window/normalization endpoint and actual original-norm scope. |

## Registration and complete preservation

The complete final13:11 new original follows.
Only its duplicate short frontmatter is removed, its first title is demoted and outer newlines normalized.
All ten explicit anchors, source/reuse and contribution accounts, equations1--12, original stopped checkpoint and resumed timestamps remain.
The working original stays until a different reviewer checks this actual extraction, adoption occurs and whole-body preservation and exact incoming links are reconciled.
The global X hypothesis remains INTEGER>=1; only A,B and the two-band/pair threshold Y are real, as in the original.
No real-X extension is introduced.

## Argument

## Fixed positive triple density without uniform short-pair constants

Date: 2026-10-13T04:42.
Human author Yin.
Delegated direct_triple author continues G0001 under the root's same authorized execution window.

<a id="nonlinear-triple-question"></a>
## Exact question and fixed boundaries

For every fixed delta,C>0, does T_X>=delta W^3 and X<=C W force H_X>=c(delta,C)W for every finite integer capacity array 1<=w_o<=phi(o), with W=sum w_o, H_X=max_(1<=n<=X)sum_(o|n)w_o and ordered repeated-label T_X=sum_(lcm(a,b,c)<=X)w_a w_b w_c?
The intended conclusion is uniform as degrees and the union of order primes grow.
Actual-polynomial use additionally retains complete root groups, a good prime, original field degree and every norm/depth.

[C96](Yin_C_G0096_v1.md#statement) refutes the universal linear short-pair K bound.
[C98](Yin_C_G0098_v1.md#statement) refutes the direct LINEAR-in-density bound T_X<=K X H_X W even on actual reciprocal good-2 units, but supplies no uniform positive density.
Those routes are closed at exactly their refuted scope.
[C97](Yin_C_G0097_v1.md#statement) proves capture with a bounded UNION of order primes.
[C91](Yin_C_G0091_v1.md#statement) still supplies its unconditional sublinear bound and exact residual-bucket argument; its former uniform-K premise is false.
A new nonlinear density argument or actual fixed-positive-density obstruction is needed.

The separately assigned averaged_lcm author owns analysis of the special squarefree divisor family.
This draft instead investigates the general capacity model.
No new native mathematical program is started.
The main question is open at the start of this round.

<a id="nonlinear-triple-reuse-search"></a>
## Reuse and bounded search

Read the current S4 goal-directed frontier and the fixed C96--C98 decisions and exact scopes.
Earlier C86/C88/C91 residual and circular mechanisms were read in the preceding author round, with no change in their interfaces.
A local search of the literature and source-audit collection by lcm, gcd sums, weighted density and fractional Helly returned no exact usable general theorem beyond those records.

A bounded primary-source web search on 2026-10-13 queried totient-weighted short lcm density, fractional Helly for cyclic subgroups and Koukoulopoulos--Maynard GCD graphs.
Leads included the original Annals Duffin--Schaeffer paper and work titled Extremal problems for GCDs; they are being screened for precise applicability, not yet adopted as proof inputs.
General convex fractional Helly theorems have an ambient-dimension hypothesis not supplied here.
No theorem, exhaustive search or novelty claim follows from a search result.

## Continuing status

Author exploration; no new theorem or fixed-positive-density counterexample asserted.

<a id="nonlinear-triple-source-interface"></a>
## Green--Walker input and the limits of its use

2026-10-13T04:59.
The useful source is Ben Green and Aled Walker, *Extremal problems for GCDs*, Combinatorics, Probability and Computing30(2021),922--929, DOI10.1017/S0963548321000092.
The actual published eight-page [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D3BE6C493BF68649458DDED6D20AEB55/S0963548321000092a.pdf/extremal-problems-for-gcds.pdf) was read at Theorem1.1, printed922/PDF1, with its parameter setup and remarks on printed923/PDF2.
This is a statement/applicability acceptance of the published theorem.
Its underlying GCD-graph/minimal-counterexample proof and the Koukoulopoulos--Maynard source proof have NOT received a complete independent source-proof audit here.
The following weighted transfer and root-capture deduction are project arguments needing their own review.
After the explicitly authorized resumption, this exact accepted dependency was organized as [GW21-U001](../audits/literature/GW21/Yin_U001.md#gw21-u001); the original stopped checkpoint below retains its then-pending meaning.

Fix epsilon in(0,1).
The source supplies a finite threshold p0(epsilon), independent of all scale parameters.
Its theorem implies that there is a finite constant K_epsilon>=1 such that, for A,B>=1 and1<=D<=min(A,B), finite integer sets I subset[A,2A], J subset[B,2B], and rho in(0,1],

    # {(a,b) in I x J : gcd(a,b)>=D} >=rho |I||J|
    implies |I||J|<=K_epsilon rho^(-2-epsilon) AB/D^2. (1)

For instance its displayed constant is at most1000^(1+pi(p0(epsilon))), so this is a uniform finite choice of K_epsilon.
No numerical value of p0 or effective optimal constant is claimed.
Ordered pairs are meant; I and J need not be disjoint and diagonal pairs are allowed.

The newer source lead Haozhe Gou, arXiv:2604.21122v1, was screened at its actual HTML introduction, Corollary1.4 and Lemma3.1.
Its Corollary1.4 makes the same elementary two-variable lcm-to-gcd conversion below.
Its higher-dimensional statement and scale-epsilon large-sieve bounds are NOT inputs.
It supplies no adopted weighted/root theorem here.
The original Annals Duffin--Schaeffer paper was opened as a proof-method lead, but no theorem or proof from it is imported.
Thus only(1) is a new accepted external mathematical statement.

<a id="nonlinear-triple-weighted-two-band"></a>
## 1. Exact weighted estimate between two order bands

Put

    q=2+epsilon, theta=1/q, beta=2/q,
    r=1-theta=1-beta/2,
    B_epsilon=(4K_epsilon)^(1/q).                     (2)

Here2/3<beta<1 and1/2<r<2/3.
Let A,B>=1, let I and J be finite integer sets in[A,2A] and[B,2B], and attach arbitrary REAL weights0<=u_a<=2A,0<=v_b<=2B.
Let U=sum u_a and V=sum v_b.
For every real Y>0,

    sum_(a in I,b in J,lcm(a,b)<=Y)u_a v_b
       <=B_epsilon Y^beta (UV)^r.                    (3)

There is no totient assumption in this two-band statement.
It consequently covers the actual bounds w_a<=phi(a)<=a<2A on a half-open band[A,2A).

First consider unweighted subsets I',J'.
If Y<1, or one band has lower endpoint greater than Y, there are no compatible pairs.
In the remaining case Y>=max(A,B)>=1, every compatible pair has

    gcd(a,b)=ab/lcm(a,b)>=AB/Y.

Set D=max(1,AB/Y).
Then1<=D<=min(A,B), including the boundary AB/Y<1.
If E is the number of compatible pairs and E>0, use(1) with rho=E/(|I'||J'|).
It gives

    E<=K_epsilon^theta (AB/D^2)^theta
                            (|I'||J'|)^r
     <=K_epsilon^theta (Y^2/(AB))^theta
                            (|I'||J'|)^r.             (4)

The last inequality is equality in its scale factor when AB/Y>=1.
When AB/Y<1, it uses AB<=Y^2/(AB), equivalent to AB<=Y.
The zero-edge/empty-set cases satisfy(4) directly, without introducing rho=0 into(1).

For weighted sets write f_a=u_a/(2A), g_b=v_b/(2B), both in[0,1].
For s,t in[0,1], let I_s={a:f_a>s}, J_t={b:g_b>t}.
The identity f_a g_b=int_0^1 int_0^1 1_(a in I_s,b in J_t) ds dt is an elementary finite level-set integration.
Apply(4) to each pair of level sets and integrate.
Since0<r<1, concavity gives

    int_0^1 |I_s|^r ds <=(sum_a f_a)^r,
    int_0^1 |J_t|^r dt <=(sum_b g_b)^r.

Multiplication by4AB yields

    4AB*K_epsilon^theta*(Y^2/(AB))^theta
         *(U/(2A))^r*(V/(2B))^r
       =(4K_epsilon)^theta Y^(2theta)(UV)^r,

which is(3).
All sums are finite; no convergence or probabilistic rounding assumption is hidden.
The transfer by finite level sets is elementary, and is not claimed as a new general integration principle.
Crucially, the exponent beta is LESS THAN1.
Equation(3) is not the false linear short-pair estimate.

<a id="nonlinear-triple-scale-mass-bound"></a>
## 2. The actual distribution across order bands

Let S be any nonempty finite set of positive integers and give each a in S an arbitrary real weight0<w_a<=a.
The original actual setting w_a in Z_(>0), w_a<=phi(a), is a specialization.
Put W=sum_(a in S)w_a.
Fix an integer X>=1 and define the eligible bands

    S_k={a in S: 2^k<=a<2^(k+1), a<=X},
    W_k=sum_(a in S_k)w_a,
    L=1+floor(log_2 X), 0<=k<L,
    Z=sum_(k=0)^(L-1) W_k^r,
    L_eff=(sum_(k=0)^(L-1)(W_k/W)^r)^(2/beta).       (5)

If no order is eligible, define L_eff=0.
Orders above X remain in W but contribute no compatible triple.
When there is eligible mass,0<L_eff<=L.
Indeed concavity or Holder gives sum_k(W_k/W)^r<=L^(1-r)(sum_k W_k/W)^r<=L^(beta/2).
L_eff is simply the displayed real function of the actual eligible masses; it need not be an integer, and may be below1 when much of W lies above X.

Define the eligible short-pair mass at real Y>0 by

    P_2^X(Y)=sum_(a,b in S, a<=X,b<=X,lcm(a,b)<=Y)w_a w_b.

Apply(3) to every ordered band pair with A=2^k,B=2^l and the actual weights.
Summing preserves every diagonal, repeated label and pair orientation.
It proves

    P_2^X(Y)<=B_epsilon Y^beta Z^2
            =B_epsilon Y^beta W^(2-beta) L_eff^beta.  (6)

If Y<1 the left side is zero and the inequality still holds.
If Y>X, there is no extension of S beyond its already defined eligible set.
Empty bands make zero contributions.
The bound is uniform over all prime supports and all positive-integer orders; no bounded-union-prime hypothesis is imposed.

When exactly M occupied bands carry all W equally, the formula gives L_eff=M.
Therefore the generic inequality L_eff<=L cannot be replaced by a universal constant from the mass algebra alone.
This observation is not an actual fixed-positive-density counterexample: no compatible-triple property is asserted for those formal equal masses.
The unresolved logarithmic loss cannot simply be erased by concavity.

<a id="nonlinear-triple-capture-theorem"></a>
## 3. An unconditional logarithmic-loss capture theorem

For the same actual array and X, set

    h(n)=sum_(a in S,a divides n)w_a,
    H_X=max_(integer1<=n<=X)h(n),
    U_X(a,b)=sum_(c in S,lcm(a,b,c)<=X)w_c,
    T_X=sum_(a,b,c in S,lcm(a,b,c)<=X)w_a w_b w_c.

Suppose0<delta<=1 and T_X>=delta W^3.
In particular some orders are eligible and L_eff>0.
Then

    H_X >= c_epsilon delta^(2+epsilon/2)
                         W^2/(X L_eff)
         >=c_epsilon delta^(2+epsilon/2)
                         W^2/[X(1+floor(log_2 X))],
    c_epsilon=1/[2(2B_epsilon)^(1/beta)]>0.           (7)

This conclusion is UNCONDITIONAL apart from the explicitly accepted external theorem(1).
It assumes neither the refuted universal K nor the refuted linear-in-density bound.
All constants depend only on epsilon, not X,W,number of groups,prime supports or the polynomial degree.

Here is the complete residual and splitting argument, retaining the mechanism already proved in C86/C91.
For a pair with L0=lcm(a,b)<=X, put R0=floor(X/L0).
For each compatible third order c, its residual r(c)=c/gcd(c,L0) satisfies1<=r(c)<=R0, and lcm(a,b,c)=L0*r(c).
Each fixed residual bucket has total mass at most H_X, because all its orders divide the ONE integer n=L0*r<=X.
Therefore

    U_X(a,b)<=R0 H_X<=X H_X/L0.                       (8)

If L0>X its true link is zero.
This argument requires neither integer weights nor all triples compatible; in actual arithmetic it retains complete integer groups.

Choose the positive real threshold

    Y=(W/L_eff)*(delta/(2B_epsilon))^(1/beta).         (9)

For pairs with lcm<=Y use only U_X(a,b)<=W and(6).
Their contribution divided by W^3 is at most delta/2.
For all remaining eligible pairs, (8) gives U_X(a,b)<=XH_X/Y, whether or not they have a positive link.
The sum of their pair weights is at most W^2.
Hence

    delta<=T_X/W^3
           <=B_epsilon(Y L_eff/W)^beta+XH_X/(YW)
            =delta/2+XH_X/(YW).

Rearranging and substituting(9) proves(7), since1+1/beta=2+epsilon/2.
If Y<1 the short part is empty and its asserted upper bound remains valid; if Y>X the long part is empty and the displayed upper bound still holds, so a putative conflicting parameter choice simply cannot meet the assumed density.
No integrality rounding or enlarged time window is used.
X=1 and all repeated-label cases are included.

For example fixing epsilon=1/2 gives a definite positive constant c_(1/2) and density exponent9/4.
With fixed delta,gamma,C>0, W>=gamma*d and X<=C*d, the general conclusion is

    H_X >= [c_(1/2) delta^(9/4) gamma^2/C]
                      d/[1+floor(log_2(Cd))].         (10)

This improves the previously available C91 lower order d^(3/4)/sqrt(log d) to d/log d, with all parameters fixed.
It is STILL sublinear in d and by itself does not discharge L168's uniform eta*d gate.
No claim of asymptotic sharpness or optimal density exponent is made.

<a id="nonlinear-triple-bounded-scale-income"></a>
## 4. Positive income with bounded scale-mass factor

Fix epsilon in(0,1),0<delta,gamma<=1,C>0 and B0>0.
Consider an ACTUAL monic irreducible nontorsion integer-unit polynomial P of original degree d, a good prime p, and a nonempty selection of COMPLETE occurring residue-order groups S with w_a<=phi(a), W>=gamma*d.
Suppose an integer1<=X<=C*d satisfies

    T_X>=delta W^3, L_eff<=B0.                        (11)

Then (7) gives a SINGLE integer n<=X<=C*d with

    h(n)>=[c_epsilon delta^(2+epsilon/2) gamma^2/(C B0)]d,
    A_p(n)>=eta*d,
    eta=[c_epsilon delta^(2+epsilon/2) gamma^2/(C B0)]log2>0.
                                                               (12)

The maximum H_X is attained on the finite integer range; its numerical location is not claimed to have been enumerated.
A common finite bound on the number of occupied dyadic order bands implies(11)'s L_eff bound.
More generally the exact nonuniform masses may give a substantially smaller L_eff.
This sufficient condition has no restriction on the UNION of order primes and differs from C97's common-prime-pool hypothesis.
Neither condition is asserted to follow from the other in full generality.

The full original norm and local income remain

    D_n=Norm_(Q(alpha)/Q)(alpha^n-1)
       =Res(P,t^n-1)=product_(all d original roots)(alpha_i^n-1),
    C_n=|D_n| in Z_(>0),
    A_p(n)=(log p)v_p(C_n)
          =(log p)sum_(all original p-adic roots)v_p(alpha_i^n-1).

At a good prime every selected returning root contributes at least one to its normalized valuation; all remaining roots have nonnegative valuations.
This is exactly [C256's good-prime floor](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail), with actual higher/exceptional depths kept on the left, including p=2.
Thus A_p(n)>=h(n)log p>=h(n)log2 at the SAME n, proving(12).
No smaller field for alpha^n, selected norm, content multiplication or depth-one equality is substituted.
The auxiliary remains the single integer polynomial t^n-1 at its complete degree n, content1 and coefficient squared norm2; there is no packet denominator or missing cofactor.

The accepted [L168 finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) now gives its strict positive m(P)>m0(C,eta)>0 at its existing actual norm-tower, finite-degree-escape and external-source scope.
This is a positive measure theorem for the precisely specified class(11), not a new uniform result for every P.

Consequently, along any hypothetical sequence with total m(P)->0, fixed gamma,delta,C and actual positive-triple-density certificates of the above type, L_eff must tend to infinity.
Otherwise an infinite subsequence would have L_eff<=B0 for some fixed B0 and contradict the same positive bound.
This necessary escape concerns the actual distribution of root mass across dyadic order magnitudes, not merely the number of distinct orders or distinct primes.
It supplies no proof that the positive-density certificates themselves exist near one.

<a id="nonlinear-triple-history-and-limits"></a>
## Outcome, failed shortcuts and author limits

The starting general no-loss question remains OPEN.
The actual progress is the general bound(7), its explicit d/log d consequence and a new positive class with uniformly bounded L_eff, using a published theorem at precisely stated scope.
This is more than a renamed equivalent open assumption: the required weighted pair estimate(6) has a complete proof from(1), and (7) is unconditional for every finite capacity array in its domain.
The bounded scale-mass hypothesis is only needed when extracting a positive fraction of original degree.

The source's two-variable GCD estimate does not directly apply to root multiplicities: simply replacing |I| by sum w_a without the level-set transfer would be unjustified.
Nor does its dyadic form directly yield a global uniform constant: summing bands produces the factor L_eff.
The complete calculation retains both effects.
The elementary lcm-to-gcd conversion is credited as known, explicitly appearing also in Gou Corollary1.4; no novel arithmetic identity is claimed.

An alternative contemplated fractional moment bound sum_(a,b)w_a w_b/lcm(a,b)^s<=C_s W^(2-s),0<s<1, would remove the scale loss through the residual inequality, but it was neither proved nor refuted here and is NOT an input or an asserted equivalent theorem.
No formal or actual counterexample is fabricated from the failure of a critical exponent or a larger real-weight operator inequality.
The independently assigned squarefree-divisor-family analysis remains with averaged_lcm; none of that author's new, not-yet-adopted results is needed for this proof.

The author checked all real/zero weights at the band level, empty sets and zero-edge branches, exact GCD-theorem scale hypotheses including AB/Y<1, ordered diagonal conventions, finite level-set integrals, concavity exponents and cancellation of A,B, full eligible-band normalization including mass above X, L_eff>0 under positive triple density, the two appearances of W in the residual split, thresholds below1 or above X, the exponent2+epsilon/2, comparison with C91, and every original-norm/depth/cost interface.
These are AUTHOR checks.
An independent whole reviewer is required before organizing adoption.
No new native mathematical program, numerical source constant or formal verification occurred.

<a id="nonlinear-triple-stopped-checkpoint"></a>
## Author preservation checkpoint; execution stopped before source organization or review

2026-10-13T05:02.
Root reported the authenticated weekly account-window change and instructed all authors to stop new exploration and review under Yin's execution policy.
This checkpoint preserves ONLY the arguments already developed and saved above before that instruction: the exact source statement, weighted two-band derivation, general scale-mass estimate, residual split, d/log d improvement and bounded-L_eff actual-income consequence.
It starts no additional proof, acquisition or review.

The entire artifact is an UNADOPTED AUTHOR DRAFT.
No independent whole review, actual Claim extraction, extraction review or Task acceptance has occurred.
Root explicitly confirmed during preservation closeout that source registration was NOT performed: no GW21 bibliography/registry entry or source-local U exists, and this author authored NO source-local U/readme.
The proposed source key remains pending.
The actual publisher URL, edition, theorem locator, precise hypotheses and statement-only inspection boundary are retained above so that source organization can resume without claiming unavailable evidence.
There are no links to nonexistent GW21 canonical source files.
No final material-validation command was run after the stop.

On an explicitly authorized resumption in a valid execution window: first verify the actual GW21 registration/acquisition outcome, then create the exact source-local statement/applicability record, and arrange a noncontributing WHOLE review of this complete saved argument and its actual interfaces.
Only after those steps consider a fixed Claim and a different actual-extraction review.
The fully general fixed-positive-density/no-loss bridge and near-one coverage remain unresolved.

<a id="nonlinear-triple-resumed-entire-freeze"></a>
## Resumed source organization and entire author freeze

2026-10-13T05:09.
This author resumed ONLY source organization and preparation of the already-developed argument for whole review; no new mathematical exploration or change of theorem was undertaken.

Root registered GW21 in the canonical bibliography and registry at13:07.
Both local-download attempts failed, so there is no retained GW21.pdf; the actual online published theorem remains the inspected source.
This author created [GW21-U001](../audits/literature/GW21/Yin_U001.md#gw21-u001) and its source-local entrance, recording the exact published theorem, finite p0(epsilon) dependence, online-only access, published versus arXiv-v2 distinction and statement/applicability acceptance with no complete source-proof audit.
The source citation above now points to that actual fixed input.
The13:02 checkpoint remains true as historical preservation and is superseded only as to current execution/source-organization availability.

ENTIRE AUTHOR FREEZE: preserve the original question/search and source account, equations(1)--(12), all general real-weight/actual-root domains, exact two-band proof, finite level-set transfer, L_eff summation, residual split and endpoint cases, d/log d improvement, bounded-L_eff original-norm consequence, remaining no-loss/near-one gaps, failed/unproved shortcuts and stopped checkpoint.
No independent project review or fixed Claim acceptance is asserted yet.
A noncontributor must review this entire artifact together with its exact new GW21-U001 and existing C91/L74/L168 interfaces.
The sole new external mathematical dependency is the exact GW21 theorem; Gou and the Annals paper remain source-screening context only.

2026-10-13T05:11.
Final ENTIRE delivery freeze after source-file creation and successful scoped material validation of D24 and GW21-U001.
The13:09 entry records the start of this source-organization closeout; this13:11 freeze is the completed artifact supplied for whole review.
No mathematical statement or proof changed during the closeout.
