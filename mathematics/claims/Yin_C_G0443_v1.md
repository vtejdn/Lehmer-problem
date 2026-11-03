---
author: Yin
---

# Complete rational norm-one coefficient reduction and nonreduced mod-two image

This retains the complete necessary mathematical argument from [the complete original G381 account](../ledger/Yin_L_G0381_v1.md).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

For every rational Laurent norm-one column v=(f,g)^T in Q[t,t^-1]^2 satisfying ff*+2gg*=1 with *=t->t^-1, its actual least common scalar denominator is odd.
Coefficient reduction at2 is therefore defined in Z_(2), and its complete image is precisely

    { (t^k,(t-1)a(t))^T : k in Z, a in F2[t,t^-1] }.

Necessity includes fbar fbar*=1 in the Laurent domain and the extra constant-point condition gbar(1)=0, obtained by the full mod8 odd-square argument at t1.
It is not merely the degenerate mod2 norm equation.

For constructive sufficiency use H=diag(1,2), Pi=(1/3)[[1,2],[1,2]], E=I-Pi+t Pi, D=diag(t,1), V=E D^-1.
These are exact rational Laurent H-paraunitaries, and

    Vbar=[[1,0],[(t-1)t^-1,1]],
    (D^j V D^-j)bar=[[1,0],[(t-1)t^(-j-1),1]].

For any finite Laurent h, multiply the conjugates corresponding to its nonzero monomials to obtain Wbar=[[1,0],[(t-1)h,1]].
For the requested k,a put h=t^-k a and v=W D^k e1.
Negative exponents and the empty product are allowed.
If h has s nonzero coefficients, the displayed actual common denominator divides3^s, with no equality or exponent-independent width bound.
All identities, including inverses and conjugation signs, are proved locally without a group-generation or source-factorization theorem.

For the ORIGINAL irreducible reciprocal quartic P=t^4-2t^3+t^2-2t+1 and alpha=t modP, use the actual nonreduced quotient

    A2=F2[t]/((t^2+t+1)^2)=F2[t]/(t^4+t^2+1).

It has16 elements; a=t modPbar and a-1 are units, and a has exact order6, retaining the nilpotents.
The complete coefficient-reduction-and-evaluation image is exactly

    { (a^k,b)^T : k mod6, b in A2 },

with96 distinct vectors, each admitting a lift with scalar denominator a power of3.
For every degree<4 representative B of b, Gbar=B+B(1)Pbar has Gbar(1)=0 and Gbar(a)=b, so every second coordinate is constructed explicitly.
This is finite-reduction surjectivity, not arbitrary rational-field orbit surjectivity or an exact prescribed-value lift.

The actual original target u=(tau,(1-alpha)^-1)^T, tau=alpha+alpha^-1, reduces to(a^3,a^2+a^3), and therefore passes this complete screen.
The explicit congruence lift

    v0=t^2 E e1=(t^2(t+2)/3,t^2(t-1)/3)^T

has exact norm1, least denominator3 and union width1, by the full polynomial identity5+2(t+t^-1)+4-2(t+t^-1)=9.
After clearing its denominator its original full signed resultants are41,-1, including the monomial and degree4 signs.
An exact original-unit interpolant at denominator3 instead requires81,-81.
Thus v0 is a congruence control, not an exact original-unit interpolant, even up to signed monomial twists; it contradicts neither the exact width<=4 obstruction nor full norm/covariance costs.

The proof classifies only this coefficient/finite quotient image and supplies no unrun finite enumeration, native evidence, higher-congruence classification, original-field orbit theorem, input-uniform degree/cost or Mahler-gap conclusion.
Its original day-precision freeze and then-open exact-target language are historical; the separate later L384 exact word solves that target and all its dyadic reductions, without changing this classification or its41,-1 control.
No external source proof, new mathematical program, scan or Task/E execution is used.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:16 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact original odd-denominator theorem](Yin_C_G0430_v1.md#paraunitary-scalar-denominator-primes) | Only odd least scalar denominator for every rational weighted Laurent norm-one column and full original signed q^4 norm requirements. |
| dependency | [Exact original quartic and unit data](Yin_C_G0430_v1.md#paraunitary-lift-reuse-and-domain) | Original irreducible reciprocal degree4 field, all-root units and full norm signs, without discarding any conjugate or scalar content. |
| dependency | [Exact finite-width comparison](Yin_C_G0430_v1.md#independent-twist-width-four-obstruction) | Only original-unit width<=4 exclusion for independently signed twists; the new congruence control does not meet its original exact residues. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:17 |
| status | proved |
| reason | Adopt the complete actual SELF check of the exact coefficient image, all constructive and necessary cases, nonreduced quotient/order6/96 image, target and full original norm controls. Preserve all original author/whole SELF, day/time precision, no-native/source and later-target status boundaries; no new proof repair, source theorem or Task execution occurs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0430_v1.md#paraunitary-scalar-denominator-primes) | Only odd least scalar denominator for every rational weighted Laurent norm-one column and full original signed q^4 norm requirements. |
| dependency | [Exact accepted input](Yin_C_G0430_v1.md#paraunitary-lift-reuse-and-domain) | Original irreducible reciprocal degree4 field, all-root units and full norm signs, without discarding any conjugate or scalar content. |
| dependency | [Exact accepted input](Yin_C_G0430_v1.md#independent-twist-width-four-obstruction) | Only original-unit width<=4 exclusion for independently signed twists; the new congruence control does not meet its original exact residues. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0646_v1.md#current-mod-two-image-whole-finding) | Entire exact Statement and Argument plus full original Sections1–5/equations1–8 and all old whole bindings, useful negative/domain/cost/source limits. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="complete-nonreduced-mod-two-image"></a>
The exact original denominator/unit and width inputs are retained in [C430](Yin_C_G0430_v1.md#paraunitary-scalar-denominator-primes).
The dated original exploration and then-open status remain at L381; the separate later [L384 exact word](Yin_C_G0453_v1.md#exact-width-five-lift-discovery) does not supply a premise to this classification.

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
