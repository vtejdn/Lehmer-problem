---
author: Yin
---
# One coupled dyadic lift of actual divided trace remainders

Date: 2026-10-20T17:03.
The complete author proof began at2026-10-20T17:01; its coupled layer and later same-layer quadratic specialization are retained below.
Human author Yin.
This is one bounded author continuation of the actual-unit inquiry under the [selected retained-draft Task scope](../tasks/Yin_T_G0001_v1.md#decision-resume-retained-draft-inquiries-2026-10-20).
Its author draft was D37 at the stated original date; that address is extraction provenance, not a logical input.
Root supplied the coupled lift proposal, the two obstruction conditions and the proposed rank formula.
Root also proposed the quadratic-primary specialization; its exact dyadic-quotient order is already supplied by the adopted C197v3 QX6, as reused below.
The retained_methods_audit author reconstructed the full changing-divisor identity, coefficient precision, coupled residual changes, all kernel and representative boundaries and the application limitations below.
The b3_strategy_critique assignment supplied strategic priority and scope limits, not an independent review of this proof.
The scope is ONLY T_1=T_0+8V and the passage of both canonical residuals from coefficientwise divisibility by4 to divisibility by8.
There is no higher-modulus iteration, parameter scan, mathematical program or original-input construction.
The endpoint optimization round is not continued.

<a id="responsible-question"></a>
## Precise question and existing-material reuse

The desired finite test must use the SAME coefficient correction V for both original divided-remainder residuals.
Choosing two unrelated residual corrections, free quotient coordinates or a free G would not test the actual input map.
[The generic half-difference interface in C196v3](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) already proves integrality and the dependence of theta_2 mod2 on T mod4; it is not a theorem for this next coupled layer.
[C197v2's retained correction mechanism](Yin_C_G0197_v2.md#retained-intermediate-mechanisms) treats a prescribed degree30 support, and [C197v3](Yin_C_G0197_v3.md#statement) proves generalized quadratic-primary necessary conditions modulo4.
Those results do not supply an all-monic mod4-to-mod8 existence criterion for a fixed T mod8.
[The complete C199v4 gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) has the narrower actual-field, zero-Haar and unique-unsaturated domain and retains original integer cyclotomic layers.
No equivalence between its entire gate and the new coefficient obstruction is assumed.

<a id="statement"></a>
<a id="coupled-layer-statement"></a>
## Exact generic finite theorem

Let r>=1, let T_0 in Z[X] be monic of degree r, and fix s in{1,-1}.
No irreducibility, total reality, reciprocal original polynomial, nonzero quotient value or zero-Haar condition is imposed.
For every monic T of degree r define, by actual monic integer division,

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    theta_p(T)=rem_T(T(C_p))/p, p=2,3,5,
    G(T)=rem_T(theta_5(T)^3-2theta_3(T)^5),
    F(T)=rem_T(2theta_5(T)^2-3theta_2(T)^5),
    X_s(T)=rem_T(theta_3(T)^2-theta_2(T)^3
                     +s(theta_5(T)^3-2theta_3(T)^5)). (CL1)

All theta_p are integer polynomials of degree less than r, as proved below; every other displayed remainder also has degree less than r.
Assume every coefficient of F(T_0) and X_s(T_0) is divisible by4.
Put

    U=T_0 mod2, B=F_2[X]/(U),
    a=theta_2(T_0) mod2 in B,
    O_F=(F(T_0)/4) mod2 in B,
    O_X=(X_s(T_0)/4) mod2 in B.                      (CL2)

Division by4 here takes place in the integer coefficient module BEFORE reduction; it is not division by a zero divisor in B.
For an integer polynomial V with deg V<r set T_1=T_0+8V and v=V mod2 in B.
The distinct v in B correspond exactly to the2^r monic coefficient classes T_1 mod16 above the fixed class T_0 mod8.
Let Fr(aB)={z^2:z in aB}, the image of squaring on the actual ideal aB, regarded as an F_2-vector subspace of B.
Then

    exists v in B with F(T_1)=X_s(T_1)=0 mod8
      iff O_X in Fr(aB) and O_F=a^2 O_X in B.         (CL3)

For such a solution, every integer representative of v gives the same two congruences.
If U=product_psi psi^(N_psi), with all distinct monic irreducibles retained, put

    t_psi=min(N_psi,ord_psi a),
    rho=sum_psi deg(psi)*max(ceil(N_psi/2)-t_psi,0).   (CL4)

Here ord_psi0=infinity and a is any polynomial representative of its class; the truncated order t_psi is independent of that choice.
When (CL3) holds, exactly2^(r-rho) classes v solve it; otherwise none do.
This is a fiber count for the ACTUAL fixed errors, not a probability or a claim that errors are independently or uniformly distributed.
The criterion is invariant under choosing a different base representative T_0+8W of the same monic class modulo8, with the precise error and solution translations proved below.

Under the additional complete support hypothesis

    U=X^A phi^N product_i Q_i^(B_i),
    phi=X^2+X+1, A>=2, N>6A, B_i>=2,

where all exponents are integers and the Q_i are all distinct remaining monic irreducibles over F_2, different from X and phi, the adopted C197v3 input gives N=7A, A even and ord_phi a=2A.
On B_phi=F_2[X]/(phi^(7A)), the first correction vanishes identically, the local rank is3A, and the local simultaneous criterion is precisely

    O_F=0, O_X in phi^(4A)Fr(B_phi).

Every other primary component must still pass the generic criterion.
These are additional support hypotheses and a necessary one-layer interface, not an exclusion or realization of C199's full original-input gate.
The complete specialized proof and its boundary are in Section5.

<a id="argument"></a>
## Complete proof

<a id="integrality-and-changing-divisor"></a>
## 1. Integrality, monic division and the full changing-divisor term

For p=2,3,5, the displayed polynomials satisfy C_p congruent X^p modulo p.
For any monic integer T, reduction modulo p gives T(C_p) congruent T(X)^p.
Monic division over Z has integer quotient and remainder, and its coefficient recursion commutes with reduction modulo any integer modulus.
The remainder of T(X)^p on division by T is zero, so rem_T(T(C_p)) has every coefficient divisible by p.
This proves the integrality claimed in (CL1), including reducible, repeated-root and constant-term-zero T.
This is the elementary generic interface already retained in C196/C197, rederived here to state the present domain completely.

More generally, monic division of a fixed-degree numerator depends polynomially with integer coefficients on the numerator coefficients and lower divisor coefficients.
This follows directly by repeatedly subtracting the leading numerator coefficient times a monomial multiple of the monic divisor.
Thus congruent numerator and monic divisor coefficients give congruent canonical remainders.
No root selection, separability or field extension is involved.

Write the EXACT integer division for T_0 at the dyadic prime as

    T_0(C_2)=T_0 Q_0+2theta_2(T_0).                  (CL5)

The polynomial Q_0 is monic of degree r.
Substitute T_1=T_0+8V and use linearity of composition in the coefficients of T:

    T_1(C_2)
      =T_1 Q_0+2theta_2(T_0)
                       +8[V(C_2)-VQ_0].

Taking the remainder modulo T_1 preserves theta_2(T_0), since its degree is less than r.
Consequently the exact integer identity is

    theta_2(T_1)=theta_2(T_0)
                    +4 rem_(T_1)[V(C_2)-VQ_0].      (CL6)

This retains the term -VQ_0 caused by changing the divisor.
It has not been replaced by composition alone before monic reduction.
Reducing (CL5) modulo2 gives U Q_0bar=U(X^2)=U^2 in the polynomial domain F_2[X].
Since U is nonzero and monic, polynomial cancellation yields Q_0bar=U.
This cancellation occurs in F_2[X], not in the zero-divisor algebra B.
If h=rem_U(v^2) denotes the unique representative of the square of v of degree less than r, (CL6) therefore gives the coefficientwise congruence

    theta_2(T_1)=theta_2(T_0)+4h mod8.               (CL7)

Indeed V(C_2)bar=v(X^2)=v^2, and the other term is vU, which vanishes modulo U.
An arbitrary integer lift of h can be used in the last equation.

For p=3,5, numerator and divisor reduction modulo8 are unchanged, so
rem_(T_1)(T_1(C_p)) congruent rem_(T_0)(T_0(C_p)) modulo8.
Both remainders are divisible by p in Z[X], and p is invertible modulo8, hence

    theta_3(T_1)=theta_3(T_0) mod8,
    theta_5(T_1)=theta_5(T_0) mod8,
    G(T_1)=G(T_0) mod8.                              (CL8)

The last assertion uses the same monic-division compatibility and concerns the canonical polynomial, coefficient by coefficient.
It is not only an equality of values at a selected root.

<a id="coupled-error-map"></a>
## 2. The simultaneous error map

Since T_1 congruent T_0 modulo8, the two quotient rings modulo8 share their monic coordinate basis1,X,...,X^(r-1).
For residual differences modulo8 one may therefore reduce using either divisor.
For n=3 or5 the integer binomial expansion gives

    (theta_2(T_0)+4h)^n
        =theta_2(T_0)^n+4n theta_2(T_0)^(n-1)h mod8,

because every term involving at least two factors4h is divisible by16.
Combining this with (CL8) gives the coefficientwise canonical congruences

    F(T_1)-F(T_0)=4 rem_U(a^4 v^2) mod8,
    X_s(T_1)-X_s(T_0)=4 rem_U(a^2 v^2) mod8.          (CL9)

For the first equation -3*5=-15 is1 modulo2, and for the second -3 is1 modulo2 after the common factor4 is removed.
The sign s disappears from the correction because the entire G term is unchanged modulo8; O_X itself still depends on the actual s and T_0.
Monic division of4 times an integer polynomial commutes with multiplication by4, so passing from its reduction modulo8 to the remainder modulo U in (CL9) is legitimate.

The assumed divisibility by4 of both old remainders and (CL9) prove the same divisibility for both new remainders.
Dividing their integer coefficients by4 and then reducing modulo2 gives the exact errors

    O_F(T_1)=O_F+a^4 v^2,
    O_X(T_1)=O_X+a^2 v^2 in B.                       (CL10)

A canonical integer remainder divisible by4 is divisible by8 exactly when its divided coefficients vanish modulo2.
Equivalently its divided class is zero in B, since its canonical degree is less than r.
Therefore simultaneous success means

    O_X=(av)^2,
    O_F=a^2(av)^2.                                  (CL11)

The first equation is solvable exactly when O_X lies in Fr(aB).
Under it the second holds exactly when O_F=a^2O_X.
This proves both directions of (CL3), with the SAME v for both equations.
No independent choices of two corrections have been introduced.

<a id="frobenius-rank-and-boundaries"></a>
## 3. Exact rank, fibers and nilpotent boundaries

The map

    L:B->B, v |-> (av)^2=a^2v^2

is F_2-linear, as is the full paired map v |-> (a^2L(v),L(v)).
The second coordinate makes their kernels equal and their ranks identical.
CRT decomposes B as the product of B_psi=F_2[X]/(psi^(N_psi)), independently of whether U is squarefree.
On one component write N=N_psi, n=deg psi and t=min(N,ord_psi a).
If v has truncated order j, then (av)^2 vanishes in this component exactly when

    t+j>=ceil(N/2).

Thus the local kernel is the ideal

    psi^k B_psi, k=max(ceil(N/2)-t,0),

of F_2-dimension n(N-k).
One may see this dimension directly from the multiples of psi^k of degree less than nN; it uses no choice of coefficient field or unjustified residue-field linearity of squaring.
The image rank is therefore nk, and summing over CRT proves (CL4).
Every nonempty fiber of L is a coset of its kernel and has2^(r-rho) elements.
The relation O_F=a^2O_X then makes it the complete paired fiber as well.

If a=0 on a component, take t=N; the correction map there is zero, and BOTH errors must already be zero there.
If t>=ceil(N/2), the same zero-map conclusion holds even when a is nonzero and nilpotent.
If a is a unit on a component, the abstract rank formula gives n ceil(N/2), including squarefree N=1, where Frobenius on the finite residue field is bijective.
There is no inference that the nilpotent ring's full squaring map is surjective when N>1.

Under the ACTUAL base assumption F(T_0)=0 mod4, its reduction modulo2 already gives a^5=0 in B.
Consequently every nonzero local component has t>=ceil(N/5), and a unit component cannot occur in this theorem's admissible base data.
The preceding unit discussion checks the general linear-algebra boundary only; it does not claim a compatible residual model with a unit a.
All correction and fiber formulas include arbitrary repeated irreducible factors and the zero a case.
For the optional degree-zero convention T_0=1, the algebra is zero, V=0 is the sole correction, all remainders and errors vanish, the empty rank sum is0, and the count is1.
No original-field interpretation is assigned to that convention.

<a id="base-representative-invariance"></a>
## 4. Actual coefficient precision and base representative changes

The classes U and a depend only on T_0 modulo2 and modulo4, respectively, by (CL6) or the old half-difference interface.
The odd theta_3,theta_5 and G modulo8 depend only on T_0 modulo8.
The dyadic theta_2 modulo8, hence the two errors in (CL2), are determined by T_0 modulo16.
Indeed replacing T_0 by T_0+16W is (CL6) with V=2W, so its dyadic quotient changes by a polynomial divisible by8; the odd quotients and divisors are also unchanged modulo8.
Thus the errors themselves need not be assigned to a single unspecified representative of T_0 modulo8.

Instead, choose a different integer base T_0'=T_0+8W, with deg W<r, and put w=W mod2.
It remains monic of degree r, still satisfies both residual congruences modulo4, and has the same U and a.
Equations (CL9)--(CL10) give

    O_F'=O_F+a^4w^2,
    O_X'=O_X+a^2w^2.                                (CL12)

The obstruction O_F+a^2O_X is unchanged, and the class of O_X in B/Fr(aB) is unchanged.
This proves that the two obstruction tests in (CL3) are independent of the chosen base representative of the fixed coefficient class modulo8.
A correction v' relative to T_0' corresponds to v=w+v' relative to T_0, because
T_0'+8V'=T_0+8(W+V').
This is a bijection on coefficient classes modulo16 and preserves the exact solution count.
No distributional independence of errors is implied by translating their common affine image.

<a id="quadratic-primary-coupled-layer"></a>
## 5. Exact quadratic-primary specialization of the same layer

Add to the generic theorem the ENTIRE reduction hypothesis of C197v3:

    U=X^A phi^N product_i Q_i^(B_i),
    phi=X^2+X+1,
    A>=2, N>6A, B_i>=2,                            (CL13)

where the Q_i are all distinct remaining monic irreducibles, different from X and phi; an empty product is permitted at the statement level.
These are additional hypotheses, not consequences for every arbitrary monic T_0.
The two residual congruences required by that theorem are exactly the coefficientwise-divisibility hypotheses of the present theorem, because canonical monic remainder zero modulo4 is equivalent to membership in(4,T_0).
The adopted [C197v3 generalized proof](Yin_C_G0197_v3.md#quadratic-primary-generalized-root), QX6 and QX9 together with its parity argument, gives

    N=7A, A even,
    ord_phi(theta_2(T_0) mod2)=2A.                  (CL14)

The order assertion is already explicit in QX6: the actual second residual gives theta_2bar^3=theta_5bar^3 of exact order6A<N, so the actual theta_2bar has exact order2A.
It is not inferred for a free nilpotent coordinate, and it does not require a new valuation argument at a selected root.
Its class is the same a used in (CL2), restricted to B_phi=F_2[X]/(phi^(7A)).
Thus a^4=0 in B_phi, since8A>=7A, and

    Fr(aB_phi)=Fr(phi^(2A)B_phi)
               =phi^(4A)Fr(B_phi),
    rho_phi=2(ceil(7A/2)-2A)=3A.                   (CL15)

For the image identity, a has the exact form phi^(2A) times a unit, so aB_phi is precisely the indicated ideal, and squaring the ideal gives the displayed Frobenius image.
The rank calculation uses deg phi=2 and the already established evenness of A.
In this component the first residual correction is identically zero for every v.
The local simultaneous lift criterion therefore reduces exactly to

    O_F=0 in B_phi,
    O_X in phi^(4A)Fr(B_phi).                       (CL16)

Indeed the generic criterion's first condition is the displayed image membership; under it a^2O_X=a^4v^2=0, so its second condition is precisely O_F=0.
Conversely those two local conditions supply the required local correction; the full global test still requires every other primary component.
Merely asking O_X to be divisible by phi^(4A) is weaker than the specified Frobenius-image membership and is not substituted for it.
The local image has dimension3A over F_2, whereas the whole ideal phi^(4A)B_phi has dimension6A.

For the actual unsaturated-quadratic C199 branch, these are necessary coefficient conditions at the original, unnormalized multiplicity A.
They do not silently replace A by the Frobenius-normalized A_0, which need not define a smaller characteristic-zero trace input.
If the exact original residuals are already assumed then O_F=O_X=0 automatically, as explained next.
No proof or counterexample is supplied here deciding whether the earlier modulo4 conditions together with the full normalized necessary C199 gate alone force O_F=0 or the second condition in(CL16).
Thus(CL16) is an accurate necessary interface for this one lift, not an established new exclusion of that branch.

<a id="actual-gate-application-boundary"></a>
## 6. What this does and does not add to the actual canonical G gate

For an original input satisfying the complete exact C199v4 hypotheses, minimality of its actual monic T implies the canonical F(T) and X_s(T) are identically zero in Z[X].
It therefore passes (CL3) with O_F=O_X=0 and the actual unmodified representative v=0.
This observation does not make the proposed test an additional contradiction for an already assumed actual solution.
Its operational use is instead exact: a candidate monic coefficient class modulo8 whose two modulo4 residuals vanish admits a simultaneous modulo8 solution in its next coefficient bit if and only if the two specific tests in (CL3) hold.
Failure excludes every integer lift of that fixed modulo8 class from the exact original residual equations.
Passing retains only the two congruences and no characteristic-zero existence assertion.

This supplies a precise coupled coefficient obstruction missing from the inspected earlier monic interfaces, but no particular C199-compatible class has been proved to fail it.
No independence from, incompatibility with, or strict strengthening of the FULL normalized actual C199v4 gate is established here.
That gate includes actual original-field hypotheses, complete cyclotomic factorization and the original layer multiplicities, not just a formal value of G modulo8.
Although (CL8) fixes the canonical G polynomial modulo8 throughout this correction, it does not preserve its full integer factorization, zero-Haar property, degree, irreducibility of T, real-root pattern or any original polynomial realization.
It also supplies no estimate of the original-root/Haar discrepancy for the unreduced G in C195.
The current bounded result stops at this one coupled layer; it neither prescribes a higher-modulus iteration nor treats V or G as freely realized original inputs.

<a id="exact-inputs"></a>
## Exact inputs and review boundary

The generic coefficient theorem and rank calculation are proved completely here.
The actual primary specialization invokes only the precisely matched adopted C197v3 interface listed below; the other fixed materials supply attribution, comparison or independent upstream evidence.
The new generic statement has a different domain and question from C197's prescribed-support theorem and C199's original zero-Haar theorem, so neither older family is revised.

| Input | Actual role and limit |
| --- | --- |
| [C197v3 generalized-root theorem](Yin_C_G0197_v3.md#quadratic-primary-generalized-root) | Sole external logical input to the primary specialization: QX6's exact ord_phi theta2bar=2A and QX9/parity's N=7A and even A, under the full extra-support and mod4 premises. |
| [C196v3 generic quotient algebra](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Attribution for integral half differences, monic compatibility and dependence on T mod4; the new changing-divisor and coupled next-layer proof is supplied completely here. |
| [C197v2 earlier finite correction](Yin_C_G0197_v2.md#retained-intermediate-mechanisms) | Scope comparison: the earlier degree30 and prescribed-support mod4 correction is not a generic coupled mod8 theorem and supplies no new actual realization. |
| [C199v4 full original gate](Yin_C_G0199_v4.md#statement) | Application comparison only; complete actual residual and cyclotomic hypotheses are not replaced by freely chosen coefficient classes, G residues or correction vectors. |
| [R477 accepted generalized input review](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Existing coverage of all QX steps, with initial review context currently unknown, including the actual QX6/QX9/parity interface; upstream author overlaps remain disclosed there. |

Root and retained_methods_audit are the new mathematical authors; the earlier source authors and review roles remain at their fixed scopes.
The strategic-priority assignment is not a mathematical review.
The complete proof has been author-checked for original polynomial definitions, integrality, changing divisors, actual error precision, rank and all zero/unit/nilpotent cases, base translations and the exact primary specialization.
The candidate awaits a separately arranged noncontributor whole review; no previous review is transferred to it.
No Claim adoption, Task/E decision, shared index, source account or old fixed proof was changed by registration.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-21)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T17:03 |
| status | open |
| reason | Register the complete arbitrary-monic simultaneous mod4-to-mod8 divided-remainder criterion, exact Frobenius rank and fibers, representative invariance and matched quadratic-primary specialization. The original full C199 gate has not been shown incompatible, strengthened or realized; the bounded inquiry stops at this one layer and awaits independent whole review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact finite theorem](#statement) | All arbitrary-monic hypotheses, same correction for both residuals, exact iff and count, primary specialization with complete extra support, and no original-realization or full-gate exclusion assertion. |
| argument | [Complete proof](#argument) | CL1--CL16, integral division and changing divisor, odd/canonical-G stability, paired error map, full rank/fiber and representative proofs, all boundary cases and application limits. |
| dependency | [Exact generalized primary input](Yin_C_G0197_v3.md#quadratic-primary-generalized-root) | Only QX6, QX9 and parity: same actual theta2bar order2A, N=7A and even A under the matched generic mod4/full-support hypotheses. |
| support | [Earlier generic quotient identities](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Known integral half-difference and monic-modulus interface, rederived here with the complete new changing-divisor term rather than assumed at a higher precision. |
| support | [Earlier prescribed finite correction](Yin_C_G0197_v2.md#retained-intermediate-mechanisms) | Existing narrower mod4 correction and nonrealization boundary, not a proof of the new all-monic simultaneous criterion. |
| support | [Full actual canonical gate](Yin_C_G0199_v4.md#statement) | Exact comparison domain and continuing original-field/cyclotomic conditions; no mutable draft or freely chosen G is a premise. |
| support | [Actual generalized input evidence](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Independent QX6/QX9/parity coverage and matched mod4 domain with preserved upstream author relationships; not an independent review of CL. |

### Decision whole-reviewed-2026-10-21

| Field | Value |
| --- | --- |
| date | 2026-10-20T17:16 |
| status | proved |
| authority | Internal adoption within Yin's selected retained-draft inquiries. |
| reason | Adopt the entire actual CL1--CL16 theorem through the complete noncontributor R491 finding: same correction, actual divided integer remainders, full changing-divisor term, paired iff, exact rank and fibers, base invariants and all primary boundaries. The specialized one-layer criterion has not excluded or realized the full actual C199 gate; stop this bounded layer without automatic higher-modulus iteration. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact finite theorem](#statement) | All arbitrary-monic hypotheses, same correction for both residuals, exact iff and count, primary specialization with complete extra support, and no original-realization or full-gate exclusion assertion. |
| argument | [Complete proof](#argument) | CL1--CL16, integral division and changing divisor, odd/canonical-G stability, paired error map, full rank/fiber and representative proofs, all boundary cases and application limits. |
| dependency | [Exact generalized primary input](Yin_C_G0197_v3.md#quadratic-primary-generalized-root) | Only QX6, QX9 and parity: same actual theta2bar order2A, N=7A and even A under the matched generic mod4/full-support hypotheses. |
| support | [Earlier generic quotient identities](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Known integral half-difference and monic-modulus interface, rederived here with the complete new changing-divisor term rather than assumed at a higher precision. |
| support | [Earlier prescribed finite correction](Yin_C_G0197_v2.md#retained-intermediate-mechanisms) | Existing narrower mod4 correction and nonrealization boundary, not a proof of the new all-monic simultaneous criterion. |
| support | [Full actual canonical gate](Yin_C_G0199_v4.md#statement) | Exact comparison domain and continuing original-field/cyclotomic conditions; no mutable draft or freely chosen G is a premise. |
| support | [Actual generalized input evidence](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Independent QX6/QX9/parity coverage and matched mod4 domain with preserved upstream author relationships; not an independent review of CL. |
| review | [Whole coupled-lift finding](../audits/reviews/Yin_R_G0491_v1.md#coupled-dyadic-lift-whole-finding) | Entire actual statement and CL1--CL16 proof, sole dependency and all four supports, precise coefficient and ring operations, every primary and nilpotent boundary, same-correction rank/fibers, representative invariance and original-realization limits; actual upstream author relationships and review scopes retained. |

