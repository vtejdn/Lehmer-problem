---
author: Yin
---

# Complete cyclotomic removal and exact repair for the power-of-two six-term family

The original2026-10-07 argument by review_matrix_completion for Yin is retained completely from [L51](../ledger/Yin_L_G0051_v1.md).
Its original whole-quotient and selected-irreducible boundaries are preserved.

## Statement

Let g>=3 be an integer, and put

    S_6(x)=x^6-x^5+x^4-x^3+x^2-x+1,
    q_g=t^(7g)+1-t^(2g+1)-t^(3g+1)-t^(4g-1)-t^(5g-1),
    r_g=q_g/(t^g+1)=S_6(t^g)-t^(2g+1)-t^(4g-1).

Every root of unity of q_g either has zeta^g=-1 or has order dividing at least one of28,30,36,42,48.
For g=2^k with integer k>=2, the entire cyclotomic part c_g of r_g is1 when k is even and one simple Phi_6 when k is odd.
Put F_g=r_g/c_g, the complete noncyclotomic quotient, without assuming it irreducible.
For a monic polynomial f define b_n(f)=n^(-1)sum_(j|n)mu(n/j)sum_(alpha root of f)alpha^j, with full multiplicity, and D(f)=sum_n n max(0,-b_n(f)).
R_*(f) is the least degree of a monic cyclotomic product c such that fc is the nonzero characteristic polynomial of a nonnegative integer matrix; arbitrary additional zero eigenvalues are permitted.
Then

    D(F_g)=2g,     R_*(F_g)=g                 for even k,
    D(F_g)=2g+7,   R_*(F_g)=g+2               for odd k.

The same minima are attained among cyclotomic products making every b_n nonnegative, since the explicit minimizing products recover the original primitive graph.
The only negative counts for even k are b_(2g)=-1; for odd k they are b_1=b_6=b_(2g)=-1.
The positive strictly dominant Perron root and all-power degree preservation of that root are retained from the actual primitive graph.
If F_g=pH with p its Perron minimal factor, the exact transfer identity is b_(2g)(p)=-1-b_(2g)(H), so b_(2g)(H)>=0 suffices for that selected-factor obstruction.
No such sign, all-parameter irreducibility or small-Mahler conclusion is supplied for an arbitrary H.

