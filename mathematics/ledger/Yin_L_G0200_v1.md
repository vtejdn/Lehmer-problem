---
author: Yin
---

# A saturated degree-six input with a principal cyclic control ideal

Date: 2026-10-10.

<a id="degree-six-principal-saturation-fixed-scope"></a>
## Adopted scope

The coordinating AI for Yin adopts its complete cross-route proof and resultant_research's separate complete noncontributor review.
The structural agent's discovery of the states and six-digit words in the concurrently reviewed L199 work is explicit reuse.
The new saturation, inverse, principal-ideal connection and exact trace-radius calculation are the coordinator's contribution.
The reviewer disclosed its earlier L197 contribution.

The actual irreducible degree-six Salem input P=t^6-t^5-t^3-t+1 saturates the full doubling resultant at2^6.
Its normalized full-order unit and inverse are explicit, and its actual control ideal is I=(beta^3-1)O=(1-beta^(-3))O with index4.
The compact candidates have the exact joint neutral squared radius z_+^2-1 in(3,4), and the displayed original words return them to zero.
This supplies a genuine common input for the saturation and control routes, and shows why the quartic saturation exclusion cannot extend unchanged to degree six.

The principal-ideal identities do not prove compact completeness or normalized hull coverage; those separate obligations are fixed in L199/J40.
The explicit inverse at this input is not a uniform coefficient bound, and bounded short cyclic norms supply no degree-linear income.

G0001 remains active and unresolved.
Historical pending-review language records the original chronology; the complete appended review determines the reviewed scope.
Only heading depth and relative navigation are transformed in the retained source below.

<a id="retained-degree-six-principal-proof"></a>
## The degree-six control ideal is principal in an actual saturated input

Date: 2026-10-10.
Direct cross-route observation by the coordinating AI for Yin.
The structural agent's D63/J40 discovery identified the three compact candidates0 and plus/minus(1-beta^(-3)); its exact compact enumeration and joint-hull proof remain that agent's separate work.
The coordinator independently derives the saturation, inverse and principal-ideal identities below from the fixed L183/L195 degree-six input.
This contribution is separate from D63's proof and pending its own complete noncontributor review.
No program or new external source is used.

<a id="degree-six-saturation-principal-control-ideal"></a>
### Exact identities and their scope

Let beta be the Salem root of

    P(t)=t^6-t^5-t^3-t+1,
    T(z)=z^3-z^2-3z+1,
    P(t)=t^3 T(t+t^(-1)).

