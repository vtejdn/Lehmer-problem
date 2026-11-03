---
author: Yin
---

# Exact quadratic complementary energy and its integer trace dependence

Date: 2026-10-11T19:18.
Human author: Yin.
Provenance: project deduction using the fixed all-representative certificate method.
Internal parameter calibration under the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Root supplied the complete candidate; the responsible author checked all parity/equality/cost branches.
The old family, Euclidean scalar and Gram computations are credited at their actual scope below.
No main-theorem designation or objective change is made.

## Statement

For EVERY INTEGER a>=3, let P_a=t^2-a t+1, alpha=(a+sqrt(a^2-4))/2, K=Q(alpha), and use the ACTUAL monogenic order O_0=Z[alpha].
The polynomial is actually irreducible, alpha is a nontorsion integer unit, and its ORIGINAL degree is2.
Fix the allowed common coefficient window[0,2].
A rational coordinate f=x+y t+z t^2 is admissible exactly when its ACTUAL residue (m,n)=(x-z,y+a z) is in Z^2 minus{0}.
Packets have finite positive normalized rational weights and ALL aggregate lags zero.
Formal-real packets retain this same integer-coordinate condition, not a test at one numerical root.

Put k=floor(a/2) and L=floor(a^2/4)+1.
Let E_2^Q,E_2^R and Gamma_2^Q have the exact C16 energy and rational-PD-Toeplitz meanings.
Then

    E_2^Q=E_2^R=Gamma_2^Q=1/L,

with an ACTUAL rational primal minimum and rational positive-definite Toeplitz dual maximum.
The proof uses only C16 weak duality and matching explicit witnesses, not the later general completeness theorem.

**A. All minimizing packets.** The common prototype is f_A=(1+t^2)/a and its TOTAL weight is (L-1)/L.
For even a=2k, the remaining type is f_B=(1-t^2)/2 with total weight1/L.
For odd a=2k+1, the remaining allowed types are f_B=((k+1)-kt^2)/a and f_C=(k-(k+1)t^2)/a with COMBINED total weight1/L.
Either negative type may be absent.
All minimizers consist exactly of signed copies from the appropriate list, with positive repetitions/splits inside these masses.
The formal-real equality class permits irrational weight splits; denominator statements below apply to RATIONAL packets only.

**B. Whole-lattice analytic certificate.** The rational Toeplitz form with diagonal1, first lag a/(2L) and second lag a^2/(2L)-1 is positive definite.
Writing ell=n+k m, its complete coefficient identity is

    f^T W f=(m^2+ell^2)/L+(1-1/L)y^2, a=2k,
    f^T W f=(m^2+m ell+ell^2)/L+(1-1/L)y^2, a=2k+1.

The integer residue change is unimodular.
The two binary integer forms have complete nonzero minimum1 and four/six shortest vectors respectively; equality additionally forces y=0.
This supplies the all-representative lower bound and complete equality classification above.

**C. Actual costs and coefficient comparison.** Every rational minimizing packet has ACTUAL least coefficient denominator q=a and least final weight denominator M divisible by L.
The standard two-label attainer has M=L, integer energy S=a^2/L, residue norms+1,-(L-2), and full numerator resultants+a^2,-a^2(L-2).
Contents are1,k in the even case and1,1 in the odd two-label case; the other odd type is also primitive.
The GENERAL split copied signed product is

    a^(2M)[-(L-2)]^(M/L),

which is -a^(2L)(L-2) only when M=L.
All minimizers have weighted income I=log a+log(L-2)/(2L), and true surplus (log L)/2+log(L-2)/(2L).
It is charged by actual original-width expense Tm(P_a)/d=m(P_a)=arcosh(a/2), with all contents and signs retained.

The COMPLETE Euclidean residue quotient minimum is2/(a^2+2), with only the signed shortest representatives (a+2t+a t^2)/(a^2+2).
Their positive autocorrelations cannot cancel in positive mixtures.
The new complementary minimum divided by that old scalar floor is(a^2+2)/(2L)>1 and tends to2.
As a tends to infinity, E_2 tends to0 while m(P_a) tends to infinity and expense minus surplus tends to log2.
This fixed-degree coefficient calibration supplies no near-one family, degree-uniform gap or overorder extension.

