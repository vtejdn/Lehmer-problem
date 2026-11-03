---
author: Yin
---
# Three-prime mixed defects: a universal nonvanishing certificate with original costs

Human author Yin.
Root and g_bridge_audit are mathematical contributors.
Root supplied the substantive 2,3,5 compatibility contradiction and the proposed universal nonvanishing conclusion; g_bridge_audit is checking its exact old formula, deriving integral identities and paying the original polynomial/norm/coefficient interfaces.
Neither contributor may provide independent whole review.
No new native program is needed for the direct algebra below.

## Question and bounded reuse

For an ACTUAL nontorsion integer unit alpha with monic irreducible minimal polynomial P of original degree d, can three fixed-prime mixed defects guarantee at least one nonzero original-field algebraic integer, without the unresolved single-pair nonvanishing problem?
Retain all original conjugates, divisibility constants, polynomial degrees and coefficient expenses.
Reciprocity is not assumed.
A nonzero conclusion is not a cheap Archimedean bound or a G0001 gap.

The exact accepted antecedent is [C146v1's free-ring mixed-prime formula](Yin_C_G0146_v1.md#different-prime-defect-calculation), with [BS09-U001v2](../audits/literature/BS09/Yin_U001.md#bs09-u001) supplying classical attribution, not a quotient-ring descent or an analytic estimate.
The actual base quotients are nonzero and integral by that interface and its [C237 base-prime input](Yin_C_G0237_v1.md#base-prime-power-extra-valuation).
[C148](Yin_C_G0148_v1.md#statement), independently reproduced in [J96](../computations/programs/Yin_J_G0096/readme.md#independent-native-result), classifies only the single 2/3 pair in degrees2/4 and leaves higher-degree single-pair nonvanishing open.
The present disjunction does not settle that single-pair problem.
The old joint linear-minor/projection obstruction remains C146v1 Section1, rather than being silently bypassed by choosing new notation.

A bounded exact-string G claims/ledger/drafts search for three-prime defect, u_5, H25, H35 and5a^15 returned no retained same statement; the existing general coefficient formula is sufficient for the direct calculation here, so no new external theorem or field-wide novelty claim is needed.
An initial PowerShell brace/glob query failed before searching and was replaced by the actual directory/glob search; that failed query supplies no evidence.

<a id="three-prime-nonvanishing"></a>
## 1. Exact compatibility contradiction in the actual original field

Let a=P(alpha^2)/2, b=P(alpha^3)/3, c=P(alpha^5)/5.
These are nonzero elements of the ACTUAL monogenic order Z[alpha].
For delta_p f=(f(t^p)-f(t)^p)/p on Z[t], the old formula gives

    E=delta_2 delta_3 P(alpha)-delta_3 delta_2 P(alpha)=b^2-a^3,
    F=delta_2 delta_5 P(alpha)-delta_5 delta_2 P(alpha)=2c^2-3a^5,
    D=delta_3 delta_5 P(alpha)-delta_5 delta_3 P(alpha)=8c^3-16b^5.
                                                               (1)

The coefficients are respectively(-1,1),(-3,2),(-16,8) from the old formula; no new p-derivation on Z[alpha] is assumed.
Put G=D/8=c^3-2b^5, which is also integral by its displayed expression, not by division of an arbitrary integral element.

For clarity about the nonreciprocal domain, integrality uses P(t^p)=P(t)^p modulo p, followed by P(alpha)=0.
Nonvanishing is the [C231 retained cross-exponent input](Yin_C_G0231_v1.md#mixed-power-resultant-identities): if alpha^p were a conjugate of alpha, an automorphism tau in the normal closure sending alpha to alpha^p would have finite order n, and alpha=tau^n(alpha)=alpha^(p^n) would force torsion.
No normal-closure norm or degree enters this argument.
Thus the actual base hypotheses for a,b,c need neither reciprocity nor a Galois original field.

If E=F=G=0, then b^2=a^3,2c^2=3a^5,c^3=2b^5.
Cubing the second equation gives8c^6=27a^15.
Squaring the third and using the first gives8c^6=32b^10=32a^15.
Hence5a^15=0, impossible in characteristic zero because a is nonzero.
Thus at least one of E,F,G (equivalently E,F,D) is nonzero.
This holds in the original field, not as a selection of different pairs at different embeddings.
Every embedding sends any selected nonzero element to a nonzero element.

<a id="statement"></a>
For EVERY actual nontorsion integer unit alpha with original monic irreducible P and degree d, at least one of the three explicitly integral defects E,F,G in(1) is nonzero.
Equivalently, at least one of the integer polynomials H23,H25,H35 in(4) is not divisible by P.
Their degrees are respectively6d,10d,15d.
The selected defect is simultaneously nonzero at ALL original conjugates.
The exact universal integral identity(3), signed norm identities/floors(5), no-choice full-norm integer(6), and weighted pointwise/product bounds(8),(10) hold with their stated constants.
These conclusions require no reciprocity, total reality, Galois original field, unramified prime or powered degree-preservation assumption.
They do not assert that a prescribed one of the three defects is always nonzero, or that their coefficient/Archimedean expense is small.

<a id="argument"></a>
The full argument is Section1 and Sections2--5 below.
The mathematical inputs are the old integral nonzero base quotients and exact mixed-prime formula linked above.
All new identities and estimates below are proved by direct algebra, without a native computation or an uninspected source theorem.

<a id="integral-three-defect-identity"></a>
## 2. An explicit integral ideal certificate

Define the actual integral elements

    S=b^8+a^3b^6+a^6b^4+a^9b^2+a^12,
    T=4c^4+6a^5c^2+9a^10,
    U=c^3+2b^5.                                      (2)

Then the following is a polynomial identity in Z[a,b,c], and hence an identity in the ORIGINAL order:

    5a^15 = F*T - 8G*U - 32E*S
           = F*T - D*U - 32E*S.                       (3)

Indeed F*T=(2c^2)^3-(3a^5)^3=8c^6-27a^15;8G*U=8(c^6-4b^10); and E*S=b^10-a^15.
Subtracting gives exactly5a^15.
All coefficients, powers and signs in(3) are therefore verified without elimination or a CAS.
Since a!=0 and the original field has characteristic zero, (3) also supplies the disjunctive nonvanishing proof directly.

The left side of(3) is NOT claimed a unit.
The base quotient a need not be a unit, and5 is not invertible in the original integer order.
In the generic Laurent polynomial ring Z[a^(+-1),b^(+-1),c^(+-1)], no integral combination of E,F,G can equal1: reducing modulo5 and evaluating at(a,b,c)=(1,1,3) makes all three zero.
This is a formal algebraic specialization, NOT a constructed original polynomial input or near-one counterexample.
It explains why dividing(3) by5a^15 in the FIELD does not yield a denominator-free unit certificate in the original order.
Actual additional relations for a particular P might alter that ideal question; none are asserted here.

<a id="original-polynomials-and-norms"></a>
## 3. Displayed integer numerators, exact original norms and no choice of embeddings

Write Pj(t)=P(t^j).
Choose the three explicit integer polynomials

    H23=9P2^3-8P3^2,          H23(alpha)=-72E,
    H25=75P2^5-64P5^2,        H25(alpha)=-800F,
    H35=250P3^5-243P5^3,      H35(alpha)=-30375G.        (4)

The identities follow by a=P2(alpha)/2,b=P3(alpha)/3,c=P5(alpha)/5.
Their guaranteed integral denominators are72=2^3*3^2,800=2^5*5^2 and30375=3^5*5^3.
For the ACTUAL mixed defect D=8G the last identity is also H35(alpha)=-(30375/8)D; integrality with the stated30375 normalization follows from the displayed integral G, not from dividing an arbitrary integral D by8.
The coefficient pairs of the displayed polynomial expressions are coprime; no claim is made that the expanded H has primitive content or that these guaranteed divisibilities are its maximal valuation.

Since P is monic, the leading coefficients of H23,H25,H35 are1,11,7, respectively, so their degrees are EXACTLY6d,10d,15d.
P's constant coefficient is +/-1.
No assertion of monicity or constant1 is made for all three H, and reciprocity is not used.
For irreducible P, each H vanishes at alpha if and only if P divides it; a nonzero value remains nonzero at every original conjugate.

For j in{23,25,35}, let Cj be72,800,30375 and beta_j be E,F,G.
The signed original-field identity is

    Res(P,Hj)=Norm_(K/Q) Hj(alpha)
             =(-1)^d Cj^d Norm_(K/Q) beta_j.           (5)

Here K=Q(alpha), of ORIGINAL degree d.
Since beta_j lies in Z[alpha], its norm is an integer; if beta_j!=0 then it is a nonzero integer.
Therefore at least ONE j has |Res(P,Hj)|>=Cj^d.
This assertion uses one common choice j for all d conjugates, not d independent local choices, and it retains any repetitions among values of beta_j by taking the full K norm.
The argument does not replace K by the possibly smaller field Q(beta_j), nor assume the degree of alpha^p equals d.

There is also a choice-free integer quantity involving only the three FULL norms:

    N0=Norm_K(E)^2+Norm_K(F)^2+Norm_K(G)^2
      =(Res(P,H23)/72^d)^2+(Res(P,H25)/800^d)^2
                              +(Res(P,H35)/30375^d)^2
      is an integer >=1.                              (6)

This is positivity of rational integer squares, so it remains valid when K has nonreal embeddings.
In contrast, E^2+F^2+G^2 inside K is not asserted nonzero: squares of complex numbers can cancel.
Formula(6) applies norms BEFORE squares and sums, rather than claiming a false sum-of-squares positivity in K.
There are three norm computations, each with the original d embeddings; no splitting-field norm or extra orbit count occurs.

<a id="weighted-pointwise-defect-bound"></a>
## 4. A quantitative all-root consequence, retaining its weights

The identity also supplies an explicit complex pointwise bound.
For any a,b,c in C, not all zero, set

    M=max{|a|^(1/2),|b|^(1/3),|c|^(1/5)},
    eta=max{|E|/M^6, |F|/M^10, |G|/M^15}.             (7)

Then

    eta >= 27/5075.                                   (8)

To prove it, scale a,b,c by M^2,M^3,M^5 respectively.
The defects scale by M^6,M^10,M^15, while all terms in(3) scale by M^30.
Thus it suffices to treat M=1.
In this normalization, |a|,|b|,|c|<=1 and at least one is1.
The explicit coefficients in(2) give |S|<=5, |T|<=19, |U|<=3.
Therefore(3) implies

    5|a|^15 <= 32*5|E|+19|F|+8*3|G|
              <=203 eta.                             (9)

If eta>1/5 then(8) already holds.
Otherwise, if |a|=1 then |a|^15=1.
If |b|=1, the equation E=b^2-a^3 gives |a|^3>=1-eta>=4/5, so |a|^15>=(4/5)^5>=27/125.
If |c|=1, the equation F=2c^2-3a^5 gives3|a|^5>=2-eta>=9/5, so |a|^15>=(3/5)^3=27/125.
All cases give5|a|^15>=27/25.
Combining with(9) yields eta>=27/(25*203)=27/5075, proving(8), including the equality endpoint eta=1/5.

Apply this independently at all ORIGINAL embeddings sigma_i:K->C.
With Mi and eta_i from(7),

    product_(i=1)^d eta_i >=(27/5075)^d,
    product_(i=1)^d Mi >=|Norm_K(a)|^(1/2)>=1.         (10)

The first product permits different maximizing labels at different embeddings, so it is NOT rewritten as the norm of one selected defect.
The separate field-level disjunction in Section1, not such an exchange of maximum and product, supplies the common nonzero j in(5).
Formula(10) is a quantitative no-common-zero certificate; its small constant and the Mi scaling do not supply an extra positive arithmetic norm floor or cheap analytic expense.

<a id="three-prime-cost-and-scope"></a>
## 5. Full coefficient expense and the precise remaining analytic obligation

Put L=||P||_1 and m=m(P).
The displayed numerators have

    L23=9L^3+8L^2, L25=75L^5+64L^2,
    L35=250L^5+243L^3,
    ||Hj||_1<=Lj.                                     (11)

With q23=6,q25=10,q35=15, multiplying the pointwise bound |Hj(alpha_i)|<=Lj max(1,|alpha_i|)^(qj*d) over every ORIGINAL conjugate gives, for each nonzero beta_j,

    0<=log|Norm_K beta_j|
       <=d[log(Lj/Cj)+qj*m].                          (12)

For zero beta_j the corresponding absolute norm is zero and the exponential upper bound still holds without taking its logarithm.
Hence the exact no-choice quantity(6) satisfies

    1<=N0<=sum_(j=23,25,35) exp(2d[log(Lj/Cj)+qj*m]).   (13)

These are actual paid original-degree inequalities.
They are too weak even at their formal zero-measure endpoint: any nontorsion monic integer-unit P has L>=3.
Indeed L=2 with monic leading coefficient and constant+/-1 leaves only t^d+/-1, whose roots are torsion.
At L=3 the three Lj are respectively315,18801,67311, which all exceed72,800,30375.
Since each Lj is increasing in L>0, all three bracketed coefficient terms log(Lj/Cj) are already positive for every allowed L before qj*m is added.
Thus THESE triangle upper bounds and the guaranteed floors cannot imply a positive lower bound for m.
This is a comparison of the retained bounds, not an actual nontorsion input with m=0 or an obstruction to sharper cancellation estimates.

The more generic coefficient estimate L<=2^d exp(m), obtained by multiplying1+|alpha_i| over the roots, further displays an O(d^2) cost in the unnormalized log norm.
Likewise Mi in(7) obeys

    Mi<=max{(L/2)^(1/2),(L/3)^(1/3),(L/5)^(1/5)}
             *max(1,|alpha_i|)^d.                     (14)

So the normalization in(10) cannot simply be declared bounded from small total m alone.
No cyclic-unit norm theorem has been transferred to a nonmultiplicative defect without its missing analytic interface.

The new result removes the need to settle the individual H23 nonvanishing problem before obtaining SOME nonzero defect in a fixed three-prime family.
It does not show H23 itself never vanishes, does not alter C148/J96's exact scope, and does not evade the old fixed-space linear-minor coefficient costs merely by relabeling them.
It supplies a different, explicitly nonlinear, universally nonzero finite family with degree at most15d.
The remaining useful question is whether global nontorsion together with small TOTAL m can control at least one of these three original norms or their precise coupled expression more sharply than(11)--(14), with every coefficient and denominator paid.

Contribution boundary: root supplied the three equations and the27-versus32 contradiction.
g_bridge_audit checked all coefficients from the actual fixed formula and supplied(2)--(14), the integral-order/field distinction, generic mod5 obstruction, common-embedding and norm-sum interfaces, pointwise constant and full expense analysis.
No new native mathematics was executed.
Classical p-derivation attribution remains the existing BS09 source unit; no theorem or novelty claim beyond this checked local derivation is imported.

<a id="author-freeze"></a>
Author freeze2026-10-15T15:03.
The full statement and Sections1--5/formulas(1)--(14) were self-checked: old mixed-prime signs; exact characteristic-zero contradiction; the three telescoping products in(3); all denominators and leading coefficients; signed full norm and integer-square sum; the weighted normalization and its eta endpoints; and every original-degree/coefficient expense.
Root and this author are proof contributors, so the complete fixed result requires a separate noncontributor's whole review.
This is a complete bounded author result, not an adopted G0001 gap or an independent review.

## Fixed organization

Retain the complete three-prime argument as one new Claim: its statement is a universal finite disjunction, distinct from C148's single-pair question and C146's supplied-Frobenius-class criteria.
Preserve every integral, pointwise and original-norm interface and useful failed expense/unit-ideal inference.
Root supplied the compatibility contradiction and g_bridge_audit supplied the complete extension and costs; both are contributors.
No additional native or source acquisition evidence is needed, and whole noncontributor review remains separate.

## Current assessment
[Selected decision](#decision-current-sylvester-proof-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T15:05 |
| status | open |
| reason | Fix the complete universal three-prime nonvanishing candidate and integral certificate, with all original norms, degree/divisibility constants, weighted pointwise estimates and explicit expense limitations. Whole independent review remains pending; this is not an inexpensive auxiliary theorem or unrestricted G0001 completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete universal finite-family statement](#statement) | Every nontorsion integer unit, no reciprocal/Galois restriction, at least one common original-root nonzero defect; all integral, signed-norm, no-choice and weighted consequences with original costs. |
| argument | [Entire five-section proof](#argument) | All fourteen formulas, compatibility contradiction, integral ideal identity, full original polynomial/norm return, weighted complex bound and exact failure of retained triangle costs. |
| dependency | [Existing mixed-prime formula](Yin_C_G0146_v1.md#different-prime-defect-calculation) | Exact free-polynomial p-derivation identity before evaluation and original integral quotient normalization, without quotient-ring Frobenius descent. |
| dependency | [Integral base quotients](../ledger/Yin_L_G0063_v1.md#base-prime-power-extra-valuation) | P(alpha^p)/p in the actual original order, no prime/ramification or degree-preservation restriction. |
| dependency | [Cross-exponent nonvanishing](../ledger/Yin_L_G0059_v1.md#mixed-power-resultant-identities) | All base quotients nonzero by global nontorsion, without assuming original Galois or reciprocal structure. |
| support | [Earlier single-pair classification](Yin_C_G0148_v1.md#statement) | Exact degree2/4 result and general single-pair question, distinct from the new three-pair disjunction; not a proof premise for the universal statement. |
| support | [Classical mechanism attribution](../audits/literature/BS09/Yin_U001.md#bs09-u001) | Already accepted distinct-prime p-derivation context at its exact source-reading boundary; no new external theorem or original proof audit is imported. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T15:13 |
| status | proved |
| reason | Adopt the complete three-prime nonlinear defect certificate after actual R367 whole review. The universal disjunction, integral identity, signed original norm floors, norm-square sum and weighted complex estimate hold with all original costs. Old base quotients already had universal nonvanishing and degree-linear norm floors; the new content is the specified mixed-defect family. No prescribed single-pair theorem, cheap analytic expense or unrestricted G0001 completion is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete universal finite-family statement](#statement) | Every nontorsion integer unit, no reciprocal/Galois restriction, at least one common original-root nonzero defect; all integral, signed-norm, no-choice and weighted consequences with original costs. |
| argument | [Entire five-section proof](#argument) | All fourteen formulas, compatibility contradiction, integral ideal identity, full original polynomial/norm return, weighted complex bound and exact failure of retained triangle costs. |
| dependency | [Existing mixed-prime formula](Yin_C_G0146_v1.md#different-prime-defect-calculation) | Exact free-polynomial p-derivation identity before evaluation and original integral quotient normalization, without quotient-ring Frobenius descent. |
| dependency | [Integral base quotients](../ledger/Yin_L_G0063_v1.md#base-prime-power-extra-valuation) | P(alpha^p)/p in the actual original order, no prime/ramification or degree-preservation restriction. |
| dependency | [Cross-exponent nonvanishing](../ledger/Yin_L_G0059_v1.md#mixed-power-resultant-identities) | All base quotients nonzero by global nontorsion, without assuming original Galois or reciprocal structure. |
| support | [Earlier single-pair classification](Yin_C_G0148_v1.md#statement) | Exact degree2/4 result and general single-pair question, distinct from the new three-pair disjunction; not a proof premise for the universal statement. |
| support | [Classical mechanism attribution](../audits/literature/BS09/Yin_U001.md#bs09-u001) | Already accepted distinct-prime p-derivation context at its exact source-reading boundary; no new external theorem or original proof audit is imported. |
| review | [Actual whole finding](../audits/reviews/Yin_R_G0367_v1.md#three-prime-defect-whole-independent-finding) | Complete five sections/fourteen formulas, all domain, integral, original-norm and weighted-cost interfaces, exact old-base comparison and source/contribution limits. |


### Decision current-confluent-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:11 |
| status | proved |
| reason | Select C231#mixed-power-resultant-identities as the complete current home of the identical original L59 full-root cross-exponent nonvanishing, multiplicity and exact resultant conventions at the unchanged used scope. The complete retained proof and actual current statement were read, including non-torsion and degree-drop boundaries; this is routine same-content interface adoption. Mathematical status, selected statement/argument/finding and every relation scope remain. Original dated decisions and R bindings retain their actual L59 inputs, and no new independent review or additional arithmetic surplus is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every nontorsion integer unit, no reciprocal/Galois restriction, at least one common original-root nonzero defect; all integral, signed-norm, no-choice and weighted consequences with original costs. |
| argument | [Argument](#argument) | All fourteen formulas, compatibility contradiction, integral ideal identity, full original polynomial/norm return, weighted complex bound and exact failure of retained triangle costs. |
| dependency | [Dependency](Yin_C_G0146_v1.md#different-prime-defect-calculation) | Exact free-polynomial p-derivation identity before evaluation and original integral quotient normalization, without quotient-ring Frobenius descent. |
| dependency | [Dependency](../ledger/Yin_L_G0063_v1.md#base-prime-power-extra-valuation) | P(alpha^p)/p in the actual original order, no prime/ramification or degree-preservation restriction. |
| dependency | [Dependency](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | All base quotients nonzero by global nontorsion, without assuming original Galois or reciprocal structure. |
| support | [Support](Yin_C_G0148_v1.md#statement) | Exact degree2/4 result and general single-pair question, distinct from the new three-pair disjunction; not a proof premise for the universal statement. |
| support | [Support](../audits/literature/BS09/Yin_U001.md#bs09-u001) | Already accepted distinct-prime p-derivation context at its exact source-reading boundary; no new external theorem or original proof audit is imported. |
| review | [Review](../audits/reviews/Yin_R_G0367_v1.md#three-prime-defect-whole-independent-finding) | Complete five sections/fourteen formulas, all domain, integral, original-norm and weighted-cost interfaces, exact old-base comparison and source/contribution limits. |


### Decision current-sylvester-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:29 |
| status | proved |
| reason | Select C237 as the complete current responsible home of the identical retained L63 original-order prime quotient, nonreduced Frobenius and exact integral coefficient-pairing/Sylvester interfaces at the actual anchors below. The full proof, current statement and each used scalar/local/index boundary were read; this is same-content locator adoption. Mathematical status, selected statement/argument/finding and all relation scopes remain unchanged. All prior current C226/C231/Haar homes remain selected where present, while old dated decisions and R bindings keep their actual L63 inputs. No new independent review, low-cost norm or uniform arithmetic gain is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every nontorsion integer unit, no reciprocal/Galois restriction, at least one common original-root nonzero defect; all integral, signed-norm, no-choice and weighted consequences with original costs. |
| argument | [Argument](#argument) | All fourteen formulas, compatibility contradiction, integral ideal identity, full original polynomial/norm return, weighted complex bound and exact failure of retained triangle costs. |
| dependency | [Dependency](Yin_C_G0146_v1.md#different-prime-defect-calculation) | Exact free-polynomial p-derivation identity before evaluation and original integral quotient normalization, without quotient-ring Frobenius descent. |
| dependency | [Dependency](Yin_C_G0237_v1.md#base-prime-power-extra-valuation) | P(alpha^p)/p in the actual original order, no prime/ramification or degree-preservation restriction. |
| dependency | [Dependency](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | All base quotients nonzero by global nontorsion, without assuming original Galois or reciprocal structure. |
| support | [Support](Yin_C_G0148_v1.md#statement) | Exact degree2/4 result and general single-pair question, distinct from the new three-pair disjunction; not a proof premise for the universal statement. |
| support | [Support](../audits/literature/BS09/Yin_U001.md#bs09-u001) | Already accepted distinct-prime p-derivation context at its exact source-reading boundary; no new external theorem or original proof audit is imported. |
| review | [Review](../audits/reviews/Yin_R_G0367_v1.md#three-prime-defect-whole-independent-finding) | Complete five sections/fourteen formulas, all domain, integral, original-norm and weighted-cost interfaces, exact old-base comparison and source/contribution limits. |

