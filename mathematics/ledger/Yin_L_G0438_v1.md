---
author: Yin
---
# Unbuffered balanced shears: arithmetic gate, exact costs and two-input failure

The complete current mathematical statement and necessary original proof are adopted in [C581](../claims/Yin_C_G0581_v1.md#decision-complete-current-self-adoption), with [actual constructor whole SELF review](../audits/reviews/Yin_R_G0758_v1.md#current-g439-complete-self-finding).
The complete original analysis, source/contribution boundaries, useful failures and mathematical continuation questions remain below.


Original mathematical dates: 2026-10-18T09:58 and2026-10-18T10:50.
Fixed content extraction: 2026-10-20T12:10.
Human author Yin.
The shear_arithmetic agent supplied the initial residual analysis; entropy_attainment_bridge supplied the integer-q gate and exact transformed-family comparison, with root supplying the residual question and comparison request.
The draft_comparison_cleanup agent preserves those existing author arguments here under root's retention assignment and contributes no new mathematical deduction.
The original extraction retained author-level mathematics; it supplied no whole independent review.
The previously certified J99/J100 evidence and its own reviews keep exactly their existing scopes.

<a id="historical-unresolved-unbuffered-stage"></a>
## Historical question and later resolution

The following original question and unresolved-stage observations belong to the two2026-10-18 author stages identified above.
They are preserved so that earlier C157 versions and later extraction-context references can point to the actual historical responsibility without treating a future result as their premise.
The arbitrary totally real integral-triple target was later refuted by [C192's actual unit residuals](../claims/Yin_C_G0192_v1.md#statement), adopted through [whole R466](../audits/reviews/Yin_R_G0466_v1.md#unit-residual-existence-whole-independent-finding).
That later theorem is not used in the older gate or circle comparisons below.
Every occurrence of an unresolved q=1 question in the retained dated comparison describes that historical stage, not the current mathematical status.
The complete original buffered alternative is already retained in [C157v1](../claims/Yin_C_G0157_v1.md#argument) and its later actual versions, so its proof is not copied here.

## Responsible question and reused inputs

Let F be a totally real number field of degree r and let a,b,c be nonzero algebraic integers in F.
Put e=b^2-a^3, f=2c^2-3a^5 and g=c^3-2b^5.
For s in {1,-1}, examine Q_s=(e+s g)^2+f^2+g^2 and the target Norm_F(Q_s)>=2^r.
The unresolved case is identified below; the later balanced-family comparison explains why resolving it is unnecessary for the two already screened controls.

[C153v2](../claims/Yin_C_G0153_v2.md#argument) supplies exactly the exclusions (e,g)!=(0,0) and (f,g)!=(0,0) over a totally real field.
[C155](../claims/Yin_C_G0155_v1.md#argument) supplies the full norm argument for two nonzero integral squares and the stronger singleton estimate only under e=f=0.
[C156](../claims/Yin_C_G0156_v1.md#argument) preserves this same singleton distinction under balanced weights.
The direct existing inputs suffice for the case reduction below; no new literature premise is used or needed.
The C155 singleton estimate must not be silently used for the changed relation e+s g=0.

<a id="unbuffered-reduction"></a>
## Exact reduction for the unbuffered shear

Write x=e+s g.
If at least two of x,f,g are nonzero, choose two fixed nonzero integral elements u,v among them.
For every real embedding sigma, sigma(Q_s)>=sigma(u)^2+sigma(v)^2>=2|sigma(u)sigma(v)|.
Multiplying all r inequalities gives Norm_F(Q_s)>=2^r|Norm_F(u)Norm_F(v)|>=2^r.
The choice of u,v is global in F; it does not vary with the embedding.

There cannot be zero nonzero transformed coordinates, since that would give f=g=0.
The sole-x case would give f=g=0 and is excluded by C153v2.
The sole-f case would give g=x=0, hence e=g=0, and is excluded by C153v2.
The only remaining case is therefore

    f=0, e+s g=0, g!=0,
    Q_s=g^2.

The target reduces exactly to |Norm_F(g)|>=2^(r/2) on this residual system.
Even excluding a unit g would not by itself establish this exponential bound for arbitrary r: a nonunit only yields |Norm_F(g)|>=2.
C155 yields only Norm_F(Q_s)>=1 here, because the old h=e^2+f^2+g^2 is 2g^2.
At the original2026-10-18 stage, no counterexample and no proof of the stronger residual norm inequality had been obtained.

The elementary valuation identity from f=0 is

    5 v_p(a)=v_p(2)+2v_p(c)-v_p(3).

At a prime over 2, this forces v_p(a)>0 but does not force v_p(c)>0; when v_p(c)=0 it is compatible with 5v_p(a)=v_p(2).
The residual equation e+s g=0 reduces modulo that prime to b^2+s c^3=0.
Thus this observation alone does not exclude a unit g, whose reduction would be c^3.
At a prime over 3, v_p(c)>0 follows, but g may reduce to -2b^5 and again need not vanish.
These are limitations of the elementary local test, not existence claims.

<a id="unbuffered-balanced-reassessment"></a>
## Bounded reassessment: the balanced gate and the actual two-input screen

2026-10-18T10:50.
The entropy_attainment_bridge AI supplied the integer-q>=2 gate and direct shear comparison below for Yin; root identified the residual question and requested the comparison with the buffered family.
These are the original author-checked deductions at their historical stage.

### The residual problem only blocks the integer parameter q=1

For every integer s and integer q>=2 put

    x=e+s g,
    H_(s,q)^0=q^2(x^2+g^2)+f^2.

Under the original totally real integral-triple hypotheses, this element is totally positive and

    Norm_F(H_(s,q)^0)>=(2q)^r.                       (1)

Indeed if f=0, C153v2 gives g!=0, so every embedding has H_(s,q)^0>=q^2 g^2 and

    Norm_F(H_(s,q)^0)>=q^(2r)|Norm_F(g)|^2
                         >=q^(2r)>=(2q)^r.

The last step is exactly q>=2; no extra divisibility or exponential lower bound on Norm_F(g) is used.
If f!=0 and g!=0, the q^2 g^2 and f^2 terms give the full bound by weighted AM-GM and their nonzero integer norms.
If f!=0 and g=0, then e!=0 by C153v2, so x=e and the same argument uses q^2 e^2 and f^2.
These cases are exhaustive and prove total positivity and (1) simultaneously.
Thus the unresolved q=1 singleton is unnecessary for the balanced integer-q>=2 family.
The assertion does not establish the missing bound |Norm_F(g)|>=2^(r/2) when q=1.

For the actual C157 original-polynomial setting retain its exact trace domain, d=2r, L=972000 and numerator phases.
Define

    A_(U,s)^0=[13500 t^(9d/2)H23+32s H35]^2+32^2 H35^2,
    A_(s,q)^0=q^2 A_(U,s)^0+A25,
    B_(s,q)^0=t^(-15d)A_(s,q)^0/(qL^2).

The same exact phase identities give B_(s,q)^0(alpha)=H_(s,q)^0/q.
Consequently, for every integer s and q>=2,

    Norm_K(B_(s,q)^0(alpha))=Norm_F(H_(s,q)^0)^2/q^d>=2^d,
    Norm_K(B_(s,q)^0(alpha))=Res(P,A_(s,q)^0)/(qL^2)^d.

Every original embedding and the full q^d denominator remain.
The exact numerator degree is 30d and its leading and constant coefficient is 50176(s^2+1)q^2>0, since only the two H35 square terms reach the endpoints.
The centered support remains [-15d,15d] and the same supremum return charges 30m(P).
No Haar-to-original-root replacement is inferred.

### A direct transformed-family comparison closes s=+1 and s=-1 on both controls

Use C157's real centered circle functions E,G,F_0 and put

    U_0=E^2+G^2,
    U_s^0=(E+sG)^2+G^2,
    V=F_0^2.

For s in {1,-1}, direct completion of squares gives

    3U_s^0-U_0
      =2E^2+6sEG+5G^2
      =2(E+(3s/2)G)^2+G^2/2>=0.                  (2)

Thus U_s^0>=U_0/3 pointwise on the circle.
All relevant logarithms are integrable: U_s^0>=G^2, G is a nonzero Laurent polynomial with finitely many finite-order circle zeros, and V is the already treated nonzero square.
The finite exceptional zero set therefore does not obstruct logarithmic comparison or integration.
For every positive real q, weighted AM-GM and (2) give

    I_(s,q)^0=integral log(q U_s^0+q^(-1)V)
       >=log2+(J_(U,s)^0+J_V)/2
       >=log2+(J_(U,0)+J_V-log3)/2.                 (3)

This uses the actual transformed circle function, rather than transferring an unweighted Haar failure by assertion.
The [J99 certified component account](../computations/programs/Yin_J_G0099/readme.md#certified-results), independently checked in [R377](../audits/reviews/Yin_R_G0377_v1.md#two-input-component-finding), already gives

    quartic_Salem_seed: J_(U,0)+J_V=3.242875824944,
    Lehmer_degree10:    J_(U,0)+J_V=4.254495252414,

each with certified absolute error below 1e-10.
Their existing enclosures imply the strict bounds >3 and >4 respectively.
Since exp(2)>1+2+2=5>3, log3<2.
Equation (3) consequently proves

    I_(s,q)^0>log2+1/2   on the quartic input,
    I_(s,q)^0>log2+1     on the Lehmer input,          (4)

simultaneously for s=+1,-1 and every real q>0.
No new scalar approximation or numerical certificate is needed for these deliberately coarse strict margins.
In particular both signs fail every sub-log2 target and the earlier 1/16 operational margin, including every legal integer q>=2 and the still-unproved q=1 arithmetic case.

### Why the weaker H35-only screen would have been misleading

Removing the buffer changes the generic all-real-s lower bound from U_s>=2G^2 to U_s^0>=G^2.
The resulting all-(s,q) lower envelope is log2+(J_G+J_V)/2, smaller than the buffered bound by exactly (log2)/2.
The [J100 component account](../computations/programs/Yin_J_G0100/readme.md#certified-results) already has J_G+J_V<0 on both controls, so that weaker screen alone would leave room for both.
This change is real but does not contradict (4): the H35-only comparison is uniform over every real shear s, whereas (2)--(4) use the actual bounded signs s=+1,-1.
No grid or higher-precision integration is justified for those two signs by failure of the weaker screen.

More generally Cauchy-Schwarz applied to E=(E+sG)-sG gives

    E^2+G^2<=(s^2+2)[(E+sG)^2+G^2],
    I_(s,q)^0>=log2+(J_(U,0)+J_V-log(s^2+2))/2.     (5)

The first inequality follows from E^2<=(1+s^2)[(E+sG)^2+G^2] and G^2<=(E+sG)^2+G^2.
This is a valid elementary screen for any specified real s, with its explicit shear cost; it is not an estimate uniform in unbounded s.
Exploring larger s would be a different allocation and would still require actual circle and original-root transfer costs.

### Remaining singleton and its relevance

The initial q=1 system remains unresolved: f=0 implies a is totally positive and 3^r Norm_F(a)^5=2^r Norm_F(c)^2, so 2^r divides Norm_F(a)^5 and Norm_F(a)>=2^(r/5).
This statement is about a, not g.
The relation e+s g=0 implies b^2=a^3-sg; eliminating c through f=0 gives

    27a^15=8(2b^5+g)^2.

Reducing modulo the integral ideal (g) yields 5a^15 in (g), because b^10=(b^2)^5 is congruent to a^15 modulo (g).
This is an upper divisibility constraint on g and supplies no desired lower bound for its full norm.
The existing local valuation analysis likewise neither proves the exponential norm floor nor constructs an admissible totally real counterexample.
No trace-quotient realization of a residual counterexample has been shown.

The bounded analytical screen is therefore complete without resolving that more general abstract system.
For q>=2 the arithmetic gate is already open by (1), but the actual s=+1,-1 families are closed on both prescribed controls by (4).
For q=1 the unresolved gate cannot rescue their failed Haar side on those controls.
A useful next application of the abstract singleton would require a different input or a mathematically justified changed shear allocation whose certified circle side is useful.
The candidate-level failure on these two controls is not a conclusion about every original polynomial.
