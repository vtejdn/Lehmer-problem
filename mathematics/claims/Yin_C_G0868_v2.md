---
author: Yin
---

# Analytic damping and uniform gaps for reciprocal three-block measures

This project deduction extends the pole-free cyclotomic-input result of [C868 v1](Yin_C_G0868_v1.md#statement).
It permits arbitrary monic reciprocal integer blocks of even degree and constant coefficient1, while retaining the actual measure of common content.
This version's mathematical status and evidence are owned by the selected assessment below.
The earlier v1 review remains at its exact scope; the new version has its own whole-proof finding.

## Inputs

[The v1 statement](Yin_C_G0868_v1.md#statement) retains AM1-AM2 and CG1-CG5 at their exact original hypotheses, including the cyclotomic restriction on both blocks in CG1-CG5.
[Its selected assessment](Yin_C_G0868_v1.md#decision-whole-independent-review-2026-11-05) and the adopted review remain unchanged in that fixed predecessor.
The present germ-multiplier assertion extends the finite argument behind [v1 AM2](Yin_C_G0868_v1.md#first-energy-crossing), rather than applying a holomorphic-disk hypothesis to a quotient that may have poles.
The [v1 radial logarithm proof](Yin_C_G0868_v1.md#boundary-log-poisson) is used only for factors with their zero on the unit circle; the new inside-root and denominator-reflection checks are given explicitly below.
The [v1 short-polynomial calculations](Yin_C_G0868_v1.md#short-polynomial-completion) are retained at their actual coefficient and symmetry scope and are reproduced where needed for the new cost.

## Statement

Let

    gamma=(sqrt(5)-2)^2/50.

All torus integrals use normalized Haar measure, and m denotes total logarithmic Mahler measure without division by degree.
Write P[g] for the disk Poisson integral

    P[g](z)=integral_T (1-|z|^2)/|zeta-z|^2 g(zeta) dmu(zeta).

### Integer germs with a bounded analytic multiplier

Let f be an analytic germ at0 with Taylor series in Z[[z]] and f(0)=1.
Suppose q and u are holomorphic on the entire open unit disk and satisfy

    |q(z)|<=1,       |u(z)|<=2,
    q(0)=exp(-tau),       tau>=0,
    u=fq on a neighborhood of0.                            (GM1)

If a finite Taylor prefix of f has coefficient square energy at least5, then tau>=gamma.
Equivalently,

    tau<gamma  implies that f is a polynomial germ
    with integer coefficients and total square energy<=4. (GM2)

No analytic continuation of f itself to the entire disk and no boundary H2 assumption on f are required.
The conclusions concern the exact germ and all its Taylor coefficients, not a truncated replacement of the input.

### Arbitrary reciprocal integer blocks

Let A0,B0 be monic reciprocal integer polynomials with constant coefficient1 and even degrees2a,2b, allowing the constant polynomial1.
Set

    A(x)=x^(-a)A0(x),       B(x)=x^(-b)B0(x),
    F(x,y)=A(x)(y+y^(-1))-B(x),       f=B0/A0,
    phi(t)=0                         for real |t|<=2,
    phi(t)=arcosh(|t|/2)             for real |t|>2.

The logarithm of F is integrable on T^2 and

    epsilon=integral_T phi(B/A)>=0,
    tau:=m_2(F)=m(A0)+epsilon.                              (RG1)

The finitely many undefined values of B/A on T are ignored in the integral.
Then

    if f is neither1 nor1+x^(2h) for an integer h>=1,
    tau>=gamma.                                            (RG2)

In the two exceptional cases,

    B0=A0, or B0=A0(1+x^(2h)),
    tau=m(A0).                                              (RG3)

Thus tau<gamma forces one of RG3's exact polynomial identities and leaves precisely the one-variable measure m(A0).
For arbitrary blocks the exact zero condition is RG3 together with m(A0)=0.

Two useful subdomains consequently have a full positive gap:

    If A0 is a cyclotomic product and B0 is arbitrary
    under the stated integer reciprocal hypotheses,
    then tau=0 or tau>=gamma,
    with tau=0 exactly for RG3.                            (RG4)

    If gcd(A0,B0)=1, then tau=0 or tau>=gamma,
    with tau=0 exactly for A0=1 and
    B0=1 or B0=1+x^(2h), h>=1.                             (RG5)

The gcd in RG5 is the monic polynomial gcd over Q, equivalently over Z for these monic integer inputs.
For coprime inputs with A0 nonconstant, tau is always at least gamma.

For every fixed pair in this full domain and every integer N>max(0,b-a),

    P_N(t)=t^(2N)A0(t)+A0(t)-t^(N+a-b)B0(t)

is a monic reciprocal integer polynomial with constant coefficient1 and actual degree2(N+a), and

    m(P_N)->tau       as N->infinity.                       (RG6)

For a fixed pair outside RG3, sufficiently large N have m(P_N)>=gamma/2.
No pair-uniform effective delay bound, positive bound for all varying-pair finite specializations, or arbitrary-input Lehmer gap is asserted.
The exceptional pairs A0=B0 retain every one-variable measure m(A0), so a full positive gap for all pairs is not a conclusion.

<a id="source-and-scope"></a>
## Sources, scope and contribution

The original analytic damping, integer first-crossing estimate, three-block construction and source comparison are retained in [C868 v1](Yin_C_G0868_v1.md#source-and-scope).
In particular, its BM05 comparison concerns the established reciprocal quadratic Jensen mechanism and actual inspected subfamilies, not a literature-priority claim for the present conclusion.
The normalized finite Blaschke product and coefficient-space norm method also occur in [C296](Yin_C_G0296_v1.md#endpoint-row-hardy-closure), there for the different endpoint relation-space problem.
Here their exact pole-cancellation and constant-term costs are checked directly.

The general Jensen expression with the leading-coefficient term m(A0) is the same established quadratic calculation, and is proved below with full integrability.
Only RG6 uses the accepted full fixed-Laurent-polynomial Lawton theorem from Theorem14 and Example15 of arXiv:0905.0604v1, at the recorded scope in [Den09 U002](../audits/literature/Den09/Yin_U002.md#den09-u002).
Its original proof, including torus-zero control, is not newly audited.
No external boundary factorization theorem or an almost-everywhere boundary maximum principle is used for the new uniform estimate.

The coordinating agent proposed first allowing an arbitrary reciprocal numerator and then canceling a general denominator's inside-disk poles with its normalized Blaschke product.
The assigned three_block agent checked the root-reflection inequality and multiplier normalization and extracted the precise structural conclusion RG2-RG3.
The finite first-crossing mechanism itself remains the earlier joint contribution identified in v1.
The varying-delay cyclotomic control below was supplied by the coordinating agent.
These are author-side development contributions and checks, not independent review of this new version.

<a id="argument"></a>
## Complete argument

<a id="germ-first-crossing"></a>
### 1. Finite projection for an integer germ

For a disk-holomorphic function v(z)=sum v_j z^j, let ||v||_H2^2=sum |v_j|^2, allowing infinity.
Integrating its Taylor series on circles of radius r<1 and letting r increase to1 gives from GM1

    ||q||_H2<=1,       ||u||_H2<=2,
    ||1-q||_H2^2
      =1+||q||_H2^2-2exp(-tau)
      <=2(1-exp(-tau))<=2tau.                              (1)

The constant term is real and positive, as required for this last identity.
These estimates concern q and u, which are holomorphic and bounded on the whole disk.

If a Taylor prefix of f reaches square energy5, take the first such index N.
Write f(z)=sum_(j>=0)c_j z^j near0, with c_j in Z and c_0=1.
Let

    s=sum_(j<N)c_j^2,       c=|c_N|,       P=sum_(j=0)^N c_j z^j.

Then 1<=s<=4, c>=1 and s+c^2>=5.
Every earlier nonzero coefficient has absolute value1, since c_0=1 and an earlier coefficient of absolute value at least2 would already have reached5.
Thus

    ||P||_H2=sqrt(s+c^2),       sum_(j=0)^N |c_j|=s+c.

Writing S_N for coefficient truncation through degree N, the germ identity u=fq gives exactly

    S_Nu=S_N(Pq),
    P-S_Nu=S_N(P(1-q)).                                    (2)

No continuation or norm of the full f tail appears here.
The finite polynomial P multiplies H2 boundedly with norm at most its coefficient absolute sum s+c, by the radial-circle bound |P(rzeta)|<=s+c.
The coefficient projection S_N is contractive on H2.
Applying these two facts only to u and P(1-q), both in H2, proves

    sqrt(s+c^2)<=2+(s+c)sqrt(2tau).                         (3)

For completeness, the unchanged integer minimization from v1 is

    (sqrt(s+c^2)-2)/(s+c)>=(sqrt(5)-2)/5.                   (4)

For c=1 the hypotheses force s=4 and equality holds.
For c=2,s=1 the ratio is (sqrt(5)-2)/3; for c=2,2<=s<=4 it is at least (sqrt(6)-2)/6>1/15.
For c>=3 it is at least (c-2)/(c+4)>=1/7.
Since (sqrt(5)-2)/5<1/20, these cases prove (4).
Equations (3)-(4) give tau>=gamma.

If no prefix reaches5, the integer Taylor series has at most four nonzero unit coefficients in total square energy.
It is therefore a finite polynomial germ.
This proves GM2, including the possibility that the originally given germ had a smaller disk of convergence.

<a id="general-quadratic-cost"></a>
### 2. Full Jensen cost for arbitrary blocks

Reciprocity and real coefficients make A and B real on T.
For x away from the finitely many zeros of A0 on T, put t=B(x)/A(x).
Then |t|=|f(x)| and

    F(x,y)=A(x)y^(-1)(y^2-t y+1).

As in the complete [v1 quadratic calculation](Yin_C_G0868_v1.md#quadratic-cost-integrability), the quadratic roots have product1 and their y-circle logarithmic mean is phi(t).
The absolute logarithmic integral of the quadratic is at most phi(t)+4log2, since each normalized linear factor has logarithmic L1 norm at most2log2.
This calculation imposes no condition on the locations of the roots of B0 or A0 beyond avoiding the exceptional boundary fiber in the division.

The controlling inequality

    phi(t)<=log^+|t|<=log^+|B0(x)|+log^-|A0(x)|

still has an integrable right side for arbitrary polynomial blocks.
Roots away from T cause no boundary singularity, and the finite logarithmic singularities on T are integrable.
Together with integrability of log|A|, this proves absolute integrability of log|F| and justifies Fubini even with common roots and multiplicities.
The result is now

    m_2(F)=m(A0)+integral_T phi(B/A),

rather than dropping the first term.
This proves RG1.
Both terms are nonnegative: the integral is nonnegative by definition and a monic polynomial has m(A0)=sum log^+|alpha|>=0.

<a id="root-reflection-poisson"></a>
### 3. Rootwise Poisson comparison, including numerator zeros

Because A0(0)=B0(0)=1, all their roots are nonzero and their constant-normalized factorizations are products of 1-z/alpha.
The quotient f has an integer Taylor series with constant coefficient1 on some neighborhood of0, by coefficient recursion in A0 f=B0.
It need not be holomorphic throughout the unit disk.

For a root beta of B0 with |beta|<1, the boundary identity is

    |1-zeta/beta|=|beta|^(-1)|1-conj(beta)zeta|,
    |zeta|=1.

Consequently the Poisson extension of its boundary logarithm is

    -log|beta|+log|1-conj(beta)z|.

For |z|<1,

    |1-conj(beta)z|^2-|z-beta|^2
      =(1-|beta|^2)(1-|z|^2)>0.

It follows that

    log|1-z/beta|
      <=P[log|1-zeta/beta|](z),                            (5)

including the value -infinity at z=beta.
For |beta|>1 the same Poisson relation is an equality because the factor is zero-free on a neighborhood of the closed disk.
For |beta|=1 the equality follows from the radial L1 calculation retained in [v1](Yin_C_G0868_v1.md#boundary-log-poisson).
Adding the finitely many factors gives

    log|B0(z)|<=P[log|B0||_T](z).                          (6)

Thus inside-disk numerator zeros change the old harmonic equality only in the direction needed for a majorant.

<a id="pole-canceling-multiplier"></a>
### 4. Denominator reflection and its exact measure price

For each root alpha of A0 with |alpha|<1, counted with multiplicity, put

    I_alpha(z)=|alpha|(1-z/alpha)/(1-conj(alpha)z),
    I_A(z)=product_(|alpha|<1) I_alpha(z).

Each factor has modulus1 on T and modulus at most1 in the disk, as follows from the same squared-modulus identity used in (5).
It is analytic in a neighborhood of the closed disk and has its zero at alpha.
The normalization gives I_alpha(0)=|alpha|, so I_A(0)>0.

Define the polynomial

    A_out(z)
      =product_(|alpha|<1) [(1-conj(alpha)z)/|alpha|]
         product_(|alpha|>=1) (1-z/alpha).

Then A0=I_A A_out as rational functions.
The polynomial A_out has no zero in the open disk, retains any unit-circle roots, and has |A_out|=|A0| on T.
In particular the meromorphic quotient f I_A extends holomorphically throughout the disk as

    f I_A=B0/A_out.                                        (7)

The constant coefficient and monicity of A0 give product_alpha |alpha|=1.
Therefore

    I_A(0)=product_(|alpha|<1)|alpha|
          =exp(-m(A0)),
    A_out(0)=exp(m(A0)).                                   (8)

Every factor of A_out is zero-free in the disk with its only possible boundary zeros handled by v1's radial L1 argument.
Its boundary logarithm therefore has exact Poisson extension log|A_out(z)|.
Combining this with (6)-(7) yields

    log|f(z)I_A(z)|
      <=P[log|B0|-log|A0|](z).                            (9)

The left side refers to the holomorphic extension in (7), so it remains meaningful at canceled poles.
This is an interior inequality proved factor by factor, not an inference of an interior bound solely from an almost-everywhere boundary bound.

Let g=phi(B/A) on T, so g>=0 and integral g=epsilon by RG1.
On the complement of the finite exceptional set,

    log|f|<=log2+g,

because |f|=|B/A| and |B/A|<=2exp(phi(B/A)).
Define

    H_g(z)=integral_T (zeta+z)/(zeta-z) g(zeta) dmu(zeta),
    q(z)=I_A(z)exp(-H_g(z)),
    u(z)=(B0(z)/A_out(z))exp(-H_g(z)).

The integral defines an analytic function with Re H_g=P[g]>=0 and H_g(0)=epsilon.
Thus q and u are holomorphic throughout the disk.
Equation (9) proves |u|<=2 there, while |I_A|<=1 proves |q|<=1.
Moreover, (8) and RG1 give

    q(0)=exp(-m(A0)-epsilon)=exp(-tau),
    u=fq near0.                                           (10)

This verifies every hypothesis of GM1, including the precise charge for all inside-disk denominator roots and all their multiplicities.

<a id="structural-completion"></a>
### 5. Completion and the exact exceptional content

If tau<gamma, GM2 and (10) make f a polynomial germ of square energy at most4.
Multiplication by A0 shows that A0 f=B0 is a polynomial identity, since it holds near0.
Consequently f is a monic reciprocal integer polynomial of constant coefficient1 and even degree.
Reciprocity follows by reversing that identity and canceling A0.
No claim that its roots are cyclotomic is needed for the next step.

Energy1 gives f=1, and energy2 gives f=1+x^(2h) for an integer h>=1.
At energy3, monicity and reciprocity force

    f=1+sigma x^h+x^(2h),       sigma in {1,-1}, h>=1.

On the set sigma cos(h theta)>=sqrt(3)/2, of normalized measure1/6, one has |f|>=1+sqrt(3)>5/2.
Since arcosh(5/4)=log2,

    epsilon=integral_T phi(B/A)>=log2/6.                    (11)

At energy4 all four nonzero coefficients have absolute value1.
Put X=|f|^2-4, X_+=max(X,0) and X_-=max(-X,0).
Then E X=0, -4<=X<=12 and E X^2>=2, the last inequality coming from the two extreme nonconstant Fourier coefficients of |f|^2.
Hence E X_+=E X_- and

    2<=E X^2<=12 E X_++4 E X_-=16 E X_+.

On X>0,

    phi(B/A)>=log(|f|/2)
             =(1/2)log(1+X/4)>=X/32,

so

    epsilon>=1/256.                                        (12)

These are the v1 short-polynomial estimates applied to epsilon, not an identification of epsilon with the new total cost tau.
Since tau=m(A0)+epsilon>=epsilon and both bounds (11)-(12) exceed gamma, neither energy3 nor energy4 is possible when tau<gamma.
Thus only RG3's two identities remain, proving RG2.

If f=1 then B=A and F=A y^(-1)(y^2-y+1).
If f=1+x^(2h), then B=A(x^h+x^(-h)) and

    F=A y^(-1)(y-x^h)(y-x^(-h)).

In both cases phi(B/A)=0 almost everywhere and RG1 gives tau=m(A0).
This proves RG3 and the stated general zero condition.

If A0 is cyclotomic, m(A0)=0, so RG2-RG3 give RG4 even when B0 is not assumed cyclotomic.
If gcd(A0,B0)=1, either identity in RG3 forces A0=1.
The corresponding B0 are exactly1 and1+x^(2h), and both have zero cost.
All other coprime pairs satisfy RG2, proving RG5 without a separate gcd-decomposition theorem.

<a id="fixed-pair-and-original-target"></a>
### 6. Fixed-pair specialization and the original-target boundary

The algebraic return is unchanged for arbitrary blocks.
For N>max(0,b-a),

    t^(N+a)F(t,t^N)
      =t^(2N)A0(t)+A0(t)-t^(N+a-b)B0(t)=P_N(t).

The middle term begins at positive degree and ends below2(N+a).
Reflection about degree N+a exchanges the two A0 blocks and preserves the shifted B0 block.
Thus P_N is monic reciprocal, integral, of constant coefficient1 and actual degree2(N+a).
No cyclotomic hypothesis enters this degree calculation.

For the fixed Laurent polynomial F, the nonzero integer relations on (1,N) have least sup norm N.
The accepted full Lawton theorem gives m(P_N)->m_2(F)=tau, proving RG6.
The proof supplies no cutoff uniform over varying A0,B0.

There is an explicit varying-input obstruction to dropping that qualification.
For h>=1 take

    A0=1,       B0=1-x^h+x^(2h),       N=2h.

These are admissible inputs, and epsilon>=log2/6 by (11), so their two-variable costs are bounded away from zero.
Nevertheless

    P_N=x^(4h)-x^(3h)+x^(2h)-x^h+1=Phi_10(x^h)

is a cyclotomic product and has measure0.
Here N tends to infinity with h and satisfies N>b-a=h.
For each fixed h the separate limit N->infinity still satisfies RG6.
This is a family of zero-measure finite specializations, not a positive sequence tending to zero.

Finally, let P be any monic reciprocal integer polynomial of even degree and constant coefficient1, and set A0=B0=P.
Then

    F=x^(-a)P(x)(y+y^(-1)-1),
    m_2(F)=m(P).

Thus arbitrary common content retains the original one-variable reciprocal unit problem exactly.
In RG3's first case, P_N=A0(t)(t^(2N)-t^N+1); in its second case, P_N=A0(t)(t^(N-h)-1)(t^(N+h)-1), with N>h.
Those factors outside A0 are cyclotomic, so the exceptional finite specializations also retain m(A0) exactly.
The structural theorem separates this surviving content from the uniform gap of the nonexceptional ratios.
It does not prove a positive gap for arbitrary common content, an irreducible-factor or all-power conclusion, or the unrestricted G0001 contract.

## Assessment history

### Decision whole-general-block-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T18:42 |
| status | proved |
| reason | Adopt the complete integer-germ multiplier assertion and arbitrary reciprocal-block structural theorem after the independent whole-proof finding R1091 v2. Every nonexceptional ratio pays at least (sqrt(5)-2)^2/50; coprime inputs and cyclotomic-denominator inputs have a full positive gap. The two exceptional ratios retain exactly m(A0), including the unrestricted one-variable difficulty. No uniform varying-pair delay cutoff, arbitrary original-input reduction or G0001 completion is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | GM1-GM2 and RG1-RG6, precise exceptional identities, both full-gap subdomains, total-measure normalization and all common-content and specialization limits. |
| argument | [Complete proof](#argument) | All six sections, including the local germ identity, complete quadratic integral, numerator inequality, denominator reflection, exact multiplier price and original-target boundary. |
| dependency | [V1 quadratic calculation](Yin_C_G0868_v1.md#quadratic-cost-integrability) | Normalized linear-factor absolute-logarithm bounds and reciprocal quadratic Jensen calculation only, without dropping m(A0) for the new general denominator. |
| dependency | [V1 boundary-root calculation](Yin_C_G0868_v1.md#boundary-log-poisson) | Radial L1 convergence and exact Poisson extension for unit-circle root factors; inside-root inequalities and pole cancellation are proved in this version. |
| dependency | [Lawton statement](../audits/literature/Den09/Yin_U002.md#den09-u002) | The accepted arXiv:0905.0604v1 Theorem14/Example15 fixed-Laurent-polynomial interface for RG6, including torus zeros; no new original-proof audit. |
| review | [Independent general-blocks whole-proof finding](../audits/reviews/Yin_R_G1091_v2.md#general-blocks-whole-proof-finding) | Entire exact statement and argument, inherited calculations at their checked scopes, every new interface and original-target limitation; no substantive repair supplied by the reviewer. |

## Current assessment

[Selected decision](#decision-whole-general-block-review-2026-11-05)
