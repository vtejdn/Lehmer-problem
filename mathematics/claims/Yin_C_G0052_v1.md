---
author: Yin
---
# Exact no-circle half-profile selection and its condition-ratio cost

Date: 2026-10-12T09:53.
Human author Yin.
Root authored the original proof and this fixed extraction; root cannot independently review either.
The ENTIRE original D8 mathematical proof, original questions/reuse/contribution,17:28 freeze and17:34 bounded source-screen account are preserved below.
Initial status remains proof draft / under review.
No old interrupted review message is treated as an actual fixed review finding.

## Statement

Let P be an ACTUAL monic irreducible self-reciprocal nontorsion integer-unit minimal polynomial of original even degree d=2s>=2, alpha a root, O0=Z[alpha], sigma(alpha)=alpha^-1 and total m=m(P)>0.
An actual half-profile means a finite family of NONZERO actual O0 integers u_j, positive normalized RATIONAL weights lambda_j, sum lambda_j u_j sigma(u_j)=1/2, with their unique ordinary INTEGER representatives of degree<d.
Let c_infty(P) be the infimum of max_circle sum lambda_j f_jf_j* over the FULL such finite class, without assuming attainment.

**A. Exact availability equivalence and actual finite selection.**
A half-profile whose circle symbol G satisfies G(z)>1/2 at EVERY unit-circle point exists if and only if P has NO unit-circle root.
In that case choose epsilon in{+1,-1} so that

    H=epsilon t^-s P>0 on the circle,
    h_-=min_circleH>0, h_+=max_circleH, R=h_+/h_->1.

H has INTEGER real self-star coefficients, positive integer H_0 and ACTUAL radius s.
For every rational0<a<h_- and rational b>=h_+, and every rational K>0 with K a>1/2, there is an ACTUAL finite half-profile with ALL ordinary integer representatives of degree<=s and a positive rational finite mass W obeying

    1/2+K a<W<=1/2+K H_0,
    G=1/2+K H/(2W-1), x=2G-1.

Specifically apply C34 to K(H-a), clear EACH factor's coefficients individually, add constant1 at raw weight1/2+K a, and call the actual resulting mass W.
Divide its raw weights by2W-1 and add constant1 with positive weight(W-1)/(2W-1).
This is exactly normalized; no positive-Gram-to-integer-mass assumption or supremum attainment is made.
All actual values are nonzero because their ordinary degree<=s<d.
For rational

    A=2K a/(2W-1), B=2K b/(2W-1)

one has0<A<x(z)<=B, A>=a/H_0, B<b/a and A/B=a/b.
Thus this is an actual supplied positive-margin profile at C48's exact scope, with no total-real trace-field restriction or uniform margin guarantee.

**B. Full-class infimum upper bound.**
Each such profile has actual circle maximum<(1+b/a)/2.
Passing only through rational enclosures gives

    c_infty(P)<=(1+R)/2.

The same upper bound holds for the infimum restricted to degree<=s representatives.
No optimizer, endpoint profile, denominator bound or fixed norm inventory is asserted.
Circle-root inputs are excluded from this upper selector and its R definition.

**C. Actual-radius finite packet.**
Put C=(1+b/a)/2>1 and D=ceil(sqrt(1+b/a))+2.
C43's rational whole-interval filter, followed by the exact positive Gram and paired repair locally counted at actual radius s, supplies finite rational complementary packets with all values nonzero in O0,

    E'=(1/2+delta)/(1+delta), 0<delta<=1,
    1/2<E'<=3/4,
    T<=3sD=(3d/2)[ceil(sqrt(1+b/a))+2].

Here delta=rho^2 sum_l d_l for an ACTUAL rational rho>0 and fixed finite positive Gram weights; every chosen finite rho is separately admissible.
At actual filter degree1<=e<=D, all labels lie in[-es,2es], so T is the span after ONE common monomial.
For fixed profile/filter/Gram there are finite choices E'->1/2; no limiting packet is asserted.
Applying C48 instead is valid with A,B but gives a generic O(d(b/a)log(2+b/a)) cap, weaker for this selector than the displayed square-root bound.

