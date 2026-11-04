---
author: Yin
---

# Full-primary square targets, endpoint obstructions and paid coprime sources

Human author Yin.
Provenance: project deduction under the unchanged [G0001 original contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the repeated-primary square mechanism, full old-primary target, exact padding support count and paid gcd repair.
The characteristic_zero_bridge agent checked the genuine integer canonical carries, derived the half-multiplicity quotient and exact restricted image/count, and proved the shared-primary and support-dimension obstructions.
Root read the entire saved OP1--OP15 and GC1--GC6 arguments.
Both agents are substantive contributors; fresh isolated whole review and separate adoption were still outstanding at author registration.
The [adopted C755](Yin_C_G0755_v1.md#decision-whole-reviewed-2026-10-25) supplies its actual source/padding and structural reference interfaces, but its whole review is not a review of the new mathematics here.
No native coefficient scan, numerical rank, actual full-primary target membership or original shared-factor gcd has been evaluated.
The separate continuing endpoint and certificate analyses in D6 are not incorporated into this Claim as unresolved premises.

## Statement

Use C_2=X^2-2, C_3=X^3-3X and C_5=X^5-5X^3+5X.
For each monic integer T, its OWN canonical polynomials are

    a_T=rem_T(T(C_2))/2, b_T=rem_T(T(C_3))/3,
    c_T=rem_T(T(C_5))/5,
    F_T=rem_T(2c_T^2-3a_T^5),
    G_T=rem_T(c_T^3-2b_T^5),
    X_(s,T)=rem_T(b_T^2-a_T^3+sG_T), s in{1,-1}.

All monic divisions and scalar divisions are actual integer operations at the SAME T before reduction.
Bars denote coefficient reduction modulo2.
For j>=1, the integral trace C_j satisfies C_j(z+z^(-1))=z^j+z^(-j); put c_j=C_jbar.
For positive odd n, B_n is the COMPLETE nonidentity n-th-root trace polynomial, so c_n=XB_n^2 and degB_n=(n-1)/2.
Write P_f(z)=z^(degf)f(z+z^(-1)) for a monic binary trace f.
Height1 reciprocal lifts here are monic with constant1 and every supported coefficient equal to1 or-1.

### A. General repeated-primary square property

Let U=product_psi psi^(e_psi) be any monic binary polynomial, with distinct monic irreducible psi and EVERY e_psi>=2.
Choose arbitrary monic integer lifts P_psi and T_0=product_psi P_psi^(e_psi).
For every monic integer T with Tbar=U there is a unique integer V of degree less than degU such that T=T_0+2V, and

    a_(T_0)bar=0,
    a_Tbar=Vbar^2 in F_2[X]/U.

Thus the exact set of canonical a_Tbar classes for UNRESTRICTED monic trace lifts is the square image in that quotient.
This does not assert a height1 or support-restricted realization.

### B. Complete old source, endpoint and actual square target

Retain an ACTUAL complete C691-type source, original or paid as in C753/C755, with

    Q=2^ell, ell>=82, m=Q/4-2,
    phi=X^2+X+1, chi=Xphi^2, lambda=X^3+X,
    Psi=phi(chi),
    U_old=X^(2m)Y_old phi^(14m), d=degU_old,
    B_src=X^(Q-m)H_aux(chi),
    H_old=X^(2m)Y_old,
    C_old=X^(2m)Y_old(chi)Psi^(14m).

Every complete factor and multiplicity is retained.
Y_old is monic and prime to Xphi, every occurring irreducible factor has multiplicity at least2, and both full forward divisibilities hold.
Retain all actual DG3/DG6 data, including C_old=beta^2B_src^(-2) modulo phi^(16m), with the specified cube-one beta, same auxiliary H_aux, selected exact triple fresh factor, canonical source remainder and positive gap.
Every numerical degree bound used must be the ACTUAL enlarged bound of that source.

Assume its endpoint is admissible and has the two reflected pairs:

    n=2d-5, gcd(n,15)=1,
    Dbar=P_(U_old)/(z^2+1), r=2d-2,
    delta_i=[z^i]Dbar for every i>=0,
    delta_0=delta_1=delta_2=delta_3=1,
    U_e=U_old B_n^2, d_e=3d-6.

Adopted C753 supplies actual inputs with these conditions for every Q in the stated range.
The source and the outer endpoint polynomial are distinct.
Let the full support size of Dbar be2k_support.
The unique nonzero even endpoint mask is J=1+z^2 and sigma=(1+z)^3(1+z^n).

For every monic integer T with Tbar=U_e,

    b_Tbar=0 modulo U_e,
    c_Tbar=0 modulo H_old B_n^2.

The latter assertion retains full SUMMED multiplicities at any overlap.
In R=F_2[X]/U_old put gamma_old=[U_e(chi)].
It is0 on all old X/Y primaries, while

    gamma_old=phi^(4m)C_old B_n(chi)^2
       =[phi^(2m)beta B_src^(-1)B_n(chi)]^2
                                                modulo phi^(14m).

Consequently gamma_old is a square in R and gamma_old^5=0.
The equality uses only the OLD source DG6 data and the actual outer square; it does not assume all source jets survive the arbitrary outer factor.

Fix any edge pattern eta=(eta_1,eta_2,eta_3) among (++-),(+-+),(-++),(---), and put eta_0=1.
Let I_ne={j:4<=j<d-1,delta_j=1}, of size k_support-4.
Use the ACTUAL reference

    L_eta=sum_(j=0)^3 eta_j(z^j+z^(r-j))
                 +sum_(j in I_ne)(z^j-z^(r-j)),
    L_eta^*=z^r L_eta(z^(-1)),
    P_eta=L_eta+z^(2n)L_eta^*,
    P_eta=z^(d_e)T_eta(z+z^(-1)).

All these trace indices are positive; T_eta is its genuine monic trace.
Set alpha_eta=[a_(T_eta)bar] in R.
Every height1 lift in this edge/mask fiber is obtained uniquely by flipping the k_support-4 nonedge pairs.
Both alpha_eta and delta_eta=gamma_old+alpha_eta are squares in R, and delta_eta=0 modulo X^4.

### C. Exact half-multiplicity image and sufficient full first-bit condition

For this part assume the EXTRA condition

    gcd(B_n,Y_old phi)=1.

Write the complete old factorization and define

    U_old=X^(2m) product_(psi!=X)psi^(e_psi),
    K=X^(m-1) product_(psi!=X)psi^ceil(e_psi/2),
    t=degK, I=(X) in F_2[X]/K.

Let S_4 be the space of square classes in R vanishing modulo X^4.
There is an exact F_2-linear isomorphism

    L_n:I -> S_4, [v] -> [c_n^2 v^2],
    dim I=dim S_4=t-1
         =sum_psi deg(psi)ceil(e_psi/2)-2,

where e_X=2m.
Let mu_eta be the UNIQUE preimage of the ACTUAL delta_eta.
For the fixed edge pattern, the stronger old-primary target a_Tbar=gamma_old is equivalent to the actual restricted affine system

    sum_(j in I_ne) epsilon_j[c_(d-1-j)]=mu_eta in I,
    epsilon_j in F_2.

If the column map has rank r_I and mu_eta is in its image, this system has exactly2^(k_support-4-r_I) sign solutions; otherwise it has none.
Full column span is sufficient for every one of the four edge patterns, but is not necessary for its particular target.

Every such solution gives BOTH full coefficientwise F_T=0 and X_(s,T)=0 modulo2 at the SAME T, for both signs.
This uses the stronger old target together with the already passing added B_n^2 mask and the stated coprimality.
It is NOT an iff characterization or count of ALL full first-bit residual solutions.
All these lifts avoid factors dividing z^(2n)-1, but irreducibility is not asserted.
At q=2^j, exact height1 descent retains the same base-sign problem and full reciprocal degree2q(3d-6).

The classes c_1,...,c_(t-1) form a basis of I, so actual supported representatives of such a basis would be sufficient.
A finite full companion period modulo K exists, with crude bound2^(4t), but its coverage by actual supported indices is an additional obligation.
The low-X period in C755 is not a period modulo K.
The unreduced ideal(X) modulo U_old has dimension d-1, exceeding the at most d-5 nonedge variables, so demanding span of that unreduced space is impossible.

### D. Shared-primary obstruction and complete-row gcd test

Without assuming the extra coprimality, let psi divide both B_n and Y_old and have old multiplicity e>=2.
For EVERY actual lift in the unique nonzero even mask,

    ord_psi(a_Tbar)=2.

Its full multiplicity in U_e is e+2, and b_Tbar=c_Tbar=0 modulo psi^(e+2).
Therefore

    full F_T even     => e<=8,
    full X_(s,T) even => e<=4.

For e>=9 the first residual has exact local order10 and fails; for e>=5 the second has exact local order6 and fails.
Both residual signs give the same binary conclusion.
The zero-mask cyclotomic family is separate.
Even the stronger target a_Tbar=gamma_old modulo U_old is impossible when a shared old factor has e>=3, although the weaker full residual equations at that factor can still survive for some smaller e.

Let M_rows be the lcm of all positive-exponent nontrivial ordinary-row indices and the ell_row indices of positive nontrivial divided rows B_(5ell_row)/phi in the COMPLETE old Y presentation, including the fresh cubic and all later rows.
Then

    gcd(B_n,Y_old phi)=1 iff gcd(n,M_rows)=1.

This uses gcd(n,15)=1 and full primitive-order partitions.
No actual original gcd is evaluated.

### E. Exact whole support and the limitation of the PX padding family

For the actual C755 padding parameters retain

    D_1=(1+z)^(4m-2)H(z), H(1)=1, degH<n_p,
    rho=4m-1=Q-9,
    D_*=H(z)(1+z^(n_p))^rho/(1+z),
    d_*=d_1+rho(n_p-1)/2.

Then the ordinary integer support count is EXACTLY

    wt(D_*)=Qn_p/4, k_*=Qn_p/8.

This counts ALL blocks, not merely the first dense run.
The full half-multiplicity square-target space has dimension at least d_*/2-2, and

    (d_*/2-2)-(k_*-4)
        =[(Q-18)n_p-2Q+4d_1+34]/8>0.

Thus, even when the extra gcd condition holds, all nonedge columns together CANNOT be onto the full target space of Part C.
This does not imply that any ACTUAL mu_eta is outside their image and does not affect C755's proved old-X surjectivity or exact local counts.

For the same actual parameters,

    gcd(n_e,n_p)=gcd(n_p,2d_1-Q+4), n_e=2d_*-5.

If nontrivial, the common row contributes an old multiplicity at least rho>=9, so Part D excludes both full residual conditions in every nonzero even mask.
The gcd is not asserted always nontrivial.

### F. Actual paid elimination of the full endpoint gcd

Start with an ACTUAL adopted C753 source of degree d_0 and pre-fresh exponent E_pre,0=0 modulo4.
Retain its same Q,m,L=4Q,e_pad=12Q,H_aux,B_src,beta,Z_0,n_star and exact triple fresh factor.
Let n_s=1+10L c_s, where c_s=1 if L=1 modulo3 and2 otherwise, and b_s=(n_s-1)/2<=40Q.
First form

    Y_1=Y_0 B_(n_s)^9, d_1=d_0+9b_s.

Define K_odd to be the lcm of5,7 and all complete primitive orders in this CURRENT Y_1 row presentation.
It is odd and prime to3, includes n_star and n_s, and does not depend on any later parameter.
Equivalently include all positive ordinary-row indices and full5ell_row indices of nontrivial positive divided rows.
Since36Q is a unit modulo K_odd, choose the unique integer s with0<=s<K_odd such that

    d_2=d_1+36Q s=3 modulo K_odd,
    Y_2=Y_1 B_7^(s e_pad).

Here s is an ordinary exponent selector, distinct from the residual sign.
Put

    rho=Q-9, c_0=2d_2-5,
    D_crit=c_0-rho=2d_2-Q+4>=14Q-116>0,
    K_X=ceil(m/3)-1,
    P_run=the least power of2 at least2K_X+1,
    A_len=2d_2-2+P_run,
    B_step=30L K_odd,
    c_pad=D_crit ceil(A_len/(B_step D_crit)),
    n_pad=1+B_step c_pad, b_pad=(n_pad-1)/2,
    Y_*=Y_2 B_(n_pad)^rho,
    U_*=X^(2m)Y_*phi^(14m), d_*=d_2+rho b_pad,
    n_e=2d_*-5.

These are actual complete polynomial extensions with no circular parameter choice.
They satisfy

    E_pre,*=0 modulo4, gcd(n_e,15)=1,
    gcd(n_e,K_odd n_pad)=1,
    gcd(B_(n_e),Y_*phi)=1.

All complete original source conditions, both forward divisibilities, floor2, the same exact fresh3, full DG3/DG6/root data, derivative divisibility, nonzero actual canonical binary source remainder and positive gap are retained.
The source endpoint still has exactly two mask dimensions.
This genuinely pays the gcd premise of Part C; it supplies no actual image membership.

The exact new costs from the C753 input are

    Delta_total=9b_s+36Q s+rho b_pad,
    degY_*=degY_0+Delta_total,
    d_*=d_0+Delta_total,
    degR_*=degR_0+Delta_total,
    d_2<=d_0+360Q+36Q(K_odd-1),
    n_pad<1+A_len+B_step D_crit,
    d_*<d_2+(rho/2)(A_len+B_step D_crit).

These finite costs use the ACTUAL K_odd and d_2.
They are not assigned C691's original DG8 budget, C753's396Q increment or C755's polynomial-in-Q coarse bound.
The full source gap remains m-8-5degH_aux>5m/256.
At raised q, source degrees and gap multiply by q, source reciprocal degree is2q d_*, and the further outer endpoint reciprocal degree is2q(3d_*-6).
The same maximal Frobenius exponent, integer layer vector and zero strict-window correction are retained with their actual full factors and new degree.
The synthetic integer polynomial gains the complete trace factors of the three displayed added rows, counting all multiplicities; it remains distinct from the actual integer canonical G_T.
The full source preservation concerns U_* BEFORE the arbitrary outer B_(n_e)^2.

This repaired family still has rho=Q-9 and meets Part E's full-support hypotheses with d_1 replaced by d_2.
Thus k_*=Qn_pad/8 exactly and uniform surjectivity still fails.
No actual target nonattainment, full old-primary height1 realization, irreducibility, higher precision, controlled total Mahler measure, characteristic-zero identity or unrestricted G0001 conclusion is asserted.

## Complete argument

<a id="full-old-primary-square-target-and-image"></a>
### Full old-primary square targets, exact sign images and two concrete limitations

This is the complete fixed author argument by root and characteristic_zero_bridge, separate from the continuing old-X system and certificate inquiry in D6.
Root proposed the repeated-primary square property, the full old-primary target and the whole-support count for the dense padding family.
Characteristic_zero_bridge checked the actual integer carry, derived the exact half-multiplicity quotient and target count, and proved the shared-primary obstruction and the precise padding dimension deficit below.
The actually consumed fixed inputs are [C736 FT2's integral product rule](Yin_C_G0736_v1.md#complete-argument), [C691 DG3--DG6](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24), [C747's full mask/own-divisor carry](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25), and [adopted C753's paid admissible complete source](Yin_C_G0753_v1.md#decision-whole-reviewed-2026-10-25).
The final comparison reads the exact PX padding formulas in [adopted C755](Yin_C_G0755_v1.md#decision-whole-reviewed-2026-10-25), and proves the new whole-support count directly rather than importing any all-old-primary assertion or independent review from that separate old-X result.
No native support expansion, matrix rank, actual finite target or shared-factor gcd has been evaluated.

#### Repeated binary primary factors force the canonical first remainder to be a square

Let U=product_psi psi^(e_psi) be any monic binary polynomial with EVERY e_psi>=2.
For each distinct monic irreducible psi choose an arbitrary monic integer lift P_psi and put T_0=product_psi P_psi^(e_psi).
For an integer polynomial A write Delta(A)=[A(C_2)-A^2]/2, C_2=X^2-2.
This is an actual integer polynomial, and a_T=rem_T Delta(T) for each monic integer T.
The integral product rule reduces to

    Deltabar(AB)=Abar^2 Deltabar(B)+Bbar^2 Deltabar(A).

Induction, before any quotient is taken, gives

    Deltabar(T_0)=sum_psi (e_psi mod2)
        psi^(2e_psi-2) Deltabar(P_psi)
        product_(eta!=psi) eta^(2e_eta).        (OP1)

For even e_psi the corresponding term is zero.
For odd e_psi>=3, 2e_psi-2>=e_psi; the other primary factors occur to twice their required orders.
Thus U divides EVERY surviving term and a_(T_0)bar=0 in F_2[X]/U.

Every monic integer T with Tbar=U is uniquely T=T_0+2V with degV<degU.
The EXACT integer identity is

    Delta(T_0+2V)=Delta(T_0)+V(C_2)-2T_0V-2V^2.

Monic division commutes with reduction at the SAME binary divisor U, so

    a_Tbar=Vbar^2 in F_2[X]/U.                  (OP2)

In particular every actual canonical a_Tbar is a square class.
Conversely every square class occurs among unrestricted monic integer trace lifts by choosing a degree-bounded integer lift V.
This converse imposes no height1 or restricted reciprocal-support condition and supplies no such sign solution.

#### A concrete square target on every OLD primary

Use an actual complete original or paid source

    U_old=X^(2m)Y_old phi^(14m), d=degU_old,
    phi=X^2+X+1, chi=Xphi^2,
    H_old=X^(2m)Y_old, B_src=X^(Q-m)H_aux(chi),

with Q=2^ell, ell>=82, m=Q/4-2, all irreducible multiplicities of Y_old at least2, Y_old prime to Xphi, both full forward divisibilities, and the complete retained DG6 identities.
The C753 source is an actual such input with the admissible e=2 endpoint.
More generally explicitly assume that endpoint here, so

    n=2d-5, gcd(n,15)=1,
    U_e=U_old B_n^2, d_e=3d-6,
    delta_0=delta_1=delta_2=delta_3=1.

The endpoint's unique nonzero even mask is J=1+z^2 with sigma=(1+z)^3(1+z^n).
Let gamma_old be the class of U_e(chi) in R=F_2[X]/U_old.

Since U_old|U_old(lambda) and B_n|B_n(lambda), lambda=X^3+X, one has U_e|U_e(lambda).
Thus every actual T with Tbar=U_e has b_Tbar=0 in the FULL quotient by U_e.
Also the forward divisibilities give

    H_old B_n^2 | U_e(chi).

This retains the SUM of multiplicities at overlaps: the two full polynomial divisibilities multiply before taking any primary quotient.
Consequently the actual c_Tbar vanishes on the full H_old B_n^2 component, and gamma_old=0 on every old X/Y primary.

Write C_old=X^(2m)Y_old(chi)Psi^(14m), Psi=phi(chi).
The retained DG6 identity gives, at the full old phi-primary,

    gamma_old=phi^(4m) C_old B_n(chi)^2
             =[phi^(2m) beta B_src^(-1) B_n(chi)]^2
                                                   modulo phi^(14m),
    C_old=beta^2 B_src^(-2) modulo phi^(16m).    (OP3)

Every inverse in this display is in the phi-unit algebra.
Because n is coprime5, B_n(chi) is a phi-unit: chi=0 modulo phi and B_n(0)=1.
Therefore gamma_old is a square in R by CRT, its phi-order is exactly4m, and

    gamma_old^5=0 in R.                        (OP4)

This conclusion does not require the arbitrary outer B_n^2 to preserve all DG3/DG6 jets of the NEW polynomial U_e.
It uses the OLD source's actual DG6 data and the explicit square B_n(chi)^2.

Fix any one of C755 PX5's four edge patterns (++-),(+-+),(-++),(---), and take the actual integer reference lift with that edge pattern and all remaining pair signs fixed as in C755 PX5.
Let alpha_ref be its OWN a_Tbar reduced in R.
All multiplicities of U_e are at least2, so OP2 makes alpha_ref square.
C747's own-divisor jet gives alpha_ref=0 modulo X^3 because J(1)=0.
A square modulo X^(2m) has only even coefficients below that precision, so in fact alpha_ref=0 modulo X^4.
Thus the actual difference

    delta=gamma_old+alpha_ref

is a square in R and vanishes modulo X^4.
No reference coefficient is replaced by a freely chosen error representative.

#### The exact half-multiplicity quotient, rather than an unpaid full period

For this subsection assume the explicit additional condition

    gcd(B_n,Y_old phi)=1.                      (OP5)

Write the COMPLETE old primary factorization as

    U_old=X^(2m) product_(psi!=X) psi^(e_psi),
    K_0=X^m product_(psi!=X) psi^ceil(e_psi/2),
    K=X^(m-1) product_(psi!=X) psi^ceil(e_psi/2),
    t=degK.

The factors and exponents are those of the actual enlarged Y_old, including all overlaps and phi.
The kernel of f -> f^2 in R is exactly the ideal generated by K_0: U_old|f^2 if and only if K_0|f.
Hence squaring gives an F_2-linear bijection from F_2[X]/K_0 to the square classes of R.

Let I=(X) in F_2[X]/K, and let S_4 be the subspace of square classes in R whose X-primary component is divisible by X^4.
The exact binary identity c_n=C_nbar=XB_n^2, with B_n(0)=1, and OP5 imply the F_2-linear ISOMORPHISM

    L_n:I -> S_4,
    [v] -> [c_n^2 v^2],
    dim I=dim S_4=t-1
         =sum_psi deg(psi)ceil(e_psi/2)-2.      (OP6)

Here e_X=2m and degX=1.
For the proof, the required divisibility on X is 2+2ord_X(v)>=2m, so the kernel exponent is m-1.
On each other old primary c_n is a unit, and the kernel exponent is ceil(e_psi/2).
These are precisely K.
For surjectivity, the unique square root of an S_4 class modulo K_0 is divisible by X^2 at X.
Divide it by c_n=XB_n^2: at X this leaves a unique class modulo X^(m-1) divisible by X, and at every other primary division is by a unit.
CRT gives exactly one class in I.
Thus the ACTUAL delta above has a unique preimage mu in I; this is an existence and uniqueness statement for a quotient class, not an evaluated coefficient vector.

The full old degree is d, while this target dimension is at least d/2-2.
The formerly proposed demand to span the unreduced ideal(X) in F_2[X]/U_old would require dimension d-1.
There are at most d-5 nonedge sign variables, so that unreduced spanning condition is impossible.
The square kernel must first be removed as in OP6; replacing it by an unexplained full-period condition does not repair that dimension error.

#### Exact restricted image condition and what it would prove

Let Dbar=P_(U_old)/(z^2+1), of degree2d-2, and let

    I_ne={j:4<=j<d-1, [z^j]Dbar=1},
    |I_ne|=k_support-4.

These are the ACTUAL nonedge pair positions, not every index in their interval.
C755 PX5's integer trace conversion and genuine changing-divisor carry give exactly

    a_Tbar=alpha_ref+
       sum_(j in I_ne) epsilon_j c_n^2 c_(d-1-j)^2 in R.

Therefore the stronger old-primary target a_Tbar=gamma_old is equivalent to

    sum_(j in I_ne) epsilon_j [c_(d-1-j)]=mu
                          in I=(X) modulo K.   (OP7)

This is a complete finite F_2 affine interface with the true canonical target and all full source multiplicities retained.
Let r_I be the rank of its actual column map.
For the fixed edge pattern there are exactly2^(k_support-4-r_I) sign solutions if mu lies in its image, and zero otherwise.
If the columns span I, every one of the four permitted edge patterns has a solution to its own actual target.
A numerical rank or any particular target membership is NOT evaluated.

Every sign solution of OP7 gives BOTH F_Tbar=0 and X_(s,T)bar=0 on the full OLD U_old: b_Tbar=0, a_Tbar=c_Tbar there, and gamma_old^5=0.
Every member of the chosen mask already passes both residual conditions modulo the added B_n^2.
Under OP5 these moduli are coprime, so CRT gives

    F_T=0 and X_(s,T)=0 modulo2
        at the SAME full divisor T, for both s. (OP8)

The count in OP7 is for the STRONGER target a_Tbar=gamma_old, not an iff count of every full first-bit solution.
Nilpotent old components and the other cube-root branches may allow additional solutions to the residual equations.
The four edge patterns retain absence of factors dividing z^(2n)-1, but this alone is not irreducibility.
Every resulting full reciprocal degree is2(3d-6), and raised q=2^j height1 descent has full degree2q(3d-6), with the same base signs and own canonical conditions.

A concrete sufficient image test would be that the actual nonedge classes contain a basis of I.
The classes c_1,...,c_(t-1) are one such basis: each polynomial is monic of its degree, has zero constant term, and the coefficient matrix is triangular.
Alternatively a proved full companion period modulo K, actually covered by supported nonedge indices, would suffice.
For A=[[X,1],[1,0]] over F_2[X]/K, detA=1 and c_j=tr(A^j), so a finite matrix period exists; the crude bound2^(4t) follows just by counting all2-by2 matrices.
This existence neither provides supported indices nor pays the period in a new source.
The low-X period in C755 is only modulo its low-X power and cannot be applied modulo K.

#### Shared old factors give an actual canonical obstruction

Return to the full endpoint and DO NOT assume OP5.
Let psi be a common irreducible factor of B_n and Y_old, with old multiplicity e>=2.
Because n is coprime15, this is neither X nor phi.
The complete B_n is squarefree, so its multiplicity in U_e is e+2.

At a reciprocal root zeta of psi one has zeta^n=1 and zeta!=1.
Set v=1+z^n and u=z^(2n).
The zero of v is simple because n is odd, and zeta+1 and u(zeta) are units.
For every actual height1 member of the unique nonzero even mask, C747 MP11 is the GLOBAL identity

    Delta_z(P)bar
      =v^4 Deltabar_L+u^2 sigma^2+u v^2 Dbar^2,
    sigma=(1+z)^3v.                            (OP9)

At zeta the middle term has EXACT order2.
The first has order at least4, while Dbar has order e there, so the third has order at least2+2e>=6.
Thus no leading cancellation is possible and ord_zeta Delta_z(P)bar=2, independently of all allowed signs.

The trace map z -> z+z^(-1) is unramified at zeta: its derivative is1+zeta^(-2), nonzero since zeta!=1 in characteristic2.
The exact integer trace identity Delta_z(P)=z^(2d_e)Delta_T(z+z^(-1)) therefore transfers this order2 to the trace root.
The difference between Delta_Tbar and the OWN canonical a_Tbar is divisible by U_e, of order e+2>=4 there.
Consequently

    ord_psi(a_Tbar)=2.                         (OP10)

This is an exact order, not just the added-modulus vanishing condition.
The earlier full forward argument gives b_Tbar=c_Tbar=0 modulo psi^(e+2).
Hence full first-bit evenness forces respectively

    full F_T even       => e+2<=10, hence e<=8,
    full X_(s,T) even   => e+2<=6,  hence e<=4.  (OP11)

If e+2 exceeds the displayed threshold, the corresponding residual has exact local order10 or6 and cannot vanish modulo U_e.
Both residual signs have the same binary condition.
Thus a shared old factor of multiplicity at least5 rules out every full second-residual solution in this nonzero even mask; multiplicity at least9 rules out the first residual as well.
The zero-mask cyclotomic family is separate.
These are sufficient local obstructions, not a universal exclusion of every endpoint source, and smaller shared multiplicities are not declared harmless at all other primaries.

Even the STRONG target a_Tbar=gamma_old can fail before OP11 applies: if a shared old factor has e>=3, OP10 has nonzero order2 modulo psi^e while gamma_old vanishes there.
The corresponding nonedge columns all contain B_n^4, so they cannot remove this pinned order2.
This explains why OP5 cannot be silently omitted from OP7--OP8.

For a retained complete row presentation, OP5 itself has a finite integer form.
Take M_rows to be the lcm of every positive-exponent ordinary-row index and every positive-exponent divided-row index ell_row from B_(5ell_row)/phi, including the fresh cubic and all later rows, but ignoring trivial rows.
Then, since n is already prime to5,

    gcd(B_n,Y_old phi)=1
        iff gcd(n,M_rows)=1.                   (OP12)

Indeed ordinary B_r shares a nonidentity trace with B_n exactly when gcd(n,r)>1.
The divided row consists of the complete orders d and5d for d|ell_row,d>1; since5 does not divide n, its intersection is equivalent to gcd(n,ell_row)>1.
All multiplicities remain relevant to OP11, even though they do not affect this gcd test.

#### Exact total support of the PX padding family and its dimension deficit

Use the EXACT PX parameters, independently of any future source modification:

    D_1=(1+z)^(4m-2)H(z), H(1)=1,
    degH=2d_1-2-(4m-2)<n_p,
    rho=4m-1=Q-9,
    D_*=H(z)(1+z^(n_p))^rho/(1+z),
    d_*=d_1+rho(n_p-1)/2.

All of these are full polynomials, not truncated low blocks.
The integer rho is odd.
Write (1+t)^rho=sum_i b_i t^i.
Its coefficients occur in equal pairs b_(2r)=b_(2r+1), since (1+t)^rho=(1+t)(1+t^2)^((rho-1)/2).
Every nonzero pair contributes the shifted polynomial

    z^(2r n_p) H(z)(1+z^(n_p))/(1+z).

Its degree is less than2n_p.
If f_j=sum_(i=0)^j [z^i]H, then for0<=j<n_p the two length-n_p blocks have coefficients f_j and1+f_j, because degH<n_p and H(1)=1.
They therefore contain exactly n_p ones in total.
The apparent truncated tail of the last block is already zero, since f_j=1 for j>=degH.
Distinct pairs have disjoint length-2n_p supports, so

    wt(D_*)=n_p wt((1+t)^rho)/2.                (OP13)

Here wt is the ordinary integer number of nonzero binary coefficients.
Since rho=2^ell-9 has all ell binary digits1 except digit3, the exact factorization

    (1+t)^rho=product_(0<=i<ell,i!=3)(1+t^(2^i))

has2^(ell-1)=Q/2 distinct subset exponents, with no cancellation.
Thus the ACTUAL full support and low-pair count are

    wt(D_*)=Q n_p/4, k_*=Q n_p/8.              (OP14)

This uses all blocks, not just PX's first consecutive run.
In particular all nonedge sign columns together number k_*-4.

For this enlarged old source, the S_4 space of OP6 has dimension at least d_*/2-2.
Even if OP5 holds, that dimension is STRICTLY larger than all k_*-4 nonedge variables, because

    (d_*/2-2)-(k_*-4)
      =[(Q-18)n_p-2Q+4d_1+34]/8>0.             (OP15)

For example n_p>=3, Q>=32 and d_1>=1 already make the displayed numerator positive; the actual source range is much larger.
Therefore the entire PX nonedge map CANNOT be onto this full half-multiplicity target space.
No enlargement of its one low-X run or appeal to its other existing support blocks can turn this PARTICULAR padding family into uniform surjectivity.
This does not prove that its ACTUAL mu is outside the image, and does not affect C755's genuine low-X surjectivity or sign counts.

The same actual parameters expose a separate gcd test with the newly added full row:

    gcd(n_e,n_p)=gcd(n_p,2d_1-Q+4),
    n_e=2d_*-5.

If this gcd is nontrivial, some common complete old primary has multiplicity at least rho=Q-9>=9.
OP11 then rules out BOTH full residual conditions in every nonzero even endpoint mask for that source, independently of the low-X solution.
The gcd has not been evaluated, and it is not asserted always nontrivial.

The remaining existence problem is precise: supply an ACTUAL complete source with paid degrees and retained fresh3 for which the required shared-primary tests pass and one of the TRUE targets in OP7 lies in the actual restricted image, or find a different fully priced mechanism.
A full companion period depends on the enlarged source's root orders and primary multiplicities; the new B_(n_p) alone forces a companion period modulo its primitive root component to be a multiple of n_p, and nilpotent precision must also be retained.
Thus increasing n_p and using only a run of length<n_p is self-referential, not a solution.
The exact support deficit above strengthens that limitation for the present PX family without claiming actual target nonattainment.
No all-old-primary height1 existence, irreducibility, higher precision, characteristic-zero identity or Mahler conclusion is asserted.

<a id="paid-full-row-coprimality-repair"></a>
### A separately paid complete-source repair of the full endpoint gcd

This is the complete fixed paid-gcd argument proposed by root and checked by characteristic_zero_bridge after OP1--OP15.
It changes the padding parameters and budgets; it does not modify C755's fixed old-X statement or claim full old-primary feasibility.
The construction shows that OP5's gcd premise can be achieved on an ACTUAL complete source while retaining the same fresh factor and all source data.
It leaves the precise image/target obligation unresolved, and its unchanged rho retains the negative dimension result.

Start with an actual adopted C753 source U_0=X^(2m)Y_0phi^(14m), degree d_0, E_pre,0=0 modulo4 and gcd(2d_0-5,15)=1.
Retain Q,m,L=4Q,e_pad=12Q,H_aux,B_src,beta,Z_0 and the original selected n_star with exact triple psi_star.
First apply the small invisible row B_(n_s)^9 from C751/PX:

    b_s=(n_s-1)/2<=40Q,
    Y_1=Y_0 B_(n_s)^9,
    d_1=d_0+9b_s, E_pre,1=1 modulo4.           (GC1)

Its degree increment is0 modulo15, it preserves every complete source condition and it misses the selected fresh factor.

Define K_odd NOW, before choosing any later parameter, to be the lcm of5,7 and all complete primitive orders occurring in the retained whole-row presentation of Y_1.
Equivalently one may include each positive ordinary-row index and the full5ell_row index of each nontrivial positive divided row.
The trivial divided row is1 and need not be included.
All these integers are odd and prime to3; K_odd includes n_star and n_s.
Adding7 in advance accounts for the next ordinary factor without any circular dependence on its exponent.
Thus gcd(36Q,K_odd)=1.

Choose the unique ordinary integer s with0<=s<K_odd such that

    d_2=d_1+36Q s=3 modulo K_odd,
    Y_2=Y_1 B_7^(s e_pad).                     (GC2)

This is an actual finite choice by inversion of36Q modulo K_odd.
The new B_7 factor is invisible in the full source ring by UC1 and misses n_star because7<n_star.
If s>0, its exponent is at least2.
It leaves E_pre,2=1 modulo4 and leaves d_2=d_1 modulo3.
Writing c_0=2d_2-5 gives c_0=1 modulo K_odd and c_0!=0 modulo3.
In particular the new degree is also admissible modulo5.

Put rho=4m-1=Q-9 and

    D_crit=c_0-rho=2d_2-Q+4,
    K_X=ceil(m/3)-1,
    P_run=the least power of2 at least2K_X+1,
    A_len=2d_2-2+P_run,
    B_step=30L K_odd,
    c_pad=D_crit ceil(A_len/(B_step D_crit)),
    n_pad=1+B_step c_pad,
    b_pad=(n_pad-1)/2.                         (GC3)

All parameters are chosen in this order, so K_odd and D_crit do not depend on n_pad.
The quantity D_crit is positive: d_2>=30m gives D_crit>=14Q-116>0.
The index n_pad is odd,1 modulo15,1 modulo10L,1 modulo n_star,1 modulo K_odd and1 modulo D_crit.
Also n_pad-1>=A_len.
Consequently it supplies PX's complete low support run, is a legitimate full invisible ordinary row, and contains no original primitive-order-n_star factor.

Form the ACTUAL complete source

    Y_*=Y_2 B_(n_pad)^rho,
    U_*=X^(2m)Y_*phi^(14m), d_*=d_2+rho b_pad,
    n_e=2d_*-5=c_0+rho(n_pad-1).               (GC4)

The full ordinary exponent satisfies E_pre,*=1+rho=0 modulo4.
One has n_e=1 modulo K_odd and n_e=c_0 modulo3, hence gcd(n_e,15)=1.
Furthermore

    gcd(n_e,n_pad)=gcd(c_0-rho,n_pad)
                 =gcd(D_crit,n_pad)=1.

Every root order of Y_2 divides K_odd; every newly added root order divides n_pad.
The complete row criterion OP12 therefore proves

    gcd(B_(n_e),Y_*phi)=1.                     (GC5)

This is an actual all-old-primary gcd guarantee, not merely absence of the selected fresh factor.
The full endpoint mask still has e=2 by the unchanged exponent-class calculation.

All three additions are complete ordinary rows, invisible at X^(8m)phi^(16m), with each positive exponent at least2.
They retain both global forward divisibilities, the floor2, the same exact triple psi_star, all DG3/DG6 jets and root data, and X^(8m)|Y_*'.
The actual all-primary canonical recomputation is the same as UC8--UC9: with R_*=X^(2m)Y_*phi^(12m)B_src one has R_*=rem_(U_*)(U_*(chi)^3)!=0 and the unchanged gap m-8-5degH_aux>5m/256.
The source maximal Frobenius exponent, full raised reciprocal degree, layer vector and zero strict-window correction remain unchanged in meaning, with the new full degree used.
The actual synthetic integer polynomial is multiplied by the complete trace factors for B_(n_s)^9, B_7^(s e_pad) and B_(n_pad)^rho, with all overlapping multiplicities added; it is not identified with the integer canonical G.

The exact paid degree increment from the C753 input is

    Delta_total=9b_s+36Q s+rho b_pad,
    degY_*=degY_0+Delta_total,
    d_*=d_0+Delta_total,
    degR_*=degR_0+Delta_total.                 (GC6)

In particular d_2<=d_0+360Q+36Q(K_odd-1), and the exact ceiling choice gives

    n_pad<1+A_len+B_step D_crit,
    d_*<d_2+(rho/2)(A_len+B_step D_crit).

These are fully specified FINITE new costs in the actual K_odd and d_2.
They are not assigned either C691's DG8 budget, C753's396Q increment or C755's polynomial-in-Q coarse numerical bound.
At raised q all source degrees and the full gap are multiplied by q, with source reciprocal degree2q d_*.
The further endpoint polynomial U_e=U_*B_(n_e)^2 has trace degree3d_*-6 and full reciprocal degree2q(3d_*-6).
As before, the complete source preservation just proved belongs to U_* before that arbitrary outer endpoint factor.

This construction also meets the exact hypotheses of the whole-support calculation OP13--OP15, with d_1 there replaced by the present d_2 and n_p by n_pad.
Indeed D_2=(1+z)^(4m-2)H with H(1)=1 and degH<n_pad, and rho remains Q-9.
Thus k_*=Q n_pad/8 exactly and the available nonedge columns still cannot be onto the full half-multiplicity target space.
The gcd obstacle has been constructively removed; the actual target may or may not lie in the smaller image.
No rank, target membership, full old-primary height1 solution, irreducibility, controlled Mahler measure or characteristic-zero identity is asserted.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision full-primary-interface-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T22:06 |
| status | open |
| reason | Register the complete OP1--OP15 and GC1--GC6 author theorem after root read both entire saved arguments. The general repeated-primary square property gives a genuine full old-primary target and an exact half-multiplicity restricted sign-image interface; shared factors force an actual order2 obstruction, and the entire PX support has a precise dimension deficit. A separate fully paid complete-source construction removes the endpoint gcd obstacle without removing that deficit or establishing actual target membership. Root and characteristic_zero_bridge are contributors, not independent reviewers; fresh isolated whole review and separate adoption were still outstanding at author registration. The adopted C755 review is not borrowed for this new mathematics. No full old-primary sign solution, irreducibility, original Mahler control or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete full-primary interface and paid-gcd theorem](#statement) | Parts A--F: general repeated-primary square property; complete source and actual target; exact half-multiplicity quotient, restricted image and sufficient first-bit implication; shared-order obstruction; exact total padding support and dimension limit; actual paid gcd repair with all costs and realization exclusions. |
| argument | [Entire OP1--OP15 and GC1--GC6 proof](#complete-argument) | Actual integer Delta carries and primary exponents, full old target and unique quotient preimage, genuine supported signs/counts, full shared-primary order transfer, complete row gcd, all padding blocks and dimension calculation, noncircular paid parameters, every retained source condition and new fee. |
| dependency | [Adopted exact canonical integer product interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT2 actual integral Delta product rule and monic reduction, including shared factors. The general floor2 square-class consequence is proved here rather than imported from its factor-quotient statement. |
| dependency | [Adopted complete original source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | Complete DG3--DG6 data, multiplicity floor, both forward maps, actual C_old square/unit formula at phi16m, original auxiliary/fresh-factor/gap and full synthetic-layer meanings. Enlarged sources retain their own actual degrees. |
| dependency | [Adopted endpoint mask and own-divisor global carry](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) | Structural a=d-3 mask with two reflected pairs, unique nonzero even J, actual X3 jet, MP11 full reciprocal carry and trace transfer, added-modulus conditions with overlap, and exact raised height1 descent. Its old numerical bound and full global feasibility are not inferred. |
| dependency | [Adopted complete row and invisible class control](Yin_C_G0751_v1.md#decision-whole-reviewed-2026-10-25) | Exact pre-fresh convention, low reciprocal class, small invisible ordinary row with exponent9, complete full-source reconstruction, primitive-order partition and synthetic-factor/layer scopes. |
| dependency | [Adopted paid admissible complete source](Yin_C_G0753_v1.md#decision-whole-reviewed-2026-10-25) | Actual source for every Q>=2^82 with E_pre=0 and admissible two-dimensional endpoint, original full source/fresh/gap data, safe B7 exponent and396Q fee. The GC construction pays its NEW separate degrees. |
| dependency | [Adopted dense-support old-X construction](Yin_C_G0755_v1.md#decision-whole-reviewed-2026-10-25) | PX2--PX3 exact complete padding parameters and full D_*=H(1+z^n)^rho/(1+z), plus PX5 actual reference/sign/canonical carry and four edge patterns, structurally applied with the actual retained source. The full-support count, half-multiplicity dimension obstruction and paid gcd modification are new here; its review and numerical bound do not extend to them. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T22:15 |
| status | proved |
| reason | Register the complete OP1--OP15 and GC1--GC6 author theorem after root read both entire saved arguments. The general repeated-primary square property gives a genuine full old-primary target and an exact half-multiplicity restricted sign-image interface; shared factors force an actual order2 obstruction, and the entire PX support has a precise dimension deficit. A separate fully paid complete-source construction removes the endpoint gcd obstacle without removing that deficit or establishing actual target membership. Adopt fresh isolated whole R976 after root read all OP1--OP15 and GC1--GC6, the fixed standalone Parts A--F and exact dependency scopes, then the entire independent finding. Root and characteristic_zero_bridge remain contributors. The reviewer supplied no repair; all actual canonical, quotient, support, obstruction and paid source obligations passed with the strong-target and unknown-membership boundaries preserved. The adopted C755 review is not borrowed for this new mathematics. No full old-primary sign solution, irreducibility, original Mahler control or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete full-primary interface and paid-gcd theorem](#statement) | Parts A--F: general repeated-primary square property; complete source and actual target; exact half-multiplicity quotient, restricted image and sufficient first-bit implication; shared-order obstruction; exact total padding support and dimension limit; actual paid gcd repair with all costs and realization exclusions. |
| argument | [Entire OP1--OP15 and GC1--GC6 proof](#complete-argument) | Actual integer Delta carries and primary exponents, full old target and unique quotient preimage, genuine supported signs/counts, full shared-primary order transfer, complete row gcd, all padding blocks and dimension calculation, noncircular paid parameters, every retained source condition and new fee. |
| dependency | [Adopted exact canonical integer product interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT2 actual integral Delta product rule and monic reduction, including shared factors. The general floor2 square-class consequence is proved here rather than imported from its factor-quotient statement. |
| dependency | [Adopted complete original source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | Complete DG3--DG6 data, multiplicity floor, both forward maps, actual C_old square/unit formula at phi16m, original auxiliary/fresh-factor/gap and full synthetic-layer meanings. Enlarged sources retain their own actual degrees. |
| dependency | [Adopted endpoint mask and own-divisor global carry](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) | Structural a=d-3 mask with two reflected pairs, unique nonzero even J, actual X3 jet, MP11 full reciprocal carry and trace transfer, added-modulus conditions with overlap, and exact raised height1 descent. Its old numerical bound and full global feasibility are not inferred. |
| dependency | [Adopted complete row and invisible class control](Yin_C_G0751_v1.md#decision-whole-reviewed-2026-10-25) | Exact pre-fresh convention, low reciprocal class, small invisible ordinary row with exponent9, complete full-source reconstruction, primitive-order partition and synthetic-factor/layer scopes. |
| dependency | [Adopted paid admissible complete source](Yin_C_G0753_v1.md#decision-whole-reviewed-2026-10-25) | Actual source for every Q>=2^82 with E_pre=0 and admissible two-dimensional endpoint, original full source/fresh/gap data, safe B7 exponent and396Q fee. The GC construction pays its NEW separate degrees. |
| dependency | [Adopted dense-support old-X construction](Yin_C_G0755_v1.md#decision-whole-reviewed-2026-10-25) | PX2--PX3 exact complete padding parameters and full D_*=H(1+z^n)^rho/(1+z), plus PX5 actual reference/sign/canonical carry and four edge patterns, structurally applied with the actual retained source. The full-support count, half-multiplicity dimension obstruction and paid gcd modification are new here; its review and numerical bound do not extend to them. |
| review | [Fresh independent whole full-primary and paid-gcd review](../audits/reviews/Yin_R_G0976_v1.md#whole-full-primary-and-paid-gcd-finding) | Entire fixed Parts A--F and OP1--OP15/GC1--GC6, all actual integer carries and primary multiplicities, exact target/image/count, shared-factor and whole-support limitations, noncircular paid gcd repair and full retained source/cost/raised scope; independently reviewed with exact statement and argument bindings. |

