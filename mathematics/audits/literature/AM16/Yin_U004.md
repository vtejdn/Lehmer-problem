---
author: Yin
---
# AM16-U004: Salem subdegree coverage and the diagonal/inverse boundary

Date: 2026-10-18T11:43.
Human record author Yin.
Root proposed the off-inverse-pair subdegree specialization of the newly inspected rank-two theorem and requested a complete case split for C162.
The entropy_attainment_bridge AI supplies the exact applicability, exponent and residue-mass checks below.
Both are contributors; this is source/application acceptance and an author coverage check, not an independent review of their project proofs.
No new Claim, computation, variable-rank theorem or revision of fixed U003 is supplied.

<a id="am16-u004"></a>
## Read; accepted fixed-rank application and coverage classification

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Francesco Amoroso and David Masser, Lower bounds for the height in Galois extensions, institutional author postprint dated 3 August 2016, printed 1--5/PDF 2--6; same retained AM16--author-postprint.pdf as U001--U003.

Passages: Theorem 2.1 on printed 1--2/PDF 2--3, including the joint-degree convention and adjacent attribution, exactly as retained in U003.

Inspection: Reuse of the directly inspected fixed K=Q,r=2 statement; the present off-pair field-degree application, fixed-epsilon rearrangements and complete C162 Salem case split were checked. No original source-proof audit or new source acquisition. The separately adopted project L205 interface and its R104 review were read at their exact stated scope.


The [exact accepted rank-two input](Yin_U003.md#am16-u003) gives, for every FIXED epsilon>0, a constant C_2(epsilon)>0 independent of the multiplicatively independent nonzero algebraic numbers x,y, such that

    max{h_abs(x),h_abs(y)}
      >=C_2(epsilon)[Q(x,y):Q]^(-1/2-epsilon).        (1)

The rank is always two, and the base is always Q.
There is no uniform assertion as epsilon varies and no implicit dependence on the degree hidden in the choice of epsilon.
The source's attribution and original-proof limits remain those of U003.

### 1. Every actual off-pair subdegree has a classical lower bound

Let P be the primitive minimal polynomial of a genuine Salem number alpha>1, let X be its d=2t>=4 distinct roots, and let m=log alpha=d h_abs(alpha).
Let L be the normal closure, G=Gal(L/Q), and take any x,y in X belonging to DIFFERENT inverse pairs, so y is neither x nor x^(-1).
Put

    H=G_x, s=|H.y|=[G_x:G_x intersection G_y],
    M=[Q(x,y):Q].

The accepted [L_G397 pair-field identity](../../../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) gives M=ds.
Indeed the subgroup fixing both x and y is G_x intersection G_y, so the full joint field has index ds.
This is the same compositum degree M in [C_G162](../../../claims/Yin_C_G0162_v1.md#statement), not C162's potentially smaller degree D of the cross-exponent ratio x^p/y.
No prime or ratio enters the present application.

The numbers x,y are multiplicatively independent.
Choose an automorphism tau sending x to the real exterior root alpha.
Because inversion commutes with G, tau(y) is neither alpha nor alpha^(-1), hence has modulus one and is nontorsion.
Applying tau to x^a y^b=1 and taking absolute values forces a=0; nontorsion then forces b=0.
This also covers a C162 starting root x which is not itself the exterior real root.
For x=alpha the same argument needs no preliminary automorphism.

The two heights equal m/d, so (1) gives, simultaneously for EVERY off-pair orbit,

    m>=C_2(epsilon)
        d^(1/2-epsilon)/s^(1/2+epsilon).             (2)

The constant is the same for every input and every off-pair orbit at this fixed epsilon.
There is no normal-trace-field, Frobenius, matching-density, ramification or abelianity hypothesis.
Normal trace fields are a special case with s<=2, but are not needed for (2).

### 2. Bounded and sublinear-power subdegrees are already gap classes

For a fixed S>=1, an input admitting even ONE off-pair subdegree s<=S satisfies, on taking epsilon=1/4,

    m>=C_2(1/4) S^(-3/4) d^(1/4)
      >=sqrt(2) C_2(1/4) S^(-3/4)>0.                (3)

More generally fix 0<delta<=1 and A>0, and suppose some off-pair subdegree satisfies s<=A d^(1-delta).
Set

    epsilon_delta=delta/[2(2-delta)].

Then 1/2+epsilon_delta=1/(2-delta) and
(1/2-epsilon_delta)/(1/2+epsilon_delta)=1-delta.
Substitution in (2) yields the degree-uniform positive bound

    m>=C_2(epsilon_delta) A^(-1/(2-delta)).          (4)

At this exact epsilon the powers of d cancel; no growth in d is claimed in (4).
If growth is wanted, choose instead the smaller fixed epsilon=delta/[4(2-delta)].
The remaining exponent is delta/4, giving

    m>=C_2(epsilon) A^(-1/2-epsilon) d^(delta/4).    (5)

All parameters delta,A,epsilon in these family statements are fixed before varying the input.

### 3. Exact necessary subdegree growth in a hypothetical zero-gap sequence

Rearranging (2) with epsilon_delta gives

    s>=C_2(epsilon_delta)^(2-delta)
        m^(-(2-delta)) d^(1-delta), 0<delta<=1.     (6)

Let s_min(P) be the least off-pair subdegree for a fixed starting root; transitivity makes this minimum independent of that starting root.
Since the same constant works for all off-pair orbits, (6) holds for s_min(P) as well.
Thus on ANY hypothetical sequence of genuine Salem inputs with m_n tending to zero,

    s_min(P_n)/d_n^(1-delta) tends to infinity
        for every FIXED 0<delta<=1.                 (7)

In particular every off-pair subdegree tends to infinity; none can remain bounded or at most A d_n^(1-delta) for fixed A,delta.
The degrees must tend to infinity: for bounded d and m<=1, the integer coefficients are bounded by |a_(d-k)|<=binomial(d,k) exp(m), leaving only finitely many polynomials, each with positive m.
Since s_min<=d-2, (7) implies

    log s_min(P_n)/log d_n tends to 1.               (8)

This is not a positive lower bound for s_min/d and does not assert s_min is asymptotic to d.
No choice delta=delta_n tending to zero is justified without additional control of C_2(epsilon_delta).
Neither existence of a zero-gap sequence nor attainment of these necessary bounds is asserted.

### Fixed diagonal/inverse coverage classification

The distinct diagonal/inverse residue-mass argument and exhaustive C162 Salem case split are retained in [C483's unselected fixed supplement](../../../claims/Yin_C_G0483_v1.md#salem-diagonal-inverse-coverage).
The general rank-two inequality and bounded-s coverage already have C483/L398's adequate fixed home; [C165](../../../claims/Yin_C_G0165_v1.md#off-pair-salem-ratio-proof) owns inverse-pair independence and the exact off-pair cost.
The sublinear-power and logarithmic-ratio formulas above are their direct fixed-parameter algebraic consequences, with no new uniform-in-epsilon input or source-proof depth.
C162/C165 retain their actual support selections; no source statement, project adoption or old review is broadened by this placement.
