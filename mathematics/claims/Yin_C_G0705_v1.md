---
author: Yin
---

# Matching square-root degree growth of the actual critical-width Wiener sum

Human author Yin.
Root derived the projection derivative and contact-mass comparison below while inspecting the fixed logarithm-free C704 theorem.
This is author mathematics, not an independent review.
The weighted Fourier inequality is the elementary mechanism already written in C174 equation11 and reused in C690; it is proved again here only to fix constants and zero cases.
The new result is its complete original-projection/contact application and matching actual-degree growth, not a new abstract Sobolev inequality.
The focused reuse check distinguished earlier bounds for an unclipped projection, the two-factor fixed-width ceiling, and fixed-polynomial narrow-width limits from this varying weighted family.
No native computation or new external source is used.

## Statement

All circle integrals use Haar probability, derivatives are angular, and Fourier coefficients use negative exponentials.
For an integrable function f write ||f||_A=sum_(n in Z)|fhat(n)| and W_*(f)=sum_(n!=0)|fhat(n)|.

### Projection and contact envelope

Let d>=1 be an integer, Pi any orthogonal projection on C^(2d), and v(z)=(1,z,...,z^(2d-1))^T.
Define

    h(z)=v(z)^*Pi v(z)/(2d), f_tau=(1-h/tau)_+,
    mu_tau=Pr{h<=tau}, tau>0.

Then 0<=h<=1, f_tau is absolutely continuous with derivative in L2, and

    |h'|<=2(2d-1)sqrt(h)<=4d sqrt(h),
    ||f_tau||_2<=sqrt(mu_tau),
    ||f_tau'||_2<=4d tau^-1/2 sqrt(mu_tau),             (UC1)
    ||f_tau||_A<=sqrt(2mu_tau)
                   +2sqrt(2pi d)tau^-1/4 sqrt(mu_tau). (UC2)

The rank of Pi is unrestricted; zero, constant and threshold-equality cases are included.
The complete Fourier sum is controlled, without a finite frequency cutoff or a prior absolute-summability assumption.

### Same actual weighted family and complete critical band

Use EXACTLY C704 RF2--RF5, equivalently the adopted C678 square-prime weighted family: the same actual composite K, first prime a_j, L_j=K+a_j+2, M_j=floor(a_j/4), and c_j the least prime exceeding(L_j+1)^2.
Retain its actual monic irreducible Salem polynomial P_j, d_j=K+a_j+c_j, every d_j relation column and the original2d_j orthogonal projection.
Write h_j=h_orig,j and f_(j,tau)=(1-h_j/tau)_+.
Keep the exact fixed constants C_stab, C_mass, A_chi, H_rf, M_rf and D_rf=2^10 H_rf of C704.
In particular

    16M_j^2<d_j<2^10 M_j^2, epsilon_j<1/M_j,
    ||f_(j,sigma)-F_sigma composed with iota_j||_1
                                      <=C_stab epsilon_j
                                      for EVERY sigma>0,
    Pr{h_phase,j<=eta}<=2sqrt(eta), 0<eta<=1.

These are the literal original-family RF6--RF7 interfaces, not product-Haar replacements.

For EVERY actual j and0<tau<=1/2, set H=M_j^2tau.
Then

    mu_(j,tau)<=min{1,4sqrt(2tau)+2C_stab epsilon_j},    (UC3)
    W_*(f_(j,tau))<=||f_(j,tau)||_A
       <=sqrt2+2sqrt(2pi d_j)
                         sqrt(4sqrt2+2C_stab H^-1/2). (UC4)

For every fixed real h>0 define

    B_h=sqrt2+2sqrt(2pi)*sqrt(4sqrt2+64C_stab/sqrt(h)).

For EVERY actual j with d_j>=2h,

    W_*(f_(j,h/d_j))<=B_h sqrt(d_j).                   (UC5)

For every fixed h>=D_rf, put a_h=C_mass/(2A_chi sqrt(h))>0.
For every actual j with M_j>=M_rf and d_j>=64h,

    a_h sqrt(d_j)-1<=W_*(f_(j,h/d_j))
                                      <=B_h sqrt(d_j). (UC6)

