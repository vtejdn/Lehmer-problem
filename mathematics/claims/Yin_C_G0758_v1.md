---
author: Yin
---

# First-four canonical precision and cyclotomic trace multiplicity bounds

Human author Yin.
The [selected G0001 continuation](../tasks/Yin_T_G0001_v1.md#decision-resume-after-account-handoff-2026-10-25) authorizes this work.
Provenance: project deduction from actual canonical integer identities, full cyclotomic trace factors and the precisely scoped accepted local and Mahler sources below.
Root proposed the general E>6A domain, unique weight E-A, actual same-binary quotient model, unequal local residual valuations and full remaining-degree consequences, and first identified the C754 family evaluation.
Earlier_bit_obstruction checked every Delta cancellation and integer-model step, generic prime-order/unit range, exact canonical evaluation and coefficient inference, derived the necessary root-difference lemma from the accepted primitive-product/value-at-one source, and checked all full-part endpoints and family quantifiers.
Root read the complete family and generic author arguments and the precise Bel17/The26b source interfaces.
Both are contributors, not independent reviewers.
The [D5 generic development](../drafts/Yin_D_G0005.md#general-first-four-cyclotomic-trace-bound) and [initial family calculation](../drafts/Yin_D_G0005.md#cyclotomic-family-exact-first-bit-valuation) are provenance only.
The entire necessary argument is fixed here: GF1 states the main theorem; the complete FV2 root-difference lemma precedes GF2--GF6; GF15 retains all C754 family conclusions as a specialization of the generic proof.
The separate family-only proof is not required as a mutable input or duplicated here.
This complete author theorem is initially open for fresh independent whole review.

## Statement

### GF1. Precise generic statement and retained source scope

Let T be ANY monic integer polynomial with

    U=Tbar=X^A Y phi^E,
    A>=1, E>6A integers, phi=X^2+X+1,
    Y monic in F_2[X], gcd(Y,Xphi)=1.           (GF1)

There is no global forward-divisibility hypothesis on Y and no normalized K or prescribed construction of T.
Fix either epsilon in{1,-1} and use the integer trace polynomials and OWN actual canonical remainders

    C_0=2, C_1=X, C_(n+1)=X C_n-C_(n-1),
    C_2=X^2-2, C_3=X^3-3X,
    C_5=X^5-5X^3+5X,
    a_T=rem_T T(C_2)/2, b_T=rem_T T(C_3)/3,
    c_T=rem_T T(C_5)/5,
    F_T=rem_T(2c_T^2-3a_T^5),
    G_T=rem_T(c_T^3-2b_T^5),
    X_epsilon=rem_T(b_T^2-a_T^3+epsilon(c_T^3-2b_T^5)).

All prime divisions are performed on actual integer coefficients before any reduction, as in C736.
The coefficient valuation v_2(F_T) is the minimum valuation of its nonzero integer coefficients, with value+infinity for the zero polynomial.
Assume X_epsilon is coefficientwise even.
For a monic integer trace factor J of T, write P_J(z)=z^(degJ)J(z+z^(-1)).
If P_J is completely cyclotomic and E_c=ord_phi Jbar>A, then necessarily

    w=E-A is a power of2, w>5A, w>=8,
    V_w=F_(10w)=g(C_w) divides T EXACTLY ONCE,
    g=X^2-X-1,
    D=T/V_w is monic integral,
    Dbar=X^A Y phi^A.                          (GF2)

Here F_n is the full integer primitive-order trace factor, not the canonical residual F_T.
At ANY primitive10w trace theta=zeta+zeta^(-1) and ANY normalized dyadic place of Q(zeta), v(2)=1, one has

    v(a_T(theta))=v(c_T(theta))=2A/w,
    b_T(theta)=0,
    v(F_T(theta))=min(1+4A/w,10A/w)<2.          (GF3)

The two arguments of this minimum are unequal because equality would require w=6A, impossible for a power of2 and a positive integer A.
Therefore F_T is not coefficientwise divisible by4 whenever such a J exists.
If F_T is additionally even, its coefficient valuation is exactly1.

Consequently, under the stronger actual assumption F_T=0 modulo4, EVERY cyclotomic trace factor J of T satisfies

    ord_phi Jbar<=A.

The FULL noncyclotomic reciprocal part of P_T then has degree at least4(E-A), counting all factors and multiplicities, and m(P_T)>0.
This is a total remaining-degree statement, not a per-factor bound or a residual-inheritance assertion.
It applies only to genuine integer trace factors J; arbitrary partial reciprocal cyclotomic divisors need not have the required even endpoint multiplicities.

For the adopted C754 family, the same generic result gives exact coefficient valuation v_2(F_T)=1 for EVERY permitted Y and integer lift and EVERY dyadic q>=2, with exact root value5/4 at every primitive160q trace and every normalized dyadic place.
The detailed specialization and its preserved unit/evaluation scope are stated in GF6.

The local reuse search inspected C199v3 DL1--DL3 and C266's retained primitive-layer scope.
Those statements start from a NONTORSION algebraic unit and retain its finite layers; they are not applied to the torsion roots in this argument.
The exact root-difference lemma FV2 is used at all r>=1, with its accepted [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001) primitive-product/value-at-one input and geometric-unit proof.
The precise source facts are the complete primitive-root product on printed p3 and Theorem9 on p8 giving Phi_(2^r)(1)=2; the value-at-one subargument was inspected completely in that source unit.
No new reading of the original PDF or an unquoted local ramification theorem is asserted here.
The valuation conventions remain the recorded [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) scope; no ambient ramification index is assumed.
The complete integer trace and dyadic factor identities are [C752 CY3--CY4/CY7](Yin_C_G0752_v1.md#decision-whole-reviewed-2026-10-25), and the exact integer canonical product interface is [C736](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25).
Strict Mahler positivity uses precisely the accepted product-form Kronecker statement in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), preserving its source-inspection limits and asserting no quantitative lower bound.

## Complete argument

### FV2. Primitive dyadic root difference without an assumed ramification index

Fix any number field containing a primitive2^r root eta, r>=1, and any normalized additive valuation v above2 with v(2)=1.
Every root of unity is an algebraic unit.
The residue of eta is1 because X^(2^r)-1=(X-1)^(2^r) in characteristic2.
For every odd j with1<=j<2^r,

    (1-eta^j)/(1-eta)=1+eta+...+eta^(j-1)

is an algebraic integer with residue j=1, hence a local unit.
All the factors1-eta^j therefore have the same finite valuation.
The exact primitive-root factorization and the accepted prime-power value at1 give

    2=Phi_(2^r)(1)=product_(1<=j<2^r,j odd)(1-eta^j).

There are2^(r-1) factors, so additivity of the valuation proves

    v(1-eta)=1/2^(r-1).                        (FV2)

This proof also includes r=1 and is independent of the selected prime above2.
It neither assumes nor calculates the full ramification index of the ambient field.

### GF2. The required local dyadic order without full forward stability

Work only in the full binary phi^E component of F_2[X]/U, writing alpha,beta,gamma for the actual reductions of a_T,b_T,c_T.
The integer odd divisions precede reduction, so

    beta=[U(lambda)]=0, lambda=X^3+X,
    gamma=[U(chi)]
         =[phi^(2A)X^A Y(chi)phi(chi)^E],
    chi=Xphi^2.                                (GF4)

For beta, phi(lambda)=phi*(X^4+X^3+1) has exact phi-order1, and lambda modulo phi equals X+1, which permutes the two phi roots.
Thus lambda and Y(lambda) are units at phi and the displayed U(lambda) is divisible by phi^E.
This is a LOCAL zero only; no global beta zero or Y|Y(lambda) is asserted.
For gamma, chi=0 modulo phi and Y(0)=1, so every factor after phi^(2A) is a phi-unit.
Hence gamma has exact order2A, and gamma^3 has exact order6A<E.
The even second residual gives alpha^3=gamma^3 modulo phi^E for either sign.
Writing a nonzero class as a power of phi times a unit proves

    ord_phi alpha=2A.                          (GF5)

This is also why the strict premise E>6A is retained.

### GF3. Actual cyclotomic factor expansion and the unique possible weight

Let J be as in GF1 with E_c>A, and write T=J R over Z.
Then E_r=ord_phi Rbar=E-E_c and Rbar=phi^(E_r)r_0 with r_0 a phi-unit.
Use the complete C752 trace classification to write

    J=J_5 Q,
    J_5=f^(m_0) product_(b>=1)V_b^(m_b),
    f=X^2+X-1,
    V_b=F_(2^b*5)=g(C_(lambda_b)),
    lambda_b=2^(b-1),
    J_5bar=phi^(E_c), Qbar a phi-unit,
    E_c=m_0+sum_(b>=1)m_b lambda_b.             (GF6)

All m_b are their actual nonnegative integer multiplicities, and every factor at every other order, including the endpoints, remains in Q.
The actual integer Delta product rule reduces to the full identity

    Delta(J)bar=Qbar^2 [
       (m_0 mod2)phi^(2(E_c-1))Delta(f)bar
       +sum_(b>=1,m_b odd)
              phi^(2(E_c-lambda_b))Delta(V_b)bar]
                              +phi^(2E_c)Delta(Q)bar.

Here Delta(f)bar has exact phi-order1, whereas every Delta(V_b)bar is a phi-unit, by the actual divided-remainder identities in C752 CY9.
In

    Delta(T)bar=Rbar^2 Delta(J)bar
                                   +Jbar^2 Delta(R)bar,

the first summand's f term has order2E-1 when present, its Delta(Q) term has order at least2E, and the odd m_b terms have exact orders2E-2lambda_b.
The second complete summand has order at least2E_c>2A.
If no odd m_b with b>=1 occurs, both summands have order greater than2A, contradicting GF5.
Otherwise let w be the largest lambda_b with m_b odd.
The weights are distinct powers of2, so its term is uniquely lowest in the first summand, of exact order2E-2w.
It lies below the f and Delta(Q) orders and cannot cancel with another term of that first summand.

If w<E-A, both complete summands have order greater than2A, again impossible.
If w>E-A, its first-summand order is below2A; but E_c>=w and w>E-A>E/2, so the second summand has order at least2w>2E-2w and cannot cancel it.
Only w=E-A remains.
Reduction by the actual T cannot create or remove the resulting term at order2A or a uniquely lower order, since these are strictly below E.
Thus w is a power of2 and w=E-A>5A, implying w>=8.
The corresponding factor is V_w=g(C_w)=F_(10w), and it occurs in J.
Because E<2w, it can occur only once in T: a second copy would force phi^(2w)|U.
Monic integer division by this actual factor now gives D=T/V_w and

    Dbar=U/phi^w=X^A Y phi^A,                 (GF7)

proving every algebraic assertion in GF2 without a coprimality assumption.

### GF4. A legitimate integer model for both quotient evaluations

Choose ANY monic integer lift Y_tilde of Y, put Phi=X^2+X+1 and form the integer polynomial

    M=X^A Y_tilde Phi^A.

Equation GF7 gives an ACTUAL identity

    D=M+2H, H in Z[X].                        (GF8)

Let zeta be any primitive10w root, theta=zeta+zeta^(-1), and take any prime of K=Q(zeta) over2 with normalized v(2)=1.
Write10w=5*2^s with s=1+log_2 w>=4.
The reduction of zeta has exact order5, so theta_bar and C_2(theta)_bar are roots of phi; in particular both are units.
The factor1-C_w(theta) is a unit because its residue is1+theta_bar^w and w is a power of2, while theta_bar has order3.
Y_tilde(C_2(theta)) is a unit because Y is prime to phi.

Using the exact trace identity z^2 f(z+z^(-1))=Phi_5(z), one has

    f(C_2(theta))=(zeta^10-1)/(zeta^4(zeta^2-1)),
    v(f(C_2(theta)))=2/w.

Indeed zeta^10 is primitive w and the denominator is a unit.
Since Phi=f+2 and2/w<1, unequal valuations give v(Phi(C_2(theta)))=2/w.
Thus

    v(M(C_2(theta)))=2A/w<1.                 (GF9)

For the fifth value let xi=zeta^5, primitive2w=2^s.
The root -xi^2 is primitive w: its exponent relative to xi^2 is1+w/2, which is odd because w>=8.
The root-difference lemma FV2 applies and gives

    C_5(theta)=(xi^2+1)/xi,
    v(C_5(theta))=2/w.

This value has residue0, so Y_tilde(C_5(theta)) and Phi(C_5(theta)) both have residue1 and are units.
Consequently

    v(M(C_5(theta)))=2A/w<1.                 (GF10)

These calculations use s>=4, not the narrower s>=6 domain of the preceding C754-only evaluation.
Both C_2(theta) and C_5(theta) are algebraic integers, hence v(2H(C_i(theta)))>=1 for i=2,5.
The actual error in GF8 therefore cannot cancel or change either value below1 in GF9--GF10.
We obtain

    v(D(C_2(theta)))=v(D(C_5(theta)))=2A/w.    (GF11)

No high coefficient of D, chosen root lift, factorization of Y_tilde or local class composition has been assumed beyond its actual binary reduction.

### GF5. Actual canonical evaluations and the coefficient-four obstruction

The actual integer divided-remainder identity of V_w is

    V_w(C_2)=V_w Q_2(V_w)+2(1-C_w).

Using T=D V_w and V_w(theta)=0 in the ACTUAL canonical identities gives

    a_T(theta)=D(C_2(theta))*(1-C_w(theta)).

For the odd maps, put rho=zeta^w, a primitive10 root.
The trace polynomials commute and C_5(C_w(theta))=-2, so

    V_w(C_5(theta))=g(-2)=5,
    c_T(theta)=D(C_5(theta)).

Also g(C_3)=g*(X^4+X^3-4X^2-4X+1) over Z; composition by C_w therefore gives V_w(C_3(theta))=0 and b_T(theta)=0.
All divisions by2,3,5 in these evaluations come from the actual integer defining identities, before reduction or evaluation; no residual quotient is substituted for a canonical value.
Together with GF11 and the unit1-C_w(theta), these formulas prove

    v(a_T(theta))=v(c_T(theta))=2A/w,
    b_T(theta)=0.                             (GF12)

The actual F_T quotient vanishes on evaluation at theta, so the two terms in its value have valuations1+4A/w and10A/w.
They are unequal, since equality would force w=6A, which has a factor3 and is not a power of2.
Both are below2 because w>5A.
Thus

    v(F_T(theta))=min(1+4A/w,10A/w)<2.          (GF13)

If F_T=4H_F for an integer polynomial H_F, its value at the algebraic integer theta would have valuation at least2, a contradiction.
This proves the generic obstruction without presuming that F_T is even.
When F_T is even as an additional hypothesis, it is therefore even but not divisible by4, with exact coefficient valuation1.

<a id="gf6-full-remaining-factor-positivity-and-the-c794-corollary"></a>
### GF6. Full remaining factor, positivity and the C754 corollary

If F_T is divisible by4 and X_epsilon is even in the GF1 domain, GF13 rules out every cyclotomic trace factor J with E_c>A.
Take the FULL cyclotomic part P_cyc of P_T, retaining the entire multiplicity of each cyclotomic factor.
All multiplicities at z=1 and z=-1 are even because P_T is a trace lift; the complete P_cyc includes those entire endpoint factors.
The exact C752 endpoint and symmetric-Laurent argument therefore gives a monic integer J with P_J=P_cyc and a monic integer R with T=J R and P_R=P_T/P_cyc.
This is a genuine trace factor in the proved domain, so ord_phi Jbar<=A and

    ord_phi Rbar>=E-A,
    degR>=2(E-A),
    deg(P_T/P_cyc)=2degR>=4(E-A).              (GF14)

Every remaining reciprocal irreducible factor is noncyclotomic by the definition of the FULL removed part; the bound retains their total degrees and multiplicities.
An arbitrary smaller reciprocal cyclotomic divisor need not have even endpoint multiplicities and is not silently substituted for P_cyc.
Since E>A, the remaining part is nonconstant.
The monic P_T has constant coefficient1; the accepted Kronecker characterization implies m(P_T)>0 because it is not completely cyclotomic.
Neither the degree bound nor positivity gives a uniform Mahler gap or an inherited residual congruence for the remaining factor.

For C754, A=2q, E=18q and J=T_q is itself a completely cyclotomic trace input.
Writing its actual polynomial as T_q=B^q V_q with B=X^2f^2 mathcal_Y, the required weight is w=E-A=16q and the actual quotient D in GF7 is B^q.
For EVERY permitted Y and its unchanged integer lift, EVERY dyadic q=2^k>=2, EVERY primitive160q root zeta and EVERY prime of Q(zeta) over2 with v(2)=1, GF4--GF5 give

    theta=zeta+zeta^(-1),
    a_T(theta)=B(C_2(theta))^q*(1-C_(16q)(theta)),
    c_T(theta)=B(C_5(theta))^q, b_T(theta)=0,
    v(B(C_2(theta)))=v(B(C_5(theta)))=1/(4q),
    v(a_T(theta))=v(c_T(theta))=1/4,
    v(F_T(theta))=min(3/2,5/4)=5/4,
    v_2(F_T)=1.                               (GF15)

The last coefficient conclusion uses C754's actual F_T evenness and the general coefficient-four obstruction.
The direct family unit checks are included in GF4 at w=16q: theta and C_2(theta), 1-C_(16q)(theta) and mathcal_Y(C_2(theta)) are units; C_5(theta) has valuation2/w, while f(C_5(theta)) and mathcal_Y(C_5(theta)) are units.
Here10w=5*2^s has s=k+5>=6, a special case of the generic s>=4 range; the primitive-root and signed-root checks therefore cover every endpoint of the family.
Thus the generic proof covers all the actual family valuation conclusions without an additional family-only proof or an inference of higher precision from q.
It excludes completely cyclotomic inputs with F modulo4 and X modulo2 in this E>6A profile, but does not exclude all possible binary profiles or solve the unrestricted higher-precision cyclotomic question.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision first-four-cyclotomic-multiplicity-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T22:35 |
| status | open |
| reason | Register the complete GF1--GF6 theorem with the full internal FV2 root-difference proof and C754 specialization GF15. For arbitrary monic integer T with Tbar=X^A Y phi^E, A>=1, E>6A, Y prime to Xphi and own X_epsilon even, any cyclotomic integer trace factor with phi-multiplicity greater than A forces the unique dyadic weight w=E-A>5A and an actual single factor F_(10w). The genuine remaining integer quotient and its binary model give all normalized local a/b/c values and exact vF=min(1+4A/w,10A/w)<2, with no tie. Hence F divisible by4 forces every such trace multiplicity<=A, full noncyclotomic reciprocal degree>=4(E-A) and strict positive Mahler measure; if F is only even while the large factor exists, its coefficient valuation is exactly1. No global Y-forward hypothesis or normalized K is needed. The primitive-root difference is proved from the accepted complete product/Phi_(2^r)(1)=2 source, including r1, without an assumed ambient ramification index. The family corollary retains every C754 source/lift/q/root/place quantifier and exact value5/4, proving its F is always even but not divisible by4. Root and Earlier_bit_obstruction are contributors; fresh independent whole review remains outstanding. Nontorsion layer inputs are not applied to torsion. No arbitrary partial reciprocal-divisor trace assumption, individual-factor degree/precision inheritance, quantitative Mahler gap, general exclusion of all cyclotomic high-precision profiles, compatible characteristic-zero realization or unrestricted Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete generic and family statements](#statement) | GF1--GF3, included GF14--GF15: minimal arbitrary-T binary domain, either second sign, every integer cyclotomic trace factor, forced single dyadic factor and actual quotient, all primitive-root/dyadic-place exact evaluations, F4 obstruction and conditional exact coefficient valuation1, full remaining reciprocal degree and positivity, all C754 family choices and limits. |
| argument | [Complete local lemma, generic proof and specialization](#complete-argument) | Entire internal FV2 and GF2--GF6/GF4--GF15: geometric-unit primitive-root valuation including r1, phi-local beta/gamma without forward assumptions, full exact Delta expansion and unique-weight cases, same-binary integer model with error2H and generic s>=4, actual canonical quotients and unequal residual terms, coefficient inference, complete cyclotomic endpoint trace lift and degree, and family specialization with all unit/root/place quantifiers. |
| dependency | [Adopted actual integer canonical interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT1--FT4 actual monic prime-divisible remainders, integral Delta and exact product identity for arbitrary monic integer factors including shared multiplicities. No factor precision inheritance or modular division by2 is assumed. |
| dependency | [Adopted full cyclotomic trace and factor identities](Yin_C_G0752_v1.md#decision-whole-reviewed-2026-10-25) | CY3--CY4 and CY7 exact complete integer trace decomposition, endpoint multiplicities, V_b=g(C_(lambda_b)), actual dyadic divided remainders and Delta orders, and full-part symmetric-Laurent mechanism. GF2--GF6 prove all arbitrary-E extensions anew; C752's E=7A residual/degree conclusion is not formally rescaled or applied outside its domain. |
| dependency | [Accepted primitive-root product and prime-power value at one](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Printed p3 cyclotomic definition/factorization and p8 Theorem9 Phi_(2^r)(1)=2, with its completely inspected value-at-one subargument. FV2 supplies the full local geometric-unit deduction for every r>=1 and every normalized dyadic prime. No new PDF reading, quoted ramification theorem or broader source-proof audit is asserted. |
| dependency | [Accepted normalized local valuation convention](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Actual number-field prime/DVR normalization v=ord_p/e_p, v(2)=1 and nonnegative values on algebraic integers, including ramified primes. No unramifiedness, field-degree substitution, Frobenius lift, norm sum or assumed cyclotomic ramification degree enters the proof. Preserve the U's ancestor-proof inspection limits. |
| dependency | [Accepted product-form measure-one characterization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Height-normalization section, printed p322: a measure-one integer polynomial is a monomial times a product of cyclotomic polynomials with multiplicities. Applied to monic P_T with constant1 after the full remaining-part result, yielding strict positivity only; no quantitative lower bound or new source-proof inspection. |
| dependency | [Adopted actual cyclotomic first-bit family](Yin_C_G0754_v1.md#decision-whole-reviewed-2026-10-25) | OC1--OC6 actual T_q=(X^2 f^2 mathcal_Y)^q g(C_(16q)), all permitted complete source/lift choices, dyadic q>=2, binary profile, own X even and especially actual F coefficientwise even. Used only for GF15's exact valuation-one family corollary; generic GF1--GF14 has no C754 source-existence or forward-divisibility premise. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T22:46 |
| status | proved |
| reason | Adopt the complete GF1--GF6 theorem with the full internal FV2 root-difference proof and C754 specialization GF15. For arbitrary monic integer T with Tbar=X^A Y phi^E, A>=1, E>6A, Y prime to Xphi and own X_epsilon even, any cyclotomic integer trace factor with phi-multiplicity greater than A forces the unique dyadic weight w=E-A>5A and an actual single factor F_(10w). The genuine remaining integer quotient and its binary model give all normalized local a/b/c values and exact vF=min(1+4A/w,10A/w)<2, with no tie. Hence F divisible by4 forces every such trace multiplicity<=A, full noncyclotomic reciprocal degree>=4(E-A) and strict positive Mahler measure; if F is only even while the large factor exists, its coefficient valuation is exactly1. No global Y-forward hypothesis or normalized K is needed. The primitive-root difference is proved from the accepted complete product/Phi_(2^r)(1)=2 source, including r1, without an assumed ambient ramification index. The family corollary retains every C754 source/lift/q/root/place quantifier and exact value5/4, proving its F is always even but not divisible by4. Root and Earlier_bit_obstruction are contributors. Fresh independent whole R978 passed the entire fixed statement, complete FV2/GF argument, every family and generic endpoint, full factors and all precise accepted-input scopes without substantive repair; adopt on that separately recorded finding. Nontorsion layer inputs are not applied to torsion. No arbitrary partial reciprocal-divisor trace assumption, individual-factor degree/precision inheritance, quantitative Mahler gap, general exclusion of all cyclotomic high-precision profiles, compatible characteristic-zero realization or unrestricted Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete generic and family statements](#statement) | GF1--GF3, included GF14--GF15: minimal arbitrary-T binary domain, either second sign, every integer cyclotomic trace factor, forced single dyadic factor and actual quotient, all primitive-root/dyadic-place exact evaluations, F4 obstruction and conditional exact coefficient valuation1, full remaining reciprocal degree and positivity, all C754 family choices and limits. |
| argument | [Complete local lemma, generic proof and specialization](#complete-argument) | Entire internal FV2 and GF2--GF6/GF4--GF15: geometric-unit primitive-root valuation including r1, phi-local beta/gamma without forward assumptions, full exact Delta expansion and unique-weight cases, same-binary integer model with error2H and generic s>=4, actual canonical quotients and unequal residual terms, coefficient inference, complete cyclotomic endpoint trace lift and degree, and family specialization with all unit/root/place quantifiers. |
| dependency | [Adopted actual integer canonical interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT1--FT4 actual monic prime-divisible remainders, integral Delta and exact product identity for arbitrary monic integer factors including shared multiplicities. No factor precision inheritance or modular division by2 is assumed. |
| dependency | [Adopted full cyclotomic trace and factor identities](Yin_C_G0752_v1.md#decision-whole-reviewed-2026-10-25) | CY3--CY4 and CY7 exact complete integer trace decomposition, endpoint multiplicities, V_b=g(C_(lambda_b)), actual dyadic divided remainders and Delta orders, and full-part symmetric-Laurent mechanism. GF2--GF6 prove all arbitrary-E extensions anew; C752's E=7A residual/degree conclusion is not formally rescaled or applied outside its domain. |
| dependency | [Accepted primitive-root product and prime-power value at one](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Printed p3 cyclotomic definition/factorization and p8 Theorem9 Phi_(2^r)(1)=2, with its completely inspected value-at-one subargument. FV2 supplies the full local geometric-unit deduction for every r>=1 and every normalized dyadic prime. No new PDF reading, quoted ramification theorem or broader source-proof audit is asserted. |
| dependency | [Accepted normalized local valuation convention](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Actual number-field prime/DVR normalization v=ord_p/e_p, v(2)=1 and nonnegative values on algebraic integers, including ramified primes. No unramifiedness, field-degree substitution, Frobenius lift, norm sum or assumed cyclotomic ramification degree enters the proof. Preserve the U's ancestor-proof inspection limits. |
| dependency | [Accepted product-form measure-one characterization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Height-normalization section, printed p322: a measure-one integer polynomial is a monomial times a product of cyclotomic polynomials with multiplicities. Applied to monic P_T with constant1 after the full remaining-part result, yielding strict positivity only; no quantitative lower bound or new source-proof inspection. |
| dependency | [Adopted actual cyclotomic first-bit family](Yin_C_G0754_v1.md#decision-whole-reviewed-2026-10-25) | OC1--OC6 actual T_q=(X^2 f^2 mathcal_Y)^q g(C_(16q)), all permitted complete source/lift choices, dyadic q>=2, binary profile, own X even and especially actual F coefficientwise even. Used only for GF15's exact valuation-one family corollary; generic GF1--GF14 has no C754 source-existence or forward-divisibility premise. |
| review | [Fresh independent whole first-four finding](../audits/reviews/Yin_R_G0978_v1.md#whole-first-four-cyclotomic-finding) | Entire fixed GF1, internal FV2 and GF2--GF6/GF2--GF15, every local/full-factor/endpoint/family conclusion and exact source scope. No quantitative gap, arbitrary-profile exclusion or Task completion. |