Its irreducibility, Salem status and the outer trace z_+=beta+beta^(-1) in(2,sqrt5) are fixed in [L183](Yin_L_G0183_v1.md#fractional-module-five-class-obstruction).
The sharper beta interval(3/2,151/100) and actual ideal I=(2,beta^2+beta+1), with O/I=F4 and [O:I]=4, are fixed in [L195](Yin_L_G0195_v1.md#four-state-real-overlap-entry).
Set O=Z[beta].

Write z_1,z_2,z_3 for all roots of T.
Their elementary symmetric functions are1,-3,-1.
The squared roots therefore have symmetric functions7,11,1.
Subtracting2 from all three squared roots gives symmetric functions1,-5,-1.
Thus the full doubled trace polynomial and full powered polynomial are

    U(z)=product_j(z-(z_j^2-2))=z^3-z^2-5z+1=T(z)-2z,
    Q(t)=P^[2](t)=t^3 U(t+t^(-1))
         =P(t)-2(t^4+t^2).                                  (1)

These retain all original inverse pairs and multiplicities.
Direct trace evaluation gives

    Res(T,U)=product_j(-2z_j)=8,
    Res(P,Q)=Res(T,U)^2=64=2^6.                             (2)

The second identity is the retained full trace-resultant identity in [L66](Yin_L_G0066_v1.md#reciprocal-mixed-resultant-square).
This is an actual nontorsion degree-six saturated input, so the new [L197 quartic exclusion](Yin_L_G0197_v1.md#quartic-saturation-torsion-only) cannot extend unchanged to degree six.

The normalized full-order element and its inverse are also explicit:

    W(beta)=(Q(beta)-P(beta))/2=-beta^3 z_+,
    W(beta)^(-1)=beta^(-3)(z_+^2-z_+-3) in O.                (3)

Indeed T(z_+)=0 gives z_+^(-1)=-z_+^2+z_++3, and beta is an algebraic unit.
Multiplication verifies (3) directly.
The trace norm of z is-1 and its full norm is one, in agreement with saturation.
This identifies a concrete inverse, not a uniform coefficient bound for varying inputs.

The control ideal in L195 is principal:

    I=(beta^3-1)O=aO,
    a=1-beta^(-3)=-1-beta-2beta^2+beta^5.                    (4)

To prove the first equality, the quotient map beta to b in F4 has b^3=1, so(beta^3-1)O is contained in I.
Its index in the actual power-basis order is the absolute determinant of multiplication by beta^3-1, namely its absolute field norm.
Since T(2)=-1 and T(-1)=2,

    |Norm(beta^3-1)|=|T(2)| T(-1)^2=4.

Both ideals thus have index4, proving equality without assuming O is a maximal order.
Multiplication by the unit beta^(-3) proves I=aO.
Reducing beta^3(-1-beta-2beta^2+beta^5) with P gives beta^3-1, verifying the integral expression for a.

The two candidate states plus/minus a really lie in the narrow domain and have a small neutral radius.
At the expanding embedding0<a_+<1.
At the stable embedding a_-=1-beta^3, whose absolute value is less than(151/100)^3-1<5/2.
Also S=beta/(beta-1)>(151/100)/(51/100)=151/51>5/2, so |a_-|<S.
For the two unit-circle pairs, let z_1,z_2 be their real traces and define rho(a)^2 as in L195.
Then

    rho(a)^2=sum_(j=1)^2[2-(z_j^3-3z_j)]
            =6-(z_1^2+z_2^2)
            =z_+^2-1 in(3,4).                              (5)

Here T(z_j)=0 gives z_j^3-3z_j=z_j^2-1 and the full square sum is7.
Thus both nonzero states have rho<2, in particular below5/2.
This proves their inclusion directly, not completeness of the compact slice.

Finally P(beta)=0 gives

    beta^6 a=beta^6-beta^3=beta^5+beta-1.

The original six-digit word(-1,0,0,0,-1,1) therefore returns a exactly to zero; its negation returns-a.
The state and return identification were communicated by the structural agent in its D63 work; they are explicitly reused here.
The new contribution is the complete saturation, inverse and principal-ideal connection, together with the exact trace-radius calculation.

### Limits and checking

The coordinator checked the three elementary-symmetric calculations, all resultant signs, the actual inverse, equality of finite-index ideals, integral expression for a, narrow real/stable bounds, the full two-pair neutral norm, and the exact return identity.
This is proof-only work with no new numerical evidence.
A separate review is pending.

Neither(4) nor(5) proves that0 and plus/minus a exhaust the compact ideal slice; that needs D63/J40's separate complete enumeration.
Nor does a known principal ideal by itself provide a normalized control hull or compact termination.
Conversely this exact cross-route identification does not turn the bounded short cyclic norms into degree-linear income, control inverses uniformly in the full saturated class, or prove a Mahler gap.
It supplies one actual shared arithmetic/control input and preserves all independent certificate obligations.
G0001 remains active and unresolved.



The original `Yin_R_G0099_v1#degree-six-principal-ideal-independent-review` checked this complete proof at2026-10-10 day precision; [the later full comparison](../audits/reviews/Yin_R_G0697_v1.md#l200-and-r99) preserves its actual original inputs, verdict, UNKNOWN relationship, contribution and source/nonexecution limits.

## Retention and review bindings

The original complete separate review applied to the entire [retained argument](#retained-degree-six-principal-proof) and its stated reused interfaces; [its later full comparison](../audits/reviews/Yin_R_G0697_v1.md#l200-and-r99) retains that historical scope without backdating a later review as the original adoption input.
Its contribution disclosures and all limits remain part of this fixed record.

The complete D G0067 proof and the substantive history of its original noncontributor finding remain at their declared scopes in this record and the linked full comparison.
Fixed proof retention does not complete the Task.
