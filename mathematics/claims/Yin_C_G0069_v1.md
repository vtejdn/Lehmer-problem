---
author: Yin
---
# Finite trace classification of biased binomial pairs and the Salem radial price

Date: 2026-10-12T13:00.
Human author Yin.
Fixed extraction under continuing G0001 authorization.
Root authored the original D24 mathematics and its20:53 correction.
g0001_review_recovery independently whole-reviewed that actual corrected body in R292 and NOW authors this new exact statement and extraction wrapper.
R292 remains evidence about the original whole body only; this new Claim needs actual statement/interface review by a different noncontributor.
The original negative R291 remains fixed at its original20:41 scope.
This registration makes no adoption or draft-retirement decision.

## Statement

Let P be an ACTUAL monic irreducible polynomial in Z[t], the minimal polynomial of a nontorsion algebraic integer unit alpha, with ORIGINAL degree d>=2, field K=Q(alpha), original monogenic order O0=Z[alpha], all original conjugates beta_1,...,beta_d, nu=Norm_(K/Q)(alpha) in{+1,-1}, coefficient height H_P=max_i|p_i| and total logarithmic Mahler measure m(P)>0.
No reciprocity or flatness is assumed unless explicitly stated below.
Choose a positive INTEGER h and NONZERO integers a,b.
All norms and multiplicities below use K and d, even if a powered element has smaller degree.

**A. Exact pair and both original-degree ratio tests.**
Retain BOTH indexed polynomials F_+(t)=a+b*t^h and F_-(t)=a-b*t^h, each with weight1/2.
Their values are nonzero O0 integers, their actual common physical width is h, their actual coefficient denominator is q=1, and their FINAL indexed weight denominator is M=2, one copy of each label.
Their complete complementary energy and signed full norms satisfy

    E=a^2+b^2>=2,
    D_+=Norm_(K/Q)(a+b*alpha^h),
    D_-=Norm_(K/Q)(a-b*alpha^h),
    D_+*D_-=Norm_(K/Q)(a^2-b^2*alpha^(2h)),
    sigma(a,b)=log|D_+*D_-|/(2d)-(1/2)log E.

For e in{+1,-1}, define

    B_e(X)=product_(i=1)^d(X-beta_i^(e*2h)),
    K_e(X)=B_e(X)-(X+1)^d.

B_e is monic integral of ORIGINAL degree d, retaining every repeated powered conjugate.
K_e is a nonzero integer polynomial of degree at most d-1.
For X=(a/b)^2 and Y=(b/a)^2,

    sigma(a,b)=(1/(2d))log(|B_+(X)|/(X+1)^d)
              =(1/(2d))log(|B_-(Y)|/(Y+1)^d).

In the inverse-orientation factorization the original SIGNED norm factor is(-1)^d*nu^(2h)=(-1)^d before absolute values.
No reciprocal symmetry is assumed for these two identities.
For real X>(1+H_P)^(2h), B_e(X)>0, so the corresponding full surplus is positive exactly when K_e(X)>0.
Every coefficient content remains in D_+,D_-; there is no E<1 premise.

**B. Complete finite first-trace classification, effective threshold and fixed-input limit.**
Put

    s_(e,j)=Tr_(K/Q)(alpha^(e*2h*j)),
    C_(e,j)=s_(e,j)-d*(-1)^j, 1<=j<=d,
    s_e=min{j in{1,...,d}: C_(e,j)!=0}.

This first index exists in BOTH orientations.
If k_e=d-s_e, then the leading coefficient of K_e is the NONZERO integer

    c_e=-C_(e,s_e)/s_e,
    deg K_e=k_e.

In particular s_e divides C_(e,s_e).
Write K_e(X)=c_e*X^(k_e)+sum_(ell<k_e)k_(e,ell)*X^ell and put L_e=sum_(ell<k_e)|k_(e,ell)|, with L_e=0 when k_e=0.
Define the finite exact threshold and an integer amplitude

    R_e=max{1,(1+H_P)^(2h),L_e/|c_e|},
    A_e=2+(1+H_P)^(2h)+L_e.

Whenever the oriented squared ratio exceeds R_e, its complete surplus has sign -sign(C_(e,s_e)).
One has A_e^2>R_e: (a,b)=(A_+,1) and(1,A_-) give the corresponding strict signs, and larger integer amplitudes in that orientation have the same sign.
Thus a negative first C gives arbitrarily biased successful pairs, whereas a positive first C gives eventual failure in that direction.
This is a classification, not only a sufficient trace test.

For FIXED P and h, the limits over nonzero integer amplitude ratios are

    lim_(|a/b|->infinity)(a/b)^(2s_+)*sigma(a,b)
         =-C_(+,s_+)/(2d*s_+),
    lim_(|b/a|->infinity)(b/a)^(2s_-)*sigma(a,b)
         =-C_(-,s_-)/(2d*s_-).

These thresholds and asymptotics are not asserted uniform as P,h or d varies.
The local Newton/formal-series proof covers repeated powered roots without a degree substitution.

