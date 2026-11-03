---
author: Yin
---

# Height-one signs for the complete canonical source reduce to three affine systems

Human author Yin.
Provenance: project deduction under the unchanged [G0001 original contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the restricted sign-space, square carry and three local branches, and contributed the dyadic-coefficient form of the support obstruction.
The characteristic_zero_bridge agent checked the full source, actual monic trace conversion and carry, every primary exponent, reciprocal nonsquareness and exact descent, and derived the support-weight obstruction and explicit finite interfaces.
Root read the entire HS1--HS15 argument and descent and directly reread the consumed C691 DG1--DG8 source scope.
Both agents are contributors; this open fixed candidate awaits fresh isolated whole review and a separate adoption decision.
No native coefficient expansion, sign search or new source acquisition has been run.

<a id="height-one-full-source-first-bit-interface"></a>
## Statement

Use C_0=2,C_1=X,C_(j+1)=X C_j-C_(j-1), and the SAME actual canonical integer polynomials for each monic trace divisor T:

    a(T)=rem_T(T(C_2))/2,
    b(T)=rem_T(T(C_3))/3,
    c(T)=rem_T(T(C_5))/5,
    F(T)=rem_T(2c(T)^2-3a(T)^5),
    G(T)=rem_T(c(T)^3-2b(T)^5),
    X_s(T)=rem_T(b(T)^2-a(T)^3+s G(T)), s in{1,-1}.

Every displayed scalar division is taken in the integer coefficient module before reduction modulo2.
Write ord_2 for the minimum coefficient2-adic order, with ord_2(0)=infinity.
For a monic integer P, H(P) is its maximum absolute coefficient, S(P)=max_(|z|=1)|P(z)| is its true circle supremum, and m(P) is the complete sum of log max(1,|lambda|) over ALL original roots with multiplicity.

For every ell>=82, Q=2^ell and m=Q/4-2, fix one actual COMPLETE Y supplied by [C691 DG1--DG8](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24), retaining its prescribed H,B, finite jets, both forward divisibilities, all repeated factors and fresh exact triple factor.
The source exponent ell, denoted s in C691, is separate from the residual sign s in{1,-1}.
Put phi=X^2+X+1, chi=X phi^2, Psi=phi(chi), H_0=X^(2m)Y, U_0=H_0 phi^(14m), R_0=H_0 phi^(12m)B, C_00=X^(2m)Y(chi)Psi^(14m) and d=30m+deg Y.
The complete original reciprocal binary polynomial is Pbar_0(z)=z^d U_0(z+z^(-1)); R_0 denotes canonical binary G, never this original polynomial.
The source formal notation used below is h_Q(X)=1+sum_(i=0)^(ell-1)X^(Q-2^i), and x is the compositional inverse of chi at0.
All inverse unit series below are taken in F_2[[X]] at0 or the explicitly stated phi-primary quotient.

The polynomial Pbar_0 is nonsquare.
Its complete coefficient support determines the unique integer lift P_+ with all supported coefficients+1, its monic trace T_+, and exactly the sign family T_epsilon=T_+-2V_epsilon of HS3.
The original monic and reciprocal endpoint coefficients are fixed at1; the central coefficient is proved0 for this source.
The allowed directions are precisely V_epsilonbar=sum_(j in I)epsilon_j C_jbar for the supported paired indices I, never an unrestricted trace residue.
Define alpha=rem_(U_0)([T_+(C_2)-T_+^2]/2 modulo2).
For every allowed sign choice, a_bar=alpha+rem_(U_0)(V_epsilonbar^2), b_bar=0 and G_bar=R_0!=0.

Factor the FULL H_0=product_f f^(e_f) and put H_third=product_f f^(ceil(e_f/3)) and M=H_third phi^(6m).
For each of the EXACTLY three cube-one units zeta modulo phi^(2m), let t_zeta in F_2[X]/M be the unique CRT class equal to0 modulo H_third and to phi^(4m)zeta C_00 modulo phi^(6m).
Then an allowed height1 lift has F=X_s=0 modulo2, for either and hence both signs, if and only if its sign vector solves one of the three affine linear systems

    sum_(j in I) epsilon_j rem_M(C_jbar^2)
                       =t_zeta+rem_M(alpha).

These matrices have deg M rows and |I| columns, with deg M<=13m+deg Y/2<=7200Q^3+603Q^2+64Q and |I|<=d-1.
The full degree, canonical gap and source costs are precisely HS1--HS2; no root or factor is removed.

If w is the number of nonzero coefficients of the COMPLETE Pbar_0, a necessary feasibility condition is

    w=0 modulo4,
    w/2 modulo2=sum_(h>=0)[X^(2^h)]U_0.

The first possible contribution is [X^(Q/2)]U_0=[X^4](Y phi^(14m))=[X^2]H^(-1), but all later powers through d must still be included.
Only floor(log_2 d)+1 coefficient queries are needed to state this parity test; no efficient coefficient-extraction algorithm or evaluated parity is asserted.

For every q=2^k, every height1 monic reciprocal integer P of constant1 with reduction Pbar_0^q is uniquely Q_int(z^q) for one of these SAME signed bases Q_int, and q is its maximal actual dyadic composition exponent.
All six canonical polynomials compose exactly, so all residual orders and first-bit feasibility descend exactly to this one base, while binary G remains R_0^q!=0.
The full H,S,m values are unchanged by this exact substitution.
If the original P is irreducible and nontorsion, the base has those properties; the actual original/base degrees are2dq and2d, trace degrees dq and d, and common nonzero trace-value norms retain the powers q and2q in the original trace and full fields respectively.
No irreducibility ascent is asserted.

This is a necessary-and-sufficient interface for the restricted ALGEBRAIC first-bit sign problem, together with an explicit necessary support obstruction.
It asserts neither that one of the three systems is solvable nor that all are inconsistent for an actual complete representative.
Actual source parity, matrix ranks, a passing sign choice, original irreducibility and higher residual precision remain separate unresolved questions.
No passing irreducible height1 realization of the full C691 source or characteristic-zero solution is supplied.

## Complete argument

### Full input and the original reciprocal polynomial

Fix ell>=82, Q=2^ell, m=Q/4-2 and a_exp=2m=Q/2-4.
Choose ONE actual complete Y furnished by C691 DG1--DG8, retaining its full whole-factor H and B=X^(Q-m)H(chi), both forward divisibilities, all multiplicities, finite jets and fresh exact triple factor.
Here phi=X^2+X+1, chi=X phi^2, Psi=phi(chi), and H is exactly the complete W_(n_-)^(k_m)W_3^(b_m) from C691, with its stated parameters and costs.
The letter a_exp is the source exponent, distinct from the actual canonical polynomial a(T).
Keep the full binary polynomials

    H_0=X^(2m)Y, U_0=H_0 phi^(14m),
    R_0=H_0 phi^(12m)B,
    C_00=X^(2m)Y(chi)Psi^(14m),
    d=deg U_0=30m+deg Y,
    Pbar_0(z)=z^d U_0(z+z^(-1)).                  (HS1)

The symbol R_0 continues to mean the CANONICAL binary G from C691, never the original reciprocal polynomial Pbar_0.
The original polynomial has full degree2d, constant1 and reciprocal symmetry.
At a raised source q=2^k it is Pbar_0^q, with full original degree2dq.
The full costs remain

    deg Y<=14400Q^3+1206Q^2+120Q,
    d<=14400Q^3+1206Q^2+128Q,
    deg R_0=26m+deg Y+deg B,
    d-deg R_0=m-8-5deg H>5m/256.                 (HS2)

No factor or original multiplicity is discarded.
Different permissible choices of Y can have different full coefficient supports; this interface does not pretend the finite class alone specifies one such support.

The polynomial Pbar_0 is nonsquare, but this does NOT follow from trace nonsquareness alone.
For x=z+z^(-1), formal differentiation in the Laurent ring gives

    Pbar_0'(z)=z^(d-1)[(d modulo2)U_0(x)+x U_0'(x)].

