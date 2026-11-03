---
author: Yin
---

# Complete cubic-unit counterfamily to nonnegative doubling phase balance

The complete original D42 theorem and every necessary proof are retained from [L175](../ledger/Yin_L_G0175_v1.md#retained-negative-phase-control).
The original coordinator authored the cubic family, root geometry, cancellation, circle bound and full-integral interpretation, and explicitly self-checked the whole written proof.
That [actual original whole author check](../audits/reviews/Yin_R_G0074_v1.md#negative-phase-original-author-check-finding) is retained at the original 2026-10-10 day precision.
The separately assigned [whole noncontributor account](../audits/reviews/Yin_R_G0074_v1.md#negative-phase-balance-independent-review) has unestablished actual initial target context, so its independent-review relationship remains unknown.
The positive finite trinomial observations motivated the changed question and are not premises of the proof.
The proof is elementary polynomial arithmetic and the explicit integrable Mahler convention.
No new source or computation is used.

## Statement

For every integer A>=2 let

    f_A(t)=t^3+A t^2+(1-A)t-1,
    f_A*(t)=t^3 f_A(1/t),
    G_A=((f_A*)^2 f_A(t^2)+f_A^2 f_A*(t^2))/2.

Then f_A is a primitive irreducible monic algebraic-unit polynomial.
Its three roots are real and simple, with one in each disjoint interval

    (-A-1,-A), (-1,0), (0,1).

Exactly the negative root has modulus tau_A>1, and

    A<tau_A<A+1, m(f_A)=log(tau_A)>log A.

The auxiliary G_A is a nonzero integer polynomial.
Its exact reversal relation f_A+f_A*=t+t^2 cancels the cubic-in-A part of its numerator.
For every point of the unit circle,

    |G_A|<=85A^2.

Using the full logarithmic Mahler measure, including all factors and any leading coefficient, put Delta_A=log2+m(G_A)-3m(f_A).
Then

    Delta_A<log(170/A),
    hence Delta_A<=log(170/A).

In particular Delta_A<0 for every integer A>=171, and it is eventually below every fixed real number as A tends to infinity.
The result disproves nonnegative full phase balance on all primitive irreducible monic unit seeds, while the coefficient height and m(f_A)>log A grow.

More generally, for any nonzero integer polynomial f of actual degree k with nonzero G_f as above and r=f*/f on the circle where defined,

    log2+m(G_f)-3m(f)
        =integral_circle log|r(z)^2+r(z^2)| dmu,
    m(G_f)<=3m(f).

Every logarithmic singularity is integrable and the equality holds almost everywhere, without a Fourier or limiting interchange.
The proof preserves the factor2 and uses Haar invariance under z->z^2.
No irreducibility, monicity, one-expanding-pair or favorable cofactor assertion about G_A is needed.
The family is not the height-one trinomial pilot class or a positive near-one Salem sequence.
A delayed-Salem-family energy limit is not assumed for these seeds.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:31 |
| status | open |
| reason | Retain the complete unbounded-A cubic negative-phase construction, every exact root/unit/cancellation/integral proof and all height/measure/factor/family-transfer limits. Actual complete current whole self-check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete cubic negative-phase theorem](#statement) | Entire original D42 statement and equations(1)--(5) for every integer A>=2: explicit primitive irreducible monic cubic unit and all three disjoint simple real-root intervals/unique negative exterior root/A<tau<A+1/exact measure, actual-degree reversal and A-independent f+f*=t+t^2, full cubic cancellation and85A^2 unit-circle bound including division by2, every auxiliary factor/leading coefficient in Mahler measure, strict bound implying stated non-strict Delta<=log(170/A)/A>=171 negativity/divergence, general nonzero integer f and nonzero G integrable rational circle identity and universal upper bound, and growing-height/measure/nontrinomial/no-Salem-family-transfer/no-one-factor/near-one limits. |
| argument | [Entire original elementary proof](#argument) | Entire original D42 statement and equations(1)--(5) for every integer A>=2: explicit primitive irreducible monic cubic unit and all three disjoint simple real-root intervals/unique negative exterior root/A<tau<A+1/exact measure, actual-degree reversal and A-independent f+f*=t+t^2, full cubic cancellation and85A^2 unit-circle bound including division by2, every auxiliary factor/leading coefficient in Mahler measure, strict bound implying stated non-strict Delta<=log(170/A)/A>=171 negativity/divergence, general nonzero integer f and nonzero G integrable rational circle identity and universal upper bound, and growing-height/measure/nontrinomial/no-Salem-family-transfer/no-one-factor/near-one limits. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:34 |
| status | proved |
| reason | Adopt after actual whole current self-check of every unbounded-A root/unit/cancellation/circle/Mahler/integral step and the complete negative-sign/divergence conclusion. Preserve growing height/measure, every auxiliary factor/leading coefficient and exact no-family-transfer limits. No substantive defect or missing hypothesis was found; the current whole SELF does not close the original whole UNKNOWN arrangement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire original D42 statement and equations(1)--(5) for every integer A>=2: explicit primitive irreducible monic cubic unit and all three disjoint simple real-root intervals/unique negative exterior root/A<tau<A+1/exact measure, actual-degree reversal and A-independent f+f*=t+t^2, full cubic cancellation and85A^2 unit-circle bound including division by2, every auxiliary factor/leading coefficient in Mahler measure, strict bound implying stated non-strict Delta<=log(170/A)/A>=171 negativity/divergence, general nonzero integer f and nonzero G integrable rational circle identity and universal upper bound, and growing-height/measure/nontrinomial/no-Salem-family-transfer/no-one-factor/near-one limits. |
| argument | [Exact retained argument](#argument) | Entire original D42 statement and equations(1)--(5) for every integer A>=2: explicit primitive irreducible monic cubic unit and all three disjoint simple real-root intervals/unique negative exterior root/A<tau<A+1/exact measure, actual-degree reversal and A-independent f+f*=t+t^2, full cubic cancellation and85A^2 unit-circle bound including division by2, every auxiliary factor/leading coefficient in Mahler measure, strict bound implying stated non-strict Delta<=log(170/A)/A>=171 negativity/divergence, general nonzero integer f and nonzero G integrable rational circle identity and universal upper bound, and growing-height/measure/nontrinomial/no-Salem-family-transfer/no-one-factor/near-one limits. |
| review | [Complete actual current whole self finding](../audits/reviews/Yin_R_G0615_v1.md#current-negative-cubic-phase-finding) | Entire original D42 statement and equations(1)--(5) for every integer A>=2: explicit primitive irreducible monic cubic unit and all three disjoint simple real-root intervals/unique negative exterior root/A<tau<A+1/exact measure, actual-degree reversal and A-independent f+f*=t+t^2, full cubic cancellation and85A^2 unit-circle bound including division by2, every auxiliary factor/leading coefficient in Mahler measure, strict bound implying stated non-strict Delta<=log(170/A)/A>=171 negativity/divergence, general nonzero integer f and nonzero G integrable rational circle identity and universal upper bound, and growing-height/measure/nontrinomial/no-Salem-family-transfer/no-one-factor/near-one limits. Actual whole relationship is self-reviewed; all original complete noncontributor UNKNOWN and known author SELF scopes remain separately retained. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:20 |
| status | proved |
| reason | Adopt the new isolated entire negative cubic phase finding, covering every original integer A>=2 root/unit/irreducibility and 85A² cancellation cost, full general phase identity and every growing-height/family/near-one limit; original whole UNKNOWN and author SELF remain historical. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original D42 statement and equations(1)--(5) for every integer A>=2: explicit primitive irreducible monic cubic unit and all three disjoint simple real-root intervals/unique negative exterior root/A<tau<A+1/exact measure, actual-degree reversal and A-independent f+f*=t+t^2, full cubic cancellation and85A^2 unit-circle bound including division by2, every auxiliary factor/leading coefficient in Mahler measure, strict bound implying stated non-strict Delta<=log(170/A)/A>=171 negativity/divergence, general nonzero integer f and nonzero G integrable rational circle identity and universal upper bound, and growing-height/measure/nontrinomial/no-Salem-family-transfer/no-one-factor/near-one limits. |
| argument | [Complete selected argument](#argument) | Entire original D42 statement and equations(1)--(5) for every integer A>=2: explicit primitive irreducible monic cubic unit and all three disjoint simple real-root intervals/unique negative exterior root/A<tau<A+1/exact measure, actual-degree reversal and A-independent f+f*=t+t^2, full cubic cancellation and85A^2 unit-circle bound including division by2, every auxiliary factor/leading coefficient in Mahler measure, strict bound implying stated non-strict Delta<=log(170/A)/A>=171 negativity/divergence, general nonzero integer f and nonzero G integrable rational circle identity and universal upper bound, and growing-height/measure/nontrinomial/no-Salem-family-transfer/no-one-factor/near-one limits. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0625_v1.md#whole-negative-cubic-phase-finding) | Entire original D42 statement and equations(1)--(5) for every integer A>=2: explicit primitive irreducible monic cubic unit and all three disjoint simple real-root intervals/unique negative exterior root/A<tau<A+1/exact measure, actual-degree reversal and A-independent f+f*=t+t^2, full cubic cancellation and85A^2 unit-circle bound including division by2, every auxiliary factor/leading coefficient in Mahler measure, strict bound implying stated non-strict Delta<=log(170/A)/A>=171 negativity/divergence, general nonzero integer f and nonzero G integrable rational circle identity and universal upper bound, and growing-height/measure/nontrinomial/no-Salem-family-transfer/no-one-factor/near-one limits. The entire precise current Statement and Argument, with the corresponding original whole scope and every retained negative/source/nonexecution boundary, are independently reviewed in this new finding. Old UNKNOWN/SELF findings remain historical. |

## Complete retained argument

<a id="argument"></a>

<a id="retained-negative-phase-control"></a>

<a id="negative-doubling-phase-balance"></a>
### Statement and exact seed geometry

For an integer A>=2, put

    f_A(t)=t^3+A t^2+(1-A)t-1,
    f_A*(t)=t^3 f_A(1/t),
    G_A=[(f_A*)^2 f_A(t^2)+f_A^2 f_A*(t^2)]/2.

The polynomial G_A is a nonzero integer polynomial by the Frobenius parity identity and the direct value G_A(1)=1.
The seed is monic with constant coefficient -1 and is irreducible: its only possible rational roots are +/-1, whereas f_A(1)=1 and f_A(-1)=2A-3 are nonzero.
It is consequently a primitive irreducible algebraic-unit input of fixed degree three.

All its roots are real, with one in each of

    (-A-1,-A),       (-1,0),       (0,1).

Indeed f_A(-A-1)=-2A-3<0, f_A(-A)=A^2-A-1>0, f_A(-1)=2A-3>0, f_A(0)=-1 and f_A(1)=1.
The three disjoint sign changes already account for its entire degree.
Thus exactly one root lies outside the unit circle; if its modulus is tau_A then

    A<tau_A<A+1,          m(f_A)=log(tau_A)>log A.       (1)

This is a negative exterior root.
Neither it nor the resulting auxiliary is declared to be a positive near-one Salem input.

Let m denote the usual logarithmic Mahler measure, including the leading coefficient for a nonmonic polynomial, and define the exact total phase balance

    Delta_A=log2+m(G_A)-3m(f_A).

Then

    Delta_A<=log(170/A).                               (2)

In particular Delta_A<0 for every integer A>=171, and Delta_A tends to minus infinity in the sense that it is eventually below every fixed real number.
This disproves a nonnegative phase-balance assertion over all primitive irreducible monic unit seeds.
It says nothing against such a statement on a genuinely smaller specified seed class.

### Direct quadratic-size bound for the numerator

The key is the exact relation

    f_A+f_A*=u,             u(t)=t+t^2,

whose right side is independent of A.
Write f=f_A, f_2=f_A(t^2), u_2=u(t^2).
The numerator of G_A becomes

    (f*)^2 f_2+f^2 f*(t^2)
       =(-f+u)^2 f_2+f^2(-f_2+u_2)
       =-2f u f_2+u^2 f_2+f^2 u_2.                   (3)

The order-A^3 part has cancelled exactly.
On the unit circle,

    |u|<=2, |u_2|<=2,
    |f|,|f_2|<=3+2A<=5A.

With F=3+2A, equation(3) gives

    |G_A|<=3F^2+2F<=85A^2,             A>=1.

Jensen's integral definition of Mahler measure therefore yields

    m(G_A)<=log(85A^2).                               (4)

Combine (4) with (1) to obtain Delta_A<log2+log85+2log A-3log A=log(170/A).
The weaker non-strict version in(2) is retained for convenience.
The upper bound tending to minus infinity is sufficient for the stated divergence; no root approximation for G_A is needed.

### Why this is the actual full circle-phase balance

The general direct identity also clarifies the scope of this control.
For any nonzero integer f for which G_f is nonzero, and away from its finitely many circle zeros, let r(z)=f*(z)/f(z).
Then |r(z)|=1 on the circle and

    G_f(z)=[f(z)^2 f(z^2)/2] [r(z)^2+r(z^2)].

All logarithmic singularities are integrable because the rational expression is nonzero.
Integrating and using that z->z^2 preserves normalized Haar measure gives

    log2+m(G_f)-3m(f)
       = integral_(|z|=1) log|r(z)^2+r(z^2)| dmu(z).    (5)

In particular this is a full circle integral; selecting positive Fourier modes would not determine its sign.
The same identity and |r(z)^2+r(z^2)|<=2 give the general upper bound m(G_f)<=3m(f), consistently with (4).
The root-free unit circle for f_A has already been proved by its real-root intervals, although the integrable identity does not need that stronger condition.

For the plastic seed, the retained [complete plastic arithmetic analysis](Yin_C_G0409_v1.md#complete-plastic-mixed-energy-limit) identifies its positive balance with the complete normalized mixed energy of a specific delayed Salem family.
No corresponding family-limit theorem is being assumed for f_A here.
Equation(5) is the directly defined total phase balance itself.
Its negative sign does not refute the existing positive plastic-family result, nor supply a near-one counterexample: m(f_A)>log A grows without bound.
The auxiliaries G_A need not be irreducible or have only one expanding pair, and all their factors and leading coefficients remain in (2)--(5).

## Actual contributions and exact comparison boundary

The original coordinator's complete author contribution and actual whole self-check are retained in L175/R74.
The original final noncontributor review checked the entire written proof without computation and found no mathematical defect, with its actual initial-context unknown boundary unchanged.
The independent-looking words in that historical account do not supply an isolated current whole finding.

The earlier [complete trinomial and exact finite account](Yin_C_G0412_v1.md#sparse-trinomial-auxiliary) supplied the motivating positive observations, without a certified general lower sign.
The [complete special plastic analysis](Yin_C_G0409_v1.md#complete-plastic-mixed-energy-limit) separately identifies a positive phase balance and energy limit for its own delayed Salem family.
Neither observation is a proof premise here, and no corresponding family-limit theorem is transferred to f_A.
Every auxiliary factor and leading coefficient remains charged in the direct circle supremum/Mahler bound.
The negative balance comes with growing coefficient height and measure and supplies no positive near-one example, height-one trinomial refutation, favorable cofactor or uniform gap.
No native run, new source reading or Task execution occurs.
