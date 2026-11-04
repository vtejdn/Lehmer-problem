---
author: Yin
---

# Complete integer central-coefficient descent and fully charged Salem critical barriers

This retains the complete necessary mathematical argument from [Complete original central-descent account](../ledger/Yin_L_G0374_v1.md#central-descent-source-and-domain).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let P in Z[t] be the actual monic irreducible minimal polynomial of a genuine Salem number beta>1, of degree2s>=4 and constant term1.
Write P(t)=t^s Q(t+t^-1), where monic integral Q has distinct real roots -2<x_1<...<x_(s-1)<2<x_s=x_0=beta+beta^-1.
All s-1 critical points y_i are simple and strictly interlace these roots.
Define c=-Q(2), a positive integer, and a=min{ -Q(y):Q'(y)=0 and y is a local minimum }, which is positive and attained.
For real u>=0 let Q_u=Q+u and P_u=P+u t^s; integer u alone makes P_u an actual monic integer reciprocal polynomial of the same degree/constant term, with repeated or cyclotomic output factors allowed.
Then Q_u has all roots real, counted with multiplicity, if and only if 0<=u<=a.
Every critical equality at a minimum is exactly a double root; simultaneous critical equalities and all roots remain counted.

If a>=1, every Q_u root is at least -2 for all0<=u<=1, including the possible odd-s endpoint Q(-2)=-1,u1.
For u<c, exactly one trace root x(u)>2 remains, on the last increasing branch, and every other trace root is in[-2,2].
At u=c=1, the cases Q'(2)>0, Q'(2)=0 and Q'(2)<0 give respectively a simple rightmost2 with no root above2, an exactly double rightmost2 with no root above2, and penultimate2 with exactly one root above2.
Thus for the complete original-degree integer neighbor P_1=P+t^s, 1<M(P_1)<M(P) holds exactly in the a>=1 cases c>=2 or c1 with Q'(2)<0; for c1 and Q'(2)>=0 one instead has M(P_1)=1.
Every circle factor and endpoint multiplicity is retained.
In the positive output case the unique noncyclotomic irreducible factor contains both real exterior/contracting roots and may have smaller degree; the other factors are cyclotomic products, possibly repeated.
A measure-one output is not a smaller positive value in the Lehmer infimum.

For0<=u<1 under a>=1, with m(P_u)=log M(P_u), the full original measure satisfies dx/du=-1/Q'(x(u)) and dm(P_u)/du=-1/[sqrt(x(u)^2-4)Q'(x(u))]<0.
All other original pairs stay on the circle, and integration to1 gives the exact measure change, using the finite continuous root/measure limit as an improper integral when x(u)->2.
No uniform size of this decrease is obtained.
If this shape-preserving unit central move gives no smaller positive measure, a<1 or [c1,Q'(2)>=0] is necessary.
For a<1 the failure of the all-real trace shape alone says nothing about the full measure after nonreal traces appear.

The complete critical-value product is product_(Q'(y_i)=0)|Q(y_i)|=|disc Q|/s^s, retaining all s-1 roots and the leading coefficient s of Q'.
For Q(x)=sum_(j=0)^s q_j x^j set A_Q=sum_j|q_j|x_0^j, with x_0=M(P)+M(P)^-1.
Then a>=|disc Q|/[s^s A_Q^(s-2)]>=1/[s^s A_Q^(s-2)], including s2 with exponent0.
This is the full monic integer polynomial discriminant, not an integer floor on one critical value or a field discriminant; all original degree and trace-coefficient costs are paid.

For any fixed monic real polynomial Q of the fixed degree s>=2, if I_Q={u in R: every root of Q+u lies in[-2,2]} is nonempty, it is a closed interval of length at most4 and contains at most5 integer shifts giving measure one.
The accepted MPV author-version capacity theorem is applied only after choosing u_0 in I_Q and scaling p(y)=2^-s[Q(2y)+u_0], with alpha=2^-s(u_0-u).
The all-interval hypothesis is essential, and the result bounds neither measure just outside I_Q nor distance of endpoints from integers across varying Q.
For the exact original Lehmer polynomial P_L=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1, the attributed identity P_L+t^5=Phi_1^2 Phi_2^2 Phi_3^2 Phi_6 and direct Q_L+1=(x^2-4)(x+1)^2(x-1) give a=c=1 and Q_L'(2)=36>0.
It therefore calibrates the measure-one alternative and gives no smaller positive measure.

The complete proof below retains the known perturbation/capacity attribution and exact undated author-PostScript version, original trace scaling and accepted Kronecker product/multiplicity scope.
There is no new perturbation method, source-proof audit or journal-version equivalence claim, numerical scan, finite root or measure program, degree-uniform barrier, global minimum theorem or unrestricted gap.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:35 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Complete original Salem interlacing](Yin_C_G0402_v1.md#salem-interlacing-critical-orders) | Only original genuine Salem trace roots and every simple derivative root/endpoint order; no phase estimate is a premise. |
| dependency | [Exact original reciprocal trace domain](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Actual monic integer trace polynomial and original full degree, with no proper-field or half-normalized measure replacement. |
| dependency | [Exact original Lehmer input](Yin_C_G0243_v1.md#reciprocal-trace-lehmer-control) | Only the complete degree10 polynomial and original trace expression/root domain; no compact enumeration or co-return theorem is needed. |
| dependency | [Exact accepted capacity and perturbation source](../audits/literature/MPV98/Yin_U001.md#mpv98-u001) | Undated prepublication author PostScript converted to19-page PDF, Theorems2.1–2.2 and existing Lehmer identity; only exact statement/applicability/scaling, not equality or original potential-theory proof audit. |
| dependency | [Original full Mahler and Kronecker interface](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Complete multiplicative Mahler measure and measure-one integer products including all factor and endpoint multiplicities; accepted statement, no new proof audit. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:42 |
| status | proved |
| reason | Adopt the actual complete SELF finding after checking the exact original domain, whole retained proof, all endpoint/multiplicity/factor/measure cases and full discriminant/coefficient/capacity expenses. Original source versions, distinct reading occurrences, author and R201 SELF scopes and actual historical times remain separate; no new computation or uniform-gap result is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0402_v1.md#salem-interlacing-critical-orders) | Only original genuine Salem trace roots and every simple derivative root/endpoint order; no phase estimate is a premise. |
| dependency | [Exact accepted input](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Actual monic integer trace polynomial and original full degree, with no proper-field or half-normalized measure replacement. |
| dependency | [Exact accepted input](Yin_C_G0243_v1.md#reciprocal-trace-lehmer-control) | Only the complete degree10 polynomial and original trace expression/root domain; no compact enumeration or co-return theorem is needed. |
| dependency | [Exact accepted input](../audits/literature/MPV98/Yin_U001.md#mpv98-u001) | Undated prepublication author PostScript converted to19-page PDF, Theorems2.1–2.2 and existing Lehmer identity; only exact statement/applicability/scaling, not equality or original potential-theory proof audit. |
| dependency | [Exact accepted input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Complete multiplicative Mahler measure and measure-one integer products including all factor and endpoint multiplicities; accepted statement, no new proof audit. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0616_v1.md#current-central-descent-whole-finding) | Entire exact Statement and complete necessary original mathematical argument, all real/integer, repeated/factor, positive-versus-measure-one, derivative/resultant/capacity/source and nonuniformity boundaries. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="central-descent-source-and-domain"></a>
## 1. Existing perturbation theory and actual Salem domain

The primary search located the directly relevant existing work [MPV98-U001](../audits/literature/MPV98/Yin_U001.md#mpv98-u001).
Its author-version Theorems2.1--2.2 study central coefficient perturbation, real trace shifts and capacity.
Its p.2 already gives the exact cyclotomic perturbation expression for Lehmer's polynomial.
Those mechanisms and that example are reused with attribution; no new perturbation method or historical novelty is claimed here.
The changed local question is a completely scoped integer one-step criterion starting from a genuine Salem input, including whether its full new measure remains positive.

Let P be the monic irreducible minimal polynomial of a genuine Salem number beta>1, with degree2s>=4 and
\[
P(t)=t^s Q(t+t^{-1}).
\]
Q is monic integral of degree s, with distinct real roots
\[
-2<x_1<\cdots<x_{s-1}<2<x_s=x_0=\beta+\beta^{-1}.
\]
Its s-1 critical points y_i are simple, real and strictly interlace these roots, as in [L369](Yin_C_G0402_v1.md#salem-interlacing-critical-orders).
In particular none lies at or below-2, and at most the last lies at or above2.
Define
\[
c=-Q(2)\in\mathbb Z_{\ge1},\qquad
a=\min_{\substack{Q'(y)=0\\y\text{ a local minimum}}}(-Q(y))>0.       \tag{1}
\]
There is at least one local minimum, the rightmost critical point.
Every original local minimum value is negative and every local maximum value positive, since Q has distinct real roots.

For real u>=0 put Q_u=Q+u and P_u=P+u t^s=t^s Q_u(t+t^-1).
For integer u, P_u is an actual monic integer reciprocal polynomial of the SAME degree and constant coefficient1.
Repeated/cyclotomic output factors are allowed; P_u is not assumed irreducible.

<a id="real-trace-shift-criterion"></a>
## 2. Exact all-real criterion and the two endpoints

For every u>=0,
\[
Q_u\text{ has all roots real, with multiplicities}
\quad\Longleftrightarrow\quad 0\le u\le a.                       \tag{2}
\]
For sufficiency, each original local maximum stays positive and each local minimum remains nonpositive.
The intervals cut by the s-1 simple critical points, with the two unbounded end intervals, then supply all s roots by signs and monotonicity.
Equality at a critical minimum gives a double root, counted twice; different critical points remain distinct, and the total count is still s.
For necessity, if Q_u has s real roots, Rolle counting exhausts its unchanged s-1 simple derivative roots between them.
Thus every local minimum must be nonpositive and every local maximum nonnegative.
A minimum whose original magnitude is smaller than u violates this.
This is the elementary constant-shift root-count mechanism also present in MPV98's interval proof; the precise current domain is supplied above.

Assume now a>=1.
For every0<=u<=1, all Q_u roots are at least-2.
Indeed Q(-2) has sign(-1)^s and is a nonzero integer.
For even s it is positive, so adding u leaves a positive value on the decreasing leftmost branch.
For odd s, Q(-2)<=-1, so adding u leaves a nonpositive value on the increasing leftmost branch.
Since every derivative root is greater than-2, in either case the leftmost root is at least-2; the others are larger.
Equality can occur at u=1 and Q(-2)=-1 and is retained.

For u<c, Q_u(2)<0.
Its last negative interval must contain2, so exactly one trace root lies above2 and all others lie in[-2,2].
More explicitly, the derivative has at most one critical point above2; two distinct monotonic branches to the right would place2 on the nonnegative side before the final two roots, contrary to Q_u(2)<0.
The rightmost root x(u)>2 lies on the strictly increasing branch beyond y_(s-1).

At u=c=1, the trace point2 is a root.
There are three exact possibilities:
\[
\begin{array}{c|c}
Q'(2)>0 & 2\text{ is the rightmost root; no root is above2},\\
Q'(2)=0 & 2\text{ is a double rightmost root; no root is above2},\\
Q'(2)<0 & 2\text{ is the penultimate root; one root remains above2}.
\end{array}                                                     \tag{3}
\]
This follows from the sign of the unchanged derivative on the two branches adjacent to its rightmost minimum.
A critical point at2 can only be that last minimum, and it is simple, so the zero of Q_1 there has exactly multiplicity2.
These endpoint cases cannot be replaced by the assertion that Q(2)+1=0 alone forces Mahler measure one.

<a id="integer-central-descent"></a>
## 3. Full Mahler consequence and coefficient derivative

Under a>=1, let P_1=P+t^s.
Every trace root in[-2,2] supplies only unit-circle roots of P_1, including their full multiplicities at the endpoints.
Each trace root above2 supplies a positive inverse pair.
The classification in Section2 therefore gives
\[
\begin{cases}
1<M(P_1)<M(P),&
 c\ge2\ \text{or}\ [c=1,\ Q'(2)<0],\\
M(P_1)=1,& c=1,\ Q'(2)\ge0.
\end{cases}                                                     \tag{4}
\]
In the first case the unique exterior trace root is strictly smaller than x_0: on the original last increasing branch, Q_1(x_0)=1 and its zero occurs earlier.
The map x to(x+sqrt(x^2-4))/2 is strictly increasing for x>2.
Hence the FULL measure, not a selected factor estimate, strictly decreases while remaining positive.

The noncyclotomic factor containing the exterior pair may have smaller degree; no degree preservation is claimed for that factor.
The complete P_1 retains degree2s and integer normalization.
Its other factors have all roots on the circle and hence are cyclotomic by the accepted integer Kronecker theorem.
The measure-one case is a cyclotomic product, potentially with repeated factors; it is not a smaller positive value in the Lehmer infimum.

For0<=u<1 under the same hypothesis, there is exactly one exterior trace root x(u)>2 and it is simple.
Implicit differentiation and the original total logarithmic measure give
\[
\frac{dx}{du}=-\frac1{Q'(x(u))},\qquad
\frac{d\,m(P_u)}{du}
 =-\frac1{\sqrt{x(u)^2-4}\,Q'(x(u))}<0.                       \tag{5}
\]
Every other original pair is on the circle, so no omitted derivative contribution is being suppressed.
Integrating(5) up to1 is valid as an improper integral when the exterior root reaches2, by monotonicity and continuity of the roots and the finite limit m(P_1).
This gives the exact full paid measure change, without a uniform lower bound for its size.

Consequently, if this shape-preserving integer neighbor supplies no smaller POSITIVE measure, then necessarily
\[
a<1\quad\text{or}\quad[c=1,\ Q'(2)\ge0].                     \tag{6}
\]
The first alternative means the all-real trace shape is lost before completing the unit coefficient move.
It does NOT prove that the full Mahler measure of P_1 is larger: nonreal trace pairs must then be evaluated at their full cost separately.
Formula(6) is a necessary local obstruction for this one move, not a global minimum theorem or a proof of a gap.

<a id="critical-value-arithmetic-cost"></a>
## 4. An integer discriminant charges the critical barrier

The complete original critical-value product satisfies
\[
\prod_{Q'(y_i)=0}|Q(y_i)|
 =\frac{|\operatorname{disc}Q|}{s^s}.                        \tag{7}
\]
Indeed the leading coefficient of Q' is s, so its full resultant with the monic degree-s Q is s^s product_i Q(y_i), equal in absolute value to the polynomial discriminant.
There are s-1 simple critical roots; no proper field or selected root replaces this product.

Write Q(x)=sum_(j=0)^s q_j x^j and define the explicit positive coefficient cost
\[
A_Q=\sum_{j=0}^s|q_j|\,x_0^j,\qquad x_0=M(P)+M(P)^{-1}.
\]
Every y_i lies in(-2,x_0), so |Q(y_i)|<=A_Q.
Selecting a minimum that attains a in(1) yields
\[
a\ge
\frac{|\operatorname{disc}Q|}{s^s A_Q^{s-2}}
\ge\frac1{s^s A_Q^{s-2}}.                                    \tag{8}
\]
This includes s=2, with exponent0.
The discriminant is the full monic integer polynomial discriminant.
The bound pays degree and all trace coefficients and gives no degree-uniform positive threshold.
Thus a small critical barrier cannot be replaced by an uncharged assertion of a small algebraic number or by an integer floor on a single critical value.

<a id="capacity-and-lehmer-central-control"></a>
## 5. Capacity boundary and the existing Lehmer example

For any fixed monic real Q, if the set
\[
\mathcal I_Q=\{u\in\mathbb R: Q+u\text{ has all roots in }[-2,2]\}
\]
is nonempty, choose one u_0 in it and apply MPV98-U001 to Q+u_0.
Translation of the source's shift interval and its verified trace scaling show that I_Q is a closed interval of length at most4.
Thus this coefficient line contains at most5 integer values producing M(P_u)=1.
The source theorem requires the all-interval base and is invoked only after u_0 is chosen.
It neither bounds the measure just outside I_Q nor separates its endpoints uniformly from integers across varying Q.

For the original Lehmer polynomial, the known source identity is
\[
P_L+t^5=\Phi_1^2\Phi_2^2\Phi_3^2\Phi_6.
\]
The actual trace factorization is directly
\[
Q_L(x)+1=(x^2-4)(x+1)^2(x-1).                                \tag{9}
\]
This expands to x^5+x^4-5x^3-5x^2+4x+4, as required.
Therefore Q_L(2)=-1 and the u=1 output is a cyclotomic product.
The double trace root at-1 gives Q_L'(-1)=0 and Q_L(-1)=-1, so a<=1.
Equation(2), applied to the displayed all-real shifted roots, gives a>=1, hence a=1 exactly.
Also Q_L'(2)=36>0.
This is precisely the second alternative in(6): an integer move reaches measure one, without producing a smaller positive measure.
It is an existing cyclotomic perturbation example, now used to calibrate the full one-step distinction.

## 6. Outcome and author freeze

The exact integer coefficient move has an all-real critical-value criterion, a complete positive-versus-zero Mahler outcome, an actual derivative formula, and a full discriminant charge on any small critical obstruction.
Known central perturbation/capacity theory and the existing Lehmer factorization are explicitly reused.
The remaining uniform question is not solved: critical barriers, coefficient costs and behavior after the trace roots leave the real interval can vary with degree.