The trace substitution is injective, as seen from the largest Laurent exponent of a nonzero polynomial in x.
If d is even, a zero derivative would imply U_0'=0, contradicting C691's fresh factor of exact multiplicity3 and consequent nonsquareness.
If d is odd, it would imply U_0+XU_0'=0, so U_0 would have only odd-degree nonzero terms.
But its lowest nonzero term is X^(2m), with coefficient1 because Y(0)=phi(0)=1, and2m is even.
This also contradicts a zero derivative.
Thus Pbar_0 is nonsquare and Pbar_0^q has actual maximal Frobenius power q.

### Every allowed height1 sign and its monic trace conversion

Write the ACTUAL complete reciprocal coefficient support uniquely as

    Pbar_0=z^(2d)+1
       +sum_(j=1)^(d-1) p_j(z^(d+j)+z^(d-j))
       +p_0 z^d, p_j in F_2.

Take p_j in{0,1} for the positive integer lift.
The Chebyshev identity gives the unique monic integer trace

    T_+=C_d+sum_(j=1)^(d-1) p_j C_j+p_0,
    P_+(z)=z^d T_+(z+z^(-1)).

Every C_j for j>=1 has even constant term, so p_0=U_0(0)=0 for THIS complete source.
For a general binary reciprocal source one must retain the central constant sign; it is absent here only by this proved zero coefficient.
Every height1 monic reciprocal integer lift with constant1 is exactly

    T_epsilon=T_+-2V_epsilon,
    V_epsilon=sum_(j=1)^(d-1) epsilon_j p_j C_j
                      +epsilon_0 p_0,
    epsilon_j in{0,1},
    P_epsilon(z)=z^d T_epsilon(z+z^(-1)).         (HS3)

