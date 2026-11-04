---
author: Yin
---
# Actual attained-range scalar filtering with a unit-circle conjugate

Date: 2026-10-12T09:02.
Human author Yin.
Provenance: project deduction using the exact adopted profile, support and accepted derivative interfaces.
Context: [the unrestricted G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
This fixed registration retains the ENTIRE original D2 author proof/history.
Whole-D review and actual registered-statement extraction review remain distinct; the initial assessment below is proof draft / under review.

## Statement

Let P be an ACTUAL monic irreducible self-reciprocal nontorsion integer-unit minimal polynomial of original even degree d>=2, K=Q(alpha), O0=Z[alpha], sigma(alpha)=alpha^-1.
Assume P has AT LEAST ONE actual unit-circle root.
Supply a finite nonempty family of nonzero actual u_j in O0, positive rational weights lambda_j summing to1, and RATIONAL0<E0<1 with sum lambda_j u_j sigma(u_j)=E0.
Let f_j in Z[t] be their unique ordinary representatives of degree<d and let star send t to t^-1.
Put

    G=sum_j lambda_j f_j f_j*, x=G/E0-1,
    C_*=max_(abs z=1)G(z), B=C_*/E0-1,
    r=the ACTUAL self-star radius of G.

Then G is nonconstant, C_*>1 and d<=2r<=2(d-1); in particular B>0.
C_* is the ACTUAL real maximum, not a freely chosen rational upper bound.
No total-real trace-field or general-E0 profile-existence theorem is assumed.

Let p be a real scalar polynomial of ACTUAL degree D with p(0)^2=1 satisfying ONLY the attained-range contraction

    0<=(1+x(z))p(x(z))^2<=1 for EVERY abs z=1.

A candidate packet must retain at least one coordinate v_j=p(x)f_j, unchanged apart from a nonzero scalar or monomial multiplier, with STRICTLY POSITIVE final weight.
Its physical width T is the span of the UNION of the positive-weight labels' coefficient supports after one common monomial normalization.
The necessary degree/support conclusions allow real p; an actual integer-resultant construction uses rational coordinates and its own complete costs.

**A. Positive attained interval and actual degree.**
The actual image of x on the circle contains[0,B].
This does not assert contraction on[-1,0], on all[-1,B], or on a larger interval defined by a supplied upper C.
Put delta=1-1/sqrt2 and kappa=delta/pi.
Then D>=1 and, for EVERY real0<a<=B,

    D>=[1-(1+a)^(-1/2)]/[2arcsin(sqrt(a/B))].

For B>=1 this gives

    D>=delta/[2arcsin(1/sqrt B)]>=kappa sqrt B.

For ALL B>0, including0<B<1,

    D>=max{1,kappa sqrt B}.

Both p(0)=+1 and-1 and the endpoints a=B and B=1 are included.
The derivative estimate uses trig degree D, not2D+1 or an upper degree cap.

**B. Actual retained-coordinate physical width.**
Every packet in the stated architecture satisfies

    T>=2Dr+width(f_j)>=Dd,
    T/d>=max{1,kappa sqrt(C_*/E0-1)}.

If all initial coordinates are retained, the first bound uses max_j width(f_j).
For B>=1 the sharper bound is T/d>=max{1,delta/[2arcsin(1/sqrt B)]}.
Nonzero scalar factors, monomial multipliers, coefficient/weight denominator clearing, arbitrarily small positive weights and cancellation between different covariance labels do not erase this individual retained support.
At each original conjugate, x(alpha_i)=0 and v_j(alpha_i)=+/-u_j remain nonzero.
There is no completion-existence assertion for an arbitrary p satisfying the weak contraction.

**C. Matching half-energy order on the SAME profile.**
When E0=1/2, every such packet obeys

    T/d>=max{1,kappa sqrt(2C_*-1)}
       >=max{1,kappa sqrt C_*}.

For the SAME supplied profile choose rational Cbar with C_*<=Cbar<2C_*.
The adopted C43v2 rational whole-interval construction is also an attained-range filter and retains all initial filtered coordinates with positive final weights.
It constructs an actual finite complementary packet with1/2<E'<=3/4 and

    T<=3(ceil(sqrt(2Cbar))+2)(d-1)<=15d sqrt C_*.

Thus the necessary and achievable physical-width orders are d sqrt C_* up to absolute factors in THIS half-energy/unit-circle/retained-coordinate class.
No optimum, bounded precision/denominators, completion for every admissible p or analogous general-E0 construction is claimed.

**D. Accepted full-signature and genuine-Salem consequences.**
Continue ONLY at E0=1/2 and with h>0 actual original circle roots.
Put k=d-h, m=m(P)>0 and Lambda=(1/d)sum lambda_j log abs(Norm_K(u_j))>=0, using the INITIAL normalized profile weights.
The adopted C46 gives k>0 and k log C_*>=h log2+2d Lambda-2(d-1)m.
Hence

    T/d>=max{1,kappa exp([h log2+2d Lambda-2(d-1)m]/(2k))}.

All d original roots are counted, including both members of each complex pair.
C46's validity when h=0 does not extend the attained-range argument to that case.
For a genuine-Salem input d>=4, h=d-2,k=2, put gamma=kappa/sqrt2=(sqrt2-1)/(2pi).
Then

    T/d>=max{1,gamma 2^(d/4)exp(d Lambda/2-(d-1)m/2)}.

For0<m<=c=log2/4, this implies T/d>=max{1,gamma 2^(d/8)}.
OPTIONAL further use of C46's accepted Dim19-v1 house interface m>=c/d, at its retained statement/applicability depth, gives

    T/d>=max{1,gamma exp((log2)^2/(32m))}.

The signature and degree-exponential bounds do not need that optional house premise.
Each bound concerns actual inputs/profiles/packets in its precise domain; a faster-than-any-fixed-power1/m consequence is only along a HYPOTHETICAL genuine-Salem near-one sequence, whose existence is not asserted.
No new source acceptance, original house-proof audit or later-edition comparison is made.

**E. Complete finite arithmetic and limits.**
For C's actual rational construction, at each finite positive rational rho the paired repair retains original FINAL weights lambda_j/(1+s)>0, where s=rho^2 sum_a d_a>0, and E'=(1/2+s)/(1+s).
No packet at rho=0 is introduced.
Let V_b be all rational Laurent coordinates, ell the one common monomial shift, q the actual coefficient denominator, F_b=q t^ell V_b in Z[t], omega_b the FINAL normalized weights, M_w their actual denominator, m_b=M_w omega_b positive integer copies and N_b=Norm_K(V_b(alpha)) the signed full original degree-d norms.
Then

    Res(P,F_b)=q^d N_b,
    product_b Res(P,F_b)^(m_b)=q^(d M_w)product_b N_b^(m_b),
    sum_b omega_b ||F_b||_2^2=q^2 E',
    (1/d)sum_b omega_b log abs(Res(P,F_b))
        =log q+(1/d)sum_b omega_b log abs(N_b).

The common unit monomial has full norm1.
Contents, actual q, FINAL M_w, changed weights and all signed norms/copies remain; initial Lambda is not the later final-weight norm average.
These costs may grow.
A nonrational real p used in the necessary lemma is not assigned an integer resultant packet.

The result closes the tested attained-range-only scalar escape when an ACTUAL unit-circle root forces the positive interval.
Inputs without such a root, nonscalar filters, deletion/recombination/reduction of every retained coordinate, architectures omitting the contraction, and arbitrary complementary packets remain outside scope.
No dimension-independent upper profile selection, near-one sequence, unrestricted gap or Task completion is obtained.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T09:02 |
| status | open |
| reason | Register the exact attained-range/unit-circle retained-coordinate statement and preserve the ENTIRE original author proof/history. R249's whole finding covers its exact16:40 D2 freeze only. Actual registered-statement, fixed-argument, dependency-interface and preservation inspection remains pending before adoption; no unrestricted gap is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact A--E, all supplied rational general-E0 and actual-maximum hypotheses, circle root, scalar degree and positive retention, half-energy matching/price domains, complete costs and limitations. |
| argument | [Complete retained argument](#argument) | ENTIRE D2 Sections1--9/Lemma1/Theorem2/Corollary3/equations1--22, source/contribution/history/self-check and16:40 freeze, without mathematical change. |
| dependency | [Actual general-profile radius](Yin_C_G0047_v1.md#minimal-polynomial-radius-floor) | Nonconstant actual supplied rational-E0 integral profile,C_*>1 and original d<=2r<=2(d-1); no use of the old whole-interval degree conclusion. |
| dependency | [Exact retained coordinate endpoints](Yin_C_G0047_v1.md#exact-filtered-coordinate-width) | Actual real scalar degree, exact Laurent support and individual positive retention give physical union-width lower bounds. |
| dependency | [Accepted trigonometric derivative](../audits/literature/QZ19/Yin_U001.md#qz19-u001) | Existing arXiv-v1 Theorem1.1 trig-degree-at-most N>=1 sup derivative at recorded statement/selected interpolation scope, used with N=D on the full real circle. |
| dependency | [Matching rational half-energy construction](Yin_C_G0043_v2.md#chebyshev-damping-actual-domain-and-statement) | SAME supplied half-profile and rational Cbar, complete actual construction and sufficient degree/width used only for the matching upper direction. |
| dependency | [Finite positive paired repair](Yin_C_G0043_v2.md#chebyshev-damping-gram-repair-and-width) | Strict rational remainder and positive retained original weights at every finite rho, final energy and all coefficient support. |
| dependency | [Full original rational/integer costs](Yin_C_G0043_v2.md#chebyshev-damping-all-original-costs) | Actual q, FINAL M_w/weights/copies, contents, signed original degree-d norms and norm1 common monomial. |
| dependency | [Adopted full-signature price](Yin_C_G0046_v1.md#full-signature-profile-norm-floor) | SAME initial half-profile, all original h/k roots and INITIAL norm weights; used only with added h>0 in the new scalar argument. |
| dependency | [Optional accepted house price](Yin_C_G0046_v1.md#salem-measure-only-profile-price) | Only genuine-Salem0<m<=log2/4 and retained Dim19-v1 statement/applicability scope; exact exponential constant and hypothetical-sequence boundary. |
| support | [Original whole-D2 finding](../audits/reviews/Yin_R_G0249_v1.md#attained-range-circle-root-whole-finding) | Entire exact16:40 author freeze and its original contributor/source disclosure only; the actual new registered artifact still requires its own extraction/interface finding. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T09:20 |
| status | proved |
| reason | Adopt the separate noncontributor actual registered-statement, complete-preservation and selected-interface finding at its actual SELF relationship, alongside the exact whole-author review. The same reviewer retained the known author-validation context of its earlier same-target whole review. Retain all original proofs, corrections, contribution and source limits, actual costs and historical assessments. The supplied-profile, finite-class or fixed-input scopes do not establish unrestricted Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact A--E, all supplied rational general-E0 and actual-maximum hypotheses, circle root, scalar degree and positive retention, half-energy matching/price domains, complete costs and limitations. |
| argument | [Complete retained argument](#argument) | ENTIRE D2 Sections1--9/Lemma1/Theorem2/Corollary3/equations1--22, source/contribution/history/self-check and16:40 freeze, without mathematical change. |
| dependency | [Actual general-profile radius](Yin_C_G0047_v1.md#minimal-polynomial-radius-floor) | Nonconstant actual supplied rational-E0 integral profile,C_*>1 and original d<=2r<=2(d-1); no use of the old whole-interval degree conclusion. |
| dependency | [Exact retained coordinate endpoints](Yin_C_G0047_v1.md#exact-filtered-coordinate-width) | Actual real scalar degree, exact Laurent support and individual positive retention give physical union-width lower bounds. |
| dependency | [Accepted trigonometric derivative](../audits/literature/QZ19/Yin_U001.md#qz19-u001) | Existing arXiv-v1 Theorem1.1 trig-degree-at-most N>=1 sup derivative at recorded statement/selected interpolation scope, used with N=D on the full real circle. |
| dependency | [Matching rational half-energy construction](Yin_C_G0043_v2.md#chebyshev-damping-actual-domain-and-statement) | SAME supplied half-profile and rational Cbar, complete actual construction and sufficient degree/width used only for the matching upper direction. |
| dependency | [Finite positive paired repair](Yin_C_G0043_v2.md#chebyshev-damping-gram-repair-and-width) | Strict rational remainder and positive retained original weights at every finite rho, final energy and all coefficient support. |
| dependency | [Full original rational/integer costs](Yin_C_G0043_v2.md#chebyshev-damping-all-original-costs) | Actual q, FINAL M_w/weights/copies, contents, signed original degree-d norms and norm1 common monomial. |
| dependency | [Adopted full-signature price](Yin_C_G0046_v1.md#full-signature-profile-norm-floor) | SAME initial half-profile, all original h/k roots and INITIAL norm weights; used only with added h>0 in the new scalar argument. |
| dependency | [Optional accepted house price](Yin_C_G0046_v1.md#salem-measure-only-profile-price) | Only genuine-Salem0<m<=log2/4 and retained Dim19-v1 statement/applicability scope; exact exponential constant and hypothetical-sequence boundary. |
| support | [Original whole-D2 finding](../audits/reviews/Yin_R_G0249_v1.md#attained-range-circle-root-whole-finding) | Entire exact16:40 author freeze and its original contributor/source disclosure only; the actual new registered artifact still requires its own extraction/interface finding. |
| review | [Actual SELF extraction](../audits/reviews/Yin_R_G0254_v1.md#c49-attained-range-extraction-finding) | Actual registered statement, complete retained argument and present selected interfaces, checked separately from the original whole-author freeze. |

## Fixed organization and contribution boundary

2026-10-12T09:02.
Under root's bounded second-batch organization assignment, g0001_routes for Yin authored this registered statement and retained the complete [original D2 freeze](#attained-range-entire-author-freeze).
This extractor contributes the new registration and is not its independent reviewer.
The original root and D2 author supplied the mathematical candidate/proof as their unchanged account discloses.
R249's separate reviewer relationship and antecedent contribution disclosures remain at their original scopes.

The complete original account below has only its repeated front matter removed, first title lowered from level1 to level2 and terminal whitespace normalized.
All equations, anchors, source inputs, proof steps, original pending-status paragraphs and16:40 freeze remain.
Relative links from this claims directory resolve identically, so no locator rebasing is required.
The current assessment above selects the new registration; historical pending statements in the preserved proof do not create a second current selection.
No original D2 or R249 is edited here, and no new mathematical exploration or native computation occurs.

## Argument

The ENTIRE original author account follows, selected as the fixed proof with its exact original history and boundaries.
The original whole finding supplies only its recorded scope until a separate reviewer checks this actual registered extraction.

## Attained-range scalar filtering at an actual unit-circle conjugate

Date: 2026-10-12T08:34.
Human author Yin.
New bounded AUTHOR inquiry under root-coordinated G0001 and the current human continuation instruction.
This is a newly allocated rolling draft, irrespective of any earlier use of its numeric address.
Root supplied the substantive candidate and the assigned author will reconstruct its hypotheses, proof and limits; both are contributors, not independent reviewers.

## Current question and starting scope

Does replacing a whole-scalar-interval contraction by contraction only on the actual circle range evade the square-root profile-cost width obstruction, when the actual minimal polynomial has at least one unit-circle conjugate?
Test the continuous-range reduction, actual circle maximum, general-energy small-range branch, both signs of the scalar value at zero, actual degree and retained-coordinate support.
Apply the accepted full-signature and genuine-Salem profile prices only within their half-energy domains.

Starting interfaces are [C47 actual radius and endpoint support](Yin_C_G0047_v1.md#exact-filtered-coordinate-width), [C47 general actual-profile domain](Yin_C_G0047_v1.md#scalar-width-actual-domain), [C46 full-norm signature floor](Yin_C_G0046_v1.md#full-signature-profile-norm-floor), [C46 optional house consequence](Yin_C_G0046_v1.md#salem-measure-only-profile-price), [C43v2 matching rational construction](Yin_C_G0043_v2.md#chebyshev-damping-actual-domain-and-statement), and [QZ19-U001](../audits/literature/QZ19/Yin_U001.md#qz19-u001) at its already accepted trigonometric derivative statement and inspection scope.

The preflight local C/L/D search found the existing explicit exclusion of attained-range-only filters but no retained result closing this circle-root subcase.
Enough local proof and source inputs are available; no new source acquisition or primary proof audit is planned.
This does not establish novelty.
No theorem is adopted by this draft, and no extension to inputs without a circle root, nonscalar filters, coordinate-replacing constructions or arbitrary packets is assumed.
Initial status at creation: author inquiry begun; the completed author proof and current outcome are recorded below.

<a id="attained-range-reuse-and-source"></a>
## 1. Exact reuse and contribution boundary

The bounded preflight searched current G-series Claims, ledgers and drafts for attained-range, actual-range, whole-interval and Bernstein interfaces.
C43v2 and C47 expressly exclude filters controlled only on the smaller attained range; L394 controls a different radial-displacement quantity.
No retained result in that screen covers the present circle-root subcase.
This search is not an exhaustive novelty finding.

The adopted [C47 actual radius](Yin_C_G0047_v1.md#minimal-polynomial-radius-floor) and [exact coordinate-width argument](Yin_C_G0047_v1.md#exact-filtered-coordinate-width) are the support inputs.
Its whole-interval degree theorem is NOT invoked for the new degree estimate.
[C43v2](Yin_C_G0043_v2.md#chebyshev-damping-actual-domain-and-statement) supplies the existing rational half-energy construction only for the matching upper comparison; [C46](Yin_C_G0046_v1.md#full-signature-profile-norm-floor) supplies the already accepted half-profile prices.
Their adopted statements and precise argument interfaces were read after the first fixed-organization batch closed.

The only analytic source input is [QZ19-U001](../audits/literature/QZ19/Yin_U001.md#qz19-u001), read in full at its recorded scope: arXiv1903.10801v1, Theorem1.1, printed/PDFp.3 and the retained selected Riesz-interpolation reading on pp.4--5.
A complex trigonometric polynomial of degree at most N>=1 satisfies ||R'||_infinity<=N||R||_infinity on the entire real circle.
This established statement is already accepted.
No new proof audit, full-paper reading, QZ19 Section5/Mahler derivative input or full correction-body comparison occurs.
The optional measure-only consequence consumes C46's already accepted house interface, with its existing source-statement boundary, not a newly inspected source theorem.

Root supplied the substantive candidate: a unit-circle conjugate puts zero in the attained scalar range, the positive interval alone forces degree of square-root order by the accepted Bernstein inequality, and C47 then supplies the retained-coordinate width.
This author reconstructs the entire domain, constants, small-B branch, finite arithmetic and accepted-price consequences.
Root and this author are contributors and cannot supply independent review of this derivation.
The intermediate-value property of a continuous real function on the circle, cosine substitution and finite endpoint algebra below are elementary local arguments.
Adequate accepted local inputs suffice; no external search or acquisition is needed.

<a id="attained-range-actual-domain"></a>
## 2. Actual profile and the weaker scalar contract

Let P be an ACTUAL monic irreducible self-reciprocal nontorsion integer-unit minimal polynomial, of original even degree d>=2.
Put K=Q(alpha), O0=Z[alpha] and sigma(alpha)=alpha^(-1).
Supply a finite nonempty family of nonzero actual u_j in O0, positive rational weights lambda_j summing to one, and RATIONAL 0<E0<1 such that

    sum_j lambda_j u_j sigma(u_j)=E0 in K.                 (1)

Let f_j in Z[t] be the unique ordinary representatives of degree<d.
Define star by t->t^(-1), and put

    G(t)=sum_j lambda_j f_j(t)f_j(t)^*,
    x(t)=G(t)/E0-1,
    C_*=max_(|z|=1)G(z),
    B=C_*/E0-1.                                          (2)

Here C_* is the ACTUAL real maximum, not a chosen rational upper bound.
By C47's actual-profile radius lemma, G is nonconstant, C_*>1 and its actual self-star radius r satisfies d<=2r<=2(d-1).
Hence B>0 for every input here.

The NEW hypothesis is that P has at least one actual original root zeta with |zeta|=1.
This includes every genuine-Salem input but not every reciprocal input.
No total-real trace-field hypothesis is imposed, and the original degree and all embeddings remain unchanged.

Consider a real scalar polynomial p with p(0)^2=1 and ACTUAL degree D.
For the intended arithmetic packets p is rational; the necessary degree and support arguments hold already for real p.
Impose ONLY

    0<=(1+x(z))p(x(z))^2<=1 for EVERY |z|=1.              (3)

Thus the contract is imposed on the ACTUAL attained range of x, without requiring it on all[-1,B].
A candidate final packet must retain at least one coordinate

    v_j(t)=p(x(t))f_j(t)                                  (4)

unchanged apart from a nonzero scalar or monomial multiplier, with strictly positive final weight.
Its actual physical width T is the span of the UNION of all positive-weight labels' coefficient supports, after one common monomial normalization.
Other added labels may cancel covariance lags but do not remove retained coefficient support.

No construction or rational completion for every p satisfying(3) is asserted.
Deletion/recombination of every coordinate(4), replacement by residues modulo P, nonscalar filters and arbitrary complementary packets remain outside this architecture.

<a id="unit-circle-root-attained-positive-interval"></a>
## 3. A unit-circle conjugate forces the whole positive interval to be attained

**Lemma 1.**
Under(1)--(2) and the unit-circle-root hypothesis, the image of x on the unit circle contains the entire interval[0,B].

*Proof.*
The field identity(1), evaluated at any original root of the actual minimal polynomial, gives G(zeta)=E0.
At the unit-circle root this Laurent value equals the circle square symbol: real integer coefficients imply f_j(zeta^(-1))=overline(f_j(zeta)), so

    G(zeta)=sum_j lambda_j |f_j(zeta)|^2=E0.             (5)

The continuous real nonnegative function theta->G(exp(i theta)) on the compact circle attains its minimum C_min and maximum C_*.
Its image is the interval[C_min,C_*]: for any intermediate value one can follow a circle arc between a minimum point and a maximum point and apply continuity.
Equation(5) puts E0 in this interval.
Therefore every value in[E0,C_*], and hence every X in[0,B], is attained.
This proves the lemma.

In particular(3) implies

    |p(X)|<=1/sqrt(1+X)<=1 for EVERY X in[0,B].           (6)

It does NOT establish(3) on[-1,0] or on[-1,B].
The actual lower endpoint is C_min/E0-1, which need not be -1.
This proof supplies a different positive-interval argument rather than silently applying C47's whole-interval theorem.
Nor does any larger supplied upper C make C/E0-1 an attained value: B in this inquiry is always the actual quantity in(2).

<a id="attained-positive-interval-degree-floor"></a>
## 4. Necessary actual degree from the positive interval alone

Put

    delta=1-1/sqrt(2)>0,
    kappa=delta/pi.                                      (7)

**Theorem 2.**
Every scalar p in Section2 has D>=1.
If B>=1, then

    D>=delta/[2arcsin(1/sqrt(B))]>=kappa sqrt(B).         (8)

For ALL B>0, including 0<B<1,

    D>=max{1,kappa sqrt(B)}.                             (9)

More precisely, for every real a with 0<a<=B,

    D>=[1-(1+a)^(-1/2)]/[2arcsin(sqrt(a/B))].            (10)

*Proof.*
If D=0, p is identically+1 or-1, since p(0)^2=1.
At the attained positive value X=B the upper inequality in(3) becomes 1+B<=1, impossible.
Thus D>=1; this also verifies the positive-degree hypothesis required by QZ19.

Define the real trigonometric polynomial

    R(theta)=p(B(1-cos(theta))/2).                        (11)

A polynomial of actual degree D in cos(theta) has trigonometric degree at most D.
For EVERY real theta the argument of p lies in[0,B], so(6) gives ||R||_infinity<=1 on the entire real circle.
The precise accepted QZ19 theorem with N=D therefore yields ||R'||_infinity<=D.
No factor2D+1 from C47's different quadratic-energy substitution is used here.

For any 0<a<=B, set theta_a=2arcsin(sqrt(a/B)), so 0<theta_a<=pi, R(0)=p(0) and R(theta_a)=p(a).
The reverse triangle inequality and(6) give

    |R(0)-R(theta_a)|
        >=|p(0)|-|p(a)|>=1-(1+a)^(-1/2)>0.

On the other hand the integral of R' along[0,theta_a] bounds this difference by theta_a D.
This proves(10) for BOTH p(0)=1 and p(0)=-1.
There is no assumption about p's sign at a or between0 and a.

When B>=1, set a=1 to obtain the first inequality of(8).
The elementary chord estimate arcsin y<=(pi/2)y on[0,1] gives the second.
Combining it with D>=1 proves(9) for B>=1.
If 0<B<1, then kappa sqrt(B)<1, and the separately proved D>=1 gives(9).
At B=1, theta_1=pi and the same argument applies without a singular endpoint.
The integer degree can also be bounded by ceilings of these real bounds, but no limit through a ceiling or degree-cap substitution is used.

<a id="attained-range-physical-width-floor"></a>
## 5. Exact retained support turns the degree floor into physical width

**Corollary 3.**
Every retained-coordinate packet in Section2 satisfies

    T>=2Dr+width(f_j)>=Dd,
    T/d>=max{1,kappa sqrt(C_*/E0-1)}.                     (12)

If all initial coordinates are retained, the first lower bound can use max_j width(f_j).
When B>=1, the sharper necessary bound is

    T/d>=max{1,delta/[2arcsin(1/sqrt(B))]}.              (13)

*Proof.*
Invoke ONLY C47's exact radius and endpoint-support conclusions.
The coefficients of p(x) at exponents+Dr and-Dr are its nonzero leading coefficient times the D-th powers of the corresponding nonzero endpoints of x.
Lower powers cannot cancel these endpoints.
Product width adds for nonzero Laurent polynomials, so width(p(x)f_j)=2Dr+width(f_j).
Positive retention makes the full union span at least this individual width; the actual minimal-polynomial radius floor d<=2r gives T>=Dd.
Now apply Theorem2.

Common denominator clearing, nonzero scalar factors, arbitrary monomial factors and final positive-weight copies do not change an individual retained width.
A very small positive weight still retains support.
Cancellation among different coordinate squares does not delete the coordinate itself.
The statement is therefore about ACTUAL physical width, not merely a sufficient degree or width cap.

At every original conjugate x(alpha_i)=0, so p(0)=+/-1 gives v_j(alpha_i)=+/-u_j.
These values remain nonzero; in the rational p case they are the same actual order integers up to a sign.
This observation supplies no existence theorem for the missing repair coordinates or their positivity.

<a id="half-energy-attained-range-matching-order"></a>
## 6. Matching half-energy order for the enlarged scalar class

Suppose E0=1/2.
Then B=2C_*-1>1, so every packet in the attained-range class obeys

    T/d>=max{1,kappa sqrt(2C_*-1)}
       >=max{1,kappa sqrt(C_*)}.                         (14)

The last step uses C_*>1.
This lower bound needs an actual unit-circle root but does not need the whole interval[-1,B].

For the SAME supplied profile, choose a RATIONAL Cbar with C_*<=Cbar<2C_*.
Such a rational exists; no algorithmic precision or denominator bound is asserted.
C43v2's adopted rational construction, applied with Cbar, controls the larger whole interval[-1,2Cbar-1].
It therefore also satisfies the current actual-range contract and retains ALL the original filtered coordinates with positive final weights.
The resulting finite actual complementary packet has

    T<=3(ceil(sqrt(2Cbar))+2)(d-1)
      <=15d sqrt(C_*).                                   (15)

Indeed ceil(sqrt(2Cbar))+2<=sqrt(2Cbar)+3<2sqrt(C_*)+3<=5sqrt(C_*).
The coarser last constant is for convenience, not an exact optimum.
Its construction has final constant covariance1/2<E'<=3/4 and all the original rational and integer costs described in Section8.

Thus for each fixed half-profile with an actual unit-circle conjugate, the necessary and achievable physical-width orders are d sqrt(C_*) up to absolute factors even in the ENLARGED class that only tests the attained scalar range.
The existence half uses the known C43 construction; it does not assert that every admissible p admits a completion.
It gives no optimizer for p, C_*, the profile family or the packet width.
No analogous general-E0 completion theorem is claimed.

This resolves the tested escape at this scope: merely removing the negative unused part of the scalar interval cannot beat square-root order when a unit-circle conjugate forces the positive interval[0,B] to remain.
Constants differ from C47's stronger whole-interval estimate, and no stronger constant is claimed here.

<a id="attained-range-signature-and-salem-price"></a>
## 7. Accepted signature and genuine-Salem width consequences

Continue at E0=1/2 and with at least one actual unit-circle root.
Let h count ALL original roots on the unit circle, k=d-h, m=m(P)>0 and

    Lambda=(1/d)sum_j lambda_j log|Norm_K(u_j)|>=0,        (16)

using the INITIAL normalized profile weights.
Adopted C46 supplies k>0 and

    k log C_*>=h log2+2d Lambda-2(d-1)m.                 (17)

All original roots, including both members of every complex pair, occur in these counts.
C46 is valid at wider signatures, but the present scalar-degree argument still needs h>0; it does not automatically extend to h=0 merely because(17) does.

Combining(17) with the monotone square root in(14) proves the finite actual bound

    T/d>=max{1,kappa
         exp([h log2+2d Lambda-2(d-1)m]/(2k))}.           (18)

This is an unconditional project deduction from the already adopted exact C46 input on the present half-energy/unit-circle domain.
It is not obtained by reversing C43's sufficient width upper bound; it uses the separate actual-support lower proof of Sections3--5.

For a genuine-Salem input of original degree d>=4, h=d-2 and k=2.
Put

    gamma=kappa/sqrt(2)=(sqrt(2)-1)/(2pi)>0.

Then(18) gives

    T/d>=max{1,gamma 2^(d/4)
                  exp(d Lambda/2-(d-1)m/2)}.             (19)

For 0<m<=c=log2/4, dropping Lambda>=0 and using

    d log2/4-(d-1)m/2>=d log2/8

gives

    T/d>=max{1,gamma 2^(d/8)}.                            (20)

These bounds use only C46's full-signature norm theorem and the present scalar argument.
For the OPTIONAL measure-only form, additionally use C46's exact accepted-house consequence on genuine-Salem0<m<=c.
Every actual profile has C_*>=c_infty(P), so that accepted infimum bound gives:

    C_*>=(1/2)exp((log2)^2/(16m)).

Its accepted source is the retained Dim19 v1 Theorem1 house statement through the recorded Smy08-U001 interface, at statement/applicability depth; no new source-proof review or later-edition claim is made.
Substitution into(14) gives

    T/d>=max{1,gamma exp((log2)^2/(32m))}.                 (21)

Equivalently(20) and the same accepted m>=c/d give this estimate.
Omitting the optional house input omits(21);(18)--(20) do not need it.

Each inequality applies to EACH actual input/profile and retained-coordinate attained-range packet in its stated domain.
Along any HYPOTHETICAL genuine-Salem sequence with m tending to zero, this class's necessary T/d then exceeds every fixed power of1/m.
No such sequence is asserted to exist.
These statements neither prove a gap nor construct a counterexample, nor rule out arbitrary complementary packets, different coordinate architectures or the complete G0001 objective.

<a id="attained-range-arithmetic-and-boundaries"></a>
## 8. Finite arithmetic, source limits and what remains open

The lower proof never selects a coefficient approximation, Gram factorization, repair parameter or a completed packet.
For the matching C43 existence comparison, use its ACTUAL rational p with p(0)=1, strictly positive rational remainder and complete paired repair.
At every finite rational rho>0 that repair retains original weights lambda_j/(1+s)>0, where s=rho^2 sum_a d_a>0, and has E'=(1/2+s)/(1+s).
Taking rho toward0 never supplies a packet at rho0 or removes any retained support.
General rational E0 and an arbitrary p satisfying(3) do not automatically supply the strictly positive remainder needed for that construction.

For that actual C43 packet, let V_b be all its rational Laurent coordinates, ell its ONE common monomial shift, q the actual common coefficient denominator, F_b=q t^ell V_b in Z[t], omega_b the FINAL normalized weights, M_w their actual common denominator and m_b=M_w omega_b positive integer copies.
Retain the signed full original degree-d norms N_b=Norm_K(V_b(alpha)).
The existing exact accounting is

    Res(P,F_b)=q^d N_b,
    product_b Res(P,F_b)^(m_b)=q^(d M_w) product_b N_b^(m_b),
    sum_b omega_b ||F_b||_2^2=q^2 E',
    (1/d)sum_b omega_b log|Res(P,F_b)|
         =log q+(1/d)sum_b omega_b log|N_b|.              (22)

The common monomial has full norm1, and actual contents/copies are retained.
The initial Lambda in(16) is NOT the later final-weight norm average in(22).
All final weights and actual q/M_w/contents can grow; neither the support lower bound nor rational choice of Cbar makes these costs free or proves a bit-complexity bound.
A real nonrational p in the necessary scalar lemma is not inserted into an integer resultant construction.

The tempting implication that attained-range control automatically gives C47's whole[-1,B] control is NOT proved and is not used.
What succeeds is a narrower new deduction: at an actual unit-circle conjugate, the attained range contains[0,B], and that positive interval already forces the same square-root order.
The new result therefore closes that particular proposed scalar escape for this domain while preserving C47's historical theorem and its exact original bounds.

The following remain outside this finding: reciprocal inputs without an actual unit-circle root; filters outside the scalar polynomial class; removal/recombination/reduction of every retained coordinate; architectures that do not impose the contraction(3); arbitrary exact complementary packets; dimension-independent upper profile selection; and the unrestricted positive-gap or zero-gap conclusion.
No native mathematical computation, solver, numerical approximation, new J, external source acquisition or Claim adoption was performed by this author inquiry.

<a id="attained-range-author-selfcheck"></a>
## 9. Author self-check and present outcome

The complete author check reconstructed every hypothesis and implication in Sections2--8.
In particular it checked actual minimality and irreducibility; original degree and nonzero integer representatives; the rational field identity at an original circle root; the real continuous connected image and ACTUAL attained maximum; C_*>1 and B>0; that only[0,B], not all[-1,B], is inferred; both p(0) signs; D0 exclusion before applying QZ19; the trigonometric degree D rather than2D+1; the full real-theta sup norm; endpoints a=B and B=1; the separate small-B branch; the arcsine constant and exact derivative-integral direction; actual support radius and noncancellable endpoints; real necessary filters versus rational actual packets; strictly positive finite retained weights; and the absence of a completion theorem for every admissible scalar.

The matching comparison was checked using a rational Cbar in[C_*,2C_*), all C43 half-energy hypotheses, the ceiling inequality and constant15, and actual retention under every finite paired repair.
All-signature composition was restricted to h>0, with k>0 supplied by C46; initial norm weights and all original root counts were retained.
The genuine-Salem substitutions, gamma=kappa/sqrt(2), small-measure constant c=log2/4, optional house domain, infimum-to-actual-profile direction and exponent(log2)^2/(32m) were checked separately.
No hypothetical sequence existence or gap conclusion is inferred.

The author found no unresolved mathematical step in this scoped argument.
The result strengthens the tested domain from whole-interval scalar control to actual-attained-range scalar control ONLY when the actual input has a unit-circle conjugate.
It remains an author-complete proof with self-check awaiting a separately organized whole noncontributor review.
Root and this author both contributed and neither can provide that independent review of this derivation.
No Claim has been registered or adopted from this draft.

<a id="attained-range-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T08:40.
Freeze the ENTIRE Sections1--9, Lemma1, Theorem2, Corollary3, equations(1)--(22), matching construction comparison, accepted signature/Salem consequences, complete arithmetic and all source/contribution/noncompletion boundaries after author self-check.
The bounded material check passed with checked1 before this self-check/freeze paragraph and is repeated for the final saved text.
That is structural evidence, not a proof verdict.
Request separate whole noncontributor review before fixed organization or adoption.
