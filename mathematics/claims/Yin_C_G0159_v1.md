---
author: Yin
---
# Refined square-root angular moments and the actual cubic Fourier expense

Human author Yin.
The cross_term_reuse agent supplied the coarse angular calculation and actual weighted-cubic application; root supplied the sharper lower-degree-endpoint substitution and its monotonicity argument.
Both are contributors and neither can independently review this complete account.
The new argument was developed in D39 under the continuing G0001 authority.
Only accepted mathematical and source inputs are used.
The external discovery-only frontier remains in D39 and supplies no premise here.
No numerical program, new integration or parameter scan is used.

## Statement

Let alpha be a nontorsion algebraic integer unit of original degree d and total logarithmic Mahler measure m>0.
Write all d original conjugates as alpha_i=r_i z_i with |z_i|=1, counted with their complete original multiplicity.
For 0<u<=exp(-40), put

    ell=log(1/u),
    A(ell)=ell-log2400-3log ell,
    B(u)=2400u ell^3 A(ell),
    e_ref(u)=min{1,15sqrt(B(u))+4u},
    e_coarse(u)=min{1,735sqrt(u)ell^2+4u}.               (1)

Then A(ell)>ell/2>=20, both envelopes are increasing and tend to zero at zero, and e_ref<=e_coarse.
For every nonzero integer n with u_n=|n|m/d<=exp(-40),

    |(1/d)sum_(i=1)^d z_i^n|<=e_ref(u_n).               (2)

Consequently e_ref(Tm/d) bounds every frequency 0<|n|<=T whenever T>=1 and 0<Tm/d<=exp(-40).
No preserved powered degree, reciprocity or total-real-field assumption is required.
The comparison O(sqrt(u)log(1/u)^2) improves the small-parameter exponent of the accepted L229 envelope O(u^(1/4)sqrt(log(1/u))), without asserting pointwise dominance over that older envelope on the entire common domain.
Their minimum may be used on that domain.

For every real Laurent polynomial G(z)=sum_(|n|<=L)c_n z^n with L>=1 and 0<Lm/d<=exp(-40), let nu_P=d^(-1)sum_i delta_(z_i) and let mu be normalized circle Haar measure.
Then

    |integral G dnu_P-integral G dmu|
      <=sum_(0<|n|<=L)|c_n|e_ref(|n|m/d)
      <=e_ref(Lm/d)sum_(n!=0)|c_n|.                    (3)

In particular take the accepted C158 cubic G_3 for the actual N=2d residual projection, with any valid integer frequency bound 1<=L<=3(2d-1), and put gamma=log(4/3).
On the same small-height domain,

    sum_(0<|n|<=L)|G3hat(n)|e_ref(|n|m/d)
       >=gamma-4m log2-1/16.                           (4)

If an actual proposed input class had the reverse strict upper bound on this weighted sum, that class could contain no input in the declared domain.
No such class or automatic coefficient-budget bound is supplied here.
C145's necessary moving-test expense and C158's large-measure all-input obstruction remain consistent with (4).

The left sides in (2)--(3) are angular moments and angular discrepancies.
They are not the complete cyclic logarithmic norms bounded by C147v4.
This result alone changes neither C146v4's Frobenius-class escape nor its logarithmic power5, and supplies no new C147 cyclic-norm version or k^(-3)(log k)^(-4) supplied-class gap.
The unrestricted G0001 objective remains open.

<a id="argument"></a>
## 1. Actual powered degree and the accepted interfaces

It is enough initially to take n>=1 and beta=alpha^n.
Beta is again a nontorsion algebraic integer unit; write N=[Q(beta):Q] for its ACTUAL degree and u=h(beta)=nm/d.
The height here is the absolute Weil height of beta, equal to the stated normalized original total measure.
Each distinct conjugate beta_j occurs exactly d/N times in the original list alpha_i^n.
Therefore

    (1/d)sum_i z_i^n=(1/N)sum_(j=1)^N beta_j/|beta_j|.  (5)

No original multiplicity or possible degree drop is removed.