**D. Full original costs.**
Initially q_initial=1, but actual initial weight denominator and full signed norms N_j may be arbitrarily large.
For each actual completed packet, let q be its ACTUAL coefficient denominator, omega_b its FINAL normalized rational weights, M_w their actual least denominator, m_b=M_w omega_b, F_b=qV_b the integer numerators after the common monomial and D_b=Norm(V_b(alpha)) the complete SIGNED original norms.
Then

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^(m_b)=q^(dM_w) product_b D_b^(m_b),
    sum_b omega_b ||F_b||_2^2=q^2E',
    Lambda_final=Lambda_initial/(1+delta)>=0,
    Lambda_initial=(1/d)sum_j lambda_j log|N_j|,
    Lambda_final-(1/2)log E'<=(T/d)m(P).

Every original root, actual copy, content, initial versus FINAL weight and signed norm remains.
The monomial has full norm1.
No extra uncancelled log q loss, free denominator or algorithmic bound is claimed.

**E. Exact necessary ratio price and conditional subclass gate.**
For every actual no-circle input above,

    m(P)>=log2/[3(sqrt(1+R)+3)],
    R>=max{1,(max{0,log2/(3m(P))-3})^2-1}.

Along ANY HYPOTHETICAL such sequence m(P)->0, liminf m(P)^2R(P)>=(log2)^2/9.
This follows by applying the full-root inequality to the ACTUALLY constructed packets with the local s-radius width upper bound and taking continuous scalar limits, not by reversing an arbitrary sufficient width cap.
No such sequence is asserted to exist.

If ADDITIONALLY some m0>0 and0<=eta<(log2)^2/9 obey m(P)^2R(P)<=eta for ALL such actual no-circle inputs with0<m(P)<=m0, then that subclass has the explicit gap

    min{m0,(log2/3-sqrt(eta))/4}>0.

The uniform UPPER premise is UNPROVED and the subclass excludes circle-root inputs.
Neither this conditional statement nor qualitative finite R solves unrestricted G0001.

