---
author: Yin
---

# Both smaller-Mahler irreducible factors lose the full canonical residual precision

Human author Yin.
Provenance: project deduction under the unchanged [G0001 original contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the D=2,mu=17 factorization, own-divisor comparison and exact odd quotients for both factors; characteristic_zero_bridge checked every identity, root, full degree and measure and both complete canonical computations by hand.
Root read the complete updated PF1--PF4 argument and two-factor table.
Both agents are contributors; this open fixed candidate awaits fresh isolated whole review and a separate adoption decision.
No native polynomial scan or new source acquisition is used.

<a id="smaller-mahler-factor-loses-canonical-precision"></a>
## Statement

Use C_0=2,C_1=X,C_(j+1)=X C_j-C_(j-1), and the SAME actual canonical integer polynomials for each monic trace divisor T:

    a(T)=rem_T(T(C_2))/2,
    b(T)=rem_T(T(C_3))/3,
    c(T)=rem_T(T(C_5))/5,
    F(T)=rem_T(2c(T)^2-3a(T)^5),
    G(T)=rem_T(c(T)^3-2b(T)^5),
    X_s(T)=rem_T(b(T)^2-a(T)^3+s G(T)), s in{1,-1}.

Every displayed scalar division is taken in the integer coefficient module before reduction modulo2.
Write ord_2 for the minimum coefficient2-adic order, with ord_2(0)=infinity.
For a monic integer P, H(P) is its maximum absolute coefficient, S(P)=max_(|z|=1)|P(z)| is its true circle supremum, and m(P) is the complete sum of log max(1,|lambda|) over ALL original roots with multiplicity.

Let T_17=X^2-17X-2, P_17(z)=z^4-17z^3-17z+1, Q_fac(z)=z^4-3z^3-4z^2-3z+1, V=X^2-3X-6 and V_minus=X^2+3X-6.
Then P_17(z^2)=Q_fac(z)Q_fac(-z) is the COMPLETE rational factorization into two monic irreducible reciprocal integer polynomials of degree4, with respective traces V and V_minus.
The full product has trace T_17(C_2)=V(X)V(-X), of degree4, and full original degree8.
If beta_17 is the unique positive exterior root of P_17, then17<beta_17<18, the positive exterior root of Q_fac is sqrt(beta_17), and both factors have full logarithmic Mahler measure (1/2)log beta_17.
The complete product has full measure log beta_17.

For both residual signs, recomputation with each polynomial's OWN trace divisor gives these exact ordered triples (ord_2(F),ord_2(X_s),ord_2(G)):

    P_17(z^2), trace T_17(C_2): (11,9,15),
    Q_fac(z), trace V:          (0,0,11),
    Q_fac(-z), trace V_minus:   (5,3,11).

Consequently NEITHER smaller-measure irreducible factor preserves the full product's joint precision9: their actual joint precisions are0 and3.
All scalar divisions and canonical polynomials are retained in the complete proof below.
This is one explicit counterexample to automatic precision preservation under selection of a smaller-Mahler irreducible factor, not a statement about all factorizations or a near-one family.
The nonsquare-norm sufficient hypothesis for C729's irreducible towers is not extended to this norm-square point2(17+1)=36.

## Complete argument

Let

    T_17=X^2-17X-2,
    P_17(z)=z^4-17z^3-17z+1,
    Q_fac(z)=z^4-3z^3-4z^2-3z+1,
    V(X)=X^2-3X-6, V_minus(X)=V(-X)=X^2+3X-6.

Then the exact INTEGER identities are

    Q_fac(z)=z^2 V(z+z^(-1)),
    P_17(z^2)=Q_fac(z)Q_fac(-z),
    T_17(C_2)=V(X)V(-X)=X^4-21X^2+36.            (PF1)

Indeed the product of the two quartic factors is

    (z^4-4z^2+1)^2-9z^2(z^2+1)^2
                          =z^8-17z^6-17z^2+1.

Thus the nonsquare-norm hypothesis in C729 is not silently extended to mu=17, where2(mu+1)=36 is a square and this first dyadic pullback is actually reducible.
The example makes no claim that a square norm always forces reducibility.

The two trace roots of V are (3+sqrt33)/2>2 and (3-sqrt33)/2 in(-2,2).
Consequently Q_fac has one positive exterior root theta>1, its positive reciprocal and two nonreal unit-circle roots.
By PF1, theta^2 is an exterior positive root of P_17, hence equals its unique Salem root beta_17.
C729 gives the ACTUAL irreducibility of P_17 and deg_Q(beta_17)=4.
Therefore

    4=[Q(beta_17):Q]
       <=[Q(theta):Q]<=deg Q_fac=4,

so Q_fac is itself irreducible of degree4 and is the genuine Salem minimal polynomial of theta.
Its companion Q_fac(-z) is also irreducible by the invertible substitution z to-z and has the same root moduli.
All roots of the complete product are retained, and

    theta=sqrt(beta_17), 17<beta_17<18,
    m(Q_fac)=m(Q_fac(-z))=(1/2)log beta_17,
    m(P_17(z^2))=log beta_17.                    (PF2)

Thus choosing Q_fac really halves the positive total logarithmic Mahler measure by choosing a DIFFERENT irreducible original input; the complete product keeps its full measure.
This is a fixed positive-measure example, not a near-one family.

The canonical system must now be recomputed using the factor's OWN monic trace V.
One has

    V(C_2)=X^4-7X^2+4,
    X^2=3X+6 modulo V,
    X^4=63X+90 modulo V,
    rem_V V(C_2)=42X+52,
    a(V)=21X+26.                                 (PF3)

All these are integer identities or actual monic integer remainders, and the final scalar division is exact.
The corresponding own-divisor odd quotients can also be computed exactly without a coefficient scan.
In the V quotient the recurrence gives

    C_3=12X+18, C_5=209X+288,
    rem_V V(C_3)=828X+1128,
    rem_V V(C_5)=250800X+344160.

For example C_3^2=864X+1188 and C_5^2=251427X+345030 modulo V; subtracting3C_p+6 gives the displayed remainders.
After the legitimate integer divisions by3 and5 one obtains

    b(V)=276X+376=4(69X+94),
    c(V)=50160X+68832=16(3135X+4302).

The other factor has actual trace V_minus.
Direct division gives V_minus(C_2)=X^4-X^2-8 and a(V_minus)=-30X+38.
For odd p=3,5, C_p(-X)=-C_p(X), so V_minus(C_p(X))=V(C_p(-X)); substitution in the integer monic division by V gives the exact division by V_minus.
Thus its three actual quotients are

    a(V_minus)=-30X+38=2(-15X+19),
    b(V_minus)=-276X+376=4(-69X+94),
    c(V_minus)=-50160X+68832=16(-3135X+4302).      (PF4)

The binary trace U=Vbar=X^2+X is squarefree with COMPLETE roots0 and1.
Both C_3bar=X^3+X and C_5bar=X^5+X^3+X preserve this two-element set: C_3bar sends both roots to0, while C_5bar fixes both.
The exact integer quotients additionally show that both factors have ord_2(b)=2, ord_2(c)=4 and (b/4)bar=(c/16)bar=X.
For V, a has order0 with reduction X; for V_minus, a has order1 with (a/2)bar=X+1.
In the quotient by U, both X and X+1 are nonzero idempotents, so each of their positive powers remains itself.

For BOTH factors, the two terms of G=c^3-2b^5 have orders12 and11.
After division by2^11 the second term has nonzero reduction X, so each actual G has EXACT order11.
For V, the a^5 term of F and a^3 term of X_s are the unique terms of order0, both with nonzero reduction X.
For V_minus, the a^5 term has order5 against order9 for2c^2, so F has exact order5 with normalized reduction X+1.
The a^3 term of X_s has order3 against order4 for b^2 and order11 for G, so X_s has exact order3 with normalized reduction X+1.
These conclusions hold for both s=1,-1.

In contrast, mu=17=1+2^4 lies in C729's r=4,u=1 row, and exact covariance under C_2 gives the full-product row in the exact comparison:

| Original integer polynomial | Its OWN trace divisor | Full degree | Full logarithmic measure | ord_2(F) | ord_2(X_s), both signs | ord_2(G) | Exact joint precision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P_17(z^2) | T_17(C_2) | 8 | log beta_17 | 11 | 9 | 15 | 9 |
| Q_fac(z) | V | 4 | (1/2)log beta_17 | 0 | 0 | 11 | 0 |
| Q_fac(-z) | V_minus | 4 | (1/2)log beta_17 | 5 | 3 | 11 | 3 |

Both factors are irreducible, and PF1 is the complete factorization over Q.
Thus NEITHER smaller-measure irreducible factor preserves the full product's joint precision9 when the canonical system is recomputed with that factor's own trace divisor.
The full-product row concerns actual remainders for its degree4 TRACE divisor; the factor rows concern their respective degree2 trace divisors.
This is a complete explicit counterexample to automatic preservation of the SAME canonical residual precision when selecting a smaller-Mahler irreducible factor.
It makes no universal claim about factorization of other source families or about how much precision another factor choice might retain elsewhere.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision two-factor-precision-loss-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T18:11 |
| status | open |
| reason | Register the complete PF1--PF4 factorization, actual irreducibility/root/measure argument, every own-divisor canonical quotient and both-factor exact valuation table. Both irreducible factors halve the full positive measure but lose the product's joint precision9, to0 and3 respectively. No universal factorization obstruction or vanishing-Mahler conclusion follows. Both agents are contributors; fresh isolated whole review and a separate acceptance decision remain outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete two-factor precision-loss counterexample](#statement) | Exact integer factorization and distinct trace divisors, both irreducible full-degree factors, every root and total measure, both residual signs, all three exact F/X/G order rows and their joint precision, with the norm-square and generalization boundaries. |
| argument | [Complete PF1--PF4 and exact table proof](#complete-argument) | Direct factor multiplication, trace roots and degree inclusion proving each factor irreducible, all integer own-divisor a/b/c computations, nonzero binary idempotents and unique lowest terms, and the adopted full-product comparison with all measures retained. |
| dependency | [Adopted priced Chebyshev family and exact covariance](Yin_C_G0729_v1.md#decision-whole-reviewed-2026-10-25) | LC5 actual irreducibility/degree/root/measure at D=2,mu=17; the r=4,u=1 exact F/X/G orders11/9/15; and unconditional pure trace-composition covariance. The extra nonsquare-norm irreducibility theorem is not invoked at2(mu+1)=36. The two factor computations and all their actual orders are proved directly here. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T18:21 |
| status | proved |
| reason | Adopt the complete PF1--PF4 and exact two-factor table after the fresh independent whole two-factor finding in R952 passed. Root read the entire author proof, checked the fixed standalone statement and exact selected scope, and read the full independent finding. The complete rational factorization, actual irreducibility, all own-divisor integer quotients, both residual signs, exact orders and full root/measure accounting are supported. The full product has joint precision9; its two smaller-measure irreducible factors have joint precisions0 and3. This is one complete counterexample to automatic precision preservation under taking a smaller-Mahler factor, not a universal statement about all factorizations or a near-one family. C729 nonsquare-norm tower hypotheses are not imported at the norm-square point. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete two-factor precision-loss counterexample](#statement) | Exact integer factorization and distinct trace divisors, both irreducible full-degree factors, every root and total measure, both residual signs, all three exact F/X/G order rows and their joint precision, with the norm-square and generalization boundaries. |
| argument | [Complete PF1--PF4 and exact table proof](#complete-argument) | Direct factor multiplication, trace roots and degree inclusion proving each factor irreducible, all integer own-divisor a/b/c computations, nonzero binary idempotents and unique lowest terms, and the adopted full-product comparison with all measures retained. |
| dependency | [Adopted priced Chebyshev family and exact covariance](Yin_C_G0729_v1.md#decision-whole-reviewed-2026-10-25) | LC5 actual irreducibility/degree/root/measure at D=2,mu=17; the r=4,u=1 exact F/X/G orders11/9/15; and unconditional pure trace-composition covariance. The extra nonsquare-norm irreducibility theorem is not invoked at2(mu+1)=36. The two factor computations and all their actual orders are proved directly here. |
| review | [Fresh independent whole two-factor finding](../audits/reviews/Yin_R_G0952_v1.md#whole-two-factor-precision-loss-finding) | Entire fixed statement, PF1--PF4 and both-factor table, complete irreducibility/root/measure account, all own-divisor canonical divisions and exact orders for both signs, with the stated source and counterexample limits. |

