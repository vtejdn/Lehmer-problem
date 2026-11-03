---
author: Yin
---

# Monic residual quotient construction and its ninth-power endpoint cost

Human author Yin.
The paid_comparison contributor developed the complete construction, derivative identity and endpoint-cost proof on 2026-10-23 UTC under the active G0001 continuation.
Root assigned the original-polynomial comparison and authorized fixed registration, without supplying these derivations.
The complete author argument is retained here; the selected assessment owns its separate whole review and adoption.
No native program, parameter scan, numerical root computation or source acquisition was performed.

## Statement

Let P in Z[z] be monic irreducible reciprocal nontorsion, of degree d=2r>=2 and constant coefficient1.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), and assume that the actual trace field Q(delta) is totally real, with monic minimal trace polynomial T.
Use C_p(z+z^(-1))=z^p+z^(-p), theta_p=rem_T T(C_p)/p for p=2,3,5, and the ACTUAL integral values

    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.

Assume the full original residual f=e+s g=0, g!=0, for one s in{1,-1}.
Retain the SAME UNREDUCED polynomials

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    h=9d/2,
    W_s=13500z^h H23+32sH35.

Their exact degrees are6d,10d,15d and15d, respectively; the first three leading and constant coefficients are1,11,7.
The adopted C587v2 original identities give P|H25 and P|W_s.

**A. Primitive quotients and an actual monic multiplier candidate.**
The positive content of W_s is EXACTLY4.
Consequently

    Q25=H25/P in Z[z],
    R_s=(W_s/4)/P in Z[z]

are primitive reciprocal polynomials of respective degrees9d and14d, with leading and constant coefficients11 and56s.
Define the numerator F_s, its quotient D_s and the proposed transferred numerator N_s by

    F_s=3375s z^h H23+8H35-5(z^(5d)+1)H25,
    D_s=F_s/P=s R_s-5(z^(5d)+1)Q25,
    N_s=H35 D_s.                                  (1)

Then F_s and D_s are monic reciprocal integer polynomials of EXACT degrees15d and14d, each with constant coefficient1.
The polynomial N_s is primitive reciprocal integral of degree29d and has leading and constant coefficients7.
These statements concern polynomial COEFFICIENTS; they do not assign evaluation1 at z=1 or z=-1.

