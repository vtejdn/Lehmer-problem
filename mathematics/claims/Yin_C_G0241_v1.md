---
author: Yin
---

# Exact prime-power repetition of unramified Frobenius quotients

This retains the complete original 2026-10-07 proof of [L64](../ledger/Yin_L_G0064_v1.md).
The additive construction covers nonunit integral components and p=2, while the stronger full primary-group conclusion keeps its precise unramified hypothesis.

## Statement

Let alpha be any nonzero nontorsion algebraic integer with monic minimal polynomial P of degree d>=1, integral companion A, R=Z[t]/P and Delta=abs(discP).
For every prime p and integer r>=1 put q=p^r, retain the full degree-d powered polynomial P^[q] with every original conjugate and multiplicity, and set

    R_(1,q)=Res(P,P^[q]),
    rho_q=rem_P(P(t^q))/p in Z[t],
    C_q=P(A^q)/p=rho_q(A).

These divided matrices are integral and nonsingular, and abs(det C_q)=abs(R_(1,q))/p^d.
No unit hypothesis, powered-degree preservation or replacement of d by a smaller powered degree is imposed.
If p does not divide Delta, write the distinct irreducible factors of P mod p with degrees f_i.
There are finite integers k_i>=1, independent of r, such that

    v_p(R_(1,p^r))=sum_i f_i k_i=v_p(R_(1,p)),
    (coker C_(p^r))[p^infinity]
        is isomorphic to direct_sum_i (Z/p^(k_i-1)Z)^(f_i).

Zero exponents give trivial groups; the unnormalized full Sylvester groups have exponents k_i instead.
The principal ideals rho_(p^r)(alpha)O and rho_p(alpha)O coincide componentwise in O=R tensor Z_p.
These are abstract finite-group and ideal conclusions, without canonical integral matrix conjugacy or any assertion about contributions at primes other than p.
The proof constructs every simple-root/idempotent Frobenius lift and its finite order directly, then proves the exact additive error valuation and congruence, including nonunit components and p=2.
Its derivative/Fermat-quotient test is stated additively when alpha is not a local unit.

For arbitrary primes, including p dividing Delta, the exact identity in the possibly nonreduced algebra F_p[t]/P is

    rho_(p^r)=rho_p^(p^(r-1)).

Thus v_p(R_(1,p^r))>d iff v_p(R_(1,p))>d for every r>=1.
If P mod p=product_j g_j^(e_j) and h_j is the multiplicity of g_j in rho_p mod p, with infinity for the zero polynomial, the first lifting nullity is

    sum_j deg(g_j) min(e_j,p^(r-1)h_j),

