---
author: Yin
---
# Actual coefficient formula for the first dyadic trace-remainder error

Human author Yin.
The same_trace contributor developed FE1--FE11 on2026-10-23 under the [all-strategy continuation](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
The original author section in [D1](../drafts/Yin_D_G0001.md#same-t-first-error-coefficient-formula) is extraction provenance, not a logical input.
This material retains the complete statement and proof; its selected assessment below owns the actual review and adoption.
The new conclusion computes the formerly unspecified first error directly from the SAME monic T at the existing modulus8, and gives an exact local criterion plus a low-coefficient obstruction.
No higher-modulus iteration, numerical scan, original-input realization or unrestricted Mahler bound is asserted.
The reuse check inspected C197v3's actual localized mod4 interface, C202's complete paired mod8 criterion, C199v5's full normalized actual gate and the existing author handoff.
The core coefficient argument below is self-contained; the exact fixed inputs supply its stated branch application and comparison at the scopes listed after the proof.

## Statement


Let A>=2 be even, put N=7A, and write Phi=X^2+X+1 in Z[X] and phi=Phi mod2.
Let T in Z[X] be monic and have an exact decomposition

    T=H Phi^(7A)+2Phi^A K+4W,
    phi not dividing Hbar Kbar,                 (FE1)

where H,K,W are integer polynomials and a bar means reduction modulo2.
No irreducibility, total reality or characteristic-zero original realization is required for this coefficient statement.
For C_2=X^2-2 and C_5=X^5-5X^3+5X use the actual integer monic remainders

    a=rem_T(T(C_2))/2,
    c=rem_T(T(C_5))/5,
    F=rem_T(2c^2-3a^5).

Assume every coefficient of F is divisible by4.
Let Q_8 be the localization of (Z/8Z)[X]/(T mod8) at integer polynomials whose reduction is prime to phi, and similarly define Q_4.
Their characteristic-two quotient is B_phi=F_2[X]/(phi^(7A)).
Assume, as an explicit additional input, that an integer polynomial C has been chosen with

    cbar=phi^(2A) Cbar in B_phi.                 (FE2)

For the entire C197 support U=X^A phi^(7A) product_i Q_i^(B_i), with every remaining Q_i prime to X phi, this is the actual QX5 class, not an extra free coordinate.
One may choose any integer polynomial lift of

    Cbar=X^A product_i Q_i(chi)^(B_i) Psi^(7A),
    chi=X phi^2, Psi=phi(chi).

In particular (FE1)--(FE2) apply to the full C199v5 normalized A_0=2 branch with its ORIGINAL A=2q and all original factors retained.
No division of integer cyclotomic multiplicities by q is made.

Put Delta_2(K)=(K(C_2)-K^2)/2 in Z[X] and D_K=Delta_2(K)bar+Kbar^2.
Define the actual integer polynomial

    J_F=H C^2+3K^11.

Perform its canonical monic integer division by Phi^(3A):

    J_F=Phi^(3A) L_F+2M_F,
    deg M_F<6A.                                (FE3)

The stated evenness of the remainder follows from the assumed F=0 modulo4, as proved below, so (FE3) defines integer polynomials L_F,M_F without choosing a half in a ring of characteristic two.
Define O_F=(F/4) mod2 in B_phi, where the division uses the integer canonical coefficients before reduction.
Then the complete identity in B_phi is

    O_F=phi^A Kbar L_Fbar/Hbar^2
          +phi^(2A) Kbar^9 Wbar^2/Hbar
          +phi^(3A) Kbar^10 Wbar/Hbar
          +phi^(4A) [M_Fbar+Kbar^9 D_K]/Hbar.    (FE4)

Every displayed denominator is a unit in the specified local ring.
Consequently the first-error condition O_F=0 is equivalent to the single explicitly calculated congruence

    L_Fbar+phi^A Hbar Kbar^8 Wbar^2
      +phi^(2A) Hbar Kbar^9 Wbar
      +phi^(3A) Hbar [Kbar^(-1)M_Fbar
                                      +Kbar^8 D_K]
                         =0 modulo phi^(6A).     (FE5)

In particular it requires the polynomial congruences

    J_Fbar=0 modulo phi^(4A),
    J_Fbar=phi^(4A) Hbar Kbar^8 Wbar^2
              +phi^(5A) Hbar Kbar^9 Wbar
                                      modulo phi^(6A). (FE6)

The first line raises the explicit necessary root precision from the previously available modulo phi^(3A) relation to modulo phi^(4A).
It does not claim independence from all of the full C199 gate or prove that any admissible full-gate class fails it.
For a candidate with j=ord_phi J_Fbar in the range3A<=j<4A, the exact first-error order is

    ord_phi O_F=j-2A,
    A<=ord_phi O_F<2A.                          (FE7)

Such a candidate cannot satisfy the existing C202 first-error condition, for any integer V with deg V<deg T in the same coefficient class T->T+4V modulo4.
This excludes that entire specified coefficient class from a simultaneous mod8 solution; no such complete C199 candidate is asserted to have been constructed here.

## Argument

### Integer halves and the actual dyadic coefficient

Monic division of T(C_p) commutes with reduction modulo p, and C_p=X^p modulo p.
Since T(C_p)=T^p modulo p, both actual remainders are divisible by their displayed prime in Z[X].
The dyadic remainder also equals rem_T Delta_2(T), because T(C_2)=T^2+2Delta_2(T).
Monicity makes (Z/2^jZ)[X]/(T mod2^j) free over Z/2^jZ.
Clearing an allowed denominator therefore gives ann_(Q_4)(2)=2Q_4, ann_(Q_8)(4)=2Q_8 and the usual reduction kernels.
Thus an element of2Q_4 has a unique half modulo2 and an element of4Q_8 has a unique quarter modulo2.
This reproduces the explicit module argument of C197 QX10; it is not division by an arbitrary zero divisor.

Write U_1=Phi^A K and T_0=H Phi^N.
In Q_4, the relation (FE1) gives T_0=-2U_1.
For D=Delta_2(Phi), the integer binomial formula gives

    Delta_2(Phi^N)=N Phi^(2N-2)D
                    +2 binom(N,2)Phi^(2N-4)D^2 modulo4.

Both coefficients are even, both exponents are at least N, and Phi^N=-2Phi^A K/H in Q_4.
Hence this expression is zero in Q_4.
The product identity

    Delta_2(H Phi^N)=H^2 Delta_2(Phi^N)
       +Phi^(2N)Delta_2(H)+2Delta_2(H)Delta_2(Phi^N)

is therefore zero there as well, since Phi^(2N)=0 in Q_4.
Expanding Delta_2(T_0+2U_1+4W) and using T_0=-2U_1 gives

    a=U_1(C_2)-2U_1^2+2W(C_2)
      =U_1^2+2Z in Q_4,
    Zbar=phi^(2A)D_K+Wbar^2 in B_phi.           (FE8)

Here the last equality uses the characteristic-two product formula and the evenness of A, which makes Delta_2(Phi^A)bar=0.
It also uses W(C_2)bar=Wbar^2 and the unique module half just established.
Choose any localized integer lift Z of that half.
In Q_8 there is then a localized class E with a=U_1^2+2Z+4E.
Neither Z nor E is chosen independently of this actual a.

### Complete expansion at modulo8

By (FE2) and the reduction kernel, c=Phi^(2A)C+2D_c in Q_8 for a localized class D_c.
The actual first-residual expansion gives

    2c^2=2Phi^(4A)C^2 modulo8,
    a^5=U_1^10+2U_1^8 Z modulo8.               (FE9)

For the second identity, every term involving (2Z)^2 is divisible by8.
The only possible term from4E is20U_1^8 E, which also vanishes because U_1^8 has zero reduction in B_phi and hence belongs to2Q_8.
The remaining first-order coefficient10 is2 modulo8.
These facts show that (FE9) uses the actual fifth power without an unrecorded dependence on the next dyadic coefficient.

Reducing the powers by the SAME divisor relation in (FE1), in Q_8 one has

    U_1^10=-2Phi^(4A)K^11/H
                        -4Phi^(3A)K^10W/H,
    2U_1^8 Z=-4Phi^(2A)K^9Z/H.

Therefore

    F=2Phi^(4A)J_F/H
         +4Phi^(3A)K^10W/H
         +4Phi^(2A)K^9Z/H modulo8.              (FE10)

The canonical remainder F represents this same element of Q_8; the divisor has not been replaced while expanding.
Reducing (FE10) modulo4 and using the assumed F=0 gives, after the legitimate module cancellation of2,

    phi^(4A) J_Fbar=0 in B_phi.

Since Hbar is a unit and B_phi has modulus phi^(7A), this is exactly phi^(3A)|J_Fbar in F_2[X].
The remainder of canonical integer division of J_F by Phi^(3A) is consequently even, proving (FE3).
Substituting (FE3) into (FE10) gives

    2Phi^(4A)J_F/H
      =2Phi^(7A)L_F/H+4Phi^(4A)M_F/H
      =-4Phi^A K L_F/H^2+4Phi^(4A)M_F/H modulo8.

The discarded term is -8W L_F/H^2.
Take the legitimate quarter in Q_8, reduce modulo2, and insert (FE8).
This proves (FE4), including the term from reducing Phi^(7A) by the same T.
Multiplication by the unit Hbar^2/Kbar and cancellation of phi^A changes the modulus from phi^(7A) to phi^(6A), yielding precisely (FE5).
Reducing (FE5) modulo phi^(3A) and multiplying by phi^(3A) yields the second line of (FE6), and its first line follows in particular.
If3A<=j<4A, the first term in (FE4) has order j-2A<2A while all other terms have order at least2A, so no cancellation is possible and (FE7) follows.

### Independence of coefficient presentation and exact application boundary

The full formula (FE4) equals the actual canonical O_F, so changing an allowed presentation cannot change that element.
Its low obstruction also has an explicit presentation check.
With H fixed, the exact replacement K->K+2L and W->W-Phi^A L leaves T unchanged.
It leaves J_Fbar,Hbar,Kbar unchanged and changes the right side of (FE6) only by a multiple of phi^(6A).
Changing H to H+2S can be compensated by K->K-Phi^(6A)S, again leaving (FE6) unchanged modulo phi^(6A).
Any two decompositions (FE1) with the same prescribed Hbar differ by a combination of these replacements: reduce their difference modulo4 to obtain K'-K+Phi^(6A)S even, then solve for W'-W in the exact integer identity.
An alternative allowed C has Cbar'-Cbar in phi^(5A), because (FE2) fixes their product by phi^(2A) modulo phi^(7A).
Its change to J_Fbar has order at least10A and therefore does not change (FE6) or (FE7).
Thus the low diagnostic belongs to the same T and its actual quotient class, rather than to an artificial decomposition choice.

For a genuine change T^+=T+4V with V in Z[X] and deg V<deg T, fix H,K,C and replace W by W+V, writing v=V mod2.
The whole reduction and odd quotient class remain unchanged, so (FE2) still holds.
Equation (FE10) modulo4 also proves that local first-residual divisibility by4 is retained.
Whenever the canonical global quarters are defined, (FE4) gives exactly

    O_F(T^+)-O_F(T)
      =phi^(2A)Kbar^9 v^2/Hbar
                      +phi^(3A)Kbar^10 v/Hbar.  (FE11)

The same identity holds for the local module quarters if only local divisibility is imposed.
It verifies directly that the low range below2A is already fixed throughout the whole coefficient class modulo4, retaining both the quadratic and the linear changing-divisor terms.
For the second-residual specialization, put b=rem_T(T(C_3))/3, C_3=X^3-3X, and X_s=rem_T(b^2-a^3+s(c^3-2b^5)), with s in{1,-1}.
The exact changing-divisor identity used in C202 CL6, with4V in place of8V, gives a(T^+)=a(T)+2h modulo4 with hbar=v^2; the odd quotients and the monic remainder divisor are unchanged modulo4.
Hence X_s(T^+)-X_s(T)=2abar^2v^2 modulo4.
If both second residuals vanish modulo4, legitimate module cancellation gives abar^2v^2=0 in B_phi.
Since (FE8) gives abar=phi^(2A)Kbar^2 with Kbar a unit, this is exactly v in phi^(3A/2)B_phi.
Then the two terms of (FE11) have orders at least5A and9A/2, respectively, so the first-error coefficients below9A/2 are fixed.
In particular T->T+8V leaves the entire local O_F unchanged, as required by C202.

For the full SAME-T inquiry this calculates one of the formerly undecided errors at the original multiplicity A=2q.
A candidate must pass (FE5), the actual Gamma modulo8 condition and every original modulo4 condition, and must also satisfy the separate C202 test O_X in phi^(4A)Fr(B_phi), where O_X is the canonical second residual divided by4 before reduction and Fr denotes the image of squaring.
The other primary components and complete integer cyclotomic factorization remain required on that SAME input.
No compatible finite seed or universal failure of (FE5) on the full gate has been established here.
The next discriminating question is whether those full Gamma and second-residual premises force (FE5), or admit a candidate whose calculated J_Fbar violates (FE6); replacing the actual coefficients by free units would not decide it.
The newly explicit low obstruction supplies no unrestricted Mahler gap or original-root/Haar bound.

## Exact fixed inputs and review boundary

| Input | Exact use and boundary |
| --- | --- |
| [C197v3 actual quotient and decomposition](Yin_C_G0197_v3.md#quadratic-primary-generalized-root) | Branch application only: QX5 gives the actual C5 reduction in FE2, QX7 the same-T decomposition, and QX9/parity gives N=7A with even A under its full support and both mod4 residual premises. The generic FE theorem instead assumes FE1--FE2 explicitly. |
| [C197v3 localized mod4 argument](Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge) | Attribution and comparison for the localized module half and the earlier J_Fbar divisibility by phi^(3A). Both facts needed in FE are proved directly above; no historical review is extended. |
| [C199v5 full actual statement](Yin_C_G0199_v5.md#statement) | Exact application boundary: original normalized A_0=2 means original A=2q and all original factors, actual divided remainders and integer cyclotomic multiplicities remain. No full-gate incompatibility or seed is inferred. |
| [C202 quadratic-primary coupled criterion](Yin_C_G0202_v1.md#quadratic-primary-coupled-layer) | The already fixed mod8 target is O_F=0 and O_X in phi^(4A)Fr(B_phi), with every other primary component also required. This is the criterion to which FE5 and FE7 are applied, not a proof of their new coefficient formula. |
| [C202 exact changing-divisor identity](Yin_C_G0202_v1.md#integrality-and-changing-divisor) | The exact CL6 identity, with4V substituted for8V, is used only for the last second-residual-preservation specialization; its quotient reduction is hbar=v^2. |

The source author of this material contributed to the derivation and cannot independently review it.
The displayed argument has been author-checked for integer divisibility, canonical remainder precision, every localized denominator, the module-quarter operation, complete low-coefficient implications and presentation changes.
It remains open pending the separately arranged whole review, and does not change any old Claim decision or review relationship.
The new theorem may be reviewed at its precise conditional coefficient domain without assuming the existence of a full original C199 input.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T14:43 |
| status | open |
| reason | Register the complete FE1--FE11 author candidate: exact same-T first-error formula, equivalent coefficient criterion, low obstruction and coefficient-class exclusion, all presentation and changing-divisor checks. Whole independent review and adoption remain pending; no full C199 branch exclusion, compatible seed or unrestricted gap is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete conditional coefficient statement](#statement) | FE1--FE7 with actual monic T, actual divided remainders, original even A, integer canonical division and precise no-realization boundary. |
| argument | [Complete candidate proof](#argument) | FE8--FE11 and derivation of FE3--FE7, all module halves and quarters, exact powers and changing divisors, lift invariance, coefficient-class exclusion and full-gate limits. |
| dependency | [Actual primary input](Yin_C_G0197_v3.md#quadratic-primary-generalized-root) | Only the C197 branch application: QX5/QX7/QX9 and evenness match FE1--FE2 for the actual whole support; not a dependency of the explicitly conditional generic coefficient calculation. |
| dependency | [Full original normalized domain](Yin_C_G0199_v5.md#statement) | Only the original A=2q application and preserved full actual/cyclotomic boundary; no additional realization or universal exclusion premise. |
| dependency | [Existing coupled primary target](Yin_C_G0202_v1.md#quadratic-primary-coupled-layer) | The exact O_F=0 and Frobenius-image O_X criterion used for the stated application of the calculated obstruction. |
| dependency | [Exact divisor-change identity](Yin_C_G0202_v1.md#integrality-and-changing-divisor) | CL6 under the explicitly substituted correction4V, solely for preservation of the second residual modulo4 in the final specialization. |
| support | [Earlier localized unit precision](Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge) | Attribution and comparison for module halves and earlier modulo phi^(3A) root precision, with the necessary algebra fully rederived in this proof. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T15:05 |
| status | proved |
| authority | Yin activated all strategies and continued the unchanged G0001 Task. |
| reason | Adopt the complete FE1--FE11 coefficient theorem after the isolated whole R806 finding. Every original multiplicity, actual quotient and changing-divisor term remains; no compatible full-gate seed, universal exclusion or original Mahler bound is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete conditional coefficient statement](#statement) | FE1--FE7 with actual monic T, actual divided remainders, original even A, integer canonical division and precise no-realization boundary. |
| argument | [Complete candidate proof](#argument) | FE8--FE11 and derivation of FE3--FE7, all module halves and quarters, exact powers and changing divisors, lift invariance, coefficient-class exclusion and full-gate limits. |
| dependency | [Actual primary input](Yin_C_G0197_v3.md#quadratic-primary-generalized-root) | Only the C197 branch application: QX5/QX7/QX9 and evenness match FE1--FE2 for the actual whole support; not a dependency of the explicitly conditional generic coefficient calculation. |
| dependency | [Full original normalized domain](Yin_C_G0199_v5.md#statement) | Only the original A=2q application and preserved full actual/cyclotomic boundary; no additional realization or universal exclusion premise. |
| dependency | [Existing coupled primary target](Yin_C_G0202_v1.md#quadratic-primary-coupled-layer) | The exact O_F=0 and Frobenius-image O_X criterion used for the stated application of the calculated obstruction. |
| dependency | [Exact divisor-change identity](Yin_C_G0202_v1.md#integrality-and-changing-divisor) | CL6 under the explicitly substituted correction4V, solely for preservation of the second residual modulo4 in the final specialization. |
| support | [Earlier localized unit precision](Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge) | Attribution and comparison for module halves and earlier modulo phi^(3A) root precision, with the necessary algebra fully rederived in this proof. |
| review | [Whole isolated independent finding](../audits/reviews/Yin_R_G0806_v1.md#actual-dyadic-coefficient-whole) | Entire exact current statement, complete argument and every selected input at the explicitly bound scope; actual isolated independent review, with all upstream source and non-realization limits preserved. |

