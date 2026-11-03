---
author: Yin
---

# Complete modulo-two image of rational weighted Laurent norm-one columns

Date:2026-10-11T15:00.
Root coordinating AI for Yin fixes the complete restricted author account below under the continuing G0001 weekly authorization, after separately organized complete review in [the responsible R](../audits/reviews/Yin_R_G0207_v1.md#mod-two-image-whole-finding).
Adopt exactly its stated hypotheses, original costs, failures and source/review limits.
No unrestricted Mahler gap, canonical Claim or Task completion is asserted.

<a id="coupled-method-fixed-scope"></a>
## Fixed scope and preservation

The entire author account follows, with only title depth, navigation and final blank-line normalization.
Allocation-era pending-review statements remain history; the linked fixed R supplies the actual completed review scope.
Proposed or unrun computations remain unrun.
No new allowance, input-uniform conditioning or actual unit/covariance realization is inferred.
Further mathematics uses a distinct draft.

The current complete coefficient reduction and nonreduced quartic image theorem is retained in [C443](../claims/Yin_C_G0443_v1.md#complete-nonreduced-mod-two-image), adopted after [R646 whole self-review](../audits/reviews/Yin_R_G0646_v1.md#current-mod-two-image-whole-finding).
The entire original author body below retains day-precision freeze, the22:57 R207 report and23:00 retention, exact41,-1 control and its then-open target; the later [L384 exact word](Yin_L_G0384_v1.md#exact-width-five-lift-discovery) has its own separate scope.
No current research Task/E resumes.

## Complete retained account


## Exact modulo-two image of rational weighted Laurent norm-one columns

Date:2026-10-11.
Root AI for Yin, under the continuing G0001 weekly authorization.
This responsible draft tests whether the known odd-denominator/monomial reduction obstruction can decide the actual quartic interpolation problem at unrestricted width.
The completed [L377](Yin_L_G0377_v1.md) supplies its original input and denominator necessity.
[D26's rational delay-projection construction](Yin_L_G0380_v1.md#rational-weighted-delay-factorization) suggests the changed question, but every matrix identity needed here is checked directly below; its pending independent review is not assumed complete.
No native program or finite search is declared.

## Reuse and exact question

A bounded local screen of L377, the responsible D26 and existing Claims/source-audit entrances found the odd-denominator monomial necessity and rational delay factorization, but no image classification for this reduction.
The new step is elementary exact matrix arithmetic over the rational Laurent ring and its modulo-two reduction; no external group-generation theorem is needed.
No novelty claim or inference from an unsuccessful literature search is made.
The underlying factor form has the classical attribution checked in D26; this proof does not invoke an uninspected factorization theorem.

Let H=diag(1,2), R=Q[t,t^-1], f*=f(t^-1).
A rational Laurent column v=(f,g)^T has norm one when ff*+2gg*=1.
L377 proves that its least common scalar denominator is odd.
Therefore each coefficient lies in the local ring Z_(2), and reduction modulo2 is unambiguous.
The question is the COMPLETE image of all such columns, and then its image in the actual quotient A_2=F2[t]/(t^4+t^2+1).

<a id="complete-mod-two-column-image"></a>
## 1. Necessary image, including the constant-point constraint

The reduction of ff*+2gg*=1 gives fbar fbar*=1 in the Laurent domain F2[t,t^-1].
Its units are monomials, so fbar=t^k for some integer k.
This is the same extreme-lag argument as L377.
There is a second necessary condition:

    gbar(1)=0, or equivalently gbar in (t-1)F2[t,t^-1].       (1)

Indeed f(1),g(1) belong to Z_(2) and f(1)^2+2g(1)^2=1.
Reduction modulo2 first shows f(1) odd.
In Z/8 every odd square is1, including an odd rational numerator divided by an odd denominator.
If g(1) were odd, the left side would be3 modulo8, impossible.
Hence g(1) is even, proving(1).
Evaluating a Laurent polynomial at1 is legitimate and divisibility by t-1 follows after multiplying by a monomial.

We will prove that these are ALL restrictions on the reduction.
This is a statement about reductions of exact rational Laurent norm-one columns, not about lifting a prescribed algebraic value exactly over Q.

<a id="constructive-mod-two-shear-lift"></a>
## 2. Explicit norm-one matrices realizing every allowed reduction

Put r=(1,1)^T, Pi=(1/3)[[1,2],[1,2]], and

    E=I-Pi+t Pi=(1/3)[[2+t,2(t-1)],[t-1,1+2t]],
    D=diag(t,1), V=E D^-1.                                  (2)

Direct multiplication gives Pi^2=Pi and Pi^T H=H Pi.
Consequently E^sharp H E=H, where sharp is transpose followed by t->t^-1.
The diagonal D has the same property, so V and every D^j V D^-j do too.
All coefficients lie in Z[1/3], including the explicit inverses.
Reducing(2) modulo2 gives

    Vbar=[[1,0],[(t-1)t^-1,1]],
    (D^j V D^-j)bar=[[1,0],[(t-1)t^(-j-1),1]].              (3)

For any Laurent polynomial h over F2, expand h as a FINITE sum of monomials.
Multiplying the corresponding matrices in(3) adds their lower-left entries, since [[1,0],[a,1]][[1,0],[b,1]]=[[1,0],[a+b,1]].
Thus there exists an explicit rational Laurent H-paraunitary W, with only powers of3 in its scalar denominators, such that

    Wbar=[[1,0],[(t-1)h,1]].                                 (4)

Given k and any desired gbar=(t-1)a(t), apply this construction with h=t^-k a.
Then v=W D^k e_1 is an exact norm-one rational Laurent column and

    vbar=(t^k,(t-1)a(t))^T.                                 (5)

This proves the complete image classification.
The zero a case uses the empty product.
Negative exponents cause no difficulty.
If h has s nonzero coefficients, the displayed construction uses s copies of V conjugated by diagonal monomials, and its common denominator divides3^s; neither equality nor a uniform degree bound independent of those exponents is claimed.
The necessary bound from Section1 and sufficiency(5) match exactly.

<a id="actual-quartic-mod-two-orbit"></a>
## 3. Exact image at the original nonreduced quartic quotient

Use the original irreducible reciprocal unit polynomial

    P=t^4-2t^3+t^2-2t+1, alpha=t mod P,
    tau=alpha+alpha^-1, u=(tau,(1-alpha)^-1)^T.

Its mod2 polynomial is Pbar=(t^2+t+1)^2=t^4+t^2+1, and A_2 has16 elements.
Both t and t-1 are invertible in A_2: Pbar(0)=Pbar(1)=1.
The class a of t has exact multiplicative order6.
In fact a^6=1 since (t^3+1)^2=(t+1)^2 Pbar, while a^3 is not1 because t^3+1 has smaller degree than Pbar; also a and a^2 are not1.
The only proper divisors of6 are1,2,3, proving exactness without replacing this ring by its reduced field.

The complete image of all rational norm-one columns after coefficient reduction and quotient evaluation is

    { (a^k,b)^T : k modulo6, b in A_2 }.                     (6)

There are exactly96 such vectors.
Necessity follows from Section1.
To realize b, choose its unique representative B(t) of degree<4 and set Gbar=B+B(1)Pbar.
Then Gbar(1)=0 and Gbar(a)=b.
Section2 gives a norm-one lift with first reduction t^k and second reduction Gbar.
Every such quotient vector has a lift whose scalar denominator uses only powers of3.
This is an exact constructive surjectivity statement for the finite reduction(6), not surjectivity over the original rational number field.

<a id="actual-target-mod-two-control-and-full-norm-cost"></a>
## 4. The actual target passes, with a strict full-norm distinction

The original L377 formulas give tau_bar=a^3 and ((1-alpha)^-1)_bar=a^2+a^3.
Thus u lies in the complete finite image(6).
An explicit particularly short lift of this REDUCTION is

    v_0=t^2 E e_1=(t^2(t+2)/3, t^2(t-1)/3)^T.              (7)

Its exact norm one follows from(2), or directly from

    (t+2)(t^-1+2)+2(t-1)(t^-1-1)=9.

Its two reductions are a^3 and a^2+a^3 as required.
Its actual scalar denominator is3 and union support is[2,3].
It does NOT interpolate u over Q.
Clearing denominators gives F=t^2(t+2), G=t^2(t-1), with full original resultants

    Res(P,F)=P(-2)=41, Res(P,G)=P(1)=-1.                    (8)

Here the norm of alpha is1, and P has even degree4, so both signs and monomial factors are accounted for.
A denominator3 interpolant to the original unit values would instead have full resultants+81 and-81.
Thus the small-width modulo-two lift supplies no unit/covariance surplus for the original exact problem, and it does not contradict L377's exact width-at-most-four exclusion.
Reduction at2 loses precisely arithmetic information that these full norms retain.

## 5. Outcome, next gate and author freeze

The monomial first-coordinate and even constant-point second-coordinate conditions classify the full coefficient reduction.
At the original quartic quotient, the image consists of all96 vectors in(6), and the actual target belongs to it with the explicit control(7).
Therefore a method using only this mod2 orbit cannot exclude arbitrary-width rational Laurent interpolation at that target.
Higher congruence depth, other arithmetic places, exact field orbit membership or full archimedean/norm constraints remain possible; this theorem excludes none of them.
The full original quotient interpolation and unrestricted G0001 remain unresolved.

Author self-check covers odd rational reduction, the modulo8 constant-point argument, Laurent units, H-selfadjoint projection and matrix inverses, conjugation exponents and all shear sums, finite construction/denominator bound, the nonreduced quotient and exact order6, all16 second coordinates and96 distinct vectors, target residues, the width-one reduction control, and complete signed resultants41,-1 versus81,-81.
These are exact algebraic calculations, with no native computation or scan.
The complete Sections1--5 and equations(1)--(8) are frozen for separately organized whole noncontributor review; no independent review is claimed here.
