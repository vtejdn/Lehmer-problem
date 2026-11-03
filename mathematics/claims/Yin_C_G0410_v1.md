---
author: Yin
---

# Complete reciprocal-unit factor universality for the doubling auxiliary

The complete original D39 final statement and Sections1--5 are retained from [L174](../ledger/Yin_L_G0174_v1.md#retained-doubling-universality-argument).
The coordinator supplied the general construction, all evaluations, nonvanishing/reciprocal-degree proof and normalized height boundary, and explicitly self-checked the complete proof at the original day precision.
That actual [whole author check](../audits/reviews/Yin_R_G0073_v1.md#doubling-universality-original-author-check-finding) and the separately assigned [whole noncontributor account](../audits/reviews/Yin_R_G0073_v1.md#doubling-auxiliary-universality-independent-review) have different relationships.
The latter's actual initial target context is not established and remains unknown.
The original special plastic observation motivated this question; its older retained first-identity provenance is not a new novelty claim.
The original unnormalized numerator2tL versus normalized G_f=tL clarification was made before the final old whole review, without a mathematical proof change.
The later L38/L139 comparison remains explicitly outside that earlier review.
No new source or computation is needed.

## Statement

Let P in Z[t] be monic, reciprocal, irreducible and nontorsion, of degree d with P(0)=1, where t^d P(1/t)=P(t) and no root is a root of unity.
These hypotheses force even d>=2.
There is an explicitly constructed integer seed f of actual degree1<=k<=2d+1 such that

    f*(t)=t^k f(1/t),
    G_f(t)=((f*(t))^2 f(t^2)+f(t)^2 f*(t^2))/2

is a nonzero integer polynomial divisible by P in Z[t].
After removing its maximal monomial factor t^ell, G_f/t^ell is reciprocal of actual degree4k-2ell<=8d+4 and still has P as a factor.
The seed and auxiliary need not be monic; a primitive seed can also be chosen.

Retain all multiplicities in Q(t)=product_i(t-alpha_i^2), where alpha_i are all d conjugates.
For the actual signed R=Res(P,Q), the existing full-resultant theorem gives R!=0 and |R|>=2^d.
Choose A,B in Z[t] of degrees less than d with AP+BQ=R by the integral Sylvester adjugate and put

    f=t BQ+(t^2-1)AP.

Then f=Rt mod P and f=R(t^2-1) mod Q.
Its exact four evaluations at alpha, alpha^(-1), alpha^2 and alpha^(-2), with reversal taken at its actual k even if f(0)=0, cancel the numerator of G_f at alpha.
Characteristic-two Frobenius makes the division by2 integral for every integer f.
The complete nonzero argument below excludes an identically vanishing auxiliary by the rational equation s(t^2)=s(t)^2, whose nonzero rational solutions are t^j, j in Z.

Write m=log M(P), H(f)=max_j|f_j| and ||f||_circle=max_(|z|=1)|f(z)|.
For the particular unnormalized representative above,

    H(f)>=2^d exp(-2d m)/(2d+2).

If P has a unit-circle conjugate, the bound improves to2^d/(2d+2).
This is a bound on the actual constructed polynomial after cancellations.
It is not invariant under removing its integer coefficient content c>0.
Indeed c divides R, D=R/c is a nonzero integer, f_0=f/c is primitive, and G_(f_0)=G_f/c^3 is again integral, nonzero and divisible by P with unchanged degree.
The analogous primitive bound replaces |R| by |D|; no exponential floor on D is established.

Factor occurrence in this nonlinear doubling-auxiliary class is therefore universal on exactly the stated domain.
The result supplies no favorable primitive height, cyclotomic complementary factor, small auxiliary/complementary Mahler measure, exclusion of alternative efficient seeds, or uniform gap.
The older half-degree linear delay encoding for even reciprocal cores of degree at least4 is a different auxiliary theorem and is compared separately below.

## Current assessment

[Selected decision](#decision-retained-registration)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:17 |
| status | open |
| reason | Retain the complete general doubling-auxiliary construction/nonzero/reciprocity/content proof and its exact degree/height/cost limits, with the original review and later-comparison boundaries distinct. Actual complete current whole self-check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete factor-universality and cost theorem](#statement) | Entire original final statement and Sections1--5 for every monic reciprocal irreducible nontorsion P with constant1: actual even d>=2/full squared-conjugate multiset and all multiplicities, integral Sylvester adjugate with signed resultant R/nonvanishing2^d floor, explicit degree<=2d+1 seed and all four evaluations with actual reversal/possible f(0)=0, characteristic-two integrality/monic Z divisibility, complete Laurent rational-functional-equation nonzero proof, formal length4k reversal and maximal-monomial removal/degree<=8d+4, specific unnormalized coefficient-height lower bound and circle refinement, exact content c divides R/primitive seed/cubic scaling with uncontrolled D=R/c and no Mahler/cofactor cost; later comparison to the distinct earlier linear delay encoding is explicitly separate from the old review scope. |
| argument | [Complete original direct proof and explicit comparison](#argument) | Entire original final statement and Sections1--5 for every monic reciprocal irreducible nontorsion P with constant1: actual even d>=2/full squared-conjugate multiset and all multiplicities, integral Sylvester adjugate with signed resultant R/nonvanishing2^d floor, explicit degree<=2d+1 seed and all four evaluations with actual reversal/possible f(0)=0, characteristic-two integrality/monic Z divisibility, complete Laurent rational-functional-equation nonzero proof, formal length4k reversal and maximal-monomial removal/degree<=8d+4, specific unnormalized coefficient-height lower bound and circle refinement, exact content c divides R/primitive seed/cubic scaling with uncontrolled D=R/c and no Mahler/cofactor cost; later comparison to the distinct earlier linear delay encoding is explicitly separate from the old review scope. |
| dependency | [Full-conjugate mixed-resultant theorem](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Only Q=product_i(t-alpha_i^2) with all actual conjugates/multiplicities, integer reciprocal degree d and the nonzero signed Res(P,Q) with abs(R)>=2^d on the exact irreducible nontorsion unit domain; no powered-degree-preservation or new source proof is used. |
| dependency | [Earlier complete linear delay encoding](Yin_C_G0345_v1.md#universal-half-degree-delay-encoding) | Only the separate comparison on reciprocal irreducible cores of even degree at least4: a linear delay t^N f+f* with the earlier monic coprime nonreciprocal half-degree seed and explicit coefficient cost is a different auxiliary, not an input needed for this nonlinear construction or a claim of first universality. |
| dependency | [Complete special plastic identity](Yin_C_G0409_v1.md#plastic-lehmer-resultant-reduction) | Only the exact older numerator h^2 f(z^2)+f^2 h(z^2)=2zL, hence normalized G_f=zL, as the disclosed motivating comparison; the general existence/nonzero/content proof is given locally and does not require the special family. |


## Complete retained argument

<a id="argument"></a>

<a id="retained-doubling-universality-argument"></a>

<a id="doubling-auxiliary-factor-universality"></a>
### Statement and scope

Let P in Z[t] be monic, reciprocal, irreducible and nontorsion, of degree d with constant coefficient1.
Here reciprocal means t^d P(1/t)=P(t), and nontorsion means its roots are not roots of unity.
These hypotheses force d to be even and at least2: a reciprocal odd-degree polynomial has -1 as a root, and no irreducible degree-one polynomial in the stated domain is nontorsion.
For any nonzero f in Z[t] of actual degree k, write f*(t)=t^k f(1/t), and define

    G_f(t)=[f*(t)^2 f(t^2)+f(t)^2 f*(t^2)]/2.             (1)

Then there is an explicitly constructed f of degree k<=2d+1 such that G_f is a nonzero integer polynomial, P divides G_f in Z[t], and deg G_f<=8d+4.
After removing its maximal monomial factor, G_f is reciprocal.
Neither f nor G_f is asserted to be monic or primitive.
No estimate making the complementary factor's Mahler measure small is supplied.

The division by2 in(1) is integral for every integer f, independently of the construction: modulo2 the identities f(t^2)=f(t)^2 and f*(t^2)=f*(t)^2 make the two numerator summands equal.
This is exactly the elementary Frobenius divisibility behind the normalization, not an extra norm-income theorem.

### 1. A full powered polynomial and an integral construction

Let alpha_1,...,alpha_d be all conjugates of a root alpha of P, and retain every multiplicity in

    Q(t)=product_(i=1)^d(t-alpha_i^2).

This is a monic reciprocal polynomial in Z[t] of degree d and constant coefficient1.
It need not be the minimal polynomial of alpha^2; no power-degree-preservation assumption is made.
The fixed nonzero full mixed resultant interface [complete full-resultant interface](Yin_C_G0231_v1.md#mixed-power-resultant-identities) gives

    R=Res(P,Q) != 0,              |R|>=2^d.               (2)

In particular P and Q are relatively prime over Q.
The integral Sylvester matrix has determinant R up to the harmless basis-order sign.
Applying its adjugate to the coefficient vector of the constant polynomial gives integer polynomials A,B of degrees less than d such that, after fixing that sign,

    A(t)P(t)+B(t)Q(t)=R.                                 (3)

This elementary adjugate statement can also be read as clearing denominators in the degree-bounded polynomial Bezout identity; the actual signed resultant, rather than an unspecified denominator, suffices.
Define

    f(t)=t B(t)Q(t)+(t^2-1) A(t)P(t).                    (4)

All coefficients are integral and deg f<=2d+1.
Reducing modulo the two polynomials gives

    f(t)=R t                  modulo P(t),
    f(t)=R(t^2-1)             modulo Q(t).               (5)

In particular f is nonzero, since f(alpha)=R alpha!=0.
It also has actual degree k>=1: a constant f would make alpha=f(alpha)/R rational, contradicting the irreducible degree d>=2.

### 2. Exact vanishing at the target factor

Reciprocity puts alpha^(-1) among the roots of P, while alpha^2 and alpha^(-2) are roots of Q.
Formula(5) therefore yields

    f(alpha)=R alpha,          f(alpha^(-1))=R alpha^(-1),
    f(alpha^2)=R(alpha^4-1),   f(alpha^(-2))=R(alpha^(-4)-1).

The actual degree k of f fixes its reversal, so

    f*(alpha)=R alpha^(k-1),
    f*(alpha^2)=-R alpha^(2k-4)(alpha^4-1).

Substituting these exact values in the numerator of(1) gives

    R^3 alpha^(2k-2)(alpha^4-1)
       -R^3 alpha^(2k-2)(alpha^4-1)=0.

Thus P divides G_f over Q.
Since P is monic and G_f has integer coefficients, monic polynomial division gives the divisibility in Z[t].
The values f(alpha^2) and f*(alpha^2) are also nonzero because alpha is nontorsion, although their nonvanishing is not needed for this cancellation itself.

### 3. The constructed auxiliary cannot vanish identically

For completeness, a vanishing polynomial in(1) would not constitute factor occurrence.
Suppose its numerator were identically zero and put

    r(t)=f*(t)/f(t),          s(t)=-r(t) in Q(t).

Then r(t^2)=-r(t)^2, or s(t^2)=s(t)^2.
Every nonzero rational function satisfying this equation is a monomial t^j with integer j.
Indeed, expand at zero as s(t)=c t^j(1+a t^l+...), where l>=1 is the first nonzero higher term if there is one.
Comparing leading coefficients gives c=c^2 and hence c=1.
If a first higher term existed, the right-hand side would have coefficient2a at degree l relative to its leading term, while the left-hand side has no such term because its first higher degree is2l.
This contradiction shows that the normalized Laurent expansion is exactly1, and rational identity then gives s=t^j.

Consequently r(t)=-t^j.
But the computed values at alpha give r(alpha)=alpha^(k-2).
Therefore alpha^(k-2-j)=-1.
If the exponent is zero this says1=-1; otherwise it makes alpha a root of unity.
Both are impossible.
Thus G_f is nonzero.

### 4. Reciprocal shape, cost boundary and consequence

Formal reversal at length4k gives

    t^(4k) G_f(1/t)=G_f(t).

If ell is the order of vanishing at zero, its actual degree is4k-ell.
Removing t^ell leaves a reciprocal polynomial of degree4k-2ell.
Since P(0)=1, P remains a factor after this removal.
The degree bound in the statement follows from k<=2d+1.

This is a factor-universality statement with a linear degree bound.
It does not realize P as the whole auxiliary, make its complementary factor cyclotomic, bound coefficient height favorably, or preserve small Mahler measure.
The construction uses a Bezout identity cleared by the full resultant R, whose absolute value already has the floor2^d.
The unnormalized representative does have the elementary height bound recorded next, but normalization can remove part of that scalar.
Neither fact precludes a more efficient representation.
The construction has no controlled Mahler-cost theorem.

In particular, the appearance of the original Lehmer polynomial in D38's fixed plastic calculation is mathematically concrete but occurrence somewhere in this auxiliary class alone cannot restrict the unrestricted reciprocal-unit problem: every target in that domain occurs.
A useful strengthened route would need an exact auxiliary identity with controlled cofactor measure or a restriction on the permitted seeds that is both restrictive and covers the target inputs.
D38's special fixed seed retains its much sharper exact factorization and full-energy interpretation; this general construction does not replace or weaken that calculation.

### 5. Coefficient height and its content-normalization boundary

Write m=log M(P), H(f)=max_j|f_j|, and ||f||_circle=max_(|z|=1)|f(z)|.
Choose a conjugate alpha with |alpha|>=1, which exists because the unit constant coefficient makes the product of all conjugate moduli one.
Since f(alpha)=R alpha and k>=1, the exterior polynomial bound gives

    ||f||_circle >= |R| |alpha|^(1-k)
                  >= |R| exp(-(k-1)m)
                  >= 2^d exp(-2d m).

The exterior bound follows by applying the maximum-modulus principle to z^k f(1/z) on the unit disk.
Also ||f||_circle<=(k+1)H(f), so for the specific unnormalized representative(4),

    H(f)>=2^d exp(-2d m)/(2d+2).                         (6)

If P has a unit-circle conjugate, direct evaluation there improves this to H(f)>=2^d/(2d+2).
This describes the constructed representative itself, after any cancellations of its coefficients, but it is not a scale-invariant height obstruction.

Indeed let c>0 be its integer coefficient content and let f_0=f/c be primitive.
Since alpha is an algebraic unit,

    R/c = f_0(alpha)/alpha

is both rational and an algebraic integer, so c divides R.
Put D=R/c, a nonzero integer.
Then f_0(alpha)=D alpha, f_0(alpha^2)=D(alpha^4-1), and G_(f_0)=G_f/c^3 remains a nonzero integer polynomial divisible by P.
Its degree is unchanged.
Thus the factor-universality statement can also use a primitive seed.
The elementary lower bound for that primitive seed replaces |R| by |D|; there is no conclusion here forcing |D| to retain the exponential floor2^d.
Such a conclusion cannot be obtained merely by dividing the resultant floor by an uncontrolled content.

Finally even a coefficient-height lower bound would not itself lower-bound Mahler measure or the complementary factor's measure.
Equation(6) is therefore a precise normalization/cost boundary, not a hidden proof of a gap or a prohibition on controlled alternative seeds.

## Later reuse comparison and actual original scope

The first plastic numerator identity was already retained in the complete family elimination table and was rediscovered by the arithmetic author.
That rediscovery was the actual original trigger, without a novelty claim.
For this fixed seed the unnormalized numerator is2zL and normalized G_f=zL, as in [the complete special reduction](Yin_C_G0409_v1.md#plastic-lehmer-resultant-reduction).
The general proof above uses only the full-resultant interface and its explicit local construction.

The earlier [complete half-degree delay encoding](Yin_C_G0345_v1.md#universal-half-degree-delay-encoding) covers reciprocal irreducible cores of even degree at least4 with a monic coprime nonreciprocal seed of half the core degree plus one and explicit coefficient costs.
Its auxiliary is linear t^N f+f*, distinct from this nonlinear G_f.
It already shows that an unrestricted seed presentation alone is not selective.
The present theorem gives the corresponding occurrence/content boundary for G_f, without replacing that older theorem, extending its domain to degree2, or claiming the first presentation-universality observation.
The original comparison was a subsequent reuse clarification outside the earlier D39 whole review; its original date/account remain in L174/R73.
The current whole check must include the explicit comparison as well as every proof step above.
No bound on primitive height, auxiliary/complementary Mahler cost or an effective gap follows from factor occurrence or the unnormalized coefficient-height inequality.