**C. Genuine Salem inputs: two-sided finite bias restriction and ALL-ratio radial gate.**
Assume ADDITIONALLY that P is a genuine Salem minimal polynomial, with roots beta>1,beta^(-1) and d-2 unit-circle roots; here m(P)=log beta.
Then C_(e,1)>4 and s_e=1 for BOTH orientations.
Both extreme-bias directions eventually fail.
Every positive-surplus pair lies in the guaranteed CLOSED interval

    1/R_- <= (a/b)^2 <= R_+.

No sign at the untested threshold endpoints is claimed.
For EVERY nonzero amplitude ratio, put

    v=a^2*b^2/(a^2+b^2)^2 in(0,1/4],
    x=h*m(P)>0.

Positive surplus NECESSARILY implies

    |1-4v*cosh(x)^2|>1,
    v>1/(2*cosh(x)^2),
    x>log(1+sqrt(2)).

Consequently ALL pairs at h*m(P)<=log(1+sqrt(2)) have nonpositive full surplus, regardless of amplitude height or bias.
This is an all-ratio necessary condition, not sufficient: all original unit-circle factors and their phase losses remain charged.
The input-dependent finite interval is not an absolute interval for varying inputs.

**D. Separate small-measure angular/radial price and exact sequence/product scope.**
Retain the ADDITIONAL genuine-Salem hypothesis of C and the separately accepted C66/L229 angular interface with

    U=h*m(P)/d=x/d,
    c0=log(2)/4, h0=c0*exp(-20),
    b(u)=max{u,sqrt(u/c0)*log(sqrt(c0/u))},
    epsilon(u)=min{1,15*sqrt(b(u))+4u}, 0<u<=h0,
    delta=epsilon(2U)+4U.

Under the EXPLICIT supplied conditions0<2U<=h0 and delta<1, positive sigma forces v<2U/(1-delta).
Combining with C gives

    4x*cosh(x)^2>d*(1-delta).

If in addition delta<=1/2 and d>=256, then every positive pair satisfies

    h*m(P)>(1/4)log d.

For any fixed C>0, such a pair at h<=C*d therefore requires m(P)>log d/(4C*d).
This is a conditional necessary price; A--C and E do not use the angular source estimate.

Precisely, for ANY hypothetical sequence of actual genuine Salem inputs with positive m(P)->0 and the EXTRA rate condition d*m(P)/log d->0, and for every FIXED C>0, eventually NO positive-surplus pair with1<=h<=C*d exists, for ANY nonzero integer amplitudes depending on the input.
Actual integer-coefficient finiteness at bounded degree and measure gives d->infinity; U<=C*m(P)->0 makes the explicit angular conditions eventual.
The EXTRA rate is not silently deduced from m(P)->0 alone.

The same eventual exclusion holds for the complete independent-sign product family of C66: any finite number r>=1 of factors(a_j+epsilon_j*b_j*t^(h_j)), ALL2^r sign labels with weights2^(-r), positive integer h_j, nonzero integer a_j,b_j, and actual total width T=sum_j h_j<=C*d.
The exact total sigma is sum_j sigma_j, so a positive total supplies a positive constituent with h_j<=T.
This remains valid when r, amplitudes and exponents vary with the input; uniform epsilon(u)->0 on0<u<=2C*m(P) supplies the common eventual domain.
No uniform absolute margin is transferred to one constituent.
A legal single common rational rescaling of such a product leaves sigma unchanged under C66's separate actual O0-membership condition; arbitrary nonproduct weights or unrelated packet constructions are outside this conclusion.

Neither the hypothetical input sequence nor a successful packet is asserted to exist.
There is no unrestricted G0001 obstruction, uniform positive construction, or inference that d*m/log d tends to zero on every near-one family.

**E. An actual irreducible general-unit control positive at ALL biases.**
The polynomial P(t)=t^4+5t^2+1 is irreducible over Q, monic integral, reciprocal and a nontorsion unit polynomial of ACTUAL degree4.
Its two imaginary expanding roots and two imaginary contracting roots give fixed total m(P)=log((5+sqrt(21))/2)>0; it is not Salem and is not a near-one family.
At h=1,

    B_+(X)=(X^2+5X+1)^2,
    K_+(X)=6X^3+21X^2+6X>0 for X>0.

The powered element's degree2 does not remove the ORIGINAL degree4 square.
For ALL nonzero integers a,b,

    D_+=D_-=a^4+5a^2*b^2+b^4>0,
    D_+*D_-=(a^4+5a^2*b^2+b^4)^2,
    E=a^2+b^2,
    sigma=(1/4)log[(a^4+5a^2*b^2+b^4)/(a^2+b^2)^2]>0.

