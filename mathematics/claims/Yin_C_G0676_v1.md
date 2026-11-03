---
author: Yin
---

# Balanced forward multiplicities permit simultaneous modulo-four lifts

Human author Yin.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
This entire statement and proof are initially open for fresh isolated whole mathematical review.

<a id="balanced-square-mod-four-extension"></a>
Root proposed replacing C672's strong forward hypotheses by quantitative root-multiplicity inequalities, and strengthening the partial-H padding accordingly.
Original_law checked the actual integer divisions, both non-phi residuals, the complete phi half-error and counts, and the full partial-H degree/application scope below.
Both are contributors, not independent reviewers of this new extension.
The exact question is whether the SAME actual integer T can satisfy both residuals modulo4 when strong C3 is impossible for the chosen partial H.
The proof is analytic, with no new native calculation, parameter scan or child agent.

The exact adopted inputs are [C669](Yin_C_G0669_v1.md#decision-whole-reviewed-2026-10-24), for its actual local same-divisor calculation, and [C672](Yin_C_G0672_v1.md#decision-whole-reviewed-2026-10-24), for the square-base half-remainder and coefficient calculation.
The [adopted C674 construction](Yin_C_G0674_v1.md#decision-whole-reviewed-2026-10-24) supplies the partial-H application at its complete fixed mathematical scope.
The generic theorem below has its own explicit polynomial hypotheses and does not assume any C674 existence result.
The application repeats and proves the new padding inequalities, retaining every earlier cost and realization boundary.

<a id="balanced-square-mod-four-statement"></a>
## Statement

Let A>=2 be even, put Phi=X^2+X+1 over Z, phi=Phi modulo2, chi=Xphi^2 and Psi=phi(chi).
Let Y in F_2[X] be a monic square prime to Xphi, set

    H_0=X^A Y, U=H_0phi^(7A),
    h=degH_0, d=degU=h+14A,
    C_0=X^A Y(chi)Psi^(7A),

and assume the following EXACT polynomial and high-primary identities:

    H_0^3 divides H_0(X^3+X)^4,
    H_0 divides H_0(chi)^2,
    H_0^6=C_0^21 modulo phi^(4A).                        (BS1)

The divisibilities count the full local multiplicity of each actual pullback, including any critical preimage.
Neither H_0|H_0(X^3+X) nor H_0|H_0(chi) is assumed.
All irreducible multiplicities N_psi in H_0 are even and at least2.
Choose monic integer lifts P_psi with P_X=X and define the ACTUAL square base and its half-support polynomial by

    mathcal_H=product_(psi|H_0)P_psi^(N_psi)=X^A mathcal_Y,
    J_H=product_(psi|H_0)psi^(N_psi/2), j_H=h/2.

Let Z be the unique unit eleventh root of H_0C_0^2 modulo phi^(3A).
For an integer polynomial K with k=Kbar satisfying

    k=Z modulo phi^(3A), J_H|k, degK<d-2A,

and any integer W of degree<d, set

    T=mathcal_H Phi^(7A)+2Phi^A K+4W.                    (BS2)

This is monic of degree d with reduction U.
Define its actual monic integer divided remainders, with ONE common divisor T, by

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a=rem_T(T(C_2))/2, b=rem_T(T(C_3))/3,
    c=rem_T(T(C_5))/5,
    F(T)=rem_T(2c^2-3a^5),
    X_s(T)=rem_T(b^2-a^3+s(c^3-2b^5)), s in{1,-1}.

Every divided remainder is integral.
All congruences below concern the coefficients of these actual canonical remainders.

### A. Complete simultaneous criterion and counts

For EVERY allowed K and EVERY W, F(T)=0 modulo4, and X_s(T) is even.
Both residuals already vanish modulo4 on every non-phi primary.
More precisely, on those primaries a is even, b^2=0 modulo4, 2c^2=0 modulo4 and c^3=0 modulo4.
The reductions bbar,cbar themselves need not be zero there.
At phi one still has bbar=0, so b^2=0 modulo4 holds globally.
For either fixed sign, there exists W solving both coefficientwise residual congruences modulo4 if and only if

    [X^i]k=0 for every odd i with A/2<=i<3A/2.           (BS3)

When BS3 holds, exactly2^(d-3A) coefficient classes T modulo8 above the fixed T modulo4 solve both equations.
The criterion is independent of the integer lift of k and of the sign; the corresponding T sets for the two signs need not be identical.

There always exists such a k: the unique CRT polynomial

    k=Z modulo phi^(3A), k=0 modulo J_H X^A,
    degk<j_H+7A<d-2A                                   (BS4)

satisfies BS3.
Its coefficient0/1 lift supplies an actual K.
If n_K=h+6A-j_H, the allowed k family has2^n_K elements and precisely2^(n_K-A/2) satisfy BS3.
For either fixed sign the total number of distinct coefficient classes T modulo8 in BS2 solving both residuals modulo4 is therefore

    2^(n_K+d-7A/2)>0.                                  (BS5)

These are coefficient classes modulo8 satisfying residual equations modulo4, not residual solutions modulo8.

### B. Complete local error, with the changing-divisor term retained

Put chi_0=X Phi^2, Psi_0=Phi(chi_0),

    C=X^A mathcal_Y(chi_0)Psi_0^(7A),
    D_K=((K(C_2)-K^2)/2)bar+k^2.

Perform actual monic integer division before local reduction:

    sC^3-K^6=Phi^A L_s+2M_s, degM_s<2A.                 (BS6)

The remainder is even, L_sbar is divisible by phi^(3A), and the following class is well-defined in R_phi=F_2[X]/phi^(3A):

    eta_s=(L_sbar/phi^(3A))/(H_0 k^3)
       +phi^(2A)(M_sbar/k^4+D_K)
       +C_0^2Psi^A k(chi)/k^4.                         (BS7)

The numerator quotient is taken by exact polynomial division before entering R_phi; denominators are units there.
The entire simultaneous criterion for a specified W is

    F(T)=X_s(T)=0 modulo4
        if and only if Wbar^2=eta_s in R_phi.            (BS8)

Its derivative is exactly

    eta_s'=C_0^2Psi^A k^(-4) phi^2 k'(chi) in R_phi.     (BS9)

The sign relation is eta_-+eta_+=(phi^A k)^2 in R_phi, and a valid solution is translated by Wbar->Wbar+phi^A k for the opposite sign.

### C. Partial-H application with every actual cost

Take the full formal target and polynomial domain of C674: m>=1, Q a power of2 with2m<Q<5m, H(0)=1,5degH<5m-Q, B=X^(Q-m)H(chi), a specified square S in phi^(4m) modulo phi^(8m), and the full C677 CRT class with Pi_(4m)=0.
Use the SAME actual finite order set M and smooth set M_smooth defined from J=H(chi) in C674, and its actual largest irreducible multiplicity mu_max.
Choose now ANY integer

    E_pad>=max(2mu_max+2,4mu_max).                       (BS10)

Define C_comp, Y_seed=C_comp/J, D_C,D_seed and the full representative Y_0 exactly as in C674, but with THIS actual E_pad.
All C674 forward-square, canonical, full gate, nonsquare/odd-part and conditional integer-Haar statements persist, with

    H_norm=X^(2m)Y_0,
    H_norm^3 divides H_norm(X^3+X)^4,
    H_norm divides H_norm(chi)^2.                       (BS11)

For every q=2^k>=2 set

    A=2mq, Y=Y_0^q, H_0=H_norm^q,
    U=(H_norm phi^(14m))^q,
    h=q(2m+degY_0), d=q(30m+degY_0).

Then the entire BS1--BS9 theorem applies to these SAME canonical characteristic-two data.
Thus for every chosen sign there are actual monic integer T with reduction U whose two actual same-T residuals vanish coefficientwise modulo4.
The fixed-K count is2^(q(24m+degY_0)), and the total BS5 exponent is q(36m+3degY_0/2).
All support, row and fresh-factor costs remain

    D_C=E_pad sum_(n in M)varphi(n)/2
                       +sum_(n in M_smooth)mu_n varphi(n)/2,
    D_seed=D_C-5degH, D_B=Q-m+5degH,
    N=4m, L=least power of2 >=2N+1,
    e=3 times the least power of2 >=2N,
    K_bound=max(30L,4(D_seed+D_B)^2),
    n_fresh=1+10Lk_f, K_bound<n_fresh<=K_bound+20L+1,
    gcd(n_fresh,15)=1,
    degY_0<=D_seed+75L^2(e+1)+3(n_fresh-1)/2.             (BS12)

Here k_f is chosen by C674's explicit one-increment formula; there is no new search.
The actual degree of T is d and the canonical characteristic-two remainder degree is

    w_deg=q(26m+degY_0+D_B),
    d-w_deg=q(5m-Q-5degH)>0.

### D. The partial order31 example at normalized multiplicity24

For H=f_31=1+t^2+t^5,m=12,Q=32,S=0,a_0=144q, C674 has mu_max=1,E_pad=4 and already satisfies BS10.
Its existing representative therefore needs NO increase of the completion or fresh-factor budget.
For every q=2^k>=2 the construction gives actual T for either sign with

    d=q(360+degY_0)<=473704955q,
    w_deg=q(357+degY_0)<=473704952q,
    d-w_deg=3q, degY_0<=473704595.                       (BS13)

The fixed-K exponent is q(288+degY_0), the total coefficient exponent is q(432+3degY_0/2), and the original full canonical q remains maximal.
The weak-forward construction is essential: C674 proves that Y_0H(chi) complete and Y_0|Y_0(C_3) are incompatible for this H.
In fact raising Y_0 and J to the q-th power preserves that nonconstant order31 multiplicity profile, so strong C3 does not appear automatically after Frobenius powering.
The integer zero-Haar lift and all actual integer layers remain compatible data of the SAME characteristic-two construction.
The new T is not proved to have that chosen integer G_int as its actual G_can.

### Exact limits

There is no assertion for the nonsquare q=1 application, no residual solution modulo8, and no solution of the characteristic-zero equations.
The actual shared coefficients and actual divided remainders ARE used for the two modulo4 residuals, but this does not establish irreducibility, total reality, original nonzero field values, G_int=G_can or a full original A_0=24 realization.
The unrestricted G0001 task remains unresolved.

<a id="balanced-square-mod-four-argument"></a>
## Complete argument

### BC1. Exact square base and all-primary detection

Let H_* be the polynomial square root of H_0 and let mathcal_H_* be the product of the chosen integer P_psi with exponents N_psi/2.
Then

    F_*=mathcal_H_* Phi^(7A/2),
    mathcal_H Phi^(7A)=F_*^2,
    U_*=F_*bar=H_*phi^(7A/2), U=U_*^2.

These are exact INTEGER squares before any reduction.
In the free monic quotient Q_4=(Z/4Z)[X]/(T), and in every primary localization, ann(2)=2Q_4.
Thus a class2g vanishes precisely when gbar vanishes in the corresponding reduction modulo U.
The maximal ideals correspond exactly to the irreducible factors of U because2 is nilpotent.
Vanishing in all these localizations detects zero globally, and the monic free basis then detects coefficientwise divisibility of a canonical remainder.

Every theta_p is integral because C_p=X^p modulo p and T(C_p)=T^p modulo p, which has zero remainder modulo T.
For Delta_2(P)=(P(C_2)-P^2)/2, the exact-square base has Delta_2(F_*^2)bar=0 as a polynomial: writing F_*(C_2)=F_*^2+2Delta_2(F_*) and squaring makes the numerator divisible by4.
The full additive expansion with2Phi^A K+4W therefore gives

    abar=(phi^A k)^2 in F_2[X]/U.

Since J_H=H_* divides k, abar is zero on EVERY H_0-primary component.
Thus a is even there, and a^3,a^5 vanish modulo4 there for every W.
This calculation does not require either strong forward divisibility.

### BC2. The actual square of b on every non-phi primary

Fix psi|H_*, put n=ord_psi(H_*), and define

    M_3=ord_psi(H_*(X^3+X)),
    M_5=ord_psi(H_*(chi)).

Taking square roots of the polynomial multiplicity inequalities BS1 gives 4M_3>=3n and2M_5>=n.
These are effective pullback multiplicities, so no unramified-preimage assumption is hidden.
Put M_3^U=ord_psi(U_*(X^3+X)); it is at least M_3.
At phi itself, cubing permutes primitive fifth traces with nonzero derivative, so ord_phi U_*(X^3+X)=7A/2.
It follows on ALL factors that U_* divides U_*(X^3+X)^2.
Perform actual monic INTEGER division

    F_*(C_3)^2=Q_3 F_*+2E_3,                            (BE1)

where2E_3 is the even canonical remainder.
Modulo2 the quotient is the exact polynomial U_*(X^3+X)^2/U_*.
In particular ord_psi(Q_3bar)=2M_3^U-n.
Squaring BE1 in Z[X] before reducing gives

    F_*(C_3)^4=Q_3^2F_*^2 modulo4.

In Q_4 one has3b=T(C_3), so 9b^2=T(C_3)^2.
Since9=1 modulo4 and the2K term has zero cross term after squaring,

    b^2=F_*(C_3)^4
       =-2Q_3^2 Phi^A K modulo4.                        (BE2)

The4W term disappears, and the last equality uses the SAME divisor relation F_*^2=-2Phi^A K modulo4.
At the chosen psi, phi is a unit and ord_psi(k)>=n.
The coefficient after the factor2 in BE2 has order at least

    2(2M_3^U-n)+n=4M_3^U-n>=2n.

The reduction modulus there is psi^(2n), so b^2=0 modulo4 on that component.
At phi, U(X^3+X) is divisible by phi^(7A), so bbar=0 and b^2=0 modulo4 directly.
Thus b^2=0 modulo4 globally, and b^5 also vanishes modulo4.
This proves the needed assertion even though bbar can be a nonzero nilpotent on a non-phi component.

### BC3. The actual C5 cube and the first residual off phi

At the same psi define M_5^U=ord_psi(U_*(chi))>=M_5.
The actual reduction cbar is U(chi) modulo U, so cbar^2 has order at least4M_5^U>=2n and vanishes on this component.
Consequently2c^2=0 modulo4 there.
Together with BC1's a^5=0 this proves the first residual off phi.

For the cube we need an actual integer division, not just the preceding reduction.
Since3M_5^U>=n for every psi|H_*, H_* divides U_*(chi)^3.
Perform the monic integer division by mathcal_H_*, NOT by a phi-unit approximation to the changing T:

    F_*(C_5)^3=Q_5 mathcal_H_*+2E_5,                    (BE3)

where2E_5 is its even canonical remainder.
Then Q_5bar=U_*(chi)^3/H_* and ord_psi Q_5bar=3M_5^U-n.
Squaring BE3 before reduction yields F_*(C_5)^6=Q_5^2 mathcal_H_*^2 modulo4.
In the psi localization Phi is a unit, and the SAME T relation gives

    mathcal_H_*^2=-2Phi^(-6A)K modulo4.

Therefore this cubic base term is zero: after its factor2 the coefficient order is at least

    2(3M_5^U-n)+n=6M_5^U-n>=2n.

There is also the ACTUAL cross term from2Phi(C_5)^A K(C_5).
Since5=1 modulo4, c=T(C_5) in Q_4, and its full cube is

    c^3=F_*(C_5)^6
         +2F_*(C_5)^4 Phi(C_5)^A K(C_5) modulo4.       (BE4)

After the displayed2, F_*bar(chi)^4 alone has order4M_5^U>=2n, so the cross term vanishes without discarding K(C_5).
The condition H_*|k in fact also gives ord_psi k(chi)>=M_5, an additional nonnegative order, but this extra bound is unnecessary.
All remaining binomial terms have a coefficient divisible by4.
Thus c^3=0 modulo4 off phi.
Together with BC1--BC2 this proves BOTH actual residuals vanish modulo4 on every non-phi primary, for every allowed K,W and both signs.

### BC4. The unchanged local phi calculation and the complete half-error

In C669's phi calculation MT3--MT5, strong forward divisibility is used through the previously established bbar=0; its off-phi conclusions were supplied separately by MT2.
BC1--BC3 replace those conclusions by actual modulo4 products, and bbar=0 at phi still holds as proved above.
Every remaining hypothesis for its phi calculation holds directly: A is even, the integer base is the exact factorized square, Y'=0, k is the specified high unit root, and the old support congruence is BS1.
For transparency the resulting local identities, including the changing divisor, are retained here.

In the phi localization the SAME divisor satisfies

    Phi^(7A)=-2Phi^A K/mathcal_H modulo4.

The root and old support imply k^6=C_0^3 modulo phi^(4A): raise the root identity k^11=H_0C_0^2 modulo phi^(3A) to the sixth power, whose error has order at least6A, and use H_0^6=C_0^21 modulo phi^(4A).
The resulting (k^6/C_0^3)^11=1 has only the unit solution1 because11 is prime to the unit group order3*4^(4A-1).
Thus a_bar^3=c_bar^3 on this component; off phi both cubes vanish modulo2 by BC1 and BC3.
Both residuals are therefore even globally.

The exact additive half-difference gives

    a=Phi^(2A)K^2+2Z_a,
    Z_abar=phi^(2A)D_K+w^2,
    D_K=((K(C_2)-K^2)/2)bar+k^2,

where w=Wbar and Z_a is the actual half in the local quotient.
Expanding the first residual and then using the divisor gives

    F(T)=2Phi^(4A)(mathcal_H C^2+3K^11)/mathcal_H
                                                    modulo4.

The root identity makes this zero.
For c, write C_5=chi_0+2E with E integral.
The derivative of the integer square base has zero reduction, so its Taylor correction at chi_0 is already divisible by4.
Thus the full local cube is

    c^3=Phi^(6A)C^3
        +2Phi^(4A)C^2Psi_0^A K(chi_0) modulo4.

The odd quotients3,5 have been handled before reduction; BC2 gives b^2=2b^5=0 modulo4 here as well.
Now perform BS6's actual monic division, whose remainder is even by k^6=C_0^3 modulo phi^(4A).
The reduced quotient L_sbar is divisible by phi^(3A).
Reducing Phi^(7A)L_s using the SAME T before taking the legitimate half gives the ENTIRE remaining error

    (X_s(T)/2)bar
      =phi^A k L_sbar/H_0
        +phi^(6A)(M_sbar+k^4D_K)
        +phi^(4A)(C_0^2Psi^A k(chi)+k^4w^2)
                                  modulo phi^(7A).      (BE5)

The first term is retained; it is precisely the changing-divisor contribution.
Canceling phi^(4A) against the exact modulus and dividing by k^4 gives BS7--BS8.
The global equivalence follows from the already proved off-phi vanishings and all-primary detection in BC1, rather than from a phi-only check.

### BC5. Integer square half-remainder and the full derivative criterion

Write mathcal_Y=mathcal_V^2 and set

    D=X^(A/2)mathcal_V(chi_0)Psi_0^(7A/2), C=D^2.

The reduced consequence k^6=C_0^3 gives phi^(2A)|(k^3+Dbar^3).
Hence actual integer division supplies K^3-D^3=Phi^A Q+2V.
Squaring before reduction gives

    K^6-D^6
      =Phi^A(2D^3Q+Phi^A Q^2+4QV)+4D^3V+4V^2.

Its remainder modulo Phi^A is divisible by4, so M_+bar=0.
For the negative sign, subtracting the corresponding difference shows M_-bar=rem_(phi^A)(k^6).
This is a square polynomial, since phi^A is a square and one can divide k^3 by phi^(A/2) and square the quotient/remainder identity.
Thus M_sbar'=0 for either sign.
The conclusion uses the actual integer half-remainder; square reduction alone would not suffice.

Differentiate k^11=H_0C_0^2 modulo phi^(3A).
The modulus has zero derivative and H_0'=0, so k'=0 in R_phi.
Over the integers,

    ((K(C_2)-K^2)/2)'=X K'(X^2-2)-KK',

whence D_K'=X(k')^2+kk'=0 in R_phi.
The first numerator in BS7 is exactly

    L_sbar/phi^(3A)=(C_0^3+k^6)/phi^(4A),

a square polynomial because numerator and exact divisor are squares.
Its denominator has derivative zero in R_phi, as do the entire middle term and the square-unit prefactor of the last term.
The sole remaining derivative is BS9, since chi'=phi^2.

The factor J_H contains X^(A/2), so all coefficients of k below that degree vanish.
For odd i the corresponding contribution to phi^2k'(chi) is phi^2chi^(i-1), of EXACT phi-order2i.
It vanishes modulo phi^(3A) if i>=3A/2, and the lower distinct orders cannot cancel their least nonzero term.
The prefactor in BS9 is a unit.
Therefore eta_s'=0 if and only if BS3 holds.
An element of R_phi is a square precisely when its derivative is zero: its degree<6A representative then has zero derivative as a polynomial and has a unique polynomial square root modulo phi^(3A/2).
This proves existence and the exact criterion for EVERY integer lift K.
The two signs differ by the square(phi^A k)^2 in eta, giving the stated solution translation.

### BC6. Bounded CRT and every coefficient count

The moduli J_H X^A and phi^(3A) are coprime.
CRT gives BS4 with degree below j_H+7A<d-2A; its X^(3A/2) divisibility implies every coefficient condition BS3.
When soluble, BS8 fixes w precisely modulo phi^(3A/2), whose degree is3A.
The remaining d-3A binary coefficients are free, proving the fixed-K count.

For the complete K count, choose the CRT representative k_* modulo J_H phi^(3A) of degree<j_H+6A.
Every allowed k has the unique expression

    k=k_*+phi^(3A)J_H V, degV<n_K=h+6A-j_H.

Writing J_H=X^(A/2)J_0 with J_0(0)=1, the multiplier phi^(3A)J_0 is a unit modulo X^A.
As V runs through degrees below A, all A coefficient values from degree A/2 through degree below3A/2 vary freely.
These V are allowed because n_K>=6A>A.
The A/2 odd conditions are independent, leaving precisely2^(n_K-A/2) values of k.
Distinct k give distinct T modulo4 because deg(Phi^A K)<d; for a fixed integer K, distinct w give distinct T modulo8.
Changing K to K+2V only translates W by Phi^A V of degree<d, so there is no double count from integer lifts.
Multiplication of the counts proves BS5 for either fixed sign.

### BC7. Strengthened partial-H padding and its complete degree scope

Use C674's actual order sets and its elementary proof that every smooth W_(3^a5^b) is irreducible.
With E_pad as in BS10, its complete product C_comp still contains J exactly and every root multiplicity of Y_seed on M lies in

    [E_pad-mu_max,E_pad].

Since E_pad>=4mu_max, every target multiplicity for EITHER trace map is at least3E_pad/4, hence at least three quarters of every possible source multiplicity.
Both images stay in M and the derivatives are units there, as proved from the actual nontrivial odd core in C674.
All smooth orders cancel from Y_seed, so no omitted critical source remains in that factor.
If M is empty, C_comp=J and Y_seed=1; the smooth contribution is still retained in the actual D_C.
The inequality E_pad>=2mu_max+2 separately preserves the original support floor.

The complete correction Z and invisible B_(n_fresh)^3 obey BOTH stronger forward divisibilities, so their target multiplicities are at least their source multiplicities at every actual root.
Adding the three factors' multiplicities preserves the three-quarter lower bound for each map.
The endpoint X^(2m) has simple self-image under both maps and also satisfies this bound.
Thus H_norm=X^(2m)Y_0 obeys both the first inequality in BS11 and the stronger three-quarter bound for chi; the latter implies the required one-half bound in BS11.
Critical roots cause no unstated assumption: the seed has none, and the complete factors' global divisibilities already count full pullback multiplicity.

Every other step of C674 is unchanged because it used only the weaker E_pad>=2mu_max+2: finite membership of C_comp/J, exact complete row correction, all support floors, the paid fresh factor, global nonsquareness, canonical cube, full gate, odd parts and the complete product Y_0H(chi).
Its degree calculation uses the ACTUAL new E_pad through D_C and D_seed, not the previous smaller seed cost.
This proves BS12 with every completion/row/fresh expense included.
No normalized degree is silently substituted for the full polynomial degree.

For q>=2, H_0=H_norm^q and Y=Y_0^q are squares, the two inequalities raise unchanged, and the original old support identity raises to precision4A=8mq.
The exact integer factorized base can use the full q-multiplied exponents, so it is an integer square as required by BC1.
All hypotheses of the generic theorem hold, while the original canonical remainder, full C677 gate, maximal Frobenius q, integer layers and Haar compatibility remain those of the same characteristic-two input.
Substituting A,h,d gives the two displayed count exponents.

For the order31 example mu_max=1 and E_pad=4 already satisfy BS10, so C674's complete costs remain exactly those in BS13.
Its strong-C3 obstruction remains after q-th powering: if Y_0^q divided Y_0(C_3)^q, cancellation of the positive q in each root multiplicity would imply the forbidden normalized divisibility.
Equivalently the partial product J^q still has unequal primitive-order31 multiplicities q,0,0.
Thus actual same-T modulo4 solvability is compatible with the proved failure of the stronger forward condition.
This does not identify the actual integer residual with the synthetic G_int or supply any higher residual or characteristic-zero identity.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision balanced-mod-four-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:57 |
| status | open |
| reason | Register the exact square-input same-T modulo4 extension under three-quarter C3 and one-half C5 effective multiplicity bounds. Actual integer monic divisions and the same changing divisor prove all non-phi residuals vanish without requiring bbar or cbar to be zero; the full phi error retains its changing-divisor term, exact low odd-coefficient criterion, bounded CRT and complete K/W/T counts. Strengthened partial-H padding supplies every q>=2 application with full original costs, including the m12 partial-order31 example at unchanged degree bound. No strong-C3 upgrade, q1 assertion, modulo8 residual solution, G_int=G_can, characteristic-zero or full original realization is claimed. Root and original_law are contributors; fresh isolated whole review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire balanced same-T theorem](#balanced-square-mod-four-statement) | BS1--BS13: explicit square polynomial inputs, effective pullback multiplicities, actual integer base and common divisor, all-primary residuals, complete error/criterion/counts, paid partial-H padding, every q>=2 and the m12 branch with remaining limits. |
| argument | [Complete actual-divisor proof](#balanced-square-mod-four-argument) | BC1--BC7 and BE1--BE5: exact square lift, integer quotient/half-remainder, odd denominators, effective local orders and every cross term, all-primary detection, unchanged full phi error, exact derivative/CRT/counts and complete padding/cost application. |
| dependency | [Adopted actual local same-T calculation](Yin_C_G0669_v1.md#decision-whole-reviewed-2026-10-24) | Only the verified factorized-base, actual-divisor phi calculation and complete eta/square-image/sign interfaces at their explicitly checked local hypotheses. Its stronger all-primary assumptions are replaced by the new BC1--BC3 proof, not silently imported. |
| dependency | [Adopted square-base refinement](Yin_C_G0672_v1.md#decision-whole-reviewed-2026-10-24) | Actual integer square half-remainder, complete derivative and low coefficient obstruction, bounded CRT and coefficient-fiber count; every applicability condition is rechecked after replacing strong forward divisibility. |
| dependency | [Adopted complete partial-H construction](Yin_C_G0674_v1.md#decision-whole-reviewed-2026-10-24) | Complete PH1--PH11/PC1--PC9 construction, exact smooth/partial factors and finite sources, canonical/full gate/q/odd parts/layers/Haar and all costs, strong-C3 obstruction and m12 norm. Only corrected R1062v2 is selected by its adoption; empty M leaves C_comp=J, Y_seed=1. The new padding inequalities are proved here. |
| support | [Exact remaining realization limits](#exact-limits) | Actual simultaneous residuals modulo4 do not imply modulo8 residuals, equality with the synthetic integer Haar polynomial, characteristic-zero equations, irreducibility, total reality or unrestricted Task completion. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:18 |
| status | proved |
| reason | The entire fixed BS1--BS13 statement and BC1--BC7/BE1--BE5 proof were directly read, including the actual integer divisions, effective multiplicities, all-primary modulo4 detection, complete phi error, exact coefficient criterion and counts, enlarged partial-H padding and complete costs. Fresh isolated whole R897 independently reconstructs every new step at the exact adopted C669/C672/C674 interfaces. Adopt the whole theorem and every q>=2 partial-H application, including m12 at unchanged cost; no q1, modulo8 residual solution, G_int=G_can, characteristic-zero or unrestricted realization is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire balanced same-T theorem](#balanced-square-mod-four-statement) | BS1--BS13: explicit square polynomial inputs, effective pullback multiplicities, actual integer base and common divisor, all-primary residuals, complete error/criterion/counts, paid partial-H padding, every q>=2 and the m12 branch with remaining limits. |
| argument | [Complete actual-divisor proof](#balanced-square-mod-four-argument) | BC1--BC7 and BE1--BE5: exact square lift, integer quotient/half-remainder, odd denominators, effective local orders and every cross term, all-primary detection, unchanged full phi error, exact derivative/CRT/counts and complete padding/cost application. |
| dependency | [Adopted actual local same-T calculation](Yin_C_G0669_v1.md#decision-whole-reviewed-2026-10-24) | Only the verified factorized-base, actual-divisor phi calculation and complete eta/square-image/sign interfaces at their explicitly checked local hypotheses. Its stronger all-primary assumptions are replaced by the new BC1--BC3 proof, not silently imported. |
| dependency | [Adopted square-base refinement](Yin_C_G0672_v1.md#decision-whole-reviewed-2026-10-24) | Actual integer square half-remainder, complete derivative and low coefficient obstruction, bounded CRT and coefficient-fiber count; every applicability condition is rechecked after replacing strong forward divisibility. |
| dependency | [Adopted complete partial-H construction](Yin_C_G0674_v1.md#decision-whole-reviewed-2026-10-24) | Complete PH1--PH11/PC1--PC9 construction, exact smooth/partial factors and finite sources, canonical/full gate/q/odd parts/layers/Haar and all costs, strong-C3 obstruction and m12 norm. Only corrected R1062v2 is selected by its adoption; empty M leaves C_comp=J, Y_seed=1. The new padding inequalities are proved here. |
| support | [Exact remaining realization limits](#exact-limits) | Actual simultaneous residuals modulo4 do not imply modulo8 residuals, equality with the synthetic integer Haar polynomial, characteristic-zero equations, irreducibility, total reality or unrestricted Task completion. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0897_v1.md#whole-balanced-forward-mod-four-finding) | Complete fixed statement, argument, exact input applicability, actual integer/global scope, every application and all stated limitations; the main agent read the complete finding before this adoption. |
