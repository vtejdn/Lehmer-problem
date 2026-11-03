---
author: Yin
---
# The normalized unit gate requires an odd multiplicity at an order divisible by five

Human author Yin.
The same_trace contributor derived SG1--SG11 and authored the exact finite certificate under the [current G0001 all-strategy continuation](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
The [D1 author section](../drafts/Yin_D_G0001.md#full-gate-coprime-five-support-certificate) is extraction provenance, not a logical input.
The result fixes a complete support obstruction before an actual monic coefficient test is possible on the proposed coprime15 support family.
It does not decide C624 FE5 independence for the remaining support classes.
The reuse check inspected C199v5's full normalized gate and complete support bridge, C199v2's exact-order group definitions, the previous Mersenne-support failure and the conditional coprime15 construction.
The new target reduction and separating character are not supplied by those earlier interfaces.
The argument uses exact polynomial arithmetic only; the selected assessment owns its separate whole mathematical and native review and adoption.

## Statement


For each odd n>1, let W_n in F_2[X] be the monic product of the distinct traces z+z^(-1) of primitive n-th roots z in an algebraic closure of F_2, one trace for each inverse pair.
Let Y=product_(n odd,n>1,n!=5) W_n^(b_n), where the b_n are nonnegative integers with finite support.
Thus Y is monic and prime to X phi, and the empty product is permitted before the additional conditions below.
Assume the following low-X, unit-root and full normalized gate conditions.
Then there is an odd n>5 with5|n and b_n odd.
The subsequent proof also identifies both exact local target classes and supplies an all-order separating character.
For an original input, the [full C199v5 statement](Yin_C_G0199_v5.md#statement) on its normalized A_0=2 branch supplies precisely this complete-group factorization and these conditions, with b_n its NORMALIZED complete multiplicities.
Write phi=X^2+X+1, chi=X phi^2, Psi=phi(chi), and retain

    Y=1+X^2 modulo X^4,
    H=X^2Y, C=X^2Y(chi)Psi^14, V=X^5Y,
    Z^11=HC^2 modulo phi^6,
    Z(V+C^3)+HV epsilon X^4(X+1)^8 phi^4=0
                                      modulo phi^8, (SG1)

where Z is the unique unit class at that stated precision and epsilon is an arbitrary element of{0,1}.
Evaluate the gate using a chosen unit representative of Z in F_2[X]_(phi).
If it holds for one representative, (SG3) below forces V+C^3 to have order at least4, so every representative of the same class modulo phi^6 gives the same gate modulo phi^8.
In the original C199 application, epsilon is the parity of the ORIGINAL cyclotomic layer exponent a_(k+4), with q=2^k; no individual integer multiplicity is divided by q.
The earlier support condition H^6=C^21 modulo phi^8 remains required.
The question here is whether all complete odd-order groups in the odd-multiplicity part of Y can have order coprime to5.
This includes every support whose entire set of orders is coprime to15 or coprime to5, with arbitrary degree and multiplicities.
It does not assume that a normalized polynomial is realized by a smaller characteristic-zero trace input.

## Argument

### Complete reduction of both parity targets

Since chi has phi-order2, the low-X hypothesis gives Y(chi)=1+X^2phi^4 modulo phi^8.
Also Psi=1+Xphi^2+X^2phi^4, so Psi^2=1+X^2phi^4 modulo phi^8 and Psi^14=1+X^2phi^4 modulo phi^8.
Consequently

    C=X^2 modulo phi^8.                         (SG2)

After substitution of (SG2) and division by the unit X^5, the full gate in (SG1) becomes

    Z(Y+X)=epsilon X^6Y^2(X+1)^8 phi^4
                                      modulo phi^8. (SG3)

It first forces Y=X modulo phi^4.
Modulo phi^4 the root equation is therefore Z^11=X^7.
The identity X^3=1+(X+1)phi gives X^12=1 modulo phi^4, and X^5 satisfies that root equation since55=7 modulo12.
Uniqueness of the eleventh root in this unit group follows directly: its residue lies in F_4^*, where exponent11 is coprime to3, and for1+u with u in(phi), the first nonzero coefficient of (1+u)^11-1 is that of u.
Thus Z=X^5 modulo phi^4.
Furthermore X^8(X+1)^8=(1+phi)^8=1 modulo phi^4.
Dividing (SG3) by Z and using precisely this depth4 information for its phi^4 coefficient yields

    Y=X+epsilon phi^4X^7 modulo phi^8.           (SG4)

Conversely (SG4) together with Y=1+X^2 modulo X^4 gives (SG2), the same Z modulo phi^4, and hence the entire gate (SG3) modulo phi^8.
It also gives the earlier support condition: Y^6=X^6 modulo phi^8 and X^24=1 modulo phi^8, so H^6=X^18=X^42=C^21 there.
Thus both original parity choices have been retained, and (SG4) is equivalent to these full normalized local conditions after the already adopted A_0=2 complement and low-X conclusions.
No whole integer Gamma or canonical monic T is supplied by this equivalence.

### Fixed ambient ring and all-order period

Put

    M=X^4 phi^8=X^20+X^12+X^4,
    R=F_2[X]/M.                                 (SG5)

This ring has dimension20 over F_2 and393216 units, since its CRT components have8 and3*4^7 units.
For odd n>=1 let B_n be the monic trace polynomial of all nonidentity n-th roots of unity in an algebraic closure of F_2, one trace for each inverse pair.
It is defined over F_2 because the complete root set is invariant under Frobenius.
The n-th roots are distinct, and distinct inverse pairs have distinct traces: equal traces are roots of the same quadratic z^2+xz+1.
Thus B_n is squarefree, B_n(0)=1, and phi divides B_n precisely when5 divides n.
The explicit Laurent identity is

    z^((n-1)/2) B_n(z+z^(-1))=(z^n+1)/(z+1).

It proves B_1=1, B_3=X+1 and, by multiplication by z+z^(-1), the recurrence

    B_(n+2)=X B_n+B_(n-2), n>=3 odd.             (SG6)

The substitution F_2[X]->F_2[z,z^(-1)] is injective because the highest positive Laurent exponent of a nonzero polynomial is its degree, so the Laurent calculation establishes the polynomial identity.
For A=[[X,1],[1,0]], the recurrence is advanced by one application of A when n increases by2.
The identities

    A^2=XA+I,
    A^8-I=X^4 A^4,
    A^5-I=phi[phi A+(X+1)I]

are polynomial matrix identities over F_2.
The commuting binomial identity gives A^40=I modulo phi^8, while A^8=I modulo X^4 gives A^40=I there as well.
CRT therefore yields

    A^40=I in M_2(R),
    B_(n+80)=B_n in R for every odd n>=1.        (SG7)

The case n=1 follows by applying A^40 to the initial vector(B_3,B_1); all later cases follow by the same recurrence.
There are exactly32 odd residue classes1<=n<80 with5 not dividing n, and every corresponding B_n is a unit in R.
No upper bound on the actual n or on deg Y has entered this reduction.

### Complete groups and a separating character

Use Omega_n for the complete SET of irreducible exact-order trace factors as in [C199v2](Yin_C_G0199_v2.md#statement), and write W_n=product_(psi in Omega_n)psi for its complete group polynomial.
For odd n>1 the disjoint root partition gives

    B_n=product_(d|n,d>1) W_d.                  (SG8)

When5 does not divide n, every factor in (SG8) is a unit in R.
Induction on n shows that each W_n belongs to the subgroup generated by the allowed B_d: divide B_n by its already treated proper-divisor group factors.
Equivalently the exact divisor inversion is W_n=product_(d|n)B_d^(mu(n/d)), with B_1=1 and the usual squarefree divisor signs; summing those signs over divisors is(1-1)^s for s distinct prime factors.
This supplies the inversion directly without an unproved source theorem.
Conversely each allowed B_n is a product of allowed complete groups by (SG8).
Consequently their generated subgroups in R^* are identical; arbitrary multiplicities and inverse signs are covered because the finite group expresses every inverse as a nonnegative power.
The same subgroup is generated if one additionally requires3 not dividing the actual n: each admissible odd residue modulo80 has a representative n+80k coprime to3, without changing its class by (SG7).

Because M'=0, ordinary differentiation is well-defined on R.
For a unit u define D(u)=u'/u in R and define the F_2-linear functional

    Lambda(f)=[X^13]f+[X^15]f,
    lambda(u)=Lambda(D(u)).                     (SG9)

The coefficients in (SG9) belong to the unique representative of degree below20.
The product and inverse rules prove D(uv)=D(u)+D(v), so lambda is a group homomorphism R^*->F_2.
It vanishes on every square.
The finite certificate verifies

    lambda(B_n)=0 for all odd1<=n<80 with5 not dividing n.
                                                        (SG10)

The exact32 rows below and the [J119 native generation and verification](../computations/programs/Yin_J_G0119/readme.md#results-and-limits) are the complete finite input to this step.
Hexadecimal notation encodes a polynomial by placing its X^j coefficient in bit j.
For each row, multiply its B by its D modulo M and obtain the ordinary derivative of B; B is a unit by the preceding geometric argument, so the displayed D is uniquely B prime divided by B.
Each D has equal X^13 and X^15 coefficients.

| n | B_n modulo M | D(B_n) modulo M |
| --- | --- | --- |
| 1 | 0x00001 | 0x00000 |
| 3 | 0x00003 | 0xff00f |
| 7 | 0x0000d | 0x749d4 |
| 9 | 0x0001d | 0x1a2e4 |
| 11 | 0x00037 | 0xfadfb |
| 13 | 0x00073 | 0xc178f |
| 17 | 0x001d1 | 0x5bb10 |
| 19 | 0x00373 | 0xf4b4f |
| 21 | 0x00737 | 0xb4f4b |
| 23 | 0x00d1d | 0x1bf14 |
| 27 | 0x03707 | 0x8138b |
| 29 | 0x07303 | 0xba9ff |
| 31 | 0x0d101 | 0x5a6e0 |
| 33 | 0x1d101 | 0x34dd0 |
| 37 | 0x73707 | 0xbf40b |
| 39 | 0xd1d0d | 0x40404 |
| 41 | 0xd1d0d | 0x40404 |
| 43 | 0x73707 | 0xbf40b |
| 47 | 0x1d101 | 0x34dd0 |
| 49 | 0x0d101 | 0x5a6e0 |
| 51 | 0x07303 | 0xba9ff |
| 53 | 0x03707 | 0x8138b |
| 57 | 0x00d1d | 0x1bf14 |
| 59 | 0x00737 | 0xb4f4b |
| 61 | 0x00373 | 0xf4b4f |
| 63 | 0x001d1 | 0x5bb10 |
| 67 | 0x00073 | 0xc178f |
| 69 | 0x00037 | 0xfadfb |
| 71 | 0x0001d | 0x1a2e4 |
| 73 | 0x0000d | 0x749d4 |
| 77 | 0x00003 | 0xff00f |
| 79 | 0x00001 | 0x00000 |

No enumerated-subgroup membership assertion is a premise.
Equations (SG7)--(SG8) then give lambda(W_n)=0 for EVERY odd n coprime to5.

The low-X condition and the two possibilities (SG4) determine unique target classes y_0,y_1 in R.
In binary coefficient notation, where bit j is the coefficient of X^j, the finite certificate gives

    y_0=0x70705,
    y_1=0x78f85,
    D(y_0)=D(y_1)=X^15+X^7,
    lambda(y_0)=lambda(y_1)=1.                  (SG11)

Thus neither target belongs to the subgroup generated by all complete groups of order coprime to5.
More generally, if all complete groups of order divisible by5 beyond5 occur with even normalized multiplicity, their square contribution has lambda0, as does every coprime5 group, contradicting (SG11).
Therefore the full normalized A_0=2 gate requires at least one complete group of odd order n>5 with5|n and ODD normalized multiplicity in Y.
This conclusion retains original q and does not assert oddness of any individual original integer cyclotomic exponent.

### Outcome and continuation boundary

The proposed support construction using only orders coprime to15 fails before the actual T coefficient stage, even allowing arbitrary degree, all complete groups, arbitrary multiplicities and both original layer parities.
The same obstruction rules out every Y whose odd-multiplicity groups are all coprime to5.
It does not determine the exact K_T/O_F errors on any surviving full-gate coefficient class and does not decide whether FE5 is independent of that remaining full gate.
Orders divisible by5 beyond5, their complete C3/C5 constraints, every actual Gamma coefficient and the simultaneous same-T residuals remain essential.
No finite seed, original characteristic-zero realization or unrestricted Mahler conclusion is claimed.

## Exact inputs and review scope

| Input | Actual role |
| --- | --- |
| [C199v5 exact normalized gate](Yin_C_G0199_v5.md#statement) | Application only: complete A_0=2 hypotheses, arbitrary original q, low-X coefficients, H/C/V, original layer epsilon, unit-root precision and full local gate. The formal support theorem states these conditions directly and proves its own implication. |
| [C199v5 complete group bridge](Yin_C_G0199_v5.md#normalized-a2-odd-part-and-degree-return) | Application only: Y has complete odd-order groups with their full normalized multiplicities, excluding1 and5; no arbitrary partial orbit or smaller characteristic-zero polynomial. |
| [C199v2 exact-order groups](Yin_C_G0199_v2.md#statement) | Definition and attribution for complete trace groups. The B_n factor partition and divisor inversion needed here are proved directly from the roots. |
| [J119 exact certificate](../computations/programs/Yin_J_G0119/readme.md#results-and-limits) | Native support for all32 explicitly displayed polynomial identities, the recurrence matrix period, both target CRT classes, full local gate checks and separating characters. Separate native arithmetic was authored by the same contributor and is not independent agent review. |

The proof uses no subgroup-size oracle: the32 polynomial identities and explicit character prove nonmembership directly.
The formal conclusion permits arbitrary degrees and multiplicities through the proved80-period and exact complete-group partition, not by extrapolating a finite order scan.
The result retains every original q and leaves the full actual coefficient, Gamma and higher5-order compatibility questions open.
A reviewer must inspect the full target reduction, matrix-period argument, root partition/inversion, logarithmic derivative well-definedness, every certificate row and both targets, plus the exact original-domain application.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T15:37 |
| status | open |
| reason | Register the complete support-obstruction candidate: both exact normalized target jets, all-order80-period, complete-group divisor partition, explicit logarithmic-derivative character and verified32-row native certificate. It excludes the proposed coprime15/coprime5 support family and requires some higher5-order group with odd normalized multiplicity; full-gate FE5 independence and original realization remain unresolved. Await isolated whole mathematical and native review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete formal support theorem](#statement) | Arbitrary finite complete-group product, stated low-X and entire normalized local gate for either parity, odd normalized multiplicity at some odd n>5 divisible by5, and exact original-application boundary. |
| argument | [Complete SG1--SG11 proof](#argument) | Both target reductions and converse, previous support condition, matrix80-period, root factor partition/divisor inversion, well-defined character, all32 displayed identities, both targets and even-multiplicity consequence. |
| dependency | [Original normalized gate and domain](Yin_C_G0199_v5.md#statement) | Only the exact original-input application of the separately stated formal theorem; all original q, root precision and integer layer parity retained. |
| dependency | [Complete original group bridge](Yin_C_G0199_v5.md#normalized-a2-odd-part-and-degree-return) | Only the original application's uniform complete normalized group multiplicities and exclusion of1 and5 from Y. |
| support | [Exact-order trace group definitions](Yin_C_G0199_v2.md#statement) | Existing definition and scope of complete Omega_n sets; new root partition, recurrence and inversion are supplied here. |
| support | [Whole finite native certificate](../computations/programs/Yin_J_G0119/readme.md#results-and-limits) | Every32 generator identity, both target identities, exact matrix period and full local gate checks, with separate author arithmetic verification and no dependence on BFS or an unbounded numerical inference. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T15:53 |
| status | proved |
| reason | Adopt the complete support obstruction, both full local parity targets, all-order80-period and32-row character certificate after the isolated whole R810 review and independently reconstructed native evidence. The conclusion requires odd normalized multiplicity at a higher5-order group; it does not exclude that remaining class or supply actual T, Gamma, FE5 independence or a characteristic-zero realization. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete formal support theorem](#statement) | Arbitrary finite complete-group product, stated low-X and entire normalized local gate for either parity, odd normalized multiplicity at some odd n>5 divisible by5, and exact original-application boundary. |
| argument | [Complete SG1--SG11 proof](#argument) | Both target reductions and converse, previous support condition, matrix80-period, root factor partition/divisor inversion, well-defined character, all32 displayed identities, both targets and even-multiplicity consequence. |
| dependency | [Original normalized gate and domain](Yin_C_G0199_v5.md#statement) | Only the exact original-input application of the separately stated formal theorem; all original q, root precision and integer layer parity retained. |
| dependency | [Complete original group bridge](Yin_C_G0199_v5.md#normalized-a2-odd-part-and-degree-return) | Only the original application's uniform complete normalized group multiplicities and exclusion of1 and5 from Y. |
| support | [Exact-order trace group definitions](Yin_C_G0199_v2.md#statement) | Existing definition and scope of complete Omega_n sets; new root partition, recurrence and inversion are supplied here. |
| support | [Whole finite native certificate](../computations/programs/Yin_J_G0119/readme.md#results-and-limits) | Every32 generator identity, both target identities, exact matrix period and full local gate checks, with separate author arithmetic verification and no dependence on BFS or an unbounded numerical inference. |
| review | [Whole isolated independent finding](../audits/reviews/Yin_R_G0810_v1.md#whole-support-obstruction-finding) | Entire fixed statement and SG1--SG11 proof, every exact selected input and all certificate rows/targets, with actual independent native reconstruction and the original-domain source limits. |

