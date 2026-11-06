---
author: Yin
---

# Moving zero-measure inputs: uniform layer costs and the exceptional low-order factors

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The coordinating contributor selected varying cyclotomic pairs, the Fourier lower bound and the reduction to actual small factors.
The construction contributor established uniform discrete costs by a short geometric factor and a separate individual-layer estimate.
The bottleneck contributor checked complete primitive content and constructed an explicit example with both large content and genuine global factor growth.
The source contributor found the reciprocal-root filter and inspected the original Kroneckerian-field inequality used below.
These are ordinary author-development contributions and source-statement uses, not an independent project review or a resolution of the Task.

<a id="moving-zero-measure-pair-scope"></a>
## Inputs, normalization and the construction question

[V1](Yin_L_G0458_v1.md#homogeneous-layer-moving-source-limit) leaves a real diagonal limitation: its fixed-pair phase limit and content constants cannot be applied uniformly when the input pair changes.
The present construction tests moving inputs whose own logarithmic Mahler measures are exactly zero, while retaining all integer content and every actual positive factor of the output.
The known [factor-proliferation bridge](Yin_L_G0450_v1.md#positive-factor-counterexample-bridge) would need bounded complete primitive measure and unbounded positive irreducible-factor count.

Let A and B be nonzero primitive integer polynomials of zero measure.
They may change freely with the outer exponent N>=1.
By the accepted Kronecker characterization they have the form
\[
 A=\eta_A z^r C,\qquad B=\eta_B z^s D,\qquad
 \eta_A,\eta_B\in\{1,-1\},                            \tag{Z1}
\]
where C,D are monic products of cyclotomic polynomials, including the empty product.
Repeated factors are allowed.
A common monic zero-measure factor can be removed from both inputs: it contributes only its N-th power, of zero measure and content one, to
\[
                    F_N=A^N-B^N,\qquad
                    P_N=\operatorname{prim}(F_N).     \tag{Z2}
\]
Thus assume the inputs are coprime, with min(r,s)=0.
The ratio A/B is assumed nonconstant.
For proportional zero-measure inputs it is plus or minus one, and the nonzero primitive output has zero measure; an identically zero output is not a candidate.

Write m for total logarithmic Mahler measure, cont for the positive coefficient gcd and prim(H)=H/cont(H).
All positive irreducible factors and their multiplicities are counted in r_+.
No leading coefficient, content or zero root is omitted from this convention.

The exact integer layers remain
\[
       F_N=\prod_{d\mid N}\Phi_d(A,B),\qquad
       \operatorname{prim}(F_N)
           =\prod_{d\mid N}\operatorname{prim}(\Phi_d(A,B)). \tag{Z3}
\]
Their distinctness and content accounting are the [finite identities of v1](Yin_L_G0458_v1.md#homogeneous-layer-accounting).
The number of layers does not by itself count positive irreducible factors.

<a id="moving-pair-fourier-floor"></a>
## A uniform Fourier cost for a nontrivial cyclotomic quotient

Set
\[
 I(A,B)=\int_{\mathbb T}\log\max(|A|,|B|)\,d\mu,\qquad
 U=\log|A/B|.
\]
Both input measures are zero, and the boundary logarithms are integrable, so
\[
                              I(A,B)=\tfrac12\int_{\mathbb T}|U|\,d\mu. \tag{Z4}
\]
Signs and relative powers of z do not change this boundary identity; they are still retained in the actual output.

Suppose C and D in (Z1) are different.
Their constant-normalized quotient is analytic and nonvanishing in the open disk and has expansion
\[
                 \frac{D(0)C(z)}{C(0)D(z)}
                     =1+c z^j+O(z^{j+1}),\qquad
                    j\ge1,\quad c\in\mathbb Z\setminus\{0\}. \tag{Z5}
\]
The integrality follows from the constant-unit inverse power series for D.
The analytic logarithm with value zero at zero has the same first coefficient c.
Its boundary real part is U, and hence its j-th complex Fourier coefficient is c/2.
This passage to the boundary can be justified term by term in the finite product of factors with roots on the unit circle: the Fourier coefficients of each logarithm are square summable, and radial limits converge in L2 and therefore in L1.
Consequently
\[
                \int_{\mathbb T}|U|\,d\mu\ge |c|/2,
                 \qquad I(A,B)\ge |c|/4\ge1/4.        \tag{Z6}
\]
Equivalently, one may write the constant-normalized quotient as a finite product of (1-z^j) to integer powers and read its earliest nonzero Fourier coefficient.
No lower bound on a changing input's degree is used.

For nonzero constant-one inputs, (Z5) also makes the first nonzero coefficient of A^N-B^N equal to Nc.
Thus cont(F_N) divides Nc and log cont(F_N)<=log N+log|c|<=log N+log(4I).
This directly prices one possible moving-content escape.
The stronger finite estimates below do not require that restricted constant-one normalization.

<a id="moving-pair-effective-phase"></a>
## Reciprocal roots and the effective phase difference

For the monic cyclotomic parts, C*=C(0)C and D*=D(0)D.
Put
\[
 \epsilon=C(0)/D(0)\in\{1,-1\},\qquad
 \Delta=2(r-s)+\deg C-\deg D,\qquad R=A/B.
\]
The signs eta_A and eta_B cancel in the reversal identity, giving
\[
                         R(1/z)=\epsilon z^{-\Delta}R(z). \tag{Z7}
\]
The relative zero-root powers therefore cannot be discarded when computing Delta.
For example A=z and B=z^2+1 have Delta=0 even though their ordinary degrees differ.

If a positive-measure irreducible rational factor f of F_N were reciprocal, its nonzero nontorsion root beta and its inverse would both be output roots.
The cyclotomic inputs do not vanish at such a root, so R(beta)^N=R(beta^(-1))^N=1.
Equation (Z7) implies
\[
                              \beta^{N\Delta}=\epsilon^N. \tag{Z8}
\]
If Delta is nonzero this forces beta to be a root of unity, a contradiction.
If Delta=0 but epsilon^N=-1 it is an immediate contradiction.

In those branches every positive irreducible factor is nonreciprocal.
A nonmonic primitive factor already costs at least log 2; a monic nonunit does also.
For the remaining monic factors, the accepted [Smyth statement](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number) gives m(f)>=log theta_0, where theta_0>1 solves theta_0^3-theta_0-1=0.
Since log 2>log theta_0,
\[
              m(P_N)\ge r_+(P_N)\log\theta_0
       \quad\hbox{if }\Delta\ne0\hbox{ or }\epsilon^N=-1. \tag{Z9}
\]
This is a factorwise bound, uniform over moving inputs and N.

The remaining branch has Delta=0 and epsilon^N=1.
On the circle, conjugation of R(z) equals R(1/z), so R is real valued when epsilon=1 and purely imaginary when epsilon=-1, away from its finitely many zeros and poles.
Here C and D cannot be equal: equality and Delta=0 would make R constant.
Thus (Z6) applies throughout the remaining branch.

<a id="moving-pair-uniform-primitive-cost"></a>
## Direct discrete cost with the content paid

Choose b dividing N and k=N/b, and use the actual integer factor
\[
 S_{N,b}=\frac{A^N-B^N}{A^b-B^b}
         =\sum_{j=0}^{k-1}A^{b(k-1-j)}B^{bj}.          \tag{Z10}
\]
All choices below have nonzero denominating polynomials because R is nonconstant.
Their constant terms show cont(S_(N,b))<=k.
Indeed if one input has zero constant term, the other has constant plus or minus one and S has constant plus or minus one.
If both constants are plus or minus one, an even b gives |S(0)|=k; for b=1 with odd k the alternating or constant-sign sum has absolute value one or k.
These are all the cases used below.

For real t and odd k,
\[
              \left|\frac{t^k-1}{t-1}\right|
                 \ge\tfrac12\max(1,|t|)^{k-1}.        \tag{Z11}
\]
For t>=0 the sum of nonnegative powers gives the same bound without one half, for any k.
For t<0 and odd k, the left side is (|t|^k+1)/(|t|+1), which gives (Z11) whether |t| is at most or at least one.
The expression at t=1 is interpreted as the geometric sum.

Apply this pointwise to t=R^b and retain the complete factor |B|^(N-b).
The resulting bounds are as follows.

| Circle values of R | Exponent | b | Lower bound for m(S_(N,b)) |
| --- | --- | --- | --- |
| Real | N odd | 1 | (N-1)I-log 2 |
| Real | N even | 2 | (N-2)I |
| Purely imaginary | N congruent to 2 modulo 4 | 2 | (N-2)I-log 2 |
| Purely imaginary | N divisible by 4 | 4 | (N-4)I |

The powers of |B| turn max(1,|R|^b)^(k-1) exactly into max(|A|,|B|)^(N-b).
All logarithmic boundary singularities are integrable.
Thus these are finite, actual-output estimates, with no Riemann-sum error or pair-dependent continuity modulus.

Content multiplicativity and nonnegativity of the other primitive integer factor give
\[
 m(P_N)\ge m(\operatorname{prim}S_{N,b})
          \ge m(S_{N,b})-\log k.
\]
Combining the table with (Z6) proves, for every remaining balanced-phase input and N>=4,
\[
                         m(P_N)\ge
                     \frac{N-4}{4}-\log(2N).          \tag{Z12}
\]
The lower bound tends to infinity uniformly even when the input degrees, coefficients and contents change with N.
Therefore increasing the explicit layer exponent cannot keep the full primitive measure bounded in this branch.
Together with (Z9), the proposed mechanism of bounded full measure and growing positive-factor count cannot be supplied merely by increasing the outer layer exponent.
A bounded exponent still permits unbounded factor count inside one moving layer; that distinct possibility is not excluded by (Z12).

<a id="moving-pair-exact-content-control"></a>
## Exact content and a sharper same-phase comparison

A useful more precise formula holds when A and B are primitive with A(0)=B(0) in {1,-1}.
Write c_N=cont(A^N-B^N) and c_1=cont(A-B).
Then
\[
                     c_N=c_1\prod_{p\mid c_1}p^{v_p(N)}. \tag{Z13}
\]
For completeness, use the coefficient-minimum Gauss valuations and their rational-function extension from [v1](Yin_L_G0458_v1.md#fixed-pair-gauss-content).
If p divides c_N, reduction gives (A/B)^N=1 in F_p(z).
This rational function is constant; the common nonzero constant coefficient forces its value to be one.
Hence p divides c_1.
For odd p, the Gauss-valuation lifting calculation gives v_p(c_N)=v_p(c_1)+v_p(N).
For p=2 dividing c_1, every coefficient of A+B is even and its constant coefficient is plus or minus two, so w_2(A+B)=1.
The even-prime lifting formula from v1 then gives the same equality; for odd N it gives v_2(c_N)=v_2(c_1).
These statements prove (Z13) at every prime, including the absence of other primes.

Suppose in addition that R is real on the circle.
The two input values have a common unit phase and can be written as that phase times real numbers x,y.
For N>=2,
\[
 |x^N-y^N|\ge\max(|x|,|y|)^{N-2}|x^2-y^2|.           \tag{Z14}
\]
For like signs use 1-t^N>=1-t^2 for 0<=t<=1; for unlike signs and odd N use 1+t^N>=1-t^2.
After integration and content removal,
\[
 m(P_N)\ge(N-2)I+m(\operatorname{prim}F_2)+\log(c_2/c_N)
          \ge(N-2)I-\log N.                          \tag{Z15}
\]
Here (Z13) gives c_N/c_2<=N, and for even N it gives the sharper c_N/c_2<=N/2.
This preserves the actual changing content, rather than hiding it in a fixed-pair constant.

<a id="moving-pair-large-content-example"></a>
## Genuine global factor growth with large content, at a growing cost

Fix an odd prime p and j>=1.
Set
\[
 U=(z-1)^{2p-2},\qquad V=\Phi_p(z)^2,\qquad
 q=p^{j-1},\qquad A=U^q,\quad B=V^q.                  \tag{Z16}
\]
These are coprime monic constant-one cyclotomic products of equal degree.
The identity
\[
 (z-1)^2(U-V)=(z-1)^{2p}-(z^p-1)^2
\]
shows that cont(U-V)=p.
Indeed reduction modulo p makes the right side zero, while its coefficients at z and z^2 are -2p and p(2p-1), whose gcd is p.
The common factor (z-1)^2 is monic and has content one.

With M=qN, equations (Z13) and (Z16) give the exact moving contents
\[
 \operatorname{cont}(A-B)=p^j,\qquad
 A^N-B^N=U^M-V^M,\qquad
 \operatorname{cont}(A^N-B^N)=p^{j+v_p(N)}.            \tag{Z17}
\]
Thus the large content is real, rather than an assumed rounding gain.

On the circle,
\[
                       U/V=\left((z-1)^{p-1}/\Phi_p(z)\right)^2
\]
is nonnegative real: the ratio inside the square is a real quotient of reciprocal polynomials of equal degree and constant one.
Every layer Phi_d(U,V) with d dividing M and d>1 consequently has no root on the circle, since no primitive d-th root of unity is a positive real number.
The values at zeros of V are nonzero by coprimality.
Each layer is nonconstant, with degree (2p-2)phi(d) and nonzero leading coefficient Phi_d(1).
Distinct layers are coprime, so
\[
                       r_+(\operatorname{prim}(A^N-B^N))
                                \ge\tau(M)-1.         \tag{Z18}
\]
For instance j tending to infinity with N fixed already makes this count tend to infinity.
These are genuine global positive factors, not just local factors or repeated common cyclotomic factors.

But the first coefficient of log(U/V) is -2p: the coefficients at z in U and V are -(2p-2) and 2.
Thus (Z6) gives I(U,V)>=p/2.
Using (Z15) with exponent M proves the complete price
\[
                  m(\operatorname{prim}(A^N-B^N))
                       \ge (M-2)p/2-\log M
                       \longrightarrow\infty.        \tag{Z19}
\]
At M=1 the displayed lower bound is negative and follows directly from nonnegativity; the divergence is as M tends to infinity with p fixed.
The construction fails even when only the input multiplicity q grows and the displayed outer exponent N stays fixed.
Neither its arbitrarily large content nor its growing count supplies a small-measure construction.

<a id="moving-pair-individual-layer-cost"></a>
## An additional uniform high-order layer estimate

For monic cyclotomic products A,B of the same degree, consider a remaining balanced phase and H_d=Phi_d(A,B).
For d>4 and t real or purely imaginary,
\[
 \log|\Phi_d(t)|\ge\varphi(d)\log^+|t|
                               -\tau(d)\log(2d).      \tag{Z20}
\]
To prove this, write t=xi v with xi in {1,-1,i,-i} and 0<=v<1 and use
\[
                      \Phi_d(\xi v)
                        =\prod_{e\mid d}(1-\xi^e v^e)^{\mu(d/e)}.
\]
When xi^e=1, split 1-v^e=(1-v)(1+v+...+v^(e-1)).
The latter logarithm lies between zero and log e.
The coefficients of log(1-v) sum to zero because Phi_d(xi) is nonzero for d>4.
For xi^e=-1 or plus or minus i, the modulus logarithm lies between zero and log 2.
Summing the absolute bounds proves a bound tau(d)log(2d) on the absolute logarithm for v<1.
Continuity covers v=1, and reciprocity covers v>1, proving (Z20).

Homogeneous evaluation and m(B)=0 then give
\[
                         m(H_d)\ge\varphi(d)I-\tau(d)\log(2d).
\]
Its leading coefficient is Phi_d(1), and the identity d=product_(e|d,e>1) Phi_e(1) shows 1<=Phi_d(1)<=d.
Therefore
\[
              m(\operatorname{prim}H_d)
                 \ge\frac{\varphi(d)}4-\tau(d)\log(2d)-\log d. \tag{Z21}
\]
For all sufficiently large d this is at least phi(d)/8.
One may use the elementary estimates phi(d)>=sqrt(d/2) and tau(d)=O(d^(1/4)); the latter follows by bounding the finitely many small-prime factors separately in the divisor-product formula.
This supplementary bound is for the indicated monic equal-degree inputs.
It does not turn a bound on the number of layers into a bound on their internal irreducible-factor counts.

<a id="moving-pair-low-order-factor-reduction"></a>
## Small factors can occur only in exceptional low-order layers

Let phi=(1+sqrt(5))/2 and delta=(log phi)/2.
Use the original [Sch75 monic-integral corollary](../audits/literature/Sch75/Yin_U001.md#sch75-monic-integral-gap), accepted at its inspected external-statement scope.
For a Kroneckerian field K and a monic polynomial p in O_K[z] with nonzero constant coefficient, if its conjugate reversal is not a scalar multiple of p, the corollary gives
\[
                  \sum_{\sigma:K\hookrightarrow\mathbb C}
                         m(\sigma p)
                       \ge [K:\mathbb Q]\delta.        \tag{Z22}
\]
The sum counts every embedding, and m(sigma p) is the full polynomial measure.
The source's content-ideal contribution is one in this monic integral case.
No fractional-content cancellation or whole-proof audit is used.

Consider an actual primitive irreducible positive factor f of F_N with m(f)<delta.
Since delta<log 2, its leading and constant coefficients have absolute value one; choose the monic sign.
Also delta<log theta_0, so (Z9) forces Delta=0 and epsilon^N=1.
Choose a root beta of f and put zeta=R(beta).
Then zeta is an N-th root of unity and K=Q(zeta) is a Kroneckerian field contained in Q(beta).
Let p be the monic K-minimal polynomial of beta.
Its coefficients are in O_K because beta is an algebraic integer.
The norm N_(K/Q)(p) is monic rational integral and divisible by f, and both have degree [K:Q][Q(beta):K]=deg f.
Thus
\[
                            f=N_{K/\mathbb Q}(p).     \tag{Z23}
\]

If p were self-inversive, beta and 1/overline(beta) would both be roots of p and hence of the same fiber R(z)=zeta.
But (Z7), real coefficients of R and Delta=0 give
\[
                R(1/\overline\beta)
                  =\epsilon\,\overline{R(\beta)}
                  =\epsilon\,\overline\zeta.
\]
Therefore self-inversiveness forces zeta^2=epsilon.
If that equality fails, p meets (Z22), and (Z23) gives m(f)>=[K:Q]delta>=delta, a contradiction.
Consequently every such small positive factor satisfies
\[
                              \zeta^2=\epsilon.       \tag{Z24}
\]

For epsilon=1 the only possibilities are zeta=1 and -1, so f divides A-B or A+B; the latter occurs in F_N only for even N.
For epsilon=-1 the only possibilities are zeta=i and -i, so f divides A^2+B^2 and can occur in F_N only when N is divisible by four.
In particular no factor below delta occurs in the balanced epsilon=-1 branch with N congruent to two modulo four.
These statements include content and all embeddings of the actual algebraic factor.

For a fixed input pair, raising N cannot add any further small-factor types beyond these low-order layers.
It does not increase their multiplicities either: the roots of X^N-1 are simple in characteristic zero, so at a noncyclotomic output root the order of vanishing is the order in A-zeta B, independent of the multiple N of the order of zeta.
For changing input pairs, the exceptional layers themselves change and can still have complicated internal factorizations.

<a id="moving-pair-lehmer-exception-control"></a>
## The retained exception already contains the Lehmer seed

The [same fixed Lehmer polynomial used in L450](Yin_L_G0450_v5.md#moving-map-actual-inputs) has the exact representation
\[
              P_L(z)=(z+1)(z^3-1)(z^6-1)-z^5.         \tag{Z25}
\]
Both inputs have zero measure, are coprime, and have effective phase difference Delta=10-2(5)=0 and epsilon=1.
Thus this is an actual A-B exceptional layer, including the relative zero-root power that must be retained.
The source's Salem property gives one positive real root lambda>1 and m(P_L)=log lambda.
The exact values P_L(1)=-1 and P_L(5/4)=3129421/1048576>0 imply lambda<5/4.
Since (5/4)^2<phi, this gives 0<m(P_L)<delta.
The low-order exception is therefore necessary even for a familiar small-measure input; it is not a claim that every exceptional layer has zero measure or the new uniform gap.
No varying family with smaller measures is produced by this identity alone.

<a id="moving-pair-outcome-and-next-input"></a>
## Outcome and remaining construction

The full primitive cost is uniformly controlled across changing zero-measure input pairs.
Unbalanced effective phases have the factorwise Smyth gap (Z9); balanced phases have the uniform divergent bound (Z12) as N grows.
The explicit large-content example has genuine global factor proliferation but pays its complete increasing cost in (Z19).

More sharply, every positive factor below delta is confined to A-B, A+B or the stated A^2+B^2 exception, with the exact phase and divisibility conditions in (Z24).
All other positive factors have a uniform gap.
Thus a bounded-full-cost sequence with unbounded positive-factor count must place that growth inside the changing exceptional layers; the new outer layers cannot provide it.

The remaining question is to construct an actual small factor or an unbounded positive-factor count inside those exceptional moving polynomials, while preserving their entire primitive cost.
No such construction or universal exclusion has been obtained here.
No numerical scan, native computation or new project Claim assessment is part of this version.
The fixed-pair results, ordinary Chebyshev exclusion and unresolved changing reciprocal-trace comparison remain at their exact v1 scopes.

The construction contributor read the saved arguments (Z1)--(Z24) and checked the signed and zero-root input extension, effective phase, geometric-sum content, individual-layer scope and low-order factor algebra.
The bottleneck contributor separately checked the exact-content formula and the explicit large-content/global-factor example.
The source contributor checked the low-order reduction against the original Sch75 corollary, including its monic specialization, embedding sum and norm-polynomial multiplicity.
The coordinating contributor read the complete resulting account and checked the Lehmer identity and exact rational endpoint value in (Z25).
These are ordinary author checks; the original external proof dependencies were not independently audited and no formal R was created.