The actual q is1, FINAL indexed M is2, and physical width is1.
Both contents equal g=gcd(|a|,|b|); g^4 per norm and g^8 in their copied product remain present, cancelling only in the complete surplus.
The original trace is-10, C_(+,1)=-6, and lim_(|a|->infinity)a^2*sigma(a,1)=3/4, with the reciprocal orientation analogous.
This disproves a general-unit eventual-bias-failure claim.
The surplus still tends to zero as bias diverges, so it gives no uniform positive margin or near-one input construction.

**F. Algebraic homogeneity versus admissibility; full actual costs.**
For EVERY common positive rational scalar c, define scaled pair values c*(a+/-b*alpha^h).
Independently of whether they are integral, the full algebraic norms and energy obey

    D'_+=c^d*D_+, D'_-=c^d*D_-, E'=c^2*E,
    log|D'_+*D'_-|/(2d)-(1/2)log E'=sigma.

The scaled pair remains an ADMISSIBLE actual integer packet only when BOTH values belong to the original O0; nonvanishing is automatic.
Under that separately imposed condition D'_+,D'_- are nonzero signed integers.
Let q_star be the ACTUAL least coefficient denominator after scaling and coefficient cancellation.
Keeping the two original indexed labels, FINAL M remains2 and the complete signed numerator resultant is

    q_star^(2d)*D'_+*D'_-.

No denominator of c before cancellation, norm divisibility test, or merged-label denominator replaces actual q_star or FINAL M.
All contents and inverse-orientation signs remain charged.
A common monomial shift preserves physical width and absolute norms, while its signed nu powers remain in every affected norm.
Merging/splitting labels or independently shifting atoms requires recomputing actual FINAL M/copy multiplicities and common physical width; no such operation is part of the asserted raw-pair formula.

