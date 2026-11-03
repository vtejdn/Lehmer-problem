---
author: Yin
---

# Exact local height-one masks and a sharpened multiplier obstruction

Human author Yin.
Provenance: project deduction under the unchanged [G0001 original contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the symmetric half-sum mask, sharpened degree endpoint and exact local count.
The characteristic_zero_bridge agent checked and authored the full squared-modulus equivalence with old-source overlap, integer trace carry, ambient reciprocity, mask realization, endpoint signs, exact counting, weak-ceiling cases and raised-source descent.
Root read the entire saved WM1--WM15 argument.
Both agents are substantive contributors; this open fixed candidate awaits fresh isolated whole review and a separate acceptance decision.
No native coefficient expansion, actual support-rank calculation or sign search is used.

## Statement

Use C_0=2,C_1=X,C_(j+1)=XC_j-C_(j-1), with bars denoting coefficient reduction modulo2.
For odd n=2a+1, let B_n=1+sum_(j=1)^a C_jbar be the COMPLETE polynomial of nonidentity n-th-root traces, one root per inverse pair.
For every monic integer trace T use its OWN actual canonical system

    a_T=rem_T(T(C_2))/2,
    b_T=rem_T(T(C_3))/3,
    c_T=rem_T(T(C_5))/5,
    F_T=rem_T(2c_T^2-3a_T^5),
    G_T=rem_T(c_T^3-2b_T^5),
    X_(s,T)=rem_T(b_T^2-a_T^3+s G_T), s in{1,-1}.

Every scalar division is in Z[X] before binary reduction, and every remainder is taken with the indicated SAME monic divisor.
Height1 means all integer coefficients belong to{0,1,-1}, with maximum absolute value1.
The multiplier parameter a is distinct from the canonical polynomial a_T.

### A. Exact local mask and all height-one lifts

Start with an actual complete bounded source Y from the [adopted C691 construction](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24), at ell>=82, Q=2^ell and m=Q/4-2.
Retain every full factor and multiplicity, its actual selected fresh order n_star, and

    phi=X^2+X+1, U_0=X^(2m)Y phi^(14m),
    d=deg U_0=30m+deg Y,
    Pbar_old(z)=z^d U_0(z+z^(-1)),
    Dbar=Pbar_old/(z^2+1), r=2d-2.

Dbar is an actual monic reciprocal binary polynomial of degree r, constant1 and central coefficient0.
Write its full support size as2k, where k counts the supported reciprocal pairs including (0,r).
For ANY integer a>=ceil(d/2) with n=2a+1 coprime to15, put U_a=U_0 B_n^2 and d_a=d+2a.
Then the full reciprocal binary polynomial is Pbar_a=Dbar(1+z^(2n)), of degree2d_a, with disjoint coefficient blocks.
Every monic reciprocal height1 integer lift of Pbar_a with constant1 is uniquely

    P=L+z^(2n)L^*, L^*=z^r L(z^(-1)),
    L(0)=1, deg L=r, Lbar=Dbar,

where each supported coefficient of L is either sign and every unsupported coefficient is0.
Use P's own monic trace T of degree d_a and set S=(L+L^*)/2 in Z[z].
For each sign s the following conditions are EQUIVALENT:

    B_n^2 | F_Tbar;
    B_n^2 | X_(s,T)bar;
    B_n | a_Tbar;
    S_n | Sbar, where S_n=(z^n+1)/(z+1);
    Sbar=(z+1)(z^n+1)J for J in the space below.

These are local conditions on the ADDED B_n^2 modulus, and remain equivalent when B_n overlaps the old source U_0.
They do not include any further old multiplicity on such an overlapping factor.
Set h=r-n-1=2(d-a-2) and A_n=(z+1)(z^n+1).
For h>=0 define

    Jspace={J in F_2[z]: deg J<=h,
              z^h J(z^(-1))=J,
              support(A_n J) subset support(Dbar)};

for h<0 define Jspace={0}.
This is a finite F_2 vector space, parametrizing exactly all allowed reciprocal same-sign-pair masks.
The displayed reciprocal equation uses ambient degree h, allowing zero leading and constant coefficients.
If e=dim Jspace, every J has EXACTLY 2^(k-1) distinct actual height1 lifts P, so the total local count is2^(e+k-1).
For h>=0 one has e<=min(k,d-a-1), without assuming a value of this actual rank.
The zero-mask fiber consists exactly of the2^(k-1) lifts with L^*=-L and

    P=L(1-z^(2n)).

They are reducible and contain the cyclotomic factor z-1.
The nonzero-mask fiber has exactly (2^e-1)2^(k-1) local lifts, without asserting their irreducibility or full-source residual conditions.
Consequently the number of irreducible lifts satisfying full evenness of either own residual is at most (2^e-1)2^(k-1).
Full evenness of F_T and full evenness of X_(s,T) are each sufficient to impose the local condition, but they are NOT asserted globally equivalent.
For comparison, [C731's complete-source first-bit interface](Yin_C_G0731_v1.md#decision-whole-reviewed-2026-10-25) retains the three full old-primary affine sign systems; their actual ranks and solvability are not determined by this local count.

### B. Sharper obstruction, endpoint and actual weak choice

For a>=d-1 the space Jspace is zero, so evenness of EITHER full own residual F_T or X_(s,T) forces the displayed factorization and reducibility.
This includes the endpoint a=d-1 and strengthens the previous a>=d conclusion in [C738 HB](Yin_C_G0738_v1.md#large-complete-multiplier-height-one-obstruction), without editing that fixed theorem.
At a=d-2, when this endpoint satisfies the stated coprimality assumptions, e=1 if and only if [z]Dbar=1; otherwise e=0.
This conditional coefficient criterion does not evaluate the actual complete source.
In the remaining range ceil(d/2)<=a<=d-2, any irreducible full first-bit lift must come from a NONZERO vector of the explicit homogeneous mask space, followed by all still-required old-primary equations.

For the actual complete WEAK multiplier of C738, put M=30Q n_star and a_mul=M ceil(d/(2M)).
Then

    a_mul>=d-1 iff d<=M+1 or d=2M+1.

If neither case holds, a_mul<=d-2 and the actual mask-space rank remains undetermined.
The comparison uses the actual degree d, not its upper bound, and does not assert which branch a particular uncomputed source occupies.

### C. Raised sources and full-source boundaries

For every q=2^j, height1 lifts P_q of Pbar_a^q are in bijection with the base lifts by P_q(z)=P(z^q), with full degree2q d_a and own trace T(C_q).
Exact canonical covariance identifies the added B_n^(2q) residual conditions with those of Part A, so all three local counts remain unchanged.
The zero-mask fiber is exactly

    P_q(z)=L(z^q)(1-z^(2nq)),

and full evenness descends to the base.
In particular the obstruction in Part B persists at every q with its complete original degree.

For a=a_mul, [adopted C738](Yin_C_G0738_v1.md#decision-whole-reviewed-2026-10-25) retains the COMPLETE source Y_star=Y B_n^2, U_star=U_a and R_star=R_0 B_n^2, where R_0=X^(2m)Y phi^(12m)B and B=X^(Q-m)H(C_5bar) is the original C691 polynomial.
Its two full forward divisibilities, original jets and doubled root identities, exact fresh multiplicity3, nonzero actual G_Tbar=R_star^q for Tbar=U_star^q, maximal dyadic exponent q, degree gap and full layer/synthetic-Haar data are inherited at their precise C738 scopes.
In particular

    deg Y_star<29040Q^3+7212Q^2+308Q,
    d_a<29040Q^3+7212Q^2+316Q,
    deg U_star-deg R_star=m-8-5deg H>5m/256.

At q the degrees and gap are multiplied by q, and the original reciprocal degree is2q d_a.
These are the enlarged paid bounds, not the original DG8 bounds.
The complete-source conclusions are not automatically asserted for every a in Part A's broader algebraic local domain.
The synthetic integer polynomial in C738 is not identified with the actual integer canonical G.
No full-source sign-system rank, passing irreducible height1 input, higher residual precision, total-Mahler bound, field-norm estimate or characteristic-zero identity is supplied by this theorem.
It neither excludes the original C691 source nor declares the full sign systems inconsistent.

## Complete argument

<a id="weak-multiplier-height-one-local-mask"></a>
### Exact added-component sign masks for the weaker complete multiplier

This is the complete fixed author argument contributed by root and characteristic_zero_bridge.
Root proposed the symmetric half-sum, sharpened endpoint and local counting mechanism; characteristic_zero_bridge checked the full squared-modulus equivalence, integer carry, ambient reciprocal quotient, endpoint signs, exact fibers and scope below.
The actual mathematical inputs are [adopted C738 PA and HB](Yin_C_G0738_v1.md#decision-whole-reviewed-2026-10-25), [C608's complete B_n Laurent/root interface](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23), and [C724's actual height1 support descent and canonical covariance](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25).
C738 supplies the full actual C691 source, its complete multiplier and every retained original cost and canonical/source condition; the new argument refines only the height1 conclusion for the added component.
The exact overlap issue is resolved here by polynomial divisibility, not by assuming that the old and added factors are coprime.
No coefficient scan, actual rank calculation or external theorem is used.

#### Full original support and the local residual condition

Use the SAME complete C691 base U_0 of degree d, with U_0 divisible by X^(2m), 2m>1, and its actual reciprocal polynomial Pbar_old=z^d U_0(z+z^(-1)).
Put

    Dbar=Pbar_old/(z^2+1), r=2d-2,
    Dbar=z^(d-1)(U_0/X)(z+z^(-1)).             (WM1)

As proved in C738 HB3--HB4, Dbar is monic reciprocal of degree r, has constant1, and has central coefficient0.
For completeness, each positive Chebyshev polynomial over F_2 has constant0, so a trace polynomial vanishing at0 has no constant Chebyshev-basis term.
The positive Chebyshev expansion of U_0/X therefore gives the stated zero central coefficient of Dbar.
Write its FULL support size as w_D=2k; the k supported pairs include the endpoint pair (0,r), and there is no supported central index.

For the algebraic local argument let a be any integer with a>=ceil(d/2), let n=2a+1 and assume gcd(n,15)=1.
Set

    U_a=U_0 B_n^2, d_a=d+2a,
    Pbar_a=z^(d_a)U_a(z+z^(-1))
           =Dbar(1+z^(2n)).                    (WM2)

The complete B_n is 1+sum_(j=1)^a C_jbar and satisfies z^a B_n(z+z^(-1))=(z^n+1)/(z+1).
Its degree is a, its roots are all distinct nonzero traces of nonidentity n-th roots, and gcd(n,15)=1 gives B_n|B_n(C_3bar) and B_n|B_n(C_5bar).
The arguments below apply to this algebraic domain without claiming that every such a preserves the original finite jets, exact fresh factor or canonical R_0 data.
For the actual complete family, take C738's a_mul=30Q n_star ceil(d/(60Q n_star)); all of those additional properties and its NEW paid degree bounds then hold by C738.
The argument also applies to any other a for which those full-source properties have separately been established.

Because 2n>r, the blocks in WM2 are disjoint.
Every monic reciprocal height1 integer lift P of Pbar_a, of constant1 and FULL degree 2d_a=r+2n, is uniquely

    P=L+z^(2n)L^*, L^*=z^r L(z^(-1)),
    L(0)=1, deg L=r, Lbar=Dbar.                (WM3)

Each supported coefficient of L is in{1,-1}; each unsupported coefficient, including the center, is0.
The coefficient of z^r in L is not fixed to1: either choice leaves P monic, since the high leading coefficient is L(0)=1.
Conversely every such L gives one of the specified monic reciprocal height1 lifts, so WM3 is a bijection with the actual allowed signs.
Let T be P's OWN monic integer trace polynomial of degree d_a.
All canonical a_T,b_T,c_T,F_T,G_T,X_(s,T) below are calculated using this same T and division by2,3,5 in Z before reduction; the multiplier parameter a is not the canonical polynomial a_T.

Define the ADDED-COMPONENT condition to be

    B_n^2 | X_(s,T)bar in F_2[X].              (WM4)

It is not the assertion X_(s,T)bar=0 on the full U_a quotient.
Since B_n^2 divides Tbar and Tbar(C_p) for p=3,5, reducing the actual monic division and then using the odd scalar division gives

    B_n^2 | b_Tbar and B_n^2 | c_Tbar.

Consequently the actual remainder polynomials satisfy

    F_Tbar = a_Tbar^5 modulo B_n^2,
    X_(s,T)bar = a_Tbar^3 modulo B_n^2.         (WM5)

These statements use only that B_n^2 divides the full Tbar, so they remain valid when B_n and U_0 share factors with arbitrary old multiplicities.
Because B_n is squarefree, B_n^2 divides either displayed power if and only if B_n divides a_Tbar.
Thus the added-component first and second residual conditions are equivalent to each other, to B_n|a_Tbar, and are independent of s=1 or-1.
Evenness of EITHER full own residual F_T or X_(s,T) implies this local condition, but their GLOBAL evenness conditions are not asserted equivalent.
In particular local satisfaction does not settle the additional multiplicity on an old factor that also occurs in B_n, or any other old primary condition.

#### Integer carry and the exact reciprocal mask

Define the actual integer half-difference and half-sum

    E=(L^*-L)/2, S=(L+L^*)/2=L+E.              (WM6)

Both are integral because Lbar=L^*bar=Dbar.
The polynomial S is reciprocal with ambient degree r and central coefficient0, and Sbar=Ebar+Dbar.
At a supported pair its two coefficients in S are equal and are either1,-1, or0.
The binary coefficient is1 precisely when the two signs in L agree, and0 precisely when they are opposite.
At every unsupported index S is0.
Thus Sbar is the supported same-sign-pair mask, and Sbar=0 if and only if S=0 as an integer polynomial.

For any integer polynomial A write Delta(A)=[A(z^2)-A(z)^2]/2; also write Delta_T=[T(C_2)-T^2]/2.
Coefficient Frobenius makes these integral, and a_T=rem_T Delta_T.
The exact trace identity and block expansion give

    Delta(P)=z^(2d_a)Delta_T(z+z^(-1)),
    Delta(P)=Delta(L)+z^(4n)Delta(L^*)-z^(2n)LL^*,
    Delta(L^*)-Delta(L)=E(z^2)-2LE-2E^2.       (WM7)

All divisions in WM7 precede binary reduction.
At EVERY nonidentity n-th root zeta in the algebraic closure of F_2, WM7 gives

    Delta(P)bar(zeta)=Ebar(zeta)^2+Dbar(zeta)^2
                     =Sbar(zeta)^2.

No value of Dbar(zeta) is assumed nonzero.
The nonzero factor zeta^(2d_a), the trace identity, and a_T=rem_T Delta_T show that B_n|a_Tbar if and only if Sbar vanishes at all those n-1 distinct roots.
Equivalently, with S_n(z)=1+z+...+z^(n-1), the EXACT added-component condition is

    S_n | Sbar.                               (WM8)

This proves both implications, including the direction from a chosen mask to the genuine canonical condition.

The even ambient degree r and zero central coefficient imply Sbar(1)=Sbar'(1)=0.
Indeed the two entries in every supported pair sum to0 at1, and their contributions to the derivative sum to (j+r-j)Sbar_j=r Sbar_j=0 in F_2.
Thus (z+1)^2 divides Sbar.
Since n is odd, S_n(1)=1, so S_n is coprime to z+1 and WM8 is equivalent to

    Sbar=A_n J, A_n=(z+1)(z^n+1),
    deg J<=h=r-n-1=2(d-a-2).                   (WM9)

When h<0 the only allowable J is0.
When h>=0, A_n is monic reciprocal of degree n+1 and constant1, and its product has ambient reciprocal degree r if and only if

    z^h J(z^(-1))=J(z).                        (WM10)

To verify the implication from the product, reverse the polynomial using these ambient degrees and cancel the nonzero factor A_n in F_2[z].
The reverse implication follows by multiplication.
Ambient reciprocity allows the highest and lowest coefficients of J to be zero; it is not a demand that every nonzero J have actual degree h or constant1.

Define the finite F_2 vector space

    Jspace={J: deg J<=h, z^h J(z^(-1))=J,
              support(A_n J) subset support(Dbar)}              (WM11)

for h>=0, and define Jspace={0} for h<0.
The support condition is a family of homogeneous linear zero-coefficient equations and automatically imposes the required central zero, because the center is outside support(Dbar).
Multiplication by A_n is injective, so Jspace parametrizes exactly the reciprocal supported masks satisfying the local residual condition.
If e=dim_F2 Jspace and h>=0, then e<=min(k,h/2+1)=min(k,d-a-1); no value of this actual rank is assumed or calculated.

#### Every allowed mask is realizable, with exact local counting

For any J in Jspace, set sigma=A_n J.
For a supported pair {j,r-j}, sigma_j=sigma_(r-j) specifies whether its two signs must agree or disagree.
There is no further condition on an individual pair.
For the endpoint pair, L(0)=1 makes L_r=1 when sigma_0=1, and L_r=-1 when sigma_0=0, so this pair has exactly one choice.
For each of the other k-1 supported pairs choose L_j freely in{1,-1}; then set L_(r-j)=L_j if sigma_j=1 and L_(r-j)=-L_j if sigma_j=0.
Set every unsupported coefficient to0.
This constructs every allowed L with mask sigma once and only once; its actual integer half-sum reduces to sigma.
The full block polynomial P is then a valid monic reciprocal height1 lift, and WM4--WM8 prove its added-component condition.
Thus each J has exactly 2^(k-1) lifts, and

    number of local passing lifts = 2^(e+k-1),
    number with J=0              = 2^(k-1),
    number with J!=0             = (2^e-1)2^(k-1).                (WM12)

These counts concern distinct actual P (equivalently their own traces T), because WM3 is unique.
They count the ADDED B_n^2 condition, not the three full-source systems of C731 or any higher residual bits.
In particular the local condition is always solvable: its zero-mask fiber is nonempty, even when all full-source systems remain undecided.

The zero-mask fiber has S=0, hence L^*=-L and

    P=L(1-z^(2n)).                            (WM13)

Both factors are nonconstant and P has the cyclotomic factor z-1.
Conversely this antisymmetry gives J=0, so this is exactly the counted zero-mask fiber.
Nonzero J does not imply irreducibility, global first-bit satisfaction, or absence of some other cyclotomic factor.
Any irreducible full first-bit lift must come from nonzero J, so its number is at most (2^e-1)2^(k-1), without asserting that this upper bound is attained or that any such lift exists.
The same necessary bound applies if only one of the two full own residuals is required to be even.

#### Sharpened endpoint, actual ceiling choice and raised sources

If a>=d-1 then h<0, so every local passing height1 lift is in WM13.
Therefore evenness of EITHER full own residual F_T or X_(s,T) forces reducibility for this sharper range, including a=d-1.
This strictly extends C738 HB's previously proved a>=d endpoint without changing that fixed theorem or its stronger-source cost.
It still concerns this added-multiplier domain, not the original C691 source.

At the next endpoint a=d-2, h=0, so J is0 or1.
Here n+1=r and A_n=1+z+z^(r-1)+z^r.
The two endpoints already belong to support(Dbar), and the two inner positions are paired and distinct from the center since the actual C691 degree d is greater than3.
Consequently e=1 exactly when [z]Dbar=1, and e=0 otherwise.
This criterion is conditional on this endpoint satisfying the original n-coprimality assumptions and is not a calculated coefficient of the actual source.
When ceil(d/2)<=a<=d-2 in general, WM11 is the explicit lower-degree homogeneous support system that every potentially irreducible lift must satisfy nontrivially.

For C738's actual WEAK ceiling, write M=30Q n_star, t=ceil(d/(2M)), so a_mul=Mt.
Its location in the forced-reducible range is exactly

    a_mul>=d-1
       iff d<=M+1 or d=2M+1.                  (WM14)

For t=1 this follows from a_mul=M, and for t=2 the inequalities 2M<d<=2M+1 leave precisely d=2M+1.
For t>=3 the integer lower bound d>=2M(t-1)+1 exceeds Mt+1, so the condition fails.
If neither case in WM14 holds, the same actual weak ceiling has a_mul<=d-2 and its mask-space dimension remains to be determined from the complete Dbar.
No supplied upper degree bound alone is substituted for this actual comparison, and no branch is asserted for an uncomputed chosen representative.

Finally let q=2^j and consider height1 monic reciprocal lifts of Pbar_a^q, with FULL original degree 2q d_a.
The exact height1 support argument gives a bijection P_q(z)=P(z^q) with the base lifts in WM3, and their own traces satisfy T_q=T(C_q).
By the adopted all-six canonical covariance, the binary first and second residuals are the corresponding base residuals composed with X^q.
Hence divisibility by the ADDED B_n^(2q) is equivalent to the base added B_n^2 condition; all three exact counts in WM12 are unchanged at each q.
Full evenness descends as well.
The zero-mask lifts are exactly

    P_q(z)=L(z^q)(1-z^(2nq)),                  (WM15)

and are reducible with their full degree retained.
For the actual complete weak multiplier, C738 supplies the maximal dyadic exponent q, the unchanged degree gap, nonzero ACTUAL canonical Gbar=R_star^q, complete source multiplicities and its enlarged paid degree, layer and synthetic-Haar statements.
Those facts are not inferred from the local count, and the synthetic polynomial is not identified with the actual integer canonical G.
Neither a full sign-system rank, an irreducible height1 realization, higher precision, an original total-Mahler bound nor a characteristic-zero identity is supplied by WM1--WM15.
The remaining concrete question in the genuine weak range is whether the ACTUAL support-mask space has a nonzero vector that also extends to the full old-primary conditions and an irreducible original input.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision local-mask-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T19:28 |
| status | open |
| reason | Register the complete WM1--WM15 author theorem after root read the whole saved argument. The added squared-component condition has an exact reciprocal support-mask parameterization and local height1 count, allowing old-source overlap. Full evenness of either own residual separately forces reducibility when a>=d-1; the weaker range retains an explicit undetermined mask space and every old-primary obligation. The actual weak ceiling and all dyadic support descents retain their precise scopes and costs. Both contributors are authors of this argument; fresh isolated whole review and a separate acceptance decision remain outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact local masks, endpoint and raised-source theorem](#statement) | Parts A--C, including the complete original source, broader explicitly local a-domain, all actual integer divisions, equivalence only at the added squared modulus, exact sign fibers/counts, sharpened obstruction, conditional endpoint, actual weak-ceiling cases, full original degrees and every unresolved global/analytic boundary. |
| argument | [Entire WM1--WM15 proof](#complete-argument) | Full support and local odd quotients, genuine integer trace carry, all nonidentity roots with overlap, reciprocal quotient and central constraint, realization/counting including the fixed constant endpoint, zero-mask factorization, actual ceiling cases and all-q exact descent. |
| dependency | [Adopted complete parity-zero multiplier and carry input](Yin_C_G0738_v1.md#decision-whole-reviewed-2026-10-25) | PA1--PA12 actual complete C691 multiplier/source and enlarged expense; HB3--HB7 full reciprocal quotient, central coefficient, separated-support form and exact integer carry. Its old a>=d obstruction informs the new a>=d-1 refinement but is not claimed to prove it; generic finite-precision existence imports no height1 or irreducibility. |
| dependency | [Adopted complete original source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 complete bounded starting Y, original H/B/U_0/R_0 and multiplicities, retained fresh order and exact triple factor, source degree/gap and canonical/root/layer data as consumed through C738. No original numerical bound is assigned to the enlarged source. |
| dependency | [Adopted complete Chebyshev-root interface](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23) | Full B_n Laurent geometric sum, squarefree nonidentity-root trace set and inverse-pair correspondence; powers3/5 permute this complete set when gcd(n,15)=1. No native finite support scan or unrelated gate exclusion is used. |
| dependency | [Adopted exact height1 descent and covariance](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Exact height1 support substitution, actual integer trace composition and all-six canonical covariance. Used for the bijection at every q and local/global evenness descent with full degree; no ascending irreducibility or unconstructed field norm is inferred. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T19:37 |
| status | proved |
| reason | Adopt the complete Parts A--C and WM1--WM15 theorem after fresh isolated whole R960 PASS. Root read the entire saved mathematical argument, its fixed statement and selected input scopes, and the full independent finding. The actual own-divisor squared-component equivalence survives old-factor overlap; the integer half-sum and double root at one give the exact ambient reciprocal support space, converse realization and local counts with the endpoint sign fixed. The zero-mask fiber, sharpened a>=d-1 obstruction, conditional next endpoint, exact weak-ceiling alternatives and all-q descent retain their complete scope. No actual mask rank, old-primary compatibility, irreducible realization, higher residual precision, characteristic-zero identity, Mahler bound or unrestricted Task completion is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact local masks, endpoint and raised-source theorem](#statement) | Parts A--C, including the complete original source, broader explicitly local a-domain, all actual integer divisions, equivalence only at the added squared modulus, exact sign fibers/counts, sharpened obstruction, conditional endpoint, actual weak-ceiling cases, full original degrees and every unresolved global/analytic boundary. |
| argument | [Entire WM1--WM15 proof](#complete-argument) | Full support and local odd quotients, genuine integer trace carry, all nonidentity roots with overlap, reciprocal quotient and central constraint, realization/counting including the fixed constant endpoint, zero-mask factorization, actual ceiling cases and all-q exact descent. |
| dependency | [Adopted complete parity-zero multiplier and carry input](Yin_C_G0738_v1.md#decision-whole-reviewed-2026-10-25) | PA1--PA12 actual complete C691 multiplier/source and enlarged expense; HB3--HB7 full reciprocal quotient, central coefficient, separated-support form and exact integer carry. Its old a>=d obstruction informs the new a>=d-1 refinement but is not claimed to prove it; generic finite-precision existence imports no height1 or irreducibility. |
| dependency | [Adopted complete original source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 complete bounded starting Y, original H/B/U_0/R_0 and multiplicities, retained fresh order and exact triple factor, source degree/gap and canonical/root/layer data as consumed through C738. No original numerical bound is assigned to the enlarged source. |
| dependency | [Adopted complete Chebyshev-root interface](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23) | Full B_n Laurent geometric sum, squarefree nonidentity-root trace set and inverse-pair correspondence; powers3/5 permute this complete set when gcd(n,15)=1. No native finite support scan or unrelated gate exclusion is used. |
| dependency | [Adopted exact height1 descent and covariance](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Exact height1 support substitution, actual integer trace composition and all-six canonical covariance. Used for the bijection at every q and local/global evenness descent with full degree; no ascending irreducibility or unconstructed field norm is inferred. |
| review | [Fresh independent whole local-mask finding](../audits/reviews/Yin_R_G0960_v1.md#whole-local-mask-finding) | Entire fixed Parts A--C and WM1--WM15, complete squared modulus with overlap, true carries, reciprocal support equations and exact counts, sharpened endpoint and actual ceiling, all-q descent, original expenses and the full local/global/source limits. |

