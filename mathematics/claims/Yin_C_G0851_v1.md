---
author: Yin
---

# Finite Fourier budgets and explicit scalar and phase cutoffs

Human author Yin.
Root supplied the independent-variable coefficient majorant, associated sharper exception count and proposed explicit scalar and phase exponents256 and512.
Contributor core_feedback_structure checked the complete finite variance/Parseval/counting proof, actual-versus-lifted mean distinction, all constants and strict domain/error inequalities, original norm scaling, zero branches and growing-denominator consequence.
Both are substantive proof contributors.
The complete project deduction is adopted by the [selected decision](#decision-whole-reviewed-2026-10-28) after [whole independent R1071](../audits/reviews/Yin_R_G1071_v1.md#whole-finite-fourier-budget-finding).
The [D7 source section](../drafts/Yin_D_G0007.md#finite-fourier-budget-and-explicit-cutoffs) supplies extraction provenance only; the entire required argument is fixed below and has no mutable Draft premise.
No fixed predecessor proof, cutoff, review relationship or selected decision is changed by this registration.

## Statement

**A. A finite Fourier coefficient budget for every true term count.**

<a id="finite-logarithmic-coefficient-budget"></a>
**Definition (finite logarithmic coefficient budget).**
Let F(x)=sum_(i=1..N)a_i x^(e_i) be a NONZERO real Laurent polynomial with N>=1 TRUE collected nonzero terms: the exponents e_i are distinct integers and the real a_i are nonzero.
Set S=sum_i|a_i|, choose real delta>0 and B>=S^2+delta^2, and let J>=1 be an integer.
With F^dagger(x)=F(x^(-1)), normalized circle Haar measure and

    Y=1-(F F^dagger+delta^2)/B,
    Phi_J=(1/2)log B-(1/2)sum_(j=1..J)Y^j/j,
    H_J=sum_(j=1..J)1/j,
    Lambda_(N,J)=(H_J/4)*sqrt((2J+1)^(N-1)-1),

one has

    sum_(l!=0)|[x^l]Phi_J|<=Lambda_(N,J).

In particular Lambda_(1,J)=0, and the estimate applies to integer or rational coefficients and negative exponents.
One may also use min{2^J,Lambda_(N,J)}, retaining the old coefficient estimate when it is smaller.
The independent variables used to prove the estimate control coefficient sums only; their Haar mean is not substituted for the actual circle constant.
The hand control F=1+x+x^2, delta=1, B=10, J=2 has actual-minus-lifted constant equal to-1/100.

**B. The same actual logarithmic constant with a smaller available angular expense.**
Throughout the arithmetic parts, let alpha be an ACTUAL nontorsion algebraic integer unit, P its monic irreducible minimal polynomial, d>=2 its ORIGINAL degree and m=m(P)>0 its TOTAL logarithmic Mahler measure.
Retain all original embeddings and actual powered-field repetitions.
Use the exact inherited positive-domain modulus

    c0=log2/4, h0=c0 exp(-20),
    b(v)=max{v,sqrt(v/c0)log sqrt(c0/v)},
    epsilon(v)=min{1,15sqrt(b(v))+4v}, 0<v<=h0.

For F in Z[x] of actual degree T>=1, true term count N, coefficient length S and Res(P,F)!=0, choose rational delta>0 and rational B>=S^2+delta^2 as in A.
Let c_J=CT_x Phi_J be the ACTUAL finite circle constant and h=T*m/d.
On0<Jh<=h0,

    log|Res(P,F)|/d
       <=c_J+(1+S/delta)h+Lambda_(N,J)epsilon(Jh).

If F(alpha)/q is a NONZERO algebraic integer for an integer q>=2, the left side is at least log q by the complete signed original norm.
No norm floor is assigned to a zero value.
The radial expense, actual constant, frequency range JT and finite matrix size2JT+1 are unchanged.
A Laurent numerator is first monomial-normalized with its unit sign accounted for; width0 is treated directly.

**C. An explicit scalar cutoff, rigidity and positive-real-weight consequences.**
Fix an integer q>=2; it need only clear coefficients and need not be their least denominator.
Set

    B_s=q^2+1, delta_s=1/(2q^2 B_s),
    eta=1/(8q^4 B_s^2), J_s=ceil(B_s/(4eta^2)),
    u_s(q)=q^(-256q^2).

For every NONZERO integer Laurent numerator F with coefficient energy at most q^2, algebraically integral F(alpha)/q allowing zero, and true span T satisfying T*m/d<=u_s,

    F=+/-q x^j for some integer j.

For ANY rational Laurent polynomial f with qf integral, NONZERO algebraic-integral value and its OWN true span T satisfying T*m/d<=u_s,

    ||f||_2^2>=1,
    ||f||_2^2=1 if and only if f is a TRUE signed monomial,
    f not a true signed monomial implies ||f||_2^2>=1+1/q^2.

There is no final term-count hypothesis on f, and the last alternative includes a one-term coefficient other than+1 or-1.
For a finite family with the same q, each satisfying the preceding own-span and nonzero integral-value hypotheses, and arbitrary positive REAL weights summing1,

    E>=1+mu/q^2,

where E is weighted coefficient energy and mu is the total weight on nonsigned monomials.
Equality E=1 holds exactly when every indexed atom is a true signed monomial.
No covariance, common union span, minimum weight or rational-weight denominator is assumed.
For a supplied nonmonomial integer numerator of energy at most q^2 and integral quotient value, including zero, the additional original window0<T<=C*d gives m(P)>u_s(q)/C for every fixed C>0 and every original degree.

**D. An explicit phase cutoff with the same large-separation or noncollision test.**
For the same q,B_s,delta_s,eta set

    delta_p=delta_s*eta, B_p=4q^2+1,
    J_p=ceil(B_p/(eta*delta_p^2)),
    u_p(q)=q^(-512q^2).

Let H in Z[x] have H(0)!=0, actual degree k>=0, coefficient energy at most q^2 and H different from the two constants +/-q.
Define its actual reversal H*(x)=x^k H(1/x), let sigma be either sign, and write S_H=supp(H), s=|S_H|.
For J=J_p define the SAME finite support data as C848:

    A_H={(r,1):r in S_H} union {(k-r,0):r in S_H},
    E_H=A_H-A_H, W_J(H)=E_H+...+E_H  (J summands),
    Bad(H)={n in Z_(>0): a+nb=0 for some(a,b) in W_J(H)
                                      with b!=0}.

For any positive n outside Bad(H), put F_n=x^n H+sigma H* and T=n+k.
If F_n(alpha)/q is algebraically integral, allowing zero, then

    T*m/d>u_p(q).

The sufficient condition n>kJ_p is included, because Bad(H) is contained in{1,...,kJ_p}.
Allowed constant seeds, both signs, nonmonic H, nonreciprocal P and overlap of support intervals retain their actual domains.
The true degree and span are T, and the original window T<=C*d gives m(P)>u_p(q)/C in every original degree.
This proof repeats the C92 zero exclusion and B's raw full-norm transfer; it does not use C845/C848 at their older arithmetic cutoffs.

**E. A sharper finite support-exception count and the distinct-shift consequence.**
For the same H and unchanged J=J_p,

    |W_J(H)|<=min{(4s^2)^J,(2J+1)^(2s-1)},
    |Bad(H)|<=N'_q,
    N'_q=min{(4q^4)^J,(2J+1)^(2q^2-1)}.

The actual set Bad(H) is unchanged and is not asserted minimal.
For more than N'_q DISTINCT supplied positive shifts of the SAME H, each with a possibly different sign, integral quotient value including zero, and original window n+k<=C*d, at least one shift is good and m(P)>u_p(q)/C.
Two signs at one n do not count as two shifts, and no supply of such shifts is proved.
C848's support-lattice sufficient condition, supp(H) contained in gZ with positive integer g>J and gcd(n,g)=1, remains valid without an n/k lower bound.
The improved count is also compatible with C848's old cutoff independently of the new Fourier budget.

**F. A conditional growing-denominator budget.**
Fix C>0 and suppose actual inputs with m_j>0 tending to0 have supplied scalar or phase certificates at their respective full hypotheses above, with coefficient-clearing integers q_j>=2 allowed to vary.
For the scalar alternative the certificate is a nonmonomial low-energy numerator as in C, not an arbitrary high-energy scalar value.
Then respectively

    log(1/m_j)<256q_j^2 log q_j+log C,
    log(1/m_j)<512q_j^2 log q_j+log C.

Consequently q_j^2 log q_j=o(log(1/m_j)) is impossible for a family of these certificates eventually.
This is conditional on the actual supplied arithmetic and window data, not a positive gap uniform over all growing denominators or automatic input coverage.

The explicit u_s and u_p are positive rationals and need not be dyadic unless q is a power of2.
They are proved for the NEW Lambda expense and are not asserted to pass the older2^J tests.
The proof retains the actual logarithmic constants, source-inspection boundaries and original radial/frequency/matrix costs.
No optimal exponent, superiority to every older K0 bound, numerical cutoff search, practical enumeration, bounded-degree patch, new source theorem or unrestricted Lehmer conclusion is asserted.

## Complete argument

<a id="exact-reuse-and-coefficient-budget"></a>
### FQ1. Exact reuse and the changed coefficient expense

[C137 Sections1--2](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) already separate the ACTUAL finite circle constant c_J, the full original radial expense and the nonconstant Fourier coefficient sum.
Its equation6 bounds that last sum by2^J using the coefficient length of each power of Y.
Only this coefficient estimate is changed below; neither the actual constant term nor the original conjugate law is replaced.
[C140's normalized sparse transfer](Yin_C_G0140_v1.md#statement) retains the same old2^J estimate after its separate regularization, and [C113](Yin_C_G0113_v1.md#statement) treats discriminant/Gram regularization and sparse support constraints, not the new finite coefficient count.
The scalar field-free margin is the adopted [C844 ER3 calculation](Yin_C_G0844_v1.md#uniform-energy-logarithmic-margin); the phase margin is [C845 Statement A](Yin_C_G0845_v1.md#statement), with exact specialization supplied either by its large-separation argument or by [C848's finite-support condition](Yin_C_G0848_v1.md#finite-exception-set-and-specialization).
Their old arithmetic conclusions are not applied at a cutoff whose old2^J test has not been proved.

The bounded-range variance identity, finite Parseval and coefficient Cauchy--Schwarz are ALREADY explicit in [adopted C168 Section1](Yin_C_G0168_v1.md#actual-cubic-l2-cost), which credits [C145's existing frequency-dimension comparison](Yin_C_G0145_v1.md#statement).
Those calculations count a growing actual circle frequency interval.
The new step here is to bound the coefficient algebra on N independent monomial variables, use its sum-zero frequency lattice, and pull back the resulting coefficient bound without transferring its Haar mean.
The ordinary finite identities are reproduced at the required scope; no new Parseval, variance or Cauchy--Schwarz theorem is asserted.
A targeted local search and the directly read C113/C137/C140/C844/C845/C168 interfaces did not supply this exact independent-variable majorant and explicit256/512 cutoff assembly; this is not an exhaustive search or novelty claim.
The exact [C570 modulus](Yin_C_G0570_v1.md#uniform-powered-angular-coherence), original powered-field multiplicities and inherited Pri11/Dim19 source-inspection limits remain unchanged.
No BS13 constant, new source acquisition, native computation, numerical certificate search or bounded-degree completion is used.

<a id="independent-variable-fourier-majorant"></a>
### FQ2. A finite coefficient majorant from N independent variables

Let F(x)=sum_(i=1..N) a_i x^(e_i) be any NONZERO real Laurent polynomial, with DISTINCT collected integer exponents e_i and real coefficients a_i!=0, so N>=1 is its TRUE term count.
Put S=sum_i|a_i|, choose real delta>0 and B>=S^2+delta^2, and fix an integer J>=1.
On the circle define

    Y=1-(F F^dagger+delta^2)/B,
    Phi=(1/2)log B-(1/2)sum_(j=1..J)Y^j/j,
    H_J=sum_(j=1..J)1/j,
    Lambda_(N,J)=(H_J/4)*sqrt((2J+1)^(N-1)-1).        (FQ1)

Here F^dagger(x)=F(x^(-1)), which equals conjugate(F(x)) on the circle because the coefficients are real.
The assertion is

    sum_(l!=0)|[x^l]Phi|<=Lambda_(N,J).                (FQ2)

It applies in particular to rational or integer coefficients and to negative exponents.
When N=1 the right side is0, exactly as required for a monomial's constant squared modulus.

Introduce independent circle variables z_1,...,z_N ONLY for this coefficient estimate:

    Fhat(z)=sum_i a_i z_i,
    Fhat^dagger(z)=Fhat(z_1^(-1),...,z_N^(-1)),
    Yhat=1-(Fhat Fhat^dagger+delta^2)/B,
    Gammahat=-(1/2)sum_(j=1..J)Yhat^j/j,
    Phihat=(1/2)log B+Gammahat.

On the full N-torus, |Fhat|<=S gives0<=Yhat<=1, and hence

    -H_J/2<=Gammahat<=0.

For a real random variable X with values in[a,b] on a probability space, integrating(X-a)(b-X)>=0 gives

    Var(X)<= (mean X-a)(b-mean X)<=(b-a)^2/4.

This is the elementary range-variance identity already used in C168.
Apply it to Gammahat with a=-H_J/2 and b=0.
Finite character orthogonality on the N-torus, equivalently finite Parseval, gives

    sum_(v!=0)|[z^v]Gammahat|^2
       =Var(Gammahat)<=H_J^2/16.                      (FQ3)

Indeed each distinct integer character has integral0 unless it is the zero character, so this equality follows by expanding the finite square and integrating term by term.
No infinite Fourier series or limiting interchange is involved.

Every exponent of Fhat Fhat^dagger is a difference of two coordinate unit vectors.
Consequently every exponent v of Gammahat satisfies

    sum_i v_i=0,             |v_i|<=J for every i.

The first N-1 coordinates each have at most2J+1 possibilities and determine the last coordinate, so there are at most(2J+1)^(N-1) possible frequencies in total, and at most that number minus1 are nonzero.
Some counted vectors may violate the last coordinate bound or have zero coefficients; this only makes the bound larger.
Cauchy--Schwarz with FQ3 yields

    sum_(v!=0)|[z^v]Phihat|
      =sum_(v!=0)|[z^v]Gammahat|<=Lambda_(N,J).        (FQ4)

Under the monomial substitution z_i=x^(e_i), Phihat becomes exactly Phi.
A lifted frequency v maps to l=sum_i v_i e_i.
For l!=0, every contributing v is nonzero; collecting coefficients and applying the triangle inequality therefore proves FQ2.
Nonzero lifted frequencies that map to zero are simply omitted from this upper bound for NONCONSTANT target coefficients.
There is no assertion that the lifted Haar constant equals the actual circle constant.
The original C137 bound2^J remains valid too, so min{2^J,Lambda_(N,J)} may be used when convenient.
For fixed N this is bounded polynomially in J, for example by H_J<=J; no optimality or efficient-size claim is made.

A small exact control shows why the mean distinction matters.
For F=1+x+x^2, delta=1, B=10 and J=2, the actual circle moments of |F|^2 are3 and19, while those of |z_1+z_2+z_3|^2 are3 and15.
The actual second moment is3^2+2*2^2+2*1^2=19 from the Laurent coefficients of |F|^2, and the independent second moment counts2*3^2-3=15 matching index pairs.
Thus CT_x Phi minus CT_z Phihat is -(19-15)/(4*10^2)=-1/100, not zero.
This example is a hand finite-coefficient calculation; the coefficient bound transfers while the mean does not.

<a id="actual-constant-and-original-norm-transfer"></a>
### FQ3. The same actual constant, original norm and radial expense

In all arithmetic applications below, let alpha be an ACTUAL nontorsion algebraic integer unit, P its monic irreducible minimal polynomial, d>=2 its ORIGINAL degree and m=m(P)>0 its TOTAL logarithmic Mahler measure.
Let F in Z[x] have degree T>=1, true term count N, coefficient length S and nonzero resultant with P.
For rational delta>0, rational B>=S^2+delta^2 and integer J>=1, let c_J=CT_x Phi be the ACTUAL circle constant of FQ1 and h=T*m/d.
On the unchanged domain0<Jh<=h0, C137's proof gives the sharpened inequality

    log|Res(P,F)|/d
      <=c_J+(1+S/delta)h+Lambda_(N,J)epsilon(Jh).       (FQ5)

To verify the changed step explicitly, retain every original root alpha_i=r_i z_i and the original values V_i=F(alpha_i)/max(1,r_i)^T.
C137's exact identity and radial bound are

    log|Res(P,F)|/d=h+(1/d)sum_i log|V_i|,
    |V_i-F(z_i)|<=S min(1,T|log r_i|),
    sum_i|log r_i|=2m.

The derivative bound for psi_delta(t)=(1/2)log(t^2+delta^2) is1/(2delta), so the averaged radial expense is S*h/delta.
The same finite Phi still pointwise majorizes psi_delta(|F|).
Its actual frequencies have |l|<=JT, and C570 bounds every nonzero original angular average by epsilon(Jh).
Apply FQ2 to this ACTUAL Phi to obtain

    (1/d)sum_i Phi(z_i)<=c_J+Lambda_(N,J)epsilon(Jh),

which proves FQ5 with all original multiplicities intact.
The finite matrix size remains2JT+1 and the regularization/Taylor tail remains exactly the original one.

If F(alpha)/q is a NONZERO algebraic integer for an integer q>=2, its complete original signed norm gives

    Res(P,F)=q^d Norm_(Q(alpha)/Q)(F(alpha)/q),
    log|Res(P,F)|/d>=log q.                            (FQ6)

This uses full algebraic integrality, not only membership in Z[alpha].
No such norm floor is applied at a zero value; that case is excluded separately below.
For an integer Laurent numerator, a single monomial normalization gives true degree equal to its positive span, preserves all coefficient counts and circle moduli, and multiplies its full signed norm only by a power of Norm(alpha) in{+1,-1}.
Width0 is handled directly instead of evaluating epsilon(0).

<a id="explicit-modulus-domain-bound"></a>
### FQ4. An elementary bound for the exact inherited modulus

Retain

    c0=log2/4, h0=c0 exp(-20),
    b(v)=max{v,sqrt(v/c0)log sqrt(c0/v)},
    epsilon(v)=min{1,15sqrt(b(v))+4v}, 0<v<=h0.

The elementary integral formula for log2 gives1/8<c0<1, and2<e<4 follows from the exponential series.
In particular

    h0>2^(-43),
    epsilon(v)<=34v^(1/8)<=q^6 v^(1/8)
                    for every q>=2 and0<v<=h0.        (FQ7)

For the second assertion put t=sqrt(v/c0), so0<t<=exp(-10)<1.
Maximizing log x/sqrt x at x=e^2 gives log x<=(2/e)sqrt x for x>=1.
Hence t log(1/t)<=sqrt t, while v=c0 t^2<=sqrt t, so b(v)<=(v/c0)^(1/4).
It follows that epsilon(v)<=15c0^(-1/8)v^(1/8)+4v<=34v^(1/8), using c0^(-1/8)<2 and v<=1.
Finally34<=q^6 for q>=2.
The lower bound for h0 is c0 e^(-20)>(1/8)4^(-20)=2^(-43).
These estimates apply only on the displayed positive domain.

<a id="explicit-scalar-cutoff-and-rigidity"></a>
### FQ5. The explicit scalar threshold and all scalar consequences

Fix q>=2 and retain C844's field-free constants

    B_s=q^2+1, delta_s=1/(2q^2 B_s),
    eta=1/(8q^4 B_s^2), J_s=ceil(B_s/(4eta^2)),
    u_s(q)=q^(-256q^2).                               (FQ8)

The integer q only clears coefficients; it need not be their least denominator.
The explicit positive rational u_s need not be dyadic unless q is a power of2.
The proof needs only a positive cutoff, not a dyadic search representation.
This is a new threshold for the sharpened FQ5 expense; it is NOT asserted to satisfy C844's older2^J inequality.

For all q>=2 the following elementary bounds hold:

    eta>=q^(-12),
    J_s=16q^8 B_s^5<=50q^18<=q^24,
    1+q/delta_s<=q^7,
    H_(J_s)<=1+24log q<=q^6,
    2J_s+1<=q^26,
    Lambda_(q^2,J_s)<=q^(13q^2+6).                    (FQ9)

Indeed B_s<=(5/4)q^2 makes eta>=(2/25)q^(-8)>=q^(-12) and16(5/4)^5<50.
The expression inside the ceiling defining J_s is the displayed integer16q^8 B_s^5, and50<=q^6.
The radial bound follows from1+2q^3 B_s<=q^7.
For the harmonic bound use H_J<=1+log J; the function q^6-1-24log q is positive at2 using log2<1 and is increasing for q>=2.
The last two estimates follow from q^2>=4 and the definition of Lambda, dropping the harmless divisor4 and negative subtractions when taking an upper bound.

First certify the domain directly:

    J_s u_s<=q^(24-256q^2)<=2^(-1000)<h0.

Thus FQ7 may now be used at u_s and J_s u_s.
It gives epsilon(J_s u_s)<=q^9 u_s^(1/8), and therefore

    Lambda_(q^2,J_s)epsilon(J_s u_s)
      <=q^(15-19q^2)<=q^(-14),
    (1+q/delta_s)u_s<=q^(7-256q^2)<=q^(-14),
    (1+q/delta_s)u_s+Lambda_(q^2,J_s)epsilon(J_s u_s)
      <=2q^(-14)<q^(-12)<=eta.                        (FQ10)

The separate zero guard is

    (q^2-1)epsilon(u_s)+2q^2 u_s
      <=q^(8-32q^2)+2q^(2-256q^2)
      <=3q^(-4)<=3/16<1.                              (FQ11)

All exponent comparisons hold for every q>=2, without a numerical search.

Let F be a NONZERO integer Laurent polynomial of coefficient energy at most q^2, and suppose F(alpha)/q is algebraically integral, including a possible zero value.
For a nonmonomial normalize its true span to T>0, put h=T*m/d and suppose h<=u_s.
Integer coefficients give true term count N<=q^2 and S_raw=||F||_1<=q^2.
C92 with effective support rho<=q^2 and FQ11 first excludes F(alpha)=0.
C844's field-free ER3 calculation, at the unchanged delta_s,B_s,J_s, supplies the actual normalized constant c_s<-2eta for f=F/q.
With delta_raw=q delta_s and B_raw=q^2 B_s, the raw majorant equals log q plus the normalized majorant and B_raw>=S_raw^2+delta_raw^2.
Equations FQ5--FQ6 and monotonicity in h and in N now give

    0<=c_s+(1+q/delta_s)u_s
                         +Lambda_(q^2,J_s)epsilon(J_s u_s)
      <-2eta+eta<0,

contradiction.
Thus every such nonmonomial satisfies T*m/d>u_s.
If F=a x^j has width0, multiplying its integral value by the algebraic-integer unit alpha^(-j) makes a/q a rational algebraic integer, hence an integer.
The energy bound and a!=0 force a=+/-q, with no use of epsilon(0).

Consequently C844's scalar and real-weight conclusions hold with the explicit u_s by this new proof.
Precisely, for ANY rational Laurent f with qf integral, NONZERO algebraic-integral value and OWN span T satisfying T*m/d<=u_s, energy is at least1, equality holds exactly for true signed monomials, and otherwise energy is at least1+1/q^2.
For energy at most1 apply the numerator conclusion to qf; for greater energy use that q^2 times the energy is an integer.
This removes any final term-count assumption, because the low-energy branch itself supplies the required count.
For a finite family sharing q, each with its own span bound and arbitrary positive REAL weights summing1, summation gives E>=1+mu/q^2, where mu is the weight on nonsigned monomials, and E=1 exactly when every atom is a true signed monomial.
No covariance, common union span, minimum weight or rational weight denominator is introduced.
For any supplied nonmonomial numerator of energy at most q^2 and integral value, including zero, the additional window T<=C*d gives m(P)>u_s/C in every original degree.

<a id="explicit-phase-cutoff-and-noncollision"></a>
### FQ6. The explicit phase threshold with unchanged separation or noncollision

For q>=2 retain the SAME eta and C845 phase parameters

    delta_p=delta_s*eta=1/(16q^6 B_s^3),
    B_p=4q^2+1,
    J_p=ceil(B_p/(eta*delta_p^2)),
    u_p(q)=q^(-512q^2).                               (FQ12)

Again u_p is an explicit positive rational, not necessarily dyadic, and is asserted for the new Fourier expense only.
The elementary parameter estimates are

    delta_p>q^(-17), B_p<=q^5, eta>=q^(-12),
    J_p<=q^52, 1+2q/delta_p<=q^20,
    H_(J_p)<=1+52log q<=q^7,
    2J_p+1<=q^54,
    Lambda_(2q^2,J_p)<=q^(54q^2+7).                   (FQ13)

For the first bound, delta_p>=(4/125)q^(-12)>q^(-17), since(4/125)q^5>=128/125>1.
Then B_p/(eta*delta_p^2)<q^51, so its ceiling is at most q^51+1<=q^52.
The radial estimate follows from1+2q^18<=q^20.
For the harmonic estimate, q^7-1-52log q is positive at2 and increasing for q>=2; the frequency and Lambda bounds follow as in FQ9.

The domain is certified before using FQ7:

    J_p u_p<=q^(52-512q^2)<=2^(-1996)<h0.

Now epsilon(J_p u_p)<=q^(25/2)u_p^(1/8)<=q^13 u_p^(1/8), and hence

    Lambda_(2q^2,J_p)epsilon(J_p u_p)
       <=q^(20-10q^2)<=q^(-20)<q^(-14),
    (1+2q/delta_p)u_p<=q^(20-512q^2)<q^(-14),
    (1+2q/delta_p)u_p+Lambda_(2q^2,J_p)epsilon(J_p u_p)
       <2q^(-14)<q^(-12)<=eta.                        (FQ14)

The separate zero guard is

    (2q^2-1)epsilon(u_p)+4q^2 u_p
       <=2q^(8-64q^2)+4q^(2-512q^2)
       <=6q^(-4)<=3/8<1.                              (FQ15)

Let H be any allowed C845 seed: H in Z[x], H(0)!=0, actual degree k>=0, coefficient energy at most q^2 and H different from the two constants +/-q.
Let sigma be either sign, n a positive integer and F_n=x^n H+sigma H* with the ACTUAL degree-k reversal.
Assume either n>kJ_p as in C845, or more generally n outside C848's support-defined Bad(H) for this unchanged J_p.
The true endpoints give T=n+k>0, N<=2q^2 and S_raw<=2q^2, even when the two support intervals overlap.
C845's field-free margin and the applicable exact finite specialization give the actual normalized circle constant c_p<-2eta.
No lifted Haar mean is used for that fact.

Suppose F_n(alpha)/q is algebraically integral, including zero, and h=T*m/d<=u_p.
C92 and FQ15 first exclude the zero value.
Use the complete signed norm FQ6 with delta_raw=q delta_p, B_raw=q^2 B_p and the actual F_n.
Since S_raw<=2q^2 and delta_p^2<1, these raw parameters satisfy B_raw>=S_raw^2+delta_raw^2.
The raw Y and majorant are the same normalized specialization as before; the raw majorant constant is log q+c_p, and its nonconstant coefficient sum is now bounded by Lambda_(N,J_p)<=Lambda_(2q^2,J_p).
Equation FQ5 and the FQ14 bounds therefore yield

    0<=c_p+(1+2q/delta_p)u_p
                         +Lambda_(2q^2,J_p)epsilon(J_p u_p)
      <-2eta+eta<0.                                  (FQ16)

Thus T*m/d>u_p, and a supplied original window T<=C*d gives m(P)>u_p/C in every degree.
This reproduces the changed arithmetic proof rather than invoking C845/C848 at their old cutoffs.
Their allowed constants, both signs, full algebraic integrality, all original embeddings and every radial/frequency/matrix expense remain.
C848's support set and count N_q=(4q^4)^(J_p), support-lattice sufficient condition and many-DISTINCT-integral-shift implication remain valid because J_p and the finite specialization are unchanged; their gap now uses u_p by FQ16.
The new coefficient price does not construct the required integral values or original window.

<a id="sharper-support-exception-count"></a>
### FQ6a. The same sum-zero count sharpens the exception bound

Retain the SAME support set A_H and the SAME J=J_p as in [C848](Yin_C_G0848_v1.md#phase-support-and-exceptional-shifts).
Label its N=2s DISTINCT points by v_1,...,v_N in Z^2, where s=|supp(H)|<=q^2.
Every point of W_J(H), being a sum of J differences v_i-v_j, has the form sum_i z_i v_i for integers z_i satisfying

    sum_i z_i=0,                 |z_i|<=J.

The first N-1 coordinates determine the last, so the number of such integer vectors is at most(2J+1)^(N-1).
Different vectors may give the same point of W_J, and some counted vectors may not be sums of J differences; both effects only lower the image cardinality.
Combining this count with C848's existing count gives

    |W_J(H)|<=min{(4s^2)^J,(2J+1)^(2s-1)},
    |Bad(H)|<=N'_q,
    N'_q=min{(4q^4)^J,(2J+1)^(2q^2-1)}.              (FQ17)

The finite set Bad(H) itself is unchanged, and this is not an assertion that it is minimal.
For more than N'_q DISTINCT supplied positive integral shifts of the same H, with the same original input and window n+k<=C*d and possibly varying signs, at least one shift is good.
The new FQ16 transfer then gives m(P)>u_p/C.
The same improved cardinality also works with C848's older cutoff and all its unchanged hypotheses, independently of the new Fourier estimate.
No exception set or numerical N'_q has been enumerated, and no supply of those shifts is inferred.

<a id="growing-denominator-budget-boundary"></a>
### FQ7. Varying denominator budgets and the exact limitation

For a fixed C>0, consider actual inputs with total m_j>0 tending to0, and supplied scalar or phase certificates satisfying all of the preceding respective energy, integrality, original-window and, in the phase case, separation/noncollision hypotheses.
The denominator q_j>=2 is allowed to vary, but each input uses its supplied coefficient-clearing integer and its own corresponding J and cutoff.
The proved bounds imply respectively

    log(1/m_j)<256q_j^2 log q_j+log C,
    log(1/m_j)<512q_j^2 log q_j+log C.                 (FQ18)

Therefore a family of such certificates with

    q_j^2 log q_j=o(log(1/m_j))                       (FQ19)

is impossible eventually, in either stated class.
Equivalently C*m_j is eventually at most its corresponding explicit u_s(q_j) or u_p(q_j), contradicting the original-span exclusion.
This is a conditional denominator-budget obstruction, not a positive gap uniform over arbitrary growing q and not automatic auxiliary coverage.
For the scalar version the certificate is a nonmonomial low-energy numerator, as in FQ5; a general high-energy scalar value is not such a certificate.

The contribution is an improved finite coefficient expense with the ACTUAL logarithmic constant untouched, together with explicit sufficient rational cutoffs, the sharper support-exception count and their exact conditional consequences.
The independent variables are an auxiliary coefficient estimate only, not a replacement probability law or mean for the original polynomial.
The matrix sizes2JT+1, actual windows, finite-specialization assumptions and inherited source-inspection limits remain.
No superiority to every older K0 bound, optimal exponent, numerical gap computation, practical enumeration, bounded-degree patch, unrestricted Lehmer conclusion or novelty claim is asserted.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision finite-fourier-budget-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T23:44 |
| status | open |
| reason | Fix the complete finite independent-variable coefficient budget and all explicit256/512 scalar/phase cutoff conclusions, retaining the actual mean and original arithmetic costs, zero/width0 branches, arbitrary-support scalar and own-span real-weight results, sharper support-exception count and conditional growing-denominator budgets. Fresh whole independent review and responsible adoption remain outstanding. No older2^J cutoff test, automatic certificate supply, source-proof expansion or unrestricted gap is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete coefficient-budget and cutoff statement](#statement) | Entire A--F: all real Laurent true-term counts, finite coefficient majorant and mean control, original integer-unit/norm/domain setting, explicit scalar/family/phase statements, every positive-rational/zero/width/window/sign/overlap branch, sharper Bad count and distinct-shift/growing-q consequences, with all costs and limits. |
| argument | [Complete FQ1--FQ7/FQ6a proof](#complete-argument) | All nineteen equations and unnumbered deductions: reuse, bounded variance/Parseval/sum-zero count and pullback, actual-mean countercontrol, changed raw C137 inequality, exact epsilon/domain constants, every256/512 inequality, C92 before the full norm, scalar/family and phase consequences, sharper exception count and growing-denominator argument. |
| dependency | [Actual finite logarithmic original-root certificate](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) | Sections1--2/equations1--7: actual finite majorant/tail/constant, original radial identities and matrix size, complete nonzero integral norm floor and old2^J coefficient bound for the optional minimum. The new Lambda expense replaces only the old coefficient-sum estimate. |
| dependency | [Scalar field-free finite negative margin](Yin_C_G0844_v1.md#uniform-energy-logarithmic-margin) | ER3 through ER7 only: actual integer low-energy extreme-lag variance, regularized scalar margin and finite Taylor constant below -2eta at unchanged delta_s/B_s/J_s. No use of the older arithmetic cutoff or its2^J test. |
| dependency | [Phase field-free margin and exact separated specialization](Yin_C_G0845_v1.md#statement) | Statement A and actual phase parameter definitions: every allowed seed including constants, both signs, finite normalized torus constant below -2eta and exact n>kJ_p specialization. No application of its arithmetic Statement B at a changed cutoff. |
| dependency | [Finite-support noncollision and original endpoint bounds](Yin_C_G0848_v1.md#statement) | Support data A_H/E_H/W_J/Bad, exact good-shift constant identity, old finite cardinality, all-positive-shift endpoint/term/length bounds and support-lattice criterion only. The changed cutoff and improved count are proved here, not inferred from its older arithmetic inequality. |
| dependency | [Short rational annihilator inequality](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Original-degree zero-value inequality at true positive span with effective support at most q^2 or2q^2, used before a norm logarithm under the explicitly checked positive domain. |
| dependency | [Exact original finite-frequency modulus](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact c0/h0/b/epsilon, positive domain, monotonicity/zero limit, negative frequencies and every original powered-field repetition; inherited Pri11/Dim19 source-inspection limits unchanged. |
| support | [Existing bounded-range l2 mechanism](Yin_C_G0168_v1.md#actual-cubic-l2-cost) | Exact prior variance-from-range proof, finite Parseval and coefficient Cauchy--Schwarz, with its actual growing circle-frequency count. Attribution for these elementary mechanisms; no Salem moment or projection theorem is imported. |
| support | [Existing frequency-dimension comparison](Yin_C_G0145_v1.md#statement) | Prior square-root frequency-dimension cost for a bounded-range finite approximation, distinguishing the new independent-variable count from the already known range/Parseval mechanism. No input-uniform certificate or new source theorem is borrowed. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T23:57 |
| status | proved |
| reason | Adopt the entire Statement A--F and FQ1--FQ7/FQ6a proof after root read the complete author argument, fixed statement and whole independent R1071. The independent-variable coefficient bound preserves the actual mean, all original norm/radial/frequency costs and zero guards; every all-q domain and strict inequality for the explicit256/512 rational cutoffs, scalar/real-weight/phase consequences, sharper Bad count and conditional growing-denominator budget is covered. The C168/C145 attribution remains distinct from their historical unknown review relationships, with the needed elementary mechanism rederived. No older2^J cutoff certification, automatic certificate availability, optimality or unrestricted Lehmer conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete coefficient-budget and cutoff statement](#statement) | Entire A--F: all real Laurent true-term counts, finite coefficient majorant and mean control, original integer-unit/norm/domain setting, explicit scalar/family/phase statements, every positive-rational/zero/width/window/sign/overlap branch, sharper Bad count and distinct-shift/growing-q consequences, with all costs and limits. |
| argument | [Complete FQ1--FQ7/FQ6a proof](#complete-argument) | All nineteen equations and unnumbered deductions: reuse, bounded variance/Parseval/sum-zero count and pullback, actual-mean countercontrol, changed raw C137 inequality, exact epsilon/domain constants, every256/512 inequality, C92 before the full norm, scalar/family and phase consequences, sharper exception count and growing-denominator argument. |
| dependency | [Actual finite logarithmic original-root certificate](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) | Sections1--2/equations1--7: actual finite majorant/tail/constant, original radial identities and matrix size, complete nonzero integral norm floor and old2^J coefficient bound for the optional minimum. The new Lambda expense replaces only the old coefficient-sum estimate. |
| dependency | [Scalar field-free finite negative margin](Yin_C_G0844_v1.md#uniform-energy-logarithmic-margin) | ER3 through ER7 only: actual integer low-energy extreme-lag variance, regularized scalar margin and finite Taylor constant below -2eta at unchanged delta_s/B_s/J_s. No use of the older arithmetic cutoff or its2^J test. |
| dependency | [Phase field-free margin and exact separated specialization](Yin_C_G0845_v1.md#statement) | Statement A and actual phase parameter definitions: every allowed seed including constants, both signs, finite normalized torus constant below -2eta and exact n>kJ_p specialization. No application of its arithmetic Statement B at a changed cutoff. |
| dependency | [Finite-support noncollision and original endpoint bounds](Yin_C_G0848_v1.md#statement) | Support data A_H/E_H/W_J/Bad, exact good-shift constant identity, old finite cardinality, all-positive-shift endpoint/term/length bounds and support-lattice criterion only. The changed cutoff and improved count are proved here, not inferred from its older arithmetic inequality. |
| dependency | [Short rational annihilator inequality](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Original-degree zero-value inequality at true positive span with effective support at most q^2 or2q^2, used before a norm logarithm under the explicitly checked positive domain. |
| dependency | [Exact original finite-frequency modulus](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact c0/h0/b/epsilon, positive domain, monotonicity/zero limit, negative frequencies and every original powered-field repetition; inherited Pri11/Dim19 source-inspection limits unchanged. |
| support | [Existing bounded-range l2 mechanism](Yin_C_G0168_v1.md#actual-cubic-l2-cost) | Exact prior variance-from-range proof, finite Parseval and coefficient Cauchy--Schwarz, with its actual growing circle-frequency count. Attribution for these elementary mechanisms; no Salem moment or projection theorem is imported. |
| support | [Existing frequency-dimension comparison](Yin_C_G0145_v1.md#statement) | Prior square-root frequency-dimension cost for a bounded-range finite approximation, distinguishing the new independent-variable count from the already known range/Parseval mechanism. No input-uniform certificate or new source theorem is borrowed. |
| review | [Whole independent Fourier-budget finding](../audits/reviews/Yin_R_G1071_v1.md#whole-finite-fourier-budget-finding) | Entire Statement A--F and FQ1--FQ19, all actual-mean/support/domain/norm/zero/width/sign/weight/window cases, explicit rational cutoffs and combinatorial/growing-q consequences, exact accepted inputs and historical attribution/source boundaries; independent arrangement without mutable Draft or substantive repair. |

