---
author: Yin
---

# Canonical residuals remain nonzero modulo two in an actual bounded-circle Chebyshev family

Human author Yin.
Provenance: project deduction under the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
The characteristic_zero_bridge agent developed BC1--BC8; root read the entire candidate and contributed to the denominator-free remainder and complete-root proof.
Both are contributors and neither supplies an independent review of this new result.
The existing actual Salem family and its source/acceptance boundaries remain those of C136, at the exact subfamily stated below.


The characteristic_zero_bridge agent selected the actual four-term family from [C136](Yin_C_G0136_v1.md#statement) after checking the existing controlled-height and same-source candidates.
Its actual [isolated whole adopted assessment](Yin_C_G0136_v1.md#decision-isolated-current-whole-review-20261022-m04) supplies the irreducible Salem interpretation ONLY on q=5^r, r>=1.
The new denominator-free canonical calculation below is valid for every D>=2 without any irreducibility premise.
Root checked and contributed to the complete Chebyshev remainder, consecutive-polynomial identity and root-closure argument; this is coauthor mathematics, not independent review.
No native computation, parameter scan or new external source is used.
The previous q=1 nonsquare case in [C672](Yin_C_G0672_v1.md#decision-whole-reviewed-2026-10-24) remains outside its square-input existence conclusion; nothing here decides all height1 sign lifts of C691's full fixed source.

<a id="bounded-circle-chebyshev-residual-discriminator"></a>
## Statement

For EVERY integer D>=2 define

    T_D(X)=C_D(X)-3C_(D-1)(X),
    P_D(z)=z^D T_D(z+z^(-1))
          =z^(2D)-3z^(2D-1)-3z+1,
    L=2D-1, U=T_D mod2.                           (BC1)

Use C_0=2,C_1=X,C_(j+1)=X C_j-C_(j-1), and the SAME actual integer canonical polynomials

    a=rem_(T_D)(T_D(C2))/2,
    b=rem_(T_D)(T_D(C3))/3,
    c=rem_(T_D)(T_D(C5))/5,
    F=rem_(T_D)(2c^2-3a^5),
    X_s=rem_(T_D)(b^2-a^3+s(c^3-2b^5)),
    G=rem_(T_D)(c^3-2b^5), s in{1,-1}.

Then U is a squarefree degree-D polynomial whose complete root set over the algebraic closure of F_2 is

    {zeta+zeta^(-1):zeta^L=1}.                    (BC2)

This set includes0 exactly once, from zeta=1, and includes every nonidentity root order dividing L, not just primitive roots.
In particular U=X V_L for a squarefree V_L with V_L(0)!=0.
The exact first canonical quotient and all binary reductions are

    a=rem_(T_D)(3C_(D-1)^2+2),
    abar=X, bbar=cbar=0,
    Fbar=rem_U(X^5)!=0,
    X_sbar=rem_U(X^3)!=0, Gbar=0.                 (BC3)

Write ord_2(R) for the minimum2-adic valuation among nonzero coefficients of an integer polynomial R, with ord_2(0)=infinity.
Consequently both actual residuals have EXACT coefficient2-adic order0, for each sign and every D>=2.
No member passes even the modulo2 residual gate, hence none passes modulo4 or8.
The conclusion Gbar=0 does not assert that the integer canonical G is zero.
Write H(P) for the maximum absolute coefficient, S(P)=max_(|z|=1)|P(z)| and m(P) for the complete logarithmic Mahler measure, with every root and multiplicity counted.
Then

    H(P_D)=3, S(P_D)=8,
    ord_2(T_D')=0.                               (BC4)

On the accepted actual C136 subfamily D=(5^r+1)/2, r>=1, P_D is irreducible and genuine Salem of FULL degree2D=5^r+1, and

    log3<m(P_D)<log4, m(P_D)->log3.              (BC5)

All root/field/nonzero-integrality interpretations on that subfamily are the actual original ones from C136; no factor, degree or measure is removed.
The measure is bounded and positive, not a sequence tending to zero.
The algebraic calculation for other D is not used to silently enlarge C136's irreducibility or Salem theorem.

For EVERY integer j>=0, set k=2^j and take the complete actual integer polynomials T_(D,k)=T_D(C_k), P_(D,k)=P_D(z^k), of degrees Dk and2Dk.
Their corresponding actual canonical polynomials satisfy

    ord_2(F_(D,k))=ord_2(X_(s,D,k))=0,
    G_(D,k)bar=0,
    H(P_(D,k))=3, S(P_(D,k))=8,
    m(P_(D,k))=m(P_D),
    ord_2(T_(D,k)')=j.

No irreducibility is asserted for these higher pullbacks; the unconditional identities concern the complete actual polynomials, with no factors removed.
For k>1 over the accepted C136 base the complete polynomial has exactly k exterior roots and is not a genuine Salem minimal polynomial as a whole.
This is an actual bounded-S, unbounded-derivative family whose residual precision remains0, not a nonexistence theorem for arbitrary controlled-height inputs or for the unrestricted G0001 objective.
The binary conclusion Gbar=0 prevents this family from realizing C691's required nonzero binary canonical G; height1 sign lifts of that different full source remain unresolved.

## Complete argument

### Complete proof of the squarefree trace domain

In characteristic2 the original reciprocal polynomial reduces to

    P_Dbar=(z+1)(z^L+1), L odd.

The polynomial z^L-1 has L distinct nonzero roots because its derivative is z^(L-1), which is nonzero at each such root.
For every one of these roots zeta, the actual trace identity gives U(zeta+zeta^(-1))=0.
Two nonzero elements have the same trace exactly when they are the two roots of the same quadratic z^2-Xz+1, so the trace fibers are inverse pairs, except at zeta=1.
In characteristic2 the equation zeta=zeta^(-1) forces zeta^2=1 and hence zeta=1; likewise trace0 occurs only there.
Thus the distinct trace values number1+(L-1)/2=D.
Since U is monic of degree D, these values exhaust its roots and all roots are simple, proving BC2 with every full factor retained.
For each p in{3,5}, raising any L-th root to its p-th power stays in that full root set, including when p divides L and some roots map to1.
Therefore C_p sends the entire trace-root set of U into itself.
This is why the0 trace cannot be discarded in the next division.

### Exact dyadic remainder before reduction, including the zero-trace primary

Set W=C_(D-1), so T_D=C_D-3W.
The exact integer identity C_j(C2)=C_j^2-2 gives

    T_D(C2)=C_D^2-3W^2+4
           =T_D(C_D+3W)+6W^2+4.                 (BC6)

Monic integer division is linear and commutes with multiplication by the integer2, so its actual remainder divided by2 is precisely the first formula in BC3.
No division inside a characteristic-two quotient is used.

The exact consecutive-polynomial identity is

    C_D^2+W^2-X C_D W=4-X^2.                     (BC7)

It follows by substituting X=z+z^(-1), expanding the Laurent expressions C_j=z^j+z^(-j), and using injectivity from the highest Laurent term.
At a binary root x of U one has C_D(x)=W(x), so BC7 reduces to

    x W(x)^2=x^2.

For x!=0 this gives W(x)^2=x.
At x=0, the recurrence gives C_j(0) even for every j>=0, so Wbar(0)=0 and Wbar(0)^2=0=x as well.
Thus no cancellation by X is made on the zero-trace component.
By the squarefreeness of U, Wbar^2=X in F_2[X]/U.
The canonical degree bounds and D>=2 identify the actual reduced polynomial abar with X, not just a chosen abstract value.

### Both odd canonical quotients and the nonzero residuals

Actual integrality of b and c follows from C_p=X^p modulo p and monic division, as in the accepted C697 canonical interface.
Because3 and5 are odd, reducing their actual divided remainders modulo2 gives

    bbar=rem_U(U(C3bar)),
    cbar=rem_U(U(C5bar)).

BC2's whole-root power closure and squarefreeness make both displayed remainders zero.
This holds even when p divides L; all roots mapping to trace0 were included.
Reduction of the SAME actual F, X_s and G now gives the remaining formulas in BC3, with no residual coordinate chosen independently.
There is a nonzero root of U because L>=3 supplies a nonidentity L-th root zeta and only zeta=1 has trace0.
At that root x, both x^3 and x^5 are nonzero.
Therefore neither canonical remainder rem_U X^3 nor rem_U X^5 is the zero polynomial, including at D=2.
This proves the exact coefficient orders and both signs.

### Exact circle bound, adopted actual Salem family, and pure pullbacks

The four coefficient positions of P_D are distinct for D>=2, so its height is3 and coefficient l1 sum is8.
The circle triangle bound gives S(P_D)<=8, while the exact value P_D(-1)=8 gives equality.
Squarefree U implies U'!=0, so T_D' has an odd coefficient and its exact coefficient2-adic order is0.
These arguments prove BC4 without a numerical maximization or source-height substitution.
C136 supplies BC5 at precisely its q=5^r original domain, including exact irreducibility, full degree, every root and positive total measure; no new source-proof inspection is claimed.

For every dyadic k=2^j>=1, one may also take the actual integer polynomials

    T_(D,k)=T_D(C_k), P_(D,k)=P_D(z^k).

The adopted [C697 exact covariance](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25), with G's explicit extension in [C724](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25), gives all the corresponding canonical compositions.
Their exact coefficient2-adic orders therefore satisfy

    ord_2(F_(D,k))=ord_2(X_(s,D,k))=0,
    G_(D,k)bar=0,
    H(P_(D,k))=3, S(P_(D,k))=8,
    m(P_(D,k))=m(P_D),
    ord_2(T_(D,k)')=j.                            (BC8)

Nonzero binary composition by X^k preserves the residual order0, while C724's exact trace-derivative formula and BC4 give the final equality.
The circle equality uses surjectivity of z->z^k, and the complete measure equality counts every k-th root in every original root fiber.
No irreducibility of these higher pullbacks is asserted; the unconditional statement is about the complete actual integer polynomials and canonical trace remainders.
For k>1 over a C136 base the complete polynomial has k exterior roots, so it is not a genuine Salem minimal polynomial as a whole.

Thus bounded TRUE S and unbounded derivative divisibility can coexist in actual polynomial inputs whose residual precision remains exactly0.
This is a concrete failure of this controlled-height family and its pure pullbacks, not a failure theorem for every small-height lift or for Lehmer's conjecture.
It lies outside C691's required nonzero binary canonical G and never supplies a compatible sign lift of that complete source.
The full C691 height1 sign-feasibility question remains unresolved; the closed square-input C672 result cannot be applied after descent to a nonsquare q1 base.


## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision bounded-circle-residual-discriminator-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T16:55 |
| status | open |
| reason | Register the complete BC1--BC8 actual-polynomial discriminator after contributor checking. Exact integer monic division and the full squarefree binary trace-root set give abar=X, bbar=cbar=0 and both actual residual coefficient orders exactly0 for every D>=2 and both signs. S=8 and height3 are exact; the original irreducible Salem/measure interpretation retains only C136's adopted subfamily. Every pure dyadic pullback preserves residual order0 and full measure while its exact trace-derivative order grows, without an irreducibility assertion for the higher polynomial. This is a complete bounded-family obstruction, not a sign-lift verdict on C691 or a general controlled-height/unrestricted-gap theorem. Fresh isolated whole review remains required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual bounded-circle statement](#statement) | BC1--BC5 and BC8, all generic D>=2 canonical algebra, both signs, zero/nonzero binary distinctions, full squarefree root set, exact H/S/derivative orders, precisely restricted actual Salem subfamily, every dyadic pullback and all original measure/degree/irreducibility limitations. |
| argument | [Complete BC1--BC8 proof](#complete-argument) | Whole characteristic-two inverse-pair count including trace0 and all proper root orders, exact integer dyadic remainder, consecutive Chebyshev identity without cancellation at X=0, both odd canonical divisions and power closures even when p divides2D-1, nonzero remainder witnesses, exact S=8, original source application and all pure-pullback costs. |
| dependency | [Adopted actual four-term Salem family](Yin_C_G0136_v1.md#decision-isolated-current-whole-review-20261022-m04) | Its original family/trace interface and Section1 only for q=5^r,r>=1: actual irreducibility, full degreeq+1, complete Salem root distribution and log3<m<log4 tending tolog3. No selected-prime5/3 coverage or new original-source proof claim is imported. |
| dependency | [Adopted integer canonical and composition interface](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) | Actual integrality of divided remainders and DP7 exact canonical a/b/c/F/X_s covariance under monic trace composition. The new abar/bbar/cbar and residual calculations are proved here for the stated family. |
| dependency | [Adopted complete G covariance and exact derivative loss](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Actual G monic-division covariance, preservation of exact coefficient2-adic order, full H/S/measure composition identities and HD8 exact trace-derivative loss; no height-controlled existence or passing-certificate input is imported. |
| support | [Full C691 source boundary](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | Comparison only: its full nonzero binary canonical R and separately chosen integer synthetic data; this Chebyshev family does not realize that source. |
| support | [Square-input modulo4 construction and its nonsquare limit](Yin_C_G0672_v1.md#decision-whole-reviewed-2026-10-24) | Comparison only: its q>=2 square-input existence theorem explicitly supplies no q1 nonsquare result, so it cannot decide height1 sign feasibility after an actual descent to that base. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T17:03 |
| status | proved |
| reason | Adopt the complete BC1--BC8 bounded-circle discriminator after reading the entire fixed theorem and fresh isolated whole R947. Actual integer division, full squarefree trace roots including zero and all proper orders, both signs and endpoints, exact residual orders0, height3 and S=8, derivative order and all complete pullback costs are supported. Irreducible Salem and positive-measure assertions retain only the exact adopted C136 subfamily; no higher pullback irreducibility is inferred. This is a specific actual-family failure, not a universal controlled-height obstruction, a C691 sign-lift verdict or G0001 completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual bounded-circle statement](#statement) | BC1--BC5 and BC8, all generic D>=2 canonical algebra, both signs, zero/nonzero binary distinctions, full squarefree root set, exact H/S/derivative orders, precisely restricted actual Salem subfamily, every dyadic pullback and all original measure/degree/irreducibility limitations. |
| argument | [Complete BC1--BC8 proof](#complete-argument) | Whole characteristic-two inverse-pair count including trace0 and all proper root orders, exact integer dyadic remainder, consecutive Chebyshev identity without cancellation at X=0, both odd canonical divisions and power closures even when p divides2D-1, nonzero remainder witnesses, exact S=8, original source application and all pure-pullback costs. |
| dependency | [Adopted actual four-term Salem family](Yin_C_G0136_v1.md#decision-isolated-current-whole-review-20261022-m04) | Its original family/trace interface and Section1 only for q=5^r,r>=1: actual irreducibility, full degreeq+1, complete Salem root distribution and log3<m<log4 tending tolog3. No selected-prime5/3 coverage or new original-source proof claim is imported. |
| dependency | [Adopted integer canonical and composition interface](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) | Actual integrality of divided remainders and DP7 exact canonical a/b/c/F/X_s covariance under monic trace composition. The new abar/bbar/cbar and residual calculations are proved here for the stated family. |
| dependency | [Adopted complete G covariance and exact derivative loss](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Actual G monic-division covariance, preservation of exact coefficient2-adic order, full H/S/measure composition identities and HD8 exact trace-derivative loss; no height-controlled existence or passing-certificate input is imported. |
| support | [Full C691 source boundary](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | Comparison only: its full nonzero binary canonical R and separately chosen integer synthetic data; this Chebyshev family does not realize that source. |
| support | [Square-input modulo4 construction and its nonsquare limit](Yin_C_G0672_v1.md#decision-whole-reviewed-2026-10-24) | Comparison only: its q>=2 square-input existence theorem explicitly supplies no q1 nonsquare result, so it cannot decide height1 sign feasibility after an actual descent to that base. |
| review | [Fresh isolated whole bounded-circle review](../audits/reviews/Yin_R_G0947_v1.md#whole-bounded-circle-residual-finding) | Independently reviewed entire fixed statement and complete proof, current open decision and consumed dependency/comparison scopes, including every D/prime/sign endpoint, source root/measure scope and all actual pullback limitations. |

