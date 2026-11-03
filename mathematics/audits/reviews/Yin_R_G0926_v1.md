---
author: Yin
---

# Independent whole review of the critical-width matching degree theorem

Human record author: Yin.
Review act: 2026-10-25T06:57 UTC.
This is a separately arranged isolated independent whole mathematical inspection of [C705](../../claims/Yin_C_G0705_v1.md#statement), including its complete argument and the exact necessary C704 interfaces.
The reviewing agent did not contribute to the proof or any repair.
The assignment supplied the fixed C705 and C704 paths, requested coverage and operational metadata, without proof-development dialogue, a mathematical development summary or a prior review finding.
No D40, other development material or prior R was consulted.
Initial findings were formed from the complete C705 statement and proof before reading C704's complete local argument and its current adoption decision.
The current C704 decision was read to establish its actual accepted-input scope, not as a substitute for checking the mathematics invoked by C705.
C174 equation (11) and C690's corresponding Fourier-inequality passage were also read for the exact reuse attribution.

The scope is every assertion UC1--UC8 and every zero, constant, threshold, degree and uniform-band case claimed in C705.
The C704 local proof was read in full and its consumed interfaces checked below; C704's previously accepted supporting theorems and their original literature proofs were not recursively re-audited.
There is no new computation, source acquisition, formal proof check or Task-completion finding.
This newly performed independent review is necessary evidence not already supplied by C705's author derivation, and is retained in its own fixed R under the common content decision.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole matching-degree finding](#whole-matching-degree-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole matching-degree finding](#whole-matching-degree-review) | [C705 statement](../../claims/Yin_C_G0705_v1.md#statement) | Entire UC1--UC7 statement: every finite orthogonal projection, all degenerate cases, the same actual weighted family and original circle, full Fourier norm, genuine degree, fixed-height and entire compact-height-band bounds, all thresholds and stated limits. |
| [Whole matching-degree finding](#whole-matching-degree-review) | [C705 complete argument](../../claims/Yin_C_G0705_v1.md#complete-argument) | Entire Sections 1--4 including UC8: exact projection derivative, clipping and level sets, finite-set Fourier summability and all norm-zero cases, actual width-2tau comparison, degree conversion, subtraction and uniform quantifiers. |
| [Whole matching-degree finding](#whole-matching-degree-review) | [C704 statement](../../claims/Yin_C_G0704_v1.md#statement) | Exact consumed RF2--RF7 actual family, original projection, contact law, uniform L1 comparison, epsilon and genuine degree bounds, plus RF10--RF12 constants and full lower strip; this is an accepted-input and consuming-interface review, not a new independent review of the whole recursive C704 dependency chain. |
| [Whole matching-degree finding](#whole-matching-degree-review) | [C704 complete argument](../../claims/Yin_C_G0704_v1.md#complete-argument) | All six local sections read; verify exact original-circle comparison, finite-law contact, actual degree inequalities, full strip and their applicability to C705, with C704's accepted upstream theorem and source depths retained. |
| [Whole matching-degree finding](#whole-matching-degree-review) | [C704 current accepted decision](../../claims/Yin_C_G0704_v1.md#decision-whole-reviewed-2026-10-25) | Actual proved decision dated 2026-10-25T06:55, supplying the resolved necessary input at its declared actual-family and source scopes; no prior R finding was read or reclassified. |
| [Whole matching-degree finding](#whole-matching-degree-review) | [C174 Fourier mechanism](../../claims/Yin_C_G0174_v1.md#narrow-contact-wiener-model) | Only Section 4 equation (11) and its finite-set proof, matching the fully reproduced elementary inequality; no fixed-polynomial limiting conclusion is imported. |
| [Whole matching-degree finding](#whole-matching-degree-review) | [C690 Fourier use](../../claims/Yin_C_G0690_v1.md#4-clipped-derivative-and-the-entire-fourier-sum) | Only the explicitly reproduced weighted Fourier inequality and its attribution to C174; no two-factor-family estimate is used as a premise. |
| [Whole matching-degree finding](#whole-matching-degree-review) | [C705 source and scope boundary](../../claims/Yin_C_G0705_v1.md#source-and-scope-boundary) | Exact attribution and inherited source-depth limits, publication-time open statement distinguished from C704's later actual acceptance, and no optimal-height, small-height, leading-constant, near-one or unrestricted Task conclusion. |

## Obligations and decisive evidence

### Arbitrary orthogonal projections and clipping: UC1

For the stated angular parametrization, h=||Pi v||_2^2/(2d) lies in [0,1], since an orthogonal projection is a contraction and ||v||_2^2=2d.
Differentiating gives h'=2 Re< Pi v, Pi v'>/(2d).
The bound ||v'||_2<=(2d-1)sqrt(2d) gives |h'|<=2(2d-1)sqrt(h)<=4d sqrt(h), including h=0 because Pi v then vanishes.
The reasoning uses neither a special rank nor a phase substitution.

The positive-part scalar map is Lipschitz, so f_tau is absolutely continuous for every tau>0.
Its a.e. derivative equals -h'/tau on {h<tau} and zero on {h>tau}.
For a nonconstant trigonometric h the threshold set is finite; for constant h the clipped function is constant, so the threshold-equality case has derivative zero directly.
Thus |f_tau'|<=4d tau^(-1/2) 1_{h<tau} and |f_tau|<=1_{h<tau}<=1_{h<=tau}, giving both L2 bounds without an unstated assumption tau<=1.
In particular Pi=0 gives f_tau=1, Pi=I and tau=1 give f_tau=0, and constant h=tau gives f_tau=0 although mu_tau=1.
These cases create no contradiction because the estimates are upper bounds; mu_tau=0 forces both relevant norms to vanish.

### Complete Fourier summability and constants: UC8 and UC2

For an absolutely continuous periodic g with g' in L2, the negative-exponential convention gives the derivative coefficients in*ghat(n), and Parseval gives the weighted square sum A^2+E^2/t^2.
For each finite frequency set, Cauchy--Schwarz bounds its absolute sum by the product of that square-sum bound and the square root of sum_n(1+(n/t)^2)^(-1).
The decreasing positive-tail integral gives the latter sum at most 1+pi*t for every t>0.
Increasing finite sets first proves absolute summability; it does not assume it.

If A=0, continuity and the L2 norm imply g=0; if E=0, absolute continuity makes g constant and its A norm is A.
For A,E>0, t=E/A gives sqrt(2A^2+2pi*A*E)<=sqrt(2)A+sqrt(2pi)sqrt(AE).
The same displayed UC8 bound also covers both zero cases, although the constant-function estimate is stronger.
Using UC1, A<=sqrt(mu_tau) and E<=4d tau^(-1/2)sqrt(mu_tau) imply sqrt(AE)<=2sqrt(d)tau^(-1/4)sqrt(mu_tau).
This is exactly UC2, with its stated constant 2sqrt(2pi*d), and includes the zeroth coefficient and every high-frequency coefficient created by clipping.

The inspected C174 equation (11) is the identical finite-set mechanism under t=1/epsilon, and C690 explicitly reuses it.
Their other limiting conclusions are unnecessary here because C705 gives the complete finite norm argument.

### Actual contact mass and original upper envelope: UC3 and UC4

C704 RF7 compares the original cap and F_sigma composed with the same iota_j for every positive sigma.
At sigma=2tau, the inclusion {h_orig,j<=tau} implies f_(j,2tau)>=1/2 pointwise, including equality at the threshold.
Therefore mu_(j,tau)<=2 integral f_(j,2tau)<=2 integral(F_(2tau) composed with iota_j)+2C_stab*epsilon_j.
The phase cap is bounded by its sublevel indicator, and C704 RF6 with the untranslated actual law gives that indicator mass at most 2sqrt(2tau) when 0<tau<=1/2.
This yields the coefficient 4sqrt(2tau) in UC3, and the additional bound by 1 is the ordinary probability bound.
The finite common-zero conventions in C704 have zero circle measure and do not change this argument.
No product-Haar law or independence assertion enters the contact estimate.

Dividing the resulting mass estimate by sqrt(tau), and using epsilon_j<1/M_j, gives mu_(j,tau)/sqrt(tau)<=4sqrt(2)+2C_stab*H^(-1/2).
UC2 and sqrt(mu_tau)<=1 then yield exactly UC4.
This establishes its entire Fourier-norm upper bound on the actual original projection, without a finite return window.

### Genuine degree, every actual finite index and fixed heights: UC5 and UC6

The C704 actual degree d_j=K+a_j+c_j is the degree of the retained minimal polynomial and not a raw polynomial degree or a selected-frequency count.
The same RF4 bound d_j<1024M_j^2 gives H=M_j^2*h/d_j>h/1024 and H^(-1/2)<32/sqrt(h).
For every actual j with d_j>=2h, tau=h/d_j<=1/2, so substituting this bound in UC4 gives the displayed B_h after using sqrt(2)<=sqrt(2)*sqrt(d_j).
No limiting operation is used in UC5, and h>0 is sufficient.

For h>=D_rf=1024H_rf, the same strict degree inequality gives H>H_rf.
Together with M_j>=M_rf and d_j>=64h, this puts the actual tau=h/d_j in the full C704 RF11 strip H_rf/M_j^2<=tau<=1/64.
Its lower bound is exactly C_mass*sqrt(d_j)/(2A_chi*sqrt(h))-1=a_h*sqrt(d_j)-1.
All constants are fixed at the same C704 choice of K and bump, A_chi and C_mass are positive, and a_h is positive for each finite fixed h in the stated range.
The upper bound UC5 applies simultaneously since d_j>=64h implies d_j>=2h.
If d_j>=4/a_h^2, then a_h*sqrt(d_j)>=2 and subtracting 1 loses at most half that term.
Finally a_j>(j+1)K implies M_j=floor(a_j/4) and d_j tend to infinity, so every finite threshold is eventually satisfied without any monotonicity premise.
This proves precisely the asserted square-root order for each fixed h>=D_rf.

### Entire compact height bands: UC7

For every width with h_-<=d_j*tau<=h_+, put h=d_j*tau inside the already established finite-index estimates.
The common conditions M_j>=M_rf and d_j>=64h_+ ensure the lower strip and upper-domain conditions for every such h simultaneously.
The lower coefficient a_h decreases in h, so a_h>=a_+=C_mass/(2A_chi*sqrt(h_+)).
The upper coefficient B_h also decreases in h because C_stab is positive, so B_h<=B_(h_-).
The same inequalities thus hold for every width in the closed band, including both endpoints and the singleton case h_-=h_+.
The common condition d_j>=4/a_+^2 supplies its uniform positive lower multiple.
There is no chosen grid of widths, no width-sequence monotonicity requirement and no exchange of fixed-polynomial and varying-degree limits.

## Necessary dependency and source assessment

C704 was published as open, but its current [decision-whole-reviewed-2026-10-25](../../claims/Yin_C_G0704_v1.md#decision-whole-reviewed-2026-10-25) actually selects status proved at 2026-10-25T06:55.
The necessary C704 input is therefore resolved for this review at its exact accepted scope, rather than being assumed unresolved from C705's truthful publication-time history.
The inspection independently checked that C705 uses exactly its square-prime parameters, every original relation column, original 2d window, actual-law contact and all-width L1 comparison, genuine degree bounds and complete lower strip.
C704 Sections 1--6 were read, including the finite rational interpolation, missing cyclic sample, full Gram pole, translated-law calculation, five localized costs and full-support error powers.
No incompatible family, changed constant, unverified new local extension or cycle back through C705 was found in this use.

This review accepts the upstream statements already selected by C704 at their retained inspection depths.
In particular, C708's weighted source, torsion-killer and minimality conclusions, C726's unchanged stationary-phase patch and localized square mass, and the other adopted scalar/kernel mechanisms are not presented as newly re-audited source proofs here.
C704 retains the Tao26 primary-statement/applicability scope without a full-source proof audit, and its classical Par88 attribution does not replace the finite proof actually written there.
C705 introduces no further external theorem premise beyond this resolved project input and the elementary fully displayed estimates.
The local Fourier reuse attribution was checked at the exact C174 and C690 passages.
There is no outstanding new source-identification obligation created by this consuming argument.

## Whole matching-degree review

The complete C705 argument establishes UC1--UC8 with every stated projection, zero, constant, threshold-equality, actual-index, degree and entire-band quantifier.
No mathematical defect or unresolved necessary interface was found.
With the exact currently accepted C704 input at the scope above, this finding supports adoption of the entire fixed C705 statement and complete argument.
It does not itself select or modify C705's assessment.

The conclusion is matching square-root degree growth only on the specified actual weighted family for fixed h>=D_rf and compact height bands inside that range.
The bounds establish no leading constant, optimal height threshold, conclusion for all smaller positive heights, uniform upper bound over all original polynomials, near-one family or unrestricted G0001 completion.
The positive Mahler interval log(2)<m(P_j)<log(4), original 2d window and inherited source-inspection limits remain exactly as stated.
