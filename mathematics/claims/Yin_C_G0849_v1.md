---
author: Yin
---

# Uniform Mahler gaps from fixed bivariate templates at all exponent ratios

Human author Yin.
Root proposed the finite primitive-ratio split, finite-field patch, general Laurent-template extension and exact contribution boundary.
Primitive_second_eight checked and assembled the complete certificate, content and monomial reductions, finite-field multiplicities, original-field arithmetic, all costs, fixed-reversal corollary and source/effectiveness limits.
Both are substantive contributors, not independent reviewers of this proof.
The [current adopted decision](#decision-whole-reviewed-2026-10-28) selects the complete statement and proof with [whole independent R1069](../audits/reviews/Yin_R_G1069_v1.md#whole-all-ratio-template-finding).
The OPEN wording retained inside the fixed argument describes its initial author status; the current selection and historical decisions remain distinct.
No native computation, numerical cutoff, finite-field exponent evaluation or source acquisition is part of this result.

## Statement

### A. Fixed templates and every actual positive specialization ratio

<a id="fixed-bivariate-template-specialization-class"></a>
**Definition.** Fix an integer q>=2 and a nonempty finite set Fset of nonzero integer Laurent polynomials F(z,w) with

    m_2(F)=integral_(T^2)log|F(z,w)|<log q.             (ST1)

Integrals use normalized Haar measure and natural logarithms, with torus zeros retained.
An admitted specialization consists of an actual nontorsion algebraic integer unit alpha with monic irreducible minimal polynomial P of ORIGINAL degree d>=2, one template, positive integers n,g and

    V(x)=F(x^g,x^n)!=0,
    V/q notin Z[x,x^(-1)],
    V(alpha)/q algebraically integral in Q(alpha).    (ST2)

The value may be zero; coefficientwise nonintegrality and nonzero-polynomial conditions are separate.
Write T=span V and m(P)=log M(P) for TOTAL logarithmic Mahler measure.
The unit and coefficientwise conditions force T>0.
No reciprocity, monicity of the templates, order membership, good prime, bounded ramification or degree preservation under powering is required.

There is a positive rational a(q,Fset), algorithmically computable from the finite input under ST1, such that EVERY admitted specialization satisfies

    T*m(P)/d>a(q,Fset).                              (ST3)

Consequently, for every fixed real C>0, the additional original window T<=C*d gives m(P)>a(q,Fset)/C, uniformly in every positive pair n,g and every original degree.
No large-separation hypothesis is imposed.
The rational a is independent of C; an effective numerical gap follows from computable C or a supplied rational upper bound, not from an unspecified noncomputable real parameter.

### B. Complete computable construction and all costs

Let A,B be the maximum separate z,w exponent widths over Fset, K=max(2,max #supp F), S=max(1,ceil(max ||F||_1/q)) and B_reg=S^2+1.
BT3 gives a terminating rational constant-coefficient search producing delta,J,eta and a domain-first positive dyadic u with

    c_F<-2eta,
    Ju<h0,
    (1+S/delta)u+2^J epsilon(Ju)<eta,
    (K-1)epsilon(u)+2Ku<1,                           (ST4)

using the exact c0,h0,epsilon displayed in the proof.
For ell=gcd(n,g), n0=n/ell and g0=g/ell, every pair with n0>JA or g0>JB has exact finite constant-term preservation.
At every remaining positive primitive pair, the true undilated span is at most L=2JAB.
If A,B>=1, for each prime pi dividing q put

    M_L=lcm(1,...,L), e_pi=min{e>=0: pi^e>=L},
    N_pi=pi^(e_pi)*(pi^(M_L)-1),
    a(q,Fset)=min(u,min_(pi|q)u_pi/N_pi),             (ST5)

where u_pi is any computable dyadic output of adopted C845's ordered algorithm at modulus pi.
If A=0 or B=0, all positive pairs are good and a=u; no empty-range lcm is formed.
The finite-field exponent retains every irreducible multiplicity, and actual content/monomial stripping makes the construction valid for nonmonic specializations whose endpoint coefficients vanish modulo pi.

The good branch pays the true collected span T, raw delta q*delta, raw B q^2*B_reg, radial multiplier1+S/delta, frequency range JT, coefficient price2^J and matrix size2JT+1.
C92 excludes a zero evaluated auxiliary before the original degree-d norm is used.
The exceptional branch uses the actual binomial exponent N_pi*ell<=N_pi*T, with C845's full original-field costs listed in BT18a.
There is no replacement of d by [Q(alpha^ell):Q], no squarefree substitution and no uncharged exponent enlargement.
The algorithms are proved to terminate but are not numerically executed; no useful runtime or optimal constant is asserted.

### C. Every exponent ratio for fixed monic reversal seeds

<a id="fixed-reversal-all-ratio-corollary"></a>
Let Gset be any fixed finite nonempty monic integral family with M(G)<q and actual degree k_G, including initial zeros and G=1.
For every positive n,g and either sigma in{+1,-1}, put

    F_(n,g,G,sigma)=x^n G(x^g)+sigma G*(x^g),
    G*(x)=x^(k_G)G(1/x), T=n+g*k_G.                  (ST6)

If F_(n,g,G,sigma)(alpha)/q is algebraically integral in the original field, allowing zero, the same type of uniform positive bound T*m(P)/d>a_G holds for every original degree and every n/g ratio.
The leading coefficient1, constant coefficient sigma and true span T show that the polynomial and coefficientwise exclusions in A hold automatically, even under overlap.
For these templates m_2(wG(z)+sigma G*(z))=m(G) by scalar Jensen and legitimate Fubini through zeros.
BT8 proves the optional single-prime constant a_G=min(u_G,u_pi/N_pi(2kJ_G)) for k=max deg G>=1 and ANY ONE fixed prime pi|q; for k=0 take a_G=u_G.
Thus T<=C*d gives m(P)>a_G/C.
This option retains all costs and needs no minimum over different primes or low-degree completion.

### D. Essential hypotheses and coverage boundary

The nonintegral-coefficient hypothesis is essential: F=z+w, q=2 and g=n gives m_2(F)=0 but V/2=x^g, which is integral on every integer unit and has span0.
The claimed positive paid-span inequality cannot include that case.
The finite-template and strict mean hypotheses, actual integrality and original window are conditional data, not an automatic construction for arbitrary P.
There is no uniform assertion over changing template families or q, no numerical gap, near-one construction, novelty or unrestricted Lehmer conclusion.
In particular this theorem does not remove C847's repetition condition for its unbounded family of period seeds.

## Complete argument

The proof below contains the complete general argument, explicit finite-field lemma, all original costs and the single-prime fixed-reversal corollary.
No mutable Draft, unrun program or C848 assertion is a proof premise.

### BT1. Exact reused inputs and finite-template domain

[C842 EF2--EF5](Yin_C_G0842_v1.md#ef2-a-computable-finite-two-variable-majorant) supplies the finite regularized logarithm mechanism, but the changed template domain and every specialization below are proved explicitly.
[Den09-U001's Mahler conventions and singularities](../audits/literature/Den09/Yin_U001.md#mahler-measure) retains the standard fact that a nonzero Laurent polynomial has integrable logarithm, one-variable Jensen with unit-circle zeros and invariance under monomial multiplication.
That existing unit was read at its actual accepted-statement scope; its original general integrability proof was not audited there and is not claimed newly audited here.
All integrals use normalized Haar measure and natural logarithms, with no principal-value or zero-deletion convention.
The finite-field input is the inspected [Hun74-U006](../audits/literature/Hun74/Yin_U006.md#hun74-u006), and the patch uses [adopted C845](Yin_C_G0845_v1.md#decision-whole-reviewed-2026-10-28) only at constant seed1 in its original-field Statement B.
[C137 Sections1--2](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) supplies the finite majorant, raw radial estimate, full nonconstant Fourier price and nonzero original norm floor.
[C92's effective-support inequality](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) excludes a possible zero value before that norm is used, with [C570's exact powered angular modulus](Yin_C_G0570_v1.md#uniform-powered-angular-coherence), original multiplicities and inherited source limits.
These exact adopted interfaces are reused; no low-degree completion by C394 is needed.

The bounded comparison read [C140's normalized sparse criterion](Yin_C_G0140_v1.md#statement) and [C141's modular-divisor/zero interface](Yin_C_G0141_v1.md#reuse-full-modular-divisor).
C140 requires a supplied negative circle Mahler margin, which is not assumed for the exceptional polynomials below; C141's fixed-prime noncoverage does not supply or refute the present conditional theorem.
[C433's primitive-trinomial theorem](Yin_C_G0433_v1.md#statement), with C428 as its preceding full-polynomial limit account, concerns a different complete doubling expression and positive phase limit, not the present original-input arithmetic conclusion.
The corrected [C135 v2 antecedent account](Yin_C_G0135_v2.md#binary-binomial-antecedent-correction) credits [C71's full dyadic gate](Yin_C_G0071_v1.md#tailored-dyadic-full-gate), nonzero guards and prior original linear-width gap.
Those results already supply binomial mechanisms on their exact dyadic original-order/divisibility domains; here C845's constant seed gives the required prime-general FULL-algebraic-integrality interface.
[C848's finite-support exclusion](Yin_C_G0848_v1.md#statement) has a varying low-coefficient-energy seed domain and does not settle every excluded ratio; it is comparison only, not a proof premise.
No novelty or exclusive arithmetic coverage follows from this bounded reuse screen.

Fix an integer q>=2 and a nonempty finite set Fset of NONZERO integer Laurent polynomials F(z,w), with the proved promise

    m_2(F):=integral_(T^2)log|F(z,w)|<log q.            (BT1)

Let A be the maximum z-exponent width among the templates and B the maximum w-exponent width.
Widths are maxima minus minima in each support, not absolute exponent locations.
Set

    K=max(2,max_F #supp F),
    S=max(1,ceil(max_F ||F||_1/q)), B_reg=S^2+1.        (BT2)

Let alpha be an actual nontorsion algebraic integer unit of monic irreducible minimal polynomial P, ORIGINAL degree d>=2 and total logarithmic Mahler measure m(P)>0.
For positive integers n,g and one template require

    V(x)=F(x^g,x^n)!=0,
    V/q notin Z[x,x^(-1)],
    V(alpha)/q algebraically integral in Q(alpha),
    T=span V<=C*d, fixed real C>0.                    (BT3)

The value may initially be zero; the Laurent polynomial and its coefficientwise nonintegrality are separate hypotheses.
No monicity or reciprocity of the templates, reciprocity of P, monogenic-order membership or good-prime hypothesis is assumed.
There is a computable positive rational a(q,Fset), independent of n,g,alpha,d and C, such that

    T*m(P)/d>a(q,Fset),   m(P)>a(q,Fset)/C.            (BT4)

For arbitrary positive real C the latter is a real mathematical bound.
For computable C, a rational upper bound C_hat>=C yields the computable rational gap a/C_hat; no effective output is inferred from an unspecified noncomputable C.

### BT2. Width zero is empty and normalization preserves the original unit

If T=0, then V=a_0*x^v with nonzero integer a_0 and integer v.
Multiplying the integral value V(alpha)/q by the algebraic integer unit alpha^(-v) would make the rational a_0/q an algebraic integer, hence an integer, contrary to BT3.
Therefore every admitted input has T>0.
For v0=min supp V set

    W=x^(-v0)V in Z[x], deg W=span W=T, W(0)!=0,
    W(alpha)/q=alpha^(-v0)V(alpha)/q.                 (BT5)

This preserves full integrality and vanishing in the SAME original field, and changes its absolute norm only by |Norm(alpha)|^(-v0)=1.
Coefficient collection gives #supp W<=K, ||W||_1<=qS and rho(W):=||W||_1^2/||W||_2^2<=K, with every nonzero original coefficient retained.

### BT3. A terminating common finite certificate from the mean promise

For each template use f=F/q and f^dagger(z,w)=f(z^(-1),w^(-1)).
At stages r=1,2,... put

    delta_r=2^(-r), J_r=ceil(B_reg*2^(3r)),
    Y_(F,r)=1-(f f^dagger+delta_r^2)/B_reg,
    Phi_(F,r)=(log B_reg)/2
                      -(1/2)sum_(j=1..J_r)Y_(F,r)^j/j,
    c_(F,r)=CT_(z,w)Phi_(F,r).                        (BT6)

All nonlogarithmic coefficients are rational.
Because |f|<=S and delta_r<=1, one has 0<=Y<=1-delta_r^2/B_reg<1.
The scalar-series estimate already proved in C842 gives

    0<=Phi_(F,r)-(1/2)log(|f|^2+delta_r^2)
       <=B_reg/[2(J_r+1)delta_r^2]<=2^(-r)/2.         (BT7)

The regularized mean decreases to m_2(F)-log q<0 by accepted logarithmic integrability; subtract from a common upper bound before applying monotone convergence.
Thus c_(F,r) tends to a negative limit for each of the FINITELY many templates.
Write c_(F,r)=(log B_reg)/2-b_(F,r) with rational b_(F,r).
Use C842 EF3's rational logarithm-series intervals to compute L_r with 0<=L_r-log B_reg<=2^(-r), and the rational U_r=max_F(L_r/2-b_(F,r)).
Continue if U_r>=0; otherwise set delta=delta_r, J=J_r and eta=min(1,-U_r/4).
This terminates and certifies c_F<=U_r<-2eta for every template, without an exact transcendental equality test, numerical quadrature, BS13 constant or quantitative specialization rate.

Retain C570's exact modulus

    c0=log2/4, h0=c0 exp(-20),
    b(v)=max(v,sqrt(v/c0)log sqrt(c0/v)),
    epsilon(v)=min(1,15sqrt(b(v))+4v), 0<v<=h0.

Choose a positive dyadic u by the domain-first rational-interval search satisfying

    Ju<h0,
    (1+S/delta)u+2^J epsilon(Ju)<eta,
    (K-1)epsilon(u)+2Ku<1.                            (BT8)

Certify Ju<h0 before evaluating either epsilon value.
Dovetail candidates and precisions for the strict tests; termination follows from epsilon(v)->0.
The parameters depend only on the fixed finite input, with no coefficient-energy assumption on its templates.

### BT4. Every good primitive ratio uses the TRUE specialized span

Let ell=gcd(n,g), n0=n/ell and g0=g/ell.
The Fourier support of f f^dagger lies in |a|<=A,|b|<=B, so that of Phi lies in |a|<=JA,|b|<=JB.
Coprimality gives ag+bn=0 exactly when(a,b)=(n0*t,-g0*t) for an integer t.
If

    n0>JA OR g0>JB,                                  (BT9)

only t=0 is possible, so

    CT_x Phi_F(x^g,x^n)=c_F<-2eta.                    (BT10)

If A=0 or B=0, all positive pairs are good.
Negative exponent locations are harmless because these are width bounds.

Set h=T*m(P)/d and suppose h<=u.
For W from BT5, C92 first excludes W(alpha)=0: its exact positive-span inequality would give
1<=(rho(W)-1)epsilon(h)+2rho(W)h<1.
Only then is Res(P,W)=q^d Norm(W(alpha)/q) a nonzero integer multiple of q^d in the ORIGINAL degree d.
Use C137 with delta_raw=q delta and B_raw=q^2 B_reg, so B_raw>=||W||_1^2+delta_raw^2 and the radial multiplier is at most1+S/delta.
Since W W^dagger=V V^dagger, the raw finite majorant is exactly log q+Phi_F(x^g,x^n).
Subtract the original norm floor and apply BT8--BT10:

    0<=c_F+(1+S/delta)h+2^J epsilon(Jh)<-eta<0.       (BT11)

Thus T*m(P)/d>u.
After ACTUAL coefficient collection W W^dagger has frequencies in[-T,T], so the finite majorant has range JT and matrix size2JT+1, with coefficient price2^J.
These costs use true T even if gA+nB is larger or interior coefficients cancel.
No original conjugate or powered-field multiplicity is removed.

### BT5. Every exceptional ratio: content, monomial factor and full multiplicity

Assume A,B>=1.
Exceptional coprime pairs have n0<=JA and g0<=JB, hence form a finite set.
For the actual template and pair put A_r(x)=F(x^g0,x^n0).
The substitution x->x^ell is injective on Laurent polynomials and preserves their coefficient lists.
Thus V=A_r(x^ell), and zero or coefficientwise q-divisible A_r are precisely those excluded by BT3.
An admitted A_r is also not a monomial by BT2, and

    1<=t_r=span A_r<=g0*A+n0*B<=L:=2JAB,
    T=ell*t_r.                                      (BT12)

Let v_r=min supp A_r, h_r its positive coefficient content, and put

    c_r=gcd(q,h_r), q_r=q/c_r>1,
    A'_r=x^(-v_r)A_r/c_r in Z[x].                    (BT13)

The degree is t_r<=L, the integer constant term is nonzero, and
gcd(content A'_r,q_r)=gcd(h_r/c_r,q/c_r)=1.
Neither primitivity over Z nor monicity is asserted.
Here O_(Q(alpha)) denotes the algebraic integers in the SAME original field, not an assumed monogenic order.
The exact original-unit identity is

    A'_r(alpha^ell)/q_r
       =alpha^(-v_r*ell)*V(alpha)/q in O_(Q(alpha)).  (BT14)

Choose a prime pi|q_r, necessarily dividing fixed q.
Then A'_rbar is nonzero modulo pi; write it as x^v f with f(0)!=0 and deg f<=L, allowing constant f.
Both the leading degree and constant term may have dropped modulo pi.
For every pi|q define

    M_L=lcm(1,...,L), e_pi=min{e>=0: pi^e>=L},
    N_pi=pi^(e_pi)*(pi^(M_L)-1).                     (BT15)

<a id="uniform-finite-field-binomial-exponent"></a>
**Finite-field lemma.** Every polynomial over F_pi of degree at most L and nonzero constant term divides x^(N_pi)-1, up to its harmless nonzero scalar factor.
A nonzero constant polynomial divides it immediately.
For positive degree, factor its monic normalization into distinct monic irreducibles f_i with multiplicities m_i.
Each f_i has degree e_i<=L and nonzero constant term, and F_pi[x]/(f_i) is a field with pi^(e_i) elements.
Hun74-U006 Proposition5.6 implies that its nonzero element represented by x satisfies x^(pi^(e_i)-1)=1.
Since e_i divides M_L, the integer pi^(e_i)-1 divides pi^(M_L)-1, so f_i divides x^(pi^(M_L)-1)-1.
That polynomial is squarefree: its exponent is not divisible by pi and its derivative has no common root with it.
In characteristic pi,

    x^(N_pi)-1=(x^(pi^(M_L)-1)-1)^(pi^(e_pi)).        (BT15a)

Every m_i<=L<=pi^(e_pi), so all repeated factors are retained; pairwise coprimality gives the full divisibility.
This proves the lemma without replacing the input by its radical or requiring a number-field good prime.
Apply it to the actual f above.
A nonzero scalar is a field unit, so f itself divides x^(N_pi)-1; a constant f causes no exception.
Consequently A'_rbar divides x^v(x^(N_pi)-1).
Lift the actual quotient coefficientwise to obtain integer B_r,C_r with

    x^v(x^(N_pi)-1)=B_r(x)A'_r(x)+pi C_r(x).         (BT16)

This retains every repeated factor and the full mod-p monomial v, without an assumption about reduction of the original P.

### BT6. The patch and the complete effective constant

Because pi|q_r, BT14 implies A'_r(alpha^ell)/pi is integral by multiplication by q_r/pi.
Evaluate BT16 at alpha^ell and divide by the algebraic INTEGER UNIT alpha^(v*ell):

    (alpha^(N_pi*ell)-1)/pi
      =alpha^(-v*ell)*[B_r(alpha^ell)A'_r(alpha^ell)/pi
                                     +C_r(alpha^ell)]
                                       in O_(Q(alpha)). (BT17)

No order index, good reduction, ramification bound or minimal polynomial of alpha^ell is used.
For each pi|q take u_pi from adopted C845's ordered algorithm at modulus pi.
Its constant seed1, minus sign and shift N_pi*ell satisfy every hypothesis on the original alpha, giving

    N_pi*ell*m(P)/d>u_pi,
    T*m(P)/d=t_r*ell*m(P)/d>t_r*u_pi/N_pi>=u_pi/N_pi. (BT18)

The patched span N_pi*ell is at most N_pi*T<=N_pi*C*d.
For clarity, let Delta_pi, B_ph,pi and J_pi be C845's exact phase regularization, raw-normalized bound and cutoff at modulus pi, and retain its actual u_pi.
The seed H=1 has nonzero constant term, degree0 and energy1<=pi^2, differs from +/-pi, and its shift N_pi*ell>0 satisfies the degree-zero separation automatically.
The binomial has true support2 and length2; its genuine span is N_pi*ell.
The full costs are

    delta_raw=pi*Delta_pi, B_raw=pi^2*B_ph,pi,
    radial multiplier1+2pi/Delta_pi,
    frequency J_pi*N_pi*ell, coefficient price2^(J_pi),
    matrix size2J_pi*N_pi*ell+1.                     (BT18a)

All original d conjugates remain, regardless of the degree of alpha^ell, and no patched exponent is treated as an uncharged constant.
Nontorsion already makes the binomial value nonzero, although C845 includes an initially possible zero value.
Prime powers dividing q require no separate Hensel or valuation argument: exact content removal produces q_r, and one prime divisor with nonzero reduction suffices.

For A,B>=1 return

    a(q,Fset)=min(u,min_(pi|q)u_pi/N_pi)>0;            (BT19)

if A=0 or B=0 return a=u without forming L or its lcm.
The finite minimum is a computable positive rational depending only on fixed inputs.
BT11 and BT18 prove BT4 for all positive ratios and all actual degrees.
No exceptional specialization needs to be enumerated to obtain this sufficient constant: uniform L and the finite prime divisors of q suffice.
No C394, original-degree enumeration, number-field order computation or numerical evaluation of N_pi is part of the proof.

### BT7. Fixed-reversal corollary, essential exclusion and scope

For a finite monic G family with M(G)<q take F_(G,sigma)(z,w)=wG(z)+sigma G*(z) for both signs.
For almost every z, |G*(z)|=|G(z)| and G(z)!=0; scalar Jensen in w gives the inner mean log|G(z)|.
Den09-U001's accepted integrability justifies Fubini through the null zero sets, hence m_2(F_(G,sigma))=m(G)<log q.
Their specializations have leading coefficient1, constant coefficient sigma and true span n+g*k_G, including G(0)=0 and G=1.
They are therefore never zero or coefficientwise divisible by q.
This proves the fixed-reversal corollary for all n,g; BT8 gives its useful single-prime sufficient constant without repeating the general good-ratio proof.

The coefficientwise exclusion is essential to this paid-span criterion.
For F(z,w)=z+w and q=2, Jensen gives m_2(F)=0<log2, but g=n gives V=2x^g and V(alpha)/2=alpha^g integral for EVERY algebraic integer unit, with true span0.
Without the exclusion, the strict first inequality BT4 is impossible and the supplied-certificate condition becomes tautological in this example.
This is not a counterexample to Lehmer's conjecture or a claim about other possible gaps.

The result requires fixed finite templates with their strict mean promise, a nonzero coefficientwise nonintegral specialization, full algebraic integrality at an actual original unit and a supplied original linear window.
It neither supplies templates for arbitrary inputs nor gives a uniform constant over varying families or q.
In particular it does not remove C847's repetition condition for its unbounded family of period seeds.
The actual finite-field, binomial and finite-Fourier antecedents are credited in BT1; no novelty, original-source proof audit, practical complexity, numerical run, near-one construction or unrestricted conclusion is claimed.
The general statement and its fixed-reversal corollary are fixed OPEN here for fresh whole independent review and responsible adoption.

<a id="single-prime-reversal-constant"></a>
### BT8. The fixed-reversal family can use one chosen prime

Let the integer q>=2 and a fixed finite nonempty monic integral Gset satisfy M(G)<q, with actual degrees k_G and k=max k_G; initial zeros of G are allowed.
In this subsection write V_G=x^n G(x^g)+sigma G*(x^g) for the specialized univariate auxiliary.
Use the two signs and exact endpoints from BT7, so every specialized auxiliary has leading coefficient1, constant coefficient sigma and span T=n+g*k_G.
For these templates choose K_G=2(k+1), S_G=max(1,ceil(2 max_G ||G||_1/q)) and B_G=S_G^2+1.
The C842 EF2--EF3 minus-sign certificate supplies delta_G,J_G,eta_G; the plus-sign certificate is identical because f_(G,+)(z,w)=-f_(G,-)(z,-w).
Choose u_G by the three inequalities (BT8) with these G-specific parameters and K_G, using the same ordered domain-first algorithm.
Their Fourier widths are |a|<=k*J_G, |b|<=J_G, so the proof of BT4 applies unchanged when n0>k*J_G or g0>J_G.
It gives T*m(P)/d>u_G, with all original costs and zero handling already proved there.
If k=0, every G=1 and every positive pair is good; set a_G=u_G and form no lcm.

If k>=1, exceptional pairs satisfy n0<=k*J_G, g0<=J_G.
For every G and sign their actual A_r=x^n0 G(x^g0)+sigma G*(x^g0) is monic, has constant sigma and degree between1 and L_G=2k*J_G, even when its two interior blocks overlap.
Fix ANY ONE prime pi dividing q, uniformly for the whole family, and define M_(L_G), e_pi and N_pi(L_G) as in BT15 with L=L_G.
All A_r reductions have their full degree and nonzero constant term modulo this same pi.
The finite-field lemma therefore gives an exact integer identity

    x^(N_pi(L_G))-1=B_r A_r+pi C_r.                 (BT20)

No content reduction or mod-p monomial stripping is needed in this monic unit-constant case.
Since A_r(alpha^ell)/pi=(q/pi)*(V_G(alpha)/q) is an algebraic integer in the ORIGINAL field, BT20 gives the same full binomial integrality and C845 bound as BT17--BT18.
Thus the single-prime option is

    a_G=min(u_G,u_pi/N_pi(L_G))>0, k>=1,
    T*m(P)/d>a_G, m(P)>a_G/C.                        (BT21)

This uses only one chosen pi instead of the all-prime minimum needed for arbitrary nonmonic template specializations.
All patched costs in BT18a remain charged with N_pi(L_G)*ell<=N_pi(L_G)*T; no improvement over another sufficient constant is asserted.
For n=d,g=1,sigma=-1 and V_G in(P,q), ideal membership gives the original integral value and T/d<=1+k/2, recovering C842's earlier finite-reversal class with a possibly different constant and without its bounded-degree completion.
The genuinely enlarged conditional domain permits arbitrary supplied n,g, both signs and full algebraic integrality, still with the SAME fixed finite G family.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision fixed-template-all-ratios-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T23:35 |
| status | open |
| reason | Fix the complete general finite-bivariate-template original-unit gap at every positive exponent ratio, with exact coefficientwise exclusion, true specialized span, effective finite certificate, full finite-field content/monomial/multiplicity patch, original-degree costs and fixed monic reversal corollary with its single-prime option. Root and primitive_second_eight are substantive contributors. Whole independent review and responsible adoption remain separate; no numerical execution, new source audit, automatic all-input coverage or unrestricted conclusion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire general theorem and corollary](#statement) | Complete A--D/ST1--ST6: fixed finite integer Laurent templates and strict mean promise, every positive exponent pair and original degree, full algebraic integrality including zero, nonzero/coefficientwise exclusion, actual span, effective constants and costs, fixed monic reversal corollary and all coverage/computability boundaries. |
| argument | [Complete BT1--BT8 proof](#complete-argument) | Exact finite certificate and primitive kernel, positive-domain and zero-before-norm handling, original Laurent normalization, full content/monomial finite-field patch including repeated factors and lost modular endpoints, complete original-field binomial costs, every degenerate-width/constant case, Jensen corollary and single-prime refinement. |
| dependency | [Adopted finite reversal certificate](Yin_C_G0842_v1.md#decision-whole-reviewed-2026-10-28) | EF2--EF5 only: scalar-series tail, finite rational logarithm/constant-term search, exact raw scaling and positive-domain cutoff mechanism. General-template adaptation and every exceptional-ratio branch are proved here; no C394 or bounded-period conclusion is imported. |
| dependency | [Adopted constant-seed original norm theorem](Yin_C_G0845_v1.md#decision-whole-reviewed-2026-10-28) | Statement B at H=1, degree0, sign minus, modulus any prime pi dividing q and shift N_pi*ell>0; full algebraic integrality in the unchanged original field, every original embedding, actual exponent and all BT18a costs. No varying-seed separation is bypassed. |
| dependency | [Adopted finite logarithmic norm mechanism](Yin_C_G0137_v1.md#decision-isolated-whole-review-20261023-m04) | Sections1--2/equations1--7: finite majorant and scalar tail, raw radial multiplier, nonconstant coefficient price2^J, actual original span and matrix size, nonzero full original norm floor. |
| dependency | [Adopted zero-value exclusion](Yin_C_G0092_v1.md#decision-current-isolated-whole-review-20261022-m04) | Exact nonzero rational-polynomial positive-span/effective-support inequality, used before any evaluated norm logarithm under the stated positive epsilon domain. |
| dependency | [Adopted powered angular modulus](Yin_C_G0570_v1.md#decision-complete-isolated-whole-adoption) | c0,h0,b,epsilon, monotonicity, computability and zero limit, negative frequencies and every original powered-field repetition; inherited Pri11/Dim19 accepted-source limits unchanged. |
| dependency | [Accepted Mahler conventions and integrability](../audits/literature/Den09/Yin_U001.md#den09-u001) | Mahler-measure passage only: normalized Haar/natural logarithms, nonzero Laurent-polynomial logarithmic integrability, one-variable Jensen through zeros and monomial invariance; standard accepted statements, without a new audit of their original proofs or determinant-theory input. |
| dependency | [Accepted finite-field interface](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Chapter V Section5, Proposition5.6 and finite-field cardinality/splitting-polynomial conventions at the recorded statement/applicability scope. The full universal exponent, multiplicities and integer lifts are proved locally; no global Frobenius or number-field realization input. |
| support | [Normalized sparse criterion comparison](Yin_C_G0140_v1.md#statement) | Its supplied negative circle Mahler margin is not assumed for exceptional A_r; no BS13 constant or original proof is imported. |
| support | [Earlier modular-divisor and zero scope](Yin_C_G0141_v1.md#reuse-full-modular-divisor) | Existing original-order divisor/zero mechanism and finite-prime coverage limits are comparison only, not a supply of present template certificates. |
| support | [Corrected dyadic antecedent account](Yin_C_G0135_v2.md#binary-binomial-antecedent-correction) | Credits C71's prior full two-binomial gate, nonzero conditions and original linear-width gap; retained general-k valuation scope does not replace the prime-general full-algebraic-integrality premise selected here. |
| support | [Primitive-trinomial specialization comparison](Yin_C_G0433_v1.md#statement) | Different complete doubling expression and positive full-polynomial limit; no BGMP rate, full source proof or trinomial conclusion is a premise. |
| support | [Finite-support good-shift comparison](Yin_C_G0848_v1.md#statement) | Different varying low-coefficient-energy domain and support-dependent good shifts, not the present every-ratio finite-template patch; no C848 assertion is used in the proof. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T23:51 |
| status | proved |
| reason | Adopt the complete general Statement A--D and BT1--BT8 proof after root read both full author arguments, the entire assembled fixed C849 and whole independent R1069. The true Laurent span and coefficientwise exclusion, exact finite certificate, every primitive ratio, full content/modular-monomial/multiplicity patch, same original-field binomial transfer and all costs are covered, including degenerate widths and the both-sign monic reversal single-prime corollary. Accepted source inspection limits and computable-C qualifications remain exact. No numerical execution, arbitrary varying-template or varying-modulus coverage, automatic near-one certificate or unrestricted Lehmer conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire general theorem and corollary](#statement) | Complete A--D/ST1--ST6: fixed finite integer Laurent templates and strict mean promise, every positive exponent pair and original degree, full algebraic integrality including zero, nonzero/coefficientwise exclusion, actual span, effective constants and costs, fixed monic reversal corollary and all coverage/computability boundaries. |
| argument | [Complete BT1--BT8 proof](#complete-argument) | Exact finite certificate and primitive kernel, positive-domain and zero-before-norm handling, original Laurent normalization, full content/monomial finite-field patch including repeated factors and lost modular endpoints, complete original-field binomial costs, every degenerate-width/constant case, Jensen corollary and single-prime refinement. |
| dependency | [Adopted finite reversal certificate](Yin_C_G0842_v1.md#decision-whole-reviewed-2026-10-28) | EF2--EF5 only: scalar-series tail, finite rational logarithm/constant-term search, exact raw scaling and positive-domain cutoff mechanism. General-template adaptation and every exceptional-ratio branch are proved here; no C394 or bounded-period conclusion is imported. |
| dependency | [Adopted constant-seed original norm theorem](Yin_C_G0845_v1.md#decision-whole-reviewed-2026-10-28) | Statement B at H=1, degree0, sign minus, modulus any prime pi dividing q and shift N_pi*ell>0; full algebraic integrality in the unchanged original field, every original embedding, actual exponent and all BT18a costs. No varying-seed separation is bypassed. |
| dependency | [Adopted finite logarithmic norm mechanism](Yin_C_G0137_v1.md#decision-isolated-whole-review-20261023-m04) | Sections1--2/equations1--7: finite majorant and scalar tail, raw radial multiplier, nonconstant coefficient price2^J, actual original span and matrix size, nonzero full original norm floor. |
| dependency | [Adopted zero-value exclusion](Yin_C_G0092_v1.md#decision-current-isolated-whole-review-20261022-m04) | Exact nonzero rational-polynomial positive-span/effective-support inequality, used before any evaluated norm logarithm under the stated positive epsilon domain. |
| dependency | [Adopted powered angular modulus](Yin_C_G0570_v1.md#decision-complete-isolated-whole-adoption) | c0,h0,b,epsilon, monotonicity, computability and zero limit, negative frequencies and every original powered-field repetition; inherited Pri11/Dim19 accepted-source limits unchanged. |
| dependency | [Accepted Mahler conventions and integrability](../audits/literature/Den09/Yin_U001.md#den09-u001) | Mahler-measure passage only: normalized Haar/natural logarithms, nonzero Laurent-polynomial logarithmic integrability, one-variable Jensen through zeros and monomial invariance; standard accepted statements, without a new audit of their original proofs or determinant-theory input. |
| dependency | [Accepted finite-field interface](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Chapter V Section5, Proposition5.6 and finite-field cardinality/splitting-polynomial conventions at the recorded statement/applicability scope. The full universal exponent, multiplicities and integer lifts are proved locally; no global Frobenius or number-field realization input. |
| support | [Normalized sparse criterion comparison](Yin_C_G0140_v1.md#statement) | Its supplied negative circle Mahler margin is not assumed for exceptional A_r; no BS13 constant or original proof is imported. |
| support | [Earlier modular-divisor and zero scope](Yin_C_G0141_v1.md#reuse-full-modular-divisor) | Existing original-order divisor/zero mechanism and finite-prime coverage limits are comparison only, not a supply of present template certificates. |
| support | [Corrected dyadic antecedent account](Yin_C_G0135_v2.md#binary-binomial-antecedent-correction) | Credits C71's prior full two-binomial gate, nonzero conditions and original linear-width gap; retained general-k valuation scope does not replace the prime-general full-algebraic-integrality premise selected here. |
| support | [Primitive-trinomial specialization comparison](Yin_C_G0433_v1.md#statement) | Different complete doubling expression and positive full-polynomial limit; no BGMP rate, full source proof or trinomial conclusion is a premise. |
| support | [Finite-support good-shift comparison](Yin_C_G0848_v1.md#statement) | Different varying low-coefficient-energy domain and support-dependent good shifts, not the present every-ratio finite-template patch; no C848 assertion is used in the proof. |
| review | [Whole independent all-ratio template finding](../audits/reviews/Yin_R_G1069_v1.md#whole-all-ratio-template-finding) | Entire Statement A--D and BT1--BT8, every actual-span/domain/zero/content/modular-endpoint/multiplicity/original-norm branch and all enlarged costs, fixed-reversal single-prime option, exact accepted sources and comparison/effectiveness limits; independent arrangement without mutable Draft or substantive repair. |

