---
author: Yin
---

# Reciprocal three-block cyclotomic delays: integer prefixes and their degree cost

Date: 2026-11-05.
Prepared for Yin by the coordinating agent and the assigned three_block agent during the G0001 exploration.
The coordinator proposed the phase-balanced three-block object, the small-measure integer-prefix estimate, and the four-term and full-degree completion below.
The assigned agent checked those deductions, supplied the exact zero-measure classification and the positive controls, and prepared this account.
These are ordinary author-side checks of a bounded exploration, not an independent review, a new accepted Claim or a whole-goal conclusion.

<a id="scope-and-existing-homes"></a>
## Scope and existing homes

[L133 v1](Yin_L_G0133_v1.md#fixed-seed-limit-and-scope) retains its delay-seed return and fixed-seed limits.
[L133 v2](Yin_L_G0133_v2.md#cyclotomic-boundary-log-gap) excludes arbitrarily chosen distinct cyclotomic blocks in yA-B using the total-measure Smyth bound.
The present variant stays in this cyclotomic delay-block topic but uses reciprocal three-block specializations, for which that nonreciprocal-factor argument does not apply.
Neither earlier version nor its actual review coverage is replaced or extended by this account.

[C224](../claims/Yin_C_G0224_v1.md#statement) treats its specific alternating kernels and their fixed and joint limits.
Its [diagonal proof](../claims/Yin_C_G0224_v1.md#lawton-diagonal-kernels) supplies the pattern reused for the positive control below, but not a classification of the unrestricted cyclotomic quotients here.
The [BM05 source comparison](../audits/literature/BM05/Yin_U001.md#source-quadratic-families) identifies existing reciprocal quadratic subfamilies and the same quadratic Jensen mechanism.
Its [exact finite-cover comparison](../audits/literature/BM05/Yin_U001.md#finite-cover-and-exact-control) identifies the coprime positive control below as a source subfamily, and its [six-term comparison](../audits/literature/BM05/Yin_U001.md#six-term-limit-comparison) identifies that control's fixed positive limit.
The construction and that control are not claimed as new literature results; the inspected source supplies no uniform gap for the unrestricted cyclotomic products here.
The positive Poisson kernel and its Fourier coefficients are already available in [C10 v2](../claims/Yin_C_G0010_v2.md#argument), and the coefficient-space Parseval convention in [C296](../claims/Yin_C_G0296_v1.md#endpoint-row-hardy-closure).
The boundary logarithm passage needed here is justified below rather than inferred from a finite-polynomial square bound.
Lawton is used only at the accepted fixed-Laurent-polynomial, full-measure interface recorded for Theorem14 and Example15 of arXiv:0905.0604v1 in [Den09 U002](../audits/literature/Den09/Yin_U002.md#den09-u002).
Its original proof, including its control at torus zeros, is not newly audited.

<a id="three-block-integral"></a>
## Definition of the phase-balanced object and its exact logarithmic cost

Let A0 and B0 be monic reciprocal products of cyclotomic polynomials with constant coefficient1 and even degrees 2a and 2b.
Multiplicities are unrestricted, and the empty product1 is allowed.
Put

    A(x)=x^(-a) A0(x),       B(x)=x^(-b) B0(x),
    F(x,y)=A(x)(y+y^(-1))-B(x),
    f(z)=B0(z)/A0(z)=sum_(j>=0)c_j z^j.

Thus A and B are real on the unit circle T, while f is analytic and nonzero in the open disk.
The coefficients c_j are integers and c_0=1 because A0 has integer coefficients and constant coefficient1.
The ratio t=B/A is real off a finite set of circle points, and |t|=|f| there.
All circle and torus integrals below use normalized Haar measure, and m denotes total logarithmic Mahler measure.
Define

    g(t)=0                         if |t|<=2,
    g(t)=arcosh(|t|/2)             if |t|>2.

Then the complete two-variable cost is

    epsilon=m_2(F)=integral_T g(B/A).                         (1)

For an x away from the finitely many zeros of A0, factor y^2-t y+1.
Its roots have product1; when |t|<=2 both lie on T, and when |t|>2 the larger root modulus is exp(g(t)).
Consequently its y-circle logarithmic integral is g(t), and that of F is log|A(x)|+g(t).
The latter integrates to (1), since m(A0)=0.

This iterated calculation includes all torus zeros, poles of the quotient and common cyclotomic factors.
For each root lambda, the absolute value of y-lambda is max(1,|lambda|) times a rotated factor |1-r y| or |1-r y^(-1)| with 0<=r<=1.
Each normalized factor has mean logarithm0, positive logarithm at most log2, and hence logarithmic L1 norm at most 2log2.
It follows that the y-integral of |log|y^2-t y+1|| is at most g(t)+4log2.
Moreover g(t)<=log^+|t|<=log^+|B0|+log^-|A0|, which is integrable on T.
The finite logarithmic root singularities of A0 and B0 are integrable, so Fubini applies to the full logarithm of F.
No division at an exceptional point is used.

<a id="integer-prefix-estimate"></a>
## Small measure forces an integral sparse prefix

Pointwise off the exceptional set,

    log|f|<=log2+g(B/A).                                     (2)

Indeed |t|<=2 gives this directly, and otherwise |t|=2cosh(g(t))<=2exp(g(t)).
The boundary function log|f| is a finite signed sum of functions log|1-zeta^(-1)x| with |zeta|=1.
For each such function its positive-Poisson integral is its harmonic value log|1-zeta^(-1)z| inside the disk.
One elementary justification first replaces x by rho x, with rho<1, and uses the absolutely convergent logarithm series and the Poisson Fourier coefficients r^|k|.
As rho increases to1 the circle logarithms converge in L1: their positive parts are bounded by log2, and, near their one singularity, their negative parts are dominated by a constant plus |log|theta||, using |1-rho exp(i theta)|>=sqrt(2)|theta|/pi for rho>=1/2 and |theta|<=pi.
The fixed interior Poisson kernel is bounded, so the L1 limit gives the asserted identity, also for the signed sum.

The Poisson kernel has maximum (1+r)/(1-r), and (1)-(2) therefore give

    |f(r exp(i theta))|<=2exp(epsilon(1+r)/(1-r)),   0<r<1.

Parseval on each interior circle, followed by truncation, yields

    sum_(j=0)^N c_j^2
      <=4 r^(-2N) exp(2epsilon(1+r)/(1-r)).

For an integer N>=1 and r=exp(-c/N), this is

    sum_(j=0)^N c_j^2
      <=4exp(2c+2epsilon coth(c/(2N))).                       (3)

Suppose 0<epsilon<=1/1000 and set N=floor(1/(1000epsilon)) and c=1/20.
Since coth u<=1+1/u for u>0, the exponent on the right of (3) is at most

    1/10+2epsilon+80epsilon N<=0.182<1/5.

The elementary inequality log(5/4)>1/5 gives 4exp(1/5)<5.
The left side of (3) is an integer, so

    sum_(j=0)^floor(1/(1000epsilon)) c_j^2<=4.                (4)

Because c_0=1, this prefix has at most three further nonzero coefficients, each equal to1 or -1.
This is the arithmetic step: a real-valued norm estimate becomes a discrete coefficient restriction.
It does not by itself bound the position of the next nonzero coefficient or the degrees of A0 and B0.

<a id="zero-measure-classification"></a>
## Exact zero-measure classification

Under the stated hypotheses,

    epsilon=0  if and only if
    B0=A0, or B0=A0(1+x^(2h)) for an integer h>=1.           (5)

If epsilon=0, the preceding Poisson estimate gives |f(z)|<=2 in the disk.
Letting r increase to1 in Parseval gives sum_(j>=0)c_j^2<=4.
Since the coefficients are integers, f is a polynomial.
Thus A0 divides B0, and f is monic reciprocal with constant coefficient1, even degree, and only cyclotomic roots.

Its coefficient square energy cannot equal4.
That equality together with |f|<=2 would force |f|^2=4 almost everywhere on T.
A nonconstant polynomial with nonzero constant and leading coefficients has a nonzero Fourier coefficient at its extreme positive lag, so it cannot have constant modulus.
The constant polynomial here is1 and has energy1.
If the energy is3, monicity and reciprocity force f=1+sigma x^h+x^(2h), where sigma is1 or -1 and h>=1.
At x^h=sigma its absolute value is3, contradicting |f|<=2.
Energy2 gives f=1+x^(2h), and energy1 gives f=1.
This proves the necessity in (5); a minus binomial is excluded by monicity and constant coefficient1.

Conversely, the first case has F=A y^(-1)(y^2-y+1), and the second has

    F=A y^(-1)(y-x^h)(y-x^(-h)).

Both have total logarithmic measure0, which proves sufficiency including common cyclotomic factors.

<a id="first-deviation-degree-cost"></a>
## First integral deviation and the complete degree price

When it exists, define the first energy deviation by

    J=min{j>=0: sum_(k=0)^j c_k^2>=5}.

Then J>=1 and

    epsilon>1/(1000J).                                      (6)

For epsilon>1/1000 this is immediate.
For 0<epsilon<=1/1000, (4) implies floor(1/(1000epsilon))<J, and hence 1/(1000epsilon)<J.
The index J need not exist for every positive-measure polynomial quotient; the following short-polynomial bounds supply the missing cases.

If the full coefficient square energy of a polynomial f is3, its already derived form is 1+sigma x^h+x^(2h).
On a set of normalized measure1/6 where sigma cos(h theta)>=sqrt(3)/2, its modulus is at least1+sqrt(3)>5/2.
Thus g(B/A)>=log2 on that set, and epsilon>=log2/6.
Energies1 and2 are exactly the zero-measure cases in (5).

If the full energy is4, all four nonzero coefficients have absolute value1, because c_0=1 and f is monic.
Put X=|f|^2-4 on T.
Then E X=0 and -4<=X<=12, while Parseval for |f|^2 gives E X^2>=2 because its two extreme Fourier coefficients have modulus1.
Writing X_+=max(X,0) and X_-=max(-X,0), one has E X_+=E X_- and

    2<=E X^2<=12 E X_+ +4 E X_-=16 E X_+.

On X>0,

    g(B/A)>=log(|f|/2)
           =(1/2)log(1+X/4)>=X/32.

The last inequality follows from log(1+u)>=u/(1+u) and 0<u<=3.
Consequently

    epsilon>=1/256                                           (7)

for this four-term case.

Write D=deg A0 and E=deg B0, retaining the actual input degrees rather than silently cancelling common factors.
For a nonpolynomial quotient, D>=1 and the coefficients of A0 f=B0 obey the homogeneous order-D recurrence at every index greater than E.
There cannot be D consecutive zero coefficients wholly after index E, because this recurrence would force all subsequent coefficients to vanish and make f a polynomial.
Each of the four disjoint length-D blocks between E+1 and E+4D therefore contains a nonzero integer coefficient.
Together with c_0=1 they give J<=E+4D.

For a polynomial quotient, its degree is E-D.
If 0<epsilon<=1/1000, (5), (7) and the three-term bound exclude full energy at most4, so J exists and J<=E-D<=E+4D.
This also covers D=0, where f=B0.
If epsilon>1/1000, the claimed degree inequality follows directly whenever D+E>0.
Thus every positive-measure input in this family satisfies

    epsilon>1/(1000(E+4D)).                                 (8)

The case D=E=0 is A0=B0=1 and has epsilon=0.
Estimate (8) is a complete degree-dependent cost for this family, not a uniform positive constant.
The step from (4) to (8) is precisely where the actual input degrees enter.

<a id="positive-controls"></a>
## Positive controls with delayed coefficient deviations

First take A0=1+x^(2k) and B0=1, with k>=1.
Then f=1/(1+x^(2k)) and J=8k, while epsilon is independent of k by the measure-preserving covering x->x^k.
It is positive: in the k=1 integral, the event |cos theta|<=1/8 has normalized measure at least1/(4pi), and on it |B/A|>=4.
Hence epsilon>=arcosh(2)/(4pi).
This example alone is only an exponent dilation.

To remove an increasing common x dilation, take

    A0_n=1+x^(2n+2),       B0_n=1+x^(2n),       n>=1,
    F_n=(x^(n+1)+x^(-n-1))(y+y^(-1))-(x^n+x^(-n)).

The two blocks are coprime: a common root would satisfy x^(2n)=x^(2n+2)=-1, forcing x^2=1 and then x^(2n)=1.
The x frequencies n and n+1 are coprime, so no growing common power substitution in x explains this sequence.
This statement does not assert primitive support in every lattice sense: a fixed parity restriction in the two-variable support remains, and neither irreducibility nor a Task-specific all-power property is inferred.
The first five nonzero coefficients of f_n=B0_n/A0_n occur at

    0, 2n, 2n+2, 4n+2, 4n+4,

with signs +,+,-,-,+, respectively.
Thus J_n=4n+4.
Every epsilon_n=m_2(F_n) is positive by (5), since f_n is not a polynomial.

In fact these measures tend to a fixed positive value.
Put

    G(u,v,y)=(v+v^(-1))(y+y^(-1))-(u+u^(-1)).

For each fixed n, the accepted two-variable Lawton theorem permits an integer H_n>n^3 such that

    |m(F_n(t,t^(H_n)))-m_2(F_n)|<1/n.

Here F_n(t,t^(H_n))=G(t^n,t^(n+1),t^(H_n)).
The relation parameter of (n,n+1,H_n) tends to infinity: for n>=2, a relation of sup norm less than n/2 cannot have a nonzero third coefficient, since its H_n term exceeds the possible sum of the other two terms.
With third coefficient0, coprimality of n and n+1 forces every nonzero relation to have sup norm at least n+1.
The accepted three-variable fixed-polynomial Lawton theorem therefore gives

    epsilon_n -> epsilon_*:=m_3(G).

The same Jensen and logarithmic-integrability argument as for (1), now integrating in u and v, gives

    epsilon_*=integral_(T^2) g((u+u^(-1))/(v+v^(-1))).

On the independent events |cos(arg v)|<=1/8 and |cos(arg u)|>=1/2, of measures at least1/(4pi) and 2/3, respectively, the ratio has absolute value at least4.
Consequently epsilon_*>=arcosh(2)/(6pi)>0.
This is a fixed-polynomial diagonal argument with separately selected H_n, not an effective uniform convergence rate for varying input polynomials.
It shows that arbitrarily late integral coefficient deviations, even without growing common x dilation, are compatible with a measure bounded away from zero.
It supplies neither a sequence epsilon_n->0 nor a proof that every positive input has a uniform gap.

<a id="original-polynomial-return"></a>
## Exact return to integral reciprocal polynomials and the unresolved step

For a fixed pair A0,B0 and an integer N>max(0,b-a), clear the Laurent monomial in F(t,t^N) to obtain

    P_N(t)=t^(N+a)F(t,t^N)
          =t^(2N)A0(t)+A0(t)-t^(N+a-b)B0(t).

This is a monic reciprocal integer polynomial with constant coefficient1 and actual degree2(N+a).
Indeed the middle shifted block begins at positive degree and ends below2(N+a).
Reflection about degree N+a exchanges the two A0 blocks and preserves the shifted B0 block, proving reciprocity.
Monomial clearing leaves Mahler measure unchanged.
For this fixed pair, the relation parameter of (1,N) is N, so the accepted Lawton theorem gives m(P_N)->epsilon as N tends to infinity.

If a sequence of pairs in the stated family actually satisfied epsilon_j>0 and epsilon_j->0, one could choose an integer N_j separately for each pair, above its actual threshold, with

    |m(P_(N_j))-epsilon_j|<epsilon_j/2.

Then 0<m(P_(N_j))<3epsilon_j/2 would tend to zero for genuine integral reciprocal unit polynomials of degrees2(N_j+a_j).
Factoring such a polynomial over Z would provide a positive-measure monic irreducible unit factor with total logarithmic measure at most that of the polynomial.
No uniform lower bound on each noncyclotomic factor or Task-specific all-power condition follows merely from this construction.
The choice of N_j can depend on the complete pair and epsilon_j, and no uniform effective Lawton cutoff or bound on the resulting factor degree is supplied.

The present exploration proves the integer prefix restriction, the exact zero set and the degree-dependent bound (8), with the controls above.
It supplies neither the positive vanishing-measure sequence required for this return nor a uniform lower bound ruling one out.
A uniform strategy would need a further mechanism that controls the full quotient beyond the degree-growing first-deviation window, or an alternative arithmetic cost that remains positive independently of D and E.
The three-block object therefore remains a bounded exploratory test of integer constraints, not a new adopted strategy resolving G0001.