Consequently W_*(f_(j,h/d_j)) has order sqrt(d_j) as j tends to infinity, for each such fixed h.
Explicitly its lower bound can be replaced by(a_h/2)sqrt(d_j) once also d_j>=4/a_h^2.

More generally, fix real D_rf<=h_-<=h_+<infinity and put a_+=C_mass/(2A_chi sqrt(h_+)).
For EVERY actual j with M_j>=M_rf and d_j>=64h_+, and EVERY tau with h_-<=d_j tau<=h_+,

    a_+ sqrt(d_j)-1<=W_*(f_(j,tau))
                                  <=B_(h_-) sqrt(d_j). (UC7)

The positive lower multiple a_+/2 holds uniformly in this ENTIRE band once also d_j>=4/a_+^2.
There is no restriction to a sampled width, no monotonicity condition on a width sequence, and no fixed-polynomial limit interchanged with the varying degree.

The matched order is only the degree growth in this proved critical-width regime.
It does not identify a leading constant, prove that D_rf is an optimal height threshold, settle smaller positive h, or supply a uniform upper bound for all original polynomials.
The actual log2<m(P_j)<log4 interval, full2d window and source-inspection limits of C704 remain.
There is no near-one family, characteristic-zero residual construction or unrestricted G0001 completion.

## Complete argument

### 1. The original projection derivative and all zero cases

Write v(t)=v(exp(it)).
Orthogonality gives h=||Pi v||_2^2/(2d), hence 0<=h<=||v||_2^2/(2d)=1.
The derivative is

    h'=2Re< Pi v, Pi v'>/(2d).

Cauchy--Schwarz, ||Pi||<=1 and ||v'||^2=sum_(r=0)^(2d-1)r^2<=(2d)(2d-1)^2 give |h'|<=2(2d-1)sqrt(h).
This also holds at h=0, where Pi v=0 makes the derivative zero directly.

The scalar clipping map is Lipschitz, so its composition with smooth h is absolutely continuous.
Where h<tau its derivative is -h'/tau, and where h>tau it is zero.
On a threshold level interval h=tau the derivative of h and the clipped function is zero.
More generally the standard a.e. chain rule yields the same bound on a level set; alternatively a nonconstant trigonometric h has only finitely many such level points, while a constant h is immediate.
Thus a.e.

    |f_tau'|<=4d tau^-1/2 1_(h<tau),
    |f_tau|<=1_(h<tau)<=1_(h<=tau).

Integrating proves UC1, including mu_tau=0 and any constant projection profile.
No derivative estimate for an independently sampled phase has replaced the original projection.

### 2. The complete Fourier inequality

For any absolutely continuous periodic g with g' in L2, put A=||g||_2 and E=||g'||_2.
For any t>0 and any finite set of integer Fourier frequencies, weighted Cauchy--Schwarz and Parseval give a bound by

    [sum_(n in Z)(1+(n/t)^2)^-1]^(1/2)
                 [A^2+E^2/t^2]^(1/2).

The summand is decreasing for n>=0, so comparing both tails with the positive-half-line integral gives sum_n(1+(n/t)^2)^-1<=1+pi t.
Increasing the finite frequency sets therefore proves absolute Fourier summability and

    ||g||_A<=sqrt((1+pi t)(A^2+E^2/t^2)).

If A=0 then g=0 and the conclusion is immediate.
If E=0, absolute continuity makes g constant, so ||g||_A=A.
If A,E>0, take t=E/A and use sqrt(x+y)<=sqrt(x)+sqrt(y).
In all cases this yields

    ||g||_A<=sqrt2 A+sqrt(2pi)*sqrt(AE).                (UC8)

This is the exact elementary C174 equation11 mechanism, with the parameter optimized for the present use; no new source theorem is imported.
Substituting UC1 into UC8 gives UC2 because sqrt(AE)<=2sqrt(d)tau^-1/4 sqrt(mu_tau).

### 3. Actual contact mass from the original comparison

