---
author: Yin
---
# Dyadic trace pullback and the exact ideal criterion for one coupled residual lift

Human author Yin.
Root developed this argument within the renewed [G0001 continuation](../tasks/Yin_T_G0001_v1.md#decision-resume-until-two-percent-remaining-2026-10-25).
This is author mathematics awaiting independent whole review.
Before proof investment, the existing [C202 exact changing-divisor argument](Yin_C_G0202_v1.md#integrality-and-changing-divisor), [C586v2 trace composition account](Yin_C_G0586_v2.md#argument) and [C689 next-layer criterion](Yin_C_G0689_v1.md#statement) were read.
Their fixed scopes do not supply the all-level, enlarged-degree iff below.
The common content decision therefore selects a new C with its complete proof, without a duplicate process draft.
The commuting trace identity is the elementary normalized identity already used in C586, not a new external theorem; the new coefficient covariance and lifting conclusions are proved here.
No native computation, coefficient search or source acquisition is used.

## Statement

### DP1. Complete arbitrary-monic domain

Let C_0=2,C_1=X,C_(j+1)=XC_j-C_(j-1), so C_j(z+z^-1)=z^j+z^-j.
Let T in Z[X] be monic of degree d>=1, let s in{1,-1}, and define the ACTUAL canonical polynomials

    a_T=rem_T T(C_2)/2, b_T=rem_T T(C_3)/3,
    c_T=rem_T T(C_5)/5,
    F(T)=rem_T(2c_T^2-3a_T^5),
    X_s(T)=rem_T(b_T^2-a_T^3+s(c_T^3-2b_T^5)).       (DP1)

All are integer polynomials of degree<d.
Reducible T, repeated factors and zero constant coefficient are allowed.
Fix any integer n>=1 and assume F(T),X_s(T) are coefficientwise divisible by2^n.
Set

    U=Tbar, B=F_2[X]/U, alpha=a_Tbar,
    E_F=(F(T)/2^n)bar, E_X=(X_s(T)/2^n)bar in B.     (DP2)

The divisions by2^n precede reduction and occur in the integer coefficient module.
For every dyadic q=2^r>=2, consider EXACTLY the monic coefficient classes

    T_new=T(C_q)+2^(n+1)V modulo2^(n+2), degV<qd.    (DP3)

Both residuals of some DP3 vanish coefficientwise modulo2^(n+1) if and only if

    E_X in alpha^2 B, E_F=alpha^2 E_X in B.          (DP4)

These are tests in the original degree-d quotient, retaining all primary factors.
If DP4 holds, choose deg h<d with E_X=alpha^2h in B.
The coefficient0/1 integer lift of

    v=h^(q/2), degv<qd/2                            (DP5)

is a successful V; any integer lift of a successful v gives the same congruences.
With the full factorization and truncated orders

    U=product_psi psi^(N_psi),
    t_psi=min(N_psi,ord_psi alpha), ord_psi0=infinity,
    rho_q=sum_psi deg(psi) max(qN_psi/2-qt_psi,0),   (DP6)

the EXACT number of successful classes DP3 is2^(qd-rho_q), or zero when DP4 fails.
The truncated orders do not depend on the representative of alpha, and qN_psi/2 is an integer.
This counts only the specified highest-correction family, not all lower coefficient classes or every lift of the original T.

### DP2. Exact covariance and quadratic-primary application

For every positive integer j the following hold as exact INTEGER canonical-polynomial identities:

    a_(T(C_j))=a_T(C_j), b_(T(C_j))=b_T(C_j),
    c_(T(C_j))=c_T(C_j),
    F(T(C_j))=F(T)(C_j), X_s(T(C_j))=X_s(T)(C_j).    (DP7)

Suppose an actual monic T' of degree d satisfies F(T')=0 modulo16, X_s(T')=0 modulo8, and its actual reduction and canonical dyadic remainder have

    U=H_0 phi^(7A), phi=X^2+X+1, gcd(H_0,phi)=1,
    A>=2 even, d=degH_0+14A,
    alpha=0 modulo H_0,
    alpha=phi^(2A)k^2 modulo phi^(7A), gcd(k,phi)=1.  (DP8)

Set E=(X_s(T')/8)bar.
For every dyadic q>=2 there is

    T_*=T'(C_q)+16V, degV<qd,
    F(T_*)=X_s(T_*)=0 modulo16                       (DP9)

if and only if

    E=0 modulo H_0 and E=0 modulo phi^(4A).          (DP10)

Each nonempty family has exactly2^(q(d-3A)) classes modulo32 above T'(C_q) modulo16, and one solution has degV<qd/2.

For ANY complete actual C689 input satisfying SX1--SX4, its ACTUAL SX5--SX6 first correction T' has precisely DP8 and the two required residual congruences.
Consequently its two SX7 tests are necessary and sufficient for DP9, for every dyadic q>=2; SX8 is not required for this enlarged-degree family.
If T'=T+8V_0, then the output is congruent to T(C_q) modulo8.
No particular passing SX4/SX7 input is asserted.
C689's same-degree all-lift count and derivative criterion remain unchanged, since this theorem changes the degree and the specified coefficient family.

### DP3. Degree, Frobenius and original-cost boundary

For dyadic q, the canonical reductions are U_q=U^q and alpha_q=alpha^q.
DP3 changes neither reduction because n>=1.
If alpha is a nonzero polynomial, deg alpha_q=q deg alpha and

    qd-deg alpha_q=q(d-deg alpha).                  (DP11)

The same degree scaling holds for any nonzero characteristic-two canonical polynomial expression in a,b,c, pulled back through DP7 and then subjected to DP3.
If U and alpha originally have a specified common maximal dyadic Frobenius exponent, that exponent is multiplied by q; no original maximality is inferred without its premise.

For P(z)=z^d T(z+z^-1), the UNCORRECTED trace pullback corresponds exactly to P(z^j) and m(P(z^j))=m(P) for every j>=1.
The correction in DP3 changes that polynomial and receives no irreducibility, total-reality, root-location, coefficient-height or Mahler bound here.
No equality G_int=G_can, characteristic-zero residual, original-field norm gain, near-one family or unrestricted Task completion follows.

## Complete argument

### DP4. Exact integer composition and monic division

The trace recurrence gives integer coefficients and leading term X^j for j>=1.
Substitution X=z+z^-1 proves the Laurent identity by recurrence and is injective: a nonzero degree-e polynomial has a nonzero z^e leading Laurent coefficient.
It follows directly that C_i(C_j)=C_(ij)=C_j(C_i), with exactly the normalization used in C586v2.
If R=TQ+R_0 is actual monic division and degR_0<d, then

    R(C_j)=T(C_j)Q(C_j)+R_0(C_j), degR_0(C_j)<jd.

Uniqueness of monic division proves exact canonical remainder covariance, including zero remainder.
For p=2,3,5, C_p=X^p modulo p and T(C_p)=T^p modulo p; the actual integer remainder is therefore coefficientwise divisible by p.
This proves integrality in DP1.
Commuting C_j with each C_p and using remainder covariance proves the first three DP7 identities before the legitimate integer divisions.
Polynomial arithmetic followed by one more monic division proves the residual identities.
No roots, fields, irreducibility or squarefreeness are used.

Repeated composition of C_2=X^2-2 gives C_q=X^q modulo2 for dyadic q.
Thus DP7 gives U_q=U^q, alpha_q=alpha^q, and errors E_F^q,E_X^q in B_q=F_2[X]/U^q.
The map B -> B_q, f -> f^q, is well defined and injective: full irreducible multiplicities show U^q|f^q exactly when U|f.

### DP5. Actual changing-divisor formula at every level

Let A be any monic degree-D integer polynomial and A_new=A+2^(n+1)V, degV<D.
Write A(C_2)=A Q_2+2a_A.
Actual monic division gives the exact identity

    a_(A_new)=a_A+2^n rem_(A_new)(V(C_2)-VQ_2).     (DP12)

This retains the changing-divisor term -VQ_2.
Reduction of the original division yields U_A Q_2bar=U_A^2 in the polynomial domain, so Q_2bar=U_A.
The new remainder in DP12 therefore reduces to v^2 in F_2[X]/U_A.
For p=3,5 the numerator and divisor are unchanged modulo2^(n+1), and division by p is invertible there; the odd canonical quotients are unchanged at that precision.
Final monic division also commutes with coefficient reduction.

Each binomial term of order at least two in the dyadic change has factor2^(2n), divisible by2^(n+1) for n>=1.
The two linear coefficients -15 and -3 are odd.
Consequently the ACTUAL canonical residual differences are

    F(A_new)-F(A)=2^n rem_(U_A)(alpha_A^4 v^2),
    X_s(A_new)-X_s(A)=2^n rem_(U_A)(alpha_A^2 v^2)
                                      modulo2^(n+1). (DP13)

Using either final divisor at this modulus is legitimate since A_new=A modulo2^(n+1); the lower dyadic-half carry was already retained in DP12.
This proves the higher-level identity directly from the C202 mechanism rather than assuming its original theorem had this scope.
It covers both signs, n=1 and all nilpotent components.

### DP6. Complete ideal criterion and explicit correction

Apply DP13 to A=T(C_q).
The two equations in B_q are exactly

    alpha^(4q)v^2=E_F^q,
    alpha^(2q)v^2=E_X^q.                            (DP14)

Multiply the second by alpha^(2q) and use injectivity of the q-power map to obtain the necessary equality E_F=alpha^2 E_X in B.
At a full primary psi^(qN), put t=min(N,ord_psi alpha).
If2t>=N the second left side is zero, requiring ord_psi E_X>=N.
If2t<N, its divisibility by psi^(2qt) requires ord_psi E_X>=2t, with the zero class included.
These cases are precisely E_X in alpha^2B at that primary.
CRT gives the first DP4 condition globally.
Only divisibility in the polynomial domain was used; no zero divisor was cancelled.

Conversely E_X=alpha^2h modulo U implies E_X^q=alpha^(2q)h^q modulo U^q.
Since q is even, v=h^(q/2) solves the second DP14 equation with degv<qd/2.
The coupling equality in DP4 supplies the first one.
DP13 shows every integer lift of that v works.
This proves necessity, sufficiency and the short-degree construction.

### DP7. Every coefficient fiber and every primary

Once the coupling holds, the first equation is determined by the second.
The homogeneous map is v -> alpha^(2q)v^2 on the qd-dimensional binary space B_q.
At psi^(qN) its kernel is exactly

    ord_psi v>=max(qN/2-qt,0).

This follows from2qt+2ord_psi v>=qN, with no restriction when2t>=N.
Hence its rank on that primary is deg(psi)max(qN/2-qt,0).
Summing over CRT components gives rho_q, and each nonempty affine fiber has2^(qd-rho_q) elements.
Distinct degree<qd reductions of V give distinct monic classes DP3 modulo2^(n+2), proving the exact count.
The argument includes alpha=0 and every repeated factor without a distribution assumption.

### DP8. Exact modulo16 consumer

Under DP8, alpha^4 is zero: it is zero on H_0 and has phi-order8A>=7A.
The ideal alpha^2B is zero on H_0 and is the entire phi^(4A) ideal at phi, because k^4 is a unit.
At n=3 the first error is zero since F(T')=0 modulo16.
If E belongs to alpha^2B, then alpha^2E=0 follows from alpha^4=0.
Thus DP4 is exactly DP10, proving the iff DP9--DP10.
All H_0 primaries have rank zero; the degree-two phi primary has rank2(7Aq/2-2Aq)=3Aq.
The count is therefore2^(q(d-3A)), with the same explicit short-degree correction.

C689's SX4 assumption supplies its actual SX5--SX6 T', satisfying F16 and X_s8.
The correction leaves its reduced a unchanged, and SX10 is exactly DP8.
Its SX7 becomes DP10, so the present enlarged-degree family requires no additional SX8 test.
This neither proves SX4/SX7 for a specific input nor changes the scope of C689's fixed-degree classification.

### DP9. Exact remaining boundaries

A nonzero characteristic-two polynomial f(C_q)=f(X^q)=f^q has q times the original degree.
DP7 ensures the composed expressions are already canonical representatives with degree<qd.
DP12 at n>=1 and the odd-quotient continuity show DP3 preserves all their reductions.
This proves DP11 and the polynomial-expression extension.
Membership in F_2[X^(2^k)] is determined by divisibility of the positive exponents by2^k; multiplication of those exponents by q proves the asserted common maximal-Frobenius scaling when originally specified.
The monic positive-degree U keeps that common maximum finite, even when the other polynomial is constant.

The exact reciprocal identity is

    z^(jd)T(C_j(z+z^-1))=z^(jd)T(z^j+z^-j)=P(z^j).

All j roots above a root beta of P contribute log^+|beta| in total, with its full multiplicity; the leading coefficient remains one.
This proves m(P(z^j))=m(P), the already retained C586 composition boundary, without irreducibility.
A later coefficient correction is a different polynomial and has no unproved original-root or Mahler control here.
Synthetic integer layers, true canonical G, exact characteristic-zero equations and the unrestricted original objective remain separate obligations.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision pullback-candidate

| Field | Value |
| --- | --- |
| date | 2026-10-25T05:18 |
| status | open |
| reason | Register the complete all-monic and all-level dyadic trace-pullback criterion, exact covariance, full highest-correction fibers and short-degree solution, with the actual modulo16 quadratic-primary consumer. First and low/non-phi second errors remain necessary; no passing input or original realization is claimed. The author-complete proof awaits isolated independent whole review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete pullback theorem](#statement) | DP1--DP11, all monic inputs, n>=1 and dyadic q>=2, exact iff and full primary count, actual first-corrected modulo16 consumer and every degree/realization limit. |
| argument | [Complete proof](#complete-argument) | DP4--DP9 and DP12--DP14, exact normalized trace/monic covariance, legitimate all-level halves and carry, complete ideal iff, explicit short correction, nilpotent ranks and actual original-cost boundary. |
| support | [Existing changing-divisor mechanism](Yin_C_G0202_v1.md#integrality-and-changing-divisor) | Exact integer quotient identity and monic-modulus continuity; the new all-level formulas and pullback are proved directly, without attributing them to the old one-layer theorem. |
| support | [Existing self-composition account](Yin_C_G0586_v2.md#argument) | Credited trace normalization, elementary commuting identity and unchanged Mahler measure; actual-field and irreducibility conclusions are not imported, and the historical SELF relationship is unchanged. |
| dependency | [Actual first modulo16 correction](Yin_C_G0689_v1.md#statement) | Application only: complete SX1--SX4 give actual SX5--SX6 T' with reduced data SX10; SX7 becomes the enlarged-degree iff without assuming its satisfaction or transferring the fixed-degree fiber count. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T05:29 |
| status | proved |
| reason | Adopt the independent whole review of DP1--DP14, the exact all-monic/all-level dyadic pullback criterion, full primary fibers, short-degree correction and conditional actual C689 application. Every integer half and changing-divisor term is retained. The enlarged-degree family removes the square-image restriction only after the stated ideal/coupling tests pass; no passing original input, characteristic-zero realization or Mahler improvement is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete pullback theorem](#statement) | DP1--DP11, all monic inputs, n>=1 and dyadic q>=2, exact iff and full primary count, actual first-corrected modulo16 consumer and every degree/realization limit. |
| argument | [Complete proof](#complete-argument) | DP4--DP9 and DP12--DP14, exact normalized trace/monic covariance, legitimate all-level halves and carry, complete ideal iff, explicit short correction, nilpotent ranks and actual original-cost boundary. |
| support | [Existing changing-divisor mechanism](Yin_C_G0202_v1.md#integrality-and-changing-divisor) | Exact integer quotient identity and monic-modulus continuity; the new all-level formulas and pullback are proved directly, without attributing them to the old one-layer theorem. |
| support | [Existing self-composition account](Yin_C_G0586_v2.md#argument) | Credited trace normalization, elementary commuting identity and unchanged Mahler measure; actual-field and irreducibility conclusions are not imported, and the historical SELF relationship is unchanged. |
| dependency | [Actual first modulo16 correction](Yin_C_G0689_v1.md#statement) | Application only: complete SX1--SX4 give actual SX5--SX6 T' with reduced data SX10; SX7 becomes the enlarged-degree iff without assuming its satisfaction or transferring the fixed-degree fiber count. |
| review | [Fresh isolated whole review](../audits/reviews/Yin_R_G0917_v1.md#whole-pullback-finding) | Entire fixed statement and argument, exact direct-input applications, all quantifiers and declared limitations; independently reviewed. |