**F. Exact fixed-input calibration.**
For P_A=t^2-A t+1, every integer A>=3, H=A-t-t^-1 and R=(A+2)/(A-2).
The new bound is c_infty(P_A)<=A/(A-2), strictly weaker than C39's OLD exact attained1+3/[2(A-1)].
The difference is(A+2)/[2(A-2)(A-1)]>0.
Degree2 is fixed and total m is bounded away from0; this is a scope control, not a near-one family.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T09:53 |
| status | open |
| reason | Register the exact no-circle finite integer selection, actual-radius realization and condition-ratio consequences while retaining the entire original account. A previous reviewer message was interrupted before fixed evidence; current separate whole review and later actual extraction review are required before adoption. No uniform upper-ratio premise or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete A--F, actual no-circle subclass, finite rational construction, full costs and explicit conditional guards. |
| argument | [Entire retained argument](#argument) | Complete original D8 Sections1--6/Proposition1/equations1--16,17:28 mathematical freeze and17:34 post-freeze source screen. |
| dependency | [Rational positive Gram](Yin_C_G0034_v1.md#statement) | Strict rational remainder at ACTUAL radius s, followed by individual integer coefficient clearing. |
| dependency | [Integer mass normalization](Yin_C_G0039_v1.md#statement) | Actual W>1 finite normalization only; no positive Gram substitute, endpoint supremum or inherited quadratic novelty. |
| dependency | [Rational Chebyshev filter](Yin_C_G0043_v2.md#statement) | Exact rational jets/positive whole-interval remainder and finite pairing; sharper s-radius support budget proved locally. |
| dependency | [Supplied positive-margin alternative](Yin_C_G0048_v1.md#statement) | Exact A,B hypothesis and local finite general-energy construction; selector availability is new local work. |
| dependency | [Full original-root inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Complete nonzero integer values, all roots, actual final weights/norms and common physical width. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T10:06 |
| status | proved |
| reason | Adopt the actual noncontributor extraction/interface finding and the separately fixed whole-author finding at their exact scopes. Entire proofs, source/contribution/correction history and all finite costs remain. Conditional uniform selection, particular versus universal single-factor preservation and unrestricted Task completion are not inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete A--F, actual no-circle subclass, finite rational construction, full costs and explicit conditional guards. |
| argument | [Entire retained argument](#argument) | Complete original D8 Sections1--6/Proposition1/equations1--16,17:28 mathematical freeze and17:34 post-freeze source screen. |
| dependency | [Rational positive Gram](Yin_C_G0034_v1.md#statement) | Strict rational remainder at ACTUAL radius s, followed by individual integer coefficient clearing. |
| dependency | [Integer mass normalization](Yin_C_G0039_v1.md#statement) | Actual W>1 finite normalization only; no positive Gram substitute, endpoint supremum or inherited quadratic novelty. |
| dependency | [Rational Chebyshev filter](Yin_C_G0043_v2.md#statement) | Exact rational jets/positive whole-interval remainder and finite pairing; sharper s-radius support budget proved locally. |
| dependency | [Supplied positive-margin alternative](Yin_C_G0048_v1.md#statement) | Exact A,B hypothesis and local finite general-energy construction; selector availability is new local work. |
| dependency | [Full original-root inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Complete nonzero integer values, all roots, actual final weights/norms and common physical width. |
| support | [Entire original author review](../audits/reviews/Yin_R_G0258_v1.md#positive-circle-selection-whole-finding) | Whole self-review of original17:28 mathematics plus17:34 source context; no interrupted-message verdict substitutes for this fixed finding. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0259_v1.md#c52-no-circle-actual-extraction-finding) | Actual statement, complete retained proof, preservation and present direct interfaces, separate from original whole scope. |

## Registration and complete preservation

Date: 2026-10-12T09:53.
Root authored both proof and wrapper.
The entire source body below is retained with only repeated author front matter removed, first title demoted, relative Claim links rebased and final whitespace normalized.
Every exact argument, cost, contribution/source boundary and original date remains.
The initial candidate and pending status are historical and do not override the selected decision.
No source is newly adopted by this extraction; the bounded post-freeze screen remains a record of unadopted leads.
Original whole review and actual extraction review are separate obligations.

## Argument

## Positive-circle half-profiles from the signed hyperbolic minimal polynomial

Date: 2026-10-12T09:21.
Human author Yin.
Root AUTHOR inquiry under the unchanged G0001 weekly continuation.
This new working address inherits no prior serial contents.
Root cannot independently review this argument.

## Precise next question and reuse

For an ACTUAL irreducible reciprocal non-torsion integer-unit minimal P of even degree d=2s with NO root on the unit circle, use the strictly positive real Laurent polynomial H=epsilon t^(-s)P(t), epsilon in{+1,-1}.
Can its exact rational Gram and actual integer-square mass yield a finite normalized rational half-profile with a strictly positive attained margin, at a cost controlled by R=max_circleH/min_circleH?
This would discharge C48's supplied-profile availability on this no-circle domain only, while retaining a potentially unbounded condition ratio.
It does not apply to Salem/circle-root inputs and does not assume a near-one family.

Bounded local reuse screen read the actual adopted [C34](Yin_C_G0034_v1.md#statement) rational positive Gram, [C39](Yin_C_G0039_v1.md#statement) integer mass and exact W>=1 normalization, [C43v2](Yin_C_G0043_v2.md#statement) square-root construction and inverse-square profile price, [C48](Yin_C_G0048_v1.md#statement) supplied positive-margin filter, and [C49](Yin_C_G0049_v1.md#statement) circle-root restriction.
A bounded current-Claim search for no-circle/positive signed polynomial mechanisms found no retained version of this exact construction; no exhaustive novelty claim follows.
The local argument below will use these actually accepted interfaces, elementary compactness and exact coefficient arithmetic.
No new external theorem, source acquisition or native mathematical computation is needed.

## Candidate and author boundary

Take rationals0<a<minH and b>=maxH.
Start with raw Laurent G=1/2+K H and a rational K>0 with K a>1/2.
Subtract gamma=1/2+K a>1 and apply C34 to K(H-a); clear each rational factor denominator individually to get integer atoms of degree at most s<d.
Add constant1 with weight gamma.
Its actual finite total mass W>gamma>1 should permit precisely C39's transformation: divide raw weights by2W-1 and add another constant1 of weight(W-1)/(2W-1).
The resulting normalized profile has field energy1/2 and circle symbol1/2+K H/(2W-1).
Since W>1/2+K a and W<=1/2+K H_0, the actual x=2G_new-1 should satisfy H/H_0<=x<H/a and hence rational supplied lower/upper margins with ratio a/b.
All original integer residues are nonzero by their ordinary degree<s+1<=d.
Full norms, initial/final weights and coefficient denominators will be priced separately; positive Gram is not silently equated with normalized integer mass.

Potential conclusion: c_infty(P)<(1+b/a)/2 for every such rational enclosure and thus c_infty(P)<=(1+R)/2 as an INFIMUM, with no endpoint attainment.
C43 then produces finite actual packets of width O(d sqrt(R)) for each rational enclosure; C48 also applies but its generic O(d R log R) cap is weaker for this particular selection.
Compare the actual support radius r=s, not merely d-1.
The main missing uniform quantity is R, not profile existence.
Check a self-reciprocal no-circle polynomial is indeed constant-sign after centering, exact nonzero/integrality, mass normalization, strict versus limiting inequalities and all cost/condition consequences before claiming a theorem.

## Status

Developing AUTHOR proof only.
Independent whole review, fixed registration and actual extraction review are all pending.

No Task completion or general upper-selection theorem is asserted.


<a id="positive-circle-selection-domain"></a>
## 1. Actual no-circle input and the signed minimal polynomial

Let P in Z[t] be the ACTUAL monic irreducible self-reciprocal nontorsion integer-unit minimal polynomial of alpha, of even degree d=2s>=2.
Let O0=Z[alpha], sigma(alpha)=alpha^-1, and use all d original embeddings and total Mahler measure m=m(P)>0.
Suppose P has NO root on the unit circle.
The Laurent polynomial t^-s P(t) is real on that circle, because reciprocal coefficients give conjugate-symmetric Laurent coefficients.
It never vanishes there.
Its continuous value has constant sign on the connected circle.
Choose epsilon in{1,-1} so that

    H(t)=epsilon t^-s P(t)>0 on abs(t)=1.             (1)

This H has INTEGER real self-star coefficients, ACTUAL radius s (both endpoint coefficients are epsilon), H(alpha)=0, and positive integer constant coefficient H_0.
Put

    h_-=min_circle H>0, h_+=max_circle H,
    R=h_+/h_->1.                                     (2)

Strict R>1 follows because H is not constant: its endpoint coefficients are nonzero.
In particular H_0 lies strictly between its minimum and maximum; weak bounds suffice below.
These are actual quantities of the original minimal polynomial, not a polynomial chosen after deleting conjugates or replacing alpha by a power.
Neither a total-real trace-field hypothesis nor a root-separation estimate is assumed.
Nontorsion and Kronecker positivity m>0 are at the Task's already accepted actual-unit scope.

Fix ANY rational enclosures

    0<a<h_-, b>=h_+,

and ANY positive rational K with K a>1/2.
Such finite rational choices exist by strict positivity; no algorithm, bit bound, certificate for locating h_-, or uniform choice is asserted.
The letter K in Sections1--5 is a positive scalar, not the number field.
Set

    G_raw=1/2+K H, gamma=1/2+K a>1.                  (3)

The remainder G_raw-gamma=K(H-a) is strictly positive, real rational self-star and has actual radius s.
Apply precisely the adopted C34 A to it.
This gives s+1 positive rational weights d_j and nonzero rational polynomials g_j of degree<=s, with exact identity

    K(H-a)=sum_j d_j g_j g_j*.

Clear EACH polynomial's coefficient denominator separately: take integers b_j>=1, f_j=b_j g_j in Z[t] and raw weights a_j=d_j/b_j^2>0.
Add f_0=1 with a_0=gamma.
Then

    G_raw=sum_(j=0)^(s+1) a_j f_j f_j*,
    W=sum_j a_j>gamma=1/2+K a>1.                  (4)

Here * is t->t^-1.
The final s+1 factors can be linearly independent as in C34, but that is not needed.
Every f_j is nonzero, degree<=s<d, and therefore f_j(alpha) is a NONZERO actual element of O0.
This conclusion uses minimality/irreducibility at the original degree and holds at every conjugate.
Clearing the factors changes raw weights and does not preserve their old mass.
Formula(4) is a true finite integer-square decomposition, not a PSD relaxation.

Integer coefficient energies give the exact upper mass bound

    W<=sum_j a_j ||f_j||_2^2=(G_raw)_0
      =1/2+K H_0.                                   (5)

Thus every allowed actual construction above has a rational finite W obeying (4)--(5).
No supremum is mistaken for an attained decomposition.
The simpler explicit added-constant proof of (4) is the same constructive mechanism behind C39's lower mass bound, used at a strict rational interior point.

<a id="positive-circle-selection-normalization"></a>
## 2. Exact integer mass normalization and strict attained margins

Use precisely C39 B's W>1 normalization.
Keep all j labels with positive weights a_j/(2W-1), and add an additional constant integer atom1 with weight(W-1)/(2W-1)>0.
The sum of these weights is (W+W-1)/(2W-1)=1.
At alpha the weighted relative norm is

    [G_raw(alpha)+W-1]/(2W-1)
      =(W-1/2)/(2W-1)=1/2.

Thus this is an ACTUAL finite normalized positive rational half-profile, with nonzero integer targets in O0 and their ordinary representatives of degree<=s<d.
Its circle symbol is exactly

    G=(G_raw+W-1)/(2W-1)
      =1/2+K H/(2W-1),
    x=2G-1=2K H/(2W-1).                             (6)

The actual radius of both G and x is s, since K>0 and H has nonzero endpoints.
All points on the circle have G>1/2.
Define positive rational bounds

    A=2K a/(2W-1), B=2K b/(2W-1), kappa=A/B=a/b.

Their exact bounds and costs follow from (4)--(5):

    0<A<x(z)<=B on abs(z)=1,
    A>=a/H_0, B<b/a,
    G_max=1/2+K h_+/(2W-1)<(1+b/a)/2.             (7)

The equality x(z)<=B permits b=h_+ if that actual maximum is rational.
The strict lower A<x and strict upper B<b/a come from a<h_- and W>gamma respectively.
For G_max<(1+b/a)/2 it suffices to use h_+<=b and W>gamma.
No inequality has been reversed by replacing a by a higher endpoint.

**Proposition1 (exact availability equivalence and a finite upper selector).**
Within the actual reciprocal-unit domain, there is a finite actual normalized rational half-profile with G(z)>1/2 at EVERY unit-circle point if and only if P has no unit-circle root.
In the no-circle case one can require ALL ordinary integer representatives to have degree<=d/2 and the exact margins(7).
The forward direction is immediate: at any actual circle root zeta, inversion is conjugation, so the half-profile field identity evaluates to G(zeta)=1/2.
The reverse is (1)--(7).
This equivalence is qualitative with explicit input-dependent enclosures; it is not a uniform margin theorem.

Taking the infimum c_infty(P) over the FULL actual finite half-profile class defined in C43, every rational enclosure above supplies an actual profile with

    c_infty(P)<(1+b/a)/2.

Let rationals a increase to h_- and b decrease to h_+ (using upper rational approximants).
This proves

    c_infty(P)<=(1+R)/2.                            (8)

The passage is for an infimum; it does NOT supply an actual profile at the endpoint, a limit of rational weights as an admissible finite packet, or an optimizer.
It is also an upper bound for the class restricted to degree<=s representatives.
C39's integer-mass obstruction is respected by the explicit W>1 construction; a positive Gram alone would not suffice.

<a id="positive-circle-selection-width"></a>
## 3. Actual-radius square-root packet construction

Take the supplied rational bound C=(1+b/a)/2, so C>1 because b>=h_+>h_->a.
Set

    D=ceil(sqrt(2C))+2=ceil(sqrt(1+b/a))+2.

C43 A supplies a rational polynomial p with p(0)=1,p'(0)=-1/2, actual degree e<=D, and h(X)=[1-(1+X)p(X)^2]/X^2 strictly positive on the WHOLE[-1,2C-1].
Its first derivative forces e>=1.
The actual x in(6) lies in this domain.
Put v_j=p(x)f_j, including the added constant label, and

    H_rep=(1/2)h(x),
    1/2-sum_j lambda_j v_jv_j*=x^2 H_rep.           (9)

All original values v_j(alpha)=f_j(alpha) remain NONZERO actual integers.
Since deg h=2e-1 and x has actual radius s, the actual Laurent radius L of H_rep obeys L<=(2e-1)s.
It is strictly positive on the circle, with an explicit rational margin from C43, so C34 gives a rational positive finite sum H_rep=sum_l d_l g_lg_l*, deg g_l<=L.
This uses the actual radius, not an artificial degree d-1 block.

Choose a finite rational rho>0 with delta=rho^2 sum_l d_l<=1, put Z_l=x g_l and form the paired labels Z_l/rho+1,Z_l/rho-1 with RAW positive weights d_l rho^2/2.
Retain each original v_j at its original raw normalized weight lambda_j.
At alpha each new label is respectively+1 or-1.
Normalize all weights by1+delta.
Directly adding the two squares gives the actual constant covariance

    E'=(1/2+delta)/(1+delta), 1/2<E'<=3/4.           (10)

For fixed filter/Gram and rational rho tending to0, this supplies only finite positive packets with E' approaching1/2 from above.
It does not use a rho0 packet or presume that delta can be assigned any specified rational value.

For completeness, track the WHOLE support union.
The original f_j lie in[0,s], x in[-s,s], p(x) in[-es,es], and hence each v_j in[-es,es+s].
The added paired coordinates lie in[-s,L+s] together with the exponent0 constant.
Since e>=1 and L<=(2e-1)s, ALL labels lie in

    [-es, 2es].

Indeed es+s<=(2e)s and L+s<=2es.
After ONE common monomial t^(es), the actual physical width T is at most3es.
Therefore

    T<=3sD=(3d/2)[ceil(sqrt(1+b/a))+2].             (11)

Possible cancellations or actual degree drop only reduce this upper bound.
This sharper factor d/2 is derived here from the actual s-radius and ordinary degree<=s; it is not silently read into C43's registered worst-case d-1 bound.
Every label retains a positive FINAL weight; its small size does not erase occupied support.

The positive-margin alternative C48 also applies to exactly the rational A,B of(7), giving e<=1+ceil((b/a)log[8(1+B)(1+B/2)^2(b/a)^2]) and the SAME locally counted support T<=3es.
Because B<b/a, this generic cap is O(d(b/a)log(2+b/a)).
For this selector it is asymptotically weaker than(11); it is recorded as actual applicability, not advertised as the best quantitative bound.
C48's fixed-ratio logarithmic benefit requires a different favorable variation of the supplied profile.

<a id="positive-circle-selection-full-costs"></a>
## 4. Complete original arithmetic and exact income

The initial profile has q_initial=1.
Its ACTUAL least common positive weight denominator M_initial is finite but not bounded by d,R,a,b or K here.
Every ordinary f_j has content and a complete SIGNED original-degree norm N_j=Norm(f_j(alpha)) in Z minus{0}.
The added constants have norm1 because d is even.
Put

    Lambda_initial=(1/d)sum_j lambda_j log|N_j|>=0.

No small norm inventory or unit-only property is asserted: clearing rational Gram coefficients can create large integral values and norms.
The initial coefficient mean is generally not1/2, and no lag cancellation is asserted until(9)--(10).

For EACH actual finite completed packet, let q be the ACTUAL common coefficient denominator after the common monomial; let omega_b be its FINAL positive normalized rational weights, M_w their ACTUAL least denominator, m_b=M_w omega_b the actual positive integer copies, F_b=qV_b the integer numerator polynomials, and D_b=Norm(V_b(alpha)) the complete SIGNED original norms.
All these nonzero values are integral.
The original unit monomial has full norm1.
Therefore

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^(m_b)=q^(dM_w) product_b D_b^(m_b),
    sum_b omega_b ||F_b||_2^2=q^2 E',
    Lambda_final=(1/d)sum_b omega_b log|D_b|
                 =Lambda_initial/(1+delta)>=0.     (12)

The direct full-original-root expense from C10, used only for this actually complementary finite family, gives

    Lambda_final-(1/2)log E'<=(T/d)m(P).            (13)

All scalar contents, q, M_w, repeated labels and signed norms are present before taking absolute logarithms; the q cancellation in the normalized surplus creates no extra log q loss and no free denominator bound.
The construction yields finitely many positive labels at each stage, even though denominators/weights can diverge in a limiting argument.
No determinant rescaling by a rational constant is used to fabricate integrality.

<a id="positive-circle-selection-condition-price"></a>
## 5. Explicit condition-ratio price and remaining uniform gate

Fix P and the rational enclosure a,b.
Keep its actually constructed finite profile, filter and Gram fixed, and take only the finite rho choices of Section3 tending to0.
Inequality(13), nonnegative Lambda_final and(11) imply at every step

    (1/2)log(1/E')<=(3D/2)m.

The limit E'->1/2 concerns these real inequalities, not a limiting admissible packet.
It gives

    m>=(log2)/(3D)
     >=(log2)/[3(sqrt(1+b/a)+3)],                 (14)

where D<=sqrt(1+b/a)+3 gives the uniformly safe weak comparison, including integral square roots.
The retained theorem is

    m>=(log2)/[3(sqrt(1+b/a)+3)].

Indeed D<=sqrt(1+b/a)+3 always suffices; no strictness is required.
Let a increase to h_- and b decrease to h_+.
Continuity, without choosing one limiting rational profile, gives the exact actual-input conclusion

    m(P)>=(log2)/[3(sqrt(1+R)+3)],
    R>=max{1,(max{0,log2/(3m(P))-3})^2-1}.         (15)

The weak R>=1 guard is deliberately safe; (2) already gives R>1.
This is a NECESSARY condition cost derived from the same actual input and its constructive upper selector, not a uniform numerical Mahler gap.
Along any HYPOTHETICAL no-circle actual reciprocal sequence with m(P)->0, it implies

    liminf m(P)^2 R(P)>=(log2)^2/9.                (16)

No such sequence is asserted to exist.
The stronger constant than a blind use of C43's d-1 profile bound comes from the explicitly proved radius/degree s=d/2 support budget in(11), not a reversal of a sufficient width bound.
The direction used is: an ACTUAL finite construction gives a width UPPER bound, the universally valid full-root inequality gives a measure LOWER bound, and both are combined for that same constructed packet.

A precise sufficient extra gate on this NO-CIRCLE subclass is the following: suppose some m0>0 and0<=eta<(log2)^2/9 satisfy m(P)^2R(P)<=eta for ALL actual no-circle reciprocal inputs with0<m(P)<=m0.
Put A0=log2/3.
From(15),

    A0<=sqrt(m(P)^2+m(P)^2R(P))+3m(P)
       <=sqrt(m(P)^2+eta)+3m(P)
       <=4m(P)+sqrt(eta).

Hence every such input has m(P)>=(A0-sqrt(eta))/4>0, and the subclass gap min{m0,(A0-sqrt(eta))/4} follows.
A uniform R=o(m^-2) suffices.
This UPPER bound on R is UNPROVED and the statement does not cover circle-root inputs; it is not the unrestricted G0001 result.
Merely observing finite R for every fixed P establishes neither uniformity nor the premise on the whole near-one range.

<a id="positive-circle-selection-control-and-review"></a>
## 6. Exact control, limitations and author self-check

For the ACTUAL fixed quadratic P_A=t^2-A t+1, integer A>=3, choose epsilon=-1.
Then H=A-t-t^-1, H_0=A, h_-=A-2,h_+=A+2, R=(A+2)/(A-2).
The new infimum selector(8) reads

    c_infty(P_A)<=A/(A-2).

The independently adopted C39 gives the sharper EXACT attained value1+3/[2(A-1)].
The new bound is strictly larger: their difference is(A+2)/[2(A-2)(A-1)]>0.
Thus this control verifies scope and avoids claiming an optimizer or rediscovering the old sharp quadratic result.
The family has fixed d=2 and m(P_A)=log[(A+sqrt(A^2-4))/2]>=log[(3+sqrt5)/2]>0; it is not a near-one sequence.
No numerical approximation or native computation was run.

The author checked the whole chain: actual reciprocity/constant sign and original radius; positive rational enclosure and strict remainder; C34 versus C39 normalization; separate polynomial denominator clearing; ordinary degree<s+1<=d and nonzero residues at EVERY conjugate; positive normalized weights and exact half-energy; strict versus nonstrict bounds and infimum passage; actual radius s and whole paired-support union; finite repair parameters and complete full signed norms; correct coefficient versus FINAL-weight denominators; the direct inequality direction; continuous condition-ratio passage; optional near-one quantifiers and positive parameter guards; fixed quadratic comparison and source/contribution history.
Equation(14) deliberately uses the uniformly safe weak ceiling comparison, including integral square roots.

This is a local new composition/selection argument using the actually adopted C34/C39/C43/C48 interfaces at their stated proof-review/source depth.
It is not a fresh proof audit of their original classical inputs.
It adds no external theorem or bibliography entry.
The root developed the substantive reasoning directly in this responsible D and is its author; independent whole proof review and later actual fixed extraction are still required before adoption.
The conceptual result changes supplied-positive-margin availability to an exact no-circle existence equivalence with an explicit condition-ratio price; the difficult uniform UPPER condition remains open.


<a id="positive-circle-selection-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T09:28.
ENTIRE Sections1--6, Proposition1, equations(1)--(16), exact control, source/reuse/contribution and all actual-cost/limitation paragraphs are frozen for separate noncontributor review.
All mathematical reasoning was written and hand checked here.
No native program, solver, unrecorded numerical experiment or source intake occurred.
Root remains contributor and cannot independently review this argument.
Fixed registration and actual extraction review remain pending.


## Post-freeze bounded source screen

2026-10-12T09:34.
A follow-up screen queried Mahler measure with no roots on the unit circle, positive integer trigonometric polynomials, hyperbolic and expansive-polynomial terms.
It inspected primary search extracts and the existing retained [Smy08 source account](../audits/literature/Smy08/readme.md), with a textual keyword check of its retained PDF.
The extracts mainly concerned general Mahler/sparse bounds, link hyperbolicity or polynomials with ALL roots outside the disk; none supplied an applicable new uniform bound for the precise no-circle reciprocal-unit condition ratio in this proof.
These searches are leads only, not a source-wide negative theorem or an assertion of novelty.
No new external theorem, artifact, bibliographic identity or proof premise was adopted.
The complete mathematical Sections1--6 and17:28 freeze above are unchanged.
This dated source-screen account is additional author context for the whole reviewer.