For0<tau<=1/2, every point with h_j<=tau has f_(j,2tau)>=1/2.
All functions are nonnegative, so

    mu_(j,tau)<=2 integral f_(j,2tau)
       <=2 integral(F_(2tau) composed with iota_j)
                                      +2C_stab epsilon_j
       <=2Pr{h_phase,j<=2tau}+2C_stab epsilon_j
       <=4sqrt(2tau)+2C_stab epsilon_j.

The comparison uses the SAME actual original circle and width2tau.
Its global L1 bound is valid for every positive width, and2tau<=1 is precisely the stated domain needed for the contact law.
No coordinate independence, translated probability replacement or pointwise Gram-ratio lower bound is assumed.
Adding the trivial probability bound1 proves UC3.

Since epsilon_j<1/M_j,

    mu_(j,tau)/sqrt(tau)
                         <=4sqrt2+2C_stab/(M_j sqrt(tau))
                         =4sqrt2+2C_stab H^-1/2.

Apply UC2 and sqrt(mu)<=1 to obtain UC4.
This bounds the ENTIRE original Fourier sum, including every high-frequency coefficient introduced by clipping.

### 4. Genuine degree, matching lower bound and uniform height intervals

At tau=h/d_j, the genuine degree upper bound d_j<2^10 M_j^2 gives H=M_j^2 h/d_j>h/2^10.
Therefore H^-1/2<32/sqrt(h).
For d_j>=2h the width lies in UC4's domain, and

    ||f_(j,h/d_j)||_A
       <=sqrt2+2sqrt(2pi)*sqrt(d_j)
                                      sqrt(4sqrt2+64C_stab/sqrt(h))
       <=B_h sqrt(d_j),

where the last step uses d_j>=1.
This proves UC5 at every stated actual j.

For h>=D_rf, C704 RF4/RF11 give H>h/2^10>=H_rf.
If M_j>=M_rf and d_j>=64h, then tau=h/d_j<=1/64, so the entire fixed C704 lower strip applies to this actual original cap.
Its lower bound is exactly a_h sqrt(d_j)-1, proving UC6 together with UC5.
When d_j>=4/a_h^2 the subtractive1 costs at most half of a_h sqrt(d_j).
The actual a_j>(j+1)K implies M_j and d_j tend to infinity, so every finite threshold is eventually met; no monotonicity beyond this divergence is required.

For UC7, let h=d_j tau vary within the specified interval.
The lower threshold h>=h_->=D_rf supplies the C704 strip, while d_j>=64h_+ ensures tau<=1/64.
The coefficient a_h decreases with h, so its minimum is a_+.
The upper coefficient B_h also decreases with h, so its maximum is B_(h_-).
Both estimates therefore hold simultaneously for EVERY width in the full band, with the stated common actual-index thresholds.
The same subtraction argument supplies its uniform positive lower multiple.

## Source and scope boundary