Indeed each supported paired coefficient must be+1 or-1, each unsupported coefficient must be0, and the monic and reciprocal endpoint coefficients are both fixed at1.
There is no endpoint sign variable.
Conversely every displayed choice has precisely those properties and H(P_epsilon)=1.
Put I={j:1<=j<d,p_j=1}; for this source the allowed binary trace directions form

    V_space=span_(F_2){C_jbar:j in I},
    dim V_space=|I|,                              (HS4)

because these polynomials have distinct monic degrees below d.
This is the actual allowed sign space, not all of F_2[X]/U_0.

### Exact canonical carry with the changing divisor retained

For any monic integer T put

    Delta(T)=[T(C_2)-T^2]/2 in Z[X].

Integrality follows from C_2=X^2-2 and T(X^2)=T(X)^2 modulo2.
Actual monic division gives a(T)=rem_T Delta(T): the term T^2 has zero remainder, and the remaining numerator is exactly twice Delta(T).
For T_epsilon=T_+-2V_epsilon the integer identity is

    Delta(T_epsilon)=Delta(T_+)-V_epsilon(C_2)
                         +2T_+V_epsilon-2V_epsilon^2.

Reduction commutes with monic remainder, and T_epsilonbar=U_0 for every sign choice.
Consequently, with alpha=rem_(U_0)(Delta(T_+)bar),

    a(T_epsilon)bar
       =alpha+rem_(U_0)(V_epsilonbar^2).          (HS5)

The factor2 was divided in Z[X] before binary reduction.
This proves the complete changing-divisor carry rather than replacing the permitted signs by arbitrary residue coordinates.
For p=3,5 the odd integer division is invertible modulo2 and gives the fixed binary quotients

    b(T_epsilon)bar=rem_(U_0)U_0(X^3+X)=0,
    c(T_epsilon)bar=rem_(U_0)U_0(chi)=:c_0,
    G(T_epsilon)bar=c_0^3=R_0!=0.                (HS6)

Here and below powers inside the quotient mean actual polynomial powers followed by the full monic remainder.
C691 gives the first divisibility, the displayed canonical R_0, and deg R_0<d; its full nonzero binary G is preserved for EVERY sign choice.
Moreover

    U_0(chi)=phi^(4m) C_00,
    H_0 divides C_00,
    C_00 is a phi-unit.

The first identity follows by expanding chi^(2m), the second from Y|Y(chi), and the unit assertion follows from C691 DG6.
Thus c_0 vanishes on the full H_0 component, not merely on its root set.

### All primary components reduce to exactly three affine targets

Let A_0=F_2[X]/U_0 and write v=a(T_epsilon)bar in A_0.
For either original sign s=1 or-1, both residuals vanish modulo2 exactly when

    v^5=0, v^3=c_0^3 in A_0.                    (HS7)

The second equation already implies the first on this source.
To prove this and obtain the precise targets, factor the FULL H_0 as product_f f^(e_f), over its monic irreducible factors, and define

    H_third=product_f f^(ceil(e_f/3)),
    M=H_third phi^(6m).                           (HS8)

At each f|H_0, c_0=0 modulo f^(e_f), so v^3=c_0^3 is equivalent to v divisible by f^(ceil(e_f/3)).
This implies v^5=0 on that entire primary component.
All e_f are at least2; in particular the fresh exact triple factors remain present in H_third with exponent1.

