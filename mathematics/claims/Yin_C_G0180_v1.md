---
author: Yin
---
# No rational b or g in the unbuffered residual singleton

Date: 2026-10-20T10:01.
Human author Yin.
The draft_inventory_later agent supplied the rational-b positive-root argument.
Root supplied the rational-g reduction, its derivative and two-real-root bound, and the resulting restricted norm conclusion.
The entropy_attainment_bridge agent supplied the additional root-distance and integer-trace contradiction, reconstructed both complete arguments and authored this fixed candidate.
The rational-b monotonicity idea was also examined independently in the latter author's scratch analysis before receipt of the full proof; no independent review is claimed for this parallel author discussion.
All three agents are contributors to the present proof.
The entropy_attainment_bridge author also authored the upstream C178 valuation theorem and the earlier q>=2 comparison; root reviewed C178 through the self-reviewed R447 finding, which is reused at that actual scope.

## Statement

Let F be any totally real number field and let a,b,c be nonzero algebraic integers in F.
For s in{1,-1}, suppose

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.                                  (1)

Then neither b nor g is rational.
This excludes both rational-coordinate branches in every ambient degree, including fields with arbitrarily high ramification.
It does not prove the exponential norm floor for the remaining nonrational g.
No embedding subset replaces F, and when a smaller field is used below all elements are proved to belong to it before applying its local obstruction.

The real-variable estimate used in the rational-g proof is explicit.
For every real n>=1, the polynomial

    P_n(X)=27(X^2+n)^5-8(2X^5+n)^2                 (2)

has exactly two distinct real roots, denoted -u<0<v, and

    0<u-v<8/(625n)<1.                              (3)

This estimate is used only when n is a positive rational integer.
All algebraic integers and field degrees in(1) remain exact; no numerical root isolation or finite scan is used.

<a id="argument"></a>
## Complete proof

### 1. Positivity and the rational-field obstruction