The original false ONLY IF assertion about algebraic equality, its exact c=1/2 quartic counterexample, negative R291 and dated repair are retained in the complete argument.
The Mas12 selected Newton formula is attribution for the locally proved recurrence, not a new unproved premise or retrospective alteration of L10's history.
No source-proof scope, first-window theorem, smaller powered degree or free normalization is imported.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T13:00 |
| status | open |
| reason | Register the exact A--F statement and entire corrected20:53 D24 argument, retaining original allocation, first freeze, original negative R291, actual scaling correction and selected Mas12 attribution. R292 whole-reviewed the original corrected body only; its reviewer now authors this new wrapper, so a different noncontributor must inspect the actual extraction before adoption. No draft retirement or unrestricted Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, general actual unit and both orientations, finite and asymptotic classification, additional Salem/explicit angular hypotheses, all sequence/product limits, actual positive control and full costs. |
| argument | [Complete retained corrected proof](#argument) | ENTIRE original allocation/candidate/history, Sections1--6/equations1--18, original20:41 freeze,20:53 scaling repair and preserved counterexample/negative review, plus actual selected-source attribution. |
| dependency | [C66 exact independent-sign product](Yin_C_G0066_v1.md#biased-sign-product-exact-packet) | ONLY D's product extension: complete indexed norm/energy identity, exact finite sum of constituent surpluses and total physical width; no new positive-margin conclusion. |
| dependency | [C66 supplied small-measure budget](Yin_C_G0066_v1.md#biased-sign-product-small-measure-budget) | ONLY D: v<2U/(1-delta) for a single pair, with exact supplied conditions, cutoff2h and delta=epsilon(2U)+4U. |
| dependency | [C66 legal scaling interface](Yin_C_G0066_v1.md#statement) | ONLY D's legal common rational scaling of its specified product family, PartD actual O0 membership and retained complete costs; pair scaling in F is also proved locally. |
| dependency | [L229 actual angular interface](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | ONLY D's supplied epsilon/c0/h0/b domain and uniform epsilon(u)->0, preserving every original powered multiplicity and accepted Pri11/Dim19 source limit. |
| support | [Corrected original whole review](../audits/reviews/Yin_R_G0292_v1.md#biased-pair-corrected-whole-finding) | ENTIRE actual20:53 corrected D24 and its exact interfaces, not this newly authored statement/wrapper or a prospective adoption. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T13:16 |
| status | proved |
| reason | Adopt the corrected original whole R292 and separate actual extraction R294, preserving original negative R291 and the dated scaling counterexample/repair. The original-degree two-orientation finite trace classification, genuine-Salem radial necessary gate, explicitly conditional angular price and actual positive control are proved at their stated scopes. Algebraic scaling and actual integer admissibility remain distinct; no uniform lower income or unrestricted gap follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, general actual unit and both orientations, finite and asymptotic classification, additional Salem/explicit angular hypotheses, all sequence/product limits, actual positive control and full costs. |
| argument | [Complete retained corrected proof](#argument) | ENTIRE original allocation/candidate/history, Sections1--6/equations1--18, original20:41 freeze,20:53 scaling repair and preserved counterexample/negative review, plus actual selected-source attribution. |
| dependency | [C66 exact independent-sign product](Yin_C_G0066_v1.md#biased-sign-product-exact-packet) | ONLY D's product extension: complete indexed norm/energy identity, exact finite sum of constituent surpluses and total physical width; no new positive-margin conclusion. |
| dependency | [C66 supplied small-measure budget](Yin_C_G0066_v1.md#biased-sign-product-small-measure-budget) | ONLY D: v<2U/(1-delta) for a single pair, with exact supplied conditions, cutoff2h and delta=epsilon(2U)+4U. |
| dependency | [C66 legal scaling interface](Yin_C_G0066_v1.md#statement) | ONLY D's legal common rational scaling of its specified product family, PartD actual O0 membership and retained complete costs; pair scaling in F is also proved locally. |
| dependency | [L229 actual angular interface](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | ONLY D's supplied epsilon/c0/h0/b domain and uniform epsilon(u)->0, preserving every original powered multiplicity and accepted Pri11/Dim19 source limit. |
| support | [Corrected original whole review](../audits/reviews/Yin_R_G0292_v1.md#biased-pair-corrected-whole-finding) | ENTIRE actual20:53 corrected D24 and its exact interfaces, not this newly authored statement/wrapper or a prospective adoption. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0294_v1.md#biased-pair-actual-extraction-finding) | Complete actual statement/argument, entire original preservation and exact direct interfaces checked after allocation by a noncontributor, with prior ancestor roles disclosed. |

## Registration and complete preservation

This is author extraction of the whole corrected result, not a new research deduction or acceptance.
[Original D24](#biased-pair-entire-author-freeze) and its [actual20:53 correction](#biased-pair-rescaling-dated-correction) are ancestry and the preservation target, not a missing argument behind this fixed Claim.
Root remains the original mathematical and correction author; g0001_review_recovery authors the new statement/wrapper.
A different reviewer must examine this actual Claim's quantifiers, statement/body interfaces and complete preservation.

The ENTIRE original D24 body follows.
Only its duplicate front matter is represented once, its first title is demoted from one hash to two, and line endings and separating/terminal blank space are normalized.
All original formulas, anchors, allocation and pending-status history, failed strengthenings, original20:41 freeze, negative R291 link,20:53 correction/counterexample and Mas12 attribution are retained.
Existing relative links remain valid from this sibling Claim directory; no source passage, proof paragraph or meaningful historical sentence is omitted.

The ordinary Mas12 source account and [actual selected PDF](../literature/pdf/Mas12.pdf) retain attribution-only scope, with the local formal-series derivation supplying the proof.
They are not canonical R binding targets or new accepted source-theorem units.
L10 is local formula ancestry with its old historical attribution limit, not a reciprocal-input premise for this general-unit result.
R291's original negative verdict remains fixed; R292 does not automatically cover this extraction merely because its proof body is preserved.

No adoption, original-D retirement or new native mathematical program accompanies this registration.
Body comparison and material checks are author preservation/structure checks only, not independent review of this new wrapper.

## Argument

## Exact trace classification of highly biased complementary binomial pairs

Date: 2026-10-12T12:38.
Human author Yin.
Root author inquiry under the continuing G0001 instruction.
Root selects all formulas and proofs below; another noncontributor must independently review any completed result.
No new native mathematical run, primary-source intake, adoption or execution allowance is part of this draft.

## Responsible question and bounded reuse

[C66](Yin_C_G0066_v1.md#statement) identifies very unequal amplitudes as an unproved remaining possibility for the complete independent-sign product family.
Its actual-extraction review has been delivered; responsible adoption is separately pending at this allocation.
This draft studies a SINGLE actual pair and the fixed-input large-ratio limit, without presuming that limit uniform in degree, polynomial or exponent.
The exact pair arithmetic will be proved locally, so pending adoption is not a missing mathematical premise.

A bounded G Claim/ledger/draft search for large amplitude, high bias, binomial trace, power sums and Newton identities found [L10's integer orbit supplement](../ledger/Yin_L_G0010_v1.md#integer-orbit-constraints), [C26](Yin_C_G0026_v1.md#statement), C66, the older balanced-pair Poisson limitation and the trace-construction work C1/C8.
L10's formal logarithmic-derivative derivation was actually read: its retained statement is reciprocal, while the elementary coefficient identity is locally derived below for the present general unit.
Its original priority/source-attribution limitation is preserved; no new literature-wide novelty or uninspected theorem claim is made.

<a id="biased-pair-responsible-candidate"></a>
## Candidate and exact input

Let P be an actual monic irreducible nontorsion integer-unit minimal polynomial, degree d>=2, alpha a root, actual order O0=Z[alpha], and all original conjugates beta_i.
Fix a positive integer h.
For nonzero integers a,b retain both indexed polynomials a+b t^h and a-b t^h, each with weight1/2.
The proposed question is whether the sign of their COMPLETE norm surplus at arbitrarily large amplitude ratio is determined by a finite list of original traces.
Both orientations a/b and b/a must be priced; reciprocal symmetry is not assumed.
Any constructive positive control must be an actual irreducible unit input, retain original powered-root multiplicities, both full signed norms, q and final M, and have its fixed positive measure distinguished from a hypothetical near-one sequence.

No theorem is claimed at allocation.
Work will remain here, including any failed strengthening, full finite algebraic control, exact domain, safe checkpoint and proof/review boundaries.
No enumeration is authorized by this candidate.
An initial normal-allocation request lacking the required leading author header was refused without creating a material; this corrected request uses the same supported allocator with the required header, not a predicted identifier.


<a id="biased-pair-exact-full-norm"></a>
## 1. Exact original pair and a finite polynomial sign test

Write K=Q(alpha), nu=Norm(alpha)=+/-1 and H_P=max_i|p_i|.
Both actual values a+/-b alpha^h are nonzero: otherwise alpha^h would be rational and both it and its inverse integral, hence +/-1, contrary to nontorsion.
The circle average is exactly a^2+b^2, so with BOTH original signed norms D_+,D_-, the complete income and surplus are

    D_+ D_-=Norm(a^2-b^2 alpha^(2h)),
    sigma(a,b)=log|D_+D_-|/(2d)-(1/2)log(a^2+b^2).       (1)

This is an actual complementary packet with q1, FINAL indexed M2, one copy of each label and actual common width h.
The leading and constant coefficients are nonzero.
Every coefficient content, original degree and signed norm is retained.
No coefficient-energy-below-one hypothesis is made.

For e in{+1,-1}, define the original-degree polynomials

    B_e(X)=product_(i=1)^d (X-beta_i^(e*2h)),
    K_e(X)=B_e(X)-(X+1)^d.                              (2)

Let A be multiplication by alpha in the ORIGINAL integer power basis of O0.
It and A^-1 are integer matrices because p0 is a unit.
Then B_e=det(XI-A^(e*2h)) is monic integral of degree d.
The original roots and their multiplicities are all retained, even if alpha^(2h) has smaller minimal degree.
Characteristic0 gives the d distinct embeddings of K, and hence this eigenvalue/product identity; no powered-degree preservation is assumed.

For X=(a/b)^2, cancellation of the complete b^(2d) factor in (1) gives

    sigma(a,b)=(1/(2d))log(|B_+(X)|/(X+1)^d).           (3)

For Y=(b/a)^2, instead factor (-alpha^(2h)) at ALL roots.
Its full norm is (-1)^d nu^(2h)=(-1)^d, so after the absolute value

    sigma(a,b)=(1/(2d))log(|B_-(Y)|/(Y+1)^d).           (4)

The sign factor is not silently discarded in the signed product; (4) is an absolute-income equality only.
Thus both extreme orientations have a genuine original-field test, with no unjustified a/b symmetry for a nonreciprocal input.

Each K_e is NONZERO: if B_e=(X+1)^d, every beta_i^(e*2h)=-1, so alpha^(4h)=1.
Its degree is at most d-1.
All roots of either P or its monic reciprocal p0*t^d*P(t^-1) have modulus at most1+H_P.
Indeed for |z|>1+H_P, the nonleading coefficient sum is at most H_P sum_(j=0)^(d-1)|z|^j<|z|^d.
The reciprocal has the same coefficient height.
Consequently for real X>(1+H_P)^(2h), all real factors of B_e(X) are positive and every complex conjugate pair contributes a positive modulus square, so B_e(X)>0.
In this range (3) or (4) is positive EXACTLY when K_e(X)>0.

<a id="biased-pair-first-trace-classification"></a>
## 2. Complete finite first-trace classification and effective threshold

Put s_(e,j)=Tr_(K/Q)(alpha^(e*2h*j)) and

    C_(e,j)=s_(e,j)-d*(-1)^j, 1<=j<=d.                 (5)

All are integers.
For any multiset lambda_1,...,lambda_d, Q(z)=product(1-lambda_i z) satisfies the formal identity

    -z Q'(z)/Q(z)=sum_(j>=1)(sum_i lambda_i^j) z^j.

This is obtained by differentiating each factor and expanding 1/(1-lambda_i z) as a formal geometric series.
If B(X)=X^d+c1 X^(d-1)+...+cd, coefficient comparison gives

    s_j+c1 s_(j-1)+...+c_(j-1)s_1+j*c_j=0, 1<=j<=d.   (6)

This is the elementary Newton calculation already credited in L10, now explicitly valid here without its reciprocal-input specialization.
Compare (6) to the d roots all equal to -1.
If C_(e,j) vanished for j1,...,d, successive coefficients would all equal those of(X+1)^d, contradicting K_e nonzero.
Thus the first nonzero index s_e lies in{1,...,d}.
All earlier coefficients agree and the first differing coefficient is

    c_e=-C_(e,s_e)/s_e, a NONZERO integer,
    deg K_e=d-s_e.                                     (7)

Here s_e is an index, distinguished from the trace s_(e,j).
Equation(7) follows by subtraction of the j=s_e equations: all preceding coefficient and trace terms coincide.
In particular s_e divides C_(e,s_e).

Write K_e(X)=c_e X^m+sum_(ell<m)k_ell X^ell, with m=d-s_e, and let L_e=sum_(ell<m)|k_ell| (zero when m0).
For X>=1 and X>L_e/|c_e|, the lower sum has magnitude at most L_e X^(m-1)<|c_e|X^m when m>=1; for m0 the constant sign is immediate.
Thus for

    X>R_e=max{1,(1+H_P)^(2h),L_e/|c_e|},               (8)

the complete surplus in the corresponding orientation has sign -sign C_(e,s_e).
This is a computable FINITE fixed-input threshold using exact integer companion powers or (6); no root approximation or experiment is needed.
For example the integer A_e=2+(1+H_P)^(2h)+L_e satisfies A_e^2>R_e.
Taking(a,b)=(A_e,1) for e+ or(1,A_e) for e- is an actual strict-sign control.
Larger integer amplitudes in that orientation have the same sign.
This is an existence of arbitrarily biased successful pairs if the first C is negative, and an eventual failure theorem if it is positive, not merely a sufficient trace test.

The precise fixed-input asymptotic is

    lim_(|a/b|->infinity) (a/b)^(2s_+) sigma(a,b)
                       =-C_(+,s_+)/(2d s_+),
    lim_(|b/a|->infinity) (b/a)^(2s_-) sigma(a,b)
                       =-C_(-,s_-)/(2d s_-).           (9)

Indeed K_e(X)/(X+1)^d=c_e X^(-s_e)+O(X^(-s_e-1)), and log(1+y)/y tends to1.
The limit is over nonzero integer amplitude ratios tending to infinity; homogeneity makes it a function of the ratio.
All constants and thresholds here depend on the FIXED P,h.
Equation(9) is not a uniform asymptotic when d, P or h varies.

<a id="biased-pair-salem-finite-bias-gate"></a>
## 3. Genuine Salem inputs: eventual bias failure and an all-ratio radial gate

Assume now P is a genuine Salem minimal polynomial: its roots consist of beta>1,beta^-1 and d-2 unit-circle roots, with m(P)=log beta.
All original roots remain.
For either orientation e,

    s_(e,1)>=beta^(2h)+beta^(-2h)-(d-2)>4-d,
    C_(e,1)=s_(e,1)+d>4.                              (10)

Reciprocity permutes the roots, so both orientations have the same trace; (10) can also be checked separately.
Hence s_e1 and c_e=-C_(e,1)<0, and all sufficiently extreme ratios fail in BOTH directions.
Any successful ratio must lie in the finite input-dependent interval R_-^(-1)<(a/b)^2<R_+ (enlarging either R if necessary does not harm the statement).
Strict endpoints can instead be included harmlessly; only ratios outside the open region where(8) is strict are excluded.
To avoid attributing the untested threshold endpoints a sign, the exact guaranteed containment is

    1/R_- <= (a/b)^2 <= R_+.                           (11)

There is a stronger necessary condition valid at EVERY nonzero amplitude ratio.
Set A0=a^2+b^2, v=a^2b^2/A0^2 in(0,1/4], and x=h log beta.
Each unit-circle factor of the full product has modulus at most A0.
The product of the real reciprocal pair is exactly

    (a^2-b^2 beta^(2h))(a^2-b^2 beta^(-2h))
       =A0^2[1-v(beta^h+beta^-h)^2].                    (12)

If sigma>0, the full absolute product exceeds A0^d.
Therefore necessarily

    |1-4v cosh^2 x|>1,
    v>1/(2 cosh^2 x),
    x>log(1+sqrt2).                                    (13)

The second inequality uses v>0 and the last uses v<=1/4 and the strict monotonicity of cosh on x>0.
The exact equality cosh(log(1+sqrt2))=sqrt2 follows directly.
Consequently EVERY pair at h*m(P)<=log(1+sqrt2) has nonpositive full surplus, regardless of bias or coefficient height.
Condition(13) is necessary, not sufficient: unit-circle phase losses are still charged.
This gives a meaningful upper limit on admissible bias at a fixed radial expenditure, with both amplitude orientations included.

No uniform G0001 impossibility follows: h<=C*d permits h*m as large as C*d*m, and no required bound on d*m has been proved.
In particular the input-dependent interval(11) cannot be combined with an unbounded-degree limit as though its endpoints were absolute.

<a id="biased-pair-angular-radial-price"></a>
## 4. Combining the separate accepted angular test at its exact scope

For a single pair, [C66 PartC](Yin_C_G0066_v1.md#statement) gives an additional necessary condition ONLY with its explicit supplied small-measure hypotheses.
Write U=h*m(P)/d=x/d, c0=log2/4, h0=c0*exp(-20),

    b(u)=max{u,sqrt(u/c0)*log(sqrt(c0/u))},
    epsilon(u)=min{1,15sqrt(b(u))+4u},
    delta=epsilon(2U)+4U,
    0<2U<=h0, delta<1.

Then positive sigma forces v<2U/(1-delta).
Combining this UPPER bound with the LOWER bound(13) gives the necessary joint price

    4x cosh^2 x > d(1-delta).                           (14)

This paragraph is explicitly conditional on that separately fixed angular interface; Sections1--3 and5 do not need its external source estimates.
C66 in turn retains the original L229 angular-source and powered-multiplicity scopes; this draft does not claim new source-proof inspection.

If additionally delta<=1/2 and d>=256, every positive pair must satisfy

    h*m(P) > (1/4)log d.                               (15)

For if 0<x<=(1/4)log d, then cosh^2 x<=exp(2x)<=sqrt d, so4x cosh^2 x<=sqrt d log d<=d/2.
The last inequality is log d<=sqrt d/2: at256 it holds, and the derivative of sqrt d/2-log d is (sqrt d-4)/(4d)>=0 thereafter.
This contradicts(14), whose right side is at least d/2.
Thus any such pair at h<=C*d necessarily has

    m(P)>log d/(4C*d).                                 (16)

For a hypothetical Salem sequence with m->0 and d*m/log d->0, no positive single pair with h<=C*d exists eventually.
Here d necessarily tends to infinity along that hypothesis (log d bounded below and d*m tends to zero for bounded d; alternatively the fixed-degree integer-coefficient finiteness at bounded Mahler measure rules out a positive near-one sequence).
A direct proof of the latter finiteness is |p_(d-j)|<=binom(d,j)*exp(m), by the elementary symmetric sums and each subset root product<=exp(m); finitely many integer coefficient vectors remain for bounded d,m.
Thus the d>=256 condition is eventually valid.
Since U<=C*m->0, the explicit small-measure and delta<=1/2 conditions also eventually hold.

A complete sign-product packet with positive TOTAL sigma has at least one constituent with positive sigma_j, by C66's exact sum, and that h_j<=T.
Therefore the same eventual exclusion applies to that entire independent-sign product family at T<=C*d along the stated additionally small d*m/log d sequence.
No monotonicity of delta at different cutoffs is assumed: apply the uniform limit epsilon(u)->0 to each 0<U_j<=C*m, so all constituent tests meet the same eventual hypotheses.
This still excludes only a specified recipe on a conditional sequence, not an actual exhibited family or the unrestricted gap.

<a id="biased-pair-actual-positive-control"></a>
## 5. Actual all-bias successful control, original multiplicities and all costs

The polynomial P(t)=t^4+5t^2+1 is monic, integral, reciprocal and a unit polynomial.
It is irreducible over Q: rational linear roots would be +/-1, neither a root.
A reducible monic integer quartic without a linear factor must factor as(t^2+c t+b)(t^2-c t+e) with integers c,b,e and be1.
Thus b=e=1 or b=e=-1, and the t^2 coefficient b+e-c^2 is at most2, never5.
This uses the elementary monic integer factor property: rational monic factors of an integer monic polynomial have algebraic-integer rational coefficients, hence integer.
There is no missed opposite-sign constant case because be1.

The squared roots are the two negative numbers(-5+/-sqrt21)/2.
The four roots are +/-i*sqrt((5+sqrt21)/2) and their inverse-modulus counterparts, so P is nontorsion and its fixed total measure is log((5+sqrt21)/2)>0.
It is not Salem and does not form a near-one sequence.
At h1, the ACTUAL original-degree polynomial is

    B_+(X)=(X^2+5X+1)^2,
    K_+(X)=6X^3+21X^2+6X>0 for X>0.                   (17)

The powered element has degree2, but the norm polynomial MUST keep the square at original degree4.
Direct substitution gives, for ANY nonzero integer a,b,

    D_+=D_-=a^4+5a^2b^2+b^4>0,
    D_+D_-=(a^4+5a^2b^2+b^4)^2,
    E=a^2+b^2,
    sigma=(1/4)log[(a^4+5a^2b^2+b^4)/(a^2+b^2)^2]>0. (18)

Every atom is a nonzero actual integer, q1, FINAL M2, width1, and the two numerator contents both equal gcd(|a|,|b|).
Their fourth powers remain in the norms and eighth power in the signed copied product; they cancel only in the complete surplus.
The trace is Tr(alpha^2)=-10, C_(+,1)=-6, so for b1 equation(9) reads lim_(|a|->infinity) a^2 sigma(a,1)=3/4, agreeing with(18).
Reciprocity gives the analogous other orientation.
No native computation is used: every expansion and coefficient identity is displayed and hand-derived.

This explicit control disproves a general-unit claim that sufficiently biased complementary pairs must fail.
It does not prove that the surviving high-bias regime supplies ANY uniform positive margin: even for this fixed successful input, the surplus tends to zero as bias diverges.
It also shows why original powered multiplicity and signature cannot be dropped in a trace criterion.

<a id="biased-pair-full-costs-and-failed-strengthenings"></a>
## 6. Exact rescaling boundary and failed stronger conclusions

All formulas above retain the two full signed degree-d norms and exact original width.
For EVERY common positive rational scalar c, the displayed full-norm surplus is algebraically unchanged, whether or not the scaled values are integers.
The scaled pair is still an ADMISSIBLE actual integer packet ONLY IF BOTH c(a+/-b alpha^h) belong to the actual O0 (nonvanishing already follows from c>0 and Section1).
In the following admissible-packet accounting, impose that separate integrality condition.
Let q_star be the actual least coefficient denominator after this operation, not the denominator of c before cancellation.
Then E'=c^2E, D'_+/-=c^d D_+/-, the full copied integer numerator resultant is q_star^(2d) D'_+D'_-, and final indexed M remains2 if the original two labels remain.
Norm divisibility alone is no integrality test.
Contents and the sign(-1)^d in the inverse-orientation factorization stay charged.
A common monomial shift retains width and absolute norms but contributes nu raised to its actual signed norm exponent.
Merging/splitting labels or independent shifts require their own actual final M/common-width calculation; none is used in the theorem.

Rejected strengthenings are explicit: (i) the finite sign stabilization is not uniform in varying P,h,d; (ii) Salem failure at all biases requires the displayed radial or joint test, not merely reciprocity; (iii) positive high-bias general-unit controls do not construct near-one inputs or a fixed lower margin; (iv) the d*m/log d restriction is an EXTRA hypothesis and cannot be silently assumed for a hypothetical small-measure family; (v) a product's positive sum gives a positive constituent but does not give a uniform lower margin or cheaper physical width; (vi) original powered degree collapse does not permit replacing d by a smaller degree in norm income; (vii) no first-window E<1 theorem is invoked for these E>=2 raw packets.

<a id="biased-pair-entire-author-freeze"></a>
## Author completion and safe checkpoint

Completed at 2026-10-12T12:41.
The entire proposed fixed result is Sections1--6: exact original-degree two-orientation trace classification with computable finite thresholds and asymptotic, Salem all-ratio radial gate, precisely conditional combined angular price, actual irreducible positive all-bias control and all full costs/limits.
Root authored every new step.
No independent mathematical finding, adoption, source-proof extension, native run, formal verification or unrestricted Task completion is asserted.
A new independent whole review must check particularly the two orientations, first-difference sign/divisibility, threshold endpoints, full powered multiplicity, factor1/4, Salem real-pair absolute sign, d>=256 argument and all conditional sequence quantifiers.
Any extraction must retain this ENTIRE body including original allocation and all failed-strengthening notes.


<a id="biased-pair-rescaling-dated-correction"></a>
## Dated correction of the scaling statement

2026-10-12T12:53.
The original20:41 freeze contained the exact sentence: "For a common positive rational scalar c, the same sigma is obtained ONLY if BOTH c(a+/-b alpha^h) are nonzero actual O0 integers."
The independent original WHOLE review [R291](../audits/reviews/Yin_R_G0291_v1.md#biased-pair-original-rescaling-finding) found this ONLY IF assertion false as a claim about the algebraic surplus.
Its negative finding is preserved and is not a pass for these changed bytes.

The original control gives a precise counterexample: P=t^4+5t^2+1, a=b=1, c=1/2.
Before scaling D_+=D_-=7 and E2; after scaling the two actual values(1+/-alpha)/2 have noninteger power-basis coordinates and therefore do NOT lie in O0, although their rational norms are7/16 and E'=1/2.
Nevertheless the identical algebraic sigma=(1/4)log(7/4) remains.
Thus integrality is an admissibility requirement, not a necessary condition for homogeneity.
The active Section6 sentence now explicitly separates these two facts; all later integer-norm and q_star accounting is imposed ONLY for the admissible scaled packet.
No original theorem in Sections1--5 or finite trace/Salem conclusion changes.
The original error, exact counterexample, first freeze and negative review remain retained.
Root is the correcting author; new independent corrected-whole inspection is required.

<a id="biased-pair-newton-attribution-update"></a>
## Dated classical-formula attribution resolution

2026-10-12T12:53.
After the original whole review, the root author completed the bounded Newton-identity source follow-up.
[Mas12, printedp2 Problem7(a)](../literature/pdf/Mas12.pdf) explicitly states the general-variable elementary-symmetric/power-sum recurrence before its finite-field application.
Its coefficient convention c_j=(-1)^j sigma_j gives Section2 equation(6), valid over the present characteristic-zero field and for repeated powered roots.
Actual selected text and rendered page were inspected; the [source account](../audits/literature/Mas12/readme.md#newton-identity-selected-attribution) records institutional authorship, course2012, access limits, and exact attribution-only scope.
The local formal-series proof remains the mathematical argument.
No uninspected external solution, historical-original proof, priority claim or new mathematical assumption is imported.
L10's earlier unresolved-source history is not changed.

This corrected entire body, original history, new source scope and all formula/quantifier obligations now form the actual next whole-review target.
There has been no native mathematical run or fixed Claim extraction at this checkpoint.
