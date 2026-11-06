---
author: Yin
---
# Binary auxiliary supply and the remaining low-energy controls

Human author Yin.
This continuing G0001 inquiry is developed by the arithmetic agent as a proof contributor, not an independent reviewer.
The supplied binary energy-four phase problem is now settled by [C864 v2](../claims/Yin_C_G0864_v2.md#decision-whole-independent-review-2026-11-04), using a logarithmic-margin or full-period dichotomy at the original degree cost.
The current question is automatic auxiliary supply on genuine near-one inputs, with the retained controls also informing other denominator or coefficient-budget choices.
[C849](../claims/Yin_C_G0849_v1.md#fixed-bivariate-template-specialization-class) already handles fixed templates of negative normalized Haar mean at every specialization ratio, and must be reused before claiming new coverage.
[C141](../claims/Yin_C_G0141_v1.md#statement) already excludes automatic fixed-prime sparse-auxiliary supply for certain inputs far from one; those inputs do not settle near-zero total Mahler coverage.
The fixed and varying-conductor precision ceilings [C839](../claims/Yin_C_G0839_v1.md#fixed-norm-and-order-denominator) and [C840](../claims/Yin_C_G0840_v1.md#varying-conductor-unit-resultant-family) do not suggest another precision iteration in those families.
The continuing inquiries and numerical diagnostics here remain author work; fixed results and their assessments are owned by the exact linked Claims.
The [binary reflection reduction](#binary-reflection-reduction) preserves the original auxiliary's congruence, field and span.
The adopted [C862](../claims/Yin_C_G0862_v1.md#decision-whole-independent-review-2026-11-04) supplies the low-pair branch, while [C863 v4](../claims/Yin_C_G0863_v4.md#decision-whole-independent-review-2026-11-04) supplies the exact finite circle reduction used by C864 v2.
The residual pure-circle sign question remains open, but is no longer required for the supplied binary arithmetic class.

## Supplied-class scope and a necessary distinction

Fix the denominator q=2 and an integer seed H with H(0) nonzero and coefficient energy at most4, excluding the constant seeds +/-2.
For a positive integer n and k=deg H retain the actual reversal H*(x)=x^k H(x^(-1)) and V=x^n H+H*.
The adopted theorem allows both reversal signs, changes of coefficient lift modulo2 and a full binary period, while bounding the complete resulting exponent by a fixed multiple of n+k.
The full arithmetic input is an original nontorsion integer unit alpha for which V(alpha)/2 is integral; a formal phase family alone does not supply such inputs near total Mahler measure zero.

The unconditional mean bound fails already for H=1+x+x^2-x^3 and n=1.
Here V=-x^4+2x^3+2x^2+2x-1 and -V=x^2((x+x^(-1))^2-2(x+x^(-1))-4).
The larger trace root is 1+sqrt(5)>5/2, so its expanding reciprocal root exceeds2 and M(V)>2.
The other trace root lies in(-2,2), so this is the complete positive Mahler contribution.
This control has V modulo2 equal to x^4+1 and is already in a bounded-period gap class; it does not disprove the combined dichotomy.

<a id="trace-one-resonant-family"></a>
## A four-term family with a long-order binary factor

Let N=2^r with r>=2, and choose epsilon, eta, delta in{1,-1}.
Set

    H_N=1+epsilon*x^(N-1)+eta*x^N+delta*x^(3N-2),
    V_N=x^2 H_N+H_N*,       deg V_N=3N.

The seed has exactly four distinct unit coefficients, constant1 and energy4.
The exact eight-summand formula is

    V_N=delta*x^(3N)+x^(3N-2)
        +epsilon*(x^(N+1)+x^(2N-1))
        +eta*(x^(N+2)+x^(2N-2))+x^2+delta.

At N=4 the two eta summands coincide and must be collected; the remaining N>=8 cases have eight distinct exponents.

In characteristic2 every sign has the same reduction, and direct multiplication gives

    V_N mod2=(x+1)(x^(N-1)+1)
               *(x^N+x+1)*(x^N+x^(N-1)+1).

The polynomial x^N+x+1 is the relative-trace-one polynomial in F_(N^2).
If it has a root beta of multiplicative order N^2-1, then every product of binomials x^(a_j)-1 divisible by V_N modulo2 must contain an exponent a_j divisible by N^2-1.
Indeed beta must annul one factor in that product, so beta^(a_j)=1.
Consequently the total binomial degree is at least N^2-1, whereas deg V_N=3N.
This concerns a cover of the full phase reduction, not every possible factor of an unrelated original minimal polynomial.

The primitive trace-one input is supported by CK21, Cohen--Kapetanakis, arXiv:2108.08066v1, Theorem1.1 on printed p.1, directly read at https://arxiv.org/pdf/2108.08066 and retained in the [same edition](../literature/pdf/CK21.pdf).
Its q=N, extension degree2 and prescribed trace1 satisfy neither listed exception.
Only that primary statement and its application were inspected; no original proof audit or primitive-element enumeration is claimed.
The authors attribute the primitive theorem to Cohen's 1990 work and explain that their amended 2-primitive argument is a different issue.

<a id="resonant-cubic-mean-test"></a>
## The actual unresolved Haar discriminator

Writing z=x and u=x^N gives the fixed Laurent template

    F_(epsilon,eta,delta)(z,u)
      =(delta+z^(-2))*u^3
       +(epsilon*z^(-1)+eta*z^(-2))*u^2
       +(epsilon*z+eta*z^2)*u+(z^2+delta).

Thus V_N=F(x,x^N) exactly.
The two-variable mean m_2(F) is the next discriminator: the binary cost obstruction alone does not show m_2(F)>=log2.
If every sign template instead has m_2(F)<log2, [C849](../claims/Yin_C_G0849_v1.md#fixed-bivariate-template-specialization-class) already supplies a fixed-template gap under its genuine integral-value and original-window hypotheses.
No new theorem follows merely from writing that application.
The [J134 diagnostic](../computations/programs/Yin_J_G0134/readme.md) retains exact finite identity checks and exploratory Jensen quadrature separately from proof.
Numerical means are not certified upper or lower bounds and do not establish the desired limiting inequality.
The actual completed meshes1024,4096 and16384 gave all eight sign means near0.2275,0.3671 or0.5630, with no value near or above log2.
This family therefore supplies a genuine long binary-cover cost but no evidence for the required high-Haar branch.
The numerical search is stopped at that stated failure; proving its negative margin would be an application-preparation question for C849, not a new universal coverage theorem.

<a id="denominator-three-resonance-obstruction"></a>
## The fixed-lift obstruction and its actual arithmetic repair

The exact q=3 seed family, strict high-Haar estimate and absolutely irreducible non-binomial residue template are fixed and independently reviewed in [C859](../claims/Yin_C_G0859_v1.md#decision-whole-independent-review-2026-11-04).
Its [balanced-lift comparison](../claims/Yin_C_G0859_v1.md#balanced-lift-coverage) shows that the same arithmetic inputs already have a short energy-eight numerator, by replacing the seed coefficient 2 with -1 modulo3.
The existing C844 scalar theorem then supplies the original-window gap, including zero evaluated values.
Thus the chosen bad phase is a formal template obstruction, but this entire family is not an uncovered arithmetic class.
Its uncomputed one-variable binomial cost is no longer prioritized for advancing G0001.

## Remaining question after minimizing the actual residue lift

For a proposed phase V and fixed denominator q, first minimize the squared integer coefficients in its coefficientwise residue class modulo q, preserving any necessary endpoint and span facts.
Every such change preserves algebraic integrality of V(alpha)/q on the same integer unit.
If a nonzero resulting numerator has coefficient energy at most q^2 and is not a true signed monomial +/-q x^j, [C844 Part A](../claims/Yin_C_G0844_v1.md#statement) already supplies its paid original-window gap.
The next genuine test must therefore retain a residue class whose minimal available energy exceeds q^2, or identify a concrete restriction preventing the purported replacement.
For that class, test a strict phase mean or another actually paid certificate while keeping near-one original-input supply separate.
No such uncovered family or unrestricted supply theorem is established by the present examples.

<a id="binary-reflection-reduction"></a>
## Exact residue energy and the binary sign question

This is continuing author work for Yin, developed by the certificate-supply contributor on 2026-11-05, Asia/Shanghai.
It is a direct coefficient calculation and a conditional reuse of the accepted scalar and bounded-term theorems, not an independently reviewed result.

### The exact coefficient minimum before any analytic choice

Let q>=2, let H=sum_(r=0..k)h_r x^r be any allowed seed of C845, let n>0, sigma in{1,-1}, T=n+k and t=k-n.
Put V=x^n H+sigma H* and rho_q(c)=min_(z in Z)|c+qz|.
Since H(0) is nonzero and its energy is at most q^2, while the constant seeds +/-q are excluded, the nonzero endpoint h_k satisfies |h_k|<q.
Thus every coefficientwise representative of V modulo q retains nonzero endpoint residues at 0 and T.
The minimum coefficient energy among all such representatives is attained by taking a nearest residue independently at every exponent; adding terms at other exponents cannot lower it.
Its value is exactly

    E_min(V mod q)
       =2 sum_(0<=r<=k, r>t) rho_q(h_r)^2
        +2 sum_({r,s}, 0<=r<s<=t, r+s=t)
                                      rho_q(h_r+sigma h_s)^2
        +1_(t>=0 and t even) rho_q((1+sigma)h_(t/2))^2.  (BE1)

When t<0 the second and third sums are empty and the first includes every coefficient of H.
For t>=0, the outside indices r>t contribute the two separate coefficients h_r and sigma h_r at reflected exponents.
Each distinct pair r+s=t contributes h_r+sigma h_s and its sigma multiple at the two overlap positions.
Only r=s=t/2 contributes a single central coefficient, proving the formula without a generic no-overlap assumption.
Any minimizing representative supported in [0,T] has actual span T because the two endpoint residues remain nonzero.
Its quotient value at the same algebraic integer alpha is integral whenever V(alpha)/q is integral, since the change divided by q is an integer polynomial in alpha.

### At denominator two only three and four pairs remain beyond scalar energy

For q=2 every nonzero coefficient of H is +/-1, and H has at most four such coefficients.
The reduction of V is reciprocal, with nonzero endpoints, and its central coefficient is zero: an overlap center contributes either 2h_r or zero.
Consequently its support has exactly 2s terms in s reflected pairs, with 1<=s<=4, and

    E_min(V mod2)=2s.                                  (BE2)

The values s<=2 are already covered by [C851's explicit scalar cutoff](../claims/Yin_C_G0851_v1.md#explicit-scalar-cutoff-and-rigidity), including zero evaluated values, because a minimizing representative has energy at most4 and cannot be +/-2 times a monomial.
Its exact conclusion is T*m(P)/d>u_s(2), and an original window T<=Cd gives m(P)>u_s(2)/C.
For s=3 or4, no coefficientwise congruent representative has energy at most4, even if extra exponents are allowed.
This does not exclude a useful multiple or another algebraic-integral auxiliary with different residues.

Let e_1,...,e_s be the distinct supported exponents below T/2, including zero.
For every independent sign choice epsilon_j in{1,-1}, the polynomial

    A_epsilon(x)=sum_(j=1..s)epsilon_j(x^(T-e_j)-x^(e_j))  (BE3)

is a coefficientwise representative of V modulo2.
It is nonzero, has the same span T, at most eight terms and coefficient length at most8, and has integral A_epsilon(alpha)/2 on the same original field whenever V(alpha)/2 is integral.
No symmetry requirement on the original chosen lift restricts these sign choices.

With a_j=T/2-e_j, the actual circle formula is

    m(A_epsilon)=integral_0^(2pi)
          log|2 sum_j epsilon_j sin(a_j theta)| dtheta/(2pi).  (BE4)

All a_j are distinct and positive, and are either all integers or all half-integers.
In the half-integer case put b_j=2a_j, which are all odd, and substitute theta=2u.
The absolute value of the resulting sum has period pi, so its normalized integral over [0,pi] equals the normalized full-circle integral for the positive integer frequencies b_j.
Thus the integer-frequency question covers both parity cases without changing the actual original field or degree.

Conversely, every tuple of distinct positive integers b_1,...,b_s with s<=4 occurs in an allowed binary phase configuration.
Write K=max b_j, b=min b_j, choose n=K+b, k=K-b and H=sum_j epsilon_j x^(b_j-b).
Then H has energy s, actual degree k and nonzero constant coefficient, and

    x^n H-H*=sum_j epsilon_j(x^(K+b_j)-x^(K-b_j)).       (BE5)

This includes k=0 when s=1, where the allowed seed is a constant +/-1.
The reduction therefore does not introduce a larger artificial frequency class merely to simplify the analytic task.

### The supplied binary class is covered; original-input supply remains open

[C864 v2](../claims/Yin_C_G0864_v2.md#decision-whole-independent-review-2026-11-04) proves a uniform positive Gamma_bin(C) whenever an actual original unit admits one of these integral binary reflections of span at most C*d.
The theorem includes both reversal signs, all allowed seeds, zero auxiliary values, full residue multiplicities and integrality in the full original ring.
Its low-pair branch uses C862; its large primitive-frequency branch uses the adopted C863 v4; every bounded primitive-frequency pattern returns through a full binary quotient-ring period and the original degree-d binomial norm.
No remaining pure-circle inequality or exceptional-circle enumeration is required for that supplied-class conclusion.

Consequently a sufficiently near-one input has no such short binary auxiliary.
For reciprocal inputs, its degree-linear trace code has no nonzero word of weight at most four, and distinct unordered trace-residue pairs have distinct sums.
These exact restrictions still allow the zero code and do not produce a word, seed or shift.
The arithmetic problem is now to obtain an actual input-specific relation or a different uniformly paid certificate for every sufficiently near-one input.
A proposed finite-field or trace-recurrence construction must identify how the actual small total Mahler measure supplies the required relation within the paid original window.

The separate analytic assertion of a uniform good sign on every four-frequency circle remains open only on the finite primitive candidates specified by [C863 v4](../claims/Yin_C_G0863_v4.md#explicit-finite-circle-reduction).
Its completion would strengthen the pure analytic theorem, but is no longer the missing premise of the binary supplied-class gap.

The [J134 screen](../computations/programs/Yin_J_G0134/readme.md#binary-sign-screen) supports only selecting this analytic question.
Its shifted 2048-point quadrature on the stated finite tuples has no certified error bound near zeros and proves neither the all-frequency assertion nor a uniform margin.
Pointwise sign averaging is insufficient: the real sine coefficients can align at an individual angle, so a valid proof must use their actual common circle parameter and integer frequencies.

<a id="binary-bad-sign-control"></a>
### A bad sign and a cyclotomic sign on the same genuine support

The stronger assertion that every anti-reciprocal sign lift has Mahler measure below2 is false even for an allowed energy-four binary seed.
Take the positive frequencies(1,3,7,9), K=9, n=10 and k=8.
For signs(1,-1,1,1), the actual seed is H_bad=1-x^2+x^6+x^8, and

    A_bad=x^10 H_bad-H_bad*
         =x^18+x^16-x^12+x^10-x^8+x^6-x^2-1
         =Q(x^2),
    Q(y)=y^9+y^8-y^6+y^5-y^4+y^3-y-1
         =(y-1)(y^2+1) f(y),
    f(y)=y^6+2y^5+y^4-y^3+y^2+2y+1
         =y^3 C(y+y^(-1)),
    C(t)=t^3+2t^2-2t-5.                               (BE6)

All displayed identities follow by multiplication.
Here is a strict proof that M(A_bad)>2, independent of J134's quadrature.
The critical points of C are(-2+/-sqrt10)/3, and its local maximum has value(20sqrt10-83)/27<0.
Thus C has exactly one real root a.
The exact values C(3/2)=-1/8 and C(38/25)=1447/15625 show

    3/2<a<38/25<2.

The other roots are a nonreal conjugate pair u+iv,u-iv.
Their sum and product give u=-(a+2)/2 and u^2+v^2=5/a.
Consequently

    2u^2/9+2v^2=10/a-4(a+2)^2/9
        >125/19-30976/5625
        =1+7706/106875>1.                             (BE7)

The strict comparison uses the fact that10/a-4(a+2)^2/9 is strictly decreasing for a>0.
Choose the solution w of w+w^(-1)=u+iv with |w|=r>1.
Such a choice exists because the two roots are reciprocal and a unit-circle w would give a real trace.
Writing w=r exp(i theta), if r<=sqrt2 then

    2u^2/9+2v^2
      =((r+r^(-1))^2/(9/2))*cos(theta)^2
        +((r-r^(-1))^2/(1/2))*sin(theta)^2<=1,

contrary to(BE7).
Hence r>sqrt2.
The two roots over the real trace a lie on the unit circle, while the four roots over u+iv,u-iv consist of w,w^(-1),conjugate(w),conjugate(w)^(-1).
It follows that M(f)=r^2>2.
The two other factors of Q are cyclotomic, and substitution x->x^2 preserves Mahler measure, so M(A_bad)=M(f)>2.

On exactly the same binary support choose signs(1,-1,-1,1).
The seed H_good=1-x^2-x^6+x^8=(1-x^2)(1-x^6) is reciprocal, giving

    A_good=x^10 H_good-H_good*
          =(x^10-1)(1-x^2)(1-x^6),
    M(A_good)=1.                                       (BE8)

Both seeds have energy4 and the same degree8; both full auxiliaries have span18 and are congruent coefficientwise modulo2.
Thus every actual original input with integral A_bad(alpha)/2 also has integral A_good(alpha)/2 in the same field and window.
This is a genuine need to choose a sign, not a counterexample to the existence-of-a-good-sign question or to its original arithmetic application.
The control is already covered once the good sign is selected; no new near-one family or unrestricted gap follows.

## Reuse and source-search scope

The bounded search inspected the current C141, C144, C720, C724, C840 and C842--C851 interfaces relevant to sparse supply, same-input precision and phase separation.
An external search for recent Lehmer coefficient-congruence results led back to the already retained JT26 source and its adequate U001/U002; no new JT26 acquisition or acceptance is needed.
The new trace-one search identified the primary Cohen--Kapetanakis theorem above; the 1990 publisher page returned403 when opened, and secondary search summaries are not mathematical premises.
The recognized square-lattice measure prompted the bounded Guttmann--Rogers statement check just recorded; its arXiv v2 URL was unavailable to the browser, while the author-hosted published PDF supplied the exact displayed identity.
The remaining G0001 obligation in this inquiry is automatic original near-zero-input supply or another paid arithmetic mechanism; the binary energy-four supplied class is covered by C864 v2.

<a id="trace-order-supply-test"></a>
## The actual trace-order rank-collapse candidate and its failed current implication

This bounded contributor inquiry on 2026-11-04 tests input-specific dyadic saturation as a source of a short trace relation; it establishes no automatic supply theorem or new independently reviewed result.
For an actual reciprocal nontorsion integer unit of degree2h, put beta=alpha+alpha^(-1), F=Q(beta), A=Z[beta], O=O_F and D=O/A.
The elementary group-theoretic identity is

    ker(A/2A -> O/2O) isomorphic to D[2],
    r_2=dim_(F_2)image(A -> O/2O)=h-kappa,
    kappa=dim_(F_2)D[2].                              (TS1)

The isomorphism sends u+A, with2u in A, to2u+2A.
It is well-defined and injective because2u in2A forces u in A, and every a in A intersect2O arises from u=a/2 in O.
The dimension formula follows because A is free of rank h.
This elementary identity holds for any trace-field signature; it does not extend the domain of a separately cited local theorem.
A large value of v_2([O:A]) by itself cannot be substituted for kappa, which counts the two-torsion directions rather than their exponents.

Every trace t_n=alpha^n+alpha^(-n) belongs to A by t_0=2, t_1=beta and t_(n+1)=beta*t_n-t_(n-1).
Consequently all the trace residues and their pair sums lie in the image of cardinality2^(r_2).
In the exact near-one range and window of [C864 v2](../claims/Yin_C_G0864_v2.md#trace-code-weight-five), its disjoint Sidon sets therefore give the diagnostic necessity

    2^(r_2)>=1+N(N+1)/2,   2N<=Cd.                    (TS2)

The rank-collapse candidate would need a genuine small-Mahler argument producing the opposite strict inequality for some N proportional to d, hence an upper image dimension below log_2(1+N(N+1)/2), of order2log_2N.
No such archimedean-to-dyadic rank estimate is proved here.
Equation (TS2) is a diagnostic consequence of the accepted trace-code theorem, not a new source of a weight-four word.

The actual [C198 local image formula](../claims/Yin_C_G0198_v1.md#trace-order-local-image-exact-kernel) already describes this image through the original residue clusters and their full local multiplicities.
Its accepted scope assumes a totally real trace field and the original specified canonical quotient values.
Its stronger bound r_2<=floor(10h/11) additionally requires the full residual equations f=0, e+sigma*g=0 and g!=0 for a fixed sigma in{1,-1}; small total Mahler measure alone is not among the hypotheses forcing those equations.
Even when those hypotheses hold, a ten-elevenths dimension bound remains compatible with (TS2) at N proportional to d and does not force the required logarithmic rank collapse.
The underlying local formula is not silently promoted to all trace signatures, and no universal near-one bound for kappa is inferred.

The inspected [C18 capacity theorem](../claims/Yin_C_G0018_v1.md#statement) retains a dimension-dependent lattice constant and fixed-input determinant asymptotics, rather than the missing uniform image-rank estimate.
The [Sam07 integral factor interface](../audits/literature/Sam07/Yin_U001.md#sam07-u001) requires a supplied congruence exponent, while [ADZ14's central-extension height theorem](../audits/literature/ADZ14/Yin_U001.md#central-local-height-theorem) retains fixed base degree and fixed local-degree data.
Applying the latter over the quadratic trace extension K/F does not keep its base degree fixed when h grows.
These inspected inputs therefore do not close this candidate's missing implication.

A bounded primary-source search used Mahler measure, trace-order index, sparse multiples, and small height.
The [MS25 institutional abstract](https://pure.royalholloway.ac.uk/en/publications/short-mahler-measure-preserving-multiples-of-multivariable-polyno/) still describes a potentially failing shortness method, not a guaranteed compression theorem for arbitrary near-one inputs.
Only that primary abstract was read; the linked accepted-manuscript request returned HTTP403, and no manuscript algorithm or proof was inspected.
This preserves the existing [abstract-only MS25 boundary](../audits/literature/MS25/readme.md#abstract-only-scope), without a new theorem premise or identical retry.
The publisher HTML for [Small Mahler measures with bounds on the house and shortness](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/small-mahler-measures-with-bounds-on-the-house-and-shortness/9B26AFC3240DB267B05C4E660F4BFCA2), Theorems2.2--2.3, was also read at statement scope: those finiteness assertions assume shortness5 or6 and a fixed house bound above1, rather than supply such shortness from small total measure.
No claim of exhaustive search, new source acceptance or absence of a different method is made.

The precise continuation point is an actual estimate coupling small total m(P) to the original local image or to a short Chebyshev-basis representative of a nonzero saturation class.
Formal trace recurrences, the present index information and the inspected shortness statements supply no such estimate.
This rank-collapse branch is left at that concrete missing implication, with no new fixed negative Claim or numerical diagnostic.

The inspected [MS12b Pisot/interlacing representation](../audits/literature/MS12b/Yin_U001.md#ms12b-u001) supplies a different source of actual Salem-specific representations with degree controlled linearly by the original degree.
Its source statement does not supply the coefficient-energy or binary-support bound needed by C864 v2, and it does not cover the entire reciprocal-unit domain.
Any use of that representation must establish the missing support/integrality-window interface on the chosen representative; the existence of some interlacing representation alone does not discharge it.

<a id="sparse-compactness-and-cgl26-test"></a>
## Existing sparse-gap coverage of the generalized Boyd family

[CGL26-U001](../audits/literature/CGL26/Yin_U001.md#cgl26-u001) already records inspection of the original v1 abstract and Sections 4.1--4.2, including Equation (19), rendered PDF pages 16--17 and comparison with versioned HTML.
Its existing DS17/L19 comparison covers the seven-term numerator and its entire quotient by cyclotomic factors, while the reported searches and further asymptotic, irreducibility and cyclotomic-classification arguments retain their unverified scope.
An arbitrary selected noncyclotomic factor requires separate information, with the source unit linking C92's bounded span-to-factor-degree interface.
Neither this construction, the [C221 completion criteria](../claims/Yin_C_G0221_v1.md#controlled-entropy-completion), nor the [fixed-polynomial Lawton interface](../audits/literature/Den09/Yin_U002.md#den09-u002) supplies automatic uniformly bounded-support completion for arbitrary near-one inputs.

<a id="automatic-multiple-and-frobenius-supply"></a>
## Automatic small-coefficient multiples and Frobenius values retain different missing costs

This author-working comparison tests two automatic original-input constructions against the supplied binary criterion.
It supplies no new auxiliary for all near-one inputs and makes no new independent-review or source-acceptance claim.

The adopted [C281 norm-grid construction](../claims/Yin_C_G0281_v1.md#effective-first-height-one-relation) already supplies, for every actual original nonzero algebraic integer with m(P)<log 2, a nonzero height-one multiple Q=P C with

    deg Q < ceil[(2d/(log 2-m(P)))log(8d/(log 2-m(P)))].

On any fixed m(P)<=m_0<log 2 this is O_(m_0)(d log(d+1)).
The guaranteed support bound is the same order, and the multiplier only satisfies m(C)<=log(support Q)/2-m(P).
Thus this is actual positive supply of a relation, but it supplies neither the degree-linear window nor the fixed coefficient support needed by [C864 v2](../claims/Yin_C_G0864_v2.md#statement).
The [constant-weight variant](../claims/Yin_C_G0281_v1.md#degree-support-tradeoff) keeps its sufficient condition binomial(n,k)>(5k)^d M(P)^(n-1); it does not assert a relation at fixed k and n proportional to d.

For reciprocal P, reflection can preserve the annihilation relation but does not repair those two estimates by itself.
If Q has degree L and support K, then for n>=1 and sigma in {1,-1}, the polynomial x^n Q+sigma Q* is again divisible by P, is nonzero with span n+L, and has at most K binary reflected pairs before overlap cancellation.
Taking n=1 therefore gives an integral half-value, including zero, but the available estimates remain K=O(d log d) and L+1=O(d log d).
Neither overlap cancellation to at most four pairs nor a different linear-span representative follows from the construction.
Binary Frobenius dilation also leaves the number of nonzero coefficients unchanged and multiplies the span by 2^a, since Q(x)^(2^a)=Q(x^(2^a)) in characteristic two.
It cannot by itself turn those bounds into the desired fixed-pair, original-degree window.
These observations delimit this proposed postprocessing; they do not exclude a different compression argument using additional original-input information.

The other attempted automatic source is the normalized Frobenius value.
Using the full powered-root polynomial P^[2], coefficientwise Frobenius gives H_P=(P^[2]-P)/2 in Z[x], with degree below d and

    Res(P,P^[2])=2^d Res(P,H_P),
    H_P(alpha)=P^[2](alpha)/2.

This is exactly the existing [C1 normalized doubling object](../claims/Yin_C_G0001_v1.md#fixed-doubling-reuse-boundary), with the [C231 full-root convention](../claims/Yin_C_G0231_v1.md#mixed-power-resultant-identities) and C237 local refinements retained there.
It is not a new source of arithmetic income merely because its value is integral.
The same fixed C1 account retains the actual Lehmer control with normalized R_(1,2)=1 and R_(1,3)=1, whereas its full confluent quantity also includes the separate index I_2^2.
Thus even on an actual small reciprocal input, an individual normalized Frobenius norm can have no strict surplus.
The current [C860 v4 resultant budget](../claims/Yin_C_G0860_v4.md#coherent-center-precision-budget) still pays the full d log(2d) term in its cross-resultant estimate.
A positive replacement would have to prove new joint original-conjugate information, a useful collection of actual norm surpluses, or a genuinely cheaper original auxiliary; none of those follows from the displayed automatic half-value.

The bounded source comparison also located Idris--Sac-Epee, [On the existence of Newman and Littlewood multiples for certain integer polynomials, arXiv:2607.15520](https://arxiv.org/abs/2607.15520), whose primary indexed abstract reports finite examples without Newman multiples at Mahler measure as low as 1.263095875491, and finite Littlewood-degree results.
Only that abstract was inspected at the primary index; the direct arXiv page and HTML requests were unavailable, so no original theorem proof, certification program or finite output is adopted here.
In particular its reported positive-measure controls neither prove nor refute automatic supply below every possible threshold above one, and its abstract supplies no uniform degree-linear or fixed-support construction.
This lead is not a new premise for G0001.

The remaining first unsupported step is therefore quantitative compression from actual small total Mahler measure to a fixed-support relation in a degree-linear original window, or an alternative norm certificate with a proved original cost return.
The finite-field recurrence alone, the height-one multiple alone and the separate normalized Frobenius integrality alone each omit that information.
No such compression theorem or new favorable near-one class is established by this bounded inquiry.
