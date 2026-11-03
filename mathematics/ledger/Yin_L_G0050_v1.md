---
author: Yin
---

# G0001: a uniform Mahler obstruction for the essential-block family

The complete current mathematical home is [Yin_C_G0271_v1](../claims/Yin_C_G0271_v1.md#argument), adopted at 2026-10-21T06:39 after the [actual complete current self-check](../audits/reviews/Yin_R_G0532_v1.md#current-complete-uniform-measure-finding).
The original2026-10-07 mathematics and still-needed fixed review input below retain their original scope and date; this is no new research run.


Date: 2026-10-07.
Direct argument by assigned AI assess_shortness_route and the coordinating AI for Yin.
This continues [L G0048](Yin_L_G0048_v1.md#unbounded-essential-block-family).
The source input is precisely Lawton's specialization theorem as retained in [Den09 U002, Theorem 14 / Example 15](../audits/literature/Den09/Yin_U002.md).
The coordinating AI rechecked the exact theorem statement on printed page 12 of the retained Den09 PDF: arbitrary integer specialization vectors, the sup-norm relation parameter, and the full polynomial limit including zeros.
The original Lawton proof, particularly its control near zeros, remains an accepted external statement and was not audited here.
Everything below concerning the integral and its lower bound is a direct argument.

<a id="essential-family-measure-obstruction"></a>
Write theta_0 for the positive root greater than one of x^3-x-1.
Put

    S_6(x)=x^6-x^5+x^4-x^3+x^2-x+1,
    r_(g,h)(t)=S_6(t^g)-t^(2g+h)-t^(4g-h),

where g>=3, 1<=h<g/2 and gcd(g,h)=1.
There is an integer G such that

    M(r_(g,h))>4/3>theta_0

for every g>=G and every such h.
In particular only finitely many admissible pairs (g,h) in this entire offset family can meet M<theta_0; their whole-polynomial repair degrees are consequently bounded.
This assertion does not identify those pairs or exclude any untested finite g.
The proof supplies no effective value of G.
This is an exclusion of a particular infinite-family mechanism, not a general Lehmer bound.

<a id="offset-essential-repair"></a>
## The repair obstruction survives every permitted offset

Direct multiplication gives

    q_(g,h)=(t^g+1)r_(g,h)
       =t^(7g)+1-t^(2g+h)-t^(3g+h)-t^(4g-h)-t^(5g-h).

The [positive graph of L G0048](Yin_L_G0048_v1.md#positive-length-six-graph) applies with D=7g, a=2g+h and b=3g+h.
The inequalities a<=b<D/2 follow from h<g/2.
The support gcd is one: the difference b-a=g, and gcd(g,2g+h)=gcd(g,h)=1.
The graph is therefore primitive, zero-one and unimodular, with 7g vertices and 7g+3 arrows.
Its four distinct simple-cycle lengths are

    2g+h, 3g+h, 4g-h, 5g-h.

The girth is 2g+h>2g.
In particular its normalized net traces b_j(q) vanish for j<=2g and are nonnegative for every j.
Here b_j is the primitive-orbit count, or equivalently j^(-1) times the Mobius transform of the power traces.
Net traces add under multiplication of monic polynomials.

The factor t^g+1=(t^(2g)-1)/(t^g-1) contributes -1 at index g, +1 at index 2g, and zero at every other index.
Thus

    b_g(r)=1,       b_(2g)(r)=-1,

and every other b_j(r) is nonnegative.
With the whole-polynomial repair conventions of L G0048,

    D(r)=2g,       phi(2g)<=R_*(r)<=g.

Indeed any cyclotomic repair must contribute positively at index 2g, so it contains a factor Phi_m with 2g dividing m.
Its degree is at least phi(2g).
The block t^g+1 gives an actual repair of degree g back to the displayed nonnegative graph.
For g=2^k, k>=2, the minimum is exactly R_*(r)=g.
This is a statement about the whole r, without assuming irreducibility; no trace obstruction for an individual irreducible factor follows automatically.

<a id="essential-family-mahler-limit"></a>
## A single Laurent polynomial governs all offsets

Let

    F(x,y)=A(x)-y/x-x/y,
    A(x)=x^3+x^(-3)-x^2-x^(-2)+x+x^(-1)-1.

The normalization is exact:

    t^(-3g)r_(g,h)(t)=F(t^g,t^h).

Multiplication by this monomial does not change Mahler measure.
For the vector (g,h), every nonzero integer relation is a nonzero multiple of (h,-g), because gcd(g,h)=1.
Therefore the relation parameter q(g,h) in the accepted Lawton theorem is exactly g.
It follows that

    M(r_(g,h)) -> M(F)

as g tends to infinity, uniformly over the admissible h.
The uniform assertion is just the meaning of the source's limit as q(g,h) tends to infinity: otherwise a sequence of exceptions with g tending to infinity would contradict that limit.
No rate is supplied by this use of Lawton.

We next prove M(F)>4/3 directly.
Write m=log M.
For x=exp(i theta), A(x) is real and equals

    A(theta)=2cos(3theta)-2cos(2theta)+2cos(theta)-1.

Changing y to xz in the inner circle integral turns F into A(theta)-z-z^(-1).
Jensen's formula for z^2-A(theta)z+1 gives

    m(F)=(1/pi) integral_(0 to pi) H(A(theta)) dtheta,

where H(a)=0 for |a|<=2 and H(a)=acosh(|a|/2) otherwise.
The equality uses the symmetry theta -> 2pi-theta.
The inner formula is Jensen's formula even when roots lie on the circle.
Integrability for this particular two-variable polynomial can be checked directly: |F|<=9 on the torus, so its positive logarithmic part is bounded by log 9.
For each fixed theta, Jensen gives a finite inner integral H>=0, hence the integral of the negative logarithmic part is at most log 9.
Tonelli applied to that nonnegative part now bounds its full two-variable integral.
Both parts are integrable, justifying Fubini and the displayed formula even across the torus zeros.

<a id="four-interval-mahler-certificate"></a>
## Four standard angles give an exact lower bound

For theta=pi-v put

    B(v)=-A(pi-v)=1+2cos(v)+2cos(2v)+2cos(3v).

On 0<v<=pi/5, all three sines in

    B'(v)=-2[sin(v)+2sin(2v)+3sin(3v)]

are positive.
Thus |A(theta)| is strictly increasing on [4pi/5,pi]; it is already greater than two at the left endpoint.
Define beta(C)=(C+sqrt(C^2-4))/2 for C>2.
Then H(A)=log beta(|A|) there.

Use the four successive intervals with the following left endpoints and widths:

| Left endpoint | Width | Exact left value C=|A| | A strict lower bound for beta(C) |
| --- | --- | --- | --- |
| 4pi/5 | pi/30 | (3+sqrt(5))/2 | 21/10 |
| 5pi/6 | pi/24 | 2+sqrt(3) | 17/5 |
| 7pi/8 | pi/24 | 1+sqrt(2)+sqrt(2-sqrt(2))+sqrt(2+sqrt(2)) | 24/5 |
| 11pi/12 | pi/12 | 1+(3sqrt(2)+sqrt(6))/2+sqrt(3) | 59/10 |

Here is a rational check of every radical comparison.
The respective values C strictly exceed

    13/5,       37/10,       501/100,       6071/1000.

For the first two entries use sqrt(5)>11/5 and sqrt(3)>17/10.
For the third use 141/100<sqrt(2)<71/50, sqrt(2-sqrt(2))>19/25 and sqrt(2+sqrt(2))>46/25; the last two inequalities follow by squaring and the preceding bounds on sqrt(2).
For the fourth use sqrt(2)>707/500, sqrt(6)>61/25 and sqrt(3)>173/100.
All these are direct comparisons of positive rational squares.

If c denotes one of the four displayed rational lower bounds and r the corresponding proposed beta bound, then

    c-(r+1/r) = 1/42, 1/170, 1/600, 89/59000,

respectively.
All are positive.
Since C=beta(C)+beta(C)^(-1) and u+u^(-1) is strictly increasing for u>1, the beta bounds follow.

Monotonicity on the four intervals now gives

    120 m(F) > log[(21/10)^4 (17/5)^5 (24/5)^5 (59/10)^10].

The product inside the logarithm exceeds (4/3)^120.
Clearing denominators reduces this to the exact integer inequality

    3^129 7^4 17^5 59^10 > 2^239 5^24.

The difference of its two sides is

    8974787145568340055163490857248851240275402837848061222773499890465546707334700093441531,

which is positive.
Therefore m(F)>log(4/3).
Also (4/3)^3-4/3-1=1/27>0, and x^3-x-1 is strictly increasing for x>=1.
This proves 4/3>theta_0 and completes the asserted uniform eventual exclusion.

<a id="independent-taylor-limit-check"></a>
## An independent exact check of the same strict inequality

A separate certificate uses v=j pi/24, j=1,...,5, and monotonicity of B on [0,5pi/24], where all three derivative sines are still positive.
For 0<=u<=2 the alternating Taylor bound gives

    cos(u)>=C(u)=1-u^2/2+u^4/24-u^6/720.

The function C is decreasing for u>0: its derivative is -u(1-u^2/6+u^4/120), and the parenthesis is positive.
From pi<22/7, all arguments in question are less than 2, and

    B(j pi/24) >= 1+2 sum_(k=1 to 3) C(11jk/84).

For the five rational numbers

    r_j = 33/5, 29/5, 24/5, 17/5, 17/10,

the last rational lower bound exceeds r_j+1/r_j by, respectively,

    1501867811237/139114020519936,
    3008031551863/28652745703680,
    1506916427/86740254720,
    8886782197/262444330260,
    39758216785363/1074971976744960.

Integrating over the five intervals of width pi/24 therefore gives 24m(F)>log product(r_j).
Their product is 3318876/3125, and

    product(r_j)-(4/3)^24
      =57739308097115356/882592301503125 >0.

This independently proves the same strict bound.
Exact rational arithmetic for both certificates is retained in [the J G0006 script](../computations/programs/Yin_J_G0006/limit/verify.py) and its successful output (`mathematics/computations/outputs/Yin_J_G0006/limit/result.json`).
The coordinating AI independently read and reran the retained script with `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0006/limit/verify.py` (Python 3.12.14).
These checks contain no numerical integration, finite-g scan or effective convergence cutoff.
The program is auxiliary to the displayed analytic proof.

<a id="essential-support-next-step"></a>
## What must change in the next arithmetic test

Changing h within the preceding family cannot evade this limit obstruction.
A concrete change of support, rather than a change of offset, is to replace S_6 by

    S_4(x)=x^4-x^3+x^2-x+1,
    rho_(g,h)=S_4(t^g)-t^(g+h)-t^(3g-h).

For the same admissible g,h its completion is

    (t^g+1)rho_(g,h)
       =t^(5g)+1-t^(g+h)-t^(2g+h)-t^(3g-h)-t^(4g-h).

The L G0048 graph has D=5g, a=g+h, b=2g+h, support gcd one and girth g+h.
It again is primitive, zero-one and unimodular with edge excess three.
Although the girth is now below 2g, every closed orbit of length less than twice the girth is a simple cycle.
None of the four simple-cycle lengths g+h, 2g+h, 3g-h, 4g-h equals 2g.
Thus b_g(q)=b_(2g)(q)=0, and the same subtraction of t^g+1 proves D(rho)=2g and phi(2g)<=R_*(rho)<=g.

Its limiting Laurent polynomial instead has

    F_2(x,y)=x^2+x^(-2)-x-x^(-1)+1-y/x-x/y,
    A_2(c)=4c^2-2c-1,      c=cos(theta).

The identical Jensen argument supplies its exact one-dimensional integral, and Lawton supplies uniform convergence over these offsets.
No numerical value, comparison with theta_0 or eligible irreducible core is asserted for this different limit.
It is a concrete alternative support with the essential repair mechanism preserved; whether its limiting measure is smaller enough is a new obligation, not a conclusion of this record.

A broader next target is to classify reciprocal length-six Phi_2(t^g) block patterns and prove or disprove a structural alternative: either an essential growing block forces a measure bound above the small-core range, or a controlled shorter completion removes it.
The present proof settles the S_6 pattern and shows why repeatedly tuning its offsets cannot substitute for that structural question.
It does not establish the proposed alternative for all patterns.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0015_v1.md#review-and-limitations), with its original inspected scope and relationship.