C704 is the exact direct actual-family input for its uniform original L1 comparison, original contact law, genuine degree and full-support lower bound.
At this candidate's publication it is a fixed open theorem undergoing fresh independent whole review; this dependent result is likewise open until its necessary input and its own proof are sufficiently reviewed.
C678's source/killer/minimality and the C693 v2 stationary-phase input remain at the exact inspection depths declared in C704; they are not newly re-audited here.
UC1--UC3 and the upper-envelope argument use only the displayed finite projection algebra, a.e. clipping derivative, probability comparison and elementary complete Fourier estimate.
C174 and C690 identify the already retained Fourier mechanism; none of their fixed-polynomial or two-factor limiting conclusions is transferred to this family.
There is no new external source claim, numerical experiment or optimal-height assertion.
The order sqrt(d_j) is matched only for the actual stated family and critical-width band.
Its Mahler interval remains bounded away from zero, so this result does not settle the unrestricted Lehmer Task.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision matching-degree-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T06:53 |
| status | open |
| reason | Register the complete original projection/contact upper envelope and matching square-root-degree growth for every fixed sufficiently large critical height and every compact positive height band in the stated regime. The full Fourier sum, exact actual-law comparison, all finite degree/width endpoints and subtractive lower cost are retained. The C704 input and this dependent theorem await sufficient independent whole review; no optimal threshold, leading constant or unrestricted conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete projection and actual-band theorem](#statement) | UC1--UC7: every finite orthogonal projection and zero/constant case, actual weighted original contact/upper envelope, genuine degree normalization, full fixed-height and uniform-band matching orders, and all limitations. |
| argument | [Complete original derivative and Fourier proof](#complete-argument) | Sections1--4/UC8: exact projected-vector derivative, a.e. clipping and mass bound, complete Fourier optimization with zero cases, actual width2tau comparison, all degree thresholds and uniform quantifiers. |
| dependency | [Exact rational-comparison actual-family theorem](Yin_C_G0704_v1.md#statement) | RF2--RF7 genuine square-prime original family, all-width original L1 comparison and original contact law, plus RF10--RF12 exact lower strip/constants; its entire relevant argument is read, with publication-time open status retained. |
| support | [Existing complete Fourier inequality](Yin_C_G0174_v1.md#narrow-contact-wiener-model) | Only the elementary equation11 L2/derivative mechanism in its argument, reproduced completely here; none of its fixed-polynomial asymptotic claims is an input. |
| support | [Earlier distinct ceiling use](Yin_C_G0690_v1.md#statement) | Comparison and reuse attribution for the same weighted Fourier inequality; its two-factor family, fixed-width ceiling and other conclusions are not transferred. |
| support | [Source and scope boundary](#source-and-scope-boundary) | Actual family and original-window scope, pending dependency review at publication, inherited source depths and absence of threshold optimality or unrestricted completion. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T07:01 |
| status | proved |
| reason | Adopt the complete original-projection/contact envelope and matching critical-width square-root-degree theorem after main reading of C705 and fresh isolated whole R926. C704 is now adopted at the exact required actual-family scope. Every projection and norm-zero case, full Fourier summability, original-law width2tau comparison, genuine degree threshold, subtractive lower cost and entire compact-height-band quantifier is checked. The matched order is confined to this proved regime; no leading constant, optimal height threshold, smaller-height, near-one or unrestricted conclusion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete projection and actual-band theorem](#statement) | UC1--UC7: every finite orthogonal projection and zero/constant case, actual weighted original contact/upper envelope, genuine degree normalization, full fixed-height and uniform-band matching orders, and all limitations. |
| argument | [Complete original derivative and Fourier proof](#complete-argument) | Sections1--4/UC8: exact projected-vector derivative, a.e. clipping and mass bound, complete Fourier optimization with zero cases, actual width2tau comparison, all degree thresholds and uniform quantifiers. |
| dependency | [Exact rational-comparison actual-family theorem](Yin_C_G0704_v1.md#statement) | RF2--RF7 genuine square-prime original family, all-width original L1 comparison and original contact law, plus RF10--RF12 exact lower strip/constants; its exact required input is now resolved by the current adopted decision, while the publication-time open history remains preserved. |
| support | [Existing complete Fourier inequality](Yin_C_G0174_v1.md#narrow-contact-wiener-model) | Only the elementary equation11 L2/derivative mechanism in its argument, reproduced completely here; none of its fixed-polynomial asymptotic claims is an input. |
| support | [Earlier distinct ceiling use](Yin_C_G0690_v1.md#statement) | Comparison and reuse attribution for the same weighted Fourier inequality; its two-factor family, fixed-width ceiling and other conclusions are not transferred. |
| support | [Source and scope boundary](#source-and-scope-boundary) | Actual family and original-window scope, resolved current input versus pending review at publication, inherited source depths and absence of threshold optimality or unrestricted completion. |
| review | [Fresh independent whole matching-degree finding](../audits/reviews/Yin_R_G0926_v1.md#whole-matching-degree-review) | Entire UC1--UC8 statement and proof, all zero/constant/threshold and actual-law cases, complete Fourier sum, exact accepted C704 scope, all degree endpoints and uniform band quantifiers. |