The first equation of(1) gives a>0 at every real embedding, because3a^5=2c^2>0.
The accepted [C178 unramified-prime conclusion](Yin_C_G0178_v1.md#statement) says that a triple(1) cannot lie in any number field having an unramified prime over2.
In particular no such triple of nonzero rational integers exists.
The complete fixed input is [C178's proof](Yin_C_G0178_v1.md#argument), checked in the self-reviewed [R447](../audits/reviews/Yin_R_G0447_v1.md#residual-two-adic-whole-independent-finding) and adopted in its [selected decision](Yin_C_G0178_v1.md#decision-whole-reviewed-2026-10-20).
This input is not being independently re-proved by its author here.

We also use the following elementary field fact with its proof.
If K is a subfield of a totally real field F and beta in F satisfies beta^3 in K, then beta belongs to K.
For an embedding of K into R, every embedding of K(beta) extending it is real and maps beta to a root of X^3-beta^3 under that embedding.
There is only one real cube root.
Separability in characteristic zero therefore makes [K(beta):K]=1.
The same argument will be applied only to explicitly exhibited cubic powers in K.

<a id="rational-b-exclusion"></a>
### 2. A rational b is impossible

Suppose b=B is rational.
Integrality makes B a nonzero rational integer.
Put y=a^3, so every conjugate of y is positive, and set

    K=2sB^5-B^2=B^2(2sB^3-1) in Z minus{0}.

The residual equation gives c^3=s(y+K).
Squaring and using f=0 therefore gives

    27y^5=8(y+K)^2.                                (4)

For each fixed nonzero integer K, equation(4) has exactly one positive real root.
If K>0, the function y^5/(y+K)^2 on y>0 increases strictly from0 to infinity, since its logarithmic derivative is

    5/y-2/(y+K)=(3y+5K)/(y(y+K))>0.

If K=-H<0, then H>=1.
On(0,H), y^5/(H-y)^2 increases strictly from0 to infinity.
At y=H the equation is impossible, and for y>H,

    y^5/(y-H)^2>y^3>H^3>=1>8/27.

Thus there is no further positive root.
Every conjugate of y satisfies the same rational polynomial(4) and is positive, so all are equal to its unique positive root.
Consequently y is rational.
The real-cube-root field fact gives a rational; it also gives c rational from c^3=s(y+K).
Then a,b,c are rational integers, contrary to Section1.
This proves the first exclusion for the original arbitrary ambient F.

<a id="rational-g-real-root-count"></a>
### 3. Real roots when g is a rational integer

Suppose g is rational and nonzero, hence an integer.
The transformation

    (b,c,s,g)->(-b,-c,-s,-g)                         (5)

preserves a, f=0, the residual equation and integrality.
We may therefore suppose g=n is a positive integer, with s still one of the two permitted signs.
From(1),

    a^3=b^2+s n>0,
    c^3=2b^5+n,
    27(b^2+s n)^5=8(2b^5+n)^2.                     (6)

For real x in the domain x^2+s n>0 define

    R_s(x)=(2x^5+n)/(x^2+s n)^(5/2),
    C=sqrt(27/8),
    R_s'(x)=5n x(2s x^3-1)/(x^2+s n)^(7/2).        (7)

Equation(6) requires R_s(b)=C or -C.
Here1<C<2.

If s=-1, the allowed domain is abs(x)>sqrt(n)>=1.
For x>sqrt(n), R_-(x)>2 immediately.
For x=-t<-sqrt(n), use

    t^5-(t^2-n)^(5/2)>n^(5/2)>=n,

which follows from (A+B)^(5/2)>A^(5/2)+B^(5/2) for A,B>0, with A=t^2-n and B=n.
It gives -2t^5+n<-2(t^2-n)^(5/2), so R_-(x)<-2.
Thus s=-1 has no allowed real solution.
Equivalently, no nonpositive value of x^2-n can rescue(6): its left side would be nonpositive and the right side nonnegative, with equality at the endpoints impossible for n>=1.

If s=1, the domain is the entire real line.
On the negative half-line, the derivative in(7) is positive and R_+(x) increases strictly from-2 to n^(-3/2)<=1.
It crosses -C exactly once and never crosses C there.
On the positive half-line it decreases until x=2^(-1/3) and then increases to2.
Its numerator is positive, its initial value is at most1 and its minimum is positive and at most1.
It therefore crosses C exactly once and never crosses -C there.
At x=0 its value is at most1, so0 is not a root.
This proves the two distinct real roots asserted in(2), for every real n>=1.

<a id="rational-g-integer-trace-gap"></a>
### 4. Exact separation of the two real roots

Write the two roots as -u<0<v, and set

    A_n(x)=2x^5-C(x^2+n)^(5/2) for x>0.

The two level equations just proved give

    A_n(v)=-n, A_n(u)=n.                            (8)

The positive root satisfies v>5sqrt(n).
Indeed, 5sqrt(n) lies on the strictly increasing positive branch of R_+, and

    R_+(5sqrt(n))
       =(6250+n^(-3/2))/26^(5/2)
       <=6251/26^(5/2)<C.                           (9)

The final strict inequality is the exact integer comparison

    8*6251^2=312600008<320797152=27*26^5.

For every x>=5sqrt(n),

    A_n'(x)
      =5x^4[2-C(1+n/x^2)^(3/2)]
      >=5x^4[2-(39/25)^(3/2)]
      >x^4/4>=625n^2/4.                            (10)

Here C(26/25)^(3/2)=(39/25)^(3/2)<39/20; after squaring, the last strict comparison is

    59319/15625<1521/400.

Thus A_n is strictly increasing on[v,infinity), starts there at-n and tends to positive infinity because2-C>0.
Its unique solution to A_n(x)=n is u, so u>v.
Integrating the strict derivative bound between v and u in(8) gives

    2n>(625n^2/4)(u-v),
    0<u-v<8/(625n)<1.                              (11)

This proves(3), retaining the actual constants and strictness without numerical approximations.

### 5. The rational-g contradiction in the actual field

Every Q-conjugate of b is real, because b belongs to the totally real field F, and satisfies the rational polynomial P_n in(2).
It therefore belongs to the two-element set{-u,v}; characteristic-zero separability gives [Q(b):Q]<=2.
If this degree were2, the two conjugates would be exactly -u and v.
The trace of the algebraic integer b would then be v-u in(-1,0), by(11), whereas its rational trace is an integer.
This is impossible.
Hence b is rational.
Section2 already excludes every rational b.
Alternatively, (6) and the real-cube-root field fact put a,c in Q(b)=Q, and Section1 excludes the resulting rational-integer triple directly.
Undoing(5) proves the assertion for either initial sign of g and either initial s.
The original ambient field need not be quadratic, normal or unramified; the argument proved the smaller field membership before using any rational-field obstruction.

<a id="inputs-and-limits"></a>
## Exact inputs and unresolved scope

| Input | Actual use and limit |
| --- | --- |
| [C178 statement](Yin_C_G0178_v1.md#statement) | Only the impossibility of a residual triple in Q, whose2-prime is unramified; no high-ramification norm floor is imported. |
| [C178 complete argument](Yin_C_G0178_v1.md#argument) | The accepted explicit valuation/parity proof supplies that rational-field obstruction. |
| [R447](../audits/reviews/Yin_R_G0447_v1.md#residual-two-adic-whole-independent-finding) | Self-reviewed upstream finding for C178, authored there by the present entropy_attainment_bridge contributor; this is not a review of the new rational-branch proof. |
| [Original singleton responsibility](../ledger/Yin_L_G0438_v1.md#unbuffered-reduction) | Original question and extraction context only; no mutable draft is a logical premise. |

The remaining background consists of elementary separability, real embeddings, integral traces, exact rational inequalities and one-variable differentiation; every nonroutine application is supplied above.
No external theorem or source-proof upgrade is used.
No numerical computation, bounded scan, root approximation or rational point is presented as an algebraic-integer norm certificate.
The complete author check covers both signs, the integer thresholds K and n, all real-root domains, exact differentiation, both integer comparisons, strict derivative integration and the degree/trace argument.
Because the new proof has multiple contributors, none is an independent whole reviewer of it.
Independent review and adoption remain separate from this registration.

The conclusion closes exactly the rational-b and rational-g branches of D37.
It does not establish abs(Norm_F(g))>=2^(r/2) for nonrational g, does not exclude nonrational units and does not turn one embedding's small trace into a full norm inequality.
The original arbitrary-field singleton remains the continuing problem.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:01 |
| status | open |
| reason | Register the complete rational-coordinate exclusions and exact two-root trace-gap proof for independent review. These are genuine closed branches of the original problem, while arbitrary nonrational g remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Rational-coordinate exclusions](#statement) | Full original totally real integral domain, both signs, neither b nor g rational, and explicit two-real-root gap(2)--(3). |
| argument | [Complete proof](#argument) | Sections1--5, formulas(4)--(11), exact field descent, positive-root count, both signs and domains, strict derivative constants and integral-trace contradiction. |
| dependency | [C178 accepted obstruction](Yin_C_G0178_v1.md#argument) | Only exclusion in Q at its unramified2-prime after actual field membership has been proved. |
| support | [Complete input and contributor account](#inputs-and-limits) | Elementary background, upstream author's relationship and R447 reuse, no-computation boundary and open nonrational scope. |
| support | [C178 independent review](../audits/reviews/Yin_R_G0447_v1.md#residual-two-adic-whole-independent-finding) | Upstream exact valuation/parity scope only; not evidence of a whole review of this new proof. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:17 |
| status | proved |
| authority | Internal adoption under Yin's selected arbitrary-field singleton continuation. |
| reason | Adopt the full rational-b and rational-g exclusions and exact real two-root gap through noncontributor whole R451. Both coordinate branches are excluded in every ambient totally real degree; no inference to nonrational units or the full residual norm floor is made. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Rational-coordinate exclusions](#statement) | Full original totally real integral domain, both signs, neither b nor g rational, and explicit two-real-root gap(2)--(3). |
| argument | [Complete proof](#argument) | Sections1--5, formulas(4)--(11), exact field descent, positive-root count, both signs and domains, strict derivative constants and integral-trace contradiction. |
| dependency | [C178 accepted obstruction](Yin_C_G0178_v1.md#argument) | Only exclusion in Q at its unramified2-prime after actual field membership has been proved. |
| support | [Complete input and contributor account](#inputs-and-limits) | Elementary background, upstream author's relationship and R447 reuse, no-computation boundary and open nonrational scope. |
| support | [C178 valuation finding](../audits/reviews/Yin_R_G0447_v1.md#residual-two-adic-whole-independent-finding) | Upstream exact valuation/parity scope only; not evidence of a whole review of this new proof. |
| review | [Whole rational-branch finding](../audits/reviews/Yin_R_G0451_v1.md#c180-whole-rational-branch-finding) | Entire final statement and all eleven formulas, complete field descent and both sign domains, exact derivative/root-distance bounds and integer-trace contradiction, with contributor and upstream-review roles disclosed. |

