---
author: Yin
---
# Actual physical-width floors for retained-coordinate scalar profile repair

Date: 2026-10-12T08:19.
Human author Yin.
Provenance: project deduction.
This fixed organization retains the ENTIRE original D11 author account, including its conditional D9 interface, contribution history, source limits and dated freeze.
Separate whole-author review and actual extraction/interface review remain distinct.

## Statement

Let P be an ACTUAL monic irreducible self-reciprocal nontorsion integer-unit minimal polynomial of original even degree d>=2, K=Q(alpha), O0=Z[alpha] and sigma(alpha)=alpha^(-1).
Supply a finite nonempty family of nonzero actual u_j in O0, positive rational lambda_j with sum lambda_j=1, and RATIONAL 0<E0<1 such that sum lambda_j u_j sigma(u_j)=E0 in K.
Write f_j in Z[t] for the unique ordinary representatives of degree<d.
With star replacing t by t^(-1), put G=sum lambda_j f_j f_j*, x=G/E0-1, actual C_*=max_circle G and actual self-star radius r.
A final packet's physical width T is the span of the UNION of its positive-weight labels' coefficient supports, after one common monomial normalization.

**A. Actual radius and exact endpoint support.**
G is nonconstant, C_*>1 and d<=2r<=2(d-1).
For every nonzero real scalar polynomial p of ACTUAL degree D>=0 and every j,

    width(p(x))=2Dr,
    width(p(x)f_j)=2Dr+width(f_j).

Thus any packet retaining at least one such coordinate, unchanged apart from a nonzero scalar or monomial multiplier, with POSITIVE final weight has T>=2Dr+width(f_j)>=Dd.
If all initial coordinates survive, T>=2Dr+max_j width(f_j).
Scalar/weight denominator clearing, arbitrarily small positive weights and cancellations between different covariance labels do not remove this occupied support.
A degree upper cap cannot replace actual D in this lower bound.

**B. Whole-interval scalar requirement implies a physical-width floor.**
Choose any REAL C>=C_* and a rational real polynomial p such that p(0)^2=1 and

    0<=(1+X)p(X)^2<=1 for EVERY X in[-1,C/E0-1].

Then D>=1 and

    2D+1>=1/arcsin(sqrt(E0/C))>=(2/pi)sqrt(C/E0),
    T/d>=max{1,(1/2)(1/arcsin(sqrt(E0/C))-1)}
       >=max{1,sqrt(C/E0)/pi-1/2}.

The SAME filter also obeys these bounds with C replaced by its actual C_*.
The interval may be restricted to that actual-maximum subinterval without rationalizing C_*, passing through a ceiling, or choosing an optimizer.
Both p(0)=1 and p(0)=-1 are covered.
Control only on the ATTAINED range of x on the circle, coordinate replacement/recombination eliminating all retained labels, or reduction modulo P does not meet the whole-interval/retention premises.

**C. Matching order at half energy and every finite repair.**
For E0=1/2 and RATIONAL C>=C_*, adopted C43v2 constructs a member of this SAME class with

    T<=3(ceil(sqrt(2C))+2)(d-1).

Every member has T>=d max{1,sqrt(2C)/pi-1/2}; in particular d sqrt(2C)/(2pi)<=T for every member, while a constructed member has T<=12d sqrt(2C).
Hence the physical order is d sqrt(C) up to absolute factors WITHIN this precise class, without an exact optimum or arbitrary-packet conclusion.

C43's chosen filter retains all v_j=p(x)f_j.
Its strict positive remainder has rational Gram H=sum_a d_a g_a g_a*, d_a>0.
For finite rational rho>0, Z_a=xg_a and K_(a,+/-)=Z_a/rho +/-1 have raw weights d_a rho^2/2 per sign.
With s=rho^2 sum_a d_a>0, original FINAL weights are lambda_j/(1+s)>0 and E'=(1/2+s)/(1+s).
EACH finite repair retains the width floor, even along rho decreasing to0; no rho0 packet is asserted.
Whenever a valid analogous repair exists for general E0, its energy is (E0+s)/(1+s).
Neither existence of completion for every interval-admissible p nor a general-E0 extension of the half-energy construction is claimed.

