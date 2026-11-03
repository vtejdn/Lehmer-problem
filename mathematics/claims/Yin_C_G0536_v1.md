---
author: Yin
---

# Exponential invisibility of complete cyclic norms to any fixed finite prime set

The complete original mathematical argument is retained from [L413](../ledger/Yin_L_G0413_v1.md#unit-prefix-reuse-boundary).
Its original contributions, fixed inputs, useful failures, source inspection and native-execution limits are preserved.
The [original review](../audits/reviews/Yin_R_G0421_v1.md#fixed-prime-invisibility-whole-independent-finding) keeps its actual original L/J/source bindings, date, relationship declaration and checked scope; it is not retrospectively bound to this C.
The current constructor has read the original proof and historical reviews; any current whole finding by this constructor is SELF.

## Statement

For a nontorsion algebraic unit alpha with actual degree d and minimal polynomial P, put C_n(P)=abs Norm_(Q(alpha)/Q)(alpha^n-1), with every original embedding retained.
Absolute norm1 is equivalent to alpha^n-1 being a unit already in Z[alpha]; no equivalence of nonunit Smith profiles in different orders is asserted.

Fix any finite nonempty set S of rational primes, Q=product_(p in S)p and p0=min S.
For every integer r>=2, d=2r, there exists a monic irreducible reciprocal nontorsion integer-unit polynomial P of actual degree d such that every p in S is a good prime, P mod p is irreducible and every reduced root has exact order p^r+1.
For every integer n>=1 and p in S,

    v_p(C_n(P))=0 if p^r+1 does not divide n,
    v_p(C_n(P))>=d if p^r+1 divides n.

Thus gcd(C_n(P),Q)=1 for every1<=n<=p0^r, and for every fixed C>0 the entire S-part of all norms with1<=n<=Cd is1 for every sufficiently large r.
The complete logarithmic measure satisfies

    log(d+1)<=m(P)<=log((Q+4)d).

In particular m(P)=log d+O_S(1); no bounded-total-measure or near-one counterexample is obtained.
An empty S is vacuous.
No full cyclic norm is asserted equal1 and no outside-prime income is bounded.
The construction uses the original companion lattice and retains all depths and original degree.
The original unit-prefix question is a specialization of the accepted Ste12 interface, with its unbounded logarithmic time factor and merely historical conjecture/computation reports.
Those comparison results are not premises of this construction and give no automatic positive original-degree-normalized income.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision complete-fixed-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:21 |
| status | open |
| reason | Register the exact complete statement and original argument at their responsible C home after content/dependency judgment. Actual current whole checking and adopting review remain separate; original mathematical, source, native, contribution and historical review boundaries are retained without research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Every finite nonempty rational-prime set, every even degree2r>=4, original-order cyclic norms, actual irreducible reciprocal nontorsion units, complete valuation dichotomy and exponential window, both total-measure bounds and classical-prefix/source limits. |
| argument | [Entire complete argument](#argument) | Every finite nonempty rational-prime set, every even degree2r>=4, original-order cyclic norms, actual irreducible reciprocal nontorsion units, complete valuation dichotomy and exponential window, both total-measure bounds and classical-prefix/source limits. |
| dependency | [Exact fixed input](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Accepted finite-field existence/cardinality, Frobenius, extension-degree and separability statements; multiplicative cyclicity is proved locally. |
| dependency | [Exact fixed input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exactly #smy08-height-normalization: Complete Mahler/Jensen circle identity including root multiplicities and integrable circle zeros, used only for M(P)<=coefficient l1. |
| support | [Exact fixed input](../audits/literature/Ste12/Yin_U001.md#ste12-u001) | Already inspected source definitions, Corollaries1--2 and historical e(d) report; comparison and attribution only, no new source reading or original-proof audit. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:36 |
| status | proved |
| reason | Under the current human maintenance authorization, adopt the exact complete current statement and original fixed argument after the actually completed R737 constructor SELF whole inspection. Preserve original author/source/native evidence, old R bindings and relationships, and all initial open registrations or precision successors. No new research or producer is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Every finite nonempty rational-prime set, every even degree2r>=4, original-order cyclic norms, actual irreducible reciprocal nontorsion units, complete valuation dichotomy and exponential window, both total-measure bounds and classical-prefix/source limits. |
| argument | [Entire complete argument](#argument) | Every finite nonempty rational-prime set, every even degree2r>=4, original-order cyclic norms, actual irreducible reciprocal nontorsion units, complete valuation dichotomy and exponential window, both total-measure bounds and classical-prefix/source limits. |
| dependency | [Exact fixed input](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Accepted finite-field existence/cardinality, Frobenius, extension-degree and separability statements; multiplicative cyclicity is proved locally. |
| dependency | [Exact fixed input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exactly #smy08-height-normalization: Complete Mahler/Jensen circle identity including root multiplicities and integrable circle zeros, used only for M(P)<=coefficient l1. |
| support | [Exact fixed input](../audits/literature/Ste12/Yin_U001.md#ste12-u001) | Already inspected source definitions, Corollaries1--2 and historical e(d) report; comparison and attribution only, no new source reading or original-proof audit. |
| review | [Complete current SELF finding](../audits/reviews/Yin_R_G0737_v1.md#current-g414-complete-self-finding) | Entire exact current Statement and complete Argument with every listed actual input, original field/core/law/time/cost boundary and no new mathematical producer; constructor SELF, not independent. |

## Complete original argument

<a id="argument"></a>

### Original account: Classical unit-prefix rigidity and exponential invisibility to fixed prime sets

Date: 2026-10-18T16:26.
Human author Yin.
Root assigned the original complete cyclic-unit-prefix question and supplied no proof step.
The loglog_cyclic_review agent performs the reuse comparison and develops the changed construction below.
No extension of J107 is made.

<a id="unit-prefix-reuse-boundary"></a>
## 1. The original question is an existing exceptional-unit problem

For an original nontorsion algebraic unit alpha of degree d, write

    C_n(P)=abs Norm_(Q(alpha)/Q)(alpha^n-1).

These are COMPLETE nonzero integer norms, with every original embedding retained.
The condition C_1=...=C_N=1 is exactly the statement that every alpha^n-1 for1<=n<=N is an algebraic integer unit.
It is independent of whether one tests the inverse in the maximal order or the original order Z[alpha]: multiplication by alpha^n-1 has determinant +/-1 on the original power basis precisely in this case, and its integral adjugate then supplies its inverse in Z[alpha].
This observation does not identify higher nonunit Smith profiles in different orders.

The primary [Stewart2012 interface](../audits/literature/Ste12/Yin_U001.md#ste12-u001), Exceptional units and cyclic resultants, defines this prefix length E0(alpha).
Its Corollary1 bounds E0 by c d(log(d+1))^4/(log log(d+2))^3 with an effectively computable absolute positive c.
Its Corollary2 already treats a constant prefix of absolute cyclic resultants, not only the value1.
The actual printed408--409/PDF2--3 statements were read from the institutional primary PDF and retained in Ste12-U001 with the exact bibliographic/artifact registration.
No original proof audit is claimed, and the construction below does not depend on either theorem.

Ste12 printed417/PDF11 already reports e(d)=d for d<=6 and the conjecture e(d)<d for d>=7, with the paper's standing nonzero hypothesis in the definition of e(d).
That directly inspected primary passage is also retained in Ste12-U001.
The already retained [Ste13 source](../audits/literature/Ste13/readme.md#ste13-discovery-screen) is a DIFFERENT paper; its Section6 repeats this history and was also read, without changing the earlier source screen's scope.
These are historical conjecture/computation reports, not independently reproduced computations, an accepted linear theorem or a claim about its current open status.
Thus a universal fixed-linear unit-prefix theorem is not being proposed here as a new question.
An exact-unit rigidity theorem would in any event guarantee only some log C_n>=log2; after division by the ORIGINAL d this alone is not the positive fixed norm density required by C147.

The local reuse screen also read [L74 complete original aggregation](../ledger/Yin_L_G0074_v1.md#aggregate-cyclic-norm-criterion), [L76's finite prime-exponent witness](../ledger/Yin_L_G0076_v1.md#finite-cyclic-norm-prime-witness), [Dim16's degree/height-dependent all-index bound](../audits/literature/Dim16/Yin_U001.md#dim16-cyclic-all-index), and [L188's complete cyclotomic-layer average](../ledger/Yin_L_G0188_v1.md#complete-cyclic-layer-average).
They already supply finite or conditional income with their actual time and measure costs.
L188 and [L217](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope) also construct actual reciprocal local-data controls, but do not state the simultaneous complete absence from ANY supplied finite prime set in the exponentially long prefix proved next.
The current question therefore changes from global unit-prefix rigidity to the precise limitation of a preassigned finite arithmetic-prime test.
No absence-of-priority or novelty claim is made.

<a id="fixed-prime-invisibility-statement"></a>
## 2. Changed exact statement

Fix ANY finite nonempty set S of rational primes and put Q=product_(p in S)p and p0=min S.
For every integer r>=2, put d=2r.
There exists an ACTUAL monic irreducible reciprocal nontorsion integer-unit polynomial P of degree d such that every p in S is a good prime, P mod p is irreducible, and its roots all have exact order p^r+1.
The complete original cyclic norms then satisfy

    v_p(C_n(P))=0  if p^r+1 does not divide n,
    v_p(C_n(P))>=d if p^r+1 divides n.                (1)

In particular

    gcd(C_n(P),Q)=1 for every1<=n<=p0^r.             (2)

The original total logarithmic measure can be kept within

    log(d+1)<=m(P)<=log((Q+4)d).                     (3)

For every fixed C>0, the entire S-part of ALL complete cyclic norms in1<=n<=Cd is therefore1 for all sufficiently large r.
This is a simultaneous zero-income obstruction for the supplied finite prime set, even with actual irreducibility, reciprocity, good reduction and a logarithmic rather than linear measure upper bound.
It is NOT a statement that the full cyclic norms equal1, nor a near-one or bounded-total-measure counterexample.
In fact (3) gives m(P)=log d+O_S(1), making the unbounded-total-measure boundary explicit.
An empty S is vacuous and may be enlarged to{2} if a nontrivial control is wanted.

<a id="fixed-prime-invisibility-proof"></a>
## 3. Complete finite-field and integral construction

The established finite-field existence and Frobenius statements are [Hun74-U006](../audits/literature/Hun74/Yin_U006.md#hun74-u006), at their accepted statement/applicability scope.
Its cyclic Galois group is not silently identified with the multiplicative group.
Here is the additional elementary multiplicative argument.
For a finite subgroup G of a field's multiplicative group, let e be the least common multiple of all element orders.
For each prime power dividing e maximally, choose an element whose order has that prime-power part and take a power to isolate it.
The product of these commuting elements of coprime orders has order e.
Every element of G is a root of X^e-1, so |G|<=e, while Lagrange gives e<=|G|.
Thus G is cyclic, and a finite field with p^(2r) elements contains an element eta of exact order p^r+1.

This eta has degree EXACTLY2r over F_p.
If its degree were a proper divisor k of2r, then k<=r and eta would lie in the field with p^k elements.
Its order would then divide p^k-1<=p^r-1, contradicting p^r+1.
The Frobenius identity eta^(p^r)=eta^(-1) shows that inversion permutes its conjugates.
Its monic minimal polynomial g_(p,r) is therefore reciprocal of degree2r and has constant term1, with distinct roots of exact order p^r+1.
The constant term can also be checked by pairing inverse conjugates; none is equal to its inverse because p^r+1>2.

Apply coefficientwise integer CRT to the r free reciprocal coefficients of the polynomials g_(p,r), for all p in S.
Choose the coefficient a1 of t^(d-1), also the coefficient of t, in its prescribed class modulo Q with

    2d<=a1<2d+Q.

Choose each remaining free coefficient a2,...,ar in a centered representative interval with absolute value at most Q/2.
Define the complete polynomial

    P(t)=t^(2r)+a1 t^(2r-1)+...+ar t^r+...+a1 t+1.

Then P reduces to g_(p,r) at every p in S.
It is irreducible over Q because any monic nontrivial integer factorization would reduce to a nontrivial factorization at one such prime.
It is a reciprocal integer-unit polynomial of original degree d.
Every reduction is squarefree, so no p in S divides its polynomial discriminant.

The sum of its complex conjugates is -a1, and hence at least one conjugate has modulus at least a1/d>=2, so P is nontorsion.
To price the TOTAL measure more precisely, put x_i=max(|alpha_i|-1,0).
Then sum_i|alpha_i|<=d+sum_i x_i and M(P)=product_i(1+x_i)>=1+sum_i x_i.
Consequently a1<=sum_i|alpha_i|<=d+M(P)-1 and M(P)>=a1-d+1>=d+1.
This proves the lower bound in (3) without confusing a house bound with the product measure.
For d>=4 its coefficient l1 norm is at most

    2+2(2d+Q)+(d-3)Q<=(Q+4)d.

The elementary circle bound M(P)<=sum_j|a_j| follows from [Smy08-U001's Mahler/Jensen circle identity](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), including its original-root multiplicities and integrable circle-zero convention, together with the pointwise coefficient bound on |P|.
It proves the upper inequality in (3) without requiring any further lower-bound theorem from that source unit.
No maximum-root estimate is incorrectly used as an upper bound for the product Mahler measure.

Let A be the original integral companion on Z[alpha].
Modulo p it acts on F_p[t]/g_(p,r), the actual field with p^d elements.
Multiplication by alpha^n-1 is invertible there if p^r+1 does not divide n, and is zero there otherwise.
In the first case det(A^n-I) is a p-adic unit.
In the second case every entry of A^n-I is divisible by p, so its determinant is divisible by p^d.
That determinant is the COMPLETE original field norm; it is nonzero because P is irreducible and nontorsion.
This proves (1), and p^r+1>p0^r for every p in S proves (2).
All initial depths are included in the zero statement; no deeper layer can contribute where the determinant is a p-adic unit.

<a id="unit-prefix-rigidity-income-boundary"></a>
## 4. What remains unproved

This construction closes a proposed inference from testing any fixed finite set of rational primes to actual global unit-prefix rigidity on the general reciprocal-unit domain.
It does not close such a test under an additional sufficiently small TOTAL measure assumption, since (3) explicitly excludes that regime.
It also does not give an upper bound for contributions from primes outside S.
Those contributions may already be large at small n.
No global complete cyclic norm has been computed in this construction.

The existing L409/L411 capacity laws remain fully consistent: at depth1 the entire local mass d activates at the label p^r+1, and all higher-depth labels are later multiples.
The exponential time is retained, not renamed a fixed multiple of d.
Likewise L74's full norm aggregation remains valid at each actual exponent.
A route to a uniform gap still needs actual positive d-scale complete norm income in a fixed degree-linear window, or a different fully charged arithmetic mechanism.
Neither historical exceptional-unit estimates nor finite-prime silence provides that missing input.

The newly read Stewart2012 interface is now retained at Ste12-U001, with exact source registration and separate proof-inspection limits.
No numerical source constant, factorization, norm scan or high-prime computation was executed.
The complete construction, original costs and source-inspection boundaries are retained here; the separate R finding owns independent review.