## Current assessment
[Selected decision](#decision-current-complete-isolated-adoption)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-11T19:18 |
| status | open |
| reason | Register the complete integer-parameter optimum/equality and cost statement with its exact frozen author argument. Separate whole and actual C statement/dependency review is pending; old fixed-a4 and Euclidean-result reviews are not automatically expanded. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All integer a>=3 in ACTUAL O_0 and fixed allowed window2, complete parity/equality classes, rational denominator conditions and growing-measure limits only. |
| argument | [Argument](#argument) | Complete03:10 author freeze Sections1--8/theorem/equations1--19, local binary-form/square proof and every original-degree cost. |
| dependency | [All-representative weighted certificate and energy domain](Yin_C_G0016_v1.md#statement) | Exact nonzero integer residues, rational/formal-real conventions and WEAK Toeplitz/quotient inequality; the local matching pair and W establish equality without C17. |
| dependency | [Direct generic-monic full-root inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Complete original degree2 norms, actual common width and final weights for the charged surplus comparison. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-11T19:25 |
| status | proved |
| reason | Adopt the completed separate noncontributor finding for this exact registered scope and selected fixed argument. Complete original histories, current repairs, source inspection limits and all costs remain; no uniform efficiency, unrestricted gap or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All integer a>=3 in ACTUAL O_0 and fixed allowed window2, complete parity/equality classes, rational denominator conditions and growing-measure limits only. |
| argument | [Argument](#argument) | Complete03:10 author freeze Sections1--8/theorem/equations1--19, local binary-form/square proof and every original-degree cost. |
| dependency | [Dependency](Yin_C_G0016_v1.md#statement) | Exact nonzero integer residues, rational/formal-real conventions and WEAK Toeplitz/quotient inequality; the local matching pair and W establish equality without C17. |
| dependency | [Dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Complete original degree2 norms, actual common width and final weights for the charged surplus comparison. |
| review | [Current finding](../audits/reviews/Yin_R_G0746_v1.md#c20-quadratic-parameter-extraction-finding) | Exact registered statement, selected complete argument, changed interfaces and dependencies in this physical version; preserved original reviews are not silently expanded. |


### Decision current-complete-isolated-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:16 |
| status | proved |
| reason | Adopt the exact complete current statement and selected full argument with R746's separately assigned isolated whole finding at this specific target. All actual-order/domain, finite/rational/formal-real, window, equality, original norm/denominator and unresolved-uniformity boundaries remain. The original UNKNOWN findings retain their actual dates, fixed inputs, source/checker/preservation facts and relationships; the new finding does not backfill their contexts or adopt any stronger conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | All integer a>=3 in ACTUAL O_0 and fixed allowed window2, complete parity/equality classes, rational denominator conditions and growing-measure limits only. |
| argument | [Exact retained argument](#argument) | Complete03:10 author freeze Sections1--8/theorem/equations1--19, local binary-form/square proof and every original-degree cost. |
| dependency | [Exact retained dependency](Yin_C_G0016_v1.md#statement) | Exact nonzero integer residues, rational/formal-real conventions and WEAK Toeplitz/quotient inequality; the local matching pair and W establish equality without C17. |
| dependency | [Exact retained dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Complete original degree2 norms, actual common width and final weights for the charged surplus comparison. |
| review | [Complete current isolated finding](../audits/reviews/Yin_R_G0746_v1.md#current-c20-complete-isolated-independent-finding) | Entire exact current Statement, complete selected Argument and all necessary interfaces, with actual complete initial judgment2026-10-22T19:11 preceding complete old-finding comparison2026-10-22T19:12; no proof repair, expanded source-proof scope or new native run. |

## Argument

The whole frozen D15 author account follows unchanged apart from first-title depth and final whitespace.
The exact irreducibility/order statement, both full coefficient-square identities, positive definiteness, all integer shortest vectors, matching packets and every parity-specific norm/content/denominator calculation are physically present.
Current C16 weak duality and C10 full-root expense supply the selected reused inputs.
The old L249 scalar representative and L4 Gram value are credited comparisons rederived locally; no necessary proof is left behind an L redirect.

The optimal packet and optimal Toeplitz matrix are explicit here, so this is a special attained primal/dual equality and does not infer generic attainment from C17.
Integer a and actual O_0 are indispensable; no real-parameter or maximal-order generalization is silently selected.
Final rational-weight denominators may grow under splitting, and the complete product formula uses that actual M.

## Exact quadratic complementary energy as the trace coefficient varies

Date: 2026-10-12.
Authored by the paraunitary researcher AI for Yin.
This distinct responsible draft was allocated for a new focused theoretical parameter control.
Root supplied the full odd/even polynomial, weighted-form, equality-packet, denominator and norm candidate and is a substantive contributor.
The author checked and organized the complete argument below.
The author previously developed the different fixed a=4 control in C16; neither that authorship nor its old review is an independent review of the present parameter theorem.
No native mathematical program, scan, solver, new J or new external theorem is used.

<a id="quadratic-parameter-reuse-and-domain"></a>
## 1. Bounded reuse and exact changed scope

The [C16 fixed a=4 optimum](Yin_C_G0016_v1.md#sharp-quadratic-window-minimum) is the direct predecessor and is NOT claimed new.
Its [whole-lattice weighted certificate](Yin_C_G0016_v1.md#weighted-quotient-lattice-certificate) supplies the finite-window comparison method; the parameter proof below is a complete explicit square calculation, so it does not require general dual completeness.

The corrected [C14 v2 statement](Yin_C_G0014_v2.md#statement) concerns actual integral values, short windows and the q=2,S=2 boundary.
The corrected [C15 v2 statement](Yin_C_G0015_v2.md#statement) concerns periodic packets, near-minimum INTEGER energy, reciprocal congruence and signed-period widths.
Those objectives differ from minimizing normalized E while q and weights vary.
Its existing monogenic a=3 packet at width4 and E=1/4 was checked against the new width2 value below; it is consistent with the different window.

The original quadratic family and its irreducibility are already used in [L249](../ledger/Yin_L_G0249_v1.md#quadratic-centered-all-circle-control) and [L296](../ledger/Yin_L_G0296_v1.md#actual-anti-column-quadratic-all-window-control).
L249's j=1 formula already gives the Euclidean least representative and its energy.
[L4's Gram discussion](../ledger/Yin_L_G0004_v1.md#degree-window-tests) already records the preceding value G_3=a^2+2.
These scalar/Gram facts are rederived only to compare the new complete complementary optimum.
[L245](../ledger/Yin_L_G0245_v1.md#positive-root-weight-complete-cost) optimizes positive weights on ORIGINAL ROOTS followed by a full coefficient operator bound; it is not the present Toeplitz form acting on coefficient correlations and nonzero integral residues.

A bounded G-material search by the parameter polynomial, floor(a^2/4), quadratic energy and the neighboring optimal-control interfaces did not locate the complete odd/even complementary classification below.
This is no exhaustive priority claim.
The binary forms are checked by direct integer squares and enumeration at value1; no perfect-form classification, continuous-parameter theorem or new source theorem is imported.

Fix an INTEGER a>=3 and put

    P_a(t)=t^2-a t+1,
    alpha=(a+sqrt(a^2-4))/2,
    O_0=Z[alpha],
    k=floor(a/2), L=floor(a^2/4)+1.
    a=2k: L=k^2+1; a=2k+1: L=k^2+k+1.             (1)

Since (a-1)^2<a^2-4<a^2, the discriminant is not a square.
Thus P_a is the actual irreducible minimal polynomial of alpha, of degree2.
Its roots are the two positive reciprocal numbers alpha>1 and alpha^-1<1, so it is a nontorsion integer-unit input and

    Norm_K(alpha)=1,
    m(P_a)=log alpha=arcosh(a/2)>0.                 (2)

No larger order or maximal-order identification is assumed.
Monicity and alpha^-1=a-alpha give the actual integral power basis1,alpha in O_0.

Use the ALLOWED common coefficient window [0,2].
A rational coordinate f=x+y t+z t^2 has nonzero actual O_0 value precisely when

    (m,n)=(x-z,y+a z) in Z^2 minus{0},
    f(alpha)=m+n alpha.                            (3)

Consider every finite family of such rational f_b with strictly positive rational normalized weights omega_b and exact constant covariance sum omega_b f_b f_b*=E.
There is no bound on the number of labels, rational coefficient denominators or weight denominators.
Let E_2^Q be the infimum.
The formal-real version E_2^R retains (3) as the integer coordinate condition, not merely membership of a numerical value at one real embedding.

<a id="quadratic-parameter-minimum-statement"></a>
## 2. Exact minimum and all equality families

**Theorem.** In this exact domain,

    E_2^Q=E_2^R=Gamma_2^Q=1/L,                      (4)

and a rational two-coordinate family attains the minimum and a rational positive-definite Toeplitz form attains the C16 dual supremum.

For even a=2k, define

    f_A=(1+t^2)/a, f_B=(1-t^2)/2.                  (5)

Every minimizing packet in the allowed window consists of signed copies of f_A and f_B.
Their TOTAL weights must respectively be (L-1)/L and1/L.

For odd a=2k+1, define

    f_A=(1+t^2)/a,
    f_B=((k+1)-k t^2)/a,
    f_C=(k-(k+1)t^2)/a.                            (6)

Every minimizing packet consists of signed copies from this list.
The total f_A weight is (L-1)/L, while the COMBINED f_B and f_C weight is1/L.
Either negative-type label may be absent, and each present label may be repeated with positive weights and either overall sign.
Thus a two-label rational attainer uses f_A and f_B at weights (L-1)/L,1/L; using f_C instead also works in the odd case.
Real weights may be split irrationally in the formal-real equality class; assertions about their least integer denominator below apply to the rational class only.

The root-supplied candidate is established next with every parity, positivity, equality and cost condition explicit.

<a id="quadratic-parameter-square-identities"></a>
## 3. Positive Toeplitz form and complete integer minima

Let W be the rational symmetric Toeplitz matrix

    W=[[1,a/(2L),a^2/(2L)-1],
       [a/(2L),1,a/(2L)],
       [a^2/(2L)-1,a/(2L),1]].                     (7)

For the actual residue (m,n) from (3), put ell=n+k m.
Direct expansion gives

    a=2k:
      f^T W f=(m^2+ell^2)/L+(1-1/L)y^2;

    a=2k+1:
      f^T W f=(m^2+m ell+ell^2)/L+(1-1/L)y^2.       (8)

Here f in the quadratic form denotes its coefficient column (x,y,z).
To check every coefficient, in the even case ell=kx+y+kz; in the odd case ell=kx+y+(k+1)z.
The binary numerator in either case has x^2 and z^2 coefficients L, y^2 coefficient1, xy and yz coefficients a, and xz coefficient a^2-2L.
Adding (L-1)y^2 and dividing by L produces exactly the diagonal and doubled off-diagonal entries in (7).
Thus no parity-dependent factor2 is missing.

Both forms in (8) are positive definite.
For the odd binary form,

    m^2+m ell+ell^2=(ell+m/2)^2+3m^2/4.

Its even analogue is a sum of two squares.
The coefficient1-1/L is positive, since L>=3.
The transformation (x,y,z)->(m,n,y) is invertible because a!=0: z=(n-y)/a and x=m+z.
Thus all terms in (8) vanish only for f=0, proving W>0 on the entire real coefficient space.

For nonzero integer (m,n), the integer transformation (m,n)->(m,ell) is unimodular.
In the even case its nonzero binary minimum is1, attained only at

    (m,ell)=(0,+/-1),(+/-1,0).

In the odd case the positive binary form is an integer, so its nonzero minimum is at least1.
Equality implies3m^2/4<=1, hence m=0,+1,-1.
At m=0 one has ell=+/-1; at m=1, ell=0,-1; and at m=-1, ell=0,1.
Therefore its complete value1 set is

    (m,ell)=(0,+/-1),(+/-1,0),(1,-1),(-1,1).        (9)

All six vectors do occur.
This elementary enumeration is complete, with no search cap or unproved shortest-vector premise.

For fixed residue (m,n), the representative y=0 is always available, with x=m+n/a and z=n/a.
Hence (8) is also the exact weighted least-norm quotient calculation; its residue form is uniformly

    G_W=[[1,a/(2L)],[a/(2L),1/L]],
    min_(0!=r in Z^2) r^T G_W r=1/L.               (10)

Indeed both binary forms expand to Lm^2+a mn+n^2.
This agrees with the C16 quotient formula (A W^-1 A^T)^-1, without relying on an unverified matrix inverse.

<a id="quadratic-parameter-complementarity-and-equality"></a>
## 4. Exact cancellation and necessity of the stated masses

The constant covariance condition is exactly vanishing of the weighted lag-one and lag-two coefficients:

    sum_b omega_b y_b(x_b+z_b)=0,
    sum_b omega_b x_b z_b=0.

Because W has diagonal1 and constant entries on each off-diagonal, these two equations imply sum omega_b f_b^T W f_b=E.
Equation (8) and the nonzero integer residue condition therefore give E>=1/L for every allowed rational or formal-real packet.

At equality every positive-weight coordinate must satisfy y=0 and its binary form must have value1.
For even a, the four vectors above give exactly signed f_A and f_B in (5).
For odd a, (9) gives exactly signed f_A,f_B,f_C in (6): the residues of their positive representatives are respectively

    (0,1), (1,-k), and (1,-k-1) in the odd case,
    (0,1), (1,-k) in the even case.                 (11)

No coordinate with nonzero y, different residue or additional coefficient shape can appear at equality, because all weights are strictly positive.

All these coordinates have lag one zero.
f_A has lag-two coefficient1/a^2.
Every other type has lag-two coefficient

    -(L-1)/a^2.

For even a this is -1/4, since L-1=k^2 and a=2k.
For odd a it is -k(k+1)/a^2 for both f_B and f_C.
If p is the total weight of f_A copies, exact lag-two cancellation is

    p/a^2-(1-p)(L-1)/a^2=0,
    p=(L-1)/L.                                    (12)

An overall sign leaves each autocorrelation unchanged.
Thus all the equality classifications and total weights in Section2 are necessary, including the combined rather than individual odd B/C mass.

Conversely, every finite packet of the listed signed types with those total masses has both lags zero.
Its weighted W energy is1/L by (8), hence its ordinary aggregate energy is1/L as well.
The displayed two-label rational packet proves actual attainment.
The C16 weak bound mu(W)<=Gamma_2^Q<=E_2^Q, together with (10), now proves all of (4), with an actual dual maximizer.
No general dual-completeness theorem is needed for this matched certificate.

All prototype polynomials have nonzero constant and t^2 coefficients, so every equality packet has actual common union width2 in this allowed window.
A common Laurent shift translates that window and multiplies values by an actual unit, with full norm1.
No independent support enlargement or omitted endpoint is hidden in the classification.

<a id="quadratic-parameter-actual-integrality-and-norms"></a>
## 5. Actual order values and every original signed norm

The relation alpha^2=a alpha-1 gives

    f_A(alpha)=alpha,
    f_B(alpha)=1-k alpha,
    f_C(alpha)=1-(k+1)alpha in the odd case.

These values belong to the ACTUAL O_0.
The degree-below2 residue coordinates in (11) are nonzero, so the values are nonzero by irreducibility.
There is no inference of order membership from norm size.

For any integer c,

    Norm_K(1-c alpha)=1-a c+c^2.

Consequently in every parameter case,

    D_A=+1,
    D_B=-(L-2),
    D_C=-(L-2) when present.                        (13)

For a=2k use1-2k^2+k^2=1-k^2.
For a=2k+1 use1-(2k+1)k+k^2=1-k(k+1), and replacing k by k+1 gives the same value.
Since L>=3, these negative norms are never zero.
At the endpoint a=3, L=3 and D_B=D_C=-1; those labels are units.
For all a>=4 their absolute norm is greater than1.
No unit-only optimality statement is inferred from the larger allowed class.

Both original conjugates are included in these degree-two norms.
Overall signs do not change them, since Norm_K(-1)=1.
The order is stable under alpha->alpha^-1=a-alpha; in this quadratic field the relative involution is the original conjugation.
As a consistency check, the weighted field norm profile is

    ((L-1)/L)*1+(1/L)*[-(L-2)]=1/L.

This uses the complete original field, not a discarded exterior factor or trace-degree replacement.

<a id="quadratic-parameter-denominators-and-full-costs"></a>
## 6. Least denominators, contents and complete copied products

For the standard two-label packet, the ACTUAL least coefficient denominator is q=a.
The f_A coefficients include1/a, while every other prototype coefficient denominator divides a; in the even case a is divisible by2.
Its weights have ACTUAL least denominator M=L, since they are (L-1)/L and1/L.

More generally every rational equality packet contains an f_A copy with positive total mass, so q=a still holds.
Clearing all its final weights by the least M makes the combined non-A multiplicity M/L an integer.
Therefore L divides M.
Arbitrary positive rational splitting can increase M; it is not always equal to L.

The integer numerators and their contents/energies are:

| Parameter | Numerator F_A | Other possible numerator | Contents | Coefficient energies |
| --- | --- | --- | --- | --- |
| a=2k | 1+t^2 | k(1-t^2) | 1,k | 2,2k^2=2(L-1) |
| a=2k+1 | 1+t^2 | (k+1)-k t^2, or k-(k+1)t^2 | 1,1 | 2,k^2+(k+1)^2=2L-1 |

The odd contents are1 because the two nonzero coefficients are consecutive integers.
The numerator height of the non-A coordinate is k in the even case and k+1 in the odd case; its coefficient absolute sum is a.
The common actual degree/window is2, not the degree of a power or an enlarged parent polynomial.

Every original full numerator resultant is

    Res(P_a,F_A)=a^2,
    Res(P_a,F_B)=-a^2(L-2),
    Res(P_a,F_C)=-a^2(L-2) when C is present.

For the standard packet the complete signed product, integer covariance and income are

    product_b Res(P_a,F_b)^(M omega_b)
        =-a^(2L)(L-2),
    S=q^2 E=a^2/L,
    I=log a+log(L-2)/(2L),
    I-(1/2)log S=(1/2)log L+log(L-2)/(2L).          (14)

The positive-type multiplicity is L-1 and the negative-type multiplicity is1, which determines the sign in this product.
For an arbitrary rational equality packet the CORRECT general product is instead

    a^(2M)[-(L-2)]^(M/L), L divides M.              (15)

Its q,S,I and surplus remain the values in (14), since its total masses and norm types are fixed.
In particular the sign can change when the negative total multiplicity M/L is even.
The two-label signed formula is not imposed on a split packet with different M.

Every content is retained.
The even content k divides q=a=2k although its residue usually has nonunit norm; this is consistent with C14's sufficient-not-necessary content criterion.
Dividing that numerator by k while retaining its old value, weights, energy or norm would be invalid.
In general the exact content restriction is c^2 dividing a^2 D_b, with the original degree2.

The [C10 exact original-root inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) applies to these actual integer numerators, positive normalized weights, nonzero resultants and common T=2.
It charges their ENTIRE surplus at

    (1/2)log L+log(L-2)/(2L)
       <=(T/d)m(P_a)=m(P_a)=arcosh(a/2).            (16)

No content, scalar, weight multiplicity, negative norm or original root is removed.
The already accepted finite proof has no small-height restriction.
This calibration does not turn a norm lower floor into an actual-order divisibility statement.

<a id="quadratic-parameter-euclidean-comparison"></a>
## 7. Exact comparison with the old Euclidean quotient minimum

Here

    A=[[1,0,-1],[0,1,a]],
    AA^T=[[2,-a],[-a,a^2+1]],
    det(AA^T)=a^2+2.

Direct inversion and square completion give

    r^T(AA^T)^-1 r
      =[(a^2+1)m^2+2a mn+2n^2]/(a^2+2)
      =m^2/2+[2/(a^2+2)](n+a m/2)^2.              (17)

If m!=0 the value is at least1/2, whereas2/(a^2+2)<1/2 for a>=3.
If m=0, a nonzero integer n gives the minimum exactly at n=+/-1.
Therefore the complete Euclidean residue minimum is2/(a^2+2), with the two shortest coefficient representatives

    +/-(a+2t+a t^2)/(a^2+2).

This is precisely the j=1 representative already retained in L249.
Its value is +/-alpha; it is not a newly discovered scalar projection.
Each representative has positive lag-two autocorrelation a^2/(a^2+2)^2 (and positive lag one4a/(a^2+2)^2).
Overall signs do not change either.
Hence no positive normalized mixture of those Euclidean shortest representatives alone can be exactly complementary.

The new complete optimum is therefore strictly above that scalar quotient floor, with exact ratio

    (1/L)/[2/(a^2+2)]=(a^2+2)/(2L)
      =2-4/(a^2+4) for even a,
      =2-2/(a^2+3) for odd a,
    ratio ->2 as integer a->infinity.               (18)

This is a comparison against the COMPLETE nonzero integer Euclidean residue lattice, not a finite selected seed list.
It quantifies the cost of exact autocorrelation cancellation after actual integrality is kept.

<a id="quadratic-parameter-scope-and-self-check"></a>
## 8. Parameter dependence, existing boundaries and complete self-check

The family already has fixed degree2 and increasing original coefficient a.
Its exact asymptotic charges are

    a^2 E_2 ->4, q=a,
    M=L~a^2/4 for the standard packet,
    S=a^2/L ->4,
    m(P_a)-log a ->0,
    m(P_a)-[ (1/2)log L+log(L-2)/(2L) ] ->log2.    (19)

For the measure limit, alpha/a=(1+sqrt(1-4/a^2))/2 tends to1.
For the remaining limits use L/a^2->1/4 and log(L-2)/L->0.
Thus the normalized complementary energy tends to zero while the actual total Mahler measure tends to infinity, the least coefficient denominator grows linearly and the displayed least weight denominator grows quadratically.
This is coefficient dependence at fixed degree, not a near-one sequence.
The individual signs and nonunit norms in (13)--(16) explain the arithmetic part of that coupling.

At a=4 the formulas reproduce C16's already accepted E_2=1/5 result, not a new fixed control.
At a=3 they give E_2=1/3 in width2.
C15's existing a=3 packet has E=1/4 in width4 and fixes a different near-minimum integer-energy regime; it does not contradict the present smaller-window minimum.
More generally S=a^2/L here is not C14's q=2,S=2 boundary or C15's single-extra-integer-energy condition.
The new theorem optimizes E over ALL allowed rational coefficient and positive rational weight choices at this fixed window.
No growing number of labels is required for the attaining examples, but arbitrary label counts are included in the lower proof.

The parameter a is an integer throughout.
The actual order, integer residue lattice, least denominators and odd/even shortest-vector sets do not support a continuous-a version by formal substitution.
No maximal-order claim, prescribed unit-only inventory, unrestricted gap or uniform deficit on small-total-measure inputs is asserted.
No general principle of quadratic forms or complementary-binomial existence is claimed novel.

Author self-check reconstructed the actual discriminant intervals, original two-root norm and measure, nonmaximal-order guard and power-basis membership; both full coefficient expansions in (8), positivity on all real coefficients, the unimodular residue change, all four/six shortest vectors and every equality coordinate; positive-weight equality implications, zero lag-one and exact lag-two masses, absent/present odd labels and signs; rational versus formal-real weight scope; every actual residue, original signed norm and the a=3 endpoint; q=a necessity, M=L for two labels and L|M for all rational minimizers; complete coefficient contents, heights, integer energies and copied product signs in both standard and split packets; C10's actual hypotheses and paid window; the old Euclidean quotient and shortest representatives with their positive lags; the exact improvement ratios and growing-measure limits.
Root supplied the substantive full candidate; this is author self-review only.

No native mathematical program, scan, solver, new external theorem, J or source-intake write was used.
Separate whole noncontributor review and root adoption remain pending.
G0001 remains active and unrestrictedly unresolved.

<a id="quadratic-parameter-entire-author-freeze"></a>
The COMPLETE Sections1--8, the theorem and both odd/even equality classifications, equations(1)--(19), all original norm/denominator/content/multiplicity costs, reuse and growing-measure boundaries are author-frozen at2026-10-11T19:10 for a separately organized whole noncontributor review.
Scoped material validation passed before this paragraph and is repeated afterward; it checks structure and locators rather than mathematics.
Root supplied the substantive candidate and cannot be the whole noncontributor reviewer.
Author development stops at this freeze.



## Registration and preservation operation

2026-10-11T19:18: retain the COMPLETE2026-10-11T19:10 D15 freeze directly as the Claim argument.
The separate reviewer has reconstructed the candidate and will check this actual registered statement and current interfaces before giving C-specific bindings.
Original contribution and historical reuse boundaries remain.
The original D is retired only after full-body comparison and incoming-reference maintenance.
No native mathematical program, new allowance or Task completion accompanies registration.