The accepted [C147v4 degree inversion](Yin_C_G0147_v4.md#quantitative-actual-degree-inversion), equation(5) there, applies to this actual nontorsion unit and exact height u<=exp(-40), and gives

    1/N<=2400u[log(1/u)]^3.                            (6)

Its quantitative Dobrowolski input, numerical conversion and source proof-reading boundaries remain those of that accepted argument.
The separately accepted [C267 house consequence](Yin_C_G0267_v1.md#degree-only-primitive-escape) gives u>=c/N^2 with c=log2/4>1/8.
Hence N>=sqrt(c/u)>exp(20)/sqrt8>55 on the declared domain.
For the final elementary comparison, exp(20)>2^20 and sqrt8<3 suffice.
Thus the actual monic minimal polynomial of beta meets Pri11's degree condition.

[Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) accepts the finite source statement that a globally A_0-Lipschitz real test supported in the radius-R_0 disk has discrepancy at most

    A_0(2R_0+1)sqrt(max(log N/N,u))

for the actual N>=55 simple integer-polynomial conjugates of beta.
The source theorem is used at that accepted statement/applicability scope, without a new full source-proof audit.
The compact cosine specialization below is the already retained [L229 interface](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence); only its degree price is changed here.

## 2. The sharper lower-degree endpoint

Put ell=log(1/u)>=40 and

    L_u=1/(2400u ell^3),    log L_u=A(ell).

First A(ell)>ell/2>=20.
At ell=40 this is equivalent to

    exp(20)>2400*40^3=153600000.

The positive factorial series gives exp(1)>8/3.
Since (8/3)^6>350 and (8/3)^2>7, exp(20)>350^3*7>153600000.
The derivative of A(ell)-ell/2 is 1/2-3/ell>0 on ell>=40, proving the claim throughout the domain.
In particular L_u>exp(1), and (6) says N>=L_u.
Because log x/x decreases for x>=exp(1),

    log N/N<=log L_u/L_u
             =2400u ell^3 A(ell)=B(u).                (7)

The same B(u) dominates u, since 2400ell^3 A(ell)>1.
This proves max(log N/N,u)<=B(u), with no unproved assumption log N<=ell.
The inversion is applied at EXACT u=nm/d before any subsequent monotonicity comparison.

For the coarser envelope, A(ell)<ell immediately yields B(u)<2400u ell^4.
For completeness the original two-case calculation gives the same coarse bound directly: if N>=1/u then log N/N<=u ell by monotonicity of log x/x, whereas if N<1/u then log N<ell and (6) gives log N/N<=2400u ell^4.
That upper bound on log N is used only in its valid second branch.
Both cases also dominate u.

## 3. Compact angular test with all radial and phase costs

Let q(z)=z/max(1,|z|), and let chi(z) be 1 for |z|<=1, 2-|z| for 1<=|z|<=2, and 0 beyond radius 2.
For real theta put

    phi_theta(z)=chi(z) Re(exp(-i theta)q(z)).

The map q has modulus at most1 and global Lipschitz constant at most2: the numerator and normalized-denominator differences each cost at most |z-w|.
The cutoff chi has range [0,1] and Lipschitz constant1, so phi_theta is globally 3-Lipschitz and supported in the radius-2 disk.
On the circle it is cos(arg z-theta), with normalized Haar mean zero.
Thus Pri11 supplies the precise constant 3(2*2+1)=15.

For nonzero z with radius r, the difference from cos(arg z-theta) is at most 2|log r|.
Indeed for r<=1 the loss is at most1-r<=-log r; for1<=r<=2 it is at most r-1<=2log r; and for r>=2 it is at most1<=2log r.
The unit identity gives (1/N)sum_j |log|beta_j||=2u, so the full radial correction is at most4u.
Equations (5)--(7) now yield

    |(1/d)sum_i cos(n arg z_i-theta)|
       <=15sqrt(B(u))+4u.

This is uniform in theta.
Choose theta to equal the argument of the complex angular mean (the zero mean needs no choice) to obtain its modulus.
Together with the trivial modulus bound1, this proves (2) for n>0.
For n<0, the angular mean is the complex conjugate of the mean at |n|, giving exactly the same bound without applying a height formula to a different object.

Since 15^2*2400=540000<735^2, the coarse radicand bound proves e_ref<=e_coarse.
All phases, the support-radius convention, source constant and complete d/N multiplicity have been retained.

## 4. Monotonicity and finite Fourier transfer

As a function of ell,

    B(u)=2400exp(-ell)ell^3 A(ell),
    (d/dell)log B=-1+3/ell+(1-3/ell)/A(ell)
                  <-1+5/ell<0.

Since ell decreases when u increases, B and e_ref are increasing on 0<u<=exp(-40).
They tend to zero at zero.
The derivative of sqrt(u)ell^2 is u^(-1/2)[ell^2/2-2ell]>0 on this domain, so e_coarse is increasing as well.
Adding4u and taking the minimum with1 preserve these assertions.

The accepted L229 angular envelope is also valid here because exp(-40)<(log2/4)exp(-20), its original cutoff.
Its minimum with e_ref is therefore a legitimate optional improvement.
No specific ordering between the old and new envelopes throughout the common domain is asserted.
Their stated asymptotic comparison follows from the positive extra power u^(1/4) dominating any fixed logarithmic power.

For a finite Laurent G, Haar integration removes every nonconstant monomial and integration against nu_P evaluates its corresponding original angular mean.
The constant coefficient cancels exactly.
Applying the triangle inequality, then (2) at each actual frequency and finally monotonicity, proves (3).
There is no infinite-series interchange or coefficient-height assumption in this finite step.

<a id="actual-weighted-cubic-test"></a>
## 5. Accepted cubic setup and the exact necessary coefficient expense

[C158's actual whole-reviewed decision](Yin_C_G0158_v1.md#decision-whole-reviewed-2026-10-18), selecting [R380](../audits/reviews/Yin_R_G0380_v1.md#projection-log-whole-independent-finding), has now been read.
Its accepted setup uses the actual N=2d residual kernel k, with h=log(1+k), gamma=log(4/3), and

    G_3=log2-v/2-v^2/8-v^3/24,    v=1-k.

It supplies the valid frequency bound3(2d-1), exact original valueslog2 and uniform error0<=G_3-h<=1/32.
These are accepted inputs, not a silently assumed pending C158 candidate.
The different variable v avoids confusing this polynomial argument with the height u used above.

The accepted [C145 contact estimate](Yin_C_G0145_v1.md#logarithmic-contact-discrepancy) for this SAME h gives

    integral h dnu_P-integral h dmu
       >=gamma-(log2)D_N(P),
    D_N(P)<=2(2d-1)m/d<=4m.

Replacing both integrals by those of G_3 costs at most2/32=1/16, hence

    integral G_3 dnu_P-integral G_3 dmu
       >=gamma-4m log2-1/16.                          (8)

Using the one-sided approximation could improve that replacement loss, but the stated safe bound is sufficient and is what (4) uses.
Under 0<Lm/d<=exp(-40), (3) bounds the absolute value of the same discrepancy by its actual frequency-weighted sum.
The discrepancy itself is at most its absolute value, so (8) proves (4), even if its right side is nonpositive.

The first weighted sum in (3) retains low-frequency concentration that a uniform worst-frequency bound may lose.
Neither expression is asserted small for arbitrary residual cubic coefficients.
An actual class satisfying a strict upper bound below (8) would produce a contradiction, but finding such an arithmetic class or proving its general coverage remains unresolved.
No input coefficients, class or finite example were evaluated in this argument.

<a id="angular-cyclic-separation"></a>
## 6. The separate cyclic-norm boundary and fixed scope

The angular left side of (2) differs from log|Norm(beta^n-1)| divided by the original degree.
C147v4's 86sqrt(u)log(1/u)^(5/2) is a bound for that CYCLIC LOG NORM, not an alternative upper bound to combine with e_ref in a minimum.
The retained mathematical correction is that an additional fully paid logarithmic summation or regularization argument is required to turn angular moments into a cyclic logarithmic-norm estimate.

This fixed result is consequently a new angular Claim, not a revision of the C147 cyclic theorem.
It does not improve C146v4's logarithmic power5 or justify the proposed power4 supplied-class gap by substitution.
Any independently developed improvement using a different source factor or logarithmic argument must have its own correct left side, full costs and actual review.
All previous C146/C147 physical versions and accepted scopes remain unchanged.

## Author check and contribution boundaries

Root and cross_term_reuse checked the complete strengthened candidate before this fixed registration.
The checks covered the exact own-field height and d/N multiplicity, every original root and negative frequency, the actual N>=55 source gate, both the sharper endpoint and preserved coarse split, A(ell)>ell/2 without numerical evaluation, radicand and monotonicity signs, the compact-test constant15 and radial4u, cancellation of the finite Fourier constant, actual adopted C158 setup and the safe two-integral approximation loss.
This is author checking, not independent acceptance.
The existing source proof-reading limits of C147v4, L80 and Pri11-U001 remain unchanged.

The external frontier screen did not supply a new premise.
D39 retains its discovery-only source identities, inspected passages and limitations separately rather than copying them into this proof.
Root supplied the refined lower-endpoint calculation; cross_term_reuse supplied the coarse envelope, source-interface application and weighted-cubic deduction.
Both are authors and neither can independently whole-review the result.
No numerical program, mathematical experiment, source acquisition or general-input coefficient-budget claim is made.

## Current assessment
[Selected decision](#decision-current-degree-bound-proof-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T10:27 |
| status | open |
| reason | Register the complete refined angular envelope and actual weighted-cubic expense for fresh whole review, preserving original powered degrees, source gates and the explicit separation from cyclic logarithmic norms. No acceptance or unrestricted gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete angular statement](#statement) | Every original nontorsion integer unit, every nonzero frequency in the declared height domain, finite Fourier transfer and actual cubic necessary budget. |
| argument | [Complete local proof](#argument) | Sections1--6, refined/coarse estimates, all original multiplicities, radial/source costs, monotonicity, accepted cubic application and corrected cyclic boundary. |
| dependency | [Accepted actual-degree inversion](Yin_C_G0147_v4.md#quantitative-actual-degree-inversion) | Only1/N<=2400u log(1/u)^3 at exact own-field height u<=exp(-40), with its accepted quantitative-source boundaries; no cyclic bound is substituted. |
| dependency | [Accepted house consequence](../ledger/Yin_L_G0080_v1.md#degree-only-primitive-escape) | The boundu>=c/N^2, c=log2/4>1/8, to ensure the ACTUAL source degree threshold N>=55. |
| dependency | [Finite compact Lipschitz discrepancy](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Exact source constant A_0(2R_0+1), support radius and max(log N/N,u) normalization for the actual simple integer minimal polynomial. |
| dependency | [Existing angular test and envelope](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Original cosine construction, complete powered multiplicity and old increasing envelope for the optional minimum/comparison. |
| dependency | [Accepted cubic and projection setup](Yin_C_G0158_v1.md#statement) | Actual N=2d kernel, G_3 coefficients, true frequency upper bound, exact original values and uniform1/32 approximation error; adopted by its actual whole-reviewed decision/R380. |
| dependency | [Accepted logarithmic contact estimate](Yin_C_G0145_v1.md#logarithmic-contact-discrepancy) | Delta=1 discrepancy and D_N<=4m on this exact kernel, retaining its original-angular rather than full-root meaning. |

### Decision whole-reviewed-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T10:35 |
| status | proved |
| reason | Adopt the complete refined/coarse angular-moment envelopes, exact finite Fourier transfer and actual cubic necessary budget after whole R382 review. The left side is an angular moment, not the complete cyclic logarithmic norm; no Frobenius consumer or automatic coefficient budget is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete angular statement](#statement) | Every original nontorsion integer unit, every nonzero frequency in the declared height domain, finite Fourier transfer and actual cubic necessary budget. |
| argument | [Complete local proof](#argument) | Sections1--6, refined/coarse estimates, all original multiplicities, radial/source costs, monotonicity, accepted cubic application and corrected cyclic boundary. |
| dependency | [Accepted actual-degree inversion](Yin_C_G0147_v4.md#quantitative-actual-degree-inversion) | Only1/N<=2400u log(1/u)^3 at exact own-field height u<=exp(-40), with its accepted quantitative-source boundaries; no cyclic bound is substituted. |
| dependency | [Accepted house consequence](../ledger/Yin_L_G0080_v1.md#degree-only-primitive-escape) | The boundu>=c/N^2, c=log2/4>1/8, to ensure the ACTUAL source degree threshold N>=55. |
| dependency | [Finite compact Lipschitz discrepancy](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Exact source constant A_0(2R_0+1), support radius and max(log N/N,u) normalization for the actual simple integer minimal polynomial. |
| dependency | [Existing angular test and envelope](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Original cosine construction, complete powered multiplicity and old increasing envelope for the optional minimum/comparison. |
| dependency | [Accepted cubic and projection setup](Yin_C_G0158_v1.md#statement) | Actual N=2d kernel, G_3 coefficients, true frequency upper bound, exact original values and uniform1/32 approximation error; adopted by its actual whole-reviewed decision/R380. |
| dependency | [Accepted logarithmic contact estimate](Yin_C_G0145_v1.md#logarithmic-contact-discrepancy) | Delta=1 discrepancy and D_N<=4m on this exact kernel, retaining its original-angular rather than full-root meaning. |
| review | [Whole finding](../audits/reviews/Yin_R_G0382_v1.md#refined-angular-whole-independent-finding) | Complete angular statement and proof, all six input interfaces, actual powered multiplicities, source constants and radial cost, monotone endpoint and weighted cubic scope. |

### Decision current-degree-bound-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:25 |
| status | proved |
| reason | Locate only the already used original accepted house-to-degree consequence at its complete retained C267 home. Its exact Dim19-v1 statement scope, degree/measure normalization and every existing support/dependency scope are unchanged; no primitive-exponent result is newly imported. This routine locating adoption preserves current mathematical status, every other relation and all original dated decisions/fixed R inputs, and asserts no new independent review or source-proof audit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every original nontorsion integer unit, every nonzero frequency in the declared height domain, finite Fourier transfer and actual cubic necessary budget. |
| argument | [Argument](#argument) | Sections1--6, refined/coarse estimates, all original multiplicities, radial/source costs, monotonicity, accepted cubic application and corrected cyclic boundary. |
| dependency | [Dependency](Yin_C_G0147_v4.md#quantitative-actual-degree-inversion) | Only1/N<=2400u log(1/u)^3 at exact own-field height u<=exp(-40), with its accepted quantitative-source boundaries; no cyclic bound is substituted. |
| dependency | [Dependency](Yin_C_G0267_v1.md#degree-only-primitive-escape) | The boundu>=c/N^2, c=log2/4>1/8, to ensure the ACTUAL source degree threshold N>=55. |
| dependency | [Dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Exact source constant A_0(2R_0+1), support radius and max(log N/N,u) normalization for the actual simple integer minimal polynomial. |
| dependency | [Dependency](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Original cosine construction, complete powered multiplicity and old increasing envelope for the optional minimum/comparison. |
| dependency | [Dependency](Yin_C_G0158_v1.md#statement) | Actual N=2d kernel, G_3 coefficients, true frequency upper bound, exact original values and uniform1/32 approximation error; adopted by its actual whole-reviewed decision/R380. |
| dependency | [Dependency](Yin_C_G0145_v1.md#logarithmic-contact-discrepancy) | Delta=1 discrepancy and D_N<=4m on this exact kernel, retaining its original-angular rather than full-root meaning. |
| review | [Review](../audits/reviews/Yin_R_G0382_v1.md#refined-angular-whole-independent-finding) | Complete angular statement and proof, all six input interfaces, actual powered multiplicities, source constants and radial cost, monotone endpoint and weighted cubic scope. |
