---
author: Yin
---

# Exterior-controlled varying-seed factor gaps and exact half-degree reciprocal-core encoding

This retains the complete original 2026-10-08 [L139 mathematical argument](../ledger/Yin_L_G0139_v1.md).
The coordinator supplied and checked the root Poisson/Blaschke/uniform-delay mechanism; growth_arithmetic_status checked it and supplied the half-degree encoding, inverse/costs and cubic/quartic control, with both contributions explicit.
No current Task/E execution, source acquisition, mathematical program run or algorithm implementation is selected by this maintenance.

## Statement

For every nonconstant monic integer unit seed h with gcd(h,h*)=1, exterior count k and rational 0<epsilon<=1/4, assume every exterior root has modulus at least 1+4epsilon.
The exact two guards (2), or rational sufficient N>=ceil(2k/epsilon), give the full simple circle-root and reciprocal off-circle distribution and m(P)>log(1+epsilon) for every positive monic factor of both signs.
No coefficient height, seed degree or interior-root separation is bounded; a cyclotomic reciprocal gcd may be restored with its exact twist, while a varying positive gcd requires its own gap.
Every monic reciprocal irreducible positive core P of degree 2ell>=4 has the exact two-choice degree-(ell+1) seed encoding (9)--(10), a coprime choice, nonreciprocity, explicit height/l1 costs and only the added factor t+1.
The full inverse bijection holds without irreducibility or positive measure; even full returns vanish and odd returns give exactly twice the core norm, paying precisely the extra degree cost.
The necessary alternative (15) retains both exterior separation and exterior-count/delay cost.
The exact coprime cubic/irreducible quartic control (16)--(18) has seed and output exterior roots approaching one but Mahler measures tending to infinity, refuting only a seed-degree-only root annulus.
No fixed-degree Mahler-factor-gap refutation, near-one family, source theorem, root-isolation run or uniform original Mahler gap is supplied.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T10:23 |
| status | open |
| reason | Retain the complete exact original theorem and argument; actual current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original Sections1--7 and (1)--(18), repeated-root Poisson/strict endpoint/winding, exterior-only height-free contour and both twists, gcd scope, two-choice encoding/nonreciprocity, full inverse/height/norm costs, necessary alternative, exact irreducible cubic/quartic control and every root-annulus versus Mahler limitation. |
| argument | [Complete argument](#argument) | Entire original Sections1--7 and (1)--(18), repeated-root Poisson/strict endpoint/winding, exterior-only height-free contour and both twists, gcd scope, two-choice encoding/nonreciprocity, full inverse/height/norm costs, necessary alternative, exact irreducible cubic/quartic control and every root-annulus versus Mahler limitation. |
| dependency | [Exact retained input](Yin_C_G0340_v1.md#reciprocal-gcd-removal) | Only the complete own-degree reciprocal-gcd/twist and coprime residual interface; the new uniform estimates are derived directly. |
| dependency | [Exact retained input](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) | Exact cyclic norm and generic degree-cost normalization for the encoding identity; no new arithmetic mass follows. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T10:29 |
| status | proved |
| reason | Adopt the complete exact original theorem and retained argument after actual current whole self-review, preserving every finite quantifier, source/native limit, exact cost, original input and sufficient-versus-actual boundary. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original Sections1--7 and (1)--(18), repeated-root Poisson/strict endpoint/winding, exterior-only height-free contour and both twists, gcd scope, two-choice encoding/nonreciprocity, full inverse/height/norm costs, necessary alternative, exact irreducible cubic/quartic control and every root-annulus versus Mahler limitation. |
| argument | [Complete argument](#argument) | Entire original Sections1--7 and (1)--(18), repeated-root Poisson/strict endpoint/winding, exterior-only height-free contour and both twists, gcd scope, two-choice encoding/nonreciprocity, full inverse/height/norm costs, necessary alternative, exact irreducible cubic/quartic control and every root-annulus versus Mahler limitation. |
| dependency | [Exact retained input](Yin_C_G0340_v1.md#reciprocal-gcd-removal) | Only the complete own-degree reciprocal-gcd/twist and coprime residual interface; the new uniform estimates are derived directly. |
| dependency | [Exact retained input](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) | Exact cyclic norm and generic degree-cost normalization for the encoding identity; no new arithmetic mass follows. |
| review | [Actual current whole self-check](../audits/reviews/Yin_R_G0562_v1.md#current-varying-seed-encoding-finding) | Complete current statement, retained proof and every directly used interface; self-reviewed. All old findings retain their actual original inputs, dates, contexts and mathematical limits. |

## Complete retained argument

<a id="argument"></a>
<a id="varying-seed-uniform-factor-gap"></a>
### 1. A uniform theorem controlled by exterior roots and delay

Let h be a nonconstant monic polynomial in Z[t], with h(0) in {1,-1}, degree r, and

    h*(t)=t^r h(t^(-1)),       gcd(h,h*)=1.

There are no unit-circle roots: if h(beta)=0 and |beta|=1, real coefficients give h*(beta)=beta^r overline(h(beta))=0.
Let k be the number of roots outside the unit circle, counted with multiplicity.
The remaining r-k roots are strictly inside.
Both groups are nonempty because the product of all root moduli is one.
In particular 1<=k<=r-1.

Fix a rational 0<epsilon<=1/4 and assume only the exterior guard

    |beta|>=1+4epsilon for every exterior root of h.        (1)

No distance from the unit circle is assumed for interior roots.
Put

    R=1+epsilon,       c_epsilon=(5+4epsilon)/3<=2.

For an integer N>=1 and tau in {1,-1}, define

    G_(N,tau)=t^N h+tau h*.

It is monic of degree N+r, has constant coefficient tau, and G_(N,tau)*=tau G_(N,tau).
Suppose the two explicit inequalities

    N>=k(1+1/(2epsilon)),       R^N>c_epsilon^k           (2)

hold.
Then G_(N,tau) has exactly N+r-2k simple roots on the unit circle, exactly k roots outside |z|=R, and exactly k roots inside |z|=R^(-1), with multiplicity in the two off-circle counts.
In particular every positive-Mahler-measure monic factor P of either sign satisfies

    m(P)>log(1+epsilon).                                  (3)

A single rational sufficient condition for (2) is

    N>=ceil(2k/epsilon).                                  (4)

The threshold depends on the exterior count k and epsilon, without a coefficient-height bound or a seed-degree bound.
Thus a family of different seeds satisfying the same exterior guard and (4) has the uniform all-positive-factor gap (3), even if their degrees and coefficient heights are unbounded.
This is a restricted family theorem; its hypotheses are not claimed for arbitrary cores.

<a id="exterior-poisson-phase-count"></a>
### 2. Exact phase count with no interior-root separation cost

Since h has no roots on the unit circle, write

    h(e^(i theta))=|h(e^(i theta))| exp(i phi(theta))

with a continuously differentiable argument lift.
Its winding increment is 2pi(r-k).
On the circle one has

    G_(N,tau)(e^(i theta))
      =|h(e^(i theta))| exp(i(r theta-phi(theta)))
         [exp(i W_N(theta))+tau],
    W_N(theta)=(N-r)theta+2phi(theta).

Logarithmic differentiation, counting repeated roots, gives

    W_N'(theta)
       =N+sum_(h(beta)=0) (1-|beta|^2)/|e^(i theta)-beta|^2.
                                                               (5)

Indeed phi'=sum_beta Re(z/(z-beta)), and for |z|=1, 2Re(z/(z-beta))-1=(1-|beta|^2)/|z-beta|^2.

Every interior summand in (5) is strictly positive.
For an exterior root of modulus x, (1) gives

    (x^2-1)/|e^(i theta)-beta|^2
       <=(x+1)/(x-1)=1+2/(x-1)<=1+1/(2epsilon).

There is at least one interior root.
Consequently

    W_N'(theta)>N-k(1+1/(2epsilon))>=0                  (6)

under the first condition in (2).
The strictness is retained even at equality in that condition.
The phase increases by exactly

    W_N(theta+2pi)-W_N(theta)=2pi(N+r-2k).

A strictly increasing phase with this increment solves exp(i W_N)=-tau exactly N+r-2k times in a half-open period.
This is a positive integer, as is also forced by the strict increase.
The roots are simple: differentiating the displayed factorization at a zero gives a nonzero theta-derivative because the prefactor is nonzero and W_N'>0.

Reciprocity pairs every off-circle root with its inverse, retaining multiplicity.
The degree N+r therefore leaves exactly k exterior roots and k interior roots.
This is an exact count, not an asymptotic statement or just a lower bound on the circle roots.

<a id="height-free-exterior-contour"></a>
### 3. A height-free contour bound

On |z|=R, no root of h is present: its interior roots lie inside one and its exterior roots lie at modulus at least 1+4epsilon>R.
Real coefficients allow the product expression

    |h*(z)/h(z)|
       =product_(h(beta)=0) |1-overline(beta)z|/|z-beta|.

The identity

    |1-overline(beta)z|^2-|z-beta|^2
       =(R^2-1)(|beta|^2-1)                              (7)

shows that each interior-root ratio is strictly less than one, regardless of how close that root is to the unit circle.

For an exterior root of modulus x>=1+4epsilon, the ratio is maximized over the angle of z when z and beta have the same argument.
This follows either directly from (7), whose positive added numerator is fixed while the denominator is then smallest, or by writing |z-beta|^2=R^2+x^2-2Rx cos(theta).
The resulting bound is

    |1-overline(beta)z|/|z-beta|
       <=(Rx-1)/(x-R)
       <=[R(1+4epsilon)-1]/(3epsilon)=c_epsilon.          (8)

The second inequality uses the derivative (1-R^2)/(x-R)^2<0 of the first quotient.
Thus |h*(z)/h(z)|<=c_epsilon^k.
Under the second inequality in (2),

    |z^N h(z)|>|h*(z)|                 on |z|=R.

The contour homotopy z^N h(z)+u tau h*(z), 0<=u<=1, is nonzero on that circle.
Its winding number is constant, so G_(N,tau) has the same number N+r-k of roots inside R as z^N h.
Therefore it has exactly k roots outside R and none on the contour.
Section 2 already counted exactly k roots outside one.
Every exterior root is consequently outside R; reciprocity gives the interior bound R^(-1).
This proves the asserted root distribution.

A positive-measure monic factor has an exterior root by the root-product definition of Mahler measure.
That root has modulus greater than R, proving (3) without a Kronecker input.

To verify (4), first note that 2/epsilon>1+1/(2epsilon) for 0<epsilon<=1/4.
Also

    log(1+epsilon)>=epsilon/(1+epsilon)>=4epsilon/5.

Thus N>=2k/epsilon gives N log R>=8k/5>k log2>=k log c_epsilon.
The elementary inequality log2<1 already suffices for strictness.
Both inequalities in (2) follow.
All comparisons in (2), or the sufficient integer threshold (4), are effective with rational epsilon and the root count k; no transcendental comparison is needed if (4) is used.

The extension through a cyclotomic gcd is exact.
For a monic integral unit seed f, let g=gcd(f,f*) be its monic full gcd and f=g h.
As in the direct gcd argument of L G0134, g*=eta g with eta=g(0) in {1,-1}, gcd(h,h*)=1, and

    t^N f+sigma f*=g(t^N h+sigma eta h*).

If g is a product of cyclotomic polynomials, it contributes no positive irreducible factor.
Conditions (1)--(4) for the residual h therefore give (3) for every positive factor of both original signs.
If h=1 the entire product is cyclotomic and the assertion is vacuous.
A varying noncyclotomic gcd cannot be discarded in this extension; its positive factors would require their own gap.

<a id="universal-half-degree-delay-encoding"></a>
### 4. Every reciprocal core also has an exact short-delay encoding

Let P in Z[t] be monic, reciprocal, irreducible and of positive Mahler measure, with degree 2ell>=4.
Write

    P(t)=sum_(j=0)^(2ell) p_j t^j,
    p_j=p_(2ell-j),       p_0=p_(2ell)=1,
    Q(t)=(t+1)P(t)=sum_(j=0)^(2ell+1) q_j t^j.

Then q_j=p_j+p_(j-1), with coefficients outside the range of P interpreted as zero, and q_j=q_(2ell+1-j).
For e in {1,-1} set

    f_e(t)=e+(q_ell-e)t
                    +sum_(j=0)^(ell-1) q_j t^(ell+1-j).
                                                               (9)

This is a monic integral unit seed of degree r=ell+1 and constant coefficient e.
A direct coefficient comparison gives

    t^ell f_e+f_e*=(t+1)P.                              (10)

Indeed the coefficients at indices 0,...,ell-1 are q_0,..., q_(ell-1) from f_e*, the coefficients at ell and ell+1 are both e+(q_ell-e)=q_ell, and the remaining coefficients are their reciprocal partners.
Thus the delay is N=ell=r-1, the full degree is 2ell+1, and the unique positive irreducible core is exactly P.
Only the single cyclotomic factor t+1 has been added.

The seed may always be chosen with no reciprocal gcd.
A common factor of f_e and f_e* divides (t+1)P.
Because deg f_e=ell+1<2ell, the irreducible polynomial P cannot divide it.
Since P(-1)!=0, the full gcd is either 1 or t+1.
But

    f_+(t)-f_-(t)=2(1-t),
    f_+(-1)-f_-(-1)=4.                                  (11)

At most one choice vanishes at -1.
Choosing the other gives gcd(f_e,f_e*)=1.
This is a two-choice exact integer test.
The chosen seed has no unit-circle roots by the elementary gcd argument already used in Section 1.

In fact both choices in (9) are nonreciprocal up to sign.
Such reciprocity would have to be f_e*=e f_e, by comparison of leading coefficients.
Then t^ell+e would divide (t+1)P.
It is relatively prime to P because its degree ell is less than deg P, and P is irreducible.
It would therefore divide t+1, impossible for ell>=2.
Nonreciprocity, removal of the reciprocal gcd, and a unique positive core hence do not by themselves restrict the reciprocal inputs encoded in (10).

Let H(P)=max_j|p_j| and ||P||_1=sum_j|p_j|.
The construction has the explicit costs

    H(f_e)<=2H(P)+1,
    ||f_e||_1<=||P||_1+2.                               (12)

For the second inequality,

    ||f_e||_1<=2+sum_(j=0)^ell |q_j|
       <=2+2sum_(j=0)^(ell-1)|p_j|+|p_ell|
       =2+||P||_1.

These are costs inherited from the input, not uniform bounds on all reciprocal cores.
The construction requires neither a large arbitrary coefficient multiplier nor a claimed new small-measure seed.
Its seed degree grows linearly with the actual core degree.

<a id="encoding-inverse-and-cyclic-cost"></a>
### 5. The inverse map and unchanged cyclic-norm certificate

For each fixed e, (9) is a coefficientwise bijection between all monic reciprocal integer polynomials of degree 2ell and all monic integer polynomials of degree ell+1 with constant coefficient e.
Irreducibility and positive measure are unnecessary for this algebraic assertion.
Indeed, for any such f, the polynomial t^ell f+f* is reciprocal of odd degree 2ell+1, so it vanishes at -1.
Exact monic division by t+1 gives a monic reciprocal integer polynomial P of degree 2ell.
Its coefficients recover (9).

More explicitly, if c_i are the coefficients of f, read

    q_j=c_(ell+1-j) for 0<=j<ell,
    q_ell=c_1+e,
    p_0=1,       p_j=q_j-p_(j-1) for 1<=j<=ell,

and reflect the p_j across degree 2ell.
This recovers the complete input.
Thus (10) is a genuine change of coefficient coordinates, not an arithmetic assertion proved about P merely by presenting it as a delay factor.

Its cyclic-norm bookkeeping is also exact.
For R_n(H)=|Res(H,t^n-1)|, a noncyclotomic irreducible P has R_n(P)>0 at every positive integer n.
Equation (10) gives

    R_n(t^ell f_e+f_e*)=0                  if n is even,
    R_n(t^ell f_e+f_e*)=2 R_n(P)           if n is odd.    (13)

At every odd return, the generic full-presentation and actual-core [certificates](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) are identical:

    [log R_n(t^ell f_e+f_e*)-(2ell+1)log2]/n
                  =[log R_n(P)-2ell log2]/n.             (14)

The extra norm factor exactly pays the extra degree cost.
No return exponent, prime-ideal mass, or improvement to the aggregate criterion follows from the encoding alone.
At the specific return times n=k'ell, (13) still applies: even times vanish, and odd times have only this exact cancellation.
This does not assert a failure of the actual core's arithmetic coverage at those times.

Combining the two principal results gives a precise necessary parameter alternative.
Choose the coprime seed in (9), and let k be its exterior-root count.
For any rational 0<epsilon<=1/4, if M(P)<1+epsilon, then at least one of the following holds:

    some exterior seed root has modulus <1+4epsilon;
    k>ell epsilon/2.                                    (15)

Otherwise (1) and N=ell>=2k/epsilon would imply (3), contradicting M(P)<1+epsilon.
This locates the missing seed information; it is not a proof that either alternative actually provides a small Mahler family, nor a verification of arithmetic coverage.

<a id="fixed-degree-annulus-control"></a>
### 6. Fixed degree does not itself give a uniform root annulus

Here is an exact control separating root-annulus failure from Mahler-gap failure.
For integers n>=3, let A=n^2 and put

    P_A(t)=t^4-A t^3+(2A-1)t^2-A t+1,
    q_A(x)=x^2-Ax+2A-3,
    P_A(t)=t^2 q_A(t+t^(-1)).                           (16)

The discriminant of q_A is (A-4)^2-4.
For A>=9 it lies strictly between (A-5)^2 and (A-4)^2, so q_A is irreducible over Q.
For either root x, K=Q(x) is quadratic.
Moreover,

    Norm_(K/Q)(x^2-4)=q_A(2)q_A(-2)=4A+1=4n^2+1.

This is strictly between (2n)^2 and (2n+1)^2 and is not a rational square.
Hence x^2-4 cannot be a square in K.
The equation t^2-xt+1 is irreducible over K.
A root generates x=t+t^(-1), so has degree four over Q; therefore P_A is irreducible.

Put u=A-4>=5.
The shifted quadratic is

    q_A(2+y)=y^2-u y+1.

Its smaller root y_A lies in (0,2/u), as follows from its positive value at zero and negative value 4/u^2-1 at 2/u.
Its two roots are positive.
Thus both roots x_A<X_A of q_A are greater than two, and x_A=2+y_A tends to two.
The corresponding exterior roots lambda_A,mu_A of P_A satisfy

    lambda_A+lambda_A^(-1)=x_A,
    mu_A+mu_A^(-1)=X_A,
    lambda_A->1,       mu_A>A-4->infinity.                (17)

For the last bound, x_A<3 gives X_A=A-x_A>A-3, and mu_A=X_A-mu_A^(-1)>X_A-1.
The other roots are the positive reciprocals.
Consequently M(P_A)=lambda_A mu_A>A-4 tends to infinity.
This is not a small-Mahler example.

The half-degree encoding at ell=2 and e=-1 is the cubic seed

    f_A(t)=t^3+(1-A)t^2+A t-1,
    t^2 f_A+f_A*=(t+1)P_A.                              (18)

It has gcd(f_A,f_A*)=1: that gcd divides (t+1)P_A, its degree is too small to contain P_A, and f_A(-1)=-2A-1 is nonzero.
Thus even among coprime cubic seeds, unbounded coefficient height can give exterior roots of the delay output approaching the circle.
There is no common root-free annulus about the unit circle for all such delay outputs based only on seed degree.

The exterior seed guard also genuinely degenerates in this control.
For y>=0,

    f_A(1+y)=1+(5-A)y+(4-A)y^2+y^3.

It is positive at y=0 and at y=2/A its value is

    -1+6/A+16/A^2+8/A^3<0                  for A>=9.

The inequality follows by decreasing each reciprocal-power term from its value at A=9, where their sum is 638/729<1.
There is therefore an exterior seed root in (1,1+2/A).
No common positive epsilon can satisfy (1) for this family.
The delay N=2 is also far below the sufficient threshold (4).
Both costs remain visible.

<a id="varying-seed-remaining-scope"></a>
### 7. What changes, and what remains unresolved

The uniform theorem supplies a new varying-seed class on which all positive factors have a gap, with a threshold depending only on the number and radial separation of exterior seed roots.
It needs neither bounded coefficient height nor separation of interior roots from the circle.
It applies to both delay signs and does not rely on there being a unique positive factor.

The half-degree encoding supplies the complementary exact coverage diagnostic.
Every reciprocal irreducible core of degree at least four already has a coprime nonreciprocal seed of degree half the core degree plus one, at delay one less than the seed degree, with only one cyclotomic factor added and small explicit coefficient overhead.
Consequently those presentation properties alone cannot be additional evidence toward a gap or cyclic-norm coverage.
The exterior-root and relative-delay hypotheses in Sections 1--3 add substantive information that the encoding does not supply.

The fixed-degree control rules out a seed-degree-only version of the uniform root-annulus statement.
It does not rule out a common positive Mahler-factor gap for all seeds of one fixed degree: its irreducible quartic measures instead tend to infinity.
Whether that stronger factor-gap assertion holds when seed degree is fixed, coefficients are unbounded and delays are arbitrary remains unresolved in this account.
No uniform assertion over all seed degrees, near-one counterexample family, or solution of G0001 is claimed.
