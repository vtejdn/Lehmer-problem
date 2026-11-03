---
author: Yin
---
# Actual Salem two-five compatibility requires paid endpoint tail mass

Date: 2026-10-20T16:52.
Human author Yin.
This is a substantive continuation of the same actual endpoint-compatibility inquiry as [C201v1](Yin_C_G0201_v1.md#statement), whose complete proof and [adopted assessment](Yin_C_G0201_v1.md#decision-whole-reviewed-2026-10-21) remain unchanged.
The new proof compares the original field identity at the exterior trace and one interior trace, retaining the complete remaining product and the integer endpoint factor.
Root supplied the two-point direction, the symmetric scalar product bound, the finite constants and the extension retaining all M>=1.
The retained_methods_audit author verified and developed the exact two-point factorizations, all signs, polynomial bounds, tail charges and boundary cases.
Root also identified the existing degree-bound coverage; entropy_attainment_bridge located and checked its precise C134/R488 and C107 source/application interfaces.
These three agents are contributors to this revised account and cannot supply its independent whole review.
The older R632/R633 activities concern different arguments, and R488 reviews only the unchanged v1.
No mathematical program, numerical scan, new source acquisition or external theorem proof audit was used.

<a id="statement"></a>
## Exact statement and retained predecessor

Let P in Z[z] be the monic irreducible minimal polynomial of a genuine Salem number lambda>1.
Precisely, P has degree d=2r>=4, constant coefficient1 and reciprocal symmetry, its two real roots are lambda and lambda^(-1), and all its other roots are nonreal numbers of modulus1 paired by inversion.
Write

    P(z)=z^r T(z+z^(-1)),
    K=Q(lambda), delta_0=lambda+lambda^(-1),
    F=Q(delta_0), [K:F]=2, [F:Q]=r,
    m=m(P)=log lambda, x=delta_0-2=2cosh(m)-2>0.

Here m is the TOTAL logarithmic Mahler measure, and T in Z[X] is the actual monic irreducible trace polynomial.
Its other roots are distinct delta_j in(-2,2), with t_j=2-delta_j in(0,4), for1<=j<=r-1.
The polynomials C_k are defined by C_k(z+z^(-1))=z^k+z^(-k), so C_2(X)=X^2-2 and C_5(X)=X^5-5X^3+5X.
Use the actual divided trace values

    a=T(C_2(delta_0))/2=theta_2(delta_0),
    c=T(C_5(delta_0))/5=theta_5(delta_0),
    theta_p=rem_T(T(C_p))/p in Z[X], deg theta_p<r,
    p=2,5.

These are the nonzero integral elements of the specified trace order supplied by C201v1 and its accepted C153v2 input.
Assume the ACTUAL equality in F

    f=2c^2-3a^5=0.                                      (PT1)

No second residual equation, three-prime coordinate, g!=0 or trace-order-index condition is assumed.
Set

    M=|P(1)|=-T(2)=x product_(j=1)^(r-1)t_j in Z_(>0).

The symbol M denotes this integer endpoint value, not the multiplicative Mahler measure.

### A. Unchanged complete endpoint theorem

The whole [v1 theorem and its precise domain](Yin_C_G0201_v1.md#statement) are retained by dependency, with their complete proof in that fixed predecessor.
In particular, for a_k=C_k(2+x)-2 and q_k^+=a_k/x,

    75/64=M^(-3) [(q_5^+-1)^2/(q_2^+-1)^5]
                 product_j[(1+a_5/t_j)^2/(1+a_2/t_j)^5]. (PT2)

When M=1, at least one t_j<x(4+x)=4sinh(m)^2.
For its angle0<theta_j<pi, t_j=4sin(theta_j/2)^2 and sin(theta_j/2)<sinh(m); the inverse-sine bound is used only when sinh(m)<1.
No M>=2 contact assertion is imported from v1.

### B. Explicit two-point exclusion for every integer endpoint value

Choose any one interior trace and relabel it delta_1=2-t, where t=t_1>0.
Define the complete remaining sum, including every other interior trace, by

    S=sum_(j=2)^(r-1)1/t_j,
    tau=(x+t)S.

For r=2 this is the empty sum S=0.
For every input in the stated original domain, the following three inequalities cannot hold simultaneously:

    0<x<=1/1000, 0<t<=1/200, tau<=1/250.               (PT3)

Equivalently, if the two displayed small endpoint distances hold, actual f=0 forces tau>1/250.
This conclusion holds for every positive integer M, retaining its exact M^(-6) factor in the two-point product.
The selected interior trace need not be the nearest one.

### C. Unit endpoint value and the automatically selected nearest trace

Assume M=1 and0<x<=1/1000, and now choose t=t_1=min_j t_j.
Then the unchanged contact theorem gives t<x(4+x)<5x, and the sharper complete tail parameter necessarily satisfies

    sigma=x sum_(j=2)^(r-1)1/t_j>1/1000.               (PT4)

This stronger numerical corollary uses a separate sharper tail charge, not the implication tau<=1/250 from sigma<=1/1000.
The latter implication is not asserted.
An empty tail is included in the exclusion.
Neither conclusion asserts a second root at a fixed multiple of x: the full sum may receive contributions from many roots.

### D. Existing qualitative coverage of bounded-tail classes

Without requiring f=0 or M=1, every hypothetical sequence of genuine Salem inputs with m(P)->0 satisfies sigma->infinity for any choice of one excluded interior trace; consequently tau>=sigma also tends to infinity.
This follows from the accepted Dobrowolski benchmark and the old integer endpoint identity, with the complete elementary adaptation below.
Thus, for each fixed finite nonnegative tail bound, the corresponding bounded-sigma or bounded-tau class already has a qualitative positive Mahler gap from prior inputs.
Parts B--C retain explicit original-equation constraints and their stated constants; they do not claim new qualitative gap coverage, an unrestricted Mahler gap, or the existence of a near-one family.

<a id="argument"></a>
## Complete proof of the added conclusions

<a id="two-point-exact-original-products"></a>
### 1. Two original embeddings and both exact products

Part A is exactly the adopted [C201v1 statement](Yin_C_G0201_v1.md#statement), including its original-field interface and full proof.
The present proof uses that interface, and Part C additionally uses its strict M=1 contact.
The proof of Part B does not assume M=1 or infer any contact from it.
For a selected t define

    b_k=2-C_k(2-t), q_k^-=b_k/t, u=t/x>0,
    A_+=(q_5^+-1)^2/(q_2^+-1)^5,
    A_-=(q_5^--1)^2/(q_2^--1)^5,
    L_+=product_(j=2)^(r-1)
          [(1+a_5/t_j)^2/(1+a_2/t_j)^5],
    L_-=product_(j=2)^(r-1)
          [(1-b_5/t_j)^2/(1-b_2/t_j)^5].              (PT5)

The superscript minus is a label, not a sign in q_k^-.
All products over an empty tail equal1.
For the factorizations below, impose the explicit positive-factor domain q_k^+>1, q_k^->1 and0<b_k<t_j for every tail root and k=2,5.
Sections2--4 verify every one of these conditions in the two cases actually used.
Factoring the same monic original T gives

    T(C_k(2+x))
      =(a_k-x)(a_k+t) product_tail(a_k+t_j)
      =M(q_k^+-1)(1+q_k^+/u)
          product_tail(1+a_k/t_j),
    T(C_k(2-t))
      =(-b_k-x)(t-b_k) product_tail(t_j-b_k)
      =M(q_k^--1)(1+u q_k^-)
          product_tail(1-b_k/t_j).                    (PT6)

At the inner point the first TWO factors are negative and their product is positive; the remaining factors are positive in the declared domain.
At the outer point every factor is positive.
Since T is the irreducible minimal polynomial of delta_0, the embedding F->R sending delta_0 to delta_1 transports (PT1) to the actual values T(C_k(delta_1))/k.
Indeed the divided-remainder identity has the same evaluation at every root of T.
Clearing the original denominators2 and5 at each of these two embeddings therefore yields

    R_+:=T(C_5(2+x))^2/T(C_2(2+x))^5=75/64,
    R_-:=T(C_5(2-t))^2/T(C_2(2-t))^5=75/64.            (PT7)

Every denominator is nonzero and positive by the factors just identified.
Substitution into the actual ratios, including the selected interior root, gives

    R_+=M^(-3) A_+
          [u^3(u+q_5^+)^2/(u+q_2^+)^5] L_+,
    R_-=M^(-3) A_-
          [(1+u q_5^-)^2/(1+u q_2^-)^5] L_-.          (PT8)

These are exact finite identities, not limiting approximations or freely chosen trace tuples.
Their product retains M^(-6), which is at most1 because M is a positive integer.

<a id="finite-symmetric-scalar-bound"></a>
### 2. Uniform scalar bound on the complete selected pair

Assume only0<x<=1/1000 and0<t<=1/200 in this section.
Direct polynomial expansion gives

    q_2^+=4+x,
    q_5^+=25+50x+35x^2+10x^3+x^4,
    q_2^-=4-t,
    q_5^-=25-50t+35t^2-10t^3+t^4.                   (PT9)

Since x<=1, q_5^+<=25+96x<26 and q_2^+>=4.
For the minus values, t^2(35-10t+t^2)>0 shows q_5^->=25-50t>1.
Also

    q_5^--25=t(-50+35t-10t^2+t^3)<0,

because35t+t^3<1 on0<t<=1/200.
Thus q_5^-<=25, q_2^->39/10, b_5<=25t and b_2<=4t, while both q_k^->1 and q_k^+>1.
In particular

    0<A_+<625/243<3,
    0<A_-<576/(29/10)^5<3.                           (PT10)

For the last bound,29^5=20511149>19200000, which is equivalent to576<3(29/10)^5.
The two non-prefactor terms in (PT8) have positive denominators and are bounded above in product by

    H(v)=(26v+677)^2/[(39/10)v+1621/100]^5,
    v=u+u^(-1)>=2.                                   (PT11)

To see the exact cancellation, their upper envelope is

    u^3 (u+26)^2(1+26u)^2
       /[(u+39/10)^5(1+(39/10)u)^5].

The numerator paired product is u(26v+677), the denominator paired product is u[(39/10)v+1621/100], and the remaining powers of u cancel.
For v>=2 the logarithmic derivative of H is

    52/(26v+677)-1950/(390v+1621).

Its positive common denominator has numerator -30420v-1235858<0.
Consequently

    H(v)<=H(2)=729^2/(2401/100)^5
               =729^2/(49/10)^10
               <729^2/24^5<1/14.                    (PT12)

The final strict inequality follows from24^5=7962624 and14*729^2=7440174.
This bound holds for ALL u>0, without a compactness assumption on t/x.
It therefore covers an arbitrarily small u as well as any other positive ratio permitted by the finite hypotheses, with no unpaid uniform limiting step.
Combining (PT10)--(PT12) shows that the selected-pair part A_+ A_- times the two bracketed factors in (PT8) is strictly less than9/14.

<a id="complete-tail-all-endpoint-values"></a>
### 3. Complete tail charge and the all-M contradiction

Assume all three conditions in (PT3).
For every tail root, positivity of the summands gives

    b_5/t_j<=b_5 S<=25tS<=25tau<=1/10<1,
    b_2/t_j<=b_2 S<=4tS<=4tau<=2/125<1.              (PT13)

Together with Section2 this verifies the entire positive-factor domain needed in (PT6)--(PT8).
If the tail is empty these pointwise conditions are vacuous and L_+=L_-=1.
All logarithms below are ordinary real logarithms of positive factors.
Using log(1+z)<=z for z>=0 and discarding only the nonpositive denominator-log terms gives

    log L_+<=2a_5 S<=52xS.

For the inner product, the numerator-log terms are nonpositive.
The elementary inequality -log(1-z)<=z/(1-z), for0<=z<1, follows by integrating1/(1-s)<=1/(1-z) on0<=s<=z.
It gives, using the same common bound for every tail factor,

    log L_-<=5b_2 S/(1-4tau)
              <=20tS/(1-4tau).

Since tau<=1/250, one has20/(1-4tau)<=2500/123<52.
Hence the COMPLETE, degree-independent tail budget is

    log(L_+ L_-)<=52(x+t)S=52tau<=26/125<1/4,
    L_+ L_-<4/3.                                    (PT14)

For the last inequality, exp(y)<=1/(1-y) for0<=y<1 follows termwise from the power series; alternatively use exp(1/4)<4/3 and the strict preceding upper bound.
No negative term was estimated by an unsupported positive approximation, and no tail root was omitted.
Equations (PT8), (PT10)--(PT14), and M^(-6)<=1 now imply

    (75/64)^2=R_+ R_-<1*(9/14)*(4/3)=6/7<1,          (PT15)

contradicting75/64>1.
This proves Part B for every positive integer M without dropping its endpoint cost.

<a id="unit-endpoint-sharper-tail-corollary"></a>
### 4. Sharper charge under automatic M=1 contact

Suppose M=1 and0<x<=1/1000, and select the nearest interior root.
Part A gives

    0<t<x(4+x)<5x<=1/200.                            (PT16)

Assume for contradiction sigma=xS<=1/1000.
For a nonempty tail, each x/t_j<=sigma, so t_j>=1000x.
The polynomial bounds in Section2 imply b_5<=25t<125x<t_j and b_2<=4t<20x<t_j.
Thus the same positive-factor domain and exact formulas apply; for an empty tail they apply without further conditions.
The outer tail bound becomes log L_+<=52sigma.
For the inner tail, every b_2/t_j<=b_2S<=20sigma<1, so the same logarithmic inequality gives

    log L_-<=5b_2S/(1-20sigma)
              <=100sigma/(1-20sigma).

Both displayed upper bounds increase with sigma on the stated interval.
Therefore

    log(L_+ L_-)<=52sigma+100sigma/(1-20sigma)
                 <=13/250+5/49=1887/12250<1/4.       (PT17)

The estimate also holds with value0 when S=0.
Again L_+ L_-<4/3, and the scalar bound from Section2 gives exactly the contradiction (PT15).
This proves the strict inequality (PT4), including its proposed equality boundary.
It uses no inference of (PT3) from the sigma bound and no choice of a limiting value of u.

<a id="prior-dobrowolski-coverage-of-bounded-tail"></a>
### 5. Prior coverage: a bounded tail already excludes near-one inputs

This subsection no longer assumes f=0 or M=1; retain only the genuine Salem domain and choose any one interior trace to omit from S.
For r>=4, all r-2 remaining distances are strictly less than4, and x=2cosh(m)-2>=m^2.
Consequently

    sigma=xS>x(r-2)/4>=dx/16>=dm^2/16.               (PT18)

This strict comparison is used only for r>=4, not for the r=2 empty sum.
The old [C107 endpoint bound](Yin_C_G0107_v1.md#signed-norm-gap-assessment), equation13, gives

    x>4^(-(r-1)).                                    (PT19)

It follows directly from M=x product_j t_j>=1 and product_j t_j<4^(r-1).
Thus m->0, and hence x->0, forces r and d to tend to infinity: every bounded degree has a fixed positive right side in (PT19).
This handles all small degrees, including r=2 and r=3, without applying a large-degree logarithmic estimate there.

The already adopted [C134 inverse-measure comparison](Yin_C_G0134_v1.md#two-node-degree-and-inverse-measure-scales), equation18, states the safe bound

    m(P)>=1/[2400(log d)^3], d>=exp(exp1).            (PT20)

Its input is the accepted Dobrowolski statement in the retained Smy08 edition, not a newly selected Voutier constant.
The precise source equation and conversion were checked in [R798, Section5](../audits/reviews/Yin_R_G0798_v1.md#two-node-whole-independent-finding): Smy08 printed326 equation11 bounds the MULTIPLICATIVE Mahler measure from below by1+(1/1200)(log log d/log d)^3 on the nontorsion algebraic-integer domain, and log(1+y)>=y/2 for0<=y<=1 yields (PT20) when log log d>=1.
The present lambda is a nonzero nontorsion algebraic integer of original degree d, and m is its total logarithmic measure, so every hypothesis matches.
The existing source acceptance and original-proof inspection limits are unchanged; no disputed resultant explanation or Voutier improvement is used.
For sufficiently large d, (PT18)--(PT20) give

    sigma>d/[16*2400^2*(log d)^6]->infinity.          (PT21)

The final divergence follows by writing d=exp(y), since exp(y)/y^6 tends to infinity.
Combined with bounded-degree escape from (PT19), this proves Part D along every hypothetical near-one sequence.
Since tau=(x+t)S>=xS=sigma, the same statement holds for tau.

Equivalently, a fixed finite upper bound on sigma forces d to be bounded by (PT21), with all remaining small degrees finite in number; (PT19) then supplies a positive lower bound for x and hence for m.
A bound on tau implies the same bound on sigma.
This is a direct adaptation of already accepted degree and endpoint inputs, not a new qualitative gap theorem or a claim of an actual near-one sequence.
The explicit two-point constants in Parts B--C are retained for their original f=0 constraints, without claiming a comparison to the best numerical bound obtainable from other results.

<a id="scope-inputs-and-review-boundary"></a>
## Scope, exact inputs and review boundary

The complete v1 endpoint product/contact/angle theorem remains fixed and independently adopted at its own version.
Its original proof is not duplicated, altered, or retrospectively covered by a new author check.
The new content is the exact two-embedding product, the fully paid finite tail exclusions, and the explicit comparison with existing qualitative coverage.
All denominators, trace embeddings, original degree labels, positive integer endpoint factors and empty-product cases are retained.
There is no assertion that an actual f=0 input exists, that all small-measure Salem inputs have a bounded tail, or that aggregate tail mass forces a fixed number of roots at comparable endpoint scale.
No arbitrary reciprocal extension, original-full-norm/Haar identification, canonical/unreduced G substitution or solution of the varying-P discrepancy is made.
The unrestricted G0001 objective and the remaining original comparison obligations stay unresolved.

| Input | Actual role and limit |
| --- | --- |
| [C201v1 complete theorem](Yin_C_G0201_v1.md#statement) | Logical dependency for the unchanged endpoint theorem, actual original trace/quotient domain and strict M=1 contact; its exact all-M cost remains intact. |
| [C134 accepted degree comparison](Yin_C_G0134_v1.md#two-node-degree-and-inverse-measure-scales) | Logical dependency only for the already-covered qualitative tail conclusion, specifically equation18 and its total-measure/large-degree scope; not needed for Parts B--C. |
| [C107 endpoint identity and floor](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Attribution for the independently rederived bounded-degree floor (PT19); no new norm income or uniform-in-degree bound. |
| [R488 v1 whole finding](../audits/reviews/Yin_R_G0488_v1.md#salem-endpoint-contact-whole-finding) | Existing review of the unchanged predecessor and its precise trace/source interfaces, with initial review context currently unknown; not a review of this revised proof. |
| [R798 original degree/source finding](../audits/reviews/Yin_R_G0798_v1.md#two-node-whole-independent-finding) | Existing evidence for C134 equation18, with initial review context currently unknown, exact source conversion and inspection limits, reused only at that scope. |

The assigned contributing author read back the entire new fixed account and checked exact expansions, both inner negative factors, M^(-6), the all-u scalar comparison, both complete tail charges and the prior-coverage distinction.
This is author checking, not an independent finding or adoption.
A separate noncontributor whole review must cover Parts A--D, every new proof step, the reused inputs and their source/application boundaries.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-21)

## Assessment history

### Decision whole-reviewed-2026-10-21

| Field | Value |
| --- | --- |
| date | 2026-10-20T16:58 |
| status | proved |
| authority | Internal adoption within Yin's selected retained-draft inquiries. |
| reason | Adopt complete Parts A--D and PT1--PT21 through actual whole independent R490. Preserve the two original embeddings, all integer endpoint values and M^(-6), exact finite scalar/full-tail costs, separate sharper M=1 charge, arbitrary selected root and empty-tail boundaries. The accepted Dobrowolski/endpoint chain already gives bounded-tail qualitative coverage; the new result is the explicit original f=0 two-point constraint, not a new qualitative gap class or the unrestricted transfer. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Parts A--D, original genuine Salem domain and actual f-only identity, inherited v1 theorem, all-M finite exclusion, sharper M=1 tail necessity and separately identified prior qualitative coverage. |
| argument | [Complete revised argument](#argument) | All PT1--PT21, actual embedding/sign identities, complete scalar and tail inequalities, empty-tail and all-u boundaries, degree-source adaptation and limitations. |
| dependency | [Unchanged adopted endpoint theorem](Yin_C_G0201_v1.md#statement) | Actual trace/quotient domain, complete predecessor theorem and M=1 strict contact; whole v1 argument and R488 remain at their fixed scopes. |
| dependency | [Accepted original-degree benchmark](Yin_C_G0134_v1.md#two-node-degree-and-inverse-measure-scales) | Only equation18's total m>=1/[2400(log d)^3] for d>=exp(exp1), reused in the separate prior-coverage proof. |
| support | [Earlier integer endpoint floor](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Attribution and scope for M=x product t_j and x>4^(-(r-1)); rederived for bounded-degree escape without new uniform income. |
| support | [Predecessor evidence](../audits/reviews/Yin_R_G0488_v1.md#salem-endpoint-contact-whole-finding) | Actual whole v1 finding and accepted upstream interfaces only; no automatic transfer to v2 or self-review claim. |
| support | [Degree/source evidence](../audits/reviews/Yin_R_G0798_v1.md#two-node-whole-independent-finding) | Existing Section5 review of C134 equation18, retained Smy08 equation11, conversion to total measure and unchanged source-proof limits. |
| review | [Whole two-point finding](../audits/reviews/Yin_R_G0490_v1.md#salem-two-point-tail-whole-finding) | Entire actual Parts A--D/PT1--PT21, both dependencies and three supports, all original signs and scalars, every tail factor, full u-domain and threshold endpoints, precise large/small-degree old coverage and unchanged source/contributor limits; no proof correction or reviewer contribution. |

## Historical assessments

<a id="decision-initial"></a>

### Historical assessment initial

| Field | Value |
| --- | --- |
| date | 2026-10-20T16:52 |
| status | proof draft |
| review-status | under review |
| reason | Retain the substantive continuation of the adopted endpoint inquiry: exact original two-point products with M^(-6), all-M finite tail exclusion, the sharper M=1 corollary, and complete prior Dobrowolski coverage of bounded-tail classes. Preserve v1 unchanged and require a new noncontributor whole review; no new qualitative gap domain or unrestricted solution is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Parts A--D, original genuine Salem domain and actual f-only identity, inherited v1 theorem, all-M finite exclusion, sharper M=1 tail necessity and separately identified prior qualitative coverage. |
| argument | [Complete revised argument](#argument) | All PT1--PT21, actual embedding/sign identities, complete scalar and tail inequalities, empty-tail and all-u boundaries, degree-source adaptation and limitations. |
| dependency | [Unchanged adopted endpoint theorem](Yin_C_G0201_v1.md#statement) | Actual trace/quotient domain, complete predecessor theorem and M=1 strict contact; whole v1 argument and R488 remain at their fixed scopes. |
| dependency | [Accepted original-degree benchmark](Yin_C_G0134_v1.md#two-node-degree-and-inverse-measure-scales) | Only equation18's total m>=1/[2400(log d)^3] for d>=exp(exp1), reused in the separate prior-coverage proof. |
| support | [Earlier integer endpoint floor](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Attribution and scope for M=x product t_j and x>4^(-(r-1)); rederived for bounded-degree escape without new uniform income. |
| support | [Predecessor independent evidence](../audits/reviews/Yin_R_G0488_v1.md#salem-endpoint-contact-whole-finding) | Actual whole v1 finding and accepted upstream interfaces only; no automatic transfer to v2 or self-review claim. |
| support | [Degree/source independent evidence](../audits/reviews/Yin_R_G0798_v1.md#two-node-whole-independent-finding) | Existing Section5 review of C134 equation18, retained Smy08 equation11, conversion to total measure and unchanged source-proof limits. |