At phi, c_0 has exact order4m and c_0^3 has exact order12m<14m, because C_00 is a unit.
Hence v^3=c_0^3 modulo phi^(14m) forces v to have exact phi-order4m.
Writing v=phi^(4m)w reduces that equation to

    w^3=C_00^3 modulo phi^(2m),
    w=zeta C_00 modulo phi^(2m),
    zeta^3=1 modulo phi^(2m).

There are exactly three such zeta.
Indeed the residue unit group F_4^* has three cube-one elements, while the principal-unit group modulo phi^(2m) has2-power order, so its cube map is bijective.
For completeness, on that finite abelian2-group choose an integer inverse to3 modulo its order; exponentiation by that inverse is the inverse cube map, establishing existence and uniqueness in each residue class.
Equivalently the three choices are the reductions of1,beta,beta^2 from C691 DG6; its beta is specified to the larger precision16m.
Therefore the exact phi constraint is

    v=phi^(4m)zeta C_00 modulo phi^(6m).          (HS9)

It also implies v^5=0 modulo phi^(14m), since20m>=14m.
This proves the claimed implication and retains every original primary exponent.

For each of the three zeta, let t_zeta be the unique degree<deg M representative given by the coprime CRT conditions

    t_zeta=0 modulo H_third,
    t_zeta=phi^(4m)zeta C_00 modulo phi^(6m).

Then the simultaneous first residual bit is equivalent to ONE of the three exact linear systems

    sum_(j in I) epsilon_j rem_M(C_jbar^2)
                    =t_zeta+rem_M(alpha)
                    in F_2[X]/M.                (HS10)

Every column is a permitted original paired-coefficient sign; the center and both endpoints have been accounted for explicitly.
The equivalence is necessary and sufficient for the ALGEBRAIC first-bit sign problem, not just a local necessary test.
It does not assert that any of the three right sides belongs to the span of the displayed columns.
No irreducibility, nontorsion or higher-residual conclusion follows merely from a solution of these systems.

Their coefficient matrices have deg M rows and |I| columns over F_2.
Since every e_f>=2, ceil(e_f/3)<=e_f/2, and hence

    deg M=deg H_third+12m<=13m+(deg Y)/2,
    |I|<=d-1,
    deg M<=7200Q^3+603Q^2+64Q.                   (HS11)

The final bound uses13m<13Q/4 and the full C691 bound on deg Y; the phi^(6m) component has degree12m because deg phi=2.
This is only a conservative dimension bound, not an efficient algorithm or a computed rank.
The same complete Y determines both these columns and the carry alpha, so they cannot be chosen independently.

<a id="height-one-zero-trace-support-obstruction"></a>
### A concrete support obstruction and its dyadic-coefficient form

Let w be the number of NONZERO coefficients of the full binary reciprocal Pbar_0.
Because p_0=0,

    w=2+2|I|.

Every allowed V_epsilonbar vanishes at X=0, so HS5 shows that the constant value of a(T_epsilon)bar is independent of every sign choice.
Since T_+(0) is even,

    alpha(0)=Delta(T_+)(0) modulo2
       =[T_+(-2)-T_+(0)^2]/2 modulo2
       =1+|I|=w/2 modulo2.                       (HS12)

Here C_j(-2)=2(-1)^j, and the square T_+(0)^2 is divisible by4.
Passing to remainder modulo U_0 does not change this constant value because U_0(0)=0.
The required equation v^3=c_0^3 at the X-primary component forces v(0)=0.
Thus

    w=0 modulo4                                  (HS13)

is a NECESSARY condition for any allowed height1 lift to pass even the first simultaneous residual bit.
In HS10 it is an explicit zero-row obstruction: every allowed column has zero constant coefficient, while the right side has constant w/2 modulo2.
If the actual full source has w=2 modulo4, all of its height1 sign lifts fail this first bit; no such parity has been asserted for the chosen C691 representatives.

There is an equivalent test using only selected coefficients of the trace polynomial:

    w/2 modulo2
       =sum_(h>=0) [X^(2^h)]U_0 in F_2.          (HS14)

To prove it, define the finite linear functional Lambda(f)=sum_(h>=0)[X^(2^h)]f.
For j=2^t v with v odd, the trace identities give C_jbar=C_vbar^(2^t).
The odd C_v has only odd-degree monomials, and its linear coefficient is1 modulo2.
The last assertion also follows directly by differentiating C_(n+1)=XC_n-C_(n-1) at0: every even C_n(0) is even, so all odd-index derivatives at0 agree modulo2 with C_1'(0)=1.
Thus the ONLY positive2-power monomial contributing to Lambda(C_jbar) is X^(2^t), with coefficient1.
Hence Lambda(C_jbar)=1 for every j>=1.
Applying this to the full expansion U_0=C_dbar+sum_(j in I)C_jbar proves HS14.

