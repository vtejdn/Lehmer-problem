---
author: Yin
---
# Complete multiplicity-four complement classification and original branch exclusion

Human author Yin.
The same_trace contributor derived the exact six-representative classification, completed both coefficient cases and checked the original applicability and final contradiction.
Root requested an exact check of the endpoint-order and degree bounds and a complete remaining-complement analysis.
The proposed endpoint equality was not used: the current source gives only ord_X R_0>=A_0, while the COMPLETE complement has degree below2A_0.
The work continues under the [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
Focused reuse read the current C197 derivative proof, C199v3 UP8--UP9, C199v4 normalized gate/complement, the exact C199v5 QC9--QC13 finite cube calculation, C609v2's actual endpoint parity and adopted C621v2.
The new proof uses an exact degree-derived list of representatives, not a numerical scan or an arbitrary support/degree cutoff.
No new J, native calculation, higher coefficient search or external source theorem is used.
The result is initially open for a fresh isolated whole mathematical review.

## Statement

### Exact formal complement classification

Put phi=X^2+X+1, chi=Xphi^2 and Psi=phi(chi).
Let Y in F_2[X] be monic, prime to Xphi, with X^8 dividing Y'.
Let B in F_2[X] be monic, prime to phi, and satisfy

    deg B<8,
    ord_X B is even.

The constant B=1 is included among the initial possibilities.
Define the same local units

    H=X^4Y,
    C=X^4Y(chi)Psi^28

in F_2[X]_(phi).
Assume exactly the two congruences

    HB=C^3 modulo phi^8,
    H^6=C^21 modulo phi^16.                    (LC1)

Then necessarily

    B=X^6,
    Y=1+X^4 modulo X^8.                        (LC2)

This formal assertion does not assume that Y or B is a complete cyclotomic product, does not assume an original field realization, and imposes no bound on deg Y.
It does not identify a global square root of Y from a local congruence.
The precise even X-order hypothesis on B is used to eliminate two of six representatives; it is not an assertion that B is a square.
No equality ord_X(HB)=10 or lower bound ord_XB>=6 is assumed in (LC1); the conclusion supplies those orders only after the classification.

### Entire normalized multiplicity-four branch

Let P in Z[z] be monic irreducible reciprocal nontorsion, of degree d=2r and constant coefficient1.
For an original root alpha set delta=alpha+alpha^(-1), K=Q(alpha), and suppose F=Q(delta) is totally real.
Let T in Z[X] be the actual monic degree-r minimal polynomial of delta, so P(z)=z^rT(z+z^(-1)) and [K:F]=2.
Use C_p(z+z^(-1))=z^p+z^(-p) and the actual integral divided monic remainders

    theta_p=rem_T(T(C_p))/p, p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta).

Assume a,b,c are nonzero and, for one s in{1,-1},

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.

Put G=rem_T(theta_5^3-2theta_3^5), w=deg G<r, U=T mod2 and R_G=G mod2.
Assume the normalized circle Haar integral of log(G(z+z^(-1))^2), with the integrable logarithm at circle zeros, is0.
Assume also

    ord_phi R_G<ord_phi U,
    ord_psi R_G>=ord_psi U for every irreducible psi|U, psi!=phi.

Let q=2^k be the actual maximal power of2 for which U is a q-th power, and use C199's actual canonical U=U_0^q and R_G=R_0^q.
Set A_0=ord_X U/q.
Add ONLY A_0=4.
Use the actual unique complete monic complement B, whose existence, phi-unit property and strict bound deg B<8 follow from C199v4:

    H_0=U_0/phi^28=X^4Y,
    V_0=R_0/phi^24=H_0B.

There is no such original P,T and residual data.
This excludes the ENTIRE normalized A_0=4 branch at the stated original zero-Haar and unique-unsaturated domain, with every complete complement, every original q=2^k and arbitrary complete higher5 support retained.
It does not assume B=X^6 as an extra original hypothesis.

