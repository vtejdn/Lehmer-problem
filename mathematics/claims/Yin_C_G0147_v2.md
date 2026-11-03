---
author: Yin
---
# Direct planar energy for complete cyclic norms

Date: 2026-10-15T13:37.
Human author Yin.
Root authors this new F-inspired inquiry under the continuing G0001 goal, in parallel with the separate algebraic coverage inquiry and the already assigned sixth-power class combination.
Root is a proof contributor and cannot independently review this account.
The responsible question is whether the direct Dirichlet-energy discrepancy, rather than a termwise Fourier/Lipschitz estimate, improves the universal actual-height cyclic expense without new arithmetic coverage assumptions.

## Reuse and the changed source interface

Root read the complete [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001), [Pri11 initial energy reading](../audits/literature/Pri11/readme.md#pri11-actual-product-energy), [L168 original compact truncation](../ledger/Yin_L_G0168_v1.md#general-unit-actual-product-cost), [L209 modulus](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus), and the currently adopted [C147](Yin_C_G0147_v1.md#decision-whole-reviewed-2026-10-15).
The exact local search for Theorem4.2/(4.16) and Dirichlet integral found the old L167 attribution and no adopted direct general-unit energy application.
Its complete relevant comparison is still to be read before any final novelty/scope claim.

The retained Pri11 arXiv1307.5734v1, printed/PDF pp.14--16, has been text-read in this turn.
Its Theorem4.2 is broader than the Theorem3.1 currently selected by U001; the existing readme explicitly did NOT adopt it.
A new source unit with exact statement, hypotheses and inspection limits is required before treating it as a resolved input.
The source theorem may be used at accepted statement/applicability scope; no new full external proof audit is claimed.

## Concrete candidate to verify

For beta=alpha^n of actual degree N and height h=nm/d, retain L168's normalized chord u(z)=abs(1-z)/max(1,abs z), truncation f_T=log max(u,exp(-T)), and compact test phi=chi_R f_T.
L168 already gives the full-original norm reduction, finite circle mean, global Lipschitz constant and one-sided exterior error.
The new target is a direct bound on the planar Dirichlet integral D[phi] of order T+1 rather than bounding it by support area times the square of the global Lipschitz constant.

Proposed parameters are ell=log(1/h), T=ell/4, R=exp(T), and source circular regularization radius epsilon=h.
If D[phi] is O(T+1), the accepted house bound N>=sqrt(c/h), c=log2/4, would control the source radicand 2h- log(abs disc(P_beta))/N^2+ell/N+4h.
The candidate universal result is O(h^(1/4)log(1/h)).
Its exact constants, all parameter domains, a.e. derivative conditions and compact support must be proved.
No such bound is yet asserted as established.

The proposed energy calculation separates the disk abs z<=1, the exterior disk using inversion z->1/conjugate(z), and the cutoff annulus.
Every useful failure will remain here.
No new native mathematical program or J is planned; PDF renders are disposable source-inspection byproducts only.
C147 and every earlier fixed proof remain unchanged.
This route supplies at most a sharper upper expense, not positive norm income or an unrestricted Mahler gap.

<a id="statement"></a>
## Statement of the developed direct-energy estimate

Let alpha be any nontorsion algebraic integer unit of ORIGINAL degree d, with total m=log M(P_alpha)>0.
Let n>=1 be an integer, beta=alpha^n, N=[Q(beta):Q] the ACTUAL powered degree, h=nm/d, and C_n=abs Norm_(Q(alpha)/Q)(alpha^n-1).
Then C_n is a positive nonzero integer.
For ALL T>=1, R>=2 and epsilon>0,

    log C_n/d <= h+exp(-T)/2+1/R
          +(3exp(T)+T/R)epsilon
          +sqrt((4T+7)(2h-log(epsilon)/N+4epsilon)).      (1)

In particular, with the accepted house constant c=log2/4, every0<h<=exp(-40) satisfies the universal upper bound

    0<=log C_n/d<=4 h^(1/4)log(1/h).                     (2)

The displayed modulus is increasing on this domain and tends to zero.
This conclusion retains every original conjugate and arbitrary powered-degree drops, with no Salem, reciprocity, good-prime or bounded-height-coefficient restriction.
It supplies an upper norm expense, not any positive local income.
No optimality or unconditional Mahler gap is asserted.

The new source input is [Pri11-U002](../audits/literature/Pri11/Yin_U002.md#pri11-u002), accepted only for compact GLOBALLY LIPSCHITZ real tests with finite Dirichlet integral.
The full source theorem's more general continuity/a.e.-derivative wording is not imported without that restriction.
The actual project test below meets the stronger regularity.

<a id="argument"></a>
## Complete argument

<a id="normalized-chord-energy-calculation"></a>
## 1. Exact planar energy of the normalized truncated logarithm

The exact original-norm reduction and compact-test definitions are the adopted [L168 Section1--2](../ledger/Yin_L_G0168_v1.md#general-unit-actual-product-cost).
In the actual powered field,

    log C_n/d=(1/N)sum_(j=1)^N log abs(1-beta_j),
    h=(1/N)sum_j log max(1,abs beta_j),                  (3)

because each beta_j occurs d/N times among the original powered conjugates.
All factors are nonzero by nontorsion.
Define on the entire complex plane

    u(z)=abs(1-z)/max(1,abs z),
    f_T(z)=log max(u(z),exp(-T)), T>=1.

L168 proves0<=u<=2, u globally3-Lipschitz and f_T globally3exp(T)-Lipschitz, with -T<=f_T<=log2 and hence abs(f_T)<=T.
These are original global test bounds, not estimates only on a disk or circle.

For abs z<1, f_T(z)=g_T(z):=max(log abs(1-z),-T).
Away from the circle abs(1-z)=exp(-T), which has area zero, its gradient has magnitude0 in the flattened disk and1/abs(1-z) outside it.
Thus

    integral_(abs z<1) abs(grad f_T)^2 dA
       <= integral_(exp(-T)<abs(z-1)<2) abs(z-1)^(-2)dA
       =2pi(T+log2).                                    (4)

This is a polar-coordinate integral centered at1; the larger annulus is used only for an upper bound.

For abs z>1 put w=I(z)=1/conjugate(z)=z/abs(z)^2.
Directly,

    u(z)=abs(1-w), f_T(z)=g_T(I(z)).
    
In real coordinates I(x)=x/abs(x)^2.
Its derivative is
abs(x)^(-2)[Id-2x x^t/abs(x)^2], where the bracket is an orthogonal reflection.
Hence

    DI(x)^t DI(x)=abs(x)^(-4)Id,
    abs det DI(x)=abs(x)^(-4).

The gradient-square factor and the Jacobian therefore cancel in the change of variables from the exterior disk to0<abs w<1.
This proves, directly rather than by an unpriced regularity assertion,

    integral_(abs z>1) abs(grad f_T)^2 dA
       = integral_(0<abs w<1) abs(grad g_T)^2 dA
       <=2pi(T+log2).

Together with(4), and ignoring only the boundary circle of area zero,

    D[f_T]<=4pi(T+log2).                                (5)

The function f_T itself is not compactly supported; (5) alone does NOT authorize inserting it in Pri11.
Compactness is supplied in the next step.
Its global Lipschitz property makes the a.e. chain rule and integrals above legitimate; the finitely many separating curves introduce no jump in the function.

<a id="compact-cutoff-energy-cost"></a>
## 2. Cutoff annulus, global continuity and one-sided norm control

Let chi_R be the L168 radial cutoff:1 on abs z<=R, linearly decreasing to0 on R<=abs z<=2R, and0 outside; R>=2.
Put phi=chi_R f_T.
It is real, continuous, compactly supported and globally Lipschitz, with

    Lip(phi)<=3exp(T)+T/R.                              (6)

At a.e. point the product gradient and (a+b)^2<=2a^2+2b^2 give

    D[phi]<=2D[f_T]
       +2 integral_(R<=abs z<=2R) f_T^2 abs(grad chi_R)^2 dA.

On that annulus, the reverse triangle inequality gives
1-1/abs z<=u(z)<=1+1/abs z.
Consequently
abs(log u(z))<=-log(1-1/abs z)<=2/abs z<=2/R.
Also log u(z)>=-log2>-1>=-T, so f_T=log u there; the truncation does not change this annulus estimate.
Since abs(grad chi_R)<=1/R and the annular area is3pi R^2,

    D[phi]<=8pi(T+log2)+24pi/R^2,
    D[phi]/(2pi)<=4T+7.                                 (7)

The final inequality uses log2<1 and R>=2.
In particular the cost is linear in T, even when R grows.
It is NOT estimated by the whole support area times the square of the global Lipschitz constant.

The unchanged L168 one-sided majorization, with f(z)=log u(z), is

    f(z)<=phi(z)+1/R,
    integral phi dmu<=exp(-T)/2,                        (8)

where mu is circle probability.
Its exact proof was reread: inside R, f<=f_T; outside R, if f_T<=0 multiplying by chi_R increases it, while if f_T>0 then f_T=f and the lost positive portion is at most log(1+1/abs z)<=1/R.
On the circle chi_R=1, the mean of f is0 and its flattened part contributes at most exp(-T)/2 by the elementary chord lower bound.
These facts hold for all the present T,R, including the eventual growing choice.
No exterior conjugate is removed.

<a id="direct-pri11-energy-application"></a>
## 3. Applying the actual source to the actual powered polynomial

Apply [Pri11-U002](../audits/literature/Pri11/Yin_U002.md#pri11-u002) to the monic irreducible minimal polynomial of beta, of actual degree N.
It has simple integral zeros, nonzero integer discriminant with absolute value at least1, and log M=N h.
The test phi in Section2 is compact and globally Lipschitz with the proved finite energy(7).
Its global modulus satisfies omega_phi(epsilon)<=Lip(phi)*epsilon for every epsilon>0.

Dropping only the NONPOSITIVE discriminant term in the source upper radicand yields

    abs((1/N)sum_j phi(beta_j)-integral phi dmu)
      <=(3exp(T)+T/R)epsilon
           +sqrt((4T+7)(2h-log(epsilon)/N+4epsilon)).    (9)

This is the direct Theorem4.2 interface, not U001's larger support-area Lipschitz upper estimate.
No N>=55 premise is needed for this source statement.
The simplified radicand is nonnegative: the actual source radicand bounds a nonnegative energy and the removed term is nonpositive; alternatively4epsilon-log(epsilon)/N has a positive minimum for every N>=1.

Equations(3), (8) and (9) prove(1).
This keeps the original norm normalized by d, through the exact d/N embedding multiplicity in(3).
No claim that alpha^n preserves degree, no conditional independence of its roots and no finite-source frequency extrapolation enters.

<a id="explicit-quarter-power-modulus"></a>
## 4. Explicit small-height parameters and constants

Assume0<h<=exp(-40) and put ell=log(1/h)>=40.
Choose

    T=ell/4, R=exp(T)=h^(-1/4), epsilon=h.              (10)

Then T>=10>=1 and R>=exp(10)>2, so every previous finite inequality applies.
These are real analytic test parameters, not arithmetic denominators or auxiliary norm incomes.

Use the SAME accepted Dim19-v1 house interface as L209, at [Smy08-U001's exact subsection](../audits/literature/Smy08/Yin_U001.md#smy08-house).
The actual powered unit beta is nontorsion and has degree N>=2, and the house bound gives

    log M(P_beta)>=c/N, h>=c/N^2,
    1/N<=sqrt(h/c)<3sqrt(h), c=log2/4>1/8.             (11)

No later source edition or stronger degree lower bound is introduced.
The last strict inequality follows from1/sqrt(c)<sqrt8<3.

The two factors inside the energy square root of(1) obey

    4T+7=ell+7<=2ell,
    2h-log(epsilon)/N+4epsilon
        =6h+ell/N
        <=6h+3ell sqrt(h)<=4ell sqrt(h).              (12)

For the last comparison,6sqrt(h)<=6<ell.
Therefore the square-root term is at most sqrt8 ell h^(1/4)<3ell h^(1/4).

All remaining terms in(1) sum to

    h+(3/2)h^(1/4)+3h^(3/4)+(ell/4)h^(5/4)
       <=(11/2+ell/4)h^(1/4)
       <=ell h^(1/4),                                (13)

using0<h<1 and ell>=40.
This proves(2), with the conservative constant4.
Every contribution in(13) comes from the original normalization, circle truncation, exterior cutoff and global continuity modulus; none is omitted.

The derivative of h^(1/4)log(1/h) is h^(-3/4)[log(1/h)/4-1], positive on the entire stated domain, and its limit at0 is0.
Integrality gives the lower bound0 in(2).
The theorem permits C_n=1; torsion, n=0 and h=0 are outside its declared domain.

<a id="direct-energy-comparison-and-source-boundary"></a>
## 5. Earlier mechanisms, precise gain and unresolved arithmetic

The earlier [L167 Salem energy proof](../ledger/Yin_L_G0167_v1.md#actual-powered-salem-discriminant-energy) was read in full.
It is a self-contained circle/discriminant calculation that separates exactly two off-circle conjugates, proves powered-degree preservation and keeps the diagonal regularization term.
It uses Pri11 for method attribution, not direct adoption.
The present all-unit planar test has different hypotheses and directly adopts the newly checked U002 theorem; L167's historical proof and source boundary remain unchanged.

L168 already owns the normalized chord, compact cutoff, circle truncation and one-sided exterior comparison.
This account reuses those facts explicitly.
The NEW local proof is the linear-in-T global Dirichlet integral, its exact cutoff annulus cost and the fully paid direct energy substitution with parameter choice(10).
The inversion energy calculation is supplied above by its actual derivative and Jacobian.
No general potential-theory novelty is claimed.

On the common small-height domain, C147 still gives B h^(1/5)log^(2/5)(1/h), B=75c^(-1/4)+9.
The ratio of the NEW displayed upper modulus to that one is exactly

    (4/B) h^(1/20)log^(3/5)(1/h) ->0.                (14)

This is an asymptotic improvement for the same complete cyclic norm, not an assertion of pointwise dominance at every finite parameter or an optimal exponent.
The minimum of the two valid bounds remains available.
No C146 class-escape consequence is proved or used in this inquiry.

The source unit U002 owns the actual current statement/visual inspection and the globally Lipschitz restriction.
Its printed potential-theory proof was read for the mechanism, with its foundational energy identity retained as an external input; it was not independently reproduced in full.
The source has no simple N>=55 restriction here; that belongs to U001 and must not be imported or used to disguise an actual-degree substitution.
The house theorem remains at its old accepted statement/application scope.
Root is the sole contributor to the new local calculations and cannot independently whole-review them.

This is a positive analytic improvement, but it provides no automatic local lower norm income.
In particular making an upper expense tend to zero does not by itself contradict the integer norm floor1, whose normalized logarithm is0.
The separate algebraic coverage inquiry must still produce positive original income or another mechanism.
G0001 remains unrestricted and unresolved.

<a id="planar-energy-entire-author-freeze"></a>
## 6. Entire author check and freeze

2026-10-15T13:49.
Root freezes the ENTIRE original account: responsible question and reuse history, complete Statement, Sections1--5 and all fourteen formulas, local energy and cutoff derivations, finite source application, explicit parameters, earlier comparisons and remaining arithmetic boundary.
The initial source and L167-reading obligations at opening are now resolved by the actual reading and new U002; they remain in the retained opening as development history.

Root is the sole contributor to this new local proof.
The author check reconstructed the inversion identity, actual derivative/reflection and Jacobian cancellation, interior truncated-annulus integral, continuity and a.e. chain rule on both disks, cutoff gradient inequality and annular value bound, full global Lipschitz constant, exact circle mean and one-sided exterior control.
It then checked the source's actual degree, leading scalar and negative discriminant term, every powered norm repetition, all T,R,epsilon domains, the nonnegative simplified radicand, the explicit h<=exp(-40) endpoint, inherited house-to-degree inequality, every constant in(12)--(13), monotonicity and comparison exponent(14).
No missing hypothesis was found in this author check.

A separately assigned source-only helper independently read the actual retained PDF and confirmed U002's formula, measures, leading/discriminant conventions, unrestricted positive epsilon and deliberate globally Lipschitz restriction.
That source inspection contributed no new project proof step and is NOT a whole independent review of this account.
U002's root source-inspection record and its external-proof limits remain exact.
The whole new project argument still requires separately organized noncontributor review after fixed retention.

The scoped two-file check of this D and U002 returned checked2 before freeze; it is structural evidence only.
No native mathematical computation, J, numerical integration or new external-source download was used.
The disposable PDF render is source inspection only.
This new universal modulus is naturally a substantive successor in the C147 family, preserving its older proof and actual R359.
It supplies no Frobenius-class conclusion or unrestricted G0001 completion.

## Fixed organization

Retain the complete frozen direct-energy account.
Earlier [C147v1](Yin_C_G0147_v1.md#decision-whole-reviewed-2026-10-15) and [R359](../audits/reviews/Yin_R_G0359_v1.md#frequency-weighted-cyclic-whole-independent-finding) remain fixed; their finite Fourier proof has different adopted inputs.
This successor adds a local Dirichlet-energy bound and directly adopts Pri11-U002 at its restricted source scope.
Root is its proof contributor, not its independent reviewer.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-15)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T13:50 |
| status | open |
| reason | Retain the complete direct planar-energy cyclic-norm proof with explicit all-unit actual-degree and compact-test costs. Independent whole review is pending; positive arithmetic coverage and unrestricted G0001 remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire direct-energy modulus](#statement) | Universal finite T,R,epsilon estimate and explicit4 h^(1/4)log(1/h) bound for all original nontorsion integer units and powered degrees, including monotonicity and exact limits. |
| argument | [Entire energy proof](#argument) | All six sections and fourteen formulas, actual inversion and cutoff energy, original norm and finite source application, exact parameters and all source/contribution boundaries. |
| dependency | [Original norm and compact truncation](../ledger/Yin_L_G0168_v1.md#general-unit-actual-product-cost) | Actual d/N field-norm reduction, normalized chord, global Lipschitz bounds, circle truncation and one-sided exterior estimate with every original conjugate. |
| dependency | [Direct source energy theorem](../audits/literature/Pri11/Yin_U002.md#pri11-u002) | Retained Theorem4.2/(4.16) only on compact globally Lipschitz real tests with finite Dirichlet integral, every positive regularization radius, actual discriminant and degree; recorded external-proof limits. |
| dependency | [Accepted house interface](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | ONLY the smy08-house subsection's exact retained Dim19-v1 house bound on the actual nontorsion powered polynomial, yielding h>=c/N^2; no later edition or full source-proof adoption. |
| support | [Previous complete cyclic modulus](Yin_C_G0147_v1.md#statement) | Same complete norm and powered-height comparison; its old proof and independent review remain valid, with asymptotic ratio computed locally. |
| support | [Earlier Salem circle energy](../ledger/Yin_L_G0167_v1.md#actual-powered-salem-discriminant-energy) | Reuse and method-scope comparison: exact Salem circle argument and old attribution-only Pri11 use, not an imported general-unit premise. |

### Decision whole-reviewed-2026-10-15

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T13:58 |
| status | proved |
| reason | Adopt the actual whole noncontributor review of the direct planar-energy cyclic-norm bound, including global compact-test energy, every original norm and powered-degree multiplicity, all finite parameters and restricted source interfaces. Positive arithmetic income and unrestricted G0001 remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire direct-energy modulus](#statement) | Universal finite T,R,epsilon estimate and explicit4 h^(1/4)log(1/h) bound for all original nontorsion integer units and powered degrees, including monotonicity and exact limits. |
| argument | [Entire energy proof](#argument) | All six sections and fourteen formulas, actual inversion and cutoff energy, original norm and finite source application, exact parameters and all source/contribution boundaries. |
| dependency | [Original norm and compact truncation](../ledger/Yin_L_G0168_v1.md#general-unit-actual-product-cost) | Actual d/N field-norm reduction, normalized chord, global Lipschitz bounds, circle truncation and one-sided exterior estimate with every original conjugate. |
| dependency | [Direct source energy theorem](../audits/literature/Pri11/Yin_U002.md#pri11-u002) | Retained Theorem4.2/(4.16) only on compact globally Lipschitz real tests with finite Dirichlet integral, every positive regularization radius, actual discriminant and degree; recorded external-proof limits. |
| dependency | [Accepted house interface](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | ONLY the smy08-house subsection's exact retained Dim19-v1 house bound on the actual nontorsion powered polynomial, yielding h>=c/N^2; no later edition or full source-proof adoption. |
| support | [Previous complete cyclic modulus](Yin_C_G0147_v1.md#statement) | Same complete norm and powered-height comparison; its old proof and independent review remain valid, with asymptotic ratio computed locally. |
| support | [Earlier Salem circle energy](../ledger/Yin_L_G0167_v1.md#actual-powered-salem-discriminant-energy) | Reuse and method-scope comparison: exact Salem circle argument and old attribution-only Pri11 use, not an imported general-unit premise. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0361_v1.md#planar-energy-whole-independent-finding) | Complete actual successor statement and six-section fourteen-formula proof, every selected input/support, actual source regularity and all original costs and contribution limits. |