All terms below exponent2m=Q/2-4 vanish.
Since ell>=82, the first possible positive2-power exponent is Q/2, and its contribution is

    [X^(Q/2)]U_0=[X^4](Y phi^(14m)).

DG3 gives the further exact expression

    [X^4](Y phi^(14m))=[X^2]H^(-1).             (HS15)

Indeed Y=phi^(-14m)H^(-2)h_Q(x)^(-2) modulo X^(8m), so Y phi^(14m)=H^(-2)h_Q(x)^(-2) at that precision.
The first possible nonconstant term of h_Q(x) has order Q/2, since x has order1 and leading coefficient1, and its inverse square is1 modulo X^Q.
Taking coefficient X^4 and then the characteristic-two square root gives HS15.
The full parity in HS14 still includes EVERY later positive2-power exponent through deg U_0; HS15 alone does not decide it.
There are at most floor(log_2 d)+1 selected coefficient queries, with d bounded in HS2, but no low computational cost for extracting those coefficients from the full representative is asserted.
Neither their values nor the final parity have been evaluated here.

### Exact descent of every height1 ascent and the remaining obligation

Let q=2^k and let P be any monic reciprocal integer polynomial with constant1, H(P)=1 and binary reduction Pbar_0^q.
Its nonzero integer support equals its binary support, all of whose indices are divisible by q.
Consequently P=Q_int(z^q) for a unique actual height1 monic reciprocal integer polynomial Q_int of degree2d and binary reduction Pbar_0.
The proved nonsquareness of Pbar_0 makes q the maximal actual dyadic composition exponent as well.
Thus Q_int is exactly one of the sign lifts HS3, and its trace is the corresponding T_epsilon.
The actual original trace is T_epsilon(C_q), and C724's all-six exact covariance preserves EVERY residual coefficient order and the nonzero binary canonical G=R_0^q.
Therefore algebraic first-bit feasibility at ANY q is exactly HS10 on this SAME base; increasing q adds no sign variables or first-bit choices.
Conversely any base sign solution supplies height1 reciprocal polynomial solutions at every q by substitution, with no assertion that these ascents are irreducible.

If the original P is irreducible and nontorsion, those properties descend to Q_int by the adopted C724 argument; they are additional requirements beyond HS10.
For every actual polynomial in this substitution, its true circle supremum and full logarithmic Mahler measure equal those of the base, with all q roots in each original fiber counted.
If the original and base are irreducible, the actual full degrees are2dq and2d and the trace degrees are dq and d; every common nonzero trace value has original trace norm equal to the base trace norm to the q-th power, and original full-field norm equal to that base trace norm to the2q-th power.
No total-reality assumption or degree-normalized measure replaces these exact expenses.

