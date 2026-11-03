---
author: Yin
---

# Exact canonical cofactor transfer and residual precision compatibility

Human author Yin.
The [selected G0001 continuation](../tasks/Yin_T_G0001_v1.md#decision-resume-after-account-handoff-2026-10-25) authorizes this work.
Provenance: direct integer polynomial deduction and consuming comparison with the adopted fixed materials below.
Root proposed the general divided-remainder identity, its actual quotient-bracket proof and the three cofactor weights for the adopted C732 example.
Salem_completion checked the full integer proof and endpoints, derived the weighted residual and precision-defect interfaces, and checked every displayed example product by direct quotient-ring arithmetic.
Both are contributors, not independent reviewers.
A bounded search of current fixed G Claims found the generic dyadic product rule in [C196v3](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification), and the different additive Witt-count factor identity in [C223](Yin_C_G0223_v1.md#statement), but no complete cofactor-weight interface for the present canonical residual system.
The relevant accepted comparison is [C732's full two-factor counterexample](Yin_C_G0732_v1.md#decision-whole-reviewed-2026-10-25); its PF3--PF4 own-divisor values and complete precision scope were read.
C729's exact dyadic-composition mechanism and quotient formulas were checked only for the displayed product comparison, not as a new irreducibility or Mahler premise.
No native polynomial scan, external theorem or new independent review is used.

## Statement

### FT1. Exact domain and canonical factor identity

Let A,B be arbitrary MONIC polynomials in Z[X], of any nonnegative degrees, and let T=AB.
Use

    C_2=X^2-2, C_3=X^3-3X,
    C_5=X^5-5X^3+5X.

For P=A,B,T and p in{2,3,5}, define the ACTUAL integer monic quotient and divided remainder by

    P(C_p)=P Q_p(P)+p theta_p(P),
    theta_p(P)=rem_P(P(C_p))/p.

The divisibility by p is proved in FT2 before any reduction modulo p.
For P=1 set its remainder equal to0, so theta_p(1)=0 and Q_p(1)=1.
Let R_A=Z[X]/(A), and use square brackets for its actual quotient map.
Then the EXACT identity is

    [theta_p(T)]=[B(C_p)] [theta_p(A)] in R_A,
                                      p=2,3,5.          (FT1)

Equivalently there is an actual integer L_p with

    theta_p(T)-B(C_p)theta_p(A)=A L_p.            (FT2)

There is no coprimality, squarefreeness, irreducibility, field, root-location or nonzero-constant-term assumption.
Repeated and shared factors are retained.
Every composition B(C_p) is formed as a full integer polynomial before reduction; it is not an endomorphism of an arbitrary quotient class.

Monic constant factors are exactly1: B=1 gives the identical canonical system, while A=1 gives the zero quotient and a vacuous identity.
The zero polynomial is not monic and is excluded, so no negative polynomial degree is an input; the zero remainder may have degree minus infinity by the usual convention.
All other coefficients, including constant coefficients, may have either sign or be zero.
Both residual signs s=1 and s=-1 are treated below without choosing one implicitly.

The same identity also holds for factors with leading coefficient-1 if their canonical remainders are defined by division with that unit leading coefficient.
For the sign-normalized pair(-A,-B) the product T is unchanged, theta_p(-A)=-theta_p(A) and(-B)(C_p)=-B(C_p), so the product in FT1 is unchanged.
This does NOT identify the own residuals of A and-A: their odd and even powers transform as stated in FT3.
No extension to a nonunit leading coefficient or a nonunit constant polynomial is asserted.

## Complete argument

### FT2. Actual integer division, including common factors

For each of the three primes C_p=X^p modulo p, and Frobenius on F_p[X] gives P(C_p)=P^p modulo p for every integer P.
Monic division commutes with coefficient reduction, so the canonical remainder is a coefficientwise p-multiple and

    Q_p(P)=P^(p-1) modulo p.                     (FT3)

This includes P=1.
Subtract the two ACTUAL identities for A and T:

    p[theta_p(T)-B(C_p)theta_p(A)]
             =A[Q_p(A)B(C_p)-B Q_p(T)].          (FT4)

By FT3 the bracket on the right has reduction

    A^(p-1)B^p-B(AB)^(p-1)=0 modulo p.

Thus the bracket is coefficientwise divisible by p in Z[X]; define its genuine integer quotient to be L_p.
Cancel p in the INTEGER polynomial identity FT4 to obtain FT2.
No division by p in F_p[X], in a modular quotient or in a ring with p-torsion has occurred.
A and B may have any common factors because this calculation does not cancel either of them.

For comparison with the retained dyadic product rule, put

    Delta_p(P)=(P(C_p)-P^p)/p in Z[X].

The same Frobenius congruence proves integrality, and monic division gives theta_p(P)=rem_P Delta_p(P).
The EXACT product identity is

    Delta_p(AB)=B(C_p)Delta_p(A)+A^pDelta_p(B).

Reducing this integer identity modulo A gives a second proof of FT1.
For p=2, reduction of this identity modulo2 gives the earlier C196v3 product rule; that retained elementary mechanism is not claimed newly discovered here.
The present interface keeps the actual integer cofactor weight and all three canonical primes.

As a concrete repeated-factor consequence, for every integer r>=1,

    [theta_p(A^r)]=p^(r-1)[theta_p(A)]^r in R_A.  (FT5)

Indeed take B=A^(r-1) and use[A(C_p)]=p[theta_p(A)] before raising it to r-1.
This statement is only in the factor quotient R_A, not an assertion of equality in the larger quotient by A^r.
It exhibits directly how shared factors can hide canonical precision.

### FT3. The full weighted residual system

In R_A put

    alpha=[theta_2(A)], beta=[theta_3(A)],
    gamma=[theta_5(A)],
    u=[B(C_2)], v=[B(C_3)], w=[B(C_5)].

For any monic P use its OWN canonical polynomials

    a(P)=theta_2(P), b(P)=theta_3(P), c(P)=theta_5(P),
    F(P)=rem_P(2c(P)^2-3a(P)^5),
    G(P)=rem_P(c(P)^3-2b(P)^5),
    X_s(P)=rem_P(b(P)^2-a(P)^3+s G(P)).

Since A divides T, taking a T-remainder and then reducing modulo A has the same result as reducing the original polynomial modulo A.
Thus FT1 proves the complete EXACT weighted equations

    [F(T)]=2w^2gamma^2-3u^5alpha^5,
    [G(T)]=w^3gamma^3-2v^5beta^5,
    [X_s(T)]=v^2beta^2-u^3alpha^3
                         +s(w^3gamma^3-2v^5beta^5). (FT6)

These are identities in the ordinary integral factor quotient, even when that quotient has zero divisors.
They are not the unweighted equations for A unless the required cofactor compatibility is supplied.
They are also different from pure trace-composition covariance, which changes the divisor by composition rather than choosing a factor.

For either sign the following exact defect form is often more useful:

    [F(T)]=u^5[F(A)]+D_F,
    D_F=2(w^2-u^5)gamma^2,

    [G(T)]=w^3[G(A)]+D_G,
    D_G=2(w^3-v^5)beta^5,

    [X_s(T)]=v^2[X_s(A)]+D_X,
    D_X=(v^2-u^3)alpha^3+s(w^3-v^2)gamma^3
                                      +2s(v^2-v^5)beta^5. (FT7)

Every coefficient2 and3 is retained; none is canceled when a later coefficient ring makes it a nonunit.
For the optional sign normalization A->-A, one has

    F(-A)=2gamma^2+3alpha^5,
    G(-A)=-G(A),
    X_s(-A)=beta^2+alpha^3-sG(A) in R_A.

Thus changing a factor's sign is not an unexplained preservation of its own residuals, although FT1 itself is compatible with the two simultaneous factor signs.

### FT4. Exact precision-descent criteria and sufficient unit weights

Fix an integer modulus N>=2 and work in R_(A,N)=(Z/NZ)[X]/(A modN).
For A of positive degree, the monic coefficient basis1,X,...,X^(degA-1) shows that F(A),G(A),X_s(A) are coefficientwise divisible by N exactly when their respective classes vanish in R_(A,N).
For A=1 this condition is vacuous.
The precision N=1 is trivial, and a negative modulus gives the same ideal as its absolute value.
In particular all dyadic precisions N=2^n with n>=1 are covered.

Suppose the product has the corresponding coefficientwise residual divisibility.
If u is a unit, FT7 gives the exact equivalence

    F(A)=0 modulo N  iff  D_F=0 in R_(A,N).

If w is a unit, the analogous statement for G holds with D_G.
If v is a unit, the analogous statement for X_s holds with D_X.
For example, when F(T) and X_s(T) both vanish modulo N and u,v are units, the factor has the SAME joint precision modulo N if and only if BOTH actual defects D_F,D_X vanish in the factor quotient.
This is an actual-triple criterion, not a condition imposed on freely chosen alpha,beta,gamma.
If a required weight is a nonunit, these cancellations are unavailable and the exact equations FT6--FT7 must be used without canceling it.

A transparent SUFFICIENT compatibility is the existence of a unit eta in R_(A,N) such that

    u=eta^2, v=eta^3, w=eta^5, eta^9=1.           (FT8)

Then

    [F(T)]=eta^10[F(A)],
    [G(T)]=eta^15[G(A)],
    [X_s(T)]=eta^6[X_s(A)] in R_(A,N),            (FT9)

because eta^15=eta^6.
All three multipliers are units, so product residual vanishing gives the corresponding own-factor residual vanishing at the SAME modulus, for either residual sign.
The particularly simple case u=v=w=1 is included.
These sufficient weight equations are NOT asserted necessary: the actual defects may vanish because of the actual canonical values or coefficient torsion without the full equations FT8.
The same exact equations in R_A itself transfer characteristic-zero zeros if their multipliers are units there; no source family with those extra properties is presumed.

For completeness a weight[B(C_p)] is a unit in R_(A,N) exactly when

    gcd(A mod ell, B(C_p) mod ell)=1
                      for every prime ell dividing N. (FT10)

Modulo ell this is the polynomial Bezout criterion in F_ell[X].
An inverse lifts from ell to ell^e because the ideal(ell) is nilpotent in the latter finite coefficient ring; a finite geometric sum in the error constructs the inverse.
The integer Chinese remainder theorem combines these inverses over the distinct prime powers dividing N.
Conversely every unit remains a unit on each such reduction, proving necessity.
For dyadic N it suffices to check the single full polynomial gcd modulo2, retaining repeated factors.

Even coprimality of A and B does not directly check FT10: the cofactor is evaluated at C_p.
For example A=X-1 and B=X are coprime already over Z, but B(C_3)=-2 in R_A=Z, which is not a unit modulo2^n for n>=1.
Unitness, when available, enables the displayed cancellations; the separate weight defects still have to be checked rather than omitted.
This theorem claims no reverse implication from a condition in one factor quotient to global product residual precision.

<a id="ft5-exact-cofactor-weights-in-the-adopted-c769-example"></a>
### FT5. Exact cofactor weights in the adopted C732 example

Take

    A=V=X^2-3X-6,
    B=V_minus=X^2+3X-6,
    T=AB=X^4-21X^2+36.

In R_A, X^2=3X+6, and C732 supplies the actual own-divisor values

    alpha=21X+26,
    beta=276X+376,
    gamma=50160X+68832.

The three full composition reductions are

    C_2=3X+4, C_3=12X+18, C_5=209X+288 modulo A.

Their squares at the same divisor give the exact cofactor weights

    u=B(C_2)=60X+76,
    v=B(C_3)=900X+1236,
    w=B(C_5)=252054X+345888 modulo A.             (FT11)

For example C_3^2=864X+1188 and C_5^2=251427X+345030; adding3C_p-6 gives v and w.
The direct integer products and subsequent monic reduction are

| Canonical product class | Exact representative modulo A | Exact coefficient2-adic order |
| --- | --- | --- |
| u alpha=[a(T)] | 6936X+9536 | 3 |
| v beta=[b(T)] | 1424736X+1955136 | 5 |
| w gamma=[c(T)] | 72628208928X+99666334656 | 5 |

These products recover the full-product canonical classes, not the factor's own canonical values.
As a second direct algebraic comparison within this proof, put Z=X for the base divisor T_17=Z^2-17Z-2.
Its actual quotient-ring values are C_2=17Z, C_3=288Z+34 and C_5=83809Z+9792.
Substituting into T_17(C_p) and performing its actual prime divisions gives

    a(T_17)=2312Z+288,
    b(T_17)=474912Z+55488,
    c(T_17)=24209402976Z+2828722752.

Pure composition by C_2 gives the ACTUAL full-product canonical polynomials

    a(T)=2312X^2-4336,
    b(T)=474912X^2-894336,
    c(T)=24209402976X^2-45590083200.               (FT12)

Indeed C_p(C_2)=C_2(C_p), substitution in the actual T_17 division gives a division by T_17(C_2)=T, and the composed remainder has degree<4; the scalar division is unchanged.
Reducing FT12 by A gives exactly the three representatives in the table, verifying the weights without a polynomial scan.

The weights have respective exact orders2,2,1, so none is a dyadic unit.
Modulo Abar=X^2+X one has the nonzero orthogonal idempotents X and X+1:

    alpha_bar=X,
    (beta/4)bar=(gamma/16)bar=X,
    (u/4)bar=(v/4)bar=X+1, (w/2)bar=X.

Thus the first two products gain an EXTRA bit from X(X+1)=0; the third has no such extra bit because X^2=X is nonzero.
Their displayed integer coefficients establish the exact orders3,5,5, not only lower bounds.
The entire product has the adopted C732 residual orders11,9,15 for F,X_s,G, whereas the own V system has0,0,11 and the own V_minus system has5,3,11.
The weighted identities explain the mechanism without altering those accepted root, degree or measure statements.
Exchanging A and B is covered by the same general theorem; no coprimality or irreducibility is used for this algebraic interface.

### FT6. What this interface supplies and does not supply

The factor's OWN canonical system is recovered from the product only with its actual cofactor weights and the required precision defects or sufficient unit compatibility.
A factor may have lower Mahler measure while these weights are nonunits or its defects are nonzero; C732 already supplies a complete instance of precision loss.
The present theorem neither asserts that every factor loses precision nor that a useful compatible factor always exists.
It supplies an exact integral test that can be applied to a specified factor and cofactor at a specified modulus, including shared factors and both residual signs.
It gives no arbitrary irreducible-factor selection theorem, no degree-uniform Mahler bound and no unrestricted G0001 conclusion.
This complete author theorem awaits fresh independent whole review; no adoption is supplied by the contributor checks.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision canonical-cofactor-transfer-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T18:38 |
| status | open |
| reason | Register the complete exact integer cofactor identity for all three canonical primes, all weighted residual and actual-defect precision interfaces, sufficient unit compatibility and exact modular unit criterion, repeated-factor identity, constant/sign/common-factor endpoints and the complete C732 weight/product comparison. Every prime division is performed on actual integer coefficients before reduction. Root and Salem_completion are contributors; fresh independent whole review remains outstanding. No automatic factor-precision transfer, compatible factor selection, universal factor obstruction, Mahler bound or unrestricted G0001 conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete cofactor-transfer statement](#statement) | FT1--FT2 exact identity for arbitrary monic A,B, including constants, common/repeated factors and the explicitly qualified signed-leading extension; FT5 repeated powers, FT6--FT10 weighted/defect/unit precision consequences and FT11--FT12 actual C732 comparison are fully stated and proved in FT2--FT5. |
| argument | [Complete integer and precision proof](#complete-argument) | Entire FT2--FT6: actual p-divisible quotient bracket, integral Delta_p product identity, genuine monic factor reduction, every F/G/X weight and defect, actual-triple iff under units, sufficient eta9 compatibility, modular gcd/unit proof, repeated factors, exact example products/composition check and every scope boundary. |
| dependency | [Adopted actual two-factor counterexample](Yin_C_G0732_v1.md#decision-whole-reviewed-2026-10-25) | PF1--PF4 actual A=V and B=V_minus, own-divisor a/b/c and accepted full-product/factor F/X/G precision table. The new cofactor weights and all integer products are checked directly here. Root, irreducibility and measure facts are only the accepted comparison scope; no general factor-transfer statement is imported. |
| support | [Retained generic dyadic product rule](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Attribution/comparison ONLY: integral Delta_2, monic remainder compatibility and the generic product identity modulo2. Its specialized degree28, Hensel and other conclusions are not dependencies or asserted generalized here. |
| support | [Different retained Witt-count factor identity](Yin_C_G0223_v1.md#statement) | Reuse-search comparison ONLY: the additive b_(2g)(p)=-1-b_(2g)(H) interface concerns a different invariant and does not supply this canonical cofactor transfer. No graph, selected-factor, irreducibility or Mahler statement is a premise. |
| support | [Adopted exact quotient and pure-composition comparison](Yin_C_G0729_v1.md#decision-whole-reviewed-2026-10-25) | LC3/LC4 and pure C2 covariance were inspected only for the concrete T17/product comparison. All displayed low-degree quotient and composition arithmetic is rederived in FT5; no external root or irreducibility mechanism is a logical premise of the general theorem. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T18:51 |
| status | proved |
| reason | Adopt the entire FT1--FT6 canonical cofactor-transfer theorem after fresh isolated whole R956 PASS. Root read the complete integrated author argument, fixed statement and full independent finding. The actual integer p-divisible bracket and Delta_p proofs, all constant/sign/shared-factor endpoints, weighted residuals and exact defects, all-modulus unit equivalences and sufficient eta compatibility are supported. The repeated-factor identity and complete C732 cofactor products retain every actual division and exact coefficient order. C196v3 and C223 remain precisely scoped comparisons. The result provides conditional same-precision transfer, not arbitrary compatible-factor existence, automatic preservation under taking a smaller-Mahler factor, a reverse inference from one factor quotient or unrestricted G0001 completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete cofactor-transfer statement](#statement) | FT1--FT2 exact identity for arbitrary monic A,B, including constants, common/repeated factors and the explicitly qualified signed-leading extension; FT5 repeated powers, FT6--FT10 weighted/defect/unit precision consequences and FT11--FT12 actual C732 comparison are fully stated and proved in FT2--FT5. |
| argument | [Complete integer and precision proof](#complete-argument) | Entire FT2--FT6: actual p-divisible quotient bracket, integral Delta_p product identity, genuine monic factor reduction, every F/G/X weight and defect, actual-triple iff under units, sufficient eta9 compatibility, modular gcd/unit proof, repeated factors, exact example products/composition check and every scope boundary. |
| dependency | [Adopted actual two-factor counterexample](Yin_C_G0732_v1.md#decision-whole-reviewed-2026-10-25) | PF1--PF4 actual A=V and B=V_minus, own-divisor a/b/c and accepted full-product/factor F/X/G precision table. The new cofactor weights and all integer products are checked directly here. Root, irreducibility and measure facts are only the accepted comparison scope; no general factor-transfer statement is imported. |
| support | [Retained generic dyadic product rule](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Attribution/comparison ONLY: integral Delta_2, monic remainder compatibility and the generic product identity modulo2. Its specialized degree28, Hensel and other conclusions are not dependencies or asserted generalized here. |
| support | [Different retained Witt-count factor identity](Yin_C_G0223_v1.md#statement) | Reuse-search comparison ONLY: the additive b_(2g)(p)=-1-b_(2g)(H) interface concerns a different invariant and does not supply this canonical cofactor transfer. No graph, selected-factor, irreducibility or Mahler statement is a premise. |
| support | [Adopted exact quotient and pure-composition comparison](Yin_C_G0729_v1.md#decision-whole-reviewed-2026-10-25) | LC3/LC4 and pure C2 covariance were inspected only for the concrete T17/product comparison. All displayed low-degree quotient and composition arithmetic is rederived in FT5; no external root or irreducibility mechanism is a logical premise of the general theorem. |
| review | [Fresh independent whole cofactor-transfer finding](../audits/reviews/Yin_R_G0956_v1.md#whole-canonical-cofactor-transfer-finding) | Entire fixed statement, all FT1--FT12 and FT1--FT6 argument sections, actual integer quotient identities, every weighted/defect/unit endpoint, repeated factors and full example arithmetic, with exact source/comparison and existence limitations. |

