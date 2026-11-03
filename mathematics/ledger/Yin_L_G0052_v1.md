---
author: Yin
---

# G0001: S4 and joint escape in the alternating-kernel family

Date: 2026-10-07.
The complete current theorem and proof are [C224](../claims/Yin_C_G0224_v1.md#statement), including the full general-K1 corollary.
The original argument below remains the actual fixed input of the relocated historical findings; current statement-and-proof checking has its own date in R511.
Direct argument by assigned AI assess_shortness_route and the coordinating AI for Yin.
This continues the [support-change question in L G0050](Yin_L_G0050_v1.md#essential-support-next-step).
The only non-elementary convergence input is the exact univariate Lawton theorem already retained in [Den09 U002, Theorem 14 / Example 15](../audits/literature/Den09/Yin_U002.md).
No multivariable-specialization extension is assumed, no new literature is acquired, and Lawton's original proof remains unaudited.

<a id="alternating-kernel-scope"></a>
## Exact family and the remaining finite-kernel obligation

For r>=1 put

    S_(2r)(x)=sum_(j=0 to 2r) (-1)^j x^j,
    A_r(x)=x^(-r)S_(2r)(x),
    F_r(x,z)=A_r(x)-z-z^(-1).

On the unit circle,

    A_r(exp(i theta))=cos((r+1/2)theta)/cos(theta/2),

with the removable endpoint value interpreted by continuity.
For g>=3, 1<=h<g/2 and gcd(g,h)=1 define

    rho_(r,g,h)(t)=S_(2r)(t^g)
                  -t^((r-1)g+h)-t^((r+1)g-h),
    q_(r,g,h)=(t^g+1)rho_(r,g,h).

This record proves M(F_2)>4/3>theta_0, complementing the r=3 result in L G0050, and proves that both the fixed-kernel limits as r tends to infinity and the joint limits as r and g tend to infinity exceed 4/3.
Here theta_0 is the positive root greater than one of x^3-x-1.

More precisely, the set

    B={r>=4 : M(F_r)<=theta_0}

is finite, though this proof does not identify it or prove it empty.
Any sequence of members of the family with r>=2, g tending to infinity and M(rho)<=theta_0 has a subsequence with one fixed r in B.
The measure-only corollary below extends this conclusion to all delay parameters in the K=1 endpoint-pair pattern; the exact repair budget remains asserted only for the central offsets defined above.
Thus a full uniform exclusion for all r>=2 has been reduced to an explicit finite, but non-effectively bounded, collection of analytic integrals.
That remaining assertion is not proved here.
The result does not classify the other two-block kernels or the second pairing pattern.

<a id="general-alternating-repair"></a>
## Essential repair persists for every r>=2

The completion expands to

    q=t^((2r+1)g)+1
         -t^((r-1)g+h)-t^(rg+h)
         -t^((r+1)g-h)-t^((r+2)g-h).

The [L G0048 graph](Yin_L_G0048_v1.md#positive-length-six-graph) applies with D=(2r+1)g, a=(r-1)g+h and b=rg+h.
Its four simple-cycle lengths are the four displayed negative exponents.
They are distinct, a<=b<D/2, and gcd(D,a,b)=1: b-a=g and gcd(g,a)=gcd(g,h)=1.
The graph is primitive, zero-one and unimodular, with D vertices and D+3 arrows.

For r>=3 its girth a exceeds 2g, so b_g(q)=b_(2g)(q)=0.
For r=2 the girth is g+h, still greater than g; furthermore 2g<2(g+h).
A primitive closed orbit of length below twice the girth must be a simple cycle, because a repeated vertex splits it into two nonempty closed walks, each at least as long as the girth.
None of the four simple-cycle lengths equals 2g.
Thus b_g(q)=b_(2g)(q)=0 also for r=2.
All other normalized net traces of q are nonnegative graph counts.

The block t^g+1 contributes -1 at g and +1 at 2g.
Exactly as in L G0048, the whole quotient therefore has

    b_g(rho)=1,       b_(2g)(rho)=-1,
    D(rho)=2g,       phi(2g)<=R_*(rho)<=g.

There are no other negative net traces.
For g a power of two the optimal repair degree is exactly g.
These are whole-polynomial assertions; no irreducibility or sign of the other noncyclotomic factors is assumed.

For r=1, by contrast,

    rho=t^(2g)-t^(2g-h)-t^g-t^h+1

is exactly the coprime length-five family of [L G0045](Yin_L_G0045_v1.md).
It already has a primitive nonnegative realization with edge excess two.
The extra block is therefore removable, and the preceding negative-trace argument does not apply.
This explains the structural significance of the distinction r=1 versus r>=2 independently of any numerical limit.

<a id="s4-measure-certificate"></a>
## A four-angle certificate for the S4 discriminator

Jensen's formula, with the same Tonelli justification as in L G0050, gives

    m(F_r)=(1/pi) integral_(0 to pi) H(A_r(exp(i theta))) dtheta,

where H(a)=0 for |a|<=2 and H(a)=acosh(|a|/2) otherwise.
We write m=log M.
For r=2 and theta=pi-v the real kernel becomes

    B_2(v)=1+2cos(v)+2cos(2v).

It is strictly decreasing on 0<v<=pi/4, since B_2'=-2(sin(v)+2sin(2v))<0.
On this interval B_2>2.
Hence the four right endpoints below provide lower integral rectangles.
Put beta(C)=(C+sqrt(C^2-4))/2.

| Right endpoint | Interval width | Exact C=B_2 at the endpoint | Strict beta lower bound |
| --- | --- | --- | --- |
| pi/12 | pi/12 | 1+sqrt(2+sqrt(3))+sqrt(3) | 22/5 |
| pi/6 | pi/12 | 2+sqrt(3) | 17/5 |
| pi/5 | pi/30 | 1+sqrt(5) | 14/5 |
| pi/4 | pi/20 | 1+sqrt(2) | 15/8 |

The endpoint values C strictly exceed, respectively,

    233/50, 37/10, 16/5, 241/100.

Use sqrt(3)>173/100 and sqrt(2+sqrt(3))>193/100 for the first comparison; the second uses sqrt(3)>17/10, the third sqrt(5)>11/5, and the fourth sqrt(2)>141/100.
All follow by positive rational squares.
Subtracting beta_bound+1/beta_bound from these rational lower bounds gives

    9/275, 1/170, 3/70, 1/600,

all positive.
Thus

    60m(F_2)>log[(22/5)^5(17/5)^5(14/5)^2(15/8)^3].

The product is 302529602582361/7812500, and its difference from (4/3)^60 is the positive rational

    2439986548937466580382687023461944415367561
    /331180924025126589955425259382812500.

This proves M(F_2)>4/3.
The inequality 4/3>theta_0 follows from (4/3)^3-4/3-1=1/27>0 and monotonicity of x^3-x-1 on x>=1.
By the fixed-r Lawton interface already checked in L G0050, only finitely many admissible (g,h) in this S4 family can have M(rho)<=theta_0.
No effective cutoff is obtained.

<a id="three-variable-kernel-limit"></a>
## One three-variable polynomial controls the growing kernels

The coordinating AI supplied the useful fixed polynomial

    P(x,W,z)=1+xW^2-W(x+1)(z+z^(-1)).

Its fixed-r specialization satisfies

    P_r(x,z):=P(x,x^r,z)=x^r(x+1)F_r(x,z),

so M(P_r)=M(F_r): the monomial and x+1 have measure one.

There is an exact elementary formula for its full three-variable measure.
Fix W,z on the unit circle and put a=z+z^(-1), which is real.
As a polynomial in x,

    P=(1-Wa)+x(W^2-Wa).

Both coefficients have modulus |W-a|.
Jensen in x therefore gives log|W-a|, and Jensen in W gives log max(1,|a|).
Consequently

    m(P)=(2/pi) integral_(0 to pi/3) log(2cos v) dv.       (1)

The exceptional simultaneous zero coefficients occur only on a Haar-null set.
Integrability can be justified without an extra convergence assumption.
The function log|W-a| has bounded positive part and, by the second Jensen identity, uniformly bounded integral of its negative part in W; Tonelli gives full integrability in (W,z).
Since |P|<=6 on the torus, its positive logarithmic part is bounded.
The first Jensen identity then bounds its negative part by that bounded positive part plus |log|W-a||.
Tonelli and Fubini justify both integrations in (1).

Here is an exact lower bound for (1).
Use seven intervals of width pi/24 with right endpoints j pi/24, j=1,...,7, and discard the remaining positive integral.
For 0<=u<=1,

    cos(u)>=C(u)=1-u^2/2+u^4/24-u^6/720.

The Taylor remainder has the displayed sign; C is decreasing for u>0 because C'=-u(1-u^2/6+u^4/120)<0.
Using pi<22/7 and 11*7/84<1, exact rational substitution gives

    2cos(j pi/24) >= 2C(11j/84)>c_j,

for

    (c_1,...,c_7)=(99/50,193/100,46/25,173/100,
                   79/50,141/100,121/100).

The seven positive comparison margins are retained in the exact arithmetic artifact.
Their product is

    product(c_j)=102470302201707/3125000000000,

and

    product(c_j)-(4/3)^12
       =2028119872377369787/1660753125000000000 >0.

Thus 12m(P)>log product(c_j)>12log(4/3), proving M(P)>4/3.

<a id="lawton-diagonal-kernels"></a>
## Diagonal use of the accepted univariate Lawton theorem

We first prove m(F_r)->m(P) as r tends to infinity, without invoking a multivariable-specialization theorem.
For each fixed r, Lawton applied to the two-variable polynomial P_r and vectors (1,H) gives

    m(P_r(t,t^H))->m(P_r)       as H->infinity.

Choose an integer H_r>r^2 large enough that the difference of these two logarithmic measures is less than 1/r.
Now

    P_r(t,t^(H_r))=P(t,t^r,t^(H_r)).

The relation parameter of (1,r,H_r) is exactly r.
A relation of sup norm strictly below r cannot have a nonzero third coefficient, because its H_r contribution then has absolute value greater than |nu_1+r nu_2|.
With third coefficient zero, any nonzero relation has nu_1=-r nu_2 and sup norm at least r.
The vector (r,-1,0) attains r.
Hence the accepted three-variable univariate Lawton theorem applies to this diagonal sequence.
Its measures tend to m(P), and the 1/r error proves m(F_r)->m(P).

Since m(P)>log(4/3)>log(theta_0), there exists an integer R such that M(F_r)>4/3 for all r>=R.
This proves the asserted finiteness of B, but provides neither R nor the members of B.
It is not an assertion that the intermediate kernels are monotone in r.

<a id="joint-lawton-relation"></a>
## Exact relation length excludes joint parameter escape

The actual completion in this record has the single fixed-polynomial description

    q_(r,g,h)(t)=P(t^g,t^(rg),t^(h-g)).

The negative exponent h-g is allowed in the accepted Laurent version of Lawton.
For v=(g,rg,h-g), its relation parameter is exactly

    q(v)=min(g,r).                                      (2)

Indeed any integer relation is

    g(nu_1+r nu_2)+(h-g)nu_3=0.

Because gcd(g,h)=1, a nonzero nu_3 must be divisible by g, forcing sup norm at least g.
If nu_3=0, a nonzero relation forces sup norm at least r.
Conversely (r,-1,0) and (g-h,0,g) are relations of sup norms r and g, respectively.
This proves (2).

It follows directly from the accepted fixed-polynomial Lawton statement that

    M(rho_(r,g,h))=M(q_(r,g,h))->M(P)>4/3

uniformly as min(g,r) tends to infinity, over all admissible h.
In particular there is a common T such that both g>=T and r>=T force M(rho)>4/3.
No effective T is supplied.

Now suppose g tends to infinity along a small-measure sequence with r>=2.
An unbounded subsequence of r would contradict this joint limit.
Passing to a subsequence therefore fixes r.
At this fixed r, the relation parameter of (g,h-g) is g, so the two-variable Lawton theorem gives M(rho)->M(F_r).
The fixed value must satisfy M(F_r)<=theta_0.
The certificates here and in L G0050 rule out r=2,3, and the preceding diagonal argument leaves only the finite set B.
This proves the initial finite-kernel reduction.
It does not prove B empty or give a uniform all-r measure gap.

<a id="general-k1-measure-corollary"></a>
## The measure reduction covers every K=1 delay

The Type-I K=1 pairing pattern permits the larger range

    R_(r,g,u)=S_(2r)(t^g)-t^u-t^(2rg-u),
    r>=2, g>=3, 0<u<2rg, gcd(u,g)=1.

Its completion is again the same fixed polynomial,

    (t^g+1)R_(r,g,u)=P(t^g,t^(rg),t^(u-rg)).

For any relation of the vector (g,rg,u-rg), a nonzero third coefficient must be divisible by g.
A relation with third coefficient zero has sup norm at least r.
Consequently

    q(g,rg,u-rg)>=min(g,r).

This lower bound suffices for uniform convergence to M(P)>4/3 as min(g,r) tends to infinity; an equality assertion is unnecessary.
At fixed r, the two-variable specialization of F_r has the coprime exponent vector (g,u-rg), whose relation parameter is

    max(g,|u-rg|)>=g.

Thus the same fixed-r convergence and the same finite-B argument apply uniformly throughout 0<u<2rg.
In particular the preceding conclusions are not confined to the central-offset slice u=(r-1)g+h.
This extension is only about measure.
Outside that slice the cycle lengths can fall below g, and the proof of D=2g and the lower repair bound given above does not apply.
No claim that the neutral block is essential for every such u is made.

## Evidence, actual review and stopping boundary

Exact rational checks for the S4 and three-variable bounds are retained in [J G0007](../computations/programs/Yin_J_G0007/readme.md), with [verify.py](../computations/programs/Yin_J_G0007/verify.py) and result.json (`mathematics/computations/outputs/Yin_J_G0007/result.json`).
The author first executed the arithmetic script successfully, and the coordinator subsequently ran both retained J programs with exit code zero.
The current commands, input/output homes and exact-versus-exploratory boundaries are in J G0007.
Exploratory quadrature that selected this route is separately retained in [diagnostics.py](../computations/programs/Yin_J_G0007/diagnostics.py) and diagnostics.json (`mathematics/computations/outputs/Yin_J_G0007/diagnostics.json`).
Those six limiting-integral values are explicitly uncertified, are not a polynomial/root sweep, and are not premises of any statement above.
No new numerical branch was opened after the exact certificates passed.

The original formal author/coordinator and separate whole/corollary checks are retained in [R511](../audits/reviews/Yin_R_G0511_v1.md#historical-alternating-author-finding), with their actual2026-10-07 date and separate self/unknown relationships.
The [separate historical finding](../audits/reviews/Yin_R_G0511_v1.md#historical-alternating-whole-finding) keeps the full-before-corollary and final-written-corollary scopes distinct.
The current C224 self-review and adoption do not establish that old reviewer's context isolation.
All statements still depend on the previously accepted full Lawton theorem, not a newly reviewed proof of it.
The bounded attempt stops at the explicit finite-kernel gap.
Neither that gap nor the other pairing patterns has been resolved, and no conclusion about the full Lehmer conjecture follows.