The useful result is the complete finite linear interface and the concrete necessary parity obstruction, with exact original support and source costs.
The unresolved input is an actual full Y for which one of the three restricted right sides is proved to lie in the allowed-column span, or a proof that it does not, followed by the genuinely separate irreducibility and higher-precision obligations if it does.
Neither an arbitrary trace lift, a selected root set, the local existence of all three cube-root branches nor the q>=2 square-input theorem of C672 settles this restricted nonsquare-base sign problem.
No height1 lift of the full C691 source has been constructed or excluded by the present work.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision height-one-sign-interface-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T18:11 |
| status | open |
| reason | Register the complete HS1--HS15 and exact-descent author argument after both contributors read its whole scope. The complete C691 source yields exactly three restricted sign systems, an actual support/dyadic-coefficient parity obstruction and honest full degree/norm/measure costs. No source parity, matrix rank, feasible sign vector, irreducibility ascent or higher-precision realization is inferred. Fresh isolated whole review and a separate acceptance decision remain outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full restricted-sign, parity and descent statement](#statement) | Every actual complete C691 Y, all s>=82 and q=2^k, exact allowed signs and canonical carry, all primary components and three targets, corrected matrix dimension, support/dyadic parity, original nonsquareness and exact height1 descent, with full norm/degree/analytic costs and all unresolved feasibility limits. |
| argument | [Complete HS1--HS15 and descent proof](#complete-argument) | Original reciprocal derivative and parity cases, central/endpoints and monic trace basis, integer Delta carry, all full-primary cubic constraints and cube-one branches, restricted linear equivalence, support functional and DG3 coefficient expression, every actual ascent and field-norm multiplicity. |
| dependency | [Adopted complete canonical source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 complete H,B,Y and both forward divisibilities, low/high finite jets, C_00 unit and full canonical R_0 identity, all multiplicity floors and fresh exact triple factor, maximal Frobenius and complete degree/gap costs. HS15 uses the actual DG3 formal low unit and HS9 uses DG6 cube-one units at the stated precisions. No higher integer residual or irreducible realization is imported. |
| dependency | [Adopted height1 descent and all-six exact covariance](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | HD10--HD13 support-based exact descent only after proving THIS reciprocal binary base nonsquare, all-six canonical covariance and exact coefficient orders, unchanged H/S/full measure, irreducibility/nontorsion descent and retained original q/2q norm multiplicities. No sign choice, irreducibility ascent or passing-certificate existence is imported. |
| dependency | [Adopted integer canonical interface](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) | Actual integral divided monic remainders and exact canonical composition; the first-quotient changing-divisor carry is proved explicitly by Delta here. |
| support | [Square-input construction and its exact domain](Yin_C_G0672_v1.md#decision-whole-reviewed-2026-10-24) | Boundary comparison only: q>=2 square-input solvability does not supply unrestricted signs or a q1 nonsquare-base theorem after height1 descent. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T18:23 |
| status | proved |
| reason | Adopt the complete HS1--HS15 and exact-descent interface after the fresh independent whole height-one finding in R952 passed. Root read the entire integrated author proof, reread the consumed full C691 scope, checked the fixed standalone statement and read the full independent finding. The source exponent was renamed ell to distinguish it from the residual sign s; the same independent reviewer confirmed this is only alpha-renaming and retains the whole verdict. The exact allowed sign space, genuine canonical carry, all full primary constraints, three restricted affine systems, complete matrix costs, necessary support parity and exact dyadic descent are supported. Actual full-source parity, ranks, a sign solution, irreducibility and higher precision remain unresolved. No arbitrary trace freedom, source truncation, passing height1 realization or unrestricted G0001 completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full restricted-sign, parity and descent statement](#statement) | Every actual complete C691 Y, all s>=82 and q=2^k, exact allowed signs and canonical carry, all primary components and three targets, corrected matrix dimension, support/dyadic parity, original nonsquareness and exact height1 descent, with full norm/degree/analytic costs and all unresolved feasibility limits. |
| argument | [Complete HS1--HS15 and descent proof](#complete-argument) | Original reciprocal derivative and parity cases, central/endpoints and monic trace basis, integer Delta carry, all full-primary cubic constraints and cube-one branches, restricted linear equivalence, support functional and DG3 coefficient expression, every actual ascent and field-norm multiplicity. |
| dependency | [Adopted complete canonical source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 complete H,B,Y and both forward divisibilities, low/high finite jets, C_00 unit and full canonical R_0 identity, all multiplicity floors and fresh exact triple factor, maximal Frobenius and complete degree/gap costs. HS15 uses the actual DG3 formal low unit and HS9 uses DG6 cube-one units at the stated precisions. No higher integer residual or irreducible realization is imported. |
| dependency | [Adopted height1 descent and all-six exact covariance](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | HD10--HD13 support-based exact descent only after proving THIS reciprocal binary base nonsquare, all-six canonical covariance and exact coefficient orders, unchanged H/S/full measure, irreducibility/nontorsion descent and retained original q/2q norm multiplicities. No sign choice, irreducibility ascent or passing-certificate existence is imported. |
| dependency | [Adopted integer canonical interface](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) | Actual integral divided monic remainders and exact canonical composition; the first-quotient changing-divisor carry is proved explicitly by Delta here. |
| support | [Square-input construction and its exact domain](Yin_C_G0672_v1.md#decision-whole-reviewed-2026-10-24) | Boundary comparison only: q>=2 square-input solvability does not supply unrestricted signs or a q1 nonsquare-base theorem after height1 descent. |
| review | [Fresh independent whole height-one finding](../audits/reviews/Yin_R_G0952_v1.md#whole-height-one-interface-finding) | Entire fixed statement and HS1--HS15/descent argument, all allowed signs and actual carries, complete primary constraints and three affine systems, exact dimension/parity and reciprocal descent, full analytic/norm costs and unresolved feasibility boundaries; source-index alpha-renaming separately confirmed. |