## Current assessment
[Selected decision](#decision-current-complete-proof-homes)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:28 |
| status | open |
| reason | Register the exact retained theorem and complete original argument; applicable current statement, proof and interface checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every integer g>=3 order reduction and every k>=2 power-of-two quotient, complete cyclotomic multiplicity, exact all-order D/R* optima and the precise irreducible-factor transfer limitation. |
| argument | [Complete retained proof](#argument) | All fifteen pairings, ten triangle partitions, determinant elimination, primitive conjugate/embedding argument, every exceptional two-primary case, simple Phi6 derivative and both complete repair lower/upper bounds. |
| dependency | [Direct rational relative-order proof](../ledger/Yin_L_G0044_v1.md#minimal-vanishing-order) | Only the complete rational minimal-vanishing-relation order theorem, with its elementary cyclotomic hypotheses and original source-inspection limit. |
| dependency | [Small unit-root classification](../ledger/Yin_L_G0045_v1.md#five-root-vanishing-classification) | Only minimal sizes2,3,5 at size at most5, including repeated terms and absorbed signs; no sharp degree34 computation is used. |
| dependency | [Actual six-term primitive graph](../ledger/Yin_L_G0048_v1.md#unbounded-essential-block-family) | Exact q_g graph, positive dominant root, full net-trace counts and girth2g+1; necessary trace obstruction and explicit positive repair, without invoking KOR00 sufficiency. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:33 |
| status | proved |
| reason | Adopt the exact retained theorem and complete argument after the actual whole current self-review in R511, with all used inputs resolved at their stated scopes; historical findings retain their original dates and unknown/self relationships, and no unrestricted gap, new research execution or independent certification is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every integer g>=3 order reduction and every k>=2 power-of-two quotient, complete cyclotomic multiplicity, exact all-order D/R* optima and the precise irreducible-factor transfer limitation. |
| argument | [Complete retained proof](#argument) | All fifteen pairings, ten triangle partitions, determinant elimination, primitive conjugate/embedding argument, every exceptional two-primary case, simple Phi6 derivative and both complete repair lower/upper bounds. |
| dependency | [Direct rational relative-order proof](../ledger/Yin_L_G0044_v1.md#minimal-vanishing-order) | Only the complete rational minimal-vanishing-relation order theorem, with its elementary cyclotomic hypotheses and original source-inspection limit. |
| dependency | [Small unit-root classification](../ledger/Yin_L_G0045_v1.md#five-root-vanishing-classification) | Only minimal sizes2,3,5 at size at most5, including repeated terms and absorbed signs; no sharp degree34 computation is used. |
| dependency | [Actual six-term primitive graph](../ledger/Yin_L_G0048_v1.md#unbounded-essential-block-family) | Exact q_g graph, positive dominant root, full net-trace counts and girth2g+1; necessary trace obstruction and explicit positive repair, without invoking KOR00 sufficiency. |
| review | [Complete current finding](../audits/reviews/Yin_R_G0511_v1.md#current-power-two-repair-finding) | Entire exact Statement and complete retained Argument, every integer parameter, all determinant/order/multiplicity cases, both exact repair optima and irreducible-factor boundary, after actual current contributor-context self-review. |

### Decision current-complete-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:42 |
| status | proved |
| reason | Use the adequate complete same-object C homes for current dependencies; exact scopes, original proof, all other selections and old R bindings remain unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every integer g>=3 order reduction and every k>=2 power-of-two quotient, complete cyclotomic multiplicity, exact all-order D/R* optima and the precise irreducible-factor transfer limitation. |
| argument | [Complete retained proof](#argument) | All fifteen pairings, ten triangle partitions, determinant elimination, primitive conjugate/embedding argument, every exceptional two-primary case, simple Phi6 derivative and both complete repair lower/upper bounds. |
| dependency | [Direct rational relative-order proof](Yin_C_G0262_v2.md#minimal-vanishing-order) | Only the complete rational minimal-vanishing-relation order theorem, with its elementary cyclotomic hypotheses and original source-inspection limit. |
| dependency | [Small unit-root classification](Yin_C_G0263_v1.md#five-root-vanishing-classification) | Only minimal sizes2,3,5 at size at most5, including repeated terms and absorbed signs; no sharp degree34 computation is used. |
| dependency | [Actual six-term primitive graph](Yin_C_G0269_v1.md#unbounded-essential-block-family) | Exact q_g graph, positive dominant root, full net-trace counts and girth2g+1; necessary trace obstruction and explicit positive repair, without invoking KOR00 sufficiency. |
| review | [Complete current finding](../audits/reviews/Yin_R_G0511_v1.md#current-power-two-repair-finding) | Entire exact Statement and complete retained Argument, every integer parameter, all determinant/order/multiplicity cases, both exact repair optima and irreducible-factor boundary, after actual current contributor-context self-review. |

## Complete retained argument

<a id="argument"></a>

Original proof date:2026-10-07.

For g>=3 retain

    q_g=t^(7g)+1-t^(2g+1)-t^(3g+1)-t^(4g-1)-t^(5g-1),
    r_g=q_g/(t^g+1)=S_6(t^g)-t^(2g+1)-t^(4g-1).

<a id="power-two-noncyclotomic-repair"></a>
The result below concerns g=2^k, k>=2.
The entire cyclotomic part of r_g is

    c_g=1                 if k is even,
    c_g=Phi_6             if k is odd,                       (1)

with multiplicity one in the second case.
Put F_g=r_g/c_g, the whole noncyclotomic quotient.
Its exact canonical and minimum cyclotomic repair degrees are

    D(F_g)=2g,       R_*(F_g)=g,             if k is even,
    D(F_g)=2g+7,     R_*(F_g)=g+2,           if k is odd.     (2)

In particular the negative normalized net trace at index 2g survives removal of all cyclotomic factors.
This does not transfer that negative trace to a chosen irreducible factor if F_g is reducible.
If F_g is irreducible, (2) applies to the actual Perron minimal polynomial.
No all-parameter irreducibility assertion is made.

<a id="essential-family-order-reduction"></a>
## A finite order reduction outside the known block

We first prove for every g>=3 that every root of unity of q_g either satisfies zeta^g=-1, or has order dividing at least one of

    28, 30, 36, 42, 48.                                  (3)

Label the formal support points, in coordinates multiplying (g,1), by

    P=(0,0), Q=(7,0), A=(2,1), B=(3,1), C=(4,-1), D=(5,-1).

The coefficients at P,Q are +1 and those at A,B,C,D are -1.
At a root zeta of order m the six signed unit terms sum to zero.
If the relation is minimal, the rational relative-order lemma gives m|30, since the support differences generate the full integer exponent lattice: consecutive negative exponents differ by g, and 2g+1 together with g has gcd one.

Otherwise the minimal components have sizes 2+2+2 or 3+3.
This follows from L G0045: a nonempty minimal unit-root relation of size at most five has size two, three or five, so a proper partition of six has precisely those two forms.
In a pair, the original root ratios have order dividing two; in a triangle, they have order dividing six after the original signs are restored.

Here is the elementary determinant test used in the following finite tables.
If both within-component difference vectors v=(v_1,v_2) and w=(w_1,w_2) obey

    m | L(v_1 g+v_2),       m | L(w_1 g+w_2),

then m divides L det(v,w): eliminate g by taking the corresponding integer linear combination.
Consequently m divides L times the gcd of all nonzero such determinants.
The table entries are determinants of the displayed fixed integer points, independent of g; no torsion-root scan is used.

For three pair components take L=2.
If P and Q are paired, the remaining pairings give:

| Pairing of A,B,C,D | gcd of nonzero difference determinants |
| --- | ---: |
| AB, CD | all differences horizontal |
| AC, BD | 14 |
| AD, BC | 2 |

In the first row the negative pair AB itself gives zeta^g=-1.
In every other matching P is paired to X and Q to Y, with X!=Y in {A,B,C,D}; the last two points form the third pair.
The determinant gcds are:

| X | Y=A | Y=B | Y=C | Y=D |
| --- | ---: | ---: | ---: | ---: |
| A | -- | 1 | 1 | 5 |
| B | 1 | -- | 9 | 1 |
| C | 1 | 5 | -- | 1 |
| D | 9 | 1 | 1 | -- |

For example, X=A,Y=D gives opposite vectors (2,1),(-2,-1) and the remaining difference (1,-2), whose determinant has absolute value five.
These fifteen matchings are exhaustive.
Apart from zeta^g=-1, they give m dividing one of 28,4,2,10,18.

For two triangle components take L=6.
Choose the triple containing P; the complementary triple is determined.
The gcd of the absolute determinants internal to the two triples is:

| Other points with P | QA | QB | QC | QD | AB | AC | AD | BC | BD | CD |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gcd | 1 | 1 | 1 | 1 | 1 | 6 | 7 | 7 | 8 | 1 |

For example the AC and complementary QBD determinants both have absolute value six; the BD and complementary QAC determinants both have absolute value eight.
These ten partitions give m dividing one of 6,36,42,48.
Combining the cases proves (3).

<a id="power-two-cyclotomic-classification"></a>
## A trace identity excludes the remaining orders

Define

    A_0(y)=y^3-y^2-2y+1.

Dividing r_g(t) by t^(3g) gives the exact Laurent identity

    t^(-3g)r_g(t)
      =A_0(t^g+t^(-g))-(t^(g-1)+t^(-(g-1))).            (4)

If zeta^g=-1, then r_g(zeta)=7-zeta-zeta^(-1), which is at least five.
Thus the known block t^g+1 is relatively prime to r_g.
Every cyclotomic root of r_g must therefore have an order from (3).

For any root of unity X of odd order n>=5, the number A_0(X+X^(-1)) has a real conjugate strictly below -2.
Indeed, the primitive conjugate X=exp(2 pi i (n-1)/(2n)) gives

    x=X+X^(-1)=-2cos(pi/n)<=-2cos(pi/5)=-phi,

where phi=(1+sqrt(5))/2.
The polynomial A_0 is strictly increasing for x<=-phi, and

    A_0(-phi)=-phi^2<-2.

Any embedding on Q(X) extends to the ambient root-of-unity field.
Under that embedding the other side of (4) remains Y+Y^(-1) for a root of unity Y, and lies in [-2,2].
Hence an odd order n>=5 for X=zeta^g is impossible.

Write m=2^a n with n odd.
Every candidate order in (3) has a<=4.
If k>=4, then X=zeta^(2^k) has order n, which is odd.
The preceding argument excludes n>=5.
If n=1, then X=1 and A_0(2)=1, so (4) would require Y=zeta^(g-1) to have order six.
But Y has the same power-of-two order m as zeta, because g-1 is odd.
This is impossible.
If n=3, then X+X^(-1)=-1 and A_0(-1)=1, so Y must have order six.
For even k, 3 divides g-1 and the order of Y is a power of two.
For odd k, 3 does not divide g-1 and ord(Y)=m; thus precisely m=6 remains.

Only two small k cases need additional checks, still without polynomial factorization.
For k=2, the candidates with a>k are m=8,16,24,48.
Their X-orders are respectively 2,4,6,12.
For k=3, they are m=16,48 with X-orders 2,6.
Order two gives A_0(-2)=-7 and is impossible.
Order four gives A_0(0)=1 and would require Y-order six, whereas the m=16 case has Y-order sixteen.
Order six gives A_0(1)=-1 and would require Y-order three: the relevant Y-orders are eight for (g,m)=(4,24), and forty-eight for (8,48).
Finally X-order twelve has a conjugate with x=-sqrt(3), giving A_0(x)=-2-sqrt(3)<-2.
All these candidates are excluded.
The remaining orders have a<=k and are handled by the same odd-order argument.
Thus no order except six survives, and it can survive only for odd k.

For odd k, g=2 modulo six.
At a primitive sixth root zeta put X=zeta^g=zeta^2 and Y=zeta^(g-1)=zeta.
Then X+X^(-1)=-1 and Y+Y^(-1)=1, so (4) vanishes.
The root is simple.
For the Laurent expression L on the right of (4),

    t L'(t)=g A_0'(X+X^(-1))(X-X^(-1))
                -(g-1)(Y-Y^(-1)).

At zeta, A_0'(-1)=3 and X-X^(-1)=Y-Y^(-1)!=0.
Therefore tL'=(2g+1)(Y-Y^(-1))!=0.
Multiplication by t^(3g) preserves this nonzero derivative at a root.
This completes the proof of (1), including multiplicity.

<a id="power-two-repair-transfer"></a>
## Exact repair of the whole noncyclotomic quotient

L G0048 proves that r_g has precisely one negative normalized net trace:

    b_(2g)(r_g)=-1,

with b_g(r_g)=1 and all other b_j(r_g)>=0.
In fact the other counts vanish below the graph girth 2g+1.
For even k no further factors are removed, giving D(F_g)=2g.
The factor t^g+1 has degree g and repairs F_g back to q_g.
Any repair must affect index 2g positively, so it contains a cyclotomic factor with order divisible by 2g and degree at least phi(2g)=g.
Thus R_*(F_g)=g.

For odd k>=3, remove the single Phi_6.
Its nonzero normalized corrections are +1 at one and six, and -1 at two and three.
Since g>=8, these four indices are below the girth and distinct from g and 2g.
Hence F_g has precisely the three negative counts

    b_1(F_g)=b_6(F_g)=b_(2g)(F_g)=-1.

This gives D(F_g)=2g+7.
The product Phi_6(t)(t^g+1) repairs F_g and has degree g+2.
To prove the reverse bound, every repair must affect both six and 2g positively.
If a factor affects both, its order is divisible by lcm(6,2g)=6g, and its degree is at least phi(6g)=2g>g+2.
Otherwise the factors which can affect these two indices belong to disjoint collections.
They cost at least phi(6)=2 and phi(2g)=g respectively.
Any repair of degree below g+2 is therefore impossible, proving (2).

The inference uses the full noncyclotomic quotient.
Its positive Perron root and all-power degree preservation for that root come from the primitive graph already proved in L G0048.
However, several noncyclotomic irreducible factors may contribute different normalized traces whose sum is the displayed negative count.
No sign for the Perron irreducible factor alone follows from additivity.
An exact factorization showing F_g irreducible is a sufficient transfer certificate.
More generally, for F_g=p H with p the Perron minimal factor, the exact condition at index 2g is

    b_(2g)(p)=-1-b_(2g)(H),

so b_(2g)(H)>=0 suffices to retain the obstruction; that inequality must itself be checked.
The present argument establishes no such positivity for an arbitrary noncyclotomic H.