**D. Full arithmetic remains charged.**
For an actual C43 packet, let V_b be its rational Laurent coordinates, ell its single common monomial shift, q its actual common coefficient denominator, F_b=q t^ell V_b in Z[t], omega_b its FINAL normalized rational weights, M_w their actual denominator, m_b=M_w omega_b positive integer copies, and D_b=Norm_K(V_b(alpha)) with original degree d and signs.
Then

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^(m_b)=q^(d M_w) product_b D_b^(m_b),
    sum_b omega_b ||F_b||_2^2=q^2 E',
    (1/d)sum_b omega_b log|Res(P,F_b)|
        =log q+(1/d)sum_b omega_b log|D_b|.

Actual contents, q, FINAL M_w, original signed norms and every retained copy remain.
The original lambda_j in a profile-price input are not replaced by these later final weights.
The width proof supplies no free denominator, scalar normalization, norm-income, or bit-complexity conclusion.

**E. Exact conditional signature and Salem implications.**
At E0=1/2, let h count ALL original roots on the unit circle, k=d-h>0, m=m(P)>0 and Lambda=(1/d)sum_j lambda_j log|Norm_K(u_j)|>=0 with the INITIAL normalized weights.
IF the fixed [full-signature profile premise](Yin_C_G0046_v1.md#full-signature-profile-norm-floor) holds for this same profile,

    k log C_*>=h log2+2d Lambda-2(d-1)m,

then the retained-coordinate whole-interval packet has

    T/d>=(sqrt(2)/pi)
         exp([h log2+2d Lambda-2(d-1)m]/(2k))-1/2,

together with T/d>=1.
For a genuine-Salem input d>=4, h=d-2 and k=2, this becomes

    T/d>=(1/pi)2^(d/4)exp(d Lambda/2-(d-1)m/2)-1/2.

If additionally 0<m<=log2/4, dropping Lambda gives T/d>=(1/pi)2^(d/8)-1/2.
IF the exact optional [house-based premise](Yin_C_G0046_v1.md#salem-measure-only-profile-price) is also invoked, m>=(log2)/(4d) yields

    T/d>=(1/pi)exp((log2)^2/(32m))-1/2.

These remain explicit implications with those precise inputs.
The original author account's pending-D9 status is historical; this extraction does not silently adopt a pending D9 Claim or enlarge its accepted source inspection.
No hypothetical near-one genuine-Salem sequence is asserted to exist, no lower bound for all complementary packets is proved, and unrestricted G0001 remains unresolved.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T08:19 |
| status | open |
| reason | Organize the exact retained-coordinate whole-interval width statement and preserve the entire original argument and history. Whole-D11 review is available; this actual fixed statement, preservation and dependency interface await separate review. The D9 compositions remain explicit implications, without silently adopting pending support or resolving G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact supplied general-E0 profile, actual radius/degree/support, whole-interval retention, finite arithmetic and conditional signature/Salem conclusions. |
| argument | [Entire retained original argument](#argument) | Complete D11 Sections1--8, equations1--17, proofs, source/contribution boundaries, original self-check and15:06 freeze. |
| dependency | [Actual half-profile convention](Yin_C_G0037_v1.md#statement) | Actual monogenic order and half-profile conventions only; general-E0 statements use a supplied profile, without an existence theorem. |
| dependency | [Matching half-energy construction](Yin_C_G0043_v2.md#chebyshev-damping-actual-domain-and-statement) | Actual rational half-energy filter, strict positive remainder and sufficient degree/physical-width bounds; a cap is not the necessary actual degree. |
| dependency | [Positive finite paired repair](Yin_C_G0043_v2.md#chebyshev-damping-gram-repair-and-width) | Exact retained original coordinates, all positive final weights, finite rho, complete union support and common shift. |
| dependency | [Full original arithmetic](Yin_C_G0043_v2.md#chebyshev-damping-all-original-costs) | Actual q, FINAL weight denominator/copies, signed full original norms, contents and the actual original-root expense interface; none is waived by the width argument. |
| dependency | [Accepted trigonometric Bernstein](../audits/literature/QZ19/Yin_U001.md#qz19-u001) | Exact Theorem1.1 at its retained arXiv-v1 statement and selected interpolation reading scope; N=2D+1 on the full circle, no Mahler derivative or correction-body input. |
| dependency | [Conditional full-signature premise](Yin_C_G0046_v1.md#full-signature-profile-norm-floor) | Only the explicit Section7 implication for the SAME initial half-profile, original h/k and initial full-norm average; fixed extraction pending adoption. |
| dependency | [Conditional optional house premise](Yin_C_G0046_v1.md#salem-measure-only-profile-price) | Only the optional Section7 measure corollary on genuine-Salem0<m<=log2/4, preserving the exact accepted source-statement boundary; no new acceptance. |
| support | [Whole-author D11 finding](../audits/reviews/Yin_R_G0245_v1.md#retained-scalar-width-whole-finding) | Entire exact original15:06 D11 freeze only, not independent certification of this later extracted statement and fixed interfaces. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T08:28 |
| status | proved |
| reason | Adopt the exact retained-coordinate whole-interval scalar width theorem and its explicitly conditional profile-price compositions after separate whole and actual-extraction reviews. C46 now has its own independent acceptance; retain the original conditional formulation and each reviewer contribution boundary. No arbitrary-packet width theorem or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact supplied general-E0 profile, actual radius/degree/support, whole-interval retention, finite arithmetic and conditional signature/Salem conclusions. |
| argument | [Entire retained original argument](#argument) | Complete D11 Sections1--8, equations1--17, proofs, source/contribution boundaries, original self-check and15:06 freeze. |
| dependency | [Actual half-profile convention](Yin_C_G0037_v1.md#statement) | Actual monogenic order and half-profile conventions only; general-E0 statements use a supplied profile, without an existence theorem. |
| dependency | [Matching half-energy construction](Yin_C_G0043_v2.md#chebyshev-damping-actual-domain-and-statement) | Actual rational half-energy filter, strict positive remainder and sufficient degree/physical-width bounds; a cap is not the necessary actual degree. |
| dependency | [Positive finite paired repair](Yin_C_G0043_v2.md#chebyshev-damping-gram-repair-and-width) | Exact retained original coordinates, all positive final weights, finite rho, complete union support and common shift. |
| dependency | [Full original arithmetic](Yin_C_G0043_v2.md#chebyshev-damping-all-original-costs) | Actual q, FINAL weight denominator/copies, signed full original norms, contents and the actual original-root expense interface; none is waived by the width argument. |
| dependency | [Accepted trigonometric Bernstein](../audits/literature/QZ19/Yin_U001.md#qz19-u001) | Exact Theorem1.1 at its retained arXiv-v1 statement and selected interpolation reading scope; N=2D+1 on the full circle, no Mahler derivative or correction-body input. |
| dependency | [Conditional full-signature premise](Yin_C_G0046_v1.md#full-signature-profile-norm-floor) | Only the explicit Section7 implication for the SAME initial half-profile, original h/k and initial full-norm average; fixed extraction pending adoption. |
| dependency | [Conditional optional house premise](Yin_C_G0046_v1.md#salem-measure-only-profile-price) | Only the optional Section7 measure corollary on genuine-Salem0<m<=log2/4, preserving the exact accepted source-statement boundary; no new acceptance. |
| support | [Whole-author D11 finding](../audits/reviews/Yin_R_G0245_v1.md#retained-scalar-width-whole-finding) | Entire exact original15:06 D11 freeze only, not independent certification of this later extracted statement and fixed interfaces. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0248_v1.md#c47-retained-scalar-width-extraction-finding) | Entire actual statement and fixed argument, precise direct interfaces, full preservation and mathematical limits checked by the separately organized noncontributor at the finding's explicit scope. |

## Argument

The complete original author account follows.
Only the short author header is supplied once, its first title is demoted to a second-level heading, relative links into the claims directory are rebased, and historical same-drafts D9 links are rebased to the drafts directory.
Every original word, proof, conditional status, source limitation, contribution statement and dated freeze is retained.
Historical pending wording is not a new current assessment.

## Actual width floors for retained-coordinate scalar profile repair

Date: 2026-10-12.
Human author Yin.
New bounded AUTHOR inquiry under the root-coordinated G0001 continuation.
Mathematical status: complete author proof with self-review, awaiting separate whole review; no adoption or independent review is asserted.

## Starting question and contribution

Determine whether C43v2's whole-scalar-interval polynomial degree lower bound gives a genuine ACTUAL physical-width lower bound for the SAME common scalar filter architecture.
The final packet must retain at least one nonzero original filtered coordinate p(G/E0-1)f_j with positive final weight.
Root supplied the core candidate: minimal-polynomial divisibility forces actual covariance radius at least d/2; exact Laurent endpoint multiplication prevents support cancellation; then T>=Dd can combine with the accepted scalar degree floor.
This author reconstructs every hypothesis and boundary.
Root and this author are contributors, not independent reviewers.

Use the ACTUAL monic irreducible reciprocal unit minimal polynomial, actual nonzero integer field atoms and normalized rational positive weights.
Separate actual circle maximum C_* from a supplied rational upper C; whole-interval requirements from attained-range-only requirements; exact scalar degree from an upper bound; positive coordinate retention from transformations that delete or recombine coordinates; and finite rational paired repair from its limiting parameters.
Preserve D9's full-signature/Salem profile price only as a conditional premise until fixed acceptance.
No new mathematical program, solver or J is planned.

Direct starting inputs: [C43v2 scalar-order comparison](Yin_C_G0043_v2.md#chebyshev-damping-scalar-order-lower-bound), [C43v2 complete repair](Yin_C_G0043_v2.md#chebyshev-damping-actual-domain-and-statement), [C37 actual profiles](Yin_C_G0037_v1.md#statement), [L394 actual radius versus atom width](../ledger/Yin_L_G0394_v1.md), and the pending [D9 full-signature profile floor](Yin_C_G0046_v1.md#full-signature-profile-norm-floor).
Exact local reuse and the accepted QZ19 source scope will be retained before the proof is frozen.

<a id="scalar-width-reuse-and-source"></a>
## 1. Exact reuse, source scope and the changed assertion

The author read C43v2's selected statement, complete scalar degree comparison, Gram/paired-repair construction, width accounting and original-cost sections.
Its scalar lower bound is explicitly confined to the WHOLE interval, while its physical width is an UPPER bound.
C37 supplies the actual input profile class.
L394 distinguishes actual covariance radius from individual atom width, since lags can cancel among different atom squares.
The present argument respects that distinction; it proves a separate lower bound for the actual radius from the actual minimal polynomial.
L389's original physical union-width convention was also read.
A bounded G-series search for minimal-polynomial radius floors and scalar composition width floors found these related interfaces, without an existing statement of the deduction below.
No exhaustive novelty claim is made.

The accepted external input is ONLY [QZ19-U001](../audits/literature/QZ19/Yin_U001.md#qz19-u001), read in full: arXiv1903.10801v1, Theorem 1.1, printed/PDF p.3, with the recorded selected Riesz interpolation reading on pp.4--5.
A complex trigonometric polynomial of degree at most N>=1 satisfies ||T'||_infinity<=N||T||_infinity.
Its full original proof, QZ19 Section5, the full later correction and Mahler derivative inequalities are not new inputs.
The normalized-energy substitution in Section5 below repeats C43's short argument to make its exact domain visible; it does not claim a new Bernstein theorem.

The degree/divisibility and endpoint support calculations below are direct finite polynomial algebra, not a new external theorem.
Local fixed inputs suffice, so no external search or source-global intake was needed.
The separate D9 author account was read for the exact conditional inequality in Section7.
Its pending status is retained throughout; the unconditional width theorem does not rely on D9.

Root supplied the substantive core: minimal-polynomial radius floor, exact support endpoints, retaining the original filtered coordinates and the scalar-interval comparison.
This author reconstructed the proof, constants, actual-versus-upper-bound distinction, repair behavior and conditional consequences.
Both root and this author are contributors and cannot supply independent review of this derivation.
No native mathematical program, solver, J, numerical root estimate or coefficient approximation was run.

<a id="scalar-width-actual-domain"></a>
## 2. Actual integral profile and the precise architecture

Let P be an ACTUAL monic irreducible self-reciprocal nontorsion integer-unit minimal polynomial of degree d>=2.
Set K=Q(alpha), O0=Z[alpha] and sigma(alpha)=alpha^(-1).
Its original degree is even and P(0)=1, as in C37.
Take any finite nonempty family of nonzero u_j in O0, positive rational weights lambda_j summing to one, and a RATIONAL number E0 with 0<E0<1 such that

    sum_j lambda_j u_j sigma(u_j)=E0 in K.                    (1)

Write f_j in Z[t] for the unique ordinary representative of u_j of degree<d.
Each f_j is nonzero.
For rational Laurent polynomials star replaces t by t^(-1).
Define

    G(t)=sum_j lambda_j f_j(t)f_j(t)^*,
    x(t)=G(t)/E0-1,
    C_*=max_(|z|=1)G(z),
    A=[G]_0=sum_j lambda_j ||f_j||_2^2.                        (2)

On the circle G is real, continuous and nonnegative; its maximum C_* is an ACTUAL finite real number, not assumed rational.
The finite coefficient mean satisfies A>=1 because every f_j is a nonzero integer polynomial.
Evaluation at alpha gives G(alpha)=E0 and x(alpha)=0 as field identities.
Applying each original embedding gives the same identities there.
No equality is claimed between G at a generic point of the unit circle and the field value E0.

For a nonzero Laurent polynomial F put

    lo(F)=min{h:[F]_h!=0}, hi(F)=max{h:[F]_h!=0},
    width(F)=hi(F)-lo(F).                                     (3)

The actual self-star radius of G is r=max{|h|:[G]_h!=0}.
A final finite packet has a positive weight for every retained label.
Its physical width T is the span of the UNION of the coefficient supports of all those labels; after a single common monomial shift this is their actual maximum degree, as in C43.
The support of any retained label is contained in that union.

The architecture tested here chooses one rational real scalar polynomial p of ACTUAL degree D, forms

    v_j(t)=p(x(t))f_j(t),                                     (4)

and retains at least one such nonzero coordinate, unchanged apart from a nonzero scalar factor or monomial shift, with positive final weight.
C43's paired repair retains ALL v_j and satisfies this requirement.
The lower bound also applies if additional coordinates are introduced, even if their lags cancel some covariance lags.
Such covariance cancellation does not delete the occupied coefficient support of a retained coordinate.

For the scalar-degree part, choose a real number C>=C_* and require

    B=C/E0-1,
    p(0)^2=1,
    0<=(1+X)p(X)^2<=1 for EVERY X in [-1,B].                  (5)

Actual rational constructions choose a rational upper C; the lower-bound argument itself requires no rationality of C.
The condition is on the WHOLE indicated interval.
A filter controlled only on the attained range x({|z|=1}) does not automatically satisfy (5).
In particular its lower endpoint may exceed -1.

This is a precise retained-coordinate scalar architecture, not a claim about every exact complementary packet.
Replacing or recombining the original coordinates so that no label of the form (4) survives, or reducing them modulo P to other representatives, falls outside the retention premise.
No covariance, norm or width preservation for those transformations is assumed.

<a id="minimal-polynomial-radius-floor"></a>
## 3. Actual radius forced by the field identity

**Lemma 1.**
Every profile in Section2 satisfies

    G is nonconstant, C_*>1, and d<=2r<=2(d-1).               (6)

*Proof.*
If G were constant, the field identity would make this constant E0, whereas its constant coefficient is A>=1>E0.
Thus r>=1.
Each f_j has ordinary degree at most d-1, so every f_j f_j* has support in [-(d-1),d-1], giving r<=d-1.
Since G is self-star with rational real coefficients, its two endpoint coefficients satisfy g_(-r)=g_r!=0.
Therefore

    Q(t)=t^r(G(t)-E0) in Q[t]                                (7)

is a NONZERO ordinary polynomial of EXACT degree 2r, with nonzero constant and leading coefficients.
Subtracting E0 changes only its middle coefficient.
Since alpha!=0 and G(alpha)=E0, Q(alpha)=0.
The ACTUAL minimal polynomial P divides Q in Q[t], hence d<=2r.
Padding by the actual radius is crucial: no claimed equality of r and individual atom widths enters.

Finally C_*>=A>=1 by integration on the unit circle.
If C_*=1, then the continuous nonnegative function 1-G has integral 1-A<=0; it must vanish everywhere.
Thus G is the constant Laurent polynomial 1, contradicting the preceding argument.
Hence C_*>1.
This is a strict assertion for EACH actual finite profile, not a strict lower bound for its possibly unattained infimum.

<a id="exact-filtered-coordinate-width"></a>
## 4. Exact Laurent width of every retained coordinate

**Lemma 2.**
Let p be any nonzero real scalar polynomial of actual degree D>=0.
Then for every j,

    width(p(x))=2Dr,
    width(v_j)=2Dr+width(f_j).                                (8)

For D=0 these mean that a nonzero scalar has width zero.
For D>=1 write the leading scalar coefficient as a_D!=0.
Since the endpoint coefficients of x are g_(-r)/E0 and g_r/E0, respectively, the coefficients of p(x) at exponents -Dr and Dr are EXACTLY

    a_D(g_(-r)/E0)^D and a_D(g_r/E0)^D.                        (9)

They are nonzero.
Every lower power of x has radius at most (D-1)r<Dr and cannot cancel either endpoint.
Thus the first identity in (8) holds.
For any two nonzero Laurent polynomials, the highest coefficient of their product is the product of their highest coefficients: only the pair of highest exponents contributes.
The same holds at the lowest exponent.
This proves width(FH)=width(F)+width(H) and hence the second identity.
Neither coefficient cancellation inside the product nor cancellation between different coordinate squares changes these endpoint facts.

**Corollary 3 (physical width).**
Any packet retaining a coordinate (4) with positive weight has

    T>=2Dr+width(f_j)>=Dd.                                    (10)

If all original coordinates survive, the stronger inequality T>=2Dr+max_j width(f_j) follows.
A nonzero scalar multiplier, signed monomial twist, common denominator clearing or common monomial normalization preserves the individual width.
Positive weight may be arbitrarily small; occupied support still remains occupied.
Merely listing a coordinate with weight zero would not meet the premise.

The proof of (10) uses ACTUAL degree D, not a sufficient degree cap.
In particular C43's upper bound D<=ceil(sqrt(2C))+2 cannot be inserted as a lower bound here.
Section5 separately supplies a necessary lower bound for D in the whole-interval class.

<a id="whole-interval-physical-width-floor"></a>
## 5. Necessary physical width from the accepted scalar inequality

**Theorem 4.**
Under (1)--(5), the actual scalar degree satisfies D>=1 and

    2D+1 >= 1/arcsin(sqrt(E0/C)) >= (2/pi)sqrt(C/E0).         (11)

Consequently every retained-coordinate packet obeys

    T/d >= D >= max{1, (1/2)(1/arcsin(sqrt(E0/C))-1)},
    T/d >= max{1, sqrt(C/E0)/pi-1/2}.                         (12)

The same assertions with C replaced by C_* are valid for EVERY such packet.
The integer degree may also be bounded below by the ceiling of the real lower bound in (12); no ceiling is needed for the continuous consequences below.

*Proof.*
Lemma1 and E0<1 imply B>0.
If D=0, p(0)^2=1 makes p identically +1 or -1; at X=B the product in (5) equals 1+B>1, contradiction.
Thus D>=1.

For completeness, the source-normalized calculation in C43 applies to every B>0, not only its half-energy B>=1.
Put Q(X)=(1+X)p(X)^2 and

    R(theta)=Q(-1+(B+1)(1-cos theta)/2)-1/2.

This is a real trigonometric polynomial of degree at most 2D+1, with sup norm at most 1/2 on the entire real circle by (5).
At theta=0 its value is -1/2.
At theta0=2arcsin(1/sqrt(B+1)), its affine argument is zero and its value is +1/2.
The accepted QZ19 derivative bound at degree 2D+1 gives

    1<=theta0 ||R'||_infinity<=theta0(2D+1)/2.

This proves the first inequality of (11).
The elementary chord bound arcsin y<=(pi/2)y for 0<=y<=1 proves the second, with y=sqrt(E0/C).
Combining (11), D>=1 and (10) proves (12).

For the actual maximum, the very SAME p satisfies (5) on [-1,C_*/E0-1], because this is a subinterval of [-1,C/E0-1].
Applying the proof on that subinterval gives (11)--(12) with C_*.
No rational representation of C_*, limit of filters, optimizer, or passage through a discontinuous ceiling is used.

Choosing an unnecessarily large upper C imposes a more demanding whole-interval contract and may enlarge the degree/width floor for filters obeying that contract.
It does not enlarge an intrinsic lower bound for filters that never obeyed the enlarged interval.
Conversely the actual-maximum lower bound depends only on the supplied G and its required whole-interval contraction.
If p is only verified on the actual attained range, the step ||R||_infinity<=1/2 can fail and the degree argument above supplies no conclusion for that p.
This boundary is essential.

At E0=1/2 and rational C>=C_*, C43 constructs at least one packet in this precise class with T<=3(ceil(sqrt(2C))+2)(d-1).
Every packet in this class instead has the necessary lower bound T>=d max{1,sqrt(2C)/pi-1/2}.
Thus d sqrt(C) is the correct physical-width ORDER up to absolute factors within this retained-coordinate WHOLE-interval class.
For an explicit nonoptimal comparison, max{1,a-1/2}>=a/2 for a>=0 gives T>=d sqrt(2C)/(2pi) for every such packet, while C>=1 makes the constructed upper bound at most 12d sqrt(2C).
This combines a proved lower mechanism with an existing construction; it does not identify an exact optimum or extend the class.

<a id="positive-paired-repair-retention"></a>
## 6. Paired repair preserves the width floor at every finite step

For C43's actual half-energy construction, p(0)=1, so v_j(alpha)=u_j at EVERY original conjugate.
In the broader lower-bound domain p(0)=-1 merely changes all these values to -u_j; they remain nonzero actual order integers.
The theorem above does not assert the existence of a rational completion for every p satisfying only (5).
Completion requires the additional strictly positive remainder/Gram hypotheses provided by C43 for its actual chosen p.

In C43's construction put x=2G-1, H=(1/2)h(x) and write its rational positive Gram representation as H=sum_a d_a g_a g_a*, d_a>0.
Put Z_a=xg_a and choose a finite rational rho>0.
The two repair labels are

    K_(a,+)=Z_a/rho+1, K_(a,-)=Z_a/rho-1,
    s=rho^2 sum_a d_a>0.

Their raw weights are d_a rho^2/2 per sign.
After normalization the original coordinates v_j remain EXACTLY the same Laurent polynomials and have final weights lambda_j/(1+s)>0.
The final covariance is E'=(1/2+s)/(1+s).
Thus no finite rho deletes the support responsible for (10)--(12).
Choosing a positive sequence rho decreasing to zero gives E' decreasing to 1/2, while EACH finite member still obeys the width floor.
No limiting packet at rho=0 is introduced.

More generally, whenever the same paired repair is valid at rational E0, its normalized energy is (E0+s)/(1+s), strictly increasing in s because E0<1; the finite positive original weights have the same form.
This observation concerns retention and normalization only, and does not claim C43's half-energy construction has already been extended to every E0.

For the actual rational packet, common coefficient denominator clearing multiplies each retained coordinate by a nonzero integer q; a common monomial shift moves all support endpoints by the same integer.
Both leave T unchanged.
Clearing FINAL positive rational weights makes positive integer copies of every retained label, so their support remains.
The full signed original resultants, contents, actual q and weight denominator are still those of the C43/C10 accounting; no denominator or normalization claim is suppressed by the geometric width argument.
In particular letting these denominators grow cannot shrink an occupied exponent span.

<a id="conditional-signature-width-price"></a>
## 7. Conditional all-signature and genuine-Salem consequences

This section is an explicit conditional interface to the PENDING [D9 full-signature theorem](Yin_C_G0046_v1.md#full-signature-profile-norm-floor), not an adoption of that draft.
The unconditional results are Sections2--6.
D9 supplies, for the SAME actual half-profile with ordinary representatives of degree<=d-1,

    k log C_* >= h log2+2d Lambda-2(d-1)m,
    Lambda=(1/d)sum_j lambda_j log|Norm_K(u_j)|>=0,
    h=#{original roots on the unit circle}, k=d-h>0.           (13)

The weights in Lambda are the INITIAL normalized profile weights, not the later paired-repair weights.
The distinction matters even though the width deduction uses only the initial G.
Both members of every complex pair are counted in h and d.
Neither a totally real trace field nor a genuine-Salem root configuration is assumed for (13).

**Conditional Corollary 5.**
If (13) is established for the profile, any half-energy packet in the retained-coordinate WHOLE-interval architecture satisfies

    T/d >= (sqrt(2)/pi)
       exp([h log2+2d Lambda-2(d-1)m]/(2k))-1/2,              (14)

together with the unconditional guard T/d>=1.
This follows directly by substituting the positive lower bound for C_* from (13) into the monotone square root in (12) with E0=1/2.
No lower bound is deduced from C43's sufficient WIDTH UPPER bound; (14) uses the independently proved exact-support lower mechanism of Sections3--5.

For a genuine-Salem input of even original degree d>=4, exactly k=2 roots are off-circle and h=d-2.
Then (14) becomes

    T/d >= (1/pi) 2^(d/4)
                exp(d Lambda/2-(d-1)m/2)-1/2.               (15)

Dropping Lambda>=0 and restricting 0<m<=log2/4 gives the convenient finite bound

    T/d >= (1/pi)2^(d/8)-1/2,                                (16)

again combined with T/d>=1.
Indeed d log2/4-(d-1)m/2>=d log2/8.
Thus the required physical width within this scalar architecture can have an exponential original-degree floor under this precise conditional input, not merely an exponential sufficient upper estimate.

For an optional measure-only formulation, IF D9's already-stated accepted house interface m>=c/d, c=log2/4, is also invoked, its conditional measure bound is C_*>=(1/2)exp(A/m), A=(log2)^2/16, on 0<m<=c.
Substitution in (12) gives

    T/d >= (1/pi)exp((log2)^2/(32m))-1/2.                    (17)

Equivalently (16) and d>=c/m give the same weaker finite estimate.
No fresh source acceptance occurs here: this is conditional on the EXACT input/inspection boundary recorded in D9 and its linked C38/Smy08/Dim19 interface.
Omitting that source premise simply omits (17); (15)--(16) need only (13).

The consequences hold for each actual input/profile satisfying their hypotheses.
They do not assert that any genuine-Salem sequence with m tending to zero exists.
Along such a HYPOTHETICAL sequence, if (13) and the retained house interface are established, the required T/d in this architecture grows faster than any fixed power of 1/m by (17).
That does not prove a gap, disprove another profile completion, or give a lower bound on every possible exact complementary packet.
In particular different coordinate transformations or filters controlled only on a smaller attained range remain outside the conclusion.

<a id="scalar-width-outcome-and-selfcheck"></a>
## 8. Outcome, limitation and author self-check

The tested implication succeeds at a narrower, explicit scope than an arbitrary-packet claim: C43's scalar degree lower bound DOES imply an ACTUAL width lower bound when the whole-interval filter is composed with the actual profile and at least one original filtered coordinate survives at positive weight.
The new bridge is (6)--(10), using the actual minimal polynomial and noncancellable support endpoints.
A lower bound on input C alone cannot reverse a sufficient width upper bound; the present proof supplies the missing independent width-lower argument for this architecture.
It leaves all broader completion questions open.

The concrete changed discriminator is whether a proposed improvement genuinely changes the scalar interval, deletes/replaces the retained coordinates, or uses a non-scalar construction.
Better Gram precision, smaller repair parameters, smaller final positive weights, scalar denominator clearing and cancellation of final covariance lags alone cannot remove (12).
The conditional signature/Salem bounds sharpen this scale test only after their exact premise is independently accepted.

Author self-check covered actual minimality/irreducibility and rational field identities; E0 rational and 0<E0<1; nonzero unique integer representatives; coefficient mean A>=1; nonconstant actual r rather than atom width; Laurent padding and exact degree/constant coefficient of (7); both support endpoints in (9); D=0 and p(0)=-1; actual D versus a degree upper cap; entire interval versus actual attained range; real actual maximum versus rational supplied upper and no ceiling limit; accepted trigonometric degree and source scope; positive finite retention under paired normalization; nonzero coefficient/weight denominator scaling and monomial invariance; all original root counts and initial versus final norm weights; signs and factors of two in (13)--(17); conditional pending-source status; hypothetical near-one sequences and the absence of an arbitrary-packet claim.

No numerical mathematical program, solver, new J, source artifact, global research material or existing fixed proof was changed.
Root and this author supplied the contributions specified in Section1.
The complete proof is author self-checked and awaits a separately organized whole noncontributor review.
Root remains responsible for fixed retention and any later adoption of D9 into Section7.
G0001 remains active and unresolved.

<a id="scalar-width-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T07:06.
The complete Sections1--8, Lemmas1--2, Corollary3, Theorem4 and conditional Corollary5, equations(1)--(17), matching-order comparison within the exact class, positive finite paired-repair retention, actual-versus-upper-C distinction, source scope and all contribution/limitation boundaries are frozen after author self-check.
The scoped material command returned `checked: 1` on the complete body before this final clarification/comparison/freeze addition and is repeated after it.
That check concerns material structure, not mathematical proof.
Independent whole review and later fixed organization remain pending.

## Registration and preservation operation

2026-10-12T08:19.
Human author Yin.
Under the current explicit G0001 instruction, organize the independently whole-reviewed D11 result for fixed reuse while preserving its complete original account.
Before extraction the result was the rolling [D11 author freeze](#scalar-width-entire-author-freeze), with [R245's whole finding](../audits/reviews/Yin_R_G0245_v1.md#retained-scalar-width-whole-finding).
After extraction the registered statement and full argument live together in this fixed C, initially proof draft / under review.
No old decision or historical review is changed.

This extraction adds no mathematical strengthening.
The general-E0 theorem assumes a supplied profile, the matching existence statement remains half-energy, and all D9 compositions remain explicit conditional implications.
The actual fixed D9 locator is [C46](Yin_C_G0046_v1.md#statement), independently allocated and then communicated by its extractor; its pending extraction is not silently accepted.
Source-domain, actual-degree, interval, retained-coordinate, finite-repair and original arithmetic boundaries remain visible.
D9 ancestry in the retained author body stays at its historical draft locator, while the new selected conditional interfaces identify exact fixed sections.

The extractor read the whole original D11 and R245 before organization and checked the direct C43v2, C37 and QZ19 interfaces for faithful registration.
This is extraction work, not independent review of the extracted Claim.
Root coordinates subsequent independent interface review, dependency adoption, live strategy/navigation changes and any later draft retirement.
The original D11 remains intact.
No manuscript, historical R or source record is edited by this extraction.
