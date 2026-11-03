---
author: Yin
---

# Binary canonical G of fully cyclotomic first-four inputs is supported at odd orders divisible by fifteen

Human author Yin.
Provenance: project deduction under the unchanged [G0001 original contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the general odd-order reduction, actual cofactor model and final fifteen-divisible support statement.
The characteristic_zero_bridge agent proved and checked the general trace reductions and Delta-unit mechanism, all split binary components, every actual local evaluation and the separate w=1/B=0 and fifth-order endpoint cases.
Root read the entire saved OT1--OT17 argument, including its endpoints, full multiplicities and exact source scopes.
Both agents are substantive contributors; fresh isolated whole review and separate adoption remain outstanding.
No native coefficient scan, new original-source acquisition, assumed cyclotomic ramification index or nontorsion-layer theorem is used.
The entire necessary argument is fixed below and has no D proof dependency.

## Statement

### A. Full original domain and exact primary-support conclusion

Let T be ANY monic integer polynomial of degree d for which

    P_T(z)=z^d T(z+z^(-1))

is a COMPLETE product of cyclotomic polynomials, retaining all factors and actual multiplicities.
No irreducibility or nontorsion hypothesis is imposed.
Use C_2=X^2-2, C_3=X^3-3X and C_5=X^5-5X^3+5X, and the OWN canonical polynomials

    a=rem_T T(C_2)/2, b=rem_T T(C_3)/3,
    c=rem_T T(C_5)/5,
    F=rem_T(2c^2-3a^5), G=rem_T(c^3-2b^5),
    X_epsilon=rem_T(b^2-a^3+epsilon G),
    epsilon in{1,-1}.

Every prime division is an actual integer coefficient division before reduction, and every remainder uses the SAME original T.
Assume

    F=0 modulo4 coefficientwise,
    X_epsilon=0 modulo2 coefficientwise

for one, hence either, sign epsilon.

For n>2 define the full monic integer primitive-order trace factor F_n by

    z^(varphi(n)/2)F_n(z+z^(-1))=Phi_n(z).

The indexed F_n is distinct from the canonical residual F.
For odd h>1 put f_h=F_hbar.
These binary polynomials are squarefree, may be reducible, are pairwise coprime and are all prime to X.
The complete trace factorization gives

    U=Tbar=X^A product_(h>1 odd)f_h^(E_h),
    A>=0, E_h>=0, finitely many E_h nonzero.

The exponent E_h is uniform on every irreducible component of the COMPLETE f_h.
The exponent A retains all odd-part-one trace factors, including every endpoint contribution from X-2 and X+2.
Then the actual degree-bounded binary canonical remainder satisfies

    X^A product_(h>1 odd,15 not dividing h)
                         f_h^(E_h) divides Gbar.

Equivalently Gbar is zero on every full primary component except possibly those of odd root order divisible by15.
If Gbar!=0, at least one such fifteen-divisible component must therefore occur and be nonzero.
This does NOT assert vanishing on those remaining components, does not assert G=0 over Z, and does not construct a compatible example there.
T=1 has the zero quotient and is included trivially.
The full reciprocal degree remains2d throughout; no original residual congruence is transferred to a chosen factor.

### B. General trace and dyadic-unit statements used in the proof

For EVERY odd h>1 and dyadic w>=1,

    V_(h,w)=F_(2wh)=F_(2h)(C_w),
    F_(2h)(X)=(-1)^(varphi(h)/2)F_h(-X),
    V_(h,w)bar=f_h^w.

The trace polynomial C_w is defined by C_w(z+z^(-1))=z^w+z^(-w).
For Delta(A)=[A(C_2)-A^2]/2, one has

    f_h | Delta(F_h)bar,
    gcd(Delta(V_(h,w))bar,f_h)=1.

These assertions hold on every binary irreducible component of f_h, not merely at a selected root.

Let zeta be ANY primitive2wh root, theta=zeta+zeta^(-1), and v ANY normalized dyadic valuation of a number field containing the roots, with v(2)=1.
Then

    v(F_h(theta))=1/w,
    v(V_(h,w)(C_2(theta)))=1,
    v(V_(h,w)(C_2(theta))/2)=0.

The last quotient is the value of the ACTUAL integral dyadic divided remainder.
For w>=2 one also has v(F_h(C_2(theta)))=2/w.
For w=1, instead, F_h(C_2(theta))=0 exactly; the finite2/w formula is NOT used at that endpoint.
These conclusions follow from complete primitive-root products and geometric units, without an ambient ramification-index formula.

For every fully cyclotomic T as in Part A, but WITHOUT assuming either residual congruence, fix h with E=E_h>0.
Its actual alpha=abar has the alternative

    alpha=0 modulo f_h^E,
    or ord_psi(alpha)=2E-2w for EVERY psi|f_h,
       for a dyadic w with w<=E<2w.

In the second case V_(h,w) is an ACTUAL integer trace factor of T occurring exactly once.
The weight is the largest dyadic w whose actual factor multiplicity is odd.
The complete odd-base term, all other dyadic terms and the full other-order cofactor are included in this conclusion.

### C. Exact obstruction at h>5 divisible by five and prime to three

Suppose h>5, 5|h and3 does not divide h.
Put k=h/5>1, E=E_h>0 and B=E_k>=0.
For a fully cyclotomic T, its local beta=bbar is zero on f_h^E, and gamma=cbar has order B when B<E.
Thus the Gbar component is nonzero exactly when E>3B.

Assume only the own second residual is even and E>3B.
The actual dyadic factor then satisfies

    B=2E-2w, B even,
    w=E-B/2>5B/2,
    V_w=F_(2wh) occurs exactly once in T,
    D=T/V_w in Z[X] monic.

The full binary exponents of D at orders h and k are B/2 and B.
If B>0, necessarily B>=2 and w>=8, and for every primitive2wh trace theta and normalized dyadic place,

    v(D(C_2(theta)))=v(D(C_5(theta)))=B/w,
    v(a(theta))=v(c(theta))=B/w,
    b(theta)=0,
    v(F(theta))=min(1+2B/w,5B/w)<2.

The two residual-term values are unequal because a tie would require w=3B.
The cofactor estimate uses its ACTUAL identity D=M+2H with an integral same-binary model; the error values are at least1 and cannot cancel the displayed values below1.
Hence F cannot be coefficientwise divisible by4.

If B=0, w=E may equal1.
The two actual D evaluations and both a(theta),c(theta) are units; b(theta)=0 and v(F(theta))=0.
Thus F is not even in this case.
The removed factor has trace degree w varphi(h)/2 and full reciprocal degree w varphi(h), counted once; no remaining cofactor or multiplicity is discarded.

### D. Fifth-order/endpoints and limits of the conclusion

For h=5, write phi=f_5=X^2+X+1 and A=ord_X U.
A nonzero Gbar component requires E_5>6A.
If A>=1, adopted C758 applies in its exact arbitrary-T domain with the cyclotomic trace factor J=T and excludes F divisible by4.
If A=0, the unit branch is proved directly using the general Part B half-unit, including w=1, and gives v(F(theta))=0.
No A=0 application of C758 is made.

For every odd h with5 not dividing h, C_5 permutes the full primitive h traces, so gamma and Gbar vanish on f_h^(E_h).
At X the exact order of C_5bar=Xphi^2 is1, so the full X-primary Gbar also vanishes.
These statements complete Part A.

At h divisible by15 the map C_3 lowers odd root order and beta can compete in the second residual; the zero-beta argument in Part C is unavailable.
Those components remain unresolved.
No all-cyclotomic binary-G-zero theorem, noncyclotomic-factor conclusion, quantitative Mahler bound, characteristic-zero identity, source-family existence or unrestricted G0001 conclusion is asserted.

## Complete argument

<a id="cyclotomic-binary-g-odd-fifteen-support"></a>
### Fully cyclotomic first-four inputs have binary G supported only at odd orders divisible by fifteen

This is the complete fixed author argument proposed by root and checked by characteristic_zero_bridge.
The initial assessment is OPEN pending fresh isolated whole review and separate adoption.
The input [C758](Yin_C_G0758_v1.md#decision-whole-reviewed-2026-10-25) is now adopted and supplies only its exact FV2 root-difference lemma and the h=5, A>=1 first-four obstruction.
The complete integer trace classification is reused from [C752 CY3](Yin_C_G0752_v1.md#decision-whole-reviewed-2026-10-25), and actual canonical monic divisions/Delta products from [C736](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25).
The general h trace reductions, Delta-unit statement and all new local evaluations below are PROVED here, rather than extending C752's fifth-order formulas without proof.
The actually read [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001) supplies complete primitive-root products, integral cyclotomic polynomials and Phi_(2^r)(1)=2 at its recorded page3/pages6--8 scope.
Its irreducibility and integer-ring statements retain their stated original-proof limits.
The actually read [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) supplies the normalized number-field valuation convention and integrality facts only; no ramification index, nontorsion-layer theorem, norm estimate or Frobenius-lift bound is imported.

#### Exact statement and full cyclotomic domain

Let T be any monic integer trace of degree d such that

    P_T(z)=z^d T(z+z^(-1))

is a COMPLETE product of cyclotomic polynomials, with every actual multiplicity retained.
No irreducibility or nontorsion hypothesis is imposed.
For its OWN actual canonical system use

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a=rem_T T(C_2)/2, b=rem_T T(C_3)/3,
    c=rem_T T(C_5)/5,
    F=rem_T(2c^2-3a^5), G=rem_T(c^3-2b^5),
    X_epsilon=rem_T(b^2-a^3+epsilon G),
    epsilon in{1,-1}.

Assume coefficientwise F=0 modulo4 and X_epsilon=0 modulo2 for one, hence either, sign.
For each odd h>1 let F_h be the full primitive-order INTEGER trace factor and f_h=F_hbar; these are different from the canonical residual F.
Write the complete binary factorization by odd root order as

    U=Tbar=X^A product_(h>1 odd) f_h^(E_h),
    A>=0, E_h>=0, finitely many E_h nonzero.    (OT1)

Each f_h is squarefree, different f_h are coprime, and X is prime to every f_h.
The conclusion is that Gbar, as a class in F_2[X]/U, is zero on the X-primary component and on EVERY full f_h^(E_h) component with15 not dividing h.
Equivalently,

    X^A product_(h>1 odd,15 not dividing h)
            f_h^(E_h) divides Gbar.            (OT2)

Thus every nonzero primary component of the actual binary canonical G must have odd root order divisible by15.
This does NOT assert Gbar=0 on the components with15|h, and does not imply G itself is zero.
T=1 has the zero quotient and satisfies the conclusion trivially.
The proof keeps the original reciprocal degree2d and never passes a residual congruence to a chosen factor.

#### General full trace factors and reduction at every odd order

For n>2, C752's integral symmetric-Laurent argument gives the monic integer polynomial F_n with

    z^(varphi(n)/2) F_n(z+z^(-1))=Phi_n(z).

Its roots are the complete inverse pairs of primitive n-th roots.
The endpoint trace factors X-2 and X+2 lift to(z-1)^2 and(z+1)^2; their multiplicities in P_T are even, and all their contributions are retained in A.
For each odd h>1 separate the actual factors of T with that odd part:

    T_h=F_h^(m_0) product_(w a power of2)
                           V_(h,w)^(m_w),
    V_(h,w)=F_(2wh)=F_(2h)(C_w),
    E_h=m_0+sum_w m_w w.                       (OT3)

The equality for V_(h,w) follows from the complete primitive-root condition: z^w is primitive2h exactly when z is primitive2wh for dyadic w.
The full inverse pairs and equal monic degrees identify the polynomials.
Also F_(2h)(X)=(-1)^(varphi(h)/2)F_h(-X), because its trace roots are the negatives of the primitive h traces.

At any dyadic place, distinct odd-order roots of unity have distinct reductions.
Indeed if a nontrivial odd-order root xi of order r reduced to1, the exact identity1+xi+...+xi^(r-1)=0 would reduce to the odd integer r=1, a contradiction.
Trace reductions coincide only for inverse roots, since

    (zeta+zeta^(-1))-(rho+rho^(-1))
          =(zeta-rho)(1-(zeta rho)^(-1)).

The primitive odd h traces therefore remain distinct after inverse pairing, are nonzero in characteristic2, and are disjoint from every other odd-order trace set.
This proves the squarefreeness and coprimality assertions in OT1, including reducible f_h.
Since F_(2h)bar=f_h and C_wbar=X^w for dyadic w,

    V_(h,w)bar=f_h^w.                          (OT4)

Together with the full endpoint factors, these facts prove OT1 with the UNIFORM exponent E_h on every irreducible component of f_h.
No irreducibility of f_h over F_2 is assumed.

#### Root differences and the general divided-remainder unit

Use any normalized additive valuation v above2 in a number field containing the indicated roots, with v(2)=1.
All roots of unity and all polynomial arguments below are algebraic integers.
For a primitive2^r root eta, r>=1, the accepted complete product and value at one give

    2=product_(1<=j<2^r,j odd)(1-eta^j).

Each quotient(1-eta^j)/(1-eta) is a geometric sum with residue1, hence a unit.
There are2^(r-1) factors, so

    v(1-eta)=1/2^(r-1).                        (OT5)

This is C758 FV2's complete argument, also valid at r=1, and it assumes no ambient ramification index.

Let h>1 be odd, w a power of2, zeta primitive2wh, and theta=zeta+zeta^(-1).
At every chosen dyadic place decompose zeta=rho eta with rho primitive h and eta primitive2w.
The trace difference from rho has one factor of valuation1/w by OT5, and a second factor with nonzero residue1-rhobar^(-2).
Every other primitive h trace has different residue.
The full primitive product consequently gives

    v(F_h(theta))=1/w.                         (OT6)

When w>=2 the same reasoning applied to zeta^2, whose dyadic part is primitive w and whose odd part is still primitive h, gives

    v(F_h(C_2(theta)))=2/w.                    (OT7)

The condition w>=2 is essential: for w=1, C_2(theta) is an EXACT primitive h trace and F_h(C_2(theta))=0.
That endpoint will never be assigned the finite value2/w.

There is nevertheless a unit statement valid for EVERY w>=1.
Put xi=zeta^w, primitive2h, and sigma=xi^2+xi^(-2), a primitive h trace.
Then V_(h,w)(C_2(theta))=F_(2h)(sigma).
The full roots of F_(2h) are the negatives of the primitive h traces.
In its product at sigma, exactly one factor is2sigma, of valuation1 since sigmabar!=0, and every other factor has distinct nonzero residue.
Therefore

    v(V_(h,w)(C_2(theta)))=1,
    v(V_(h,w)(C_2(theta))/2)=0                 (OT8)

for every primitive2wh trace and every normalized dyadic place, INCLUDING w=1.
The quotient in OT8 is the evaluation of the actual integral dyadic divided remainder, by C736's monic integer identity; it is not division in characteristic2.

Define Delta(A)=[A(C_2)-A^2]/2 in Z[X].
Since V_(h,w)(theta)=0, Delta(V_(h,w))(theta)=V_(h,w)(C_2(theta))/2 is a unit.
The reductions of these theta cover EVERY root of f_h: lift the primitive h odd root and multiply by a primitive2w root.
Thus

    gcd(Delta(V_(h,w))bar,f_h)=1               (OT9)

on every irreducible component.
For the odd base F_h, doubling permutes its primitive roots, so F_h(C_2)=F_h Q_h with Q_h integral.
Modulo2 one has Q_hbar=f_h by monic division and cancellation in F_2[X].
Hence(Q_h-F_h)/2 is an actual integer polynomial and

    Delta(F_h)=F_h (Q_h-F_h)/2.

In particular f_h divides Delta(F_h)bar.
No assertion that its order is exactly1 is needed.

#### The largest odd dyadic weight determines every surviving local alpha order

Fix odd h>1 with E=E_h>0, and write T=T_h D_h with D_hbar prime to f_h.
The full integer Delta product rule gives, after reduction,

    Delta(T)bar=D_hbar^2 [
       (m_0 mod2) f_h^(2(E-1))Delta(F_h)bar
       +sum_(w:m_w odd) f_h^(2(E-w))
                                  Delta(V_(h,w))bar]
                           +f_h^(2E)Delta(D_h)bar. (OT10)

All actual multiplicities m_0,m_w are retained.
The odd-base term has order at least2E-1.
Each displayed dyadic term has EXACT f_h order2E-2w by OT9, simultaneously on every irreducible component.
The last cofactor term has order at least2E.
If the odd dyadic set is nonempty, its largest weight w is unique and has uniquely smallest order among these terms.
Thus reduction by U cannot cancel a term below order E, and the actual alpha=abar has the alternative

    alpha=0 modulo f_h^E,
    or ord_psi(alpha)=2E-2w for EVERY psi|f_h,
       where w is a power of2 and w<=E<2w.    (OT11)

If there is no odd dyadic term, or its maximal weight has2E-2w>=E, the first alternative holds.
If the second holds, the actual factor V_(h,w) occurs exactly once in T, because a second occurrence would contribute at least2w>E to E_h.
The statement allows f_h to split and does not replace its complete exponent by the order at a selected binary root.

#### Nonzero G at h>5 with five dividing h and three prime to h contradicts first-four

Now assume h>5, 5|h and3 not dividing h.
Put k=h/5>1, E=E_h>0 and B=E_k>=0.
Work in every full f_h^E component.
C_3 permutes the primitive h roots, so beta=bbar=0 there, with full exponent E retained.
C_5 sends primitive h roots to primitive k roots.
Its binary derivative is phi^2, phi=X^2+X+1, and is nonzero at the h traces because h!=5.
All other odd-order factors and the endpoint X factor are units at these image traces.
Consequently gamma=cbar=[U(C_5bar)] has exact order B at every psi|f_h when B<E, and is zero modulo f_h^E when B>=E.
Since Gbar=gamma^3, its component is nonzero exactly when

    E>3B.                                     (OT12)

Assume this nonzero case.
The even second residual gives alpha^3=gamma^3 modulo f_h^E and therefore ord_psi(alpha)=B on every irreducible component.
Apply OT11 to obtain

    B=2E-2w, B even,
    w=E-B/2>5B/2,
    V_w=F_(2wh) occurs EXACTLY ONCE in T.      (OT13)

The notation V_w here means V_(h,w).
Let D=T/V_w, an actual monic integer cofactor.
Its full binary exponents at orders h and k are respectively B/2 and B; all other complete factors remain in D.
The removed trace degree is w varphi(h)/2 and its full reciprocal degree is w varphi(h), counted once; no original norm or degree is normalized away.

First suppose B>0.
Then B>=2 and w>=8.
Write

    Dbar=f_h^(B/2) f_k^B Z,
    gcd(Z,f_h f_k)=1,
    M=F_h^(B/2) F_k^B Z_tilde,
    D=M+2H, H in Z[X],                         (OT14)

where Z_tilde is ANY monic integer lift of the actual Z.
This is a genuine same-binary polynomial model, not a claimed factorization of D into those integer lifts.

Take any primitive2wh zeta, its trace theta and any normalized dyadic place.
At C_2(theta), OT7 gives v(F_h(C_2(theta)))=2/w.
Its reduction has primitive odd order h, so F_k and Z_tilde are units there.
At C_5(theta), zeta^5 has primitive odd part k and primitive dyadic part2w, so OT6 at k gives v(F_k(C_5(theta)))=1/w.
Here F_h and Z_tilde are units because the reduced odd order is k.
It follows that both M evaluations have valuation B/w<1.
The actual integer error2H has valuation at least1 at either algebraic-integer argument and cannot change these smaller values.
Thus

    v(D(C_2(theta)))=v(D(C_5(theta)))=B/w.     (OT15)

The complete factor V_w(C_3(theta)) is exactly zero, since3 is prime to2wh.
Also V_w(C_5(theta))=F_(2h)(C_(5w)(theta)) is a unit: its reduced odd order is k rather than h.
OT8 and the actual integer canonical identities at T(theta)=0 therefore give

    v(a(theta))=v(c(theta))=B/w,
    b(theta)=0,
    v(F(theta))=min(1+2B/w,5B/w)<2.           (OT16)

The last two candidate valuations are unequal, since equality would require w=3B, impossible for a power of2 and a positive integer B.
The strict inequality uses w>5B/2, so in particular5B/w<2.
Coefficientwise divisibility F=0 modulo4 would force v(F(theta))>=2, because theta is integral.
This contradicts OT16.

If B=0, OT13 gives w=E, including the possible w=1.
The actual Dbar is prime to BOTH f_h and f_k, so both D(C_2(theta)) and D(C_5(theta)) are units directly from their reductions.
Use OT8, not OT7, and the same unit V_w(C_5(theta)).
Then a(theta) and c(theta) are units and b(theta)=0.
The two terms of F(theta) have valuations1 and0, hence

    v(F(theta))=0 when B=0.                    (OT17)

Thus F is not even, a stronger contradiction.
This separate argument covers the w=1 endpoint where OT7 would be invalid.

#### The fifth-order and endpoint components, and the exact remaining support

At h=5 put E=E_5 and retain the exact endpoint exponent A=ord_X U from OT1.
The local C_3 map permutes fifth traces, so beta=0 modulo phi^E.
Since C_5bar=Xphi^2 maps them to trace0 with phi-order2, gamma has exact phi-order2A when2A<E and is zero otherwise.
Thus a nonzero G component at h=5 requires E>6A.

If A>=1, take J=T in the ADOPTED C758 GF1--GF3 theorem.
Its arbitrary-T domain is exactly U=X^A Yphi^E with Y prime to Xphi and E>6A; the own second residual is even.
The whole reciprocal P_T is cyclotomic and its E_c=E>A, so C758 gives F not divisible by4, a contradiction.
No global forward condition or prescribed source construction is needed in this application.

If A=0, gamma is a phi-unit and the even second residual forces alpha a unit.
OT11 at h=5 gives w=E and an actual single V_(5,w), with Dbar prime to phi AND X.
For theta primitive10w, both D(C_2(theta)) and D(C_5(theta)) are units: the residues have respectively odd orders5 and1, the latter being trace0.
OT8 still gives the dyadic half-unit; V_(5,w)(C_5(theta)) is a unit because its argument after C_w has odd order1 and f_5(0)=1.
Again a(theta),c(theta) are units and F(theta) has valuation0.
This includes w=1 and excludes the remaining h=5 nonzero-G case without applying C758 outside A>=1.

If h>1 is odd and5 does not divide h, C_5 permutes the COMPLETE primitive h traces.
Consequently U(C_5bar) is divisible by f_h^(E_h) and gamma, hence Gbar, is zero on that full component.
This conclusion does not depend on the behavior of b there.
At the X-primary, C_5bar=Xphi^2 has exact X-order1 and all other factors of U are units at0, so U(C_5bar) has X-order A.
The full X-primary G component is therefore zero as well.

Combining these cases with OT12--OT17 proves OT2.
No statement has been made that the components with15|h vanish: there C_3 lowers odd root order, beta can compete with alpha and gamma in the second residual, and the zero-beta step used above is unavailable.
The unresolved15-divisible components are the precise remaining scope, not an assertion that a compatible example exists there.
Every argument concerns the original full T, full cyclotomic factors and actual monic remainders, with all endpoint and repeated multiplicities retained.
No all-cyclotomic binary-G-zero theorem, noncyclotomic-factor or Mahler lower bound, characteristic-zero identity, source-family existence or unrestricted G0001 conclusion is claimed.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision odd-fifteen-support-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T22:54 |
| status | open |
| reason | Register the complete OT1--OT17 author theorem after root read the entire saved argument and endpoints. For a fully cyclotomic reciprocal trace input with actual F divisible by4 and own X_epsilon even, the binary canonical G vanishes on every complete primary component whose odd root order is not divisible by15. General odd-order trace reductions, all split components, true Delta-unit and largest-weight facts, actual same-binary cofactor evaluations and the w1/B0 and h5/A0 endpoints are proved in full, with C758 used only in its exact accepted h5/A>=1 scope. Root and characteristic_zero_bridge are substantive contributors, not independent reviewers; fresh isolated whole review and separate adoption remain outstanding. The fifteen-divisible components, characteristic-zero equations and unrestricted Task remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete odd-order support theorem](#statement) | Parts A--D: original fully cyclotomic domain and full multiplicities, coefficientwise F4/X2 hypotheses, exact CRT support conclusion, general trace/Delta-unit facts, largest-weight alternative, exact h>5 evaluations, w1/B0 and h5/A0 endpoints, and every remaining fifteen-divisible limitation. |
| argument | [Entire OT1--OT17 proof](#complete-argument) | Complete integer trace and reduction construction, odd-root reduction separation, primitive dyadic product/unit estimate at every place, general half-unit, full Delta/cofactor expansion, exact local alpha/gamma orders and integer model, unequal residual values, coefficient inference and all endpoint/remaining-support cases. |
| dependency | [Adopted full cyclotomic trace classification](Yin_C_G0752_v1.md#decision-whole-reviewed-2026-10-25) | CY3 full integer trace factors, even endpoint multiplicities, retained complete cyclotomic product and fifth-order factor normalization. General h reductions, factor compositions and Delta-unit facts are explicitly proved here, not inferred from its fifth-order formulas. |
| dependency | [Adopted first-four fifth-order obstruction and root-difference lemma](Yin_C_G0758_v1.md#decision-whole-reviewed-2026-10-25) | FV2 primitive2-power root difference for all r>=1, reproduced in OT5, and GF1--GF3 only at h=5,A>=1,E>6A with J=T. No generic h, A0, nontorsion-layer or quantitative Mahler conclusion is imported. |
| dependency | [Adopted genuine canonical integer interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Actual coefficientwise prime divisions, monic integer quotient/remainder identities and exact Delta product rule, including repeated and common factors. No automatic residual inheritance by a factor or division by2 in a binary quotient is used. |
| dependency | [Accepted primitive products and value at one](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Printed p3 complete primitive-root product, pages6--7 integral cyclotomic factors and p8 Theorem9 Phi_(2^r)(1)=2; the value-at-one subargument was completely inspected in the U, while irreducibility/integer-ring original proofs retain its recorded limits. The new local trace/unit deductions are supplied here, without a new PDF or whole-source inspection. |
| dependency | [Accepted normalized number-field valuation convention](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Actual dyadic prime/DVR normalization v(2)=1, nonnegative values on algebraic integers and local units, including ramified primes. No ancestor-proof expansion, assumed cyclotomic ramification index, norm sum, degree substitution or Frobenius-lift result enters this proof. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T23:05 |
| status | proved |
| reason | Adopt the complete Parts A--D and OT1--OT17 theorem through fresh independent whole R980, whose entire finding root read. It passes all general odd-order trace, split-component, dyadic-unit, largest-weight, actual-cofactor, prime-division and full-primary assertions without substantive repair, with every root/place, w1/B0/A0/h5/T1 endpoint and exact accepted-input inspection limit retained. For a fully cyclotomic original T with own F modulo4 and either X modulo2, the actual binary G vanishes on X and every full odd-order component whose order is not divisible by15. All general Part B and conditional Part C claims are included. Root and characteristic_zero_bridge remain contributors; the separate fresh whole finding supplies independent review evidence. The fifteen-divisible components remain unresolved; no all-cyclotomic G-zero theorem, quantitative Mahler bound, characteristic-zero realization, compatible example or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete odd-order support theorem](#statement) | Parts A--D: original fully cyclotomic domain and full multiplicities, coefficientwise F4/X2 hypotheses, exact CRT support conclusion, general trace/Delta-unit facts, largest-weight alternative, exact h>5 evaluations, w1/B0 and h5/A0 endpoints, and every remaining fifteen-divisible limitation. |
| argument | [Entire OT1--OT17 proof](#complete-argument) | Complete integer trace and reduction construction, odd-root reduction separation, primitive dyadic product/unit estimate at every place, general half-unit, full Delta/cofactor expansion, exact local alpha/gamma orders and integer model, unequal residual values, coefficient inference and all endpoint/remaining-support cases. |
| dependency | [Adopted full cyclotomic trace classification](Yin_C_G0752_v1.md#decision-whole-reviewed-2026-10-25) | CY3 full integer trace factors, even endpoint multiplicities, retained complete cyclotomic product and fifth-order factor normalization. General h reductions, factor compositions and Delta-unit facts are explicitly proved here, not inferred from its fifth-order formulas. |
| dependency | [Adopted first-four fifth-order obstruction and root-difference lemma](Yin_C_G0758_v1.md#decision-whole-reviewed-2026-10-25) | FV2 primitive2-power root difference for all r>=1, reproduced in OT5, and GF1--GF3 only at h=5,A>=1,E>6A with J=T. No generic h, A0, nontorsion-layer or quantitative Mahler conclusion is imported. |
| dependency | [Adopted genuine canonical integer interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Actual coefficientwise prime divisions, monic integer quotient/remainder identities and exact Delta product rule, including repeated and common factors. No automatic residual inheritance by a factor or division by2 in a binary quotient is used. |
| dependency | [Accepted primitive products and value at one](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Printed p3 complete primitive-root product, pages6--7 integral cyclotomic factors and p8 Theorem9 Phi_(2^r)(1)=2; the value-at-one subargument was completely inspected in the U, while irreducibility/integer-ring original proofs retain its recorded limits. The new local trace/unit deductions are supplied here, without a new PDF or whole-source inspection. |
| dependency | [Accepted normalized number-field valuation convention](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Actual dyadic prime/DVR normalization v(2)=1, nonnegative values on algebraic integers and local units, including ramified primes. No ancestor-proof expansion, assumed cyclotomic ramification index, norm sum, degree substitution or Frobenius-lift result enters this proof. |
| review | [Fresh independent whole odd-order finding](../audits/reviews/Yin_R_G0980_v1.md#whole-finding) | Entire standalone Parts A--D and complete OT1--OT17, full multiplicities and split components, every generic and exceptional root/place evaluation, source scopes and final CRT support; all stated remaining-domain limits. |