**B. Exact original-value nonvanishing test and norm ratio.**
Define the ACTUAL integer polynomial

    J_s=3375s z^(h-1)[hH23+zH23']
          +8H35'-5(z^(5d)+1)H25'.                 (2)

It has degree15d-1 and leading coefficient290d.
At every original root one has

    D_s(alpha)=J_s(alpha)/P'(alpha),
    Norm_(K/Q)D_s(alpha)
             =Res(P,J_s)/Res(P,P').               (3)

The denominator is nonzero.
The identity includes a possible zero numerator; no logarithm of a zero value is taken.
In particular

    D_s(alpha)!=0 iff P does not divide J_s
                   iff Res(P,J_s)!=0.             (4)

If nonzero, the ratio in (3) is a nonzero rational integer and has absolute value at least1.
Neither monicity nor constant coefficient1 of D_s resolves (4).

**C. An unconditional cost for this specific candidate.**
Put t=P(1), a nonzero integer under the original hypotheses.
The exact evaluation is

    D_s(1)=t[1250t^3+(30375s-1944)t+640-27000s].    (5)

For EVERY nonzero integer t and both signs,

    abs D_s(1)>=100 abs(t)^4>0,
    ||N_s||_1>=700 abs P(1)^9.                    (6)

For s=1 the stronger D_1(1)>=1250 abs(t)^4 holds.
Thus D_s has no factor z-1, and this particular multiplier cannot meet a fixed normalized coefficient budget on a class with unbounded abs P(1), independently of its degree or support.
Precisely, at C605's normalization with k0=30375 and any fixed positive rational q<2^(6/11),

    ||N_s/(k0q)||_1<=S_0
       implies abs P(1)<=[30375qS_0/700]^(1/9).     (7)

In particular S_0=1 requires abs P(1)=1.
There is no assertion that abs P(1) grows on an actual or hypothetical near-one full-residual family.

The construction gives an ACTUAL monic, constant-one integral candidate of degree14d rather than an arbitrary multiplier existence premise.
It does not establish its original nonvanishing, a useful upper bound on m(D_s), a uniformly sparse N_s, or its normalized coefficient budget on the remaining bounded-endpoint inputs.
No actual full-residual input, uniform D_G bound or G0001 completion is supplied.

## Reuse and reason for the construction

The directly used original divisibilities, phases, degrees and quotient endpoints are the complete [C587v2 DR1--DR12 account](Yin_C_G0587_v2.md#full-residual-direct-original-polynomial-reuse).
It provides Q25 with endpoint11 and QW=W_s/P with endpoint224s, and only LOWER Mahler bounds for those unnormalized quotients.
[C605](Yin_C_G0605_v1.md#statement) already proves primitivity of H25/H35, a real exterior H35 root in the actual trace domain, and a fully paid sufficient theorem for an ACTUAL multiplier with all its nonvanishing, Mahler, degree, support and coefficient hypotheses.
Those results are retained unchanged.
The new step identifies the exact removable integer content4 of W_s, then cancels the primitive quotient endpoint56 against5*11 to obtain (1).
The purpose is to examine a concrete construction rather than infer sparse numerator bounds from a displayed expression.

The author read the complete C587v2 original-polynomial account, C605's content proof and multiplier domain, C607's actual numerator/jet budgets, and C149/C150's full defect-syzygy and original-order limitations before the deduction.
A targeted local search for W_s content, primitive quotient combinations, endpoint56 and Q25/QW cancellation located no matching retained construction.
Existing fixed inputs and direct integer polynomial arithmetic suffice; no additional external theorem or mathematical program is needed.
This bounded reuse search makes no literature novelty claim.
The elementary mod-prime product check below supplies the required content facts without an unpriced order or maximal-order assertion.

The main question is still the original G0001 comparison.
The canonical trace remainder used in C196/C199 is a different object and is not changed by this construction.
The old C149 identity permits no free division by5a^15 in the integral order; no such step is used here.
The present polynomial cancellation also leaves all expanded coefficients in N_s, rather than counting the displayed summands as its support.

## Complete argument

### 1. The exact removable content of W_s

Put

    V_s=W_s/4=3375z^h H23+8sH35 in Z[z].

Its degree is15d and its leading and constant coefficients are56s.
Indeed the shifted H23 term has support only in[h,h+6d]=[9d/2,21d/2], strictly inside[0,15d].
Therefore its positive content divides56=2^3*7.
The coefficient of z^h in V_s is3375 times the constant coefficient1 of H23, plus a multiple of8 from the H35 term.
It is odd, so2 does not divide the content.

For the prime7 use the exact lowest-exponent mechanism in C605.
Write P mod7=1+c z^k+terms of higher degree, where c!=0 and1<=k<=d is the least positive exponent surviving modulo7.
Such k exists because P remains monic and nonconstant modulo7.
Since250=243=5 modulo7, H35 has its first nonzero positive coefficient at z^(3k), with value25c!=0 modulo7.
The constant coefficient7 vanishes modulo7.
Every positive exponent of the first term3375z^hH23 is at least h=9d/2>3d>=3k.
Thus the coefficient of z^(3k) in V_s is8s*25c, nonzero modulo7.
The content is not divisible by7 either, proving cont(V_s)=1 and cont(W_s)=4.
No original-root evaluation or full-residual relation was needed for this content calculation.

Under the original residual hypotheses, P divides H25 and W_s over Z by the fixed C587v2 argument.
Since V_s is integral and P is monic, rational divisibility of V_s by P also gives its integral quotient R_s by monic division.
The quotient Q25 is integral for the same reason.
C605 gives cont(H25)=1.
If a prime divided every coefficient of Q25, it would divide every coefficient of H25=P Q25, a contradiction; hence Q25 is primitive.
The same reasoning using cont(V_s)=1 proves that R_s is primitive.
Their exact degrees and endpoint coefficients follow from division by monic P with constant coefficient1.

### 2. Reciprocal cancellation with every degree retained

P, H23, H25 and H35 are reciprocal at their respective actual degrees.
The shifted term z^h H23 is symmetric at the common formal degree15d because2h+6d=15d.
Thus V_s is reciprocal of degree15d, and dividing by reciprocal P gives reciprocal R_s of degree14d.
Similarly Q25 is reciprocal of degree9d.
The factor z^(5d)+1 is reciprocal of degree5d, so its product with Q25 is reciprocal of degree14d.

Both the leading and constant coefficient of sR_s are56, while those of5(z^(5d)+1)Q25 are55.
Therefore their difference D_s is monic with constant coefficient1 and exact degree14d.
It is reciprocal and integral by the preceding paragraph.
Multiplying by P gives the exact F_s in (1), with degree15d, leading coefficient1 and constant coefficient1.
There is no cancellation of any unretained original factor or scalar.

N_s=H35D_s has exact degree29d and endpoint coefficients7.
It is reciprocal.
It is also primitive: if a prime divided every coefficient of N_s, then in the polynomial domain F_p[z] the product of H35 mod p and D_s mod p would be zero.
The former is nonzero by C605's primitivity theorem, and the latter is nonzero because it is monic.
This is impossible.
These coefficient statements prove A, but say nothing about the value of D_s at an original root or at either real endpoint.

### 3. The precise derivative obstruction to original nonvanishing

Differentiating the actual numerator in (1) gives

    F_s'=J_s-25d z^(5d-1)H25.                     (8)

The omitted term on the right is a known multiple of P.
Since F_s=P D_s, evaluation at any original root alpha_i yields

    J_s(alpha_i)=F_s'(alpha_i)=P'(alpha_i)D_s(alpha_i).

P has simple roots in characteristic zero, so P'(alpha_i)!=0.
This proves the first identity in (3) without a transversality assumption.
Its content is that transversality remains exactly the nonzero value of J_s at the same root.

The first summand of J_s has degree21d/2-1, strictly less than15d-1.
At degree15d-1 the other two summands have coefficients8*7*15d=840d and-5*11*10d=-550d.
Their sum is290d, proving the stated exact degree and leading coefficient.
The full derivative F_s' has leading coefficient15d; (8) retains the difference275d from its multiple-of-P term.
No leading term has been discarded from the identity at the polynomial level.

Because P is monic, multiplying the displayed evaluation identity over all d original roots is exactly

    Res(P,J_s)=Res(P,P') Res(P,D_s),
    Res(P,D_s)=Norm_(K/Q)D_s(alpha).

This proves (3), including the case of zero numerator.
Irreducibility of P makes J_s(alpha)=0 equivalent to P|J_s, and likewise for D_s.
Thus (4) follows.
When nonzero, D_s(alpha) is an algebraic integer and the ratio is its full nonzero integer norm, with every original embedding retained.
No field generated by a quotient replaces K, and no lower norm estimate is inferred when J_s vanishes.

The exact Mahler identity is separately

    m(D_s)=m(F_s)-m(P)>=0.

The inequality follows because D_s is a nonzero integer polynomial.
A useful small-Mahler upper bound would require a new upper estimate on this DIFFERENCE; the degree and endpoint normalization alone do not supply one.
No such estimate is asserted here.

### 4. The actual evaluation at1

Since P is irreducible nontorsion, P(1)=t is a nonzero integer.
At z=1 the complete unreduced values are

    H23(1)=9t^3-8t^2,
    H25(1)=75t^5-64t^2,
    H35(1)=250t^5-243t^3.

In (1) the shift is1 and z^(5d)+1=2.
Thus

    F_s(1)=1250t^5+(30375s-1944)t^3
                         +(640-27000s)t^2.

Division by P(1)=t proves (5).
In particular, constant coefficient1 of D_s did not license replacing this evaluation by1.
The evaluation retains the whole original P(1), not a normalized trace value.

For s=1,

    D_1(1)=1250t^4+28431t^2-26360t.

If t>=1, the last two terms equal t(28431t-26360)>0.
If t<=-1, both of those terms are positive.
Therefore D_1(1)>=1250|t|^4 for every allowed t.

For s=-1,

    D_(-1)(1)=1250t^4-32319t^2+27640t.

For |t|>=7 the triangle inequality gives

    |D_(-1)(1)|/|t|^4
      >=1250-32319/49-27640/343
       =174877/343>500>100.                       (9)

This handles BOTH signs of t on the unbounded range.
The remaining exact arithmetic is as follows; the middle columns are absolute values of the displayed polynomial, with no approximate roots or sampled extrapolation.

| j | abs D_(-1)(1) at t=j | abs D_(-1)(1) at t=-j | 100j^4 |
| --- | --- | --- | --- |
| 1 | 3429 | 58709 | 100 |
| 2 | 53996 | 164556 | 1600 |
| 3 | 106701 | 272541 | 8100 |
| 4 | 86544 | 307664 | 25600 |
| 5 | 111475 | 164925 | 62500 |
| 6 | 622356 | 290676 | 129600 |

Every middle entry exceeds the final entry.
Together with (9) and the positive-sign argument, this proves the first bound in (6) on every nonzero integer and both values of s.
It also proves D_s(1)!=0, hence z-1 does not divide this specific candidate.
This is not the original-value nonvanishing statement in (4).

### 5. Ninth-power coefficient cost and the exact remaining problem

For every nonzero integer t,

    |H35(1)|=|t|^3(250t^2-243)>=7|t|^5,

because250t^2-243-7t^2=243(t^2-1)>=0.
The coefficient norm of an ordinary polynomial dominates its modulus at1.
Consequently

    ||N_s||_1>=|N_s(1)|
       =|H35(1)| |D_s(1)|>=700|t|^9,

which proves (6) without any degree, support or Mahler estimate.
Applying the actual scalar1/(30375q) proves (7).
Since q<2^(6/11)<2, for |t|>=2 the normalized lower bound is greater than358400/60750>1.
Thus S_0=1 forces |P(1)|=1, as claimed.
The argument yields no converse and no construction on that remaining endpoint class.

For C605, the present D_s provides the exact degree budget B=14 and its resulting numerator has degree29d.
The remaining hypotheses are all substantive: (4) must be nonzero, m(D_s) must meet the chosen saving budget, and the ACTUAL expanded N_s must meet the uniform support and normalized coefficient bounds.
The ninth-power estimate rules out the latter for this construction on every class with unbounded |P(1)| and fixed q,S_0.
It does not rule out the construction on bounded-endpoint inputs, nor any other multiplier that can cancel an endpoint factor.
The full residual equations have not been shown to force endpoint growth.

The exact algebraic continuation point is J_s modulo P for original nonvanishing, together with an upper bound for m(F_s)-m(P) and actual expanded N_s coefficients on a justified bounded-endpoint class.
There is currently no proof or actual full-residual example supplying these three requirements.
The unit leading/constant coefficients remove one scalar obstacle but do not satisfy those missing analytic or arithmetic conditions.
No universal sparse numerator or original-root/Haar identification is inferred.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T16:06 |
| status | open |
| reason | Register the concrete primitive-quotient normalization, actual monic constant-one D_s construction, complete derivative/original-norm identity and all-sign ninth-power endpoint coefficient obstruction. Whole separate review and adoption remain pending; original nonvanishing, small Mahler cost, uniformly sparse numerator and useful full-residual class are not supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Parts A--C with the complete actual trace/residual domain, every content/degree/phase/leading/constant coefficient, original-value norm ratio and all nonzero integer endpoint signs. |
| argument | [Complete argument](#complete-argument) | All five sections, exact modulo2/modulo7 content proof, reciprocal quotient combination, full derivative and norm, finite signed table, unbounded endpoint proof and precise unresolved requirements. |
| dependency | [Actual original divisibilities](Yin_C_G0587_v2.md#full-residual-direct-original-polynomial-reuse) | Entire matched same-P H23/H25/H35 conventions, full residual f=e+s g=0, phase9d/2, monic integer divisibility and exact quotient degrees/endpoints. |
| dependency | [Primitive unreduced defects](Yin_C_G0605_v1.md#statement) | Exact primitive H25/H35 and their lowest-exponent modulo7 argument; the new W_s content and quotient cancellation are proved here. |
| support | [Paid multiplier target](Yin_C_G0605_v1.md#statement) | Only the actual full norm/Mahler/degree/support/coefficient requirements and fixed normalization30375q; no missing condition is inferred for D_s. |
| support | [Actual multiplier coefficient obstruction](Yin_C_G0607_v1.md#statement) | Earlier general jet/endpoint-budget context, not a premise of the direct ninth-power calculation. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T16:18 |
| status | proved |
| reason | Adopt the exact primitive-quotient construction, monic constant-one multiplier, derivative/full original norm criterion and all-sign ninth-power endpoint coefficient cost after the isolated whole R813 finding. The original-root nonvanishing, useful small Mahler difference, expanded sparsity/coefficient budget and useful actual full-residual input class remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Parts A--C with the complete actual trace/residual domain, every content/degree/phase/leading/constant coefficient, original-value norm ratio and all nonzero integer endpoint signs. |
| argument | [Complete argument](#complete-argument) | All five sections, exact modulo2/modulo7 content proof, reciprocal quotient combination, full derivative and norm, finite signed table, unbounded endpoint proof and precise unresolved requirements. |
| dependency | [Actual original divisibilities](Yin_C_G0587_v2.md#full-residual-direct-original-polynomial-reuse) | Entire matched same-P H23/H25/H35 conventions, full residual f=e+s g=0, phase9d/2, monic integer divisibility and exact quotient degrees/endpoints. |
| dependency | [Primitive unreduced defects](Yin_C_G0605_v1.md#statement) | Exact primitive H25/H35 and their lowest-exponent modulo7 argument; the new W_s content and quotient cancellation are proved here. |
| support | [Paid multiplier target](Yin_C_G0605_v1.md#statement) | Only the actual full norm/Mahler/degree/support/coefficient requirements and fixed normalization30375q; no missing condition is inferred for D_s. |
| support | [Actual multiplier coefficient obstruction](Yin_C_G0607_v1.md#statement) | Earlier general jet/endpoint-budget context, not a premise of the direct ninth-power calculation. |
| review | [Whole isolated independent finding](../audits/reviews/Yin_R_G0813_v1.md#monic-residual-quotient-whole-finding) | Entire unchanged A--C statement and complete argument, all selected inputs, reconstructed same-P divisibilities, precise derivative/norm identity and exhaustive endpoint arithmetic, with accepted source scope retained. |

