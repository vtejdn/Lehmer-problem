---
author: Yin
---
# Rational proportional coordinates in the residual singleton

Date: 2026-10-20T11:30.
Human author Yin.
The entropy_attainment_bridge agent supplied this entire proportional-coordinate proof, first for b=c/3 and then for every rational ratio.
Root coordinated the continuing residual question but supplied no step of this extension.
The author's earlier contributions to C178 and C188 are reused as accepted inputs, with their existing independent reviews; this author account is not an independent review of either input or of the present candidate.
No finite calculation or source theorem about integral-point existence is a premise.

## Statement

Let F be a totally real number field of degree r, let a,b,c be nonzero algebraic integers in F, and let s in{1,-1}.
Assume

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0,
    c/b in Q.

Then, for H=Q(a,b,c),

    c/b>1, [H:Q]<=3,
    abs(Norm_F(g))>=2^r.                           (1)

The norm is the full original ambient norm.
No triple in this proportional class is asserted to exist.
The statement does not cover nonzero affine offsets or arbitrary nonproportional integral pairs, and is not the unrestricted singleton norm theorem.

<a id="argument"></a>
## Complete proof

By accepted [C188](Yin_C_G0188_v1.md#statement), H=Q(a).
The first equation makes a totally positive; since its nonzero norm is an integer, some real embedding has a>=1.

Write c=lambda b with nonzero rational lambda.
At an embedding with a>=1, the first projection argument of C188 shows that s b and s c have the same sign: the polynomial2X^5-X^2 takes a positive level when s c>0 and a level below-1 when s c<0, with the corresponding unique root of that same sign.
Thus lambda>0.
If lambda<=1, then

    b^2=3a^5/(2lambda^2)>a^3, b^2>=3/2,
    abs(g)=abs(b)^3(2b^2-lambda^3)
          >=(4/3)abs(b)^5>b^2>abs(b^2-a^3)

at that embedding, contradicting b^2-a^3=-s g.
Consequently lambda>1.

Put kappa=3/(2lambda^2), so b^2=kappa a^5.
Dividing the residual equation by a^3 and squaring gives

    kappa^3 a^9(lambda^3-2kappa a^5)^2
      =(1-kappa a^2)^2.                            (2)

Every conjugate of the totally positive a is a positive root of this rational polynomial equation.
Set v=lambda*3^(-1/5), w=lambda*sqrt(2/3), so0<v<w; the last inequality is equivalent to27<32.
For x>0, x!=w define

    F_lambda(x)=kappa^(3/2) x^(9/2)
                 (lambda^3-2kappa x^5)/(1-kappa x^2).

Equation(2) is exactly F_lambda(x)=1 or-1 away from w.
The points v,w and0 do not solve(2).
The derivative has the sign of

    D_lambda(x)=30kappa^2 x^7-38kappa x^5
                  -5kappa lambda^3 x^2+9lambda^3.

Descartes' rule gives at most two positive zeros, because its descending nonzero coefficients have two sign changes.
There is one in(0,v), since D_lambda(0)>0 and

    D_lambda(v)=20kappa v^5(kappa v^2-1)<0.

There is another in(w,infinity), since

    D_lambda(w)=4(lambda^3-2kappa w^5)<0

and the leading coefficient is positive.
These are the only positive derivative zeros.
Thus F_lambda is positive on(0,v), with one maximum, giving at most two roots at level1.
On(v,w) it decreases from0 to-minus infinity, giving exactly one root at level-1.

There are no roots in(w,infinity).
Indeed v<w and strict convexity of y^(5/2) give

    F_lambda(x)
      =2kappa^(3/2)x^(9/2)(x^5-v^5)/(x^2-w^2)
      >2kappa^(3/2)x^(9/2)(5/2)w^3
      =5x^(9/2)>5(2/3)^(9/4)>1.

The final bound uses lambda>1 and hence x>w>sqrt(2/3); its strict comparison with1 follows, for example, from625*512>19683 after fourth powers.
Therefore(2) has at most three positive roots in total.
All distinct conjugates of a lie among them, so by C188 the actual H=Q(a) has degree at most3.
C178 and the complete original norm tower now give

    abs(Norm_F(g))=abs(Norm_H(g))^[F:H]
      >=2^([H:Q][F:H])=2^[F:Q].                   (3)

This rules out a low-norm counterexample for EVERY rational proportional b,c pair, including b=c/3.
It does not cover nonzero affine offsets or arbitrary nonproportional integral pairs, and it is not the unrestricted singleton norm theorem.

<a id="exact-inputs"></a>
## Inputs, scope and contribution boundaries

The complete argument uses the elementary norm and embedding facts stated above, differentiation, the intermediate value theorem, Descartes' rule of signs and strict convexity of y^(5/2).
All application domains, signs, zeros, derivative intervals and numerical inequalities for these elementary facts are displayed in the proof.
The actual new conclusion is the full rational proportional class, not another finite affine grid.
The two direct project inputs are already adopted at their exact stated scopes.
The prior fixed-input authorship does not supply an independent review of this new proof.

| Input | Exact scope used |
| --- | --- |
| [C188 statement and proof](Yin_C_G0188_v1.md#argument) | H=Q(a) for the entire actual residual domain, plus the explicitly proved sign of b at an embedding with a>=1 and fixed c. |
| [C178 statement and proof](Yin_C_G0178_v1.md#argument) | Every actual triple in a field of degree at most4 has full norm at least2 to that degree; applied in H after proving its degree at most3. |
| Elementary real calculus | Exactly the derivative and convexity calculations displayed here; no numerical roots, implicit fixed-degree classification or approximate thresholds. |
| Original-field norm tower | F/H is retained in both exponent and norm, as in(3); no replacement of the requested full norm by a smaller own-field norm. |

The author's complete readback checked the rational-ratio sign, the strict lambda>1 exclusion, both critical points, all three positive intervals and the full field-degree implication.
Independent review and adoption remain separate.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T11:30 |
| status | open |
| reason | Register the complete infinite rational proportional class and its full original norm cost for separate whole review; the general nonproportional residual singleton remains open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete rational proportional theorem](#statement) | Original totally real integral residual triples, rational c/b, primitive degree bound and full ambient norm. |
| argument | [Complete real-root proof](#argument) | Ratio sign, lambda>1, exact derivative and positive-root count, accepted primitive-field input and unchanged norm tower. |
| dependency | [C188 positive-coordinate field theorem](Yin_C_G0188_v1.md#statement) | Actual H=Q(a) and the sign selection already proved in its first projection argument. |
| dependency | [C178 local two-adic theorem](Yin_C_G0178_v1.md#statement) | Its explicit low-degree full-norm consequence, used only after [H:Q]<=3. |
| support | [Exact inputs and boundaries](#exact-inputs) | Complete elementary application scope, prior author relationships, no computational premise and no assertion of existence or a general norm theorem. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T11:47 |
| status | proved |
| authority | Internal adoption within Yin's selected residual singleton inquiry. |
| reason | Adopt the full rational proportional class through the complete independent R464 finding. Its actual generated field has degree at most3 and its full ambient norm is at least2 to the original degree. Nonzero affine offsets, arbitrary nonproportional pairs and the unrestricted residual target remain separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete rational proportional theorem](#statement) | Original totally real integral residual triples, rational c/b, primitive degree bound and full ambient norm. |
| argument | [Complete real-root proof](#argument) | Ratio sign, lambda>1, exact derivative and positive-root count, accepted primitive-field input and unchanged norm tower. |
| dependency | [C188 positive-coordinate field theorem](Yin_C_G0188_v1.md#statement) | Actual H=Q(a) and the sign selection already proved in its first projection argument. |
| dependency | [C178 local two-adic theorem](Yin_C_G0178_v1.md#statement) | Its explicit low-degree full-norm consequence, used only after [H:Q]<=3. |
| support | [Exact inputs and boundaries](#exact-inputs) | Complete elementary application scope, prior author relationships, no computational premise and no assertion of existence or a general norm theorem. |
| review | [Whole proportional finding](../audits/reviews/Yin_R_G0464_v1.md#rational-proportional-whole-independent-finding) | Entire actual statement, every real-root interval and endpoint, accepted input interfaces and full original norm tower, with upstream authorship disclosed. |