Combined with the independently adopted A_0=2 exclusion in C609v2 and inherited evenness, any remaining input on this exact domain must have even A_0>=6.
No power-of-two restriction on A_0 is introduced.
Multiple unsaturated factors, positive Haar, other normalized multiplicities, other original domains and the unrestricted G0001 objective remain outside this exclusion.
No original input, Gamma-modulo8 match, smaller field or new actual quotient construction is supplied.

## Argument

### What the current endpoint and complement bounds actually say

The original C199v3 [UP8--UP9 proof](Yin_C_G0199_v3.md#unique-quadratic-unsaturated-frobenius-parity) retains

    M_X=ord_X R_0>=A_0,

and explicitly states that no equality at X is used.
Thus an equality5A_0/2 or an initial restriction to X^6 and X^6(X+1) is not an available input for this classification.
The [complete C199v4 complement](Yin_C_G0199_v4.md#normalized-low-degree-complement) includes every saturated-factor surplus and every extra factor, and gives exactly deg B<2A_0.
At A_0=4 the strict degree bound is8.
The proof below starts with all polynomials at that exact bound, including constant and low-X-order possibilities.

### The gate projection reduces to an exact cube equation

Because Y(0)=1 and X^8 divides Y', write

    Y=1+uX^2+vX^4+wX^6 modulo X^8,
    u,v,w in F_2.                              (LC3)

All four odd coefficients below degree8 vanish, since their derivatives would have X-order below8.
Define the actual polynomial

    Q=X^2Psi^14(1+u chi+v chi^2+w chi^3).

The omitted Y coefficients become multiples of chi^8 and hence of phi^16.
Squaring the displayed expression gives exactly

    C=Q^2 modulo phi^16.                       (LC4)

The first congruence in (LC1), raised to the sixth power, gives H^6B^6=C^18 modulo phi^16.
Indeed the nonzero powers of an error E in (A+E)^6-A^6 are2,4,6, so an order-eight error becomes order at least16.
Combining with the second congruence and canceling the unit C^18 yields B^6C^3=1 modulo phi^16.
By (LC4) this is (BQ)^6=1 modulo phi^16.
In the polynomial/local ring, a square has twice the phi-order of its base, including the infinite-order case.
Therefore

    (BQ)^3=1 modulo phi^8.                     (LC5)

This is an exact order implication, not cancellation of an arbitrary square in a nonreduced quotient.

### Coefficient field and the complete six representatives

In S=F_2[X]/phi^8 put p=phi and

    beta=X+p+p^2+p^4.

Then beta^2+beta+1=0, beta'=0 and

    S=F_4[p]/p^8,
    X=beta+p+p^2+p^4.

The displayed substitutions generate both rings and both have dimension16 over F_2, proving the identification.
A unit with cube1 in S is one of the three constants1,beta,beta^2.
For a unit c(1+h), c in F_4^*, h in pS, the least nonzero term of h+h^2+h^3 cannot cancel, so (1+h)^3=1 forces h=0.
Consequently (LC5) means BQ=gamma for some gamma in{1,beta,beta^2}.

Reduce first modulo phi^4.
Since Psi^14=1 modulo phi^4 and chi^2 has order4,

    Q=X^2(1+u chi) modulo phi^4,
    B=gamma(X^(-2)+u X^(-1)phi^2)
                                        modulo phi^4.          (LC6)

The modulus phi^4 has degree8.
Every class has exactly one polynomial representative of degree below8, so (LC6) determines the ACTUAL complete B, not merely a truncation of it.
In this quotient,

    beta=X^4,
    beta^2=X^4+1,
    X^(-2)=X^6+X^2,
    X^(-1)phi^2=X^7+X.

These follow directly from phi^4=X^8+X^4+1 and X^12=1; multiplication verifies each inverse identity.
The complete six possibilities are therefore

| u | gamma | Exact polynomial B | ord_X B |
| --- | --- | --- | --- |
| 0 | 1 | X^6+X^2 | 2 |
| 0 | beta | X^2 | 2 |
| 0 | beta^2 | X^6 | 6 |
| 1 | 1 | X^7+X^6+X^2+X | 1 |
| 1 | beta | X^7+X^5+X^3+X^2=X^2(1+chi) | 2 |
| 1 | beta^2 | X^6+X^5+X^3+X | 1 |

This table is obtained by one exact inverse and the three constants, not by a coefficient enumeration.
The assumed even X-order eliminates the first and third u=1 rows.
It does not eliminate or assume away any u=0 row.
In particular X^6(X+1) is not among the representatives forced by (LC6).

### The u=0 case reduces to the fixed small cube calculation

For u=0, every remaining B is globally a square, so write

    B=E^2,
    E in{X^3+X,X,X^3}.

Differentiating BQ=gamma modulo phi^8 is legitimate because (phi^8)'=0 and gamma'=0.
Since B'=0, while

    Q'=w X^2Psi^14 chi^2 chi',
    chi'=phi^2,

a nonzero w would give the derivative exact phi-order6; B, X and Psi are units at phi.
That contradicts divisibility by phi^8.
Thus w=0.
The remaining Q is the exact square [X Psi^7(1+v chi)]^2, so (LC5) gives

    [E X Psi^7(1+v chi)]^3=1 modulo phi^4.      (LC7)

This is precisely the formal finite cube calculation retained in C199v5 QC9--QC13, with its small polynomial called E here and its coefficient y_2 called v.
No original A_0=2 input, actual field or already-excluded branch is imported into that formal calculation.
For completeness the entire three-case algebra is displayed next.

In F_2[X]/phi^4 one has X=beta+p+p^2, X^4=beta and X^2=beta^2+p^2.
Put h=1+v.
Then

    Psi^7(1+v Xp^2)=1+h beta p^2+h p^3
                                             modulo p^4.

For W=E X Psi^7(1+v chi), the three exact expansions are

    E=X^3+X:
       W=1+(1+h beta)p^2+h p^3;
    E=X:
       W=beta^2+(1+h)p^2+h beta^2 p^3;
    E=X^3:
       W=beta+h beta^2 p^2+h beta p^3.

The cube-one condition says W is a coefficient-field constant.
In all three rows its p^3 coefficient first forces h=0.
At h=0, the first two rows still have a nonzero p^2 coefficient and the third is the constant beta.
Thus exactly E=X^3 and v=1 survive.
Together with u=0,w=0 this gives B=X^6 and Y=1+X^4 modulo X^8.

### The sole even-order u=1 representative fails at depth eight

For u=1 the sole parity survivor is B=X^2(1+chi), corresponding to gamma=beta.
Modulo phi^8, Psi^14=1+chi^2.
Multiplying the exact expressions for B and Q gives

    BQ=X^4[1+v chi^2+(v+w)chi^3]
                                             modulo phi^8.

Here all chi^4 terms have order at least8 and are discarded at precisely that modulus.
In the coefficient-field coordinates above,

    X^4=beta+p^4,
    chi^2=beta^2p^4+p^6,
    chi^3=p^6+beta^2p^7
                                             modulo p^8.

The full product is therefore

    BQ=beta+(v+1)p^4+w beta p^6+(v+w)p^7
                                             modulo p^8.      (LC8)

For equality with the constant beta, the p^4 coefficient requires v=1 and the p^6 coefficient requires w=0.
The p^7 coefficient is then1, a contradiction.
Thus no u=1 case survives.
The six representatives are exhausted, proving the formal conclusion (LC2).

### Every formal hypothesis is supplied by the same original input

Assume now the entire original domain in the statement with A_0=4.
C199 supplies H_0=X^4Y, its actual full complement B and the exact bound deg B<8; both Y and B are phi-units and Y(0)=1.
The [C197v3 normalized odd-part bound](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) gives X^8 dividing W_U'.
Writing Y=J^2W_U with J(0)=1 gives X^8 dividing Y'.
This uses the actual T-support odd part; it does not identify it with the G-unit odd part before the complement is determined.

The [C609v2 actual parity conclusion](Yin_C_G0609_v2.md#statement) gives ord_XB even on this complete original domain.
Its proof uses the complete actual V_0 factorization, not an assumption that Y alone has complete order groups.
Thus no completeness of Y is required before B is classified.

The original five-layer weight is sum_b a_b lambda_b=24q, with lambda_0=lambda_1=1 and lambda_b=2^(b-1) for b>=2.
In C199's normalized window8q<lambda_b<24q the sole possible power is16q, at the original index b=k+5.
Hence the actual correction is

    S_star=epsilon X^8(X+1)^16phi^8,
    epsilon=a_(k+5) mod2.

The factor (X+1)^16, actual original indices and both parity choices are retained, and no a_b is divided by q.
The full root/gate condition with Z_0 a unit therefore yields

    V_0=H_0B=C_00^3 modulo phi^8.

Its exact old support condition is H_0^6=C_00^21 modulo phi^16, with C_00=X^4Y(chi)Psi^28.
These are precisely (LC1) for the SAME H_0,C_00,B,Y.
All hypotheses of the formal classification have now been checked, so the actual COMPLETE complement must equal X^6.
In particular the endpoint order10 is a consequence of the argument, not an input borrowed from a different theorem.

### Exact adopted obstruction and the remaining normalized range

The [adopted C621v2 statement](Yin_C_G0621_v2.md#statement) excludes the ENTIRE original A_0=4,B=X^6 subbranch, with all higher5 complete orders and every allowed original q.
Its complete original hypotheses are exactly those in the current statement, and the sole additional B hypothesis was just proved.
Applying that fixed theorem gives the contradiction and excludes every actual normalized A_0=4 input on this domain.
Its already reviewed J126 all-order certificate is used only through the exact fixed C621v2 theorem; it was not expanded or rerun.
The same original q, fields, monic T, complete canonical remainder and original integer layers persist throughout.
No local jet was used to infer a maximal global Frobenius power or a smaller original realization.

C199's inherited A_0 is even and at least2.
C609v2 already excludes the complete A_0=2 branch, and the present result excludes4, so any remaining normalized multiplicity on this exact domain is even and at least6.
The facts do not restrict A_0 to powers of2, and no next-multiplicity or larger-support search follows from this bounded result.
The original Task remains unresolved outside the exact exclusions stated here.

## Reuse and review boundary

The actual C197/C199 bounds were read before deriving the representative list.
The lower order M_X>=A_0 was retained in its correct direction, and every surplus/extra factor remains within the full degree of B.
The u=0 finite calculation is reused at its exact explicit algebraic scope from C199v5 and is reproduced here to make the new substitution and precision inspectable.
The u=1 exclusion is the new complete depth-eight expansion (LC8).
The formal classification is a separate algebraic statement from C621's whole-group image theorem; the latter supplies only the final original contradiction.
No native calculation or external-source claim was introduced.
Neither the current contributor nor the root proposer independently reviews this work; previous fixed review relationships remain at their actual scopes.
A fresh isolated whole review must inspect the formal hypotheses, all six representatives, both depth cases, every original applicability step and the exact final C621v2 use before adoption.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T18:53 |
| status | open |
| reason | Register the complete analytic degree-below8 complement classification under the exact parity/derivative/two-gate hypotheses, and its application excluding the entire original normalized A_0=4 branch via adopted C621v2. All six representatives, square-root precision, original q and layers, complete B costs and remaining even A_0>=6 boundary are retained. The new proof awaits a fresh isolated whole review; no unrestricted Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete formal and original theorem](#statement) | Every monic B of degree below8 satisfying the explicit formal hypotheses, arbitrary Y degree, exact B=X^6 conclusion and complete actual A_0=4 exclusion for every original q. |
| argument | [Entire analytic proof](#argument) | Correct original bounds, local square/cube reduction, all six exact representatives, parity elimination, both depth checks and every same-original-input hypothesis before the final contradiction. |
| dependency | [Complete actual normalized gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Actual H_0/C_00/V_0, original q/five-layer window and exact unit-root/gate/old-support precision, retaining the full correction factor. |
| dependency | [Complete complement and degree bound](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Actual unique monic B includes all surplus/extra factors and has degree below2A_0; no endpoint equality is assumed. |
| dependency | [Original T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | Exact QX17--QX20 under maximal normalization, giving the low-X derivative order8 for W_U and then Y at A_0=4. |
| dependency | [Actual complete complement parity](Yin_C_G0609_v2.md#statement) | Even ord_XB on the full original zero-Haar/unique-unsaturated domain, plus the already proved A_0=2 exclusion for the final remaining-range statement. |
| dependency | [Entire monomial-complement obstruction](Yin_C_G0621_v2.md#statement) | Exact complete original A_0=4,B=X^6 nonexistence for every q and all complete higher5 orders; used only after B=X^6 is derived. |
| dependency | [Original domain and inherited evenness](Yin_C_G0199_v5.md#statement) | Full original P/T/field/residual/Haar/unsaturation hypotheses, canonical normalization and even A_0>=2; no A_0=2 original input is substituted. |
| support | [Correct original endpoint inequality](Yin_C_G0199_v3.md#unique-quadratic-unsaturated-frobenius-parity) | UP8--UP9 only give M_X>=A_0 and explicitly use no equality at X; this guards the classification's actual starting scope. |
| support | [Exact smaller formal cube calculation](Yin_C_G0199_v5.md#normalized-a2-exact-complement) | Only QC9--QC13's explicit finite polynomial/cube algebra, with small polynomial E and coefficient v here; its proof is reproduced and no original A_0=2 realization is imported. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T19:03 |
| status | proved |
| reason | Adopt the complete formal complement classification and entire original normalized A_0=4 exclusion through isolated whole R829 after main reading of the full fixed C/R. Every degree-below8 complement is included; parity, local precision, all six representatives and exact original hypotheses are checked before invoking C621v2. The remaining range on this exact zero-Haar/unique-unsaturated domain is even A_0>=6, not only powers of2. Other domains and the unrestricted Task remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete formal and original theorem](#statement) | Every monic B of degree below8 satisfying the explicit formal hypotheses, arbitrary Y degree, exact B=X^6 conclusion and complete actual A_0=4 exclusion for every original q. |
| argument | [Entire analytic proof](#argument) | Correct original bounds, local square/cube reduction, all six exact representatives, parity elimination, both depth checks and every same-original-input hypothesis before the final contradiction. |
| dependency | [Complete actual normalized gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Actual H_0/C_00/V_0, original q/five-layer window and exact unit-root/gate/old-support precision, retaining the full correction factor. |
| dependency | [Complete complement and degree bound](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Actual unique monic B includes all surplus/extra factors and has degree below2A_0; no endpoint equality is assumed. |
| dependency | [Original T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | Exact QX17--QX20 under maximal normalization, giving the low-X derivative order8 for W_U and then Y at A_0=4. |
| dependency | [Actual complete complement parity](Yin_C_G0609_v2.md#statement) | Even ord_XB on the full original zero-Haar/unique-unsaturated domain, plus the already proved A_0=2 exclusion for the final remaining-range statement. |
| dependency | [Entire monomial-complement obstruction](Yin_C_G0621_v2.md#statement) | Exact complete original A_0=4,B=X^6 nonexistence for every q and all complete higher5 orders; used only after B=X^6 is derived. |
| dependency | [Original domain and inherited evenness](Yin_C_G0199_v5.md#statement) | Full original P/T/field/residual/Haar/unsaturation hypotheses, canonical normalization and even A_0>=2; no A_0=2 original input is substituted. |
| support | [Correct original endpoint inequality](Yin_C_G0199_v3.md#unique-quadratic-unsaturated-frobenius-parity) | UP8--UP9 only give M_X>=A_0 and explicitly use no equality at X; this guards the classification's actual starting scope. |
| support | [Exact smaller formal cube calculation](Yin_C_G0199_v5.md#normalized-a2-exact-complement) | Only QC9--QC13's explicit finite polynomial/cube algebra, with small polynomial E and coefficient v here; its proof is reproduced and no original A_0=2 realization is imported. |
| review | [Independent whole multiplicity-four complement finding](../audits/reviews/Yin_R_G0829_v1.md#whole-a4-complement-classification-finding) | Entire fixed statement and analytic proof, every formal representative and depth case, actual parity/gate/degree source interface and final C621v2 application; all prior source/native and SELF/UNKNOWN boundaries remain unchanged. |

