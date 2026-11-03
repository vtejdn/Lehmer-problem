---
author: Yin
---
# Actual cyclotomic unit gates and canonical Frobenius constraints

Date: 2026-10-20T16:25.
Human author Yin.
This substantive v3 continues the same actual zero-Haar canonical-residual inquiry as [adopted v2](Yin_C_G0199_v2.md#decision-whole-reviewed-2026-10-20), while stating the broader no-zero-Haar domain of the new unique-unsaturated parity consequence separately.
The complete physical [v1](Yin_C_G0199_v1.md#argument) and [v2](Yin_C_G0199_v2.md#argument), their exact decisions and the actual [R481](../audits/reviews/Yin_R_G0481_v1.md#zero-haar-odd-order-consumer-whole-finding) and [R483](../audits/reviews/Yin_R_G0483_v1.md#joint-order-cancellation-consumer-whole-finding) reviews remain unchanged.
KC1--KC9, JT1--JT15 and CC1--CC8 are reused through that fixed v2; they are not copied or silently re-reviewed here.
This version contains the complete new CC9, DL1--DL13, UJ1--UJ20, UR1--UR12 and UP1--UP11 arguments.
Their original author dates and local contribution accounts are retained in their respective sections.

Root and draft_inventory_later contributed CC9, DL/UJ and UP.
Root and entropy_attainment_bridge contributed UR; its exact relation to their upstream C197 work is explicitly retained.
The order-31 formal comparison was developed by entropy_attainment_bridge and is fully reproduced at the needed scope in UJ; its fixed L440 home is a comparison/provenance link, not a premise supplying a missing argument.
The draft_inventory_later agent assembled this version and checked the extraction interfaces, without claiming an independent review of contributor-overlapping work.
No new source acquisition, mathematical program, order enumeration, original-input construction or adoption occurs in this version.

<a id="statement"></a>
## Exact theorem statement with distinct hypothesis domains

### Common actual residual domain

Let P in Z[z] be monic irreducible reciprocal nontorsion, with constant coefficient1 and degree d=2r.
For a root alpha set K=Q(alpha), delta=alpha+alpha^(-1), and assume that the actual trace field F=Q(delta) is totally real.
Let T in Z[X] be its monic degree-r minimal polynomial, so P(z)=z^r T(z+z^(-1)) and [K:F]=2.
Use C_p(z+z^(-1))=z^p+z^(-p) and the ACTUAL divided monic remainders

    theta_p=rem_T(T(C_p))/p in Z[X], p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta),
    a,b,c nonzero algebraic integers in F,
    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0, s in{1,-1},
    g=c^3-2b^5!=0.

Put G=rem_T(theta_5^3-2theta_3^5), w=deg G<r, U=T mod2 and R=G mod2.
Let I_can be the integral of log(G(z+z^(-1))^2) against normalized circle Haar probability, with the integrable-log convention at circle zeros.
In the following conclusions the common domain alone does NOT include I_can=0.
An irreducible factor psi of U is unsaturated when ord_psi R<ord_psi U; the zero R has infinite orders and has no unsaturated factor.
Write Phi=X^2+X+1 in Z[X], phi=Phi mod2 and chi=C5 mod2=X phi^2.

### A. All-degree parity in the unique-unsaturated class, without zero Haar

Suppose phi is the ONLY unsaturated factor of U.
Then R!=0 and C197 gives the complete support

    U=X^A phi^(7A) product_i Q_i^(B_i),
    A>=2, B_i>=2, ord_phi R=6A,

where the Q_i are all distinct remaining monic irreducibles, different from X and phi.
Let k=min{v_2(A),v_2(B_i) for all i}, taking k=v_2(A) for an empty product, and put A_0=A/2^k, B_i0=B_i/2^k and U=U_0^(2^k).
The exact canonical remainder satisfies

    R=R_0^(2^k),
    R_0=rem_(U_0)(U_0(chi)^3)!=0,
    R_0 is not a square in F_2[X].

Equivalently R_0'!=0, and the maximal common Frobenius power of R is exactly2^k, the same as that of U.
The inherited C197 conditions are A_0 even and deg W_U>=2A_0+1 for W_U=product_(B_i0 odd)Q_i.
The proof charges every saturated factor, every extra factor of R and the exact2A_0 degree deficit at phi.
It allows reduction degree drop and places no bound on w, r or m(P).
It does not cover additional unsaturated factors or assert existence or nonexistence of this actual class.

### B. Prior zero-Haar theorem and the same-target refinement

For this part and Parts D--F additionally assume I_can=0.
All conclusions of the [exact v2 statement](Yin_C_G0199_v2.md#statement) remain in force, including the complete product

    H(z)=epsilon z^w G(z+z^(-1))
        =product_m Phi_m(z)^(a_m),
    epsilon=lc(G) in{1,-1}, w>=1,
    sum_m a_m phi(m)=2w<d,
    R!=0, deg R=w.

All a_m are retained, a_1 and a_2 are even, and phi(m) in this display denotes Euler's totient.
For each odd part n, set E_n=sum_b a_(2^b n)lambda_b, with lambda_0=1 and lambda_b=2^(b-1) for b>=1.
Its uniform reduced trace multiplicity is nu_n=E_n for n>1 and nu_1=E_1/2.
The full original weighted expense remains

    sum_m a_m log|Res(P,Phi_m)|
       =2log|Norm_F(g)| >=(6d/11)log2.

In the coprime-to-5 case, the necessary large-source witness of v2 must additionally satisfy

    3 not congruent to +/-5*2^j modulo n
                                  for every j>=0.

More precisely, if gcd(n,15)=1 and 3 is congruent to +/-5*2^j modulo n for some j, C3 and C5 induce the same permutation of the order-n irreducible trace factors.
A source with N_psi>5nu_n/3 would require the same target to have both multiplicities nu_n/3 and nu_n/2, which is impossible.
This refines the existing witness, without excluding the remaining cross-order cases or constructing an actual residual input.

### C. Exact local cyclotomic layers in their broader classical domain

The following preliminary applies to ANY nontorsion algebraic unit alpha and actual completion K_q of K=Q(alpha) at2, independently of zero Haar or the residual equations.
Normalize v=ord_q/e_q so v(2)=1, let n be the exact odd order of the residue of alpha, and let omega in K_q be the unique n-th root of unity with that residue.
Put u=alpha/omega and L_j=v(u^(2^j)-1)>0.
All L_j are finite, and

    v(Phi_m(alpha))=0 unless oddpart(m)=n;
    v(Phi_n(alpha))=L_0;
    v(Phi_(2^b n)(alpha))=L_b-L_(b-1), b>=1.

For y=u^(2^j), L=L_j, the latter increment is v(y+1):
it is L if L<1, it is1 if L>1, and at L=1 it is exactly1+v(1+(y-1)/2)>=1, with the actual possible cancellation retained.
Thus a layer with lambda_b L_0<1 has value lambda_b L_0.
In the common reciprocal domain the C191 periodic trace lift is eta=omega+omega^(-1), and v(delta-eta)=L_0 for n>1 and2L_0 for n=1.
No replacement local field or maximal residue-field assumption is made.

For the common residual domain with I_can=0, these values give the exact original comparison

    v(g)=sum_b a_(2^b n)(L_b-L_(b-1))
         =3v(c)=(3/2)(5v(a)-1),

where the b=0 summand means a_n L_0.
Every other odd-order factor is still present as a unit.
The full original weights satisfy

    v_2|Norm_F(g)|=sum_(p|2)e_p f_p v_p(g),
    v_2|Norm_K(g)|=2sum_(p|2)e_p f_p v_p(g),
    |Res(P,H)|=|Norm_F(g)|^2.

### D. Quadratic-branch value match and the complete finite unit gate

In the zero-Haar domain suppose phi is unsaturated, with no requirement that it be the only unsaturated factor.
Then A>=2 is even, U=X^A phi^(7A)product_i Q_i^(B_i), and there is a selected ACTUAL root x of T with

    q=Phi(x), v(q)=1/(6A), v(2)=1,
    v(theta_2(x))=v(theta_5(x))=1/3,
    v(theta_3(x))>=1.

For the corresponding original alpha_i, its odd residue order is5 and L_0=1/(6A).
The full same-order multiplicity is sum_b a_(2^b*5)lambda_b=6A; every occurring lambda_b is strictly below6A.
All those layers are noncritical and their total value is exactly v(g)=1, agreeing with the original expression c^3-2b^5.
This supplies no additional valuation exclusion.
At the selected original prime, e_p=6A,f_p=2, and the sole prime above it in K has e_q=6A,f_q=4; their full norm-valuation contributions are12A and24A.

Let F_m be the monic integer trace polynomial defined by Phi_m(z)=z^(phi(m)/2)F_m(z+z^(-1)) for m>=3.
Write the COMPLETE factorization

    G=V product_(b>=0) F_b^(a_b),
    F_b=F_(2^b*5), nu=6A,
    sum_b a_b lambda_b=nu,

where V includes the sign and all other odd-order trace factors, including the even-multiplicity m=1,2 endpoint factors.
Thus Vbar is a unit at phi.
The exact first factors are F_0=Phi-2 and F_1=Phi-2(X+1).
For b>=2 and lambda=lambda_b,

    F_b=F_1(C_lambda)
       =Phi^lambda+2X^(lambda/2)(X+1)^lambda modulo4.

The complete product includes each odd a_b correction once; the two lambda=1 phases are retained and combined.
Only the odd layers with lambda_b>2A affect the specified strict unit window below2/3.
Define

    S=sum_(a_b odd, lambda_b>2A)
          X^(lambda_b/2)(X+1)^lambda_b phi^(nu-lambda_b).

Choose the integer lifts of Q_i used in C197 and write the actual T as

    H_T=X^A product_i Q_i^(B_i),
    T=H_T Phi^(7A)+2Phi^A U_T+4W,
    U_Tbar a unit at phi,
    chi_0=X Phi^2, Psi_0=Phi(chi_0),
    J_0=product_i Q_i(chi_0)^(B_i),
    C_0=X^A J_0 Psi_0^(7A).

Every extra factor and higher lift W remains in these formulas.
Let D=Vbar+C_0bar^3, so phi^A divides D by the exact canonical remainder.
The class Z is the UNIQUE unit satisfying

    Z^11=H_Tbar C_0bar^2 modulo phi^(3A).

The actual residual equations imply the window

    v(G(x)/q^nu-C_0(x)^3)>=2/3,
    equivalently v(G(x)-q^nu C_0(x)^3)>=5/3.

Under these actual-root hypotheses this window is equivalent to the fully specified congruence

    ZD+H_Tbar Vbar S=0 modulo phi^(4A).

The proof retains 2=-q^nu H_T(x)/U_T(x)+rho with v(rho)>=11/6 and pays every normalized correction error above5/6 and every other relevant coefficient error at least1.
The congruence is necessary, not sufficient for the original residual system.
If k_D=ord_phi D, then under the congruence k_D>=4A iff S=0.
Otherwise A<=k_D<4A and the largest odd-multiplicity layer must satisfy

    lambda_max=6A-k_D is a power of2,
    2A<lambda_max<=5A.

The full coefficient congruence remains required when this leading-order condition holds.

### E. Exact relation to the old support condition and the actual-unit odd part

Use the characteristic-two local ring O_loc=F_2[X]_(phi), and in this part abbreviate H=H_Tbar, V=Vbar, C_0=C_0bar.
The OLD C197 support condition F_old=H^6/C_0^21=1 modulo phi^(4A) is equivalent to Z^6=C_0^3 modulo phi^(4A).
This equivalence is a precise rewriting of old information and is not claimed to strengthen C197.
Put

    S_0=sum_(a_b odd, lambda_b>2A)
          X^(lambda_b/4)(X+1)^(lambda_b/2)
                           phi^(3A-lambda_b/2).

All displayed exponents are nonnegative integers, S=S_0^2, and the empty sum is allowed.
Under the old support condition the new unit gate is equivalent to the conjunction

    S in phi^A O_loc,
    V=[Z^3/(1+(Z^5/C_0)S_0)]^2 modulo phi^(4A).

The denominator is a unit, all choices of a lift of Z give the same condition, and the weaker3A substitution is used only after multiplying by S in phi^A.
In particular V is a square class modulo phi^(4A), equivalently ord_phi V'>=4A.
For the actual polynomial V=J_G^2 W_G with W_G squarefree and monic,

    W_G=1, or
    ord_phi W_G'>=4A and deg W_G>=8A+1.

The full uniform cyclotomic order groups occur in W_G according to the parity of their nu_n, with odd order5 already removed.
This W_G is distinct from the T-support polynomial W_U in Part A.
The square alternative is not excluded; neither the derivative condition nor its degree alternative is sufficient for the full specified square congruence.
No strict separation from the old support condition on realized actual inputs is asserted.

### F. Complete existing-model failure and unchanged limits

For the explicit data

    Q=X^15+X^14+X^12+X^8+1,
    U=X^2 phi^14 Q^3, R_star=X^3 phi^12 Q^3,

the full integer trace lift G_star=X^3(Phi-2)^12 mathcal_Q^3, with z^15 mathcal_Q(z+z^(-1))=Phi_31(z), has the complete pullback Phi_4^3 Phi_5^12 Phi_31^3.
It has A=2, S=0 and ord_phi(Vbar+C_0bar^3)=2; a hypothesized actual root with the stated C197 data would have normalized difference value1/6 and absolute value7/6<5/3, contradicting the necessary window.
Every complete dyadic repartition with this same R_star and U also fails, because it would require lambda_max=10.
The proof below verifies this comparison directly, without assuming L440's derivation.
These formal data already fail the old C197 support condition; this test supplies no independent new actual-input coverage and no original residual example.
Neither this version nor its parity result proves a uniform original-root/Haar transfer, an actual residual realization, or exclusion of all remaining zero-Haar configurations.

<a id="argument"></a>
## Complete new proof and exact fixed reuse

All definitions, full uniform multiplicities, C3/C5 support closures, prior order/cancellation conclusions and weighted original-resultant expenses invoked from v2 are precisely its [complete fixed argument](Yin_C_G0199_v2.md#argument), adopted through [R483](../audits/reviews/Yin_R_G0483_v1.md#joint-order-cancellation-consumer-whole-finding).
This is a one-way dependence on that physical predecessor, not a mutable family selector or a claim that its review covers the following new mathematics.
The following complete arguments replace their original draft proof homes for this candidate version.

<a id="zero-haar-coincident-three-five-targets"></a>
### Coincident C3/C5 targets exclude the cancellation witness

Date: 2026-10-20T15:27.
Root supplied this exact same-target condition after C199v2 was registered; the draft_inventory_later agent checked the direct application to (CC7).
This new consequence is not part of that fixed v2 or its actual R483 review.

In the complete original domain and notation of [adopted C199v2](Yin_C_G0199_v2.md#statement), fix an occurring odd n with gcd(n,15)=1 and suppose

    3 congruent to +/-5*2^j modulo n
                                      for some j>=0. (CC9)

For any primitive order-n z and x=q(z), this congruence gives tau(x)=chi(x)^(2^j).
Hence tau and chi induce the SAME permutation of Omega_n, not necessarily the identity permutation.
Their targets for each psi in S_n are the same irreducible factor, and both local degrees are 1.
But a source with N_psi>5nu_n/3 would have target exponent nu_n/3 under chi and nu_n/2 under tau by (CC7).
Since nu_n>0 these values are unequal, a contradiction.
Thus no such source exists and the complete disjoint pairing again yields (CC8) for this group.

Accordingly any actual large-source witness from the coprime-to-5 case must also fail (CC9).
If 3 divides n the congruence already fails by coprimality of its right side; no cross-order C3 target is reclassified as a same-order permutation.
This is a direct condition on the existing witness, with no search over n, enumeration, new arithmetic realization or change to the fixed C199v2 proof.

Original DL author date: 2026-10-20T15:44.
Human author Yin.
Root proposed testing the actual dyadic values of the complete zero-Haar cyclotomic product against the original residual equations and the C197 quadratic high branch.
The draft_inventory_later agent checked the existing local-layer proof, constructed the needed root-of-unity lift within the actual completion, separated it from both trace lifts, and derived the complete value and norm comparison.
This is author work, not an independent review or a new proof claim for the classical cyclotomic-layer formula.
No numerical calculation, parameter enumeration, new source acquisition or characteristic-zero residual construction is used.
The new necessary content is the exact original-generator/trace interface and the proved failure of this value comparison to strengthen the specified n=5 branch.

<a id="dyadic-cyclotomic-original-value-cost"></a>
## Reuse and exact scope

[L78's individual cyclotomic-layer formula](../ledger/Yin_L_G0078_v1.md#primitive-cyclotomic-local-layers) already gives the complete local valuations, including all bad primes, before summing norms.
Its [critical-layer argument](../ledger/Yin_L_G0078_v1.md#old-layer-exception-threshold) and [L74's fixed-prime proof](../ledger/Yin_L_G0074_v1.md#fixed-prime-actual-growth) retain initial cancellation and the exact eventual slope.
[L79](../ledger/Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) gives the reduction support and multiplicities.
Those classical steps are reused rather than registered as new mathematics.
The additional lift uses exactly the accepted simple-root specialization of [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001), with its actual source-proof limits.
The local degree and normalization conventions are the accepted scope of [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001).
No general Teichmuller structure theorem or uninspected source is assumed.

First let alpha be a nontorsion algebraic unit and K=Q(alpha).
Fix one actual prime q of K over 2 and work in its completion K_q.
Write v=ord_q/e_q, so v(2)=1, and let n be the exact order of the nonzero residue of alpha.
It is a finite odd integer.
All statements in the next section concern this specified original alpha and prime, not every possible root or a replacement of K by a freely chosen field.

## The actual root-of-unity lift and every dyadic layer

The polynomial Z^n-1 has integral coefficients and derivative n alpha^(n-1), a unit at alpha.
Its value at alpha has positive valuation.
Con26e-U001 therefore gives a unique root omega in K_q with the same residue as alpha.
It has exact order n, because its reduction has that order and omega^n=1.
Put

    u=alpha/omega,
    L_j=v(u^(2^j)-1)>0, j>=0.                  (DL1)

Every L_j is finite: otherwise alpha would be a product of roots of unity and hence torsion.
This constructs only the needed odd-order root-of-unity lift in the actual completion; no extra local field is charged or silently substituted.
The odd-cofactor argument in L74 gives v(x^n-1)=v(x-1) for v(x-1)>0, because n is odd and the linear term is the unique least-valued term.
Hence L_j=v(alpha^(n*2^j)-1).

For a positive cyclotomic index m, its valuation at alpha is zero unless its odd part is exactly n.
For the matching layers, the complete individual formula of L78 becomes

    v(Phi_n(alpha))=L_0,
    v(Phi_(2^b n)(alpha))=L_b-L_(b-1)
         =v(u^(2^(b-1))+1), b>=1.              (DL2)

The equality before introducing u follows from the prime-to-2 Mobius cancellation in L78, including n=1.
The final equality follows by factoring the difference of squares.
Equivalently, L79's exact cyclotomic quotient identity gives the same result after the odd-cofactor equality above.
No assumption that alpha^(2^b) generates K is made, and every layer keeps its actual multiplicity when used in a product.

The normalized critical case cannot be suppressed.
If y=u^(2^j), write L=L_j=v(y-1).
Since y+1=(y-1)+2, one obtains

    L<1: v(y+1)=L,      L_(j+1)=2L;
    L>1: v(y+1)=1,      L_(j+1)=L+1;
    L=1: v(y+1)=1+v(1+(y-1)/2)>=1,
                         L_(j+1)=1+v(y+1)>=2. (DL3)

All values remain finite by nontorsion.
In the last line, (y-1)/2 is a unit and its further cancellation with -1 is actual extra information.
The increment is not asserted to equal 1 at L=1.
After that line the next value is at least 2, so all later increments equal 1.
This is precisely the critical-depth limitation of L78, not a uniform bound on the exceptional unit term.

Write lambda_0=1 and lambda_b=2^(b-1) for b>=1.
If lambda_b L_0<1, every preceding squaring stays strictly below the critical value, and (DL3) gives

    v(Phi_(2^b n)(alpha))=lambda_b L_0.          (DL4)

For b=0 this is simply the first line of (DL2).
If no power-of-two multiple of L_0 equals 1, the nonzero-index layer formula is min(lambda_b L_0,1) for b>=1.
When a critical layer does occur, its exact value is the third line of (DL3), and it cannot be replaced by that minimum.

## The original trace periodic root, including order one

Now impose the original reciprocal setting: P is monic irreducible reciprocal nontorsion, with constant coefficient 1 and degree d=2r, delta=alpha+alpha^(-1), and F=Q(delta) is totally real.
Let p be the prime of F below q, and use the compatible normalized valuations v(2)=1 on both completions.
Let h be the degree over F_2 of the residue of delta.
In the residue field, the quadratic trace identity gives 2^h congruent to either sign of 1 modulo n, including the trivial n=1 case.
Thus eta=omega+omega^(-1) solves C_(2^h)(eta)=eta and has the same residue as delta.
The polynomial C_(2^h)(X)-X has unit derivative modulo 2.
Its unique lift in F_p is the [C191 periodic root](Yin_C_G0191_v2.md#argument), and uniqueness after passing to K_q proves that this eta is precisely that same root and belongs to F_p.
This identifies the two constructions; it does not identify a generic multiplicative lift of the trace residue with eta.

The exact factorization

    delta-eta=(alpha-omega)(alpha-omega^(-1))/alpha

gives the complete distance relation

    t=v(delta-eta)=L_0,      n>1,
    t=v(delta-2)=2L_0,       n=1.                (DL5)

For n>1 the two roots omega and omega^(-1) have distinct reductions, so the second factor is a unit.
For n=1 both are 1, the root eta is 2, and the factor is a square; this is the required trace doubling.
None of these valuations uses the ramification index of a larger splitting field in place of the actual original completion.

## Complete cyclotomic product, original residual values and norm weights

Use the full actual residual domain of [C196v3](Yin_C_G0196_v3.md#statement).
Let T in Z[X] be the monic degree-r minimal polynomial of delta, so P(z)=z^r T(z+z^(-1)).
Set theta_l=rem_T(T(C_l))/l in Z[X] for l=2,3,5, with a=theta_2(delta), b=theta_3(delta) and c=theta_5(delta) all nonzero.
For a fixed s in {1,-1}, assume

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0,
    G_can=rem_T(theta_5^3-2theta_3^5),
    G_can(delta)=g,
    I_can=0.                                   (DL6)

Here w=deg G_can<r and I_can is the logarithm of G_can(z+z^(-1))^2 integrated against normalized circle Haar probability.
The complete zero-Haar factorization and scalar convention are those already proved in [C199v2](Yin_C_G0199_v2.md#statement):

    H(z)=epsilon z^w G_can(z+z^(-1))
        =product_m Phi_m(z)^(a_m),
    epsilon in {1,-1}, sum_m a_m phi(m)=2w<d.

The value of epsilon alpha^w is a local unit.
At the fixed original prime q, all factors whose odd part differs from n have valuation zero, but they remain genuine units in the full value.
The C196v3 support theorem and the complete trace factorization ensure that this actual n is among the occurring odd parts.
The exact paid valuation is

    v(g)=sum_(b>=0) a_(2^b n) ell_b,
    ell_0=L_0, ell_b=L_b-L_(b-1) for b>=1.       (DL7)

Only the finitely many occurring indices contribute.
The [C178 residual valuation](Yin_C_G0178_v1.md#statement), in the same normalization, gives the exact comparison

    sum_b a_(2^b n) ell_b
       =v(g)=3v(c)=(3/2)(5v(a)-1).              (DL8)

This is local value data, not the complete normalized unit of g.
The zero-valuation factors omitted from the sum cannot be omitted from a future unit congruence.

For completeness put E_n=sum_b a_(2^b n)lambda_b.
The full trace multiplicity is nu_n=E_n for n>1 and nu_1=E_1/2 for n=1, by the complete reduction and trace calculation in C199v2.
Thus E_n L_0=nu_n t in both cases of (DL5).
If E_n L_0<1, every occurring layer satisfies (DL4) and v(g)=E_n L_0=nu_n t.
The same equality holds when E_n L_0=1 and E_n is not a power of 2, because each occurring lambda_b is a power of 2, is at most E_n by the nonnegative sum, and is therefore strictly smaller than E_n.
This elementary boundary observation will apply to the selected quadratic branch below; it does not replace the critical rule (DL3) in general.

All original degree weights remain in the full norm.
If e_p,f_p are the ramification and residue degrees of F_p/Q_2, and e_q,f_q are those of K_q/Q_2, the accepted all-prime degree sum gives

    v_2(abs(Norm_F(g)))=sum_(p|2)e_p f_p v_p(g),
    v_2(abs(Norm_K(g)))=sum_(q|2)e_q f_q v_q(g)
                     =2sum_(p|2)e_p f_p v_p(g). (DL9)

Indeed v_q(g)=v_p(g) on the compatible normalization, while the relative local degrees above each p sum to [K:F]=2.
No unramifiedness of K/F is assumed for this general identity.
The polynomial evaluation has H(alpha)=epsilon alpha^w g, and Norm_K(alpha)=1, so the complete original resultant also retains abs(Res(P,H))=abs(Norm_F(g))^2.
There is no extra factor from identifying the trace and original fields or from a powered generator.

<a id="quadratic-high-branch-exact-value-match"></a>
## The selected n=5 high branch pays exactly the existing value

Use the actual original-input specialization of [C197v3 QX1--QX9](Yin_C_G0197_v3.md#quadratic-primary-generalized-root), not its more general arbitrary-monic domain alone.
Let Phi=X^2+X+1, phi=Phi mod 2, and suppose the canonical phi component is unsaturated.
Write A for the multiplicity at X in T mod 2.
Then C197 gives A>=2 even, N_phi=7A, ord_phi R=6A, and a SELECTED actual root x of the original minimal T in a finite 2-adic field for which

    v(Phi(x))=1/(6A),
    v(theta_2(x))=v(theta_5(x))=1/3,
    v(theta_3(x))>=1.                            (DL10)

These assertions are about that selected root; no identical distance is asserted at every original conjugate or prime.
Choose the corresponding original root alpha_i of P with x=alpha_i+alpha_i^(-1), and extend the same normalized valuation.
The reduction of x is a root of phi, so the exact odd residue order of alpha_i is 5.
For example, z^2-xz+1=0 implies z^4+z^3+z^2+z+1=0 at either reduced trace root, and z!=1, proving this order without a root search.

The root beta_0 used in C197 satisfies Phi(beta_0)=0.
It is NOT the C191 periodic trace root eta.
The exact factorization C4(X)-X=(X-2)(X+1)(X^2+X-1) shows that eta in this residue class satisfies X^2+X-1=0, so Phi(eta)=2.
Both Phi differences have the unit factor x+eta+1 or beta_0+eta+1 at this residue, and therefore

    v(beta_0-eta)=1,
    v(x-eta)=v(Phi(x)-2)=1/(6A),
    L_0=v(alpha_i/omega-1)=1/(6A).               (DL11)

The second equality uses 1/(6A)<1, so the terms have unequal valuations.
Here omega is the actual order-5 lift of the residue of alpha_i; it is not beta_0 or a multiplicative lift of x.

The order-5 trace factor is exactly phi, so the complete cyclotomic multiplicity satisfies

    E_5=nu_5=sum_b a_(2^b*5)lambda_b=6A.         (DL12)

For every occurring such index, nonnegativity of the multiplicities implies lambda_b<=6A.
Each lambda_b is a power of 2, while 6A is divisible by 3, so equality is impossible and lambda_b<6A.
Thus ALL occurring same-order layers are strictly below their critical threshold; by (DL4),

    v(Phi_(2^b*5)(alpha_i))=lambda_b/(6A),
    v(g)=sum_b a_(2^b*5)lambda_b/(6A)=1.         (DL13)

Every other odd-order factor is a unit and contributes zero to this valuation, though its normalized value is not discarded.
The actual residual expression at the SAME selected root already gives

    v(c^3)=1,
    v(2b^5)>=6,
    v(c^3-2b^5)=1.

Consequently (DL13) agrees exactly with (DL8) and (DL10).
The apparent exclusion of layers with lambda_b>=6A adds no constraint: their absence is already forced by the nonnegative sum (DL12).
There is no new valuation contradiction, stronger cyclotomic order exclusion or new norm income at this selected prime from this comparison.

One can also check the actual field weights at this root without adding an input hypothesis.
Since Phi(x) lies in the original F_p and has value 1/(6A), its integer ramification index e_p is divisible by 6A.
The trace factor degree is 2, and the C191 maximal-order filtration gives N_phi=sum_(p in this cluster)e_p f_p/2=7A.
Hence the selected p has e_p=6A and f_p=2; its cluster contribution is 6A and the other primes in that trace cluster contribute A.
The residue of alpha_i has order 5 and therefore degree 4 over F_2.
Since [K:F]=2, the sole prime q above this selected p has relative residue degree 2 and ramification degree 1, so e_q=6A and f_q=4.
Its contribution to the norm valuation of g is 12A in F and 24A in K, exactly as required by (DL9).
These identities are consequences of the already selected root and full filtration, not a claim that every original prime has these degrees.

## Outcome and the unit-data boundary

The full original cyclotomic value can now be compared without mixing integer and normalized valuations, without confusing a root-of-unity lift with a trace periodic root, and without losing the order-one doubling or any original K/F weights.
The n=5 application supplies an exact non-improvement result: the complete positive cyclotomic multiplicity and the actual C197 selected-root value pay the same amount automatically.
It neither realizes the branch nor removes the stronger coefficient and mod4 restrictions already retained by C197.

Any further comparison must retain normalized units, not infer new information from the matching valuations alone.
In particular factors of every other odd order, the exact centering unit epsilon alpha_i^w, the difference eta-beta_0, and the actual higher integral lift of T remain part of that unit value.
No cancellation among those units or uniform precision bound is proved here.
The complete C191 arithmetic floor and C195 paid logarithmic-transfer obligation remain unchanged.

The exact reused inputs are L74/L78/L79, Con26e-U001, The26b-U001, C191v2 for periodic roots and complete filtration, C178 for the local full-residual equation, C199v2 for the complete zero-Haar factorization/multiplicities, and C197v3 for the selected actual root and its exact domain.
The source and predecessor inspection boundaries are retained; their classical and adopted conclusions are not new independent proof audits by this author.
This DL stage proves no next unit-jet conclusion; the separately authored UJ part below supplies the subsequent comparison, with its own original date and scope.

<a id="quadratic-zero-haar-mod4-unit-jet"></a>
## The complete mod4 trace-layer and finite unit comparison

Date: 2026-10-20T16:02.
Human author Yin.
Root supplied the proposed dyadic trace-layer congruence, the full-unit comparison target, and the unique-eleventh-root elimination and leading-order consequences.
The draft_inventory_later agent verified the exact cyclotomic trace factors, all phases and error thresholds, derived the actual-T substitution criterion, and checked the complete order-31 comparison below.
Both are mathematical contributors; this is new author work from a later round than DL, and is not included in an existing independent review.
The new proof invokes the fixed [C197v3 actual-root interface](Yin_C_G0197_v3.md#quadratic-primary-generalized-root) and [complete localized-mod4 relation QX11](Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge), not a formal reduction treated as a characteristic-zero identity.
No numerical calculation, coefficient enumeration, new source or new finite-degree cutoff is used.

### Full original hypotheses and all trace factors

Keep the actual full residual and zero-Haar hypotheses (DL6), and the selected n=5 root and all original field/valuation conventions (DL10)--(DL11).
Thus A>=2 is even, nu=6A, q=Phi(x) with Phi=X^2+X+1, and v(q)=1/(6A), v(2)=1.
The original integer canonical polynomial G=G_can has its COMPLETE cyclotomic factorization after the reciprocal pullback.
For m>=3 define the monic integer trace polynomial F_m by

    Phi_m(z)=z^(phi(m)/2) F_m(z+z^(-1)).

Its integrality follows from the [integer reciprocal Laurent basis in L66](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) and C199; no division of the original coefficient normalization is made.
The factors m=1,2 have even multiplicities and contribute (X-2)^(a_1/2) and (X+2)^(a_2/2) to G, respectively.
Separate precisely the factors with odd part 5:

    G(X)=V(X) product_(b>=0) F_b(X)^(a_b),
    F_b=F_(2^b*5), a_b>=0,
    sum_b a_b lambda_b=nu=6A,
    lambda_0=1, lambda_b=2^(b-1) for b>=1.       (UJ1)

Here V includes the sign of G and EVERY other odd-order trace factor, including the m=1,2 factors when present.
It is an integer polynomial whose reduction is a unit at phi=Phi mod 2.
Only finitely many a_b are positive, and a positive multiplicity forces lambda_b<6A by (DL12).
The use of a_b in this section means the multiplicity of Phi_(2^b*5), not a multiplicity of a selected reduced factor.

### Every dyadic trace-layer phase modulo4

The first two exact trace factors are

    F_0=X^2+X-1=Phi-2,
    F_1=X^2-X-1=Phi-2(X+1).                     (UJ2)

For b>=2, put lambda=lambda_b.
The exact cyclotomic substitution identity gives

    F_b(X)=F_1(C_lambda(X)).

Indeed Phi_(2^b*5)(z)=Phi_10(z^lambda); the primitive-root orders and the complete degrees agree, and the reciprocal centers yield this trace identity.
The doubling recurrence C_(2k)=C_k^2-2, starting at C2=X^2-2, proves C_lambda=X^lambda-2 modulo4 for every power of 2 with lambda>=2.
Consequently F_b=X^(2lambda)-X^lambda+1 modulo4.
For any three polynomials, repeated squaring modulo4 gives

    (A_1+A_2+A_3)^lambda
      =sum_i A_i^lambda
         +2 sum_(i<j)(A_i A_j)^(lambda/2) modulo4.

The case lambda=2 is the exact square, and squaring a valid instance proves the next one because the terms already multiplied by 2 disappear modulo4.
Apply it to X^2,X,1, and use (X+1)^lambda=X^lambda+1 modulo2.
This proves the full proposed formula

    F_b=Phi^lambda+2u_b modulo4,
    u_b=X^(lambda/2)(X+1)^lambda, b>=2.         (UJ3)

For the same congruence at b=0,1 use u_0=1 and u_1=X+1, both with lambda_b=1.
The signs -2 in (UJ2) are therefore accounted for modulo4 rather than identifying these two different characteristic-zero phases.
Every u_b is a unit at phi.

Expanding the finite complete product modulo4 now gives

    product_b F_b^(a_b)
      =Phi^nu+2 sum_(a_b odd)u_b Phi^(nu-lambda_b)
                                                    modulo4. (UJ4)

All terms using two correction factors are multiples of 4, and the coefficient of a single correction is a_b modulo2.
The b=0,1 contributions with the same exponent combine as (a_0 mod2)+(a_1 mod2)(X+1).
This is either zero or a unit at phi; they are not silently counted as two independent exponents.
All other lambda_b are distinct.

### The actual comparison window, including the full lift of T

Use the complete C197v3 notation with a distinct name for its two-lift unit:

    H_T=X^A product_i Q_i^(B_i),
    T=H_T Phi^(7A)+2Phi^A U_T+4W,
    U_T mod2 a unit at phi,
    chi_0=X Phi^2, Psi_0=Phi(chi_0),
    J_0=product_i Q_i(chi_0)^(B_i),
    C_0=X^A J_0 Psi_0^(7A).                    (UJ5)

All Q_i are the distinct extra factors from the ENTIRE reduction of T, with their actual multiplicities and the chosen integer lifts in C197.
All higher coefficients remain in the integer W.
At the selected actual root x, C197 gives

    c=q^(2A) C_0(x)+error of valuation at least1.

Hence c/q^(2A)-C_0(x) has valuation at least2/3.
The exact original relation g=c^3-2b^5, with v(c)=1/3 and v(b)>=1, gives v(g/c^3-1)>=5.
Cubing the preceding unit approximation and combining the two errors proves the necessary target

    v(G(x)/q^nu-C_0(x)^3)>=2/3,
    equivalently v(G(x)-q^nu C_0(x)^3)>=5/3.     (UJ6)

This is a comparison with the actual integer G, not only with R=G mod2.

Let V_0 be any integer lift of Vbar=V mod2.
Replacing V by V_0 in the principal term q^nu V has error of valuation at least2, and in a term already multiplied by 2 the error has valuation at least2 before any nonnegative q power.
Likewise the remainder modulo4 in (UJ4) has valuation at least2 at the integral root x.
After division by q^nu, whose value is1, these errors all have valuation at least1.
An individual normalized correction has valuation

    v(2u_b(x)q^(-lambda_b))=1-lambda_b/(6A).

Thus only the odd-multiplicity terms with lambda_b>2A can affect the strict window below2/3.
The terms at equality lambda_b=2A have value exactly2/3 and may be discarded only for this specified inclusive target.
In particular both lambda=1 phases have been paid and lie above the window.
Define the ordinary polynomial over F_2

    S=sum_(a_b odd, lambda_b>2A)
                       ubar_b phi^(nu-lambda_b). (UJ7)

Every exponent is positive, because lambda_b<nu.

The actual equality T(x)=0 in (UJ5), divided by q^A U_T(x), gives

    2=-q^nu H_T(x)/U_T(x)+rho,
    v(rho)>=2-A/(6A)=11/6.                     (UJ8)

This is the required substitution of the original two-lift phase.
Its error in a normalized correction is at least11/6-lambda_b/(6A)>5/6, since lambda_b<6A, so it cannot affect (UJ6).
Combining (UJ4)--(UJ8), and multiplying by the unit U_T(x), shows that (UJ6) is equivalent to valuation at least2/3 for an integer polynomial expression whose reduction is

    U_Tbar D+H_Tbar Vbar S,
    D=Vbar+C_0bar^3.                             (UJ9)

Here the minus sign from (UJ8) becomes plus only after reduction to characteristic2.
If an integral polynomial unit-denominator expression has reduced phi-order k<4A, its value at x has exact valuation k/(6A)<2/3: write its numerator as Phi^k K+2L and use the unequal valuations.
If the reduced order is at least4A, its valuation is at least min(4A/(6A),1)=2/3.
The units U_T and all retained denominators do not alter that comparison.
Therefore the EXACT finite-window criterion is

    U_Tbar D+H_Tbar Vbar S=0 modulo phi^(4A).     (UJ10)

It is necessary for an actual residual realization of the full cyclotomic G and is equivalent to the window (UJ6) under the stated actual-root hypotheses.
It is not sufficient for the original characteristic-zero residual system.
All other odd-order factors remain in Vbar, and all extra T factors remain in H_T,J_0 and C_0.
The actual W was retained and its error paid in (UJ8); no assertion that T mod4 uniquely determines the original root is used.

### Eliminate the lift parameter with its already proved original relation

The actual canonical identity is R=rem_(Tbar)(Tbar(chi)^3), where chi=X phi^2.
Since R=phi^nu Vbar and Tbar(chi)^3=phi^nu C_0bar^3, it gives only

    phi^A divides D=Vbar+C_0bar^3.               (UJ11)

A multiple of Tbar has not been set to zero at x in characteristic zero.
Indeed an order as low as A can still affect the window (UJ6).

The full localized-mod4 theorem C197v3 QX11 also gives

    U_Tbar^11=E_11 modulo phi^(3A),
    E_11=H_Tbar X^(2A) Jbar^2 Psibar^(14A),
    Jbar=J_0 mod2, Psibar=Psi_0 mod2.            (UJ12)

Every factor on the right is a unit at phi.
The finite local ring F_2[X]/phi^(3A) has residue field F_4, and its unit group has order3*4^(3A-1).
Its reduction kernel has exactly4^(3A-1) elements, because a residue is a unit precisely when it is nonzero modulo phi.
Since 11 is coprime to this group order and the unit group is abelian, raising to the eleventh power is a bijection.
For example an inverse is an integer power determined by Bezout's identity for 11 and this group order; no computation or choice of a root is required.
Let Z be the UNIQUE class with Z^11=E_11 in this unit group.
Then Z=U_Tbar modulo phi^(3A).
Because D is divisible by phi^A, (UJ10) is therefore equivalent to the fully specified criterion

    Z D+H_Tbar Vbar S=0 modulo phi^(4A).          (UJ13)

Any lift of Z gives the same class in this formula.
This removes a free two-lift parameter from the test; it does not remove H_T,Jbar,Psibar or the full cyclotomic factor data that specify E_11 and D.
The modulus is input-dependent through A, with no global degree cutoff or asserted uniform transfer cost.

### A necessary leading-order condition without enumeration

Let k=ord_phi D, including k=infinity if D=0.
By (UJ11), k>=A.
If S is nonzero, its least exponent comes from the LARGEST lambda_b with odd a_b and lambda_b>2A.
Those lambda_b are distinct because the coincident b=0,1 layers have already left this window, and all ubar_b are units.
Hence

    ord_phi S=nu-lambda_max<4A.                 (UJ14)

All of Z,H_Tbar,Vbar are units.
Consequently (UJ13) has the following necessary consequences:

    k>=4A iff S=0;
    A<=k<4A implies
       S!=0, lambda_max=6A-k is a power of2,
       2A<lambda_max<=5A.                       (UJ15)

The first equivalence is asserted under the criterion (UJ13); without that criterion D and S are independent data.
For the second line, two terms of different phi-orders cannot cancel, so equality of their orders is necessary.
The full coefficient congruence (UJ13) remains required even when the orders agree.
Thus a value 6A-k that is not a power of 2 excludes the supplied complete reduction and cyclotomic factor budget without any enumeration of candidate orders or original degrees.
The individual odd multiplicity at lambda_max and the absence of larger odd layers are also retained in the definition of S.

<a id="order31-actual-cyclotomic-lift-unit-failure"></a>
### The complete order-31 comparison fails this window

Consider the already proposed [L440 order-31 comparison data](../ledger/Yin_L_G0440_v1.md#five-order-odd-support-budget-test) with A=2,

    Q=X^15+X^14+X^12+X^8+1 in F_2[X],
    Tbar=X^2 phi^14 Q^3,
    R_star=X^3 phi^12 Q^3.                      (UJ16)

The entropy_attainment_bridge agent authored that formal model and its original full-rational-unit failure; the present authors supply the new actual-cyclotomic-lift comparison.
This test does not assert that the formal lower-level model is an actual residual input.
The order-31 trace polynomial mathcal_Q in Z[X] is defined by z^15 mathcal_Q(z+z^(-1))=Phi_31(z), and its reduction is Q.
For a direct check of the reduction, the characteristic-two identities C_(2k)=C_k^2 and C_(2k+1)=C_(k+1)C_k+X give C7=X^7+X^5+X, C15=X^15+X^13+X^9+X, and C31=X^31+X^29+X^25+X^17+X=XQ^2.
Substitute z+z^(-1), use z^31-1=(z-1)Phi_31(z), and cancel the resulting squared Laurent identity; the domain has injective squaring, giving the claimed full reduction.
The integrality of mathcal_Q follows from the same integer reciprocal trace basis used above.
Thus the complete integer zero-Haar lift being tested is

    G_star=X^3(Phi-2)^12 mathcal_Q^3,
    z^72 G_star(z+z^(-1))
          =Phi_4(z)^3 Phi_5(z)^12 Phi_31(z)^3.   (UJ17)

Its degree is72, its pullback degree144 is below2deg Tbar=150, and every factor and multiplicity is retained.
It has nu=12, a_0=12 even and no other same-order layers, so S=0.
All other factors contribute Vbar=X^3 Q^3; they cannot be replaced by1.
The complete C197 expression is

    C_0bar^3=X^6 Q(chi)^9 Psi^42,
    Psi=phi(chi), chi=X phi^2.                  (UJ18)

This holds whether the integer lifts of the individual factors of Q multiply to mathcal_Q or differ by even coefficients.
Those differences do not alter the displayed finite-field unit data.

At either root beta of phi, take the formal local parameter p=phi and write X=beta+y.
The relation y+y^2=p gives

    X=beta+p+p^2+O(p^4).

Using Q's exact displayed polynomial, X^8=beta^2+O(p^8), X^12=1+O(p^4), X^14=beta^2+p^2+O(p^4), and X^15=1+beta^2 p+p^2+O(p^3).
Therefore

    Q=1+beta^2 p+O(p^3),
    X^3=1+beta^2 p+p^2+O(p^3),
    X^3 Q^3=1+p^2+O(p^3).                      (UJ19)

Also Q(Y)-1 has order8 at Y=0 and chi has phi-order2, so Q(chi)=1 modulo p^16.
Since Psi=1+Xp^2+X^2p^4 and 42 is even, Psi^42=1+O(p^4).
It follows that

    C_0bar^3=1+beta p^2+O(p^4),
    D=Vbar+C_0bar^3=beta^2 p^2+O(p^3),
    ord_phi D=2<4A=8.                          (UJ20)

The coefficient beta^2 is nonzero at both conjugate roots, so this is the exact irreducible-factor order.
For the displayed G_star, S=0 and (UJ13) fails for every allowed two-lift U_T.
More precisely, the actual unit difference in (UJ6) would have valuation2/(6A)=1/6, and the absolute difference G_star(x)-q^12 C_0(x)^3 would have value7/6<5/3.
Thus G_star cannot be the actual canonical g-polynomial of a full residual realization with these data.

The leading-order test gives the same conclusion for every complete cyclotomic dyadic repartition with this SAME reduced G and T: k=2 would require lambda_max=6A-k=10, which is not a power of2.
This is a test at the existing model's complete reduction and factor budget, not a new canonical-degree bound or a claim of new all-support exclusion.
The stronger pre-existing C197 full rational-unit condition already excludes the actual T-support in [L440's separate comparison](../ledger/Yin_L_G0440_v1.md#five-order-extra-support-full-mod4-failure); the present argument locates the failure of the proposed actual cyclotomic G lift in the lower comparison window itself.
Neither the formal quotient compatibility modulo2 nor the existence of a zero-Haar lift of R_star is promoted to a characteristic-zero realization.

### Closed scope of this finite-jet round

The proved output is the complete layer formula (UJ2)--(UJ4), the precisely paid window criterion (UJ10)/(UJ13), its nonenumerative leading-order consequences, and the exact existing-model failure (UJ20).
The scalar, original-field, complete cyclotomic degrees and original weighted resultants remain those of (DL6)--(DL9) and C199.
The test keeps all other odd-order unit factors and the actual two-lift relation of T; it does not infer a uniform original/Haar transfer or eliminate every possible E_11,D,S configuration.
No expansion beyond this bounded comparison or new input enumeration has been carried out.
The full original C197 QX11 and actual-root assumptions are direct inputs.
Root contributed to that upstream proof; its adopted [R477 independent consumer finding](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) is reused at its actual scope.
The present root/draft_inventory_later author derivation has not received an independent review.

Date: 2026-10-20T16:12.
Human author Yin.
The entropy_attainment_bridge agent checked the complete frozen UJ1--UJ20 account and developed the local-ring equivalence and precise new-data boundary below.
Root and that agent reached the sixth-power precision argument in parallel.
Root proposed the square/derivative consequence and the finite degree alternative for the odd-multiplicity part of the actual G-unit; the agent checked and completed their exact algebra and truncation scopes.
Both are contributors to the present relation theorem.
The underlying UJ construction is root/draft_inventory_later author work, and the old C197 support theorem retains its existing author and independent-review boundaries.
This is author discussion and a complete new deduction, not an independent review of UJ or of the contributor-overlapping C197 proof.
No mathematical program, finite-order search, new source acquisition or actual original-input construction was used.

<a id="cyclotomic-unit-gate-reuse-scope"></a>
## Exact reuse and changed obligation

The actual [C197v3 localized-mod4 proof](Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge) supplies QX11 and the complete support condition F=1 modulo phi^(4A), with its actual [R477 evidence](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding).
The present author contributed to that upstream proof and reuses its independent evidence rather than describing this as a new independent audit.
The complete [UJ1--UJ20 proof above](#quadratic-zero-haar-mod4-unit-jet) supplies the same fixed-version author input; it has not yet received an independent review.
Its displayed unit-window criterion, proved completely in this version, is the interface for the consequences below; this author relation proof does not promote its review status.
The local-ring implications are proved explicitly and therefore also apply conditionally to any units satisfying the stated equations.
The original [C199v2](Yin_C_G0199_v2.md#zero-haar-joint-three-five-order-obstruction) supplies the complete trace-order factor multiplicities, not a new modulus-four conclusion.

In the actual application, P is monic irreducible reciprocal nontorsion, has degree d=2r and constant coefficient1, delta=alpha+alpha^(-1), F=Q(delta) is totally real, and T is its actual monic minimal polynomial.
The nonzero integral quotient values a,b,c are theta_p(delta), theta_p=rem_T T(C_p)/p for p=2,3,5, with

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0, s in{1,-1}.

Assume the canonical G=rem_T(theta_5^3-2theta_3^5) has zero squared Haar logarithm.
Put U=T mod2, R=G mod2, Phi=X^2+X+1 in Z[X], and phi=Phi mod2; assume N_phi=ord_phi U>ord_phi R, the unsaturated quadratic branch.
The adopted C197 theorem then has A>=2 even, N_phi=7A, nu_5=6A and the selected actual root of valuation v_2(Phi(x))=1/(6A).
All other original fields, complete cyclotomic factors and scalar conventions remain those proved in the preceding UJ part.
The following notation is entirely in characteristic two after reduction:

    O_loc=F_2[X]_(phi),
    H=X^A product_i Q_i^(B_i),
    chi=X phi^2, Psi=phi(chi),
    J=product_i Q_i(chi)^(B_i),
    C_0=X^A J Psi^(7A),
    E=H C_0^2,
    F_old=H^6/C_0^21.                           (UR1)

Here H,C_0,E are units in O_loc.
The Q_i and B_i are the complete extra support and multiplicities of T mod2, as in C197; they have not been omitted from any unit.
The letter F_old is a rational FUNCTION, not the original trace field F.

Let V be the reduction of the ACTUAL remaining cyclotomic unit factor in G after removing all trace factors of odd order5.
Let a_b be the complete multiplicities of the removed cyclotomic trace factors of orders2^b*5, with lambda_0=lambda_1=1 and lambda_b=2^(b-1) for b>=2, so sum_b a_b lambda_b=6A.
The UJ criterion uses

    D=V+C_0^3 in phi^A O_loc,
    S=sum_(a_b odd, lambda_b>2A)
          X^(lambda_b/2)(X+1)^(lambda_b)
                         phi^(6A-lambda_b),
    Z^11=E modulo phi^(3A),
    ZD+HVS=0 modulo phi^(4A).                   (UR2)

The class Z is the unique unit eleventh root modulo phi^(3A); any polynomial lift of it may be used.
All occurring lambda_b are strictly below6A, and the terms b=0,1 are outside this S-window.
The divisibility D in phi^A comes from the actual canonical remainder relation; V is not a free unit parameter.
The old C197 necessary condition is F_old=1 modulo phi^(4A).

<a id="old-support-sixth-power-equivalence"></a>
## The old condition is exactly a sixth-power condition at the full precision

For each positive integer n, the finite local ring O_loc/(phi^n) is F_2[X]/(phi^n).
Its unit group has order3*4^(n-1): there are4^n residue classes and4^(n-1) nonunits.
This group is abelian and its order is coprime to11, so raising to the eleventh power is an automorphism.
An inverse exponent follows directly from Bezout's identity and the finite group order.
This elementary argument applies at both n=3A and n=4A.

Take any lift Z of the unique class in(UR2).
In characteristic two, if Z^11=E+phi^(3A)K, then

    Z^66=E^6 modulo phi^(6A).                   (UR3)

Indeed the sixth-power expansion has only terms with error powers2,4,6 besides E^6; its first possible error order is6A, not3A.
Thus, in O_loc/(phi^(4A)),

    (Z^6/C_0^3)^11=F_old.

By the eleventh-power automorphism, this proves the equivalence

    F_old=1 modulo phi^(4A)
      iff Z^6=C_0^3 modulo phi^(4A).            (UR4)

Changing the lift of Z by a multiple of phi^(3A) changes its sixth power only by a multiple of phi^(6A), so(UR4) is independent of that choice.
The converse also follows directly by raising the right side to the eleventh power and applying(UR3).
This is a full-precision rewriting of the ALREADY adopted T-support condition.
It supplies no additional restriction on T and is not a new breakthrough or a strict strengthening of C197.

<a id="actual-unit-gate-square-equivalence"></a>
## What the new gate additionally says about the actual G-unit

Assume the old condition(UR4), as every actual residual input must.
The UJ gate in(UR2), together with D in phi^A and the unit status of Z,H,V, first forces

    S in phi^A O_loc.                            (UR5)

This includes S=0.
The first term ZD already has that divisibility; a nonzero term HVS of smaller order could not cancel modulo phi^(4A).
Only AFTER this step can the weaker3A precision in the eleventh-root equation be multiplied into the desired4A precision.
Specifically,

    H/Z-Z^10/C_0^2 in phi^(3A) O_loc,

and multiplying by S gives zero modulo phi^(4A).
Divide the UJ gate by the unit Z and use(UR4).
It is therefore equivalent to the conjunction

    S in phi^A O_loc,
    V[1+(Z^5/C_0)^2 S]=Z^6 modulo phi^(4A).     (UR6)

Conversely, these two assertions allow the same replacement in reverse and recover the original gate.
Without(UR5), replacing H/Z at only3A precision would be unjustified.
Although the gate itself is independent of the lift of Z because D has order at least A, this fact alone would not justify an arbitrary4A substitution for H/Z.

Every term in S is a square in F_2[X].
Indeed A>=2 even and lambda_b>2A imply lambda_b>=8; hence lambda_b/2, lambda_b and6A-lambda_b are all even nonnegative integers.
Define the explicit polynomial

    S_0=sum_(a_b odd, lambda_b>2A)
          X^(lambda_b/4)(X+1)^(lambda_b/2)
                         phi^(3A-lambda_b/2).
    S=S_0^2.                                    (UR7)

All exponents displayed here are integers, and3A-lambda_b/2 is positive because lambda_b<6A.
If the sum is empty, S_0=0.
Equation(UR5) implies S_0 in phi^(A/2), so1+(Z^5/C_0)S_0 is a unit with residue1.
Thus(UR6) can also be written as

    S in phi^A O_loc,
    V=[Z^3/(1+(Z^5/C_0)S_0)]^2
                                  modulo phi^(4A).         (UR8)

This is an exact algebraic simplification of the NEW gate using the OLD support condition, not a claim that the gate holds automatically.
The right side is a specific square determined by all the actual data, not merely a requirement that some square exist.
All choices of a lift of Z give the same congruence by(UR6) and its equivalence to the well-defined gate.

In particular a necessary consequence is

    V is a square in O_loc/(phi^(4A)),
    ord_phi V'>=4A.                             (UR9)

For the derivative assertion, write V-B^2=phi^(4A)K in the local ring.
In characteristic two, (B^2)'=0 and (phi^(4A))'=0, so V'=phi^(4A)K'.
Differentiating local fractions is legitimate because every inverted denominator stays a unit at phi.
Conversely, a class with derivative zero in this quotient is a square: take its polynomial representative of degree below8A, differentiate, and use that its derivative has degree below8A and is divisible by the degree8A polynomial phi^(4A).
The derivative is therefore zero as a polynomial, all odd coefficients vanish, and the representative is a square over F_2.
This converse concerns only the square-class condition; it does NOT turn(UR9) into a sufficient condition for(UR8), which specifies the actual square and also(UR5).

<a id="actual-g-unit-odd-part-condition"></a>
## The precise odd-multiplicity polynomial and its finite degree alternative

In the actual zero-Haar situation V is a polynomial unit at phi.
Factor it over F_2 and write uniquely

    V=J_G^2 W_G,
    W_G squarefree and monic, phi not dividing J_G W_G.
                                                            (UR10)

The polynomial W_G is the product of the irreducible factors whose multiplicities in V are odd.
It contains X exactly when nu_1 is odd.
For each odd n>1 other than5, it contains the ENTIRE product of Omega_n exactly when nu_n is odd, by the adopted uniform multiplicity theorem.
The order-five factor has already been removed from V and is not inserted again.
Thus no selected subset of a complete cyclotomic order is hidden in W_G.

Differentiation gives V'=J_G^2 W_G'.
Because J_G is a unit at phi, (UR9) yields the exact necessary condition

    ord_phi W_G'=ord_phi V'>=4A.                (UR11)

If W_G=1, this derivative is zero and its order is infinite; that alternative is not excluded.
If W_G is nonconstant, squarefreeness over the perfect field F_2 makes W_G' nonzero.
The polynomial divisibility phi^(4A) divides W_G' then forces

    deg W_G'>=8A,
    deg W_G>=8A+1.                             (UR12)

This proves the complete alternative: either W_G=1, or the displayed finite degree bound holds.
It does not eliminate the square-unit branch, and it is not sufficient for the full coefficient equation(UR8).

The polynomial W_G is NOT C197's W_odd=product_(B_i/2^k odd)Q_i, which is built from T-support multiplicities after their common power-of-two extraction.
The two polynomials are built from different data: actual canonical G multiplicities versus T multiplicities.
They can overlap in support without being equal, and the degree bound on W_G does not by itself pay a surplus sum involving N_psi-nu_n.
No new canonical-degree cutoff or global budget contradiction is asserted.

<a id="unit-gate-actual-information-boundary"></a>
## Exact logical gain and the unresolved original-input question

The relation(UR4) is wholly old T-support information, expressed through the same uniquely determined root Z.
The new UJ comparison keeps the actual complete cyclotomic G, its dyadic odd-multiplicity correction S and its canonical-remainder unit V.
Using old F simplifies that comparison to(UR8) and yields the necessary derivative/odd-part consequences(UR9)--(UR12).
It does not delete V or S, and the pre-existing canonical congruence D in phi^A supplies only the first A orders, not the additional3A orders required by the gate.
The full original unit-window derivation, including its characteristic-zero error prices, is the preceding UJ proof; a rational-function identity about F alone is not a substitute.

This account proves no actual residual example satisfying the old support condition but failing the new gate.
Accordingly it makes no claim of strict additional realized coverage or logical independence of the two tests on the entire actual-input class.
An arbitrary choice of V cannot establish such a separation because V must be the canonical remainder of the SAME T and have its complete original cyclotomic factorization.
The existing order31 model in L440 and the UJ application already fails the old C197 condition, so its further UJ failure supplies no independent new exclusion of a previously surviving actual class.
Its formal zero-Haar lift is not an actual g-polynomial.

The specific remaining question is whether the simultaneous old support condition and the actual equation(UR8), with all canonical and cyclotomic constraints, admit or exclude the still-allowed inputs.
The square alternative W_G=1 and the larger nonconstant W_G alternative both remain possible necessary configurations.
No finite-order search, new parameter grid, original realization or unrestricted Mahler/Haar transfer is part of this result.

<a id="unique-quadratic-unsaturated-frobenius-parity"></a>
## A unique unsaturated quadratic component forces an odd remainder multiplicity

Date: 2026-10-20T16:12.
Human author Yin.
Root supplied the proposed common-Frobenius and complete degree-budget argument.
The draft_inventory_later agent checked the exact remainder division, all multiplicities, empty-product and reduction-degree boundaries, and retained the complete proof below.
Both are mathematical contributors to this new author consequence; this new consequence has not received an independent review.
The new content is an all-degree parity restriction for the precisely specified unique-unsaturated class, rather than a new numerical cutoff or a zero-Haar assertion.

### Actual original domain and the precise extra hypothesis

Let P in Z[z] be monic irreducible reciprocal nontorsion with constant coefficient1 and degree d=2r.
For a root alpha let delta=alpha+alpha^(-1), let the actual F=Q(delta) be totally real, and let T in Z[X] be its monic degree-r minimal polynomial, so P(z)=z^r T(z+z^(-1)).
Use the [actual trace-quotient domain of C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain):

    theta_p=rem_T(T(C_p))/p in Z[X], p=2,3,5,
    a=theta_2(delta), b=theta_3(delta),
    c=theta_5(delta), a,b,c all nonzero,
    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0, s in{1,-1},
    g=c^3-2b^5!=0.                               (UP1)

Let G_can=rem_T(theta_5^3-2theta_3^5), U=T mod2, R=G_can mod2 and phi=X^2+X+1 in F_2[X].
Assume phi divides U and is its ONLY unsaturated irreducible factor:

    ord_phi R<ord_phi U,
    ord_psi R>=ord_psi U
             for EVERY irreducible psi|U, psi!=phi. (UP2)

In particular R is nonzero; the zero polynomial, with infinite orders at all factors, cannot satisfy the first inequality.
Its degree may drop on reduction from G_can, but monic division still gives deg R<deg U=r.
No zero-Haar, cyclotomic factorization, small Mahler measure or bounded original degree is assumed.

The [exact canonical C196 graph of C196v3](Yin_C_G0196_v3.md#canonical-c5-residue-graph) and the [complete C197v3 quadratic theorem](Yin_C_G0197_v3.md#quadratic-primary-extra-support-obstruction) give the ENTIRE factorization and exact source order

    U=X^A phi^(7A) product_i Q_i^(B_i),
    A>=2, B_i>=2,
    ord_phi R=6A,                               (UP3)

where the Q_i are all the distinct remaining monic irreducible factors, different from X and phi.
All other factors of R remain allowed and will be charged separately.
The original exact equations in (UP1) imply the mod4 quotient hypotheses of C197 because evaluation at delta gives divisibility by its actual monic minimal polynomial T.
Thus this use does not replace the actual quotients by freely chosen coordinates.

### The inherited odd-support cost and common Frobenius power

Define the finite integer k and the positive integer exponents A_0,B_i0 by

    k=min{v_2(A),v_2(B_i) for all i},
    A_0=A/2^k, B_i0=B_i/2^k,
    U_0=X^(A_0) phi^(7A_0) product_i Q_i^(B_i0).
                                                     (UP4)

For an empty product take k=v_2(A).
The integer valuations in this definition concern exponents, not valuations in the original number field.
Because 7 is odd, the phi exponent introduces no smaller common power of2.
Consequently U=U_0^(2^k), and this is the maximal common Frobenius power of U.

The [adopted C197v3 common-Frobenius odd-part result](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) gives

    A_0 is even,
    W_U=product_(B_i0 odd) Q_i is nonconstant,
    deg W_U>=2A_0+1.                            (UP5)

This is the existing full rational-unit and logarithmic-derivative conclusion, not a new proof of its higher-adic input.
The empty product cannot actually occur under these hypotheses: it would make A_0 odd by the definition of k, contrary to (UP5).
More generally A_0 even and the minimum in (UP4) force at least one B_i0 to be odd, with no assumption about the individual degrees of those Q_i.
All such factors, including a possible X+1, occur in W_U and in its full degree cost.

### Exact Frobenius compatibility of the canonical remainder

Put chi=C5 mod2=X phi^2.
The exact polynomial identity from the C196 graph is

    R=rem_U(U(chi)^3).

Define R_0 by actual monic Euclidean division in F_2[X]:

    U_0(chi)^3=U_0 L_0+R_0,
    deg R_0<deg U_0.                            (UP6)

The zero remainder is permitted when defining this division, but will be excluded by (UP2).
Taking the 2^k-th power of (UP6) gives

    U(chi)^3=U L_0^(2^k)+R_0^(2^k).

The degree of the last term is less than deg U whenever it is nonzero.
Uniqueness of monic remainder therefore proves the exact equality

    R=R_0^(2^k), R_0!=0,
    deg R=2^k deg R_0<2^k deg U_0=deg U.        (UP7)

This argument uses the same U and the same chi; it does not divide a residue class or choose a different representative of the canonical R.
The nonzero assertion follows from R!=0.
Every irreducible factor multiplicity is divided by exactly 2^k in this identity, including any factor of R outside the support of U.
Thus (UP2)--(UP3) become

    ord_phi R_0=6A_0,
    M_X:=ord_X R_0>=A_0,
    M_i:=ord_(Q_i) R_0>=B_i0.                   (UP8)

The only permitted deficit among factors of U_0 is the phi deficit A_0, whose degree contribution is 2A_0.

### A square would overspend the entire canonical degree budget

Suppose for contradiction that R_0 is a square in F_2[X].
Then all its irreducible factor multiplicities are even.
For each odd B_i0, saturation in (UP8) consequently forces

    M_i>=B_i0+1.                                (UP9)

For even B_i0 the bound remains M_i>=B_i0.
At X the bound M_X>=A_0 suffices; no assumed equality at X is used.
Write the complete factorization

    R_0=X^(M_X) phi^(6A_0) product_i Q_i^(M_i) E,

where E is monic, coprime to U_0 and may equal1.
The extra polynomial E has nonnegative degree, and is not discarded from the comparison.
Subtracting the two COMPLETE degrees gives the exact identity and bound

    deg R_0-deg U_0
      =-2A_0+(M_X-A_0)
          +sum_i (M_i-B_i0)deg Q_i+deg E
      >=-2A_0+deg W_U
      >=1.                                     (UP10)

The first negative term is exactly the unique phi deficit, with its irreducible degree2 paid.
Every other displayed contribution is nonnegative, and the odd-exponent factors contribute their full W_U degree by (UP9).
This contradicts the strict canonical remainder degree in (UP7).
Therefore

    R_0 is not a square in F_2[X];
    equivalently R_0'!=0;
    R is not a 2^(k+1)-th power in F_2[X].       (UP11)

For the derivative equivalence, a polynomial over F_2 has zero derivative exactly when only even powers of X occur, in which case replacing X^(2j) by X^j gives its unique square root.
The final equivalence also uses injectivity of Frobenius: if R were a 2^(k+1)-th power, (UP7) would make R_0 a square.
Thus the maximal common Frobenius power of the nonzero canonical R is exactly the same 2^k as that of U.
When k=0 this says R itself is not a square.
When k>0 the original R is already a square by (UP7), so the conclusion concerns its normalized remainder R_0 rather than incorrectly excluding those automatic squares.

### Exact boundary of this author consequence

The conclusion applies at every original degree and Mahler measure in the actual domain (UP1), subject to the explicit unique-unsaturated hypothesis (UP2).
Reduction degree drop and extra factors of R only preserve or strengthen the degree contradiction; neither is assumed absent.
If another irreducible component is unsaturated, its further negative degree contribution would enter (UP10), and this proof gives no contradiction without paying that contribution.
The argument does not prove existence or nonexistence of the unique-unsaturated class, and it does not combine this parity restriction with the distinct zero-Haar unit-jet consequences proved separately in this version.
Its direct inputs are the actual C153 domain, C196v3 canonical identity and exact unsaturated formula, and C197v3 complete odd-support degree cost.
Root's upstream C197 authorship is retained, and its actual [R477 independent coverage](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) is reused at that fixed scope.
No new source, computation, input enumeration or independent review is asserted for this UP derivation.
Its candidate registration is the present v3 assessment below.

<a id="exact-inputs"></a>
## Exact direct inputs, comparison roles and original proof boundaries

| Input | Exact role |
| --- | --- |
| [C199v2](Yin_C_G0199_v2.md#argument) | All fixed KC/JT/CC through CC8, exact zero-Haar factorization, uniform order multiplicities, both support closures, target expenses and complete original weighted resultants; the new CC9 is proved here. |
| [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual P/K/F/T normalization and the three nonzero integral divided trace quotients, at the same original generator; no free integral triple substitution. |
| [C196v3](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | Exact monic canonical remainder, every original cluster and exact unsaturated exponent, used in UJ and UP; no later finite-width result is imported. |
| [C197v3 actual root](Yin_C_G0197_v3.md#quadratic-primary-generalized-root), [localized bridge](Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge), [odd-support theorem](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | Complete support N=7A, A even, chosen actual root and quotient values, full two-lift form of the same T, QX11 at3A precision and old rational-unit condition at4A, plus common-Frobenius W_U degree; each local application retains all Q_i and higher lifts. |
| [C191v2](Yin_C_G0191_v2.md#argument) | Simple periodic trace root and full maximal-order cluster exponent and local weights; the original norm floor is reused through v2 for the unchanged weighted expense. |
| [C178](Yin_C_G0178_v1.md#statement) | Exact full-residual local relation v(g)=3v(c)=(3/2)(5v(a)-1), with normalized v(2)=1 after dividing integer valuations by e. |
| [L74](../ledger/Yin_L_G0074_v1.md#fixed-prime-actual-growth), [L78](../ledger/Yin_L_G0078_v1.md#primitive-cyclotomic-local-layers) | Existing individual local cyclotomic formula, odd-cofactor identity and critical cancellation scope; the full needed formula and original-generator application are stated and derived in DL. |
| [L79](../ledger/Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) | Complete cyclotomic reduction support/multiplicities and quotient identity, not a later module or entropy conclusion. |
| [L66](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Integer reciprocal Laurent basis and trace polynomial convention, explicitly used for the complete F_m and mathcal_Q factors. |
| [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Accepted simple-root Hensel specialization for the actual odd-order root-of-unity lift inside K_q; no broad Teichmuller theorem or new source inspection. |
| [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Actual ramification/residue-degree normalization and all-prime degree sums, with its original source-proof limits. |
| [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001), [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Inherited exact classical cyclotomic definition/integrality/divisor factorization and scalar Jensen/Kronecker source attribution through v2; no new bad-characteristic source audit or enlarged proof-inspection claim. |
| [R483](../audits/reviews/Yin_R_G0483_v1.md#joint-order-cancellation-consumer-whole-finding), [R481](../audits/reviews/Yin_R_G0481_v1.md#zero-haar-odd-order-consumer-whole-finding) | Actual adopted v2 and v1 whole independent consumer scopes only; no retrospective coverage of CC9, DL/UJ, UR or UP. |
| [R477](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding), [R474](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding), [R468](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Exact upstream C197, C196 and C191 independent coverage, retaining all contributor-overlap boundaries; not a new self-review of these sources or this version. |
| [L440 order-31 model](../ledger/Yin_L_G0440_v1.md#five-order-odd-support-budget-test), [old-condition comparison](../ledger/Yin_L_G0440_v1.md#five-order-extra-support-full-mod4-failure) | Comparison and original model attribution only; UJ16--UJ20 supply the complete current polynomial and failure proof rather than importing a missing argument from L. |

The original extraction locations were D35 CC9/UP, D39 DL/UJ and D40 UR, at the mathematical dates and contributor accounts retained in the complete sections above.
Those working locations are provenance, not dependencies or necessary locations of an unregistered proof.
All new reasoning is present in this fixed version, and the predecessor proofs used as premises are precisely identified physical materials.
Root and entropy_attainment_bridge authored the C197 input; its actual R477 is reused rather than independently self-reviewed here.
The draft_inventory_later agent independently reviewed C196v3 in R474 and coauthored the old original-return part of C191, whose whole R468 scope remains explicit.
All three agents are contributors to this assembly through the new blocks described above; no one of them is designated an independent reviewer of the entire new version.
The unchanged old v1/v2 reviews do not adopt this candidate.
The DL local valuation non-improvement, the old-F equivalence, the stronger formal-model failure already supplied by old F, the distinct W_U/W_G definitions and the unsolved multi-unsaturated/square-unit cases remain limitations of the theorem, not omitted obligations.

## Current assessment
[Selected decision](#decision-initial)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T16:25 |
| status | open |
| reason | Complete candidate assembly of the same zero-Haar actual-cyclotomic inquiry, with explicit broader domains for the classical local layers and unique-unsaturated Frobenius parity. Preserve all CC9, DL1--DL13, UJ1--UJ20, UR1--UR12 and UP1--UP11 reasoning, exact inputs, scalar/local/global costs and author/source boundaries. Reuse physical adopted v2 for KC/JT/CC through CC8; new whole independent consumer review is required. No adoption, realization, all-residual exclusion or unrestricted transfer is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete domain-separated theorem](#statement) | Common actual residual domain; no-zero-Haar unique-unsaturated parity; prior zero-Haar theorem and same-target refinement; arbitrary-unit local layers; selected quadratic actual value match, complete finite unit gate, old-F relation, specified square and odd-part alternatives, full model failure and all original costs. |
| argument | [Complete new derivation](#argument) | CC9, DL1--DL13, UJ1--UJ20, UR1--UR12 and UP1--UP11 in full, exact monic Frobenius division, critical valuations, complete trace layers and higher-lift errors, finite-ring root precision, actual-unit and T-support distinction, self-contained example and all boundaries. |
| dependency | [Physical adopted v2 argument](Yin_C_G0199_v2.md#argument) | Exact KC/JT/CC through CC8, complete zero-Haar product and uniform multiplicities, both support closures, witness and all original resultant/degree expense; no later draft premise. |
| dependency | [Actual trace domain](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Same original monic reciprocal P, totally real trace F, actual T and integral nonzero divided quotient values. |
| dependency | [Original canonical graph](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | Exact CG3 remainder and CG5 unsaturated values with complete support/multiplicity, used in canonical UJ divisibility and UP; no later finite cutoff input. |
| dependency | [Complete generalized quadratic theorem](Yin_C_G0197_v3.md#argument) | QX actual support/root/two-lift, all extra factors, QX11 exact3A relation, old rational-unit4A condition and QX17--QX20 odd-support degree after common Frobenius extraction. |
| dependency | [Periodic root and full cluster weights](Yin_C_G0191_v2.md#argument) | Actual periodic lift uniqueness, complete maximal-order filtration and local weights used in DL; norm income for the inherited expenses is already included in the v2 premise. |
| dependency | [Residual local valuation](Yin_C_G0178_v1.md#statement) | Exact local full-residual value relation at every actual original dyadic prime. |
| dependency | [Odd-cofactor and local growth](../ledger/Yin_L_G0074_v1.md#fixed-prime-actual-growth) | Classical fixed-prime odd-cofactor valuation equality, with no new uniform bound on the critical unit term. |
| dependency | [Individual cyclotomic layers](../ledger/Yin_L_G0078_v1.md#primitive-cyclotomic-local-layers) | Exact individual Phi_m valuation support and layers, including the initial and critical bad-prime cases reconstructed in DL. |
| dependency | [Complete cyclotomic reduction](../ledger/Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) | Full reduction and quotient formulas for all2-adic layers and odd parts, with multiplicity and order-one trace doubling. |
| dependency | [Integral trace basis](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | The integral reciprocal Laurent/Chebyshev basis for complete trace polynomials and original field convention. |
| dependency | [Simple-root Hensel source](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Only the accepted actual-completion simple-root specialization for omega, with original source-proof scope. |
| dependency | [Local degree source](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Actual normalized valuations, local residue/ramification degrees and all-prime degree sums; no new source-proof inspection. |
| support | [Physical v1 and review](Yin_C_G0199_v1.md#argument) | Original KC proof/version preserved with its exact adopted R481, not recopied or extended. |
| support | [Actual v2 independent review](../audits/reviews/Yin_R_G0483_v1.md#joint-order-cancellation-consumer-whole-finding) | Entire old v2 scope only; not a review of new blocks. |
| support | [Actual C197 independent review](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Complete upstream QX proof and original author boundaries, not contributor self-review. |
| support | [Actual C196 independent review](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Exact graph and generic quotient interface reused at its accepted scope; reviewer-now-author relation disclosed. |
| support | [Actual C191 independent review](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Original whole periodic/cluster/norm coverage and earlier author overlap. |
| support | [Inherited cyclotomic source attribution](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Exact retained source definition/integrality/divisor-factorization scope via v2, no broadened source audit. |
| support | [Inherited scalar/Jensen/Kronecker attribution](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact inherited source scope, including signs, multiplicities and integrable circle zeros. |
| support | [Fixed order-31 comparison](../ledger/Yin_L_G0440_v1.md#five-order-odd-support-budget-test) | Original formal model attribution/comparison only; its current UJ polynomial derivation is fully in this C argument and gives no strict newly realized coverage. |
| support | [Complete exact inputs and limits](#exact-inputs) | All direct fixed inputs, classical attribution, old independent scopes, contributor relationships, broader versus zero-Haar domains, complete scalar/norm expenses and no mutable proof premise. |
