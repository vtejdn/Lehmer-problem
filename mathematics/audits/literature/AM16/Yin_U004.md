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

### 4. The two excluded orbitals and their existing residue coverage

The diagonal y=x and inverse y=x^(-1) cases have s=1, but x,y are multiplicatively dependent, so (1)--(8) do not apply to them.
They occur for every Salem polynomial and cannot be silently included in the off-pair minimum.
Their treatment retains the ACTUAL residue-Frobenius lift and positive matching density from C162.

The needed independent existing result is [L_G205 Section 4](../../../ledger/Yin_L_G0205_v1.md#bounded-residue-mass-near-one-escape), selected in its [adopted scope](../../../ledger/Yin_L_G0205_v1.md#local-rigidity-near-one-mass-fixed-scope) and covered by the [complete R_G104 review](../../reviews/Yin_R_G0104_v1.md#minimal-frobenius-local-complete-independent-review).
For any nontorsion monic irreducible unit polynomial P, let W_(p,F)(P) count its complete mod-p factor degree in factors of degree at most F, including each polynomial multiplicity.
For a supplied fixed 0<gamma_0<=1, the condition W_(p,F)>=gamma_0 d gives

    m>=gamma_0 log2/
       [N_(p,F) p^(ceil(1/gamma_0)+1)],
    N_(p,F)=lcm_(1<=f<=F)(p^f-1).                   (9)

This is L205 equation (14), which needs no unramifiedness, distinct reductions, maximal power-basis order or bound on the normal-closure ramification.
The original-label counting and repeated-reduction scope are explicitly checked in R104.
The present account uses that accepted result; it performs no new independent review of L205.

For C162's diagonal orbital, b matching roots obey sigma(z)=z, hence their nonzero reductions satisfy z_bar^p=z_bar and lie in F_p.
Thus W_(p,1)>=b and a matching density b/d>=gamma_0 satisfies (9) with F=1.
For the inverse orbital, b matching roots obey sigma(z)=z^(-1), hence z_bar^(p+1)=1 and z_bar^(p^2)=z_bar.
Their reductions lie in F_(p^2), so W_(p,2)>=b and (9) applies with F=2, where N_(p,2)=p^2-1.
Several roots may have the same reduction; W counts the original root labels with exactly their reduction multiplicities, so the inequalities still hold.
This establishes the inverse case also at ramified primes, without borrowing the narrower unramified hypothesis from the earlier L160/L162 inverse-matching estimates.

For each fixed p, L205 also says W_(p,2)/d tends to zero along any hypothetical total-zero-gap sequence.
Consequently both diagonal and inverse matching densities tend to zero, uniformly over actual Frobenius lifts at that p, since both are bounded above by W_(p,2)/d.
A fixed finite prime pool permits the same conclusion by taking the maximum of finitely many such bounds.

### 5. Exact consequence for the C162 Salem domain

For genuine Salem inputs, C162's chosen pair belongs to exactly one of the three preceding cases; membership in the same inverse pair is G-invariant.
Suppose its prime belongs to a fixed finite set, its valency satisfies s<=S for fixed S, and its matching density satisfies gamma>=gamma_0>0.
An off-pair orbit is already covered by (3), independently of the prime and gamma.
A diagonal or inverse orbit is already covered by (9), with F=1 or 2.
The minimum of (3) and the finitely many F=2 constants in (9) is therefore a uniform positive gap covering the ENTIRE stated bounded-parameter Salem class.

Accordingly the bounded-valency C162 specialization supplies no new qualitative Salem gap coverage beyond the classical rank-two theorem and existing residue-mass result.
Its explicit parameter dependence, local norm identities, signs and original-field return may still be useful and need not coincide numerically with these bounds.
No comparison of unknown C_2(epsilon) with C162's explicit constants is asserted.
This does not classify C162's full domain of arbitrary nontorsion algebraic integer units: the off-pair independence used above is specific to the Salem signature.
The original unrestricted G0001 gap and possible methods using growing off-pair subdegrees remain unresolved.

This bounded reuse check stops after the exhaustive Salem scope split.
No further literature search, computation, source-proof review or new-theorem claim is needed for the stated classification.