and v_p(R_(1,p^r)) is at least d plus this quantity.
This all-prime first-layer result does not identify full ramified valuations or full ramified primary groups.
No uniform arithmetic frequency, size, other-prime growth, entropy improvement or Lehmer gap is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:40 |
| status | open |
| reason | Register the complete original proof and its exact domains in a responsible Claim; actual full current review and any adoption follow separately. Old dated inputs and review accounts remain separate, with no new research, computation or original-source proof audit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complete statement](#statement) | All original unramified full-valuation/primary-group conclusions and separately guarded arbitrary-prime first-lifting/nullity bounds, nonunit and p=2 included. |
| argument | [Complete retained proof](#argument) | Entire original simple-root/idempotent lifting, finite-order Frobenius, additive recurrence, derivative interface, Smith-group proof and full all-prime binomial/gcd multiplicity proof with all remaining limits. |
| dependency | [Complete integral Sylvester and base quotient](Yin_C_G0237_v1.md#base-prime-power-extra-valuation) | Exact full-original-root nonvanishing, integral rho_q/P(A^q)/p, determinant p^d normalization and normalized Sylvester quotient, without a unit or powered-degree assumption. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:45 |
| status | proved |
| reason | Adopt the exact complete prime-repetition theorem after actual full current self-review of every local lifting, additive recurrence, nonunit/p2, Smith and arbitrary-prime nilpotent interface. The full unramified conclusion and weaker ramified first-layer scope remain separate; no other-prime growth, new research or independent-review claim is made. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All original unramified full-valuation/primary-group conclusions and separately guarded arbitrary-prime first-lifting/nullity bounds, nonunit and p=2 included. |
| argument | [Argument](#argument) | Entire original simple-root/idempotent lifting, finite-order Frobenius, additive recurrence, derivative interface, Smith-group proof and full all-prime binomial/gcd multiplicity proof with all remaining limits. |
| dependency | [Dependency](Yin_C_G0237_v1.md#base-prime-power-extra-valuation) | Exact full-original-root nonvanishing, integral rho_q/P(A^q)/p, determinant p^d normalization and normalized Sylvester quotient, without a unit or powered-degree assumption. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0519_v1.md#current-prime-repetition-finding) | Entire exact current statement, complete retained proof and every selected interface, self-reviewed; all original dated findings remain at their actual old inputs. |

## Complete retained argument

<a id="argument"></a>

The entire original mathematical argument, local equation numbering, failure controls and remaining boundaries are retained below.
Only heading depth and already established current responsible proof locators change.

<a id="frobenius-repetition-hypotheses"></a>
### Exact hypotheses and statement

Let alpha be a nonzero nontorsion algebraic integer, let P be its monic minimal polynomial of degree d, and let A be its integral companion matrix.
Set R=Z[t]/P and Delta=abs(disc P).
For a prime p and r>=1 define

    q=p^r,
    P^[q](t)=product_i(t-alpha_i^q),
    R_(1,q)=Res(P,P^[q]),
    rho_q(t)=rem_P(P(t^q))/p in Z[t],
    C_q=P(A^q)/p=rho_q(A).                             (1)

The polynomial P^[q] retains all d original conjugates, including any multiplicities.
No degree-preservation assumption on alpha^q is needed here.
The integrality in (1), nonzero resultant, and identity

    |det C_q|=|R_(1,q)|/p^d                            (2)

are the exact L G0063 interface.
The parameter d in the denominator does not become a smaller powered degree.

If p does not divide Delta, then for every r>=1,

    v_p(R_(1,p^r))=v_p(R_(1,p)),                       (3)

and the p-primary finite groups coker C_(p^r) are mutually isomorphic.
More precisely, if the irreducible factors of P mod p have degrees f_1,...,f_s, there are finite integers k_i>=1, independent of r, such that

    v_p(R_(1,p^r))=sum_i f_i k_i,
    (coker C_(p^r))[p^infinity]
       is isomorphic to direct-sum_i
              (Z/p^(k_i-1) Z)^(f_i).                 (4)

An exponent k_i-1=0 contributes the trivial group.
This is an abstract finite-group statement, not a claim of canonical integer matrix conjugacy.
By L G0063 it also describes the p-primary normalized Sylvester quotient.
The full Sylvester cokernel has the corresponding exponents k_i, again independent of r.

The argument applies to every nonzero nontorsion algebraic integer in the stated unramified scope.
A global unit hypothesis is not needed; the proof below does not divide by alpha.
The primary unit/reciprocal application remains included.

<a id="direct-etale-frobenius-lift"></a>
### The local algebra and its Frobenius lift, with the needed facts proved

Put O=R tensor_Z Z_p.
It is finite free and p-adically complete.
Since p does not divide Delta, P mod p is squarefree and

    O/pO is isomorphic to product_i F_(p^f_i).

The elementary lifting fact used here is the following.
In any p-adically complete ring, a solution modulo p of F(x)=0 whose derivative is a unit has a unique lift in that residue class.
Newton iteration x_new=x-F(x)/F'(x) squares the error ideal, so it converges.
Uniqueness follows from F(x)-F(y)=(x-y)(F'(y)+(x-y)G(x,y)): the second factor is a unit when x-y is divisible by p.
This proves the required form of Hensel lifting, including p=2.

Apply this to x^2-x to lift the mutually orthogonal residue idempotents.
Their products and sum have the same uniquely lifted idempotent residues, so

    O=product_i O_i,

where O_i has residue field F_(p^f_i) and is free of Z_p-rank f_i.
In O_i an element with nonzero residue is a unit, by lifting its residue inverse and a convergent geometric series.
Every nonzero element is uniquely p^k times a unit: O_i is p-torsion-free and the intersection of p^n O_i is zero, as follows from finite freeness.
Thus O_i is a discrete valuation ring with uniformizer p.
Write v_i(p)=1.
These elementary facts are precisely the unramified properties used below.

Write alpha also for the class of t in O.
The residue alpha^p is a simple root of P in O/pO.
The preceding root lifting constructs a unique beta in O with

    P(beta)=0,       beta=alpha^p modulo p.

Substitution alpha->beta defines a Z_p-algebra map sigma:O->O.
Its reduction is the Frobenius automorphism of the product of finite fields; hence its determinant as a Z_p-linear map is a unit, so sigma is an automorphism.
It fixes each lifted idempotent and preserves each O_i.
It is an isometry there because it fixes p and permutes the units.
On O_i, sigma^(f_i) reduces to the identity, and sigma^(f_i)(alpha_i) and alpha_i are roots of P with the same residue.
Uniqueness of the simple-root lift makes them equal.
Since alpha_i generates O_i as a Z_p-algebra,

    sigma^(f_i)=identity on O_i.                       (5)

This supplies the precise finite unramified Frobenius fact needed in the proof, rather than treating an unspecified Frobenius lift as an additional source premise.

<a id="additive-frobenius-error-stability"></a>
### An additive error recurrence proves the exact stability

Work in a fixed component O_i and suppress the subscript.
Define

    delta_r=alpha^(p^r)-sigma^r(alpha),
    k=v(delta_1).

The Frobenius residue identity gives k>=1.
It is finite: if delta_1=0, then alpha^p=sigma(alpha), and iteration through the finite order in (5) gives alpha^(p^f)=alpha.
The component value of alpha is nonzero, and its minimal polynomial over Q is P; this would make the original alpha a root of unity.
That is excluded by the hypotheses.

Suppose v(delta_r)=k.
Direct expansion gives

    delta_(r+1)=sigma^r(delta_1)
       +[(sigma^r(alpha)+delta_r)^p-(sigma^r(alpha))^p]. (6)

Every term in the bracket has valuation at least k+1.
For the linear term this follows from its coefficient p.
The intermediate binomial coefficients are divisible by p, and their terms have valuation at least 1+jk.
The last term has valuation pk>=k+1.
All powers of sigma^r(alpha) are integral, so they can only add valuation.
This calculation is also valid at p=2 and k=1; a possible cancellation among bracket terms only increases their valuation.
The first term of (6) has valuation exactly k because sigma is an isometry.
Therefore, for every r>=1,

    v(delta_r)=k,
    delta_r=sigma^(r-1)(delta_1) modulo p^(k+1).        (7)

There is no cancellation between that first term and the bracket.
The proof works equally for a local nonunit alpha.
In that case v(alpha)>0, so directly

    v(alpha^(p^r)-sigma^r(alpha))=v(alpha),

and k=v(alpha).
A multiplicative expression alpha^p/sigma(alpha) would not be a unit there and is unnecessary.

Next sigma^r(alpha) is a root of P and P'(sigma^r(alpha)) is a unit.
Dividing P(X) by X-sigma^r(alpha) in O_i[X], the other factor takes a unit value at any X with the same residue as that root.
Since alpha^(p^r) has precisely that residue,

    v(P(alpha^(p^r)))=v(delta_r)=k,
    v(rho_(p^r)(alpha))=k-1.                           (8)

Equivalently, after passing to an unramified splitting ring, the matched root factor is delta_r and every unmatched root factor is a unit, because the reduced roots are distinct.

Multiplication by p^(k_i-1) times a unit on O_i has Smith exponent k_i-1 repeated f_i times as a Z_p-linear map.
Its determinant valuation is f_i(k_i-1).
Applying this in all components to C_q, and then (2), proves (3)--(4).
In fact the principal ideals rho_(p^r)(alpha)O and rho_p(alpha)O coincide, component by component.

<a id="derivative-fermat-quotient-link"></a>
### Derivative, Fermat quotient and the first lifting condition

In the same unramified ring, Taylor expansion at sigma^r(alpha) gives the exact first-order relation

    rho_(p^r)(alpha)
       =P'(sigma^r(alpha)) delta_r/p modulo p.         (9)

The derivative is a unit.
Thus the first higher p factor on a component is exactly the condition delta_1=0 modulo p^2 there.
For a unit component this is the vanishing modulo p of the twisted Fermat quotient

    [alpha^p/sigma(alpha)-1]/p.

For a nonunit component the well-defined additive quantity (alpha^p-sigma(alpha))/p supplies the same test.
Their derivative form (9) is the precise link to the polynomial gcd criterion of L G0063.
Equation (7) also gives

    rho_(p^r)(alpha)=sigma^(r-1)(rho_p(alpha)) modulo p.

Repeatedly using this same prime cannot turn a nonvanishing component into a vanishing one, or deepen an already vanishing component's p-adic length in the unramified setting.

<a id="all-prime-first-quotient-repetition"></a>
### A weaker exact repetition identity holds even at ramified primes

For this paragraph p is any prime; do not assume p does not divide Delta.
For a monic integer polynomial P define

    F_p(t)=[P(t^p)-P(t)^p]/p in Z[t].

Coefficientwise Frobenius proves integrality.
More generally let F_(p^r)(t)=[P(t^(p^r))-P(t)^(p^r)]/p.
Expanding the p-th power of P(t^(p^r))=P(t)^(p^r)+pF_(p^r)(t) shows

    F_(p^(r+1))(t)=F_p(t^(p^r)) modulo p,

because all terms in the remaining difference before division by p are divisible by p^2, also for p=2.
Substituting P(t)=0 therefore gives the identity in the possibly nonreduced algebra F_p[t]/P:

    rho_(p^r)=rho_p^(p^(r-1)).                         (10)

In particular an element on the right is a unit if and only if rho_p is a unit.
By the exact L G0063 criterion,

    v_p(R_(1,p^r))>d iff v_p(R_(1,p))>d                (11)

for every r>=1, with no unramified hypothesis.
Equivalently the monic polynomial gcd satisfies

    gcd(P mod p,rho_(p^r) mod p)
      =gcd(P mod p,(rho_p mod p)^(p^(r-1))).            (12)

The irreducible factors occurring in this gcd are fixed, but their multiplicities can increase when P mod p has repeated factors.
If P mod p=product_j g_j^(e_j) and h_j is the multiplicity of g_j in rho_p mod p, then the first lifting matrix's nullity is exactly

    sum_j deg(g_j) min(e_j,p^(r-1)h_j).                (13)

Interpret h_j as infinity if rho_p mod p is zero.
The dimension formula follows from the elementary fact that multiplication by f on F_p[t]/P has kernel dimension deg gcd(P,f), obtained by writing P=gP_1,f=gf_1 with P_1 and f_1 coprime.
Every modular null direction requires a Smith factor divisible by p.
Since C_(p^r) is the already divided matrix, this also gives

    v_p(R_(1,p^r)) >= d
        +sum_j deg(g_j) min(e_j,p^(r-1)h_j).           (14)

Equations (10)--(13) are a first-lifting statement.
They neither prove equality of full valuations nor identify the entire p-primary cokernel when p divides Delta.
In that case the simple root lift, unit derivative, and separation of unmatched factors used for (8) are unavailable.
No ramified analogue of (3)--(4) is asserted here.

<a id="frobenius-repetition-strategy-boundary"></a>
### Consequence and the remaining arithmetic obligation

The result concerns the p-primary contribution at the same prime that supplies the mandatory Frobenius floor.
It does not say the integer |R_(1,p^r)|/p^d is independent of r, or that contributions at primes ell!=p remain unchanged.
It does not identify Sylvester entropy with the original m(P), and it changes no entropy or degree normalization in the finite determinant construction.

For p not dividing Delta, choosing larger r cannot strengthen that prime's contribution to the normalized quotient: all its Smith exponents were already present at r=1.
At arbitrary primes, even the presence of a first extra p factor cannot be created by repetition if it was absent initially.
Meaningful new arithmetic would have to enter through the initial twisted Fermat quotients, ramified higher lengths, interactions at other primes, different base levels or other actual factors of Q_arith.
This proof gives no uniform frequency or size bound for any of those possibilities, and supplies no degree-independent entropy gap.
