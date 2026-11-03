---
author: Yin
---

# A quadratic trace-field prime selector and its fixed-mass cost

Date: 2026-10-09 (Asia/Hong_Kong).
Completed bounded G0001/S_G0008 record written by assigned AI `growth_arithmetic_status` for Yin.
This AI selected and checked the direct application of the retained BS96 theorem to the quadratic trace extension, its actual ideal mass, rational-ramification guard, field/height normalization, and the comparison below.
The coordinator supplied the general-k calculus bound in Section 3 and proposed the ramified-prime quartic control in Section 4; this AI checked and completed their written details.
Complete noncontributor independent AI review and adoption are recorded below.
No new source search, acquisition, numerical run, prime scan, or canonical edit was performed.

The external input is only the already accepted conditional statement [BS96-U001](../audits/literature/BS96/Yin_U001.md#bs96-u001).
Its analytic proof and numerical constants are not newly audited.
The trace field and involution are from [L66](Yin_L_G0066_v1.md#reciprocal-trace-domain), the exact ideal-norm and binomial lifting interfaces from [L74](Yin_L_G0074_v1.md#content-versus-ideal-norm), and the field-discriminant/height estimate from [L75](Yin_L_G0075_v1.md#chebotarev-period-cost).
[L161](Yin_L_G0161_v1.md#trace-factor-common-exponent) and [L162](Yin_L_G0162_v1.md#matching-union-local-cost) specify the existing exact matching and fraction obligations.

<a id="quadratic-trace-prime-selector"></a>
## 1. An actual selector using the original degree-d field

Let P be monic, irreducible, reciprocal and noncyclotomic in Z[t], of degree d=2s>=4 and constant coefficient one.
Choose a root alpha and put

    K=Q(alpha),     F=Q(alpha+alpha^(-1)),
    m=log M(P)>0,   D_K=|disc(K)|.

L66 gives [F:Q]=s and [K:F]=2.
The extension K/F is Galois, with its nonidentity automorphism sigma(alpha)=alpha^(-1).
K need not be Galois over Q.

Under exactly the ERH scope retained in BS96-U001, apply its arbitrary-base theorem to E=K over F and the class {sigma}.
It supplies a degree-one prime ideal p_F of F, unramified in K/F, with Frobenius sigma and

    Norm_(F/Q)(p_F)=p,
    p<=U_K=(4 log D_K+2.5d+5)^2.                           (1)

Here p is a rational prime.
Both the absolute degree d and the absolute discriminant D_K belong to the top field K of this quadratic extension.
They are not substituted into a theorem about the normal closure: the actual theorem is applied to a different Galois extension, K/F.
Thus (1) is a legitimate whole-splitting-field bypass.

The degree-one statement in the accepted source is essential.
Without it, a base prime of residue degree f would instead give Norm(p_F)=p^f and the associated return exponent p^f+1.
No newly adopted unconditional or generalized ERH theorem is being used here.

There is a unique prime q of K over p_F.
Inertia in the quadratic extension gives

    e(q/p_F)=1,     f(q/p_F)=2,     Norm_(K/Q)(q)=p^2.

The arithmetic Frobenius congruence at q is

    alpha^p=sigma(alpha)=alpha^(-1) modulo q.

Consequently alpha^(p+1)-1 belongs to q.
This is an actual prime ideal of the original field K and not a repeated count over conjugate embeddings.

The rational prime p may ramify in F/Q.
The source's relative unramifiedness does not silently exclude this case.
It causes no problem here: the absolute residue degree of q is still two, so the integer norm valuation contributed by q is at least two.
Neither p not dividing disc(P) nor unramifiedness in the whole splitting field is required.
In particular alpha need not generate the full residue field at a bad power-basis prime.

<a id="quadratic-trace-ideal-mass"></a>
## 2. All automatic lifts and the remaining discriminant cost

Normalize v=ord_q by v(q)=1.
Then v(p)=e_q>=1.
If v(x-1)=a>=1, the binomial expansion gives

    v(x^p-1)>=min(a+e_q,pa)>=a+1.

This also holds at p=2; cancellation only increases the valuation.
Induction therefore gives, for every integer r>=0,

    ord_q(alpha^((p+1)p^r)-1)>=r+1,
    v_p(C_((p+1)p^r))>=2(r+1),
    C_n=|Norm_(K/Q)(alpha^n-1)|>0.                         (2)

Using L74's full-degree archimedean bound C_n<=2^d exp(nm),

    m>=B_1(p,r)
      :=[2(r+1)log p-d log 2]/[(p+1)p^r].                 (3)

The coefficient two is the actual absolute residue-degree contribution of this selected q.
There is no multiplier s from the number of trace embeddings.
Other prime ideals over the same p and exceptional initial valuation depths may contribute more; the selection theorem has not bounded that extra mass below.

For a declared bounded-measure domain m<=m_0, the retained discriminant inequality gives

    log D_K<=log|disc P|<=d log d+(2d-2)m_0,
    U_K<=[4d log d+8(d-1)m_0+2.5d+5]^2
        =O_(m_0)(d^2(log d)^2).                           (4)

The power-basis index only reduces D_K from |disc P|; it has not been assumed to be one.
Equation (4) retains the field, degree and height cost without introducing the much larger splitting field.
It supplies an upper bound for the selected prime, not a lower bound on the least such prime or a bound for a prime with many matched trace directions.

For completeness, (1)--(3) do provide a positive, explicitly degree-dependent certificate.
Choose

    r=ceil(d log 2/(2 log p)).

Then the numerator in (3) is at least 2 log p, and

    n=(p+1)p^r<=p(p+1)2^(d/2)<=U_K(U_K+1)2^(d/2),
    m>=2 log 2/[U_K(U_K+1)2^(d/2)].                       (5)

This weak conditional degree-dependent bound is not presented as a new competitive Mahler lower bound.
Its role is to make the finite prime-selection and subsequent exponent costs explicit.

<a id="fixed-matched-mass-envelope"></a>
## 3. Why locating one pair does not close the common-cost target

More generally suppose only the automatic floor from k matched pairs is supplied, with 1<=k<=d/2.
The certificate obtained by this floor and the same archimedean estimate is

    B_k(p,r)
      =[2k(r+1)log p-d log 2]/[(p+1)p^r].                 (6)

This hypothesis concerns a proved lower floor; it does not assert that the true norm or valuations equal that floor.
Since n=(p+1)p^r>p^(r+1), a positive value of (6) requires

    n>2^(d/(2k)).                                        (7)

Moreover (r+1)log p<log n, so

    B_k(p,r)
      <[2k log n-d log 2]/n
      <=(2k/e)2^(-d/(2k)).                               (8)

The last inequality holds for every real n>0.
Differentiating f(n)=(2k log n-d log 2)/n gives its unique maximum at log n=1+d log 2/(2k), where its value is the right side of (8).
This proves the bound without restricting the prime's size or using the prime-selection estimate (1).

In particular the one-pair selector has

    B_1(p,r)<=(2/e)2^(-d/2)                               (9)

for every prime p and every automatic lift r.
Thus even idealized location of that one local pair cannot make this restricted certificate degree-uniform.
Equation (8) is not an upper bound on m, C_n, any exceptional depth, or the additional mass at other ideals.
It also does not forbid a different joint archimedean estimate.
The exponential optimization phenomenon has a related actual-family instance in [L150](Yin_L_G0150_v1.md#seeded-return-continuation-boundary); the new selected interface here is the arbitrary-base quadratic prime theorem and its exact original-field mass, not the calculus bound by itself.
L159's separate average-capacity limitation is not being imposed on this individual return exponent.

<a id="trace-selector-control-and-stop"></a>
## 4. Retained actual control and the scope of the stop

Use the existing irreducible quartic Salem input

    P_4=t^4-t^3-t^2-t+1,
    T_4=x^2-x-3

and let z be the trace generator.
Its relation gives

    Delta=z^2-4=z-1,       Norm_(F/Q)(Delta)=T_4(1)=-3.

Since disc(T_4)=13 is squarefree, O_F=Z[z].
At the rational prime 3 the trace polynomial reduces to z(z-1), so 3 splits unramified in F into the two degree-one primes

    p_0=(3,z),       p_1=(3,z-1).

At p_0 the quadratic t^2-z t+1 reduces to t^2+1, irreducible over F_3, with nonzero discriminant 2.
Thus p_0 is unramified and inert in K/F.
Its unique prime q in K has absolute norm 9 and supplies (2) at p=3.
Taking r=1, n=12, gives

    m(P_4)>=[4 log3-4 log2]/12=log(3/2)/3>0.             (10)

This useful local direction coexists with actual rational ramification elsewhere above 3.
Indeed p_0 does not divide Delta, whereas p_1 does.
The norm Delta=-3 therefore gives ord_(p_1)(Delta)=1.
Also K=F(sqrt(Delta)).
For a prime Q of K over p_1, integer valuations satisfy

    2 ord_Q(sqrt(Delta))=ord_Q(Delta)=e(Q/p_1).

Hence e(Q/p_1) is even and must equal two.
Thus 3 ramifies in K and consequently in its normal closure.
The whole-splitting-field unramifiedness hypothesis of L160 is not satisfied at this prime, but the present selected local ideal remains valid.
Consistently, disc(P_4)=13^2 T_4(2)T_4(-2)=-3*13^2.

These are manual exact reductions on a retained actual input, not a new prime scan or numerical run.
The measure is fixed away from one, and the example supplies no varying-degree or near-one coverage.
It demonstrates a genuine extension of the usable local domain, not additional simultaneous mass.

The bounded selection therefore has a precise outcome.
The direct relative quadratic theorem replaces the splitting field by K and gives a polynomial-in-degree prime bound on a bounded-measure domain, conditional on its retained ERH hypotheses.
In exchange, the proved guaranteed mass is only one quadratic local direction.
Neither degree-one prime selection nor the induced quadratic character supplies many such directions at the same rational p.

Stop this one-pair selection plus automatic-lift floor as a candidate for a degree-uniform gap.
Continuing would require a new simultaneous-mass or actual-depth statement, or a different archimedean cost; another constant improvement in (1) does not address (8).
No conclusion is drawn about the least prime with large matching count, actual norm mass, or the unrestricted Task.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0062_v1.md#complete-independent-written-review-and-adoption), with its original inspected scope and relationship.
