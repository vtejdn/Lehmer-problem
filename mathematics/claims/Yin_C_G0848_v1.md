---
author: Yin
---

# Finite-support phase noncollision and bounded exceptional shifts

Human author Yin.
Root supplied the finite-support resonance construction, uniform exception count, many-shift and support-lattice consequences, and both near-diagonal comparison classes.
Contributor core_feedback_structure checked the complete support/endpoint arguments, changed arithmetic transfer, both reciprocal-class constructions and the actual older C93/C95 coverage, including the eight-term alternative for the ten-term presentation.
Both are substantive proof contributors.
This complete project deduction is [adopted](#decision-whole-reviewed-2026-10-28) after [whole independent R1068](../audits/reviews/Yin_R_G1068_v1.md#whole-finite-support-phase-finding) at the exact fixed scope below.
The [D7 source section](../drafts/Yin_D_G0007.md#finite-support-phase-noncollision) supplies extraction provenance only; no mutable Draft is a proof premise.

## Statement

Fix an integer q>=2.
An allowed seed is H in Z[x] with H(0)!=0, actual degree k>=0, sum_r H_r^2<=q^2, and H different from the two constant polynomials +/-q.
Let S={r:H_r!=0}, s=|S|, and H*(x)=x^k H(1/x); both signs sigma in{+1,-1} are allowed.
The seed need not be monic or reciprocal and its degree and support may vary.
All coefficients below are true collected coefficients, all torus integrals use normalized Haar measure, and all spans retain actual endpoints.

Use the SAME q-only constants and cutoff as C845:

    B=q^2+1, delta=1/(2q^2 B), eta=1/(8q^4 B^2),
    delta_p=delta*eta, B_p=4q^2+1,
    J=J_p=ceil(B_p/(eta*delta_p^2)),
    c0=log2/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0)log sqrt(c0/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0.

Choose any computable positive dyadic u_q satisfying

    J u_q<h0,
    (1+2q/delta_p)u_q+2^J epsilon(Ju_q)<eta,
    (2q^2-1)epsilon(u_q)+4q^2 u_q<1.

C845's ordered algorithm proves existence and first certifies J*u_q<h0 BEFORE evaluating either epsilon term.
Neither this algorithm nor the finite-set enumeration below has been numerically executed here.

**A. A finite support test with a degree-independent exception count.**
<a id="phase-support-and-exceptional-shifts"></a>
**Definition (phase support and exceptional shifts).**
Define

    A_H={(r,1):r in S} union {(k-r,0):r in S},
    E_H=A_H-A_H,
    W_J(H)=E_H+...+E_H  (J summands),
    Bad(H)={n in Z_(>0): a+nb=0 for some(a,b) in W_J(H)
                                      with b!=0},
    N_q=(4q^4)^J.

Then

    |W_J(H)|<=(4s^2)^J<=N_q,
    |Bad(H)|<=N_q,       Bad(H) subset {1,...,kJ}.

The set Bad(H) depends only on S, with the same set for both signs and all nonzero coefficient values on that support.
It is exactly computable by finite integer sumsets, divisibility tests and comparisons.
For k=0 it is empty.
The bound is uniform in k, but N_q is not presented as a practical enumeration size or an evaluated numerical constant.

For f(z,w)=(wH(z)+sigma H*(z))/q, f^dagger(z,w)=f(z^(-1),w^(-1)), and

    Y=1-(f f^dagger+delta_p^2)/B_p,
    Phi=(1/2)log B_p-(1/2)sum_(j=1..J)Y^j/j,

the entire Fourier support of Phi lies in W_J(H).
For EVERY positive n outside Bad(H), the exact finite coefficient identity is

    CT_x Phi(x,x^n)=CT_(z,w)Phi<-2eta.

Membership in Bad(H) need not mean failure of the actual constant-term equality after coefficient cancellation.
The set is not asserted minimal, and no failure of a Mahler gap at an excluded shift is claimed.

**B. Changed arithmetic exclusion with all original degrees and costs.**
Let alpha be an ACTUAL nontorsion algebraic integer unit, P its monic irreducible minimal polynomial, d>=2 its ORIGINAL degree and m=m(P)>0 its TOTAL logarithmic Mahler measure.
For every positive integer n, put F_(n,sigma)=x^n H+sigma H*.
It is nonzero with true degree and span T=n+k, at most2q^2 nonzero coefficients, coefficient length at most2q^2 and effective support rho=||F||_1^2/||F||_2^2 at most2q^2, including any overlap or cancellation between the two blocks.
If n is outside Bad(H) and F_(n,sigma)(alpha)/q is algebraically integral over Z in Q(alpha), allowing zero, then

    (n+k)m(P)/d>u_q.

Full algebraic integrality is sufficient; membership in Z[alpha] is not required.
All d original embeddings, original power multiplicities, the true auxiliary span, radial multiplier1+2q/delta_p, frequency range J*T, coefficient price2^J and matrix size2J*T+1 remain paid.
The proof uses C92 before the nonzero signed norm and repeats C137's raw transfer using A; it does NOT invoke C845 Statement B beyond its n>kJ hypothesis.
For any fixed C>0, the additional original window n+k<=C*d therefore gives m(P)>u_q/C in every degree.

**C. More than N_q distinct integral shifts for one seed.**
For the SAME actual alpha, allowed H, fixed q and C>0, suppose a finite set I contains more than N_q DISTINCT positive integers.
For each n in I suppose there is a sign sigma_n such that F_(n,sigma_n)(alpha)/q is algebraically integral, including a possible zero value, and n+k<=C*d.
Then at least one shift is outside Bad(H), and m(P)>u_q/C.
The signs may vary with n; two signs at one n do not count as two shifts.
No such collection of short integral shifts is supplied for an arbitrary input.

**D. A support-lattice certificate.**
For any positive integer g with S contained in gZ, g>J and gcd(n,g)=1, the positive shift n is outside Bad(H).
This conclusion requires no n/k lower bound and no claim about the degree of a radical or power field.
It is a sufficient support condition, not a conclusion that every seed has such a lattice.

**E. Nonempty near-diagonal comparison classes and their older coverage.**
Write J_3=J_p(3), u_3=u_q at q=3 and K0=(log2/4)/(2*36^8*5^64), the retained C93/C95 constant.
For every odd k>J_3, take H=x^k+2, n=k+2 and sigma=-1.
Then n is outside Bad(H), although n<=kJ_3, and

    F_n=x^(2k+2)+2x^(k+2)-2x^k-1=(x^2-1)Q_k,
    Q_k=sum_(i=0..k)x^(2i)+2x^k.

Every actual monic reciprocal irreducible noncyclotomic P of degree d=2k with P congruent to Q_k modulo3 satisfies m(P)>u_3/2.
There are infinitely many such P in every indicated degree and residue class by C842 NG.
The SAME class already satisfies m(P)>K0/2 by C93: F_n/3 has four terms, energy10/9<5/4 and value in the original order, with the zero branch excluded by C93 A before B.

For every integer g>J_3, take H_0=1+x+x^2+x^3+x^5, H_g=H_0(x^g), k=5g, n=5g+1 and F_g=x^n H_g-H_g*.
Then n is outside Bad(H), although n<=kJ_3; F_g has ten coefficients +/-1 and true degree10g+1, and Q_g=F_g/(x-1) is a monic reciprocal integer polynomial of degree10g and constant term1.
Every actual monic reciprocal irreducible noncyclotomic P of degree d=10g with P congruent to Q_g modulo3 satisfies m(P)>u_3/2, and C842 NG again gives infinitely many such P in each degree/class.
This class too already satisfies m(P)>K0/2, through the different original-order certificate

    A_g=(x^g-1)H_g=x^(6g)-x^(5g)+x^(4g)-1,
    G_g=(x^g-1)F_g=x^n A_g+A_g*.

It has exactly eight coefficients +/-1, normalized energy8/9, true span11g+1<2d and integral value after division by3; C95 A/C supply the prior contradiction.
These examples demonstrate a strictly broader support-separation test than the sufficient n>kJ condition, not new arithmetic class coverage beyond all older criteria.
No numerical comparison of u_3/2 with K0/2, automatic seed production, exclusive-coverage or novelty assertion, varying-q uniformity or unrestricted Mahler conclusion is made.

## Complete argument

<a id="exact-reuse-and-changed-specialization"></a>
### PX1. Preparation and the precise changed question

[Adopted C845](Yin_C_G0845_v1.md#decision-whole-reviewed-2026-10-28) supplies its field-free [Statement A](Yin_C_G0845_v1.md#statement), q-only constants and [complete finite majorant](Yin_C_G0845_v1.md#finite-majorant-and-exact-specialization).
Its n>kJ_p condition is a sufficient way to separate the constant coefficient using only the rectangular frequency bounds.
The question here is whether the ACTUAL finite support gives an effective exclusion set with cardinality bounded independently of the varying seed degree.
The change below does not invoke C845 Statement B as a black box outside its separation hypothesis: the changed specialization is proved directly, and the original arithmetic transfer is paid again in PX5.

[C842 EF4](Yin_C_G0842_v1.md#ef4-exact-finite-frequency-specialization-and-genuine-modulus-scaling) and [C137 Sections1--2](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) already retain exact finite Fourier specialization and the complete logarithmic transfer mechanism.
[C140](Yin_C_G0140_v1.md#statement) already gives a normalized sparse auxiliary criterion when a uniform negative logarithmic margin is supplied, including its [zero closure](Yin_C_G0140_v1.md#normalized-cost-zero-value-closure); it does not itself identify the present support-dependent exceptional shifts, and its BS13 regularization is not used here.
A targeted current Claim search for noncollision, exceptional/forbidden shifts and Minkowski-sum formulations found no retained result supplying this precise exception set or count; C206's Minkowski-sum alphabet identity concerns algebraic entropy, not this phase specialization.
This bounded reuse check does not establish novelty.
The needed source attribution and inspection limits are inherited exactly from C845's field-free calculation, scalar Jensen passage and C137/C92/C570 inputs; no new external result or source acquisition is required.

The concrete q=3 example below DOES have prior arithmetic coverage by [adopted C93](Yin_C_G0093_v1.md#decision-organized-reviewed), whose Statement A supplies independence and four-power saturation and whose Statement B supplies the seven-power energy floor5/4 in the original order.
It will illustrate the changed separation condition, not a new Mahler-gap class beyond all earlier criteria.
The source [JT26 Theorem1.3](../audits/literature/JT26/Yin_U002.md#jt26-u002) is compared only at its literal uniform odd/even residue hypothesis.
[Adopted C842 NG](Yin_C_G0842_v1.md#ng-every-compatible-reciprocal-residue-class-has-infinitely-many-actual-inputs) supplies actual nonvacuity of the reciprocal comparison class, with no new irreducibility or native calculation.

<a id="phase-support-and-uniform-constants"></a>
### PX2. Allowed seeds, fixed constants and the finite support set

Fix an integer q>=2 and an allowed seed H in Z[x] with H(0)!=0, actual degree k>=0, coefficient energy sum_r H_r^2<=q^2, and H different from the two constants +/-q.
Let S={r:H_r!=0}, s=|S|, so0,k belong to S and1<=s<=q^2.
The actual degree-k reversal is H*(x)=x^k H(1/x), and sigma ranges over{+1,-1}.
Use C845's SAME q-only constants and cutoff:

    B=q^2+1, delta=1/(2q^2 B), eta=1/(8q^4 B^2),
    delta_p=delta*eta, B_p=4q^2+1,
    J=J_p=ceil(B_p/(eta*delta_p^2)),
    c0=log2/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0)log sqrt(c0/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0.          (PX1)

Choose any of its computable positive dyadic u_q satisfying

    J u_q<h0,
    (1+2q/delta_p)u_q+2^J epsilon(Ju_q)<eta,
    (2q^2-1)epsilon(u_q)+4q^2 u_q<1.                   (PX2)

The already proved ordered algorithm certifies the first domain inequality before evaluating either epsilon term, and then certifies the other strict inequalities.
No new numerical cutoff is evaluated here.
In particular J>=2 is an integer depending only on q, since B_p>1 and0<eta*delta_p^2<1.

Define the finite integer sets

    A_H={(r,1):r in S} union {(k-r,0):r in S},
    E_H=A_H-A_H,
    W_J(H)=E_H+...+E_H  (J summands).                 (PX3)

The two parts of A_H have distinct second coordinates, so |A_H|=2s; every first coordinate lies between0 and k.
Thus(0,0) belongs to E_H, |E_H|<=4s^2, and every(a,b) in W_J(H) satisfies |a|<=kJ and |b|<=J.
The image of the finite Cartesian product E_H^J under addition is W_J(H), giving

    |W_J(H)|<=|E_H|^J<=(4s^2)^J<=(4q^4)^J=:N_q.       (PX4)

The cardinality bounds in PX4 are independent of k and of all coefficient signs, once q is fixed.
The number N_q is a specified finite integer, not a computed numerical result or practical enumeration bound.

<a id="finite-exception-set-and-specialization"></a>
### PX3. The exceptional set and exact finite specialization

Define the support-dependent set of positive integer shifts

    Bad(H)={n in Z_(>0): a+nb=0 for some(a,b) in W_J(H)
                              with b!=0}.             (PX5)

This set depends only on S and its actual maximum k, not on sigma or the nonzero coefficient values of H.
It is computed exactly by first forming E_H and then W_0={(0,0)}, W_(j+1)=W_j+E_H for j=0,...,J-1.
For each resulting(a,b) with b!=0, retain -a/b precisely when it is a positive integer, and remove repetitions.
All operations are finite integer addition, divisibility and comparison; no root approximation or numerical integration enters this algorithm.
Each pair contributes at most one shift, hence

    |Bad(H)|<=N_q,        Bad(H) subset {1,...,kJ}.     (PX6)

The second assertion follows from n=|a|/|b|<=kJ for every positive resonance.
If k=0, every a is zero, so Bad(H) is empty.
The set is a sufficient support exclusion set: membership does not assert that the actual collected coefficients fail to cancel, or that a gap is false at that shift.

For f(z,w)=(wH(z)+sigma H*(z))/q and f^dagger(z,w)=f(z^(-1),w^(-1)), use C845's actual finite Laurent polynomial

    Y=1-(f f^dagger+delta_p^2)/B_p,
    Phi=(1/2)log B_p-(1/2)sum_(j=1..J)Y^j/j.

Its field-free conclusion gives c_(H,sigma):=CT_(z,w)Phi<-2eta for every allowed seed and either sign.
The support of f is A_H, the support of f f^dagger is contained in E_H, and the support of Y is also contained in E_H because(0,0) belongs to E_H.
For each1<=j<=J, the support of Y^j lies in the j-fold sum of E_H, which is a subset of W_J(H) by padding with zeros.
The constant term of Phi also lies in W_J(H), so its ENTIRE actual Fourier support is contained in W_J(H), regardless of coefficient cancellation.

For any positive n outside Bad(H), a supported frequency maps to zero under(a,b)->a+nb only if b=0 and then a=0.
Consequently

    CT_x Phi(x,x^n)=CT_(z,w)Phi=c_(H,sigma)<-2eta       (PX7)

by exact finite coefficient collection.
No n>k or disjoint-block hypothesis was used.
C845's sufficient condition n>kJ is recovered immediately from PX6, but PX7 also permits smaller shifts whenever this finite resonance test passes.

<a id="lattice-support-noncollision"></a>
### PX3a. A lattice-support certificate with no delay-to-degree ratio

Suppose a positive integer g satisfies S subset gZ, g>J and gcd(n,g)=1.
Then k is also a multiple of g, so every first coordinate of A_H, E_H and W_J(H) is a multiple of g.
For a resonance a+nb=0 with(a,b) in W_J(H), reduction modulo g and coprimality imply g divides b.
Since |b|<=J<g, one has b=0 and then a=0.
Consequently

    S subset gZ, g>J, gcd(n,g)=1  imply n notin Bad(H). (PX7a)

This requires no bound on n/k and does not assert that an arbitrary seed has such a support lattice.
It is a direct finite-support consequence of PX3, not an irreducibility or radical-degree assertion.

<a id="true-endpoints-with-overlap"></a>
### PX4. True endpoints and all coefficient costs, including overlap

For ANY positive integer n, define

    F_(n,sigma)(x)=x^n H(x)+sigma H*(x), T=n+k.

The constant term is sigma H_k!=0, because x^n H has no constant term.
The degree-T coefficient is H_k!=0, because H* has degree k<T.
Therefore F_(n,sigma) is nonzero and its TRUE degree and span are exactly T=n+k>0, even if the two support blocks overlap or some interior coefficients cancel.
The triangle inequality and Cauchy--Schwarz give the complete bounds

    #supp(F_(n,sigma))<=2s<=2q^2,
    ||F_(n,sigma)||_1<=2||H||_1<=2q^2,
    rho(F_(n,sigma)):=||F_(n,sigma)||_1^2/
                      ||F_(n,sigma)||_2^2<=2q^2.     (PX8)

The equalities for separated blocks in C845 are not imported; only these valid inequalities are needed.
No coefficient-energy bound for F itself is assumed.
The specialization of f is exactly F_(n,sigma)/q, including every overlap and collected coefficient.

<a id="original-arithmetic-transfer-and-many-shifts"></a>
### PX5. The changed arithmetic exclusion and the many-shift consequence

Let alpha be an ACTUAL nontorsion algebraic integer unit, P its monic irreducible minimal polynomial of ORIGINAL degree d>=2, and m=m(P)>0 its TOTAL logarithmic Mahler measure.
Retain all d original embeddings and every original powered-field repetition in the inherited C570 modulus.
Suppose n is positive and outside Bad(H), and F_(n,sigma)(alpha)/q is algebraically integral in Q(alpha), initially allowing zero and without requiring membership in Z[alpha].
We prove

    (n+k)m/d>u_q.                                    (PX9)

Put h=T*m/d and suppose for contradiction0<h<=u_q.
If the value is zero, [C92](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) applies to the nonzero rational polynomial of true positive span T from PX4.
Its exact original-degree inequality and PX8 imply

    1<=(rho-1)epsilon(h)+2rho h
      <=(2q^2-1)epsilon(u_q)+4q^2 u_q<1,

contradicting PX2.
Only after this zero exclusion does full algebraic integrality give

    Res(P,F_(n,sigma))=q^d N,
    N=Norm_(Q(alpha)/Q)(F_(n,sigma)(alpha)/q)
                                      in Z minus{0}. (PX10)

Hence the full original logarithmic norm floor is log|Res(P,F_(n,sigma))|/d>=log q.
Apply C137 Sections1--2 to the actual INTEGER polynomial F_(n,sigma), with

    delta_raw=q delta_p, B_raw=q^2 B_p,
    S_raw=||F_(n,sigma)||_1<=2q^2.

Its raw bound B_raw>=S_raw^2+delta_raw^2 holds because B_p=4q^2+1 and delta_p^2<1.
The raw Y is Y(x,x^n), and the raw finite majorant is log q+Phi(x,x^n).
Using the new PX7 identity, rather than assuming C845's large-separation conclusion, gives

    0<=c_(H,sigma)+(1+S_raw/(q delta_p))h
                                +2^J epsilon(Jh)
      <=c_(H,sigma)+(1+2q/delta_p)u_q
                                +2^J epsilon(Ju_q)
      <-2eta+eta=-eta<0.                              (PX11)

All evaluations lie in0<Jh<=Ju_q<h0.
This pays the complete radial multiplier, full original norm, finite frequency range JT, coefficient price2^J and matrix size2JT+1, and proves PX9 without a bounded-degree patch.
No field degree is replaced by a seed degree or specialized power degree.

For any fixed C>0, the additional original window n+k<=C*d yields m(P)>u_q/C.
More generally, suppose the SAME allowed H has a finite set I of more than N_q DISTINCT positive shifts, with for each n in I a sign sigma_n and an algebraically integral value F_(n,sigma_n)(alpha)/q, and with n+k<=C*d for every n in I.
Because Bad(H) is common to both signs and has size at most N_q, some n in I is good, so the SAME gap m(P)>u_q/C follows.
Counting the two signs at one shift as two shifts would be invalid.
Neither this pigeonhole statement nor the finite enumeration supplies those integral shifts or the window for an arbitrary original input.

<a id="four-term-near-diagonal-class"></a>
### PX6. A near-diagonal comparison class with actual nonvacuity

Take q=3, J=J_p(3), any odd integer k>J and n=k+2, with H=x^k+2 and sigma=-1.
Then H(0)=2, its coefficient energy is5<=9, and it is an allowed nonmonomial seed.
Every first coordinate of A_H is0 or k, so every(a,b) in W_J(H) has a=c*k with integer |c|<=J and |b|<=J.
If a+nb=0, gcd(k,k+2)=1 implies k divides b; since |b|<=J<k, necessarily b=0 and then c=0.
Thus n is outside Bad(H).
Since J>=2 and k>J, one has n=k+2<=2k<=kJ, so C845's sufficient condition n>kJ fails for this presentation.

The exact four-term auxiliary and its factorization are

    F_n=x^(2k+2)+2x^(k+2)-2x^k-1=(x^2-1)Q_k,
    Q_k=sum_(i=0..k)x^(2i)+2x^k.                      (PX12)

The comparison Q_k is monic and reciprocal of degree D=2k, with constant term1.
For ANY actual monic reciprocal irreducible noncyclotomic P of degree D satisfying P congruent to Q_k coefficientwise modulo3, write Q_k-P=3R with R in Z[x].
At an original root alpha of P,

    F_n(alpha)/3=(alpha^2-1)R(alpha) in Z[alpha].

This verifies integrality in the original order, including the initially possible zero value; no irreducibility or noncyclotomic assertion about Q_k itself is required.
The actual auxiliary window is T/D=(2k+2)/(2k)=1+1/k<2, so PX9 gives m(P)>u_3/2 for the whole class.
C842 NG applies to the actual symmetric inner residue assignment of Q_k and constructs infinitely many monic reciprocal irreducible noncyclotomic P in each such original degree and residue class.
Its complete CRT/Eisenstein and coefficient costs are reused, not claimed newly executed.

Modulo3 the comparison has all even coefficients1 and all odd coefficients0 except the middle odd index k, which has coefficient2.
Because k>J>=2, the odd indices include both the exceptional middle index and other odd indices.
Thus this class does not satisfy JT26 Theorem1.3's uniform odd-residue hypothesis at modulus3; this literal comparison does not exclude other old criteria or other applications to individual P.

<a id="existing-four-term-class-coverage"></a>
### PX7. The older C93 bound and the exact contribution boundary

For the SAME comparison class, the four distinct exponents0,k,k+2,2k+2 give

    f=F_n/3,
    ||f||_2^2=(1+4+4+1)/9=10/9<5/4,
    f(alpha) in O0=Z[alpha].

Use C93's retained constant K0=(log2/4)/(2*36^8*5^64).
If m(P)<=K0/2, the true span condition is T*m(P)/D=(1+1/k)m(P)<K0.
C93 Statement A then makes the four actual powers rationally independent, so f(alpha) is nonzero BEFORE its nonzero-value Statement B is invoked.
Statement B would force ||f||_2^2>=5/4 for this true nonsigned-monomial polynomial, contradicting10/9.
Equivalently, Statement A's r<=4 saturation directly excludes the genuine denominator3 coefficient vector in the original-order lattice.
Therefore the prior theorem already gives the uniform gap m(P)>K0/2 for this class.
No numerical ordering between this old constant and the unevaluated u_3/2 is required for the coverage conclusion.

The near-diagonal family consequently demonstrates a strict improvement in the support test over C845's sufficient n>kJ bound, with genuine nonempty original coefficient classes, but does NOT establish new Mahler-class coverage beyond the existing small-support theorem.
The general result is the degree-independent finite exceptional-set bound, its exact computable support test, the full original arithmetic transfer for every good shift and the same-seed many-shift consequence.
Bad(H) is not asserted minimal, a bad shift need not fail after coefficient cancellation, and no practical cost of enumeration or numerical N_q has been computed.
No automatic supply of short integral shifts, period application beyond its own retained scope, uniform varying-q bound, near-one construction or unrestricted Lehmer conclusion is obtained.

<a id="ten-term-class-and-eight-term-alternative"></a>
### PX8. A ten-term presentation and its older eight-term alternative

For any integer g>J_p(3), a second concrete test of PX7a uses H_0(x)=1+x+x^2+x^3+x^5, q=3 and

    H_g(x)=H_0(x^g), k=5g, n=5g+1, g>J_p(3),
    F_g=x^n H_g-H_g*, T=10g+1.                       (PX13)

The seed has coefficient energy5<=9, nonzero constant term and leading coefficient1.
Its support is contained in gZ and gcd(n,g)=1, so PX7a applies.
Since n>k, the support blocks are disjoint and F_g has exactly ten coefficients in{+1,-1}.
Thus ||F_g/3||_2^2=10/9>1 and this particular ten-term polynomial does not meet the direct at-most-seven/eight-term hypotheses of C93/C95.
Nevertheless n=5g+1<=2k<=kJ, so the large-separation sufficient condition of C845 again fails for this presentation.

Reversal in the full degree T gives F_g*=-F_g, and F_g(1)=0.
Hence Q_g=F_g/(x-1) lies in Z[x], is monic of degree D=10g and has constant term1.
Since(x-1)*=1-x, the identity F_g*=-F_g implies -(x-1)Q_g*=-(x-1)Q_g and hence Q_g*=Q_g in its actual degree D.
For every actual monic reciprocal irreducible noncyclotomic P of degree D with P congruent to Q_g modulo3, write Q_g-P=3R_g.
Then F_g(alpha)/3=(alpha-1)R_g(alpha) belongs to the original order Z[alpha], and T/D=1+1/(10g)<2.
PX9 therefore gives m(P)>u_3/2, while C842 NG supplies infinitely many such P in each degree and residue class.
This uses no assertion about the irreducibility or noncyclotomic factors of Q_g.

However, the actual earlier-criterion screen finds a different short certificate in the SAME original field and class.
Put

    A_g=(x^g-1)H_g=x^(6g)-x^(5g)+x^(4g)-1,
    A_g*=1-x^g+x^(2g)-x^(6g),
    G_g=(x^g-1)F_g=x^n A_g+A_g*.                     (PX14)

The last sign is positive because reversal in degree6g gives A_g*=-(x^g-1)H_g*.
The four shifted exponents are1 modulo g and the four unshifted exponents are0 modulo g; g>J>=1 prevents collisions between those blocks.
Each block has four distinct exponents, so G_g has exactly eight coefficients in{+1,-1}, true span T'=11g+1 and

    ||G_g/3||_2^2=8/9<1,
    G_g(alpha)/3=(alpha^g-1)F_g(alpha)/3 in Z[alpha].

Use [adopted C95](Yin_C_G0095_v1.md#decision-organized-reviewed) at its actual [Statement A/C](Yin_C_G0095_v1.md#statement) and the same K0 as in PX7.
If m(P)<=K0/2, then T'*m(P)/D<K0 because T'/D=(11g+1)/(10g)<2.
C95 A first supplies independence of the eight actual powers, making the displayed value nonzero; C95 C would then force its energy at least1, contradicting8/9.
Thus this comparison class too already has the older uniform gap m(P)>K0/2.

This is an explicit reason not to infer new arithmetic coverage merely because one proposed auxiliary has ten terms.
Both comparison families verify a genuine gain in the finite-support separation test and have nonempty original classes, while existing smaller certificates cover their Mahler-gap conclusions.
The general bounded-exception and lattice-support results retain their exact fixed-q, supplied-integrality and original-window scope, with no exclusive-coverage or novelty assertion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision finite-support-phase-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T23:00 |
| status | open |
| reason | Fix the complete finite-support exception-set theorem, changed all-original-degree arithmetic transfer, many-shift and lattice-support consequences, and both nonempty near-diagonal examples with their actual earlier C93/C95 coverage. The proof preserves every q-only cutoff, full norm, radial/frequency/matrix cost and source boundary; fresh whole independent review and adoption remain outstanding. No automatic integral-shift supply or unrestricted gap is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete finite-support statement](#statement) | Entire A--E: allowed seeds and constants, exact support/sumset/Bad construction and cardinality, exact finite specialization, original-unit/full-integrality/zero-value arithmetic setting, every cost, many distinct shifts, lattice certificate, both nonempty classes and their older coverage with all limitations. |
| argument | [Complete PX argument](#complete-argument) | PX1--PX8 and PX3a, all PX1--PX14 and PX7a formulas: targeted reuse, support counting/algorithm, exact constant-term proof, overlap-safe endpoints, repeated C92/C137 transfer, multiple-shift and gcd arguments, both comparison constructions, C842 nonvacuity and concrete C93/C95 alternative coverage. |
| dependency | [Field-free uniform phase certificate and q-only constants](Yin_C_G0845_v1.md#statement) | Statement A and its constants/ordered cutoff only: allowed seed domain, actual two-variable Phi, uniform torus constant less than -2eta and computable u_q. Statement B's n>kJ arithmetic conclusion is not invoked outside its domain; the changed transfer is supplied here. |
| dependency | [Finite logarithmic original-root certificate](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) | Sections1--2/equations1--7 only: finite raw majorant, full original radial cost, coefficient price2^J, exact finite-frequency domain/matrix size and nonzero integral norm floor, applied after the new support specialization and zero exclusion. |
| dependency | [Short rational annihilator inequality](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Nonzero rational polynomial of true positive span, effective support at most2q^2 and original-degree zero-value inequality; used before the full signed norm even when the two input blocks overlap. |
| dependency | [Original finite-frequency modulus](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact c0,h0,b,epsilon, positive domain, monotonicity/zero limit, negative frequencies and every original powered-field repetition; inherited Pri11/Dim19 source-inspection boundaries unchanged. |
| dependency | [Actual compatible-class nonvacuity](Yin_C_G0842_v1.md#ng-every-compatible-reciprocal-residue-class-has-infinitely-many-actual-inputs) | NG only: infinitely many actual monic reciprocal irreducible noncyclotomic integer-unit polynomials in each supplied compatible residue class at its original even degree, with exact CRT/Eisenstein and coefficient costs. Used for both examples, not the general exception theorem. |
| dependency | [Existing four-term class coverage](Yin_C_G0093_v1.md#statement) | Statement A independence/four-power saturation and Statement B energy floor5/4 at the actual K0, original order and true span; these already cover the four-term q=3 example, with independence before the nonzero-value floor. |
| dependency | [Existing eight-term alternative coverage](Yin_C_G0095_v1.md#statement) | Statement A independence and Statement C energy floor at the same K0, applied to G_g/3 in the same original order with eight true terms, energy8/9 and span11g+1<2d; this pays the older coverage of the ten-term presentation. |
| support | [Existing finite specialization method](Yin_C_G0842_v1.md#ef4-exact-finite-frequency-specialization-and-genuine-modulus-scaling) | Attribution/comparison for exact finite Fourier coefficient collection and raw modulus scaling; its fixed finite seed family and bounded-degree completion are not used for the new finite exception theorem. |
| support | [Normalized sparse logarithmic comparison](Yin_C_G0140_v1.md#statement) | Existing conditional transfer once an actual uniform negative logarithmic margin is supplied; no BS13 regularization or constant is imported here, and it does not supply the present exceptional-shift set. |
| support | [Literal odd/even residue comparison](../audits/literature/JT26/Yin_U002.md#jt26-u002) | Theorem1.3's fixed uniform odd/even residue conditions only: the central odd defect in the first q=3 example violates its modulus3 parity hypothesis. No exclusion of all earlier criteria or other individual-input applications is inferred. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T23:11 |
| status | proved |
| reason | Adopt the complete Statement A--E and PX1--PX8/PX3a proof after root read the entire author argument, fixed statement and whole independent R1068. The finite support/sumset algorithm and degree-independent exception bound, exact noncollision, true endpoints with overlap, changed C92-before-C137 full-integrality transfer, every original cost, distinct-shift and support-lattice consequences are covered. Both actual reciprocal comparison classes and their explicit older C93/C95 coverage are retained; R329/R331 keep their current self-reviewed input relationships. No automatic certificate availability, minimal bad set, exclusive arithmetic coverage, practical constant or unrestricted Lehmer conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete finite-support statement](#statement) | Entire A--E: allowed seeds and constants, exact support/sumset/Bad construction and cardinality, exact finite specialization, original-unit/full-integrality/zero-value arithmetic setting, every cost, many distinct shifts, lattice certificate, both nonempty classes and their older coverage with all limitations. |
| argument | [Complete PX argument](#complete-argument) | PX1--PX8 and PX3a, all PX1--PX14 and PX7a formulas: targeted reuse, support counting/algorithm, exact constant-term proof, overlap-safe endpoints, repeated C92/C137 transfer, multiple-shift and gcd arguments, both comparison constructions, C842 nonvacuity and concrete C93/C95 alternative coverage. |
| dependency | [Field-free uniform phase certificate and q-only constants](Yin_C_G0845_v1.md#statement) | Statement A and its constants/ordered cutoff only: allowed seed domain, actual two-variable Phi, uniform torus constant less than -2eta and computable u_q. Statement B's n>kJ arithmetic conclusion is not invoked outside its domain; the changed transfer is supplied here. |
| dependency | [Finite logarithmic original-root certificate](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) | Sections1--2/equations1--7 only: finite raw majorant, full original radial cost, coefficient price2^J, exact finite-frequency domain/matrix size and nonzero integral norm floor, applied after the new support specialization and zero exclusion. |
| dependency | [Short rational annihilator inequality](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Nonzero rational polynomial of true positive span, effective support at most2q^2 and original-degree zero-value inequality; used before the full signed norm even when the two input blocks overlap. |
| dependency | [Original finite-frequency modulus](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact c0,h0,b,epsilon, positive domain, monotonicity/zero limit, negative frequencies and every original powered-field repetition; inherited Pri11/Dim19 source-inspection boundaries unchanged. |
| dependency | [Actual compatible-class nonvacuity](Yin_C_G0842_v1.md#ng-every-compatible-reciprocal-residue-class-has-infinitely-many-actual-inputs) | NG only: infinitely many actual monic reciprocal irreducible noncyclotomic integer-unit polynomials in each supplied compatible residue class at its original even degree, with exact CRT/Eisenstein and coefficient costs. Used for both examples, not the general exception theorem. |
| dependency | [Existing four-term class coverage](Yin_C_G0093_v1.md#statement) | Statement A independence/four-power saturation and Statement B energy floor5/4 at the actual K0, original order and true span; these already cover the four-term q=3 example, with independence before the nonzero-value floor. |
| dependency | [Existing eight-term alternative coverage](Yin_C_G0095_v1.md#statement) | Statement A independence and Statement C energy floor at the same K0, applied to G_g/3 in the same original order with eight true terms, energy8/9 and span11g+1<2d; this pays the older coverage of the ten-term presentation. |
| support | [Existing finite specialization method](Yin_C_G0842_v1.md#ef4-exact-finite-frequency-specialization-and-genuine-modulus-scaling) | Attribution/comparison for exact finite Fourier coefficient collection and raw modulus scaling; its fixed finite seed family and bounded-degree completion are not used for the new finite exception theorem. |
| support | [Normalized sparse logarithmic comparison](Yin_C_G0140_v1.md#statement) | Existing conditional transfer once an actual uniform negative logarithmic margin is supplied; no BS13 regularization or constant is imported here, and it does not supply the present exceptional-shift set. |
| support | [Literal odd/even residue comparison](../audits/literature/JT26/Yin_U002.md#jt26-u002) | Theorem1.3's fixed uniform odd/even residue conditions only: the central odd defect in the first q=3 example violates its modulus3 parity hypothesis. No exclusion of all earlier criteria or other individual-input applications is inferred. |
| review | [Whole independent finite-support finding](../audits/reviews/Yin_R_G1068_v1.md#whole-finite-support-phase-finding) | Entire Statement A--E and PX1--PX8/PX3a, every support/domain/overlap/norm/cost branch, actual accepted dependency scopes, both reciprocal-class nonvacuity proofs and their older four/eight-term coverage, with inherited source and self-review relationships preserved. |

