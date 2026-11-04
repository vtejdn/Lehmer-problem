---
author: Yin
---

<a id="weighted-lift-choice-cyclotomic-padding"></a>
# Integer lift transport, cyclotomic padding and unbounded Mahler branches at finite precision

Human author Yin.
The [selected G0001 continuation](../tasks/Yin_T_G0001_v1.md#decision-resume-after-account-handoff-2026-10-25) authorizes this work.
Provenance: project deduction from the actual constructed weighted powers, exact integer canonical divisions and complete trace-factor interfaces identified below.

Root proposed transporting the actual weighted-power construction across same-binary integer root lifts, then choosing complete cyclotomic trace lifts and separating their zero-Mahler factor.
Root also proposed the final-root integer variation, middle-coefficient Mahler bound and strict core-degree ratio, all checked below.
Salem_completion checked every source and correction term, the actual monic canonical congruences, endpoint roots, full-factor relifts and complete trace-factor source interface below.
These are author contributions, not independent review; the complete candidate requires fresh independent whole scrutiny and separate adoption.
The construction consumes [adopted C748](Yin_C_G0748_v1.md#decision-whole-reviewed-2026-10-25) and the actual source powers in [adopted C746](Yin_C_G0746_v1.md#decision-whole-reviewed-2026-10-25).
The complete C691 statement and six-section proof, C608 complete W_n/B_n identities, C667 FC1--FC3/FC6, and C199's integer trace/reduction interfaces were read at the exact scopes used below.
The integral reciprocal Laurent basis is also retained in C243's proof; only that elementary polynomial basis is used here, not its field hypotheses or index conclusions.
No new external theorem, numerical polynomial expansion or source-factor selection is needed.

## Statement

### LP1. Exact transport lemma and the resulting scope

Let d>=1 and let D>=1 be dyadic.
Suppose an actual monic degree-d integer polynomial has a FINITE presentation

    T=sum_i 2^(s_i) B_i^(r_i),
    s_i>=0, r_i a positive power of2,
    D divides 2^(s_i)r_i for EVERY i.              (LP1)

The polynomials B_i are actual integer polynomials, not binary classes or formal error coordinates.
Replace them by ANY integer B_i^new with B_i^new=B_i modulo2, subject to the new sum T_new being monic of the SAME degree d.
Then

    T_new=T modulo2D,
    T_new' divisible by D,                        (LP2)

and the OWN actual canonical systems at the two monic divisors satisfy

    a_(T_new)=a_T modulo D,
    b_(T_new)=b_T, c_(T_new)=c_T modulo2D,
    G(T_new)=G(T) modulo2D,
    F(T_new)=F(T), X_epsilon(T_new)=X_epsilon(T)
                                                   modulo D. (LP3)

All congruences are coefficientwise polynomial congruences, with either sign separately fixed.
Here C_2=X^2-2, C_3=X^3-3X and C_5=X^5-5X^3+5X are the same integer polynomials at both divisors.
The canonical definitions are exactly those of C748: a=rem_T T(C_2)/2, b=rem_T T(C_3)/3, c=rem_T T(C_5)/5, F=rem_T(2c^2-3a^5), G=rem_T(c^3-2b^5), X_epsilon=rem_T(b^2-a^3+epsilon G).
No common factor, squarefreeness, irreducibility or field quotient is assumed in this lemma.

Every explicitly constructed C748 source, BOTH and FIRST-only output admits LP1 with its stated derivative divisor D, as verified in LP4--LP5.
Its original q bound makes D at least the required final power of2, including the highest root of power1.
Thus its prescribed finite residual precision and nonzero canonical G modulo2 survive the new lift choice.
This conclusion concerns the ACTUAL changed full polynomial; it does not assert that arbitrary factor quotients retain that precision.
The explicit factor-preserving relift, cyclotomic/core factorization, finite-precision application and fixed-class unbounded-Mahler conclusions in LP6--LP10 are also part of the complete statement.

## Complete argument

### LP2. Genuine binomial congruence, including the last root of power1

Write B_i^new=B_i+2E_i over Z.
For a dyadic r and1<=j<=r, the identity j binom(r,j)=r binom(r-1,j-1) gives

    v_2(2^j binom(r,j))
       >=v_2(r)+j-v_2(j)>=v_2(r)+1.

Consequently (B+2E)^r-B^r is coefficientwise divisible by2r.
For r=1 this is the exact difference2E, so that endpoint is included without an asymptotic or even-power assumption.
Multiplying by2^s proves each summand difference is a multiple of2^(s+1)r, hence of2D under LP1.
Summing gives the first congruence in LP2.
Each new summand derivative is itself a multiple of2^s r, so T_new' is divisible by D without relying on cancellation between terms.
The original T has that derivative property for the same reason.
No degree-preservation assumption is needed for the congruence itself; the common monic degree is needed for the canonical comparison next.

### LP3. Same-degree monic division and every actual canonical loss

If monic integer divisors T_1,T_2 have the same degree and are congruent modulo an integer m, then for numerators A_1=A_2 modulo m their monic quotients and degree-below-d remainders are congruent modulo m.
Indeed the monic long-division algorithm uses only addition and multiplication of integer coefficients; after padding both numerators to a common degree bound it has the same descending steps, and reduction modulo m commutes with each step.
Equivalently it is the unique monic division over Z/mZ, whose remainder bound is the same d.
This needs no invertibility of a non-leading coefficient and no domain property of Z/mZ.

Apply this with m=2D to T_i(C_p), p=2,3,5, and the two actual divisors.
The prime divided remainders exist over Z because C_p=X^p modulo p and T_i(C_p)=T_i^p modulo p.
For p=2 their difference is an actual2D multiple before division, giving a_new-a in D Z[X].
For p=3 or5, the numerator difference is both a p-multiple and a2D multiple; since p is coprime to2D, division by p leaves a2D multiple.
This proves the a,b,c assertions in LP3 without division in a characteristic-two quotient.
The actual G numerators are congruent modulo2D, so a final monic division gives G_new=G modulo2D.
The F and X numerators are congruent modulo D using their displayed a,b,c/G congruences, and the final divisors are also congruent modulo D; hence their remainders satisfy LP3.
This argument retains both the changing numerator and changing divisor; it does not substitute a fixed-divisor remainder for the new canonical one.
It does not generally give F or X modulo2D, and that extra bit is not needed for the construction.

### LP4. Every actual weighted source term

Retain C748's parameters kappa>=5, M=2^kappa, L=M+kappa-3, ORIGINAL q, A=aq with a even, h=q h_b and d=h+14A.
Put J_K=H_b^((1-1/M)q), J_W=H_b^((1-2/M)q).
All roots named here are the actual integer roots constructed by C746/C748, with their actual lower factors imposed before taking powers.
The complete C746 source through its repaired BOTH8 output has the following terms; each outer Phi power is absorbed into the displayed root to obtain LP1.

| Actual term | Power r of its integer root | Outside coefficient | Guaranteed derivative divisor of this term |
| --- | --- | --- | --- |
| (H_b Phi^(7a))^q | q | 1 | q |
| 2Phi^A K_b^q | q | 2 | 2q |
| 4B_0^(2q/M) | 2q/M | 4 | 8q/M |
| 2Phi^(5A)L_1b^(q/M) | q/M | 2 | 2q/M |
| 4Phi^(3A/2)V_b^p, p=q/(4M) | p | 4 | q/M |
| 2Phi^(15A/2)M_b^p | p | 2 | q/(2M) |
| 2Phi^(9A)R_b^(q/(16M)) | q/(16M) | 2 | q/(8M) |
| 4Phi^(3A)V_src,b^(q/(16M)) | q/(16M) | 4 | q/(4M) |
| 8Z_b^(q/(64M)) | q/(64M) | 8 | q/(8M) |

The sixth row uses the ACTUAL L_2=Phi^(5A/2)M_b^p inside K_2=K_1+Phi^(4A)L_2; after multiplication by2Phi^A its exponent is15A/2.
It is not a binary target substituted for an integer source term.
The source's minimum termwise derivative divisor is exactly q/(8M)=q/2^(kappa+3), matching C746 GS0.
All r are dyadic divisors of q.
Since a is even, r divides A/2, so every outer Phi exponent in the table is divisible by r and can be absorbed into B_i before taking the r-th power.
The leading first term is monic of degree d; every other term has degree<d by the actual source CRT bounds.
No canonical remainder is added as an unstructured extra term in this presentation.

### LP5. Every later source jet, ordinary correction and terminal endpoint

At source stage j>=2, C748 adds only

    2^jPhi^(9A)R_b^(r_j),
    2^(j+1)Phi^(3A)V_b^(r_j),
    2^(j+2)Z_b^(q/2^(6j+kappa)),
    r_j=q/2^(6j+kappa-2).

Their termwise derivative divisors are respectively D_j,2D_j,D_j, with D_j=q/2^(5j+kappa-2).
All earlier terms have larger dyadic derivative divisors, by the explicitly decreasing source-stage budgets.
The potential pre-jet highest root is not included if that source stage stops before it; only the final chosen root after the jet is added.
The completed-final16 branch is included exactly when C748 includes it.

For a generic completed BOTH2^l input with derivative divisor D_old=q/2^Dexp and error exponent e=Dexp+l, put r_0=q/2^e.
Its actual following terms and termwise derivative divisors are

| Added term | Actual root power | Termwise derivative divisor |
| --- | --- | --- |
| 2^(l-1)Phi^(4A)B | r_0 | D_old/2 |
| 2^lV_0 | r_0 | D_old |
| 2^lPhi^(3A/2)U_1 | r_0/2 | D_old/2 |
| 2^(l-1)Phi^(15A/2)N | r_0/4 | D_old/8 |
| 2^lPhi^(3A/2)U_2 | r_0/4 | D_old/4 |
| 2^(l+1)R_final | r_0/16 | D_old/8 |

Only the first three rows occur for the FIRST-only branch.
The special l=3 step has roots nu_0,nu_0,nu_0/2,nu_0/4,nu_0/4,nu_0/16 and coefficients4,8,8,4,8,16, with the same relative divisor table because D_old=8nu_0.
Its special auxiliary Z occupies the second row and has the proved actual factor/power.
No l=3 formula is inferred by relabelling the generic mathematical correction identity; this table only records its already constructed integer terms.

All these outer Phi exponents are multiples of A/2 and all actual root powers divide q, so the same absorption argument as LP4 applies.
Each full correction has degree<d, every old term remains present unchanged, and the new minimum termwise divisor is D_old/8 for a full step or D_old/2 for a FIRST-only step.
Induction over the actual finite construction therefore proves LP1 for the final stated D, without relying on derivative cancellation.
For a C748 BOTH2^n output,

    D=q/2^(3n+2t+kappa-8)>=2^n;

for a FIRST2^m/X2^(m-1) output,

    D=q/2^(3m+2t+kappa-10)>=2^m.

The source endpoint likewise has D=q/2^(5t+kappa-2)>=2^(t+2).
These inequalities use the ORIGINAL q bounds, not an increase after the polynomial is chosen.
At the minimal full-step root endpoint r_final=1 the final term still has2^s r_final=D, so LP2 gives2D and LP3 retains the complete target precision.
The next divided-error VALUES or additional primary bits of C748 are not asserted unchanged; only the stated congruences and derivative divisor have been proved for the relift.

### LP6. Constructing the new full-factor roots without changing binary choices

Choose ANY monic H_b^new in Z[X] reducing to H_b0, of degree h_b, of the form X^aY_lift with Y_lift monic and Y_liftbar=Y_b.
Choose ANY monic Phi_new of degree2 reducing to phi.
These choices need not factor into individual monic lifts of the irreducible psi themselves.
The old proved construction is first fixed, including all its binary CRT root POLYNOMIALS and every actual root-factor/degree bound.
No new canonical target is recomputed from Phi_new or H_b^new.

Each old root apart from the distinguished leading one has the form

    B_i=Phi^(v_i) H_b^(u_i) X^(w_i) Q_i

with nonnegative integer exponents, after its exact lower factors and any absorbed outer Phi powers are separated.
The Q_i here are actual integer polynomials; their binary reductions are exact polynomial quotients of the old binary root by its proved lower factors.
If an old root is zero, use the zero new root.
Otherwise choose Q_i^new to be any integer lift of Q_ibar with degree at most degQ_i, for example its coefficient0/1 polynomial representative.
Put

    B_i^new=Phi_new^(v_i) (H_b^new)^(u_i)X^(w_i)Q_i^new. (LP4)

This has the SAME binary root polynomial and degree no larger than the old actual root.
All required integer factors are imposed before taking r_i-th powers; an arbitrary coefficient lift of the whole binary root is not presumed to retain them.
The same binary CRT class at every original high and lower modulus is therefore retained automatically.
Replacing a monic factor by its same-degree monic lift does not change any root degree cost.

For the leading term take B_0^new=H_b^new Phi_new^(7a) exactly.
It is monic of degree h_b+14a, so its q-th power is monic of degree d.
Every other new weighted term has degree<d by LP4--LP5 and the unchanged root bounds.
Hence T_new=sum_i2^(s_i)(B_i^new)^(r_i) is monic of the SAME degree d, as required by LP1--LP3.
This explicitly constructs an allowed relift; it does not treat degree or monicity as an unverified generic choice.

The root factors after raising give H_b^new to exponent q in the leading and initial K_0 terms, exponent(1-1/M)q in each first/second K correction and later source R correction, and exponent(1-2/M)q in initial W, all later W roots and every final highest correction.
The initial root exponents are the exact C746 factors H_b^(M/2-1), H_b^(M-1), H_b^(4M-8), H_b^(4M-4), H_b^(16M-32), H_b^(16M-16) and H_b^(64M-128) in their respective W_0,L_1,V,M,V_src,R,Z roots.
For later roots the exponent is the required J_K or J_W exponent divided by that root's actual dyadic power, always an integer.
In this grouping the C746 K terms and every later source R term enter2Phi_new^A K_new; all generic/special earlier, high, paired and final remaining additions have coefficients divisible by4 and enter4W_new.
Thus an ordinary earlier B or paired N carrying only J_W is never assigned to K_new or required to carry J_K.
The resulting polynomial has the actual form

    T_new=(H_b^new)^q Phi_new^(7A)
                      +2Phi_new^A K_new+4W_new,
    (H_b^new)^((1-1/M)q)|K_new,
    (H_b^new)^((1-2/M)q)|W_new,                  (LP5)

with the same degree bounds on K_new,W_new.
In particular, for the integer r_H=(1-2/M)q,

    T_new=(H_b^new)^(r_H) T_core,
    T_core in Z[X] monic,
    degT_core=(2/M)h+14A.                        (LP6)

There is no division by a nonunit leading coefficient: the factor is monic and divides every displayed integer term.
Writing K_new=(H_b^new)^((1-1/M)q)K_hat and W_new=(H_b^new)^(r_H)W_hat gives the useful exact core expression

    T_core=(H_b^new)^(2q/M) Phi_new^(7A)
                   +2Phi_new^A(H_b^new)^(q/M)K_hat+4W_hat.

No canonical residual statement for this smaller divisor is inferred from that expression.

The sole precision proof for this NEW integer lift is LP2--LP3.
In particular the C743 proof requiring individual psi lifts is not re-applied to an arbitrary whole H_b^new, and the old C5/Phi composition identities are not asserted for Phi_new.
Such properties are unnecessary for transport of the already proved finite congruences.
Binary Tbar=U and Gbar=R_0^q, maximal Frobenius q, actual derivative divisor D and all old degree/cost bounds are retained; extra next-error values or higher non-phi bits are retained only if separately justified, not by the new factorization alone.

### LP7. The complete source admits a cyclotomic whole-factor lift

This part specializes to the COMPLETE C691 source chosen in C748 GA10, rather than an arbitrary partial-group Y_b.
C608 defines W_n as the full inverse-paired primitive odd-order trace polynomial and proves B_n=product_(d|n,d>1)W_d.
C667 FC1--FC3 show that every ordinary row B_n and divided row B_(5ell)/phi is a nonnegative product of complete W_d and W_(5d), retaining each complete multiplicity.
Its exponent-floor adjustment and the complete fresh B_n^3 factor remain nonnegative whole products.
C691 uses precisely this construction at its larger finite target, so its actual Y_b has a finite factorization

    Y_b=product_(n odd,n>1,n!=5) W_n^(b_n),
    b_n nonnegative integers.                   (LP7)

The complete factors and every repeated multiplicity are retained.
This is not an assertion that an arbitrary irreducible factor of a W_n has an integer cyclotomic trace lift of the same degree.

For odd n>1, let F_n in Z[X] be the full monic integer trace polynomial satisfying

    Phi_n(z)=z^(varphi(n)/2)F_n(z+z^(-1)).       (LP8)

This is the adopted C667/C199 integer trace-factor interface used in C691 DG7.
Its elementary integrality mechanism is worth making explicit: a monic reciprocal polynomial C(z) of degree2e has invariant Laurent polynomial z^(-e)C(z)=c_e+sum_(j=1)^e c_(e+j)(z^j+z^(-j)).
The integer recurrence C_0(X)=2, C_1(X)=X, C_(j+1)=XC_j-C_(j-1) represents each z^j+z^(-j), giving a monic integer degree-e trace polynomial.
This is the integral reciprocal basis retained in C243; no irreducibility, nontorsion field, degree guard or index assertion from that theorem is used here.
For the reciprocal cyclotomic Phi_n it proves LP8 without any fractional coefficient normalization.

For odd n, z^n-1 is squarefree in characteristic2, and its complete divisor factorization shows that Phi_n mod2 has precisely the primitive n-th roots, each once.
Inverse pairs have distinct traces except at order1, which is excluded.
The characteristic-two Laurent substitution is injective because the highest positive Laurent exponent detects a nonzero polynomial's degree.
Consequently LP8 reduces to

    F_nbar=W_n, degF_n=degW_n=varphi(n)/2.       (LP9)

These are the complete trace/reduction facts already retained in C199v2/v3 and C667, with their necessary polynomial reasoning stated here.
No new external source claim is substituted for that checked fixed input.

Now choose the actual monic integer polynomials

    Y_lift=product_n F_n^(b_n),
    H_b^new=X^aY_lift,
    Phi_new=F_5=X^2+X-1.                        (LP10)

They have exactly the binary reductions and degrees required in LP6.
Their reciprocal pullbacks are the COMPLETE cyclotomic products

    P_H(z)=z^(h_b)H_b^new(z+z^(-1))
          =(z^2+1)^a product_n Phi_n(z)^(b_n),
    z^2 Phi_new(z+z^(-1))=z^4+z^3+z^2+z+1=Phi_5(z). (LP11)

The X^a endpoint is Phi_4^a, with no missing endpoint scalar or multiplicity.
The n=5 group is excluded from Y_b because it is prime to phi; the separate Phi_new factor is explicitly the full fifth cyclotomic trace factor.
The original integer Phi=X^2+X+1 is NOT claimed cyclotomic under this pullback; LP10 genuinely changes that lift by-2.

### LP8. Exact reciprocal factorization and absolute Mahler equality

Perform LP6's root relift with the actual LP10 choices, and let d_core=(2/M)h+14A.
The integers2q/M and r_H=(1-2/M)q are integral, so d_core is an integer.
Set

    P(z)=z^d T_new(z+z^(-1)),
    P_core(z)=z^(d_core)T_core(z+z^(-1)).

Both are monic reciprocal integer polynomials, of degrees2d and2d_core and constant coefficient1.
Equation LP6 gives the EXACT factorization

    P=P_H^(r_H) P_core,
    deg_trace T_core=(2/M)h+14A,
    deg P_core=(4/M)h+28A.                       (LP12)

The strict source margin h>(9M+1)A also gives the pure degree comparison

    degP_core/degP=d_core/d
              <(32M+2)/(M(9M+15)).

Indeed the function(2x/M+14)/(x+14) is strictly decreasing for M>2, and evaluating at x=9M+1 gives the stated bound.
This ratio is not a normalization of the Mahler equality below.

No coprimality between P_H and P_core is needed, and all repeated factors count.
Under the Task's absolute logarithmic Mahler measure m(f)=log|leading(f)|+sum_roots log max(1,|root|), products add because their leading coefficients multiply and root multisets concatenate.
Every root of the monic P_H in LP11 is a root of unity, so m(P_H)=0.
Therefore

    m(P)=m(P_core).                              (LP13)

This is an equality of absolute reciprocal-polynomial Mahler measures, with no degree normalization.
It is not an equality between the ordinary trace-polynomial measures m(T_new) and m(T_core), whose removed trace roots can have absolute value greater than1.
The congruence transport gives no comparison between the Mahler measures of the OLD reciprocal polynomial and this relifted P.
No positive or small value of m(P_core), no height bound and no irreducibility of P_core is established.

### LP9. Arbitrary finite precision with padding, and the factor boundary

For each separately fixed epsilon in{1,-1} and integer N>=1, choose the complete C748 GA18 data originally: kappa>=5 with M+1>=N, t=M/2-2, q>=2^(5M+kappa-8), and Q_src=2^ell with ell>=max(82,kappa+1).
Take its actual BOTH2^(M+1) output and its derivative divisor D=q/2^(4M+kappa-9)>=2^(M+1).
LP4--LP6 construct an actual monic T_new with the LP10 cyclotomic lower lifts, SAME degree and binary source, satisfying

    F(T_new)=X_epsilon(T_new)=0 modulo2^N,
    G(T_new)bar=R_0^q!=0,
    T_new=(H_b^new)^(r_H)T_core,
    m(z^dT_new(z+z^(-1)))=m(P_core).              (LP14)

In fact the stronger constructed BOTH2^(M+1) precision survives, and actual integer G(T_new) is nonzero because its binary reduction is nonzero.
The old original degree/gap, full fresh-factor maximal q, reciprocal degree and separate synthetic layer costs remain those paid in C748; only the chosen integer lifts have changed.
The derivative and all polynomial-degree bounds were proved termwise, including the final root of power1.
No partial-group substitution, unbounded coefficient search or hidden recomputation of an actual canonical target is needed to define the relift.

The canonical residuals in LP14 belong to the FULL T_new.
They are not assigned to T_core, nor is G(T_core) assigned the old binary value or a nonzero conclusion.
C736's exact cofactor weights explain why arbitrary factor extraction cannot be treated as same-precision canonical transfer; any actual loss or compatibility statement for the core is a separate obligation.
The cyclotomic P_H is a factor of the reciprocal pullback of T_new, not an identification of its actual canonical G with C691's separate synthetic zero-Haar polynomial.
No one polynomial for both signs, compatible infinite precision sequence, exact characteristic-zero residual identity, bounded height, irreducibility, total reality, near-one Mahler measure or unrestricted G0001 conclusion is supplied.

### LP10. Unbounded Mahler measure inside one fixed finite-precision coefficient class

Fix epsilon,N and choose kappa,M,t,Q_src as in LP9, but now select the permitted endpoint q EXACTLY as

    q=2^(5M+kappa-8), t=M/2-2, n=M+1.

Its exponent exceeds the primary/source floor L=M+kappa-3 by4M-5>0 and the source-root exponent6t+kappa by2M+4>0.
Thus this is an originally valid choice, not a post hoc alteration of a constructed polynomial.
In the last ordinary full step, the prior error exponent is4 less than5M+kappa-8.
Its earlier B,V_0 powers are16, first high-U power8, paired N,U_2 powers4, paired error power2 and final highest-root power1.
All preceding roots have the positive integral powers already checked in LP4--LP5.
The final term is therefore exactly2^(M+1)Z, where the ACTUAL integer Z has factor(H_b^new)^(r_H) and degree<(1-2/M)h+3A<d.

For ANY integer u, replace that root by

    Z_u=Z+2u(H_b^new)^(r_H).

This preserves its binary polynomial and actual lower factor, and its degree is still below the same bound because deg(H_b^new)^(r_H)=(1-2/M)h.
This includes a zero old root: the bound is on the actual permitted degree, not equality with the old zero polynomial's degree.
LP1--LP3 apply at D=2^(M+1), including r_final=1, so every resulting T_u has the same finite residual precision, canonical nonzero binary G, degree, actual factors and derivative bound.
More strongly, all T_u have the SAME coefficient class modulo2D=2^(M+2).
Their cores satisfy the exact relation

    T_core,u=T_core,0+2^(M+2)u,
    P_core,u=P_core,0+2^(M+2)u z^(d_core).        (LP15)

Here P_u=z^dT_u(z+z^(-1)) and P_core,u=z^(d_core)T_core,u(z+z^(-1)), with the SAME factor P_H^(r_H) in P_u=P_H^(r_H)P_core,u for every u.

Only the middle reciprocal coefficient varies; write it as A_mid(u)=A_mid(0)+2^(M+2)u.
For any monic polynomial P_core,u of degree2d_core, the elementary symmetric formula in its roots alpha_1,...,alpha_(2d_core) gives

    |A_mid(u)|<=binom(2d_core,d_core)
                    product_i max(1,|alpha_i|)
              =binom(2d_core,d_core) exp(m(P_core,u)).

Each individual d_core-fold product is bounded by the displayed full product, and there are exactly the indicated binomial number of such products; repeated roots cause no exception.
For every u with A_mid(u)!=0 this proves

    m(P_u)=m(P_core,u)
       >=log|A_mid(0)+2^(M+2)u|-log binom(2d_core,d_core),
    m(P_u) tends to infinity as |u| tends to infinity. (LP16)

Thus even with the requested N, sign, complete source, original q, degree, binary CRT classes and coefficient class modulo2D fixed, this permitted family has UNBOUNDED absolute Mahler measure.
This does not give a lower bound for every other choice in that finite-precision class or exclude a small-measure branch; it proves only the displayed unbounded family.
It also supplies no canonical precision inheritance to the smaller core.
The proof uses only the Task's root-product definition and elementary symmetric coefficients, not an external analytic estimate.
This complete author candidate requires fresh independent whole scrutiny; no adoption is made here.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision integer-lift-cyclotomic-padding-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:16 |
| status | open |
| reason | Register the complete LP1--LP10 author theorem after the actual source/term and whole-factor checks. Every constructed C748 output is a finite weighted dyadic-power sum with termwise derivative divisor D; replacing roots by same-binary integer lifts at the same monic degree gives T_new=T mod2D, canonical a modD, b/c/G mod2D and F/X modD, including the final root-power1 endpoint. Actual quotient-first root lifts with whole H_b_new and Phi_new preserve the original finite precision and nonzero full canonical G. For the complete C691 whole-group source, choosing cyclotomic trace lifts and Phi_new=X^2+X-1 yields T_new=H_b_new^r_H T_core, core trace degree2h/M+14A, its strict degree ratio and exact absolute reciprocal Mahler equality. At the paid smallest q for maximal BOTH(M+1), one fixed source/q/degree and coefficient class modulo2D contains the explicit constant-core variation with unbounded Mahler measure. Root and Salem_completion are contributors; fresh independent whole review remains outstanding. No small-measure exclusion, core canonical precision or nonzero core G, old/new Mahler preservation, compatible infinite precision, exact characteristic-zero residual identity, irreducibility or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete transport, padding and endpoint statements](#statement) | LP1--LP3 general same-binary root transport for finite weighted dyadic-power sums at a common monic degree; complete C746/C748 applications in LP4--LP6; whole-source cyclotomic lift, exact core degrees/ratio and absolute reciprocal Mahler equality in LP7--LP9; and LP10 fixed-source/q/degree/coefficient-class unbounded Mahler branch. No core canonical precision or nonzero core G is asserted. |
| argument | [Complete integer and finite-precision proof](#complete-argument) | Entire LP2--LP10, equations LP1--LP16 and both actual term tables: genuine binomial coefficient estimate including r1, monic changing-divisor congruences and odd prime division, every termwise derivative/root/degree cost, quotient-first new factors and K/W grouping, whole W_n/trace reduction, exact reciprocal factorization, root-product Mahler identity and endpoint middle-coefficient divergence with every stated scope limit. |
| dependency | [Adopted actual arbitrary finite-precision construction](Yin_C_G0748_v1.md#decision-whole-reviewed-2026-10-25) | GA1--GA10/GA18 ACTUAL constructed source and later roots, original q/degree bounds, all source/special/generic/high/pair/final correction coefficients and root powers, final derivative divisor, complete canonical residual targets and nonzero Gbar. LP4--LP5 verify the stronger term-by-term presentation rather than infer it from derivative divisibility alone; no arbitrary existential polynomial is presumed to have the chosen presentation. |
| dependency | [Adopted complete weighted BOTH8 source](Yin_C_G0746_v1.md#decision-whole-reviewed-2026-10-25) | GS1--GS4.5 actual initial q,q,2q/M,q/M and p=q/(4M) source powers, supported L_2=Phi^(5A/2)M_b^p, two source-jet roots and final q/(64M) root, all true lower factors and degree costs. LP4 enumerates every term and LP6 checks their factor exponents and K/W allocation. GS5 conditional downstream bookkeeping is not a premise. |
| dependency | [Adopted complete source and retained original costs](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 and complete Sections1--6: actual complete nonnegative whole-group Y, row floor and fresh complete B_n^3, nonzero canonical R_0 and maximal q, complete original degree/gap/layer costs. Only this whole-source specialization supports the chosen cyclotomic Y_lift; the separate synthetic zero-Haar G_int is never identified with canonical G(T_new). |
| dependency | [Adopted complete rows and integer trace-factor interface](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | FC1--FC3 ordinary B_n and exact divided B_(5ell)/phi row products, nonnegative complete W_d/W_(5d) multiplicities, floor adjustment and full fresh factor; FC6 complete integer F_n trace/reduction identity. These establish the actual Y_b factorization and allowed whole-factor cyclotomic lift. No original irreducible field realization or arbitrary partial-group lift is imported. |
| support | [Complete primitive trace-group definitions and root partition](Yin_C_G0608_v1.md#argument) | Definition of full W_n and SG6--SG8 nonidentity B_n Laurent identity and complete divisor partition. Used only as the established whole-group interface read for LP7, not its normalized A_0=2 gate, separating-character obstruction or native certificate. |
| support | [Retained exact odd cyclotomic reduction](Yin_C_G0199_v2.md#cyclotomic-reduction-identifies-the-relevant-orders) | KC6 and its odd-order squarefree exact-root argument identify Phi_n mod2 with the full primitive n-th roots. The odd case needed for F_nbar=W_n is also explicitly established in LP7. No zero-Haar premise, original field, valuation or complete gate conclusion is a dependency. |
| support | [Integer trace-polynomial attribution and explicit fifth factor](Yin_C_G0199_v3.md#full-original-hypotheses-and-all-trace-factors) | Only the retained F_m definition, integral reciprocal-basis attribution and explicit F_5=X^2+X-1. The necessary identity is proved directly in LP7 and consumed through the adopted C667/C691 interface; no whole-v3 adoption, original zero-Haar field hypothesis, phase formula or valuation conclusion is inferred. |
| support | [Integral reciprocal Laurent basis](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Only the elementary integer recurrence representing z^j+z^(-j) as a polynomial in z+z^(-1), explicitly written again in LP7. No irreducibility, nontorsion field, degree guard, order index or entropy comparison from C243 is applied to cyclotomic factors. |
| support | [Exact cofactor-weight boundary](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | The accepted canonical cofactor transfer explains the stated exclusion of automatic same-precision inheritance by T_core. Its factor formulas and examples are not used to claim any new core precision, nonzero core G or loss theorem here. |
| support | [Absolute logarithmic Mahler convention](../tasks/Yin_T_G0001_v1.md#contract) | Only the original root-product definition with leading coefficient and full multiplicities. LP8 proves multiplicativity and zero measure of the explicit monic cyclotomic product directly; LP10 proves its elementary symmetric coefficient bound directly. No normalized-by-degree measure, positive gap or Task completion is inferred. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:25 |
| status | proved |
| reason | Register the complete LP1--LP10 author theorem after the actual source/term and whole-factor checks. Every constructed C748 output is a finite weighted dyadic-power sum with termwise derivative divisor D; replacing roots by same-binary integer lifts at the same monic degree gives T_new=T mod2D, canonical a modD, b/c/G mod2D and F/X modD, including the final root-power1 endpoint. Actual quotient-first root lifts with whole H_b_new and Phi_new preserve the original finite precision and nonzero full canonical G. For the complete C691 whole-group source, choosing cyclotomic trace lifts and Phi_new=X^2+X-1 yields T_new=H_b_new^r_H T_core, core trace degree2h/M+14A, its strict degree ratio and exact absolute reciprocal Mahler equality. At the paid smallest q for maximal BOTH(M+1), one fixed source/q/degree and coefficient class modulo2D contains the explicit constant-core variation with unbounded Mahler measure. Adopt fresh isolated whole R970 after root read the complete LP1--LP10 proof, fixed statement and input scopes, and the entire independent finding. Root and Salem_completion remain contributors. The reviewer checked all actual construction interfaces and endpoint/source/measure limits without contributing a repair or claiming a recursive review of every transitive input. No small-measure exclusion, core canonical precision or nonzero core G, old/new Mahler preservation, compatible infinite precision, exact characteristic-zero residual identity, irreducibility or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete transport, padding and endpoint statements](#statement) | LP1--LP3 general same-binary root transport for finite weighted dyadic-power sums at a common monic degree; complete C746/C748 applications in LP4--LP6; whole-source cyclotomic lift, exact core degrees/ratio and absolute reciprocal Mahler equality in LP7--LP9; and LP10 fixed-source/q/degree/coefficient-class unbounded Mahler branch. No core canonical precision or nonzero core G is asserted. |
| argument | [Complete integer and finite-precision proof](#complete-argument) | Entire LP2--LP10, equations LP1--LP16 and both actual term tables: genuine binomial coefficient estimate including r1, monic changing-divisor congruences and odd prime division, every termwise derivative/root/degree cost, quotient-first new factors and K/W grouping, whole W_n/trace reduction, exact reciprocal factorization, root-product Mahler identity and endpoint middle-coefficient divergence with every stated scope limit. |
| dependency | [Adopted actual arbitrary finite-precision construction](Yin_C_G0748_v1.md#decision-whole-reviewed-2026-10-25) | GA1--GA10/GA18 ACTUAL constructed source and later roots, original q/degree bounds, all source/special/generic/high/pair/final correction coefficients and root powers, final derivative divisor, complete canonical residual targets and nonzero Gbar. LP4--LP5 verify the stronger term-by-term presentation rather than infer it from derivative divisibility alone; no arbitrary existential polynomial is presumed to have the chosen presentation. |
| dependency | [Adopted complete weighted BOTH8 source](Yin_C_G0746_v1.md#decision-whole-reviewed-2026-10-25) | GS1--GS4.5 actual initial q,q,2q/M,q/M and p=q/(4M) source powers, supported L_2=Phi^(5A/2)M_b^p, two source-jet roots and final q/(64M) root, all true lower factors and degree costs. LP4 enumerates every term and LP6 checks their factor exponents and K/W allocation. GS5 conditional downstream bookkeeping is not a premise. |
| dependency | [Adopted complete source and retained original costs](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 and complete Sections1--6: actual complete nonnegative whole-group Y, row floor and fresh complete B_n^3, nonzero canonical R_0 and maximal q, complete original degree/gap/layer costs. Only this whole-source specialization supports the chosen cyclotomic Y_lift; the separate synthetic zero-Haar G_int is never identified with canonical G(T_new). |
| dependency | [Adopted complete rows and integer trace-factor interface](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | FC1--FC3 ordinary B_n and exact divided B_(5ell)/phi row products, nonnegative complete W_d/W_(5d) multiplicities, floor adjustment and full fresh factor; FC6 complete integer F_n trace/reduction identity. These establish the actual Y_b factorization and allowed whole-factor cyclotomic lift. No original irreducible field realization or arbitrary partial-group lift is imported. |
| support | [Complete primitive trace-group definitions and root partition](Yin_C_G0608_v1.md#argument) | Definition of full W_n and SG6--SG8 nonidentity B_n Laurent identity and complete divisor partition. Used only as the established whole-group interface read for LP7, not its normalized A_0=2 gate, separating-character obstruction or native certificate. |
| support | [Retained exact odd cyclotomic reduction](Yin_C_G0199_v2.md#cyclotomic-reduction-identifies-the-relevant-orders) | KC6 and its odd-order squarefree exact-root argument identify Phi_n mod2 with the full primitive n-th roots. The odd case needed for F_nbar=W_n is also explicitly established in LP7. No zero-Haar premise, original field, valuation or complete gate conclusion is a dependency. |
| support | [Integer trace-polynomial attribution and explicit fifth factor](Yin_C_G0199_v3.md#full-original-hypotheses-and-all-trace-factors) | Only the retained F_m definition, integral reciprocal-basis attribution and explicit F_5=X^2+X-1. The necessary identity is proved directly in LP7 and consumed through the adopted C667/C691 interface; no whole-v3 adoption, original zero-Haar field hypothesis, phase formula or valuation conclusion is inferred. |
| support | [Integral reciprocal Laurent basis](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Only the elementary integer recurrence representing z^j+z^(-j) as a polynomial in z+z^(-1), explicitly written again in LP7. No irreducibility, nontorsion field, degree guard, order index or entropy comparison from C243 is applied to cyclotomic factors. |
| support | [Exact cofactor-weight boundary](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | The accepted canonical cofactor transfer explains the stated exclusion of automatic same-precision inheritance by T_core. Its factor formulas and examples are not used to claim any new core precision, nonzero core G or loss theorem here. |
| support | [Absolute logarithmic Mahler convention](../tasks/Yin_T_G0001_v1.md#contract) | Only the original root-product definition with leading coefficient and full multiplicities. LP8 proves multiplicativity and zero measure of the explicit monic cyclotomic product directly; LP10 proves its elementary symmetric coefficient bound directly. No normalized-by-degree measure, positive gap or Task completion is inferred. |
| review | [Fresh independent whole integer-lift and padding review](../audits/reviews/Yin_R_G0970_v1.md#c788-whole-review) | Entire LP1--LP10, LP1--LP16, both actual term tables, every endpoint, quotient/factor/degree/source/finite-precision conclusion and fixed-class unbounded branch, with exact fixed statement/proof bindings and independently reviewed relationship. Earlier adopted constructions are reused at their inspected consuming interfaces. |

